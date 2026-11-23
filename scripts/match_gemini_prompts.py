import json, re, sys
from pathlib import Path
import numpy as np
from PIL import Image

raw = Path(sys.argv[1]).read_text(encoding="utf-8")
m = re.search(r'### Result\s*"(.*)"\s*###', raw, re.S) or re.search(r'"(\{.*\})"', raw, re.S)
s = m.group(1).encode().decode("unicode_escape")
fp = {int(k): np.array([int(x) for x in v.split(",")], float)
      for k, v in json.loads(s).items() if v and v[0].isdigit()}
for f in sorted(Path("projects/tap-07-tom-tit/assets/long").glob("L*.png")):
    im = np.asarray(Image.open(f).convert("L").resize((32, 18), Image.BILINEAR), float).ravel()
    best = sorted(((np.abs(im - v).mean(), k) for k, v in fp.items()))[:2]
    print(f.stem, "-> prompt", best[0][1], f"(d={best[0][0]:.1f}; next {best[1][1]} d={best[1][0]:.1f})")
