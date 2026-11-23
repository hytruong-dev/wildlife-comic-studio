import json

words = json.load(open('projects/tap-07-tom-tit/audio/long_words_fixed.json', encoding='utf-8'))

# Print all sentences in each scene with their start and end time
import re

for sid in ["scene01", "scene02", "scene03", "scene04", "scene05", "scene06"]:
    ws = words[sid]
    dur = ws[-1]['e']
    print(f"\n=================== {sid} (total {dur:.1f}s) ===================")
    cur_sentence = []
    st = ws[0]['s']
    for w in ws:
        cur_sentence.append(w['w'])
        if re.search(r'[.!?]$', w['w']):
            s_text = " ".join(cur_sentence)
            en = w['e']
            print(f"[{st:5.1f}s - {en:5.1f}s] (hold {en - st:4.1f}s): {s_text}")
            cur_sentence = []
            st = en
    if cur_sentence:
        print(f"[{st:5.1f}s - {dur:5.1f}s]: {' '.join(cur_sentence)}")
