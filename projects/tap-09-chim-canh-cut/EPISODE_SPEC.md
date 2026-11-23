# TẬP 9 — CHIM CÁNH CỤT · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-09-chim-canh-cut`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-09-chim-canh-cut`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F3` · **Persona giọng:** `phien_toa` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Chim Cánh Cụt |
| Tiêu đề YouTube | Đẩy Bạn Xuống Biển Để Thử Hải Cẩu Báo?! \| Chim Cánh Cụt \| Tập 9 |
| Video dài | `renders/tap-09-chim-canh-cut_long.mp4` — 8:48.0 (528.0s) |
| Shorts | `renders/tap-09-chim-canh-cut_shorts.mp4` — 0:50.1 (50.1s) |
| Thumbnail | `renders/tap-09-chim-canh-cut_thumbnail.jpg` |
| Số hình | dài 87 beat / 87 ảnh riêng; Shorts 13 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.1**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/84 của video YouTube về Chim Cánh Cụt). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ. Nhân vật phụ cố định: ngài thẩm phán hải mã (walrus) già đội tóc giả trắng xoăn, cầm búa gỗ; ông công tố viên hoạt hình đeo kính tròn, mặc áo choàng đen. HÌNH L01 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nam Cực. -40°C. Gió rít qua những tảng băng trắng xóa...". Bố cục: Toàn cảnh Nam Cực trong bão tuyết: núi băng trắng xanh, gió cuốn tuyết thành vệt, bầu trời xám. BÊN PHẢI cắm một chiếc nhiệt kế khổng lồ đóng băng, cột đỏ tụt xuống tận đáy. KHÔNG có chú cánh cụt nơ đỏ trong cảnh này.
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — BỊ CÁO MẶC VEST ĐUÔI TÔM
*Badge:* `VỤ ÁN NAM CỰC` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene01_p0.wav` (314 ký tự) · mood `tram_bi_an`

```text
Nam Cực. Âm bốn mươi độ C. Gió rít qua những tảng băng trắng xóa... Một viên sỏi vừa biến mất khỏi tổ của người hàng xóm. Ở mép băng, một chú chim vừa bị đẩy rơi tõm xuống làn nước lạnh buốt. Và trên nền tuyết trắng tinh, những vệt màu hồng kéo dài như ai đó vừa nã súng sơn... Ai đứng sau tất cả những chuyện này?
```
**Part 1** → `audio/vs/scene01_p1.wav` (21 ký tự) · 🎭 cameo `tham_phan`

```text
Bị cáo, mời đứng lên!
```
**Part 2** → `audio/vs/scene01_p2.wav` (518 ký tự) · mood `hao_hung`

```text
[surprise-oh] Và bị cáo là... một chú chim cao chưa tới bảy mươi xăng-ti-mét, nặng từ ba đến sáu ki-lô-gam, tức là cỡ một con mèo nhà, đang đi lạch bạch như trẻ mẫu giáo đi học muộn! [laughter] Kính thưa bồi thẩm đoàn, đây là chim cánh cụt A-đê-li, loài cánh cụt nhỏ nhất ở Nam Cực. Lưng đen, bụng trắng, quanh mắt có một vòng trắng tròn xoe như vừa bị ai dọa giật mình. Ở tòa này, chúng tôi gọi bị cáo bằng biệt danh: Quý ông Vest Đuôi Tôm. Trông lịch lãm như đi dự tiệc cưới, nhưng hồ sơ thì dày hơn cả cuốn từ điển!
```
**Part 3** → `audio/vs/scene01_p3.wav` (270 ký tự) · mood `nghiem_trang_gia`

```text
Hôm nay, công tố viên là tôi sẽ đưa ra bốn bằng chứng. Trộm cắp tài sản. Đẩy bạn vào chỗ nguy hiểm. Tấn công bằng vũ khí sinh học tầm xa. Và hành hung cả nhà khoa học! Còn bồi thẩm đoàn, tức là các bạn, sẽ tự quyết định: một kẻ đáng yêu như thế này... có thật sự có tội?
```

### scene02 — KẺ TRỘM SỎI XỨ BĂNG
*Thẻ chương:* TRỘM SỎI NHÀ HÀNG XÓM ĐỂ XÂY TỔ

*Badge:* `BẰNG CHỨNG #1` · *mood mặc định:* `nghiem_trang_gia`

**Part 0** → `audio/vs/scene02_p0.wav` (583 ký tự)

```text
Bằng chứng số một: trộm cắp tài sản có giá trị lớn. Tài sản bị trộm là... một viên sỏi. [dissatisfaction-hnn] Vâng, bồi thẩm đoàn không nghe nhầm đâu. Một viên sỏi. Nhưng ở Nam Cực, sỏi không hề rẻ. Chỉ khoảng hai phần trăm lục địa này là không bị băng phủ. Mỗi mùa xuân, hàng triệu chú cánh cụt A-đê-li kéo nhau lên đúng những bãi đá hiếm hoi ấy để xây tổ. Và tổ của chúng không làm bằng cỏ, không làm bằng lông, mà làm bằng sỏi. Trung bình mỗi tổ cần khoảng hai trăm viên. Tức là một con chim nặng bằng con mèo phải tự tay, à không, tự mỏ, khuân hai trăm viên đá về nhà! [laughter]
```
**Part 1** → `audio/vs/scene02_p1.wav` (354 ký tự) · mood `don_dap`

```text
Và thế là tội ác bắt đầu! Hàng xóm vừa quay lưng. Quý ông Vest Đuôi Tôm rón rén bước tới. Ngoạm một viên! Quay về tổ! Đặt xuống! Lại rón rén đi tiếp! Có kẻ trộm xong còn đứng ngay sau lưng nạn nhân để chọn viên thứ hai! Nạn nhân phát hiện thì sao? Mổ! Đập cánh! Rượt đuổi vòng quanh bãi đá! Một cuộc rượt đuổi tốc độ cao... hai cây số một giờ. [laughter]
```
**Part 2** → `audio/vs/scene02_p2.wav` (620 ký tự) · mood `hao_hung`

```text
Điều buồn cười nhất là: kẻ trộm giỏi nhất lại chính là kẻ canh nhà kỹ nhất. Các nhà làm phim tài liệu đã quay được một gã vừa đi trộm khắp nơi, vừa đứng gác tổ mình như bảo vệ ngân hàng. Bởi vì gã biết rõ hơn ai hết: ở đây, ai cũng là trộm! Bồi thẩm đoàn thử tưởng tượng: cả một khu phố năm triệu dân, nhà nào cũng thiếu gạch, và ai cũng đang lén lấy gạch nhà bên cạnh. [laughter] Cứ đà này, có khi một viên sỏi đi một vòng khắp xóm rồi lại quay về đúng cái tổ ban đầu! Còn ở họ hàng nhà cánh cụt Gen-tu, chàng trai mang viên sỏi đẹp nhất tặng bạn đời như tặng nhẫn kim cương. Ở Nam Cực, không có sỏi thì đừng mơ lấy vợ!
```
**Part 3** → `audio/vs/scene02_p3.wav` (291 ký tự) · mood `hao_hung`

```text
Mà bồi thẩm đoàn biết không, nhiều chàng cánh cụt năm nào cũng quay về xây tổ đúng chỗ cũ, mong cô bạn đời năm ngoái nhận ra nhà mà quay lại. Thế nên một cái tổ đẹp vừa là ngôi nhà, vừa là... tấm biển địa chỉ! Tổ xấu quá thì sao? Cô nàng đi lướt qua luôn, coi như không quen biết! [laughter]
```
**Part 4** → `audio/vs/scene02_p4.wav` (61 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Thưa tòa, cháu không trộm! Cháu chỉ... mượn vĩnh viễn thôi ạ!
```
**Part 5** → `audio/vs/scene02_p5.wav` (235 ký tự)

```text
Bồi thẩm đoàn đã nghe rồi đấy. Mượn vĩnh viễn! [laughter] Công tố viên đề nghị ghi nhận: bị cáo có hành vi chiếm đoạt sỏi một cách có hệ thống, có tổ chức, và có cả kỹ năng nhìn trước ngó sau chuyên nghiệp. Bằng chứng số một, kết thúc.
```

### scene03 — ĐẨY BẠN XUỐNG NƯỚC DÒ HẢI CẨU
*Thẻ chương:* ĐẨY BẠN XUỐNG BIỂN ĐỂ THỬ HẢI CẨU BÁO

*Badge:* `BẰNG CHỨNG #2` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene03_p0.wav` (266 ký tự) · mood `tram_bi_an`

```text
Bằng chứng số hai. Hiện trường: mép băng, lúc chiều tà. Hàng trăm chú cánh cụt đứng chen chúc sát mép nước. Ai cũng đói. Ai cũng muốn xuống biển bắt cá và tôm nhỏ. Nhưng... không ai chịu nhảy trước. Vì sao ư? Vì dưới làn nước tối kia... có thể có thứ gì đó đang chờ.
```
**Part 1** → `audio/vs/scene03_p1.wav` (346 ký tự) · mood `don_dap`

```text
[surprise-wa] Hải cẩu báo! Dài tới ba mét rưỡi! Nặng tới năm trăm ki-lô-gam! Bơi nhanh bốn mươi cây số một giờ! Cái đầu to như đầu rắn! Hàm đầy răng nanh dài! Nó nấp ngay dưới mép băng, chỉ ló mỗi cái mũi! Chờ đúng khoảnh khắc một chú cánh cụt chạm nước! So với Quý ông Vest Đuôi Tôm nặng bằng con mèo, đây là một chiếc xe tải có răng! [laughter]
```
**Part 2** → `audio/vs/scene03_p2.wav` (438 ký tự)

```text
Và thế là cảnh tượng kỳ lạ nhất Nam Cực diễn ra. Cả bầy chen tới, chen lui, huých nhau, ủn nhau. Con đứng hàng đầu cố bám chân lại. Mấy con phía sau cứ thế mà dồn lên. Và rồi... tõm! Một bạn xui xẻo rơi xuống nước! Cả bầy lập tức nín thở, nghển cổ nhìn theo như khán giả xem phim kinh dị. Nếu bạn ấy bơi đi bình an, cả hội ào ào nhảy theo như đi tắm biển ngày hè! [laughter] Còn nếu không... thì cả bầy lùi lại, đứng chờ thêm một lúc nữa.
```
**Part 3** → `audio/vs/scene03_p3.wav` (323 ký tự) · mood `nghiem_trang_gia`

```text
Nhân chứng của vụ án này là một người rất đặc biệt. Năm một ngàn chín trăm mười một, bác sĩ Lê-vích của đoàn thám hiểm Nam Cực nước Anh đã sống gần một năm ở Kếp A-đe, ngày ngày ngồi quan sát từng chú cánh cụt A-đê-li. Ông ghi lại cảnh chúng đứng trên mép băng, né qua né lại, và cố đẩy nhau xuống nước. Xin mời nhân chứng.
```
**Part 4** → `audio/vs/scene03_p4.wav` (96 ký tự) · 🎭 cameo `ong_gia_ke`

```text
Mấy con đứng sau suýt đẩy được hàng đầu xuống nước, thế là hàng đầu vòng ra phía sau để đẩy lại!
```
**Part 5** → `audio/vs/scene03_p5.wav` (231 ký tự)

```text
Bồi thẩm đoàn nghe rõ chưa? Vòng ra phía sau để đẩy lại! [laughter] Đây không còn là đi bơi nữa, đây là trò kéo co ngược chiều! Thua thì làm vật thí nghiệm, thắng thì được đi ăn trưa an toàn. Bằng chứng số hai, cực kỳ nghiêm trọng!
```

### scene04 — KHẨU SÚNG PHÂN ÁP LỰC CAO
*Thẻ chương:* BẮN PHÂN XA 1,34 MÉT — NHÌN THẤY TỪ VŨ TRỤ

*Badge:* `BẰNG CHỨNG #3` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene04_p0.wav` (465 ký tự) · mood `nghiem_trang_gia`

```text
Bằng chứng số ba: tấn công bằng vũ khí sinh học tầm xa. [dissatisfaction-hnn] Thưa bồi thẩm đoàn, vũ khí đó... là phân. Chim cánh cụt ấp trứng nhiều ngày liền không rời tổ. Vậy nó đi vệ sinh ở đâu? Rất đơn giản. Nó đứng dậy, quay lưng ra mép tổ, nhấc đuôi lên, và... bắn! Một vệt trắng hồng phóng thẳng ra ngoài. Cứ thế, quanh mỗi cái tổ là những tia vệt tỏa ra như tia nắng mặt trời. Nhìn từ trên cao, cả bãi đá giống hệt một bức tranh vẽ bằng súng sơn! [laughter]
```
**Part 1** → `audio/vs/scene04_p1.wav` (507 ký tự)

```text
Chuyện nghe thì buồn cười, nhưng các nhà khoa học đã tính toán hẳn hoi. Năm hai ngàn lẻ ba, hai nhà khoa học đo độ dài vệt phân quanh tổ, rồi dùng công thức vật lý tính ra áp suất bên trong bụng chim cánh cụt. [surprise-ah] Kết quả: từ mười đến sáu mươi ki-lô-pát-xcan! Mạnh gấp mấy lần lúc con người đi vệ sinh, cỡ một nửa áp suất lốp xe hơi! Công trình này còn đoạt giải I-gơ Nô-ben năm hai ngàn lẻ năm, giải thưởng dành cho những nghiên cứu khiến người ta bật cười trước, rồi mới suy nghĩ sau. [laughter]
```
**Part 2** → `audio/vs/scene04_p2.wav` (401 ký tự) · mood `don_dap`

```text
Chưa hết! Năm hai ngàn hai mươi, hai nhà khoa học Nhật Bản tính lại trên loài cánh cụt Hum-bôn! Lần này tính cả góc bắn! Cả sức cản không khí! Cả độ sệt của phân! Kết quả: tầm bắn xa nhất một mét ba mươi tư! Tốc độ gần tám cây số một giờ! Nếu đổi sang cỡ người, đó là bắn xa hơn ba mét! [surprise-wa] Và họ nghiêm túc khuyên nhân viên thủy cung: hãy đứng cách xa ít nhất một mét ba mươi tư! [laughter]
```
**Part 3** → `audio/vs/scene04_p3.wav` (539 ký tự)

```text
Và vũ khí này mạnh tới mức... nhìn thấy được từ ngoài vũ trụ! Năm hai ngàn mười hai, các nhà khoa học Anh soi ảnh vệ tinh dọc bờ biển Nam Cực, tìm những mảng màu nâu trên nền băng trắng. Mảng nâu đó chính là phân chim cánh cụt! Lần theo dấu vết ấy, họ tìm ra bốn mươi sáu đàn cánh cụt hoàng đế, họ hàng to xác của bị cáo, và đếm được khoảng năm trăm chín mươi lăm ngàn con, gần gấp đôi con số người ta từng nghĩ. Bồi thẩm đoàn thấy chưa: đi đâu cũng để lại dấu vết, lộ cả trên ảnh vệ tinh! Đây là băng nhóm bất cẩn nhất lịch sử! [laughter]
```

### scene05 — CÔN ĐỒ CÁNH CỨNG TÁT CẢ NHÀ KHOA HỌC
*Thẻ chương:* TÁT CẢ NHÀ KHOA HỌC BẰNG CÁNH CỨNG

*Badge:* `BẰNG CHỨNG #4` · *mood mặc định:* `nghiem_trang_gia`

**Part 0** → `audio/vs/scene05_p0.wav` (400 ký tự)

```text
Bằng chứng số bốn: hành hung người đang làm nhiệm vụ. Nạn nhân là... các nhà khoa học. Khi nhà nghiên cứu cúi xuống gần tổ để cân chim non, Quý ông Vest Đuôi Tôm không hề bỏ chạy. Nó lao tới, đứng thẳng người, và tát! Bằng đôi cánh cứng như mái chèo! Phạch! Phạch! Phạch! [laughter] Cánh chim cánh cụt không bay được, nhưng xương cánh dẹt và đặc, quất vào ống chân thì đau như bị cô giáo gõ thước kẻ.
```
**Part 1** → `audio/vs/scene05_p1.wav` (256 ký tự) · mood `don_dap`

```text
Không chỉ con người! Chim cướp biển Xku-a sải cánh rộng hơn một mét lượn tới định cướp trứng? Tát! Hải cẩu bò lên quá gần? Tát! Hàng xóm lấn sang nửa bước? Tát luôn! Cả đời bị cáo chỉ có hai chế độ: đứng im dễ thương, và tát không cần báo trước! [laughter]
```
**Part 2** → `audio/vs/scene05_p2.wav` (321 ký tự) · mood `hao_hung`

```text
Và đừng tưởng bị cáo chậm chạp. Trên cạn, nó đi lạch bạch như ông cụ đi chợ. Nhưng xuống nước thì như tên lửa: bơi mười lăm cây số một giờ, lặn sâu tới một trăm tám mươi mét, và khi phóng lên, nó có thể bật một cú nhảy cao tới hai mét, đáp thẳng lên tảng băng! [surprise-oh] Trên bờ là diễn viên hài, dưới nước là đặc vụ!
```
**Part 3** → `audio/vs/scene05_p3.wav` (274 ký tự) · mood `don_dap`

```text
Còn khi lười đi bộ trên tuyết? Bị cáo nằm sấp xuống, lấy cái bụng làm ván trượt, hai chân đạp phía sau, lướt vèo vèo như trẻ con chơi cầu trượt! [laughter] Các nhà khoa học gọi đó là cách tiết kiệm sức. Còn tòa án gọi đó là... tẩu thoát khỏi hiện trường bằng xe trượt riêng!
```
**Part 4** → `audio/vs/scene05_p4.wav` (359 ký tự)

```text
Công tố viên xin tổng kết. Trộm sỏi. Đẩy bạn xuống nước. Nã súng phân xa một mét ba mươi tư. Và tát cả nhà khoa học! Ngay cả nhân chứng Lê-vích năm xưa cũng gọi những chú chim trẻ hay gây rối là... lũ du côn! [laughter] Ông còn viết một số trang nhật ký bằng chữ cái Hy Lạp để người khác không đọc được. Bằng chứng đã đủ. Công tố viên đề nghị mức án cao nhất!
```

### scene06 — LUẬT SƯ BÀO CHỮA & PHÁN QUYẾT
*Thẻ chương:* LUẬT SƯ LẬT NGƯỢC CẢ 4 BẰNG CHỨNG

*Badge:* `PHÁN QUYẾT` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene06_p0.wav` (510 ký tự) · mood `am_ap`

```text
Khoan đã! Phản đối! Bây giờ, xin cho tôi cởi áo công tố viên, và khoác áo luật sư bào chữa. Bởi vì bồi thẩm đoàn mới chỉ nghe một nửa câu chuyện. Về bằng chứng số một: vì sao phải trộm sỏi? Mỗi mùa xuân, tuyết tan thành những dòng nước lạnh chảy tràn qua bãi đá. Quả trứng nằm sát mặt đất sẽ bị ngâm nước, lạnh cóng, rồi hỏng. Một đống sỏi cao chính là chiếc bè cứu sinh, nâng quả trứng lên khỏi vũng nước. Tổ càng cao, trứng càng an toàn. Thứ bị cáo trộm không phải của cải, mà là... cơ hội sống cho con mình.
```
**Part 1** → `audio/vs/scene06_p1.wav` (470 ký tự) · mood `hao_hung`

```text
Về bằng chứng số hai: nhiều nhà khoa học cho rằng phần lớn những cú rơi ở mép băng không phải âm mưu gì cả. Đó chỉ là cảnh chen lấn giờ cao điểm: bầy đông dồn lên, con đứng đầu bị đẩy ra mép, và thế là tõm. Nhảy theo bầy lại là cách sống sót tốt nhất, vì một con hải cẩu báo không thể bắt hết cả trăm con cùng lúc. Về bằng chứng số ba: bắn phân ra xa là để giữ tổ khô ráo, sạch sẽ cho trứng và con non. Đó là vệ sinh cá nhân... chỉ hơi mạnh tay một chút thôi! [laughter]
```
**Part 2** → `audio/vs/scene06_p2.wav` (254 ký tự) · mood `am_ap`

```text
Còn bằng chứng số bốn, tát cả nhà khoa học? Bồi thẩm đoàn hãy nhìn kỹ: đó là một ông bố bé nhỏ, nặng bằng con mèo, dám đứng chắn trước mọi thứ to lớn hơn mình gấp nhiều lần, chỉ để bảo vệ hai quả trứng. Nếu đó là tội, thì đó là tội... làm bố quá tận tâm.
```
**Part 3** → `audio/vs/scene06_p3.wav` (69 ký tự) · 🎭 cameo `tham_phan`

```text
Cộc cộc cộc! Tòa tuyên: bị cáo vô tội... nhưng phải trả lại viên sỏi!
```
**Part 4** → `audio/vs/scene06_p4.wav` (259 ký tự) · mood `hao_hung`

```text
Và thế là Quý ông Vest Đuôi Tôm bước ra khỏi tòa, lạch bạch quay về tổ, trong mỏ ngậm... một viên sỏi mới nhặt của nhà bên cạnh. [laughter] Còn bạn, nếu là bồi thẩm đoàn, bạn sẽ tuyên bị cáo có tội hay vô tội? Hãy viết phán quyết của bạn ở phần bình luận nhé!
```
**Part 5** → `audio/vs/scene06_p5.wav` (280 ký tự) · mood `am_ap`

```text
Tập sau, chúng ta sẽ rời tòa án để bước vào phòng khám, nơi một bệnh nhân đặc biệt đang chờ: Gấu Cô-a-la. Bày sẵn đĩa lá ngon nhất ngay trước mặt, nhưng bệnh nhân này thà nhịn đói, vì bộ não của nó... không nhận ra đó là thức ăn. Hẹn gặp lại các bạn trong hồ sơ bệnh án tiếp theo!
```

### Shorts → `audio/vs/shorts.wav`

```text
Bị cáo, mời đứng lên! [surprise-oh] Chú chim cánh cụt mặc vest đuôi tôm này đang bị truy tố vì tội đẩy bạn xuống biển... để thử xem có hải cẩu báo hay không! Bị cáo chỉ cao bảy mươi xăng-ti-mét, nặng ngang một con mèo nhà, đi lạch bạch như trẻ mẫu giáo. Hiện trường: mép băng Nam Cực. Hàng trăm chú chim chen chúc, ai cũng đói, nhưng không ai chịu nhảy trước. Vì dưới nước là hải cẩu báo dài ba mét rưỡi, nặng năm trăm ki-lô-gam, đang nấp sẵn! Thế là chen lên, ủn tới, và... tõm! Một bạn xui xẻo rơi xuống trước. Cả bầy nín thở nhìn theo. Bạn ấy bơi đi an toàn? Cả hội ào ào nhảy theo như đi tắm biển! [laughter] Chưa hết, bị cáo còn trộm sỏi nhà hàng xóm để xây tổ, và bắn phân xa tới một mét ba mươi tư! Nhưng khoan, nhiều nhà khoa học nói đây không phải âm mưu, chỉ là chen lấn giờ cao điểm, ai đứng đầu hàng thì bị dồn xuống! [question-ah] Vậy bị cáo có tội hay vô tội? Xem trọn phiên tòa trong video dài ngay bên dưới, vì bị cáo này...
```

**Whisper prompt:** `Chim cánh cụt A-đê-li, Adélie, Quý ông Vest Đuôi Tôm, bị cáo, bồi thẩm đoàn, công tố viên, hải cẩu báo, sỏi, Nam Cực, Levick, Cape Adare, Ig Nobel, Humboldt, Gentoo, Skua, kPa, Koala`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| Âm bốn mươi độ C | -40°C |
| âm bốn mươi độ C | -40°C |
| bảy mươi xăng-ti-mét | 70cm |
| từ ba đến sáu ki-lô-gam | 3-6kg |
| hai phần trăm | 2% |
| hai trăm viên | 200 viên |
| năm triệu | 5 triệu |
| hai cây số một giờ | 2km/h |
| ba mét rưỡi | 3,5m |
| năm trăm ki-lô-gam | 500kg |
| bốn mươi cây số một giờ | 40km/h |
| một ngàn chín trăm mười một | 1911 |
| gần một năm | gần 1 năm |
| hai ngàn lẻ ba | 2003 |
| hai ngàn lẻ năm | 2005 |
| hai ngàn hai mươi | 2020 |
| hai ngàn mười hai | 2012 |
| từ mười đến sáu mươi ki-lô-pát-xcan | 10-60 kPa |
| một mét ba mươi tư | 1,34m |
| tám cây số một giờ | 8km/h |
| ba mét | 3m |
| bốn mươi sáu | 46 |
| năm trăm chín mươi lăm ngàn | 595.000 |
| hơn một mét | hơn 1m |
| mười lăm cây số một giờ | 15km/h |
| một trăm tám mươi mét | 180m |
| hai mét | 2m |
| bốn bằng chứng | 4 bằng chứng |
| số một | số 1 |
| số hai | số 2 |
| số ba | số 3 |
| số bốn | số 4 |
| hai quả trứng | 2 quả trứng |
| hai chế độ | 2 chế độ |
| hai nhà khoa học | 2 nhà khoa học |
| A-đê-li | Adélie |
| Lê-vích | Levick |
| Kếp A-đe | Cape Adare |
| I-gơ Nô-ben | Ig Nobel |
| Hum-bôn | Humboldt |
| Gen-tu | Gentoo |
| Xku-a | Skua |
| Cô-a-la | Koala |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · BỊ CÁO MẶC VEST ĐUÔI TÔM · 56.5s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:04.0 (4.0s) | L01 | Nam Cực. -40°C. Gió rít qua những tảng băng trắng xóa... | **-40°C** · lạnh thấu xương · R/360 · [0.78, 0.6] | Toàn cảnh Nam Cực trong bão tuyết: núi băng trắng xanh, gió cuốn tuyết thành vệt, bầu trời xám. BÊN PHẢI cắm một chiếc nhiệt kế khổng lồ đóng băng, cột đỏ tụt xuống tận đáy. KHÔNG có chú cánh cụt nơ đỏ trong cảnh này. |
| b02 | 00:04.0–00:06.5 (2.5s) | L02 | Một viên sỏi vừa biến mất khỏi tổ của người hàng xóm. |  | Một cái tổ hình vòng tròn xếp bằng những viên sỏi xám nằm trên bãi đá, phía trước tổ có một chỗ trống hình viên sỏi được khoanh bằng nét đứt như hiện trường vụ án; một chiếc kính lúp to ở GIỮA soi vào chỗ trống; BÊN TRÁI một chú cánh cụt hàng xóm (không đeo nơ) há mỏ sửng sốt. |
| b03 | 00:06.5–00:09.7 (3.2s) | L03 | Ở mép băng, một chú chim vừa bị đẩy rơi tõm xuống làn nước lạnh buốt. |  | Mép một tảng băng trôi trên biển xanh thẫm: một chú cánh cụt (không đeo nơ) đang rơi tõm xuống nước, hai cánh vung loạn, nước bắn tung tóe; trên mép băng thấy một chiếc chân cánh cụt khác vừa rụt lại đầy bí ẩn. |
| b04 | 00:09.7–00:15.4 (5.7s) | L04 | Và trên nền tuyết trắng tinh, những vệt màu hồng kéo dài như ai đó vừa nã súng sơn... Ai đứng sau tất cả những chuyện này? |  | Nhìn từ trên cao: nền tuyết trắng với nhiều vệt màu hồng trắng tỏa ra từ một cái tổ sỏi như tia nắng, giống hiện trường bị bắn súng sơn; một cái bóng đen nhỏ lạch bạch bỏ đi ở góc phải. |
| b05 | 00:15.4–00:18.2 (2.8s) | L05 | Bị cáo, mời đứng lên! |  | Phòng xử án băng giá: Ở GIỮA trên bục cao là ngài thẩm phán hải mã (walrus) già đội tóc giả trắng xoăn, cầm búa gỗ, mặt nghiêm nghị, búa gỗ giơ lên; phía dưới BÊN PHẢI là vành móng ngựa bằng gỗ còn trống, đèn chiếu sáng vào đó. |
| b06 | 00:18.2–00:26.7 (8.5s) | L06 | Và bị cáo là... một chú chim cao chưa tới 70cm, nặng 3-6kg, tức là cỡ một con mèo nhà, đang đi lạch bạch như trẻ mẫu giáo đi | **70 CM** · chiều cao bị cáo · R/330 · [0.62, 0.45]<br>**3-6 KG** · nặng như con mèo · L/470 · [0.25, 0.6] | Trong vành móng ngựa gỗ là chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ, nhỏ xíu đến mức chỉ ló được nửa cái đầu qua thành gỗ, đang nhón chân; BÊN TRÁI là một con mèo nhà màu cam ngồi cạnh để so sánh kích cỡ (cao gần bằng nhau); có thước đo |
| b07 | 00:26.7–00:35.8 (9.1s) | L07 | học muộn! Kính thưa bồi thẩm đoàn, đây là chim cánh cụt Adélie, loài cánh cụt nhỏ nhất ở Nam Cực. Lưng đen, bụng trắng, quanh mắt có một vòng trắng tròn xoe như vừa bị ai dọa giật mình. |  | Chân dung cận cảnh chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ, đứng thẳng như chụp ảnh hồ sơ, hai cánh khép, vòng trắng quanh mắt tròn xoe như vừa bị dọa giật mình, vài giọt mồ hôi lo lắng. |
| b08 | 00:35.8–00:44.2 (8.4s) | L08 | Ở tòa này, chúng tôi gọi bị cáo bằng biệt danh: Quý ông Vest Đuôi Tôm. Trông lịch lãm như đi dự tiệc cưới, nhưng hồ sơ thì dày hơn cả cuốn từ điển! |  | chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ thêm áo vest đuôi tôm đen bóng như đi dự tiệc cưới, cầm ly nước, cười lịch lãm; BÊN PHẢI là một chồng hồ sơ giấy khổng lồ cao hơn cả chú cánh cụt, sắp đổ. |
| b09 | 00:44.2–00:51.7 (7.5s) | L09 | Hôm nay, công tố viên là tôi sẽ đưa ra 4 bằng chứng. Trộm cắp tài sản. Đẩy bạn vào chỗ nguy hiểm. Tấn công bằng vũ khí sinh học tầm xa. Và hành hung cả nhà khoa |  | ông công tố viên hoạt hình đeo kính tròn, mặc áo choàng đen đứng BÊN TRÁI giơ tay chỉ vào một bảng ghim 4 tấm ảnh bằng chứng ở BÊN PHẢI: một viên sỏi, một cú rơi xuống nước bắn tung tóe, một vệt bắn màu hồng trắng, một bàn tay bị tát đỏ ửng. |
| b10 | 00:51.7–00:56.5 (4.8s) | L10 | học! Còn bồi thẩm đoàn, tức là các bạn, sẽ tự quyết định: một kẻ đáng yêu như thế này... có thật sự có tội? |  | Hàng ghế bồi thẩm đoàn gồm các bạn nhỏ hoạt hình đủ màu da và vài con thú dễ thương, nửa số đang nhìn với đôi mắt trái tim, nửa còn lại nheo mắt nghi ngờ; ở GIỮA phía trước là chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ đang chớp mắt ngây  |

### scene02 · KẺ TRỘM SỎI XỨ BĂNG · 105.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.5 (7.5s) | L11 | Bằng chứng số 1: trộm cắp tài sản có giá trị lớn. Tài sản bị trộm là... một viên sỏi. Vâng, bồi thẩm đoàn không nghe nhầm đâu. Một viên sỏi. |  | Một túi nilon đựng tang vật trong suốt kẹp nhãn trắng (nhãn trống không chữ) đặt trên bàn gỗ của tòa; bên trong túi chỉ có đúng MỘT viên sỏi xám bé xíu; đèn rọi vào; KHÔNG có chú cánh cụt nơ đỏ trong cảnh này. |
| b02 | 00:07.5–00:11.6 (4.1s) | L12 | Nhưng ở Nam Cực, sỏi không hề rẻ. Chỉ khoảng 2% lục địa này là không bị băng phủ. | **2%** · đất không có băng · R/380 · [0.7, 0.55] | Bản đồ lục địa Nam Cực hoạt hình nhìn từ trên: gần như toàn bộ phủ băng trắng, chỉ có vài mảng đá nâu xám nhỏ xíu dọc bờ biển được khoanh tròn đỏ; một chiếc kính lúp ở GIỮA-PHẢI soi vào một mảng đá. KHÔNG có chú cánh cụt nơ đỏ trong cảnh này. |
| b03 | 00:11.6–00:15.9 (4.3s) | L13 | Mỗi mùa xuân, hàng triệu chú cánh cụt Adélie kéo nhau lên đúng những bãi đá hiếm hoi ấy để xây tổ. |  | Một đoàn cánh cụt Adélie đông nghịt nối đuôi nhau lạch bạch đi từ biển băng lên một bãi đá trống, kéo dài tới tận chân trời, con nào cũng hăm hở. |
| b04 | 00:15.9–00:19.1 (3.2s) | L14 | Và tổ của chúng không làm bằng cỏ, không làm bằng lông, mà làm bằng sỏi. |  | Chia 3 ô: BÊN TRÁI tổ cỏ bị gạch chéo đỏ, Ở GIỮA tổ lông vũ bị gạch chéo đỏ, BÊN PHẢI một cái tổ tròn xếp bằng sỏi xám có dấu tích xanh lá to. |
| b05 | 00:19.1–00:26.9 (7.7s) | L15 | Trung bình mỗi tổ cần khoảng 200 viên. Tức là một con chim nặng bằng con mèo phải tự tay, à không, tự mỏ, khuân 200 viên đá về nhà! | **200 VIÊN** · sỏi cho 1 cái tổ · R/340 · [0.72, 0.5] | chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ ngậm một viên sỏi trong mỏ, mồ hôi nhễ nhại, cạnh một đống sỏi cao như núi nhỏ BÊN PHẢI; BÊN TRÁI là con mèo nhà ngồi nhìn ngạc nhiên để so sánh: con chim nặng bằng con mèo mà phải khuân cả núi đ |
| b06 | 00:26.9–00:31.2 (4.3s) | L16 | Và thế là tội ác bắt đầu! Hàng xóm vừa quay lưng. Quý ông Vest Đuôi Tôm rón rén |  | Bãi đá với nhiều tổ sỏi: BÊN TRÁI một chú cánh cụt hàng xóm (không đeo nơ) đang quay lưng ngắm biển; BÊN PHẢI chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ đeo mặt nạ kẻ trộm đen che mắt, nhón chân rón rén tiến tới tổ hàng xóm. |
| b07 | 00:31.2–00:34.1 (2.9s) | L17 | bước tới. Ngoạm một viên! Quay về tổ! Đặt xuống! Lại rón rén đi tiếp! |  | chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ ngậm một viên sỏi, chạy lạch bạch thật nhanh với vệt chuyển động phía sau, từ tổ hàng xóm BÊN TRÁI về tổ của mình BÊN PHẢI, mũi tên nét đứt chỉ đường đi. |
| b08 | 00:34.1–00:37.0 (2.9s) | L18 | Có kẻ trộm xong còn đứng ngay sau lưng nạn nhân để chọn viên thứ hai! |  | chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ đứng ngay sau lưng một chú cánh cụt hàng xóm đang ngủ gật trên tổ, một cánh đặt lên cằm như đang lựa chọn, mắt nheo nhìn viên sỏi đẹp nhất trong tổ của nạn nhân. |
| b09 | 00:37.0–00:43.4 (6.4s) | L19 | Nạn nhân phát hiện thì sao? Mổ! Đập cánh! Rượt đuổi vòng quanh bãi đá! Một cuộc rượt đuổi tốc độ cao... 2km/h. | **2 KM/H** · tốc độ rượt đuổi · L/360 · [0.5, 0.55] | Cuộc rượt đuổi vòng quanh bãi đá: một chú cánh cụt hàng xóm giận dữ (không đeo nơ) giơ cánh đuổi theo chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ đang ngậm sỏi bỏ chạy; cả hai chạy rất chậm như quay chậm, bên cạnh có một con ốc sên đang vư |
| b10 | 00:43.4–00:55.9 (12.5s) | L20 | Điều buồn cười nhất là: kẻ trộm giỏi nhất lại chính là kẻ canh nhà kỹ nhất. Các nhà làm phim tài liệu đã quay được một gã vừa đi trộm khắp nơi, vừa đứng gác tổ mình như bảo vệ ngân hàng. Bởi vì gã biết rõ hơn ai hết: ở đây, ai cũng là trộm! |  | chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ đội mũ bảo vệ, cầm đèn pin, đứng gác cái tổ sỏi của mình như bảo vệ ngân hàng, mắt đảo nghi ngờ; BÊN TRÁI một nhóm làm phim tài liệu (người cầm máy quay) đang lén quay lại. |
| b11 | 00:55.9–01:07.1 (11.2s) | L21 | Bồi thẩm đoàn thử tưởng tượng: cả một khu phố 5 triệu dân, nhà nào cũng thiếu gạch, và ai cũng đang lén lấy gạch nhà bên cạnh. Cứ đà này, có khi một viên sỏi đi một vòng khắp xóm rồi lại quay về đúng cái tổ ban đầu! | **5 TRIỆU** · dân số khu phố · R/400 · [0.5, 0.5] | Nhìn từ trên cao: một vòng tròn khổng lồ gồm rất nhiều tổ sỏi, mỗi chú cánh cụt đều đang lén lấy sỏi của tổ bên cạnh, các mũi tên nhỏ nối thành một vòng xoay; ở giữa vòng tròn có một viên sỏi phát sáng đi theo đường nét đứt quay về đúng tổ ban đầu. |
| b12 | 01:07.1–01:15.3 (8.2s) | L22 | Còn ở họ hàng nhà cánh cụt Gentoo, chàng trai mang viên sỏi đẹp nhất tặng bạn đời như tặng nhẫn kim cương. Ở Nam Cực, không có sỏi thì đừng mơ lấy |  | Một chú cánh cụt Gentoo (mỏ cam đỏ, vệt trắng trên đỉnh đầu, chân cam) quỳ một chân, hai cánh dâng lên một viên sỏi tròn bóng lấp lánh như nhẫn kim cương cho một cô cánh cụt Gentoo đang ôm má e thẹn, trái tim bay quanh. |
| b13 | 01:15.3–01:26.0 (10.7s) | L85 | vợ! Mà bồi thẩm đoàn biết không, nhiều chàng cánh cụt năm nào cũng quay về xây tổ đúng chỗ cũ, mong cô bạn đời năm ngoái nhận ra nhà mà quay lại. Thế nên một cái tổ đẹp vừa là ngôi nhà, vừa là... tấm biển địa chỉ! |  | chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ đứng bên tổ sỏi đúng chỗ cũ, cạnh tổ cắm một hòm thư nhỏ hình ngôi nhà (không chữ); xa xa một cô cánh cụt Adélie đeo nơ hồng đang đi tới, bong bóng nghĩ của cô vẽ hình cái tổ năm ngoái giống hệt; |
| b14 | 01:26.0–01:30.3 (4.3s) | L86 | Tổ xấu quá thì sao? Cô nàng đi lướt qua luôn, coi như không quen biết! |  | Một chú cánh cụt (không đeo nơ) đứng cạnh cái tổ lèo tèo chỉ vài viên sỏi, mặt hi vọng; cô cánh cụt đeo nơ hồng ngẩng cao đầu đi lướt qua, mắt nhìn đi chỗ khác, vẻ coi như không quen biết; chú kia há mỏ thất vọng hài hước. |
| b15 | 01:30.3–01:34.5 (4.1s) | L23 | Thưa tòa, cháu không trộm! Cháu chỉ... mượn vĩnh viễn thôi ạ! |  | Trong vành móng ngựa: chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ chắp hai cánh trước ngực làm mặt ngây thơ, mắt to long lanh; phía sau lưng chú lộ ra một viên đá xám tròn nhỏ; BÊN PHẢI ngài thẩm phán hải mã (walrus) già đội tóc giả trắng  |
| b16 | 01:34.5–01:45.4 (10.9s) | L24 | Bồi thẩm đoàn đã nghe rồi đấy. Mượn vĩnh viễn! Công tố viên đề nghị ghi nhận: bị cáo có hành vi chiếm đoạt sỏi một cách có hệ thống, có tổ chức, và có cả kỹ năng nhìn trước ngó sau chuyên nghiệp. Bằng chứng số 1, kết thúc. |  | chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ đứng trước bức tường đo chiều cao kiểu chụp ảnh can phạm (chỉ có vạch kẻ ngang, không số), hai cánh ôm một viên sỏi, mặt phụng phịu; đèn flash máy ảnh lóe sáng. |

### scene03 · ĐẨY BẠN XUỐNG NƯỚC DÒ HẢI CẨU · 83.6s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:05.2 (5.2s) | L25 | Bằng chứng số 2. Hiện trường: mép băng, lúc chiều tà. Hàng trăm chú cánh cụt đứng chen chúc sát mép nước. |  | Mép băng lúc chiều tà, trời cam tím: hàng trăm chú cánh cụt Adélie đứng chen chúc sát mép tảng băng nhìn xuống làn nước biển xanh thẫm phía dưới. |
| b02 | 00:05.2–00:09.7 (4.6s) | L26 | Ai cũng đói. Ai cũng muốn xuống biển bắt cá và tôm nhỏ. Nhưng... không ai chịu nhảy trước. Vì sao ư? |  | Cận cảnh vài chú cánh cụt trên mép băng ôm bụng đói, bong bóng suy nghĩ phía trên vẽ cá bạc và tôm nhỏ màu hồng; nhưng các ngón chân dừng sát mép băng, run run, không ai dám bước; chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ đứng ở hàng giữ |
| b03 | 00:09.7–00:13.8 (4.0s) | L27 | Vì dưới làn nước tối kia... có thể có thứ gì đó đang chờ. |  | Mặt cắt ngang tảng băng và biển: phía trên là chân các chú cánh cụt sát mép, phía dưới mặt nước tối om có một cái bóng to lớn mờ mờ với hai con mắt phát sáng đang rình. KHÔNG có chú cánh cụt nơ đỏ trong cảnh này. |
| b04 | 00:13.8–00:17.4 (3.6s) | L28 | Hải cẩu báo! Dài tới 3,5m! Nặng tới 500kg! Bơi nhanh | **3,5 M** · chiều dài hải cẩu báo · L/330 · [0.5, 0.62]<br>**500 KG** · nặng như con bò · R/470 · [0.62, 0.42] | Một con hải cẩu báo (leopard seal) hoạt hình to dài, thân thon màu xám bạc có đốm đen, đầu to như đầu rắn, nằm dọc khung hình; một chiếc thước dây vàng kéo từ mũi tới đuôi. KHÔNG có chú cánh cụt nơ đỏ trong cảnh này. |
| b05 | 00:17.4–00:20.2 (2.8s) | L30 | 40km/h! Cái đầu to như đầu rắn! Hàm đầy răng nanh dài! |  | Cận cảnh đầu hải cẩu báo há miệng rộng (không máu, phong cách hài), lộ hàm răng nanh dài nhọn trắng, mắt láu cá. KHÔNG có chú cánh cụt nơ đỏ trong cảnh này. |
| b06 | 00:20.2–00:24.6 (4.4s) | L31 | Nó nấp ngay dưới mép băng, chỉ ló mỗi cái mũi! Chờ đúng khoảnh khắc một chú cánh cụt chạm |  | Mặt cắt mép băng: hải cẩu báo nấp sát dưới mép băng, chỉ ló mỗi cái mũi trên mặt nước; phía trên mép băng các chú cánh cụt chưa hề hay biết. |
| b07 | 00:24.6–00:29.2 (4.6s) | L32 | nước! So với Quý ông Vest Đuôi Tôm nặng bằng con mèo, đây là một chiếc xe tải có răng! |  | So sánh hài hước: BÊN TRÁI chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ bé xíu; BÊN PHẢI hải cẩu báo được vẽ như một chiếc xe tải có bánh xe và hàm răng nanh to đùng, cười nhe răng. |
| b08 | 00:29.2–00:34.3 (5.1s) | L33 | Và thế là cảnh tượng kỳ lạ nhất Nam Cực diễn ra. Cả bầy chen tới, chen lui, huých nhau, ủn nhau. |  | Đám đông cánh cụt trên mép băng chen chúc huých nhau, ủn nhau, cánh vung loạn xạ, mặt hoảng hốt, giống giờ tan tầm; chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ kẹt ở giữa đám đông. |
| b09 | 00:34.3–00:37.6 (3.3s) | L34 | Con đứng hàng đầu cố bám chân lại. Mấy con phía sau cứ thế mà dồn lên. |  | Một chú cánh cụt (không đeo nơ) đứng hàng đầu đang ngả người ra sau, hai chân bấu chặt mép băng, hai cánh chới với; phía sau mấy chú khác dồn lên ép tới. |
| b10 | 00:37.6–00:40.3 (2.7s) | L35 | Và rồi... tõm! Một bạn xui xẻo rơi xuống nước! |  | Chú cánh cụt xui xẻo (không đeo nơ) rơi tõm xuống nước tạo cột nước bắn tung tóe hình vương miện, chữ tượng thanh được thay bằng các tia nước to. |
| b11 | 00:40.3–00:43.6 (3.3s) | L36 | Cả bầy lập tức nín thở, nghển cổ nhìn theo như khán giả xem phim kinh dị. |  | Cả bầy cánh cụt trên mép băng nghển cổ nhìn xuống nước, mắt mở to nín thở như khán giả xem phim kinh dị, có con ôm hộp bỏng ngô, có con che mắt hé nhìn; chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ cắn móng cánh. |
| b12 | 00:43.6–00:47.8 (4.2s) | L37 | Nếu bạn ấy bơi đi bình an, cả hội ào ào nhảy theo như đi tắm biển ngày hè! |  | Chú cánh cụt dưới nước vẫy cánh vui vẻ bình an; phía trên cả bầy ào ào nhảy xuống theo như đi tắm biển ngày hè, có con đeo kính bơi, có con mang phao vịt. |
| b13 | 00:47.8–00:51.4 (3.6s) | L38 | Còn nếu không... thì cả bầy lùi lại, đứng chờ thêm một lúc nữa. |  | Cả bầy cánh cụt lùi lại xa mép băng một bước, đứng thành hàng lo lắng, mồ hôi rơi, nhìn đồng hồ cát; mặt nước phía trước chỉ còn bong bóng (không có cảnh bạo lực); chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ đứng ở cuối hàng. |
| b14 | 00:51.4–01:01.1 (9.7s) | L39 | Nhân chứng của vụ án này là một người rất đặc biệt. Năm 1911, bác sĩ Levick của đoàn thám hiểm Nam Cực nước Anh đã sống gần 1 năm ở Cape Adare, ngày ngày ngồi quan sát từng chú cánh cụt Adélie. | **1911** · Cape Adare · R/330 · [0.3, 0.5] | Năm 1911: một bác sĩ thám hiểm người Anh hoạt hình, râu mép, mặc áo lông thú dày và mũ len, ngồi trên thùng gỗ cạnh túp lều gỗ phủ tuyết, cầm sổ tay và bút chì quan sát đàn cánh cụt Adélie; phong cách hơi cổ điển màu nâu sepia nhẹ. |
| b15 | 01:01.1–01:06.5 (5.5s) | L40 | Ông ghi lại cảnh chúng đứng trên mép băng, né qua né lại, và cố đẩy nhau xuống nước. Xin mời nhân chứng. |  | Trang sổ tay mở rộng với hình phác thảo bằng bút chì: các chú cánh cụt né qua né lại trên mép băng và đẩy nhau xuống nước, có mũi tên phác thảo; bàn tay bác sĩ cầm bút chì đang vẽ. |
| b16 | 01:06.5–01:11.5 (5.0s) | L41 | Mấy con đứng sau suýt đẩy được hàng đầu xuống nước, thế là hàng đầu vòng ra phía sau để đẩy lại! |  | Vòng tròn hài hước: những chú cánh cụt hàng đầu suýt rơi liền chạy vòng ra phía sau đám đông để đẩy lại, tạo thành một vòng xoay vô tận có mũi tên tròn; một ông lão nhân chứng râu bạc ở góc trái kể lại, tay chỉ vào. |
| b17 | 01:11.5–01:23.6 (12.1s) | L42 | Bồi thẩm đoàn nghe rõ chưa? Vòng ra phía sau để đẩy lại! Đây không còn là đi bơi nữa, đây là trò kéo co ngược chiều! Thua thì làm vật thí nghiệm, thắng thì được đi ăn trưa an toàn. Bằng chứng số 2, cực kỳ nghiêm trọng! |  | Trò kéo co ngược chiều: hai đội cánh cụt đứng hai bên mép băng cố đẩy ngược nhau về phía nước; BÊN PHẢI một chú (không đeo nơ) thắng cuộc thong thả ăn con cá, BÊN TRÁI chú thua cuộc bơi dưới nước liếc nhìn lo lắng; chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc  |

### scene04 · KHẨU SÚNG PHÂN ÁP LỰC CAO · 94.0s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.9 (9.9s) | L43 | Bằng chứng số 3: tấn công bằng vũ khí sinh học tầm xa. Thưa bồi thẩm đoàn, vũ khí đó... là phân. Chim cánh cụt ấp trứng nhiều ngày liền không rời tổ. Vậy nó đi vệ sinh ở đâu? Rất đơn giản. |  | chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ nằm ấp trứng trên tổ sỏi, mặt kiên nhẫn mệt mỏi, xung quanh các tờ lịch bay vèo vèo thể hiện nhiều ngày trôi qua, tuyết rơi trên đầu; BÊN PHẢI một chiếc khăn phủ che một 'vũ khí' bí ẩn hình ống. |
| b02 | 00:09.9–00:14.4 (4.5s) | L44 | Nó đứng dậy, quay lưng ra mép tổ, nhấc đuôi lên, và... bắn! Một vệt trắng hồng phóng thẳng ra ngoài. |  | Phong cách hoạt hình hài nhẹ nhàng, thân thiện trẻ em: chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ đứng ở mép tổ, quay lưng ra ngoài, chổng đuôi lên, phóng ra một vệt chất lỏng trắng hồng thành đường vòng cung bay xa như vòi nước, vẻ mặt t |
| b03 | 00:14.4–00:21.5 (7.1s) | L45 | Cứ thế, quanh mỗi cái tổ là những tia vệt tỏa ra như tia nắng mặt trời. Nhìn từ trên cao, cả bãi đá giống hệt một bức tranh vẽ bằng súng sơn! |  | Nhìn từ trên cao: nhiều cái tổ sỏi tròn, quanh mỗi tổ có các vệt trắng hồng tỏa ra đều như tia nắng mặt trời hoặc như vết súng sơn, tạo thành một bức tranh hoa văn đẹp mắt trên bãi đá. |
| b04 | 00:21.5–00:31.9 (10.4s) | L46 | Chuyện nghe thì buồn cười, nhưng các nhà khoa học đã tính toán hẳn hoi. Năm 2003, 2 nhà khoa học đo độ dài vệt phân quanh tổ, rồi dùng công thức vật lý tính ra áp suất bên trong bụng chim cánh cụt. | **2003** · đo vệt phân · R/330 · [0.4, 0.62] | Hai nhà khoa học hoạt hình mặc áo khoác đỏ, một người quỳ cầm thước dây đo độ dài một vệt trắng hồng trên tuyết, người kia cầm máy tính bỏ túi và bảng kẹp giấy với công thức vẽ nguệch ngoạc (không chữ đọc được); một chú cánh cụt đứng nhìn ngơ ngác. |
| b05 | 00:31.9–00:39.5 (7.6s) | L47 | Kết quả: 10-60 kPa! Mạnh gấp mấy lần lúc con người đi vệ sinh, cỡ một nửa áp suất lốp xe hơi! | **60 KPA** · áp suất cực đại · L/340 · [0.22, 0.4] | BÊN TRÁI một chú cánh cụt với chiếc đồng hồ đo áp suất to dán bên cạnh, kim vọt lên vùng đỏ; BÊN PHẢI một chiếc lốp xe hơi với đồng hồ đo áp suất kim cao gấp đôi; dấu bằng một nửa ở giữa. |
| b06 | 00:39.5–00:47.7 (8.2s) | L48 | Công trình này còn đoạt giải Ig Nobel năm 2005, giải thưởng dành cho những nghiên cứu khiến người ta bật cười trước, rồi mới suy nghĩ sau. | **IG NOBEL** · giải năm 2005 · R/340 · [0.5, 0.4] | Lễ trao giải vui nhộn: hai nhà khoa học trên sân khấu cầm chiếc cúp hình chú cánh cụt vàng, khán giả bên dưới cười nghiêng ngả, pháo giấy bay. |
| b07 | 00:47.7–00:55.5 (7.7s) | L49 | Chưa hết! Năm 2020, 2 nhà khoa học Nhật Bản tính lại trên loài cánh cụt Humboldt! Lần này tính cả góc bắn! Cả sức cản không khí! Cả độ sệt của phân! | **2020** · tính lại tầm bắn · R/330 · [0.25, 0.45] | Hai nhà khoa học Nhật Bản hoạt hình đeo kính đứng cạnh tấm bảng trắng vẽ một đường parabol và các mũi tên lực (không chữ); BÊN PHẢI một chú cánh cụt Humboldt (mặt có mảng da hồng quanh mỏ, một vạch đen ngang ngực) đứng trên tảng đá. |
| b08 | 00:55.5–00:59.4 (3.9s) | L50 | Kết quả: tầm bắn xa nhất 1,34m! Tốc độ gần 8km/h! | **1,34 M** · tầm bắn xa nhất · R/360 · [0.78, 0.68]<br>**8 KM/H** · tốc độ bay · L/470 · [0.45, 0.35] | Chú cánh cụt Humboldt đứng trên tảng đá BÊN TRÁI, một đường vòng cung nét đứt bay sang BÊN PHẢI đáp xuống cạnh một lá cờ cắm trên đất; một thước dây vàng kéo dài bên dưới dọc theo đường bay. |
| b09 | 00:59.4–01:01.9 (2.5s) | L51 | Nếu đổi sang cỡ người, đó là bắn xa hơn 3m! | **> 3 M** · nếu là con người · R/360 · [0.85, 0.7] | So sánh quy mô: BÊN TRÁI một chú cánh cụt nhỏ với đường vòng cung ngắn; BÊN PHẢI một người đàn ông hoạt hình đứng cạnh một đường vòng cung khổng lồ dài gấp nhiều lần chạm tới lá cờ xa, ông ta ôm mặt ngượng ngùng; phong cách hài lịch sự. |
| b10 | 01:01.9–01:06.2 (4.3s) | L52 | Và họ nghiêm túc khuyên nhân viên thủy cung: hãy đứng cách xa ít nhất 1,34m! | **1,34 M** · khoảng cách an toàn · L/400 · [0.5, 0.78] | Một nhân viên thủy cung hoạt hình mặc áo mưa vàng, đội mũ bảo hộ, cầm ô che, đứng sau một vạch kẻ an toàn màu vàng đen trên sàn, cách xa một chú cánh cụt Humboldt đang chổng đuôi; mặt nhân viên cảnh giác buồn cười. |
| b11 | 01:06.2–01:10.0 (3.8s) | L53 | Và vũ khí này mạnh tới mức... nhìn thấy được từ ngoài vũ trụ! |  | Không gian vũ trụ: một vệ tinh nhân tạo có tấm pin mặt trời bay trên quỹ đạo, bên dưới là quả địa cầu nhìn thấy lục địa Nam Cực trắng xóa; ống kính vệ tinh chiếu tia sáng xuống. KHÔNG có chú cánh cụt nơ đỏ trong cảnh này. |
| b12 | 01:10.0–01:17.9 (7.8s) | L54 | Năm 2012, các nhà khoa học Anh soi ảnh vệ tinh dọc bờ biển Nam Cực, tìm những mảng màu nâu trên nền băng trắng. Mảng nâu đó chính là phân chim cánh cụt! | **2012** · soi ảnh vệ tinh · R/330 · [0.55, 0.4] | Các nhà khoa học hoạt hình ngồi trước màn hình máy tính lớn hiển thị ảnh vệ tinh: nền băng trắng có những mảng màu nâu đỏ được khoanh tròn; một người chỉ tay ngạc nhiên, người kia cầm cốc trà. |
| b13 | 01:17.9–01:27.1 (9.3s) | L55 | Lần theo dấu vết ấy, họ tìm ra 46 đàn cánh cụt hoàng đế, họ hàng to xác của bị cáo, và đếm được khoảng 595.000 con, gần gấp đôi con số người ta từng nghĩ. | **46 ĐÀN** · cánh cụt hoàng đế · L/340 · [0.4, 0.5]<br>**595.000** · con được đếm · R/460 · [0.65, 0.45] | Một đàn cánh cụt hoàng đế khổng lồ (to cao, mảng vàng cam ở cổ và má, mỏ dài có vạch cam) đứng đông nghịt tới tận chân trời trên băng, cạnh đàn là một mảng màu nâu; vài chú con lông xám đứng giữa chân bố mẹ. |
| b14 | 01:27.1–01:34.0 (6.9s) | L56 | Bồi thẩm đoàn thấy chưa: đi đâu cũng để lại dấu vết, lộ cả trên ảnh vệ tinh! Đây là băng nhóm bất cẩn nhất lịch sử! |  | Một tấm ảnh vệ tinh khổng lồ treo trong tòa như tấm áp phích truy nã, trên ảnh là một vệt nâu chỉ thẳng tới một băng nhóm cánh cụt đang ngơ ngác; phía trước chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ lấy cánh che mặt xấu hổ. |

### scene05 · CÔN ĐỒ CÁNH CỨNG TÁT CẢ NHÀ KHOA HỌC · 76.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.7 (8.7s) | L57 | Bằng chứng số 4: hành hung người đang làm nhiệm vụ. Nạn nhân là... các nhà khoa học. Khi nhà nghiên cứu cúi xuống gần tổ để cân chim non, Quý ông Vest Đuôi Tôm không hề bỏ chạy. |  | Một nhà nghiên cứu hoạt hình mặc áo khoác cam, quỳ xuống cạnh tổ sỏi cầm một chiếc cân treo nhỏ định cân chú cánh cụt con lông xám; chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ đứng phắt dậy, mắt trợn giận dữ, lông dựng. |
| b02 | 00:08.7–00:13.2 (4.5s) | L58 | Nó lao tới, đứng thẳng người, và tát! Bằng đôi cánh cứng như mái chèo! Phạch! Phạch! Phạch! |  | chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ đứng thẳng người, vung cánh tát mạnh vào ống chân nhà nghiên cứu, các tia sao va chạm và vệt chuyển động; nhà nghiên cứu nhảy lò cò ôm chân, mặt méo xệch hài hước. |
| b03 | 00:13.2–00:18.6 (5.4s) | L59 | Cánh chim cánh cụt không bay được, nhưng xương cánh dẹt và đặc, quất vào ống chân thì đau như bị cô giáo gõ thước kẻ. |  | Hình mặt cắt kỹ thuật kiểu sách giáo khoa: chiếc cánh cánh cụt dẹt như mái chèo, bên trong lộ xương dẹt đặc màu kem; BÊN PHẢI để so sánh là một cây thước kẻ gỗ và một mái chèo gỗ có hình dạng tương tự. |
| b04 | 00:18.6–00:23.0 (4.4s) | L60 | Không chỉ con người! Chim cướp biển Skua sải cánh rộng hơn 1m lượn tới định cướp trứng? Tát! | **> 1 M** · sải cánh chim Skua · R/340 · [0.6, 0.3] | Một con chim cướp biển Skua nâu sải cánh rộng sà xuống định cướp quả trứng; chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ nhảy lên vung cánh tát vào mỏ nó, lông Skua bay tán loạn. |
| b05 | 00:23.0–00:26.3 (3.3s) | L61 | Hải cẩu bò lên quá gần? Tát! Hàng xóm lấn sang nửa bước? Tát luôn! |  | Chia đôi khung: BÊN TRÁI chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ tát một con hải cẩu lông nâu đang bò lại quá gần tổ khiến nó giật mình lùi lại; BÊN PHẢI chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụn |
| b06 | 00:26.3–00:30.8 (4.5s) | L62 | Cả đời bị cáo chỉ có 2 chế độ: đứng im dễ thương, và tát không cần báo trước! |  | Chia đôi khung có nút công tắc ở giữa: BÊN TRÁI chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ đứng im dễ thương, má hồng, trái tim bay quanh; BÊN PHẢI cùng chú cánh cụt đó mắt đỏ rực, cánh vung tát ra liên tục như cánh quạt. |
| b07 | 00:30.8–00:35.0 (4.3s) | L63 | Và đừng tưởng bị cáo chậm chạp. Trên cạn, nó đi lạch bạch như ông cụ đi chợ. |  | chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ đi lạch bạch trên băng như ông cụ đi chợ, khoác giỏ đi chợ trên cánh, chậm rãi; phía sau là một con ốc sên đi cùng tốc độ. |
| b08 | 00:35.0–00:40.1 (5.0s) | L64 | Nhưng xuống nước thì như tên lửa: bơi 15km/h, lặn sâu tới 180m, | **15 KM/H** · tốc độ bơi · L/340 · [0.5, 0.45]<br>**180 M** · lặn sâu nhất · R/470 · [0.12, 0.85] | Dưới nước xanh: chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ lao đi như tên lửa ngư lôi với vệt bọt khí dài phía sau, đuổi theo đàn cá bạc; bên trái có thang đo độ sâu vẽ vạch xuống tận đáy tối. |
| b09 | 00:40.1–00:47.5 (7.4s) | L65 | và khi phóng lên, nó có thể bật một cú nhảy cao tới 2m, đáp thẳng lên tảng băng! Trên bờ là diễn viên hài, dưới nước là đặc vụ! | **2 M** · cú nhảy lên băng · R/360 · [0.75, 0.3] | chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ phóng vọt khỏi mặt nước, bay cao lên theo đường cong và đáp gọn lên mặt một tảng băng cao, tư thế ngầu như đặc vụ đeo kính râm; một thước đo chiều cao dựng cạnh tảng băng. |
| b10 | 00:47.5–00:56.9 (9.4s) | L87 | Còn khi lười đi bộ trên tuyết? Bị cáo nằm sấp xuống, lấy cái bụng làm ván trượt, hai chân đạp phía sau, lướt vèo vèo như trẻ con chơi cầu trượt! Các nhà khoa học gọi đó là cách tiết kiệm sức. |  | chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ nằm sấp trên tuyết, lấy bụng trắng làm ván trượt, hai chân đạp phía sau tung tuyết, lướt vèo vèo xuống dốc với vệt tốc độ, mặt sung sướng như trẻ con chơi cầu trượt. |
| b11 | 00:56.9–01:00.3 (3.5s) | L88 | Còn tòa án gọi đó là... tẩu thoát khỏi hiện trường bằng xe trượt riêng! |  | Hài hước: chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ trượt bụng trên tuyết thoát khỏi một tòa án băng phía sau, miệng ngậm một viên sỏi; phía sau một chú cảnh sát hải cẩu nhỏ đội mũ cảnh sát chạy đuổi theo hụt hơi, còi thổi. |
| b12 | 01:00.3–01:06.1 (5.8s) | L66 | Công tố viên xin tổng kết. Trộm sỏi. Đẩy bạn xuống nước. Nã súng phân xa 1,34m. Và tát cả nhà khoa |  | ông công tố viên hoạt hình đeo kính tròn, mặc áo choàng đen đứng BÊN TRÁI giơ tay chỉ mạnh vào bảng ghim 4 bằng chứng BÊN PHẢI: viên sỏi, cú rơi xuống nước, vệt bắn hồng trắng, cú tát vào ống chân; chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở  |
| b13 | 01:06.1–01:10.2 (4.1s) | L67 | học! Ngay cả nhân chứng Levick năm xưa cũng gọi những chú chim trẻ hay gây rối là... lũ du côn! |  | Ông bác sĩ thám hiểm năm 1911 (râu mép, áo lông thú) cau mày nhìn một nhóm cánh cụt Adélie trẻ nghịch ngợm mặc áo khoác da, đội mũ lưỡi trai ngược, đang xô đẩy nhau phá phách trên bãi đá. |
| b14 | 01:10.2–01:13.7 (3.5s) | L68 | Ông còn viết một số trang nhật ký bằng chữ cái Hy Lạp để người khác không đọc được. |  | Ông bác sĩ thám hiểm năm 1911 ngồi trong lều gỗ dưới ánh đèn dầu, lén lút che một trang nhật ký bằng tay, trên trang có các ký hiệu ngoằn ngoèo bí ẩn bị một ổ khóa vẽ đè lên; vẻ mặt bí mật hài hước. |
| b15 | 01:13.7–01:16.7 (2.9s) | L69 | Bằng chứng đã đủ. Công tố viên đề nghị mức án cao nhất! |  | ông công tố viên hoạt hình đeo kính tròn, mặc áo choàng đen đập mạnh tập hồ sơ xuống bàn, giấy bay tứ tung; ngài thẩm phán hải mã (walrus) già đội tóc giả trắng xoăn, cầm búa gỗ trên bục nhìn xuống; chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở |

### scene06 · LUẬT SƯ BÀO CHỮA & PHÁN QUYẾT · 91.6s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.9 (8.9s) | L70 | Khoan đã! Phản đối! Bây giờ, xin cho tôi cởi áo công tố viên, và khoác áo luật sư bào chữa. Bởi vì bồi thẩm đoàn mới chỉ nghe một nửa câu chuyện. Về bằng chứng số 1: vì sao |  | Người đàn ông hoạt hình đeo kính tròn đang cởi chiếc áo choàng đen công tố viên ném sang một bên và khoác lên bộ vest xanh dương của luật sư bào chữa, tay giơ ngón trỏ 'phản đối', vẻ mặt quyết tâm; tia sáng đổi vai phía sau. |
| b02 | 00:08.9–00:12.5 (3.6s) | L71 | phải trộm sỏi? Mỗi mùa xuân, tuyết tan thành những dòng nước lạnh chảy tràn qua bãi đá. |  | Mùa xuân Nam Cực: tuyết tan thành những dòng nước lạnh xanh nhạt chảy tràn qua bãi đá làm tổ của đàn cánh cụt, tạo thành các vũng nước lớn. |
| b03 | 00:12.5–00:15.6 (3.1s) | L72 | Quả trứng nằm sát mặt đất sẽ bị ngâm nước, lạnh cóng, rồi hỏng. |  | Một quả trứng cánh cụt hoạt hình có khuôn mặt dễ thương nằm sát mặt đất trong vũng nước lạnh, run cầm cập, quấn khăn len, băng giá bám quanh; cái tổ thấp lè tè bị nước tràn vào. |
| b04 | 00:15.6–00:20.8 (5.1s) | L73 | Một đống sỏi cao chính là chiếc bè cứu sinh, nâng quả trứng lên khỏi vũng nước. Tổ càng cao, trứng càng an toàn. |  | chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ ngồi ấp 2 quả trứng trên một đống sỏi cao như hòn đảo nhỏ giữa dòng nước tan, trứng khô ráo an toàn; các tổ thấp xung quanh bị ngập; có chiếc phao cứu sinh vẽ mờ như biểu tượng. |
| b05 | 00:20.8–00:26.0 (5.3s) | L74 | Thứ bị cáo trộm không phải của cải, mà là... cơ hội sống cho con mình. Về bằng chứng số 2: |  | chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ ôm hai quả trứng vào lòng trên tổ sỏi cao, ánh sáng vàng ấm áp tỏa quanh, trái tim nhỏ bay lên, khuôn mặt hiền hậu. |
| b06 | 00:26.0–00:34.7 (8.7s) | L75 | nhiều nhà khoa học cho rằng phần lớn những cú rơi ở mép băng không phải âm mưu gì cả. Đó chỉ là cảnh chen lấn giờ cao điểm: bầy đông dồn lên, con đứng đầu bị đẩy ra mép, và thế là tõm. |  | Cảnh giờ cao điểm ở mép băng như ga tàu điện ngầm đông nghịt: hàng trăm chú cánh cụt dồn lên, một chú đầu hàng bị đẩy ra mép một cách vô tình, ai cũng ngơ ngác không cố ý. |
| b07 | 00:34.7–00:41.2 (6.4s) | L76 | Nhảy theo bầy lại là cách sống sót tốt nhất, vì một con hải cẩu báo không thể bắt hết cả trăm con cùng lúc. Về bằng chứng số 3: |  | Hàng trăm chú cánh cụt cùng lúc lao xuống nước tỏa ra mọi hướng; ở giữa một con hải cẩu báo xoay vòng chóng mặt, mắt quay mòng mòng không biết đuổi con nào. |
| b08 | 00:41.2–00:49.6 (8.5s) | L77 | bắn phân ra xa là để giữ tổ khô ráo, sạch sẽ cho trứng và con non. Đó là vệ sinh cá nhân... chỉ hơi mạnh tay một chút thôi! Còn bằng chứng số |  | chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ cầm một cây chổi nhỏ quét tổ sỏi sạch bóng lấp lánh, chú cánh cụt con lông xám ngồi trong tổ khô ráo vui vẻ; các vệt trắng hồng nằm xa bên ngoài tổ. |
| b09 | 00:49.6–00:57.9 (8.2s) | L78 | 4, tát cả nhà khoa học? Bồi thẩm đoàn hãy nhìn kỹ: đó là một ông bố bé nhỏ, nặng bằng con mèo, dám đứng chắn trước mọi thứ to lớn hơn mình gấp nhiều lần, chỉ để bảo vệ 2 quả trứng. |  | chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ bé nhỏ dang hai cánh đứng chắn trước tổ có hai quả trứng; phía trước là ba cái bóng khổng lồ cao gấp nhiều lần: chim Skua, hải cẩu báo và một nhà khoa học; chú cánh cụt không lùi bước, ánh mắt ki |
| b10 | 00:57.9–01:00.1 (2.3s) | L79 | Nếu đó là tội, thì đó là tội... làm bố quá tận |  | chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ làm bố ôm chú cánh cụt con lông xám vừa nở, hai bố con dụi má nhau, trái tim to màu đỏ phía sau, cảnh ấm áp cảm động. |
| b11 | 01:00.1–01:04.6 (4.4s) | L80 | tâm. Cộc cộc cộc! Tòa tuyên: bị cáo vô tội... nhưng phải trả lại viên |  | ngài thẩm phán hải mã (walrus) già đội tóc giả trắng xoăn, cầm búa gỗ gõ búa xuống bàn có các vạch tượng thanh rung; phía dưới chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ trong vành móng ngựa thở phào nhẹ nhõm nhưng đang bị yêu cầu đưa trả |
| b12 | 01:04.6–01:11.8 (7.2s) | L81 | sỏi! Và thế là Quý ông Vest Đuôi Tôm bước ra khỏi tòa, lạch bạch quay về tổ, trong mỏ ngậm... một viên sỏi mới nhặt của nhà bên cạnh. |  | chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ lạch bạch rời khỏi tòa án quay về tổ, trong mỏ ngậm một viên sỏi mới vừa nhặt từ tổ nhà bên cạnh, liếc mắt tinh nghịch; chú hàng xóm phía sau đang ngủ không hay biết. |
| b13 | 01:11.8–01:18.3 (6.5s) | L82 | Còn bạn, nếu là bồi thẩm đoàn, bạn sẽ tuyên bị cáo có tội hay vô tội? Hãy viết phán quyết của bạn ở phần bình luận nhé! |  | Hàng ghế bồi thẩm đoàn các bạn nhỏ hoạt hình đa dạng đang giơ thẻ bài: một nửa thẻ hình ngón cái hướng lên màu xanh, một nửa thẻ hình ngón cái hướng xuống màu đỏ, vẻ mặt đang suy nghĩ hào hứng; không có chữ trên thẻ. |
| b14 | 01:18.3–01:23.0 (4.7s) | L83 | Tập sau, chúng ta sẽ rời tòa án để bước vào phòng khám, nơi một bệnh nhân đặc biệt đang chờ: Gấu |  | Phòng khám bác sĩ thú y hoạt hình sáng sủa: một chú gấu Koala lông xám, tai tròn bông xù, mũi đen to, ngồi trên ghế bệnh nhân mắt lờ đờ ngơ ngác, cạnh đó có ống nghe và tấm phim X-quang treo tường. KHÔNG có chú cánh cụt nơ đỏ trong cảnh này. |
| b15 | 01:23.0–01:31.6 (8.7s) | L84 | Koala. Bày sẵn đĩa lá ngon nhất ngay trước mặt, nhưng bệnh nhân này thà nhịn đói, vì bộ não của nó... không nhận ra đó là thức ăn. Hẹn gặp lại các bạn trong hồ sơ bệnh án tiếp theo! |  | Chú gấu Koala ngồi trước một chiếc đĩa sứ đầy lá bạch đàn xanh tươi đặt ngay trước mặt, nhưng nhìn chằm chằm vào chiếc đĩa với dấu chấm hỏi to trên đầu, bụng sôi òng ọc; KHÔNG có chú cánh cụt nơ đỏ trong cảnh này. |

## 5. Phân cảnh Shorts — từng beat

Banner: **ĐẨY BẠN XUỐNG BIỂN / ĐỂ THỬ HẢI CẨU?!** · giọng 48.6s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Bị cáo, mời đứng lên! |  |
| s02 | 00:02.1 | S02 | Chú chim cánh cụt mặc vest đuôi tôm này đang bị truy tố vì tội đẩy bạn xuống biển... để thử xem có hải cẩu báo hay không! |  |
| s03 | 00:08.2 | S03 | Bị cáo chỉ cao 70cm, nặng ngang một con mèo nhà, đi lạch bạch như trẻ mẫu giáo. | **70 CM** · chiều cao bị cáo · L/620 · [0.45, 0.4] |
| s04 | 00:13.1 | S04 | Hiện trường: mép băng Nam Cực. Hàng trăm chú chim chen chúc, ai cũng đói, nhưng không ai chịu nhảy trước. |  |
| s05 | 00:18.2 | S05 | Vì dưới nước là hải cẩu báo dài 3,5m, nặng 500kg, đang nấp sẵn! | **3,5 M** · hải cẩu báo · R/560 · [0.5, 0.7]<br>**500 KG** · nặng như con bò · L/900 · [0.45, 0.75] |
| s06 | 00:22.2 | S06 | Thế là chen lên, ủn tới, và... tõm! Một bạn xui xẻo rơi xuống |  |
| s07 | 00:26.1 | S07 | trước. Cả bầy nín thở nhìn theo. |  |
| s08 | 00:28.1 | S08 | Bạn ấy bơi đi an toàn? Cả hội ào ào nhảy theo như đi tắm biển! |  |
| s09 | 00:31.5 | S09 | Chưa hết, bị cáo còn trộm sỏi nhà hàng xóm để xây |  |
| s10 | 00:34.0 | S10 | tổ, và bắn phân xa tới 1,34m! | **1,34 M** · tầm bắn · R/620 · [0.7, 0.62] |
| s11 | 00:36.5 | S13 | Nhưng khoan, nhiều nhà khoa học nói đây không phải âm mưu, |  |
| s12 | 00:39.5 | S11 | chỉ là chen lấn giờ cao điểm, ai đứng đầu hàng thì bị dồn xuống! |  |
| s13 | 00:43.6 | S12 | Vậy bị cáo có tội hay vô tội? Xem trọn phiên tòa trong video dài ngay bên dưới, vì bị cáo này... |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nam Cực. -40°C. Gió rít qua những tảng băng trắng xóa...". Bố cục: Toàn cảnh Nam Cực trong bão tuyết: núi băng trắng xanh, gió cuốn tuyết thành vệt, bầu trời xám. BÊN PHẢI cắm một chiếc nhiệt kế khổng lồ đóng băng, cột đỏ tụt xuống tận đáy. KHÔNG có chú cánh cụt nơ đỏ trong cảnh này.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một viên sỏi vừa biến mất khỏi tổ của người hàng xóm.". Bố cục: Một cái tổ hình vòng tròn xếp bằng những viên sỏi xám nằm trên bãi đá, phía trước tổ có một chỗ trống hình viên sỏi được khoanh bằng nét đứt như hiện trường vụ án; một chiếc kính lúp to ở GIỮA soi vào chỗ trống; BÊN TRÁI một chú cánh cụt hàng xóm (không đeo nơ) há mỏ sửng sốt.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ở mép băng, một chú chim vừa bị đẩy rơi tõm xuống làn nước lạnh buốt.". Bố cục: Mép một tảng băng trôi trên biển xanh thẫm: một chú cánh cụt (không đeo nơ) đang rơi tõm xuống nước, hai cánh vung loạn, nước bắn tung tóe; trên mép băng thấy một chiếc chân cánh cụt khác vừa rụt lại đầy bí ẩn.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và trên nền tuyết trắng tinh, những vệt màu hồng kéo dài như ai đó vừa nã súng sơn... Ai đứng sau tất cả những chuyện này?". Bố cục: Nhìn từ trên cao: nền tuyết trắng với nhiều vệt màu hồng trắng tỏa ra từ một cái tổ sỏi như tia nắng, giống hiện trường bị bắn súng sơn; một cái bóng đen nhỏ lạch bạch bỏ đi ở góc phải.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bị cáo, mời đứng lên!". Bố cục: Phòng xử án băng giá: Ở GIỮA trên bục cao là ngài thẩm phán hải mã (walrus) già đội tóc giả trắng xoăn, cầm búa gỗ, mặt nghiêm nghị, búa gỗ giơ lên; phía dưới BÊN PHẢI là vành móng ngựa bằng gỗ còn trống, đèn chiếu sáng vào đó.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và bị cáo là... một chú chim cao chưa tới 70cm, nặng 3-6kg, tức là cỡ một con mèo nhà, đang đi lạch bạch như trẻ mẫu giáo đi học muộn!". Bố cục: Trong vành móng ngựa gỗ là chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ, nhỏ xíu đến mức chỉ ló được nửa cái đầu qua thành gỗ, đang nhón chân; BÊN TRÁI là một con mèo nhà màu cam ngồi cạnh để so sánh kích cỡ (cao gần bằng nhau); có thước đo chiều cao vẽ vạch (không số) sau lưng chú cánh cụt.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kính thưa bồi thẩm đoàn, đây là chim cánh cụt Adélie, loài cánh cụt nhỏ nhất ở Nam Cực. Lưng đen, bụng trắng, quanh mắt có một vòng trắng tròn xoe như vừa bị ai dọa giật mình.". Bố cục: Chân dung cận cảnh chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ, đứng thẳng như chụp ảnh hồ sơ, hai cánh khép, vòng trắng quanh mắt tròn xoe như vừa bị dọa giật mình, vài giọt mồ hôi lo lắng.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ở tòa này, chúng tôi gọi bị cáo bằng biệt danh: Quý ông Vest Đuôi Tôm. Trông lịch lãm như đi dự tiệc cưới, nhưng hồ sơ thì dày hơn cả cuốn từ điển!". Bố cục: chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ thêm áo vest đuôi tôm đen bóng như đi dự tiệc cưới, cầm ly nước, cười lịch lãm; BÊN PHẢI là một chồng hồ sơ giấy khổng lồ cao hơn cả chú cánh cụt, sắp đổ.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hôm nay, công tố viên là tôi sẽ đưa ra 4 bằng chứng. Trộm cắp tài sản. Đẩy bạn vào chỗ nguy hiểm. Tấn công bằng vũ khí sinh học tầm xa. Và hành hung cả nhà khoa học!". Bố cục: ông công tố viên hoạt hình đeo kính tròn, mặc áo choàng đen đứng BÊN TRÁI giơ tay chỉ vào một bảng ghim 4 tấm ảnh bằng chứng ở BÊN PHẢI: một viên sỏi, một cú rơi xuống nước bắn tung tóe, một vệt bắn màu hồng trắng, một bàn tay bị tát đỏ ửng.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn bồi thẩm đoàn, tức là các bạn, sẽ tự quyết định: một kẻ đáng yêu như thế này... có thật sự có tội?". Bố cục: Hàng ghế bồi thẩm đoàn gồm các bạn nhỏ hoạt hình đủ màu da và vài con thú dễ thương, nửa số đang nhìn với đôi mắt trái tim, nửa còn lại nheo mắt nghi ngờ; ở GIỮA phía trước là chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ đang chớp mắt ngây thơ.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bằng chứng số 1: trộm cắp tài sản có giá trị lớn. Tài sản bị trộm là... một viên sỏi. Vâng, bồi thẩm đoàn không nghe nhầm đâu. Một viên sỏi.". Bố cục: Một túi nilon đựng tang vật trong suốt kẹp nhãn trắng (nhãn trống không chữ) đặt trên bàn gỗ của tòa; bên trong túi chỉ có đúng MỘT viên sỏi xám bé xíu; đèn rọi vào; KHÔNG có chú cánh cụt nơ đỏ trong cảnh này.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng ở Nam Cực, sỏi không hề rẻ. Chỉ khoảng 2% lục địa này là không bị băng phủ.". Bố cục: Bản đồ lục địa Nam Cực hoạt hình nhìn từ trên: gần như toàn bộ phủ băng trắng, chỉ có vài mảng đá nâu xám nhỏ xíu dọc bờ biển được khoanh tròn đỏ; một chiếc kính lúp ở GIỮA-PHẢI soi vào một mảng đá. KHÔNG có chú cánh cụt nơ đỏ trong cảnh này.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi mùa xuân, hàng triệu chú cánh cụt Adélie kéo nhau lên đúng những bãi đá hiếm hoi ấy để xây tổ.". Bố cục: Một đoàn cánh cụt Adélie đông nghịt nối đuôi nhau lạch bạch đi từ biển băng lên một bãi đá trống, kéo dài tới tận chân trời, con nào cũng hăm hở.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và tổ của chúng không làm bằng cỏ, không làm bằng lông, mà làm bằng sỏi.". Bố cục: Chia 3 ô: BÊN TRÁI tổ cỏ bị gạch chéo đỏ, Ở GIỮA tổ lông vũ bị gạch chéo đỏ, BÊN PHẢI một cái tổ tròn xếp bằng sỏi xám có dấu tích xanh lá to.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trung bình mỗi tổ cần khoảng 200 viên. Tức là một con chim nặng bằng con mèo phải tự tay, à không, tự mỏ, khuân 200 viên đá về nhà!". Bố cục: chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ ngậm một viên sỏi trong mỏ, mồ hôi nhễ nhại, cạnh một đống sỏi cao như núi nhỏ BÊN PHẢI; BÊN TRÁI là con mèo nhà ngồi nhìn ngạc nhiên để so sánh: con chim nặng bằng con mèo mà phải khuân cả núi đá.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và thế là tội ác bắt đầu! Hàng xóm vừa quay lưng. Quý ông Vest Đuôi Tôm rón rén bước tới.". Bố cục: Bãi đá với nhiều tổ sỏi: BÊN TRÁI một chú cánh cụt hàng xóm (không đeo nơ) đang quay lưng ngắm biển; BÊN PHẢI chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ đeo mặt nạ kẻ trộm đen che mắt, nhón chân rón rén tiến tới tổ hàng xóm.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ngoạm một viên! Quay về tổ! Đặt xuống! Lại rón rén đi tiếp!". Bố cục: chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ ngậm một viên sỏi, chạy lạch bạch thật nhanh với vệt chuyển động phía sau, từ tổ hàng xóm BÊN TRÁI về tổ của mình BÊN PHẢI, mũi tên nét đứt chỉ đường đi.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Có kẻ trộm xong còn đứng ngay sau lưng nạn nhân để chọn viên thứ hai!". Bố cục: chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ đứng ngay sau lưng một chú cánh cụt hàng xóm đang ngủ gật trên tổ, một cánh đặt lên cằm như đang lựa chọn, mắt nheo nhìn viên sỏi đẹp nhất trong tổ của nạn nhân.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nạn nhân phát hiện thì sao? Mổ! Đập cánh! Rượt đuổi vòng quanh bãi đá! Một cuộc rượt đuổi tốc độ cao... 2km/h.". Bố cục: Cuộc rượt đuổi vòng quanh bãi đá: một chú cánh cụt hàng xóm giận dữ (không đeo nơ) giơ cánh đuổi theo chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ đang ngậm sỏi bỏ chạy; cả hai chạy rất chậm như quay chậm, bên cạnh có một con ốc sên đang vượt qua họ.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Điều buồn cười nhất là: kẻ trộm giỏi nhất lại chính là kẻ canh nhà kỹ nhất. Các nhà làm phim tài liệu đã quay được một gã vừa đi trộm khắp nơi, vừa đứng gác tổ mình như bảo vệ ngân hàng. Bởi vì gã biết rõ hơn ai hết: ở đây, ai cũng là trộm!". Bố cục: chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ đội mũ bảo vệ, cầm đèn pin, đứng gác cái tổ sỏi của mình như bảo vệ ngân hàng, mắt đảo nghi ngờ; BÊN TRÁI một nhóm làm phim tài liệu (người cầm máy quay) đang lén quay lại.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bồi thẩm đoàn thử tưởng tượng: cả một khu phố 5 triệu dân, nhà nào cũng thiếu gạch, và ai cũng đang lén lấy gạch nhà bên cạnh. Cứ đà này, có khi một viên sỏi đi một vòng khắp xóm rồi lại quay về đúng cái tổ ban đầu!". Bố cục: Nhìn từ trên cao: một vòng tròn khổng lồ gồm rất nhiều tổ sỏi, mỗi chú cánh cụt đều đang lén lấy sỏi của tổ bên cạnh, các mũi tên nhỏ nối thành một vòng xoay; ở giữa vòng tròn có một viên sỏi phát sáng đi theo đường nét đứt quay về đúng tổ ban đầu.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn ở họ hàng nhà cánh cụt Gentoo, chàng trai mang viên sỏi đẹp nhất tặng bạn đời như tặng nhẫn kim cương. Ở Nam Cực, không có sỏi thì đừng mơ lấy vợ!". Bố cục: Một chú cánh cụt Gentoo (mỏ cam đỏ, vệt trắng trên đỉnh đầu, chân cam) quỳ một chân, hai cánh dâng lên một viên sỏi tròn bóng lấp lánh như nhẫn kim cương cho một cô cánh cụt Gentoo đang ôm má e thẹn, trái tim bay quanh.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thưa tòa, cháu không trộm! Cháu chỉ... mượn vĩnh viễn thôi ạ!". Bố cục: Trong vành móng ngựa: chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ chắp hai cánh trước ngực làm mặt ngây thơ, mắt to long lanh; phía sau lưng chú lộ ra một viên đá xám tròn nhỏ; BÊN PHẢI ngài thẩm phán hải mã (walrus) già đội tóc giả trắng xoăn, cầm búa gỗ nhướng một bên mày, mỉm cười hài hước.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bồi thẩm đoàn đã nghe rồi đấy. Mượn vĩnh viễn! Công tố viên đề nghị ghi nhận: bị cáo có hành vi chiếm đoạt sỏi một cách có hệ thống, có tổ chức, và có cả kỹ năng nhìn trước ngó sau chuyên nghiệp. Bằng chứng số 1, kết thúc.". Bố cục: chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ đứng trước bức tường đo chiều cao kiểu chụp ảnh can phạm (chỉ có vạch kẻ ngang, không số), hai cánh ôm một viên sỏi, mặt phụng phịu; đèn flash máy ảnh lóe sáng.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bằng chứng số 2. Hiện trường: mép băng, lúc chiều tà. Hàng trăm chú cánh cụt đứng chen chúc sát mép nước.". Bố cục: Mép băng lúc chiều tà, trời cam tím: hàng trăm chú cánh cụt Adélie đứng chen chúc sát mép tảng băng nhìn xuống làn nước biển xanh thẫm phía dưới.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ai cũng đói. Ai cũng muốn xuống biển bắt cá và tôm nhỏ. Nhưng... không ai chịu nhảy trước. Vì sao ư?". Bố cục: Cận cảnh vài chú cánh cụt trên mép băng ôm bụng đói, bong bóng suy nghĩ phía trên vẽ cá bạc và tôm nhỏ màu hồng; nhưng các ngón chân dừng sát mép băng, run run, không ai dám bước; chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ đứng ở hàng giữa.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vì dưới làn nước tối kia... có thể có thứ gì đó đang chờ.". Bố cục: Mặt cắt ngang tảng băng và biển: phía trên là chân các chú cánh cụt sát mép, phía dưới mặt nước tối om có một cái bóng to lớn mờ mờ với hai con mắt phát sáng đang rình. KHÔNG có chú cánh cụt nơ đỏ trong cảnh này.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hải cẩu báo! Dài tới 3,5m! Nặng tới 500kg! Bơi nhanh 40km/h!". Bố cục: Một con hải cẩu báo (leopard seal) hoạt hình to dài, thân thon màu xám bạc có đốm đen, đầu to như đầu rắn, nằm dọc khung hình; một chiếc thước dây vàng kéo từ mũi tới đuôi. KHÔNG có chú cánh cụt nơ đỏ trong cảnh này.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cái đầu to như đầu rắn! Hàm đầy răng nanh dài!". Bố cục: Cận cảnh đầu hải cẩu báo há miệng rộng (không máu, phong cách hài), lộ hàm răng nanh dài nhọn trắng, mắt láu cá. KHÔNG có chú cánh cụt nơ đỏ trong cảnh này.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó nấp ngay dưới mép băng, chỉ ló mỗi cái mũi! Chờ đúng khoảnh khắc một chú cánh cụt chạm nước!". Bố cục: Mặt cắt mép băng: hải cẩu báo nấp sát dưới mép băng, chỉ ló mỗi cái mũi trên mặt nước; phía trên mép băng các chú cánh cụt chưa hề hay biết.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "So với Quý ông Vest Đuôi Tôm nặng bằng con mèo, đây là một chiếc xe tải có răng!". Bố cục: So sánh hài hước: BÊN TRÁI chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ bé xíu; BÊN PHẢI hải cẩu báo được vẽ như một chiếc xe tải có bánh xe và hàm răng nanh to đùng, cười nhe răng.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và thế là cảnh tượng kỳ lạ nhất Nam Cực diễn ra. Cả bầy chen tới, chen lui, huých nhau, ủn nhau.". Bố cục: Đám đông cánh cụt trên mép băng chen chúc huých nhau, ủn nhau, cánh vung loạn xạ, mặt hoảng hốt, giống giờ tan tầm; chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ kẹt ở giữa đám đông.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Con đứng hàng đầu cố bám chân lại. Mấy con phía sau cứ thế mà dồn lên.". Bố cục: Một chú cánh cụt (không đeo nơ) đứng hàng đầu đang ngả người ra sau, hai chân bấu chặt mép băng, hai cánh chới với; phía sau mấy chú khác dồn lên ép tới.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và rồi... tõm! Một bạn xui xẻo rơi xuống nước!". Bố cục: Chú cánh cụt xui xẻo (không đeo nơ) rơi tõm xuống nước tạo cột nước bắn tung tóe hình vương miện, chữ tượng thanh được thay bằng các tia nước to.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cả bầy lập tức nín thở, nghển cổ nhìn theo như khán giả xem phim kinh dị.". Bố cục: Cả bầy cánh cụt trên mép băng nghển cổ nhìn xuống nước, mắt mở to nín thở như khán giả xem phim kinh dị, có con ôm hộp bỏng ngô, có con che mắt hé nhìn; chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ cắn móng cánh.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu bạn ấy bơi đi bình an, cả hội ào ào nhảy theo như đi tắm biển ngày hè!". Bố cục: Chú cánh cụt dưới nước vẫy cánh vui vẻ bình an; phía trên cả bầy ào ào nhảy xuống theo như đi tắm biển ngày hè, có con đeo kính bơi, có con mang phao vịt.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn nếu không... thì cả bầy lùi lại, đứng chờ thêm một lúc nữa.". Bố cục: Cả bầy cánh cụt lùi lại xa mép băng một bước, đứng thành hàng lo lắng, mồ hôi rơi, nhìn đồng hồ cát; mặt nước phía trước chỉ còn bong bóng (không có cảnh bạo lực); chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ đứng ở cuối hàng.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhân chứng của vụ án này là một người rất đặc biệt. Năm 1911, bác sĩ Levick của đoàn thám hiểm Nam Cực nước Anh đã sống gần 1 năm ở Cape Adare, ngày ngày ngồi quan sát từng chú cánh cụt Adélie.". Bố cục: Năm 1911: một bác sĩ thám hiểm người Anh hoạt hình, râu mép, mặc áo lông thú dày và mũ len, ngồi trên thùng gỗ cạnh túp lều gỗ phủ tuyết, cầm sổ tay và bút chì quan sát đàn cánh cụt Adélie; phong cách hơi cổ điển màu nâu sepia nhẹ.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ông ghi lại cảnh chúng đứng trên mép băng, né qua né lại, và cố đẩy nhau xuống nước. Xin mời nhân chứng.". Bố cục: Trang sổ tay mở rộng với hình phác thảo bằng bút chì: các chú cánh cụt né qua né lại trên mép băng và đẩy nhau xuống nước, có mũi tên phác thảo; bàn tay bác sĩ cầm bút chì đang vẽ.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mấy con đứng sau suýt đẩy được hàng đầu xuống nước, thế là hàng đầu vòng ra phía sau để đẩy lại!". Bố cục: Vòng tròn hài hước: những chú cánh cụt hàng đầu suýt rơi liền chạy vòng ra phía sau đám đông để đẩy lại, tạo thành một vòng xoay vô tận có mũi tên tròn; một ông lão nhân chứng râu bạc ở góc trái kể lại, tay chỉ vào.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bồi thẩm đoàn nghe rõ chưa? Vòng ra phía sau để đẩy lại! Đây không còn là đi bơi nữa, đây là trò kéo co ngược chiều! Thua thì làm vật thí nghiệm, thắng thì được đi ăn trưa an toàn. Bằng chứng số 2, cực kỳ nghiêm trọng!". Bố cục: Trò kéo co ngược chiều: hai đội cánh cụt đứng hai bên mép băng cố đẩy ngược nhau về phía nước; BÊN PHẢI một chú (không đeo nơ) thắng cuộc thong thả ăn con cá, BÊN TRÁI chú thua cuộc bơi dưới nước liếc nhìn lo lắng; chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ làm trọng tài thổi còi.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bằng chứng số 3: tấn công bằng vũ khí sinh học tầm xa. Thưa bồi thẩm đoàn, vũ khí đó... là phân. Chim cánh cụt ấp trứng nhiều ngày liền không rời tổ. Vậy nó đi vệ sinh ở đâu? Rất đơn giản.". Bố cục: chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ nằm ấp trứng trên tổ sỏi, mặt kiên nhẫn mệt mỏi, xung quanh các tờ lịch bay vèo vèo thể hiện nhiều ngày trôi qua, tuyết rơi trên đầu; BÊN PHẢI một chiếc khăn phủ che một 'vũ khí' bí ẩn hình ống.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó đứng dậy, quay lưng ra mép tổ, nhấc đuôi lên, và... bắn! Một vệt trắng hồng phóng thẳng ra ngoài.". Bố cục: Phong cách hoạt hình hài nhẹ nhàng, thân thiện trẻ em: chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ đứng ở mép tổ, quay lưng ra ngoài, chổng đuôi lên, phóng ra một vệt chất lỏng trắng hồng thành đường vòng cung bay xa như vòi nước, vẻ mặt tỉnh bơ; quả trứng trong tổ vẫn sạch sẽ.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cứ thế, quanh mỗi cái tổ là những tia vệt tỏa ra như tia nắng mặt trời. Nhìn từ trên cao, cả bãi đá giống hệt một bức tranh vẽ bằng súng sơn!". Bố cục: Nhìn từ trên cao: nhiều cái tổ sỏi tròn, quanh mỗi tổ có các vệt trắng hồng tỏa ra đều như tia nắng mặt trời hoặc như vết súng sơn, tạo thành một bức tranh hoa văn đẹp mắt trên bãi đá.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chuyện nghe thì buồn cười, nhưng các nhà khoa học đã tính toán hẳn hoi. Năm 2003, 2 nhà khoa học đo độ dài vệt phân quanh tổ, rồi dùng công thức vật lý tính ra áp suất bên trong bụng chim cánh cụt.". Bố cục: Hai nhà khoa học hoạt hình mặc áo khoác đỏ, một người quỳ cầm thước dây đo độ dài một vệt trắng hồng trên tuyết, người kia cầm máy tính bỏ túi và bảng kẹp giấy với công thức vẽ nguệch ngoạc (không chữ đọc được); một chú cánh cụt đứng nhìn ngơ ngác.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kết quả: 10-60 kPa! Mạnh gấp mấy lần lúc con người đi vệ sinh, cỡ một nửa áp suất lốp xe hơi!". Bố cục: BÊN TRÁI một chú cánh cụt với chiếc đồng hồ đo áp suất to dán bên cạnh, kim vọt lên vùng đỏ; BÊN PHẢI một chiếc lốp xe hơi với đồng hồ đo áp suất kim cao gấp đôi; dấu bằng một nửa ở giữa.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Công trình này còn đoạt giải Ig Nobel năm 2005, giải thưởng dành cho những nghiên cứu khiến người ta bật cười trước, rồi mới suy nghĩ sau.". Bố cục: Lễ trao giải vui nhộn: hai nhà khoa học trên sân khấu cầm chiếc cúp hình chú cánh cụt vàng, khán giả bên dưới cười nghiêng ngả, pháo giấy bay.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa hết! Năm 2020, 2 nhà khoa học Nhật Bản tính lại trên loài cánh cụt Humboldt! Lần này tính cả góc bắn! Cả sức cản không khí! Cả độ sệt của phân!". Bố cục: Hai nhà khoa học Nhật Bản hoạt hình đeo kính đứng cạnh tấm bảng trắng vẽ một đường parabol và các mũi tên lực (không chữ); BÊN PHẢI một chú cánh cụt Humboldt (mặt có mảng da hồng quanh mỏ, một vạch đen ngang ngực) đứng trên tảng đá.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kết quả: tầm bắn xa nhất 1,34m! Tốc độ gần 8km/h!". Bố cục: Chú cánh cụt Humboldt đứng trên tảng đá BÊN TRÁI, một đường vòng cung nét đứt bay sang BÊN PHẢI đáp xuống cạnh một lá cờ cắm trên đất; một thước dây vàng kéo dài bên dưới dọc theo đường bay.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu đổi sang cỡ người, đó là bắn xa hơn 3m!". Bố cục: So sánh quy mô: BÊN TRÁI một chú cánh cụt nhỏ với đường vòng cung ngắn; BÊN PHẢI một người đàn ông hoạt hình đứng cạnh một đường vòng cung khổng lồ dài gấp nhiều lần chạm tới lá cờ xa, ông ta ôm mặt ngượng ngùng; phong cách hài lịch sự.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và họ nghiêm túc khuyên nhân viên thủy cung: hãy đứng cách xa ít nhất 1,34m!". Bố cục: Một nhân viên thủy cung hoạt hình mặc áo mưa vàng, đội mũ bảo hộ, cầm ô che, đứng sau một vạch kẻ an toàn màu vàng đen trên sàn, cách xa một chú cánh cụt Humboldt đang chổng đuôi; mặt nhân viên cảnh giác buồn cười.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và vũ khí này mạnh tới mức... nhìn thấy được từ ngoài vũ trụ!". Bố cục: Không gian vũ trụ: một vệ tinh nhân tạo có tấm pin mặt trời bay trên quỹ đạo, bên dưới là quả địa cầu nhìn thấy lục địa Nam Cực trắng xóa; ống kính vệ tinh chiếu tia sáng xuống. KHÔNG có chú cánh cụt nơ đỏ trong cảnh này.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Năm 2012, các nhà khoa học Anh soi ảnh vệ tinh dọc bờ biển Nam Cực, tìm những mảng màu nâu trên nền băng trắng. Mảng nâu đó chính là phân chim cánh cụt!". Bố cục: Các nhà khoa học hoạt hình ngồi trước màn hình máy tính lớn hiển thị ảnh vệ tinh: nền băng trắng có những mảng màu nâu đỏ được khoanh tròn; một người chỉ tay ngạc nhiên, người kia cầm cốc trà.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lần theo dấu vết ấy, họ tìm ra 46 đàn cánh cụt hoàng đế, họ hàng to xác của bị cáo, và đếm được khoảng 595.000 con, gần gấp đôi con số người ta từng nghĩ.". Bố cục: Một đàn cánh cụt hoàng đế khổng lồ (to cao, mảng vàng cam ở cổ và má, mỏ dài có vạch cam) đứng đông nghịt tới tận chân trời trên băng, cạnh đàn là một mảng màu nâu; vài chú con lông xám đứng giữa chân bố mẹ.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bồi thẩm đoàn thấy chưa: đi đâu cũng để lại dấu vết, lộ cả trên ảnh vệ tinh! Đây là băng nhóm bất cẩn nhất lịch sử!". Bố cục: Một tấm ảnh vệ tinh khổng lồ treo trong tòa như tấm áp phích truy nã, trên ảnh là một vệt nâu chỉ thẳng tới một băng nhóm cánh cụt đang ngơ ngác; phía trước chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ lấy cánh che mặt xấu hổ.
```
</details>

<details><summary>L57</summary>

```text
HÌNH L57 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bằng chứng số 4: hành hung người đang làm nhiệm vụ. Nạn nhân là... các nhà khoa học. Khi nhà nghiên cứu cúi xuống gần tổ để cân chim non, Quý ông Vest Đuôi Tôm không hề bỏ chạy.". Bố cục: Một nhà nghiên cứu hoạt hình mặc áo khoác cam, quỳ xuống cạnh tổ sỏi cầm một chiếc cân treo nhỏ định cân chú cánh cụt con lông xám; chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ đứng phắt dậy, mắt trợn giận dữ, lông dựng.
```
</details>

<details><summary>L58</summary>

```text
HÌNH L58 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó lao tới, đứng thẳng người, và tát! Bằng đôi cánh cứng như mái chèo! Phạch! Phạch! Phạch!". Bố cục: chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ đứng thẳng người, vung cánh tát mạnh vào ống chân nhà nghiên cứu, các tia sao va chạm và vệt chuyển động; nhà nghiên cứu nhảy lò cò ôm chân, mặt méo xệch hài hước.
```
</details>

<details><summary>L59</summary>

```text
HÌNH L59 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cánh chim cánh cụt không bay được, nhưng xương cánh dẹt và đặc, quất vào ống chân thì đau như bị cô giáo gõ thước kẻ.". Bố cục: Hình mặt cắt kỹ thuật kiểu sách giáo khoa: chiếc cánh cánh cụt dẹt như mái chèo, bên trong lộ xương dẹt đặc màu kem; BÊN PHẢI để so sánh là một cây thước kẻ gỗ và một mái chèo gỗ có hình dạng tương tự.
```
</details>

<details><summary>L60</summary>

```text
HÌNH L60 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không chỉ con người! Chim cướp biển Skua sải cánh rộng hơn 1m lượn tới định cướp trứng? Tát!". Bố cục: Một con chim cướp biển Skua nâu sải cánh rộng sà xuống định cướp quả trứng; chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ nhảy lên vung cánh tát vào mỏ nó, lông Skua bay tán loạn.
```
</details>

<details><summary>L61</summary>

```text
HÌNH L61 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hải cẩu bò lên quá gần? Tát! Hàng xóm lấn sang nửa bước? Tát luôn!". Bố cục: Chia đôi khung: BÊN TRÁI chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ tát một con hải cẩu lông nâu đang bò lại quá gần tổ khiến nó giật mình lùi lại; BÊN PHẢI chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ tát luôn một chú cánh cụt hàng xóm vừa lấn sang nửa bước.
```
</details>

<details><summary>L62</summary>

```text
HÌNH L62 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cả đời bị cáo chỉ có 2 chế độ: đứng im dễ thương, và tát không cần báo trước!". Bố cục: Chia đôi khung có nút công tắc ở giữa: BÊN TRÁI chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ đứng im dễ thương, má hồng, trái tim bay quanh; BÊN PHẢI cùng chú cánh cụt đó mắt đỏ rực, cánh vung tát ra liên tục như cánh quạt.
```
</details>

<details><summary>L63</summary>

```text
HÌNH L63 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và đừng tưởng bị cáo chậm chạp. Trên cạn, nó đi lạch bạch như ông cụ đi chợ.". Bố cục: chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ đi lạch bạch trên băng như ông cụ đi chợ, khoác giỏ đi chợ trên cánh, chậm rãi; phía sau là một con ốc sên đi cùng tốc độ.
```
</details>

<details><summary>L64</summary>

```text
HÌNH L64 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng xuống nước thì như tên lửa: bơi 15km/h, lặn sâu tới 180m,". Bố cục: Dưới nước xanh: chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ lao đi như tên lửa ngư lôi với vệt bọt khí dài phía sau, đuổi theo đàn cá bạc; bên trái có thang đo độ sâu vẽ vạch xuống tận đáy tối.
```
</details>

<details><summary>L65</summary>

```text
HÌNH L65 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "và khi phóng lên, nó có thể bật một cú nhảy cao tới 2m, đáp thẳng lên tảng băng! Trên bờ là diễn viên hài, dưới nước là đặc vụ!". Bố cục: chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ phóng vọt khỏi mặt nước, bay cao lên theo đường cong và đáp gọn lên mặt một tảng băng cao, tư thế ngầu như đặc vụ đeo kính râm; một thước đo chiều cao dựng cạnh tảng băng.
```
</details>

<details><summary>L66</summary>

```text
HÌNH L66 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Công tố viên xin tổng kết. Trộm sỏi. Đẩy bạn xuống nước. Nã súng phân xa 1,34m. Và tát cả nhà khoa học!". Bố cục: ông công tố viên hoạt hình đeo kính tròn, mặc áo choàng đen đứng BÊN TRÁI giơ tay chỉ mạnh vào bảng ghim 4 bằng chứng BÊN PHẢI: viên sỏi, cú rơi xuống nước, vệt bắn hồng trắng, cú tát vào ống chân; chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ ở góc dưới phải toát mồ hôi.
```
</details>

<details><summary>L67</summary>

```text
HÌNH L67 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ngay cả nhân chứng Levick năm xưa cũng gọi những chú chim trẻ hay gây rối là... lũ du côn!". Bố cục: Ông bác sĩ thám hiểm năm 1911 (râu mép, áo lông thú) cau mày nhìn một nhóm cánh cụt Adélie trẻ nghịch ngợm mặc áo khoác da, đội mũ lưỡi trai ngược, đang xô đẩy nhau phá phách trên bãi đá.
```
</details>

<details><summary>L68</summary>

```text
HÌNH L68 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ông còn viết một số trang nhật ký bằng chữ cái Hy Lạp để người khác không đọc được.". Bố cục: Ông bác sĩ thám hiểm năm 1911 ngồi trong lều gỗ dưới ánh đèn dầu, lén lút che một trang nhật ký bằng tay, trên trang có các ký hiệu ngoằn ngoèo bí ẩn bị một ổ khóa vẽ đè lên; vẻ mặt bí mật hài hước.
```
</details>

<details><summary>L69</summary>

```text
HÌNH L69 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bằng chứng đã đủ. Công tố viên đề nghị mức án cao nhất!". Bố cục: ông công tố viên hoạt hình đeo kính tròn, mặc áo choàng đen đập mạnh tập hồ sơ xuống bàn, giấy bay tứ tung; ngài thẩm phán hải mã (walrus) già đội tóc giả trắng xoăn, cầm búa gỗ trên bục nhìn xuống; chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ trong vành móng ngựa run cầm cập.
```
</details>

<details><summary>L70</summary>

```text
HÌNH L70 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khoan đã! Phản đối! Bây giờ, xin cho tôi cởi áo công tố viên, và khoác áo luật sư bào chữa. Bởi vì bồi thẩm đoàn mới chỉ nghe một nửa câu chuyện. Về bằng chứng số 1: vì sao phải trộm sỏi?". Bố cục: Người đàn ông hoạt hình đeo kính tròn đang cởi chiếc áo choàng đen công tố viên ném sang một bên và khoác lên bộ vest xanh dương của luật sư bào chữa, tay giơ ngón trỏ 'phản đối', vẻ mặt quyết tâm; tia sáng đổi vai phía sau.
```
</details>

<details><summary>L71</summary>

```text
HÌNH L71 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi mùa xuân, tuyết tan thành những dòng nước lạnh chảy tràn qua bãi đá.". Bố cục: Mùa xuân Nam Cực: tuyết tan thành những dòng nước lạnh xanh nhạt chảy tràn qua bãi đá làm tổ của đàn cánh cụt, tạo thành các vũng nước lớn.
```
</details>

<details><summary>L72</summary>

```text
HÌNH L72 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Quả trứng nằm sát mặt đất sẽ bị ngâm nước, lạnh cóng, rồi hỏng.". Bố cục: Một quả trứng cánh cụt hoạt hình có khuôn mặt dễ thương nằm sát mặt đất trong vũng nước lạnh, run cầm cập, quấn khăn len, băng giá bám quanh; cái tổ thấp lè tè bị nước tràn vào.
```
</details>

<details><summary>L73</summary>

```text
HÌNH L73 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một đống sỏi cao chính là chiếc bè cứu sinh, nâng quả trứng lên khỏi vũng nước. Tổ càng cao, trứng càng an toàn.". Bố cục: chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ ngồi ấp 2 quả trứng trên một đống sỏi cao như hòn đảo nhỏ giữa dòng nước tan, trứng khô ráo an toàn; các tổ thấp xung quanh bị ngập; có chiếc phao cứu sinh vẽ mờ như biểu tượng.
```
</details>

<details><summary>L74</summary>

```text
HÌNH L74 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thứ bị cáo trộm không phải của cải, mà là... cơ hội sống cho con mình. Về bằng chứng số 2:". Bố cục: chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ ôm hai quả trứng vào lòng trên tổ sỏi cao, ánh sáng vàng ấm áp tỏa quanh, trái tim nhỏ bay lên, khuôn mặt hiền hậu.
```
</details>

<details><summary>L75</summary>

```text
HÌNH L75 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nhiều nhà khoa học cho rằng phần lớn những cú rơi ở mép băng không phải âm mưu gì cả. Đó chỉ là cảnh chen lấn giờ cao điểm: bầy đông dồn lên, con đứng đầu bị đẩy ra mép, và thế là tõm.". Bố cục: Cảnh giờ cao điểm ở mép băng như ga tàu điện ngầm đông nghịt: hàng trăm chú cánh cụt dồn lên, một chú đầu hàng bị đẩy ra mép một cách vô tình, ai cũng ngơ ngác không cố ý.
```
</details>

<details><summary>L76</summary>

```text
HÌNH L76 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhảy theo bầy lại là cách sống sót tốt nhất, vì một con hải cẩu báo không thể bắt hết cả trăm con cùng lúc. Về bằng chứng số 3:". Bố cục: Hàng trăm chú cánh cụt cùng lúc lao xuống nước tỏa ra mọi hướng; ở giữa một con hải cẩu báo xoay vòng chóng mặt, mắt quay mòng mòng không biết đuổi con nào.
```
</details>

<details><summary>L77</summary>

```text
HÌNH L77 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bắn phân ra xa là để giữ tổ khô ráo, sạch sẽ cho trứng và con non. Đó là vệ sinh cá nhân... chỉ hơi mạnh tay một chút thôi! Còn bằng chứng số 4,". Bố cục: chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ cầm một cây chổi nhỏ quét tổ sỏi sạch bóng lấp lánh, chú cánh cụt con lông xám ngồi trong tổ khô ráo vui vẻ; các vệt trắng hồng nằm xa bên ngoài tổ.
```
</details>

<details><summary>L78</summary>

```text
HÌNH L78 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tát cả nhà khoa học? Bồi thẩm đoàn hãy nhìn kỹ: đó là một ông bố bé nhỏ, nặng bằng con mèo, dám đứng chắn trước mọi thứ to lớn hơn mình gấp nhiều lần, chỉ để bảo vệ 2 quả trứng.". Bố cục: chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ bé nhỏ dang hai cánh đứng chắn trước tổ có hai quả trứng; phía trước là ba cái bóng khổng lồ cao gấp nhiều lần: chim Skua, hải cẩu báo và một nhà khoa học; chú cánh cụt không lùi bước, ánh mắt kiên định.
```
</details>

<details><summary>L79</summary>

```text
HÌNH L79 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu đó là tội, thì đó là tội... làm bố quá tận tâm.". Bố cục: chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ làm bố ôm chú cánh cụt con lông xám vừa nở, hai bố con dụi má nhau, trái tim to màu đỏ phía sau, cảnh ấm áp cảm động.
```
</details>

<details><summary>L80</summary>

```text
HÌNH L80 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cộc cộc cộc! Tòa tuyên: bị cáo vô tội... nhưng phải trả lại viên sỏi!". Bố cục: ngài thẩm phán hải mã (walrus) già đội tóc giả trắng xoăn, cầm búa gỗ gõ búa xuống bàn có các vạch tượng thanh rung; phía dưới chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ trong vành móng ngựa thở phào nhẹ nhõm nhưng đang bị yêu cầu đưa trả lại một viên sỏi.
```
</details>

<details><summary>L81</summary>

```text
HÌNH L81 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và thế là Quý ông Vest Đuôi Tôm bước ra khỏi tòa, lạch bạch quay về tổ, trong mỏ ngậm... một viên sỏi mới nhặt của nhà bên cạnh.". Bố cục: chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ lạch bạch rời khỏi tòa án quay về tổ, trong mỏ ngậm một viên sỏi mới vừa nhặt từ tổ nhà bên cạnh, liếc mắt tinh nghịch; chú hàng xóm phía sau đang ngủ không hay biết.
```
</details>

<details><summary>L82</summary>

```text
HÌNH L82 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn bạn, nếu là bồi thẩm đoàn, bạn sẽ tuyên bị cáo có tội hay vô tội? Hãy viết phán quyết của bạn ở phần bình luận nhé!". Bố cục: Hàng ghế bồi thẩm đoàn các bạn nhỏ hoạt hình đa dạng đang giơ thẻ bài: một nửa thẻ hình ngón cái hướng lên màu xanh, một nửa thẻ hình ngón cái hướng xuống màu đỏ, vẻ mặt đang suy nghĩ hào hứng; không có chữ trên thẻ.
```
</details>

<details><summary>L83</summary>

```text
HÌNH L83 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tập sau, chúng ta sẽ rời tòa án để bước vào phòng khám, nơi một bệnh nhân đặc biệt đang chờ: Gấu Koala.". Bố cục: Phòng khám bác sĩ thú y hoạt hình sáng sủa: một chú gấu Koala lông xám, tai tròn bông xù, mũi đen to, ngồi trên ghế bệnh nhân mắt lờ đờ ngơ ngác, cạnh đó có ống nghe và tấm phim X-quang treo tường. KHÔNG có chú cánh cụt nơ đỏ trong cảnh này.
```
</details>

<details><summary>L84</summary>

```text
HÌNH L84 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bày sẵn đĩa lá ngon nhất ngay trước mặt, nhưng bệnh nhân này thà nhịn đói, vì bộ não của nó... không nhận ra đó là thức ăn. Hẹn gặp lại các bạn trong hồ sơ bệnh án tiếp theo!". Bố cục: Chú gấu Koala ngồi trước một chiếc đĩa sứ đầy lá bạch đàn xanh tươi đặt ngay trước mặt, nhưng nhìn chằm chằm vào chiếc đĩa với dấu chấm hỏi to trên đầu, bụng sôi òng ọc; KHÔNG có chú cánh cụt nơ đỏ trong cảnh này.
```
</details>

<details><summary>L85</summary>

```text
HÌNH L85 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mà bồi thẩm đoàn biết không, nhiều chàng cánh cụt năm nào cũng quay về xây tổ đúng chỗ cũ, mong cô bạn đời năm ngoái nhận ra nhà mà quay lại. Thế nên một cái tổ đẹp vừa là ngôi nhà, vừa là... tấm biển địa chỉ!". Bố cục: chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ đứng bên tổ sỏi đúng chỗ cũ, cạnh tổ cắm một hòm thư nhỏ hình ngôi nhà (không chữ); xa xa một cô cánh cụt Adélie đeo nơ hồng đang đi tới, bong bóng nghĩ của cô vẽ hình cái tổ năm ngoái giống hệt; trái tim nhỏ bay lên.
```
</details>

<details><summary>L86</summary>

```text
HÌNH L86 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tổ xấu quá thì sao? Cô nàng đi lướt qua luôn, coi như không quen biết!". Bố cục: Một chú cánh cụt (không đeo nơ) đứng cạnh cái tổ lèo tèo chỉ vài viên sỏi, mặt hi vọng; cô cánh cụt đeo nơ hồng ngẩng cao đầu đi lướt qua, mắt nhìn đi chỗ khác, vẻ coi như không quen biết; chú kia há mỏ thất vọng hài hước.
```
</details>

<details><summary>L87</summary>

```text
HÌNH L87 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn khi lười đi bộ trên tuyết? Bị cáo nằm sấp xuống, lấy cái bụng làm ván trượt, hai chân đạp phía sau, lướt vèo vèo như trẻ con chơi cầu trượt! Các nhà khoa học gọi đó là cách tiết kiệm sức.". Bố cục: chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ nằm sấp trên tuyết, lấy bụng trắng làm ván trượt, hai chân đạp phía sau tung tuyết, lướt vèo vèo xuống dốc với vệt tốc độ, mặt sung sướng như trẻ con chơi cầu trượt.
```
</details>

<details><summary>L88</summary>

```text
HÌNH L88 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn tòa án gọi đó là... tẩu thoát khỏi hiện trường bằng xe trượt riêng!". Bố cục: Hài hước: chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ trượt bụng trên tuyết thoát khỏi một tòa án băng phía sau, miệng ngậm một viên sỏi; phía sau một chú cảnh sát hải cẩu nhỏ đội mũ cảnh sát chạy đuổi theo hụt hơi, còi thổi.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Bị cáo, mời đứng lên!". Bố cục: Phòng xử án băng giá dọc: phía trên ngài thẩm phán hải mã (walrus) già đội tóc giả trắng xoăn, cầm búa gỗ gõ búa; phía dưới chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ trong vành móng ngựa gỗ, một cánh lén lút đẩy một chú cánh cụt khác về phía mép băng có nước biển xanh.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Chú chim cánh cụt mặc vest đuôi tôm này đang bị truy tố vì tội đẩy bạn xuống biển... để thử xem có hải cẩu báo hay không!". Bố cục: chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ mặc vest đuôi tôm đen bóng đứng ở mép băng, một cánh đẩy lưng một chú cánh cụt khác (không đeo nơ) đang chới với sắp rơi xuống nước; phía dưới nước thấp thoáng bóng hải cẩu báo.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Bị cáo chỉ cao 70cm, nặng ngang một con mèo nhà, đi lạch bạch như trẻ mẫu giáo.". Bố cục: chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ đứng cạnh một con mèo nhà màu cam cao gần bằng; phía sau thước đo chiều cao kẻ vạch; chú cánh cụt đi lạch bạch như trẻ mẫu giáo đeo cặp sách nhỏ.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Hiện trường: mép băng Nam Cực. Hàng trăm chú chim chen chúc, ai cũng đói, nhưng không ai chịu nhảy trước.". Bố cục: Mép băng Nam Cực dọc khung: hàng trăm chú cánh cụt chen chúc sát mép, ôm bụng đói, bong bóng nghĩ hình cá, nhưng không ai dám bước xuống nước.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Vì dưới nước là hải cẩu báo dài 3,5m, nặng 500kg, đang nấp sẵn!". Bố cục: Mặt cắt dọc: phía trên mép băng là chân các chú cánh cụt; phía dưới là con hải cẩu báo xám đốm đen dài to, đầu như rắn, há miệng lộ răng nanh, đang nấp rình.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Thế là chen lên, ủn tới, và... tõm! Một bạn xui xẻo rơi xuống trước.". Bố cục: Đám đông cánh cụt chen lấn ủn nhau, một chú (không đeo nơ) bị dồn rơi tõm xuống nước tạo cột nước bắn tung tóe.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Cả bầy nín thở nhìn theo.". Bố cục: Cả bầy cánh cụt nghển cổ nhìn xuống nước, mắt mở to, có con ôm bỏng ngô, có con che mắt; chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ cắn móng cánh.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Bạn ấy bơi đi an toàn? Cả hội ào ào nhảy theo như đi tắm biển!". Bố cục: Chú cánh cụt dưới nước vẫy cánh bình an, cả bầy ào ào nhảy xuống theo như đi tắm biển, có con đeo kính bơi, có con mang phao vịt.
```
</details>

<details><summary>S09</summary>

```text
HÌNH S09 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Chưa hết, bị cáo còn trộm sỏi nhà hàng xóm để xây tổ,". Bố cục: chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ đeo mặt nạ kẻ trộm ngậm một viên sỏi rón rén bỏ chạy khỏi tổ hàng xóm đang ngủ gật.
```
</details>

<details><summary>S10</summary>

```text
HÌNH S10 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "và bắn phân xa tới 1,34m!". Bố cục: Phong cách hoạt hình hài thân thiện trẻ em: chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ đứng trên tổ sỏi chổng đuôi phóng một vệt trắng hồng thành vòng cung bay xa, có thước dây vàng đo bên dưới tới lá cờ.
```
</details>

<details><summary>S11</summary>

```text
HÌNH S11 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "chỉ là chen lấn giờ cao điểm, ai đứng đầu hàng thì bị dồn xuống!". Bố cục: Cảnh giờ cao điểm ở mép băng như ga tàu điện đông nghịt: hàng trăm chú cánh cụt dồn lên, chú đầu hàng bị đẩy ra mép vô tình, ai cũng ngơ ngác.
```
</details>

<details><summary>S12</summary>

```text
HÌNH S12 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Vậy bị cáo có tội hay vô tội? Xem trọn phiên tòa trong video dài ngay bên dưới, vì bị cáo này...". Bố cục: Cận cảnh chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ trong vành móng ngựa ngước nhìn thẳng ra người xem với đôi mắt to long lanh ngây thơ, hai cánh ôm một viên sỏi sau lưng, ngài thẩm phán hải mã (walrus) già đội tóc giả trắng xoăn, cầm búa gỗ cầm búa phía sau lưỡng lự.
```
</details>

<details><summary>S13</summary>

```text
HÌNH S13 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Nhưng khoan, nhiều nhà khoa học nói đây không phải âm mưu,". Bố cục: Một nhà khoa học hoạt hình mặc áo khoác đỏ cầm kính lúp quan sát đám cánh cụt ở mép băng, giơ một tay ra hiệu 'khoan đã'; chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ đứng cạnh gật gù đồng ý, vẻ mặt được minh oan.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/84 của video YouTube về Chim Cánh Cụt). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ. Nhân vật phụ cố định: ngài thẩm phán hải mã (walrus) già đội tóc giả trắng xoăn, cầm búa gỗ; ông công tố viên hoạt hình đeo kính tròn, mặc áo choàng đen. HÌNH L01 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nam Cực. -40°C. Gió rít qua những tảng băng trắng xóa...". Bố cục: Toàn cảnh Nam Cực trong bão tuyết: núi băng trắng xanh, gió cuốn tuyết thành vệt, bầu trời xám. BÊN PHẢI cắm một chiếc nhiệt kế khổng lồ đóng băng, cột đỏ tụt xuống tận đáy. KHÔNG có chú cánh cụt nơ đỏ trong cảnh này.
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/13 của video YouTube Shorts về Chim Cánh Cụt). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ. Nhân vật phụ: ngài thẩm phán hải mã (walrus) già đội tóc giả trắng xoăn, cầm búa gỗ. HÌNH S01 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú cánh cụt Adélie đen trắng, vòng trắng quanh mắt, nơ bướm đỏ ở cổ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Bị cáo, mời đứng lên!". Bố cục: Phòng xử án băng giá dọc: phía trên ngài thẩm phán hải mã (walrus) già đội tóc giả trắng xoăn, cầm búa gỗ gõ búa; phía dưới chú chim cánh cụt Adélie hoạt hình nhỏ nhắn tròn trịa: đầu và lưng đen tuyền, bụng trắng, quanh mỗi mắt có vòng trắng tròn nổi bật, mắt to long lanh biểu cảm, mỏ ngắn màu đen, chân hồng cam, đeo một chiếc nơ bướm đỏ nhỏ ở cổ trong vành móng ngựa gỗ, một cánh lén lút đẩy một chú cánh cụt khác về phía mép băng có nước biển xanh.
```
</details>

## 7. SEO

- **title:** Đẩy Bạn Xuống Biển Để Thử Hải Cẩu Báo?! | Chim Cánh Cụt | Tập 9
- **hook_paragraph:** Chim cánh cụt Adélie cao chưa tới 70cm, nặng như một con mèo, nhưng bị đưa ra tòa với 4 bằng chứng: trộm sỏi nhà hàng xóm, đẩy bạn xuống biển thử hải cẩu báo, bắn phân xa 1,34m với áp suất 10-60 kPa (giải Ig Nobel 2005) và tát cả nhà khoa học! Phiên tòa hài hước nhất Nam Cực — bị cáo có tội hay vô tội?
- **question:** Nếu bạn là bồi thẩm đoàn, bạn tuyên chim cánh cụt CÓ TỘI hay VÔ TỘI? Bình luận phán quyết của bạn nhé!
- **next_teaser:** Gấu Koala — bày sẵn đĩa lá trước mặt nhưng thà nhịn đói vì... não không nhận ra
- **shorts_title:** Đẩy Bạn Xuống Biển Để Thử Hải Cẩu?! 🐧 #shorts #chimcanhcut
- **shorts_desc:** Chim cánh cụt bị đưa ra tòa vì tội đẩy bạn xuống biển để thử xem có hải cẩu báo 500kg hay không! 🐧⚖️
👉 Xem trọn phiên tòa với 4 bằng chứng — video Tập 9 trên kênh Vẽ Chuyện Hoang Dã.
- **bullets:** Bằng chứng #1: mỗi tổ cần ~200 viên sỏi — và ai cũng đi trộm của hàng xóm · Bằng chứng #2: chen nhau ở mép băng, ai rơi xuống trước thì 'dò' hải cẩu báo 500kg · Bằng chứng #3: súng phân bắn xa 1,34m, nhìn thấy cả từ ảnh vệ tinh · Bằng chứng #4: tát cả nhà khoa học bằng đôi cánh cứng như mái chèo
- **tags:** chim cánh cụt, chim canh cut, penguin, adelie penguin, cánh cụt adelie, chim cánh cụt trộm sỏi, chim cánh cụt đẩy bạn xuống nước, hải cẩu báo, leopard seal, nam cực, penguin poop pressure, ig nobel, thế giới động vật, động vật hài hước, vẽ chuyện hoang dã, whiteboard animation, khoa học thú vị, dạy bé về động vật
- **hashtags:** #ChimCanhCut #Penguin #TheGioiDongVat #VeChuyenHoangDa #KhoaHoc

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-09-chim-canh-cut
python src/episode/pipeline.py tts    projects/tap-09-chim-canh-cut     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-09-chim-canh-cut     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-09-chim-canh-cut     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-09-chim-canh-cut              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-09-chim-canh-cut --force
python scripts/beat_sheet.py projects/tap-09-chim-canh-cut               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-09-chim-canh-cut/audio/shorts.wav projects/tap-09-chim-canh-cut/renders/tap-09-chim-canh-cut_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-09-chim-canh-cut
python src/episode/pipeline.py seo    projects/tap-09-chim-canh-cut
python src/episode/episode_doc.py     projects/tap-09-chim-canh-cut
```
