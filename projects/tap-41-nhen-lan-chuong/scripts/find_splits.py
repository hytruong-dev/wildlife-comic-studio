import json
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from src.episode.pipeline import finder

P = Path('projects/tap-41-nhen-lan-chuong')
plan = json.load(open(P / 'specs/longform_plan.json', encoding='utf-8'))
words = json.load(open(P / 'audio/long_words_fixed.json', encoding='utf-8'))
ep = json.load(open(P / 'episode.json', encoding='utf-8'))

for sid, pl in plan['scenes'].items():
    T = finder(words[sid])
    D = json.load(open(P / f'audio/{sid}_parts_duration.json'))['total_duration']
    beats = []
    for k, bp in enumerate(pl['beats']):
        st = 0.0 if bp['at'] in (0, '0', '') else max(0.0, round(T(bp['at']) - 0.30, 2))
        beats.append({'k': k+1, 'at': bp['at'], 'st': st})
    
    for i, b in enumerate(beats):
        nxt = beats[i+1]['st'] if i+1 < len(beats) else D
        hold = nxt - b['st']
        if hold > 15.0:
            mid = (b['st'] + nxt) / 2
            # find words around mid
            cand_words = [w for w in words[sid] if mid - 2.5 <= w['s'] <= mid + 2.5]
            full_window = ' '.join(w['w'] for w in words[sid] if b['st'] <= w['s'] <= nxt)
            # find sentences or clauses inside this window
            print(f"=== {sid} b{b['k']:02d} ({b['st']:.1f}s -> {nxt:.1f}s, hold {hold:.1f}s, target mid={mid:.1f}s) ===")
            print(f"  Window text: {full_window}")
            print("  Candidate words near mid:")
            for w in cand_words:
                print(f"    {w['s']:.2f}s: {w['w']}")
