#!/usr/bin/env python3
"""Recompute every financial number the plan quotes, from its stated drivers.

    python3 tools/model.py           # print the ledger
    python3 tools/model.py --check   # compare with the figures printed on the page

Drivers are inputs, not outputs: change one and the whole ledger moves. The page
quotes these figures, so a mismatch here means the page is wrong.

Token price: $3 / 1M input, $15 / 1M output. Token counts are the four rows of
section 00 (agent-to-agent, small, standard, heavy).
"""
import sys

TOKEN_IN, TOKEN_OUT = 3.0 / 1e6, 15.0 / 1e6

# name: (input tokens, output tokens)
TOKENS = {
    "a2a": (3_000, 300),
    "small": (40_000, 4_000),
    "standard": (60_000, 12_000),
    "heavy": (800_000, 60_000),
}

FEE_CONTRACT = 0.06            # settlement fee on the contract rail
FEE_METERED = 0.015            # metered rail
AUDIT_SAMPLE = 0.10            # share of settled tasks that get a human audit
AUDIT_COST = 19.00             # 20 minutes at $57/hour
PER_TASK_INFRA = 0.35          # gas $0.04 + sandbox $0.06 + indexer/RPC $0.25
FIXED_MONTH = 3_260            # team $3,000 + hosting/indexer $260

# month, tasks/month, average ticket, blended take
ANCHORS = [
    (1, 30, 40.0, 0.060),
    (3, 120, 42.0, 0.060),
    (6, 480, 45.0, 0.066),
    (9, 1_150, 54.0, 0.071),
    (12, 2_400, 61.0, 0.074),
]

SEED = 26_700
CONTRACTS = 6_500              # paid to external auditors, one-off
LIQUIDITY = 4_000              # locked in markets, recoverable
SUBSIDY = 2_000                # cold-start incentives, one-off
TRANCH = 30_000
TRANCH_MONTH = 5               # end of month 5, gated on the month-5 metrics


def inference(task):
    i, o = TOKENS[task]
    return i * TOKEN_IN + o * TOKEN_OUT


def interp(month, idx):
    """Piecewise-linear interpolation of anchor column idx (0 tasks, 1 ticket, 2 take)."""
    points = [(0, 0.0)] + [(m, [t, tk, take][idx]) for m, t, tk, take in ANCHORS]
    for (m0, v0), (m1, v1) in zip(points, points[1:]):
        if m0 <= month <= m1:
            return v0 + (v1 - v0) * (month - m0) / (m1 - m0)
    return points[-1][1]


def unit_economics(ticket=61.0, task="standard"):
    fee = FEE_CONTRACT * ticket
    audit = AUDIT_SAMPLE * AUDIT_COST
    contribution = fee - audit - PER_TASK_INFRA
    return {
        "ticket": ticket,
        "fee": round(fee, 2),
        "audit": round(audit, 2),
        "infra": PER_TASK_INFRA,
        "contribution": round(contribution, 2),
        "contribution_pct_of_fee": round(100 * contribution / fee, 1),
        "contribution_pct_of_gmv": round(100 * contribution / ticket, 2),
        "worker_inference": round(inference(task), 4),
        "worker_net": round(ticket - fee - inference(task), 2),
    }


def month_ledger():
    rows = []
    for m in range(1, 13):
        tasks = interp(m, 0)
        ticket = interp(m, 1)
        take = interp(m, 2)
        revenue = tasks * ticket * take
        variable = tasks * (AUDIT_SAMPLE * AUDIT_COST + PER_TASK_INFRA)
        contribution = revenue - variable
        rows.append({"month": m, "tasks": round(tasks), "ticket": round(ticket, 2),
                     "take": round(take, 4), "gmv": round(tasks * ticket, 0),
                     "revenue": round(revenue, 0), "contribution": round(contribution, 0),
                     "net": round(contribution - FIXED_MONTH, 0)})
    return rows


def cash_curve():
    """Operating cash: seed minus one-offs, then monthly net, plus the month-5 tranche."""
    cash = SEED - CONTRACTS - LIQUIDITY - SUBSIDY
    rows, trough, trough_month = [], cash, 0
    for r in month_ledger():
        cash += r["net"]
        if r["month"] == TRANCH_MONTH:
            cash += TRANCH
        if cash < trough:
            trough, trough_month = cash, r["month"]
        rows.append({"month": r["month"], "closing": round(cash, 0)})
    return rows, trough, trough_month


def main():
    u = unit_economics()
    rows = month_ledger()
    cash_rows, trough, trough_month = cash_curve()
    m12 = rows[-1]

    breakeven_fee = FIXED_MONTH / u["contribution"]
    per_task_12 = m12["contribution"] / m12["tasks"]
    breakeven_blend = FIXED_MONTH / per_task_12
    float_month = m12["gmv"] * (9 / 30) * 0.035 / 12
    op_cash0 = SEED - CONTRACTS - LIQUIDITY - SUBSIDY
    runway_zero = op_cash0 / FIXED_MONTH
    neg = next((r["month"] for r in cash_rows if r["closing"] < 0), None)
    # The settlement fee alone, same variable cost: the conservative path the
    # page quotes next to the blended one. If these two diverge, the profit in
    # the table is ancillary margin, and the page has to say so.
    fee_only = [r["tasks"] * r["ticket"] * FEE_CONTRACT
                - r["tasks"] * (AUDIT_SAMPLE * AUDIT_COST + PER_TASK_INFRA) - FIXED_MONTH
                for r in rows]
    fee_pos = next((r["month"] for r, v in zip(rows, fee_only) if v > 0), None)
    blend_pos = next((r["month"] for r in rows if r["net"] > 0), None)

    print("UNIT ECONOMICS  $61 standard task")
    for k, v in u.items():
        print(f"  {k:26} {v}")
    print("\n12-MONTH LEDGER")
    for r in rows:
        print(f"  m{r['month']:2} tasks {r['tasks']:5}  ticket ${r['ticket']:5.2f}  "
              f"take {r['take']*100:4.1f}%  rev ${r['revenue']:7.0f}  "
              f"contrib ${r['contribution']:6.0f}  net ${r['net']:6.0f}")
    print(f"\nBREAK-EVEN   fee-only {breakeven_fee:.0f} tasks/mo | blend {breakeven_blend:.0f} tasks/mo")
    print(f"MONTH-12     revenue ${m12['revenue']:.0f}  contribution ${m12['contribution']:.0f}  "
          f"per task ${per_task_12:.2f}  profit ${m12['net']:.0f}")
    print(f"CASH         operating at t0 ${op_cash0:.0f} ({runway_zero:.1f} months at zero revenue)")
    print(f"FEE-ONLY     net at m12 ${fee_only[-1]:.0f}; turns positive in month {fee_pos}; "
          f"blended path turns positive in month {blend_pos}")
    print(f"             trough ${trough:.0f} at m{trough_month}; first negative month {neg}")
    print(f"             closing m12 ${cash_rows[-1]['closing']:.0f}")
    print(f"FLOAT        ${float_month:.1f}/month at month-12 GMV (3.5% APY, 9-day hold)")
    print("CASH ROWS    " + ", ".join(f"m{c['month']}=${c['closing']:.0f}" for c in cash_rows
                                      if c["month"] in (1, 3, 5, 6, 9, 12)))
    print("\nHEAD-TO-HEAD at AOV $60 (standard task, worker inference $0.36)")
    for rate in (0.04, 0.06, 0.08, 0.10):
        fee = rate * 60
        net = 60 - fee - inference("standard")
        print(f"  {rate*100:4.1f}%  fee ${fee:5.2f}  worker keeps ${net:6.2f}  "
              f"({100*net/60:5.1f}% of ticket)")
    print("\nFLOORS on a $0.05 agent-to-agent call")
    for name, price in (("$2.00 per verdict", 2.00), ("$0.25 floor", 0.25),
                        ("$0.40 floor", 0.40), ("1.5% metered (this plan)", FEE_METERED * 0.05)):
        print(f"  {name:28} ${price:7.4f}  = {100*price/0.05:6.0f}% of the ticket")

    pinned = {
        "contribution": 1.41, "contribution_pct_of_fee": 38.5,
        "m12_revenue": 10834, "m12_contribution": 5434, "m12_profit": 2174,
        "m12_per_task": 2.26, "breakeven_fee": 2312, "breakeven_blend": 1440,
        "float_month": 128.0, "fee_only_net_m12": 124, "fee_only_turn": 12,
        "blend_turn": 11,
    }
    got = {"contribution": u["contribution"], "contribution_pct_of_fee": u["contribution_pct_of_fee"],
           "m12_revenue": m12["revenue"], "m12_contribution": m12["contribution"],
           "m12_profit": m12["net"], "m12_per_task": round(per_task_12, 2),
           "breakeven_fee": round(breakeven_fee, 0), "breakeven_blend": round(breakeven_blend, 0),
           "float_month": round(float_month, 0),
           "fee_only_net_m12": round(fee_only[-1], 0), "fee_only_turn": fee_pos,
           "blend_turn": blend_pos}

    if "--check" in sys.argv:
        bad = 0
        for k, want in pinned.items():
            tol = 1.0 if isinstance(want, int) else 0.02
            ok = abs(got[k] - want) <= tol
            print(("OK   " if ok else "FAIL ") + f"{k:24} page={want} model={got[k]}")
            bad += 0 if ok else 1
        print("\ncheck:", "PASS" if not bad else f"FAIL ({bad} mismatches)")
        return 1 if bad else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
