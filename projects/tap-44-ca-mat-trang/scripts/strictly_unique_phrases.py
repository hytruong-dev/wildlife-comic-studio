import json
from pathlib import Path
from src.episode.build_plans import script_tokens, ptext, find, norm

P = Path("projects/tap-44-ca-mat-trang")
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
                # Check with build_plans find() from position 0
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
    print(f"{sid}: all {len(beats)} beats verified with find(): {idx}")

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

print(f"shorts: all {len(sb['shorts'])} beats verified with find(): {s_idx}")

(P / "specs" / "storyboard.json").write_text(json.dumps(sb, ensure_ascii=False, indent=2), encoding="utf-8")
print("Saved verified unique phrases to storyboard.json!")
