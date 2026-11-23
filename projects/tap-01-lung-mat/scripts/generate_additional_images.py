"""
Generate 5 Additional Illustrations for Expanded Lung Mat Scenes
Uses FastSD CPU (Intel OpenVINO + SD-Turbo) + Rembg (Transparent Background)
Matches the exact comic illustration art style of existing project assets.
"""

import sys
import time
from pathlib import Path
from PIL import Image

ROOT_DIR = Path(__file__).resolve().parents[3]
PROJ_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from src.image_gen.fastsd_generator import FastSDCPUGenerator
from rembg import remove

OUT_DIR = PROJ_DIR / "assets" / "gemini_downloaded"
OUT_DIR.mkdir(parents=True, exist_ok=True)

PROMPTS = [
    {
        "filename": "c2_badger_rpg_stats_sheet.png",
        "prompt": "Honey badger RPG character stats sheet, glowing colorful health bars and energy meters, comic cartoon game UI style, vibrant colors, high contrast, clean white background"
    },
    {
        "filename": "c3_badger_crushing_turtle_musk.png",
        "prompt": "Honey badger cracking a thick tortoise shell with strong powerful jaws, comic cartoon style, vibrant colors, crisp line art, clean white background"
    },
    {
        "filename": "c4_acetylcholine_molecular_shield.png",
        "prompt": "Cartoon honey badger with glowing green molecular energy shield deflecting purple snake venom drops, comic book art, clean white background"
    },
    {
        "filename": "c5_stoffel_mud_balls_broom_escape.png",
        "prompt": "Clever honey badger making large round mud balls and stacking them into a tower near concrete wall, comic cartoon style, vibrant colors, clean white background"
    },
    {
        "filename": "c6_sea_otter_rock_tool.png",
        "prompt": "Cute sea otter floating on its back on ocean water cracking a clam shell with a small flat stone on its tummy, comic cartoon style, vibrant colors, clean white background"
    }
]

def generate_and_clean_image(gen: FastSDCPUGenerator, item: dict):
    out_file = OUT_DIR / item["filename"]
    print(f"\n=======================================================")
    print(f"[GENERATING] {item['filename']}")
    print(f"Prompt: {item['prompt']}")
    
    t0 = time.time()
    raw_tmp = OUT_DIR / f"raw_{item['filename']}"
    gen.generate(
        prompt=item["prompt"],
        output_path=str(raw_tmp),
        negative_prompt="blurry, low quality, dark, distorted, realistic photo, watermark, noisy",
        width=512,
        height=512,
        steps=1
    )
    
    # Remove background with rembg
    print(f"  [Rembg] Removing background for {item['filename']}...")
    im_raw = Image.open(raw_tmp)
    im_nobg = remove(im_raw)
    
    # Resize to standard wide illustration canvas (1024x559) with transparent padding
    canvas_w, canvas_h = 1024, 559
    canvas = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))
    scale = min(canvas_w / im_nobg.width, canvas_h / im_nobg.height)
    new_w = max(1, int(round(im_nobg.width * scale)))
    new_h = max(1, int(round(im_nobg.height * scale)))
    im_resized = im_nobg.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    paste_x = (canvas_w - new_w) // 2
    paste_y = (canvas_h - new_h) // 2
    canvas.paste(im_resized, (paste_x, paste_y), im_resized)
    canvas.save(out_file)
    
    raw_tmp.unlink(missing_ok=True)
    print(f"[SUCCESS] Saved {out_file.name} in {time.time() - t0:.1f}s!")

def main():
    print("=======================================================")
    print("STARTING BATCH IMAGE GENERATION FOR EXPANDED SCENES")
    print(f"Target directory: {OUT_DIR}")
    print("=======================================================")
    
    gen = FastSDCPUGenerator()
    for item in PROMPTS:
        generate_and_clean_image(gen, item)
        
    print("\n=======================================================")
    print("ALL 5 ADDITIONAL ILLUSTRATIONS GENERATED SUCCESSFULLY!")
    print("=======================================================")

if __name__ == "__main__":
    main()
