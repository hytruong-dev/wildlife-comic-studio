import json, re, difflib

norm = lambda s: "".join(c.lower() for c in s if c.isalnum() or c in "°/-_")

raw = json.load(open('projects/tap-07-tom-tit/audio/long_words_raw.json', encoding='utf-8'))
sc1_wh = raw['scene01']

script = "[surprise-oh] Nếu bạn nghĩ một sinh vật dài chưa đầy hai mươi xăng-ti-mét, khoác lên mình bộ cánh sặc sỡ đủ bảy sắc cầu vồng thì chỉ biết làm cảnh dưới đáy biển, thì bạn vừa phạm phải sai lầm chết người nhất cuộc đời!"

# Test replacing phrases in script before tokenizing
replacements = [
    ("hai mươi xăng-ti-mét", "20cm"),
    ("bảy sắc cầu vồng", "7 sắc cầu vồng"),
    ("A-T-K", "ATK"),
    ("S-P-D", "SPD"),
    ("D-E-F", "DEF"),
    ("U-V", "UV"),
    ("Cáp-vi-tây-sơn", "Cavitation"),
    ("Xô-nô-lu-mi-nét-xen", "Sonoluminescence"),
    ("Bu-li-găng", "Bouligand"),
]

text = script
text = re.sub(r"\[[a-zA-Z0-9_\-]+\]", " ", text)
for src, dst in replacements:
    text = text.replace(src, dst)

tokens = text.split()
print("Tokens:", tokens[:15])

# Let's see how align matches tokens with sc1_wh
def align(script_toks, wh):
    wh = [w for w in wh if norm(w["w"])]
    a, b = [norm(x["w"]) for x in wh], [norm(x) for x in script_toks]
    res = [None] * len(script_toks)
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op == "equal":
            for k in range(j2 - j1):
                res[j1 + k] = {"w": script_toks[j1 + k], "s": wh[i1 + k]["s"], "e": wh[i1 + k]["e"]}
        elif op in ("replace", "insert"):
            if i2 > i1:
                t0, t1 = wh[i1]["s"], wh[i2 - 1]["e"]
            else:
                t0 = wh[i1 - 1]["e"] if i1 > 0 else 0.0
                t1 = wh[i1]["s"] if i1 < len(wh) else t0 + 0.3 * (j2 - j1)
            t1 = max(t1, t0 + 0.12 * (j2 - j1))
            lens = [max(1, len(b[j])) for j in range(j1, j2)]
            tot, acc = sum(lens), 0
            for k, j in enumerate(range(j1, j2)):
                s = t0 + (t1 - t0) * acc / tot
                acc += lens[k]
                res[j] = {"w": script_toks[j], "s": round(s, 3), "e": round(t0 + (t1 - t0) * acc / tot, 3)}
    ratio = difflib.SequenceMatcher(None, a, b, autojunk=False).ratio()
    return res, ratio

res, ratio = align(tokens, sc1_wh[:len(tokens)+10])
print(f"Match ratio: {ratio:.2f}")
for r in res[:12]:
    print(f"  {r['w']:12s} [{r['s']:.2f}s - {r['e']:.2f}s]")
