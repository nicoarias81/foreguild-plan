### (1) Contradictions and arithmetic that does not follow

1. **The plan needs roughly $56.7k, not the advertised $26.7k—and the prize does not fund the stated first tranche.**  
   **Quote:** “Seed target: ~$26.7k” and “the revenue curve carries it to month 5.”  
   **Against:** “the second tranche of about $30k closes by the end of month 5”; month 5 net is “−$3,056,” and profit begins only in month 11. Also, the “roughly $9.9k” prize supposedly “funds the contracts and the seed liquidity,” but those cost $6,500 + $4,000 = $10,500.  
   **What is wrong:** Total required funding is about $56.7k. Without the additional $30k arriving before month-5 expenses, cash goes negative during month 5. “Burn crosses zero” is false; only the cash balance crosses zero.  
   **Minimal fix:** State a $56.7k total financing requirement, identify a committed source for the second tranche, and require it before month 5. Reduce contracts plus liquidity to no more than the actual prize.

2. **The audit-cost assumption contradicts itself; the adverse version destroys fee-only economics.**  
   **Quote:** “$12–$32 per audit (~$19 avg)” and “$19 is one human audit at 20 minutes × $57/hour.”  
   **Against:** “Auditor … ~40 minutes of human review” for “$19,” and a reference to “Section 06’s $15–$60 band,” which Section 06 does not contain.  
   **What is wrong:** Forty minutes at $57/hour costs $38, not $19. At a 10% sample, expected audit cost becomes $3.80 per task; contribution at a $61 ticket becomes $3.66 − $3.80 − $0.35 = **−$0.49**, so settlement fees never cover fixed costs.  
   **Minimal fix:** Run timed audits, choose one duration and wage, then recompute every unit-economics, runway and break-even table.

3. **The 1% triage fee is simultaneously booked gross and omitted from revenue.**  
   **Quote:** “Foreguild books it as revenue and as an identical cost.”  
   **Against:** “6.0% settlement + 1.4% from the other three lines = 7.4%,” producing month-12 revenue of $10,834.  
   **What is wrong:** If the 1% is revenue, gross take is 8.4%, or $12,298 on $146,400 GMV, with a $1,464 corresponding expense. If it is a pass-through under net presentation, it is neither revenue nor cost. The current treatment makes reported revenue and the futarchy metric undefined.  
   **Minimal fix:** Use net presentation and exclude the triage pool from both revenue and expense, or restate all revenue tables at 8.4% gross.

4. **The lanes and the model use incompatible prices and audit policies.**  
   **Quote:** “Contract … $1 and up … 6.0%” and “nothing in the twelve-month table moves, because the contract rail carries all of it.”  
   **Against:** “The audited lane starts at $40: 6% fee”; “The small-task lane covers $5–$40: 4% fee”; and the metered rail covers “$0.001–$1.00.”  
   **What is wrong:** The contract rail overlaps the metered rail at $1, conflicts with the separate 4% small-task lane, and leaves the treatment of $1–$5 unclear. More importantly, the model applies average audit economics without publishing the task mix across no-audit, 10%-audit and 100%-audit bands. An average ticket cannot recover these nonlinear costs.  
   **Minimal fix:** Define non-overlapping bands and publish monthly task count, GMV, fee and audit cost for each lane separately.

5. **The governance market has incompatible resolution windows.**  
   **Quote:** “The metric is NPR₉₀—net protocol revenue over the 90 days following a decision.”  
   **Against:** The fee decision optimises “30-day trailing protocol revenue,” and “Fee markets resolve 30 days after the change goes live.”  
   **What is wrong:** A 90-day outcome cannot resolve after 30 days. “Only changes whose worst case moves less than 5% … go to a market. Everything else goes to a market” also imposes no actual boundary.  
   **Minimal fix:** Use one 90-day prospective window and resolve only after it closes; send decisions above the 5% exposure limit to the multisig rather than another nominal market.

### (2) Claims stated as measured that are not

6. **Anecdotes and identities are presented as measurements of supply and review efficiency.**  
   **Quote:** “Supply arrives free—the poidh observation of two quality claims in 40 minutes is the proof”; “review cost drops by 85%”; and “Markets are better than people at aggregating dispersed judgment.”  
   **What is wrong:** One $2 bounty does not measure acquisition cost, repeat supply or quality. Reading 3 rather than 20 submissions reduces the poster’s item count by 85%; it does not reduce total review cost if traders must inspect the submissions first. No measured recall, reviewer time, manipulation rate or cost per correct ranking is supplied.  
   **Minimal fix:** Label these as hypotheses until a controlled pilot reports total human minutes, trader payouts, recall@3/5, failure rate and repeat participation.

### (3) Single weakest load-bearing assumption

7. **The entire product assumes a $0.61 market can perform the expensive review that the poster refuses to perform.**  
   **Quote:** “Survivors go to a market”; “the whole 1% pool”; and “the market only decides what they read first.”  
   **What is wrong:** On the base $61 task, all traders collectively receive $0.61 while needing enough attention to rank up to 20 submissions. They predict the poster’s preference, not objective correctness, and can trade without doing substantive review or manipulate a thin market. If this does not produce reliable top-three recall, Foreguild is merely outsourcing review to underpaid speculators, and every revenue, retention and audit assumption collapses.  
   **Minimal fix:** Do not fund the marketplace until a 20-task blinded pilot shows a predeclared recall@3 and total-review-cost advantage over one paid reviewer.

### (4) What to delete

8. **Delete the competitor census and “last 48 hours” sections.**  
   **Quote:** “Written after reading all 22 entries already on the board” versus “Fifty entries are on the board” and “reading every claim … all fifty.”  
   **What is wrong:** It is internally stale, consumes substantial space, depends on regex classifications that do not validate the business, and contributes nothing to demand, unit economics or execution.  
   **Minimal fix:** Delete Sections 00 and “What arrived in the last 48 hours”; retain at most one sentence identifying directly adopted mechanics.