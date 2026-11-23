import json
from pathlib import Path
from src.episode.build_plans import script_tokens, ptext, find

P = Path("projects/tap-44-ca-mat-trang")
sb = json.loads((P / "specs" / "storyboard.json").read_text(encoding="utf-8"))
ep = json.loads((P / "episode.json").read_text(encoding="utf-8"))
display = ep.get("display_fix", {})

# Clear all current stickers from beats first
for b in sb["long"]:
    b["stickers"] = []
for b in sb["shorts"]:
    b["stickers"] = []

# List of desired stickers for longform:
# (scene, trigger_word_in_subtitles, side, y, value, label, target)
long_stickers_def = [
    ("scene01", "10 tấn", "R", 360, "10 TẤN", "cần cẩu công nghiệp", [0.75, 0.5]),
    ("scene01", "2 tấn", "R", 380, "2 TẤN", "thể trọng kỷ lục", [0.72, 0.5]),
    ("scene02", "3.2 km/h", "L", 360, "3.2 KM/H", "vận tốc bơi thực tế", [0.28, 0.5]),
    ("scene02", "7.5 cm", "R", 380, "7.5 CM", "độ dày da đệm", [0.75, 0.5]),
    ("scene03", "99%", "R", 360, "99%", "thực đơn sứa biển", [0.75, 0.5]),
    ("scene03", "800 mét", "L", 380, "800 M", "độ sâu lặn săn", [0.3, 0.5]),
    ("scene03", "4°C", "R", 360, "4°C", "nhiệt độ biển sâu", [0.75, 0.5]),
    ("scene04", "40 loài", "R", 360, "40 LOÀI", "ký sinh trùng bám da", [0.75, 0.5]),
    ("scene04", "3 mét", "L", 380, "3 MÉT", "cú phóng vọt mặt nước", [0.28, 0.5]),
    ("scene05", "300 triệu", "R", 360, "300 TRIỆU", "kỷ lục sinh sản trứng", [0.75, 0.5]),
    ("scene05", "2 mm", "L", 380, "2 MM", "kích thước ấu trùng", [0.28, 0.5]),
    ("scene05", "60 triệu", "R", 360, "X60 TRIỆU", "tăng trưởng thể trọng", [0.75, 0.5])
]

# For each scene, find which beat interval [lo, hi) covers the trigger word
by_scene = {}
for b in sb["long"]:
    by_scene.setdefault(b["scene"], []).append(b)

for sid, beats in by_scene.items():
    sc_meta = next(x for x in ep["longform"]["scenes"] if x["id"] == sid)
    toks = script_tokens(" ".join(ptext(x) for x in sc_meta["parts"]), display)
    
    # Calculate beat intervals
    idx = []
    for b in beats:
        idx.append(find(toks, b["at"]))
    idx.append(len(toks))
    
    # Find stickers belonging to this scene
    st_defs = [s for s in long_stickers_def if s[0] == sid]
    for _, word, side, y, val, lbl, tgt in st_defs:
        try:
            w_idx = find(toks, word)
            # Find which beat index j covers w_idx
            assigned = False
            for j in range(len(beats)):
                lo = idx[j]
                hi = idx[j + 1]
                if lo <= w_idx < hi:
                    beats[j].setdefault("stickers", []).append({
                        "at": word,
                        "side": side,
                        "y": y,
                        "value": val,
                        "label": lbl,
                        "target": tgt
                    })
                    assigned = True
                    print(f"Assigned sticker {val} to {sid} beat {j} (interval {lo}..{hi})")
                    break
            if not assigned:
                print(f"WARNING: could not assign {val} in {sid}")
        except Exception as e:
            print(f"Error finding word {word} in {sid}: {e}")

# Shorts stickers
s_toks = script_tokens(ep["shorts"]["text"], display)
s_beats = sb["shorts"]
s_idx = [find(s_toks, b["at"]) for b in s_beats]
s_idx.append(len(s_toks))

shorts_st_defs = [
    ("2 tấn", "L", 500, "2 TẤN", "gã khổng lồ", [0.3, 0.5]),
    ("300 triệu", "R", 520, "300 TRIỆU", "kỷ lục sinh sản", [0.7, 0.5])
]
for word, side, y, val, lbl, tgt in shorts_st_defs:
    try:
        w_idx = find(s_toks, word)
        for j in range(len(s_beats)):
            lo = s_idx[j]
            hi = s_idx[j + 1]
            if lo <= w_idx < hi:
                s_beats[j].setdefault("stickers", []).append({
                    "at": word,
                    "side": side,
                    "y": y,
                    "value": val,
                    "label": lbl,
                    "target": tgt
                })
                print(f"Assigned shorts sticker {val} to beat {j}")
                break
    except Exception as e:
        print(f"Error finding shorts word {word}: {e}")

(P / "specs" / "storyboard.json").write_text(json.dumps(sb, ensure_ascii=False, indent=2), encoding="utf-8")
print("Reanchored stickers successfully!")

