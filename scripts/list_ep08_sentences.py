import json, re
from pathlib import Path

P = Path('projects/tap-08-chon-gulo')
ep = json.loads((P / 'episode.json').read_text(encoding='utf-8'))
words = json.loads((P / 'audio' / 'long_words_fixed.json').read_text(encoding='utf-8'))

for sc in ep['longform']['scenes']:
    sid = sc['id']
    ws = words[sid]
    sents = []
    curr = []
    for w in ws:
        curr.append(w)
        if any(w['w'].endswith(p) for p in ['.', '!', '?']):
            sents.append(curr)
            curr = []
    if curr:
        sents.append(curr)
    print(f"=== {sid} (total {ws[-1]['e']:.2f}s, {len(sents)} sentences) ===")
    for idx, s in enumerate(sents):
        first4 = ' '.join(w['w'] for w in s[:5])
        print(f"  [{idx+1:02d}] {s[0]['s']:6.2f}s - {s[-1]['e']:6.2f}s ({s[-1]['e'] - s[0]['s']:4.1f}s): {first4} ... {s[-1]['w']}")
