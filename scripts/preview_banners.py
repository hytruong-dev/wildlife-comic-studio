"""Stack banner cutouts on dotted paper for review: python scripts/preview_banners.py projects/<slug>"""
import sys
from pathlib import Path
import cv2, numpy as np

P = Path(sys.argv[1])
fs = sorted((P / "assets/banners").glob("*.png"))
W = 1000
tiles = []
for f in fs:
    im = cv2.imread(str(f), cv2.IMREAD_UNCHANGED)
    s = W / im.shape[1]
    im = cv2.resize(im, (W, int(im.shape[0] * s)), interpolation=cv2.INTER_AREA)
    bg = np.full((im.shape[0] + 20, W + 20, 3), (215, 225, 235), np.uint8)
    a = im[:, :, 3:4].astype(np.float32) / 255
    roi = bg[10:10 + im.shape[0], 10:10 + W]
    roi[:] = (im[:, :, :3] * a + roi * (1 - a)).astype(np.uint8)
    cv2.putText(bg, f.stem, (14, 24), 0, 0.6, (0, 0, 255), 2)
    tiles.append(bg)
out = P / "renders/banner_preview.jpg"
cv2.imwrite(str(out), np.vstack(tiles))
print(out)
