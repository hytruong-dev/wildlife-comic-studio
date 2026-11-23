---
name: humor-voice
description: Viết kịch bản HÀI HƯỚC + THÚ VỊ cho kênh "Vẽ Chuyện Hoang Dã" và đọc nó bằng VoiceStudio (OmniVoice, cục bộ, miễn phí) để giọng có cảm xúc như Tập 1-5. Dùng ở Bước 1 (kịch bản) và Bước 2 (giọng) của episode-production, hoặc khi chủ kênh nói "viết hài hơn", "giọng nhạt quá", "tạo voice", "đọc thử".
---

# Hài hước & giọng đọc — chuẩn kênh Vẽ Chuyện Hoang Dã

Kênh = **khoa học thật, kể bằng giọng "ông anh tếu"**. Người xem ở lại vì cười + "ồ, thật á?".
Tập 1-5 (Lửng Mật "gã Chí Phèo", Stoffel vượt ngục) được khen vì vui; Tập 6 bị chê "chưa có cảm xúc".
Skill này chặn lỗi đó cho mọi tập sau. Giọng: **chỉ VoiceStudio**, ElevenLabs đã bỏ hẳn.

---

## PHẦN A — VIẾT KỊCH BẢN HÀI

### A1. 8 kỹ thuật gây cười (mỗi chương dùng ≥ 3 kỹ thuật khác nhau)
| # | Kỹ thuật | Ví dụ đã duyệt / mẫu |
|---|---|---|
| 1 | **Nhân cách hóa thành "nhân vật"** — gán con vật 1 tính cách/biệt danh Việt, gọi lại suốt tập | Lửng Mật = "gã Chí Phèo số một hành tinh"; Gấu Nước = "kẻ bất tử lười biếng" |
| 2 | **So sánh đời thường phóng đại** — quy số liệu khoa học về đồ vật ai cũng biết | "da dày 6 mm, lỏng như áo khoác mượn của anh trai"; "mỏ chứa 13 lít — vừa một xô lau nhà" |
| 3 | **Cú bẻ lái bi hài** (setup nghiêm → punchline tầm thường) | "Sống sót qua 5 lần tận thế… mà thua một con ốc sên." |
| 4 | **Câu chốt ngắn sau câu dài** — punchline ≤ 8 từ, đứng riêng | "...nhai nốt nửa con rắn còn lại. Như ăn bim bim." |
| 5 | **Lời thoại tưởng tượng của con vật** (1 câu, trong ngoặc kép) | Sư tử nhìn Lửng Mật: "Thôi, hôm nay anh ăn chay." |
| 6 | **Hệ quy chiếu game/đời sống** — RPG stats, "buff", "nerf", "bug của tạo hóa", "lỗi game" | "Nhà phát triển game sẽ bị khiếu nại vì nhân vật quá mất cân bằng!" |
| 7 | **Hỏi tu từ rồi tự trả lời tỉnh bơ** | "Bạn nghĩ tường bê tông giam được nó? Ừ, nó cũng nghĩ thế. Trong đúng năm phút." |
| 8 | **Callback** — nhắc lại biệt danh/câu đùa đầu tập ở chương cuối & Shorts | Câu chốt Shorts trả lời luôn câu hook (khép trọn ý, không bỏ lửng) |

### A2. Nhịp độ hài (quy tắc đo được)
- **Mỗi 20-30 giây lời đọc (~350-500 ký tự) phải có ≥ 1 chỗ cười** (kỹ thuật 2-5). Chương 4 (điểm yếu) và 5 (chuyện có thật) dày nhất.
- Công thức đoạn: **Sự thật sốc (số liệu) → So sánh đời thường → Punchline ngắn.**
- Mỗi chương kết bằng 1 punchline hoặc 1 câu hỏi gây tò mò, không kết bằng câu giải thích khô.
- Biệt danh nhân vật xuất hiện ≥ 4 lần trong tập (chương 1, 3, 5, 6).

### A3. Giới hạn (không được vượt)
- Sự thật khoa học **luôn đúng**; đùa ở cách kể, không bịa số liệu. Nếu phóng đại thì nói rõ "kiểu như", "cứ như".
- Thân thiện gia đình/trẻ em (TASTE-41): không thô tục, không chửi, không đùa chết chóc ghê rợn, không chế giễu vùng miền/ngoại hình người.
- Không "hơ hơ", "haha" viết ra chữ; tiếng cười do tag `[laughter]` làm. Không meme hết hạn khó hiểu.
- Không lộ cấu trúc ("ở phần tiếp theo"), không lặp ý (TASTE-52).

### A4. Viết để GIỌNG đọc ra cảm xúc (VoiceStudio đọc theo dấu câu)
- `!` = năng lượng cao; `?` = lên giọng hỏi; `...` = ngừng chờ punchline (đặt ngay trước câu chốt).
- Câu ngắn = nhanh, dồn dập; câu dài = kể chuyện. Xen kẽ, đừng để 3 câu dài liên tiếp.
- Từ cảm thán Việt tự nhiên giúp giọng "diễn": *Ơ kìa!, Ủa?, Trời đất!, Thật luôn!, Khoan đã!, Đấy!, Cay không cơ chứ!*
- Số viết bằng chữ khi dễ đọc sai ("âm hai trăm bảy mươi hai độ"); tên nước ngoài phiên âm + `display_fix`.
- **Mọi số viết bằng chữ PHẢI có `display_fix`** để phụ đề hiện số (`"mười ngàn bốn trăm g": "10.400g"`, `"hai mươi năm": "20 năm"`) — chủ kênh bắt lỗi này ở Tập 7.
- Mỗi câu phải **vẽ được thành 1 hình** (ai, làm gì, đạo cụ nào) vì mỗi câu sẽ là 1 ảnh riêng.

### A4b. Mẫu câu hài đã duyệt (Tập 7 Tôm Tít — "Mike Tyson của đại dương")
- Hỏi tu từ dồn dập: *"Cua biển mai dày ư? Một đấm vỡ nát! Vỏ ốc xà cừ cứng như đá ư? Hai đấm thành bột vụn!"*
- Hệ quy chiếu đời sống: *"Một phe đấm bốc, một phe đấu kiếm, đúng là cả một gia tộc võ lâm dưới đáy biển!"*
- So sánh tài trợ thể thao: *"…được thay luôn một cặp búa mới tinh, cứ như võ sĩ được tài trợ đôi găng mới sau mỗi mùa giải vậy!"*
- Cài cắm tò mò (cầu nối chương): *"Nhưng cái giá của món quà đó thì... lát nữa bạn sẽ biết!"*
- Punchline đối xứng: *"Ra ngoài thì đấm nứt kính, về nhà thì ngoan như mèo!"*
- Bẻ lái bi hài: *"…võ sĩ bất khả chiến bại này lại biến thành một miếng thạch bơ mềm nhũn, sợ cả một con ốc sên bò ngang qua!"*

### A4b2. Mẫu đã duyệt Tập 9 (F3 Phiên tòa — "Quý ông Vest Đuôi Tôm", giọng đa phong cách)
- Mở bằng hiện trường bí ẩn (`tram_bi_an`) 3 câu → cameo thẩm phán *"Bị cáo, mời đứng lên!"* → giọng chính bẻ lái
  `[surprise-oh] Và bị cáo là... một chú chim cao chưa tới bảy mươi xăng-ti-mét... đang đi lạch bạch như trẻ mẫu giáo đi học muộn! [laughter]`
- Nghiêm trang giả rồi tầm thường: *"Bằng chứng số một: trộm cắp tài sản có giá trị lớn. Tài sản bị trộm là... một viên sỏi."*
- Phóng đại số liệu chậm: *"Một cuộc rượt đuổi tốc độ cao... hai cây số một giờ."*
- Cameo bị cáo tự bào chữa: *"Thưa tòa, cháu không trộm! Cháu chỉ... mượn vĩnh viễn thôi ạ!"* → *"Bồi thẩm đoàn đã nghe rồi đấy. Mượn vĩnh viễn!"*
- Nhân chứng có thật (bác sĩ Levick 1911) đọc bằng giọng `ong_gia_ke` = vừa thật vừa buồn cười.
- Khoa học "khó nói" (áp suất phân, giải Ig Nobel) → giọng nghiêm túc + số liệu thật = hài mà vẫn sạch cho trẻ em.
- Chương cuối đổi vai luật sư bào chữa (`am_ap`) lật ngược cả 4 bằng chứng bằng khoa học → phán quyết cameo → callback viên sỏi.
- Kết: câu hỏi cho bình luận ("bạn tuyên có tội hay vô tội?") + teaser tập sau theo format của nó (phòng khám Koala). Không "bấm đăng ký".

### A4c. Độ dài khi giọng nhanh (luật 2026-11-08, hiệu chỉnh Tập 9)
Đo thật Tập 9 (đa mood, có cameo): **17,6 ký tự/s ở tempo 1.0**, tempo trung bình 1.12 → ~19,7 ký tự/s → **nhắm ≥ 10.000 ký tự lời**
(không tính tag). Tập 9 viết 9.489 ký tự → chỉ 8:19, phải thêm 545 ký tự mới đạt 8:48. `pipeline.py check` đã dùng công thức mới
và đòi ước lượng ≥ 8:45. Thêm part giữa chương: `src/episode/voice_cache.py snapshot` TRƯỚC khi sửa, `remap` SAU khi sửa.
(Cũ: giọng chạy **tempo 1.10** ≈ 18,7 ký tự/s → video dài ≥ 8:30 cần ≥ 9.200 ký tự — đã lạc quan quá.)
Thiếu → viết thêm **part mới** (sự thật vui + punchline, mỗi part 250-450 ký tự) ở cuối chương 2-5, không kéo dài câu cũ,
không hạ tempo. `python scripts/voice_budget.py projects/<slug> 515` cho biết số ký tự còn thiếu.

### A5. Tag cảm xúc VoiceStudio (CHỈ những tag này — tag khác bị tự xóa)
| Tag | Dùng khi | Tần suất |
|---|---|---|
| `[laughter]` | ngay **sau** punchline (cười theo khán giả) | 1-2 lần/chương, không đặt 2 tag liền nhau |
| `[surprise-oh]` / `[surprise-ah]` / `[surprise-wa]` | **đầu** câu tiết lộ số liệu sốc | 1-2 lần/chương |
| `[question-ah]` / `[question-oh]` | cuối câu hỏi tu từ trêu người xem | ≤ 1/chương |
| `[sigh]` | trước câu "bi hài" (thương hại con vật) | ≤ 1/chương |
| `[dissatisfaction-hnn]` | giả vờ chê (kẻ săn mồi thất bại) | hiếm |
Tag ElevenLabs cũ (`[excited]`, `[laughs]`, `[curious]`…) **không còn tác dụng** — đừng viết.
Ví dụ: `[surprise-oh] Ơ kìa! Gấu Nước chịu được âm hai trăm bảy mươi độ... Vậy mà! Một con ốc sên bò ngang qua là xong phim! [laughter] Cay không cơ chứ!`

### A6. Checklist trước khi chạy `tts` (tự chấm, sửa đến khi đạt)
- [ ] Có biệt danh nhân vật, xuất hiện ≥ 4 lần
- [ ] Mỗi part (≤ 1.300 ký tự) có ≥ 2 chỗ cười và ≥ 1 tag
- [ ] Mỗi chương kết bằng punchline/câu hỏi
- [ ] Shorts tập lẻ kể trọn vẹn (TASTE-66; mega giữ kiểu phễu cũ): ≥ 3 punchline, tag `[surprise-oh]` ở câu 1, `[laughter]` sau cú bẻ lái,
      có giới thiệu con vật + 2-3 sự thật có số + giải thích vì sao + câu chốt trả lời hook; KHÔNG kêu xem video dài, KHÔNG bỏ lửng
- [ ] Không câu nào sai sự thật; không từ thô tục
- [ ] Viết đúng persona của format (xưng hô, từ vựng); mỗi scene/part có `mood` hợp tình huống; 2-6 part `cast` (B4b)
- [ ] `episode.json` có `nickname` (biệt danh, check đếm ≥ 4 lần) và `sources` (nguồn cho từng số liệu)
- [ ] Huyền thoại phổ biến về con vật đã kiểm chứng — sai thì kể như huyền thoại rồi bẻ lái bằng khoa học (Tập 9)
- [ ] Cụm mở đầu câu không lặp nguyên văn trong cùng chương (để làm mốc beat duy nhất)
- `python src/episode/pipeline.py check projects/<slug>` in danh sách tag đã dùng — "NONE" là chưa đạt — và **lint kịch bản**
  (`!! script:` = số đọc bằng chữ thiếu `display_fix` (kể cả biến thể viết hoa đầu câu), chữ số trong lời, tag lạ, part > 1300,
  biệt danh < 4, thiếu sources). Sửa đến khi in `script lint OK`.

---

## PHẦN B — GIỌNG ĐỌC BẰNG VOICESTUDIO

### B1. Cấu hình (đã khóa trong `config/channel.json > voice`)
- Engine: VoiceStudio / OmniVoice (k2-fsa), chạy bằng Python trong `.venv` của VoiceStudio (`voicestudio_python`).
- Giọng: **nhân bản từ clip tham chiếu** `assets/voice_refs/adam_funny_ep1.wav` (+ `.txt` là lời của clip) — 9 s giọng Adam
  tươi vui Tập 1 ("Lửng Mật bỗng mở to mắt… tỉnh queo như vừa ngủ trưa dậy"). **Cảm xúc của clip tham chiếu lan sang toàn bộ bài đọc**,
  nên clip vui → giọng vui. Đã được chủ kênh duyệt (2026-11-07, file mẫu `projects/_voice_test/VOICESTUDIO_hai_huoc.mp3`).
- `speed` 1.05, `steps` 32, **`tempo_long` 1.10, `tempo_shorts_min` 1.10** (2026-11-08: chủ kênh thấy 1.0 "hơi chậm"; 1.10 nhanh-vui mà vẫn rõ chữ, align match 0.92-0.95).
- Chuỗi filter Shorts: `aresample=48000` ĐẦU TIÊN rồi mới atempo/highpass/lowpass (giọng gốc 24 kHz — LESSON-73, lỗi ù tai Tập 7).
- Model đã tải sẵn ở `%LOCALAPPDATA%/OmniVoice/hf_cache` — chạy offline.

### B2. Lệnh
```bash
python src/episode/pipeline.py check projects/<slug>   # kiểm tra VoiceStudio + đếm tag
python src/episode/pipeline.py tts   projects/<slug>   # tạo audio/vs/*.wav -> audio/sceneXX.wav, audio/shorts.wav
```
- CPU (không GPU): **~7 giây tính cho 1 giây audio** → 1 tập 9 phút ≈ 60-70 phút. Luôn chạy nền (`block_until_ms: 0`) và theo dõi bằng AwaitShell.
- Có cache: part nào đã có `audio/vs/<id>.wav` thì bỏ qua. Muốn đọc lại 1 part → xóa đúng file đó rồi chạy lại `tts`.
- Đọc thử nhanh 1 câu (≈ 2 phút):
  ```powershell
  & "$env:LOCALAPPDATA\com.debpalash.omnivoice-studio\project\.venv\Scripts\python.exe" src/audio/omnivoice_tts.py `
     --ref assets/voice_refs/adam_funny_ep1.wav --text "Câu thử..." --out projects/_voice_test/thu.wav --speed 1.05
  ```

### B3. Kiểm tra chất lượng giọng (bắt buộc sau `tts`)
1. `pipeline.py align` — match ratio mỗi chương ≥ 0.8 (thấp hơn = đọc sai/nuốt chữ → xóa part đó, tạo lại; đổi cách viết câu nếu lặp lại).
   Lưu ý: Whisper hay nghe "ốc sên" thành "Âu Xen", "lửng" thành "lừng" — lỗi của Whisper, không phải giọng.
2. Nghe 2-3 đoạn có `[laughter]`: tiếng cười tự nhiên? Nếu méo/kỳ → bỏ tag ở câu đó, tạo lại part.
3. OmniVoice thỉnh thoảng đọc 1 lần ra kết quả kém (sai thanh điệu, lặp từ) → chỉ cần tạo lại part đó (kết quả ngẫu nhiên mỗi lần).

### B4. Đổi/ thêm giọng tham chiếu
- Clip 6-12 s, 1 người nói, không nhạc nền, **đúng cảm xúc muốn có** (vui, năng lượng), kèm file `.txt` chép **chính xác** lời trong clip.
- Lưu vào `assets/voice_refs/`, sửa `config/channel.json > voice.reference`. Thử bằng lệnh đọc thử ở B2 trước khi chạy cả tập.
- Clip có sẵn: `adam_funny_ep1.wav` (chuẩn, vui), `adam_v3_ep6.wav` (điềm hơn, dùng cho đoạn trầm/bài học nếu muốn).
- Không dùng clip thì thầm (TASTE-32), không clip có tiếng cười ở giữa (giọng sẽ cười lung tung).

### B4b. Giọng ĐA PHONG CÁCH (bắt buộc từ Tập 9 — chống "một màu")
Toàn bộ quy chuẩn: `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`; cấu hình `config/voice_personas.json`.
- **Persona = theo format tập** (F1 bác sĩ bất lực, F2 kỹ sư vũ khí, F3 công tố viên→luật sư, F4 phóng viên 24h,
  F5 nhà khoa học điên, F6 kể chuyện ông trùm, F7 bình luận viên) → đổi **cách viết**: xưng hô, từ vựng, câu mở/đóng.
  Kỹ thuật hài #6 (RPG/buff/nerf) chỉ dày đặc ở F7; format khác dùng hệ quy chiếu của persona (bệnh án, tòa án, bản tin…).
- **Mood = theo tình huống từng đoạn**: `hao_hung` · `don_dap` · `tram_bi_an` · `nghiem_trang_gia` · `bi_hai` · `am_ap`
  (gán `"mood"` cho scene hoặc part). Mỗi mood tự đổi clip tham chiếu + speed + tempo và có cách viết riêng (câu ngắn cho
  dồn dập, `...` cho bí ẩn, văn phong hành chính rồi bẻ lái cho nghiêm trang giả).
- **Cast = vai phụ lên tiếng** (`{"text": "Bị cáo, mời đứng lên!", "cast": "tham_phan"}`): 9 giọng — `tham_phan`,
  `cong_to_vien`, `ba_trum`, `be_con`, `ga_khong_lo`, `chu_ngo_ngac`, `co_tro_ly`, `ong_gia_ke`, `phat_thanh_vien`.
  2-6 part/tập, ≤ 2 câu mỗi part, ngay sau là giọng chính phản ứng (= chỗ cười).
- Luật đo được (`pipeline.py check`): ≥ 3 mood, không mood > 50% lời, cameo ≤ 8%, tempo trung bình ≥ 1.10.
- Đổi mood/cast của 1 part → xóa `audio/vs/<scene>_p<i>.wav` rồi `tts` lại.

### B5. Nếu VoiceStudio hỏng / máy mới
- Cài VoiceStudio (https://voicestudio.sh → Windows), mở 1 lần, tải model **OmniVoice** trong tab Models.
- Sửa `voice.voicestudio_python` nếu đường dẫn khác. Chạy `pipeline.py check`.
- **Không** quay lại ElevenLabs, gTTS, edge-tts. Nếu không tạo được giọng → dừng và báo chủ kênh.
