# -*- coding: utf-8 -*-
import json

words = json.load(open('projects/tap-33-ech-go-bac-cuc/audio/long_words_fixed.json', encoding='utf-8'))
targets = [
    ("scene01", 65.9, 81.8),
    ("scene01", 81.8, 99.0),
    ("scene01", 99.0, 118.2),
    ("scene02", 0.0, 24.9),
    ("scene02", 24.9, 44.9),
    ("scene02", 56.6, 78.1),
    ("scene03", 0.0, 19.4),
    ("scene03", 42.2, 67.8),
    ("scene03", 79.8, 94.9),
    ("scene04", 0.0, 18.3),
    ("scene04", 43.3, 74.7),
    ("scene04", 95.8, 113.6),
    ("scene05", 0.0, 18.5),
    ("scene05", 18.5, 41.2),
    ("scene05", 50.8, 72.6),
    ("scene06", 0.0, 17.2),
    ("scene06", 28.6, 44.3),
    ("scene06", 44.3, 64.6),
    ("scene06", 64.6, 88.7),
    ("scene06", 98.0, 116.1),
]

for sid, t0, t1 in targets:
    mid = (t0 + t1) / 2
    in_range = [w for w in words[sid] if t0 + 2 <= w["s"] <= t1 - 2]
    # pick 3-word phrase around midpoint
    closest = min(in_range, key=lambda w: abs(w["s"] - mid)) if in_range else None
    if closest:
        idx = words[sid].index(closest)
        phrase = " ".join(w["w"] for w in words[sid][idx:idx+3])
        print(f"{sid} [{t0:.1f}-{t1:.1f}s] mid={mid:.1f}s: at '{phrase}' (time {closest['s']:.1f}s)")
    else:
        print(f"{sid} [{t0:.1f}-{t1:.1f}s]: NO WORDS FOUND")

swords = json.load(open('projects/tap-33-ech-go-bac-cuc/audio/shorts_words.json', encoding='utf-8'))
print("=== SHORTS ===")
for t0, t1 in [(0.0, 11.2), (20.0, 28.8), (28.8, 36.5)]:
    in_range = [w for w in swords if t0 + 1 <= w["start"] <= t1 - 1]
    mid = (t0 + t1) / 2
    closest = min(in_range, key=lambda w: abs(w["start"] - mid)) if in_range else None
    if closest:
        idx = swords.index(closest)
        phrase = " ".join(w["word"] for w in swords[idx:idx+3])
        print(f"Shorts [{t0:.1f}-{t1:.1f}s]: at '{phrase}' (time {closest['start']:.1f}s)")
