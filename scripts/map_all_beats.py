import json

plan = json.load(open('projects/tap-07-tom-tit/specs/longform_plan.json', encoding='utf-8'))
words = json.load(open('projects/tap-07-tom-tit/audio/long_words_fixed.json', encoding='utf-8'))
norm = lambda s: "".join(c.lower() for c in s if c.isalnum() or c in "°/-_")

def finder(ws):
    nw = [norm(w['w']) for w in ws]
    def T(phrase, after=0.0):
        toks = [norm(x) for x in phrase.split() if norm(x)]
        for i in range(len(ws) - len(toks) + 1):
            if ws[i]['s'] >= after and nw[i:i+len(toks)] == toks:
                return ws[i]['s']
        raise SystemExit(f"NOT FOUND: {phrase!r}")
    return T

for sid, sc in plan['scenes'].items():
    ws = words[sid]
    T = finder(ws)
    dur = ws[-1]['e']
    print(f"\n==================== {sid}: {sc['title']} ({dur:.1f}s) ====================")
    beats = sc['beats']
    for i, b in enumerate(beats):
        st = 0.0 if b['at'] == 0 else T(b['at'])
        nxt = T(beats[i+1]['at']) if i + 1 < len(beats) else dur
        
        # get text spoken in this interval
        spoken = [w['w'] for w in ws if st - 0.1 <= w['s'] < nxt - 0.1]
        text_preview = " ".join(spoken)
        print(f"Beat {i+1:02d} [{st:5.1f}s - {nxt:5.1f}s] ({b['image']})")
        print(f"   Voice: {text_preview[:120]}...")
