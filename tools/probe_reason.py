import json
import os
import sys
import urllib.request

model = sys.argv[1] if len(sys.argv) > 1 else "anthropic/claude-opus-5"
effort = sys.argv[2] if len(sys.argv) > 2 else "low"
b = {"model": model, "max_tokens": 3000, "reasoning_effort": effort,
     "messages": [{"role": "user", "content": "Reply with exactly: OK"}]}
r = urllib.request.Request("https://api.qa.saia.ai/v1/chat/completions", data=json.dumps(b).encode(),
                           headers={"content-type": "application/json",
                                    "authorization": "Bearer " + os.environ["HERMES_CUSTOM_CUSTOM_API_KEY"]})
d = json.load(urllib.request.urlopen(r, timeout=180))
c = d["choices"][0]
print(json.dumps({"effort": effort, "finish": c.get("finish_reason"),
                  "len": len(c["message"].get("content") or ""),
                  "content": (c["message"].get("content") or "")[:40], "usage": d.get("usage")}))
