# GEMINI.md / AntiGravity entry point

Đọc `AGENTS.md` trước (giao thức bộ nhớ). Khi chủ kênh nói **"làm tập tiếp theo <con vật>"**:
đọc `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md` (18 luật) + tập mẫu chuẩn vàng **`examples/ep09_reference/`** (Tập 9 Chim Cánh Cụt), rồi
làm theo `.agents/skills/core/episode-production/SKILL.md` từ Bước 0 đến Bước 8 (workflow ngắn: `.agent/workflows/lam-tap-moi.md`).
Kịch bản + giọng đọc: theo `.agents/skills/core/humor-voice/SKILL.md` (hài hước, giọng VoiceStudio cục bộ — không dùng ElevenLabs).

Công cụ chạy bằng terminal (không phụ thuộc MCP của Cursor):
- Ảnh Gemini: `node src/episode/gemini_gen.cjs projects/<slug> probe|long|shorts|extra` (Playwright + Chrome profile đã đăng nhập Google,
  `config/channel.json > chrome_profile`). Nếu AntiGravity có công cụ trình duyệt riêng cũng có thể dán prompt từ `specs/image_prompts.json`,
  lưu ảnh đúng tên vào `assets/inbox/` rồi `python src/episode/import_images.py`.
- Phân cảnh: `specs/storyboard.json` → `python src/episode/build_plans.py projects/<slug>`.
- Lệnh chạy lâu (tts ~80 phút, gemini_gen ~60 phút, render ~25 phút) chạy nền và theo dõi log, không chờ chặn.

Video tổng hợp 60-80 phút ("làm mega", "tập tổng hợp", "trọn bộ 10 tập"): làm theo `.agents/skills/core/mega-compilation/SKILL.md`
(Phần B — ảnh, giọng, render, ghép) và `docs/strategy/MEGA_COMPILATION.md`. Workflow ngắn: `.agent/workflows/lam-mega.md`.

⛔ Không bao giờ tự đăng/lên lịch YouTube — dừng sau gói SEO và chờ lệnh "đăng" kèm giờ.
