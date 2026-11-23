# TẬP 46 — LỢN HƯƠU BABIRUSA · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-46-lon-huou-babirusa`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-46-lon-huou-babirusa`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F1` · **Persona giọng:** `bac_si` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Lợn Hươu Babirusa |
| Tiêu đề YouTube | Nghịch Lý Tiến Hóa Tự Sát: Cặp Răng Nanh Tự Đâm Thủng Hộp Sọ?! \| Lợn Hươu Babirusa \| Tập 46 |
| Video dài | `renders/tap-46-lon-huou-babirusa_long.mp4` — 8:45.5 (525.5s) |
| Shorts | `renders/tap-46-lon-huou-babirusa_shorts.mp4` — 0:42.2 (42.2s) |
| Thumbnail | `renders/tap-46-lon-huou-babirusa_thumbnail.jpg` |
| Số hình | dài 56 beat / 56 ảnh riêng; Shorts 8 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.1**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/56 của video YouTube về Lợn Hươu Babirusa). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa vẽ tay đặc trưng cho chủ đề, nét mực sắc nét, màu sắc tương phản cuốn hút, tối giản giàu tính biểu tượng khoa học; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — BỆNH ÁN SỐ 46 — BÁC SĨ CHẤN ĐỘNG TRƯỚC CA PHẪU THUẬT RĂNG NANH MỌC NGƯỢC
*Thẻ chương:* BỆNH ÁN PHÁP Y ĐẶC BIỆT TIẾP NHẬN SINH VẬT CÓ VŨ KHÍ TỰ SÁT

*Badge:* `HỒ SƠ BỆNH ÁN` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene01_p0.wav` (443 ký tự) · mood `hao_hung`

```text
Khẩn cấp mở cửa phòng phẫu thuật pháp y sinh học hoang dã! Y tá đâu, chuẩn bị ngay cho tôi bộ kẹp kim loại titan, cưa xương phẫu thuật và máy chụp cắt lớp sọ não ba chiều đa tầng lập tức! Bệnh nhân tiếp theo của chúng ta hôm nay là một ca bệnh giải phẫu chấn động bậc nhất giới động vật có vú: Một sinh vật sống tại vùng rừng nhiệt đới đảo Sulawesi của đất nước Indonesia, mang trên mình một bản án tử hình sinh học do chính tạo hóa lập trình!
```
**Part 1** → `audio/vs/scene01_p1.wav` (111 ký tự) · 🎭 cameo `co_tro_ly`

```text
Bác sĩ ơi, bệnh nhân này vừa bước vào cửa mà hai cái răng trên mặt nó đã đâm thủng cả tấm rèm phòng khám rồi ạ!
```
**Part 2** → `audio/vs/scene01_p2.wav` (494 ký tự) · mood `hao_hung`

```text
[surprise-wa] Cô trợ lý chớ vội hoảng sợ! Hãy để tôi đọc to bệnh án số bốn mươi sáu: Sinh vật kỳ quặc này có tên là Babirusa, hay còn gọi là Lợn Hươu! Nhưng trong giới y khoa nghiên cứu tiến hóa, chúng tôi gọi gã bằng một biệt danh đầy rùng mình: Gã bệnh nhân tự sát tiến hóa! [laughter] Trong khi mọi loài thú có răng nanh trên Trái Đất đều dùng nanh để xé thịt con mồi hoặc tự vệ chống lại kẻ thù, thì cặp răng nanh của gã bạn này lại mọc ngược theo một quỹ đạo tự hủy diệt không thể tin nổi!
```
**Part 3** → `audio/vs/scene01_p3.wav` (501 ký tự) · mood `tram_bi_an`

```text
Nhìn vào khối cơ thể lực lưỡng nặng gần một trăm ki-lô-gam với đôi chân thon dài như loài hươu rừng, bạn sẽ thấy một vẻ đẹp dũng mãnh và hoang dã. Nhưng khi phóng to góc máy vào phần đầu của gã, toàn bộ bác sĩ sẽ phải rùng mình: Bốn chiếc răng nanh khổng lồ mọc tua tủa quanh miệng, trong đó hai chiếc răng hàm trên mọc xuyên thủng thịt mũi rồi uốn cong ngược trở lại, nhắm thẳng vào chính giữa hộp sọ của chủ nhân! Hãy cùng chúng tôi đặt tấm phim chẩn đoán lên bàn mổ để vén màn bí ẩn kinh hoàng này!
```

### scene02 — GIẢI PHẪU DỊ TẬT — CẶP RĂNG NANH HÀM TRÊN XOAY 180 ĐỘ ĐÂM XUYÊN DA MÕM
*Thẻ chương:* GIẢI MÃ CƠ CHẾ RĂNG XOAY MỘT TRĂM TÁM MƯƠI ĐỘ ĐÂM XUYÊN MÕM

*Badge:* `GIẢI PHẪU DỊ TẬT` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene02_p0.wav` (470 ký tự) · mood `don_dap`

```text
Hãy đặt tấm phim chụp cắt lớp vi tính xương sọ của Gã bệnh nhân tự sát tiến hóa lên màn hình! Điều đầu tiên khiến toàn thể hội đồng giám định y khoa phải dụi mắt bàng hoàng: Hãy nhìn vào chân răng của hàm trên! Ở tất cả các loài lợn rừng thông thường, mầm răng nanh hàm trên mọc hướng xuống dưới hoặc chếch sang hai bên mép miệng. Nhưng ở cá thể lợn đực Babirusa, toàn bộ hốc chân răng hàm trên đã bị xoay ngược một trăm tám mươi độ trong quá trình phát triển phôi thai!
```
**Part 1** → `audio/vs/scene02_p1.wav` (71 ký tự) · 🎭 cameo `co_tro_ly`

```text
Ủa bác sĩ ơi, thế cái răng mọc ngược lên trời thì nó đâm đi đâu hả bác?
```
**Part 2** → `audio/vs/scene02_p2.wav` (544 ký tự) · mood `tram_bi_an`

```text
Khám phá quá trình phát triển của bệnh nhân sẽ khiến quý vị rùng mình hơn nữa: Khi một chú lợn hươu con vừa chào đời, gương mặt gã hoàn toàn bình thường, mõm trơn láng và chưa hề có chiếc nanh nào lộ diện! Nhưng khi bước vào độ tuổi dậy thì khoảng một hai tuổi, chiếc mầm nanh quái đản bắt đầu đội thịt chồi lên! Da mõm gã sưng vù, căng tức cực độ cho đến khi mũi nanh sắc nhọn xé toang thớ thịt, đâm thủng một lỗ hổng vĩnh viễn trên sống mũi để vươn thẳng ra ngoài không khí! Một nghi thức trưởng thành đẫm máu mà tạo hóa bắt gã phải trải qua!
```
**Part 3** → `audio/vs/scene02_p3.wav` (453 ký tự) · mood `don_dap`

```text
[surprise-oh] Câu hỏi của cô trợ lý chạm đúng vào bi kịch giải phẫu đau đớn nhất! Do chân răng hướng ngược lên đỉnh đầu, khi chiếc răng nanh bắt đầu mọc dài ra ở tuổi dậy thì, nó hoàn toàn không chui vào khoang miệng! Thay vào đó, chiếc răng nanh nhọn hoắt đâm thẳng qua vòm họng trên, chọc thủng lớp mỡ, lớp thịt dày và xé rách lớp da mõm phía trên để chồi thẳng ra ngoài không khí! Một ca phẫu thuật tự nhiên đẫm máu mà chính cơ thể gã phải gánh chịu!
```
**Part 4** → `audio/vs/scene02_p4.wav` (360 ký tự) · mood `hao_hung`

```text
Chưa dừng lại ở đó, gã còn sở hữu thêm một cặp răng nanh ở hàm dưới dài tới hai mươi xăng-ti-mét! Cặp nanh dưới này mọc chìa sang hai bên má rồi uốn cong lên trên như hai chiếc lưỡi mác sắc bén! Đây là vũ khí cận chiến lợi hại giúp gã tự vệ trước các loài thú săn mồi và húc tung đối thủ trong những trận quyết đấu tranh giành lãnh thổ giữa rừng rậm nhiệt đới!
```

### scene03 — VÒNG CUNG TỰ SÁT — CHIẾC RĂNG 40CM UỐN CONG ĐÂM THỦNG HỘP SỌ LỢN GIÀ
*Thẻ chương:* MŨI KHOAN BỐN MƯƠI XĂNG TI MÉT UỐN CONG CẮM VÀO NÃO BỘ

*Badge:* `VÒNG CUNG TỰ SÁT` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene03_p0.wav` (392 ký tự) · mood `don_dap`

```text
Chẩn đoán triệu chứng số ba đưa chúng ta đến với nghịch lý rùng mình nhất của hồ sơ bệnh án! Sau khi đâm xuyên qua da mõm chồi lên trên trời, cặp răng nanh hàm trên của Gã bệnh nhân tự sát tiến hóa không dừng lại! Khác với răng của con người ngừng phát triển khi trưởng thành, răng nanh của lợn hươu không có chân răng đóng kín, nghĩa là chúng liên tục dài ra không ngừng trong suốt cuộc đời!
```
**Part 1** → `audio/vs/scene03_p1.wav` (509 ký tự) · mood `hao_hung`

```text
Điều nực cười nhất trong cấu tạo giải phẫu của cặp nanh trên này chính là độ bền cơ học của chúng! Mọi người thường nghĩ răng nanh lợn rừng phải cứng như thép và sắc bén vô song đúng không? Hoàn toàn ngược lại! Cặp răng nanh hàm trên của Babirusa hoàn toàn không có lớp men răng cứng bao bọc bên ngoài, ruột xốp rỗng và cực kỳ giòn xốp! Nếu gã lỡ dại dùng cặp nanh này để húc đá hay ủi gốc cây tìm thức ăn, chúng sẽ gãy vụn ngay lập tức! Nghĩa là gã mang trên mặt một cặp vũ khí tự sát vừa vô dụng vừa dễ gãy!
```
**Part 2** → `audio/vs/scene03_p2.wav` (401 ký tự) · mood `don_dap`

```text
Chiều dài của cặp nanh trên có thể chạm mốc ba mươi đến bốn mươi xăng-ti-mét! Và điều điên rồ là thay vì mọc thẳng đứng lên trời, chúng bắt đầu uốn cong dần thành một vòng cung hoàn hảo hướng ngược trở lại phía sau, nhắm thẳng vào vầng trán của chính chủ nhân! Khoảng cách giữa đầu nhọn chiếc nanh và lớp xương trán cứ thế thu hẹp dần từng tháng, từng năm, tựa như một chiếc đồng hồ đếm ngược tử thần!
```
**Part 3** → `audio/vs/scene03_p3.wav` (393 ký tự) · mood `tram_bi_an`

```text
[surprise-wa] Nếu một chú lợn hươu may mắn sống thọ vượt mốc mười lăm năm tuổi trong tự nhiên mà không bị mài mòn răng, thảm kịch kinh hoàng sẽ chính thức xảy ra: Đầu nhọn của chiếc răng nanh dài bốn mươi xăng-ti-mét sẽ chạm vào da trán, đâm xuyên qua lớp thịt đầu, nghiền nát lớp xương sọ cứng đặc và cắm thẳng vào mô não của chính nó! Một ca tử vong do chính chiếc răng trên mặt mình gây ra!
```
**Part 4** → `audio/vs/scene03_p4.wav` (374 ký tự) · mood `nghiem_trang_gia`

```text
Các nhà tự nhiên học khi thám hiểm đảo Sulawesi đã từng tìm thấy những bộ xương sọ lợn hươu cổ xưa, nơi chiếc răng nanh mọc xuyên qua xương trán và trồi hẳn vào bên trong khoang não! Một cái chết từ từ và vô cùng đau đớn! Bất kỳ bác sĩ nào khi nhìn vào cấu trúc này cũng phải thốt lên: Tại sao tiến hóa lại có thể tạo ra một lỗi thiết kế tàn nhẫn và ngớ ngẩn đến nhường này?
```

### scene04 — BÍ ẨN TIẾN HÓA — CHỌN LỌC GIỚI TÍNH ĐÁNH ĐỔI TÍNH MẠNG VÌ BẠN TÌNH
*Thẻ chương:* TẠI SAO CHỌN LỌC TỰ NHIÊN KHÔNG LOẠI BỎ CẶP NAI TỰ HỦY

*Badge:* `BÍ ẨN TIẾN HÓA` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene04_p0.wav` (307 ký tự) · mood `hao_hung`

```text
Câu hỏi lớn nhất đặt ra cho các nhà khoa học: Quy luật chọn lọc tự nhiên vốn dĩ sẽ đào thải những đột biến có hại cho sự sinh tồn. Vậy tại sao suốt hàng triệu năm qua, Gã bệnh nhân tự sát tiến hóa vẫn không bị tuyệt chủng mà vẫn ngang nhiên diễu hành khắp các hòn đảo Indonesia với cặp nanh tự sát trên mặt?
```
**Part 1** → `audio/vs/scene04_p1.wav` (87 ký tự) · 🎭 cameo `co_tro_ly`

```text
Bác sĩ ơi, hay là do mấy con lợn cái nó mê những anh chàng có răng nanh cong vút thế ạ?
```
**Part 2** → `audio/vs/scene04_p2.wav` (341 ký tự) · mood `hao_hung`

```text
[surprise-oh] Cô trợ lý lại một lần nữa đưa ra chẩn đoán chính xác tuyệt đối! Đáp án cho nghịch lý này nằm ở cán cân quyền lực của chọn lọc giới tính! Trong mắt các nàng lợn hươu cái, một chàng lợn đực sở hữu cặp răng nanh trên uốn cong dài ngoằng chạm sát trán chính là biểu tượng tối thượng của sự quyến rũ và sức mạnh sinh tồn! [laughter]
```
**Part 3** → `audio/vs/scene04_p3.wav` (407 ký tự) · mood `tram_bi_an`

```text
Bởi vì sao? Một con lợn đực có thể sống sót đến tuổi già, vượt qua bao mùa khô hạn, thú dữ và bệnh tật để cặp nanh mọc dài tới mức sắp đâm vào trán chứng minh một điều rõ ràng: Gã sở hữu một bộ gen sinh tồn cực kỳ phi thường! Cặp nanh càng dài và càng nguy hiểm, gã càng dễ dàng chiếm trọn trái tim của các nàng lợn cái và truyền lại bộ gen tự sát này cho thế hệ sau trước khi chiếc nanh kịp cắm vào não gã!
```
**Part 4** → `audio/vs/scene04_p4.wav` (494 ký tự) · mood `hao_hung`

```text
Chính vì cặp nanh trên quá giòn và quý giá, các chàng lợn đực đã sáng tạo ra một nghi thức thi đấu tranh giành bạn tình độc nhất vô nhị: Khi hai gã lợn đực bước vào đấu trường quyết đấu, chúng tuyệt đối không bao giờ lao vào húc nanh đối đầu như lợn rừng thông thường vì sợ gãy mất món bảo bối quyến rũ! Thay vào đó, chúng đứng thẳng dậy bằng hai chân sau như hai võ sĩ quyền Anh hạng nặng, dùng hai mõm tỳ chặt vào nhau rồi vật lộn đẩy ngã đối phương trong tiếng gầm gừ vang dội cánh rừng già!
```

### scene05 — CỖ MÁY SINH HỌC — CHIẾC BỤNG LÊN MEN NHƯ BÒ VÀ ĐÔI CHÂN HƯƠU CHẠY NHANH
*Thẻ chương:* CHIẾC BỤNG LÊN MEN XENLULOZO VÀ ĐÔI CHÂN BẬC THẦY BƠI LỘI

*Badge:* `CỖ MÁY SINH HỌC` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene05_p0.wav` (401 ký tự) · mood `don_dap`

```text
Khám nghiệm toàn diện cơ thể của Gã bệnh nhân tự sát tiến hóa còn hé lộ những bí mật sinh học phi thường khác! Quý vị có biết tại sao người bản địa lại gọi loài này là Babirusa, ghép từ hai chữ babi nghĩa là con lợn và rusa nghĩa là con hươu không? Đó là vì gã sở hữu một vóc dáng hoàn toàn khác biệt so với họ hàng lợn ủn ỉn: Đôi chân thon dài, cao ráo và gân guốc tựa như một chú hươu sao dũng mãnh!
```
**Part 1** → `audio/vs/scene05_p1.wav` (300 ký tự) · mood `hao_hung`

```text
Nhờ đôi chân hươu thần thánh này, lợn hươu có thể phi nước đại qua những đầm lầy hiểm trở và đặc biệt là khả năng bơi lội siêu đẳng! Chúng có thể bơi vượt qua các eo biển rộng hàng cây số nối liền giữa các hòn đảo hoang sơ của quần đảo Sulawesi để tìm kiếm nguồn thức ăn mới mà không sợ bị chết đuối!
```
**Part 2** → `audio/vs/scene05_p2.wav` (434 ký tự) · mood `don_dap`

```text
[surprise-wa] Đặt ống soi vào ổ bụng của gã, hệ tiêu hóa sẽ khiến các chuyên gia giải phẫu phải kinh ngạc: Thay vì dạ dày đơn giản như loài lợn ăn tạp, dạ dày của Babirusa phát triển thành cấu trúc nhiều ngăn phức tạp, chứa đầy các chủng vi sinh vật cộng sinh tương tự như dạ dày của loài bò nhai lại! Hệ thống này giúp gã tiêu hóa triệt để chất xơ xenlulozo thô cứng từ lá cây, rễ củ và thậm chí là những loại nấm rừng có độc tố cao!
```
**Part 3** → `audio/vs/scene05_p3.wav` (303 ký tự) · mood `tram_bi_an`

```text
Để tránh cho chiếc nanh trên đâm vào trán quá sớm, những chú lợn đực thông minh thường xuyên tìm đến những thân cây gỗ lim cứng hoặc đá tảng để cọ xát và mài mòn đầu răng nanh! Đó là cuộc chạy đua sinh tồn từng ngày giữa sự phát triển tự sát của chiếc răng và nỗ lực mài mòn kiên trì của chính chủ nhân!
```
**Part 4** → `audio/vs/scene05_p4.wav` (486 ký tự) · mood `hao_hung`

```text
Chưa hết đâu nhé, chế độ ăn nhiều lá cây rừng chứa độc tố tanin đòi hỏi Gã bệnh nhân tự sát tiến hóa phải có một liệu trình giải độc cực kỳ thông minh: Các nhà nghiên cứu phát hiện ra đàn lợn hươu thường xuyên hành hương đến các mỏ đá muối khoáng tự nhiên và suối nước nóng địa nhiệt ở đảo Sulawesi! Tại đây, gã cần mẫn liếm láp những mảng bùn khoáng giàu canxi và natri để trung hòa độc tố trong dạ dày, đồng thời bổ sung khoáng chất giúp nuôi dưỡng cặp nanh khổng lồ mọc dài liên tục!
```

### scene06 — ĐƠN THUỐC TIẾN HÓA — BÀI HỌC TRIẾT LÝ VÀ THỬ THÁCH ĐOÁN TẬP 47
*Thẻ chương:* ĐƠN THUỐC TIẾN HÓA VÀ THỬ THÁCH ĐOÁN TẬP BỐN MƯƠI BẢY

*Badge:* `LỜI KẾT BỆNH ÁN` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene06_p0.wav` (466 ký tự) · mood `am_ap`

```text
Hồ sơ bệnh án số bốn mươi sáu chính thức khép lại với kết luận chẩn đoán: Lợn Hươu Babirusa là một kiệt tác dị biệt và là lời cảnh tỉnh triết lý sâu sắc của tự nhiên! Trong cuộc sống, đôi khi những vũ khí, những hào quang hay những lợi thế mạnh mẽ nhất mà bạn dày công vun đắp, nếu không được kiểm soát và định hướng đúng đắn, lại chính là thứ quay mũi giáo lại đâm vào chính bạn! Biết tiết chế sức mạnh và kiểm soát tham vọng chính là bài học sinh tồn đắt giá nhất!
```
**Part 1** → `audio/vs/scene06_p1.wav` (228 ký tự) · mood `hao_hung`

```text
Nếu được quyền can thiệp vào quy trình tiến hóa của chú lợn hươu Babirusa, bạn sẽ chọn bẻ cong chiếc nanh ra ngoài để gã an toàn hay giữ nguyên vẻ đẹp quyến rũ chết người này? Hãy để lại bình luận chẩn đoán của bạn bên dưới nhé!
```
**Part 2** → `audio/vs/scene06_p2.wav` (422 ký tự) · mood `tram_bi_an`

```text
Còn bây giờ, hãy chuẩn bị cùng xưởng chế tạo vũ khí sinh học bước vào bản vẽ kỹ thuật của tập bốn mươi bảy! Một sinh vật đồ sộ trên thảo nguyên Châu Phi sở hữu chiếc cổ dài tới hai mét, một trái tim nặng mười một ki-lô-gam với huyết áp cao gấp đôi con người, và một hệ thống van thủy lực vi mô thần kỳ giúp nó cúi đầu uống nước mà không bị nổ tung mạch máu não! Bạn có biết cỗ máy thủy lực sinh học vĩ đại này là ai không?
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Khi tiến hóa chơi khăm tàn nhẫn: Loài lợn sở hữu cặp răng nanh tự đâm thủng da mặt rồi uốn cong cắm thẳng vào não của chính nó! Đây là Lợn Hươu Babirusa, loài động vật kỳ lạ đặc hữu của hòn đảo Sulawesi, Indonesia! Ở con đực, mầm răng nanh hàm trên bị xoay ngược một trăm tám mươi độ, đâm xuyên qua thịt mõm chồi lên trời. Chiếc nanh dài tới bốn mươi xăng-ti-mét uốn cong thành vòng cung hướng thẳng về trán, và ở những con già, mũi nanh nhọn hoắt sẽ đâm xuyên xương sọ cắm vào não gây tử vong! Kỳ lạ thay, gen tự sát này vẫn tồn tại hàng triệu năm vì lợn cái mê mẩn những con đực có nanh cong sát trán, coi đó là biểu tượng sống thọ và quyến rũ! Chúng phải liên tục cọ răng vào cây để mài mòn, tự cứu lấy mạng sống của mình trước món quà chết người của tạo hóa!
```

**Whisper prompt:** `Lợn Hươu Babirusa, Babyrousa celebensis`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| bốn mươi sáu | 46 |
| Bốn mươi sáu | 46 |
| Tập bốn mươi sáu | Tập 46 |
| bốn mươi lăm | 45 |
| Bốn mươi lăm | 45 |
| bốn mươi bảy | 47 |
| Bốn mươi bảy | 47 |
| số bốn mươi sáu | số 46 |
| Số bốn mươi sáu | Số 46 |
| bốn mươi xăng-ti-mét | 40 cm |
| Bốn mươi xăng-ti-mét | 40 cm |
| ba mươi xăng-ti-mét | 30 cm |
| Ba mươi xăng-ti-mét | 30 cm |
| hai mươi xăng-ti-mét | 20 cm |
| Hai mươi xăng-ti-mét | 20 cm |
| một trăm | 100 |
| Một trăm | 100 |
| một trăm ki-lô-gam | 100 kg |
| Một trăm ki-lô-gam | 100 kg |
| một trăm tám mươi độ | 180° |
| Một trăm tám mươi độ | 180° |
| mười lăm năm | 15 năm |
| Mười lăm năm | 15 năm |
| hai mươi tư giờ | 24 giờ |
| Hai mươi tư giờ | 24 giờ |
| hàng triệu năm | hàng triệu năm |
| Hàng triệu năm | Hàng triệu năm |
| triệu năm | triệu năm |
| không một | không 1 |
| Không một | Không 1 |
| một cặp | 1 cặp |
| Một cặp | 1 cặp |
| một ca bệnh | 1 ca bệnh |
| Một ca bệnh | 1 ca bệnh |
| một loài | 1 loài |
| Một loài | 1 loài |
| một chú | 1 chú |
| Một chú | 1 chú |
| một con | 1 con |
| Một con | 1 con |
| một chiếc | 1 chiếc |
| Một chiếc | 1 chiếc |
| một chiếc máy | 1 chiếc máy |
| Một chiếc máy | 1 chiếc máy |
| một hòn đảo | 1 hòn đảo |
| Một hòn đảo | 1 hòn đảo |
| một mũi tên | 1 mũi tên |
| Một mũi tên | 1 mũi tên |
| một vụ án | 1 vụ án |
| Một vụ án | 1 vụ án |
| một bài học | 1 bài học |
| Một bài học | 1 bài học |
| một phần | 1 phần |
| Một phần | 1 phần |
| một vòng cung | 1 vòng cung |
| Một vòng cung | 1 vòng cung |
| một tấm phim | 1 tấm phim |
| Một tấm phim | 1 tấm phim |
| một khối | 1 khối |
| Một khối | 1 khối |
| một hệ thống | 1 hệ thống |
| Một hệ thống | 1 hệ thống |
| một điểm tựa | 1 điểm tựa |
| Một điểm tựa | 1 điểm tựa |
| Su-la-we-si | Sulawesi |
| ba mươi | 30 |
| mười một | 11 |
| mười lăm | 15 |
| một hai tuổi | 1-2 tuổi |
| hai chân sau | 2 chân sau |
| hai chân | 2 chân |
| bốn mươi | 40 |
| hai mươi | 20 |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · BỆNH ÁN SỐ 46 — BÁC SĨ CHẤN ĐỘNG TRƯỚC CA PHẪU THUẬT RĂNG NANH MỌC NGƯỢC · 78.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.4 (8.4s) | L01 | Khẩn cấp mở cửa phòng phẫu thuật pháp y sinh học hoang dã! Y tá đâu, chuẩn bị ngay cho tôi bộ kẹp kim loại titan, cưa xương phẫu thuật và máy chụp cắt lớp |  | Phòng phẫu thuật pháp y sinh vật cổ: bác sĩ pháp y cú mèo đeo kính lúp một mắt và tạp dề da thuộc, cầm kẹp kim loại titan và cưa xương cầm cưa xương và kẹp titan đang chỉ đạo hiện trường khẩn cấp; trên bàn mổ ánh đèn chiếu sáng hồ sơ vụ án. |
| b02 | 00:08.4–00:16.8 (8.4s) | L02 | sọ não ba chiều đa tầng lập tức! Bệnh nhân tiếp theo của chúng ta hôm nay là 1 ca bệnh giải phẫu chấn động bậc nhất giới động vật có vú: Một sinh vật sống tại vùng rừng |  | Cận cảnh cửa vào: Tấm rèm phòng khám bị hai chiếc răng nanh cong vút đâm thủng toạc một đường; cô trợ lý thỏ trắng đeo tạp dề chữ thập đỏ bưng khay dụng cụ phẫu thuật ôm khay dụng cụ hoảng hốt lùi lại. |
| b03 | 00:16.8–00:26.4 (9.6s) | L03 | nhiệt đới đảo Sulawesi của đất nước Indonesia, mang trên mình một bản án tử hình sinh học do chính tạo hóa lập trình! Bác sĩ ơi, bệnh nhân này vừa bước vào cửa mà hai cái |  | chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu lừng lững bước vào: Toàn thân màu xám tro gân guốc, bốn chiếc nanh khổng lồ mọc tua tủa quanh mặt; ánh mắt sắc lạnh bí hiểm. |
| b04 | 00:26.4–00:36.5 (10.1s) | L04 | răng trên mặt nó đã đâm thủng cả tấm rèm phòng khám rồi ạ! Cô trợ lý chớ vội hoảng sợ! Hãy để tôi đọc to bệnh án số 46: Sinh vật kỳ quặc này có tên là Babirusa, |  | bác sĩ pháp y cú mèo đeo kính lúp một mắt và tạp dề da thuộc, cầm kẹp kim loại titan và cưa xương cầm tấm bảng bệnh án số bốn mươi sáu; tiêu đề GÃ BỆNH NHÂN hi sinh bảo vệ tổ TIẾN HÓA hiện lên sắc nét theo phong cách tranh khắc gỗ Sulawesi. |
| b05 | 00:36.5–00:45.5 (9.0s) | L05 | hay còn gọi là Lợn Hươu! Nhưng trong giới y khoa nghiên cứu tiến hóa, chúng tôi gọi gã bằng một biệt danh đầy rùng mình: Gã bệnh nhân tự sát tiến hóa! Trong khi mọi |  | So sánh chức năng răng nanh: BÊN TRÁI là hổ báo dùng nanh cắn xé con mồi; BÊN PHẢI là chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu với cặp nanh hàm trên mọc ngược theo quỹ đạo tự hủy kỳ lạ. |
| b06 | 00:45.5–00:53.1 (7.6s) | L06 | loài thú có răng nanh trên Trái Đất đều dùng nanh để xé thịt con mồi hoặc tự vệ chống lại kẻ thù, thì cặp răng nanh của gã bạn này lại mọc ngược theo một quỹ đạo tự |  | Bàn cân thể trọng pháp y: chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu đứng trên cân hiển thị thể trọng một trăm ki-lô-gam; đôi chân thon dài như hươu rừng nổi rõ từng thớ cơ. |
| b07 | 00:53.1–01:02.1 (9.0s) | L07 | hủy diệt không thể tin nổi! Nhìn vào khối cơ thể lực lưỡng nặng gần 100 kg với đôi chân thon dài như loài hươu rừng, bạn sẽ thấy một vẻ đẹp dũng mãnh và hoang dã. Nhưng | **100 KG** · thể trọng cơ bắp · R/360 · [0.75, 0.5] | Phóng to đầu của chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu: Bốn chiếc nanh mọc quanh miệng, hai chiếc nanh trên đâm xuyên qua sống mũi rồi uốn cong ngược nhắm thẳng vào giữa trán. |
| b08 | 01:02.1–01:10.4 (8.4s) | L08 | khi phóng to góc máy vào phần đầu của gã, toàn bộ bác sĩ sẽ phải rùng mình: Bốn chiếc răng nanh khổng lồ mọc tua tủa quanh miệng, trong đó hai chiếc răng hàm trên mọc xuyên |  | bác sĩ pháp y cú mèo đeo kính lúp một mắt và tạp dề da thuộc, cầm kẹp kim loại titan và cưa xương dùng thước kẹp đo góc uốn cong của răng nanh; biểu cảm kinh ngạc trước cấu trúc cơ thể kỳ lạ nhất từng ghi nhận. |
| b09 | 01:10.4–01:18.9 (8.5s) | L09 | thủng thịt mũi rồi uốn cong ngược trở lại, nhắm thẳng vào chính giữa hộp sọ của chủ nhân! Hãy cùng chúng tôi đặt tấm phim chẩn đoán lên bàn mổ để vén màn bí ẩn kinh hoàng này! |  | Bản đồ hòn đảo Sulawesi, Indonesia thời cổ đại hiện lên mờ ảo; bác sĩ pháp y cú mèo đeo kính lúp một mắt và tạp dề da thuộc, cầm kẹp kim loại titan và cưa xương bắt đầu mở màn chẩn đoán giải phẫu chuyên sâu. |

### scene02 · GIẢI PHẪU DỊ TẬT — CẶP RĂNG NANH HÀM TRÊN XOAY 180 ĐỘ ĐÂM XUYÊN DA MÕM · 91.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.2 (9.2s) | L10 | Hãy đặt tấm phim chụp cắt lớp vi tính xương sọ của Gã bệnh nhân tự sát tiến hóa lên màn hình! Điều đầu tiên khiến toàn thể hội đồng giám định y khoa phải dụi mắt bàng hoàng: Hãy |  | Màn hình cắt lớp vi tính xương sọ: Khung xương hàm của chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu hiện rõ chi tiết; bác sĩ pháp y cú mèo đeo kính lúp một mắt và tạp dề da thuộc, cầm kẹp kim loại titan và cưa xương |
| b02 | 00:09.2–00:17.5 (8.3s) | L11 | nhìn vào chân răng của hàm trên! Ở tất cả các loài lợn rừng thông thường, mầm răng nanh hàm trên mọc hướng xuống dưới hoặc chếch sang hai bên mép miệng. Nhưng ở cá thể lợn đực Babirusa, toàn bộ |  | So sánh mầm răng: Ở lợn thường mầm răng hướng xuống dưới; ở chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu toàn bộ hốc chân răng bị xoay ngược một trăm tám mươi độ hướng thẳng lên đỉnh đầu. |
| b03 | 00:17.5–00:27.4 (9.9s) | L12 | hốc chân răng hàm trên đã bị xoay ngược 180° trong quá trình phát triển phôi thai! Ủa bác sĩ ơi, thế cái răng mọc ngược lên trời thì nó đâm đi đâu hả bác? Khám phá quá trình phát | **180°** · xoay chân răng · L/380 · [0.28, 0.5] | Lợn con mới sinh: Chú lợn con trơn láng đáng yêu bú mẹ; chưa hề có dấu vết của chiếc nanh mọc ngược nào lộ diện. |
| b04 | 00:27.4–00:36.0 (8.6s) | L13 | triển của bệnh nhân sẽ khiến quý vị rùng mình hơn nữa: Khi 1 chú lợn hươu con vừa chào đời, gương mặt gã hoàn toàn bình thường, mõm trơn láng và chưa hề có chiếc nanh nào lộ diện! Nhưng khi |  | Tuổi dậy thì đau đớn: Chú lợn trẻ khoảng một hai tuổi với sống mũi sưng vù; đầu nanh nhọn hoắt đội thịt chuẩn bị xé toang da mặt. |
| b05 | 00:36.0–00:45.6 (9.6s) | L14 | bước vào độ tuổi dậy thì khoảng 1-2 tuổi, chiếc mầm nanh quái đản bắt đầu đội thịt chồi lên! Da mõm gã sưng vù, căng tức cực độ cho đến khi mũi nanh sắc nhọn xé toang thớ thịt, đâm |  | Khoảnh khắc đâm thủng da mõm: Mũi nanh trên xé rách lớp thịt mũi, trồi thẳng ra ngoài không khí tạo thành hai lỗ thủng vĩnh viễn trên mặt gã. |
| b06 | 00:45.6–00:54.7 (9.2s) | L15 | thủng một lỗ hổng vĩnh viễn trên sống mũi để vươn thẳng ra ngoài không khí! Một nghi thức trưởng thành đẫm máu mà tạo hóa bắt gã phải trải qua! Câu hỏi của cô trợ lý chạm đúng vào bi kịch |  | cô trợ lý thỏ trắng đeo tạp dề chữ thập đỏ bưng khay dụng cụ phẫu thuật ôm mặt rùng mình trước ca phẫu thuật tự nhiên đẫm nước màu mà cơ thể chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu phải gánh chịu từ khi còn trẻ |
| b07 | 00:54.7–01:04.0 (9.2s) | L16 | giải phẫu đau đớn nhất! Do chân răng hướng ngược lên đỉnh đầu, khi chiếc răng nanh bắt đầu mọc dài ra ở tuổi dậy thì, nó hoàn toàn không chui vào khoang miệng! Thay vào đó, chiếc răng nanh nhọn |  | Giải phẫu cặp nanh dưới: Chiếc nanh hàm dưới dài hai mươi xăng-ti-mét chìa sang hai bên má uốn cong lên trên như hai chiếc lưỡi mác sắc lẻm. |
| b08 | 01:04.0–01:11.9 (7.9s) | L17 | hoắt đâm thẳng qua vòm họng trên, chọc thủng lớp mỡ, lớp thịt dày và xé rách lớp da mõm phía trên để chồi thẳng ra ngoài không khí! Một ca phẫu thuật tự nhiên đẫm máu mà chính cơ thể |  | Mô phỏng chiến đấu: chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu dùng cặp nanh dưới sắc bén húc tung kẻ thù trong một trận phục kích bảo vệ lãnh thổ giữa rừng rậm. |
| b09 | 01:11.9–01:22.1 (10.2s) | L18 | gã phải gánh chịu! Chưa dừng lại ở đó, gã còn sở hữu thêm 1 cặp răng nanh ở hàm dưới dài tới 20 cm! Cặp nanh dưới này mọc chìa sang hai bên má rồi uốn cong lên trên | **20 CM** · nanh dưới cận chiến · R/360 · [0.75, 0.5] | Bức tranh giải phẫu đối chiếu: Nanh dưới là vũ khí cận chiến sinh tử; nanh trên là cỗ máy tự hủy đang từ từ dài ra. |
| b10 | 01:22.1–01:31.7 (9.5s) | L19 | như hai chiếc lưỡi mác sắc bén! Đây là vũ khí cận chiến lợi hại giúp gã tự vệ trước các loài thú săn mồi và húc tung đối thủ trong những trận quyết đấu tranh giành lãnh thổ giữa rừng rậm nhiệt đới! |  | bác sĩ pháp y cú mèo đeo kính lúp một mắt và tạp dề da thuộc, cầm kẹp kim loại titan và cưa xương ghi chép chẩn đoán dị tật giai đoạn một vào hồ sơ bệnh án pháp y. |

### scene03 · VÒNG CUNG TỰ SÁT — CHIẾC RĂNG 40CM UỐN CONG ĐÂM THỦNG HỘP SỌ LỢN GIÀ · 100.3s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.5 (8.5s) | L20 | Chẩn đoán triệu chứng số ba đưa chúng ta đến với nghịch lý rùng mình nhất của hồ sơ bệnh án! Sau khi đâm xuyên qua da mõm chồi lên trên trời, cặp răng nanh hàm trên của |  | Mô hình 3D quỹ đạo tăng trưởng: Chiếc nanh trên của chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu liên tục dài ra không ngừng trong suốt cuộc đời do không có chân răng đóng kín. |
| b02 | 00:08.5–00:17.2 (8.8s) | L21 | Gã bệnh nhân tự sát tiến hóa không dừng lại! Khác với răng của con người ngừng phát triển khi trưởng thành, răng nanh của lợn hươu không có chân răng đóng kín, nghĩa là chúng liên tục dài ra không ngừng |  | Cắt lớp vi thể răng: Cặp nanh trên xốp rỗng không có lớp men răng cứng bao bọc; bác sĩ pháp y cú mèo đeo kính lúp một mắt và tạp dề da thuộc, cầm kẹp kim loại titan và cưa xương dùng ngón tay gõ nhẹ thấy rung rinh dễ gãy. |
| b03 | 00:17.2–00:27.0 (9.8s) | L22 | trong suốt cuộc đời! Điều nực cười nhất trong cấu tạo giải phẫu của cặp nanh trên này chính là độ bền cơ học của chúng! Mọi người thường nghĩ răng nanh lợn rừng phải cứng như thép và sắc bén |  | chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu cố ủi mõm vào tảng đá nhưng nanh trên lập tức mẻ một mảnh; gã giật mình vội vàng lùi lại bảo vệ cặp nanh quý giá. |
| b04 | 00:27.0–00:36.6 (9.6s) | L23 | vô song đúng không? Hoàn toàn ngược lại! Cặp răng nanh hàm trên của Babirusa hoàn toàn không có lớp men răng cứng bao bọc bên ngoài, ruột xốp rỗng và cực kỳ giòn xốp! Nếu gã lỡ dại dùng |  | Thước đo góc uốn cong: Chiếc nanh dài tới ba mươi đến bốn mươi xăng-ti-mét, uốn cong thành một vòng cung hoàn hảo nhắm thẳng về vầng trán. |
| b05 | 00:36.6–00:46.0 (9.3s) | L24 | cặp nanh này để húc đá hay ủi gốc cây tìm thức ăn, chúng sẽ gãy vụn ngay lập tức! Nghĩa là gã mang trên mặt 1 cặp vũ khí tự sát vừa vô dụng vừa dễ gãy! Chiều dài |  | Khoảng cách tử thần: Thước kẹp đo khoảng cách giữa đầu nhọn chiếc nanh và da trán của chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu chỉ còn vỏn vẹn vài mi-li-mét mong manh. |
| b06 | 00:46.0–00:55.1 (9.2s) | L25 | của cặp nanh trên có thể chạm mốc 30 đến 40 cm! Và điều điên rồ là thay vì mọc thẳng đứng lên trời, chúng bắt đầu uốn cong dần thành 1 vòng cung hoàn hảo hướng ngược trở lại phía sau, | **30-40 CM** · vòng cung tự sát · R/360 · [0.75, 0.5] | Đồng hồ đếm ngược tử thần quay tíc tắc: Càng sống thọ, nguy cơ đầu nanh cắm vào trán càng đến gần từng ngày. |
| b07 | 00:55.1–01:04.8 (9.7s) | L26 | nhắm thẳng vào vầng trán của chính chủ nhân! Khoảng cách giữa đầu nhọn chiếc nanh và lớp xương trán cứ thế thu hẹp dần từng tháng, từng năm, tựa như 1 chiếc đồng hồ đếm ngược tử thần! Nếu |  | Cá thể già mười lăm năm tuổi: Đầu nanh cắm thủng da trán, bắt đầu nghiền nát lớp xương sọ phía trước trong sự đau đớn cùng cực. |
| b08 | 01:04.8–01:14.5 (9.6s) | L27 | 1 chú lợn hươu may mắn sống thọ vượt mốc 15 năm tuổi trong tự nhiên mà không bị mài mòn răng, thảm kịch kinh hoàng sẽ chính thức xảy ra: Đầu nhọn của chiếc răng nanh dài 40 cm sẽ | **15 NĂM** · thời điểm đâm sọ · L/380 · [0.3, 0.5] | Tiêu bản hiện vật hộp sọ lợn hươu cổ xưa với cặp răng nanh uốn cong cắm xuyên qua xương trán vào khoang não: Hộp sọ cổ xưa bảo tàng với chiếc nanh cắm ngập vào bên trong khoang não; bằng chứng lịch sử chấn động. |
| b09 | 01:14.5–01:23.5 (9.0s) | L28 | chạm vào da trán, đâm xuyên qua lớp thịt đầu, nghiền nát lớp xương sọ cứng đặc và cắm thẳng vào mô não của chính nó! Một ca tử vong do chính chiếc răng trên mặt mình gây ra! Các |  | bác sĩ pháp y cú mèo đeo kính lúp một mắt và tạp dề da thuộc, cầm kẹp kim loại titan và cưa xương và cô trợ lý thỏ trắng đeo tạp dề chữ thập đỏ bưng khay dụng cụ phẫu thuật nghiêm trang tưởng niệm trước cái chết bi thảm do chính vũ khí trên mặt gây ra. |
| b10 | 01:23.5–01:32.3 (8.8s) | L29 | nhà tự nhiên học khi thám hiểm đảo Sulawesi đã từng tìm thấy những bộ xương sọ lợn hươu cổ xưa, nơi chiếc răng nanh mọc xuyên qua xương trán và trồi hẳn vào bên trong khoang não! Một cái chết |  | Câu hỏi lớn của tạo hóa: Tại sao chọn lọc tự nhiên lại không đào thải một cơ chế hi sinh bảo vệ tổ kỳ quặc nhường này suốt hàng triệu năm? |
| b11 | 01:32.3–01:40.3 (8.0s) | L30 | từ từ và vô cùng đau đớn! Bất kỳ bác sĩ nào khi nhìn vào cấu trúc này cũng phải thốt lên: Tại sao tiến hóa lại có thể tạo ra một lỗi thiết kế tàn nhẫn và ngớ ngẩn đến nhường này? |  | bác sĩ pháp y cú mèo đeo kính lúp một mắt và tạp dề da thuộc, cầm kẹp kim loại titan và cưa xương lật sang trang hồ sơ tiếp theo để giải mã bí ẩn chọn lọc giới tính. |

### scene04 · BÍ ẨN TIẾN HÓA — CHỌN LỌC GIỚI TÍNH ĐÁNH ĐỔI TÍNH MẠNG VÌ BẠN TÌNH · 84.3s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.3 (9.3s) | L31 | Câu hỏi lớn nhất đặt ra cho các nhà khoa học: Quy luật chọn lọc tự nhiên vốn dĩ sẽ đào thải những đột biến có hại cho sự sinh tồn. Vậy tại sao suốt hàng triệu năm qua, |  | Bảng nghiên cứu sinh thái cổ xưa minh họa quy luật tự nhiên, biểu đồ đối chiếu tiến hóa và sự kỳ diệu của muôn loài. |
| b02 | 00:09.3–00:18.8 (9.5s) | L32 | Gã bệnh nhân tự sát tiến hóa vẫn không bị tuyệt chủng mà vẫn ngang nhiên diễu hành khắp các hòn đảo Indonesia với cặp nanh tự sát trên mặt? Bác sĩ ơi, hay là do mấy con lợn cái nó |  | cô trợ lý thỏ trắng đeo tạp dề chữ thập đỏ bưng khay dụng cụ phẫu thuật giơ tay thắc mắc liệu có phải các nàng lợn cái mê mẩn những chàng lợn có cặp nanh cong chạm sát trán. |
| b03 | 00:18.8–00:28.3 (9.5s) | L33 | mê những anh chàng có răng nanh cong vút thế ạ? Cô trợ lý lại một lần nữa đưa ra chẩn đoán chính xác tuyệt đối! Đáp án cho nghịch lý này nằm ở cán cân quyền lực của chọn lọc |  | Đấu trường sắc đẹp rừng già: nàng lợn hươu cái duyên dáng không có nanh trên, ánh mắt ngưỡng mộ nhìn chàng lợn đực với ánh mắt si tình đang ngắm nhìn chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu khoe cặp nanh vòng c |
| b04 | 00:28.3–00:39.3 (11.0s) | L34 | giới tính! Trong mắt các nàng lợn hươu cái, một chàng lợn đực sở hữu cặp răng nanh trên uốn cong dài ngoằng chạm sát trán chính là biểu tượng tối thượng của sự quyến rũ và sức mạnh sinh tồn! Bởi |  | Biểu tượng sống thọ: Chỉ những chàng lợn có gen sinh tồn vượt trội mới sống sót đủ lâu để cặp nanh mọc dài chạm trán. |
| b05 | 00:39.3–00:47.6 (8.3s) | L35 | vì sao? 1 con lợn đực có thể sống sót đến tuổi già, vượt qua bao mùa khô hạn, thú dữ và bệnh tật để cặp nanh mọc dài tới mức sắp đâm vào trán chứng minh một điều rõ ràng: |  | Trái tim tình yêu chiến thắng: chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu chiếm trọn tình cảm của bạn tình, thành công truyền lại bộ gen nanh hi sinh bảo vệ tổ cho bầy lợn con thế hệ sau. |
| b06 | 00:47.6–00:55.7 (8.1s) | L36 | Gã sở hữu một bộ gen sinh tồn cực kỳ phi thường! Cặp nanh càng dài và càng nguy hiểm, gã càng dễ dàng chiếm trọn trái tim của các nàng lợn cái và truyền lại bộ gen tự |  | Nghi thức quyết đấu độc lạ: Hai chàng lợn đực tuyệt đối không húc nanh vào nhau vì sợ gãy món trang sức quý giá. |
| b07 | 00:55.7–01:04.6 (9.0s) | L37 | sát này cho thế hệ sau trước khi chiếc nanh kịp cắm vào não gã! Chính vì cặp nanh trên quá giòn và quý giá, các chàng lợn đực đã sáng tạo ra một nghi thức thi đấu tranh giành bạn tình |  | Đấu quyền Anh rừng rậm: Hai chú lợn đứng thẳng dậy bằng hai chân sau, dùng mõm tỳ vào nhau vật lộn đẩy ngã đối thủ như võ sĩ hạng nặng. |
| b08 | 01:04.6–01:14.3 (9.6s) | L38 | độc nhất vô nhị: Khi hai gã lợn đực bước vào đấu trường quyết đấu, chúng tuyệt đối không bao giờ lao vào húc nanh đối đầu như lợn rừng thông thường vì sợ gãy mất món bảo bối quyến rũ! |  | chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu giành chiến thắng vẻ vang, đứng ngạo nghễ gầm gừ khẳng định vị thế thủ lĩnh bầy đàn. |
| b09 | 01:14.3–01:24.3 (10.0s) | L39 | Thay vào đó, chúng đứng thẳng dậy bằng 2 chân sau như hai võ sĩ quyền Anh hạng nặng, dùng hai mõm tỳ chặt vào nhau rồi vật lộn đẩy ngã đối phương trong tiếng gầm gừ vang dội cánh rừng già! | **2 CHÂN SAU** · đấu vật quyền anh · R/360 · [0.75, 0.5] | bác sĩ pháp y cú mèo đeo kính lúp một mắt và tạp dề da thuộc, cầm kẹp kim loại titan và cưa xương gật gù thấu hiểu sức mạnh kỳ diệu của chọn lọc giới tính trong tự nhiên. |

### scene05 · CỖ MÁY SINH HỌC — CHIẾC BỤNG LÊN MEN NHƯ BÒ VÀ ĐÔI CHÂN HƯƠU CHẠY NHANH · 94.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.6 (8.6s) | L40 | Khám nghiệm toàn diện cơ thể của Gã bệnh nhân tự sát tiến hóa còn hé lộ những bí mật sinh học phi thường khác! Quý vị có biết tại sao người bản địa lại gọi loài này là Babirusa, ghép |  | Nguồn gốc tên gọi Babirusa: Ghép từ babi (lợn) và rusa (hươu); chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu sải bước kiêu hãnh với dáng dấp thanh thoát của loài hươu sao. |
| b02 | 00:08.6–00:17.1 (8.5s) | L41 | từ hai chữ babi nghĩa là con lợn và rusa nghĩa là con hươu không? Đó là vì gã sở hữu một vóc dáng hoàn toàn khác biệt so với họ hàng lợn ủn ỉn: Đôi chân thon dài, cao ráo và gân guốc |  | Đôi chân hươu thần tốc: chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu phi nước đại băng qua các vùng đầm lầy hiểm trở trên hòn đảo Sulawesi hoang sơ. |
| b03 | 00:17.1–00:26.8 (9.6s) | L42 | tựa như 1 chú hươu sao dũng mãnh! Nhờ đôi chân hươu thần thánh này, lợn hươu có thể phi nước đại qua những đầm lầy hiểm trở và đặc biệt là khả năng bơi lội siêu đẳng! Chúng có thể bơi vượt |  | Bậc thầy bơi biển: chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu ung dung bơi vượt qua eo biển sóng cuộn nối liền giữa các hòn đảo để tìm kiếm nguồn thức ăn trù phú. |
| b04 | 00:26.8–00:36.8 (10.1s) | L43 | qua các eo biển rộng hàng cây số nối liền giữa các hòn đảo hoang sơ của quần đảo Sulawesi để tìm kiếm nguồn thức ăn mới mà không sợ bị chết đuối! Đặt ống soi vào ổ bụng của gã, hệ tiêu | **SULAWESI** · địa bàn đặc hữu · L/380 · [0.28, 0.5] | Nội soi ổ bụng: Dạ dày nhiều ngăn phức tạp của chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu hiện rõ trên màn hình y tế; cơ chế lên men vi sinh vật giống hệt dạ dày loài bò nhai lại. |
| b05 | 00:36.8–00:45.3 (8.4s) | L44 | hóa sẽ khiến các chuyên gia giải phẫu phải kinh ngạc: Thay vì dạ dày đơn giản như loài lợn ăn tạp, dạ dày của Babirusa phát triển thành cấu trúc nhiều ngăn phức tạp, chứa đầy các chủng vi sinh vật cộng |  | Lò phản ứng sinh học: Các chủng vi sinh vật cộng sinh miệt mài phân giải chất xơ thô cứng và trung hòa độc tố từ nấm rừng. |
| b06 | 00:45.3–00:55.2 (9.9s) | L45 | sinh tương tự như dạ dày của loài bò nhai lại! Hệ thống này giúp gã tiêu hóa triệt để chất xơ xenlulozo thô cứng từ lá cây, rễ củ và thậm chí là những loại nấm rừng có độc tố cao! Để |  | Hành hương giải độc: Đàn lợn hươu tụ tập bên mỏ bùn khoáng tự nhiên và suối nước nóng địa nhiệt bốc khói nghi ngút. |
| b07 | 00:55.2–01:04.4 (9.2s) | L46 | tránh cho chiếc nanh trên đâm vào trán quá sớm, những chú lợn đực thông minh thường xuyên tìm đến những thân cây gỗ lim cứng hoặc đá tảng để cọ xát và mài mòn đầu răng nanh! Đó là cuộc chạy đua |  | chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu cần mẫn liếm láp bùn khoáng canxi và natri để thanh lọc cơ thể và nuôi dưỡng khung xương. |
| b08 | 01:04.4–01:13.9 (9.6s) | L47 | sinh tồn từng ngày giữa sự phát triển tự sát của chiếc răng và nỗ lực mài mòn kiên trì của chính chủ nhân! Chưa hết đâu nhé, chế độ ăn nhiều lá cây rừng chứa độc tố tanin đòi hỏi Gã |  | Cuộc chiến mài răng cứu mạng: chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu cọ xát cặp nanh trên vào thân cây gỗ lim cứng cáp để mài mòn mũi nhọn trước khi nó chạm trán. |
| b09 | 01:13.9–01:22.3 (8.4s) | L48 | bệnh nhân tự sát tiến hóa phải có một liệu trình giải độc cực kỳ thông minh: Các nhà nghiên cứu phát hiện ra đàn lợn hươu thường xuyên hành hương đến các mỏ đá muối khoáng tự nhiên và suối nước nóng địa |  | Vệt mài sáng bóng trên thân cây lim; chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu thở phào nhẹ nhõm khi khoảng cách an toàn với hộp sọ được nới rộng. |
| b10 | 01:22.3–01:34.9 (12.6s) | L49 | nhiệt ở đảo Sulawesi! Tại đây, gã cần mẫn liếm láp những mảng bùn khoáng giàu canxi và natri để trung hòa độc tố trong dạ dày, đồng thời bổ sung khoáng chất giúp nuôi dưỡng cặp nanh khổng lồ mọc dài liên tục! |  | bác sĩ pháp y cú mèo đeo kính lúp một mắt và tạp dề da thuộc, cầm kẹp kim loại titan và cưa xương ghi nhận liệu trình tự điều trị sinh tồn thông minh bậc nhất của bệnh nhân. |

### scene06 · ĐƠN THUỐC TIẾN HÓA — BÀI HỌC TRIẾT LÝ VÀ THỬ THÁCH ĐOÁN TẬP 47 · 55.2s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.2 (8.2s) | L50 | Hồ sơ bệnh án số 46 chính thức khép lại với kết luận chẩn đoán: Lợn Hươu Babirusa là một kiệt tác dị biệt và là lời cảnh tỉnh triết lý sâu sắc |  | bác sĩ pháp y cú mèo đeo kính lúp một mắt và tạp dề da thuộc, cầm kẹp kim loại titan và cưa xương gấp lại tập hồ sơ bệnh án số bốn mươi sáu; bức tranh phong cảnh rừng nhiệt đới Sulawesi cổ xưa hiện lên trầm mặc. |
| b02 | 00:08.2–00:15.8 (7.6s) | L51 | của tự nhiên! Trong cuộc sống, đôi khi những vũ khí, những hào quang hay những lợi thế mạnh mẽ nhất mà bạn dày công vun đắp, nếu không được kiểm soát và định hướng đúng đắn, |  | Bài học triết lý sinh tồn: chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu đứng giữa ánh hoàng hôn với cặp nanh cong vút; lời cảnh tỉnh về việc kiểm soát vũ khí nội tại trong cuộc sống. |
| b03 | 00:15.8–00:23.7 (7.9s) | L52 | lại chính là thứ quay mũi giáo lại đâm vào chính bạn! Biết tiết chế sức mạnh và kiểm soát tham vọng chính là bài học sinh tồn đắt giá nhất! Nếu được quyền |  | Màn hình tương tác người xem: Hai lựa chọn phẫu thuật hài hước: Nút 1 bẻ cong nanh ra ngoài cứu mạng, Nút 2 để nguyên nanh cong cho gã tán gái. |
| b04 | 00:23.7–00:32.5 (8.8s) | L53 | can thiệp vào quy trình tiến hóa của chú lợn hươu Babirusa, bạn sẽ chọn bẻ cong chiếc nanh ra ngoài để gã an toàn hay giữ nguyên vẻ đẹp quyến rũ chết người này? Hãy |  | cô trợ lý thỏ trắng đeo tạp dề chữ thập đỏ bưng khay dụng cụ phẫu thuật giơ biển chỉ dẫn mời quý khán giả để lại ý kiến bình luận chẩn đoán bên dưới video. |
| b05 | 00:32.5–00:40.2 (7.8s) | L54 | để lại bình luận chẩn đoán của bạn bên dưới nhé! Còn bây giờ, hãy chuẩn bị cùng xưởng chế tạo vũ khí sinh học bước vào bản vẽ kỹ thuật của tập 47! |  | Bản vẽ kỹ thuật tập bốn mươi bảy hé lộ: Chú hươu cao cổ với chiếc cổ dài hai mét sừng sững giữa thảo nguyên Châu Phi nắng rực. |
| b06 | 00:40.2–00:47.7 (7.5s) | L55 | Một sinh vật đồ sộ trên thảo nguyên Châu Phi sở hữu chiếc cổ dài tới hai mét, một trái tim nặng 11 ki-lô-gam với huyết áp cao gấp đôi con người, và 1 hệ |  | Sơ đồ giải phẫu trái tim mười một cân và hệ thống van tĩnh mạch chống nổ não khi chú hươu cúi đầu uống nước. |
| b07 | 00:47.7–00:55.2 (7.5s) | L56 | thống van thủy lực vi mô thần kỳ giúp nó cúi đầu uống nước mà không bị nổ tung mạch máu não! Bạn có biết cỗ máy thủy lực sinh học vĩ đại này là ai không? |  | Màn hình kết thúc: Dòng chữ HẸN GẶP LẠI Ở TẬP 47 HƯƠU CAO CỔ lung linh với lời kêu gọi đăng ký kênh theo dõi. |

## 5. Phân cảnh Shorts — từng beat

Banner: **TIẾN HÓA TỰ SÁT / RĂNG ĐÂM THỦNG HỘP SỌ?!** · giọng 40.7s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Khi tiến hóa chơi khăm tàn nhẫn: Loài lợn sở hữu cặp răng nanh tự đâm thủng da mặt |  |
| s02 | 00:04.3 | S02 | rồi uốn cong cắm thẳng vào não của chính nó! Đây là Lợn Hươu Babirusa, loài động vật kỳ |  |
| s03 | 00:09.1 | S03 | lạ đặc hữu của hòn đảo Sulawesi, Indonesia! Ở con đực, mầm răng nanh hàm trên bị xoay ngược 180°, | **180°** · xoay ngược nanh · L/500 · [0.3, 0.5] |
| s04 | 00:15.5 | S04 | đâm xuyên qua thịt mõm chồi lên trời. Chiếc nanh dài tới 40 cm uốn cong thành vòng cung hướng thẳng về | **40 CM** · vòng cung tự sát · R/520 · [0.7, 0.5] |
| s05 | 00:21.4 | S05 | trán, và ở những con già, mũi nanh nhọn hoắt sẽ đâm xuyên xương sọ cắm vào não gây tử |  |
| s06 | 00:25.9 | S06 | vong! Kỳ lạ thay, gen tự sát này vẫn tồn tại hàng triệu năm vì lợn cái mê mẩn những con |  |
| s07 | 00:31.0 | S07 | đực có nanh cong sát trán, coi đó là biểu tượng sống thọ và quyến rũ! Chúng phải liên tục |  |
| s08 | 00:35.6 | S08 | cọ răng vào cây để mài mòn, tự cứu lấy mạng sống của mình trước món quà chết người của tạo hóa! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khẩn cấp mở cửa phòng phẫu thuật pháp y sinh học hoang dã! Y tá đâu, chuẩn bị ngay cho tôi bộ kẹp kim loại titan, cưa xương phẫu thuật và máy chụp cắt lớp sọ não". Bố cục: Phòng phẫu thuật pháp y sinh vật cổ: bác sĩ pháp y cú mèo đeo kính lúp một mắt và tạp dề da thuộc, cầm kẹp kim loại titan và cưa xương cầm cưa xương và kẹp titan đang chỉ đạo hiện trường khẩn cấp; trên bàn mổ ánh đèn chiếu sáng hồ sơ vụ án.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "ba chiều đa tầng lập tức! Bệnh nhân tiếp theo của chúng ta hôm nay là 1 ca bệnh giải phẫu chấn động bậc nhất giới động vật có vú: Một sinh vật sống tại vùng rừng nhiệt". Bố cục: Cận cảnh cửa vào: Tấm rèm phòng khám bị hai chiếc răng nanh cong vút đâm thủng toạc một đường; cô trợ lý thỏ trắng đeo tạp dề chữ thập đỏ bưng khay dụng cụ phẫu thuật ôm khay dụng cụ hoảng hốt lùi lại.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "đới đảo Sulawesi của đất nước Indonesia, mang trên mình một bản án tử hình sinh học do chính tạo hóa lập trình! Bác sĩ ơi, bệnh nhân này vừa bước vào cửa mà hai cái răng trên". Bố cục: chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu lừng lững bước vào: Toàn thân màu xám tro gân guốc, bốn chiếc nanh khổng lồ mọc tua tủa quanh mặt; ánh mắt sắc lạnh bí hiểm.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "mặt nó đã đâm thủng cả tấm rèm phòng khám rồi ạ! Cô trợ lý chớ vội hoảng sợ! Hãy để tôi đọc to bệnh án số 46: Sinh vật kỳ quặc này có tên là Babirusa, hay". Bố cục: bác sĩ pháp y cú mèo đeo kính lúp một mắt và tạp dề da thuộc, cầm kẹp kim loại titan và cưa xương cầm tấm bảng bệnh án số bốn mươi sáu; tiêu đề GÃ BỆNH NHÂN hi sinh bảo vệ tổ TIẾN HÓA hiện lên sắc nét theo phong cách tranh khắc gỗ Sulawesi.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "còn gọi là Lợn Hươu! Nhưng trong giới y khoa nghiên cứu tiến hóa, chúng tôi gọi gã bằng một biệt danh đầy rùng mình: Gã bệnh nhân hi sinh bảo vệ tổ tiến hóa! Trong khi mọi loài thú". Bố cục: So sánh chức năng răng nanh: BÊN TRÁI là hổ báo dùng nanh cắn xé con mồi; BÊN PHẢI là chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu với cặp nanh hàm trên mọc ngược theo quỹ đạo tự hủy kỳ lạ.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "có răng nanh trên Trái Đất đều dùng nanh để xé thịt con mồi hoặc tự vệ chống lại kẻ thù, thì cặp răng nanh của gã bạn này lại mọc ngược theo một quỹ đạo tự hủy". Bố cục: Bàn cân thể trọng pháp y: chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu đứng trên cân hiển thị thể trọng một trăm ki-lô-gam; đôi chân thon dài như hươu rừng nổi rõ từng thớ cơ.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "diệt không thể tin nổi! Nhìn vào khối cơ thể lực lưỡng nặng gần 100 kg với đôi chân thon dài như loài hươu rừng, bạn sẽ thấy một vẻ đẹp dũng mãnh và hoang dã. Nhưng khi". Bố cục: Phóng to đầu của chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu: Bốn chiếc nanh mọc quanh miệng, hai chiếc nanh trên đâm xuyên qua sống mũi rồi uốn cong ngược nhắm thẳng vào giữa trán.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "phóng to góc máy vào phần đầu của gã, toàn bộ bác sĩ sẽ phải rùng mình: Bốn chiếc răng nanh khổng lồ mọc tua tủa quanh miệng, trong đó hai chiếc răng hàm trên mọc xuyên thủng". Bố cục: bác sĩ pháp y cú mèo đeo kính lúp một mắt và tạp dề da thuộc, cầm kẹp kim loại titan và cưa xương dùng thước kẹp đo góc uốn cong của răng nanh; biểu cảm kinh ngạc trước cấu trúc cơ thể kỳ lạ nhất từng ghi nhận.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "thịt mũi rồi uốn cong ngược trở lại, nhắm thẳng vào chính giữa hộp sọ của chủ nhân! Hãy cùng chúng tôi đặt tấm phim chẩn đoán lên bàn mổ để vén màn bí ẩn kinh hoàng này!". Bố cục: Bản đồ hòn đảo Sulawesi, Indonesia thời cổ đại hiện lên mờ ảo; bác sĩ pháp y cú mèo đeo kính lúp một mắt và tạp dề da thuộc, cầm kẹp kim loại titan và cưa xương bắt đầu mở màn chẩn đoán giải phẫu chuyên sâu.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy đặt tấm phim chụp cắt lớp vi tính xương sọ của Gã bệnh nhân hi sinh bảo vệ tổ tiến hóa lên màn hình! Điều đầu tiên khiến toàn thể hội đồng giám định y khoa phải dụi mắt bàng hoàng: Hãy nhìn". Bố cục: Màn hình cắt lớp vi tính xương sọ: Khung xương hàm của chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu hiện rõ chi tiết; bác sĩ pháp y cú mèo đeo kính lúp một mắt và tạp dề da thuộc, cầm kẹp kim loại titan và cưa xương chỉ tay vào hốc chân răng hàm trên kỳ dị.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "vào chân răng của hàm trên! Ở tất cả các loài lợn rừng thông thường, mầm răng nanh hàm trên mọc hướng xuống dưới hoặc chếch sang hai bên mép miệng. Nhưng ở cá thể lợn đực Babirusa, toàn bộ hốc". Bố cục: So sánh mầm răng: Ở lợn thường mầm răng hướng xuống dưới; ở chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu toàn bộ hốc chân răng bị xoay ngược một trăm tám mươi độ hướng thẳng lên đỉnh đầu.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chân răng hàm trên đã bị xoay ngược 180° trong quá trình phát triển phôi thai! Ủa bác sĩ ơi, thế cái răng mọc ngược lên trời thì nó đâm đi đâu hả bác? Khám phá quá trình phát triển của". Bố cục: Lợn con mới sinh: Chú lợn con trơn láng đáng yêu bú mẹ; chưa hề có dấu vết của chiếc nanh mọc ngược nào lộ diện.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bệnh nhân sẽ khiến quý vị rùng mình hơn nữa: Khi 1 chú lợn hươu con vừa chào đời, gương mặt gã hoàn toàn bình thường, mõm trơn láng và chưa hề có chiếc nanh nào lộ diện! Nhưng khi bước". Bố cục: Tuổi dậy thì đau đớn: Chú lợn trẻ khoảng một hai tuổi với sống mũi sưng vù; đầu nanh nhọn hoắt đội thịt chuẩn bị xé toang da mặt.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "vào độ tuổi dậy thì khoảng 1-2 tuổi, chiếc mầm nanh quái đản bắt đầu đội thịt chồi lên! Da mõm gã sưng vù, căng tức cực độ cho đến khi mũi nanh sắc nhọn xé toang thớ thịt, đâm thủng một". Bố cục: Khoảnh khắc đâm thủng da mõm: Mũi nanh trên xé rách lớp thịt mũi, trồi thẳng ra ngoài không khí tạo thành hai lỗ thủng vĩnh viễn trên mặt gã.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "lỗ hổng vĩnh viễn trên sống mũi để vươn thẳng ra ngoài không khí! Một nghi thức trưởng thành đẫm nước màu mà tạo hóa bắt gã phải trải qua! Câu hỏi của cô trợ lý chạm đúng vào bi kịch giải". Bố cục: cô trợ lý thỏ trắng đeo tạp dề chữ thập đỏ bưng khay dụng cụ phẫu thuật ôm mặt rùng mình trước ca phẫu thuật tự nhiên đẫm nước màu mà cơ thể chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu phải gánh chịu từ khi còn trẻ.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "phẫu đau đớn nhất! Do chân răng hướng ngược lên đỉnh đầu, khi chiếc răng nanh bắt đầu mọc dài ra ở tuổi dậy thì, nó hoàn toàn không chui vào khoang miệng! Thay vào đó, chiếc răng nanh nhọn hoắt". Bố cục: Giải phẫu cặp nanh dưới: Chiếc nanh hàm dưới dài hai mươi xăng-ti-mét chìa sang hai bên má uốn cong lên trên như hai chiếc lưỡi mác sắc lẻm.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "đâm thẳng qua vòm họng trên, chọc thủng lớp mỡ, lớp thịt dày và xé rách lớp da mõm phía trên để chồi thẳng ra ngoài không khí! Một ca phẫu thuật tự nhiên đẫm nước màu mà chính cơ thể gã". Bố cục: Mô phỏng chiến đấu: chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu dùng cặp nanh dưới sắc bén húc tung kẻ thù trong một trận phục kích bảo vệ lãnh thổ giữa rừng rậm.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "phải gánh chịu! Chưa dừng lại ở đó, gã còn sở hữu thêm 1 cặp răng nanh ở hàm dưới dài tới 20 cm! Cặp nanh dưới này mọc chìa sang hai bên má rồi uốn cong lên trên như hai". Bố cục: Bức tranh giải phẫu đối chiếu: Nanh dưới là vũ khí cận chiến sinh tử; nanh trên là cỗ máy tự hủy đang từ từ dài ra.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chiếc lưỡi mác sắc bén! Đây là vũ khí cận chiến lợi hại giúp gã tự vệ trước các loài thú săn mồi và húc tung đối thủ trong những trận quyết đấu tranh giành lãnh thổ giữa rừng rậm nhiệt đới!". Bố cục: bác sĩ pháp y cú mèo đeo kính lúp một mắt và tạp dề da thuộc, cầm kẹp kim loại titan và cưa xương ghi chép chẩn đoán dị tật giai đoạn một vào hồ sơ bệnh án pháp y.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chẩn đoán triệu chứng số ba đưa chúng ta đến với nghịch lý rùng mình nhất của hồ sơ bệnh án! Sau khi đâm xuyên qua da mõm chồi lên trên trời, cặp răng nanh hàm trên của Gã bệnh". Bố cục: Mô hình 3D quỹ đạo tăng trưởng: Chiếc nanh trên của chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu liên tục dài ra không ngừng trong suốt cuộc đời do không có chân răng đóng kín.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nhân hi sinh bảo vệ tổ tiến hóa không dừng lại! Khác với răng của con người ngừng phát triển khi trưởng thành, răng nanh của lợn hươu không có chân răng đóng kín, nghĩa là chúng liên tục dài ra không ngừng trong". Bố cục: Cắt lớp vi thể răng: Cặp nanh trên xốp rỗng không có lớp men răng cứng bao bọc; bác sĩ pháp y cú mèo đeo kính lúp một mắt và tạp dề da thuộc, cầm kẹp kim loại titan và cưa xương dùng ngón tay gõ nhẹ thấy rung rinh dễ gãy.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "suốt cuộc đời! Điều nực cười nhất trong cấu tạo giải phẫu của cặp nanh trên này chính là độ bền cơ học của chúng! Mọi người thường nghĩ răng nanh lợn rừng phải cứng như thép và sắc bén vô". Bố cục: chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu cố ủi mõm vào tảng đá nhưng nanh trên lập tức mẻ một mảnh; gã giật mình vội vàng lùi lại bảo vệ cặp nanh quý giá.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "song đúng không? Hoàn toàn ngược lại! Cặp răng nanh hàm trên của Babirusa hoàn toàn không có lớp men răng cứng bao bọc bên ngoài, ruột xốp rỗng và cực kỳ giòn xốp! Nếu gã lỡ dại dùng cặp". Bố cục: Thước đo góc uốn cong: Chiếc nanh dài tới ba mươi đến bốn mươi xăng-ti-mét, uốn cong thành một vòng cung hoàn hảo nhắm thẳng về vầng trán.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nanh này để húc đá hay ủi gốc cây tìm thức ăn, chúng sẽ gãy vụn ngay lập tức! Nghĩa là gã mang trên mặt 1 cặp vũ khí hi sinh bảo vệ tổ vừa vô dụng vừa dễ gãy! Chiều dài của cặp". Bố cục: Khoảng cách tử thần: Thước kẹp đo khoảng cách giữa đầu nhọn chiếc nanh và da trán của chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu chỉ còn vỏn vẹn vài mi-li-mét mong manh.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nanh trên có thể chạm mốc 30 đến 40 cm! Và điều điên rồ là thay vì mọc thẳng đứng lên trời, chúng bắt đầu uốn cong dần thành 1 vòng cung hoàn hảo hướng ngược trở lại phía sau, nhắm". Bố cục: Đồng hồ đếm ngược tử thần quay tíc tắc: Càng sống thọ, nguy cơ đầu nanh cắm vào trán càng đến gần từng ngày.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "thẳng vào vầng trán của chính chủ nhân! Khoảng cách giữa đầu nhọn chiếc nanh và lớp xương trán cứ thế thu hẹp dần từng tháng, từng năm, tựa như 1 chiếc đồng hồ đếm ngược tử thần! Nếu 1 chú". Bố cục: Cá thể già mười lăm năm tuổi: Đầu nanh cắm thủng da trán, bắt đầu nghiền nát lớp xương sọ phía trước trong sự đau đớn cùng cực.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "lợn hươu may mắn sống thọ vượt mốc 15 năm tuổi trong tự nhiên mà không bị mài mòn răng, thảm kịch kinh hoàng sẽ chính thức xảy ra: Đầu nhọn của chiếc răng nanh dài 40 cm sẽ chạm". Bố cục: Tiêu bản hiện vật hộp sọ lợn hươu cổ xưa với cặp răng nanh uốn cong cắm xuyên qua xương trán vào khoang não: Hộp sọ cổ xưa bảo tàng với chiếc nanh cắm ngập vào bên trong khoang não; bằng chứng lịch sử chấn động.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "vào da trán, đâm xuyên qua lớp thịt đầu, nghiền nát lớp xương sọ cứng đặc và cắm thẳng vào mô não của chính nó! Một ca tử vong do chính chiếc răng trên mặt mình gây ra! Các nhà tự". Bố cục: bác sĩ pháp y cú mèo đeo kính lúp một mắt và tạp dề da thuộc, cầm kẹp kim loại titan và cưa xương và cô trợ lý thỏ trắng đeo tạp dề chữ thập đỏ bưng khay dụng cụ phẫu thuật nghiêm trang tưởng niệm trước cái chết bi thảm do chính vũ khí trên mặt gây ra.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nhiên học khi thám hiểm đảo Sulawesi đã từng tìm thấy những bộ xương sọ lợn hươu cổ xưa, nơi chiếc răng nanh mọc xuyên qua xương trán và trồi hẳn vào bên trong khoang não! Một cái chết từ từ". Bố cục: Câu hỏi lớn của tạo hóa: Tại sao chọn lọc tự nhiên lại không đào thải một cơ chế hi sinh bảo vệ tổ kỳ quặc nhường này suốt hàng triệu năm?
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "và vô cùng đau đớn! Bất kỳ bác sĩ nào khi nhìn vào cấu trúc này cũng phải thốt lên: Tại sao tiến hóa lại có thể tạo ra một lỗi thiết kế tàn nhẫn và ngớ ngẩn đến nhường này?". Bố cục: bác sĩ pháp y cú mèo đeo kính lúp một mắt và tạp dề da thuộc, cầm kẹp kim loại titan và cưa xương lật sang trang hồ sơ tiếp theo để giải mã bí ẩn chọn lọc giới tính.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, phong cách khắc gỗ thổ dân Dark Tribal Woodcut tương phản đen trắng sắc sảo và đỏ đất; chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong; nền trắng tinh khiết, KHÔNG chữ, không số, không logo). Bố cục: Bảng nghiên cứu sinh thái cổ xưa minh họa quy luật tự nhiên, biểu đồ đối chiếu tiến hóa và sự kỳ diệu của muôn loài.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bệnh nhân hi sinh bảo vệ tổ tiến hóa vẫn không bị tuyệt chủng mà vẫn ngang nhiên diễu hành khắp các hòn đảo Indonesia với cặp nanh hi sinh bảo vệ tổ trên mặt? Bác sĩ ơi, hay là do mấy con lợn cái nó mê". Bố cục: cô trợ lý thỏ trắng đeo tạp dề chữ thập đỏ bưng khay dụng cụ phẫu thuật giơ tay thắc mắc liệu có phải các nàng lợn cái mê mẩn những chàng lợn có cặp nanh cong chạm sát trán.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "những anh chàng có răng nanh cong vút thế ạ? Cô trợ lý lại một lần nữa đưa ra chẩn đoán chính xác tuyệt đối! Đáp án cho nghịch lý này nằm ở cán cân quyền lực của chọn lọc giới". Bố cục: Đấu trường sắc đẹp rừng già: nàng lợn hươu cái duyên dáng không có nanh trên, ánh mắt ngưỡng mộ nhìn chàng lợn đực với ánh mắt si tình đang ngắm nhìn chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu khoe cặp nanh vòng cung lộng lẫy.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tính! Trong mắt các nàng lợn hươu cái, một chàng lợn đực sở hữu cặp răng nanh trên uốn cong dài ngoằng chạm sát trán chính là biểu tượng tối thượng của sự quyến rũ và sức mạnh sinh tồn! Bởi". Bố cục: Biểu tượng sống thọ: Chỉ những chàng lợn có gen sinh tồn vượt trội mới sống sót đủ lâu để cặp nanh mọc dài chạm trán.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "vì sao? 1 con lợn đực có thể sống sót đến tuổi già, vượt qua bao mùa khô hạn, thú dữ và bệnh tật để cặp nanh mọc dài tới mức sắp đâm vào trán chứng minh một điều rõ ràng:". Bố cục: Trái tim tình yêu chiến thắng: chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu chiếm trọn tình cảm của bạn tình, thành công truyền lại bộ gen nanh hi sinh bảo vệ tổ cho bầy lợn con thế hệ sau.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gã sở hữu một bộ gen sinh tồn cực kỳ phi thường! Cặp nanh càng dài và càng nguy hiểm, gã càng dễ dàng chiếm trọn trái tim của các nàng lợn cái và truyền lại bộ gen hi sinh bảo vệ tổ này". Bố cục: Nghi thức quyết đấu độc lạ: Hai chàng lợn đực tuyệt đối không húc nanh vào nhau vì sợ gãy món trang sức quý giá.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "cho thế hệ sau trước khi chiếc nanh kịp cắm vào não gã! Chính vì cặp nanh trên quá giòn và quý giá, các chàng lợn đực đã sáng tạo ra một nghi thức thi đấu tranh giành bạn tình độc". Bố cục: Đấu quyền Anh rừng rậm: Hai chú lợn đứng thẳng dậy bằng hai chân sau, dùng mõm tỳ vào nhau vật lộn đẩy ngã đối thủ như võ sĩ hạng nặng.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nhất vô nhị: Khi hai gã lợn đực bước vào đấu trường quyết đấu, chúng tuyệt đối không bao giờ lao vào húc nanh đối đầu như lợn rừng thông thường vì sợ gãy mất món bảo bối quyến rũ! Thay". Bố cục: chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu giành chiến thắng vẻ vang, đứng ngạo nghễ gầm gừ khẳng định vị thế thủ lĩnh bầy đàn.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "vào đó, chúng đứng thẳng dậy bằng 2 chân sau như hai võ sĩ quyền Anh hạng nặng, dùng hai mõm tỳ chặt vào nhau rồi vật lộn đẩy ngã đối phương trong tiếng gầm gừ vang dội cánh rừng già!". Bố cục: bác sĩ pháp y cú mèo đeo kính lúp một mắt và tạp dề da thuộc, cầm kẹp kim loại titan và cưa xương gật gù thấu hiểu sức mạnh kỳ diệu của chọn lọc giới tính trong tự nhiên.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khám nghiệm toàn diện cơ thể của Gã bệnh nhân hi sinh bảo vệ tổ tiến hóa còn hé lộ những bí mật sinh học phi thường khác! Quý vị có biết tại sao người bản địa lại gọi loài này là Babirusa, ghép từ hai". Bố cục: Nguồn gốc tên gọi Babirusa: Ghép từ babi (lợn) và rusa (hươu); chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu sải bước kiêu hãnh với dáng dấp thanh thoát của loài hươu sao.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chữ babi nghĩa là con lợn và rusa nghĩa là con hươu không? Đó là vì gã sở hữu một vóc dáng hoàn toàn khác biệt so với họ hàng lợn ủn ỉn: Đôi chân thon dài, cao ráo và gân guốc tựa". Bố cục: Đôi chân hươu thần tốc: chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu phi nước đại băng qua các vùng đầm lầy hiểm trở trên hòn đảo Sulawesi hoang sơ.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "như 1 chú hươu sao dũng mãnh! Nhờ đôi chân hươu thần thánh này, lợn hươu có thể phi nước đại qua những đầm lầy hiểm trở và đặc biệt là khả năng bơi lội siêu đẳng! Chúng có thể bơi vượt qua". Bố cục: Bậc thầy bơi biển: chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu ung dung bơi vượt qua eo biển sóng cuộn nối liền giữa các hòn đảo để tìm kiếm nguồn thức ăn trù phú.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "các eo biển rộng hàng cây số nối liền giữa các hòn đảo hoang sơ của quần đảo Sulawesi để tìm kiếm nguồn thức ăn mới mà không sợ bị chết đuối! Đặt ống soi vào ổ bụng của gã, hệ tiêu hóa". Bố cục: Nội soi ổ bụng: Dạ dày nhiều ngăn phức tạp của chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu hiện rõ trên màn hình y tế; cơ chế lên men vi sinh vật giống hệt dạ dày loài bò nhai lại.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "sẽ khiến các chuyên gia giải phẫu phải kinh ngạc: Thay vì dạ dày đơn giản như loài lợn ăn tạp, dạ dày của Babirusa phát triển thành cấu trúc nhiều ngăn phức tạp, chứa đầy các chủng vi sinh vật cộng sinh". Bố cục: Lò phản ứng sinh học: Các chủng vi sinh vật cộng sinh miệt mài phân giải chất xơ thô cứng và trung hòa độc tố từ nấm rừng.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tương tự như dạ dày của loài bò nhai lại! Hệ thống này giúp gã tiêu hóa triệt để chất xơ xenlulozo thô cứng từ lá cây, rễ củ và thậm chí là những loại nấm rừng có độc tố cao! Để tránh". Bố cục: Hành hương giải độc: Đàn lợn hươu tụ tập bên mỏ bùn khoáng tự nhiên và suối nước nóng địa nhiệt bốc khói nghi ngút.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "cho chiếc nanh trên đâm vào trán quá sớm, những chú lợn đực thông minh thường xuyên tìm đến những thân cây gỗ lim cứng hoặc đá tảng để cọ xát và mài mòn đầu răng nanh! Đó là cuộc chạy đua sinh". Bố cục: chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu cần mẫn liếm láp bùn khoáng canxi và natri để thanh lọc cơ thể và nuôi dưỡng khung xương.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tồn từng ngày giữa sự phát triển hi sinh bảo vệ tổ của chiếc răng và nỗ lực mài mòn kiên trì của chính chủ nhân! Chưa hết đâu nhé, chế độ ăn nhiều lá cây rừng chứa độc tố tanin đòi hỏi Gã bệnh nhân". Bố cục: Cuộc chiến mài răng cứu mạng: chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu cọ xát cặp nanh trên vào thân cây gỗ lim cứng cáp để mài mòn mũi nhọn trước khi nó chạm trán.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "hi sinh bảo vệ tổ tiến hóa phải có một liệu trình giải độc cực kỳ thông minh: Các nhà nghiên cứu phát hiện ra đàn lợn hươu thường xuyên hành hương đến các mỏ đá muối khoáng tự nhiên và suối nước nóng địa nhiệt". Bố cục: Vệt mài sáng bóng trên thân cây lim; chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu thở phào nhẹ nhõm khi khoảng cách an toàn với hộp sọ được nới rộng.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "ở đảo Sulawesi! Tại đây, gã cần mẫn liếm láp những mảng bùn khoáng giàu canxi và natri để trung hòa độc tố trong dạ dày, đồng thời bổ sung khoáng chất giúp nuôi dưỡng cặp nanh khổng lồ mọc dài liên tục!". Bố cục: bác sĩ pháp y cú mèo đeo kính lúp một mắt và tạp dề da thuộc, cầm kẹp kim loại titan và cưa xương ghi nhận liệu trình tự điều trị sinh tồn thông minh bậc nhất của bệnh nhân.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hồ sơ bệnh án số 46 chính thức khép lại với kết luận chẩn đoán: Lợn Hươu Babirusa là một kiệt tác dị biệt và là lời cảnh tỉnh triết lý sâu sắc của tự". Bố cục: bác sĩ pháp y cú mèo đeo kính lúp một mắt và tạp dề da thuộc, cầm kẹp kim loại titan và cưa xương gấp lại tập hồ sơ bệnh án số bốn mươi sáu; bức tranh phong cảnh rừng nhiệt đới Sulawesi cổ xưa hiện lên trầm mặc.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nhiên! Trong cuộc sống, đôi khi những vũ khí, những hào quang hay những lợi thế mạnh mẽ nhất mà bạn dày công vun đắp, nếu không được kiểm soát và định hướng đúng đắn,". Bố cục: Bài học triết lý sinh tồn: chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu đứng giữa ánh hoàng hôn với cặp nanh cong vút; lời cảnh tỉnh về việc kiểm soát vũ khí nội tại trong cuộc sống.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "lại chính là thứ quay mũi giáo lại đâm vào chính bạn! Biết tiết chế sức mạnh và kiểm soát tham vọng chính là bài học sinh tồn đắt giá nhất! Nếu được quyền can". Bố cục: Màn hình tương tác người xem: Hai lựa chọn phẫu thuật hài hước: Nút 1 bẻ cong nanh ra ngoài cứu mạng, Nút 2 để nguyên nanh cong cho gã tán gái.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "thiệp vào quy trình tiến hóa của chú lợn hươu Babirusa, bạn sẽ chọn bẻ cong chiếc nanh ra ngoài để gã an toàn hay giữ nguyên vẻ đẹp quyến rũ chết người này? Hãy". Bố cục: cô trợ lý thỏ trắng đeo tạp dề chữ thập đỏ bưng khay dụng cụ phẫu thuật giơ biển chỉ dẫn mời quý khán giả để lại ý kiến bình luận chẩn đoán bên dưới video.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "để lại bình luận chẩn đoán của bạn bên dưới nhé! Còn bây giờ, hãy chuẩn bị cùng xưởng chế tạo vũ khí sinh học bước vào bản vẽ kỹ thuật của tập 47! Một". Bố cục: Bản vẽ kỹ thuật tập bốn mươi bảy hé lộ: Chú hươu cao cổ với chiếc cổ dài hai mét sừng sững giữa thảo nguyên Châu Phi nắng rực.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "sinh vật đồ sộ trên thảo nguyên Châu Phi sở hữu chiếc cổ dài tới hai mét, một trái tim nặng 11 ki-lô-gam với huyết áp cao gấp đôi con người, và 1 hệ thống". Bố cục: Sơ đồ giải phẫu trái tim mười một cân và hệ thống van tĩnh mạch chống nổ não khi chú hươu cúi đầu uống nước.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "van thủy lực vi mô thần kỳ giúp nó cúi đầu uống nước mà không bị nổ tung mạch nước màu não! Bạn có biết cỗ máy thủy lực sinh học vĩ đại này là ai không?". Bố cục: Màn hình kết thúc: Dòng chữ HẸN GẶP LẠI Ở TẬP 47 HƯƠU CAO CỔ lung linh với lời kêu gọi đăng ký kênh theo dõi.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Khi tiến hóa chơi khăm tàn nhẫn: Loài lợn sở hữu cặp răng nanh tự đâm thủng da mặt rồi". Bố cục: Cận cảnh mở đầu: chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán với cặp răng nanh dài tới bốn mươi xăng-ti-mét uốn cong thành vòng cung sắp cắm vào trán; ánh mắt ngơ ngác tấu hài.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "uốn cong cắm thẳng vào não của chính nó! Đây là Lợn Hươu Babirusa, loài động vật kỳ lạ đặc". Bố cục: Đây là Lợn Hươu Babirusa hòn đảo Sulawesi, Indonesia mang gen hi sinh bảo vệ tổ tiến hóa kỳ lạ nhất hành tinh.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "hữu của hòn đảo Sulawesi, Indonesia! Ở con đực, mầm răng nanh hàm trên bị xoay ngược 180°, đâm xuyên qua". Bố cục: Mầm răng nanh trên xoay ngược một trăm tám mươi độ, đâm xuyên qua da mõm chồi thẳng ra ngoài không khí.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "thịt mõm chồi lên trời. Chiếc nanh dài tới 40 cm uốn cong thành vòng cung hướng thẳng về trán,". Bố cục: Chiếc nanh mọc dài bốn mươi xăng-ti-mét uốn cong về trán, ở lợn già có thể đâm xuyên xương sọ cắm vào não gây tử vong.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "và ở những con già, mũi nanh nhọn hoắt sẽ đâm xuyên xương sọ cắm vào não gây tử vong!". Bố cục: Nàng lợn cái si tình đứng ngắm chàng lợn đực; nanh càng cong sát trán càng chứng minh gã sống thọ và quyến rũ.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Kỳ lạ thay, gen hi sinh bảo vệ tổ này vẫn tồn tại hàng triệu năm vì lợn cái mê mẩn những con đực". Bố cục: Khi quyết đấu tranh bạn tình, hai chú lợn đứng bằng hai chân sau vật lộn như võ sĩ quyền Anh để tránh làm gãy nanh giòn.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "có nanh cong sát trán, coi đó là biểu tượng sống thọ và quyến rũ! Chúng phải liên tục cọ". Bố cục: chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán cần mẫn cọ nanh vào thân cây gỗ lim mài mòn mũi nhọn để tự cứu lấy mạng sống của mình.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú lợn hươu babirusa hoạt hình màu xám tro với cặp răng nanh uốn cong đâm ngược vào trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "răng vào cây để mài mòn, tự cứu lấy mạng sống của mình trước món quà chết người của tạo hóa!". Bố cục: Một nghịch lý tiến hóa chết người của tạo hóa; mời đăng ký kênh xem trọn bộ bệnh án số bốn mươi sáu.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/56 của video YouTube về Lợn Hươu Babirusa). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa vẽ tay đặc trưng cho chủ đề, nét mực sắc nét, màu sắc tương phản cuốn hút, tối giản giàu tính biểu tượng khoa học; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/8 của video YouTube Shorts về Lợn Hươu Babirusa). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa vẽ tay đặc trưng cho chủ đề, nét mực sắc nét, màu sắc tương phản cuốn hút, tối giản giàu tính biểu tượng khoa học; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú lợn hươu babirusa hoạt hình góc cạnh bí hiểm màu xám tro đá núi lửa, cặp nanh hàm trên mọc ngược đâm xuyên da mõm uốn cong thành vòng cung hướng về phía trán, cặp nanh dưới nhọn hoắt chìa sang hai bên má, đôi chân thon dài gân guốc như chân hươu. 
```
</details>

## 7. SEO

- **title:** Nghịch Lý Tiến Hóa Tự Sát: Cặp Răng Nanh Tự Đâm Thủng Hộp Sọ?! | Lợn Hươu Babirusa | Tập 46
- **hook_paragraph:** Khám phá bệnh án kỳ quái của Lợn Hươu Babirusa — loài lợn rừng Indonesia có cặp răng nanh trên xoay 180 độ đâm thủng da mõm, uốn cong 40cm đâm xuyên hộp sọ nhưng vẫn được con cái mê mẩn!
- **question:** Nếu được quyền phẫu thuật cho chú lợn Babirusa, bạn sẽ bẻ nanh ra ngoài cứu mạng hay để nguyên cho gã tán gái?
- **next_teaser:** Tập 47: Hươu Cao Cổ — cỗ máy thủy lực cổ dài 2m và van tĩnh mạch chống nổ não!
- **shorts_title:** Tiến hóa chơi khăm: Răng nanh tự đâm thủng hộp sọ?! 🐗 #shorts #babirusa
- **shorts_desc:** Khám phá Lợn Hươu Babirusa — loài lợn có cặp răng nanh mọc ngược đâm xuyên da mặt, uốn cong 40cm đâm thủng hộp sọ chính mình!
- **bullets:** Răng nanh hàm trên xoay ngược 180 độ, đâm xuyên qua da mõm chồi lên trời · Nanh dài 40cm uốn cong thành vòng cung đâm xuyên xương trán vào não lợn già · Gen tự sát tồn tại vì con cái coi nanh dài sát trán là biểu tượng sống thọ quyến rũ · Đôi chân thon dài như hươu chạy nhanh, bơi vượt biển và dạ dày lên men như bò
- **tags:** lon huou babirusa, babirusa, babyrousa, rang nanh dam vao so, tien hoa tu sat, the gioi dong vat, ve chuyen hoang da, dong vat ky di, whiteboard animation
- **hashtags:** #LonHuouBabirusa #Babirusa #TheGioiDongVat #VeChuyenHoangDa #KhoaHoc

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-46-lon-huou-babirusa
python src/episode/pipeline.py tts    projects/tap-46-lon-huou-babirusa     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-46-lon-huou-babirusa     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-46-lon-huou-babirusa     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-46-lon-huou-babirusa              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-46-lon-huou-babirusa --force
python scripts/beat_sheet.py projects/tap-46-lon-huou-babirusa               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-46-lon-huou-babirusa/audio/shorts.wav projects/tap-46-lon-huou-babirusa/renders/tap-46-lon-huou-babirusa_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-46-lon-huou-babirusa
python src/episode/pipeline.py seo    projects/tap-46-lon-huou-babirusa
python src/episode/episode_doc.py     projects/tap-46-lon-huou-babirusa
```
