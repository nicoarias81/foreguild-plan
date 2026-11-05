# REVIEW: "Foreguild: sell the receipt, not the review" (@ariasnico)

## 1. VERDICT

**6/10** — The strongest market-design thinking I've seen in this format, but the revenue section — the one thing this contest explicitly optimises for — contradicts itself in three places, and a judge who runs a prediction-market protocol will check that math first; borderline top-3, likely beaten by a cleaner submission.

## 2. FATAL FLAWS

- **Headline contradicts the model.** The plan opens with "Target: $182k of GMV in month 12 at a 7.4% blended take, which is roughly $13.5k/month of protocol revenue." The 12-month table says month 12 is **$146,400 GMV and $10,834 revenue**. Both cannot be true. $182k × 7.4% = $13.5k, so the headline is internally consistent with itself but not with the table two sections later. This is the plan's own headline number and it doesn't survive contact with its own appendix.
- **The take-rate story doesn't add up.** Unit economics counts *both* the 6% settlement fee and the 2% market fee as protocol revenue ($3.66 + $1.22 = $4.88/task). But the revenue table's blended take at month 12 is **7.4% — below the 8% those two fees alone produce** — while claiming insurance, float and licensing push the blend *up* from 6%. Either the 2% market fee goes to traders/liquidity (in which case the $2.63 contribution margin and the 1,240-task break-even are wrong), or it's protocol revenue (in which case blended take should be ≥8% and rising). The plan needs both to be true and they can't be.
- **The margin percentage is wrong.** $2.63 on $4.88 of revenue is **53.9%**, not 43%. $2.63 on a $61 ticket is **4.3%**. "43%" matches neither; it looks like someone dropped a decimal and nobody checked.
- **The contest prize is treated as the project's treasury.** "Treasury target: 0.5 ETH + 4,000 USDC" and Section 08: "What the 0.5 ETH + 4,000 USDC actually buys." The prize is a reward to the *author*, not seed capital for Foreguild. Worse, the "deliberately fundable at the prize level alone" reduced budget is "~$9k" — which still exceeds 0.5 ETH + 4,000 USDC at any ETH price below ~$10k (unverified current price, but the claim is unsupported either way).
- **The 90-day operations budget contradicts the fixed cost base.** "$3,200 — First 90 days of operations: Infra, indexer, RPC, Kleros bonds, audits" against a stated fixed cost of **$3,260/month**. Three months of the stated cost base is ~$9,780. Either the team works free for a quarter or one of the two numbers is fiction.
- **Unverified anecdotes presented as data.** The poidh bounty numbers (#38, #39, "$2–$1,208", "two claims in 40 minutes", the honeypot field) and the claim that "Seer already wrote the thesis on its own site" and that "the rebrand, the Devcon merch and the naming of this very job board all ran as opportunity markets" are all plausible but **unverified** — and the observation date "2026-11-05" is either a typo or from the future. For a plan whose entire pitch is "trust the receipt," citing receipts nobody can check is self-undermining.

## 3. ARITHMETIC CHECK

**Unit economics block:**
- 6% × $61 = $3.66 ✓
- 2% × $61 = $1.22 ✓
- $3.66 + $1.22 − $1.90 − $0.35 = $2.63 ✓ (the addition is right)
- **"43%" is wrong**: $2.63 / $4.88 revenue = 53.9%; $2.63 / $61 ticket = 4.3%. No reading yields 43%.
- Structural error: whether the $1.22 market fee is treasury revenue at all is inconsistent with the blended-take column (see above).

**12-month revenue table (row arithmetic all checks out):**
- 120 × $38 = $4,560 ✓; × 6.0% = $273.6 ≈ $274 ✓
- 480 × $45 = $21,600 ✓; × 6.6% = $1,425.6 ≈ $1,426 ✓
- 1,150 × $54 = $62,100 ✓; × 7.1% = $4,409.1 ≈ $4,409 ✓
- 2,400 × $61 = $146,400 ✓; × 7.4% = $10,833.6 ≈ $10,834 ✓
- "$130k run-rate": $10,834 × 12 = $130,008 ✓ — but this confirms the **headline ($182k / $13.5k) is the wrong number**, not the table.
- Revenue-share column: 72 + 11 + 6 + 8 + 3 = 100 ✓, but the float line fails absolutely: 3.5% APY × 9/365 days = **0.086% of escrow**. On $146.4k GMV that's ~$126/month, not the ~$650 (6% of $10,834) claimed. Off by ~5×.

**Break-even:**
- Fixed cost: $3,000 + $260 = $3,260 ✓
- $3,260 / $2.63 = 1,239.5 ≈ 1,240 ✓ — but only under the 8%-of-ticket revenue assumption. At the plan's own month-12 blended take of 7.4% ($4.51/task), contribution is $2.26 and break-even is **~1,443 tasks/month**. At month-3 economics ($38 ticket, 6% take only): contribution $0.03/task — essentially never breaks even. The 1,240 figure is the most flattering possible reading and nothing else in the document supports it.

## 4. BRIEF COVERAGE

- **Where tasks come from — SOLID.** Five ranked waves with ticket sizes, an honest "these are assumptions" flag, and a concrete cold-start pitch; wave 3 (Seer's own backlog) is smart flattery that's also operationally real.
- **How agents are assigned work — SOLID.** Claim-with-bond, claim ceilings after 5 claims, deterministic tests before markets; the mechanism is specific enough to implement.
- **How completed work is assessed — SOLID.** Three-layer table with costs and finality; the "poster reads top-k, market only orders the queue" asymmetry is genuinely well-argued.
- **Spending/disputes/human intervention — SOLID.** Escrow-held-not-team, priced escalation via Reality.eth/Kleros, three enumerated human powers with a 2% override trigger; the "protocol takes nothing from disputes" incentive note is a nice touch.
- **Revenue — WEAK.** Five lines with rates and shares is structurally the best revenue section I'd expect, but the arithmetic contradictions above mean the numbers can't all be true, and the judge is being asked to fund a plan that can't audit itself.
- **How futarchy directs the agents' actions — WEAK.** Section 09 governs *protocol parameters* (fees, categories, bond sizes) — it never explains how a futarchy outcome changes what an *agent does* on a Tuesday. The brief explicitly asks how "governance directs their actions"; the plan answers how governance directs the fee schedule. There is no link from market resolution to agent behaviour, permissions, or task routing.

## 5. WHAT IS ACTUALLY GOOD

- The core reframe — review cost, not agent supply, is the binding constraint, and "revenue per review-minute" as the north-star metric — is a thesis the Seer team is publicly committed to; it speaks their language.
- The refusal to accept untestable tasks ("Foreguild refuses tasks that cannot be tested, and that refusal is a feature") is the single best design decision in the plan and costs nothing.
- The 90-day table has kill criteria per milestone, including honest ones ("Repeat rate below 20% (we are a bounty board, not a job board)") — most submissions have no falsification conditions at all.
- Section 13 pre-commits to three conditions under which the author would rewrite the plan, including abandoning futarchy for a multisig if markets can't hold $500 of liquidity. Naming your own failure modes is credible with this audience.
- The collusion/stale-listing risk table shows the author actually used poidh rather than theorising about it.

## 6. FIVE CONCRETE FIXES

1. **Make the numbers tell one story.** Pick either $146.4k GMV / $10,834 / 1,443 break-even (table-consistent) or $182k / $13.5k and regenerate every downstream figure. Right now the opening bet, the unit economics, and the model are three different plans. This is the first thing a futarchy team checks, and it's currently wrong three ways.
2. **Decide what the 2% triage fee is and fix everything downstream.** If it's protocol revenue, month-12 blended take must be ≥8% and the table's 7.4% is wrong; if it's paid to liquidity providers, delete the $1.22 from contribution margin, recompute break-even (~1,443+ tasks), and recheck whether the business clears $3,260/month at all. One paragraph resolving this fixes the margin %, the break-even, and the float inconsistency's neighbourhood in one move.
3. **Delete the prize-as-treasury framing entirely.** Replace Section 08 with a protocol-treasury budget funded by early revenue plus an explicit optional grant request, and drop "deliberately fundable at the prize level alone" — the reduced ~$9k plan still doesn't fit the prize, so the sentence currently fails on its own arithmetic while also misreading what the prize is.
4. **Add half a page: "From market resolution to agent behaviour."** Map each futarchy decision to the agent-facing artifact it changes (fee market resolves → settlement-fee constant in the escrow contract → agent bid pricing updates; category whitelist resolves → task router allowlist updates). This is the brief's explicit ask and the plan's biggest coverage hole.
5. **Downgrade the poidh anecdotes to labelled evidence or link them.** Change "observable today" to "anecdotally observed on 2025-11-05 (unverified): …" with bounty IDs and links, and fix the year. The observations are the plan's most vivid material; presenting unverifiable screenshots-equivalents as data to the team that *runs* poidh is the fastest way to get caught out — they can check #38 and #39 in thirty seconds.