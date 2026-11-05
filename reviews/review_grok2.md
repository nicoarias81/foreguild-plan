1. VERDICT — 5/10. It would not place top-3: a revenue-first plan that still misstates break-even, runway, and which line actually produces profit will not survive Seer-team scrutiny or a market that can read a table.

2. FATAL FLAWS
- Cash does not reach the claimed business. Seed is a 90-day spend ($9,000 team + $3,200 infra + $6,500 audit + $4,000 liquidity + $2,000 subsidy + $2,000 reserve = $26,700). After day 90 the reserve is $2,000 against a $3,260/mo fixed base. Month-3 revenue is $274. There is no bridge to the stated break-even.
- “About 18 months of runway at the month-12 cost base if revenue stalls at month 6” is false: $26,700 / $3,260 ≈ 8.2 months at zero revenue; at month-6 revenue ($1,426) net burn is $1,834 and runway is ≈14.6 months. Not 18.
- Intro: “break-even at roughly 2,300 settled tasks per month, reached in month 10.” The table is 1,150 tasks in month 9 and 2,400 in month 12. Independent interpolation puts ~2,300 tasks in month 12, and monthly P&L crossing zero around month 11. Month 10 is wrong.
- “Four lines, one of which pays the bills” (settlement, 81%) contradicts the P&L. Month-12 settlement contribution is $1.41 × 2,400 = $3,384 vs $3,260 fixed — $124/mo. The advertised $2,164 profit is the other three lines (audit upgrades, eval data, certification), which have no buyers, no volumes, and no costs.
- Triage fee still disagrees with itself after they called out the last draft: §06 Layer 2 “2% of task value (fee)”; §07 “poster pays 1%”; unit economics “Triage fee (1%)”. Prose says “Foreguild books it as revenue and as an identical cost”; the 12-month table does not book it at all (7.4% × $146,400 = $10,834, no extra 1%).
- Full-audit line is three prices at once: “priced at cost plus a margin” / “$25 flat” / Layer 3 cost “$15–$60”. $25 is not cost-plus when cost is $60.
- Treasury cannot fund the FAO it describes. Example mandate: “on-chain analytics, $4,000 budget…” — larger than a month of opex and 2× the $2,000 reserve. Multiple category mandates are unfunded.
- Month-3 avg ticket $38 is below their own Wave 1 floor “$40–$400”. Observation date “poidh bounties on 2026-11-05” is unverified and, if the close date is 12 November 2025, in the future. Rebrand/Devcon merch “pilot record” is unverified.

3. ARITHMETIC CHECK
Unit economics (recomputed): 6% × $61 = $3.66. $3.66 − $1.90 − $0.35 = $1.41. $1.41 / $3.66 = 38.5%. Those four figures add. What is wrong/unlabelled: $61 mix is unlabelled; $19 audit is unlabelled (not the midpoint of $15–$60); $0.35 gas+sandbox unlabelled; 38.5% is margin on the 6% fee only, not on GMV (1.41/61 = 2.3%) and not on blended revenue; triage 1% vs 2% (above); pass-through is $0.00 net only if the 1% is excluded — which then contradicts “books it as revenue”.

Revenue-line shares vs blended take: 81+7+8+4 = 100. 6% × $146,400 = $8,784; $8,784 / $10,834 = 81.1% (ok). 6.0% + 1.4% = 7.4% (ok). Implied volumes are unlabelled and not fundable as stated: audit upgrades 7% → ~$758 → ~30 tasks/mo at $25 (1.3% of 2,400) while avg ticket is $61 and upgrades are “on tasks above $250”; data 8% → ~$867 at $4–$12 with no units; cert 4% → ~$433 with no exams/mo. Ancillary 19% of revenue is 1.4% of GMV only if those volumes exist.

12-month table (recomputed): 120 × 38 = 4,560; 6.0% = 273.6 ≈ $274. 480 × 45 = 21,600; 6.6% = 1,425.6 ≈ $1,426. 1,150 × 54 = 62,100; 7.1% = 4,409.1 ≈ $4,409. 2,400 × 61 = 146,400; 7.4% = 10,833.6 ≈ $10,834. Row arithmetic holds. $10,834 × 12 = $130,008 (ok). Inconsistent with other claims: ticket $38 vs Wave 1 $40–$400; 2,400 tasks in month 12 vs “reached in month 10” at 2,300; blended take >6% is entirely the unlabelled ancillary volumes.

Break-even vs fixed $3,260: $3,260 / $1.41 ≈ 2,312 tasks (matches “~2,310” / “roughly 2,300”). That task count is not month 10 in their table (month 10 ≈ 1,570 tasks). Using month-12 $2.26/task, $3,260 / $2.26 ≈ 1,442 tasks — a different break-even they also do not hit in month 10 on a like-for-like mix. 2,400 × $2.26 = $5,424; $5,424 − $3,260 = $2,164 (ok as algebra, not as economics: $2.26 assumes the 19% extras). Settlement-only at month 12: $3,384 − $3,260 = $124, not $2,164. Seed “18 months” is wrong (see above). Prize “~$9.9k” covering “about a third” of $26,700 is unverified (ETH/USD) and is the author’s bounty, which they correctly refuse to treat as treasury — then still treat it as “first tranche” of protocol capital.

4. BRIEF COVERAGE
- Where tasks come from — WEAK: five waves and “a DM and settle in a week”; no funnel, conversion, or how two part-timers produce 2,400 settled tasks/mo.
- How agents are assigned — SOLID: escrow + test, bond, claim cap then beat-the-best; assignment is specified.
- How completed work is assessed — WEAK: three-layer stack is clear, but Layer 2 depends on triage liquidity they must seed, Layer 3 prices contradict, and the poster still reads top-3 so “sell the receipt” is a ranked shortlist.
- Spending / disputes / human intervention — SOLID: Reality.eth + Kleros, loser-pays, one-round cap, three logged human powers, 2% override trigger — assuming those tools work as they describe (Seer wiring unverified).
- Revenue — WEAK: table rows add up; break-even month, runway, triage booking, audit price, and “settlement pays the bills” do not; ancillary lines are plugs that create the 7.4% and the profit.
- How futarchy directs agents — WEAK: mandate → budget → who may claim is more concrete than average, but the $4,000 mandate cannot be paid, fee/whitelist markets are parameter tweaks not task direction, and “futarchy markets on Gnosis” vs Seer’s own markets is unverified.

5. WHAT IS ACTUALLY GOOD
- Review-cost-as-the-product is the right problem for this audience (whether or not the Seer-site thesis quote is accurate — unverified).
- Kill criteria in §10 are falsifiable (settle 10/20, −40% review time, paid task by day 56, repeat rate).
- Facts-on-Reality.eth vs parameters-on-futarchy is the correct FAO split; they do not pretend a market reviews a PR.
- No listing fees / no subscriptions, with an explicit non-gameability reason for the metric.
- Three named rewrite conditions (tests <30%, repeat <20%, fee-market liquidity <$500) are more honest than the GMV chart.

6. FIVE CONCRETE FIXES
1. Replace the intro sentence and the seed footnote with a 12-row cash flow: opening cash, spend by bucket, revenue, variable cost, closing cash. Delete “month 10” and “18 months”. If $26.7k dies at day 90, say what is raised in month 4 or cut the plan to the 8-week prize path.
2. Pick one triage number (1% or 2%), one booking rule (in GMV-take or pass-through off-income), and make §06, §07, unit economics, and the table identical. Residual 1%/2% from the draft they already disavowed is disqualifying in v2.
3. Rebuild month-12 P&L with settlement only ($8,784 revenue, $1.41 contribution, ~$124 profit) as the base case; put audit upgrades / $4–$12 pairs / certifications in a separate upside table with named buyers and units, not inside the 7.4%.
4. Publish a task funnel that two people at $3,000/mo can actually run (hours, outbound, close rate, repeat-poster rate) that outputs 120 / 480 / 1,150 / 2,400, and make month-3 ticket ≥ the Wave 1 floor or change the wave table.
5. Resize mandates, Kleros bonds, and seed liquidity to cash on hand (example mandate ≤ reserve), and replace “$25 flat” / “cost plus margin” / “$15–$60” with one audit tariff: price, cost, who pays, sample vs 100% >$1,000, and the $19 used in unit economics.