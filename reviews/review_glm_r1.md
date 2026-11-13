# 1. VERDICT
**8.5/10.** Yes — this would place top-3 among the entries in document C; it is the only entry that recomputes, discloses its own weak assumptions, and ships markets.

# 2. FATAL FLAWS
Nothing disqualifying, but four items a judge will catch:

- **Stale/wrong census.** "Written after reading all 54 entries already on the board" / "Fifty-five entries are on the board" / "the 54-entry convergence table" — document C shows **83 claims** on the bounty. The convergence table ("45 of 55 name a metric", "0 price the worker's cost") is the plan's differentiation argument and it is built on a count that is visibly wrong by the board's own page. The "0 of 55 price worker inference" claim is also immediately qualified by "the closest is 9441", which concedes the cell isn't 0. Embarrassing, not fatal — but the headline differentiator rests on a stale regex run.
- **Ancillary lines carried at gross.** "the three smaller lines are carried at gross revenue with no direct cost modelled." The plan admits this, but then still uses the 7.4% blend for the headline "$10,834 of monthly revenue" and "break-even in month 11". The honest headline is the fee-only one (+$124 in month 12). The plan says this — then buries it. Judges read headlines.
- **Futarchy is advisory for half the horizon.** "the default for the first six months is advisory-first… the team holds a 2-of-3 veto." The brief asks how "futarchy would govern its actions"; for months 1–6 the honest answer in this plan is "a multisig with a market's opinion attached". The mandate mechanism (section 10) partially answers this, but the binding threshold (≥$3,000 and ≥20 traders) is met by **zero branches today** by the plan's own measurement.
- **Unverifiable "measured" data presented as data.** The poidh buyer-base stats (193 wallets, 30.7% repeat, median $11.81) and Seer depth scrape are load-bearing and cannot be checked from the claim alone. They are labelled with scripts, which is better than the field, but "ETH at $2,235" is asserted as "the price the revenue model uses" with no date-stamped source a judge can hit.

# 3. ARITHMETIC CHECK
**Unit economics:** 6% × $61 = $3.66 ✓. $3.66 − $1.90 − $0.35 = $1.41 ✓. $1.41/$3.66 = 38.5% ✓. Blended: 7.4% × $61 = $4.514; − $2.25 = $2.264 ≈ $2.26 ✓; 50.1% ✓.

**Break-even:** $3,260 / $1.41 = **2,312** ✓ (plan says 2,310 in the header, 2,312 in section 07 — cosmetic). $3,260 / $2.26 = **1,442**; plan says 1,440 (section 07) and "roughly 1,450" (header) — cosmetic but three different numbers for the same quantity.

**Revenue shares:** settlement $8,784 / $10,834 = 81.1% ✓; ancillary $2,050 = 18.9% vs 7+8+4 = 19% ✓. Float: $146,400 × 3.5% × 9/365 = $126.5 vs "$128" — cosmetic.

**12-month table:** M3 $5,040×6.0% = $302 ✓; M6 $21,600×6.6% = $1,426 ✓; M9 $62,100×7.1% = $4,409 ✓; M12 $146,400×7.4% = $10,834 ✓.

**Contribution column:** M3: 120 × ($2.52−$2.25) = $32 ✓. M6: 480 × ($2.97−$2.25) = $346 ✓. M9: 1,150 × ($54×7.1%−$2.25) = 1,150 × $1.584 = $1,822 ✓. M12: 2,400 × $2.264 = **$5,434** ✓ (but $2.26 × 2,400 = $5,424 — the plan prints both $2.26 and $5,434; rounding, cosmetic). **M1: $72 revenue → $4 contribution is unexplained** — at the M3 per-task contribution (~$0.27 on a $42 ticket) $72 of GMV yields under $1; $4 implies ~15 tasks at ~$5 tickets, contradicting the $42 average. Small dollar amount, unexplained inconsistency — cosmetic but sloppy in the one table judges recompute.

**Cash curve:** $14,200 − $3,256 = $10,944 ✓; M4 trough $1,312 ✓; M5 +$30,000 − $3,056 = $28,256 ✓; M12 $21,792 ✓. Internally consistent.

**Break-even both ways:** fee-only M12 contribution 2,400 × $1.41 = $3,384 vs $3,260 → +$124, break-even in month 12 ✓ as stated. Blended crosses M11 (+$771) ✓. Sensitivity table (5/10/15/20% sample: $2.36/$1.41/$0.46/−$0.49; BE 1,381/2,312/7,087/never) all recompute ✓. Ticket floor: $2.25/6% = $37.50 ✓. Mix: 0.6×60+0.3×12+0.1×220 = $61.60 ✓. Ledger closes to $61.61 ✓. Small lane: $0.72−$0.02 = $0.70; 3,260/0.70 = 4,657 ≈ 4,660 ✓.

**No fatal arithmetic errors.** Every load-bearing number closes; the flaws are the unexplained M1 contribution, the 2,310/2,312/1,440/1,450 drift, and the gross-vs-net presentation of the 1.4 ancillary points.

# 4. BRIEF COVERAGE
- **Where tasks come from — SOLID.** Five ranked waves with time-to-first-dollar logic, plus measured poidh buyer data and an explicit "no paid acquisition" argument with arithmetic.
- **Assignment — SOLID.** Claim-not-bid, bond, claim ceiling after 5, deterministic test gate, market triage to top-k.
- **Assessment — SOLID.** Three layers with costs, adversarial test authorship, sampled audit, escalation gate at 8× cost.
- **Spending/disputes/human intervention — SOLID.** Escrow contract, Reality.eth + Kleros ladder with loser-pays, three named human reserved powers with a 2% override trigger.
- **Revenue — SOLID.** Four lines, unit economics, party-by-party ledger that closes, sensitivity tables, funding tranches with a named trough month.
- **Futarchy directs actions — WEAK.** The mandate mechanism is the right shape, but binding governance is deferred until a depth/trader threshold no branch on Seer meets today, and a 2-of-3 human veto sits over everything for six months. Honest, but it concedes the brief's core question for most of the horizon.

# 5. WHAT IS ACTUALLY GOOD
- The verification-ratio framing (audit bill as % of fee, falling with ticket size) is a genuinely novel lens no entry in C offers.
- The $37.50 floor derivation and the two-lane split that follows from it is real design work, not assertion.
- The ledger that closes to $61.61 across seven parties, with each party's own break-even.
- Shipping two Seer markets with tx hashes and publishing empty books as empty.
- Dated, falsifiable predictions with kill criteria distinct from targets.

# 6. FIVE CONCRETE FIXES
1. **Re-run the census against the current board (83 claims) and republish section 00.** Change "Prices the worker's own inference | 0" to "1 (partial, 9441)" or delete the row; the differentiation claim must survive the actual count, not the 9-Nov snapshot.
2. **Make the fee-only path the headline.** Change the header to: "$8,784/mo settlement-fee revenue at month 12, +$124 over the $3,260 fixed base; ancillary lines add $2,050 gross, uncosted." Move the 7.4%/$10,834 figure below the disclosure. Currently the optimistic number leads and the correction trails it by 900 words.
3. **Fix the M1 contribution line.** At $42 average ticket and $0.27/task contribution, $72 of GMV yields ~$0.50, not $4. Either restate M1 contribution as ~$0–1 or show the task count/ticket that produces $4.
4. **Pick one break-even pair and use it everywhere.** Header says 1,450/2,310; section 07 says 1,440/2,312. Correct values: **1,442 and 2,312**. Use them in both places.
5. **Delete or qualify "futarchy markets on Gnosis" (section 02).** Seer's own deployment data in this plan shows markets on Optimism, Gnosis and Base; naming Gnosis as the governance venue contradicts the plan's own section 10 measurement and the Base markets it shipped. Say "Seer futarchy markets" and name the deployment chain per decision.

FATAL_ARITHMETIC: no
FATAL_CONSISTENCY: no

[reasoning]
Need to check arithmetic.

Unit economics: fee 6% × $61 = $3.66. Audit $1.90, gas $0.35 → contribution $1.41. 1.41/3.66 = 38.5%. ✓.

Blended: 7.4% of $61 = $4.514. Minus $2.25 costs = $2.264 ≈ $2.26. 2.26/4.51 = 50.1% ✓. Break-even fee-only: 3260/1.41 = 2312 ✓. Blended: 3260/2.26 = 1442 ≈ 1440 ✓.

Revenue table: month 12: 146,400 × 7.4% = $10,833.6 ✓. Month 9: 62,100 × 7.1% = $4,409.1 ✓. Month 6: 21,600 × 6.6% = $1,425.6 ✓. Month 3: 5,040 × 6% = $302.4 ✓.

But: blended take 7.4% = 6% + 1.4% ancillary. Ancillary revenue at month 12 = 1.4% × 146,400 = $2,050. Settlement fee = 6% × 146,400 = $8,784. 8,784/10,834 = 81.1% ✓. Ancillary $2,050/10,834 = 18.9%, but table says 7+8+4 = 19% ✓.

Fee-only month-12 contribution: 2,400 × 1.41 = $3,384 ✓ vs fixed 3,260 → +$124 ✓. Blended: 2,400 × 2.26 = $5,424, plan says $5,434 — off by $10 (rounding: 2.264×2400 = 5433.6, so $5,434 consistent with unrounded; but $2.26 stated → 5,424). Cosmetic.

Profit month 12: 5,434 − 3,260 = $2,174 ✓.

Cash curve: month 1 revenue $72, contribution $4? 72×... contribution should be ~38.5% of revenue = $28, not $4. Hmm. Month 1: revenue $72, contribution $4 — inconsistent with unit economics. Month 3: revenue $302, contribution $32 — 10.6%. Month 6: 1,426 → 346 = 24%. Month 9: 4,409 → 1,822 = 41%. Month 12: 10,834 → 5,434 = 50%. Early months low contribution maybe because fixed audit per task at low tickets? Month 3: 120 tasks, avg $42, fee $2.52, audit $1.90, gas $0.35 → contribution $0.27/task × 120 = $32.4 ✓! Month 1: $72 revenue... tasks? If avg ticket $42, ~1.7 tasks? Contribution $4 plausible-ish. Actually month 1: 72/42 ≈ 1.7 tasks × 0.27 = $0.46, not $4. Hmm, but maybe more tasks smaller. Unverifiable; weak. Month 6: 480 tasks × $45: fee $2.70 − 2.25 = $0.45 × 480 = $216, not $346. Blended take 6.6% → 0.66% ancillary adds 480×45×0.0066... contribution at blended: 45×6.6% = $2.97 − 2.25 = $0.72 × 480 = $346 ✓. OK month 6 consistent with blended. Month 3 at blended 6.0%: 42×6% = 2.52 − 2.25 = 0.27 × 120 = $32.4 ✓. Month 1: $72 revenue at 6% → contribution (72/42 tasks?) — if avg ticket $42, tasks = 1.71, contribution 0.46. $4 implies ~15 tasks at $4.8 ticket? Inconsistent but tiny. Flag as unexplained.

Cash: start $14,200. Month1 net −3,256 → 10,944 ✓. Month 3 closing 4,472: months 1–3 cumulative net = −3,256 −3,242? −3,256 + m2 + (−3,228) = 4,472−14,200 = −9,728 → m2 = −3,244. Plausible. Month 4: 4,472 − 3,160 = 1,312 ✓. Month 5: 1,312 − 3,056 + 30,000 = 28,256 ✓. Month 6: 28,256 − 2,914 = 25,342 ✓. Month 9: 25,342 − (m7+m8+m9 nets). m9 net −1,438. 25,342 − 19,278 = 6,064 over 3 months; m7, m8 nets sum = 6,064 − 1,438 = 4,626 of burn, plausible. Month 10: 19,278 − 431 = 18,847 ✓. Month 11: +771 → 19,618 ✓. Month 12: +2,174 → 21,792 ✓.

Break-even "crossed in month 11" ✓ (+771).

Fee-only break-even: month 12 contribution fee-only = 3,384 > 3,260, +124 ✓, so fee-only break-even in month 12 ✓.

Small-task lane: $12 avg, fee $0.72, gas $0.02 → $0.70 ✓. 3,260/0.70 = 4,657 ≈ 4,660 ✓.

Audit sample sensitivity: 5%: audit $0.95, contribution 3.66−0.95−0.35 = 2.36 ✓; BE 3260/2.36 = 1,381 ✓. 15%: 2.85 → 0.46; 3260/0.46 = 7,087 ✓. 20%: 3.80 → −0.49 ✓.

Ticket floor: fee 6%×T = 2.25 → T = $37.50 ✓.

Mix: 0.6×60 + 0.3×12 + 0.1×220 = 36+3.6+22 = $61.60 ✓.

Ledger: worker gets 94% of 61 = $57.34, less $0.36 inference → +$56.98 ✓. Poster pays $61.61. Sum check: 56.98+0.36+0.61+1.90+0.35+1.41 = 61.61 ✓. But wait: Foreguild takes $3.66 fee, pays out $2.25 (audit 1.90 + gas 0.35), keeps 1.41 ✓. Ledger closes.

But: audit is 10% sample — expected $1.90 per task means every task pays full audit cost, i.e., audit $19 per audited task × 10% = $1.90. Ledger lists auditor "+$1.90 expected per task" — fine.

Inconsistency: section 07 says "the unit economics charge a human audit to every task ($1.90), while the mix implies an audit on 70% of them... about $1.33. The model therefore overstates audit cost by roughly $0.57" — 10% sample of 70% = 7% of tasks audited → expected audit = 0.07 × 19 = $1.33. But base case charges $1.90 = 10% of tasks audited. So the "10% sample" applies to audited-lane tasks only (70% of tasks), meaning effective sample 7%. The plan acknowledges. OK.

But wait: "100% of tasks above $1,000" — the $150+ band avg $220, none above $1,000, fine.

Discrepancy: header says "break-even at roughly 1,450 settled tasks" vs 1,440 elsewhere — cosmetic.

Section 00 says "Fifty-five entries" / "54 entries" inconsistently ("written after reading all 54 entries", "Fifty-five entries are on the board", "counted over the 55 claim bodies", script checks "54-entry convergence table"). Internal inconsistency — flag.

Also "of 55" table: 45+13+28+16+13+28+16+30+51+0+3 — these overlap, fine.

Triage fee: poster pays 1% ($0.61), pass-through. But then poster pays $61.61 total; fine. But triage fee is a cost to poster not in revenue — consistent.

Full-audit upgrade $25 flat on tasks above $250, but audit costs $19 base — margin $6, disclosed ✓. But 100% audit above $1,000 "the poster buys that audit as part of the $25 upgrade" — $25 for a $19 audit, fine.

Data licensing $4–12/pair at 8% of month-12 revenue = $867/mo → ~100–215 pairs; small lane 30% of 2,400 = 720 tasks/mo producing pairs — plausible.

Certification 4% = $433/mo at $25–150 → 3–17 certs/mo. Plausible-ish.

Seer desk: 10% of settled prize, capped at 15% of month-6 revenue. Month 6 revenue $1,426 → cap $214. Fine.

Float: $146,400 GMV, 9-day holds, 3.5% APY: 146,400 × 0.035 × 9/365 = $126.5 ≈ $128 ✓. 128/10,834 = 1.18% ✓.

Factual issues: "futarchy markets on Gnosis" — Seer is its own protocol; plan says decisions go through "futarchy markets on Gnosis" then later "price-based decision markets on Gnosis... the same stack Seer documents". Seer deploys on multiple chains (Base, Gnosis, Optimism per their own data). Saying Gnosis specifically is odd but not fatal. "Reality.eth with Kleros backstop" — plausible for Seer; unverified but consistent with doc C.

"402-style payment challenges" — obscure, likely x402. Minor.

Claim of measured poidh data — can't verify, but labelled.

Contradiction: section 00 says "not one of them prices the worker's own cost" and "Prices the worker's own inference | 0" but then says "The closest is 9441, whose fee formula nets out guardian compute cost" — minor.

Also: "Median entry: 965 characters" — doc C entries are much longer than 965 chars; the claim bodies quoted are hundreds of words. 965 chars median seems wrong vs. evidence in doc C — but doc C only shows 10 of 83. Still, the plan says 55 entries; doc C says 83 claims. The plan's census (55) contradicts the board (83). That's a factual error against document C — the plan was written 9 Nov, maybe before more entries. Still flag: "written after reading all 54 entries" vs 83 on board — stale/incorrect count.

Also the plan claims "Two of 68 markets clear it today, and neither is a branch" then names two parent markets — consistent.

Governance: advisory-first with 2-of-3 team veto — honest but weakens "futarchy governs" requirement; brief wants futarchy directing actions. It does explain mandate mechanism — solid.

Break-even claim in header: "crossed in month 11" — blended yes.

One more: month-12 contribution $5,434 vs $2.26×2,400 = $5,424 — cosmetic rounding.

Month 1 contribution $4 unexplained — flag.

Fee-only month-12 profit +$124 stated; but earlier "the settlement fee alone lands at $3,384 of contribution against $3,260 — covers the rent and nothing else" ✓.

Also "Break-even at that blend ~1,440" vs header "1,450" — cosmetic.

Score: this is a very strong entry — detailed, self-auditing, live markets, measured data. Weaknesses: census count wrong (54/55 vs 83), month-1 contribution unexplained, ancillary lines carried at gross with no cost (disclosed), futarchy advisory for 6 months. Top-3? Likely yes among doc C. Score ~8.5.

Fatal arithmetic? No — everything recomputes. Fatal consistency? The 54/55/83 count is an embarrassment but not fatal; ancillary gross-margin assumption disclosed. Say no for both, but flag.

Write tersely.
