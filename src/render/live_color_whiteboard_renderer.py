"""
Live Color Whiteboard Animation Engine:
"Vẽ tới đâu tô màu liền tới đấy, không phải vẽ xong mới tô"
(Single-pass direct color painting along semantic stroke streams)
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

ROOT = Path(__file__).resolve().parents[2]
SRT_SCRIPTS = ROOT / "tools" / "srt-whiteboard-animation" / "scripts"
sys.path.insert(0, str(SRT_SCRIPTS))
import stream_render as sr

DEFAULT_HAND = ROOT / "tools" / "srt-whiteboard-animation" / "assets" / "user_clean_hand.png"

class LiveColorWhiteboardRenderer:
    def __init__(self, canvas_path: Path, annotation_path: Path, hand_path: Path = DEFAULT_HAND, fps: int = 24):
        self.canvas_path = Path(canvas_path)
        self.annotation_path = Path(annotation_path)
        self.hand_path = Path(hand_path)
        self.fps = fps
        
        self.color_img = cv2.imread(str(self.canvas_path))
        if self.color_img is None:
            raise FileNotFoundError(f"Cannot read canvas image: {canvas_path}")
        self.h, self.w = self.color_img.shape[:2]
        
        with open(self.annotation_path, "r", encoding="utf-8") as f:
            self.ann = json.load(f)
            
        self.elements = sorted(self.ann["elements"], key=lambda e: e["reveal"]["startMs"])
        
        # Load hand rig
        hand_raw = cv2.imread(str(self.hand_path), cv2.IMREAD_UNCHANGED)
        if hand_raw is None:
            raise FileNotFoundError(f"Cannot read hand asset: {self.hand_path}")
        hand_h = 440
        scale = hand_h / hand_raw.shape[0]
        hand_w = int(hand_raw.shape[1] * scale)
        self.hand_resized = cv2.resize(hand_raw, (hand_w, hand_h), interpolation=cv2.INTER_AREA)
        self.hand_bgr = self.hand_resized[:, :, :3]
        self.hand_alpha = (self.hand_resized[:, :, 3] / 255.0)[:, :, None].astype(np.float32)
        self.hand_h = hand_h
        self.hand_w = hand_w
        
        # Exact calibrated tip coordinates for user_clean_hand
        self.tip_x = int(round(9 * scale))
        self.tip_y = int(round(2 * scale))
        
        # Brush disk
        self.brush_r = 28
        y_idx, x_idx = np.ogrid[-self.brush_r:self.brush_r+1, -self.brush_r:self.brush_r+1]
        disk = np.clip(1.0 - np.sqrt(x_idx**2 + y_idx**2) / self.brush_r, 0.0, 1.0)
        self.disk = (disk ** 0.75).astype(np.float32)
        
        # Detect active features
        gray = cv2.cvtColor(self.color_img, cv2.COLOR_BGR2GRAY)
        self.thresh_map = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 10)
        self.grid_edge = 10
        self.active_all = sr._active_mask(self.thresh_map, self.grid_edge, 10)
        self.diff_bg = np.sum(np.abs(self.color_img.astype(np.int16) - np.array([255, 255, 255])), axis=2)

    def _stamp_hand(self, canvas: np.ndarray, px: int, py: int) -> np.ndarray:
        # Align marker tip exactly at (px, py)
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

    def _allowed_mask(self, element: dict, later_elements: list[dict]) -> np.ndarray:
        mask = np.zeros((self.h, self.w), dtype=bool)
        reg = element["region"]
        rx, ry, rw, rh = reg["x"], reg["y"], reg["width"], reg["height"]
        mask[ry:ry+rh, rx:rx+rw] = True
        for later in later_elements:
            lreg = later["region"]
            lx, ly, lw, lh = lreg["x"], lreg["y"], lreg["width"], lreg["height"]
            mask[ly:ly+lh, lx:lx+lw] = False
        return mask

    def _plan_element_path(self, allowed: np.ndarray, reg: dict) -> list[tuple[int, int]]:
        rx, ry, rw, rh = reg["x"], reg["y"], reg["width"], reg["height"]
        allowed_cell = sr._to_grid_blocks(allowed.astype(np.uint8), self.grid_edge).any(axis=(2, 3))
        active = self.active_all & allowed_cell
        
        path_pixels: list[tuple[int, int]] = []
        if active.any():
            streams = sr.cluster_ink_streams(active)
            cells = sr.flatten_streams(streams)
            path_pixels.extend([(c[1] * self.grid_edge + self.grid_edge // 2,
                                 c[0] * self.grid_edge + self.grid_edge // 2) for c in cells])
            visited = set(cells)
        else:
            visited = set()
            
        # Scan remaining content cells in region so background colors are filled
        step = self.grid_edge
        r_start = ry // step
        r_end = (ry + rh) // step + 1
        c_start = rx // step
        c_end = (rx + rw) // step + 1
        
        for r in range(r_start, r_end):
            cols = range(c_start, c_end) if r % 2 == 0 else range(c_end - 1, c_start - 1, -1)
            for c in cols:
                if (r, c) not in visited:
                    y0, y1 = max(0, r * step), min(self.h, (r + 1) * step)
                    x0, x1 = max(0, c * step), min(self.w, (c + 1) * step)
                    if y1 > y0 and x1 > x0 and allowed[y0:y1, x0:x1].any():
                        if self.diff_bg[y0:y1, x0:x1].max() > 20:
                            path_pixels.append((c * step + step // 2, r * step + step // 2))
                            
        return path_pixels

    def render(self, output_mp4: Path, audio_wav: Path | None = None) -> Path:
        output_mp4 = Path(output_mp4)
        output_mp4.parent.mkdir(parents=True, exist_ok=True)
        raw_video = output_mp4.with_name(output_mp4.stem + "_raw.mp4")
        
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        writer = cv2.VideoWriter(str(raw_video), fourcc, self.fps, (self.w, self.h))
        if not writer.isOpened():
            raise RuntimeError(f"Cannot open video writer: {raw_video}")
            
        drawn = np.full((self.h, self.w, 3), 255, dtype=np.float32)
        total_ms = self.ann.get("sceneDurationMs", 0)
        ms_per_frame = 1000.0 / self.fps
        cur_ms = 0.0
        
        def fill_static(until_ms: float):
            nonlocal cur_ms
            n = int(round((until_ms - cur_ms) / ms_per_frame))
            if n <= 0:
                return
            snap = drawn.astype(np.uint8)
            for _ in range(n):
                writer.write(snap)
            cur_ms += n * ms_per_frame
            
        print(f"[LiveColor] Starting render: {len(self.elements)} elements, {total_ms}ms target...")
        t0 = time.time()
        
        brush_r = self.brush_r
        disk = self.disk
        
        for idx, elem in enumerate(self.elements):
            rev = elem["reveal"]
            start_ms = rev["startMs"]
            dur_ms = rev["durationMs"]
            fill_static(start_ms)
            
            allowed = self._allowed_mask(elem, self.elements[idx+1:])
            path = self._plan_element_path(allowed, elem["region"])
            elem_frames = max(1, int(round(dur_ms * self.fps / 1000.0)))
            
            if not path:
                # If no path, directly reveal allowed area
                drawn[allowed] = self.color_img[allowed]
                fill_static(cur_ms + dur_ms)
                continue
                
            steps_per_frame = max(1.0, len(path) / elem_frames)
            pts_idx = 0
            
            for fi in range(elem_frames):
                next_idx = min(len(path), int((fi + 1) * steps_per_frame))
                for pi in range(pts_idx, next_idx):
                    px, py = path[pi]
                    y0, y1 = max(0, py - brush_r), min(self.h, py + brush_r + 1)
                    x0, x1 = max(0, px - brush_r), min(self.w, px + brush_r + 1)
                    
                    by0, by1 = y0 - (py - brush_r), disk.shape[0] - ((py + brush_r + 1) - y1)
                    bx0, bx1 = x0 - (px - brush_r), disk.shape[1] - ((px + brush_r + 1) - x1)
                    
                    m = disk[by0:by1, bx0:bx1] * allowed[y0:y1, x0:x1]
                    m = m[:, :, None]
                    
                    target = drawn[y0:y1, x0:x1]
                    source = self.color_img[y0:y1, x0:x1].astype(np.float32)
                    target[...] = target * (1.0 - m) + source * m
                    
                pts_idx = next_idx
                if pts_idx > 0 and pts_idx <= len(path):
                    cur_px, cur_py = path[min(len(path)-1, pts_idx-1)]
                else:
                    cur_px = elem["region"]["x"] + elem["region"]["width"] // 2
                    cur_py = elem["region"]["y"] + elem["region"]["height"] // 2
                    
                frame = self._stamp_hand(drawn.astype(np.uint8), cur_px, cur_py)
                writer.write(frame)
                
            # Guarantee 100% of this element is cleanly revealed at end of element
            drawn[allowed] = self.color_img[allowed]
            cur_ms += elem_frames * ms_per_frame
            
        # Gaze at the complete artwork
        gaze_until = max(total_ms, cur_ms + 500)
        fill_static(gaze_until)
        writer.release()
        
        print(f"[LiveColor] Silent animation rendered in {time.time() - t0:.1f}s")
        
        # Mux audio if provided
        if audio_wav and Path(audio_wav).exists():
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
            print(f"[LiveColor] Master video with audio exported: {output_mp4}")
        else:
            if raw_video != output_mp4:
                if output_mp4.exists():
                    output_mp4.unlink()
                raw_video.rename(output_mp4)
                
        return output_mp4

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python live_color_whiteboard_renderer.py <canvas.png> <annotation.json> <output.mp4> [audio.wav]")
        sys.exit(1)
    c_p = Path(sys.argv[1])
    a_p = Path(sys.argv[2])
    o_p = Path(sys.argv[3])
    aud_p = Path(sys.argv[4]) if len(sys.argv) >= 5 else None
    renderer = LiveColorWhiteboardRenderer(c_p, a_p)
    renderer.render(o_p, aud_p)
