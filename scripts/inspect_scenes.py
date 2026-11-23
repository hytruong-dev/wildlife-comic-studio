import json
from pathlib import Path

P = Path("projects/tap-07-tom-tit")
A = P / "audio"
words = json.load(open(A / "long_words_fixed.json", encoding="utf-8"))

for sid in ["scene01", "scene02", "scene03", "scene04", "scene05", "scene06"]:
    d_file = A / f"{sid}_parts_duration.json"
    if d_file.exists():
        d = json.load(open(d_file, encoding="utf-8"))["total_duration"]
    else:
        d = words[sid][-1]["e"]
    ws = words[sid]
    text = " ".join(w["w"] for w in ws)
    print(f"=== {sid} (total: {d:.2f}s, words: {len(ws)}) ===")
    print(text[:150] + "...")
