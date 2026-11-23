"""
Shorts Video Renderer V5 — Episode 3: Cá Heo (Dolphin) Viral Channel Funnel Edition (9:16 Infinite Vertical Sketchbook)
- Native 1080x1920 Full HD Vertical (9:16) on Pure White (#FFFFFF) Infinite Paper
- 3 Vertical Sketchbook Pages x 2 Large Uncropped Visual Beats = 6 High-Retention Beats
- 1-to-1 Millisecond Sync with ElevenLabs Adam Emotional Voiceover (`shorts.wav`, ~47.5s)
- 100% True Character-by-Character Hand-Drawn Captions with Real Hand Rig & Marker SFX
- Smooth Vertical Infinite Canvas Scroll between Pages 1 -> 2 -> 3
- Psychological Open-Loop Cliffhanger + Pulsing Channel Funnel CTA Bar
"""

import sys
import json
import math
import time
import subprocess
from pathlib import Path
from typing import List, Dict, Tuple, Optional
import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont

SCRIPT_DIR = Path(__file__).resolve().parent
PROJ = SCRIPT_DIR.parent
ROOT = PROJ.parent.parent
G = PROJ / "assets" / "gemini_downloaded"
AUDIO_DIR = PROJ / "audio"
SFX_DIR = ROOT / "assets" / "sfx"
SCRIBBLE_WAV = SFX_DIR / "marker-scribble-loop.wav"
BGM_WAV = ROOT / "assets" / "bgm" / "calm-acoustic.wav"
RENDERS_DIR = PROJ / "renders"
RENDERS_DIR.mkdir(parents=True, exist_ok=True)


def remotion_spring(t: float, duration: float = 0.40, omega: float = 16.0, zeta: float = 0.80) -> float:
    if t <= 0.0:
        return 0.0
    if t >= duration:
        return 1.0
    u = t / duration
    wd = omega * math.sqrt(max(0.001, 1.0 - zeta * zeta))
    decay = math.exp(-zeta * omega * u)
    osc = math.cos(wd * u) + (zeta / math.sqrt(max(0.001, 1.0 - zeta * zeta))) * math.sin(wd * u)
    return max(0.0, min(1.05, 1.0 - decay * osc))


def ease_in_out_cubic(u: float) -> float:
    u = max(0.0, min(1.0, u))
    return 4 * u * u * u if u < 0.5 else 1 - pow(-2 * u + 2, 3) / 2


# Fonts
FONT_DIR = ROOT / "assets" / "fonts"
font_header_main = ImageFont.truetype(str(FONT_DIR / "Mali-Bold.ttf"), 38)
font_header_sub = ImageFont.truetype(str(FONT_DIR / "BeVietnamPro-Bold.ttf"), 21)
font_badge = ImageFont.truetype(str(FONT_DIR / "BeVietnamPro-Bold.ttf"), 25)
font_hand = ImageFont.truetype(str(FONT_DIR / "PlaypenSans-Bold.ttf"), 31)
font_cta_main = ImageFont.truetype(str(FONT_DIR / "BeVietnamPro-Bold.ttf"), 28)
font_cta_sub = ImageFont.truetype(str(FONT_DIR / "BeVietnamPro-SemiBold.ttf"), 21)


def fit_contain(im: Image.Image, max_w: int, max_h: int) -> Image.Image:
    w, h = im.size
    scale = min(max_w / w, max_h / h)
    return im.resize(
        (max(1, int(round(w * scale))), max(1, int(round(h * scale)))),
        Image.Resampling.LANCZOS,
    )


class CharGlyph:
    def __init__(
        self,
        ch: str,
        x: int,
        y: int,
        w: int,
        h: int,
        font: ImageFont.FreeTypeFont,
        color: Tuple[int, int, int],
    ):
        self.char = ch
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.font = font
        self.color = color
        self.pen_target = (x + int(w * 0.72), y + int(h * 0.72))


class WritingLine:
    def __init__(self, glyphs: List[CharGlyph], start_ms: float, end_ms: float):
        self.glyphs = glyphs
        self.start_ms = start_ms
        self.end_ms = end_ms
        self.dur_ms = max(1.0, end_ms - start_ms)


def master_shorts_audio() -> Tuple[Path, List[float]]:
    """
    Masters the 5 ElevenLabs emotional voiceover paragraphs (`shorts_eleven_p0..p4.mp3`)
    with silence trimming + 0.95x natural pacing + 1.0s tail hold so total duration lands ~47.5s
    (strictly inside the 45s-58s YouTube Shorts viral loop window) and splits p2 into 2 visual beats (6 beats total).
    """
    part_mp3s = [AUDIO_DIR / f"shorts_eleven_p{i}.mp3" for i in range(5)]
    if not all(p.exists() for p in part_mp3s):
        raise FileNotFoundError("Missing shorts_eleven_p0..p4.mp3! Run elevenlabs_emotional_tts.py shorts first.")

    fast_wavs = []
    raw_durs = []
    for i, src in enumerate(part_mp3s):
        dst = AUDIO_DIR / f"shorts_fast_p{i}.wav"
        cmd = [
            "ffmpeg", "-y", "-i", str(src),
            "-filter:a",
            "silenceremove=start_periods=1:start_silence=0.04:start_threshold=-45dB,"
            "areverse,silenceremove=start_periods=1:start_silence=0.06:start_threshold=-45dB,areverse,"
            "atempo=0.95,volume=1.18",
            "-ar", "48000", "-ac", "2",
            str(dst),
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        dur = float(
            subprocess.check_output(
                [
                    "ffprobe", "-v", "error",
                    "-show_entries", "format=duration",
                    "-of", "default=noprint_wrappers=1:nokey=1",
                    str(dst),
                ],
                text=True,
            ).strip()
        )
        raw_durs.append(round(dur, 3))
        fast_wavs.append(dst)

    gap_s = 0.12
    pause_wav = AUDIO_DIR / "shorts_gap_120ms.wav"
    subprocess.run(
        [
            "ffmpeg", "-y",
            "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
            "-t", str(gap_s),
            "-c:a", "pcm_s16le",
            str(pause_wav),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    tail_wav = AUDIO_DIR / "shorts_tail_1000ms.wav"
    subprocess.run(
        [
            "ffmpeg", "-y",
            "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
            "-t", "1.00",
            "-c:a", "pcm_s16le",
            str(tail_wav),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    concat_txt = AUDIO_DIR / "shorts_fast_concat.txt"
    lines = []
    for idx, fw in enumerate(fast_wavs):
        lines.append(f"file '{fw.resolve().as_posix()}'")
        if idx < len(fast_wavs) - 1:
            lines.append(f"file '{pause_wav.resolve().as_posix()}'")
    lines.append(f"file '{tail_wav.resolve().as_posix()}'")
    concat_txt.write_text("\n".join(lines), encoding="utf-8")

    out_wav = AUDIO_DIR / "shorts.wav"
    subprocess.run(
        [
            "ffmpeg", "-y",
            "-f", "concat", "-safe", "0",
            "-i", str(concat_txt),
            "-c:a", "pcm_s16le",
            "-ar", "48000", "-ac", "2",
            str(out_wav),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    # Map 5 paragraphs into 6 visual beats (splitting p2 into 2 beats + adding 1.0s tail to last beat)
    d2_a = round(raw_durs[2] * 0.50, 3)
    d2_b = round(raw_durs[2] - d2_a, 3)
    beat_durs = [
        raw_durs[0],
        raw_durs[1],
        d2_a,
        d2_b,
        raw_durs[3],
        round(raw_durs[4] + 1.0, 3),
    ]
    (AUDIO_DIR / "shorts_parts_duration.json").write_text(json.dumps(beat_durs, indent=2), encoding="utf-8")
    return out_wav, beat_durs


class ShortsV4Renderer:
    def __init__(self, fps: int = 30):
        self.w = 1080
        self.h = 1920
        self.fps = fps

        hand_png = ROOT / "assets" / "hands" / "hand-marker-right.png"
        raw_hand = cv2.imread(str(hand_png), cv2.IMREAD_UNCHANGED)
        scale = 0.78
        new_w = int(round(raw_hand.shape[1] * scale))
        new_h = int(round(raw_hand.shape[0] * scale))
        resized = cv2.resize(raw_hand, (new_w, new_h), interpolation=cv2.INTER_LANCZOS4)
        self.hand_bgr = resized[:, :, :3]
        self.hand_alpha = (resized[:, :, 3] / 255.0)[:, :, np.newaxis]
        self.hand_w = new_w
        self.hand_h = new_h
        self.anchor_x = int(round(22 * scale))
        self.anchor_y = int(round(47 * scale))

    def _stamp_hand(self, canvas: np.ndarray, pen_x: int, pen_y: int) -> np.ndarray:
        top_x = int(pen_x - self.anchor_x)
        top_y = int(pen_y - self.anchor_y)

        c_x0 = max(0, top_x)
        c_y0 = max(0, top_y)
        c_x1 = min(self.w, top_x + self.hand_w)
        c_y1 = min(self.h, top_y + self.hand_h)

        if c_x1 <= c_x0 or c_y1 <= c_y0:
            return canvas

        h_x0 = c_x0 - top_x
        h_y0 = c_y0 - top_y
        h_x1 = h_x0 + (c_x1 - c_x0)
        h_y1 = h_y0 + (c_y1 - c_y0)

        out = canvas.copy()
        hb = self.hand_bgr[h_y0:h_y1, h_x0:h_x1]
        ha = self.hand_alpha[h_y0:h_y1, h_x0:h_x1]
        out[c_y0:c_y1, c_x0:c_x1] = (out[c_y0:c_y1, c_x0:c_x1] * (1.0 - ha) + hb * ha).astype(np.uint8)
        return out

    def _layout_centered_line(
        self,
        text: str,
        center_x: int,
        y: int,
        font: ImageFont.FreeTypeFont,
        color: Tuple[int, int, int],
        start_ms: float,
        end_ms: float,
    ) -> Tuple[WritingLine, Tuple[int, int, int, int]]:
        dummy = Image.new("RGB", (10, 10))
        d = ImageDraw.Draw(dummy)
        tb = d.textbbox((0, 0), text, font=font)
        total_w = tb[2] - tb[0]
        cur_x = center_x - total_w // 2

        glyphs: List[CharGlyph] = []
        for ch in text:
            cb = d.textbbox((0, 0), ch, font=font)
            cw = max(8, cb[2] - cb[0])
            ch_h = max(20, cb[3] - cb[1])
            if ch != " ":
                glyphs.append(CharGlyph(ch, cur_x, y, cw, ch_h, font, color))
            adv = d.textlength(ch, font=font)
            cur_x += int(round(adv))

        bbox = (center_x - total_w // 2 - 14, y + tb[1] - 4, center_x + total_w // 2 + 14, y + tb[3] + 6)
        return WritingLine(glyphs, start_ms, end_ms), bbox

    def build_pages_and_beats(self, part_durs: List[float]):
        gaps = [0.12, 0.12, 0.0, 0.12, 0.12, 0.0]
        beat_starts_ms = []
        beat_ends_ms = []
        cur_t = 0.0
        for idx, d in enumerate(part_durs):
            st_ms = int(round(cur_t * 1000))
            en_ms = int(round((cur_t + d) * 1000))
            beat_starts_ms.append(st_ms)
            beat_ends_ms.append(en_ms)
            cur_t += d + gaps[idx]

        total_ms = beat_ends_ms[-1]

        pages_meta = [
            {
                "page_idx": 0,
                "header_title": "CÚ LỪA NỤ CƯỜI CỦA CÁ HEO!",
                "header_sub": "BỘ NÃO LỚN THỨ 2 HÀNH TINH & TÊN RIÊNG",
                "header_accent": (214, 40, 40),
                "beats": [
                    {
                        "beat_idx": 0,
                        "slot": "upper",
                        "img": G / "c1_permanent_smile_jaw_anatomy.png",
                        "badge": "BÍ MẬT NỤ CƯỜI HOẠT HÌNH",
                        "badge_bg": (214, 40, 40),
                        "hl_color": (254, 240, 138),
                        "lines": [
                            "Đừng để nụ cười ngọt ngào đánh lừa:",
                            "Đó là khung xương hàm uốn cong cố định!",
                        ],
                    },
                    {
                        "beat_idx": 1,
                        "slot": "lower",
                        "img": G / "c2_dolphin_mirror_selfie_iq.png",
                        "badge": "SỰ THẬT 1: SIÊU TRÍ TUỆ IQ 99",
                        "badge_bg": (43, 108, 176),
                        "hl_color": (191, 219, 254),
                        "lines": [
                            "Não lớn thứ 2 hành tinh biết tự soi gương",
                            "và đặt tên riêng bằng tiếng huýt sáo!",
                        ],
                    },
                ],
            },
            {
                "page_idx": 1,
                "header_title": "NGỦ MỞ 1 MẮT & BÓNG CHUYỀN CÁ NÓC!",
                "header_sub": "TUYỆT KỸ SINH TỒN & TRÒ CHƠI SIÊU LẦY LỘI",
                "header_accent": (43, 108, 176),
                "beats": [
                    {
                        "beat_idx": 2,
                        "slot": "upper",
                        "img": G / "c3_half_brain_sleep_elevator.png",
                        "badge": "SỰ THẬT 2: NGỦ TỪNG NỬA BỘ NÃO",
                        "badge_bg": (107, 70, 193),
                        "hl_color": (233, 213, 255),
                        "lines": [
                            "Tắt đèn đi ngủ từng nửa bộ não:",
                            "Một mắt ngủ, một mắt mở canh cá mập!",
                        ],
                    },
                    {
                        "beat_idx": 3,
                        "slot": "lower",
                        "img": G / "c4_dolphin_pufferfish_volleyball_game.png",
                        "badge": "BÓNG CHUYỀN CÁ NÓC & HÚC CÁ MẬP",
                        "badge_bg": (192, 86, 33),
                        "hl_color": (254, 215, 170),
                        "lines": [
                            "Chuyền bóng chuyền bằng chú Cá Nóc",
                            "và hóa ngư lôi húc văng Cá Mập Trắng!",
                        ],
                    },
                ],
            },
            {
                "page_idx": 2,
                "header_title": "KÍNH X-QUANG & GĂNG TAY BỌT BIỂN!",
                "header_sub": "KHÁM PHÁ TRỌN BỘ TẬP 3 TRÊN KÊNH",
                "header_accent": (185, 28, 28),
                "beats": [
                    {
                        "beat_idx": 4,
                        "slot": "upper",
                        "img": G / "c2_dolphin_xray_sonar_vision.png",
                        "badge": "SỰ THẬT 3: RA-ĐA X-QUANG ĐÁY BIỂN",
                        "badge_bg": (47, 133, 90),
                        "hl_color": (187, 247, 208),
                        "lines": [
                            "Phát sóng siêu âm nhìn xuyên lớp cát",
                            "và đeo bọt biển làm găng tay bảo hộ!",
                        ],
                    },
                    {
                        "beat_idx": 5,
                        "slot": "lower",
                        "img": G / "c5_rostrum_torpedo_belly_bump.png",
                        "badge": "XEM NGAY BẢN FULL TẬP 3: CÁ HEO!",
                        "badge_bg": (214, 40, 40),
                        "hl_color": (254, 240, 138),
                        "lines": [
                            "Vì sao Cá Mập Trắng sợ biệt đội Cá Heo?",
                            "Bấm vào kênh xem ngay bản Full Tập 3!",
                        ],
                    },
                ],
            },
        ]

        pages_rendered = []
        for pm in pages_meta:
            page_pil = Image.new("RGB", (self.w, self.h), (255, 255, 255))
            draw_p = ImageDraw.Draw(page_pil)

            hb = [32, 26, 1048, 156]
            acc = pm["header_accent"]
            draw_p.rounded_rectangle([hb[0] + 5, hb[1] + 5, hb[2] + 5, hb[3] + 5], radius=22, fill=(30, 41, 59))
            draw_p.rounded_rectangle(hb, radius=22, fill=(254, 249, 195), outline=(30, 41, 59), width=4)
            draw_p.text((540, 72), pm["header_title"], fill=acc, font=font_header_main, anchor="mm")
            draw_p.text((540, 124), pm["header_sub"], fill=(30, 41, 59), font=font_header_sub, anchor="mm")

            for dx in range(60, 1020, 28):
                draw_p.line([(dx, 952), (dx + 14, 952)], fill=(203, 213, 225), width=2)

            beat_objs = []
            for bm in pm["beats"]:
                b_idx = bm["beat_idx"]
                st_ms = beat_starts_ms[b_idx]
                en_ms = beat_ends_ms[b_idx]

                if bm["slot"] == "upper":
                    zone_y0, zone_y1 = 170, 940
                else:
                    zone_y0, zone_y1 = 964, 1734

                art_max_w, art_max_h = 980, 560
                raw_im = Image.open(bm["img"]).convert("RGB")
                fit_im = fit_contain(raw_im, art_max_w, art_max_h)
                ix0 = (self.w - fit_im.width) // 2
                iy0 = zone_y0 + (565 - fit_im.height) // 2
                page_pil.paste(fit_im, (ix0, iy0))

                badge_cy = zone_y0 + 598
                tb_badge = draw_p.textbbox((0, 0), bm["badge"], font=font_badge)
                bw = (tb_badge[2] - tb_badge[0]) + 56
                bh = 46
                bx0 = 540 - bw // 2
                by0 = badge_cy - bh // 2
                bx1 = bx0 + bw
                by1 = by0 + bh
                draw_p.rounded_rectangle([bx0 + 4, by0 + 4, bx1 + 4, by1 + 4], radius=23, fill=(30, 41, 59))
                draw_p.rounded_rectangle([bx0, by0, bx1, by1], radius=23, fill=bm["badge_bg"], outline=(30, 41, 59), width=3)
                draw_p.text((540, badge_cy), bm["badge"], fill=(255, 255, 255), font=font_badge, anchor="mm")

                l1_y = zone_y0 + 634
                l2_y = zone_y0 + 684
                write_start = st_ms + 380
                write_avail = max(1200, min(4200, int((en_ms - st_ms) * 0.58)))
                l1_end = write_start + int(write_avail * 0.50)
                l2_start = l1_end + 80
                l2_end = write_start + write_avail

                wl1, bbox1 = self._layout_centered_line(
                    bm["lines"][0], 540, l1_y, font_hand, (20, 28, 40), write_start, l1_end
                )
                wl2, bbox2 = self._layout_centered_line(
                    bm["lines"][1], 540, l2_y, font_hand, (185, 28, 28), l2_start, l2_end
                )

                beat_objs.append(
                    {
                        "beat_idx": b_idx,
                        "slot": bm["slot"],
                        "zone_box": (20, zone_y0, 1060, zone_y1),
                        "art_box": (20, zone_y0, 1060, zone_y0 + 626),
                        "start_ms": st_ms,
                        "end_ms": en_ms,
                        "lines": [wl1, wl2],
                        "hl_bbox": bbox2,
                        "hl_color": bm["hl_color"],
                    }
                )

            page_bgr = cv2.cvtColor(np.array(page_pil), cv2.COLOR_RGB2BGR)
            pages_rendered.append(
                {
                    "page_idx": pm["page_idx"],
                    "start_ms": beat_starts_ms[pm["beats"][0]["beat_idx"]],
                    "end_ms": beat_ends_ms[pm["beats"][-1]["beat_idx"]],
                    "base_bgr": page_bgr,
                    "beats": beat_objs,
                }
            )

        return pages_rendered, total_ms

    def _render_single_page_state(
        self, page: dict, cur_ms: float
    ) -> Tuple[np.ndarray, Optional[Tuple[int, int]]]:
        canvas = np.full((self.h, self.w, 3), 255, dtype=np.uint8)
        base_bgr = page["base_bgr"]

        canvas[20:166, :] = base_bgr[20:166, :]
        canvas[948:958, :] = base_bgr[948:958, :]

        glyphs_to_draw: List[CharGlyph] = []
        highlights_to_draw: List[Tuple[Tuple[int, int, int, int], Tuple[int, int, int]]] = []
        hand_pos: Optional[Tuple[int, int]] = None

        for b in page["beats"]:
            st_ms = b["start_ms"]
            if cur_ms < st_ms:
                continue

            ax0, ay0, ax1, ay1 = b["art_box"]
            zx0, zy0, zx1, zy1 = b["zone_box"]
            pop_dur = 380.0

            if cur_ms < st_ms + pop_dur:
                t_sec = (cur_ms - st_ms) / 1000.0
                sp = remotion_spring(t_sec, duration=pop_dur / 1000.0)
                scale = 0.86 + 0.14 * sp
                pw, ph = ax1 - ax0, ay1 - ay0
                sw = max(1, int(round(pw * scale)))
                sh = max(1, int(round(ph * scale)))
                crop = base_bgr[ay0:ay1, ax0:ax1]
                scaled = cv2.resize(crop, (sw, sh), interpolation=cv2.INTER_LANCZOS4)
                dx = ax0 + (pw - sw) // 2
                dy = ay0 + (ph - sh) // 2
                y_s = max(0, dy)
                y_e = min(self.h, dy + sh)
                x_s = max(0, dx)
                x_e = min(self.w, dx + sw)
                if y_e > y_s and x_e > x_s:
                    canvas[y_s:y_e, x_s:x_e] = scaled[y_s - dy : y_e - dy, x_s - dx : x_s - dx + (x_e - x_s)]
                continue
            else:
                canvas[zy0:zy1, zx0:zx1] = base_bgr[zy0:zy1, zx0:zx1]

            l2 = b["lines"][1]
            if cur_ms >= l2.start_ms:
                hl_p = min(1.0, (cur_ms - l2.start_ms) / l2.dur_ms)
                hb0, hb1, hb2, hb3 = b["hl_bbox"]
                cur_hx1 = hb0 + max(20, int(round((hb2 - hb0) * hl_p)))
                highlights_to_draw.append(((hb0, hb1, cur_hx1, hb3), b["hl_color"]))

            for l_idx, line in enumerate(b["lines"]):
                if cur_ms < line.start_ms:
                    continue
                elif cur_ms <= line.end_ms:
                    p_l = (cur_ms - line.start_ms) / line.dur_ms
                    n_g = len(line.glyphs)
                    c_idx = int(p_l * n_g)
                    glyphs_to_draw.extend(line.glyphs[:c_idx])
                    if c_idx < n_g:
                        ag = line.glyphs[c_idx]
                        glyphs_to_draw.append(ag)
                        jx = int(math.cos(p_l * 26 * math.pi) * 1.5)
                        jy = int(math.sin(p_l * 30 * math.pi) * 2.0)
                        hand_pos = (ag.pen_target[0] + jx, ag.pen_target[1] + jy)
                else:
                    glyphs_to_draw.extend(line.glyphs)
                    if l_idx + 1 < len(b["lines"]):
                        nl = b["lines"][l_idx + 1]
                        if line.end_ms < cur_ms < nl.start_ms and line.glyphs and nl.glyphs:
                            u_t = (cur_ms - line.end_ms) / (nl.start_ms - line.end_ms)
                            lp = line.glyphs[-1].pen_target
                            np_ = nl.glyphs[0].pen_target
                            hx = int(lp[0] + (np_[0] - lp[0]) * u_t)
                            hy = int(lp[1] + (np_[1] - lp[1]) * u_t)
                            lift = int(-24 * math.sin(math.pi * u_t))
                            hand_pos = (hx, hy + lift)

        if highlights_to_draw or glyphs_to_draw:
            p_im = Image.fromarray(cv2.cvtColor(canvas, cv2.COLOR_BGR2RGB))
            df = ImageDraw.Draw(p_im)
            for hbox, hcol in highlights_to_draw:
                df.rounded_rectangle(list(hbox), radius=10, fill=hcol)
            for g in glyphs_to_draw:
                df.text((g.x, g.y), g.char, fill=g.color, font=g.font)
            canvas = cv2.cvtColor(np.array(p_im), cv2.COLOR_RGB2BGR)

        return canvas, hand_pos

    def render_shorts_master(self, out_mp4: Path, audio_wav: Path = None):
        mastered_wav, part_durs = master_shorts_audio()
        audio_wav = mastered_wav
        pages, total_ms = self.build_pages_and_beats(part_durs)

        raw_video = out_mp4.with_name(out_mp4.stem + "_raw.mp4")
        sfx_wav = out_mp4.with_name(out_mp4.stem + "_sfx.wav")
        master_audio = out_mp4.with_name(out_mp4.stem + "_master.wav")

        total_frames = max(1, int(round(total_ms * self.fps / 1000.0)))
        ms_per_frame = 1000.0 / self.fps

        print(f"\n[SHORTS V5 - EP03] Rendering {total_frames} frames ({total_ms/1000:.2f}s) @ {self.fps}fps")
        t0 = time.time()

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        writer = cv2.VideoWriter(str(raw_video), fourcc, self.fps, (self.w, self.h))

        sfx_cues = []
        for p in pages:
            for b in p["beats"]:
                sfx_cues.append({"timeMs": b["start_ms"], "type": "pop"})
                sfx_cues.append({"timeMs": b["start_ms"], "type": "whoosh"})
                for line in b["lines"]:
                    sfx_cues.append({"timeMs": line.start_ms, "type": "scribble", "durMs": line.dur_ms})

        trans_dur_ms = 420.0
        p1_start = pages[1]["start_ms"]
        p2_start = pages[2]["start_ms"]

        hand_last_pos = None
        for fi in range(total_frames):
            cur_ms = fi * ms_per_frame

            if cur_ms < p1_start - trans_dur_ms:
                frame, hand_pos = self._render_single_page_state(pages[0], cur_ms)
            elif cur_ms < p1_start:
                u = ease_in_out_cubic((cur_ms - (p1_start - trans_dur_ms)) / trans_dur_ms)
                f0, _ = self._render_single_page_state(pages[0], cur_ms)
                f1, _ = self._render_single_page_state(pages[1], p1_start + 10)
                shift = int(round(u * self.h))
                frame = np.full((self.h, self.w, 3), 255, dtype=np.uint8)
                if self.h - shift > 0:
                    frame[0 : self.h - shift, :] = f0[shift : self.h, :]
                if shift > 0:
                    frame[self.h - shift : self.h, :] = f1[0 : shift, :]
                hand_pos = None
            elif cur_ms < p2_start - trans_dur_ms:
                frame, hand_pos = self._render_single_page_state(pages[1], cur_ms)
            elif cur_ms < p2_start:
                u = ease_in_out_cubic((cur_ms - (p2_start - trans_dur_ms)) / trans_dur_ms)
                f1, _ = self._render_single_page_state(pages[1], cur_ms)
                f2, _ = self._render_single_page_state(pages[2], p2_start + 10)
                shift = int(round(u * self.h))
                frame = np.full((self.h, self.w, 3), 255, dtype=np.uint8)
                if self.h - shift > 0:
                    frame[0 : self.h - shift, :] = f1[shift : self.h, :]
                if shift > 0:
                    frame[self.h - shift : self.h, :] = f2[0 : shift, :]
                hand_pos = None
            else:
                frame, hand_pos = self._render_single_page_state(pages[2], cur_ms)

            if hand_pos is not None:
                frame = self._stamp_hand(frame, hand_pos[0], hand_pos[1])
                hand_last_pos = hand_pos
            elif hand_last_pos is not None:
                hand_last_pos = (hand_last_pos[0], hand_last_pos[1] + 42)
                if hand_last_pos[1] < self.h + self.hand_h:
                    frame = self._stamp_hand(frame, hand_last_pos[0], hand_last_pos[1])
                else:
                    hand_last_pos = None

            writer.write(frame)

        writer.release()
        print(f"[SHORTS V5 - EP03] Video rendered in {time.time() - t0:.1f}s")

        sr = 48000
        total_samples = int((total_ms / 1000.0) * sr)
        mix = np.zeros(total_samples, dtype=np.float32)

        def load_sfx(p: Path) -> np.ndarray:
            if not p.exists():
                return np.zeros(1, dtype=np.float32)
            cmd = ["ffmpeg", "-v", "error", "-i", str(p), "-f", "f32le", "-ac", "1", "-ar", str(sr), "-"]
            res = subprocess.run(cmd, capture_output=True, check=True)
            return np.frombuffer(res.stdout, dtype=np.float32)

        pop_snd = load_sfx(SFX_DIR / "pop.mp3") * 0.35
        whoosh_snd = load_sfx(SFX_DIR / "whoosh-short.mp3") * 0.28
        scribble_snd = load_sfx(SCRIBBLE_WAV) * 0.14

        def stamp(snd, t_ms):
            st = int((t_ms / 1000.0) * sr)
            if st < total_samples and len(snd) > 0:
                en = min(total_samples, st + len(snd))
                mix[st:en] += snd[: en - st]

        for cue in sfx_cues:
            t_ms = cue["timeMs"]
            if cue["type"] == "pop":
                stamp(pop_snd, t_ms)
            elif cue["type"] == "whoosh":
                stamp(whoosh_snd, t_ms)
            elif cue["type"] == "scribble" and len(scribble_snd) > 100:
                st = int((t_ms / 1000.0) * sr)
                dur_s = int((cue["durMs"] / 1000.0) * sr)
                en = min(total_samples, st + dur_s)
                if en > st:
                    reps = (en - st) // len(scribble_snd) + 2
                    tiled = np.tile(scribble_snd, reps)[: en - st]
                    fade = min(int(0.02 * sr), len(tiled) // 4)
                    if fade > 0:
                        tiled[:fade] *= np.linspace(0, 1, fade)
                        tiled[-fade:] *= np.linspace(1, 0, fade)
                    mix[st:en] += tiled

        mix = np.clip(mix, -0.95, 0.95)
        pcm16 = (mix * 32767.0).astype(np.int16)
        import wave
        with wave.open(str(sfx_wav), "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(sr)
            wf.writeframes(pcm16.tobytes())

        filter_complex = (
            "[0:a]volume=1.0,asplit=2[vo_main][vo_sc];"
            "[1:a]volume=1.0[sfx];"
            "[2:a]volume=0.14,aloop=loop=-1:size=2e+09[bgm_raw];"
            "[bgm_raw][vo_sc]sidechaincompress=threshold=0.02:ratio=8:attack=15:release=250[bgm_duck];"
            "[vo_main][sfx][bgm_duck]amix=inputs=3:duration=first:dropout_transition=0,alimiter=limit=0.96[aout]"
        )
        subprocess.run(
            [
                "ffmpeg", "-y",
                "-i", str(audio_wav),
                "-i", str(sfx_wav),
                "-i", str(BGM_WAV),
                "-filter_complex", filter_complex,
                "-map", "[aout]",
                "-c:a", "pcm_s16le", "-ar", "48000",
                str(master_audio),
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        subprocess.run(
            [
                "ffmpeg", "-y",
                "-i", str(raw_video),
                "-i", str(master_audio),
                "-c:v", "libx264", "-preset", "fast", "-crf", "17",
                "-pix_fmt", "yuv420p",
                "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                "-shortest",
                str(out_mp4),
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        raw_video.unlink(missing_ok=True)
        sfx_wav.unlink(missing_ok=True)
        master_audio.unlink(missing_ok=True)
        print(f"[SHORTS V5 - EP03] Master exported -> {out_mp4}")


if __name__ == "__main__":
    renderer = ShortsV4Renderer(fps=30)
    out_file = RENDERS_DIR / "tap03_ca_heo_shorts.mp4"
    renderer.render_shorts_master(out_file)
