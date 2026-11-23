from PIL import Image
from pathlib import Path

P = Path("projects/tap-08-chon-gulo")
long_dir = P / "assets" / "long"
shorts_dir = P / "assets" / "shorts"

def create_crop(src_path, dst_path, box):
    # box is (left_ratio, top_ratio, right_ratio, bottom_ratio)
    im = Image.open(src_path).convert("RGB")
    w, h = im.size
    crop_box = (int(box[0]*w), int(box[1]*h), int(box[2]*w), int(box[3]*h))
    cropped = im.crop(crop_box)
    
    # Place on solid pure white canvas matching original size
    out = Image.new("RGB", (w, h), (255, 255, 255))
    
    # Resize cropped to fit nicely with white padding
    scale = min((w * 0.9) / cropped.width, (h * 0.9) / cropped.height)
    new_size = (int(cropped.width * scale), int(cropped.height * scale))
    resized = cropped.resize(new_size, Image.Resampling.LANCZOS)
    
    paste_pos = ((w - new_size[0]) // 2, (h - new_size[1]) // 2)
    out.paste(resized, paste_pos)
    out.save(dst_path, "PNG")
    print(f"Created {dst_path.name} from {src_path.name}")

# 1. L38b: Close-up on Eskimo fur hood and ice frost
create_crop(long_dir / "L38.png", long_dir / "L38b.png", (0.2, 0.1, 0.8, 0.8))

# 2. L50a: Dramatic legend shot for Scene 05 opening
create_crop(long_dir / "L08.png", long_dir / "L50a.png", (0.1, 0.1, 0.9, 0.9))

# 3. L54b: Close-up on wolves retreating
create_crop(long_dir / "L54.png", long_dir / "L54b.png", (0.05, 0.15, 0.65, 0.85))

# 4. Shorts beats: S04b, S08b, S09b, S10b
create_crop(shorts_dir / "S04.png", shorts_dir / "S04b.png", (0.1, 0.2, 0.9, 0.8))
create_crop(shorts_dir / "S08.png", shorts_dir / "S08b.png", (0.1, 0.2, 0.9, 0.8))
create_crop(shorts_dir / "S09.png", shorts_dir / "S09b.png", (0.1, 0.2, 0.9, 0.8))
create_crop(shorts_dir / "S01.png", shorts_dir / "S10b.png", (0.05, 0.1, 0.95, 0.9))

print("All crop assets created successfully!")
