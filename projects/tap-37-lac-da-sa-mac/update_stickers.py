# -*- coding: utf-8 -*-
import json

path = 'projects/tap-37-lac-da-sa-mac/specs/storyboard.json'
with open(path, encoding='utf-8') as f:
    sb = json.load(f)

# Update b10 and b11 stickers
sb['long'][9]['stickers'] = [
    {'at': '15%', 'side': 'L', 'y': 390, 'value': '15%', 'label': 'người ngừng đập', 'target': [0.35, 0.45]}
]

sb['long'][10]['stickers'] = [
    {'at': '30%', 'side': 'R', 'y': 370, 'value': '30%', 'label': 'lạc đà chịu tải', 'target': [0.65, 0.45]},
    {'at': '40%', 'side': 'L', 'y': 420, 'value': '40%', 'label': 'giới hạn tối đa', 'target': [0.35, 0.5]}
]

with open(path, 'w', encoding='utf-8') as f:
    json.dump(sb, f, ensure_ascii=False, indent=2)

print("Updated b10 and b11 stickers successfully!")

