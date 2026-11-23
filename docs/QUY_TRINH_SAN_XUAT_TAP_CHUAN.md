# QUY TRÌNH SẢN XUẤT 1 TẬP CHUẨN — "Vẽ Chuyện Hoang Dã"
### Tổng hợp mọi thứ đã làm và đã sửa từ Tập 6 (Gấu Nước) → Tập 7 (Tôm Tít) → **Tập 9 (Chim Cánh Cụt — chuẩn vàng hiện tại, làm 1 lần QA PASS)**

> **Ai đọc file này:** mọi AI (Cursor, Antigravity, Claude, Codex…) hoặc người dựng video trước khi làm tập mới.
> **Thứ tự đọc bắt buộc:** `AGENTS.md` → file này → `.agents/skills/core/episode-production/SKILL.md` →
> `.agents/skills/core/humor-voice/SKILL.md` → **tập mẫu `examples/ep09_reference/`** (episode.json + storyboard.json + EPISODE_SPEC.md).
> Lệnh kích hoạt: chủ kênh nói **"làm tập tiếp theo <con vật>"**. ⛔ Không bao giờ tự đăng YouTube.

---

## 0. Mười tám điều luật không được phá (rút ra từ lỗi thật của Tập 7 → Tập 9)

| # | Luật | Lỗi Tập 7 đã gặp nếu phá luật |
|---|---|---|
| 1 | **Mỗi câu/ý thoại = 1 hình riêng**, vẽ đúng thứ đang nói. Không dùng lại hình cho ý khác (`Image reuse: {}`). | Hình lặp, hình không khớp lời đang nói |
| 2 | Video dài chỉ dùng **ảnh ngang 16:9 riêng** (`L01…`). Không bao giờ lấy ảnh dọc Shorts (`S…`) cho video dài. | Ảnh dọc bị co nhỏ giữa khung |
| 3 | Mỗi hình giữ **3–15 giây**. >15s → tách câu, thêm hình. | Đứng hình lâu, người xem thoát |
| 4 | Sticker số liệu **luôn có `target: [x, y]`** → renderer vẽ mũi tên cong + vòng mục tiêu chỉ **đúng chi tiết** trong tranh. | Popup trôi nổi, không có mũi tên |
| 5 | Tag cảm xúc `[laughter]`… **chỉ cho giọng đọc**, không bao giờ hiện trên phụ đề. | Phụ đề hiện "[laughter] nội dung" |
| 6 | Lời đọc viết số bằng chữ, **phụ đề hiện số** qua `display_fix` ("hai mươi xăng-ti-mét" → `20cm`). | Phụ đề hiện chữ "mười ngàn bốn trăm g" |
| 7 | Âm thanh VoiceStudio 24 kHz: **`aresample=48000` đứng ĐẦU** chuỗi filter, trước highpass/lowpass. | Tiếng ù/rè suốt Shorts (sàn nhiễu -22 dBFS) |
| 8 | Đổi ảnh/beat/sticker → `spec` rồi `render --force`. Không `--force` = renderer dùng lại cảnh cũ đã cache. | Render 30s, video vẫn ảnh cũ |
| 9 | Giọng đọc **tempo 1.10** (nhanh, vui) và video dài **≥ 8:30**. Thiếu → **viết thêm nội dung**, không bao giờ giảm tempo. | Giọng lề mề; hoặc video < 8:30 |
| 10 | **Kiểm tra từng chi tiết trước khi báo xong**: audit beat, bảng ảnh, khung hình thật tại sticker, hum probe, QA. | Chủ kênh phải tự phát hiện lỗi |
| 11 | **Mỗi tập một FORMAT kể chuyện + một PERSONA giọng** (`config/series_roadmap.json`), không trùng tập liền trước. Hết công thức "6 chương + RPG" cố định. Chi tiết: `docs/strategy/FORMAT_KE_CHUYEN.md`. | Kênh lặp một màu, người xem chán |
| 12 | **Giọng đổi theo tình huống**: ≥ 3 mood/tập, không mood > 50%, 2-6 câu cameo vai phụ, tempo trung bình ≥ 1.10. Chi tiết: `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`. | Giọng đều đều từ đầu tới cuối |
| 13 | **Phân cảnh viết trong `specs/storyboard.json`, sinh plan + prompt bằng `src/episode/build_plans.py`** — không viết tay `longform_plan.json`. Công cụ tự chép lời thoại nguyên văn vào prompt và chặn lỗi cụm từ/sticker trước khi tốn giờ tạo ảnh. | Prompt lệch lời; cụm `at` sai phát hiện muộn sau khi đã tạo ảnh (Tập 7-8) |
| 14 | **Cụm `at` phải DUY NHẤT trong chương** (spec lấy lần xuất hiện đầu tiên). | Tập 9: "Về bằng chứng số…" lặp 4 lần → beat nhảy ngược |
| 15 | **Chèn part giữa chương → `voice_cache.py snapshot` trước, `remap` sau** (cache giọng đặt tên theo vị trí). Chèn beat sau khi đã có ảnh → beat mới mang `"id"` số mới; bỏ beat → `skip_numbers`. | Giọng cũ ghép nhầm lời mới; ảnh cũ lệch tên |
| 16 | **Không tin ước lượng thời lượng có biên mỏng**: `check` phải báo ≥ 8:45 (biên 15s). Thật ra có thể hụt vài giây. | Tập 9 bản đầu: ước 8:47 → thật 8:19 (đã hiệu chỉnh công thức) |
| 17 | **Ảnh Gemini tạo bằng `src/episode/gemini_gen.cjs`** (Playwright + profile Chrome đã đăng nhập), không phụ thuộc Playwright MCP. Chạy lại bao nhiêu lần cũng chỉ tạo ảnh còn thiếu. | MCP chưa nạp → kẹt cả buổi; lấy nhầm ảnh cũ |
| 18 | **Huyền thoại phổ biến phải kiểm chứng**; nếu khoa học nói khác → biến nó thành cú bẻ lái (không kể sai). | Tập 9 "cố ý đẩy bạn dò hải cẩu" = sách thiếu nhi; khoa học: chen lấn vô tình |
| 19 | **Teaser tập sau bằng bóng đen bí ẩn (TASTE-68 — chủ kênh chốt 09/11/2026)**: TUYỆT ĐỐI KHÔNG đọc thẳng tên con vật tập sau! Tranh vẽ bóng đen (solid black silhouette / shadowed cutout) + dấu hỏi; lời đọc đưa 2-3 manh mối sốc để khán giả đoán và bình luận. | Đọc toạc tên con vật làm mất tính tò mò tương tác |
| 20 | **Tiêu đề KHÔNG ghi số thời lượng (phút) & Màn hình kết thúc tự động 100% (TASTE-70 — chủ kênh chốt 10/11/2026)**: Tuyệt đối không ghi `[60 PHÚT]` hay số phút vào tiêu đề (YouTube đã có badge thời gian trên thumbnail; ghi vào làm tiêu đề dài bị cắt cụt `...`). Khi đăng video, script upload bắt buộc tự động gắn trọn gói Màn hình kết thúc (1 Video phù hợp + 1 Playlist Thế Giới Động Vật + 1 Nút đăng ký) ở 20s cuối. | Tiêu đề bị cắt cụt; video thiếu màn hình kết thúc làm mất người xem quay lại |

---

## 1. Bức tranh tổng thể (pipeline)

```
pipeline.py init (format/persona từ roadmap) ─► nghiên cứu ─► episode.json (kịch bản hài + mood/cast + display_fix + art + SEO)
        │                                                     pipeline.py check  (lint kịch bản + ước lượng ≥ 8:45)
        ├─► pipeline.py tts    (VoiceStudio, mood tempo) ─► audio/sceneXX.wav, shorts.wav   [nền ~80 phút]
        │       └ thiếu giờ: voice_cache.py snapshot → thêm part → remap → tts
        ├─► specs/storyboard.json ─► src/episode/build_plans.py ─► longform_plan + shorts_plan + image_prompts  [song song]
        │   src/episode/extra_prompts.py ─► extra_prompts.json (banner chương, banner Shorts, thumbnail)
        │   node src/episode/gemini_gen.cjs <P> long|shorts|extra ─► assets/inbox ─► import_images.py --sheet
        │   prep_banners.py + banner_sheet.py (đọc chính tả)
        │
        ├─► pipeline.py align  (Whisper + chữ kịch bản)   ─► long_words_fixed.json, shorts_words.json
        ├─► pipeline.py spec   ─► "spec OK"  ─► scripts/audit_beats.py ─► src/episode/target_sheet.py (mũi tên)
        ├─► pipeline.py render --force ─► scripts/beat_sheet.py (xem khung hình thật) ─► hum_probe.py
        ├─► pipeline.py qa (≥ 8:30, -14 LUFS, Shorts 40–59.5s) ─► pipeline.py seo
        └─► src/episode/episode_doc.py ─► projects/<slug>/EPISODE_SPEC.md  (tài liệu đầy đủ của tập)
                                                     ⛔ DỪNG — chờ lệnh "đăng" + giờ
```

Cấu trúc thư mục 1 tập (`projects/tap-NN-<ten>/`):

| File | Vai trò |
|---|---|
| `episode.json` | `format`, `persona`, `nickname`, `sources`, `art`, `longform.scenes[]` (`badge`, `banner_title`, `chapter_title`, `hook`, `mood`, `parts` ≤ 1.300 ký tự, part `{text, mood}`/`{text, cast}`), `shorts`, `display_fix`, `whisper_prompt`, `seo` |
| `audio/vs/<scene>_pN.wav` | giọng thô VoiceStudio (cache — xóa file để đọc lại 1 part) |
| `audio/sceneXX.wav`, `sceneXX_parts_duration.json` | giọng đã tempo + 0,4s đầu + 0,35s nghỉ giữa part |
| `audio/long_words_fixed.json` | mốc thời gian từng chữ (chữ kịch bản đã hiện số) — nguồn sự thật khi đặt beat |
| `specs/storyboard.json` | **phân cảnh do người/AI viết** (nhân vật cố định, mỗi câu 1 beat: at, layout, stickers+target, impacts, id) |
| `specs/longform_plan.json`, `shorts_plan.json`, `image_prompts.json`, `image_catalog.md` | **sinh bởi `build_plans.py`** — không sửa tay |
| `specs/extra_prompts.json` | sinh bởi `extra_prompts.py` từ `episode.json > art` + `badge`/`banner_title` |
| `assets/inbox/` · `assets/_src/` · `assets/banners/` | ảnh Gemini thô (.txt dataURL) · banner thô · banner đã cắt nền |
| `audio/vs/_cache_index.json` | ảnh chụp text ↔ file cache giọng (`voice_cache.py`) |
| `specs/longform_spec.json`, `shorts_spec.json` | do `spec` sinh ra, renderer đọc |
| `specs/image_prompts.json` | prompt Gemini nguyên văn của từng ảnh |
| `specs/image_catalog.md` | mô tả NỘI DUNG THẬT của từng file ảnh (đã xem tận mắt) |
| `renders/` | mp4 dài/Shorts/thumbnail, `beat_audit/*.jpg`, `long_v2/sceneXX.mkv` (cache) |
| `EPISODE_SPEC.md` | tài liệu tập đầy đủ (sinh tự động) |

---

## 2. Xây dựng nội dung

### 2.0 Chọn format & persona (từ Tập 9)
Tra `config/series_roadmap.json` → `format` + `persona` của tập. Nguyên liệu nghiên cứu bên dưới vẫn cần đủ,
nhưng **xếp vào khung của format** (F1 = 4 lần khám bệnh, F3 = 4 bằng chứng + phán quyết, F4 = mốc giờ trong ngày,
F5 = 5 level thử thách…). Badge banner chương đổi theo format (`BỆNH ÁN #01`, `06:00 SÁNG`, `BẰNG CHỨNG #1`, `LEVEL 3`…).

### 2.1 Nghiên cứu (WebSearch, 6–8 sự thật kiểm chứng được)
Cần đủ 6 loại "nguyên liệu" (bảng dưới là cách xếp kiểu cũ F7/Tập 7 — format khác xếp lại theo khung của format):

| Chương | Nguyên liệu | Tập 7 Tôm Tít (mẫu) |
|---|---|---|
| 1 Hook | Nghịch lý gây sốc + biệt danh nhân vật | "dài chưa đầy 20cm, lòe loẹt như công chúa… nhưng đấm nhanh ngang đạn súng trường" → **"Mike Tyson của đại dương"** |
| 2 Chỉ số RPG | HP/ATK/DEF/SPD + so sánh đời thường | ATK 1.500 N, SPD 10.400g, chớp mắt 0,1s = 30 cú đấm, phi công 9g ngất vs càng ×1.000 |
| 3 Cơ chế khoa học | Giải thích siêu năng lực, Việt hóa thuật ngữ | Bọt khí Cavitation 4.700°C, phát quang; giáp nano Bouligand bẻ cong vết nứt |
| 4 Cú bẻ lái | Điểm yếu bất ngờ, bi hài | Lột xác → mềm như thạch, sợ cả ốc sên; dọa ma bằng bóng; ác mộng bể cá cảnh |
| 5 Chuyện có thật | Năm, nơi chốn, tên | Tháng 4/1998, thủy cung Norfolk (Anh), tôm "Tyson" 10cm đấm nứt kính; mắt 16 loại tế bào màu → cảm biến ung thư |
| 6 Bài học + CTA | Bài học sống, câu hỏi bình luận, teaser tập sau | "Mạnh ≠ bất khả chiến bại, biết thu mình khi yếu"; teaser Cá Thòi Lòi |

Không bịa số. Phóng đại thì nói rõ "cứ như", "kiểu như".

### 2.2 Viết lời hài (chi tiết ở `humor-voice` skill)
- Công thức đoạn: **Sự thật sốc (số liệu) → So sánh đời thường → Punchline ngắn ≤ 8 từ** + `[laughter]`.
- Mỗi 20–30s lời đọc có ≥ 1 chỗ cười; biệt danh xuất hiện ≥ 4 lần; mỗi chương kết bằng punchline/câu hỏi.
- Ví dụ đã duyệt Tập 7:
  - *"Cua biển mai dày ư? Một đấm vỡ nát! Vỏ ốc xà cừ cứng như đá ư? Hai đấm thành bột vụn!"* (hỏi tu từ dồn dập)
  - *"Một phe đấm bốc, một phe đấu kiếm, đúng là cả một gia tộc võ lâm dưới đáy biển!"* (hệ quy chiếu đời sống)
  - *"Ra ngoài thì đấm nứt kính, về nhà thì ngoan như mèo!"* (punchline đối xứng)
- **Mỗi câu phải "vẽ được"** — vì mỗi câu sẽ thành 1 hình. Câu trừu tượng → thêm hình ảnh cụ thể (đạo cụ, so sánh).

### 2.3 Viết cho giọng đọc & phụ đề
| Viết trong lời đọc | Khai báo `display_fix` | Phụ đề hiện |
|---|---|---|
| `hai mươi xăng-ti-mét` | `"hai mươi xăng-ti-mét": "20cm"` | 20cm |
| `mười ngàn bốn trăm g` | `"mười ngàn bốn trăm g": "10.400g"` | 10.400g |
| `bốn ngàn bảy trăm độ C` | `"bốn ngàn bảy trăm độ C": "4.700°C"` | 4.700°C |
| `Cáp-vi-tây-sơn` | `"Cáp-vi-tây-sơn": "Cavitation"` | Cavitation |
| `A-T-K` | `"A-T-K": "ATK"` | ATK |
- Cụm nhiều chữ được thay trước (dài trước ngắn sau) rồi mới tách từ → mốc thời gian vẫn đúng.
- **Mọi con số đọc bằng chữ đều phải có `display_fix`.** Sau `align`, mở `long_words_fixed.json` tìm chữ số còn sót dạng chữ.
- `whisper_prompt`: liệt kê tên riêng + số khó để Whisper nghe đúng.

### 2.4 Độ dài & tempo (luật mới 2026-11-08)
- Giọng: VoiceStudio speed 1.05 + **atempo 1.10** (đặt trong `config/channel.json > voice.tempo_long`).
- Đo thật Tập 7: ≈ **17 ký tự/giây ở tempo 1.0** → ở tempo 1.10 ≈ 18,7 ký tự/s.
- Video dài **≥ 8:30 (510s)** = lời đọc ≥ ~9.200 ký tự (không tính tag) + 20s intro/outro. Nhắm **9.300–10.000 ký tự** (≈ 8:35–9:15).
- `pipeline.py check` in ước lượng; `pipeline.py tts` in thời lượng thật và cảnh báo `TOO SHORT`.
- Thiếu → `python scripts/voice_budget.py projects/<slug> 515` cho biết cần thêm bao nhiêu ký tự → viết **part mới** (sự thật thú vị/chuyện vui) cuối chương 2–5, chạy lại `tts` (chỉ part mới được tạo, ~2 phút CPU cho 300 ký tự).
- Shorts: tempo tự tính để giọng ≤ 53s, tối thiểu 1.10; mục tiêu 45–53s.

---

## 3. Giọng đọc VoiceStudio
- Engine OmniVoice cục bộ, clone `assets/voice_refs/adam_funny_ep1.wav` (vui). Không ElevenLabs/edge-tts/gTTS.
- Tag hợp lệ: `[laughter] [sigh] [surprise-oh] [surprise-ah] [surprise-wa] [question-ah] [question-oh] [dissatisfaction-hnn]`.
- `[laughter]` ngay SAU punchline; `[surprise-*]` ĐẦU câu số liệu sốc; ≤ 2 tag/part liền nhau thì bỏ bớt.
- Chuỗi xử lý (đã khóa trong `pipeline.py tts`):
  - Dài: `atempo=1.10` → 48 kHz stereo → nối 0,4s đầu + 0,35s nghỉ giữa part (`LESSON-62`).
  - Shorts: `aresample=48000,atempo=…,highpass=f=75,lowpass=f=12000,acompressor…` — **resample phải đứng đầu** (`LESSON-73`).
- Sau `tts` luôn `align`: match mỗi chương ≥ 0,9 (Tập 7: 0,92–0,95). < 0,8 → xóa `audio/vs/<part>.wav`, đọc lại.
- **Đa phong cách (từ Tập 9):** persona theo format, `mood` theo tình huống (6 mood: hào hứng, dồn dập, trầm bí ẩn,
  nghiêm trang giả, bi hài, ấm áp — mỗi mood có clip tham chiếu/tempo riêng), `cast` cho 9 giọng vai phụ
  (thẩm phán, bé con, bà trùm, gã khổng lồ…, clip ở `assets/voice_refs/cast_*.wav`). Toàn bộ: `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`.

---

## 4. Tạo ảnh Gemini (16:9 dài, 9:16 Shorts)

### 4.1 Prompt mở chat (quy chuẩn + nhân vật cố định) — mẫu Tập 7
```text
Tạo hình ảnh (cảnh 1/N của video YouTube về Tôm Tít). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9;
phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng
tươi sáng, biểu cảm hoạt hình hài hước cường điệu; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số,
không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Tôm Tít (peacock mantis shrimp)
hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi có điểm màu cầu vồng, hai mắt to lồi trên cuống biểu cảm,
hai càng búa gập trước ngực như võ sĩ. NỘI DUNG CẢNH 1 (lời thoại: "<câu>"): <bố cục>.
```

### 4.2 Prompt từng hình
```text
HÌNH L60 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật Tôm Tít mai xanh ngọc, râu đỏ cam, mắt lồi
trên cuống, hai càng búa; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu thoại nguyên văn>".
Bố cục: <BÊN TRÁI …; Ở GIỮA …; BÊN PHẢI …; ai làm gì, biểu cảm; đạo cụ hình ảnh hóa con số>.
```
Quy tắc viết bố cục (rút ra từ 66 ảnh Tập 7):
1. **Chép nguyên văn câu thoại** vào prompt — Gemini vẽ đúng ý hơn hẳn.
2. Chia vùng TRÁI / GIỮA / PHẢI rõ ràng → biết trước toạ độ để đặt `target` sticker.
3. **Hình ảnh hóa con số bằng đạo cụ**: 4.700°C → nhiệt kế kịch trần cạnh Mặt Trời; 9g → phi công ngất trong buồng lái; 20 năm → vạch khắc đếm trên vách hang. Sticker sẽ chỉ vào đạo cụ đó.
4. So sánh = chia đôi khung (người vs tôm, kính thường ✗ vs acrylic ✓).
5. Câu nói về nhân vật khác → ghi rõ "KHÔNG có Tôm Tít trong cảnh này".
6. Họ hàng/nhân vật phụ → mô tả khác màu rõ (phe đâm: nâu vàng sọc) để không nhầm nhân vật chính.
7. Không bao giờ yêu cầu chữ/số trong tranh (trừ thumbnail).

### 4.3 Tạo & lấy ảnh tự động — `src/episode/gemini_gen.cjs` (chuẩn Tập 9, không cần MCP)
```bash
node src/episode/gemini_gen.cjs projects/<slug> probe            # signedIn: true ? (false -> đăng nhập Google 1 lần trong cửa sổ mở ra)
node src/episode/gemini_gen.cjs projects/<slug> long             # nền; ~30s/ảnh; 20 ảnh/chat, chat mới tự gửi lại quy chuẩn + nhân vật
node src/episode/gemini_gen.cjs projects/<slug> shorts
node src/episode/gemini_gen.cjs projects/<slug> extra            # banner chương C01.., banner Shorts B00, thumbnail T01
node src/episode/gemini_gen.cjs projects/<slug> long --only L09,L23 --per-chat 1   # ảnh bị timeout
python src/episode/import_images.py projects/<slug> --sheet      # khử watermark (nếu có), chia L/S/T, bảng xem nhanh
python src/episode/prep_banners.py projects/<slug> projects/<slug>/assets/_src && python src/episode/banner_sheet.py projects/<slug>
```
- Đóng mọi Chrome đang dùng profile `config/channel.json > chrome_profile` trước khi chạy (profile bị khóa → lỗi mở trình duyệt).
- Prompt lấy từ `specs/image_prompts.json` (do `build_plans.py` sinh, đã chép lời thoại nguyên văn). Ảnh đã có → bỏ qua; chạy lại thoải mái.
- Lấy ảnh trong `model-response` **mới** + chặn trùng hash → không còn lỗi ảnh lệch tên của Tập 7. Log: `assets/inbox/_gen_log.jsonl`.
- ~5% ảnh timeout (Gemini trả lời chữ) → `--only … --per-chat 1`; vẫn lỗi → viết lại `layout` nhẹ nhàng hơn (vd chủ đề "phân": thêm
  "phong cách hoạt hình hài thân thiện trẻ em").
- Hết lượt (3 lỗi liên tiếp) → `--account 1` (tài khoản Google thứ 2 trong cùng profile).
- **Xem bằng mắt** `renders/snapshots/sheet_long.jpg`, `sheet_shorts.jpg`, `banners.jpg` (đọc từng chữ tiếng Việt), thumbnail.
- Cách cũ bằng Playwright MCP (Tập 7) vẫn dùng được khi cần thao tác tay; `.cursor/mcp.json` đã khai báo server `playwright`.

> ⚠ Lỗi Tập 7 (bản đầu): lấy ảnh theo `img` cũ của chat → nhiều file trùng hoặc lệch tên/nội dung. Luôn lấy ảnh trong `model-response` **mới xuất hiện sau khi gửi**, rồi xem ảnh trước khi đặt tên vào plan. Nếu nghi lệch, dùng `scripts/match_gemini_prompts.py` (dấu vân tay ảnh) để xác minh.

---

## 5. Phân cảnh & sticker chỉ đúng chỗ

### 5.0 Viết `specs/storyboard.json` → `python src/episode/build_plans.py projects/<slug>` (chuẩn Tập 9)
Không viết tay plan. Storyboard = nhân vật cố định + danh sách beat; công cụ sinh plan (định dạng bên dưới) + prompt + catalog
và chặn lỗi ngay (cụm không có/trùng, sticker thiếu target hoặc đọc sau khi ảnh chuyển, ảnh dùng 2 lần). Mẫu: `examples/ep09_reference/storyboard.json`.
```json
{"characters": {"HERO": "chú chim cánh cụt Adélie ... đeo một chiếc nơ bướm đỏ nhỏ ở cổ", "HERO_S": "...", "NO_HERO": "KHÔNG có ...",
                "JUDGE": "ngài thẩm phán hải mã ..."},
 "side_characters": ["JUDGE"], "shorts_title_lines": ["ĐẨY BẠN XUỐNG BIỂN", "ĐỂ THỬ HẢI CẨU?!"], "skip_numbers": [29],
 "long": [{"scene": "scene03", "at": "Hải cẩu báo! Dài", "layout": "Một con hải cẩu báo ... thước dây vàng kéo từ mũi tới đuôi. {NO_HERO}.",
           "stickers": [{"at": "3,5m", "side": "L", "y": 330, "value": "3,5 M", "label": "chiều dài hải cẩu báo", "target": [0.5, 0.62]}],
           "impacts": []},
          {"scene": "scene02", "at": "Mà bồi thẩm đoàn biết", "layout": "...", "id": "L85"}],
 "shorts": [{"at": 0, "layout": "..."}, {"at": "Nhưng khoan, nhiều nhà", "layout": "...", "id": "S13"}]}
```
- `"id"`: chỉ khi chèn beat SAU khi đã tạo ảnh (số mới lớn hơn số cuối) — các ảnh cũ giữ nguyên tên.
- `skip_numbers`: số ảnh của beat đã bị gộp/bỏ (ảnh vẫn nằm đó nhưng không dùng) — các beat sau không bị dời số.
- Phụ kiện nhận dạng cố định cho nhân vật chính (nơ đỏ Tập 9) giữ nhân vật đồng nhất qua 100 ảnh và tách khỏi đồng loại "không đeo nơ".

### 5.1 Beat video dài (`specs/longform_plan.json` — do build_plans sinh)
```json
"scene05": {"chapter_no": 5, "title": "VỤ ÁN THỦY CUNG BỂ NÁT & ĐÔI MẮT THẦN 16 MÀU",
  "hook": "ĐẤM NỨT KÍNH THỦY CUNG VÀ NHÌN THẤY TẾ BÀO UNG THƯ", "card": true,
  "beats": [
    {"at": "Và gã giang hồ", "image": "assets/long/L65.png",
     "stickers": [{"at": "20 năm", "side": "R", "y": 400, "value": "20 NĂM", "label": "chung một hang", "target": [0.5, 0.55]}],
     "impacts": []}
]}
```
- `at` = 3–5 chữ **chép nguyên văn từ `long_words_fixed.json`** (đã là chữ hiện số: "20 năm", không phải "hai mươi năm"). Beat đầu chương `0`.
- Hình hiện sớm 0,3s trước cụm từ. Giữ 3–15s.
- Sticker: tối đa 2/hình; `value` ≤ 8–10 ký tự IN HOA; `label` ≤ 22 ký tự; `side` L/R; `y` 300–560; `at` = lúc con số được đọc.
- **`target` = [x, y] tỉ lệ 0..1 trên ảnh gốc** của đúng chi tiết đang nói. Cách đo: mở ảnh, ước lượng (x = vị trí ngang / chiều rộng, y = vị trí dọc / chiều cao). Ví dụ L64 (hai tôm nhắn tin bên trái-giữa) → `[0.33, 0.45]`; L65 (cặp vợ chồng ở giữa) → `[0.5, 0.55]`.
- `impacts`: cụm từ có tiếng va chạm (đấm, nổ, vỡ) → SFX.

### 5.2 Beat Shorts (`specs/shorts_plan.json`)
10–12 beat, mỗi câu 1 hình 3–6s, `title_lines` 2 dòng IN HOA ≤ 22 ký tự, sticker y: L 540–1060 / R 520–780, beat cuối = cảnh con vật đúng câu chốt (không mascot/CTA, không mũi tên chỉ link).
**Shorts tập lẻ kể trọn vẹn (TASTE-66; video tổng hợp/mega giữ Shorts phễu cũ):** hook → giới thiệu con vật → 2-3 sự thật có số → vì sao → câu chốt trả lời hook. Không kêu xem video dài, không bỏ lửng, không câu cắt lửng nối vòng.

### 5.3 Kiểm tra trước render
```bash
python src/episode/pipeline.py spec projects/<slug>      # phải "spec OK" (không thiếu ảnh, không phrase not found, hold ≤ 15s)
python scripts/audit_beats.py projects/<slug>            # in từng beat + lời đang nói + sticker; cuối: Image reuse: {}
python src/episode/target_sheet.py projects/<slug>       # vòng đỏ = chỗ mũi tên chỉ, trên ảnh gốc -> renders/snapshots/targets_*.jpg
python src/episode/pipeline.py render projects/<slug> --preview   # ~1 phút: sheet từng chương + contact sheet Shorts
```
Đọc **từng dòng** audit: lời đang nói có đúng là thứ vẽ trong ảnh không? Sticker xuất hiện đúng lúc đọc số?

---

## 6. Render & kiểm thử (bắt buộc đủ 6 bước)
```bash
python src/episode/pipeline.py render projects/<slug> --force           # dài ~25–30 phút + Shorts ~5 phút, chạy nền
python scripts/beat_sheet.py projects/<slug>                            # renders/beat_audit/sceneXX.jpg: 1 khung/beat ngay lúc sticker hiện
python scripts/hum_probe.py projects/<slug>/audio/shorts.wav projects/<slug>/renders/<slug>_shorts.mp4   # sàn nhiễu lúc nghỉ < -40 dBFS
python src/episode/pipeline.py qa projects/<slug>                       # dài ≥ 8:30, -14±1,5 LUFS, TP ≤ -1; Shorts 40–59,5s
python src/episode/pipeline.py seo projects/<slug>
python src/episode/episode_doc.py projects/<slug>                       # EPISODE_SPEC.md
```
Xem bằng mắt các `beat_audit/*.jpg`: mũi tên chỉ đúng chi tiết? sticker không che mặt con vật? phụ đề không có `[tag]`, số hiện đúng dạng số? Ảnh nào sai → sửa plan/ảnh → `spec` → `render --force` lại.

---

## 7. Bảng tra lỗi nhanh (đã gặp thật)
| Triệu chứng | Nguyên nhân | Cách sửa |
|---|---|---|
| Hình không khớp lời / hình lặp | 1 hình ôm nhiều câu; ảnh Gemini lấy nhầm response | 1 câu 1 hình; lấy ảnh từ response mới; `audit_beats.py` |
| Phụ đề có `[laughter]` | tag không bị lọc | `script_tokens()` đã lọc `\[[a-zA-Z0-9_\-]+\]`; chạy lại `align` |
| Phụ đề hiện chữ thay số | thiếu `display_fix` | thêm cụm vào `display_fix` → `align` → sửa `at` trong plan cho khớp chữ mới |
| Popup không có mũi tên | sticker thiếu `target` | thêm `target: [x,y]` |
| Ù/rè suốt Shorts | lowpass 12k trên âm 24 kHz | `aresample=48000` đầu chuỗi (đã sửa) + bỏ track scribble loop |
| Render xong 30s, ảnh cũ | cache `long_v2/sceneXX.mkv` | `render --force` |
| `phrase not found` | `at` không đúng chữ trong `long_words_fixed.json` | chép đúng nguyên văn (đã qua display_fix) |
| Gemini báo giới hạn | hết lượt tài khoản | `/u/1/app` tài khoản 2 |
| Video < 8:30 | lời quá ngắn sau tempo 1.10 | `voice_budget.py` → thêm part → `tts` |
| Giọng chậm | tempo 1.0 | `tempo_long` 1.10 (mặc định kênh) |
| `check` báo đủ giờ nhưng tts hụt | ước lượng cũ 17 ký tự/s quá lạc quan với giọng đa mood | công thức mới 17,6 ký tự/s theo tempo từng mood + biên 15s; nhắm ≥ 10.000 ký tự |
| Chèn part → giọng ghép nhầm | cache `audio/vs/<scene>_p<i>.wav` theo vị trí | `voice_cache.py snapshot` trước, `remap` sau |
| `holds only 1.6s (<2s)` | 2 beat quá sát nhau (câu dồn dập) | gộp beat, chuyển sticker sang beat trước, số ảnh vào `skip_numbers` |
| Shorts `holds > 7s` | 1 ảnh ôm 2 câu | tách câu, thêm beat `"id": "S13"` + ảnh |
| `phrase not found` ở `display_fix` | chữ hoa đầu câu ("Âm bốn mươi độ C") khác key thường | thêm key viết hoa |
| beat nhảy ngược / `first occurs before` | cụm `at` lặp trong chương | chọn cụm duy nhất (build_plans báo) |
| `gemini_gen` timeout 1 ảnh | Gemini trả lời bằng chữ / chậm | `--only Lxx --per-chat 1`; viết lại layout |
| `gemini_gen` không mở được Chrome | profile đang mở ở cửa sổ khác | đóng Chrome dùng profile đó |
| Playwright MCP không có tool | Cursor chưa bật server | không cần — dùng `gemini_gen.cjs`; muốn MCP thì bật trong Settings → MCP |

---

## 8. Checklist bàn giao (đánh dấu hết mới được báo "xong")
- [ ] Kịch bản: biệt danh ≥ 4 lần, ≥ 1 chỗ cười/20–30s, mọi số có `display_fix`, mỗi câu vẽ được
- [ ] `tts` in LONG-FORM ≥ 8:30 ở tempo 1.10; `align` match ≥ 0,9
- [ ] `check` sạch: không `!! script:`/`!! voice-diversity`, ước lượng ≥ 8:45; `sources` đủ
- [ ] storyboard → `build_plans` OK; `gemini_gen` missing = []; đã xem sheet_long/sheet_shorts/banners/thumbnail
- [ ] Mỗi câu 1 ảnh 16:9 riêng; đã xem từng ảnh; `image_catalog.md` + `image_prompts.json` đầy đủ
- [ ] `target_sheet` vòng đỏ đúng chi tiết; `render --preview` đã xem
- [ ] `spec OK`; `audit_beats.py` → `Image reuse: {}`, hold 3–15s, lời khớp hình
- [ ] `render --force`; `beat_sheet.py` đã xem hết; mũi tên chỉ đúng
- [ ] `hum_probe` sàn nhiễu < -40 dBFS; `qa` PASS
- [ ] `seo` + `EPISODE_SPEC.md` sinh xong; ghi `production_log` (`memory_harvester.py --log-video`)
- [ ] **Đa phong cách bắt buộc từ Tập 32 (`TASTE-73`, `TASTE-74`, `TASTE-75`)**:
  - `episode.json > art.visual_style` + `style_label`: Mỗi tập có 1 phong cách vẽ tranh minh họa riêng biệt theo thế giới quan của loài vật (`config/series_roadmap.json`).
  - `scenes[].banner_bar_style` (`C01..C06 -> assets/banners/chapter_NN.png`): Mỗi chương có 1 kiểu thanh tiêu đề trên màn hình biến hóa riêng, bỏ hẳn thanh chữ nhật navy viền vàng cố định.
  - `scenes[].card_style` + `card_sub` (`K01..K06 -> assets/banners/card_NN.png`): Bảng chuyển chương lớn giữa màn hình (1.6s đầu mỗi chương) bắt buộc sinh bằng prompt ảnh AI qua `extra_prompts.py` -> `gemini_gen.cjs extra` -> `prep_banners.py`, tuyệt đối không vẽ khung PIL đơn điệu.
  - `art.shorts_banner_style` (`B00 -> assets/banners/shorts_title.png`): Banner Shorts đồng bộ 100% chủ đề thị giác của tập.
  - `src/render/theme_effects.py`: Tự động đổi giao diện Thẻ Sticker số liệu HUD, Mũi tên chỉ điểm và Vòng khóa mục tiêu theo format/theme của từng tập.
- [ ] Báo cáo chủ kênh và **dừng** — chờ lệnh "đăng" + giờ

