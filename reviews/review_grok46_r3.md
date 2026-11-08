1. «$19 is one human audit at 20 minutes × $57/hour» / «$19 for 40 minutes, ≈$28/hr» / «$12–$32 per audit (~$19 avg)» vs «Section 06's $15–$60 band … 15 to 40 minutes»

Three incompatible reviewer economics, all used to pin the same $1.90 amortised cost. Forty minutes at the $57 rate is $38, not $19; 10% sample then costs $3.80 against a $3.66 fee and contribution is −$0.49/task — the row they already labelled «never». Every break-even (1,445 / 2,312), the $37.50 floor, month-12 profit (~$2,164), and the 6%-vs-8% table sit on $19. Pick one duration and one wage, recompute $19, and only then rerun tools/model.py; if the honest number is ~$38, the 6% audited lane is insolvent.

2. «$14,200 of operating cash … the revenue curve carries it to month 5» / «month 5's burn crosses zero» vs cash table month 5 net −$3,056, P&L «positive in month 11», and «second tranche of about $30k closes by the end of month 5 or not at all»

The $26.7k seed (prize as first tranche) does not fund the 12-month plan. Their own ledger is insolvent in month 5 without an uncommitted ~$30k raise gated on 35% repeat. «Burn crosses zero» in month 5 is false; burn is still ~$3k. State required capital as ~$57k, or cut fixed cost / scope to the prize-only 8-week path and stop quoting month-12 $10,834.

3. Contract rail «$1 and up … 6.0%, no floor» vs «small-task lane covers $5–$40: 4% fee, no human audit» vs metered «$0.001–$1.00 … 1.5%» vs «calls under $1 settle in batches of 500» vs «settles when it crosses $0.50, roughly ten calls» vs «Stake … floor $1» after «The floor is the bug»

At least three lanes, two batch rules, and a $1 bond floor that re-imposes the tax they exist to attack ($1 on a $0.05 call is 2,000%). $1–$5 is unspecified. One schedule, one settlement rule, and delete the bond floor or the no-floor thesis.

4. Weakest load-bearing assumption: «the model only clears at a $37.50 average ticket» plus Layer-1 tests, while evidence is «a $2 pot collected two substantive … claims inside 40 minutes» and Wave 1 is «calibrated against observed poidh bounties ($2–$1,208)».

If tickets stay in the observed $2–$25 band, their own table is −$0.75 to −$2.12/task and «volume makes it worse». If work is not script-testable, cost jumps from ~$0.001 to thin markets plus $19 humans. Failure of either assumption takes GMV, 7.4% blend, futarchy-on-revenue, and data-licensing with it. For it to hold, most settled volume must be objectively testable *and* ≥$40 *and* repeating — the opposite of the live market they cite. Put mix weights on the page and a kill if month-3 average ticket is still ~$42 (contribution ~$0.27/task; 2,400 tasks still lose money).

5. «$61 is month-12 GMV divided by month-12 tasks: $146,400 ÷ 2,400. It falls out of the wave mix» — wave shares never appear; nor do drivers for 120 / 480 / 1,150 / 2,400.

Presented as a derived fact. Without weights, $61, $10,834, and 1,445 BE are inputs with footnotes. Publish the mix (tasks and GMV by wave and rail) in the document, not only in an unseen script.

6. NPR₉₀: «Fee changes resolve 90 days after the change goes live» vs «30-day trailing protocol revenue» vs «Fee markets resolve 30 days after the change goes live» vs «A market that resolves before the metric window closes measures noise».

The governance object is undefined; 30-day resolution of a 90-day metric is the failure mode they named. One window, one resolve date, rewrite the fee-market row.

7. Same $61 task: worker inference «$0.36» (token table at $3/$15 per M) vs ledger «~$0.90» vs «Anthropic's … $0.58 — with retries, call it $0.90». Worker «$57.34 … 92.5%» is 94.0% of $61; 92.5% is $57.34 minus $0.90. Indexer «$0.25» is inside the $0.35 unit cost «at month-9 volume (1,150 tasks)» *and* inside the $260 fixed base they say is «not double-counted» (260/1,150 = $0.226, and 2,400 × $0.25 = $600 against a $260 bill).

The worker-margin argument and the $1.41 contribution both move. One inference number; put indexer in fixed *or* variable.

8. Delete outright §00 («Fifty entries are on the board…») through «What arrived in the last 48 hours…» and the regex bake-off.

It does not specify a fee, a lane, a hire, or a kill; it spends the opening on other contestants. A funder reading for an operating plan is already behind the first contradiction.
I am preparing to judge the operating plan as a hostile, numerate evaluator.

I am now auditing the plan for contradictions, unsupported claims, and the weakest load-bearing assumption. I will compile the findings into at most eight items ordered by cost to a funding decision, each with a short quote, the flaw, and the minimal fix. I am starting with the opening claim.

The opening financial claim checks out. The $146,400 twelve-month target at 7.4% blended take equals roughly $10,834 monthly revenue. Fixed costs of $3,260 align with the break-even math. The 1,450-task and 2,310-task figures are consistent with the $2.26 and $1.41 per-task contribution margins.

The opening claim and the cash table disagree by about ten dollars. The opening text says month twelve contribution is $5,424 and profit is roughly $2,164. The cash table lists contribution as $5,434 and profit as $2,174. The $10 gap is a simple arithmetic error.

The unit economics check confirms the $1.41 fee-only and $2.26 blended contribution margins. The $19 audit cost is exactly 20 minutes at $57 per hour. The blended margin assumes audit upgrades, data licensing, and certification add no variable cost, treating them as pure margin.

The plan contradicts itself on auditor rates. It claims one audit costs $19 for 20 minutes at $57 per hour. The same audit is listed as $19 for 40 minutes. The $12–$32 band implies 12.6 to 33.7 minutes at that rate. The $28 per hour figure is inconsistent with both.

The $0.25 indexer-and-RPC allocation per task at month-nine volume of 1,150 tasks totals $287.50. That exceeds the $260 monthly indexer-and-RPC bill. The plan also lists this allocation as part of the per-task contribution line while simultaneously charging the full $260 as a fixed cost. This double-counts the indexer and RPC expenses.

The plan claims gas and sandbox compute are already in the contribution line and therefore not double-counted. That is wrong. The $0.25 indexer allocation is added to the per-task cost while the full $260 indexer bill remains in fixed costs. At month twelve this produces $860 in indexer expenses against a $260 budget.

The $0.25 indexer allocation is a rounded figure. It should not be added to the per-task cost while the full $260 indexer bill remains in fixed costs. The two must be mutually exclusive. That overlap artificially raises the break-even threshold.

The worker ledger shows the poster pays $61.61 for a $61 ticket plus a 1% triage fee.

The worker ledger contains a simple arithmetic error. The worker takes $57.34 from escrow and pays a $1.22 refundable bond, so the net should be $56.12. The plan instead claims a net of $56.44. The $0.32 gap is the model provider inference cost, which is being incorrectly subtracted from the worker's net.

The worker ledger claims the worker keeps 92.5% of the ticket. That is 56.44 out of 61. The earlier "Why 6%" table claims 93.4% (56.04 out of 60). The 92.5% figure subtracts inference from the 93.4% figure. The plan never defines what "worker keeps" means. The 93.4% figure subtracts inference from the 94.0% escrow release.

The worker cost table lists inference at $0.36 per task. The ledger later claims roughly $0.90. That is a 2.5x contradiction. The $0.36 figure is correct for a standard 60k-in/12k-out task under the stated token pricing. The ledger's $0.90 is unsupported.

The plan cites Anthropic's own worked example as the source of the $0.90 inference figure. That example prices a 50k-input, 15k-output session at $0.58, or roughly $0.90 with retries. The $0.36 figure is correct for a standard 60k/12k task under the stated token rates. The heavy-agentic, small-task, and agent-to-agent cost calculations all check out.

The metered fee rail is off by a tenth of a cent: the table uses 0.00075, the text uses 0.0008. The buyer balance settlement claim checks out. The $0.0002 fee example is a hypothetical, not a contradiction.

The metered rail is capped at $1 by construction, yet the table lists $0.001–$1.00 and the text says calls under $1 settle in batches of 500. That batch size is $25, not $0.50. The plan also describes three fee lanes: small-task at 4% with no audit, metered at 1.5%, and contract at 6%.

The plan defines three fee lanes: metered at 1.5% with deterministic testing, small-task at 4% with no human audit, and audited/contract at 6% with a 10% human sample. The contract rail is described as starting at $1 and at $37.50, while the small-task lane covers $5–$40. This leaves a $1–$5 gap between the two lanes that the plan never fills.

The floor table contains an arithmetic error. At a $38 ticket the contribution line shows +$0.03, but the math is 2.28 minus 1.90 minus 0.35, which equals zero. The $0.35 gas cost is missing from the "Audit" column, so the table subtracts it twice. The $37.50 floor is correct because 2.25 minus 1.90 minus 0.35 equals exactly zero. The $61 task line is also wrong: 3.66 minus 1.90 minus 0.35 equals 1.41, not the listed 1.76.

The table omits the $0.35 gas cost from the Audit column, so the contribution line implicitly includes it. The $37.50 floor is still correct because the gas cost is subtracted twice.

Audit sample sensitivity checks out. A 5% sample costs $0.95 in audits, raising break-even to 1,381 tasks. A 10% sample costs $1.41, raising it to 2,312 tasks. A 15% sample costs $2.85, raising it to 7,087 tasks.

The small-task lane assumes a $15 average ticket. A 4% fee on that ticket is $0.60, minus $0.02 gas, equals the listed $0.58 contribution. The plan never explains why the lane targets $15 instead of the $22.50 arithmetic midpoint of $5–$40. The twelve-month model begins with 120 tasks in month three.

The twelve-month task volume and fee math checks out. Month three is 120 tasks at 6.0% for $302.40. Month six is 480 tasks at 6.6% for $1,425.60. Month nine is 1,150 tasks at 7.1% for $4,409.10. Month twelve is 2,400 tasks at 7.4% for $10,833.60. Annual run-rate revenue is $130,008. The $12,500 day-one commitments and $14,200 operating cash are correct. The $14,200 operating budget minus the $12,500 commitments leaves $1,700 in seed capital. The $3,260 monthly break-even covers the $1,

The twelve-month cash curve checks out. Month one closes at $10,944. Month two is skipped. Month three closes at $4,472. Month four closes at $1,312. Month five receives a $30,000 tranche and closes at $28,256. Month six closes at $25,342. Month nine closes at $19,278.

The month-nine to month-twelve cash curve is internally consistent. The three-month gap between month six and month nine shows a net loss of $6,064, which matches the $2,021 monthly average. Month twelve closes at $21,792, and the three-month average of $838 is plausible if month eleven is slightly positive.

The month-twelve contribution line is off by ten dollars. The plan lists $5,434, but the correct figure is $5,424. The profit line is also off by ten dollars, showing $2,174 instead of $2,164.

The plan claims break-even in month eleven, yet linear interpolation of the task curve suggests the threshold is crossed in month ten. The task volume grows from 120 to 480 to 1,150 to 2,400 across months three through twelve. If the same growth rate continues, month ten would reach roughly 1,470 tasks and month eleven roughly 1,880 tasks. That would place the 1,445-task break-even point in month ten.

Geometric interpolation confirms break-even in month eleven. Month ten would still lose roughly $2,780. Month eleven would contribute about $4,023. The plan claims month five's burn crosses zero. The cash table shows month five net loss of $3,056. This is false. The second tranche prevents cash from hitting zero. It does not make burn cross zero. The plan also contradicts itself by saying the seed does not reach break-even on its own while claiming month eleven P&L turns positive.

The plan treats the $0.35 gas cost as a steady-state unit-economics figure for month twelve, but that cost was derived from month-nine volume of 1,150 tasks. The seed table also claims the revenue curve carries cash to month five, which contradicts the stated month-eleven break-even.

The plan overstates variable cost by applying the month-nine allocation rate to month-twelve volume. At 2,400 tasks the cost is $0.108 per task, not $0.25.

The 1% triage fee is excluded from the 7.4% blended settlement rate. Revenue is 7.4% of ticket-only GMV.

The full-audit upgrade is a flat $25 plus 7% of month-twelve revenue, or roughly $758.

The upgrade math checks out. Thirty upgrades per month from 2,400 tasks is 1.25 percent. The evaluation data line is 4.5 percent opt-in. Certification is 8.7 monthly. The fee breakdown sums to 100 percent. The settlement fee is $8,776.

The desk contract is 10% of the settled prize. Six points are the settlement fee already in the table. Four points cover desk gas and audit at cost. That extra slice is capped at 15% of month-six revenue, or $214.

The desk contract wording is ambiguous. It is unclear whether the 15 percent cap applies to the full 10 percent desk slice or only the extra 4 percent beyond the 6 percent settlement fee already in the table.

The worker bond is a 2 percent default on task value with a $1 floor. On a $0.05 call that floor is 2,000 percent of the ticket. The plan criticizes other bounties for $0.25 floors while using a far higher one.

The plan contradicts its own "floor is the bug" thesis by requiring a $1 floor on the metered rail. On a $2 task the $1 bond is 50 percent of the work, which undermines the claim that 2 percent is not excessive. The $1.30 worker break-even is inconsistent with the $0.90 base plus a $1 floor. Dispute bonds are 20 percent of task value with a $5 minimum, so a $40 task carries an $8 bond while a $2 task carries a $5 bond. The escalation threshold is never specified.

The plan lists a 1% Layer 2 cost as a pass-through to traders, yet it also claims Foreguild books that same amount as revenue and identical cost. This is a direct contradiction.

The human-audit rules are also inconsistent. They say 10% of market-ranked winners in the audited lane are randomly selected, and 100% of tasks above $1,000 are audited. Yet the plan also states that every task above $1,000 is audited in full and that the poster buys that audit as part of the $25 upgrade. It never clarifies whether the $1,000 threshold triggers mandatory protocol auditing or merely a poster-purchased upgrade.

The audit rules are now fully resolved. Tasks above $40 are audited at random by the protocol. Tasks above $250 may be fully audited by the poster for $25. The $1,000 threshold is not mandatory. The plan never models the cost of auditing tasks that do not buy the upgrade.

The plan never specifies the wave mix percentages. It asserts an average ticket of $61 without stating how many tasks fall into each price band. That is a load-bearing hole.

If even two percent of tasks are above $1,000, the protocol would face roughly forty-eight extra full audits. At $19 each, that adds about $821 in cost. That would wipe most of the month-twelve profit.

The wave mix is now reconstructed. Wave one runs $40–400, wave two $300–3,000, wave three $50–500, wave four $2,000–20,000, and wave five $5–80. To hit an average ticket of $61, the plan must assume the cheap end of every wave. Month three’s $42 average sits at the bottom of wave one, and month twelve’s $61 sits near the bottom of wave one again. The twelve-month table therefore assumes the low end of every wave, which is implausible.

The low ticket average is a deliberate planning choice, not a contradiction. The plan calibrates ticket sizes against poidh bounties, yet it rejects poidh’s $2–$1,208 range because that segment cannot support auditing. The first three demand waves are crypto bounties priced at $40–$400, $300–$3,000, and $50–$500. Those are the unprofitable segment. The core contradiction is that the board must cold-start from Seer backlog and poidh bounties, which are mostly $2 tasks, while unit economics require a $61 average ticket.

The plan claims DAO grants in wave two are reachable with a direct message and a week, but those are multi-month grants committees, not quick bounties. It asserts a $61 agent task equals roughly $150 of human work, then claims the same deliverable costs 59 percent less. That arithmetic is correct, yet the comparison is unsupported. The plan also cites two quality claims on a $2 poidh bounty as proof that supply is free, but that observation cannot scale to 2,400 tasks per month.

The 85 percent review cost drop is arithmetic, but it assumes a twenty-task sample is typical. The claim that markets aggregate judgment better than people is presented as fact, yet it is debatable at a median liquidity of $1.13. Seer depth measurements are cited as script-derived data, but they cannot be verified as true or fabricated.

The plan header claims twenty-two entries are already on the board, but the body states fifty entries are present. That contradiction is not a contradiction of arithmetic or logic, yet it is a direct factual error.

The plan states that sixty entries landed after the previous revision, which is inconsistent with the header claiming twenty-two entries were already on the board. The body’s count of fifty entries is treated as a correction to that earlier figure.

The plan contradicts itself on fee-market resolution timing. It states that fee changes resolve ninety days after going live, yet the futarchy metric is ninety days and the table shows a thirty-day trailing revenue cadence. That is a direct contradiction.

The futarchy gate is self-defeating. The plan says only changes whose worst-case impact is under five percent of monthly revenue stay small. Everything else goes to a market. That means every change goes to a market. The gate is therefore empty.

The plan contradicts itself on the market veto. It says the team holds a 2-of-3 veto, yet it also says the veto is deleted when the threshold trips. The binding threshold requires $3,000 liquidity and 20 distinct traders. One conditional market already cleared the liquidity half with $7,598.

The plan cites a Seer board measured on 8 November 2026, which may be a future or simulated date. The ninety-day forecast targets 120 tasks per month, matching month three of the twelve-month model, which yields $302 in revenue and leaves seed cash at $4,472 by month three. The kill condition demands no external task be posted by day fourteen, a very tight deadline. The prize of roughly $9,900 covers about 37 percent of the $26,700 seed.

The plan treats the prize as a deliberately smaller eight-week proof-of-concept. It would skip external audits, leave founders unpaid, and fund only $1,500 in market liquidity for twenty tasks. The ledger entry for a $61.61 task is internally inconsistent. The worker receives $57.34 while the triage, auditor, and Foreguild fees are drawn from a $3.66 pool. The auditor’s expected $1.90 is paid by the protocol from that same pool, not by the poster. The poster’s $61.61 deposit therefore cannot cover the worker’s $57.34 salary.

The plan’s “every dollar traced” ledger is arithmetic broken. The worker’s $0.90 model-provider fee is paid from the $57.34 salary, not from the $61.61 deposit. Adding all “takes out” rows yields $62.16, not $61.61. The plan also misstates the fee split: it claims the protocol keeps 39 percent and the human audit and settlement cost 61 percent, yet the actual breakdown is roughly 38.5 percent to the protocol and 61.5 percent to audit and gas.

The plan claims a desk holding $500 and capturing 10% of flow would earn roughly $146 per month, or 29% annualized. That is 2,277% APR. The mechanism is unsupported because the pool is a prediction market, not a market-maker spread.

The plan’s $1.41 per-task fee and $2.26 blended take are inconsistent with the earlier 1,450 and 2,310 task targets. The auditor’s $19 charge is also internally contradictory: it is described as a 20-minute audit at $57 per hour, yet the same $19 is also described as a 40-minute audit at roughly $28 per hour. That is a direct numerical contradiction.

The plan assumes two part-time team members at $1,500 per month, or $3,000 per month total, for the full year. That is a capacity assumption for running a 2,400-task-per-month marketplace with futarchy, Kleros, DAO sales, and model labs.

The plan is circular: it proposes using Foreguild itself to bounty the work that builds the board.

A 35 percent repeat-poster rate gates the $30,000 tranche at month five. The business model does not project tasks for month five, so the seed of $26,700 plus the prize is exhausted by month five. Without the tranche, the company dies before month eleven, when profitability is projected.

The plan asks sponsors to fund a business that requires a second $30,000 raise by month five. That follow-on is not committed in the seed target, so the $26,700 budget is insufficient to reach month eleven. The plan is asking for funding to support a business that cannot survive without an unpledged second tranche.

The float calculation is correct. Nine-day holds at 3.5 percent annualized on month-12 gross monthly volume yield roughly $128 per month. The metered rail’s 0.05 percent base multiplied by 1.5 percent equals 0.00075, which rounds to 0.0008. The plan claims this rail is upside that does not count toward revenue, but the twelve-month table shows no movement because the contract rail carries all of it.

The plan warns that metered volume could outpace contract volume and lower blended take, yet it also claims never to blend the rails and that metered volume is excluded from the twelve-month model. The small-task lane at $5–40 with a 4% rate is absent from the twelve-month model. If a fraction of tasks fall into that lane, the average ticket and take rate would drop, making the $61 target harder to reach.

The plan lists three fee rates: 6% on the contract rail, 4% on the small-task lane, and 1.5% on the metered rail. The twelve-month model uses only the 6% contract rate. If the small-task lane exists in year one, the 6% rate overstates settlement fees. The plan also contradicts itself on task pricing. It claims the contract rail starts at $1 and up, yet it later says the audited lane starts at $40 and the small-task lane is $5–$40. That leaves a gap between $1 and $40 where the 6% rate is applied without any audit.

The plan contradicts itself on governance timing. It requires a ninety-day metric window, yet it says fee markets resolve thirty days after a change goes live. That thirty-day resolution is exactly the noise failure mode the plan warns against.

The plan also presents first-hand poidh observations as measured facts. It claims honeypot forms, stale acceptingClaims listings, and two claims in forty minutes. Those are unsupported claims masquerading as verified data.

The plan cites fifty entries with forty futarchy names and zero worker inference prices, yet it offers no repository to verify that regex count. It claims Seer board statistics as measured facts without source. The $57-per-hour auditor rate is unattributed. It cites a 3.5 percent annualized yield on escrow. It quotes Anthropic’s $0.58 worked example as fact. It asserts markets aggregate dispersed judgment better than humans and that supply arrives free. It compares human freelancers to $150 and cites a median entry of 1,010 characters. None of these are substantiated.

The plan claims the longest entry is 3,308 characters and the shortest is 20, yet it offers no repository to verify those field statistics. It also asserts the contest brief requires this submission to become an outcome in a Seer market, but the brief itself is not included for verification.

The plan assumes posters will pay $40–$61 per task, yet the comparable poidh market clears at $2. The plan’s own cold-start relies on Seer bounties and poidh-like tasks. Alternatively, it assumes a prediction market with median $1.13 liquidity can triage submissions well enough that posters only read k=3 and still accept the work, achieving an 85 percent review reduction. Neither assumption is supported.

The plan assumes deterministic acceptance tests cover most demand, yet the core work is subjective Layer 2. It also warns that if the first twenty tasks show tests cover under thirty percent of demand, triage stops being a bonus and becomes the whole product. The “sell the receipt, not the review” model requires cheap Layer 1 verification, accurate markets, or cheap human audit.

Human audit is unworkable below the $37.50 floor. The plan assumes enough objectively-testable, publicly-verifiable tasks priced at $40 or above will reach 1,445 settled tasks per month. Without that volume, the lanes collapse into unprofitable small bounties or un-auditable subjective work. The two-part-time team is also stretched too thin to source 2,400 tasks while running operations, disputes, DAO sales, and evaluation-data sales.

The plan’s own poidh evidence contradicts both volume and ticket-price assumptions. If tickets stay at $2–25, unit economics go negative and volume makes it worse. Both are required.

The plan demands a large volume of crypto-native or DAO tasks that are objectively testable, clear at $40 or above, and repeat at 35 percent or higher.

Delete outright: the 50-entry field survey, the “what arrived in the last 48 hours” section, the six dated predictions, and the “how to check this page” instruction.

The plan also wastes space comparing other platforms’ eight-percent floors and listing party-by-party reasons for staying. The vocabulary-saturation argument and the escrow float discussion are unnecessary. The worker probability log score never appears in the economics. The mandates system is a second product. The judge will keep the final critique to eight items ordered by funding-decision cost.

Auditor cost is internally inconsistent. The plan lists $57 per hour for twenty minutes, $28 per hour for forty minutes, and a $12–$32 range. It also cites $15–$60. These figures are required to justify the $19 verification cost and the $37.50 floor.

Inference pricing is contradictory. The same task is priced at $0.36 and $0.90. Worker scores are 92.5% and 93.4%. The auditor rate is $57.34.

The indexer cost is double-counted. It appears as $0.35 and $260 fixed.

The judge is now structuring the final critique as eight items, each with a quote, a diagnosis, and a minimal fix, ordered by funding-decision cost. The first item is the arithmetic contradiction: the plan claims a $26,700 seed is sufficient, yet its own twelve-month burn model shows the runway crosses zero in month five and only turns positive in month eleven.

The $19 audit cost is internally inconsistent. If the audit takes forty minutes at $57 per hour, the amortized cost becomes $3.80. That exceeds the $3.66 fee, making the contribution negative and the break-even assumption impossible. This is the largest number bug because it inverts solvency. The judge has now ordered the final critique into eight items, with this arithmetic contradiction at the top.

The $19 audit cost is internally inconsistent. The plan claims it is a forty-minute $57-per-hour review, yet it also calls it a twenty-minute $28-per-hour audit. If the review truly takes forty minutes, the rate is $28 per hour, not $57. That $28 figure is too low for a security auditor. The $1.90 amortized audit cost is the single number that determines the $37.50 floor and the 2,312 break-even point.

The $15–$60 reviewer band in Section 06 is inconsistent with its own $12–$32 range. At $57 per hour, the $12–$32 band maps to 12.6–33.7 minutes, while the $15–$60 band would require 16–63 minutes or a different rate.

Worker net math is also wrong. The plan lists a $57.34 worker fee minus a $1.22 bond, yet the net is calculated as $56.44, implying the bond is $0.90. That is a $0.32 arithmetic error.

The judge found further arithmetic drift. The $61.61 take-out figure does not close. Month 12 contribution is listed as 5,424 and 5,434. Break-even targets are 1,450, 1,445, and 1,445. The 2,310 and 2,312 figures are also inconsistent. The intro and body cite different numbers. The 81 percent revenue-to-contribution ratio could be misread. The bond floor is $1 versus no floor. The plan cites two substantive claims in 40 minutes as proof supply is free. It also cites stale acceptingClaims listings on bounties #38 and #39.

The judge also treats Seer’s 3,051 markets claim as unverifiable because the repository JSON is missing. The plan presents the poidh observation of two quality claims in forty minutes as proof that supply arrives free, yet this is an unsupported generalization masquerading as evidence. It also asserts that markets are better than people without citation, and cites a comparable human task at roughly three hours for $150 or more.

The $61 average and the $146,400 annual target are derived from a wave mix that is never defined in the document. The script that computes them is absent, so the judge cannot verify the numbers. The task-count drivers for 120, 480, 1,150, and 2,400 are also unstated. These figures are presented as model outputs rather than explicit assumptions.

The 7.4 percent blended fee is arithmetically consistent. The three line items total 19 percent of revenue, and 19 percent of 7.4 percent equals 7.4 percent of GMV. The judge also verified the upgrade math: at $25 each, 758 revenue from upgrades implies roughly 30 upgrades. Data and certificate fees sum to 2,058.

Thirty full-audit upgrades are plausible. A skewed mix of 2,370 tasks at $50 and 30 at $900 yields an average near $61. The evaluation-data demand wave and the verified-pair revenue line are distinct business models. They can coexist.

Wave 4 is implicitly dependent on waves 1–2 producing volume, yet it is not explicitly included in the month-12 GMV mix. The judge now considers the plan fully evaluated.

The judge has finalized the eight-item critique. The first two items are the audit rate contradiction and the seed-runway arithmetic. The third item is the fee-lane contradiction. The fourth is the weakest assumption: the plan demands testable tasks at $40 or above, yet its only evidence is poidh bounties priced at $2. The fifth is the missing wave mix and the absent model script. The sixth is the futarchy governance mismatch between 30 and 90 days. The seventh is the inference pricing and indexer double-count, or the unsupported supply-is-free claim. The eighth is the deletion of section 00.

The $0.35 indexer double-count is conservative, so it is lower priority. The 92.5% worker log score is inconsistent with the $57.34 fee and $61 average. The $1.41 break-even figure includes a $0.25 indexer cost already in the $3,260 fixed cost, which is a second double-count. The 39% versus 38.5% protocol share, the 1,450 versus 1,445 break-even targets, and the 2% human-intervention override are too minor to include.

The $0.25 indexer double-count is conservative, so it does not inflate the break-even target. The $19 audit cost is held constant by trading hours for wage; the plan uses forty minutes at a lower rate to keep the fee flat, which is a modeling trick rather than a funding lie.

The judge is now writing the critique in English, with no praise and no summary of the plan. The judge is also verifying the opening cash flow: starting with $14,200 in operating funds, month one shows $72 in revenue, $4 in contribution, and a $3,256 net loss, leaving $10,944 at month end. The judge is checking whether the $4 contribution on $72 revenue is internally consistent, since that implies a variable cost of roughly $2.34 per task, which is higher than the $3.66 fee.

The judge now sees that month one’s $4 contribution is impossible under any realistic assumption. At 28.6 tasks, the expected contribution is roughly $40, not $4. Even a 100 percent audit rate would yield a massive negative contribution, not a small positive. The $72 revenue implies only about 28 tasks, so the $4 figure is mathematically inconsistent with the stated unit economics.

The month-one $4 contribution is internally consistent. Auditing roughly 10 percent of 29 tasks at $19 each, plus gas, yields about $5.20 in contribution, which is close to the stated $4. The plan used actual lower ticket prices rather than the $61 average. Month three’s $32 contribution is also correct: at $42 per task, the net is $0.27 per task, so 120 tasks yield $32. The break-even point is therefore roughly 12,074 tasks, not the 2,310 figure.

The plan only breaks even because the average ticket rises from $42 to $61. If the ticket stayed at $42, the 2,400-task volume would yield roughly $648 in contribution, far below the $3,260 fixed cost. Month 12 must therefore rely on the higher $61 ticket, which means the wave mix must shift up. That shift is unstated. At $42, the 120-task month-three contribution is only possible because exactly 10 percent of 120 tasks are audited.

The plan claims the growth curve crosses both break-even points between months 11 and 12. Month 11 likely only clears the lower 1,445 target. The higher 2,310 target is only reached at month 12. The judge considers this a minor quibble. The eight-item critique is finalized. The judge is now writing the harsh, quote-driven evaluation.

The judge is now ordering the eight items by funding risk. The $19 audit cost is ranked first because it inverts solvency. The seed-runway assumption is second because the $26,700 starting cash would be exhausted by month five without the uncommitted $30,000. The fee-lane contradiction is third because the stated rails, fees, and floors are incompatible. The weakest assumption is fourth. The judge is now drafting the remaining items.