# -*- coding: utf-8 -*-
import json
import sys

sys.path.insert(0, 'src/episode')
from pipeline import norm, ptext, script_tokens

ep = json.load(open('projects/tap-33-ech-go-bac-cuc/episode.json', encoding='utf-8'))
sb = json.load(open('projects/tap-33-ech-go-bac-cuc/specs/storyboard.json', encoding='utf-8'))
display = ep.get('display_fix', {})

def test_find(toks, phrase, after=0):
    if phrase in (0, '0', ''): return 0
    want = [norm(x) for x in str(phrase).split() if norm(x)]
    n = [norm(t) for t in toks]
    for i in range(after, len(toks) - len(want) + 1):
        if n[i:i + len(want)] == want: return i
    return -1

scenes = {s['id']: s for s in ep['longform']['scenes']}
for sid, s in scenes.items():
    toks = script_tokens(' '.join(ptext(x) for x in s['parts']), display)
    beats = [b for b in sb['long'] if b['scene'] == sid]
    cur = 0
    for idx, b in enumerate(beats):
        pos = test_find(toks, b['at'], cur)
        if pos < 0:
            first_pos = test_find(toks, b['at'], 0)
            print(f'ERROR {sid} beat {idx}: {b["at"]!r} found at {first_pos} but cur={cur}')
        else:
            cur = pos

stoks = script_tokens(ep['shorts']['text'], display)
cur = 0
for idx, b in enumerate(sb['shorts']):
    pos = test_find(stoks, b['at'], cur)
    if pos < 0:
        first_pos = test_find(stoks, b['at'], 0)
        print(f'ERROR shorts beat {idx}: {b["at"]!r} found at {first_pos} but cur={cur}')
    else:
        cur = pos

