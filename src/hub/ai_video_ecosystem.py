"""
AI Video Ecosystem Hub - Central Orchestration for 13 State-of-the-Art Video Engines
Combines:
  1. geeklee/srt-whiteboard-animation: Mask partition + stream ink/color rendering
  2. letuandat131/whiteboard-animation-vi: Subject-first coloring & ISNet foreground separation
  3. masihsultani/whiteboard-animator: CRAFT text detection & TSP skeleton path sequencing
  4. hi-nikola/hand-drawn-explainer-video-nikola: Dual semantic islands & whiteboard preflight
  5. cth9191/animate: Procedural canvas animation & beat-mapped audio cuts
  6. edwardaiwang-svg/kinodraw: Infinite whiteboard camera & 1760+ doodle matching
  7. heygen-com/hyperframes: HTML5/SVG/Canvas programmatic rendering engine
  8. remotion.dev: React frame-accurate video composition & dynamic typography
  9. kurbaitaev/ghost-editor: Voice Activity Detection (VAD), silence trimming & video QA
  10. mattpocock/skills: Universal Agent Skills architecture & progressive disclosure
  11. kulaxyz/self-learning-skills: Verified golden path promotion & failure pattern harvesting
  12. frontmatters/agentbrain: Persistent cross-session agent cognitive memory
  13. kadiresen/context-bank: Context-efficient retrieval memory bank
"""

import os
import sys
import json
import subprocess
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
TOOLS_DIR = ROOT_DIR / "tools"

ECOSYSTEM_REGISTRY = {
    "srt-whiteboard-animation": {
        "repo": "geeklee/srt-whiteboard-animation",
        "category": "Whiteboard Stream Engine",
        "path": TOOLS_DIR / "srt-whiteboard-animation",
        "entry": TOOLS_DIR / "srt-whiteboard-animation" / "scripts" / "render_stream_whiteboard.py",
        "status": "ready",
        "description": "Stream ink->color whiteboard renderer with mask partition orchestration & drawing hand rig"
    },
    "whiteboard-animation-vi": {
        "repo": "letuandat131/whiteboard-animation-vi",
        "category": "Subject-First Separation & Hand Rig",
        "path": TOOLS_DIR / "whiteboard-animation-vi",
        "entry": TOOLS_DIR / "whiteboard-animation-vi" / "handdraw" / "render.py",
        "status": "ready",
        "description": "Characters first coloring via ISNet anime-seg, Lab color clustering & realistic photographic hand dynamics"
    },
    "whiteboard-animator": {
        "repo": "masihsultani/whiteboard-animator",
        "category": "Text Detection & Path Sequencing",
        "path": TOOLS_DIR / "whiteboard-animator",
        "entry": TOOLS_DIR / "whiteboard-animator" / "whiteboard_animator" / "cli.py",
        "status": "ready",
        "description": "CRAFT ONNX text detection to write words vs outline shapes, skeleton endpoints & brush fill sweeps"
    },
    "hand-drawn-explainer-video-nikola": {
        "repo": "hi-nikola/hand-drawn-explainer-video-nikola",
        "category": "Dual Semantic Islands & Story QA",
        "path": TOOLS_DIR / "hand-drawn-explainer-video-nikola",
        "entry": TOOLS_DIR / "hand-drawn-explainer-video-nikola" / "scripts" / "stroke_story_preflight.py",
        "status": "ready",
        "description": "Dual semantic islands layout, stroke-by-stroke storytelling, and preflight video verification"
    },
    "animate": {
        "repo": "cth9191/animate",
        "category": "Procedural Animation & Beat Sync",
        "path": TOOLS_DIR / "animate",
        "entry": TOOLS_DIR / "animate" / "plugins" / "animate" / "skills" / "animate" / "tools" / "beats.mjs",
        "status": "ready",
        "description": "Procedural animation in 7 styles (cut paper, crosshatch, riso, math, pixel, sketchbook) with music beat mapping"
    },
    "kinodraw": {
        "repo": "edwardaiwang-svg/kinodraw",
        "category": "Doodle Matching & Camera Kinematics",
        "path": TOOLS_DIR / "kinodraw",
        "entry": TOOLS_DIR / "kinodraw" / "kinodraw",
        "status": "ready",
        "description": "Script-to-doodle semantic planner (1,760+ icons), infinite canvas camera movements, neural voice sync"
    },
    "hyperframes": {
        "repo": "heygen-com/hyperframes",
        "category": "HTML5/SVG Video Engine",
        "path": TOOLS_DIR / "hyperframes",
        "entry": TOOLS_DIR / "hyperframes" / "packages" / "cli",
        "status": "ready",
        "description": "Render HTML/CSS/GSAP directly to MP4 with 450+ ready-made templates, kinetic text & transitions"
    },
    "remotion": {
        "repo": "remotion.dev",
        "category": "React Frame-Accurate Timeline",
        "path": ROOT_DIR / "node_modules" / "remotion",
        "entry": ROOT_DIR / "node_modules" / ".bin" / "remotion",
        "status": "ready",
        "description": "React-based programmatic video rendering, composition timeline, and dynamic typography"
    },
    "ghost-editor": {
        "repo": "kurbaitaev/ghost-editor",
        "category": "Audio VAD & Video Polish",
        "path": TOOLS_DIR / "ghost-editor",
        "entry": TOOLS_DIR / "ghost-editor" / "scripts" / "vad_pauses.py",
        "status": "ready",
        "description": "Voice Activity Detection silence trimmer, audio leveling, subtitle QA & eased crossfades"
    },
    "mattpocock-skills": {
        "repo": "mattpocock/skills",
        "category": "Universal Agent Skills Standard",
        "path": TOOLS_DIR / "mattpocock-skills",
        "entry": TOOLS_DIR / "mattpocock-skills" / "skills",
        "status": "ready",
        "description": "Standardized skill specifications, progressive disclosure, and domain-driven agent architectures"
    },
    "self-learning-skills": {
        "repo": "kulaxyz/self-learning-skills",
        "category": "Automated Self-Learning",
        "path": TOOLS_DIR / "self-learning-skills",
        "entry": TOOLS_DIR / "self-learning-skills" / "skills" / "self-learning" / "SKILL.md",
        "status": "ready",
        "description": "Recognize-the-moment golden path promotion with strict passing check & ruled-out dead-end gates"
    },
    "agentbrain": {
        "repo": "frontmatters/agentbrain",
        "category": "Portable Cognitive Memory",
        "path": TOOLS_DIR / "agentbrain",
        "entry": TOOLS_DIR / "agentbrain",
        "status": "ready",
        "description": "Cross-agent persistent Markdown knowledge base keeping long-term context intact across sessions"
    },
    "context-bank": {
        "repo": "kadiresen/context-bank",
        "category": "Context-Efficient Memory Bank",
        "path": TOOLS_DIR / "context-bank",
        "entry": TOOLS_DIR / "context-bank",
        "status": "ready",
        "description": "Capped, retrieval-first project memory preventing context window saturation"
    },
    "fastsdcpu": {
        "repo": "rupeshs/fastsdcpu",
        "category": "Fast CPU Text-to-Image Engine",
        "path": TOOLS_DIR / "fastsdcpu",
        "entry": ROOT_DIR / "src" / "image_gen" / "fastsd_generator.py",
        "status": "ready",
        "description": "Ultra-fast text-to-image on CPU using Intel OpenVINO, SD-Turbo & Tiny AutoEncoder (TAESD)"
    }
}


def print_ecosystem_status():
    print("=" * 80)
    print("AI VIDEO ECOSYSTEM - 14 INTEGRATED REPOSITORIES & ENGINES")
    print("=" * 80)
    for idx, (key, info) in enumerate(ECOSYSTEM_REGISTRY.items(), start=1):
        exists = info["path"].exists()
        status_symbol = "[OK]" if exists else "[MISSING]"
        print(f"{idx:2d}. {status_symbol} {key.upper():<32} | {info['category']}")
        print(f"    Source : https://github.com/{info['repo'] if 'http' not in info['repo'] else info['repo']}")
        print(f"    Path   : {info['path'].relative_to(ROOT_DIR) if exists else info['path']}")
        print(f"    Role   : {info['description']}")
        print("-" * 80)


if __name__ == "__main__":
    print_ecosystem_status()
