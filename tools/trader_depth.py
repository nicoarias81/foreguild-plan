#!/usr/bin/env python3
"""Measure how many distinct traders each funded market on Seer actually has.

Why this exists: liquidity is a number the search endpoint hands you, but
"20 distinct traders" — the second half of the binding-futarchy threshold —
is not in it. The per-market PnL leaderboard does expose one row per
address, so it is the honest source: an address counts as a trader only if
its volume is above zero (a row with volume 0 is a liquidity provider or the
creator, not someone who priced the question).

    python3 tools/trader_depth.py             # fresh scan, writes data/*.json
    python3 tools/trader_depth.py --check     # re-reads the dump, no network

Endpoints (public, no key):
    POST https://app.seer.pm/.netlify/functions/markets-search
    GET  https://app.seer.pm/.netlify/functions/get-market-pnl-leaderboard?chainId=100&marketId=0x..
"""
import datetime as dt
import json
import statistics
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

SEARCH = "https://app.seer.pm/.netlify/functions/markets-search"
LEADER = "https://app.seer.pm/.netlify/functions/get-market-pnl-leaderboard"
UA = "Mozilla/5.0 (compatible; foreguild-plan/1.0; +https://nicoarias81.github.io/foreguild-plan/)"
OUT = Path(__file__).resolve().parent.parent / "data"
LIQUIDITY_FLOOR = 50.0   # below this a market has no book worth counting
CHAIN = 100              # Gnosis


def post(url, payload, tries=3):
    body = json.dumps(payload).encode()
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, data=body, headers={
                "content-type": "application/json", "user-agent": UA})
            return json.load(urllib.request.urlopen(req, timeout=90))
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
            if attempt == tries - 1:
                raise
            time.sleep(2 * (attempt + 1))


def get(url, tries=3):
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers={"user-agent": UA})
            return json.load(urllib.request.urlopen(req, timeout=90))
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
            if attempt == tries - 1:
                raise
            time.sleep(2 * (attempt + 1))


def fetch_all(view=None):
    first = post(SEARCH, {"limit": 100, "page": 1, **(view or {})})
    pages = int(first.get("pages") or 1)
    markets = list(first.get("markets") or [])
    for page in range(2, pages + 1):
        markets += post(SEARCH, {"limit": 100, "page": page, **(view or {})}).get("markets") or []
        if view:
            time.sleep(0.3)
    return markets


def fetch_conditional_ids():
    """Seer's own notion of a branch, asked of the server.

    Every market in the unfiltered view carries a parentMarket id, so testing
    for that field marks *all* of them as branches. The conditional view is
    the server's answer to "which markets are branches", and it is a strict
    subset of the board (1,153 of 3,051), so membership is the only usable
    test.
    """
    return {m["id"] for m in fetch_all({"showConditionalMarkets": True})}


def traders(market_id):
    d = get(f"{LEADER}?chainId={CHAIN}&marketId={market_id}")
    rows = d.get("rows") or []
    active = [r for r in rows if float(r.get("volume") or 0) > 0]
    return {
        "ranked": len(rows),
        "traders": len(active),
        "trader_volume_usd": round(sum(float(r.get("volume") or 0) for r in active), 2),
        "top_trader_volume_usd": round(max((float(r.get("volume") or 0) for r in active), default=0.0), 2),
    }


def scan():
    markets = fetch_all()
    branches = fetch_conditional_ids()
    funded = [m for m in markets if float(m.get("liquidityUSD") or 0) >= LIQUIDITY_FLOOR]
    funded.sort(key=lambda m: -float(m.get("liquidityUSD") or 0))
    rows = []
    for m in funded:
        mid = m.get("id")
        try:
            t = traders(mid)
        except Exception as exc:  # one dead market should not kill the scan
            t = {"error": repr(exc)[:120], "ranked": None, "traders": None}
        rows.append({
            "id": mid,
            "name": (m.get("marketName") or "")[:90],
            "conditional": mid in branches,
            "liquidity_usd": round(float(m.get("liquidityUSD") or 0), 2),
            "volume_usd": round(float(m.get("volumeUSD") or 0), 2),
            **t,
        })
        print(f"  {t.get('traders')!s:>4} traders  liq ${rows[-1]['liquidity_usd']:>9,.0f}  {rows[-1]['name'][:50]}")
    good = [r for r in rows if r.get("traders") is not None]
    counts = [r["traders"] for r in good]
    as_branch = [r for r in good if r["conditional"]]
    as_parent = [r for r in good if not r["conditional"]]
    both = [r for r in good if r["liquidity_usd"] >= 3000 and r["traders"] >= 20]
    summary = {
        "markets_scanned": len(rows),
        "markets_with_traders": sum(1 for c in counts if c > 0),
        "markets_at_20_traders": sum(1 for c in counts if c >= 20),
        "markets_at_3": sum(1 for c in counts if c >= 3),
        "max_traders": max(counts) if counts else None,
        "median_traders_all": statistics.median(counts) if counts else None,
        "median_traders_positive": statistics.median([c for c in counts if c > 0]) if any(counts) else 0,
        "total_distinct_address_rows": sum(r.get("ranked") or 0 for r in good),
        "liquidity_floor_usd": LIQUIDITY_FLOOR,
        "branches_in_sample": len(as_branch),
        "parents_in_sample": len(as_parent),
        "branch_traders_median": statistics.median([r["traders"] for r in as_branch]) if as_branch else 0,
        "parent_traders_median": statistics.median([r["traders"] for r in as_parent]) if as_parent else 0,
        "clears_3k_and_20_traders": len(both),
        "clearing_market_ids": [r["id"] for r in both],
    }
    report = {
        "fetched_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "sources": {"search": SEARCH, "leaderboard": LEADER},
        "definition": "a trader is an address whose volume on the market is above zero; "
                      "rows with volume 0 are liquidity or the creator",
        "summary": summary,
        "markets": rows,
    }
    return report


def check():
    files = sorted(OUT.glob("trader_depth_*.json"))
    if not files:
        print("no dump found; run without --check first")
        return 1
    report = json.loads(files[-1].read_text(encoding="utf-8"))
    s = report["summary"]
    markets = report["markets"]
    pinned = [
        ("markets_scanned", s["markets_scanned"], 68),
        ("markets_with_traders", s["markets_with_traders"], 62),
        ("markets_at_20_traders", s["markets_at_20_traders"], 13),
        ("max_traders", s["max_traders"], 50),
        ("median_traders_all", s["median_traders_all"], 9),
        ("branches_in_sample", s.get("branches_in_sample"), 5),
        ("parents_traders_median", s.get("parent_traders_median"), 9),
        ("clears_3k_and_20_traders", sum(1 for m in markets
            if m["liquidity_usd"] >= 3000 and (m.get("traders") or 0) >= 20), 2),
        ("both_are_branches", sum(1 for m in markets if m["liquidity_usd"] >= 3000
            and (m.get("traders") or 0) >= 20 and m["conditional"]), 0),
    ]
    bad = 0
    for name, got, want in pinned:
        ok = got == want
        print(f"  {'OK  ' if ok else 'FAIL'} {name:26} page={want} data={got}")
        bad += 0 if ok else 1
    print(f"\ncheck: {'PASS' if not bad else f'FAIL ({bad} mismatches)'} - {files[-1].name}")
    return 0 if not bad else 1


def main():
    if "--check" in sys.argv:
        return check()
    OUT.mkdir(exist_ok=True)
    report = scan()
    stamp = dt.date.today().isoformat()
    path = OUT / f"trader_depth_{stamp}.json"
    path.write_text(json.dumps(report, indent=1), encoding="utf-8")
    print("\n" + json.dumps(report["summary"], indent=1))
    print("written:", path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
