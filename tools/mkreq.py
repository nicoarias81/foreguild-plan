#!/usr/bin/env python3
"""Write the request body for one model from a prompt file (no giant argv)."""
import json, sys
from pathlib import Path
prompt = Path(sys.argv[1]).read_text(encoding="utf-8")
out = Path(sys.argv[2]); model = sys.argv[3]
body = {"model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 6000, "temperature": 0.2}
out.write_text(json.dumps(body), encoding="utf-8")
print(out.name, model, len(prompt), "chars")
