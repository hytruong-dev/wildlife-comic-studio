import json
from pathlib import Path

def finder(words):
    def f(text, after=0.0):
        t_low = text.lower().strip(".,!?:;\"'()")
        tokens = [x for x in t_low.split() if x]
        if not tokens: return after
        for i in range(len(words)):
            w = words[i]
            if not w or w.get("s", 0) < after: continue
            if words[i]["w"].lower().strip(".,!?:;\"'()") == tokens[0]:
                match = True
                for k in range(1, len(tokens)):
                    if i + k >= len(words) or words[i+k]["w"].lower().strip(".,!?:;\"'()") != tokens[k]:
                        match = False
                        break
                if match: return words[i]["s"]
        return after
    return f

P = Path("projects/tap-35-ca-voi-sat-thu")
plan = json.loads((P / "specs/longform_plan.json").read_text(encoding="utf-8"))
words = json.loads((P / "audio/long_words_fixed.json").read_text(encoding="utf-8"))

for sid, pl in plan["scenes"].items():
    T = finder(words[sid])
    D = json.loads((P / f"audio/{sid}_parts_duration.json").read_text())["total_duration"]
    print(f"=== {sid} (total {D:.1f}s) ===")
    beats = []
    for k, bp in enumerate(pl["beats"]):
        st = 0.0 if bp["at"] in (0, "0", "") else max(0.0, round(T(bp["at"]) - 0.30, 2))
        beats.append({"k": k, "at": bp["at"], "st": st})
    for i, b in enumerate(beats):
        nxt = beats[i+1]["st"] if i + 1 < len(beats) else D
        hold = nxt - b["st"]
        flag = " [TOO LONG >15s]" if hold > 15.0 else (" [TOO SHORT <2s]" if hold < 2.0 else "")
        print(f"  b{b['k']+1:02d}: {b['st']:5.1f}s -> {nxt:5.1f}s ({hold:4.1f}s) at={repr(str(b['at'])[:35])}{flag}")

print("\n=== SHORTS ===")
splan = json.loads((P / "specs/shorts_plan.json").read_text(encoding="utf-8"))
swords = json.loads((P / "audio/shorts_words.json").read_text(encoding="utf-8"))
vd = swords[-1]["end"]
Ts = finder(swords)
for idx, b in enumerate(splan["beats"]):
    st = 0.0 if b["at"] in (0, "0", "") else max(0.0, round(Ts(b["at"]) - 0.30, 2))
    nxt = vd if idx + 1 >= len(splan["beats"]) else max(0.0, round(Ts(splan["beats"][idx+1]["at"]) - 0.30, 2))
    hold = nxt - st
    flag = " [TOO LONG >7s]" if hold > 7.0 else (" [TOO SHORT <2s]" if hold < 2.0 else "")
    print(f"  s{idx+1:02d}: {st:4.1f}s -> {nxt:4.1f}s ({hold:4.1f}s) at={repr(str(b['at'])[:30])}{flag}")
