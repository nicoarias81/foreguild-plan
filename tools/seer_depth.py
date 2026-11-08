#!/usr/bin/env python3
"""Measure Seer market depth from Seer's public API (read-only, no key).

Endpoint documented at https://docs.seer.pm/developers/api:
    POST https://app.seer.pm/.netlify/functions/markets-search  {"limit":100,"page":N}

Writes data/seer_depth_<date>.json with the fields the plan quotes, so every
number in the governance section can be recomputed:
    python3 tools/seer_depth.py

Independent of any other submission's script: this fetches the same public
endpoint, counts markets, and reports liquidity/volume percentiles over the
whole board and over conditional (child) markets separately.
"""
import json
import statistics
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

URL = "https://app.seer.pm/.netlify/functions/markets-search"
UA = "Mozilla/5.0 (compatible; foreguild-plan/1.0; +https://nicoarias81.github.io/foreguild-plan/)"
OUT = Path(__file__).resolve().parent.parent / "data"


def call(body, tries=4):
    for i in range(tries):
        try:
            req = urllib.request.Request(
                URL, data=json.dumps(body).encode(),
                headers={"content-type": "application/json", "User-Agent": UA})
            return json.load(urllib.request.urlopen(req, timeout=90))
        except Exception as exc:  # noqa: BLE001
            if i == tries - 1:
                raise
            print("retry", i, repr(exc)[:120], flush=True)
            time.sleep(3 * (i + 1))


def fetch(view):
    first = call({"limit": 100, "page": 1, **view})
    total, pages = first["count"], first["pages"]
    markets = list(first["markets"])
    for page in range(2, pages + 1):
        markets += call({"limit": 100, "page": page, **view})["markets"]
        if page % 10 == 0:
            print(f"  page {page}/{pages}", flush=True)
        time.sleep(0.35)
    return total, markets


def num(value):
    try:
        return float(value or 0)
    except (TypeError, ValueError):
        return 0.0


def q(values, frac):
    if not values:
        return None
    s = sorted(values)
    return s[min(len(s) - 1, int(frac * len(s)))]


def is_conditional(m):
    parent = str((m.get("parentMarket") or {}).get("id", "")).lower().replace("0x", "")
    return bool(set(parent) - {"0"})


def summarise(markets):
    liq = [num(m.get("liquidityUSD")) for m in markets]
    vol = [num(m.get("volumeUSD")) for m in markets]
    funded = [v for v in liq if v > 0]
    traded = [v for v in vol if v > 0]
    return {
        "markets": len(markets),
        "with_liquidity": len(funded),
        "traded_volume_gt0": len(traded),
        "liquidity_median_all_usd": round(statistics.median(liq), 2) if liq else None,
        "liquidity_median_funded_usd": round(statistics.median(funded), 2) if funded else None,
        "liquidity_p90_funded_usd": round(q(funded, 0.9), 2) if funded else None,
        "liquidity_gt_1k": sum(1 for v in liq if v > 1000),
        "liquidity_gt_10k": sum(1 for v in liq if v > 10000),
        "liquidity_total_usd": round(sum(liq), 2),
        "volume_median_traded_usd": round(statistics.median(traded), 2) if traded else None,
        "volume_p90_traded_usd": round(q(traded, 0.9), 2) if traded else None,
        "volume_gt_1k": sum(1 for v in vol if v > 1000),
        "volume_gt_10k": sum(1 for v in vol if v > 10000),
        "volume_total_usd": round(sum(vol), 2),
        "volume_max_usd": round(max(vol), 2) if vol else None,
    }


def check():
    """Compare the saved dump with the figures printed in section 10 of the page."""
    files = sorted(OUT.glob("seer_depth_*.json"))
    if not files:
        print("no dump found; run without --check first")
        return 1
    report = json.loads(files[-1].read_text(encoding="utf-8"))
    a = report["datasets"]["all"]["groups"]["all"]
    c = report["datasets"]["conditional"]["groups"]["all"]
    pinned = [
        ("all.markets", a["markets"], 3051),
        ("all.with_liquidity", a["with_liquidity"], 437),
        ("all.liquidity_median_funded_usd", a["liquidity_median_funded_usd"], 1.13),
        ("all.liquidity_p90_funded_usd", a["liquidity_p90_funded_usd"], 331.56),
        ("all.liquidity_gt_1k", a["liquidity_gt_1k"], 18),
        ("all.liquidity_gt_10k", a["liquidity_gt_10k"], 0),
        ("all.liquidity_total_usd", a["liquidity_total_usd"], 63521.85),
        ("all.traded_volume_gt0", a["traded_volume_gt0"], 556),
        ("all.volume_median_traded_usd", a["volume_median_traded_usd"], 45.83),
        ("all.volume_p90_traded_usd", a["volume_p90_traded_usd"], 5091.49),
        ("all.volume_gt_10k", a["volume_gt_10k"], 42),
        ("cond.markets", c["markets"], 1153),
        ("cond.with_liquidity", c["with_liquidity"], 125),
        ("cond.liquidity_median_funded_usd", c["liquidity_median_funded_usd"], 25.91),
        ("cond.liquidity_gt_1k", c["liquidity_gt_1k"], 3),
        ("cond.liquidity_total_usd", c["liquidity_total_usd"], 13446.42),
    ]
    bad = 0
    for name, got, want in pinned:
        tol = max(0.01 * abs(want), 0.01)
        ok = abs(got - want) <= tol
        print(("OK   " if ok else "FAIL ") + f"{name:32} page={want} data={got}")
        bad += 0 if ok else 1
    print("\ncheck:", "PASS" if not bad else f"FAIL ({bad} mismatches)", "-", files[-1].name)
    return 0 if not bad else 1


def main():
    if "--check" in sys.argv:
        return check()
    OUT.mkdir(exist_ok=True)
    stamp = datetime.now(timezone.utc)
    report = {"fetched_utc": stamp.isoformat(timespec="seconds"),
              "source": URL, "datasets": {}}
    for name, view in (("all", {}), ("conditional", {"showConditionalMarkets": True})):
        print("fetch", name, flush=True)
        reported, markets = fetch(view)
        groups = {"all": markets}
        for chain in sorted({m.get("chainId") for m in markets}):
            groups[f"chain_{chain}"] = [m for m in markets if m.get("chainId") == chain]
        groups["conditional"] = [m for m in markets if is_conditional(m)]
        groups["futarchy_type"] = [m for m in markets if m.get("type") == "Futarchy"]
        report["datasets"][name] = {
            "request": view,
            "reported_count": reported,
            "fetched": len(markets),
            "groups": {k: summarise(v) for k, v in groups.items() if v},
        }
        print(name, "reported", reported, "fetched", len(markets), flush=True)

    path = OUT / f"seer_depth_{stamp:%Y-%m-%d}.json"
    path.write_text(json.dumps(report, indent=1), encoding="utf-8")
    print("wrote", path, flush=True)
    for name, ds in report["datasets"].items():
        g = ds["groups"]
        print(name, json.dumps({k: g[k] for k in ("all", "conditional") if k in g})[:900], flush=True)


if __name__ == "__main__":
    sys.exit(main())
