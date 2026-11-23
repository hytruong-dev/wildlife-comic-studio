---
description: Làm tập mới kênh Vẽ Chuyện Hoang Dã (video dài + Shorts + banner + thumbnail + SEO) theo chuẩn vàng Tập 9, dừng trước khi đăng
---

1. Đọc `AGENTS.md`, `.agent_memory/director_taste.md`, `.agent_memory/lessons_learned.md`, `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.
2. Đọc và làm theo `.agents/skills/core/episode-production/SKILL.md` (Bước 0 → Bước 8); kịch bản hài + giọng VoiceStudio theo
   `.agents/skills/core/humor-voice/SKILL.md`. Bắt chước `examples/ep09_reference/` (episode.json, storyboard.json).
3. Chuỗi lệnh (thay <P> = projects/tap-NN-ten, chạy từ thư mục gốc):
   - `python src/episode/pipeline.py init <P> --no N --animal "Tên"` → nghiên cứu (WebSearch) → viết `<P>/episode.json`
   - `python src/episode/pipeline.py check <P>` → sửa đến khi sạch `!!` và ước lượng ≥ 8:45
   - nền: `python src/episode/pipeline.py tts <P>`
   - viết `<P>/specs/storyboard.json` → `python src/episode/build_plans.py <P>` → `python src/episode/extra_prompts.py <P>`
   - nền: `node src/episode/gemini_gen.cjs <P> probe` → `long` → `shorts` → `extra` (thiếu ảnh: `--only … --per-chat 1`)
   - `python src/episode/import_images.py <P> --sheet` · `python src/episode/prep_banners.py <P> <P>/assets/_src` · `python src/episode/banner_sheet.py <P>` → XEM ảnh
   - tts hụt giờ: `voice_cache.py <P> snapshot` → thêm part → `voice_cache.py <P> remap` → `tts` → beat mới có `"id"`
   - `pipeline.py align <P>` → `pipeline.py spec <P>` → `python scripts/audit_beats.py <P>` → `python src/episode/target_sheet.py <P>`
   - `pipeline.py render <P> --preview` → nền `pipeline.py render <P> --force`
   - `pipeline.py qa <P>` · `python scripts/beat_sheet.py <P>` · `python scripts/hum_probe.py <P>/audio/shorts.wav <P>/renders/<slug>_shorts.mp4`
   - `pipeline.py seo <P>` · `python src/episode/episode_doc.py <P>` · `python src/memory/memory_harvester.py --log-video …`
4. Dừng sau Bước 8, báo cáo, hỏi giờ đăng. Chỉ chạy Bước 9 (`node src/episode/upload_youtube.cjs`) khi chủ kênh ra lệnh.
