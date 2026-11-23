# HỆ THỐNG GIỌNG ĐỌC ĐA PHONG CÁCH — "Vẽ Chuyện Hoang Dã"
> Mục tiêu: **mỗi tập một giọng dẫn khác, trong tập giọng đổi theo tình huống**, có vai phụ lên tiếng — hết cảnh "một màu".
> Vẫn 100% VoiceStudio/OmniVoice cục bộ (không ElevenLabs). Cấu hình: `config/voice_personas.json`. Code: `src/episode/pipeline.py`
> (`part_voice`, `voice_diversity`), `src/audio/omnivoice_tts.py` (mỗi job có `ref`/`instruct` riêng). Mẫu nghe: `projects/_voice_test/MAU_GIONG_DA_PHONG_CACH.mp3`.

---

## 1. Ba lớp giọng

| Lớp | Đổi theo | Cách làm kỹ thuật | Ví dụ |
|---|---|---|---|
| **Persona** (vai người dẫn) | **Format của tập** (F1-F7) | Cách viết (xưng hô, từ vựng, câu mở/đóng) + phân bổ mood mặc định | F1 bác sĩ bất lực, F3 công tố viên → luật sư, F7 bình luận viên |
| **Mood** (cảm xúc đoạn) | **Tình huống trong cảnh** | Clip tham chiếu khác (`ref`) + `speed` + `tempo` + bộ tag riêng, gán theo part/scene | Đuổi bắt → `don_dap`; bí ẩn → `tram_bi_an`; cứu hộ → `am_ap` |
| **Cast** (vai phụ, cameo) | **Nhân vật lên tiếng** trong câu chuyện | Giọng khác hẳn (đàn ông già trầm, bé gái, phụ nữ trung niên…) — thiết kế bằng OmniVoice voice-design rồi **đóng băng** thành clip `assets/voice_refs/cast_<id>.wav` | Thẩm phán "Tòa tuyên…", Koala con "Mẹ ơi con đói!", trợ lý lab |

Giọng chính (Adam, clone `adam_funny_ep1.wav`) vẫn dẫn **≥ 92%** lời — đó là "thương hiệu" kênh; persona/mood làm nó đổi sắc thái, cast chỉ là điểm nhấn.

## 2. Sáu mood (gán bằng `"mood"`)

| Mood | Khi nào dùng | Clip ref | speed / tempo | Cách VIẾT để giọng ra đúng | Tag ưu tiên |
|---|---|---|---|---|---|
| `hao_hung` *(mặc định)* | Kể chuyện vui, so sánh đời thường | `adam_funny_ep1` | 1.05 / 1.12 | Câu vừa, nhiều `!`, punchline ≤ 8 từ | `[laughter]` `[surprise-oh]` |
| `don_dap` | Săn mồi, đánh nhau, đếm ngược, số liệu dồn | `adam_funny_ep1` | 1.12 / 1.18 | Câu ≤ 10 từ, liệt kê, động từ mạnh, `!` cuối mỗi câu | `[surprise-wa]` |
| `tram_bi_an` | Mở màn bí ẩn, hiện trường, đêm tối, tiết lộ lớn | `adam_v3_ep6` (điềm) | 1.00 / 1.08 | Câu ngắn, `...` trước tiết lộ, câu hỏi treo; **không** `[laughter]`, **không thì thầm** (TASTE-32) | `[question-oh]` |
| `nghiem_trang_gia` | Bệnh án, bản tin, đọc cáo trạng — rồi bẻ lái | `adam_v3_ep6` | 1.02 / 1.11 | Văn phong hành chính ("Chẩn đoán:", "Bằng chứng số hai:") + 1 câu tầm thường cực ngắn làm punchline | `[dissatisfaction-hnn]` `[laughter]` |
| `bi_hai` | Điểm yếu, thất bại, thương hại con vật | `adam_v3_ep6` | 1.00 / 1.08 | `[sigh]` đầu đoạn, kể cái khổ, chốt câu tự giễu | `[sigh]` `[laughter]` |
| `am_ap` | Cứu hộ, mẫu tử, bảo tồn, teaser cuối | `adam_v3_ep6` | 1.00 / 1.08 | Câu mềm, xưng "chúng ta", không cảm thán dồn | — |

**Tempo trung bình cả tập (theo ký tự) phải ≥ 1.10** (TASTE-61). Mood chậm phải được bù bằng `don_dap`/`hao_hung`; `pipeline.py check` và `tts` tự tính và cảnh báo.

## 3. Tám persona theo format

| Persona | Format | Xưng hô | Câu mở mẫu | Từ vựng riêng | Phân bổ mood gợi ý | Cameo hợp |
|---|---|---|---|---|---|---|
| `bac_si` | F1 | "tôi" – "bệnh nhân" – "các đồng nghiệp" | *"Bệnh nhân số mười, mời vào!"* | chẩn đoán, nội soi, kê đơn, tiên lượng | nghiêm trang giả 35 · hào hứng 35 · bi hài 20 · ấm áp 10 | `chu_ngo_ngac`, `co_tro_ly`, `be_con` |
| `ky_su_vu_khi` | F2 | "tôi" – "đội kỹ thuật" | *"Hồ sơ mật cấp độ đỏ. Mở khóa!"* | thông số, nạp đạn, khai hỏa, bản vẽ | dồn dập 35 · hào hứng 40 · trầm bí ẩn 25 | `phat_thanh_vien`, `ga_khong_lo` |
| `phien_toa` | F3 | công tố viên → (chương cuối) luật sư bào chữa; khán giả = "bồi thẩm đoàn" | *"Bị cáo, mời đứng lên!"* | bị cáo, bằng chứng, nhân chứng, phản đối! | nghiêm trang giả 30 · dồn dập 25 · hào hứng 25 · ấm áp 20 | `tham_phan`, `ong_gia_ke`, `cong_to_vien` |
| `phong_vien_24h` | F4 | "chúng tôi đang có mặt tại…" – "quý vị" | *"Bây giờ là sáu giờ sáng. Cuộc đua sinh tồn bắt đầu!"* | bây giờ là, còn đúng, đếm ngược | **theo giờ**: sáng hào hứng → trưa dồn dập → tối trầm bí ẩn → đêm ấm áp | `phat_thanh_vien`, `ong_gia_ke` |
| `nha_khoa_hoc` | F5 | "tôi" – "trợ lý thí nghiệm" | *"Ghi chép thí nghiệm, ngày thứ nhất…"* | cấp độ, mẫu vật, tăng liều, "kết quả: vẫn sống" | hào hứng 40 · dồn dập 30 · bí ẩn 15 · bi hài 15; **tempo tăng dần theo level** 1.08→1.18 | `co_tro_ly`, `phat_thanh_vien` |
| `ong_trum` | F6 | kể ngôi 3, "gia đình", "anh em" | *"Gia đình này có một quy tắc…"* | gia tộc, luật ngầm, đàn em, bà trùm | trầm bí ẩn 40 · nghiêm trang giả 30 · hào hứng 30 | `ba_trum`, `ga_khong_lo` |
| `binh_luan_vien` | F7 | "tôi" – "khán giả" – "tuyển thủ" | *"Kính thưa quý vị, tuyển thủ đã bước vào sàn đấu!"* | combo, chí mạng, K.O, buff/nerf | dồn dập 45 · hào hứng 40 · bi hài 15 | `ga_khong_lo`, `phat_thanh_vien` |
| `giai_dau` | đặc biệt | MC – "toàn thể khán đài" | *"Mười nhà vô địch. Một chiếc đai. Không có hòa!"* | vòng loại, nhánh đấu, đi tiếp | dồn dập 50 · hào hứng 35 · bí ẩn 15 | `tham_phan` |

Persona = **cách viết lời** (xưng hô, từ vựng, câu mở/đóng) + **mood mặc định**. Chi tiết đầy đủ trong `config/voice_personas.json > personas`.

## 4. Chín giọng cameo (gán bằng `"cast"`)

| id | Vai | Thiết kế gốc (OmniVoice instruct) | Clip đóng băng |
|---|---|---|---|
| `tham_phan` | Thẩm phán | male, elderly, very low pitch | `assets/voice_refs/cast_tham_phan.wav` |
| `cong_to_vien` | Công tố viên | female, middle-aged, moderate pitch | `cast_cong_to_vien.wav` |
| `ba_trum` | Bà trùm / nữ hoàng | female, middle-aged, low pitch | `cast_ba_trum.wav` |
| `be_con` | Con non / nhân vật bé xíu | female, child, high pitch | `cast_be_con.wav` |
| `ga_khong_lo` | Kẻ săn mồi to xác | male, middle-aged, very low pitch | `cast_ga_khong_lo.wav` |
| `chu_ngo_ngac` | Con vật ngơ ngác | male, young adult, high pitch | `cast_chu_ngo_ngac.wav` |
| `co_tro_ly` | Trợ lý phòng lab | female, young adult, moderate pitch | `cast_co_tro_ly.wav` |
| `ong_gia_ke` | Cụ già / nhân chứng | male, elderly, low pitch | `cast_ong_gia_ke.wav` |
| `phat_thanh_vien` | Bản tin khẩn | female, young adult, moderate pitch | `cast_phat_thanh_vien.wav` |

- **Vì sao phải đóng băng:** voice-design của OmniVoice bốc **giọng ngẫu nhiên mỗi lần gọi** → cùng một "thẩm phán" mà mỗi part một giọng.
  `python scripts/make_cast_refs.py` thiết kế mỗi giọng 1 lần, lưu clip + `.txt`, rồi trỏ `ref` vào clip → các tập sau clone đúng giọng đó.
  Nghe lại từng clip; không ưng → `python scripts/make_cast_refs.py --redo --only tham_phan`.
- **Luật cameo:** 2-6 part/tập, tổng ≤ 8% ký tự lời; mỗi cameo **1-2 câu ngắn** (≤ 120 ký tự), đứng thành part riêng, ngay sau là giọng chính bình luận lại (phản ứng = chỗ cười).
  Lời cameo là thoại tưởng tượng (kỹ thuật hài #5) — vẫn phải đúng khoa học, không thô tục.
- Shorts: tối đa 1 cameo (part riêng không hỗ trợ trong Shorts 1 đoạn → để giọng chính "nhại" lại bằng ngoặc kép).

## 5. Ma trận tình huống → mood (dùng khi gán từng part)

| Tình huống trong cảnh | Mood | Ghi chú viết |
|---|---|---|
| Câu hook mở tập / hiện trường vụ án / tiết lộ "sự thật đáng sợ" | `tram_bi_an` | 2-3 câu rồi chuyển `hao_hung` để không nặng nề |
| Số liệu kỷ lục, so sánh đời thường, chuyện vui | `hao_hung` | mặc định |
| Đuổi bắt, đánh nhau, đếm ngược, liệt kê 3+ chiến tích | `don_dap` | câu ≤ 10 từ |
| Đọc hồ sơ / cáo trạng / bệnh án / thông số | `nghiem_trang_gia` | luôn kết bằng punchline tầm thường |
| Điểm yếu, chết lãng xẹt, tiến hóa "chơi khăm" | `bi_hai` | `[sigh]` 1 lần |
| Mẹ con, cứu hộ, bảo tồn, bài học, teaser tập sau | `am_ap` | không cảm thán dồn |
| Con vật / nhân vật phụ "nói" | cameo `cast` | part riêng, ≤ 2 câu |

**Đường cong cảm xúc mỗi tập (bắt buộc ≥ 3 mood, không mood nào > 50% lời):**
`mở bí ẩn/sốc → hào hứng → dồn dập (đỉnh 1) → nghiêm trang giả/bi hài (bẻ lái) → dồn dập (đỉnh 2) → ấm áp (teaser)`.

## 6. Cú pháp trong `episode.json`

```json
{
 "format": "F3", "persona": "phien_toa",
 "longform": {"scenes": [
  {"id": "scene01", "badge": "VỤ ÁN NAM CỰC", "mood": "tram_bi_an", "parts": [
     "Nam Cực, âm bốn mươi độ. Một viên sỏi... vừa biến mất.",
     {"text": "Bị cáo, mời đứng lên!", "cast": "tham_phan"},
     {"text": "[surprise-oh] Và bị cáo là... một chú chim cao chưa tới bảy mươi xăng-ti-mét, đang đi lạch bạch như trẻ mẫu giáo! [laughter]", "mood": "hao_hung"}
  ]},
  {"id": "scene02", "badge": "BẰNG CHỨNG #1", "parts": ["... (persona default mood) ..."]}
 ]},
 "shorts": {"mood": "hao_hung", "text": "..."}
}
```
Thứ tự ưu tiên: **part** (`mood`/`cast`/`tempo`/`speed`) > **scene** (`mood`) > `episode.default_mood` > `persona.default_mood` > kênh.
Part dạng chuỗi thường vẫn chạy như cũ (tương thích Tập 1-8).

## 7. Quy trình (chen vào episode-production)
1. **Bước 0** — đọc `config/series_roadmap.json`: lấy `format` + `persona` của tập; ghi vào `episode.json`.
2. **Bước 1 (kịch bản)** — viết theo persona (xưng hô, từ vựng, câu mở/đóng), gán `mood` cho từng scene/part theo ma trận mục 5, chèn 2-6 cameo.
3. `python src/episode/pipeline.py check projects/<slug>` → dòng `voice: format … | moods: … | cameo … | avg tempo …`; sửa đến khi **không còn dòng `!! voice-diversity`**.
4. **Bước 2 (tts)** — chạy như cũ; pipeline tự chọn ref/tempo theo mood/cast cho từng part. Lần đầu trên máy mới: `python scripts/make_cast_refs.py`.
5. **Kiểm tra giọng**: `align` match ≥ 0.85 mọi chương (cameo trẻ con/già có thể thấp hơn — nghe lại part đó); nghe 1 part mỗi mood + mọi cameo.
6. `EPISODE_SPEC.md` ghi lại format/persona/mood từng part để tập sau tránh trùng.

## 8. Lưu ý kỹ thuật (đã thử thật 2026-11-08)
- Mẫu thử: thẩm phán F0 ≈ 133 Hz, bé con ≈ 363 Hz, dồn dập ≈ 260 Hz, trầm bí ẩn/bác sĩ ≈ 142-145 Hz → khác nhau rõ rệt; Whisper đọc lại đúng 95%+ chữ.
- `instruct` chỉ nhận đúng các từ khóa của OmniVoice: giới tính (`male/female`), tuổi (`child/teenager/young adult/middle-aged/elderly`),
  cao độ (`very low … very high pitch`), `whisper` (**cấm** — TASTE-32), accent tiếng Anh (không dùng cho tiếng Việt). Sai chính tả → lỗi.
- Ghép `instruct` + clone (`ref`) được, nhưng clone thắng về âm sắc; muốn giọng khác hẳn → `ref: null` (thiết kế) rồi đóng băng.
- Đổi mood của 1 part → **xóa** `audio/vs/<scene>_p<i>.wav` rồi `tts` lại (cache theo tên file, không theo mood).
- Tag cảm xúc vẫn chỉ 8 tag cũ (humor-voice A5).
