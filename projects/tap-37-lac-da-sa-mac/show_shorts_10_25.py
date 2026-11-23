# -*- coding: utf-8 -*-
import json

sw = json.load(open('projects/tap-37-lac-da-sa-mac/audio/shorts_words.json', encoding='utf-8'))
for w in sw:
    if 10.0 <= w['start'] <= 25.0:
        print(f"{w['start']:5.2f}s - {w['end']:5.2f}s: {w['word']}")

