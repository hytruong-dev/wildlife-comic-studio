"""Move ~/ep07_fix/<name>.txt into the inbox, import it, and write a small preview jpg."""
import shutil, subprocess, sys
from pathlib import Path
import cv2

P = Path("projects/tap-07-tom-tit")
src_dir = Path.home() / "ep07_fix"
for name in sys.argv[1:]:
    src = src_dir / f"{name}.txt"
    (P / "assets/inbox").mkdir(parents=True, exist_ok=True)
    shutil.copy(src, P / "assets/inbox" / f"{name}.txt")
subprocess.run([sys.executable, "src/episode/import_images.py", str(P)], check=True)
for name in sys.argv[1:]:
    im = cv2.imread(str(P / "assets/long" / f"{name}.png"))
    cv2.imwrite(str(src_dir / f"{name}_prev.jpg"), cv2.resize(im, (896, int(896 * im.shape[0] / im.shape[1]))))
    print("preview", src_dir / f"{name}_prev.jpg")
