[reasoning]
Let me work through this carefully. The submission is a long, detailed plan. I need to check arithmetic.

Key numbers:

Unit economics block:
- Settlement fee 6% × $61 = $3.66 ✓
- Triage fee pass-through $0.00 net ✓
- Amortised audit: 10% sample × $19 = $1.90 ✓
- Gas + sandbox $0.35
- Contribution fee-only: $3.66 − $1.90 − $0.35 = $1.41 ✓
- Contribution as % of fee: 1.41/3.66 = 38.52% ✓ (they say 38.5%)
- Contribution as % of ticket: 1.41/61 = 2.31% — they say "2.3% of ticket" in ledger ✓

Blended: 7.4% blended take on $61 = $4.514. Contribution at blend: $4.514 − $1.90 − $0.35 = $2.264 ≈ $2.26 ✓. As % of fee: 2.26/4.51 = 50.1% — they say "(50%)" ✓.

Break-even:
- Fee-only: $3,260 / $1.41 = 2,312.06 → they say ~2,310 tasks/mo in the header, and 2,312 later. Header says 2,310, section 07 says 2,312. Minor inconsistency (cosmetic).
- Blended: $3,260 / $2.26 = 1,442.5 → they say ~1,440. Header says 1,450. Header says "roughly 1,450" — cosmetic rounding inconsistency (1,440 vs 1,450 vs 1,442).

12-month revenue table:
- Month 3: 120 × $42 = $5,040 GMV ✓; 6.0% → $302.40 ✓
- Month 6: 480 × $45 = $21,600 ✓; 6.6% → $1,425.60 ✓ ($1,426)
- Month 9: 1,150 × $54 = $62,100 ✓; 7.1% → $4,409.10 ✓
- Month 12: 2,400 × $61 = $146,400 ✓; 7.4% → $10,833.60 ✓ ($10,834)

Check blended take consistency: month 12 revenue $10,834 on GMV $146,400 = 7.401% ✓. Settlement fee alone: 6% × 146,400 = $8,784. They say settlement fee is 81% of revenue: 8,784/10,834 = 81.08% ✓. Other lines 19%: audit upgrades 7%, data 8%, certification 4% = 19% ✓. 7% of 10,834 = $758; 8% = $867; 4% = $433. Sum of other lines = $2,050. They say "the $2,050 gap between the two paths" — 10,834 − 8,784 = $2,050 ✓.

Fee-only month 12 contribution: 2,400 tasks × $1.41 = $3,384 ✓ ("lands at $3,384 of contribution against $3,260 of fixed cost"). Fee-only profit: 3,384 − 3,260 = $124 ✓ ("+$124 in month 12").

Blended month 12 contribution: 2,400 × $2.26 = $5,424. They say $5,434. Hmm. 2,400 × 2.264 = $5,433.6 → $5,434 ✓ if using unrounded $2.264. But the table says "Contribution at 7.4% blend $2.26/task" and "Month-12 contribution $5,434/mo → profit ~$2,174". 5,434 − 3,260 = 2,174 ✓. OK consistent with unrounded.

But wait: revenue table month 12 revenue $10,834; contribution should be revenue minus variable costs. Variable costs: audit 2,400 × $1.90 = $4,560; gas 2,400 × $0.35 = $840. Total variable = $5,400. Revenue $10,834 − $5,400 = $5,434 ✓. Great, internally consistent.

Fee-only: 8,784 − 5,400 = $3,384 ✓.

Break-even fee-only: 3,260/1.41 = 2,312 ✓. Blended: 3,260/2.264 = 1,440 ✓.

Cash table:
- Month 1: revenue $72, contribution $4? 72 × 1.41/61? Hmm, contribution ratio ~2.31% of GMV fee-only... $72 × 0.0231 = $1.66. They say $4. Actually contribution per task at month 1: avg ticket lower? Month 1 revenue $72 — what tasks? If avg ticket $42-ish... Actually contribution $4 on $72 revenue = 5.6% of revenue. Hmm, that's higher than the 38.5% of fee... fee = 6% of 72 = $4.32; contribution = 38.5% of that = $1.66. They report $4. That looks wrong. Wait — maybe month 1 has no audit costs (fee waived tasks?). Actually weeks 1-4 fee waived. Month 1 revenue $72 — but fee waived means revenue $0? Hmm. Actually the seed subsidy pays the settlement fee on first tasks. Confusing. Let me check the cash curve arithmetic for internal consistency.

Month 1: Net = contribution − fixed = 4 − 3,260 = −$3,256 ✓ (matches). Closing cash $10,944. Starting operating cash $14,200. 14,200 − 3,256 = 10,944 ✓.

Month 3: contribution $32, net −$3,228 ✓ (32−3260). Closing: from month 1's 10,944, month 2 net? Not shown. 10,944 − 3,228 (month 3) = 7,716; then month 3 closing is 4,472, so month 2 net = 4,472 − 7,716 = −3,244. Contribution month 2 = 3,260 − 3,244 = $16. Plausible interpolation (month 2 revenue ~$160?). OK.

Month 4: contribution $100, net −$3,160 ✓. Closing: 4,472 − 3,160 = 1,312 ✓ trough.

Month 5: contribution $204, net −$3,056 ✓. Closing: 1,312 − 3,056 + 30,000 = 28,256 ✓.

Month 6: contribution $346, net −$2,914 ✓. Closing 28,256 − 2,914 = 25,342 ✓.

Month 9: contribution $1,822, net −$1,438 ✓. Closing 25,342 − (months 7,8,9 nets). Months 7+8+9 total net = 19,278 − 25,342 = −6,064. Month 9 net −1,438, so months 7+8 = −4,626, i.e., avg −2,313 each. Contribution month 7 ≈ 3,260−2,313 = $947? Revenue month 7 ~ $2,900? Interpolating between month 6 ($1,426) and month 9 ($4,409): month 7 ~$2,400, month 8 ~$3,300. Contribution at ~50% of revenue: ~$1,200 and ~$1,650. Hmm, contribution/revenue ratio: month 6: 346/1,426 = 24.3%. Month 9: 1,822/4,409 = 41.3%. Month 12: 5,434/10,834 = 50.2%. The contribution margin as % of revenue rises because fixed audit $1.90/task is a smaller share as ticket grows. Let me check month 9: tasks 1,150, avg ticket $54. Fee-only contribution per task: 6%×54 = $3.24 − 1.90 − 0.35 = $0.99. Blended: 7.1%×54 = $3.834 − 2.25 = $1.584. × 1,150 = $1,821.6 → $1,822 ✓. 

Month 6: 480 tasks, $45. Blended 6.6%×45 = $2.97 − 2.25 = $0.72 × 480 = $345.6 → $346 ✓.

Month 3: 120 tasks, $42. 6.0%×42 = $2.52 − 2.25 = $0.27 × 120 = $32.4 → $32 ✓.

Month 12: 2,400 × (7.4%×61 − 2.25) = 2,400 × (4.514−2.25) = 2,400 × 2.264 = 5,433.6 ✓.

Month 4: revenue $640, contribution $100. Tasks? If avg ticket ~$43, tasks ≈ 15. 6.2%×43 = 2.67 − 2.25 = 0.42 × 15 = $6.3. Hmm, $100 contribution on $640 revenue = 15.6%. To get $100 contribution: contribution/task ~0.42 → 238 tasks? But revenue $640/238 = $2.69 avg ticket. Inconsistent. Or fewer tasks with higher contribution. Actually month 4 revenue $640: if avg ticket $42, ~15 tasks, contribution should be ~$6, not $100. This looks like an inconsistency. Let me check: month 3 revenue $302, contribution $32 (10.6% of revenue). Month 4 revenue $640, contribution $100 (15.6%). Month 5 revenue $1,014, contribution $204 (20.1%). Month 6 $1,426 → $346 (24.3%). The progression of contribution margin % of revenue: 10.6%, 15.6%, 20.1%, 24.3%, then month 9 41.3%, month 10 44.5%, month 11 47.5%, month 12 50.2%. Given fixed audit cost per task, contribution margin % of revenue rises with ticket. But month 3→6 avg ticket only rises $42→$45, yet margin % nearly doubles from 10.6% to 24.3%. Let me compute what margin % should be at ticket $45, blended 6.6%: contribution/task = 0.72, revenue/task = 2.97, margin = 24.2% ✓ matches month 6. At ticket $42, 6.0%: 0.27/2.52 = 10.7% ✓ matches month 3. At month 4: to get 15.6% margin, need contribution/task ÷ revenue/task = 0.156. With blended take t and ticket p: (t·p − 2.25)/(t·p) = 0.156 → t·p(1−0.156) = 2.25 → t·p = 2.666. If t = 6.2%, p = $43. So contribution/task = 0.416, tasks = 640/43 ≈ 14.9 → contribution = $6.2, not $100. Wait, I conflated. Contribution total = tasks × per-task contribution = 14.9 × 0.416 = $6.2. But table says $100. So month 4 contribution is inconsistent: $100 vs ~$6. Hmm wait, let me recheck month 5: revenue $1,014, contribution $204. If avg ticket ~$44, tasks ≈ 23, per-task contribution at 6.4%: 0.44×... 6.4%×44 = 2.816 − 2.25 = 0.19 × 23 = $4.4. Not $204. So months 4 and 5 contributions look way off... unless task counts are much higher with lower tickets. Month 5: contribution $204. If per-task contribution is $0.19, tasks = 1,074, revenue = 1,074 × 44 = $47k, not $1,014. Contradiction.

Hmm wait, maybe I should reconsider: maybe contribution here isn't per the unit economics. Let me check month 6 again: 480 tasks stated in revenue table, contribution $346 → per task $0.72 ✓ consistent. Month 9: 1,150 tasks, $1,822 → $1.58/task ✓. Month 12: 2,400, $5,434 → $2.26 ✓. Month 3: 120 tasks, $32 → $0.27 ✓. So months 3, 6, 9, 12 are consistent. Months 1, 4, 5, 10, 11 are interpolated. Month 4: revenue $640. Interpolating tasks between 120 (m3) and 480 (m6): m4 ~ 240 tasks? Revenue $640/240 = $2.67 ticket — no. Interpolating revenue between 302 and 1,426: m4 ~ $640 ✓ linear-ish. Tasks m4 ~ 240, ticket $2.67? That contradicts avg ticket $42-45. Actually if tasks interpolate 120→480, m4 = 240, m5 = 360. Revenue m4 = 240 × 42 = $10,080, not $640. So the revenue table itself (tasks × ticket = GMV) doesn't interpolate linearly — month 3 GMV $5,040 but month 4 revenue only $640? Month 3 revenue $302 = 6% of $5,040 GMV. Month 4 revenue $640 implies GMV ~$10,300 at 6.2%. But month 6 GMV is only $21,600. So month 4 GMV $10,300 vs month 3 $5,040 and month 6 $21,600 — plausible growth actually (5.0k → 10.3k → ~15k? → 21.6k). OK so GMV grows smoothly. Then tasks m4 = 10,300/43 ≈ 240. Contribution should be 240 × 0.42 ≈ $100. Oh! That works. 240 tasks × $0.416 = $99.8 ≈ $100 ✓. I made an error before: 640/43 ≈ 14.9 — no wait, revenue $640 is the fee revenue, not GMV. GMV = revenue/take = 640/0.062 ≈ $10,323. Tasks = 10,323/43 ≈ 240. Contribution = 240 × (0.062×43 − 2.25) = 240 × 0.416 = $100 ✓. 

Month 5: revenue $1,014, take ~6.4% → GMV $15,844, tasks ~360 (interpolating 240→480), ticket $44. Contribution = 360 × (0.064×44 − 2.25) = 360 × 0.566 = $204 ✓. 

Month 1: revenue $72, contribution $4. Take 6%, GMV $1,200, tasks ~30 (weeks 1-4: 20 tasks sourced weeks 3-4... month 1 is weeks 1-4). 30 tasks × (0.06×40 − 2.25) = 30 × 0.15 = $4.5 ≈ $4 ✓. OK.

Month 10: revenue $6,354, contribution $2,829. Take ~7.25%? GMV = 6,354/0.0725 ≈ $87,641. Tasks interpolate 1,150→2,400: m10 ≈ 1,567. Ticket = 87,641/1,567 ≈ $55.9. Contribution/task = 0.0725×55.9 − 2.25 = 4.053 − 2.25 = 1.803 × 1,567 = $2,825 ≈ $2,829 ✓ roughly.

Month 11: revenue $8,494, contribution $4,031. Take 7.3%? GMV = 116,356. Tasks ~1,983. Ticket $58.7. Contribution/task = 0.073×58.7 − 2.25 = 4.285−2.25 = 2.035 × 1,983 = $4,035 ≈ $4,031 ✓.

OK so the cash table is broadly consistent. Good.

Now check specific claims:

1. "break-even at roughly 1,450 settled tasks per month at that blend (2,310 if only the settlement fee counted)" — computed 1,440 and 2,312. Header says 1,450 and 2,310; section 07 says 1,440 and 2,312. Cosmetic rounding inconsistencies.

2. "crossed in month 11" — month 11 net +$771 ✓ blended; fee-only month 12 +$124 ✓.

3. "Month 12 annualises to $130k of run-rate revenue" — 10,834 × 12 = $130,008 ✓.

4. Escrow float: "nine-day holds at ~3.5% APY on month-12 GMV are about $128 a month". GMV $146,400/month. Float = GMV × 9/30 ≈ $43,920 average held. At 3.5% APY: 43,920 × 0.035 = $1,537/year = $128/month ✓. Good.

5. "1.2% of month-12 revenue" — 128/10,834 = 1.18% ✓.

6. Worker keeps: $61 − 6% fee = $57.34; less $0.36 inference = $56.98 ✓. 56.98/61 = 93.4% ✓.

7. Rate table: 4%: fee $2.44, worker keeps 61−2.44 = 58.56, less 0.36 = 58.20 ✓ (95.4% of 61 = 58.19 ✓). Protocol keeps after audit+infra: 2.44 − 1.90 − 0.35 = 0.19 ✓. 8%: 4.88 − 2.25 = 2.63 ✓. 10%: 6.10 − 2.25 = 3.85 ✓. Worker keeps 8%: 61−4.88−0.36 = 55.76 ✓ (91.4%). 10%: 61−6.10−0.36 = 54.54 ✓ (89.4% ✓).

8. Inference: 60k in × $3/M = $0.18; 12k out × $15/M = $0.18; total $0.36 ✓.

9. Worker break-even ticket: "A $0.39 ticket. An hour-long session at 50k input and 15k output tokens costs $0.38" — 50k×$3/M = $0.15; 15k×$15/M = $0.225; total $0.375 ≈ $0.38 ✓. But "a $0.39 ticket" as worker break-even — worker keeps 94% of ticket, so break-even ticket = 0.38/0.94 = $0.404, not $0.39. Minor. Actually if fee is 6%, worker nets 0.94×ticket; 0.375/0.94 = $0.399 ≈ $0.40. They say $0.39. Cosmetic.

10. Audit sensitivity table: 
- 5% sample: audit = 0.5×1.90 = $0.95. Contribution = 3.66 − 0.95 − 0.35 = $2.36 ✓. Break-even: 3,260/2.36 = 1,381.4 ✓.
- 10%: $1.41, 2,312 ✓.
- 15%: audit 2.85; 3.66−2.85−0.35 = $0.46 ✓. Break-even 3,260/0.46 = 7,087 ✓.
- 20%: audit 3.80; 3.66−3.80−0.35 = −$0.49 ✓ "never" ✓.

11. Ticket sensitivity:
- $2.25: fee 0.135 → $0.14 ✓; contribution 0.135−1.90−0.35 = −$2.115 → −$2.12 ✓.
- $15: 0.90 − 2.25 = −$1.35 ✓.
- $25: 1.50 − 2.25 = −$0.75 ✓.
- $38: 2.28 − 2.25 = +$0.03 ✓.
- $61: +$1.41 ✓.
- $150: 9.00 − 2.25 = +$6.75 ✓.
Floor: fee = audit + gas → 0.06p = 2.25 → p = $37.50 ✓.

12. Small-task lane: "$12 average... contributes $0.70 a task — 97% of its fee". Fee at 6% × 12 = $0.72. Contribution = 0.72 − gas 0.02 = $0.70 ✓. 0.70/0.72 = 97.2% ✓. "would need about 4,660 tasks a month to carry the fixed base": 3,260/0.70 = 4,657 ✓.

13. Verification ratio table: $61: fee 3.66, audit 1.90, audit/fee = 51.9% → 52% ✓; audit/GMV = 1.90/61 = 3.11% ✓. $120: 7.20, 26.4% → 26% ✓; 1.58% ✓. $158: 9.48, 20.04% → 20% ✓; 1.20% ✓.

14. Triage trader: "at month 12 that is a $1,464/mo pool" — 1% of GMV 146,400 = $1,464 ✓. "a desk holding $500 and capturing 10% of flow earns ~$146" ✓.

15. Seed arithmetic: buckets: 9,000 + 6,500 + 4,000 + 3,200 + 2,000 + 2,000 = 26,700 ✓. "$14,200 of operating cash after the one-offs": one-offs = 6,500 + 4,000 + 2,000 = 12,500; 26,700 − 12,500 = 14,200 ✓. But then it says "Of those $10,500 of contracts and liquidity" — 6,500 + 4,000 = 10,500 ✓ (contracts + liquidity, excluding subsidy). "the prize covers $9,900 and the $600 difference is founders' money" — 10,500 − 9,900 = 600 ✓. Prize ~$9.9k (0.5 ETH at $2,235 = $1,117.50 + 4,000 USDC = $5,117.50). Wait! 0.5 ETH at $2,235 = $1,117.50. Plus $4,000 = $5,117.50, not $9.9k!

Hold on. ETH at $2,235 (stated: "ETH at $2,235, the price the revenue model uses"). 0.5 ETH = $1,117.50. Prize = $1,117.50 + $4,000 = $5,117.50. The plan says "The prize (0.5 ETH + 4,000 USDC, roughly $9.9k at current prices)". That's wrong by their own ETH price! $9.9k would need ETH at ~$11,800. This is a real arithmetic error — internal inconsistency. They use ETH = $2,235 for the model but $9.9k for the prize implies ETH ≈ $11,800. FATAL? It's an embarrassing inconsistency: at their own ETH price the prize is ~$5.1k, not $9.9k. That breaks: "the prize covers $9,900" of the $10,500; actually it covers $5,117.50, leaving $5,382.50 founders' money, not $600. And "$16,800 if the prize lands" — 26,700 − 9,900 = 16,800 ✓ internally, but with correct prize value it'd be 26,700 − 5,117.50 = $21,582.50. This is a genuine arithmetic/consistency error. Is it fatal? It's a significant error in the funding section — the plan's whole "what the prize buys" framing collapses. I'd call it fatal-adjacent; at minimum a major embarrassing inconsistency. Given the brief emphasizes credibility, mispricing the prize by ~2× using their own stated ETH price is a serious flaw. I'll flag it as fatal consistency error (FATAL_CONSISTENCY: yes).

Wait — maybe ETH price: they say "ETH at $2,235, the price the revenue model uses". Hmm, current ETH in Nov 2026 (fictional) — unverified. But internal consistency: $9.9k prize requires 0.5 ETH = $5,900 → ETH = $11,800. Contradiction with $2,235. Definitely inconsistent.

Also "roughly $9.9k at current prices" — even at ETH $2,235, 0.5 ETH + 4,000 = $5,118. So the $9.9k is flat wrong given their own number.

16. Cash trough: "the month-4 trough of −$1,312 sits inside it" — reserve $2,000, trough $1,312 ✓ sits inside.

17. "4.4 months at zero revenue": 14,200/3,260 = 4.356 ✓.

18. Month-12 revenue shares: settlement 81%, others 19% (7+8+4) ✓ = 100%.

19. Blended take decomposition: 6.0% + 1.4% = 7.4% ✓. Check: other lines revenue $2,050 on GMV $146,400 = 1.40% ✓.

20. "the $40–80 band and the $150+ band are both in the audited lane — about $1.33" — 70% of tasks audited at 10% sample: 0.7 × 0.1 × 19 = $1.33 ✓. And they charge $1.90 (full 10% of all tasks) — overstating by $0.57 ✓.

21. Mix check: 60% × $60 + 30% × $12 + 10% × $220 = 36 + 3.6 + 22 = $61.60 ✓. But wait: 60% of tasks at $40–80 average ~$60 — but the audited lane starts at $40 and small lane is $1–40. The mix says 30% at $5–25 (small lane) — fine. But then "the mix implies an audit on 70% of them" — 60% + 10% = 70% ✓.

Hmm, but wait: the audited lane requires tickets ≥ $40 for the 10% sample; tasks above $1,000 get 100% audit. The mix's 10% above $150 average $220 — fine, below $1,000.

But there's a subtle issue: the unit economics charges $0.35 gas+sandbox to every task, but the small-task lane has gas batched to ~$0.02. Minor.

22. "an 8% board and a 6% board differ by $1.22 on a $61 task" — 2% × 61 = $1.22 ✓.

23. Metered rail: "at $0.05 a $0.0002 fee would be 0.4% of the ticket" — 1.5%? No: they say a fixed $0.0002 fee... hmm, "at $0.05 a $0.0002 fee would be 0.4% of the ticket, but at $0.001 it would be 20%". 0.0002/0.05 = 0.4% ✓; 0.0002/0.001 = 20% ✓. OK but where does $0.0002 come from? Presumably 1.5%... no, 1.5% of 0.05 = $0.00075. The $0.0002 seems to be a hypothetical fixed per-call settlement cost. Fine as illustration. Actually earlier table says "This plan: $0.00075 (1.5%)" for the $0.05 call ✓ (1.5% × 0.05 = 0.00075).

24. "calls under $1 settle in batches of 500 against one settlement... a buyer's balance settles when it crosses $0.50, roughly ten calls at five cents" — batches of 500 vs settle at $0.50 (~10 calls)? Inconsistent: "batches of 500" vs "$0.50, roughly ten calls". 500 calls at $0.05 = $25, not $0.50. Internal contradiction between "batches of 500" and "crosses $0.50, roughly ten calls". Cosmetic-to-moderate inconsistency. Hmm, maybe batches of 500 calls per on-chain settlement transaction (batching 500 calls into one tx), and each buyer's balance settles at $0.50. Those could coexist but it's confusing. Flag as unlabelled inconsistency.

25. Section 00 census: "Fifty-five entries are on the board" vs document C says "83 claims are on this bounty". The plan says 55 entries, written 9 Nov; document C (presumably current) says 83 claims. Also "Written after reading all 54 entries already on the board" in the header vs "Fifty-five entries" in section 00 vs "the 54-entry convergence table" in the check section. Internal inconsistency: 54 vs 55. And vs document C's 83. The 54/55 discrepancy: header says 54, section 00 says 55 ("Fifty-five entries are on the board... of 55"). Also "Median entry: 965 characters" — fine. The count mismatch with the actual board (83) makes the census stale/understated — but the plan is dated 9 Nov; document C is "already on the board" now. Since the plan claims to have read "all 54/55", and there are 83 now, the census is outdated — but more importantly the internal 54 vs 55 inconsistency is sloppy. Flag.

Also "45 of 55 name a concrete 90-day revenue number" — but the row says "Futarchy over one welfare metric | 45". Then "29 name a concrete 90-day revenue number". OK.

26. Seer depth measurement: "3,051 markets, of which 1,153 are conditional". Document C claim 9558 says "Of 2,446 unresolved Seer markets on 4 chains, 178 are still open for trading". The plan addresses a discrepancy with "an earlier entrant... reports 548 conditional markets, which is exactly the Gnosis subset". The plan's numbers (3,051 total, 1,153 conditional) vs claim 9558's (2,446 unresolved, 178 open for trading). These measure different things (total vs unresolved vs open). Not necessarily contradictory. Unverified either way — I can't check. Note as unverified.

27. "Two markets, live on Base since this morning" — market addresses, tx hashes. Unverifiable to me. The plan admits books are empty and the wallet holds 0.0051 ETH and cannot answer (0.01 ETH bond needed). Honest. But note: creating markets on Seer — does Seer have a Base deployment? Document C claim 9558 mentions "2,446 unresolved Seer markets on 4 chains" and claim 9570/9425 "created Seer markets on Base". So plausible. Unverified specifics.

Also: "cost 0.0000371 ETH in gas (about $0.08)" — 0.0000371 × 2,235 = $0.0829 ✓ consistent with their ETH price. Interesting — so they DO use $2,235 elsewhere, making the $9.9k prize figure even more clearly wrong.

28. "the 0.01 ETH in the market parameters is the minimum a respondent posts to Reality.eth" — unverified about Seer mechanics; plausible (Reality.eth minimum bond). Can't verify; note as unverified but plausible.

29. "Futarchy markets on Gnosis" in section 02 constitution — but then they create markets on Base, and measure 602 conditional on Optimism, 548 Gnosis, 3 Base. Seer is multichain. Saying "futarchy markets on Gnosis" as the constitution while the measurement shows Gnosis is only part — minor inconsistency; also "Markets are price-based decision markets on Gnosis" in section 10. Given their own data shows Seer on multiple chains, pinning to Gnosis is a factual wobble. Minor.

30. "Seer already wrote the thesis on its own site: with AI, the cost of reviewing work is more than the time it takes to do it" — unverified quote, plausible.

31. "poidh bounties ($2–$1,208)" vs later "poidh's live bounties run $2 to $25" — contradiction! Section 03: "calibrated against observed poidh bounties ($2–$1,208)". Section 07: "poidh's live bounties run $2 to $25, and none of them has an acceptance test." These can be reconciled (observed range historically vs currently live), but as written it's a flat contradiction: $2–$1,208 vs $2–$25. Also section 08: "Most of the public bounty boards run at exactly that size, $2 to $25". And section 01 mentions "$2 pot" bounty. And buyer stats: "Median lifetime spend among payers is $11.81, mean $75.94, ninetieth percentile $122.92; 18 wallets have spent over $100 and two over $1,000". If only two wallets spent over $1,000 lifetime, a $1,208 single bounty is possible. But "poidh's live bounties run $2 to $25" vs "observed poidh bounties ($2–$1,208)" — needs reconciliation; as written, contradictory. Flag as internal inconsistency (moderate).

32. Buyer base: "193 wallets have ever posted one, 140 have had a bounty accepted... 43 of those 140 — 30.7% — came back". 43/140 = 30.71% ✓. Segment table: 53 + 97 + 43 = 193 ✓. "Settled once 97 — 31% [share of spend]"; "Settled twice or more 43 — 69%". 31+69 = 100 ✓. "top ten carry 70.6%" — plausible. Mean $75.94 × 140 = $10,631 total spend; top ten 70.6% = $7,506; two over $1,000... plausible. OK.

33. "A task at the model's $60 average earns $3.60 of fee" — 6% × 60 = $3.60 ✓ (though elsewhere avg is $61 → $3.66; minor). "A repeat buyer settling three tasks a month is worth $10.80" ✓. "twenty approaches a week at a loaded $35 an hour — costs about $1,400 a month" — 20 approaches/week; how many hours? If each approach takes ~4 hours → 80 hrs/month × 35 = $2,800. If 2 hrs → $1,400. Unlabelled assumption but roughly plausible. "at a generous 8% approach-to-first-post conversion that is roughly $1,080 per first poster" — 80 approaches/month × 8% = 6.4 posters; 1,400/6.4 = $218.75, not $1,080! Wait: "twenty approaches a week" = ~87/month. 8% conversion → 7 posters. $1,400/7 = $200/poster. To get $1,080/poster you'd need conversion of 1,400/(1,080) → 1.3 posters from 87 approaches = 1.5% conversion. So either the 8% is wrong or the $1,080 is wrong. Hmm, unless "approach-to-first-post conversion" of 8% means 8% of approaches lead to a first post... $1,400 / (87 × 0.08) = $1,400/6.96 = $201. The plan says "roughly $1,080 per first poster". That's 5× off. Then "A first poster recovers that in a hundred months" — 1,080/10.80 = 100 months ✓ internally consistent with $1,080, but the $1,080 doesn't follow from 8% conversion of 20/week. Let me double check: maybe they mean $35/hour loaded and each approach takes... to cost $1,400/month with 20 approaches/week (~87/month), that's $16/approach → 27 min each. OK. Conversion 8% → 7 posters. $1,400/7 = $200. So "$1,080 per first poster" is wrong by 5.4×, OR the conversion implied is ~1.5% not 8%. Either way the stated numbers don't close. This is a genuine arithmetic error. Is it fatal? It's in the argument that paid acquisition doesn't work — the conclusion (CAC >> LTV) holds even more strongly at $200/poster vs $10.80/month value (still 18+ months payback... actually $200/$10.80 = 18.5 months, still bad). So conclusion robust, number wrong. Flag as arithmetic error, not fatal to conclusion but embarrassing in a plan that brags about recomputability.

Hmm wait, maybe "8% approach-to-first-post" — maybe approaches convert to first POST at 8%, but a poster who posts once... and the $1,080 is per first poster who then... no. $1,400/month ÷ (87 × 0.08) = $201. The $1,080 would require ~1.3 posters/month. So the numbers don't close. Definitely flag.

34. "the count falls 85%" — 3/20 read vs 20: reading 3 instead of 20 = 85% reduction ✓.

35. "Median all-in buyer cost ≤1.6× the accepted bid" — fine.

36. "month-6 revenue" cap: desk contract "capped at 15% of month-6 revenue" — month 6 revenue $1,426; 15% = $214. Desk at 10% of settled prize... fine.

37. "nine-day holds" vs worker "payouts slower than a day" push-out — poster escrow held ~9 days, worker paid... fine.

38. Ledger table: "$61.61 in from the poster" — $61 ticket + 1% triage ($0.61) = $61.61 ✓. Worker takes $57.34 released from escrow: 61 − 3.66 = 57.34 ✓, less 0.36 inference → +56.98 ✓ (92.5% of 61 = 56.4... 56.98/61 = 93.4%. They say 92.5%. Hmm: 56.98/61.61 = 92.48% → 92.5% if measured against $61.61 total in. But earlier "Worker agent | 92.5% of the ticket" in "Why each party stays" — 56.98/61 = 93.4%. Inconsistent base: 92.5% (of $61.61) vs 93.4% (of $61). In the ledger the % column is "% of ticket" and poster is 101% (61.61/61). So worker 56.98/61 = 93.4%, not 92.5%. But if % of $61.61, poster would be 100%. The ledger's % column: poster 101% → base is $61 ticket. Worker 92.5% → should be 93.4%. Error! Let me check others: model provider 0.36/61 = 0.59% → 0.6% ✓. Triage 0.61/61 = 1.0% ✓. Auditor 1.90/61 = 3.11% → 3.1% ✓. Infra 0.35/61 = 0.57% → 0.6% ✓. Foreguild 1.41/61 = 2.31% → 2.3% ✓. Sum: 101 + 93.4 + 0.6 + 1.0 + 3.1 + 0.6 + 2.3 = 202%? The ledger says "the last column sums to zero" — meaning nets sum to zero: −61.61 + 56.98 + 0.36 + 0.61 + 1.90 + 0.35 + 1.41 = 0.00? Let's check: −61.61 + 56.98 = −4.63; +0.36 = −4.27; +0.61 = −3.66; +1.90 = −2.37; +0.35 = −2.02; +1.41 = −0.61. Not zero! Off by −$0.61. Hmm. Wait — dispute jurors $0. Let me recount: poster −61.61; worker +56.98; model +0.36; triage +0.61; auditor +1.90; jurors 0; infra +0.35; foreguild +1.41. Sum of positives: 56.98+0.36+0.61+1.90+0.35+1.41 = 61.61. −61.61 + 61.61 = 0 ✓. I mis-added: 56.98+0.36 = 57.34; +0.61 = 57.95; +1.90 = 59.85; +0.35 = 60.20; +1.41 = 61.61 ✓. Great, sums to zero. But wait — the worker's net is stated as "+$56.98" which is already net of $0.36 inference paid to model provider. And model provider separately gets +$0.36. So the worker's "takes out $57.34... less $0.36 of inference → +$56.98" and model +0.36 — consistent, no double count ✓. And Foreguild "+$1.41" with note "plus $2.25 of the fee it collects, paid straight out to audit and gas" — 3.66 − 1.41 = 2.25 ✓. Good, ledger closes.

But the worker % — 92.5% vs 93.4%. In the ledger, "% of ticket" column: worker 92.5%. 56.98/61 = 93.41%. 56.98/61.61 = 92.48%. Poster listed at 101% = 61.61/61. So the column base is $61 ticket, and worker should be 93.4%. The 92.5% appears to be computed against $61.61. Inconsistent base within one column. Also "Why each party stays" table says "Worker agent | 92.5% of the ticket". Minor arithmetic slip (cosmetic but sloppy in a plan whose selling point is arithmetic rigor).

39. "Foreguild | $1.41 per task, $2.26 at the blended take | 2,312 tasks/mo on fee alone, 1,440 at the blend" ✓ consistent.

40. "Contribution at 7.4% blend $2.26/task (50%)" — 2.26/4.51 = 50.1% ✓ (as % of blended fee). OK.

41. Month-12 profit "~$2,174" ✓.

42. "the $2,050 gap between the two paths is an assumption" — 5,434 − 3,384 = 2,050 ✓.

43. Header: "Target: $146,400 of GMV in month 12 at a 7.4% blended take, which is $10,834 of monthly revenue against a fixed cost base of $3,260 — break-even at roughly 1,450 settled tasks per month at that blend (2,310 if only the settlement fee counted), crossed in month 11." — 1,450 vs computed 1,440; 2,310 vs 2,312. Cosmetic.

44. "Escalation... gated on size: a decision escalates only when the stake exceeds 8× the cost of the next step" — fine.

45. "0.05 ETH" bond start — at $2,235 = $111.75. Fine.

46. "the prize... roughly $9.9k" — THE big error as established. Also "it funds the contracts and the seed liquidity" — contracts $6,500 + liquidity $4,000 = $10,500; prize claimed $9,900. With correct prize $5,118, it doesn't cover them. Also "That also fixes what cheque is being asked for... $16,800 if the prize lands and $26,700 if it does not" — 26,700 − 9,900 = 16,800 ✓ internally but built on the wrong prize value.

Also note: the brief says if submitted through Poidh, winner gets 0.5 ETH Poidh bounty + 4,000 USDC from Seer. The plan treats the prize as "the first tranche" of funding — but the plan hasn't won yet; counting the prize as committed capital is speculative. The plan does hedge ("if the prize lands"). But treating a contest prize you haven't won as tranche 1 of your treasury is a credibility issue — though they do hedge with the $26,700 path. Actually they say "the prize is treated as the first tranche" and separately "$26,700 if it does not [land]". Hmm, they say "$16,800 if the prize lands and $26,700 if it does not, with the month-5 tranche sized for the second case." OK, hedged. But the $9.9k valuation error propagates.

47. "0.5 ETH Poidh bounty plus 4,000 USDC" — the plan says "roughly $9.9k at current prices". Even at ETH = $11,800... The plan's own ETH price is $2,235. So error confirmed.

48. Section 00: "of 55" table — "Futarchy over one welfare metric | 45" then "29 name a concrete 90-day revenue number". Fine.

49. "Median entry: 965 characters. The longest is 3,308, the shortest 20" — fine.

50. "we counted... 27 projects" — that's claim 9568's number, not this plan.

51. "3,051 markets fetched in 31 pages" — 3,051/31 ≈ 98.4/page. Fine.

52. "1,153 conditional... 125 funded... three clear $1,000, and exactly one clears $3,000 ($7,598)". Then later: "Two of 68 markets clear it today, and neither is a branch." Wait — "two markets clear both halves of a depth threshold at once — the National Rally candidacy ($7,185 of liquidity, 49 traders) and the National Assembly seat count ($6,791, 49)". These are parents. And "the Le Pen candidacy market has 49 traders, and its own child... is the deepest branch on the board at $7,598 and carries 9" — the branch has $7,598 liquidity but only 9 traders, so doesn't clear 20 traders. Consistent with "neither is a branch" (the two clearing both thresholds are parents). But earlier: "Eighteen clear $1,000; none clears $10,000" (all markets) and "three clear $1,000 [conditional], and exactly one clears $3,000 ($7,598)". The branch at $7,598 clears $3,000 liquidity but has 9 traders < 20 → doesn't clear both. Consistent. OK.

But: "a decision binds when the market holds ≥$3,000 of liquidity and ≥20 addresses with non-zero volume... Two of 68 markets clear it today, and neither is a branch." The 68 markets are those above $50 liquidity from trader_depth. Fine.

53. "the National Rally candidacy ($7,185 of liquidity, 49 traders)" — but earlier "the busiest has 50" traders. 49 ≤ 50 ✓.

54. Prediction 6: "One fee decision resolved by a market holding ≥$3,000 and ≥20 traders | 2027-08-15". Fine.

55. "3,051 markets fetched in 31 pages" — fine.

56. "Of the 1,153 conditional markets, 602 are on Optimism, 548 on Gnosis and 3 on Base" — 602+548+3 = 1,153 ✓. "The whole conditional set holds $13,446" and "$13,436 Gnosis + $10 Optimism + $0 Base" = 13,446 ✓.

57. "an earlier entrant on this bounty reports 548 conditional markets, which is exactly the Gnosis subset" — this refers to claim 9558? Claim 9558 says "178 are still open for trading" — hmm, that doesn't mention 548 conditional. Document C claim 9558: "Of 2,446 unresolved Seer markets on 4 chains, 178 are still open for trading, and none holds $1,000 of depth." No 548. The plan says "an earlier entrant... reports 548 conditional markets". Not in the visible excerpts of C. Unverified — can't confirm any entrant reported 548. Possibly in a trimmed portion. I'll note unverified.

58. "the National Rally candidacy... and the National Assembly seat count" — French election markets on Seer. Unverified but plausible.

59. "Seer's Opportunity Markets (revenue thesis... pilot on the rebrand, Devcon merch and the naming of this job board)" — unverified.

60. "poidh #1531, Base" — from claim 9553. Fine.

61. Section 05: "after a threshold (default: 5 claims), new claims must beat the current best by a stated margin" — fine.

62. "the poster reads the top k by price (default k = 3)" — fine.

63. Week 9–10 milestone: "First advisory futarchy market live... No market reaches $3,000 of liquidity with 20 traders by month 12 — then the fee stays a multisig decision" — kill criterion listed for weeks 9-10 but references month 12; odd placement but fine.

64. "Month 12: 2,400 tasks" vs "break-even at roughly 1,450" — fine.

65. Revenue line shares: settlement 81%, upgrade 7%, data 8%, cert 4%. Check against rates: full-audit upgrade $25 flat on tasks above $250 — 7% of $10,834 = $758/month → ~30 upgrades/month. Data: $4–12/pair, 8% = $867 → ~100-200 pairs. Cert: $25–150, 4% = $433 → few certs. Plausible-ish. Fine.

66. "Blend at month 12: 6.0% settlement + 1.4% from the other three lines = 7.4%" ✓.

67. "A $25 audit upgrade on a $19 audit is $6 of margin, not $25" ✓ — good honesty.

68. "month-12 GMV... nine-day holds" — but disputes/escrow: fine.

69. "the metered rail is capped at $1 by construction" vs "Ticket | $0.001–$1.00" ✓ consistent. But "a $
