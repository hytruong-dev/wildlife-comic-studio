import json, re

P = "projects/tap-15-capybara"
words = json.load(open(f"{P}/audio/long_words_fixed.json", encoding="utf-8"))
plan = json.load(open(f"{P}/specs/longform_plan.json", encoding="utf-8"))

def finder(ws):
    def T(phrase, after=0.0):
        toks = phrase.strip().split()
        first, rest = toks[0].lower(), [w.lower() for w in toks[1:]]
        for i, w in enumerate(ws):
            if w["s"] >= after and w["w"].lower() == first:
                if len(rest) == 0 or [x["w"].lower() for x in ws[i + 1 : i + 1 + len(rest)]] == rest:
                    return w["s"]
        return -1
    return T

for sid, pl in plan["scenes"].items():
    T = finder(words[sid])
    D = json.load(open(f"{P}/audio/{sid}_parts_duration.json", encoding="utf-8"))["total_duration"]
    print(f"\n=================== {sid} (total {D:.2f}s) ===================")
    beats = []
    for k, bp in enumerate(pl["beats"]):
        st = 0.0 if bp["at"] in (0, "0", "") else max(0.0, round(T(bp["at"]) - 0.30, 2))
        beats.append({"id": f"{sid}_b{k+1:02d}", "st": st, "at": bp["at"], "img": bp["image"]})
    for i, b in enumerate(beats):
        nxt = beats[i+1]["st"] if i+1 < len(beats) else D
        dur = nxt - b["st"]
        flag = " *** TOO SHORT (<2s)" if dur < 2.0 else (" *** TOO LONG (>15s)" if dur > 15.0 else "")
        print(f"  {b['id']} ({b['img']}): {b['st']:.2f}s - {nxt:.2f}s (dur {dur:.2f}s) | at: '{b['at']}'{flag}")

# Also check shorts
splan = json.load(open(f"{P}/specs/shorts_plan.json", encoding="utf-8"))
swords = json.load(open(f"{P}/audio/shorts_words.json", encoding="utf-8"))
sT = finder(swords)
sD = json.load(open(f"{P}/audio/shorts_parts_duration.json", encoding="utf-8"))["total_duration"]
print(f"\n=================== SHORTS (total {sD:.2f}s) ===================")
sbeats = []
for k, bp in enumerate(splan["beats"]):
    st = 0.0 if bp["at"] in (0, "0", "") else max(0.0, round(sT(bp["at"]) - 0.20, 2))
    sbeats.append({"id": f"s{k+1:02d}", "st": st, "at": bp["at"], "img": bp["image"]})
for i, b in enumerate(sbeats):
    nxt = sbeats[i+1]["st"] if i+1 < len(sbeats) else sD
    dur = nxt - b["st"]
    flag = " *** TOO LONG (>7s)" if dur > 7.0 else ""
    print(f"  {b['id']} ({b['img']}): {b['st']:.2f}s - {nxt:.2f}s (dur {dur:.2f}s) | at: '{b['at']}'{flag}")
