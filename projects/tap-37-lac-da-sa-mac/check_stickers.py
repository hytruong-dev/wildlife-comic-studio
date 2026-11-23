# -*- coding: utf-8 -*-
import json

sb = json.load(open('projects/tap-37-lac-da-sa-mac/specs/storyboard.json', encoding='utf-8'))
for i in [9, 10]:
    b = sb['long'][i]
    print(f"b{i+1}: at={b.get('at')} | stickers={b.get('stickers')}")

