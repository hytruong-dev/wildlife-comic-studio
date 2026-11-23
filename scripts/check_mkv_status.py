from pathlib import Path
import time

P = Path("projects/tap-07-tom-tit/renders/long_v2")
for f in sorted(P.glob("scene*.mkv")):
    st = f.stat()
    age = time.time() - st.st_mtime
    print(f"{f.name}: size={st.st_size:,} bytes, modified {age:.1f}s ago")
