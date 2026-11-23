"""Freeze every cameo voice of config/voice_personas.json > cast into a fixed reference clip.

OmniVoice voice-design ("instruct": "male, elderly, very low pitch") picks a NEW random timbre on every call,
so the same character would sound different in each part. This script designs each voice ONCE, saves
assets/voice_refs/cast_<id>.wav + .txt, and points the cast entry at it ("ref"), so later episodes clone it.

usage: python scripts/make_cast_refs.py [--only tham_phan,be_con] [--redo]
Runs in VoiceStudio's venv automatically (~1 min CPU per voice). Listen to each clip; --redo --only <id> to re-roll.
"""
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CFG = ROOT / "config" / "voice_personas.json"
CH = json.loads((ROOT / "config" / "channel.json").read_text(encoding="utf-8"))
LINES = {  # neutral but characterful line, ~8-10 s, no laughter (TASTE-32: no whisper)
    "tham_phan": "Phiên tòa hôm nay xét xử một vụ án rất đặc biệt. Mời bị cáo đứng lên, và hãy trả lời thật rõ ràng trước tòa.",
    "cong_to_vien": "Thưa quý tòa, bằng chứng đã quá rõ ràng. Bị cáo có mặt tại hiện trường, và không hề có một lời giải thích nào.",
    "ba_trum": "Ở khu vực này, mọi chuyện đều phải qua tay tôi. Ai muốn ăn, phải xếp hàng. Ai muốn sống, phải nghe lời.",
    "be_con": "Mẹ ơi, con đói lắm rồi! Hôm nay mình ăn gì vậy mẹ? Con muốn ra ngoài chơi một chút thôi mà!",
    "ga_khong_lo": "Cả khu rừng này là của ta. Không ai dám bước vào lãnh thổ của ta, kể cả con sư tử già kia.",
    "chu_ngo_ngac": "Ủa, cái gì vừa rơi xuống vậy? Mình đang ngủ mà... Thôi kệ, ngủ tiếp một chút nữa vậy.",
    "co_tro_ly": "Thưa giáo sư, mẫu vật đã sẵn sàng. Nhiệt độ đã tăng lên mức tối đa, và nó vẫn còn đang ngáp ạ.",
    "ong_gia_ke": "Hồi tôi còn trẻ, ở vùng này người ta kể rằng có một con vật kỳ lạ, chẳng ai dám lại gần nó cả.",
    "phat_thanh_vien": "Tin khẩn cấp! Một sự việc chưa từng có vừa xảy ra. Chúng tôi sẽ cập nhật thông tin mới nhất ngay sau đây.",
}

def main():
    only = sys.argv[sys.argv.index("--only") + 1].split(",") if "--only" in sys.argv else None
    redo = "--redo" in sys.argv
    cfg = json.loads(CFG.read_text(encoding="utf-8"))
    jobs = []
    for cid, c in cfg["cast"].items():
        if only and cid not in only:
            continue
        out = ROOT / "assets" / "voice_refs" / f"cast_{cid}.wav"
        if out.exists() and not redo:
            continue
        txt = LINES.get(cid, "Xin chào, đây là giọng mẫu của nhân vật trong kênh Vẽ Chuyện Hoang Dã.")
        out.with_suffix(".txt").write_text(txt, encoding="utf-8")
        if out.exists():
            out.unlink()
        jobs.append({"text": txt, "out": str(out), "ref": None, "instruct": c["design"], "speed": 1.0, "_id": cid})
    if jobs:
        jf = ROOT / "projects" / "_cast_jobs.json"
        jf.write_text(json.dumps(jobs, ensure_ascii=False), encoding="utf-8")
        py = Path(os.path.expandvars(CH["voice"]["voicestudio_python"]))
        subprocess.run([str(py), str(ROOT / "src/audio/omnivoice_tts.py"), "--ref", str(ROOT / CH["voice"]["reference"]),
                        "--jobs", str(jf)], check=True)
        jf.unlink(missing_ok=True)
    for cid, c in cfg["cast"].items():
        ref = ROOT / "assets" / "voice_refs" / f"cast_{cid}.wav"
        if ref.exists():
            c["ref"] = f"assets/voice_refs/cast_{cid}.wav"
            c["instruct"] = None  # timbre now comes from the frozen clip
    CFG.write_text(json.dumps(cfg, ensure_ascii=False, indent=1), encoding="utf-8")
    print("cast refs:", {k: v.get("ref") for k, v in cfg["cast"].items()})

if __name__ == "__main__":
    main()
