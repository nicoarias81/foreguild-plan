#!/usr/bin/env python3
"""Build the round-n review prompt: brief + competition + prior rounds + plan text."""
import json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

INTRO = """You are a harsh, experienced reviewer on a judging panel for a paid contest run by the team behind Seer, a futarchy/prediction-market protocol.

Below are four documents:
(A) the official contest brief;
(B) the submitted operating plan (HTML stripped to text);
(C) the competing entries already on the board (title + opening of each claim body), so you can judge whether this plan is distinguishable rather than one more restatement;
(D) the previous reviews of earlier versions of this plan, so you do not repeat what was already fixed - report what is STILL wrong.

Judge ONLY this submission against the contest brief. The winner is chosen by the Seer team's own judgement, and every submission becomes an outcome in a Seer market - so credibility with that audience is what matters.

This is round {rnd} of revision. Be equally harsh: report what is still wrong, and whether the revenue model is internally consistent and fundable. Do not praise for having been fixed.

Report, in this exact structure and in English:
1. VERDICT - score 1-10 (one decimal is fine), and one sentence on whether it would place top-3 among the entries in document C.
2. FATAL FLAWS - things that would disqualify or embarrass it (factual errors about futarchy/Seer mechanics, promises the treasury cannot fund, arithmetic that does not add up, unsupported claims presented as data, claims that contradict document C where document C is right). Quote the plan.
3. ARITHMETIC CHECK - recompute independently and show your sums: the unit-economics block (per-task revenue, costs, contribution, contribution as % of fee), the revenue-line shares against the blended take, the 12-month revenue table, and the stated break-even against the fixed cost base both ways (fee-only and blended). State every number that is wrong, unlabelled or internally inconsistent, and say explicitly whether any error is fatal or cosmetic.
4. BRIEF COVERAGE - where tasks come from, how agents are assigned work, how completed work is assessed, how spending/disputes/human intervention are handled, revenue, and how futarchy directs the agents' actions. Mark each MISSING / WEAK / SOLID with one line of why.
5. WHAT IS ACTUALLY GOOD - max 5 bullets, only defensible ones.
6. FIVE CONCRETE FIXES - specific and ordered by expected impact on the judge's decision. Each fix must be either a number that does not close (give the correct number) or a claim to delete/qualify. No generic advice.

Also state at the end, on one line: FATAL_ARITHMETIC: yes|no and FATAL_CONSISTENCY: yes|no.

Be concrete, quote the plan where you criticise it, and do not pad. Never invent facts about Seer; if you are unsure whether something is accurate, say "unverified" instead of asserting.
"""

def clip(s, n):
    s = s.strip()
    return s if len(s) <= n else s[:n].rsplit(" ", 1)[0] + " [...trimmed]"

def competition(limit):
    b = json.load(open(ROOT.parent / "b1531_live.json", encoding="utf-8"))
    rows = []
    for c in b["claims"]:
        if c["issuerAddress"].lower() == "0xf5f9d435cf5d8c334340fa2b40b792d7136b9d90":
            continue
        rows.append("[claim %s / %s] %s\n%s" % (c["claimId"], c["issuerAddress"][:10], c["title"], clip(c["description"], 520)))
        if len(rows) >= limit:
            break
    head = ("%d claims are on this bounty; the %d most recent independent ones are quoted here, newest first. "
            "The submitter's own earlier claim is excluded.\n" % (len(b["claims"]), limit))
    return head + "\n\n".join(rows)

def prior(rnd):
    if rnd <= 1:
        files = ["review_gpt56sol_r5.md", "review_opus5_r5.md"]
    else:
        prev = rnd - 1
        files = ["review_glm_r%d.md" % prev, "review_grok_r%d.md" % prev, "review_sol_r%d.md" % prev]
    out = []
    for f in files:
        p = HERE / f
        if p.exists():
            out.append("--- %s ---\n%s" % (f, clip(p.read_text(encoding="utf-8"), 7000)))
    return "\n\n".join(out) if out else "(no prior reviews)"

def main():
    rnd = int(sys.argv[1]); out = Path(sys.argv[2])
    plan = (ROOT / "plan_live.txt").read_text(encoding="utf-8")
    brief = (ROOT / "bounty_raw.txt").read_text(encoding="utf-8")
    txt = (INTRO.replace("{rnd}", str(rnd))
           + "\n=== DOCUMENT A: CONTEST BRIEF ===\n" + brief.strip()
           + "\n\n=== DOCUMENT C: COMPETING ENTRIES ON THE BOARD ===\n" + competition(10)
           + "\n\n=== DOCUMENT D: PREVIOUS REVIEWS OF THIS SUBMISSION ===\n" + prior(rnd)
           + "\n\n=== DOCUMENT B: THE SUBMISSION (HTML stripped to text) ===\n" + plan.strip() + "\n")
    out.write_text(txt, encoding="utf-8")
    print("round %d: %d chars -> %s" % (rnd, len(txt), out))

if __name__ == "__main__":
    main()
