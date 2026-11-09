"""Who already pays for work on poidh, counted from the same raw logs as the CSV.

Purpose: the growth section needs the buyer population measured, not assumed.
Every number here comes from BountyCreated / ClaimAccepted events in
../poidh-v3-data/data/raw_logs_<chain>.json (cutoff 2026-11-08T03:59:54Z).

Run: python tools/buyer_base.py
Writes data/buyer_base.json
"""
import json
import statistics
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = Path("C:/Users/nicoa/poidh-v3-data")
DATA = REPO / "data"
sys.path.insert(0, str(REPO / "scripts"))
import build_csv as B  # noqa: E402

ETH = 1e18


def main():
    per_chain = {}
    issuers = defaultdict(lambda: {"bounties": 0, "accepted": [], "chains": set()})
    for chain in B.CHAINS:
        raw = json.loads((DATA / f"raw_logs_{chain}.json").read_text(encoding="utf-8"))
        bounties = {}
        accepted = defaultdict(int)
        for lg in B.sort_logs(raw["core"]):
            name = B.topic_name(lg["topics"][0])
            w = B.words(lg.get("data") or "0x")
            if name == "BountyCreated":
                bid = B.uint(lg["topics"][1])
                iss = B.addr_of_topic(lg["topics"][2])
                bounties[bid] = {"issuer": iss, "amount": B.uint(w[2])}
                issuers[iss]["bounties"] += 1
                issuers[iss]["chains"].add(chain)
            elif name == "ClaimAccepted" and w:
                accepted[B.uint(lg["topics"][1])] += 1
        for bid, a in bounties.items():
            if bid in accepted:
                issuers[a["issuer"]]["accepted"].append(a["amount"] / ETH)
        per_chain[chain] = {"bounties": len(bounties), "accepted": len(accepted)}

    paid = {k: v for k, v in issuers.items() if v["accepted"]}
    spend = [sum(v["accepted"]) for v in paid.values()]
    repeat = {k: v for k, v in paid.items() if len(v["accepted"]) >= 2}
    out = {
        "cutoff": "2026-11-08T03:59:54Z",
        "per_chain": per_chain,
        "issuers_total": len(issuers),
        "issuers_with_accepted_bounty": len(paid),
        "issuers_with_2plus_accepted": len(repeat),
        "issuers_2plus_share_pct": round(100 * len(repeat) / len(paid), 1) if paid else 0,
        "issuers_paid_gt_100usd": sum(1 for s in spend if s * ETH_PRICE > 100),
        "issuers_paid_gt_1000usd": sum(1 for s in spend if s * ETH_PRICE > 1000),
        "spend_median_usd": round(statistics.median(spend) * ETH_PRICE, 2) if spend else 0,
        "spend_mean_usd": round(statistics.mean(spend) * ETH_PRICE, 2) if spend else 0,
        "spend_p90_usd": round(sorted(spend)[int(0.9 * (len(spend) - 1))] * ETH_PRICE, 2) if spend else 0,
        "top10_share_of_spend_pct": round(100 * sum(sorted(spend)[-10:]) / sum(spend), 1) if spend else 0,
        "eth_price_usd": ETH_PRICE,
        "repeat_issuer_detail": sorted(
            ({"issuer": k, "accepted_bounties": len(v["accepted"]), "usd": round(sum(v["accepted"]) * ETH_PRICE, 2),
              "chains": sorted(v["chains"])} for k, v in repeat.items()),
            key=lambda x: -x["usd"])[:15],
    }
    (ROOT / "data" / "buyer_base.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
    for k, v in out.items():
        if k != "repeat_issuer_detail":
            print(k, "=", v)
    print("\ntop repeat issuers:")
    for r in out["repeat_issuer_detail"]:
        print(f"  {r['issuer']}  {r['accepted_bounties']:>2} accepted  ${r['usd']:>8.2f}  {','.join(r['chains'])}")


ETH_PRICE = 2235.0  # ETH/USD used in the plan's own model (section 05), so the two agree

if __name__ == "__main__":
    main()
