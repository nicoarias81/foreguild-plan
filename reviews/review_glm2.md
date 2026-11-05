# 1. VERDICT

**6/10** — The governance and coverage sections are top-3 quality, but the revision still ships three arithmetic claims that don't survive a calculator, and a Seer judge who runs the numbers (as this plan explicitly invites them to) will dock it for exactly the sin it accuses other plans of.

# 2. FATAL FLAWS

- **Two irreconcilable contribution figures for the same $61 ticket.** The unit economics block says contribution is **$1.41 (38.5%)**. Two paragraphs later: "Month-12 contribution **$2.26/task**". Both use a $61 ticket. The $2.26 only works if you include the non-settlement revenue lines (7.4% × $61 = $4.51 − $1.90 − $0.35 = $2.26); the $1.41 only works if you exclude them. The plan never reconciles this, and it uses **each** figure where it flatters: break-even uses the pessimistic $1.41, month-12 profit uses the optimistic $2.26. You cannot have both.
- **Break-even timing is wrong.** "break-even at roughly 2,300 settled tasks per month, reached in month 10." Month 9 is 1,150 tasks; month 12 is 2,400. Even at the plan's own implied growth rate (~28%/mo), month 10 is ~1,470 and month 11 ~1,880. Break-even at 2,310 tasks lands in **month 12**, not month 10 — and that's using the $1.41 contribution; at $2.26 it's ~1,440 tasks (~month 11). Either way, the headline claim is false.
- **"About 18 months of runway at the month-12 cost base if revenue stalls at month 6" is arithmetically impossible.** At the month-12 cost base ($3,260 fixed + metered costs), $26,700 buys **~8 months at zero revenue**. At month-6 revenue ($1,426/mo) it's ~14.6 months even if you wrongly net full revenue rather than contribution. 18 months appears nowhere in the plan's own numbers.
- **The triage fee is still stated two different ways** — the exact inconsistency the revision claims to have fixed. Assessment table, Layer 2: "**2% of task value (fee)**". Revenue section: "the poster pays **1%** of the ticket into the triage market." The confessional paragraph ("an earlier draft… counted that 1%–2% as margin") draws attention to a discrepancy that is still live in the document.
- **Unverified Seer mechanics presented as citation.** "FutarchyFactory/FutarchyRouter", "two collateral tokens, YES/NO pools", and the claim that the rebrand and Devcon merch "ran as opportunity markets" are stated as fact from "Seer docs". I cannot verify these; if any is wrong, the plan's credibility with the Seer team — the entire judging criterion — takes a direct hit. The naming-contest pilot is verifiable from the brief; the rest is not.
- **The evidence is dated 2026-11-05.** "first-hand observations of poidh bounties on 2026-11-05" — submissions close 12 November. Either the year is a typo (embarrassing in a section whose whole point is "we checked the data") or the observation is from the future. Also: bounty #38/#39 and the honeypot anecdote are checkable claims; if a judge pulls bounty #38 and it doesn't match, the "observable today" framing collapses.

# 3. ARITHMETIC CHECK

**Unit economics block:**
- Settlement fee: 6% × $61 = **$3.66 ✓**
- Amortised audit: "10% × $19" = $1.90 — the **$19 is unexplained**. The assessment table prices audits at "$15–$60 per audit". $19 sits inside that range but nothing derives it, and nothing accounts for the "100% of tasks above $1,000" audit obligation in the per-task line. **Unlabelled number.**
- Gas + sandbox: −$0.35, no derivation. Weak but plausible.
- Contribution: 3.66 − 1.90 − 0.35 = **$1.41 ✓**; $1.41/$3.66 = **38.5% ✓** — but the denominator excludes three of the four revenue lines that the blended take counts. Internally inconsistent scope.

**Revenue-line shares vs blended take:**
- Shares: 81% + 7% + 8% + 4% = 100% ✓
- Blended: 6.0% / 0.81 = 7.407% → other lines = 1.407% ≈ "1.4%" ✓. **This reconciles.** (Note the poster actually pays 6% + 1% triage + audit upgrades ≈ 7%+ of ticket; the 7.4% is protocol revenue, not poster cost — defensible but never stated.)

**12-month table:**
- M3: 120 × $38 = $4,560 ✓; 6.0% → $273.60 ≈ $274 ✓
- M6: 480 × $45 = $21,600 ✓; 6.6% → $1,425.60 ≈ $1,426 ✓
- M9: 1,150 × $54 = $62,100 ✓; 7.1% → $4,409.10 ≈ $4,409 ✓
- M12: 2,400 × $61 = $146,400 ✓; 7.4% → $10,833.60 ≈ $10,834 ✓
- Annualised: $10,834 × 12 = $130,008 ≈ "$130k" ✓
- **The table itself is clean. The errors are around it.**

**Break-even vs fixed base:**
- $3,260 / $1.41 = **2,312** ≈ "~2,310" ✓ as a division — but see Fatal Flaws: the month-10 claim is false, and using $2.26 gives 1,442, so the plan quotes two break-evens implicitly and never says which governs.
- Month-12 profit: 2,400 × $2.26 = $5,424 ✓; $5,424 − $3,260 = $2,164 ✓ — but built on the contribution figure the unit-economics block contradicts.

**Other numbers:**
- Escrow float: "nine-day holds at ~3.5% APY return about **$12 a month** at month-12 volume." Month-12 GMV is $146,400; average outstanding float ≈ $146,400 × 9/30 ≈ $43,900; at 3.5% APY that is **~$128/month, not $12**. Off by 10×. Conservative direction, still a wrong number in a plan that lectures about honest arithmetic.
- Seed total: 9,000 + 6,500 + 4,000 + 3,200 + 2,000 + 2,000 = **$26,700 ✓**
- "Infra… $3,200 — ninety days of the non-team cost base plus dispute bonds": non-team fixed is