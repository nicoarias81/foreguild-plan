#!/usr/bin/env python3
"""Extract choices[0].message.content from a response json into markdown."""
import json, sys
from pathlib import Path
resp = Path(sys.argv[1]); out = Path(sys.argv[2])
d = json.loads(resp.read_text(encoding="utf-8"))
ch = d["choices"][0]
msg = ch.get("message") or {}
text = (msg.get("content") or "") + (("\n\n[reasoning]\n" + msg["reasoning_content"]) if msg.get("reasoning_content") else "")
out.write_text(text.strip() + "\n", encoding="utf-8")
u = d.get("usage") or {}
print("%s -> %s  chars=%d finish=%s tokens=%s" % (resp.name, out.name, len(text), ch.get("finish_reason"), u.get("total_tokens")))
