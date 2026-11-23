import json
from pathlib import Path
from src.episode.pipeline import finder

P = Path("projects/tap-42-ca-thoi-loi")
lp = json.load(open(P / "specs/longform_plan.json", encoding="utf-8"))
words = json.load(open(P / "audio/long_words_fixed.json", encoding="utf-8"))

def examine_scene(sid):
    T = finder(words[sid])
    dur = json.load(open(P / f"audio/{sid}_parts_duration.json"))["total_duration"]
    beats = lp["scenes"][sid]["beats"]
    for i, b in enumerate(beats):
        st = 0.0 if b["at"] in (0, "0", "") else max(0.0, round(T(b["at"]) - 0.30, 2))
        nxt = dur if i + 1 == len(beats) else (0.0 if beats[i+1]["at"] in (0, "0", "") else max(0.0, round(T(beats[i+1]["at"]) - 0.30, 2)))
        hold = nxt - st
        flag = " *** HOLD > 15s ***" if hold > 15.0 else ""
        print(f"  {sid}_b{i+1:02d} ({b['image']}) at='{b['at']}': start={st:.2f}, nxt={nxt:.2f}, hold={hold:.2f}s{flag}")

for sid in ["scene01", "scene02", "scene06"]:
    print(f"--- {sid} ---")
    examine_scene(sid)

sp = json.load(open(P / "specs/shorts_plan.json", encoding="utf-8"))
sw = json.load(open(P / "audio/shorts_words.json", encoding="utf-8"))
Ts = finder(sw, ("word", "start"))
vd = 40.85
print("--- shorts ---")
for i, b in enumerate(sp["beats"]):
    st = float(b["at_s"]) if "at_s" in b else (0.0 if b["at"] in (0, "0", "") else max(0.0, round(Ts(b["at"]) - 0.25, 2)))
    nxt = vd if i + 1 == len(sp["beats"]) else (float(sp["beats"][i+1]["at_s"]) if "at_s" in sp["beats"][i+1] else (0.0 if sp["beats"][i+1]["at"] in (0, "0", "") else max(0.0, round(Ts(sp["beats"][i+1]["at"]) - 0.25, 2))))
    hold = nxt - st
    flag = " *** HOLD > 7s ***" if hold > 7.0 else ""
    print(f"  shorts_b{i+1:02d} ({b['image']}) at='{b.get('at', '')}': start={st:.2f}, nxt={nxt:.2f}, hold={hold:.2f}s{flag}")

