import json
from pathlib import Path
from src.episode.pipeline import script_tokens, ptext

p = Path("projects/tap-34-qua-den/episode.json")
with open(p, "r", encoding="utf-8") as f:
    ep = json.load(f)

with open("projects/tap-34-qua-den/audio/long_words_fixed.json", "r", encoding="utf-8") as f:
    lw = json.load(f)

for sc in ep["longform"]["scenes"]:
    sc_id = sc["id"]
    words = lw[sc_id]
    total_dur = words[-1]["e"]
    print(f"{sc_id}: {len(words)} words, duration = {total_dur:.1f}s")
    # print word at every ~8-10s interval
    cur_t = 0
    intervals = []
    for w in words:
        if w["s"] >= cur_t:
            intervals.append((w["s"], w["w"]))
            cur_t += 8.5
    print("  intervals:", [(round(t, 1), w) for t, w in intervals])

