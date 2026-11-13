1. **VERDICT — 4.1/10.** It would not place top-3 among document C: the verification-led positioning is distinguishable, but the funding arithmetic is materially wrong and the blended-profit case is not sufficiently costed.

2. **FATAL FLAWS**

- **The prize is overstated by almost 2×, breaking the immediate financing ask.** The plan says:  
  > “The prize (0.5 ETH + 4,000 USDC, roughly $9.9k at current prices)”  
  Using the plan’s own ETH price of $2,235:  
  0.5 × $2,235 + $4,000 = **$5,117.50**, not $9,900.  
  Therefore the claimed post-prize cheque is not $16,800; it is **$21,582.50** to reach the $26,700 seed. The statement that the prize covers all but $600 of $10,500 of contracts and liquidity is wrong by **$4,782.50**. This is fatal because it directly misstates what can be funded.

- **The blended break-even is presented as operating economics even though ancillary direct costs are explicitly omitted.** The plan admits:  
  > “the three smaller lines are carried at gross revenue with no direct cost modelled”  
  but then states:  
  > “Contribution at 7.4% blend $2.26/task (50%)”  
  and:  
  > “Month-12 contribution $5,434/mo → profit ~$2,174”  
  Data-licensing revenue sharing, certification delivery, sales/legal work, and incremental full-audit costs are absent. Thus $2.26 is revenue less only the baseline audit/infrastructure allowance, not defensible contribution after all variable costs. The fee-only case is arithmetically coherent; the blended profitability and month-11 break-even are not established.

- **The supposedly complete ledger excludes a paid verification mechanism.** The plan says:  
  > “anyone may submit a failing test … for a share of the ticket (2–5%, capped at $40)”  
  but later claims:  
  > “The ledger closes: $61.61 in … $61.61 out across seven parties”  
  No test-challenger payment appears in that ledger or unit economics. At a $61 ticket, 2–5% is **$1.22–$3.05** whenever paid—enough to consume or exceed the $1.41 fee-only contribution. Funding source and incidence are unspecified. The “every dollar traced” claim is false as written.

- **The market is a ranking signal, not verification, yet the submission repeatedly sells it as review.** It says:  
  > “whose reviewers are markets”  
  and:  
  > “The market decides which submission is best”  
  But the proposed market predicts which submission the poster will accept. That can rank buyer preference; it does not independently prove validity or quality. Because the poster sees the ranking and then determines the outcome, the design also has a reflexive resolution problem. The stronger verification claims must be qualified.

- **The 1% market-payment mechanism is unverified and economically underspecified.** The plan says:  
  > “100% of it is paid out to the participants in that market”  
  and treats it as a costless pass-through. It does not explain how this interacts with Seer’s actual trading, liquidity-provider gains/losses, trader losses, or resolution payouts. Whether Seer supports this exact fixed-pool distribution is **unverified**. A $0.61 pool on the standard task is also not credible compensation for multiple traders reading submissions without measured evidence.

- **Mandatory full-audit pricing contradicts itself.** The plan says tasks above $1,000 receive:  
  > “100%” audit  
  and:  
  > “pays that audit at cost”  
  while the revenue table offers:  
  > “Full-audit upgrade … $25 flat”  
  Audit cost is stated as $14–$38. It is unclear whether >$1,000 tasks pay $25, actual cost, or a separate mandatory charge. This obligation is absent from the model.

- **The governance metric is not actually singular.** The plan says:  
  > “Governance needs one number … Foreguild’s is net protocol revenue”  
  Yet its governance table assigns category contribution margin, failure rate, time-to-acceptance, spam rejection, and worker retention as optimisation metrics. The later explanation calls these constraints, but the table says otherwise and supplies no decision rule for resolving conflicts. That is a serious FAO consistency defect, not merely presentation.

- **Growth is assumed rather than operationally financed.** Tasks rise from 120 in month 3 to 2,400 in month 12 while the plan rejects paid acquisition and budgets only two part-time roles, one of them “growth lead.” Existing measured demand is described as just 140 paying wallets. No quantified integration funnel or poster/task productivity closes the gap. Consequently the revenue curve does not support the financing case; it merely assumes the volume that produces break-even.

3. **ARITHMETIC CHECK**

### Unit economics per $61 task

Settlement revenue:

- 6% × $61 = **$3.66**

Baseline variable costs:

- Audit: 10% × $19 = **$1.90**
- Gas, sandbox and marginal infrastructure = **$0.35**
- Total modelled variable cost = **$2.25**

Fee-only contribution:

- $3.66 − $1.90 − $0.35 = **$1.41**
- Contribution as percentage of settlement fee:  
  $1.41 ÷ $3.66 = **38.52%**

This block is correct, subject to omitted adversarial-test, mandatory-audit and dispute-related costs.

Blended revenue per task:

- 7.4% × $61 = **$4.514**
- Modelled contribution: $4.514 − $2.25 = **$2.264**
- Rounded = **$2.26**
- Contribution as percentage of blended revenue:  
  $2.264 ÷ $4.514 = **50.15%**

The arithmetic is correct, but calling this full “contribution” is misleading because ancillary direct costs are unmodelled. **Consistency error; material, not merely cosmetic.**

### Revenue-line shares against the 7.4% blended take

Settlement fee:

- 6.0 ÷ 7.4 = **81.081%**
- The stated 81% is correct after rounding.

Ancillary lines collectively:

- 1.4 ÷ 7.4 = **18.919%**

The listed shares are 7% + 8% + 4% = **19%**, which is close but not exact.

If those rounded shares are applied to month-12 revenue of $10,833.60:

- Full audits: 7% × $10,833.60 = **$758.35**
- Data licensing: 8% × $10,833.60 = **$866.69**
- Certification: 4% × $10,833.60 = **$433.34**
- Total ancillary = **$2,058.38**

But the actual 1.4-point ancillary total is:

- 1.4% × $146,400 = **$2,049.60**

Difference: **$8.78**, caused by rounded shares. **Cosmetic.**

The implied exact take-rate allocations corresponding to 7%/8%/4% rounded revenue shares are not supplied, nor are volumes for audits, licensed pairs or certifications. That is a modelling omission, not an arithmetic error.

### Twelve-month revenue checkpoints

Month 3:

- 120 × $42 = **$5,040 GMV**
- $5,040 × 6.0% = **$302.40**
- Stated $302: correct after rounding.

Month 6:

- 480 × $45 = **$21,600 GMV**
- $21,600 × 6.6% = **$1,425.60**
- Stated $1,426: correct after rounding.

Month 9:

- 1,150 × $54 = **$62,100 GMV**
- $62,100 × 7.1% = **$4,409.10**
- Stated $4,409: correct after rounding.

Month 12:

- 2,400 × $61 = **$146,400 GMV**
- $146,400 × 7.4% = **$10,833.60**
- Stated $10,834: correct after rounding.

However, the stated month-12 mix yields:

- 60% × $60 = $36.00
- 30% × $12 = $3.60
- 10% × $220 = $22.00
- Weighted average = **$61.60**, not $61.00

At $61.60:

- GMV would be 2,400 × $61.60 = **$147,840**
- Revenue at 7.4% would be **$10,940.16**

Difference from the table:

- GMV: **$1,440**
- Revenue: **$106.56**

This is a small but real driver inconsistency. **Cosmetic individually, embarrassing given the claim that the model checks every figure.**

Also, this is not a complete 12-month revenue table; it supplies only months 3, 6, 9 and 12.

### Break-even against $3,260 fixed cost

Fee-only:

- Contribution per task = **$1.41**
- $3,260 ÷ $1.41 = **2,312.06 tasks**
- Therefore minimum whole-task break-even = **2,313 tasks/month**

The plan variously says “~2,310,” “2,312,” and “2,310 if only the settlement fee counted.” These are acceptable approximations.

At 2,400 month-12 tasks:

- 2,400 × $1.41 = **$3,384**
- $3,384 − $3,260 = **$124 profit**

Correct, before omitted costs.

Blended:

- Exact modelled contribution = **$2.264**
- $3,260 ÷ $2.264 = **1,439.93**
- Minimum whole-task break-even = **1,440 tasks/month**

The later figure of 1,440 is correct. The opening’s “roughly 1,450” is merely coarse rounding.

At 2,400 tasks:

- 2,400 × $2.264 = **$5,433.60**
- $5,433.60 − $3,260 = **$2,173.60**

Rounded stated figures of $5,434 and $2,174 are correct—but only under the unjustified assumption that all ancillary revenue has zero additional direct cost.

### Funding arithmetic

Using the plan’s $2,235 ETH price:

- 0.5 ETH = **$1,117.50**
- Plus 4,000 USDC = **$5,117.50**
- Not **$9,900**

Required external cheque after winning:

- $26,700 − $5,117.50 = **$21,582.50**
- Not **$16,800**

Prize coverage of $10,500 contracts plus launch liquidity:

- $10,500 − $5,117.50 = **$5,382.50 remaining**
- Not **$600**

This is a **fatal arithmetic error** because it changes the launch capital requirement and invalidates the reduced funding narrative.

4. **BRIEF COVERAGE**

- **Where tasks come from — SOLID.** Five demand waves, an initial desk contract and measured existing-wallet demand are specified, although the scale-up to 2,400 monthly tasks is unsupported.
- **How agents are assigned work — WEAK.** Workers “claim” tasks, but “beat the current best by a stated margin” has no defined bid variable, pricing rule or selection mechanism.
- **How completed work is assessed — WEAK.** Deterministic tests and sampled audits are concrete, but acceptance-prediction markets are overstated as verification and adversarial testing is uncosted.
- **Spending, disputes and human intervention — SOLID.** Escalation bonds, Reality.eth/Kleros backstop, reserved human powers and treasury buckets are described; exact Seer-stack compatibility remains unverified.
- **Revenue — WEAK.** The 6% settlement line closes, but 19% of projected month-12 revenue comes from uncosted and unvalidated ancillary products.
- **How futarchy directs agents’ actions — WEAK.** The mandate chain is described, but governance remains advisory, metrics conflict, and the allocation/conditional-market decision rule is insufficiently specified.

5. **WHAT IS ACTUALLY GOOD**

- The fee-only unit economics are transparent and independently recomputable.
- Separating low-value deterministic work from the human-audited lane addresses a real fixed-cost problem.
- The plan does not pretend the contest prize is protocol treasury capital—although it badly misvalues the prize.
- Disputes and human overrides have explicit limits rather than being hand-waved away.
- The task-level ledger correctly reconciles the baseline $61.61 flow before the omitted challenger and ancillary costs.

6. **FIVE CONCRETE FIXES**

1. Replace every “$9.9k prize” figure with **$5,117.50** at the stated $2,235/ETH price; replace the post-prize seed cheque of **$16,800** with **$21,582.50**, and the claimed $600 contracts/liquidity gap with **$5,382.50**.

2. Delete the claims that blended break-even occurs in month 11 and that month-12 profit is $2,174 unless direct costs and volumes are added for all three ancillary lines. The currently defensible result is only the fee case: **$1.41/task, 2,313-task break-even, and $124 month-12 profit before omitted costs**.

3. Delete “the ledger closes” or add the adversarial-test bounty explicitly. At a $61 ticket, the stated 2–5% payment is **$1.22–$3.05 per paid challenge**; specify its incidence and payer before claiming any contribution figure.

4. Qualify “reviewers are markets” and “the market decides which submission is best” to: **the market predicts poster acceptance and ranks the review queue; it does not independently verify correctness**. Delete the fixed 1% participant-payout claim unless that exact Seer mechanic is verified.

5. Reconcile the month-12 driver: either use the stated mix’s **$61.60 average, $147,840 GMV and $10,940.16 revenue**, or change the band assumptions so they actually produce the table’s **$61 average, $146,400 GMV and $10,833.60 revenue**.

FATAL_ARITHMETIC: yes  
FATAL_CONSISTENCY: yes
