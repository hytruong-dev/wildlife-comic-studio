import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from src.episode.pipeline import finder

P = Path('projects/tap-41-nhen-lan-chuong')
sb = json.load(open(P / 'specs/storyboard.json', encoding='utf-8'))
words = json.load(open(P / 'audio/long_words_fixed.json', encoding='utf-8'))
sw = json.load(open(P / 'audio/shorts_words.json', encoding='utf-8'))

# Clean existing stickers from old beats that moved
for b in sb['long']:
    if b.get('id') == 'L02':
        # 50.000 was moved to L34
        b['stickers'] = [s for s in b.get('stickers', []) if s['at'] != '50.000']
    elif b.get('id') == 'L03':
        # 24/7 was moved to L35
        b['stickers'] = [s for s in b.get('stickers', []) if s['at'] != '24/7']
    elif b.get('id') == 'L13':
        # 'kẻ dệt sợi bạc' was moved to L42
        b['stickers'] = [s for s in b.get('stickers', []) if s['at'] != 'kẻ dệt sợi bạc']
    elif b.get('id') == 'L14':
        # 20 was moved to L43
        b['stickers'] = [s for s in b.get('stickers', []) if s['at'] != '20']
    elif b.get('id') == 'L16':
        # 24 giờ was moved to L44
        b['stickers'] = [s for s in b.get('stickers', []) if s['at'] != '24 giờ']
    elif b.get('id') == 'L19':
        # 30% was moved to L47
        b['stickers'] = [s for s in b.get('stickers', []) if s['at'] != '30%']
    elif b.get('id') == 'L22':
        # 'biệt thự thông tầng' was moved to L49
        b['stickers'] = [s for s in b.get('stickers', []) if s['at'] != 'biệt thự thông tầng']
    elif b.get('id') == 'L27':
        # '30 phút' was moved to L53
        b['stickers'] = [s for s in b.get('stickers', []) if s['at'] != '30 phút']

# Clean shorts S05 sticker
for b in sb['shorts']:
    if b.get('id') == 'S05':
        b['stickers'] = [s for s in b.get('stickers', []) if s['at'] != '24 giờ']

# Attach moved stickers to new beats
for b in sb['long']:
    if b.get('id') == 'L34':
        b['stickers'] = [{"at": "50.000", "side": "R", "y": 380, "value": "50.000", "label": "loài nhện duy nhất", "target": [0.35, 0.5]}]
    elif b.get('id') == 'L35':
        b['stickers'] = [{"at": "24/7", "side": "R", "y": 360, "value": "24/7", "label": "sống dưới nước", "target": [0.75, 0.5]}]
    elif b.get('id') == 'L42':
        b['stickers'] = [{"at": "kẻ dệt sợi bạc", "side": "L", "y": 360, "value": "Argyroneta", "label": "kẻ dệt sợi bạc", "target": [0.5, 0.5]}]
    elif b.get('id') == 'L43':
        b['stickers'] = [{"at": "20", "side": "R", "y": 360, "value": "20-30 LẦN", "label": "con thoi nạp khí", "target": [0.75, 0.5]}]
    elif b.get('id') == 'L44':
        b['stickers'] = [{"at": "24 giờ", "side": "R", "y": 360, "value": "24 GIỜ", "label": "thở thẩm thấu", "target": [0.75, 0.5]}]
    elif b.get('id') == 'L47':
        b['stickers'] = [{"at": "30%", "side": "R", "y": 360, "value": "+30%", "label": "đực lớn hơn cái", "target": [0.35, 0.5]}]
    elif b.get('id') == 'L49':
        b['stickers'] = [{"at": "biệt thự thông tầng", "side": "R", "y": 360, "value": "2 PHÒNG", "label": "biệt thự thông tầng", "target": [0.5, 0.5]}]
    elif b.get('id') == 'L53':
        b['stickers'] = [{"at": "30 phút", "side": "R", "y": 360, "value": "30 PHÚT", "label": "vá lành pháo đài", "target": [0.75, 0.5]}]

for b in sb['shorts']:
    if b.get('id') == 'S08':
        b['stickers'] = [{"at": "24 giờ", "side": "L", "y": 620, "value": "24 GIỜ", "label": "thở dưới nước", "target": [0.5, 0.5]}]

with open(P / 'specs/storyboard.json', 'w', encoding='utf-8') as f:
    json.dump(sb, f, ensure_ascii=False, indent=1)

print("Stickers successfully re-anchored!")
