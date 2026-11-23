# wildlife-comic-studio

Xưởng sản xuất video kênh YouTube **Vẽ Chuyện Hoang Dã** (Wild Tales Sketch): video dài ≥ 8:30 + Shorts về động vật kỳ lạ,
tranh vẽ tay AI (Gemini), giọng kể hài bằng VoiceStudio/OmniVoice chạy cục bộ, render bằng Python + FFmpeg.

## Máy mới

```powershell
git clone https://github.com/hytruong-dev/wildlife-comic-studio.git
cd wildlife-comic-studio
powershell -ExecutionPolicy Bypass -File scripts\setup_new_machine.ps1
```

Chi tiết từng bước, phiên bản đã khóa và 2 bước làm tay (VoiceStudio, đăng nhập Chrome): **[SETUP_MAY_MOI.md](SETUP_MAY_MOI.md)**.

## Bắt đầu làm việc

- AI agent: đọc [`AGENTS.md`](AGENTS.md) (giao thức bộ nhớ) và [`CLAUDE.md`](CLAUDE.md).
- Làm tập mới: nói *"làm tập tiếp theo <con vật>"* → quy trình `.agents/skills/core/episode-production/SKILL.md`.
- Tập tổng hợp 60-80 phút: *"làm mega"* → `.agents/skills/core/mega-compilation/SKILL.md`.
- Lịch đăng: [`docs/LICH_DANG_VIDEO.md`](docs/LICH_DANG_VIDEO.md). Bản đồ thư mục: [`docs/CAU_TRUC_DU_AN.md`](docs/CAU_TRUC_DU_AN.md).

Video, ảnh và giọng đã render (~70 GB) **không** nằm trong repo; mỗi tập giữ `episode.json` + `specs/` để tái tạo.
