# LỊCH ĐĂNG VIDEO — Vẽ Chuyện Hoang Dã

> **SINH TỰ ĐỘNG** từ `python src/episode/publish_schedule.py` (dữ liệu: `config/publish_schedule.json`). Đừng sửa tay — sửa script rồi chạy lại.
> Cập nhật: 23/11/2026 11:52. Giờ Việt Nam (UTC+7).

## Quy tắc (TASTE-68, chốt 12/11/2026)

| Loại | Giờ | Ghi chú |
|---|---|---|
| Video dài tập lẻ | **17:00** ngày D | 1 tập/ngày, không đăng 2 tập/ngày |
| Shorts của tập đó | **11:30** ngày D+1 | Sau đó chạy `link_shorts_related.cjs` (video dài đã công khai) |
| Mega (10 tập) | **17:00 ngày tiếp theo** | Phát sóng ngay sau khi tập thứ 10 của nhóm lên sóng (cứ 10 tập có 1 Mega). Shorts mega 11:30 ngày hôm sau |
| Hashtag | 3 tag có dấu | `#độngvật #<con vật> #VẽChuyệnHoangDã` — tiêu đề không `| Tập N`, Shorts không `#shorts` |

## Khi chủ kênh nói "đăng"

1. `python src/episode/publish_schedule.py --show <số tập | mega-NN>` → in ngày giờ + lệnh upload đúng lịch.
2. Nếu giờ trong lịch đã qua (hoặc < 30 phút nữa) → báo chủ kênh, đề xuất mục kế tiếp; **không** tự dời cả lịch.
3. Chủ kênh chỉ định giờ khác → dùng giờ đó, rồi chạy lại script để cập nhật lịch (mục đã lên lịch lấy giờ từ `upload_result.json`).
4. Sau 17:00 ngày đăng video dài: `node src/episode/link_shorts_related.cjs <project>`.

## Lịch đầy đủ

| # | Video | Video dài | Shorts | Trạng thái | Dự án |
|---|---|---|---|---|---|
| ep1 | Tập 1 — Lửng Mật [▶](https://youtu.be/WRAp223qZ60) | Thứ Tư 04/11/2026 17:34 | Chủ Nhật 15/11/2026 11:30 | ✅ đã lên | `projects/tap-01-lung-mat` |
| ep2 | Tập 2 — Rái Cá Biển [▶](https://youtu.be/DOPcbU7gvjs) | Thứ Năm 05/11/2026 11:48 | — | ✅ đã lên | `projects/tap-02-rai-ca-bien` |
| ep3 | Tập 3 — Cá Heo [▶](https://youtu.be/WbE6Nn7XUIE) | Thứ Năm 05/11/2026 18:23 | — | ✅ đã lên | `projects/tap-03-ca-heo` |
| ep4 | Tập 4 — Thú Mỏ Vịt [▶](https://youtu.be/ogvEUfQOWGA) | Thứ Sáu 06/11/2026 16:07 | — | ✅ đã lên | `projects/tap-04-thu-mo-vit` |
| ep5 | Tập 5 — Chim Bồ Nông [▶](https://youtu.be/KXJQReDxDcA) | Thứ Bảy 07/11/2026 11:00 | — | ✅ đã lên | `projects/tap-05-chim-bo-nong` |
| ep6 | Tập 6 — Gấu Nước [▶](https://youtu.be/HEjl0zaZSTQ) | Thứ Bảy 07/11/2026 18:30 | Thứ Bảy 07/11/2026 18:30 | ✅ đã lên | `projects/tap-06-gau-nuoc` |
| ep7 | Tập 7 — Tôm Tít [▶](https://youtu.be/jLgbk3YMqq4) | Chủ Nhật 08/11/2026 11:30 | Chủ Nhật 08/11/2026 11:30 | ✅ đã lên | `projects/tap-07-tom-tit` |
| ep8 | Tập 8 — Chồn Gulo [▶](https://youtu.be/R4S5wDrD-KQ) | Chủ Nhật 08/11/2026 19:00 | Chủ Nhật 08/11/2026 19:00 | ✅ đã lên | `projects/tap-08-chon-gulo` |
| ep9 | Tập 9 — Chim Cánh Cụt [▶](https://youtu.be/HC1vxRkS1Yk) | Thứ Hai 09/11/2026 11:30 | Thứ Hai 09/11/2026 11:30 | ✅ đã lên | `projects/tap-09-chim-canh-cut` |
| ep10 | Tập 10 — Gấu Koala [▶](https://youtu.be/xeQbH_olDGc) | Thứ Hai 09/11/2026 18:00 | Thứ Hai 09/11/2026 18:00 | ✅ đã lên | `projects/tap-10-gau-koala` |
| mega-01 | **Mega 01 — Đại Hội Sinh Tồn #1 (Tập 1-10)** [▶](https://youtu.be/I_Th6_Vfrmg) | Thứ Ba 10/11/2026 18:30 | Thứ Ba 10/11/2026 18:30 | ✅ đã lên | `projects/mega-01-dai-hoi-sinh-ton` |
| ep11 | Tập 11 — Gấu Trúc Lớn [▶](https://youtu.be/3AvFhe50yv4) | Thứ Ba 10/11/2026 11:30 | Thứ Ba 10/11/2026 11:30 | ✅ đã lên | `projects/tap-11-gau-truc-lon` |
| ep12 | Tập 12 — Hà Mã [▶](https://youtu.be/D8LcXZejE_M) | Thứ Bảy 14/11/2026 18:00 | Thứ Bảy 14/11/2026 18:00 | ✅ đã lên | `projects/tap-12-ha-ma` |
| ep13 | Tập 13 — Con Lười [▶](https://youtu.be/2WQRFsxDuVc) | Thứ Tư 11/11/2026 11:30 | Thứ Tư 11/11/2026 11:30 | ✅ đã lên | `projects/tap-13-con-luoi` |
| ep14 | Tập 14 — Chim Tu Hú [▶](https://youtu.be/1Nw5IMioe84) | Thứ Tư 11/11/2026 18:00 | Thứ Tư 11/11/2026 18:00 | ✅ đã lên | `projects/tap-14-chim-tu-hu` |
| ep15 | Tập 15 — Capybara [▶](https://youtu.be/zmduiBy2GC0) | Chủ Nhật 15/11/2026 18:00 | Chủ Nhật 15/11/2026 18:00 | ✅ đã lên | `projects/tap-15-capybara` |
| ep16 | Tập 16 — Tôm Súng [▶](https://youtu.be/9qwc5nupDYs) | Thứ Năm 12/11/2026 17:00 | Thứ Sáu 13/11/2026 11:30 | ✅ đã lên | `projects/tap-16-tom-sung` |
| ep17 | Tập 17 — Lươn Điện [▶](https://youtu.be/ubQ5nlwFwHY) | Thứ Sáu 13/11/2026 17:00 | Thứ Bảy 14/11/2026 11:30 | ✅ đã lên | `projects/tap-17-luon-dien` |
| ep18 | Tập 18 — Bọ Pháo Thủ [▶](https://youtu.be/m5tPGB8-Lqs) | Thứ Bảy 14/11/2026 17:00 | Chủ Nhật 15/11/2026 11:30 | ✅ đã lên | `projects/tap-18-bo-phao-thu` |
| ep19 | Tập 19 — Thằn Lằn Quỷ Gai [▶](https://youtu.be/TOKARvgr_ps) | Chủ Nhật 15/11/2026 17:00 | Thứ Hai 16/11/2026 11:30 | ✅ đã lên | `projects/tap-19-than-lan-quy-gai` |
| ep20 | Tập 20 — Cá Cung Thủ [▶](https://youtu.be/uEOTKQcGiGQ) | Thứ Hai 16/11/2026 17:00 | Thứ Ba 17/11/2026 11:30 | ✅ đã lên | `projects/tap-20-ca-cung-thu` |
| mega-02 | **Mega 02 — Đại Hội Sinh Tồn Mùa 2 (Tập 11-20)** [▶](https://youtu.be/RXs5TOV1TOw) | Thứ Ba 17/11/2026 17:00 | Thứ Tư 18/11/2026 11:30 | ✅ đã lên | `projects/mega-02-dai-hoi-sinh-ton` |
| ep21 | Tập 21 — Ếch Lông Wolverine [▶](https://youtu.be/BedOTEZNewg) | Thứ Tư 18/11/2026 17:00 | Thứ Năm 19/11/2026 11:30 | ✅ đã lên | `projects/tap-21-ech-long-wolverine` |
| ep22 | Tập 22 — Kỳ Nhông Axolotl [▶](https://youtu.be/_FRAi_hMatQ) | Thứ Năm 19/11/2026 17:00 | Thứ Sáu 20/11/2026 11:30 | ✅ đã lên | `projects/tap-22-ky-nhong-axolotl` |
| ep23 | Tập 23 — Hải Sâm [▶](https://youtu.be/Vvz75e4gSjI) | Thứ Sáu 20/11/2026 17:00 | Thứ Bảy 21/11/2026 11:30 | ✅ đã lên | `projects/tap-23-hai-sam` |
| ep24 | Tập 24 — Cá Mút Đá Hagfish [▶](https://youtu.be/K610mvcP2q0) | Thứ Bảy 21/11/2026 17:00 | Chủ Nhật 22/11/2026 11:30 | ✅ đã lên | `projects/tap-24-ca-mut-da-hagfish` |
| ep25 | Tập 25 — Bạch Tuộc Mimic [▶](https://youtu.be/m4T5sDoTQEY) | Chủ Nhật 22/11/2026 17:00 | Thứ Hai 23/11/2026 11:30 | ✅ đã lên | `projects/tap-25-bach-tuoc-mimic` |
| ep26 | Tập 26 — Gấu Túi Wombat [▶](https://youtu.be/gbNn4hDOF0Q) | Thứ Hai 23/11/2026 17:00 | Thứ Ba 24/11/2026 11:30 | ⏰ đã hẹn giờ | `projects/tap-26-gau-tui-wombat` |
| ep27 | Tập 27 — Chuột Chũi Sao [▶](https://youtu.be/LpexBbrZD_c) | Thứ Ba 24/11/2026 17:00 | Thứ Tư 25/11/2026 11:30 | ⏰ đã hẹn giờ | `projects/tap-27-chuot-chui-sao` |
| ep28 | Tập 28 — Kiến Nổ Cảm Tử [▶](https://youtu.be/HTha5orQDbQ) | Thứ Tư 25/11/2026 17:00 | Thứ Năm 26/11/2026 11:30 | ⏰ đã hẹn giờ | `projects/tap-28-kien-no-cam-tu` |
| ep29 | Tập 29 — Sứa Bất Tử [▶](https://youtu.be/V0EIQ_vxhjY) | Thứ Năm 26/11/2026 17:00 | Thứ Sáu 27/11/2026 11:30 | ⏰ đã hẹn giờ | `projects/tap-29-sua-bat-tu` |
| ep30 | Tập 30 — Hải Ly [▶](https://youtu.be/mk4y7BDSvKE) | Thứ Sáu 27/11/2026 17:00 | Thứ Bảy 28/11/2026 11:30 | ⏰ đã hẹn giờ | `projects/tap-30-hai-ly` |
| mega-03 | **Mega 03 — tổng hợp Tập 21-30** [▶](https://youtu.be/Uv9bObwYZ_0) | Thứ Bảy 28/11/2026 17:00 | Chủ Nhật 29/11/2026 11:30 | ⏰ đã hẹn giờ | `projects/mega-03-dai-hoi-sinh-ton` |
| ep31 | Tập 31 — Chim Cắt Lớn [▶](https://youtu.be/7mo4j23bGE0) | Chủ Nhật 29/11/2026 17:00 | Thứ Hai 30/11/2026 11:30 | ⏰ đã hẹn giờ | `projects/tap-31-chim-cat-lon` |
| ep32 | Tập 32 — Chuột Chũi Trũi [▶](https://youtu.be/sEECUAyj7Ac) | Thứ Hai 30/11/2026 17:00 | Thứ Ba 01/12/2026 11:30 | ⏰ đã hẹn giờ | `projects/tap-32-chuot-chui-trui` |
| ep33 | Tập 33 — Ếch Gỗ Bắc Cực [▶](https://youtu.be/W2_eIz2xpKk) | Thứ Ba 01/12/2026 17:00 | Thứ Tư 02/12/2026 11:30 | ⏰ đã hẹn giờ | `projects/tap-33-ech-go-bac-cuc` |
| ep34 | Tập 34 — Quạ Đen [▶](https://youtu.be/nSnLwEzqNto) | Thứ Tư 02/12/2026 17:00 | Thứ Năm 03/12/2026 11:30 | ⏰ đã hẹn giờ | `projects/tap-34-qua-den` |
| ep35 | Tập 35 — Cá Voi Sát Thủ [▶](https://youtu.be/AeBT1FORR50) | Thứ Năm 03/12/2026 17:00 | Thứ Sáu 04/12/2026 11:30 | ⏰ đã hẹn giờ | `projects/tap-35-ca-voi-sat-thu` |
| ep36 | Tập 36 — Chim Gõ Kiến [▶](https://youtu.be/3CUEadgb9mY) | Thứ Sáu 04/12/2026 17:00 | Thứ Bảy 05/12/2026 11:30 | ⏰ đã hẹn giờ | `projects/tap-36-chim-go-kien` |
| ep37 | Tập 37 — Lạc Đà Sa Mạc [▶](https://youtu.be/zSltw9GkVVA) | Thứ Bảy 05/12/2026 17:00 | Chủ Nhật 06/12/2026 11:30 | ⏰ đã hẹn giờ | `projects/tap-37-lac-da-sa-mac` |
| ep38 | Tập 38 — Dê Núi Bắc Mỹ [▶](https://youtu.be/X8iDYVBtjyQ) | Chủ Nhật 06/12/2026 17:00 | Thứ Hai 07/12/2026 11:30 | ⏰ đã hẹn giờ | `projects/tap-38-de-nui-bac-my` |
| ep39 | Tập 39 — Chim Bách Thanh [▶](https://youtu.be/sDsCqOAroeQ) | Thứ Hai 07/12/2026 17:00 | Thứ Ba 08/12/2026 11:30 | ⏰ đã hẹn giờ | `projects/tap-39-chim-bach-thanh` |
| ep40 | Tập 40 — Kiến Cắt Lá [▶](https://youtu.be/A_ha-Iiyv_Q) | Thứ Ba 08/12/2026 17:00 | Thứ Tư 09/12/2026 11:30 | ⏰ đã hẹn giờ | `projects/tap-40-kien-cat-la` |
| mega-04 | **Mega 04 — tổng hợp Tập 31-40** | Thứ Tư 09/12/2026 17:00 | Thứ Năm 10/12/2026 11:30 | 📝 kế hoạch | `projects/mega-04-biet-doi-dac-nhiem-sinh-hoc` |
| ep41 | Tập 41 — Nhện Lặn Chuông | Thứ Năm 10/12/2026 17:00 | Thứ Sáu 11/12/2026 11:30 | 📝 kế hoạch | `projects/tap-41-nhen-lan-chuong` |
| ep42 | Tập 42 — Cá Thoi Loi | Thứ Sáu 11/12/2026 17:00 | Thứ Bảy 12/12/2026 11:30 | 📝 kế hoạch | `projects/tap-42-ca-thoi-loi` |
| ep43 | Tập 43 — Ong Bắp Cày Ngọc | Thứ Bảy 12/12/2026 17:00 | Chủ Nhật 13/12/2026 11:30 | 📝 kế hoạch | `projects/tap-43-ong-bap-cay-ngoc` |
| ep44 | Tập 44 — Cá Mặt Trăng | Chủ Nhật 13/12/2026 17:00 | Thứ Hai 14/12/2026 11:30 | 📝 kế hoạch | `projects/tap-44-ca-mat-trang` |
| ep45 | Tập 45 — Vẹt Kakapo | Thứ Hai 14/12/2026 17:00 | Thứ Ba 15/12/2026 11:30 | 📝 kế hoạch | `projects/tap-45-vet-kakapo` |
| ep46 | Tập 46 — Lợn Rừng Babirusa | Thứ Ba 15/12/2026 17:00 | Thứ Tư 16/12/2026 11:30 | 📝 kế hoạch | `projects/tap-46-lon-huou-babirusa` |
| ep47 | Tập 47 — Hươu Cao Cổ | Thứ Tư 16/12/2026 17:00 | Thứ Năm 17/12/2026 11:30 | 📝 kế hoạch | `projects/tap-47-huou-cao-co` |
| ep48 | Tập 48 — Cò Mỏ Giày | Thứ Năm 17/12/2026 17:00 | Thứ Sáu 18/12/2026 11:30 | 📝 kế hoạch | `projects/tap-48-co-mo-giay` |
| ep49 | Tập 49 — Nhím Lông Nhọn | Thứ Sáu 18/12/2026 17:00 | Thứ Bảy 19/12/2026 11:30 | 📝 kế hoạch | `projects/tap-49-nhim-long-nhon` |
| ep50 | Tập 50 — Khỉ Đột Lưng Bạc | Thứ Bảy 19/12/2026 17:00 | Chủ Nhật 20/12/2026 11:30 | 📝 kế hoạch | `projects/tap-50-khi-dot-lung-bac` |
| mega-05 | **Mega 05 — tổng hợp Tập 41-50** | Chủ Nhật 20/12/2026 17:00 | Thứ Hai 21/12/2026 11:30 | 📝 kế hoạch | _chưa làm_ |
| ep51 | Tập 51 — Rắn Hổ Mang Chúa | Thứ Hai 21/12/2026 17:00 | Thứ Ba 22/12/2026 11:30 | 📝 kế hoạch | _chưa làm_ |
| ep52 | Tập 52 — Cá Sấu Nước Mặn | Thứ Ba 22/12/2026 17:00 | Thứ Tư 23/12/2026 11:30 | 📝 kế hoạch | _chưa làm_ |
| ep53 | Tập 53 — Cá Voi Xanh | Thứ Tư 23/12/2026 17:00 | Thứ Năm 24/12/2026 11:30 | 📝 kế hoạch | _chưa làm_ |
| ep54 | Tập 54 — Rồng Komodo | Thứ Năm 24/12/2026 17:00 | Thứ Sáu 25/12/2026 11:30 | 📝 kế hoạch | _chưa làm_ |
| ep55 | Tập 55 — Cá Mập Megalodon | Thứ Sáu 25/12/2026 17:00 | Thứ Bảy 26/12/2026 11:30 | 📝 kế hoạch | _chưa làm_ |
| ep56 | Tập 56 — Tê Tê | Thứ Bảy 26/12/2026 17:00 | Chủ Nhật 27/12/2026 11:30 | 📝 kế hoạch | _chưa làm_ |
| ep57 | Tập 57 — Cá Mập Trắng | Chủ Nhật 27/12/2026 17:00 | Thứ Hai 28/12/2026 11:30 | 📝 kế hoạch | _chưa làm_ |
| ep58 | Tập 58 — Đại Bàng Harpy | Thứ Hai 28/12/2026 17:00 | Thứ Ba 29/12/2026 11:30 | 📝 kế hoạch | _chưa làm_ |
| ep59 | Tập 59 — Tắc Kè Hoa | Thứ Ba 29/12/2026 17:00 | Thứ Tư 30/12/2026 11:30 | 📝 kế hoạch | _chưa làm_ |
| ep60 | Tập 60 — Linh Cẩu Đốm | Thứ Tư 30/12/2026 17:00 | Thứ Năm 31/12/2026 11:30 | 📝 kế hoạch | _chưa làm_ |
| mega-06 | **Mega 06 — tổng hợp Tập 51-60** | Thứ Năm 31/12/2026 17:00 | Thứ Sáu 01/01/2027 11:30 | 📝 kế hoạch | _chưa làm_ |

## Ghi chú lịch sử

- Tập 1–15 + Mega 01 đăng theo lịch cũ (2 tập/ngày 11:30 & 18:00, Shorts cùng giờ). Số liệu 12/11/2026: Shorts 11:30 hơn Shorts tối; video dài 0–33 view vì Shorts chưa gắn "Video có liên quan" (đã gắn lại Tập 6–15 + Mega 01).
- Tập 16–20 đã dời sang lịch mới ngày 12/11/2026.
- `projects/mega-01-bang-phong-than/` (bản cắt ghép) **không nằm trong lịch** — chỉ đăng khi chủ kênh yêu cầu.
