# TẬP 24 — CÁ MÚT ĐÁ HAGFISH · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-24-ca-mut-da-hagfish`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-24-ca-mut-da-hagfish`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F5` · **Persona giọng:** `nha_khoa_hoc` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Cá Mút Đá Hagfish |
| Tiêu đề YouTube | Sinh Vật Biến 20 Lít Nước Thành Keo Nhớt Làm Nghẹt Thở Cá Mập?! |
| Video dài | `renders/tap-24-ca-mut-da-hagfish_long.mp4` — 9:03.3 (543.3s) |
| Shorts | `renders/tap-24-ca-mut-da-hagfish_shorts.mp4` — 0:50.4 (50.4s) |
| Thumbnail | `renders/tap-24-ca-mut-da-hagfish_thumbnail.jpg` |
| Số hình | dài 65 beat / 65 ảnh riêng; Shorts 11 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.1**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/65 của video YouTube về Cá Mút Đá Hagfish). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán. Nhân vật phụ cố định: ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước; cô trợ lý phòng thí nghiệm hoạt hình mặc áo blouse xanh nhạt đeo thẻ nhân viên; chú cá mập xám hung dữ răng nhọn hoắt há to miệng ngạt thở hài hước. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — QUÁI VẬT 4 TRÁI TIM KHÔNG XƯƠNG SỐNG
*Badge:* `HỒ SƠ MẪU VẬT` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene01_p0.wav` (438 ký tự) · mood `tram_bi_an`

```text
Ghi chép thí nghiệm phòng lab đáy biển sâu, ca trực rạng sáng. Đèn huỳnh quang tím bật sáng chiếu thẳng vào bể cách ly số hai mươi tư. Giữa đáy nước lạnh ngắt, một sinh vật dài ngoằng trơn nhẫy như sợi dây thừng màu hồng xám đang cuộn tròn bất động... Không có hàm răng trên dưới. Không có cột sống lưng. Không có lấy một chiếc vây bơi hoàn chỉnh. Và đôi mắt thì thoái hóa thành hai đốm trắng mờ đục chẳng nhìn thấy nổi ánh sáng mặt trời!
```
**Part 1** → `audio/vs/scene01_p1.wav` (128 ký tự) · 🎭 cameo `co_tro_ly`

```text
Viện trưởng ơi, mẫu vật này nhìn trơn tuột lù đù như cọng bún thiu, thả vào bể nuôi chung với cá mập lỡ bị nuốt chửng thì sao ạ?
```
**Part 2** → `audio/vs/scene01_p2.wav` (484 ký tự) · mood `hao_hung`

```text
[surprise-oh] Trợ lý ngây thơ quá rồi! Nếu có con cá mập nào dại dột đớp phải mẫu vật này, thì kẻ phải cầu cứu đội cấp cứu chính là con cá mập chứ không phải nó đâu! [laughter] Xin giới thiệu với các đồng nghiệp: đây là Cá Mút Đá Hagfish, sinh vật cổ đại thuộc lớp Myxini, một trong những nhánh động vật có hộp sọ nguyên thủy nhất hành tinh. Chiều dài trung bình từ bốn mươi đến tám mươi xăng-ti-mét. Trong giới sinh vật học, chúng tôi gọi thẳng tên nó bằng biệt danh: Cỗ Máy Tạo Đờm!
```
**Part 3** → `audio/vs/scene01_p3.wav` (594 ký tự) · mood `nghiem_trang_gia`

```text
Tổ tiên của nó đã tung tăng dưới đáy biển từ hơn ba trăm triệu năm trước, tức là xuất hiện trước cả loài khủng long bạo chúa, sống sót qua hàng loạt đại tuyệt chủng mà chẳng thèm thay đổi hình dáng! Toàn bộ cơ thể nó chỉ có hộp sọ bằng sụn dẻo, không có đốt sống thật, nhưng lại sở hữu tới bốn quả tim độc lập để bơm máu! Và thứ vũ khí sinh học kinh dị giúp nó bất khả chiến bại suốt hàng trăm triệu năm qua chính là khả năng phóng ra một đại dương chất nhầy đặc quánh làm ngạt thở mọi kẻ săn mồi! Đêm nay, tôi tuyên bố kích hoạt hệ thống thử thách năm cấp độ cực hạn để giải mã Cỗ Máy Tạo Đờm!
```

### scene02 — CỖ MÁY SIÊU TỐC BIẾN 20 LÍT NƯỚC THÀNH KEO NHỚT
*Thẻ chương:* BÙNG NỔ 10.000 LẦN THỂ TÍCH CHỈ TRONG MỘT NỐT NHẠC

*Badge:* `CẤP ĐỘ 1: TẠO ĐỜM` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene02_p0.wav` (378 ký tự) · mood `hao_hung`

```text
Khởi động Cấp độ một: Thử thách công suất phóng chất nhầy! Nhìn từ bên ngoài, làn da của Cỗ Máy Tạo Đờm mềm mại, lỏng lẻo như một chiếc áo khoác quá khổ mượn của anh trai. Nhưng nếu bạn soi kính hiển vi chạy dọc hai bên sườn của nó, bạn sẽ đếm được từ một trăm đến một trăm năm mươi lỗ chân lông đặc biệt. Đó chính là miệng xả của hàng trăm túi tuyến chất nhầy sinh học tối tân!
```
**Part 1** → `audio/vs/scene02_p1.wav` (253 ký tự) · mood `don_dap`

```text
Hãy quan sát thí nghiệm khi một kẻ thù vừa chạm miệng vào người nó! Ngay lập tức, các túi tuyến này bóp nghẹt, bắn ra một lượng dịch đục chỉ nhỏ bằng hạt đậu. Nhưng khoảnh khắc giọt dịch chạm vào nước biển, một phản ứng dây chuyền nổ tung! [surprise-wa]
```
**Part 2** → `audio/vs/scene02_p2.wav` (342 ký tự) · mood `don_dap`

```text
Chỉ trong vòng đúng không phẩy bốn giây — tức là nhanh hơn một cái chớp mắt của con người — giọt dịch nhỏ xíu đó lập tức trương nở thể tích lên gấp mười ngàn lần! Một con cá mút đá dài nửa mét có thể biến toàn bộ hai mươi lít nước biển xung quanh thành một khối keo nhớt đặc quánh, sánh mịn chẳng khác nào một xô thạch khổng lồ! [surprise-oh]
```
**Part 3** → `audio/vs/scene02_p3.wav` (485 ký tự) · mood `hao_hung`

```text
Làm thế nào mà một giọt dịch bé tí lại biến cả xô nước thành keo dính nhanh đến mức ma quái như vậy? Tiến sĩ Douglas Fudge tại phòng thí nghiệm cơ sinh học đã giải mã bí ẩn dưới kính hiển vi: bên trong túi dịch chứa hàng ngàn cuộn sợi tơ protein siêu nhỏ làm từ chất sừng keratin, mỗi sợi cuộn chặt như một cuộn chỉ may vá tinh xảo. Khi gặp nước biển và lực xoáy, các cuộn chỉ tự bung sợi với vận tốc ánh sáng, đan cài vào các hạt chất nhầy hút nước giữ chặt mọi phân tử nước biển lại!
```
**Part 4** → `audio/vs/scene02_p4.wav` (220 ký tự) · mood `hao_hung`

```text
Kết quả tạo ra một loại vật liệu siêu nhớt không phải gel đặc, mà là một khối mạng lưới chất lỏng đàn hồi vô cùng bền bỉ! [laughter] Kẻ thù chưa kịp cắn miếng nào đã thấy miệng mình ngập ngụa trong cả biển đờm nhầy nhụa!
```
**Part 5** → `audio/vs/scene02_p5.wav` (157 ký tự) · 🎭 cameo `co_tro_ly`

```text
Viện trưởng ơi, em thử đong một xô nước biển năm ga-lông, thả một chú cá mút đá vào quấy nhẹ một cái là cả xô nước đông đặc nhấc bổng cả cái muôi lên luôn ạ!
```
**Part 6** → `audio/vs/scene02_p6.wav` (410 ký tự) · mood `hao_hung`

```text
[surprise-oh] Trợ lý chứng kiến tận mắt rồi đấy! Kỳ diệu ở chỗ: toàn bộ mạng lưới sợi tơ và chất nhầy chỉ chiếm chưa tới không phẩy một phần trăm tổng khối lượng, còn lại tới chín mươi chín phẩy chín phần trăm đều là nước biển bị bắt giữ! Tận dụng chính nước của môi trường để làm vũ khí bảo vệ mình, đúng là cỗ máy tiết kiệm nguyên liệu siêu đẳng nhất hành tinh! Cấp độ một: Phóng chất nhầy thành công mỹ mãn!
```

### scene03 — VŨ KHÍ BÓP NGHẸT KHIẾN CÁ MẬP HUNG DỮ PHẢI NHẢ VỘI
*Thẻ chương:* BÍT KÍN KHE MANG LÀM KẺ SĂN MỒI SUÝT CHẾT NGẠT

*Badge:* `CẤP ĐỘ 2: BÓP NGHẸT` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene03_p0.wav` (351 ký tự) · mood `tram_bi_an`

```text
Trợ lý, nâng độ khó lên Cấp độ hai: Thử nghiệm vũ khí phòng thủ trước chúa tể đại dương! Trong chuỗi thức ăn dưới đáy biển sâu, cá mập hay cá mú khổng lồ là những sát thủ săn mồi tàn bạo nhất. Khi nhìn thấy Cỗ Máy Tạo Đờm bơi chậm chạp không vây, không vảy, không gai nhọn, con cá mập lập tức lao tới há rộng bộ hàm sắc nhọn đớp trọn con mồi vào họng!
```
**Part 1** → `audio/vs/scene03_p1.wav` (203 ký tự) · mood `don_dap`

```text
Khoảnh khắc hàm cá mập vừa nghiến xuống lớp da lỏng lẻo của cá mút đá, các túi tuyến hai bên sườn lập tức khai hỏa! Hai mươi lít chất nhầy bùng nổ ngay bên trong khoang miệng của kẻ đi săn! [surprise-wa]
```
**Part 2** → `audio/vs/scene03_p2.wav` (341 ký tự) · mood `don_dap`

```text
Điều kinh hoàng bắt đầu: cá mập thở bằng cách hút nước vào miệng rồi ép nước chảy qua các khe mang hai bên để lọc oxy. Nhưng khối chất nhầy của Cỗ Máy Tạo Đờm là một loại polymer nhớt dính siêu cấp: dòng nước chảy qua mang càng mạnh, các sợi tơ keratin càng dãn dài và quấn chặt bít kín mít toàn bộ các khe mang thở của cá mập! [surprise-oh]
```
**Part 3** → `audio/vs/scene03_p3.wav` (130 ký tự) · 🎭 cameo `co_tro_ly`

```text
Báo cáo viện trưởng, cảm biến ghi nhận con cá mập đang quằn quại lắc đầu dữ dội, nó ho sặc sụa và nhả mẫu vật ra ngay lập tức kìa!
```
**Part 4** → `audio/vs/scene03_p4.wav` (510 ký tự) · mood `hao_hung`

```text
Đúng thế các đồng nghiệp ạ! Bị bít kín mang là đồng nghĩa với việc bị bóp nghẹt khí quản nghẹt thở đến chết chỉ trong vài giây! Con cá mập hoảng loạn nhả vội cá mút đá ra ngoài, liên tục ho khạc để cố tống mớ đờm dính ra khỏi khe mang rồi tháo chạy bạt mạng! Các video gắn camera dưới đáy biển sâu đã ghi nhận hàng chục vụ tấn công của cá mập hay cá chình biển, và một trăm phần trăm kẻ săn mồi đều phải vội vã tháo chạy thề không bao giờ bén mảng lại gần! [laughter] Cấp độ hai: Chúa tể biển sâu bị hạ đo ván!
```

### scene04 — ẢO THUẬT TỰ THẮT NÚT CƠ THỂ GẠT ĐỜM VÀ XÉ MỒI
*Thẻ chương:* TỰ THẮT NÚT DÂY THỪNG TỪ ĐẦU ĐẾN ĐUÔI SIÊU ẢO

*Badge:* `CẤP ĐỘ 3: THẮT NÚT` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene04_p0.wav` (389 ký tự) · mood `nghiem_trang_gia`

```text
Tăng cấp độ thử thách lên Cấp độ ba: Nghệ thuật cơ học tự thắt nút cơ thể! Sau khi phóng ra cả một biển chất nhầy nhớt bốc mùi bám đầy khắp người, Cỗ Máy Tạo Đờm phải đối mặt với một bài toán sinh tử: nếu không dọn sạch lớp đờm dính trên cơ thể mình, chính các khe mang thở của nó cũng sẽ bị nghẹt thở đến chết! Không có chân tay, không có vây, làm thế nào để nó gạt sạch lớp keo dính này?
```
**Part 1** → `audio/vs/scene04_p1.wav` (223 ký tự) · mood `hao_hung`

```text
Và đây là lúc tuyệt kỹ ảo thuật đỉnh cao bậc nhất giới động vật xuất hiện! Cỗ Máy Tạo Đờm uốn cong chiếc đuôi, tự luồn cơ thể mình qua một vòng tròn để tạo thành một nút thắt thòng lọng hình số tám quanh thân! [surprise-oh]
```
**Part 2** → `audio/vs/scene04_p2.wav` (296 ký tự) · mood `don_dap`

```text
Sau đó, nó co bóp các bó cơ dọc sống lưng để trượt nút thắt đó di chuyển từ từ từ đầu xuống tận đuôi! Chiếc nút thắt di động này đóng vai trò như một chiếc cần gạt nước kính ô tô, miết chặt vào da và cạo sạch bong toàn bộ lớp chất nhầy nhớt trôi tuột ra ngoài cơ thể trong vài giây! [surprise-wa]
```
**Part 3** → `audio/vs/scene04_p3.wav` (413 ký tự) · mood `hao_hung`

```text
Chưa hết đâu các đồng nghiệp! Vì loài cá này hoàn toàn không có hàm răng trên dưới để nhai cắn, khi tìm thấy một xác cá voi chết chìm dưới đáy biển sâu, nó lại dùng đúng tuyệt kỹ thắt nút này: cắm chiếc đĩa lưỡi có gai sừng keratin vào thịt xác chết, rồi thắt nút cơ thể tỳ mạnh vào tảng thịt để tạo đòn bẩy xé toạc từng mảng thức ăn! [laughter] Không có hàm răng, nó lấy chính cơ thể mình làm chiếc cờ-lê cơ học!
```
**Part 4** → `audio/vs/scene04_p4.wav` (483 ký tự) · mood `hao_hung`

```text
Đặc biệt nhất, khi chui rúc sâu vào bên trong những xác chết khổng lồ tăm tối nơi nồng độ oxy gần như bằng không, Cỗ Máy Tạo Đờm lại kích hoạt một năng lực chấn động giới sinh học: nó có thể hấp thụ trực tiếp các chất dinh dưỡng và a-xít a-min xuyên qua lớp da và mang của mình! Đây là loài động vật có xương sống duy nhất trên Trái Đất được ghi nhận có khả năng ăn thức ăn bằng da chẳng khác nào các loài giun biển nguyên thủy! Cấp độ ba: Hoàn thành xuất sắc tuyệt đối không tì vết!
```

### scene05 — VỤ LẬT XE TRÊN CAO TỐC OREGON VÀ SỢI TƠ TƯƠNG LAI
*Thẻ chương:* 7.500 POUND CÁ MÚT ĐÁ BIẾN CAO TỐC THÀNH BIỂN NHẦY

*Badge:* `CẤP ĐỘ 4: OREGON 2017` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene05_p0.wav` (326 ký tự) · mood `hao_hung`

```text
Nâng công suất máy quét lên Cấp độ bốn: Khảo nghiệm sự kiện thực tế kinh điển ngoài đời thực! Nếu các đồng nghiệp vẫn nghĩ chất nhầy của Cỗ Máy Tạo Đờm chỉ là chuyện viễn tưởng dưới đáy biển sâu, thì hãy quay ngược thời gian về ngày mười ba tháng bảy năm hai ngàn mười bảy trên Quốc lộ một trăm linh một bang O-rê-gơn nước Mỹ!
```
**Part 1** → `audio/vs/scene05_p1.wav` (226 ký tự) · mood `nghiem_trang_gia`

```text
Báo cáo cảnh sát giao thông: Một chiếc xe tải chở bảy ngàn năm trăm pound — tức là gần ba ngàn bốn trăm ki-lô-gam cá mút đá sống đang trên đường vận chuyển — bỗng nhiên gặp sự cố phanh gấp và lật nhào ngang giữa đường cao tốc!
```
**Part 2** → `audio/vs/scene05_p2.wav` (361 ký tự) · mood `don_dap`

```text
Hàng ngàn chú cá mút đá bị văng ra khỏi thùng chứa, rơi lộp độp xuống mặt đường nhựa nóng rực và bị kích động hoảng loạn tột độ. [surprise-wa] Đồng loạt hàng ngàn Cỗ Máy Tạo Đờm kích hoạt cơ chế tự vệ: chúng xả hàng tấn chất nhầy nhớt bao phủ kín mít mặt đường cao tốc và trùm lên một chiếc xe ô tô con gần đó như cảnh tượng trong phim quái vật ngoài hành tinh!
```
**Part 3** → `audio/vs/scene05_p3.wav` (296 ký tự) · mood `hao_hung`

```text
Đội cứu hỏa và cảnh sát giao thông bang O-rê-gơn phải điều động máy ủi đất và vòi rồng cứu hỏa công suất cực đại phun nước cật lực suốt nhiều giờ liền mới dọn dẹp sạch được bãi chiến trường nhầy nhụa trơn như đổ mỡ! [laughter] Vụ tai nạn trở thành đề tài sốt dẻo trên toàn bộ các mặt báo quốc tế!
```
**Part 4** → `audio/vs/scene05_p4.wav` (499 ký tự) · mood `hao_hung`

```text
Từ sự kiện chấn động đó, các nhà khoa học vật liệu quân sự của Hải quân Mỹ đã vào cuộc nghiên cứu sâu sợi tơ của cá mút đá. Kết quả cho thấy các sợi protein keratin trong chất nhầy mỏng gấp một trăm lần sợi tóc người nhưng có độ bền kéo và độ dẻo dai tương đương tơ nhện và sợi ni-lông nhân tạo! Người ta đang nghiên cứu dùng loại sợi sinh học này để dệt quần áo chống đạn, làm sợi chỉ khâu y tế tự tiêu và chế tạo màng dập lửa thân thiện với môi trường! [surprise-oh] Cấp độ bốn: Vượt qua xuất sắc!
```

### scene06 — KHẮC TINH HẢI QUỲ VÀ BÓNG ĐEN ĐIỆP VIÊN ĐẠI DƯƠNG
*Thẻ chương:* TỬ HUYỆT DUY NHẤT VÀ BÓNG ĐEN ĐIỆP VIÊN 9 NÃO

*Badge:* `CẤP TỐI THƯỢNG` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene06_p0.wav` (246 ký tự) · mood `tram_bi_an`

```text
Bước vào Cấp độ tối thượng: Liệu Cỗ Máy Tạo Đờm có thực sự bất tử dưới đáy đại dương? Cá mập cắn phải nhả. Cá mú đớp phải ho khạc. Bị mắc kẹt thì tự thắt nút tẩu thoát. Chẳng lẽ quái vật này không có lấy một kẻ thù tự nhiên nào sao? [question-oh]
```
**Part 1** → `audio/vs/scene06_p1.wav` (414 ký tự) · mood `bi_hai`

```text
Và đây là câu trả lời bất ngờ: Khắc tinh số một đánh bại được Cỗ Máy Tạo Đờm lại là những sinh vật... không hề có mang để thở! Đó là những bông hải quỳ ăn thịt khổng lồ và các loài chim biển! Hải quỳ săn mồi bằng xúc tu có tế bào gai châm độc, nuốt chửng con mồi qua khoang bụng mở mà không cần hút nước qua mang, nên chất nhầy của cá mút đá hoàn toàn mất tác dụng! Đúng là vỏ quýt dày có móng tay nhọn! [laughter]
```
**Part 2** → `audio/vs/scene06_p2.wav` (358 ký tự) · mood `hao_hung`

```text
Tổng kết ghi chép phòng thí nghiệm số hai mươi tư: Mẫu vật đạt điểm mười tuyệt đối cho cỗ máy phòng thủ chất nhầy kỳ dị nhất tiến hóa! Còn các trợ lý thì sao? Nếu được sở hữu một trong hai năng lực: biến cả xô nước thành keo nhớt trong một giây, hay tự thắt nút cơ thể hình số tám để trốn thoát, bạn chọn cái nào? Hãy bình luận lựa chọn của bạn bên dưới nhé!
```
**Part 3** → `audio/vs/scene06_p3.wav` (507 ký tự) · mood `am_ap`

```text
Hồ sơ phòng thí nghiệm hôm nay xin tạm khép lại. Nhưng tập sau, chúng ta sẽ bước vào hồ sơ thế giới ngầm đại dương để điều tra một siêu điệp viên bí ẩn bậc nhất biển cả! Một sinh vật sở hữu tới chín bộ não độc lập, ba trái tim đập nhịp nhàng, dòng máu màu xanh lam huyền bí, và sở hữu tài hóa trang thiên bẩm: có thể biến hình mượt mà thành mười lăm loài sinh vật kịch độc khác nhau dưới đáy biển chỉ trong chớp mắt! Đố các bạn biết bóng đen bí ẩn kỳ sau là loài vật nào? Hãy đoán ngay ở phần bình luận nhé!
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Chỉ cần một con cá mập vừa cắn vào thân, loài vật này có thể biến hai mươi lít nước biển xung quanh thành một khối keo nhớt đặc quánh chỉ trong không phẩy bốn giây làm kẻ săn mồi suýt chết ngạt! [laughter] Đây là Cá Mút Đá Hagfish, sinh vật cổ đại ba trăm triệu năm dài nửa mét sống dưới đáy biển sâu. Cơ thể nó không có xương sống, có tới bốn quả tim độc lập, và sở hữu hàng trăm lỗ xả chất nhầy hai bên sườn! Khi bị tấn công, các sợi tơ protein dãn nở gấp mười ngàn lần bít kín hoàn toàn các khe mang thở của cá mập khiến kẻ đi săn ho sặc sụa phải nhả vội ra tẩu thoát! [surprise-wa] Để gạt sạch đờm khỏi người mình, nó tự thắt cơ thể thành nút thòng lọng hình số tám từ đầu đến đuôi như ảo thuật gia! Năm hai ngàn mười bảy, một xe tải chở ba ngàn bốn trăm ki-lô-gam cá mút đá lật nhào đã biến cả đường cao tốc ở Mỹ thành một biển chất nhầy nhớt trượt ngã cả xe cứu hỏa! Một cỗ máy tạo đờm độc nhất vô nhị của đại dương!
```

**Whisper prompt:** `Cá Mút Đá Hagfish, Cỗ Máy Tạo Đờm, Myxini, Đa-vít Phút-giơ, Douglas Fudge, O-rê-gơn, Oregon, Quốc lộ 101, cao tốc 101, 7.500 pound, 3.400kg, 20 lít, 10.000 lần, 0,4 giây, 300 triệu năm, 4 trái tim, sợi tơ keratin, thắt nút, travelling knot, 5 cấp độ, cấp độ 1, cấp độ 2, cấp độ 3, cấp độ 4, cấp độ 5`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| hai mươi tư | 24 |
| hai mươi lăm | 25 |
| Hai mươi lít | 20 lít |
| hai mươi lít | 20 lít |
| hai mươi xăng-ti-mét | 20cm |
| ba mươi xăng-ti-mét | 30cm |
| bốn mươi xăng-ti-mét | 40cm |
| bốn mươi đến tám mươi xăng-ti-mét | 40-80cm |
| tám mươi xăng-ti-mét | 80cm |
| mười ngàn lần | 10.000 lần |
| nửa mét | 0,5m |
| không phẩy một phần trăm | 0,1% |
| chín mươi chín phẩy chín phần trăm | 99,9% |
| năm ga-lông | 5 gallon |
| không phẩy bốn giây | 0,4 giây |
| một giây | 1 giây |
| hai giây | 2 giây |
| năm ngàn | 5.000 |
| bốn trái tim | 4 trái tim |
| bốn quả tim | 4 quả tim |
| ba trăm triệu năm | 300 triệu năm |
| hàng trăm triệu năm | hàng trăm triệu năm |
| hàng trăm lỗ | hàng trăm lỗ |
| một trăm năm mươi | 150 |
| một trăm | 100 |
| một trăm phần trăm | 100% |
| bảy ngàn năm trăm pound | 7.500 pound |
| ba ngàn bốn trăm ki-lô-gam | 3.400kg |
| mười ba tháng bảy năm hai ngàn mười bảy | 13/7/2017 |
| Năm hai ngàn mười bảy | 2017 |
| năm hai ngàn mười bảy | 2017 |
| năm mươi | 50 |
| mười lăm | 15 |
| chín bộ não | 9 bộ não |
| ba trái tim | 3 trái tim |
| mười lăm loài | 15 loài |
| năm cấp độ | 5 cấp độ |
| cấp độ một | cấp độ 1 |
| cấp độ hai | cấp độ 2 |
| cấp độ ba | cấp độ 3 |
| cấp độ bốn | cấp độ 4 |
| cấp độ năm | cấp độ 5 |
| cấp một | cấp 1 |
| cấp hai | cấp 2 |
| cấp ba | cấp 3 |
| cấp bốn | cấp 4 |
| thứ nhất | thứ 1 |
| thứ hai | thứ 2 |
| thứ ba | thứ 3 |
| thứ tư | thứ 4 |
| thứ năm | thứ 5 |
| điểm mười | điểm 10 |
| a-xít a-min | axit amin |
| Đa-vít Phút-giơ | Douglas Fudge |
| O-rê-gơn | Oregon |
| Kê-ra-tin | Keratin |
| kê-ra-tin | keratin |
| Quốc lộ một trăm linh một | Quốc lộ 101 |
| cao tốc một trăm linh một | cao tốc 101 |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · QUÁI VẬT 4 TRÁI TIM KHÔNG XƯƠNG SỐNG · 80.8s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.1 (7.1s) | L01 | Ghi chép thí nghiệm phòng lab đáy biển sâu, ca trực rạng sáng. Đèn huỳnh quang tím bật sáng chiếu thẳng vào bể cách ly số 24. |  | Phòng thí nghiệm đáy biển sâu ca trực rạng sáng: ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước và cô trợ lý phòng thí nghiệm hoạt hình mặc áo blouse xanh nhạt đeo thẻ nhân viên đứng trước bể cách ly số 24 phát sáng ánh huỳnh quang tím. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này. |
| b02 | 00:07.1–00:12.2 (5.1s) | L02 | Giữa đáy nước lạnh ngắt, một sinh vật dài ngoằng trơn nhẫy như sợi dây thừng màu hồng xám đang cuộn tròn bất động... |  | Bên trong làn nước lạnh ngắt, chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán dài ngoằng trơn nhẫy như sợi dây thừng màu hồng xám đang cuộn tròn bồng bềnh dưới đáy bể. |
| b03 | 00:12.2–00:21.6 (9.3s) | L03 | Không có hàm răng trên dưới. Không có cột sống lưng. Không có lấy một chiếc vây bơi hoàn chỉnh. Và đôi mắt thì thoái hóa thành hai đốm trắng mờ đục chẳng nhìn thấy nổi ánh sáng mặt trời! |  | Bốn ô đồ họa chẩn đoán gạch chéo đỏ: không có hàm răng trên dưới, không có cột sống lưng, không có vây bơi, và đôi mắt mờ đục. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này. |
| b04 | 00:21.6–00:29.2 (7.6s) | L04 | Viện trưởng ơi, mẫu vật này nhìn trơn tuột lù đù như cọng bún thiu, thả vào bể nuôi chung với cá mập lỡ bị nuốt chửng thì sao ạ? |  | BÊN TRÁI cô trợ lý phòng thí nghiệm hoạt hình mặc áo blouse xanh nhạt đeo thẻ nhân viên lo lắng nhìn vào bể kính tưởng tượng chú cá mút đá bị con cá mập to nuốt chửng; BÊN PHẢI chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán trôi lờ đờ ngơ ngác. |
| b05 | 00:29.2–00:37.3 (8.1s) | L05 | Trợ lý ngây thơ quá rồi! Nếu có con cá mập nào dại dột đớp phải mẫu vật này, thì kẻ phải cầu cứu đội cấp cứu chính là con cá mập chứ không phải nó đâu! |  | ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước bật cười lắc ngón tay chỉ lên màn hình: hình ảnh con cá mập phải gọi xe cứu thương cấp cứu vì trót đớp phải cá mút đá. |
| b06 | 00:37.3–00:45.9 (8.6s) | L06 | Xin giới thiệu với các đồng nghiệp: đây là Cá Mút Đá Hagfish, sinh vật cổ đại thuộc lớp Myxini, một trong những nhánh động vật có hộp sọ nguyên thủy nhất hành tinh. |  | Bản đồ cây tiến hóa đại dương cổ đại giới thiệu lớp Myxini có hộp sọ nguyên thủy nhất; chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán uốn lượn đội chiếc vương miện cổ xưa. |
| b07 | 00:45.9–00:48.6 (2.8s) | L07 | Chiều dài trung bình từ 40-80cm. | **40-80 CM** · chiều dài cơ thể · R/350 · [0.65, 0.5] | Ở GIỮA chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán nằm thẳng cạnh chiếc thước đo chiều cao màu vàng 40-80cm của phòng thí nghiệm. |
| b08 | 00:48.6–00:53.5 (4.9s) | L08 | Trong giới sinh vật học, chúng tôi gọi thẳng tên nó bằng biệt danh: Cỗ Máy Tạo Đờm! |  | chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán tự hào đeo dải băng danh hiệu Cỗ Máy Tạo Đờm, xung quanh bắn ra những giọt bọt nước phát sáng ngộ nghĩnh. |
| b09 | 00:53.5–01:01.7 (8.2s) | L09 | Tổ tiên của nó đã tung tăng dưới đáy biển từ hơn 300 triệu năm trước, tức là xuất hiện trước cả loài khủng long bạo chúa, sống sót qua hàng loạt đại tuyệt chủng mà chẳng thèm thay đổi hình dáng! | **300 TR NĂM** · sống trước khủng long · L/350 · [0.35, 0.45] | Dòng thời gian 300 triệu năm: tổ tiên chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán bơi tung tăng dưới đáy biển kỷ Phấn trắng trước cả thời khủng long bạo chúa T-Rex đứng trên bờ gầm rú. |
| b10 | 01:01.7–01:07.9 (6.2s) | L10 | Toàn bộ cơ thể nó chỉ có hộp sọ bằng sụn dẻo, không có đốt sống thật, nhưng lại sở hữu tới 4 quả tim độc lập để bơm máu! | **4 QUẢ TIM** · bơm máu độc lập · R/350 · [0.65, 0.48] | Mặt cắt giải phẫu trong suốt của chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán: hộp sọ bằng sụn dẻo và 4 quả tim độc lập màu đỏ tươi đang đập rộn ràng bơm máu khắp thân. |
| b11 | 01:07.9–01:16.0 (8.1s) | L11 | Và thứ vũ khí sinh học kinh dị giúp nó bất khả chiến bại suốt hàng trăm triệu năm qua chính là khả năng phóng ra một đại dương chất nhầy đặc quánh làm ngạt thở mọi kẻ săn mồi! |  | chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán phóng ra một làn sóng chất nhầy bọt trắng bao phủ cả một vùng nước biển làm một đàn cá săn mồi ho sặc sụa dạt ra xa. |
| b12 | 01:16.0–01:20.8 (4.8s) | L12 | Đêm nay, tôi tuyên bố kích hoạt hệ thống thử thách 5 cấp độ cực hạn để giải mã Cỗ Máy Tạo Đờm! | **5 CẤP ĐỘ** · thử thách phòng lab · L/350 · [0.35, 0.45] | ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước gạt cần gạt lớn; bảng đèn LED bật sáng dòng chữ THỬ THÁCH 5 CẤP ĐỘ CỰC HẠN. |

### scene02 · CỖ MÁY SIÊU TỐC BIẾN 20 LÍT NƯỚC THÀNH KEO NHỚT · 114.8s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.9 (9.9s) | L13 | Khởi động Cấp độ một: Thử thách công suất phóng chất nhầy! Nhìn từ bên ngoài, làn da của Cỗ Máy Tạo Đờm mềm mại, lỏng lẻo như một chiếc áo khoác quá khổ mượn của anh trai. |  | Bảng điện tử hiện CẤP ĐỘ 1: THỬ THÁCH CÔNG SUẤT PHÓNG CHẤT NHẦY; chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán có làn da mềm mại như chiếc áo khoác quá khổ lỏng lẻo. |
| b02 | 00:09.9–00:19.9 (10.0s) | L14 | Nhưng nếu bạn soi kính hiển vi chạy dọc hai bên sườn của nó, bạn sẽ đếm được từ 100 đến 150 lỗ chân lông đặc biệt. Đó chính là miệng xả của hàng trăm túi tuyến chất nhầy sinh học tối tân! | **150 LỖ** · dọc hai bên sườn · R/350 · [0.62, 0.5] | Kính hiển vi chạy dọc hai bên sườn chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán: hiển thị từ 100 đến 150 lỗ chân lông đặc biệt là miệng xả của các túi tuyến chất nhầy. |
| b03 | 00:19.9–00:25.0 (5.1s) | L15 | Hãy quan sát thí nghiệm khi một kẻ thù vừa chạm miệng vào người nó! Ngay lập tức, các túi tuyến này bóp nghẹt, |  | Một chiếc que gắp phòng lab chạm nhẹ vào thân chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán; các túi tuyến hai bên sườn lập tức bóp mạnh chuẩn bị khai hỏa. |
| b04 | 00:25.0–00:32.0 (7.0s) | L16 | bắn ra một lượng dịch đục chỉ nhỏ bằng hạt đậu. Nhưng khoảnh khắc giọt dịch chạm vào nước biển, một phản ứng dây chuyền nổ tung! |  | Túi tuyến bắn ra một giọt dịch đục nhỏ bằng hạt đậu rơi vào nước biển, bắt đầu phản ứng dây chuyền nổ tung. |
| b05 | 00:32.0–00:36.0 (3.9s) | L17 | Chỉ trong vòng đúng 0,4 giây — tức là nhanh hơn một cái chớp mắt của con người | **0,4 GIÂY** · tốc độ bùng nổ · L/350 · [0.35, 0.45] | Đồng hồ cát siêu tốc đếm 0,4 giây nhấp nháy đỏ rực; giọt dịch nhỏ chạm vào nước biển phát nổ dây chuyền thần tốc. |
| b06 | 00:36.0–00:48.2 (12.2s) | L18 | — giọt dịch nhỏ xíu đó lập tức trương nở thể tích lên gấp 10.000 lần! Một con cá mút đá dài 0,5m có thể biến toàn bộ 20 lít nước biển xung quanh thành một khối keo nhớt đặc quánh, sánh mịn chẳng khác nào một xô thạch khổng lồ! | **10.000 LẦN** · trương nở thể tích · R/350 · [0.65, 0.45]<br>**20 LÍT KEO** · từ một giọt dịch · L/480 · [0.32, 0.55] | Giọt dịch trương nở 10.000 lần, biến toàn bộ 20 lít nước biển xung quanh thành một khối keo nhớt đặc quánh sánh mịn như xô thạch khổng lồ. |
| b07 | 00:48.2–00:53.7 (5.5s) | L19 | Làm thế nào mà một giọt dịch bé tí lại biến cả xô nước thành keo dính nhanh đến mức ma quái như vậy? |  | ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước cầm chiếc kính lúp to tướng soi vào giọt dịch phát sáng, đặt dấu hỏi lớn về tốc độ tạo keo nhớt phi thường. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này. |
| b08 | 00:53.7–01:05.7 (12.0s) | L20 | Tiến sĩ Douglas Fudge tại phòng thí nghiệm cơ sinh học đã giải mã bí ẩn dưới kính hiển vi: bên trong túi dịch chứa hàng ngàn cuộn sợi tơ protein siêu nhỏ làm từ chất sừng keratin, mỗi sợi cuộn chặt như một cuộn chỉ may vá tinh xảo. | **D. FUDGE** · giải mã sợi tơ · L/350 · [0.35, 0.45] | Tiến sĩ Douglas Fudge tại phòng lab soi kính hiển vi: bên trong giọt dịch chứa hàng ngàn cuộn sợi tơ protein keratin cuộn tròn như cuộn chỉ may. |
| b09 | 01:05.7–01:13.5 (7.8s) | L21 | Khi gặp nước biển và lực xoáy, các cuộn chỉ tự bung sợi với vận tốc ánh sáng, đan cài vào các hạt chất nhầy hút nước giữ chặt mọi phân tử nước biển lại! |  | Sơ đồ hiển vi: các cuộn chỉ tơ keratin bung sợi với vận tốc cực nhanh, đan xen vào các hạt chất nhầy hút giữ chặt mọi phân tử nước biển. |
| b10 | 01:13.5–01:25.3 (11.7s) | L22 | Kết quả tạo ra một loại vật liệu siêu nhớt không phải gel đặc, mà là một khối mạng lưới chất lỏng đàn hồi vô cùng bền bỉ! Kẻ thù chưa kịp cắn miếng nào đã thấy miệng mình ngập ngụa trong cả biển đờm nhầy nhụa! |  | Một khối mạng lưới chất lỏng đàn hồi siêu nhớt bao bọc lấy kẻ thù; một con cá săn mồi há hốc mồm ngập ngụa trong đờm nhầy nhụa. |
| b11 | 01:25.3–01:34.1 (8.8s) | L23 | Viện trưởng ơi, em thử đong một xô nước biển 5 gallon, thả một chú cá mút đá vào quấy nhẹ một cái là cả xô nước đông đặc nhấc bổng cả cái muôi lên luôn ạ! | **5 GALLON** · đông đặc cả xô · R/350 · [0.65, 0.5] | cô trợ lý phòng thí nghiệm hoạt hình mặc áo blouse xanh nhạt đeo thẻ nhân viên nhấc một chiếc muôi to cắm vào xô nước biển 5 gallon có chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán, cả xô nước đông đặc nhấc bổng cả khối thạch lên mặt bàn. |
| b12 | 01:34.1–01:45.5 (11.4s) | L24 | Trợ lý chứng kiến tận mắt rồi đấy! Kỳ diệu ở chỗ: toàn bộ mạng lưới sợi tơ và chất nhầy chỉ chiếm chưa tới 0,1% tổng khối lượng, còn lại tới 99,9% đều là nước biển bị bắt giữ! | **0,1% TƠ** · giữ 99,9% nước · L/350 · [0.35, 0.45] | Biểu đồ tròn so sánh: 0,1% sợi tơ protein giữ trọn 99,9% nước biển xung quanh. |
| b13 | 01:45.5–01:54.8 (9.2s) | L25 | Tận dụng chính nước của môi trường để làm vũ khí bảo vệ mình, đúng là cỗ máy tiết kiệm nguyên liệu siêu đẳng nhất hành tinh! Cấp độ một: Phóng chất nhầy thành công mỹ mãn! |  | chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán bơi kiêu hãnh giữa làn nước trong bể; bảng Cấp độ 1 bật đèn xanh PASS rực rỡ. |

### scene03 · VŨ KHÍ BÓP NGHẸT KHIẾN CÁ MẬP HUNG DỮ PHẢI NHẢ VỘI · 76.1s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.8 (9.8s) | L26 | Trợ lý, nâng độ khó lên Cấp độ hai: Thử nghiệm vũ khí phòng thủ trước chúa tể đại dương! Trong chuỗi thức ăn dưới đáy biển sâu, cá mập hay cá mú khổng lồ là những sát thủ săn mồi tàn bạo nhất. |  | Bảng điện tử hiện CẤP ĐỘ 2: BÓP NGHẸT CHÚA TỂ ĐẠI DƯƠNG; ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước chỉ lên sơ đồ chuỗi thức ăn đáy biển sâu. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này. |
| b02 | 00:09.8–00:17.2 (7.4s) | L27 | Khi nhìn thấy Cỗ Máy Tạo Đờm bơi chậm chạp không vây, không vảy, không gai nhọn, con cá mập lập tức lao tới há rộng bộ hàm sắc nhọn đớp trọn con mồi vào họng! |  | chú cá mập xám hung dữ răng nhọn hoắt há to miệng ngạt thở hài hước hung dữ há rộng bộ hàm sắc nhọn lao tới đớp chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán đang bơi lững lờ. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này. |
| b03 | 00:17.2–00:26.8 (9.6s) | L28 | Khoảnh khắc hàm cá mập vừa nghiến xuống lớp da lỏng lẻo của cá mút đá, các túi tuyến hai bên sườn lập tức khai hỏa! 20 lít chất nhầy bùng nổ ngay bên trong khoang miệng của kẻ đi săn! | **20 LÍT ĐỜM** · nổ trong miệng · R/350 · [0.65, 0.48] | Hàm cá mập vừa nghiến vào lớp da cá mút đá, túi tuyến khai hỏa bùng nổ 20 lít chất nhầy trắng đặc ngay trong họng chú cá mập xám hung dữ răng nhọn hoắt há to miệng ngạt thở hài hước. |
| b04 | 00:26.8–00:32.5 (5.7s) | L29 | Điều kinh hoàng bắt đầu: cá mập thở bằng cách hút nước vào miệng rồi ép nước chảy qua các khe mang hai bên để lọc oxy. |  | Sơ đồ hô hấp cá mập: cá mập hút nước vào miệng rồi ép qua các khe mang hai bên để lọc oxy. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này. |
| b05 | 00:32.5–00:42.9 (10.4s) | L30 | Nhưng khối chất nhầy của Cỗ Máy Tạo Đờm là một loại polymer nhớt dính siêu cấp: dòng nước chảy qua mang càng mạnh, các sợi tơ keratin càng dãn dài và quấn chặt bít kín mít toàn bộ các khe mang thở của cá mập! |  | Sợi tơ keratin trong chất nhầy dãn dài quấn chặt bít kín mít toàn bộ các khe mang thở của cá mập như mạng nhện cao su. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này. |
| b06 | 00:42.9–00:49.7 (6.8s) | L31 | Báo cáo viện trưởng, cảm biến ghi nhận con cá mập đang quằn quại lắc đầu dữ dội, nó ho sặc sụa và nhả mẫu vật ra ngay lập tức kìa! |  | cô trợ lý phòng thí nghiệm hoạt hình mặc áo blouse xanh nhạt đeo thẻ nhân viên reo lên chỉ tay vào màn hình cảm biến: chú cá mập xám hung dữ răng nhọn hoắt há to miệng ngạt thở hài hước đang quằn quại lắc đầu dữ dội, ho sặc sụa và nhả chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo |
| b07 | 00:49.7–00:55.9 (6.2s) | L32 | Đúng thế các đồng nghiệp ạ! Bị bít kín mang là đồng nghĩa với việc bị bóp nghẹt khí quản nghẹt thở đến chết chỉ trong vài giây! |  | ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước giải thích: bị bít kín mang là đồng nghĩa với việc bị bóp nghẹt khí quản nghẹt thở đến chết chỉ trong vài giây. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này. |
| b08 | 00:55.9–01:03.0 (7.1s) | L33 | Con cá mập hoảng loạn nhả vội cá mút đá ra ngoài, liên tục ho khạc để cố tống mớ đờm dính ra khỏi khe mang rồi tháo chạy bạt mạng! |  | chú cá mập xám hung dữ răng nhọn hoắt há to miệng ngạt thở hài hước ho khạc hoảng loạn tống mớ đờm ra ngoài và tháo chạy bạt mạng khỏi đáy biển. |
| b09 | 01:03.0–01:16.1 (13.1s) | L34 | Các video gắn camera dưới đáy biển sâu đã ghi nhận hàng chục vụ tấn công của cá mập hay cá chình biển, và 100% kẻ săn mồi đều phải vội vã tháo chạy thề không bao giờ bén mảng lại gần! Cấp độ hai: Chúa tể biển sâu bị hạ đo ván! | **100% CHẠY** · không dám ăn · R/350 · [0.68, 0.45] | Màn hình camera đáy biển sâu ghi nhận 100% kẻ săn mồi cá mập và cá chình đều tháo chạy; bảng Cấp độ 2 bật PASS. |

### scene04 · ẢO THUẬT TỰ THẮT NÚT CƠ THỂ GẠT ĐỜM VÀ XÉ MỒI · 90.6s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.2 (9.2s) | L35 | Tăng cấp độ thử thách lên Cấp độ ba: Nghệ thuật cơ học tự thắt nút cơ thể! Sau khi phóng ra cả một biển chất nhầy nhớt bốc mùi bám đầy khắp người, Cỗ Máy Tạo Đờm phải đối mặt với một bài toán sinh tử: |  | Bảng điện tử hiện CẤP ĐỘ 3: NGHỆ THUẬT TỰ THẮT NÚT CƠ THỂ; ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước đặt bài toán sinh tử khi đờm bám kín thân cá mút đá. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này. |
| b02 | 00:09.2–00:18.1 (8.8s) | L36 | nếu không dọn sạch lớp đờm dính trên cơ thể mình, chính các khe mang thở của nó cũng sẽ bị nghẹt thở đến chết! Không có chân tay, không có vây, làm thế nào để nó gạt sạch lớp keo dính này? |  | chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán phủ đầy chất nhầy nhớt bốc mùi đang tìm cách giải cứu chính mình, không chân không vây. |
| b03 | 00:18.1–00:30.0 (11.9s) | L37 | Và đây là lúc tuyệt kỹ ảo thuật đỉnh cao bậc nhất giới động vật xuất hiện! Cỗ Máy Tạo Đờm uốn cong chiếc đuôi, tự luồn cơ thể mình qua một vòng tròn để tạo thành một nút thắt thòng lọng hình số tám quanh thân! |  | chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán uốn cong chiếc đuôi, tự luồn cơ thể mình qua một vòng tròn tạo thành nút thắt hình số tám quanh thân cực kỳ điêu luyện. |
| b04 | 00:30.0–00:35.1 (5.1s) | L38 | Sau đó, nó co bóp các bó cơ dọc sống lưng để trượt nút thắt đó di chuyển từ từ từ đầu xuống tận đuôi! |  | chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán co bóp các bó cơ dọc sống lưng để trượt nút thắt di chuyển từ đầu xuống đuôi. |
| b05 | 00:35.1–00:43.9 (8.8s) | L39 | Chiếc nút thắt di động này đóng vai trò như một chiếc cần gạt nước kính ô tô, miết chặt vào da và cạo sạch bong toàn bộ lớp chất nhầy nhớt trôi tuột ra ngoài cơ thể trong vài giây! |  | Vòng thắt di động hình số tám trượt dọc thân như chiếc cần gạt nước ô tô, lau sạch bong toàn bộ lớp bọt nhớt trôi tuột ra ngoài trong vài giây. |
| b06 | 00:43.9–00:56.9 (13.0s) | L40 | Chưa hết đâu các đồng nghiệp! Vì loài cá này hoàn toàn không có hàm răng trên dưới để nhai cắn, khi tìm thấy một xác cá voi chết chìm dưới đáy biển sâu, nó lại dùng đúng tuyệt kỹ thắt nút này: cắm chiếc đĩa lưỡi có gai sừng keratin vào thịt xác chết, |  | Dưới đáy biển sâu bên cạnh tảng thức ăn biển: chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán cắm đĩa lưỡi gai sừng keratin bám chắc vào khối thức ăn. |
| b07 | 00:56.9–01:02.6 (5.7s) | L41 | rồi thắt nút cơ thể tỳ mạnh vào tảng thịt để tạo đòn bẩy xé toạc từng mảng thức ăn! Không có hàm răng, |  | chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán thắt nút cơ thể tỳ mạnh vào tảng thịt tạo đòn bẩy xé toạc từng mảng thịt ngon lành. |
| b08 | 01:02.6–01:05.5 (2.9s) | L42 | nó lấy chính cơ thể mình làm chiếc cờ-lê cơ học! |  | chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán uốn thân tạo đòn bẩy cơ học thông minh như chiếc cờ-lê, mặt cười toe toét thưởng thức bữa ăn ngon lành dưới đáy biển. |
| b09 | 01:05.5–01:14.5 (9.0s) | L43 | Đặc biệt nhất, khi chui rúc sâu vào bên trong những xác chết khổng lồ tăm tối nơi nồng độ oxy gần như bằng không, Cỗ Máy Tạo Đờm lại kích hoạt một năng lực chấn động giới sinh học: |  | Khung cảnh đáy biển sâu tối thẫm: chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán lặn sâu vào nơi nồng độ oxy gần bằng không mà vẫn bơi lội khỏe mạnh. |
| b10 | 01:14.5–01:19.8 (5.4s) | L44 | nó có thể hấp thụ trực tiếp các chất dinh dưỡng và axit amin xuyên qua lớp da và mang của mình! | **ĂN QUA DA** · hấp thụ axit amin · R/350 · [0.65, 0.48] | Mặt cắt da chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán: các phân tử axit amin và dưỡng chất thấm trực tiếp qua da và mang vào máu. |
| b11 | 01:19.8–01:30.6 (10.8s) | L45 | Đây là loài động vật có xương sống duy nhất trên Trái Đất được ghi nhận có khả năng ăn thức ăn bằng da chẳng khác nào các loài giun biển nguyên thủy! Cấp độ ba: Hoàn thành xuất sắc tuyệt đối không tì vết! |  | So sánh tiến hóa: chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán là loài có xương sống duy nhất ăn bằng da như giun biển nguyên thủy; bảng Cấp độ 3 bật PASS rực rỡ. |

### scene05 · VỤ LẬT XE TRÊN CAO TỐC OREGON VÀ SỢI TƠ TƯƠNG LAI · 85.5s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:10.2 (10.2s) | L46 | Nâng công suất máy quét lên Cấp độ bốn: Khảo nghiệm sự kiện thực tế kinh điển ngoài đời thực! Nếu các đồng nghiệp vẫn nghĩ chất nhầy của Cỗ Máy Tạo Đờm chỉ là chuyện viễn tưởng dưới đáy biển sâu, |  | Bảng điện tử hiện CẤP ĐỘ 4: KHẢO NGHIỆM SỰ KIỆN OREGON 2017; ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước giở tài liệu thời gian. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này. |
| b02 | 00:10.2–00:16.4 (6.2s) | L47 | thì hãy quay ngược thời gian về ngày 13/7/2017 trên Quốc lộ 101 bang Oregon nước Mỹ! | **QL 101** · tai nạn Oregon 2017 · L/350 · [0.35, 0.45] | Tấm biển Quốc lộ 101 bang Oregon nước Mỹ mở ra trên màn hình với ngày 13/7/2017. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này. |
| b03 | 00:16.4–00:26.9 (10.5s) | L48 | Báo cáo cảnh sát giao thông: Một chiếc xe tải chở 7.500 pound — tức là gần 3.400kg cá mút đá sống đang trên đường vận chuyển — bỗng nhiên gặp sự cố phanh gấp và lật nhào ngang giữa đường cao tốc! | **3.400 KG** · cá mút đá sống · R/350 · [0.65, 0.48] | Chiếc xe tải chở 7.500 pound (3.400kg) cá mút đá sống gặp sự cố phanh gấp và lật nhào ngang giữa đường cao tốc nhựa đen. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này. |
| b04 | 00:26.9–00:33.7 (6.7s) | L49 | Hàng ngàn chú cá mút đá bị văng ra khỏi thùng chứa, rơi lộp độp xuống mặt đường nhựa nóng rực và bị kích động hoảng loạn tột độ. |  | Hàng ngàn chú cá mút đá văng ra khỏi thùng chứa, rơi lộp độp xuống mặt đường nhựa nóng rực. |
| b05 | 00:33.7–00:43.9 (10.2s) | L50 | Đồng loạt hàng ngàn Cỗ Máy Tạo Đờm kích hoạt cơ chế tự vệ: chúng xả hàng tấn chất nhầy nhớt bao phủ kín mít mặt đường cao tốc và trùm lên một chiếc xe ô tô con gần đó như cảnh tượng trong phim quái vật ngoài hành tinh! |  | Hàng tấn chất nhầy nhớt bao phủ kín mít mặt đường cao tốc và trùm lên một chiếc xe ô tô con màu trắng như phim quái vật ngoài hành tinh. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này. |
| b06 | 00:43.9–00:55.5 (11.5s) | L51 | Đội cứu hỏa và cảnh sát giao thông bang Oregon phải điều động máy ủi đất và vòi rồng cứu hỏa công suất cực đại phun nước cật lực suốt nhiều giờ liền mới dọn dẹp sạch được bãi chiến trường nhầy nhụa trơn như đổ mỡ! |  | Máy ủi đất và lính cứu hỏa cầm vòi rồng phun nước cật lực dọn dẹp bãi chiến trường nhầy nhụa trơn như đổ mỡ trên đường cao tốc. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này. |
| b07 | 00:55.5–00:59.6 (4.1s) | L52 | Vụ tai nạn trở thành đề tài sốt dẻo trên toàn bộ các mặt báo quốc tế! |  | Các mặt báo quốc tế giật tít sốt dẻo về bãi đờm khổng lồ phong tỏa cao tốc Oregon. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này. |
| b08 | 00:59.6–01:05.9 (6.3s) | L53 | Từ sự kiện chấn động đó, các nhà khoa học vật liệu quân sự của Hải quân Mỹ đã vào cuộc nghiên cứu sâu sợi tơ của cá mút đá. |  | Các nhà khoa học vật liệu quân sự của Hải quân Mỹ vào cuộc nghiên cứu cấu trúc phân tử sợi tơ của cá mút đá trên kính hiển vi. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này. |
| b09 | 01:05.9–01:15.0 (9.1s) | L54 | Kết quả cho thấy các sợi protein keratin trong chất nhầy mỏng gấp 100 lần sợi tóc người nhưng có độ bền kéo và độ dẻo dai tương đương tơ nhện và sợi ni-lông nhân tạo! | **1/100 TÓC** · bền ngang tơ nhện · L/350 · [0.35, 0.45] | Phóng đại sợi tơ protein keratin mỏng gấp 100 lần sợi tóc người nhưng có độ bền kéo và độ dẻo dai tương đương tơ nhện và sợi ni-lông nhân tạo. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này. |
| b10 | 01:15.0–01:25.5 (10.5s) | L55 | Người ta đang nghiên cứu dùng loại sợi sinh học này để dệt quần áo chống đạn, làm sợi chỉ khâu y tế tự tiêu và chế tạo màng dập lửa thân thiện với môi trường! Cấp độ bốn: Vượt qua xuất sắc! |  | Mô hình ứng dụng tương lai: áo giáp chống đạn dệt từ tơ cá mút đá, chỉ khâu phẫu thuật tự tiêu và bình cứu hỏa sinh học; bảng Cấp độ 4 bật PASS. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này. |

### scene06 · KHẮC TINH HẢI QUỲ VÀ BÓNG ĐEN ĐIỆP VIÊN ĐẠI DƯƠNG · 75.3s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.7 (8.7s) | L56 | Bước vào Cấp độ tối thượng: Liệu Cỗ Máy Tạo Đờm có thực sự bất tử dưới đáy đại dương? Cá mập cắn phải nhả. Cá mú đớp phải ho khạc. Bị mắc kẹt thì tự thắt nút tẩu thoát. |  | Bảng điện tử chớp sáng chữ CẤP ĐỘ TỐI THƯỢNG: TRÙM CUỐI ĐẠI DƯƠNG; ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước khoanh tay trầm ngâm suy nghĩ trước bể nuôi. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này. |
| b02 | 00:08.7–00:12.2 (3.5s) | L57 | Chẳng lẽ quái vật này không có lấy một kẻ thù tự nhiên nào sao? |  | Mô hình đồ họa 4 chiến tích của cá mút đá đặt cạnh dấu hỏi lớn: liệu sinh vật này có khắc tinh tự nhiên nào không? KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này. |
| b03 | 00:12.2–00:21.5 (9.3s) | L58 | Và đây là câu trả lời bất ngờ: Khắc tinh số một đánh bại được Cỗ Máy Tạo Đờm lại là những sinh vật... không hề có mang để thở! Đó là những bông hải quỳ ăn thịt khổng lồ và các loài chim biển! |  | Một bông hải quỳ ăn thịt khổng lồ dưới đáy biển và chim biển xuất hiện như những sinh vật không hề có mang thở. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này. |
| b04 | 00:21.5–00:32.2 (10.7s) | L59 | Hải quỳ săn mồi bằng xúc tu có tế bào gai châm độc, nuốt chửng con mồi qua khoang bụng mở mà không cần hút nước qua mang, nên chất nhầy của cá mút đá hoàn toàn mất tác dụng! Đúng là vỏ quýt dày có móng tay nhọn! |  | Hải quỳ dùng các xúc tu châm nọc nuốt trọn cá mút đá qua khoang bụng mở mà không cần mang thở, chất nhầy bị vô hiệu hóa hoàn toàn. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này. |
| b05 | 00:32.2–00:39.3 (7.1s) | L60 | Tổng kết ghi chép phòng thí nghiệm số 24: Mẫu vật đạt điểm 10 tuyệt đối cho cỗ máy phòng thủ chất nhầy kỳ dị nhất tiến hóa! | **ĐIỂM 10** · phòng thủ chất nhầy · R/350 · [0.58, 0.45] | ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước giơ tấm bảng điểm 10 tuyệt đối trao cho chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán; cả phòng lab vỗ tay khen ngợi cỗ máy phòng thủ chất nhầy k |
| b06 | 00:39.3–00:50.9 (11.6s) | L61 | Còn các trợ lý thì sao? Nếu được sở hữu một trong hai năng lực: biến cả xô nước thành keo nhớt trong 1 giây, hay tự thắt nút cơ thể hình số tám để trốn thoát, bạn chọn cái nào? Hãy bình luận lựa chọn của bạn bên dưới nhé! |  | Hai bàn cân lựa chọn: BÊN TRÁI biểu tượng xô nước biến thành keo nhớt trong 1 giây; BÊN PHẢI biểu tượng tự thắt nút cơ thể hình số 8, các bạn nhỏ giơ thẻ bình luận. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này. |
| b07 | 00:50.9–00:59.2 (8.3s) | L62 | Hồ sơ phòng thí nghiệm hôm nay xin tạm khép lại. Nhưng tập sau, chúng ta sẽ bước vào hồ sơ thế giới ngầm đại dương để điều tra một siêu điệp viên bí ẩn bậc nhất biển cả! |  | ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước đóng tập hồ sơ số 24 lại, ánh đèn chuyển sang ánh sáng mờ ảo của thế giới ngầm đại dương với bản đồ kho báu bí ẩn. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này. |
| b08 | 00:59.2–01:04.3 (5.1s) | L63 | Một sinh vật sở hữu tới 9 bộ não độc lập, 3 trái tim đập nhịp nhàng, dòng máu màu xanh lam huyền bí, | **9 NÃO** · siêu điệp viên biển · L/350 · [0.35, 0.45]<br>**3 TIM** · máu màu xanh lam · R/480 · [0.68, 0.55] | Một sinh vật bí ẩn được vẽ hoàn toàn bằng BÓNG ĐEN ĐẶC TUYỀN (solid black silhouette) hình bạch tuộc 8 xúc tu uốn lượn, bên trong hiện đồ họa 9 bộ não nhỏ phát sáng, 3 quả tim và dòng máu xanh lam, có dấu hỏi chấm vàng to tướng phía trên; KHÔNG vẽ rõ mắt hay màu da. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này. |
| b09 | 01:04.3–01:10.8 (6.5s) | L64 | và sở hữu tài hóa trang thiên bẩm: có thể biến hình mượt mà thành 15 loài sinh vật kịch độc khác nhau dưới đáy biển chỉ trong chớp mắt! | **15 LOÀI** · tuyệt kỹ biến hình · R/350 · [0.65, 0.48] | Chiếc BÓNG ĐEN ĐẶC TUYỀN bí ẩn có 8 xúc tu đang biến hình thành các loài sinh vật biển kịch độc như rắn biển và cá mao tiên. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này. |
| b10 | 01:10.8–01:15.3 (4.5s) | L65 | Đố các bạn biết bóng đen bí ẩn kỳ sau là loài vật nào? Hãy đoán ngay ở phần bình luận nhé! |  | Chiếc BÓNG ĐEN ĐẶC TUYỀN bí ẩn nằm giữa ba dấu hỏi chấm vàng cam lấp lánh mời gọi khán giả bình luận đoán tên con vật kỳ sau. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này. |

## 5. Phân cảnh Shorts — từng beat

Banner: **BIẾN 20 LÍT NƯỚC / THÀNH KEO NHỚT?!** · giọng 48.9s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Chỉ cần một con cá mập vừa cắn vào thân, |  |
| s02 | 00:02.9 | S02 | loài vật này có thể biến 20 lít nước biển xung quanh thành một khối keo nhớt đặc quánh | **20 LÍT KEO** · trong 0,4 giây · R/560 · [0.58, 0.48] |
| s03 | 00:07.3 | S10 | chỉ trong 0,4 giây làm kẻ săn mồi suýt chết ngạt! |  |
| s04 | 00:11.2 | S03 | Đây là Cá Mút Đá Hagfish, sinh vật cổ đại 300 triệu năm dài 0,5m sống dưới đáy biển sâu. | **300 TR NĂM** · cổ đại không xương · L/720 · [0.42, 0.55] |
| s05 | 00:16.2 | S04 | Cơ thể nó không có xương sống, có tới 4 quả tim độc lập, và sở hữu hàng trăm lỗ xả chất nhầy hai bên sườn! | **4 QUẢ TIM** · bơm máu độc lập · R/620 · [0.62, 0.52] |
| s06 | 00:21.9 | S05 | Khi bị tấn công, các sợi tơ protein dãn nở gấp 10.000 lần bít kín hoàn toàn các khe mang thở của cá mập | **10.000 LẦN** · dãn nở bít mang · L/650 · [0.45, 0.5] |
| s07 | 00:27.6 | S06 | khiến kẻ đi săn ho sặc sụa phải nhả vội ra tẩu thoát! |  |
| s08 | 00:31.2 | S07 | Để gạt sạch đờm khỏi người mình, nó tự thắt cơ thể thành nút thòng lọng hình số tám từ đầu đến đuôi như ảo thuật gia! |  |
| s09 | 00:37.5 | S08 | 2017, một xe tải chở 3.400kg cá mút đá lật nhào | **3.400 KG** · lật xe Oregon 2017 · R/650 · [0.58, 0.5] |
| s10 | 00:41.5 | S11 | đã biến cả đường cao tốc ở Mỹ thành một biển chất nhầy nhớt trượt ngã cả xe cứu hỏa! |  |
| s11 | 00:46.3 | S09 | Một cỗ máy tạo đờm độc nhất vô nhị của đại dương! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ghi chép thí nghiệm phòng lab đáy biển sâu, ca trực rạng sáng. Đèn huỳnh quang tím bật sáng chiếu thẳng vào bể cách ly số 24.". Bố cục: Phòng thí nghiệm đáy biển sâu ca trực rạng sáng: ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước và cô trợ lý phòng thí nghiệm hoạt hình mặc áo blouse xanh nhạt đeo thẻ nhân viên đứng trước bể cách ly số 24 phát sáng ánh huỳnh quang tím. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giữa đáy nước lạnh ngắt, một sinh vật dài ngoằng trơn nhẫy như sợi dây thừng màu hồng xám đang cuộn tròn bất động...". Bố cục: Bên trong làn nước lạnh ngắt, chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán dài ngoằng trơn nhẫy như sợi dây thừng màu hồng xám đang cuộn tròn bồng bềnh dưới đáy bể.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không có hàm răng trên dưới. Không có cột sống lưng. Không có lấy một chiếc vây bơi hoàn chỉnh. Và đôi mắt thì thoái hóa thành hai đốm trắng mờ đục chẳng nhìn thấy nổi ánh sáng mặt trời!". Bố cục: Bốn ô đồ họa chẩn đoán gạch chéo đỏ: không có hàm răng trên dưới, không có cột sống lưng, không có vây bơi, và đôi mắt mờ đục. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Viện trưởng ơi, mẫu vật này nhìn trơn tuột lù đù như cọng bún thiu, thả vào bể nuôi chung với cá mập lỡ bị nuốt chửng thì sao ạ?". Bố cục: BÊN TRÁI cô trợ lý phòng thí nghiệm hoạt hình mặc áo blouse xanh nhạt đeo thẻ nhân viên lo lắng nhìn vào bể kính tưởng tượng chú cá mút đá bị con cá mập to nuốt chửng; BÊN PHẢI chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán trôi lờ đờ ngơ ngác.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trợ lý ngây thơ quá rồi! Nếu có con cá mập nào dại dột đớp phải mẫu vật này, thì kẻ phải cầu cứu đội cấp cứu chính là con cá mập chứ không phải nó đâu!". Bố cục: ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước bật cười lắc ngón tay chỉ lên màn hình: hình ảnh con cá mập phải gọi xe cứu thương cấp cứu vì trót đớp phải cá mút đá.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Xin giới thiệu với các đồng nghiệp: đây là Cá Mút Đá Hagfish, sinh vật cổ đại thuộc lớp Myxini, một trong những nhánh động vật có hộp sọ nguyên thủy nhất hành tinh.". Bố cục: Bản đồ cây tiến hóa đại dương cổ đại giới thiệu lớp Myxini có hộp sọ nguyên thủy nhất; chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán uốn lượn đội chiếc vương miện cổ xưa.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chiều dài trung bình từ 40-80cm.". Bố cục: Ở GIỮA chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán nằm thẳng cạnh chiếc thước đo chiều cao màu vàng 40-80cm của phòng thí nghiệm.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong giới sinh vật học, chúng tôi gọi thẳng tên nó bằng biệt danh: Cỗ Máy Tạo Đờm!". Bố cục: chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán tự hào đeo dải băng danh hiệu Cỗ Máy Tạo Đờm, xung quanh bắn ra những giọt bọt nước phát sáng ngộ nghĩnh.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tổ tiên của nó đã tung tăng dưới đáy biển từ hơn 300 triệu năm trước, tức là xuất hiện trước cả loài khủng long bạo chúa, sống sót qua hàng loạt đại tuyệt chủng mà chẳng thèm thay đổi hình dáng!". Bố cục: Dòng thời gian 300 triệu năm: tổ tiên chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán bơi tung tăng dưới đáy biển kỷ Phấn trắng trước cả thời khủng long bạo chúa T-Rex đứng trên bờ gầm rú.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Toàn bộ cơ thể nó chỉ có hộp sọ bằng sụn dẻo, không có đốt sống thật, nhưng lại sở hữu tới 4 quả tim độc lập để bơm máu!". Bố cục: Mặt cắt giải phẫu trong suốt của chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán: hộp sọ bằng sụn dẻo và 4 quả tim độc lập màu đỏ tươi đang đập rộn ràng bơm máu khắp thân.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và thứ vũ khí sinh học kinh dị giúp nó bất khả chiến bại suốt hàng trăm triệu năm qua chính là khả năng phóng ra một đại dương chất nhầy đặc quánh làm ngạt thở mọi kẻ săn mồi!". Bố cục: chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán phóng ra một làn sóng chất nhầy bọt trắng bao phủ cả một vùng nước biển làm một đàn cá săn mồi ho sặc sụa dạt ra xa.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đêm nay, tôi tuyên bố kích hoạt hệ thống thử thách 5 cấp độ cực hạn để giải mã Cỗ Máy Tạo Đờm!". Bố cục: ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước gạt cần gạt lớn; bảng đèn LED bật sáng dòng chữ THỬ THÁCH 5 CẤP ĐỘ CỰC HẠN.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khởi động Cấp độ một: Thử thách công suất phóng chất nhầy! Nhìn từ bên ngoài, làn da của Cỗ Máy Tạo Đờm mềm mại, lỏng lẻo như một chiếc áo khoác quá khổ mượn của anh trai.". Bố cục: Bảng điện tử hiện CẤP ĐỘ 1: THỬ THÁCH CÔNG SUẤT PHÓNG CHẤT NHẦY; chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán có làn da mềm mại như chiếc áo khoác quá khổ lỏng lẻo.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng nếu bạn soi kính hiển vi chạy dọc hai bên sườn của nó, bạn sẽ đếm được từ 100 đến 150 lỗ chân lông đặc biệt. Đó chính là miệng xả của hàng trăm túi tuyến chất nhầy sinh học tối tân!". Bố cục: Kính hiển vi chạy dọc hai bên sườn chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán: hiển thị từ 100 đến 150 lỗ chân lông đặc biệt là miệng xả của các túi tuyến chất nhầy.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy quan sát thí nghiệm khi một kẻ thù vừa chạm miệng vào người nó! Ngay lập tức, các túi tuyến này bóp nghẹt,". Bố cục: Một chiếc que gắp phòng lab chạm nhẹ vào thân chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán; các túi tuyến hai bên sườn lập tức bóp mạnh chuẩn bị khai hỏa.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bắn ra một lượng dịch đục chỉ nhỏ bằng hạt đậu. Nhưng khoảnh khắc giọt dịch chạm vào nước biển, một phản ứng dây chuyền nổ tung!". Bố cục: Túi tuyến bắn ra một giọt dịch đục nhỏ bằng hạt đậu rơi vào nước biển, bắt đầu phản ứng dây chuyền nổ tung.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chỉ trong vòng đúng 0,4 giây — tức là nhanh hơn một cái chớp mắt của con người —". Bố cục: Đồng hồ cát siêu tốc đếm 0,4 giây nhấp nháy đỏ rực; giọt dịch nhỏ chạm vào nước biển phát nổ dây chuyền thần tốc.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "giọt dịch nhỏ xíu đó lập tức trương nở thể tích lên gấp 10.000 lần! Một con cá mút đá dài 0,5m có thể biến toàn bộ 20 lít nước biển xung quanh thành một khối keo nhớt đặc quánh, sánh mịn chẳng khác nào một xô thạch khổng lồ!". Bố cục: Giọt dịch trương nở 10.000 lần, biến toàn bộ 20 lít nước biển xung quanh thành một khối keo nhớt đặc quánh sánh mịn như xô thạch khổng lồ.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Làm thế nào mà một giọt dịch bé tí lại biến cả xô nước thành keo dính nhanh đến mức ma quái như vậy?". Bố cục: ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước cầm chiếc kính lúp to tướng soi vào giọt dịch phát sáng, đặt dấu hỏi lớn về tốc độ tạo keo nhớt phi thường. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tiến sĩ Douglas Fudge tại phòng thí nghiệm cơ sinh học đã giải mã bí ẩn dưới kính hiển vi: bên trong túi dịch chứa hàng ngàn cuộn sợi tơ protein siêu nhỏ làm từ chất sừng keratin, mỗi sợi cuộn chặt như một cuộn chỉ may vá tinh xảo.". Bố cục: Tiến sĩ Douglas Fudge tại phòng lab soi kính hiển vi: bên trong giọt dịch chứa hàng ngàn cuộn sợi tơ protein keratin cuộn tròn như cuộn chỉ may.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi gặp nước biển và lực xoáy, các cuộn chỉ tự bung sợi với vận tốc ánh sáng, đan cài vào các hạt chất nhầy hút nước giữ chặt mọi phân tử nước biển lại!". Bố cục: Sơ đồ hiển vi: các cuộn chỉ tơ keratin bung sợi với vận tốc cực nhanh, đan xen vào các hạt chất nhầy hút giữ chặt mọi phân tử nước biển.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kết quả tạo ra một loại vật liệu siêu nhớt không phải gel đặc, mà là một khối mạng lưới chất lỏng đàn hồi vô cùng bền bỉ! Kẻ thù chưa kịp cắn miếng nào đã thấy miệng mình ngập ngụa trong cả biển đờm nhầy nhụa!". Bố cục: Một khối mạng lưới chất lỏng đàn hồi siêu nhớt bao bọc lấy kẻ thù; một con cá săn mồi há hốc mồm ngập ngụa trong đờm nhầy nhụa.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Viện trưởng ơi, em thử đong một xô nước biển 5 gallon, thả một chú cá mút đá vào quấy nhẹ một cái là cả xô nước đông đặc nhấc bổng cả cái muôi lên luôn ạ!". Bố cục: cô trợ lý phòng thí nghiệm hoạt hình mặc áo blouse xanh nhạt đeo thẻ nhân viên nhấc một chiếc muôi to cắm vào xô nước biển 5 gallon có chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán, cả xô nước đông đặc nhấc bổng cả khối thạch lên mặt bàn.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trợ lý chứng kiến tận mắt rồi đấy! Kỳ diệu ở chỗ: toàn bộ mạng lưới sợi tơ và chất nhầy chỉ chiếm chưa tới 0,1% tổng khối lượng, còn lại tới 99,9% đều là nước biển bị bắt giữ!". Bố cục: Biểu đồ tròn so sánh: 0,1% sợi tơ protein giữ trọn 99,9% nước biển xung quanh.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tận dụng chính nước của môi trường để làm vũ khí bảo vệ mình, đúng là cỗ máy tiết kiệm nguyên liệu siêu đẳng nhất hành tinh! Cấp độ một: Phóng chất nhầy thành công mỹ mãn!". Bố cục: chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán bơi kiêu hãnh giữa làn nước trong bể; bảng Cấp độ 1 bật đèn xanh PASS rực rỡ.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trợ lý, nâng độ khó lên Cấp độ hai: Thử nghiệm vũ khí phòng thủ trước chúa tể đại dương! Trong chuỗi thức ăn dưới đáy biển sâu, cá mập hay cá mú khổng lồ là những sát thủ săn mồi tàn bạo nhất.". Bố cục: Bảng điện tử hiện CẤP ĐỘ 2: BÓP NGHẸT CHÚA TỂ ĐẠI DƯƠNG; ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước chỉ lên sơ đồ chuỗi thức ăn đáy biển sâu. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi nhìn thấy Cỗ Máy Tạo Đờm bơi chậm chạp không vây, không vảy, không gai nhọn, con cá mập lập tức lao tới há rộng bộ hàm sắc nhọn đớp trọn con mồi vào họng!". Bố cục: chú cá mập xám hung dữ răng nhọn hoắt há to miệng ngạt thở hài hước hung dữ há rộng bộ hàm sắc nhọn lao tới đớp chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán đang bơi lững lờ. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khoảnh khắc hàm cá mập vừa nghiến xuống lớp da lỏng lẻo của cá mút đá, các túi tuyến hai bên sườn lập tức khai hỏa! 20 lít chất nhầy bùng nổ ngay bên trong khoang miệng của kẻ đi săn!". Bố cục: Hàm cá mập vừa nghiến vào lớp da cá mút đá, túi tuyến khai hỏa bùng nổ 20 lít chất nhầy trắng đặc ngay trong họng chú cá mập xám hung dữ răng nhọn hoắt há to miệng ngạt thở hài hước.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Điều kinh hoàng bắt đầu: cá mập thở bằng cách hút nước vào miệng rồi ép nước chảy qua các khe mang hai bên để lọc oxy.". Bố cục: Sơ đồ hô hấp cá mập: cá mập hút nước vào miệng rồi ép qua các khe mang hai bên để lọc oxy. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng khối chất nhầy của Cỗ Máy Tạo Đờm là một loại polymer nhớt dính siêu cấp: dòng nước chảy qua mang càng mạnh, các sợi tơ keratin càng dãn dài và quấn chặt bít kín mít toàn bộ các khe mang thở của cá mập!". Bố cục: Sợi tơ keratin trong chất nhầy dãn dài quấn chặt bít kín mít toàn bộ các khe mang thở của cá mập như mạng nhện cao su. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo viện trưởng, cảm biến ghi nhận con cá mập đang quằn quại lắc đầu dữ dội, nó ho sặc sụa và nhả mẫu vật ra ngay lập tức kìa!". Bố cục: cô trợ lý phòng thí nghiệm hoạt hình mặc áo blouse xanh nhạt đeo thẻ nhân viên reo lên chỉ tay vào màn hình cảm biến: chú cá mập xám hung dữ răng nhọn hoắt há to miệng ngạt thở hài hước đang quằn quại lắc đầu dữ dội, ho sặc sụa và nhả chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán ra ngay lập tức.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đúng thế các đồng nghiệp ạ! Bị bít kín mang là đồng nghĩa với việc bị bóp nghẹt khí quản nghẹt thở đến chết chỉ trong vài giây!". Bố cục: ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước giải thích: bị bít kín mang là đồng nghĩa với việc bị bóp nghẹt khí quản nghẹt thở đến chết chỉ trong vài giây. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Con cá mập hoảng loạn nhả vội cá mút đá ra ngoài, liên tục ho khạc để cố tống mớ đờm dính ra khỏi khe mang rồi tháo chạy bạt mạng!". Bố cục: chú cá mập xám hung dữ răng nhọn hoắt há to miệng ngạt thở hài hước ho khạc hoảng loạn tống mớ đờm ra ngoài và tháo chạy bạt mạng khỏi đáy biển.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các video gắn camera dưới đáy biển sâu đã ghi nhận hàng chục vụ tấn công của cá mập hay cá chình biển, và 100% kẻ săn mồi đều phải vội vã tháo chạy thề không bao giờ bén mảng lại gần! Cấp độ hai: Chúa tể biển sâu bị hạ đo ván!". Bố cục: Màn hình camera đáy biển sâu ghi nhận 100% kẻ săn mồi cá mập và cá chình đều tháo chạy; bảng Cấp độ 2 bật PASS.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tăng cấp độ thử thách lên Cấp độ ba: Nghệ thuật cơ học tự thắt nút cơ thể! Sau khi phóng ra cả một biển chất nhầy nhớt bốc mùi bám đầy khắp người, Cỗ Máy Tạo Đờm phải đối mặt với một bài toán sinh tử:". Bố cục: Bảng điện tử hiện CẤP ĐỘ 3: NGHỆ THUẬT TỰ THẮT NÚT CƠ THỂ; ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước đặt bài toán sinh tử khi đờm bám kín thân cá mút đá. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nếu không dọn sạch lớp đờm dính trên cơ thể mình, chính các khe mang thở của nó cũng sẽ bị nghẹt thở đến chết! Không có chân tay, không có vây, làm thế nào để nó gạt sạch lớp keo dính này?". Bố cục: chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán phủ đầy chất nhầy nhớt bốc mùi đang tìm cách giải cứu chính mình, không chân không vây.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và đây là lúc tuyệt kỹ ảo thuật đỉnh cao bậc nhất giới động vật xuất hiện! Cỗ Máy Tạo Đờm uốn cong chiếc đuôi, tự luồn cơ thể mình qua một vòng tròn để tạo thành một nút thắt thòng lọng hình số tám quanh thân!". Bố cục: chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán uốn cong chiếc đuôi, tự luồn cơ thể mình qua một vòng tròn tạo thành nút thắt hình số tám quanh thân cực kỳ điêu luyện.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sau đó, nó co bóp các bó cơ dọc sống lưng để trượt nút thắt đó di chuyển từ từ từ đầu xuống tận đuôi!". Bố cục: chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán co bóp các bó cơ dọc sống lưng để trượt nút thắt di chuyển từ đầu xuống đuôi.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chiếc nút thắt di động này đóng vai trò như một chiếc cần gạt nước kính ô tô, miết chặt vào da và cạo sạch bong toàn bộ lớp chất nhầy nhớt trôi tuột ra ngoài cơ thể trong vài giây!". Bố cục: Vòng thắt di động hình số tám trượt dọc thân như chiếc cần gạt nước ô tô, lau sạch bong toàn bộ lớp bọt nhớt trôi tuột ra ngoài trong vài giây.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa hết đâu các đồng nghiệp! Vì loài cá này hoàn toàn không có hàm răng trên dưới để nhai cắn, khi tìm thấy một xác cá voi chết chìm dưới đáy biển sâu, nó lại dùng đúng tuyệt kỹ thắt nút này: cắm chiếc đĩa lưỡi có gai sừng keratin vào thịt xác chết,". Bố cục: Dưới đáy biển sâu bên cạnh tảng thức ăn biển: chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán cắm đĩa lưỡi gai sừng keratin bám chắc vào khối thức ăn.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "rồi thắt nút cơ thể tỳ mạnh vào tảng thịt để tạo đòn bẩy xé toạc từng mảng thức ăn! Không có hàm răng,". Bố cục: chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán thắt nút cơ thể tỳ mạnh vào tảng thịt tạo đòn bẩy xé toạc từng mảng thịt ngon lành.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nó lấy chính cơ thể mình làm chiếc cờ-lê cơ học!". Bố cục: chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán uốn thân tạo đòn bẩy cơ học thông minh như chiếc cờ-lê, mặt cười toe toét thưởng thức bữa ăn ngon lành dưới đáy biển.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đặc biệt nhất, khi chui rúc sâu vào bên trong những xác chết khổng lồ tăm tối nơi nồng độ oxy gần như bằng không, Cỗ Máy Tạo Đờm lại kích hoạt một năng lực chấn động giới sinh học:". Bố cục: Khung cảnh đáy biển sâu tối thẫm: chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán lặn sâu vào nơi nồng độ oxy gần bằng không mà vẫn bơi lội khỏe mạnh.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nó có thể hấp thụ trực tiếp các chất dinh dưỡng và axit amin xuyên qua lớp da và mang của mình!". Bố cục: Mặt cắt da chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán: các phân tử axit amin và dưỡng chất thấm trực tiếp qua da và mang vào máu.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đây là loài động vật có xương sống duy nhất trên Trái Đất được ghi nhận có khả năng ăn thức ăn bằng da chẳng khác nào các loài giun biển nguyên thủy! Cấp độ ba: Hoàn thành xuất sắc tuyệt đối không tì vết!". Bố cục: So sánh tiến hóa: chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán là loài có xương sống duy nhất ăn bằng da như giun biển nguyên thủy; bảng Cấp độ 3 bật PASS rực rỡ.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nâng công suất máy quét lên Cấp độ bốn: Khảo nghiệm sự kiện thực tế kinh điển ngoài đời thực! Nếu các đồng nghiệp vẫn nghĩ chất nhầy của Cỗ Máy Tạo Đờm chỉ là chuyện viễn tưởng dưới đáy biển sâu,". Bố cục: Bảng điện tử hiện CẤP ĐỘ 4: KHẢO NGHIỆM SỰ KIỆN OREGON 2017; ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước giở tài liệu thời gian. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "thì hãy quay ngược thời gian về ngày 13/7/2017 trên Quốc lộ 101 bang Oregon nước Mỹ!". Bố cục: Tấm biển Quốc lộ 101 bang Oregon nước Mỹ mở ra trên màn hình với ngày 13/7/2017. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo cảnh sát giao thông: Một chiếc xe tải chở 7.500 pound — tức là gần 3.400kg cá mút đá sống đang trên đường vận chuyển — bỗng nhiên gặp sự cố phanh gấp và lật nhào ngang giữa đường cao tốc!". Bố cục: Chiếc xe tải chở 7.500 pound (3.400kg) cá mút đá sống gặp sự cố phanh gấp và lật nhào ngang giữa đường cao tốc nhựa đen. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hàng ngàn chú cá mút đá bị văng ra khỏi thùng chứa, rơi lộp độp xuống mặt đường nhựa nóng rực và bị kích động hoảng loạn tột độ.". Bố cục: Hàng ngàn chú cá mút đá văng ra khỏi thùng chứa, rơi lộp độp xuống mặt đường nhựa nóng rực.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đồng loạt hàng ngàn Cỗ Máy Tạo Đờm kích hoạt cơ chế tự vệ: chúng xả hàng tấn chất nhầy nhớt bao phủ kín mít mặt đường cao tốc và trùm lên một chiếc xe ô tô con gần đó như cảnh tượng trong phim quái vật ngoài hành tinh!". Bố cục: Hàng tấn chất nhầy nhớt bao phủ kín mít mặt đường cao tốc và trùm lên một chiếc xe ô tô con màu trắng như phim quái vật ngoài hành tinh. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đội cứu hỏa và cảnh sát giao thông bang Oregon phải điều động máy ủi đất và vòi rồng cứu hỏa công suất cực đại phun nước cật lực suốt nhiều giờ liền mới dọn dẹp sạch được bãi chiến trường nhầy nhụa trơn như đổ mỡ!". Bố cục: Máy ủi đất và lính cứu hỏa cầm vòi rồng phun nước cật lực dọn dẹp bãi chiến trường nhầy nhụa trơn như đổ mỡ trên đường cao tốc. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vụ tai nạn trở thành đề tài sốt dẻo trên toàn bộ các mặt báo quốc tế!". Bố cục: Các mặt báo quốc tế giật tít sốt dẻo về bãi đờm khổng lồ phong tỏa cao tốc Oregon. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Từ sự kiện chấn động đó, các nhà khoa học vật liệu quân sự của Hải quân Mỹ đã vào cuộc nghiên cứu sâu sợi tơ của cá mút đá.". Bố cục: Các nhà khoa học vật liệu quân sự của Hải quân Mỹ vào cuộc nghiên cứu cấu trúc phân tử sợi tơ của cá mút đá trên kính hiển vi. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kết quả cho thấy các sợi protein keratin trong chất nhầy mỏng gấp 100 lần sợi tóc người nhưng có độ bền kéo và độ dẻo dai tương đương tơ nhện và sợi ni-lông nhân tạo!". Bố cục: Phóng đại sợi tơ protein keratin mỏng gấp 100 lần sợi tóc người nhưng có độ bền kéo và độ dẻo dai tương đương tơ nhện và sợi ni-lông nhân tạo. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Người ta đang nghiên cứu dùng loại sợi sinh học này để dệt quần áo chống đạn, làm sợi chỉ khâu y tế tự tiêu và chế tạo màng dập lửa thân thiện với môi trường! Cấp độ bốn: Vượt qua xuất sắc!". Bố cục: Mô hình ứng dụng tương lai: áo giáp chống đạn dệt từ tơ cá mút đá, chỉ khâu phẫu thuật tự tiêu và bình cứu hỏa sinh học; bảng Cấp độ 4 bật PASS. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bước vào Cấp độ tối thượng: Liệu Cỗ Máy Tạo Đờm có thực sự bất tử dưới đáy đại dương? Cá mập cắn phải nhả. Cá mú đớp phải ho khạc. Bị mắc kẹt thì tự thắt nút tẩu thoát.". Bố cục: Bảng điện tử chớp sáng chữ CẤP ĐỘ TỐI THƯỢNG: TRÙM CUỐI ĐẠI DƯƠNG; ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước khoanh tay trầm ngâm suy nghĩ trước bể nuôi. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L57</summary>

```text
HÌNH L57 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chẳng lẽ quái vật này không có lấy một kẻ thù tự nhiên nào sao?". Bố cục: Mô hình đồ họa 4 chiến tích của cá mút đá đặt cạnh dấu hỏi lớn: liệu sinh vật này có khắc tinh tự nhiên nào không? KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L58</summary>

```text
HÌNH L58 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và đây là câu trả lời bất ngờ: Khắc tinh số một đánh bại được Cỗ Máy Tạo Đờm lại là những sinh vật... không hề có mang để thở! Đó là những bông hải quỳ ăn thịt khổng lồ và các loài chim biển!". Bố cục: Một bông hải quỳ ăn thịt khổng lồ dưới đáy biển và chim biển xuất hiện như những sinh vật không hề có mang thở. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L59</summary>

```text
HÌNH L59 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hải quỳ săn mồi bằng xúc tu có tế bào gai châm độc, nuốt chửng con mồi qua khoang bụng mở mà không cần hút nước qua mang, nên chất nhầy của cá mút đá hoàn toàn mất tác dụng! Đúng là vỏ quýt dày có móng tay nhọn!". Bố cục: Hải quỳ dùng các xúc tu châm nọc nuốt trọn cá mút đá qua khoang bụng mở mà không cần mang thở, chất nhầy bị vô hiệu hóa hoàn toàn. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L60</summary>

```text
HÌNH L60 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tổng kết ghi chép phòng thí nghiệm số 24: Mẫu vật đạt điểm 10 tuyệt đối cho cỗ máy phòng thủ chất nhầy kỳ dị nhất tiến hóa!". Bố cục: ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước giơ tấm bảng điểm 10 tuyệt đối trao cho chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán; cả phòng lab vỗ tay khen ngợi cỗ máy phòng thủ chất nhầy kỳ dị nhất.
```
</details>

<details><summary>L61</summary>

```text
HÌNH L61 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn các trợ lý thì sao? Nếu được sở hữu một trong hai năng lực: biến cả xô nước thành keo nhớt trong 1 giây, hay tự thắt nút cơ thể hình số tám để trốn thoát, bạn chọn cái nào? Hãy bình luận lựa chọn của bạn bên dưới nhé!". Bố cục: Hai bàn cân lựa chọn: BÊN TRÁI biểu tượng xô nước biến thành keo nhớt trong 1 giây; BÊN PHẢI biểu tượng tự thắt nút cơ thể hình số 8, các bạn nhỏ giơ thẻ bình luận. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L62</summary>

```text
HÌNH L62 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hồ sơ phòng thí nghiệm hôm nay xin tạm khép lại. Nhưng tập sau, chúng ta sẽ bước vào hồ sơ thế giới ngầm đại dương để điều tra một siêu điệp viên bí ẩn bậc nhất biển cả!". Bố cục: ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước đóng tập hồ sơ số 24 lại, ánh đèn chuyển sang ánh sáng mờ ảo của thế giới ngầm đại dương với bản đồ kho báu bí ẩn. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L63</summary>

```text
HÌNH L63 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một sinh vật sở hữu tới 9 bộ não độc lập, 3 trái tim đập nhịp nhàng, dòng máu màu xanh lam huyền bí,". Bố cục: Một sinh vật bí ẩn được vẽ hoàn toàn bằng BÓNG ĐEN ĐẶC TUYỀN (solid black silhouette) hình bạch tuộc 8 xúc tu uốn lượn, bên trong hiện đồ họa 9 bộ não nhỏ phát sáng, 3 quả tim và dòng máu xanh lam, có dấu hỏi chấm vàng to tướng phía trên; KHÔNG vẽ rõ mắt hay màu da. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L64</summary>

```text
HÌNH L64 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "và sở hữu tài hóa trang thiên bẩm: có thể biến hình mượt mà thành 15 loài sinh vật kịch độc khác nhau dưới đáy biển chỉ trong chớp mắt!". Bố cục: Chiếc BÓNG ĐEN ĐẶC TUYỀN bí ẩn có 8 xúc tu đang biến hình thành các loài sinh vật biển kịch độc như rắn biển và cá mao tiên. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>L65</summary>

```text
HÌNH L65 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đố các bạn biết bóng đen bí ẩn kỳ sau là loài vật nào? Hãy đoán ngay ở phần bình luận nhé!". Bố cục: Chiếc BÓNG ĐEN ĐẶC TUYỀN bí ẩn nằm giữa ba dấu hỏi chấm vàng cam lấp lánh mời gọi khán giả bình luận đoán tên con vật kỳ sau. KHÔNG có chú cá mút đá đeo kính bảo hộ trên trán trong cảnh này.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Chỉ cần một con cá mập vừa cắn vào thân,". Bố cục: Khung dọc: con cá mập há to hàm răng nhọn hoắt vừa đớp vào chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "loài vật này có thể biến 20 lít nước biển xung quanh thành một khối keo nhớt đặc quánh". Bố cục: Túi tuyến bùng nổ 20 lít chất nhầy đặc quánh làm cá mập nghẹt thở ho sặc sụa trong 0,4 giây.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Đây là Cá Mút Đá Hagfish, sinh vật cổ đại 300 triệu năm dài 0,5m sống dưới đáy biển sâu.". Bố cục: chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán bơi bảnh bao hình sợi dây thừng dài 0,5m dưới đáy biển sâu, bên cạnh chiếc thước đo chiều cao màu vàng.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Cơ thể nó không có xương sống, có tới 4 quả tim độc lập, và sở hữu hàng trăm lỗ xả chất nhầy hai bên sườn!". Bố cục: Đồ họa giải phẫu trong suốt của chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán: không có xương sống, 4 quả tim đỏ đang đập rộn ràng và hàng trăm lỗ xả chất nhầy hai bên sườn.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Khi bị tấn công, các sợi tơ protein dãn nở gấp 10.000 lần bít kín hoàn toàn các khe mang thở của cá mập". Bố cục: Các sợi tơ protein dãn nở gấp 10.000 lần quấn chặt bít kín mít các khe mang thở của cá mập.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "khiến kẻ đi săn ho sặc sụa phải nhả vội ra tẩu thoát!". Bố cục: Con cá mập ho sặc sụa quằn quại nhả vội cá mút đá ra ngoài và tháo chạy bạt mạng.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Để gạt sạch đờm khỏi người mình, nó tự thắt cơ thể thành nút thòng lọng hình số tám từ đầu đến đuôi như ảo thuật gia!". Bố cục: chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán tự luồn đuôi thắt nút cơ thể hình số tám từ đầu đến đuôi như chiếc cần gạt nước cạo sạch bong lớp đờm dính.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "2017, một xe tải chở 3.400kg cá mút đá lật nhào". Bố cục: Chiếc xe tải chở 3.400kg cá mút đá lật nhào trên cao tốc Oregon 2017.
```
</details>

<details><summary>S09</summary>

```text
HÌNH S09 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Một cỗ máy tạo đờm độc nhất vô nhị của đại dương!". Bố cục: Chân dung chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán uốn lượn tỏa hào quang ngầu lòi giữa đại dương, đeo kính bảo hộ phòng lab với nụ cười tự hào của kẻ bất khả chiến bại.
```
</details>

<details><summary>S10</summary>

```text
HÌNH S10 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "chỉ trong 0,4 giây làm kẻ săn mồi suýt chết ngạt!". Bố cục: Đồng hồ siêu tốc đếm 0,4 giây nhấp nháy, một khối keo nhớt đặc quánh bùng nổ bao phủ cả miệng con cá mập.
```
</details>

<details><summary>S11</summary>

```text
HÌNH S11 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Mút Đá Hagfish hồng xám trơn nhẫy, thân dài uốn lượn, kính bảo hộ tròn trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "đã biến cả đường cao tốc ở Mỹ thành một biển chất nhầy nhớt trượt ngã cả xe cứu hỏa!". Bố cục: Mặt đường cao tốc biến thành biển chất nhầy nhớt bọt trắng xóa trơn trượt làm ngã xe cộ cứu hỏa.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/65 của video YouTube về Cá Mút Đá Hagfish). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán. Nhân vật phụ cố định: ông viện trưởng phòng thí nghiệm hoạt hình tóc xù bạc, mặc áo blouse trắng, vẻ mặt thông thái hài hước; cô trợ lý phòng thí nghiệm hoạt hình mặc áo blouse xanh nhạt đeo thẻ nhân viên; chú cá mập xám hung dữ răng nhọn hoắt há to miệng ngạt thở hài hước. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/11 của video YouTube Shorts về Cá Mút Đá Hagfish). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Cá Mút Đá Hagfish (Myxini) hoạt hình màu hồng xám trơn nhẫy như sợi dây thừng dài, thân uốn lượn mềm mại, đầu tròn không có hàm răng, hai mắt tròn ngộ nghĩnh, đeo một chiếc kính bảo hộ phòng lab tròn xoe trên trán. Nhân vật phụ: chú cá mập xám hung dữ răng nhọn hoắt há to miệng ngạt thở hài hước. 
```
</details>

## 7. SEO

- **title:** Sinh Vật Biến 20 Lít Nước Thành Keo Nhớt Làm Nghẹt Thở Cá Mập?!
- **hook_paragraph:** Cá Mút Đá Hagfish cổ đại 300 triệu năm không xương sống nhưng sở hữu vũ khí kinh dị bậc nhất đại dương: biến 20 lít nước thành chất nhầy đặc quánh trong 0,4 giây bít kín mang cá mập và tự thắt nút cơ thể hình số 8 để gạt sạch đờm tẩu thoát!
- **question:** Nếu được sở hữu 1 năng lực của Cá Mút Đá Hagfish: biến 20 lít nước thành keo nhớt tức thì hay tự thắt nút cơ thể hình số 8, bạn chọn cái nào? Và đoán xem bóng đen tập sau là loài nào?
- **next_teaser:** Bóng đen siêu điệp viên đại dương: 9 bộ não, 3 quả tim, máu xanh lam và tài hóa trang thành 15 loài kịch độc!
- **shorts_title:** Biến 20 Lít Nước Thành Keo Nhớt Làm Nghẹt Thở Cá Mập?! 🐟 #độngvật #cámútđá
- **shorts_desc:** Cá Mút Đá Hagfish biến 20 lít nước thành keo nhớt đặc quánh trong 0,4 giây bít kín mang cá mập và tự thắt nút cơ thể hình số 8 để thoát thân! Giải mã Cỗ Máy Tạo Đờm cổ đại 300 triệu năm.
- **bullets:** Cấp độ 1: 150 lỗ tuyến bắn chất nhầy dãn nở 10.000 lần thể tích trong 0,4 giây · Cấp độ 2: Bít kín khe mang khiến cá mập và cá mú sặc ngạt thở phải nhả vội · Cấp độ 3: Tuyệt kỹ tự thắt nút cơ thể hình số 8 để cạo sạch đờm và tạo đòn bẩy xé mồi · Cấp độ 4: Vụ lật xe chở 3.400kg cá mút đá biến cao tốc Oregon 2017 thành biển chất nhầy · Cấp độ 5: Sợi tơ keratin siêu bền gấp nhiều lần nylon ứng dụng áo giáp chống đạn
- **tags:** cá mút đá hagfish, ca mut da hagfish, hagfish, cá mút đá, chất nhầy cá mút đá, hagfish slime, động vật kỳ lạ, thế giới động vật, động vật hài hước, vẽ chuyện hoang dã, whiteboard animation, khoa học thú vị, thử thách 5 cấp độ
- **hashtags:** #độngvật #cámútđá #VẽChuyệnHoangDã

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-24-ca-mut-da-hagfish
python src/episode/pipeline.py tts    projects/tap-24-ca-mut-da-hagfish     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-24-ca-mut-da-hagfish     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-24-ca-mut-da-hagfish     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-24-ca-mut-da-hagfish              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-24-ca-mut-da-hagfish --force
python scripts/beat_sheet.py projects/tap-24-ca-mut-da-hagfish               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-24-ca-mut-da-hagfish/audio/shorts.wav projects/tap-24-ca-mut-da-hagfish/renders/tap-24-ca-mut-da-hagfish_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-24-ca-mut-da-hagfish
python src/episode/pipeline.py seo    projects/tap-24-ca-mut-da-hagfish
python src/episode/episode_doc.py     projects/tap-24-ca-mut-da-hagfish
```
