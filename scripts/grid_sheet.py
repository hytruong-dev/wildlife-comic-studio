"""Images with a 10% coordinate grid, for measuring sticker `target` [x, y]:
python scripts/grid_sheet.py out.jpg img1 img2 ..."""
import sys
from pathlib import Path
import cv2, numpy as np

out, files = sys.argv[1], sys.argv[2:]
tiles = []
for f in files:
    im = cv2.imread(f)
    im = cv2.resize(im, (int(im.shape[1] * 560 / im.shape[0]), 560))
    h, w = im.shape[:2]
    for k in range(1, 10):
        cv2.line(im, (int(w * k / 10), 0), (int(w * k / 10), h), (0, 0, 255) if k == 5 else (255, 160, 0), 1)
        cv2.line(im, (0, int(h * k / 10)), (w, int(h * k / 10)), (0, 0, 255) if k == 5 else (255, 160, 0), 1)
        cv2.putText(im, str(k), (int(w * k / 10) + 2, 12), 0, 0.4, (0, 0, 200), 1)
        cv2.putText(im, str(k), (2, int(h * k / 10) - 2), 0, 0.4, (0, 0, 200), 1)
    cv2.putText(im, Path(f).stem, (6, h - 8), 0, 0.7, (0, 0, 255), 2)
    tiles.append(im)
row = np.hstack([np.pad(t, ((0, 0), (0, 6), (0, 0)), constant_values=255) for t in tiles])
cv2.imwrite(out, row)
print(out)
