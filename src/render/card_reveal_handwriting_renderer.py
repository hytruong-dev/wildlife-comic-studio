"""
Card Reveal & Handwriting Whiteboard Renderer
=============================================
Architecture:
1. AI Illustrated Images appear via smooth Pop-in / Card Entrance Animation (Scale 0.85 -> 1.0 with ease-out).
   NO hand scribbling over the artwork!
2. The Hand Rig exclusively writes text (Titles, Subheadings, Bullet Points) from left to right.
3. Micro handwriting jitter on the pen tip for ultra-realistic whiteboard writing.
4. Auto-lowering hand during narration pauses.
"""

import sys
import os
import json
import math
import time
import subprocess
from pathlib import Path
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
HAND_ASSET = ROOT / "tools" / "srt-whiteboard-animation" / "assets" / "user_clean_hand.png"

try:
    FONT_TITLE = ImageFont.truetype("arialbd.ttf", 22)
    FONT_HEADER = ImageFont.truetype("arialbd.ttf", 15)
    FONT_BOLD = ImageFont.truetype("arialbd.ttf", 14)
    FONT_REG = ImageFont.truetype("arial.ttf", 13)
except:
    FONT_TITLE = FONT_HEADER = FONT_BOLD = FONT_REG = ImageFont.load_default()

def ease_out_back(t: float) -> float:
    c1 = 1.70158
    c3 = c1 + 1
    return 1 + c3 * math.pow(t - 1, 3) + c1 * math.pow(t - 1, 2)

def ease_out_cubic(t: float) -> float:
    return 1 - math.pow(1 - t, 3)

class CardRevealHandwritingRenderer:
    def __init__(self, scene_spec: dict, hand_path: Path = HAND_ASSET, fps: int = 24, w: int = 1280, h: int = 720):
        self.spec = scene_spec
        self.fps = fps
        self.w = w
        self.h = h
        self.hand_path = Path(hand_path)
        
        # Load and scale hand rig
        hand_raw = cv2.imread(str(self.hand_path), cv2.IMREAD_UNCHANGED)
        if hand_raw is None:
            raise FileNotFoundError(f"Cannot read hand asset: {self.hand_path}")
        hand_h = 420
        scale = hand_h / hand_raw.shape[0]
        hand_w = int(hand_raw.shape[1] * scale)
        self.hand_resized = cv2.resize(hand_raw, (hand_w, hand_h), interpolation=cv2.INTER_AREA)
        self.hand_bgr = self.hand_resized[:, :, :3]
        self.hand_alpha = (self.hand_resized[:, :, 3] / 255.0)[:, :, None].astype(np.float32)
        self.hand_h = hand_h
        self.hand_w = hand_w
        self.tip_x = int(round(9 * scale))
        self.tip_y = int(round(2 * scale))

    def _stamp_hand(self, canvas: np.ndarray, px: int, py: int) -> np.ndarray:
        top_x = px - self.tip_x
        top_y = py - self.tip_y
        
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

    def render(self, output_mp4: Path, audio_wav: Path) -> Path:
        output_mp4 = Path(output_mp4)
        output_mp4.parent.mkdir(parents=True, exist_ok=True)
        raw_video = output_mp4.with_name(output_mp4.stem + "_raw.mp4")
        
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        writer = cv2.VideoWriter(str(raw_video), fourcc, self.fps, (self.w, self.h))
        if not writer.isOpened():
            raise RuntimeError(f"Cannot open video writer: {raw_video}")

        total_ms = self.spec["totalDurationMs"]
        total_frames = max(1, int(round(total_ms * self.fps / 1000.0)))
        ms_per_frame = 1000.0 / self.fps
        
        print(f"[Renderer] Rendering {total_frames} frames ({total_ms}ms) -> {output_mp4.name}...")
        t0 = time.time()
        
        # Prepare static target images
        base_img, full_target = self._create_canvases()
        
        # We will render frame by frame
        for fi in range(total_frames):
            cur_ms = fi * ms_per_frame
            frame_img, hand_pos = self._render_frame_at_ms(cur_ms, base_img, full_target)
            
            # If hand is active, stamp it
            if hand_pos is not None:
                hx, hy = hand_pos
                frame_with_hand = self._stamp_hand(frame_img, hx, hy)
                writer.write(frame_with_hand)
            else:
                writer.write(frame_img)
                
        writer.release()
        print(f"[Renderer] Silent video generated in {time.time() - t0:.1f}s")
        
        # Mux with FFmpeg
        cmd_mux = [
            "ffmpeg", "-y",
            "-i", str(raw_video),
            "-i", str(audio_wav),
            "-c:v", "libx264",
            "-preset", "fast",
            "-crf", "20",
            "-pix_fmt", "yuv420p",
            "-c:a", "aac",
            "-b:a", "192k",
            "-shortest",
            str(output_mp4)
        ]
        subprocess.run(cmd_mux, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if raw_video.exists():
            try:
                raw_video.unlink()
            except:
                pass
        print(f"[Renderer] Exported master with audio: {output_mp4}")
        return output_mp4

    def _create_canvases(self) -> tuple[np.ndarray, np.ndarray]:
        """
        Creates two canvases:
        1. base_card_canvas: Has the outer rounded cards, headers, and AI photos (NO bullet text).
        2. full_canvas: Has everything including all bullet text.
        """
        # Canvas 1: Base Card Canvas
        base_pil = Image.new("RGB", (self.w, self.h), (255, 255, 255))
        draw_b = ImageDraw.Draw(base_pil)
        
        # Canvas 2: Full Canvas
        full_pil = Image.new("RGB", (self.w, self.h), (255, 255, 255))
        draw_f = ImageDraw.Draw(full_pil)
        
        # 1. Header on Full Canvas
        hdr = self.spec["header"]
        title_text = hdr["text"]
        bbox = draw_f.textbbox((0, 0), title_text, font=FONT_TITLE)
        t_w, t_h = bbox[2] - bbox[0], bbox[3] - bbox[1]
        pad_x, pad_y = 28, 8
        box_w, box_h = t_w + 2 * pad_x, t_h + 2 * pad_y
        box_x0 = (self.w - box_w) // 2
        box_y0 = 10
        box_x1, box_y1 = box_x0 + box_w, box_y0 + box_h
        
        # Both canvases have header box frame
        for d in (draw_b, draw_f):
            d.rounded_rectangle([box_x0, box_y0, box_x1, box_y1], radius=8,
                                fill=(250, 248, 242), outline=(40, 40, 40), width=2)
        # Only full canvas has the header text (so hand writes it)
        draw_f.text((self.w // 2, box_y0 + box_h // 2), title_text, fill=(35, 35, 35), font=FONT_TITLE, anchor="mm")
        
        # 2. Panels
        for panel in self.spec["panels"]:
            box = panel["box"]
            x0, y0, x1, y1 = box
            w, h = x1 - x0, y1 - y0
            color = panel["color"]
            header_bg = panel["header_bg"]
            
            im_raw = Image.open(panel["img_path"]).convert("RGB")
            scale = min((w - 32) / im_raw.width, 280 / im_raw.height)
            iw, ih = int(round(im_raw.width * scale)), int(round(im_raw.height * scale))
            im_scaled = im_raw.resize((iw, ih), Image.Resampling.LANCZOS)
            im_x = x0 + (w - iw) // 2
            im_y = y0 + 44
            
            for d, im_target in ((draw_b, base_pil), (draw_f, full_pil)):
                # Outer frame
                d.rounded_rectangle(box, radius=8, fill=(255, 255, 255), outline=color, width=2)
                # Header bar
                d.rectangle([x0 + 2, y0 + 2, x1 - 2, y0 + 34], fill=header_bg)
                d.text((x0 + 16, y0 + 18), panel["title"], fill=color, font=FONT_HEADER, anchor="lm")
                # Paste Image
                im_target.paste(im_scaled, (im_x, im_y))
                d.rectangle([im_x - 1, im_y - 1, im_x + iw, im_y + ih], outline=(220, 225, 230), width=1)
                d.rounded_rectangle(box, radius=8, outline=color, width=2)
                
            # Add bullet points ONLY to full canvas
            ty = im_y + ih + 18
            tx = x0 + 20
            for bp in panel["bullets"]:
                draw_f.text((tx, ty), bp["title"], fill=bp.get("color", (30, 30, 30)), font=FONT_BOLD)
                ty += 22
                for line in bp["desc"].split("\n"):
                    draw_f.text((tx + 12, ty), line, fill=(70, 70, 70), font=FONT_REG)
                    ty += 18
                ty += bp.get("gap", 8)
                
        base_bgr = cv2.cvtColor(np.array(base_pil), cv2.COLOR_RGB2BGR)
        full_bgr = cv2.cvtColor(np.array(full_pil), cv2.COLOR_RGB2BGR)
        return base_bgr, full_bgr

    def _render_frame_at_ms(self, cur_ms: float, base_img: np.ndarray, full_target: np.ndarray) -> tuple[np.ndarray, tuple[int, int] | None]:
        frame = np.full((self.h, self.w, 3), 255, dtype=np.uint8)
        hand_pos = None
        
        # 1. Header Reveal
        hdr = self.spec["header"]
        h_start, h_dur = hdr["startMs"], hdr["durMs"]
        h_box = hdr.get("box", [280, 10, 1000, 52])
        hx0, hy0, hx1, hy1 = h_box
        
        # Show header box background
        frame[hy0:hy1, hx0:hx1] = base_img[hy0:hy1, hx0:hx1]
        
        if cur_ms >= h_start:
            if cur_ms < h_start + h_dur:
                # Handwriting header text from left to right
                p = (cur_ms - h_start) / h_dur
                reveal_x = int(hx0 + p * (hx1 - hx0))
                frame[hy0:hy1, hx0:reveal_x] = full_target[hy0:hy1, hx0:reveal_x]
                jitter = int(math.sin(p * 20 * math.pi) * 2)
                hand_pos = (reveal_x, (hy0 + hy1) // 2 + jitter)
            else:
                frame[hy0:hy1, hx0:hx1] = full_target[hy0:hy1, hx0:hx1]
                
        # 2. Panels Reveal
        for panel in self.spec["panels"]:
            p_start = panel["startMs"]
            if cur_ms < p_start:
                continue
                
            x0, y0, x1, y1 = panel["box"]
            pw, ph = x1 - x0, y1 - y0
            
            # Card Pop-in Animation (350ms duration)
            card_pop_dur = 350.0
            if cur_ms < p_start + card_pop_dur:
                progress = min(1.0, (cur_ms - p_start) / card_pop_dur)
                scale = 0.88 + 0.12 * ease_out_back(progress)
                
                # Scaled card
                sw = max(1, int(round(pw * scale)))
                sh = max(1, int(round(ph * scale)))
                card_crop = base_img[y0:y1, x0:x1]
                card_scaled = cv2.resize(card_crop, (sw, sh), interpolation=cv2.INTER_LINEAR)
                
                dest_x = x0 + (pw - sw) // 2
                dest_y = y0 + (ph - sh) // 2
                
                dy0, dy1 = max(0, dest_y), min(self.h, dest_y + sh)
                dx0, dx1 = max(0, dest_x), min(self.w, dest_x + sw)
                cy0, cy1 = max(0, -dest_y), min(sh, self.h - dest_y)
                cx0, cx1 = max(0, -dest_x), min(sw, self.w - dest_x)
                
                frame[dy0:dy1, dx0:dx1] = card_scaled[cy0:cy1, cx0:cx1]
            else:
                # Full base card is visible
                frame[y0:y1, x0:x1] = base_img[y0:y1, x0:x1]
                
                # 3. Bullet Points Handwriting (Hand writes line by line)
                for bp in panel["bullets"]:
                    b_start = bp["startMs"]
                    b_dur = bp["durMs"]
                    bx0, by0, bx1, by1 = bp["region"]
                    
                    if cur_ms < b_start:
                        continue
                    elif cur_ms < b_start + b_dur:
                        # Handwriting this bullet point!
                        p = (cur_ms - b_start) / b_dur
                        reveal_x = int(bx0 + p * (bx1 - bx0))
                        frame[by0:by1, bx0:reveal_x] = full_target[by0:by1, bx0:reveal_x]
                        
                        jitter = int(math.sin(p * 25 * math.pi) * 3)
                        hand_pos = (reveal_x, by0 + (by1 - by0) // 2 + jitter)
                    else:
                        # Completely revealed
                        frame[by0:by1, bx0:bx1] = full_target[by0:by1, bx0:bx1]
                        
        return frame, hand_pos
