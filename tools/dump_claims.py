#!/usr/bin/env python3
"""Dump one bounty from the poidh MCP endpoint.

    python3 tools/dump_claims.py --id 1531 --chain base --out data/bounty_1531.json

The host's default resolution for poidh.xyz times out from here (188.114.9x),
while the Cloudflare anycast addresses answer, so the fetch falls back to
pinned IPs before giving up. The dump is the artefact section 00 is counted
from; it carries `_fetched_at` and `_fetch_host` so a stale census is visible.
"""
import argparse
import http.client
import json
import socket
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

PINNED = ["104.21.0.1", "172.67.155.1", "188.114.96.1"]


class PinnedHTTPSConnection(http.client.HTTPSConnection):
    """Connect to a fixed IP but keep the Host header and SNI for poidh.xyz."""

    pinned_ip = None

    def connect(self):
        self.sock = socket.create_connection((self.pinned_ip, 443), timeout=30)
        self.sock = self._context.wrap_socket(self.sock, server_hostname=self.host)


class PinnedHTTPSHandler(urllib.request.HTTPSHandler):
    def __init__(self, ip):
        super().__init__()
        self.ip = ip

    def https_open(self, req):
        conn_cls = type("Conn", (PinnedHTTPSConnection,), {"pinned_ip": self.ip})
        return self.do_open(conn_cls, req)


def rpc(name, args, ip=None):
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                       "params": {"name": name, "arguments": args}}).encode()
    req = urllib.request.Request(
        "https://poidh.xyz/api/mcp", data=body,
        headers={"content-type": "application/json",
                 "accept": "application/json, text/event-stream",
                 "user-agent": "Mozilla/5.0 (compatible; foreguild-census/1.0)"})
    opener = (urllib.request.build_opener(PinnedHTTPSHandler(ip)) if ip
              else urllib.request.build_opener())
    raw = opener.open(req, timeout=45).read().decode("utf-8", "replace")
    if raw.lstrip().startswith("event:") or "\ndata: " in raw:
        raw = "".join(line[6:] for line in raw.splitlines() if line.startswith("data: "))
    payload = json.loads(raw)
    if "error" in payload:
        raise RuntimeError(payload["error"])
    content = payload["result"].get("content") or []
    text = "".join(c.get("text", "") for c in content if c.get("type") == "text")
    return json.loads(text) if text else payload["result"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--id", type=int, required=True)
    ap.add_argument("--chain", default="base")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    last = None
    for ip in [None] + PINNED:
        for attempt in range(2):
            try:
                d = rpc("get_bounty", {"chain": a.chain, "id": a.id}, ip)
                d["_fetched_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
                d["_fetch_host"] = ip or "default-dns"
                out = Path(a.out)
                out.parent.mkdir(parents=True, exist_ok=True)
                out.write_text(json.dumps(d, indent=1, ensure_ascii=False), encoding="utf-8")
                bodies = [len((c.get("description") or "").strip()) for c in d.get("claims", [])]
                print(f"{len(d.get('claims', []))} claims, {len(bodies)} bodies, "
                      f"median {sorted(bodies)[len(bodies)//2] if bodies else 0}, "
                      f"fetched {d['_fetched_at']} via {d['_fetch_host']} -> {out}")
                return 0
            except (urllib.error.URLError, RuntimeError, TimeoutError, OSError, ValueError) as e:
                last = e
    print(f"fetch failed: {last}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
