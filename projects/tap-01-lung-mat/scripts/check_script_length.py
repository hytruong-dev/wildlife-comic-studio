import sys
from pathlib import Path
sys.path.insert(0, 'projects/tap-01-lung-mat/scripts')
from generate_full_duration_audio_125x import FULL_SCENES

total_chars = 0
total_words = 0
for sc in FULL_SCENES[:-1]:
    chars = sum(len(p) for p in sc['paragraphs'])
    words = sum(len(p.split()) for p in sc['paragraphs'])
    print(f"{sc['id']}: {len(sc['paragraphs'])} paras | {words} words | {chars} chars | target: {sc['target_sec']}s")
    total_chars += chars
    total_words += words
print(f"TOTAL: {total_words} words | {total_chars} chars")
