import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROJ = ROOT / "projects" / "tap-01-lung-mat"
P37 = PROJ / "renders" / "qa_audit" / "all_gemini_37"
G = PROJ / "assets" / "gemini_downloaded"
B = G / "_raw_with_watermark_backup"

spec_text = (PROJ / "scripts" / "build_rich_scene_specs.py").read_text(encoding="utf-8")

b_hashes = {hashlib.md5(x.read_bytes()).hexdigest(): x.name for x in B.glob("*.png")}
g_hashes = {hashlib.md5(x.read_bytes()).hexdigest(): x.name for x in G.glob("*.png")}

print("=== ALL 37 GEMINI IMAGES AUDIT ===")
for f in sorted(P37.glob("*.png")):
    h = hashlib.md5(f.read_bytes()).hexdigest()
    name = b_hashes.get(h) or g_hashes.get(h) or "UNMAPPED"
    in_spec = "YES (IN VIDEO)" if (name != "UNMAPPED" and name in spec_text) else "NO"
    print(f"  {f.name:10s} -> {name:40s} | {in_spec}")
