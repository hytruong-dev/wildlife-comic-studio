# -*- coding: utf-8 -*-
"""Validate that all sticker anchors are strictly inside their beat ranges."""
import json
import sys
from pathlib import Path

sys.path.insert(0, "src/episode")
from pipeline import script_tokens, norm, ptext
from build_plans import find

P = Path("projects/tap-35-ca-voi-sat-thu")
ep = json.loads((P / "episode.json").read_text("utf-8"))
sb = json.loads((P / "specs/storyboard.json").read_text("utf-8"))

for sc in ep["longform"]["scenes"]:
    sid = sc["id"]
    toks = [t for p in sc["parts"] for t in script_tokens(ptext(p), ep.get("display_fix", {}))]
    beats = [b for b in sb["long"] if b["scene"] == sid]
    idx = [find(toks, b["at"], 0 if i == 0 else find(toks, beats[i-1]["at"])) for i, b in enumerate(beats)]
    idx.append(len(toks))
    print(f"\n=== {sid} ===")
    for i, b in enumerate(beats):
        lo, hi = idx[i], idx[i+1]
        for s in b.get("stickers", []):
            try:
                s_pos = find(toks, s["at"], lo)
                if s_pos >= hi:
                    print(f"  !! Beat {i:02d} ({b['at']}): sticker {s['at']!r} at {s_pos} >= next beat {hi}")
                else:
                    print(f"  OK Beat {i:02d} ({b['at']}): sticker {s['at']!r} at {s_pos} (range {lo}..{hi})")
            except Exception as e:
                print(f"  ERROR Beat {i:02d} ({b['at']}): sticker {s['at']!r} NOT FOUND in range {lo}..{len(toks)}: {e}")

