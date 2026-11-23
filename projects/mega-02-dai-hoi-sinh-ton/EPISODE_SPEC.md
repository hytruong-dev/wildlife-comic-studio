# TẬP ĐẶC BIỆT ĐẠI HỘI SINH TỒN #2 (SAU 10 TẬP TIẾP THEO: TẬP 11-20) — 10 QUÁI KIỆT — ĐẠI HỘI SINH TỒN MÙA 2 · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`mega-02-dai-hoi-sinh-ton`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/mega-02-dai-hoi-sinh-ton`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F_SPECIAL` · **Persona giọng:** `giai_dau` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | 10 quái kiệt — Đại Hội Sinh Tồn Mùa 2 |
| Tiêu đề YouTube | [TẬP ĐẶC BIỆT] 10 Quái Kiệt Tranh Đoạt Vương Miện Vũ Khí Sinh Học: Ai Lên Ngôi Vô Địch? |
| Video dài | `renders/mega-02-dai-hoi-sinh-ton_long.mp4` — 60:27.7 (3627.7s) |
| Shorts | `renders/mega-02-dai-hoi-sinh-ton_shorts.mp4` — 0:51.3 (51.3s) |
| Thumbnail | `renders/mega-02-dai-hoi-sinh-ton_thumbnail.jpg` |
| Số hình | dài 410 beat / 410 ảnh riêng; Shorts 11 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.1**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 60:00.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/410 của video YouTube về 10 quái kiệt — Đại Hội Sinh Tồn Mùa 2). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: anh MC dẫn chương trình hoạt hình vui tính: tóc vuốt dựng, mặc bộ vest đỏ tươi, thắt nơ bướm vàng, cầm chiếc micro vàng, nụ cười rộng. Nhân vật phụ cố định: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — 10 QUÁI KIỆT MỚI BƯỚC VÀO ĐẤU TRƯỜNG VŨ KHÍ
*Thẻ chương:* ĐẤU TRƯỜNG VŨ KHÍ MÙA 2

*Badge:* `KHAI MẠC MÙA 2` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene01_p0.wav` (700 ký tự) · mood `tram_bi_an`

```text
Bóng tối bao trùm lấy một đấu trường La Mã khổng lồ giữa lòng rừng già đại ngàn... Mười chiếc bục thi đấu bọc thép đứng im lìm trong màn sương đêm kỳ bí. Và ở chính giữa đấu trường, một chiếc vương miện vàng nạm đá quý lấp lánh đang xoay tròn trên bệ đá cẩm thạch, chờ đợi chủ nhân xứng đáng nhất. Đêm nay, mười sinh vật kỳ dị từ Tập mười một đến Tập hai mươi của kênh Vẽ Chuyện Hoang Dã sẽ chính thức hội tụ trên cùng một sàn đấu sinh tử! Không phải để kể lại những gì khán giả đã xem, mà để đọ sức trực tiếp bằng hàng loạt phát hiện khoa học mới toanh chưa từng tiết lộ! Mỗi loài mang theo một bí mật tiến hóa dị thường mà ngay cả những nhà sinh vật học lão luyện nhất cũng phải ngỡ ngàng bật ngửa.
```
**Part 1** → `audio/vs/scene01_p1.wav` (715 ký tự) · mood `hao_hung`

```text
[surprise-oh] Bật toàn bộ đèn pha! Chào mừng toàn thể muôn loài muôn thú đã đến với Đại Hội Sinh Tồn Mùa hai! Tôi là người dẫn chương trình đêm nay, và tôi xin cam kết danh dự: tất cả những gì bạn sắp nghe đều là những công trình nghiên cứu mới hoàn toàn! Từ việc Gấu Trúc tắm phân ngựa để chống rét, cho tới Cá Cung Thủ nhớ được bốn mươi bốn khuôn mặt người hay Tôm Súng bắn ra dòng plasma dưới đáy biển! [laughter] Luật chơi Mùa hai vô cùng khốc liệt: tám vòng thi đấu chính thức, xen kẽ giờ giải lao hậu trường, lễ trao giải phụ và vòng phúc khảo tin đồn thế kỷ. Mỗi vòng thi, ban giám khảo trao ba tấm huy chương: Vàng được ba điểm, Bạc hai điểm, và Đồng một điểm. Riêng Vòng Chung Kết sẽ được nhân đôi điểm số!
```
**Part 2** → `audio/vs/scene01_p2.wav` (116 ký tự) · 🎭 cameo `tham_phan`

```text
Giám khảo xin nhắc nhở: cấm nã đạn vào bảng điểm, cấm phóng điện vào ghế ban tổ chức và cấm đi vệ sinh giữa sân đấu!
```
**Part 3** → `audio/vs/scene01_p3.wav` (228 ký tự) · mood `hao_hung`

```text
Nghe rõ chưa các đấu sĩ? Nhất là anh chàng Hà Mã và cô nàng Bọ Pháo Thủ đang cười tủm tỉm đằng kia! [laughter] Bây giờ, xin mời toàn thể khán đài cùng chào đón sự xuất hiện của mười tuyển thủ tinh nhuệ nhất Mùa hai trên thảm đỏ!
```
**Part 4** → `audio/vs/scene01_p4.wav` (526 ký tự) · mood `don_dap`

```text
Tuyển thủ số một! Thiện xạ đầm lầy sở hữu bộ não tính toán quang học không cần vỏ não! Cá Cung Thủ! Tuyển thủ số hai! Chiến binh sa mạc Úc mặc áo giáp chông sắt và hút ẩm từ cát khô! Thằn Lằn Quỷ Gai! Tuyển thủ số ba! Siêu pháo thủ tí hon chỉ dài bằng đốt ngón tay nhưng truyền cảm hứng cho động cơ tên lửa! Bọ Pháo Thủ! Tuyển thủ số bốn! Cỗ máy phát điện sống biết hợp tác săn mồi theo bầy đàn hơn một trăm con! Lươn Điện! Tuyển thủ số năm! Thủ lĩnh đội quân tôm lính sống trong tổ bọt biển dưới quyền một Tôm Chúa! Tôm Súng!
```
**Part 5** → `audio/vs/scene01_p5.wav` (457 ký tự) · mood `hao_hung`

```text
Tuyển thủ số sáu! Quý ngài ngoại giao Pantanal nuôi con chung bình đẳng và ngủ ngâm mình dưới lòng sông! Capybara! Tuyển thủ số bảy! Kẻ cải trang thành chim ưng để đánh lừa hàng xóm và bay vòng tròn mười sáu ngàn cây số mỗi năm! Chim Tu Hú! Tuyển thủ số tám! Chú gấu lười rừng mưa mang cả vườn nấm tiêu diệt tế bào ung thư trên từng sợi lông! Con Lười! Tuyển thủ số chín! Người vận chuyển hàng tạ nguyên tố Silicon cho các dòng sông lớn tại châu Phi! Hà Mã!
```
**Part 6** → `audio/vs/scene01_p6.wav` (115 ký tự) · mood `nghiem_trang_gia`

```text
Và tuyển thủ số mười... xin mời quý vị nhìn lên màn hình vì bạn ấy đang bận trồng cây chuối bên ngoài sân vận động!
```
**Part 7** → `audio/vs/scene01_p7.wav` (86 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Ơ... tới lượt em đi vào rồi hả? Đợi em tụt xuống nhặt nốt nhánh trúc đã nha anh MC ơi!
```
**Part 8** → `audio/vs/scene01_p8.wav` (140 ký tự) · mood `hao_hung`

```text
Rồi, đủ mười thành viên tinh anh! Và theo nghi thức truyền thống của Đại Hội Sinh Tồn, mời cả mười đấu sĩ tiến vào khu vực Lễ Cân Ký Đo Đạc!
```
**Part 9** → `audio/vs/scene01_p9.wav` (564 ký tự) · mood `don_dap`

```text
Hà Mã bước lên đầu tiên! Rầm! Mặt sàn rung bần bật! Hơn ba tấn trọng lượng đè nặng xuống bàn cân thép chịu lực! Tuyển thủ nặng ký nhất giải đấu! Tiếp theo là Gấu Trúc Lớn: một trăm mười ki-lô-gam cơ bắp và mỡ dự phòng, dù nhìn bề ngoài trông chỉ toàn bông gòn! Bố Già Capybara bước lên với phong thái điềm đạm tuyệt đối: sáu mươi lăm ki-lô-gam! Chuột gặm nhấm lớn nhất hành tinh hiện nay! Lươn Điện dài hai mét nặng hai mươi ki-lô-gam trườn lên bàn cân thủy tinh; kế bên là Con Lười nặng bốn ki-lô-gam nhưng một phần ba trọng lượng nằm ở bụng lá cây chưa tiêu hóa!
```
**Part 10** → `audio/vs/scene01_p10.wav` (306 ký tự) · mood `hao_hung`

```text
Nhóm hạng lông tiếp tục lên sàn: Chim Tu Hú nặng chỉ một trăm mười gam, Thằn Lằn Quỷ Gai vỏn vẹn bốn mươi gam, và Cá Cung Thủ hai trăm gam! Cuối cùng là hai gã tí hon Tôm Súng và Bọ Pháo Thủ! Cân thông thường không thể đo nổi, ban tổ chức phải dùng cân phân tích hóa học trong lồng kính kín gió! [laughter]
```
**Part 11** → `audio/vs/scene01_p11.wav` (165 ký tự) · mood `nghiem_trang_gia`

```text
Bọ Pháo Thủ chỉ nặng chưa đầy nửa gam! Tức là Hà Mã nặng gấp... sáu triệu lần Bọ Pháo Thủ! Sự chênh lệch này khiến máy tính của ban tổ chức suýt bốc khói! [laughter]
```
**Part 12** → `audio/vs/scene01_p12.wav` (273 ký tự) · mood `hao_hung`

```text
Sau lễ cân ký, giới cá cược và chuyên gia phân tích đồng loạt đặt cửa vô địch cho ba gã khổng lồ hỏa lực: Tôm Súng, Lươn Điện và Hà Mã! Còn Bọ Pháo Thủ nửa gam và Con Lười chậm chạp? Các chuyên gia ghi một dòng ngắn gọn: chỉ mong hai bạn đi hết được vòng gửi xe! [laughter]
```
**Part 13** → `audio/vs/scene01_p13.wav` (281 ký tự) · mood `tram_bi_an`

```text
Nhưng đừng bao giờ coi thường sức mạnh ẩn giấu của những kẻ nhỏ bé! Đêm nay, từng định kiến sẽ bị lật tung bằng những dữ liệu khoa học xác thực nhất! Tám vòng thi đấu! Một trăm phần trăm dữ liệu mới! Chỉ có trí tuệ tiến hóa thực sự mới đủ sức chạm tay vào chiếc vương miện Mùa hai!
```
**Part 14** → `audio/vs/scene01_p14.wav` (110 ký tự) · mood `hao_hung`

```text
Khoan đã, trước khi vào vòng một, hãy cùng nghe nhận xét nhanh từ tổ trọng tài kỹ thuật về dàn đấu sĩ năm nay!
```
**Part 15** → `audio/vs/scene01_p15.wav` (135 ký tự) · 🎭 cameo `co_tro_ly`

```text
Báo cáo MC: toàn bộ các cảm biến áp suất, đồng hồ đo vôn kế một ngàn vôn và máy chụp CT đều đã được hiệu chuẩn ở mức an toàn tuyệt đối!
```
**Part 16** → `audio/vs/scene01_p16.wav` (268 ký tự) · mood `hao_hung`

```text
Tuyệt vời! Còn các tuyển thủ thì sao? Tôm Súng đang khởi động khớp lò xo càng súng lách tách, trong khi Hà Mã đang há miệng kiểm tra lại cặp răng nanh! Không chần chừ thêm một giây nào nữa! Chúng ta hãy cùng tiến vào Vòng một ngay bây giờ: Năng lượng và cấu tạo kỳ dị!
```

### scene02 — CẤU TẠO KỲ DỊ VÀ NGUỒN NĂNG LƯỢNG BÍ MẬT BÊN TRONG CƠ THỂ
*Thẻ chương:* BÍ MẬT NĂNG LƯỢNG SINH HỌC

*Badge:* `VÒNG 1` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene02_p0.wav` (542 ký tự) · mood `hao_hung`

```text
Chào mừng toàn thể khán đài bước vào Vòng một: Giải mã cấu tạo ẩn giấu và nguồn năng lượng sinh học! Ở vòng mở màn này, chúng ta không thi chạy hay cắn nhau, mà đưa các tuyển thủ vào máy quét công nghệ cao! Ban giám khảo muốn biết: bộ máy bên trong cơ thể loài nào được thiết kế tinh vi, tiết kiệm hoặc tạo ra công suất năng lượng điên rồ nhất? Thí sinh đầu tiên bước vào máy quét ba chiều là pháo thủ đại dương Tôm Súng! Khán giả đều đã biết cú búng càng tạo sóng âm của nó, nhưng cấu tạo tạo ra plasma mới là điều làm các kỹ sư choáng váng!
```
**Part 1** → `audio/vs/scene02_p1.wav` (287 ký tự) · mood `nghiem_trang_gia`

```text
Năm hai ngàn mười chín, nhóm kỹ sư cơ khí tại Đại học Texas A&M đã dùng tia X siêu nhỏ quét lớp vỏ lột xác của Tôm Súng để in ba chiều phóng đại gấp năm lần! Họ gắn một lò xo bẫy chuột để mô phỏng cơ bắp tôm búng càng! Kết quả thu được khiến cả giới vật lý plasma phải sững sờ kinh ngạc!
```
**Part 2** → `audio/vs/scene02_p2.wav` (362 ký tự) · mood `don_dap`

```text
Chỉ bằng lực cơ học đơn thuần không cần dùng điện hay tia laser, thiết bị mô phỏng càng Tôm Súng đã tạo ra dòng plasma dưới nước với hiệu suất cao gấp mười lần máy móc nhân tạo hiện đại! Nhưng điều thú vị hơn nằm ở chức năng dự phòng thiên tài của Tôm Súng! Điều gì xảy ra nếu trong một cuộc giao tranh nảy lửa, nó bị kẻ thù cắn gãy mất chiếc càng súng khổng lồ?
```
**Part 3** → `audio/vs/scene02_p3.wav` (528 ký tự) · mood `hao_hung`

```text
Câu trả lời là: nó không hề bị tàn phế! Ngay sau khi mất chiếc càng súng bên phải, bộ gen của Tôm Súng lập tức kích hoạt cơ chế đảo ngược bất đối xứng! Chiếc càng nhỏ vốn chỉ dùng để gắp thức ăn bên tay trái sẽ phình to thần tốc sau vài lần lột xác, biến hình thành một khẩu đại bác súng nước mới toanh! Còn bên cụt cũ sẽ mọc lại một chiếc càng nhỏ thay thế! [surprise-oh] Một dây chuyền tự đổi tay thuận và tái tạo vũ khí vĩnh cửu! Dù gãy súng bao nhiêu lần, Tôm Súng vẫn luôn có một khẩu đại bác dự phòng trong tay! [laughter]
```
**Part 4** → `audio/vs/scene02_p4.wav` (321 ký tự) · mood `tram_bi_an`

```text
Và để kiểm tra thêm độ hiệu quả của cấu trúc cơ thể, các nhà nghiên cứu còn đưa thêm một thí sinh hạng trung vào buồng kiểm tra cấu trúc xương đặc biệt: Capybara! Mặc dù sống quanh năm tại vùng đầm lầy nóng ẩm Nam Mỹ, Capybara lại sở hữu rất ít tuyến mồ hôi trên da nên không thể đổ mồ hôi làm mát như con người hay ngựa!
```
**Part 5** → `audio/vs/scene02_p5.wav` (228 ký tự) · mood `hao_hung`

```text
Thay vì tốn nước đổ mồ hôi, cấu trúc bộ lông thưa cứng và lớp mỡ mỏng cho phép nhiệt lượng thoát ra cực nhanh ngay khi nó bước xuống ngâm mình trong làn nước mát! Một thiết kế làm mát bằng nước hoàn hảo cho gã khổng lồ gặm nhấm!
```
**Part 6** → `audio/vs/scene02_p6.wav` (102 ký tự) · 🎭 cameo `tham_phan`

```text
Giám khảo ghi nhận: cấu trúc cơ khí tạo plasma siêu việt và khả năng đổi tay vũ khí cực kỳ thông minh!
```
**Part 7** → `audio/vs/scene02_p7.wav` (214 ký tự) · mood `hao_hung`

```text
Tuyển thủ thứ hai bước vào buồng đo công suất năng lượng là Nhà Máy Điện Sống: Lươn Điện! Chúng ta đều biết con số đỉnh tám trăm sáu mươi Vôn, nhưng công suất điện thực tế và cơ chế bơm ion mới là kỳ quan sinh học!
```
**Part 8** → `audio/vs/scene02_p8.wav` (520 ký tự) · mood `don_dap`

```text
Trong khoảnh khắc săn mồi, nguồn điện của Lươn Điện có thể đạt cường độ dòng điện xấp xỉ một Ampe, tức là công suất tức thời đạt mức tương đương hơn tám trăm Oát! Làm thế nào sáu ngàn tế bào pin sinh học có thể xả hàng chục phát liên tiếp mà không bị cạn kiệt ngay lập tức? Bí mật nằm ở hệ thống bơm ion Natri và Kali siêu tốc! Ngay sau mỗi lần phóng điện, các bơm sinh hóa tiêu thụ phân tử năng lượng ATP lập tức vận chuyển ngược dòng hàng tỷ ion qua màng tế bào, tái nạp điện thế sẵn sàng chiến đấu chỉ trong tích tắc!
```
**Part 9** → `audio/vs/scene02_p9.wav` (188 ký tự) · mood `tram_bi_an`

```text
Không cần dây cắm sạc, không cần pin lithium độc hại, toàn bộ quá trình sản xuất và tái nạp điện diễn ra bằng muối khoáng và nước ngọt ngay trong thớ thịt mềm mại của con cá! [surprise-wa]
```
**Part 10** → `audio/vs/scene02_p10.wav` (487 ký tự) · mood `nghiem_trang_gia`

```text
Và bây giờ là bất ngờ gây sốc nhất Vòng một! Tuyển thủ thứ ba bước lên máy đo năng lượng là chú gấu tròn xoe suốt ngày chỉ biết ôm tre: Gấu Trúc Lớn! Trong suốt nhiều thập kỷ, giới sinh học đau đầu tự hỏi: ăn một thứ thức ăn nghèo dinh dưỡng như tre với đường ruột ngắn ngủn của thú ăn thịt, tại sao Gấu Trúc không chết đói? Năm hai ngàn mười lăm, nghiên cứu đột phá công bố trên tạp chí Science của nhóm tiến sĩ Yonggang Nie đã giải mã bí mật động trời ẩn sâu trong bộ gen của Gấu Trúc!
```
**Part 11** → `audio/vs/scene02_p11.wav` (332 ký tự) · mood `don_dap`

```text
Các nhà khoa học phát hiện Gấu Trúc sở hữu một đột biến độc nhất vô nhị trên gen Đu-ốc hai — loại gen chịu trách nhiệm tổng hợp hormone tuyến giáp kiểm soát tốc độ đốt cháy năng lượng! Kết quả là mức độ hormone tuyến giáp Tê bốn trong máu Gấu Trúc chỉ bằng bốn mươi sáu phẩy chín phần trăm so với các loài thú có vú cùng kích thước!
```
**Part 12** → `audio/vs/scene02_p12.wav` (606 ký tự) · mood `hao_hung`

```text
Không chỉ giảm hormone, tiến hóa còn thu nhỏ kích thước não bộ của Gấu Trúc đi năm phần trăm và kích thước quả thận đi mười một phần trăm để cắt giảm tối đa chi phí vận hành cơ thể! Tính tổng thể, mức tiêu hao năng lượng hàng ngày của Gấu Trúc hoang dã chỉ bằng bốn mươi lăm phần trăm so với một con thú bình thường nặng bằng nó! Tức là nó sống bằng chưa tới một nửa bình xăng của loài khác! [surprise-oh] Để kiểm chứng, các nhà khoa học đã cấy đúng đoạn đột biến gen này vào chuột thí nghiệm, và lũ chuột lập tức trở nên ít vận động hơn hẳn năm mươi lăm phần trăm y hệt phong thái của gấu trúc! [laughter]
```
**Part 13** → `audio/vs/scene02_p13.wav` (346 ký tự) · 🎭 cameo `tham_phan`

```text
Vòng một kết thúc với kết quả thuyết phục tuyệt đối! Ban giám khảo xin công bố huy chương đồng thuộc về Gấu Trúc Lớn với đột biến gen Đu-ốc hai tiết kiệm năng lượng thiên tài! Huy chương bạc thuộc về Lươn Điện với hệ thống tái nạp ion siêu tốc! Và Huy chương vàng gọi tên Tôm Súng với công nghệ plasma vượt trội cùng cơ chế đổi tay súng dự phòng!
```
**Part 14** → `audio/vs/scene02_p14.wav` (258 ký tự) · mood `hao_hung`

```text
Bảng tổng sắp sau Vòng một: Tôm Súng dẫn đầu với ba điểm, Lươn Điện hai điểm, và Gấu Trúc Lớn xuất sắc ghi điểm đồng đầu tiên! Vòng hai ngay sau đây sẽ thử thách khả năng bắn tỉa tầm xa và trí tuệ quang học siêu phàm! Mời quý vị cùng hướng mắt về trường bắn!
```

### scene03 — XẠ THỦ TẦM XA VÀ TRÍ TUỆ THỊ GIÁC KHÔNG TƯỞNG
*Thẻ chương:* BẮN TỈA VÀ NHẬN DIỆN KHUÔN MẶT

*Badge:* `VÒNG 2` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene03_p0.wav` (419 ký tự) · mood `hao_hung`

```text
Chào mừng toàn thể quý vị đến với Vòng hai: Đấu trường xạ thủ tầm xa và trí tuệ thị giác siêu phàm! Ở vòng này, ban giám khảo không chỉ đo tầm bắn mà còn kiểm tra bộ não xử lý hình ảnh của các tuyển thủ! Đấu sĩ mở màn là tay súng thiện xạ nổi tiếng nhất thế giới cá: Cá Cung Thủ! Khán giả đều đã nghe tài bắn tia nước tính khúc xạ ánh sáng của nó, nhưng thí nghiệm tại Đại học Oxford mới thực sự gây chấn động thế giới!
```
**Part 1** → `audio/vs/scene03_p1.wav` (327 ký tự) · mood `tram_bi_an`

```text
Lâu nay giới khoa học thần kinh tin rằng chỉ những loài có vỏ não mới phát triển cao như con người, khỉ hay chim mới có khả năng phân biệt được khuôn mặt phức tạp của con người! Cá hoàn toàn không có cấu trúc vỏ não mới này! Vậy liệu một con cá nhỏ bé ở đầm lầy có thể phân biệt được mặt người này với mặt người khác hay không?
```
**Part 2** → `audio/vs/scene03_p2.wav` (727 ký tự) · mood `don_dap`

```text
Năm hai ngàn mười sáu, tiến sĩ Cait Newport tại Đại học Oxford và Đại học Queensland đã công bố nghiên cứu chấn động trên tạp chí Scientific Reports! Nhóm nghiên cứu huấn luyện Cá Cung Thủ nhận diện một khuôn mặt người mục tiêu để nhận thưởng thức ăn, sau đó trộn lẫn khuôn mặt đó vào giữa bốn mươi bốn khuôn mặt người lạ hoàn toàn khác nhau! Kết quả làm toàn bộ giới khoa học thần kinh sững sờ: Cá Cung Thủ phun tia nước trúng phóc bức ảnh khuôn mặt quen thuộc với độ chính xác trung bình từ tám mươi mốt đến tám mươi sáu phần trăm! [surprise-oh] Thậm chí khi các nhà khoa học chuyển toàn bộ ảnh sang màu đen trắng, đồng bộ độ sáng và cắt bỏ hết kiểu tóc lẫn đường viền đầu, chú cá vẫn nhận ra gương mặt đó không chút sai sót!
```
**Part 3** → `audio/vs/scene03_p3.wav` (469 ký tự) · mood `hao_hung`

```text
Quý vị thử tưởng tượng xem: một con cá dài một gang tay không có vỏ não nhận dạng lại nhớ mặt người giỏi hơn cả nhiều ứng dụng camera an ninh cũ kỹ! [laughter] Chưa dừng lại ở đó, khi bắn mồi thật trên cành cây, Cá Cung Thủ còn tự động đo trọng lượng của con mồi để điều chỉnh thể tích tia nước bắn ra! Nó kiểm soát sự bất ổn định thủy động lực học khi nén dòng nước, tụ toàn bộ năng lượng vào mũi đạn tạo ra lực va chạm lớn hơn lực bám chân của côn trùng tới mười lần!
```
**Part 4** → `audio/vs/scene03_p4.wav` (405 ký tự) · mood `tram_bi_an`

```text
Không chỉ nhớ được bốn mươi bốn khuôn mặt ở góc nhìn thẳng, thí nghiệm nâng cao của Đại học Oxford còn thử xoay nghiêng các bức ảnh khuôn mặt theo nhiều góc độ khác nhau! Kết quả đáng kinh ngạc: Cá Cung Thủ vẫn nhận diện chính xác người quen qua từng góc nghiêng mà không hề bị đánh lừa! Điều này chứng tỏ thị giác của loài cá này giải mã không gian ba chiều phức tạp hơn ta tưởng rất nhiều! [surprise-oh]
```
**Part 5** → `audio/vs/scene03_p5.wav` (113 ký tự) · 🎭 cameo `tham_phan`

```text
Giám khảo ghi nhận: bộ não xử lý thị giác của Cá Cung Thủ là một kiệt tác vượt xa mọi giới hạn kích thước não bộ!
```
**Part 6** → `audio/vs/scene03_p6.wav` (991 ký tự) · mood `don_dap`

```text
Tuyển thủ thứ hai bước vào bài thi bắn tỉa là pháo thủ tí hon: Bọ Pháo Thủ! Nếu Cá Cung Thủ bắn tỉa bằng tia nước lạnh, thì Bọ Pháo Thủ là chuyên gia điều áp và nổ xung phản lực vi mô! Quý vị đã biết nhiệt độ tia hóa chất của nó sôi một trăm độ C, nhưng điều gì tạo ra lực đẩy mạnh mẽ mà không làm vỡ nòng súng chỉ rộng vài phần nghìn xăng-ti-mét? Theo nghiên cứu mô phỏng thủy động lực học tại Đại học Leeds, bí mật nằm ở quá trình sôi chớp nhoáng bên trong buồng đốt nhỏ xíu: hơi nước chiếm tới hơn chín mươi phần trăm thể tích khí thoát ra! Áp suất chỉ cần tăng nhẹ khoảng một trăm mili-ba là đủ tống toàn bộ hỗn hợp hóa chất sôi ra ngoài với vận tốc từ mười hai đến ba mươi lăm mét mỗi giây, xé nhỏ thành hàng tỷ hạt sương đường kính chỉ từ một đến năm trăm mi-crô-mét! Nhờ tháp pháo đuôi có khớp xoay linh hoạt hai trăm bảy mươi độ, chú bọ tí hon có thể vừa chạy trốn vừa bắn chuẩn xác vào mắt những kẻ săn mồi đang truy đuổi phía sau lưng mà không cần ngoái đầu nhìn lại! [surprise-wa]
```
**Part 7** → `audio/vs/scene03_p7.wav` (492 ký tự) · mood `tram_bi_an`

```text
Và tuyển thủ thứ ba của vòng hai mang đến một tuyệt kỹ đánh lừa thị giác đỉnh cao không cần dùng đến một giọt đạn nào: Chim Tu Hú! Khán giả đều đã nghe chuyện Tu Hú đẻ trộm trứng trong mười giây, nhưng tại sao một con chim to xác như Tu Hú lại có thể bình yên bay lượn sát tổ chim chủ mà không bị bầy chim nhỏ xúm vào mổ đuổi đi? Năm hai ngàn mười một, giáo sư Welbergen và Davies công bố phát hiện thú vị trên tạp chí Behavioral Ecology về chiến thuật ngụy trang Batesian kép của Chim Tu Hú!
```
**Part 8** → `audio/vs/scene03_p8.wav` (587 ký tự) · mood `hao_hung`

```text
Từ hình dáng cánh nhọn, kiểu bay lướt gió cho đến những dải lông vằn ngang màu nâu xám trước ngực và chân vàng, Chim Tu Hú trưởng thành đã tiến hóa ngoại hình giống hệt... Chim Ưng Sẻ ăn thịt! Khi chim chủ nhà nhìn thấy bộ ngực vằn ngang đó lướt qua, chúng lập tức hoảng loạn tưởng là kẻ săn mồi hung tợn nên bay đi trốn giữ mạng thay vì ở lại tấn công kẻ lạ mặt! [laughter] Thậm chí các nhà khoa học thử dùng sơn che đi các vạch vằn trên ngực mô hình Tu Hú, lập tức đàn chim chích trở nên hung hãn lao vào đánh đuổi túi bụi! Một màn cải trang cảnh sát chìm ngoạn mục của giới loài chim!
```
**Part 9** → `audio/vs/scene03_p9.wav` (535 ký tự) · mood `hao_hung`

```text
Thêm một màn đọ tài gay cấn nữa ở bài kiểm tra thị giác mà anh MC xin bổ sung giữa hai sát thủ bắn tỉa dưới nước: Cá Cung Thủ và Lươn Điện! Trong tự nhiên, mặt nước đâu phải lúc nào cũng phẳng lặng như gương! Các thí nghiệm chứng minh Cá Cung Thủ vẫn bắn trúng đích ngay cả khi mặt nước đang gợn sóng liên tục nhờ khả năng cập nhật góc lệch theo thời gian thực! Còn Lươn Điện thì dùng trường điện áp thấp mười Vôn để phân biệt rạch ròi đâu là một thanh nhựa cách điện vô tri, đâu là một con cá thật đang thở thoi thóp dưới lớp bùn đặc!
```
**Part 10** → `audio/vs/scene03_p10.wav` (314 ký tự) · 🎭 cameo `tham_phan`

```text
Kết quả Vòng hai đã được chốt! Huy chương đồng thuộc về Chim Tu Hú với màn cải trang thành Chim Ưng Sẻ đánh lừa cả xóm chim chủ! Huy chương bạc thuộc về Bọ Pháo Thủ với vòi phun sương tốc độ ba mươi lăm mét mỗi giây! Và Huy chương vàng thuộc về Cá Cung Thủ với siêu năng lực nhận diện bốn mươi bốn khuôn mặt người!
```
**Part 11** → `audio/vs/scene03_p11.wav` (319 ký tự) · mood `hao_hung`

```text
Bảng tổng sắp cập nhật điểm số sau hai vòng: Tôm Súng và Cá Cung Thủ đồng dẫn đầu với ba điểm! Bọ Pháo Thủ bám sát với hai điểm! Lươn Điện hai điểm, Gấu Trúc một điểm, Tu Hú một điểm! Vòng ba ngay sau đây sẽ thử thách khả năng sinh tồn trước thời tiết khắc nghiệt và những giải pháp chống chọi thiên nhiên kỳ quặc nhất!
```

### scene04 — CHỐNG CHỊU THỜI TIẾT KHẮC NGHIỆT — TẮM PHÂN NGỰA, HÚT CÁT ẨM VÀ TREO NỘI TẠNG
*Thẻ chương:* BÍ KÍP CHỐNG RÉT VÀ NẮNG CHÁY

*Badge:* `VÒNG 3` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene04_p0.wav` (569 ký tự) · mood `hao_hung`

```text
Chào mừng quý vị đến với Vòng ba: Thử thách chống chịu thời tiết cực hạn! Sân vận động lúc này được chia thành hai nửa đối lập: một bên là núi tuyết mùa đông lạnh buốt và một bên là sa mạc nắng cháy bỏng rát! Ở vòng này, ban giám khảo muốn tìm ra những bộ óc sinh tồn sáng tạo nhất: khi thiên nhiên nổi giận với cái rét cắt da hay cái nóng thiêu đốt, bạn dùng chiêu gì để sống sót? Đấu sĩ bước vào nửa sân băng tuyết đầu tiên là chú gấu mũm mĩm đến từ dãy núi Tứ Xuyên: Gấu Trúc Lớn! Một loài gấu nhưng hoàn toàn không biết ngủ đông như họ hàng gấu nâu hay gấu Bắc Cực!
```
**Part 1** → `audio/vs/scene04_p1.wav` (330 ký tự) · mood `tram_bi_an`

```text
Không ngủ đông, ăn thực đơn tre nghèo nàn calo nên không tích trữ được nhiều lớp mỡ dày, làm thế nào Gấu Trúc hoang dã có thể chịu nổi những đêm đông tuyết rơi trắng xóa trên đỉnh núi cao? Năm hai ngàn hai mươi, nhóm nghiên cứu của giáo sư Fuwen Wei công bố phát hiện trên tạp chí PNAS khiến cả thế giới phải... bịt mũi ngỡ ngàng!
```
**Part 2** → `audio/vs/scene04_p2.wav` (510 ký tự) · mood `bi_hai`

```text
Khi trời trở lạnh giữa tiết trời từ âm năm đến mười lăm độ C, Gấu Trúc hoang dã đi tìm những đống phân ngựa tươi mới thải ra dưới mười ngày tuổi! Nó không ngửi cho vui... mà nó cúi xuống chà xát phân ngựa lên má, lên cổ, rồi lăn lộn toàn thân mình vào giữa đống phân ngựa cho đến khi phủ kín khắp bộ lông trắng đen! [laughter] Tại sao một loài vật đáng yêu lại đi tắm phân ngựa giữa mùa đông giá rét? Các nhà sinh vật học phát hiện trong phân ngựa tươi chứa nồng độ cao hai hợp chất hóa học gọi là BCP và BCPO!
```
**Part 3** → `audio/vs/scene04_p3.wav` (770 ký tự) · mood `don_dap`

```text
Khi thấm qua da, hai hợp chất này bám thẳng vào kênh cảm biến nhiệt lạnh Tê-rờ-pê-mờ tám trên tế bào thần kinh, khóa chặt công tắc báo lạnh khiến não bộ mất cảm giác rét buốt! [surprise-oh] Nhờ lớp kem ủ phân ngựa chống rét tự nhiên này, Gấu Trúc bình thản bước qua tuyết giá mà không bị co ro! Một cách dùng dược liệu tự nhiên từ môi trường đỉnh cao nhất thế giới động vật! [laughter] Chưa hết, năm hai ngàn hai mươi mốt, nghiên cứu trên Scientific Reports còn giải mã thêm: bộ lông trắng đen nổi tiếng của Gấu Trúc thực chất là áo tàng hình hoàn hảo trong rừng núi! Phần lông đen hòa vào bóng râm sâu thẳm và gốc cây ẩm ướt, còn phần lông trắng hòa lẫn vào mảng tuyết và tán lá sáng! Nhờ đó mắt của báo hoa mai và chó sói hoàn toàn không nhận ra đường viền cơ thể gấu!
```
**Part 4** → `audio/vs/scene04_p4.wav` (790 ký tự) · mood `hao_hung`

```text
Bây giờ chúng ta chuyển sang nửa sân sa mạc nắng cháy với sự góp mặt của Thằn Lằn Quỷ Gai! Ở Tập mười chín, khán giả đã biết nó uống nước bằng bàn chân qua rãnh mao dẫn. Nhưng nghiên cứu mới năm hai ngàn mười sáu còn tiết lộ chi tiết sâu hơn nữa! Tiến sĩ Philipp Comanns từ Đại học RWTH Aachen Đức đã cân đo từng mi-li-gam nước trong một giờ uống nước của chú thằn lằn chỉ nặng bốn mươi gam này! Trong một giờ ngâm chân vào vũng nước nhỏ, chú Quỷ Gai đóng mở hàm nhấp nháy gần hai ngàn năm trăm lần, mỗi ngụm hút vào miệng chỉ nhỏ đúng không phẩy bảy mi-crô-lít, nhưng tổng lượng nước uống được đạt một phẩy hai mươi tám gam! Đồng thời, mạng lưới rãnh trên bề mặt da của nó còn giữ trữ lại được thêm một phẩy ba mươi hai gam nước nữa giống như một chiếc bình giữ ẩm di động đeo quanh người!
```
**Part 5** → `audio/vs/scene04_p5.wav` (402 ký tự) · mood `tram_bi_an`

```text
Và đây là cú bẻ lái quan trọng của khoa học: thực tế sương đọng buổi sáng trên sa mạc không đủ để làm đầy các rãnh mao dẫn này! Vậy làm sao nó gom đủ nước giữa cát khô? Các nhà khoa học quan sát thấy một hành động siêu thông minh: nó dùng chân trước hất tung cát ẩm lên phủ kín lưng mình, sau đó ép chặt bụng xuống cát để các rãnh mao dẫn hút sạch từng giọt hơi ẩm từ lớp cát phủ hai mặt! [surprise-wa]
```
**Part 6** → `audio/vs/scene04_p6.wav` (1022 ký tự) · mood `am_ap`

```text
Tuyển thủ thứ ba bước vào thử thách sinh tồn khắc nghiệt của Vòng ba là Con Lười! Sống cả đời treo ngược trên ngọn cây rừng mưa nhiệt đới, cơ thể Con Lười làm sao để không bị... nghẹt thở bởi chính sức nặng của ruột gan mình? Ở hầu hết các loài động vật có vú, nếu bạn treo ngược đầu quá lâu, toàn bộ trọng lượng của gan, dạ dày đầy thức ăn sẽ đè bẹp xuống cơ hoành và hai lá phổi khiến việc hít thở trở nên cực kỳ mệt nhọc! Nhưng năm hai ngàn mười bốn, nghiên cứu của Rebecca Cliffe công bố trên tạp chí Biology Letters đã khám phá ra một cấu trúc giải phẫu độc quyền của Con Lười: các dây chằng xơ neo nội tạng! Những sợi dây chằng xơ đặc biệt này đóng vai trò như hệ thống dây cáp treo cầu giữ chặt gan và dạ dày cố định vào khung xương sườn, ngăn tuyệt đối không cho chúng đè lên phổi khi Con Lười treo ngược! Nhờ hệ thống dây cáp treo nội tạng này, Con Lười tiết kiệm được tới mười ba phần trăm năng lượng hô hấp mỗi khi treo ngược, giúp nó sống thong dong với chế độ ăn lá cây ít calo suốt cả cuộc đời! [surprise-oh]
```
**Part 7** → `audio/vs/scene04_p7.wav` (597 ký tự) · mood `nghiem_trang_gia`

```text
Và trong nửa sân nắng nóng thiêu đốt, cỗ xe tăng ba tấn Hà Mã cũng bước vào kiểm tra khả năng chống tia cực tím dưới ánh nắng gay gắt! Theo nghiên cứu hóa sinh nổi tiếng trên tạp chí Nature năm hai ngàn lẻ bốn của giáo sư Yoko Saikawa, chất lỏng chống nắng trên da Hà Mã lúc mới tiết ra hoàn toàn... trong suốt không màu! Chỉ sau vài phút tiếp xúc với không khí, hai sắc tố axit hipposudoric và norhipposudoric tự động phản ứng biến dịch tiết thành màu đỏ tươi rực rỡ, rồi chuyển sang màu nâu sẫm bám chặt nhiều giờ liền để hấp thụ trọn dải tia UV từ hai trăm đến sáu trăm na-nô-mét! [surprise-oh]
```
**Part 8** → `audio/vs/scene04_p8.wav` (332 ký tự) · 🎭 cameo `tham_phan`

```text
Kết quả Vòng ba cực kỳ xứng đáng! Huy chương đồng thuộc về Con Lười với hệ thống dây chằng treo nội tạng tiết kiệm mười ba phần trăm năng lượng thở! Huy chương bạc thuộc về Thằn Lằn Quỷ Gai với kỹ thuật hắt cát ẩm thu gom nước qua rãnh da! Và Huy chương vàng thuộc về Gấu Trúc Lớn với bí kíp tắm phân ngựa chống rét độc nhất vô nhị!
```
**Part 9** → `audio/vs/scene04_p9.wav` (357 ký tự) · mood `hao_hung`

```text
Bảng tổng sắp sau Vòng ba chứng kiến màn bứt phá ngoạn mục: Gấu Trúc Lớn vươn lên dẫn đầu với bốn điểm! Tôm Súng ba điểm! Cá Cung Thủ ba điểm! Thằn Lằn Quỷ Gai, Lươn Điện và Bọ Pháo Thủ đồng hai điểm! Con Lười và Tu Hú ghi một điểm! Bây giờ, đấu trường tạm nghỉ giải lao giữa hiệp để MC đột kích phòng thay đồ xem các đấu sĩ đang làm gì phía sau hậu trường!
```

### scene05 — PHỎNG VẤN HẬU TRƯỜNG VÀ NHỮNG PHA KHÓ ĐỠ
*Thẻ chương:* HẬU TRƯỜNG BẤT ỔN MÙA 2

*Badge:* `NGHỈ GIỮA HIỆP` · *mood mặc định:* `bi_hai`

**Part 0** → `audio/vs/scene05_p0.wav` (399 ký tự) · mood `hao_hung`

```text
[surprise-oh] Xin chào toàn thể khán giả! Chúng ta đang có mặt trực tiếp tại khu vực phòng thay đồ của Đại Hội Sinh Tồn Mùa hai! Trong lúc ban tổ chức chuẩn bị sân khấu cho hiệp hai, hãy xem các đấu sĩ đang làm gì phía sau hậu trường! Vừa mới giành huy chương vàng Vòng ba, ngôi sao đang dẫn đầu bảng tổng sắp là Gấu Trúc Lớn! Nhưng khoan... cái mùi gì nồng nặc bốc ra từ phòng số mười một thế này?!
```
**Part 1** → `audio/vs/scene05_p1.wav` (160 ký tự) · mood `bi_hai`

```text
Trời đất ơi! Gấu Trúc Lớn vừa mang nguyên một xô... phân ngựa tươi từ vùng núi Tứ Xuyên vào phòng nghỉ để bôi lên mặt giữ ấm giữa máy lạnh phòng chờ! [laughter]
```
**Part 2** → `audio/vs/scene05_p2.wav` (129 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Anh MC vào làm một miếng cho ấm người nè! Ở phòng chờ mở điều hòa hai mươi độ lạnh muốn đóng băng, bôi cái này vào ấm cực luôn á!
```
**Part 3** → `audio/vs/scene05_p3.wav` (321 ký tự) · mood `hao_hung`

```text
Thôi thôi cảm ơn em, anh MC xin phép từ chối vì anh mặc vest đỏ đi dẫn chương trình chứ không phải đi leo núi tuyết! [laughter] Chúc mừng em giữ vững phong độ nhé! Điểm dừng chân tiếp theo là khu vực hồ bơi thư giãn của Bố Già Capybara! Hãy xem vị Bộ trưởng Ngoại giao đang nghỉ ngơi kiểu gì sau ba vòng chưa có điểm nào!
```
**Part 4** → `audio/vs/scene05_p4.wav` (150 ký tự) · mood `tram_bi_an`

```text
Ủa? Bố Già Capybara trốn đi đâu mất tiêu rồi? Trong bồn nước chẳng thấy ai ngoài mấy ngọn rong bèo lững lờ trôi... Khoan đã, nhìn kỹ mặt nước kia kìa!
```
**Part 5** → `audio/vs/scene05_p5.wav` (426 ký tự) · mood `am_ap`

```text
[surprise-oh] Hóa ra vị trí mắt, tai và hai lỗ mũi của Capybara nằm xếp thẳng hàng trên đỉnh đầu giống hệt cấu tạo của Hà Mã! Nó đang ngủ say giấc nồng ngay dưới lòng hồ chỉ để hở đúng mắt mũi tai lên mặt nước! Một tư thế ngủ vừa giữ mát làn da, vừa dễ dàng thở không khí và quan sát động tĩnh xung quanh mà không kẻ thù nào phát hiện được! Chào Bố Già! Nằm ngâm nước thế này thì chút nữa thi Vòng bốn có bị lạnh bụng không ạ?
```
**Part 6** → `audio/vs/scene05_p6.wav` (121 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Khò... khò... Nước ấm thế này ngủ sướng lắm anh bạn... Để tôi ngủ thêm mười phút nữa rồi ra cân hết Vòng bốn cho anh xem!
```
**Part 7** → `audio/vs/scene05_p7.wav` (287 ký tự) · mood `hao_hung`

```text
Thần thái của người đàn ông chưa có điểm nào mà vẫn ngủ ngon lành như đang nắm chắc chiếc cúp vô địch trong tay! Bây giờ chúng ta ghé thăm phòng của Chim Tu Hú! Chào Chim Tu Hú! Sao trong phòng nghỉ mà bạn lại chuẩn bị hành lý bay đi đâu thế này? Chúng ta vẫn còn năm vòng thi nữa cơ mà!
```
**Part 8** → `audio/vs/scene05_p8.wav` (219 ký tự) · mood `don_dap`

```text
Anh MC không biết rồi! Sau giải đấu này, tôi phải bay ngay chuyến bay đường dài mười sáu ngàn cây số từ châu Âu sang tận Trung Phi để tránh rét mùa đông đấy! Tôi chỉ tranh thủ ghé đây kiếm ít huy chương thôi! [laughter]
```
**Part 9** → `audio/vs/scene05_p9.wav` (171 ký tự) · mood `hao_hung`

```text
Chà, đúng là phi công hạng nặng! Và căn phòng cuối cùng trong giờ giải lao là phòng của cô nàng Con Lười! Không biết bạn ấy đã tiêu hóa xong chiếc lá từ hồi khai mạc chưa?
```
**Part 10** → `audio/vs/scene05_p10.wav` (285 ký tự) · mood `bi_hai`

```text
Ban tổ chức trang bị một chiếc đồng hồ bấm giờ treo ngay cạnh mặt Con Lười! MC đặt một câu hỏi ngắn: bạn cảm thấy đấu trường Mùa hai thế nào? Con Lười nhướng mày... mở hé miệng... mất năm giây để hít hơi... mất mười giây để cong môi... và mất cả một phút mới phát âm được chữ đầu tiên!
```
**Part 11** → `audio/vs/scene05_p11.wav` (82 ký tự) · 🎭 cameo `be_con`

```text
Tôi... cảm... thấy... đại... hội... năm... nay... rất... là... vui... luôn... ạ...
```
**Part 12** → `audio/vs/scene05_p12.wav` (503 ký tự) · mood `hao_hung`

```text
Chưa hết đâu quý vị! Ghé ngang phòng số mười sáu của Tôm Súng, chúng ta bắt gặp chú tôm đang ngồi đánh bóng khẩu đại bác cùng người bạn thân thiết là một chú cá bống mắt lồi! Chú cá bống làm nhiệm vụ canh cửa bảo vệ còn Tôm Súng dùng càng đào cát làm phòng ở chung sang trọng! Một cặp đôi bạn thân gắn bó keo sơn nhất thế giới biển cả! Còn trong phòng bên cạnh, nhà máy điện Lươn Điện đang vừa bơi lội thư giãn vừa thưởng thức bữa ăn nhẹ bằng thịt cá nhỏ để nạp đầy năng lượng cho bộ bơm ion Natri Kali!
```
**Part 13** → `audio/vs/scene05_p13.wav` (487 ký tự) · mood `hao_hung`

```text
Còn tại góc phòng sa mạc nhân tạo, Thằn Lằn Quỷ Gai đang tận hưởng bồn tắm cát ẩm mát rượi, chuẩn bị tinh thần đối đầu với gã khổng lồ Hà Mã ở vòng bốn! Bước sang phòng số hai mươi của Cá Cung Thủ, chúng ta bắt gặp chú cá đang nhìn chằm chằm vào một cuốn an-bum ảnh chân dung dán đầy mặt các thành viên ban tổ chức! Chú cá đang luyện tập ghi nhớ từng nếp nhăn trên khuôn mặt của giám khảo để phòng trường hợp giám khảo chấm điểm thiếu công bằng là... phun nước thẳng vào kính! [laughter]
```
**Part 14** → `audio/vs/scene05_p14.wav` (365 ký tự) · mood `bi_hai`

```text
Sang tới phòng số mười tám của Bọ Pháo Thủ, ban tổ chức thấy một cái bàn đầy ắp các loại lá cây và xác côn trùng giàu dưỡng chất giúp chú bọ nạp lại kho nguyên liệu hóa học! Còn trong bồn tắm bùn khổng lồ ở cuối hành lang, gã khổng lồ Hà Mã đang ngâm mình thư giãn, làn da tiết ra lớp dịch nhờn trong suốt dần chuyển màu đỏ hồng lấp lánh dưới ánh đèn phòng thay đồ!
```
**Part 15** → `audio/vs/scene05_p15.wav` (128 ký tự) · 🎭 cameo `ga_khong_lo`

```text
Này anh MC, chút nữa thi vòng dinh dưỡng nhớ chuẩn bị thật nhiều cỏ non nhé, chứ tôi đang đói cồn cào cả ba ngăn dạ dày rồi đấy!
```
**Part 16** → `audio/vs/scene05_p16.wav` (77 ký tự) · mood `hao_hung`

```text
Vâng vâng, ban tổ chức đã chuẩn bị sẵn cả một xe tải cỏ tươi ngoài sân rồi ạ!
```
**Part 17** → `audio/vs/scene05_p17.wav` (567 ký tự) · mood `hao_hung`

```text
Trên đường quay lại sân chính, MC còn bắt gặp Gấu Trúc Lớn đang tập động tác trồng cây chuối khởi động cơ tay trước khi bước vào vòng thi tiêu hóa! Còn anh chàng Cá Cung Thủ và Tôm Súng thì đang thi xem ai bắn trúng bia nhanh hơn ở hành lang làm ướt sũng cả chiếc áo vest đỏ của MC! [laughter] Giờ nghỉ giải lao đầy ắp tiếng cười đã kết thúc! Chuông báo động hiệp hai vang lên dồn dập đưa toàn thể đấu sĩ quay trở lại sàn đấu chính! Vòng bốn ngay sau đây sẽ giải mã những bí mật động trời về dinh dưỡng và sức ảnh hưởng sinh thái của các đấu sĩ! Hãy sẵn sàng đón xem!
```

### scene06 — DINH DƯỠNG DỊ THƯỜNG VÀ VAI TRÒ BƠM KHOÁNG CHẤT SINH THÁI
*Thẻ chương:* BƠM SILICON VÀ RĂNG MÀI VĨNH CỬU

*Badge:* `VÒNG 4` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene06_p0.wav` (569 ký tự) · mood `hao_hung`

```text
Chào mừng toàn thể quý vị trở lại với hiệp hai của Đại Hội Sinh Tồn Mùa hai: Vòng bốn — Dinh dưỡng dị thường và chuỗi cung ứng sinh thái! Ở vòng thi này, ban giám khảo không chỉ nhìn vào việc con vật ăn cái gì, mà còn đánh giá xem hệ tiêu hóa của nó mang lại tác động kinh thiên động địa nào cho thiên nhiên xung quanh! Thí sinh đầu tiên bước vào vòng cân đo sinh thái là cỗ xe tăng ba tấn châu Phi: Hà Mã! Khán giả đều biết Hà Mã thích quạt đuôi văng phân đánh dấu lãnh thổ, nhưng nghiên cứu năm hai ngàn mười chín đã phát hiện một bí mật vĩ đại ẩn trong đống phân đó!
```
**Part 1** → `audio/vs/scene06_p1.wav` (362 ký tự) · mood `tram_bi_an`

```text
Năm hai ngàn mười chín, nhà sinh thái học Jonas Schoelynck tại Đại học Antwerp Bỉ công bố một nghiên cứu chấn động trên tạp chí uy tín Science Advances! Vào ban đêm, mỗi con Hà Mã rời mặt nước lên đồng cỏ gặm hàng chục ký cỏ giàu chất khoáng Silicon thực vật. Đến ban ngày, chúng quay về ngâm mình dưới sông và bài tiết toàn bộ số khoáng chất đó xuống dòng nước!
```
**Part 2** → `audio/vs/scene06_p2.wav` (917 ký tự) · mood `don_dap`

```text
Các nhà khoa học đo được con số kinh hoàng: đàn Hà Mã dọc theo sông Mara ở Kenya bơm trực tiếp khoảng không phẩy bốn tấn nguyên tố Silicon nguyên chất xuống lòng sông mỗi ngày! Số Silicon do Hà Mã vận chuyển chiếm tới bảy mươi sáu phần trăm tổng lượng dòng chảy Silicon của toàn bộ con sông lớn! Không có Hà Mã, con sông gần như mất đi ba phần tư nguồn cung Silicon tự nhiên! [surprise-oh] Tại sao Silicon lại quan trọng đến thế? Bởi vì nó là vật liệu thiết yếu để loài tảo khuê cực nhỏ dưới hồ Victoria xây dựng lớp vỏ thủy tinh và quang hợp tạo oxy nuôi sống hàng triệu con cá thương phẩm! Chưa hết, dù trông giống lợn, Hà Mã thực chất tiến hóa một chiếc dạ dày ba ngăn lên men vi sinh cực kỳ phức tạp gọi là hệ tiêu hóa giả nhai lại! Nhờ hệ thống lên men ba ngăn tiết kiệm năng lượng này, một cỗ xe tăng nặng ba tấn chỉ cần ăn lượng cỏ bằng khoảng một phẩy năm phần trăm trọng lượng cơ thể mỗi ngày là đủ sinh tồn!
```
**Part 3** → `audio/vs/scene06_p3.wav` (585 ký tự) · mood `tram_bi_an`

```text
Và nhân tiện nhắc tới đường ruột kỳ lạ trong vòng dinh dưỡng này, khoa học năm hai ngàn mười lăm còn phát hiện thêm một sự thật sốc nữa về hệ vi sinh vật trong bụng Gấu Trúc Lớn! Theo nghiên cứu công bố trên tạp chí mBio khi phân tích hàng loạt mẫu phân của Gấu Trúc qua các mùa, đường ruột của chúng vẫn... không hề tiến hóa ra nhóm vi khuẩn tiêu hóa xen-lu-lô như loài bò hay cừu! Tức là suốt hai triệu năm chuyển sang ăn chay, ngay cả đội quân vi khuẩn trong bụng Gấu Trúc vẫn giữ nguyên cấu trúc của thú ăn thịt! Một màn bảo thủ di truyền cứng đầu nhất lịch sử tiến hóa! [laughter]
```
**Part 4** → `audio/vs/scene06_p4.wav` (207 ký tự) · mood `am_ap`

```text
Còn chú Con Lười thì sao? Bên cạnh tốc độ tiêu hóa siêu chậm, Con Lười còn điều chỉnh thân nhiệt biến thiên linh hoạt từ hai mươi bốn độ C vào ban đêm lên ba mươi ba độ C lúc phơi nắng giống như loài bò sát!
```
**Part 5** → `audio/vs/scene06_p5.wav` (133 ký tự) · 🎭 cameo `tham_phan`

```text
Giám khảo kinh ngạc: phân của Hà Mã hóa ra lại là nguồn phân bón khoáng chất vàng nuôi sống cả một hệ sinh thái hồ khổng lồ châu Phi!
```
**Part 6** → `audio/vs/scene06_p6.wav` (184 ký tự) · mood `hao_hung`

```text
Tuyển thủ thứ hai bước lên sàn đo dinh dưỡng là Bố Già đầm lầy: Capybara! Ngoài tập tính ăn lại phân mềm buổi sáng đã nổi tiếng, Bố Già còn có một bí mật về bộ răng cửa đáng kinh ngạc!
```
**Part 7** → `audio/vs/scene06_p7.wav` (661 ký tự) · mood `don_dap`

```text
Giống như họ hàng nhà hải ly và sóc, cặp răng cửa hình chiếc đục sắc bén ở hàm trước của Capybara... mọc dài ra không bao giờ ngừng suốt cả cuộc đời! Nếu một chú Capybara lười biếng không chịu nhai, cặp răng cửa sẽ mọc dài đâm xuyên qua cả hàm làm nó không thể đóng miệng lại được! Để giữ cho hàm răng luôn ngắn gọn và sắc bén, mỗi ngày Bố Già phải tiêu thụ đều đặn từ ba đến bốn ki-lô-gam cỏ xơ cứng chứa đầy tinh thể cát và gặm cả vỏ cây gỗ cứng để mài mòn men răng tự nhiên! Đồng thời, men răng của nó có cấu trúc tự mài sắc: mặt ngoài cứng hơn mặt trong, khiến càng nhai đồ cứng thì lưỡi răng lại càng trở nên bén ngọt hơn như dao gọt hoa quả! [surprise-wa]
```
**Part 8** → `audio/vs/scene06_p8.wav` (808 ký tự) · mood `hao_hung`

```text
Và tuyển thủ thứ ba mang đến bài thi dinh dưỡng cực kỳ dị biệt: Thằn Lằn Quỷ Gai! Ở Tập mười chín chúng ta đã biết thực đơn độc nhất của nó là kiến đen, nhưng chiến thuật bẫy kiến của nó mới thực sự là bậc thầy kiên nhẫn! Nghiên cứu sinh thái học tại Tây Úc cho thấy Thằn Lằn Quỷ Gai không bao giờ đuổi theo đàn kiến tốn sức! Nó chọn ngồi lì đúng tại ngã tư đường mòn giao nhau vào lúc sáng sớm hoặc chiều mát khi đàn kiến đi kiếm ăn đông nhất! Mỗi cú phóng lưỡi dính diễn ra trong chớp mắt, tiêu thụ hàng ngàn con kiến chứa axit formic nhưng lại giữ cho độ pH dạ dày cân bằng hoàn hảo nhờ dịch đệm kiềm tính đặc biệt! Đặc biệt, chiếc gù mỡ sau cổ và phần đuôi mập của nó đóng vai trò như một kho pin thực phẩm dự trữ, giúp nó nhịn ăn hoàn toàn suốt mùa đông khắc nghiệt khi đàn kiến chui sâu xuống lòng đất!
```
**Part 9** → `audio/vs/scene06_p9.wav` (517 ký tự) · mood `hao_hung`

```text
Chưa dừng lại ở đó, ban giám khảo còn chấm thêm điểm cộng cho khả năng giữ gìn và sử dụng răng hàm của Gấu Trúc Lớn! Khác với răng nhọn xé thịt của hổ hay sư tử, răng hàm của Gấu Trúc đã tiến hóa to gấp bảy lần bình thường với lớp men răng cực dày có khả năng tự phục hồi các vết nứt siêu nhỏ khi nhai tre cứng suốt mười bốn tiếng mỗi ngày! Còn gã khổng lồ Hà Mã nhờ có dạ dày ba ngăn lên men hiệu quả mà có thể ung dung dành tới mười sáu tiếng mỗi ngày ngâm mình nghỉ ngơi dưới sông mà chẳng cần ăn suốt cả ban ngày!
```
**Part 10** → `audio/vs/scene06_p10.wav` (326 ký tự) · 🎭 cameo `tham_phan`

```text
Ban giám khảo công bố kết quả Vòng bốn! Huy chương đồng thuộc về Thằn Lằn Quỷ Gai với chiến thuật phục kích ngã tư và kho mỡ đuôi dự trữ năng lượng! Huy chương bạc thuộc về Capybara với cặp răng cửa tự mài sắc mọc vĩnh cửu! Và Huy chương vàng thuộc về Hà Mã với công trạng bơm bốn trăm ký Silicon mỗi ngày nuôi sống dòng sông!
```
**Part 11** → `audio/vs/scene06_p11.wav` (339 ký tự) · mood `hao_hung`

```text
Bảng tổng sắp cập nhật điểm số mới nhất: Gấu Trúc dẫn đầu bốn điểm! Tôm Súng ba điểm! Cá Cung Thủ, Thằn Lằn Quỷ Gai và Hà Mã cùng chạm mốc ba điểm! Lươn Điện, Bọ Pháo Thủ, Capybara đồng hai điểm! Tu Hú và Con Lười một điểm! Vòng năm ngay sau đây sẽ lật mở những xã hội bí mật và sức mạnh bầy đàn gây sốc nhất thế giới động vật! Đừng bỏ lỡ!
```

### scene07 — SỨC MẠNH BẦY ĐÀN VÀ NHỮNG XÃ HỘI BÍ MẬT CHƯA TỪNG BIẾT
*Thẻ chương:* TÔM CHÚA VÀ BẦY LƯƠN SĂN MỒI

*Badge:* `VÒNG 5` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene07_p0.wav` (596 ký tự) · mood `hao_hung`

```text
Chào mừng toàn thể khán đài bước vào Vòng năm: Sức mạnh bầy đàn và những xã hội bí mật! Lâu nay chúng ta thường nghĩ những sát thủ mang vũ khí hạng nặng đều thích hành động đơn độc như sói hoang. Nhưng trong thế giới khoa học hiện đại, những phát hiện mới nhất đã lật nhào hoàn toàn định kiến đó! Hãy chuẩn bị tinh thần chứng kiến màn lột xác của ba tuyển thủ đêm nay! Ứng cử viên đầu tiên bước lên bục là pháo thủ đại dương: Tôm Súng! Ai cũng biết nó sống cộng sinh với cá bống gác hang, nhưng ít ai biết một nhánh họ hàng của Tôm Súng lại thiết lập hẳn một... vương quốc ong kiến dưới đáy biển!
```
**Part 1** → `audio/vs/scene07_p1.wav` (441 ký tự) · mood `tram_bi_an`

```text
Năm một ngàn chín trăm chín mươi sáu, nhà sinh vật học biển Emmett Duffy công bố một phát hiện làm chấn động giới động vật học trên tạp chí Nature danh tiếng! Cho đến trước năm một ngàn chín trăm chín mươi sáu, khái niệm xã hội bậc cao eusociality — tức là có một con chúa duy nhất đẻ trứng, còn hàng trăm con khác hy sinh quyền sinh sản để đi làm lính bảo vệ tổ — chỉ được tìm thấy ở côn trùng như ong, kiến, mối và chuột dũi trần trên cạn!
```
**Part 2** → `audio/vs/scene07_p2.wav` (715 ký tự) · mood `don_dap`

```text
Và loài tôm súng Synalpheus regalis chính là loài sinh vật biển đầu tiên trên hành tinh được xác nhận sở hữu cấu trúc xã hội bậc cao eusociality giống hệt như kiến và ong! [surprise-oh] Trong một tổ bọt biển chứa hơn ba trăm thành viên đó, chỉ có duy nhất một Tôm Chúa cái khổng lồ làm nhiệm vụ sinh sản! Toàn bộ hàng trăm con tôm lính còn lại — vốn là anh chị em ruột thịt của nhau — hoàn toàn không bao giờ sinh sản! Chúng sở hữu chiếc càng súng lớn hơn hẳn để làm lính gác bảo vệ các lối vào tổ bọt biển trước kẻ thù xâm lược! Khi có cua hoặc cá lạ mon men tới gần, cả đội quân tôm lính đồng loạt búng càng tạo thành dàn pháo thanh âm đẩy lùi kẻ thù bảo vệ Tôm Chúa và đàn em nhỏ an toàn tuyệt đối! [surprise-wa]
```
**Part 3** → `audio/vs/scene07_p3.wav` (443 ký tự) · mood `hao_hung`

```text
Một đế chế quân sự thu nhỏ có nữ hoàng và binh lính ngay trong lòng đại dương! Một phát hiện thay đổi cả sách giáo khoa sinh học biển! Tiếp theo là một cú sốc thứ hai đến từ rừng rậm Amazon, làm đảo lộn hàng trăm năm hiểu biết của loài người về tuyển thủ Lươn Điện! Suốt hơn hai thế kỷ kể từ thời nhà thám hiểm Alexander von Humboldt, cả thế giới khoa học đều khẳng định Lươn Điện là loài sát thủ cô độc tuyệt đối, đi săn một mình vào ban đêm!
```
**Part 4** → `audio/vs/scene07_p4.wav` (960 ký tự) · mood `don_dap`

```text
Cho đến tháng giêng năm hai ngàn hai mươi mốt, nhóm nghiên cứu của giáo sư Douglas Bastos và tiến sĩ David de Santana công bố phát hiện kinh hoàng trên tạp chí Ecology and Evolution! Họ phát hiện một bầy đàn khổng lồ gồm hơn một trăm con Lươn Điện trưởng thành — dài từ một mét hai đến một mét tám — đang tụ họp và phối hợp săn mồi tập thể giống hệt như bầy sói hay đàn cá voi sát thủ! [surprise-oh] Mỗi khi bình minh và hoàng hôn buông xuống, hơn một trăm con lươn này cùng bơi vòng tròn lùa hàng ngàn con cá nhỏ dồn chặt lại thành một quả cầu mồi khổng lồ sát bờ nước nông! Sau đó, từng tốp từ hai đến mười con Lươn Điện tách đội hình áp sát quả cầu mồi, và cùng lúc phát động một loạt xung điện đồng loạt với tổng điện áp cộng hưởng cực đại! Cú phóng điện tập thể mạnh đến nỗi khiến hàng trăm con cá nhỏ bị giật văng bắn tung lên không trung rồi rơi xuống mặt nước bất tỉnh nhân sự, trở thành bữa tiệc thịnh soạn cho cả trăm thành viên trong bầy! [laughter]
```
**Part 5** → `audio/vs/scene07_p5.wav` (812 ký tự) · mood `am_ap`

```text
Tuyển thủ thứ ba bước vào vòng đấu xã hội không dùng đến vũ khí giật điện hay búng càng, mà chinh phục khán đài bằng tình mẫu tử vĩ đại của đại gia đình: Capybara! Nghiên cứu về hành vi nuôi con hộ alloparenting do các nhà khoa học Brazil thực hiện đã hé lộ một nét văn hóa cộng đồng cực kỳ nhân văn của Bố Già đầm lầy! Trong một bầy Capybara, tất cả các con cái thường là chị em họ hàng gần gũi. Khi sinh con vào cùng thời điểm, các bà mẹ sẵn sàng cho bất kỳ đứa trẻ nào trong đàn đến bú sữa mà hoàn toàn không phân biệt đâu là con ruột của mình, đâu là con của hàng xóm! Thậm chí ngay từ khi mới sinh ra vài ngày tuổi, chuột con đã mở mắt, mọc đủ lông, biết đi lại và bơi lội theo cả đại gia đình, được tất cả các bác các chú trong bầy cùng đứng gác sủa báo động bảo vệ trước báo đốm và trăn gấm! [surprise-oh]
```
**Part 6** → `audio/vs/scene07_p6.wav` (565 ký tự) · mood `tram_bi_an`

```text
Không chịu thua trước các xã hội đoàn kết của Tôm Súng, Lươn Điện hay Capybara, Chim Tu Hú bước lên bục để trình diễn cuộc chạy đua vũ trang tâm lý căng thẳng với chính các chim chủ nhà! Các nhà điểu học phát hiện rằng: một số loài chim chủ thông minh đã tiến hóa khả năng nhận diện hoa văn trứng lạ tinh tường đến mức tự mình kiểm tra từng quả trứng trong tổ! Vì thế, Chim Tu Hú mẹ phải phát triển bộ nhớ không gian siêu việt để ghi nhớ vị trí và lịch đẻ trứng của hàng chục tổ chim hàng xóm cùng lúc, căn đúng khung giờ chiều vắng mặt để đánh tráo trứng hoàn hảo!
```
**Part 7** → `audio/vs/scene07_p7.wav` (313 ký tự) · 🎭 cameo `tham_phan`

```text
Ban giám khảo xin công bố kết quả Vòng năm! Huy chương đồng thuộc về Capybara với văn hóa nuôi con tập thể không phân biệt vô cùng nhân văn! Huy chương bạc thuộc về Lươn Điện với chiến thuật săn mồi bầy đàn hơn một trăm con! Và Huy chương vàng thuộc về Tôm Súng với xã hội ong kiến ba trăm tôm lính dưới đáy biển!
```
**Part 8** → `audio/vs/scene07_p8.wav` (354 ký tự) · mood `hao_hung`

```text
Bảng tổng sắp sau Vòng năm thay đổi vị trí dẫn đầu: Tôm Súng vọt lên ngôi đầu với sáu điểm! Lươn Điện và Gấu Trúc Lớn bám sát phía sau với bốn điểm! Cá Cung Thủ, Quỷ Gai, Hà Mã và Capybara đồng ba điểm! Vòng sáu ngay sau đây sẽ đưa chúng ta bay qua nửa vòng Trái Đất và lặn xuống đáy sông châu Phi trong thử thách Hành trình vĩ đại và định vị không gian!
```

### scene08 — HÀNH TRÌNH VĨ ĐẠI VÀ SIÊU GIÁC QUAN ĐỊNH VỊ KHÔNG GIAN
*Thẻ chương:* BAY 16000KM VÀ NGHE BẰNG XƯƠNG HÀM

*Badge:* `VÒNG 6` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene08_p0.wav` (612 ký tự) · mood `hao_hung`

```text
Chào mừng toàn thể khán đài bước vào Vòng sáu: Hành trình vĩ đại và siêu giác quan định vị không gian! Ở vòng thi này, ban giám khảo sẽ kiểm tra khả năng vượt không gian và cách các tuyển thủ giao tiếp bằng những giác quan mà con người không hề có! Từ bầu trời Bắc Âu băng giá cho tới lòng sông đục ngầu châu Phi, đấu sĩ nào xứng đáng nhận danh hiệu bậc thầy định vị tối thượng? Tuyển thủ mở màn vòng thi di chuyển khiến tất cả mọi người phải ngước nhìn lên bầu trời: Siêu Trộm Tổ Ấm Chim Tu Hú! Khán giả quen thấy nó loanh quanh bên tổ chim chích, nhưng khả năng bay đường dài của nó mới thực sự là huyền thoại!
```
**Part 1** → `audio/vs/scene08_p1.wav` (371 ký tự) · mood `tram_bi_an`

```text
Năm hai ngàn mười bốn, nhóm nghiên cứu của nhà điểu học Mikkel Willemoes công bố trên tạp chí PLOS ONE kết quả theo dõi vệ tinh đột phá nhất từng thực hiện trên loài Chim Tu Hú! Thông thường, những loài chim di cư đi đơn độc ban đêm như Tu Hú được cho là bay tản mát theo hướng ngẫu nhiên. Nhưng dữ liệu vệ tinh từ Đan Mạch và Thụy Điển đã cho thấy một sự thật kinh ngạc!
```
**Part 2** → `audio/vs/scene08_p2.wav` (654 ký tự) · mood `don_dap`

```text
Mỗi năm, một chú Chim Tu Hú nhỏ bé nặng khoảng một trăm gam tự mình bay đơn độc vào ban đêm một hành trình khép kín theo chiều kim đồng hồ dài tới mười sáu ngàn cây số! [surprise-oh] Điều khó tin hơn cả: sau khi vượt hơn năm ngàn cây số xuyên qua sa mạc Sahara chết chóc để tới vùng Sahel phía Đông, khoảng cách sai lệch giữa những con chim bay riêng lẻ này trung bình chỉ cách nhau đúng một trăm sáu mươi bốn cây số! Từ Bắc Âu xuống Đông Nam Âu, sang Trung Phi trú đông, rồi vòng qua Tây Phi bay ngược về châu Âu vào mùa xuân! Một hệ thống định vị GPS sinh học bẩm sinh với sáu trạm dừng chân cố định qua hàng triệu năm không sai một nhịp! [surprise-wa]
```
**Part 3** → `audio/vs/scene08_p3.wav` (372 ký tự) · mood `hao_hung`

```text
Rời khỏi bầu trời mười sáu ngàn cây số, chúng ta lặn sâu xuống lòng sông đục ngầu châu Phi để kiểm tra siêu giác quan dưới nước của cỗ xe tăng ba tấn: Hà Mã! Câu hỏi đặt ra cho ban giám khảo là: khi lặn hoàn toàn dưới nước tối tăm với đôi tai đã gập kín để ngăn nước vào, làm sao Hà Mã vẫn nghe được âm thanh và xác định chính xác hướng gọi của đồng loại từ dưới đáy sông?
```
**Part 4** → `audio/vs/scene08_p4.wav` (671 ký tự) · mood `don_dap`

```text
Nghiên cứu âm học dưới nước của tiến sĩ William Barklow đã giải mã khả năng thính giác lưỡng cư độc nhất vô nhị này: Hà Mã nghe âm thanh dưới nước bằng... xương hàm dưới! Khi âm thanh dưới nước truyền tới, rung động đập vào xương hàm dưới, truyền qua dải mô mỡ dẫn âm thẳng vào tai trong bên trái và bên phải, giúp Hà Mã xác định chính xác phương hướng âm thanh giống hệt như người anh em họ xa Cá Heo và Cá Voi! [surprise-oh] Đặc biệt hơn, Hà Mã còn phát ra các xung âm thanh lưỡng cư đồng thời vào cả không khí phía trên lẫn dòng nước phía dưới! Nhờ cơ chế truyền rung động qua hàm dưới, tiếng gọi bầy đàn trầm đục của nó vang xa hàng cây số xuyên thấu mọi lớp bùn đục!
```
**Part 5** → `audio/vs/scene08_p5.wav` (315 ký tự) · mood `hao_hung`

```text
Và tuyển thủ thứ ba bước vào bài thi định vị không gian sẽ mang lại cho quý vị một màn trình diễn vừa hài hước vừa khôn ngoan: Gấu Trúc Lớn! Vì sống cô độc giữa rừng tre rậm rạp mênh mông, Gấu Trúc giao tiếp với đồng loại qua những 'bảng tin mùi hương' tiết ra từ tuyến mùi dưới đuôi và nước tiểu quệt lên thân cây!
```
**Part 6** → `audio/vs/scene08_p6.wav` (745 ký tự) · mood `bi_hai`

```text
Nhưng ở đây có một quy luật cạnh tranh ngầm cực kỳ khốc liệt: vết mùi càng nằm ở vị trí cao trên thân cây thì chủ nhân của nó càng được coi là to lớn, khỏe mạnh và đáng gờm nhất! Vậy một chú Gấu Trúc đực lùn mũm mĩm phải làm sao? Nghiên cứu của tiến sĩ Ron Swaisgood tại vườn thú San Diego và khu bảo tồn Ngọa Long ghi nhận một pha xiếc thú không tưởng: Gấu Trúc đực chống hai tay trước xuống đất, lộn ngược người... trồng cây chuối đẩy hai chân sau bò ngược lên thân cây! [laughter] Ở tư thế trồng cây chuối thẳng đứng đó, chú gấu xịt nước tiểu và bôi mùi hương lên cao chót vót trên thân cây! Một chiêu 'khai gian chiều cao' cực kỳ thông minh khiến các tình địch trẻ tuổi đi ngang qua ngửi thấy liền khiếp sợ bỏ đi không dám gây sự! [laughter]
```
**Part 7** → `audio/vs/scene08_p7.wav` (530 ký tự) · mood `am_ap`

```text
Cũng trong bài thi di chuyển không gian, hãy nhìn qua đồng hồ đo quãng đường của hai tuyển thủ sống tại ranh giới nước và cây cối: Con Lười và Cá Cung Thủ! Trên những ngọn cây cao, trung bình mỗi ngày Con Lười chỉ di chuyển được vỏn vẹn khoảng ba mươi tám mét — tức là chưa bằng một nửa chiều dài sân bóng đá! Nhưng điều kỳ diệu là dù sống ở vùng cửa sông nơi độ mặn thay đổi chóng mặt theo thủy triều mỗi ngày, Cá Cung Thủ vẫn điều chỉnh được áp suất thẩm thấu trong máu một cách hoàn hảo để sống khỏe ở cả nước ngọt lẫn nước lợ!
```
**Part 8** → `audio/vs/scene08_p8.wav` (621 ký tự) · mood `don_dap`

```text
Và đừng quên khả năng tăng tốc tẩu thoát bất ngờ trên cạn của Bố Già Capybara khi phát hiện kẻ săn mồi nguy hiểm tiếp cận bất ngờ! Nhờ cấu tạo bốn ngón có màng ở hai chân trước và ba ngón có màng ở hai chân sau, Bố Già đầm lầy phóng mình lao thẳng xuống dòng sông sâu chỉ trong nháy mắt, đồng thời chuyển hẳn đồng hồ sinh học sang kiếm ăn hoàn toàn vào ban đêm khi khu vực có nhiều mối đe dọa rình rập! Còn anh chàng Tôm Súng dưới rạn san hô lại có một chiến thuật giữ liên lạc đặc biệt: mỗi khi bầy tôm lính búng càng đồng loạt, sóng âm thanh vang xa hàng trăm mét dưới đáy biển để cảnh báo lãnh thổ cho các rạn lân cận!
```
**Part 9** → `audio/vs/scene08_p9.wav` (307 ký tự) · 🎭 cameo `tham_phan`

```text
Kết quả Vòng sáu tuyệt vời đã có! Huy chương đồng thuộc về Gấu Trúc Lớn với tuyệt chiêu trồng cây chuối đánh dấu lãnh thổ lừa tình địch! Huy chương bạc thuộc về Hà Mã với công nghệ nghe âm thanh dưới nước qua xương hàm dưới! Và Huy chương vàng thuộc về Chim Tu Hú với đường bay vệ tinh mười sáu ngàn cây số!
```
**Part 10** → `audio/vs/scene08_p10.wav` (417 ký tự) · mood `hao_hung`

```text
Bảng điểm sau Vòng sáu trở nên cực kỳ sít sao: Tôm Súng dẫn đầu với sáu điểm! Hà Mã và Gấu Trúc Lớn đồng hạng nhì với năm điểm! Lươn Điện và Chim Tu Hú bám sát với bốn điểm! Cá Cung Thủ, Quỷ Gai và Capybara đồng ba điểm! Bọ Pháo Thủ hai điểm và Con Lười một điểm! Bây giờ, trước khi bước vào ba chặng đua nước rút cuối cùng, mời toàn thể quý vị đến với Lễ Trao Giải Phụ: Di sản tiền sử và những họ hàng quái đản nhất!
```

### scene09 — CÁC CỤ TỔ KHỔNG LỒ 4 TẤN VÀ NHỮNG HỌ HÀNG DỊ BIỆT
*Thẻ chương:* LƯỜI KHỔNG LỒ VÀ BỌ KÝ SINH TỔ KIẾN

*Badge:* `GIẢI PHỤ` · *mood mặc định:* `bi_hai`

**Part 0** → `audio/vs/scene09_p0.wav` (476 ký tự) · mood `hao_hung`

```text
[surprise-oh] Chào mừng toàn thể quý vị khán giả đến với sự kiện đặc biệt giữa hiệp hai của Mùa hai: Bảo Tàng Di Sản Tiến Hóa và Lễ Trao Giải Phụ! Không tính vào điểm vô địch, nhưng lễ trao giải phụ đêm nay sẽ bật mí những bí mật chấn động về cụ tổ tiền sử và những người anh em họ hàng kỳ quái nhất của các tuyển thủ! Danh hiệu phụ đầu tiên — Giải thưởng 'Cụ Tổ Khổng Lồ Đáng Sợ Nhất Tiền Sử' — xin được xướng tên họ hàng cổ đại của chú Con Lười bé nhỏ đang ngồi ngủ gật kia!
```
**Part 1** → `audio/vs/scene09_p1.wav` (911 ký tự) · mood `tram_bi_an`

```text
Nếu ngày nay Con Lười chỉ nặng khoảng bốn đến năm ki-lô-gam và treo lơ lửng trên ngọn cây, thì chỉ khoảng mười ngàn năm trước, cụ tổ của nó mang tên Lười Đất Khổng Lồ Megatherium là một quái vật ngang ngửa voi ma mút! Với chiều cao khi đứng thẳng lên tới sáu mét và nặng tới bốn tấn, Lười Đất Khổng Lồ sở hữu bộ móng vuốt dài ngang thanh kiếm để đào những đường hầm ngầm khổng lồ xuyên qua lớp đất đá cứng ở Nam Mỹ! Những đường hầm cổ đại mang tên Paleoburrows tại Brazil dài hàng trăm mét và cao tới hai mét vẫn còn nguyên vẹn vết cào khổng lồ trên vách đá, khiến các nhà địa chất từng lầm tưởng là công trình của người cổ đại! Thậm chí từng tồn tại một nhánh họ hàng mang tên Lười Biển Thalassocnus sống dọc bờ biển Peru, tiến hóa bộ xương nặng trĩu để lặn xuống đáy Thái Bình Dương gặm rong biển hệt như loài bò biển! [surprise-oh] Một cúp lưu niệm hóa thạch xứng đáng được trao tặng cho dòng họ Lười vĩ đại!
```
**Part 2** → `audio/vs/scene09_p2.wav` (362 ký tự) · mood `hao_hung`

```text
Danh hiệu phụ thứ hai — Giải thưởng 'Cuộc Đào Tẩu Hóa Thạch Lâu Đời Nhất' — thuộc về Gấu Trúc Lớn với hóa thạch cụ tổ Ailurarctos tám triệu năm tuổi tại tỉnh Vân Nam! Phát hiện hóa thạch này chứng minh rằng ngay từ tám triệu năm trước, tổ tiên của Gấu Trúc đã có chiếc xương cổ tay mọc dài ra thành ngón tay giả thứ sáu để cầm nắm thân tre ăn uống! [surprise-wa]
```
**Part 3** → `audio/vs/scene09_p3.wav` (589 ký tự) · mood `bi_hai`

```text
Danh hiệu phụ thứ ba — Giải thưởng 'Điệp Viên Nằm Vùng Bất Tử' — khiến cả hội đồng khoa học phải bật cười nghiêng ngả, thuộc về họ hàng nhà Bọ Pháo Thủ mang tên Paussinae! Khác với Bọ Pháo Thủ của chúng ta dùng súng một trăm độ C bắn nhau tóe lửa, nhánh họ hàng Paussinae lại cất súng đi và tiến hóa tuyến tiết ra đúng hợp chất hóa học mùi hương của... Kiến Chúa! Chui vào tận phòng ngủ hoàng gia của đàn kiến, chú bọ này sống êm ấm như một vị hoàng đế, được kiến thợ chăm sóc hầu hạ lau chùi, và thỉnh thoảng lén ăn thịt luôn cả ấu trùng kiến con mà đàn kiến không hề hay biết! [laughter]
```
**Part 4** → `audio/vs/scene09_p4.wav` (608 ký tự) · mood `tram_bi_an`

```text
Và danh hiệu phụ cuối cùng — Giải thưởng 'Dòng Họ Điệp Viên Bí Ẩn Nhất' — dành tặng cho các cô nàng Chim Tu Hú với bí mật di truyền mang tên Gentes! Làm sao một loài chim Tu Hú có thể làm giả trứng giống hệt của hàng chục loài chim chủ khác nhau mà không bị lai tạp màu sắc lẫn lộn? Các nhà di truyền học giải mã được rằng: bộ gen quy định màu sắc và hoa văn vỏ trứng của Tu Hú nằm trọn trên nhiễm sắc thể W — thứ chỉ truyền thẳng từ chim mẹ sang con gái! Nhờ vậy, trong cùng một loài chia thành hàng chục dòng họ bí mật truyền nghề gia truyền suốt hàng ngàn năm mà không bao giờ bị mất bí kíp! [surprise-oh]
```
**Part 5** → `audio/vs/scene09_p5.wav` (994 ký tự) · mood `hao_hung`

```text
Và giải thưởng phụ thứ năm — danh hiệu 'Khu Vườn Sinh Thái Di Động Đông Đúc Nhất' — tiếp tục gọi tên Con Lười với hơn chín trăm con bọ cánh cứng, bướm đêm và hàng triệu vi sinh vật chung sống hòa bình trên cùng một bộ lông! Trên thực tế, mỗi sợi lông thô bên ngoài của Con Lười có các vết nứt siêu nhỏ chạy dọc theo chiều dài, đóng vai trò như những căn hộ chung cư lý tưởng giữ nước mưa để cả hệ sinh thái tí hon cùng phát triển! Tiếp theo là giải thưởng 'Sinh Con Khắc Nghiệt Nhất Thế Giới Thú' dành cho Gấu Trúc Lớn! Trong khoảng gần một nửa số ca sinh nở, gấu trúc mẹ đẻ ra hai chú gấu con sinh đôi tí hon yếu ớt! Trong suốt tuần đầu tiên sau khi sinh, gấu mẹ khổng lồ phải ôm chặt đứa con bé bằng ngón tay cái vào lòng liên tục không rời nửa bước để truyền hơi ấm! Tuy nhiên trong tự nhiên, nguồn sữa ít ỏi từ khẩu phần ăn tre chỉ đủ cho mẹ nuôi đúng một đứa con khỏe mạnh hơn, đồng thời gấu con sinh ra điếc đặc và phải mất tới bốn mươi lăm ngày sau mới mở mắt nhìn thế giới lần đầu tiên!
```
**Part 6** → `audio/vs/scene09_p6.wav` (597 ký tự) · mood `am_ap`

```text
Cuối cùng là giải 'Bậc Thầy Hợp Tác Không Cần Ngôn Ngữ' dành cho cặp bạn thân Tôm Súng và Cá Bống! Dù Tôm Súng mắt cực kém, chỉ cần một cái chạm râu nhẹ lên đuôi Cá Bống là cả hai phối hợp tác chiến ăn ý hàng chục năm liền! Tôm Súng cặm cụi dọn dẹp xây sửa căn hầm dưới cát mỗi ngày, còn Cá Bống kiên nhẫn đứng gác cửa và thậm chí chia sẻ luôn cả những mẩu thức ăn thừa cho người bạn thợ xây mù lòa! Những giải thưởng phụ tuyệt vời đã giúp chúng ta hiểu sâu sắc hơn về cội nguồn của muôn loài! Bây giờ, hãy siết chặt dây an toàn vì trước mắt chúng ta là ba vòng thi quyết định vận mệnh ngôi vương!
```

### scene10 — PHÚC KHẢO TIN ĐỒN — ĐẬP TAN NHỮNG LẦM TƯỞNG THẾ KỶ BẰNG THỰC NGHIỆM
*Thẻ chương:* KHOA HỌC ĐÍNH CHÍNH LẦM TƯỞNG

*Badge:* `VÒNG 7` · *mood mặc định:* `nghiem_trang_gia`

**Part 0** → `audio/vs/scene10_p0.wav` (565 ký tự) · mood `hao_hung`

```text
Chào mừng toàn thể khán đài bước vào Vòng bảy: Đấu trường phúc khảo tin đồn và đập tan những hiểu lầm thế kỷ! Trong thế giới tự nhiên, có rất nhiều lời đồn thổi nghe rất lọt tai nhưng thực chất lại sai hoàn toàn về mặt khoa học! Ở vòng đấu này, ban giám khảo sẽ đưa ra bốn lời đồn đại phổ biến nhất về các thí sinh, sau đó dùng bằng chứng thực nghiệm để lật tẩy sự thật! Lời đồn số một nhắm thẳng vào Thằn Lằn Quỷ Gai: rất nhiều bài viết trên mạng khẳng định loài thằn lằn sa mạc Úc chỉ cần ngồi yên buổi sáng là sương đêm tự động ngưng tụ chảy đầy rãnh da để uống!
```
**Part 1** → `audio/vs/scene10_p1.wav` (183 ký tự) · mood `tram_bi_an`

```text
Liệu sương sớm có thực sự đủ làm đầy mạng lưới rãnh mao dẫn trên cơ thể Quỷ Gai hay không? Tiến sĩ Philipp Comanns đã tiến hành một thí nghiệm cân đo lạnh lùng trong phòng thí nghiệm!
```
**Part 2** → `audio/vs/scene10_p2.wav` (576 ký tự) · mood `don_dap`

```text
Kết quả cân đo chứng minh lời đồn đó... sai bét! Lượng hơi nước ngưng tụ từ không khí chỉ đủ làm ướt nhẹ bề mặt lớp gai ngoài cùng, hoàn toàn không đủ tạo thành giọt để chảy vào hệ thống rãnh mao dẫn! Thậm chí khi đứng trên cát có độ ẩm lên tới hai mươi hai phần trăm, lượng nước hút từ cát chỉ làm đầy được năm mươi chín phần trăm các rãnh da! Để giải khát triệt để giữa sa mạc khô cằn, Quỷ Gai phải chủ động hất cát ẩm phủ lên khắp lưng mình, ép hai mặt da hút lấy từng phân tử nước từ đất! Một phát hiện dập tắt hoàn toàn huyền thoại 'chỉ ngồi chờ sương rơi'! [surprise-oh]
```
**Part 3** → `audio/vs/scene10_p3.wav` (560 ký tự) · mood `hao_hung`

```text
Lời đồn số hai gọi tên Nhà Máy Điện Sống: Lươn Điện! Suốt hàng trăm năm, mọi cuốn sách giáo khoa đều dạy rằng Lươn Điện là loài cá săn mồi cô độc tuyệt đối, ghét giao du với đồng loại! Nhưng như chúng ta đã chứng kiến ở Vòng năm từ báo cáo tại lưu vực sông Iriri Brazil năm hai ngàn hai mươi mốt: hơn một trăm con Lươn Điện trưởng thành tụ họp và săn mồi tập thể hai lần mỗi ngày! Từ bảy giờ ba mươi sáng đến năm giờ chiều chúng nghỉ ngơi yên ả dưới đáy bùn, nhưng cứ đúng bình minh và hoàng hôn là cả trăm con hợp sức tạo thành đội quân săn mồi không đối thủ!
```
**Part 4** → `audio/vs/scene10_p4.wav` (636 ký tự) · mood `bi_hai`

```text
Lời đồn số ba nhắm vào chú gấu mũm mĩm: Gấu Trúc Lớn! Nhiều người chế giễu rằng Gấu Trúc là một lỗi tiến hóa ngớ ngẩn, dễ bị tuyệt chủng vì lười biếng và vụng về! Khoa học xin phản biện dứt khoát: Gấu Trúc chẳng hề ngớ ngẩn chút nào! Bộ lông trắng đen của nó được tính toán chính xác để ngụy trang hoàn hảo trước mắt thú ăn thịt trong rừng tuyết! Ngoài ra, đột biến gen Đu-ốc hai giúp nó sống khỏe bằng nguồn thức ăn ít ai thèm tranh giành, và nó còn biết dùng hợp chất phân ngựa làm thuốc giảm cảm giác lạnh mùa đông! Nếu không bị con người thu hẹp rừng tre, Gấu Trúc hoàn toàn dư sức ngự trị vùng núi Tứ Xuyên thêm hàng triệu năm nữa!
```
**Part 5** → `audio/vs/scene10_p5.wav` (566 ký tự) · mood `don_dap`

```text
Và lời đồn số bốn nhắm vào Bọ Pháo Thủ: Nhiều người thắc mắc tại sao phản ứng sinh nhiệt một trăm độ C lại không làm Bọ Pháo Thủ tự thiêu rụi bụng mình ngay từ phát bắn đầu tiên? Các nhà hóa học hữu cơ giải mã bí mật cực kỳ tinh vi: hai hóa chất hydroquinone và oxy già được chứa tách biệt hoàn toàn trong một túi dự trữ an toàn không hề có chất xúc tác! Phản ứng chỉ xảy ra bên trong buồng phản ứng bọc vỏ chitin cứng như gốm chịu nhiệt trong khoảnh khắc vài phần nghìn giây ngay trước khi bị tống thẳng ra ngoài! Nhờ đó chú bọ luôn an toàn tuyệt đối! [surprise-wa]
```
**Part 6** → `audio/vs/scene10_p6.wav` (396 ký tự) · mood `bi_hai`

```text
Lời đồn số năm nhắm vào Bố Già Capybara: trên mạng xã hội, nhiều người tin rằng Capybara hiền lành tuyệt đối đến mức không bao giờ cắn bất kỳ ai dù bị chọc ghẹo ra sao! Sự thật đính chính: dù tính tình cực kỳ điềm đạm, nhưng khi bị dồn ép vào góc tường hoặc khi bảo vệ đàn con nhỏ, cặp răng cửa sắc như dao đục của Capybara có thể tung ra cú cắn chí mạng rách toạc thịt kẻ xâm phạm! [surprise-oh]
```
**Part 7** → `audio/vs/scene10_p7.wav` (380 ký tự) · mood `hao_hung`

```text
Và lời đồn số sáu gọi tên Cá Cung Thủ: nhiều khán giả lầm tưởng loài cá này sống hoàn toàn bằng việc bắn rơi côn trùng đậu trên lá cây! Thực tế nghiên cứu dạ dày cho thấy: phần lớn khẩu phần ăn hàng ngày của Cá Cung Thủ là tôm tép, giáp xác và cá con bơi ngay dưới mặt nước! Kỹ năng bắn tia nước hạ côn trùng là tuyệt chiêu săn mồi bổ sung khi thức ăn dưới nước trở nên khan hiếm!
```
**Part 8** → `audio/vs/scene10_p8.wav` (619 ký tự) · mood `tram_bi_an`

```text
Và lời đồn cuối cùng trong vòng phúc khảo nhắm vào Chim Tu Hú: nhiều khán giả cứ nghe thấy tên họ nhà Tu Hú là mặc định rằng một trăm phần trăm các loài chim tu hú trên Trái Đất đều đi đẻ nhờ và hất trứng hàng xóm! Sự thật minh oan từ cuốn chuyên khảo nổi tiếng của Đại học Oxford: trong số khoảng một trăm bốn mươi loài thuộc họ Cu cu trên toàn thế giới, thực chất chỉ có khoảng năm mươi chín loài sống ký sinh đẻ nhờ! Hơn một nửa gia tộc họ hàng của Tu Hú — với hơn tám mươi loài khác nhau — vẫn tự mình chăm chỉ tha rơm xây tổ, tự ấp trứng và mớm mồi nuôi con khôn lớn như những ông bố bà mẹ mẫu mực nhất! [laughter]
```
**Part 9** → `audio/vs/scene10_p9.wav` (283 ký tự) · 🎭 cameo `tham_phan`

```text
Kết quả Vòng bảy phúc khảo tin đồn: Huy chương vàng thuộc về Thằn Lằn Quỷ Gai với thí nghiệm lật tẩy huyền thoại uống sương đêm! Huy chương bạc thuộc về Lươn Điện với bằng chứng lật đổ định kiến săn mồi cô độc! Huy chương đồng thuộc về Bọ Pháo Thủ với cơ chế van cách ly chống tự nổ!
```
**Part 10** → `audio/vs/scene10_p10.wav` (409 ký tự) · mood `hao_hung`

```text
Bảng điểm sau Vòng bảy trở nên căng thẳng đến nghẹt thở: Ba tuyển thủ đồng dẫn đầu với sáu điểm là Tôm Súng, Lươn Điện và Thằn Lằn Quỷ Gai! Gấu Trúc và Hà Mã bám sát phía sau với năm điểm! Bọ Pháo Thủ và Chim Tu Hú bốn điểm, Cá Cung Thủ và Capybara ba điểm, Con Lười một điểm! Trước mắt chúng ta chỉ còn Vòng Bán Kết và Vòng Chung Kết điểm nhân đôi! Ai sẽ bứt tốc vào phút chót? Xin mời theo dõi ngay sau đây!
```

### scene11 — TIA X ĐỒNG BỘ XUYÊN BỤNG BỌ VÀ KHO BÁU THUỐC TRONG LÔNG LƯỜI
*Thẻ chương:* CÚ LỘI NGƯỢC DÒNG NGOẠN MỤC

*Badge:* `BÁN KẾT` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene11_p0.wav` (539 ký tự) · mood `hao_hung`

```text
Chào mừng toàn thể quý vị khán đài bước vào Vòng Bán Kết sinh tử của Đại Hội Sinh Tồn Mùa hai! Chỉ còn một bước chân nữa thôi là chúng ta sẽ bước vào Vòng Chung Kết nhân đôi điểm số! Và đúng như tinh thần của giải đấu, Vòng Bán Kết sẽ chứng kiến những công nghệ nghiên cứu tối tân nhất thế kỷ hai mươi mốt được chiếu trực tiếp lên sàn đấu! Đấu sĩ mở màn Bán Kết là chú bọ tí hon từng bị đánh giá thấp nhất lúc khai mạc: Bọ Pháo Thủ! Lần này chúng ta không nhìn từ bên ngoài mà nhìn xuyên thấu vào bên trong bụng chú bọ khi nó đang nhả đạn!
```
**Part 1** → `audio/vs/scene11_p1.wav` (240 ký tự) · mood `tram_bi_an`

```text
Năm hai ngàn mười lăm, một nhóm khoa học gia tại Viện Công Nghệ Massachusetts MIT và Đại học Arizona đã thực hiện một kỳ tích chưa từng có: đưa Bọ Pháo Thủ vào máy gia tốc hạt synchrotron quay phim tia X tốc độ hai ngàn khung hình mỗi giây!
```
**Part 2** → `audio/vs/scene11_p2.wav` (463 ký tự) · mood `don_dap`

```text
Đoạn phim tia X đã vén bức màn bí mật về cơ chế van tự động thiên tài bên trong cơ thể dài chưa đầy hai phân này! Ngay khi tia hơi nóng được tống ra ngoài qua nòng pháo, áp suất trong buồng phản ứng tụt xuống, cánh van lại tự động bật mở cho một giọt nhiên liệu mới chảy xuống! Đây chính là cơ chế tự điều áp bằng chính vụ nổ của mình mà không cần tiêu tốn năng lượng não bộ để điều khiển từng phát bắn! Một cỗ máy cơ khí sinh học hoàn mỹ tuyệt đối! [surprise-wa]
```
**Part 3** → `audio/vs/scene11_p3.wav` (635 ký tự) · mood `am_ap`

```text
Tuyển thủ thứ hai bước lên sàn Bán Kết khiến cả hội trường phải lặng người vì ngạc nhiên: Thánh sống chậm Con Lười! Kẻ đang đứng cuối bảng tổng sắp với chỉ một điểm duy nhất! Nhiều người nghĩ Con Lười chẳng làm được gì ngoài việc treo ngược ngủ gật. Nhưng năm hai ngàn mười bốn, tiến sĩ Sarah Higginbotham tại Viện Nghiên cứu Nhiệt đới Smithsonian đã phát hiện một kho báu y học nằm ngay trên bộ lông thô ráp của nó! Từ mẫu lông của chỉ chín chú Con Lười ba ngón hoang dã, các nhà khoa học đã phân lập nuôi cấy thành công tới tám mươi bốn chủng nấm độc đáo thuộc ngành nấm túi, trong đó có những loài chưa từng được nhân loại biết tới!
```
**Part 4** → `audio/vs/scene11_p4.wav` (688 ký tự) · mood `don_dap`

```text
Và khi đưa chiết xuất từ những chủng nấm lông lười này đi thử nghiệm sinh học, kết quả thu được làm rung chuyển cả ngành dược học thế giới! Bảy mươi bốn chủng nấm được chiết xuất thử nghiệm: hai mươi phẩy sáu phần trăm số mẫu đã tiêu diệt và ức chế cực mạnh tế bào ung thư vú Mờ-xê-ép bảy ở người! Chưa hết, nhiều chủng nấm khác trên lông Con Lười còn tỏ ra cực kỳ hiệu quả trong việc tiêu diệt ký sinh trùng gây bệnh sốt rét ác tính Plasmodium falciparum, bệnh Chagas nhiệt đới và hai mươi chủng nấm có khả năng kháng vi khuẩn gây bệnh kháng thuốc! [surprise-oh] Một hiệu thuốc di động sống treo lơ lửng trên ngọn cây rừng nhiệt đới! Ai dám bảo Thánh sống chậm là vô dụng nào? [laughter]
```
**Part 5** → `audio/vs/scene11_p5.wav` (585 ký tự) · mood `hao_hung`

```text
Tuyển thủ thứ ba mang đến bài thi cuối cùng của Bán Kết: Cá Cung Thủ! Bên cạnh trí tuệ nhớ bốn mươi bốn khuôn mặt người, nghiên cứu của Wöhl và Schuster còn giải mã tốc độ phản xạ thần tốc của loài cá này! Ngay khi con mồi trên cành vừa bị bắn rơi và chạm mặt nước hoặc rơi tự do trong không trung, bộ não cá chỉ mất vỏn vẹn bốn mươi mili-giây để tính toán lại toàn bộ góc quay cơ thể! Hơn nữa, mắt của Cá Cung Thủ tiến hóa hai vùng võng mạc chuyên biệt: vùng dưới nhìn sắc nét dưới nước tối và vùng trên chuyên nhìn xuyên qua mặt nước để phóng đại hình ảnh côn trùng giữa không trung!
```
**Part 6** → `audio/vs/scene11_p6.wav` (942 ký tự) · mood `tram_bi_an`

```text
Không chỉ dừng lại ở đó, ban giám khảo còn kiểm tra khả năng chịu đựng và duy trì nòi giống trong điều kiện khắc nghiệt của Hà Mã và Thằn Lằn Quỷ Gai! Trong cơ bắp đồ sộ của Hà Mã chứa mật độ myoglobin dự trữ oxy cực cao tương tự các loài cá voi đại dương! Nhờ kho oxy dự trữ trong từng thớ thịt đó, nó dễ dàng chạy bộ phi nước đại dưới đáy sông suốt năm phút mà không hề mỏi cơ! Còn Thằn Lằn Quỷ Gai mái đến mùa sinh sản lại tự mình đào một đường hầm sâu tới ba mươi xăng-ti-mét dưới cát cứng sa mạc, đẻ từ ba đến mười quả trứng rồi lấp kín xóa sạch mọi dấu vết! Khoảng ba đến bốn tháng sau, những chú quỷ gai con nở ra từ dưới lòng đất, tự mình đội cát chui lên với bộ giáp gai mini sắc nhọn sẵn sàng chiến đấu ngay từ ngày đầu tiên! Còn Bố Già Capybara thì sao? Để bảo toàn mạng sống trong mùa khô khắc nghiệt khi đầm lầy cạn kiệt, hàng trăm cá thể tụ họp thành đại liên minh rộng lớn cùng canh gác cho nhau trước móng vuốt báo đốm Jaguar!
```
**Part 7** → `audio/vs/scene11_p7.wav` (328 ký tự) · 🎭 cameo `tham_phan`

```text
Kết quả Vòng Bán Kết lịch sử đã có! Huy chương đồng thuộc về Cá Cung Thủ với phản xạ bốn mươi mili-giây và cấu trúc mắt kép nhìn xuyên mặt nước! Huy chương bạc thuộc về Con Lười với vườn nấm tám mươi bốn chủng diệt sốt rét và tế bào ung thư! Và Huy chương vàng thuộc về Bọ Pháo Thủ với phát hiện tia X đồng bộ van nổ tự điều áp!
```
**Part 8** → `audio/vs/scene11_p8.wav` (455 ký tự) · mood `hao_hung`

```text
Hãy nhìn lên Bảng Tổng Sắp ngay trước giờ bước vào Vòng Chung Kết! Cuộc đua kịch tính chưa từng thấy trong lịch sử: Bốn tuyển thủ đồng hạng nhất với sáu điểm là Tôm Súng, Lươn Điện, Thằn Lằn Quỷ Gai và Bọ Pháo Thủ! Gấu Trúc Lớn và Hà Mã bám ngay phía sau với năm điểm! Chim Tu Hú và Cá Cung Thủ bốn điểm! Capybara và Con Lười ba điểm! Thời khắc quyết định vận mệnh Mùa hai đã điểm! Xin mời toàn thể khán đài tiến vào Vòng Chung Kết: Món Quà Cho Nhân Loại!
```

### scene12 — MÓN QUÀ CHO NHÂN LOẠI — CÔNG NGHỆ ĐỘT PHÁ TƯƠNG LAI
*Thẻ chương:* ĐIỂM NHÂN ĐÔI ĐỊNH ĐOẠT VƯƠNG MIỆN

*Badge:* `CHUNG KẾT` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene12_p0.wav` (587 ký tự) · mood `hao_hung`

```text
Giờ phút thiêng liêng nhất của Đại Hội Sinh Tồn Mùa hai đã đến: Vòng Chung Kết Tối Thượng! Như đã công bố từ đầu giải, mọi huy chương tại vòng chung kết này sẽ được nhân đôi điểm số! Huy chương vàng trị giá sáu điểm! Huy chương bạc bốn điểm! Và huy chương đồng hai điểm! Với bốn ứng cử viên đang hòa nhau ở mốc sáu điểm và sáu ứng cử viên bám sát ngay phía sau, bất kỳ điều điên rồ nào cũng có thể xảy ra! Chủ đề thi đấu cao quý nhất của đêm chung kết là: Món Quà Cho Nhân Loại! Khoa học và kỹ thuật loài người đã học hỏi được những công nghệ thay đổi thế giới nào từ mười quái kiệt này?
```
**Part 1** → `audio/vs/scene12_p1.wav` (477 ký tự) · mood `don_dap`

```text
Ứng cử viên mở màn Chung Kết là Tôm Súng! Ngoài khả năng tạo plasma dưới nước hiệu suất cao gấp mười lần máy laser tại Đại học Texas A&M, sóng xung kích cavitation của nó còn đang được nghiên cứu ứng dụng trong xử lý nước thải và khoan đá ngầm không gây ô nhiễm! Bằng cách hội tụ năng lượng cơ học vào một điểm sụp đổ bong bóng khí siêu nhỏ, các kỹ sư có thể tạo ra phản ứng hóa học nhiệt độ cao để phân hủy chất độc công nghiệp dưới nước mà không cần hóa chất tẩy rửa độc hại!
```
**Part 2** → `audio/vs/scene12_p2.wav` (511 ký tự) · mood `hao_hung`

```text
Ứng cử viên thứ hai bước lên bục trình diễn công nghệ là Thằn Lằn Quỷ Gai! Dựa trên thí nghiệm cân đo rãnh da năm hai ngàn mười sáu và nghiên cứu tổng hợp năm hai ngàn mười bảy của tiến sĩ Philipp Comanns, các kỹ sư vật liệu đã phát minh ra tấm màng thu ẩm sa mạc thụ động! Lấy cảm hứng từ cấu trúc rãnh hình nêm dẫn nước một chiều chống bay hơi của chú thằn lằn sa mạc Úc, những tấm màng kim loại khắc laser vi mô này có khả năng hút ẩm từ sương đêm và đất ẩm dẫn về bể chứa mà không tốn một Oát điện năng nào!
```
**Part 3** → `audio/vs/scene12_p3.wav` (635 ký tự) · mood `don_dap`

```text
Ứng cử viên thứ ba: Lươn Điện! Một phát minh công nghệ y sinh từng lên trang bìa tạp chí Nature cuối năm hai ngàn mười bảy của giáo sư Michael Mayer và tiến sĩ Thomas Schroeder! Thay vì dùng pin kim loại cứng chứa hóa chất độc hại có nguy cơ rò rỉ trong cơ thể bệnh nhân, nhóm nghiên cứu đã xếp hàng ngàn giọt gel nước hydrogel chứa muối ion xen kẽ qua màng chọn lọc! Khi tiếp xúc đồng thời, hàng ngàn ngăn gel mềm tạo ra hiệu điện thế lên tới một trăm mười Vôn hoàn toàn tương thích sinh học với cơ thể người! Mở ra kỷ nguyên cung cấp năng lượng vĩnh cửu cho máy tạo nhịp tim, kính áp tròng thông minh và robot mềm y tế! [surprise-oh]
```
**Part 4** → `audio/vs/scene12_p4.wav` (542 ký tự) · mood `am_ap`

```text
Ứng cử viên thứ tư khiến cả khán đài xúc động nghẹn ngào: Thánh sống chậm Con Lười! Kẻ bị chế giễu suốt từ đầu giải đấu lại đang nắm giữ chìa khóa cứu sống hàng triệu bệnh nhân! Hơn hai mươi phần trăm số chủng nấm phân lập từ bộ lông rêu xanh của Con Lười có khả năng tiêu diệt tế bào ung thư vú Mờ-xê-ép bảy, bên cạnh những hoạt chất cực mạnh chống lại ký sinh trùng sốt rét và vi khuẩn kháng kháng sinh đang đe dọa nhân loại! Một loài vật đi chậm nhất hành tinh nhưng lại đi trước ngành dược học hiện đại cả một bước tiến dài! [surprise-wa]
```
**Part 5** → `audio/vs/scene12_p5.wav` (879 ký tự) · mood `don_dap`

```text
Và ứng cử viên cuối cùng bước lên sân khấu Chung Kết là pháo thủ tí hon nửa gam: Bọ Pháo Thủ! Công trình khoa học của giáo sư Andy McIntosh tại Đại học Leeds nước Anh đã làm thay đổi ngành công nghệ phun đốt toàn cầu! Công nghệ phun sương chớp nhoáng mang thương hiệu µMist mô phỏng chính xác van cơ học buồng phản ứng của Bọ Pháo Thủ: không cần máy bơm áp suất cao cồng kềnh hay khí nén độc hại, chỉ dùng nhiệt năng nhỏ tạo vụ nổ hơi giãn nở! Công nghệ này giúp tăng hiệu suất đốt cháy nhiên liệu của động cơ tên lửa và tua-bin khí, tạo ra các ống hít thuốc hen suyễn chính xác tới từng mi-crô-mét, và đặc biệt là chế tạo ra súng chữa cháy rừng thế hệ mới! Chỉ từ một buồng nén nhỏ dài năm xăng-ti-mét, thiết bị mô phỏng Bọ Pháo Thủ bắn luồng sương dập lửa xa tới mười mét với lượng nước tiết kiệm gấp nhiều lần! Một phát minh cứu rừng và cứu người vô cùng vĩ đại! [surprise-oh]
```
**Part 6** → `audio/vs/scene12_p6.wav` (771 ký tự) · mood `hao_hung`

```text
Và trước khi trao giải, ban giám khảo còn tôn vinh hai món quà y học đầy bất ngờ từ hai chú gấu và hà mã! Thứ nhất, năm hai ngàn mười hai các nhà khoa học đã giải mã bộ gen của Gấu Trúc Lớn và phát hiện ra một chuỗi peptit kháng khuẩn cực mạnh mang tên cathelicidin-AM! Trong thử nghiệm diệt vi khuẩn Staphylococcus kháng thuốc, hợp chất từ Gấu Trúc tiêu diệt sạch vi khuẩn chỉ trong chưa đầy một giờ đồng hồ, nhanh gấp sáu lần so với thuốc kháng sinh clindamycin thông thường mất tới sáu giờ! [surprise-oh] Còn sắc tố axit hipposudoric từ mồ hôi đỏ của Hà Mã chặn đứng toàn bộ dải tia cực tím từ hai trăm đến sáu trăm na-nô-mét mà lại không hòa tan trôi tuột trong nước và thân thiện với rạn san hô — mở đường chế tạo kem chống nắng sinh học thế hệ mới bảo vệ đại dương!
```
**Part 7** → `audio/vs/scene12_p7.wav` (654 ký tự) · 🎭 cameo `tham_phan`

```text
Thời khắc công bố kết quả Chung Kết điểm nhân đôi đã điểm! Sau khi cân nhắc giá trị khoa học, tính ứng dụng thực tiễn và sức lan tỏa nhân văn, hội đồng giám khảo xin tuyên bố: Huy chương đồng Chung Kết và hai điểm thuộc về Lươn Điện với phát minh pin sinh học mềm hydrogel nuôi máy tạo nhịp tim tương lai! Huy chương bạc Chung Kết và bốn điểm thuộc về... Con Lười! Với vườn nấm kỳ diệu trên bộ lông giúp con người chống lại bệnh sốt rét và tế bào ung thư! [surprise-wa] Và Huy chương vàng Chung Kết cùng sáu điểm quyết định của Đại Hội Sinh Tồn Mùa hai chính thức thuộc về... Bọ Pháo Thủ! Với công nghệ phun sương vi mô cứu hỏa và động cơ tên lửa vũ trụ!
```
**Part 8** → `audio/vs/scene12_p8.wav` (203 ký tự) · mood `hao_hung`

```text
Từ vị trí bị đánh giá chỉ vào thi cho đủ đội hình, chú bọ dài hai phân đã làm nên cú lội ngược dòng vĩ đại nhất mọi thời đại! Mời toàn thể quý vị cùng hướng mắt lên Bảng Tổng Sắp Chung Cuộc ngay sau đây!
```

### scene13 — LỄ TRAO HUY CHƯƠNG VÀ BẢNG TỔNG SẮP ĐIỂM SỐ MÙA 2
*Thẻ chương:* TÂN VƯƠNG NỬA GAM ĐĂNG QUANG

*Badge:* `TỔNG SẮP` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene13_p0.wav` (356 ký tự) · mood `hao_hung`

```text
[surprise-oh] Khoảnh khắc lịch sử của Đại Hội Sinh Tồn Mùa hai đã chính thức khép lại mọi dự đoán! Xin mời toàn thể mười tuyển thủ và hàng vạn khán giả cùng hướng mắt lên Bảng Tổng Sắp Cuối Cùng! Trải qua tám vòng đấu khốc liệt với một trăm phần trăm dữ liệu khoa học mới hoàn toàn, bảng vàng danh dự Mùa hai đã ghi tên những nhà chinh phục xứng đáng nhất!
```
**Part 1** → `audio/vs/scene13_p1.wav` (441 ký tự) · mood `don_dap`

```text
Và Tân Vương của Đại Hội Sinh Tồn Mùa hai chính thức gọi tên: Bọ Pháo Thủ với tổng điểm mười hai điểm! Hai huy chương vàng, một huy chương bạc và một huy chương đồng! [surprise-wa] Nặng chưa đầy nửa gam và từng bị các chuyên gia gạch tên ngay từ vòng cân ký! Nhưng với buồng phản ứng tia X đồng bộ, cơ chế van nổ tự điều áp không cần khí đẩy và bằng sáng chế công nghệ cứu hỏa bắn xa mười mét, Bọ Pháo Thủ đã chinh phục trọn vẹn cả thế giới!
```
**Part 2** → `audio/vs/scene13_p2.wav` (695 ký tự) · mood `hao_hung`

```text
Ngôi vị Á Quân thuộc về: Lươn Điện với tám điểm! Ba huy chương bạc và hai huy chương đồng! Đập tan định kiến sống cô độc bằng màn săn mồi bầy đàn hơn một trăm con tại sông Iriri, cùng phát minh pin mềm hydrogel một trăm mười Vôn nuôi sống trái tim nhân loại! Xứng danh chiến thần đầm lầy Nam Mỹ! Và cú lội ngược dòng ngoạn mục nhất đêm nay gọi tên: Con Lười ở vị trí Hạng Ba chung cuộc với bảy điểm! Hai huy chương bạc và một huy chương đồng! [laughter] Từ một thí sinh bị trêu chọc vì mất mười phút mới trả lời xong một câu hỏi, Con Lười đã chứng minh sức mạnh phi thường với hệ thống dây chằng treo nội tạng, cụ tổ khổng lồ bốn tấn và tám mươi bốn chủng nấm chống ung thư sốt rét trên bộ lông!
```
**Part 3** → `audio/vs/scene13_p3.wav` (908 ký tự) · mood `am_ap`

```text
Xếp ngay sát nút phía sau là hai chiến binh sáu điểm: Tôm Súng với hai huy chương vàng nhờ công nghệ tạo plasma gấp mười lần laser và đế chế xã hội ba trăm tôm lính; cùng Thằn Lằn Quỷ Gai với một vàng, một bạc, một đồng nhờ kỹ thuật hắt cát ẩm và màng thu nước sa mạc! Nhóm năm điểm gọi tên hai gã khổng lồ đáng mến: Hà Mã với danh hiệu cỗ máy bơm bốn trăm ký Silicon mỗi ngày và thính giác xương hàm dưới; cùng Gấu Trúc Lớn với đột biến gen Đu-ốc hai, áo ngụy trang và liệu pháp phân ngựa chống rét! Nhóm bốn điểm vinh danh hai bậc thầy bầu trời và mặt nước: Chim Tu Hú với đường bay vệ tinh mười sáu ngàn cây số và màn cải trang chim ưng; cùng Cá Cung Thủ với bộ não nhận diện bốn mươi bốn khuôn mặt người chính xác tám mươi sáu phần trăm! Và cuối cùng, Bố Già Capybara đạt ba điểm danh dự với một huy chương bạc và một huy chương đồng nhờ cặp răng cửa tự mài sắc và văn hóa nuôi con chung cực kỳ nhân văn!
```
**Part 4** → `audio/vs/scene13_p4.wav` (468 ký tự) · mood `hao_hung`

```text
Khoan đã! Trước khi bước vào lễ bế mạc, anh MC xin phép điểm lại hành trình đáng kinh ngạc của cả mười đấu sĩ và phỏng vấn nhanh bộ ba quán quân đêm nay! Từ những giây phút đầu tiên bị giới chuyên gia chê bai là tí hon và chậm chạp, Bọ Pháo Thủ và Con Lười đã chứng minh rằng giá trị thực sự của sự sống không nằm ở vẻ bề ngoài! Xin chúc mừng Tân Vương Bọ Pháo Thủ! Từ vị trí bị gạch tên ở vòng cân ký cho tới ngôi vương mười hai điểm, cảm xúc của bạn lúc này thế nào?
```
**Part 5** → `audio/vs/scene13_p5.wav` (211 ký tự) · 🎭 cameo `phat_thanh_vien`

```text
Thưa anh MC và toàn thể khán đài, kích thước chưa đầy nửa gam chưa bao giờ là giới hạn! Chỉ cần bạn có áp suất nội tại vững vàng và không bao giờ bỏ cuộc dù có bị nuốt vào bụng cóc, bạn sẽ luôn bùng nổ tỏa sáng!
```
**Part 6** → `audio/vs/scene13_p6.wav` (363 ký tự) · mood `hao_hung`

```text
Một phát biểu cực kỳ bùng nổ! Còn Á Quân Lươn Điện thì sao? Từ một sinh vật bị gán mác cô độc, bạn đã cho cả thế giới thấy sức mạnh đoàn kết của bầy đàn hơn một trăm chiến binh! Còn Hạng Ba Con Lười — chủ nhân của cú lội ngược dòng giàu cảm xúc nhất lịch sử Đại Hội Sinh Tồn! Hãy giơ cao hai tấm huy chương bạc và chiếc cúp hiệu thuốc rừng mưa của bạn lên đi nào!
```
**Part 7** → `audio/vs/scene13_p7.wav` (105 ký tự) · 🎭 cameo `be_con`

```text
Cảm ơn... tất cả... mọi người... Nhớ bảo vệ... rừng cây... cho tụi mình... treo ngược... ngủ ngon... nha!
```
**Part 8** → `audio/vs/scene13_p8.wav` (116 ký tự) · mood `hao_hung`

```text
Và chúng ta cũng đừng quên bảy người anh hùng còn lại đã chiến đấu hết mình suốt tám vòng thi đấu nghẹt thở đêm nay!
```
**Part 9** → `audio/vs/scene13_p9.wav` (669 ký tự) · mood `don_dap`

```text
Tôm Súng và Thằn Lằn Quỷ Gai đã chứng minh rằng dù nhỏ bé nhưng hỏa lực plasma và kỹ thuật thu hoạch ẩm sa mạc đủ sức khuất phục bất kỳ đối thủ to xác nào! Hà Mã và Gấu Trúc Lớn đã lật đổ mọi định kiến sai lầm bấy lâu nay bằng nguồn khoáng chất Silicon nuôi sống dòng sông và bộ gen tiết kiệm năng lượng thiên tài! Còn bộ ba Chim Tu Hú, Cá Cung Thủ và Bố Già Capybara thì mãi mãi là biểu tượng của trí tuệ định vị không gian, thị giác nhận diện khuôn mặt và tinh thần ngoại giao hòa bình bất diệt! Mười đấu sĩ, mười tuyệt tác tiến hóa độc bản! Không một ai ra về tay trắng, và từng con số đêm nay đều là một lời tri ân sâu sắc gửi tới trí tuệ vĩ đại của mẹ thiên nhiên!
```

### scene14 — BÀI HỌC MÙA 2, BẢO TỒN THIÊN NHIÊN VÀ HÉ LỘ DỊ NHÂN MÙA 3
*Thẻ chương:* THÔNG ĐIỆP BẢO TỒN VÀ MÙA 3

*Badge:* `BẾ MẠC` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene14_p0.wav` (212 ký tự) · mood `am_ap`

```text
Bọ Pháo Thủ đứng trên đỉnh bục cao nhất, chiếc vương miện vàng bé xíu nằm vừa vặn trên chiếc đầu màu cam ánh kim. Một sinh vật nặng chưa tới nửa gam đã chiến thắng ngoạn mục giữa những cỗ xe tăng nặng tới ba tấn!
```
**Part 1** → `audio/vs/scene14_p1.wav` (124 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Chúc mừng bạn Bọ Pháo Thủ nha! Đợi mình xuống khỏi cái cây chuối này rồi tụi mình cùng đi ăn tiệc tre với cá sấu Caiman nhé!
```
**Part 2** → `audio/vs/scene14_p2.wav` (413 ký tự) · mood `hao_hung`

```text
Nhìn lại toàn bộ tám vòng thi đấu vừa qua, Mùa hai đã dạy cho chúng ta một bài học tuyệt đẹp: trong tự nhiên không hề có sinh vật nào là 'lỗi tiến hóa' hay 'vô dụng'! Mỗi đặc điểm kỳ quặc mà thoạt nhìn ta tưởng là ngớ ngẩn — như việc Con Lười treo ngược, Gấu Trúc lăn phân ngựa hay Hà Mã thải phân xuống nước — thực chất đều là những mắt xích hoàn hảo giữ cho cỗ máy Trái Đất vận hành trơn tru qua hàng triệu năm!
```
**Part 3** → `audio/vs/scene14_p3.wav` (265 ký tự) · mood `am_ap`

```text
Và giống như thư viện sống khổng lồ của thiên nhiên, mười loài vật đêm nay đã mở ra cho nhân loại những công nghệ thay đổi cả tương lai: từ pin mềm nuôi trái tim nhân tạo, màng thu nước không tốn điện, vòi phun cứu hỏa xuyên rừng đến thuốc chống ung thư và sốt rét!
```
**Part 4** → `audio/vs/scene14_p4.wav` (1220 ký tự) · mood `bi_hai`

```text
[sigh] Nhưng ngay ngoài cánh cửa đấu trường này, những trang sách quý giá đó đang đối mặt với nguy cơ bị xé rách mãi mãi bởi chính tác động của con người! Rừng mưa nhiệt đới Panama và Amazon bị tàn phá đe dọa ngôi nhà của Con Lười và Lươn Điện — khiến chúng ta có thể mất đi những chủng nấm kháng sinh chưa kịp khám phá! Khu bảo tồn rừng tre Tứ Xuyên cũng cần được gìn giữ từng mét vuông để Gấu Trúc Lớn có đủ nguồn thức ăn quanh năm và giữ lại peptit kháng khuẩn quý giá trong máu của chúng! Đầm lầy Pantanal Nam Mỹ đang đối mặt với những trận cháy rừng lịch sử và hạn hán kéo dài, đe dọa không gian sống bình yên của hàng ngàn Bố Già Capybara và muôn loài chung sống xung quanh! Sự suy giảm quần thể Hà Mã làm đứt gãy nguồn cung bốn trăm ký Silicon mỗi ngày cho các dòng sông châu Phi; còn biến đổi khí hậu khắc nghiệt khiến hành trình di cư mười sáu ngàn cây số của Chim Tu Hú ngày càng gian nan hơn! Tại những rạn san hô Caribe nơi Tôm Súng sinh sống, hiện tượng axit hóa đại dương và tẩy trắng san hô đang phá hủy những ngôi nhà bọt biển của cả đế chế ba trăm tôm lính! Và tại vùng rừng ngập mặn Đông Nam Á, nạn chặt phá rừng ven biển đang thu hẹp môi trường săn mồi độc đáo của những xạ thủ Cá Cung Thủ thông minh!
```
**Part 5** → `audio/vs/scene14_p5.wav` (485 ký tự) · mood `am_ap`

```text
Nhưng tin vui cũng đã đến khi nỗ lực bảo tồn toàn cầu phát huy tác dụng! Nhờ việc phục hồi hàng ngàn héc-ta hành lang rừng tre kết nối tại Trung Quốc, Liên minh Bảo tồn Thiên nhiên Quốc tế IUCN đã chính thức hạ cấp Gấu Trúc Lớn từ mức Nguy Cấp xuống mức Sắp Nguy Cấp! Đó là minh chứng hùng hồn nhất cho thấy: khi con người chung tay hành động, thiên nhiên luôn có cơ hội hồi sinh mạnh mẽ! Bởi vì bảo vệ một loài vật bé nhỏ cũng chính là giữ lại cơ hội sống cho chính nhân loại mai sau!
```
**Part 6** → `audio/vs/scene14_p6.wav` (662 ký tự) · mood `hao_hung`

```text
Và bây giờ, lá phiếu quyền lực nhất nằm trong tay của chính bạn! Bạn có đồng ý với ngôi vương của Bọ Pháo Thủ không? Hay trong trái tim bạn, Lươn Điện, Con Lười, Tôm Súng hay Hà Mã mới là nhà vô địch thực thụ? Và trước khi khép lại cánh cửa đấu trường Mùa hai, anh MC có một thử thách nhỏ dành cho các nhà thông thái nhí và khán giả đang theo dõi màn hình: Trong suốt hơn một tiếng vừa qua, chi tiết khoa học mới nào làm bạn bất ngờ nhất: Gấu Trúc tắm phân ngựa chống rét, Cá Cung Thủ nhớ mặt người hay Bọ Pháo Thủ tạo ra súng cứu hỏa? Hãy bình luận tên nhà vô địch của bạn và chia sẻ xem bạn ấn tượng nhất với phát hiện khoa học mới nào dưới phần bình luận nhé!
```
**Part 7** → `audio/vs/scene14_p7.wav` (420 ký tự) · mood `am_ap`

```text
Mười tập phim lẻ, một đêm đại hội lịch sử với hàng trăm sự thật khoa học kỳ thú! Hy vọng hành trình hơn một giờ đồng hồ cùng Vẽ Chuyện Hoang Dã đã mang đến cho bạn thật nhiều tiếng cười sảng khoái và tình yêu sâu sắc dành cho thế giới tự nhiên! Nếu bạn thích phong cách đại hội tranh tài mới toanh này, đừng ngần ngại chia sẻ video này cho bạn bè và người thân cùng chiêm ngưỡng những kiệt tác tuyệt vời của tạo hóa nhé!
```
**Part 8** → `audio/vs/scene14_p8.wav` (130 ký tự) · mood `tram_bi_an`

```text
Và xin đừng vội tắt màn hình... bởi vì cánh cửa đường hầm bí mật của Đại Hội Sinh Tồn Mùa ba vừa hé mở những hồ sơ rùng mình nhất!
```
**Part 9** → `audio/vs/scene14_p9.wav` (833 ký tự) · mood `hao_hung`

```text
Một biệt đội dị nhân sở hữu những năng lực tự hủy và tái sinh điên rồ chưa từng thấy chuẩn bị đổ bộ! Một chú ếch tự co cơ bẻ gãy xương ngón chân đâm thủng da thịt làm móng vuốt chiến đấu! Một chú kỳ nhông sáu sừng mọc lại nguyên vẹn cả chi, tủy sống, một phần ba trái tim và não bộ mà không để lại một vết sẹo! Và một sinh vật đáy biển tự bắn toàn bộ ruột gan qua hậu môn trói chặt kẻ thù! Thậm chí còn có sự góp mặt của loài chim cắt lao xuống với vận tốc ba trăm tám mươi chín cây số một giờ, và loài cá mặt trăng nặng hai tấn ngơ ngác bậc nhất đại dương! Cộng thêm những cao thủ tí hon biết biến hóa thành thây ma và loài bò sát có sừng mọc xuyên qua hộp sọ! Mười dị nhân tiếp theo đang nóng lòng chờ ngày ra mắt! Hẹn gặp lại toàn thể quý vị khán giả tại Đại Hội Sinh Tồn Mùa ba! Phóng viên và MC xin chào tạm biệt và hẹn gặp lại!
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Mười quái kiệt mới. Tám vòng đấu sinh tử. Một chiếc vương miện! Tôm Súng và Lươn Điện được đặt cược sẽ thắng. Còn Bọ Pháo Thủ nửa gam... chuyên gia bảo tham gia cho vui! [laughter] Vòng một: Tôm Súng tạo dòng plasma dưới nước hiệu suất gấp mười lần máy laser! Vòng hai: Cá Cung Thủ nhận diện được bốn mươi bốn khuôn mặt người dù không có vỏ não! Vòng ba: Gấu Trúc tắm phân ngựa tươi để khóa thụ thể lạnh, còn Quỷ Gai hất cát ẩm lên lưng giải khát! Vòng bốn: Hà Mã bơm bốn trăm ký Silicon mỗi ngày xuống sông nuôi cả hệ sinh thái hồ châu Phi! Vòng năm: Lươn Điện bỏ lối sống cô độc, hợp tác săn mồi theo bầy đàn hơn một trăm con! Chung kết: ai mang lại công nghệ đỉnh cao nhất cho loài người? Nấm lông lười diệt ung thư hay vòi phun tên lửa Bọ Pháo Thủ? [surprise-wa] Và tân vương Mùa hai là... chú bọ nửa gam từng bị gạch tên ngay từ vòng cân ký! [question-ah] Bạn có đồng ý không? Xem trọn tám vòng đấu trong video dài nhé, vì ở đây có mười quái kiệt mới, tám vòng đấu sinh tử, và một chiếc vương miện!
```

**Whisper prompt:** `Đại Hội Sinh Tồn, Mùa 2, Vẽ Chuyện Hoang Dã, Gấu Trúc, Hà Mã, Con Lười, Chim Tu Hú, Capybara, Tôm Súng, Lươn Điện, Bọ Pháo Thủ, Thằn Lằn Quỷ Gai, Cá Cung Thủ, Tứ Xuyên, Amazon, Pantanal, Alice Springs, 218 dB, 5.000°C, 860V, 100°C, 500 lần/giây, 1.800 PSI, 2.500 con kiến, cavitation, sonoluminescence, electrocytes, hydroquinone, Snell, morillo, cecotrophy`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| hai mươi tư giờ | 24 giờ |
| Hai mươi tư giờ | 24 giờ |
| hai trăm mười tám đề-xi-ben | 218 dB |
| Hai trăm mười tám đề-xi-ben | 218 dB |
| tám trăm sáu mươi Vôn | 860V |
| Tám trăm sáu mươi Vôn | 860V |
| sáu trăm Vôn | 600V |
| bốn trăm Vôn | 400V |
| mười Vôn | 10V |
| năm ngàn độ C | 5.000°C |
| Năm ngàn độ C | 5.000°C |
| một trăm độ C | 100°C |
| Một trăm độ C | 100°C |
| bốn mươi lăm độ C | 45°C |
| năm mươi độ C | 50°C |
| dưới mười độ C | dưới 10°C |
| một ngàn tám trăm P-S-I | 1.800 PSI |
| Một ngàn tám trăm P-S-I | 1.800 PSI |
| năm trăm lần mỗi giây | 500 lần/giây |
| Năm trăm lần mỗi giây | 500 lần/giây |
| năm trăm phát | 500 phát |
| hai ngàn năm trăm | 2.500 |
| Hai ngàn năm trăm | 2.500 |
| một ngàn | 1.000 |
| Một ngàn | 1.000 |
| sáu ngàn | 6.000 |
| Sáu ngàn | 6.000 |
| hai trăm bảy mươi độ | 270° |
| chín mươi độ | 90° |
| ba mét | 3m |
| Ba mét | 3m |
| hai mét | 2m |
| Hai mét | 2m |
| ba tấn | 3 tấn |
| Ba tấn | 3 tấn |
| sáu mươi lăm ki-lô-gam | 65kg |
| Sáu mươi lăm ki-lô-gam | 65kg |
| hai mươi ki-lô-gam | 20kg |
| hai mươi xăng-ti-mét | 20cm |
| mười xăng-ti-mét | 10cm |
| năm xăng-ti-mét | 5cm |
| bốn xăng-ti-mét | 4cm |
| ba xăng-ti-mét | 3cm |
| hai xăng-ti-mét | 2cm |
| mười giây | 10 giây |
| Mười giây | 10 giây |
| ba mươi giây | 30 giây |
| hai mili-giây | 2 mili-giây |
| một phần mười giây | 1/10 giây |
| ba mươi ngày | 30 ngày |
| Ba mươi ngày | 30 ngày |
| mười bốn tiếng | 14 tiếng |
| Mười bốn tiếng | 14 tiếng |
| năm phút | 5 phút |
| mười lăm phút | 15 phút |
| một tiếng | 1 tiếng |
| Một tiếng | 1 tiếng |
| tám cây số một giờ | 8 km/h |
| ba mươi lăm cây số một giờ | 35 km/h |
| một trăm cây số một giờ | 100 km/h |
| tám mươi phần trăm | 80% |
| Tám mươi phần trăm | 80% |
| năm mươi sáu phần trăm | 56% |
| chín mươi chín phần trăm | 99% |
| một trăm phần trăm | 100% |
| Một trăm phần trăm | 100% |
| một phần ba | 1/3 |
| Một phần ba | 1/3 |
| năm mươi phần trăm | 50% |
| Năm mươi phần trăm | 50% |
| hai mươi phần trăm | 20% |
| gấp ba lần | gấp 3 lần |
| Gấp ba lần | gấp 3 lần |
| gấp bốn lần | gấp 4 lần |
| gấp hai lần | gấp 2 lần |
| gấp mười lần | gấp 10 lần |
| gấp đôi | gấp đôi |
| Mùa hai | Mùa 2 |
| mùa hai | mùa 2 |
| Tập mười tám | Tập 18 |
| Tập hai mươi | Tập 20 |
| Năm hai ngàn mười chín | Năm 2019 |
| năm hai ngàn mười chín | năm 2019 |
| Năm hai ngàn mười tám | Năm 2018 |
| năm hai ngàn mười tám | năm 2018 |
| Năm hai ngàn mười sáu | Năm 2016 |
| Năm hai ngàn mười lăm | Năm 2015 |
| Năm hai ngàn mười bốn | Năm 2014 |
| năm hai ngàn mười bốn | năm 2014 |
| Năm hai ngàn lẻ bảy | Năm 2007 |
| năm hai ngàn lẻ một | năm 2001 |
| Năm hai ngàn | Năm 2000 |
| Năm một ngàn chín trăm bốn mươi bảy | Năm 1947 |
| A-ma-dôn | Amazon |
| Pan-ta-nan | Pantanal |
| Tứ Xuyên | Tứ Xuyên |
| Xen-xi-út | Celsius |
| Kê-vin | Kelvin |
| Xo-nar | Sonar |
| Na-sa | NASA |
| Xơ-nen | Snell |
| mười bảy phần trăm | 17% |
| Mười bảy phần trăm | 17% |
| tám mươi ba phần trăm | 83% |
| Tám mươi ba phần trăm | 83% |
| ba mươi tám ký | 38kg |
| bốn mươi lần | 40 lần |
| ba mươi phần trăm | 30% |
| Ba mươi phần trăm | 30% |
| chông sắt | chông sắt |
| 100 km/h | 100 km/h |
| 218 dB | 218 dB |
| 5.000°C | 5.000°C |
| 860V | 860V |
| 500 phát | 500 phát |
| 100°C | 100°C |
| 1.800 PSI | 1.800 PSI |
| 3m | 3m |
| 2 mili-giây | 2 mili-giây |
| 5cm | 5cm |
| 10cm | 10cm |
| 270° | 270° |
| 30 ngày | 30 ngày |
| 1/3 | 1/3 |
| 56% | 56% |
| 1 tiếng | 1 tiếng |
| 30 giây | 30 giây |
| 8 km/h | 8 km/h |
| 15 phút | 15 phút |
| bốn mươi bốn | 44 |
| tám mươi mốt | 81 |
| tám mươi sáu phần trăm | 86% |
| hai mươi phẩy sáu phần trăm | 20,6% |
| tám mươi bốn | 84 |
| bảy mươi tư | 74 |
| mười lăm phần tỷ giây | 15 phần tỷ giây |
| một trăm mười Vôn | 110V |
| một trăm mười ki-lô-gam | 110kg |
| một trăm ki-lô-gam | 100kg |
| bốn ki-lô-gam | 4kg |
| năm ki-lô-gam | 5kg |
| một trăm mười gam | 110g |
| bốn mươi gam | 40g |
| hai trăm gam | 200g |
| mười hai đến ba mươi lăm mét | 12-35m |
| ba mươi lăm mét | 35m |
| một đến năm trăm mi-crô-mét | 1-500 μm |
| một trăm mili-ba | 100 mbar |
| chín mươi phần trăm | 90% |
| bốn mươi lăm phần trăm | 45% |
| bốn mươi sáu phẩy chín phần trăm | 46,9% |
| năm mươi lăm phần trăm | 55% |
| năm phần trăm | 5% |
| mười một phần trăm | 11% |
| mười lăm độ C | 15°C |
| âm năm độ C | -5°C |
| âm năm | -5 |
| hai mươi hai độ C | 22°C |
| hai mươi độ | 20 độ |
| bảy mươi sáu phần trăm | 76% |
| hai mươi bốn phần trăm | 24% |
| không phẩy bốn tấn | 0,4 tấn |
| bốn trăm ký | 400kg |
| một phẩy năm phần trăm | 1,5% |
| ba đến bốn ki-lô-gam | 3-4kg |
| mười sáu ngàn cây số | 16.000km |
| năm ngàn cây số | 5.000km |
| một trăm sáu mươi bốn cây số | 164km |
| năm gam | 5g |
| một mét hai đến một mét tám | 1,2-1,8m |
| hai đến mười con | 2-10 con |
| mười ngàn năm | 10.000 năm |
| sáu mét | 6m |
| bốn tấn | 4 tấn |
| tám triệu năm | 8 triệu năm |
| năm mươi chín phần trăm | 59% |
| hai mươi hai phần trăm | 22% |
| một phẩy hai mươi tám gam | 1,28g |
| một phẩy ba mươi hai gam | 1,32g |
| không phẩy bảy mi-crô-lít | 0,7 μl |
| bảy giờ ba mươi | 07:30 |
| năm giờ chiều | 17:00 |
| hai ngàn khung hình | 2.000 fps |
| năm trăm đến một ngàn lần | 500-1.000 lần |
| mười mét | 10m |
| mười hai điểm | 12 điểm |
| tám điểm | 8 điểm |
| bảy điểm | 7 điểm |
| sáu điểm | 6 điểm |
| năm điểm | 5 điểm |
| bốn điểm | 4 điểm |
| ba điểm | 3 điểm |
| hai điểm | 2 điểm |
| một điểm | 1 điểm |
| mười lăm điểm | 15 điểm |
| Tám mươi bốn | 84 |
| Hai mươi phẩy sáu | 20,6 |
| Bảy mươi bốn | 74 |
| Bốn mươi bốn | 44 |
| Mười sáu ngàn | 16.000 |
| Ba trăm | 300 |
| ba trăm | 300 |
| Một trăm | 100 |
| một trăm | 100 |
| tám trăm Oát | 800W |
| một Am-pe | 1A |
| một cây số | 1km |
| một phần tỷ giây | 1 phần tỷ giây |
| hai phân | 2cm |
| chỉ dưới ba mươi xăng-ti-mét | <30cm |
| chỉ bốn | 4 |
| số 44 | 44 |
| 44 khuôn mặt | 44 khuôn mặt |
| 16.000km | 16.000km |
| bốn mươi tám | 48 |
| bốn mươi lăm | 45 |
| hai mươi | 20 |
| mười hai | 12 |
| mười một | 11 |
| tám mươi | 80 |
| một trăm mười lăm | 115 |
| mười lăm | 15 |
| hai mươi hai | 22 |
| bốn mươi | 40 |
| sáu triệu lần | 6.000.000 lần |
| mười phút | 10 phút |
| năm giây | 5 giây |
| một phút | 1 phút |
| bốn năm con | 4-5 con |
| tám đến mười | 8-10 |
| hai ba vòng | 2-3 vòng |
| 38 đoạn | 38 đoạn |
| ba mươi tám | 38 |
| tám chú | 8 chú |
| chín chú | 9 chú |
| bảy chú | 7 chú |
| một trăm năm mươi | 150 |
| bốn mươi mili-giây | 40ms |
| ba mươi tám mét | 38m |
| hai trăm đến sáu trăm na-nô-mét | 200-600nm |
| hai mươi bốn độ C | 24°C |
| ba mươi ba độ C | 33°C |
| mười bốn phần trăm | 14% |
| mười bốn | 14 |
| một ngàn vôn | 1.000V |
| ba mươi xăng-ti-mét | 30cm |
| ba trăm tám mươi chín cây số một giờ | 389 km/h |
| ba tháng | 3 tháng |
| một giờ đồng hồ | 1 giờ |
| sáu giờ | 6 giờ |
| chín trăm lần | 900 lần |
| một trăm gam | 100g |
| chín trăm con | 900 con |
| bảy mươi | 70 |
| hai triệu năm | 2 triệu năm |
| một trăm năm mươi độ | 150 độ |
| năm mươi chín | 59 |
| một trăm bốn mươi | 140 |
| năm mươi chú | 50 chú |
| ba đến bốn tháng | 3-4 tháng |
| tám mươi loài | 80 loài |
| Tập mười một | Tập 11 |
| Tập mười chín | Tập 19 |
| Mùa ba | Mùa 3 |
| Đu-ốc hai | DUOX2 |
| Tê-rờ-pê-mờ tám | TRPM8 |
| Mờ-xê-ép bảy | MCF-7 |
| Tê bốn | T4 |
| mười ba phần trăm | 13% |
| Mười sáu | 16 |
| mười sáu | 16 |
| mười tám | 18 |
| hàng trăm năm | hàng trăm năm |
| triệu năm | triệu năm |
| ngàn năm | ngàn năm |
| Không một | Không một |
| ba chiều | 3D |
| mười giờ | 10:00 |
| một giờ | 1 giờ |
| bảy lần | 7 lần |
| gấp bảy lần | gấp 7 lần |
| mười sáu tiếng | 16 tiếng |
| ba mươi độ | 30 độ |
| bốn mươi hai | 42 |
| ba mươi ba | 33 |
| hai mươi tư | 24 |
| hai mươi mốt | 21 |
| tám trăm | 800 |
| năm trăm | 500 |
| bốn trăm | 400 |
| hai trăm | 200 |
| sáu mươi | 60 |
| năm mươi | 50 |
| ba mươi | 30 |
| hai mươi lăm | 25 |
| mười bảy | 17 |
| mười ba | 13 |
| năm hai ngàn hai mươi mốt | năm 2021 |
| năm hai ngàn hai mươi | năm 2020 |
| năm hai ngàn mười bảy | năm 2017 |
| năm hai ngàn mười sáu | năm 2016 |
| năm hai ngàn mười lăm | năm 2015 |
| năm hai ngàn mười hai | năm 2012 |
| năm hai ngàn mười một | năm 2011 |
| năm hai ngàn lẻ bốn | năm 2004 |
| một ngàn chín trăm chín mươi sáu | 1996 |
| năm hai ngàn | năm 2000 |
| chín trăm chín mươi sáu | 996 |
| mười ngày | 10 ngày |
| sáu lần | 6 lần |
| năm lần | 5 lần |
| một giây | 1 giây |
| một con | 1 con |
| hàng trăm mét | hàng trăm mét |
| hàng triệu con | hàng triệu con |
| hàng ngàn con | hàng ngàn con |
| vài phần nghìn giây | vài phần nghìn giây |
| vài phần nghìn xăng-ti-mét | vài phần nghìn cm |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · 10 QUÁI KIỆT MỚI BƯỚC VÀO ĐẤU TRƯỜNG VŨ KHÍ · 261.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.3 (7.3s) | L01 | Bóng tối bao trùm lấy một đấu trường La Mã khổng lồ giữa lòng rừng già đại ngàn... Mười chiếc bục thi đấu bọc thép đứng im lìm trong màn sương đêm kỳ |  | Toàn cảnh đấu trường La Mã hoạt hình khổng lồ chìm trong màn sương đêm kỳ bí, mười chiếc bục tròn phát sáng bao quanh một bục vinh quang trung tâm; KHÔNG có anh MC trong cảnh này. |
| b02 | 00:07.3–00:14.2 (6.9s) | L02 | bí. Và ở chính giữa đấu trường, một chiếc vương miện vàng nạm đá quý lấp lánh đang xoay tròn trên bệ đá cẩm thạch, chờ đợi chủ nhân xứng đáng |  | Cận cảnh chiếc vương miện vàng nạm ngọc phát ra những tia sáng vàng rực rỡ trên bệ đá cẩm thạch giữa sân; KHÔNG có anh MC trong cảnh này. |
| b03 | 00:14.2–00:20.9 (6.7s) | L03 | nhất. Đêm nay, mười sinh vật kỳ dị từ Tập 11 đến Tập 20 của kênh Vẽ Chuyện Hoang Dã sẽ chính thức hội tụ trên cùng một sàn đấu sinh |  | Mười chiếc bóng đen bí ẩn của 10 con vật (Gấu Trúc, Hà Mã, Lười, Tu Hú, Capybara, Tôm Súng, Lươn Điện, Bọ Pháo Thủ, Quỷ Gai, Cá Cung Thủ) xuất hiện tại cửa hầm; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:20.9–00:27.2 (6.3s) | L04 | tử! Không phải để kể lại những gì khán giả đã xem, mà để đọ sức trực tiếp bằng hàng loạt phát hiện khoa học mới toanh chưa từng |  | Mười đôi mắt hoạt hình rực sáng trong bóng tối với đủ thần thái: ngầu, tinh quái, điềm đạm, lờ đờ và hừng hực lửa chiến; KHÔNG có anh MC trong cảnh này. |
| b05 | 00:27.2–00:34.9 (7.6s) | L05 | tiết lộ! Mỗi loài mang theo một bí mật tiến hóa dị thường mà ngay cả những nhà sinh vật học lão luyện nhất cũng phải ngỡ ngàng bật ngửa. |  | Những biểu tượng vũ khí phát sáng lơ lửng quanh cửa hầm: tia sét xanh, ngọn lửa đỏ, giọt nước áp suất, gai bọc thép và chiếc cúp vinh quang; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:34.9–00:40.4 (5.5s) | L06 | Bật toàn bộ đèn pha! Chào mừng toàn thể muôn loài muôn thú đã đến với Đại Hội Sinh Tồn Mùa 2! |  | Dàn đèn pha công suất lớn rọi sáng rực rỡ toàn bộ đấu trường, pháo hoa nổ tung trên bầu trời đêm; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vest đỏ tươi giơ micro vàng nở nụ cười rạng rỡ. |
| b07 | 00:40.4–00:47.8 (7.4s) | L07 | Tôi là người dẫn chương trình đêm nay, và tôi xin cam kết danh dự: tất cả những gì bạn sắp nghe đều là những công trình nghiên cứu mới hoàn toàn! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đặt tay lên ngực cam kết, phía sau là màn hình lớn chiếu biểu tượng các tạp chí khoa học uy tín (không chữ). |
| b08 | 00:47.8–00:55.5 (7.7s) | L08 | Từ việc Gấu Trúc tắm phân ngựa để chống rét, cho tới Cá Cung Thủ nhớ được 44 khuôn mặt người hay Tôm Súng bắn ra dòng plasma dưới đáy biển! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng nháy mắt hóm hỉnh, tay kia giơ tập tài liệu dày cộm có hình bánh răng và tia sét; khán đài thú rừng vẫy cờ reo hò náo nhiệt. |
| b09 | 00:55.5–01:03.6 (8.1s) | L09 | Luật chơi Mùa 2 vô cùng khốc liệt: tám vòng thi đấu chính thức, xen kẽ giờ giải lao hậu trường, lễ trao giải phụ và vòng phúc khảo tin đồn thế kỷ. |  | tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) hiện lên giữa sân với 8 ô thử thách: năng lượng, xạ thủ, chống chịu, tiêu hóa, bầy đàn, hành trình, phúc khảo và món quà nhân loại. |
| b10 | 01:03.6–01:11.4 (7.8s) | L10 | Mỗi vòng thi, ban giám khảo trao ba tấm huy chương: Vàng được 3 điểm, Bạc 2 điểm, và Đồng 1 điểm. Riêng Vòng Chung Kết sẽ được nhân đôi điểm số! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ ngồi ở bàn giám khảo trên cao gõ búa gỗ, trước mặt là khay nhung đỏ bày ba chiếc huy chương vàng, bạc, đồng sáng loáng. |
| b11 | 01:11.4–01:18.1 (6.7s) | L11 | Giám khảo xin nhắc nhở: cấm nã đạn vào bảng điểm, cấm phóng điện vào ghế ban tổ chức và cấm đi vệ sinh giữa sân đấu! |  | Cận cảnh bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ cúi đầu nhìn qua gọng kính tròn, vẻ mặt nghiêm nghị đưa cánh ra lệnh chỉ đạo. |
| b12 | 01:18.1–01:24.3 (6.2s) | L12 | Nghe rõ chưa các đấu sĩ? Nhất là anh chàng Hà Mã và cô nàng Bọ Pháo Thủ đang cười tủm tỉm đằng kia! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng liếc nhìn sang chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ và chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C đang giả vờ huýt sáo ngây thơ vô số tội. |
| b13 | 01:24.3–01:30.2 (5.9s) | L13 | Bây giờ, xin mời toàn thể khán đài cùng chào đón sự xuất hiện của mười tuyển thủ tinh nhuệ nhất Mùa 2 trên thảm đỏ! |  | Cửa đường hầm mở toang, ánh đèn flash chớp sáng liên hồi, khói lạnh cuồn cuộn thổi qua lối đi chính; KHÔNG có anh MC trong cảnh này. |
| b14 | 01:30.2–01:34.9 (4.7s) | L14 | Tuyển thủ số một! Thiện xạ đầm lầy sở hữu bộ não tính toán quang học không cần vỏ não! Cá |  | chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn bơi lượn trong một bồn nước di động trong suốt, đôi mắt lồi đảo quanh quét tìm mục tiêu khoe tài; KHÔNG có anh MC trong cảnh này. |
| b15 | 01:34.9–01:39.9 (5.0s) | L15 | Cung Thủ! Tuyển thủ số hai! Chiến binh sa mạc Úc mặc áo giáp chông sắt và hút ẩm từ cát khô! Thằn Lằn Quỷ |  | chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm đội mũ safari kaki lạch bạch bước ra thảm đỏ, toàn thân phủ kín hàng trăm chiếc gai nón nhọn hoắt oai phong; KHÔNG có anh MC trong cảnh này. |
| b16 | 01:39.9–01:44.9 (5.0s) | L16 | Gai! Tuyển thủ số ba! Siêu pháo thủ tí hon chỉ dài bằng đốt ngón tay nhưng truyền cảm hứng cho động cơ tên lửa! Bọ |  | chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C bước ra, sau đuôi bốc lên một làn khói trắng nghi ngút từ nòng pháo mini cực ngầu; KHÔNG có anh MC trong cảnh này. |
| b17 | 01:44.9–01:49.7 (4.8s) | L17 | Pháo Thủ! Tuyển thủ số bốn! Cỗ máy phát điện sống biết hợp tác săn mồi theo bầy đàn hơn 100 con! Lươn Điện! |  | chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh uốn lượn trong bể nước kính cường lực, thân phát ra những tia điện xanh neon chói lòa; KHÔNG có anh MC trong cảnh này. |
| b18 | 01:49.7–01:54.5 (4.7s) | L18 | Tuyển thủ số năm! Thủ lĩnh đội quân tôm lính sống trong tổ bọt biển dưới quyền một Tôm Chúa! Tôm Súng! |  | chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa giơ chiếc càng búng khổng lồ to bằng nửa thân hình lên trời, đeo kính ngắm bắn tỉa cực kỳ tự tin; KHÔNG có anh MC trong cảnh này. |
| b19 | 01:54.5–02:00.3 (5.9s) | L19 | Tuyển thủ số sáu! Quý ngài ngoại giao Pantanal nuôi con chung bình đẳng và ngủ ngâm mình dưới lòng sông! Capybara! |  | chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia đội chiếc mũ phớt đen mafia thong thả bước ra, mắt híp tịt điềm đạm trước rừng ống kính phóng viên; KHÔNG có anh MC trong cảnh này. |
| b20 | 02:00.3–02:06.5 (6.2s) | L20 | Tuyển thủ số bảy! Kẻ cải trang thành chim ưng để đánh lừa hàng xóm và bay vòng tròn 16.000km mỗi năm! Chim Tu |  | chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái bay lượn sà xuống mép bục, nơ tím than lịch lãm, mắt đỏ nhấp nháy nhếch mép láu cá; KHÔNG có anh MC trong cảnh này. |
| b21 | 02:06.5–02:12.4 (5.9s) | L21 | Hú! Tuyển thủ số tám! Chú gấu lười rừng mưa mang cả vườn nấm tiêu diệt tế bào ung thư trên từng sợi lông! Con Lười! |  | chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini được một nhân viên kéo trên chiếc xe lăn phủ rêu xanh, một tay giơ lên chào khán giả với tốc độ cực chậm; KHÔNG có anh MC trong cảnh này. |
| b22 | 02:12.4–02:18.4 (6.0s) | L22 | Tuyển thủ số chín! Người vận chuyển hàng tạ nguyên tố Silicon cho các dòng sông lớn tại châu Phi! Hà Mã! |  | chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ bước ra làm rung chuyển mặt sàn, đeo đai lưng đỏ vô địch, ngoác miệng khoe cặp răng nanh khổng lồ; KHÔNG có anh MC trong cảnh này. |
| b23 | 02:18.4–02:24.4 (5.9s) | L23 | Và tuyển thủ số mười... xin mời quý vị nhìn lên màn hình vì bạn ấy đang bận trồng cây chuối bên ngoài sân vận động! |  | chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu đang chổng ngược hai chân sau lên thân cây bằng hai tay trước để đánh dấu mùi, mặt tròn xoe ngơ ngác quay lại nhìn ống kính; KHÔNG có anh MC trong cảnh này. |
| b24 | 02:24.4–02:29.2 (4.8s) | L24 | Ơ... tới lượt em đi vào rồi hả? Đợi em tụt xuống nhặt nốt nhánh trúc đã nha anh MC ơi! |  | Cận cảnh chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu lộn một vòng rơi bịch xuống đất, ôm cọng tre chạy lạch bạch lên sân khấu đáng yêu; KHÔNG có anh MC trong cảnh này. |
| b25 | 02:29.2–02:36.7 (7.5s) | L25 | Rồi, đủ mười thành viên tinh anh! Và theo nghi thức truyền thống của Đại Hội Sinh Tồn, mời cả mười đấu sĩ tiến vào khu vực Lễ Cân Ký Đo Đạc! |  | Chiếc bàn cân điện tử khổng lồ giữa đấu trường sáng đèn, các nhân viên kỹ thuật đeo găng tay chuẩn bị ghi chép; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cầm micro đứng bên cạnh. |
| b26 | 02:36.7–02:43.6 (6.9s) | L26 | Hà Mã bước lên đầu tiên! Rầm! Mặt sàn rung bần bật! Hơn 3 tấn trọng lượng đè nặng xuống bàn cân thép chịu lực! Tuyển thủ nặng ký nhất giải đấu! | **3 TẤN** · Hà Mã nặng nhất · R/380 · [0.72, 0.45] | chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ đứng lên cân, chiếc cân lún xuống kêu răng rắc, màn hình điện tử hiện số đỏ chót nhấp nháy; KHÔNG có anh MC trong cảnh này. |
| b27 | 02:43.6–02:48.8 (5.2s) | L27 | Tiếp theo là Gấu Trúc Lớn: 110kg cơ bắp và mỡ dự phòng, dù nhìn bề ngoài trông chỉ toàn bông gòn! |  | chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu ngồi phịch lên bàn cân, ôm chặt bó tre xanh ngơ ngác nhìn con số điện tử nhảy vọt qua mốc một trăm; KHÔNG có anh MC trong cảnh này. |
| b28 | 02:48.8–02:54.8 (6.0s) | L28 | Bố Già Capybara bước lên với phong thái điềm đạm tuyệt đối: 65kg! Chuột gặm nhấm lớn nhất hành tinh hiện nay! | **65KG** · Chuột lớn nhất · L/380 · [0.38, 0.78] | chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia bước lên cân với phong thái quý ông điềm đạm, màn hình hiện số 65kg, anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vỗ vai thán phục; KHÔNG có anh MC trong cảnh này. |
| b29 | 02:54.8–03:03.0 (8.2s) | L29 | Lươn Điện dài 2m nặng 20kg trườn lên bàn cân thủy tinh; kế bên là Con Lười nặng 4kg nhưng 1/3 trọng lượng nằm ở bụng lá cây chưa tiêu hóa! |  | Hai chiếc cân nhỏ hơn: chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh uốn mình trong bể cân 20kg, chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini treo ngược vào khung cân chớp mắt lờ đờ; KHÔNG có anh MC trong cảnh này. |
| b30 | 03:03.0–03:10.3 (7.3s) | L30 | Nhóm hạng lông tiếp tục lên sàn: Chim Tu Hú nặng chỉ 110g, Thằn Lằn Quỷ Gai vỏn vẹn 40g, và Cá Cung Thủ 200g! |  | Ba tuyển thủ đứng trên đĩa cân điện tử chính xác cao: chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái, chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm và chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu n |
| b31 | 03:10.3–03:19.1 (8.8s) | L31 | Cuối cùng là hai gã tí hon Tôm Súng và Bọ Pháo Thủ! Cân thông thường không thể đo nổi, ban tổ chức phải dùng cân phân tích hóa học trong lồng kính kín gió! |  | Nhân viên đặt chiếc đĩa siêu nhỏ vào lồng kính thí nghiệm nơi chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C dài chưa tới hai phân và chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa dài 4cm đang đứng nghiêm; KHÔNG có anh MC trong cảnh này. |
| b32 | 03:19.1–03:27.0 (7.9s) | L32 | Bọ Pháo Thủ chỉ nặng chưa đầy nửa gam! Tức là Hà Mã nặng gấp... 6.000.000 lần Bọ Pháo Thủ! Sự chênh lệch này khiến máy tính của ban tổ chức suýt bốc khói! |  | Bảng so sánh hoạt hình: một bên là chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ to như ngọn núi, một bên là chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C nhỏ như đầu bút bi; nhân viên kỹ thuật ôm đầu kinh ngạc; KHÔNG có anh MC trong cảnh này. |
| b33 | 03:27.0–03:34.0 (7.0s) | L33 | Sau lễ cân ký, giới cá cược và chuyên gia phân tích đồng loạt đặt cửa vô địch cho ba gã khổng lồ hỏa lực: Tôm Súng, Lươn Điện và Hà Mã! |  | Màn hình chiếu cột dự đoán: ba cột cao vút gắn hình đầu chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa, chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh, chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh  |
| b34 | 03:34.0–03:41.3 (7.2s) | L34 | Còn Bọ Pháo Thủ nửa gam và Con Lười chậm chạp? Các chuyên gia ghi một dòng ngắn gọn: chỉ mong hai bạn đi hết được vòng gửi xe! |  | Các cột dự đoán thấp lè tè gắn hình chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C và chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini, chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C cau mày giơ nắm |
| b35 | 03:41.3–03:47.7 (6.5s) | L35 | Nhưng đừng bao giờ coi thường sức mạnh ẩn giấu của những kẻ nhỏ bé! Đêm nay, từng định kiến sẽ bị lật tung bằng những dữ liệu khoa học xác |  | Cận cảnh ánh mắt lóe sáng kiên định của chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C và chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini, ngọn lửa nhiệt huyết bùng cháy trong từng cử chỉ; KHÔNG có anh MC trong cảnh này. |
| b36 | 03:47.7–03:55.0 (7.3s) | L36 | thực nhất! Tám vòng thi đấu! 100% dữ liệu mới! Chỉ có trí tuệ tiến hóa thực sự mới đủ sức chạm tay vào chiếc vương miện Mùa 2! |  | Chiếc vương miện vàng tỏa sáng chói lòa ở trung tâm đấu trường, mười cái bóng đổ dài hướng về phía đỉnh vinh quang; KHÔNG có anh MC trong cảnh này. |
| b37 | 03:55.0–04:01.0 (6.0s) | L37 | Khoan đã, trước khi vào vòng một, hãy cùng nghe nhận xét nhanh từ tổ trọng tài kỹ thuật về dàn đấu sĩ năm nay! |  | Tổ trọng tài gồm bác sĩ khám nghiệm, kỹ sư vũ khí và phóng viên 24 giờ cùng đứng quanh bàn thiết bị đo đạc tối tân; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng tiến tới phỏng vấn. |
| b38 | 04:01.0–04:07.9 (6.9s) | L38 | Báo cáo MC: toàn bộ các cảm biến áp suất, đồng hồ đo vôn kế 1.000V và máy chụp CT đều đã được hiệu chuẩn ở mức an toàn tuyệt đối! |  | Cô trợ lý phòng thí nghiệm giơ bảng kẹp hồ sơ kiểm tra các nút bấm nhấp nháy xanh trên bàn điều khiển; KHÔNG có anh MC trong cảnh này. |
| b39 | 04:07.9–04:15.8 (7.9s) | L39 | Tuyệt vời! Còn các tuyển thủ thì sao? Tôm Súng đang khởi động khớp lò xo càng súng lách tách, trong khi Hà Mã đang há miệng kiểm tra lại cặp răng nanh! |  | chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa bóp nhẹ chiếc càng khổng lồ kêu cạch cạch làm tia nước bắn tung tóe; chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ ngáp một cái rộng 150 độ khoe răng nanh sắc nhọn; KHÔNG có anh MC trong cảnh này. |
| b40 | 04:15.8–04:21.9 (6.0s) | L40 | Không chần chừ thêm 1 giây nào nữa! Chúng ta hãy cùng tiến vào Vòng một ngay bây giờ: Năng lượng và cấu tạo kỳ dị! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vung micro chỉ thẳng về phía cổng đấu trường nơi các máy quét cấu trúc sinh học và tia laser đang rực sáng đón chờ. |

### scene02 · CẤU TẠO KỲ DỊ VÀ NGUỒN NĂNG LƯỢNG BÍ MẬT BÊN TRONG CƠ THỂ · 267.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:10.9 (10.9s) | L41 | Chào mừng toàn thể khán đài bước vào Vòng một: Giải mã cấu tạo ẩn giấu và nguồn năng lượng sinh học! Ở vòng mở màn này, chúng ta không thi chạy hay cắn nhau, mà đưa các tuyển thủ vào máy quét công nghệ cao! |  | Sân đấu biến thành một trung tâm nghiên cứu công nghệ cao với các máy chụp cắt lớp vi tính CT, camera nhiệt hồng ngoại và màn hình ADN; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đứng cạnh bảng thông số. |
| b02 | 00:10.9–00:18.0 (7.1s) | L42 | Ban giám khảo muốn biết: bộ máy bên trong cơ thể loài nào được thiết kế tinh vi, tiết kiệm hoặc tạo ra công suất năng lượng điên rồ nhất? |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ cầm chiếc thước kẹp và mô hình phân tử năng lượng phát sáng, trước mặt là ba chiếc huy chương đầu tiên của mùa giải. |
| b03 | 00:18.0–00:28.4 (10.3s) | L43 | Thí sinh đầu tiên bước vào máy quét 3D là pháo thủ đại dương Tôm Súng! Khán giả đều đã biết cú búng càng tạo sóng âm của nó, nhưng cấu tạo tạo ra plasma mới là điều làm các kỹ sư choáng váng! |  | chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa bước vào buồng quét laser, chiếc càng búng khổng lồ được phóng đại thành mô hình cơ khí 3D quay tròn trên màn hình lớn; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:28.4–00:35.3 (7.0s) | L44 | Năm 2019, nhóm kỹ sư cơ khí tại Đại học Texas A&M đã dùng tia X siêu nhỏ quét lớp vỏ lột xác của Tôm Súng để in 3D phóng đại gấp |  | Phòng thí nghiệm Đại học Texas A&M: hai kỹ sư mặc áo blouse trắng đặt chiếc càng tôm phóng đại 3D bằng nhựa vào bể nước thử nghiệm; KHÔNG có anh MC trong cảnh này. |
| b05 | 00:35.3–00:41.8 (6.4s) | L45 | 5 lần! Họ gắn một lò xo bẫy chuột để mô phỏng cơ bắp tôm búng càng! Kết quả thu được khiến cả giới vật lý plasma phải sững sờ kinh ngạc! |  | Mô hình càng in 3D đóng sập với tiếng kêu vang dội, một chùm tia plasma sáng rực kéo dài mười lăm phần tỷ giây lóe lên giữa lòng nước; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:41.8–00:50.4 (8.7s) | L46 | Chỉ bằng lực cơ học đơn thuần không cần dùng điện hay tia laser, thiết bị mô phỏng càng Tôm Súng đã tạo ra dòng plasma dưới nước với hiệu suất cao gấp 10 lần máy móc nhân tạo hiện đại! | **GẤP 10 LẦN** · Hiệu suất tạo plasma · R/380 · [0.66, 0.48] | Biểu đồ so sánh hiệu suất tạo plasma: cột máy laser và điện cực thấp lè tè, cột mô hình càng chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa vọt cao gấp 10 lần rực sáng; KHÔNG có anh MC trong cảnh này. |
| b07 | 00:50.4–00:58.8 (8.4s) | L47 | Nhưng điều thú vị hơn nằm ở chức năng dự phòng thiên tài của Tôm Súng! Điều gì xảy ra nếu trong một cuộc giao tranh nảy lửa, nó bị kẻ thù cắn gãy mất chiếc càng súng khổng lồ? |  | Hình minh họa chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa bị một con cá lớn đớp mất chiếc càng súng to bên phải, để lại phần khớp cụt ngủn đáng thương; KHÔNG có anh MC trong cảnh này. |
| b08 | 00:58.8–01:06.8 (8.0s) | L48 | Câu trả lời là: nó không hề bị tàn phế! Ngay sau khi mất chiếc càng súng bên phải, bộ gen của Tôm Súng lập tức kích hoạt cơ chế đảo ngược bất đối xứng! |  | Tín hiệu gen phát sáng từ trung tâm thần kinh chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa truyền tín hiệu sang chiếc càng nhỏ bên trái đang đứng bình thường; KHÔNG có anh MC trong cảnh này. |
| b09 | 01:06.8–01:17.7 (11.0s) | L49 | Chiếc càng nhỏ vốn chỉ dùng để gắp thức ăn bên tay trái sẽ phình to thần tốc sau vài lần lột xác, biến hình thành một khẩu đại bác súng nước mới toanh! Còn bên cụt cũ sẽ mọc lại một chiếc càng nhỏ thay thế! |  | Qua các chu kỳ lột xác, chiếc càng nhỏ bên trái của chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa lớn vọt lên thành càng súng khổng lồ, còn bên phải mọc ra càng nhỏ xinh xắn; KHÔNG có anh MC trong cảnh này. |
| b10 | 01:17.7–01:26.4 (8.6s) | L50 | Một dây chuyền tự đổi tay thuận và tái tạo vũ khí vĩnh cửu! Dù gãy súng bao nhiêu lần, Tôm Súng vẫn luôn có một khẩu đại bác dự phòng trong tay! |  | chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa giơ khẩu đại bác mới bên tay trái ngắm bắn bùm một phát đầy tự tin, cả khán đài vỗ tay rầm rộ; KHÔNG có anh MC trong cảnh này. |
| b11 | 01:26.4–01:34.0 (7.6s) | L51 | Và để kiểm tra thêm độ hiệu quả của cấu trúc cơ thể, các nhà nghiên cứu còn đưa thêm một thí sinh hạng trung vào buồng kiểm tra cấu trúc xương đặc biệt: Capybara! |  | chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia bước vào buồng quét cấu trúc giải phẫu cơ thể, màn hình hiện lên khung xương và hệ thống tuyến mồ hôi dưới da; KHÔNG có anh MC trong cảnh này. |
| b12 | 01:34.0–01:42.1 (8.1s) | L52 | Mặc dù sống quanh năm tại vùng đầm lầy nóng ẩm Nam Mỹ, Capybara lại sở hữu rất ít tuyến mồ hôi trên da nên không thể đổ mồ hôi làm mát như con người hay ngựa! |  | Kính hiển vi soi lên lớp da lông nâu thô của chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia: các tuyến mồ hôi thưa thớt gần như không đáng kể; KHÔNG có anh MC trong cảnh này. |
| b13 | 01:42.1–01:54.2 (12.1s) | L53 | Thay vì tốn nước đổ mồ hôi, cấu trúc bộ lông thưa cứng và lớp mỡ mỏng cho phép nhiệt lượng thoát ra cực nhanh ngay khi nó bước xuống ngâm mình trong làn nước mát! Một thiết kế làm mát bằng nước hoàn hảo cho gã khổng lồ gặm nhấm! |  | chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia ngâm nửa thân dưới làn nước xanh mát rượi, các mũi tên nhiệt màu đỏ bay vèo ra ngoài làm cơ thể hạ nhiệt tức thì; KHÔNG có anh MC trong cảnh này. |
| b14 | 01:54.2–02:00.2 (6.0s) | L54 | Giám khảo ghi nhận: cấu trúc cơ khí tạo plasma siêu việt và khả năng đổi tay vũ khí cực kỳ thông minh! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gật gù thán phục, gắn ngôi sao đánh dấu vào bảng chấm điểm cho chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa. |
| b15 | 02:00.2–02:11.6 (11.4s) | L55 | Tuyển thủ thứ hai bước vào buồng đo công suất năng lượng là Nhà Máy Điện Sống: Lươn Điện! Chúng ta đều biết con số đỉnh 860V, nhưng công suất điện thực tế và cơ chế bơm ion mới là kỳ quan sinh học! |  | chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh bơi vào bể đo công suất điện nối thẳng với một bảng bóng đèn khổng lồ và đồng hồ đo Ampe; KHÔNG có anh MC trong cảnh này. |
| b16 | 02:11.6–02:19.4 (7.8s) | L56 | Trong khoảnh khắc săn mồi, nguồn điện của Lươn Điện có thể đạt cường độ dòng điện xấp xỉ một Ampe, tức là công suất tức thời đạt mức tương đương hơn 800W! |  | Đồng hồ Ampe và Watt nhảy vọt đồng thời, dàn bóng đèn sân khấu sáng rực rỡ chỉ bằng nguồn năng lượng phát ra từ thân chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh; KHÔNG có anh MC trong cảnh này. |
| b17 | 02:19.4–02:26.8 (7.4s) | L57 | Làm thế nào 6.000 tế bào pin sinh học có thể xả hàng chục phát liên tiếp mà không bị cạn kiệt ngay lập tức? Bí mật nằm ở hệ thống bơm ion Natri và Kali siêu tốc! |  | Kính hiển vi điện tử soi vào màng tế bào electrocyte: hàng triệu kênh bơm ion Natri và Kali mở đóng nhịp nhàng như hàng triệu cánh cửa tự động; KHÔNG có anh MC trong cảnh này. |
| b18 | 02:26.8–02:35.9 (9.0s) | L58 | Ngay sau mỗi lần phóng điện, các bơm sinh hóa tiêu thụ phân tử năng lượng ATP lập tức vận chuyển ngược dòng hàng tỷ ion qua màng tế bào, tái nạp điện thế sẵn sàng chiến đấu chỉ trong tích tắc! |  | Thanh pin năng lượng bên cạnh chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh tụt xuống rồi vụt nạp đầy lại một trăm phần trăm màu xanh lá chỉ trong nháy mắt; KHÔNG có anh MC trong cảnh này. |
| b19 | 02:35.9–02:45.3 (9.4s) | L59 | Không cần dây cắm sạc, không cần pin lithium độc hại, toàn bộ quá trình sản xuất và tái nạp điện diễn ra bằng muối khoáng và nước ngọt ngay trong thớ thịt mềm mại của con cá! |  | Thân hình chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh phát sáng dịu nhẹ các mạch ion sinh học tự nhiên tuyệt đẹp, kỹ sư điện tử trên khán đài há hốc mồm kinh ngạc; KHÔNG có anh MC trong cảnh này. |
| b20 | 02:45.3–02:52.7 (7.5s) | L60 | Và bây giờ là bất ngờ gây sốc nhất Vòng một! Tuyển thủ thứ ba bước lên máy đo năng lượng là chú gấu tròn xoe suốt ngày chỉ biết ôm tre: Gấu Trúc Lớn! |  | chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu lạch bạch bước vào máy quét trao đổi chất, hai tay vẫn ôm khư khư một mầm trúc tươi vừa nhai vừa gãi đầu; KHÔNG có anh MC trong cảnh này. |
| b21 | 02:52.7–03:00.3 (7.6s) | L61 | Trong suốt nhiều thập kỷ, giới sinh học đau đầu tự hỏi: ăn một thứ thức ăn nghèo dinh dưỡng như tre với đường ruột ngắn ngủn của thú ăn thịt, tại sao Gấu Trúc không chết đói? |  | Một bác sĩ thú y hoạt hình cầm máy tính bấm liên hồi, nhìn chiếc ruột ngắn ngủn và đống tre khô mà vò đầu bứt tai khó hiểu; KHÔNG có anh MC trong cảnh này. |
| b22 | 03:00.3–03:07.7 (7.4s) | L62 | Năm 2015, nghiên cứu đột phá công bố trên tạp chí Science của nhóm tiến sĩ Yonggang Nie đã giải mã bí mật động trời ẩn sâu trong bộ gen của Gấu Trúc! |  | Trang bìa tạp chí Science năm 2015 hiện lên với sơ đồ chuỗi xoắn ADN phát sáng điểm đột biến màu đỏ rực ở gen DUOX2; KHÔNG có anh MC trong cảnh này. |
| b23 | 03:07.7–03:16.7 (9.0s) | L63 | Các nhà khoa học phát hiện Gấu Trúc sở hữu một đột biến độc nhất vô nhị trên gen DUOX2 — loại gen chịu trách nhiệm tổng hợp hormone tuyến giáp kiểm soát tốc độ đốt cháy năng lượng! |  | Sơ đồ tuyến giáp của chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu hiển thị con dấu khóa hãm công suất, mức hormone T4 giảm chỉ còn một nửa bình thường; KHÔNG có anh MC trong cảnh này. |
| b24 | 03:16.7–03:23.3 (6.6s) | L64 | Kết quả là mức độ hormone tuyến giáp T4 trong máu Gấu Trúc chỉ bằng 46,9% so với các loài thú có vú cùng kích thước! |  | Biểu đồ cột hormone: cột của chó sói và gấu nâu cao chót vót một trăm phần trăm, cột của chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu chỉ thấp gần một nửa; KHÔNG có anh MC trong cảnh này. |
| b25 | 03:23.3–03:32.8 (9.4s) | L65 | Không chỉ giảm hormone, tiến hóa còn thu nhỏ kích thước não bộ của Gấu Trúc đi 5% và kích thước quả thận đi 11% để cắt giảm tối đa chi phí vận hành cơ thể! |  | Hình ảnh cắt lớp X-quang nội tạng chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu: tim, thận và não đều chạy ở chế độ tiết kiệm điện siêu hạng; KHÔNG có anh MC trong cảnh này. |
| b26 | 03:32.8–03:44.4 (11.7s) | L66 | Tính tổng thể, mức tiêu hao năng lượng hàng ngày của Gấu Trúc hoang dã chỉ bằng 45% so với 1 con thú bình thường nặng bằng nó! Tức là nó sống bằng chưa tới một nửa bình xăng của loài khác! |  | chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu ngồi thư giãn với biểu tượng pin tiết kiệm năng lượng Eco màu xanh lá phát sáng trên bụng, vẫy tay chào đầy tự hào; KHÔNG có anh MC trong cảnh này. |
| b27 | 03:44.4–03:55.1 (10.6s) | L67 | Để kiểm chứng, các nhà khoa học đã cấy đúng đoạn đột biến gen này vào chuột thí nghiệm, và lũ chuột lập tức trở nên ít vận động hơn hẳn 55% y hệt phong thái của gấu trúc! |  | Đàn chuột thí nghiệm có gen gấu trúc nằm phơi bụng thư giãn không thèm chạy bánh xe tập thể dục, cả khán đài cười ồ thích thú; KHÔNG có anh MC trong cảnh này. |
| b28 | 03:55.1–04:04.4 (9.3s) | L68 | Vòng một kết thúc với kết quả thuyết phục tuyệt đối! Ban giám khảo xin công bố huy chương đồng thuộc về Gấu Trúc Lớn với đột biến gen DUOX2 tiết kiệm năng lượng thiên tài! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ bước ra đeo huy chương đồng lên cổ chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu đang ôm tre vui sướng; khán đài vỗ tay tán thưởng. |
| b29 | 04:04.4–04:14.2 (9.9s) | L69 | Huy chương bạc thuộc về Lươn Điện với hệ thống tái nạp ion siêu tốc! Và Huy chương vàng gọi tên Tôm Súng với công nghệ plasma vượt trội cùng cơ chế đổi tay súng dự phòng! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ trao huy chương bạc cho chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh và huy chương vàng lấp lánh cho chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa; tiếng pháo tay vang dội |
| b30 | 04:14.2–04:20.7 (6.4s) | L70 | Bảng tổng sắp sau Vòng một: Tôm Súng dẫn đầu với 3 điểm, Lươn Điện 2 điểm, và Gấu Trúc Lớn xuất sắc ghi điểm đồng đầu |  | tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) bừng sáng ba cột điểm đầu tiên của chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa, chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon l |
| b31 | 04:20.7–04:27.9 (7.2s) | L71 | tiên! Vòng hai ngay sau đây sẽ thử thách khả năng bắn tỉa tầm xa và trí tuệ quang học siêu phàm! Mời quý vị cùng hướng mắt về trường bắn! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng dẫn đầu đoàn tiến về trường bắn rừng ngập mặn nơi những tấm bia di động và các bài toán thị giác hóc búa đang chờ đón. |

### scene03 · XẠ THỦ TẦM XA VÀ TRÍ TUỆ THỊ GIÁC KHÔNG TƯỞNG · 285.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:11.0 (11.0s) | L72 | Chào mừng toàn thể quý vị đến với Vòng hai: Đấu trường xạ thủ tầm xa và trí tuệ thị giác siêu phàm! Ở vòng này, ban giám khảo không chỉ đo tầm bắn mà còn kiểm tra bộ não xử lý hình ảnh của các tuyển thủ! |  | Đấu trường chuyển sang khu rừng ngập mặn với những cành cây cao vươn ra mặt nước và hàng loạt camera tốc độ cao lắp đặt khắp nơi; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cầm micro quan sát. |
| b02 | 00:11.0–00:21.9 (10.9s) | L73 | Đấu sĩ mở màn là tay súng thiện xạ nổi tiếng nhất thế giới cá: Cá Cung Thủ! Khán giả đều đã nghe tài bắn tia nước tính khúc xạ ánh sáng của nó, nhưng thí nghiệm tại Đại học Oxford mới thực sự gây chấn động thế giới! |  | chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn bơi tiến vào bồn kính thử nghiệm, đối diện là một màn hình máy tính chống nước kỳ lạ chứ không phải côn trùng; KHÔNG có anh MC trong cảnh này. |
| b03 | 00:21.9–00:30.6 (8.7s) | L74 | Lâu nay giới khoa học thần kinh tin rằng chỉ những loài có vỏ não mới phát triển cao như con người, khỉ hay chim mới có khả năng phân biệt được khuôn mặt phức tạp của con người! |  | Sơ đồ bộ não người với vùng vỏ não mới neocortex phát sáng rực rỡ, đối chiếu với bộ não nhỏ xíu đơn giản của loài cá; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:30.6–00:37.9 (7.3s) | L75 | Cá hoàn toàn không có cấu trúc vỏ não mới này! Vậy liệu 1 con cá nhỏ bé ở đầm lầy có thể phân biệt được mặt người này với mặt người khác hay không? |  | Màn hình thí nghiệm chiếu ảnh hai khuôn mặt người đặt cạnh nhau trước mặt chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn, các nhà khoa học hồi hộp theo dõi; KHÔNG có anh MC trong cảnh này. |
| b05 | 00:37.9–00:45.4 (7.5s) | L76 | Năm 2016, tiến sĩ Cait Newport tại Đại học Oxford và Đại học Queensland đã công bố nghiên cứu chấn động trên tạp chí Scientific Reports! |  | Trang bìa tạp chí Scientific Reports năm 2016 hiện rõ tên thí nghiệm trên loài Cá Cung Thủ Toxotes chatareus; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:45.4–00:53.5 (8.1s) | L77 | Nhóm nghiên cứu huấn luyện Cá Cung Thủ nhận diện một khuôn mặt người mục tiêu để nhận thưởng thức ăn, sau đó trộn lẫn khuôn mặt đó vào giữa 44 khuôn mặt người lạ hoàn toàn khác | **44 MẶT** · Thử nghiệm nhận diện · L/380 · [0.42, 0.3] | Màn hình hiển thị ma trận 44 bức ảnh khuôn mặt người đa dạng kích cỡ và đường nét phía trên mặt nước bể cá; KHÔNG có anh MC trong cảnh này. |
| b07 | 00:53.5–01:03.6 (10.0s) | L78 | nhau! Kết quả làm toàn bộ giới khoa học thần kinh sững sờ: Cá Cung Thủ phun tia nước trúng phóc bức ảnh khuôn mặt quen thuộc với độ chính xác trung bình từ 81 đến 86%! |  | chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn ngắm kỹ và bắn tia nước chuẩn xác trúng ngay khuôn mặt mục tiêu giữa rừng ảnh người, biểu đồ tỷ lệ chính xác vọt lên 86%; KHÔNG có anh MC trong cảnh này. |
| b08 | 01:03.6–01:12.0 (8.5s) | L79 | Thậm chí khi các nhà khoa học chuyển toàn bộ ảnh sang màu đen trắng, đồng bộ độ sáng và cắt bỏ hết kiểu tóc lẫn đường viền đầu, chú cá vẫn nhận ra gương mặt đó không chút sai sót! |  | Những bức ảnh khuôn mặt đen trắng bị cắt tròn đều giống hệt nhau, chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn vẫn không hề bối rối mà bắn trúng ngay lập tức; KHÔNG có anh MC trong cảnh này. |
| b09 | 01:12.0–01:20.1 (8.1s) | L80 | Quý vị thử tưởng tượng xem: 1 con cá dài một gang tay không có vỏ não nhận dạng lại nhớ mặt người giỏi hơn cả nhiều ứng dụng camera an ninh cũ kỹ! |  | Một nhân vật hoạt hình mặc áo sọc đeo mặt nạ hài hước đi ngang qua bể cá thì bị chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn nhận ra mặt lạ rồi phun tia nước vào mặt khiến nhân vật giật mình hài hước, khán giả cười ồ; KHÔNG có anh MC trong cảnh này. |
| b10 | 01:20.1–01:27.6 (7.5s) | L81 | Chưa dừng lại ở đó, khi bắn mồi thật trên cành cây, Cá Cung Thủ còn tự động đo trọng lượng của con mồi để điều chỉnh thể tích tia nước bắn ra! |  | So sánh hai phát bắn: với con kiến nhỏ nó bắn tia nước mảnh nhẹ nhàng, với con bọ cánh cứng nặng cân nó nén khối nước to gấp nhiều lần; KHÔNG có anh MC trong cảnh này. |
| b11 | 01:27.6–01:36.3 (8.7s) | L82 | Nó kiểm soát sự bất ổn định thủy động lực học khi nén dòng nước, tụ toàn bộ năng lượng vào mũi đạn tạo ra lực va chạm lớn hơn lực bám chân của côn trùng tới mười lần! |  | Hình ảnh phóng đại tia nước đang bay biến thành một đầu đạn thủy lực tròn đặc, đập bật chú bọ cứng đầu rơi thẳng xuống nước; KHÔNG có anh MC trong cảnh này. |
| b12 | 01:36.3–01:44.2 (7.9s) | L83 | Không chỉ nhớ được 44 khuôn mặt ở góc nhìn thẳng, thí nghiệm nâng cao của Đại học Oxford còn thử xoay nghiêng các bức ảnh khuôn mặt theo nhiều góc độ khác nhau! |  | Các bức ảnh khuôn mặt trên màn hình máy tính xoay nghiêng sang trái phải ba mươi độ, chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn bơi nghiêng đầu quan sát chăm chú; KHÔNG có anh MC trong cảnh này. |
| b13 | 01:44.2–01:56.3 (12.1s) | L84 | Kết quả đáng kinh ngạc: Cá Cung Thủ vẫn nhận diện chính xác người quen qua từng góc nghiêng mà không hề bị đánh lừa! Điều này chứng tỏ thị giác của loài cá này giải mã không gian 3D phức tạp hơn ta tưởng rất nhiều! |  | chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn bắn tia nước trúng phóc bức ảnh xoay nghiêng, đèn xanh báo hiệu kết quả đúng nhấp nháy rực rỡ; KHÔNG có anh MC trong cảnh này. |
| b14 | 01:56.3–02:02.8 (6.5s) | L85 | Giám khảo ghi nhận: bộ não xử lý thị giác của Cá Cung Thủ là một kiệt tác vượt xa mọi giới hạn kích thước não bộ! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ đeo kính gật gù thán phục, ghi điểm tuyệt đối vào bảng thi cho chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn. |
| b15 | 02:02.8–02:11.1 (8.3s) | L86 | Tuyển thủ thứ hai bước vào bài thi bắn tỉa là pháo thủ tí hon: Bọ Pháo Thủ! Nếu Cá Cung Thủ bắn tỉa bằng tia nước lạnh, thì Bọ Pháo Thủ là chuyên gia điều áp và nổ xung phản lực vi |  | chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C tiến lên bục thử nghiệm tốc độ cao, các cảm biến áp suất và camera nhiệt chĩa thẳng vào chóp bụng có nòng súng của chú bọ; KHÔNG có anh MC trong cảnh này. |
| b16 | 02:11.1–02:18.6 (7.5s) | L87 | mô! Quý vị đã biết nhiệt độ tia hóa chất của nó sôi 100°C, nhưng điều gì tạo ra lực đẩy mạnh mẽ mà không làm vỡ nòng súng chỉ rộng vài phần nghìn cm? |  | Mặt cắt ngang nòng súng siêu nhỏ của chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C phóng đại hàng ngàn lần dưới kính hiển vi điện tử quét; KHÔNG có anh MC trong cảnh này. |
| b17 | 02:18.6–02:27.3 (8.8s) | L88 | Theo nghiên cứu mô phỏng thủy động lực học tại Đại học Leeds, bí mật nằm ở quá trình sôi chớp nhoáng bên trong buồng đốt nhỏ xíu: hơi nước chiếm tới hơn 90% thể tích khí thoát |  | Sơ đồ buồng đốt với các bọt hơi nước sôi giãn nở tức thời chiếm hơn 90% thể tích, tạo áp suất đẩy luồng sương lao vọt ra ngoài; KHÔNG có anh MC trong cảnh này. |
| b18 | 02:27.3–02:38.5 (11.2s) | L89 | ra! Áp suất chỉ cần tăng nhẹ khoảng 100 mbar là đủ tống toàn bộ hỗn hợp hóa chất sôi ra ngoài với vận tốc từ 12-35m mỗi giây, xé nhỏ thành hàng tỷ hạt sương đường kính chỉ từ 1-500 |  | Dải hạt sương hóa chất siêu mịn phun ra ở tốc độ 35 m/s tạo thành một bức tường hơi nóng bỏng rát bao phủ toàn bộ mục tiêu; KHÔNG có anh MC trong cảnh này. |
| b19 | 02:38.5–02:48.6 (10.1s) | L90 | μm! Nhờ tháp pháo đuôi có khớp xoay linh hoạt 270°, chú bọ tí hon có thể vừa chạy trốn vừa bắn chuẩn xác vào mắt những kẻ săn mồi đang truy đuổi phía sau lưng mà không cần ngoái đầu nhìn lại! |  | chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C chạy hết tốc lực về phía trước nhưng nòng pháo quay ngược ra sau bắn trúng phóc mũi chú bọ ngựa khổng lồ đang đuổi theo; KHÔNG có anh MC trong cảnh này. |
| b20 | 02:48.6–02:54.9 (6.3s) | L91 | Và tuyển thủ thứ ba của vòng hai mang đến một tuyệt kỹ đánh lừa thị giác đỉnh cao không cần dùng đến một giọt đạn nào: Chim Tu Hú! |  | chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái sải cánh bay lượn trên khu vực thử nghiệm thị giác, phía dưới là hàng chục mô hình chim chích đang ngồi canh tổ; KHÔNG có anh MC trong cảnh này. |
| b21 | 02:54.9–03:04.0 (9.1s) | L92 | Khán giả đều đã nghe chuyện Tu Hú đẻ trộm trứng trong 10 giây, nhưng tại sao 1 con chim to xác như Tu Hú lại có thể bình yên bay lượn sát tổ chim chủ mà không bị bầy chim nhỏ xúm vào mổ đuổi đi? |  | Một chú chim chích nhỏ ngước nhìn lên bầu trời thấy bóng chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái bay tới, bỗng nhiên toàn thân run lẩy bẩy tụt sâu xuống đáy tổ nấp kín; KHÔNG có anh MC trong cảnh này. |
| b22 | 03:04.0–03:12.6 (8.7s) | L93 | Năm 2000 11, giáo sư Welbergen và Davies công bố phát hiện thú vị trên tạp chí Behavioral Ecology về chiến thuật ngụy trang Batesian kép của Chim Tu Hú! |  | Bức ảnh so sánh hai loài chim đặt cạnh nhau: bên trái là Chim Ưng Sẻ ăn thịt hung dữ, bên phải là chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái trưởng thành có bộ lông giống hệt; KHÔNG có anh MC trong cảnh này. |
| b23 | 03:12.6–03:22.6 (9.9s) | L94 | Từ hình dáng cánh nhọn, kiểu bay lướt gió cho đến những dải lông vằn ngang màu nâu xám trước ngực và chân vàng, Chim Tu Hú trưởng thành đã tiến hóa ngoại hình giống hệt... Chim Ưng Sẻ ăn thịt! |  | Phóng đại họa tiết lông ngực vằn ngang của chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái và chim ưng sẻ, đường nét trùng khớp đến từng chi tiết đánh lừa thị giác; KHÔNG có anh MC trong cảnh này. |
| b24 | 03:22.6–03:32.3 (9.8s) | L95 | Khi chim chủ nhà nhìn thấy bộ ngực vằn ngang đó lướt qua, chúng lập tức hoảng loạn tưởng là kẻ săn mồi hung tợn nên bay đi trốn giữ mạng thay vì ở lại tấn công kẻ lạ mặt! |  | Các chú chim sẻ cuống cuồng chui tọt vào bụi rậm trốn, để lại chiếc tổ trống không cho chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái thong thả đáp xuống thực hiện phi vụ dễ như trở bàn tay; KHÔNG có anh MC trong cảnh này. |
| b25 | 03:32.3–03:43.3 (10.9s) | L96 | Thậm chí các nhà khoa học thử dùng sơn che đi các vạch vằn trên ngực mô hình Tu Hú, lập tức đàn chim chích trở nên hung hãn lao vào đánh đuổi túi bụi! Một màn cải trang cảnh sát chìm ngoạn mục của giới loài chim! |  | Mô hình Tu Hú bị che vạch ngực bị bầy chim sẻ xúm lại mổ rụng lông tơi tả, còn mô hình giữ nguyên vạch ngực lại khiến cả xóm chim im thin thít; KHÔNG có anh MC trong cảnh này. |
| b26 | 03:43.3–03:50.9 (7.6s) | L97 | Thêm một màn đọ tài gay cấn nữa ở bài kiểm tra thị giác mà anh MC xin bổ sung giữa hai sát thủ bắn tỉa dưới nước: Cá Cung Thủ và Lươn Điện! |  | Màn hình chia đôi: một bên là chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn bơi dưới mặt nước gợn sóng lăn tăn, một bên là chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh lượn quanh các vật cản nhựa và kim loại; KHÔNG có anh MC trong cản |
| b27 | 03:50.9–04:01.8 (10.9s) | L98 | Trong tự nhiên, mặt nước đâu phải lúc nào cũng phẳng lặng như gương! Các thí nghiệm chứng minh Cá Cung Thủ vẫn bắn trúng đích ngay cả khi mặt nước đang gợn sóng liên tục nhờ khả năng cập nhật góc lệch theo thời gian |  | chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn ngắm bắn xuyên qua những gợn sóng lăn tăn trên mặt hồ và vẫn bắn rơi trúng phóc con bọ đậu trên cành cây; KHÔNG có anh MC trong cảnh này. |
| b28 | 04:01.8–04:11.3 (9.5s) | L99 | thực! Còn Lươn Điện thì dùng trường điện áp thấp 10V để phân biệt rạch ròi đâu là một thanh nhựa cách điện vô tri, đâu là 1 con cá thật đang thở thoi thóp dưới lớp bùn đặc! |  | chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh lượn qua thanh nhựa bỏ đi không thèm để ý, lập tức dừng lại khóa mục tiêu vào chú cá đang trốn sau hòn đá; KHÔNG có anh MC trong cảnh này. |
| b29 | 04:11.3–04:19.2 (7.8s) | L100 | Kết quả Vòng hai đã được chốt! Huy chương đồng thuộc về Chim Tu Hú với màn cải trang thành Chim Ưng Sẻ đánh lừa cả xóm chim chủ! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ trao huy chương đồng cho chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái đang khoe bộ lông ngực vằn ngang lịch lãm; khán đài gật gù thán phục. |
| b30 | 04:19.2–04:28.6 (9.4s) | L101 | Huy chương bạc thuộc về Bọ Pháo Thủ với vòi phun sương tốc độ 35m mỗi giây! Và Huy chương vàng thuộc về Cá Cung Thủ với siêu năng lực nhận diện 44 khuôn mặt người! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ trao huy chương bạc cho chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C và huy chương vàng lấp lánh cho chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn; tiếng r |
| b31 | 04:28.6–04:39.4 (10.8s) | L102 | Bảng tổng sắp cập nhật điểm số sau hai vòng: Tôm Súng và Cá Cung Thủ đồng dẫn đầu với 3 điểm! Bọ Pháo Thủ bám sát với 2 điểm! Lươn Điện 2 điểm, Gấu Trúc 1 điểm, Tu Hú 1 điểm! |  | tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) sáng rực các cột điểm: cuộc đua giữa các siêu xạ thủ và cỗ máy năng lượng đang nóng lên từng phút! |
| b32 | 04:39.4–04:45.4 (6.0s) | L103 | Vòng ba ngay sau đây sẽ thử thách khả năng sinh tồn trước thời tiết khắc nghiệt và những giải pháp chống chọi thiên nhiên kỳ quặc nhất! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vung tay dẫn đường sang khu vực thử nghiệm khí hậu nơi bão tuyết băng giá và nắng nóng sa mạc đang cùng lúc gầm rú. |

### scene04 · CHỐNG CHỊU THỜI TIẾT KHẮC NGHIỆT — TẮM PHÂN NGỰA, HÚT CÁT ẨM VÀ TREO NỘI TẠNG · 281.6s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:10.7 (10.7s) | L104 | Chào mừng quý vị đến với Vòng ba: Thử thách chống chịu thời tiết cực hạn! Sân vận động lúc này được chia thành hai nửa đối lập: một bên là núi tuyết mùa đông lạnh buốt và một bên là sa mạc nắng cháy bỏng rát! |  | Đấu trường chia làm đôi: nửa trái phủ đầy tuyết trắng và gió bấc thổi mạnh âm năm độ C, nửa phải là cồn cát sa mạc đỏ rực khô khốc; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng khoác áo phao một nửa và mặc áo cộc tay một nửa đứng ở ranh giới. |
| b02 | 00:10.7–00:19.5 (8.8s) | L105 | Ở vòng này, ban giám khảo muốn tìm ra những bộ óc sinh tồn sáng tạo nhất: khi thiên nhiên nổi giận với cái rét cắt da hay cái nóng thiêu đốt, bạn dùng chiêu gì để sống sót? |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ cầm một chiếc nhiệt kế khổng lồ và chiếc ô che nắng, trước mặt là ba tấm huy chương vàng, bạc, đồng lấp lánh. |
| b03 | 00:19.5–00:29.6 (10.0s) | L106 | Đấu sĩ bước vào nửa sân băng tuyết đầu tiên là chú gấu mũm mĩm đến từ dãy núi Tứ Xuyên: Gấu Trúc Lớn! Một loài gấu nhưng hoàn toàn không biết ngủ đông như họ hàng gấu nâu hay gấu Bắc Cực! |  | chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu đứng giữa bão tuyết mùa đông ở nhiệt độ âm năm độ C, gió thổi vù vù qua lớp lông dày nhưng gấu trúc không có hang ngủ đông; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:29.6–00:38.6 (9.0s) | L107 | Không ngủ đông, ăn thực đơn tre nghèo nàn calo nên không tích trữ được nhiều lớp mỡ dày, làm thế nào Gấu Trúc hoang dã có thể chịu nổi những đêm đông tuyết rơi trắng xóa trên đỉnh núi cao? |  | Một nhà khoa học hoạt hình lắp camera hồng ngoại ẩn trên thân cây rừng Tứ Xuyên, theo dõi bóng dáng chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu di chuyển trong đêm đông lạnh giá; KHÔNG có anh MC trong cảnh này. |
| b05 | 00:38.6–00:45.9 (7.3s) | L108 | Năm 2000 20, nhóm nghiên cứu của giáo sư Fuwen Wei công bố phát hiện trên tạp chí PNAS khiến cả thế giới phải... bịt mũi ngỡ ngàng! |  | Màn hình chiếu 38 đoạn video camera hồng ngoại ghi lại một hành vi cực kỳ kỳ quặc của Gấu Trúc khi nhiệt độ tụt xuống dưới 15°C; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:45.9–00:52.8 (6.9s) | L109 | Khi trời trở lạnh giữa tiết trời từ -5 đến 15°C, Gấu Trúc hoang dã đi tìm những đống phân ngựa tươi mới thải ra dưới 10 ngày tuổi! |  | chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu sục sạo dọc con đường mòn thương mại cổ xưa trên núi, mắt sáng rực khi phát hiện một đống phân ngựa còn bốc hơi ấm; KHÔNG có anh MC trong cảnh này. |
| b07 | 00:52.8–01:01.3 (8.5s) | L110 | Nó không ngửi cho vui... mà nó cúi xuống chà xát phân ngựa lên má, lên cổ, rồi lăn lộn toàn thân mình vào giữa đống phân ngựa cho đến khi phủ kín khắp bộ lông trắng đen! |  | chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu lăn tròn hai ba vòng phủ phân lên mặt và lưng với vẻ mặt vô cùng tận hưởng khoan khoái; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng và khán giả trợn mắt kinh ngạc; KHÔNG có anh MC trong cảnh này. |
| b08 | 01:01.3–01:10.6 (9.3s) | L111 | Tại sao một loài vật đáng yêu lại đi tắm phân ngựa giữa mùa đông giá rét? Các nhà sinh vật học phát hiện trong phân ngựa tươi chứa nồng độ cao hai hợp chất hóa học gọi là BCP và BCPO! |  | Hình ảnh phân tử BCP và BCPO phát sáng màu cam ấm áp bốc lên từ đống phân ngựa tươi, bay vào tiếp xúc với làn da của gấu; KHÔNG có anh MC trong cảnh này. |
| b09 | 01:10.6–01:19.4 (8.8s) | L112 | Khi thấm qua da, hai hợp chất này bám thẳng vào kênh cảm biến nhiệt lạnh TRPM8 trên tế bào thần kinh, khóa chặt công tắc báo lạnh khiến não bộ mất cảm giác rét buốt! |  | Mô phỏng phân tử: các hạt BCP khóa chặt chiếc cổng cảm biến lạnh TRPM8, ngọn gió tuyết thổi qua nhưng đồng hồ cảm giác của gấu báo ấm áp bình thường; KHÔNG có anh MC trong cảnh này. |
| b10 | 01:19.4–01:28.3 (8.8s) | L113 | Nhờ lớp kem ủ phân ngựa chống rét tự nhiên này, Gấu Trúc bình thản bước qua tuyết giá mà không bị co ro! Một cách dùng dược liệu tự nhiên từ môi trường đỉnh cao nhất thế giới động vật! |  | chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu đứng ngạo nghễ giữa trời tuyết với nụ cười mãn nguyện, bên cạnh là đàn chuột thí nghiệm bôi hợp chất này cũng chạy nhảy tưng bừng trên mặt băng; KHÔNG có anh MC trong cảnh này. |
| b11 | 01:28.3–01:36.5 (8.2s) | L114 | Chưa hết, năm 2021, nghiên cứu trên Scientific Reports còn giải mã thêm: bộ lông trắng đen nổi tiếng của Gấu Trúc thực chất là áo tàng hình hoàn hảo trong rừng núi! |  | Bức ảnh chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu đứng giữa rừng cây có tuyết và bóng râm: nhìn từ xa bộ lông hòa lẫn hoàn toàn vào đá, thân cây tối màu và mảng tuyết trắng; KHÔNG có anh MC trong cảnh này. |
| b12 | 01:36.5–01:46.5 (10.0s) | L115 | Phần lông đen hòa vào bóng râm sâu thẳm và gốc cây ẩm ướt, còn phần lông trắng hòa lẫn vào mảng tuyết và tán lá sáng! Nhờ đó mắt của báo hoa mai và chó sói hoàn toàn không nhận ra đường viền cơ thể gấu! |  | Hình ảnh minh họa qua góc nhìn thị giác mờ của chó sói và báo đốm: chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu hoàn toàn biến mất giữa nền rừng loang lổ sáng tối; KHÔNG có anh MC trong cảnh này. |
| b13 | 01:46.5–01:59.4 (12.9s) | L116 | Bây giờ chúng ta chuyển sang nửa sân sa mạc nắng cháy với sự góp mặt của Thằn Lằn Quỷ Gai! Ở Tập 19, khán giả đã biết nó uống nước bằng bàn chân qua rãnh mao dẫn. Nhưng nghiên cứu mới năm 2016 còn tiết lộ chi tiết sâu hơn nữa! |  | chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm đứng trên cồn cát đỏ sa mạc Úc khô khốc, nhiệt độ mặt cát bốc khói hầm hập; KHÔNG có anh MC trong cảnh này. |
| b14 | 01:59.4–02:07.3 (7.9s) | L117 | Tiến sĩ Philipp Comanns từ Đại học RWTH Aachen Đức đã cân đo từng mi-li-gam nước trong 1 giờ uống nước của chú thằn lằn chỉ nặng 40g này! |  | Phòng thí nghiệm đo độ ẩm: chú chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm nặng 40g đứng trên bàn cân điện tử siêu chính xác có kết nối máy tính đồ thị; KHÔNG có anh MC trong cảnh này. |
| b15 | 02:07.3–02:18.8 (11.6s) | L118 | Trong 1 giờ ngâm chân vào vũng nước nhỏ, chú Quỷ Gai đóng mở hàm nhấp nháy gần 2.500 lần, mỗi ngụm hút vào miệng chỉ nhỏ đúng 0,7 μl, nhưng tổng lượng nước uống được đạt 1,28g! |  | Đồng hồ đếm số lần đóng mở miệng của chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm nhảy vọt lên 2.500 nhịp, các giọt nước siêu nhỏ 0,7 microlit xếp hàng chạy liên tục vào họng; KHÔNG có anh MC trong cảnh này. |
| b16 | 02:18.8–02:27.8 (8.9s) | L119 | Đồng thời, mạng lưới rãnh trên bề mặt da của nó còn giữ trữ lại được thêm 1,32g nước nữa giống như một chiếc bình giữ ẩm di động đeo quanh người! |  | Toàn thân chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm phát sáng mạng lưới kênh dẫn nước xanh biếc, vừa giữ nước uống vừa làm bể chứa dự phòng cho sa mạc; KHÔNG có anh MC trong cảnh này. |
| b17 | 02:27.8–02:36.4 (8.6s) | L120 | Và đây là cú bẻ lái quan trọng của khoa học: thực tế sương đọng buổi sáng trên sa mạc không đủ để làm đầy các rãnh mao dẫn này! Vậy làm sao nó gom đủ nước giữa cát khô? |  | Thí nghiệm làm mát thằn lằn xuống 22°C trong phòng ẩm: những hạt sương nhỏ li ti bám trên gai nhưng không đủ chảy xuống rãnh da để uống; KHÔNG có anh MC trong cảnh này. |
| b18 | 02:36.4–02:47.2 (10.8s) | L121 | Các nhà khoa học quan sát thấy một hành động siêu thông minh: nó dùng chân trước hất tung cát ẩm lên phủ kín lưng mình, sau đó ép chặt bụng xuống cát để các rãnh mao dẫn hút sạch từng giọt hơi ẩm từ lớp cát phủ hai mặt! |  | chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm dùng chân hất từng nắm cát ẩm từ lớp dưới mặt đất lên phủ đầy lưng, tạo thành chiếc máy ép hút nước thiên tài không tốn một giọt sức lực; KHÔNG có anh MC trong cảnh này. |
| b19 | 02:47.2–02:58.0 (10.8s) | L122 | Tuyển thủ thứ ba bước vào thử thách sinh tồn khắc nghiệt của Vòng ba là Con Lười! Sống cả đời treo ngược trên ngọn cây rừng mưa nhiệt đới, cơ thể Con Lười làm sao để không bị... nghẹt thở bởi chính sức nặng của ruột gan mình? |  | chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini treo ngược bốn chân trên cành cây cao, ánh đèn X-quang chiếu xuyên qua lồng ngực để kiểm tra áp lực lên hai lá phổi; KHÔNG có anh MC trong cảnh này. |
| b20 | 02:58.0–03:07.6 (9.6s) | L123 | Ở hầu hết các loài động vật có vú, nếu bạn treo ngược đầu quá lâu, toàn bộ trọng lượng của gan, dạ dày đầy thức ăn sẽ đè bẹp xuống cơ hoành và hai lá phổi khiến việc hít thở trở nên cực kỳ mệt nhọc! |  | Hình minh họa một chú khỉ thử treo ngược người nhưng mặt đỏ bừng khó thở vì dạ dày nặng nề đè xuống phổi; KHÔNG có anh MC trong cảnh này. |
| b21 | 03:07.6–03:17.0 (9.4s) | L124 | Nhưng năm 2014, nghiên cứu của Rebecca Cliffe công bố trên tạp chí Biology Letters đã khám phá ra một cấu trúc giải phẫu độc quyền của Con Lười: các dây chằng xơ neo nội tạng! |  | Sơ đồ giải phẫu ngực chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini: các dải dây chằng xơ chắc chắn gắn chặt lá gan và dạ dày 4 ngăn trực tiếp vào những chiếc xương sườn dưới gần cơ hoành; KHÔNG có anh MC trong cảnh này. |
| b22 | 03:17.0–03:26.6 (9.6s) | L125 | Những sợi dây chằng xơ đặc biệt này đóng vai trò như hệ thống dây cáp treo cầu giữ chặt gan và dạ dày cố định vào khung xương sườn, ngăn tuyệt đối không cho chúng đè lên phổi khi Con Lười treo ngược! |  | Hai lá phổi của chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini phồng xẹp nhẹ nhàng tự do trong khoang ngực, trong khi dạ dày nặng 30% trọng lượng cơ thể được treo lơ lửng an toàn phía dưới; KHÔNG có anh MC trong cảnh này. |
| b23 | 03:26.6–03:36.9 (10.3s) | L126 | Nhờ hệ thống dây cáp treo nội tạng này, Con Lười tiết kiệm được tới 13% năng lượng hô hấp mỗi khi treo ngược, giúp nó sống thong dong với chế độ ăn lá cây ít calo suốt cả cuộc đời! |  | Bảng thông số năng lượng hô hấp giảm 13%, chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini mỉm cười treo ngược một tay vẫy chào ban giám khảo đầy tự tin; KHÔNG có anh MC trong cảnh này. |
| b24 | 03:36.9–03:43.1 (6.3s) | L127 | Và trong nửa sân nắng nóng thiêu đốt, cỗ xe tăng 3 tấn Hà Mã cũng bước vào kiểm tra khả năng chống tia cực tím dưới ánh nắng gay gắt! |  | chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ đứng giữa nắng gắt chói chang ở nửa sân sa mạc, các cảm biến đo phổ ánh sáng UV chiếu thẳng vào lớp da xám bóng của chú hà mã; KHÔNG có anh MC trong cảnh này. |
| b25 | 03:43.1–03:51.4 (8.3s) | L128 | Theo nghiên cứu hóa sinh nổi tiếng trên tạp chí Nature năm 2004 của giáo sư Yoko Saikawa, chất lỏng chống nắng trên da Hà Mã lúc mới tiết ra hoàn toàn... trong suốt không màu! |  | Cận cảnh lỗ chân lông chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ: một giọt dịch nhớt trong suốt như nước vừa rỉ ra dưới ánh nắng mặt trời; KHÔNG có anh MC trong cảnh này. |
| b26 | 03:51.4–04:04.8 (13.3s) | L129 | Chỉ sau vài phút tiếp xúc với không khí, hai sắc tố axit hipposudoric và norhipposudoric tự động phản ứng biến dịch tiết thành màu đỏ tươi rực rỡ, rồi chuyển sang màu nâu sẫm bám chặt nhiều giờ liền để hấp thụ trọn dải tia UV từ 200-600nm! |  | Giọt dịch chuyển màu ngoạn mục từ trong suốt sang đỏ tươi rồi nâu óng, tạo thành tấm khiên quang học chặn đứng toàn bộ tia tử ngoại độc hại; KHÔNG có anh MC trong cảnh này. |
| b27 | 04:04.8–04:12.9 (8.1s) | L130 | Kết quả Vòng ba cực kỳ xứng đáng! Huy chương đồng thuộc về Con Lười với hệ thống dây chằng treo nội tạng tiết kiệm 13% năng lượng thở! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ trao huy chương đồng cho chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini đang treo ngược mỉm cười hiền hậu; khán đài vỗ tay rộn rã. |
| b28 | 04:12.9–04:23.1 (10.2s) | L131 | Huy chương bạc thuộc về Thằn Lằn Quỷ Gai với kỹ thuật hắt cát ẩm thu gom nước qua rãnh da! Và Huy chương vàng thuộc về Gấu Trúc Lớn với bí kíp tắm phân ngựa chống rét độc nhất vô nhị! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ trao huy chương bạc cho chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm và huy chương vàng cho chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu (sau khi bắt chú gấu đi tắm s |
| b29 | 04:23.1–04:35.1 (12.0s) | L132 | Bảng tổng sắp sau Vòng ba chứng kiến màn bứt phá ngoạn mục: Gấu Trúc Lớn vươn lên dẫn đầu với 4 điểm! Tôm Súng 3 điểm! Cá Cung Thủ 3 điểm! Thằn Lằn Quỷ Gai, Lươn Điện và Bọ Pháo Thủ đồng 2 điểm! Con Lười và Tu Hú ghi 1 điểm! |  | tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) cập nhật cột điểm cao vút của chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu ở vị trí số một; cả khán đài hò reo không ngớt trước cục diện đảo chiều không tưởng! |
| b30 | 04:35.1–04:41.6 (6.5s) | L133 | Bây giờ, đấu trường tạm nghỉ giải lao giữa hiệp để MC đột kích phòng thay đồ xem các đấu sĩ đang làm gì phía sau hậu trường! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cầm micro chạy nhanh về phía hành lang phòng thay đồ nơi mùi hương kỳ lạ và tiếng ồn ào đang vang lên. |

### scene05 · PHỎNG VẤN HẬU TRƯỜNG VÀ NHỮNG PHA KHÓ ĐỠ · 250.5s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:11.7 (11.7s) | L134 | Xin chào toàn thể khán giả! Chúng ta đang có mặt trực tiếp tại khu vực phòng thay đồ của Đại Hội Sinh Tồn Mùa 2! Trong lúc ban tổ chức chuẩn bị sân khấu cho hiệp hai, hãy xem các đấu sĩ đang làm gì phía sau hậu trường! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vest đỏ cầm micro đi dọc hành lang hậu trường nhộn nhịp, các nhân viên tất bật đẩy xe thức ăn và bình oxy. |
| b02 | 00:11.7–00:20.9 (9.2s) | L135 | Vừa mới giành huy chương vàng Vòng ba, ngôi sao đang dẫn đầu bảng tổng sắp là Gấu Trúc Lớn! Nhưng khoan... cái mùi gì nồng nặc bốc ra từ phòng số 11 thế này?! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng bịt mũi nhăn mặt nhìn làn khói xanh lè bốc ra từ khe cửa phòng số 11 có dán biển hình gấu trúc. |
| b03 | 00:20.9–00:29.1 (8.1s) | L136 | Trời đất ơi! Gấu Trúc Lớn vừa mang nguyên một xô... phân ngựa tươi từ vùng núi Tứ Xuyên vào phòng nghỉ để bôi lên mặt giữ ấm giữa máy lạnh phòng chờ! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vừa mở cửa liền giật lùi lại khi thấy chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu đang đắp mặt nạ phân ngựa lên hai má, ngồi thư giãn trên ghế bành vô tư; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:29.1–00:36.1 (7.0s) | L137 | Anh MC vào làm một miếng cho ấm người nè! Ở phòng chờ mở điều hòa 20 độ lạnh muốn đóng băng, bôi cái này vào ấm cực luôn á! |  | chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu giơ chiếc muôi đầy kem phân ngựa mời chào anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng với ánh mắt tròn xoe chân thành nhất quả đất; KHÔNG có anh MC trong cảnh này. |
| b05 | 00:36.1–00:44.5 (8.3s) | L138 | Thôi thôi cảm ơn em, anh MC xin phép từ chối vì anh mặc vest đỏ đi dẫn chương trình chứ không phải đi leo núi tuyết! Chúc mừng em giữ vững phong độ nhé! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vội vàng đóng sập cửa chạy biến ra ngoài hành lang, vuốt ngực thở phào nhẹ nhõm làm cả trường quay cười nghiêng ngả. |
| b06 | 00:44.5–00:53.0 (8.5s) | L139 | Điểm dừng chân tiếp theo là khu vực hồ bơi thư giãn của Bố Già Capybara! Hãy xem vị Bộ trưởng Ngoại giao đang nghỉ ngơi kiểu gì sau ba vòng chưa có điểm nào! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đẩy cửa bước vào khu vực hồ nước ấm phòng số 15, mặt nước tĩnh lặng phẳng lì không thấy bóng dáng thí sinh đâu; KHÔNG có anh MC trong cảnh này. |
| b07 | 00:53.0–01:01.1 (8.2s) | L140 | Ủa? Bố Già Capybara trốn đi đâu mất tiêu rồi? Trong bồn nước chẳng thấy ai ngoài mấy ngọn rong bèo lững lờ trôi... Khoan đã, nhìn kỹ mặt nước kia kìa! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng ngó nghiêng tìm kiếm khắp phòng nghỉ, trên mặt hồ chỉ thấy ba chấm nhỏ xíu nổi lềnh bềnh sát nhau; KHÔNG có anh MC trong cảnh này. |
| b08 | 01:01.1–01:11.0 (9.8s) | L141 | Hóa ra vị trí mắt, tai và hai lỗ mũi của Capybara nằm xếp thẳng hàng trên đỉnh đầu giống hệt cấu tạo của Hà Mã! Nó đang ngủ say giấc nồng ngay dưới lòng hồ chỉ để hở đúng mắt mũi tai lên mặt nước! |  | Cận cảnh dưới làn nước trong suốt: toàn bộ cơ thể béo múp 65kg của chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia đang nằm ngủ ngon lành dưới đáy hồ, chỉ để lộ đúng đỉnh mũi và hai mắt trên mặt nước; KHÔNG có anh MC trong cảnh này. |
| b09 | 01:11.0–01:17.0 (6.0s) | L142 | Một tư thế ngủ vừa giữ mát làn da, vừa dễ dàng thở không khí và quan sát động tĩnh xung quanh mà không kẻ thù nào phát hiện được! |  | Bóng báo đốm đi ngang qua bờ hồ nhìn lướt qua nhưng không thấy gì ngoài ba chấm nhỏ tưởng là cành cây khô; KHÔNG có anh MC trong cảnh này. |
| b10 | 01:17.0–01:21.2 (4.2s) | L143 | Chào Bố Già! Nằm ngâm nước thế này thì chút nữa thi Vòng bốn có bị lạnh bụng không ạ? |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng khom người dí micro sát mặt nước phỏng vấn nhỏ nhẹ để không làm đánh thức giấc ngủ trưa của Bố Già; KHÔNG có anh MC trong cảnh này. |
| b11 | 01:21.2–01:28.3 (7.1s) | L144 | Khò... khò... Nước ấm thế này ngủ sướng lắm anh bạn... Để tôi ngủ thêm 10 phút nữa rồi ra cân hết Vòng bốn cho anh xem! |  | chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia mở hé một mắt, ngáp một cái nhẹ nhàng rồi nhắm mắt ngủ tiếp tạo ra mấy bọt khí bong bóng phồng ở mũi; KHÔNG có anh MC trong cảnh này. |
| b12 | 01:28.3–01:36.6 (8.3s) | L145 | Thần thái của người đàn ông chưa có điểm nào mà vẫn ngủ ngon lành như đang nắm chắc chiếc cúp vô địch trong tay! Bây giờ chúng ta ghé thăm phòng của Chim Tu Hú! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng bước sang phòng số 14, nơi chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái đang ngồi xếp gọn một chiếc ba lô du lịch mini và đeo thiết bị định vị GPS; KHÔNG có anh MC trong cảnh này. |
| b13 | 01:36.6–01:43.3 (6.7s) | L146 | Chào Chim Tu Hú! Sao trong phòng nghỉ mà bạn lại chuẩn bị hành lý bay đi đâu thế này? Chúng ta vẫn còn năm vòng thi nữa cơ mà! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng ngạc nhiên chỉ tay vào chiếc bản đồ thế giới trải rộng trên bàn phòng nghỉ của chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái; KHÔNG có anh MC trong cảnh này. |
| b14 | 01:43.3–01:53.8 (10.5s) | L147 | Anh MC không biết rồi! Sau giải đấu này, tôi phải bay ngay chuyến bay đường dài 16.000km từ châu Âu sang tận Trung Phi để tránh rét mùa đông đấy! Tôi chỉ tranh thủ ghé đây kiếm ít huy chương thôi! |  | chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái đeo kính râm phi công, chỉ tay vào đường bay đỏ vẽ hình vòng cung khép kín qua lục địa châu Phi trên bản đồ; KHÔNG có anh MC trong cảnh này. |
| b15 | 01:53.8–02:02.9 (9.1s) | L148 | Chà, đúng là phi công hạng nặng! Và căn phòng cuối cùng trong giờ giải lao là phòng của cô nàng Con Lười! Không biết bạn ấy đã tiêu hóa xong chiếc lá từ hồi khai mạc chưa? |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng nhẹ nhàng hé cửa phòng số 13, ánh đèn vàng dịu nhẹ chiếu lên cành cây nơi chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini đang treo ngược; KHÔNG có anh MC trong cảnh này. |
| b16 | 02:02.9–02:09.7 (6.8s) | L149 | Ban tổ chức trang bị một chiếc đồng hồ bấm giờ treo ngay cạnh mặt Con Lười! MC đặt một câu hỏi ngắn: bạn cảm thấy đấu trường Mùa 2 thế nào? |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng giơ micro lên trước mặt chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini, kim đồng hồ bấm giờ bắt đầu chạy tích tắc từng giây từng phút; KHÔNG có anh MC trong cảnh này. |
| b17 | 02:09.7–02:16.6 (6.8s) | L150 | Con Lười nhướng mày... mở hé miệng... mất 5 giây để hít hơi... mất 10 giây để cong môi... và mất cả 1 phút mới phát âm được chữ đầu tiên! |  | Cận cảnh chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini nhếch mép từ từ như phim quay chậm 0,1 lần, anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng chống cằm chờ đợi mắt dần díu lại; KHÔNG có anh MC trong cảnh này. |
| b18 | 02:16.6–02:20.4 (3.9s) | L151 | Tôi... cảm... thấy... đại... hội... năm... nay... rất... là... vui... luôn... ạ... |  | Khi chữ cuối cùng thoát ra khỏi miệng Con Lười, thì nhân viên hậu trường đã kịp ăn xong hai tô phở và dọn dẹp sạch sẽ cả hành lang! [laughter] :: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng giật mình tỉnh giấc khi nghe tiếng chuông báo hết giờ giải lao vang lên inh ỏi, nhân viên đang lau sàn mỉm cười lắc đầu; KHÔNG có anh MC trong cảnh này. |
| b19 | 02:20.4–02:29.3 (8.9s) | L152 | Chưa hết đâu quý vị! Ghé ngang phòng số 16 của Tôm Súng, chúng ta bắt gặp chú tôm đang ngồi đánh bóng khẩu đại bác cùng người bạn thân thiết là một chú cá bống mắt lồi! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng nhìn qua ô cửa kính bể nước phòng 16: chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa đang dùng càng nhỏ lau chùi càng súng to, bên cạnh là chú cá bống nhỏ vẫy đuôi canh gác cửa phòng; KHÔNG có anh MC trong cảnh này. |
| b20 | 02:29.3–02:37.2 (7.9s) | L153 | Chú cá bống làm nhiệm vụ canh cửa bảo vệ còn Tôm Súng dùng càng đào cát làm phòng ở chung sang trọng! Một cặp đôi bạn thân gắn bó keo sơn nhất thế giới biển cả! |  | chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa chạm nhẹ cặp râu dài lên đuôi cá bống ăn mừng, hai người bạn cùng vẫy tay chào ống kính máy quay thân thiện; KHÔNG có anh MC trong cảnh này. |
| b21 | 02:37.2–02:46.7 (9.5s) | L154 | Còn trong phòng bên cạnh, nhà máy điện Lươn Điện đang vừa bơi lội thư giãn vừa thưởng thức bữa ăn nhẹ bằng thịt cá nhỏ để nạp đầy năng lượng cho bộ bơm ion Natri Kali! |  | chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh lượn vòng trong bể nước ấm, vài tia điện nhỏ lách tách sáng lên màu xanh dịu báo hiệu dung lượng pin đã đầy một trăm phần trăm; KHÔNG có anh MC trong cảnh này. |
| b22 | 02:46.7–02:54.9 (8.3s) | L155 | Còn tại góc phòng sa mạc nhân tạo, Thằn Lằn Quỷ Gai đang tận hưởng bồn tắm cát ẩm mát rượi, chuẩn bị tinh thần đối đầu với gã khổng lồ Hà Mã ở vòng bốn! |  | chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm nằm thư thái phủ một lớp cát ẩm mịn lên khắp sống lưng gai góc, nhấp nháy miệng uống nước đầy sảng khoái; KHÔNG có anh MC trong cảnh này. |
| b23 | 02:54.9–03:03.2 (8.2s) | L156 | Bước sang phòng số 20 của Cá Cung Thủ, chúng ta bắt gặp chú cá đang nhìn chằm chằm vào một cuốn an-bum ảnh chân dung dán đầy mặt các thành viên ban tổ chức! |  | chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn bơi sát thành bể kính, mắt đảo qua lại soi xét hàng loạt tấm ảnh chụp mặt anh MC và bà giám khảo Cú mèo; KHÔNG có anh MC trong cảnh này. |
| b24 | 03:03.2–03:12.0 (8.9s) | L157 | Chú cá đang luyện tập ghi nhớ từng nếp nhăn trên khuôn mặt của giám khảo để phòng trường hợp giám khảo chấm điểm thiếu công bằng là... phun nước thẳng vào kính! |  | chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn nháy mắt tinh ranh ngậm đầy một họng nước, anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng giật mình lấy chiếc micro che mặt lùi lại phòng thủ; KHÔNG có anh MC trong cảnh này. |
| b25 | 03:12.0–03:20.6 (8.6s) | L158 | Sang tới phòng số 18 của Bọ Pháo Thủ, ban tổ chức thấy một cái bàn đầy ắp các loại lá cây và xác côn trùng giàu dưỡng chất giúp chú bọ nạp lại kho nguyên liệu hóa học! |  | chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C ngồi trước mâm cơm thịnh soạn nạp nhiên liệu cho túi dự trữ hydroquinone và oxy già sau những phát bắn thử nghiệm; KHÔNG có anh MC trong cảnh này. |
| b26 | 03:20.6–03:29.9 (9.3s) | L159 | Còn trong bồn tắm bùn khổng lồ ở cuối hành lang, gã khổng lồ Hà Mã đang ngâm mình thư giãn, làn da tiết ra lớp dịch nhờn trong suốt dần chuyển màu đỏ hồng lấp lánh dưới ánh đèn phòng thay đồ! |  | chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ ngâm mình ngập tới mang tai trong bồn bùn rộng lớn, thả những bong bóng nước to đùng thư thái giữa giờ nghỉ; KHÔNG có anh MC trong cảnh này. |
| b27 | 03:29.9–03:36.8 (6.9s) | L160 | Này anh MC, chút nữa thi vòng dinh dưỡng nhớ chuẩn bị thật nhiều cỏ non nhé, chứ tôi đang đói cồn cào cả ba ngăn dạ dày rồi đấy! |  | chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ há to chiếc miệng rộng ngoác 150 độ ngáp một cái vang rền làm rung cả cửa kính phòng thay đồ; KHÔNG có anh MC trong cảnh này. |
| b28 | 03:36.8–03:41.0 (4.2s) | L161 | Vâng vâng, ban tổ chức đã chuẩn bị sẵn cả một xe tải cỏ tươi ngoài sân rồi ạ! |  | Nhân viên kéo một xe tải chất đầy cỏ non xanh mướt tiến về phía khu vực thi đấu Vòng bốn; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng lau mồ hôi vẫy tay tạm biệt chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ. |
| b29 | 03:41.0–03:48.9 (7.9s) | L162 | Trên đường quay lại sân chính, MC còn bắt gặp Gấu Trúc Lớn đang tập động tác trồng cây chuối khởi động cơ tay trước khi bước vào vòng thi tiêu hóa! |  | chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu chống hai tay xuống thảm tập thể dục lắc lư cái bụng tròn, khuôn mặt tập trung cao độ nhưng lại ngã lăn kềnh hài hước; KHÔNG có anh MC trong cảnh này. |
| b30 | 03:48.9–03:56.1 (7.2s) | L163 | Còn anh chàng Cá Cung Thủ và Tôm Súng thì đang thi xem ai bắn trúng bia nhanh hơn ở hành lang làm ướt sũng cả chiếc áo vest đỏ của MC! |  | chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn và chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa đồng loạt bắn tia nước trúng mục tiêu, giọt nước bắn tung tóe ướt hết vạt áo anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng làm khán giả cư |
| b31 | 03:56.1–04:03.4 (7.3s) | L164 | Giờ nghỉ giải lao đầy ắp tiếng cười đã kết thúc! Chuông báo động hiệp hai vang lên dồn dập đưa toàn thể đấu sĩ quay trở lại sàn đấu chính! |  | Tiếng còi vang dội khắp hành lang, mười tuyển thủ chỉnh trang lại trang phục tiến ra đường hầm bước vào chặng đua tăng tốc của hiệp hai. |
| b32 | 04:03.4–04:10.5 (7.1s) | L165 | Vòng bốn ngay sau đây sẽ giải mã những bí mật động trời về dinh dưỡng và sức ảnh hưởng sinh thái của các đấu sĩ! Hãy sẵn sàng đón xem! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vung tay dẫn đường ra sân khấu chính nơi màn hình phân tích sinh thái học khổng lồ đã bật sáng rực rỡ. |

### scene06 · DINH DƯỠNG DỊ THƯỜNG VÀ VAI TRÒ BƠM KHOÁNG CHẤT SINH THÁI · 281.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.4 (7.4s) | L166 | Chào mừng toàn thể quý vị trở lại với hiệp hai của Đại Hội Sinh Tồn Mùa 2: Vòng bốn — Dinh dưỡng dị thường và chuỗi cung ứng sinh thái! |  | Sân khấu chính biến thành một mô hình hệ sinh thái sông ngòi châu Phi và rừng nhiệt đới rộng lớn với các biểu đồ hóa chất phát sáng; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cầm micro giới thiệu. |
| b02 | 00:07.4–00:16.3 (8.9s) | L167 | Ở vòng thi này, ban giám khảo không chỉ nhìn vào việc con vật ăn cái gì, mà còn đánh giá xem hệ tiêu hóa của nó mang lại tác động kinh thiên động địa nào cho thiên nhiên xung quanh! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ đeo kính soi vào ống nghiệm chứa các khoáng chất lấp lánh, trước mặt là ba tấm huy chương vàng, bạc, đồng sáng chói. |
| b03 | 00:16.3–00:29.8 (13.5s) | L168 | Thí sinh đầu tiên bước vào vòng cân đo sinh thái là cỗ xe tăng 3 tấn châu Phi: Hà Mã! Khán giả đều biết Hà Mã thích quạt đuôi văng phân đánh dấu lãnh thổ, nhưng nghiên cứu năm 2019 đã phát hiện một bí mật vĩ đại ẩn trong đống phân đó! |  | chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ bệ vệ bước lên sàn khấu mô phỏng dòng sông Mara ở Kenya, bên dưới là những đàn cá nhỏ và tảo thủy sinh đang bơi lội; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:29.8–00:37.3 (7.5s) | L169 | Năm 2019, nhà sinh thái học Jonas Schoelynck tại Đại học Antwerp Bỉ công bố một nghiên cứu chấn động trên tạp chí uy tín Science Advances! |  | Trang bài báo Science Advances năm 2019 hiện lên dòng tiêu đề gọi Hà Mã là 'Cỗ máy bơm nguyên tố Silicon sống của tự nhiên'; KHÔNG có anh MC trong cảnh này. |
| b05 | 00:37.3–00:47.6 (10.3s) | L170 | Vào ban đêm, mỗi con Hà Mã rời mặt nước lên đồng cỏ gặm hàng chục ký cỏ giàu chất khoáng Silicon thực vật. Đến ban ngày, chúng quay về ngâm mình dưới sông và bài tiết toàn bộ số khoáng chất đó xuống dòng nước! |  | chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ ăn cỏ xanh mướt trên thảo nguyên ban đêm dưới ánh trăng, sau đó nhảy xuống dòng sông Mara thư giãn vào ban ngày; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:47.6–00:56.1 (8.5s) | L171 | Các nhà khoa học đo được con số kinh hoàng: đàn Hà Mã dọc theo sông Mara ở Kenya bơm trực tiếp khoảng 0,4 tấn nguyên tố Silicon nguyên chất xuống lòng sông mỗi ngày! |  | Chiếc cân tải trọng khổng lồ hiển thị con số 400 kg tinh thể Silicon lấp lánh chảy ào ào vào dòng nước xanh biếc; KHÔNG có anh MC trong cảnh này. |
| b07 | 00:56.1–01:05.7 (9.6s) | L172 | Số Silicon do Hà Mã vận chuyển chiếm tới 76% tổng lượng dòng chảy Silicon của toàn bộ con sông lớn! Không có Hà Mã, con sông gần như mất đi ba phần tư nguồn cung Silicon tự nhiên! | **76%** · Đóng góp cho dòng sông · R/380 · [0.68, 0.48] | Biểu đồ tròn dòng chảy Silicon: 76% màu đỏ mang biểu tượng chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ, chỉ 24% đến từ xói mòn đất đá tự nhiên; KHÔNG có anh MC trong cảnh này. |
| b08 | 01:05.7–01:15.2 (9.5s) | L173 | Tại sao Silicon lại quan trọng đến thế? Bởi vì nó là vật liệu thiết yếu để loài tảo khuê cực nhỏ dưới hồ Victoria xây dựng lớp vỏ thủy tinh và quang hợp tạo oxy nuôi sống hàng triệu con cá thương phẩm! |  | Kính hiển vi soi các tế bào tảo khuê lấp lánh như những viên pha lê thủy tinh dưới đáy hồ, đàn cá lớn bơi lượn đông đúc vui tươi; KHÔNG có anh MC trong cảnh này. |
| b09 | 01:15.2–01:22.3 (7.1s) | L174 | Chưa hết, dù trông giống lợn, Hà Mã thực chất tiến hóa một chiếc dạ dày ba ngăn lên men vi sinh cực kỳ phức tạp gọi là hệ tiêu hóa giả nhai lại! |  | Sơ đồ giải phẫu dạ dày 3 ngăn của chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ: thức ăn lên men từ từ trong các ngăn chứa vi khuẩn giúp nó sống khỏe dù ăn ít hơn bò nhiều lần; KHÔNG có anh MC trong cảnh này. |
| b10 | 01:22.3–01:30.4 (8.1s) | L175 | Nhờ hệ thống lên men ba ngăn tiết kiệm năng lượng này, một cỗ xe tăng nặng 3 tấn chỉ cần ăn lượng cỏ bằng khoảng 1,5% trọng lượng cơ thể mỗi ngày là đủ sinh tồn! |  | Bảng so sánh lượng ăn: con bò ăn một đống cỏ khổng lồ so với phần ăn khiêm tốn hơn nhiều của chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ; KHÔNG có anh MC trong cảnh này. |
| b11 | 01:30.4–01:38.9 (8.5s) | L176 | Và nhân tiện nhắc tới đường ruột kỳ lạ trong vòng dinh dưỡng này, khoa học năm 2015 còn phát hiện thêm một sự thật sốc nữa về hệ vi sinh vật trong bụng Gấu Trúc Lớn! |  | Phòng thí nghiệm sinh học phân tử chiếu ảnh phóng đại hàng tỷ vi khuẩn sống bên trong đường ruột của chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu; KHÔNG có anh MC trong cảnh này. |
| b12 | 01:38.9–01:49.4 (10.5s) | L177 | Theo nghiên cứu công bố trên tạp chí mBio khi phân tích hàng loạt mẫu phân của Gấu Trúc qua các mùa, đường ruột của chúng vẫn... không hề tiến hóa ra nhóm vi khuẩn tiêu hóa xen-lu-lô như loài bò hay cừu! |  | Biểu đồ so sánh vi khuẩn ruột: ruột bò đầy vi khuẩn Ruminococcaceae phân hủy cỏ, còn ruột chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu lại toàn vi khuẩn Escherichia và Streptococcus giống hệt chó sói và hổ! KHÔNG có anh MC trong cảnh này. |
| b13 | 01:49.4–01:59.0 (9.5s) | L178 | Tức là suốt 2 triệu năm chuyển sang ăn chay, ngay cả đội quân vi khuẩn trong bụng Gấu Trúc vẫn giữ nguyên cấu trúc của thú ăn thịt! Một màn bảo thủ di truyền cứng đầu nhất lịch sử tiến hóa! |  | chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu nhìn vào kính hiển vi thấy đội quân vi khuẩn ăn thịt trong bụng mình liền ngơ ngác gãi đầu cười trừ, cả khán đài cười ồ; KHÔNG có anh MC trong cảnh này. |
| b14 | 01:59.0–02:09.2 (10.2s) | L179 | Còn chú Con Lười thì sao? Bên cạnh tốc độ tiêu hóa siêu chậm, Con Lười còn điều chỉnh thân nhiệt biến thiên linh hoạt từ 24°C vào ban đêm lên 33°C lúc phơi nắng giống như loài bò sát! |  | Biểu đồ nhiệt độ cơ thể chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini dao động nhịp nhàng theo ánh nắng mặt trời từ 24°C đến 33°C giúp tiết kiệm tối đa năng lượng chuyển hóa; KHÔNG có anh MC trong cảnh này. |
| b15 | 02:09.2–02:16.9 (7.7s) | L180 | Giám khảo kinh ngạc: phân của Hà Mã hóa ra lại là nguồn phân bón khoáng chất vàng nuôi sống cả một hệ sinh thái hồ khổng lồ châu Phi! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ vỗ tay thán phục, đặt ngôi sao điểm tối đa cho chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ trên bảng chấm thi. |
| b16 | 02:16.9–02:26.7 (9.8s) | L181 | Tuyển thủ thứ hai bước lên sàn đo dinh dưỡng là Bố Già đầm lầy: Capybara! Ngoài tập tính ăn lại phân mềm buổi sáng đã nổi tiếng, Bố Già còn có một bí mật về bộ răng cửa đáng kinh ngạc! |  | chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia ngồi trước một bàn tiệc gồm toàn cỏ lau cứng, vỏ cây sần sùi và quả bí đỏ tươi ngon; KHÔNG có anh MC trong cảnh này. |
| b17 | 02:26.7–02:33.8 (7.2s) | L182 | Giống như họ hàng nhà hải ly và sóc, cặp răng cửa hình chiếc đục sắc bén ở hàm trước của Capybara... mọc dài ra không bao giờ ngừng suốt cả cuộc đời! |  | Phóng đại hàm răng cửa màu trắng ngà của chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia: mũi tên chỉ tốc độ răng mọc dài ra liên tục mỗi tuần như hai chiếc đục thép; KHÔNG có anh MC trong cảnh này. |
| b18 | 02:33.8–02:39.3 (5.5s) | L183 | Nếu một chú Capybara lười biếng không chịu nhai, cặp răng cửa sẽ mọc dài đâm xuyên qua cả hàm làm nó không thể đóng miệng lại được! |  | Hình minh họa hài hước: chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia tưởng tượng răng mình mọc dài thòng lọng như răng nanh ma cà rồng rồi giật mình lắc đầu nguầy nguậy; KHÔNG có anh MC trong cảnh này. |
| b19 | 02:39.3–02:48.2 (8.9s) | L184 | Để giữ cho hàm răng luôn ngắn gọn và sắc bén, mỗi ngày Bố Già phải tiêu thụ đều đặn từ 3-4kg cỏ xơ cứng chứa đầy tinh thể cát và gặm cả vỏ cây gỗ cứng để mài mòn men răng tự |  | chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia gặm cành cây vỏ cứng rôm rốp làm những tia lửa mài răng lóe sáng hoạt hình đầy thú vị; KHÔNG có anh MC trong cảnh này. |
| b20 | 02:48.2–02:57.3 (9.0s) | L185 | nhiên! Đồng thời, men răng của nó có cấu trúc tự mài sắc: mặt ngoài cứng hơn mặt trong, khiến càng nhai đồ cứng thì lưỡi răng lại càng trở nên bén ngọt hơn như dao gọt hoa quả! |  | Cận cảnh lưỡi răng cửa chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia được mài vát chéo sắc lẹm như mũi dao thợ mộc, cắt phăng thân cây sậy chỉ trong một nhát cắn; KHÔNG có anh MC trong cảnh này. |
| b21 | 02:57.3–03:09.0 (11.8s) | L186 | Và tuyển thủ thứ ba mang đến bài thi dinh dưỡng cực kỳ dị biệt: Thằn Lằn Quỷ Gai! Ở Tập 19 chúng ta đã biết thực đơn độc nhất của nó là kiến đen, nhưng chiến thuật bẫy kiến của nó mới thực sự là bậc thầy kiên nhẫn! |  | chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm đứng bất động bên một con đường mòn đầy kiến đen Iridomyrmex đang bò tấp nập giữa cát đỏ; KHÔNG có anh MC trong cảnh này. |
| b22 | 03:09.0–03:20.0 (11.0s) | L187 | Nghiên cứu sinh thái học tại Tây Úc cho thấy Thằn Lằn Quỷ Gai không bao giờ đuổi theo đàn kiến tốn sức! Nó chọn ngồi lì đúng tại ngã tư đường mòn giao nhau vào lúc sáng sớm hoặc chiều mát khi đàn kiến đi kiếm ăn đông |  | Bản đồ chiến thuật của chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm: ngồi phục kích ngay nút giao thông ngã tư của bầy kiến giống cảnh sát giao thông chặn chốt kiểm tra; KHÔNG có anh MC trong cảnh này. |
| b23 | 03:20.0–03:29.2 (9.2s) | L188 | nhất! Mỗi cú phóng lưỡi dính diễn ra trong chớp mắt, tiêu thụ hàng ngàn con kiến chứa axit formic nhưng lại giữ cho độ pH dạ dày cân bằng hoàn hảo nhờ dịch đệm kiềm tính đặc biệt! |  | Bên trong dạ dày chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm: các bọt dịch kiềm màu xanh lam trung hòa ngay lập tức những giọt axit đỏ rực từ bụng đàn kiến; KHÔNG có anh MC trong cảnh này. |
| b24 | 03:29.2–03:39.4 (10.2s) | L189 | Đặc biệt, chiếc gù mỡ sau cổ và phần đuôi mập của nó đóng vai trò như một kho pin thực phẩm dự trữ, giúp nó nhịn ăn hoàn toàn suốt mùa đông khắc nghiệt khi đàn kiến chui sâu xuống lòng đất! |  | Chiếc đuôi mập mạp phát sáng lớp năng lượng mỡ dự trữ vàng óng, chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm yên tâm cuộn tròn nghỉ ngơi chờ mùa xuân tới; KHÔNG có anh MC trong cảnh này. |
| b25 | 03:39.4–03:45.2 (5.8s) | L190 | Chưa dừng lại ở đó, ban giám khảo còn chấm thêm điểm cộng cho khả năng giữ gìn và sử dụng răng hàm của Gấu Trúc Lớn! |  | Cận cảnh hàm răng hàm bản rộng phẳng lì của chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu đang nghiền nát một thân tre già cứng như gỗ lim; KHÔNG có anh MC trong cảnh này. |
| b26 | 03:45.2–03:56.4 (11.2s) | L191 | Khác với răng nhọn xé thịt của hổ hay sư tử, răng hàm của Gấu Trúc đã tiến hóa to gấp 7 lần bình thường với lớp men răng cực dày có khả năng tự phục hồi các vết nứt siêu nhỏ khi nhai tre cứng suốt 14 tiếng mỗi ngày! |  | Sơ đồ men răng chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu phóng đại hàng ngàn lần: các lớp tinh thể khoáng xếp đan xen giúp tự làm lành vết nứt vi mô khi chịu lực nén khổng lồ; KHÔNG có anh MC trong cảnh này. |
| b27 | 03:56.4–04:06.0 (9.6s) | L192 | Còn gã khổng lồ Hà Mã nhờ có dạ dày ba ngăn lên men hiệu quả mà có thể ung dung dành tới 16 tiếng mỗi ngày ngâm mình nghỉ ngơi dưới sông mà chẳng cần ăn suốt cả ban ngày! |  | chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ nằm ngâm mình thư thái dưới dòng sông xanh mát, đàn cá nhỏ bơi lượn quanh người dọn sạch ký sinh trùng trên da; KHÔNG có anh MC trong cảnh này. |
| b28 | 04:06.0–04:14.2 (8.2s) | L193 | Ban giám khảo công bố kết quả Vòng bốn! Huy chương đồng thuộc về Thằn Lằn Quỷ Gai với chiến thuật phục kích ngã tư và kho mỡ đuôi dự trữ năng lượng! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ trao huy chương đồng cho chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm đang giơ ngón cái đầy tự hào; khán đài vỗ tay tán thưởng. |
| b29 | 04:14.2–04:24.2 (10.0s) | L194 | Huy chương bạc thuộc về Capybara với cặp răng cửa tự mài sắc mọc vĩnh cửu! Và Huy chương vàng thuộc về Hà Mã với công trạng bơm 400kg Silicon mỗi ngày nuôi sống dòng sông! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ trao huy chương bạc cho chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia và huy chương vàng sáng loáng cho chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh t |
| b30 | 04:24.2–04:36.2 (12.0s) | L195 | Bảng tổng sắp cập nhật điểm số mới nhất: Gấu Trúc dẫn đầu 4 điểm! Tôm Súng 3 điểm! Cá Cung Thủ, Thằn Lằn Quỷ Gai và Hà Mã cùng chạm mốc 3 điểm! Lươn Điện, Bọ Pháo Thủ, Capybara đồng 2 điểm! Tu Hú và Con Lười 1 điểm! |  | tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) rực sáng bảng điểm cân bằng cực kỳ căng thẳng, khoảng cách giữa các đấu sĩ chỉ tính bằng một tấm huy chương! |
| b31 | 04:36.2–04:41.7 (5.5s) | L196 | Vòng năm ngay sau đây sẽ lật mở những xã hội bí mật và sức mạnh bầy đàn gây sốc nhất thế giới động vật! Đừng bỏ lỡ! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vung tay chỉ về phía đấu trường hợp tác xã hội nơi hàng trăm cá thể nhỏ bé đang tập hợp thành một đội quân hùng mạnh. |

### scene07 · SỨC MẠNH BẦY ĐÀN VÀ NHỮNG XÃ HỘI BÍ MẬT CHƯA TỪNG BIẾT · 256.5s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:10.6 (10.6s) | L197 | Chào mừng toàn thể khán đài bước vào Vòng năm: Sức mạnh bầy đàn và những xã hội bí mật! Lâu nay chúng ta thường nghĩ những sát thủ mang vũ khí hạng nặng đều thích hành động đơn độc như sói hoang. |  | Sân đấu tối sầm lại rồi bật đèn chiếu sáng ba mô hình sinh thái bí ẩn: một rạn san hô bọt biển, một hồ sông Amazon sâu thẳm và một đầm lầy cỏ lau rộng lớn; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng hạ thấp giọng đầy kịch tính. |
| b02 | 00:10.6–00:18.9 (8.2s) | L198 | Nhưng trong thế giới khoa học hiện đại, những phát hiện mới nhất đã lật nhào hoàn toàn định kiến đó! Hãy chuẩn bị tinh thần chứng kiến màn lột xác của ba tuyển thủ đêm nay! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ mở cuốn hồ sơ mật đóng dấu đỏ tuyệt mật, trước mặt là ba tấm huy chương vàng, bạc, đồng chờ trao cho đội quân xuất sắc nhất. |
| b03 | 00:18.9–00:31.3 (12.5s) | L199 | Ứng cử viên đầu tiên bước lên bục là pháo thủ đại dương: Tôm Súng! Ai cũng biết nó sống cộng sinh với cá bống gác hang, nhưng ít ai biết một nhánh họ hàng của Tôm Súng lại thiết lập hẳn một... vương quốc ong kiến dưới đáy biển! |  | chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa vẫy càng gọi tới một khối bọt biển khổng lồ màu vàng cam rực rỡ từ đại dương Caribe, bên trong lúc nhúc hàng trăm sinh vật nhỏ bé; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:31.3–00:38.4 (7.1s) | L200 | Năm 1996, nhà sinh vật học biển Emmett Duffy công bố một phát hiện làm chấn động giới động vật học trên tạp chí Nature danh |  | Trang bìa tạp chí Nature năm 1996 hiện lên hình ảnh phóng đại loài tôm súng bọt biển Synalpheus regalis sống thành bầy đàn khổng lồ; KHÔNG có anh MC trong cảnh này. |
| b05 | 00:38.4–00:52.8 (14.4s) | L201 | tiếng! Cho đến trước năm 1996, khái niệm xã hội bậc cao eusociality — tức là có 1 con chúa duy nhất đẻ trứng, còn hàng trăm con khác hy sinh quyền sinh sản để đi làm lính bảo vệ tổ — chỉ được tìm thấy ở côn trùng như ong, kiến, mối và chuột dũi trần trên cạn! |  | Biểu đồ phân loại xã hội tự nhiên: ong mật, kiến lửa và mối trên cạn đứng cạnh một dấu chấm hỏi khổng lồ dưới đáy biển xanh; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:52.8–01:01.7 (8.9s) | L202 | Và loài tôm súng Synalpheus regalis chính là loài sinh vật biển đầu tiên trên hành tinh được xác nhận sở hữu cấu trúc xã hội bậc cao eusociality giống hệt như kiến và ong! |  | Cắt lớp chiếc bọt biển dưới kính hiển vi: hơn ba trăm con tôm súng sống chen chúc trong các đường hầm bọt biển như một thành phố ngầm thu nhỏ; KHÔNG có anh MC trong cảnh này. |
| b07 | 01:01.7–01:07.2 (5.5s) | L203 | Trong một tổ bọt biển chứa hơn 300 thành viên đó, chỉ có duy nhất một Tôm Chúa cái khổng lồ làm nhiệm vụ sinh sản! | **300 LÍNH** · Chung một tổ bọt biển · L/380 · [0.36, 0.46] | Cận cảnh Tôm Chúa to béo nằm ở trung tâm buồng an toàn bên trong bọt biển, trên đầu đội chiếc vương miện nhỏ xíu lấp lánh; KHÔNG có anh MC trong cảnh này. |
| b08 | 01:07.2–01:16.8 (9.5s) | L204 | Toàn bộ hàng trăm con tôm lính còn lại — vốn là anh chị em ruột thịt của nhau — hoàn toàn không bao giờ sinh sản! Chúng sở hữu chiếc càng súng lớn hơn hẳn để làm lính gác bảo vệ các lối vào tổ bọt biển trước kẻ thù xâm lược! |  | Đội quân tôm lính xếp hàng dọc các lỗ thông hơi của bọt biển, đồng loạt giơ càng súng nhắm thẳng ra ngoài sẵn sàng nhả đạn; KHÔNG có anh MC trong cảnh này. |
| b09 | 01:16.8–01:26.0 (9.2s) | L205 | Khi có cua hoặc cá lạ mon men tới gần, cả đội quân tôm lính đồng loạt búng càng tạo thành dàn pháo thanh âm đẩy lùi kẻ thù bảo vệ Tôm Chúa và đàn em nhỏ an toàn tuyệt đối! |  | Kẻ xâm nhập bị sóng xung kích từ hàng chục khẩu súng tôm bắn bật ngửa ra xa không kịp trở tay; KHÔNG có anh MC trong cảnh này. |
| b10 | 01:26.0–01:32.7 (6.7s) | L206 | Một đế chế quân sự thu nhỏ có nữ hoàng và binh lính ngay trong lòng đại dương! Một phát hiện thay đổi cả sách giáo khoa sinh học biển! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vỗ tay thán phục trước thành phố bọt biển của chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa, khán giả trầm trồ không ngớt. |
| b11 | 01:32.7–01:39.9 (7.2s) | L207 | Tiếp theo là một cú sốc thứ hai đến từ rừng rậm Amazon, làm đảo lộn hàng trăm năm hiểu biết của loài người về tuyển thủ Lươn Điện! |  | Đèn sân khấu tắt tối om rồi chiếu rọi vào một khúc sông nhỏ mang tên Iriri tại bang Pará nước Brazil; KHÔNG có anh MC trong cảnh này. |
| b12 | 01:39.9–01:49.2 (9.3s) | L208 | Suốt hơn hai thế kỷ kể từ thời nhà thám hiểm Alexander von Humboldt, cả thế giới khoa học đều khẳng định Lươn Điện là loài sát thủ cô độc tuyệt đối, đi săn một mình vào ban đêm! |  | Bức tranh cũ vẽ một con lươn điện bơi cô đơn một mình giữa dòng sông tối đen như mực; KHÔNG có anh MC trong cảnh này. |
| b13 | 01:49.2–01:58.0 (8.7s) | L209 | Cho đến tháng giêng năm 2021, nhóm nghiên cứu của giáo sư Douglas Bastos và tiến sĩ David de Santana công bố phát hiện kinh hoàng trên tạp chí Ecology and Evolution! |  | Hình ảnh chiếc máy quay dưới nước ghi lại cảnh tượng chưa từng có trong tự nhiên tại một hồ nước nông nối với sông Iriri; KHÔNG có anh MC trong cảnh này. |
| b14 | 01:58.0–02:08.0 (10.1s) | L210 | Họ phát hiện một bầy đàn khổng lồ gồm hơn 100 con Lươn Điện trưởng thành — dài từ 1,2-1,8m — đang tụ họp và phối hợp săn mồi tập thể giống hệt như bầy sói hay đàn cá voi sát thủ! | **> 100 CON** · Săn mồi theo bầy đàn · R/380 · [0.66, 0.5] | Hơn một trăm con chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh bơi thành vòng tròn lớn rộng hàng chục mét, tỏa ra ánh sáng xanh neon rực rỡ khắp mặt hồ nước tối; KHÔNG có anh MC trong cảnh này. |
| b15 | 02:08.0–02:15.3 (7.3s) | L211 | Mỗi khi bình minh và hoàng hôn buông xuống, hơn 100 con lươn này cùng bơi vòng tròn lùa hàng ngàn con cá nhỏ dồn chặt lại thành một quả cầu mồi khổng lồ sát bờ |  | Hàng ngàn chú cá nhỏ bị dồn ép co cụm lại thành một quả cầu bạc xoay tròn ở vùng nước cạn, bị vây kín tứ phía bởi bức tường lươn điện; KHÔNG có anh MC trong cảnh này. |
| b16 | 02:15.3–02:23.4 (8.1s) | L212 | nước nông! Sau đó, từng tốp từ 2-10 con Lươn Điện tách đội hình áp sát quả cầu mồi, và cùng lúc phát động một loạt xung điện đồng loạt với tổng điện áp cộng hưởng cực |  | Tốp mười con chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh đồng loạt phóng những tia sét xanh tím chói lòa vào quả cầu cá nhỏ, mặt nước sủi bọt phát sáng như có sấm sét đánh trúng; KHÔNG có anh MC trong cảnh này. |
| b17 | 02:23.4–02:34.1 (10.7s) | L213 | đại! Cú phóng điện tập thể mạnh đến nỗi khiến hàng trăm con cá nhỏ bị giật văng bắn tung lên không trung rồi rơi xuống mặt nước bất tỉnh nhân sự, trở thành bữa tiệc thịnh soạn cho cả trăm thành viên trong bầy! |  | Cá nhỏ bay vọt lên khỏi mặt nước rơi xuống lả tả, cả đàn lươn điện thong thả chia nhau thưởng thức bữa tiệc công bằng hòa thuận; KHÔNG có anh MC trong cảnh này. |
| b18 | 02:34.1–02:42.0 (7.9s) | L214 | Tuyển thủ thứ ba bước vào vòng đấu xã hội không dùng đến vũ khí giật điện hay búng càng, mà chinh phục khán đài bằng tình mẫu tử vĩ đại của đại gia đình: Capybara! |  | Bức tranh ấm áp của một đại gia đình chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia đông đúc gồm bốn năm con mẹ và hàng chục chú chuột con mũm mĩm đáng yêu đang nằm sưởi nắng bên bờ sông; KHÔNG có anh MC trong cảnh này. |
| b19 | 02:42.0–02:49.2 (7.2s) | L215 | Nghiên cứu về hành vi nuôi con hộ alloparenting do các nhà khoa học Brazil thực hiện đã hé lộ một nét văn hóa cộng đồng cực kỳ nhân văn của Bố Già đầm lầy! |  | Các mẹ chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia nằm cạnh nhau cho một bầy con nhỏ khoảng tám đến mười bé cùng bú sữa một cách vô tư bình đẳng; KHÔNG có anh MC trong cảnh này. |
| b20 | 02:49.2–03:01.2 (12.0s) | L216 | Trong một bầy Capybara, tất cả các con cái thường là chị em họ hàng gần gũi. Khi sinh con vào cùng thời điểm, các bà mẹ sẵn sàng cho bất kỳ đứa trẻ nào trong đàn đến bú sữa mà hoàn toàn không phân biệt đâu là con ruột của mình, đâu là con của hàng xóm! |  | Một chú chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia con mũm mĩm chạy từ mẹ này sang mẹ kia xin bú sữa và đều được các cô các dì vỗ về liếm lông âu yếm; KHÔNG có anh MC trong cảnh này. |
| b21 | 03:01.2–03:13.2 (12.0s) | L217 | Thậm chí ngay từ khi mới sinh ra vài ngày tuổi, chuột con đã mở mắt, mọc đủ lông, biết đi lại và bơi lội theo cả đại gia đình, được tất cả các bác các chú trong bầy cùng đứng gác sủa báo động bảo vệ trước báo đốm và trăn gấm! |  | Những chú chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia con tí hon bơi nối đuôi nhau ngay phía sau lưng đàn bố mẹ lớn, ánh mắt hạnh phúc an toàn tuyệt đối; KHÔNG có anh MC trong cảnh này. |
| b22 | 03:13.2–03:23.4 (10.3s) | L218 | Không chịu thua trước các xã hội đoàn kết của Tôm Súng, Lươn Điện hay Capybara, Chim Tu Hú bước lên bục để trình diễn cuộc chạy đua vũ trang tâm lý căng thẳng với chính các chim chủ nhà! |  | chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái đứng trước tấm bảng chiến thuật đầy mũi tên đối đầu giữa chim ký sinh và chim chủ nhà; KHÔNG có anh MC trong cảnh này. |
| b23 | 03:23.4–03:30.6 (7.2s) | L219 | Các nhà điểu học phát hiện rằng: một số loài chim chủ thông minh đã tiến hóa khả năng nhận diện hoa văn trứng lạ tinh tường đến mức tự mình kiểm tra từng quả trứng trong tổ! |  | Chú chim chích mẹ đeo kính lúp soi xét tỉ mỉ từng chấm đốm trên vỏ trứng trong tổ mình, phát hiện quả trứng có đốm lệch liền hất ra ngoài; KHÔNG có anh MC trong cảnh này. |
| b24 | 03:30.6–03:40.7 (10.1s) | L220 | Vì thế, Chim Tu Hú mẹ phải phát triển bộ nhớ không gian siêu việt để ghi nhớ vị trí và lịch đẻ trứng của hàng chục tổ chim hàng xóm cùng lúc, căn đúng khung giờ chiều vắng mặt để đánh tráo trứng hoàn hảo! |  | Bản đồ khu rừng trong đầu chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái hiện sáng rực vị trí hàng chục chiếc tổ chim hàng xóm kèm đồng hồ đếm ngược thời gian ra vào của từng nhà; KHÔNG có anh MC trong cảnh này. |
| b25 | 03:40.7–03:48.8 (8.0s) | L221 | Ban giám khảo xin công bố kết quả Vòng năm! Huy chương đồng thuộc về Capybara với văn hóa nuôi con tập thể không phân biệt vô cùng nhân văn! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ trao huy chương đồng cho chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia đang âu yếm vỗ về đàn con nhỏ; khán đài thả tim rợp trời. |
| b26 | 03:48.8–03:58.1 (9.3s) | L222 | Huy chương bạc thuộc về Lươn Điện với chiến thuật săn mồi bầy đàn hơn 100 con! Và Huy chương vàng thuộc về Tôm Súng với xã hội ong kiến 300 tôm lính dưới đáy biển! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ trao huy chương bạc cho chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh và huy chương vàng cho chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa; tiếng hò reo vang dội đấu trường |
| b27 | 03:58.1–04:09.6 (11.5s) | L223 | Bảng tổng sắp sau Vòng năm thay đổi vị trí dẫn đầu: Tôm Súng vọt lên ngôi đầu với 6 điểm! Lươn Điện và Gấu Trúc Lớn bám sát phía sau với 4 điểm! Cá Cung Thủ, Quỷ Gai, Hà Mã và Capybara đồng 3 điểm! |  | tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) cập nhật cột điểm cao vút của chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa ở vị trí dẫn đầu; cuộc đua bắt đầu bước vào giai đoạn khốc liệt nhất! |
| b28 | 04:09.6–04:16.5 (6.9s) | L224 | Vòng sáu ngay sau đây sẽ đưa chúng ta bay qua nửa vòng Trái Đất và lặn xuống đáy sông châu Phi trong thử thách Hành trình vĩ đại và định vị không gian! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng giơ cao quả địa cầu phát sáng chuẩn bị cho hành trình phiêu lưu vạn dặm ở Vòng sáu. |

### scene08 · HÀNH TRÌNH VĨ ĐẠI VÀ SIÊU GIÁC QUAN ĐỊNH VỊ KHÔNG GIAN · 277.2s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:13.3 (13.3s) | L225 | Chào mừng toàn thể khán đài bước vào Vòng sáu: Hành trình vĩ đại và siêu giác quan định vị không gian! Ở vòng thi này, ban giám khảo sẽ kiểm tra khả năng vượt không gian và cách các tuyển thủ giao tiếp bằng những giác quan mà con người không hề có! |  | Sân vận động trình chiếu một quả địa cầu 3D khổng lồ xoay tròn giữa không gian với các đường bay xuyên lục địa và sóng âm dưới đáy sông; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cầm chiếc la bàn vàng. |
| b02 | 00:13.3–00:19.8 (6.5s) | L226 | Từ bầu trời Bắc Âu băng giá cho tới lòng sông đục ngầu châu Phi, đấu sĩ nào xứng đáng nhận danh hiệu bậc thầy định vị tối thượng? |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ đặt quả địa cầu nhỏ lên bàn, cầm chiếc kính lúp soi vào những tuyến đường di cư chằng chịt khắp hành tinh. |
| b03 | 00:19.8–00:31.9 (12.1s) | L227 | Tuyển thủ mở màn vòng thi di chuyển khiến tất cả mọi người phải ngước nhìn lên bầu trời: Siêu Trộm Tổ Ấm Chim Tu Hú! Khán giả quen thấy nó loanh quanh bên tổ chim chích, nhưng khả năng bay đường dài của nó mới thực sự là huyền thoại! |  | chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái đứng trên bục xuất phát, trên lưng gắn một chiếc ba lô phát tín hiệu vệ tinh siêu nhẹ màu bạc lấp lánh; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:31.9–00:40.7 (8.8s) | L228 | Năm 2014, nhóm nghiên cứu của nhà điểu học Mikkel Willemoes công bố trên tạp chí PLOS ONE kết quả theo dõi vệ tinh đột phá nhất từng thực hiện trên loài Chim Tu Hú! |  | Màn hình vệ tinh hiện lên bản đồ châu Âu và châu Phi với những vệt sáng đỏ theo dõi hành trình của tám chú chim Tu Hú gắn chip nặng 5 gam; KHÔNG có anh MC trong cảnh này. |
| b05 | 00:40.7–00:50.1 (9.4s) | L229 | Thông thường, những loài chim di cư đi đơn độc ban đêm như Tu Hú được cho là bay tản mát theo hướng ngẫu nhiên. Nhưng dữ liệu vệ tinh từ Đan Mạch và Thụy Điển đã cho thấy một sự thật kinh ngạc! |  | Quỹ đạo bay của các chú chim chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái hiện lên trên màn hình bản đồ dưới dạng một đường vòng cung khổng lồ cực kỳ đồng nhất; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:50.1–00:58.4 (8.3s) | L230 | Mỗi năm, một chú Chim Tu Hú nhỏ bé nặng khoảng 100g tự mình bay đơn độc vào ban đêm một hành trình khép kín theo chiều kim đồng hồ dài tới 16.000km! | **16.000 KM** · Đường bay mỗi năm · L/380 · [0.38, 0.56] | Chú chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái vỗ cánh bay xuyên đêm qua biển Địa Trung Hải, sa mạc Sahara mênh mông để tiến tới những cánh rừng mưa nhiệt đới ở Trung Phi; KHÔNG có anh MC trong cảnh này. |
| b07 | 00:58.4–01:09.2 (10.8s) | L231 | Điều khó tin hơn cả: sau khi vượt hơn 5.000km xuyên qua sa mạc Sahara chết chóc để tới vùng Sahel phía Đông, khoảng cách sai lệch giữa những con chim bay riêng lẻ này trung bình chỉ cách nhau đúng 164km! |  | Mũi tên vệ tinh đo khoảng cách giữa các điểm dừng chân của bầy chim ở vùng Sahel châu Phi cực kỳ sát sao như được lập trình bằng GPS; KHÔNG có anh MC trong cảnh này. |
| b08 | 01:09.2–01:20.7 (11.5s) | L232 | Từ Bắc Âu xuống Đông Nam Âu, sang Trung Phi trú đông, rồi vòng qua Tây Phi bay ngược về châu Âu vào mùa xuân! Một hệ thống định vị GPS sinh học bẩm sinh với sáu trạm dừng chân cố định qua hàng triệu năm không sai một nhịp! |  | Chuỗi sáu điểm dừng chân phát sáng trên bản đồ từ Đan Mạch xuống Congo rồi vòng qua Tây Phi trở về nhà, cả khán đài vỗ tay vang dội; KHÔNG có anh MC trong cảnh này. |
| b09 | 01:20.7–01:28.9 (8.3s) | L233 | Rời khỏi bầu trời 16.000km, chúng ta lặn sâu xuống lòng sông đục ngầu châu Phi để kiểm tra siêu giác quan dưới nước của cỗ xe tăng 3 tấn: Hà |  | chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ bước xuống bể kính sâu trong suốt, đôi tai nhỏ xíu trên đỉnh đầu khép chặt lại, lỗ mũi đóng kín mít như van tàu ngầm; KHÔNG có anh MC trong cảnh này. |
| b10 | 01:28.9–01:40.1 (11.1s) | L234 | Mã! Câu hỏi đặt ra cho ban giám khảo là: khi lặn hoàn toàn dưới nước tối tăm với đôi tai đã gập kín để ngăn nước vào, làm sao Hà Mã vẫn nghe được âm thanh và xác định chính xác hướng gọi của đồng loại từ dưới đáy sông? |  | Sơ đồ giải phẫu đầu chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ dưới nước: sóng âm thanh lan truyền trong nước nhanh gấp năm lần trong không khí dội tới chiếc đầu đồ sộ; KHÔNG có anh MC trong cảnh này. |
| b11 | 01:40.1–01:48.0 (7.9s) | L235 | Nghiên cứu âm học dưới nước của tiến sĩ William Barklow đã giải mã khả năng thính giác lưỡng cư độc nhất vô nhị này: Hà Mã nghe âm thanh dưới nước bằng... xương hàm dưới! |  | Cận cảnh chiếc xương hàm dưới khổng lồ của chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ: một khối mô mỡ truyền âm đặc biệt nối từ xương hàm chạy thẳng lên hộp sọ tai trong; KHÔNG có anh MC trong cảnh này. |
| b12 | 01:48.0–01:59.6 (11.6s) | L236 | Khi âm thanh dưới nước truyền tới, rung động đập vào xương hàm dưới, truyền qua dải mô mỡ dẫn âm thẳng vào tai trong bên trái và bên phải, giúp Hà Mã xác định chính xác phương hướng âm thanh giống hệt như người anh em họ xa Cá Heo và Cá Voi! |  | Các vòng sóng âm dưới nước chạm vào hai bên hàm dưới của chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ rồi truyền tín hiệu sáng rực thẳng vào hai tai trong; KHÔNG có anh MC trong cảnh này. |
| b13 | 01:59.6–02:11.2 (11.6s) | L237 | Đặc biệt hơn, Hà Mã còn phát ra các xung âm thanh lưỡng cư đồng thời vào cả không khí phía trên lẫn dòng nước phía dưới! Nhờ cơ chế truyền rung động qua hàm dưới, tiếng gọi bầy đàn trầm đục của nó vang xa hàng cây số xuyên thấu mọi lớp bùn đục! |  | chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ ngâm một nửa mõm dưới mặt nước phát ra tiếng kêu vang rền làm mặt nước rung lên từng đợt sóng đồng tâm lan tỏa cả hai môi trường; KHÔNG có anh MC trong cảnh này. |
| b14 | 02:11.2–02:18.6 (7.4s) | L238 | Và tuyển thủ thứ ba bước vào bài thi định vị không gian sẽ mang lại cho quý vị một màn trình diễn vừa hài hước vừa khôn ngoan: Gấu Trúc Lớn! |  | chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu đứng trước một hàng cây thông thẳng tắp trong khu vực thi đấu đánh dấu lãnh thổ; KHÔNG có anh MC trong cảnh này. |
| b15 | 02:18.6–02:27.8 (9.2s) | L239 | Vì sống cô độc giữa rừng tre rậm rạp mênh mông, Gấu Trúc giao tiếp với đồng loại qua những 'bảng tin mùi hương' tiết ra từ tuyến mùi dưới đuôi và nước tiểu quệt lên thân cây! |  | Một cái cây thông có những vạch đánh dấu phát sáng như bảng tin nhắn mùi hương của cộng đồng gấu trúc trong rừng; KHÔNG có anh MC trong cảnh này. |
| b16 | 02:27.8–02:38.7 (11.0s) | L240 | Nhưng ở đây có một quy luật cạnh tranh ngầm cực kỳ khốc liệt: vết mùi càng nằm ở vị trí cao trên thân cây thì chủ nhân của nó càng được coi là to lớn, khỏe mạnh và đáng gờm nhất! Vậy một chú Gấu Trúc đực lùn mũm mĩm phải làm sao? |  | Hai chú chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu đứng so chiều cao cạnh gốc cây, chú gấu mũm mĩm nhìn ngọn cây cao chót vót mà gãi đầu suy nghĩ mưu mẹo; KHÔNG có anh MC trong cảnh này. |
| b17 | 02:38.7–02:50.8 (12.0s) | L241 | Nghiên cứu của tiến sĩ Ron Swaisgood tại vườn thú San Diego và khu bảo tồn Ngọa Long ghi nhận một pha xiếc thú không tưởng: Gấu Trúc đực chống hai tay trước xuống đất, lộn ngược người... trồng cây chuối đẩy hai chân sau bò ngược lên thân cây! |  | chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu chống hai tay trước vững vàng, vắt ngược hai chân sau lên cao dọc theo thân cây thông một cách siêu dẻo dai như vận động viên thể dục dụng cụ; KHÔNG có anh MC trong cảnh này. |
| b18 | 02:50.8–03:03.9 (13.2s) | L242 | Ở tư thế trồng cây chuối thẳng đứng đó, chú gấu xịt nước tiểu và bôi mùi hương lên cao chót vót trên thân cây! Một chiêu 'khai gian chiều cao' cực kỳ thông minh khiến các tình địch trẻ tuổi đi ngang qua ngửi thấy liền khiếp sợ bỏ đi không dám gây sự! |  | Một chú gấu trúc trẻ khác đi ngang qua ngửi thấy vết mùi cao tít trên đầu liền hoảng hốt tưởng đối thủ cao ba mét vội vàng quay đầu chạy mất dép; KHÔNG có anh MC trong cảnh này. |
| b19 | 03:03.9–03:11.9 (7.9s) | L243 | Cũng trong bài thi di chuyển không gian, hãy nhìn qua đồng hồ đo quãng đường của hai tuyển thủ sống tại ranh giới nước và cây cối: Con Lười và Cá Cung Thủ! |  | Màn hình chia đôi: một bên là tán rừng rậm Amazon xanh thẳm, một bên là vùng cửa sông rừng ngập mặn giao thoa nước ngọt và nước mặn; KHÔNG có anh MC trong cảnh này. |
| b20 | 03:11.9–03:18.4 (6.5s) | L244 | Trên những ngọn cây cao, trung bình mỗi ngày Con Lười chỉ di chuyển được vỏn vẹn khoảng 38m — tức là chưa bằng một nửa chiều dài sân |  | Thước đo quãng đường hiển thị con số 38 mét màu xanh dịu; chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini thong thả trèo từng bước một qua tán lá rậm; KHÔNG có anh MC trong cảnh này. |
| b21 | 03:18.4–03:29.7 (11.3s) | L245 | bóng đá! Nhưng điều kỳ diệu là dù sống ở vùng cửa sông nơi độ mặn thay đổi chóng mặt theo thủy triều mỗi ngày, Cá Cung Thủ vẫn điều chỉnh được áp suất thẩm thấu trong máu một cách hoàn hảo để sống khỏe ở cả nước ngọt lẫn nước lợ! |  | Sơ đồ mang cá chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn: các tế bào chuyên biệt tự động bơm thải muối thừa lúc nước triều dâng và giữ lại muối khoáng khi nước sông ngọt tràn về; KHÔNG có anh MC trong cảnh này. |
| b22 | 03:29.7–03:35.9 (6.2s) | L246 | Và đừng quên khả năng tăng tốc tẩu thoát bất ngờ trên cạn của Bố Già Capybara khi phát hiện kẻ săn mồi nguy hiểm tiếp cận bất ngờ! |  | Một con báo đốm rình rập sau bụi cỏ lao vọt ra tấn công, chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia lập tức chuyển từ chế độ điềm đạm sang chế độ chạy nước rút; KHÔNG có anh MC trong cảnh này. |
| b23 | 03:35.9–03:48.4 (12.5s) | L247 | Nhờ cấu tạo bốn ngón có màng ở hai chân trước và ba ngón có màng ở hai chân sau, Bố Già đầm lầy phóng mình lao thẳng xuống dòng sông sâu chỉ trong nháy mắt, đồng thời chuyển hẳn đồng hồ sinh học sang kiếm ăn hoàn toàn vào ban đêm khi khu vực có nhiều mối đe dọa rình rập! |  | chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia tung cú nhảy gọn lẹ xuống lòng sông dưới ánh trăng đêm, bốn chân màng rẽ nước bơi biến mất tăm nhanh chóng; KHÔNG có anh MC trong cảnh này. |
| b24 | 03:48.4–03:58.7 (10.3s) | L248 | Còn anh chàng Tôm Súng dưới rạn san hô lại có một chiến thuật giữ liên lạc đặc biệt: mỗi khi bầy tôm lính búng càng đồng loạt, sóng âm thanh vang xa hàng trăm mét dưới đáy biển để cảnh báo lãnh thổ cho các rạn lân cận! |  | Sóng âm thanh cộng hưởng từ tổ bọt biển của chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa lan tỏa qua các rạn san hô rực rỡ sắc màu dưới đáy đại dương; KHÔNG có anh MC trong cảnh này. |
| b25 | 03:58.7–04:06.4 (7.8s) | L249 | Kết quả Vòng sáu tuyệt vời đã có! Huy chương đồng thuộc về Gấu Trúc Lớn với tuyệt chiêu trồng cây chuối đánh dấu lãnh thổ lừa tình địch! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ trao huy chương đồng cho chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu đang chống hai tay trồng cây chuối ăn mừng khiến cả khán đài cười ồ thích thú. |
| b26 | 04:06.4–04:15.7 (9.2s) | L250 | Huy chương bạc thuộc về Hà Mã với công nghệ nghe âm thanh dưới nước qua xương hàm dưới! Và Huy chương vàng thuộc về Chim Tu Hú với đường bay vệ tinh 16.000km! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ trao huy chương bạc cho chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ và huy chương vàng lấp lánh cho chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái; tiếng vỗ tay vang rền đấ |
| b27 | 04:15.7–04:29.5 (13.9s) | L251 | Bảng điểm sau Vòng sáu trở nên cực kỳ sít sao: Tôm Súng dẫn đầu với 6 điểm! Hà Mã và Gấu Trúc Lớn đồng hạng nhì với 5 điểm! Lươn Điện và Chim Tu Hú bám sát với 4 điểm! Cá Cung Thủ, Quỷ Gai và Capybara đồng 3 điểm! Bọ Pháo Thủ 2 điểm và Con Lười 1 |  | tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) sáng rực màn hình với mười cột điểm san sát nhau cực kỳ gay cấn, mọi khoảng cách đều có thể bị san lấp trong nháy mắt! |
| b28 | 04:29.5–04:37.2 (7.7s) | L252 | điểm! Bây giờ, trước khi bước vào ba chặng đua nước rút cuối cùng, mời toàn thể quý vị đến với Lễ Trao Giải Phụ: Di sản tiền sử và những họ hàng quái đản nhất! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vung tay biến sàn đấu thành bảo tàng cổ sinh vật học với những bộ xương hóa thạch khổng lồ và ánh đèn tím huyền bí. |

### scene09 · CÁC CỤ TỔ KHỔNG LỒ 4 TẤN VÀ NHỮNG HỌ HÀNG DỊ BIỆT · 226.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.7 (7.7s) | L253 | Chào mừng toàn thể quý vị khán giả đến với sự kiện đặc biệt giữa hiệp hai của Mùa 2: Bảo Tàng Di Sản Tiến Hóa và Lễ Trao Giải Phụ! |  | Đấu trường hóa thành bảo tàng lịch sử tự nhiên hoành tráng với các bộ xương hóa thạch phát sáng lung linh; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vest đỏ cầm chiếc đèn pin vàng soi chiếu các kỷ nguyên cổ đại. |
| b02 | 00:07.7–00:16.0 (8.3s) | L254 | Không tính vào điểm vô địch, nhưng lễ trao giải phụ đêm nay sẽ bật mí những bí mật chấn động về cụ tổ tiền sử và những người anh em họ hàng kỳ quái nhất của các tuyển thủ! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ đội chiếc mũ khảo cổ học trên mái tóc giả trắng, cầm chiếc chổi quét bụi hóa thạch và bốn chiếc cúp kỷ niệm bằng đồng thau cổ kính. |
| b03 | 00:16.0–00:24.5 (8.5s) | L255 | Danh hiệu phụ đầu tiên — Giải thưởng 'Cụ Tổ Khổng Lồ Đáng Sợ Nhất Tiền Sử' — xin được xướng tên họ hàng cổ đại của chú Con Lười bé nhỏ đang ngồi ngủ gật kia! |  | Màn hình chiếu bức tranh cổ sinh vật học Nam Mỹ thời Kỷ Băng Hà: bóng dáng khổng lồ của một con thú cao sáu mét che rợp cả khu rừng; chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini mở to mắt ngạc nhiên; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:24.5–00:35.0 (10.5s) | L256 | Nếu ngày nay Con Lười chỉ nặng khoảng bốn đến 5kg và treo lơ lửng trên ngọn cây, thì chỉ khoảng 10.000 năm trước, cụ tổ của nó mang tên Lười Đất Khổng Lồ Megatherium là một quái vật ngang ngửa voi ma mút! |  | So sánh kích thước: chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini hiện đại nhỏ như chú mèo ngồi trên lòng bàn chân khổng lồ của cụ tổ Megatherium đứng thẳng cao sáu mét nặng bốn tấn; KHÔNG có anh MC trong cảnh này. |
| b05 | 00:35.0–00:44.8 (9.8s) | L257 | Với chiều cao khi đứng thẳng lên tới 6m và nặng tới 4 tấn, Lười Đất Khổng Lồ sở hữu bộ móng vuốt dài ngang thanh kiếm để đào những đường hầm ngầm khổng lồ xuyên qua lớp đất đá cứng ở Nam Mỹ! | **NẶNG 4 TẤN** · Cụ tổ Con Lười xưa · L/380 · [0.44, 0.45] | Một đường hầm khổng lồ rộng mấy mét có dấu cào móng vuốt khổng lồ trên vách đá tại Brazil, các nhà khảo cổ học đi bộ bên trong kinh ngạc; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:44.8–00:54.8 (10.1s) | L258 | Những đường hầm cổ đại mang tên Paleoburrows tại Brazil dài hàng trăm mét và cao tới 2m vẫn còn nguyên vẹn vết cào khổng lồ trên vách đá, khiến các nhà địa chất từng lầm tưởng là công trình của người cổ đại! |  | Nhà địa chất học soi đèn pin lên trần hang động đầy vết cào móng vuốt song song đều tăm tắp rộng hàng mét; KHÔNG có anh MC trong cảnh này. |
| b07 | 00:54.8–01:05.1 (10.3s) | L259 | Thậm chí từng tồn tại một nhánh họ hàng mang tên Lười Biển Thalassocnus sống dọc bờ biển Peru, tiến hóa bộ xương nặng trĩu để lặn xuống đáy Thái Bình Dương gặm rong biển hệt như loài bò biển! |  | Bức tranh phục dựng chú Lười Biển cổ đại bơi lặn dưới đáy đại dương Peru cổ đại gặm thảm cỏ biển xanh mướt; KHÔNG có anh MC trong cảnh này. |
| b08 | 01:05.1–01:09.0 (3.9s) | L260 | Một cúp lưu niệm hóa thạch xứng đáng được trao tặng cho dòng họ Lười vĩ đại! |  | chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini chậm rãi giơ tay nhận chiếc cúp hình xương hóa thạch nhỏ từ tay bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ, nụ cười tự hào rạng rỡ; KHÔNG có anh MC trong cảnh này. |
| b09 | 01:09.0–01:18.3 (9.2s) | L261 | Danh hiệu phụ thứ hai — Giải thưởng 'Cuộc Đào Tẩu Hóa Thạch Lâu Đời Nhất' — thuộc về Gấu Trúc Lớn với hóa thạch cụ tổ Ailurarctos 8 triệu năm tuổi tại tỉnh Vân Nam! |  | Chiếc hộp kính trưng bày hóa thạch xương hàm và ngón tay giả thứ sáu cổ đại tám triệu năm tuổi vừa được khai quật tại Trung Quốc; KHÔNG có anh MC trong cảnh này. |
| b10 | 01:18.3–01:28.0 (9.7s) | L262 | Phát hiện hóa thạch này chứng minh rằng ngay từ 8 triệu năm trước, tổ tiên của Gấu Trúc đã có chiếc xương cổ tay mọc dài ra thành ngón tay giả thứ sáu để cầm nắm thân tre ăn uống! |  | Bức tranh phục dựng chú gấu trúc cổ đại tám triệu năm trước đang dùng sáu ngón tay kẹp cành trúc ăn ngon lành bên bờ hồ cổ; KHÔNG có anh MC trong cảnh này. |
| b11 | 01:28.0–01:35.6 (7.6s) | L263 | Danh hiệu phụ thứ ba — Giải thưởng 'Điệp Viên Nằm Vùng Bất Tử' — khiến cả hội đồng khoa học phải bật cười nghiêng ngả, thuộc về họ hàng nhà Bọ Pháo Thủ mang tên Paussinae! |  | Kính lúp phóng đại một chú bọ cánh cứng kỳ lạ có đôi râu dẹt hình chiếc lá to bản đang hiên ngang bước thẳng vào cửa hang của một đàn kiến lửa hung dữ; KHÔNG có anh MC trong cảnh này. |
| b12 | 01:35.6–01:45.7 (10.0s) | L264 | Khác với Bọ Pháo Thủ của chúng ta dùng súng 100°C bắn nhau tóe lửa, nhánh họ hàng Paussinae lại cất súng đi và tiến hóa tuyến tiết ra đúng hợp chất hóa học mùi hương của... Kiến Chúa! |  | Đàn kiến thợ hung dữ vừa chạy tới định cắn nhưng ngửi thấy mùi thơm giống hệt Kiến Chúa liền cúi rạp đầu cung kính rước chú bọ vào tận sâu bên trong tổ; KHÔNG có anh MC trong cảnh này. |
| b13 | 01:45.7–01:56.7 (11.0s) | L265 | Chui vào tận phòng ngủ hoàng gia của đàn kiến, chú bọ này sống êm ấm như một vị hoàng đế, được kiến thợ chăm sóc hầu hạ lau chùi, và thỉnh thoảng lén ăn thịt luôn cả ấu trùng kiến con mà đàn kiến không hề hay biết! |  | Chú bọ nằm phơi bụng trên chiếc ngai vàng giữa tổ kiến, đàn kiến thợ cần mẫn đút mồi và chải râu phục vụ, chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C lắc đầu cười khoái chí; KHÔNG có anh MC trong cảnh này. |
| b14 | 01:56.7–02:04.0 (7.3s) | L266 | Và danh hiệu phụ cuối cùng — Giải thưởng 'Dòng Họ Điệp Viên Bí Ẩn Nhất' — dành tặng cho các cô nàng Chim Tu Hú với bí mật di truyền mang tên Gentes! |  | Sơ đồ nhiễm sắc thể giới tính W của chim cái chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái phát sáng lấp lánh bên cạnh bốn quả trứng mang bốn màu sắc xanh, nâu, đốm và trắng hoàn toàn khác nhau; KHÔNG có anh MC trong cảnh này. |
| b15 | 02:04.0–02:10.3 (6.2s) | L267 | Làm sao một loài chim Tu Hú có thể làm giả trứng giống hệt của hàng chục loài chim chủ khác nhau mà không bị lai tạp màu sắc lẫn lộn? |  | Hai con chim Tu Hú cái cùng loài bay theo hai hướng khác nhau: một con chỉ đẻ trứng xanh giống chim chích sậy, con kia chỉ đẻ trứng trắng đốm giống chim chích bụi; KHÔNG có anh MC trong cảnh này. |
| b16 | 02:10.3–02:18.2 (7.9s) | L268 | Các nhà di truyền học giải mã được rằng: bộ gen quy định màu sắc và hoa văn vỏ trứng của Tu Hú nằm trọn trên nhiễm sắc thể W — thứ chỉ truyền thẳng từ chim mẹ sang con |  | Chuỗi ADN phát sáng trên nhiễm sắc thể W chuyển thẳng công thức phối màu vỏ trứng từ chim mẹ sang chim con gái; KHÔNG có anh MC trong cảnh này. |
| b17 | 02:18.2–02:26.2 (8.0s) | L269 | gái! Nhờ vậy, trong cùng một loài chia thành hàng chục dòng họ bí mật truyền nghề gia truyền suốt hàng ngàn năm mà không bao giờ bị mất bí kíp! |  | Cuốn gia phả bí truyền màu sắc vỏ trứng của dòng họ chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái được truyền qua từng thế hệ mẹ con, cả khán đài gật gù thán phục; KHÔNG có anh MC trong cảnh này. |
| b18 | 02:26.2–02:37.7 (11.5s) | L270 | Và giải thưởng phụ thứ năm — danh hiệu 'Khu Vườn Sinh Thái Di Động Đông Đúc Nhất' — tiếp tục gọi tên Con Lười với hơn 900 con bọ cánh cứng, bướm đêm và hàng triệu vi sinh vật chung sống hòa bình trên cùng một bộ lông! |  | Kính phóng đại soi vào bộ lông chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini: giống như một thành phố thu nhỏ có cả bọ cánh cứng, bướm đêm, tảo xanh và nấm cùng sinh hoạt nhộn nhịp; KHÔNG có anh MC trong cảnh này. |
| b19 | 02:37.7–02:48.6 (11.0s) | L271 | Trên thực tế, mỗi sợi lông thô bên ngoài của Con Lười có các vết nứt siêu nhỏ chạy dọc theo chiều dài, đóng vai trò như những căn hộ chung cư lý tưởng giữ nước mưa để cả hệ sinh thái tí hon cùng phát triển! |  | Ảnh minh họa khoa học dưới kính lúp phóng đại một sợi rêu xanh và bộ lông chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini với những hốc nhỏ li ti chứa giọt nước mưa trong veo và các cụm vi nấm tí hon đang phát sáng lung linh; KHÔNG có anh MC trong cảnh này. |
| b20 | 02:48.6–02:57.6 (9.0s) | L272 | Tiếp theo là giải thưởng 'Sinh Con Khắc Nghiệt Nhất Thế Giới Thú' dành cho Gấu Trúc Lớn! Trong khoảng gần một nửa số ca sinh nở, gấu trúc mẹ đẻ ra hai chú gấu con sinh đôi tí hon yếu |  | Mẹ chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu nằm ôm hai chú gấu con hồng hào nhỏ xíu vừa chào đời trong hang đá phủ tuyết trắng; KHÔNG có anh MC trong cảnh này. |
| b21 | 02:57.6–03:06.1 (8.5s) | L273 | ớt! Trong suốt tuần đầu tiên sau khi sinh, gấu mẹ khổng lồ phải ôm chặt đứa con bé bằng ngón tay cái vào lòng liên tục không rời nửa bước để truyền hơi ấm! |  | Mẹ chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu nhắm mắt âu yếm ôm ấp gấu con hồng hào trong vòng tay ấm áp giữa mùa đông tuyết trắng; KHÔNG có anh MC trong cảnh này. |
| b22 | 03:06.1–03:17.7 (11.5s) | L274 | Tuy nhiên trong tự nhiên, nguồn sữa ít ỏi từ khẩu phần ăn tre chỉ đủ cho mẹ nuôi đúng một đứa con khỏe mạnh hơn, đồng thời gấu con sinh ra điếc đặc và phải mất tới 45 ngày sau mới mở mắt nhìn thế giới lần đầu tiên! |  | Chú gấu con bắt đầu mọc lốm đốm lông đen ở tai và mắt sau vài tuần, từ từ mở đôi mắt tròn xoe dễ thương; KHÔNG có anh MC trong cảnh này. |
| b23 | 03:17.7–03:28.3 (10.6s) | L275 | Cuối cùng là giải 'Bậc Thầy Hợp Tác Không Cần Ngôn Ngữ' dành cho cặp bạn thân Tôm Súng và Cá Bống! Dù Tôm Súng mắt cực kém, chỉ cần một cái chạm râu nhẹ lên đuôi Cá Bống là cả hai phối hợp tác chiến ăn ý hàng chục năm liền! |  | chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa và chú cá bống nhỏ bắt tay ăn mừng chiếc cúp tình bạn pha lê, cả khán đài mỉm cười ấm áp; KHÔNG có anh MC trong cảnh này. |
| b24 | 03:28.3–03:36.5 (8.2s) | L276 | Tôm Súng cặm cụi dọn dẹp xây sửa căn hầm dưới cát mỗi ngày, còn Cá Bống kiên nhẫn đứng gác cửa và thậm chí chia sẻ luôn cả những mẩu thức ăn thừa cho người bạn thợ xây mù |  | Cảnh tượng ấm áp dưới đáy biển: chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa đẩy cát xây hang, cá bống nhỏ bơi canh chừng phía trên bảo vệ bình yên cho ngôi nhà chung; KHÔNG có anh MC trong cảnh này. |
| b25 | 03:36.5–03:46.4 (9.9s) | L277 | lòa! Những giải thưởng phụ tuyệt vời đã giúp chúng ta hiểu sâu sắc hơn về cội nguồn của muôn loài! Bây giờ, hãy siết chặt dây an toàn vì trước mắt chúng ta là ba vòng thi quyết định vận mệnh ngôi vương! |  | Ánh đèn bảo tàng tắt dần, đèn pha đấu trường bật sáng chói lòa trở lại báo hiệu cuộc chiến căng thẳng ở Vòng bảy sắp sửa bắt đầu! |

### scene10 · PHÚC KHẢO TIN ĐỒN — ĐẬP TAN NHỮNG LẦM TƯỞNG THẾ KỶ BẰNG THỰC NGHIỆM · 258.6s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:11.2 (11.2s) | L278 | Chào mừng toàn thể khán đài bước vào Vòng bảy: Đấu trường phúc khảo tin đồn và đập tan những hiểu lầm thế kỷ! Trong thế giới tự nhiên, có rất nhiều lời đồn thổi nghe rất lọt tai nhưng thực chất lại sai hoàn toàn về mặt khoa |  | Chiếc kính lúp khổng lồ của ban giám khảo hạ xuống rọi luồng ánh sáng trắng sắc nét xuống giữa sân đấu; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cầm tập hồ sơ có đóng dấu 'PHÚC KHẢO' đứng cạnh bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ. |
| b02 | 00:11.2–00:19.2 (8.0s) | L279 | học! Ở vòng đấu này, ban giám khảo sẽ đưa ra bốn lời đồn đại phổ biến nhất về các thí sinh, sau đó dùng bằng chứng thực nghiệm để lật tẩy sự thật! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gõ búa gỗ dứt khoát, trước mặt là ba tấm huy chương vàng, bạc, đồng đang chờ trao cho những màn đính chính giá trị nhất. |
| b03 | 00:19.2–00:29.5 (10.4s) | L280 | Lời đồn số một nhắm thẳng vào Thằn Lằn Quỷ Gai: rất nhiều bài viết trên mạng khẳng định loài thằn lằn sa mạc Úc chỉ cần ngồi yên buổi sáng là sương đêm tự động ngưng tụ chảy đầy rãnh da để uống! |  | Hình ảnh chiếc bình sương buổi sáng gắn dấu hỏi chấm to đùng phía trên đầu chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:29.5–00:38.8 (9.2s) | L281 | Liệu sương sớm có thực sự đủ làm đầy mạng lưới rãnh mao dẫn trên cơ thể Quỷ Gai hay không? Tiến sĩ Philipp Comanns đã tiến hành một thí nghiệm cân đo lạnh lùng trong phòng thí nghiệm! |  | Tiến sĩ hoạt hình mặc áo blouse trắng đặt chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm vào một căn phòng lạnh 22°C rồi tăng dần độ ẩm không khí lên bão hòa như sương mù sa mạc; KHÔNG có anh MC trong cảnh này. |
| b05 | 00:38.8–00:47.6 (8.8s) | L282 | Kết quả cân đo chứng minh lời đồn đó... sai bét! Lượng hơi nước ngưng tụ từ không khí chỉ đủ làm ướt nhẹ bề mặt lớp gai ngoài cùng, hoàn toàn không đủ tạo thành giọt để chảy vào hệ thống rãnh mao |  | Các hạt sương li ti đậu trên đầu gai của chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm rồi bay hơi mất trước khi kịp chạm vào đường dẫn xuống miệng, kim cân không hề nhúc nhích; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:47.6–00:54.1 (6.5s) | L283 | dẫn! Thậm chí khi đứng trên cát có độ ẩm lên tới 22%, lượng nước hút từ cát chỉ làm đầy được 59% các rãnh |  | Màn hình hiển thị 59% rãnh mao dẫn được nạp đầy màu xanh dương khi chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm chỉ đứng yên một chỗ trên cát ẩm; KHÔNG có anh MC trong cảnh này. |
| b07 | 00:54.1–01:05.3 (11.3s) | L284 | da! Để giải khát triệt để giữa sa mạc khô cằn, Quỷ Gai phải chủ động hất cát ẩm phủ lên khắp lưng mình, ép hai mặt da hút lấy từng phân tử nước từ đất! Một phát hiện dập tắt hoàn toàn huyền thoại 'chỉ ngồi chờ sương rơi'! |  | chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm dùng bốn chân cào lớp cát ẩm tung lên phủ kín lưng mình, hệ thống rãnh da lập tức nạp đầy nước một trăm phần trăm chảy thẳng về họng; KHÔNG có anh MC trong cảnh này. |
| b08 | 01:05.3–01:15.0 (9.7s) | L285 | Lời đồn số hai gọi tên Nhà Máy Điện Sống: Lươn Điện! Suốt hàng trăm năm, mọi cuốn sách giáo khoa đều dạy rằng Lươn Điện là loài cá săn mồi cô độc tuyệt đối, ghét giao du với đồng loại! |  | Cuốn sách sinh học cũ hiện dòng chữ 'Săn mồi đơn độc' bị con dấu đỏ đóng đè lên chữ 'SAI SỰ THẬT'; KHÔNG có anh MC trong cảnh này. |
| b09 | 01:15.0–01:24.8 (9.8s) | L286 | Nhưng như chúng ta đã chứng kiến ở Vòng năm từ báo cáo tại lưu vực sông Iriri Brazil năm 2021: hơn 100 con Lươn Điện trưởng thành tụ họp và săn mồi tập thể hai lần mỗi |  | Cảnh quay thực tế dưới đáy hồ Iriri: hơn 100 con chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh vây kín quả cầu cá nhỏ rồi tung đòn sét đồng loạt như một đội quân đặc nhiệm thực thụ; KHÔNG có anh MC trong cảnh này. |
| b10 | 01:24.8–01:34.7 (9.9s) | L287 | ngày! Từ 07:30 sáng đến 17:00 chúng nghỉ ngơi yên ả dưới đáy bùn, nhưng cứ đúng bình minh và hoàng hôn là cả trăm con hợp sức tạo thành đội quân săn mồi không đối thủ! |  | Chiếc đồng hồ chia múi giờ hoạt động của đàn lươn: giờ nghỉ ngơi dưới bùn và giờ tổng tấn công lúc bình minh, hoàng hôn; KHÔNG có anh MC trong cảnh này. |
| b11 | 01:34.7–01:42.7 (8.0s) | L288 | Lời đồn số ba nhắm vào chú gấu mũm mĩm: Gấu Trúc Lớn! Nhiều người chế giễu rằng Gấu Trúc là một lỗi tiến hóa ngớ ngẩn, dễ bị tuyệt chủng vì lười biếng và vụng về! |  | Một nhóm khán giả hoạt hình chỉ tay vào chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu đang lăn tròn cười nhạo nhưng bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ giơ tay ra hiệu im lặng xem bằng chứng; KHÔNG có anh MC trong cảnh này. |
| b12 | 01:42.7–01:51.5 (8.8s) | L289 | Khoa học xin phản biện dứt khoát: Gấu Trúc chẳng hề ngớ ngẩn chút nào! Bộ lông trắng đen của nó được tính toán chính xác để ngụy trang hoàn hảo trước mắt thú ăn thịt trong rừng tuyết! |  | Hình ảnh chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu hòa lẫn vào rừng trúc phủ tuyết và bóng râm thân cây khiến báo hoa mai đi ngang qua không thể phát hiện; KHÔNG có anh MC trong cảnh này. |
| b13 | 01:51.5–01:59.9 (8.4s) | L290 | Ngoài ra, đột biến gen DUOX2 giúp nó sống khỏe bằng nguồn thức ăn ít ai thèm tranh giành, và nó còn biết dùng hợp chất phân ngựa làm thuốc giảm cảm giác lạnh mùa đông! |  | Bức tranh ghép bốn năng lực ẩn giấu của chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu: áo ngụy trang tàng hình, gen tiết kiệm năng lượng, ngón tay thứ sáu và liệu pháp chống rét; KHÔNG có anh MC trong cảnh này. |
| b14 | 01:59.9–02:05.8 (5.9s) | L291 | Nếu không bị con người thu hẹp rừng tre, Gấu Trúc hoàn toàn dư sức ngự trị vùng núi Tứ Xuyên thêm hàng triệu năm nữa! |  | chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu mỉm cười vỗ ngực đầy tự hào giữa cánh rừng tre xanh ngát, cả khán đài đồng loạt vỗ tay xin lỗi chú gấu dễ thương; KHÔNG có anh MC trong cảnh này. |
| b15 | 02:05.8–02:14.0 (8.2s) | L292 | Và lời đồn số bốn nhắm vào Bọ Pháo Thủ: Nhiều người thắc mắc tại sao phản ứng sinh nhiệt 100°C lại không làm Bọ Pháo Thủ tự thiêu rụi bụng mình ngay từ phát bắn đầu tiên? |  | Hình ảnh minh họa hài hước: một chú bọ giả tưởng bị phình bụng bốc cháy nổ tung như quả bóng bay; KHÔNG có anh MC trong cảnh này. |
| b16 | 02:14.0–02:22.3 (8.3s) | L293 | Các nhà hóa học hữu cơ giải mã bí mật cực kỳ tinh vi: hai hóa chất hydroquinone và oxy già được chứa tách biệt hoàn toàn trong một túi dự trữ an toàn không hề có chất xúc tác! |  | Sơ đồ hai buồng tách biệt: túi chứa nguyên liệu nguội lạnh nằm yên bình, cách ly hoàn toàn bởi một van cơ học đóng chặt như cửa két sắt ngân hàng; KHÔNG có anh MC trong cảnh này. |
| b17 | 02:22.3–02:32.4 (10.0s) | L294 | Phản ứng chỉ xảy ra bên trong buồng phản ứng bọc vỏ chitin cứng như gốm chịu nhiệt trong khoảnh khắc vài phần nghìn giây ngay trước khi bị tống thẳng ra ngoài! Nhờ đó chú bọ luôn an toàn tuyệt đối! |  | Buồng phản ứng lót lớp vỏ chitin siêu bền chịu nhiệt phun xả áp lực ra ngoài chỉ trong tích tắc mà thân bọ hoàn toàn mát lạnh; KHÔNG có anh MC trong cảnh này. |
| b18 | 02:32.4–02:40.8 (8.4s) | L295 | Lời đồn số năm nhắm vào Bố Già Capybara: trên mạng xã hội, nhiều người tin rằng Capybara hiền lành tuyệt đối đến mức không bao giờ cắn bất kỳ ai dù bị chọc ghẹo ra sao! |  | Hình minh họa một chú Capybara đội vòng hoa thiên thần hiền từ bên cạnh dấu hỏi chấm cảnh báo màu đỏ; KHÔNG có anh MC trong cảnh này. |
| b19 | 02:40.8–02:51.7 (10.9s) | L296 | Sự thật đính chính: dù tính tình cực kỳ điềm đạm, nhưng khi bị dồn ép vào góc tường hoặc khi bảo vệ đàn con nhỏ, cặp răng cửa sắc như dao đục của Capybara có thể tung ra cú cắn chí mạng rách toạc thịt kẻ xâm phạm! |  | chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia nhe cặp răng cửa dài sắc bén gầm gừ cảnh báo khi có kẻ lạ mặt tiến sát đàn con nhỏ, lập tức khiến chó săn giật mình lùi bước; KHÔNG có anh MC trong cảnh này. |
| b20 | 02:51.7–02:59.1 (7.4s) | L297 | Và lời đồn số sáu gọi tên Cá Cung Thủ: nhiều khán giả lầm tưởng loài cá này sống hoàn toàn bằng việc bắn rơi côn trùng đậu trên lá cây! |  | Bức tranh chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn chỉ nhìn chằm chằm lên ngọn cây phía trên mà bỏ qua mọi con cá con bơi ngang trước mũi; KHÔNG có anh MC trong cảnh này. |
| b21 | 02:59.1–03:11.6 (12.5s) | L298 | Thực tế nghiên cứu dạ dày cho thấy: phần lớn khẩu phần ăn hàng ngày của Cá Cung Thủ là tôm tép, giáp xác và cá con bơi ngay dưới mặt nước! Kỹ năng bắn tia nước hạ côn trùng là tuyệt chiêu săn mồi bổ sung khi thức ăn dưới nước trở nên khan hiếm! |  | Biểu đồ thực đơn của chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn: 80% mồi là động vật thủy sinh dưới nước, 20% còn lại là côn trùng bắn hạ từ trên không; KHÔNG có anh MC trong cảnh này. |
| b22 | 03:11.6–03:22.2 (10.7s) | L299 | Và lời đồn cuối cùng trong vòng phúc khảo nhắm vào Chim Tu Hú: nhiều khán giả cứ nghe thấy tên họ nhà Tu Hú là mặc định rằng 100% các loài chim tu hú trên Trái Đất đều đi đẻ nhờ và hất trứng hàng xóm! |  | Hình minh họa cả gia tộc chim Tu Hú đều bị dán nhãn 'Kẻ lười biếng đẻ nhờ' trên tấm bảng gỗ lớn; KHÔNG có anh MC trong cảnh này. |
| b23 | 03:22.2–03:31.6 (9.4s) | L300 | Sự thật minh oan từ cuốn chuyên khảo nổi tiếng của Đại học Oxford: trong số khoảng 140 loài thuộc họ Cu cu trên toàn thế giới, thực chất chỉ có khoảng 59 loài sống ký sinh đẻ nhờ! |  | Biểu đồ phân tách họ nhà Tu Hú: phần lớn gồm hơn tám mươi loài mang nhãn xanh 'Tự xây tổ nuôi con đàng hoàng'; KHÔNG có anh MC trong cảnh này. |
| b24 | 03:31.6–03:41.6 (9.9s) | L301 | Hơn một nửa gia tộc họ hàng của Tu Hú — với hơn 80 loài khác nhau — vẫn tự mình chăm chỉ tha rơm xây tổ, tự ấp trứng và mớm mồi nuôi con khôn lớn như những ông bố bà mẹ mẫu mực nhất! |  | Một chú chim cu cườm họ hàng nhà chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái đội mũ bảo hộ chăm chỉ xây tổ ấm cho con, chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái đứng bên cạnh gật gù bênh vực danh dự dòng họ; KHÔNG có anh MC trong cảnh này. |
| b25 | 03:41.6–03:48.9 (7.3s) | L302 | Kết quả Vòng bảy phúc khảo tin đồn: Huy chương vàng thuộc về Thằn Lằn Quỷ Gai với thí nghiệm lật tẩy huyền thoại uống sương đêm! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ trao huy chương vàng cho chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm đứng giơ cao nắm đấm ăn mừng; tiếng vỗ tay tán thưởng vang dậy khắp khán đài. |
| b26 | 03:48.9–03:57.4 (8.5s) | L408 | Huy chương bạc thuộc về Lươn Điện với bằng chứng lật đổ định kiến săn mồi cô độc! Huy chương đồng thuộc về Bọ Pháo Thủ với cơ chế van cách ly chống tự nổ! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ trao huy chương bạc cho chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh và huy chương đồng cho chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C; cả đấu trường reo hò nồng nhiệt. |
| b27 | 03:57.4–04:04.8 (7.5s) | L303 | Bảng điểm sau Vòng bảy trở nên căng thẳng đến nghẹt thở: Ba tuyển thủ đồng dẫn đầu với 6 điểm là Tôm Súng, Lươn Điện và Thằn Lằn Quỷ Gai! |  | tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) hiện lên với nhóm dẫn đầu sáu điểm san sát nhau; bầu không khí trường quay nóng hơn bao giờ hết! |
| b28 | 04:04.8–04:12.0 (7.2s) | L409 | Gấu Trúc và Hà Mã bám sát phía sau với 5 điểm! Bọ Pháo Thủ và Chim Tu Hú 4 điểm, Cá Cung Thủ và Capybara 3 điểm, Con Lười 1 điểm! |  | Bảng điểm hiển thị nhóm bám đuổi chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu, chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ ở mốc 5 điểm cùng chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác m |
| b29 | 04:12.0–04:18.6 (6.6s) | L304 | Trước mắt chúng ta chỉ còn Vòng Bán Kết và Vòng Chung Kết điểm nhân đôi! Ai sẽ bứt tốc vào phút chót? Xin mời theo dõi ngay sau đây! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vung micro chỉ về phía khu vực thử nghiệm Bán Kết rực sáng ánh đèn xanh đầy kịch tính. |

### scene11 · TIA X ĐỒNG BỘ XUYÊN BỤNG BỌ VÀ KHO BÁU THUỐC TRONG LÔNG LƯỜI · 243.2s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.3 (9.3s) | L305 | Chào mừng toàn thể quý vị khán đài bước vào Vòng Bán Kết sinh tử của Đại Hội Sinh Tồn Mùa 2! Chỉ còn một bước chân nữa thôi là chúng ta sẽ bước vào Vòng Chung Kết nhân đôi điểm |  | Đấu trường Bán Kết sáng rực với máy gia tốc tia X đồng bộ cỡ lớn, kính hiển vi phân tách thuốc sinh học và đường đua phản xạ thị giác; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đứng giữa bục dẫn chương trình. |
| b02 | 00:09.3–00:17.2 (8.0s) | L306 | số! Và đúng như tinh thần của giải đấu, Vòng Bán Kết sẽ chứng kiến những công nghệ nghiên cứu tối tân nhất thế kỷ 21 được chiếu trực tiếp lên sàn đấu! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ ngồi chỉnh kính trên bục giám khảo, trước mặt là ba chiếc huy chương Bán Kết sáng lấp lánh dưới ánh đèn pha. |
| b03 | 00:17.2–00:28.2 (10.9s) | L307 | Đấu sĩ mở màn Bán Kết là chú bọ tí hon từng bị đánh giá thấp nhất lúc khai mạc: Bọ Pháo Thủ! Lần này chúng ta không nhìn từ bên ngoài mà nhìn xuyên thấu vào bên trong bụng chú bọ khi nó đang nhả đạn! |  | chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C tiến vào buồng chụp tia X đồng bộ khổng lồ, ánh sáng X-ray chuẩn bị quét qua phần bụng của chú bọ; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:28.2–00:40.2 (12.0s) | L308 | Năm 2015, một nhóm khoa học gia tại Viện Công Nghệ Massachusetts MIT và Đại học Arizona đã thực hiện một kỳ tích chưa từng có: đưa Bọ Pháo Thủ vào máy gia tốc hạt synchrotron quay phim tia X tốc độ 2.000 fps mỗi giây! |  | Màn hình tia X trực tiếp hiển thị khung xương và các buồng nội tạng bên trong bụng chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C với độ sắc nét từng mi-crô-mét; KHÔNG có anh MC trong cảnh này. |
| b05 | 00:40.2–00:45.9 (5.7s) | L309 | Đoạn phim tia X đã vén bức màn bí mật về cơ chế van tự động thiên tài bên trong cơ thể dài chưa đầy 2cm này! |  | Hình ảnh quay chậm tia X: khi hai hóa chất trộn vào buồng phản ứng, áp suất nổ bùng lên đẩy van đầu vào tự động đóng sập lại ngay lập tức! :: Mũi tên áp suất nổ bên trong buồng phản ứng ép chặt cánh van ngăn không cho hỗn hợp sôi trào ngược vào túi dự trữ an toàn; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:45.9–00:53.2 (7.3s) | L310 | Ngay khi tia hơi nóng được tống ra ngoài qua nòng pháo, áp suất trong buồng phản ứng tụt xuống, cánh van lại tự động bật mở cho một giọt nhiên liệu mới chảy xuống! |  | Van mở ra nhỏ giọt rồi đóng sập, nổ bùm, mở ra, đóng sập lặp đi lặp lại với tốc độ năm trăm đến một ngàn lần trong một giây! [surprise-oh] :: Toàn bộ chu trình đóng mở van cơ học tự động hoàn toàn nhờ áp suất nổ lặp đi lặp lại nhịp nhàng như động cơ xung phản lực của tên lửa V1! KHÔNG có anh MC trong cảnh này. |
| b07 | 00:53.2–01:01.7 (8.6s) | L311 | Đây chính là cơ chế tự điều áp bằng chính vụ nổ của mình mà không cần tiêu tốn năng lượng não bộ để điều khiển từng phát bắn! Một cỗ máy cơ khí sinh học hoàn mỹ tuyệt đối! |  | Cả khán đài và đội ngũ kỹ sư cơ khí đứng bật dậy vỗ tay tán thưởng cho chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C đang giơ càng chào khiêm tốn; KHÔNG có anh MC trong cảnh này. |
| b08 | 01:01.7–01:10.7 (9.0s) | L312 | Tuyển thủ thứ hai bước lên sàn Bán Kết khiến cả hội trường phải lặng người vì ngạc nhiên: Thánh sống chậm Con Lười! Kẻ đang đứng cuối bảng tổng sắp với chỉ 1 điểm duy nhất! |  | chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini từ từ trườn ra giữa sân khấu, trên bộ lông rêu xanh của chú là hàng chục ống nghiệm phòng thí nghiệm đang tỏa ánh sáng lung linh; KHÔNG có anh MC trong cảnh này. |
| b09 | 01:10.7–01:22.1 (11.3s) | L313 | Nhiều người nghĩ Con Lười chẳng làm được gì ngoài việc treo ngược ngủ gật. Nhưng năm 2014, tiến sĩ Sarah Higginbotham tại Viện Nghiên cứu Nhiệt đới Smithsonian đã phát hiện một kho báu y học nằm ngay trên bộ lông thô ráp của nó! |  | Bức ảnh tiến sĩ hoạt hình thu thập cẩn thận vài sợi lông lưng của chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini tại Vườn quốc gia Soberanía nước Panama đưa vào ống nghiệm bảo quản; KHÔNG có anh MC trong cảnh này. |
| b10 | 01:22.1–01:32.9 (10.8s) | L314 | Từ mẫu lông của chỉ 9 chú Con Lười ba ngón hoang dã, các nhà khoa học đã phân lập nuôi cấy thành công tới 84 chủng nấm độc đáo thuộc ngành nấm túi, trong đó có những loài chưa từng được nhân loại biết tới! |  | Tám mươi bốn đĩa thạch nuôi cấy nấm phát sáng đa sắc màu xếp thành ma trận khổng lồ trên màn hình phòng thí nghiệm; KHÔNG có anh MC trong cảnh này. |
| b11 | 01:32.9–01:39.7 (6.8s) | L315 | Và khi đưa chiết xuất từ những chủng nấm lông lười này đi thử nghiệm sinh học, kết quả thu được làm rung chuyển cả ngành dược học thế giới! |  | Các giọt chiết xuất nấm lông lười nhỏ xuống các đĩa chứa mầm bệnh nguy hiểm nhất của loài người trong kính hiển vi; KHÔNG có anh MC trong cảnh này. |
| b12 | 01:39.7–01:46.4 (6.7s) | L316 | 74 chủng nấm được chiết xuất thử nghiệm: 20,6% số mẫu đã tiêu diệt và ức chế cực mạnh tế bào ung thư vú MCF-7 ở | **20,6% MẪU** · Diệt tế bào ung thư · R/380 · [0.65, 0.45] | Hình ảnh các tế bào ung thư vú MCF-7 bị các phân tử hoạt chất nấm từ lông chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini tấn công tan rã nhanh chóng; KHÔNG có anh MC trong cảnh này. |
| b13 | 01:46.4–01:59.0 (12.6s) | L317 | người! Chưa hết, nhiều chủng nấm khác trên lông Con Lười còn tỏ ra cực kỳ hiệu quả trong việc tiêu diệt ký sinh trùng gây bệnh sốt rét ác tính Plasmodium falciparum, bệnh Chagas nhiệt đới và 20 chủng nấm có khả năng kháng vi khuẩn gây bệnh kháng thuốc! |  | Bốn loại vi khuẩn và ký sinh trùng nguy hiểm đều bị quét sạch bởi các hoạt chất trích xuất từ vườn nấm di động trên lưng chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini; KHÔNG có anh MC trong cảnh này. |
| b14 | 01:59.0–02:05.2 (6.2s) | L318 | Một hiệu thuốc di động sống treo lơ lửng trên ngọn cây rừng nhiệt đới! Ai dám bảo Thánh sống chậm là vô dụng nào? |  | chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini đeo chiếc áo blouse bác sĩ mini mỉm cười hiền hậu, khán giả trên khán đài đồng loạt cúi đầu nể phục; KHÔNG có anh MC trong cảnh này. |
| b15 | 02:05.2–02:16.0 (10.8s) | L319 | Tuyển thủ thứ ba mang đến bài thi cuối cùng của Bán Kết: Cá Cung Thủ! Bên cạnh trí tuệ nhớ 44 khuôn mặt người, nghiên cứu của Wöhl và Schuster còn giải mã tốc độ phản xạ thần tốc của loài cá này! |  | chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn bơi sát mặt nước bể thử nghiệm với hàng chục cảm biến điện sinh học đo tốc độ phản xạ não bộ đang hoạt động liên tục; KHÔNG có anh MC trong cảnh này. |
| b16 | 02:16.0–02:25.3 (9.3s) | L320 | Ngay khi con mồi trên cành vừa bị bắn rơi và chạm mặt nước hoặc rơi tự do trong không trung, bộ não cá chỉ mất vỏn vẹn 40ms để tính toán lại toàn bộ góc quay cơ thể! |  | Bộ não chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn phát tia xung thần kinh trong 40 mili-giây, điều khiển vây đuôi quay phắt thân cá hướng thẳng về điểm mồi sắp rơi; KHÔNG có anh MC trong cảnh này. |
| b17 | 02:25.3–02:35.9 (10.6s) | L321 | Hơn nữa, mắt của Cá Cung Thủ tiến hóa hai vùng võng mạc chuyên biệt: vùng dưới nhìn sắc nét dưới nước tối và vùng trên chuyên nhìn xuyên qua mặt nước để phóng đại hình ảnh côn trùng giữa không trung! |  | Sơ đồ giải phẫu mắt kép sinh học của chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn: hai luồng ánh sáng trên không và dưới nước hội tụ chính xác trên hai vùng võng mạc riêng biệt; KHÔNG có anh MC trong cảnh này. |
| b18 | 02:35.9–02:42.8 (6.9s) | L322 | Không chỉ dừng lại ở đó, ban giám khảo còn kiểm tra khả năng chịu đựng và duy trì nòi giống trong điều kiện khắc nghiệt của Hà Mã và Thằn Lằn Quỷ Gai! |  | Sân đấu Bán Kết bật đèn chiếu sáng hai khu vực mô phỏng lòng sông thiếu oxy và tầng cát sâu nóng bức; KHÔNG có anh MC trong cảnh này. |
| b19 | 02:42.8–02:53.9 (11.0s) | L323 | Trong cơ bắp đồ sộ của Hà Mã chứa mật độ myoglobin dự trữ oxy cực cao tương tự các loài cá voi đại dương! Nhờ kho oxy dự trữ trong từng thớ thịt đó, nó dễ dàng chạy bộ phi nước đại dưới đáy sông suốt 5 phút mà không hề mỏi |  | Phóng đại thớ cơ đỏ thẫm của chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ chứa đầy các phân tử myoglobin tích trữ oxy giúp vận động bền bỉ dưới đáy nước sâu; KHÔNG có anh MC trong cảnh này. |
| b20 | 02:53.9–03:03.1 (9.2s) | L324 | cơ! Còn Thằn Lằn Quỷ Gai mái đến mùa sinh sản lại tự mình đào một đường hầm sâu tới 30cm dưới cát cứng sa mạc, đẻ từ ba đến mười quả trứng rồi lấp kín xóa sạch mọi dấu vết! |  | Sơ đồ hang ngầm dưới cát đỏ sa mạc Úc: chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm mẹ cẩn thận dùng chân sau gạt cát phẳng lì che giấu ổ trứng ở độ sâu 30cm; KHÔNG có anh MC trong cảnh này. |
| b21 | 03:03.1–03:10.6 (7.5s) | L325 | Khoảng 3-4 tháng sau, những chú quỷ gai con nở ra từ dưới lòng đất, tự mình đội cát chui lên với bộ giáp gai mini sắc nhọn sẵn sàng chiến đấu ngay từ ngày đầu tiên! |  | Những chú chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm con tí hon đội cát ngoi lên mặt đất giữa ánh nắng sa mạc, đôi mắt tinh anh đầy bản lĩnh sinh tồn; KHÔNG có anh MC trong cảnh này. |
| b22 | 03:10.6–03:21.3 (10.8s) | L326 | Còn Bố Già Capybara thì sao? Để bảo toàn mạng sống trong mùa khô khắc nghiệt khi đầm lầy cạn kiệt, hàng trăm cá thể tụ họp thành đại liên minh rộng lớn cùng canh gác cho nhau trước móng vuốt báo đốm Jaguar! |  | Bức tranh cả một đàn lớn hơn năm mươi chú chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia quây quần bên vũng nước còn sót lại giữa mùa khô, thay phiên nhau đứng gác bảo vệ bầy con; KHÔNG có anh MC trong cảnh này. |
| b23 | 03:21.3–03:29.3 (8.0s) | L327 | Kết quả Vòng Bán Kết lịch sử đã có! Huy chương đồng thuộc về Cá Cung Thủ với phản xạ 40ms và cấu trúc mắt kép nhìn xuyên |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ trao huy chương đồng cho chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn đang giơ vây vẫy chào khán giả; tiếng vỗ tay vang dội. |
| b24 | 03:29.3–03:39.5 (10.1s) | L328 | mặt nước! Huy chương bạc thuộc về Con Lười với vườn nấm 84 chủng diệt sốt rét và tế bào ung thư! Và Huy chương vàng thuộc về Bọ Pháo Thủ với phát hiện tia X đồng bộ van nổ tự điều áp! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ trao huy chương bạc cho chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini và huy chương vàng cho chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C; pháo hoa nổ rực trời đấu trường |
| b25 | 03:39.5–03:49.9 (10.4s) | L329 | Hãy nhìn lên Bảng Tổng Sắp ngay trước giờ bước vào Vòng Chung Kết! Cuộc đua kịch tính chưa từng thấy trong lịch sử: Bốn tuyển thủ đồng hạng nhất với 6 điểm là Tôm Súng, Lươn Điện, Thằn Lằn Quỷ Gai và Bọ Pháo Thủ! |  | tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) rực sáng bốn cột điểm cao bằng nhau ở mốc sáu điểm tạo thành thế trận tứ mã tranh ngôi vương nghẹt thở! |
| b26 | 03:49.9–03:56.7 (6.8s) | L330 | Gấu Trúc Lớn và Hà Mã bám ngay phía sau với 5 điểm! Chim Tu Hú và Cá Cung Thủ 4 điểm! Capybara và Con Lười 3 điểm! |  | Cả mười cột điểm đều sát nút nhau đến mức bất kỳ ai giành vàng Chung Kết nhân đôi sáu điểm đều có cơ hội bước lên đỉnh vinh quang! |
| b27 | 03:56.7–04:03.2 (6.4s) | L331 | Thời khắc quyết định vận mệnh Mùa 2 đã điểm! Xin mời toàn thể khán đài tiến vào Vòng Chung Kết: Món Quà Cho Nhân Loại! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vung micro vàng hô vang, ánh đèn sân khấu hội tụ toàn bộ vào bục vinh quang nơi chiếc vương miện đang chờ chủ nhân. |

### scene12 · MÓN QUÀ CHO NHÂN LOẠI — CÔNG NGHỆ ĐỘT PHÁ TƯƠNG LAI · 263.2s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.6 (9.6s) | L332 | Giờ phút thiêng liêng nhất của Đại Hội Sinh Tồn Mùa 2 đã đến: Vòng Chung Kết Tối Thượng! Như đã công bố từ đầu giải, mọi huy chương tại vòng chung kết này sẽ được nhân đôi điểm số! |  | Cả sân vận động bùng nổ trong ánh sáng vàng kim lộng lẫy, biểu tượng 'ĐIỂM NHÂN ĐÔI' xoay tròn phát sáng rực rỡ trên màn hình lớn; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vest đỏ giơ hai tay đón chào khoảnh khắc lịch sử. |
| b02 | 00:09.6–00:21.2 (11.5s) | L333 | Huy chương vàng trị giá 6 điểm! Huy chương bạc 4 điểm! Và huy chương đồng 2 điểm! Với bốn ứng cử viên đang hòa nhau ở mốc 6 điểm và sáu ứng cử viên bám sát ngay phía sau, bất kỳ điều điên rồ nào cũng có thể xảy ra! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ nâng chiếc vương miện nạm ngọc vàng lấp lánh trên tay, đặt trang trọng bên cạnh chiếc cúp vô địch sáng chói giữa sân đấu. |
| b03 | 00:21.2–00:30.6 (9.5s) | L334 | Chủ đề thi đấu cao quý nhất của đêm chung kết là: Món Quà Cho Nhân Loại! Khoa học và kỹ thuật loài người đã học hỏi được những công nghệ thay đổi thế giới nào từ mười quái kiệt này? |  | Màn hình lớn trình chiếu các hình ảnh tương lai: phi thuyền vũ trụ, trạm thu nước sa mạc, thiết bị cấy ghép tim nhân tạo và phòng bào chế thuốc cứu người; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:30.6–00:43.2 (12.6s) | L335 | Ứng cử viên mở màn Chung Kết là Tôm Súng! Ngoài khả năng tạo plasma dưới nước hiệu suất cao gấp 10 lần máy laser tại Đại học Texas A&M, sóng xung kích cavitation của nó còn đang được nghiên cứu ứng dụng trong xử lý nước thải và khoan đá ngầm không gây ô nhiễm! |  | Mô hình chiếc càng chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa in 3D tạo ra chùm tia plasma khử trùng sạch bóng hàng triệu vi khuẩn trong bể nước ô nhiễm chỉ trong tích tắc; KHÔNG có anh MC trong cảnh này. |
| b05 | 00:43.2–00:52.9 (9.6s) | L336 | Bằng cách hội tụ năng lượng cơ học vào 1 điểm sụp đổ bong bóng khí siêu nhỏ, các kỹ sư có thể tạo ra phản ứng hóa học nhiệt độ cao để phân hủy chất độc công nghiệp dưới nước mà không cần hóa chất tẩy rửa độc hại! |  | Dòng nước thải đục ngầu đi qua buồng phóng cavitation mô phỏng chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa biến ngay thành dòng nước tinh khiết trong vắt; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:52.9–01:06.4 (13.6s) | L337 | Ứng cử viên thứ hai bước lên bục trình diễn công nghệ là Thằn Lằn Quỷ Gai! Dựa trên thí nghiệm cân đo rãnh da năm 2016 và nghiên cứu tổng hợp năm 2017 của tiến sĩ Philipp Comanns, các kỹ sư vật liệu đã phát minh ra tấm màng thu ẩm sa mạc thụ động! |  | Tấm vật liệu mô phỏng mạng lưới rãnh mao dẫn bất đối xứng trên da chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm được căng rộng trên các cồn cát sa mạc khô hạn; KHÔNG có anh MC trong cảnh này. |
| b07 | 01:06.4–01:19.4 (13.0s) | L338 | Lấy cảm hứng từ cấu trúc rãnh hình nêm dẫn nước một chiều chống bay hơi của chú thằn lằn sa mạc Úc, những tấm màng kim loại khắc laser vi mô này có khả năng hút ẩm từ sương đêm và đất ẩm dẫn về bể chứa mà không tốn một Oát điện năng nào! |  | Những giọt hơi ẩm nhỏ li ti tự động gom tụ chảy thành dòng nước tinh khiết vào bình chứa giúp người dân vùng khô hạn giải khát; KHÔNG có anh MC trong cảnh này. |
| b08 | 01:19.4–01:28.1 (8.7s) | L339 | Ứng cử viên thứ ba: Lươn Điện! Một phát minh công nghệ y sinh từng lên trang bìa tạp chí Nature cuối năm 2017 của giáo sư Michael Mayer và tiến sĩ Thomas Schroeder! |  | Trang tạp chí Nature giới thiệu mô hình 'Cơ quan phát điện mềm nhân tạo' lấy cảm hứng từ tế bào electrocyte của chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh; KHÔNG có anh MC trong cảnh này. |
| b09 | 01:28.1–01:37.3 (9.2s) | L340 | Thay vì dùng pin kim loại cứng chứa hóa chất độc hại có nguy cơ rò rỉ trong cơ thể bệnh nhân, nhóm nghiên cứu đã xếp hàng ngàn giọt gel nước hydrogel chứa muối ion xen kẽ qua màng chọn lọc! |  | Sơ đồ tấm màng hydrogel mềm dẻo trong suốt xếp lớp theo kiểu gấp giấy origami của Nhật Bản, phát ra dòng điện sinh học ổn định 110V khi ấn nhẹ; KHÔNG có anh MC trong cảnh này. |
| b10 | 01:37.3–01:49.2 (11.9s) | L341 | Khi tiếp xúc đồng thời, hàng ngàn ngăn gel mềm tạo ra hiệu điện thế lên tới 110V hoàn toàn tương thích sinh học với cơ thể người! Mở ra kỷ nguyên cung cấp năng lượng vĩnh cửu cho máy tạo nhịp tim, kính áp tròng thông minh và robot mềm y tế! | **PIN 110V** · Hydrogel sinh học · L/380 · [0.42, 0.46] | Chiếc máy tạo nhịp tim gắn màng pin mềm hydrogel đập nhịp nhàng trong lồng ngực bệnh nhân mà không bao giờ cần mổ thay pin nữa; KHÔNG có anh MC trong cảnh này. |
| b11 | 01:49.2–01:58.4 (9.2s) | L342 | Ứng cử viên thứ tư khiến cả khán đài xúc động nghẹn ngào: Thánh sống chậm Con Lười! Kẻ bị chế giễu suốt từ đầu giải đấu lại đang nắm giữ chìa khóa cứu sống hàng triệu bệnh nhân! |  | chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini bước ra giữa ánh sáng ấm áp, bên cạnh là hình ảnh phòng thí nghiệm dược phẩm quốc tế đang nghiên cứu các chủng nấm quý từ lông lười; KHÔNG có anh MC trong cảnh này. |
| b12 | 01:58.4–02:09.7 (11.3s) | L343 | Hơn 20% số chủng nấm phân lập từ bộ lông rêu xanh của Con Lười có khả năng tiêu diệt tế bào ung thư vú MCF-7, bên cạnh những hoạt chất cực mạnh chống lại ký sinh trùng sốt rét và vi khuẩn kháng kháng sinh đang đe dọa nhân loại! |  | Những viên thuốc kháng sinh và thuốc đặc trị ung thư thế hệ mới tỏa sáng từ chiết xuất vườn nấm sinh thái trên bộ lông của chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini; KHÔNG có anh MC trong cảnh này. |
| b13 | 02:09.7–02:15.5 (5.8s) | L344 | Một loài vật đi chậm nhất hành tinh nhưng lại đi trước ngành dược học hiện đại cả một bước tiến dài! |  | Cả hội trường đứng dậy vỗ tay vang dội dành tặng sự trân trọng lớn lao cho chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini, chú lười mỉm cười rưng rưng xúc động; KHÔNG có anh MC trong cảnh này. |
| b14 | 02:15.5–02:25.8 (10.3s) | L345 | Và ứng cử viên cuối cùng bước lên sân khấu Chung Kết là pháo thủ tí hon nửa gam: Bọ Pháo Thủ! Công trình khoa học của giáo sư Andy McIntosh tại Đại học Leeds nước Anh đã làm thay đổi ngành công nghệ phun đốt toàn cầu! |  | Giáo sư kỹ thuật hoạt hình đặt mô hình buồng đốt của chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C lên bục trình diễn, bên cạnh là chiếc bằng sáng chế Mỹ cấp năm 2015 cho công nghệ phun sương vi mô; KHÔNG có anh MC trong cảnh này. |
| b15 | 02:25.8–02:35.8 (10.0s) | L346 | Công nghệ phun sương chớp nhoáng mang thương hiệu µMist mô phỏng chính xác van cơ học buồng phản ứng của Bọ Pháo Thủ: không cần máy bơm áp suất cao cồng kềnh hay khí nén độc hại, chỉ dùng nhiệt năng nhỏ tạo vụ nổ hơi giãn |  | Mô hình động cơ phản lực và ống hít y tế sử dụng đầu phun vi mô từ công nghệ Bọ Pháo Thủ phun ra màn sương hạt siêu mịn đồng đều tuyệt đối; KHÔNG có anh MC trong cảnh này. |
| b16 | 02:35.8–02:45.6 (9.8s) | L347 | nở! Công nghệ này giúp tăng hiệu suất đốt cháy nhiên liệu của động cơ tên lửa và tua-bin khí, tạo ra các ống hít thuốc hen suyễn chính xác tới từng mi-crô-mét, và đặc biệt là chế tạo ra súng chữa cháy rừng thế hệ mới! |  | Một lính cứu hỏa đeo ba lô chữa cháy mini dài chỉ 5cm nhưng phun tia sương nước áp suất cao bắn xa tới 10 mét dập tắt đám cháy rừng rực lửa ngay tức khắc! KHÔNG có anh MC trong cảnh này. |
| b17 | 02:45.6–02:56.5 (10.9s) | L348 | Chỉ từ một buồng nén nhỏ dài 5cm, thiết bị mô phỏng Bọ Pháo Thủ bắn luồng sương dập lửa xa tới 10m với lượng nước tiết kiệm gấp nhiều lần! Một phát minh cứu rừng và cứu người vô cùng vĩ đại! | **BẮN XA 10M** · Cứu hỏa buồng 5cm · R/380 · [0.7, 0.44] | Ngọn lửa cháy rừng bị dập tắt sạch sẽ trong chớp mắt, hàng ngàn loài thú rừng an toàn reo hò ăn mừng; KHÔNG có anh MC trong cảnh này. |
| b18 | 02:56.5–03:01.8 (5.4s) | L349 | Và trước khi trao giải, ban giám khảo còn tôn vinh hai món quà y học đầy bất ngờ từ hai chú gấu và hà mã! |  | Màn hình lớn hiển thị hai phòng thí nghiệm dược phẩm đang phân tích ADN của chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu và dịch tiết da của chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ; KHÔNG có anh MC trong cảnh này. |
| b19 | 03:01.8–03:10.5 (8.6s) | L350 | Thứ nhất, năm 2012 các nhà khoa học đã giải mã bộ gen của Gấu Trúc Lớn và phát hiện ra một chuỗi peptit kháng khuẩn cực mạnh mang tên cathelicidin-AM! |  | Sơ đồ phân tử peptit cathelicidin-AM xoắn ốc phát sáng xanh lam được trích xuất từ mẫu máu bảo tồn của chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu; KHÔNG có anh MC trong cảnh này. |
| b20 | 03:10.5–03:22.1 (11.7s) | L351 | Trong thử nghiệm diệt vi khuẩn Staphylococcus kháng thuốc, hợp chất từ Gấu Trúc tiêu diệt sạch vi khuẩn chỉ trong chưa đầy 1 giờ, nhanh gấp 6 lần so với thuốc kháng sinh clindamycin thông thường mất tới 6 |  | Đồng hồ đếm ngược so sánh: bên trái thuốc từ chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu quét sạch vi khuẩn dưới 1 giờ, bên phải thuốc kháng sinh thường mất tới 6 giờ; KHÔNG có anh MC trong cảnh này. |
| b21 | 03:22.1–03:33.2 (11.1s) | L352 | giờ! Còn sắc tố axit hipposudoric từ mồ hôi đỏ của Hà Mã chặn đứng toàn bộ dải tia cực tím từ 200-600nm mà lại không hòa tan trôi tuột trong nước và thân thiện với rạn san hô |  | Một lọ kem chống nắng sinh học mang biểu tượng chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ che chắn tia nắng UV rực rỡ mà vẫn giữ cho rạn san hô bên dưới xanh tươi an toàn; KHÔNG có anh MC trong cảnh này. |
| b22 | 03:33.2–03:37.1 (3.9s) | L410 | — mở đường chế tạo kem chống nắng sinh học thế hệ mới bảo vệ đại dương! |  | Một chú cá hề và rạn san hô cầu vồng bơi lội vui vẻ bên cạnh biểu tượng khiên chống nắng sinh học màu đỏ của chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ; KHÔNG có anh MC trong cảnh này. |
| b23 | 03:37.1–03:46.8 (9.7s) | L353 | Thời khắc công bố kết quả Chung Kết điểm nhân đôi đã điểm! Sau khi cân nhắc giá trị khoa học, tính ứng dụng thực tiễn và sức lan tỏa nhân văn, hội đồng giám khảo xin tuyên bố: |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gõ mạnh chiếc búa gỗ xuống bàn, cả đấu trường nín thở im phăng phắc chờ nghe phán quyết cuối cùng. |
| b24 | 03:46.8–03:53.4 (6.7s) | L354 | Huy chương đồng Chung Kết và 2 điểm thuộc về Lươn Điện với phát minh pin sinh học mềm hydrogel nuôi máy tạo nhịp tim tương lai! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ đeo tấm huy chương đồng danh giá lên cổ chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh, các tia điện xanh chúc mừng lấp lánh. |
| b25 | 03:53.4–04:02.3 (8.9s) | L355 | Huy chương bạc Chung Kết và 4 điểm thuộc về... Con Lười! Với vườn nấm kỳ diệu trên bộ lông giúp con người chống lại bệnh sốt rét và tế bào ung thư! |  | Cả khán đài vỡ òa reo hò khi chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini nhận tấm huy chương bạc quý giá, vươn mình từ cuối bảng xếp hạng lên nhóm dẫn đầu! |
| b26 | 04:02.3–04:12.8 (10.5s) | L356 | Và Huy chương vàng Chung Kết cùng 6 điểm quyết định của Đại Hội Sinh Tồn Mùa 2 chính thức thuộc về... Bọ Pháo Thủ! Với công nghệ phun sương vi mô cứu hỏa và động cơ tên lửa vũ trụ! |  | Pháo hoa vàng rực nổ rền trời, bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ trao tấm huy chương vàng chung kết cho chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C, anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng nhảy cẫng lên ăn mừng lịch sử! |
| b27 | 04:12.8–04:23.2 (10.4s) | L357 | Từ vị trí bị đánh giá chỉ vào thi cho đủ đội hình, chú bọ dài 2cm đã làm nên cú lội ngược dòng vĩ đại nhất mọi thời đại! Mời toàn thể quý vị cùng hướng mắt lên Bảng Tổng Sắp Chung Cuộc ngay sau đây! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng chỉ tay lên tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) đang bùng cháy ánh sáng rực rỡ chuẩn bị lễ đăng quang chính thức. |

### scene13 · LỄ TRAO HUY CHƯƠNG VÀ BẢNG TỔNG SẮP ĐIỂM SỐ MÙA 2 · 213.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:10.2 (10.2s) | L358 | Khoảnh khắc lịch sử của Đại Hội Sinh Tồn Mùa 2 đã chính thức khép lại mọi dự đoán! Xin mời toàn thể mười tuyển thủ và hàng vạn khán giả cùng hướng mắt lên Bảng Tổng Sắp Cuối Cùng! |  | tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) hình chiếc khiên khổng lồ giữa sân vận động bừng sáng rực rỡ với mười cột đèn màu sắc từ cao xuống thấp, pháo hoa và dải băng kim tuyến rơi ngập tràn không gian; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vest đỏ đứng cạnh micro vàng. |
| b02 | 00:10.2–00:18.2 (8.0s) | L359 | Trải qua tám vòng đấu khốc liệt với 100% dữ liệu khoa học mới hoàn toàn, bảng vàng danh dự Mùa 2 đã ghi tên những nhà chinh phục xứng đáng nhất! |  | Mười tuyển thủ đứng dàn hàng ngang dưới ánh đèn sân khấu lung linh, trên ngực mỗi bạn lấp lánh những tấm huy chương danh giá; KHÔNG có anh MC trong cảnh này. |
| b03 | 00:18.2–00:26.1 (7.9s) | L360 | Và Tân Vương của Đại Hội Sinh Tồn Mùa 2 chính thức gọi tên: Bọ Pháo Thủ với tổng điểm 12 điểm! Hai huy chương vàng, một huy chương bạc và một huy chương đồng! |  | chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C bước lên bục số một cao nhất, chiếc cúp vô địch vàng ròng và vương miện nạm ngọc được đặt lên đầu chú bọ tí hon, pháo hoa rực sáng góc trời; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:26.1–00:38.7 (12.6s) | L361 | Nặng chưa đầy nửa gam và từng bị các chuyên gia gạch tên ngay từ vòng cân ký! Nhưng với buồng phản ứng tia X đồng bộ, cơ chế van nổ tự điều áp không cần khí đẩy và bằng sáng chế công nghệ cứu hỏa bắn xa 10m, Bọ Pháo Thủ đã chinh phục trọn vẹn cả thế giới! |  | Cận cảnh chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C giơ cao chiếc cúp vô địch vàng, nòng pháo sau đuôi bắn lên trời một chùm khói pháo hoa ăn mừng rực rỡ; KHÔNG có anh MC trong cảnh này. |
| b05 | 00:38.7–00:43.5 (4.8s) | L362 | Ngôi vị Á Quân thuộc về: Lươn Điện với 8 điểm! Ba huy chương bạc và hai huy chương |  | chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh uốn lượn vươn mình lên bục số hai, đeo bộ huy chương lấp lánh quanh cổ cùng vầng hào quang tia sét xanh neon tuyệt đẹp; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:43.5–00:54.1 (10.6s) | L363 | đồng! Đập tan định kiến sống cô độc bằng màn săn mồi bầy đàn hơn 100 con tại sông Iriri, cùng phát minh pin mềm hydrogel 110V nuôi sống trái tim nhân loại! Xứng danh chiến thần đầm lầy Nam |  | chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh nháy mắt cười tự tin, các nhà khoa học trên khán đài đứng dậy vỗ tay chúc mừng á quân; KHÔNG có anh MC trong cảnh này. |
| b07 | 00:54.1–01:02.2 (8.1s) | L364 | Mỹ! Và cú lội ngược dòng ngoạn mục nhất đêm nay gọi tên: Con Lười ở vị trí Hạng Ba chung cuộc với 7 điểm! Hai huy chương bạc và một huy chương đồng! |  | chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini bước lên bục số ba với nụ cười hiền lành rạng rỡ, cổ đeo hai tấm huy chương bạc sáng chói giữa tiếng hò reo vang dội của khán đài; KHÔNG có anh MC trong cảnh này. |
| b08 | 01:02.2–01:15.0 (12.8s) | L365 | Từ một thí sinh bị trêu chọc vì mất 10 phút mới trả lời xong một câu hỏi, Con Lười đã chứng minh sức mạnh phi thường với hệ thống dây chằng treo nội tạng, cụ tổ khổng lồ 4 tấn và 84 chủng nấm chống ung thư sốt rét trên bộ lông! |  | Bức ảnh chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini treo ngược tay cầm ống nghiệm thuốc cứu người, ánh mắt tự hào rạng rỡ; KHÔNG có anh MC trong cảnh này. |
| b09 | 01:15.0–01:28.1 (13.1s) | L366 | Xếp ngay sát nút phía sau là hai chiến binh 6 điểm: Tôm Súng với hai huy chương vàng nhờ công nghệ tạo plasma gấp 10 lần laser và đế chế xã hội 300 tôm lính; cùng Thằn Lằn Quỷ Gai với một vàng, một bạc, một đồng nhờ kỹ thuật hắt cát ẩm và màng thu nước sa mạc! |  | chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa và chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm đứng cạnh nhau giơ càng và chỉnh mũ safari chào khán đài đầy kiêu hãnh, mỗi bạn đeo đầy huy chương sáng loáng; KHÔNG có anh MC trong cảnh này. |
| b10 | 01:28.1–01:38.8 (10.7s) | L367 | Nhóm 5 điểm gọi tên hai gã khổng lồ đáng mến: Hà Mã với danh hiệu cỗ máy bơm 400kg Silicon mỗi ngày và thính giác xương hàm dưới; cùng Gấu Trúc Lớn với đột biến gen DUOX2, áo ngụy trang và liệu pháp phân ngựa |  | chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ và chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu đứng khoác vai nhau cười tươi rạng rỡ, một tay cầm bình Silicon và một tay cầm mầm trúc xanh tươi; KHÔNG có anh MC trong cảnh này. |
| b11 | 01:38.8–01:50.2 (11.3s) | L368 | chống rét! Nhóm 4 điểm vinh danh hai bậc thầy bầu trời và mặt nước: Chim Tu Hú với đường bay vệ tinh 16.000km và màn cải trang chim ưng; cùng Cá Cung Thủ với bộ não nhận diện 44 khuôn mặt người chính xác 86%! |  | chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái đậu trên thành bể kính của chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn, cả hai cùng giơ tấm huy chương vàng vòng đấu của mình khoe với khán giả; KHÔNG có anh MC trong cảnh này. |
| b12 | 01:50.2–01:59.1 (8.9s) | L369 | Và cuối cùng, Bố Già Capybara đạt 3 điểm danh dự với một huy chương bạc và một huy chương đồng nhờ cặp răng cửa tự mài sắc và văn hóa nuôi con chung cực kỳ nhân văn! |  | chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia đội mũ phớt mỉm cười điềm đạm nhấp ngụm trà thảo mộc, nhận tràng pháo tay nồng nhiệt từ toàn thể các loài thú rừng; KHÔNG có anh MC trong cảnh này. |
| b13 | 01:59.1–02:07.1 (8.1s) | L370 | Khoan đã! Trước khi bước vào lễ bế mạc, anh MC xin phép điểm lại hành trình đáng kinh ngạc của cả mười đấu sĩ và phỏng vấn nhanh bộ ba quán quân đêm nay! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cầm micro tiến sát bục vinh quang 1-2-3 nơi chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C, chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh và chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu x |
| b14 | 02:07.1–02:16.0 (8.9s) | L371 | Từ những giây phút đầu tiên bị giới chuyên gia chê bai là tí hon và chậm chạp, Bọ Pháo Thủ và Con Lười đã chứng minh rằng giá trị thực sự của sự sống không nằm ở vẻ bề ngoài! |  | Màn hình lớn chiếu lại đoạn phim khoảnh khắc chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C đứng cạnh kính hiển vi ở Vòng cân ký và giờ phút đăng quang rực rỡ trên bục số một; KHÔNG có anh MC trong cảnh này. |
| b15 | 02:16.0–02:22.6 (6.6s) | L372 | Xin chúc mừng Tân Vương Bọ Pháo Thủ! Từ vị trí bị gạch tên ở vòng cân ký cho tới ngôi vương 12 điểm, cảm xúc của bạn lúc này thế nào? |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đưa chiếc micro sát nòng pháo nhỏ xíu của chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C trên bục số một; ánh đèn flash chớp sáng liên hồi. |
| b16 | 02:22.6–02:32.6 (10.0s) | L373 | Thưa anh MC và toàn thể khán đài, kích thước chưa đầy nửa gam chưa bao giờ là giới hạn! Chỉ cần bạn có áp suất nội tại vững vàng và không bao giờ bỏ cuộc dù có bị nuốt vào bụng cóc, bạn sẽ luôn bùng nổ tỏa sáng! |  | chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C giơ chiếc cúp vàng lên cao, bắn một chùm khói pháo hoa hình ngôi sao lên trần đấu trường ăn mừng đầy khí thế; KHÔNG có anh MC trong cảnh này. |
| b17 | 02:32.6–02:41.8 (9.3s) | L374 | Một phát biểu cực kỳ bùng nổ! Còn Á Quân Lươn Điện thì sao? Từ một sinh vật bị gán mác cô độc, bạn đã cho cả thế giới thấy sức mạnh đoàn kết của bầy đàn hơn 100 chiến binh! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng quay sang bể kính của chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh, chú lươn điện chớp những tia sét xanh màu cầu vồng cực kỳ đẹp mắt chào khán giả; KHÔNG có anh MC trong cảnh này. |
| b18 | 02:41.8–02:51.3 (9.5s) | L375 | Còn Hạng Ba Con Lười — chủ nhân của cú lội ngược dòng giàu cảm xúc nhất lịch sử Đại Hội Sinh Tồn! Hãy giơ cao hai tấm huy chương bạc và chiếc cúp hiệu thuốc rừng mưa của bạn lên đi nào! |  | chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini chậm rãi nhưng đầy tự hào giơ cao hai tấm huy chương bạc lấp lánh, phía sau là các bác sĩ và nhà dược học vỗ tay rần rần; KHÔNG có anh MC trong cảnh này. |
| b19 | 02:51.3–02:56.6 (5.2s) | L376 | Cảm ơn... tất cả... mọi người... Nhớ bảo vệ... rừng cây... cho tụi mình... treo ngược... ngủ ngon... nha! |  | Chú lười chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini mỉm cười hiền hậu mất mười giây để nói hết câu chúc, khiến cả khán đài vừa cười vừa rưng rưng xúc động; KHÔNG có anh MC trong cảnh này. |
| b20 | 02:56.6–03:03.0 (6.4s) | L377 | Và chúng ta cũng đừng quên bảy người anh hùng còn lại đã chiến đấu hết mình suốt tám vòng thi đấu nghẹt thở đêm nay! |  | Bảy tuyển thủ còn lại cùng bước lên bục đồng hạng vinh dự, giơ cao những kỷ niệm chương lấp lánh dưới ánh đèn sân khấu; KHÔNG có anh MC trong cảnh này. |
| b21 | 03:03.0–03:10.3 (7.3s) | L378 | Tôm Súng và Thằn Lằn Quỷ Gai đã chứng minh rằng dù nhỏ bé nhưng hỏa lực plasma và kỹ thuật thu hoạch ẩm sa mạc đủ sức khuất phục bất kỳ đối thủ to xác nào! |  | chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa bắn một phát pháo bọt khí ăn mừng trên không, chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm tung nắm cát đỏ lấp lánh vẫy chào khán giả; KHÔNG có anh MC trong cảnh này. |
| b22 | 03:10.3–03:17.4 (7.2s) | L379 | Hà Mã và Gấu Trúc Lớn đã lật đổ mọi định kiến sai lầm bấy lâu nay bằng nguồn khoáng chất Silicon nuôi sống dòng sông và bộ gen tiết kiệm năng lượng thiên tài! |  | chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ và chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu cùng bắt tay cười tươi, phía sau là bản đồ sinh thái châu Phi và rừng tre Tứ Xuyên rực sáng; KHÔNG có anh MC trong cảnh này. |
| b23 | 03:17.4–03:25.9 (8.5s) | L380 | Còn bộ ba Chim Tu Hú, Cá Cung Thủ và Bố Già Capybara thì mãi mãi là biểu tượng của trí tuệ định vị không gian, thị giác nhận diện khuôn mặt và tinh thần ngoại giao hòa bình bất diệt! |  | chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái, chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn và chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia nâ |
| b24 | 03:25.9–03:33.9 (7.9s) | L381 | Mười đấu sĩ, mười tuyệt tác tiến hóa độc bản! Không một ai ra về tay trắng, và từng con số đêm nay đều là một lời tri ân sâu sắc gửi tới trí tuệ vĩ đại của mẹ thiên nhiên! |  | Mười tuyển thủ đứng quây quần bên nhau trên bục vinh quang dưới mưa pháo giấy ngũ sắc, cùng giơ cao tay ăn mừng tình đoàn kết. |

### scene14 · BÀI HỌC MÙA 2, BẢO TỒN THIÊN NHIÊN VÀ HÉ LỘ DỊ NHÂN MÙA 3 · 239.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:10.6 (10.6s) | L382 | Bọ Pháo Thủ đứng trên đỉnh bục cao nhất, chiếc vương miện vàng bé xíu nằm vừa vặn trên chiếc đầu màu cam ánh kim. Một sinh vật nặng chưa tới nửa gam đã chiến thắng ngoạn mục giữa những cỗ xe tăng nặng tới 3 tấn! |  | chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C đứng trên bục số một giơ cao cúp vàng, vương miện lấp lánh; xung quanh là chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ, chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân p |
| b02 | 00:10.6–00:18.0 (7.4s) | L383 | Chúc mừng bạn Bọ Pháo Thủ nha! Đợi mình xuống khỏi cái cây chuối này rồi tụi mình cùng đi ăn tiệc tre với cá sấu Caiman nhé! |  | chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu lộn nhào từ trên bục xuống thảm cỏ, ôm cành trúc vẫy tay chào vui vẻ bên cạnh chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia đang ngồi thư giãn; KHÔNG có anh MC trong cản |
| b03 | 00:18.0–00:26.4 (8.4s) | L384 | Nhìn lại toàn bộ tám vòng thi đấu vừa qua, Mùa 2 đã dạy cho chúng ta một bài học tuyệt đẹp: trong tự nhiên không hề có sinh vật nào là 'lỗi tiến hóa' hay 'vô |  | Bức tranh ghép toàn cảnh mười đấu sĩ: từ chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini mang vườn nấm chữa bệnh, chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu tiết kiệm năng lượng bằng đột biến gen, đến chú Hà Mã hoạt hình khổng lồ béo tr |
| b04 | 00:26.4–00:39.4 (13.0s) | L385 | dụng'! Mỗi đặc điểm kỳ quặc mà thoạt nhìn ta tưởng là ngớ ngẩn — như việc Con Lười treo ngược, Gấu Trúc lăn phân ngựa hay Hà Mã thải phân xuống nước — thực chất đều là những mắt xích hoàn hảo giữ cho cỗ máy Trái Đất vận hành trơn tru qua hàng triệu năm! |  | Các bánh răng sinh thái xanh lá khổng lồ gắn hình 10 con vật quay đều nhịp nhàng tạo thành một hành tinh Trái Đất tươi xanh rực rỡ; KHÔNG có anh MC trong cảnh này. |
| b05 | 00:39.4–00:52.9 (13.5s) | L386 | Và giống như thư viện sống khổng lồ của thiên nhiên, mười loài vật đêm nay đã mở ra cho nhân loại những công nghệ thay đổi cả tương lai: từ pin mềm nuôi trái tim nhân tạo, màng thu nước không tốn điện, vòi phun cứu hỏa xuyên rừng đến thuốc chống ung thư và sốt rét! |  | Nhà khoa học hoạt hình cùng các đấu sĩ mở từng trang sách ánh sáng chứa bản vẽ pin mềm, vòi phun sương và phân tử thuốc y học mới; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:52.9–01:00.1 (7.2s) | L387 | Nhưng ngay ngoài cánh cửa đấu trường này, những trang sách quý giá đó đang đối mặt với nguy cơ bị xé rách mãi mãi bởi chính tác động của con người! |  | Bầu trời chuyển màu xám buồn lắng đọng, hình ảnh cánh rừng nhiệt đới bị thu hẹp và dòng sông ô nhiễm nổi lên phía sau sân khấu; KHÔNG có anh MC trong cảnh này. |
| b07 | 01:00.1–01:08.2 (8.0s) | L388 | Rừng mưa nhiệt đới Panama và Amazon bị tàn phá đe dọa ngôi nhà của Con Lười và Lươn Điện — khiến chúng ta có thể mất đi những chủng nấm kháng sinh chưa kịp khám phá! |  | Hình ảnh chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini ôm cành cây cô đơn giữa mảng rừng bị chặt phá, ống nghiệm nấm thuốc mờ dần như sắp biến mất; KHÔNG có anh MC trong cảnh này. |
| b08 | 01:08.2–01:16.3 (8.2s) | L389 | Khu bảo tồn rừng tre Tứ Xuyên cũng cần được gìn giữ từng mét vuông để Gấu Trúc Lớn có đủ nguồn thức ăn quanh năm và giữ lại peptit kháng khuẩn quý giá trong máu của chúng! |  | Cánh rừng trúc Tứ Xuyên xanh tươi đón ánh nắng bình minh, gia đình chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu vui đùa hạnh phúc giữa bụi tre non; KHÔNG có anh MC trong cảnh này. |
| b09 | 01:16.3–01:25.6 (9.2s) | L390 | Đầm lầy Pantanal Nam Mỹ đang đối mặt với những trận cháy rừng lịch sử và hạn hán kéo dài, đe dọa không gian sống bình yên của hàng ngàn Bố Già Capybara và muôn loài chung sống xung quanh! |  | Bức tranh đầm lầy Pantanal bốc cháy khói mù, chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia dẫn đàn con nhỏ chạy về vùng nước an toàn; KHÔNG có anh MC trong cảnh này. |
| b10 | 01:25.6–01:35.7 (10.1s) | L391 | Sự suy giảm quần thể Hà Mã làm đứt gãy nguồn cung 400kg Silicon mỗi ngày cho các dòng sông châu Phi; còn biến đổi khí hậu khắc nghiệt khiến hành trình di cư 16.000km của Chim Tu Hú ngày càng gian nan |  | Quần thể chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ thưa thớt bên dòng sông cạn khô nứt nẻ, chú chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái mệt mỏi bay giữa cơn bão sa mạc dữ dội; KHÔNG có anh MC trong cảnh này. |
| b11 | 01:35.7–01:44.5 (8.8s) | L392 | hơn! Tại những rạn san hô Caribe nơi Tôm Súng sinh sống, hiện tượng axit hóa đại dương và tẩy trắng san hô đang phá hủy những ngôi nhà bọt biển của cả đế chế 300 tôm lính! |  | Rạn san hô trắng xóa dưới đáy biển buồn bã, chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa ôm chặt chiếc bọt biển nhỏ bảo vệ tổ ấm của Tôm Chúa; KHÔNG có anh MC trong cảnh này. |
| b12 | 01:44.5–01:51.8 (7.3s) | L393 | Và tại vùng rừng ngập mặn Đông Nam Á, nạn chặt phá rừng ven biển đang thu hẹp môi trường săn mồi độc đáo của những xạ thủ Cá Cung Thủ thông minh! |  | Khu rừng ngập mặn bên bờ biển bị thu hẹp, chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn bơi ngơ ngác tìm kiếm những tán lá xanh phía trên mặt nước; KHÔNG có anh MC trong cảnh này. |
| b13 | 01:51.8–02:04.7 (12.9s) | L394 | Nhưng tin vui cũng đã đến khi nỗ lực bảo tồn toàn cầu phát huy tác dụng! Nhờ việc phục hồi hàng ngàn héc-ta hành lang rừng tre kết nối tại Trung Quốc, Liên minh Bảo tồn Thiên nhiên Quốc tế IUCN đã chính thức hạ cấp Gấu Trúc Lớn từ mức Nguy Cấp xuống mức Sắp Nguy Cấp! |  | Bức tranh khu rừng trúc xanh mướt nối liền các dãy núi cao, đàn gấu trúc mẹ con vui đùa tung tăng dưới ánh nắng ấm áp; KHÔNG có anh MC trong cảnh này. |
| b14 | 02:04.7–02:15.3 (10.6s) | L395 | Đó là minh chứng hùng hồn nhất cho thấy: khi con người chung tay hành động, thiên nhiên luôn có cơ hội hồi sinh mạnh mẽ! Bởi vì bảo vệ một loài vật bé nhỏ cũng chính là giữ lại cơ hội sống cho chính nhân loại mai sau! |  | Bàn tay trẻ thơ dịu dàng nâng niu quả địa cầu xanh biếc có mười người bạn hoang dã mỉm cười vẫy tay bình yên; KHÔNG có anh MC trong cảnh này. |
| b15 | 02:15.3–02:26.1 (10.9s) | L396 | Và bây giờ, lá phiếu quyền lực nhất nằm trong tay của chính bạn! Bạn có đồng ý với ngôi vương của Bọ Pháo Thủ không? Hay trong trái tim bạn, Lươn Điện, Con Lười, Tôm Súng hay Hà Mã mới là nhà vô địch thực |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng bước ra sát màn hình chĩa chiếc micro vàng về phía khán giả, phía sau là tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) hiển thị đủ mười gương mặt tuyển thủ chờ bình chọn. |
| b16 | 02:26.1–02:33.1 (7.0s) | L397 | thụ? Và trước khi khép lại cánh cửa đấu trường Mùa 2, anh MC có một thử thách nhỏ dành cho các nhà thông thái nhí và khán giả đang theo dõi |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng bước ra sát rìa sân khấu mỉm cười hóm hỉnh, bên cạnh hiện lên những biểu tượng câu đố khoa học thú vị; KHÔNG có anh MC trong cảnh này. |
| b17 | 02:33.1–02:43.3 (10.2s) | L398 | màn hình: Trong suốt hơn 1 tiếng vừa qua, chi tiết khoa học mới nào làm bạn bất ngờ nhất: Gấu Trúc tắm phân ngựa chống rét, Cá Cung Thủ nhớ mặt người hay Bọ Pháo Thủ tạo ra súng cứu hỏa? |  | Màn hình hiện ba khung ảnh kỷ niệm rực rỡ của chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu, chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn và chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đạ |
| b18 | 02:43.3–02:49.6 (6.3s) | L399 | Hãy bình luận tên nhà vô địch của bạn và chia sẻ xem bạn ấn tượng nhất với phát hiện khoa học mới nào dưới phần bình luận nhé! |  | Mười tuyển thủ đồng loạt vẫy tay tạm biệt khán giả giữa mưa hoa giấy rực rỡ sắc màu; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cúi chào nồng nhiệt. |
| b19 | 02:49.6–03:01.8 (12.2s) | L400 | Mười tập phim lẻ, một đêm đại hội lịch sử với hàng trăm sự thật khoa học kỳ thú! Hy vọng hành trình hơn 1 giờ cùng Vẽ Chuyện Hoang Dã đã mang đến cho bạn thật nhiều tiếng cười sảng khoái và tình yêu sâu sắc dành cho thế giới tự nhiên! |  | Bức tranh kỷ niệm mười tuyển thủ Mùa hai cùng ôm nhau mỉm cười rạng rỡ giữa khung cảnh rừng xanh sông biếc lấp lánh ánh mặt trời; KHÔNG có anh MC trong cảnh này. |
| b20 | 03:01.8–03:10.1 (8.2s) | L401 | Nếu bạn thích phong cách đại hội tranh tài mới toanh này, đừng ngần ngại chia sẻ video này cho bạn bè và người thân cùng chiêm ngưỡng những kiệt tác tuyệt vời của tạo hóa nhé! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng giơ cao chiếc micro vàng mỉm cười tri ân khán giả, phía sau là mười đấu sĩ vẫy tay thân thiện. |
| b21 | 03:10.1–03:16.5 (6.4s) | L402 | Và xin đừng vội tắt màn hình... bởi vì cánh cửa đường hầm bí mật của Đại Hội Sinh Tồn Mùa 3 vừa hé mở những hồ sơ rùng mình nhất! |  | Cánh cửa thép khổng lồ mang số ba màu đỏ rực từ từ mở hé, luồng ánh sáng tím ma mị và sương lạnh cuồn cuộn tràn ra sàn đấu; KHÔNG có anh MC trong cảnh này. |
| b22 | 03:16.5–03:26.3 (9.7s) | L403 | Một biệt đội dị nhân sở hữu những năng lực tự hủy và tái sinh điên rồ chưa từng thấy chuẩn bị đổ bộ! Một chú ếch tự co cơ bẻ gãy xương ngón chân đâm thủng da thịt làm móng vuốt chiến đấu! |  | Bóng đen bí ẩn đầu tiên lộ rõ bàn chân ếch với những chiếc móng vuốt xương trắng sắc nhọn đâm xuyên qua đầu ngón chân như siêu anh hùng Wolverine; KHÔNG có anh MC trong cảnh này. |
| b23 | 03:26.3–03:36.8 (10.5s) | L404 | Một chú kỳ nhông sáu sừng mọc lại nguyên vẹn cả chi, tủy sống, 1/3 trái tim và não bộ mà không để lại một vết sẹo! Và một sinh vật đáy biển tự bắn toàn bộ ruột gan qua hậu môn trói chặt kẻ thù! |  | Hai bóng đen tiếp theo: chú kỳ nhông Axolotl sáu sừng lơ lửng phát sáng hào quang tái sinh và sinh vật đáy biển bắn mạng tơ ruột gan rực sáng; KHÔNG có anh MC trong cảnh này. |
| b24 | 03:36.8–03:44.8 (8.0s) | L405 | Thậm chí còn có sự góp mặt của loài chim cắt lao xuống với vận tốc 389 km/h, và loài cá mặt trăng nặng hai tấn ngơ ngác bậc nhất đại |  | Hai bóng đen khổng lồ xuất hiện phía sau màn sương: bóng chim cắt xé gió lao xuống từ tầng mây và bóng cá mặt trăng tròn xoe kỳ dị; KHÔNG có anh MC trong cảnh này. |
| b25 | 03:44.8–03:53.0 (8.3s) | L406 | dương! Cộng thêm những cao thủ tí hon biết biến hóa thành thây ma và loài bò sát có sừng mọc xuyên qua hộp sọ! Mười dị nhân tiếp theo đang nóng lòng chờ ngày ra |  | Cánh cửa đường hầm Mùa 3 phát ánh sáng xanh biếc huyền bí với hàng loạt bóng đen hình thù quái dị chưa từng xuất hiện trên màn ảnh; KHÔNG có anh MC trong cảnh này. |
| b26 | 03:53.0–03:59.4 (6.4s) | L407 | mắt! Hẹn gặp lại toàn thể quý vị khán giả tại Đại Hội Sinh Tồn Mùa 3! Phóng viên và MC xin chào tạm biệt và hẹn gặp lại! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cùng mười tuyển thủ Mùa 2 đồng loạt vẫy tay chào tạm biệt khán giả trong tiếng nhạc khải hoàn rền vang khắp đấu trường. |

## 5. Phân cảnh Shorts — từng beat

Banner: **ĐẠI HỘI SINH TỒN #2 / AI LÊN NGÔI VƯƠNG?!** · giọng 49.8s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Mười quái kiệt mới. Tám vòng đấu sinh tử. Một chiếc vương miện! |  |
| s02 | 00:03.7 | S02 | Tôm Súng và Lươn Điện được đặt cược sẽ thắng. Còn Bọ Pháo Thủ nửa gam... chuyên gia bảo tham gia cho vui! |  |
| s03 | 00:09.0 | S03 | Vòng một: Tôm Súng tạo dòng plasma dưới nước hiệu suất gấp 10 lần máy laser! | **GẤP 10 LẦN** · Tạo plasma dưới nước · R/640 · [0.54, 0.52] |
| s04 | 00:13.5 | S04 | Vòng hai: Cá Cung Thủ nhận diện được 44 khuôn mặt người dù không có vỏ não! | **44 MẶT** · Nhận diện chính xác · L/620 · [0.58, 0.28] |
| s05 | 00:17.4 | S05 | Vòng ba: Gấu Trúc tắm phân ngựa tươi để khóa thụ thể lạnh, còn Quỷ Gai hất cát ẩm lên lưng giải |  |
| s06 | 00:22.1 | S06 | khát! Vòng bốn: Hà Mã bơm 400kg Silicon mỗi ngày xuống sông nuôi cả hệ sinh thái hồ châu Phi! |  |
| s07 | 00:27.4 | S07 | Vòng năm: Lươn Điện bỏ lối sống cô độc, hợp tác săn mồi theo bầy đàn hơn 100 con! |  |
| s08 | 00:31.9 | S08 | Chung kết: ai mang lại công nghệ đỉnh cao nhất cho loài người? Nấm lông lười diệt ung thư hay vòi phun tên lửa Bọ Pháo Thủ? |  |
| s09 | 00:38.1 | S09 | Và tân vương Mùa 2 là... chú bọ nửa gam từng bị gạch tên ngay từ vòng cân ký! |  |
| s10 | 00:42.0 | S10 | Bạn có đồng ý không? Xem trọn tám vòng đấu trong video dài nhé, |  |
| s11 | 00:45.7 | S11 | vì ở đây có mười quái kiệt mới, tám vòng đấu sinh tử, và một chiếc vương miện! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bóng tối bao trùm lấy một đấu trường La Mã khổng lồ giữa lòng rừng già đại ngàn... Mười chiếc bục thi đấu bọc thép đứng im lìm trong màn sương đêm kỳ bí.". Bố cục: Toàn cảnh đấu trường La Mã hoạt hình khổng lồ chìm trong màn sương đêm kỳ bí, mười chiếc bục tròn phát sáng bao quanh một bục vinh quang trung tâm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và ở chính giữa đấu trường, một chiếc vương miện vàng nạm đá quý lấp lánh đang xoay tròn trên bệ đá cẩm thạch, chờ đợi chủ nhân xứng đáng nhất.". Bố cục: Cận cảnh chiếc vương miện vàng nạm ngọc phát ra những tia sáng vàng rực rỡ trên bệ đá cẩm thạch giữa sân; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đêm nay, mười sinh vật kỳ dị từ Tập 11 đến Tập 20 của kênh Vẽ Chuyện Hoang Dã sẽ chính thức hội tụ trên cùng một sàn đấu sinh tử!". Bố cục: Mười chiếc bóng đen bí ẩn của 10 con vật (Gấu Trúc, Hà Mã, Lười, Tu Hú, Capybara, Tôm Súng, Lươn Điện, Bọ Pháo Thủ, Quỷ Gai, Cá Cung Thủ) xuất hiện tại cửa hầm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không phải để kể lại những gì khán giả đã xem, mà để đọ sức trực tiếp bằng hàng loạt phát hiện khoa học mới toanh chưa từng tiết lộ!". Bố cục: Mười đôi mắt hoạt hình rực sáng trong bóng tối với đủ thần thái: ngầu, tinh quái, điềm đạm, lờ đờ và hừng hực lửa chiến; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi loài mang theo một bí mật tiến hóa dị thường mà ngay cả những nhà sinh vật học lão luyện nhất cũng phải ngỡ ngàng bật ngửa.". Bố cục: Những biểu tượng vũ khí phát sáng lơ lửng quanh cửa hầm: tia sét xanh, ngọn lửa đỏ, giọt nước áp suất, gai bọc thép và chiếc cúp vinh quang; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bật toàn bộ đèn pha! Chào mừng toàn thể muôn loài muôn thú đã đến với Đại Hội Sinh Tồn Mùa 2!". Bố cục: Dàn đèn pha công suất lớn rọi sáng rực rỡ toàn bộ đấu trường, pháo hoa nổ tung trên bầu trời đêm; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vest đỏ tươi giơ micro vàng nở nụ cười rạng rỡ.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tôi là người dẫn chương trình đêm nay, và tôi xin cam kết danh dự: tất cả những gì bạn sắp nghe đều là những công trình nghiên cứu mới hoàn toàn!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đặt tay lên ngực cam kết, phía sau là màn hình lớn chiếu biểu tượng các tạp chí khoa học uy tín (không chữ).
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Từ việc Gấu Trúc tắm phân ngựa để chống rét, cho tới Cá Cung Thủ nhớ được 44 khuôn mặt người hay Tôm Súng bắn ra dòng plasma dưới đáy biển!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng nháy mắt hóm hỉnh, tay kia giơ tập tài liệu dày cộm có hình bánh răng và tia sét; khán đài thú rừng vẫy cờ reo hò náo nhiệt.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Luật chơi Mùa 2 vô cùng khốc liệt: tám vòng thi đấu chính thức, xen kẽ giờ giải lao hậu trường, lễ trao giải phụ và vòng phúc khảo tin đồn thế kỷ.". Bố cục: tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) hiện lên giữa sân với 8 ô thử thách: năng lượng, xạ thủ, chống chịu, tiêu hóa, bầy đàn, hành trình, phúc khảo và món quà nhân loại.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi vòng thi, ban giám khảo trao ba tấm huy chương: Vàng được 3 điểm, Bạc 2 điểm, và Đồng 1 điểm. Riêng Vòng Chung Kết sẽ được nhân đôi điểm số!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ ngồi ở bàn giám khảo trên cao gõ búa gỗ, trước mặt là khay nhung đỏ bày ba chiếc huy chương vàng, bạc, đồng sáng loáng.
```
</details>

<details><summary>L100</summary>

```text
HÌNH L100 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kết quả Vòng hai đã được chốt! Huy chương đồng thuộc về Chim Tu Hú với màn cải trang thành Chim Ưng Sẻ đánh lừa cả xóm chim chủ!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ trao huy chương đồng cho chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái đang khoe bộ lông ngực vằn ngang lịch lãm; khán đài gật gù thán phục.
```
</details>

<details><summary>L101</summary>

```text
HÌNH L101 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Huy chương bạc thuộc về Bọ Pháo Thủ với vòi phun sương tốc độ 35m mỗi giây! Và Huy chương vàng thuộc về Cá Cung Thủ với siêu năng lực nhận diện 44 khuôn mặt người!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ trao huy chương bạc cho chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C và huy chương vàng lấp lánh cho chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn; tiếng reo hò vang dậy trường bắn.
```
</details>

<details><summary>L102</summary>

```text
HÌNH L102 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bảng tổng sắp cập nhật điểm số sau hai vòng: Tôm Súng và Cá Cung Thủ đồng dẫn đầu với 3 điểm! Bọ Pháo Thủ bám sát với 2 điểm! Lươn Điện 2 điểm, Gấu Trúc 1 điểm, Tu Hú 1 điểm!". Bố cục: tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) sáng rực các cột điểm: cuộc đua giữa các siêu xạ thủ và cỗ máy năng lượng đang nóng lên từng phút!
```
</details>

<details><summary>L103</summary>

```text
HÌNH L103 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vòng ba ngay sau đây sẽ thử thách khả năng sinh tồn trước thời tiết khắc nghiệt và những giải pháp chống chọi thiên nhiên kỳ quặc nhất!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vung tay dẫn đường sang khu vực thử nghiệm khí hậu nơi bão tuyết băng giá và nắng nóng sa mạc đang cùng lúc gầm rú.
```
</details>

<details><summary>L104</summary>

```text
HÌNH L104 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chào mừng quý vị đến với Vòng ba: Thử thách chống chịu thời tiết cực hạn! Sân vận động lúc này được chia thành hai nửa đối lập: một bên là núi tuyết mùa đông lạnh buốt và một bên là sa mạc nắng cháy bỏng rát!". Bố cục: Đấu trường chia làm đôi: nửa trái phủ đầy tuyết trắng và gió bấc thổi mạnh âm năm độ C, nửa phải là cồn cát sa mạc đỏ rực khô khốc; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng khoác áo phao một nửa và mặc áo cộc tay một nửa đứng ở ranh giới.
```
</details>

<details><summary>L105</summary>

```text
HÌNH L105 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ở vòng này, ban giám khảo muốn tìm ra những bộ óc sinh tồn sáng tạo nhất: khi thiên nhiên nổi giận với cái rét cắt da hay cái nóng thiêu đốt, bạn dùng chiêu gì để sống sót?". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ cầm một chiếc nhiệt kế khổng lồ và chiếc ô che nắng, trước mặt là ba tấm huy chương vàng, bạc, đồng lấp lánh.
```
</details>

<details><summary>L106</summary>

```text
HÌNH L106 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đấu sĩ bước vào nửa sân băng tuyết đầu tiên là chú gấu mũm mĩm đến từ dãy núi Tứ Xuyên: Gấu Trúc Lớn! Một loài gấu nhưng hoàn toàn không biết ngủ đông như họ hàng gấu nâu hay gấu Bắc Cực!". Bố cục: chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu đứng giữa bão tuyết mùa đông ở nhiệt độ âm năm độ C, gió thổi vù vù qua lớp lông dày nhưng gấu trúc không có hang ngủ đông; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L107</summary>

```text
HÌNH L107 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không ngủ đông, ăn thực đơn tre nghèo nàn calo nên không tích trữ được nhiều lớp mỡ dày, làm thế nào Gấu Trúc hoang dã có thể chịu nổi những đêm đông tuyết rơi trắng xóa trên đỉnh núi cao?". Bố cục: Một nhà khoa học hoạt hình lắp camera hồng ngoại ẩn trên thân cây rừng Tứ Xuyên, theo dõi bóng dáng chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu di chuyển trong đêm đông lạnh giá; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L108</summary>

```text
HÌNH L108 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Năm 2000 20, nhóm nghiên cứu của giáo sư Fuwen Wei công bố phát hiện trên tạp chí PNAS khiến cả thế giới phải... bịt mũi ngỡ ngàng!". Bố cục: Màn hình chiếu 38 đoạn video camera hồng ngoại ghi lại một hành vi cực kỳ kỳ quặc của Gấu Trúc khi nhiệt độ tụt xuống dưới 15°C; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L109</summary>

```text
HÌNH L109 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi trời trở lạnh giữa tiết trời từ -5 đến 15°C, Gấu Trúc hoang dã đi tìm những đống phân ngựa tươi mới thải ra dưới 10 ngày tuổi!". Bố cục: chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu sục sạo dọc con đường mòn thương mại cổ xưa trên núi, mắt sáng rực khi phát hiện một đống phân ngựa còn bốc hơi ấm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giám khảo xin nhắc nhở: cấm nã đạn vào bảng điểm, cấm phóng điện vào ghế ban tổ chức và cấm đi vệ sinh giữa sân đấu!". Bố cục: Cận cảnh bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ cúi đầu nhìn qua gọng kính tròn, vẻ mặt nghiêm nghị đưa cánh ra lệnh chỉ đạo.
```
</details>

<details><summary>L110</summary>

```text
HÌNH L110 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó không ngửi cho vui... mà nó cúi xuống chà xát phân ngựa lên má, lên cổ, rồi lăn lộn toàn thân mình vào giữa đống phân ngựa cho đến khi phủ kín khắp bộ lông trắng đen!". Bố cục: chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu lăn tròn hai ba vòng phủ phân lên mặt và lưng với vẻ mặt vô cùng tận hưởng khoan khoái; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng và khán giả trợn mắt kinh ngạc; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L111</summary>

```text
HÌNH L111 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tại sao một loài vật đáng yêu lại đi tắm phân ngựa giữa mùa đông giá rét? Các nhà sinh vật học phát hiện trong phân ngựa tươi chứa nồng độ cao hai hợp chất hóa học gọi là BCP và BCPO!". Bố cục: Hình ảnh phân tử BCP và BCPO phát sáng màu cam ấm áp bốc lên từ đống phân ngựa tươi, bay vào tiếp xúc với làn da của gấu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L112</summary>

```text
HÌNH L112 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi thấm qua da, hai hợp chất này bám thẳng vào kênh cảm biến nhiệt lạnh TRPM8 trên tế bào thần kinh, khóa chặt công tắc báo lạnh khiến não bộ mất cảm giác rét buốt!". Bố cục: Mô phỏng phân tử: các hạt BCP khóa chặt chiếc cổng cảm biến lạnh TRPM8, ngọn gió tuyết thổi qua nhưng đồng hồ cảm giác của gấu báo ấm áp bình thường; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L113</summary>

```text
HÌNH L113 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhờ lớp kem ủ phân ngựa chống rét tự nhiên này, Gấu Trúc bình thản bước qua tuyết giá mà không bị co ro! Một cách dùng dược liệu tự nhiên từ môi trường đỉnh cao nhất thế giới động vật!". Bố cục: chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu đứng ngạo nghễ giữa trời tuyết với nụ cười mãn nguyện, bên cạnh là đàn chuột thí nghiệm bôi hợp chất này cũng chạy nhảy tưng bừng trên mặt băng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L114</summary>

```text
HÌNH L114 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa hết, năm 2021, nghiên cứu trên Scientific Reports còn giải mã thêm: bộ lông trắng đen nổi tiếng của Gấu Trúc thực chất là áo tàng hình hoàn hảo trong rừng núi!". Bố cục: Bức ảnh chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu đứng giữa rừng cây có tuyết và bóng râm: nhìn từ xa bộ lông hòa lẫn hoàn toàn vào đá, thân cây tối màu và mảng tuyết trắng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L115</summary>

```text
HÌNH L115 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Phần lông đen hòa vào bóng râm sâu thẳm và gốc cây ẩm ướt, còn phần lông trắng hòa lẫn vào mảng tuyết và tán lá sáng! Nhờ đó mắt của báo hoa mai và chó sói hoàn toàn không nhận ra đường viền cơ thể gấu!". Bố cục: Hình ảnh minh họa qua góc nhìn thị giác mờ của chó sói và báo đốm: chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu hoàn toàn biến mất giữa nền rừng loang lổ sáng tối; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L116</summary>

```text
HÌNH L116 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bây giờ chúng ta chuyển sang nửa sân sa mạc nắng cháy với sự góp mặt của Thằn Lằn Quỷ Gai! Ở Tập 19, khán giả đã biết nó uống nước bằng bàn chân qua rãnh mao dẫn. Nhưng nghiên cứu mới năm 2016 còn tiết lộ chi tiết sâu hơn nữa!". Bố cục: chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm đứng trên cồn cát đỏ sa mạc Úc khô khốc, nhiệt độ mặt cát bốc khói hầm hập; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L117</summary>

```text
HÌNH L117 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tiến sĩ Philipp Comanns từ Đại học RWTH Aachen Đức đã cân đo từng mi-li-gam nước trong 1 giờ uống nước của chú thằn lằn chỉ nặng 40g này!". Bố cục: Phòng thí nghiệm đo độ ẩm: chú chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm nặng 40g đứng trên bàn cân điện tử siêu chính xác có kết nối máy tính đồ thị; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L118</summary>

```text
HÌNH L118 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong 1 giờ ngâm chân vào vũng nước nhỏ, chú Quỷ Gai đóng mở hàm nhấp nháy gần 2.500 lần, mỗi ngụm hút vào miệng chỉ nhỏ đúng 0,7 μl, nhưng tổng lượng nước uống được đạt 1,28g!". Bố cục: Đồng hồ đếm số lần đóng mở miệng của chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm nhảy vọt lên 2.500 nhịp, các giọt nước siêu nhỏ 0,7 microlit xếp hàng chạy liên tục vào họng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L119</summary>

```text
HÌNH L119 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đồng thời, mạng lưới rãnh trên bề mặt da của nó còn giữ trữ lại được thêm 1,32g nước nữa giống như một chiếc bình giữ ẩm di động đeo quanh người!". Bố cục: Toàn thân chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm phát sáng mạng lưới kênh dẫn nước xanh biếc, vừa giữ nước uống vừa làm bể chứa dự phòng cho sa mạc; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nghe rõ chưa các đấu sĩ? Nhất là anh chàng Hà Mã và cô nàng Bọ Pháo Thủ đang cười tủm tỉm đằng kia!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng liếc nhìn sang chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ và chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C đang giả vờ huýt sáo ngây thơ vô số tội.
```
</details>

<details><summary>L120</summary>

```text
HÌNH L120 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và đây là cú bẻ lái quan trọng của khoa học: thực tế sương đọng buổi sáng trên sa mạc không đủ để làm đầy các rãnh mao dẫn này! Vậy làm sao nó gom đủ nước giữa cát khô?". Bố cục: Thí nghiệm làm mát thằn lằn xuống 22°C trong phòng ẩm: những hạt sương nhỏ li ti bám trên gai nhưng không đủ chảy xuống rãnh da để uống; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L121</summary>

```text
HÌNH L121 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà khoa học quan sát thấy một hành động siêu thông minh: nó dùng chân trước hất tung cát ẩm lên phủ kín lưng mình, sau đó ép chặt bụng xuống cát để các rãnh mao dẫn hút sạch từng giọt hơi ẩm từ lớp cát phủ hai mặt!". Bố cục: chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm dùng chân hất từng nắm cát ẩm từ lớp dưới mặt đất lên phủ đầy lưng, tạo thành chiếc máy ép hút nước thiên tài không tốn một giọt sức lực; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L122</summary>

```text
HÌNH L122 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyển thủ thứ ba bước vào thử thách sinh tồn khắc nghiệt của Vòng ba là Con Lười! Sống cả đời treo ngược trên ngọn cây rừng mưa nhiệt đới, cơ thể Con Lười làm sao để không bị... nghẹt thở bởi chính sức nặng của ruột gan mình?". Bố cục: chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini treo ngược bốn chân trên cành cây cao, ánh đèn X-quang chiếu xuyên qua lồng ngực để kiểm tra áp lực lên hai lá phổi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L123</summary>

```text
HÌNH L123 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ở hầu hết các loài động vật có vú, nếu bạn treo ngược đầu quá lâu, toàn bộ trọng lượng của gan, dạ dày đầy thức ăn sẽ đè bẹp xuống cơ hoành và hai lá phổi khiến việc hít thở trở nên cực kỳ mệt nhọc!". Bố cục: Hình minh họa một chú khỉ thử treo ngược người nhưng mặt đỏ bừng khó thở vì dạ dày nặng nề đè xuống phổi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L124</summary>

```text
HÌNH L124 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng năm 2014, nghiên cứu của Rebecca Cliffe công bố trên tạp chí Biology Letters đã khám phá ra một cấu trúc giải phẫu độc quyền của Con Lười: các dây chằng xơ neo nội tạng!". Bố cục: Sơ đồ giải phẫu ngực chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini: các dải dây chằng xơ chắc chắn gắn chặt lá gan và dạ dày 4 ngăn trực tiếp vào những chiếc xương sườn dưới gần cơ hoành; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L125</summary>

```text
HÌNH L125 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Những sợi dây chằng xơ đặc biệt này đóng vai trò như hệ thống dây cáp treo cầu giữ chặt gan và dạ dày cố định vào khung xương sườn, ngăn tuyệt đối không cho chúng đè lên phổi khi Con Lười treo ngược!". Bố cục: Hai lá phổi của chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini phồng xẹp nhẹ nhàng tự do trong khoang ngực, trong khi dạ dày nặng 30% trọng lượng cơ thể được treo lơ lửng an toàn phía dưới; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L126</summary>

```text
HÌNH L126 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhờ hệ thống dây cáp treo nội tạng này, Con Lười tiết kiệm được tới 13% năng lượng hô hấp mỗi khi treo ngược, giúp nó sống thong dong với chế độ ăn lá cây ít calo suốt cả cuộc đời!". Bố cục: Bảng thông số năng lượng hô hấp giảm 13%, chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini mỉm cười treo ngược một tay vẫy chào ban giám khảo đầy tự tin; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L127</summary>

```text
HÌNH L127 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và trong nửa sân nắng nóng thiêu đốt, cỗ xe tăng 3 tấn Hà Mã cũng bước vào kiểm tra khả năng chống tia cực tím dưới ánh nắng gay gắt!". Bố cục: chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ đứng giữa nắng gắt chói chang ở nửa sân sa mạc, các cảm biến đo phổ ánh sáng UV chiếu thẳng vào lớp da xám bóng của chú hà mã; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L128</summary>

```text
HÌNH L128 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Theo nghiên cứu hóa sinh nổi tiếng trên tạp chí Nature năm 2004 của giáo sư Yoko Saikawa, chất lỏng chống nắng trên da Hà Mã lúc mới tiết ra hoàn toàn... trong suốt không màu!". Bố cục: Cận cảnh lỗ chân lông chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ: một giọt dịch nhớt trong suốt như nước vừa rỉ ra dưới ánh nắng mặt trời; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L129</summary>

```text
HÌNH L129 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chỉ sau vài phút tiếp xúc với không khí, hai sắc tố axit hipposudoric và norhipposudoric tự động phản ứng biến dịch tiết thành màu đỏ tươi rực rỡ, rồi chuyển sang màu nâu sẫm bám chặt nhiều giờ liền để hấp thụ trọn dải tia UV từ 200-600nm!". Bố cục: Giọt dịch chuyển màu ngoạn mục từ trong suốt sang đỏ tươi rồi nâu óng, tạo thành tấm khiên quang học chặn đứng toàn bộ tia tử ngoại độc hại; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bây giờ, xin mời toàn thể khán đài cùng chào đón sự xuất hiện của mười tuyển thủ tinh nhuệ nhất Mùa 2 trên thảm đỏ!". Bố cục: Cửa đường hầm mở toang, ánh đèn flash chớp sáng liên hồi, khói lạnh cuồn cuộn thổi qua lối đi chính; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L130</summary>

```text
HÌNH L130 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kết quả Vòng ba cực kỳ xứng đáng! Huy chương đồng thuộc về Con Lười với hệ thống dây chằng treo nội tạng tiết kiệm 13% năng lượng thở!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ trao huy chương đồng cho chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini đang treo ngược mỉm cười hiền hậu; khán đài vỗ tay rộn rã.
```
</details>

<details><summary>L131</summary>

```text
HÌNH L131 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Huy chương bạc thuộc về Thằn Lằn Quỷ Gai với kỹ thuật hắt cát ẩm thu gom nước qua rãnh da! Và Huy chương vàng thuộc về Gấu Trúc Lớn với bí kíp tắm phân ngựa chống rét độc nhất vô nhị!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ trao huy chương bạc cho chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm và huy chương vàng cho chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu (sau khi bắt chú gấu đi tắm sạch mùi phân ngựa); pháo hoa nổ vang dội.
```
</details>

<details><summary>L132</summary>

```text
HÌNH L132 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bảng tổng sắp sau Vòng ba chứng kiến màn bứt phá ngoạn mục: Gấu Trúc Lớn vươn lên dẫn đầu với 4 điểm! Tôm Súng 3 điểm! Cá Cung Thủ 3 điểm! Thằn Lằn Quỷ Gai, Lươn Điện và Bọ Pháo Thủ đồng 2 điểm! Con Lười và Tu Hú ghi 1 điểm!". Bố cục: tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) cập nhật cột điểm cao vút của chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu ở vị trí số một; cả khán đài hò reo không ngớt trước cục diện đảo chiều không tưởng!
```
</details>

<details><summary>L133</summary>

```text
HÌNH L133 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bây giờ, đấu trường tạm nghỉ giải lao giữa hiệp để MC đột kích phòng thay đồ xem các đấu sĩ đang làm gì phía sau hậu trường!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cầm micro chạy nhanh về phía hành lang phòng thay đồ nơi mùi hương kỳ lạ và tiếng ồn ào đang vang lên.
```
</details>

<details><summary>L134</summary>

```text
HÌNH L134 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Xin chào toàn thể khán giả! Chúng ta đang có mặt trực tiếp tại khu vực phòng thay đồ của Đại Hội Sinh Tồn Mùa 2! Trong lúc ban tổ chức chuẩn bị sân khấu cho hiệp hai, hãy xem các đấu sĩ đang làm gì phía sau hậu trường!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vest đỏ cầm micro đi dọc hành lang hậu trường nhộn nhịp, các nhân viên tất bật đẩy xe thức ăn và bình oxy.
```
</details>

<details><summary>L135</summary>

```text
HÌNH L135 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vừa mới giành huy chương vàng Vòng ba, ngôi sao đang dẫn đầu bảng tổng sắp là Gấu Trúc Lớn! Nhưng khoan... cái mùi gì nồng nặc bốc ra từ phòng số 11 thế này?!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng bịt mũi nhăn mặt nhìn làn khói xanh lè bốc ra từ khe cửa phòng số 11 có dán biển hình gấu trúc.
```
</details>

<details><summary>L136</summary>

```text
HÌNH L136 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trời đất ơi! Gấu Trúc Lớn vừa mang nguyên một xô... phân ngựa tươi từ vùng núi Tứ Xuyên vào phòng nghỉ để bôi lên mặt giữ ấm giữa máy lạnh phòng chờ!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vừa mở cửa liền giật lùi lại khi thấy chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu đang đắp mặt nạ phân ngựa lên hai má, ngồi thư giãn trên ghế bành vô tư; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L137</summary>

```text
HÌNH L137 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Anh MC vào làm một miếng cho ấm người nè! Ở phòng chờ mở điều hòa 20 độ lạnh muốn đóng băng, bôi cái này vào ấm cực luôn á!". Bố cục: chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu giơ chiếc muôi đầy kem phân ngựa mời chào anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng với ánh mắt tròn xoe chân thành nhất quả đất; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L138</summary>

```text
HÌNH L138 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thôi thôi cảm ơn em, anh MC xin phép từ chối vì anh mặc vest đỏ đi dẫn chương trình chứ không phải đi leo núi tuyết! Chúc mừng em giữ vững phong độ nhé!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vội vàng đóng sập cửa chạy biến ra ngoài hành lang, vuốt ngực thở phào nhẹ nhõm làm cả trường quay cười nghiêng ngả.
```
</details>

<details><summary>L139</summary>

```text
HÌNH L139 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Điểm dừng chân tiếp theo là khu vực hồ bơi thư giãn của Bố Già Capybara! Hãy xem vị Bộ trưởng Ngoại giao đang nghỉ ngơi kiểu gì sau ba vòng chưa có điểm nào!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đẩy cửa bước vào khu vực hồ nước ấm phòng số 15, mặt nước tĩnh lặng phẳng lì không thấy bóng dáng thí sinh đâu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyển thủ số một! Thiện xạ đầm lầy sở hữu bộ não tính toán quang học không cần vỏ não! Cá Cung Thủ!". Bố cục: chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn bơi lượn trong một bồn nước di động trong suốt, đôi mắt lồi đảo quanh quét tìm mục tiêu khoe tài; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L140</summary>

```text
HÌNH L140 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ủa? Bố Già Capybara trốn đi đâu mất tiêu rồi? Trong bồn nước chẳng thấy ai ngoài mấy ngọn rong bèo lững lờ trôi... Khoan đã, nhìn kỹ mặt nước kia kìa!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng ngó nghiêng tìm kiếm khắp phòng nghỉ, trên mặt hồ chỉ thấy ba chấm nhỏ xíu nổi lềnh bềnh sát nhau; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L141</summary>

```text
HÌNH L141 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hóa ra vị trí mắt, tai và hai lỗ mũi của Capybara nằm xếp thẳng hàng trên đỉnh đầu giống hệt cấu tạo của Hà Mã! Nó đang ngủ say giấc nồng ngay dưới lòng hồ chỉ để hở đúng mắt mũi tai lên mặt nước!". Bố cục: Cận cảnh dưới làn nước trong suốt: toàn bộ cơ thể béo múp 65kg của chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia đang nằm ngủ ngon lành dưới đáy hồ, chỉ để lộ đúng đỉnh mũi và hai mắt trên mặt nước; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L142</summary>

```text
HÌNH L142 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một tư thế ngủ vừa giữ mát làn da, vừa dễ dàng thở không khí và quan sát động tĩnh xung quanh mà không kẻ thù nào phát hiện được!". Bố cục: Bóng báo đốm đi ngang qua bờ hồ nhìn lướt qua nhưng không thấy gì ngoài ba chấm nhỏ tưởng là cành cây khô; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L143</summary>

```text
HÌNH L143 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chào Bố Già! Nằm ngâm nước thế này thì chút nữa thi Vòng bốn có bị lạnh bụng không ạ?". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng khom người dí micro sát mặt nước phỏng vấn nhỏ nhẹ để không làm đánh thức giấc ngủ trưa của Bố Già; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L144</summary>

```text
HÌNH L144 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khò... khò... Nước ấm thế này ngủ sướng lắm anh bạn... Để tôi ngủ thêm 10 phút nữa rồi ra cân hết Vòng bốn cho anh xem!". Bố cục: chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia mở hé một mắt, ngáp một cái nhẹ nhàng rồi nhắm mắt ngủ tiếp tạo ra mấy bọt khí bong bóng phồng ở mũi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L145</summary>

```text
HÌNH L145 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thần thái của người đàn ông chưa có điểm nào mà vẫn ngủ ngon lành như đang nắm chắc chiếc cúp vô địch trong tay! Bây giờ chúng ta ghé thăm phòng của Chim Tu Hú!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng bước sang phòng số 14, nơi chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái đang ngồi xếp gọn một chiếc ba lô du lịch mini và đeo thiết bị định vị GPS; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L146</summary>

```text
HÌNH L146 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chào Chim Tu Hú! Sao trong phòng nghỉ mà bạn lại chuẩn bị hành lý bay đi đâu thế này? Chúng ta vẫn còn năm vòng thi nữa cơ mà!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng ngạc nhiên chỉ tay vào chiếc bản đồ thế giới trải rộng trên bàn phòng nghỉ của chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L147</summary>

```text
HÌNH L147 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Anh MC không biết rồi! Sau giải đấu này, tôi phải bay ngay chuyến bay đường dài 16.000km từ châu Âu sang tận Trung Phi để tránh rét mùa đông đấy! Tôi chỉ tranh thủ ghé đây kiếm ít huy chương thôi!". Bố cục: chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái đeo kính râm phi công, chỉ tay vào đường bay đỏ vẽ hình vòng cung khép kín qua lục địa châu Phi trên bản đồ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L148</summary>

```text
HÌNH L148 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chà, đúng là phi công hạng nặng! Và căn phòng cuối cùng trong giờ giải lao là phòng của cô nàng Con Lười! Không biết bạn ấy đã tiêu hóa xong chiếc lá từ hồi khai mạc chưa?". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng nhẹ nhàng hé cửa phòng số 13, ánh đèn vàng dịu nhẹ chiếu lên cành cây nơi chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini đang treo ngược; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L149</summary>

```text
HÌNH L149 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ban tổ chức trang bị một chiếc đồng hồ bấm giờ treo ngay cạnh mặt Con Lười! MC đặt một câu hỏi ngắn: bạn cảm thấy đấu trường Mùa 2 thế nào?". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng giơ micro lên trước mặt chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini, kim đồng hồ bấm giờ bắt đầu chạy tích tắc từng giây từng phút; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyển thủ số hai! Chiến binh sa mạc Úc mặc áo giáp chông sắt và hút ẩm từ cát khô! Thằn Lằn Quỷ Gai!". Bố cục: chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm đội mũ safari kaki lạch bạch bước ra thảm đỏ, toàn thân phủ kín hàng trăm chiếc gai nón nhọn hoắt oai phong; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L150</summary>

```text
HÌNH L150 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Con Lười nhướng mày... mở hé miệng... mất 5 giây để hít hơi... mất 10 giây để cong môi... và mất cả 1 phút mới phát âm được chữ đầu tiên!". Bố cục: Cận cảnh chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini nhếch mép từ từ như phim quay chậm 0,1 lần, anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng chống cằm chờ đợi mắt dần díu lại; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L151</summary>

```text
HÌNH L151 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tôi... cảm... thấy... đại... hội... năm... nay... rất... là... vui... luôn... ạ...". Bố cục: Khi chữ cuối cùng thoát ra khỏi miệng Con Lười, thì nhân viên hậu trường đã kịp ăn xong hai tô phở và dọn dẹp sạch sẽ cả hành lang! [laughter] :: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng giật mình tỉnh giấc khi nghe tiếng chuông báo hết giờ giải lao vang lên inh ỏi, nhân viên đang lau sàn mỉm cười lắc đầu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L152</summary>

```text
HÌNH L152 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa hết đâu quý vị! Ghé ngang phòng số 16 của Tôm Súng, chúng ta bắt gặp chú tôm đang ngồi đánh bóng khẩu đại bác cùng người bạn thân thiết là một chú cá bống mắt lồi!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng nhìn qua ô cửa kính bể nước phòng 16: chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa đang dùng càng nhỏ lau chùi càng súng to, bên cạnh là chú cá bống nhỏ vẫy đuôi canh gác cửa phòng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L153</summary>

```text
HÌNH L153 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chú cá bống làm nhiệm vụ canh cửa bảo vệ còn Tôm Súng dùng càng đào cát làm phòng ở chung sang trọng! Một cặp đôi bạn thân gắn bó keo sơn nhất thế giới biển cả!". Bố cục: chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa chạm nhẹ cặp râu dài lên đuôi cá bống ăn mừng, hai người bạn cùng vẫy tay chào ống kính máy quay thân thiện; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L154</summary>

```text
HÌNH L154 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn trong phòng bên cạnh, nhà máy điện Lươn Điện đang vừa bơi lội thư giãn vừa thưởng thức bữa ăn nhẹ bằng thịt cá nhỏ để nạp đầy năng lượng cho bộ bơm ion Natri Kali!". Bố cục: chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh lượn vòng trong bể nước ấm, vài tia điện nhỏ lách tách sáng lên màu xanh dịu báo hiệu dung lượng pin đã đầy một trăm phần trăm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L155</summary>

```text
HÌNH L155 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn tại góc phòng sa mạc nhân tạo, Thằn Lằn Quỷ Gai đang tận hưởng bồn tắm cát ẩm mát rượi, chuẩn bị tinh thần đối đầu với gã khổng lồ Hà Mã ở vòng bốn!". Bố cục: chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm nằm thư thái phủ một lớp cát ẩm mịn lên khắp sống lưng gai góc, nhấp nháy miệng uống nước đầy sảng khoái; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L156</summary>

```text
HÌNH L156 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bước sang phòng số 20 của Cá Cung Thủ, chúng ta bắt gặp chú cá đang nhìn chằm chằm vào một cuốn an-bum ảnh chân dung dán đầy mặt các thành viên ban tổ chức!". Bố cục: chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn bơi sát thành bể kính, mắt đảo qua lại soi xét hàng loạt tấm ảnh chụp mặt anh MC và bà giám khảo Cú mèo; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L157</summary>

```text
HÌNH L157 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chú cá đang luyện tập ghi nhớ từng nếp nhăn trên khuôn mặt của giám khảo để phòng trường hợp giám khảo chấm điểm thiếu công bằng là... phun nước thẳng vào kính!". Bố cục: chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn nháy mắt tinh ranh ngậm đầy một họng nước, anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng giật mình lấy chiếc micro che mặt lùi lại phòng thủ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L158</summary>

```text
HÌNH L158 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sang tới phòng số 18 của Bọ Pháo Thủ, ban tổ chức thấy một cái bàn đầy ắp các loại lá cây và xác côn trùng giàu dưỡng chất giúp chú bọ nạp lại kho nguyên liệu hóa học!". Bố cục: chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C ngồi trước mâm cơm thịnh soạn nạp nhiên liệu cho túi dự trữ hydroquinone và oxy già sau những phát bắn thử nghiệm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L159</summary>

```text
HÌNH L159 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn trong bồn tắm bùn khổng lồ ở cuối hành lang, gã khổng lồ Hà Mã đang ngâm mình thư giãn, làn da tiết ra lớp dịch nhờn trong suốt dần chuyển màu đỏ hồng lấp lánh dưới ánh đèn phòng thay đồ!". Bố cục: chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ ngâm mình ngập tới mang tai trong bồn bùn rộng lớn, thả những bong bóng nước to đùng thư thái giữa giờ nghỉ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyển thủ số ba! Siêu pháo thủ tí hon chỉ dài bằng đốt ngón tay nhưng truyền cảm hứng cho động cơ tên lửa! Bọ Pháo Thủ!". Bố cục: chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C bước ra, sau đuôi bốc lên một làn khói trắng nghi ngút từ nòng pháo mini cực ngầu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L160</summary>

```text
HÌNH L160 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Này anh MC, chút nữa thi vòng dinh dưỡng nhớ chuẩn bị thật nhiều cỏ non nhé, chứ tôi đang đói cồn cào cả ba ngăn dạ dày rồi đấy!". Bố cục: chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ há to chiếc miệng rộng ngoác 150 độ ngáp một cái vang rền làm rung cả cửa kính phòng thay đồ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L161</summary>

```text
HÌNH L161 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vâng vâng, ban tổ chức đã chuẩn bị sẵn cả một xe tải cỏ tươi ngoài sân rồi ạ!". Bố cục: Nhân viên kéo một xe tải chất đầy cỏ non xanh mướt tiến về phía khu vực thi đấu Vòng bốn; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng lau mồ hôi vẫy tay tạm biệt chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ.
```
</details>

<details><summary>L162</summary>

```text
HÌNH L162 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trên đường quay lại sân chính, MC còn bắt gặp Gấu Trúc Lớn đang tập động tác trồng cây chuối khởi động cơ tay trước khi bước vào vòng thi tiêu hóa!". Bố cục: chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu chống hai tay xuống thảm tập thể dục lắc lư cái bụng tròn, khuôn mặt tập trung cao độ nhưng lại ngã lăn kềnh hài hước; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L163</summary>

```text
HÌNH L163 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn anh chàng Cá Cung Thủ và Tôm Súng thì đang thi xem ai bắn trúng bia nhanh hơn ở hành lang làm ướt sũng cả chiếc áo vest đỏ của MC!". Bố cục: chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn và chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa đồng loạt bắn tia nước trúng mục tiêu, giọt nước bắn tung tóe ướt hết vạt áo anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng làm khán giả cười ồ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L164</summary>

```text
HÌNH L164 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giờ nghỉ giải lao đầy ắp tiếng cười đã kết thúc! Chuông báo động hiệp hai vang lên dồn dập đưa toàn thể đấu sĩ quay trở lại sàn đấu chính!". Bố cục: Tiếng còi vang dội khắp hành lang, mười tuyển thủ chỉnh trang lại trang phục tiến ra đường hầm bước vào chặng đua tăng tốc của hiệp hai.
```
</details>

<details><summary>L165</summary>

```text
HÌNH L165 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vòng bốn ngay sau đây sẽ giải mã những bí mật động trời về dinh dưỡng và sức ảnh hưởng sinh thái của các đấu sĩ! Hãy sẵn sàng đón xem!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vung tay dẫn đường ra sân khấu chính nơi màn hình phân tích sinh thái học khổng lồ đã bật sáng rực rỡ.
```
</details>

<details><summary>L166</summary>

```text
HÌNH L166 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chào mừng toàn thể quý vị trở lại với hiệp hai của Đại Hội Sinh Tồn Mùa 2: Vòng bốn — Dinh dưỡng dị thường và chuỗi cung ứng sinh thái!". Bố cục: Sân khấu chính biến thành một mô hình hệ sinh thái sông ngòi châu Phi và rừng nhiệt đới rộng lớn với các biểu đồ hóa chất phát sáng; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cầm micro giới thiệu.
```
</details>

<details><summary>L167</summary>

```text
HÌNH L167 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ở vòng thi này, ban giám khảo không chỉ nhìn vào việc con vật ăn cái gì, mà còn đánh giá xem hệ tiêu hóa của nó mang lại tác động kinh thiên động địa nào cho thiên nhiên xung quanh!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ đeo kính soi vào ống nghiệm chứa các khoáng chất lấp lánh, trước mặt là ba tấm huy chương vàng, bạc, đồng sáng chói.
```
</details>

<details><summary>L168</summary>

```text
HÌNH L168 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thí sinh đầu tiên bước vào vòng cân đo sinh thái là cỗ xe tăng 3 tấn châu Phi: Hà Mã! Khán giả đều biết Hà Mã thích quạt đuôi văng phân đánh dấu lãnh thổ, nhưng nghiên cứu năm 2019 đã phát hiện một bí mật vĩ đại ẩn trong đống phân đó!". Bố cục: chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ bệ vệ bước lên sàn khấu mô phỏng dòng sông Mara ở Kenya, bên dưới là những đàn cá nhỏ và tảo thủy sinh đang bơi lội; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L169</summary>

```text
HÌNH L169 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Năm 2019, nhà sinh thái học Jonas Schoelynck tại Đại học Antwerp Bỉ công bố một nghiên cứu chấn động trên tạp chí uy tín Science Advances!". Bố cục: Trang bài báo Science Advances năm 2019 hiện lên dòng tiêu đề gọi Hà Mã là 'Cỗ máy bơm nguyên tố Silicon sống của tự nhiên'; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyển thủ số bốn! Cỗ máy phát điện sống biết hợp tác săn mồi theo bầy đàn hơn 100 con! Lươn Điện!". Bố cục: chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh uốn lượn trong bể nước kính cường lực, thân phát ra những tia điện xanh neon chói lòa; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L170</summary>

```text
HÌNH L170 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vào ban đêm, mỗi con Hà Mã rời mặt nước lên đồng cỏ gặm hàng chục ký cỏ giàu chất khoáng Silicon thực vật. Đến ban ngày, chúng quay về ngâm mình dưới sông và bài tiết toàn bộ số khoáng chất đó xuống dòng nước!". Bố cục: chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ ăn cỏ xanh mướt trên thảo nguyên ban đêm dưới ánh trăng, sau đó nhảy xuống dòng sông Mara thư giãn vào ban ngày; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L171</summary>

```text
HÌNH L171 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà khoa học đo được con số kinh hoàng: đàn Hà Mã dọc theo sông Mara ở Kenya bơm trực tiếp khoảng 0,4 tấn nguyên tố Silicon nguyên chất xuống lòng sông mỗi ngày!". Bố cục: Chiếc cân tải trọng khổng lồ hiển thị con số 400 kg tinh thể Silicon lấp lánh chảy ào ào vào dòng nước xanh biếc; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L172</summary>

```text
HÌNH L172 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Số Silicon do Hà Mã vận chuyển chiếm tới 76% tổng lượng dòng chảy Silicon của toàn bộ con sông lớn! Không có Hà Mã, con sông gần như mất đi ba phần tư nguồn cung Silicon tự nhiên!". Bố cục: Biểu đồ tròn dòng chảy Silicon: 76% màu đỏ mang biểu tượng chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ, chỉ 24% đến từ xói mòn đất đá tự nhiên; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L173</summary>

```text
HÌNH L173 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tại sao Silicon lại quan trọng đến thế? Bởi vì nó là vật liệu thiết yếu để loài tảo khuê cực nhỏ dưới hồ Victoria xây dựng lớp vỏ thủy tinh và quang hợp tạo oxy nuôi sống hàng triệu con cá thương phẩm!". Bố cục: Kính hiển vi soi các tế bào tảo khuê lấp lánh như những viên pha lê thủy tinh dưới đáy hồ, đàn cá lớn bơi lượn đông đúc vui tươi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L174</summary>

```text
HÌNH L174 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa hết, dù trông giống lợn, Hà Mã thực chất tiến hóa một chiếc dạ dày ba ngăn lên men vi sinh cực kỳ phức tạp gọi là hệ tiêu hóa giả nhai lại!". Bố cục: Sơ đồ giải phẫu dạ dày 3 ngăn của chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ: thức ăn lên men từ từ trong các ngăn chứa vi khuẩn giúp nó sống khỏe dù ăn ít hơn bò nhiều lần; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L175</summary>

```text
HÌNH L175 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhờ hệ thống lên men ba ngăn tiết kiệm năng lượng này, một cỗ xe tăng nặng 3 tấn chỉ cần ăn lượng cỏ bằng khoảng 1,5% trọng lượng cơ thể mỗi ngày là đủ sinh tồn!". Bố cục: Bảng so sánh lượng ăn: con bò ăn một đống cỏ khổng lồ so với phần ăn khiêm tốn hơn nhiều của chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L176</summary>

```text
HÌNH L176 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và nhân tiện nhắc tới đường ruột kỳ lạ trong vòng dinh dưỡng này, khoa học năm 2015 còn phát hiện thêm một sự thật sốc nữa về hệ vi sinh vật trong bụng Gấu Trúc Lớn!". Bố cục: Phòng thí nghiệm sinh học phân tử chiếu ảnh phóng đại hàng tỷ vi khuẩn sống bên trong đường ruột của chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L177</summary>

```text
HÌNH L177 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Theo nghiên cứu công bố trên tạp chí mBio khi phân tích hàng loạt mẫu phân của Gấu Trúc qua các mùa, đường ruột của chúng vẫn... không hề tiến hóa ra nhóm vi khuẩn tiêu hóa xen-lu-lô như loài bò hay cừu!". Bố cục: Biểu đồ so sánh vi khuẩn ruột: ruột bò đầy vi khuẩn Ruminococcaceae phân hủy cỏ, còn ruột chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu lại toàn vi khuẩn Escherichia và Streptococcus giống hệt chó sói và hổ! KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L178</summary>

```text
HÌNH L178 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tức là suốt 2 triệu năm chuyển sang ăn chay, ngay cả đội quân vi khuẩn trong bụng Gấu Trúc vẫn giữ nguyên cấu trúc của thú ăn thịt! Một màn bảo thủ di truyền cứng đầu nhất lịch sử tiến hóa!". Bố cục: chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu nhìn vào kính hiển vi thấy đội quân vi khuẩn ăn thịt trong bụng mình liền ngơ ngác gãi đầu cười trừ, cả khán đài cười ồ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L179</summary>

```text
HÌNH L179 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn chú Con Lười thì sao? Bên cạnh tốc độ tiêu hóa siêu chậm, Con Lười còn điều chỉnh thân nhiệt biến thiên linh hoạt từ 24°C vào ban đêm lên 33°C lúc phơi nắng giống như loài bò sát!". Bố cục: Biểu đồ nhiệt độ cơ thể chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini dao động nhịp nhàng theo ánh nắng mặt trời từ 24°C đến 33°C giúp tiết kiệm tối đa năng lượng chuyển hóa; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyển thủ số năm! Thủ lĩnh đội quân tôm lính sống trong tổ bọt biển dưới quyền một Tôm Chúa! Tôm Súng!". Bố cục: chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa giơ chiếc càng búng khổng lồ to bằng nửa thân hình lên trời, đeo kính ngắm bắn tỉa cực kỳ tự tin; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L180</summary>

```text
HÌNH L180 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giám khảo kinh ngạc: phân của Hà Mã hóa ra lại là nguồn phân bón khoáng chất vàng nuôi sống cả một hệ sinh thái hồ khổng lồ châu Phi!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ vỗ tay thán phục, đặt ngôi sao điểm tối đa cho chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ trên bảng chấm thi.
```
</details>

<details><summary>L181</summary>

```text
HÌNH L181 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyển thủ thứ hai bước lên sàn đo dinh dưỡng là Bố Già đầm lầy: Capybara! Ngoài tập tính ăn lại phân mềm buổi sáng đã nổi tiếng, Bố Già còn có một bí mật về bộ răng cửa đáng kinh ngạc!". Bố cục: chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia ngồi trước một bàn tiệc gồm toàn cỏ lau cứng, vỏ cây sần sùi và quả bí đỏ tươi ngon; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L182</summary>

```text
HÌNH L182 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giống như họ hàng nhà hải ly và sóc, cặp răng cửa hình chiếc đục sắc bén ở hàm trước của Capybara... mọc dài ra không bao giờ ngừng suốt cả cuộc đời!". Bố cục: Phóng đại hàm răng cửa màu trắng ngà của chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia: mũi tên chỉ tốc độ răng mọc dài ra liên tục mỗi tuần như hai chiếc đục thép; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L183</summary>

```text
HÌNH L183 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu một chú Capybara lười biếng không chịu nhai, cặp răng cửa sẽ mọc dài đâm xuyên qua cả hàm làm nó không thể đóng miệng lại được!". Bố cục: Hình minh họa hài hước: chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia tưởng tượng răng mình mọc dài thòng lọng như răng nanh ma cà rồng rồi giật mình lắc đầu nguầy nguậy; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L184</summary>

```text
HÌNH L184 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Để giữ cho hàm răng luôn ngắn gọn và sắc bén, mỗi ngày Bố Già phải tiêu thụ đều đặn từ 3-4kg cỏ xơ cứng chứa đầy tinh thể cát và gặm cả vỏ cây gỗ cứng để mài mòn men răng tự nhiên!". Bố cục: chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia gặm cành cây vỏ cứng rôm rốp làm những tia lửa mài răng lóe sáng hoạt hình đầy thú vị; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L185</summary>

```text
HÌNH L185 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đồng thời, men răng của nó có cấu trúc tự mài sắc: mặt ngoài cứng hơn mặt trong, khiến càng nhai đồ cứng thì lưỡi răng lại càng trở nên bén ngọt hơn như dao gọt hoa quả!". Bố cục: Cận cảnh lưỡi răng cửa chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia được mài vát chéo sắc lẹm như mũi dao thợ mộc, cắt phăng thân cây sậy chỉ trong một nhát cắn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L186</summary>

```text
HÌNH L186 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và tuyển thủ thứ ba mang đến bài thi dinh dưỡng cực kỳ dị biệt: Thằn Lằn Quỷ Gai! Ở Tập 19 chúng ta đã biết thực đơn độc nhất của nó là kiến đen, nhưng chiến thuật bẫy kiến của nó mới thực sự là bậc thầy kiên nhẫn!". Bố cục: chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm đứng bất động bên một con đường mòn đầy kiến đen Iridomyrmex đang bò tấp nập giữa cát đỏ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L187</summary>

```text
HÌNH L187 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nghiên cứu sinh thái học tại Tây Úc cho thấy Thằn Lằn Quỷ Gai không bao giờ đuổi theo đàn kiến tốn sức! Nó chọn ngồi lì đúng tại ngã tư đường mòn giao nhau vào lúc sáng sớm hoặc chiều mát khi đàn kiến đi kiếm ăn đông nhất!". Bố cục: Bản đồ chiến thuật của chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm: ngồi phục kích ngay nút giao thông ngã tư của bầy kiến giống cảnh sát giao thông chặn chốt kiểm tra; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L188</summary>

```text
HÌNH L188 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi cú phóng lưỡi dính diễn ra trong chớp mắt, tiêu thụ hàng ngàn con kiến chứa axit formic nhưng lại giữ cho độ pH dạ dày cân bằng hoàn hảo nhờ dịch đệm kiềm tính đặc biệt!". Bố cục: Bên trong dạ dày chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm: các bọt dịch kiềm màu xanh lam trung hòa ngay lập tức những giọt axit đỏ rực từ bụng đàn kiến; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L189</summary>

```text
HÌNH L189 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đặc biệt, chiếc gù mỡ sau cổ và phần đuôi mập của nó đóng vai trò như một kho pin thực phẩm dự trữ, giúp nó nhịn ăn hoàn toàn suốt mùa đông khắc nghiệt khi đàn kiến chui sâu xuống lòng đất!". Bố cục: Chiếc đuôi mập mạp phát sáng lớp năng lượng mỡ dự trữ vàng óng, chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm yên tâm cuộn tròn nghỉ ngơi chờ mùa xuân tới; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyển thủ số sáu! Quý ngài ngoại giao Pantanal nuôi con chung bình đẳng và ngủ ngâm mình dưới lòng sông! Capybara!". Bố cục: chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia đội chiếc mũ phớt đen mafia thong thả bước ra, mắt híp tịt điềm đạm trước rừng ống kính phóng viên; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L190</summary>

```text
HÌNH L190 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa dừng lại ở đó, ban giám khảo còn chấm thêm điểm cộng cho khả năng giữ gìn và sử dụng răng hàm của Gấu Trúc Lớn!". Bố cục: Cận cảnh hàm răng hàm bản rộng phẳng lì của chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu đang nghiền nát một thân tre già cứng như gỗ lim; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L191</summary>

```text
HÌNH L191 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khác với răng nhọn xé thịt của hổ hay sư tử, răng hàm của Gấu Trúc đã tiến hóa to gấp 7 lần bình thường với lớp men răng cực dày có khả năng tự phục hồi các vết nứt siêu nhỏ khi nhai tre cứng suốt 14 tiếng mỗi ngày!". Bố cục: Sơ đồ men răng chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu phóng đại hàng ngàn lần: các lớp tinh thể khoáng xếp đan xen giúp tự làm lành vết nứt vi mô khi chịu lực nén khổng lồ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L192</summary>

```text
HÌNH L192 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn gã khổng lồ Hà Mã nhờ có dạ dày ba ngăn lên men hiệu quả mà có thể ung dung dành tới 16 tiếng mỗi ngày ngâm mình nghỉ ngơi dưới sông mà chẳng cần ăn suốt cả ban ngày!". Bố cục: chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ nằm ngâm mình thư thái dưới dòng sông xanh mát, đàn cá nhỏ bơi lượn quanh người dọn sạch ký sinh trùng trên da; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L193</summary>

```text
HÌNH L193 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ban giám khảo công bố kết quả Vòng bốn! Huy chương đồng thuộc về Thằn Lằn Quỷ Gai với chiến thuật phục kích ngã tư và kho mỡ đuôi dự trữ năng lượng!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ trao huy chương đồng cho chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm đang giơ ngón cái đầy tự hào; khán đài vỗ tay tán thưởng.
```
</details>

<details><summary>L194</summary>

```text
HÌNH L194 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Huy chương bạc thuộc về Capybara với cặp răng cửa tự mài sắc mọc vĩnh cửu! Và Huy chương vàng thuộc về Hà Mã với công trạng bơm 400kg Silicon mỗi ngày nuôi sống dòng sông!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ trao huy chương bạc cho chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia và huy chương vàng sáng loáng cho chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ; cả đấu trường reo hò nồng nhiệt.
```
</details>

<details><summary>L195</summary>

```text
HÌNH L195 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bảng tổng sắp cập nhật điểm số mới nhất: Gấu Trúc dẫn đầu 4 điểm! Tôm Súng 3 điểm! Cá Cung Thủ, Thằn Lằn Quỷ Gai và Hà Mã cùng chạm mốc 3 điểm! Lươn Điện, Bọ Pháo Thủ, Capybara đồng 2 điểm! Tu Hú và Con Lười 1 điểm!". Bố cục: tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) rực sáng bảng điểm cân bằng cực kỳ căng thẳng, khoảng cách giữa các đấu sĩ chỉ tính bằng một tấm huy chương!
```
</details>

<details><summary>L196</summary>

```text
HÌNH L196 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vòng năm ngay sau đây sẽ lật mở những xã hội bí mật và sức mạnh bầy đàn gây sốc nhất thế giới động vật! Đừng bỏ lỡ!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vung tay chỉ về phía đấu trường hợp tác xã hội nơi hàng trăm cá thể nhỏ bé đang tập hợp thành một đội quân hùng mạnh.
```
</details>

<details><summary>L197</summary>

```text
HÌNH L197 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chào mừng toàn thể khán đài bước vào Vòng năm: Sức mạnh bầy đàn và những xã hội bí mật! Lâu nay chúng ta thường nghĩ những sát thủ mang vũ khí hạng nặng đều thích hành động đơn độc như sói hoang.". Bố cục: Sân đấu tối sầm lại rồi bật đèn chiếu sáng ba mô hình sinh thái bí ẩn: một rạn san hô bọt biển, một hồ sông Amazon sâu thẳm và một đầm lầy cỏ lau rộng lớn; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng hạ thấp giọng đầy kịch tính.
```
</details>

<details><summary>L198</summary>

```text
HÌNH L198 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng trong thế giới khoa học hiện đại, những phát hiện mới nhất đã lật nhào hoàn toàn định kiến đó! Hãy chuẩn bị tinh thần chứng kiến màn lột xác của ba tuyển thủ đêm nay!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ mở cuốn hồ sơ mật đóng dấu đỏ tuyệt mật, trước mặt là ba tấm huy chương vàng, bạc, đồng chờ trao cho đội quân xuất sắc nhất.
```
</details>

<details><summary>L199</summary>

```text
HÌNH L199 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ứng cử viên đầu tiên bước lên bục là pháo thủ đại dương: Tôm Súng! Ai cũng biết nó sống cộng sinh với cá bống gác hang, nhưng ít ai biết một nhánh họ hàng của Tôm Súng lại thiết lập hẳn một... vương quốc ong kiến dưới đáy biển!". Bố cục: chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa vẫy càng gọi tới một khối bọt biển khổng lồ màu vàng cam rực rỡ từ đại dương Caribe, bên trong lúc nhúc hàng trăm sinh vật nhỏ bé; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyển thủ số bảy! Kẻ cải trang thành chim ưng để đánh lừa hàng xóm và bay vòng tròn 16.000km mỗi năm! Chim Tu Hú!". Bố cục: chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái bay lượn sà xuống mép bục, nơ tím than lịch lãm, mắt đỏ nhấp nháy nhếch mép láu cá; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L200</summary>

```text
HÌNH L200 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Năm 1996, nhà sinh vật học biển Emmett Duffy công bố một phát hiện làm chấn động giới động vật học trên tạp chí Nature danh tiếng!". Bố cục: Trang bìa tạp chí Nature năm 1996 hiện lên hình ảnh phóng đại loài tôm súng bọt biển Synalpheus regalis sống thành bầy đàn khổng lồ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L201</summary>

```text
HÌNH L201 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cho đến trước năm 1996, khái niệm xã hội bậc cao eusociality — tức là có 1 con chúa duy nhất đẻ trứng, còn hàng trăm con khác hy sinh quyền sinh sản để đi làm lính bảo vệ tổ — chỉ được tìm thấy ở côn trùng như ong, kiến, mối và chuột dũi trần trên cạn!". Bố cục: Biểu đồ phân loại xã hội tự nhiên: ong mật, kiến lửa và mối trên cạn đứng cạnh một dấu chấm hỏi khổng lồ dưới đáy biển xanh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L202</summary>

```text
HÌNH L202 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và loài tôm súng Synalpheus regalis chính là loài sinh vật biển đầu tiên trên hành tinh được xác nhận sở hữu cấu trúc xã hội bậc cao eusociality giống hệt như kiến và ong!". Bố cục: Cắt lớp chiếc bọt biển dưới kính hiển vi: hơn ba trăm con tôm súng sống chen chúc trong các đường hầm bọt biển như một thành phố ngầm thu nhỏ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L203</summary>

```text
HÌNH L203 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong một tổ bọt biển chứa hơn 300 thành viên đó, chỉ có duy nhất một Tôm Chúa cái khổng lồ làm nhiệm vụ sinh sản!". Bố cục: Cận cảnh Tôm Chúa to béo nằm ở trung tâm buồng an toàn bên trong bọt biển, trên đầu đội chiếc vương miện nhỏ xíu lấp lánh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L204</summary>

```text
HÌNH L204 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Toàn bộ hàng trăm con tôm lính còn lại — vốn là anh chị em ruột thịt của nhau — hoàn toàn không bao giờ sinh sản! Chúng sở hữu chiếc càng súng lớn hơn hẳn để làm lính gác bảo vệ các lối vào tổ bọt biển trước kẻ thù xâm lược!". Bố cục: Đội quân tôm lính xếp hàng dọc các lỗ thông hơi của bọt biển, đồng loạt giơ càng súng nhắm thẳng ra ngoài sẵn sàng nhả đạn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L205</summary>

```text
HÌNH L205 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi có cua hoặc cá lạ mon men tới gần, cả đội quân tôm lính đồng loạt búng càng tạo thành dàn pháo thanh âm đẩy lùi kẻ thù bảo vệ Tôm Chúa và đàn em nhỏ an toàn tuyệt đối!". Bố cục: Kẻ xâm nhập bị sóng xung kích từ hàng chục khẩu súng tôm bắn bật ngửa ra xa không kịp trở tay; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L206</summary>

```text
HÌNH L206 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một đế chế quân sự thu nhỏ có nữ hoàng và binh lính ngay trong lòng đại dương! Một phát hiện thay đổi cả sách giáo khoa sinh học biển!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vỗ tay thán phục trước thành phố bọt biển của chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa, khán giả trầm trồ không ngớt.
```
</details>

<details><summary>L207</summary>

```text
HÌNH L207 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tiếp theo là một cú sốc thứ hai đến từ rừng rậm Amazon, làm đảo lộn hàng trăm năm hiểu biết của loài người về tuyển thủ Lươn Điện!". Bố cục: Đèn sân khấu tắt tối om rồi chiếu rọi vào một khúc sông nhỏ mang tên Iriri tại bang Pará nước Brazil; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L208</summary>

```text
HÌNH L208 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Suốt hơn hai thế kỷ kể từ thời nhà thám hiểm Alexander von Humboldt, cả thế giới khoa học đều khẳng định Lươn Điện là loài sát thủ cô độc tuyệt đối, đi săn một mình vào ban đêm!". Bố cục: Bức tranh cũ vẽ một con lươn điện bơi cô đơn một mình giữa dòng sông tối đen như mực; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L209</summary>

```text
HÌNH L209 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cho đến tháng giêng năm 2021, nhóm nghiên cứu của giáo sư Douglas Bastos và tiến sĩ David de Santana công bố phát hiện kinh hoàng trên tạp chí Ecology and Evolution!". Bố cục: Hình ảnh chiếc máy quay dưới nước ghi lại cảnh tượng chưa từng có trong tự nhiên tại một hồ nước nông nối với sông Iriri; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyển thủ số tám! Chú gấu lười rừng mưa mang cả vườn nấm tiêu diệt tế bào ung thư trên từng sợi lông! Con Lười!". Bố cục: chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini được một nhân viên kéo trên chiếc xe lăn phủ rêu xanh, một tay giơ lên chào khán giả với tốc độ cực chậm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L210</summary>

```text
HÌNH L210 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Họ phát hiện một bầy đàn khổng lồ gồm hơn 100 con Lươn Điện trưởng thành — dài từ 1,2-1,8m — đang tụ họp và phối hợp săn mồi tập thể giống hệt như bầy sói hay đàn cá voi sát thủ!". Bố cục: Hơn một trăm con chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh bơi thành vòng tròn lớn rộng hàng chục mét, tỏa ra ánh sáng xanh neon rực rỡ khắp mặt hồ nước tối; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L211</summary>

```text
HÌNH L211 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi khi bình minh và hoàng hôn buông xuống, hơn 100 con lươn này cùng bơi vòng tròn lùa hàng ngàn con cá nhỏ dồn chặt lại thành một quả cầu mồi khổng lồ sát bờ nước nông!". Bố cục: Hàng ngàn chú cá nhỏ bị dồn ép co cụm lại thành một quả cầu bạc xoay tròn ở vùng nước cạn, bị vây kín tứ phía bởi bức tường lươn điện; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L212</summary>

```text
HÌNH L212 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sau đó, từng tốp từ 2-10 con Lươn Điện tách đội hình áp sát quả cầu mồi, và cùng lúc phát động một loạt xung điện đồng loạt với tổng điện áp cộng hưởng cực đại!". Bố cục: Tốp mười con chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh đồng loạt phóng những tia sét xanh tím chói lòa vào quả cầu cá nhỏ, mặt nước sủi bọt phát sáng như có sấm sét đánh trúng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L213</summary>

```text
HÌNH L213 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cú phóng điện tập thể mạnh đến nỗi khiến hàng trăm con cá nhỏ bị giật văng bắn tung lên không trung rồi rơi xuống mặt nước bất tỉnh nhân sự, trở thành bữa tiệc thịnh soạn cho cả trăm thành viên trong bầy!". Bố cục: Cá nhỏ bay vọt lên khỏi mặt nước rơi xuống lả tả, cả đàn lươn điện thong thả chia nhau thưởng thức bữa tiệc công bằng hòa thuận; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L214</summary>

```text
HÌNH L214 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyển thủ thứ ba bước vào vòng đấu xã hội không dùng đến vũ khí giật điện hay búng càng, mà chinh phục khán đài bằng tình mẫu tử vĩ đại của đại gia đình: Capybara!". Bố cục: Bức tranh ấm áp của một đại gia đình chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia đông đúc gồm bốn năm con mẹ và hàng chục chú chuột con mũm mĩm đáng yêu đang nằm sưởi nắng bên bờ sông; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L215</summary>

```text
HÌNH L215 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nghiên cứu về hành vi nuôi con hộ alloparenting do các nhà khoa học Brazil thực hiện đã hé lộ một nét văn hóa cộng đồng cực kỳ nhân văn của Bố Già đầm lầy!". Bố cục: Các mẹ chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia nằm cạnh nhau cho một bầy con nhỏ khoảng tám đến mười bé cùng bú sữa một cách vô tư bình đẳng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L216</summary>

```text
HÌNH L216 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong một bầy Capybara, tất cả các con cái thường là chị em họ hàng gần gũi. Khi sinh con vào cùng thời điểm, các bà mẹ sẵn sàng cho bất kỳ đứa trẻ nào trong đàn đến bú sữa mà hoàn toàn không phân biệt đâu là con ruột của mình, đâu là con của hàng xóm!". Bố cục: Một chú chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia con mũm mĩm chạy từ mẹ này sang mẹ kia xin bú sữa và đều được các cô các dì vỗ về liếm lông âu yếm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L217</summary>

```text
HÌNH L217 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thậm chí ngay từ khi mới sinh ra vài ngày tuổi, chuột con đã mở mắt, mọc đủ lông, biết đi lại và bơi lội theo cả đại gia đình, được tất cả các bác các chú trong bầy cùng đứng gác sủa báo động bảo vệ trước báo đốm và trăn gấm!". Bố cục: Những chú chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia con tí hon bơi nối đuôi nhau ngay phía sau lưng đàn bố mẹ lớn, ánh mắt hạnh phúc an toàn tuyệt đối; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L218</summary>

```text
HÌNH L218 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không chịu thua trước các xã hội đoàn kết của Tôm Súng, Lươn Điện hay Capybara, Chim Tu Hú bước lên bục để trình diễn cuộc chạy đua vũ trang tâm lý căng thẳng với chính các chim chủ nhà!". Bố cục: chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái đứng trước tấm bảng chiến thuật đầy mũi tên đối đầu giữa chim ký sinh và chim chủ nhà; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L219</summary>

```text
HÌNH L219 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà điểu học phát hiện rằng: một số loài chim chủ thông minh đã tiến hóa khả năng nhận diện hoa văn trứng lạ tinh tường đến mức tự mình kiểm tra từng quả trứng trong tổ!". Bố cục: Chú chim chích mẹ đeo kính lúp soi xét tỉ mỉ từng chấm đốm trên vỏ trứng trong tổ mình, phát hiện quả trứng có đốm lệch liền hất ra ngoài; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyển thủ số chín! Người vận chuyển hàng tạ nguyên tố Silicon cho các dòng sông lớn tại châu Phi! Hà Mã!". Bố cục: chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ bước ra làm rung chuyển mặt sàn, đeo đai lưng đỏ vô địch, ngoác miệng khoe cặp răng nanh khổng lồ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L220</summary>

```text
HÌNH L220 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vì thế, Chim Tu Hú mẹ phải phát triển bộ nhớ không gian siêu việt để ghi nhớ vị trí và lịch đẻ trứng của hàng chục tổ chim hàng xóm cùng lúc, căn đúng khung giờ chiều vắng mặt để đánh tráo trứng hoàn hảo!". Bố cục: Bản đồ khu rừng trong đầu chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái hiện sáng rực vị trí hàng chục chiếc tổ chim hàng xóm kèm đồng hồ đếm ngược thời gian ra vào của từng nhà; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L221</summary>

```text
HÌNH L221 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ban giám khảo xin công bố kết quả Vòng năm! Huy chương đồng thuộc về Capybara với văn hóa nuôi con tập thể không phân biệt vô cùng nhân văn!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ trao huy chương đồng cho chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia đang âu yếm vỗ về đàn con nhỏ; khán đài thả tim rợp trời.
```
</details>

<details><summary>L222</summary>

```text
HÌNH L222 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Huy chương bạc thuộc về Lươn Điện với chiến thuật săn mồi bầy đàn hơn 100 con! Và Huy chương vàng thuộc về Tôm Súng với xã hội ong kiến 300 tôm lính dưới đáy biển!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ trao huy chương bạc cho chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh và huy chương vàng cho chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa; tiếng hò reo vang dội đấu trường.
```
</details>

<details><summary>L223</summary>

```text
HÌNH L223 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bảng tổng sắp sau Vòng năm thay đổi vị trí dẫn đầu: Tôm Súng vọt lên ngôi đầu với 6 điểm! Lươn Điện và Gấu Trúc Lớn bám sát phía sau với 4 điểm! Cá Cung Thủ, Quỷ Gai, Hà Mã và Capybara đồng 3 điểm!". Bố cục: tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) cập nhật cột điểm cao vút của chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa ở vị trí dẫn đầu; cuộc đua bắt đầu bước vào giai đoạn khốc liệt nhất!
```
</details>

<details><summary>L224</summary>

```text
HÌNH L224 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vòng sáu ngay sau đây sẽ đưa chúng ta bay qua nửa vòng Trái Đất và lặn xuống đáy sông châu Phi trong thử thách Hành trình vĩ đại và định vị không gian!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng giơ cao quả địa cầu phát sáng chuẩn bị cho hành trình phiêu lưu vạn dặm ở Vòng sáu.
```
</details>

<details><summary>L225</summary>

```text
HÌNH L225 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chào mừng toàn thể khán đài bước vào Vòng sáu: Hành trình vĩ đại và siêu giác quan định vị không gian! Ở vòng thi này, ban giám khảo sẽ kiểm tra khả năng vượt không gian và cách các tuyển thủ giao tiếp bằng những giác quan mà con người không hề có!". Bố cục: Sân vận động trình chiếu một quả địa cầu 3D khổng lồ xoay tròn giữa không gian với các đường bay xuyên lục địa và sóng âm dưới đáy sông; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cầm chiếc la bàn vàng.
```
</details>

<details><summary>L226</summary>

```text
HÌNH L226 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Từ bầu trời Bắc Âu băng giá cho tới lòng sông đục ngầu châu Phi, đấu sĩ nào xứng đáng nhận danh hiệu bậc thầy định vị tối thượng?". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ đặt quả địa cầu nhỏ lên bàn, cầm chiếc kính lúp soi vào những tuyến đường di cư chằng chịt khắp hành tinh.
```
</details>

<details><summary>L227</summary>

```text
HÌNH L227 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyển thủ mở màn vòng thi di chuyển khiến tất cả mọi người phải ngước nhìn lên bầu trời: Siêu Trộm Tổ Ấm Chim Tu Hú! Khán giả quen thấy nó loanh quanh bên tổ chim chích, nhưng khả năng bay đường dài của nó mới thực sự là huyền thoại!". Bố cục: chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái đứng trên bục xuất phát, trên lưng gắn một chiếc ba lô phát tín hiệu vệ tinh siêu nhẹ màu bạc lấp lánh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L228</summary>

```text
HÌNH L228 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Năm 2014, nhóm nghiên cứu của nhà điểu học Mikkel Willemoes công bố trên tạp chí PLOS ONE kết quả theo dõi vệ tinh đột phá nhất từng thực hiện trên loài Chim Tu Hú!". Bố cục: Màn hình vệ tinh hiện lên bản đồ châu Âu và châu Phi với những vệt sáng đỏ theo dõi hành trình của tám chú chim Tu Hú gắn chip nặng 5 gam; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L229</summary>

```text
HÌNH L229 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thông thường, những loài chim di cư đi đơn độc ban đêm như Tu Hú được cho là bay tản mát theo hướng ngẫu nhiên. Nhưng dữ liệu vệ tinh từ Đan Mạch và Thụy Điển đã cho thấy một sự thật kinh ngạc!". Bố cục: Quỹ đạo bay của các chú chim chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái hiện lên trên màn hình bản đồ dưới dạng một đường vòng cung khổng lồ cực kỳ đồng nhất; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và tuyển thủ số mười... xin mời quý vị nhìn lên màn hình vì bạn ấy đang bận trồng cây chuối bên ngoài sân vận động!". Bố cục: chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu đang chổng ngược hai chân sau lên thân cây bằng hai tay trước để đánh dấu mùi, mặt tròn xoe ngơ ngác quay lại nhìn ống kính; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L230</summary>

```text
HÌNH L230 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi năm, một chú Chim Tu Hú nhỏ bé nặng khoảng 100g tự mình bay đơn độc vào ban đêm một hành trình khép kín theo chiều kim đồng hồ dài tới 16.000km!". Bố cục: Chú chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái vỗ cánh bay xuyên đêm qua biển Địa Trung Hải, sa mạc Sahara mênh mông để tiến tới những cánh rừng mưa nhiệt đới ở Trung Phi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L231</summary>

```text
HÌNH L231 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Điều khó tin hơn cả: sau khi vượt hơn 5.000km xuyên qua sa mạc Sahara chết chóc để tới vùng Sahel phía Đông, khoảng cách sai lệch giữa những con chim bay riêng lẻ này trung bình chỉ cách nhau đúng 164km!". Bố cục: Mũi tên vệ tinh đo khoảng cách giữa các điểm dừng chân của bầy chim ở vùng Sahel châu Phi cực kỳ sát sao như được lập trình bằng GPS; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L232</summary>

```text
HÌNH L232 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Từ Bắc Âu xuống Đông Nam Âu, sang Trung Phi trú đông, rồi vòng qua Tây Phi bay ngược về châu Âu vào mùa xuân! Một hệ thống định vị GPS sinh học bẩm sinh với sáu trạm dừng chân cố định qua hàng triệu năm không sai một nhịp!". Bố cục: Chuỗi sáu điểm dừng chân phát sáng trên bản đồ từ Đan Mạch xuống Congo rồi vòng qua Tây Phi trở về nhà, cả khán đài vỗ tay vang dội; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L233</summary>

```text
HÌNH L233 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Rời khỏi bầu trời 16.000km, chúng ta lặn sâu xuống lòng sông đục ngầu châu Phi để kiểm tra siêu giác quan dưới nước của cỗ xe tăng 3 tấn: Hà Mã!". Bố cục: chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ bước xuống bể kính sâu trong suốt, đôi tai nhỏ xíu trên đỉnh đầu khép chặt lại, lỗ mũi đóng kín mít như van tàu ngầm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L234</summary>

```text
HÌNH L234 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Câu hỏi đặt ra cho ban giám khảo là: khi lặn hoàn toàn dưới nước tối tăm với đôi tai đã gập kín để ngăn nước vào, làm sao Hà Mã vẫn nghe được âm thanh và xác định chính xác hướng gọi của đồng loại từ dưới đáy sông?". Bố cục: Sơ đồ giải phẫu đầu chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ dưới nước: sóng âm thanh lan truyền trong nước nhanh gấp năm lần trong không khí dội tới chiếc đầu đồ sộ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L235</summary>

```text
HÌNH L235 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nghiên cứu âm học dưới nước của tiến sĩ William Barklow đã giải mã khả năng thính giác lưỡng cư độc nhất vô nhị này: Hà Mã nghe âm thanh dưới nước bằng... xương hàm dưới!". Bố cục: Cận cảnh chiếc xương hàm dưới khổng lồ của chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ: một khối mô mỡ truyền âm đặc biệt nối từ xương hàm chạy thẳng lên hộp sọ tai trong; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L236</summary>

```text
HÌNH L236 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi âm thanh dưới nước truyền tới, rung động đập vào xương hàm dưới, truyền qua dải mô mỡ dẫn âm thẳng vào tai trong bên trái và bên phải, giúp Hà Mã xác định chính xác phương hướng âm thanh giống hệt như người anh em họ xa Cá Heo và Cá Voi!". Bố cục: Các vòng sóng âm dưới nước chạm vào hai bên hàm dưới của chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ rồi truyền tín hiệu sáng rực thẳng vào hai tai trong; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L237</summary>

```text
HÌNH L237 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đặc biệt hơn, Hà Mã còn phát ra các xung âm thanh lưỡng cư đồng thời vào cả không khí phía trên lẫn dòng nước phía dưới! Nhờ cơ chế truyền rung động qua hàm dưới, tiếng gọi bầy đàn trầm đục của nó vang xa hàng cây số xuyên thấu mọi lớp bùn đục!". Bố cục: chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ ngâm một nửa mõm dưới mặt nước phát ra tiếng kêu vang rền làm mặt nước rung lên từng đợt sóng đồng tâm lan tỏa cả hai môi trường; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L238</summary>

```text
HÌNH L238 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và tuyển thủ thứ ba bước vào bài thi định vị không gian sẽ mang lại cho quý vị một màn trình diễn vừa hài hước vừa khôn ngoan: Gấu Trúc Lớn!". Bố cục: chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu đứng trước một hàng cây thông thẳng tắp trong khu vực thi đấu đánh dấu lãnh thổ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L239</summary>

```text
HÌNH L239 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vì sống cô độc giữa rừng tre rậm rạp mênh mông, Gấu Trúc giao tiếp với đồng loại qua những 'bảng tin mùi hương' tiết ra từ tuyến mùi dưới đuôi và nước tiểu quệt lên thân cây!". Bố cục: Một cái cây thông có những vạch đánh dấu phát sáng như bảng tin nhắn mùi hương của cộng đồng gấu trúc trong rừng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ơ... tới lượt em đi vào rồi hả? Đợi em tụt xuống nhặt nốt nhánh trúc đã nha anh MC ơi!". Bố cục: Cận cảnh chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu lộn một vòng rơi bịch xuống đất, ôm cọng tre chạy lạch bạch lên sân khấu đáng yêu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L240</summary>

```text
HÌNH L240 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng ở đây có một quy luật cạnh tranh ngầm cực kỳ khốc liệt: vết mùi càng nằm ở vị trí cao trên thân cây thì chủ nhân của nó càng được coi là to lớn, khỏe mạnh và đáng gờm nhất! Vậy một chú Gấu Trúc đực lùn mũm mĩm phải làm sao?". Bố cục: Hai chú chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu đứng so chiều cao cạnh gốc cây, chú gấu mũm mĩm nhìn ngọn cây cao chót vót mà gãi đầu suy nghĩ mưu mẹo; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L241</summary>

```text
HÌNH L241 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nghiên cứu của tiến sĩ Ron Swaisgood tại vườn thú San Diego và khu bảo tồn Ngọa Long ghi nhận một pha xiếc thú không tưởng: Gấu Trúc đực chống hai tay trước xuống đất, lộn ngược người... trồng cây chuối đẩy hai chân sau bò ngược lên thân cây!". Bố cục: chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu chống hai tay trước vững vàng, vắt ngược hai chân sau lên cao dọc theo thân cây thông một cách siêu dẻo dai như vận động viên thể dục dụng cụ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L242</summary>

```text
HÌNH L242 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ở tư thế trồng cây chuối thẳng đứng đó, chú gấu xịt nước tiểu và bôi mùi hương lên cao chót vót trên thân cây! Một chiêu 'khai gian chiều cao' cực kỳ thông minh khiến các tình địch trẻ tuổi đi ngang qua ngửi thấy liền khiếp sợ bỏ đi không dám gây sự!". Bố cục: Một chú gấu trúc trẻ khác đi ngang qua ngửi thấy vết mùi cao tít trên đầu liền hoảng hốt tưởng đối thủ cao ba mét vội vàng quay đầu chạy mất dép; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L243</summary>

```text
HÌNH L243 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cũng trong bài thi di chuyển không gian, hãy nhìn qua đồng hồ đo quãng đường của hai tuyển thủ sống tại ranh giới nước và cây cối: Con Lười và Cá Cung Thủ!". Bố cục: Màn hình chia đôi: một bên là tán rừng rậm Amazon xanh thẳm, một bên là vùng cửa sông rừng ngập mặn giao thoa nước ngọt và nước mặn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L244</summary>

```text
HÌNH L244 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trên những ngọn cây cao, trung bình mỗi ngày Con Lười chỉ di chuyển được vỏn vẹn khoảng 38m — tức là chưa bằng một nửa chiều dài sân bóng đá!". Bố cục: Thước đo quãng đường hiển thị con số 38 mét màu xanh dịu; chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini thong thả trèo từng bước một qua tán lá rậm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L245</summary>

```text
HÌNH L245 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng điều kỳ diệu là dù sống ở vùng cửa sông nơi độ mặn thay đổi chóng mặt theo thủy triều mỗi ngày, Cá Cung Thủ vẫn điều chỉnh được áp suất thẩm thấu trong máu một cách hoàn hảo để sống khỏe ở cả nước ngọt lẫn nước lợ!". Bố cục: Sơ đồ mang cá chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn: các tế bào chuyên biệt tự động bơm thải muối thừa lúc nước triều dâng và giữ lại muối khoáng khi nước sông ngọt tràn về; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L246</summary>

```text
HÌNH L246 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và đừng quên khả năng tăng tốc tẩu thoát bất ngờ trên cạn của Bố Già Capybara khi phát hiện kẻ săn mồi nguy hiểm tiếp cận bất ngờ!". Bố cục: Một con báo đốm rình rập sau bụi cỏ lao vọt ra tấn công, chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia lập tức chuyển từ chế độ điềm đạm sang chế độ chạy nước rút; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L247</summary>

```text
HÌNH L247 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhờ cấu tạo bốn ngón có màng ở hai chân trước và ba ngón có màng ở hai chân sau, Bố Già đầm lầy phóng mình lao thẳng xuống dòng sông sâu chỉ trong nháy mắt, đồng thời chuyển hẳn đồng hồ sinh học sang kiếm ăn hoàn toàn vào ban đêm khi khu vực có nhiều mối đe dọa rình rập!". Bố cục: chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia tung cú nhảy gọn lẹ xuống lòng sông dưới ánh trăng đêm, bốn chân màng rẽ nước bơi biến mất tăm nhanh chóng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L248</summary>

```text
HÌNH L248 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn anh chàng Tôm Súng dưới rạn san hô lại có một chiến thuật giữ liên lạc đặc biệt: mỗi khi bầy tôm lính búng càng đồng loạt, sóng âm thanh vang xa hàng trăm mét dưới đáy biển để cảnh báo lãnh thổ cho các rạn lân cận!". Bố cục: Sóng âm thanh cộng hưởng từ tổ bọt biển của chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa lan tỏa qua các rạn san hô rực rỡ sắc màu dưới đáy đại dương; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L249</summary>

```text
HÌNH L249 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kết quả Vòng sáu tuyệt vời đã có! Huy chương đồng thuộc về Gấu Trúc Lớn với tuyệt chiêu trồng cây chuối đánh dấu lãnh thổ lừa tình địch!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ trao huy chương đồng cho chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu đang chống hai tay trồng cây chuối ăn mừng khiến cả khán đài cười ồ thích thú.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Rồi, đủ mười thành viên tinh anh! Và theo nghi thức truyền thống của Đại Hội Sinh Tồn, mời cả mười đấu sĩ tiến vào khu vực Lễ Cân Ký Đo Đạc!". Bố cục: Chiếc bàn cân điện tử khổng lồ giữa đấu trường sáng đèn, các nhân viên kỹ thuật đeo găng tay chuẩn bị ghi chép; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cầm micro đứng bên cạnh.
```
</details>

<details><summary>L250</summary>

```text
HÌNH L250 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Huy chương bạc thuộc về Hà Mã với công nghệ nghe âm thanh dưới nước qua xương hàm dưới! Và Huy chương vàng thuộc về Chim Tu Hú với đường bay vệ tinh 16.000km!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ trao huy chương bạc cho chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ và huy chương vàng lấp lánh cho chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái; tiếng vỗ tay vang rền đấu trường.
```
</details>

<details><summary>L251</summary>

```text
HÌNH L251 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bảng điểm sau Vòng sáu trở nên cực kỳ sít sao: Tôm Súng dẫn đầu với 6 điểm! Hà Mã và Gấu Trúc Lớn đồng hạng nhì với 5 điểm! Lươn Điện và Chim Tu Hú bám sát với 4 điểm! Cá Cung Thủ, Quỷ Gai và Capybara đồng 3 điểm! Bọ Pháo Thủ 2 điểm và Con Lười 1 điểm!". Bố cục: tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) sáng rực màn hình với mười cột điểm san sát nhau cực kỳ gay cấn, mọi khoảng cách đều có thể bị san lấp trong nháy mắt!
```
</details>

<details><summary>L252</summary>

```text
HÌNH L252 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bây giờ, trước khi bước vào ba chặng đua nước rút cuối cùng, mời toàn thể quý vị đến với Lễ Trao Giải Phụ: Di sản tiền sử và những họ hàng quái đản nhất!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vung tay biến sàn đấu thành bảo tàng cổ sinh vật học với những bộ xương hóa thạch khổng lồ và ánh đèn tím huyền bí.
```
</details>

<details><summary>L253</summary>

```text
HÌNH L253 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chào mừng toàn thể quý vị khán giả đến với sự kiện đặc biệt giữa hiệp hai của Mùa 2: Bảo Tàng Di Sản Tiến Hóa và Lễ Trao Giải Phụ!". Bố cục: Đấu trường hóa thành bảo tàng lịch sử tự nhiên hoành tráng với các bộ xương hóa thạch phát sáng lung linh; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vest đỏ cầm chiếc đèn pin vàng soi chiếu các kỷ nguyên cổ đại.
```
</details>

<details><summary>L254</summary>

```text
HÌNH L254 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không tính vào điểm vô địch, nhưng lễ trao giải phụ đêm nay sẽ bật mí những bí mật chấn động về cụ tổ tiền sử và những người anh em họ hàng kỳ quái nhất của các tuyển thủ!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ đội chiếc mũ khảo cổ học trên mái tóc giả trắng, cầm chiếc chổi quét bụi hóa thạch và bốn chiếc cúp kỷ niệm bằng đồng thau cổ kính.
```
</details>

<details><summary>L255</summary>

```text
HÌNH L255 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Danh hiệu phụ đầu tiên — Giải thưởng 'Cụ Tổ Khổng Lồ Đáng Sợ Nhất Tiền Sử' — xin được xướng tên họ hàng cổ đại của chú Con Lười bé nhỏ đang ngồi ngủ gật kia!". Bố cục: Màn hình chiếu bức tranh cổ sinh vật học Nam Mỹ thời Kỷ Băng Hà: bóng dáng khổng lồ của một con thú cao sáu mét che rợp cả khu rừng; chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini mở to mắt ngạc nhiên; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L256</summary>

```text
HÌNH L256 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu ngày nay Con Lười chỉ nặng khoảng bốn đến 5kg và treo lơ lửng trên ngọn cây, thì chỉ khoảng 10.000 năm trước, cụ tổ của nó mang tên Lười Đất Khổng Lồ Megatherium là một quái vật ngang ngửa voi ma mút!". Bố cục: So sánh kích thước: chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini hiện đại nhỏ như chú mèo ngồi trên lòng bàn chân khổng lồ của cụ tổ Megatherium đứng thẳng cao sáu mét nặng bốn tấn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L257</summary>

```text
HÌNH L257 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Với chiều cao khi đứng thẳng lên tới 6m và nặng tới 4 tấn, Lười Đất Khổng Lồ sở hữu bộ móng vuốt dài ngang thanh kiếm để đào những đường hầm ngầm khổng lồ xuyên qua lớp đất đá cứng ở Nam Mỹ!". Bố cục: Một đường hầm khổng lồ rộng mấy mét có dấu cào móng vuốt khổng lồ trên vách đá tại Brazil, các nhà khảo cổ học đi bộ bên trong kinh ngạc; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L258</summary>

```text
HÌNH L258 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Những đường hầm cổ đại mang tên Paleoburrows tại Brazil dài hàng trăm mét và cao tới 2m vẫn còn nguyên vẹn vết cào khổng lồ trên vách đá, khiến các nhà địa chất từng lầm tưởng là công trình của người cổ đại!". Bố cục: Nhà địa chất học soi đèn pin lên trần hang động đầy vết cào móng vuốt song song đều tăm tắp rộng hàng mét; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L259</summary>

```text
HÌNH L259 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thậm chí từng tồn tại một nhánh họ hàng mang tên Lười Biển Thalassocnus sống dọc bờ biển Peru, tiến hóa bộ xương nặng trĩu để lặn xuống đáy Thái Bình Dương gặm rong biển hệt như loài bò biển!". Bố cục: Bức tranh phục dựng chú Lười Biển cổ đại bơi lặn dưới đáy đại dương Peru cổ đại gặm thảm cỏ biển xanh mướt; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hà Mã bước lên đầu tiên! Rầm! Mặt sàn rung bần bật! Hơn 3 tấn trọng lượng đè nặng xuống bàn cân thép chịu lực! Tuyển thủ nặng ký nhất giải đấu!". Bố cục: chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ đứng lên cân, chiếc cân lún xuống kêu răng rắc, màn hình điện tử hiện số đỏ chót nhấp nháy; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L260</summary>

```text
HÌNH L260 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một cúp lưu niệm hóa thạch xứng đáng được trao tặng cho dòng họ Lười vĩ đại!". Bố cục: chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini chậm rãi giơ tay nhận chiếc cúp hình xương hóa thạch nhỏ từ tay bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ, nụ cười tự hào rạng rỡ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L261</summary>

```text
HÌNH L261 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Danh hiệu phụ thứ hai — Giải thưởng 'Cuộc Đào Tẩu Hóa Thạch Lâu Đời Nhất' — thuộc về Gấu Trúc Lớn với hóa thạch cụ tổ Ailurarctos 8 triệu năm tuổi tại tỉnh Vân Nam!". Bố cục: Chiếc hộp kính trưng bày hóa thạch xương hàm và ngón tay giả thứ sáu cổ đại tám triệu năm tuổi vừa được khai quật tại Trung Quốc; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L262</summary>

```text
HÌNH L262 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Phát hiện hóa thạch này chứng minh rằng ngay từ 8 triệu năm trước, tổ tiên của Gấu Trúc đã có chiếc xương cổ tay mọc dài ra thành ngón tay giả thứ sáu để cầm nắm thân tre ăn uống!". Bố cục: Bức tranh phục dựng chú gấu trúc cổ đại tám triệu năm trước đang dùng sáu ngón tay kẹp cành trúc ăn ngon lành bên bờ hồ cổ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L263</summary>

```text
HÌNH L263 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Danh hiệu phụ thứ ba — Giải thưởng 'Điệp Viên Nằm Vùng Bất Tử' — khiến cả hội đồng khoa học phải bật cười nghiêng ngả, thuộc về họ hàng nhà Bọ Pháo Thủ mang tên Paussinae!". Bố cục: Kính lúp phóng đại một chú bọ cánh cứng kỳ lạ có đôi râu dẹt hình chiếc lá to bản đang hiên ngang bước thẳng vào cửa hang của một đàn kiến lửa hung dữ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L264</summary>

```text
HÌNH L264 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khác với Bọ Pháo Thủ của chúng ta dùng súng 100°C bắn nhau tóe lửa, nhánh họ hàng Paussinae lại cất súng đi và tiến hóa tuyến tiết ra đúng hợp chất hóa học mùi hương của... Kiến Chúa!". Bố cục: Đàn kiến thợ hung dữ vừa chạy tới định cắn nhưng ngửi thấy mùi thơm giống hệt Kiến Chúa liền cúi rạp đầu cung kính rước chú bọ vào tận sâu bên trong tổ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L265</summary>

```text
HÌNH L265 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chui vào tận phòng ngủ hoàng gia của đàn kiến, chú bọ này sống êm ấm như một vị hoàng đế, được kiến thợ chăm sóc hầu hạ lau chùi, và thỉnh thoảng lén ăn thịt luôn cả ấu trùng kiến con mà đàn kiến không hề hay biết!". Bố cục: Chú bọ nằm phơi bụng trên chiếc ngai vàng giữa tổ kiến, đàn kiến thợ cần mẫn đút mồi và chải râu phục vụ, chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C lắc đầu cười khoái chí; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L266</summary>

```text
HÌNH L266 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và danh hiệu phụ cuối cùng — Giải thưởng 'Dòng Họ Điệp Viên Bí Ẩn Nhất' — dành tặng cho các cô nàng Chim Tu Hú với bí mật di truyền mang tên Gentes!". Bố cục: Sơ đồ nhiễm sắc thể giới tính W của chim cái chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái phát sáng lấp lánh bên cạnh bốn quả trứng mang bốn màu sắc xanh, nâu, đốm và trắng hoàn toàn khác nhau; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L267</summary>

```text
HÌNH L267 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Làm sao một loài chim Tu Hú có thể làm giả trứng giống hệt của hàng chục loài chim chủ khác nhau mà không bị lai tạp màu sắc lẫn lộn?". Bố cục: Hai con chim Tu Hú cái cùng loài bay theo hai hướng khác nhau: một con chỉ đẻ trứng xanh giống chim chích sậy, con kia chỉ đẻ trứng trắng đốm giống chim chích bụi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L268</summary>

```text
HÌNH L268 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà di truyền học giải mã được rằng: bộ gen quy định màu sắc và hoa văn vỏ trứng của Tu Hú nằm trọn trên nhiễm sắc thể W — thứ chỉ truyền thẳng từ chim mẹ sang con gái!". Bố cục: Chuỗi ADN phát sáng trên nhiễm sắc thể W chuyển thẳng công thức phối màu vỏ trứng từ chim mẹ sang chim con gái; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L269</summary>

```text
HÌNH L269 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhờ vậy, trong cùng một loài chia thành hàng chục dòng họ bí mật truyền nghề gia truyền suốt hàng ngàn năm mà không bao giờ bị mất bí kíp!". Bố cục: Cuốn gia phả bí truyền màu sắc vỏ trứng của dòng họ chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái được truyền qua từng thế hệ mẹ con, cả khán đài gật gù thán phục; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tiếp theo là Gấu Trúc Lớn: 110kg cơ bắp và mỡ dự phòng, dù nhìn bề ngoài trông chỉ toàn bông gòn!". Bố cục: chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu ngồi phịch lên bàn cân, ôm chặt bó tre xanh ngơ ngác nhìn con số điện tử nhảy vọt qua mốc một trăm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L270</summary>

```text
HÌNH L270 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và giải thưởng phụ thứ năm — danh hiệu 'Khu Vườn Sinh Thái Di Động Đông Đúc Nhất' — tiếp tục gọi tên Con Lười với hơn 900 con bọ cánh cứng, bướm đêm và hàng triệu vi sinh vật chung sống hòa bình trên cùng một bộ lông!". Bố cục: Kính phóng đại soi vào bộ lông chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini: giống như một thành phố thu nhỏ có cả bọ cánh cứng, bướm đêm, tảo xanh và nấm cùng sinh hoạt nhộn nhịp; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L271</summary>

```text
HÌNH L271 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trên thực tế, mỗi sợi lông thô bên ngoài của Con Lười có các vết nứt siêu nhỏ chạy dọc theo chiều dài, đóng vai trò như những căn hộ chung cư lý tưởng giữ nước mưa để cả hệ sinh thái tí hon cùng phát triển!". Bố cục: Ảnh minh họa khoa học dưới kính lúp phóng đại một sợi rêu xanh và bộ lông chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini với những hốc nhỏ li ti chứa giọt nước mưa trong veo và các cụm vi nấm tí hon đang phát sáng lung linh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L272</summary>

```text
HÌNH L272 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tiếp theo là giải thưởng 'Sinh Con Khắc Nghiệt Nhất Thế Giới Thú' dành cho Gấu Trúc Lớn! Trong khoảng gần một nửa số ca sinh nở, gấu trúc mẹ đẻ ra hai chú gấu con sinh đôi tí hon yếu ớt!". Bố cục: Mẹ chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu nằm ôm hai chú gấu con hồng hào nhỏ xíu vừa chào đời trong hang đá phủ tuyết trắng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L273</summary>

```text
HÌNH L273 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong suốt tuần đầu tiên sau khi sinh, gấu mẹ khổng lồ phải ôm chặt đứa con bé bằng ngón tay cái vào lòng liên tục không rời nửa bước để truyền hơi ấm!". Bố cục: Mẹ chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu nhắm mắt âu yếm ôm ấp gấu con hồng hào trong vòng tay ấm áp giữa mùa đông tuyết trắng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L274</summary>

```text
HÌNH L274 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuy nhiên trong tự nhiên, nguồn sữa ít ỏi từ khẩu phần ăn tre chỉ đủ cho mẹ nuôi đúng một đứa con khỏe mạnh hơn, đồng thời gấu con sinh ra điếc đặc và phải mất tới 45 ngày sau mới mở mắt nhìn thế giới lần đầu tiên!". Bố cục: Chú gấu con bắt đầu mọc lốm đốm lông đen ở tai và mắt sau vài tuần, từ từ mở đôi mắt tròn xoe dễ thương; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L275</summary>

```text
HÌNH L275 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cuối cùng là giải 'Bậc Thầy Hợp Tác Không Cần Ngôn Ngữ' dành cho cặp bạn thân Tôm Súng và Cá Bống! Dù Tôm Súng mắt cực kém, chỉ cần một cái chạm râu nhẹ lên đuôi Cá Bống là cả hai phối hợp tác chiến ăn ý hàng chục năm liền!". Bố cục: chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa và chú cá bống nhỏ bắt tay ăn mừng chiếc cúp tình bạn pha lê, cả khán đài mỉm cười ấm áp; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L276</summary>

```text
HÌNH L276 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tôm Súng cặm cụi dọn dẹp xây sửa căn hầm dưới cát mỗi ngày, còn Cá Bống kiên nhẫn đứng gác cửa và thậm chí chia sẻ luôn cả những mẩu thức ăn thừa cho người bạn thợ xây mù lòa!". Bố cục: Cảnh tượng ấm áp dưới đáy biển: chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa đẩy cát xây hang, cá bống nhỏ bơi canh chừng phía trên bảo vệ bình yên cho ngôi nhà chung; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L277</summary>

```text
HÌNH L277 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Những giải thưởng phụ tuyệt vời đã giúp chúng ta hiểu sâu sắc hơn về cội nguồn của muôn loài! Bây giờ, hãy siết chặt dây an toàn vì trước mắt chúng ta là ba vòng thi quyết định vận mệnh ngôi vương!". Bố cục: Ánh đèn bảo tàng tắt dần, đèn pha đấu trường bật sáng chói lòa trở lại báo hiệu cuộc chiến căng thẳng ở Vòng bảy sắp sửa bắt đầu!
```
</details>

<details><summary>L278</summary>

```text
HÌNH L278 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chào mừng toàn thể khán đài bước vào Vòng bảy: Đấu trường phúc khảo tin đồn và đập tan những hiểu lầm thế kỷ! Trong thế giới tự nhiên, có rất nhiều lời đồn thổi nghe rất lọt tai nhưng thực chất lại sai hoàn toàn về mặt khoa học!". Bố cục: Chiếc kính lúp khổng lồ của ban giám khảo hạ xuống rọi luồng ánh sáng trắng sắc nét xuống giữa sân đấu; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cầm tập hồ sơ có đóng dấu 'PHÚC KHẢO' đứng cạnh bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ.
```
</details>

<details><summary>L279</summary>

```text
HÌNH L279 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ở vòng đấu này, ban giám khảo sẽ đưa ra bốn lời đồn đại phổ biến nhất về các thí sinh, sau đó dùng bằng chứng thực nghiệm để lật tẩy sự thật!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gõ búa gỗ dứt khoát, trước mặt là ba tấm huy chương vàng, bạc, đồng đang chờ trao cho những màn đính chính giá trị nhất.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bố Già Capybara bước lên với phong thái điềm đạm tuyệt đối: 65kg! Chuột gặm nhấm lớn nhất hành tinh hiện nay!". Bố cục: chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia bước lên cân với phong thái quý ông điềm đạm, màn hình hiện số 65kg, anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vỗ vai thán phục; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L280</summary>

```text
HÌNH L280 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lời đồn số một nhắm thẳng vào Thằn Lằn Quỷ Gai: rất nhiều bài viết trên mạng khẳng định loài thằn lằn sa mạc Úc chỉ cần ngồi yên buổi sáng là sương đêm tự động ngưng tụ chảy đầy rãnh da để uống!". Bố cục: Hình ảnh chiếc bình sương buổi sáng gắn dấu hỏi chấm to đùng phía trên đầu chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L281</summary>

```text
HÌNH L281 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Liệu sương sớm có thực sự đủ làm đầy mạng lưới rãnh mao dẫn trên cơ thể Quỷ Gai hay không? Tiến sĩ Philipp Comanns đã tiến hành một thí nghiệm cân đo lạnh lùng trong phòng thí nghiệm!". Bố cục: Tiến sĩ hoạt hình mặc áo blouse trắng đặt chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm vào một căn phòng lạnh 22°C rồi tăng dần độ ẩm không khí lên bão hòa như sương mù sa mạc; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L282</summary>

```text
HÌNH L282 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kết quả cân đo chứng minh lời đồn đó... sai bét! Lượng hơi nước ngưng tụ từ không khí chỉ đủ làm ướt nhẹ bề mặt lớp gai ngoài cùng, hoàn toàn không đủ tạo thành giọt để chảy vào hệ thống rãnh mao dẫn!". Bố cục: Các hạt sương li ti đậu trên đầu gai của chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm rồi bay hơi mất trước khi kịp chạm vào đường dẫn xuống miệng, kim cân không hề nhúc nhích; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L283</summary>

```text
HÌNH L283 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thậm chí khi đứng trên cát có độ ẩm lên tới 22%, lượng nước hút từ cát chỉ làm đầy được 59% các rãnh da!". Bố cục: Màn hình hiển thị 59% rãnh mao dẫn được nạp đầy màu xanh dương khi chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm chỉ đứng yên một chỗ trên cát ẩm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L284</summary>

```text
HÌNH L284 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Để giải khát triệt để giữa sa mạc khô cằn, Quỷ Gai phải chủ động hất cát ẩm phủ lên khắp lưng mình, ép hai mặt da hút lấy từng phân tử nước từ đất! Một phát hiện dập tắt hoàn toàn huyền thoại 'chỉ ngồi chờ sương rơi'!". Bố cục: chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm dùng bốn chân cào lớp cát ẩm tung lên phủ kín lưng mình, hệ thống rãnh da lập tức nạp đầy nước một trăm phần trăm chảy thẳng về họng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L285</summary>

```text
HÌNH L285 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lời đồn số hai gọi tên Nhà Máy Điện Sống: Lươn Điện! Suốt hàng trăm năm, mọi cuốn sách giáo khoa đều dạy rằng Lươn Điện là loài cá săn mồi cô độc tuyệt đối, ghét giao du với đồng loại!". Bố cục: Cuốn sách sinh học cũ hiện dòng chữ 'Săn mồi đơn độc' bị con dấu đỏ đóng đè lên chữ 'SAI SỰ THẬT'; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L286</summary>

```text
HÌNH L286 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng như chúng ta đã chứng kiến ở Vòng năm từ báo cáo tại lưu vực sông Iriri Brazil năm 2021: hơn 100 con Lươn Điện trưởng thành tụ họp và săn mồi tập thể hai lần mỗi ngày!". Bố cục: Cảnh quay thực tế dưới đáy hồ Iriri: hơn 100 con chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh vây kín quả cầu cá nhỏ rồi tung đòn sét đồng loạt như một đội quân đặc nhiệm thực thụ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L287</summary>

```text
HÌNH L287 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Từ 07:30 sáng đến 17:00 chúng nghỉ ngơi yên ả dưới đáy bùn, nhưng cứ đúng bình minh và hoàng hôn là cả trăm con hợp sức tạo thành đội quân săn mồi không đối thủ!". Bố cục: Chiếc đồng hồ chia múi giờ hoạt động của đàn lươn: giờ nghỉ ngơi dưới bùn và giờ tổng tấn công lúc bình minh, hoàng hôn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L288</summary>

```text
HÌNH L288 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lời đồn số ba nhắm vào chú gấu mũm mĩm: Gấu Trúc Lớn! Nhiều người chế giễu rằng Gấu Trúc là một lỗi tiến hóa ngớ ngẩn, dễ bị tuyệt chủng vì lười biếng và vụng về!". Bố cục: Một nhóm khán giả hoạt hình chỉ tay vào chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu đang lăn tròn cười nhạo nhưng bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ giơ tay ra hiệu im lặng xem bằng chứng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L289</summary>

```text
HÌNH L289 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khoa học xin phản biện dứt khoát: Gấu Trúc chẳng hề ngớ ngẩn chút nào! Bộ lông trắng đen của nó được tính toán chính xác để ngụy trang hoàn hảo trước mắt thú ăn thịt trong rừng tuyết!". Bố cục: Hình ảnh chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu hòa lẫn vào rừng trúc phủ tuyết và bóng râm thân cây khiến báo hoa mai đi ngang qua không thể phát hiện; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lươn Điện dài 2m nặng 20kg trườn lên bàn cân thủy tinh; kế bên là Con Lười nặng 4kg nhưng 1/3 trọng lượng nằm ở bụng lá cây chưa tiêu hóa!". Bố cục: Hai chiếc cân nhỏ hơn: chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh uốn mình trong bể cân 20kg, chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini treo ngược vào khung cân chớp mắt lờ đờ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L290</summary>

```text
HÌNH L290 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ngoài ra, đột biến gen DUOX2 giúp nó sống khỏe bằng nguồn thức ăn ít ai thèm tranh giành, và nó còn biết dùng hợp chất phân ngựa làm thuốc giảm cảm giác lạnh mùa đông!". Bố cục: Bức tranh ghép bốn năng lực ẩn giấu của chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu: áo ngụy trang tàng hình, gen tiết kiệm năng lượng, ngón tay thứ sáu và liệu pháp chống rét; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L291</summary>

```text
HÌNH L291 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu không bị con người thu hẹp rừng tre, Gấu Trúc hoàn toàn dư sức ngự trị vùng núi Tứ Xuyên thêm hàng triệu năm nữa!". Bố cục: chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu mỉm cười vỗ ngực đầy tự hào giữa cánh rừng tre xanh ngát, cả khán đài đồng loạt vỗ tay xin lỗi chú gấu dễ thương; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L292</summary>

```text
HÌNH L292 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và lời đồn số bốn nhắm vào Bọ Pháo Thủ: Nhiều người thắc mắc tại sao phản ứng sinh nhiệt 100°C lại không làm Bọ Pháo Thủ tự thiêu rụi bụng mình ngay từ phát bắn đầu tiên?". Bố cục: Hình ảnh minh họa hài hước: một chú bọ giả tưởng bị phình bụng bốc cháy nổ tung như quả bóng bay; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L293</summary>

```text
HÌNH L293 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà hóa học hữu cơ giải mã bí mật cực kỳ tinh vi: hai hóa chất hydroquinone và oxy già được chứa tách biệt hoàn toàn trong một túi dự trữ an toàn không hề có chất xúc tác!". Bố cục: Sơ đồ hai buồng tách biệt: túi chứa nguyên liệu nguội lạnh nằm yên bình, cách ly hoàn toàn bởi một van cơ học đóng chặt như cửa két sắt ngân hàng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L294</summary>

```text
HÌNH L294 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Phản ứng chỉ xảy ra bên trong buồng phản ứng bọc vỏ chitin cứng như gốm chịu nhiệt trong khoảnh khắc vài phần nghìn giây ngay trước khi bị tống thẳng ra ngoài! Nhờ đó chú bọ luôn an toàn tuyệt đối!". Bố cục: Buồng phản ứng lót lớp vỏ chitin siêu bền chịu nhiệt phun xả áp lực ra ngoài chỉ trong tích tắc mà thân bọ hoàn toàn mát lạnh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L295</summary>

```text
HÌNH L295 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lời đồn số năm nhắm vào Bố Già Capybara: trên mạng xã hội, nhiều người tin rằng Capybara hiền lành tuyệt đối đến mức không bao giờ cắn bất kỳ ai dù bị chọc ghẹo ra sao!". Bố cục: Hình minh họa một chú Capybara đội vòng hoa thiên thần hiền từ bên cạnh dấu hỏi chấm cảnh báo màu đỏ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L296</summary>

```text
HÌNH L296 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sự thật đính chính: dù tính tình cực kỳ điềm đạm, nhưng khi bị dồn ép vào góc tường hoặc khi bảo vệ đàn con nhỏ, cặp răng cửa sắc như dao đục của Capybara có thể tung ra cú cắn chí mạng rách toạc thịt kẻ xâm phạm!". Bố cục: chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia nhe cặp răng cửa dài sắc bén gầm gừ cảnh báo khi có kẻ lạ mặt tiến sát đàn con nhỏ, lập tức khiến chó săn giật mình lùi bước; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L297</summary>

```text
HÌNH L297 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và lời đồn số sáu gọi tên Cá Cung Thủ: nhiều khán giả lầm tưởng loài cá này sống hoàn toàn bằng việc bắn rơi côn trùng đậu trên lá cây!". Bố cục: Bức tranh chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn chỉ nhìn chằm chằm lên ngọn cây phía trên mà bỏ qua mọi con cá con bơi ngang trước mũi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L298</summary>

```text
HÌNH L298 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thực tế nghiên cứu dạ dày cho thấy: phần lớn khẩu phần ăn hàng ngày của Cá Cung Thủ là tôm tép, giáp xác và cá con bơi ngay dưới mặt nước! Kỹ năng bắn tia nước hạ côn trùng là tuyệt chiêu săn mồi bổ sung khi thức ăn dưới nước trở nên khan hiếm!". Bố cục: Biểu đồ thực đơn của chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn: 80% mồi là động vật thủy sinh dưới nước, 20% còn lại là côn trùng bắn hạ từ trên không; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L299</summary>

```text
HÌNH L299 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và lời đồn cuối cùng trong vòng phúc khảo nhắm vào Chim Tu Hú: nhiều khán giả cứ nghe thấy tên họ nhà Tu Hú là mặc định rằng 100% các loài chim tu hú trên Trái Đất đều đi đẻ nhờ và hất trứng hàng xóm!". Bố cục: Hình minh họa cả gia tộc chim Tu Hú đều bị dán nhãn 'Kẻ lười biếng đẻ nhờ' trên tấm bảng gỗ lớn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhóm hạng lông tiếp tục lên sàn: Chim Tu Hú nặng chỉ 110g, Thằn Lằn Quỷ Gai vỏn vẹn 40g, và Cá Cung Thủ 200g!". Bố cục: Ba tuyển thủ đứng trên đĩa cân điện tử chính xác cao: chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái, chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm và chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn nhìn nhau đầy thách thức; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L300</summary>

```text
HÌNH L300 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sự thật minh oan từ cuốn chuyên khảo nổi tiếng của Đại học Oxford: trong số khoảng 140 loài thuộc họ Cu cu trên toàn thế giới, thực chất chỉ có khoảng 59 loài sống ký sinh đẻ nhờ!". Bố cục: Biểu đồ phân tách họ nhà Tu Hú: phần lớn gồm hơn tám mươi loài mang nhãn xanh 'Tự xây tổ nuôi con đàng hoàng'; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L301</summary>

```text
HÌNH L301 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hơn một nửa gia tộc họ hàng của Tu Hú — với hơn 80 loài khác nhau — vẫn tự mình chăm chỉ tha rơm xây tổ, tự ấp trứng và mớm mồi nuôi con khôn lớn như những ông bố bà mẹ mẫu mực nhất!". Bố cục: Một chú chim cu cườm họ hàng nhà chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái đội mũ bảo hộ chăm chỉ xây tổ ấm cho con, chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái đứng bên cạnh gật gù bênh vực danh dự dòng họ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L302</summary>

```text
HÌNH L302 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kết quả Vòng bảy phúc khảo tin đồn: Huy chương vàng thuộc về Thằn Lằn Quỷ Gai với thí nghiệm lật tẩy huyền thoại uống sương đêm!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ trao huy chương vàng cho chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm đứng giơ cao nắm đấm ăn mừng; tiếng vỗ tay tán thưởng vang dậy khắp khán đài.
```
</details>

<details><summary>L303</summary>

```text
HÌNH L303 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bảng điểm sau Vòng bảy trở nên căng thẳng đến nghẹt thở: Ba tuyển thủ đồng dẫn đầu với 6 điểm là Tôm Súng, Lươn Điện và Thằn Lằn Quỷ Gai!". Bố cục: tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) hiện lên với nhóm dẫn đầu sáu điểm san sát nhau; bầu không khí trường quay nóng hơn bao giờ hết!
```
</details>

<details><summary>L304</summary>

```text
HÌNH L304 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trước mắt chúng ta chỉ còn Vòng Bán Kết và Vòng Chung Kết điểm nhân đôi! Ai sẽ bứt tốc vào phút chót? Xin mời theo dõi ngay sau đây!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vung micro chỉ về phía khu vực thử nghiệm Bán Kết rực sáng ánh đèn xanh đầy kịch tính.
```
</details>

<details><summary>L305</summary>

```text
HÌNH L305 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chào mừng toàn thể quý vị khán đài bước vào Vòng Bán Kết sinh tử của Đại Hội Sinh Tồn Mùa 2! Chỉ còn một bước chân nữa thôi là chúng ta sẽ bước vào Vòng Chung Kết nhân đôi điểm số!". Bố cục: Đấu trường Bán Kết sáng rực với máy gia tốc tia X đồng bộ cỡ lớn, kính hiển vi phân tách thuốc sinh học và đường đua phản xạ thị giác; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đứng giữa bục dẫn chương trình.
```
</details>

<details><summary>L306</summary>

```text
HÌNH L306 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và đúng như tinh thần của giải đấu, Vòng Bán Kết sẽ chứng kiến những công nghệ nghiên cứu tối tân nhất thế kỷ 21 được chiếu trực tiếp lên sàn đấu!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ ngồi chỉnh kính trên bục giám khảo, trước mặt là ba chiếc huy chương Bán Kết sáng lấp lánh dưới ánh đèn pha.
```
</details>

<details><summary>L307</summary>

```text
HÌNH L307 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đấu sĩ mở màn Bán Kết là chú bọ tí hon từng bị đánh giá thấp nhất lúc khai mạc: Bọ Pháo Thủ! Lần này chúng ta không nhìn từ bên ngoài mà nhìn xuyên thấu vào bên trong bụng chú bọ khi nó đang nhả đạn!". Bố cục: chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C tiến vào buồng chụp tia X đồng bộ khổng lồ, ánh sáng X-ray chuẩn bị quét qua phần bụng của chú bọ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L308</summary>

```text
HÌNH L308 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Năm 2015, một nhóm khoa học gia tại Viện Công Nghệ Massachusetts MIT và Đại học Arizona đã thực hiện một kỳ tích chưa từng có: đưa Bọ Pháo Thủ vào máy gia tốc hạt synchrotron quay phim tia X tốc độ 2.000 fps mỗi giây!". Bố cục: Màn hình tia X trực tiếp hiển thị khung xương và các buồng nội tạng bên trong bụng chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C với độ sắc nét từng mi-crô-mét; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L309</summary>

```text
HÌNH L309 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đoạn phim tia X đã vén bức màn bí mật về cơ chế van tự động thiên tài bên trong cơ thể dài chưa đầy 2cm này!". Bố cục: Hình ảnh quay chậm tia X: khi hai hóa chất trộn vào buồng phản ứng, áp suất nổ bùng lên đẩy van đầu vào tự động đóng sập lại ngay lập tức! :: Mũi tên áp suất nổ bên trong buồng phản ứng ép chặt cánh van ngăn không cho hỗn hợp sôi trào ngược vào túi dự trữ an toàn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cuối cùng là hai gã tí hon Tôm Súng và Bọ Pháo Thủ! Cân thông thường không thể đo nổi, ban tổ chức phải dùng cân phân tích hóa học trong lồng kính kín gió!". Bố cục: Nhân viên đặt chiếc đĩa siêu nhỏ vào lồng kính thí nghiệm nơi chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C dài chưa tới hai phân và chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa dài 4cm đang đứng nghiêm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L310</summary>

```text
HÌNH L310 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ngay khi tia hơi nóng được tống ra ngoài qua nòng pháo, áp suất trong buồng phản ứng tụt xuống, cánh van lại tự động bật mở cho một giọt nhiên liệu mới chảy xuống!". Bố cục: Van mở ra nhỏ giọt rồi đóng sập, nổ bùm, mở ra, đóng sập lặp đi lặp lại với tốc độ năm trăm đến một ngàn lần trong một giây! [surprise-oh] :: Toàn bộ chu trình đóng mở van cơ học tự động hoàn toàn nhờ áp suất nổ lặp đi lặp lại nhịp nhàng như động cơ xung phản lực của tên lửa V1! KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L311</summary>

```text
HÌNH L311 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đây chính là cơ chế tự điều áp bằng chính vụ nổ của mình mà không cần tiêu tốn năng lượng não bộ để điều khiển từng phát bắn! Một cỗ máy cơ khí sinh học hoàn mỹ tuyệt đối!". Bố cục: Cả khán đài và đội ngũ kỹ sư cơ khí đứng bật dậy vỗ tay tán thưởng cho chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C đang giơ càng chào khiêm tốn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L312</summary>

```text
HÌNH L312 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyển thủ thứ hai bước lên sàn Bán Kết khiến cả hội trường phải lặng người vì ngạc nhiên: Thánh sống chậm Con Lười! Kẻ đang đứng cuối bảng tổng sắp với chỉ 1 điểm duy nhất!". Bố cục: chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini từ từ trườn ra giữa sân khấu, trên bộ lông rêu xanh của chú là hàng chục ống nghiệm phòng thí nghiệm đang tỏa ánh sáng lung linh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L313</summary>

```text
HÌNH L313 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhiều người nghĩ Con Lười chẳng làm được gì ngoài việc treo ngược ngủ gật. Nhưng năm 2014, tiến sĩ Sarah Higginbotham tại Viện Nghiên cứu Nhiệt đới Smithsonian đã phát hiện một kho báu y học nằm ngay trên bộ lông thô ráp của nó!". Bố cục: Bức ảnh tiến sĩ hoạt hình thu thập cẩn thận vài sợi lông lưng của chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini tại Vườn quốc gia Soberanía nước Panama đưa vào ống nghiệm bảo quản; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L314</summary>

```text
HÌNH L314 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Từ mẫu lông của chỉ 9 chú Con Lười ba ngón hoang dã, các nhà khoa học đã phân lập nuôi cấy thành công tới 84 chủng nấm độc đáo thuộc ngành nấm túi, trong đó có những loài chưa từng được nhân loại biết tới!". Bố cục: Tám mươi bốn đĩa thạch nuôi cấy nấm phát sáng đa sắc màu xếp thành ma trận khổng lồ trên màn hình phòng thí nghiệm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L315</summary>

```text
HÌNH L315 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và khi đưa chiết xuất từ những chủng nấm lông lười này đi thử nghiệm sinh học, kết quả thu được làm rung chuyển cả ngành dược học thế giới!". Bố cục: Các giọt chiết xuất nấm lông lười nhỏ xuống các đĩa chứa mầm bệnh nguy hiểm nhất của loài người trong kính hiển vi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L316</summary>

```text
HÌNH L316 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "74 chủng nấm được chiết xuất thử nghiệm: 20,6% số mẫu đã tiêu diệt và ức chế cực mạnh tế bào ung thư vú MCF-7 ở người!". Bố cục: Hình ảnh các tế bào ung thư vú MCF-7 bị các phân tử hoạt chất nấm từ lông chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini tấn công tan rã nhanh chóng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L317</summary>

```text
HÌNH L317 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa hết, nhiều chủng nấm khác trên lông Con Lười còn tỏ ra cực kỳ hiệu quả trong việc tiêu diệt ký sinh trùng gây bệnh sốt rét ác tính Plasmodium falciparum, bệnh Chagas nhiệt đới và 20 chủng nấm có khả năng kháng vi khuẩn gây bệnh kháng thuốc!". Bố cục: Bốn loại vi khuẩn và ký sinh trùng nguy hiểm đều bị quét sạch bởi các hoạt chất trích xuất từ vườn nấm di động trên lưng chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L318</summary>

```text
HÌNH L318 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một hiệu thuốc di động sống treo lơ lửng trên ngọn cây rừng nhiệt đới! Ai dám bảo Thánh sống chậm là vô dụng nào?". Bố cục: chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini đeo chiếc áo blouse bác sĩ mini mỉm cười hiền hậu, khán giả trên khán đài đồng loạt cúi đầu nể phục; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L319</summary>

```text
HÌNH L319 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyển thủ thứ ba mang đến bài thi cuối cùng của Bán Kết: Cá Cung Thủ! Bên cạnh trí tuệ nhớ 44 khuôn mặt người, nghiên cứu của Wöhl và Schuster còn giải mã tốc độ phản xạ thần tốc của loài cá này!". Bố cục: chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn bơi sát mặt nước bể thử nghiệm với hàng chục cảm biến điện sinh học đo tốc độ phản xạ não bộ đang hoạt động liên tục; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bọ Pháo Thủ chỉ nặng chưa đầy nửa gam! Tức là Hà Mã nặng gấp... 6.000.000 lần Bọ Pháo Thủ! Sự chênh lệch này khiến máy tính của ban tổ chức suýt bốc khói!". Bố cục: Bảng so sánh hoạt hình: một bên là chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ to như ngọn núi, một bên là chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C nhỏ như đầu bút bi; nhân viên kỹ thuật ôm đầu kinh ngạc; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L320</summary>

```text
HÌNH L320 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ngay khi con mồi trên cành vừa bị bắn rơi và chạm mặt nước hoặc rơi tự do trong không trung, bộ não cá chỉ mất vỏn vẹn 40ms để tính toán lại toàn bộ góc quay cơ thể!". Bố cục: Bộ não chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn phát tia xung thần kinh trong 40 mili-giây, điều khiển vây đuôi quay phắt thân cá hướng thẳng về điểm mồi sắp rơi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L321</summary>

```text
HÌNH L321 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hơn nữa, mắt của Cá Cung Thủ tiến hóa hai vùng võng mạc chuyên biệt: vùng dưới nhìn sắc nét dưới nước tối và vùng trên chuyên nhìn xuyên qua mặt nước để phóng đại hình ảnh côn trùng giữa không trung!". Bố cục: Sơ đồ giải phẫu mắt kép sinh học của chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn: hai luồng ánh sáng trên không và dưới nước hội tụ chính xác trên hai vùng võng mạc riêng biệt; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L322</summary>

```text
HÌNH L322 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không chỉ dừng lại ở đó, ban giám khảo còn kiểm tra khả năng chịu đựng và duy trì nòi giống trong điều kiện khắc nghiệt của Hà Mã và Thằn Lằn Quỷ Gai!". Bố cục: Sân đấu Bán Kết bật đèn chiếu sáng hai khu vực mô phỏng lòng sông thiếu oxy và tầng cát sâu nóng bức; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L323</summary>

```text
HÌNH L323 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong cơ bắp đồ sộ của Hà Mã chứa mật độ myoglobin dự trữ oxy cực cao tương tự các loài cá voi đại dương! Nhờ kho oxy dự trữ trong từng thớ thịt đó, nó dễ dàng chạy bộ phi nước đại dưới đáy sông suốt 5 phút mà không hề mỏi cơ!". Bố cục: Phóng đại thớ cơ đỏ thẫm của chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ chứa đầy các phân tử myoglobin tích trữ oxy giúp vận động bền bỉ dưới đáy nước sâu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L324</summary>

```text
HÌNH L324 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn Thằn Lằn Quỷ Gai mái đến mùa sinh sản lại tự mình đào một đường hầm sâu tới 30cm dưới cát cứng sa mạc, đẻ từ ba đến mười quả trứng rồi lấp kín xóa sạch mọi dấu vết!". Bố cục: Sơ đồ hang ngầm dưới cát đỏ sa mạc Úc: chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm mẹ cẩn thận dùng chân sau gạt cát phẳng lì che giấu ổ trứng ở độ sâu 30cm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L325</summary>

```text
HÌNH L325 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khoảng 3-4 tháng sau, những chú quỷ gai con nở ra từ dưới lòng đất, tự mình đội cát chui lên với bộ giáp gai mini sắc nhọn sẵn sàng chiến đấu ngay từ ngày đầu tiên!". Bố cục: Những chú chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm con tí hon đội cát ngoi lên mặt đất giữa ánh nắng sa mạc, đôi mắt tinh anh đầy bản lĩnh sinh tồn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L326</summary>

```text
HÌNH L326 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn Bố Già Capybara thì sao? Để bảo toàn mạng sống trong mùa khô khắc nghiệt khi đầm lầy cạn kiệt, hàng trăm cá thể tụ họp thành đại liên minh rộng lớn cùng canh gác cho nhau trước móng vuốt báo đốm Jaguar!". Bố cục: Bức tranh cả một đàn lớn hơn năm mươi chú chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia quây quần bên vũng nước còn sót lại giữa mùa khô, thay phiên nhau đứng gác bảo vệ bầy con; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L327</summary>

```text
HÌNH L327 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kết quả Vòng Bán Kết lịch sử đã có! Huy chương đồng thuộc về Cá Cung Thủ với phản xạ 40ms và cấu trúc mắt kép nhìn xuyên mặt nước!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ trao huy chương đồng cho chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn đang giơ vây vẫy chào khán giả; tiếng vỗ tay vang dội.
```
</details>

<details><summary>L328</summary>

```text
HÌNH L328 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Huy chương bạc thuộc về Con Lười với vườn nấm 84 chủng diệt sốt rét và tế bào ung thư! Và Huy chương vàng thuộc về Bọ Pháo Thủ với phát hiện tia X đồng bộ van nổ tự điều áp!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ trao huy chương bạc cho chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini và huy chương vàng cho chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C; pháo hoa nổ rực trời đấu trường.
```
</details>

<details><summary>L329</summary>

```text
HÌNH L329 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy nhìn lên Bảng Tổng Sắp ngay trước giờ bước vào Vòng Chung Kết! Cuộc đua kịch tính chưa từng thấy trong lịch sử: Bốn tuyển thủ đồng hạng nhất với 6 điểm là Tôm Súng, Lươn Điện, Thằn Lằn Quỷ Gai và Bọ Pháo Thủ!". Bố cục: tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) rực sáng bốn cột điểm cao bằng nhau ở mốc sáu điểm tạo thành thế trận tứ mã tranh ngôi vương nghẹt thở!
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sau lễ cân ký, giới cá cược và chuyên gia phân tích đồng loạt đặt cửa vô địch cho ba gã khổng lồ hỏa lực: Tôm Súng, Lươn Điện và Hà Mã!". Bố cục: Màn hình chiếu cột dự đoán: ba cột cao vút gắn hình đầu chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa, chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh, chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ phát sáng rực rỡ trên bục ứng cử viên; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L330</summary>

```text
HÌNH L330 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gấu Trúc Lớn và Hà Mã bám ngay phía sau với 5 điểm! Chim Tu Hú và Cá Cung Thủ 4 điểm! Capybara và Con Lười 3 điểm!". Bố cục: Cả mười cột điểm đều sát nút nhau đến mức bất kỳ ai giành vàng Chung Kết nhân đôi sáu điểm đều có cơ hội bước lên đỉnh vinh quang!
```
</details>

<details><summary>L331</summary>

```text
HÌNH L331 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thời khắc quyết định vận mệnh Mùa 2 đã điểm! Xin mời toàn thể khán đài tiến vào Vòng Chung Kết: Món Quà Cho Nhân Loại!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vung micro vàng hô vang, ánh đèn sân khấu hội tụ toàn bộ vào bục vinh quang nơi chiếc vương miện đang chờ chủ nhân.
```
</details>

<details><summary>L332</summary>

```text
HÌNH L332 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giờ phút thiêng liêng nhất của Đại Hội Sinh Tồn Mùa 2 đã đến: Vòng Chung Kết Tối Thượng! Như đã công bố từ đầu giải, mọi huy chương tại vòng chung kết này sẽ được nhân đôi điểm số!". Bố cục: Cả sân vận động bùng nổ trong ánh sáng vàng kim lộng lẫy, biểu tượng 'ĐIỂM NHÂN ĐÔI' xoay tròn phát sáng rực rỡ trên màn hình lớn; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vest đỏ giơ hai tay đón chào khoảnh khắc lịch sử.
```
</details>

<details><summary>L333</summary>

```text
HÌNH L333 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Huy chương vàng trị giá 6 điểm! Huy chương bạc 4 điểm! Và huy chương đồng 2 điểm! Với bốn ứng cử viên đang hòa nhau ở mốc 6 điểm và sáu ứng cử viên bám sát ngay phía sau, bất kỳ điều điên rồ nào cũng có thể xảy ra!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ nâng chiếc vương miện nạm ngọc vàng lấp lánh trên tay, đặt trang trọng bên cạnh chiếc cúp vô địch sáng chói giữa sân đấu.
```
</details>

<details><summary>L334</summary>

```text
HÌNH L334 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chủ đề thi đấu cao quý nhất của đêm chung kết là: Món Quà Cho Nhân Loại! Khoa học và kỹ thuật loài người đã học hỏi được những công nghệ thay đổi thế giới nào từ mười quái kiệt này?". Bố cục: Màn hình lớn trình chiếu các hình ảnh tương lai: phi thuyền vũ trụ, trạm thu nước sa mạc, thiết bị cấy ghép tim nhân tạo và phòng bào chế thuốc cứu người; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L335</summary>

```text
HÌNH L335 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ứng cử viên mở màn Chung Kết là Tôm Súng! Ngoài khả năng tạo plasma dưới nước hiệu suất cao gấp 10 lần máy laser tại Đại học Texas A&M, sóng xung kích cavitation của nó còn đang được nghiên cứu ứng dụng trong xử lý nước thải và khoan đá ngầm không gây ô nhiễm!". Bố cục: Mô hình chiếc càng chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa in 3D tạo ra chùm tia plasma khử trùng sạch bóng hàng triệu vi khuẩn trong bể nước ô nhiễm chỉ trong tích tắc; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L336</summary>

```text
HÌNH L336 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bằng cách hội tụ năng lượng cơ học vào 1 điểm sụp đổ bong bóng khí siêu nhỏ, các kỹ sư có thể tạo ra phản ứng hóa học nhiệt độ cao để phân hủy chất độc công nghiệp dưới nước mà không cần hóa chất tẩy rửa độc hại!". Bố cục: Dòng nước thải đục ngầu đi qua buồng phóng cavitation mô phỏng chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa biến ngay thành dòng nước tinh khiết trong vắt; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L337</summary>

```text
HÌNH L337 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ứng cử viên thứ hai bước lên bục trình diễn công nghệ là Thằn Lằn Quỷ Gai! Dựa trên thí nghiệm cân đo rãnh da năm 2016 và nghiên cứu tổng hợp năm 2017 của tiến sĩ Philipp Comanns, các kỹ sư vật liệu đã phát minh ra tấm màng thu ẩm sa mạc thụ động!". Bố cục: Tấm vật liệu mô phỏng mạng lưới rãnh mao dẫn bất đối xứng trên da chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm được căng rộng trên các cồn cát sa mạc khô hạn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L338</summary>

```text
HÌNH L338 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lấy cảm hứng từ cấu trúc rãnh hình nêm dẫn nước một chiều chống bay hơi của chú thằn lằn sa mạc Úc, những tấm màng kim loại khắc laser vi mô này có khả năng hút ẩm từ sương đêm và đất ẩm dẫn về bể chứa mà không tốn một Oát điện năng nào!". Bố cục: Những giọt hơi ẩm nhỏ li ti tự động gom tụ chảy thành dòng nước tinh khiết vào bình chứa giúp người dân vùng khô hạn giải khát; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L339</summary>

```text
HÌNH L339 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ứng cử viên thứ ba: Lươn Điện! Một phát minh công nghệ y sinh từng lên trang bìa tạp chí Nature cuối năm 2017 của giáo sư Michael Mayer và tiến sĩ Thomas Schroeder!". Bố cục: Trang tạp chí Nature giới thiệu mô hình 'Cơ quan phát điện mềm nhân tạo' lấy cảm hứng từ tế bào electrocyte của chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn Bọ Pháo Thủ nửa gam và Con Lười chậm chạp? Các chuyên gia ghi một dòng ngắn gọn: chỉ mong hai bạn đi hết được vòng gửi xe!". Bố cục: Các cột dự đoán thấp lè tè gắn hình chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C và chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini, chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C cau mày giơ nắm đấm đầy quyết tâm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L340</summary>

```text
HÌNH L340 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thay vì dùng pin kim loại cứng chứa hóa chất độc hại có nguy cơ rò rỉ trong cơ thể bệnh nhân, nhóm nghiên cứu đã xếp hàng ngàn giọt gel nước hydrogel chứa muối ion xen kẽ qua màng chọn lọc!". Bố cục: Sơ đồ tấm màng hydrogel mềm dẻo trong suốt xếp lớp theo kiểu gấp giấy origami của Nhật Bản, phát ra dòng điện sinh học ổn định 110V khi ấn nhẹ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L341</summary>

```text
HÌNH L341 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi tiếp xúc đồng thời, hàng ngàn ngăn gel mềm tạo ra hiệu điện thế lên tới 110V hoàn toàn tương thích sinh học với cơ thể người! Mở ra kỷ nguyên cung cấp năng lượng vĩnh cửu cho máy tạo nhịp tim, kính áp tròng thông minh và robot mềm y tế!". Bố cục: Chiếc máy tạo nhịp tim gắn màng pin mềm hydrogel đập nhịp nhàng trong lồng ngực bệnh nhân mà không bao giờ cần mổ thay pin nữa; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L342</summary>

```text
HÌNH L342 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ứng cử viên thứ tư khiến cả khán đài xúc động nghẹn ngào: Thánh sống chậm Con Lười! Kẻ bị chế giễu suốt từ đầu giải đấu lại đang nắm giữ chìa khóa cứu sống hàng triệu bệnh nhân!". Bố cục: chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini bước ra giữa ánh sáng ấm áp, bên cạnh là hình ảnh phòng thí nghiệm dược phẩm quốc tế đang nghiên cứu các chủng nấm quý từ lông lười; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L343</summary>

```text
HÌNH L343 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hơn 20% số chủng nấm phân lập từ bộ lông rêu xanh của Con Lười có khả năng tiêu diệt tế bào ung thư vú MCF-7, bên cạnh những hoạt chất cực mạnh chống lại ký sinh trùng sốt rét và vi khuẩn kháng kháng sinh đang đe dọa nhân loại!". Bố cục: Những viên thuốc kháng sinh và thuốc đặc trị ung thư thế hệ mới tỏa sáng từ chiết xuất vườn nấm sinh thái trên bộ lông của chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L344</summary>

```text
HÌNH L344 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một loài vật đi chậm nhất hành tinh nhưng lại đi trước ngành dược học hiện đại cả một bước tiến dài!". Bố cục: Cả hội trường đứng dậy vỗ tay vang dội dành tặng sự trân trọng lớn lao cho chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini, chú lười mỉm cười rưng rưng xúc động; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L345</summary>

```text
HÌNH L345 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và ứng cử viên cuối cùng bước lên sân khấu Chung Kết là pháo thủ tí hon nửa gam: Bọ Pháo Thủ! Công trình khoa học của giáo sư Andy McIntosh tại Đại học Leeds nước Anh đã làm thay đổi ngành công nghệ phun đốt toàn cầu!". Bố cục: Giáo sư kỹ thuật hoạt hình đặt mô hình buồng đốt của chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C lên bục trình diễn, bên cạnh là chiếc bằng sáng chế Mỹ cấp năm 2015 cho công nghệ phun sương vi mô; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L346</summary>

```text
HÌNH L346 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Công nghệ phun sương chớp nhoáng mang thương hiệu µMist mô phỏng chính xác van cơ học buồng phản ứng của Bọ Pháo Thủ: không cần máy bơm áp suất cao cồng kềnh hay khí nén độc hại, chỉ dùng nhiệt năng nhỏ tạo vụ nổ hơi giãn nở!". Bố cục: Mô hình động cơ phản lực và ống hít y tế sử dụng đầu phun vi mô từ công nghệ Bọ Pháo Thủ phun ra màn sương hạt siêu mịn đồng đều tuyệt đối; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L347</summary>

```text
HÌNH L347 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Công nghệ này giúp tăng hiệu suất đốt cháy nhiên liệu của động cơ tên lửa và tua-bin khí, tạo ra các ống hít thuốc hen suyễn chính xác tới từng mi-crô-mét, và đặc biệt là chế tạo ra súng chữa cháy rừng thế hệ mới!". Bố cục: Một lính cứu hỏa đeo ba lô chữa cháy mini dài chỉ 5cm nhưng phun tia sương nước áp suất cao bắn xa tới 10 mét dập tắt đám cháy rừng rực lửa ngay tức khắc! KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L348</summary>

```text
HÌNH L348 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chỉ từ một buồng nén nhỏ dài 5cm, thiết bị mô phỏng Bọ Pháo Thủ bắn luồng sương dập lửa xa tới 10m với lượng nước tiết kiệm gấp nhiều lần! Một phát minh cứu rừng và cứu người vô cùng vĩ đại!". Bố cục: Ngọn lửa cháy rừng bị dập tắt sạch sẽ trong chớp mắt, hàng ngàn loài thú rừng an toàn reo hò ăn mừng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L349</summary>

```text
HÌNH L349 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và trước khi trao giải, ban giám khảo còn tôn vinh hai món quà y học đầy bất ngờ từ hai chú gấu và hà mã!". Bố cục: Màn hình lớn hiển thị hai phòng thí nghiệm dược phẩm đang phân tích ADN của chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu và dịch tiết da của chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng đừng bao giờ coi thường sức mạnh ẩn giấu của những kẻ nhỏ bé! Đêm nay, từng định kiến sẽ bị lật tung bằng những dữ liệu khoa học xác thực nhất!". Bố cục: Cận cảnh ánh mắt lóe sáng kiên định của chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C và chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini, ngọn lửa nhiệt huyết bùng cháy trong từng cử chỉ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L350</summary>

```text
HÌNH L350 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thứ nhất, năm 2012 các nhà khoa học đã giải mã bộ gen của Gấu Trúc Lớn và phát hiện ra một chuỗi peptit kháng khuẩn cực mạnh mang tên cathelicidin-AM!". Bố cục: Sơ đồ phân tử peptit cathelicidin-AM xoắn ốc phát sáng xanh lam được trích xuất từ mẫu máu bảo tồn của chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L351</summary>

```text
HÌNH L351 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong thử nghiệm diệt vi khuẩn Staphylococcus kháng thuốc, hợp chất từ Gấu Trúc tiêu diệt sạch vi khuẩn chỉ trong chưa đầy 1 giờ, nhanh gấp 6 lần so với thuốc kháng sinh clindamycin thông thường mất tới 6 giờ!". Bố cục: Đồng hồ đếm ngược so sánh: bên trái thuốc từ chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu quét sạch vi khuẩn dưới 1 giờ, bên phải thuốc kháng sinh thường mất tới 6 giờ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L352</summary>

```text
HÌNH L352 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn sắc tố axit hipposudoric từ mồ hôi đỏ của Hà Mã chặn đứng toàn bộ dải tia cực tím từ 200-600nm mà lại không hòa tan trôi tuột trong nước và thân thiện với rạn san hô —". Bố cục: Một lọ kem chống nắng sinh học mang biểu tượng chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ che chắn tia nắng UV rực rỡ mà vẫn giữ cho rạn san hô bên dưới xanh tươi an toàn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L353</summary>

```text
HÌNH L353 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thời khắc công bố kết quả Chung Kết điểm nhân đôi đã điểm! Sau khi cân nhắc giá trị khoa học, tính ứng dụng thực tiễn và sức lan tỏa nhân văn, hội đồng giám khảo xin tuyên bố:". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gõ mạnh chiếc búa gỗ xuống bàn, cả đấu trường nín thở im phăng phắc chờ nghe phán quyết cuối cùng.
```
</details>

<details><summary>L354</summary>

```text
HÌNH L354 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Huy chương đồng Chung Kết và 2 điểm thuộc về Lươn Điện với phát minh pin sinh học mềm hydrogel nuôi máy tạo nhịp tim tương lai!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ đeo tấm huy chương đồng danh giá lên cổ chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh, các tia điện xanh chúc mừng lấp lánh.
```
</details>

<details><summary>L355</summary>

```text
HÌNH L355 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Huy chương bạc Chung Kết và 4 điểm thuộc về... Con Lười! Với vườn nấm kỳ diệu trên bộ lông giúp con người chống lại bệnh sốt rét và tế bào ung thư!". Bố cục: Cả khán đài vỡ òa reo hò khi chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini nhận tấm huy chương bạc quý giá, vươn mình từ cuối bảng xếp hạng lên nhóm dẫn đầu!
```
</details>

<details><summary>L356</summary>

```text
HÌNH L356 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và Huy chương vàng Chung Kết cùng 6 điểm quyết định của Đại Hội Sinh Tồn Mùa 2 chính thức thuộc về... Bọ Pháo Thủ! Với công nghệ phun sương vi mô cứu hỏa và động cơ tên lửa vũ trụ!". Bố cục: Pháo hoa vàng rực nổ rền trời, bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ trao tấm huy chương vàng chung kết cho chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C, anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng nhảy cẫng lên ăn mừng lịch sử!
```
</details>

<details><summary>L357</summary>

```text
HÌNH L357 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Từ vị trí bị đánh giá chỉ vào thi cho đủ đội hình, chú bọ dài 2cm đã làm nên cú lội ngược dòng vĩ đại nhất mọi thời đại! Mời toàn thể quý vị cùng hướng mắt lên Bảng Tổng Sắp Chung Cuộc ngay sau đây!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng chỉ tay lên tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) đang bùng cháy ánh sáng rực rỡ chuẩn bị lễ đăng quang chính thức.
```
</details>

<details><summary>L358</summary>

```text
HÌNH L358 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khoảnh khắc lịch sử của Đại Hội Sinh Tồn Mùa 2 đã chính thức khép lại mọi dự đoán! Xin mời toàn thể mười tuyển thủ và hàng vạn khán giả cùng hướng mắt lên Bảng Tổng Sắp Cuối Cùng!". Bố cục: tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) hình chiếc khiên khổng lồ giữa sân vận động bừng sáng rực rỡ với mười cột đèn màu sắc từ cao xuống thấp, pháo hoa và dải băng kim tuyến rơi ngập tràn không gian; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vest đỏ đứng cạnh micro vàng.
```
</details>

<details><summary>L359</summary>

```text
HÌNH L359 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trải qua tám vòng đấu khốc liệt với 100% dữ liệu khoa học mới hoàn toàn, bảng vàng danh dự Mùa 2 đã ghi tên những nhà chinh phục xứng đáng nhất!". Bố cục: Mười tuyển thủ đứng dàn hàng ngang dưới ánh đèn sân khấu lung linh, trên ngực mỗi bạn lấp lánh những tấm huy chương danh giá; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tám vòng thi đấu! 100% dữ liệu mới! Chỉ có trí tuệ tiến hóa thực sự mới đủ sức chạm tay vào chiếc vương miện Mùa 2!". Bố cục: Chiếc vương miện vàng tỏa sáng chói lòa ở trung tâm đấu trường, mười cái bóng đổ dài hướng về phía đỉnh vinh quang; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L360</summary>

```text
HÌNH L360 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và Tân Vương của Đại Hội Sinh Tồn Mùa 2 chính thức gọi tên: Bọ Pháo Thủ với tổng điểm 12 điểm! Hai huy chương vàng, một huy chương bạc và một huy chương đồng!". Bố cục: chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C bước lên bục số một cao nhất, chiếc cúp vô địch vàng ròng và vương miện nạm ngọc được đặt lên đầu chú bọ tí hon, pháo hoa rực sáng góc trời; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L361</summary>

```text
HÌNH L361 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nặng chưa đầy nửa gam và từng bị các chuyên gia gạch tên ngay từ vòng cân ký! Nhưng với buồng phản ứng tia X đồng bộ, cơ chế van nổ tự điều áp không cần khí đẩy và bằng sáng chế công nghệ cứu hỏa bắn xa 10m, Bọ Pháo Thủ đã chinh phục trọn vẹn cả thế giới!". Bố cục: Cận cảnh chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C giơ cao chiếc cúp vô địch vàng, nòng pháo sau đuôi bắn lên trời một chùm khói pháo hoa ăn mừng rực rỡ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L362</summary>

```text
HÌNH L362 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ngôi vị Á Quân thuộc về: Lươn Điện với 8 điểm! Ba huy chương bạc và hai huy chương đồng!". Bố cục: chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh uốn lượn vươn mình lên bục số hai, đeo bộ huy chương lấp lánh quanh cổ cùng vầng hào quang tia sét xanh neon tuyệt đẹp; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L363</summary>

```text
HÌNH L363 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đập tan định kiến sống cô độc bằng màn săn mồi bầy đàn hơn 100 con tại sông Iriri, cùng phát minh pin mềm hydrogel 110V nuôi sống trái tim nhân loại! Xứng danh chiến thần đầm lầy Nam Mỹ!". Bố cục: chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh nháy mắt cười tự tin, các nhà khoa học trên khán đài đứng dậy vỗ tay chúc mừng á quân; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L364</summary>

```text
HÌNH L364 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và cú lội ngược dòng ngoạn mục nhất đêm nay gọi tên: Con Lười ở vị trí Hạng Ba chung cuộc với 7 điểm! Hai huy chương bạc và một huy chương đồng!". Bố cục: chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini bước lên bục số ba với nụ cười hiền lành rạng rỡ, cổ đeo hai tấm huy chương bạc sáng chói giữa tiếng hò reo vang dội của khán đài; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L365</summary>

```text
HÌNH L365 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Từ một thí sinh bị trêu chọc vì mất 10 phút mới trả lời xong một câu hỏi, Con Lười đã chứng minh sức mạnh phi thường với hệ thống dây chằng treo nội tạng, cụ tổ khổng lồ 4 tấn và 84 chủng nấm chống ung thư sốt rét trên bộ lông!". Bố cục: Bức ảnh chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini treo ngược tay cầm ống nghiệm thuốc cứu người, ánh mắt tự hào rạng rỡ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L366</summary>

```text
HÌNH L366 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Xếp ngay sát nút phía sau là hai chiến binh 6 điểm: Tôm Súng với hai huy chương vàng nhờ công nghệ tạo plasma gấp 10 lần laser và đế chế xã hội 300 tôm lính; cùng Thằn Lằn Quỷ Gai với một vàng, một bạc, một đồng nhờ kỹ thuật hắt cát ẩm và màng thu nước sa mạc!". Bố cục: chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa và chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm đứng cạnh nhau giơ càng và chỉnh mũ safari chào khán đài đầy kiêu hãnh, mỗi bạn đeo đầy huy chương sáng loáng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L367</summary>

```text
HÌNH L367 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhóm 5 điểm gọi tên hai gã khổng lồ đáng mến: Hà Mã với danh hiệu cỗ máy bơm 400kg Silicon mỗi ngày và thính giác xương hàm dưới; cùng Gấu Trúc Lớn với đột biến gen DUOX2, áo ngụy trang và liệu pháp phân ngựa chống rét!". Bố cục: chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ và chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu đứng khoác vai nhau cười tươi rạng rỡ, một tay cầm bình Silicon và một tay cầm mầm trúc xanh tươi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L368</summary>

```text
HÌNH L368 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhóm 4 điểm vinh danh hai bậc thầy bầu trời và mặt nước: Chim Tu Hú với đường bay vệ tinh 16.000km và màn cải trang chim ưng; cùng Cá Cung Thủ với bộ não nhận diện 44 khuôn mặt người chính xác 86%!". Bố cục: chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái đậu trên thành bể kính của chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn, cả hai cùng giơ tấm huy chương vàng vòng đấu của mình khoe với khán giả; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L369</summary>

```text
HÌNH L369 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và cuối cùng, Bố Già Capybara đạt 3 điểm danh dự với một huy chương bạc và một huy chương đồng nhờ cặp răng cửa tự mài sắc và văn hóa nuôi con chung cực kỳ nhân văn!". Bố cục: chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia đội mũ phớt mỉm cười điềm đạm nhấp ngụm trà thảo mộc, nhận tràng pháo tay nồng nhiệt từ toàn thể các loài thú rừng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khoan đã, trước khi vào vòng một, hãy cùng nghe nhận xét nhanh từ tổ trọng tài kỹ thuật về dàn đấu sĩ năm nay!". Bố cục: Tổ trọng tài gồm bác sĩ khám nghiệm, kỹ sư vũ khí và phóng viên 24 giờ cùng đứng quanh bàn thiết bị đo đạc tối tân; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng tiến tới phỏng vấn.
```
</details>

<details><summary>L370</summary>

```text
HÌNH L370 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khoan đã! Trước khi bước vào lễ bế mạc, anh MC xin phép điểm lại hành trình đáng kinh ngạc của cả mười đấu sĩ và phỏng vấn nhanh bộ ba quán quân đêm nay!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cầm micro tiến sát bục vinh quang 1-2-3 nơi chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C, chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh và chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini đang ôm cúp vàng rực rỡ.
```
</details>

<details><summary>L371</summary>

```text
HÌNH L371 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Từ những giây phút đầu tiên bị giới chuyên gia chê bai là tí hon và chậm chạp, Bọ Pháo Thủ và Con Lười đã chứng minh rằng giá trị thực sự của sự sống không nằm ở vẻ bề ngoài!". Bố cục: Màn hình lớn chiếu lại đoạn phim khoảnh khắc chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C đứng cạnh kính hiển vi ở Vòng cân ký và giờ phút đăng quang rực rỡ trên bục số một; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L372</summary>

```text
HÌNH L372 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Xin chúc mừng Tân Vương Bọ Pháo Thủ! Từ vị trí bị gạch tên ở vòng cân ký cho tới ngôi vương 12 điểm, cảm xúc của bạn lúc này thế nào?". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đưa chiếc micro sát nòng pháo nhỏ xíu của chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C trên bục số một; ánh đèn flash chớp sáng liên hồi.
```
</details>

<details><summary>L373</summary>

```text
HÌNH L373 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thưa anh MC và toàn thể khán đài, kích thước chưa đầy nửa gam chưa bao giờ là giới hạn! Chỉ cần bạn có áp suất nội tại vững vàng và không bao giờ bỏ cuộc dù có bị nuốt vào bụng cóc, bạn sẽ luôn bùng nổ tỏa sáng!". Bố cục: chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C giơ chiếc cúp vàng lên cao, bắn một chùm khói pháo hoa hình ngôi sao lên trần đấu trường ăn mừng đầy khí thế; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L374</summary>

```text
HÌNH L374 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một phát biểu cực kỳ bùng nổ! Còn Á Quân Lươn Điện thì sao? Từ một sinh vật bị gán mác cô độc, bạn đã cho cả thế giới thấy sức mạnh đoàn kết của bầy đàn hơn 100 chiến binh!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng quay sang bể kính của chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh, chú lươn điện chớp những tia sét xanh màu cầu vồng cực kỳ đẹp mắt chào khán giả; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L375</summary>

```text
HÌNH L375 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn Hạng Ba Con Lười — chủ nhân của cú lội ngược dòng giàu cảm xúc nhất lịch sử Đại Hội Sinh Tồn! Hãy giơ cao hai tấm huy chương bạc và chiếc cúp hiệu thuốc rừng mưa của bạn lên đi nào!". Bố cục: chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini chậm rãi nhưng đầy tự hào giơ cao hai tấm huy chương bạc lấp lánh, phía sau là các bác sĩ và nhà dược học vỗ tay rần rần; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L376</summary>

```text
HÌNH L376 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cảm ơn... tất cả... mọi người... Nhớ bảo vệ... rừng cây... cho tụi mình... treo ngược... ngủ ngon... nha!". Bố cục: Chú lười chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini mỉm cười hiền hậu mất mười giây để nói hết câu chúc, khiến cả khán đài vừa cười vừa rưng rưng xúc động; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L377</summary>

```text
HÌNH L377 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và chúng ta cũng đừng quên bảy người anh hùng còn lại đã chiến đấu hết mình suốt tám vòng thi đấu nghẹt thở đêm nay!". Bố cục: Bảy tuyển thủ còn lại cùng bước lên bục đồng hạng vinh dự, giơ cao những kỷ niệm chương lấp lánh dưới ánh đèn sân khấu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L378</summary>

```text
HÌNH L378 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tôm Súng và Thằn Lằn Quỷ Gai đã chứng minh rằng dù nhỏ bé nhưng hỏa lực plasma và kỹ thuật thu hoạch ẩm sa mạc đủ sức khuất phục bất kỳ đối thủ to xác nào!". Bố cục: chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa bắn một phát pháo bọt khí ăn mừng trên không, chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm tung nắm cát đỏ lấp lánh vẫy chào khán giả; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L379</summary>

```text
HÌNH L379 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hà Mã và Gấu Trúc Lớn đã lật đổ mọi định kiến sai lầm bấy lâu nay bằng nguồn khoáng chất Silicon nuôi sống dòng sông và bộ gen tiết kiệm năng lượng thiên tài!". Bố cục: chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ và chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu cùng bắt tay cười tươi, phía sau là bản đồ sinh thái châu Phi và rừng tre Tứ Xuyên rực sáng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo MC: toàn bộ các cảm biến áp suất, đồng hồ đo vôn kế 1.000V và máy chụp CT đều đã được hiệu chuẩn ở mức an toàn tuyệt đối!". Bố cục: Cô trợ lý phòng thí nghiệm giơ bảng kẹp hồ sơ kiểm tra các nút bấm nhấp nháy xanh trên bàn điều khiển; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L380</summary>

```text
HÌNH L380 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn bộ ba Chim Tu Hú, Cá Cung Thủ và Bố Già Capybara thì mãi mãi là biểu tượng của trí tuệ định vị không gian, thị giác nhận diện khuôn mặt và tinh thần ngoại giao hòa bình bất diệt!". Bố cục: chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái, chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn và chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia nâng ly trà chúc mừng đại hội thành công rực rỡ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L381</summary>

```text
HÌNH L381 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mười đấu sĩ, mười tuyệt tác tiến hóa độc bản! Không một ai ra về tay trắng, và từng con số đêm nay đều là một lời tri ân sâu sắc gửi tới trí tuệ vĩ đại của mẹ thiên nhiên!". Bố cục: Mười tuyển thủ đứng quây quần bên nhau trên bục vinh quang dưới mưa pháo giấy ngũ sắc, cùng giơ cao tay ăn mừng tình đoàn kết.
```
</details>

<details><summary>L382</summary>

```text
HÌNH L382 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bọ Pháo Thủ đứng trên đỉnh bục cao nhất, chiếc vương miện vàng bé xíu nằm vừa vặn trên chiếc đầu màu cam ánh kim. Một sinh vật nặng chưa tới nửa gam đã chiến thắng ngoạn mục giữa những cỗ xe tăng nặng tới 3 tấn!". Bố cục: chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C đứng trên bục số một giơ cao cúp vàng, vương miện lấp lánh; xung quanh là chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ, chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh, chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu, chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini cùng mỉm cười chúc mừng nhà tân vô địch nhỏ bé; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L383</summary>

```text
HÌNH L383 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chúc mừng bạn Bọ Pháo Thủ nha! Đợi mình xuống khỏi cái cây chuối này rồi tụi mình cùng đi ăn tiệc tre với cá sấu Caiman nhé!". Bố cục: chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu lộn nhào từ trên bục xuống thảm cỏ, ôm cành trúc vẫy tay chào vui vẻ bên cạnh chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia đang ngồi thư giãn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L384</summary>

```text
HÌNH L384 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhìn lại toàn bộ tám vòng thi đấu vừa qua, Mùa 2 đã dạy cho chúng ta một bài học tuyệt đẹp: trong tự nhiên không hề có sinh vật nào là 'lỗi tiến hóa' hay 'vô dụng'!". Bố cục: Bức tranh ghép toàn cảnh mười đấu sĩ: từ chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini mang vườn nấm chữa bệnh, chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu tiết kiệm năng lượng bằng đột biến gen, đến chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ bơm khoáng chất nuôi sống dòng sông; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L385</summary>

```text
HÌNH L385 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi đặc điểm kỳ quặc mà thoạt nhìn ta tưởng là ngớ ngẩn — như việc Con Lười treo ngược, Gấu Trúc lăn phân ngựa hay Hà Mã thải phân xuống nước — thực chất đều là những mắt xích hoàn hảo giữ cho cỗ máy Trái Đất vận hành trơn tru qua hàng triệu năm!". Bố cục: Các bánh răng sinh thái xanh lá khổng lồ gắn hình 10 con vật quay đều nhịp nhàng tạo thành một hành tinh Trái Đất tươi xanh rực rỡ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L386</summary>

```text
HÌNH L386 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và giống như thư viện sống khổng lồ của thiên nhiên, mười loài vật đêm nay đã mở ra cho nhân loại những công nghệ thay đổi cả tương lai: từ pin mềm nuôi trái tim nhân tạo, màng thu nước không tốn điện, vòi phun cứu hỏa xuyên rừng đến thuốc chống ung thư và sốt rét!". Bố cục: Nhà khoa học hoạt hình cùng các đấu sĩ mở từng trang sách ánh sáng chứa bản vẽ pin mềm, vòi phun sương và phân tử thuốc y học mới; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L387</summary>

```text
HÌNH L387 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng ngay ngoài cánh cửa đấu trường này, những trang sách quý giá đó đang đối mặt với nguy cơ bị xé rách mãi mãi bởi chính tác động của con người!". Bố cục: Bầu trời chuyển màu xám buồn lắng đọng, hình ảnh cánh rừng nhiệt đới bị thu hẹp và dòng sông ô nhiễm nổi lên phía sau sân khấu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L388</summary>

```text
HÌNH L388 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Rừng mưa nhiệt đới Panama và Amazon bị tàn phá đe dọa ngôi nhà của Con Lười và Lươn Điện — khiến chúng ta có thể mất đi những chủng nấm kháng sinh chưa kịp khám phá!". Bố cục: Hình ảnh chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini ôm cành cây cô đơn giữa mảng rừng bị chặt phá, ống nghiệm nấm thuốc mờ dần như sắp biến mất; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L389</summary>

```text
HÌNH L389 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khu bảo tồn rừng tre Tứ Xuyên cũng cần được gìn giữ từng mét vuông để Gấu Trúc Lớn có đủ nguồn thức ăn quanh năm và giữ lại peptit kháng khuẩn quý giá trong máu của chúng!". Bố cục: Cánh rừng trúc Tứ Xuyên xanh tươi đón ánh nắng bình minh, gia đình chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu vui đùa hạnh phúc giữa bụi tre non; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyệt vời! Còn các tuyển thủ thì sao? Tôm Súng đang khởi động khớp lò xo càng súng lách tách, trong khi Hà Mã đang há miệng kiểm tra lại cặp răng nanh!". Bố cục: chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa bóp nhẹ chiếc càng khổng lồ kêu cạch cạch làm tia nước bắn tung tóe; chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ ngáp một cái rộng 150 độ khoe răng nanh sắc nhọn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L390</summary>

```text
HÌNH L390 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đầm lầy Pantanal Nam Mỹ đang đối mặt với những trận cháy rừng lịch sử và hạn hán kéo dài, đe dọa không gian sống bình yên của hàng ngàn Bố Già Capybara và muôn loài chung sống xung quanh!". Bố cục: Bức tranh đầm lầy Pantanal bốc cháy khói mù, chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia dẫn đàn con nhỏ chạy về vùng nước an toàn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L391</summary>

```text
HÌNH L391 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sự suy giảm quần thể Hà Mã làm đứt gãy nguồn cung 400kg Silicon mỗi ngày cho các dòng sông châu Phi; còn biến đổi khí hậu khắc nghiệt khiến hành trình di cư 16.000km của Chim Tu Hú ngày càng gian nan hơn!". Bố cục: Quần thể chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ thưa thớt bên dòng sông cạn khô nứt nẻ, chú chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái mệt mỏi bay giữa cơn bão sa mạc dữ dội; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L392</summary>

```text
HÌNH L392 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tại những rạn san hô Caribe nơi Tôm Súng sinh sống, hiện tượng axit hóa đại dương và tẩy trắng san hô đang phá hủy những ngôi nhà bọt biển của cả đế chế 300 tôm lính!". Bố cục: Rạn san hô trắng xóa dưới đáy biển buồn bã, chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa ôm chặt chiếc bọt biển nhỏ bảo vệ tổ ấm của Tôm Chúa; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L393</summary>

```text
HÌNH L393 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và tại vùng rừng ngập mặn Đông Nam Á, nạn chặt phá rừng ven biển đang thu hẹp môi trường săn mồi độc đáo của những xạ thủ Cá Cung Thủ thông minh!". Bố cục: Khu rừng ngập mặn bên bờ biển bị thu hẹp, chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn bơi ngơ ngác tìm kiếm những tán lá xanh phía trên mặt nước; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L394</summary>

```text
HÌNH L394 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng tin vui cũng đã đến khi nỗ lực bảo tồn toàn cầu phát huy tác dụng! Nhờ việc phục hồi hàng ngàn héc-ta hành lang rừng tre kết nối tại Trung Quốc, Liên minh Bảo tồn Thiên nhiên Quốc tế IUCN đã chính thức hạ cấp Gấu Trúc Lớn từ mức Nguy Cấp xuống mức Sắp Nguy Cấp!". Bố cục: Bức tranh khu rừng trúc xanh mướt nối liền các dãy núi cao, đàn gấu trúc mẹ con vui đùa tung tăng dưới ánh nắng ấm áp; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L395</summary>

```text
HÌNH L395 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đó là minh chứng hùng hồn nhất cho thấy: khi con người chung tay hành động, thiên nhiên luôn có cơ hội hồi sinh mạnh mẽ! Bởi vì bảo vệ một loài vật bé nhỏ cũng chính là giữ lại cơ hội sống cho chính nhân loại mai sau!". Bố cục: Bàn tay trẻ thơ dịu dàng nâng niu quả địa cầu xanh biếc có mười người bạn hoang dã mỉm cười vẫy tay bình yên; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L396</summary>

```text
HÌNH L396 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và bây giờ, lá phiếu quyền lực nhất nằm trong tay của chính bạn! Bạn có đồng ý với ngôi vương của Bọ Pháo Thủ không? Hay trong trái tim bạn, Lươn Điện, Con Lười, Tôm Súng hay Hà Mã mới là nhà vô địch thực thụ?". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng bước ra sát màn hình chĩa chiếc micro vàng về phía khán giả, phía sau là tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) hiển thị đủ mười gương mặt tuyển thủ chờ bình chọn.
```
</details>

<details><summary>L397</summary>

```text
HÌNH L397 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và trước khi khép lại cánh cửa đấu trường Mùa 2, anh MC có một thử thách nhỏ dành cho các nhà thông thái nhí và khán giả đang theo dõi màn hình:". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng bước ra sát rìa sân khấu mỉm cười hóm hỉnh, bên cạnh hiện lên những biểu tượng câu đố khoa học thú vị; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L398</summary>

```text
HÌNH L398 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong suốt hơn 1 tiếng vừa qua, chi tiết khoa học mới nào làm bạn bất ngờ nhất: Gấu Trúc tắm phân ngựa chống rét, Cá Cung Thủ nhớ mặt người hay Bọ Pháo Thủ tạo ra súng cứu hỏa?". Bố cục: Màn hình hiện ba khung ảnh kỷ niệm rực rỡ của chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu, chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn và chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C đặt cạnh dấu hỏi bình chọn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L399</summary>

```text
HÌNH L399 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy bình luận tên nhà vô địch của bạn và chia sẻ xem bạn ấn tượng nhất với phát hiện khoa học mới nào dưới phần bình luận nhé!". Bố cục: Mười tuyển thủ đồng loạt vẫy tay tạm biệt khán giả giữa mưa hoa giấy rực rỡ sắc màu; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cúi chào nồng nhiệt.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không chần chừ thêm 1 giây nào nữa! Chúng ta hãy cùng tiến vào Vòng một ngay bây giờ: Năng lượng và cấu tạo kỳ dị!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng vung micro chỉ thẳng về phía cổng đấu trường nơi các máy quét cấu trúc sinh học và tia laser đang rực sáng đón chờ.
```
</details>

<details><summary>L400</summary>

```text
HÌNH L400 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mười tập phim lẻ, một đêm đại hội lịch sử với hàng trăm sự thật khoa học kỳ thú! Hy vọng hành trình hơn 1 giờ cùng Vẽ Chuyện Hoang Dã đã mang đến cho bạn thật nhiều tiếng cười sảng khoái và tình yêu sâu sắc dành cho thế giới tự nhiên!". Bố cục: Bức tranh kỷ niệm mười tuyển thủ Mùa hai cùng ôm nhau mỉm cười rạng rỡ giữa khung cảnh rừng xanh sông biếc lấp lánh ánh mặt trời; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L401</summary>

```text
HÌNH L401 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu bạn thích phong cách đại hội tranh tài mới toanh này, đừng ngần ngại chia sẻ video này cho bạn bè và người thân cùng chiêm ngưỡng những kiệt tác tuyệt vời của tạo hóa nhé!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng giơ cao chiếc micro vàng mỉm cười tri ân khán giả, phía sau là mười đấu sĩ vẫy tay thân thiện.
```
</details>

<details><summary>L402</summary>

```text
HÌNH L402 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và xin đừng vội tắt màn hình... bởi vì cánh cửa đường hầm bí mật của Đại Hội Sinh Tồn Mùa 3 vừa hé mở những hồ sơ rùng mình nhất!". Bố cục: Cánh cửa thép khổng lồ mang số ba màu đỏ rực từ từ mở hé, luồng ánh sáng tím ma mị và sương lạnh cuồn cuộn tràn ra sàn đấu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L403</summary>

```text
HÌNH L403 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một biệt đội dị nhân sở hữu những năng lực tự hủy và tái sinh điên rồ chưa từng thấy chuẩn bị đổ bộ! Một chú ếch tự co cơ bẻ gãy xương ngón chân đâm thủng da thịt làm móng vuốt chiến đấu!". Bố cục: Bóng đen bí ẩn đầu tiên lộ rõ bàn chân ếch với những chiếc móng vuốt xương trắng sắc nhọn đâm xuyên qua đầu ngón chân như siêu anh hùng Wolverine; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L404</summary>

```text
HÌNH L404 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một chú kỳ nhông sáu sừng mọc lại nguyên vẹn cả chi, tủy sống, 1/3 trái tim và não bộ mà không để lại một vết sẹo! Và một sinh vật đáy biển tự bắn toàn bộ ruột gan qua hậu môn trói chặt kẻ thù!". Bố cục: Hai bóng đen tiếp theo: chú kỳ nhông Axolotl sáu sừng lơ lửng phát sáng hào quang tái sinh và sinh vật đáy biển bắn mạng tơ ruột gan rực sáng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L405</summary>

```text
HÌNH L405 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thậm chí còn có sự góp mặt của loài chim cắt lao xuống với vận tốc 389 km/h, và loài cá mặt trăng nặng hai tấn ngơ ngác bậc nhất đại dương!". Bố cục: Hai bóng đen khổng lồ xuất hiện phía sau màn sương: bóng chim cắt xé gió lao xuống từ tầng mây và bóng cá mặt trăng tròn xoe kỳ dị; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L406</summary>

```text
HÌNH L406 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cộng thêm những cao thủ tí hon biết biến hóa thành thây ma và loài bò sát có sừng mọc xuyên qua hộp sọ! Mười dị nhân tiếp theo đang nóng lòng chờ ngày ra mắt!". Bố cục: Cánh cửa đường hầm Mùa 3 phát ánh sáng xanh biếc huyền bí với hàng loạt bóng đen hình thù quái dị chưa từng xuất hiện trên màn ảnh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L407</summary>

```text
HÌNH L407 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hẹn gặp lại toàn thể quý vị khán giả tại Đại Hội Sinh Tồn Mùa 3! Phóng viên và MC xin chào tạm biệt và hẹn gặp lại!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cùng mười tuyển thủ Mùa 2 đồng loạt vẫy tay chào tạm biệt khán giả trong tiếng nhạc khải hoàn rền vang khắp đấu trường.
```
</details>

<details><summary>L408</summary>

```text
HÌNH L408 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Huy chương bạc thuộc về Lươn Điện với bằng chứng lật đổ định kiến săn mồi cô độc! Huy chương đồng thuộc về Bọ Pháo Thủ với cơ chế van cách ly chống tự nổ!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ trao huy chương bạc cho chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh và huy chương đồng cho chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C; cả đấu trường reo hò nồng nhiệt.
```
</details>

<details><summary>L409</summary>

```text
HÌNH L409 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gấu Trúc và Hà Mã bám sát phía sau với 5 điểm! Bọ Pháo Thủ và Chim Tu Hú 4 điểm, Cá Cung Thủ và Capybara 3 điểm, Con Lười 1 điểm!". Bố cục: Bảng điểm hiển thị nhóm bám đuổi chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu, chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ ở mốc 5 điểm cùng chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C, chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái, chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn, chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia và chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini sẵn sàng bứt phá!
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chào mừng toàn thể khán đài bước vào Vòng một: Giải mã cấu tạo ẩn giấu và nguồn năng lượng sinh học! Ở vòng mở màn này, chúng ta không thi chạy hay cắn nhau, mà đưa các tuyển thủ vào máy quét công nghệ cao!". Bố cục: Sân đấu biến thành một trung tâm nghiên cứu công nghệ cao với các máy chụp cắt lớp vi tính CT, camera nhiệt hồng ngoại và màn hình ADN; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đứng cạnh bảng thông số.
```
</details>

<details><summary>L410</summary>

```text
HÌNH L410 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "mở đường chế tạo kem chống nắng sinh học thế hệ mới bảo vệ đại dương!". Bố cục: Một chú cá hề và rạn san hô cầu vồng bơi lội vui vẻ bên cạnh biểu tượng khiên chống nắng sinh học màu đỏ của chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ban giám khảo muốn biết: bộ máy bên trong cơ thể loài nào được thiết kế tinh vi, tiết kiệm hoặc tạo ra công suất năng lượng điên rồ nhất?". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ cầm chiếc thước kẹp và mô hình phân tử năng lượng phát sáng, trước mặt là ba chiếc huy chương đầu tiên của mùa giải.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thí sinh đầu tiên bước vào máy quét 3D là pháo thủ đại dương Tôm Súng! Khán giả đều đã biết cú búng càng tạo sóng âm của nó, nhưng cấu tạo tạo ra plasma mới là điều làm các kỹ sư choáng váng!". Bố cục: chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa bước vào buồng quét laser, chiếc càng búng khổng lồ được phóng đại thành mô hình cơ khí 3D quay tròn trên màn hình lớn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Năm 2019, nhóm kỹ sư cơ khí tại Đại học Texas A&M đã dùng tia X siêu nhỏ quét lớp vỏ lột xác của Tôm Súng để in 3D phóng đại gấp 5 lần!". Bố cục: Phòng thí nghiệm Đại học Texas A&M: hai kỹ sư mặc áo blouse trắng đặt chiếc càng tôm phóng đại 3D bằng nhựa vào bể nước thử nghiệm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Họ gắn một lò xo bẫy chuột để mô phỏng cơ bắp tôm búng càng! Kết quả thu được khiến cả giới vật lý plasma phải sững sờ kinh ngạc!". Bố cục: Mô hình càng in 3D đóng sập với tiếng kêu vang dội, một chùm tia plasma sáng rực kéo dài mười lăm phần tỷ giây lóe lên giữa lòng nước; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chỉ bằng lực cơ học đơn thuần không cần dùng điện hay tia laser, thiết bị mô phỏng càng Tôm Súng đã tạo ra dòng plasma dưới nước với hiệu suất cao gấp 10 lần máy móc nhân tạo hiện đại!". Bố cục: Biểu đồ so sánh hiệu suất tạo plasma: cột máy laser và điện cực thấp lè tè, cột mô hình càng chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa vọt cao gấp 10 lần rực sáng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng điều thú vị hơn nằm ở chức năng dự phòng thiên tài của Tôm Súng! Điều gì xảy ra nếu trong một cuộc giao tranh nảy lửa, nó bị kẻ thù cắn gãy mất chiếc càng súng khổng lồ?". Bố cục: Hình minh họa chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa bị một con cá lớn đớp mất chiếc càng súng to bên phải, để lại phần khớp cụt ngủn đáng thương; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Câu trả lời là: nó không hề bị tàn phế! Ngay sau khi mất chiếc càng súng bên phải, bộ gen của Tôm Súng lập tức kích hoạt cơ chế đảo ngược bất đối xứng!". Bố cục: Tín hiệu gen phát sáng từ trung tâm thần kinh chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa truyền tín hiệu sang chiếc càng nhỏ bên trái đang đứng bình thường; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chiếc càng nhỏ vốn chỉ dùng để gắp thức ăn bên tay trái sẽ phình to thần tốc sau vài lần lột xác, biến hình thành một khẩu đại bác súng nước mới toanh! Còn bên cụt cũ sẽ mọc lại một chiếc càng nhỏ thay thế!". Bố cục: Qua các chu kỳ lột xác, chiếc càng nhỏ bên trái của chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa lớn vọt lên thành càng súng khổng lồ, còn bên phải mọc ra càng nhỏ xinh xắn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một dây chuyền tự đổi tay thuận và tái tạo vũ khí vĩnh cửu! Dù gãy súng bao nhiêu lần, Tôm Súng vẫn luôn có một khẩu đại bác dự phòng trong tay!". Bố cục: chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa giơ khẩu đại bác mới bên tay trái ngắm bắn bùm một phát đầy tự tin, cả khán đài vỗ tay rầm rộ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và để kiểm tra thêm độ hiệu quả của cấu trúc cơ thể, các nhà nghiên cứu còn đưa thêm một thí sinh hạng trung vào buồng kiểm tra cấu trúc xương đặc biệt: Capybara!". Bố cục: chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia bước vào buồng quét cấu trúc giải phẫu cơ thể, màn hình hiện lên khung xương và hệ thống tuyến mồ hôi dưới da; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mặc dù sống quanh năm tại vùng đầm lầy nóng ẩm Nam Mỹ, Capybara lại sở hữu rất ít tuyến mồ hôi trên da nên không thể đổ mồ hôi làm mát như con người hay ngựa!". Bố cục: Kính hiển vi soi lên lớp da lông nâu thô của chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia: các tuyến mồ hôi thưa thớt gần như không đáng kể; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thay vì tốn nước đổ mồ hôi, cấu trúc bộ lông thưa cứng và lớp mỡ mỏng cho phép nhiệt lượng thoát ra cực nhanh ngay khi nó bước xuống ngâm mình trong làn nước mát! Một thiết kế làm mát bằng nước hoàn hảo cho gã khổng lồ gặm nhấm!". Bố cục: chú Chuột Lang Nước Capybara hoạt hình béo múp 65kg lông nâu vàng óng ả, mắt híp tịt điềm tĩnh trước mọi biến cố, mũi có bướu morillo đen, đội mũ phớt mafia ngâm nửa thân dưới làn nước xanh mát rượi, các mũi tên nhiệt màu đỏ bay vèo ra ngoài làm cơ thể hạ nhiệt tức thì; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giám khảo ghi nhận: cấu trúc cơ khí tạo plasma siêu việt và khả năng đổi tay vũ khí cực kỳ thông minh!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gật gù thán phục, gắn ngôi sao đánh dấu vào bảng chấm điểm cho chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyển thủ thứ hai bước vào buồng đo công suất năng lượng là Nhà Máy Điện Sống: Lươn Điện! Chúng ta đều biết con số đỉnh 860V, nhưng công suất điện thực tế và cơ chế bơm ion mới là kỳ quan sinh học!". Bố cục: chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh bơi vào bể đo công suất điện nối thẳng với một bảng bóng đèn khổng lồ và đồng hồ đo Ampe; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong khoảnh khắc săn mồi, nguồn điện của Lươn Điện có thể đạt cường độ dòng điện xấp xỉ một Ampe, tức là công suất tức thời đạt mức tương đương hơn 800W!". Bố cục: Đồng hồ Ampe và Watt nhảy vọt đồng thời, dàn bóng đèn sân khấu sáng rực rỡ chỉ bằng nguồn năng lượng phát ra từ thân chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L57</summary>

```text
HÌNH L57 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Làm thế nào 6.000 tế bào pin sinh học có thể xả hàng chục phát liên tiếp mà không bị cạn kiệt ngay lập tức? Bí mật nằm ở hệ thống bơm ion Natri và Kali siêu tốc!". Bố cục: Kính hiển vi điện tử soi vào màng tế bào electrocyte: hàng triệu kênh bơm ion Natri và Kali mở đóng nhịp nhàng như hàng triệu cánh cửa tự động; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L58</summary>

```text
HÌNH L58 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ngay sau mỗi lần phóng điện, các bơm sinh hóa tiêu thụ phân tử năng lượng ATP lập tức vận chuyển ngược dòng hàng tỷ ion qua màng tế bào, tái nạp điện thế sẵn sàng chiến đấu chỉ trong tích tắc!". Bố cục: Thanh pin năng lượng bên cạnh chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh tụt xuống rồi vụt nạp đầy lại một trăm phần trăm màu xanh lá chỉ trong nháy mắt; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L59</summary>

```text
HÌNH L59 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không cần dây cắm sạc, không cần pin lithium độc hại, toàn bộ quá trình sản xuất và tái nạp điện diễn ra bằng muối khoáng và nước ngọt ngay trong thớ thịt mềm mại của con cá!". Bố cục: Thân hình chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh phát sáng dịu nhẹ các mạch ion sinh học tự nhiên tuyệt đẹp, kỹ sư điện tử trên khán đài há hốc mồm kinh ngạc; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L60</summary>

```text
HÌNH L60 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và bây giờ là bất ngờ gây sốc nhất Vòng một! Tuyển thủ thứ ba bước lên máy đo năng lượng là chú gấu tròn xoe suốt ngày chỉ biết ôm tre: Gấu Trúc Lớn!". Bố cục: chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu lạch bạch bước vào máy quét trao đổi chất, hai tay vẫn ôm khư khư một mầm trúc tươi vừa nhai vừa gãi đầu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L61</summary>

```text
HÌNH L61 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong suốt nhiều thập kỷ, giới sinh học đau đầu tự hỏi: ăn một thứ thức ăn nghèo dinh dưỡng như tre với đường ruột ngắn ngủn của thú ăn thịt, tại sao Gấu Trúc không chết đói?". Bố cục: Một bác sĩ thú y hoạt hình cầm máy tính bấm liên hồi, nhìn chiếc ruột ngắn ngủn và đống tre khô mà vò đầu bứt tai khó hiểu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L62</summary>

```text
HÌNH L62 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Năm 2015, nghiên cứu đột phá công bố trên tạp chí Science của nhóm tiến sĩ Yonggang Nie đã giải mã bí mật động trời ẩn sâu trong bộ gen của Gấu Trúc!". Bố cục: Trang bìa tạp chí Science năm 2015 hiện lên với sơ đồ chuỗi xoắn ADN phát sáng điểm đột biến màu đỏ rực ở gen DUOX2; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L63</summary>

```text
HÌNH L63 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà khoa học phát hiện Gấu Trúc sở hữu một đột biến độc nhất vô nhị trên gen DUOX2 — loại gen chịu trách nhiệm tổng hợp hormone tuyến giáp kiểm soát tốc độ đốt cháy năng lượng!". Bố cục: Sơ đồ tuyến giáp của chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu hiển thị con dấu khóa hãm công suất, mức hormone T4 giảm chỉ còn một nửa bình thường; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L64</summary>

```text
HÌNH L64 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kết quả là mức độ hormone tuyến giáp T4 trong máu Gấu Trúc chỉ bằng 46,9% so với các loài thú có vú cùng kích thước!". Bố cục: Biểu đồ cột hormone: cột của chó sói và gấu nâu cao chót vót một trăm phần trăm, cột của chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu chỉ thấp gần một nửa; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L65</summary>

```text
HÌNH L65 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không chỉ giảm hormone, tiến hóa còn thu nhỏ kích thước não bộ của Gấu Trúc đi 5% và kích thước quả thận đi 11% để cắt giảm tối đa chi phí vận hành cơ thể!". Bố cục: Hình ảnh cắt lớp X-quang nội tạng chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu: tim, thận và não đều chạy ở chế độ tiết kiệm điện siêu hạng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L66</summary>

```text
HÌNH L66 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tính tổng thể, mức tiêu hao năng lượng hàng ngày của Gấu Trúc hoang dã chỉ bằng 45% so với 1 con thú bình thường nặng bằng nó! Tức là nó sống bằng chưa tới một nửa bình xăng của loài khác!". Bố cục: chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu ngồi thư giãn với biểu tượng pin tiết kiệm năng lượng Eco màu xanh lá phát sáng trên bụng, vẫy tay chào đầy tự hào; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L67</summary>

```text
HÌNH L67 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Để kiểm chứng, các nhà khoa học đã cấy đúng đoạn đột biến gen này vào chuột thí nghiệm, và lũ chuột lập tức trở nên ít vận động hơn hẳn 55% y hệt phong thái của gấu trúc!". Bố cục: Đàn chuột thí nghiệm có gen gấu trúc nằm phơi bụng thư giãn không thèm chạy bánh xe tập thể dục, cả khán đài cười ồ thích thú; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L68</summary>

```text
HÌNH L68 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vòng một kết thúc với kết quả thuyết phục tuyệt đối! Ban giám khảo xin công bố huy chương đồng thuộc về Gấu Trúc Lớn với đột biến gen DUOX2 tiết kiệm năng lượng thiên tài!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ bước ra đeo huy chương đồng lên cổ chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu đang ôm tre vui sướng; khán đài vỗ tay tán thưởng.
```
</details>

<details><summary>L69</summary>

```text
HÌNH L69 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Huy chương bạc thuộc về Lươn Điện với hệ thống tái nạp ion siêu tốc! Và Huy chương vàng gọi tên Tôm Súng với công nghệ plasma vượt trội cùng cơ chế đổi tay súng dự phòng!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ trao huy chương bạc cho chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh và huy chương vàng lấp lánh cho chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa; tiếng pháo tay vang dội khắp đấu trường.
```
</details>

<details><summary>L70</summary>

```text
HÌNH L70 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bảng tổng sắp sau Vòng một: Tôm Súng dẫn đầu với 3 điểm, Lươn Điện 2 điểm, và Gấu Trúc Lớn xuất sắc ghi điểm đồng đầu tiên!". Bố cục: tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) bừng sáng ba cột điểm đầu tiên của chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa, chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh và chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu; bảy đấu sĩ còn lại quyết tâm phục thù ở chặng kế tiếp.
```
</details>

<details><summary>L71</summary>

```text
HÌNH L71 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vòng hai ngay sau đây sẽ thử thách khả năng bắn tỉa tầm xa và trí tuệ quang học siêu phàm! Mời quý vị cùng hướng mắt về trường bắn!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng dẫn đầu đoàn tiến về trường bắn rừng ngập mặn nơi những tấm bia di động và các bài toán thị giác hóc búa đang chờ đón.
```
</details>

<details><summary>L72</summary>

```text
HÌNH L72 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chào mừng toàn thể quý vị đến với Vòng hai: Đấu trường xạ thủ tầm xa và trí tuệ thị giác siêu phàm! Ở vòng này, ban giám khảo không chỉ đo tầm bắn mà còn kiểm tra bộ não xử lý hình ảnh của các tuyển thủ!". Bố cục: Đấu trường chuyển sang khu rừng ngập mặn với những cành cây cao vươn ra mặt nước và hàng loạt camera tốc độ cao lắp đặt khắp nơi; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cầm micro quan sát.
```
</details>

<details><summary>L73</summary>

```text
HÌNH L73 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đấu sĩ mở màn là tay súng thiện xạ nổi tiếng nhất thế giới cá: Cá Cung Thủ! Khán giả đều đã nghe tài bắn tia nước tính khúc xạ ánh sáng của nó, nhưng thí nghiệm tại Đại học Oxford mới thực sự gây chấn động thế giới!". Bố cục: chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn bơi tiến vào bồn kính thử nghiệm, đối diện là một màn hình máy tính chống nước kỳ lạ chứ không phải côn trùng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L74</summary>

```text
HÌNH L74 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lâu nay giới khoa học thần kinh tin rằng chỉ những loài có vỏ não mới phát triển cao như con người, khỉ hay chim mới có khả năng phân biệt được khuôn mặt phức tạp của con người!". Bố cục: Sơ đồ bộ não người với vùng vỏ não mới neocortex phát sáng rực rỡ, đối chiếu với bộ não nhỏ xíu đơn giản của loài cá; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L75</summary>

```text
HÌNH L75 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cá hoàn toàn không có cấu trúc vỏ não mới này! Vậy liệu 1 con cá nhỏ bé ở đầm lầy có thể phân biệt được mặt người này với mặt người khác hay không?". Bố cục: Màn hình thí nghiệm chiếu ảnh hai khuôn mặt người đặt cạnh nhau trước mặt chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn, các nhà khoa học hồi hộp theo dõi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L76</summary>

```text
HÌNH L76 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Năm 2016, tiến sĩ Cait Newport tại Đại học Oxford và Đại học Queensland đã công bố nghiên cứu chấn động trên tạp chí Scientific Reports!". Bố cục: Trang bìa tạp chí Scientific Reports năm 2016 hiện rõ tên thí nghiệm trên loài Cá Cung Thủ Toxotes chatareus; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L77</summary>

```text
HÌNH L77 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhóm nghiên cứu huấn luyện Cá Cung Thủ nhận diện một khuôn mặt người mục tiêu để nhận thưởng thức ăn, sau đó trộn lẫn khuôn mặt đó vào giữa 44 khuôn mặt người lạ hoàn toàn khác nhau!". Bố cục: Màn hình hiển thị ma trận 44 bức ảnh khuôn mặt người đa dạng kích cỡ và đường nét phía trên mặt nước bể cá; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L78</summary>

```text
HÌNH L78 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kết quả làm toàn bộ giới khoa học thần kinh sững sờ: Cá Cung Thủ phun tia nước trúng phóc bức ảnh khuôn mặt quen thuộc với độ chính xác trung bình từ 81 đến 86%!". Bố cục: chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn ngắm kỹ và bắn tia nước chuẩn xác trúng ngay khuôn mặt mục tiêu giữa rừng ảnh người, biểu đồ tỷ lệ chính xác vọt lên 86%; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L79</summary>

```text
HÌNH L79 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thậm chí khi các nhà khoa học chuyển toàn bộ ảnh sang màu đen trắng, đồng bộ độ sáng và cắt bỏ hết kiểu tóc lẫn đường viền đầu, chú cá vẫn nhận ra gương mặt đó không chút sai sót!". Bố cục: Những bức ảnh khuôn mặt đen trắng bị cắt tròn đều giống hệt nhau, chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn vẫn không hề bối rối mà bắn trúng ngay lập tức; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L80</summary>

```text
HÌNH L80 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Quý vị thử tưởng tượng xem: 1 con cá dài một gang tay không có vỏ não nhận dạng lại nhớ mặt người giỏi hơn cả nhiều ứng dụng camera an ninh cũ kỹ!". Bố cục: Một nhân vật hoạt hình mặc áo sọc đeo mặt nạ hài hước đi ngang qua bể cá thì bị chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn nhận ra mặt lạ rồi phun tia nước vào mặt khiến nhân vật giật mình hài hước, khán giả cười ồ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L81</summary>

```text
HÌNH L81 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa dừng lại ở đó, khi bắn mồi thật trên cành cây, Cá Cung Thủ còn tự động đo trọng lượng của con mồi để điều chỉnh thể tích tia nước bắn ra!". Bố cục: So sánh hai phát bắn: với con kiến nhỏ nó bắn tia nước mảnh nhẹ nhàng, với con bọ cánh cứng nặng cân nó nén khối nước to gấp nhiều lần; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L82</summary>

```text
HÌNH L82 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó kiểm soát sự bất ổn định thủy động lực học khi nén dòng nước, tụ toàn bộ năng lượng vào mũi đạn tạo ra lực va chạm lớn hơn lực bám chân của côn trùng tới mười lần!". Bố cục: Hình ảnh phóng đại tia nước đang bay biến thành một đầu đạn thủy lực tròn đặc, đập bật chú bọ cứng đầu rơi thẳng xuống nước; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L83</summary>

```text
HÌNH L83 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không chỉ nhớ được 44 khuôn mặt ở góc nhìn thẳng, thí nghiệm nâng cao của Đại học Oxford còn thử xoay nghiêng các bức ảnh khuôn mặt theo nhiều góc độ khác nhau!". Bố cục: Các bức ảnh khuôn mặt trên màn hình máy tính xoay nghiêng sang trái phải ba mươi độ, chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn bơi nghiêng đầu quan sát chăm chú; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L84</summary>

```text
HÌNH L84 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kết quả đáng kinh ngạc: Cá Cung Thủ vẫn nhận diện chính xác người quen qua từng góc nghiêng mà không hề bị đánh lừa! Điều này chứng tỏ thị giác của loài cá này giải mã không gian 3D phức tạp hơn ta tưởng rất nhiều!". Bố cục: chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn bắn tia nước trúng phóc bức ảnh xoay nghiêng, đèn xanh báo hiệu kết quả đúng nhấp nháy rực rỡ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L85</summary>

```text
HÌNH L85 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giám khảo ghi nhận: bộ não xử lý thị giác của Cá Cung Thủ là một kiệt tác vượt xa mọi giới hạn kích thước não bộ!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ đeo kính gật gù thán phục, ghi điểm tuyệt đối vào bảng thi cho chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn.
```
</details>

<details><summary>L86</summary>

```text
HÌNH L86 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyển thủ thứ hai bước vào bài thi bắn tỉa là pháo thủ tí hon: Bọ Pháo Thủ! Nếu Cá Cung Thủ bắn tỉa bằng tia nước lạnh, thì Bọ Pháo Thủ là chuyên gia điều áp và nổ xung phản lực vi mô!". Bố cục: chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C tiến lên bục thử nghiệm tốc độ cao, các cảm biến áp suất và camera nhiệt chĩa thẳng vào chóp bụng có nòng súng của chú bọ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L87</summary>

```text
HÌNH L87 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Quý vị đã biết nhiệt độ tia hóa chất của nó sôi 100°C, nhưng điều gì tạo ra lực đẩy mạnh mẽ mà không làm vỡ nòng súng chỉ rộng vài phần nghìn cm?". Bố cục: Mặt cắt ngang nòng súng siêu nhỏ của chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C phóng đại hàng ngàn lần dưới kính hiển vi điện tử quét; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L88</summary>

```text
HÌNH L88 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Theo nghiên cứu mô phỏng thủy động lực học tại Đại học Leeds, bí mật nằm ở quá trình sôi chớp nhoáng bên trong buồng đốt nhỏ xíu: hơi nước chiếm tới hơn 90% thể tích khí thoát ra!". Bố cục: Sơ đồ buồng đốt với các bọt hơi nước sôi giãn nở tức thời chiếm hơn 90% thể tích, tạo áp suất đẩy luồng sương lao vọt ra ngoài; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L89</summary>

```text
HÌNH L89 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Áp suất chỉ cần tăng nhẹ khoảng 100 mbar là đủ tống toàn bộ hỗn hợp hóa chất sôi ra ngoài với vận tốc từ 12-35m mỗi giây, xé nhỏ thành hàng tỷ hạt sương đường kính chỉ từ 1-500 μm!". Bố cục: Dải hạt sương hóa chất siêu mịn phun ra ở tốc độ 35 m/s tạo thành một bức tường hơi nóng bỏng rát bao phủ toàn bộ mục tiêu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L90</summary>

```text
HÌNH L90 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhờ tháp pháo đuôi có khớp xoay linh hoạt 270°, chú bọ tí hon có thể vừa chạy trốn vừa bắn chuẩn xác vào mắt những kẻ săn mồi đang truy đuổi phía sau lưng mà không cần ngoái đầu nhìn lại!". Bố cục: chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C chạy hết tốc lực về phía trước nhưng nòng pháo quay ngược ra sau bắn trúng phóc mũi chú bọ ngựa khổng lồ đang đuổi theo; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L91</summary>

```text
HÌNH L91 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và tuyển thủ thứ ba của vòng hai mang đến một tuyệt kỹ đánh lừa thị giác đỉnh cao không cần dùng đến một giọt đạn nào: Chim Tu Hú!". Bố cục: chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái sải cánh bay lượn trên khu vực thử nghiệm thị giác, phía dưới là hàng chục mô hình chim chích đang ngồi canh tổ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L92</summary>

```text
HÌNH L92 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khán giả đều đã nghe chuyện Tu Hú đẻ trộm trứng trong 10 giây, nhưng tại sao 1 con chim to xác như Tu Hú lại có thể bình yên bay lượn sát tổ chim chủ mà không bị bầy chim nhỏ xúm vào mổ đuổi đi?". Bố cục: Một chú chim chích nhỏ ngước nhìn lên bầu trời thấy bóng chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái bay tới, bỗng nhiên toàn thân run lẩy bẩy tụt sâu xuống đáy tổ nấp kín; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L93</summary>

```text
HÌNH L93 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Năm 2000 11, giáo sư Welbergen và Davies công bố phát hiện thú vị trên tạp chí Behavioral Ecology về chiến thuật ngụy trang Batesian kép của Chim Tu Hú!". Bố cục: Bức ảnh so sánh hai loài chim đặt cạnh nhau: bên trái là Chim Ưng Sẻ ăn thịt hung dữ, bên phải là chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái trưởng thành có bộ lông giống hệt; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L94</summary>

```text
HÌNH L94 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Từ hình dáng cánh nhọn, kiểu bay lướt gió cho đến những dải lông vằn ngang màu nâu xám trước ngực và chân vàng, Chim Tu Hú trưởng thành đã tiến hóa ngoại hình giống hệt... Chim Ưng Sẻ ăn thịt!". Bố cục: Phóng đại họa tiết lông ngực vằn ngang của chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái và chim ưng sẻ, đường nét trùng khớp đến từng chi tiết đánh lừa thị giác; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L95</summary>

```text
HÌNH L95 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi chim chủ nhà nhìn thấy bộ ngực vằn ngang đó lướt qua, chúng lập tức hoảng loạn tưởng là kẻ săn mồi hung tợn nên bay đi trốn giữ mạng thay vì ở lại tấn công kẻ lạ mặt!". Bố cục: Các chú chim sẻ cuống cuồng chui tọt vào bụi rậm trốn, để lại chiếc tổ trống không cho chú Chim Tu Hú hoạt hình lông đốm hoa râm xám tro, mắt đỏ rực rỡ, đeo nơ tím than, vẻ mặt láu cá tinh quái thong thả đáp xuống thực hiện phi vụ dễ như trở bàn tay; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L96</summary>

```text
HÌNH L96 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thậm chí các nhà khoa học thử dùng sơn che đi các vạch vằn trên ngực mô hình Tu Hú, lập tức đàn chim chích trở nên hung hãn lao vào đánh đuổi túi bụi! Một màn cải trang cảnh sát chìm ngoạn mục của giới loài chim!". Bố cục: Mô hình Tu Hú bị che vạch ngực bị bầy chim sẻ xúm lại mổ rụng lông tơi tả, còn mô hình giữ nguyên vạch ngực lại khiến cả xóm chim im thin thít; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L97</summary>

```text
HÌNH L97 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thêm một màn đọ tài gay cấn nữa ở bài kiểm tra thị giác mà anh MC xin bổ sung giữa hai sát thủ bắn tỉa dưới nước: Cá Cung Thủ và Lươn Điện!". Bố cục: Màn hình chia đôi: một bên là chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn bơi dưới mặt nước gợn sóng lăn tăn, một bên là chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh lượn quanh các vật cản nhựa và kim loại; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L98</summary>

```text
HÌNH L98 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong tự nhiên, mặt nước đâu phải lúc nào cũng phẳng lặng như gương! Các thí nghiệm chứng minh Cá Cung Thủ vẫn bắn trúng đích ngay cả khi mặt nước đang gợn sóng liên tục nhờ khả năng cập nhật góc lệch theo thời gian thực!". Bố cục: chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn ngắm bắn xuyên qua những gợn sóng lăn tăn trên mặt hồ và vẫn bắn rơi trúng phóc con bọ đậu trên cành cây; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L99</summary>

```text
HÌNH L99 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn Lươn Điện thì dùng trường điện áp thấp 10V để phân biệt rạch ròi đâu là một thanh nhựa cách điện vô tri, đâu là 1 con cá thật đang thở thoi thóp dưới lớp bùn đặc!". Bố cục: chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh lượn qua thanh nhựa bỏ đi không thèm để ý, lập tức dừng lại khóa mục tiêu vào chú cá đang trốn sau hòn đá; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Mười quái kiệt mới. Tám vòng đấu sinh tử. Một chiếc vương miện!". Bố cục: tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) dựng giữa sân vận động rực lửa ban đêm, phía trên lơ lửng chiếc vương miện vàng phát sáng, mười chiếc bóng tuyển thủ đứng bên dưới.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Tôm Súng và Lươn Điện được đặt cược sẽ thắng. Còn Bọ Pháo Thủ nửa gam... chuyên gia bảo tham gia cho vui!". Bố cục: chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa và chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh đứng oai vệ trên hai cột điểm cao vút rực lửa và sét, bên dưới chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C và chú Con Lười ba ngón hoạt hình mặt cười toe toét ngơ ngác, lông phủ lớp rêu xanh nhạt, mắt có vệt sẫm, đeo chiếc đồng hồ báo thức mini đứng cạnh cột điểm thấp lè tè.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Vòng một: Tôm Súng tạo dòng plasma dưới nước hiệu suất gấp 10 lần máy laser!". Bố cục: chú Tôm Súng hoạt hình màu xanh biển đỏ cam, có một chiếc càng búng khổng lồ to bằng nửa thân hình, đeo kính ngắm bắn tỉa búng chiếc càng khổng lồ tạo ra đốm sáng plasma rực rỡ và luồng sóng xung kích dưới nước.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Vòng hai: Cá Cung Thủ nhận diện được 44 khuôn mặt người dù không có vỏ não!". Bố cục: chú Cá Cung Thủ hoạt hình thân dẹt màu bạc ánh vàng có 4-5 vạch đen thẳng đứng, đôi mắt to lồi xoay tròn trên đỉnh đầu, miệng nhọn hình phễu ngắm bắn bơi sát màn hình ngắm bắn tia nước chính xác trúng vào một tấm bia hình vẽ khuôn mặt hoạt hình hài hước giữa các tấm bia mục tiêu tròn.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Vòng ba: Gấu Trúc tắm phân ngựa tươi để khóa thụ thể lạnh, còn Quỷ Gai hất cát ẩm lên lưng giải khát!". Bố cục: chú Gấu Trúc Lớn hoạt hình béo tròn lông trắng đen, quầng mắt đen tròn ngơ ngác, hai tai đen xù, ôm cành trúc xanh, vẻ mặt vụng về đáng yêu lăn tròn trong tuyết lạnh và chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, đội mũ safari kaki, nơ đỏ thắm hất cát đỏ lên lưng đầy sáng tạo.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Vòng bốn: Hà Mã bơm 400kg Silicon mỗi ngày xuống sông nuôi cả hệ sinh thái hồ châu Phi!". Bố cục: chú Hà Mã hoạt hình khổng lồ béo tròn màu xám hồng tím, mồ hôi đỏ hồng bóng bẩy, miệng rộng ngoác khoe răng nanh to, đeo đai lưng vô địch đỏ đứng giữa dòng sông Mara rực rỡ, tinh thể Silicon phát sáng lan tỏa nuôi sống đàn cá bên dưới.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Vòng năm: Lươn Điện bỏ lối sống cô độc, hợp tác săn mồi theo bầy đàn hơn 100 con!". Bố cục: Hơn một trăm con chú Lươn Điện hoạt hình màu nâu xám đậm, mắt đeo kính bảo hộ cam, nơ tia sét vàng, thân phát ra các tia sét xanh neon lấp lánh quây tròn thành vòng sáng điện vây chặt đàn cá nhỏ.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Chung kết: ai mang lại công nghệ đỉnh cao nhất cho loài người? Nấm lông lười diệt ung thư hay vòi phun tên lửa Bọ Pháo Thủ?". Bố cục: Một nhà khoa học hoạt hình trầm trồ trước ống nghiệm nấm lông lười và động cơ vi đẩy phóng tia lửa của chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C.
```
</details>

<details><summary>S09</summary>

```text
HÌNH S09 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Và tân vương Mùa 2 là... chú bọ nửa gam từng bị gạch tên ngay từ vòng cân ký!". Bố cục: chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C đứng trên bục cao nhất đội vương miện vàng, giơ hai càng ăn mừng giữa pháo hoa nổ rực trời.
```
</details>

<details><summary>S10</summary>

```text
HÌNH S10 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Bạn có đồng ý không? Xem trọn tám vòng đấu trong video dài nhé,". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ và mười tuyển thủ cùng quay sang nhìn thẳng ra người xem, chú Bọ Pháo Thủ hoạt hình màu cam đỏ cánh xanh đen ánh kim, sau đuôi gắn nòng đại bác mini bốc khói nhiệt độ 100°C ở giữa giơ cúp vô địch lên.
```
</details>

<details><summary>S11</summary>

```text
HÌNH S11 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn Mùa 2; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "vì ở đây có mười quái kiệt mới, tám vòng đấu sinh tử, và một chiếc vương miện!". Bố cục: tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) dựng giữa sân vận động rực lửa ban đêm, phía trên lơ lửng chiếc vương miện vàng phát sáng, mười chiếc bóng tuyển thủ đứng bên dưới.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/410 của video YouTube về 10 quái kiệt — Đại Hội Sinh Tồn Mùa 2). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: anh MC dẫn chương trình hoạt hình vui tính: tóc vuốt dựng, mặc bộ vest đỏ tươi, thắt nơ bướm vàng, cầm chiếc micro vàng, nụ cười rộng. Nhân vật phụ cố định: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/11 của video YouTube Shorts về 10 quái kiệt — Đại Hội Sinh Tồn Mùa 2). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: anh MC dẫn chương trình hoạt hình vui tính: tóc vuốt dựng, mặc bộ vest đỏ tươi, thắt nơ bướm vàng, cầm chiếc micro vàng, nụ cười rộng. Nhân vật phụ: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ. 
```
</details>

## 7. SEO

- **title:** [TẬP ĐẶC BIỆT] 10 Quái Kiệt Tranh Đoạt Vương Miện Vũ Khí Sinh Học: Ai Lên Ngôi Vô Địch?
- **hook_paragraph:** Mười cỗ máy sinh học kỳ dị nhất từ Tập 11 đến Tập 20 trên kênh Vẽ Chuyện Hoang Dã — Gấu Trúc Lớn, Hà Mã, Con Lười, Chim Tu Hú, Capybara, Tôm Súng, Lươn Điện, Bọ Pháo Thủ, Thằn Lằn Quỷ Gai và Cá Cung Thủ — bước vào ĐẠI HỘI SINH TỒN MÙA 2 với 8 vòng đấu kịch tính và các giải phụ: đọ hỏa lực hủy diệt, xạ thủ bắn tỉa, giáp bọc thép, trao đổi chất dị thường, thao túng tâm lý ngoại giao, kỹ năng đào tẩu thần tốc, phúc khảo tin đồn và chung kết món quà cho nhân loại. Toàn bộ 100% sự thật khoa học MỚI chưa từng kể trong các tập lẻ: Tôm Súng búng nước 5.000°C làm nhiễu sóng sonar hải quân, Lươn Điện 860V dí cằm ngất cá sấu, Bọ Pháo Thủ nổ 500 phát/s thoát khỏi dạ dày cóc, Thằn Lằn Quỷ Gai hút nước từ bàn chân, Hà Mã chạy đáy sông, Con Lười tiêu hóa 30 ngày… và một nhà vô địch không ai ngờ tới!
- **question:** Nếu bạn là giám khảo, bạn sẽ trao chiếc vương miện Mùa 2 cho quái kiệt nào? Hãy viết tên nhà vô địch của bạn ở phần bình luận nhé!
- **next_teaser:** Đại Hội Sinh Tồn Mùa 3 — 10 dị nhân tái sinh và siêu năng lực (Ếch Lông Wolverine, Kỳ Nhông Axolotl, Hải Sâm...)
- **shorts_title:** Đại Hội Sinh Tồn Mùa 2: 10 Siêu Quái Kiệt – Ai Vô Địch?! 👑 #shorts #dongvat
- **shorts_desc:** Tôm Súng 5.000°C, Lươn Điện 860V, Bọ Pháo Thủ hay Thằn Lằn Quỷ Gai? Trận chiến vũ khí sinh học điên rồ nhất thế giới tự nhiên — nhà vô địch sẽ khiến bạn ngã ngửa! 👑
👉 Xem trọn bộ Đại Hội Sinh Tồn Mùa 2 trên kênh Vẽ Chuyện Hoang Dã.
- **bullets:** Vòng 1 – Hỏa lực hủy diệt: Cú búng cavitation 218 dB / 5.000°C, điện 860V, đại bác 100°C, lực cắn 1.800 PSI · Vòng 2 – Xạ thủ bắn tỉa: Cá Cung Thủ tính khúc xạ ánh sáng Snell, Bọ Pháo Thủ xoay nòng 270°, Lươn Điện hack não xung kép · Vòng 3 – Giáp phòng thủ: Quỷ Gai phồng cầu gai 90° & đầu giả, Hà Mã mồ hôi đỏ kháng khuẩn, Con Lười áo giáp rêu xanh · Vòng 4 – Tiêu hóa dị thường: Gấu Trúc nhai tre 14h, Con Lười 30 ngày/lá, Capybara cecotrophy, Quỷ Gai 2.500 kiến độc · Vòng 5 – Ngoại giao & Thao túng: Capybara làm bạn cá sấu, Tu Hú siêu kích thích họng đỏ & mafia bảo kê, Lươn Điện radar bùn · Vòng 6 – Đào tẩu thần tốc: Bọ Pháo Thủ thoát bụng cóc sau 1h, Quỷ Gai lặn cát 30s & dáng đi robot lá khô, Con Lười bơi vượt sông · Vòng 7 – Phúc khảo tin đồn: Hà Mã chạy đáy sông không bơi, Quỷ Gai không bắn máu từ mắt, Lươn Điện không phải lươn · Chung kết – Món quà nhân loại: Sóng siêu âm Tôm Súng phá sỏi thận, pin nano Lươn Điện, vòi phun tên lửa Bọ Pháo Thủ
- **tags:** vẽ chuyện hoang dã, đại hội sinh tồn, đại hội sinh tồn mùa 2, thế giới động vật, động vật kỳ lạ, tôm súng, lươn điện, bọ pháo thủ, thằn lằn quỷ gai, cá cung thủ, capybara, hà mã, con lười, gấu trúc lớn, chim tu hú, vũ khí động vật, khoa học thú vị, whiteboard animation, nghe trước khi ngủ
- **hashtags:** #VeChuyenHoangDa #TheGioiDongVat #DaiHoiSinhTon #MegaCompilation #DongVatKyLa #KhoaHoc

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/mega-02-dai-hoi-sinh-ton
python src/episode/pipeline.py tts    projects/mega-02-dai-hoi-sinh-ton     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/mega-02-dai-hoi-sinh-ton     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/mega-02-dai-hoi-sinh-ton     # phải in 'spec OK'
python scripts/audit_beats.py projects/mega-02-dai-hoi-sinh-ton              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/mega-02-dai-hoi-sinh-ton --force
python scripts/beat_sheet.py projects/mega-02-dai-hoi-sinh-ton               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/mega-02-dai-hoi-sinh-ton/audio/shorts.wav projects/mega-02-dai-hoi-sinh-ton/renders/mega-02-dai-hoi-sinh-ton_shorts.mp4
python src/episode/pipeline.py qa     projects/mega-02-dai-hoi-sinh-ton
python src/episode/pipeline.py seo    projects/mega-02-dai-hoi-sinh-ton
python src/episode/episode_doc.py     projects/mega-02-dai-hoi-sinh-ton
```
