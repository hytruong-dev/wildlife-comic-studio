import json, re

lw = json.load(open('projects/tap-07-tom-tit/audio/long_words_fixed.json', encoding='utf-8'))
found_long = []
for sid, ws in lw.items():
    for w in ws:
        if re.search(r'\[.+\]', w['w']):
            found_long.append((sid, w['w']))

if found_long:
    print(f"FAILED: Found {len(found_long)} tags in long words: {found_long}")
else:
    print("SUCCESS: ZERO emotion tags found in long_words_fixed.json!")

sw = json.load(open('projects/tap-07-tom-tit/audio/shorts_words.json', encoding='utf-8'))
found_shorts = []
for w in sw:
    if re.search(r'\[.+\]', w['word']):
        found_shorts.append(w['word'])

if found_shorts:
    print(f"FAILED: Found {len(found_shorts)} tags in shorts words: {found_shorts}")
else:
    print("SUCCESS: ZERO emotion tags found in shorts_words.json!")

sspec = json.load(open('projects/tap-07-tom-tit/specs/shorts_spec.json', encoding='utf-8'))
shorts_caps_tags = []
for b in sspec['beats']:
    for c in b.get('captions', []):
        if re.search(r'\[.+\]', c.get('text', '')):
            shorts_caps_tags.append((b['id'], c['text']))

if shorts_caps_tags:
    print(f"FAILED: Found {len(shorts_caps_tags)} tags in shorts_spec.json captions: {shorts_caps_tags}")
else:
    print("SUCCESS: ZERO emotion tags found in shorts_spec.json captions!")
