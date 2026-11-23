# AGENTS.md — BẢN ĐỒ ĐIỀU HƯỚNG & BỘ NÃO DI ĐỘNG CỦA DỰ ÁN

## 0. MÁY MỚI? ĐỌC `SETUP_MAY_MOI.md` TRƯỚC
> Khi mở dự án trên máy khác, hoặc chủ kênh nói "đọc toàn bộ dự án" / "cài đặt máy mới" / "setup":
> chạy `powershell -ExecutionPolicy Bypass -File scripts\setup_new_machine.ps1 -CheckOnly`. Còn dòng **THIEU** →
> làm theo **`SETUP_MAY_MOI.md`** (tự cài Python/Node/ffmpeg/tools/whisper; 2 bước tay: VoiceStudio + đăng nhập Chrome),
> rồi mới tiếp tục giao thức mục 1. Cấu hình riêng máy (Chrome profile, đường dẫn VoiceStudio) ghi `config/local.json` — không lên git.

## 1. GIAO THỨC BẮT BUỘC KHI KHỞI ĐỘNG (ZERO-RETRAINING HANDOVER PROTOCOL)
> **CHỈ DẪN TỐI CAO CHO AI (TRÊN MỌI MÁY TÍNH):**
> Dự án này tích hợp **Hệ thống Bộ Nhớ Tự Tiến Hóa (Self-Evolving Portable Memory)**. Trước khi phản hồi yêu cầu làm video của người dùng hoặc viết bất kỳ dòng code nào, bạn **BẮT BUỘC** phải đọc tuần tự 4 nguồn tri thức sau để tiếp nhận toàn bộ quá trình huấn luyện từ các phiên/máy tính trước:
> 1. `GLOSSARY.md` — Nắm vững ngôn ngữ chung và cấu trúc dữ liệu (`WordToken`, `VisualBeat`, `StrokePath`, `HandRig`, `CameraFrame`, `ProtectedRegion`).
> 2. `.agent_memory/director_taste.md` — Nắm vững 100% gu thẩm mỹ, tốc độ bàn tay vẽ, bảng màu và quy tắc bố cục của chủ dự án. Tuyệt đối không hỏi lại những điều đã được quy định trong file này.
> 3. `.agent_memory/lessons_learned.md` — Nắm vững các giải pháp kỹ thuật chuẩn (Golden Paths) và tránh xa các lỗi đã được khắc phục.
> 4. `.agent_memory/visual_metaphor_dictionary.json` & thư mục `.agents/skills/learned/` — Tái sử dụng các mẫu ẩn dụ hình ảnh và kỹ năng bố cục mà chủ dự án đã phê duyệt trước đó.
>
> **Sau khi đọc xong, hãy mở đầu câu trả lời bằng dòng xác nhận:**
> *"🧠 [Memory Synced] Đã đồng bộ bộ nhớ dự án (N quy tắc đạo diễn, M mẫu ẩn dụ hình ảnh, K kỹ năng đã học). Sẵn sàng sản xuất video tiếp theo theo đúng chuẩn của bạn!"*

## 1B. SẢN XUẤT TẬP MỚI — "làm tập tiếp theo <con vật>"
> Khi chủ kênh yêu cầu làm tập mới (vd "làm tập tiếp theo", "làm tập về tôm tít"): đọc **`docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`**
> (18 luật + mọi bài học Tập 6→9), xem tập mẫu chuẩn vàng **`examples/ep09_reference/`** (Tập 9 Chim Cánh Cụt — làm 1 lượt QA PASS), rồi làm theo
> **`.agents/skills/core/episode-production/SKILL.md`**. Bản đồ thư mục + công cụ: **`docs/CAU_TRUC_DU_AN.md`**.
> Phân cảnh viết ở `specs/storyboard.json` → `src/episode/build_plans.py`; ảnh Gemini tự động bằng `node src/episode/gemini_gen.cjs`
> (Playwright + Chrome profile đã đăng nhập, **không cần Playwright MCP**); chèn part giọng dùng `src/episode/voice_cache.py`.
> Giọng tempo 1.10, video dài **≥ 8:30** (thiếu thì viết thêm nội dung). Mỗi tập xong phải sinh `EPISODE_SPEC.md` (`src/episode/episode_doc.py`). Tự làm hết từ nghiên cứu → kịch bản →
> giọng → ảnh Gemini → render dài + Shorts → QA → SEO, **không hỏi lại** những gì đã quy định.
> Kịch bản phải **hài hước + thú vị** và giọng đọc dùng **VoiceStudio (OmniVoice, cục bộ, miễn phí)** theo
> **`.agents/skills/core/humor-voice/SKILL.md`**. ElevenLabs đã bỏ hẳn — không dùng lại, không xin API key.
> **Từ Tập 9: mỗi tập 1 FORMAT kể chuyện + 1 PERSONA giọng khác nhau** (`config/series_roadmap.json`,
> `docs/strategy/FORMAT_KE_CHUYEN.md`), giọng đổi mood theo tình huống + cameo vai phụ (`docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).
> ⛔ **KHÔNG tự đăng / lên lịch YouTube** — dừng sau gói SEO, chờ chủ kênh ra lệnh "đăng".
> 📅 **Lịch đăng chuẩn: `docs/LICH_DANG_VIDEO.md`** (sinh bởi `src/episode/publish_schedule.py`, TASTE-68: dài 17:00 ngày D,
> Shorts 11:30 ngày D+1, mega thứ Bảy 17:00). Lệnh "đăng" không kèm giờ → `publish_schedule.py --show <N|mega-NN>` lấy đúng ngày giờ.
> Bộ công cụ: `src/episode/` (`pipeline.py`, `build_plans.py`, `extra_prompts.py`, `gemini_gen.cjs`, `import_images.py`, `prep_banners.py`,
> `banner_sheet.py`, `target_sheet.py`, `voice_cache.py`, `episode_doc.py`, `upload_youtube.cjs`); cấu hình kênh `config/channel.json`;
> ví dụ hoàn chỉnh `examples/ep09_reference/` (mới) và `examples/ep06_reference/` (khung cũ 6 chương). Kỹ năng whiteboard-director (Cổng 1 dùng edge-tts) là quy trình cũ, KHÔNG dùng cho tập mới.

## 1C. VIDEO TỔNG HỢP — "làm mega" / "làm tập tổng hợp" / "trọn bộ 10 tập"
> Cứ 10 tập lẻ ra 1 video tổng hợp 60-80 phút (cẩm nang V5 Phần 2: `docs/strategy/CAM_NANG_V5_MEGA_COMPILATION_GOC.md`).
> Luật + định dạng: **`docs/strategy/MEGA_COMPILATION.md`**; làm theo **`.agents/skills/core/mega-compilation/SKILL.md`**;
> công cụ `src/mega/` (`transcribe_sources.py`, `silences.py`, `show_transcript.py`, `part_map.py`, `probe_range.py`, `assemble.py check|plan|build|seo|qa`).
> **Từ 09/11/2026 mặc định = NỘI DUNG MỚI HOÀN TOÀN** (TASTE-67): mẫu **`projects/mega-01-dai-hoi-sinh-ton/`** ("Đại Hội Sinh Tồn #1",
> 14 chương, ~60:35, 471 ảnh) đã xong phần lõi (`content/*.md` → `src/mega/build_from_content.py`, `pipeline.py check` sạch) —
> việc còn lại: ảnh Gemini → giọng → render như tập thường (skill Kiểu A, Phần 2). Kiểu cắt ghép (`projects/mega-01-bang-phong-than/`,
> `assemble.py`) chỉ khi chủ kênh yêu cầu rõ. ⛔ Không tự đăng.

## 1D. NGHIÊN CỨU KÊNH & ĐỐI THỦ — "phân tích kênh", "roast kênh", "nghiên cứu đối thủ", "ý tưởng tập sau", "tiêu đề/thumbnail tốt hơn"
> Bộ 17 skill TubeLab ở `.agents/skills/tubelab/` — đọc **`.agents/skills/tubelab/README_KENH.md`** trước (skill nào hợp kênh,
> chạy miễn phí bằng yt-dlp/YoutubeTags hay cần TubeLab MCP trả phí). Outlier ratio miễn phí: `python src/seo/channel_outliers.py [kênh]`.
> Báo cáo ghi `docs/research/`. Không tự đăng ký TubeLab, không tiêu credit, không sửa gì trên YouTube khi chưa được yêu cầu.
> **Mỗi tập mới tự chạy 3 bước** (đã gắn vào `episode-production`): `python src/seo/episode_research.py projects/<slug> ideas|thumbs|titles`
> (comment-mining ở Bước 0, thumbnail-concepts trước T01, title-formulas trước `pipeline.py seo`), loài hiếm thêm `--en "English name"`.

## 2. GIAO THỨC TỰ HỌC LIÊN TỤC (CONTINUOUS LEARNING DUTY)
Trong suốt cuộc trò chuyện với người dùng:
- Mỗi khi người dùng góp ý sửa đổi bố cục, tốc độ, màu sắc hoặc khen ngợi một phân cảnh, bạn PHẢI gọi `python src/memory/memory_harvester.py` (hoặc cập nhật trực tiếp vào `.agent_memory/`) NGAY TRONG LƯỢT PHẢN HỒI ĐÓ trước khi render lại video.
- Khi hoàn thành xuất file MP4 cuối cùng của một dự án, bạn PHẢI chạy bước `/retro` (Cổng kiểm duyệt số 5) để ghi nhật ký vào `.agent_memory/production_log.md` và đúc kết kỹ năng mới vào `.agents/skills/learned/` nếu có.

## 3. CÁC LỆNH VẬN HÀNH NHANH (QUICK RUN COMMANDS)
- Kiểm tra trạng thái bộ nhớ:
  ```bash
  python src/memory/memory_harvester.py --status
  ```
- Thêm quy tắc thẩm mỹ đạo diễn mới:
  ```bash
  python src/memory/memory_harvester.py --add-taste TASTE-08 "Mô tả quy tắc mới"
  ```
- Thêm bài học kỹ thuật đã kiểm chứng:
  ```bash
  python src/memory/memory_harvester.py --add-lesson LESSON-06 "Triệu chứng" "Cách làm sai cần tránh" "Giải pháp chuẩn đã kiểm chứng"
  ```
- Thêm tổ hợp ẩn dụ hình ảnh:
  ```bash
  python src/memory/memory_harvester.py --add-metaphor "từ khóa" "layout-pattern" "prim1,prim2" "col1,col2" "Ghi chú bố cục"
  ```
- Kiểm tra chất lượng video tự động (Self-QA):
  ```bash
  node src/cli/qa_checker.mjs projects/<tên-dự-án>/storyboard.json
  ```
- Render video hoàn chỉnh:
  ```bash
  node src/cli/build_video.mjs projects/<tên-dự-án>/storyboard.json --export projects/<tên-dự-án>/output.mp4
  ```

## 4. HỆ SINH THÁI 13 CÔNG NGHỆ VIDEO AI ĐÃ TÍCH HỢP (UNIFIED AI VIDEO ECOSYSTEM)
Dự án đã tích hợp và kiểm thử 13 kho công nghệ hàng đầu thế giới trong thư mục `tools/` và `node_modules/`:
1. **`geeklee/srt-whiteboard-animation`** (`tools/srt-whiteboard-animation`): Bộ dựng vẽ bảng trắng luồng (stream ink->color) với cơ chế phân vùng che chắn (mask partition orchestration) & rig bàn tay thực.
2. **`letuandat131/whiteboard-animation-vi`** (`tools/whiteboard-animation-vi`): Tách chủ thể/nhân vật tự động bằng SkyTNT Anime Segmentation (ISNet), gom màu trong không gian Lab & tô màu nhân vật trước bối cảnh (subject-first coloring).
3. **`masihsultani/whiteboard-animator`** (`tools/whiteboard-animator`): Nhận diện chữ viết bằng CRAFT ONNX model để viết từng chữ thay vì viền khối, định tuyến nét vẽ khung xương TSP & quét cọ góc.
4. **`hi-nikola/hand-drawn-explainer-video-nikola`** (`tools/hand-drawn-explainer-video-nikola`): Bố cục Hai đảo ngữ nghĩa song song (Dual Semantic Islands) & quy trình tiền kiểm tra preflight video.
5. **`cth9191/animate`** (`tools/animate`): Hoạt họa Canvas theo 7 phong cách thủ công (cut paper, crosshatch, riso, math, pixel, sketchbook) & phân tích nhịp nhạc beat-mapping (`beats.mjs`).
6. **`edwardaiwang-svg/kinodraw`** (`tools/kinodraw`): Bộ điều hướng kịch bản khớp doodle (1.760+ hình vẽ), chuyển động camera bảng trắng vô tận & đồng bộ giọng đọc nơ-ron Kokoro.
7. **`heygen-com/hyperframes`** (`tools/hyperframes`): Khung dựng video từ HTML5/CSS/GSAP với hơn 450 component có sẵn, kinetic typography và biểu đồ chuyển động.
8. **`remotion.dev`** (`node_modules/remotion`): Framework React kết xuất video từng khung hình chuẩn xác, phụ đề động và visualizer.
9. **`kurbaitaev/ghost-editor`** (`tools/ghost-editor`): Cắt tỉa khoảng lặng giọng nói tự động (VAD), cân bằng âm thanh giọng đọc, kiểm soát kích thước phụ đề & chuyển cảnh mượt mà xfade.
10. **`mattpocock/skills`** (`tools/mattpocock-skills`): Chuẩn cấu trúc Agent Skills tiến hóa theo module `SKILL.md` phục vụ kỹ sư AI.
11. **`kulaxyz/self-learning-skills`** (`tools/self-learning-skills`): Tự động đúc kết kỹ năng từ phiên làm việc thực tế với bộ lọc kiểm duyệt 3 cổng khắt khe.
12. **`frontmatters/agentbrain`** (`tools/agentbrain`): Bộ não bộ nhớ di động đa tác tử Markdown giữ nguyên ngữ cảnh qua nhiều phiên làm việc.
13. **`kadiresen/context-bank`** (`tools/context-bank`): Tối ưu hóa dung lượng token và ngân sách bộ nhớ tránh quá tải context window.
14. **`rupeshs/fastsdcpu`** (`tools/fastsdcpu`): Tạo hình ảnh từ văn bản siêu tốc trên CPU bằng Intel OpenVINO, SD-Turbo (1-step inference ~2.7s) và Tiny AutoEncoder (TAESD) giải phóng RAM, phục vụ vẽ minh họa và doodle cho kịch bản video.

Kiểm tra trạng thái hệ sinh thái bằng lệnh:
```bash
python src/hub/ai_video_ecosystem.py
```
