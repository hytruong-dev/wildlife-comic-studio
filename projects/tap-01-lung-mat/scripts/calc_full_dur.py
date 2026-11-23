import sys
from pathlib import Path
sys.path.insert(0, 'projects/tap-01-lung-mat/scripts')
from generate_full_duration_audio_125x import FULL_SCENES

total = 0
for sc in FULL_SCENES[:-1]:
    words = sum(len(p.split()) for p in sc['paragraphs'])
    # In Vietnamese at 1.25x: average speaking rate is ~3.2 words per second (190 wpm)
    sec = words / 3.2
    print(f"{sc['id']}: {words} words -> ~{sec:.1f}s ({sec/60:.2f} min)")
    total += sec
print(f"Total calculated duration: {total:.1f}s ({total/60:.2f} min, {int(total//60)}m {int(total%60)}s)")
