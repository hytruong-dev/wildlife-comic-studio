"""
Shorts Video Renderer V5 — Episode 4: Thú Mỏ Vịt (Platypus) Viral Channel Funnel Edition (9:16 Infinite Vertical Sketchbook)
- Native 1080x1920 Full HD Vertical (9:16) on Pure White (#FFFFFF) Infinite Paper
- 3 Vertical Sketchbook Pages x 2 Large Uncropped Visual Beats = 6 High-Retention Beats
- 1-to-1 Millisecond Sync with Broadcast Male Voiceover (`shorts.wav`, ~48.28s)
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
        # Probe exact durations of the fast audio parts
        fast_durs = []
        for idx in range(5):
            wav_file = AUDIO_DIR / f"shorts_fast_p{idx}.wav"
            if wav_file.exists():
                cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(wav_file)]
                d = float(subprocess.check_output(cmd, text=True).strip())
                fast_durs.append(d)
            else:
                fast_durs.append(part_durs[idx])

        gap_ms = 100
        # Beat 0: Part 0 (Hook)
        st0 = 0
        en0 = int(round(fast_durs[0] * 1000))

        # Beat 1: Part 1 (Sự thật 1: Mỏ khâu & Kéo rạch)
        st1 = en0 + gap_ms
        en1 = st1 + int(round(fast_durs[1] * 1000))

        # Beat 2 & 3: Part 2 (Sự thật 2: Không dạ dày & Ngậm sỏi má)
        st2 = en1 + gap_ms
        d2_a = 4260  # ms for sentence 1: "Sự thật thứ hai: Thú mỏ vịt hoàn toàn không có dạ dày và không có răng!"
        en2 = st2 + d2_a

        st3 = en2
        en3 = st2 + int(round(fast_durs[2] * 1000))

        # Beat 4: Part 3 (Sự thật 3: Đẻ trứng, cựa độc, sữa mồ hôi & phát sáng UV)
        st4 = en3 + gap_ms
        en4 = st4 + int(round(fast_durs[3] * 1000))

        # Beat 5: Part 4 (Call to Action sang bản Full Tập 4)
        st5 = en4 + gap_ms
        en5 = st5 + int(round(fast_durs[4] * 1000))

        beat_starts_ms = [st0, st1, st2, st3, st4, st5]
        beat_ends_ms = [en0, en1, en2, en3, en4, en5]
        total_ms = en5

        pages_meta = [
            {
                "page_idx": 0,
                "header_title": "3 SỰ THẬT SỐC: THÚ MỎ VỊT!",
                "header_sub": "CÚ LỪA MỎ VỊT KHÂU CHỈ CỦA THẾ KỶ 18",
                "header_accent": (214, 40, 40),
                "beats": [
                    {
                        "beat_idx": 0,
                        "slot": "upper",
                        "img": G / "thumb_ep04_thu_mo_vit_gemini.png",
                        "badge": "SINH VẬT KỲ DỊ NHẤT HÀNH TINH",
                        "badge_bg": (214, 40, 40),
                        "hl_color": (254, 240, 138),
                        "lines": [
                            "Đừng để vẻ ngoài ngộ nghĩnh đánh lừa!",
                            "3 sự thật sốc về sinh vật dị nhất hành tinh!",
                        ],
                    },
                    {
                        "beat_idx": 1,
                        "slot": "lower",
                        "img": G / "c1_scissors_cutting_beak_hoax_search.png",
                        "badge": "SỰ THẬT 1: CẦM KÉO RẠCH TÌM CHỈ KHÂU",
                        "badge_bg": (43, 108, 176),
                        "hl_color": (191, 219, 254),
                        "lines": [
                            "Tưởng trò chơi khăm khâu mỏ vịt vào rái cá,",
                            "Các nhà khoa học cầm kéo rạch tìm đường chỉ!",
                        ],
                    },
                ],
            },
            {
                "page_idx": 1,
                "header_title": "SỰ THẬT 2: KHÔNG DẠ DÀY & KHÔNG RĂNG!",
                "header_sub": "NHÉT SỎI ĐÁ VÀO TÚI MÁ ĐỂ NGHIỀN TÔM CUA",
                "header_accent": (194, 65, 12),
                "beats": [
                    {
                        "beat_idx": 2,
                        "slot": "upper",
                        "img": G / "c4_zero_stomach_digestive_tract.png",
                        "badge": "KHÔNG DẠ DÀY • KHÔNG HỀ CÓ RĂNG!",
                        "badge_bg": (194, 65, 12),
                        "hl_color": (254, 215, 170),
                        "lines": [
                            "Sinh vật duy nhất không hề có dạ dày!",
                            "Thực quản nối thẳng trực tiếp ruột non!",
                        ],
                    },
                    {
                        "beat_idx": 3,
                        "slot": "lower",
                        "img": G / "c4_cheek_pouches_gravel_scoop.png",
                        "badge": "NGẬM SỎI ĐÁ VÀO TÚI MÁ NGHIỀN MỒI",
                        "badge_bg": (47, 133, 90),
                        "hl_color": (187, 247, 208),
                        "lines": [
                            "Nhét đầy sỏi đá cứng vào hai túi má,",
                            "Nghiền nát vỏ tôm cua rồi nuốt thẳng!",
                        ],
                    },
                ],
            },
            {
                "page_idx": 2,
                "header_title": "SỰ THẬT 3: PHÁT SÁNG UV & CỰA ĐỘC!",
                "header_sub": "BẤM VÀO KÊNH XEM NGAY BẢN FULL TẬP 4",
                "header_accent": (107, 70, 193),
                "beats": [
                    {
                        "beat_idx": 4,
                        "slot": "upper",
                        "img": G / "c3_uv_light_biofluorescence_glow.png",
                        "badge": "SỰ THẬT 3: PHÁT SÁNG XANH DƯỚI TIA UV!",
                        "badge_bg": (107, 70, 193),
                        "hl_color": (233, 213, 255),
                        "lines": [
                            "Cựa độc như rắn, sữa rỉ qua lông bụng...",
                            "Phát sáng xanh ngọc bích dưới tia UV!",
                        ],
                    },
                    {
                        "beat_idx": 5,
                        "slot": "lower",
                        "img": G / "c1_taxonomic_crisis_chimera_puzzle.png",
                        "badge": "👉 XEM NGAY BẢN FULL TẬP 4 TRÊN KÊNH!",
                        "badge_bg": (220, 38, 38),
                        "hl_color": (254, 240, 138),
                        "lines": [
                            "Khám phá toàn bộ bí ẩn 160 triệu năm!",
                            "Bấm vào kênh xem ngay bản Full siêu cuốn!",
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
                write_start = st_ms + 250
                write_avail = max(1100, min(3800, int((en_ms - st_ms) * 0.62)))
                l1_end = write_start + int(write_avail * 0.48)
                l2_start = l1_end + 60
                l2_end = write_start + write_avail

                wl1, bbox1 = self._layout_centered_line(
                    bm["lines"][0], 540, l1_y, font_hand, (20, 20, 20), write_start, l1_end
                )
                wl2, bbox2 = self._layout_centered_line(
                    bm["lines"][1], 540, l2_y, font_hand, (20, 20, 20), l2_start, l2_end
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

    def render_shorts_master(self, out_mp4: Path, audio_wav: Path):
        part_durs = json.loads((AUDIO_DIR / "shorts_parts_duration.json").read_text(encoding="utf-8"))
        pages, total_ms = self.build_pages_and_beats(part_durs)

        raw_video = out_mp4.with_name(out_mp4.stem + "_raw.mp4")
        total_frames = max(1, int(round(total_ms * self.fps / 1000.0)))
        ms_per_frame = 1000.0 / self.fps

        print(f"\n[SHORTS V5 - EP04] Rendering {total_frames} frames ({total_ms/1000:.2f}s) @ {self.fps}fps")
        t0 = time.time()

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        writer = cv2.VideoWriter(str(raw_video), fourcc, self.fps, (self.w, self.h))

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
        print(f"[SHORTS V5 - EP04] Video rendered in {time.time() - t0:.1f}s")

        # Mux with broadcast audio + subtle acoustic BGM ducked behind voice
        if BGM_WAV.exists():
            filter_complex = (
                "[1:a]volume=1.05[v_voice];"
                "[2:a]volume=0.12,aloop=loop=-1:size=2e+09[v_bgm];"
                "[v_voice][v_bgm]amix=inputs=2:duration=first:dropout_transition=2[aout]"
            )
            cmd = [
                "ffmpeg", "-y",
                "-i", str(raw_video),
                "-i", str(audio_wav),
                "-i", str(BGM_WAV),
                "-filter_complex", filter_complex,
                "-map", "0:v:0",
                "-map", "[aout]",
                "-c:v", "libx264", "-preset", "fast", "-crf", "18",
                "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-ac", "2",
                "-shortest",
                str(out_mp4),
            ]
        else:
            cmd = [
                "ffmpeg", "-y",
                "-i", str(raw_video),
                "-i", str(audio_wav),
                "-c:v", "libx264", "-preset", "fast", "-crf", "18",
                "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-ac", "2",
                "-shortest",
                str(out_mp4),
            ]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        raw_video.unlink(missing_ok=True)
        print(f"[SHORTS V5 - EP04] Final Muxed Shorts: {out_mp4}")
        return out_mp4


if __name__ == "__main__":
    renderer = ShortsV4Renderer(fps=30)
    out_mp4 = RENDERS_DIR / "tap04_thu_mo_vit_shorts.mp4"
    audio_wav = AUDIO_DIR / "shorts.wav"
    renderer.render_shorts_master(out_mp4, audio_wav)
