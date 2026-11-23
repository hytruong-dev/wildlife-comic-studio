import json, re

words = json.load(open('projects/tap-07-tom-tit/audio/long_words_fixed.json', encoding='utf-8'))
for sid, ws in words.items():
    tags = [w['w'] for w in ws if re.match(r'^\[.+\]$', w['w'])]
    print(f"{sid}: found {len(tags)} tags: {tags}")

sw = json.load(open('projects/tap-07-tom-tit/audio/shorts_words.json', encoding='utf-8'))
stags = [w['word'] for w in sw if re.match(r'^\[.+\]$', w['word'])]
print(f"shorts: found {len(stags)} tags: {stags}")
