import json
from pathlib import Path

P = Path("projects/tap-07-tom-tit")
plan = json.load(open(P / "specs" / "longform_plan.json", encoding="utf-8"))
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

errors = []
for sid, sc in plan['scenes'].items():
    ws = words[sid]
    T = finder(ws)
    D = ws[-1]['e']
    print(f"\n--- {sid} ({D:.1f}s, {len(sc['beats'])} beats) ---")
    st_list = []
    for b in sc['beats']:
        st = 0.0 if b['at'] == 0 else max(0.0, round(T(b['at']) - 0.30, 2))
        st_list.append(st)
        
        # Check image existence
        img_p = P / b['image']
        if not img_p.exists():
            errors.append(f"Image not found: {b['image']}")
            
        # Check stickers
        for s in b.get('stickers', []):
            try:
                st_time = T(s['at'], st - 0.5)
            except Exception as e:
                errors.append(f"Sticker phrase not found: {s['at']} in {sid}")
            if "target" not in s:
                errors.append(f"Missing target on sticker {s['value']} in {sid}")
                
    for i in range(len(sc['beats'])):
        nxt = st_list[i+1] if i + 1 < len(sc['beats']) else D
        hold = nxt - st_list[i]
        b = sc['beats'][i]
        warn = ""
        if hold > 15.0:
            warn = f"!! ERROR: hold {hold:.1f}s > 15s"
            errors.append(f"{sid} b{i+1}: hold {hold:.1f}s > 15s")
        elif hold < 2.0:
            warn = f"!! ERROR: hold {hold:.1f}s < 2s"
            errors.append(f"{sid} b{i+1}: hold {hold:.1f}s < 2s")
        
        # Check consecutive duplicate
        if i > 0 and b['image'] == sc['beats'][i-1]['image']:
            warn += " !! CONSECUTIVE DUPLICATE !!"
            errors.append(f"{sid} b{i+1}: consecutive duplicate image {b['image']}")
            
        print(f"  b{i+1:02d}: st={st_list[i]:5.2f}s, hold={hold:5.2f}s -> {b['image']} {warn}")

if errors:
    print("\nFAILED with errors:")
    for e in errors:
        print("  -", e)
else:
    print("\n>>> MASTER PLAN VERIFICATION: 100% PERFECT! ALL PASSED! <<<")
