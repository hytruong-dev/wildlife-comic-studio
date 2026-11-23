# 7 FORMAT KỂ CHUYỆN LUÂN PHIÊN — "Vẽ Chuyện Hoang Dã"
> Bản chuẩn hóa (dùng cho pipeline) của tài liệu chủ kênh `docs/strategy/CAM_NANG_7_FORMAT_KE_CHUYEN_GOC.md`.
> Áp dụng **từ Tập 9**. Đọc kèm: `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md` (giọng đọc theo format & tình huống),
> lộ trình máy đọc được: `config/series_roadmap.json`. Có hiệu lực cao hơn bảng "6 chương" cũ trong `episode-production`.

---

## 1. Vì sao bỏ khung "6 chương + thẻ RPG" cố định
- **Pattern fatigue:** đến tập 3-4 khán giả đoán trước được: Chương 1 cú lừa → Chương 2 RPG → Chương 3 giải phẫu… → thoát sớm.
- **Lệch tông:** RPG hợp chiến thần (Lửng Mật, Tôm Tít) nhưng gượng ép với loài chậm, ngơ (Koala, Lười, Cá Mặt Trăng).
- Tập 1-8 đã đăng đều dùng khung cũ (`LEGACY_6CH`). **Từ Tập 9: không 2 tập liền nhau cùng format, cùng số phần, cùng kiểu thanh tiêu đề, cùng giọng dẫn.**

## 2. Bảng 7 format

| Mã | Tên | Cấu trúc (số phần) | Nhãn badge trên thanh tiêu đề | Persona giọng (xem doc giọng) | Loài hợp |
|---|---|---|---|---|---|
| **F1** | Hồ Sơ Bệnh Án Tiến Hóa Lỗi | Mở đầu (thí nghiệm/cú lừa tên gọi) + **4 hạng mục khám** (sọ → tiêu hóa → tứ chi → tập tính/kết luận) | `BỆNH ÁN #01`, `CHỤP X-QUANG`, `NỘI SOI DẠ DÀY`, `KẾT LUẬN Y KHOA` | `bac_si` — bác sĩ khám nghiệm bất lực | Koala, Gấu Trúc, Lười, Cá Mặt Trăng, Kakapo, Babirusa |
| **F2** | Giải Mã Vũ Khí Tối Mật | **3 giai đoạn**: uy lực thực tế → bản vẽ cơ khí bên trong → tử huyệt | `HỒ SƠ VŨ KHÍ`, `CƠ CHẾ NẠP ĐẠN`, `THỰC CHIẾN`, `ĐIỂM YẾU KỸ THUẬT` | `ky_su_vu_khi` — kỹ sư đọc hồ sơ mật | Tôm Tít, Tôm Súng, Bọ Pháo Thủ, Cá Cung Thủ, Chim Cắt |
| **F3** | Cáo Trạng Tòa Án Tự Nhiên | **Phiên tòa 4 bằng chứng** → lật lại góc khuất để bào chữa → phán quyết | `BẰNG CHỨNG #01`, `NHÂN CHỨNG KỂ LẠI`, `HIỆN TRƯỜNG`, `PHÁN QUYẾT` | `phien_toa` — công tố viên → luật sư bào chữa | Cánh Cụt, Cá Heo, Rái Cá, Tu Hú, Bách Thanh |
| **F4** | Nhật Ký Sinh Tồn 24 Giờ | **Chạy theo mốc giờ** `06:00 → 12:00 → 18:00 → 00:00/02:00` (biến thể: 4 mùa) | `06:00 SÁNG`, `12:00 TRƯA`, `18:00 TỐI`, `02:00 ĐÊM` | `phong_vien_24h` — phóng viên trực tiếp | Chim Ruồi, Chuột Chũi Sao, Lười, Gấu Trúc, Lạc Đà |
| **F5** | Phòng Thí Nghiệm 5 Cấp Độ | **5 level khó dần**, Level 5 = trùm cuối (thường là cú bẻ lái hài) | `THỬ THÁCH CẤP 1` … `CẤP ĐỘ TỐI THƯỢNG` | `nha_khoa_hoc` — nhà khoa học "điên", tempo tăng theo level | Gấu Nước, Sứa Bất Tử, Chuột Trũi, Ếch Gỗ, Axolotl |
| **F6** | Hồ Sơ Đế Chế & Băng Đảng | **Sơ đồ quyền lực**: đáy xã hội → đội quân → chiến thuật bầy đàn → bà trùm | `CẤP BẬC ĐÁY`, `ĐỘI QUÂN CẢM TỬ`, `CHIẾN THUẬT BẦY ĐÀN`, `BÀ TRÙM` | `ong_trum` — người kể phim tài liệu băng đảng | Cá Voi Sát Thủ, Linh Cẩu, Kiến, Ong Bắp Cày, Quạ |
| **F7** | Đấu Trường Sinh Tồn RPG | **5 phần đối kháng**: chỉ số → giáp → vũ khí → đại chiến với Sư Tử/Cá Sấu/Hổ Mang → kết quả | `CHỈ SỐ CHIẾN ĐẤU`, `GIÁP PHÒNG THỦ`, `ĐẠI CHIẾN` | `binh_luan_vien` — bình luận viên esports | Lửng Mật, Hà Mã, Tê Tê, Cầy Mangut, Khỉ Đột |
| **F_SPECIAL** | Đại Hội Sinh Tồn | Nhánh đấu loại trực tiếp giữa các quán quân | `VÒNG LOẠI`, `TỨ KẾT`, `CHUNG KẾT` | `giai_dau` — MC đại hội | Tập 61 |

**Đặt tên chương = câu tò mò của format**, không nhãn kỹ thuật (TASTE-52). Ví dụ F1: `[HẠNG MỤC 1: HỘP SỌ] 40% HỘP SỌ LÀ... NƯỚC LỎNG!`.

## 3. Cách đưa format vào 1 tập (thực thi trong pipeline)

### 3.1 `episode.json`
```json
{
 "episode_no": 9, "animal": "Chim Cánh Cụt",
 "format": "F3", "persona": "phien_toa",
 "longform": {"scenes": [
   {"id": "scene01", "badge": "VỤ ÁN NAM CỰC", "chapter_title": "...", "mood": "tram_bi_an", "parts": [...]},
   {"id": "scene02", "badge": "BẰNG CHỨNG #1", "chapter_title": "...", "parts": [...]}
 ]}
}
```
- **Số scene = số phần của format** (F2: mở đầu + 3, F5: mở đầu + 5…), không cố định 6. Mỗi scene vẫn là 1 "chương" cho renderer/SEO.
- `badge` (≤ 16 ký tự IN HOA) thay chữ "CHƯƠNG N" trên thanh tiêu đề và thẻ chương; đặt lại trong `specs/longform_plan.json > scenes.<id>.badge`
  (pipeline `spec` chuyển sang renderer). Không có `badge` → "CHƯƠNG N" như cũ.
- Banner AI chương (TASTE-62): dùng prompt 2.2.B bên dưới, badge trái = nhãn format.

### 3.2 Độ dài, nhịp hài, luật cũ — vẫn giữ nguyên
Tempo trung bình ≥ 1.10, video dài ≥ 8:30 (~9.300-10.000 ký tự), 1 câu = 1 hình 16:9, sticker có `target`, `display_fix` cho mọi số,
humor-voice (≥ 1 chỗ cười / 20-30s, biệt danh ≥ 4 lần). Format chỉ đổi **khung kể + giọng dẫn**, không nới bất kỳ luật chất lượng nào.

### 3.3 5 quy tắc sống còn khi dựng video dài (từ cẩm nang, đã có trong TASTE-52)
1. Mỗi chi tiết đắt giá chỉ bung ra **1 lần**, giải thích tận gốc rồi sang chi tiết mới.
2. Không "khoảng chết" 3s cuối mỗi tranh — hình kế tiếp lên ngay khi dứt câu.
3. Lời thoại sạch: không "hơ hơ", không đọc nhãn kỹ thuật, không chêm tiếng Anh chuyên ngành.
4. **Không câu tổng kết sáo rỗng** ("hành trình hôm nay cho thấy thiên nhiên thật kỳ diệu…"): sau chi tiết cuối → teaser tập sau 15-20s → outro.
5. Cảnh gom 3-4 tranh nhỏ luôn có 1 câu dẫn ~3s, không để trống giọng.

## 4. Bộ prompt đồ họa theo format

### 4.A Master style (cuối mọi prompt tranh — TASTE-54)
`Clean 2D comic cartoon illustration on pure solid white background, bold black ink outlines, vibrant flat colors, exaggerated funny cartoon facial expressions, clear silhouette for whiteboard animation drawing, no text, no letters, no words, no labels, no numbers, no watermark --ar 16:9` (`--ar 9:16` cho Shorts).

### 4.B Thanh tiêu đề chương biến thiên theo format
```text
2D hand-drawn whiteboard doodle illustration of a two-part horizontal header bar isolated on a pure solid white background. On the left is a sketchy [MÀU BADGE] rounded rectangular badge with bold black marker ink outlines containing bold white comic uppercase Vietnamese text "[NHÃN BADGE]". Immediately to the right is a long horizontal dark navy blue rounded rectangular bar with a sketchy golden-yellow frame containing bold bright yellow comic uppercase Vietnamese text "[TIÊU ĐỀ CHƯƠNG]". Decorated with sketchy yellow stars, tiny green leaves, and [ICON] around the frame corners. Felt-tip marker coloring texture, vibrant colors, clean cutout, no watermark.
```
| Format | [MÀU BADGE] | [ICON] |
|---|---|---|
| F1 | medical teal | medical cross, stethoscope, X-ray film, pill capsules |
| F2 | military olive green | crosshair, blueprint gears, bullets, warning stripes |
| F3 | courtroom gold | gavel, scales of justice, magnifying glass, fingerprint |
| F4 | sunrise orange (đổi sang deep purple cho mốc đêm) | alarm clock, sun / moon, hourglass |
| F5 | laboratory purple | test tubes, bubbling flask, level-up arrows, warning signs |
| F6 | blood red | crown, chess pieces, mafia fedora, pyramid hierarchy chart |
| F7 | red-orange | crossed swords, shield, lightning bolt, HP bar |

### 4.C Banner Shorts — giữ prompt chủ kênh (TASTE-62), thêm 1 đạo cụ của format cạnh con vật (ống nghe, búa tòa, đồng hồ…).

### 4.D Thumbnail
Giữ bố cục TASTE-57 (nền tối + sunburst, tiêu đề trái-trên, con vật to bên phải) + **1 đạo cụ nhận diện format**:
F1 phim X-quang, F2 bản vẽ blueprint, F3 vành móng ngựa/búa tòa, F4 đồng hồ to, F5 ống nghiệm/thanh level, F6 vương miện/sơ đồ quyền lực, F7 thanh HP.

## 5. Shorts theo format — KỂ TRỌN VẸN (45-55s, TASTE-66, chủ kênh chốt 09/11/2026)
> **Phạm vi:** chỉ cho **tập lẻ** (F1-F7). Video tổng hợp/mega sau mỗi 10 tập (F_SPECIAL) **giữ Shorts phễu cũ**
> (bỏ lửng + kêu xem video dài + câu cuối nối vòng) — xem `docs/strategy/MEGA_COMPILATION.md`.

Shorts tập lẻ là **một câu chuyện hoàn chỉnh về con vật**, xem xong là hiểu, KHÔNG còn là phễu kéo sang video dài.
Vẫn **mượn giọng của format** cho câu mở: F1 "Bệnh nhân này…", F3 "Bị cáo…", F4 "Sáu giờ sáng…", F5 "Cấp độ một…", F7 "Tuyển thủ…".

Khung 5 nhịp (900-1.050 ký tự, 10-12 câu, mỗi câu 1 ảnh):
1. **Hook nghịch lý** (1 câu) — điều sốc nhất của con vật.
2. **Giới thiệu** (1-2 câu) — nó là con gì, sống ở đâu, to cỡ nào / biệt danh.
3. **2-3 sự thật đắt giá có số liệu** (4-5 câu) — mỗi sự thật kèm so sánh đời thường.
4. **Giải thích VÌ SAO** (1-2 câu) — cơ chế khoa học / lý do tiến hóa đằng sau nghịch lý.
5. **Câu chốt trọn ý** (1-2 câu) — tổng kết dí dỏm khép lại câu chuyện, trả lời luôn câu hỏi ở hook.

Cấm: câu hỏi bỏ lửng cuối video, "xem video dài / bấm vào kênh / xem trọn bộ / link bên dưới", câu cắt lửng "vì gã này…" để nối vòng.
Ảnh cuối = cảnh con vật minh họa đúng câu chốt. `pipeline.py check` tự cảnh báo nếu Shorts còn câu phễu.

## 6. Lộ trình (đã sửa so với cẩm nang gốc)
Nguồn máy đọc: **`config/series_roadmap.json`** (`pipeline.py check` cảnh báo nếu format/persona trùng tập liền trước).
Điều chỉnh so với bản gốc:
- Tập 8 thực tế là **Chồn Gulo** (khung cũ) và teaser của nó là Chim Cánh Cụt → **Tập 9 = Chim Cánh Cụt (F3)**, **Tập 10 = Gấu Koala (F1)** — kịch bản Koala mẫu ở cẩm nang gốc Phần 3 dùng nguyên cho Tập 10 (đổi teaser cuối sang Gấu Trúc Lớn F4).
- Bản gốc có 2 chỗ trùng format liền nhau: Bọ Pháo Thủ F2 sau Tôm Súng F2 → đổi chỗ với Lươn Điện F5; Kakapo F1 kẹp giữa Cá Mặt Trăng F1 và Babirusa F1 → Kakapo đổi sang **F4** (nhật ký 24h).
- Các tập sau dời +1 so với bảng gốc; Đại Hội Sinh Tồn = Tập 61.

| Tập | Con vật | Format | Persona |
|---|---|---|---|
| 9 | Chim Cánh Cụt | F3 Tòa án | phien_toa |
| 10 | Gấu Koala | F1 Bệnh án | bac_si |
| 11 | Gấu Trúc Lớn | F4 24 giờ | phong_vien_24h |
| 12 | Hà Mã | F7 RPG | binh_luan_vien |
| 13 | Con Lười | F4 24 giờ | phong_vien_24h |
| 14 | Chim Tu Hú | F3 Tòa án | phien_toa |
| 15 | Capybara | F6 Ngoại giao/Đế chế | ong_trum |
| 16 | Tôm Súng | F2 Vũ khí | ky_su_vu_khi |
| 17 | Lươn Điện | F5 Thử thách | nha_khoa_hoc |
| 18 | Bọ Pháo Thủ | F2 Vũ khí | ky_su_vu_khi |
| … | xem `config/series_roadmap.json` (đến Tập 61) | | |

> Tập 11 & 13 cùng F4 nhưng không liền nhau — hợp lệ. Muốn đổi thứ tự: sửa `config/series_roadmap.json`, giữ luật không trùng liền kề.
