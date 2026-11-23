import json

longform = json.load(open('projects/tap-07-tom-tit/specs/longform_plan.json', encoding='utf-8'))
words = json.load(open('projects/tap-07-tom-tit/audio/long_words_fixed.json', encoding='utf-8'))
norm = lambda s: "".join(c.lower() for c in s if c.isalnum() or c in "°/-_")

def finder(ws):
    nw = [norm(w['w']) for w in ws]
    def T(phrase, after=0.0):
        toks = [norm(x) for x in phrase.split() if norm(x)]
        for i in range(len(ws) - len(toks) + 1):
            if ws[i]['s'] >= after and nw[i:i+len(toks)] == toks:
                return ws[i]['s']
        raise SystemExit(f"NOT FOUND: {phrase!r} (after {after:.1f})")
    return T

for sid, sc in longform['scenes'].items():
    ws = words[sid]
    T = finder(ws)
    print(f"Checking {sid}...")
    for b in sc['beats']:
        st = 0.0 if b['at'] == 0 else T(b['at'])
        for s in b.get('stickers', []):
            try:
                st_t = T(s['at'], st - 0.5)
            except SystemExit as e:
                print(f"  ERR sticker in {b['at']}: {e}")
        for imp in b.get('impacts', []):
            try:
                imp_t = T(imp, st - 0.5)
            except SystemExit as e:
                print(f"  ERR impact in {b['at']}: {e}")

print("Done checking longform plan phrases!")
