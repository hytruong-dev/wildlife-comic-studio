import json, sys
sys.path.insert(0, 'src/episode')
from pipeline import script_tokens, norm, ptext
from build_plans import find

with open('projects/tap-03-ca-heo/episode.json', 'r', encoding='utf-8') as f:
    ep = json.load(f)

toks = []
for p in ep['longform']['scenes'][2]['parts']:
    toks.extend(script_tokens(ptext(p), ep['display_fix']))

lo = find(toks, "Kỳ diệu hơn nữa là", 0)
hi = find(toks, "Không chỉ có não bộ", lo)
print(f"lo: {lo}, hi: {hi}, total: {len(toks)}")
print("toks[lo:hi]:", toks[lo:hi])
print("find 'suốt 8':", find(toks, "suốt 8", lo))
