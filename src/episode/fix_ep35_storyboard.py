# -*- coding: utf-8 -*-
"""Check and fix all 'at' anchors in specs/storyboard.json for Tap 35."""
import json
import re
from pathlib import Path

P = Path("projects/tap-35-ca-voi-sat-thu")
ep = json.loads((P / "episode.json").read_text(encoding="utf-8"))
sb = json.loads((P / "specs/storyboard.json").read_text(encoding="utf-8"))

# Flatten scene texts (subtitles format with display_fix applied)
def clean_text(t):
    return re.sub(r"\[[^\]]+\]", "", t).strip()

scene_texts = {}
for sc in ep["longform"]["scenes"]:
    full_sc = " ".join(clean_text(p["text"] if isinstance(p, dict) else p) for p in sc["parts"])
    # apply display_fix
    for k, v in ep.get("display_fix", {}).items():
        full_sc = full_sc.replace(k, v)
    scene_texts[sc["id"]] = full_sc

shorts_text = clean_text(ep["shorts"]["text"])
for k, v in ep.get("display_fix", {}).items():
    shorts_text = shorts_text.replace(k, v)

print("--- Checking Long Beats ---")
missing_long = []
for i, b in enumerate(sb["long"]):
    sc_id = b["scene"]
    at = b["at"]
    if at in (0, "0", ""):
        continue
    sc_txt = scene_texts.get(sc_id, "")
    if at not in sc_txt:
        missing_long.append((i, sc_id, at))

print(f"Missing long anchors: {len(missing_long)}")
for idx, sc, at in missing_long:
    print(f"  Beat {idx} ({sc}): '{at}'")

print("--- Checking Shorts Beats ---")
missing_shorts = []
for i, b in enumerate(sb["shorts"]):
    at = b["at"]
    if at in (0, "0", ""):
        continue
    if at not in shorts_text:
        missing_shorts.append((i, at))

print(f"Missing shorts anchors: {len(missing_shorts)}")
for idx, at in missing_shorts:
    print(f"  Shorts {idx}: '{at}'")

