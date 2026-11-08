#!/usr/bin/env python3
"""Send the plan text to N reviewers in parallel and save their verdicts.

    python3 tools/review.py reviews/plan_text.txt r3

Each reviewer gets the same instruction and no sight of the others, so the
disagreements between them are the useful part. Reads the key from
$HERMES_CUSTOM_CUSTOM_API_KEY and the gateway from $SAIA_BASE (default
https://api.qa.saia.ai/v1).
"""
import concurrent.futures as cf
import json
import os
import sys
import urllib.request
from pathlib import Path

BASE = os.environ.get("SAIA_BASE", "https://api.qa.saia.ai/v1")
KEY = os.environ.get("HERMES_CUSTOM_CUSTOM_API_KEY") or os.environ.get("CUSTOM_API_KEY")
MODELS = [
    ("grok46", "xai/grok-4.6"),
    ("gpt56sol", "openai/gpt-5.6-sol"),
    ("opus5", "anthropic/claude-opus-5"),
]

PROMPT = """You are a judge for a paid bounty: Seer is commissioning an operating plan for \
"Foreguild", an AI job board whose workers are agents, whose reviewers are markets, and whose \
parameters are governed by futarchy. The prize is about $10,000 and the winning entry is the one \
the sponsors would actually fund.

Read the plan below as a hostile, numerate judge. You have no obligation to be encouraging.

Your job, in this order:
1. Contradictions and arithmetic. Anywhere two sections disagree, or a number does not follow from \
the numbers around it. Quote both sides.
2. Unsupported claims presented as measured fact.
3. The single weakest load-bearing assumption — the one whose failure takes the most of the plan \
down with it — and what would have to be true for it to hold.
4. What you would delete outright: sections that cost words and buy nothing.

Rules: at most 8 items, ordered by how much they would cost the plan in a funding decision. Each \
item: a short quote from the text, what is wrong, and the minimal fix. No praise, no summary of \
what the plan says, no restating the brief. If something is merely stylistic, skip it — style is \
not a funding blocker. Answer in English.

PLAN
====
"""


def call(model, plan, tries=3):
    body = {"model": model, "max_tokens": 4000,
            "messages": [{"role": "user", "content": PROMPT + plan}]}
    for attempt in range(tries):
        try:
            req = urllib.request.Request(
                BASE + "/chat/completions", data=json.dumps(body).encode(),
                headers={"content-type": "application/json",
                         "authorization": f"Bearer {KEY}"})
            data = json.load(urllib.request.urlopen(req, timeout=600))
            msg = data["choices"][0]["message"]
            text = (msg.get("content") or "") + "\n" + (msg.get("reasoning_content") or "")
            if text.strip():
                return text.strip()
            raise RuntimeError("empty content")
        except Exception as exc:  # noqa: BLE001
            if attempt == tries - 1:
                return f"ERROR {model}: {exc!r}"[:500]
    return "ERROR"


def main():
    src = Path(sys.argv[1])
    tag = sys.argv[2] if len(sys.argv) > 2 else "r1"
    plan = src.read_text(encoding="utf-8")
    outdir = src.parent
    print(f"plan {len(plan)} chars -> {len(MODELS)} reviewers")
    with cf.ThreadPoolExecutor(max_workers=3) as pool:
        futures = {pool.submit(call, mdl, plan): name for name, mdl in MODELS}
        for fut in cf.as_completed(futures):
            name = futures[fut]
            text = fut.result()
            path = outdir / f"review_{name}_{tag}.md"
            path.write_text(text, encoding="utf-8")
            print(f"{name:10} {len(text):6} chars -> {path.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
