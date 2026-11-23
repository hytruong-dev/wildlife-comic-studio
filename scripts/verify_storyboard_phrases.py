import json, re

ep = json.load(open("projects/tap-15-capybara/episode.json", encoding="utf-8"))
sb = json.load(open("projects/tap-15-capybara/specs/storyboard.json", encoding="utf-8"))
display = ep.get("display_fix", {})

def to_sub(t):
    clean = re.sub(r"\[[^\]]+\]", "", t)
    for k in sorted(display, key=len, reverse=True):
        clean = clean.replace(k, display[k])
    return clean

# check long beats
for sc in ep["longform"]["scenes"]:
    sid = sc["id"]
    full_sc = " ".join(to_sub(p["text"] if isinstance(p, dict) else p) for p in sc["parts"])
    s_beats = [b for b in sb["long"] if b["scene"] == sid]
    for b in s_beats:
        at = b["at"]
        if at != 0 and at not in full_sc:
            print(f"[{sid}] 'at' not in text: '{at}'")
        for st in b.get("stickers", []):
            sat = st["at"]
            if sat not in full_sc:
                print(f"[{sid}] sticker 'at' not in text: '{sat}'")
        for imp in b.get("impacts", []):
            if imp not in full_sc:
                print(f"[{sid}] impact not in text: '{imp}'")

# check shorts beats
full_shorts = to_sub(ep["shorts"]["text"])
for b in sb["shorts"]:
    at = b["at"]
    if at != 0 and at not in full_shorts:
        print(f"[shorts] 'at' not in text: '{at}'")
    for st in b.get("stickers", []):
        sat = st["at"]
        if sat not in full_shorts:
            print(f"[shorts] sticker 'at' not in text: '{sat}'")
print("Check completed.")
