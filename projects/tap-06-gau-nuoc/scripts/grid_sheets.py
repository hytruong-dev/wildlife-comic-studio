"""Contact sheets with a 0.1 normalised grid, used to pick exact arrow targets (fx, fy)."""
import sys
from pathlib import Path

import cv2
import numpy as np

proj = Path(__file__).parents[1]
src = proj / "assets" / sys.argv[1]
names = sys.argv[2].split(",")
out = Path(sys.argv[3])
tiles = []
for n in names:
    p = src / n if n.endswith(".png") else src / f"{n}.png"
    im = cv2.resize(cv2.imread(str(p)), (800, 447))
    for k in range(1, 10):
        x, y = int(800 * k / 10), int(447 * k / 10)
        cv2.line(im, (x, 0), (x, 447), (255, 0, 255), 1)
        cv2.line(im, (0, y), (800, y), (255, 0, 255), 1)
        cv2.putText(im, f".{k}", (x + 2, 12), 0, 0.4, (200, 0, 200), 1)
        cv2.putText(im, f".{k}", (2, y - 2), 0, 0.4, (200, 0, 200), 1)
    cv2.putText(im, p.stem, (10, 440), 0, 0.8, (0, 0, 255), 2)
    tiles.append(im)
while len(tiles) % 2:
    tiles.append(np.full_like(tiles[0], 255))
cv2.imwrite(str(out), np.vstack([np.hstack(tiles[i:i + 2]) for i in range(0, len(tiles), 2)]))
