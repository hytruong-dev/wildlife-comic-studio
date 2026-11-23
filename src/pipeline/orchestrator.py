"""
Unified Production Orchestrator (`orchestrator.py`)
Master Entry Point for producing any Episode in the 30-Day Channel Blueprint:
- Automatically loads animal data from `master_channel_roadmap.json`.
- Enforces strict 7-Gate Preflight QA before approval.
- Coordinates Assets Sanitization, VoiceStudio (OmniVoice) Voice Synthesis, Scene Composition, Shorts Rendering, Thumbnail Creation, SEO Packaging, and Scheduled Uploading.

Usage:
    python -m src.pipeline.orchestrator --tap 6 --step qa
    python -m src.pipeline.orchestrator --tap 6 --step sanitize
    python -m src.pipeline.orchestrator --tap 6 --step thumbnail
    python -m src.pipeline.orchestrator --tap 6 --step seo
"""

import sys
import json
import argparse
from pathlib import Path
from typing import Dict, Any, Optional

ROOT = Path(__file__).resolve().parents[2]
ROADMAP_FILE = ROOT / "src" / "pipeline" / "master_channel_roadmap.json"

from src.pipeline.asset_sanitizer import sanitize_directory
from src.pipeline.preflight_qa import PreflightQAInspector


def load_roadmap() -> Dict[str, Any]:
    with open(ROADMAP_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def get_episode_data(episode_num: int) -> Dict[str, Any]:
    roadmap = load_roadmap()
    ep_str = str(episode_num)
    if ep_str not in roadmap.get("episodes", {}):
        raise ValueError(f"Episode {episode_num} not found in master roadmap!")
    return roadmap["episodes"][ep_str]


def run_preflight_qa(episode_num: int) -> bool:
    ep = get_episode_data(episode_num)
    ep_dir = ROOT / "projects" / ep.get("folder", f"tap-{episode_num:02d}")
    inspector = PreflightQAInspector(ep_dir, episode_num)
    passed, issues = inspector.run_all_gates()
    if not passed:
        print(f"[PREFLIGHT QA FAILED] Found {len(issues)} issues:")
        for iss in issues:
            print(f"  ❌ {iss}")
        return False
    print(f"✨ [PREFLIGHT QA 100% PASSED] All 7 gates cleared for Tập {episode_num:02d}!")
    return True


def run_sanitize_assets(episode_num: int) -> None:
    ep = get_episode_data(episode_num)
    ep_dir = ROOT / "projects" / ep.get("folder", f"tap-{episode_num:02d}")
    
    # 1. Longform assets
    raw_long = ep_dir / "assets" / "gemini_downloaded" / "_raw_with_watermark_backup"
    clean_long = ep_dir / "assets" / "gemini_downloaded"
    res1 = sanitize_directory(raw_long, clean_long)
    print(f"[INFO] Sanitized {len(res1)} Longform assets.")

    # 2. Shorts assets
    raw_shorts = ep_dir / "assets" / "gemini_downloaded_shorts" / "_raw_with_watermark_backup"
    clean_shorts = ep_dir / "assets" / "gemini_downloaded_shorts"
    res2 = sanitize_directory(raw_shorts, clean_shorts)
    print(f"[INFO] Sanitized {len(res2)} Shorts assets.")


def main():
    parser = argparse.ArgumentParser(description="Unified Production Orchestrator for Vẽ Chuyện Hoang Dã")
    parser.add_argument("--tap", type=int, required=True, help="Episode number (e.g. 5, 6)")
    parser.add_argument("--step", type=str, default="qa", choices=["qa", "sanitize", "status"], help="Action step to run")

    args = parser.parse_args()
    print(f"🎬 [Vẽ Chuyện Hoang Dã] Pipeline Master triggered for Episode {args.tap} (Step: {args.step})")

    if args.step == "qa":
        success = run_preflight_qa(args.tap)
        sys.exit(0 if success else 1)
    elif args.step == "sanitize":
        run_sanitize_assets(args.tap)
    elif args.step == "status":
        ep = get_episode_data(args.tap)
        print(json.dumps(ep, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
