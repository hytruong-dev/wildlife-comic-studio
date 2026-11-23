import json
from pathlib import Path

p = json.loads(Path('projects/tap-08-chon-gulo/specs/image_prompts.json').read_text(encoding='utf-8'))
words = json.loads(Path('projects/tap-08-chon-gulo/audio/long_words_fixed.json').read_text(encoding='utf-8'))

for sc in ['scene03', 'scene04', 'scene05', 'scene06']:
    ws = words[sc]
    print(f"\n=================== {sc} ===================")
    # Get all prompts for this scene
    if sc == 'scene03': items = p['longform'][24:38]
    elif sc == 'scene04': items = p['longform'][38:49]
    elif sc == 'scene05': items = p['longform'][49:57]
    elif sc == 'scene06': items = p['longform'][57:64]
    
    for item in items:
        q = item['quote']
        # find where quote appears in ws
        q_first = q.split()[0].replace(',', '').replace('.', '')
        print(f"  {item['id']}: quote='{q[:60]}...'")
