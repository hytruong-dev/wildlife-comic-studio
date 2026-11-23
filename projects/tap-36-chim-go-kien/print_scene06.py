# -*- coding: utf-8 -*-
import json
words = json.load(open('projects/tap-36-chim-go-kien/audio/long_words_fixed.json', encoding='utf-8'))['scene06']
print("=== 0s to 20s ===")
for w in words:
    if w['s'] <= 20.0:
        print(f"{w['s']:5.1f}s - {w['e']:5.1f}s: {w['w']}")
print("=== 55s to end ===")
for w in words:
    if w['s'] >= 55.0:
        print(f"{w['s']:5.1f}s - {w['e']:5.1f}s: {w['w']}")

