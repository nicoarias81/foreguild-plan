#!/usr/bin/env python3
"""Recount the convergence table of section 00 from the claim dump.

    python3 tools/field_stats.py                 # uses data/claims_2026-11-08.json
    python3 tools/field_stats.py --check         # compare with the counts on the page

Each row of the table in section 00 is one regex over the claim body. The point
is not that regexes are rigorous prose analysis; it is that the number on the
page can be recomputed by anyone who downloads the same dump, which is not true
of "twenty-two entries already agree".
"""
import json
import sys
import statistics
from pathlib import Path

HERE = Path(__file__).resolve().parent
DUMP = HERE.parent / "data" / "claims_2026-11-08.json"

PATTERNS = {
    "futarchy": r"futarch",
    "named_metric": r"(nsr|npr|nfr|ncv|ndr|nvr|cmv|gmv|net revenue|net settled|net fee)",
    "named_roles": r"\b(scout|planner|worker|verifier|auditor|orchestrator)\b",
    "take_pct": r"\b\d{1,2}(\.\d+)?\s?%",
    "per_task_floor": r"(floor|minimum fee|min\. fee|\$\d+ minimum)",
    "escrow": r"escrow",
    "bonds": r"bond|slash",
    "dispute_ladder": r"dispute|kleros|reality\.eth|arbitr",
    "risk_section": r"\brisk",
    "phased_roadmap": r"phase|roadmap|90[- ]day",
    "links_out": r"https?://",
    "prices_worker_inference": r"(inference cost|token cost|per-token|cost of the worker)",
    "metered_rail": r"metered|per-call|pay-per-call|micropay",
    "live_market_deployed": r"(app\.seer\.pm|seer\.pm/markets|deployed.{0,30}market)",
}

# the counts printed in section 00 of index.html
PAGE = {
    "futarchy": 40, "named_metric": 26, "named_roles": 13, "take_pct": 26,
    "per_task_floor": 6, "escrow": 14, "bonds": 11, "dispute_ladder": 26,
    "risk_section": 15, "phased_roadmap": 29, "links_out": 46,
    "prices_worker_inference": 0, "metered_rail": 1, "live_market_deployed": 2,
}


def main():
    data = json.loads(DUMP.read_text(encoding="utf-8"))
    claims = data["claims"] if isinstance(data, dict) else data
    bodies = [c.get("description") or "" for c in claims]  # claim body only, not the title
    import re
    counts = {k: sum(1 for b in bodies if re.search(p, b, re.I)) for k, p in PATTERNS.items()}
    lengths = [len(c.get("description") or "") for c in claims]
    print(f"claims {len(claims)}  median {statistics.median(lengths):.0f} chars  "
          f"min {min(lengths)}  max {max(lengths)}  (claim body only)")
    bad = 0
    for k in PATTERNS:
        mark = ""
        if "--check" in sys.argv:
            mark = "OK  " if counts[k] == PAGE[k] else "FAIL"
            bad += 0 if counts[k] == PAGE[k] else 1
        print(f"  {mark} {k:24} {counts[k]:3}")
    if "--check" in sys.argv:
        print("check:", "PASS" if not bad else f"FAIL ({bad})")
        return 1 if bad else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
