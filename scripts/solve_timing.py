import json
from pathlib import Path

P = Path("projects/tap-35-ca-voi-sat-thu")
words = json.loads((P / "audio/long_words_fixed.json").read_text(encoding="utf-8"))

def show(sid, s0, s1):
    print(f"\n=== {sid} [{s0}s - {s1}s] ===")
    ws = [w for w in words[sid] if w and s0 <= w["s"] <= s1]
    text = " ".join(f"{w['s']:.1f}s:{w['w']}" for w in ws)
    print(text)

show("scene02", 55, 96)
show("scene03", 20, 45)
show("scene03", 90, 100)
show("scene04", 0, 20)
show("scene05", 0, 25)
show("scene05", 70, 85)

show("scene03", 40, 56)
show("scene04", 0, 30)
