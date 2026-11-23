import json
from pathlib import Path
from src.episode.build_plans import script_tokens, ptext, find, norm

P = Path("projects/tap-45-vet-kakapo")
sb = json.loads((P / "specs" / "storyboard.json").read_text(encoding="utf-8"))
ep = json.loads((P / "episode.json").read_text(encoding="utf-8"))
display = ep.get("display_fix", {})

by_scene = {}
for b in sb["long"]:
    by_scene.setdefault(b["scene"], []).append(b)

for sid, beats in by_scene.items():
    sc_meta = next(x for x in ep["longform"]["scenes"] if x["id"] == sid)
    toks = script_tokens(" ".join(ptext(x) for x in sc_meta["parts"]), display)
    total_len = len(toks)
    step = total_len / len(beats)
    
    idx = [0]
    beats[0]["at"] = 0
    
    for b_idx in range(1, len(beats)):
        target_token_idx = int(b_idx * step)
        best_phrase = None
        best_pos = None
        min_dist = 999
        
        for cand_idx in range(idx[-1] + 10, min(total_len - 4, target_token_idx + 25)):
            for n_words in (3, 4, 5):
                cand = " ".join(toks[cand_idx:cand_idx + n_words])
                try:
                    found_pos = find(toks, cand)
                    if found_pos > idx[-1]:
                        dist = abs(found_pos - target_token_idx)
                        if dist < min_dist:
                            min_dist = dist
                            best_phrase = cand
                            best_pos = found_pos
                        break
                except SystemExit:
                    pass
        assert best_phrase is not None, f"Could not find unique phrase for {sid} beat {b_idx}"
        beats[b_idx]["at"] = best_phrase
        idx.append(best_pos)
    print(f"{sid}: all {len(beats)} beats verified: {idx}")

# Shorts
s_toks = script_tokens(ep["shorts"]["text"], display)
s_total = len(s_toks)
s_step = s_total / len(sb["shorts"])
s_idx = [0]
sb["shorts"][0]["at"] = 0

for b_idx in range(1, len(sb["shorts"])):
    target_token_idx = int(b_idx * s_step)
    best_phrase = None
    best_pos = None
    min_dist = 999
    for cand_idx in range(s_idx[-1] + 6, min(s_total - 3, target_token_idx + 15)):
        for n_words in (3, 4, 5):
            cand = " ".join(s_toks[cand_idx:cand_idx + n_words])
            try:
                found_pos = find(s_toks, cand)
                if found_pos > s_idx[-1]:
                    dist = abs(found_pos - target_token_idx)
                    if dist < min_dist:
                        min_dist = dist
                        best_phrase = cand
                        best_pos = found_pos
                    break
            except SystemExit:
                pass
    assert best_phrase is not None, f"Could not find unique phrase for shorts beat {b_idx}"
    sb["shorts"][b_idx]["at"] = best_phrase
    s_idx.append(best_pos)

print(f"shorts: all {len(sb['shorts'])} beats verified: {s_idx}")

# Clear stickers and reanchor
for b in sb["long"]:
    b["stickers"] = []
for b in sb["shorts"]:
    b["stickers"] = []

long_stickers_def = [
    ("scene01", "4 kg", "R", 360, "4 KG", "thể trọng kỷ lục", [0.75, 0.5]),
    ("scene02", "60 cm", "L", 380, "60 CM", "chiều dài cơ thể", [0.28, 0.5]),
    ("scene02", "4 kg", "R", 360, "4 KG", "loài vẹt nặng nhất", [0.75, 0.5]),
    ("scene03", "60", "L", 380, "60-90 NĂM", "tuổi thọ kỷ lục", [0.3, 0.5]),
    ("scene04", "20 mét", "R", 360, "20 MÉT", "độ cao ngọn cây", [0.75, 0.5]),
    ("scene05", "5 km", "R", 360, "5 KM", "bán kính âm thanh", [0.75, 0.5]),
    ("scene06", "250", "R", 360, "250 CÁ THỂ", "quần thể toàn cầu", [0.75, 0.5])
]

for sid, beats in by_scene.items():
    sc_meta = next(x for x in ep["longform"]["scenes"] if x["id"] == sid)
    toks = script_tokens(" ".join(ptext(x) for x in sc_meta["parts"]), display)
    idx = [find(toks, b["at"]) for b in beats]
    idx.append(len(toks))
    
    st_defs = [s for s in long_stickers_def if s[0] == sid]
    for _, word, side, y, val, lbl, tgt in st_defs:
        try:
            w_idx = find(toks, word)
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
                    print(f"Assigned sticker {val} to {sid} beat {j} (interval {lo}..{hi})")
                    break
        except Exception as e:
            print(f"Error assigning {val} in {sid}: {e}")

# Shorts stickers
s_idx_full = [find(s_toks, b["at"]) for b in sb["shorts"]]
s_idx_full.append(len(s_toks))
shorts_st_defs = [
    ("4 kg", "L", 500, "4 KG", "vẹt nặng nhất", [0.3, 0.5]),
    ("5 km", "R", 520, "5 KM", "loa phóng thanh", [0.7, 0.5])
]
for word, side, y, val, lbl, tgt in shorts_st_defs:
    try:
        w_idx = find(s_toks, word)
        for j in range(len(sb["shorts"])):
            lo = s_idx_full[j]
            hi = s_idx_full[j + 1]
            if lo <= w_idx < hi:
                sb["shorts"][j].setdefault("stickers", []).append({
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
        print(f"Error assigning shorts sticker {val}: {e}")

(P / "specs" / "storyboard.json").write_text(json.dumps(sb, ensure_ascii=False, indent=2), encoding="utf-8")
print("Saved aligned storyboard.json for Ep 45!")

