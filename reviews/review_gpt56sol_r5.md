1. **The seed runs out before the stated tranche date if the reserve is actually untouchable.**  
   - **Quotes:** “Reserve | $2,000 | Untouched”; “The operating balance is $14,200, which bottoms at $1,312 at the end of month 4”; “the second tranche of about $30k closes by the end of month 5.”  
   - **What is wrong:** The $14,200 operating balance includes the $2,000 reserve:  
     \[
     \$26,700-\$12,500=\$14,200.
     \]  
     At the stated month-4 balance, unrestricted cash is therefore:  
     \[
     \$1,312-\$2,000=-\$688.
     \]  
     The plan breaches its reserve before month 5, so the tranche cannot wait until the stated date.  
   - **Minimal fix:** Treat opening spendable cash as $12,200 and require the tranche before cash falls below $2,000—no later than month 4—or stop calling the reserve untouched.

2. **The advertised month-11 break-even relies entirely on ancillary revenue that the plan admits is not costed.**  
   - **Quotes:** “break-even at roughly 1,450 settled tasks per month at that blend … crossed in month 11”; versus “the honest profit figure is the fee-only one — +$124 in month 12, break-even in month 12 rather than month 11”; and “the three smaller lines are carried at gross revenue with no direct cost modelled.”  
   - **What is wrong:** Fee-only month-12 arithmetic is:  
     \[
     6\%\times \$146,400=\$8,784
     \]  
     \[
     \$8,784-2,400\times(\$1.90+\$0.35)-\$3,260=\$124.
     \]  
     The advertised blended result is:  
     \[
     \$10,834-\$5,400-\$3,260=\$2,174.
     \]  
     The $2,050 difference is unmodelled ancillary margin, not demonstrated profitability.  
   - **Minimal fix:** Use fee-only break-even and cash flow as the funding case, or add bottom-up volumes, adoption rates and direct costs for audits, licensing and certification.

3. **Mandatory and fallback full audits are absent from the audit-cost model.**  
   - **Quotes:** “100% of tasks above $1,000”; “fallback to full human review when liquidity is below threshold”; versus “Amortised audit (10% sample × $19 avg) −$1.90” and “the unit economics charge a human audit to every task ($1.90).”  
   - **What is wrong:** The model reserves only 10% of one audit per task. Each task requiring a full audit costs an additional:  
     \[
     \$19-\$1.90=\$17.10
     \]  
     relative to the model. No count of $1,000-plus tasks or thin-market fallbacks is included, despite tickets being assumed as high as $3,000. A $40 task sent to fallback review earns $2.40 before compute but incurs about $19 of audit cost.  
   - **Minimal fix:** Forecast both mandatory and fallback full-audit incidence by month and include their incremental cost; otherwise queue or reject thin-market tasks unless the buyer prepays the full audit.

4. **The load-bearing “$19 median” is explicitly not measured.**  
   - **Quotes:** “$14–$38 per audit, $19 median”; versus “It is an assumption about a market wage and a stopwatch, not a measurement: section 13 times the first twenty audits.”  
   - **What is wrong:** $19 is merely \(20/60\times \$57\), a selected planning point. It is not a median until audits have actually been timed. This assumed number determines the $37.50 ticket floor, contribution per task and break-even volume.  
   - **Minimal fix:** Label it “base-case assumed audit cost,” provide sensitivity at the stated 15–40 minute range, and gate the operating model or tranche on the measured first-20-audit median.

5. **Governance promises one welfare metric but assigns several incompatible ones.**  
   - **Quotes:** “Governance needs one number to optimise”; “Foreguild’s is net protocol revenue”; versus the market table using “Contribution margin per category,” “Post-audit failure rate at constant cost,” “Median time-to-acceptance, spam rejection rate,” and “Revenue per verified pair, worker retention.”  
   - **What is wrong:** Those are different objectives, including multi-variable objectives without a stated aggregation or resolution rule. A market cannot produce the claimed single welfare comparison when each decision is resolved against a different or undefined composite metric.  
   - **Minimal fix:** Resolve every policy market against NPR over a specified window, with the other measures expressed as explicit constraints, or abandon the claim that governance optimises one number.

6. **The binding-market threshold is tested at a time when a new market cannot satisfy it.**  
   - **Quotes:** “a decision binds when the market holds ≥$3,000 of liquidity and ≥20 addresses with non-zero volume, counted on the leaderboard when the question opens”; later, “One fee decision resolved by a market holding ≥$3,000 and ≥20 traders.”  
   - **What is wrong:** At opening, a newly created question has no trading history, so it cannot already have 20 addresses with non-zero volume unless an unmentioned pre-opening trading period exists. The later prediction instead tests depth at resolution. These are different rules.  
   - **Minimal fix:** Define one timestamp—immediately before policy selection or market close—and measure liquidity and unique funded traders from on-chain activity at that timestamp.