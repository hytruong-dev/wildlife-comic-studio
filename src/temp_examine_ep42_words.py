import json

def show(sid, s_min, s_max):
    words = json.load(open('projects/tap-42-ca-thoi-loi/audio/long_words_fixed.json', encoding='utf-8'))[sid]
    txt = ' '.join(f"{w['w']}({w['s']:.1f})" for w in words if s_min <= w['s'] <= s_max)
    print(f"=== {sid} [{s_min}-{s_max}] ===\n{txt}\n")

show('scene01', 45, 66)
show('scene02', 0, 36)
show('scene02', 88, 108)
show('scene06', 50, 68)

swords = json.load(open('projects/tap-42-ca-thoi-loi/audio/shorts_words.json', encoding='utf-8'))
stxt = ' '.join(f"{w['word']}({w['start']:.1f})" for w in swords)
print(f"=== shorts ===\n{stxt}\n")

