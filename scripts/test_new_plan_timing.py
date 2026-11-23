import json
from pathlib import Path

P = Path("projects/tap-07-tom-tit")
longform = json.load(open(P / "specs" / "longform_plan.json", encoding="utf-8"))
words = json.load(open(P / "audio" / "long_words_fixed.json", encoding="utf-8"))
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

all_ok = True
for sid, sc in longform['scenes'].items():
    ws = words[sid]
    T = finder(ws)
    D = ws[-1]['e']
    print(f"\n--- {sid} ({D:.1f}s, {len(sc['beats'])} beats) ---")
    st_list = []
    for b in sc['beats']:
        st = 0.0 if b['at'] == 0 else max(0.0, round(T(b['at']) - 0.30, 2))
        st_list.append(st)
    for i in range(len(sc['beats'])):
        nxt = st_list[i+1] if i + 1 < len(sc['beats']) else D
        hold = nxt - st_list[i]
        b = sc['beats'][i]
        warn = ""
        if hold > 15.0:
            warn = f"!! ERROR: hold {hold:.1f}s > 15s"
            all_ok = False
        elif hold < 2.0:
            warn = f"!! ERROR: hold {hold:.1f}s < 2s"
            all_ok = False
        
        # Check duplicate with previous beat
        dup = ""
        if i > 0 and b['image'] == sc['beats'][i-1]['image']:
            dup = "!! CONSECUTIVE DUPLICATE !!"
            all_ok = False
            
        print(f"  b{i+1:02d}: st={st_list[i]:5.2f}s, hold={hold:5.2f}s -> {b['image']} {warn} {dup}")

if all_ok:
    print("\n>>> ALL BEATS PASS THE CONSTRAINTS (NO DUPLICATE, DURATION OK)! <<<")
