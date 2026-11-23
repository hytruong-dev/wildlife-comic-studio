import json, sys
from pathlib import Path
W = json.loads((Path(__file__).resolve().parents[1] / "audio" / "long_words.json").read_text(encoding="utf-8"))
for sid, ws in W.items():
    if len(sys.argv) > 1 and sid not in sys.argv[1:]:
        continue
    print(f"=== {sid}")
    cur, t0 = [], None
    for w in ws:
        if t0 is None:
            t0 = w["s"]
        cur.append(w["w"])
        if w["w"].endswith((".", "?", "!", ",")) and len(cur) >= 6 or w is ws[-1]:
            print(f"  {t0:6.2f}-{w['e']:6.2f}  {' '.join(cur)}")
            cur, t0 = [], None
