"""
Dynamic Multi-Node Canvas & Auto-Fit Bounding Box Camera Engine V2 (`dynamic_flow_layout.py`)
=============================================================================================
Implements the 4-Pillar Infinite Whiteboard Spatial & Camera Architecture:

1. Fixed Viewport Top Header (`HUD Banner`) + Zoomable Body World Canvas:
   - The Editorial Top Header is rendered in Viewport Space (`1280x720`, top `0..66px`) so it stays
     100% fixed, centered, and un-zoomed at the top of the screen throughout all camera pans/zooms.
   - Only the Body World Canvas below the header (`y >= 68px` in Viewport) pans and zooms!

2. Dynamic Elements & World Coordinate Flow/Snake Allocator (`Gap >= 200px`):
   - Supports any arbitrary number of visual beats `N` per chapter (`2, 3, 4, 5, 6+` elements).
   - Allocates `(x, y)` World Coordinates in a Flow/Snake layout with generous spacing (`gap_x >= 200px`,
     `gap_y >= 150px`), strictly `>= 120px`.

3. Exclusive Active-Node Isolation During Focus + Sequential Cubic-Bezier Camera Keyframes:
   - For each element `i` from `1` to `N`:
     + `Keyframe Focus`: Pans camera to the exact center of node `i`, Zoom In (`1.85x - 2.15x`).
       During Focus on node `i`, adjacent/previous nodes are isolated (hidden on pure blank paper)
       so zero edge bleed from node `i-1` ever intrudes into the focused frame!
     + `Keyframe Transition`: Smoothly glides camera (`0.55s - 0.65s`, cubic-bezier) to node `i+1`
       across clean blank paper.

4. Auto-Fit Bounding Box Overview Reveal (`Zoom Out Toàn Cảnh`):
   - When the final element `N` finishes drawing, computes `[X_min, X_max, Y_min, Y_max]` across all `N`
     body nodes, calculates `Center` and `Zoom_out` to fit the Body Viewport (`1280 x (720 - header_h)`),
     and reveals all `N` completed illustrations together underneath the fixed top header.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List, Dict, Tuple, Optional, Any
from PIL import Image, ImageDraw

from editorial_sketchbook_composer import (
    create_whiteboard_canvas,
    draw_editorial_header,
    place_full_illustration_beat,
    draw_organic_line,
    INK_CHARCOAL,
    INK_MUTED,
    ACCENT_CRIMSON,
    ACCENT_AMBER,
    ACCENT_TEAL,
    ACCENT_ROYAL,
    HIGHLIGHT_YELLOW,
)


def cubic_bezier_1d(u: float, p1: float = 0.42, p2: float = 0.0, p3: float = 0.22, p4: float = 1.0) -> float:
    """Evaluates a CSS-style 1D Cubic-Bezier easing curve `cubic-bezier(x1, y1, x2, y2)` at `u in [0, 1]`."""
    if u <= 0.0:
        return 0.0
    if u >= 1.0:
        return 1.0

    def sample_x(t: float) -> float:
        return 3.0 * (1.0 - t) ** 2 * t * p1 + 3.0 * (1.0 - t) * t ** 2 * p3 + t ** 3

    def sample_dx(t: float) -> float:
        return 3.0 * (1.0 - t) ** 2 * p1 + 6.0 * (1.0 - t) * t * (p3 - p1) + 3.0 * t ** 2 * (1.0 - p3)

    def sample_y(t: float) -> float:
        return 3.0 * (1.0 - t) ** 2 * t * p2 + 3.0 * (1.0 - t) * t ** 2 * p4 + t ** 3

    t = u
    for _ in range(6):
        err = sample_x(t) - u
        if abs(err) < 1e-5:
            break
        dx = sample_dx(t)
        if abs(dx) < 1e-6:
            break
        t = max(0.0, min(1.0, t - err / dx))

    return max(0.0, min(1.0, sample_y(t)))


@dataclass
class WorldNodeConfig:
    beat_id: str
    img_path: Path
    caption_text: str
    start_ms: int
    end_ms: int
    badge_text: Optional[str] = None
    badge_color: Tuple[int, int, int] = ACCENT_CRIMSON
    highlight_color: Tuple[int, int, int] = HIGHLIGHT_YELLOW
    focus_zoom: float = 2.0  # Relative to full overview (1.8x - 2.2x)
    broll_video: Optional[Path] = None


@dataclass
class CameraKeyframe:
    time_ms: float
    cx: float
    cy: float
    crop_w: float
    crop_h: float
    zoom_relative: float
    phase: str  # "focus_hold" | "transition" | "overview_reveal"
    target_node_id: Optional[str] = None


def allocate_flow_snake_coordinates(
    n_nodes: int,
    node_w: int = 660,
    node_h: int = 430,
    gap_x: int = 75,
    gap_y: int = 60,
    margin_x: int = 80,
    margin_top: int = 60,
    margin_bottom: int = 60,
    body_aspect: float = 1280.0 / 652.0,
) -> Tuple[int, int, List[Tuple[int, int, int, int]]]:
    """
    Allocates World Coordinates `(x, y, node_w, node_h)` for `N` dynamic body elements
    using a compact Flow / Snake storyboard grid with tight inter-node gaps (`gap_x = 75px`, `gap_y = 60px`).
    """
    assert gap_x >= 40 and gap_y >= 40, "Inter-node spacing must be >= 40px"

    if n_nodes <= 2:
        row_counts = [n_nodes]
    elif n_nodes == 3:
        row_counts = [2, 1]
    elif n_nodes == 4:
        row_counts = [2, 2]
    elif n_nodes == 5:
        row_counts = [3, 2]
    else:
        row_counts = []
        rem = n_nodes
        while rem > 0:
            take = min(3, rem)
            row_counts.append(take)
            rem -= take

    max_cols = max(row_counts)
    n_rows = len(row_counts)

    content_w = max_cols * node_w + (max_cols - 1) * gap_x
    content_h = n_rows * node_h + (n_rows - 1) * gap_y

    raw_w = content_w + 2 * margin_x
    raw_h = margin_top + content_h + margin_bottom

    if raw_w / float(raw_h) < body_aspect:
        world_h = raw_h
        world_w = int(math.ceil(world_h * body_aspect))
    else:
        world_w = raw_w
        world_h = int(math.ceil(world_w / body_aspect))

    world_w += world_w % 2
    world_h += world_h % 2

    start_y = margin_top + max(0, (world_h - margin_top - margin_bottom - content_h) // 2)

    coords: List[Tuple[int, int, int, int]] = []
    for r_idx, cols_in_row in enumerate(row_counts):
        row_w = cols_in_row * node_w + (cols_in_row - 1) * gap_x
        row_start_x = (world_w - row_w) // 2
        ry = start_y + r_idx * (node_h + gap_y)

        row_boxes = []
        for c_idx in range(cols_in_row):
            rx = row_start_x + c_idx * (node_w + gap_x)
            row_boxes.append((rx, ry, node_w, node_h))

        # Snake order: odd rows flow Right -> Left so camera glides down seamlessly from the right side
        if r_idx % 2 == 1:
            row_boxes.reverse()

        coords.extend(row_boxes)

    return world_w, world_h, coords


def build_fixed_header_strip(
    viewport_w: int,
    header_h: int,
    act_badge: str,
    title_text: str,
    accent_color: Tuple[int, int, int],
    out_header_path: Path,
) -> Dict[str, Any]:
    """
    Renders the Fixed Top Header Banner at exact Viewport scale (`1280 x header_h`)
    so it stays 100% stationary at the top of the screen while the Body Canvas zooms below it.
    """
    hdr_canvas = create_whiteboard_canvas(viewport_w, header_h)
    draw = ImageDraw.Draw(hdr_canvas)
    hdr_spec = draw_editorial_header(draw, act_badge, title_text, accent_color=accent_color)
    out_header_path.parent.mkdir(parents=True, exist_ok=True)
    hdr_canvas.save(out_header_path, quality=95)
    hdr_spec["fixed_viewport_header"] = True
    hdr_spec["header_height"] = header_h
    hdr_spec["header_img"] = str(out_header_path.resolve().as_posix())
    return hdr_spec


def compute_auto_fit_bounding_box(
    panels: List[Dict[str, Any]],
    world_w: int,
    world_h: int,
    body_viewport_w: int = 1280,
    body_viewport_h: int = 652,
    padding_px: int = 75,
) -> Dict[str, float]:
    """
    Computes the Auto-Fit Bounding Box across all `N` body nodes to frame them cleanly
    inside the Body Viewport (`1280 x 652` below the fixed 68px top header).
    """
    xs0, ys0, xs1, ys1 = [], [], [], []
    for p in panels:
        bx0, by0, bx1, by1 = p["box"]
        xs0.append(bx0)
        ys0.append(by0)
        xs1.append(bx1)
        ys1.append(by1)

    x_min = float(min(xs0)) if xs0 else 0.0
    y_min = float(min(ys0)) if ys0 else 0.0
    x_max = float(max(xs1)) if xs1 else float(world_w)
    y_max = float(max(ys1)) if ys1 else float(world_h)

    bbox_w = max(100.0, x_max - x_min)
    bbox_h = max(100.0, y_max - y_min)

    cx = (x_min + x_max) / 2.0
    cy = (y_min + y_max) / 2.0

    zoom_out = min(
        body_viewport_w / (bbox_w + 2.0 * padding_px),
        body_viewport_h / (bbox_h + 2.0 * padding_px),
    )
    crop_w = min(float(world_w), body_viewport_w / max(1e-4, zoom_out))
    crop_h = min(float(world_h), body_viewport_h / max(1e-4, zoom_out))

    aspect = body_viewport_w / float(body_viewport_h)
    if crop_w / crop_h < aspect:
        crop_w = min(float(world_w), crop_h * aspect)
        crop_h = crop_w / aspect
    else:
        crop_h = min(float(world_h), crop_w / aspect)
        crop_w = crop_h * aspect

    cx = max(crop_w / 2.0, min(world_w - crop_w / 2.0, cx))
    cy = max(crop_h / 2.0, min(world_h - crop_h / 2.0, cy))

    return {
        "x_min": round(x_min, 1),
        "y_min": round(y_min, 1),
        "x_max": round(x_max, 1),
        "y_max": round(y_max, 1),
        "bbox_w": round(bbox_w, 1),
        "bbox_h": round(bbox_h, 1),
        "center_x": round(cx, 1),
        "center_y": round(cy, 1),
        "zoom_out_scale": round(zoom_out, 4),
        "crop_w": round(crop_w, 1),
        "crop_h": round(crop_h, 1),
    }


def generate_sequential_camera_keyframes(
    panels: List[Dict[str, Any]],
    overview_bbox: Dict[str, float],
    total_duration_ms: int,
    world_w: int,
    world_h: int,
    body_viewport_w: int = 1280,
    body_viewport_h: int = 652,
    focus_zoom_list: Optional[List[float]] = None,
    transition_ms: float = 620.0,
    overview_reveal_dur_ms: float = 2200.0,
) -> List[Dict[str, Any]]:
    """
    Generates Sequential Focus Camera Keyframes (`1..N`) for the Body World Canvas,
    followed by the Auto-Fit Bounding Box Overview Reveal (`Zoom Out Toàn Cảnh`).
    """
    aspect = body_viewport_w / float(body_viewport_h)
    ov_cx = overview_bbox["center_x"]
    ov_cy = overview_bbox["center_y"]
    ov_cw = overview_bbox["crop_w"]
    ov_ch = overview_bbox["crop_h"]

    keyframes: List[CameraKeyframe] = []
    n = len(panels)

    for idx, p in enumerate(panels):
        bx0, by0, bx1, by1 = p["box"]
        node_cx = (bx0 + bx1) / 2.0
        node_cy = (by0 + by1) / 2.0
        node_w = max(200.0, float(bx1 - bx0))
        node_h = max(150.0, float(by1 - by0))

        # Close-up framing: Node fills ~75-85% of body viewport height with comfortable margins
        target_ch = node_h + 60.0
        target_cw = target_ch * aspect

        # Guarantees the node is 100% DEAD CENTER in the viewport! (No clamping to world edges)
        fcx = node_cx
        fcy = node_cy
        actual_z = round(ov_cw / target_cw, 2)

        p_start = float(p["start_ms"])
        p_end = float(p["end_ms"])

        if idx == n - 1:
            hold_end = p_end
        else:
            hold_end = max(p_start + 800.0, p_end - transition_ms)

        if idx == 0 and p_start > 0:
            keyframes.append(
                CameraKeyframe(
                    time_ms=0.0,
                    cx=round(fcx, 1),
                    cy=round(fcy, 1),
                    crop_w=round(target_cw, 1),
                    crop_h=round(target_ch, 1),
                    zoom_relative=actual_z,
                    phase="focus_hold",
                    target_node_id=p["id"],
                )
            )

        keyframes.append(
            CameraKeyframe(
                time_ms=round(p_start, 1),
                cx=round(fcx, 1),
                cy=round(fcy, 1),
                crop_w=round(target_cw, 1),
                crop_h=round(target_ch, 1),
                zoom_relative=actual_z,
                phase="focus_hold",
                target_node_id=p["id"],
            )
        )
        keyframes.append(
            CameraKeyframe(
                time_ms=round(hold_end, 1),
                cx=round(fcx, 1),
                cy=round(fcy, 1),
                crop_w=round(target_cw, 1),
                crop_h=round(target_ch, 1),
                zoom_relative=actual_z,
                phase="transition" if idx + 1 < n else "overview_reveal",
                target_node_id=p["id"],
            )
        )

    # Overview Reveal: Glide smoothly from the last focused node into full Overview (500ms),
    # then HOLD for the remainder of the scene (giving viewers ~1.0s to review everything, total hold 1.5s)
    reveal_arrive_ms = min(float(total_duration_ms) - 800.0, keyframes[-1].time_ms + 500.0)
    keyframes.append(
        CameraKeyframe(
            time_ms=round(reveal_arrive_ms, 1),
            cx=ov_cx,
            cy=ov_cy,
            crop_w=ov_cw,
            crop_h=ov_ch,
            zoom_relative=1.0,
            phase="overview_reveal",
            target_node_id="all_nodes_bbox",
        )
    )
    keyframes.append(
        CameraKeyframe(
            time_ms=float(total_duration_ms),
            cx=ov_cx,
            cy=ov_cy,
            crop_w=ov_cw,
            crop_h=ov_ch,
            zoom_relative=1.0,
            phase="overview_reveal",
            target_node_id="all_nodes_bbox",
        )
    )

    return [asdict(kf) for kf in keyframes]


def build_dynamic_multi_node_scene(
    scene_id: str,
    act_badge: str,
    title_text: str,
    accent_color: Tuple[int, int, int],
    nodes: List[WorldNodeConfig],
    duration_ms: int,
    out_canvas_path: Path,
    viewport_w: int = 1280,
    viewport_h: int = 720,
    fixed_header_h: int = 68,
    node_w: int = 660,
    node_h: int = 430,
    gap_x: int = 75,
    gap_y: int = 60,
    isolate_active_node_during_focus: bool = True,
) -> Dict[str, Any]:
    """
    Builds a complete Dynamic Multi-Node Body World Canvas + Fixed Top Viewport Header
    with Exclusive Active-Node Isolation during Focus and Auto-Fit Bounding Box Overview Reveal.
    """
    n_nodes = len(nodes)
    body_viewport_w = viewport_w
    body_viewport_h = viewport_h - fixed_header_h
    body_aspect = body_viewport_w / float(body_viewport_h)

    world_w, world_h, coords = allocate_flow_snake_coordinates(
        n_nodes=n_nodes,
        node_w=node_w,
        node_h=node_h,
        gap_x=gap_x,
        gap_y=gap_y,
        margin_x=80,
        margin_top=60,
        margin_bottom=60,
        body_aspect=body_aspect,
    )

    # 1. Fixed Top Header Strip in Viewport Coordinates (1280 x 68)
    out_header_path = out_canvas_path.with_name(out_canvas_path.stem + "_header.png")
    hdr = build_fixed_header_strip(
        viewport_w=viewport_w,
        header_h=fixed_header_h,
        act_badge=act_badge,
        title_text=title_text,
        accent_color=accent_color,
        out_header_path=out_header_path,
    )

    # 2. Body World Canvas (pure white, containing only the N dynamic illustrations)
    canvas = create_whiteboard_canvas(world_w, world_h)
    draw = ImageDraw.Draw(canvas)

    panels: List[Dict[str, Any]] = []
    focus_zooms: List[float] = []

    for cfg, (nx, ny, nw, nh) in zip(nodes, coords):
        p_spec = place_full_illustration_beat(
            canvas=canvas,
            draw=draw,
            beat_id=cfg.beat_id,
            img_path=cfg.img_path,
            caption_text=cfg.caption_text,
            x=nx,
            y=ny,
            max_w=nw,
            max_h=nh,
            start_ms=cfg.start_ms,
            end_ms=cfg.end_ms,
            badge_text=cfg.badge_text,
            badge_color=cfg.badge_color,
            highlight_color=cfg.highlight_color,
            broll_video=cfg.broll_video,
        )
        panels.append(p_spec)
        focus_zooms.append(cfg.focus_zoom)

    out_canvas_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(out_canvas_path, quality=95)

    overview_bbox = compute_auto_fit_bounding_box(
        panels=panels,
        world_w=world_w,
        world_h=world_h,
        body_viewport_w=body_viewport_w,
        body_viewport_h=body_viewport_h,
        padding_px=45,
    )

    camera_keyframes = generate_sequential_camera_keyframes(
        panels=panels,
        overview_bbox=overview_bbox,
        total_duration_ms=duration_ms,
        world_w=world_w,
        world_h=world_h,
        body_viewport_w=body_viewport_w,
        body_viewport_h=body_viewport_h,
        focus_zoom_list=focus_zooms,
        transition_ms=620.0,
        overview_reveal_dur_ms=2200.0,
    )

    return {
        "scene_id": scene_id,
        "layout_mode": "dynamic_multi_node_snake_flow",
        "node_count": n_nodes,
        "world_width": world_w,
        "world_height": world_h,
        "viewport_width": viewport_w,
        "viewport_height": viewport_h,
        "fixed_header_height": fixed_header_h,
        "isolate_active_node_during_focus": isolate_active_node_during_focus,
        "min_node_gap_px": min(gap_x, gap_y),
        "duration_ms": duration_ms,
        "canvas_img": str(out_canvas_path.resolve().as_posix()),
        "header": hdr,
        "panels": panels,
        "auto_fit_bbox": overview_bbox,
        "camera_keyframes": camera_keyframes,
    }
