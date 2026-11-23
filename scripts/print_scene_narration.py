import json

words = json.load(open('projects/tap-07-tom-tit/audio/long_words_fixed.json', encoding='utf-8'))

for sid in ["scene01", "scene02", "scene03", "scene04", "scene05", "scene06"]:
    ws = words[sid]
    print(f"\n=================== {sid} (total: {ws[-1]['e']:.1f}s) ===================")
    cur = 0.0
    line = []
    for w in ws:
        line.append(w['w'])
        if w['e'] - cur >= 10.0 or w['w'].endswith(('.', '!', '?')):
            t = w['e']
            print(f"[{cur:5.1f}s - {t:5.1f}s] {' '.join(line)}")
            line = []
            cur = t
    if line:
        print(f"[{cur:5.1f}s - {ws[-1]['e']:5.1f}s] {' '.join(line)}")
