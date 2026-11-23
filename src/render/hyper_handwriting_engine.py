"""
HyperFrames & Remotion Inspired True Handwriting Engine (V4)
- Zero Rectangular Wipe ("Tuyệt đối không làm tô / quét mặt nạ chữ nhật")
- Sequential Line-by-Line, Word-by-Word, Character-by-Character writing
- Remotion Damped Harmonic Spring Physics for card & photo pop-ins
- Dynamic Carriage Return Lift Arcs & Space Hops for the Hand Rig
- HyperFrames Editorial Design System & Refined Color Palette
- Fully automated audio mastering (Voice + Line-synchronized SFX + Ducked BGM)
"""

import math
import time
import json
import subprocess
from pathlib import Path
from typing import List, Dict, Tuple, Optional, Any
import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont

# ---------------------------------------------------------
# REMOTION SPRING PHYSICS
# Damped Harmonic Oscillator: x(t) = 1 - e^(-zeta*omega*t) * (cos(wd*t) + (zeta/sqrt(1-zeta^2))*sin(wd*t))
# ---------------------------------------------------------
def remotion_spring(t: float, duration: float = 0.42, omega: float = 16.0, zeta: float = 0.82) -> float:
    """
    Returns progress from 0.0 to ~1.0 with natural organic overshoot.
    t: elapsed time in seconds
    """
    if t <= 0.0:
        return 0.0
    if t >= duration:
        return 1.0
    u = t / duration
    wd = omega * math.sqrt(max(0.001, 1.0 - zeta * zeta))
    decay = math.exp(-zeta * omega * u)
    osc = math.cos(wd * u) + (zeta / math.sqrt(max(0.001, 1.0 - zeta * zeta))) * math.sin(wd * u)
    val = 1.0 - decay * osc
    return max(0.0, min(1.06, val))

# ---------------------------------------------------------
# FONT LOADER
# ---------------------------------------------------------
FONT_DIR = Path("assets/fonts")
FONT_TITLE_L = ImageFont.truetype(str(FONT_DIR / "Mali-Bold.ttf"), 28)
FONT_CARD_HDR = ImageFont.truetype(str(FONT_DIR / "Mali-Bold.ttf"), 23)
FONT_BULLET_TITLE = ImageFont.truetype(str(FONT_DIR / "Mali-Bold.ttf"), 22)
FONT_BULLET_DESC = ImageFont.truetype(str(FONT_DIR / "PlaypenSans-Regular.ttf"), 19)
FONT_STAT_VAL = ImageFont.truetype(str(FONT_DIR / "Mali-Bold.ttf"), 17)
FONT_STAT_LABEL = ImageFont.truetype(str(FONT_DIR / "PlaypenSans-Regular.ttf"), 16)

# ---------------------------------------------------------
# TEXT STRUCTURE COMPILER (Char-by-Char Deconstruction)
# ---------------------------------------------------------
class CharGlyph:
    def __init__(self, ch: str, x: int, y: int, w: int, h: int, font: ImageFont.FreeTypeFont, color: Tuple[int, int, int]):
        self.char = ch
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.font = font
        self.color = color
        self.pen_target = (x + int(w * 0.70), y + int(h * 0.72))

class WritingLine:
    def __init__(self, glyphs: List[CharGlyph], start_ms: float, end_ms: float, is_bullet_head: bool = False, bullet_color: Optional[Tuple[int, int, int]] = None):
        self.glyphs = glyphs
        self.start_ms = start_ms
        self.end_ms = end_ms
        self.dur_ms = max(1.0, end_ms - start_ms)
        self.is_bullet_head = is_bullet_head
        self.bullet_color = bullet_color

class WritingBullet:
    def __init__(self, lines: List[WritingLine], stat_spec: Optional[Dict[str, Any]], start_ms: float, end_ms: float):
        self.lines = lines
        self.stat_spec = stat_spec
        self.start_ms = start_ms
        self.end_ms = end_ms

# ---------------------------------------------------------
# HYPERFRAME & REMOTION WHITEBOARD ENGINE
# ---------------------------------------------------------
class HyperWhiteboardRenderer:
    def __init__(self, spec: Dict[str, Any], fps: int = 30):
        self.spec = spec
        self.fps = fps
        self.w = spec.get("canvas", {}).get("width", 1920)
        self.h = spec.get("canvas", {}).get("height", 1080)

        # Hand Rig setup
        hand_png = Path("assets/hands/hand-marker-right.png")
        hand_meta_path = Path("assets/hands/hand_metadata.json")
        hand_meta = {}
        if hand_meta_path.exists():
            with open(hand_meta_path, "r", encoding="utf-8") as f:
                hand_meta = json.load(f)

        self.hand_scale = hand_meta.get("defaultScale", 0.75)
        raw_hand = cv2.imread(str(hand_png), cv2.IMREAD_UNCHANGED)
        if raw_hand is None:
            raise FileNotFoundError(f"Hand sprite not found: {hand_png}")

        new_hw = max(1, int(round(raw_hand.shape[1] * self.hand_scale)))
        new_hh = max(1, int(round(raw_hand.shape[0] * self.hand_scale)))
        resized_hand = cv2.resize(raw_hand, (new_hw, new_hh), interpolation=cv2.INTER_LANCZOS4)

        self.hand_bgr = resized_hand[:, :, :3]
        self.hand_alpha = (resized_hand[:, :, 3] / 255.0)[:, :, np.newaxis]
        self.hand_w = new_hw
        self.hand_h = new_hh
        self.anchor_x = int(round(hand_meta.get("anchor", {}).get("x", 22) * self.hand_scale))
        self.anchor_y = int(round(hand_meta.get("anchor", {}).get("y", 47) * self.hand_scale))

    def _stamp_hand(self, canvas: np.ndarray, pen_x: int, pen_y: int) -> np.ndarray:
        """Stamps hand with anchor at (pen_x, pen_y)."""
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

    def build_schedule_and_base(self) -> Tuple[np.ndarray, Dict[str, Any]]:
        """
        Builds:
        1. base_bgr: Empty cards with borders, drop shadows, header bars, and photos.
        2. writing_schedule: Deconstructed lines, words, and characters with exact timestamps.
        """
        # Warm Paper background: #F8F6F1 (248, 246, 241)
        bg_color = (248, 246, 241)
        base_pil = Image.new("RGB", (self.w, self.h), bg_color)
        draw_b = ImageDraw.Draw(base_pil)

        # Header Box (Top Pill Badge)
        hdr = self.spec["header"]
        title_text = hdr["text"]
        bbox = draw_b.textbbox((0, 0), title_text, font=FONT_TITLE_L)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        padx, pady = 44, 12
        bw, bh = tw + 2 * padx, th + 2 * pady
        bx0 = (self.w - bw) // 2
        by0 = 20
        bx1, by1 = bx0 + bw, by0 + bh

        # Multi-layer ambient drop shadow for header pill (HyperFrames style)
        draw_b.rounded_rectangle([bx0 + 5, by0 + 5, bx1 + 5, by1 + 5], radius=18, fill=(224, 220, 212))
        draw_b.rounded_rectangle([bx0 + 2, by0 + 2, bx1 + 2, by1 + 2], radius=18, fill=(234, 230, 222))
        draw_b.rounded_rectangle([bx0, by0, bx1, by1], radius=18, fill=(255, 255, 255), outline=(30, 41, 59), width=2)

        # Build Header Glyphs for writing
        hdr_glyphs = []
        cur_x = bx0 + padx
        for ch in title_text:
            cbox = draw_b.textbbox((cur_x, by0 + pady), ch, font=FONT_TITLE_L)
            cw = max(5, cbox[2] - cbox[0])
            ch_h = max(10, cbox[3] - cbox[1])
            hdr_glyphs.append(CharGlyph(ch, cur_x, by0 + pady, cw, ch_h, FONT_TITLE_L, (15, 23, 42)))
            cur_x += cw

        h_start = hdr.get("startMs", 0)
        h_dur = hdr.get("durMs", 1800)
        hdr_line = WritingLine(hdr_glyphs, h_start, h_start + h_dur)

        # Panels setup
        panels_data = []
        for panel in self.spec.get("panels", []):
            box = panel["box"]
            x0, y0, x1, y1 = box
            pw, ph = x1 - x0, y1 - y0
            color = panel["color"]
            header_bg = panel["header_bg"]
            p_start = panel["startMs"]

            # Ambient multi-layer shadow for panel card (HyperFrames editorial feel)
            draw_b.rounded_rectangle([x0 + 7, y0 + 7, x1 + 7, y1 + 7], radius=20, fill=(222, 218, 210))
            draw_b.rounded_rectangle([x0 + 3, y0 + 3, x1 + 3, y1 + 3], radius=20, fill=(232, 228, 220))
            draw_b.rounded_rectangle(box, radius=20, fill=(255, 255, 255), outline=color, width=2)

            # Modern header tab with soft tint
            draw_b.rounded_rectangle([x0 + 2, y0 + 2, x1 - 2, y0 + 52], radius=18, fill=header_bg)
            draw_b.text((x0 + 26, y0 + 27), panel["title"], fill=color, font=FONT_CARD_HDR, anchor="lm")

            # Illustration Card inside panel
            img_path = Path(panel["img_path"])
            text_y_start = y0 + 74
            if img_path.exists():
                im_raw = Image.open(img_path).convert("RGB")
                max_w = pw - 48
                max_h = int(ph * 0.44)
                scale = min(max_w / im_raw.width, max_h / im_raw.height)
                iw, ih = int(round(im_raw.width * scale)), int(round(im_raw.height * scale))
                im_scaled = im_raw.resize((iw, ih), Image.Resampling.LANCZOS)
                ix0 = x0 + (pw - iw) // 2
                iy0 = y0 + 66

                base_pil.paste(im_scaled, (ix0, iy0))
                draw_b.rounded_rectangle([ix0 - 2, iy0 - 2, ix0 + iw + 2, iy0 + ih + 2], radius=10, outline=(226, 232, 240), width=2)
                text_y_start = iy0 + ih + 20

            # Bullets deconstruction
            cur_y = text_y_start
            bullet_objs = []
            for bp in panel.get("bullets", []):
                btitle = bp["title"]
                bcolor = bp.get("color", (15, 23, 42))
                b_start = bp["startMs"]
                b_dur = bp["durMs"]
                bx = x0 + 28

                # Deconstruct Title Line
                t_glyphs = []
                tx = bx
                for ch in btitle:
                    cbox = draw_b.textbbox((tx, cur_y), ch, font=FONT_BULLET_TITLE)
                    cw = max(4, cbox[2] - cbox[0])
                    ch_h = max(10, cbox[3] - cbox[1])
                    t_glyphs.append(CharGlyph(ch, tx, cur_y, cw, ch_h, FONT_BULLET_TITLE, bcolor))
                    tx += cw

                cur_y += 32

                # Deconstruct Description Lines
                desc = bp.get("desc", "")
                desc_lines_glyphs = []
                if desc:
                    for line_str in desc.split("\n"):
                        d_glyphs = []
                        dx = bx + 16
                        for ch in line_str:
                            cbox = draw_b.textbbox((dx, cur_y), ch, font=FONT_BULLET_DESC)
                            cw = max(4, cbox[2] - cbox[0])
                            ch_h = max(8, cbox[3] - cbox[1])
                            d_glyphs.append(CharGlyph(ch, dx, cur_y, cw, ch_h, FONT_BULLET_DESC, (51, 65, 85)))
                            dx += cw
                        desc_lines_glyphs.append(d_glyphs)
                        cur_y += 28

                # Stat Spec
                stat_spec = None
                if "stat" in bp:
                    st = bp["stat"]
                    bar_x = bx + 16
                    bar_y = cur_y + 4
                    bar_w = pw - 80
                    bar_h = 16
                    stat_spec = {
                        "label": st["label"],
                        "val": st["val"],
                        "max": st.get("max", 100),
                        "color": st.get("color", color),
                        "box": [bar_x, bar_y, bar_x + bar_w, bar_y + bar_h],
                    }
                    # Draw base track on base canvas
                    draw_b.rounded_rectangle([bar_x, bar_y, bar_x + bar_w, bar_y + bar_h], radius=8, fill=(226, 232, 240))
                    cur_y += 32

                cur_y += bp.get("gap", 14)

                # Time allocation per line based on char weight
                total_chars = len(t_glyphs) + sum(len(g) for g in desc_lines_glyphs)
                stat_time = 650.0 if stat_spec else 0.0
                writing_dur = max(500.0, b_dur - stat_time)

                w_lines = []
                cur_t = b_start
                if total_chars > 0:
                    t_time = writing_dur * (len(t_glyphs) / total_chars)
                    w_lines.append(WritingLine(t_glyphs, cur_t, cur_t + t_time, is_bullet_head=True, bullet_color=color))
                    cur_t += t_time + 90.0  # carriage return pause

                    for d_g in desc_lines_glyphs:
                        d_time = writing_dur * (len(d_g) / total_chars)
                        w_lines.append(WritingLine(d_g, cur_t, cur_t + d_time))
                        cur_t += d_time + 90.0

                bullet_objs.append(WritingBullet(w_lines, stat_spec, b_start, b_start + b_dur))

            panels_data.append({
                "id": panel["id"],
                "box": box,
                "startMs": p_start,
                "bullets": bullet_objs,
            })

        base_bgr = cv2.cvtColor(np.array(base_pil), cv2.COLOR_RGB2BGR)
        schedule = {
            "header": hdr_line,
            "panels": panels_data,
        }
        return base_bgr, schedule

    def render_frame(self, cur_ms: float, base_bgr: np.ndarray, schedule: Dict[str, Any]) -> Tuple[np.ndarray, Optional[Tuple[int, int]]]:
        """
        Renders a single frame deterministically:
        - Real letter-by-letter handwriting under pen nib
        - Carriage return lift arcs between lines
        - Organic Remotion spring card pop-ins (scale + subtle vertical slide)
        """
        # Canvas starts with warm background
        frame = np.full((self.h, self.w, 3), (248, 246, 241), dtype=np.uint8)
        hand_pos = None

        # 1. Header Box
        hdr_line = schedule["header"]
        h_start = hdr_line.start_ms
        h_end = hdr_line.end_ms

        # Render Header Card Base
        frame[20:80, :] = base_bgr[20:80, :]

        # Glyphs PIL layer
        glyphs_to_draw: List[CharGlyph] = []

        # If header writing is active
        if cur_ms >= h_start:
            total_g = len(hdr_line.glyphs)
            if total_g > 0:
                p = min(1.0, max(0.0, (cur_ms - h_start) / hdr_line.dur_ms))
                active_idx = int(p * total_g)
                # Render past glyphs
                glyphs_to_draw.extend(hdr_line.glyphs[:active_idx])

                if cur_ms < h_end and active_idx < total_g:
                    # Active glyph
                    act_g = hdr_line.glyphs[active_idx]
                    glyphs_to_draw.append(act_g)
                    # Hand pen tip at active glyph
                    jx = int(math.cos(p * 22 * math.pi) * 1.5)
                    jy = int(math.sin(p * 26 * math.pi) * 2.0)
                    hand_pos = (act_g.pen_target[0] + jx, act_g.pen_target[1] + jy)
                else:
                    glyphs_to_draw.extend(hdr_line.glyphs)

        # 2. Panels
        for p_data in schedule["panels"]:
            p_start = p_data["startMs"]
            if cur_ms < p_start:
                continue

            x0, y0, x1, y1 = p_data["box"]
            pw, ph = x1 - x0, y1 - y0

            card_pop_dur = 440.0
            if cur_ms < p_start + card_pop_dur:
                # Remotion Spring Pop-In (omega=16.0, zeta=0.82)
                t_sec = (cur_ms - p_start) / 1000.0
                spring_val = remotion_spring(t_sec, duration=card_pop_dur / 1000.0)
                scale = 0.88 + 0.12 * spring_val
                slide_y = int((1.0 - spring_val) * 28)

                sw = max(1, int(round(pw * scale)))
                sh = max(1, int(round(ph * scale)))
                card_crop = base_bgr[y0:y1 + 8, x0:x1 + 8]
                scaled = cv2.resize(card_crop, (sw, sh), interpolation=cv2.INTER_LANCZOS4)

                dest_x = x0 + (pw - sw) // 2
                dest_y = y0 + (ph - sh) // 2 + slide_y

                dy0, dy1 = max(0, dest_y), min(self.h, dest_y + sh)
                dx0, dx1 = max(0, dest_x), min(self.w, dest_x + sw)
                cy0, cy1 = max(0, -dest_y), min(sh, self.h - dest_y)
                cx0, cx1 = max(0, -dest_x), min(sw, self.w - dest_x)

                frame[dy0:dy1, dx0:dx1] = scaled[cy0:cy1, cx0:cx1]
                continue
            else:
                # Base panel fully rendered
                frame[y0:y1 + 8, x0:x1 + 8] = base_bgr[y0:y1 + 8, x0:x1 + 8]

            # Bullets handwriting inside panel
            for b_obj in p_data["bullets"]:
                if cur_ms < b_obj.start_ms:
                    continue

                for line_idx, line in enumerate(b_obj.lines):
                    if cur_ms < line.start_ms:
                        # Future line: not written yet!
                        continue
                    elif cur_ms <= line.end_ms:
                        # Active Line being written right now!
                        p_line = (cur_ms - line.start_ms) / line.dur_ms
                        n_glyphs = len(line.glyphs)
                        curr_glyph_idx = int(p_line * n_glyphs)

                        glyphs_to_draw.extend(line.glyphs[:curr_glyph_idx])
                        if curr_glyph_idx < n_glyphs:
                            act_g = line.glyphs[curr_glyph_idx]
                            glyphs_to_draw.append(act_g)
                            # Pen tip at glyph with natural organic jitter
                            jx = int(math.cos(p_line * 28 * math.pi) * 1.5)
                            jy = int(math.sin(p_line * 32 * math.pi) * 2.0)
                            hand_pos = (act_g.pen_target[0] + jx, act_g.pen_target[1] + jy)
                        break
                    else:
                        # Finished line: all glyphs visible
                        glyphs_to_draw.extend(line.glyphs)

                        # Check if hand is in carriage-return transition to next line
                        if line_idx + 1 < len(b_obj.lines):
                            next_line = b_obj.lines[line_idx + 1]
                            if line.end_ms < cur_ms < next_line.start_ms:
                                # Hand carriage return lift arc!
                                u_trans = (cur_ms - line.end_ms) / (next_line.start_ms - line.end_ms)
                                last_pt = line.glyphs[-1].pen_target if line.glyphs else (x0 + 40, y0 + 100)
                                next_pt = next_line.glyphs[0].pen_target if next_line.glyphs else (x0 + 40, y0 + 140)

                                hx = int(last_pt[0] + (next_pt[0] - last_pt[0]) * u_trans)
                                hy = int(last_pt[1] + (next_pt[1] - last_pt[1]) * u_trans)
                                lift = int(-30 * math.sin(math.pi * u_trans))
                                hand_pos = (hx, hy + lift)

                # Stat bar rendering
                if b_obj.stat_spec:
                    stat_start = b_obj.lines[-1].end_ms if b_obj.lines else b_obj.start_ms
                    if cur_ms >= stat_start:
                        st = b_obj.stat_spec
                        bx0, by0, bx1, by1 = st["box"]
                        bw = bx1 - bx0
                        val = st["val"]
                        max_val = st["max"]
                        fill_pct = min(1.0, val / max_val)

                        stat_dur = 650.0
                        p_stat = min(1.0, max(0.0, (cur_ms - stat_start) / stat_dur))

                        # Animated bar fill
                        curr_fill_w = max(10, int(bw * fill_pct * p_stat))
                        # Draw bar fill directly onto frame
                        cv2.rectangle(frame, (bx0, by0), (bx0 + curr_fill_w, by1), st["color"], -1)

                        if cur_ms < stat_start + stat_dur:
                            # Hand follows the fill tip
                            hand_pos = (bx0 + curr_fill_w, (by0 + by1) // 2)

        # 3. Composite all active glyphs with high fidelity PIL rendering
        if glyphs_to_draw:
            pil_frame = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            draw_frame = ImageDraw.Draw(pil_frame)
            for g in glyphs_to_draw:
                draw_frame.text((g.x, g.y), g.char, fill=g.color, font=g.font)
            frame = cv2.cvtColor(np.array(pil_frame), cv2.COLOR_RGB2BGR)

        return frame, hand_pos

    def render_video_and_sfx(self, output_mp4: Path, narration_wav: Path, bgm_wav: Optional[Path] = None) -> Path:
        output_mp4 = Path(output_mp4)
        output_mp4.parent.mkdir(parents=True, exist_ok=True)
        raw_video = output_mp4.with_name(output_mp4.stem + "_raw.mp4")
        sfx_wav = output_mp4.with_name(output_mp4.stem + "_sfx.wav")
        master_audio = output_mp4.with_name(output_mp4.stem + "_master.wav")

        total_ms = self.spec["totalDurationMs"]
        total_frames = max(1, int(round(total_ms * self.fps / 1000.0)))
        ms_per_frame = 1000.0 / self.fps

        print(f"\n[HyperWhiteboard V4] {self.spec['id']} -> {total_frames} frames ({total_ms/1000:.2f}s) @ {self.fps}fps")
        t0 = time.time()

        base_bgr, schedule = self.build_schedule_and_base()

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        writer = cv2.VideoWriter(str(raw_video), fourcc, self.fps, (self.w, self.h))
        if not writer.isOpened():
            raise RuntimeError(f"Cannot open video writer: {raw_video}")

        # Collect SFX cues automatically
        sfx_cues = []
        # Header whoosh
        sfx_cues.append({"timeMs": schedule["header"].start_ms, "type": "whoosh"})
        sfx_cues.append({"timeMs": schedule["header"].start_ms, "type": "scribble", "durMs": schedule["header"].dur_ms})

        for p_data in schedule["panels"]:
            sfx_cues.append({"timeMs": p_data["startMs"], "type": "pop"})
            sfx_cues.append({"timeMs": p_data["startMs"], "type": "whoosh"})
            for b_obj in p_data["bullets"]:
                for line in b_obj.lines:
                    sfx_cues.append({"timeMs": line.start_ms, "type": "scribble", "durMs": line.dur_ms})
                if b_obj.stat_spec:
                    stat_start = b_obj.lines[-1].end_ms if b_obj.lines else b_obj.start_ms
                    sfx_cues.append({"timeMs": stat_start + 450, "type": "sparkle"})

        # Frame loop
        hand_last_pos = None
        for fi in range(total_frames):
            cur_ms = fi * ms_per_frame
            frame, hand_pos = self.render_frame(cur_ms, base_bgr, schedule)

            if hand_pos is not None:
                frame = self._stamp_hand(frame, hand_pos[0], hand_pos[1])
                hand_last_pos = hand_pos
            elif hand_last_pos is not None and cur_ms > 200:
                # Smoothly retract hand downwards
                hand_last_pos = (hand_last_pos[0], hand_last_pos[1] + 35)
                if hand_last_pos[1] < self.h + self.hand_h:
                    frame = self._stamp_hand(frame, hand_last_pos[0], hand_last_pos[1])
                else:
                    hand_last_pos = None

            writer.write(frame)

        writer.release()
        render_dur = time.time() - t0
        print(f"[HyperWhiteboard V4] Video rendered in {render_dur:.1f}s ({total_frames / max(0.01, render_dur):.1f} fps)")

        # Generate Synchronized SFX Track
        self._build_sfx_track(sfx_cues, total_ms, sfx_wav)

        # Mix Narration + SFX + BGM
        self._mix_audio(narration_wav, sfx_wav, master_audio, bgm_wav)

        # Mux with FFmpeg H.264 High Profile / AAC
        cmd_mux = [
            "ffmpeg", "-y",
            "-i", str(raw_video),
            "-i", str(master_audio),
            "-c:v", "libx264",
            "-preset", "fast",
            "-crf", "18",
            "-pix_fmt", "yuv420p",
            "-c:a", "aac",
            "-b:a", "256k",
            "-shortest",
            str(output_mp4)
        ]
        subprocess.run(cmd_mux, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # Clean intermediate files
        for p in (raw_video, sfx_wav, master_audio):
            p.unlink(missing_ok=True)

        print(f"[HyperWhiteboard V4] MASTER EXPORT COMPLETE: {output_mp4} ({output_mp4.stat().st_size / 1024 / 1024:.2f} MB)")
        return output_mp4

    def _build_sfx_track(self, cues: List[Dict[str, Any]], total_ms: float, out_wav: Path):
        sr = 48000
        total_samples = int((total_ms / 1000.0) * sr)
        mix = np.zeros(total_samples, dtype=np.float32)

        SFX_DIR = Path("assets/sfx")
        SCRIBBLE_WAV = SFX_DIR / "marker-scribble-loop.wav"

        def load_sfx(path: Path) -> np.ndarray:
            if not path.exists():
                return np.zeros(1, dtype=np.float32)
            cmd = ["ffmpeg", "-v", "error", "-i", str(path), "-f", "f32le", "-ac", "1", "-ar", str(sr), "-"]
            proc = subprocess.run(cmd, capture_output=True, check=True)
            return np.frombuffer(proc.stdout, dtype=np.float32)

        pop_snd = load_sfx(SFX_DIR / "pop.mp3") * 0.35
        whoosh_snd = load_sfx(SFX_DIR / "whoosh-short.mp3") * 0.28
        impact_snd = load_sfx(SFX_DIR / "impact-bass-1.mp3") * 0.38
        scribble_snd = load_sfx(SCRIBBLE_WAV) * 0.13
        sparkle_snd = load_sfx(SFX_DIR / "sparkle.mp3") * 0.25

        def stamp_sound(snd: np.ndarray, t_ms: float):
            start = int((t_ms / 1000.0) * sr)
            if start >= total_samples or len(snd) == 0:
                return
            end = min(total_samples, start + len(snd))
            mix[start:end] += snd[:end - start]

        for cue in cues:
            ctype = cue["type"]
            t_ms = cue["timeMs"]
            if ctype == "pop":
                stamp_sound(pop_snd, t_ms)
            elif ctype == "whoosh":
                stamp_sound(whoosh_snd, t_ms)
            elif ctype == "impact":
                stamp_sound(impact_snd, t_ms)
            elif ctype == "sparkle":
                stamp_sound(sparkle_snd, t_ms)
            elif ctype == "scribble" and len(scribble_snd) > 100:
                dur_ms = cue.get("durMs", 1000)
                dur_samples = int((dur_ms / 1000.0) * sr)
                start = int((t_ms / 1000.0) * sr)
                end = min(total_samples, start + dur_samples)
                if end > start:
                    seg_len = end - start
                    looped = np.tile(scribble_snd, int(math.ceil(seg_len / len(scribble_snd))))[:seg_len]
                    fade = min(int(0.04 * sr), seg_len // 2)
                    if fade > 0:
                        looped[:fade] *= np.linspace(0, 1, fade)
                        looped[-fade:] *= np.linspace(1, 0, fade)
                    mix[start:end] += looped

        mix = np.clip(mix, -0.98, 0.98)
        from scipy.io import wavfile
        wavfile.write(str(out_wav), sr, (mix * 32767).astype(np.int16))

    def _mix_audio(self, narration_wav: Path, sfx_wav: Path, out_wav: Path, bgm_wav: Optional[Path] = None):
        if bgm_wav and bgm_wav.exists():
            # Duck BGM under narration
            filter_complex = (
                "[0:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,volume=1.0[voc];"
                "[1:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,volume=0.9[sfx];"
                "[2:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,volume=0.15[bgm];"
                "[bgm][voc]sidechaincompress=threshold=0.08:ratio=5:attack=20:release=300[ducked_bgm];"
                "[voc][sfx][ducked_bgm]amix=inputs=3:weights=1 1 1:normalize=0:duration=first[aout]"
            )
            cmd = [
                "ffmpeg", "-y",
                "-i", str(narration_wav),
                "-i", str(sfx_wav),
                "-stream_loop", "-1", "-i", str(bgm_wav),
                "-filter_complex", filter_complex,
                "-map", "[aout]",
                "-ar", "48000",
                "-ac", "2",
                "-c:a", "pcm_s16le",
                str(out_wav)
            ]
        else:
            filter_complex = (
                "[0:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,volume=1.0[voc];"
                "[1:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,volume=0.9[sfx];"
                "[voc][sfx]amix=inputs=2:weights=1 1:normalize=0:duration=first[aout]"
            )
            cmd = [
                "ffmpeg", "-y",
                "-i", str(narration_wav),
                "-i", str(sfx_wav),
                "-filter_complex", filter_complex,
                "-map", "[aout]",
                "-ar", "48000",
                "-ac", "2",
                "-c:a", "pcm_s16le",
                str(out_wav)
            ]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
