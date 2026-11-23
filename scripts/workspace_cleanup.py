"""
Workspace Cleanup — Vẽ Chuyện Hoang Dã
======================================
Xóa file trung gian / rác sinh ra trong quá trình sản xuất, GIỮ LẠI mọi thứ cần
để render lại hoặc đăng video.

GIỮ:
  - MP4 cuối: *_complete_with_intro_outro.mp4, shorts *.mp4 (bản đăng), scene0X_final.mp4
  - Thumbnail, kịch bản, SEO, specs, scripts
  - Ảnh sạch + ảnh gốc (_raw_with_watermark_backup)
  - Audio master: scene0X.wav, shorts*.wav (bản master), *_words.json, *_parts_duration.json, gap_*.wav
  - File .mp3 gốc từ ElevenLabs (nhẹ, đã trả phí tạo)

XÓA:
  - Audio .wav trung gian: *_eleven_p*.wav, *_eleven_scaled_*.wav, *_part*.wav, *_fast_p*.wav, test_*
  - Thư mục ảnh chụp QA: snapshots*, qa_audit, previews, verification_snapshots, master_snapshots
  - MP4 trùng lặp (*_complete.mp4 khi đã có *_complete_with_intro_outro.mp4), *_master.mp4, temp_*.mp4, *_raw.mp4
  - PNG kiểm tra (verify_*, check_*, test_*, *_contact_sheet*)
  - Script test_*.py, __pycache__

Cách dùng:
  python scripts/workspace_cleanup.py            # dry-run, chỉ liệt kê
  python scripts/workspace_cleanup.py --apply    # xóa thật
  python scripts/workspace_cleanup.py --apply --project tap-07-xxx   # chỉ dọn 1 tập
"""

import argparse
import fnmatch
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROJECTS = ROOT / "projects"

AUDIO_DELETE = [
    "*_eleven_p*.wav", "*_eleven_scaled_*.wav", "*_part[0-9]*.wav", "*_part[0-9].txt",
    "*_fast_p*.wav", "test_*", "last_*.wav", "verify_*.wav", "*_16k.wav",
]
RENDER_DIR_DELETE = [
    "snapshots", "snapshots_*", "qa_audit", "previews", "verification_snapshots", "master_snapshots",
]
RENDER_FILE_DELETE = [
    "temp_*", "*_raw.mp4", "*_master.mp4", "verify_*", "check_*", "master_check*", "test_*",
    "scene0*_frame_*.png", "scene0*_canvas_verified.png", "*_contact_sheet*",
]
PROJECT_DIR_DELETE = ["snapshots"]
SCRIPT_DELETE = ["test_*.py"]
BRANDING_DELETE = [
    "check_v*.png", "chk_c*.png", "test_*.png", "youtube_channel_verified_*.png",
]
TOOLS_DELETE = [
    "agentbrain", "ai_video_title_generator", "animate", "context-bank", "fastsdcpu",
    "ghost-editor", "hand-drawn-explainer-video-nikola", "kinodraw", "mattpocock-skills",
    "open-ai-youtube-agent", "self-learning-skills", "whiteboard-animation-vi",
    "whiteboard-animator", "youtube_seo_research",
]
SRC_FILE_DELETE = ["src/image_gen/fastsd_generator.py"]


def match_any(name: str, patterns) -> bool:
    return any(fnmatch.fnmatch(name, p) for p in patterns)


def size_of(p: Path) -> int:
    if p.is_file():
        return p.stat().st_size
    return sum(f.stat().st_size for f in p.rglob("*") if f.is_file())


def collect(project_filter=None, include_global=True):
    targets = []
    for proj in sorted(PROJECTS.iterdir()):
        if not proj.is_dir() or (project_filter and proj.name != project_filter):
            continue
        audio = proj / "audio"
        if audio.exists():
            targets += [f for f in audio.iterdir() if f.is_file() and match_any(f.name, AUDIO_DELETE)]
        renders = proj / "renders"
        if renders.exists():
            for f in renders.iterdir():
                if f.is_dir() and match_any(f.name, RENDER_DIR_DELETE):
                    targets.append(f)
                elif f.is_file() and match_any(f.name, RENDER_FILE_DELETE):
                    targets.append(f)
            # duplicate complete.mp4 when a with_intro_outro version exists
            for f in renders.glob("*_complete.mp4"):
                if (renders / f.name.replace("_complete.mp4", "_complete_with_intro_outro.mp4")).exists():
                    targets.append(f)
        for d in PROJECT_DIR_DELETE:
            if (proj / d).is_dir():
                targets.append(proj / d)
        scripts = proj / "scripts"
        if scripts.exists():
            targets += [f for f in scripts.iterdir() if f.is_file() and match_any(f.name, SCRIPT_DELETE)]
            # SEO files misplaced inside scripts/ (canonical copies live in project root)
            for n in ("seo_package.json", "seo_package.md"):
                if (scripts / n).exists() and (proj / n).exists():
                    targets.append(scripts / n)
        # empty dirs
        for d in proj.rglob("*"):
            if d.is_dir() and not any(d.iterdir()):
                targets.append(d)

    if include_global:
        branding = ROOT / "assets" / "branding"
        targets += [f for f in branding.iterdir() if f.is_file() and match_any(f.name, BRANDING_DELETE)]
        targets += [ROOT / "tools" / t for t in TOOLS_DELETE if (ROOT / "tools" / t).exists()]
        targets += [ROOT / p for p in SRC_FILE_DELETE if (ROOT / p).exists()]
        for base in ("src", "scripts", "projects"):
            targets += [d for d in (ROOT / base).rglob("__pycache__") if d.is_dir()]

    # dedupe, drop children of already-targeted dirs
    uniq = sorted(set(targets), key=lambda p: len(p.parts))
    final = []
    for t in uniq:
        if not any(parent in final for parent in t.parents):
            final.append(t)
    return final


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="Thực sự xóa (mặc định chỉ dry-run)")
    ap.add_argument("--project", help="Chỉ dọn một tập, ví dụ tap-07-ca-sau")
    args = ap.parse_args()

    targets = collect(args.project, include_global=args.project is None)
    total = 0
    for t in targets:
        s = size_of(t)
        total += s
        kind = "DIR " if t.is_dir() else "FILE"
        print(f"{kind} {s/1e6:9.1f} MB  {t.relative_to(ROOT)}")
    print(f"\n{len(targets)} mục, tổng {total/1e9:.2f} GB")

    if not args.apply:
        print("\n[DRY-RUN] Chưa xóa gì. Thêm --apply để xóa thật.")
        return
    import os, stat

    def _force(func, path, _exc):
        os.chmod(path, stat.S_IWRITE)  # .git objects are read-only on Windows
        func(path)

    for t in targets:
        if t.is_dir():
            shutil.rmtree(t, onerror=_force)
        elif t.exists():
            t.unlink()
    print("Đã xóa xong.")


if __name__ == "__main__":
    sys.exit(main())
