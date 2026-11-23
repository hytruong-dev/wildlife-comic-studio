import json, re
from pathlib import Path

ep = json.loads(Path("projects/tap-37-lac-da-sa-mac/episode.json").read_text(encoding="utf-8"))
display_fix = ep.get("display_fix", {})

def clean(t):
    t = re.sub(r"\[[a-zA-Z0-9_\-]+\]", " ", t)
    for k, v in sorted(display_fix.items(), key=lambda x: len(x[0]), reverse=True):
        t = t.replace(k, v)
    return " ".join(t.split())

scenes_text = {sc["id"]: clean(" ".join(p["text"] for p in sc["parts"])) for sc in ep["longform"]["scenes"]}
shorts_text = clean(ep["shorts"]["text"])

sb = json.loads(Path("projects/tap-37-lac-da-sa-mac/specs/storyboard.json").read_text(encoding="utf-8"))

print("Checking LONG beats...")
for b in sb["long"]:
    sid = b["scene"]
    stext = scenes_text[sid]
    at = b["at"]
    if at not in (0, "0", ""):
        pos = stext.find(at)
        if pos == -1:
            print(f"  [MISSING LONG ANCHOR] {sid}: {repr(at)}")
        else:
            for s in b.get("stickers", []):
                sat = s["at"]
                spos = stext.find(sat, pos)
                if spos == -1:
                    print(f"  [MISSING LONG STICKER] {sid} after {repr(at)}: {repr(sat)}")

print("Checking SHORTS beats...")
for b in sb["shorts"]:
    at = b["at"]
    if at not in (0, "0", ""):
        pos = shorts_text.find(at)
        if pos == -1:
            print(f"  [MISSING SHORTS ANCHOR] {repr(at)}")
        else:
            for s in b.get("stickers", []):
                sat = s["at"]
                spos = shorts_text.find(sat, pos)
                if spos == -1:
                    print(f"  [MISSING SHORTS STICKER] after {repr(at)}: {repr(sat)}")

