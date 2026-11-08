# Response to review_gpt56sol_r4

Each finding, whether it held, and what changed. Commit `a1a9fb8`.

## 1. Ancillary revenue treated as costless — held

The model adds 1.4 points of take from the $25 audit upgrade, data licensing and certification, and carries them as revenue with no direct cost anywhere. The page quoted $5,434 of month-12 contribution and $2,174 of profit without saying that the whole profit line sits on those three lanes.

Fixed by computing the fee-only path in `tools/model.py` and quoting it next to the blended one:

- fee-only: **+$124/month in month 12**, break-even in month 12
- blended: **+$771 in month 11**, $2,174 of profit in month 12
- the $2,050 gap is ancillary margin, and the page now says a $25 upgrade on a $19 audit is $6 of margin, not $25

Both numbers are pinned in `--check`, so the copy cannot drift from the model again.

## 2. Who pays the 6% — held as ambiguity, not as an arithmetic error

The ledger was consistent (a $61 ticket, $57.34 released, $0.36 of inference → $56.98 to the worker), but the fee table said "taken from the poster's escrow at payout" while the pricing note said the fee columns are what the worker pays. Both are true of the mechanism and misleading together.

Fixed in the table: "deducted from the payout: the poster's price is the ticket and the worker nets 94% of it, so the fee is stated once and borne once."

## 3. The $19 audit presented as measured — partly held

The page gave the assumption's inputs and the $14–$38 band, but defended it with "not a number the team picked", which reads as a measurement.

Fixed: "an assumption about a market wage and a stopwatch, not a measurement: section 13 times the first twenty audits and reprices this line if the stopwatch disagrees."

## 4. The 2%/5% governance contradiction — held, and the second half was worse

The warn box gated futarchy at "under 5% of monthly revenue" while the rule above it routed everything at or above 2% to a market. Fixed to point at the 2% rule and at treasury capacity.

The sharper point stands and cost more than the contradiction: a fee branch hung under an unrelated election parent resolves on nothing, so the traders we wanted would price a question with no bearing on the fee and ignore the branch. The section has been rewritten. The fee market gets its own parent ("what should the audited-lane fee be?") with the fee alternatives as branches, and the attention is bought — treasury liquidity plus the trader subsidy — with the achieved trader count published monthly against the threshold. The measured split (63 parents with median 9 traders, 5 branches with median 5) is what makes that purchase necessary rather than optional.

## 5. Audited share 60% vs 70% — held

The $40–80 band and the $150+ band are both in the audited lane, so 70% of tickets carry an audit at a 10% sample: 0.7 × 0.1 × $19 = $1.33, and the model's $1.90 overstates audit cost by $0.57, not $0.76.

Fixed in the conservatism paragraph.

## 6. Target vs kill-criterion gray zone — held

The predictions gave a target and a looser falsification bar, so clearing the bar but missing the target could be reported as a pass.

Fixed: the column is now "Kill criterion", and the paragraph says missing a target while clearing its kill criterion is reported as a miss.

## Not changed

- The $3,000 / 20-trader binding threshold. It is the measured base rate (2 of 68 markets), and the plan already treats futarchy as advisory until it clears.
- The 6% price. Reviewers keep proposing 4% or 8% on taste; sections 06 and 12 answer with worker net and break-even, which is the only place the difference shows.
