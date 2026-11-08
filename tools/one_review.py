#!/usr/bin/env python3
"""Run one adversarial review of reviews/plan_text.txt and save it with usage.

Kept separate from review.py so a run that takes minutes can go to the
background without holding a terminal: the empty-content failures we hit on
long inputs were budget, not refusal, so max_tokens and the usage block are
printed next to the verdict.
"""
import json
import os
import sys
import urllib.request
from pathlib import Path

BASE = "https://api.qa.saia.ai/v1"
PROMPT = (
    "Hostile numerate judge of a funding plan. Report at most 6 blocking problems, "
    "ordered by what they cost a reader deciding whether to fund this: contradictions "
    "(quote both sides), arithmetic that does not follow (show the sum that fails), and "
    "claims stated as measured that are not. For each: quote, what is wrong, the minimal "
    "fix. No praise, no summary, no restating the plan. English.\n\nPLAN\n"
)


def main():
    model = sys.argv[1] if len(sys.argv) > 1 else "anthropic/claude-opus-5"
    tag = sys.argv[2] if len(sys.argv) > 2 else "opus5_r4"
    plan = Path("reviews/plan_text.txt").read_text(encoding="utf-8")
    body = {
        "model": model,
        "max_tokens": int(os.environ.get("MAXTOK", "16000")),
        "messages": [{"role": "user", "content": PROMPT + plan}],
    }
    if os.environ.get("EFFORT"):
        body["reasoning_effort"] = os.environ["EFFORT"]
    req = urllib.request.Request(
        BASE + "/chat/completions",
        data=json.dumps(body).encode(),
        headers={"content-type": "application/json",
                 "authorization": "Bearer " + os.environ["HERMES_CUSTOM_CUSTOM_API_KEY"]},
    )
    d = json.load(urllib.request.urlopen(req, timeout=1500))
    choice = d["choices"][0]
    text = choice["message"].get("content") or ""
    usage = {"model": model, "chars": len(text),
             "finish_reason": choice.get("finish_reason"), "usage": d.get("usage")}
    out = Path(f"reviews/review_{tag}.md")
    out.write_text(text, encoding="utf-8")
    Path(f"reviews/review_{tag}.usage.json").write_text(json.dumps(usage, indent=1), encoding="utf-8")
    print(json.dumps(usage))
    print(text[:600])


if __name__ == "__main__":
    main()
