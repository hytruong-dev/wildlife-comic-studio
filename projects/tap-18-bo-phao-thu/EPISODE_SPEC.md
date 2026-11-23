# TẬP 18 — BỌ PHÁO THỦ · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-18-bo-phao-thu`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-18-bo-phao-thu`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F2` · **Persona giọng:** `ky_su_vu_khi` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Bọ Pháo Thủ |
| Tiêu đề YouTube | Bị Cóc Nuốt 1 Tiếng Vẫn Thoát Thân Nhờ Khẩu Pháo 100°C Nổ 500 Lần/Giây?! \| Bọ Pháo Thủ \| Tập 18 |
| Video dài | `renders/tap-18-bo-phao-thu_long.mp4` — 8:50.2 (530.2s) |
| Shorts | `renders/tap-18-bo-phao-thu_shorts.mp4` — 0:49.5 (49.5s) |
| Thumbnail | `renders/tap-18-bo-phao-thu_thumbnail.jpg` |
| Số hình | dài 82 beat / 82 ảnh riêng; Shorts 11 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.1**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/82 của video YouTube về Bọ Pháo Thủ). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói. Nhân vật phụ cố định: chú cóc khổng lồ Nhật Bản da sần sùi màu xanh xám, mắt to tròn lồi, mồm rộng há to; chú chim săn mồi hoạt hình mỏ quặp hung hãn, lông vũ bay tứ tung; đàn kiến lửa hung hãn hàng trăm con giương càng răng cưa; chú bọ ngựa chiến binh màu xanh lá giơ hai lưỡi kiếm răng cưa sắc bén. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — PHÁO THỦ HÓA HỌC 2CM BẮN TIA HƠI SÔI 100°C
*Thẻ chương:* SINH VẬT 2CM SỞ HỮU VŨ KHÍ HÓA HỌC SÔI SÙNG SỤC

*Badge:* `HỒ SƠ VŨ KHÍ` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene01_p0.wav` (429 ký tự) · mood `tram_bi_an`

```text
Báo cáo thử nghiệm vũ khí tối mật cấp độ đỏ. Mở khóa toàn bộ dữ liệu lưu trữ của kho vũ khí sinh học! Toàn đội kỹ thuật hãy trang bị đầy đủ kính chắn nhiệt và mặt nạ phòng độc, bởi vì cỗ máy phòng vệ mà chúng ta tháo dỡ hôm nay sở hữu công nghệ cơ khí vượt xa trí tưởng tượng của con người. [surprise-oh] Quên đi những nọc độc rắn hổ hay gai nhọn bọ cạp, hãy nhìn vào một sinh vật nhỏ bé đang lững thững bò trên thảm lá rừng mục!
```
**Part 1** → `audio/vs/scene01_p1.wav` (376 ký tự) · mood `hao_hung`

```text
Đối tượng mang mã định danh số mười tám của chúng ta có ngoại hình đánh lừa thị giác tuyệt đối: Chiều dài cơ thể chỉ vỏn vẹn từ một phẩy năm xăng-ti-mét đến hai phẩy năm xăng-ti-mét, nặng chưa đầy một gam, đầu và chân màu cam đất, đôi cánh cứng màu xanh đen ánh kim. Nhìn bề ngoài, gã chẳng khác nào một chú bọ cánh cứng tầm thường mà bạn có thể vô tình giẫm phải trên lối đi.
```
**Part 2** → `audio/vs/scene01_p2.wav` (338 ký tự) · mood `don_dap`

```text
Nhưng trong danh mục vũ khí sinh học, giới khoa học quân sự đặt cho gã một biệt danh đầy nể sợ: Pháo Thủ Hóa Học, hay còn gọi là Bọ Pháo Thủ! [surprise-wa] Mỗi khi bị kẻ thù đe dọa, đuôi của con bọ này sẽ lập tức phát nổ liên thanh với tiếng nổ tanh tách đanh thép, bắn ra một luồng hơi hóa chất độc hại sôi sùng sục ở đúng một trăm độ C!
```
**Part 3** → `audio/vs/scene01_p3.wav` (320 ký tự) · mood `don_dap`

```text
Hãy tưởng tượng bạn đang bị một tia nước sôi một trăm độ C, đậm đặc hóa chất ăn mòn da bắn thẳng vào mắt với vận tốc lên tới hai mươi mét một giây! [surprise-oh] Bất kỳ loài chim săn mồi, thằn lằn hay nhện khổng lồ nào lỡ dại chạm vào Pháo Thủ Hóa Học đều phải giật bắn người, bỏng rát mắt và tháo chạy trong hoảng loạn.
```
**Part 4** → `audio/vs/scene01_p4.wav` (236 ký tự) · mood `tram_bi_an`

```text
Vậy điều kỳ diệu nào giúp một cơ thể sống mỏng manh dài chỉ hai xăng-ti-mét có thể đun sôi nước đến một trăm độ C chỉ trong vài phần nghìn giây mà không hề bị nổ tung chính bản thân mình? Hãy cùng mở bản vẽ kỹ thuật bên trong cơ thể gã!
```

### scene02 — HỆ THỐNG HAI BUỒNG TRỘN HÓA CHẤT NỔ NHỊ PHÂN
*Thẻ chương:* BÍ MẬT 2 BUỒNG CHỨA VÀ LỚP LÓT CHỊU NHIỆT

*Badge:* `BẢN VẼ CƠ KHÍ` · *mood mặc định:* `nghiem_trang_gia`

**Part 0** → `audio/vs/scene02_p0.wav` (340 ký tự) · mood `tram_bi_an`

```text
Dưới kính hiển vi điện tử quét X-quang tốc độ cao của Viện Công nghệ M-I-T, cấu trúc bên trong phần bụng của Pháo Thủ Hóa Học hiện ra hệt như một nhà máy sản xuất vũ khí hóa học thu nhỏ! [surprise-oh] Điểm cốt lõi giúp con bọ không bị tự hủy nằm ở nguyên lý vũ khí nhị phân: Tách biệt hoàn toàn hai chất phản ứng cho đến giây phút khai hỏa.
```
**Part 1** → `audio/vs/scene02_p1.wav` (335 ký tự) · mood `nghiem_trang_gia`

```text
Ở phần trên của khoang bụng là buồng chứa dự trữ lớn. Buồng này chứa hỗn hợp hai chất lỏng: mười phần trăm Hy-đrô-qui-nôn và hai mươi lăm phần trăm Hy-đrô pe-rô-xít, hay chính là nước oxy già đậm đặc. Khi hai chất này nằm chung trong buồng chứa, chúng hoàn toàn trơ lỳ và hòa bình với nhau, không hề xảy ra bất kỳ phản ứng cháy nổ nào.
```
**Part 2** → `audio/vs/scene02_p2.wav` (122 ký tự) · 🎭 cameo `co_tro_ly`

```text
Cảnh báo nhiệt độ buồng đốt đạt ngưỡng tới hạn một trăm độ C! Áp suất oxy tăng vọt, đề nghị khóa van an toàn ngay lập tức!
```
**Part 3** → `audio/vs/scene02_p3.wav` (254 ký tự) · mood `hao_hung`

```text
[laughter] Đúng như trợ lý kỹ thuật vừa báo cáo! Nối giữa buồng chứa dự trữ và buồng đốt bên ngoài là một chiếc van cơ học một chiều cực kỳ tinh xảo. Khi con bọ siết chặt cơ bụng, van mở ra, đẩy một lượng nhỏ hỗn hợp lỏng tràn vào buồng phản ứng thứ hai.
```
**Part 4** → `audio/vs/scene02_p4.wav` (331 ký tự) · mood `don_dap`

```text
Tại buồng đốt thứ hai này, thành vách được gia cố bằng một lớp màng chất sừng cu-tin dày đặc, chịu nhiệt và chống ăn mòn siêu cấp. Nơi đây đã được nạp sẵn hai enzyme xúc tác sinh học cực mạnh: Ca-ta-la-se và Pơ-rốc-xi-đa-se! [surprise-wa] Ngay khoảnh khắc giọt dung dịch chạm vào enzyme, phản ứng dây chuyền bùng nổ trong chớp mắt!
```
**Part 5** → `audio/vs/scene02_p5.wav` (296 ký tự) · mood `nghiem_trang_gia`

```text
Enzyme Ca-ta-la-se lập tức bẻ gãy Hy-đrô pe-rô-xít thành nước và khí oxy, giải phóng một lượng nhiệt khổng lồ đun sôi dung dịch lên đúng một trăm độ C! Đồng thời, enzyme Pơ-rốc-xi-đa-se oxy hóa Hy-đrô-qui-nôn thành chất Ben-zô-qui-nôn, một chất hóa học cực độc, cay xé da thịt và có mùi khét lẹt!
```
**Part 6** → `audio/vs/scene02_p6.wav` (341 ký tự) · mood `hao_hung`

```text
Toàn bộ chuỗi phản ứng sinh hóa dữ dội này diễn ra trong khoang thể tích tí hon chưa đầy một phần mười mi-li-mét khối! Nhờ lớp vỏ chitin cách nhiệt nhiều lớp bọc ngoài buồng đốt, các cơ quan nội tạng nhạy cảm khác như tim và ruột của Pháo Thủ Hóa Học hoàn toàn không bị ảnh hưởng bởi lò lửa một trăm độ C đang sôi sùng sục ngay sát bên cạnh.
```

### scene03 — ĐỘNG CƠ PHẢN LỰC XUNG 500 HZ VÀ THÁP PHÁO XOAY 270 ĐỘ
*Thẻ chương:* TỐC ĐỘ NỔ LIÊN THANH 500 ĐẾN 1000 LẦN MỖI GIÂY

*Badge:* `ĐỘNG CƠ XUNG` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene03_p0.wav` (289 ký tự) · mood `tram_bi_an`

```text
Nếu Pháo Thủ Hóa Học chỉ đơn thuần phun ra một dòng nước sôi liên tục, áp suất khổng lồ sẽ xé toạc bụng gã hoặc đẩy ngược cơ thể gã văng xa cả mét. [surprise-oh] Nhưng tạo hóa đã ban cho gã một phát minh cơ khí tương tự như động cơ tên lửa phản lực xung Vê-một của Đức trong Thế chiến hai!
```
**Part 1** → `audio/vs/scene03_p1.wav` (365 ký tự) · mood `don_dap`

```text
Mỗi phát bắn của con bọ thực chất là một chuỗi nổ liên thanh vi mô diễn ra với tần số điên rồ: Từ năm trăm lần một giây đến một ngàn lần một giây! [surprise-wa] Máy quay tốc độ cao ghi lại quy trình hoàn hảo: Khi phản ứng bùng nổ, khí oxy và hơi nước nóng giãn nở cực độ sẽ tự động ép chặt chiếc van cơ học đóng lại, ngăn không cho áp suất dội ngược vào buồng chứa.
```
**Part 2** → `audio/vs/scene03_p2.wav` (309 ký tự) · mood `don_dap`

```text
Sau đó, hơi sôi một trăm độ C phụt mạnh qua nòng đuôi ra ngoài. Ngay khi luồng hơi thoát đi, áp suất trong buồng đốt tụt xuống, van tự động mở ra hút mẻ hóa chất tiếp theo vào, và chu kỳ nổ lặp lại đúng năm trăm héc! Đó là lý do bạn nghe thấy tiếng súng nổ lách tách liên hồi như một khẩu súng máy liên thanh!
```
**Part 3** → `audio/vs/scene03_p3.wav` (111 ký tự) · 🎭 cameo `ga_khong_lo`

```text
Tôi vừa vồ thử từ phía sau một cái mà nó xoay nòng phụt thẳng vào mắt, cay xè rát bỏng húp híp suốt cả tuần lễ!
```
**Part 4** → `audio/vs/scene03_p4.wav` (413 ký tự) · mood `hao_hung`

```text
[laughter] Đừng bao giờ nghĩ đến chuyện đánh lén từ sau lưng! Đuôi của Pháo Thủ Hóa Học được thiết kế như một tháp pháo xe tăng bọc thép có khớp cầu xoay linh hoạt tới hai trăm bảy mươi độ, thậm chí gần ba trăm sáu mươi độ! Kẻ thù tấn công từ đằng trước, đằng sau, bên trái hay trên lưng, con bọ chỉ cần bẻ cong nòng đuôi qua nách hoặc qua vai là bắn trúng đích chính xác tuyệt đối mà không cần quay cả thân mình!
```
**Part 5** → `audio/vs/scene03_p5.wav` (256 ký tự) · mood `hao_hung`

```text
Thậm chí các thử nghiệm với camera chụp ảnh chuyển động siêu chậm còn chứng minh: Mỗi xung nổ vi mô chỉ kéo dài từ hai đến ba mi-li-giây! Tốc độ phản xạ ngắm bắn và khai hỏa của gã pháo thủ tí hon này nhanh hơn cái chớp mắt của con người tới hàng chục lần!
```

### scene04 — BỊ CÓC NUỐT SUỐT 1 TIẾNG VÀ MÀN NÔN ỌE TẨU THOÁT
*Thẻ chương:* THỬ THÁCH SỐNG SÓT BÊN TRONG DẠ DÀY CÓC KOBE

*Badge:* `THỰC CHIẾN KOBE` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene04_p0.wav` (337 ký tự) · mood `tram_bi_an`

```text
Bây giờ, hãy mở hồ sơ thực chiến ngoạn mục nhất trong lịch sử sinh học, một thí nghiệm chấn động thế giới do hai nhà khoa học Shinji Sugiura và Takuya Sato thuộc Đại học Kobe Nhật Bản công bố vào năm hai ngàn không trăm mười tám. [surprise-oh] Họ muốn kiểm tra: Điều gì sẽ xảy ra nếu một con cóc khổng lồ nuốt chửng Bọ Pháo Thủ vào bụng?
```
**Part 1** → `audio/vs/scene04_p1.wav` (244 ký tự) · mood `hao_hung`

```text
Loài cóc Nhật Bản nổi tiếng là kẻ phàm ăn bậc nhất, lưỡi dính phóng ra trong chớp mắt và nuốt chửng con mồi còn sống nguyên vào dạ dày ngập tràn axit tiêu hóa. Pháo Thủ Hóa Học bị chiếc lưỡi cóc cuốn chặt và trôi thẳng xuống đáy bao tử tối tăm!
```
**Part 2** → `audio/vs/scene04_p2.wav` (113 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Trời ơi cứu tôi với! Trong bụng tôi như có quả lựu đạn đang sôi ùng ục, nóng rát ruột gan không chịu nổi nữa rồi!
```
**Part 3** → `audio/vs/scene04_p3.wav` (292 ký tự) · mood `don_dap`

```text
[laughter] Đúng như tiếng rên rỉ đau đớn của chú cóc! Bị nhốt trong dạ dày thiếu oxy và ngập axit, con bọ không hề chịu đầu hàng số phận. Nó bình tĩnh kích hoạt hệ thống pháo đuôi, liên tục nã đạn hóa chất sôi một trăm độ C và xả khí Ben-zô-qui-nôn cay nồng thẳng vào niêm mạc dạ dày con cóc!
```
**Part 4** → `audio/vs/scene04_p4.wav` (268 ký tự) · mood `hao_hung`

```text
Cuộc chiến nội tạng kéo dài từ mười lăm phút đến một trăm lẻ bảy phút, trung bình hơn bốn mươi phút đồng hồ! Cuối cùng, con cóc không thể chịu đựng nổi những đợt nổ bỏng rát liên tiếp trong bụng. Nó há to mồm, co thắt dạ dày dữ dội và... ọe một bãi nôn lớn ra mặt đất!
```
**Part 5** → `audio/vs/scene04_p5.wav` (443 ký tự) · mood `hao_hung`

```text
[surprise-wa] Và từ trong đống dịch vị nhầy nhụa đó, Pháo Thủ Hóa Học lồm cồm bò ra ngoài, phủi sạch chân, giũ cánh và ung dung bước đi như chưa từng có chuyện gì xảy ra! Thống kê chấn động từ phòng thí nghiệm Kobe cho thấy: Có tới mười bốn trên mười sáu con bọ cỡ lớn đã thoát hiểm thành công, đạt tỷ lệ sống sót từ sáu mươi đến tám mươi phần trăm! Những con bọ này sau đó vẫn sống khỏe mạnh suốt nhiều tháng và tiếp tục sinh sản bình thường!
```

### scene05 — GIỚI HẠN KHO ĐẠN 20-30 PHÁT VÀ NGUY CƠ TỰ NỔ TUNG
*Thẻ chương:* TỬ HUYỆT KHI CẠN KIỆT HÓA CHẤT TRONG KHO

*Badge:* `ĐIỂM YẾU KỸ THUẬT` · *mood mặc định:* `bi_hai`

**Part 0** → `audio/vs/scene05_p0.wav` (318 ký tự) · mood `bi_hai`

```text
[sigh] Dù sở hữu hỏa lực tối tân như một khẩu pháo phản lực, nhưng trên đời này không có cỗ máy chiến tranh nào là hoàn hảo tuyệt đối. Mọi kỹ sư quân sự đều biết rằng: Sức mạnh càng hủy diệt thì cái giá phải trả càng đắt đỏ. Và điểm yếu chí mạng đầu tiên của Pháo Thủ Hóa Học chính là giới hạn của kho dự trữ đạn dược!
```
**Part 1** → `audio/vs/scene05_p1.wav` (285 ký tự) · mood `nghiem_trang_gia`

```text
Dung tích buồng chứa của con bọ dài hai xăng-ti-mét chỉ đủ hóa chất cho khoảng hai mươi đến ba mươi phát nổ liên thanh. Nếu gặp phải một đối thủ quá lì lợm hoặc bị bầy kiến lửa hàng ngàn con bao vây liên tục ép gã phải xả đạn không ngừng, con bọ sẽ rơi vào trạng thái cạn sạch kho đạn!
```
**Part 2** → `audio/vs/scene05_p2.wav` (137 ký tự) · 🎭 cameo `phat_thanh_vien`

```text
Thông báo từ trung tâm hậu cần: Kho đạn dự trữ đã cạn kiệt một trăm phần trăm! Cần tối thiểu hai mươi bốn tiếng để tổng hợp lại hóa chất!
```
**Part 3** → `audio/vs/scene05_p3.wav` (338 ký tự) · mood `bi_hai`

```text
[laughter] Chuẩn xác như bản tin hậu cần! Sau khi bắn hết cơ số đạn, Pháo Thủ Hóa Học mất từ hai mươi bốn tiếng đến ba mươi sáu tiếng ăn uống cật lực để cơ thể tái tổng hợp lại đủ lượng Hy-đrô-qui-nôn và Hy-đrô pe-rô-xít. Trong suốt khoảng thời gian nạp đạn này, gã hoàn toàn trở thành một con bọ cánh cứng yếu ớt không tấc sắt trong tay!
```
**Part 4** → `audio/vs/scene05_p4.wav` (358 ký tự) · mood `tram_bi_an`

```text
Chưa hết, gã béo tí hon này còn mang trên mình số phận của một thùng thuốc nổ di động! Nếu bị một kẻ thù to xác giẫm mạnh làm vỡ vách ngăn giữa hai buồng hóa chất khi van an toàn chưa kịp mở, phản ứng tỏa nhiệt sẽ xảy ra ngay bên trong cơ thể và nổ tung con bọ thành từng mảnh vụn! Sống bên cạnh cái chết mỗi ngày, đó là sự đánh đổi khắc nghiệt của tự nhiên.
```
**Part 5** → `audio/vs/scene05_p5.wav` (168 ký tự) · mood `nghiem_trang_gia`

```text
Bởi vậy, bài học sinh tồn đầu tiên của loài bọ này không phải là bắn bừa bãi, mà là ngắm thật kỹ, bắn thật chuẩn và chỉ khai hỏa khi thật sự bị dồn vào bước đường cùng!
```

### scene06 — ỨNG DỤNG CÔNG NGHỆ VÀ BÓNG ĐEN TẬP SAU
*Thẻ chương:* CÔNG NGHỆ BƠM PHUN PHẢN LỰC CHO TÀU VŨ TRỤ

*Badge:* `BÀI HỌC SINH TỒN` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene06_p0.wav` (364 ký tự) · mood `hao_hung`

```text
Nhìn vào Pháo Thủ Hóa Học, các kỹ sư cơ khí hàng đầu thế giới đã học được những bài học vô giá. Cấu tạo van một chiều và cơ chế phun xung nhiệt độ cao của loài bọ này hiện đang được các nhà khoa học mô phỏng để chế tạo các loại bình xịt thuốc y tế hạt siêu mịn, hệ thống dập lửa cứu hỏa siêu tốc, và thậm chí là động cơ tái khởi động cho các tàu vũ trụ thế hệ mới!
```
**Part 1** → `audio/vs/scene06_p1.wav` (278 ký tự) · mood `am_ap`

```text
Tự nhiên chính là người thầy vĩ đại nhất. Một sinh vật nhỏ bé bằng hạt lạc, không cần móng vuốt hay kích thước khổng lồ, chỉ cần kết hợp hài hòa giữa cấu trúc cơ khí tinh vi và hóa học chuẩn xác, đã có thể hiên ngang tồn tại suốt hàng triệu năm giữa muôn vàn kẻ săn mồi đẫm máu.
```
**Part 2** → `audio/vs/scene06_p2.wav` (239 ký tự) · mood `hao_hung`

```text
[surprise-oh] Bạn ấn tượng nhất với điều gì ở Pháo Thủ Hóa Học: Khả năng đun sôi hóa chất lên một trăm độ C trong tích tắc, hay màn thoát thân không tưởng sau một tiếng nằm trong dạ dày cóc? Hãy để lại bình luận chia sẻ cùng chúng tôi nhé!
```
**Part 3** → `audio/vs/scene06_p3.wav` (659 ký tự) · mood `tram_bi_an`

```text
Và bây giờ, hãy hướng ngòi bút về phân cảnh kết thúc bí ẩn! Trong tập tiếp theo, chúng ta sẽ rời khỏi thảm rừng ẩm ướt để tiến vào vùng sa mạc khô hạn bậc nhất hành tinh. [surprise-wa] Nơi đây có một bóng đen bí ẩn toàn thân phủ đầy gai nhọn sắc bén như bãi chông di động! Sinh vật kỳ dị này có siêu năng lực uống nước bằng chính da bàn chân qua hệ thống ống mao dẫn, có một chiếc đầu giả sau gáy để đánh lừa kẻ thù, và đặc biệt là vũ khí phòng vệ tối thượng: Bắn ra một tia máu đỏ lòm thẳng từ hốc mắt xa tới một mét để làm mù kẻ săn mồi! Đố bạn biết danh tính của quái kiệt sa mạc gai góc này là ai? Hãy để lại phán đoán của bạn bên dưới phần bình luận nhé!
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Bị cóc nuốt chửng vào dạ dày suốt một tiếng đồng hồ, con bọ nhỏ bé này đã làm gì để thoát thân còn sống nguyên vẹn? Đây là Bọ Pháo Thủ, gã tí hon dài chỉ hai xăng-ti-mét nhưng sở hữu khẩu đại bác hóa học đáng sợ nhất thế giới côn trùng! Bên trong bụng gã là hai buồng hóa chất riêng biệt chứa Hy-đrô-qui-nôn và Hy-đrô pe-rô-xít. Khi bị đe dọa, con bọ mở van xả hóa chất vào buồng đốt chứa enzyme xúc tác, đun sôi dung dịch lên đúng một trăm độ C và kích hoạt phản ứng nổ liên thanh năm trăm lần một giây! Tia hơi hóa chất sôi sùng sục và cay xé da bắn ra với vận tốc hai mươi mét một giây từ chiếc tháp pháo xoay hai trăm bảy mươi độ ở đuôi! Kể cả khi bị cóc nuốt vào bụng, Pháo Thủ Hóa Học vẫn bình tĩnh nã đạn liên tiếp trong dạ dày khiến con cóc đau đớn dữ dội và phải nôn ọe gã ra ngoài sau bốn mươi phút! Nhỏ bé nhưng sở hữu kỹ thuật cơ khí đỉnh cao, đó chính là bí thuật sinh tồn bất bại của Bọ Pháo Thủ!
```

**Whisper prompt:** `Bọ Pháo Thủ, Pháo Thủ Hóa Học, Carabidae, Brachinini, 100°C, 500 lần/giây, 1.000 lần/giây, 2cm, 1,5cm, 2,5cm, 20 m/s, 270°, 107 phút, 40 phút, Hydroquinone, Hydrogen peroxide, Catalase, Peroxidase, p-benzoquinone, Kobe, Shinji Sugiura, V-1, pulsejet, tháp pháo, dạ dày cóc, Thằn Lằn Quỷ Gai`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| một trăm độ C | 100°C |
| Một trăm độ C | 100°C |
| hai trăm mười hai độ Ép | 212°F |
| năm trăm lần một giây | 500 lần/giây |
| Năm trăm lần một giây | 500 lần/giây |
| một ngàn lần một giây | 1.000 lần/giây |
| Một ngàn lần một giây | 1.000 lần/giây |
| năm trăm héc | 500 Hz |
| một ngàn héc | 1.000 Hz |
| hai xăng-ti-mét | 2cm |
| Hai xăng-ti-mét | 2cm |
| một phẩy năm xăng-ti-mét | 1,5cm |
| Một phẩy năm xăng-ti-mét | 1,5cm |
| hai phẩy năm xăng-ti-mét | 2,5cm |
| mười mi-li-mét | 10mm |
| hai mươi lăm mi-li-mét | 25mm |
| hai đến ba mi-li-giây | 2-3 mili-giây |
| hai mươi mét một giây | 20 m/s |
| Hai mươi mét một giây | 20 m/s |
| mười mét một giây | 10 m/s |
| hai trăm bảy mươi độ | 270° |
| Hai trăm bảy mươi độ | 270° |
| ba trăm sáu mươi độ | 360° |
| Ba trăm sáu mươi độ | 360° |
| mười phần trăm | 10% |
| Mười phần trăm | 10% |
| hai mươi lăm phần trăm | 25% |
| Hai mươi lăm phần trăm | 25% |
| sáu mươi đến tám mươi phần trăm | 60-80% |
| Sáu mươi đến tám mươi phần trăm | 60-80% |
| mười bốn trên mười sáu | 14/16 |
| một trăm phần trăm | 100% |
| Một trăm phần trăm | 100% |
| mười tám | 18 |
| Mười tám | 18 |
| mười chín | 19 |
| hai mươi | 20 |
| ba mươi | 30 |
| bốn mươi | 40 |
| năm mươi | 50 |
| sáu mươi | 60 |
| bảy mươi | 70 |
| tám mươi | 80 |
| chín mươi | 90 |
| một trăm | 100 |
| hai trăm | 200 |
| một ngàn | 1.000 |
| mười lăm phút | 15 phút |
| Mười lăm phút | 15 phút |
| bốn mươi phút | 40 phút |
| Bốn mươi phút | 40 phút |
| một trăm lẻ bảy phút | 107 phút |
| một tiếng | 1 tiếng |
| Một tiếng | 1 tiếng |
| hai tiếng | 2 tiếng |
| hai mươi bốn tiếng | 24 tiếng |
| Hai mươi bốn tiếng | 24 tiếng |
| ba mươi sáu tiếng | 36 tiếng |
| Ba mươi sáu tiếng | 36 tiếng |
| hai ngàn không trăm mười tám | 2018 |
| Năm hai ngàn không trăm mười tám | Năm 2018 |
| thế kỷ hai mươi | thế kỷ 20 |
| Thế chiến hai | Thế chiến II |
| Thế Chiến hai | Thế chiến II |
| Vê-một | V-1 |
| Hy-đrô-qui-nôn | Hydroquinone |
| Hy-đrô pe-rô-xít | Hydrogen peroxide |
| Ca-ta-la-se | Catalase |
| Pơ-rốc-xi-đa-se | Peroxidase |
| Ben-zô-qui-nôn | Benzoquinone |
| Cô-bê | Kobe |
| Su-ghi-u-ra | Sugiura |
| Phao-xơ-giét | Pulsejet |
| Mô-lốc | Moloch |
| Tập mười tám | Tập 18 |
| Tập mười chín | Tập 19 |
| Tập mười bảy | Tập 17 |
| Tập mười sáu | Tập 16 |
| Tập mười lăm | Tập 15 |
| một mét | 1m |
| Một mét | 1m |
| một phần mười | 1/10 |
| Một phần mười | 1/10 |
| hàng ngàn độ | hàng ngàn độ |
| hàng triệu năm | hàng triệu năm |
| triệu năm | triệu năm |
| hai mươi đến ba mươi | 20-30 |
| mười lăm đến một trăm lẻ bảy | 15-107 |
| năm trăm đến một ngàn | 500-1.000 |
| hai buồng | 2 buồng |
| Hai buồng | 2 buồng |
| M-I-T | MIT |
| ki-lô-jun | kJ |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · PHÁO THỦ HÓA HỌC 2CM BẮN TIA HƠI SÔI 100°C · 82.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:02.3 (2.3s) | L01 | Báo cáo thử nghiệm vũ khí tối mật cấp độ |  | Phòng thí nghiệm quân sự tối mật: Một chiếc bàn kim loại có đèn rọi chiếu sáng, xung quanh là các bản vẽ vũ khí tối mật dán trên tường; một tấm biển đỏ đề 'BÁO CÁO THỬ NGHIỆM CẤP ĐỘ ĐỎ'. KHÔNG có chú Bọ Pháo Thủ trong cảnh này. |
| b02 | 00:02.3–00:05.2 (3.0s) | L02 | đỏ. Mở khóa toàn bộ dữ liệu lưu trữ của kho vũ khí |  | Một chiếc két sắt thép dày nặng nề đang mở khóa tung ra, bên trong tỏa ra ánh sáng xanh lam huyền bí của dữ liệu vũ khí sinh học lưu trữ; các tập hồ sơ bay lượn. KHÔNG có chú Bọ Pháo Thủ trong cảnh này. |
| b03 | 00:05.2–00:14.9 (9.6s) | L03 | sinh học! Toàn đội kỹ thuật hãy trang bị đầy đủ kính chắn nhiệt và mặt nạ phòng độc, bởi vì cỗ máy phòng vệ mà chúng ta tháo dỡ hôm nay sở hữu công nghệ cơ khí vượt xa trí tưởng tượng của con người. |  | BÊN TRÁI là các chuyên viên kỹ thuật hoạt hình đang vội vã đeo kính chắn nhiệt và mặt nạ phòng độc; BÊN PHẢI là đồng hồ đo nhiệt độ báo động đỏ rực. KHÔNG có chú Bọ Pháo Thủ trong cảnh này. |
| b04 | 00:14.9–00:20.8 (5.9s) | L04 | Quên đi những nọc độc rắn hổ hay gai nhọn bọ cạp, hãy nhìn vào một sinh vật nhỏ bé đang lững thững bò trên thảm lá rừng mục! |  | BÊN TRÁI là chiếc đầu rắn hổ mang bành nhe răng nanh và chiếc đuôi bọ cạp bị gạch chéo đỏ lớn; BÊN PHẢI là thảm lá mục rừng nhiệt đới bí ẩn với ánh nắng le lói rọi xuống một đốm sáng nhỏ. |
| b05 | 00:20.8–00:34.2 (13.4s) | L05 | Đối tượng mang mã định danh số 18 của chúng ta có ngoại hình đánh lừa thị giác tuyệt đối: Chiều dài cơ thể chỉ vỏn vẹn từ 1,5cm đến 2,5cm, nặng chưa đầy một gam, đầu và chân màu cam đất, đôi cánh cứng màu xanh đen | **1,5-2,5cm** · chiều dài cơ thể · L/360 · [0.32, 0.55] | Chân dung cận cảnh của chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói: một chú bọ cánh cứng nhỏ xíu đứng cạnh một chiếc thước dây đo chiều dài từ 1,5cm đến 2,5cm; thân màu xanh đen án |
| b06 | 00:34.2–00:40.5 (6.3s) | L06 | ánh kim. Nhìn bề ngoài, gã chẳng khác nào một chú bọ cánh cứng tầm thường mà bạn có thể vô tình giẫm phải trên lối đi. |  | Góc nhìn từ trên cao xuống lối mòn rừng: Một chiếc đế giày leo núi khổng lồ đang bước xuống sát sạt chú chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói; chú Bọ Pháo Thủ (Bombardier Bee |
| b07 | 00:40.5–00:47.1 (6.6s) | L07 | Nhưng trong danh mục vũ khí sinh học, giới khoa học quân sự đặt cho gã một biệt danh đầy nể sợ: Pháo Thủ Hóa Học, hay còn gọi là Bọ Pháo Thủ! |  | Hồ sơ vũ khí sinh học: Một tấm thẻ định danh quân sự có in ảnh chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói cùng dòng chữ lớn 'PHÁO THỦ HÓA HỌC'; bên cạnh là huy hiệu biểu tượng đầu |
| b08 | 00:47.1–00:56.2 (9.0s) | L08 | Mỗi khi bị kẻ thù đe dọa, đuôi của con bọ này sẽ lập tức phát nổ liên thanh với tiếng nổ tanh tách đanh thép, bắn ra một luồng hơi hóa chất độc hại sôi sùng sục ở đúng 100°C! | **100°C** · nhiệt độ hơi sôi · R/380 · [0.75, 0.52] | chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói kích hoạt vũ khí ở đuôi: Một tiếng nổ chói tai phát ra từ đuôi, luồng khói và hơi nước sôi 100°C bắn phụt ra như pháo cao xạ, tia nhiệt  |
| b09 | 00:56.2–01:03.8 (7.7s) | L09 | Hãy tưởng tượng bạn đang bị một tia nước sôi 100°C, đậm đặc hóa chất ăn mòn da bắn thẳng vào mắt với vận tốc lên tới 20 m/s! | **20 m/s** · vận tốc xé gió · R/360 · [0.72, 0.48] | Góc nhìn thứ nhất cực kỳ kịch tính: Tia nước sôi 100°C bắn thẳng về phía ống kính với tốc độ 20 m/s xé gió, hơi nước trắng xóa bốc lên mù mịt kèm các giọt hóa chất ăn mòn phát sáng. |
| b10 | 01:03.8–01:11.1 (7.3s) | L10 | Bất kỳ loài chim săn mồi, thằn lằn hay nhện khổng lồ nào lỡ dại chạm vào Pháo Thủ Hóa Học đều phải giật bắn người, bỏng rát mắt và tháo chạy trong hoảng loạn. |  | Cảnh tượng săn mồi hỗn loạn: BÊN TRÁI chú chú chim săn mồi hoạt hình mỏ quặp hung hãn, lông vũ bay tứ tung mỏ quặp bị trúng luồng hơi sôi đang giật bắn mình nhắm tịt mắt, lông đầu bốc khói; một con thằn lằn bên cạnh cuống cuồng tháo chạy. |
| b11 | 01:11.1–01:19.9 (8.8s) | L11 | Vậy điều kỳ diệu nào giúp một cơ thể sống mỏng manh dài chỉ 2cm có thể đun sôi nước đến 100°C chỉ trong vài phần nghìn giây mà không hề bị nổ tung chính bản thân mình? | **2cm** · kích thước tí hon · L/380 · [0.28, 0.55] | chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói đứng ở GIỮA trên nền trắng, cơ thể 2cm nhỏ bé nguyên vẹn mỉm cười; một chiếc nhiệt kế khổng lồ bên cạnh chỉ vọt lên mốc 100°C màu đỏ rực |
| b12 | 01:19.9–01:22.7 (2.7s) | L12 | Hãy cùng mở bản vẽ kỹ thuật bên trong cơ thể gã! |  | Bàn làm việc của kỹ sư: Một bản vẽ thiết kế cơ khí màu xanh lam (blueprint) trải rộng ra, hiển thị các đường nét kỹ thuật của bụng chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói với c |

### scene02 · HỆ THỐNG HAI BUỒNG TRỘN HÓA CHẤT NỔ NHỊ PHÂN · 99.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.5 (9.5s) | L13 | Dưới kính hiển vi điện tử quét X-quang tốc độ cao của Viện Công nghệ MIT, cấu trúc bên trong phần bụng của Pháo Thủ Hóa Học hiện ra hệt như một nhà máy sản xuất vũ khí hóa học thu nhỏ! |  | Phòng thí nghiệm synchrotron công nghệ cao: Kính hiển vi điện tử quét X-quang tốc độ cao đang chiếu chùm tia sáng quét qua cơ thể chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói; màn h |
| b02 | 00:09.5–00:16.6 (7.1s) | L14 | Điểm cốt lõi giúp con bọ không bị tự hủy nằm ở nguyên lý vũ khí nhị phân: Tách biệt hoàn toàn hai chất phản ứng cho đến giây phút khai hỏa. |  | Sơ đồ nguyên lý vũ khí nhị phân: Hai bình chứa hóa chất riêng biệt đặt song song, ở giữa có bức tường ngăn cách bằng thép kiên cố; biểu tượng an toàn màu xanh lá lấp lánh. |
| b03 | 00:16.6–00:19.3 (2.7s) | L15 | Ở phần trên của khoang bụng là buồng chứa dự trữ lớn. |  | Đặc tả buồng dự trữ lớn ở bụng trên của chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói: Một khoang chứa hình quả thận trong suốt, bên trong chứa đầy dung dịch lỏng trong vắt không màu |
| b04 | 00:19.3–00:26.1 (6.8s) | L16 | Buồng này chứa hỗn hợp hai chất lỏng: 10% Hydroquinone và 25% Hydrogen peroxide, hay chính là nước oxy già đậm đặc. | **10%** · Hydroquinone · L/360 · [0.3, 0.52]<br>**25%** · Hydrogen peroxide · R/420 · [0.72, 0.58] | Phân tích hóa học: Hai ống nghiệm dán nhãn; BÊN TRÁI là ống 10% Hydroquinone, BÊN PHẢI là ống 25% Hydrogen peroxide (nước oxy già); hai chất hòa vào nhau trong bình thủy tinh mà không có phản ứng. |
| b05 | 00:26.1–00:32.4 (6.3s) | L17 | Khi hai chất này nằm chung trong buồng chứa, chúng hoàn toàn trơ lỳ và hòa bình với nhau, không hề xảy ra bất kỳ phản ứng cháy nổ nào. |  | Hai phân tử hóa học hoạt hình dễ thương đang bắt tay nhau hòa bình, nở nụ cười hiền lành bên trong khoang bụng của chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói, không có một tia lửa |
| b06 | 00:32.4–00:35.5 (3.1s) | L18 | Cảnh báo nhiệt độ buồng đốt đạt ngưỡng tới hạn 100°C! | **100°C!** · nhiệt độ tới hạn · R/360 · [0.75, 0.48] | Màn hình bảng điều khiển kỹ thuật nhấp nháy đèn đỏ báo động: Cột nhiệt kế nhảy vọt lên 100°C; kim đồng hồ áp suất rung lắc dữ dội ở vùng nguy hiểm màu đỏ. |
| b07 | 00:35.5–00:39.4 (3.9s) | L19 | Áp suất oxy tăng vọt, đề nghị khóa van an toàn ngay lập tức! |  | Hình ảnh van cơ học cảnh báo: Một chiếc van kim loại màu vàng đang bị áp lực khí nén đẩy căng phồng, trợ lý kỹ thuật hoạt hình đang cuống cuồng xoay vô-lăng van khóa an toàn. |
| b08 | 00:39.4–00:41.6 (2.2s) | L20 | Đúng như trợ lý kỹ thuật vừa báo cáo! |  | chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói đội mũ kỹ sư mỉm cười tự tin, cầm chiếc mỏ lết chỉ vào cơ chế van tự động bên trong cơ thể mình; các bánh răng cơ khí ăn khớp hoàn hảo. |
| b09 | 00:41.6–00:46.5 (4.9s) | L21 | Nối giữa buồng chứa dự trữ và buồng đốt bên ngoài là một chiếc van cơ học một chiều cực kỳ tinh xảo. |  | Cận cảnh cấu trúc van cơ học một chiều: Ống dẫn hẹp nối buồng dự trữ với buồng đốt, van có lá chắn đàn hồi chỉ cho chất lỏng chảy theo một chiều từ trên xuống dưới. |
| b10 | 00:46.5–00:52.2 (5.7s) | L22 | Khi con bọ siết chặt cơ bụng, van mở ra, đẩy một lượng nhỏ hỗn hợp lỏng tràn vào buồng phản ứng thứ hai. |  | chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói siết cơ bụng màu cam đất: Khoang bụng co lại ép một giọt dung dịch lỏng màu xanh ngọc chảy qua khe van, rơi tọt xuống buồng đốt nhỏ phía |
| b11 | 00:52.2–00:58.3 (6.1s) | L23 | Tại buồng đốt thứ hai này, thành vách được gia cố bằng một lớp màng chất sừng cu-tin dày đặc, chịu nhiệt và chống ăn mòn siêu cấp. |  | Bên trong buồng đốt thứ hai: Thành vách buồng được lót bằng lớp màng sừng cutin dày cộp màu nâu đậm, bóng loáng và kiên cố như lớp gạch chịu nhiệt của lò luyện thép. |
| b12 | 00:58.3–01:03.9 (5.6s) | L24 | Nơi đây đã được nạp sẵn hai enzyme xúc tác sinh học cực mạnh: Catalase và Peroxidase! |  | Hai chú enzyme hoạt hình ngộ nghĩnh: Enzyme Catalase đội mũ công nhân cầm kéo sắc bén, và enzyme Peroxidase mang bình oxy đang đứng chờ sẵn trong buồng đốt. |
| b13 | 01:03.9–01:07.9 (3.9s) | L25 | Ngay khoảnh khắc giọt dung dịch chạm vào enzyme, phản ứng dây chuyền bùng nổ trong chớp mắt! |  | Vụ nổ dây chuyền bùng phát: Giọt dung dịch chạm vào mặt enzyme liền lóe sáng chói lòa như pháo hoa, bọt khí sôi ùng ục, các tia lửa nhiệt lượng tỏa ra dữ dội. |
| b14 | 01:07.9–01:14.7 (6.8s) | L26 | Enzyme Catalase lập tức bẻ gãy Hydrogen peroxide thành nước và khí oxy, giải phóng một lượng nhiệt khổng lồ đun sôi dung dịch lên đúng 100°C! | **100°C** · nhiệt lượng bùng nổ · L/380 · [0.32, 0.52] | Sơ đồ phản ứng hóa học bùng nổ: Hydrogen peroxide bị bẻ đôi thành H2O và bọt khí Oxy bốc hơi cuồn cuộn; ngọn lửa nhiệt lượng 100°C bùng cháy rực rỡ. |
| b15 | 01:14.7–01:21.8 (7.1s) | L27 | Đồng thời, enzyme Peroxidase oxy hóa Hydroquinone thành chất Benzoquinone, một chất hóa học cực độc, cay xé da thịt và có mùi khét lẹt! |  | Chất độc Benzoquinone hình thành: Một đám mây khí màu nâu vàng cay xè, bốc khói khét lẹt kèm các biểu tượng mắt cay xè toát ra từ dung dịch đang sôi. |
| b16 | 01:21.8–01:28.0 (6.2s) | L28 | Toàn bộ chuỗi phản ứng sinh hóa dữ dội này diễn ra trong khoang thể tích tí hon chưa đầy một phần 10mm khối! | **1/10 mm³** · thể tích buồng đốt · R/360 · [0.72, 0.5] | So sánh kích thước siêu vi mô: Một chiếc đầu kim may khổng lồ, trên đầu kim là buồng đốt tí hon của chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói đang phát sáng; kích thước chỉ 1/10  |
| b17 | 01:28.0–01:39.7 (11.7s) | L29 | Nhờ lớp vỏ chitin cách nhiệt nhiều lớp bọc ngoài buồng đốt, các cơ quan nội tạng nhạy cảm khác như tim và ruột của Pháo Thủ Hóa Học hoàn toàn không bị ảnh hưởng bởi lò lửa 100°C đang sôi sùng sục ngay sát bên cạnh. |  | Mặt cắt cách nhiệt hoàn hảo: Lớp vỏ chitin nhiều tầng cách nhiệt bao quanh buồng đốt đỏ rực; bên ngoài là trái tim và nội tạng của chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói vẫn m |

### scene03 · ĐỘNG CƠ PHẢN LỰC XUNG 500 HZ VÀ THÁP PHÁO XOAY 270 ĐỘ · 86.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.9 (7.9s) | L30 | Nếu Pháo Thủ Hóa Học chỉ đơn thuần phun ra một dòng nước sôi liên tục, áp suất khổng lồ sẽ xé toạc bụng gã hoặc đẩy ngược cơ thể gã văng xa cả mét. |  | Tình huống giả định hài hước: Nếu xịt nước sôi liên tục, cơ thể chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói bị lực phản lực đẩy lùi văng xa tít tắp, xoay mòng mòng như quả bóng bay |
| b02 | 00:07.9–00:14.1 (6.2s) | L31 | Nhưng tạo hóa đã ban cho gã một phát minh cơ khí tương tự như động cơ tên lửa phản lực xung V-1 của Đức trong Thế chiến II! | **TÊN LỬA V1** · động cơ phản lực xung · L/360 · [0.28, 0.48] | Bố cục so sánh lịch sử quân sự: BÊN TRÁI là quả tên lửa phản lực xung V-1 của Đức với cửa hút khí chớp tắt; BÊN PHẢI là cơ chế đuôi của chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói  |
| b03 | 00:14.1–00:21.5 (7.4s) | L32 | Mỗi phát bắn của con bọ thực chất là một chuỗi nổ liên thanh vi mô diễn ra với tần số điên rồ: Từ 500 lần/giây đến 1.000 lần/giây! | **500-1000Hz** · tần số nổ liên thanh · R/380 · [0.75, 0.52] | Đồng hồ đo tần số điện tử kỹ thuật số: Màn hình dao động ký hiển thị dải sóng xung nhịp răng cưa cực kỳ đều đặn, chỉ số tần số nhảy múa từ 500 lần/giây đến 1.000 lần/giây. |
| b04 | 00:21.5–00:31.0 (9.5s) | L33 | Máy quay tốc độ cao ghi lại quy trình hoàn hảo: Khi phản ứng bùng nổ, khí oxy và hơi nước nóng giãn nở cực độ sẽ tự động ép chặt chiếc van cơ học đóng lại, ngăn không cho áp suất dội ngược vào buồng chứa. |  | Hình ảnh camera quay chậm: Áp suất khí oxy bùng nổ đẩy chặt nắp van cơ học đóng khít lại; chốt khóa an toàn chặn đứng áp lực không cho dội ngược vào khoang dự trữ. |
| b05 | 00:31.0–00:34.4 (3.4s) | L34 | Sau đó, hơi sôi 100°C phụt mạnh qua nòng đuôi ra ngoài. | **100°C** · hơi nước khai hỏa · R/360 · [0.72, 0.48] | Nòng pháo đuôi của chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói khai hỏa: Luồng hơi nước sôi 100°C phụt mạnh ra ngoài thành từng xung khói trắng hình vòng tròn nối tiếp nhau như đạn |
| b06 | 00:34.4–00:41.2 (6.8s) | L35 | Ngay khi luồng hơi thoát đi, áp suất trong buồng đốt tụt xuống, van tự động mở ra hút mẻ hóa chất tiếp theo vào, và chu kỳ nổ lặp lại đúng 500 Hz! | **500 Hz** · chu kỳ tự nạp đạn · L/380 · [0.32, 0.55] | Chu kỳ hút tự động: Áp suất buồng đốt giảm mạnh tạo lực hút chân không, van tự mở ra hút mẻ hóa chất mới vào; chu kỳ lặp lại liên tục với tần số 500 Hz. |
| b07 | 00:41.2–00:45.5 (4.3s) | L36 | Đó là lý do bạn nghe thấy tiếng súng nổ lách tách liên hồi như một khẩu súng máy liên thanh! |  | Hiệu ứng âm thanh hoạt hình: Từ đuôi chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói phát ra hàng chục tia lửa kèm các chữ tượng thanh 'TÁCH! TÁCH! TÁCH!' đanh thép như súng máy liên t |
| b08 | 00:45.5–00:52.4 (6.9s) | L37 | Tôi vừa vồ thử từ phía sau một cái mà nó xoay nòng phụt thẳng vào mắt, cay xè rát bỏng húp híp suốt cả tuần lễ! |  | Chú chú chim săn mồi hoạt hình mỏ quặp hung hãn, lông vũ bay tứ tung săn mồi hoặc chú chuột to xác đang ôm mặt đau đớn, hai mắt sưng húp đỏ ửng, nước mắt ròng ròng, mỏ há hốc kêu la thảm thiết; phía xa chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn c |
| b09 | 00:52.4–00:55.2 (2.9s) | L38 | Đừng bao giờ nghĩ đến chuyện đánh lén từ sau lưng! |  | Một chú chú bọ ngựa chiến binh màu xanh lá giơ hai lưỡi kiếm răng cưa sắc bén lén lút bò rón rén lại gần từ phía sau lưng chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói; trên đầu bọ n |
| b10 | 00:55.2–01:03.0 (7.8s) | L39 | Đuôi của Pháo Thủ Hóa Học được thiết kế như một tháp pháo xe tăng bọc thép có khớp cầu xoay linh hoạt tới 270°, thậm chí gần 360°! | **270°** · tháp pháo xoay tự do · R/380 · [0.72, 0.52] | Bản vẽ tháp pháo xe tăng: Đuôi của chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói được bọc kim loại với một khớp cầu xoay linh hoạt; chiếc thước đo góc hiển thị góc xoay tự do từ 0 đế |
| b11 | 01:03.0–01:13.2 (10.1s) | L40 | Kẻ thù tấn công từ đằng trước, đằng sau, bên trái hay trên lưng, con bọ chỉ cần bẻ cong nòng đuôi qua nách hoặc qua vai là bắn trúng đích chính xác tuyệt đối mà không cần quay cả thân mình! |  | chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói không cần quay đầu: Nòng đuôi bẻ cong vòng qua nách bắn xéo một phát chính diện vào mặt kẻ tấn công phía trước; luồng hơi sôi trúng đích |
| b12 | 01:13.2–01:20.6 (7.5s) | L41 | Thậm chí các thử nghiệm với camera chụp ảnh chuyển động siêu chậm còn chứng minh: Mỗi xung nổ vi mô chỉ kéo dài từ 2-3 mili-giây! | **2-3 ms** · thời gian mỗi xung · L/360 · [0.3, 0.5] | Băng ghi hình camera siêu chậm: Một xung nổ được tua chậm từng mili-giây; đồng hồ bấm giờ hiển thị từ 2-3 mili-giây cho một lần khai hỏa trọn vẹn. |
| b13 | 01:20.6–01:26.7 (6.1s) | L42 | Tốc độ phản xạ ngắm bắn và khai hỏa của gã pháo thủ tí hon này nhanh hơn cái chớp mắt của con người tới hàng chục lần! |  | Một con mắt người hoạt hình đang chớp mắt nửa chừng; trong cùng khoảng thời gian đó chú chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói đã bắn xong hàng chục phát đạn hơi sôi vào bia n |

### scene04 · BỊ CÓC NUỐT SUỐT 1 TIẾNG VÀ MÀN NÔN ỌE TẨU THOÁT · 87.2s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:11.8 (11.8s) | L43 | Bây giờ, hãy mở hồ sơ thực chiến ngoạn mục nhất trong lịch sử sinh học, một thí nghiệm chấn động thế giới do hai nhà khoa học Shinji Sugiura và Takuya Sato thuộc Đại học Kobe Nhật Bản công bố vào năm 2018. | **NĂM 2018** · thí nghiệm chấn động · L/360 · [0.32, 0.52] | Phòng thí nghiệm Đại học Kobe Nhật Bản: Biển hiệu trường Kobe University, hai nhà khoa học Shinji Sugiura và Takuya Sato mặc áo blouse trắng đang chuẩn bị bể thí nghiệm kính. |
| b02 | 00:11.8–00:16.6 (4.8s) | L44 | Họ muốn kiểm tra: Điều gì sẽ xảy ra nếu một con cóc khổng lồ nuốt chửng Bọ Pháo Thủ vào bụng? |  | Bên trong hộp kính: Một chú chú cóc khổng lồ Nhật Bản da sần sùi màu xanh xám, mắt to tròn lồi, mồm rộng há to khổng lồ bụng bự đang ngồi đối diện chú chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi |
| b03 | 00:16.6–00:25.0 (8.3s) | L45 | Loài cóc Nhật Bản nổi tiếng là kẻ phàm ăn bậc nhất, lưỡi dính phóng ra trong chớp mắt và nuốt chửng con mồi còn sống nguyên vào dạ dày ngập tràn axit tiêu hóa. |  | Cú đớp siêu tốc: Chiếc lưỡi dài màu hồng dính nhớp của chú chú cóc khổng lồ Nhật Bản da sần sùi màu xanh xám, mắt to tròn lồi, mồm rộng há to phóng vụt ra như tia chớp, quấn chặt lấy chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp ph |
| b04 | 00:25.0–00:31.0 (6.1s) | L46 | Pháo Thủ Hóa Học bị chiếc lưỡi cóc cuốn chặt và trôi thẳng xuống đáy bao tử tối tăm! Trời ơi cứu tôi với! |  | chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói bị cuốn trôi vào họng cóc, trượt dọc theo thực quản tối tăm và rơi tõm xuống đáy hồ axit dạ dày đang sủi bọt nhớt nhầy nhụa. |
| b05 | 00:31.0–00:37.3 (6.2s) | L48 | Trong bụng tôi như có quả lựu đạn đang sôi ùng ục, nóng rát ruột gan không chịu nổi nữa rồi! |  | Mặt cắt dạ dày cóc: chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói đứng vững chãi giữa dịch vị axit, nòng pháo đuôi dựng đứng liên tục xả đạn hơi sôi 100°C vào thành dạ dày cóc. |
| b06 | 00:37.3–00:39.5 (2.2s) | L49 | Đúng như tiếng rên rỉ đau đớn của chú cóc! |  | Chú chú cóc khổng lồ Nhật Bản da sần sùi màu xanh xám, mắt to tròn lồi, mồm rộng há to toát mồ hôi đầm đìa, há mồm thở dốc, hai bàn tay ôm chặt dạ dày đang nóng ran như lò nướng bánh mì. |
| b07 | 00:39.5–00:43.2 (3.7s) | L50 | Bị nhốt trong dạ dày thiếu oxy và ngập axit, con bọ không hề chịu đầu hàng số phận. |  | chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói đội mũ bảo hộ kỹ sư hiên ngang giữa bóng tối dạ dày thiếu oxy, bình tĩnh điều chỉnh tháp pháo đuôi không hề hoảng loạn. |
| b08 | 00:43.2–00:50.3 (7.1s) | L51 | Nó bình tĩnh kích hoạt hệ thống pháo đuôi, liên tục nã đạn hóa chất sôi 100°C và xả khí Benzoquinone cay nồng thẳng vào niêm mạc dạ dày con cóc! | **100°C** · nã đạn trong dạ dày · R/380 · [0.72, 0.55] | Tia hơi hóa chất 100°C và khói độc Benzoquinone bốc mù mịt bên trong dạ dày cóc, làm niêm mạc cóc co thắt dữ dội vì cay rát. |
| b09 | 00:50.3–00:55.8 (5.5s) | L52 | Cuộc chiến nội tạng kéo dài từ 15 phút đến 107 phút, trung bình hơn 40 phút đồng hồ! | **15-107phút** · cuộc chiến sinh tử · L/360 · [0.32, 0.5]<br>**TB 40 PHÚT** · thời gian cầm cự · R/420 · [0.75, 0.58] | Đồng hồ bấm giờ cuộc chiến dạ dày: Kim đồng hồ quay từ 15 phút qua 40 phút đến mốc 107 phút; chú cóc càng lúc càng kiệt sức ngã gục xuống sàn cát. |
| b10 | 00:55.8–00:59.5 (3.7s) | L53 | Cuối cùng, con cóc không thể chịu đựng nổi những đợt nổ bỏng rát liên tiếp trong bụng. |  | Dạ dày chú cóc co bóp cực độ: Cổ họng mở toang, một luồng phản xạ nôn mửa dâng trào từ đáy bụng lên thực quản. |
| b11 | 00:59.5–01:02.1 (2.6s) | L54 | Nó há to mồm, co thắt dạ dày dữ dội |  | Chú chú cóc khổng lồ Nhật Bản da sần sùi màu xanh xám, mắt to tròn lồi, mồm rộng há to quỳ rạp xuống sàn, há hốc mồm hết cỡ, mắt nhắm nghiền chịu trận trong cơn co thắt nôn mửa dữ dội. |
| b12 | 01:02.1–01:05.0 (2.9s) | L55 | và... ọe một bãi nôn lớn ra mặt đất! |  | Một bãi dịch nôn lớn văng ra sàn nhà; chú cóc thở phào nhẹ nhõm nằm bẹp một bên với vẻ mặt sợ hãi tột cùng. |
| b13 | 01:05.0–01:13.4 (8.4s) | L56 | Và từ trong đống dịch vị nhầy nhụa đó, Pháo Thủ Hóa Học lồm cồm bò ra ngoài, phủi sạch chân, giũ cánh và ung dung bước đi như chưa từng có chuyện gì xảy ra! |  | chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói lồm cồm bò ra từ bãi dịch nôn, hai chân trước phủi sạch bùn nhớt trên mũ bảo hộ vàng, vẫy đôi cánh cứng sáng bóng bước đi hiên ngang. |
| b14 | 01:13.4–01:22.6 (9.1s) | L57 | Thống kê chấn động từ phòng thí nghiệm Kobe cho thấy: Có tới 14/16 con bọ cỡ lớn đã thoát hiểm thành công, đạt tỷ lệ sống sót từ 60-80%! | **14/16 CON** · vượt ngục thành công · L/360 · [0.3, 0.52]<br>**60-80%** · tỷ lệ sống sót · R/420 · [0.72, 0.58] | Bảng kết quả nghiên cứu Kobe: Tỷ lệ sống sót ghi nhận 14/16 con bọ (đạt 60-80%); biểu đồ cột màu xanh lá vút cao đầy ấn tượng. |
| b15 | 01:22.6–01:27.2 (4.7s) | L58 | Những con bọ này sau đó vẫn sống khỏe mạnh suốt nhiều tháng và tiếp tục sinh sản bình thường! |  | chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói cùng bạn đời và bầy ấu trùng nhỏ xíu đang vui vẻ bò trên thảm lá rừng, hoàn toàn khỏe mạnh và sung sức sau màn vượt ngục lịch sử. |

### scene05 · GIỚI HẠN KHO ĐẠN 20-30 PHÁT VÀ NGUY CƠ TỰ NỔ TUNG · 77.1s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:06.1 (6.1s) | L59 | Dù sở hữu hỏa lực tối tân như một khẩu pháo phản lực, nhưng trên đời này không có cỗ máy chiến tranh nào là hoàn hảo tuyệt đối. |  | Một chiếc bia ngắm mục tiêu quân sự bị thủng lỗ chỗ; chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói đứng cạnh một biển báo hình tam giác màu vàng cảnh báo 'GIỚI HẠN KHO ĐẠN VÀ RỦI RO  |
| b02 | 00:06.1–00:10.3 (4.1s) | L60 | Mọi kỹ sư quân sự đều biết rằng: Sức mạnh càng hủy diệt thì cái giá phải trả càng đắt |  | Bàn cân kỹ thuật: BÊN TRÁI là quả pháo nổ hủy diệt mạnh mẽ; BÊN PHẢI là chiếc đồng hồ cát đang cạn dần năng lượng, cán cân nghiêng nặng. |
| b03 | 00:10.3–00:15.1 (4.8s) | L61 | đỏ. Và điểm yếu chí mạng đầu tiên của Pháo Thủ Hóa Học chính là giới hạn của kho dự trữ đạn dược! |  | Cận cảnh buồng chứa hóa chất của chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói: Mực dung dịch chất lỏng bên trong buồng dự trữ đang tụt dần xuống đáy cạn kiệt. |
| b04 | 00:15.1–00:20.9 (5.8s) | L62 | Dung tích buồng chứa của con bọ dài 2cm chỉ đủ hóa chất cho khoảng 20-30 phát nổ liên thanh. | **20-30 PHÁT** · cơ số đạn tối đa · R/380 · [0.72, 0.55] | Hộp đạn hoạt hình: Một hộp chứa đúng 20-30 viên đạn phát sáng; mỗi phát bắn làm biến mất một viên đạn, hộp đạn dần trống rỗng. |
| b05 | 00:20.9–00:28.6 (7.7s) | L63 | Nếu gặp phải một đối thủ quá lì lợm hoặc bị bầy kiến lửa hàng ngàn con bao vây liên tục ép gã phải xả đạn không ngừng, con bọ sẽ rơi vào trạng thái cạn sạch kho đạn! |  | Tình huống vây hãm nguy hiểm: Đàn đàn kiến lửa hung hãn hàng trăm con giương càng răng cưa hàng ngàn con đỏ rực đang vây kín xung quanh chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói; |
| b06 | 00:28.6–00:32.0 (3.4s) | L64 | Thông báo từ trung tâm hậu cần: Kho đạn dự trữ đã cạn kiệt 100%! | **CẠN 100%** · kho đạn cạn kiệt · R/360 · [0.75, 0.5] | Màn hình kỹ thuật số báo động cạn kiệt: Chữ 'HẾT ĐẠN 100%' nhấp nháy đỏ rực; chiếc kim xăng chỉ về vạch E rỗng không. |
| b07 | 00:32.0–00:37.8 (5.7s) | L65 | Cần tối thiểu 24 tiếng để tổng hợp lại hóa chất! Chuẩn xác như bản tin hậu cần! | **24-36 GIỜ** · thời gian nạp đạn · L/380 · [0.32, 0.55] | Một chiếc đồng hồ đếm ngược nạp đạn: Kim đồng hồ chỉ mốc 24 tiếng đến 36 tiếng; chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói đeo băng quấn đầu nghỉ ngơi dưỡng sức. |
| b08 | 00:37.8–00:46.6 (8.8s) | L67 | Sau khi bắn hết cơ số đạn, Pháo Thủ Hóa Học mất từ 24 tiếng đến 36 tiếng ăn uống cật lực để cơ thể tái tổng hợp lại đủ lượng Hydroquinone và Hydrogen peroxide. |  | Bên trong cơ thể chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói: Hai buồng chứa hóa chất đang từ từ được nhỏ từng giọt Hydroquinone và Hydrogen peroxide mới tổng hợp vào bình chứa. |
| b09 | 00:46.6–00:51.9 (5.3s) | L68 | Trong suốt khoảng thời gian nạp đạn này, gã hoàn toàn trở thành một con bọ cánh cứng yếu ớt không tấc sắt trong tay! |  | chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói lấm lét nấp dưới một chiếc lá mục khô, hai tay ôm đầu; một chú thằn lằn đi ngang qua phía trên khiến chú Bọ Pháo Thủ (Bombardier Beetle) |
| b10 | 00:51.9–00:56.1 (4.3s) | L69 | Chưa hết, gã béo tí hon này còn mang trên mình số phận của một thùng thuốc nổ di động! |  | chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói biến thành hình một thùng thuốc nổ TNT có dây ngòi cháy dở; bước đi rón rén từng bước nhẹ nhàng như giẫm trên trứng mỏng. |
| b11 | 00:56.1–01:05.6 (9.5s) | L70 | Nếu bị một kẻ thù to xác giẫm mạnh làm vỡ vách ngăn giữa 2 buồng hóa chất khi van an toàn chưa kịp mở, phản ứng tỏa nhiệt sẽ xảy ra ngay bên trong cơ thể và nổ tung con bọ thành từng mảnh vụn! | **2 BUỒNG VỠ** · nguy cơ tự hủy · R/380 · [0.72, 0.55] | Vụ nổ tự hủy giả định: Bức tường ngăn giữa 2 buồng bị nứt vỡ; phản ứng tỏa nhiệt bùng nổ ngay trong ruột khiến khói bốc nghi ngút quanh mình chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc  |
| b12 | 01:05.6–01:09.2 (3.6s) | L71 | Sống bên cạnh cái chết mỗi ngày, đó là sự đánh đổi khắc nghiệt của tự nhiên. |  | chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói đứng trên một sợi dây thừng mảnh bắc qua vực sâu; một bên là ngọn lửa bỏng rát, một bên là bóng tối săn mồi; thần thái điềm đạm cân bằng |
| b13 | 01:09.2–01:17.1 (7.9s) | L72 | Bởi vậy, bài học sinh tồn đầu tiên của loài bọ này không phải là bắn bừa bãi, mà là ngắm thật kỹ, bắn thật chuẩn và chỉ khai hỏa khi thật sự bị dồn vào bước đường cùng! |  | chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói đứng nghiêm trang như xạ thủ bắn tỉa chuyên nghiệp, một mắt nheo lại ngắm qua kính ngắm; nòng pháo đuôi khóa chặt mục tiêu chuẩn xác 100 |

### scene06 · ỨNG DỤNG CÔNG NGHỆ VÀ BÓNG ĐEN TẬP SAU · 76.5s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:05.5 (5.5s) | L73 | Nhìn vào Pháo Thủ Hóa Học, các kỹ sư cơ khí hàng đầu thế giới đã học được những bài học vô giá. |  | Viện nghiên cứu kỹ thuật hàng không: Các kỹ sư mặc áo bảo hộ đang quan sát chú chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói trên bàn thí nghiệm; phía sau là màn hình mô phỏng dòng k |
| b02 | 00:05.5–00:18.9 (13.4s) | L74 | Cấu tạo van một chiều và cơ chế phun xung nhiệt độ cao của loài bọ này hiện đang được các nhà khoa học mô phỏng để chế tạo các loại bình xịt thuốc y tế hạt siêu mịn, hệ thống dập lửa cứu hỏa siêu tốc, và thậm chí là động cơ tái khởi động cho các tàu vũ trụ thế hệ mới! |  | Các ứng dụng công nghệ mô phỏng sinh học: Một bình xịt y tế phun sương siêu mịn, một vòi phun cứu hỏa dập lửa bọt tuyết, và một động cơ đẩy tên lửa vũ trụ mini. |
| b03 | 00:18.9–00:21.0 (2.1s) | L75 | Tự nhiên chính là người thầy vĩ đại nhất. |  | Một cuốn sách mở lớn giữa khu rừng xanh tươi: Mẹ Thiên Nhiên đội vương miện lá cây đang mỉm cười trao tặng bằng sáng chế phát minh cho chú chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc kh |
| b04 | 00:21.0–00:33.3 (12.3s) | L76 | Một sinh vật nhỏ bé bằng hạt lạc, không cần móng vuốt hay kích thước khổng lồ, chỉ cần kết hợp hài hòa giữa cấu trúc cơ khí tinh vi và hóa học chuẩn xác, đã có thể hiên ngang tồn tại suốt hàng triệu năm giữa muôn vàn kẻ săn mồi đẫm máu. |  | chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói đứng kiêu hãnh trên đỉnh một viên đá cuội phủ rêu; xung quanh các loài chim săn mồi và bọ ngựa đều giữ khoảng cách nể sợ; ánh hoàng hôn  |
| b05 | 00:33.3–00:42.6 (9.3s) | L77 | Bạn ấn tượng nhất với điều gì ở Pháo Thủ Hóa Học: Khả năng đun sôi hóa chất lên 100°C trong tích tắc, hay màn thoát thân không tưởng sau 1 tiếng nằm trong dạ dày cóc? | **PHÁO 100°C** · lựa chọn 1 · L/380 · [0.28, 0.52]<br>**THOÁT CÓC** · lựa chọn 2 · R/380 · [0.72, 0.52] | Khung hình tương tác hai lựa chọn thú vị: BÊN TRÁI là khẩu pháo xịt hơi sôi 100°C; BÊN PHẢI là màn tẩu thoát khỏi dạ dày cóc sau 1 tiếng; chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khó |
| b06 | 00:42.6–00:44.9 (2.3s) | L78 | Hãy để lại bình luận chia sẻ cùng chúng tôi nhé! |  | Hộp bình luận YouTube hoạt hình rực rỡ: Hàng chục biểu tượng ngọn lửa, tia chớp và bình luận 'BỌ PHÁO THỦ BÁ ĐẠO!' đang bay lên lung linh. |
| b07 | 00:44.9–00:47.8 (2.9s) | L79 | Và bây giờ, hãy hướng ngòi bút về phân cảnh kết thúc bí |  | Bàn vẽ chuyển màu từ rừng cây sang màu vàng cát bỏng rát của sa mạc hoang vu; ngòi bút vẽ tay lướt êm ái trên mặt giấy mở ra một vùng đất mới. |
| b08 | 00:47.8–00:54.1 (6.3s) | L80 | ẩn! Trong tập tiếp theo, chúng ta sẽ rời khỏi thảm rừng ẩm ướt để tiến vào vùng sa mạc khô hạn bậc nhất hành tinh. |  | Toàn cảnh sa mạc Úc mênh mông cát đỏ bỏng rát: Những cồn cát nhấp nhô dưới ánh mặt trời thiêu đốt; không khí bốc hơi mờ ảo đầy khắc nghiệt. |
| b09 | 00:54.1–00:57.7 (3.6s) | L81 | Nơi đây có một bóng đen bí ẩn toàn thân phủ đầy gai nhọn sắc bén như bãi chông di |  | BÓNG ĐEN HOÀN TOÀN (solid black silhouette) của một sinh vật kỳ dị toàn thân chi chít gai nhọn như quả cầu gai hay bãi chông di động, viền hào quang vàng cam sa mạc phát sáng bí ẩn. |
| b10 | 00:57.7–01:10.3 (12.6s) | L82 | động! Sinh vật kỳ dị này có siêu năng lực uống nước bằng chính da bàn chân qua hệ thống ống mao dẫn, có một chiếc đầu giả sau gáy để đánh lừa kẻ thù, và đặc biệt là vũ khí phòng vệ tối thượng: Bắn ra một tia máu đỏ lòm thẳng từ hốc mắt xa tới 1m để làm mù kẻ săn | **BẮN XA 1M** · tia máu từ mắt · R/380 · [0.75, 0.48] | Đặc tả bóng đen bí ẩn: Bàn chân giẫm lên giọt sương và nước tự hút ngược lên cơ thể; phía sau gáy có một chiếc đầu giả nhô lên; và từ hốc mắt bắn ra một tia máu đỏ thẳng tắp xa tới 1m. |
| b11 | 01:10.3–01:13.5 (3.3s) | L83 | mồi! Đố bạn biết danh tính của quái kiệt sa mạc gai góc này là ai? |  | BÓNG ĐEN BÍ ẨN (solid black silhouette) của quái kiệt gai góc nổi bật ở GIỮA; trên đầu là DẤU HỎI CHẤM LỚN MÀU ĐỎ phát sáng rực rỡ; dòng chữ 'ĐOÁN TÊN CON VẬT TẬP 19' lung linh. |
| b12 | 01:13.5–01:16.5 (3.0s) | L84 | Hãy để lại phán đoán của bạn bên dưới phần bình luận nhé! |  | Khung cảnh kết thúc hồi hộp: Chiếc cọ vẽ vàng chấm một giọt mực bí ẩn xuống mặt giấy trắng, để lại dấu hỏi lớn kích thích trí tò mò tột độ của khán giả. |

## 5. Phân cảnh Shorts — từng beat

Banner: **BỊ CÓC NUỐT 1 TIẾNG / VẪN BẮN PHÁO THOÁT THÂN?!** · giọng 48.0s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Bị cóc nuốt chửng vào dạ dày suốt 1 tiếng đồng hồ, con bọ nhỏ bé này đã làm gì để thoát thân còn sống nguyên vẹn? | **1 TIẾNG** · mắc kẹt trong dạ dày · L/580 · [0.32, 0.55] |
| s02 | 00:06.1 | S02 | Đây là Bọ Pháo Thủ, gã tí hon dài chỉ 2cm nhưng sở hữu khẩu đại bác hóa học đáng sợ nhất thế giới côn trùng! | **2cm** · kích thước tí hon · R/580 · [0.7, 0.52] |
| s03 | 00:12.8 | S03 | Bên trong bụng gã là 2 buồng hóa chất riêng biệt chứa Hydroquinone và Hydrogen peroxide. |  |
| s04 | 00:17.5 | S04 | Khi bị đe dọa, con bọ mở van xả hóa chất vào buồng đốt chứa enzyme xúc tác, |  |
| s05 | 00:21.7 | S05 | đun sôi dung dịch lên đúng 100°C và kích hoạt phản ứng nổ liên thanh 500 lần/giây! | **100°C** · nhiệt độ sôi · L/560 · [0.3, 0.48]<br>**500 Hz** · nổ liên thanh · R/620 · [0.72, 0.55] |
| s06 | 00:26.9 | S06 | Tia hơi hóa chất sôi sùng sục và cay xé da bắn ra với vận tốc 20 m/s | **20 m/s** · vận tốc xé gió · R/580 · [0.68, 0.52] |
| s07 | 00:31.4 | S07 | từ chiếc tháp pháo xoay 270° ở đuôi! | **270°** · tháp pháo xoay tự do · L/580 · [0.32, 0.5] |
| s08 | 00:33.9 | S08 | Kể cả khi bị cóc nuốt vào bụng, Pháo Thủ Hóa Học vẫn bình tĩnh nã đạn liên tiếp trong dạ dày |  |
| s09 | 00:38.6 | S09 | khiến con cóc đau đớn dữ dội và phải nôn ọe gã ra ngoài sau 40 phút! | **40 PHÚT** · thời gian nôn mửa · R/600 · [0.72, 0.55] |
| s10 | 00:42.5 | S10 | Nhỏ bé nhưng sở hữu kỹ thuật cơ khí đỉnh cao, |  |
| s11 | 00:45.2 | S11 | đó chính là bí thuật sinh tồn bất bại của Bọ Pháo Thủ! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo thử nghiệm vũ khí tối mật cấp độ đỏ.". Bố cục: Phòng thí nghiệm quân sự tối mật: Một chiếc bàn kim loại có đèn rọi chiếu sáng, xung quanh là các bản vẽ vũ khí tối mật dán trên tường; một tấm biển đỏ đề 'BÁO CÁO THỬ NGHIỆM CẤP ĐỘ ĐỎ'. KHÔNG có chú Bọ Pháo Thủ trong cảnh này.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mở khóa toàn bộ dữ liệu lưu trữ của kho vũ khí sinh học!". Bố cục: Một chiếc két sắt thép dày nặng nề đang mở khóa tung ra, bên trong tỏa ra ánh sáng xanh lam huyền bí của dữ liệu vũ khí sinh học lưu trữ; các tập hồ sơ bay lượn. KHÔNG có chú Bọ Pháo Thủ trong cảnh này.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Toàn đội kỹ thuật hãy trang bị đầy đủ kính chắn nhiệt và mặt nạ phòng độc, bởi vì cỗ máy phòng vệ mà chúng ta tháo dỡ hôm nay sở hữu công nghệ cơ khí vượt xa trí tưởng tượng của con người.". Bố cục: BÊN TRÁI là các chuyên viên kỹ thuật hoạt hình đang vội vã đeo kính chắn nhiệt và mặt nạ phòng độc; BÊN PHẢI là đồng hồ đo nhiệt độ báo động đỏ rực. KHÔNG có chú Bọ Pháo Thủ trong cảnh này.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Quên đi những nọc độc rắn hổ hay gai nhọn bọ cạp, hãy nhìn vào một sinh vật nhỏ bé đang lững thững bò trên thảm lá rừng mục!". Bố cục: BÊN TRÁI là chiếc đầu rắn hổ mang bành nhe răng nanh và chiếc đuôi bọ cạp bị gạch chéo đỏ lớn; BÊN PHẢI là thảm lá mục rừng nhiệt đới bí ẩn với ánh nắng le lói rọi xuống một đốm sáng nhỏ.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đối tượng mang mã định danh số 18 của chúng ta có ngoại hình đánh lừa thị giác tuyệt đối: Chiều dài cơ thể chỉ vỏn vẹn từ 1,5cm đến 2,5cm, nặng chưa đầy một gam, đầu và chân màu cam đất, đôi cánh cứng màu xanh đen ánh kim.". Bố cục: Chân dung cận cảnh của chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói: một chú bọ cánh cứng nhỏ xíu đứng cạnh một chiếc thước dây đo chiều dài từ 1,5cm đến 2,5cm; thân màu xanh đen ánh kim, đầu và chân màu cam đất, đội mũ bảo hộ kỹ sư vàng oai phong.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhìn bề ngoài, gã chẳng khác nào một chú bọ cánh cứng tầm thường mà bạn có thể vô tình giẫm phải trên lối đi.". Bố cục: Góc nhìn từ trên cao xuống lối mòn rừng: Một chiếc đế giày leo núi khổng lồ đang bước xuống sát sạt chú chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói; chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói ngước nhìn lên với vẻ mặt bình thản không chút sợ hãi.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng trong danh mục vũ khí sinh học, giới khoa học quân sự đặt cho gã một biệt danh đầy nể sợ: Pháo Thủ Hóa Học, hay còn gọi là Bọ Pháo Thủ!". Bố cục: Hồ sơ vũ khí sinh học: Một tấm thẻ định danh quân sự có in ảnh chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói cùng dòng chữ lớn 'PHÁO THỦ HÓA HỌC'; bên cạnh là huy hiệu biểu tượng đầu lâu có khói bốc lên.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi khi bị kẻ thù đe dọa, đuôi của con bọ này sẽ lập tức phát nổ liên thanh với tiếng nổ tanh tách đanh thép, bắn ra một luồng hơi hóa chất độc hại sôi sùng sục ở đúng 100°C!". Bố cục: chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói kích hoạt vũ khí ở đuôi: Một tiếng nổ chói tai phát ra từ đuôi, luồng khói và hơi nước sôi 100°C bắn phụt ra như pháo cao xạ, tia nhiệt phát sáng cam đỏ rực rỡ.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy tưởng tượng bạn đang bị một tia nước sôi 100°C, đậm đặc hóa chất ăn mòn da bắn thẳng vào mắt với vận tốc lên tới 20 m/s!". Bố cục: Góc nhìn thứ nhất cực kỳ kịch tính: Tia nước sôi 100°C bắn thẳng về phía ống kính với tốc độ 20 m/s xé gió, hơi nước trắng xóa bốc lên mù mịt kèm các giọt hóa chất ăn mòn phát sáng.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bất kỳ loài chim săn mồi, thằn lằn hay nhện khổng lồ nào lỡ dại chạm vào Pháo Thủ Hóa Học đều phải giật bắn người, bỏng rát mắt và tháo chạy trong hoảng loạn.". Bố cục: Cảnh tượng săn mồi hỗn loạn: BÊN TRÁI chú chú chim săn mồi hoạt hình mỏ quặp hung hãn, lông vũ bay tứ tung mỏ quặp bị trúng luồng hơi sôi đang giật bắn mình nhắm tịt mắt, lông đầu bốc khói; một con thằn lằn bên cạnh cuống cuồng tháo chạy.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vậy điều kỳ diệu nào giúp một cơ thể sống mỏng manh dài chỉ 2cm có thể đun sôi nước đến 100°C chỉ trong vài phần nghìn giây mà không hề bị nổ tung chính bản thân mình?". Bố cục: chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói đứng ở GIỮA trên nền trắng, cơ thể 2cm nhỏ bé nguyên vẹn mỉm cười; một chiếc nhiệt kế khổng lồ bên cạnh chỉ vọt lên mốc 100°C màu đỏ rực; hai bên là dấu hỏi chấm lớn.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy cùng mở bản vẽ kỹ thuật bên trong cơ thể gã!". Bố cục: Bàn làm việc của kỹ sư: Một bản vẽ thiết kế cơ khí màu xanh lam (blueprint) trải rộng ra, hiển thị các đường nét kỹ thuật của bụng chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói với các mũi tên chỉ vào các buồng chứa bí mật.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Dưới kính hiển vi điện tử quét X-quang tốc độ cao của Viện Công nghệ MIT, cấu trúc bên trong phần bụng của Pháo Thủ Hóa Học hiện ra hệt như một nhà máy sản xuất vũ khí hóa học thu nhỏ!". Bố cục: Phòng thí nghiệm synchrotron công nghệ cao: Kính hiển vi điện tử quét X-quang tốc độ cao đang chiếu chùm tia sáng quét qua cơ thể chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói; màn hình máy tính hiển thị mô hình 3D cắt lớp khoang bụng.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Điểm cốt lõi giúp con bọ không bị tự hủy nằm ở nguyên lý vũ khí nhị phân: Tách biệt hoàn toàn hai chất phản ứng cho đến giây phút khai hỏa.". Bố cục: Sơ đồ nguyên lý vũ khí nhị phân: Hai bình chứa hóa chất riêng biệt đặt song song, ở giữa có bức tường ngăn cách bằng thép kiên cố; biểu tượng an toàn màu xanh lá lấp lánh.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ở phần trên của khoang bụng là buồng chứa dự trữ lớn.". Bố cục: Đặc tả buồng dự trữ lớn ở bụng trên của chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói: Một khoang chứa hình quả thận trong suốt, bên trong chứa đầy dung dịch lỏng trong vắt không màu, thành vách mềm mại.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Buồng này chứa hỗn hợp hai chất lỏng: 10% Hydroquinone và 25% Hydrogen peroxide, hay chính là nước oxy già đậm đặc.". Bố cục: Phân tích hóa học: Hai ống nghiệm dán nhãn; BÊN TRÁI là ống 10% Hydroquinone, BÊN PHẢI là ống 25% Hydrogen peroxide (nước oxy già); hai chất hòa vào nhau trong bình thủy tinh mà không có phản ứng.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi hai chất này nằm chung trong buồng chứa, chúng hoàn toàn trơ lỳ và hòa bình với nhau, không hề xảy ra bất kỳ phản ứng cháy nổ nào.". Bố cục: Hai phân tử hóa học hoạt hình dễ thương đang bắt tay nhau hòa bình, nở nụ cười hiền lành bên trong khoang bụng của chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói, không có một tia lửa hay bong bóng khí nào.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cảnh báo nhiệt độ buồng đốt đạt ngưỡng tới hạn 100°C!". Bố cục: Màn hình bảng điều khiển kỹ thuật nhấp nháy đèn đỏ báo động: Cột nhiệt kế nhảy vọt lên 100°C; kim đồng hồ áp suất rung lắc dữ dội ở vùng nguy hiểm màu đỏ.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Áp suất oxy tăng vọt, đề nghị khóa van an toàn ngay lập tức!". Bố cục: Hình ảnh van cơ học cảnh báo: Một chiếc van kim loại màu vàng đang bị áp lực khí nén đẩy căng phồng, trợ lý kỹ thuật hoạt hình đang cuống cuồng xoay vô-lăng van khóa an toàn.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đúng như trợ lý kỹ thuật vừa báo cáo!". Bố cục: chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói đội mũ kỹ sư mỉm cười tự tin, cầm chiếc mỏ lết chỉ vào cơ chế van tự động bên trong cơ thể mình; các bánh răng cơ khí ăn khớp hoàn hảo.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nối giữa buồng chứa dự trữ và buồng đốt bên ngoài là một chiếc van cơ học một chiều cực kỳ tinh xảo.". Bố cục: Cận cảnh cấu trúc van cơ học một chiều: Ống dẫn hẹp nối buồng dự trữ với buồng đốt, van có lá chắn đàn hồi chỉ cho chất lỏng chảy theo một chiều từ trên xuống dưới.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi con bọ siết chặt cơ bụng, van mở ra, đẩy một lượng nhỏ hỗn hợp lỏng tràn vào buồng phản ứng thứ hai.". Bố cục: chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói siết cơ bụng màu cam đất: Khoang bụng co lại ép một giọt dung dịch lỏng màu xanh ngọc chảy qua khe van, rơi tọt xuống buồng đốt nhỏ phía dưới.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tại buồng đốt thứ hai này, thành vách được gia cố bằng một lớp màng chất sừng cu-tin dày đặc, chịu nhiệt và chống ăn mòn siêu cấp.". Bố cục: Bên trong buồng đốt thứ hai: Thành vách buồng được lót bằng lớp màng sừng cutin dày cộp màu nâu đậm, bóng loáng và kiên cố như lớp gạch chịu nhiệt của lò luyện thép.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nơi đây đã được nạp sẵn hai enzyme xúc tác sinh học cực mạnh: Catalase và Peroxidase!". Bố cục: Hai chú enzyme hoạt hình ngộ nghĩnh: Enzyme Catalase đội mũ công nhân cầm kéo sắc bén, và enzyme Peroxidase mang bình oxy đang đứng chờ sẵn trong buồng đốt.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ngay khoảnh khắc giọt dung dịch chạm vào enzyme, phản ứng dây chuyền bùng nổ trong chớp mắt!". Bố cục: Vụ nổ dây chuyền bùng phát: Giọt dung dịch chạm vào mặt enzyme liền lóe sáng chói lòa như pháo hoa, bọt khí sôi ùng ục, các tia lửa nhiệt lượng tỏa ra dữ dội.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Enzyme Catalase lập tức bẻ gãy Hydrogen peroxide thành nước và khí oxy, giải phóng một lượng nhiệt khổng lồ đun sôi dung dịch lên đúng 100°C!". Bố cục: Sơ đồ phản ứng hóa học bùng nổ: Hydrogen peroxide bị bẻ đôi thành H2O và bọt khí Oxy bốc hơi cuồn cuộn; ngọn lửa nhiệt lượng 100°C bùng cháy rực rỡ.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đồng thời, enzyme Peroxidase oxy hóa Hydroquinone thành chất Benzoquinone, một chất hóa học cực độc, cay xé da thịt và có mùi khét lẹt!". Bố cục: Chất độc Benzoquinone hình thành: Một đám mây khí màu nâu vàng cay xè, bốc khói khét lẹt kèm các biểu tượng mắt cay xè toát ra từ dung dịch đang sôi.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Toàn bộ chuỗi phản ứng sinh hóa dữ dội này diễn ra trong khoang thể tích tí hon chưa đầy một phần 10mm khối!". Bố cục: So sánh kích thước siêu vi mô: Một chiếc đầu kim may khổng lồ, trên đầu kim là buồng đốt tí hon của chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói đang phát sáng; kích thước chỉ 1/10 mm³ cực nhỏ.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhờ lớp vỏ chitin cách nhiệt nhiều lớp bọc ngoài buồng đốt, các cơ quan nội tạng nhạy cảm khác như tim và ruột của Pháo Thủ Hóa Học hoàn toàn không bị ảnh hưởng bởi lò lửa 100°C đang sôi sùng sục ngay sát bên cạnh.". Bố cục: Mặt cắt cách nhiệt hoàn hảo: Lớp vỏ chitin nhiều tầng cách nhiệt bao quanh buồng đốt đỏ rực; bên ngoài là trái tim và nội tạng của chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói vẫn mát rượi màu xanh êm dịu.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu Pháo Thủ Hóa Học chỉ đơn thuần phun ra một dòng nước sôi liên tục, áp suất khổng lồ sẽ xé toạc bụng gã hoặc đẩy ngược cơ thể gã văng xa cả mét.". Bố cục: Tình huống giả định hài hước: Nếu xịt nước sôi liên tục, cơ thể chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói bị lực phản lực đẩy lùi văng xa tít tắp, xoay mòng mòng như quả bóng bay xì hơi trên mặt đất.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng tạo hóa đã ban cho gã một phát minh cơ khí tương tự như động cơ tên lửa phản lực xung V-1 của Đức trong Thế chiến II!". Bố cục: Bố cục so sánh lịch sử quân sự: BÊN TRÁI là quả tên lửa phản lực xung V-1 của Đức với cửa hút khí chớp tắt; BÊN PHẢI là cơ chế đuôi của chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói có cấu trúc động cơ tương tự.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi phát bắn của con bọ thực chất là một chuỗi nổ liên thanh vi mô diễn ra với tần số điên rồ: Từ 500 lần/giây đến 1.000 lần/giây!". Bố cục: Đồng hồ đo tần số điện tử kỹ thuật số: Màn hình dao động ký hiển thị dải sóng xung nhịp răng cưa cực kỳ đều đặn, chỉ số tần số nhảy múa từ 500 lần/giây đến 1.000 lần/giây.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Máy quay tốc độ cao ghi lại quy trình hoàn hảo: Khi phản ứng bùng nổ, khí oxy và hơi nước nóng giãn nở cực độ sẽ tự động ép chặt chiếc van cơ học đóng lại, ngăn không cho áp suất dội ngược vào buồng chứa.". Bố cục: Hình ảnh camera quay chậm: Áp suất khí oxy bùng nổ đẩy chặt nắp van cơ học đóng khít lại; chốt khóa an toàn chặn đứng áp lực không cho dội ngược vào khoang dự trữ.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sau đó, hơi sôi 100°C phụt mạnh qua nòng đuôi ra ngoài.". Bố cục: Nòng pháo đuôi của chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói khai hỏa: Luồng hơi nước sôi 100°C phụt mạnh ra ngoài thành từng xung khói trắng hình vòng tròn nối tiếp nhau như đạn súng máy.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ngay khi luồng hơi thoát đi, áp suất trong buồng đốt tụt xuống, van tự động mở ra hút mẻ hóa chất tiếp theo vào, và chu kỳ nổ lặp lại đúng 500 Hz!". Bố cục: Chu kỳ hút tự động: Áp suất buồng đốt giảm mạnh tạo lực hút chân không, van tự mở ra hút mẻ hóa chất mới vào; chu kỳ lặp lại liên tục với tần số 500 Hz.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đó là lý do bạn nghe thấy tiếng súng nổ lách tách liên hồi như một khẩu súng máy liên thanh!". Bố cục: Hiệu ứng âm thanh hoạt hình: Từ đuôi chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói phát ra hàng chục tia lửa kèm các chữ tượng thanh 'TÁCH! TÁCH! TÁCH!' đanh thép như súng máy liên thanh đang nã đạn.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tôi vừa vồ thử từ phía sau một cái mà nó xoay nòng phụt thẳng vào mắt, cay xè rát bỏng húp híp suốt cả tuần lễ!". Bố cục: Chú chú chim săn mồi hoạt hình mỏ quặp hung hãn, lông vũ bay tứ tung săn mồi hoặc chú chuột to xác đang ôm mặt đau đớn, hai mắt sưng húp đỏ ửng, nước mắt ròng ròng, mỏ há hốc kêu la thảm thiết; phía xa chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói đứng ngắm nhìn.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đừng bao giờ nghĩ đến chuyện đánh lén từ sau lưng!". Bố cục: Một chú chú bọ ngựa chiến binh màu xanh lá giơ hai lưỡi kiếm răng cưa sắc bén lén lút bò rón rén lại gần từ phía sau lưng chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói; trên đầu bọ ngựa hiện lên bóng mây tưởng tượng chuẩn bị vồ mồi ngon lành.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đuôi của Pháo Thủ Hóa Học được thiết kế như một tháp pháo xe tăng bọc thép có khớp cầu xoay linh hoạt tới 270°, thậm chí gần 360°!". Bố cục: Bản vẽ tháp pháo xe tăng: Đuôi của chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói được bọc kim loại với một khớp cầu xoay linh hoạt; chiếc thước đo góc hiển thị góc xoay tự do từ 0 đến 270° quanh cơ thể.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kẻ thù tấn công từ đằng trước, đằng sau, bên trái hay trên lưng, con bọ chỉ cần bẻ cong nòng đuôi qua nách hoặc qua vai là bắn trúng đích chính xác tuyệt đối mà không cần quay cả thân mình!". Bố cục: chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói không cần quay đầu: Nòng đuôi bẻ cong vòng qua nách bắn xéo một phát chính diện vào mặt kẻ tấn công phía trước; luồng hơi sôi trúng đích 100% cực kỳ điêu luyện.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thậm chí các thử nghiệm với camera chụp ảnh chuyển động siêu chậm còn chứng minh: Mỗi xung nổ vi mô chỉ kéo dài từ 2-3 mili-giây!". Bố cục: Băng ghi hình camera siêu chậm: Một xung nổ được tua chậm từng mili-giây; đồng hồ bấm giờ hiển thị từ 2-3 mili-giây cho một lần khai hỏa trọn vẹn.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tốc độ phản xạ ngắm bắn và khai hỏa của gã pháo thủ tí hon này nhanh hơn cái chớp mắt của con người tới hàng chục lần!". Bố cục: Một con mắt người hoạt hình đang chớp mắt nửa chừng; trong cùng khoảng thời gian đó chú chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói đã bắn xong hàng chục phát đạn hơi sôi vào bia ngắm.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bây giờ, hãy mở hồ sơ thực chiến ngoạn mục nhất trong lịch sử sinh học, một thí nghiệm chấn động thế giới do hai nhà khoa học Shinji Sugiura và Takuya Sato thuộc Đại học Kobe Nhật Bản công bố vào năm 2018.". Bố cục: Phòng thí nghiệm Đại học Kobe Nhật Bản: Biển hiệu trường Kobe University, hai nhà khoa học Shinji Sugiura và Takuya Sato mặc áo blouse trắng đang chuẩn bị bể thí nghiệm kính.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Họ muốn kiểm tra: Điều gì sẽ xảy ra nếu một con cóc khổng lồ nuốt chửng Bọ Pháo Thủ vào bụng?". Bố cục: Bên trong hộp kính: Một chú chú cóc khổng lồ Nhật Bản da sần sùi màu xanh xám, mắt to tròn lồi, mồm rộng há to khổng lồ bụng bự đang ngồi đối diện chú chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói tí hon; trên đầu cả hai là dấu hỏi chấm lớn đầy hồi hộp.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Loài cóc Nhật Bản nổi tiếng là kẻ phàm ăn bậc nhất, lưỡi dính phóng ra trong chớp mắt và nuốt chửng con mồi còn sống nguyên vào dạ dày ngập tràn axit tiêu hóa.". Bố cục: Cú đớp siêu tốc: Chiếc lưỡi dài màu hồng dính nhớp của chú chú cóc khổng lồ Nhật Bản da sần sùi màu xanh xám, mắt to tròn lồi, mồm rộng há to phóng vụt ra như tia chớp, quấn chặt lấy chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói trong chớp mắt.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Pháo Thủ Hóa Học bị chiếc lưỡi cóc cuốn chặt và trôi thẳng xuống đáy bao tử tối tăm! Trời ơi cứu tôi với!". Bố cục: chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói bị cuốn trôi vào họng cóc, trượt dọc theo thực quản tối tăm và rơi tõm xuống đáy hồ axit dạ dày đang sủi bọt nhớt nhầy nhụa.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong bụng tôi như có quả lựu đạn đang sôi ùng ục, nóng rát ruột gan không chịu nổi nữa rồi!". Bố cục: Mặt cắt dạ dày cóc: chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói đứng vững chãi giữa dịch vị axit, nòng pháo đuôi dựng đứng liên tục xả đạn hơi sôi 100°C vào thành dạ dày cóc.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đúng như tiếng rên rỉ đau đớn của chú cóc!". Bố cục: Chú chú cóc khổng lồ Nhật Bản da sần sùi màu xanh xám, mắt to tròn lồi, mồm rộng há to toát mồ hôi đầm đìa, há mồm thở dốc, hai bàn tay ôm chặt dạ dày đang nóng ran như lò nướng bánh mì.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bị nhốt trong dạ dày thiếu oxy và ngập axit, con bọ không hề chịu đầu hàng số phận.". Bố cục: chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói đội mũ bảo hộ kỹ sư hiên ngang giữa bóng tối dạ dày thiếu oxy, bình tĩnh điều chỉnh tháp pháo đuôi không hề hoảng loạn.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó bình tĩnh kích hoạt hệ thống pháo đuôi, liên tục nã đạn hóa chất sôi 100°C và xả khí Benzoquinone cay nồng thẳng vào niêm mạc dạ dày con cóc!". Bố cục: Tia hơi hóa chất 100°C và khói độc Benzoquinone bốc mù mịt bên trong dạ dày cóc, làm niêm mạc cóc co thắt dữ dội vì cay rát.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cuộc chiến nội tạng kéo dài từ 15 phút đến 107 phút, trung bình hơn 40 phút đồng hồ!". Bố cục: Đồng hồ bấm giờ cuộc chiến dạ dày: Kim đồng hồ quay từ 15 phút qua 40 phút đến mốc 107 phút; chú cóc càng lúc càng kiệt sức ngã gục xuống sàn cát.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cuối cùng, con cóc không thể chịu đựng nổi những đợt nổ bỏng rát liên tiếp trong bụng.". Bố cục: Dạ dày chú cóc co bóp cực độ: Cổ họng mở toang, một luồng phản xạ nôn mửa dâng trào từ đáy bụng lên thực quản.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó há to mồm, co thắt dạ dày dữ dội và...". Bố cục: Chú chú cóc khổng lồ Nhật Bản da sần sùi màu xanh xám, mắt to tròn lồi, mồm rộng há to quỳ rạp xuống sàn, há hốc mồm hết cỡ, mắt nhắm nghiền chịu trận trong cơn co thắt nôn mửa dữ dội.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "ọe một bãi nôn lớn ra mặt đất!". Bố cục: Một bãi dịch nôn lớn văng ra sàn nhà; chú cóc thở phào nhẹ nhõm nằm bẹp một bên với vẻ mặt sợ hãi tột cùng.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và từ trong đống dịch vị nhầy nhụa đó, Pháo Thủ Hóa Học lồm cồm bò ra ngoài, phủi sạch chân, giũ cánh và ung dung bước đi như chưa từng có chuyện gì xảy ra!". Bố cục: chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói lồm cồm bò ra từ bãi dịch nôn, hai chân trước phủi sạch bùn nhớt trên mũ bảo hộ vàng, vẫy đôi cánh cứng sáng bóng bước đi hiên ngang.
```
</details>

<details><summary>L57</summary>

```text
HÌNH L57 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thống kê chấn động từ phòng thí nghiệm Kobe cho thấy: Có tới 14/16 con bọ cỡ lớn đã thoát hiểm thành công, đạt tỷ lệ sống sót từ 60-80%!". Bố cục: Bảng kết quả nghiên cứu Kobe: Tỷ lệ sống sót ghi nhận 14/16 con bọ (đạt 60-80%); biểu đồ cột màu xanh lá vút cao đầy ấn tượng.
```
</details>

<details><summary>L58</summary>

```text
HÌNH L58 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Những con bọ này sau đó vẫn sống khỏe mạnh suốt nhiều tháng và tiếp tục sinh sản bình thường!". Bố cục: chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói cùng bạn đời và bầy ấu trùng nhỏ xíu đang vui vẻ bò trên thảm lá rừng, hoàn toàn khỏe mạnh và sung sức sau màn vượt ngục lịch sử.
```
</details>

<details><summary>L59</summary>

```text
HÌNH L59 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Dù sở hữu hỏa lực tối tân như một khẩu pháo phản lực, nhưng trên đời này không có cỗ máy chiến tranh nào là hoàn hảo tuyệt đối.". Bố cục: Một chiếc bia ngắm mục tiêu quân sự bị thủng lỗ chỗ; chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói đứng cạnh một biển báo hình tam giác màu vàng cảnh báo 'GIỚI HẠN KHO ĐẠN VÀ RỦI RO KỸ THUẬT'.
```
</details>

<details><summary>L60</summary>

```text
HÌNH L60 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mọi kỹ sư quân sự đều biết rằng: Sức mạnh càng hủy diệt thì cái giá phải trả càng đắt đỏ.". Bố cục: Bàn cân kỹ thuật: BÊN TRÁI là quả pháo nổ hủy diệt mạnh mẽ; BÊN PHẢI là chiếc đồng hồ cát đang cạn dần năng lượng, cán cân nghiêng nặng.
```
</details>

<details><summary>L61</summary>

```text
HÌNH L61 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và điểm yếu chí mạng đầu tiên của Pháo Thủ Hóa Học chính là giới hạn của kho dự trữ đạn dược!". Bố cục: Cận cảnh buồng chứa hóa chất của chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói: Mực dung dịch chất lỏng bên trong buồng dự trữ đang tụt dần xuống đáy cạn kiệt.
```
</details>

<details><summary>L62</summary>

```text
HÌNH L62 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Dung tích buồng chứa của con bọ dài 2cm chỉ đủ hóa chất cho khoảng 20-30 phát nổ liên thanh.". Bố cục: Hộp đạn hoạt hình: Một hộp chứa đúng 20-30 viên đạn phát sáng; mỗi phát bắn làm biến mất một viên đạn, hộp đạn dần trống rỗng.
```
</details>

<details><summary>L63</summary>

```text
HÌNH L63 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu gặp phải một đối thủ quá lì lợm hoặc bị bầy kiến lửa hàng ngàn con bao vây liên tục ép gã phải xả đạn không ngừng, con bọ sẽ rơi vào trạng thái cạn sạch kho đạn!". Bố cục: Tình huống vây hãm nguy hiểm: Đàn đàn kiến lửa hung hãn hàng trăm con giương càng răng cưa hàng ngàn con đỏ rực đang vây kín xung quanh chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói; chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói bắn liên tục cho đến khi nòng pháo đuôi chỉ xì ra một làn khói mỏng.
```
</details>

<details><summary>L64</summary>

```text
HÌNH L64 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thông báo từ trung tâm hậu cần: Kho đạn dự trữ đã cạn kiệt 100%!". Bố cục: Màn hình kỹ thuật số báo động cạn kiệt: Chữ 'HẾT ĐẠN 100%' nhấp nháy đỏ rực; chiếc kim xăng chỉ về vạch E rỗng không.
```
</details>

<details><summary>L65</summary>

```text
HÌNH L65 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cần tối thiểu 24 tiếng để tổng hợp lại hóa chất! Chuẩn xác như bản tin hậu cần!". Bố cục: Một chiếc đồng hồ đếm ngược nạp đạn: Kim đồng hồ chỉ mốc 24 tiếng đến 36 tiếng; chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói đeo băng quấn đầu nghỉ ngơi dưỡng sức.
```
</details>

<details><summary>L67</summary>

```text
HÌNH L67 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sau khi bắn hết cơ số đạn, Pháo Thủ Hóa Học mất từ 24 tiếng đến 36 tiếng ăn uống cật lực để cơ thể tái tổng hợp lại đủ lượng Hydroquinone và Hydrogen peroxide.". Bố cục: Bên trong cơ thể chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói: Hai buồng chứa hóa chất đang từ từ được nhỏ từng giọt Hydroquinone và Hydrogen peroxide mới tổng hợp vào bình chứa.
```
</details>

<details><summary>L68</summary>

```text
HÌNH L68 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong suốt khoảng thời gian nạp đạn này, gã hoàn toàn trở thành một con bọ cánh cứng yếu ớt không tấc sắt trong tay!". Bố cục: chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói lấm lét nấp dưới một chiếc lá mục khô, hai tay ôm đầu; một chú thằn lằn đi ngang qua phía trên khiến chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói toát mồ hôi lo lắng.
```
</details>

<details><summary>L69</summary>

```text
HÌNH L69 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa hết, gã béo tí hon này còn mang trên mình số phận của một thùng thuốc nổ di động!". Bố cục: chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói biến thành hình một thùng thuốc nổ TNT có dây ngòi cháy dở; bước đi rón rén từng bước nhẹ nhàng như giẫm trên trứng mỏng.
```
</details>

<details><summary>L70</summary>

```text
HÌNH L70 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu bị một kẻ thù to xác giẫm mạnh làm vỡ vách ngăn giữa 2 buồng hóa chất khi van an toàn chưa kịp mở, phản ứng tỏa nhiệt sẽ xảy ra ngay bên trong cơ thể và nổ tung con bọ thành từng mảnh vụn!". Bố cục: Vụ nổ tự hủy giả định: Bức tường ngăn giữa 2 buồng bị nứt vỡ; phản ứng tỏa nhiệt bùng nổ ngay trong ruột khiến khói bốc nghi ngút quanh mình chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói.
```
</details>

<details><summary>L71</summary>

```text
HÌNH L71 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sống bên cạnh cái chết mỗi ngày, đó là sự đánh đổi khắc nghiệt của tự nhiên.". Bố cục: chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói đứng trên một sợi dây thừng mảnh bắc qua vực sâu; một bên là ngọn lửa bỏng rát, một bên là bóng tối săn mồi; thần thái điềm đạm cân bằng.
```
</details>

<details><summary>L72</summary>

```text
HÌNH L72 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bởi vậy, bài học sinh tồn đầu tiên của loài bọ này không phải là bắn bừa bãi, mà là ngắm thật kỹ, bắn thật chuẩn và chỉ khai hỏa khi thật sự bị dồn vào bước đường cùng!". Bố cục: chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói đứng nghiêm trang như xạ thủ bắn tỉa chuyên nghiệp, một mắt nheo lại ngắm qua kính ngắm; nòng pháo đuôi khóa chặt mục tiêu chuẩn xác 100%.
```
</details>

<details><summary>L73</summary>

```text
HÌNH L73 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhìn vào Pháo Thủ Hóa Học, các kỹ sư cơ khí hàng đầu thế giới đã học được những bài học vô giá.". Bố cục: Viện nghiên cứu kỹ thuật hàng không: Các kỹ sư mặc áo bảo hộ đang quan sát chú chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói trên bàn thí nghiệm; phía sau là màn hình mô phỏng dòng khí động lực học.
```
</details>

<details><summary>L74</summary>

```text
HÌNH L74 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cấu tạo van một chiều và cơ chế phun xung nhiệt độ cao của loài bọ này hiện đang được các nhà khoa học mô phỏng để chế tạo các loại bình xịt thuốc y tế hạt siêu mịn, hệ thống dập lửa cứu hỏa siêu tốc, và thậm chí là động cơ tái khởi động cho các tàu vũ trụ thế hệ mới!". Bố cục: Các ứng dụng công nghệ mô phỏng sinh học: Một bình xịt y tế phun sương siêu mịn, một vòi phun cứu hỏa dập lửa bọt tuyết, và một động cơ đẩy tên lửa vũ trụ mini.
```
</details>

<details><summary>L75</summary>

```text
HÌNH L75 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tự nhiên chính là người thầy vĩ đại nhất.". Bố cục: Một cuốn sách mở lớn giữa khu rừng xanh tươi: Mẹ Thiên Nhiên đội vương miện lá cây đang mỉm cười trao tặng bằng sáng chế phát minh cho chú chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói.
```
</details>

<details><summary>L76</summary>

```text
HÌNH L76 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một sinh vật nhỏ bé bằng hạt lạc, không cần móng vuốt hay kích thước khổng lồ, chỉ cần kết hợp hài hòa giữa cấu trúc cơ khí tinh vi và hóa học chuẩn xác, đã có thể hiên ngang tồn tại suốt hàng triệu năm giữa muôn vàn kẻ săn mồi đẫm máu.". Bố cục: chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói đứng kiêu hãnh trên đỉnh một viên đá cuội phủ rêu; xung quanh các loài chim săn mồi và bọ ngựa đều giữ khoảng cách nể sợ; ánh hoàng hôn rực rỡ chiếu sáng.
```
</details>

<details><summary>L77</summary>

```text
HÌNH L77 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bạn ấn tượng nhất với điều gì ở Pháo Thủ Hóa Học: Khả năng đun sôi hóa chất lên 100°C trong tích tắc, hay màn thoát thân không tưởng sau 1 tiếng nằm trong dạ dày cóc?". Bố cục: Khung hình tương tác hai lựa chọn thú vị: BÊN TRÁI là khẩu pháo xịt hơi sôi 100°C; BÊN PHẢI là màn tẩu thoát khỏi dạ dày cóc sau 1 tiếng; chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói chỉ tay mời khán giả bình luận.
```
</details>

<details><summary>L78</summary>

```text
HÌNH L78 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy để lại bình luận chia sẻ cùng chúng tôi nhé!". Bố cục: Hộp bình luận YouTube hoạt hình rực rỡ: Hàng chục biểu tượng ngọn lửa, tia chớp và bình luận 'BỌ PHÁO THỦ BÁ ĐẠO!' đang bay lên lung linh.
```
</details>

<details><summary>L79</summary>

```text
HÌNH L79 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và bây giờ, hãy hướng ngòi bút về phân cảnh kết thúc bí ẩn!". Bố cục: Bàn vẽ chuyển màu từ rừng cây sang màu vàng cát bỏng rát của sa mạc hoang vu; ngòi bút vẽ tay lướt êm ái trên mặt giấy mở ra một vùng đất mới.
```
</details>

<details><summary>L80</summary>

```text
HÌNH L80 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong tập tiếp theo, chúng ta sẽ rời khỏi thảm rừng ẩm ướt để tiến vào vùng sa mạc khô hạn bậc nhất hành tinh.". Bố cục: Toàn cảnh sa mạc Úc mênh mông cát đỏ bỏng rát: Những cồn cát nhấp nhô dưới ánh mặt trời thiêu đốt; không khí bốc hơi mờ ảo đầy khắc nghiệt.
```
</details>

<details><summary>L81</summary>

```text
HÌNH L81 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nơi đây có một bóng đen bí ẩn toàn thân phủ đầy gai nhọn sắc bén như bãi chông di động!". Bố cục: BÓNG ĐEN HOÀN TOÀN (solid black silhouette) của một sinh vật kỳ dị toàn thân chi chít gai nhọn như quả cầu gai hay bãi chông di động, viền hào quang vàng cam sa mạc phát sáng bí ẩn.
```
</details>

<details><summary>L82</summary>

```text
HÌNH L82 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sinh vật kỳ dị này có siêu năng lực uống nước bằng chính da bàn chân qua hệ thống ống mao dẫn, có một chiếc đầu giả sau gáy để đánh lừa kẻ thù, và đặc biệt là vũ khí phòng vệ tối thượng: Bắn ra một tia máu đỏ lòm thẳng từ hốc mắt xa tới 1m để làm mù kẻ săn mồi!". Bố cục: Đặc tả bóng đen bí ẩn: Bàn chân giẫm lên giọt sương và nước tự hút ngược lên cơ thể; phía sau gáy có một chiếc đầu giả nhô lên; và từ hốc mắt bắn ra một tia máu đỏ thẳng tắp xa tới 1m.
```
</details>

<details><summary>L83</summary>

```text
HÌNH L83 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đố bạn biết danh tính của quái kiệt sa mạc gai góc này là ai?". Bố cục: BÓNG ĐEN BÍ ẨN (solid black silhouette) của quái kiệt gai góc nổi bật ở GIỮA; trên đầu là DẤU HỎI CHẤM LỚN MÀU ĐỎ phát sáng rực rỡ; dòng chữ 'ĐOÁN TÊN CON VẬT TẬP 19' lung linh.
```
</details>

<details><summary>L84</summary>

```text
HÌNH L84 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy để lại phán đoán của bạn bên dưới phần bình luận nhé!". Bố cục: Khung cảnh kết thúc hồi hộp: Chiếc cọ vẽ vàng chấm một giọt mực bí ẩn xuống mặt giấy trắng, để lại dấu hỏi lớn kích thích trí tò mò tột độ của khán giả.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Bị cóc nuốt chửng vào dạ dày suốt 1 tiếng đồng hồ, con bọ nhỏ bé này đã làm gì để thoát thân còn sống nguyên vẹn?". Bố cục: Bên trong dạ dày cóc tối tăm: chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng đội mũ bảo hộ kỹ sư vàng đang đứng hiên ngang giữa dòng axit dạ dày, nòng đuôi ngắm bắn chuẩn bị khai hỏa giải cứu bản thân.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Đây là Bọ Pháo Thủ, gã tí hon dài chỉ 2cm nhưng sở hữu khẩu đại bác hóa học đáng sợ nhất thế giới côn trùng!". Bố cục: chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng đứng bệ vệ trên nền trắng, khoe chiếc mũ bảo hộ kỹ sư vàng và đôi cánh xanh đen; chiếc thước đo 2cm đặt bên cạnh khẳng định tầm vóc tí hon.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Bên trong bụng gã là 2 buồng hóa chất riêng biệt chứa Hydroquinone và Hydrogen peroxide.". Bố cục: Sơ đồ cắt lớp bụng hoạt hình: Hai buồng hóa chất riêng biệt phát sáng màu xanh ngọc và cam đất; hai nhãn tên Hydroquinone và Hydrogen peroxide nổi bật.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Khi bị đe dọa, con bọ mở van xả hóa chất vào buồng đốt chứa enzyme xúc tác,". Bố cục: Van một chiều mở ra: Hóa chất từ hai buồng dự trữ tràn vào buồng đốt chứa enzyme xúc tác, chuẩn bị cho phản ứng kích hoạt.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "đun sôi dung dịch lên đúng 100°C và kích hoạt phản ứng nổ liên thanh 500 lần/giây!". Bố cục: Phản ứng dây chuyền bùng nổ: Hóa chất bị đun sôi lên đúng 100°C với tần số nổ liên thanh 500 lần/giây chớp nháy liên hồi.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Tia hơi hóa chất sôi sùng sục và cay xé da bắn ra với vận tốc 20 m/s". Bố cục: Nòng pháo đuôi của chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng bẻ cong 270° bắn ra luồng hơi nước sôi 100°C với vận tốc 20 m/s xé toạc màn đêm; tia lửa và khói trắng bốc lên cuồn cuộn.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "từ chiếc tháp pháo xoay 270° ở đuôi!". Bố cục: Cận cảnh tháp pháo đuôi có khớp xoay 270° linh hoạt: chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng ngắm bắn chuẩn xác theo mọi hướng mà không cần quay đầu.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Kể cả khi bị cóc nuốt vào bụng, Pháo Thủ Hóa Học vẫn bình tĩnh nã đạn liên tiếp trong dạ dày". Bố cục: Chú chú cóc khổng lồ Nhật Bản da sần sùi màu xanh xám, mắt to tròn lồi, mồm rộng há to khổng lồ đang nuốt chửng chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng vào mồm nhưng ngay lập tức ôm bụng quằn quại vì bị nã đạn cay rát bên trong nội tạng.
```
</details>

<details><summary>S09</summary>

```text
HÌNH S09 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "khiến con cóc đau đớn dữ dội và phải nôn ọe gã ra ngoài sau 40 phút!". Bố cục: Chú cóc há to mồm nôn ọe một bãi dịch lớn ra mặt đất; chiếc đồng hồ bấm giờ hiển thị mốc 40 phút cầm cự của con bọ.
```
</details>

<details><summary>S10</summary>

```text
HÌNH S10 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Nhỏ bé nhưng sở hữu kỹ thuật cơ khí đỉnh cao,". Bố cục: chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng lồm cồm bò ra từ bãi dịch nôn, phủi sạch chân, giũ đôi cánh cứng bóng loáng và hiên ngang bước đi bình an vô sự.
```
</details>

<details><summary>S11</summary>

```text
HÌNH S11 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "đó chính là bí thuật sinh tồn bất bại của Bọ Pháo Thủ!". Bố cục: Khung cảnh kết thúc oai phong: chú Bọ Pháo Thủ hoạt hình màu xanh đen, đầu cam đất, đội mũ bảo hộ kỹ sư vàng đứng trên đỉnh viên đá cuội, giơ hai tay chữ V chiến thắng dưới ánh hào quang rực rỡ; biểu tượng huy chương vàng sinh tồn lấp lánh.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/82 của video YouTube về Bọ Pháo Thủ). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói. Nhân vật phụ cố định: chú cóc khổng lồ Nhật Bản da sần sùi màu xanh xám, mắt to tròn lồi, mồm rộng há to; chú chim săn mồi hoạt hình mỏ quặp hung hãn, lông vũ bay tứ tung; đàn kiến lửa hung hãn hàng trăm con giương càng răng cưa; chú bọ ngựa chiến binh màu xanh lá giơ hai lưỡi kiếm răng cưa sắc bén. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/11 của video YouTube Shorts về Bọ Pháo Thủ). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Bọ Pháo Thủ (Bombardier Beetle) hoạt hình ngộ nghĩnh: thân hình thon gọn màu xanh đen ánh kim, đầu và chân màu cam đất, đội một chiếc mũ bảo hộ kỹ sư màu vàng có gắn kính bảo hộ trong suốt trên đầu, đuôi thon gọn có khớp xoay tháp pháo bằng kim loại phát ra vệt hơi nước bốc khói. Nhân vật phụ: chú cóc khổng lồ Nhật Bản da sần sùi màu xanh xám, mắt to tròn lồi, mồm rộng há to. 
```
</details>

## 7. SEO

- **title:** Bị Cóc Nuốt 1 Tiếng Vẫn Thoát Thân Nhờ Khẩu Pháo 100°C Nổ 500 Lần/Giây?! | Bọ Pháo Thủ | Tập 18
- **hook_paragraph:** Bọ Pháo Thủ (Bombardier Beetle) dài chỉ 2cm nhưng sở hữu hệ thống hai buồng hóa chất bắn ra tia hơi sôi 100°C với tần số nổ 500 lần/giây, tháp pháo xoay 270 độ và sống sót ngoạn mục sau 1 tiếng bị cóc nuốt vào dạ dày! Giải mã vũ khí hóa học tối mật của tự nhiên.
- **question:** Bạn ấn tượng nhất với cơ chế đun sôi 100°C trong tích tắc hay màn thoát khỏi dạ dày cóc sau 1 tiếng của Bọ Pháo Thủ? Đoán xem bóng đen tập sau là loài nào nhé!
- **next_teaser:** quái kiệt sa mạc phủ đầy gai nhọn uống nước bằng chân và bắn tia máu từ mắt
- **shorts_title:** Bị Cóc Nuốt 1 Tiếng Vẫn Thoát Thân Nhờ Khẩu Pháo Sôi 100°C?! 💥 #shorts #bophaothu
- **shorts_desc:** Bọ Pháo Thủ dài 2cm nổ liên thanh 500 lần/giây xịt hơi sôi 100°C, bị cóc nuốt vào dạ dày suốt 1 tiếng vẫn nã đạn khiến cóc nôn ra bò đi bình an vô sự! Khám phá vũ khí côn trùng đỉnh cao.
- **bullets:** Hồ sơ vũ khí: Pháo Thủ Hóa Học 2cm bắn tia hóa chất sôi 100°C · Bản vẽ cơ khí: Hệ thống 2 buồng phản ứng Hydroquinone và Hydrogen peroxide · Động cơ xung 500 Hz: Tốc độ nổ liên thanh vi mô như tên lửa V-1 · Thực chiến Kobe 2018: Nã đạn trong dạ dày cóc suốt 1 tiếng và tẩu thoát · Gót chân Asin: Giới hạn kho đạn 20-30 phát và nguy cơ tự nổ · Bật mí bóng đen bí ẩn tập tiếp theo: Quái kiệt sa mạc bắn tia máu từ mắt
- **tags:** bọ pháo thủ, bo phao thu, bombardier beetle, vũ khí bọ pháo thủ, bọ pháo thủ thoát khỏi dạ dày cóc, bọ phun nước sôi, pháo thủ hóa học, động vật hài hước, thế giới động vật, vẽ chuyện hoang dã, whiteboard animation việt nam, khoa học động vật
- **hashtags:** #BoPhaoThu #BombardierBeetle #TheGioiDongVat #VeChuyenHoangDa #WhiteboardAnimation

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-18-bo-phao-thu
python src/episode/pipeline.py tts    projects/tap-18-bo-phao-thu     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-18-bo-phao-thu     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-18-bo-phao-thu     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-18-bo-phao-thu              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-18-bo-phao-thu --force
python scripts/beat_sheet.py projects/tap-18-bo-phao-thu               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-18-bo-phao-thu/audio/shorts.wav projects/tap-18-bo-phao-thu/renders/tap-18-bo-phao-thu_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-18-bo-phao-thu
python src/episode/pipeline.py seo    projects/tap-18-bo-phao-thu
python src/episode/episode_doc.py     projects/tap-18-bo-phao-thu
```
