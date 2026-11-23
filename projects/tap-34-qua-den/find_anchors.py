import json

with open("projects/tap-34-qua-den/audio/long_words_fixed.json", "r", encoding="utf-8") as f:
    lw = json.load(f)

def show_range(sc, s_min, s_max):
    print(f"=== {sc} [{s_min}-{s_max}] ===")
    res = []
    for w in lw[sc]:
        if s_min <= w["s"] <= s_max:
            res.append(f"{w['s']:.1f}s:{w['w']}")
    print(" ".join(res))

show_range("scene01", 78, 95)
show_range("scene01", 95, 114)
show_range("scene02", 0, 16)
show_range("scene02", 91, 108)
show_range("scene03", 14, 30)
show_range("scene04", 0, 17)
show_range("scene05", 40, 75)

with open("projects/tap-34-qua-den/audio/shorts_words.json", "r", encoding="utf-8") as f:
    sw = json.load(f)
print("=== shorts [25-45] ===")
print(" ".join(f"{w['s']:.1f}s:{w['w']}" for w in sw if 25 <= w["s"] <= 45))

