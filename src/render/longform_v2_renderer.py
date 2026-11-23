"""
Long-form V2 Retention Renderer — Vẽ Chuyện Hoang Dã (16:9, 1920x1080 @ 30fps)
================================================================================
Fixes found in the EP06 retention audit (07/11):
  * one illustration held 19-24 s while the voice moved on  -> one image per idea (6-12 s)
  * no subtitles in the long video                           -> word-synced kinetic captions
  * 10 s branded intro BEFORE the hook                       -> cold-open hook first, intro sting later
  * same draw-then-zoom pattern 22 times                      -> 4 entrance styles + Ken-Burns drift
  * stat facts only spoken                                    -> number stickers + arrow to the exact spot
  * -24 LUFS, true-peak +0.8 dBTP                             -> loudnorm to -14 LUFS / -1.5 dBTP
  * no sense of progress                                      -> chapter progress bar + chapter cards

Layout (1920x1080):
    0 -  128 : chapter header ribbon (fixed, compact) + progress pips
  140 -  860 : stage — ONE illustration at a time (max 1240x700) + side stickers
  880 - 1010 : kinetic caption (active word yellow)
 1040 - 1080 : thin chapter progress bar

Usage:
  python src/render/longform_v2_renderer.py projects/<ep>/specs/longform_v2_spec.json [--preview] [--scene sceneXX]
"""
from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src" / "render"))
import shorts_v4_renderer as sv  # noqa: E402  (shared helpers approved in Shorts V5)

W, H, FPS = 1920, 1080, 30
STAGE_Y0, STAGE_Y1 = 150, 860
STAGE_CX, STAGE_CY = W // 2, (STAGE_Y0 + STAGE_Y1) // 2
BOX_W, BOX_H = 1180, 690
CAPTION_CY = 948
CAPTION_SIZE = 50
HEADER_H = 128

FONT_BOLD = sv.FONT_BOLD
FONT_HAND = sv.FONT_HAND
PALETTE = sv.PALETTE


# ----------------------------------------------------------------------------- paper
def make_paper() -> np.ndarray:
    paper = np.full((H, W, 3), 255, np.uint8)
    rng = np.random.default_rng(11)
    noise = rng.normal(0, 1.1, (H, W, 1))
    paper = np.clip(paper.astype(np.float32) - np.abs(noise), 0, 255).astype(np.uint8)
    for y in range(20, H, 40):
        for x in range(20, W, 40):
            cv2.circle(paper, (x, y), 1, (228, 224, 218), -1, cv2.LINE_AA)
    return paper


# ----------------------------------------------------------------------------- header
def render_header(chapter_no: int, n_chapters: int, title: str, badge: str | None = None) -> np.ndarray:
    """Compact comic ribbon: red chapter badge + navy title bar with gold rim. RGBA(BGR) W x HEADER_H."""
    S = 2
    cw, ch = W * S, HEADER_H * S
    img = Image.new("RGBA", (cw, ch), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    ink, gold = (20, 16, 14, 255), (255, 190, 20, 255)
    f_title = sv.fit_font(FONT_BOLD, title, (1300) * S, 46 * S)
    tw = f_title.getlength(title)
    badge = badge or f"CHƯƠNG {chapter_no}"  # format-specific label, e.g. "BẰNG CHỨNG #1" (docs/strategy)
    f_badge = sv.font(FONT_BOLD, 30 * S)
    bw = f_badge.getlength(badge) + 56 * S
    total = bw + 24 * S + tw + 80 * S
    x0 = (cw - total) / 2
    y0, y1 = 20 * S, 104 * S
    # badge (red, tilted feel via offset shadow)
    d.rounded_rectangle([x0 + 7 * S, y0 + 9 * S, x0 + bw + 7 * S, y1 + 9 * S], 22 * S, fill=(0, 0, 0, 110))
    d.rounded_rectangle([x0, y0, x0 + bw, y1], 22 * S, fill=(217, 56, 30, 255), outline=ink, width=4 * S)
    d.text((x0 + bw / 2, (y0 + y1) / 2), badge, font=f_badge, fill=(255, 255, 255, 255), anchor="mm",
           stroke_width=3 * S, stroke_fill=ink)
    # title bar
    tx0 = x0 + bw + 24 * S
    tx1 = tx0 + tw + 80 * S
    d.rounded_rectangle([tx0 + 7 * S, y0 + 9 * S, tx1 + 7 * S, y1 + 9 * S], 26 * S, fill=(0, 0, 0, 110))
    grad = Image.new("RGBA", (cw, ch))
    gd = ImageDraw.Draw(grad)
    for y in range(y0, y1 + 1):
        u = (y - y0) / (y1 - y0)
        gd.line([(0, y), (cw, y)], fill=(int(38 - 26 * u), int(56 - 36 * u), int(104 - 60 * u), 255))
    m = Image.new("L", (cw, ch), 0)
    ImageDraw.Draw(m).rounded_rectangle([tx0, y0, tx1, y1], 26 * S, fill=255)
    img.paste(grad, (0, 0), m)
    d.rounded_rectangle([tx0, y0, tx1, y1], 26 * S, outline=ink, width=4 * S)
    d.rounded_rectangle([tx0 + 6 * S, y0 + 6 * S, tx1 - 6 * S, y1 - 6 * S], 21 * S, outline=gold, width=4 * S)
    d.text(((tx0 + tx1) / 2, (y0 + y1) / 2 + 2 * S), title, font=f_title, fill=(255, 226, 90, 255), anchor="mm",
           stroke_width=4 * S, stroke_fill=ink)
    # (chapter pips removed per owner request — TASTE-58)
    img = img.resize((W, HEADER_H), Image.LANCZOS)
    return sv.pil_to_rgba_bgr(img)


def load_header_image(path: Path, max_w: int = 1480) -> np.ndarray:
    """AI-drawn chapter header bar (TASTE-62, RGBA cutout from prep_banners.py) centred in W x HEADER_H.
    The bar body is fitted to ~100 px high; decorations may use the rest of the 128 px strip."""
    im = cv2.imread(str(path), cv2.IMREAD_UNCHANGED)
    if im is None or im.shape[2] != 4:
        raise ValueError(f"header_image must be an RGBA cutout: {path}")
    s = min(max_w / im.shape[1], (HEADER_H - 6) / im.shape[0])
    im = cv2.resize(im, None, fx=s, fy=s, interpolation=cv2.INTER_AREA if s < 1 else cv2.INTER_CUBIC)
    layer = np.zeros((HEADER_H, W, 4), np.uint8)
    x0, y0 = (W - im.shape[1]) // 2, (HEADER_H - im.shape[0]) // 2
    layer[y0:y0 + im.shape[0], x0:x0 + im.shape[1]] = im
    return layer

# ----------------------------------------------------------------------------- chapter card
def load_card_image(path: Path, max_w: int = 1460, max_h: int = 740) -> np.ndarray:
    """AI-drawn chapter intro card (TASTE-75, RGBA cutout from prep_banners.py) centred in W x H."""
    im = cv2.imread(str(path), cv2.IMREAD_UNCHANGED)
    if im is None or im.shape[2] != 4:
        raise ValueError(f"card_image must be an RGBA cutout: {path}")
    s = min(max_w / im.shape[1], max_h / im.shape[0])
    im = cv2.resize(im, None, fx=s, fy=s, interpolation=cv2.INTER_AREA if s < 1 else cv2.INTER_CUBIC)
    layer = np.zeros((H, W, 4), np.uint8)
    x0, y0 = (W - im.shape[1]) // 2, (H - im.shape[0]) // 2
    layer[y0:y0 + im.shape[0], x0:x0 + im.shape[1]] = im
    return layer


def render_chapter_card(chapter_no: int, title: str, hook: str, badge: str | None = None,
                        theme: str = "biolab") -> np.ndarray:
    """Full-frame chapter title card (RGBA) used for ~1.6 s at each act start."""
    return sv.te.render_themed_chapter_card(W, H, chapter_no, title, hook, badge=badge, theme=theme)


# ----------------------------------------------------------------------------- caption
def render_caption(words: list[str], active: int, pop: float) -> np.ndarray:
    up = [w.upper() for w in words]
    f = sv.fit_font(FONT_BOLD, " ".join(up), 1500, CAPTION_SIZE, 30)
    img = Image.new("RGBA", (W, 160), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    space = f.getlength(" ")
    total = sum(f.getlength(w) for w in up) + space * (len(up) - 1)
    x = (W - total) / 2
    for i, w in enumerate(up):
        fill = (255, 214, 10) if i == active else ((255, 255, 255) if i < active else (255, 255, 255, 150))
        wf, dy = f, 0
        if i == active and pop < 1.0:
            wf = sv.font(FONT_BOLD, int(f.size * (1.0 + 0.10 * (1 - pop))))
            dy = -4 * (1 - pop)
        d.text((x + f.getlength(w) / 2, 80 + dy), w, font=wf, fill=fill, anchor="mm", stroke_width=6, stroke_fill=(10, 10, 10))
        x += f.getlength(w) + space
    return sv.pil_to_rgba_bgr(img)


def build_caption_groups(words: list[dict], t0: float, t1: float, max_words: int = 5) -> list[dict]:
    """Split Whisper words inside [t0,t1) into 3-5 word groups, breaking on punctuation and pauses."""
    ws = [w for w in words if t0 - 0.05 <= w["s"] < t1 - 0.05 and w["w"] and not (w["w"].startswith("[") and w["w"].endswith("]"))]
    groups, cur = [], []
    for i, w in enumerate(ws):
        cur.append(w)
        gap = (ws[i + 1]["s"] - w["e"]) if i + 1 < len(ws) else 9
        punct = w["w"][-1] in ".,?!:;"
        if len(cur) >= max_words or (punct and len(cur) >= 2) or gap > 0.45:
            groups.append(cur)
            cur = []
    if cur:
        groups.append(cur)
    out = []
    for g in groups:
        out.append({"words": [x["w"].strip(".,?!:;") or x["w"] for x in g], "word_t": [x["s"] for x in g],
                    "t": g[0]["s"], "end": g[-1]["e"] + 0.25})
    for i in range(len(out) - 1):  # no flicker between tight groups
        if out[i + 1]["t"] - out[i]["end"] < 0.3:
            out[i]["end"] = out[i + 1]["t"]
    return out


# ----------------------------------------------------------------------------- renderer
ENTRANCES = ["draw", "draw_fast", "slide", "pop"]


SFX_CACHE: dict[Path, np.ndarray] = {}


def load_audio_pcm(p: Path, target_sr: int = 48000) -> np.ndarray:
    """Load audio file as float32 stereo at target_sr via ffmpeg pipe."""
    if p not in SFX_CACHE:
        cmd = ["ffmpeg", "-v", "error", "-i", str(p), "-ar", str(target_sr), "-ac", "2", "-f", "f32le", "-"]
        raw = subprocess.run(cmd, capture_output=True, check=True).stdout
        SFX_CACHE[p] = np.frombuffer(raw, dtype=np.float32).reshape(-1, 2)
    return SFX_CACHE[p]


def mix_scene_audio(voice_path: Path, beats: list[dict], sfx: list[tuple], dur: float) -> Path:
    """Direct PCM audio mixing in Python: zero CLI limits, handles any number of beats/SFX instantly."""
    sr = 48000
    n_samples = int(dur * sr) + sr
    mix = np.zeros((n_samples, 2), dtype=np.float32)

    # 1. Voice
    voc = load_audio_pcm(voice_path, sr)
    nv = min(len(mix), len(voc))
    mix[:nv] += voc[:nv]

    # 2. Scribble on ink
    scrib = load_audio_pcm(ROOT / "assets/sfx/marker-scribble-loop.wav", sr)
    for b in beats:
        b.setdefault("draw_s", {"draw": 2.4, "draw_fast": 1.5, "slide": 0.0, "pop": 0.0}[b["entrance"]])
        if b["entrance"] in ("draw", "draw_fast"):
            st, d_ = b["start_s"], b["draw_s"]
            d_samples = int(d_ * sr)
            if d_samples > 0:
                repeats = (d_samples // len(scrib)) + 1
                loop = np.tile(scrib, (repeats, 1))[:d_samples].copy()
                fade_samples = int(0.2 * sr)
                if fade_samples > 0 and d_samples > fade_samples:
                    fade = np.linspace(1.0, 0.0, fade_samples, dtype=np.float32)[:, None]
                    loop[-fade_samples:] *= fade
                loop *= 0.22
                idx0 = int(st * sr)
                idx1 = min(len(mix), idx0 + len(loop))
                if idx1 > idx0:
                    mix[idx0:idx1] += loop[:idx1 - idx0]

    # 3. SFX (whoosh, pop, impact)
    for tt, rel_f, vol in sfx:
        clip = load_audio_pcm(ROOT / rel_f, sr) * vol
        idx0 = max(0, int(tt * sr))
        idx1 = min(len(mix), idx0 + len(clip))
        if idx1 > idx0:
            mix[idx0:idx1] += clip[:idx1 - idx0]

    mix = mix[:int(dur * sr)]
    np.clip(mix, -1.0, 1.0, out=mix)
    audio_pcm = (mix * 32767).astype(np.int16)
    audio_tmp = voice_path.with_name(f"{voice_path.stem}_mix.pcm")
    audio_pcm.tofile(str(audio_tmp))
    return audio_tmp


def render_scene(spec: dict, sc: dict, proj: Path, out_mp4: Path, preview: bool = False) -> Path:
    voice = proj / sc["voice"]
    words = json.loads((proj / spec["words"]).read_text(encoding="utf-8"))[sc["id"]]
    dur = float(sc["duration_s"])
    beats = sc["beats"]
    for i, b in enumerate(beats):
        b["end_s"] = beats[i + 1]["start_s"] if i + 1 < len(beats) else dur
        assert b["end_s"] - b["start_s"] <= 15.5, f"{sc['id']}/{b['id']} holds >15 s (TASTE-47)"

    theme, tpal = sv.te.resolve_theme(proj)
    paper = sv.te.decorate_paper(make_paper(), theme)
    hand = sv.Hand(1.0)
    hi = sc.get("header_image")
    header = load_header_image(proj / hi) if hi and (proj / hi).exists() else \
        render_header(sc["chapter_no"], spec["n_chapters"], sc["title"], sc.get("badge"))
    ci = sc.get("card_image") or f"assets/banners/card_{sc['chapter_no']:02d}.png"
    if (proj / ci).exists():
        card = load_card_image(proj / ci)
    elif sc.get("chapter_card", True):
        card = render_chapter_card(sc["chapter_no"], sc["title"], sc.get("card_hook", ""), sc.get("badge"), theme=theme)
    else:
        card = None
    card_dur = float(sc.get("card_s", 1.6)) if card is not None else 0.0

    print(f"[{sc['id']}] preparing {len(beats)} illustrations (theme={theme}) ...")
    ch_offset = int(sc.get("chapter_no", 1))
    for k, b in enumerate(beats):
        b["ill"] = sv.Illustration(proj / b["image"], BOX_W, BOX_H)
        b.setdefault("entrance", ENTRANCES[k % len(ENTRANCES)] if k else "draw")
        b.setdefault("draw_s", {"draw": 2.4, "draw_fast": 1.5, "slide": 0.0, "pop": 0.0}[b["entrance"]])
        for j, s in enumerate(b.get("stickers", [])):
            col = tpal[(ch_offset + k + j) % len(tpal)]
            s["img"] = sv.render_sticker(s["value"], s["label"], col, 340, theme=theme, variant=ch_offset + k + j)
            s["col_bgr"] = (col[2], col[1], col[0])
            s["rot"] = (-3 if s["side"] == "L" else 3) * (1 if j % 2 == 0 else -0.6)

    caps = build_caption_groups(words, 0.0, dur + 1)
    cap_cache: dict = {}

    n_frames = int(round(dur * FPS))
    frames = range(n_frames)
    if preview:
        def _pt(b):
            last = max([s["t"] + 1.2 for s in b.get("stickers", [])] + [b["start_s"] + b["draw_s"] + 1.0])
            return min(b["end_s"] - 0.3, last)
        frames = [int(min(dur - 0.1, _pt(b)) * FPS) for b in beats]

    tmp = out_mp4.with_name(out_mp4.stem + "_video.mp4")
    pipe = None
    if not preview:
        pipe = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "bgr24",
                                 "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium",
                                 "-crf", "18", "-pix_fmt", "yuv420p", str(tmp)], stdin=subprocess.PIPE)

    yy_, xx_ = np.mgrid[0:header.shape[0], 0:header.shape[1]]
    hdr_xy = (xx_ + 0.55 * yy_).astype(np.float32)
    hdr_body = (header[:, :, 3].astype(np.float32) / 255.0)
    snaps = []
    for fi in frames:
        t = fi / FPS
        b = next((x for x in beats if x["start_s"] <= t < x["end_s"]), beats[-1])
        ill = b["ill"]
        el = t - b["start_s"]
        bdur = b["end_s"] - b["start_s"]
        canvas = paper.copy()
        ent, draw_s = b["entrance"], b["draw_s"]

        exit_u = 0.0
        if b is not beats[-1] and el > bdur - 0.22:
            exit_u = sv.ease_out_cubic((el - (bdur - 0.22)) / 0.22)
        pen = None
        sx = sy = 1.0
        rot, bob, dx_ent = 0.0, 0.0, 0.0
        layer = ill.color
        if ent in ("draw", "draw_fast") and el < draw_s:
            n = max(1, int(len(ill.path) * (el / draw_s)))
            layer = ill.ink_reveal(n)
            pen = ill.path[n - 1]
        else:
            pu = el - draw_s
            if ent in ("draw", "draw_fast") and pu < 0.30:
                k = sv.ease_out_cubic(pu / 0.30)
                inkl = ill.ink_reveal(len(ill.path))
                layer = ill.color.copy()
                layer[:, :, 3] = (ill.color[:, :, 3] * k + inkl[:, :, 3] * (1 - k)).astype(np.uint8)
                layer[:, :, :3] = (ill.color[:, :, :3] * k + inkl[:, :, :3] * (1 - k)).astype(np.uint8)
            if ent == "slide":
                dx_ent = (1 - sv.ease_out_cubic(pu / 0.45)) * W * 0.6 if pu < 0.45 else 0.0
            if ent == "pop":
                s_ = sv.spring(pu, 13.0, 0.5)
                sx = sy = max(0.05, s_)
            jelly = math.exp(-5.0 * pu) * math.sin(2 * math.pi * 2.6 * pu) if ent != "pop" else 0.0
            sx, sy = sx * (1.0 + 0.035 * jelly), sy * (1.0 - 0.035 * jelly)
            ramp = min(1.0, pu / 0.8)
            bob = 5.0 * math.sin(2 * math.pi * pu / 2.6) * ramp
            # slow Ken-Burns drift (alternating direction) keeps long holds alive
            kb = min(1.0, pu / max(1.0, bdur - draw_s))
            drift = 1.0 + 0.035 * kb
            sx, sy = sx * drift, sy * drift
            rot = 0.6 * math.sin(2 * math.pi * pu / 3.4) * ramp
            sh_t = pu - 0.35
            if 0.0 <= sh_t <= 0.8:
                if not hasattr(ill, "xy"):
                    a_, b_ = np.mgrid[0:ill.h, 0:ill.w]
                    ill.xy = (b_ + 0.55 * a_).astype(np.float32)
                span = ill.w + 0.55 * ill.h
                band = sv.shine_band(ill.xy, -140 + (span + 280) * sv.ease_out_cubic(sh_t / 0.8), 46.0) * 0.5
                band *= layer[:, :, 3].astype(np.float32) / 255.0
                layer = layer.copy()
                layer[:, :, :3] = np.clip(layer[:, :, :3] + band[:, :, None] * 255, 0, 255).astype(np.uint8)

        lh, lw = layer.shape[:2]
        A = None
        if sx != 1.0 or sy != 1.0 or rot != 0.0:
            a = math.radians(rot)
            A = np.array([[sx * math.cos(a), sx * math.sin(a)], [-sy * math.sin(a), sy * math.cos(a)]], np.float32)
            P = np.array([lw / 2, lh / 2], np.float32)
            M = np.hstack([A, (P - A @ P).reshape(2, 1)]).astype(np.float32)
            xf = lambda im: cv2.warpAffine(im, M, (lw, lh), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT,
                                           borderValue=(0, 0, 0, 0))
            layer_s, shadow_s = xf(layer), xf(ill.shadow)
        else:
            layer_s, shadow_s = layer, ill.shadow
        x0 = int(STAGE_CX - lw // 2 + dx_ent)
        y0 = int(STAGE_CY - lh // 2 - 140 * exit_u + bob)
        op = 1.0 - exit_u

        def to_screen(lx, ly):
            if A is None:
                return x0 + lx, y0 + ly
            v = A @ (np.array([lx, ly], np.float32) - np.array([lw / 2, lh / 2], np.float32)) + np.array([lw / 2, lh / 2])
            return x0 + float(v[0]), y0 + float(v[1])

        if pen is None:
            sv.alpha_paste(canvas, shadow_s, x0 + 10, y0 + 16, op)
        sv.alpha_paste(canvas, layer_s, x0, y0, op)

        # stickers + arrows to the exact feature
        for s in b.get("stickers", []):
            if t < s["t"]:
                continue
            k = sv.spring(t - s["t"], 15.0, 0.5)
            img = s["img"]
            M2 = cv2.getRotationMatrix2D((img.shape[1] / 2, img.shape[0] / 2), s["rot"], max(0.05, k))
            rimg = cv2.warpAffine(img, M2, (img.shape[1], img.shape[0]), flags=cv2.INTER_LINEAR,
                                  borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0, 0))
            cx = 205 if s["side"] == "L" else W - 205
            sy_ = s.get("y", 420)
            ap = (t - s["t"] - 0.18) / 0.40
            if ap > 0 and "target" in s:
                lx, ly = ill.local(*s["target"])
                p1 = to_screen(lx, ly)
                half = img.shape[1] / 2 - 26
                p0 = (cx + half, sy_ + 18) if s["side"] == "L" else (cx - half, sy_ + 18)
                sv.draw_target_arrow(canvas, p0, p1, min(1.0, ap), s["col_bgr"], s.get("bend", -0.2 if s["side"] == "L" else 0.2), op, theme=theme, t=t - s["t"])
                if ap >= 1.0:
                    sv.draw_target_ring(canvas, p1, t - s["t"], s["col_bgr"], op, theme=theme)
            sv.alpha_paste(canvas, rimg, int(cx - img.shape[1] / 2), int(sy_ - img.shape[0] / 2), op)

        # hand
        if pen is not None:
            hand.stamp(canvas, x0 + pen[0] + 2.0 * math.sin(t * 40), y0 + pen[1] + 1.5 * math.cos(t * 33))
        elif ent in ("draw", "draw_fast") and el - draw_s < 0.35:
            u = sv.ease_out_cubic((el - draw_s) / 0.35)
            last = ill.path[-1]
            hand.stamp(canvas, x0 + last[0] + 600 * u, y0 + last[1] + 700 * u)

        # header with periodic shine
        cyc = t % 6.0
        if cyc < 0.9:
            band = sv.shine_band(hdr_xy, -150 + (W + 300) * sv.ease_out_cubic(cyc / 0.9), 34.0) * 0.4 * hdr_body
            hl = header.copy()
            hl[:, :, :3] = np.clip(hl[:, :, :3] + band[:, :, None] * 255, 0, 255).astype(np.uint8)
            sv.alpha_paste(canvas, hl, 0, 0)
        else:
            sv.alpha_paste(canvas, header, 0, 0)

        # caption
        cap = next((c for c in caps if c["t"] <= t < c["end"]), None)
        if cap is not None:
            active = max(j for j, wt in enumerate(cap["word_t"]) if wt <= t) if t >= cap["word_t"][0] else 0
            pop = min(1.0, (t - cap["word_t"][active]) / 0.14)
            key = (id(cap), active, round(pop, 1))
            if key not in cap_cache:
                if len(cap_cache) > 400:
                    cap_cache.clear()
                cap_cache[key] = render_caption(cap["words"], active, pop)
            sv.alpha_paste(canvas, cap_cache[key], 0, CAPTION_CY - 80)

        # chapter card overlay (fades out over the first beat while the voice already runs)
        if card is not None and t < card_dur:
            a_ = 1.0 if t < card_dur - 0.35 else (card_dur - t) / 0.35
            sc_ = 0.92 + 0.08 * sv.ease_out_cubic(t / 0.35)
            veil = canvas.copy()
            cv2.rectangle(veil, (0, 0), (W, H), (241, 246, 248), -1)
            cv2.addWeighted(veil, 0.88 * a_, canvas, 1 - 0.88 * a_, 0, dst=canvas)
            Mc = cv2.getRotationMatrix2D((W / 2, H / 2), 0, sc_)
            cimg = cv2.warpAffine(card, Mc, (W, H), borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0, 0))
            sv.alpha_paste(canvas, cimg, 0, 0, a_)

        if preview:
            snaps.append((t, canvas))
        else:
            pipe.stdin.write(canvas.tobytes())
            if fi % 300 == 0:
                print(f"  [{sc['id']}] frame {fi}/{n_frames}")

    if preview:
        d = out_mp4.parent / "snapshots_long_v2"
        d.mkdir(exist_ok=True)
        th = [cv2.putText(cv2.resize(c, (640, 360)), f"{sc['id']} {t:.1f}s", (10, 30), 0, 0.8, (0, 0, 255), 2) for t, c in snaps]
        while len(th) % 3:
            th.append(np.full_like(th[0], 255))
        cv2.imwrite(str(d / f"{sc['id']}_sheet.jpg"), np.vstack([np.hstack(th[i:i + 3]) for i in range(0, len(th), 3)]))
        for k, (t, c) in enumerate(snaps):
            cv2.imwrite(str(d / f"{sc['id']}_{k + 1:02d}.jpg"), c)
        print("preview ->", d / f"{sc['id']}_sheet.jpg")
        return d

    pipe.stdin.close()
    pipe.wait()

    # ---- audio: voice + SFX (whoosh per beat, pop per colour/sticker, scribble on ink) ; BGM added at master
    sfx = []
    if card is not None:
        sfx.append((0.0, "assets/sfx/pixabay/whoosh-cinematic.mp3", 0.5))
    for i, b in enumerate(beats):
        if i > 0:
            sfx.append((b["start_s"] - 0.12, "assets/sfx/pixabay/whoosh-short.mp3", 0.45))
        sfx.append((b["start_s"] + b["draw_s"], "assets/sfx/pixabay/pop.mp3", 0.5))
        for s in b.get("stickers", []):
            sfx.append((s["t"], "assets/sfx/pixabay/pop.mp3", 0.32))
        for imp in b.get("impacts", []):
            sfx.append((imp, "assets/sfx/pixabay/impact-bass-1.mp3", 0.45))

    audio_pcm = mix_scene_audio(voice, beats, sfx, dur)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error",
                    "-i", str(tmp),
                    "-f", "s16le", "-ar", "48000", "-ac", "2", "-i", str(audio_pcm),
                    "-map", "0:v", "-map", "1:a",
                    "-c:v", "copy", "-c:a", "pcm_s16le", "-t", f"{dur:.3f}",
                    str(out_mp4.with_suffix(".mkv"))], check=True)
    audio_pcm.unlink(missing_ok=True)
    tmp.unlink(missing_ok=True)
    print("scene done:", out_mp4.with_suffix(".mkv"))
    return out_mp4.with_suffix(".mkv")


def master(spec: dict, proj: Path, scene_files: list[Path]) -> Path:
    """Concat scenes, add ducked BGM, loudnorm to -14 LUFS, splice branded intro after the cold-open hook."""
    out = proj / spec["output"]
    lst = out.with_name("long_v2_concat.txt")
    lst.write_text("\n".join(f"file '{p.resolve().as_posix()}'" for p in scene_files), encoding="utf-8")
    body = out.with_name("long_v2_body.mkv")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(body)], check=True)
    bgm = proj / "audio" / "bgm_seamless_10m.wav" if (proj / "audio" / "bgm_seamless_10m.wav").exists() else ROOT / spec["bgm"]
    body_mix = out.with_name("long_v2_body_mix.mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(body), "-stream_loop", "-1", "-i", str(bgm),
                    "-filter_complex",
                    "[0:a]asplit=2[a][sc];[1:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,volume=0.09[bg];"
                    "[bg][sc]sidechaincompress=threshold=0.06:ratio=3.5:attack=30:release=800[bgd];"
                    "[a][bgd]amix=inputs=2:duration=first:normalize=0,volume=1.12,alimiter=limit=0.75:attack=5:release=50:asc=1:level=0[ao]",
                    "-map", "0:v", "-map", "[ao]", "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-ar", "48000",
                    "-video_track_timescale", "15360", str(body_mix)], check=True)

    # branded intro/outro scaled to 1920x1080@30, loudness matched
    def norm_clip(src: Path, dst: Path):
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(src), "-vf", "scale=1920:1080:flags=lanczos,fps=30,format=yuv420p",
                        "-af", "aformat=sample_rates=48000:channel_layouts=stereo,loudnorm=I=-16:TP=-2.0",
                        "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-c:a", "aac", "-b:a", "256k", "-ar", "48000",
                        "-video_track_timescale", "15360", str(dst)], check=True)
        return dst
    intro = norm_clip(ROOT / spec["intro"], out.with_name("long_v2_intro.mp4"))
    outro = norm_clip(ROOT / spec["outro"], out.with_name("long_v2_outro.mp4"))
    hook = rest = sting = out.with_name("long_v2_unused.mp4")
    if spec.get("intro_mode", "full_first") == "full_first":
        # owner choice (TASTE-58): full original intro first, then the episode opening
        parts = [intro, body_mix, outro]
    else:
        cold = float(spec["cold_open_s"])
        hook = out.with_name("long_v2_hook.mp4")
        rest = out.with_name("long_v2_rest.mp4")
        enc = ["-c:v", "libx264", "-crf", "18", "-preset", "medium", "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-video_track_timescale", "15360"]
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(body_mix), "-t", f"{cold:.3f}"] + enc + [str(hook)], check=True)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{cold:.3f}", "-i", str(body_mix)] + enc + [str(rest)], check=True)
        sting = out.with_name("long_v2_sting.mp4")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(intro), "-t", str(spec.get("intro_sting_s", 4.0)),
                        "-af", f"afade=t=out:st={spec.get('intro_sting_s', 4.0) - 0.5}:d=0.5"] + enc + [str(sting)], check=True)
        parts = [hook, sting, rest, outro]
    lst2 = out.with_name("long_v2_final_concat.txt")
    lst2.write_text("\n".join(f"file '{p.resolve().as_posix()}'" for p in parts), encoding="utf-8")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst2), "-c", "copy",
                    "-movflags", "+faststart", str(out)], check=True)
    for p in [body, body_mix, intro, outro, hook, rest, sting, lst, lst2]:
        Path(p).unlink(missing_ok=True)
    print("MASTER:", out)
    return out


def main():
    spec_p = Path(sys.argv[1]).resolve()
    spec = json.loads(spec_p.read_text(encoding="utf-8"))
    proj = spec_p.parents[1]
    preview = "--preview" in sys.argv
    only = sys.argv[sys.argv.index("--scene") + 1] if "--scene" in sys.argv else None
    rdir = proj / "renders" / "long_v2"
    rdir.mkdir(parents=True, exist_ok=True)
    files = []
    for sc in spec["scenes"]:
        if only and sc["id"] != only:
            continue
        out = rdir / f"{sc['id']}.mp4"
        if not preview and out.with_suffix(".mkv").exists() and "--force" not in sys.argv and not only:
            files.append(out.with_suffix(".mkv"))
            continue
        files.append(render_scene(spec, sc, proj, out, preview))
    if not preview and not only:
        master(spec, proj, files)


if __name__ == "__main__":
    main()
