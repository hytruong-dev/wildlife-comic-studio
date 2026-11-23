# TẬP 16 — TÔM SÚNG · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-16-tom-sung`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-16-tom-sung`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F2` · **Persona giọng:** `ky_su_vu_khi` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Tôm Súng |
| Tiêu đề YouTube | Vũ Khí 218 dB Nóng 5.000°C Làm Điếc Sonar Hải Quân Mỹ?! \| Tôm Súng \| Tập 16 |
| Video dài | `renders/tap-16-tom-sung_long.mp4` — 9:03.5 (543.5s) |
| Shorts | `renders/tap-16-tom-sung_shorts.mp4` — 0:51.2 (51.2s) |
| Thumbnail | `renders/tap-16-tom-sung_thumbnail.jpg` |
| Số hình | dài 64 beat / 64 ảnh riêng; Shorts 12 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.1**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/64 của video YouTube về Tôm Súng). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật. Nhân vật phụ cố định: chú cá bống biển Goby hoạt hình màu vàng cát sọc xanh, mắt to lồi tròn xoe tinh ranh như kính viễn vọng, vây lưng dựng đứng như cột ăng-ten rada cảnh giới; chú cá con hoạt hình màu xanh biển ngơ ngác, mắt tròn xoe quay vòng hoa mắt vì choáng váng; chiếc tàu ngầm hải quân màu xám đậm khổng lồ với tháp chỉ huy và các cảm biến vòm sonar phía trước; cô trợ lý sóc hoạt hình đeo kính cận to tròn, mặc áo blouse trắng phòng thí nghiệm, cầm bảng kẹp tài liệu. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — PHÁO THỦ TÍ HON 4CM BẮN TIA SÓNG ÂM 218 DB
*Thẻ chương:* SINH VẬT 4CM SỞ HỮU HỎA LỰC TO HƠN ĐỘNG CƠ PHẢN LỰC

*Badge:* `HỒ SƠ MẬT` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene01_p0.wav` (389 ký tự) · mood `tram_bi_an`

```text
Báo cáo thử nghiệm vũ khí tối mật cấp độ đỏ. Mở khóa toàn bộ dữ liệu lưu trữ! Toàn đội kỹ thuật hãy chuẩn bị sẵn thiết bị bảo hộ thính giác, bởi vì cỗ máy hủy diệt mà chúng ta giải mã hôm nay sẽ làm đảo lộn hoàn toàn mọi định luật vật lý mà bạn từng biết. [surprise-oh] Quên đi những hàm răng cá mập hay xúc tu bạch tuộc khổng lồ, hãy nhìn xuống một góc đá ngầm tối tăm dưới đáy đại dương!
```
**Part 1** → `audio/vs/scene01_p1.wav` (377 ký tự) · mood `hao_hung`

```text
Đối tượng mang mã định danh số mười sáu của chúng ta có ngoại hình đánh lừa thị giác cực độ: Chiều dài cơ thể chỉ vỏn vẹn từ ba đến năm xăng-ti-mét, nặng chưa đầy vài gam, trông yếu ớt chẳng khác nào một con tép riu bơi lội trong hồ cá cảnh. [laughter] Nhưng giới sinh học hải quân quốc tế lại đặt cho gã một biệt danh vô cùng đáng sợ: Pháo Thủ Tí Hon, hay còn gọi là Tôm Súng!
```
**Part 2** → `audio/vs/scene01_p2.wav` (459 ký tự) · mood `don_dap`

```text
Lý do khiến gã tí hon này được xếp vào hàng ngũ vũ khí tối thượng nằm ở chiếc càng bên phải dị dạng to bằng một nửa chiều dài cơ thể. [surprise-wa] Mỗi khi chiếc càng này đóng sập lại, nó tạo ra một xung âm thanh kinh hoàng lên tới hai trăm mười tám đề-xi-ben! Để các chuyên viên kỹ thuật dễ hình dung, tiếng động cơ máy bay phản lực cất cánh gầm rú ở mức một trăm bốn mươi đề-xi-ben, còn phát súng trường bắn sát màng nhĩ chỉ đạt một trăm sáu mươi đề-xi-ben!
```
**Part 3** → `audio/vs/scene01_p3.wav` (305 ký tự) · mood `hao_hung`

```text
Âm thanh hai trăm mười tám đề-xi-ben của một con tôm dài bốn xăng-ti-mét đủ sức xé toạc màng nhĩ con người nếu lặn quá gần, và biến nó thành một trong những sinh vật tạo ra âm thanh lớn nhất trên toàn bộ hành tinh Trái Đất, sánh ngang với những tiếng gầm xuyên đại dương của loài cá voi nhà táng khổng lồ!
```
**Part 4** → `audio/vs/scene01_p4.wav` (219 ký tự) · mood `tram_bi_an`

```text
Hôm nay chúng ta sẽ cùng tháo dỡ từng chi tiết cơ khí bên trong chiếc càng súng độc nhất vô nhị này để xem: [surprise-oh] Làm thế nào một sinh vật bé bằng ngón tay lại có thể tạo ra hỏa lực rung chuyển cả một vùng biển?
```

### scene02 — CÀNG SÚNG PIT-TÔNG VÀ GIA TỐC KHỦNG 8.000G
*Thẻ chương:* BẬT MÍ CƠ CHẾ KẸP KHÔNG BẮN ĐẠN VẬT LÝ

*Badge:* `BẢN VẼ CƠ KHÍ` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene02_p0.wav` (365 ký tự) · mood `hao_hung`

```text
Hãy trải bản vẽ kỹ thuật chi tiết của chiếc càng súng lên bàn phân tích! [surprise-oh] Đa số mọi người đều lầm tưởng Tôm Súng dùng chiếc càng khổng lồ của mình để kẹp trực tiếp vào cổ con mồi hoặc bắn ra một mảnh xương nhọn hoắt như súng phóng lao. Quên giả thuyết nghiệp dư đó đi! Cỗ máy này hoạt động theo nguyên lý cơ học chất lỏng phức tạp hơn thế gấp bội phần.
```
**Part 1** → `audio/vs/scene02_p1.wav` (363 ký tự) · mood `nghiem_trang_gia`

```text
Càng súng của Pháo Thủ Tí Hon gồm hai nửa bất đối xứng: Nửa dưới cố định có một rãnh lõm sâu chứa nước, trong khi nửa trên di động sở hữu một mấu lồi hình pit-tông đặc bằng chất sừng cứng như thép nguội. Khi chuẩn bị khai hỏa, cơ bắp bên trong càng co rút cực đại, kéo nửa trên ngửa ra sau một góc chín mươi độ và khóa chặt vào một cái chốt hãm sinh học tự nhiên!
```
**Part 2** → `audio/vs/scene02_p2.wav` (444 ký tự) · mood `don_dap`

```text
Thời điểm chốt hãm mở bung, toàn bộ năng lượng đàn hồi tích lũy được giải phóng trong chưa đầy nửa mili-giây! Mấu lồi pit-tông lao thẳng vào rãnh nước với vận tốc lên tới một trăm cây số một giờ, tương đương hai mươi tám mét một giây. [surprise-wa] Cú đóng sập thần tốc này tạo ra mức gia tốc kỷ lục lên tới tám ngàn gờ! Hãy nhớ rằng phi công lái máy bay chiến đấu tối tân chỉ cần chịu gia tốc chín gờ là mạch máu đã dồn xuống chân và ngất lịm!
```
**Part 3** → `audio/vs/scene02_p3.wav` (94 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Ủa các anh kỹ sư ơi, em bơi cách nó tận hai gang tay mà sao sóng đánh gãy cả vây lưng thế này?
```
**Part 4** → `audio/vs/scene02_p4.wav` (464 ký tự) · mood `hao_hung`

```text
[laughter] Đúng như chú cá con ngơ ngác vừa than vãn! Khi mấu lồi pit-tông dập cực mạnh vào rãnh hẹp, nó ép toàn bộ lượng nước bên trong phụt ra ngoài thành một tia nước phản lực siêu tốc. Cơ chế ngòi nổ đàn hồi này bền bỉ đến mức Tôm Súng có thể búng liên tục hàng ngàn lần mà càng không hề bị nứt mỏi hay thoái hóa khớp sụn! Nhưng điều điên rồ nhất vẫn chưa dừng lại ở đó, bởi vì chính tia nước phản lực này mới là ngòi nổ kích hoạt quả bom năng lượng tiếp theo!
```

### scene03 — BỌT KHÍ 5.000°C NÓNG NGANG BỀ MẶT MẶT TRỜI
*Thẻ chương:* BỌT KHÍ VỠ NẮNG TƯƠNG ĐƯƠNG BỀ MẶT MẶT TRỜI

*Badge:* `HỎA LỰC SIÊU NHIỆT` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene03_p0.wav` (465 ký tự) · mood `tram_bi_an`

```text
Bây giờ, chúng ta bước vào giai đoạn nguy hiểm nhất của cuộc thử nghiệm vũ khí: Hiện tượng vật lý mang tên bong bóng Ca-vi-tây-sơn! [surprise-oh] Khi tia nước từ càng Tôm Súng bắn ra với vận tốc một trăm cây số một giờ, áp suất cục bộ xung quanh dòng chảy tụt dốc không phanh xuống dưới cả áp suất bốc hơi của nước biển. Hiện tượng tụt áp cực hạn này khiến nước bốc hơi tức thì ở nhiệt độ thường, tạo ra một bọt khí chân không li ti có đường kính chỉ vài mi-li-mét!
```
**Part 1** → `audio/vs/scene03_p1.wav` (282 ký tự) · mood `don_dap`

```text
Bọt khí này lao vút đi với tốc độ xé toạc dòng nước. Nhưng khi nó vừa bay được khoảng vài xăng-ti-mét, áp suất khổng lồ của khối nước đại dương xung quanh lập tức ép chặt và nghiền nát bọt khí chân không này! Bọt khí sụp đổ và nổ tung trong thời gian chỉ tính bằng một phần tỷ giây!
```
**Part 2** → `audio/vs/scene03_p2.wav` (130 ký tự) · 🎭 cameo `co_tro_ly`

```text
Báo cáo kỹ sư trưởng, cảm biến quang phổ ghi nhận nhiệt độ lõi bọt khí vừa chạm mốc năm ngàn độ C, chíp đo quang đã nổ tung rồi ạ!
```
**Part 3** → `audio/vs/scene03_p3.wav` (348 ký tự) · mood `don_dap`

```text
[surprise-wa] Các chuyên viên kỹ thuật không hề nghe nhầm đâu! Theo công bố chính thức trên tạp chí khoa học danh tiếng Science, sự sụp đổ đột ngột của bọt khí Ca-vi-tây-sơn nén ép các phân tử khí đến mức sinh nhiệt từ bốn ngàn bảy trăm độ C đến năm ngàn độ C! Nhiệt độ này xấp xỉ với nhiệt độ năm ngàn năm trăm độ C trên bề mặt của chính Mặt Trời!
```
**Part 4** → `audio/vs/scene03_p4.wav` (586 ký tự) · mood `hao_hung`

```text
Kèm theo nhiệt độ bề mặt Mặt Trời là một chớp sáng xanh lơ lóe lên trong tích tắc, hiện tượng mà giới vật lý gọi là Sô-nô-lu-mi-nét-xơn, tức là ánh sáng sinh ra từ sóng âm thanh! Sóng xung kích tỏa ra từ vụ nổ bọt khí đủ sức làm choáng váng hoặc tiêu diệt gọn gàng một con cá nhỏ hay làm vỡ nát mai cua cứng cách xa hai xăng-ti-mét mà ngòi nổ Tôm Súng thậm chí chưa từng chạm vào người con mồi! Đó là lý do vì sao các bảo tàng thủy cung không bao giờ dám nuôi Tôm Súng trong các bể kính thông thường, vì cú nổ bọt khí ở cự ly gần có thể tạo ra vi chấn làm rạn nứt cả kính cường lực dày!
```

### scene04 — ĐÀN TÔM RANG BẮP LÀM ĐIẾC RADAR TÀU NGẦM THẾ CHIẾN II
*Thẻ chương:* HẢI QUÂN MỸ ĐIÊN ĐẦU VÌ TIẾNG BỎNG NGÔ ĐÁY BIỂN

*Badge:* `HỒ SƠ TÁC CHIẾN` · *mood mặc định:* `nghiem_trang_gia`

**Part 0** → `audio/vs/scene04_p0.wav` (388 ký tự) · mood `tram_bi_an`

```text
Lật mở hồ sơ tác chiến lịch sử năm một ngàn chín trăm bốn mươi hai giữa đỉnh điểm Thế chiến thứ hai tại mặt trận Thái Bình Dương! [surprise-oh] Hải quân Hoa Kỳ bắt đầu trang bị hệ thống định vị thủy âm Xô-na tối tân nhất thời bấy giờ cho toàn bộ hạm đội tàu ngầm và tàu khu trục. Mục tiêu tác chiến là lắng nghe âm thanh động cơ chân vịt của tàu ngầm đối phương ẩn nấp dưới lòng biển sâu.
```
**Part 1** → `audio/vs/scene04_p1.wav` (190 ký tự) · 🎭 cameo `phat_thanh_vien`

```text
Bản tin đặc biệt từ trạm tác chiến Thái Bình Dương: Toàn bộ hệ thống cảm biến âm thanh đang bị gây nhiễu trắng! Đáy biển phát ra tiếng nổ liên thanh như hàng vạn máy súng đang bắn đồng loạt!
```
**Part 2** → `audio/vs/scene04_p2.wav` (317 ký tự) · mood `hao_hung`

```text
[laughter] Thủy thủ đoàn hoang mang cực độ! Thay vì nghe thấy tiếng ù ù trầm đục của tàu ngầm phe địch, trên tai nghe của các nhân viên Xô-na liên tục dội về những âm thanh lách tách đinh tai nhức óc, nghe chẳng khác nào ai đó đang đổ hàng triệu gói bắp ngô vào lò vi sóng khổng lồ rồi rang nổ liên tục dưới đáy biển!
```
**Part 3** → `audio/vs/scene04_p3.wav` (495 ký tự) · mood `hao_hung`

```text
Bộ chỉ huy quân sự Mỹ lập tức đặt diện tình nghi vào một loại vũ khí gây nhiễu sóng âm bí mật của phe đối phương. Họ phải khẩn cấp mời các nhà sinh vật học và chuyên gia âm thanh từ Đại học U-C-L-A đến khảo sát thực địa. [surprise-wa] Và kết quả điều tra khiến các tướng lĩnh quân sự phải ôm đầu cười trừ: Thủ phạm phá hoại hệ thống radar trị giá hàng triệu đô la không phải vũ khí tối mật nào, mà chính là hàng triệu con Pháo Thủ Tí Hon Tôm Súng đang đua nhau búng càng săn mồi dưới rạn san hô!
```
**Part 4** → `audio/vs/scene04_p4.wav` (345 ký tự) · mood `hao_hung`

```text
Về sau, chính các thuyền trưởng tàu ngầm Mỹ đã tận dụng sự cố này như một chiến thuật ngụy trang tài tình: Họ thường xuyên chủ động lái tàu ngầm ẩn nấp sâu vào các rạn san hô nơi bầy Tôm Súng đang nổ đại bác liên thanh, để âm thanh hai trăm mười tám đề-xi-ben của chúng che giấu hoàn toàn tiếng động cơ tàu ngầm trước sự lùng sục của đối phương!
```

### scene05 — LÍNH GÁC CÁ BỐNG VÀ TỬ HUYỆT RỤNG CÀNG
*Thẻ chương:* MÙ DỞ ĐÀO HẦM THUÊ VỆ SĨ CÁ BỐNG BẢO VỆ

*Badge:* `HỢP TÁC TÁC CHIẾN` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene05_p0.wav` (382 ký tự) · mood `tram_bi_an`

```text
Một vũ khí hỏa lực hạng nặng dù uy lực đến đâu cũng luôn tồn tại những lỗ hổng kỹ thuật chết người. Và tử huyệt số một của Pháo Thủ Tí Hon chính là: [surprise-oh] Gã gần như mù tịt! Lớp vỏ giáp trên đầu phát triển quá đà đã che khuất gần như toàn bộ nhãn cầu, khiến thị lực của Tôm Súng vô cùng mờ mạt, chỉ phân biệt được sáng tối mà không nhìn rõ hình thù kẻ thù đang tiến lại gần.
```
**Part 1** → `audio/vs/scene05_p1.wav` (354 ký tự) · mood `hao_hung`

```text
Để khắc phục lỗi thiết kế tai hại này, Tôm Súng đã ký một hợp đồng liên minh quân sự đỉnh cao với loài Cá Bống biển! Cá Bống có đôi mắt lồi to tròn cực kỳ tinh tường, đảm nhận vị trí trinh sát canh gác cửa hang hai mươi tư trên bảy. Trong khi đó, Tôm Súng dùng chiếc râu dài của mình liên tục chạm nhẹ vào vây đuôi của Cá Bống để nhận tín hiệu rung động.
```
**Part 2** → `audio/vs/scene05_p2.wav` (325 ký tự) · mood `hao_hung`

```text
Mỗi khi phát hiện bóng dáng kẻ săn mồi nguy hiểm, Cá Bống chỉ cần quẫy nhẹ đuôi báo động: [surprise-wa] Tôm Súng lập tức lùi tọt vào hang sâu an toàn, đổi lại Cá Bống được quyền dọn vào ở ké miễn phí trong căn hầm kiên cố do chính Tôm Súng cặm cụi đào bới suốt ngày đêm! Một hợp đồng đôi bên cùng có lợi mẫu mực của tự nhiên.
```
**Part 3** → `audio/vs/scene05_p3.wav` (101 ký tự) · 🎭 cameo `ga_khong_lo`

```text
Báo cáo thử nghiệm độ bền: Nếu khẩu đại bác bên phải bị gãy rụng thì cỗ máy này có tự hủy luôn không?
```
**Part 4** → `audio/vs/scene05_p4.wav` (603 ký tự) · mood `bi_hai`

```text
[laughter] Đây chính là cơ chế đảo chiều kỳ diệu nhất của tạo hóa! Nếu trong giao chiến chiếc càng súng khổng lồ bị đứt rời, chiếc càng gắp nhỏ xíu bên trái sẽ lập tức nhận lệnh sinh học: Nó bắt đầu phình to dần và biến đổi thành một khẩu đại bác mới toanh sau vài lần lột xác! Còn tại vị trí chiếc càng cũ bị gãy, một chiếc càng gắp nhỏ sẽ mọc lại thay thế. Tuy nhiên, mỗi khi lột xác thì toàn bộ cơ thể mềm oặt như cọng bún, đại bác mất hoàn toàn tác dụng. Trong những ngày hiểm nghèo đó, gã pháo thủ lừng danh đành ngoan ngoãn nép mình sau lưng chú cá bống canh cửa, chờ lớp vỏ giáp cứng cáp trở lại!
```

### scene06 — BÀI HỌC KÍCH THƯỚC VÀ BÓNG ĐEN 860V TẬP SAU
*Thẻ chương:* BÀI HỌC VŨ KHÍ TỐI THƯỢNG VÀ THỬ THÁCH 860 VÔN

*Badge:* `BÁO CÁO KỸ THUẬT` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene06_p0.wav` (355 ký tự) · mood `am_ap`

```text
Báo cáo tổng kết thử nghiệm kỹ thuật số mười sáu: Sinh vật bé nhỏ Tôm Súng để lại cho giới khoa học một bài học công nghệ vô cùng sâu sắc. Kích thước cơ thể chưa bao giờ là thước đo duy nhất cho sức mạnh sinh tồn. Đôi khi những hỏa lực khủng khiếp và tinh vi nhất của tự nhiên lại được ẩn giấu bên trong một thân xác tí hon khiêm nhường dưới đáy biển sâu.
```
**Part 1** → `audio/vs/scene06_p1.wav` (254 ký tự) · mood `hao_hung`

```text
Chính cơ chế nén bọt khí Ca-vi-tây-sơn và hiện tượng phát quang âm thanh của Pháo Thủ Tí Hon đã và đang mở ra cho các kỹ sư hiện đại vô số ứng dụng đột phá trong công nghệ làm sạch sóng siêu âm, y học tán sỏi thận và động cơ phản lực chất lỏng tương lai!
```
**Part 2** → `audio/vs/scene06_p2.wav` (241 ký tự) · mood `hao_hung`

```text
[surprise-oh] Bạn ấn tượng nhất với điều gì ở Pháo Thủ Tí Hon Tôm Súng: Cú nổ hai trăm mười tám đề-xi-ben làm điếc tai hải quân, hay bọt khí nóng năm ngàn độ C ngang bề mặt Mặt Trời? Hãy để lại ý kiến bình luận của đội kỹ thuật bên dưới nhé!
```
**Part 3** → `audio/vs/scene06_p3.wav` (817 ký tự) · mood `tram_bi_an`

```text
Và bây giờ, hãy hướng ngòi bút về phân cảnh kết thúc bí ẩn! Trong tập tiếp theo, chúng ta sẽ rời xa đáy biển mặn để tiến vào vùng nước ngọt đục ngầu của lưu vực rừng rậm Amazon. [surprise-wa] Hãy chiêm ngưỡng một bóng đen bí ẩn uốn lượn dài tới hai mét! Một sinh vật trơn trượt không hề có răng nanh nhọn hoắt hay nọc độc chết người, nhưng bên trong cơ thể lại chứa tới sáu ngàn tế bào pin sinh học nối tiếp nhau, sẵn sàng phóng ra luồng xung điện kinh hoàng lên tới tám trăm sáu mươi Vôn! Cú giật điện đủ sức đánh ngất lịm cả cá sấu khổng lồ và ngựa trưởng thành ngay dưới dòng nước! Nhưng điều kỳ lạ nhất là tại sao chính bản thân sinh vật này lại không hề bị điện giật? Đố các chuyên viên kỹ thuật biết danh tính của cỗ máy phát điện sống bí ẩn này là ai? Hãy viết ngay câu trả lời của bạn dưới phần bình luận nhé!
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Cảnh báo thử nghiệm vũ khí! Bạn có tin một sinh vật bé nhỏ dài chưa đầy bốn xăng-ti-mét lại sở hữu hỏa lực nổ to hơn cả động cơ máy bay phản lực? Đây là Tôm Súng, hay còn gọi là Pháo Thủ Tí Hon của các rạn san hô nhiệt đới! Thứ nhất, chiếc càng súng khổng lồ của nó có thể kẹp lại với gia tốc kinh hoàng tám ngàn gờ, tạo ra âm thanh lên tới hai trăm mười tám đề-xi-ben làm rung chuyển đáy biển! Thứ hai, cú kẹp phụt ra tia nước phản lực xé toạc áp suất, sinh ra bọt khí phát nổ ở nhiệt độ gần năm ngàn độ C, nóng ngang bề mặt Mặt Trời và phát ra chớp sáng lóe mắt! Thứ ba, vào Thế chiến thứ hai, hàng triệu con tôm súng đã đồng thanh nổ càng làm điếc đặc toàn bộ hệ thống định vị thủy âm Sonar của Hải quân Hoa Kỳ! Dù sở hữu đại bác hủy diệt nhưng mắt nó lại gần như mù tịt, phải thuê vệ sĩ cá bống canh cửa để đổi lấy chỗ ở an toàn! Đừng bao giờ đánh giá thấp những kẻ tí hon, bởi hỏa lực khủng khiếp nhất đôi khi lại nằm trong bàn tay nhỏ bé nhất!
```

**Whisper prompt:** `Tôm Súng, Pháo Thủ Tí Hon, Alpheidae, 218 dB, 140 dB, 160 dB, 8.000g, 100 km/h, 28 m/s, 5.000°C, 4.700°C, 5.500°C, Cavitation, Sonoluminescence, Sonar, UCLA, Thái Bình Dương, Thế chiến II, Cá Bống, 860V, Lươn Điện`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| hai trăm mười tám đề-xi-ben | 218 dB |
| Hai trăm mười tám đề-xi-ben | 218 dB |
| một trăm bốn mươi đề-xi-ben | 140 dB |
| Một trăm bốn mươi đề-xi-ben | 140 dB |
| một trăm sáu mươi đề-xi-ben | 160 dB |
| Một trăm sáu mươi đề-xi-ben | 160 dB |
| năm ngàn độ C | 5.000°C |
| Năm ngàn độ C | 5.000°C |
| bốn ngàn bảy trăm độ C | 4.700°C |
| Bốn ngàn bảy trăm độ C | 4.700°C |
| năm ngàn năm trăm độ C | 5.500°C |
| Năm ngàn năm trăm độ C | 5.500°C |
| hàng ngàn độ C | hàng ngàn độ C |
| Hàng ngàn độ C | hàng ngàn độ C |
| tám ngàn gờ | 8.000g |
| Tám ngàn gờ | 8.000g |
| chín gờ | 9g |
| Chín gờ | 9g |
| một trăm cây số một giờ | 100 km/h |
| Một trăm cây số một giờ | 100 km/h |
| hai mươi tám mét một giây | 28 m/s |
| Hai mươi tám mét một giây | 28 m/s |
| ba đến năm xăng-ti-mét | 3-5cm |
| Ba đến năm xăng-ti-mét | 3-5cm |
| bốn xăng-ti-mét | 4cm |
| Bốn xăng-ti-mét | 4cm |
| năm xăng-ti-mét | 5cm |
| Năm xăng-ti-mét | 5cm |
| ba xăng-ti-mét | 3cm |
| Ba xăng-ti-mét | 3cm |
| hai xăng-ti-mét | 2cm |
| vài mi-li-mét | vài mm |
| hai mi-li-mét | 2mm |
| một mili-giây | 1 mili-giây |
| Một mili-giây | 1 mili-giây |
| nửa mili-giây | 0,5 mili-giây |
| năm phút | 5 phút |
| hai mét | 2m |
| Hai mét | 2m |
| năm một ngàn chín trăm bốn mươi hai | năm 1942 |
| Năm một ngàn chín trăm bốn mươi hai | Năm 1942 |
| Thế chiến thứ hai | Thế chiến II |
| Thế chiến hai | Thế chiến II |
| sáu ngàn | 6.000 |
| Sáu ngàn | 6.000 |
| tám trăm sáu mươi Vôn | 860V |
| Tám trăm sáu mươi Vôn | 860V |
| hai mươi tư trên bảy | 24/7 |
| Tập mười sáu | Tập 16 |
| Tập mười bảy | Tập 17 |
| Tập mười lăm | Tập 15 |
| số mười sáu | số 16 |
| Số mười sáu | Số 16 |
| mười sáu | 16 |
| Mười sáu | 16 |
| Ca-vi-tây-sơn | Cavitation |
| Sô-nô-lu-mi-nét-xơn | Sonoluminescence |
| Xô-na | Sonar |
| U-C-L-A | UCLA |
| Al-phe-i-đe | Alpheidae |
| hai mươi | 20 |
| ba mươi | 30 |
| bốn mươi | 40 |
| năm mươi | 50 |
| sáu mươi | 60 |
| bảy mươi | 70 |
| tám mươi | 80 |
| chín mươi | 90 |
| một trăm | 100 |
| gấp đôi | gấp đôi |
| gấp ba | gấp ba |
| gấp mười | gấp 10 |
| hàng triệu năm | hàng triệu năm |
| hàng triệu | hàng triệu |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · PHÁO THỦ TÍ HON 4CM BẮN TIA SÓNG ÂM 218 DB · 86.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:04.7 (4.7s) | L01 | Báo cáo thử nghiệm vũ khí tối mật cấp độ đỏ. Mở khóa toàn bộ dữ liệu lưu trữ! |  | Phòng nghiên cứu vũ khí hải quân tối mật: một tập hồ sơ mật màu đỏ thẫm đóng dấu 'MẬT CẤP ĐỘ ĐỎ' nằm giữa bàn kim loại công nghệ cao, xung quanh là màn hình radar và thiết bị đo sóng âm. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này. |
| b02 | 00:04.7–00:13.3 (8.5s) | L02 | Toàn đội kỹ thuật hãy chuẩn bị sẵn thiết bị bảo hộ thính giác, bởi vì cỗ máy hủy diệt mà chúng ta giải mã hôm nay sẽ làm đảo lộn hoàn toàn mọi định luật vật lý mà bạn từng biết. |  | Biển báo hoạt hình màu vàng vẽ chiếc tai nghe chống ồn công nghiệp ngộ nghĩnh, xung quanh là các vạch sóng âm thanh biểu đồ nhảy múa sinh động. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này. |
| b03 | 00:13.3–00:18.9 (5.6s) | L03 | Quên đi những hàm răng cá mập hay xúc tu bạch tuộc khổng lồ, hãy nhìn xuống một góc đá ngầm tối tăm dưới đáy đại dương! |  | Đáy biển sâu huyền bí: BÊN TRÁI hàm răng cá mập khổng lồ và xúc tu bạch tuộc mờ ảo; BÊN PHẢI một khe đá ngầm san hô tối tăm phát ra ánh sáng bí ẩn. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này. |
| b04 | 00:18.9–00:23.4 (4.5s) | L04 | Đối tượng mang mã định danh số 16 của chúng ta có ngoại hình đánh lừa thị giác cực độ: | **MÃ SỐ 16** · đối tượng thử nghiệm · L/380 · [0.3, 0.55] | Chân dung phóng to hài hước: chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật đứng giữa khung hình, thân hình bé xíu nằm lọt thỏm trên thước đo milimet, mũ bảo hộ vàng lệch một bên, tay chống nạnh vẻ mặt tự tin ngầu lòi. |
| b05 | 00:23.4–00:31.3 (8.0s) | L05 | Chiều dài cơ thể chỉ vỏn vẹn từ 3-5cm, nặng chưa đầy vài gam, trông yếu ớt chẳng khác nào một con tép riu bơi lội trong hồ cá cảnh. | **3-5cm** · chiều dài cơ thể · R/380 · [0.75, 0.55] | So sánh kích thước trực quan: BÊN TRÁI chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật đứng cạnh một ngón tay người khổng lồ, thước dây chỉ đúng vạch 4cm; bên cạnh là chiếc cân tiểu ly đo trọng lượng vài gam. |
| b06 | 00:31.3–00:38.5 (7.2s) | L06 | Nhưng giới sinh học hải quân quốc tế lại đặt cho gã một biệt danh vô cùng đáng sợ: Pháo Thủ Tí Hon, hay còn gọi là Tôm Súng! |  | Tấm huy hiệu quân sự danh dự: chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật đứng hiên ngang trên bục vàng mang dòng chữ danh xưng 'PHÁO THỦ TÍ HON', chiếc càng súng giơ cao vác lên vai như khẩu pháo đại bác. |
| b07 | 00:38.5–00:45.8 (7.3s) | L07 | Lý do khiến gã tí hon này được xếp vào hàng ngũ vũ khí tối thượng nằm ở chiếc càng bên phải dị dạng to bằng một nửa chiều dài cơ thể. |  | Đặc tả chiếc càng súng khổng lồ bên phải của chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật: chiếc càng to bằng nửa cơ thể, lớp vỏ cam đỏ dày cộp có các khớp bản lề cơ khí và chốt hãm chắc chắn, bóng loáng. |
| b08 | 00:45.8–00:50.9 (5.0s) | L08 | Mỗi khi chiếc càng này đóng sập lại, nó tạo ra một xung âm thanh kinh hoàng lên tới 218 dB! | **218 dB** · âm thanh cực hạn · R/380 · [0.75, 0.55] | Khoảnh khắc khai hỏa chấn động: chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật đóng sập chiếc càng súng, sóng âm thanh hình vòng tròn đồng tâm màu xanh lơ bùng nổ dữ dội, làm nứt toác đá ngầm xung quanh. |
| b09 | 00:50.9–00:56.3 (5.4s) | L09 | Để các chuyên viên kỹ thuật dễ hình dung, tiếng động cơ máy bay phản lực cất cánh gầm rú ở mức 140 dB, | **140 dB** · phản lực cất cánh · L/380 · [0.25, 0.55] | So sánh âm lượng: BÊN TRÁI chiếc máy bay phản lực cất cánh gầm rú với đồng hồ đo chỉ 140 dB; bên cạnh là chiếc đồng hồ công nghiệp đo tiếng ồn. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này. |
| b10 | 00:56.3–00:59.9 (3.6s) | L10 | còn phát súng trường bắn sát màng nhĩ chỉ đạt 160 dB! | **160 dB** · tiếng súng trường · R/380 · [0.75, 0.55] | Đồ thị cột âm lượng: cột âm thanh của súng trường bắn sát tai chỉ đạt 160 dB; BÊN PHẢI cột âm thanh của chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật vọt cao tít lên mức 218 dB vượt ngưỡng chịu đựng. |
| b11 | 00:59.9–01:06.8 (6.9s) | L11 | Âm thanh 218 dB của một con tôm dài 4cm đủ sức xé toạc màng nhĩ con người nếu lặn quá gần, |  | Hình ảnh minh họa thợ lặn người: một người thợ lặn ôm hai tai bịt chặt vì sóng âm đinh tai nhức óc dưới nước; BÊN PHẢI chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật búng càng tự tin mỉm cười. |
| b12 | 01:06.8–01:16.1 (9.3s) | L12 | và biến nó thành một trong những sinh vật tạo ra âm thanh lớn nhất trên toàn bộ hành tinh Trái Đất, sánh ngang với những tiếng gầm xuyên đại dương của loài cá voi nhà táng khổng lồ! |  | So sánh đại dương: BÊN TRÁI chú cá voi nhà táng khổng lồ dài 18m đang phát tiếng gầm; BÊN PHẢI chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật bé tí 4cm nhưng cột sóng âm ngang ngửa nhau đầy kinh ngạc. |
| b13 | 01:16.1–01:21.9 (5.8s) | L13 | Hôm nay chúng ta sẽ cùng tháo dỡ từng chi tiết cơ khí bên trong chiếc càng súng độc nhất vô nhị này để xem: |  | Phòng mổ xẻ cơ khí: chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật đứng cạnh bản vẽ cấu tạo cơ khí khổng lồ, cầm cờ-lê mỏ lết chỉ vào các bộ phận pit-tông của chiếc càng súng. |
| b14 | 01:21.9–01:26.7 (4.8s) | L14 | Làm thế nào một sinh vật bé bằng ngón tay lại có thể tạo ra hỏa lực rung chuyển cả một vùng biển? |  | Cận cảnh bàn tay họa sĩ vẽ nên chiếc càng súng phóng tia năng lượng rực sáng dưới đáy biển; biểu tượng dấu hỏi chấm lớn màu vàng phát sáng tò mò. |

### scene02 · CÀNG SÚNG PIT-TÔNG VÀ GIA TỐC KHỦNG 8.000G · 86.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:12.8 (12.8s) | L15 | Hãy trải bản vẽ kỹ thuật chi tiết của chiếc càng súng lên bàn phân tích! Đa số mọi người đều lầm tưởng Tôm Súng dùng chiếc càng khổng lồ của mình để kẹp trực tiếp vào cổ con mồi hoặc bắn ra một mảnh xương nhọn hoắt như súng phóng lao. |  | Bản vẽ thiết kế Blueprint màu xanh dương: hình vẽ giải phẫu chiếc càng súng với các đường kích thước cơ khí, góc đo đạc và mũi tên chỉ dẫn chi tiết. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này. |
| b02 | 00:12.8–00:19.4 (6.6s) | L16 | Quên giả thuyết nghiệp dư đó đi! Cỗ máy này hoạt động theo nguyên lý cơ học chất lỏng phức tạp hơn thế gấp bội phần. |  | Hình ảnh minh họa hiểu lầm: BÊN TRÁI hình tôm kẹp cổ cua bị gạch chéo đỏ lớn; BÊN PHẢI là mô hình dòng chảy thủy động lực học với các xoáy nước phản lực công nghệ cao. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này. |
| b03 | 00:19.4–00:28.7 (9.3s) | L17 | Càng súng của Pháo Thủ Tí Hon gồm hai nửa bất đối xứng: Nửa dưới cố định có một rãnh lõm sâu chứa nước, trong khi nửa trên di động sở hữu một mấu lồi hình pit-tông đặc bằng chất sừng cứng như thép nguội. |  | Mổ xẻ 2 nửa càng súng: Nửa dưới cố định có rãnh lõm chứa đầy nước; nửa trên di động có mấu lồi pit-tông hình chóp đặc cứng như thép nguội, viền sáng nổi bật. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này. |
| b04 | 00:28.7–00:36.2 (7.5s) | L18 | Khi chuẩn bị khai hỏa, cơ bắp bên trong càng co rút cực đại, kéo nửa trên ngửa ra sau một góc 90 độ và khóa chặt vào một cái chốt hãm sinh học tự nhiên! |  | chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật gồng mình chuẩn bị bắn: cơ bắp cuồn cuộn, kéo nửa càng trên ngửa ra sau đúng 90 độ, cơ chế lò xo sinh học khóa chặt vào ngàm chốt hãm kêu 'tách'. |
| b05 | 00:36.2–00:41.4 (5.2s) | L19 | Thời điểm chốt hãm mở bung, toàn bộ năng lượng đàn hồi tích lũy được giải phóng trong chưa đầy 0,5 mili-giây! | **0,5 ms** · thời gian bung chốt · L/380 · [0.3, 0.55] | Đồng hồ bấm giờ siêu tốc: kim đồng hồ chỉ vạch thời gian cực ngắn dưới 0,5 mili-giây; chốt hãm bung ra giải phóng năng lượng đàn hồi khổng lồ. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này. |
| b06 | 00:41.4–00:47.5 (6.1s) | L20 | Mấu lồi pit-tông lao thẳng vào rãnh nước với vận tốc lên tới 100 km/h, tương đương 28 m/s. | **100 km/h** · tốc độ sập càng · L/380 · [0.25, 0.55]<br>**28 m/s** · vận tốc cực đại · R/480 · [0.75, 0.55] | Cận cảnh cú sập pit-tông: mấu lồi lao thẳng xuống rãnh nước với vệt tốc độ xé gió, đồng hồ tốc độ chỉ 100 km/h (28 m/s), bọt nước văng tung tóe. |
| b07 | 00:47.5–00:56.9 (9.4s) | L21 | Cú đóng sập thần tốc này tạo ra mức gia tốc kỷ lục lên tới 8.000g! Hãy nhớ rằng phi công lái máy bay chiến đấu tối tân chỉ cần chịu gia tốc 9g là mạch máu đã dồn xuống chân và ngất lịm! | **8.000g** · gia tốc kỷ lục · L/380 · [0.3, 0.55] | Đồng hồ đo gia tốc: kim đồng hồ vọt lên mức đỏ rực 8.000g; BÊN PHẢI hình một phi công vũ trụ ngồi trong buồng lái đang choáng váng vì 9g. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này. |
| b08 | 00:56.9–01:03.3 (6.4s) | L22 | Ủa các anh kỹ sư ơi, em bơi cách nó tận hai gang tay mà sao sóng đánh gãy cả vây lưng thế này? |  | Chú cá con hoạt hình màu xanh biển ngơ ngác, mắt tròn xoe quay vòng hoa mắt vì choáng váng bơi cách đó 2 gang tay, vây lưng run rẩy vì luồng sóng áp lực thổi tạt ngang người. |
| b09 | 01:03.3–01:12.7 (9.4s) | L23 | Đúng như chú cá con ngơ ngác vừa than vãn! Khi mấu lồi pit-tông dập cực mạnh vào rãnh hẹp, nó ép toàn bộ lượng nước bên trong phụt ra ngoài thành một tia nước phản lực siêu tốc. |  | Tia nước phản lực cực mạnh: mấu lồi pit-tông nén chặt đáy rãnh, tống ra một tia nước hình mũi tên áp lực cao bắn thẳng về phía trước như súng phun nước cứu hỏa siêu vi mô. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này. |
| b10 | 01:12.7–01:19.7 (7.0s) | L24 | Cơ chế ngòi nổ đàn hồi này bền bỉ đến mức Tôm Súng có thể búng liên tục hàng ngàn lần mà càng không hề bị nứt mỏi hay thoái hóa khớp sụn! |  | chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật đứng bắn liên thanh tưng bừng: càng súng búng liên hồi hàng ngàn phát 'bụp bụp', vỏ càng vẫn nguyên vẹn sáng bóng không hề có một vết nứt mỏi nào. |
| b11 | 01:19.7–01:26.7 (7.0s) | L25 | Nhưng điều điên rồ nhất vẫn chưa dừng lại ở đó, bởi vì chính tia nước phản lực này mới là ngòi nổ kích hoạt quả bom năng lượng tiếp theo! |  | Biểu tượng quả bom hẹn giờ năng lượng: tia nước phản lực phát sáng dẫn đường cho một quả bom bọt khí đang bắt đầu hình thành ở đầu ngọn nước. |

### scene03 · BỌT KHÍ 5.000°C NÓNG NGANG BỀ MẶT MẶT TRỜI · 89.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:06.9 (6.9s) | L26 | Bây giờ, chúng ta bước vào giai đoạn nguy hiểm nhất của cuộc thử nghiệm vũ khí: Hiện tượng vật lý mang tên bong bóng Cavitation! |  | Sơ đồ hiện tượng Cavitation: dòng nước vận tốc 100 km/h làm áp suất tụt dốc đứng thành vùng chân không, sinh ra một bọt khí li ti trong suốt phát sáng nhẹ. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này. |
| b02 | 00:06.9–00:15.2 (8.3s) | L27 | Khi tia nước từ càng Tôm Súng bắn ra với vận tốc 100 km/h, áp suất cục bộ xung quanh dòng chảy tụt dốc không phanh xuống dưới cả áp suất bốc hơi của nước biển. |  | Đồ thị tụt áp suất: đường cong áp suất cắm thẳng xuống dưới vạch bốc hơi nước biển; bọt khí chân không phình to đến đường kính vài milimet. |
| b03 | 00:15.2–00:22.7 (7.5s) | L28 | Hiện tượng tụt áp cực hạn này khiến nước bốc hơi tức thì ở nhiệt độ thường, tạo ra một bọt khí chân không li ti có đường kính chỉ vài mm! |  | Cận cảnh bọt khí chân không Cavitation lơ lửng trong nước biển, màng bọt khí lung linh phản chiếu ánh sáng kỳ ảo, lao vút đi xé dòng nước. |
| b04 | 00:22.7–00:32.5 (9.8s) | L29 | Bọt khí này lao vút đi với tốc độ xé toạc dòng nước. Nhưng khi nó vừa bay được khoảng vài xăng-ti-mét, áp suất khổng lồ của khối nước đại dương xung quanh lập tức ép chặt và nghiền nát bọt khí chân không này! |  | Áp lực nước biển khổng lồ từ 4 phương 8 hướng dồn ép vào bọt khí: các mũi tên màu xanh sẫm đè nén khiến bọt khí méo mó và co cụm cực mạnh. |
| b05 | 00:32.5–00:36.1 (3.5s) | L30 | Bọt khí sụp đổ và nổ tung trong thời gian chỉ tính bằng một phần tỷ giây! |  | Khoảnh khắc nổ sụp sụp đổ (implosion): bọt khí co nhỏ lại mức nanomet rồi nổ tung thành một quả cầu lửa nhiệt lượng phát sáng chói lòa trong nước. |
| b06 | 00:36.1–00:43.3 (7.2s) | L31 | Báo cáo kỹ sư trưởng, cảm biến quang phổ ghi nhận nhiệt độ lõi bọt khí vừa chạm mốc 5.000°C, chíp đo quang đã nổ tung rồi ạ! | **5.000°C** · nhiệt độ lõi nổ · R/380 · [0.75, 0.55] | Cô trợ lý sóc hoạt hình đeo kính cận to tròn, mặc áo blouse trắng phòng thí nghiệm, hốt hoảng ôm bảng kẹp tài liệu, chiếc nhiệt kế điện tử đo nhiệt độ trên tay bốc khói đen kịt vì quá tải chỉ số 5000 độ C. |
| b07 | 00:43.3–00:54.7 (11.4s) | L32 | Các chuyên viên kỹ thuật không hề nghe nhầm đâu! Theo công bố chính thức trên tạp chí khoa học danh tiếng Science, sự sụp đổ đột ngột của bọt khí Cavitation nén ép các phân tử khí đến mức sinh nhiệt từ 4.700°C đến 5.000°C! | **4.700°C** · công bố Science · L/380 · [0.3, 0.55] | Bìa tạp chí Science danh tiếng: trang bìa in hình ảnh thực nghiệm vụ nổ bọt khí Cavitation của Tôm Súng với dòng nhiệt độ 4.700°C - 5.000°C nổi bật. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này. |
| b08 | 00:54.7–00:59.0 (4.3s) | L33 | Nhiệt độ này xấp xỉ với nhiệt độ 5.500°C trên bề mặt của chính Mặt Trời! | **5.500°C** · bề mặt Mặt Trời · R/380 · [0.75, 0.55] | So sánh vũ trụ chấn động: BÊN TRÁI bề mặt Mặt Trời rực lửa vàng cam nóng 5.500°C; BÊN PHẢI chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật bắn bọt khí Cavitation tí hon đạt 5.000°C tương đương nhau. |
| b09 | 00:59.0–01:08.5 (9.5s) | L34 | Kèm theo nhiệt độ bề mặt Mặt Trời là một chớp sáng xanh lơ lóe lên trong tích tắc, hiện tượng mà giới vật lý gọi là Sonoluminescence, tức là ánh sáng sinh ra từ sóng âm thanh! |  | Hiện tượng phát quang Sonoluminescence: một chớp sáng plasma xanh lam lóe lên rực rỡ trong bóng tối đáy biển, sinh ra trực tiếp từ sóng âm thanh nén ép. |
| b10 | 01:08.5–01:19.5 (11.0s) | L35 | Sóng xung kích tỏa ra từ vụ nổ bọt khí đủ sức làm choáng váng hoặc tiêu diệt gọn gàng một con cá nhỏ hay làm vỡ nát mai cua cứng cách xa 2cm mà ngòi nổ Tôm Súng thậm chí chưa từng chạm vào người con mồi! | **2cm** · tầm bắn sóng âm · R/380 · [0.75, 0.55] | Tác động thực chiến: sóng xung kích hình vòm làm mai một con cua cứng cách 2cm nứt toác, các chú tôm cá xung quanh ngã ngửa choáng váng; chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật thổi khói ở nòng càng. |
| b11 | 01:19.5–01:29.4 (9.9s) | L36 | Đó là lý do vì sao các bảo tàng thủy cung không bao giờ dám nuôi Tôm Súng trong các bể kính thông thường, vì cú nổ bọt khí ở cự ly gần có thể tạo ra vi chấn làm rạn nứt cả kính cường lực dày! |  | Tình huống hài hước ở thủy cung: một bể cá cảnh bằng kính dày bị nứt một đường chéo lớn sau cú bắn của chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật, nước phun phì phì khiến nhân viên lau dọn toát mồ hôi. |

### scene04 · ĐÀN TÔM RANG BẮP LÀM ĐIẾC RADAR TÀU NGẦM THẾ CHIẾN II · 88.6s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:06.8 (6.8s) | L37 | Lật mở hồ sơ tác chiến lịch sử năm 1942 giữa đỉnh điểm Thế chiến II tại mặt trận Thái Bình Dương! | **NĂM 1942** · Thế chiến II · L/380 · [0.3, 0.55] | Không khí Thế chiến II năm 1942: một tấm bản đồ quân sự Thái Bình Dương với các tuyến đường biển chiến lược, mô hình tàu ngầm và máy bay thời chiến. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này. |
| b02 | 00:06.8–00:13.7 (6.9s) | L38 | Hải quân Hoa Kỳ bắt đầu trang bị hệ thống định vị thủy âm Sonar tối tân nhất thời bấy giờ cho toàn bộ hạm đội tàu ngầm và tàu khu trục. |  | Hệ thống Sonar tối tân: một chiếc chiếc tàu ngầm hải quân màu xám đậm khổng lồ với tháp chỉ huy và các cảm biến vòm sonar phía trước đang lặn dưới biển, vòm radar thủy âm mũi tàu phát ra các vòng sóng xanh lục quét đáy biển tìm đối phương. |
| b03 | 00:13.7–00:19.1 (5.4s) | L39 | Mục tiêu tác chiến là lắng nghe âm thanh động cơ chân vịt của tàu ngầm đối phương ẩn nấp dưới lòng biển sâu. |  | Bên trong khoang điều khiển tàu ngầm: thủy thủ đeo tai nghe chuyên dụng, mắt chăm chú nhìn vào màn hình dao động ký tìm tín hiệu chân vịt tàu địch. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này. |
| b04 | 00:19.1–00:29.0 (9.9s) | L40 | Bản tin đặc biệt từ trạm tác chiến Thái Bình Dương: Toàn bộ hệ thống cảm biến âm thanh đang bị gây nhiễu trắng! Đáy biển phát ra tiếng nổ liên thanh như hàng vạn máy súng đang bắn đồng loạt! |  | Phát thanh viên khẩn cấp: loa phát thanh căn cứ hải quân rung bần bật, dòng chữ 'CẢNH BÁO NHIỄU TRẮNG' nhấp nháy đỏ trên màn hình hiển thị. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này. |
| b05 | 00:29.0–00:38.6 (9.6s) | L41 | Thủy thủ đoàn hoang mang cực độ! Thay vì nghe thấy tiếng ù ù trầm đục của tàu ngầm phe địch, trên tai nghe của các nhân viên Sonar liên tục dội về những âm thanh lách tách đinh tai nhức óc, |  | Thủy thủ đoàn hoang mang cực độ: các nhân viên Sonar nhảy dựng lên ôm tai nghe nhăn nhó, màn hình âm thanh dội về những dải sóng âm sắc nhọn đinh tai nhức óc. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này. |
| b06 | 00:38.6–00:44.9 (6.3s) | L42 | nghe chẳng khác nào ai đó đang đổ hàng triệu gói bắp ngô vào lò vi sóng khổng lồ rồi rang nổ liên tục dưới đáy biển! |  | Hình ảnh ẩn dụ hài hước: một chiếc lò vi sóng khổng lồ đặt dưới đáy biển sâu đang rang nổ hàng triệu gói bắp ngô bơ vàng rực 'bốp bốp' liên thanh làm cả đại dương rung chuyển. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này. |
| b07 | 00:44.9–00:56.5 (11.6s) | L43 | Bộ chỉ huy quân sự Mỹ lập tức đặt diện tình nghi vào một loại vũ khí gây nhiễu sóng âm bí mật của phe đối phương. Họ phải khẩn cấp mời các nhà sinh vật học và chuyên gia âm thanh từ Đại học UCLA đến khảo sát thực địa. |  | Đoàn điều tra khoa học UCLA: các nhà khoa học mặc áo lặn mang kính bơi và micro thu âm chuyên dụng lặn xuống rạn san hô đầy bỡ ngỡ. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này. |
| b08 | 00:56.5–01:10.5 (14.0s) | L44 | Và kết quả điều tra khiến các tướng lĩnh quân sự phải ôm đầu cười trừ: Thủ phạm phá hoại hệ thống radar trị giá hàng triệu đô la không phải vũ khí tối mật nào, mà chính là hàng triệu con Pháo Thủ Tí Hon Tôm Súng đang đua nhau búng càng săn mồi dưới rạn san hô! |  | Cảnh tượng phát hiện bất ngờ: hàng triệu chú Tôm Súng hoạt hình màu cam đỏ đội mũ bảo hộ vàng bé xíu trong rạn san hô đua nhau búng càng súng 'tách tách', các tướng lĩnh hải quân đứng nhìn nhau ôm trán phì cười. |
| b09 | 01:10.5–01:22.5 (12.0s) | L45 | Về sau, chính các thuyền trưởng tàu ngầm Mỹ đã tận dụng sự cố này như một chiến thuật ngụy trang tài tình: Họ thường xuyên chủ động lái tàu ngầm ẩn nấp sâu vào các rạn san hô nơi bầy Tôm Súng đang nổ đại bác liên thanh, |  | Chiến thuật tàu ngầm ngụy trang tài tình: thuyền trưởng tàu ngầm Mỹ đứng trong buồng lái ra lệnh điều khiển chiếc chiếc tàu ngầm hải quân màu xám đậm khổng lồ với tháp chỉ huy và các cảm biến vòm sonar phía trước chủ động lặn sâu nấp sát vào vách rạn san hô nhiệt đới. |
| b10 | 01:22.5–01:28.6 (6.1s) | L46 | để âm thanh 218 dB của chúng che giấu hoàn toàn tiếng động cơ tàu ngầm trước sự lùng sục của đối phương! | **218 dB** · bức tường âm thanh · R/380 · [0.75, 0.55] | Bức tường âm thanh che giấu động cơ: hàng ngàn chú chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật xung quanh búng càng súng 218 dB rền vang, che giấu hoàn toàn tiếng động cơ tàu ngầm trước hệ thống sóng âm lùng sục của đối ph |

### scene05 · LÍNH GÁC CÁ BỐNG VÀ TỬ HUYỆT RỤNG CÀNG · 88.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.2 (9.2s) | L47 | Một vũ khí hỏa lực hạng nặng dù uy lực đến đâu cũng luôn tồn tại những lỗ hổng kỹ thuật chết người. Và tử huyệt số một của Pháo Thủ Tí Hon chính là: Gã gần như mù tịt! |  | Tử huyệt mắt mù: phóng to khuôn mặt chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật, lớp mai trùm kín mắt, mắt đeo kính râm dán hai dấu X mù tịt, hai tay quờ quạng vấp phải hòn đá ngầm lúng túng. |
| b02 | 00:09.2–00:18.6 (9.4s) | L48 | Lớp vỏ giáp trên đầu phát triển quá đà đã che khuất gần như toàn bộ nhãn cầu, khiến thị lực của Tôm Súng vô cùng mờ mạt, chỉ phân biệt được sáng tối mà không nhìn rõ hình thù kẻ thù đang tiến lại gần. |  | Góc nhìn mờ ảo: mô phỏng tầm nhìn của Tôm Súng chỉ toàn mảng màu xám nhòe nhoẹt không rõ hình thù, một cái bóng kẻ săn mồi lờ mờ tiến lại gần. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này. |
| b03 | 00:18.6–00:30.9 (12.3s) | L49 | Để khắc phục lỗi thiết kế tai hại này, Tôm Súng đã ký một hợp đồng liên minh quân sự đỉnh cao với loài Cá Bống biển! Cá Bống có đôi mắt lồi to tròn cực kỳ tinh tường, đảm nhận vị trí trinh sát canh gác cửa hang 24/7. | **24/7** · lính gác canh cửa · L/380 · [0.25, 0.55] | Liên minh quân sự kỳ diệu: BÊN TRÁI chú cá bống biển Goby hoạt hình màu vàng cát sọc xanh, mắt to lồi tròn xoe tinh ranh như kính viễn vọng, vây lưng dựng đứng như cột ăng-ten rada cảnh giới đứng gác ngoài cửa hang, mắt lồi đảo 360 độ cực tinh tường; BÊN PHẢI chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, |
| b04 | 00:30.9–00:37.2 (6.3s) | L50 | Trong khi đó, Tôm Súng dùng chiếc râu dài của mình liên tục chạm nhẹ vào vây đuôi của Cá Bống để nhận tín hiệu rung động. |  | Cận cảnh đường truyền tín hiệu: chiếc râu tôm dài như sợi dây cáp quang chạm nhẹ vào vây đuôi cá bống, các vòng sóng tín hiệu rung động chạy dọc thân râu. |
| b05 | 00:37.2–00:45.3 (8.1s) | L51 | Mỗi khi phát hiện bóng dáng kẻ săn mồi nguy hiểm, Cá Bống chỉ cần quẫy nhẹ đuôi báo động: Tôm Súng lập tức lùi tọt vào hang sâu an toàn, |  | Báo động khẩn cấp: chú cá bống biển Goby hoạt hình màu vàng cát sọc xanh, mắt to lồi tròn xoe tinh ranh như kính viễn vọng, vây lưng dựng đứng như cột ăng-ten rada cảnh giới quẫy đuôi rung lắc dữ dội, chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow sa |
| b06 | 00:45.3–00:54.2 (8.9s) | L52 | đổi lại Cá Bống được quyền dọn vào ở ké miễn phí trong căn hầm kiên cố do chính Tôm Súng cặm cụi đào bới suốt ngày đêm! Một hợp đồng đôi bên cùng có lợi mẫu mực của tự nhiên. |  | Căn hầm kiên cố ấm cúng: bên trong hang đá sạch sẽ, chú cá bống biển Goby hoạt hình màu vàng cát sọc xanh, mắt to lồi tròn xoe tinh ranh như kính viễn vọng, vây lưng dựng đứng như cột ăng-ten rada cảnh giới nằm thư giãn còn chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công tr |
| b07 | 00:54.2–01:00.4 (6.2s) | L53 | Báo cáo thử nghiệm độ bền: Nếu khẩu đại bác bên phải bị gãy rụng thì cỗ máy này có tự hủy luôn không? |  | Thử nghiệm rụng càng: một chú cua khổng lồ giơ kẹp thắc mắc bên cạnh bản vẽ chiếc càng súng bị gãy rời khỏi thân tôm. |
| b08 | 01:00.4–01:13.2 (12.8s) | L54 | Đây chính là cơ chế đảo chiều kỳ diệu nhất của tạo hóa! Nếu trong giao chiến chiếc càng súng khổng lồ bị đứt rời, chiếc càng gắp nhỏ xíu bên trái sẽ lập tức nhận lệnh sinh học: Nó bắt đầu phình to dần và biến đổi thành một khẩu đại bác mới toanh sau vài lần lột xác! |  | Cơ chế biến đổi đảo chiều: BÊN TRÁI chiếc càng gắp nhỏ xíu bên trái nhận tín hiệu bắt đầu phình to dần thành càng súng mới; BÊN PHẢI chiếc càng súng gãy mọc lại thành càng gắp. |
| b09 | 01:13.2–01:17.1 (3.8s) | L55 | Còn tại vị trí chiếc càng cũ bị gãy, một chiếc càng gắp nhỏ sẽ mọc lại thay thế. |  | Sơ đồ chuyển giao công nghệ sinh học: mũi tên vòng tròn mô tả chu trình đổi bên của hai chiếc càng, đảm bảo cơ thể luôn có một khẩu pháo và một chiếc kẹp ăn mồi. |
| b10 | 01:17.1–01:28.9 (11.8s) | L56 | Tuy nhiên, mỗi khi lột xác thì toàn bộ cơ thể mềm oặt như cọng bún, đại bác mất hoàn toàn tác dụng. Trong những ngày hiểm nghèo đó, gã pháo thủ lừng danh đành ngoan ngoãn nép mình sau lưng chú cá bống canh cửa, chờ lớp vỏ giáp cứng cáp trở lại! |  | Tử huyệt lột xác: chú Tôm Súng hoạt hình màu cam đỏ đội mũ bảo hộ vàng vừa lột xác, cơ thể mềm nhũn như sợi bún, càng súng rũ xuống bất lực, nép run rẩy sau lưng chú cá bống biển Goby hoạt hình màu vàng cát sọc xanh đang đứng dang vây che chở. |

### scene06 · BÀI HỌC KÍCH THƯỚC VÀ BÓNG ĐEN 860V TẬP SAU · 83.0s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:10.7 (10.7s) | L57 | Báo cáo tổng kết thử nghiệm kỹ thuật số 16: Sinh vật bé nhỏ Tôm Súng để lại cho giới khoa học một bài học công nghệ vô cùng sâu sắc. Kích thước cơ thể chưa bao giờ là thước đo duy nhất cho sức mạnh sinh tồn. |  | Phòng tổng kết kỹ thuật: tấm bảng tổng kết mang huy hiệu số 16 với biểu đồ đánh giá: Sức mạnh 99/100, Âm lượng 218 dB, Nhiệt độ 5.000°C; chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật đứng trên bục chào nghiêm trang. |
| b02 | 00:10.7–00:17.4 (6.8s) | L58 | Đôi khi những hỏa lực khủng khiếp và tinh vi nhất của tự nhiên lại được ẩn giấu bên trong một thân xác tí hon khiêm nhường dưới đáy biển sâu. |  | Hình ảnh triết lý thiên nhiên: đại dương bao la với những sinh vật khổng lồ bơi qua, nhưng tâm điểm ánh sáng chiếu vào chú chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật bé nhỏ phát sáng rực rỡ với khẩu đại bác uy lực. |
| b03 | 00:17.4–00:31.4 (14.0s) | L59 | Chính cơ chế nén bọt khí Cavitation và hiện tượng phát quang âm thanh của Pháo Thủ Tí Hon đã và đang mở ra cho các kỹ sư hiện đại vô số ứng dụng đột phá trong công nghệ làm sạch sóng siêu âm, y học tán sỏi thận và động cơ phản lực chất lỏng tương lai! |  | Ứng dụng tương lai của con người: BÊN TRÁI máy rửa siêu âm công nghiệp; BÊN PHẢI máy tán sỏi thận y tế hiện đại mô phỏng cơ chế bọt khí Cavitation của Tôm Súng. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này. |
| b04 | 00:31.4–00:43.2 (11.8s) | L60 | Bạn ấn tượng nhất với điều gì ở Pháo Thủ Tí Hon Tôm Súng: Cú nổ 218 dB làm điếc tai hải quân, hay bọt khí nóng 5.000°C ngang bề mặt Mặt Trời? Hãy để lại ý kiến bình luận của đội kỹ thuật bên dưới nhé! | **218 dB** · nổ điếc tàu ngầm · L/380 · [0.25, 0.55]<br>**5.000°C** · nóng ngang Mặt Trời · R/480 · [0.75, 0.55] | Khung bình luận tương tác: chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật cầm micro hướng về phía người xem, bên cạnh là 2 ô bình luận: 'CÚ NỔ 218 dB' và 'BỌT KHÍ 5.000°C' kèm biểu tượng dấu hỏi chấm to lớn. |
| b05 | 00:43.2–00:52.9 (9.6s) | L61 | Và bây giờ, hãy hướng ngòi bút về phân cảnh kết thúc bí ẩn! Trong tập tiếp theo, chúng ta sẽ rời xa đáy biển mặn để tiến vào vùng nước ngọt đục ngầu của lưu vực rừng rậm Amazon. |  | Chuyển cảnh bí ẩn: ngòi bút vẽ tay đang phác họa một dòng sông Amazon đục ngầu huyền bí, sương mù giăng kín mặt nước rừng rậm nhiệt đới. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này. |
| b06 | 00:52.9–01:03.5 (10.7s) | L62 | Hãy chiêm ngưỡng một bóng đen bí ẩn uốn lượn dài tới 2m! Một sinh vật trơn trượt không hề có răng nanh nhọn hoắt hay nọc độc chết người, nhưng bên trong cơ thể lại chứa tới 6.000 tế bào pin sinh học nối tiếp nhau, | **2m** · chiều dài bóng đen · L/380 · [0.25, 0.55]<br>**6.000 PIN** · tế bào phát điện · R/480 · [0.75, 0.55] | BÓNG ĐEN BÍ ẨN TẬP TIẾP THEO (TASTE-68): một bóng đen tuyền uốn lượn hình sin dài 2 mét dưới làn nước mờ đục, xung quanh là 6000 khối pin sinh học nhỏ phát sáng bí ẩn kèm dấu hỏi chấm khổng lồ. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này. |
| b07 | 01:03.5–01:11.9 (8.3s) | L63 | sẵn sàng phóng ra luồng xung điện kinh hoàng lên tới 860V! Cú giật điện đủ sức đánh ngất lịm cả cá sấu khổng lồ và ngựa trưởng thành ngay dưới dòng nước! | **860V** · điện áp cực hạn · R/380 · [0.75, 0.55] | Tia sét điện bùng nổ: từ bóng đen bí ẩn phóng ra những luồng sét điện màu xanh tím giật tung bọt nước, BÊN PHẢI bóng một con cá sấu bị giật điện ngất lịm, đồng hồ đo điện báo 860 Vôn. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này. |
| b08 | 01:11.9–01:23.0 (11.1s) | L64 | Nhưng điều kỳ lạ nhất là tại sao chính bản thân sinh vật này lại không hề bị điện giật? Đố các chuyên viên kỹ thuật biết danh tính của cỗ máy phát điện sống bí ẩn này là ai? Hãy viết ngay câu trả lời của bạn dưới phần bình luận nhé! |  | Khung hình tò mò kêu gọi bình luận: bóng đen uốn lượn bí ẩn với dấu hỏi chấm to tướng '?' màu vàng phát sáng rực rỡ, kèm dòng chữ gợi mở khán giả đoán tên con vật bên dưới phần bình luận. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này. |

## 5. Phân cảnh Shorts — từng beat

Banner: **ĐẠI BÁC 218 DECIBEL: / NÓNG 5.000 ĐỘ C!** · giọng 49.7s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Cảnh báo thử nghiệm vũ khí! |  |
| s02 | 00:01.9 | S02 | Bạn có tin một sinh vật bé nhỏ dài chưa đầy 4cm lại sở hữu hỏa lực nổ to hơn cả động cơ máy bay phản lực? | **4cm** · kích thước tí hon · R/620 · [0.75, 0.55] |
| s03 | 00:07.7 | S03 | Đây là Tôm Súng, hay còn gọi là Pháo Thủ Tí Hon của các rạn san hô nhiệt đới! |  |
| s04 | 00:11.8 | S04 | Thứ nhất, chiếc càng súng khổng lồ của nó có thể kẹp lại với gia tốc kinh hoàng 8.000g, | **8.000g** · gia tốc cực đại · L/620 · [0.25, 0.55] |
| s05 | 00:16.4 | S05 | tạo ra âm thanh lên tới 218 dB làm rung chuyển đáy biển! | **218 dB** · âm thanh cực hạn · R/620 · [0.75, 0.55] |
| s06 | 00:20.5 | S06 | Thứ hai, cú kẹp phụt ra tia nước phản lực xé toạc áp suất, sinh ra bọt khí phát nổ ở nhiệt độ gần 5.000°C, | **5.000°C** · nhiệt độ lõi nổ · L/620 · [0.25, 0.55] |
| s07 | 00:27.4 | S07 | nóng ngang bề mặt Mặt Trời và phát ra chớp sáng lóe mắt! |  |
| s08 | 00:30.3 | S08 | Thứ ba, vào Thế chiến II, hàng triệu con tôm súng đã đồng thanh nổ |  |
| s09 | 00:33.8 | S09 | càng làm điếc đặc toàn bộ hệ thống định vị thủy âm Sonar của Hải quân Hoa Kỳ! | **SONAR MỸ** · Thế chiến II · R/620 · [0.75, 0.55] |
| s10 | 00:37.5 | S10 | Dù sở hữu đại bác hủy diệt nhưng mắt nó lại gần như mù tịt, |  |
| s11 | 00:40.6 | S11 | phải thuê vệ sĩ cá bống canh cửa để đổi lấy chỗ ở an toàn! |  |
| s12 | 00:44.0 | S12 | Đừng bao giờ đánh giá thấp những kẻ tí hon, bởi hỏa lực khủng khiếp nhất đôi khi lại nằm trong bàn tay nhỏ bé nhất! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo thử nghiệm vũ khí tối mật cấp độ đỏ. Mở khóa toàn bộ dữ liệu lưu trữ!". Bố cục: Phòng nghiên cứu vũ khí hải quân tối mật: một tập hồ sơ mật màu đỏ thẫm đóng dấu 'MẬT CẤP ĐỘ ĐỎ' nằm giữa bàn kim loại công nghệ cao, xung quanh là màn hình radar và thiết bị đo sóng âm. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Toàn đội kỹ thuật hãy chuẩn bị sẵn thiết bị bảo hộ thính giác, bởi vì cỗ máy mà chúng ta giải mã hôm nay sẽ làm đảo lộn hoàn toàn mọi định luật vật lý mà bạn từng biết.". Bố cục: Biển báo hoạt hình màu vàng vẽ chiếc tai nghe chống ồn công nghiệp ngộ nghĩnh, xung quanh là các vạch sóng âm thanh biểu đồ nhảy múa sinh động. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Quên đi những hàm răng cá mập hay xúc tu bạch tuộc khổng lồ, hãy nhìn xuống một góc đá ngầm tối tăm dưới đáy đại dương!". Bố cục: Đáy biển sâu huyền bí: BÊN TRÁI hàm răng cá mập khổng lồ và xúc tu bạch tuộc mờ ảo; BÊN PHẢI một khe đá ngầm san hô tối tăm phát ra ánh sáng bí ẩn. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đối tượng mang mã định danh số 16 của chúng ta có ngoại hình đánh lừa thị giác cực độ:". Bố cục: Chân dung phóng to hài hước: chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật đứng giữa khung hình, thân hình bé xíu nằm lọt thỏm trên thước đo milimet, mũ bảo hộ vàng lệch một bên, tay chống nạnh vẻ mặt tự tin ngầu lòi.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chiều dài cơ thể chỉ vỏn vẹn từ 3-5cm, nặng chưa đầy vài gam, trông yếu ớt chẳng khác nào một con tép riu bơi lội trong hồ cá cảnh.". Bố cục: So sánh kích thước trực quan: BÊN TRÁI chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật đứng cạnh một ngón tay người khổng lồ, thước dây chỉ đúng vạch 4cm; bên cạnh là chiếc cân tiểu ly đo trọng lượng vài gam.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng giới sinh học hải quân quốc tế lại đặt cho gã một biệt danh vô cùng đáng sợ: Pháo Thủ Tí Hon, hay còn gọi là Tôm Súng!". Bố cục: Tấm huy hiệu quân sự danh dự: chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật đứng hiên ngang trên bục vàng mang dòng chữ danh xưng 'PHÁO THỦ TÍ HON', chiếc càng súng giơ cao vác lên vai như khẩu pháo đại bác.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lý do khiến gã tí hon này được xếp vào hàng ngũ vũ khí tối thượng nằm ở chiếc càng bên phải dị dạng to bằng một nửa chiều dài cơ thể.". Bố cục: Đặc tả chiếc càng súng khổng lồ bên phải của chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật: chiếc càng to bằng nửa cơ thể, lớp vỏ cam đỏ dày cộp có các khớp bản lề cơ khí và chốt hãm chắc chắn, bóng loáng.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi khi chiếc càng này đóng sập lại, nó tạo ra một xung âm thanh kinh hoàng lên tới 218 dB!". Bố cục: Khoảnh khắc khai hỏa chấn động: chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật đóng sập chiếc càng súng, sóng âm thanh hình vòng tròn đồng tâm màu xanh lơ bùng nổ dữ dội, làm nứt toác đá ngầm xung quanh.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Để các chuyên viên kỹ thuật dễ hình dung, tiếng động cơ máy bay phản lực cất cánh gầm rú ở mức 140 dB,". Bố cục: So sánh âm lượng: BÊN TRÁI chiếc máy bay phản lực cất cánh gầm rú với đồng hồ đo chỉ 140 dB; bên cạnh là chiếc đồng hồ công nghiệp đo tiếng ồn. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "còn phát súng trường bắn sát màng nhĩ chỉ đạt 160 dB!". Bố cục: Đồ thị cột âm lượng: cột âm thanh của súng trường bắn sát tai chỉ đạt 160 dB; BÊN PHẢI cột âm thanh của chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật vọt cao tít lên mức 218 dB vượt ngưỡng chịu đựng.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Âm thanh 218 dB của một con tôm dài 4cm đủ sức xé toạc màng nhĩ con người nếu lặn quá gần,". Bố cục: Hình ảnh minh họa thợ lặn người: một người thợ lặn ôm hai tai bịt chặt vì sóng âm đinh tai nhức óc dưới nước; BÊN PHẢI chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật búng càng tự tin mỉm cười.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "và biến nó thành một trong những sinh vật tạo ra âm thanh lớn nhất trên toàn bộ hành tinh Trái Đất, sánh ngang với những tiếng gầm xuyên đại dương của loài cá voi nhà táng khổng lồ!". Bố cục: So sánh đại dương: BÊN TRÁI chú cá voi nhà táng khổng lồ dài 18m đang phát tiếng gầm; BÊN PHẢI chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật bé tí 4cm nhưng cột sóng âm ngang ngửa nhau đầy kinh ngạc.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hôm nay chúng ta sẽ cùng tháo dỡ từng chi tiết cơ khí bên trong chiếc càng súng độc nhất vô nhị này để xem:". Bố cục: Phòng mổ xẻ cơ khí: chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật đứng cạnh bản vẽ cấu tạo cơ khí khổng lồ, cầm cờ-lê mỏ lết chỉ vào các bộ phận pit-tông của chiếc càng súng.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Làm thế nào một sinh vật bé bằng ngón tay lại có thể tạo ra hỏa lực rung chuyển cả một vùng biển?". Bố cục: Cận cảnh bàn tay họa sĩ vẽ nên chiếc càng súng phóng tia năng lượng rực sáng dưới đáy biển; biểu tượng dấu hỏi chấm lớn màu vàng phát sáng tò mò.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy trải bản vẽ kỹ thuật chi tiết của chiếc càng súng lên bàn phân tích! Đa số mọi người đều lầm tưởng Tôm Súng dùng chiếc càng khổng lồ của mình để kẹp trực tiếp vào cổ con mồi hoặc bắn ra một mảnh xương nhọn hoắt như súng phóng lao.". Bố cục: Bản vẽ thiết kế Blueprint màu xanh dương: hình vẽ giải phẫu chiếc càng súng với các đường kích thước cơ khí, góc đo đạc và mũi tên chỉ dẫn chi tiết. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Quên giả thuyết nghiệp dư đó đi! Cỗ máy này hoạt động theo nguyên lý cơ học chất lỏng phức tạp hơn thế gấp bội phần.". Bố cục: Hình ảnh minh họa hiểu lầm: BÊN TRÁI hình tôm kẹp cổ cua bị gạch chéo đỏ lớn; BÊN PHẢI là mô hình dòng chảy thủy động lực học với các xoáy nước phản lực công nghệ cao. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Càng súng của Pháo Thủ Tí Hon gồm hai nửa bất đối xứng: Nửa dưới cố định có một rãnh lõm sâu chứa nước, trong khi nửa trên di động sở hữu một mấu lồi hình pit-tông đặc bằng chất sừng cứng như thép nguội.". Bố cục: Mổ xẻ 2 nửa càng súng: Nửa dưới cố định có rãnh lõm chứa đầy nước; nửa trên di động có mấu lồi pit-tông hình chóp đặc cứng như thép nguội, viền sáng nổi bật. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi chuẩn bị khai hỏa, cơ bắp bên trong càng co rút cực đại, kéo nửa trên ngửa ra sau một góc 90 độ và khóa chặt vào một cái chốt hãm sinh học tự nhiên!". Bố cục: chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật gồng mình chuẩn bị bắn: cơ bắp cuồn cuộn, kéo nửa càng trên ngửa ra sau đúng 90 độ, cơ chế lò xo sinh học khóa chặt vào ngàm chốt hãm kêu 'tách'.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thời điểm chốt hãm mở bung, toàn bộ năng lượng đàn hồi tích lũy được giải phóng trong chưa đầy 0,5 mili-giây!". Bố cục: Đồng hồ bấm giờ siêu tốc: kim đồng hồ chỉ vạch thời gian cực ngắn dưới 0,5 mili-giây; chốt hãm bung ra giải phóng năng lượng đàn hồi khổng lồ. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mấu lồi pit-tông lao thẳng vào rãnh nước với vận tốc lên tới 100 km/h, tương đương 28 m/s.". Bố cục: Cận cảnh cú sập pit-tông: mấu lồi lao thẳng xuống rãnh nước với vệt tốc độ xé gió, đồng hồ tốc độ chỉ 100 km/h (28 m/s), bọt nước văng tung tóe.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cú đóng sập thần tốc này tạo ra mức gia tốc kỷ lục lên tới 8.000g! Hãy nhớ rằng phi công lái máy bay chiến đấu tối tân chỉ cần chịu gia tốc 9g là mạch máu đã dồn xuống chân và ngất lịm!". Bố cục: Đồng hồ đo gia tốc: kim đồng hồ vọt lên mức đỏ rực 8.000g; BÊN PHẢI hình một phi công vũ trụ ngồi trong buồng lái đang choáng váng vì 9g. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ủa các anh kỹ sư ơi, em bơi cách nó tận hai gang tay mà sao sóng đánh gãy cả vây lưng thế này?". Bố cục: Chú cá con hoạt hình màu xanh biển ngơ ngác, mắt tròn xoe quay vòng hoa mắt vì choáng váng bơi cách đó 2 gang tay, vây lưng run rẩy vì luồng sóng áp lực thổi tạt ngang người.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đúng như chú cá con ngơ ngác vừa than vãn! Khi mấu lồi pit-tông dập cực mạnh vào rãnh hẹp, nó ép toàn bộ lượng nước bên trong phụt ra ngoài thành một tia nước phản lực siêu tốc.". Bố cục: Tia nước phản lực cực mạnh: mấu lồi pit-tông nén chặt đáy rãnh, tống ra một tia nước hình mũi tên áp lực cao bắn thẳng về phía trước như súng phun nước cứu hỏa siêu vi mô. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cơ chế ngòi nổ đàn hồi này bền bỉ đến mức Tôm Súng có thể búng liên tục hàng ngàn lần mà càng không hề bị nứt mỏi hay thoái hóa khớp sụn!". Bố cục: chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật đứng bắn liên thanh tưng bừng: càng súng búng liên hồi hàng ngàn phát 'bụp bụp', vỏ càng vẫn nguyên vẹn sáng bóng không hề có một vết nứt mỏi nào.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng điều điên rồ nhất vẫn chưa dừng lại ở đó, bởi vì chính tia nước phản lực này mới là ngòi nổ kích hoạt quả bom năng lượng tiếp theo!". Bố cục: Biểu tượng quả bom hẹn giờ năng lượng: tia nước phản lực phát sáng dẫn đường cho một quả bom bọt khí đang bắt đầu hình thành ở đầu ngọn nước.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bây giờ, chúng ta bước vào giai đoạn nguy hiểm nhất của cuộc thử nghiệm vũ khí: Hiện tượng vật lý mang tên bong bóng Cavitation!". Bố cục: Sơ đồ hiện tượng Cavitation: dòng nước vận tốc 100 km/h làm áp suất tụt dốc đứng thành vùng chân không, sinh ra một bọt khí li ti trong suốt phát sáng nhẹ. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi tia nước từ càng Tôm Súng bắn ra với vận tốc 100 km/h, áp suất cục bộ xung quanh dòng chảy tụt dốc không phanh xuống dưới cả áp suất bốc hơi của nước biển.". Bố cục: Đồ thị tụt áp suất: đường cong áp suất cắm thẳng xuống dưới vạch bốc hơi nước biển; bọt khí chân không phình to đến đường kính vài milimet.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hiện tượng tụt áp cực hạn này khiến nước bốc hơi tức thì ở nhiệt độ thường, tạo ra một bọt khí chân không li ti có đường kính chỉ vài mm!". Bố cục: Cận cảnh bọt khí chân không Cavitation lơ lửng trong nước biển, màng bọt khí lung linh phản chiếu ánh sáng kỳ ảo, lao vút đi xé dòng nước.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bọt khí này lao vút đi với tốc độ xé toạc dòng nước. Nhưng khi nó vừa bay được khoảng vài xăng-ti-mét, áp suất khổng lồ của khối nước đại dương xung quanh lập tức ép chặt và nghiền nát bọt khí chân không này!". Bố cục: Áp lực nước biển khổng lồ từ 4 phương 8 hướng dồn ép vào bọt khí: các mũi tên màu xanh sẫm đè nén khiến bọt khí méo mó và co cụm cực mạnh.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bọt khí sụp đổ và nổ tung trong thời gian chỉ tính bằng một phần tỷ giây!". Bố cục: Khoảnh khắc nổ sụp sụp đổ (implosion): bọt khí co nhỏ lại mức nanomet rồi nổ tung thành một quả cầu lửa nhiệt lượng phát sáng chói lòa trong nước.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo kỹ sư trưởng, cảm biến quang phổ ghi nhận nhiệt độ lõi bọt khí vừa chạm mốc 5.000°C, chíp đo quang đã nổ tung rồi ạ!". Bố cục: Cô trợ lý sóc hoạt hình đeo kính cận to tròn, mặc áo blouse trắng phòng thí nghiệm, hốt hoảng ôm bảng kẹp tài liệu, chiếc nhiệt kế điện tử đo nhiệt độ trên tay bốc khói đen kịt vì quá tải chỉ số 5000 độ C.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các chuyên viên kỹ thuật không hề nghe nhầm đâu! Theo công bố chính thức trên tạp chí khoa học danh tiếng Science, sự sụp đổ đột ngột của bọt khí Cavitation nén ép các phân tử khí đến mức sinh nhiệt từ 4.700°C đến 5.000°C!". Bố cục: Bìa tạp chí Science danh tiếng: trang bìa in hình ảnh thực nghiệm vụ nổ bọt khí Cavitation của Tôm Súng với dòng nhiệt độ 4.700°C - 5.000°C nổi bật. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhiệt độ này xấp xỉ với nhiệt độ 5.500°C trên bề mặt của chính Mặt Trời!". Bố cục: So sánh vũ trụ chấn động: BÊN TRÁI bề mặt Mặt Trời rực lửa vàng cam nóng 5.500°C; BÊN PHẢI chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật bắn bọt khí Cavitation tí hon đạt 5.000°C tương đương nhau.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kèm theo nhiệt độ bề mặt Mặt Trời là một chớp sáng xanh lơ lóe lên trong tích tắc, hiện tượng mà giới vật lý gọi là Sonoluminescence, tức là ánh sáng sinh ra từ sóng âm thanh!". Bố cục: Hiện tượng phát quang Sonoluminescence: một chớp sáng plasma xanh lam lóe lên rực rỡ trong bóng tối đáy biển, sinh ra trực tiếp từ sóng âm thanh nén ép.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sóng xung kích tỏa ra từ vụ nổ bọt khí đủ sức làm choáng váng hoặc tiêu diệt gọn gàng một con cá nhỏ hay làm vỡ nát mai cua cứng cách xa 2cm mà ngòi nổ Tôm Súng thậm chí chưa từng chạm vào người con mồi!". Bố cục: Tác động thực chiến: sóng xung kích hình vòm làm mai một con cua cứng cách 2cm nứt toác, các chú tôm cá xung quanh ngã ngửa choáng váng; chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật thổi khói ở nòng càng.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đó là lý do vì sao các bảo tàng thủy cung không bao giờ dám nuôi Tôm Súng trong các bể kính thông thường, vì cú nổ bọt khí ở cự ly gần có thể tạo ra vi chấn làm rạn nứt cả kính cường lực dày!". Bố cục: Tình huống hài hước ở thủy cung: một bể cá cảnh bằng kính dày bị nứt một đường chéo lớn sau cú bắn của chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật, nước phun phì phì khiến nhân viên lau dọn toát mồ hôi.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lật mở hồ sơ tác chiến lịch sử năm 1942 giữa đỉnh điểm Thế chiến II tại mặt trận Thái Bình Dương!". Bố cục: Không khí Thế chiến II năm 1942: một tấm bản đồ quân sự Thái Bình Dương với các tuyến đường biển chiến lược, mô hình tàu ngầm và máy bay thời chiến. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hải quân Hoa Kỳ bắt đầu trang bị hệ thống định vị thủy âm Sonar tối tân nhất thời bấy giờ cho toàn bộ hạm đội tàu ngầm và tàu khu trục.". Bố cục: Hệ thống Sonar tối tân: một chiếc chiếc tàu ngầm hải quân màu xám đậm khổng lồ với tháp chỉ huy và các cảm biến vòm sonar phía trước đang lặn dưới biển, vòm radar thủy âm mũi tàu phát ra các vòng sóng xanh lục quét đáy biển tìm đối phương.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mục tiêu tác chiến là lắng nghe âm thanh động cơ chân vịt của tàu ngầm đối phương ẩn nấp dưới lòng biển sâu.". Bố cục: Bên trong khoang điều khiển tàu ngầm: thủy thủ đeo tai nghe chuyên dụng, mắt chăm chú nhìn vào màn hình dao động ký tìm tín hiệu chân vịt tàu địch. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bản tin đặc biệt từ trạm tác chiến Thái Bình Dương: Toàn bộ hệ thống cảm biến âm thanh đang bị gây nhiễu trắng! Đáy biển phát ra tiếng nổ liên thanh như hàng vạn máy súng đang bắn đồng loạt!". Bố cục: Phát thanh viên khẩn cấp: loa phát thanh căn cứ hải quân rung bần bật, dòng chữ 'CẢNH BÁO NHIỄU TRẮNG' nhấp nháy đỏ trên màn hình hiển thị. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thủy thủ đoàn hoang mang cực độ! Thay vì nghe thấy tiếng ù ù trầm đục của tàu ngầm phe địch, trên tai nghe của các nhân viên Sonar liên tục dội về những âm thanh lách tách đinh tai nhức óc,". Bố cục: Thủy thủ đoàn hoang mang cực độ: các nhân viên Sonar nhảy dựng lên ôm tai nghe nhăn nhó, màn hình âm thanh dội về những dải sóng âm sắc nhọn đinh tai nhức óc. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nghe chẳng khác nào ai đó đang đổ hàng triệu gói bắp ngô vào lò vi sóng khổng lồ rồi rang nổ liên tục dưới đáy biển!". Bố cục: Hình ảnh ẩn dụ hài hước: một chiếc lò vi sóng khổng lồ đặt dưới đáy biển sâu đang rang nổ hàng triệu gói bắp ngô bơ vàng rực 'bốp bốp' liên thanh làm cả đại dương rung chuyển. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bộ chỉ huy quân sự Mỹ lập tức đặt diện tình nghi vào một loại vũ khí gây nhiễu sóng âm bí mật của phe đối phương. Họ phải khẩn cấp mời các nhà sinh vật học và chuyên gia âm thanh từ Đại học UCLA đến khảo sát thực địa.". Bố cục: Đoàn điều tra khoa học UCLA: các nhà khoa học mặc áo lặn mang kính bơi và micro thu âm chuyên dụng lặn xuống rạn san hô đầy bỡ ngỡ. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và kết quả điều tra khiến các tướng lĩnh quân sự phải ôm đầu cười trừ: Thủ phạm phá hoại hệ thống radar trị giá hàng triệu đô la không phải vũ khí tối mật nào, mà chính là hàng triệu con Pháo Thủ Tí Hon Tôm Súng đang đua nhau búng càng săn mồi dưới rạn san hô!". Bố cục: Cảnh tượng phát hiện bất ngờ: hàng triệu chú Tôm Súng hoạt hình màu cam đỏ đội mũ bảo hộ vàng bé xíu trong rạn san hô đua nhau búng càng súng 'tách tách', các tướng lĩnh hải quân đứng nhìn nhau ôm trán phì cười.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Về sau, chính các thuyền trưởng tàu ngầm Mỹ đã tận dụng sự cố này như một chiến thuật ngụy trang tài tình: Họ thường xuyên chủ động lái tàu ngầm ẩn nấp sâu vào các rạn san hô nơi bầy Tôm Súng đang nổ đại bác liên thanh,". Bố cục: Chiến thuật tàu ngầm ngụy trang tài tình: thuyền trưởng tàu ngầm Mỹ đứng trong buồng lái ra lệnh điều khiển chiếc chiếc tàu ngầm hải quân màu xám đậm khổng lồ với tháp chỉ huy và các cảm biến vòm sonar phía trước chủ động lặn sâu nấp sát vào vách rạn san hô nhiệt đới.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "để âm thanh 218 dB của chúng che giấu hoàn toàn tiếng động cơ tàu ngầm trước sự lùng sục của đối phương!". Bố cục: Bức tường âm thanh che giấu động cơ: hàng ngàn chú chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật xung quanh búng càng súng 218 dB rền vang, che giấu hoàn toàn tiếng động cơ tàu ngầm trước hệ thống sóng âm lùng sục của đối phương.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một vũ khí hỏa lực hạng nặng dù uy lực đến đâu cũng luôn tồn tại những lỗ hổng kỹ thuật chết người. Và tử huyệt số một của Pháo Thủ Tí Hon chính là: Gã gần như mù tịt!". Bố cục: Tử huyệt mắt mù: phóng to khuôn mặt chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật, lớp mai trùm kín mắt, mắt đeo kính râm dán hai dấu X mù tịt, hai tay quờ quạng vấp phải hòn đá ngầm lúng túng.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lớp vỏ giáp trên đầu phát triển quá đà đã che khuất gần như toàn bộ nhãn cầu, khiến thị lực của Tôm Súng vô cùng mờ mạt, chỉ phân biệt được sáng tối mà không nhìn rõ hình thù kẻ thù đang tiến lại gần.". Bố cục: Góc nhìn mờ ảo: mô phỏng tầm nhìn của Tôm Súng chỉ toàn mảng màu xám nhòe nhoẹt không rõ hình thù, một cái bóng kẻ săn mồi lờ mờ tiến lại gần. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Để khắc phục lỗi thiết kế tai hại này, Tôm Súng đã ký một hợp đồng liên minh quân sự đỉnh cao với loài Cá Bống biển! Cá Bống có đôi mắt lồi to tròn cực kỳ tinh tường, đảm nhận vị trí trinh sát canh gác cửa hang 24/7.". Bố cục: Liên minh quân sự kỳ diệu: BÊN TRÁI chú cá bống biển Goby hoạt hình màu vàng cát sọc xanh, mắt to lồi tròn xoe tinh ranh như kính viễn vọng, vây lưng dựng đứng như cột ăng-ten rada cảnh giới đứng gác ngoài cửa hang, mắt lồi đảo 360 độ cực tinh tường; BÊN PHẢI chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật đứng trong cửa hang thò chiếc râu dài ra chạm vào đuôi cá.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong khi đó, Tôm Súng dùng chiếc râu dài của mình liên tục chạm nhẹ vào vây đuôi của Cá Bống để nhận tín hiệu rung động.". Bố cục: Cận cảnh đường truyền tín hiệu: chiếc râu tôm dài như sợi dây cáp quang chạm nhẹ vào vây đuôi cá bống, các vòng sóng tín hiệu rung động chạy dọc thân râu.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi khi phát hiện bóng dáng kẻ săn mồi nguy hiểm, Cá Bống chỉ cần quẫy nhẹ đuôi báo động: Tôm Súng lập tức lùi tọt vào hang sâu an toàn,". Bố cục: Báo động khẩn cấp: chú cá bống biển Goby hoạt hình màu vàng cát sọc xanh, mắt to lồi tròn xoe tinh ranh như kính viễn vọng, vây lưng dựng đứng như cột ăng-ten rada cảnh giới quẫy đuôi rung lắc dữ dội, chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật nhận tín hiệu lập tức thụt lùi tọt vào hang sâu an toàn trong chớp mắt.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "đổi lại Cá Bống được quyền dọn vào ở ké miễn phí trong căn hầm kiên cố do chính Tôm Súng cặm cụi đào bới suốt ngày đêm! Một hợp đồng đôi bên cùng có lợi mẫu mực của tự nhiên.". Bố cục: Căn hầm kiên cố ấm cúng: bên trong hang đá sạch sẽ, chú cá bống biển Goby hoạt hình màu vàng cát sọc xanh, mắt to lồi tròn xoe tinh ranh như kính viễn vọng, vây lưng dựng đứng như cột ăng-ten rada cảnh giới nằm thư giãn còn chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật cần mẫn dùng càng xúc cát đá dọn dẹp như xe ủi đất công trình chuyên nghiệp.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo thử nghiệm độ bền: Nếu khẩu đại bác bên phải bị gãy rụng thì cỗ máy này có tự hủy luôn không?". Bố cục: Thử nghiệm rụng càng: một chú cua khổng lồ giơ kẹp thắc mắc bên cạnh bản vẽ chiếc càng súng bị gãy rời khỏi thân tôm.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đây chính là cơ chế đảo chiều kỳ diệu nhất của tạo hóa! Nếu trong giao chiến chiếc càng súng khổng lồ bị đứt rời, chiếc càng gắp nhỏ xíu bên trái sẽ lập tức nhận lệnh sinh học: Nó bắt đầu phình to dần và biến đổi thành một khẩu đại bác mới toanh sau vài lần lột xác!". Bố cục: Cơ chế biến đổi đảo chiều: BÊN TRÁI chiếc càng gắp nhỏ xíu bên trái nhận tín hiệu bắt đầu phình to dần thành càng súng mới; BÊN PHẢI chiếc càng súng gãy mọc lại thành càng gắp.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn tại vị trí chiếc càng cũ bị gãy, một chiếc càng gắp nhỏ sẽ mọc lại thay thế.". Bố cục: Sơ đồ chuyển giao công nghệ sinh học: mũi tên vòng tròn mô tả chu trình đổi bên của hai chiếc càng, đảm bảo cơ thể luôn có một khẩu pháo và một chiếc kẹp ăn mồi.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuy nhiên, mỗi khi lột xác thì toàn bộ cơ thể mềm oặt như cọng bún, đại bác mất hoàn toàn tác dụng. Trong những ngày hiểm nghèo đó, gã pháo thủ lừng danh đành ngoan ngoãn nép mình sau lưng chú cá bống canh cửa, chờ lớp vỏ giáp cứng cáp trở lại!". Bố cục: Tử huyệt lột xác: chú Tôm Súng hoạt hình màu cam đỏ đội mũ bảo hộ vàng vừa lột xác, cơ thể mềm nhũn như sợi bún, càng súng rũ xuống bất lực, nép run rẩy sau lưng chú cá bống biển Goby hoạt hình màu vàng cát sọc xanh đang đứng dang vây che chở.
```
</details>

<details><summary>L57</summary>

```text
HÌNH L57 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo tổng kết thử nghiệm kỹ thuật số 16: Sinh vật bé nhỏ Tôm Súng để lại cho giới khoa học một bài học công nghệ vô cùng sâu sắc. Kích thước cơ thể chưa bao giờ là thước đo duy nhất cho sức mạnh sinh tồn.". Bố cục: Phòng tổng kết kỹ thuật: tấm bảng tổng kết mang huy hiệu số 16 với biểu đồ đánh giá: Sức mạnh 99/100, Âm lượng 218 dB, Nhiệt độ 5.000°C; chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật đứng trên bục chào nghiêm trang.
```
</details>

<details><summary>L58</summary>

```text
HÌNH L58 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đôi khi những hỏa lực khủng khiếp và tinh vi nhất của tự nhiên lại được ẩn giấu bên trong một thân xác tí hon khiêm nhường dưới đáy biển sâu.". Bố cục: Hình ảnh triết lý thiên nhiên: đại dương bao la với những sinh vật khổng lồ bơi qua, nhưng tâm điểm ánh sáng chiếu vào chú chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật bé nhỏ phát sáng rực rỡ với khẩu đại bác uy lực.
```
</details>

<details><summary>L59</summary>

```text
HÌNH L59 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chính cơ chế nén bọt khí Cavitation và hiện tượng phát quang âm thanh của Pháo Thủ Tí Hon đã và đang mở ra cho các kỹ sư hiện đại vô số ứng dụng đột phá trong công nghệ làm sạch sóng siêu âm, y học tán sỏi thận và động cơ phản lực chất lỏng tương lai!". Bố cục: Ứng dụng tương lai của con người: BÊN TRÁI máy rửa siêu âm công nghiệp; BÊN PHẢI máy tán sỏi thận y tế hiện đại mô phỏng cơ chế bọt khí Cavitation của Tôm Súng. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L60</summary>

```text
HÌNH L60 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bạn ấn tượng nhất với điều gì ở Pháo Thủ Tí Hon Tôm Súng: Cú nổ 218 dB làm điếc tai hải quân, hay bọt khí nóng 5.000°C ngang bề mặt Mặt Trời? Hãy để lại ý kiến bình luận của đội kỹ thuật bên dưới nhé!". Bố cục: Khung bình luận tương tác: chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật cầm micro hướng về phía người xem, bên cạnh là 2 ô bình luận: 'CÚ NỔ 218 dB' và 'BỌT KHÍ 5.000°C' kèm biểu tượng dấu hỏi chấm to lớn.
```
</details>

<details><summary>L61</summary>

```text
HÌNH L61 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và bây giờ, hãy hướng ngòi bút về phân cảnh kết thúc bí ẩn! Trong tập tiếp theo, chúng ta sẽ rời xa đáy biển mặn để tiến vào vùng nước ngọt đục ngầu của lưu vực rừng rậm Amazon.". Bố cục: Chuyển cảnh bí ẩn: ngòi bút vẽ tay đang phác họa một dòng sông Amazon đục ngầu huyền bí, sương mù giăng kín mặt nước rừng rậm nhiệt đới. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L62</summary>

```text
HÌNH L62 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy chiêm ngưỡng một bóng đen bí ẩn uốn lượn dài tới 2m! Một sinh vật trơn trượt không hề có răng nanh nhọn hoắt hay nọc độc chết người, nhưng bên trong cơ thể lại chứa tới 6.000 tế bào pin sinh học nối tiếp nhau,". Bố cục: BÓNG ĐEN BÍ ẨN TẬP TIẾP THEO (TASTE-68): một bóng đen tuyền uốn lượn hình sin dài 2 mét dưới làn nước mờ đục, xung quanh là 6000 khối pin sinh học nhỏ phát sáng bí ẩn kèm dấu hỏi chấm khổng lồ. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L63</summary>

```text
HÌNH L63 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "sẵn sàng phóng ra luồng xung điện kinh hoàng lên tới 860V! Cú giật điện đủ sức đánh ngất lịm cả cá sấu khổng lồ và ngựa trưởng thành ngay dưới dòng nước!". Bố cục: Tia sét điện bùng nổ: từ bóng đen bí ẩn phóng ra những luồng sét điện màu xanh tím giật tung bọt nước, BÊN PHẢI bóng một con cá sấu bị giật điện ngất lịm, đồng hồ đo điện báo 860 Vôn. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>L64</summary>

```text
HÌNH L64 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng điều kỳ lạ nhất là tại sao chính bản thân sinh vật này lại không hề bị điện giật? Đố các chuyên viên kỹ thuật biết danh tính của cỗ máy phát điện sống bí ẩn này là ai? Hãy viết ngay câu trả lời của bạn dưới phần bình luận nhé!". Bố cục: Khung hình tò mò kêu gọi bình luận: bóng đen uốn lượn bí ẩn với dấu hỏi chấm to tướng '?' màu vàng phát sáng rực rỡ, kèm dòng chữ gợi mở khán giả đoán tên con vật bên dưới phần bình luận. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Cảnh báo thử nghiệm vũ khí!". Bố cục: Cảnh báo thử nghiệm vũ khí tối mật: biển báo nguy hiểm tam giác vàng phát sáng chớp nháy cảnh báo sóng xung kích đinh tai nhức óc dưới đáy biển. KHÔNG có chú Tôm Súng đội mũ bảo hộ trong cảnh này.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Bạn có tin một sinh vật bé nhỏ dài chưa đầy 4cm lại sở hữu hỏa lực nổ to hơn cả động cơ máy bay phản lực?". Bố cục: So sánh kích thước hỏa lực: BÊN TRÁI máy bay phản lực khổng lồ gầm rú xịt khói; BÊN PHẢI chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng tí hon đứng trên thước đo 4cm giơ chiếc càng súng khổng lồ đầy thách thức.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Đây là Tôm Súng, hay còn gọi là Pháo Thủ Tí Hon của các rạn san hô nhiệt đới!". Bố cục: Chân dung rực rỡ: chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng đứng oai phong trên mỏm đá san hô, mũ bảo hộ vàng chói lọi, chiếc càng súng to kềnh càng phát ra những tia năng lượng xanh biếc lấp lánh.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Thứ nhất, chiếc càng súng khổng lồ của nó có thể kẹp lại với gia tốc kinh hoàng 8.000g,". Bố cục: Cận cảnh cơ chế sập càng thần tốc: mấu lồi đóng sập với gia tốc chóng mặt 8.000g, đồng hồ đo gia tốc rung bần bật bốc khói.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "tạo ra âm thanh lên tới 218 dB làm rung chuyển đáy biển!". Bố cục: Sóng âm thanh nổ tung: xung âm thanh 218 dB bùng phát thành các vòng tròn sóng xung kích nổ rách nước biển, làm các hòn sỏi xung quanh rung chuyển bắn tung tóe.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Thứ hai, cú kẹp phụt ra tia nước phản lực xé toạc áp suất, sinh ra bọt khí phát nổ ở nhiệt độ gần 5.000°C,". Bố cục: Hiện tượng Cavitation siêu nhiệt: tia nước cực mạnh tạo bọt khí chân không phát nổ, nhiệt độ lõi đạt mốc 5.000°C rực lửa chói lòa.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "nóng ngang bề mặt Mặt Trời và phát ra chớp sáng lóe mắt!". Bố cục: So sánh chớp sáng Sonoluminescence: một bên là quả cầu lửa Mặt Trời nóng bỏng, một bên là chớp sáng plasma xanh biếc phát ra từ cú búng càng của chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Thứ ba, vào Thế chiến II, hàng triệu con tôm súng đã đồng thanh nổ càng". Bố cục: Hàng triệu pháo thủ rạn san hô: hàng ngàn chú chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng dưới đáy biển đồng loạt búng càng súng nổ vang rền như bão đạn liên thanh rực sáng dưới đáy biển.
```
</details>

<details><summary>S09</summary>

```text
HÌNH S09 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "làm điếc đặc toàn bộ hệ thống định vị thủy âm Sonar của Hải quân Hoa Kỳ!". Bố cục: Tàu ngầm hải quân bị điếc: một chiếc chiếc tàu ngầm hải quân màu xám đậm khổng lồ với tháp chỉ huy và các cảm biến vòm sonar phía trước quân sự chìm trong biển sóng âm nhiễu loạn, các ăng-ten cảm biến sonar quay tít mù vì quá tải tín hiệu.
```
</details>

<details><summary>S10</summary>

```text
HÌNH S10 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Dù sở hữu đại bác hủy diệt nhưng mắt nó lại gần như mù tịt,". Bố cục: Điểm yếu thị lực: chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng đeo cặp kính cận dày cộp, hai tay quờ quạng đụng đầu vào tảng đá san hô lúng túng ngây ngô.
```
</details>

<details><summary>S11</summary>

```text
HÌNH S11 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "phải thuê vệ sĩ cá bống canh cửa để đổi lấy chỗ ở an toàn!". Bố cục: Đôi bạn cùng tiến: chú cá bống biển Goby hoạt hình màu vàng cát sọc xanh, mắt to lồi tròn xoe tinh ranh như kính viễn vọng, vây lưng dựng đứng như cột ăng-ten rada cảnh giới đứng gác cửa hang nghiêm nghị, chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng đứng phía sau lấy râu chạm đuôi cá bống đầy ăn ý trong căn hầm san hô an toàn.
```
</details>

<details><summary>S12</summary>

```text
HÌNH S12 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Đừng bao giờ đánh giá thấp những kẻ tí hon, bởi hỏa lực khủng khiếp nhất đôi khi lại nằm trong bàn tay nhỏ bé nhất!". Bố cục: Khoảnh khắc tổng kết trọn vẹn: chú Tôm Súng hoạt hình màu cam đỏ, càng súng khổng lồ bên phải, đội mũ bảo hộ vàng đứng trên đỉnh rạn san hô rực rỡ, giơ cao chiếc càng súng đại bác mỉm cười tự tin, dòng nước trong xanh lấp lánh chiến thắng.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/64 của video YouTube về Tôm Súng). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật. Nhân vật phụ cố định: chú cá bống biển Goby hoạt hình màu vàng cát sọc xanh, mắt to lồi tròn xoe tinh ranh như kính viễn vọng, vây lưng dựng đứng như cột ăng-ten rada cảnh giới; chú cá con hoạt hình màu xanh biển ngơ ngác, mắt tròn xoe quay vòng hoa mắt vì choáng váng; chiếc tàu ngầm hải quân màu xám đậm khổng lồ với tháp chỉ huy và các cảm biến vòm sonar phía trước; cô trợ lý sóc hoạt hình đeo kính cận to tròn, mặc áo blouse trắng phòng thí nghiệm, cầm bảng kẹp tài liệu. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/12 của video YouTube Shorts về Tôm Súng). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Tôm Súng hoạt hình màu cam đỏ rực rỡ, mắt to lồi tinh nghịch lấp lánh, một chiếc càng súng khổng lồ bên phải to bằng nửa thân mình với rãnh pit-tông cơ khí, đầu đội một chiếc mũ bảo hộ công trình màu vàng (yellow safety hard hat) nổi bật. Nhân vật phụ: chú cá bống biển Goby hoạt hình màu vàng cát sọc xanh, mắt to lồi tròn xoe tinh ranh như kính viễn vọng, vây lưng dựng đứng như cột ăng-ten rada cảnh giới; chiếc tàu ngầm hải quân màu xám đậm khổng lồ với tháp chỉ huy và các cảm biến vòm sonar phía trước. 
```
</details>

## 7. SEO

- **title:** Vũ Khí 218 dB Nóng 5.000°C Làm Điếc Sonar Hải Quân Mỹ?! | Tôm Súng | Tập 16
- **hook_paragraph:** Tôm Súng (Pistol Shrimp) chỉ dài 4cm nhưng sở hữu chiếc càng đại bác búng ra âm thanh 218 dB, tạo bọt khí Cavitation nóng tới 5.000°C ngang bề mặt Mặt Trời và từng làm điếc đặc hệ thống Sonar của Hải quân Mỹ trong Thế chiến II! Giải mã hồ sơ vũ khí tối mật của Pháo Thủ Tí Hon.
- **question:** Bạn ấn tượng nhất với điều gì ở Pháo Thủ Tí Hon Tôm Súng: Cú nổ 218 dB làm điếc radar tàu ngầm, hay bọt khí nóng 5.000°C ngang bề mặt Mặt Trời? Đoán xem bóng đen tập sau là loài nào nhé!
- **next_teaser:** sinh vật Amazon phóng luồng điện 860V giật ngất cá sấu và ngựa
- **shorts_title:** Tại Sao Con Tôm 4cm Này Lại Bắn Nổ To Hơn Động Cơ Máy Bay?! 🦐 #shorts #tomsung
- **shorts_desc:** Tôm Súng chỉ dài 4cm nhưng búng càng tạo âm thanh 218 dB, bọt khí nổ nóng 5.000°C ngang Mặt Trời và từng làm điếc hệ thống Sonar Hải quân Mỹ! Khám phá bí mật Pháo Thủ Tí Hon.
- **bullets:** Càng súng kẹp nước tạo xung âm thanh 218 dB to hơn động cơ máy bay phản lực · Gia tốc 8.000g và cơ chế pit-tông bắn tia nước vận tốc 100 km/h · Bọt khí Cavitation sụp đổ đạt nhiệt độ 5.000°C phát quang Sonoluminescence · Vụ án Thế chiến II năm 1942: Đàn tôm san hô làm tê liệt hệ thống Sonar Hải quân Mỹ · Hợp đồng liên minh với vệ sĩ Cá Bống và cơ chế đảo chiều mọc lại càng súng · Bật mí bóng đen bí ẩn tập tiếp theo: Sinh vật phóng điện 860V sông Amazon
- **tags:** tôm súng, tom sung, pistol shrimp, snapping shrimp, tôm súng 218 db, tôm súng bắn bọt khí 5000 độ, cavitation, sonoluminescence, pháo thủ tí hon, tôm súng hải quân mỹ, tôm súng và cá bống, động vật hài hước, thế giới động vật, vẽ chuyện hoang dã, whiteboard animation việt nam
- **hashtags:** #TomSung #PistolShrimp #TheGioiDongVat #VeChuyenHoangDa #WhiteboardAnimation

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-16-tom-sung
python src/episode/pipeline.py tts    projects/tap-16-tom-sung     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-16-tom-sung     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-16-tom-sung     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-16-tom-sung              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-16-tom-sung --force
python scripts/beat_sheet.py projects/tap-16-tom-sung               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-16-tom-sung/audio/shorts.wav projects/tap-16-tom-sung/renders/tap-16-tom-sung_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-16-tom-sung
python src/episode/pipeline.py seo    projects/tap-16-tom-sung
python src/episode/episode_doc.py     projects/tap-16-tom-sung
```
