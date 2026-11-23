# -*- coding: utf-8 -*-
import json

sw = json.load(open('projects/tap-37-lac-da-sa-mac/audio/shorts_words.json', encoding='utf-8'))
print("=== SHORTS 5s-18s ===")
for w in sw:
    if 5.0 <= w['start'] <= 18.0:
        print(f"{w['start']:5.2f}s - {w['end']:5.2f}s: {w['word']}")

w_sc01 = json.load(open('projects/tap-37-lac-da-sa-mac/audio/long_words_fixed.json', encoding='utf-8'))['scene01']
print("\n=== SCENE01 55s-85s ===")
for w in w_sc01:
    if 55.0 <= w['s'] <= 85.0:
        print(f"{w['s']:5.2f}s - {w['e']:5.2f}s: {w['w']}")

w_sc04 = json.load(open('projects/tap-37-lac-da-sa-mac/audio/long_words_fixed.json', encoding='utf-8'))['scene04']
print("\n=== SCENE04 35s-58s ===")
for w in w_sc04:
    if 35.0 <= w['s'] <= 58.0:
        print(f"{w['s']:5.2f}s - {w['e']:5.2f}s: {w['w']}")

w_sc05 = json.load(open('projects/tap-37-lac-da-sa-mac/audio/long_words_fixed.json', encoding='utf-8'))['scene05']
print("\n=== SCENE05 3s-25s ===")
for w in w_sc05:
    if 3.0 <= w['s'] <= 25.0:
        print(f"{w['s']:5.2f}s - {w['e']:5.2f}s: {w['w']}")

