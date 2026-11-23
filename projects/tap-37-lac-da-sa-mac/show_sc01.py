# -*- coding: utf-8 -*-
import json

sb = json.load(open('projects/tap-37-lac-da-sa-mac/specs/storyboard.json', encoding='utf-8'))
print("=== SCENE01 BEATS ===")
for i, b in enumerate(sb['long'][:12]):
    print(f"b{i+1:02d}: at={repr(b.get('at'))} | layout={b.get('layout', '')[:60]}")

