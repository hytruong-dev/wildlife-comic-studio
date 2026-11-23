"""Xóa logo Gemini (ngôi sao 4 cánh ✦ góc phải-dưới) khỏi ẢNH và VIDEO tải từ Gemini / Veo.

Nguyên lý (reverse alpha blending — khôi phục đúng màu gốc, không làm nhòe):
    Gemini dán logo trắng lên ảnh:  I = a*255 + (1-a)*G
    => ảnh gốc:                     G = (I - a*255) / (1 - a)
    `a` là bản đồ alpha chuẩn của logo (assets/watermark/gemini_alpha_{48,96}.png, lấy từ
    journey-ad/gemini-watermark-remover, kiểm chứng lại bằng ảnh tải về của kênh: tương quan 0.92).

Luật vị trí của ẢNH Gemini:
    - cạnh ngắn  > 1024 px  -> logo 96x96, cách mép phải/dưới 64 px
    - còn lại               -> logo 48x48, cách mép phải/dưới 32 px
  Tool dò quanh vị trí chuẩn (±6 px) + đo độ đậm. File tên Gemini_Generated_Image_* luôn được xóa.
VIDEO (Veo) logo khác vị trí -> tool tự dò trên góc phải-dưới bằng thống kê nhiều khung hình.

Dùng:
  python src/image/gemini_watermark.py image a.png b.jpg ...            # ghi a_clean.png ...
  python src/image/gemini_watermark.py image "C:/Users/PC/Downloads/Gemini_Generated_Image_*.png" --out-dir clean/
  python src/image/gemini_watermark.py image folder/ --inplace          # ghi đè (bản gốc giữ ở folder/_raw/)
  python src/image/gemini_watermark.py watch                            # theo dõi Downloads: ảnh Gemini mới tự xóa logo
  python src/image/gemini_watermark.py video in.mp4 out.mp4             # tự dò logo, giữ nguyên âm thanh
  python src/image/gemini_watermark.py video in.mp4 out.mp4 --box 1136,576,48 --gain 0.72
Trong code:
  from src.image.gemini_watermark import clean_image
  out, info = clean_image(cv2.imread(p))
"""
from __future__ import annotations

import argparse
import glob
import shutil
import subprocess
import sys
import time
from pathlib import Path

import cv2
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
ALPHA_DIR = ROOT / "assets" / "watermark"
IMG_EXT = (".png", ".jpg", ".jpeg", ".webp")

_ALPHA: dict[int, np.ndarray] = {}


def alpha_ref(size: int) -> np.ndarray:
    """Alpha map of the Gemini logo at `size`x`size` (float32, 0..~0.51)."""
    if size not in _ALPHA:
        base = 48 if size <= 48 else 96
        a = cv2.imread(str(ALPHA_DIR / f"gemini_alpha_{base}.png"), cv2.IMREAD_COLOR)
        if a is None:
            raise FileNotFoundError(ALPHA_DIR / f"gemini_alpha_{base}.png")
        a = a.astype(np.float32).max(2) / 255.0
        if size != base:
            a = cv2.resize(a, (size, size), interpolation=cv2.INTER_AREA if size < base else cv2.INTER_CUBIC)
        _ALPHA[size] = np.clip(a, 0, 1)
    return _ALPHA[size]


def unblend(img: np.ndarray, x0: int, y0: int, alpha: np.ndarray, gain: float = 1.0) -> np.ndarray:
    """Reverse alpha blend a white logo with given alpha at (x0,y0). Works on uint8 BGR/BGRA."""
    out = img.copy()
    s = alpha.shape[0]
    h, w = img.shape[:2]
    xa, ya, xb, yb = max(0, x0), max(0, y0), min(w, x0 + s), min(h, y0 + s)
    if xb <= xa or yb <= ya:
        return out
    a = np.clip(alpha[ya - y0:yb - y0, xa - x0:xb - x0] * gain, 0, 0.97)[:, :, None]
    p = out[ya:yb, xa:xb, :3].astype(np.float32)
    g = (p - a * 255.0) / (1.0 - a)
    out[ya:yb, xa:xb, :3] = np.where(a > 0.002, np.clip(np.rint(g), 0, 255), p).astype(np.uint8)
    return out


def _fit(gray: np.ndarray, x0: int, y0: int, a: np.ndarray):
    """Least-squares fit of I = B + gain*a*(255-B) with B = robust local background. Returns (corr, gain)."""
    s = a.shape[0]
    p = gray[y0:y0 + s, x0:x0 + s]
    if p.shape != a.shape:
        return -1.0, 0.0
    pad = 3
    reg = gray[max(0, y0 - pad):y0 + s + pad, max(0, x0 - pad):x0 + s + pad]
    B = float(np.median(np.concatenate([reg[:2].ravel(), reg[-2:].ravel(), reg[:, :2].ravel(), reg[:, -2:].ravel()])))
    if B > 245:  # white over white: invisible, nothing to remove
        return -1.0, 0.0
    m = a * (255.0 - B)
    d = p - B
    gain = float((d * m).sum() / max((m * m).sum(), 1e-6))
    pc = p - p.mean(); ac = a - a.mean()
    corr = float((pc * ac).sum() / (np.sqrt((pc * pc).sum() * (ac * ac).sum()) + 1e-6))
    return corr, gain


def detect_image(img: np.ndarray, search: int = 6, min_corr: float = 0.35):
    """Find the Gemini logo in a still image. Returns dict(x0,y0,size,gain,corr) or None."""
    h, w = img.shape[:2]
    gray = cv2.cvtColor(img[:, :, :3], cv2.COLOR_BGR2GRAY).astype(np.float32)
    big = min(h, w) > 1024
    cands = [(96, 64), (48, 32)] if big else [(48, 32), (96, 64)]
    best = None
    for size, margin in cands:
        a = alpha_ref(size)
        bx, by = w - margin - size, h - margin - size
        for dy in range(-search, search + 1):
            for dx in range(-search, search + 1):
                corr, gain = _fit(gray, bx + dx, by + dy, a)
                if best is None or corr > best["corr"]:
                    best = dict(x0=bx + dx, y0=by + dy, size=size, gain=gain, corr=corr)
    if best and best["corr"] >= min_corr and 0.25 <= best["gain"] <= 1.6:
        best["gain"] = float(np.clip(best["gain"], 0.25, 1.0)) if best["corr"] < 0.8 else 1.0
        return best
    return None


def clean_image(img: np.ndarray, force: bool = False):
    """Remove the Gemini logo if present. Returns (cleaned_img, info|None).
    force=True: always unblend at the standard spot (use for known-raw Gemini downloads)."""
    info = detect_image(img)
    if info is None and force:
        h, w = img.shape[:2]
        size, margin = (96, 64) if min(h, w) > 1024 else (48, 32)
        info = dict(x0=w - margin - size, y0=h - margin - size, size=size, gain=1.0, corr=0.0)
    if info is None:
        return img, None
    return unblend(img, info["x0"], info["y0"], alpha_ref(info["size"]), info["gain"]), info


def clean_file_inplace(f: Path, force: bool = False):
    """Xóa logo trong file, ghi đè; bản gốc chép vào <thư mục>/_raw/. Trả về info hoặc None."""
    img = cv2.imread(str(f), cv2.IMREAD_COLOR)
    if img is None:
        return None
    out, info = clean_image(img, force=force or f.name.startswith("Gemini_Generated_Image"))
    if info is None:
        return None
    raw = f.parent / "_raw"
    raw.mkdir(exist_ok=True)
    if not (raw / f.name).exists():
        shutil.copy2(f, raw / f.name)
    if f.suffix.lower() in (".jpg", ".jpeg"):
        cv2.imwrite(str(f), out, [cv2.IMWRITE_JPEG_QUALITY, 97])
    else:
        cv2.imwrite(str(f), out)
    return info


# ----------------------------------------------------------------------------------- watch
def watch(folder: Path, only_gemini: bool = True, interval: float = 2.0):
    """Chạy nền: ảnh mới xuất hiện trong `folder` được xóa logo Gemini ngay (mỗi file 1 lần)."""
    seen = {p.name for p in folder.iterdir() if p.is_file()}  # ảnh có sẵn: bỏ qua (dùng lệnh `image` nếu cần)
    print(f"[watch] Đang theo dõi {folder} — ảnh Gemini mới tải về sẽ tự xóa logo (Ctrl+C để dừng)", flush=True)
    pending: dict[str, int] = {}
    while True:
        try:
            for p in folder.iterdir():
                if not p.is_file() or p.name in seen or p.suffix.lower() not in IMG_EXT:
                    continue
                if only_gemini and not p.name.startswith("Gemini_Generated_Image"):
                    seen.add(p.name)
                    continue
                size = p.stat().st_size
                if pending.get(p.name) != size:  # đợi file tải xong (kích thước ổn định)
                    pending[p.name] = size
                    continue
                seen.add(p.name)
                pending.pop(p.name, None)
                info = clean_file_inplace(p)
                msg = f"đã xóa logo {info['size']}px" if info else "không có logo"
                print(f"[watch] {p.name}: {msg}", flush=True)
        except Exception as e:
            print(f"[watch] lỗi: {e}", flush=True)
        time.sleep(interval)


# ----------------------------------------------------------------------------------- video
def _read_frames(src: str, step: int = 1):
    cap = cv2.VideoCapture(src)
    i = 0
    while True:
        ok, f = cap.read()
        if not ok:
            break
        if i % step == 0:
            yield f
        i += 1
    cap.release()


def detect_video(src: str, region=0.35, sizes=range(28, 100, 4)):
    """Find a STATIC Gemini/Veo logo in the bottom-right `region` of the video.
    Temporal estimate of alpha ((I - median31(I)) / (255 - median31(I)) averaged over frames),
    then template-match the reference logo shape on it."""
    acc = None
    n = 0
    x1 = y1 = 0
    for f in _read_frames(src, step=3):
        h, w = f.shape[:2]
        y1, x1 = int(h * (1 - region)), int(w * (1 - region))
        g = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)[y1:, x1:]
        B = cv2.medianBlur(g, 31).astype(np.float32)
        est = (g.astype(np.float32) - B) / np.maximum(255.0 - B, 20.0)
        acc = est if acc is None else acc + est
        n += 1
    E = (acc / max(n, 1)).astype(np.float32)
    best = None
    for s in sizes:
        r = cv2.matchTemplate(E, alpha_ref(s), cv2.TM_CCOEFF_NORMED)
        _, mv, _, ml = cv2.minMaxLoc(r)
        if best is None or mv > best[0]:
            best = (mv, s, ml)
    corr, s, (mx, my) = best
    return dict(x0=x1 + mx, y0=y1 + my, size=s, corr=float(corr), frames=n)


def refine_video_gain(src: str, x0: int, y0: int, size: int) -> float:
    """Logo strength by least squares over many frames (background = Navier-Stokes inpaint around the logo)."""
    a = alpha_ref(size)
    pad = 10
    hole = np.zeros((size + 2 * pad, size + 2 * pad), np.uint8)
    hole[pad:-pad, pad:-pad] = cv2.dilate((a > 0.02).astype(np.uint8), np.ones((5, 5), np.uint8)) * 255
    num = den = 0.0
    for f in _read_frames(src, step=4):
        p = f[y0 - pad:y0 + size + pad, x0 - pad:x0 + size + pad]
        if p.shape[:2] != hole.shape:
            continue
        B = cv2.inpaint(p, hole, 7, cv2.INPAINT_NS).astype(np.float32)[pad:-pad, pad:-pad].mean(2)
        I = p.astype(np.float32)[pad:-pad, pad:-pad].mean(2)
        m = a * (255.0 - B)
        num += ((I - B) * m).sum()
        den += (m * m).sum()
    return float(num / max(den, 1e-6))


def clean_video(src: str, dst: str, box=None, gain=None, crf: int = 16, extra_boxes=()):
    """Remove a static Gemini logo from every frame, keep audio, write H.264 (yuv420p, 48k AAC, tbn 12288)."""
    if box is None:
        info = detect_video(src)
        x0, y0, size = info["x0"], info["y0"], info["size"]
        print(f"[detect] logo {size}px at ({x0},{y0}) corr={info['corr']:.2f}")
    else:
        x0, y0, size = box
    if gain is None:
        gain = refine_video_gain(src, x0, y0, size)
        print(f"[fit] gain={gain:.2f}")
    boxes = [(x0, y0, size, gain)] + [tuple(b) for b in extra_boxes]
    cap = cv2.VideoCapture(src)
    fps = cap.get(cv2.CAP_PROP_FPS) or 24.0
    w, h = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    dst_p = Path(dst)
    tmp = dst_p.with_name(dst_p.stem + "_noaudio_tmp.mp4")
    enc = subprocess.Popen([
        "ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{w}x{h}",
        "-r", f"{fps}", "-i", "-", "-c:v", "libx264", "-preset", "slow", "-crf", str(crf),
        "-pix_fmt", "yuv420p", str(tmp)], stdin=subprocess.PIPE)
    n = 0
    while True:
        ok, f = cap.read()
        if not ok:
            break
        for bx, by, bs, bg in boxes:
            f = unblend(f, bx, by, alpha_ref(bs), bg)
        enc.stdin.write(f.tobytes())
        n += 1
    cap.release()
    enc.stdin.close()
    enc.wait()
    subprocess.run([
        "ffmpeg", "-y", "-loglevel", "error", "-i", str(tmp), "-i", src, "-map", "0:v:0", "-map", "1:a:0?",
        "-c:v", "copy", "-c:a", "aac", "-b:a", "320k", "-ar", "48000", "-ac", "2",
        "-video_track_timescale", "12288", "-movflags", "+faststart", str(dst_p)], check=True)
    tmp.unlink(missing_ok=True)
    print(f"[done] {n} frames -> {dst_p}")
    return boxes


# ----------------------------------------------------------------------------------- CLI
def _expand(paths):
    out = []
    for p in paths:
        pp = Path(p)
        if pp.is_dir():
            out += sorted(q for q in pp.iterdir() if q.suffix.lower() in IMG_EXT and "_clean" not in q.stem)
        else:
            out += [Path(q) for q in sorted(glob.glob(p))] or [pp]
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    pi = sub.add_parser("image")
    pi.add_argument("paths", nargs="+")
    pi.add_argument("--out-dir")
    pi.add_argument("--inplace", action="store_true", help="ghi đè, bản gốc chép vào <thư mục>/_raw/")
    pi.add_argument("--force", action="store_true", help="xóa ở vị trí chuẩn kể cả khi không dò thấy")
    pv = sub.add_parser("video")
    pv.add_argument("src")
    pv.add_argument("dst")
    pv.add_argument("--box", help="x0,y0,size (bỏ qua để tự dò)")
    pv.add_argument("--gain", type=float)
    pv.add_argument("--extra", action="append", default=[], help="thêm logo khác: x0,y0,size,gain")
    pw = sub.add_parser("watch", help="theo dõi thư mục, ảnh Gemini mới tải về tự được xóa logo (ghi đè, gốc ở _raw/)")
    pw.add_argument("folder", nargs="?", default=str(Path.home() / "Downloads"))
    pw.add_argument("--all", action="store_true", help="xử lý mọi ảnh (mặc định chỉ Gemini_Generated_Image_*)")
    pw.add_argument("--interval", type=float, default=2.0)
    args = ap.parse_args()

    if args.cmd == "watch":
        watch(Path(args.folder), only_gemini=not args.all, interval=args.interval)
        return

    if args.cmd == "video":
        box = tuple(int(v) for v in args.box.split(",")) if args.box else None
        extra = [tuple(float(v) if i == 3 else int(v) for i, v in enumerate(e.split(","))) for e in args.extra]
        clean_video(args.src, args.dst, box=box, gain=args.gain, extra_boxes=extra)
        return

    files = _expand(args.paths)
    done = 0
    for f in files:
        img = cv2.imread(str(f), cv2.IMREAD_COLOR)
        if img is None:
            print(f"[skip] không đọc được {f}")
            continue
        if args.inplace:
            info = clean_file_inplace(f, force=args.force)
            dst = f
        else:
            # File tải thẳng từ Gemini (Gemini_Generated_Image_*) LUÔN có logo -> xóa ở vị trí chuẩn.
            out, info = clean_image(img, force=args.force or f.name.startswith("Gemini_Generated_Image"))
            if info is not None:
                if args.out_dir:
                    Path(args.out_dir).mkdir(parents=True, exist_ok=True)
                    dst = Path(args.out_dir) / f.name
                else:
                    dst = f.with_name(f.stem + "_clean" + f.suffix)
                if dst.suffix.lower() in (".jpg", ".jpeg"):
                    cv2.imwrite(str(dst), out, [cv2.IMWRITE_JPEG_QUALITY, 97])
                else:
                    cv2.imwrite(str(dst), out)
        if info is None:
            print(f"[--] {f.name}: không thấy logo Gemini")
            continue
        done += 1
        print(f"[ok] {f.name}: logo {info['size']}px @({info['x0']},{info['y0']}) corr={info['corr']:.2f} -> {dst}")
    print(f"Xong: {done}/{len(files)} ảnh đã xóa logo.")


if __name__ == "__main__":
    main()
