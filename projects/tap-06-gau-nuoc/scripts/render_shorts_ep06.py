"""
Shorts Video Renderer V6 — Episode 06: Gấu Nước (Tardigrade) Viral Channel Funnel Edition (9:16 Infinite Vertical Sketchbook)
- Native 1080x1920 Full HD Vertical (9:16) on Pure White (#FFFFFF) Infinite Paper
- 3 Vertical Sketchbook Pages x 2 Large Uncropped Visual Beats = 6 High-Retention Beats
- 1-to-1 Millisecond Sync with ElevenLabs Adam Voiceover (`shorts.wav`, 53.07s)
- 100% True Character-by-Character Hand-Drawn Captions with Real Hand Rig & Marker SFX
- Clean, watermark-free illustrations perfectly aligned with each spoken fact
- 1.5s comfortable visual CTA hold buffer at end (total ~54.57s)
- Smooth Vertical Infinite Canvas Scroll between Pages 1 -> 2 -> 3
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
G_SHORTS = PROJ / "assets" / "gemini_downloaded_shorts"
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


class ShortsV6Renderer:
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
        bbox = d.textbbox((0, 0), text, font=font)
        tot_w = bbox[2] - bbox[0]
        line_h = bbox[3] - bbox[1]
        cur_x = center_x - tot_w // 2

        glyphs = []
        for ch in text:
            cb = d.textbbox((0, 0), ch, font=font)
            cw = cb[2] - cb[0]
            ch_h = cb[3] - cb[1]
            advance = cw if cw > 0 else int(font.size * 0.32)
            glyphs.append(CharGlyph(ch, cur_x, y, advance, max(line_h, ch_h), font, color))
            cur_x += advance

        hl_pad_x = 18
        hl_pad_y = 6
        hl_box = (
            center_x - tot_w // 2 - hl_pad_x,
            y - hl_pad_y,
            center_x + tot_w // 2 + hl_pad_x,
            y + line_h + hl_pad_y,
        )
        return WritingLine(glyphs, start_ms, end_ms), hl_box

    def build_pages_and_beats(self, part_durs: Dict[str, float], gap_sec: float) -> Tuple[List[Dict], int]:
        p0 = part_durs.get("part0", 3.50)
        p1 = part_durs.get("part1", 9.50)
        p2 = part_durs.get("part2", 12.50)
        p3 = part_durs.get("part3", 12.50)
        p4 = part_durs.get("part4", 11.00)
        p5 = part_durs.get("part5", 3.57)

        gap_ms = int(round(gap_sec * 1000))

        st0 = 0
        en0 = int(round(p0 * 1000))

        st1 = en0 + gap_ms
        en1 = st1 + int(round(p1 * 1000))

        st2 = en1 + gap_ms
        en2 = st2 + int(round(p2 * 1000))

        st3 = en2 + gap_ms
        en3 = st3 + int(round(p3 * 1000))

        st4 = en3 + gap_ms
        en4 = st4 + int(round(p4 * 1000))

        st5 = en4 + gap_ms
        en5 = st5 + int(round(p5 * 1000))

        outro_buffer_ms = 1500  # 1.5s visual CTA hold buffer at end
        beat_starts_ms = [st0, st1, st2, st3, st4, st5]
        beat_ends_ms = [en0, en1, en2, en3, en4, en5]
        total_ms = en5 + outro_buffer_ms

        pages_meta = [
            {
                "page_idx": 0,
                "header_title": "3 SỰ THẬT SỐC: GẤU NƯỚC BẤT TỬ!",
                "header_sub": "KẺ SỐNG SÓT QUA ĐẠI TUYỆT CHỦNG VÀ VŨ TRỤ",
                "header_accent": (214, 40, 40),
                "beats": [
                    {
                        "beat_idx": 0,
                        "slot": "upper",
                        "img": G_SHORTS / "shorts01_superhero_space_radiation.png",
                        "badge": "KẺ BẤT TỬ TRONG KHÔNG GIAN VŨ TRỤ",
                        "badge_bg": (214, 40, 40),
                        "hl_color": (254, 240, 138),
                        "lines": [
                            "Đừng để vẻ ngoài tí hon này đánh lừa!",
                            "Sinh vật duy nhất sống sót ngoài vũ trụ!",
                        ],
                    },
                    {
                        "beat_idx": 1,
                        "slot": "lower",
                        "img": G_SHORTS / "shorts02_temperature_extreme_scale.png",
                        "badge": "SỰ THẬT 1: THANG ĐO NHIỆT ĐỘ KHẮC NGHIỆT",
                        "badge_bg": (43, 108, 176),
                        "hl_color": (191, 219, 254),
                        "lines": [
                            "Đóng băng âm 272 độ C hay luộc sôi 150 độ C,",
                            "Áp suất 6000 atm đè bẹp vỏ thép vẫn cười tươi!",
                        ],
                    },
                ],
            },
            {
                "page_idx": 1,
                "header_title": "SỰ THẬT 2: KÉN THỦY TINH VÀ ĐIỂM YẾU BI HÀI",
                "header_sub": "RÚT CẠN NƯỚC NGỦ 30 NĂM NHƯNG SỢ CHẤT NHẦY ỐC SÊN",
                "header_accent": (194, 65, 12),
                "beats": [
                    {
                        "beat_idx": 2,
                        "slot": "upper",
                        "img": G_SHORTS / "shorts03_tun_state_glass_hibernation.png",
                        "badge": "SỰ THẬT 2: KÉN THỦY TINH CRYPTOBIOSIS",
                        "badge_bg": (194, 65, 12),
                        "hl_color": (254, 215, 170),
                        "lines": [
                            "Tự rút 99% nước, co 8 chân hóa hạt thủy tinh,",
                            "Đóng băng chuyển hóa ngủ sâu suốt 30 năm!",
                        ],
                    },
                    {
                        "beat_idx": 3,
                        "slot": "lower",
                        "img": G_SHORTS / "shorts04_snail_slime_choke_trap.png",
                        "badge": "CẠM BẪY CHẤT NHẦY CỦA ỐC SÊN",
                        "badge_bg": (47, 133, 90),
                        "hl_color": (187, 247, 208),
                        "lines": [
                            "Khi thức dậy lại mềm như kẹo dẻo mỏng manh,",
                            "Bị nhớt ốc sên làm ngạt và giun tròn nuốt chửng!",
                        ],
                    },
                ],
            },
            {
                "page_idx": 2,
                "header_title": "SỰ THẬT 3: ĐẠI CHIẾN MẶT TRĂNG VÀ CTA",
                "header_sub": "BẤM VÀO KÊNH XEM NGAY BẢN FULL TẬP 6",
                "header_accent": (107, 70, 193),
                "beats": [
                    {
                        "beat_idx": 4,
                        "slot": "upper",
                        "img": G_SHORTS / "shorts05_moon_crash_sleeping_bears.png",
                        "badge": "SỰ THẬT 3: CÔNG DÂN ĐẦU TIÊN CỦA MẶT TRĂNG",
                        "badge_bg": (107, 70, 193),
                        "hl_color": (233, 213, 255),
                        "lines": [
                            "Tàu Beresheet đâm nổ tung năm 2019,",
                            "Hàng ngàn gấu nước đang ngủ trên đất Mặt Trăng!",
                        ],
                    },
                    {
                        "beat_idx": 5,
                        "slot": "lower",
                        "img": G_SHORTS / "shorts06_channel_funnel_cta_mascot.png",
                        "badge": "👉 XEM NGAY BẢN FULL TẬP 6 TRÊN KÊNH!",
                        "badge_bg": (220, 38, 38),
                        "hl_color": (254, 240, 138),
                        "lines": [
                            "Khám phá bí mật siêu công nghệ gen bất tử!",
                            "Bấm link dưới tiêu đề xem ngay bản Full nhé!",
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

                draw_p.rounded_rectangle([bx0 + 3, by0 + 3, bx1 + 3, by1 + 3], radius=14, fill=(15, 23, 42))
                draw_p.rounded_rectangle([bx0, by0, bx1, by1], radius=14, fill=bm["badge_bg"], outline=(255, 255, 255), width=2)
                draw_p.text((540, badge_cy), bm["badge"], fill=(255, 255, 255), font=font_badge, anchor="mm")

                l1_y = zone_y0 + 636
                l2_y = zone_y0 + 682
                write_start = st_ms + 260
                write_end = en_ms - 200
                w_mid = write_start + int(round((write_end - write_start) * 0.48))
                l1_end = w_mid
                l2_start = w_mid + 80
                l2_end = write_end

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

            # Draw bottom branding banner
            bb = [32, 1756, 1048, 1888]
            draw_p.rounded_rectangle([bb[0] + 4, bb[1] + 4, bb[2] + 4, bb[3] + 4], radius=20, fill=(30, 41, 59))
            draw_p.rounded_rectangle(bb, radius=20, fill=(248, 250, 252), outline=(30, 41, 59), width=3)
            draw_p.text((540, 1798), "VẼ CHUYỆN HOANG DÃ • TẬP 06", fill=(214, 40, 40), font=font_cta_main, anchor="mm")
            draw_p.text((540, 1846), "Đăng ký kênh & Bấm link tiêu đề xem bản Full 8 phút!", fill=(51, 65, 85), font=font_cta_sub, anchor="mm")

            pages_rendered.append(
                {
                    "page_idx": pm["page_idx"],
                    "bg_bgr": cv2.cvtColor(np.array(page_pil), cv2.COLOR_RGB2BGR),
                    "beats": beat_objs,
                    "start_ms": beat_objs[0]["start_ms"],
                    "end_ms": beat_objs[-1]["end_ms"],
                }
            )

        return pages_rendered, total_ms

    def _render_single_page_state(self, page_dict: Dict, cur_ms: float) -> Tuple[np.ndarray, Optional[Tuple[int, int]]]:
        canvas = page_dict["bg_bgr"].copy()
        hand_pos = None

        highlights_to_draw = []
        glyphs_to_draw = []

        for b in page_dict["beats"]:
            st = b["start_ms"]
            en = b["end_ms"]
            if cur_ms < st:
                continue

            last_line = b["lines"][-1]
            if cur_ms >= last_line.end_ms + 80:
                t_hl = (cur_ms - (last_line.end_ms + 80)) / 1000.0
                p_hl = remotion_spring(t_hl, duration=0.35)
                if p_hl > 0.0:
                    hb = b["hl_bbox"]
                    curr_x1 = int(round(hb[0] + (hb[2] - hb[0]) * p_hl))
                    highlights_to_draw.append(((hb[0], hb[1], curr_x1, hb[3]), b["hl_color"]))

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
        data = json.loads((AUDIO_DIR / "shorts_parts_duration.json").read_text(encoding="utf-8"))
        part_durs_dict = data.get("parts", {})
        gap_sec = data.get("gap_sec", 0.10)
        pages, total_ms = self.build_pages_and_beats(part_durs_dict, gap_sec)

        raw_video = out_mp4.with_name(out_mp4.stem + "_raw.mp4")
        total_frames = max(1, int(round(total_ms * self.fps / 1000.0)))
        ms_per_frame = 1000.0 / self.fps

        print(f"\n[SHORTS V6 - EP06] Rendering {total_frames} frames ({total_ms/1000:.2f}s) @ {self.fps}fps")
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
            elif hand_last_pos is not None and cur_ms < total_ms - 1500:
                pass

            writer.write(frame)
            if fi % 150 == 0 or fi == total_frames - 1:
                prog = (fi + 1) / total_frames * 100.0
                fps_act = (fi + 1) / max(0.001, time.time() - t0)
                print(f"  Frame {fi+1}/{total_frames} ({prog:5.1f}%) — {fps_act:.1f} fps", end="\r")

        writer.release()
        print(f"\n[RAW VIDEO DONE] Rendered in {time.time() - t0:.1f}s -> {raw_video.name}")

        # Audio Muxing (Voice + Marker SFX + BGM)
        print("[AUDIO MUXING] Combining voiceover, marker sound effects, and soft BGM...")
        filter_complex = (
            f"[1:a]volume=1.0[v_voice];"
            f"[2:a]aloop=loop=-1:size=2e+09,volume=0.35[v_sfx];"
            f"[3:a]aloop=loop=-1:size=2e+09,volume=0.08[v_bgm];"
            f"[v_voice][v_sfx][v_bgm]amix=inputs=3:duration=first:dropout_transition=2[a_out]"
        )

        cmd = [
            "ffmpeg", "-y",
            "-i", str(raw_video),
            "-i", str(audio_wav),
            "-i", str(SCRIBBLE_WAV),
            "-i", str(BGM_WAV),
            "-filter_complex", filter_complex,
            "-map", "0:v",
            "-map", "[a_out]",
            "-c:v", "libx264", "-preset", "fast", "-crf", "18",
            "-c:a", "aac", "-b:a", "256k", "-ar", "48000",
            "-shortest",
            str(out_mp4),
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        raw_video.unlink(missing_ok=True)
        print(f"[SHORTS COMPLETE] Final Video Exported -> {out_mp4.name} ({out_mp4.stat().st_size/1024/1024:.2f} MB)")


def main():
    renderer = ShortsV6Renderer(fps=30)
    out_mp4 = RENDERS_DIR / "shorts_ep06_final.mp4"
    audio_wav = AUDIO_DIR / "shorts.wav"
    renderer.render_shorts_master(out_mp4, audio_wav)


if __name__ == "__main__":
    main()
