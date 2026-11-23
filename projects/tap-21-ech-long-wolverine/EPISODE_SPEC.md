# TẬP 21 — ẾCH LÔNG WOLVERINE · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-21-ech-long-wolverine`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-21-ech-long-wolverine`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F1` · **Persona giọng:** `bac_si` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Ếch Lông Wolverine |
| Tiêu đề YouTube | Loài Ếch Tự Bẻ Xương Đâm Thủng Da Làm Vuốt Wolverine?! |
| Video dài | `renders/tap-21-ech-long-wolverine_long.mp4` — 9:41.4 (581.4s) |
| Shorts | `renders/tap-21-ech-long-wolverine_shorts.mp4` — 0:54.5 (54.5s) |
| Thumbnail | `renders/tap-21-ech-long-wolverine_thumbnail.jpg` |
| Số hình | dài 82 beat / 82 ảnh riêng; Shorts 12 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.1**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/82 của video YouTube về Ếch Lông Wolverine). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán. Nhân vật phụ cố định: ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế, vẻ mặt bất lực hài hước; cô trợ lý phòng khám hoạt hình mặc áo blouse xanh nhạt, kẹp tập hồ sơ bệnh án. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — CA CẤP CỨU TỰ BẺ XƯƠNG ĐÂM THỦNG DA
*Badge:* `BỆNH ÁN #21` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene01_p0.wav` (406 ký tự) · mood `tram_bi_an`

```text
Đêm khuya tại phòng cấp cứu dã chiến giữa rừng mưa Trung Phi. Đèn còi hú vang, cả ê-kíp trực bật dậy đón một ca chấn thương kỳ lạ nhất lịch sử ngành y. Bệnh nhân tự bước vào phòng khám với tám vết rách gọn lỏn dưới lòng bàn chân... Không phải do thú dữ cắn. Không phải do dẫm phải gai rừng. Mà là do chính bệnh nhân tự gồng cơ... bẻ gãy mối nối xương ngón chân mình rồi đâm xuyên qua da thịt chui ra ngoài!
```
**Part 1** → `audio/vs/scene01_p1.wav` (98 ký tự) · 🎭 cameo `co_tro_ly`

```text
Bác sĩ ơi, em băng bó xong rồi nhưng nhìn mặt bệnh nhân vẫn tỉnh bơ như không có chuyện gì luôn ạ!
```
**Part 2** → `audio/vs/scene01_p2.wav` (487 ký tự) · mood `hao_hung`

```text
[surprise-oh] Các đồng nghiệp nhìn kỹ hồ sơ đi: bệnh nhân số hai mươi mốt không phải gấu, không phải sói, mà là một con ếch! [laughter] Đây là Ếch Lông Wolverine, tên khoa học cực kỳ hầm hố, sống ẩn dật dọc các dòng suối núi ở Ca-mơ-run và vùng Trung Phi. Con đực trưởng thành dài khoảng mười đến mười ba xăng-ti-mét, to cỡ nắm tay người lớn. Trông ngoài mặt thì lầm lì mũm mĩm như cục đất sét biết thở, nhưng trong phòng khám này, chúng tôi gọi thẳng nó bằng biệt danh: Dị Nhân Đầm Lầy!
```
**Part 3** → `audio/vs/scene01_p3.wav` (598 ký tự) · mood `nghiem_trang_gia`

```text
Điều khiến tôi bất lực nhất ngay từ vòng tiếp nhận là quy luật ngược đời của loài này. Ở phần lớn thế giới ếch nhái, con cái lúc nào cũng to béo gấp rưỡi con đực để mang trứng. Riêng nhà Dị Nhân Đầm Lầy thì ngược hẳn: con cái chỉ dài chín xăng-ti-mét, còn ông chồng lại phổng phao tới mười ba xăng-ti-mét! [surprise-ah] Chưa hết, mùa thường nó trơn láng như bao con ếch khác, nhưng cứ đến mùa chăm con, hai bên sườn nó tự mọc ra một bộ lông xù xì như râu quai nón! Hôm nay, tôi mời các đồng nghiệp cùng soi đèn công suất lớn để khám nghiệm bốn hạng mục kỳ dị nhất trên cơ thể gã dị nhân tự hủy này!
```

### scene02 — CƠ CHẾ XƯƠNG TRẦN TỰ ĐÂM THỦNG DA LÀM VUỐT
*Thẻ chương:* VUỐT XƯƠNG TRẦN ĐÂM THỦNG DA THỊT

*Badge:* `CHỤP X-QUANG` · *mood mặc định:* `nghiem_trang_gia`

**Part 0** → `audio/vs/scene02_p0.wav` (607 ký tự) · mood `nghiem_trang_gia`

```text
Hạng mục khám đầu tiên: Chụp X-quang hai bàn chân sau! Nhìn bằng mắt thường, bàn chân của Dị Nhân Đầm Lầy tròn ủm, mềm mại và có màng bơi trông cực kỳ hiền lành vô hại. Nhưng khi đặt chân nó lên máy chụp cắt lớp, cả phòng khám suýt nữa làm rơi cả tách cà phê xuống sàn! [surprise-wa] Ẩn sâu bên dưới lớp da thịt mịn màng kia là cả một kho dao bấm sinh học giấu kín. Ở mèo, chó hay đại bàng, móng vuốt được làm từ chất sừng kê-ra-tin mọc sẵn bên ngoài giống như móng tay của chúng ta. Còn vuốt của Dị Nhân Đầm Lầy thì không hề có lớp sừng bọc ngoài nào cả! Thứ chọc ra ngoài là xương trần một trăm phần trăm!
```
**Part 1** → `audio/vs/scene02_p1.wav` (434 ký tự) · mood `hao_hung`

```text
Cơ chế khai hỏa của nó hoạt động chẳng khác gì phim hành động viễn tưởng! Năm hai ngàn lẻ tám, tiến sĩ Đa-vít Blách-bơn tại Đại học Ha-vớt đã soi kính hiển vi giải phẫu và giải mã bí ẩn này. Lúc bình thường, đầu xương nhọn hoắt hình móc câu nằm ngoan ngoãn dưới da, được neo chặt vào một cục xương nhỏ xíu ở đầu ngón nhờ dải mô liên kết giàu cô-la-gen. Nhờ chốt an toàn đó, nó đi lại chạy nhảy thoải mái mà không tự đâm vào chân mình!
```
**Part 2** → `audio/vs/scene02_p2.wav` (503 ký tự) · mood `don_dap`

```text
Nhưng chỉ cần một kẻ săn mồi vừa thò tay chạm vào lưng! Dị Nhân Đầm Lầy lập tức co cực mạnh bó cơ gập dưới bàn chân! Lực kéo giật đứt phăng mối nối cô-la-gen giữ chốt an toàn! Đầu xương nhọn lập tức xoay gập xuống dưới và chọc thủng lớp đệm da thịt của tám ngón chân sau! [surprise-oh] Các bác sĩ đo được lớp vỏ xương ở gốc chỉ dày không phẩy không hai mi-li-mét, nhưng càng ra tới mũi nhọn càng đặc cứng gấp hơn sáu lần, đạt không phẩy mười ba mi-li-mét, biến mũi xương thành một lưỡi dao găm thực thụ!
```
**Part 3** → `audio/vs/scene02_p3.wav` (685 ký tự) · mood `bi_hai`

```text
Nghe tới đây chắc các đồng nghiệp đều toát mồ hôi hột: thế lúc hết đánh nhau rồi, làm sao nó thu vuốt vào được? [question-ah] Chẳng lẽ đứng đó chịu trận với tám ngón chân lòi xương mãi sao? Câu trả lời còn làm bác sĩ chúng tôi ngơ ngác hơn: trên bàn chân nó hoàn toàn không có bất kỳ bó cơ nào dùng để kéo chiếc vuốt trở lại! Các nhà khoa học nhận định rằng khi cơn nguy hiểm qua đi và cơ chân thả lỏng, chiếc vuốt xương có lẽ tự trượt ngược vào trong một cách thụ động. Còn vết thương rách da kia thì nhờ khả năng hồi phục nhanh của loài lưỡng cư mà tự liền lại như chưa từng có chuyện gì xảy ra! Đúng là siêu anh hùng nhưng... mỗi lần rút vũ khí hơi tốn băng gạc một chút! [laughter]
```

### scene03 — BỘ LÔNG MẠCH MÁU GIÚP THỞ VÀ LÁ PHỔI TEO TÓP
*Thẻ chương:* LÔNG MẠCH MÁU HÚT OXY DƯỚI SUỐI

*Badge:* `NỘI SOI DA` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene03_p0.wav` (310 ký tự) · mood `hao_hung`

```text
Chuyển sang hạng mục khám thứ hai: Soi da liễu và kiểm tra hệ hô hấp! Thú thật với các đồng nghiệp, lúc mới đọc tên bệnh nhân là Ếch Lông, tôi cứ tưởng nó bị rụng tóc rơi vào người hoặc tiến hóa ngược mọc lông giống chuột. Nhưng khi đặt mẫu da dưới kính hiển vi, sự thật lại nằm ở một chân trời hoàn toàn khác!
```
**Part 1** → `audio/vs/scene03_p1.wav` (104 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Trời đất ơi, đi bơi giữa suối lạnh mà anh mặc nguyên cái áo lông rậm rạp thế kia không thấy vướng víu à?
```
**Part 2** → `audio/vs/scene03_p2.wav` (541 ký tự) · mood `hao_hung`

```text
[laughter] Chú ếch hàng xóm thắc mắc rất đúng trọng tâm, nhưng thực ra thứ mọc đầy hai bên sườn và đùi của Dị Nhân Đầm Lầy hoàn toàn không phải lông hay tóc gì cả! Đó là hàng trăm sợi nhú da mềm, đường kính mỗi sợi chỉ từ không phẩy ba mươi lăm đến không phẩy bốn mươi lăm mi-li-mét — mỏng tương đương sợi cước mảnh. Bên trong mỗi sợi nhú da ấy chạy chằng chịt những mạch máu mao mạch sát ngay lớp biểu bì ngoài cùng. Và kỳ lạ nhất là chỉ có con đực mới mọc bộ lông kỳ dị này vào đúng mùa sinh sản, khoảng từ tháng tư đến tháng sáu hàng năm!
```
**Part 3** → `audio/vs/scene03_p3.wav` (497 ký tự) · mood `nghiem_trang_gia`

```text
Tại sao tạo hóa lại gắn hàng trăm sợi tua rua mạch máu lên hông một ông bố ếch? Câu trả lời được nhà động vật học Nô-bờ tìm ra từ năm một ngàn chín trăm hai mươi lăm khi mổ xẻ nội soi lá phổi của nó. Hóa ra phổi của Dị Nhân Đầm Lầy con đực có cấu tạo vô cùng kỳ quặc và hạn chế so với nhu cầu năng lượng khổng lồ lúc nó vận động cơ bắp! Khi con cái đẻ trứng xong rồi lên bờ rừng lá khô đi chơi, ông bố ếch phải ở lại lặn ngụp dưới lòng suối đá chảy xiết để canh giữ bọc trứng suốt nhiều tuần liền!
```
**Part 4** → `audio/vs/scene03_p4.wav` (681 ký tự) · mood `hao_hung`

```text
Ngồi lì dưới nước mà không được ngoi lên thở liên tục, lại phải gồng mình trông con, lượng oxy qua lá phổi tí hon hoàn toàn không đủ dùng! Thế là cơ thể nó tự kích hoạt bản nâng cấp sinh học: mọc tua tủa hàng trăm sợi nhú da giàu mạch máu ở sườn và đùi để tăng gấp bội diện tích tiếp xúc với nước! [surprise-oh] Những sợi lông giả đó hoạt động chẳng khác nào một dàn mang cá tạm thời, hút oxy trực tiếp từ dòng suối xuyên qua da vào thẳng máu! Chưa hết, lúc ẩn mình dưới đá suối, đám tua rua lất phất theo dòng nước còn trông y hệt đám rêu tảo, giúp ông bố ngụy trang che mắt kẻ săn mồi! Hết mùa giữ trứng, bộ lông tự động teo rụng sạch sẽ, trả lại vẻ bảnh bao gọn gàng! [laughter]
```

### scene04 — SO SÁNH HỘI TỰ HỦY VÀ GAI BÁM SUỐI XIẾT
*Thẻ chương:* ĐÂM XƯƠNG SƯỜN & VẾT CÀO CHẢY MÁU

*Badge:* `GIÁM ĐỊNH TIẾN HÓA` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene04_p0.wav` (337 ký tự) · mood `don_dap`

```text
Hạng mục khám thứ ba: Kiểm tra hồ sơ gia phả dị nhân! Khi tiến sĩ Đa-vít Blách-bơn kiểm tra mẫu vật của sáu mươi ba loài ếch châu Phi trong bảo tàng, ông phát hiện không chỉ mình Dị Nhân Đầm Lầy biết chơi chiêu rút xương làm vuốt! Tổng cộng có tới mười một loài thuộc ba chi họ hàng ở Trung Phi đều sở hữu bộ vũ khí giấu kín đáng sợ này!
```
**Part 1** → `audio/vs/scene04_p1.wav` (457 ký tự) · mood `don_dap`

```text
Nếu mở rộng hồ sơ sang các loài lưỡng cư khác trên thế giới, hội tự hủy còn có một thành viên cực gắt khác là loài kỳ giông gân sườn Tây Ban Nha: khi bị tấn công, nó đẩy thẳng những đầu xương sườn nhọn hoắt xuyên qua lớp da hai bên hông kèm chất độc! Tuy vậy, cơ chế bẻ đứt mối nối xương ở đầu ngón chân để phóng ra chiếc vuốt cong sắc bén như dao găm của ếch châu Phi vẫn là thiết kế độc nhất vô nhị trong toàn bộ giới động vật có xương sống! [surprise-wa]
```
**Part 2** → `audio/vs/scene04_p2.wav` (379 ký tự) · mood `hao_hung`

```text
Chưa hết đâu các đồng nghiệp, hãy soi kỹ cả đôi bàn tay trước của ông bố Dị Nhân Đầm Lầy! Nếu chân sau giấu dao găm để chiến đấu, thì trên ngón cái bàn tay trước của con đực lại mọc lên ba hàng gai sừng màu đen cứng như kìm sắt! Bộ gai nhám này không dùng để đánh nhau, mà để khóa chặt vào thân bạn đời hoặc bám vững vào tảng đá trơn trượt giữa dòng suối chảy xiết trong mùa mưa!
```
**Part 3** → `audio/vs/scene04_p3.wav` (500 ký tự) · mood `bi_hai`

```text
Nhưng đừng thấy nó nhỏ bé mà chủ quan đưa tay ra nựng! Năm một ngàn chín trăm năm mươi tư, nhà tự nhiên học nổi tiếng người Anh Giê-rôn Đu-reo từng thuật lại cú sốc nhớ đời trong cuốn sách của ông. Khi ông dùng tay không bắt sống một chú Dị Nhân Đầm Lầy hoang dã, nó lập tức đạp mạnh hai chân sau, phóng vuốt xương cào thẳng vào lòng bàn tay ông những vết rách sâu hoắm chảy máu đầm đìa! [sigh] Đúng là nhìn mặt hiền khô tưởng cục đất biết nhảy, ai ngờ chạm vào là mất ngay miếng thịt tay! [laughter]
```
**Part 4** → `audio/vs/scene04_p4.wav` (79 ký tự) · 🎭 cameo `be_con`

```text
Bác sĩ ơi, thế mấy con nòng nọc mới nở ra đã có vuốt xương đâm rách tay chưa ạ?
```
**Part 5** → `audio/vs/scene04_p5.wav` (294 ký tự) · mood `hao_hung`

```text
Câu hỏi rất hay! Nòng nọc bé xíu sống dưới nước thì chưa mọc vuốt đâu cháu ạ, nhưng ở những loài họ hàng gần cùng nhóm, ngay cả những chú ếch con mới bước lên bờ cũng đã trang bị sẵn bộ vuốt xương giấu kín dưới chân để phòng thân rồi! Tuổi nhỏ tài cao, vừa ra đời đã mang theo vũ khí hạng nặng!
```

### scene05 — THỢ SĂN PHẢI DÙNG GIÁO BA MŨI TRÁNH VUỐT
*Thẻ chương:* THỢ SĂN PHẢI CHẾ GIÁO BA LƯỠI ĐỂ BẮT

*Badge:* `THỰC ĐỊA CAMEROON` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene05_p0.wav` (300 ký tự) · mood `hao_hung`

```text
Hạng mục khám thứ tư: Khảo sát hiện trường thực địa tại rừng núi Ca-mơ-run! Trong khi giới khoa học phương Tây đến tận năm hai ngàn lẻ tám mới giải mã hoàn toàn cơ chế vuốt xương của Dị Nhân Đầm Lầy, thì người dân bản địa vùng Trung Phi đã... biết thừa độ nguy hiểm của nó từ hàng trăm năm trước rồi!
```
**Part 1** → `audio/vs/scene05_p1.wav` (424 ký tự) · mood `don_dap`

```text
Tại nhiều làng ở Ca-mơ-run, thịt ếch lông nướng là một món ăn truyền thống rất được ưa chuộng. Nhưng có một quy tắc bất thành văn khi đi săn ban đêm: tuyệt đối không bao giờ thò tay không chộp lấy con ếch! Nếu lỡ tay túm nhầm, tám chiếc vuốt xương ở hai chân sau sẽ đạp phăng vào cổ tay gây chảy máu rất đau đớn! Vậy nên các thợ săn phải vác theo dao rựa hoặc chế tạo riêng những cây giáo cán dài để giữ khoảng cách an toàn!
```
**Part 2** → `audio/vs/scene05_p2.wav` (384 ký tự) · mood `hao_hung`

```text
Và đây là cú trớ trêu lịch sử khiến cả phòng khám phải bật cười: nhiều cây giáo chuyên dụng dùng để săn loài ếch Wolverine này được rèn với phần đầu có đúng ba lưỡi nhọn chĩa ra phía trước — trông chẳng khác nào bộ vuốt ba ngạnh bằng kim loại của nhân vật Người Sói Wolverine ngoài đời thực! [laughter] Muốn săn Người Sói đầm lầy, thợ săn buộc phải tự chế vũ khí Người Sói để đối đầu!
```
**Part 3** → `audio/vs/scene05_p3.wav` (556 ký tự) · mood `nghiem_trang_gia`

```text
Thậm chí người dân tộc Ba-cốt-xi ở Ca-mơ-run xưa kia còn lưu truyền một huyền thoại cực kỳ thú vị: họ tin rằng những con ếch mọc lông kỳ quái này không sinh ra từ dưới bùn, mà... rơi thẳng từ trên bầu trời xuống cùng những cơn mưa rào! [surprise-oh] Nhiều cặp vợ chồng hiếm muộn còn tin ăn món ếch này sẽ giúp sinh con thuận lợi. Đến nay, khoa học đã xác nhận nó chẳng hề rơi từ vũ trụ nào cả, mà chỉ là một kỳ quan tiến hóa bản địa chính hiệu — thậm chí còn được xếp vào nhóm ba phẩy năm phần trăm loài lưỡng cư có độ độc đáo di truyền cao nhất hành tinh!
```

### scene06 — ĐƠN THUỐC BẤT LỰC VÀ BÓNG ĐEN BÍ ẨN TẬP SAU
*Thẻ chương:* SẴN SÀNG CHỊU ĐAU ĐỂ BẢO VỆ SỰ SỐNG

*Badge:* `KẾT LUẬN Y KHOA` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene06_p0.wav` (375 ký tự) · mood `am_ap`

```text
Tổng kết hồ sơ bệnh án số hai mươi mốt. Thực lòng mà nói, tôi vẫn còn rùng mình mỗi khi nhìn lại tấm phim X-quang bàn chân của Dị Nhân Đầm Lầy. Để sinh tồn giữa rừng mưa khắc nghiệt đầy rẫy rắn rết và chim săn mồi, chú ếch nhỏ bé dài chỉ mười ba xăng-ti-mét này chấp nhận tự làm đau chính mình, bẻ mối nối xương đâm rách da thịt chỉ trong tích tắc để đổi lấy cơ hội sống sót!
```
**Part 1** → `audio/vs/scene06_p1.wav` (457 ký tự) · mood `hao_hung`

```text
Và ẩn sau vẻ ngoài lầm lì cùng biệt danh quái vật kinh dị, đó lại là một ông bố mẫu mực đến mức đáng nể: sẵn sàng mọc cả bộ lông mạch máu kỳ dị để ngồi lặng lẽ dưới dòng suối lạnh buốt suốt nhiều tuần liền, bảo vệ từng quả trứng nhỏ bé cho thế hệ tương lai. Kê đơn cuối cùng: cho bệnh nhân xuất viện ngay lập tức, tặng thêm một cuộn băng cá nhân dự phòng và khuyến cáo người xem... đừng bao giờ thử bắt chước! Ký tên: bác sĩ đã hoàn toàn bất lực! [laughter]
```
**Part 2** → `audio/vs/scene06_p2.wav` (279 ký tự) · mood `hao_hung`

```text
Còn các đồng nghiệp thì sao? Nếu bắt buộc phải chọn một trong hai trang bị của Dị Nhân Đầm Lầy: sở hữu vuốt xương giấu kín nhưng mỗi lần rút hơi rát tay, hay mọc lông kín sườn để lặn thở dưới nước không cần bình oxy, bạn chọn cái nào? Hãy bình luận lựa chọn của bạn bên dưới nhé!
```
**Part 3** → `audio/vs/scene06_p3.wav` (599 ký tự) · mood `am_ap`

```text
Hồ sơ phòng khám hôm nay xin tạm đóng. Nhưng tập sau, chúng ta sẽ chuyển thẳng sang phòng thí nghiệm năm cấp độ để đối mặt với một ca tiến hóa còn điên rồ hơn nữa! Một sinh vật nhỏ xíu sống dưới nước với khuôn mặt lúc nào cũng mỉm cười, trên đầu mọc sáu chiếc sừng lông xù như ăng-ten ngoài hành tinh... Điều khiến các nhà khoa học mất ngủ là dù có bị mất chân, đứt tủy sống, thậm chí mất cả một phần ba trái tim và một phần não bộ, nó vẫn tự mọc lại nguyên vẹn hoàn toàn mà không để lại lấy một vết sẹo nào! Đố các bạn biết bóng đen bí ẩn kỳ sau là loài vật nào? Hãy đoán ngay ở phần bình luận nhé!
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Bệnh nhân này vào phòng cấp cứu không phải vì bị thú dữ cắn, mà vì nó vừa... tự bẻ gãy xương ngón chân mình đâm thủng qua da! [laughter] Xin giới thiệu Ếch Lông Wolverine, gã dị nhân dài mười ba xăng-ti-mét sống dọc các dòng suối núi ở Trung Phi. Dưới lớp da tám ngón chân sau của nó giấu sẵn những chiếc móc xương nhọn hoắt nối với đầu ngón bằng sợi cô-la-gen. Khi bị kẻ thù tóm lấy, nó gồng cơ chân giật đứt mối nối đó và đẩy thẳng xương trần sắc lẹm chọc rách lớp da thịt lao ra ngoài làm vuốt chiến đấu! Một nhà tự nhiên học từng bắt sống nó và bị cào rách tay chảy máu sâu hoắm! [surprise-wa] Chưa hết, đến mùa sinh sản, con đực còn mọc hàng trăm sợi lông da rậm rạp hai bên sườn dày chỉ không phẩy bốn mi-li-mét! Lý do cực kỳ cảm động: ông bố phải ngồi lì dưới nước canh trứng suốt nhiều tuần nên cần bộ lông mạch máu này để hút thêm oxy qua da thay cho lá phổi bé xíu! Một gã dị nhân vừa biết tự rách da rút vuốt xương, vừa mọc mang lông làm ông bố tận tụy, đúng là siêu anh hùng kỳ quặc nhất thế giới tự nhiên!
```

**Whisper prompt:** `Ếch Lông Wolverine, Dị Nhân Đầm Lầy, Trichobatrachus robustus, Ca-mơ-run, Cameroon, Đa-vít Blách-bơn, David Blackburn, Ha-vớt, Harvard, cô-la-gen, collagen, kê-ra-tin, keratin, Giê-rôn Đu-reo, Gerald Durrell, Ba-cốt-xi, Bakossi, EDGE, 13cm, 9cm, 0,02mm, 0,13mm, 0,35mm, 0,45mm, 63 loài, 11 loài, 3,5%, 1954, 2008`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| hai mươi mốt | 21 |
| mười ba xăng-ti-mét | 13cm |
| mười xăng-ti-mét | 10cm |
| chín xăng-ti-mét | 9cm |
| mười một xăng-ti-mét | 11cm |
| sáu mươi ba loài | 63 loài |
| mười một loài | 11 loài |
| một trăm phần trăm | 100% |
| bốn hạng mục | 4 hạng mục |
| tám ngón chân sau | 8 ngón chân sau |
| bốn ngón | 4 ngón |
| hai chân sau | 2 chân sau |
| hai năm | 2 năm |
| hai ngàn lẻ tám | 2008 |
| một ngàn chín trăm năm mươi tư | 1954 |
| một ngàn chín trăm hai mươi lăm | 1925 |
| không phẩy không hai mi-li-mét | 0,02mm |
| không phẩy mười ba mi-li-mét | 0,13mm |
| sáu lần | 6 lần |
| không phẩy ba mươi lăm | 0,35 |
| không phẩy bốn mươi lăm mi-li-mét | 0,45mm |
| không phẩy bốn mi-li-mét | 0,4mm |
| tháng tư | tháng 4 |
| tháng sáu | tháng 6 |
| ba hàng gai | 3 hàng gai |
| ba lưỡi nhọn | 3 lưỡi nhọn |
| ba phẩy năm phần trăm | 3,5% |
| một phần ba | 1/3 |
| sáu chiếc sừng | 6 chiếc sừng |
| hàng trăm | hàng trăm |
| Ca-mơ-run | Cameroon |
| Đa-vít Blách-bơn | David Blackburn |
| Ha-vớt | Harvard |
| Cô-la-gen | Collagen |
| cô-la-gen | collagen |
| Kê-ra-tin | Keratin |
| kê-ra-tin | keratin |
| Giê-rôn Đu-reo | Gerald Durrell |
| Ba-cốt-xi | Bakossi |
| Ma-ri-a-na | Mariana |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · CA CẤP CỨU TỰ BẺ XƯƠNG ĐÂM THỦNG DA · 77.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.3 (7.3s) | L01 | Đêm khuya tại phòng cấp cứu dã chiến giữa rừng mưa Trung Phi. Đèn còi hú vang, cả ê-kíp trực bật dậy đón một ca chấn thương kỳ lạ nhất lịch sử ngành |  | BÊN TRÁI-GIỮA là phòng cấp cứu dã chiến dựng bằng lều vải giữa rừng mưa Trung Phi ban đêm, đèn cứu thương đỏ trên nóc chớp sáng rực; BÊN PHẢI là ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế, vẻ mặt bất lực hài hước và cô trợ lý phòng khám hoạt hình mặc áo blouse xanh nhạt, kẹp tập hồ sơ bệnh án giật mình bật dậy khỏi bàn trực. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong |
| b02 | 00:07.3–00:10.9 (3.6s) | L02 | y. Bệnh nhân tự bước vào phòng khám với tám vết rách gọn lỏn dưới lòng bàn chân... |  | chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán lầm lì bước vào cửa phòng khám, hai bàn chân sau quấn băng trắng nhưng vẫn ló ra tám đầu vuốt xương nhọn hoắt xuyên qua lớp băng, |
| b03 | 00:10.9–00:13.9 (3.0s) | L03 | Không phải do thú dữ cắn. Không phải do dẫm phải gai rừng. |  | Hai bong bóng suy nghĩ gạch chéo đỏ ở GIỮA: BÊN TRÁI hình răng nanh báo đốm gạch chéo đỏ, BÊN PHẢI hình bụi gai rừng gạch chéo đỏ; phía dưới là dấu chấm hỏi to. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này. |
| b04 | 00:13.9–00:19.8 (5.9s) | L04 | Mà là do chính bệnh nhân tự gồng cơ... bẻ gãy mối nối xương ngón chân mình rồi đâm xuyên qua da thịt chui ra ngoài! |  | Cận cảnh bàn chân sau của chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán bên PHẢI: chú ếch tự gồng bắp chân nổi cuồn cuộn, làm chiếc xương ngón chân nhọn đâm xuyên qua da bàn c |
| b05 | 00:19.8–00:25.6 (5.8s) | L05 | Bác sĩ ơi, em băng bó xong rồi nhưng nhìn mặt bệnh nhân vẫn tỉnh bơ như không có chuyện gì luôn ạ! |  | BÊN TRÁI cô trợ lý phòng khám hoạt hình mặc áo blouse xanh nhạt, kẹp tập hồ sơ bệnh án giơ cuộn băng gạc trắng toát mồ hôi nhìn xuống; BÊN PHẢI chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bá |
| b06 | 00:25.6–00:31.9 (6.2s) | L06 | Các đồng nghiệp nhìn kỹ hồ sơ đi: bệnh nhân số 21 không phải gấu, không phải sói, mà là một con ếch! |  | BÊN TRÁI ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế, vẻ mặt bất lực hài hước cầm tập hồ sơ bệnh án chỉ tay sửng sốt; BÊN PHẢI là hình bóng gấu xám và sói xám bị gạch bỏ, thay bằng chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua |
| b07 | 00:31.9–00:38.4 (6.5s) | L07 | Đây là Ếch Lông Wolverine, tên khoa học cực kỳ hầm hố, sống ẩn dật dọc các dòng suối núi ở Cameroon và vùng Trung Phi. |  | Bản đồ lục địa châu Phi tô sáng vùng Trung Phi và Cameroon ở BÊN TRÁI; BÊN PHẢI là dòng suối đá rừng nhiệt đới nơi chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán đang ngồi trên |
| b08 | 00:38.4–00:42.7 (4.3s) | L08 | Con đực trưởng thành dài khoảng mười đến 13cm, to cỡ nắm tay người lớn. | **10-13 CM** · dài cỡ nắm tay · R/350 · [0.79, 0.45] | Ở GIỮA chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán đứng cạnh một nắm tay người lớn hoạt hình để so kích cỡ bằng nhau; BÊN PHẢI có chiếc thước đo chiều cao màu vàng dựng thẳn |
| b09 | 00:42.7–00:50.4 (7.7s) | L09 | Trông ngoài mặt thì lầm lì mũm mĩm như cục đất sét biết thở, nhưng trong phòng khám này, chúng tôi gọi thẳng nó bằng biệt danh: Dị Nhân Đầm Lầy! |  | Chia đôi khung: BÊN TRÁI một cục đất sét nâu nặn hình con ếch; BÊN PHẢI chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán khoanh tay ưỡn ngực đeo bảng tên bệnh nhân đầy ngạo nghễ  |
| b10 | 00:50.4–00:58.1 (7.7s) | L10 | Điều khiến tôi bất lực nhất ngay từ vòng tiếp nhận là quy luật ngược đời của loài này. Ở phần lớn thế giới ếch nhái, con cái lúc nào cũng to béo gấp rưỡi con đực để mang trứng. |  | BÊN TRÁI ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế, vẻ mặt bất lực hài hước ôm trán thở dài bất lực trước chiếc cân bập bênh bị đảo ngược hoàn toàn: đĩa bên trái đặt một cô ếch xanh bình thường to hơn, đĩa bên phải là chú ếch đực nhỏ xíu bị nhấc bổng lên. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này. |
| b11 | 00:58.1–01:04.7 (6.6s) | L11 | Riêng nhà Dị Nhân Đầm Lầy thì ngược hẳn: con cái chỉ dài 9cm, còn ông chồng lại phổng phao tới 13cm! | **9 CM** · ếch cái nhỏ hơn · L/380 · [0.32, 0.58]<br>**13 CM** · ếch đực to vượt trội · R/350 · [0.7, 0.48] | So sánh kích thước trên thước kẻ phòng khám: BÊN TRÁI một cô ếch cái trơn láng (không đeo gương bác sĩ) thấp hơn hẳn; BÊN PHẢI chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán ca |
| b12 | 01:04.7–01:11.3 (6.6s) | L12 | Chưa hết, mùa thường nó trơn láng như bao con ếch khác, nhưng cứ đến mùa chăm con, hai bên sườn nó tự mọc ra một bộ lông xù xì như râu quai |  | Chia đôi trước-sau: BÊN TRÁI chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán da trơn láng gọn gàng; mũi tên ở GIỮA chỉ sang BÊN PHẢI là chú Ếch Lông Wolverine (Trichobatrachus r |
| b13 | 01:11.3–01:17.9 (6.6s) | L13 | nón! Hôm nay, tôi mời các đồng nghiệp cùng soi đèn công suất lớn để khám nghiệm 4 hạng mục kỳ dị nhất trên cơ thể gã dị nhân tự hủy này! |  | ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế, vẻ mặt bất lực hài hước đứng giữa phòng khám bật chiếc đèn phẫu thuật khổng lồ chiếu thẳng xuống chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một ch |

### scene02 · CƠ CHẾ XƯƠNG TRẦN TỰ ĐÂM THỦNG DA LÀM VUỐT · 106.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.9 (7.9s) | L14 | Hạng mục khám đầu tiên: Chụp X-quang hai bàn chân sau! Nhìn bằng mắt thường, bàn chân của Dị Nhân Đầm Lầy tròn ủm, mềm mại và có màng bơi trông cực kỳ hiền lành vô hại. |  | Cận cảnh bàn chân sau tròn ủm, có màng bơi màu nâu ô-liu của chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán đặt trên tấm đệm khám bệnh trắng tinh, nhìn bên ngoài mềm mại cực kỳ |
| b02 | 00:07.9–00:12.8 (4.8s) | L15 | Nhưng khi đặt chân nó lên máy chụp cắt lớp, cả phòng khám suýt nữa làm rơi cả tách cà phê xuống sàn! |  | ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế, vẻ mặt bất lực hài hước cầm tách cà phê làm rơi văng tung tóe xuống sàn vì choáng váng khi nhìn lên bảng đèn soi X-quang ở GIỮA: phim X-quang chiếu xuyên bàn chân chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, |
| b03 | 00:12.8–00:16.4 (3.6s) | L16 | Ẩn sâu bên dưới lớp da thịt mịn màng kia là cả một kho dao bấm sinh học giấu |  | Mặt cắt giải phẫu bàn chân ếch màu hoạt hình sạch sẽ ở GIỮA: dưới lớp da mịn là một hàng dao bấm bỏ túi màu trắng xương xếp gọn gàng ẩn bên trong thịt. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này. |
| b04 | 00:16.4–00:22.2 (5.8s) | L17 | kín. Ở mèo, chó hay đại bàng, móng vuốt được làm từ chất sừng keratin mọc sẵn bên ngoài giống như móng tay của chúng ta. |  | So sánh chia đôi: BÊN TRÁI bàn chân mèo giơ móng vuốt sừng vàng mọc bên ngoài da; BÊN PHẢI chân đại bàng với móng vuốt sừng đen uốn cong. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này. |
| b05 | 00:22.2–00:27.9 (5.8s) | L18 | Còn vuốt của Dị Nhân Đầm Lầy thì không hề có lớp sừng bọc ngoài nào cả! Thứ chọc ra ngoài là xương trần 100%! | **100% XƯƠNG** · không có vỏ sừng · R/350 · [0.56, 0.5] | Cận cảnh ngón chân sau của chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán phóng to ở GIỮA: không có lớp vỏ sừng bọc ngoài, chỉ có đầu xương trắng muốt trơn nhẵn đâm thẳng ra kh |
| b06 | 00:27.9–00:37.5 (9.6s) | L19 | Cơ chế khai hỏa của nó hoạt động chẳng khác gì phim hành động viễn tưởng! Năm 2008, tiến sĩ David Blackburn tại Đại học Harvard đã soi kính hiển vi giải phẫu và giải mã bí ẩn này. | **2008** · nghiên cứu Harvard · L/360 · [0.58, 0.42] | Trong phòng thí nghiệm Đại học, nhà khoa học hoạt hình đeo kính lúp mắt to ngồi soi bàn chân ếch trên kính hiển vi với bảng vẽ sơ đồ xương phát sáng bên cạnh. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này. |
| b07 | 00:37.5–00:46.3 (8.8s) | L20 | Lúc bình thường, đầu xương nhọn hoắt hình móc câu nằm ngoan ngoãn dưới da, được neo chặt vào một cục xương nhỏ xíu ở đầu ngón nhờ dải mô liên kết giàu collagen. |  | Sơ đồ cắt lớp ngón chân ếch ở trạng thái nghỉ (ở GIỮA): đầu xương nhọn hình móc câu nằm yên trong thịt, nối vào một cục xương tròn nhỏ đầu ngón bằng dải dây chằng đàn hồi màu hồng. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này. |
| b08 | 00:46.3–00:50.6 (4.3s) | L21 | Nhờ chốt an toàn đó, nó đi lại chạy nhảy thoải mái mà không tự đâm vào chân mình! |  | chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán vui vẻ nhảy lò cò trên lá sen xanh và chạy tung tăng trên đá suối, hai bàn chân đóng kín an toàn như có khóa cài. |
| b09 | 00:50.6–00:54.3 (3.7s) | L22 | Nhưng chỉ cần một kẻ săn mồi vừa thò tay chạm vào lưng! Dị Nhân |  | Một con rắn hổ mang rừng hoặc cầy mangut thò đầu từ BÊN TRÁI chạm vào lưng chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán; chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạ |
| b10 | 00:54.3–00:57.0 (2.6s) | L23 | Đầm Lầy lập tức co cực mạnh bó cơ gập dưới bàn chân! |  | Cận cảnh bắp chân sau của chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán gồng lên nổi cơ bắp cuồn cuộn phát sáng cam, kéo căng sợi gân bên trong bàn chân như kéo cò súng. |
| b11 | 00:57.0–00:60.0 (3.0s) | L24 | Lực kéo giật đứt phăng mối nối collagen giữ chốt an toàn! |  | Sơ đồ phóng to đầu ngón chân ếch: dải dây nối màu hồng bị giật đứt làm đôi phựt ra khỏi cục xương tròn nhỏ, tạo tia lửa hiệu ứng comic. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này. |
| b12 | 00:60.0–01:04.2 (4.2s) | L25 | Đầu xương nhọn lập tức xoay gập xuống dưới và chọc thủng lớp đệm da thịt của 8 ngón chân sau! | **8 NGÓN** · phóng vuốt xương · R/380 · [0.52, 0.38] | Hai bàn chân sau của chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán đồng loạt bật ra tám chiếc vuốt xương trắng nhọn hoắt như móng vuốt hoạt hình màu trắng sáng (phong cách hoạ |
| b13 | 01:04.2–01:14.0 (9.8s) | L26 | Các bác sĩ đo được lớp vỏ xương ở gốc chỉ dày 0,02mm, nhưng càng ra tới mũi nhọn càng đặc cứng gấp hơn 6 lần, đạt 0,13mm, biến mũi xương thành một lưỡi dao găm thực thụ! | **0,02 MM** · vỏ xương ở gốc · L/350 · [0.34, 0.55]<br>**0,13 MM** · dày gấp 6 lần ở mũi · R/350 · [0.68, 0.48] | Sơ đồ so sánh độ dày lớp vỏ xương ở gốc và mũi vuốt bằng kính hiển vi có thước đo siêu nhỏ: phần gốc mảnh như tờ giấy, phần mũi dày đặc cứng cáp như đầu lưỡi dao găm. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này. |
| b14 | 01:14.0–01:22.8 (8.9s) | L27 | Nghe tới đây chắc các đồng nghiệp đều toát mồ hôi hột: thế lúc hết đánh nhau rồi, làm sao nó thu vuốt vào được? Chẳng lẽ đứng đó chịu trận với tám ngón chân lòi xương mãi sao? |  | ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế, vẻ mặt bất lực hài hước và cô trợ lý phòng khám hoạt hình mặc áo blouse xanh nhạt, kẹp tập hồ sơ bệnh án toát mồ hôi hột nhìn bàn chân có vuốt xương lòi ra ngoài, đặt dấu chấm hỏi to tướng phía trên. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này. |
| b15 | 01:22.8–01:29.7 (6.9s) | L28 | Câu trả lời còn làm bác sĩ chúng tôi ngơ ngác hơn: trên bàn chân nó hoàn toàn không có bất kỳ bó cơ nào dùng để kéo chiếc vuốt trở lại! |  | ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế, vẻ mặt bất lực hài hước dùng kính lúp soi khắp bàn chân ếch tìm sợi cơ kéo vuốt nhưng hoàn toàn trống trơn, khuôn mặt ngơ ngác tột độ. |
| b16 | 01:29.7–01:36.0 (6.3s) | L29 | Các nhà khoa học nhận định rằng khi cơn nguy hiểm qua đi và cơ chân thả lỏng, chiếc vuốt xương có lẽ tự trượt ngược vào trong một cách |  | Cơ chân sau của chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán thả lỏng dần dưới ánh đèn xanh dịu, chiếc vuốt xương tự trượt thụ động ngược lại vào trong lớp đệm ngón chân. |
| b17 | 01:36.0–01:42.3 (6.3s) | L30 | thụ động. Còn vết thương rách da kia thì nhờ khả năng hồi phục nhanh của loài lưỡng cư mà tự liền lại như chưa từng có chuyện gì xảy ra! |  | Cận cảnh bàn chân chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán tỏa ánh sáng hồi phục xanh lá nhẹ nhàng, vết rách da nhanh chóng khép miệng tự liền lại êm ái như mới. |
| b18 | 01:42.3–01:46.9 (4.6s) | L31 | Đúng là siêu anh hùng nhưng... mỗi lần rút vũ khí hơi tốn băng gạc một chút! |  | chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán tạo dáng siêu anh hùng oai phong nhưng hai bàn chân sau quấn đầy băng gạc cá nhân hình chữ thập, ngồi cạnh một thùng băng gạc y t |

### scene03 · BỘ LÔNG MẠCH MÁU GIÚP THỞ VÀ LÁ PHỔI TEO TÓP · 108.5s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:04.2 (4.2s) | L32 | Chuyển sang hạng mục khám thứ hai: Soi da liễu và kiểm tra hệ hô hấp! |  | ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế, vẻ mặt bất lực hài hước cầm kính lúp soi da bên sườn của chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của b |
| b02 | 00:04.2–00:16.4 (12.2s) | L33 | Thú thật với các đồng nghiệp, lúc mới đọc tên bệnh nhân là Ếch Lông, tôi cứ tưởng nó bị rụng tóc rơi vào người hoặc tiến hóa ngược mọc lông giống chuột. Nhưng khi đặt mẫu da dưới kính hiển vi, sự thật lại nằm ở một chân trời hoàn toàn khác! |  | Trong bong bóng suy nghĩ hài hước của ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế, vẻ mặt bất lực hài hước, chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc |
| b03 | 00:16.4–00:22.8 (6.4s) | L34 | Trời đất ơi, đi bơi giữa suối lạnh mà anh mặc nguyên cái áo lông rậm rạp thế kia không thấy vướng víu à? |  | BÊN TRÁI một chú ếch xanh bình thường (không đeo gương, da trơn) đang bơi giữa suối tròn mắt há hốc; BÊN PHẢI chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán bơi tung tăng với b |
| b04 | 00:22.8–00:30.3 (7.5s) | L35 | Chú ếch hàng xóm thắc mắc rất đúng trọng tâm, nhưng thực ra thứ mọc đầy hai bên sườn và đùi của Dị Nhân Đầm Lầy hoàn toàn không phải lông hay tóc gì cả! |  | chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán đứng khoanh tay giải thích cho chú ếch xanh hàng xóm, hai bên sườn phất phơ các sợi tua da mềm mại chứ không phải lông thú. |
| b05 | 00:30.3–00:38.7 (8.4s) | L36 | Đó là hàng trăm sợi nhú da mềm, đường kính mỗi sợi chỉ từ 0,35 đến 0,45mm — mỏng tương đương sợi cước mảnh. | **0,35-0,45** · đường kính sợi (mm) · R/350 · [0.62, 0.52] | Cận cảnh bộ lông tua rua ở sườn chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán đặt cạnh một sợi cước câu cá trong suốt có kính lúp phóng to ở GIỮA để thấy độ mảnh của sợi nhú d |
| b06 | 00:38.7–00:43.9 (5.2s) | L37 | Bên trong mỗi sợi nhú da ấy chạy chằng chịt những mạch máu mao mạch sát ngay lớp biểu bì ngoài cùng. |  | Mặt cắt phóng to một sợi nhú da màu hồng tươi: bên trong chứa đầy mạng lưới mao mạch đỏ li ti chạy sát ngay lớp da mỏng ngoài cùng. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này. |
| b07 | 00:43.9–00:50.4 (6.5s) | L38 | Và kỳ lạ nhất là chỉ có con đực mới mọc bộ lông kỳ dị này vào đúng mùa sinh sản, khoảng từ tháng 4 đến tháng 6 hàng năm! | **THÁNG 4-6** · mùa sinh sản mọc lông · R/350 · [0.74, 0.45] | So sánh đôi vợ chồng ếch dưới ánh nắng mùa hạ: BÊN TRÁI cô ếch cái da trơn nhẵn; BÊN PHẢI chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán con đực mọc đầy bộ râu lông hai bên sườ |
| b08 | 00:50.4–00:54.4 (4.0s) | L39 | Tại sao tạo hóa lại gắn hàng trăm sợi tua rua mạch máu lên hông một ông bố ếch? |  | Bác sĩ cổ điển với cặp kính gọng tròn đang soi bản vẽ giải phẫu cổ trên bàn gỗ đặt dấu chấm hỏi vào sườn chú ếch mọc tua lông. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này. |
| b09 | 00:54.4–00:59.4 (5.0s) | L40 | Câu trả lời được nhà động vật học Nô-bờ tìm ra từ năm 1925 khi mổ xẻ nội soi lá phổi của nó. | **1925** · phát hiện giải phẫu · L/350 · [0.35, 0.45] | Tài liệu khoa học cổ và phim soi nội soi hiển thị hai lá phổi nhỏ xíu, cấu tạo khác biệt rõ rệt giữa ếch đực và ếch cái. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này. |
| b10 | 00:59.4–01:05.8 (6.4s) | L41 | Hóa ra phổi của Dị Nhân Đầm Lầy con đực có cấu tạo vô cùng kỳ quặc và hạn chế so với nhu cầu năng lượng khổng lồ lúc nó vận động cơ bắp! |  | Phim X-quang đối chiếu ngực ếch: phổi của chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán con đực rất nhỏ và có túi cơ lạ, biểu tượng đồng hồ đo oxy báo thiếu hụt khi vận động m |
| b11 | 01:05.8–01:13.3 (7.5s) | L42 | Khi con cái đẻ trứng xong rồi lên bờ rừng lá khô đi chơi, ông bố ếch phải ở lại lặn ngụp dưới lòng suối đá chảy xiết để canh giữ bọc trứng suốt nhiều tuần liền! |  | Chia đôi cảnh suối rừng: BÊN TRÁI trên bờ lá khô cô ếch cái đeo kính râm tung tăng đi dạo; BÊN PHẢI dưới đáy suối đá nước chảy xiết là chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên |
| b12 | 01:13.3–01:20.5 (7.2s) | L43 | Ngồi lì dưới nước mà không được ngoi lên thở liên tục, lại phải gồng mình trông con, lượng oxy qua lá phổi tí hon hoàn toàn không đủ dùng! |  | chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán ngồi dưới đáy suối nước xanh, trên ngực hiện hình lá phổi tí hon đang thở hổn hển với thanh pin báo đỏ yếu ớt. |
| b13 | 01:20.5–01:29.4 (8.9s) | L44 | Thế là cơ thể nó tự kích hoạt bản nâng cấp sinh học: mọc tua tủa hàng trăm sợi nhú da giàu mạch máu ở sườn và đùi để tăng gấp bội diện tích tiếp xúc với nước! |  | Cận cảnh hai bên sườn chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán bùng nổ mọc ra hàng trăm sợi tua rua da màu hồng nâu, phát sáng như bật chế độ tăng lực sinh học. |
| b14 | 01:29.4–01:36.1 (6.7s) | L45 | Những sợi lông giả đó hoạt động chẳng khác nào một dàn mang cá tạm thời, hút oxy trực tiếp từ dòng suối xuyên qua da vào thẳng máu! |  | Những bong bóng oxy nhỏ màu xanh ngọc từ dòng nước suối đang thấm xuyên thẳng qua các sợi tua rua da của chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán vào mạch máu, giống hệt  |
| b15 | 01:36.1–01:43.4 (7.3s) | L46 | Chưa hết, lúc ẩn mình dưới đá suối, đám tua rua lất phất theo dòng nước còn trông y hệt đám rêu tảo, giúp ông bố ngụy trang che mắt kẻ săn mồi! |  | chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán nấp sát hòn đá dưới suối, bộ tua rua lất phất hòa lẫn hoàn toàn vào đám rêu tảo xanh rì; một con chim săn mồi đậu phía trên ngó x |
| b16 | 01:43.4–01:48.5 (5.1s) | L47 | Hết mùa giữ trứng, bộ lông tự động teo rụng sạch sẽ, trả lại vẻ bảnh bao gọn gàng! |  | Đàn nòng nọc nhỏ bơi tung tăng đi xa; chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán rụng hết tua lông bên sườn trở lại làn da trơn láng bảnh bao, mỉm cười vẫy tay chào con. |

### scene04 · SO SÁNH HỘI TỰ HỦY VÀ GAI BÁM SUỐI XIẾT · 101.0s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:10.3 (10.3s) | L48 | Hạng mục khám thứ ba: Kiểm tra hồ sơ gia phả dị nhân! Khi tiến sĩ David Blackburn kiểm tra mẫu vật của 63 loài ếch châu Phi trong bảo tàng, ông phát hiện không chỉ mình Dị Nhân Đầm Lầy biết chơi chiêu rút xương làm | **63 LOÀI** · khảo sát bảo tàng · L/350 · [0.32, 0.5] | ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế, vẻ mặt bất lực hài hước mở ngăn tủ hồ sơ bảo tàng chất đầy hàng chục lọ tiêu bản ếch châu Phi được đánh số gọn gàng để kiểm tra gia phả. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này. |
| b02 | 00:10.3–00:15.9 (5.6s) | L49 | vuốt! Tổng cộng có tới 11 loài thuộc ba chi họ hàng ở Trung Phi đều sở hữu bộ vũ khí giấu kín đáng sợ này! | **11 LOÀI** · có vuốt giấu kín · R/350 · [0.65, 0.52] | Bảng xếp đội hình 11 chú ếch châu Phi thuộc ba nhóm họ hàng đứng dàn hàng ngang, tất cả đều giấu chiếc vuốt xương nhỏ dưới chân sau. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này. |
| b03 | 00:15.9–00:22.5 (6.6s) | L50 | Nếu mở rộng hồ sơ sang các loài lưỡng cư khác trên thế giới, hội tự hủy còn có một thành viên cực gắt khác là loài kỳ giông gân sườn Tây Ban Nha: |  | Bản đồ châu Âu và tấm hồ sơ giải phẫu lưỡng cư tự vệ mở ra trên bàn bác sĩ, hình vẽ chú kỳ giông Tây Ban Nha đang chuẩn bị tư thế phòng thủ. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này. |
| b04 | 00:22.5–00:27.3 (4.7s) | L51 | khi bị tấn công, nó đẩy thẳng những đầu xương sườn nhọn hoắt xuyên qua lớp da hai bên hông kèm chất độc! |  | Một chú kỳ giông gân sườn Tây Ban Nha màu xám nâu đốm cam mặc áo choàng gai, gồng lưng đẩy các đầu gai xương sườn trắng nhọn chọc nhẹ qua hai bên hông đầy vẻ ngầu lòi (kiểu hoạt hình, không máu). KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này. |
| b05 | 00:27.3–00:37.2 (9.9s) | L52 | Tuy vậy, cơ chế bẻ đứt mối nối xương ở đầu ngón chân để phóng ra chiếc vuốt cong sắc bén như dao găm của ếch châu Phi vẫn là thiết kế độc nhất vô nhị trong toàn bộ giới động vật có xương sống! |  | Đặt cạnh nhau trên bệ trưng bày: chiếc vuốt xương cong như dao găm của chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán tỏa hào quang vàng đứng hạng nhất về độ độc lạ trong giới  |
| b06 | 00:37.2–00:49.4 (12.2s) | L53 | Chưa hết đâu các đồng nghiệp, hãy soi kỹ cả đôi bàn tay trước của ông bố Dị Nhân Đầm Lầy! Nếu chân sau giấu dao găm để chiến đấu, thì trên ngón cái bàn tay trước của con đực lại mọc lên 3 hàng gai sừng màu đen cứng như kìm sắt! | **3 HÀNG GAI** · ngón cái tay trước · R/350 · [0.56, 0.48] | Phóng to bàn tay trước của chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán: trên ngón cái mập mạp có ba hàng gai sừng màu đen cứng cáp xếp đều tăm tắp như gai lốp xe địa hình. |
| b07 | 00:49.4–00:57.0 (7.6s) | L54 | Bộ gai nhám này không dùng để đánh nhau, mà để khóa chặt vào thân bạn đời hoặc bám vững vào tảng đá trơn trượt giữa dòng suối chảy xiết trong mùa mưa! |  | chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán dùng hai bàn tay trước có gai nhám ôm ghì chặt lấy một tảng đá trơn nhẵn giữa dòng thác nước chảy xiết trắng xóa mà không bị cuốn |
| b08 | 00:57.0–01:06.5 (9.5s) | L55 | Nhưng đừng thấy nó nhỏ bé mà chủ quan đưa tay ra nựng! Năm 1954, nhà tự nhiên học nổi tiếng người Anh Gerald Durrell từng thuật lại cú sốc nhớ đời trong cuốn sách của ông. | **1954** · sách Gerald Durrell · L/350 · [0.3, 0.45] | Nhà tự nhiên học mặc đồ thám hiểm kaki đội mũ cối ở BÊN TRÁI cầm cuốn sổ da, rón rén đưa tay về phía chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán đang ngồi giả vờ ngây thơ ở  |
| b09 | 01:06.5–01:16.0 (9.5s) | L56 | Khi ông dùng tay không bắt sống một chú Dị Nhân Đầm Lầy hoang dã, nó lập tức đạp mạnh 2 chân sau, phóng vuốt xương cào thẳng vào lòng bàn tay ông những vết rách sâu hoắm chảy máu đầm đìa! |  | chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán đạp tung hai chân sau giơ vuốt xương lên; nhà thám hiểm giật bắn người rụt tay lại với vài vệt băng đỏ dán ngang lòng bàn tay và  |
| b10 | 01:16.0–01:21.3 (5.3s) | L57 | Đúng là nhìn mặt hiền khô tưởng cục đất biết nhảy, ai ngờ chạm vào là mất ngay miếng thịt tay! |  | Chia đôi: BÊN TRÁI chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán cười hiền lành giả vờ như cục đất dễ thương; BÊN PHẢI hiện nguyên hình giơ hai chân đầy vuốt xương sắc bén khi |
| b11 | 01:21.3–01:25.6 (4.3s) | L58 | Bác sĩ ơi, thế mấy con nòng nọc mới nở ra đã có vuốt xương đâm rách tay chưa ạ? |  | Một chú nòng nọc hoạt hình tròn trĩnh màu nâu nhạt bơi trong cốc thủy tinh tròn, tò mò giơ cái đuôi lên hỏi ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế, vẻ mặt bất lực hài hước đứng bên cạnh. |
| b12 | 01:25.6–01:37.7 (12.0s) | L59 | Câu hỏi rất hay! Nòng nọc bé xíu sống dưới nước thì chưa mọc vuốt đâu cháu ạ, nhưng ở những loài họ hàng gần cùng nhóm, ngay cả những chú ếch con mới bước lên bờ cũng đã trang bị sẵn bộ vuốt xương giấu kín dưới chân để phòng thân rồi! |  | Chia đôi: BÊN TRÁI chú nòng nọc nhỏ xíu trơn tru chưa có chân tay bơi trong nước; BÊN PHẢI một chú ếch con bé bằng đồng xu vừa bước lên bờ đã giấu sẵn chiếc vuốt xương tí hon dưới bàn chân. |
| b13 | 01:37.7–01:41.0 (3.4s) | L60 | Tuổi nhỏ tài cao, vừa ra đời đã mang theo vũ khí hạng nặng! |  | Chú ếch con tý hon đội mũ bảo hiểm nhỏ xíu đứng oai vệ cạnh mô hình chiếc vuốt xương phóng to bằng kính lúp đầy tự hào. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này. |

### scene05 · THỢ SĂN PHẢI DÙNG GIÁO BA MŨI TRÁNH VUỐT · 81.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:10.7 (10.7s) | L61 | Hạng mục khám thứ tư: Khảo sát hiện trường thực địa tại rừng núi Cameroon! Trong khi giới khoa học phương Tây đến tận năm 2008 mới giải mã hoàn toàn cơ chế vuốt xương của Dị Nhân Đầm Lầy, |  | Rừng núi Cameroon ban đêm ánh trăng xanh: ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế, vẻ mặt bất lực hài hước đeo đèn pin trên trán cùng người dân bản địa châu Phi chỉ tay về phía dòng suối đá có chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sư |
| b02 | 00:10.7–00:15.9 (5.2s) | L62 | thì người dân bản địa vùng Trung Phi đã... biết thừa độ nguy hiểm của nó từ hàng trăm năm trước rồi! |  | Người thợ săn bản địa châu Phi kinh nghiệm lắc đầu chỉ biển cảnh báo vào chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán đang ngồi trên đá suối, trên đầu có đồng hồ cát quay ngư |
| b03 | 00:15.9–00:20.4 (4.5s) | L63 | Tại nhiều làng ở Cameroon, thịt ếch lông nướng là một món ăn truyền thống rất được ưa chuộng. |  | Quầy bếp lửa trại ngoài trời ở làng quê châu Phi với khói tỏa nghi ngút và xiên đồ nướng thơm lừng đặt trên đĩa gỗ; không vẽ cảnh giết mổ. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này. |
| b04 | 00:20.4–00:30.5 (10.1s) | L64 | Nhưng có một quy tắc bất thành văn khi đi săn ban đêm: tuyệt đối không bao giờ thò tay không chộp lấy con ếch! Nếu lỡ tay túm nhầm, tám chiếc vuốt xương ở 2 chân sau sẽ đạp phăng vào cổ tay gây chảy máu rất đau đớn! |  | Biển cảnh báo hoạt hình màu vàng hình bàn tay bị gạch chéo đỏ to đùng phía trên đầu chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán đang giơ chân sau khoe tám chiếc vuốt xương. |
| b05 | 00:30.5–00:35.7 (5.2s) | L65 | Vậy nên các thợ săn phải vác theo dao rựa hoặc chế tạo riêng những cây giáo cán dài để giữ khoảng cách an toàn! |  | Hai người thợ săn hoạt hình châu Phi đứng từ xa giơ những cây sào giáo dài bằng gỗ để giữ khoảng cách an toàn với chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán ngồi trên tảng  |
| b06 | 00:35.7–00:45.7 (10.0s) | L66 | Và đây là cú trớ trêu lịch sử khiến cả phòng khám phải bật cười: nhiều cây giáo chuyên dụng dùng để săn loài ếch Wolverine này được rèn với phần đầu có đúng 3 lưỡi nhọn chĩa ra phía trước | **3 LƯỠI** · giáo săn giống vuốt · R/350 · [0.56, 0.46] | Cận cảnh đầu cây giáo sắt dùng săn ếch ở GIỮA: có đúng ba lưỡi nhọn song song chĩa thẳng ra ngoài cực bén, ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế, vẻ mặt bất lực hài hước đứng cạnh bật cười chỉ vào. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này. |
| b07 | 00:45.7–00:51.3 (5.7s) | L67 | — trông chẳng khác nào bộ vuốt ba ngạnh bằng kim loại của nhân vật Người Sói Wolverine ngoài đời thực! |  | Đặt cạnh nhau để đối chiếu: BÊN TRÁI là đầu giáo sắt ba lưỡi; BÊN PHẢI là bàn tay vuốt ba ngạnh kim loại kiểu siêu anh hùng Người Sói lóe sáng hài hước. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này. |
| b08 | 00:51.3–00:55.9 (4.6s) | L68 | Muốn săn Người Sói đầm lầy, thợ săn buộc phải tự chế vũ khí Người Sói để đối đầu! |  | So sánh đối xứng hài hước: BÊN TRÁI người thợ săn cầm cây giáo ba mũi; BÊN PHẢI chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán giơ ba ngón chân có vuốt xương chĩa thẳng về phía |
| b09 | 00:55.9–01:07.5 (11.6s) | L69 | Thậm chí người dân tộc Bakossi ở Cameroon xưa kia còn lưu truyền một huyền thoại cực kỳ thú vị: họ tin rằng những con ếch mọc lông kỳ quái này không sinh ra từ dưới bùn, mà... rơi thẳng từ trên bầu trời xuống cùng những cơn mưa rào! |  | Minh họa truyền thuyết cổ tích hài hước: trên bầu trời đêm đầy sao và mây trắng, những chú chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán bung dù nhỏ bé rơi lả tả từ trên trời  |
| b10 | 01:07.5–01:10.7 (3.2s) | L70 | Nhiều cặp vợ chồng hiếm muộn còn tin ăn món ếch này sẽ giúp sinh con thuận lợi. |  | Cảnh gia đình dân làng vui vẻ ngồi quây quần quanh mâm cơm ấm áp, bên trên là dấu gạch chéo khoa học nhẹ nhàng giải thích đây chỉ là niềm tin dân gian. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này. |
| b11 | 01:10.7–01:21.4 (10.6s) | L71 | Đến nay, khoa học đã xác nhận nó chẳng hề rơi từ vũ trụ nào cả, mà chỉ là một kỳ quan tiến hóa bản địa chính hiệu — thậm chí còn được xếp vào nhóm 3,5% loài lưỡng cư có độ độc đáo di truyền cao nhất hành tinh! | **TOP 3,5%** · độc đáo nhất hành tinh · R/350 · [0.52, 0.42] | Sơ đồ cây tiến hóa rực rỡ ở GIỮA: chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán đứng trên bục vinh quang top đầu giữa hàng trăm loài ếch nhái khác, đội chiếc cúp độc đáo di tr |

### scene06 · ĐƠN THUỐC BẤT LỰC VÀ BÓNG ĐEN BÍ ẨN TẬP SAU · 85.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.0 (7.0s) | L72 | Tổng kết hồ sơ bệnh án số 21. Thực lòng mà nói, tôi vẫn còn rùng mình mỗi khi nhìn lại tấm phim X-quang bàn chân của Dị Nhân Đầm Lầy. |  | ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế, vẻ mặt bất lực hài hước đứng cạnh bảng đèn X-quang bàn chân ếch, nhìn chăm chú với ánh mắt cảm phục, tay cầm bút ghi chú vào bệnh án số 21. |
| b02 | 00:07.0–00:18.3 (11.2s) | L73 | Để sinh tồn giữa rừng mưa khắc nghiệt đầy rẫy rắn rết và chim săn mồi, chú ếch nhỏ bé dài chỉ 13cm này chấp nhận tự làm đau chính mình, bẻ mối nối xương đâm rách da thịt chỉ trong tích tắc để đổi lấy cơ hội sống sót! | **13 CM** · nhỏ bé nhưng gan lì · L/370 · [0.48, 0.6] | chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán đứng vững giữa vòng vây của một con rắn rừng và bóng chim săn mồi từ trên cao, hai chân sau sẵn sàng bung vuốt xương tự vệ dũng c |
| b03 | 00:18.3–00:23.9 (5.6s) | L82 | Và ẩn sau vẻ ngoài lầm lì cùng biệt danh quái vật kinh dị, đó lại là một ông bố mẫu mực đến mức đáng |  | Chia đôi: BÊN TRÁI một cái bóng đen oai vệ có sáu gai nhỏ; BÊN PHẢI là chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán cười hiền hậu đeo tạp dề người cha mẫu mực. |
| b04 | 00:23.9–00:31.0 (7.1s) | L74 | nể: sẵn sàng mọc cả bộ lông mạch máu kỳ dị để ngồi lặng lẽ dưới dòng suối lạnh buốt suốt nhiều tuần liền, bảo vệ từng quả trứng nhỏ bé cho thế hệ tương lai. |  | Cảnh ấm áp dưới lòng suối xanh trong: chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán với bộ tua lông sườn dịu dàng ôm che bọc trứng tròn phát sáng vàng ấm áp để bảo vệ đàn con. |
| b05 | 00:31.0–00:42.0 (11.0s) | L75 | Kê đơn cuối cùng: cho bệnh nhân xuất viện ngay lập tức, tặng thêm một cuộn băng cá nhân dự phòng và khuyến cáo người xem... đừng bao giờ thử bắt chước! Ký tên: bác sĩ đã hoàn toàn bất lực! |  | ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế, vẻ mặt bất lực hài hước đóng dấu đỏ lên tờ giấy xuất viện, trao cho chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn mà |
| b06 | 00:42.0–00:49.9 (8.0s) | L76 | Còn các đồng nghiệp thì sao? Nếu bắt buộc phải chọn một trong hai trang bị của Dị Nhân Đầm Lầy: sở hữu vuốt xương giấu kín nhưng mỗi lần rút hơi rát tay, |  | Hai lựa chọn đặt trên hai bàn cân: BÊN TRÁI biểu tượng vuốt xương trắng kèm cuộn băng gạc; BÊN PHẢI biểu tượng bộ lông sườn cùng bình oxy lặn biển, dấu hỏi chấm ở giữa. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này. |
| b07 | 00:49.9–00:56.6 (6.7s) | L77 | hay mọc lông kín sườn để lặn thở dưới nước không cần bình oxy, bạn chọn cái nào? Hãy bình luận lựa chọn của bạn bên dưới nhé! |  | Các bạn nhỏ hoạt hình hào hứng ngồi giơ hai tấm thẻ biểu tượng: một thẻ vẽ hình chiếc vuốt xương, một thẻ vẽ hình ống thở oxy dưới nước (không có chữ). KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này. |
| b08 | 00:56.6–01:04.7 (8.1s) | L78 | Hồ sơ phòng khám hôm nay xin tạm đóng. Nhưng tập sau, chúng ta sẽ chuyển thẳng sang phòng thí nghiệm năm cấp độ để đối mặt với một ca tiến hóa còn điên rồ hơn nữa! |  | ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế, vẻ mặt bất lực hài hước đóng quyển sổ bệnh án dày cộp trên bàn, ánh sáng đèn phòng khám chuyển sang ánh sáng neon xanh của phòng thí nghiệm năm cấp độ với nhiều ống nghiệm sủi bọt. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này. |
| b09 | 01:04.7–01:11.2 (6.4s) | L79 | Một sinh vật nhỏ xíu sống dưới nước với khuôn mặt lúc nào cũng mỉm cười, trên đầu mọc 6 chiếc sừng lông xù như ăng-ten ngoài hành tinh... |  | Một sinh vật bí ẩn được vẽ hoàn toàn bằng BÓNG ĐEN ĐẶC TUYỀN (solid black silhouette) bên trong bể nước phòng thí nghiệm: hình dáng một sinh vật lưỡng cư nhỏ có sáu chiếc tua sừng xù ba nhánh hai bên đầu và chiếc đuôi dài, kèm dấu hỏi chấm vàng lớn phát sáng phía trên; KHÔNG vẽ rõ mắt mũi hay màu da thật. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này. |
| b10 | 01:11.2–01:20.5 (9.4s) | L80 | Điều khiến các nhà khoa học mất ngủ là dù có bị mất chân, đứt tủy sống, thậm chí mất cả 1/3 trái tim và một phần não bộ, nó vẫn tự mọc lại nguyên vẹn hoàn toàn mà không để lại lấy một vết sẹo | **1/3 TIM** · tái sinh không sẹo · L/350 · [0.35, 0.32] | Cũng chiếc BÓNG ĐEN ĐẶC TUYỀN (solid black silhouette) của sinh vật có sáu sừng lông xù và đuôi dài đó đứng ở GIỮA, xung quanh tỏa hào quang tái sinh màu xanh lá với biểu tượng trái tim ghép liền và tia sét hồi phục không tì vết. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này. |
| b11 | 01:20.5–01:25.4 (4.9s) | L81 | nào! Đố các bạn biết bóng đen bí ẩn kỳ sau là loài vật nào? Hãy đoán ngay ở phần bình luận nhé! |  | Chiếc BÓNG ĐEN ĐẶC TUYỀN bí ẩn có sáu sừng lông xù đứng giữa khung kính hiển vi và ba dấu hỏi chấm lớn lấp lánh vàng cam mời gọi khán giả đoán tên. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này. |

## 5. Phân cảnh Shorts — từng beat

Banner: **TỰ BẺ XƯƠNG ĐÂM / THỦNG DA LÀM VUỐT?!** · giọng 53.0s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Bệnh nhân này vào phòng cấp cứu không phải vì bị thú dữ cắn, |  |
| s02 | 00:03.4 | S02 | mà vì nó vừa... tự bẻ gãy xương ngón chân mình đâm thủng qua da! |  |
| s03 | 00:07.5 | S03 | Xin giới thiệu Ếch Lông Wolverine, gã dị nhân dài 13cm sống dọc các dòng suối núi ở Trung Phi. | **13 CM** · dị nhân suối Trung Phi · R/580 · [0.62, 0.55] |
| s04 | 00:13.3 | S04 | Dưới lớp da 8 ngón chân sau của nó giấu sẵn những chiếc móc xương nhọn hoắt nối với đầu ngón bằng sợi collagen. | **8 NGÓN** · giấu dao bấm xương · L/560 · [0.5, 0.55] |
| s05 | 00:19.1 | S05 | Khi bị kẻ thù tóm lấy, nó gồng cơ chân giật đứt mối nối |  |
| s06 | 00:22.4 | S06 | đó và đẩy thẳng xương trần sắc lẹm chọc rách lớp da thịt lao ra ngoài làm vuốt chiến |  |
| s07 | 00:26.3 | S07 | đấu! Một nhà tự nhiên học từng bắt sống nó và bị cào rách tay chảy máu sâu hoắm! |  |
| s08 | 00:31.2 | S08 | Chưa hết, đến mùa sinh sản, con đực còn mọc hàng trăm sợi lông da rậm rạp hai bên sườn dày chỉ 0,4mm! | **0,4 MM** · sợi nhú da mạch máu · R/580 · [0.55, 0.55] |
| s09 | 00:37.0 | S09 | Lý do cực kỳ cảm động: ông bố phải ngồi lì dưới nước canh trứng suốt nhiều tuần nên cần bộ lông mạch |  |
| s10 | 00:42.6 | S10 | máu này để hút thêm oxy qua da thay cho lá phổi bé xíu! |  |
| s11 | 00:45.2 | S11 | Một gã dị nhân vừa biết tự rách da rút vuốt xương, vừa mọc mang lông làm ông bố tận tụy, |  |
| s12 | 00:50.1 | S12 | đúng là siêu anh hùng kỳ quặc nhất thế giới tự nhiên! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đêm khuya tại phòng cấp cứu dã chiến giữa rừng mưa Trung Phi. Đèn còi hú vang, cả ê-kíp trực bật dậy đón một ca chấn thương kỳ lạ nhất lịch sử ngành y.". Bố cục: BÊN TRÁI-GIỮA là phòng cấp cứu dã chiến dựng bằng lều vải giữa rừng mưa Trung Phi ban đêm, đèn cứu thương đỏ trên nóc chớp sáng rực; BÊN PHẢI là ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế, vẻ mặt bất lực hài hước và cô trợ lý phòng khám hoạt hình mặc áo blouse xanh nhạt, kẹp tập hồ sơ bệnh án giật mình bật dậy khỏi bàn trực. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bệnh nhân tự bước vào phòng khám với tám vết rách gọn lỏn dưới lòng bàn chân...". Bố cục: chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán lầm lì bước vào cửa phòng khám, hai bàn chân sau quấn băng trắng nhưng vẫn ló ra tám đầu vuốt xương nhọn hoắt xuyên qua lớp băng, mặt lạnh tanh không cảm xúc.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không phải do thú dữ cắn. Không phải do dẫm phải gai rừng.". Bố cục: Hai bong bóng suy nghĩ gạch chéo đỏ ở GIỮA: BÊN TRÁI hình răng nanh báo đốm gạch chéo đỏ, BÊN PHẢI hình bụi gai rừng gạch chéo đỏ; phía dưới là dấu chấm hỏi to. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mà là do chính bệnh nhân tự gồng cơ... bẻ gãy mối nối xương ngón chân mình rồi đâm xuyên qua da thịt chui ra ngoài!". Bố cục: Cận cảnh bàn chân sau của chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán bên PHẢI: chú ếch tự gồng bắp chân nổi cuồn cuộn, làm chiếc xương ngón chân nhọn đâm xuyên qua da bàn chân thò ra ngoài như lưỡi dao găm.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bác sĩ ơi, em băng bó xong rồi nhưng nhìn mặt bệnh nhân vẫn tỉnh bơ như không có chuyện gì luôn ạ!". Bố cục: BÊN TRÁI cô trợ lý phòng khám hoạt hình mặc áo blouse xanh nhạt, kẹp tập hồ sơ bệnh án giơ cuộn băng gạc trắng toát mồ hôi nhìn xuống; BÊN PHẢI chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán ngồi ngay ngắn trên giường khám, vết thương đã quấn băng nhưng mặt tỉnh bơ ngơ ngác nhìn thẳng.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các đồng nghiệp nhìn kỹ hồ sơ đi: bệnh nhân số 21 không phải gấu, không phải sói, mà là một con ếch!". Bố cục: BÊN TRÁI ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế, vẻ mặt bất lực hài hước cầm tập hồ sơ bệnh án chỉ tay sửng sốt; BÊN PHẢI là hình bóng gấu xám và sói xám bị gạch bỏ, thay bằng chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán ngồi gọn lỏn trên chiếc cân khám bệnh.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đây là Ếch Lông Wolverine, tên khoa học cực kỳ hầm hố, sống ẩn dật dọc các dòng suối núi ở Cameroon và vùng Trung Phi.". Bố cục: Bản đồ lục địa châu Phi tô sáng vùng Trung Phi và Cameroon ở BÊN TRÁI; BÊN PHẢI là dòng suối đá rừng nhiệt đới nơi chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán đang ngồi trên tảng đá rêu đầy tự hào.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Con đực trưởng thành dài khoảng mười đến 13cm, to cỡ nắm tay người lớn.". Bố cục: Ở GIỮA chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán đứng cạnh một nắm tay người lớn hoạt hình để so kích cỡ bằng nhau; BÊN PHẢI có chiếc thước đo chiều cao màu vàng dựng thẳng cạnh chú ếch.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trông ngoài mặt thì lầm lì mũm mĩm như cục đất sét biết thở, nhưng trong phòng khám này, chúng tôi gọi thẳng nó bằng biệt danh: Dị Nhân Đầm Lầy!". Bố cục: Chia đôi khung: BÊN TRÁI một cục đất sét nâu nặn hình con ếch; BÊN PHẢI chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán khoanh tay ưỡn ngực đeo bảng tên bệnh nhân đầy ngạo nghễ giữa phòng khám.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Điều khiến tôi bất lực nhất ngay từ vòng tiếp nhận là quy luật ngược đời của loài này. Ở phần lớn thế giới ếch nhái, con cái lúc nào cũng to béo gấp rưỡi con đực để mang trứng.". Bố cục: BÊN TRÁI ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế, vẻ mặt bất lực hài hước ôm trán thở dài bất lực trước chiếc cân bập bênh bị đảo ngược hoàn toàn: đĩa bên trái đặt một cô ếch xanh bình thường to hơn, đĩa bên phải là chú ếch đực nhỏ xíu bị nhấc bổng lên. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Riêng nhà Dị Nhân Đầm Lầy thì ngược hẳn: con cái chỉ dài 9cm, còn ông chồng lại phổng phao tới 13cm!". Bố cục: So sánh kích thước trên thước kẻ phòng khám: BÊN TRÁI một cô ếch cái trơn láng (không đeo gương bác sĩ) thấp hơn hẳn; BÊN PHẢI chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán cao to vạm vỡ gấp rưỡi, ưỡn ngực tự hào.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa hết, mùa thường nó trơn láng như bao con ếch khác, nhưng cứ đến mùa chăm con, hai bên sườn nó tự mọc ra một bộ lông xù xì như râu quai nón!". Bố cục: Chia đôi trước-sau: BÊN TRÁI chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán da trơn láng gọn gàng; mũi tên ở GIỮA chỉ sang BÊN PHẢI là chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán mọc tua tủa bộ lông xù xì hai bên sườn như bộ râu quai nón hài hước.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hôm nay, tôi mời các đồng nghiệp cùng soi đèn công suất lớn để khám nghiệm 4 hạng mục kỳ dị nhất trên cơ thể gã dị nhân tự hủy này!". Bố cục: ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế, vẻ mặt bất lực hài hước đứng giữa phòng khám bật chiếc đèn phẫu thuật khổng lồ chiếu thẳng xuống chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán ngồi trên ghế bệnh nhân, xung quanh bày sẵn phim X-quang và kính hiển vi.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hạng mục khám đầu tiên: Chụp X-quang hai bàn chân sau! Nhìn bằng mắt thường, bàn chân của Dị Nhân Đầm Lầy tròn ủm, mềm mại và có màng bơi trông cực kỳ hiền lành vô hại.". Bố cục: Cận cảnh bàn chân sau tròn ủm, có màng bơi màu nâu ô-liu của chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán đặt trên tấm đệm khám bệnh trắng tinh, nhìn bên ngoài mềm mại cực kỳ hiền lành vô hại.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng khi đặt chân nó lên máy chụp cắt lớp, cả phòng khám suýt nữa làm rơi cả tách cà phê xuống sàn!". Bố cục: ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế, vẻ mặt bất lực hài hước cầm tách cà phê làm rơi văng tung tóe xuống sàn vì choáng váng khi nhìn lên bảng đèn soi X-quang ở GIỮA: phim X-quang chiếu xuyên bàn chân chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán hiện rõ những chiếc xương ngón chân nhọn hoắt như lưỡi dao bấm.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ẩn sâu bên dưới lớp da thịt mịn màng kia là cả một kho dao bấm sinh học giấu kín.". Bố cục: Mặt cắt giải phẫu bàn chân ếch màu hoạt hình sạch sẽ ở GIỮA: dưới lớp da mịn là một hàng dao bấm bỏ túi màu trắng xương xếp gọn gàng ẩn bên trong thịt. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ở mèo, chó hay đại bàng, móng vuốt được làm từ chất sừng keratin mọc sẵn bên ngoài giống như móng tay của chúng ta.". Bố cục: So sánh chia đôi: BÊN TRÁI bàn chân mèo giơ móng vuốt sừng vàng mọc bên ngoài da; BÊN PHẢI chân đại bàng với móng vuốt sừng đen uốn cong. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn vuốt của Dị Nhân Đầm Lầy thì không hề có lớp sừng bọc ngoài nào cả! Thứ chọc ra ngoài là xương trần 100%!". Bố cục: Cận cảnh ngón chân sau của chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán phóng to ở GIỮA: không có lớp vỏ sừng bọc ngoài, chỉ có đầu xương trắng muốt trơn nhẵn đâm thẳng ra khỏi da.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cơ chế khai hỏa của nó hoạt động chẳng khác gì phim hành động viễn tưởng! Năm 2008, tiến sĩ David Blackburn tại Đại học Harvard đã soi kính hiển vi giải phẫu và giải mã bí ẩn này.". Bố cục: Trong phòng thí nghiệm Đại học, nhà khoa học hoạt hình đeo kính lúp mắt to ngồi soi bàn chân ếch trên kính hiển vi với bảng vẽ sơ đồ xương phát sáng bên cạnh. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lúc bình thường, đầu xương nhọn hoắt hình móc câu nằm ngoan ngoãn dưới da, được neo chặt vào một cục xương nhỏ xíu ở đầu ngón nhờ dải mô liên kết giàu collagen.". Bố cục: Sơ đồ cắt lớp ngón chân ếch ở trạng thái nghỉ (ở GIỮA): đầu xương nhọn hình móc câu nằm yên trong thịt, nối vào một cục xương tròn nhỏ đầu ngón bằng dải dây chằng đàn hồi màu hồng. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhờ chốt an toàn đó, nó đi lại chạy nhảy thoải mái mà không tự đâm vào chân mình!". Bố cục: chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán vui vẻ nhảy lò cò trên lá sen xanh và chạy tung tăng trên đá suối, hai bàn chân đóng kín an toàn như có khóa cài.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng chỉ cần một kẻ săn mồi vừa thò tay chạm vào lưng! Dị Nhân Đầm Lầy". Bố cục: Một con rắn hổ mang rừng hoặc cầy mangut thò đầu từ BÊN TRÁI chạm vào lưng chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán; chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán ở BÊN PHẢI lập tức quay ngoắt đầu lại, mắt vàng rực lửa giận dữ.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "lập tức co cực mạnh bó cơ gập dưới bàn chân!". Bố cục: Cận cảnh bắp chân sau của chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán gồng lên nổi cơ bắp cuồn cuộn phát sáng cam, kéo căng sợi gân bên trong bàn chân như kéo cò súng.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lực kéo giật đứt phăng mối nối collagen giữ chốt an toàn!". Bố cục: Sơ đồ phóng to đầu ngón chân ếch: dải dây nối màu hồng bị giật đứt làm đôi phựt ra khỏi cục xương tròn nhỏ, tạo tia lửa hiệu ứng comic. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đầu xương nhọn lập tức xoay gập xuống dưới và chọc thủng lớp đệm da thịt của 8 ngón chân sau!". Bố cục: Hai bàn chân sau của chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán đồng loạt bật ra tám chiếc vuốt xương trắng nhọn hoắt như móng vuốt hoạt hình màu trắng sáng (phong cách hoạt hình hài thân thiện trẻ em, không máu), tư thế chiến đấu cực ngầu.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các bác sĩ đo được lớp vỏ xương ở gốc chỉ dày 0,02mm, nhưng càng ra tới mũi nhọn càng đặc cứng gấp hơn 6 lần, đạt 0,13mm, biến mũi xương thành một lưỡi dao găm thực thụ!". Bố cục: Sơ đồ so sánh độ dày lớp vỏ xương ở gốc và mũi vuốt bằng kính hiển vi có thước đo siêu nhỏ: phần gốc mảnh như tờ giấy, phần mũi dày đặc cứng cáp như đầu lưỡi dao găm. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nghe tới đây chắc các đồng nghiệp đều toát mồ hôi hột: thế lúc hết đánh nhau rồi, làm sao nó thu vuốt vào được? Chẳng lẽ đứng đó chịu trận với tám ngón chân lòi xương mãi sao?". Bố cục: ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế, vẻ mặt bất lực hài hước và cô trợ lý phòng khám hoạt hình mặc áo blouse xanh nhạt, kẹp tập hồ sơ bệnh án toát mồ hôi hột nhìn bàn chân có vuốt xương lòi ra ngoài, đặt dấu chấm hỏi to tướng phía trên. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Câu trả lời còn làm bác sĩ chúng tôi ngơ ngác hơn: trên bàn chân nó hoàn toàn không có bất kỳ bó cơ nào dùng để kéo chiếc vuốt trở lại!". Bố cục: ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế, vẻ mặt bất lực hài hước dùng kính lúp soi khắp bàn chân ếch tìm sợi cơ kéo vuốt nhưng hoàn toàn trống trơn, khuôn mặt ngơ ngác tột độ.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà khoa học nhận định rằng khi cơn nguy hiểm qua đi và cơ chân thả lỏng, chiếc vuốt xương có lẽ tự trượt ngược vào trong một cách thụ động.". Bố cục: Cơ chân sau của chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán thả lỏng dần dưới ánh đèn xanh dịu, chiếc vuốt xương tự trượt thụ động ngược lại vào trong lớp đệm ngón chân.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn vết thương rách da kia thì nhờ khả năng hồi phục nhanh của loài lưỡng cư mà tự liền lại như chưa từng có chuyện gì xảy ra!". Bố cục: Cận cảnh bàn chân chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán tỏa ánh sáng hồi phục xanh lá nhẹ nhàng, vết rách da nhanh chóng khép miệng tự liền lại êm ái như mới.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đúng là siêu anh hùng nhưng... mỗi lần rút vũ khí hơi tốn băng gạc một chút!". Bố cục: chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán tạo dáng siêu anh hùng oai phong nhưng hai bàn chân sau quấn đầy băng gạc cá nhân hình chữ thập, ngồi cạnh một thùng băng gạc y tế rỗng.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chuyển sang hạng mục khám thứ hai: Soi da liễu và kiểm tra hệ hô hấp!". Bố cục: ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế, vẻ mặt bất lực hài hước cầm kính lúp soi da bên sườn của chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán, ghi chép hồ sơ da liễu và kiểm tra hệ hô hấp trong phòng khám.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thú thật với các đồng nghiệp, lúc mới đọc tên bệnh nhân là Ếch Lông, tôi cứ tưởng nó bị rụng tóc rơi vào người hoặc tiến hóa ngược mọc lông giống chuột. Nhưng khi đặt mẫu da dưới kính hiển vi, sự thật lại nằm ở một chân trời hoàn toàn khác!". Bố cục: Trong bong bóng suy nghĩ hài hước của ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế, vẻ mặt bất lực hài hước, chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán đội tóc giả xù hoặc mặc áo lông chuột ngớ ngẩn; kính hiển vi đặt bên cạnh để kiểm chứng. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trời đất ơi, đi bơi giữa suối lạnh mà anh mặc nguyên cái áo lông rậm rạp thế kia không thấy vướng víu à?". Bố cục: BÊN TRÁI một chú ếch xanh bình thường (không đeo gương, da trơn) đang bơi giữa suối tròn mắt há hốc; BÊN PHẢI chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán bơi tung tăng với bộ tua lông xù xì như đang mặc áo choàng lông thú.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chú ếch hàng xóm thắc mắc rất đúng trọng tâm, nhưng thực ra thứ mọc đầy hai bên sườn và đùi của Dị Nhân Đầm Lầy hoàn toàn không phải lông hay tóc gì cả!". Bố cục: chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán đứng khoanh tay giải thích cho chú ếch xanh hàng xóm, hai bên sườn phất phơ các sợi tua da mềm mại chứ không phải lông thú.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đó là hàng trăm sợi nhú da mềm, đường kính mỗi sợi chỉ từ 0,35 đến 0,45mm — mỏng tương đương sợi cước mảnh.". Bố cục: Cận cảnh bộ lông tua rua ở sườn chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán đặt cạnh một sợi cước câu cá trong suốt có kính lúp phóng to ở GIỮA để thấy độ mảnh của sợi nhú da.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bên trong mỗi sợi nhú da ấy chạy chằng chịt những mạch máu mao mạch sát ngay lớp biểu bì ngoài cùng.". Bố cục: Mặt cắt phóng to một sợi nhú da màu hồng tươi: bên trong chứa đầy mạng lưới mao mạch đỏ li ti chạy sát ngay lớp da mỏng ngoài cùng. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và kỳ lạ nhất là chỉ có con đực mới mọc bộ lông kỳ dị này vào đúng mùa sinh sản, khoảng từ tháng 4 đến tháng 6 hàng năm!". Bố cục: So sánh đôi vợ chồng ếch dưới ánh nắng mùa hạ: BÊN TRÁI cô ếch cái da trơn nhẵn; BÊN PHẢI chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán con đực mọc đầy bộ râu lông hai bên sườn đứng cạnh tờ lịch mùa sinh sản.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tại sao tạo hóa lại gắn hàng trăm sợi tua rua mạch máu lên hông một ông bố ếch?". Bố cục: Bác sĩ cổ điển với cặp kính gọng tròn đang soi bản vẽ giải phẫu cổ trên bàn gỗ đặt dấu chấm hỏi vào sườn chú ếch mọc tua lông. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Câu trả lời được nhà động vật học Nô-bờ tìm ra từ năm 1925 khi mổ xẻ nội soi lá phổi của nó.". Bố cục: Tài liệu khoa học cổ và phim soi nội soi hiển thị hai lá phổi nhỏ xíu, cấu tạo khác biệt rõ rệt giữa ếch đực và ếch cái. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hóa ra phổi của Dị Nhân Đầm Lầy con đực có cấu tạo vô cùng kỳ quặc và hạn chế so với nhu cầu năng lượng khổng lồ lúc nó vận động cơ bắp!". Bố cục: Phim X-quang đối chiếu ngực ếch: phổi của chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán con đực rất nhỏ và có túi cơ lạ, biểu tượng đồng hồ đo oxy báo thiếu hụt khi vận động mạnh.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi con cái đẻ trứng xong rồi lên bờ rừng lá khô đi chơi, ông bố ếch phải ở lại lặn ngụp dưới lòng suối đá chảy xiết để canh giữ bọc trứng suốt nhiều tuần liền!". Bố cục: Chia đôi cảnh suối rừng: BÊN TRÁI trên bờ lá khô cô ếch cái đeo kính râm tung tăng đi dạo; BÊN PHẢI dưới đáy suối đá nước chảy xiết là chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán ngồi lì canh một bọc trứng tròn xoe.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ngồi lì dưới nước mà không được ngoi lên thở liên tục, lại phải gồng mình trông con, lượng oxy qua lá phổi tí hon hoàn toàn không đủ dùng!". Bố cục: chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán ngồi dưới đáy suối nước xanh, trên ngực hiện hình lá phổi tí hon đang thở hổn hển với thanh pin báo đỏ yếu ớt.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thế là cơ thể nó tự kích hoạt bản nâng cấp sinh học: mọc tua tủa hàng trăm sợi nhú da giàu mạch máu ở sườn và đùi để tăng gấp bội diện tích tiếp xúc với nước!". Bố cục: Cận cảnh hai bên sườn chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán bùng nổ mọc ra hàng trăm sợi tua rua da màu hồng nâu, phát sáng như bật chế độ tăng lực sinh học.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Những sợi lông giả đó hoạt động chẳng khác nào một dàn mang cá tạm thời, hút oxy trực tiếp từ dòng suối xuyên qua da vào thẳng máu!". Bố cục: Những bong bóng oxy nhỏ màu xanh ngọc từ dòng nước suối đang thấm xuyên thẳng qua các sợi tua rua da của chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán vào mạch máu, giống hệt cơ chế mang cá.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa hết, lúc ẩn mình dưới đá suối, đám tua rua lất phất theo dòng nước còn trông y hệt đám rêu tảo, giúp ông bố ngụy trang che mắt kẻ săn mồi!". Bố cục: chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán nấp sát hòn đá dưới suối, bộ tua rua lất phất hòa lẫn hoàn toàn vào đám rêu tảo xanh rì; một con chim săn mồi đậu phía trên ngó xuống tìm không ra.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hết mùa giữ trứng, bộ lông tự động teo rụng sạch sẽ, trả lại vẻ bảnh bao gọn gàng!". Bố cục: Đàn nòng nọc nhỏ bơi tung tăng đi xa; chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán rụng hết tua lông bên sườn trở lại làn da trơn láng bảnh bao, mỉm cười vẫy tay chào con.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hạng mục khám thứ ba: Kiểm tra hồ sơ gia phả dị nhân! Khi tiến sĩ David Blackburn kiểm tra mẫu vật của 63 loài ếch châu Phi trong bảo tàng, ông phát hiện không chỉ mình Dị Nhân Đầm Lầy biết chơi chiêu rút xương làm vuốt!". Bố cục: ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế, vẻ mặt bất lực hài hước mở ngăn tủ hồ sơ bảo tàng chất đầy hàng chục lọ tiêu bản ếch châu Phi được đánh số gọn gàng để kiểm tra gia phả. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tổng cộng có tới 11 loài thuộc ba chi họ hàng ở Trung Phi đều sở hữu bộ vũ khí giấu kín đáng sợ này!". Bố cục: Bảng xếp đội hình 11 chú ếch châu Phi thuộc ba nhóm họ hàng đứng dàn hàng ngang, tất cả đều giấu chiếc vuốt xương nhỏ dưới chân sau. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu mở rộng hồ sơ sang các loài lưỡng cư khác trên thế giới, hội tự hủy còn có một thành viên cực gắt khác là loài kỳ giông gân sườn Tây Ban Nha:". Bố cục: Bản đồ châu Âu và tấm hồ sơ giải phẫu lưỡng cư tự vệ mở ra trên bàn bác sĩ, hình vẽ chú kỳ giông Tây Ban Nha đang chuẩn bị tư thế phòng thủ. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "khi bị tấn công, nó đẩy thẳng những đầu xương sườn nhọn hoắt xuyên qua lớp da hai bên hông kèm chất độc!". Bố cục: Một chú kỳ giông gân sườn Tây Ban Nha màu xám nâu đốm cam mặc áo choàng gai, gồng lưng đẩy các đầu gai xương sườn trắng nhọn chọc nhẹ qua hai bên hông đầy vẻ ngầu lòi (kiểu hoạt hình, không máu). KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuy vậy, cơ chế bẻ đứt mối nối xương ở đầu ngón chân để phóng ra chiếc vuốt cong sắc bén như dao găm của ếch châu Phi vẫn là thiết kế độc nhất vô nhị trong toàn bộ giới động vật có xương sống!". Bố cục: Đặt cạnh nhau trên bệ trưng bày: chiếc vuốt xương cong như dao găm của chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán tỏa hào quang vàng đứng hạng nhất về độ độc lạ trong giới động vật có xương sống.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa hết đâu các đồng nghiệp, hãy soi kỹ cả đôi bàn tay trước của ông bố Dị Nhân Đầm Lầy! Nếu chân sau giấu dao găm để chiến đấu, thì trên ngón cái bàn tay trước của con đực lại mọc lên 3 hàng gai sừng màu đen cứng như kìm sắt!". Bố cục: Phóng to bàn tay trước của chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán: trên ngón cái mập mạp có ba hàng gai sừng màu đen cứng cáp xếp đều tăm tắp như gai lốp xe địa hình.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bộ gai nhám này không dùng để đánh nhau, mà để khóa chặt vào thân bạn đời hoặc bám vững vào tảng đá trơn trượt giữa dòng suối chảy xiết trong mùa mưa!". Bố cục: chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán dùng hai bàn tay trước có gai nhám ôm ghì chặt lấy một tảng đá trơn nhẵn giữa dòng thác nước chảy xiết trắng xóa mà không bị cuốn trôi.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng đừng thấy nó nhỏ bé mà chủ quan đưa tay ra nựng! Năm 1954, nhà tự nhiên học nổi tiếng người Anh Gerald Durrell từng thuật lại cú sốc nhớ đời trong cuốn sách của ông.". Bố cục: Nhà tự nhiên học mặc đồ thám hiểm kaki đội mũ cối ở BÊN TRÁI cầm cuốn sổ da, rón rén đưa tay về phía chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán đang ngồi giả vờ ngây thơ ở BÊN PHẢI.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi ông dùng tay không bắt sống một chú Dị Nhân Đầm Lầy hoang dã, nó lập tức đạp mạnh 2 chân sau, phóng vuốt xương cào thẳng vào lòng bàn tay ông những vết rách sâu hoắm chảy máu đầm đìa!". Bố cục: chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán đạp tung hai chân sau giơ vuốt xương lên; nhà thám hiểm giật bắn người rụt tay lại với vài vệt băng đỏ dán ngang lòng bàn tay và biểu cảm sốc nặng (hài hước, không máu me ghê rợn).
```
</details>

<details><summary>L57</summary>

```text
HÌNH L57 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đúng là nhìn mặt hiền khô tưởng cục đất biết nhảy, ai ngờ chạm vào là mất ngay miếng thịt tay!". Bố cục: Chia đôi: BÊN TRÁI chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán cười hiền lành giả vờ như cục đất dễ thương; BÊN PHẢI hiện nguyên hình giơ hai chân đầy vuốt xương sắc bén khiến người xem giật mình.
```
</details>

<details><summary>L58</summary>

```text
HÌNH L58 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bác sĩ ơi, thế mấy con nòng nọc mới nở ra đã có vuốt xương đâm rách tay chưa ạ?". Bố cục: Một chú nòng nọc hoạt hình tròn trĩnh màu nâu nhạt bơi trong cốc thủy tinh tròn, tò mò giơ cái đuôi lên hỏi ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế, vẻ mặt bất lực hài hước đứng bên cạnh.
```
</details>

<details><summary>L59</summary>

```text
HÌNH L59 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Câu hỏi rất hay! Nòng nọc bé xíu sống dưới nước thì chưa mọc vuốt đâu cháu ạ, nhưng ở những loài họ hàng gần cùng nhóm, ngay cả những chú ếch con mới bước lên bờ cũng đã trang bị sẵn bộ vuốt xương giấu kín dưới chân để phòng thân rồi!". Bố cục: Chia đôi: BÊN TRÁI chú nòng nọc nhỏ xíu trơn tru chưa có chân tay bơi trong nước; BÊN PHẢI một chú ếch con bé bằng đồng xu vừa bước lên bờ đã giấu sẵn chiếc vuốt xương tí hon dưới bàn chân.
```
</details>

<details><summary>L60</summary>

```text
HÌNH L60 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuổi nhỏ tài cao, vừa ra đời đã mang theo vũ khí hạng nặng!". Bố cục: Chú ếch con tý hon đội mũ bảo hiểm nhỏ xíu đứng oai vệ cạnh mô hình chiếc vuốt xương phóng to bằng kính lúp đầy tự hào. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này.
```
</details>

<details><summary>L61</summary>

```text
HÌNH L61 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hạng mục khám thứ tư: Khảo sát hiện trường thực địa tại rừng núi Cameroon! Trong khi giới khoa học phương Tây đến tận năm 2008 mới giải mã hoàn toàn cơ chế vuốt xương của Dị Nhân Đầm Lầy,". Bố cục: Rừng núi Cameroon ban đêm ánh trăng xanh: ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế, vẻ mặt bất lực hài hước đeo đèn pin trên trán cùng người dân bản địa châu Phi chỉ tay về phía dòng suối đá có chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán.
```
</details>

<details><summary>L62</summary>

```text
HÌNH L62 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "thì người dân bản địa vùng Trung Phi đã... biết thừa độ nguy hiểm của nó từ hàng trăm năm trước rồi!". Bố cục: Người thợ săn bản địa châu Phi kinh nghiệm lắc đầu chỉ biển cảnh báo vào chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán đang ngồi trên đá suối, trên đầu có đồng hồ cát quay ngược thời gian hàng trăm năm. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này.
```
</details>

<details><summary>L63</summary>

```text
HÌNH L63 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tại nhiều làng ở Cameroon, thịt ếch lông nướng là một món ăn truyền thống rất được ưa chuộng.". Bố cục: Quầy bếp lửa trại ngoài trời ở làng quê châu Phi với khói tỏa nghi ngút và xiên đồ nướng thơm lừng đặt trên đĩa gỗ; không vẽ cảnh giết mổ. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này.
```
</details>

<details><summary>L64</summary>

```text
HÌNH L64 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng có một quy tắc bất thành văn khi đi săn ban đêm: tuyệt đối không bao giờ thò tay không chộp lấy con ếch! Nếu lỡ tay túm nhầm, tám chiếc vuốt xương ở 2 chân sau sẽ đạp phăng vào cổ tay gây chảy máu rất đau đớn!". Bố cục: Biển cảnh báo hoạt hình màu vàng hình bàn tay bị gạch chéo đỏ to đùng phía trên đầu chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán đang giơ chân sau khoe tám chiếc vuốt xương.
```
</details>

<details><summary>L65</summary>

```text
HÌNH L65 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vậy nên các thợ săn phải vác theo dao rựa hoặc chế tạo riêng những cây giáo cán dài để giữ khoảng cách an toàn!". Bố cục: Hai người thợ săn hoạt hình châu Phi đứng từ xa giơ những cây sào giáo dài bằng gỗ để giữ khoảng cách an toàn với chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán ngồi trên tảng đá bờ suối.
```
</details>

<details><summary>L66</summary>

```text
HÌNH L66 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và đây là cú trớ trêu lịch sử khiến cả phòng khám phải bật cười: nhiều cây giáo chuyên dụng dùng để săn loài ếch Wolverine này được rèn với phần đầu có đúng 3 lưỡi nhọn chĩa ra phía trước —". Bố cục: Cận cảnh đầu cây giáo sắt dùng săn ếch ở GIỮA: có đúng ba lưỡi nhọn song song chĩa thẳng ra ngoài cực bén, ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế, vẻ mặt bất lực hài hước đứng cạnh bật cười chỉ vào. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này.
```
</details>

<details><summary>L67</summary>

```text
HÌNH L67 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "trông chẳng khác nào bộ vuốt ba ngạnh bằng kim loại của nhân vật Người Sói Wolverine ngoài đời thực!". Bố cục: Đặt cạnh nhau để đối chiếu: BÊN TRÁI là đầu giáo sắt ba lưỡi; BÊN PHẢI là bàn tay vuốt ba ngạnh kim loại kiểu siêu anh hùng Người Sói lóe sáng hài hước. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này.
```
</details>

<details><summary>L68</summary>

```text
HÌNH L68 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Muốn săn Người Sói đầm lầy, thợ săn buộc phải tự chế vũ khí Người Sói để đối đầu!". Bố cục: So sánh đối xứng hài hước: BÊN TRÁI người thợ săn cầm cây giáo ba mũi; BÊN PHẢI chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán giơ ba ngón chân có vuốt xương chĩa thẳng về phía trước như đấu kiếm.
```
</details>

<details><summary>L69</summary>

```text
HÌNH L69 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thậm chí người dân tộc Bakossi ở Cameroon xưa kia còn lưu truyền một huyền thoại cực kỳ thú vị: họ tin rằng những con ếch mọc lông kỳ quái này không sinh ra từ dưới bùn, mà... rơi thẳng từ trên bầu trời xuống cùng những cơn mưa rào!". Bố cục: Minh họa truyền thuyết cổ tích hài hước: trên bầu trời đêm đầy sao và mây trắng, những chú chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán bung dù nhỏ bé rơi lả tả từ trên trời xuống ngôi làng phía dưới.
```
</details>

<details><summary>L70</summary>

```text
HÌNH L70 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhiều cặp vợ chồng hiếm muộn còn tin ăn món ếch này sẽ giúp sinh con thuận lợi.". Bố cục: Cảnh gia đình dân làng vui vẻ ngồi quây quần quanh mâm cơm ấm áp, bên trên là dấu gạch chéo khoa học nhẹ nhàng giải thích đây chỉ là niềm tin dân gian. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này.
```
</details>

<details><summary>L71</summary>

```text
HÌNH L71 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đến nay, khoa học đã xác nhận nó chẳng hề rơi từ vũ trụ nào cả, mà chỉ là một kỳ quan tiến hóa bản địa chính hiệu — thậm chí còn được xếp vào nhóm 3,5% loài lưỡng cư có độ độc đáo di truyền cao nhất hành tinh!". Bố cục: Sơ đồ cây tiến hóa rực rỡ ở GIỮA: chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán đứng trên bục vinh quang top đầu giữa hàng trăm loài ếch nhái khác, đội chiếc cúp độc đáo di truyền.
```
</details>

<details><summary>L72</summary>

```text
HÌNH L72 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tổng kết hồ sơ bệnh án số 21. Thực lòng mà nói, tôi vẫn còn rùng mình mỗi khi nhìn lại tấm phim X-quang bàn chân của Dị Nhân Đầm Lầy.". Bố cục: ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế, vẻ mặt bất lực hài hước đứng cạnh bảng đèn X-quang bàn chân ếch, nhìn chăm chú với ánh mắt cảm phục, tay cầm bút ghi chú vào bệnh án số 21.
```
</details>

<details><summary>L73</summary>

```text
HÌNH L73 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Để sinh tồn giữa rừng mưa khắc nghiệt đầy rẫy rắn rết và chim săn mồi, chú ếch nhỏ bé dài chỉ 13cm này chấp nhận tự làm đau chính mình, bẻ mối nối xương đâm rách da thịt chỉ trong tích tắc để đổi lấy cơ hội sống sót!". Bố cục: chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán đứng vững giữa vòng vây của một con rắn rừng và bóng chim săn mồi từ trên cao, hai chân sau sẵn sàng bung vuốt xương tự vệ dũng cảm.
```
</details>

<details><summary>L74</summary>

```text
HÌNH L74 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "sẵn sàng mọc cả bộ lông mạch máu kỳ dị để ngồi lặng lẽ dưới dòng suối lạnh buốt suốt nhiều tuần liền, bảo vệ từng quả trứng nhỏ bé cho thế hệ tương lai.". Bố cục: Cảnh ấm áp dưới lòng suối xanh trong: chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán với bộ tua lông sườn dịu dàng ôm che bọc trứng tròn phát sáng vàng ấm áp để bảo vệ đàn con.
```
</details>

<details><summary>L75</summary>

```text
HÌNH L75 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kê đơn cuối cùng: cho bệnh nhân xuất viện ngay lập tức, tặng thêm một cuộn băng cá nhân dự phòng và khuyến cáo người xem... đừng bao giờ thử bắt chước! Ký tên: bác sĩ đã hoàn toàn bất lực!". Bố cục: ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế, vẻ mặt bất lực hài hước đóng dấu đỏ lên tờ giấy xuất viện, trao cho chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán một cuộn băng cá nhân to đùng làm quà; chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán vẫy tay cười tươi rời phòng khám.
```
</details>

<details><summary>L76</summary>

```text
HÌNH L76 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn các đồng nghiệp thì sao? Nếu bắt buộc phải chọn một trong hai trang bị của Dị Nhân Đầm Lầy: sở hữu vuốt xương giấu kín nhưng mỗi lần rút hơi rát tay,". Bố cục: Hai lựa chọn đặt trên hai bàn cân: BÊN TRÁI biểu tượng vuốt xương trắng kèm cuộn băng gạc; BÊN PHẢI biểu tượng bộ lông sườn cùng bình oxy lặn biển, dấu hỏi chấm ở giữa. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này.
```
</details>

<details><summary>L77</summary>

```text
HÌNH L77 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "hay mọc lông kín sườn để lặn thở dưới nước không cần bình oxy, bạn chọn cái nào? Hãy bình luận lựa chọn của bạn bên dưới nhé!". Bố cục: Các bạn nhỏ hoạt hình hào hứng ngồi giơ hai tấm thẻ biểu tượng: một thẻ vẽ hình chiếc vuốt xương, một thẻ vẽ hình ống thở oxy dưới nước (không có chữ). KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này.
```
</details>

<details><summary>L78</summary>

```text
HÌNH L78 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hồ sơ phòng khám hôm nay xin tạm đóng. Nhưng tập sau, chúng ta sẽ chuyển thẳng sang phòng thí nghiệm năm cấp độ để đối mặt với một ca tiến hóa còn điên rồ hơn nữa!". Bố cục: ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế, vẻ mặt bất lực hài hước đóng quyển sổ bệnh án dày cộp trên bàn, ánh sáng đèn phòng khám chuyển sang ánh sáng neon xanh của phòng thí nghiệm năm cấp độ với nhiều ống nghiệm sủi bọt. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này.
```
</details>

<details><summary>L79</summary>

```text
HÌNH L79 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một sinh vật nhỏ xíu sống dưới nước với khuôn mặt lúc nào cũng mỉm cười, trên đầu mọc 6 chiếc sừng lông xù như ăng-ten ngoài hành tinh...". Bố cục: Một sinh vật bí ẩn được vẽ hoàn toàn bằng BÓNG ĐEN ĐẶC TUYỀN (solid black silhouette) bên trong bể nước phòng thí nghiệm: hình dáng một sinh vật lưỡng cư nhỏ có sáu chiếc tua sừng xù ba nhánh hai bên đầu và chiếc đuôi dài, kèm dấu hỏi chấm vàng lớn phát sáng phía trên; KHÔNG vẽ rõ mắt mũi hay màu da thật. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này.
```
</details>

<details><summary>L80</summary>

```text
HÌNH L80 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Điều khiến các nhà khoa học mất ngủ là dù có bị mất chân, đứt tủy sống, thậm chí mất cả 1/3 trái tim và một phần não bộ, nó vẫn tự mọc lại nguyên vẹn hoàn toàn mà không để lại lấy một vết sẹo nào!". Bố cục: Cũng chiếc BÓNG ĐEN ĐẶC TUYỀN (solid black silhouette) của sinh vật có sáu sừng lông xù và đuôi dài đó đứng ở GIỮA, xung quanh tỏa hào quang tái sinh màu xanh lá với biểu tượng trái tim ghép liền và tia sét hồi phục không tì vết. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này.
```
</details>

<details><summary>L81</summary>

```text
HÌNH L81 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đố các bạn biết bóng đen bí ẩn kỳ sau là loài vật nào? Hãy đoán ngay ở phần bình luận nhé!". Bố cục: Chiếc BÓNG ĐEN ĐẶC TUYỀN bí ẩn có sáu sừng lông xù đứng giữa khung kính hiển vi và ba dấu hỏi chấm lớn lấp lánh vàng cam mời gọi khán giả đoán tên. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này.
```
</details>

<details><summary>L82</summary>

```text
HÌNH L82 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và ẩn sau vẻ ngoài lầm lì cùng biệt danh quái vật kinh dị, đó lại là một ông bố mẫu mực đến mức đáng nể:". Bố cục: Chia đôi: BÊN TRÁI một cái bóng đen oai vệ có sáu gai nhỏ; BÊN PHẢI là chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán cười hiền hậu đeo tạp dề người cha mẫu mực.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Bệnh nhân này vào phòng cấp cứu không phải vì bị thú dữ cắn,". Bố cục: Khung dọc phòng cấp cứu: phía trên ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế, vẻ mặt bất lực hài hước cầm bảng bệnh án há hốc mồm; phía dưới chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán ngồi trên giường bệnh.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "mà vì nó vừa... tự bẻ gãy xương ngón chân mình đâm thủng qua da!". Bố cục: Cận cảnh bàn chân sau của chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán tự gồng cơ bắp chân làm các chiếc xương ngón chân nhọn đâm xuyên qua lớp băng và da chui ra ngoài.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Xin giới thiệu Ếch Lông Wolverine, gã dị nhân dài 13cm sống dọc các dòng suối núi ở Trung Phi.". Bố cục: chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán ngồi bảnh bao trên tảng đá suối rừng Trung Phi, bên cạnh có chiếc thước đo chiều cao màu vàng dựng thẳng.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Dưới lớp da 8 ngón chân sau của nó giấu sẵn những chiếc móc xương nhọn hoắt nối với đầu ngón bằng sợi collagen.". Bố cục: Mặt cắt phóng đại ngón chân sau của ếch theo khung dọc: đầu xương nhọn hình móc câu giấu kín trong thịt, nối vào cục xương nhỏ đầu ngón bằng dải dây chằng hồng. KHÔNG có chú ếch đeo gương bác sĩ trên trán trong cảnh này.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Khi bị kẻ thù tóm lấy, nó gồng cơ chân giật đứt mối nối đó". Bố cục: chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán quay đầu giận dữ trước một con rắn rừng, gồng cơ bắp chân sau giật đứt sợi dây nối hồng bên trong ngón chân.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "và đẩy thẳng xương trần sắc lẹm chọc rách lớp da thịt lao ra ngoài làm vuốt chiến đấu!". Bố cục: Hai bàn chân sau của chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán đồng loạt bật phựt bốn chiếc vuốt xương trắng sắc lẹm đâm xuyên qua lớp da đầu ngón lao ra ngoài như dao găm.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Một nhà tự nhiên học từng bắt sống nó và bị cào rách tay chảy máu sâu hoắm!". Bố cục: Nhà thám hiểm đội mũ cối giật mình rụt tay lại khi bị chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán quơ chân cào xước, dán mấy miếng băng cá nhân trên lòng bàn tay (hài hước, không máu).
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Chưa hết, đến mùa sinh sản, con đực còn mọc hàng trăm sợi lông da rậm rạp hai bên sườn dày chỉ 0,4mm!". Bố cục: chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán bơi dưới nước suối trong, hai bên sườn và đùi mọc tua tủa hàng trăm sợi lông da xù xì lất phất trong nước, kính lúp phóng to một sợi lông mảnh.
```
</details>

<details><summary>S09</summary>

```text
HÌNH S09 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Lý do cực kỳ cảm động: ông bố phải ngồi lì dưới nước canh trứng suốt nhiều tuần nên cần bộ lông mạch máu này". Bố cục: chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán làm ông bố tận tụy ôm giữ bọc trứng vàng dưới đáy suối đá, mắt dõi theo đàn trứng bảo vệ cẩn thận.
```
</details>

<details><summary>S10</summary>

```text
HÌNH S10 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "để hút thêm oxy qua da thay cho lá phổi bé xíu!". Bố cục: Sơ đồ cắt lớp dưới nước: các bong bóng oxy xanh ngọc từ suối xuyên qua lớp tua lông da đi thẳng vào người chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán, bên cạnh là hình lá phổi tí hon yếu ớt.
```
</details>

<details><summary>S11</summary>

```text
HÌNH S11 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Một gã dị nhân vừa biết tự rách da rút vuốt xương, vừa mọc mang lông làm ông bố tận tụy,". Bố cục: Chân dung ngầu lòi cực hài của chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán giữa khung dọc: một bên sườn có tua lông phấp phới, hai chân sau bật vuốt xương sáng loáng.
```
</details>

<details><summary>S12</summary>

```text
HÌNH S12 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Ếch Lông Wolverine nâu rêu mũm mĩm, tua lông xù hai bên sườn, đeo gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "đúng là siêu anh hùng kỳ quặc nhất thế giới tự nhiên!". Bố cục: chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán khoanh tay đứng oai vệ trên tảng đá rêu giữa khung dọc với áo choàng lá rừng nhỏ bay phấp phới, đeo gương bác sĩ bạc sáng lấp lánh.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/82 của video YouTube về Ếch Lông Wolverine). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán. Nhân vật phụ cố định: ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế, vẻ mặt bất lực hài hước; cô trợ lý phòng khám hoạt hình mặc áo blouse xanh nhạt, kẹp tập hồ sơ bệnh án. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/12 của video YouTube Shorts về Ếch Lông Wolverine). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Ếch Lông Wolverine (Trichobatrachus robustus) hoạt hình mũm mĩm màu nâu rêu pha vệt xanh ô-liu, thân bè tròn, đầu to mõm ngắn, hai mắt vàng to lồi biểu cảm hài hước, hai bên sườn và đùi có tua lông da xù xì màu nâu xanh, đeo một chiếc băng đô gương soi tròn màu bạc của bác sĩ trên trán. Nhân vật phụ: ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế, vẻ mặt bất lực hài hước. 
```
</details>

## 7. SEO

- **title:** Loài Ếch Tự Bẻ Xương Đâm Thủng Da Làm Vuốt Wolverine?!
- **hook_paragraph:** Ếch Lông Wolverine (Trichobatrachus robustus) ở Trung Phi dài chỉ 13cm nhưng sở hữu vũ khí kinh dị bậc nhất tự nhiên: tự gồng cơ giật đứt mối nối collagen để đẩy xương ngón chân đâm thủng da làm vuốt chiến đấu! Chưa hết, con đực mùa sinh sản còn mọc bộ lông mạch máu dày 0,4mm để thở dưới nước khi canh trứng.
- **question:** Nếu phải chọn 1 trong 2 'năng lực' của Ếch Lông Wolverine: rút vuốt xương (hơi đau) hay mọc lông sườn để thở dưới nước, bạn chọn cái nào? Và bạn đoán bóng đen tập sau là loài nào?
- **next_teaser:** Bóng đen bí ẩn luôn mỉm cười với 6 chiếc sừng lông xù: mất 1/3 trái tim hay não bộ vẫn mọc lại nguyên vẹn không sẹo!
- **shorts_title:** Loài Ếch Tự Bẻ Xương Đâm Thủng Da Làm Vuốt?! 🐸 #độngvật #ếchlôngwolverine
- **shorts_desc:** Ếch Lông Wolverine dài 13cm ở Trung Phi có thể tự giật đứt mối nối collagen để đẩy xương ngón chân đâm xuyên qua da làm vuốt chiến đấu! Mùa giữ trứng con đực còn mọc hàng trăm sợi nhú da 0,4mm để hút oxy dưới nước.
- **bullets:** Chụp X-quang: 8 ngón chân sau giấu vuốt xương trần không bọc sừng keratin, mũi xương dày 0,13mm · Không có cơ kéo thu vuốt: vuốt xương trượt ngược thụ động và da tự liền nhờ khả năng tái tạo lưỡng cư · Nội soi da: Bộ lông ở sườn thực chất là nhú da 0,35-0,45mm đầy mao mạch giúp thở dưới nước khi giữ trứng · Thực địa Cameroon: Thợ săn phải chế giáo dài 3 lưỡi để tránh bị vuốt ếch cào rách tay
- **tags:** ếch lông wolverine, ech long wolverine, hairy frog, horror frog, trichobatrachus robustus, ếch bẻ xương làm vuốt, ếch người sói, động vật kỳ lạ, thế giới động vật, động vật hài hước, vẽ chuyện hoang dã, whiteboard animation, khoa học thú vị, bệnh án tiến hóa
- **hashtags:** #độngvật #ếchlôngwolverine #VẽChuyệnHoangDã

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-21-ech-long-wolverine
python src/episode/pipeline.py tts    projects/tap-21-ech-long-wolverine     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-21-ech-long-wolverine     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-21-ech-long-wolverine     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-21-ech-long-wolverine              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-21-ech-long-wolverine --force
python scripts/beat_sheet.py projects/tap-21-ech-long-wolverine               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-21-ech-long-wolverine/audio/shorts.wav projects/tap-21-ech-long-wolverine/renders/tap-21-ech-long-wolverine_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-21-ech-long-wolverine
python src/episode/pipeline.py seo    projects/tap-21-ech-long-wolverine
python src/episode/episode_doc.py     projects/tap-21-ech-long-wolverine
```
