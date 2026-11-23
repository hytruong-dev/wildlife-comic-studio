"""Bộ công cụ tự động hóa toàn bộ quy trình tái thiết kế & render lại cho Tập 34 -> 40.
Chạy tuần tự từng bước: extra -> shorts -> long -> prep_banners -> import_images -> render -> qa -> seo -> doc.
"""
import sys
import subprocess
import shutil
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent

def run_cmd(args, desc):
    print(f"\n[RUNNING] {desc}: {' '.join(str(a) for a in args)}")
    res = subprocess.run(args, cwd=str(ROOT))
    if res.returncode != 0:
        print(f"  !! [FAILED] {desc} (exit {res.returncode})")
        return False
    print(f"  [SUCCESS] {desc}")
    return True

def process_episode(slug):
    print(f"\n{'='*60}\nBẮT ĐẦU TÁI THIẾT KẾ TOÀN DIỆN CHO: {slug}\n{'='*60}")
    p_dir = ROOT / "projects" / slug
    assets_dir = p_dir / "assets"
    arch_dir = assets_dir / "archive_comic2d"

    # 1. Backup old assets if not already backed up
    arch_dir.mkdir(parents=True, exist_ok=True)
    for d in ['long', 'shorts', 'banners']:
        src = assets_dir / d
        dst = arch_dir / d
        if src.exists() and not dst.exists():
            shutil.copytree(str(src), str(dst), dirs_exist_ok=True)
    print(f"  [OK] Đã bảo đảm an toàn bản backup tại {arch_dir}")

    # 2. Clear old generated images so gemini_gen regenerates with new prompts
    import glob
    for pattern in [
        f"{assets_dir}/long/*.png", f"{assets_dir}/shorts/*.png",
        f"{assets_dir}/_src/*.txt", f"{assets_dir}/_src/*.png",
        f"{assets_dir}/inbox/*.txt", f"{assets_dir}/inbox/*.png",
        f"{assets_dir}/banners/*.png"
    ]:
        for f in glob.glob(pattern):
            try: os.remove(f)
            except: pass
    print("  [OK] Đã dọn sạch assets cũ sẵn sàng tạo mới")

    # 3. Generate Extra (Banners & Thumbnail)
    if not run_cmd(["node", "src/episode/gemini_gen.cjs", f"projects/{slug}", "extra"], f"Tạo banner & thumb {slug}"):
        return False

    # 4. Generate Shorts images
    if not run_cmd(["node", "src/episode/gemini_gen.cjs", f"projects/{slug}", "shorts"], f"Tạo ảnh Shorts {slug}"):
        return False

    # 5. Generate Long images
    if not run_cmd(["node", "src/episode/gemini_gen.cjs", f"projects/{slug}", "long", "--per-chat", "10"], f"Tạo ảnh Long-form {slug}"):
        return False

    # 5B. Self-healing check for any missing images
    try:
        import json
        long_plan = json.loads((p_dir / "specs" / "longform_plan.json").read_text(encoding="utf-8"))
        shorts_plan = json.loads((p_dir / "specs" / "shorts_plan.json").read_text(encoding="utf-8"))
        inbox = p_dir / "assets" / "inbox"
        long_dir = p_dir / "assets" / "long"
        shorts_dir = p_dir / "assets" / "shorts"

        missing_long = [item["id"] for item in long_plan if not (inbox / f"{item['id']}.txt").exists() and not (long_dir / f"{item['id']}.png").exists()]
        missing_shorts = [item["id"] for item in shorts_plan if not (inbox / f"{item['id']}.txt").exists() and not (shorts_dir / f"{item['id']}.png").exists()]

        if missing_long:
            print(f"  [RETRY] Đang tạo bù {len(missing_long)} ảnh Long còn thiếu: {missing_long}")
            run_cmd(["node", "src/episode/gemini_gen.cjs", f"projects/{slug}", "long", "--only", ",".join(missing_long), "--per-chat", "1"], f"Tạo bù Long {slug}")

        if missing_shorts:
            print(f"  [RETRY] Đang tạo bù {len(missing_shorts)} ảnh Shorts còn thiếu: {missing_shorts}")
            run_cmd(["node", "src/episode/gemini_gen.cjs", f"projects/{slug}", "shorts", "--only", ",".join(missing_shorts), "--per-chat", "1"], f"Tạo bù Shorts {slug}")
    except Exception as e:
        print(f"  [WARN] Không thể kiểm tra bù ảnh: {e}")

    # 6. Prep Banners
    run_cmd(["python", "src/episode/prep_banners.py", f"projects/{slug}", f"projects/{slug}/assets/_src"], f"Tách nền Banners {slug}")

    # 7. Import Images with Sheets
    run_cmd(["python", "src/episode/import_images.py", f"projects/{slug}", "--sheet"], f"Import ảnh & lập sheet {slug}")

    # 8. Render Shorts
    run_cmd(["python", "src/episode/pipeline.py", "render", f"projects/{slug}", "--shorts"], f"Render Shorts {slug}")

    # 9. Render Long
    run_cmd(["python", "src/episode/pipeline.py", "render", f"projects/{slug}", "--long"], f"Render Long-form {slug}")

    # 10. QA, SEO & Doc
    run_cmd(["python", "src/episode/pipeline.py", "qa", f"projects/{slug}"], f"Kiểm duyệt QA {slug}")
    run_cmd(["python", "src/episode/pipeline.py", "seo", f"projects/{slug}"], f"Đóng gói SEO {slug}")
    run_cmd(["python", "src/episode/episode_doc.py", f"projects/{slug}"], f"Lập tài liệu EPISODE_SPEC {slug}")

    print(f"\n[HOÀN TẤT 100%] Đã tái thiết kế và kết xuất video thành công cho {slug}!")
    return True

if __name__ == "__main__":
    slugs = sys.argv[1:] if len(sys.argv) > 1 else [
        "tap-34-qua-den",
        "tap-35-ca-voi-sat-thu",
        "tap-36-chim-go-kien",
        "tap-37-lac-da-sa-mac",
        "tap-38-de-nui-bac-my",
        "tap-39-chim-bach-thanh",
        "tap-40-kien-cat-la",
    ]
    for s in slugs:
        ok = process_episode(s)
        if not ok:
            print(f"Tạm dừng tại {s} do có lỗi.")
            break

