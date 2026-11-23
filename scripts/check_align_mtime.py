from pathlib import Path
import time

p = Path("projects/tap-07-tom-tit/audio/long_words_fixed.json")
print("long_words_fixed.json modified ago:", time.time() - p.stat().st_mtime)
