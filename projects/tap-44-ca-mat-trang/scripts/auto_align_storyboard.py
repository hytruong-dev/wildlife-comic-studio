import json
import re
from pathlib import Path
from src.episode.build_plans import script_tokens, ptext, find, norm

P = Path("projects/tap-44-ca-mat-trang")
ep = json.loads((P / "episode.json").read_text(encoding="utf-8"))
display = ep.get("display_fix", {})

# Let's inspect each scene and find clean unique phrases for our beats
scenes = ep["longform"]["scenes"]

# Define desired number of beats per scene:
# scene01: 9 beats
# scene02: 11 beats
# scene03: 10 beats
# scene04: 11 beats
# scene05: 10 beats
# scene06: 7 beats
# total: 58 beats

beat_targets = {
    "scene01": 9,
    "scene02": 11,
    "scene03": 10,
    "scene04": 11,
    "scene05": 10,
    "scene06": 7
}

scene_beats_phrases = {}

for sc in scenes:
    sid = sc["id"]
    n_beats = beat_targets[sid]
    toks = script_tokens(" ".join(ptext(x) for x in sc["parts"]), display)
    total_len = len(toks)
    step = total_len / n_beats
    
    # We want phrase at beat 0 to be 0
    phrases = [0]
    last_idx = 0
    
    for b in range(1, n_beats):
        target_idx = int(b * step)
        # Search around target_idx for a sentence or clause start
        best_phrase = None
        best_i = None
        min_dist = 999
        
        # Look around target_idx +/- 15 tokens
        start_search = max(last_idx + 12, target_idx - 15)
        end_search = min(total_len - 5, target_idx + 15)
        
        for cand_idx in range(start_search, end_search):
            cand_3 = " ".join(toks[cand_idx:cand_idx + 3])
            # Check if cand_3 is uniquely found after last_idx
            try:
                found_i = find(toks, cand_3, after=last_idx + 1)
                if found_i > last_idx:
                    dist = abs(found_i - target_idx)
                    if dist < min_dist:
                        min_dist = dist
                        best_phrase = cand_3
                        best_i = found_i
            except SystemExit:
                pass
        if not best_phrase:
            # Fallback to 4 tokens
            for cand_idx in range(start_search, end_search):
                cand_4 = " ".join(toks[cand_idx:cand_idx + 4])
                try:
                    found_i = find(toks, cand_4, after=last_idx + 1)
                    if found_i > last_idx:
                        best_phrase = cand_4
                        best_i = found_i
                        break
                except SystemExit:
                    pass
        assert best_phrase is not None, f"Could not find unique phrase for {sid} beat {b}"
        phrases.append(best_phrase)
        last_idx = best_i
        
    scene_beats_phrases[sid] = phrases
    print(f"{sid}: found {len(phrases)} beat phrases successfully!")

# Now do shorts (8 beats)
s_toks = script_tokens(ep["shorts"]["text"], display)
s_total = len(s_toks)
s_step = s_total / 8
shorts_phrases = [0]
s_last = 0
for b in range(1, 8):
    target_idx = int(b * s_step)
    best_phrase = None
    best_i = None
    min_dist = 999
    start_search = max(s_last + 8, target_idx - 8)
    end_search = min(s_total - 4, target_idx + 8)
    for cand_idx in range(start_search, end_search):
        cand_3 = " ".join(s_toks[cand_idx:cand_idx + 3])
        try:
            found_i = find(s_toks, cand_3, after=s_last + 1)
            if found_i > s_last:
                dist = abs(found_i - target_idx)
                if dist < min_dist:
                    min_dist = dist
                    best_phrase = cand_3
                    best_i = found_i
        except SystemExit:
            pass
    shorts_phrases.append(best_phrase)
    s_last = best_i

print("Shorts phrases:", shorts_phrases)

(P / "scripts" / "phrases.json").write_text(json.dumps({
    "scenes": scene_beats_phrases,
    "shorts": shorts_phrases
}, ensure_ascii=False, indent=2), encoding="utf-8")
print("Saved phrases.json successfully!")

