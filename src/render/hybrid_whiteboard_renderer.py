"""
Hybrid Whiteboard Animation Renderer V6 (Meticulous True-Stroke Ink & Color Engine):
- Unifies the 3 flagship drawing engines (`geeklee/srt-whiteboard-animation`, `masihsultani/whiteboard-animator`, `letuandat131/whiteboard-animation-vi`):
  1. Adaptive Multiscale Ink Extraction (`build_v181d_ink_map` style): Bilateral edge-preserving filter + CLAHE + Adaptive Gaussian Threshold.
  2. Semantic Connected-Component Clustering & Density-Gradient Walk (`cluster_ink_streams` + `_gradient_walk` + `_split_bridge_connected_components`):
     - Never jumps erratically across an artwork! Finishes each contiguous subject/contour component smoothly before moving to the next.
  3. Phase 1 — Precision Line-Art Sketching (55% of drawing time):
     - Pen tip glides along continuous interpolated ink strokes (`sample_step = 2px`), revealing ONLY dark ink outlines (`ink_paint`) right under the nib (`cv2.line` radius 5px + 8x8 cell stamp).
     - Ahead of the pen is 100% pure blank paper!
  4. Phase 2 — Boustrophedon Angled Brush Color Wash (45% of drawing time):
     - Hand switches to angled serpentine brush sweeps across the sketched ink outlines, painting vibrant original colors directly under the moving marker nib with contour resistance.
  5. Discrete Character-Stepped Handwriting & 4-Layer Broadcast Audio (48kHz / 320kbps AAC + Sidechain Ducking).
"""

import sys
import os
import json
import math
import time
import wave
import subprocess
from pathlib import Path
from typing import Dict, List, Any, Tuple, Optional, Sequence

import cv2
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
SRT_SCRIPTS = ROOT / "tools" / "srt-whiteboard-animation" / "scripts"
sys.path.insert(0, str(SRT_SCRIPTS))

DEFAULT_HAND = ROOT / "assets" / "hands" / "hand-marker-right.png"
if not DEFAULT_HAND.exists():
    DEFAULT_HAND = ROOT / "projects" / "tap-01-lung-mat" / "assets" / "user_clean_hand.png"

SFX_DIR = ROOT / "assets" / "sfx"
HYPER_SFX_DIR = ROOT / "tools" / "hyperframes" / "skills" / "media-use" / "audio" / "assets" / "sfx"


def remotion_spring(t: float, duration: float = 0.36, omega: float = 16.0, zeta: float = 0.80) -> float:
    if t <= 0.0:
        return 0.0
    if t >= duration:
        return 1.0
    u = t / duration
    wd = omega * math.sqrt(max(0.001, 1.0 - zeta * zeta))
    decay = math.exp(-zeta * omega * u)
    osc = math.cos(wd * u) + (zeta / math.sqrt(max(0.001, 1.0 - zeta * zeta))) * math.sin(wd * u)
    return max(0.0, min(1.05, 1.0 - decay * osc))


def cubic_bezier_ease(u: float, p1: float = 0.42, p2: float = 0.0, p3: float = 0.22, p4: float = 1.0) -> float:
    """Evaluates a CSS-style 1D Cubic-Bezier curve `cubic-bezier(x1, y1, x2, y2)` at `u in [0, 1]`."""
    if u <= 0.0:
        return 0.0
    if u >= 1.0:
        return 1.0

    def sx(t: float) -> float:
        return 3.0 * (1.0 - t) ** 2 * t * p1 + 3.0 * (1.0 - t) * t ** 2 * p3 + t ** 3

    def sdx(t: float) -> float:
        return 3.0 * (1.0 - t) ** 2 * p1 + 6.0 * (1.0 - t) * t * (p3 - p1) + 3.0 * t ** 2 * (1.0 - p3)

    def sy(t: float) -> float:
        return 3.0 * (1.0 - t) ** 2 * t * p2 + 3.0 * (1.0 - t) * t ** 2 * p4 + t ** 3

    t = u
    for _ in range(6):
        err = sx(t) - u
        if abs(err) < 1e-5:
            break
        d = sdx(t)
        if abs(d) < 1e-6:
            break
        t = max(0.0, min(1.0, t - err / d))
    return max(0.0, min(1.0, sy(t)))


class PanelStrokePlan:
    """Holds the pre-computed Phase 1 (Ink Stream) and Phase 2 (Color Brush Wash) trajectories for a panel."""

    def __init__(
        self,
        rx: int,
        ry: int,
        rw: int,
        rh: int,
        thresh_map: np.ndarray,
        ink_mask: np.ndarray,
        ink_paint: np.ndarray,
        ink_samples: List[Tuple[int, int]],
        ink_lifts: set[int],
        sample_cell_idx: List[int],
        ordered_cells: List[Tuple[int, int]],
        color_samples: List[Tuple[int, int]],
        color_lifts: set[int],
        cell_edge: int = 8,
    ) -> None:
        self.rx = rx
        self.ry = ry
        self.rw = rw
        self.rh = rh
        self.thresh_map = thresh_map
        self.ink_mask = ink_mask
        self.ink_paint = ink_paint
        self.ink_samples = ink_samples
        self.ink_lifts = ink_lifts
        self.sample_cell_idx = sample_cell_idx
        self.ordered_cells = ordered_cells
        self.color_samples = color_samples
        self.color_lifts = color_lifts
        self.cell_edge = cell_edge


class HybridWhiteboardRenderer:
    def __init__(self, spec_path: Path, canvas_path: Path, hand_path: Path = DEFAULT_HAND, fps: int = 24):
        self.spec_path = Path(spec_path)
        self.canvas_path = Path(canvas_path)
        self.hand_path = Path(hand_path)
        self.fps = fps
        self.ms_per_frame = 1000.0 / fps

        with open(self.spec_path, "r", encoding="utf-8") as f:
            self.spec = json.load(f)

        self.color_img = cv2.imread(str(self.canvas_path))
        if self.color_img is None:
            raise FileNotFoundError(f"Cannot read canvas: {self.canvas_path}")
        self.h, self.w = self.color_img.shape[:2]

        # Viewport output resolution (supports Dynamic Multi-Node World Canvas > 1280x720)
        self.out_w = int(self.spec.get("viewport_width", 1280 if self.w > 1280 else self.w))
        self.out_h = int(self.spec.get("viewport_height", 720 if self.h > 720 else self.h))
        self.fixed_header_h = int(self.spec.get("fixed_header_height", 0))
        self.isolate_active_node = bool(self.spec.get("isolate_active_node_during_focus", False))
        self.camera_keyframes: List[Dict[str, Any]] = self.spec.get("camera_keyframes", [])

        self.fixed_hdr_img: Optional[np.ndarray] = None
        hdr_info = self.spec.get("header", {})
        if self.fixed_header_h > 0 and hdr_info.get("header_img"):
            hp = Path(hdr_info["header_img"])
            if hp.exists():
                self.fixed_hdr_img = cv2.imread(str(hp))

        # 1. Clean blank whiteboard paper base
        self.paper_base = self._build_clean_paper_base()

        # 2. Load hand rig + precompute soft drop-shadow alpha (scaled for output viewport)
        hand_raw = cv2.imread(str(self.hand_path), cv2.IMREAD_UNCHANGED)
        if hand_raw is None:
            self.hand_path = DEFAULT_HAND
            hand_raw = cv2.imread(str(self.hand_path), cv2.IMREAD_UNCHANGED)
            if hand_raw is None:
                raise FileNotFoundError(f"Cannot read hand asset: {self.hand_path}")

        self.scale = (self.out_h / 720.0) * 0.70

        self.hand_h = int(round(hand_raw.shape[0] * self.scale))
        self.hand_w = int(round(hand_raw.shape[1] * self.scale))
        self.hand_resized = cv2.resize(hand_raw, (self.hand_w, self.hand_h), interpolation=cv2.INTER_AREA)
        self.hand_bgr = self.hand_resized[:, :, :3]
        self.hand_alpha = (self.hand_resized[:, :, 3] / 255.0)[:, :, None].astype(np.float32)
        raw_a = self.hand_resized[:, :, 3].astype(np.float32) / 255.0
        self.hand_shadow_alpha = (cv2.GaussianBlur(raw_a, (21, 21), 7.0) * 0.16)[:, :, None].astype(np.float32)

        if "marker-right" in str(self.hand_path).lower():
            self.tip_x = int(round(22 * self.scale))
            self.tip_y = int(round(47 * self.scale))
        else:
            self.tip_x = int(round(5 * self.scale))
            self.tip_y = int(round(2 * self.scale))

        # 3. Color Wash Brush Disk (Feathered marker nib for Phase 2 Color Fill)
        # Note: Scaled by Fixed Node Size (720p base), NOT World Canvas height (`self.h`),
        # so multi-row World Canvases never inflate the brush radius!
        self.color_brush_r = 26
        yy, xx = np.ogrid[-self.color_brush_r : self.color_brush_r + 1, -self.color_brush_r : self.color_brush_r + 1]
        d = np.sqrt(xx * xx + yy * yy).astype(np.float32)
        self.color_disk = np.clip(
            1.0 - (d - self.color_brush_r * 0.68) / max(1.0, self.color_brush_r * 0.32), 0.0, 1.0
        )[:, :, None].astype(np.float32)

        self.line_brush_r = 8
        yy_l, xx_l = np.ogrid[-self.line_brush_r : self.line_brush_r + 1, -self.line_brush_r : self.line_brush_r + 1]
        d_l = np.sqrt(xx_l * xx_l + yy_l * yy_l)
        self.line_disk = np.clip((self.line_brush_r - d_l) / 1.5, 0.0, 1.0).astype(np.float32)

    def _interpolate_camera(self, cur_ms: float) -> Tuple[float, float, float, float, str, Optional[str]]:
        """
        Evaluates `(cx, cy, crop_w, crop_h, phase, target_node_id)` in World Coordinates at `cur_ms`
        using Cubic-Bezier easing (`C(0.42, 0.0, 0.22, 1.0)`) between sequential camera keyframes.
        """
        if not self.camera_keyframes:
            return (self.w / 2.0, self.h / 2.0, float(self.w), float(self.h), "static", None)

        kfs = self.camera_keyframes
        if cur_ms <= kfs[0]["time_ms"]:
            k0 = kfs[0]
            return (
                float(k0["cx"]),
                float(k0["cy"]),
                float(k0["crop_w"]),
                float(k0["crop_h"]),
                k0.get("phase", "focus_hold"),
                k0.get("target_node_id"),
            )
        if cur_ms >= kfs[-1]["time_ms"]:
            kl = kfs[-1]
            return (
                float(kl["cx"]),
                float(kl["cy"]),
                float(kl["crop_w"]),
                float(kl["crop_h"]),
                kl.get("phase", "overview_reveal"),
                kl.get("target_node_id"),
            )

        for i in range(len(kfs) - 1):
            k0 = kfs[i]
            k1 = kfs[i + 1]
            t0 = float(k0["time_ms"])
            t1 = float(k1["time_ms"])
            if t0 <= cur_ms <= t1:
                dur = max(1e-3, t1 - t0)
                u = (cur_ms - t0) / dur
                e = cubic_bezier_ease(u, 0.42, 0.0, 0.22, 1.0)
                cx = float(k0["cx"]) + (float(k1["cx"]) - float(k0["cx"])) * e
                cy = float(k0["cy"]) + (float(k1["cy"]) - float(k0["cy"])) * e
                cw = float(k0["crop_w"]) + (float(k1["crop_w"]) - float(k0["crop_w"])) * e
                ch = float(k0["crop_h"]) + (float(k1["crop_h"]) - float(k0["crop_h"])) * e
                # If transitioning to overview_reveal, mark phase as overview_reveal so all nodes are visible!
                if k1.get("target_node_id") == "all_nodes_bbox" or k0.get("phase") == "overview_reveal":
                    phase = "overview_reveal"
                    target_id = "all_nodes_bbox"
                else:
                    phase = k0.get("phase", "focus_hold")
                    target_id = k1.get("target_node_id") if u > 0.5 else k0.get("target_node_id")
                return (cx, cy, cw, ch, phase, target_id)

        kl = kfs[-1]
        return (
            float(kl["cx"]),
            float(kl["cy"]),
            float(kl["crop_w"]),
            float(kl["crop_h"]),
            kl.get("phase", "overview_reveal"),
            kl.get("target_node_id"),
        )

    def _apply_camera_crop(self, world_frame: np.ndarray, cx: float, cy: float, cw: float, ch: float, target_w: int, target_h: int) -> Tuple[np.ndarray, float, float, float]:
        """
        Crops `(cx, cy, cw, ch)` from `world_frame` with subpixel-smooth bilinear/area resampling
        to `(target_w, target_h)` and returns `(viewport_frame, x0, y0, scale_world_to_view)`.
        Guarantees that `(cx, cy)` is mapped precisely to `(target_w / 2, target_h / 2)`.
        """
        if not self.camera_keyframes and self.w == target_w and self.h == target_h:
            return (world_frame, 0.0, 0.0, 1.0)

        cw = max(160.0, cw)
        ch = max(90.0, ch)
        x0 = cx - cw / 2.0
        y0 = cy - ch / 2.0

        # Use warpAffine for sub-pixel smooth camera panning and zooming (zero integer jitter!)
        scale_x = target_w / cw
        scale_y = target_h / ch
        M = np.array(
            [
                [scale_x, 0.0, -x0 * scale_x],
                [0.0, scale_y, -y0 * scale_y],
            ],
            dtype=np.float32,
        )
        interp = cv2.INTER_AREA if scale_x < 1.0 else cv2.INTER_LINEAR
        view = cv2.warpAffine(
            world_frame,
            M,
            (target_w, target_h),
            flags=interp,
            borderMode=cv2.BORDER_CONSTANT,
            borderValue=(255, 255, 255),
        )
        return (view, x0, y0, scale_x)

    def _build_clean_paper_base(self) -> np.ndarray:
        corner_sample = self.color_img[4:24, 4:24]
        med_bgr = np.median(corner_sample.reshape(-1, 3), axis=0).astype(np.uint8)
        return np.full((self.h, self.w, 3), med_bgr, dtype=np.uint8)

    def _stamp_hand(self, canvas: np.ndarray, px: int, py: int, lift_px: float = 0.0) -> np.ndarray:
        out = canvas.copy()
        canv_h, canv_w = out.shape[:2]
        top_x = px - self.tip_x
        top_y = py - self.tip_y

        sh_offset_x = int(round(7 + abs(lift_px) * 0.30))
        sh_offset_y = int(round(9 + abs(lift_px) * 0.45))
        sx0 = top_x + sh_offset_x
        sy0 = top_y + sh_offset_y
        sc_x0 = max(0, sx0)
        sc_y0 = max(0, sy0)
        sc_x1 = min(canv_w, sx0 + self.hand_w)
        sc_y1 = min(canv_h, sy0 + self.hand_h)
        if sc_x1 > sc_x0 and sc_y1 > sc_y0:
            sh_x0 = sc_x0 - sx0
            sh_y0 = sc_y0 - sy0
            sh_x1 = sh_x0 + (sc_x1 - sc_x0)
            sh_y1 = sh_y0 + (sc_y1 - sc_y0)
            sa = self.hand_shadow_alpha[sh_y0:sh_y1, sh_x0:sh_x1]
            out[sc_y0:sc_y1, sc_x0:sc_x1] = (out[sc_y0:sc_y1, sc_x0:sc_x1].astype(np.float32) * (1.0 - sa)).astype(
                np.uint8
            )

        c_x0 = max(0, top_x)
        c_y0 = max(0, top_y)
        c_x1 = min(canv_w, top_x + self.hand_w)
        c_y1 = min(canv_h, top_y + self.hand_h)

        if c_x1 <= c_x0 or c_y1 <= c_y0:
            return out

        h_x0 = c_x0 - top_x
        h_y0 = c_y0 - top_y
        h_x1 = h_x0 + (c_x1 - c_x0)
        h_y1 = h_y0 + (c_y1 - c_y0)

        hb = self.hand_bgr[h_y0:h_y1, h_x0:h_x1]
        ha = self.hand_alpha[h_y0:h_y1, h_x0:h_x1]
        out[c_y0:c_y1, c_x0:c_x1] = (out[c_y0:c_y1, c_x0:c_x1] * (1.0 - ha) + hb * ha).astype(np.uint8)
        return out

    def _stamp_brush(
        self,
        drawn: np.ndarray,
        px: int,
        py: int,
        r: int,
        disk: np.ndarray,
        clip_rect: Optional[Tuple[int, int, int, int]] = None,
    ):
        if clip_rect is not None:
            cx0, cy0, cx1, cy1 = clip_rect
            y0, y1 = max(cy0, py - r), min(cy1, py + r + 1)
            x0, x1 = max(cx0, px - r), min(cx1, px + r + 1)
        else:
            y0, y1 = max(0, py - r), min(self.h, py + r + 1)
            x0, x1 = max(0, px - r), min(self.w, px + r + 1)
        if y1 <= y0 or x1 <= x0:
            return
        by0, by1 = y0 - (py - r), disk.shape[0] - ((py + r + 1) - y1)
        bx0, bx1 = x0 - (px - r), disk.shape[1] - ((px + r + 1) - x1)
        m = disk[by0:by1, bx0:bx1]
        if m.ndim == 2:
            m = m[:, :, None]
        drawn[y0:y1, x0:x1] = (drawn[y0:y1, x0:x1] * (1.0 - m) + self.color_img[y0:y1, x0:x1] * m).astype(np.uint8)

    # ──────────────────────────────────────────────────────────────────────────
    # V6 TRUE-STROKE INK & COLOR PLANNER (Adapted from stream_render.py + v181d)
    # ──────────────────────────────────────────────────────────────────────────
    @staticmethod
    def _extract_clean_ink_map(sub_bgr: np.ndarray, paper_sub: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Extracts clean black/charcoal line-art from an illustration region (`v181d` + `stream_render` method):
        Returns:
          - thresh_map (H, W) uint8: 0..255 line-art intensity on white
          - ink_mask (H, W) bool: True where stroke ink exists
          - content_mask (H, W) bool: True where any non-paper artwork pixel exists
        """
        diff = np.max(np.abs(sub_bgr.astype(np.int16) - paper_sub.astype(np.int16)), axis=2)
        content_mask = diff > 14

        gray = cv2.cvtColor(sub_bgr, cv2.COLOR_BGR2GRAY)
        smooth = cv2.bilateralFilter(gray, 7, 18, 5)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8)).apply(smooth)
        adapt = cv2.adaptiveThreshold(
            clahe, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 9
        )
        # Also include genuinely dark pixels (luminance < 115) inside content
        dark_mask = (gray < 115) & content_mask
        ink_mask = ((adapt == 0) & content_mask) | dark_mask

        # Filter tiny 1-2px isolated noise specks
        n_cc, labels, stats, _ = cv2.connectedComponentsWithStats(ink_mask.astype(np.uint8), connectivity=8)
        if n_cc > 1:
            keep = (stats[:, cv2.CC_STAT_AREA] >= 3) | (
                np.maximum(stats[:, cv2.CC_STAT_WIDTH], stats[:, cv2.CC_STAT_HEIGHT]) >= 3
            )
            keep[0] = False
            ink_mask = keep[labels]

        # Build crisp charcoal-on-paper paint layer so Phase 1 looks like authentic marker/ink line-art
        thresh_map = np.full(gray.shape, 255, dtype=np.uint8)
        thresh_map[ink_mask] = np.clip(gray[ink_mask] * 0.55 + 18, 18, 125).astype(np.uint8)
        return thresh_map, ink_mask, content_mask

    @staticmethod
    def _gradient_walk_component(cells: Sequence[Tuple[int, int]]) -> List[Tuple[int, int]]:
        """
        Walks along a connected ink component choosing the highest local density neighbor
        with minimal turn angle (`_gradient_walk` from `srt-whiteboard-animation`).
        """
        if not cells:
            return []
        cell_set = set(cells)
        # Start from highest local density cell near top-left
        best_seed = min(
            cells,
            key=lambda rc: (
                -sum(
                    1
                    for dr in (-1, 0, 1)
                    for dc in (-1, 0, 1)
                    if (rc[0] + dr, rc[1] + dc) in cell_set
                ),
                rc[0] + rc[1],
            ),
        )
        visited = {best_seed}
        path = [best_seed]
        cur = best_seed
        prev_dir = (0, 0)

        while len(visited) < len(cells):
            neighbors = [
                (cur[0] + dr, cur[1] + dc)
                for dr in (-1, 0, 1)
                for dc in (-1, 0, 1)
                if (dr != 0 or dc != 0)
                and (cur[0] + dr, cur[1] + dc) in cell_set
                and (cur[0] + dr, cur[1] + dc) not in visited
            ]
            if neighbors:
                def cost(nb: Tuple[int, int]) -> Tuple[int, int, int, int]:
                    local_d = sum(
                        1
                        for dr in (-1, 0, 1)
                        for dc in (-1, 0, 1)
                        if (nb[0] + dr, nb[1] + dc) in cell_set and (nb[0] + dr, nb[1] + dc) not in visited
                    )
                    step = (nb[0] - cur[0], nb[1] - cur[1])
                    turn = (step[0] - prev_dir[0]) ** 2 + (step[1] - prev_dir[1]) ** 2
                    return (-local_d, turn, nb[0], nb[1])

                nxt = min(neighbors, key=cost)
            else:
                unvisited = [c for c in cells if c not in visited]
                nxt = min(unvisited, key=lambda c: ((c[0] - cur[0]) ** 2 + (c[1] - cur[1]) ** 2, c[0], c[1]))

            prev_dir = (nxt[0] - cur[0], nxt[1] - cur[1])
            path.append(nxt)
            visited.add(nxt)
            cur = nxt

        return path

    def _plan_panel_strokes(self, reg: Dict[str, int]) -> PanelStrokePlan:
        """
        Builds a complete 2-Phase Drawing Plan for an illustration region:
          - Phase 1: Connected-component Ink Stream (`ink_samples`)
          - Phase 2: Boustrophedon Angled Color Wash (`color_samples`)
        """
        rx, ry, rw, rh = reg["x"], reg["y"], reg["width"], reg["height"]
        sub_bgr = self.color_img[ry : ry + rh, rx : rx + rw]
        paper_sub = self.paper_base[ry : ry + rh, rx : rx + rw]

        thresh_map, ink_mask, content_mask = self._extract_clean_ink_map(sub_bgr, paper_sub)
        ink_paint = np.repeat(thresh_map[:, :, None], 3, axis=2)

        edge = 8
        rows = max(1, math.ceil(rh / edge))
        cols = max(1, math.ceil(rw / edge))
        active = np.zeros((rows, cols), dtype=np.uint8)
        for r in range(rows):
            y0, y1 = r * edge, min(rh, (r + 1) * edge)
            for c in range(cols):
                x0, x1 = c * edge, min(rw, (c + 1) * edge)
                if ink_mask[y0:y1, x0:x1].any():
                    active[r, c] = 1

        # 1. Connected component clustering + small speck merging
        n_comp, labels = cv2.connectedComponents(active, connectivity=8)
        components: List[List[Tuple[int, int]]] = []
        for cid in range(1, n_comp):
            pts = np.argwhere(labels == cid)
            if len(pts) > 0:
                components.append([(int(p[0]), int(p[1])) for p in pts])

        if len(components) > 1:
            big = [c for c in components if len(c) > 3]
            small = [c for c in components if len(c) <= 3]
            if big and small:
                centroids = [(sum(p[0] for p in c) / len(c), sum(p[1] for p in c) / len(c)) for c in big]
                for sc in small:
                    sr = sum(p[0] for p in sc) / len(sc)
                    scol = sum(p[1] for p in sc) / len(sc)
                    best_i = min(range(len(big)), key=lambda i: (centroids[i][0] - sr) ** 2 + (centroids[i][1] - scol) ** 2)
                    big[best_i].extend(sc)
                components = big

        # Walk each component with density-gradient walk, then chain components by closest endpoint
        streams = [self._gradient_walk_component(comp) for comp in components if comp]
        # Sort initial stream: largest main subject first
        streams.sort(key=lambda s: -len(s))

        ordered_cells: List[Tuple[int, int]] = []
        tail: Optional[Tuple[int, int]] = None
        remaining = list(streams)
        while remaining:
            if tail is None:
                pick_idx = 0
            else:
                pick_idx = min(
                    range(len(remaining)),
                    key=lambda i: min(
                        (remaining[i][0][0] - tail[0]) ** 2 + (remaining[i][0][1] - tail[1]) ** 2,
                        (remaining[i][-1][0] - tail[0]) ** 2 + (remaining[i][-1][1] - tail[1]) ** 2,
                    ),
                )
            stream = remaining.pop(pick_idx)
            if tail is not None and len(stream) > 1:
                d_head = (stream[0][0] - tail[0]) ** 2 + (stream[0][1] - tail[1]) ** 2
                d_end = (stream[-1][0] - tail[0]) ** 2 + (stream[-1][1] - tail[1]) ** 2
                if d_end < d_head:
                    stream = stream[::-1]
            ordered_cells.extend(stream)
            tail = stream[-1]

        # Build finely interpolated pixel trajectory (sample_step = 3px) for Phase 1 Ink Drawing
        def cell_to_canvas_xy(cell: Tuple[int, int]) -> Tuple[int, int]:
            r, c = cell
            cx = rx + min(rw - 1, c * edge + edge // 2)
            cy = ry + min(rh - 1, r * edge + edge // 2)
            return (cx, cy)

        ink_samples: List[Tuple[int, int]] = []
        ink_lifts: set[int] = set()
        sample_cell_idx: List[int] = []
        sample_step = 3.0

        for idx, cell in enumerate(ordered_cells):
            cx, cy = cell_to_canvas_xy(cell)
            if idx == 0:
                ink_samples.append((cx, cy))
                sample_cell_idx.append(idx)
                continue
            prev_cell = ordered_cells[idx - 1]
            px, py = cell_to_canvas_xy(prev_cell)
            cell_dist = math.hypot(cell[0] - prev_cell[0], cell[1] - prev_cell[1])
            if cell_dist > 2.2:
                ink_lifts.add(len(ink_samples))
                ink_samples.append((cx, cy))
                sample_cell_idx.append(idx)
                continue
            steps = max(1, int(round(math.hypot(cx - px, cy - py) / sample_step)))
            for s in range(1, steps + 1):
                ix = int(round(px + (cx - px) * s / steps))
                iy = int(round(py + (cy - py) * s / steps))
                ink_samples.append((ix, iy))
                sample_cell_idx.append(idx)

        # 2. Build Phase 2 Boustrophedon (Serpentine) Color Wash Trajectory across content pixels
        color_samples: List[Tuple[int, int]] = []
        color_lifts: set[int] = set()
        band_step = max(16, int(round(self.color_brush_r * 0.72)))
        col_step = 6

        lane_idx = 0
        for by in range(band_step // 2, rh, band_step):
            y0 = max(0, by - band_step // 2)
            y1 = min(rh, by + band_step // 2)
            band_mask = content_mask[y0:y1, :]
            active_xs = np.where(band_mask.any(axis=0))[0]
            if len(active_xs) < 4:
                continue
            x_min_b = int(active_xs.min())
            x_max_b = int(active_xs.max())
            xs = (
                list(range(x_min_b, x_max_b + 1, col_step))
                if (lane_idx % 2 == 0)
                else list(range(x_max_b, x_min_b - 1, -col_step))
            )
            if not xs:
                continue
            if color_samples:
                color_lifts.add(len(color_samples))
            for x_local in xs:
                # Subtle organic hand wave during serpentine shading
                wave_y = int(round(2.5 * math.sin(x_local * 0.08 + lane_idx)))
                cy_canvas = ry + max(0, min(rh - 1, by + wave_y))
                cx_canvas = rx + x_local
                color_samples.append((cx_canvas, cy_canvas))
            lane_idx += 1

        return PanelStrokePlan(
            rx=rx,
            ry=ry,
            rw=rw,
            rh=rh,
            thresh_map=thresh_map,
            ink_mask=ink_mask,
            ink_paint=ink_paint,
            ink_samples=ink_samples,
            ink_lifts=ink_lifts,
            sample_cell_idx=sample_cell_idx,
            ordered_cells=ordered_cells,
            color_samples=color_samples,
            color_lifts=color_lifts,
            cell_edge=edge,
        )

    def _reveal_ink_step(
        self,
        drawn: np.ndarray,
        plan: PanelStrokePlan,
        pt_start: Tuple[int, int],
        pt_end: Tuple[int, int],
    ) -> None:
        """Reveals ONLY crisp line-art ink pixels touched by the moving pen segment."""
        rx, ry, rw, rh = plan.rx, plan.ry, plan.rw, plan.rh
        r_rad = 6
        x0 = max(0, min(pt_start[0], pt_end[0]) - rx - r_rad)
        x1 = min(rw, max(pt_start[0], pt_end[0]) - rx + r_rad + 1)
        y0 = max(0, min(pt_start[1], pt_end[1]) - ry - r_rad)
        y1 = min(rh, max(pt_start[1], pt_end[1]) - ry + r_rad + 1)
        if x1 <= x0 or y1 <= y0:
            return

        seg_mask = np.zeros((y1 - y0, x1 - x0), dtype=np.uint8)
        p0 = (pt_start[0] - rx - x0, pt_start[1] - ry - y0)
        p1 = (pt_end[0] - rx - x0, pt_end[1] - ry - y0)
        cv2.line(seg_mask, p0, p1, 255, thickness=r_rad * 2 + 1, lineType=cv2.LINE_AA)

        sub_ink = plan.ink_mask[y0:y1, x0:x1]
        reveal = (seg_mask > 0) & sub_ink
        if reveal.any():
            target = drawn[ry + y0 : ry + y1, rx + x0 : rx + x1]
            paint = plan.ink_paint[y0:y1, x0:x1]
            target[reveal] = paint[reveal]

    def _stamp_ink_cell(self, drawn: np.ndarray, plan: PanelStrokePlan, cell: Tuple[int, int]) -> None:
        """Stamps the complete 8x8 ink block right as the pen finishes traversing that cell."""
        r, c = cell
        e = plan.cell_edge
        y0, y1 = r * e, min(plan.rh, (r + 1) * e)
        x0, x1 = c * e, min(plan.rw, (c + 1) * e)
        sub_ink = plan.ink_mask[y0:y1, x0:x1]
        if sub_ink.any():
            target = drawn[plan.ry + y0 : plan.ry + y1, plan.rx + x0 : plan.rx + x1]
            paint = plan.ink_paint[y0:y1, x0:x1]
            target[sub_ink] = paint[sub_ink]

    def _plan_pill_frame_path(self, box: List[int]) -> List[Tuple[int, int]]:
        bx0, by0, bx1, by1 = box
        pts = []
        step = 14
        for x in range(bx0, bx1, step):
            pts.append((x, by0))
        pts.append((bx1, by0))
        for y in range(by0, by1, step):
            pts.append((bx1, y))
        pts.append((bx1, by1))
        for x in range(bx1, bx0, -step):
            pts.append((x, by1))
        pts.append((bx0, by1))
        for y in range(by1, by0, -step):
            pts.append((bx0, y))
        pts.append((bx0, by0))
        return pts

    def render(self, output_mp4: Path, audio_wav: Path | None = None) -> Path:
        output_mp4 = Path(output_mp4)
        output_mp4.parent.mkdir(parents=True, exist_ok=True)
        raw_video = output_mp4.with_name(output_mp4.stem + "_raw.mp4")

        total_ms = self.spec.get("duration_ms", 60000)
        total_frames = int(round(total_ms / self.ms_per_frame))

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        writer = cv2.VideoWriter(str(raw_video), fourcc, self.fps, (self.out_w, self.out_h))
        if not writer.isOpened():
            raise RuntimeError(f"Cannot open video writer: {raw_video}")

        drawn = self.paper_base.copy()
        sketch_active = [False] * total_frames
        text_active = [False] * total_frames
        sfx_events: List[Dict[str, Any]] = [{"time_ms": 0.0, "type": "page_whoosh"}]

        # Header spec
        hdr = self.spec.get("header", {})
        is_fixed_hdr = bool(hdr.get("fixed_viewport_header", False)) and (self.fixed_hdr_img is not None)
        hdr_has_box = hdr.get("has_box", False)
        hdr_box = hdr.get("box", [100, 10, 1180, 50])
        hbx0, hby0, hbx1, hby1 = hdr_box
        hdr_text_x = hdr.get("x", 200)
        hdr_text_y = hdr.get("y", 16)
        hdr_text_w = hdr.get("w", 880)
        hdr_text_h = hdr.get("h", 26)
        hdr_path = self._plan_pill_frame_path(hdr_box) if (hdr_has_box and not is_fixed_hdr) else []

        if not is_fixed_hdr:
            clean_hdr_pill = self.color_img[hby0:hby1, hbx0:hbx1].copy()
            rel_tx0 = max(0, hdr_text_x - hbx0 - 2)
            rel_tx1 = min(clean_hdr_pill.shape[1], hdr_text_x + hdr_text_w - hbx0 + 2)
            rel_ty0 = max(0, hdr_text_y - hby0 - 2)
            rel_ty1 = min(clean_hdr_pill.shape[0], hdr_text_y + hdr_text_h - hby0 + 4)
            clean_hdr_pill[rel_ty0:rel_ty1, rel_tx0:rel_tx1] = self.paper_base[
                hby0 + rel_ty0 : hby0 + rel_ty1, hbx0 + rel_tx0 : hbx0 + rel_tx1
            ]

        panels = self.spec["panels"]
        panel_schedules = {}
        panel_plans: Dict[str, PanelStrokePlan] = {}

        hdr_w = hdr.get("w", 0)
        hdr_write_dur = 0.0 if is_fixed_hdr else (1100.0 if hdr_w > 0 else 0.0)

        for idx, p in enumerate(panels):
            p_id = p["id"]
            raw_start = p["start_ms"]
            p_start = max(hdr_write_dur, float(raw_start)) if idx == 0 else float(raw_start)
            p_end = float(p["end_ms"])
            p_dur = max(500.0, p_end - p_start)

            pill_box = p.get("pill_box")
            pill_dur = 340.0 if pill_box else 0.0
            t_pill_end = p_start + pill_dur

            plan = self._plan_panel_strokes(p["img_region"])
            panel_plans[p_id] = plan

            # Step 1: Pill Badge Spring Pop (p_start -> t_pill_end)
            sfx_events.append({"time_ms": p_start, "type": "pop"})
            if idx == 0:
                sfx_events.append({"time_ms": p_start, "type": "impact"})

            # Step 2: 2-Phase True-Stroke Drawing (56% Ink Line-Art + 44% Color Brush Wash)
            t_img_start = t_pill_end
            img_total_dur = max(1000.0, (p_dur - pill_dur) * 0.76)
            t_ink_end = t_img_start + img_total_dur * 0.56
            t_img_end = t_img_start + img_total_dur

            # Step 3: Discrete Character-Stepped Caption Handwriting
            ht = p.get("header_title") or p.get("caption")
            if ht and ht.get("text"):
                t_cap_start = t_img_end
                t_cap_end = min(p_end - 250.0, t_cap_start + max(800.0, (p_dur - pill_dur) * 0.17))
            else:
                t_cap_start = t_img_end
                t_cap_end = t_img_end

            if idx + 1 < len(panels):
                sfx_events.append({"time_ms": t_cap_end, "type": "transit_whoosh"})

            panel_schedules[p_id] = {
                "p_start": p_start,
                "p_end": p_end,
                "t_pill_end": t_pill_end,
                "t_img_start": t_img_start,
                "t_ink_end": t_ink_end,
                "t_img_end": t_img_end,
                "t_cap_start": t_cap_start,
                "t_cap_end": t_cap_end,
                "next_panel": panels[idx + 1] if idx + 1 < len(panels) else None,
            }

        hdr_frame_drawn_idx = 0
        ink_sample_drawn_idx = {p["id"]: 0 for p in panels}
        ink_cell_drawn_idx = {p["id"]: 0 for p in panels}
        color_sample_drawn_idx = {p["id"]: 0 for p in panels}
        ink_completed = {p["id"]: False for p in panels}

        # Preload and style B-Roll Wildlife Clips for active in-card playback
        broll_cache: Dict[str, List[np.ndarray]] = {}
        for p in panels:
            p_id = p["id"]
            bv = p.get("broll_video")
            if bv and Path(bv).exists():
                im_r = p["img_region"]
                iw, ih = im_r["width"], im_r["height"]
                cap = cv2.VideoCapture(str(bv))
                frames = []
                while True:
                    ret, vf = cap.read()
                    if not ret or vf is None:
                        break
                    v_res = cv2.resize(vf, (iw, ih), interpolation=cv2.INTER_AREA)

                    # Add sleek semi-transparent pill badge: "[TƯ LIỆU THỰC TẾ]"
                    badge_w, badge_h = 168, 26
                    bx = iw - badge_w - 10
                    by = 10
                    if bx > 0 and by + badge_h < ih:
                        sub = v_res[by : by + badge_h, bx : bx + badge_w].astype(np.float32)
                        overlay = np.full((badge_h, badge_w, 3), (20, 20, 20), dtype=np.float32)
                        blended = (sub * 0.35 + overlay * 0.65).astype(np.uint8)
                        v_res[by : by + badge_h, bx : bx + badge_w] = blended
                        cv2.rectangle(v_res, (bx, by), (bx + badge_w, by + badge_h), (255, 255, 255), 1)
                        cv2.putText(
                            v_res,
                            "TU LIEU THUC TE",
                            (bx + 14, by + 18),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.45,
                            (255, 255, 255),
                            1,
                            cv2.LINE_AA,
                        )

                    # Clean subtle 1px frame border
                    cv2.rectangle(v_res, (0, 0), (iw - 1, ih - 1), (220, 220, 220), 1)
                    frames.append(v_res)
                cap.release()
                if frames:
                    broll_cache[p_id] = frames
                    print(f"  [B-Roll Preloaded] {p_id} -> {len(frames)} frames ({Path(bv).name})")

        last_px = self.w // 2
        last_py = self.h // 2

        print(f"[HybridRenderer V6] Rendering {total_frames} frames ({total_ms}ms) -> {raw_video.name}...")
        t0 = time.time()

        glyph_step = 9

        for fi in range(total_frames):
            cur_ms = fi * self.ms_per_frame
            cur_px = last_px
            cur_py = last_py
            cur_lift = 0.0
            is_sketching = False
            is_text_writing = False
            overlay_patches: List[Tuple[int, int, np.ndarray]] = []

            # --- 1. HEADER LOGIC ---
            if is_fixed_hdr:
                pass
            elif hdr_has_box:
                if cur_ms < 500:
                    u = cur_ms / 500.0
                    target_idx = min(len(hdr_path), int(round(u * len(hdr_path))))
                    for pi in range(hdr_frame_drawn_idx, target_idx):
                        px, py = hdr_path[pi]
                        self._stamp_brush(drawn, px, py, self.line_brush_r, self.line_disk)
                    hdr_frame_drawn_idx = target_idx
                    if target_idx > 0:
                        cur_px, cur_py = hdr_path[target_idx - 1]
                    is_text_writing = True
                elif cur_ms < 2000:
                    drawn[hby0:hby1, hbx0:hbx1] = clean_hdr_pill
                    u = min(1.0, max(0.0, (cur_ms - 500.0) / 1500.0))
                    raw_tx = hdr_text_x + u * hdr_text_w
                    stepped_tx = hdr_text_x + ((int(round(raw_tx - hdr_text_x)) // glyph_step) * glyph_step)
                    base_y = hdr_text_y + hdr_text_h * 0.58
                    x_start = int(hdr_text_x)
                    x_end = min(self.w, int(stepped_tx))
                    r0 = max(0, int(hdr_text_y - 2))
                    r1 = min(self.h, int(hdr_text_y + hdr_text_h + 4))
                    if x_end > x_start:
                        drawn[r0:r1, x_start:x_end] = self.color_img[r0:r1, x_start:x_end]
                    cur_px = int(round(raw_tx))
                    cur_py = int(round(base_y + 2.0 * math.sin(raw_tx * 0.48)))
                    is_text_writing = True
                else:
                    drawn[hby0:hby1, hbx0:hbx1] = self.color_img[hby0:hby1, hbx0:hbx1]
            else:
                if hdr_text_w > 0:
                    if cur_ms < hdr_write_dur:
                        u = min(1.0, max(0.0, cur_ms / hdr_write_dur))
                        raw_tx = hdr_text_x + u * hdr_text_w
                        stepped_tx = hdr_text_x + ((int(round(raw_tx - hdr_text_x)) // glyph_step) * glyph_step)
                        base_y = hdr_text_y + hdr_text_h * 0.58
                        x_start = int(hdr_text_x)
                        x_end = min(self.w, int(stepped_tx))
                        r0 = max(0, int(hdr_text_y - 2))
                        r1 = min(self.h, int(hdr_text_y + hdr_text_h + 4))
                        if x_end > x_start:
                            drawn[r0:r1, x_start:x_end] = self.color_img[r0:r1, x_start:x_end]
                        cur_px = int(round(raw_tx))
                        cur_py = int(round(base_y + 2.0 * math.sin(raw_tx * 0.48)))
                        is_text_writing = True
                    else:
                        r0 = max(0, int(hdr_text_y - 2))
                        r1 = min(self.h, int(hdr_text_y + hdr_text_h + 4))
                        drawn[r0:r1, int(hdr_text_x) : int(hdr_text_x + hdr_text_w)] = self.color_img[
                            r0:r1, int(hdr_text_x) : int(hdr_text_x + hdr_text_w)
                        ]

            if hdr_text_w > 0 and cur_ms < hdr_write_dur:
                pass
            else:
                # --- 2. PANELS LOGIC ---
                for p in panels:
                    p_id = p["id"]
                    sch = panel_schedules[p_id]
                    plan = panel_plans[p_id]
                    p_start = sch["p_start"]
                    p_end = sch["p_end"]

                    if cur_ms < p_start:
                        continue

                    pbx0, pby0, pbx1, pby1 = p["box"]

                    if cur_ms >= p_end:
                        drawn[pby0:pby1, pbx0:pbx1] = self.color_img[pby0:pby1, pbx0:pbx1]
                        continue

                    # A. Pill Badge Remotion Spring Pop (p_start -> t_pill_end)
                    pill_box = p.get("pill_box")
                    if pill_box:
                        px0, py0, px1, py1 = pill_box
                        if cur_ms < sch["t_pill_end"]:
                            t_sec = (cur_ms - p_start) / 1000.0
                            sp = remotion_spring(t_sec, duration=(sch["t_pill_end"] - p_start) / 1000.0)
                            scale = 0.80 + 0.20 * sp
                            pw, ph = max(2, px1 - px0), max(2, py1 - py0)
                            sw = max(2, int(round(pw * scale)))
                            sh = max(2, int(round(ph * scale)))
                            crop = self.color_img[py0:py1, px0:px1]
                            scaled = cv2.resize(crop, (sw, sh), interpolation=cv2.INTER_LANCZOS4)
                            dx = max(0, min(self.w - sw, px0 + (pw - sw) // 2))
                            dy = max(0, min(self.h - sh, py0 + (ph - sh) // 2))
                            overlay_patches.append((dx, dy, scaled))
                            if plan.ink_samples:
                                cur_px, cur_py = plan.ink_samples[0]
                            else:
                                cur_px = (px0 + px1) // 2
                                cur_py = py1 + 20
                            cur_lift = -14.0 * math.sin(min(1.0, t_sec / 0.34) * math.pi)
                            break
                        else:
                            drawn[py0:py1, px0:px1] = self.color_img[py0:py1, px0:px1]

                    # B1. PHASE 1 — Precision Connected-Stream Line-Art Sketching (t_img_start -> t_ink_end)
                    # Ahead of the pen nib is 100% pure blank paper! Only ink touched by the pen appears!
                    if cur_ms <= sch["t_ink_end"]:
                        ink_dur = max(1.0, sch["t_ink_end"] - sch["t_img_start"])
                        u_ink = min(1.0, max(0.0, (cur_ms - sch["t_img_start"]) / ink_dur))
                        samples = plan.ink_samples
                        n_samp = len(samples)
                        if n_samp > 0:
                            target_si = min(n_samp - 1, int(round(u_ink * (n_samp - 1))))
                            last_si = ink_sample_drawn_idx[p_id]
                            if last_si == 0 and target_si >= 0:
                                self._reveal_ink_step(drawn, plan, samples[0], samples[0])
                            for si in range(last_si + 1, target_si + 1):
                                if si not in plan.ink_lifts:
                                    self._reveal_ink_step(drawn, plan, samples[si - 1], samples[si])
                            ink_sample_drawn_idx[p_id] = target_si

                            # Also stamp completed 8x8 ink cells up to current pen position
                            target_ci = plan.sample_cell_idx[target_si]
                            while ink_cell_drawn_idx[p_id] <= target_ci and ink_cell_drawn_idx[p_id] < len(plan.ordered_cells):
                                self._stamp_ink_cell(drawn, plan, plan.ordered_cells[ink_cell_drawn_idx[p_id]])
                                ink_cell_drawn_idx[p_id] += 1

                            cur_px, cur_py = samples[target_si]
                            if target_si in plan.ink_lifts:
                                cur_lift = -10.0
                        else:
                            cur_px = plan.rx + plan.rw // 2
                            cur_py = plan.ry + plan.rh // 2

                        is_text_writing = True  # Use crisp marker nib sound during ink line drawing
                        break

                    # Ensure 100% of line-art ink is stamped before Phase 2 Color Wash starts
                    if not ink_completed[p_id]:
                        while ink_cell_drawn_idx[p_id] < len(plan.ordered_cells):
                            self._stamp_ink_cell(drawn, plan, plan.ordered_cells[ink_cell_drawn_idx[p_id]])
                            ink_cell_drawn_idx[p_id] += 1
                        ink_completed[p_id] = True

                    # B2. PHASE 2 — Boustrophedon Serpentine Color Brush Wash (t_ink_end -> t_img_end)
                    # Hand sweeps back and forth across the sketched ink line-art, coloring right under the nib!
                    # Strictly clipped to `art_clip_rect` so zero brush bleed ever touches the caption or pill badge!
                    art_clip_rect = (plan.rx, plan.ry, plan.rx + plan.rw, plan.ry + plan.rh)
                    if cur_ms <= sch["t_img_end"]:
                        col_dur = max(1.0, sch["t_img_end"] - sch["t_ink_end"])
                        u_col = min(1.0, max(0.0, (cur_ms - sch["t_ink_end"]) / col_dur))
                        c_samples = plan.color_samples
                        n_col = len(c_samples)
                        if n_col > 0:
                            target_ci = min(n_col - 1, int(round(u_col * (n_col - 1))))
                            last_ci = color_sample_drawn_idx[p_id]
                            for ci in range(last_ci, target_ci + 1):
                                cpx, cpy = c_samples[ci]
                                self._stamp_brush(
                                    drawn, cpx, cpy, self.color_brush_r, self.color_disk, clip_rect=art_clip_rect
                                )
                            color_sample_drawn_idx[p_id] = target_ci + 1
                            cur_px, cur_py = c_samples[target_ci]
                        else:
                            cur_px = plan.rx + plan.rw // 2
                            cur_py = plan.ry + plan.rh // 2

                        is_sketching = True  # Soft brush/chalk shading sound during color wash
                        break

                    # Finish any remaining color brush points and ensure 100% crisp full artwork
                    c_samples = plan.color_samples
                    while color_sample_drawn_idx[p_id] < len(c_samples):
                        cpx, cpy = c_samples[color_sample_drawn_idx[p_id]]
                        self._stamp_brush(
                            drawn, cpx, cpy, self.color_brush_r, self.color_disk, clip_rect=art_clip_rect
                        )
                        color_sample_drawn_idx[p_id] += 1

                    im_r = p["img_region"]
                    ix0, iy0, iw, ih = im_r["x"], im_r["y"], im_r["width"], im_r["height"]
                    drawn[iy0 : iy0 + ih, ix0 : ix0 + iw] = self.color_img[iy0 : iy0 + ih, ix0 : ix0 + iw]

                    # C. Discrete Character-Stepped Caption Handwriting
                    ht = p.get("header_title") or p.get("caption")
                    if ht and ht.get("text"):
                        r0 = max(0, int(ht["y"] - 2))
                        r1 = min(self.h, int(ht["y"] + ht["h"] + 4))
                        tx0 = max(0, int(ht["x"]))
                        tx1 = min(self.w, int(ht["x"] + ht["w"]))
                        if cur_ms <= sch["t_cap_end"]:
                            tx, ty, tw, th = ht["x"], ht["y"], ht["w"], ht["h"]
                            base_y = ty + th * 0.58
                            cap_dur = max(1.0, sch["t_cap_end"] - sch["t_cap_start"])
                            u = min(1.0, max(0.0, (cur_ms - sch["t_cap_start"]) / cap_dur))
                            raw_tx = tx + u * tw
                            stepped_tx = tx + ((int(round(raw_tx - tx)) // glyph_step) * glyph_step)

                            x_start = tx0
                            x_end = min(tx1, int(stepped_tx))
                            # Strict pre-clear of the unwritten portion of the caption box (ahead of the pen nib)
                            if x_end < tx1:
                                drawn[r0:r1, max(tx0, x_end):tx1] = self.paper_base[r0:r1, max(tx0, x_end):tx1]
                            if x_end > x_start:
                                drawn[r0:r1, x_start:x_end] = self.color_img[r0:r1, x_start:x_end]

                            cur_px = int(round(raw_tx))
                            cur_py = int(round(base_y + 2.2 * math.sin(raw_tx * 0.50)))
                            is_text_writing = True
                            break
                        else:
                            drawn[r0:r1, tx0:tx1] = self.color_img[r0:r1, tx0:tx1]

                    # D. Parabolic Hand Lift Transit to Next Panel
                    next_p = sch.get("next_panel")
                    if next_p:
                        transit_start = sch["t_cap_end"]
                        transit_dur = max(1.0, p_end - transit_start)
                        u_transit = min(1.0, max(0.0, (cur_ms - transit_start) / transit_dur))

                        start_x = p["img_region"]["x"] + p["img_region"]["width"] // 2
                        start_y = p["img_region"]["y"] + p["img_region"]["height"] // 2
                        next_r = next_p.get("img_region", {})
                        target_x = next_r.get("x", self.w // 2) + 40
                        target_y = next_r.get("y", self.h // 2) + 40
                        lift_y = -28.0 * math.sin(u_transit * math.pi)
                        cur_px = int(round(start_x + (target_x - start_x) * u_transit))
                        cur_py = int(round(start_y + (target_y - start_y) * u_transit + lift_y))
                        cur_lift = lift_y
                        break
                    else:
                        retract_dur = 600.0
                        if cur_ms < sch["t_cap_end"] + retract_dur:
                            u_retract = min(1.0, max(0.0, (cur_ms - sch["t_cap_end"]) / retract_dur))
                            start_x = p["img_region"]["x"] + p["img_region"]["width"] // 2
                            start_y = p["img_region"]["y"] + p["img_region"]["height"] // 2
                            cur_px = int(round(start_x + (self.w + 220 - start_x) * u_retract))
                            cur_py = int(round(start_y + (self.h + 220 - start_y) * u_retract))
                            cur_lift = -20.0 * u_retract
                        else:
                            cur_px = self.w + 300
                            cur_py = self.h + 300
                        break

            # Final hold: hand off-screen so full board can be admired cleanly
            if cur_ms >= total_ms - 800.0:
                cur_px = self.w + 250
                cur_py = self.h + 250
                is_sketching = False
                is_text_writing = False

            sketch_active[fi] = is_sketching
            text_active[fi] = is_text_writing
            last_px = cur_px
            last_py = cur_py

            # In-Card B-Roll Wildlife Video Blending (Pha 2: Real Wildlife Footage inside active card)
            for p in panels:
                p_id = p["id"]
                if p_id in broll_cache:
                    sch = panel_schedules[p_id]
                    t_v_start = sch["t_img_end"]
                    t_v_end = sch["p_end"]
                    if t_v_start <= cur_ms < t_v_end:
                        frames = broll_cache[p_id]
                        n_f = len(frames)
                        v_idx = int(((cur_ms - t_v_start) / 1000.0) * 24.0) % n_f
                        v_frame = frames[v_idx]

                        fade_in = min(1.0, max(0.0, (cur_ms - t_v_start) / 350.0))
                        fade_out = min(1.0, max(0.0, (t_v_end - cur_ms) / 350.0))
                        alpha = min(fade_in, fade_out)

                        im_r = p["img_region"]
                        ix0, iy0, iw, ih = im_r["x"], im_r["y"], im_r["width"], im_r["height"]
                        doodle = drawn[iy0 : iy0 + ih, ix0 : ix0 + iw]
                        blended = (
                            doodle.astype(np.float32) * (1.0 - alpha) + v_frame.astype(np.float32) * alpha
                        ).astype(np.uint8)
                        overlay_patches.append((ix0, iy0, blended))

            frame_base = drawn.copy()
            for ox, oy, patch in overlay_patches:
                ph, pw = patch.shape[:2]
                frame_base[oy : oy + ph, ox : ox + pw] = patch

            # Apply Dynamic Multi-Node Camera Keyframes (Sequential Focus + Cubic-Bezier Pan + Auto-Fit BBox Zoom Out)
            cam_cx, cam_cy, cam_cw, cam_ch, cam_phase, cam_target_id = self._interpolate_camera(cur_ms)

            # Exclusive Active-Node Isolation during Focus/Transition:
            # While zooming into a single node i, hide previously drawn adjacent nodes so 0% of node i-1 bleeds into the frame!
            # When the camera enters "overview_reveal" (Auto-Fit Bounding Box Zoom Out), reveal ALL N nodes together!
            if self.isolate_active_node and cam_phase != "overview_reveal" and cam_target_id != "all_nodes_bbox":
                active_p = None
                for p in panels:
                    sch = panel_schedules[p["id"]]
                    if sch["p_start"] <= cur_ms < sch["p_end"]:
                        active_p = p
                        break
                if active_p is None and cam_target_id:
                    for p in panels:
                        if p["id"] == cam_target_id:
                            active_p = p
                            break
                if active_p is not None:
                    abx0, aby0, abx1, aby1 = active_p["box"]
                    min_gap = int(self.spec.get("min_node_gap_px", 60))
                    pad_iso = min(12, max(4, min_gap // 3))
                    ix0 = max(0, abx0 - pad_iso)
                    iy0 = max(0, aby0 - pad_iso)
                    ix1 = min(self.w, abx1 + pad_iso)
                    iy1 = min(self.h, aby1 + pad_iso)
                    isolated_world = self.paper_base.copy()
                    isolated_world[iy0:iy1, ix0:ix1] = frame_base[iy0:iy1, ix0:ix1]
                    frame_base = isolated_world

            body_target_h = (self.out_h - self.fixed_header_h) if is_fixed_hdr else self.out_h
            body_view, crop_x0, crop_y0, cam_scale = self._apply_camera_crop(
                frame_base, cam_cx, cam_cy, cam_cw, cam_ch, self.out_w, body_target_h
            )

            if is_fixed_hdr and self.fixed_hdr_img is not None:
                view_frame = np.full((self.out_h, self.out_w, 3), 255, dtype=np.uint8)
                view_frame[0 : self.fixed_header_h, 0 : self.out_w] = self.fixed_hdr_img[
                    0 : self.fixed_header_h, 0 : self.out_w
                ]
                view_frame[self.fixed_header_h : self.out_h, 0 : self.out_w] = body_view
                y_offset_view = self.fixed_header_h
            else:
                view_frame = body_view
                y_offset_view = 0

            # Transform hand coordinates from World Space -> Viewport Space
            if cur_px >= self.w + 150 or cur_py >= self.h + 150:
                view_px = self.out_w + 300
                view_py = self.out_h + 300
            else:
                view_px = int(round((cur_px - crop_x0) * cam_scale))
                view_py = int(round((cur_py - crop_y0) * cam_scale)) + y_offset_view

            frame = self._stamp_hand(view_frame, view_px, view_py, lift_px=cur_lift)

            # Smooth 220ms Storybook Page-Turn wipe at the very end of the scene
            if cur_ms > total_ms - 220.0:
                u_turn = min(1.0, max(0.0, (cur_ms - (total_ms - 220.0)) / 220.0))
                u_ease = u_turn * u_turn * (3.0 - 2.0 * u_turn)
                shift_x = int(round(u_ease * self.out_w))
                turned = np.full((self.out_h, self.out_w, 3), self.paper_base[0, 0], dtype=np.uint8)
                if self.out_w - shift_x > 0:
                    turned[:, 0 : self.out_w - shift_x] = frame[:, shift_x : self.out_w]
                    edge_x = self.out_w - shift_x
                    sh_w = min(18, self.out_w - edge_x)
                    if sh_w > 0:
                        for sx in range(sh_w):
                            darken = 1.0 - 0.14 * (1.0 - sx / float(sh_w))
                            turned[:, edge_x + sx] = (turned[:, edge_x + sx].astype(np.float32) * darken).astype(
                                np.uint8
                            )
                frame = turned

            writer.write(frame)

        writer.release()
        elapsed = time.time() - t0
        print(f"[HybridRenderer V6] Raw video rendered in {elapsed:.1f}s ({total_frames/elapsed:.1f} fps).")

        if audio_wav and Path(audio_wav).exists():
            final_mp4 = self._master_audio(
                raw_video, output_mp4, Path(audio_wav), sketch_active, text_active, sfx_events, total_ms
            )
            if raw_video.exists() and raw_video != final_mp4:
                try:
                    raw_video.unlink()
                except Exception:
                    pass
            return final_mp4
        else:
            return raw_video

    def _master_audio(
        self,
        raw_video: Path,
        output_mp4: Path,
        voice_wav: Path,
        sketch_active: List[bool],
        text_active: List[bool],
        sfx_events: List[Dict[str, Any]],
        total_ms: float,
    ) -> Path:
        print("[AudioMastering V6] Mixing Voice + 4-Layer Synchronized SFX + Sidechain-Ducked BGM (48kHz / 320kbps)...")

        sr = 48000
        total_samples = int(round((total_ms / 1000.0) * sr))
        sfx_mix = np.zeros(total_samples, dtype=np.float32)

        def load_sfx_float(p: Path) -> np.ndarray:
            if not p.exists():
                return np.zeros(0, dtype=np.float32)
            cmd = ["ffmpeg", "-v", "error", "-i", str(p), "-f", "f32le", "-ac", "1", "-ar", str(sr), "-"]
            res = subprocess.run(cmd, capture_output=True, check=True)
            return np.frombuffer(res.stdout, dtype=np.float32)

        marker_snd = load_sfx_float(SFX_DIR / "marker-scribble-loop.wav") * 0.13
        chalk_snd = load_sfx_float(SFX_DIR / "chalk-stroke.wav") * 0.09
        page_whoosh_snd = load_sfx_float(SFX_DIR / "page-whoosh.wav") * 0.24
        pop_snd = load_sfx_float(HYPER_SFX_DIR / "pop.mp3") * 0.28
        whoosh_short_snd = load_sfx_float(HYPER_SFX_DIR / "whoosh-short.mp3") * 0.20
        impact_snd = load_sfx_float(HYPER_SFX_DIR / "impact-bass-1.mp3") * 0.16

        samples_per_frame = int(round(sr / self.fps))
        m_idx = 0
        c_idx = 0
        for fi in range(len(sketch_active)):
            s0 = fi * samples_per_frame
            s1 = min(total_samples, s0 + samples_per_frame)
            cnt = s1 - s0
            if cnt <= 0:
                continue

            if text_active[fi] and len(marker_snd) > 100:
                for k in range(cnt):
                    sfx_mix[s0 + k] += marker_snd[(m_idx + k) % len(marker_snd)]
                m_idx = (m_idx + cnt) % len(marker_snd)
            else:
                m_idx = 0

            if sketch_active[fi] and len(chalk_snd) > 100:
                for k in range(cnt):
                    sfx_mix[s0 + k] += chalk_snd[(c_idx + k) % len(chalk_snd)]
                c_idx = (c_idx + cnt) % len(chalk_snd)
            else:
                c_idx = 0

        def stamp_event(snd: np.ndarray, t_ms: float):
            if len(snd) == 0:
                return
            st = max(0, int(round((t_ms / 1000.0) * sr)))
            if st < total_samples:
                en = min(total_samples, st + len(snd))
                sfx_mix[st:en] += snd[: en - st]

        for ev in sfx_events:
            t_ms = ev["time_ms"]
            etype = ev["type"]
            if etype == "pop":
                stamp_event(pop_snd, t_ms)
            elif etype == "transit_whoosh":
                stamp_event(whoosh_short_snd, t_ms)
            elif etype == "page_whoosh":
                stamp_event(page_whoosh_snd, t_ms)
            elif etype == "impact":
                stamp_event(impact_snd, t_ms)

        sfx_mix = np.clip(sfx_mix, -0.92, 0.92)
        sfx_pcm16 = (sfx_mix * 32767.0).astype(np.int16)

        sfx_wav = output_mp4.with_name(output_mp4.stem + "_sfx.wav")
        with wave.open(str(sfx_wav), "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(sr)
            wf.writeframes(sfx_pcm16.tobytes())

        bgm_p = ROOT / "assets" / "bgm" / "calm-acoustic.wav"
        has_bgm = bgm_p.exists()

        if has_bgm:
            filter_complex = (
                f"[1:a]apad=whole_dur={total_ms/1000.0:.3f},"
                "highpass=f=80,"
                "equalizer=f=180:t=q:w=1.1:g=1.5,"
                "equalizer=f=3400:t=q:w=1.2:g=2.5,"
                "acompressor=threshold=-16dB:ratio=2.6:attack=10:release=140,"
                "volume=1.08,asplit=2[vo_main][vo_sc];"
                "[2:a]volume=0.92[sfx];"
                "[3:a]aloop=loop=-1:size=2e+09,volume=0.13[bgm_raw];"
                "[bgm_raw][vo_sc]sidechaincompress=threshold=0.018:ratio=7:attack=15:release=260[bgm_duck];"
                "[vo_main][sfx][bgm_duck]amix=inputs=3:duration=first:dropout_transition=0,alimiter=limit=0.96[aout]"
            )
            cmd = [
                "ffmpeg", "-y",
                "-i", str(raw_video),
                "-i", str(voice_wav),
                "-i", str(sfx_wav),
                "-i", str(bgm_p),
                "-filter_complex", filter_complex,
                "-map", "0:v",
                "-map", "[aout]",
                "-c:v", "libx264", "-preset", "fast", "-crf", "17",
                "-pix_fmt", "yuv420p",
                "-video_track_timescale", "12288",
                "-c:a", "aac", "-b:a", "320k", "-ar", "48000", "-ac", "2",
                "-shortest",
                str(output_mp4),
            ]
        else:
            filter_complex = (
                f"[1:a]apad=whole_dur={total_ms/1000.0:.3f},highpass=f=80,equalizer=f=3400:t=q:w=1.2:g=2.5,volume=1.08[voice];"
                "[2:a]volume=0.92[sfx];"
                "[voice][sfx]amix=inputs=2:duration=first:dropout_transition=0,alimiter=limit=0.96[aout]"
            )
            cmd = [
                "ffmpeg", "-y",
                "-i", str(raw_video),
                "-i", str(voice_wav),
                "-i", str(sfx_wav),
                "-filter_complex", filter_complex,
                "-map", "0:v",
                "-map", "[aout]",
                "-c:v", "libx264", "-preset", "fast", "-crf", "17",
                "-pix_fmt", "yuv420p",
                "-video_track_timescale", "12288",
                "-c:a", "aac", "-b:a", "320k", "-ar", "48000", "-ac", "2",
                "-shortest",
                str(output_mp4),
            ]

        print(f"[FFmpeg V6] Mastering final video: {output_mp4.name}...")
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        if sfx_wav.exists():
            try:
                sfx_wav.unlink()
            except Exception:
                pass

        print(f"[AudioMastering V6] Complete -> {output_mp4.name}")
        return output_mp4
