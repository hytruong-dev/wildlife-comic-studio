import json
import re

p_long = 'projects/tap-07-tom-tit/audio/long_words_fixed.json'
lw = json.load(open(p_long, encoding='utf-8'))
cleaned_lw = {}
for sid, ws in lw.items():
    cleaned_ws = [w for w in ws if not re.match(r'^\[[a-zA-Z0-9_\-]+\]$', w['w'])]
    print(f"Long {sid}: {len(ws)} -> {len(cleaned_ws)} words (removed {len(ws) - len(cleaned_ws)} tags)")
    cleaned_lw[sid] = cleaned_ws

with open(p_long, 'w', encoding='utf-8') as f:
    json.dump(cleaned_lw, f, ensure_ascii=False, indent=2)

p_shorts = 'projects/tap-07-tom-tit/audio/shorts_words.json'
sw = json.load(open(p_shorts, encoding='utf-8'))
cleaned_sw = [w for w in sw if not re.match(r'^\[[a-zA-Z0-9_\-]+\]$', w['word'])]
print(f"Shorts: {len(sw)} -> {len(cleaned_sw)} words (removed {len(sw) - len(cleaned_sw)} tags)")

with open(p_shorts, 'w', encoding='utf-8') as f:
    json.dump(cleaned_sw, f, ensure_ascii=False, indent=2)

print("Cleaned tags from long_words_fixed.json and shorts_words.json successfully!")
