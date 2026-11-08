## 1. Headline profitability contradicts the body, and the difference is uncosted

**Quote (header):** "break-even at roughly 1,450 settled tasks per month at that blend (2,310 if only the settlement fee counted), crossed in month 11."
**Quote (§07):** "the honest profit figure is the fee-only one — +$124 in month 12, break-even in month 12 rather than month 11 — and the $2,050 gap between the two paths is an assumption about ancillary margin, not a measurement."

The blended contribution of $2.26/task, the "+$2,174" month-12 profit, the month-11 crossing and the whole cash curve all run on the blended path, which the plan itself says is not costed. Worse, one of its own cost figures is published: "A $25 audit upgrade on a $19 audit is $6 of margin, not $25." The upgrade line is 7% of $10,834 ≈ $758 of revenue, i.e. ~30 upgrades; at the plan's own $19 cost that is ~$576 of unmodelled cost, so month-12 profit is ~$1,598, not $2,174, before touching licensing or certification cost. The cash table (closing $21,792) inherits the overstatement every month.

**Minimal fix:** run the 12-month cash table on fee-only contribution ($1.41/task), and show ancillary lines net of their stated costs ($6 per upgrade, a cost per verified pair, a cost per exam) as a separate row.

## 2. The ledger that is asserted to close does not

**Quote:** "The ledger closes: $61.61 in from the poster, $61.61 out to the people who did the work, ranked it, audited it, or settled it."

Summing the table's own "Net per task" column: −61.61 + 56.98 + 0.36 + 0.61 + 0 + 0 + 1.41 = **−$2.25**. The auditor is shown receiving "$1.90 expected per task" but netted at "$0 at pool level", and the $0.35 of gas/sandbox has no party row at all. $1.90 + $0.35 = $2.25 — exactly the gap.

**Minimal fix:** give the auditor a net of +$1.90 and add an infrastructure/gas row of +$0.35, or state the column is "net to party excluding cost pools" and show the reconciling line.

## 3. The prize is both excluded from and counted as capital

**Quote:** "the contest prize is a reward to the author, not capital the protocol already holds."
**Quote:** "The prize (0.5 ETH + 4,000 USDC, roughly $9.9k at current prices) covers about a third of the seed, so it is treated as the first tranche: it funds the contracts and the seed liquidity."

If $9.9k of the $26.7k is prize money, the external ask now is ~$16.8k and the total is ~$46.8k, not the "~$56.7k total — ~$26.7k seed now" in the header. A funder cannot tell what cheque is being requested, or whether the tranche-5 ask is still $30k if the prize is not won.

**Minimal fix:** state the ask as "external cash required: $X now, conditional on prize outcome Y/N", and show both the prize-won and prize-lost cash curves.

## 4. The reserve is spent in the base case while being described as untouched

**Quote:** "Reserve | $2,000 | Untouched; funds one dispute storm or one bad month."
**Quote:** "$1,312 — trough without the tranche."

The $2,000 reserve sits inside the "$14,200 of operating cash" that the cash table burns down. A month-4 closing balance of $1,312 means the reserve has already been consumed in the plan's own base case; there is no dispute-storm buffer left when the tranche decision is made.

**Minimal fix:** ring-fence the $2,000 (operating cash $12,200, trough −$688 in month 4, tranche needed by month 4), or delete the reserve line.

## 5. The small-task lane is costed off a ticket the mix does not contain

**Quote:** "The small-task lane covers $1–$40 at the same 6% ... At a $19 median ticket it contributes $1.12 a task — 98% of its fee — and it would need 2,900 tasks a month to carry the fixed base on its own."
**Quote (same section's mix):** "30% at $5–$25 (average ~$12, the small-task lane)."

At the mix's own $12 average, the lane's fee is $0.72, contribution ≈ $0.70 after the stated $0.02 gas, and standalone break-even is ~4,660 tasks, not 2,900. The $19 figure is 58% above the band average used to build the $61 ticket.

**Minimal fix:** use $12 for the small lane throughout, or change the mix band and re-derive the $61.60 average.

## 6. An 85% review reduction is presented as achieved, is a count ratio, and contradicts the milestone target

**Quote:** "In the common case n = 20 and k = 3, the poster's own reading drops by 85% without any model in the loop."
**Quote (§11):** "measure review-time saved against a control week of full review | Kill criterion: Review time not reduced by ≥40%."

17/20 submissions unread is not 85% less reading time — the top-3 are read more carefully, and the discarded 17 are the ones a poster skims fastest. The plan's own measurement plan has not been run, and its pass bar is less than half the number quoted as the product's core benefit.

**Minimal fix:** write it as "reads 3 of 20 submissions; time saved unmeasured, target ≥40%, measured in weeks 5–6."