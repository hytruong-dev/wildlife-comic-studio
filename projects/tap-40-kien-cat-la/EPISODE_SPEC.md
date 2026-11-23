# TẬP 40 — KIẾN CẮT LÁ · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-40-kien-cat-la`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-40-kien-cat-la`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F2` · **Persona giọng:** `ky_su_vu_khi` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Kiến Cắt Lá |
| Tiêu đề YouTube | Đại Công Trình Ngầm: Kiến Cắt Lá Xây Đô Thị 50 Triệu Dân Với Điều Hòa Tự Nhiên?! \| Tập 40 |
| Video dài | `renders/tap-40-kien-cat-la_long.mp4` — 8:44.0 (524.0s) |
| Shorts | `renders/tap-40-kien-cat-la_shorts.mp4` — 0:46.8 (46.8s) |
| Thumbnail | `renders/tap-40-kien-cat-la_thumbnail.jpg` |
| Số hình | dài 70 beat / 70 ảnh riêng; Shorts 12 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.11**, Shorts tempo tự tính (≥ 1.07) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/70 của video YouTube về Kiến Cắt Lá). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách mặt cắt kiến trúc địa tầng công trình ngầm đại quy mô (Subterranean Architectural Cross-Section & Industrial CAD Blueprint): bản vẽ mặt cắt các tầng đất sâu 8m với độ chuẩn xác kiến trúc cao, sơ đồ luồng khí thông gió đối lưu khí động học, đường ống luân chuyển hữu cơ sinh thái, nét vẽ kỹ thuật kiến trúc sắc bén, bảng đo đạc tỷ lệ công trình, phối màu xanh lục bảo thực vật, nâu đất phù sa và đường lưới kỹ thuật xanh cyan blueprint; NỀN TRẮNG TINH hoàn toàn, không watermark, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú kiến cắt lá hoạt hình thông minh đội mũ kỹ sư công trình màu cam, mang kính bảo hộ lao động, hai chiếc hàm răng cưa titan sáng bóng, vác trên lưng chiếc thước kẻ kỹ thuật; tranh vẽ 2D comic công trình ngầm nguyên bản. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — KHÁM PHÁ KỲ QUAN KIẾN TRÚC ĐẠI CÔNG TRÌNH NGẦM DƯỚI LÒNG ĐẤT
*Thẻ chương:* Bí mật về nền nông nghiệp lâu đời nhất hành tinh

*Badge:* `ĐẠI CÔNG TRƯỜNG NGẦM` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene01_p0.wav` (426 ký tự) · mood `hao_hung`

```text
Chào mừng toàn thể các kỹ sư công trình ngầm, các kiến trúc sư đô thị và những người đam mê khoa học sinh thái bước vào đại công trường kỳ vĩ nhất hành tinh! [laughter] Hôm nay, phòng thiết kế kỹ thuật sinh học của chúng tôi xin trân trọng giải mã một kỳ quan xây dựng vĩ đại nằm ẩn sâu dưới lòng thảm rừng nhiệt đới Amazon, nơi cư ngụ của một đế chế tí hon với tài năng quy hoạch đô thị vượt xa trí tưởng tượng của con người!
```
**Part 1** → `audio/vs/scene01_p1.wav` (364 ký tự) · mood `don_dap`

```text
Hãy quan sát mặt cắt bản vẽ kỹ thuật địa chất: Bên dưới một diện tích mặt đất rộng tới năm mươi mét vuông là cả một thành phố ngầm khổng lồ ăn sâu tám mét xuống lòng đất! Để xây dựng nên đô thị này, hàng triệu cư dân tí hon đã đào bới và vận chuyển hơn bốn mươi tấn đất đá lên bề mặt, tương đương với việc con người xây dựng đại kim tự tháp Giza bằng xẻng cầm tay!
```
**Part 2** → `audio/vs/scene01_p2.wav` (203 ký tự) · 🎭 cameo `co_tro_ly`

```text
[surprise-oh] Thưa Tổng chỉ huy công trình, cảm biến địa chất xác nhận bên trong thành phố ngầm này có tới hơn một ngàn căn phòng chuyên dụng kết nối với nhau bằng mạng lưới đường hầm thông gió hoàn hảo!
```
**Part 3** → `audio/vs/scene01_p3.wav` (490 ký tự) · mood `tram_bi_an`

```text
Một thông số kiến trúc gây choáng váng thưa trợ lý giám sát! Những công trình sư tài ba kiến tạo nên kiệt tác này mang tên khoa học Atta cephalotes, hay còn gọi là loài Kiến Cắt Lá, nhưng toàn bộ giới xây dựng thế giới đều nghiêng mình thán phục gọi chúng bằng danh hiệu: Đại Công Trình Sư Ngầm! Trong khi loài người mới chỉ phát minh ra nền nông nghiệp cách đây khoảng mười ngàn năm, thì loài kiến này đã thành lập những trang trại trồng nấm quy mô công nghiệp từ năm mươi triệu năm trước!
```
**Part 4** → `audio/vs/scene01_p4.wav` (360 ký tự) · mood `hao_hung`

```text
Lá cây mà chúng rầm rộ cắt xẻ và gánh vác ngày đêm trên lưng hoàn toàn không phải để ăn, mà là nguồn nguyên liệu phân bón thượng hạng để nuôi dưỡng những vườn nấm khổng lồ dưới lòng đất! Bí mật cơ khí và tổ chức nào đã giúp chúng vận hành cỗ máy nông nghiệp vĩ đại này? Xin mời quý vị cùng tôi mở bản vẽ kỹ thuật tầng một để giải mã lưỡi cưa sinh học đầu tiên!
```

### scene02 — CẶP HÀM RĂNG CƯA RUNG TẦN SỐ CAO CẮT NGỌT TỪNG PHIẾN LÁ
*Thẻ chương:* Cơ chế dao cắt rung siêu âm lấy cảm hứng cho ngành cơ khí

*Badge:* `LƯỠI CƯA SINH HỌC` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene02_p0.wav` (315 ký tự) · mood `hao_hung`

```text
Xin mời các kỹ sư cơ khí hãy zoom cận cảnh vào công cụ lao động tiền tuyến của những người thợ khai thác gỗ: Cặp hàm răng cưa thần kỳ! Hàm của kiến thợ cắt lá được gia cố bằng các nguyên tử kẽm và mangan siêu cứng, biến các răng cưa ở rìa hàm sắc bén và bền bỉ ngang ngửa với lưỡi dao phẫu thuật bằng hợp kim titan!
```
**Part 1** → `audio/vs/scene02_p1.wav` (383 ký tự) · mood `don_dap`

```text
Nhưng điều làm nên sự kinh ngạc tột độ chính là cơ chế rung tần số cao: Khi cắn vào phiến lá cây dày cộm, phần bụng của chú kiến sẽ rung lắc liên hồi với tần số lên tới một ngàn lần mỗi giây! Dao động rung này truyền thẳng xuống cặp hàm, biến nó thành một chiếc máy cưa rung siêu âm, giúp xẻ ngọt phiến lá dai nhách chỉ trong vòng chưa đầy ba mươi giây mà không tốn chút sức lực nào!
```
**Part 2** → `audio/vs/scene02_p2.wav` (127 ký tự) · 🎭 cameo `co_tro_ly`

```text
[surprise-oh] Thưa Chỉ huy, có phải mỗi mảnh lá cây được cắt ra nặng gấp nhiều lần trọng lượng cơ thể của chú kiến thợ không ạ?
```
**Part 3** → `audio/vs/scene02_p3.wav` (321 ký tự) · mood `don_dap`

```text
Chính xác tuyệt đối! Một chú kiến thợ chỉ nặng vài mi-li-gam nhưng có thể ngoạm chặt một mảnh lá nặng gấp hai mươi lần trọng lượng cơ thể mình, sau đó vác hiên ngang trên lưng chạy nước rút suốt quãng đường hàng trăm mét trở về tổ! Tương đương với việc một người lực sĩ gánh một chiếc xe hơi trên vai chạy cự ly marathon!
```
**Part 4** → `audio/vs/scene02_p4.wav` (334 ký tự) · mood `tram_bi_an`

```text
Khi hàng triệu chú kiến cùng rầm rộ khuân vác lá cây trên những con đường cao tốc thông thoáng được dọn sạch chướng ngại vật, chúng tạo nên một cảnh tượng kỳ vĩ tựa như một dòng sông xanh biếc đang cuồn cuộn chảy xuyên qua rừng rậm! Nhưng lá cây đem về tổ sẽ được chế biến ra sao? Mời các bạn cùng tôi bước xuống tầng hầm nông nghiệp!
```
**Part 5** → `audio/vs/scene02_p5.wav` (306 ký tự) · mood `hao_hung`

```text
Tốc độ hành quân của những đoàn kiến cắt lá có thể đạt tới mười lăm mét mỗi phút! Để tối ưu hóa năng suất vận chuyển, các kiến thợ công binh đi trước sẽ dùng hàm dọn sạch mọi chướng ngại vật, tạo nên những xa lộ liên tỉnh bằng phẳng rộng tới ba mươi xăng-ti-mét kéo dài bất tận xuyên qua bụi rậm nhiệt đới!
```

### scene03 — TRANG TRẠI NẤM CỘNG SINH CỔ XƯA NHẤT HÀNH TINH
*Thẻ chương:* Mối quan hệ cộng sinh tương hỗ hoàn hảo giữa kiến và nấm

*Badge:* `VƯỜN NẤM NGẦM` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene03_p0.wav` (379 ký tự) · mood `tram_bi_an`

```text
Bước vào các khoang hầm trung tâm sâu dưới lòng đất, chúng ta sẽ được chiêm ngưỡng những vườn nấm màu trắng ngà xốp như bọt biển: Đây chính là nguồn lương thực duy nhất nuôi sống toàn bộ hàng triệu cư dân của Đại Công Trình Sư Ngầm! Loài nấm này mang tên Leucoagaricus gongylophorus, một giống nấm cộng sinh đặc biệt đã gắn liền với số phận loài kiến suốt năm mươi triệu năm qua.
```
**Part 1** → `audio/vs/scene03_p1.wav` (287 ký tự) · mood `don_dap`

```text
Quy trình chế biến thức ăn tại đây diễn ra nghiêm ngặt như một nhà máy công nghiệp hiện đại: Những mảnh lá cây mang về sẽ được các kiến thợ nhai nát thành bột mịn, sau đó tẩm ướp các giọt enzyme tiêu hóa từ dịch ruột của kiến rồi đắp thành luống phân bón tơi xốp để cấy sợi nấm lên trên.
```
**Part 2** → `audio/vs/scene03_p2.wav` (236 ký tự) · mood `hao_hung`

```text
Sợi nấm sẽ tiêu hóa chất xơ cellulose cứng nhắc trong lá cây và sản sinh ra các cấu trúc phình to giàu protein và đường gọi là gongylidia. Những viên nang dinh dưỡng này chính là món ăn thượng hạng bồi bổ cho ấu trùng kiến và kiến chúa!
```
**Part 3** → `audio/vs/scene03_p3.wav` (226 ký tự) · mood `tram_bi_an`

```text
Loài nấm này phụ thuộc hoàn toàn vào kiến để được chăm sóc và diệt cỏ dại, còn loài kiến phụ thuộc hoàn toàn vào nấm để có thức ăn. Một liên minh sinh học bền chặt trường tồn qua hàng triệu năm thăng trầm của lịch sử Trái Đất!
```
**Part 4** → `audio/vs/scene03_p4.wav` (240 ký tự) · mood `hao_hung`

```text
Nhưng để duy trì một vườn nấm khổng lồ dưới lòng đất sâu tăm tối và ngột ngạt, làm thế nào để hàng ngàn tấn nấm không bị ngạt khí cacbonic hay chết vì nấm mốc dịch bệnh? Xin mời các bạn cùng tôi khám phá hệ thống điều hòa nhiệt độ đỉnh cao!
```
**Part 5** → `audio/vs/scene03_p5.wav` (347 ký tự) · mood `tram_bi_an`

```text
Ước tính mỗi tổ kiến cắt lá tiêu thụ lượng lá cây tương đương với lượng cỏ mà một con bò trưởng thành ăn trong suốt cả năm! Nhưng chúng không bao giờ tàn sát một cái cây duy nhất đến cạn kiệt, mà luôn luân phiên thu hoạch lá từ hàng chục loài cây khác nhau để bảo tồn sự đa dạng sinh học và tránh tích tụ độc tố thực vật trong trang trại nấm ngầm!
```

### scene04 — HỆ THỐNG THÔNG GIÓ ĐỐI LƯU GIỮ NHIỆT ĐỘ HAI MƯƠI LĂM ĐỘ HOÀN HẢO
*Thẻ chương:* Kỹ thuật thông gió thụ động lấy cảm hứng cho các tòa nhà chọc trời

*Badge:* `HỆ THỐNG ĐIỀU HÒA` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene04_p0.wav` (385 ký tự) · mood `hao_hung`

```text
Đây chính là đỉnh cao cơ điện công trình khiến các kỹ sư nhân loại phải ngả mũ bái phục: Hệ thống điều hòa không khí tự nhiên hoàn toàn không sử dụng điện năng! Vườn nấm ngầm đòi hỏi một môi trường cực kỳ khắt khe: Nhiệt độ phải luôn duy trì ổn định ở mức hai mươi lăm độ C và độ ẩm phải đạt chín mươi phần trăm, bất kể bên ngoài mặt đất đang là nắng hạn bỏng rát hay mưa bão ngập lụt!
```
**Part 1** → `audio/vs/scene04_p1.wav` (278 ký tự) · mood `don_dap`

```text
Để đạt được sự cân bằng vi khí hậu kỳ diệu này, Đại Công Trình Sư Ngầm đã đào đục hàng ngàn giếng thông gió thẳng đứng nối từ các phòng nuôi nấm lên mặt đất. Các giếng ở trung tâm tổ được thiết kế nhô cao hơn và đón gió nhiều hơn, tạo ra sự chênh lệch áp suất khí quyển mạnh mẽ!
```
**Part 2** → `audio/vs/scene04_p2.wav` (265 ký tự) · mood `tram_bi_an`

```text
Hiệu ứng ống khói đối lưu nhiệt tự động hút không khí nóng ẩm chứa đầy khí cacbonic độc hại từ đáy tổ đẩy ra ngoài qua các lỗ trung tâm, đồng thời hút luồng không khí tươi mát giàu oxy từ các giếng thông gió ngoại vi chìm sâu xuống đáy tổ, làm mát toàn bộ hệ thống!
```
**Part 3** → `audio/vs/scene04_p3.wav` (404 ký tự) · mood `hao_hung`

```text
Khi nhiệt độ thay đổi, hàng vạn kiến thợ sẽ hối hả chạy đến các cửa giếng để mở rộng hoặc đắp đất bịt bớt miệng giếng lại, điều tiết lưu lượng gió chính xác đến từng mi-li-mét khối! Nhiều tòa nhà chọc trời tiết kiệm năng lượng hiện đại ngày nay, tiêu biểu như trung tâm Eastgate tại Zimbabwe, đã mô phỏng trực tiếp nguyên lý thông gió của tổ kiến cắt lá để giảm chín mươi phần trăm chi phí điện máy lạnh!
```
**Part 4** → `audio/vs/scene04_p4.wav` (213 ký tự) · mood `don_dap`

```text
Một công nghệ thông gió thụ động siêu việt! Và để bảo vệ kỳ quan đô thị này trước sự xâm lăng của kẻ thù và nấm mốc ký sinh, kiến cắt lá còn sở hữu một lực lượng vũ trang và y tế chuyên môn hóa đến mức phi thường!
```
**Part 5** → `audio/vs/scene04_p5.wav` (329 ký tự) · mood `don_dap`

```text
Ngay cả trong những trận mưa lũ nhiệt đới xối xả ngập úng mặt đất, cấu trúc miệng giếng thông gió hình phễu ngược và mạng lưới cống thoát nước ngầm vẫn ngăn không cho một giọt nước nào chảy tràn vào các buồng nấm trung tâm! Một bản lĩnh thiết kế thủy lợi và địa kỹ thuật khiến mọi công trình sư hiện đại phải kinh ngạc thán phục!
```

### scene05 — PHÂN CHIA ĐẲNG CẤP XÃ HỘI CỰC ĐOAN VÀ VŨ KHÍ KHÁNG SINH SỐNG
*Thẻ chương:* Đội quân kiến lính bọc thép và phòng thí nghiệm y tế di động

*Badge:* `LỰC LƯỢNG QUÂN SỰ` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene05_p0.wav` (251 ký tự) · mood `hao_hung`

```text
Hãy quan sát sự phân tầng xã hội tinh vi trong tổ kiến: Chẳng có một xã hội động vật nào trên Trái Đất có sự phân hóa hình thể và chức năng chuyên môn sâu sắc như loài kiến cắt lá! Trong tổ có tới bốn đẳng cấp kiến khác nhau cùng chung sống hòa thuận:
```
**Part 1** → `audio/vs/scene05_p1.wav` (319 ký tự) · mood `don_dap`

```text
Ở vị trí quân đội thường trực là những chú kiến lính khổng lồ nặng gấp ba trăm lần kiến thợ nhỏ! Chúng sở hữu hộp sọ bọc thép khổng lồ chứa đầy cơ hàm cuồn cuộn, với cặp hàm sắc bén như chiếc kìm bấm có thể cắn thủng lớp da giày của con người và sẵn sàng hiến dâng tính mạng để chặn đứng những con thú ăn kiến đói khát!
```
**Part 2** → `audio/vs/scene05_p2.wav` (257 ký tự) · mood `tram_bi_an`

```text
Ngược lại, ở vị trí chăm sóc y tế là những chú kiến siêu tí hon chỉ nhỏ bằng đầu tăm. Chúng thường cưỡi ngay trên phiến lá mà các chú kiến thợ đang vác để làm vệ sinh, liên tục xua đuổi những con ruồi ký sinh phorid nguy hiểm muốn đẻ trứng lên đầu đồng đội!
```
**Part 3** → `audio/vs/scene05_p3.wav` (368 ký tự) · mood `hao_hung`

```text
Đặc biệt nhất, trên lớp vỏ mai của kiến thợ có một lớp phấn trắng mờ: Đó chính là quần thể vi khuẩn Pseudonocardia cộng sinh, một nhà máy sản xuất thuốc kháng sinh tự nhiên! Loại kháng sinh này tiêu diệt đặc hiệu các loài nấm mốc ký sinh độc hại mang tên Escovopsis, giữ cho trang trại nấm ngầm luôn vô trùng tuyệt đối suốt năm mươi triệu năm mà không hề bị lờn thuốc!
```
**Part 4** → `audio/vs/scene05_p4.wav` (160 ký tự) · mood `tram_bi_an`

```text
Một hệ thống y tế và an ninh quốc phòng hoàn hảo đến từng mi-crô-mét, bảo vệ sự phồn vinh của đế chế ngầm qua muôn vàn thử thách khắc nghiệt của mẹ thiên nhiên!
```

### scene06 — TÔN VINH KIỆT TÁC KIẾN TRÚC VÀ BÀI HỌC CHO NHÂN LOẠI
*Thẻ chương:* Bài học về sự đoàn kết tổ chức và phát triển bền vững

*Badge:* `TỔNG KẾT DỰ ÁN` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene06_p0.wav` (403 ký tự) · mood `hao_hung`

```text
Thưa toàn thể hội đồng thẩm định kiến trúc và quý khán giả theo dõi công trình, sau khi khảo sát chi tiết toàn bộ năm bản vẽ từ đại công trường ngầm tám mét, cặp hàm cưa rung siêu âm, vườn nấm nông nghiệp năm mươi triệu năm, hệ thống thông gió đối lưu hai mươi lăm độ cho đến quân đoàn kiến lính và kháng sinh sống, hội đồng nhất trí tuyệt đối trao Chứng nhận Kỳ Quan Kiến Trúc Tự Nhiên cho Kiến Cắt Lá!
```
**Part 1** → `audio/vs/scene06_p1.wav` (312 ký tự) · mood `tram_bi_an`

```text
Đại Công Trình Sư Ngầm chính là hình mẫu kiểu mẫu về nền kinh tế tuần hoàn và phát triển bền vững không rác thải. Toàn bộ chất thải từ vườn nấm ngầm đều được đưa vào các khoang rác thải hữu cơ sâu dưới đáy tổ để tái chế và nuôi dưỡng đất rừng nhiệt đới, tạo nên thảm thực vật xanh tươi màu mỡ bậc nhất hành tinh.
```
**Part 2** → `audio/vs/scene06_p2.wav` (279 ký tự) · mood `am_ap`

```text
Bài học từ loài kiến nhỏ bé nhắc nhở nhân loại chúng ta rằng: Khi hàng triệu cá nhân cùng chung sức đồng lòng, hướng về một mục tiêu chung với tinh thần kỷ luật và sự phân công lao động khoa học, những sinh vật nhỏ bé nhất cũng có thể tạo nên những kỳ tích dời non lấp bể vĩ đại!
```
**Part 3** → `audio/vs/scene06_p3.wav` (252 ký tự) · mood `hao_hung`

```text
Giữa hệ thống điều hòa thông gió đối lưu tự nhiên và kỹ thuật nuôi nấm bằng lưỡi cưa rung siêu âm, kỳ quan nào của Kiến Cắt Lá khiến bạn thán phục và truyền cảm hứng nhiều nhất? Hãy để lại ý kiến đóng góp của bạn ngay trong phần bình luận bên dưới nhé!
```
**Part 4** → `audio/vs/scene06_p4.wav` (226 ký tự) · mood `am_ap`

```text
Và đừng quên nhấn nút Đăng Ký Kênh cùng chiếc chuông thông báo để cùng đồng hành trong chuỗi tập tiếp theo của thế giới tự nhiên kỳ thú! Xin chào tạm biệt và hẹn gặp lại toàn thể các bạn trên những công trình vĩ đại tiếp theo!
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Bạn có tin loài người không phải là sinh vật đầu tiên phát minh ra nông nghiệp trên Trái Đất không? [laughter] Trước khi con người xuất hiện hàng chục triệu năm, loài Kiến Cắt Lá đã xây dựng những trang trại trồng nấm quy mô công nghiệp sâu tám mét dưới lòng đất! Bí mật kinh hoàng nằm ở chỗ: Chúng cắt lá cây không phải để ăn, mà dùng hàm rung siêu âm như máy cưa xẻ nát lá làm phân bón nuôi nấm! [dissatisfaction-hnn] Tổ của chúng đào bới hơn bốn mươi tấn đất đá, sở hữu hệ thống thông gió đối lưu tự nhiên giữ nhiệt độ luôn ổn định ở hai mươi lăm độ C mà không tốn một giọt điện năng! Thậm chí trên mai kiến còn có vi khuẩn tiết ra thuốc kháng sinh tự nhiên để bảo vệ mùa màng! [laughter] Một siêu đô thị ngầm năm mươi triệu dân vận hành bền vững suốt năm mươi triệu năm qua! Đúng là bậc thầy công trình vĩ đại nhất của tự nhiên!
```

**Whisper prompt:** `Kiến Cắt Lá, Atta cephalotes, Đại Công Trình Sư Ngầm, nấm cộng sinh, Leucoagaricus, kiến lính, kiến thợ, thông gió ngầm, 8 mét, 50 tấn đất, kháng sinh tự nhiên`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| Tập bốn mươi | Tập 40 |
| Tập bốn mươi mốt | Tập 41 |
| năm mươi triệu năm | 50 triệu năm |
| sáu mươi triệu năm | 60 triệu năm |
| hàng triệu năm | hàng triệu năm |
| triệu năm | triệu năm |
| tám mét | 8m |
| mười mét | 10m |
| ba mươi mét | 30m |
| năm mươi mét | 50m |
| hai mươi mét | 20m |
| năm mươi tấn | 50 tấn |
| hai mươi tấn | 20 tấn |
| bốn mươi tấn | 40 tấn |
| hai mươi lăm độ | 25°C |
| chín mươi phần trăm | 90% |
| một trăm phần trăm | 100% |
| năm mươi lần | 50 lần |
| ba trăm lần | 300 lần |
| ba lần | 3 lần |
| hai lần | 2 lần |
| mười lần | 10 lần |
| hai mươi tư giờ | 24 giờ |
| hai mươi bốn giờ | 24 giờ |
| thế kỷ hai mươi mốt | thế kỷ 21 |
| Đại Công Trình Sư Ngầm | Đại Công Trình Sư Ngầm |
| Atta | Atta |
| cephalotes | cephalotes |
| Leucoagaricus | Leucoagaricus |
| Pseudonocardia | Pseudonocardia |
| Escovopsis | Escovopsis |
| mười lăm mét | 15m |
| mười lăm | 15 |
| một ngàn | 1.000 |
| mười ngàn năm | 10.000 năm |
| ba mươi giây | 30 giây |
| ba mươi | 30 |
| hai mươi | 20 |
| năm mươi mét vuông | 50m² |
| năm mươi triệu dân | 50 triệu dân |
| năm mươi triệu | 50 triệu |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · KHÁM PHÁ KỲ QUAN KIẾN TRÚC ĐẠI CÔNG TRÌNH NGẦM DƯỚI LÒNG ĐẤT · 92.5s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.5 (9.5s) | L01 | Chào mừng toàn thể các kỹ sư công trình ngầm, các kiến trúc sư đô thị và những người đam mê khoa học sinh thái bước vào đại công trường kỳ vĩ nhất hành tinh! Hôm nay, |  | Phòng thiết kế kỹ thuật sinh học: chú kiến cắt lá hoạt hình thông minh đội mũ kỹ sư công trình màu cam, mang kính bảo hộ lao động, hai chiếc hàm răng cưa titan sáng bóng, vác trên lưng chiếc thước kẻ kỹ thuật; tranh vẽ 2D comic công trình ngầm nguyên bản đứng bên bàn vẽ CAD blueprint trải dài, tay cầm bút chỉ vào mặt cắt lòng đất. |
| b02 | 00:09.5–00:22.5 (13.1s) | L02 | phòng thiết kế kỹ thuật sinh học của chúng tôi xin trân trọng giải mã một kỳ quan xây dựng vĩ đại nằm ẩn sâu dưới lòng thảm rừng nhiệt đới Amazon, nơi cư ngụ của một đế chế tí hon với tài năng quy hoạch đô thị vượt xa trí tưởng tượng của con người! |  | Toàn cảnh rừng mưa nhiệt đới Amazon bạt ngàn với những tán cây cổ thụ khổng lồ vươn lên mây trời. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b03 | 00:22.5–00:28.9 (6.4s) | L03 | Hãy quan sát mặt cắt bản vẽ kỹ thuật địa chất: Bên dưới một diện tích mặt đất rộng tới 50m² là cả một thành phố ngầm |  | Mặt cắt địa chất 3D bóc tách từng lớp đất từ bề mặt thảm thực vật xuống tận độ sâu 8m dưới lòng đất. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b04 | 00:28.9–00:33.6 (4.7s) | L04 | khổng lồ ăn sâu 8m xuống lòng đất! Để xây dựng nên đô thị này, hàng triệu cư dân tí hon đã đào bới |  | Thước đo độ sâu thẳng đứng cắm mốc 8m: Hệ thống buồng ngầm đa tầng quy mô đồ sộ như tòa nhà chọc trời đảo ngược. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b05 | 00:33.6–00:36.7 (3.1s) | L05 | và vận chuyển hơn 40 tấn đất đá lên bề mặt, tương đương với việc |  | Núi đất đá 40 tấn khổng lồ trên mặt đất do hàng triệu chú kiến thợ vận chuyển từng viên đất nhỏ bé. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b06 | 00:36.7–00:40.4 (3.7s) | L06 | con người xây dựng đại kim tự tháp Giza bằng xẻng cầm tay! |  | Hình ảnh so sánh đối chiếu: Đại kim tự tháp Ai Cập bằng đá sừng sững bên cạnh công trình đào đất của đàn kiến. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b07 | 00:40.4–00:44.0 (3.6s) | L07 | Thưa Tổng chỉ huy công trình, cảm biến địa chất xác nhận bên trong thành phố |  | Cô trợ lý kỹ thuật đeo kính bảo hộ cầm máy quét siêu âm địa chấn báo cáo thông số cấu trúc ngầm. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b08 | 00:44.0–00:52.4 (8.4s) | L08 | ngầm này có tới hơn 1.000 căn phòng chuyên dụng kết nối với nhau bằng mạng lưới đường hầm thông gió hoàn hảo! Một thông số kiến trúc gây choáng váng thưa trợ lý giám |  | Sơ đồ mạng lưới 1.000 căn phòng chức năng: Phòng ấp trứng, phòng nuôi nấm, phòng kiến chúa và bãi rác ngầm. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b09 | 00:52.4–01:02.0 (9.6s) | L09 | sát! Những công trình sư tài ba kiến tạo nên kiệt tác này mang tên khoa học Atta cephalotes, hay còn gọi là loài Kiến Cắt Lá, nhưng toàn bộ giới xây dựng thế giới đều nghiêng mình thán |  | chú kiến cắt lá hoạt hình thông minh đội mũ kỹ sư công trình màu cam, mang kính bảo hộ lao động, hai chiếc hàm răng cưa titan sáng bóng, vác trên lưng chiếc thước kẻ kỹ thuật; tranh vẽ 2D comic công trình ngầm nguyên bản nở nụ cười tự hào, hai hàm răng cưa lấp lánh phản chiếu ánh đèn công trường kỹ thuật. |
| b10 | 01:02.0–01:10.0 (8.0s) | L10 | phục gọi chúng bằng danh hiệu: Đại Công Trình Sư Ngầm! Trong khi loài người mới chỉ phát minh ra nền nông nghiệp cách đây khoảng 10.000 năm, thì loài kiến |  | Biểu tượng danh hiệu vàng rực: Đại Công Trình Sư Ngầm — Danh hiệu kiến trúc sư tối cao của thế giới tự nhiên. |
| b11 | 01:10.0–01:20.9 (10.9s) | L11 | này đã thành lập những trang trại trồng nấm quy mô công nghiệp từ 50 triệu năm trước! Lá cây mà chúng rầm rộ cắt xẻ và gánh vác ngày đêm trên lưng hoàn toàn không phải để ăn, mà là nguồn nguyên liệu phân bón thượng hạng |  | Dòng thời gian so sánh: Loài người làm nông 10.000 năm đối chiếu với kiến cắt lá làm nông 50 triệu năm trước. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b12 | 01:20.9–01:32.5 (11.6s) | L12 | để nuôi dưỡng những vườn nấm khổng lồ dưới lòng đất! Bí mật cơ khí và tổ chức nào đã giúp chúng vận hành cỗ máy nông nghiệp vĩ đại này? Xin mời quý vị cùng tôi mở bản vẽ kỹ thuật tầng một để giải mã lưỡi cưa sinh học đầu tiên! |  | chú kiến cắt lá hoạt hình thông minh đội mũ kỹ sư công trình màu cam, mang kính bảo hộ lao động, hai chiếc hàm răng cưa titan sáng bóng, vác trên lưng chiếc thước kẻ kỹ thuật; tranh vẽ 2D comic công trình ngầm nguyên bản gánh mảnh lá xanh khổng lồ hình bán nguyệt trên lưng, chuẩn bị mở ra bản vẽ lưỡi cưa sinh học. |

### scene02 · CẶP HÀM RĂNG CƯA RUNG TẦN SỐ CAO CẮT NGỌT TỪNG PHIẾN LÁ · 88.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.1 (7.1s) | L13 | Xin mời các kỹ sư cơ khí hãy zoom cận cảnh vào công cụ lao động tiền tuyến của những người thợ khai thác gỗ: Cặp hàm răng cưa thần kỳ! |  | Bản vẽ cơ khí bóc tách: Cận cảnh cặp hàm răng cưa của kiến thợ được phóng to dưới kính hiển vi điện tử. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b02 | 00:07.1–00:13.7 (6.6s) | L14 | Hàm của kiến thợ cắt lá được gia cố bằng các nguyên tử kẽm và mangan siêu cứng, biến các răng cưa ở rìa hàm sắc bén và |  | Mạng lưới tinh thể nguyên tử kẽm và mangan gia cố liên kết kim loại sinh học ở rìa răng cưa. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b03 | 00:13.7–00:19.1 (5.5s) | L15 | bền bỉ ngang ngửa với lưỡi dao phẫu thuật bằng hợp kim titan! Nhưng điều làm nên sự kinh ngạc tột độ chính |  | So sánh độ cứng: Răng cưa kiến thợ cắt ngọt qua kim loại thử nghiệm sắc lẹm như dao mổ titan. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b04 | 00:19.1–00:24.1 (4.9s) | L16 | là cơ chế rung tần số cao: Khi cắn vào phiến lá cây dày cộm, phần bụng của chú kiến sẽ rung lắc liên |  | chú kiến cắt lá hoạt hình thông minh đội mũ kỹ sư công trình màu cam, mang kính bảo hộ lao động, hai chiếc hàm răng cưa titan sáng bóng, vác trên lưng chiếc thước kẻ kỹ thuật; tranh vẽ 2D comic công trình ngầm nguyên bản kích hoạt cơ chế rung bụng, các sóng dao động siêu âm lan tỏa dọc sống lưng xuống hàm. |
| b05 | 00:24.1–00:30.0 (5.9s) | L17 | hồi với tần số lên tới 1.000 lần mỗi giây! Dao động rung này truyền thẳng xuống cặp hàm, biến nó thành một chiếc máy cưa rung siêu âm, |  | Máy đo tần số hiển thị con số 1.000 Hz: Dao cắt siêu âm xẻ từng thớ lá dai nhách không tì vết. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b06 | 00:30.0–00:35.5 (5.5s) | L18 | giúp xẻ ngọt phiến lá dai nhách chỉ trong vòng chưa đầy 30 giây mà không tốn chút sức lực nào! |  | Đồng hồ bấm giờ 30 giây: Một mảnh lá tròn hoàn hảo rơi ra sau một đường cắt sắc lẹm hình cung. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b07 | 00:35.5–00:45.4 (9.9s) | L19 | Thưa Chỉ huy, có phải mỗi mảnh lá cây được cắt ra nặng gấp nhiều lần trọng lượng cơ thể của chú kiến thợ không ạ? Chính xác tuyệt đối! Một chú kiến thợ chỉ nặng vài mi-li-gam nhưng có |  | Cô trợ lý kỹ thuật trầm trồ chỉ vào chiếc cân tiểu ly đo đạc trọng lượng mảnh lá cây. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b08 | 00:45.4–00:52.0 (6.7s) | L20 | thể ngoạm chặt một mảnh lá nặng gấp 20 lần trọng lượng cơ thể mình, sau đó vác hiên ngang trên lưng chạy nước rút suốt quãng đường hàng trăm mét trở về tổ! |  | Hình ảnh minh họa: Lực sĩ con người gánh chiếc xe hơi 2 tấn trên vai chạy nước rút trên đường đua. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b09 | 00:52.0–01:02.5 (10.4s) | L21 | Tương đương với việc một người lực sĩ gánh một chiếc xe hơi trên vai chạy cự ly marathon! Khi hàng triệu chú kiến cùng rầm rộ khuân vác lá cây trên những con đường cao tốc thông thoáng được dọn sạch chướng ngại vật, chúng tạo |  | chú kiến cắt lá hoạt hình thông minh đội mũ kỹ sư công trình màu cam, mang kính bảo hộ lao động, hai chiếc hàm răng cưa titan sáng bóng, vác trên lưng chiếc thước kẻ kỹ thuật; tranh vẽ 2D comic công trình ngầm nguyên bản gánh mảnh lá nặng gấp 20 lần cơ thể phi như bay trên cành cây với nụ cười sảng khoái. |
| b10 | 01:02.5–01:12.8 (10.3s) | L22 | nên một cảnh tượng kỳ vĩ tựa như một dòng sông xanh biếc đang cuồn cuộn chảy xuyên qua rừng rậm! Nhưng lá cây đem về tổ sẽ được chế biến ra sao? Mời các bạn cùng tôi bước xuống tầng hầm nông nghiệp! |  | Dòng sông lá xanh cuồn cuộn chảy: Hàng triệu phiến lá xanh di động như làn sóng xanh trên mặt đất rừng. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b11 | 01:12.8–01:23.4 (10.6s) | L23 | Tốc độ hành quân của những đoàn kiến cắt lá có thể đạt tới 15m mỗi phút! Để tối ưu hóa năng suất vận chuyển, các kiến thợ công binh đi trước sẽ dùng hàm dọn sạch mọi chướng ngại vật, tạo |  | Đồng hồ đo tốc độ hành quân 15m/phút: Đội hình quân binh kiến di chuyển thẳng tắp theo trật tự hoàn hảo. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b12 | 01:23.4–01:28.9 (5.5s) | L24 | nên những xa lộ liên tỉnh bằng phẳng rộng tới 30 xăng-ti-mét kéo dài bất tận xuyên qua bụi rậm nhiệt đới! |  | Xa lộ cao tốc rừng rậm rộng 30cm được các kỹ sư dọn sạch sỏi đá, phẳng phiu như đường băng cao tốc. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |

### scene03 · TRANG TRẠI NẤM CỘNG SINH CỔ XƯA NHẤT HÀNH TINH · 85.8s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:10.8 (10.8s) | L25 | Bước vào các khoang hầm trung tâm sâu dưới lòng đất, chúng ta sẽ được chiêm ngưỡng những vườn nấm màu trắng ngà xốp như bọt biển: Đây chính là nguồn lương thực duy nhất nuôi sống toàn bộ hàng triệu cư dân của Đại Công Trình Sư Ngầm! |  | Tầng hầm nông nghiệp ngầm: chú kiến cắt lá hoạt hình thông minh đội mũ kỹ sư công trình màu cam, mang kính bảo hộ lao động, hai chiếc hàm răng cưa titan sáng bóng, vác trên lưng chiếc thước kẻ kỹ thuật; tranh vẽ 2D comic công trình ngầm nguyên bản bước vào căn phòng nuôi nấm trắng ngà xốp như bọt biển, tay cầm kính lúp. |
| b02 | 00:10.8–00:16.0 (5.2s) | L26 | Loài nấm này mang tên Leucoagaricus gongylophorus, một giống nấm cộng sinh đặc biệt |  | Bảng phân loại sinh học: Sợi nấm Leucoagaricus gongylophorus đan xen dày đặc như tấm thảm bông tuyết. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b03 | 00:16.0–00:19.0 (3.0s) | L27 | đã gắn liền với số phận loài kiến suốt 50 triệu năm qua. |  | Vòng tròn liên minh cộng sinh vĩnh cửu 50 triệu năm giữa loài kiến và vườn nấm ngầm. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b04 | 00:19.0–00:26.6 (7.6s) | L28 | Quy trình chế biến thức ăn tại đây diễn ra nghiêm ngặt như một nhà máy công nghiệp hiện đại: Những mảnh lá cây mang về sẽ được các kiến thợ nhai nát thành bột mịn, |  | Dây chuyền sản xuất công nghiệp: Kiến thợ nghiền nhỏ lá cây thành hỗn hợp bột mịn tơi xốp. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b05 | 00:26.6–00:32.6 (6.0s) | L29 | sau đó tẩm ướp các giọt enzyme tiêu hóa từ dịch ruột của kiến rồi đắp thành luống phân bón tơi xốp để cấy sợi nấm lên trên. |  | Các giọt enzyme tiêu hóa đặc hiệu được phun đều lên luống bột lá để chuẩn bị cấy sợi nấm mới. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b06 | 00:32.6–00:40.6 (8.1s) | L30 | Sợi nấm sẽ tiêu hóa chất xơ cellulose cứng nhắc trong lá cây và sản sinh ra các cấu trúc phình to giàu protein và đường gọi là gongylidia. |  | Cấu trúc hiển vi: Sợi nấm phân giải cellulose cứng và hình thành những bọc tròn gongylidia giàu dưỡng chất. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b07 | 00:40.6–00:45.4 (4.7s) | L31 | Những viên nang dinh dưỡng này chính là món ăn thượng hạng bồi bổ cho ấu trùng kiến và kiến chúa! |  | Kiến thợ cẩn thận mớm những viên nang gongylidia béo ngậy cho các ấu trùng kiến non và kiến chúa. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b08 | 00:45.4–00:56.5 (11.2s) | L32 | Loài nấm này phụ thuộc hoàn toàn vào kiến để được chăm sóc và diệt cỏ dại, còn loài kiến phụ thuộc hoàn toàn vào nấm để có thức ăn. Một liên minh sinh học bền chặt trường tồn qua hàng triệu năm thăng trầm của lịch sử Trái Đất! |  | chú kiến cắt lá hoạt hình thông minh đội mũ kỹ sư công trình màu cam, mang kính bảo hộ lao động, hai chiếc hàm răng cưa titan sáng bóng, vác trên lưng chiếc thước kẻ kỹ thuật; tranh vẽ 2D comic công trình ngầm nguyên bản ân cần dùng râu chải chuốt và dọn dẹp các sợi nấm già cỗi, biểu tượng người làm vườn tận tụy. |
| b09 | 00:56.5–01:09.0 (12.5s) | L33 | Nhưng để duy trì một vườn nấm khổng lồ dưới lòng đất sâu tăm tối và ngột ngạt, làm thế nào để hàng ngàn tấn nấm không bị ngạt khí cacbonic hay chết vì nấm mốc dịch bệnh? Xin mời các bạn cùng tôi khám phá hệ thống điều hòa nhiệt độ đỉnh cao! |  | Khói khí cacbonic tích tụ trong hầm sâu tăm tối, đặt ra bài toán thông gió sinh tử cho cả tổ kiến. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b10 | 01:09.0–01:15.6 (6.5s) | L34 | Ước tính mỗi tổ kiến cắt lá tiêu thụ lượng lá cây tương đương với lượng cỏ mà một con bò trưởng thành ăn trong suốt cả năm! Nhưng |  | Hình ảnh so sánh: Đàn kiến tiêu thụ lá cây tương đương một chú bò sữa ăn cỏ cả năm. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b11 | 01:15.6–01:23.0 (7.4s) | L35 | chúng không bao giờ tàn sát một cái cây duy nhất đến cạn kiệt, mà luôn luân phiên thu hoạch lá từ hàng chục loài cây khác nhau để bảo tồn sự đa dạng sinh |  | Bản đồ luân chuyển thu hoạch: Đàn kiến chia tuyến khai thác luân phiên nhiều cây rừng để bảo vệ thảm thực vật. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b12 | 01:23.0–01:25.8 (2.8s) | L36 | học và tránh tích tụ độc tố thực vật trong trang trại nấm ngầm! |  | chú kiến cắt lá hoạt hình thông minh đội mũ kỹ sư công trình màu cam, mang kính bảo hộ lao động, hai chiếc hàm răng cưa titan sáng bóng, vác trên lưng chiếc thước kẻ kỹ thuật; tranh vẽ 2D comic công trình ngầm nguyên bản kiểm tra kỹ từng mẫu lá đưa vào kho, đảm bảo chất lượng phân bón tinh khiết nhất. |

### scene04 · HỆ THỐNG THÔNG GIÓ ĐỐI LƯU GIỮ NHIỆT ĐỘ HAI MƯƠI LĂM ĐỘ HOÀN HẢO · 93.0s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.3 (8.3s) | L37 | Đây chính là đỉnh cao cơ điện công trình khiến các kỹ sư nhân loại phải ngả mũ bái phục: Hệ thống điều hòa không khí tự nhiên hoàn toàn không sử dụng điện năng! |  | Phòng điều hành khí động học: chú kiến cắt lá hoạt hình thông minh đội mũ kỹ sư công trình màu cam, mang kính bảo hộ lao động, hai chiếc hàm răng cưa titan sáng bóng, vác trên lưng chiếc thước kẻ kỹ thuật; tranh vẽ 2D comic công trình ngầm nguyên bản đứng bên mô hình các giếng thông gió đối lưu tự nhiên không dùng điện. |
| b02 | 00:08.3–00:15.9 (7.6s) | L38 | Vườn nấm ngầm đòi hỏi một môi trường cực kỳ khắt khe: Nhiệt độ phải luôn duy trì ổn định ở mức 25°C C và độ ẩm phải đạt 90%, |  | Biểu đồ tiêu chuẩn môi trường: Nhiệt độ 25°C và độ ẩm 90% rực sáng trong khung cảnh hầm ngầm. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b03 | 00:15.9–00:23.5 (7.6s) | L39 | bất kể bên ngoài mặt đất đang là nắng hạn bỏng rát hay mưa bão ngập lụt! Để đạt được sự cân bằng vi khí hậu kỳ diệu này, Đại Công Trình Sư |  | Đối lập thời tiết: Mặt đất nắng cháy gay gắt hoặc bão giông nhưng dưới hầm nấm vẫn mát mẻ êm dịu. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b04 | 00:23.5–00:31.1 (7.6s) | L40 | Ngầm đã đào đục hàng ngàn giếng thông gió thẳng đứng nối từ các phòng nuôi nấm lên mặt đất. Các giếng ở trung tâm tổ được thiết kế nhô cao hơn và đón gió nhiều hơn, |  | Hệ thống giếng đứng vươn lên mặt đất: Giếng trung tâm cao nhô lên như ống khói nhà máy đón gió lộng. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b05 | 00:31.1–00:33.4 (2.2s) | L41 | tạo ra sự chênh lệch áp suất khí quyển mạnh mẽ! |  | Mũi tên chênh lệch áp suất: Áp suất thấp ở miệng giếng cao hút mạnh không khí từ dưới đáy hầm. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b06 | 00:33.4–00:46.3 (12.9s) | L42 | Hiệu ứng ống khói đối lưu nhiệt tự động hút không khí nóng ẩm chứa đầy khí cacbonic độc hại từ đáy tổ đẩy ra ngoài qua các lỗ trung tâm, đồng thời hút luồng không khí tươi mát giàu oxy từ các giếng thông gió ngoại vi chìm sâu xuống đáy tổ, làm mát toàn bộ hệ thống! |  | Dòng khí nóng chứa CO2 màu đỏ bốc lên giếng trung tâm, dòng khí tươi mát giàu O2 màu xanh tràn xuống giếng biên. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b07 | 00:46.3–00:56.5 (10.2s) | L43 | Khi nhiệt độ thay đổi, hàng vạn kiến thợ sẽ hối hả chạy đến các cửa giếng để mở rộng hoặc đắp đất bịt bớt miệng giếng lại, điều tiết lưu lượng gió chính xác đến từng mi-li-mét khối! |  | Đội cơ động kiến thợ khiêng các hòn đất nhỏ chạy đến miệng giếng để đắp thêm hoặc mở rộng van gió. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b08 | 00:56.5–01:05.0 (8.5s) | L44 | Nhiều tòa nhà chọc trời tiết kiệm năng lượng hiện đại ngày nay, tiêu biểu như trung tâm Eastgate tại Zimbabwe, đã mô phỏng trực tiếp nguyên lý thông gió của tổ kiến cắt lá để |  | Tòa nhà chọc trời Eastgate tại Zimbabwe với kiến trúc ống khói phỏng sinh học mô phỏng tổ kiến. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b09 | 01:05.0–01:09.3 (4.3s) | L45 | giảm 90% chi phí điện máy lạnh! Một công nghệ thông gió thụ động siêu |  | Biểu đồ tiết kiệm năng lượng 90%: Hệ thống xanh bền vững lấy cảm hứng từ Đại Công Trình Sư Ngầm. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b10 | 01:09.3–01:17.4 (8.2s) | L46 | việt! Và để bảo vệ kỳ quan đô thị này trước sự xâm lăng của kẻ thù và nấm mốc ký sinh, kiến cắt lá còn sở hữu một lực lượng vũ trang và y tế chuyên môn hóa đến mức phi thường! |  | chú kiến cắt lá hoạt hình thông minh đội mũ kỹ sư công trình màu cam, mang kính bảo hộ lao động, hai chiếc hàm răng cưa titan sáng bóng, vác trên lưng chiếc thước kẻ kỹ thuật; tranh vẽ 2D comic công trình ngầm nguyên bản đứng bên cạnh chú kiến lính hộ vệ khổng lồ bọc thép uy nghi bảo vệ cửa tổ. |
| b11 | 01:17.4–01:28.0 (10.6s) | L47 | Ngay cả trong những trận mưa lũ nhiệt đới xối xả ngập úng mặt đất, cấu trúc miệng giếng thông gió hình phễu ngược và mạng lưới cống thoát nước ngầm vẫn ngăn không cho một giọt nước nào chảy tràn vào các buồng nấm trung tâm! |  | Mưa lũ nhiệt đới xối xả trên mặt đất nhưng các miệng giếng phễu ngược ngăn nước tuyệt đối. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b12 | 01:28.0–01:33.0 (5.0s) | L48 | Một bản lĩnh thiết kế thủy lợi và địa kỹ thuật khiến mọi công trình sư hiện đại phải kinh ngạc thán phục! |  | Mạng lưới cống rãnh ngầm dẫn nước mưa thừa thoát xa khỏi các khoang nuôi nấm trọng yếu. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |

### scene05 · PHÂN CHIA ĐẲNG CẤP XÃ HỘI CỰC ĐOAN VÀ VŨ KHÍ KHÁNG SINH SỐNG · 68.6s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:02.8 (2.8s) | L49 | Hãy quan sát sự phân tầng xã hội tinh vi trong tổ |  | Khu căn cứ thế giới tự nhiên và y tế: chú kiến cắt lá hoạt hình thông minh đội mũ kỹ sư công trình màu cam, mang kính bảo hộ lao động, hai chiếc hàm răng cưa titan sáng bóng, vác trên lưng chiếc thước kẻ kỹ thuật; tranh vẽ 2D comic công trình ngầm nguyên bản đứng trước bảng phân cấp xã hội 4 tầng lớp kiến chuyên môn hóa. |
| b02 | 00:02.8–00:13.4 (10.6s) | L50 | kiến: Chẳng có một xã hội động vật nào trên Trái Đất có sự phân hóa hình thể và chức năng chuyên môn sâu sắc như loài kiến cắt lá! Trong tổ có tới bốn đẳng cấp kiến khác nhau cùng chung sống hòa thuận: |  | Bốn đẳng cấp kiến xếp hàng theo kích thước: Kiến lính khổng lồ, kiến thợ lớn, kiến thợ nhỏ và kiến y tế tí hon. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b03 | 00:13.4–00:23.1 (9.7s) | L51 | Ở vị trí quân đội thường trực là những chú kiến lính khổng lồ nặng gấp 300 lần kiến thợ nhỏ! Chúng sở hữu hộp sọ bọc thép khổng lồ chứa đầy cơ hàm cuồn cuộn, với cặp hàm sắc bén như chiếc kìm bấm |  | Kiến lính bọc thép khổng lồ to gấp 300 lần kiến nhỏ, cơ hàm nở rộng như chiếc kìm bấm titan sắc bén. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b04 | 00:23.1–00:28.4 (5.3s) | L52 | có thể cắn thủng lớp da giày của con người và sẵn sàng hiến dâng tính mạng để chặn đứng những con thú ăn kiến đói khát! |  | Kiến lính dũng mãnh ngoạm chặt xua đuổi con thú ăn kiến khổng lồ để bảo vệ cửa hầm tổ. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b05 | 00:28.4–00:37.0 (8.6s) | L53 | Ngược lại, ở vị trí chăm sóc y tế là những chú kiến siêu tí hon chỉ nhỏ bằng đầu tăm. Chúng thường cưỡi ngay trên phiến lá mà các chú kiến thợ đang vác để làm vệ sinh, liên |  | Chú kiến siêu tí hon bằng đầu tăm cưỡi trên phiến lá, cầm chổi mini quét sạch bụi bẩn trên lá. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b06 | 00:37.0–00:42.2 (5.2s) | L54 | tục xua đuổi những con ruồi ký sinh phorid nguy hiểm muốn đẻ trứng lên đầu đồng đội! Đặc biệt nhất, |  | Kiến tí hon dũng cảm vung râu xua đuổi con ruồi ký sinh phorid đang lượn lờ muốn đẻ trứng. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b07 | 00:42.2–00:48.2 (6.0s) | L55 | trên lớp vỏ mai của kiến thợ có một lớp phấn trắng mờ: Đó chính là quần thể vi khuẩn Pseudonocardia cộng sinh, |  | Cận cảnh vỏ mai kiến thợ phủ lớp phấn trắng vi khuẩn Pseudonocardia phát sáng lung linh. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b08 | 00:48.2–00:51.0 (2.8s) | L56 | một nhà máy sản xuất thuốc kháng sinh tự nhiên! Loại kháng sinh |  | Các phân tử kháng sinh tự nhiên tiêu diệt tận gốc mầm nấm mốc ký sinh độc hại Escovopsis. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b09 | 00:51.0–00:55.5 (4.5s) | L57 | này tiêu diệt đặc hiệu các loài nấm mốc ký sinh độc hại mang tên Escovopsis, |  | Vườn nấm sạch bong vô trùng tuyệt đối, minh chứng cho nền y tế dự phòng 50 triệu năm không lờn thuốc. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b10 | 00:55.5–01:00.6 (5.1s) | L58 | giữ cho trang trại nấm ngầm luôn vô trùng tuyệt đối suốt 50 triệu năm mà không hề bị lờn thuốc! |  | chú kiến cắt lá hoạt hình thông minh đội mũ kỹ sư công trình màu cam, mang kính bảo hộ lao động, hai chiếc hàm răng cưa titan sáng bóng, vác trên lưng chiếc thước kẻ kỹ thuật; tranh vẽ 2D comic công trình ngầm nguyên bản chào quân hàm cùng đội quân kiến lính và đội ngũ y tế tí hon tận tụy. |
| b11 | 01:00.6–01:04.3 (3.7s) | L59 | Một hệ thống y tế và an ninh quốc phòng hoàn hảo đến từng mi-crô-mét, |  | Đế chế ngầm phồn vinh rực rỡ với hàng ngàn ánh đèn công trường hoạt động ngày đêm nhộn nhịp. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b12 | 01:04.3–01:08.6 (4.3s) | L60 | bảo vệ sự phồn vinh của đế chế ngầm qua muôn vàn thử thách khắc nghiệt của mẹ thiên nhiên! |  | Tổ kiến vững vàng trước mọi biến động thời tiết, sừng sững tồn tại qua hàng triệu năm lịch sử. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |

### scene06 · TÔN VINH KIỆT TÁC KIẾN TRÚC VÀ BÀI HỌC CHO NHÂN LOẠI · 74.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:10.1 (10.1s) | L61 | Thưa toàn thể hội đồng thẩm định kiến trúc và quý khán giả theo dõi công trình, sau khi khảo sát chi tiết toàn bộ năm bản vẽ từ đại công trường ngầm 8m, cặp hàm cưa rung siêu âm, |  | Hội đồng thẩm định kiến trúc tự nhiên: chú kiến cắt lá hoạt hình thông minh đội mũ kỹ sư công trình màu cam, mang kính bảo hộ lao động, hai chiếc hàm răng cưa titan sáng bóng, vác trên lưng chiếc thước kẻ kỹ thuật; tranh vẽ 2D comic công trình ngầm nguyên bản đứng trên bục vinh danh đón nhận Bằng Chứng Nhận Kỳ Quan Kiến Trúc. |
| b02 | 00:10.1–00:22.9 (12.8s) | L62 | vườn nấm nông nghiệp 50 triệu năm, hệ thống thông gió đối lưu 25°C cho đến quân đoàn kiến lính và kháng sinh sống, hội đồng nhất trí tuyệt đối trao Chứng nhận Kỳ Quan Kiến Trúc Tự Nhiên cho Kiến Cắt Lá! Đại Công Trình Sư Ngầm |  | Năm biểu tượng bản vẽ kỹ thuật: Hầm ngầm 8m, hàm cưa siêu âm, vườn nấm 50 triệu năm, thông gió đối lưu và kháng sinh. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b03 | 00:22.9–00:33.3 (10.4s) | L63 | chính là hình mẫu kiểu mẫu về nền kinh tế tuần hoàn và phát triển bền vững không rác thải. Toàn bộ chất thải từ vườn nấm ngầm đều được đưa vào các khoang rác thải hữu cơ sâu dưới đáy tổ để tái chế và nuôi dưỡng đất rừng nhiệt |  | Sơ đồ kinh tế tuần hoàn khép kín: Toàn bộ chất thải được phân hủy tái chế làm màu mỡ đất rừng. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b04 | 00:33.3–00:36.7 (3.4s) | L64 | đới, tạo nên thảm thực vật xanh tươi màu mỡ bậc nhất hành tinh. |  | Rừng rậm nhiệt đới tươi tốt ngút ngàn nhờ công lao cải tạo đất của hàng triệu đàn kiến ngầm. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b05 | 00:36.7–00:43.4 (6.7s) | L65 | Bài học từ loài kiến nhỏ bé nhắc nhở nhân loại chúng ta rằng: Khi hàng triệu cá nhân cùng chung sức đồng lòng, hướng về một mục tiêu chung |  | chú kiến cắt lá hoạt hình thông minh đội mũ kỹ sư công trình màu cam, mang kính bảo hộ lao động, hai chiếc hàm răng cưa titan sáng bóng, vác trên lưng chiếc thước kẻ kỹ thuật; tranh vẽ 2D comic công trình ngầm nguyên bản bắt tay cùng người kỹ sư nhân loại, biểu tượng kết nối giữa thiên nhiên và công nghệ. |
| b06 | 00:43.4–00:50.3 (6.9s) | L66 | với tinh thần kỷ luật và sự phân công lao động khoa học, những sinh vật nhỏ bé nhất cũng có thể tạo nên những kỳ tích dời non lấp bể vĩ đại! |  | Hàng triệu cánh tay kiến và con người cùng chung sức dựng xây những công trình vĩ đại dời non lấp bể. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b07 | 00:50.3–00:59.7 (9.4s) | L67 | Giữa hệ thống điều hòa thông gió đối lưu tự nhiên và kỹ thuật nuôi nấm bằng lưỡi cưa rung siêu âm, kỳ quan nào của Kiến Cắt Lá khiến bạn thán phục và truyền cảm hứng nhiều nhất? |  | Hai màn hình đối chiếu: Giếng thông gió ống khói không điện và hàm răng cưa rung tần số cao. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b08 | 00:59.7–01:04.3 (4.7s) | L68 | Hãy để lại ý kiến đóng góp của bạn ngay trong phần bình luận bên dưới nhé! Và đừng |  | Biểu tượng ô bình luận ý kiến cùng cộng đồng các nhà khoa học và kỹ sư trẻ nhiệt huyết. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b09 | 01:04.3–01:10.3 (6.0s) | L69 | quên nhấn nút Đăng Ký Kênh cùng chiếc chuông thông báo để cùng đồng hành trong chuỗi tập tiếp theo của thế giới tự nhiên kỳ thú! |  | Nút Đăng Ký Kênh rực sáng cùng chiếc chuông thông báo rung động mời gọi khám phá. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này. |
| b10 | 01:10.3–01:14.9 (4.6s) | L70 | Xin chào tạm biệt và hẹn gặp lại toàn thể các bạn trên những công trình vĩ đại tiếp theo! |  | chú kiến cắt lá hoạt hình thông minh đội mũ kỹ sư công trình màu cam, mang kính bảo hộ lao động, hai chiếc hàm răng cưa titan sáng bóng, vác trên lưng chiếc thước kẻ kỹ thuật; tranh vẽ 2D comic công trình ngầm nguyên bản vẫy tay chào tạm biệt khán giả từ cửa công trình ngầm, hẹn gặp lại ở những hành trình tiếp theo. |

## 5. Phân cảnh Shorts — từng beat

Banner: **ĐẠI CÔNG TRÌNH SƯ / KỲ QUAN NÔNG NGHIỆP 50 TRIỆU NĂM?!** · giọng 45.3s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Bạn có tin loài người không phải là sinh vật đầu tiên phát minh ra nông nghiệp trên Trái Đất không? |  |
| s02 | 00:06.5 | S02 | Trước khi con người xuất hiện hàng chục triệu năm, loài Kiến Cắt Lá đã xây dựng những trang trại trồng |  |
| s03 | 00:11.3 | S03 | nấm quy mô công nghiệp sâu 8m dưới lòng đất! |  |
| s04 | 00:13.8 | S04 | Bí mật kinh hoàng nằm ở chỗ: |  |
| s05 | 00:15.9 | S05 | Chúng cắt lá cây không phải để ăn, mà dùng hàm rung siêu |  |
| s06 | 00:18.8 | S06 | âm như máy cưa xẻ nát lá làm phân bón nuôi nấm! |  |
| s07 | 00:22.3 | S07 | Tổ của chúng đào bới hơn 40 tấn đất đá, sở |  |
| s08 | 00:25.5 | S08 | hữu hệ thống thông gió đối lưu tự nhiên |  |
| s09 | 00:27.1 | S09 | giữ nhiệt độ luôn ổn định ở 25°C C mà không tốn một giọt điện năng! |  |
| s10 | 00:32.1 | S10 | Thậm chí trên mai kiến còn có vi khuẩn tiết ra thuốc kháng sinh tự |  |
| s11 | 00:35.9 | S11 | nhiên để bảo vệ mùa màng! Một siêu đô thị ngầm 50 triệu dân vận hành bền vững suốt 50 triệu năm qua! |  |
| s12 | 00:42.4 | S12 | Đúng là bậc thầy công trình vĩ đại nhất của tự nhiên! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chào mừng toàn thể các kỹ sư công trình ngầm, các kiến trúc sư đô thị và những người đam mê khoa học sinh thái bước vào đại công trường kỳ vĩ nhất hành tinh! Hôm nay,". Bố cục: Phòng thiết kế kỹ thuật sinh học: chú kiến cắt lá hoạt hình thông minh đội mũ kỹ sư công trình màu cam, mang kính bảo hộ lao động, hai chiếc hàm răng cưa titan sáng bóng, vác trên lưng chiếc thước kẻ kỹ thuật; tranh vẽ 2D comic công trình ngầm nguyên bản đứng bên bàn vẽ CAD blueprint trải dài, tay cầm bút chỉ vào mặt cắt lòng đất.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "phòng thiết kế kỹ thuật sinh học của chúng tôi xin trân trọng giải mã một kỳ quan xây dựng vĩ đại nằm ẩn sâu dưới lòng thảm rừng nhiệt đới Amazon, nơi cư ngụ của một đế chế tí hon với tài năng quy hoạch đô thị vượt xa trí tưởng tượng của con người!". Bố cục: Toàn cảnh rừng mưa nhiệt đới Amazon bạt ngàn với những tán cây cổ thụ khổng lồ vươn lên mây trời. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy quan sát mặt cắt bản vẽ kỹ thuật địa chất: Bên dưới một diện tích mặt đất rộng tới 50m² là cả một thành phố ngầm khổng lồ". Bố cục: Mặt cắt địa chất 3D bóc tách từng lớp đất từ bề mặt thảm thực vật xuống tận độ sâu 8m dưới lòng đất. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "ăn sâu 8m xuống lòng đất! Để xây dựng nên đô thị này, hàng triệu cư dân tí hon đã đào bới và". Bố cục: Thước đo độ sâu thẳng đứng cắm mốc 8m: Hệ thống buồng ngầm đa tầng quy mô đồ sộ như tòa nhà chọc trời đảo ngược. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "vận chuyển hơn 40 tấn đất đá lên bề mặt, tương đương với việc con người". Bố cục: Núi đất đá 40 tấn khổng lồ trên mặt đất do hàng triệu chú kiến thợ vận chuyển từng viên đất nhỏ bé. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "xây dựng đại kim tự tháp Giza bằng xẻng cầm tay!". Bố cục: Hình ảnh so sánh đối chiếu: Đại kim tự tháp Ai Cập bằng đá sừng sững bên cạnh công trình đào đất của đàn kiến. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thưa Tổng chỉ huy công trình, cảm biến địa chất xác nhận bên trong thành phố ngầm này". Bố cục: Cô trợ lý kỹ thuật đeo kính bảo hộ cầm máy quét siêu âm địa chấn báo cáo thông số cấu trúc ngầm. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "có tới hơn 1.000 căn phòng chuyên dụng kết nối với nhau bằng mạng lưới đường hầm thông gió hoàn hảo! Một thông số kiến trúc gây choáng váng thưa trợ lý giám sát!". Bố cục: Sơ đồ mạng lưới 1.000 căn phòng chức năng: Phòng ấp trứng, phòng nuôi nấm, phòng kiến chúa và bãi rác ngầm. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Những công trình sư tài ba kiến tạo nên kiệt tác này mang tên khoa học Atta cephalotes, hay còn gọi là loài Kiến Cắt Lá, nhưng toàn bộ giới xây dựng thế giới đều nghiêng mình thán phục". Bố cục: chú kiến cắt lá hoạt hình thông minh đội mũ kỹ sư công trình màu cam, mang kính bảo hộ lao động, hai chiếc hàm răng cưa titan sáng bóng, vác trên lưng chiếc thước kẻ kỹ thuật; tranh vẽ 2D comic công trình ngầm nguyên bản nở nụ cười tự hào, hai hàm răng cưa lấp lánh phản chiếu ánh đèn công trường kỹ thuật.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "gọi chúng bằng danh hiệu: Đại Công Trình Sư Ngầm! Trong khi loài người mới chỉ phát minh ra nền nông nghiệp cách đây khoảng 10.000 năm, thì loài kiến này đã". Bố cục: Biểu tượng danh hiệu vàng rực: Đại Công Trình Sư Ngầm — Danh hiệu kiến trúc sư tối cao của thế giới tự nhiên.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "thành lập những trang trại trồng nấm quy mô công nghiệp từ 50 triệu năm trước! Lá cây mà chúng rầm rộ cắt xẻ và gánh vác ngày đêm trên lưng hoàn toàn không phải để ăn, mà là nguồn nguyên liệu phân bón thượng hạng để". Bố cục: Dòng thời gian so sánh: Loài người làm nông 10.000 năm đối chiếu với kiến cắt lá làm nông 50 triệu năm trước. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nuôi dưỡng những vườn nấm khổng lồ dưới lòng đất! Bí mật cơ khí và tổ chức nào đã giúp chúng vận hành cỗ máy nông nghiệp vĩ đại này? Xin mời quý vị cùng tôi mở bản vẽ kỹ thuật tầng một để giải mã lưỡi cưa sinh học đầu tiên!". Bố cục: chú kiến cắt lá hoạt hình thông minh đội mũ kỹ sư công trình màu cam, mang kính bảo hộ lao động, hai chiếc hàm răng cưa titan sáng bóng, vác trên lưng chiếc thước kẻ kỹ thuật; tranh vẽ 2D comic công trình ngầm nguyên bản gánh mảnh lá xanh khổng lồ hình bán nguyệt trên lưng, chuẩn bị mở ra bản vẽ lưỡi cưa sinh học.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Xin mời các kỹ sư cơ khí hãy zoom cận cảnh vào công cụ lao động tiền tuyến của những người thợ khai thác gỗ: Cặp hàm răng cưa thần kỳ!". Bố cục: Bản vẽ cơ khí bóc tách: Cận cảnh cặp hàm răng cưa của kiến thợ được phóng to dưới kính hiển vi điện tử. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hàm của kiến thợ cắt lá được gia cố bằng các nguyên tử kẽm và mangan siêu cứng, biến các răng cưa ở rìa hàm sắc bén và bền bỉ". Bố cục: Mạng lưới tinh thể nguyên tử kẽm và mangan gia cố liên kết kim loại sinh học ở rìa răng cưa. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "ngang ngửa với lưỡi dao phẫu thuật bằng hợp kim titan! Nhưng điều làm nên sự kinh ngạc tột độ chính là". Bố cục: So sánh độ cứng: Răng cưa kiến thợ cắt ngọt qua kim loại thử nghiệm sắc lẹm như dao mổ titan. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "cơ chế rung tần số cao: Khi cắn vào phiến lá cây dày cộm, phần bụng của chú kiến sẽ rung lắc liên hồi với". Bố cục: chú kiến cắt lá hoạt hình thông minh đội mũ kỹ sư công trình màu cam, mang kính bảo hộ lao động, hai chiếc hàm răng cưa titan sáng bóng, vác trên lưng chiếc thước kẻ kỹ thuật; tranh vẽ 2D comic công trình ngầm nguyên bản kích hoạt cơ chế rung bụng, các sóng dao động siêu âm lan tỏa dọc sống lưng xuống hàm.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tần số lên tới 1.000 lần mỗi giây! Dao động rung này truyền thẳng xuống cặp hàm, biến nó thành một chiếc máy cưa rung siêu âm, giúp". Bố cục: Máy đo tần số hiển thị con số 1.000 Hz: Dao cắt siêu âm xẻ từng thớ lá dai nhách không tì vết. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "xẻ ngọt phiến lá dai nhách chỉ trong vòng chưa đầy 30 giây mà không tốn chút sức lực nào!". Bố cục: Đồng hồ bấm giờ 30 giây: Một mảnh lá tròn hoàn hảo rơi ra sau một đường cắt sắc lẹm hình cung. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thưa Chỉ huy, có phải mỗi mảnh lá cây được cắt ra nặng gấp nhiều lần trọng lượng cơ thể của chú kiến thợ không ạ? Chính xác tuyệt đối! Một chú kiến thợ chỉ nặng vài mi-li-gam nhưng có thể". Bố cục: Cô trợ lý kỹ thuật trầm trồ chỉ vào chiếc cân tiểu ly đo đạc trọng lượng mảnh lá cây. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "ngoạm chặt một mảnh lá nặng gấp 20 lần trọng lượng cơ thể mình, sau đó vác hiên ngang trên lưng chạy nước rút suốt quãng đường hàng trăm mét trở về tổ!". Bố cục: Hình ảnh minh họa: Lực sĩ con người gánh chiếc xe hơi 2 tấn trên vai chạy nước rút trên đường đua. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tương đương với việc một người lực sĩ gánh một chiếc xe hơi trên vai chạy cự ly marathon! Khi hàng triệu chú kiến cùng rầm rộ khuân vác lá cây trên những con đường cao tốc thông thoáng được dọn sạch chướng ngại vật, chúng tạo nên một". Bố cục: chú kiến cắt lá hoạt hình thông minh đội mũ kỹ sư công trình màu cam, mang kính bảo hộ lao động, hai chiếc hàm răng cưa titan sáng bóng, vác trên lưng chiếc thước kẻ kỹ thuật; tranh vẽ 2D comic công trình ngầm nguyên bản gánh mảnh lá nặng gấp 20 lần cơ thể phi như bay trên cành cây với nụ cười sảng khoái.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "cảnh tượng kỳ vĩ tựa như một dòng sông xanh biếc đang cuồn cuộn chảy xuyên qua rừng rậm! Nhưng lá cây đem về tổ sẽ được chế biến ra sao? Mời các bạn cùng tôi bước xuống tầng hầm nông nghiệp!". Bố cục: Dòng sông lá xanh cuồn cuộn chảy: Hàng triệu phiến lá xanh di động như làn sóng xanh trên mặt đất rừng. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tốc độ hành quân của những đoàn kiến cắt lá có thể đạt tới 15m mỗi phút! Để tối ưu hóa năng suất vận chuyển, các kiến thợ công binh đi trước sẽ dùng hàm dọn sạch mọi chướng ngại vật, tạo nên những". Bố cục: Đồng hồ đo tốc độ hành quân 15m/phút: Đội hình quân binh kiến di chuyển thẳng tắp theo trật tự hoàn hảo. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "xa lộ liên tỉnh bằng phẳng rộng tới 30 xăng-ti-mét kéo dài bất tận xuyên qua bụi rậm nhiệt đới!". Bố cục: Xa lộ cao tốc rừng rậm rộng 30cm được các kỹ sư dọn sạch sỏi đá, phẳng phiu như đường băng cao tốc. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bước vào các khoang hầm trung tâm sâu dưới lòng đất, chúng ta sẽ được chiêm ngưỡng những vườn nấm màu trắng ngà xốp như bọt biển: Đây chính là nguồn lương thực duy nhất nuôi sống toàn bộ hàng triệu cư dân của Đại Công Trình Sư Ngầm!". Bố cục: Tầng hầm nông nghiệp ngầm: chú kiến cắt lá hoạt hình thông minh đội mũ kỹ sư công trình màu cam, mang kính bảo hộ lao động, hai chiếc hàm răng cưa titan sáng bóng, vác trên lưng chiếc thước kẻ kỹ thuật; tranh vẽ 2D comic công trình ngầm nguyên bản bước vào căn phòng nuôi nấm trắng ngà xốp như bọt biển, tay cầm kính lúp.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Loài nấm này mang tên Leucoagaricus gongylophorus, một giống nấm cộng sinh đặc biệt đã". Bố cục: Bảng phân loại sinh học: Sợi nấm Leucoagaricus gongylophorus đan xen dày đặc như tấm thảm bông tuyết. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "gắn liền với số phận loài kiến suốt 50 triệu năm qua.". Bố cục: Vòng tròn liên minh cộng sinh vĩnh cửu 50 triệu năm giữa loài kiến và vườn nấm ngầm. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Quy trình chế biến thức ăn tại đây diễn ra nghiêm ngặt như một nhà máy công nghiệp hiện đại: Những mảnh lá cây mang về sẽ được các kiến thợ nhai nát thành bột mịn, sau đó". Bố cục: Dây chuyền sản xuất công nghiệp: Kiến thợ nghiền nhỏ lá cây thành hỗn hợp bột mịn tơi xốp. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tẩm ướp các giọt enzyme tiêu hóa từ dịch ruột của kiến rồi đắp thành luống phân bón tơi xốp để cấy sợi nấm lên trên.". Bố cục: Các giọt enzyme tiêu hóa đặc hiệu được phun đều lên luống bột lá để chuẩn bị cấy sợi nấm mới. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sợi nấm sẽ tiêu hóa chất xơ cellulose cứng nhắc trong lá cây và sản sinh ra các cấu trúc phình to giàu protein và đường gọi là gongylidia.". Bố cục: Cấu trúc hiển vi: Sợi nấm phân giải cellulose cứng và hình thành những bọc tròn gongylidia giàu dưỡng chất. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Những viên nang dinh dưỡng này chính là món ăn thượng hạng bồi bổ cho ấu trùng kiến và kiến chúa!". Bố cục: Kiến thợ cẩn thận mớm những viên nang gongylidia béo ngậy cho các ấu trùng kiến non và kiến chúa. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Loài nấm này phụ thuộc hoàn toàn vào kiến để được chăm sóc và diệt cỏ dại, còn loài kiến phụ thuộc hoàn toàn vào nấm để có thức ăn. Một liên minh sinh học bền chặt trường tồn qua hàng triệu năm thăng trầm của lịch sử Trái Đất!". Bố cục: chú kiến cắt lá hoạt hình thông minh đội mũ kỹ sư công trình màu cam, mang kính bảo hộ lao động, hai chiếc hàm răng cưa titan sáng bóng, vác trên lưng chiếc thước kẻ kỹ thuật; tranh vẽ 2D comic công trình ngầm nguyên bản ân cần dùng râu chải chuốt và dọn dẹp các sợi nấm già cỗi, biểu tượng người làm vườn tận tụy.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng để duy trì một vườn nấm khổng lồ dưới lòng đất sâu tăm tối và ngột ngạt, làm thế nào để hàng ngàn tấn nấm không bị ngạt khí cacbonic hay chết vì nấm mốc dịch bệnh? Xin mời các bạn cùng tôi khám phá hệ thống điều hòa nhiệt độ đỉnh cao!". Bố cục: Khói khí cacbonic tích tụ trong hầm sâu tăm tối, đặt ra bài toán thông gió sinh tử cho cả tổ kiến. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ước tính mỗi tổ kiến cắt lá tiêu thụ lượng lá cây tương đương với lượng cỏ mà một con bò trưởng thành ăn trong suốt cả năm! Nhưng chúng". Bố cục: Hình ảnh so sánh: Đàn kiến tiêu thụ lá cây tương đương một chú bò sữa ăn cỏ cả năm. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "không bao giờ tàn sát một cái cây duy nhất đến cạn kiệt, mà luôn luân phiên thu hoạch lá từ hàng chục loài cây khác nhau để bảo tồn sự đa dạng sinh học và". Bố cục: Bản đồ luân chuyển thu hoạch: Đàn kiến chia tuyến khai thác luân phiên nhiều cây rừng để bảo vệ thảm thực vật. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tránh tích tụ độc tố thực vật trong trang trại nấm ngầm!". Bố cục: chú kiến cắt lá hoạt hình thông minh đội mũ kỹ sư công trình màu cam, mang kính bảo hộ lao động, hai chiếc hàm răng cưa titan sáng bóng, vác trên lưng chiếc thước kẻ kỹ thuật; tranh vẽ 2D comic công trình ngầm nguyên bản kiểm tra kỹ từng mẫu lá đưa vào kho, đảm bảo chất lượng phân bón tinh khiết nhất.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đây chính là đỉnh cao cơ điện công trình khiến các kỹ sư nhân loại phải ngả mũ bái phục: Hệ thống điều hòa không khí tự nhiên hoàn toàn không sử dụng điện năng!". Bố cục: Phòng điều hành khí động học: chú kiến cắt lá hoạt hình thông minh đội mũ kỹ sư công trình màu cam, mang kính bảo hộ lao động, hai chiếc hàm răng cưa titan sáng bóng, vác trên lưng chiếc thước kẻ kỹ thuật; tranh vẽ 2D comic công trình ngầm nguyên bản đứng bên mô hình các giếng thông gió đối lưu tự nhiên không dùng điện.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vườn nấm ngầm đòi hỏi một môi trường cực kỳ khắt khe: Nhiệt độ phải luôn duy trì ổn định ở mức 25°C C và độ ẩm phải đạt 90%,". Bố cục: Biểu đồ tiêu chuẩn môi trường: Nhiệt độ 25°C và độ ẩm 90% rực sáng trong khung cảnh hầm ngầm. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bất kể bên ngoài mặt đất đang là nắng hạn bỏng rát hay mưa bão ngập lụt! Để đạt được sự cân bằng vi khí hậu kỳ diệu này, Đại Công Trình Sư Ngầm đã". Bố cục: Đối lập thời tiết: Mặt đất nắng cháy gay gắt hoặc bão giông nhưng dưới hầm nấm vẫn mát mẻ êm dịu. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "đào đục hàng ngàn giếng thông gió thẳng đứng nối từ các phòng nuôi nấm lên mặt đất. Các giếng ở trung tâm tổ được thiết kế nhô cao hơn và đón gió nhiều hơn, tạo ra". Bố cục: Hệ thống giếng đứng vươn lên mặt đất: Giếng trung tâm cao nhô lên như ống khói nhà máy đón gió lộng. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "sự chênh lệch áp suất khí quyển mạnh mẽ!". Bố cục: Mũi tên chênh lệch áp suất: Áp suất thấp ở miệng giếng cao hút mạnh không khí từ dưới đáy hầm. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hiệu ứng ống khói đối lưu nhiệt tự động hút không khí nóng ẩm chứa đầy khí cacbonic độc hại từ đáy tổ đẩy ra ngoài qua các lỗ trung tâm, đồng thời hút luồng không khí tươi mát giàu oxy từ các giếng thông gió ngoại vi chìm sâu xuống đáy tổ, làm mát toàn bộ hệ thống!". Bố cục: Dòng khí nóng chứa CO2 màu đỏ bốc lên giếng trung tâm, dòng khí tươi mát giàu O2 màu xanh tràn xuống giếng biên. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi nhiệt độ thay đổi, hàng vạn kiến thợ sẽ hối hả chạy đến các cửa giếng để mở rộng hoặc đắp đất bịt bớt miệng giếng lại, điều tiết lưu lượng gió chính xác đến từng mi-li-mét khối!". Bố cục: Đội cơ động kiến thợ khiêng các hòn đất nhỏ chạy đến miệng giếng để đắp thêm hoặc mở rộng van gió. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhiều tòa nhà chọc trời tiết kiệm năng lượng hiện đại ngày nay, tiêu biểu như trung tâm Eastgate tại Zimbabwe, đã mô phỏng trực tiếp nguyên lý thông gió của tổ kiến cắt lá để". Bố cục: Tòa nhà chọc trời Eastgate tại Zimbabwe với kiến trúc ống khói phỏng sinh học mô phỏng tổ kiến. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "giảm 90% chi phí điện máy lạnh! Một công nghệ thông gió thụ động siêu việt!". Bố cục: Biểu đồ tiết kiệm năng lượng 90%: Hệ thống xanh bền vững lấy cảm hứng từ Đại Công Trình Sư Ngầm. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và để bảo vệ kỳ quan đô thị này trước sự xâm lăng của kẻ thù và nấm mốc ký sinh, kiến cắt lá còn sở hữu một lực lượng vũ trang và y tế chuyên môn hóa đến mức phi thường!". Bố cục: chú kiến cắt lá hoạt hình thông minh đội mũ kỹ sư công trình màu cam, mang kính bảo hộ lao động, hai chiếc hàm răng cưa titan sáng bóng, vác trên lưng chiếc thước kẻ kỹ thuật; tranh vẽ 2D comic công trình ngầm nguyên bản đứng bên cạnh chú kiến lính hộ vệ khổng lồ bọc thép uy nghi bảo vệ cửa tổ.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ngay cả trong những trận mưa lũ nhiệt đới xối xả ngập úng mặt đất, cấu trúc miệng giếng thông gió hình phễu ngược và mạng lưới cống thoát nước ngầm vẫn ngăn không cho một giọt nước nào chảy tràn vào các buồng nấm trung tâm!". Bố cục: Mưa lũ nhiệt đới xối xả trên mặt đất nhưng các miệng giếng phễu ngược ngăn nước tuyệt đối. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một bản lĩnh thiết kế thủy lợi và địa kỹ thuật khiến mọi công trình sư hiện đại phải kinh ngạc thán phục!". Bố cục: Mạng lưới cống rãnh ngầm dẫn nước mưa thừa thoát xa khỏi các khoang nuôi nấm trọng yếu. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy quan sát sự phân tầng xã hội tinh vi trong tổ kiến:". Bố cục: Khu căn cứ thế giới tự nhiên và y tế: chú kiến cắt lá hoạt hình thông minh đội mũ kỹ sư công trình màu cam, mang kính bảo hộ lao động, hai chiếc hàm răng cưa titan sáng bóng, vác trên lưng chiếc thước kẻ kỹ thuật; tranh vẽ 2D comic công trình ngầm nguyên bản đứng trước bảng phân cấp xã hội 4 tầng lớp kiến chuyên môn hóa.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chẳng có một xã hội động vật nào trên Trái Đất có sự phân hóa hình thể và chức năng chuyên môn sâu sắc như loài kiến cắt lá! Trong tổ có tới bốn đẳng cấp kiến khác nhau cùng chung sống hòa thuận:". Bố cục: Bốn đẳng cấp kiến xếp hàng theo kích thước: Kiến lính khổng lồ, kiến thợ lớn, kiến thợ nhỏ và kiến y tế tí hon. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ở vị trí quân đội thường trực là những chú kiến lính khổng lồ nặng gấp 300 lần kiến thợ nhỏ! Chúng sở hữu hộp sọ bọc thép khổng lồ chứa đầy cơ hàm cuồn cuộn, với cặp hàm sắc bén như chiếc kìm bấm có thể". Bố cục: Kiến lính bọc thép khổng lồ to gấp 300 lần kiến nhỏ, cơ hàm nở rộng như chiếc kìm bấm titan sắc bén. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "cắn thủng lớp da giày của con người và sẵn sàng hiến dâng tính mạng để chặn đứng những con thú ăn kiến đói khát!". Bố cục: Kiến lính dũng mãnh ngoạm chặt xua đuổi con thú ăn kiến khổng lồ để bảo vệ cửa hầm tổ. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ngược lại, ở vị trí chăm sóc y tế là những chú kiến siêu tí hon chỉ nhỏ bằng đầu tăm. Chúng thường cưỡi ngay trên phiến lá mà các chú kiến thợ đang vác để làm vệ sinh, liên tục". Bố cục: Chú kiến siêu tí hon bằng đầu tăm cưỡi trên phiến lá, cầm chổi mini quét sạch bụi bẩn trên lá. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "xua đuổi những con ruồi ký sinh phorid nguy hiểm muốn đẻ trứng lên đầu đồng đội! Đặc biệt nhất,". Bố cục: Kiến tí hon dũng cảm vung râu xua đuổi con ruồi ký sinh phorid đang lượn lờ muốn đẻ trứng. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "trên lớp vỏ mai của kiến thợ có một lớp phấn trắng mờ: Đó chính là quần thể vi khuẩn Pseudonocardia cộng sinh, một". Bố cục: Cận cảnh vỏ mai kiến thợ phủ lớp phấn trắng vi khuẩn Pseudonocardia phát sáng lung linh. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nhà máy sản xuất thuốc kháng sinh tự nhiên! Loại kháng sinh này". Bố cục: Các phân tử kháng sinh tự nhiên tiêu diệt tận gốc mầm nấm mốc ký sinh độc hại Escovopsis. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L57</summary>

```text
HÌNH L57 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tiêu diệt đặc hiệu các loài nấm mốc ký sinh độc hại mang tên Escovopsis,". Bố cục: Vườn nấm sạch bong vô trùng tuyệt đối, minh chứng cho nền y tế dự phòng 50 triệu năm không lờn thuốc. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L58</summary>

```text
HÌNH L58 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "giữ cho trang trại nấm ngầm luôn vô trùng tuyệt đối suốt 50 triệu năm mà không hề bị lờn thuốc!". Bố cục: chú kiến cắt lá hoạt hình thông minh đội mũ kỹ sư công trình màu cam, mang kính bảo hộ lao động, hai chiếc hàm răng cưa titan sáng bóng, vác trên lưng chiếc thước kẻ kỹ thuật; tranh vẽ 2D comic công trình ngầm nguyên bản chào quân hàm cùng đội quân kiến lính và đội ngũ y tế tí hon tận tụy.
```
</details>

<details><summary>L59</summary>

```text
HÌNH L59 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một hệ thống y tế và an ninh quốc phòng hoàn hảo đến từng mi-crô-mét,". Bố cục: Đế chế ngầm phồn vinh rực rỡ với hàng ngàn ánh đèn công trường hoạt động ngày đêm nhộn nhịp. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L60</summary>

```text
HÌNH L60 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bảo vệ sự phồn vinh của đế chế ngầm qua muôn vàn thử thách khắc nghiệt của mẹ thiên nhiên!". Bố cục: Tổ kiến vững vàng trước mọi biến động thời tiết, sừng sững tồn tại qua hàng triệu năm lịch sử. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L61</summary>

```text
HÌNH L61 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thưa toàn thể hội đồng thẩm định kiến trúc và quý khán giả theo dõi công trình, sau khi khảo sát chi tiết toàn bộ năm bản vẽ từ đại công trường ngầm 8m, cặp hàm cưa rung siêu âm,". Bố cục: Hội đồng thẩm định kiến trúc tự nhiên: chú kiến cắt lá hoạt hình thông minh đội mũ kỹ sư công trình màu cam, mang kính bảo hộ lao động, hai chiếc hàm răng cưa titan sáng bóng, vác trên lưng chiếc thước kẻ kỹ thuật; tranh vẽ 2D comic công trình ngầm nguyên bản đứng trên bục vinh danh đón nhận Bằng Chứng Nhận Kỳ Quan Kiến Trúc.
```
</details>

<details><summary>L62</summary>

```text
HÌNH L62 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "vườn nấm nông nghiệp 50 triệu năm, hệ thống thông gió đối lưu 25°C cho đến quân đoàn kiến lính và kháng sinh sống, hội đồng nhất trí tuyệt đối trao Chứng nhận Kỳ Quan Kiến Trúc Tự Nhiên cho Kiến Cắt Lá! Đại Công Trình Sư Ngầm chính là". Bố cục: Năm biểu tượng bản vẽ kỹ thuật: Hầm ngầm 8m, hàm cưa siêu âm, vườn nấm 50 triệu năm, thông gió đối lưu và kháng sinh. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L63</summary>

```text
HÌNH L63 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "hình mẫu kiểu mẫu về nền kinh tế tuần hoàn và phát triển bền vững không rác thải. Toàn bộ chất thải từ vườn nấm ngầm đều được đưa vào các khoang rác thải hữu cơ sâu dưới đáy tổ để tái chế và nuôi dưỡng đất rừng nhiệt đới,". Bố cục: Sơ đồ kinh tế tuần hoàn khép kín: Toàn bộ chất thải được phân hủy tái chế làm màu mỡ đất rừng. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L64</summary>

```text
HÌNH L64 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tạo nên thảm thực vật xanh tươi màu mỡ bậc nhất hành tinh.". Bố cục: Rừng rậm nhiệt đới tươi tốt ngút ngàn nhờ công lao cải tạo đất của hàng triệu đàn kiến ngầm. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L65</summary>

```text
HÌNH L65 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bài học từ loài kiến nhỏ bé nhắc nhở nhân loại chúng ta rằng: Khi hàng triệu cá nhân cùng chung sức đồng lòng, hướng về một mục tiêu chung với". Bố cục: chú kiến cắt lá hoạt hình thông minh đội mũ kỹ sư công trình màu cam, mang kính bảo hộ lao động, hai chiếc hàm răng cưa titan sáng bóng, vác trên lưng chiếc thước kẻ kỹ thuật; tranh vẽ 2D comic công trình ngầm nguyên bản bắt tay cùng người kỹ sư nhân loại, biểu tượng kết nối giữa thiên nhiên và công nghệ.
```
</details>

<details><summary>L66</summary>

```text
HÌNH L66 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tinh thần kỷ luật và sự phân công lao động khoa học, những sinh vật nhỏ bé nhất cũng có thể tạo nên những kỳ tích dời non lấp bể vĩ đại!". Bố cục: Hàng triệu cánh tay kiến và con người cùng chung sức dựng xây những công trình vĩ đại dời non lấp bể. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L67</summary>

```text
HÌNH L67 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giữa hệ thống điều hòa thông gió đối lưu tự nhiên và kỹ thuật nuôi nấm bằng lưỡi cưa rung siêu âm, kỳ quan nào của Kiến Cắt Lá khiến bạn thán phục và truyền cảm hứng nhiều nhất?". Bố cục: Hai màn hình đối chiếu: Giếng thông gió ống khói không điện và hàm răng cưa rung tần số cao. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L68</summary>

```text
HÌNH L68 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy để lại ý kiến đóng góp của bạn ngay trong phần bình luận bên dưới nhé! Và đừng quên". Bố cục: Biểu tượng ô bình luận ý kiến cùng cộng đồng các nhà khoa học và kỹ sư trẻ nhiệt huyết. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L69</summary>

```text
HÌNH L69 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nhấn nút Đăng Ký Kênh cùng chiếc chuông thông báo để cùng đồng hành trong chuỗi tập tiếp theo của thế giới tự nhiên kỳ thú!". Bố cục: Nút Đăng Ký Kênh rực sáng cùng chiếc chuông thông báo rung động mời gọi khám phá. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>L70</summary>

```text
HÌNH L70 (16:9 ngang, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Xin chào tạm biệt và hẹn gặp lại toàn thể các bạn trên những công trình vĩ đại tiếp theo!". Bố cục: chú kiến cắt lá hoạt hình thông minh đội mũ kỹ sư công trình màu cam, mang kính bảo hộ lao động, hai chiếc hàm răng cưa titan sáng bóng, vác trên lưng chiếc thước kẻ kỹ thuật; tranh vẽ 2D comic công trình ngầm nguyên bản vẫy tay chào tạm biệt khán giả từ cửa công trình ngầm, hẹn gặp lại ở những hành trình tiếp theo.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Bạn có tin loài người không phải là sinh vật đầu tiên phát minh ra nông nghiệp trên Trái Đất không?". Bố cục: Khung cảnh mở đầu đại công trường: chú kiến cắt lá hoạt hình thông minh đội mũ kỹ sư công trình màu cam, mang kính bảo hộ lao động, hai chiếc hàm răng cưa titan sáng bóng, vác trên lưng chiếc thước kẻ kỹ thuật; tranh vẽ 2D comic công trình ngầm nguyên bản đứng trên bản vẽ mặt cắt địa tầng ngầm, tay cầm thước đo chỉ vào độ sâu tám mét.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Trước khi con người xuất hiện hàng chục triệu năm, loài Kiến Cắt Lá đã xây dựng những trang trại trồng nấm". Bố cục: Bản vẽ lịch sử Trái Đất: Dòng thời gian 50 triệu năm trước với biểu tượng vườn nấm ngầm rực rỡ dưới chân khủng long. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "quy mô công nghiệp sâu 8m dưới lòng đất!". Bố cục: Mặt cắt đứng thành phố ngầm sâu 8m với hàng ngàn phòng chức năng kết nối chằng chịt như mạng lưới tàu điện ngầm. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Bí mật kinh hoàng nằm ở chỗ:". Bố cục: chú kiến cắt lá hoạt hình thông minh đội mũ kỹ sư công trình màu cam, mang kính bảo hộ lao động, hai chiếc hàm răng cưa titan sáng bóng, vác trên lưng chiếc thước kẻ kỹ thuật; tranh vẽ 2D comic công trình ngầm nguyên bản lắc ngón tay chỉ vào chiếc lá cây xanh mướt trên lưng, nụ cười bí ẩn của vị tổng công trình sư.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Chúng cắt lá cây không phải để ăn, mà dùng hàm rung siêu âm". Bố cục: Cận cảnh hàm răng cưa rung tần số cao xẻ ngọt phiến lá thành bột mịn rơi xuống luống phân bón hữu cơ. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "như máy cưa xẻ nát lá làm phân bón nuôi nấm!". Bố cục: Nhà máy chế biến sinh học: Kiến thợ nhào trộn bột lá với enzyme dịch ruột để nuôi sợi nấm trắng tinh khiết. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Tổ của chúng đào bới hơn 40 tấn đất đá, sở hữu". Bố cục: Đại kim tự tháp Giza đặt cạnh núi đất 40 tấn do đàn kiến tí hon đào bới vận chuyển lên mặt đất. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "hệ thống thông gió đối lưu tự nhiên". Bố cục: Sơ đồ khí động học: Luồng khí nóng màu đỏ thoát ra giếng trung tâm, luồng khí mát màu xanh tràn vào giếng ngoại vi. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>S09</summary>

```text
HÌNH S09 (DỌC 9:16, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "giữ nhiệt độ luôn ổn định ở 25°C C mà không tốn một giọt điện năng!". Bố cục: Đồng hồ nhiệt độ điện tử cố định ở 25°C và độ ẩm 90% hoàn hảo giữa thời tiết nhiệt đới khắc nghiệt. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>S10</summary>

```text
HÌNH S10 (DỌC 9:16, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Thậm chí trên mai kiến còn có vi khuẩn tiết ra thuốc kháng sinh tự nhiên". Bố cục: Kính hiển vi phóng to lớp phấn trắng trên mai kiến thợ: Vi khuẩn tiết thuốc kháng sinh tiêu diệt nấm mốc dịch bệnh. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>S11</summary>

```text
HÌNH S11 (DỌC 9:16, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "để bảo vệ mùa màng! Một siêu đô thị ngầm 50 triệu dân vận hành bền vững suốt 50 triệu năm qua!". Bố cục: Trang trại nấm trắng ngà bồng bềnh sạch bóng mầm bệnh, biểu tượng mùa màng bội thu vô trùng 50 triệu năm. KHÔNG có chú kiến cắt lá đội mũ kỹ sư công trình trong cảnh này.
```
</details>

<details><summary>S12</summary>

```text
HÌNH S12 (DỌC 9:16, phong cách mặt cắt kiến trúc địa tầng ngầm đại công trình (Subterranean Architectural Cross-Section) và nhân vật chú kiến cắt lá đội mũ kỹ sư công trình và đeo kính bảo hộ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Đúng là bậc thầy công trình vĩ đại nhất của tự nhiên!". Bố cục: chú kiến cắt lá hoạt hình thông minh đội mũ kỹ sư công trình màu cam, mang kính bảo hộ lao động, hai chiếc hàm răng cưa titan sáng bóng, vác trên lưng chiếc thước kẻ kỹ thuật; tranh vẽ 2D comic công trình ngầm nguyên bản hiên ngang đứng trên đỉnh công trình ngầm, giương cao tấm huy chương vàng Kiến Trúc Sư Vĩ Đại Của Thiên Nhiên.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/70 của video YouTube về Kiến Cắt Lá). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách mặt cắt kiến trúc địa tầng công trình ngầm đại quy mô (Subterranean Architectural Cross-Section & Industrial CAD Blueprint): bản vẽ mặt cắt các tầng đất sâu 8m với độ chuẩn xác kiến trúc cao, sơ đồ luồng khí thông gió đối lưu khí động học, đường ống luân chuyển hữu cơ sinh thái, nét vẽ kỹ thuật kiến trúc sắc bén, bảng đo đạc tỷ lệ công trình, phối màu xanh lục bảo thực vật, nâu đất phù sa và đường lưới kỹ thuật xanh cyan blueprint; NỀN TRẮNG TINH hoàn toàn, không watermark, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú kiến cắt lá hoạt hình thông minh đội mũ kỹ sư công trình màu cam, mang kính bảo hộ lao động, hai chiếc hàm răng cưa titan sáng bóng, vác trên lưng chiếc thước kẻ kỹ thuật; tranh vẽ 2D comic công trình ngầm nguyên bản. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/12 của video YouTube Shorts về Kiến Cắt Lá). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách mặt cắt kiến trúc địa tầng công trình ngầm đại quy mô (Subterranean Architectural Cross-Section & Industrial CAD Blueprint): bản vẽ mặt cắt các tầng đất sâu 8m với độ chuẩn xác kiến trúc cao, sơ đồ luồng khí thông gió đối lưu khí động học, đường ống luân chuyển hữu cơ sinh thái, nét vẽ kỹ thuật kiến trúc sắc bén, bảng đo đạc tỷ lệ công trình, phối màu xanh lục bảo thực vật, nâu đất phù sa và đường lưới kỹ thuật xanh cyan blueprint; NỀN TRẮNG TINH hoàn toàn, không watermark, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú kiến cắt lá hoạt hình thông minh đội mũ kỹ sư công trình màu cam, mang kính bảo hộ lao động, hai chiếc hàm răng cưa titan sáng bóng, vác trên lưng chiếc thước kẻ kỹ thuật; tranh vẽ 2D comic công trình ngầm nguyên bản. 
```
</details>

## 7. SEO

- **title:** Đại Công Trình Ngầm: Kiến Cắt Lá Xây Đô Thị 50 Triệu Dân Với Điều Hòa Tự Nhiên?! | Tập 40
- **hook_paragraph:** Kiến Cắt Lá (Atta cephalotes) không ăn lá cây! Chúng cắt hàng tấn lá rừng Amazon mỗi năm để làm nguyên liệu nuôi trồng nấm ngầm trong một thành phố sâu 8 mét dưới lòng đất với 50 triệu cư dân. Hệ thống điều hòa nhiệt độ không dùng điện và phòng thí nghiệm kháng sinh tự nhiên của chúng hoạt động thế nào? Cùng Kỹ sư trưởng khám phá!
- **question:** Giữa hệ thống điều hòa đối lưu không dùng điện và cặp hàm cắt lá rung tần số 1.000 Hz, kỳ quan kỹ thuật nào của Kiến Cắt Lá làm bạn thán phục nhất?
- **next_teaser:** những bí mật hoang dã chưa từng được tiết lộ trong mùa tiếp theo
- **shorts_title:** Bí mật thành phố ngầm 50 triệu dân của Kiến Cắt Lá?!
- **shorts_desc:** Kiến Cắt Lá xây dựng đô thị ngầm sâu 8m với hơn 1.000 phòng và hệ thống điều hòa tự nhiên!
- **bullets:** Cặp hàm dao cắt rung siêu âm 1.000 Hz: Nghiền nát phiến lá dai như kéo phẫu thuật laser · Thành phố ngầm sâu 8 mét: Đào bới 40 tấn đất đá tạo ra hơn 1.000 phòng chức năng kết nối ngầm · Nền nông nghiệp nấm 50 triệu năm: Trồng nấm Leucoagaricus trước khi loài người xuất hiện 50 triệu năm · Hệ thống điều hòa đối lưu không dùng điện: Lỗ thông gió trung tâm đẩy khí nóng và hút khí mát · Đội quân kiến lính bọc thép sinh học: Lớp giáp khoáng chất magnesium canxi cứng cáp chống kẻ thù · Nhà máy kháng sinh di động: Vi khuẩn trên thân kiến sản sinh hoạt chất tiêu diệt nấm mốc độc hại
- **tags:** kiến cắt lá, atta cephalotes, đại công trình ngầm, kỹ thuật sinh thái, vẽ chuyện hoang dã, whiteboard animation

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-40-kien-cat-la
python src/episode/pipeline.py tts    projects/tap-40-kien-cat-la     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-40-kien-cat-la     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-40-kien-cat-la     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-40-kien-cat-la              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-40-kien-cat-la --force
python scripts/beat_sheet.py projects/tap-40-kien-cat-la               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-40-kien-cat-la/audio/shorts.wav projects/tap-40-kien-cat-la/renders/tap-40-kien-cat-la_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-40-kien-cat-la
python src/episode/pipeline.py seo    projects/tap-40-kien-cat-la
python src/episode/episode_doc.py     projects/tap-40-kien-cat-la
```
