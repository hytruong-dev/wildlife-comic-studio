import json
from pathlib import Path

P = Path("projects/tap-07-tom-tit")
words = json.load(open(P / "audio" / "long_words_fixed.json", encoding="utf-8"))

for sid in ["scene05", "scene06"]:
    ws = words[sid]
    print(f"\n=== {sid} ===")
    for i in range(0, len(ws), 10):
        print(f"  {ws[i]['s']:5.2f}s: {ws[i]['w']}")
