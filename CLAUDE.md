# CLAUDE.md

**Máy mới / "đọc toàn bộ dự án"**: làm theo `SETUP_MAY_MOI.md` (một lệnh `scripts\setup_new_machine.ps1`) trước mọi việc khác.

Đọc `AGENTS.md` trước (giao thức bộ nhớ). Khi chủ kênh nói **"làm tập tiếp theo <con vật>"**:
đọc `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md` (18 luật) + tập mẫu chuẩn vàng **`examples/ep09_reference/`** (Tập 9 Chim Cánh Cụt), rồi
làm theo `.agents/skills/core/episode-production/SKILL.md` từ đầu đến cuối (giọng đa mood tempo TB ≥ 1.10, video dài ≥ 8:30).
Kịch bản + giọng đọc: theo `.agents/skills/core/humor-voice/SKILL.md` (hài hước, giọng VoiceStudio cục bộ — không dùng ElevenLabs).
Ảnh Gemini: `node src/episode/gemini_gen.cjs` (không cần Playwright MCP). Phân cảnh: `specs/storyboard.json` → `src/episode/build_plans.py`.

Video tổng hợp 60-80 phút ("làm mega", "tập tổng hợp"): `docs/strategy/MEGA_COMPILATION.md` + `.agents/skills/core/mega-compilation/SKILL.md`
— mặc định NỘI DUNG MỚI HOÀN TOÀN (mẫu `projects/mega-01-dai-hoi-sinh-ton/`), không cắt ghép tập cũ trừ khi được yêu cầu.

⛔ Không bao giờ tự đăng/lên lịch YouTube — dừng sau gói SEO và chờ lệnh "đăng".
📅 Khi chủ kênh nói "đăng" (có hoặc không kèm giờ): ngày giờ lấy từ **`docs/LICH_DANG_VIDEO.md`** —
`python src/episode/publish_schedule.py --show <số tập|mega-NN>` in đúng lịch + lệnh upload. Giờ chủ kênh nói rõ thì ưu tiên giờ đó.
Sau mỗi lần upload chạy lại `python src/episode/publish_schedule.py` để cập nhật docs.
