import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
d = json.loads((Path(__file__).parents[1] / "audio" / "long_words.json").read_text(encoding="utf-8"))
for k, ws in d.items():
    print("=====", k, len(ws), "end", ws[-1]["e"])
    line, t0 = [], None
    for w in ws:
        if t0 is None:
            t0 = w["s"]
        line.append(w["w"])
        if w["w"].strip()[-1:] in ".?!":
            print(f"{t0:6.1f}-{w['e']:6.1f}  {' '.join(line)}")
            line, t0 = [], None
    if line:
        print(f"{t0:6.1f}-  {' '.join(line)}")
