import os
import json
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from scipy.io import wavfile

os.makedirs("assets/hands", exist_ok=True)
os.makedirs("assets/paper", exist_ok=True)
os.makedirs("assets/sfx", exist_ok=True)

# -------------------------------------------------------------
# 1. GENERATE WARM CREAM PAPER TEXTURE (#F5EBD7)
# -------------------------------------------------------------
def generate_paper_texture():
    width, height = 1920, 1080
    base_color = np.array([245, 235, 215], dtype=np.float32) # #F5EBD7
    
    # Generate subtle paper grain
    np.random.seed(42)
    noise = np.random.normal(0, 3.5, (height, width, 1))
    
    # Fibers
    fiber_noise = np.random.normal(0, 1.5, (height, width, 1))
    
    # Subtle vignette
    y = np.linspace(-1, 1, height)[:, None]
    x = np.linspace(-1, 1, width)[None, :]
    radius = np.sqrt(x*x + y*y)
    vignette = 1.0 - 0.05 * np.clip(radius - 0.4, 0, 1)
    vignette = vignette[:, :, None]
    
    paper = (base_color + noise + fiber_noise) * vignette
    paper = np.clip(paper, 0, 255).astype(np.uint8)
    
    img = Image.fromarray(paper, mode="RGB")
    # Slight blur to make texture organic and soft
    img = img.filter(ImageFilter.GaussianBlur(radius=0.5))
    paper_path = "assets/paper/warm-cream-texture.png"
    img.save(paper_path, "PNG")
    print(f"[OK] Generated paper texture: {paper_path}")

# -------------------------------------------------------------
# 2. GENERATE REALISTIC HAND & MARKER RIG + SHADOW
# -------------------------------------------------------------
def generate_hand_rig(force=False):
    hand_path = "assets/hands/hand-marker-right.png"
    if os.path.exists(hand_path) and not force:
        print(f"[SKIP] Custom hand sprite already exists at {hand_path}. Use force=True to regenerate procedural placeholder.")
        return
    # We will render at 1000 x 1000 resolution
    w, h = 1000, 1000
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Tip location near top-left of the hand bounding box
    # Marker tip will be at (150, 120)
    tip_x, tip_y = 150, 120

    # 1. Draw marker pen: angled from tip (150, 120) towards (550, 520)
    # Angle ~ 45 degrees
    pen_dir = np.array([1.0, 1.0])
    pen_dir = pen_dir / np.linalg.norm(pen_dir)
    pen_perp = np.array([-pen_dir[1], pen_dir[0]]) # perpendicular vector

    def pt(along, across):
        p = np.array([tip_x, tip_y]) + along * pen_dir + across * pen_perp
        return (float(p[0]), float(p[1]))

    # Marker Felt Tip (chisel/conical black tip)
    tip_poly = [pt(0, 0), pt(18, -4), pt(32, -8), pt(32, 8), pt(18, 4)]
    draw.polygon(tip_poly, fill=(20, 20, 22, 255))
    # Highlight on tip
    draw.line([pt(4, -1), pt(30, -5)], fill=(55, 55, 60, 255), width=2)

    # Metallic Collar
    collar_poly = [pt(32, -9), pt(58, -11), pt(58, 11), pt(32, 9)]
    draw.polygon(collar_poly, fill=(160, 165, 175, 255))
    # Collar highlight
    draw.line([pt(33, -3), pt(57, -3)], fill=(225, 230, 235, 255), width=4)
    draw.line([pt(33, 7), pt(57, 7)], fill=(100, 105, 115, 255), width=3)

    # Marker Grip Section (matte black rubberized)
    grip_poly = [pt(58, -12), pt(180, -15), pt(180, 15), pt(58, 12)]
    draw.polygon(grip_poly, fill=(35, 37, 40, 255))
    draw.line([pt(60, -5), pt(178, -6)], fill=(75, 78, 85, 255), width=4) # grip sheen

    # Marker Barrel (extending into hand and beyond to 550)
    barrel_poly = [pt(180, -15), pt(560, -18), pt(560, 18), pt(180, 15)]
    draw.polygon(barrel_poly, fill=(25, 27, 30, 255))
    draw.line([pt(180, -7), pt(558, -8)], fill=(65, 68, 75, 255), width=5)
    # White logo brand stripe on barrel
    draw.polygon([pt(380, -12), pt(440, -13), pt(440, 0), pt(380, 0)], fill=(210, 215, 220, 220))

    # 2. Draw Realistic Hand anatomy holding the marker
    # Skin tones: base, highlight, shadow
    skin_base = (235, 190, 165, 255)
    skin_shadow = (195, 145, 120, 255)
    skin_deep_shadow = (155, 105, 85, 255)
    skin_highlight = (250, 215, 195, 255)

    # Middle finger underneath the pen supporting the grip
    mid_finger_pts = [
        pt(130, 10), pt(160, 25), pt(210, 32), pt(250, 22), pt(220, 12), pt(150, 10)
    ]
    draw.polygon(mid_finger_pts, fill=skin_shadow)

    # Index finger pressing on top of the grip
    # Curving from wrist/knuckle (pt(380, -50)) down to grip (pt(120, -10))
    idx_knuckle = pt(360, -45)
    idx_mid = pt(250, -38)
    idx_tip = pt(115, -10)
    idx_pad = pt(120, 5)
    idx_joint = pt(240, -10)

    idx_poly = [
        idx_knuckle,
        pt(330, -55),
        pt(240, -48),
        pt(160, -32),
        idx_tip,
        idx_pad,
        idx_joint,
        pt(320, -15)
    ]
    draw.polygon(idx_poly, fill=skin_base)
    # Index finger nail
    nail_pts = [pt(125, -20), pt(145, -22), pt(140, -12), pt(122, -12)]
    draw.polygon(nail_pts, fill=(245, 210, 205, 240))
    # Index knuckle shading & creases
    draw.line([pt(230, -38), pt(245, -20)], fill=skin_shadow, width=2)
    draw.line([pt(165, -28), pt(175, -15)], fill=skin_shadow, width=2)
    # Highlight along top edge
    draw.line([pt(160, -30), pt(310, -50)], fill=skin_highlight, width=3)

    # Thumb grasping marker from the front/side
    # Starts at thumb knuckle, wraps around grip near pt(135, 10)
    thumb_tip = pt(135, 12)
    thumb_pad = pt(150, 22)
    thumb_joint = pt(240, 55)
    thumb_base = pt(350, 95)
    thumb_inner = pt(320, 30)

    thumb_poly = [
        thumb_tip,
        pt(128, -2),
        pt(170, -5),
        thumb_inner,
        thumb_base,
        pt(300, 100),
        thumb_joint,
        thumb_pad
    ]
    draw.polygon(thumb_poly, fill=skin_base)
    # Thumb nail
    draw.polygon([pt(140, 2), pt(162, 2), pt(158, 12), pt(138, 10)], fill=(245, 210, 205, 240))
    # Thumb crease
    draw.line([pt(220, 35), pt(255, 65)], fill=skin_shadow, width=3)
    draw.line([pt(160, 5), pt(185, 28)], fill=skin_shadow, width=2)

    # Palm and other curled fingers (Ring finger, Pinky)
    palm_poly = [
        idx_knuckle,
        pt(480, -60), # knuckles of ring/pinky
        pt(580, -30),
        pt(680, 50),  # wrist top
        pt(750, 200), # forearm top
        pt(650, 350), # forearm bottom
        pt(520, 260), # wrist base
        thumb_base,
        thumb_inner,
        idx_knuckle
    ]
    draw.polygon(palm_poly, fill=skin_base)

    # Shading across the palm & wrist
    draw.polygon([
        pt(480, -60), pt(580, -30), pt(520, 10), pt(430, -10)
    ], fill=skin_shadow)

    # Forearm gradient & shading towards bottom right edge
    draw.polygon([
        pt(600, 150), pt(750, 200), pt(1000, 450), pt(950, 650), pt(650, 350)
    ], fill=skin_base)
    draw.polygon([
        pt(650, 350), pt(950, 650), pt(820, 750), pt(520, 260)
    ], fill=skin_shadow)

    # Soften hand edges with anti-aliasing
    hand_smooth = img.filter(ImageFilter.GaussianBlur(radius=0.7))

    hand_path = "assets/hands/hand-marker-right.png"
    hand_smooth.save(hand_path, "PNG")
    print(f"[OK] Generated hand sprite: {hand_path} (tip anchor: {tip_x}, {tip_y})")

    # 3. Create Hand Shadow layer
    # Extract alpha mask, color black with soft gaussian blur
    shadow_img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    alpha = np.array(hand_smooth.split()[3])
    # Downscale alpha slightly for pen shadow, blur heavily
    shadow_alpha = (alpha.astype(np.float32) * 0.45).astype(np.uint8)
    shadow_img.putalpha(Image.fromarray(shadow_alpha))
    shadow_blurred = shadow_img.filter(ImageFilter.GaussianBlur(radius=18))

    shadow_path = "assets/hands/hand-shadow.png"
    shadow_blurred.save(shadow_path, "PNG")
    print(f"[OK] Generated hand shadow: {shadow_path}")

    # Metadata
    metadata = {
        "width": w,
        "height": h,
        "anchor": { "x": tip_x, "y": tip_y },
        "shadowAnchor": { "x": tip_x + 18, "y": tip_y + 24 },
        "defaultScale": 0.55
    }
    with open("assets/hands/hand_metadata.json", "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)
    print("[OK] Saved hand metadata: assets/hands/hand_metadata.json")

# -------------------------------------------------------------
# 3. GENERATE PRISTINE LOCAL SFX AUDIO FILES (Zero-API)
# -------------------------------------------------------------
def generate_sfx():
    sample_rate = 44100

    # A. Marker Scribble Loop (2.0s seamless loop)
    duration = 2.5
    num_samples = int(sample_rate * duration)
    t = np.linspace(0, duration, num_samples, endpoint=False)
    
    np.random.seed(101)
    # Broadband friction noise
    noise = np.random.uniform(-1, 1, num_samples)
    
    # Filter with resonant marker friction frequencies (~1100Hz, ~3200Hz)
    # and modulate at 10-14Hz (human handwriting strokes)
    mod = 0.5 + 0.5 * np.sin(2 * np.pi * 12.0 * t) * (0.8 + 0.2 * np.sin(2 * np.pi * 3.5 * t))
    
    # Simple acoustic resonance via moving averages
    s1 = np.convolve(noise, np.ones(5)/5, mode='same')
    s2 = np.convolve(noise, np.ones(15)/15, mode='same')
    marker_sound = (s1 - s2) * mod * 0.35
    
    # Normalize to -18 dBFS peak (~0.12 amplitude)
    max_val = np.max(np.abs(marker_sound))
    if max_val > 0:
        marker_sound = (marker_sound / max_val) * 0.14
    
    wavfile.write("assets/sfx/marker-scribble-loop.wav", sample_rate, (marker_sound * 32767).astype(np.int16))
    print("[OK] Generated SFX: assets/sfx/marker-scribble-loop.wav")

    # B. Chalk Stroke (0.8s)
    duration_c = 0.8
    num_c = int(sample_rate * duration_c)
    t_c = np.linspace(0, duration_c, num_c, endpoint=False)
    noise_c = np.random.normal(0, 0.4, num_c)
    env_c = np.sin(np.pi * t_c / duration_c) ** 1.5
    chalk_sound = noise_c * env_c * 0.18
    wavfile.write("assets/sfx/chalk-stroke.wav", sample_rate, (chalk_sound * 32767).astype(np.int16))
    print("[OK] Generated SFX: assets/sfx/chalk-stroke.wav")

    # C. Page Whoosh (0.6s frequency sweep)
    duration_w = 0.65
    num_w = int(sample_rate * duration_w)
    t_w = np.linspace(0, duration_w, num_w, endpoint=False)
    # Pink noise approximation + sweeping filter
    noise_w = np.cumsum(np.random.normal(0, 0.2, num_w))
    noise_w = noise_w - np.mean(noise_w)
    # Envelope
    env_w = np.sin(np.pi * (t_w / duration_w)) ** 2
    whoosh = noise_w * env_w * 0.08
    whoosh_max = np.max(np.abs(whoosh))
    if whoosh_max > 0:
        whoosh = (whoosh / whoosh_max) * 0.16
    wavfile.write("assets/sfx/page-whoosh.wav", sample_rate, (whoosh * 32767).astype(np.int16))
    print("[OK] Generated SFX: assets/sfx/page-whoosh.wav")

if __name__ == "__main__":
    generate_paper_texture()
    generate_hand_rig()
    generate_sfx()
