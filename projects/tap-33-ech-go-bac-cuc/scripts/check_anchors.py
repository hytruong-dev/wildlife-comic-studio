# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path("src/episode").resolve()))
from pipeline import norm, ptext, script_tokens

ep = json.load(open('projects/tap-33-ech-go-bac-cuc/episode.json', encoding='utf-8'))
sb = json.load(open('projects/tap-33-ech-go-bac-cuc/specs/storyboard.json', encoding='utf-8'))
display = ep.get('display_fix', {})

def test_find(toks, phrase, after=0):
    if phrase in (0, "0", ""):
        return 0
    want = [norm(x) for x in str(phrase).split() if norm(x)]
    n = [norm(t) for t in toks]
    for i in range(after, len(toks) - len(want) + 1):
        if n[i:i + len(want)] == want:
            return i
    return -1

scenes = {s["id"]: s for s in ep["longform"]["scenes"]}
for sid, s in scenes.items():
    toks = script_tokens(" ".join(ptext(x) for x in s["parts"]), display)
    beats = [b for b in sb["long"] if b["scene"] == sid]
    cur = 0
    print(f"=== {sid} ({len(beats)} beats) ===")
    for b in beats:
        idx = test_find(toks, b["at"], cur)
        if idx < 0:
            print(f"  [BEAT FAIL] at={b['at']!r} after {cur}")
        else:
            cur = idx
        for st in b.get("stickers", []):
            sidx = test_find(toks, st["at"], idx)
            if sidx < 0:
                print(f"  [STICKER FAIL] at={st['at']!r}")
        for im in b.get("impacts", []):
            iidx = test_find(toks, im["at"], idx)
            if iidx < 0:
                print(f"  [IMPACT FAIL] at={im['at']!r}")

stoks = script_tokens(ep["shorts"]["text"], display)
cur = 0
print(f"=== SHORTS ({len(sb['shorts'])} beats) ===")
for b in sb["shorts"]:
    idx = test_find(stoks, b["at"], cur)
    if idx < 0:
        print(f"  [SHORTS BEAT FAIL] at={b['at']!r} after {cur}")
    else:
        cur = idx
    for st in b.get("stickers", []):
        sidx = test_find(stoks, st["at"], idx)
        if sidx < 0:
            print(f"  [SHORTS STICKER FAIL] at={st['at']!r}")
    for im in b.get("impacts", []):
        iidx = test_find(stoks, im["at"], idx)
        if iidx < 0:
            print(f"  [SHORTS IMPACT FAIL] at={im['at']!r}")
