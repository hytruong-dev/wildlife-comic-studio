# -*- coding: utf-8 -*-
import json
import re

def norm(w):
    return re.sub(r"[^\w\s]", "", w.lower()).strip()

def finder(words, ks=("w", "s")):
    n = [norm(w[ks[0]]) for w in words]
    def T(phrase, after=0.0):
        toks = [norm(x) for x in phrase.split() if norm(x)]
        for i in range(len(words) - len(toks) + 1):
            if words[i][ks[1]] >= after and n[i:i + len(toks)] == toks:
                return words[i][ks[1]]
        return None
    return T

plan = json.load(open('projects/tap-37-lac-da-sa-mac/specs/longform_plan.json', encoding='utf-8'))
words = json.load(open('projects/tap-37-lac-da-sa-mac/audio/long_words_fixed.json', encoding='utf-8'))

for sid in ['scene01', 'scene04', 'scene05']:
    pl = plan['scenes'][sid]
    w_list = words[sid]
    T = finder(w_list)
    D = json.load(open(f'projects/tap-37-lac-da-sa-mac/audio/{sid}_parts_duration.json'))["total_duration"]
    beats = []
    for k, bp in enumerate(pl["beats"]):
        st = 0.0 if bp["at"] in (0, "0", "") else max(0.0, round(T(bp["at"]) - 0.30, 2))
        beats.append({"id": f"{sid}_b{k+1:02d}", "at": bp["at"], "start_s": st, "image": bp["image"]})
    print(f"\n==================== {sid} (D={D:.1f}s) ====================")
    for i, b in enumerate(beats):
        nxt = beats[i + 1]["start_s"] if i + 1 < len(beats) else D
        hold = nxt - b["start_s"]
        status = "OK"
        if hold > 15.0:
            status = f"TOO LONG ({hold:.1f}s > 15s)"
        elif hold < 2.0:
            status = f"TOO SHORT ({hold:.1f}s < 2s)"
        print(f"  {b['id']}: start={b['start_s']:5.1f}s, hold={hold:4.1f}s, at={repr(b['at'])} [{status}]")

# shorts
sp = json.load(open('projects/tap-37-lac-da-sa-mac/specs/shorts_plan.json', encoding='utf-8'))
sw = json.load(open('projects/tap-37-lac-da-sa-mac/audio/shorts_words.json', encoding='utf-8'))
Ts = finder(sw, ("word", "start"))
Ds = 39.86
sbeats = []
for k, bp in enumerate(sp["beats"]):
    st = 0.0 if bp["at"] in (0, "0", "") else max(0.0, round(Ts(bp["at"]) - 0.30, 2))
    sbeats.append({"id": f"s{k+1:02d}", "at": bp["at"], "start_s": st})
print(f"\n==================== SHORTS (D={Ds:.1f}s) ====================")
for i, b in enumerate(sbeats):
    nxt = sbeats[i + 1]["start_s"] if i + 1 < len(sbeats) else Ds
    hold = nxt - b["start_s"]
    status = "OK"
    if hold > 7.0:
        status = f"TOO LONG ({hold:.1f}s > 7s)"
    elif hold < 2.0:
        status = f"TOO SHORT ({hold:.1f}s < 2s)"
    print(f"  {b['id']}: start={b['start_s']:5.1f}s, hold={hold:4.1f}s, at={repr(b['at'])} [{status}]")

