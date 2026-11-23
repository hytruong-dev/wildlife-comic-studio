# -*- coding: utf-8 -*-
"""Check chronological order of anchors in storyboard for Tap 35."""
import json
import re
from pathlib import Path

P = Path("projects/tap-35-ca-voi-sat-thu")
ep = json.loads((P / "episode.json").read_text(encoding="utf-8"))
sb = json.loads((P / "specs/storyboard.json").read_text(encoding="utf-8"))

def clean_text(t):
    return re.sub(r"\[[^\]]+\]", "", t).strip()

scene_texts = {}
for sc in ep["longform"]["scenes"]:
    full_sc = " ".join(clean_text(p["text"] if isinstance(p, dict) else p) for p in sc["parts"])
    for k, v in ep.get("display_fix", {}).items():
        full_sc = full_sc.replace(k, v)
    scene_texts[sc["id"]] = full_sc

shorts_text = clean_text(ep["shorts"]["text"])
for k, v in ep.get("display_fix", {}).items():
    shorts_text = shorts_text.replace(k, v)

for sc_id in [f"scene{i:02d}" for i in range(1, 7)]:
    print(f"\n=== {sc_id} ===")
    sc_txt = scene_texts[sc_id]
    beats = [b for b in sb["long"] if b["scene"] == sc_id]
    last_pos = -1
    for i, b in enumerate(beats):
        at = b["at"]
        if at in (0, "0", ""):
            pos = 0
        else:
            pos = sc_txt.find(at)
        status = "OK" if pos >= last_pos else f"ERROR: inverted! ({pos} < {last_pos})"
        print(f"  Beat {i:02d} [pos {pos:4d}]: '{at}' -> {status}")
        last_pos = max(last_pos, pos)

print("\n=== Shorts ===")
last_pos = -1
for i, b in enumerate(sb["shorts"]):
    at = b["at"]
    if at in (0, "0", ""):
        pos = 0
    else:
        pos = shorts_text.find(at)
    status = "OK" if pos >= last_pos else f"ERROR: inverted! ({pos} < {last_pos})"
    print(f"  Shorts {i:02d} [pos {pos:4d}]: '{at}' -> {status}")
    last_pos = max(last_pos, pos)

