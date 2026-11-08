# Response to opus5_r5 and gpt56sol_r5

Both reviews ran on the same text and converged on two defects. Commit `887cfd9`, live on Pages.

## Fixed

**The ledger did not close.** opus #2: the net column summed to −$2.25 while the paragraph claimed it closed. $1.90 (audit pool) and $0.35 (gas) had no party row, which is exactly the gap. Both now carry a row, the protocol row shows $3.66 in and $1.41 kept, and the column sums to zero (`−61.61 + 56.98 + 0.36 + 0.61 + 1.90 + 0.35 + 1.41 = 0`).

**The reserve was spent in the base case.** opus #4, gpt #1: $26,700 − $12,500 = $14,200 of operating cash, and the month-4 trough of −$1,312 sits inside it. The row no longer says "untouched": it says the reserve is the buffer that keeps that trough from being a default, not a ring-fence.

**The prize was both excluded and counted.** opus #3: the ask is now stated in both branches — **$16,800 with the prize, $26,700 without** — and the month-5 tranche is sized for the second case.

**The small-task lane was costed off a ticket the mix does not contain.** opus #5: $1.12 and 2,900 tasks came from a $19 median while the mix averages $12. Now $0.70 a task, 97% of its fee, **about 4,660 tasks** to carry the fixed base.

**An 85% count ratio presented as time.** opus #6: it now says the poster reads 3 of 20, the count falls 85%, and the reading-time saving is unmeasured until weeks 5–6 against the ≥40% target.

**"$19 median" vs "assumption".** gpt #4: the fee table now says **base case**, and every other mention defers to section 13's stopwatch.

**One welfare metric, several resolution criteria.** gpt #5: narrower measures (contribution margin, failure rate, time-to-acceptance) are now explicitly constraints; every policy market resolves against net protocol revenue over its stated window.

**The threshold could never be met at opening.** gpt #6: one timestamp — the day the decision is scheduled, after 72 hours of trading. A market opened the morning of its own decision never binds.

## Fixed partially, and labelled as such

**Mandatory and fallback full audits.** gpt #3: the model still carries only the 10% sample. What changed is the policy, not the incidence: a task that needs a full audit — above $1,000, or the thin-market fallback — pays that audit at cost, so the plan no longer implies the sample is the only audit cost. The monthly count of such tasks is not forecast, and the plan says so rather than implying the cost is zero.

## Not changed

- The blended take stays in the table as a second row with the fee-only path beside it. Removing it would hide the assumption rather than expose it, and the page now quotes both break-evens.
- The 6% price, again, for the reasons in sections 06 and 12.
