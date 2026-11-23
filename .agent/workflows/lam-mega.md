---
description: Sản xuất video tổng hợp Mega Compilation 60-80 phút (10 tập lẻ → 1 video xếp hạng) + Shorts tổng hợp, dừng trước khi đăng
---

1. Đọc `AGENTS.md` (§1C), `docs/strategy/MEGA_COMPILATION.md`, `.agents/skills/core/mega-compilation/SKILL.md`.
2. `python src/mega/assemble.py plan projects/<mega>` — nếu `CHECK OK` và đã có `episode.json` + `specs/storyboard.json` thì phần lõi đã xong,
   chỉ làm Phần B (P = projects/<mega>):
   - nền: `node src/episode/gemini_gen.cjs P probe` → `long` → `shorts` → `extra` (thiếu: `--only … --per-chat 1`)
   - `python src/episode/import_images.py P --sheet` · `python src/episode/prep_banners.py P P/assets/_src` · `python src/episode/banner_sheet.py P` → XEM ảnh
   - nền: `python src/episode/pipeline.py tts P` → `pipeline.py align P` → `pipeline.py spec P` → `python src/episode/target_sheet.py P`
   - `pipeline.py render P --preview` → nền `pipeline.py render P --force`
   - nền: `python src/mega/assemble.py build P` → `assemble.py qa P` → `assemble.py seo P`
3. Dừng, báo cáo (thời lượng, chapters, điểm mid-roll), chờ lệnh "đăng" kèm giờ. Không tự chạy `upload_youtube.cjs`.
