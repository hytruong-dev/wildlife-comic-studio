# TẬP 44 — CÁ MẶT TRĂNG · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-44-ca-mat-trang`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-44-ca-mat-trang`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F1` · **Persona giọng:** `bac_si` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Cá Mặt Trăng |
| Tiêu đề YouTube | Gã Khổng Lồ 2 Tấn Vô Tri: Bị Hải Cẩu Cắn Vẫn Nằm Phơi Nắng?! \| Cá Mặt Trăng \| Tập 44 |
| Video dài | `renders/tap-44-ca-mat-trang_long.mp4` — 9:15.1 (555.1s) |
| Shorts | `renders/tap-44-ca-mat-trang_shorts.mp4` — 0:42.4 (42.4s) |
| Thumbnail | `renders/tap-44-ca-mat-trang_thumbnail.jpg` |
| Số hình | dài 58 beat / 58 ảnh riêng; Shorts 8 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.1**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/58 của video YouTube về Cá Mặt Trăng). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa vẽ tay đặc trưng cho chủ đề, nét mực sắc nét, màu sắc tương phản cuốn hút, tối giản giàu tính biểu tượng khoa học; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim. Nhân vật phụ cố định: chiếc cần cẩu công nghiệp màu vàng cam rực rỡ với dây cáp thép to bản; chú hải cẩu xám béo tròn đang ngoạm cắn đuôi cá mặt trăng; chú ấu trùng cá mặt trăng tí hon tròn xoe như quả cầu gai phi thuyền ngoài hành tinh. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — BỆNH ÁN GÃ KHỔNG LỒ 2 TẤN NGƠ NGÁC NHẤT ĐẠI DƯƠNG
*Thẻ chương:* BỆNH ÁN GÃ KHỔNG LỒ HAI TẤN CỤT ĐUÔI VÔ TRI NHẤT ĐẠI DƯƠNG

*Badge:* `HỒ SƠ BỆNH ÁN` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene01_p0.wav` (480 ký tự) · mood `hao_hung`

```text
Mời bệnh nhân tiếp theo bước vào phòng cấp cứu đa khoa sinh vật biển khơi! Y tá đâu, điều động ngay cho tôi một chiếc cần cẩu công nghiệp tải trọng mười tấn và một bể nước muối dung tích một trăm mét khối khẩn cấp! Bệnh nhân hôm nay của chúng ta là một ca bệnh tâm lý và giải phẫu kỳ quặc bậc nhất hành tinh: Một sinh vật biển nặng tương đương một chiếc xe ô tô tải bọc thép, nhưng gương mặt lúc nào cũng đờ đẫn ngơ ngác tựa như không hề có một gợn sóng suy nghĩ nào trong não bộ!
```
**Part 1** → `audio/vs/scene01_p1.wav` (116 ký tự) · 🎭 cameo `co_tro_ly`

```text
Bác sĩ ơi, cái cân điện tử của bệnh viện vừa sập gãy đôi rồi ạ! Con cá này nó to như cái bánh xe khổng lồ ấy bác ơi!
```
**Part 2** → `audio/vs/scene01_p2.wav` (496 ký tự) · mood `hao_hung`

```text
[surprise-oh] Bệnh nhân mang mã số bốn mươi tư của chúng ta có tên khoa học là Mola mola, hay còn gọi là Cá Mặt Trăng đại dương! Nhưng tôi thường gọi thân mật ca bệnh khó đỡ này là: Gã khổng lồ vô tri! Trong khi các loài thủy quái biển sâu sở hữu hàm răng sắc nhọn, thân hình thuôn dài khí động học để săn mồi chớp nhoáng, thì bệnh nhân này lại có một thân hình dẹt tròn lẳn cụt ngủn chẳng khác nào một cái đầu cá khổng lồ bị cắt cụt đuôi đang lềnh bềnh trôi dạt giữa đại dương bao la! [laughter]
```
**Part 3** → `audio/vs/scene01_p3.wav` (541 ký tự) · mood `tram_bi_an`

```text
Khám nghiệm thể trọng của gã sẽ khiến bạn phải ngã ngửa: Một con cá mặt trăng trưởng thành có thể đạt chiều dài hơn ba mét, sải vây từ đỉnh vây lưng xuống vây bụng lên tới bốn mét, và cân nặng vượt mốc hai tấn! Đây chính là loài cá có xương thật nặng nhất trên toàn bộ hành tinh Trái Đất! Nhưng nhìn vào đôi mắt tròn xoe vô hồn và chiếc miệng tròn vo lúc nào cũng há hốc ra ngơ ngác, bạn sẽ tự hỏi: Làm thế nào mà một cỗ máy sinh học ngớ ngẩn nhường này lại có thể sinh tồn suốt hàng chục triệu năm qua giữa muôn trùng hiểm nguy của biển cả?
```

### scene02 — CẤU TẠO XƯƠNG SỤN KỲ LẠ VÀ THÙY ĐUÔI CLAVUS CỤT NGỦN
*Thẻ chương:* CỖ MÁY SINH HỌC CỤT ĐUÔI BƠI BẰNG HAI CÁNH VÂY KHỔNG LỒ

*Badge:* `GIẢI PHẪU DỊ TẬT` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene02_p0.wav` (410 ký tự) · mood `don_dap`

```text
Hãy đặt tấm phim chụp cắt lớp vi tính toàn thân của Gã khổng lồ vô tri lên màn hình chẩn đoán! Điều đầu tiên khiến toàn thể bác sĩ phẫu thuật phải dụi mắt hoài nghi: Con cá này hoàn toàn không có đuôi cá thật sự! Trong giải phẫu học loài cá, chiếc vây đuôi phía sau là động cơ đẩy chính giúp cá tăng tốc rẽ sóng. Nhưng ở cá mặt trăng, xương đuôi và cuống đuôi đã bị teo biến hoàn toàn trong quá trình tiến hóa!
```
**Part 1** → `audio/vs/scene02_p1.wav` (78 ký tự) · 🎭 cameo `co_tro_ly`

```text
Ủa bác sĩ ơi, thế cái rìa thịt lượn sóng phía sau mông của nó là cái gì thế ạ?
```
**Part 2** → `audio/vs/scene02_p2.wav` (634 ký tự) · mood `hao_hung`

```text
[surprise-wa] Cô trợ lý đã phát hiện đúng dị tật độc nhất vô nhị của bệnh nhân! Phần viền thịt nhăn nheo phía sau đuôi gã được các nhà giải phẫu gọi là thùy clavus! Đây thực chất là phần vây lưng và vây hậu môn bị kéo dài rồi hợp nhất lại thành một chiếc bánh lái thịt cụt lủn! Chiếc bánh lái này hoàn toàn không có lực đẩy về phía trước, mà chỉ đóng vai trò như một bánh lái tàu thủy lờ đờ rẽ hướng! [laughter] Chưa hết đâu nhé, bộ xương của gã khổng lồ hai tấn này phần lớn không phải là xương cứng đặc như cá chép hay cá ngừ, mà đã thoái hóa thành chất sụn xốp mềm chứa đầy nước, giúp cơ thể gã giảm thiểu tối đa trọng lượng riêng!
```
**Part 3** → `audio/vs/scene02_p3.wav` (659 ký tự) · mood `nghiem_trang_gia`

```text
Đặc biệt hơn nữa, Gã khổng lồ vô tri hoàn toàn không có bong bóng cá! Điều này đồng nghĩa với việc gã không thể điều chỉnh độ nổi nhẹ nhàng như các loài cá thông thường. Nhưng tạo hóa đã bù đắp cho gã một cặp động cơ phản lực sinh học thần sầu: Chiếc vây lưng cao vút và chiếc vây hậu môn dài ngoằng đập nhịp nhàng từ bên này sang bên kia giống hệt như đôi cánh của loài chim cánh cụt bay lượn dưới nước! Nhóm nghiên cứu của tiến sĩ Watanabe tại Đại học Tokyo đã gắn thẻ định vị điện tử và phát hiện ra: Gã khổng lồ này có thể bơi với vận tốc ba chấm hai ki-lô-mét một giờ, hoàn toàn không phải là một khúc gỗ mục trôi dạt vô định như người đời vẫn lầm tưởng!
```
**Part 4** → `audio/vs/scene02_p4.wav` (440 ký tự) · mood `hao_hung`

```text
Chưa hết đâu nhé, hãy nhìn vào tấm sinh thiết lớp biểu bì của gã! Cơ thể cá mặt trăng hoàn toàn không có vảy cá thông thường, mà được bọc kín bởi một lớp da collagen dày tới bảy chấm năm xăng-ti-mét, dẻo dai tựa như lớp lốp xe tải bọc thép! Phía trên bề mặt da phủ đầy những chiếc gai vi thể li ti tiết ra lớp chất nhờn kháng khuẩn trơn tuột, biến cơ thể gã thành một pháo đài đệm thịt êm ái hấp thụ mọi va đập giữa lòng đại dương sóng gió!
```

### scene03 — CHẾ ĐỘ ĂN 99% NƯỚC VÀ CHUYẾN LẶN SÂU 800 MÉT
*Thẻ chương:* LẶN SÂU TÁM TRĂM MÉT SĂN SỨA DƯỚI CÁI LẠNH BỐN ĐỘ C

*Badge:* `THỰC ĐƠN KỲ LẶC` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene03_p0.wav` (466 ký tự) · mood `don_dap`

```text
Chẩn đoán triệu chứng số ba dẫn chúng ta vào nhà bếp của Gã khổng lồ vô tri! Với thân hình đồ sộ nặng tới hai tấn, bạn nghĩ thực đơn hằng ngày của gã phải là những đàn cá ngừ béo ngậy hay mực ống giàu đạm đúng không? Hoàn toàn sai lầm! Chiếc miệng của cá mặt trăng nhỏ xíu, các răng dính liền lại thành một chiếc mỏ vẹt cứng nhắc không thể nhai nghiền con mồi lớn. Và món ăn khoái khẩu duy nhất chiếm tới chín mươi chín phần trăm khẩu phần của gã chính là: Sứa biển!
```
**Part 1** → `audio/vs/scene03_p1.wav` (353 ký tự) · mood `nghiem_trang_gia`

```text
Ai cũng biết sứa biển là một món ăn thảm họa dinh dưỡng: Cơ thể sứa chứa tới chín mươi chín phần trăm là nước muối, hàm lượng calo và protein thấp đến mức gần như bằng không! Để nuôi sống cỗ máy sinh học nặng hai tấn chỉ bằng sứa, Gã khổng lồ vô tri phải làm việc cật lực như một cỗ máy hút bụi đáy đại dương, nuốt chửng hàng trăm cân sứa biển mỗi ngày!
```
**Part 2** → `audio/vs/scene03_p2.wav` (534 ký tự) · mood `hao_hung`

```text
Nhưng nuốt một con sứa trơn tuột đầy chất nhầy vào bụng không hề đơn giản chút nào! Hãy cầm đèn pin soi sâu vào khoang miệng của bệnh nhân: Toàn bộ phần cuống họng của cá mặt trăng được trang bị những cụm răng họng nhọn hoắt xếp cong về phía sau! Khi gã hút nước nuốt sứa vào, chiếc cuống họng này hoạt động như một chiếc máy ép nước ly tâm: Răng họng giữ chặt con mồi không cho trôi ngược ra ngoài, đồng thời cơ họng co bóp cực mạnh để ép kiệt nước biển thừa ra khỏi mang trước khi tống cả tảng thạch sứa đậm đặc vào dạ dày tiêu hóa!
```
**Part 3** → `audio/vs/scene03_p3.wav` (459 ký tự) · mood `tram_bi_an`

```text
[surprise-oh] Để săn được những con sứa khổng lồ giàu dinh dưỡng, cá mặt trăng phải thực hiện những chuyến lặn thám hiểm cực kỳ mạo hiểm: Gã lặn thẳng xuống độ sâu tám trăm mét dưới đáy biển tăm tối, nơi áp suất nước nghiền nát kim loại và nhiệt độ tụt dốc thê thảm xuống chỉ còn bốn độ C! Nhờ lớp mỡ dày dưới da đóng vai trò như một lớp áo cách nhiệt, gã có thể săn mồi trong vùng nước băng giá suốt hàng giờ liền trước khi cơ thể bị hạ thân nhiệt nguy kịch!
```

### scene04 — HÀNH VI NẰM NGHIÊNG PHƠI NẮNG VÀ KHÁCH SẠN KÝ SINH TRÙNG
*Thẻ chương:* NẰM PHƠI NẮNG BỂ BƠI ĐỂ HỒI PHỤC THÂN NHIỆT VÀ TRỊ LIỆU

*Badge:* `SPA ĐẠI DƯƠNG` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene04_p0.wav` (493 ký tự) · mood `hao_hung`

```text
Sau mỗi chuyến lặn sâu tám trăm mét buốt giá dưới đáy đại dương, Gã khổng lồ vô tri lập tức kích hoạt liệu trình hồi sức cấp cứu độc nhất vô nhị: Gã ngoi thẳng lên mặt biển thoáng, lật nghiêng toàn bộ cơ thể dẹt hai tấn nằm phơi bụng nổi bồng bềnh trên mặt nước! Dưới ánh nắng mặt trời rực rỡ, bề mặt cơ thể rộng lớn của gã hoạt động tựa như một tấm pin năng lượng mặt trời khổng lồ, hấp thụ nhiệt lượng từ ánh nắng để sưởi ấm lại dòng máu lạnh giá và tái kích hoạt hệ thống tiêu hóa sứa biển!
```
**Part 1** → `audio/vs/scene04_p1.wav` (82 ký tự) · 🎭 cameo `co_tro_ly`

```text
Bác sĩ ơi, trên người con cá này lúc nhúc hàng ngàn con bọ ghẻ kinh dị lắm bác ơi!
```
**Part 2** → `audio/vs/scene04_p2.wav` (508 ký tự) · mood `don_dap`

```text
[surprise-wa] Đây chính là ca bệnh da liễu kinh hoàng nhất lịch sử phòng khám chúng ta! Do tốc độ di chuyển chậm rãi và lớp da nhớt không có vảy cứng, cơ thể cá mặt trăng trở thành một khách sạn năm sao di động cho hơn bốn mươi loài ký sinh trùng khác nhau bu bám! Có những loài giáp xác ký sinh cắm sâu vào mang, thậm chí ký sinh trùng này lại bị một loài ký sinh trùng khác đẻ trứng lên mình! [laughter] Nhưng Gã khổng lồ vô tri đã giải quyết vấn nạn này bằng một dịch vụ spa ngoài trời vô cùng thông minh!
```
**Part 3** → `audio/vs/scene04_p3.wav` (412 ký tự) · mood `hao_hung`

```text
Khi gã nằm nghiêng phơi nắng trên mặt biển, gã phát ra tín hiệu mời gọi các bác sĩ làm đẹp tự nhiên: Từng đàn cá bướm và cá thiên thần bơi lại rỉa sạch những con rận biển bám trên da gã. Thậm chí các chú chim mòng biển còn thản nhiên đáp thẳng xuống sườn của chú cá mặt trăng nổi bồng bềnh, cần mẫn dùng mỏ mổ từng con ký sinh trùng béo ngậy! Một dịch vụ cộng sinh spa miễn phí đỉnh cao giữa bầu trời và biển cả!
```
**Part 4** → `audio/vs/scene04_p4.wav` (626 ký tự) · mood `hao_hung`

```text
Đặc biệt hơn nữa, nếu liệu trình spa bằng chim mòng biển vẫn chưa giải quyết dứt điểm những con bọ bám dai dẳng, Gã khổng lồ vô tri sẽ kích hoạt tuyệt chiêu thể dục dưỡng sinh có một không hai: Gã lấy đà từ dưới làn nước sâu, quạt hai cánh vây hết tốc lực rồi phóng vọt cả khối thân nặng hai tấn bay thẳng lên khỏi mặt biển cao tới ba mét! [laughter] Sau đó, gã thả tự do rơi tự do rồi đập cả tấm thân dẹt khổng lồ xuống mặt nước đánh BẸP một tiếng vang dội như một vụ nổ pháo hoa! Cú va chạm bề mặt kinh thiên động địa ấy đủ sức đánh văng hàng loạt loài rận biển cứng đầu ra khỏi da thịt trong sự ngỡ ngàng của giới quan sát!
```

### scene05 — KỶ LỤC SINH SẢN ĐỈNH CAO BÙ ĐẮP CHỈ SỐ SINH TỒN CỰC THẤP
*Thẻ chương:* KỶ LỤC VÔ ĐỊCH ĐẺ BA TRĂM TRIỆU TRỨNG TRONG MỘT LẦN

*Badge:* `CỖ MÁY SINH SẢN` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene05_p0.wav` (485 ký tự) · mood `don_dap`

```text
Chẩn đoán y khoa cuối cùng giải mã lý do tại sao một sinh vật ngơ ngác, chậm chạp và không hề có vũ khí tự vệ lại không bị tuyệt chủng khỏi Trái Đất! Các thủy thủ viễn dương thường xuyên chứng kiến những cảnh tượng đau lòng: Khi bị hải cẩu hay sư tử biển tấn công, hải cẩu cắn đứt từng mảng vây của cá mặt trăng rồi xé toang lớp da, nhưng Gã khổng lồ vô tri vẫn chỉ trơ mắt nhìn trời với vẻ mặt bình thản không chút hoảng loạn! Gã hoàn toàn không có phản xạ tự vệ hay tấn công đáp trả!
```
**Part 1** → `audio/vs/scene05_p1.wav` (436 ký tự) · mood `nghiem_trang_gia`

```text
[surprise-oh] Với tỷ lệ bị săn bắt tàn khốc như vậy, chỉ một trong số hàng trăm triệu cá con có thể sống sót đến tuổi trưởng thành. Nhưng tạo hóa đã ban tặng cho bệnh nhân này một cỗ máy sinh sản vô địch thiên hạ: Trong mỗi mùa sinh sản, một con cá mặt trăng cái có thể phóng thích tới ba trăm triệu quả trứng vào làn nước biển! Đây là một kỷ lục vô tiền khoáng hậu, không một loài động vật có xương sống nào trên Trái Đất có thể so bì!
```
**Part 2** → `audio/vs/scene05_p2.wav` (497 ký tự) · mood `hao_hung`

```text
Hãy nhìn vào bức ảnh siêu âm ấu trùng của bệnh nhân: Chú cá con lúc mới chui ra khỏi vỏ trứng chỉ dài vỏn vẹn hai mi-li-mét, nhỏ hơn cả đầu tăm nhưng lại mang một ngoại hình cực kỳ tấu hài: Toàn thân chú cá con tròn ủng như một quả cầu gai, xung quanh mọc chìa ra hàng chục chiếc gai nhọn hoắt trông hệt như một chiếc phi thuyền người ngoài hành tinh tí hon! Chiếc áo giáp gai nhọn ấy giúp ấu trùng trôi nổi như sinh vật phù du và bảo vệ chúng khỏi miệng những kẻ săn mồi tí hon dưới đáy biển sâu!
```
**Part 3** → `audio/vs/scene05_p3.wav` (404 ký tự) · mood `hao_hung`

```text
Kỳ diệu hơn nữa, những chú cá mặt trăng sơ sinh vừa nở ra chỉ dài vỏn vẹn hai mi-li-mét, nhỏ hơn cả một hạt vừng và được bao bọc bởi những chiếc gai nhọn hoắt như một chú cá nóc mini! Từ kích thước hai mi-li-mét bé tí xíu ấy, cá con phải tăng trưởng khối lượng gấp sáu mươi triệu lần để trở thành một gã khổng lồ nặng hai tấn! Một bước nhảy vọt thể trọng vĩ đại nhất trong toàn bộ thế giới sinh vật biển!
```

### scene06 — ĐƠN THUỐC TIẾN HÓA VÀ THỬ THÁCH ĐOÁN TẬP 45
*Thẻ chương:* ĐƠN THUỐC TIẾN HÓA VÀ THỬ THÁCH ĐOÁN TẬP BỐN MƯƠI LĂM

*Badge:* `LỜI KẾT BỆNH ÁN` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene06_p0.wav` (508 ký tự) · mood `am_ap`

```text
Hồ sơ bệnh án số bốn mươi tư chính thức khép lại với kết luận chẩn đoán: Cá Mặt Trăng hoàn toàn khỏe mạnh và là một bài học sinh tồn triết lý sâu sắc của mẹ thiên nhiên! Đôi khi trong cuộc sống, bạn không cần phải quá bon chen ganh đua, không cần phải trang bị móng vuốt nanh nhọn để gầm gừ đe dọa người khác. Gã khổng lồ vô tri dạy chúng ta rằng: Cứ bình thản sống, cứ mở lòng phơi nắng đón nhận những điều tươi đẹp, và kiên trì mở lối đi riêng, đại dương bao la sẽ luôn dành cho bạn một chỗ đứng vững vàng!
```
**Part 1** → `audio/vs/scene06_p1.wav` (213 ký tự) · mood `hao_hung`

```text
Nếu được sinh ra với một đặc tính của loài cá mặt trăng, bạn muốn sở hữu chiếc đầu khổng lồ hai tấn vô tư phơi nắng hay cỗ máy sinh sản ba trăm triệu quả trứng? Hãy để lại bình luận chẩn đoán của bạn bên dưới nhé!
```
**Part 2** → `audio/vs/scene06_p2.wav` (397 ký tự) · mood `tram_bi_an`

```text
Còn bây giờ, hãy chuẩn bị bước vào bản tin hiện trường trực tiếp của hồ sơ số bốn mươi lăm! Một chú vẹt béo múp bốn cân đến từ New Zealand, loài vẹt duy nhất trên thế giới đã hoàn toàn quên mất cách bay, đêm đêm đi bộ cả chục cây số, và thỉnh thoảng lại thích trèo lên ngọn cây cao rồi nhảy ùm xuống đất đập mặt ngơ ngác! Bạn có biết phóng sự điều tra này sẽ đưa chúng ta gặp gỡ chú vẹt nào không?
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Nặng tới hai tấn nhưng hiền đến mức bị hải cẩu bơi lại cắn đứt từng mảng vây nó cũng chỉ nằm ngửa nhìn trời ngơ ngác! Đây là Cá Mặt Trăng, gã khổng lồ vô tri nặng nhất thế giới loài cá có xương! To xác như chiếc ô tô tải nhưng gã hoàn toàn không có đuôi cá thật sự, cơ thể cụt lủn chỉ có cái đầu tròn xoe bơi bằng hai cánh vây khổng lồ. Món ăn khoái khẩu của gã là sứa biển chứa chín mươi chín phần trăm nước, nên gã phải ăn cả tạ sứa mỗi ngày và lặn sâu tám trăm mét dưới cái lạnh bốn độ C. Sau mỗi chuyến lặn buốt giá, gã ngoi lên mặt nước nằm nghiêng phơi nắng để sưởi ấm dòng máu lạnh và cho chim mòng biển rỉa sạch ký sinh trùng. Đổi lại sự ngơ ngác ấy, cá mẹ đẻ tới ba trăm triệu quả trứng mỗi lần, một kỷ lục vô địch tuyệt đối trong giới động vật có xương sống!
```

**Whisper prompt:** `Cá Mặt Trăng, Mola mola, Gã khổng lồ vô tri, Cái đầu cụt biết bơi, thùy clavus, sứa biển, 2 tấn, 300 triệu trứng, 800 mét, 4°C, 3.2 km/h, Bác sĩ`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| bốn mươi tư | 44 |
| Bốn mươi tư | 44 |
| bốn mươi bốn | 44 |
| Bốn mươi bốn | 44 |
| Tập bốn mươi tư | Tập 44 |
| bốn mươi ba | 43 |
| Bốn mươi ba | 43 |
| bốn mươi lăm | 45 |
| Bốn mươi lăm | 45 |
| số bốn mươi tư | số 44 |
| Số bốn mươi tư | Số 44 |
| số bốn mươi lăm | số 45 |
| Số bốn mươi lăm | Số 45 |
| hai tấn | 2 tấn |
| Hai tấn | 2 tấn |
| mười tấn | 10 tấn |
| Mười tấn | 10 tấn |
| ba mét | 3 mét |
| Ba mét | 3 mét |
| bốn mét | 4 mét |
| Bốn mét | 4 mét |
| ba trăm triệu | 300 triệu |
| Ba trăm triệu | 300 triệu |
| tám trăm mét | 800 mét |
| Tám trăm mét | 800 mét |
| bốn độ C | 4°C |
| Bốn độ C | 4°C |
| chín mươi chín phần trăm | 99% |
| Chín mươi chín phần trăm | 99% |
| bốn mươi loài | 40 loài |
| Bốn mươi loài | 40 loài |
| ba chấm hai ki-lô-mét một giờ | 3.2 km/h |
| Ba chấm hai ki-lô-mét một giờ | 3.2 km/h |
| hai mươi bốn giờ | 24 giờ |
| Hai mươi bốn giờ | 24 giờ |
| hàng chục triệu năm | hàng chục triệu năm |
| Hàng chục triệu năm | Hàng chục triệu năm |
| hàng trăm triệu | hàng trăm triệu |
| Hàng trăm triệu | Hàng trăm triệu |
| hàng trăm cân | hàng trăm cân |
| Hàng trăm cân | Hàng trăm cân |
| một trăm mét khối | 100 m³ |
| Một trăm mét khối | 100 m³ |
| bảy chấm năm xăng-ti-mét | 7.5 cm |
| Bảy chấm năm xăng-ti-mét | 7.5 cm |
| hai mi-li-mét | 2 mm |
| Hai mi-li-mét | 2 mm |
| sáu mươi triệu lần | 60 triệu lần |
| Sáu mươi triệu lần | 60 triệu lần |
| sáu mươi triệu | 60 triệu |
| Sáu mươi triệu | 60 triệu |
| bốn cân | 4 kg |
| Bốn cân | 4 kg |
| chục cây số | chục cây số |
| không một loài | không 1 loài |
| Không một loài | Không 1 loài |
| không một | không 1 |
| Không một | Không 1 |
| hàng ngàn | hàng 1.000 |
| Hàng ngàn | Hàng 1.000 |
| hàng loạt | hàng loạt |
| Hàng loạt | Hàng loạt |
| triệu năm | triệu năm |
| trăm triệu | trăm triệu |
| một trăm | 100 |
| Một trăm | 100 |
| một không hai | 1 0 2 |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · BỆNH ÁN GÃ KHỔNG LỒ 2 TẤN NGƠ NGÁC NHẤT ĐẠI DƯƠNG · 83.1s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.5 (9.5s) | L01 | Mời bệnh nhân tiếp theo bước vào phòng cấp cứu đa khoa sinh vật biển khơi! Y tá đâu, điều động ngay cho tôi một chiếc cần cẩu công nghiệp tải trọng 10 tấn và một bể nước muối | **10 TẤN** · cần cẩu công nghiệp · R/360 · [0.75, 0.5] | Phòng cấp cứu đa khoa sinh vật biển: bác sĩ cá heo đeo ống nghe và kính viễn vọng, mặc áo blouse trắng hài hước đang sốt sắng chỉ huy hiện trường, bên cạnh là một bể nước mặn khổng lồ bằng kính trong suốt phát sáng bọt khí pastel turquoise. |
| b02 | 00:09.5–00:18.8 (9.3s) | L02 | dung tích 100 m³ khẩn cấp! Bệnh nhân hôm nay của chúng ta là một ca bệnh tâm lý và giải phẫu kỳ quặc bậc nhất hành tinh: Một sinh vật biển nặng tương đương một chiếc xe ô |  | Cận cảnh hiện trường: chiếc cần cẩu công nghiệp màu vàng cam rực rỡ với dây cáp thép to bản đang từ từ hạ dây cáp cẩu xuống để chuẩn bị đón nhận một ca bệnh thể trọng khổng lồ; cô trợ lý hải cẩu đeo tạp dề chữ thập đỏ bưng khay kim tiêm bên cạnh hốt hoảng ôm sổ bệnh án. |
| b03 | 00:18.8–00:27.9 (9.1s) | L03 | tô tải bọc thép, nhưng gương mặt lúc nào cũng đờ đẫn ngơ ngác tựa như không hề có một gợn sóng suy nghĩ nào trong não bộ! Bác sĩ ơi, cái cân điện tử của bệnh viện vừa sập gãy |  | chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim lừng lững xuất hiện trên móc cẩu: Một thân hình tròn dẹt khổng lồ, hai mắt tròn xoe đờ đẫn nhìn vào hư không không chớp mắt. |
| b04 | 00:27.9–00:38.0 (10.0s) | L04 | đôi rồi ạ! Con cá này nó to như cái bánh xe khổng lồ ấy bác ơi! Bệnh nhân mang mã số 44 của chúng ta có tên khoa học là Mola mola, hay còn gọi là Cá Mặt Trăng đại dương! |  | Chiếc bàn cân điện tử công nghiệp bị đè sập gãy đôi xịt khói; cô trợ lý hải cẩu đeo tạp dề chữ thập đỏ bưng khay kim tiêm ôm đầu kinh hãi; chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim vẫn giữ nguyên  |
| b05 | 00:38.0–00:46.6 (8.6s) | L05 | Nhưng tôi thường gọi thân mật ca bệnh khó đỡ này là: Gã khổng lồ vô tri! Trong khi các loài thủy quái biển sâu sở hữu hàm răng sắc nhọn, thân hình thuôn dài khí động học để |  | bác sĩ cá heo đeo ống nghe và kính viễn vọng, mặc áo blouse trắng hài hước cầm tấm bảng chẩn đoán phóng to hồ sơ bệnh án Mola mola; nền là bản đồ đại dương màu lam ngọc pastel với dòng chữ GÃ KHỔNG LỒ VÔ TRI. |
| b06 | 00:46.6–00:57.3 (10.7s) | L06 | săn mồi chớp nhoáng, thì bệnh nhân này lại có một thân hình dẹt tròn lẳn cụt ngủn chẳng khác nào một cái đầu cá khổng lồ bị cắt cụt đuôi đang lềnh bềnh trôi dạt giữa đại dương bao la! |  | So sánh hài hước: BÊN TRÁI là các loài thủy quái biển sâu cơ bắp răng nhọn hoắt khí động học; BÊN PHẢI là chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim tròn lẳn cụt lủn như cái đầu cá bị cắt rời lềnh  |
| b07 | 00:57.3–01:05.6 (8.3s) | L07 | Khám nghiệm thể trọng của gã sẽ khiến bạn phải ngã ngửa: Một con cá mặt trăng trưởng thành có thể đạt chiều dài hơn 3 mét, sải vây từ đỉnh vây lưng xuống vây bụng lên tới 4 mét, |  | Sơ đồ giải phẫu thể trọng: chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim với các mũi tên đo kích thước chiều dài 3 mét và sải vây từ trên xuống dưới 4 mét trên nền giấy can đại dương pastel. |
| b08 | 01:05.6–01:13.8 (8.3s) | L08 | và cân nặng vượt mốc 2 tấn! Đây chính là loài cá có xương thật nặng nhất trên toàn bộ hành tinh Trái Đất! Nhưng nhìn vào đôi mắt tròn xoe vô hồn và chiếc miệng tròn vo lúc nào | **2 TẤN** · thể trọng kỷ lục · R/380 · [0.72, 0.5] | Cận cảnh gương mặt vô tri: Đôi mắt tròn xoe trống rỗng và chiếc miệng tròn vo há hốc ngơ ngác của chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim; vài bong bóng nước lững lờ bay ra. |
| b09 | 01:13.8–01:23.1 (9.3s) | L09 | cũng há hốc ra ngơ ngác, bạn sẽ tự hỏi: Làm thế nào mà một cỗ máy sinh học ngớ ngẩn nhường này lại có thể sinh tồn suốt hàng chục triệu năm qua giữa muôn trùng hiểm nguy của biển cả? |  | chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim thong dong trôi giữa đại dương bao la thời tiền sử, đàn cá cổ đại vây quanh tò mò; bác sĩ cá heo đeo ống nghe và kính viễn vọng, mặc áo blouse trắng hài h |

### scene02 · CẤU TẠO XƯƠNG SỤN KỲ LẠ VÀ THÙY ĐUÔI CLAVUS CỤT NGỦN · 110.0s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.7 (8.7s) | L10 | Hãy đặt tấm phim chụp cắt lớp vi tính toàn thân của Gã khổng lồ vô tri lên màn hình chẩn đoán! Điều đầu tiên khiến toàn thể bác sĩ phẫu thuật phải dụi mắt hoài nghi: Con cá này hoàn toàn |  | Màn hình chẩn đoán chụp cắt lớp CT toàn thân của chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim: Khung xương cá lộ rõ nhưng phần đuôi sau hoàn toàn biến mất; bác sĩ cá heo đeo ống nghe và kính viễn vọn |
| b02 | 00:08.7–00:18.1 (9.4s) | L11 | không có đuôi cá thật sự! Trong giải phẫu học loài cá, chiếc vây đuôi phía sau là động cơ đẩy chính giúp cá tăng tốc rẽ sóng. Nhưng ở cá mặt trăng, xương đuôi và cuống đuôi đã bị teo biến hoàn toàn |  | Mô phỏng 3D cơ sinh học: Con cá ngừ rẽ sóng vùn vụt nhờ vây đuôi cơ bắp; đối diện là chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim không có đuôi chỉ bơi bằng cách lắc lư hai vây đứng. |
| b03 | 00:18.1–00:28.9 (10.8s) | L12 | trong quá trình tiến hóa! Ủa bác sĩ ơi, thế cái rìa thịt lượn sóng phía sau mông của nó là cái gì thế ạ? Cô trợ lý đã phát hiện đúng dị tật độc nhất vô nhị của bệnh nhân! Phần viền thịt nhăn |  | cô trợ lý hải cẩu đeo tạp dề chữ thập đỏ bưng khay kim tiêm cúi người soi kính lúp vào phần rìa thịt lượn sóng phía sau mông của chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim; biểu cảm hoang mang tột  |
| b04 | 00:28.9–00:39.3 (10.4s) | L13 | nheo phía sau đuôi gã được các nhà giải phẫu gọi là thùy clavus! Đây thực chất là phần vây lưng và vây hậu môn bị kéo dài rồi hợp nhất lại thành một chiếc bánh lái thịt cụt lủn! Chiếc bánh lái này hoàn |  | Phóng to cấu tạo giải phẫu thùy clavus: Phần vây lưng và vây phần đuôi hợp nhất thành chiếc bánh lái thịt nhăn nheo như diềm váy búp bê. |
| b05 | 00:39.3–00:49.7 (10.4s) | L14 | toàn không có lực đẩy về phía trước, mà chỉ đóng vai trò như một bánh lái tàu thủy lờ đờ rẽ hướng! Chưa hết đâu nhé, bộ xương của gã khổng lồ 2 tấn này phần lớn không phải là xương cứng đặc |  | Minh họa bánh lái tàu thủy cổ điển gắn sau mông chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim, xoay nhẹ để rẽ hướng lờ đờ giữa làn nước xanh pastel. |
| b06 | 00:49.7–01:00.2 (10.5s) | L15 | như cá chép hay cá ngừ, mà đã thoái hóa thành chất sụn xốp mềm chứa đầy nước, giúp cơ thể gã giảm thiểu tối đa trọng lượng riêng! Đặc biệt hơn nữa, Gã khổng lồ vô tri hoàn toàn không có bong bóng cá! Điều |  | Cắt lớp vi thể xương sụn: Bộ xương của chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim không phải xương cứng mà là những thớ sụn xốp chứa đầy nước; bác sĩ cá heo đeo ống nghe và kính viễn vọng, mặc áo b |
| b07 | 01:00.2–01:09.1 (8.9s) | L16 | này đồng nghĩa với việc gã không thể điều chỉnh độ nổi nhẹ nhàng như các loài cá thông thường. Nhưng tạo hóa đã bù đắp cho gã một cặp động cơ phản lực sinh học thần sầu: Chiếc vây lưng cao vút và |  | Sơ đồ động lực học: chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim không có bong bóng cá nhưng sở hữu hai cánh vây lưng và vây bụng khổng lồ đang quạt nhịp nhàng từ trái qua phải như cánh chim cánh cụt |
| b08 | 01:09.1–01:18.3 (9.2s) | L17 | chiếc vây hậu môn dài ngoằng đập nhịp nhàng từ bên này sang bên kia giống hệt như đôi cánh của loài chim cánh cụt bay lượn dưới nước! Nhóm nghiên cứu của tiến sĩ Watanabe tại Đại học Tokyo đã gắn thẻ |  | Thiết bị định vị GPS gắn trên vây lưng chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim: Đồng hồ đo tốc độ hiển thị kim chỉ vạch ba chấm hai ki-lô-mét một giờ; chú cá mặt trăng hoạt hình khổng lồ hình đĩ |
| b09 | 01:18.3–01:29.1 (10.8s) | L18 | định vị điện tử và phát hiện ra: Gã khổng lồ này có thể bơi với vận tốc 3.2 km/h, hoàn toàn không phải là một khúc gỗ mục trôi dạt vô định như người đời vẫn lầm tưởng! Chưa hết đâu nhé, hãy nhìn | **3.2 KM/H** · vận tốc bơi thực tế · L/360 · [0.28, 0.5] | Tấm kính sinh thiết biểu bì da cá: Lớp da collagen dày cộp bảy chấm năm xăng-ti-mét như lốp xe tăng; bác sĩ cá heo đeo ống nghe và kính viễn vọng, mặc áo blouse trắng hài hước dùng thước kẹp đo độ dày. |
| b10 | 01:29.1–01:40.0 (10.9s) | L19 | vào tấm sinh thiết lớp biểu bì của gã! Cơ thể cá mặt trăng hoàn toàn không có vảy cá thông thường, mà được bọc kín bởi một lớp da collagen dày tới 7.5 cm, dẻo dai tựa như lớp lốp xe tải bọc thép! | **7.5 CM** · độ dày da đệm · R/380 · [0.75, 0.5] | Kính hiển vi điện tử soi bề mặt da: Những chiếc gai vi thể li ti tiết ra màng chất nhờn trong suốt bao bọc cơ thể chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim. |
| b11 | 01:40.0–01:50.0 (10.0s) | L20 | Phía trên bề mặt da phủ đầy những chiếc gai vi thể li ti tiết ra lớp chất nhờn kháng khuẩn trơn tuột, biến cơ thể gã thành một pháo đài đệm thịt êm ái hấp thụ mọi va đập giữa lòng đại dương sóng gió! |  | chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim bơi va vào tảng đá ngầm nhưng lớp da đệm đàn hồi bật nảy ra êm ru; chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt  |

### scene03 · CHẾ ĐỘ ĂN 99% NƯỚC VÀ CHUYẾN LẶN SÂU 800 MÉT · 88.6s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.6 (7.6s) | L21 | Chẩn đoán triệu chứng số ba dẫn chúng ta vào nhà bếp của Gã khổng lồ vô tri! Với thân hình đồ sộ nặng tới 2 tấn, bạn nghĩ thực đơn hằng ngày của gã phải |  | Nhà bếp hải dương: Bàn ăn ngập tràn các đĩa cá ngừ béo ngậy và mực ống thơm lừng, nhưng chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim lắc đầu chê bai; bác sĩ cá heo đeo ống nghe và kính viễn vọng, mặc |
| b02 | 00:07.6–00:16.0 (8.3s) | L22 | là những đàn cá ngừ béo ngậy hay mực ống giàu đạm đúng không? Hoàn toàn sai lầm! Chiếc miệng của cá mặt trăng nhỏ xíu, các răng dính liền lại thành một chiếc mỏ vẹt cứng nhắc không thể |  | Cận cảnh chiếc miệng nhỏ xíu của chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim: Các răng hợp nhất thành chiếc mỏ vẹt cứng nhắc; phía trước là đàn đàn sứa biển hoạt hình trong suốt phát sáng màu hồng p |
| b03 | 00:16.0–00:25.3 (9.3s) | L23 | nhai nghiền con mồi lớn. Và món ăn khoái khẩu duy nhất chiếm tới 99% khẩu phần của gã chính là: Sứa biển! Ai cũng biết sứa biển là một món ăn thảm họa dinh dưỡng: Cơ thể sứa | **99%** · thực đơn sứa biển · R/360 · [0.75, 0.5] | Thực đơn phân tích dinh dưỡng: Chiếc đĩa bày một con sứa trong suốt với nhãn dán thành phần gồm chín mươi chín phần trăm nước muối và một phần trăm thạch gelatin. |
| b04 | 00:25.3–00:34.3 (9.0s) | L24 | chứa tới 99% là nước muối, hàm lượng calo và protein thấp đến mức gần như bằng không! Để nuôi sống cỗ máy sinh học nặng 2 tấn chỉ bằng sứa, Gã khổng lồ vô tri phải làm việc |  | chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim hóa thân thành chiếc máy hút bụi đại dương, há to mỏ hút trọn từng đàn sứa biển trôi nổi như mì sợi vào bụng. |
| b05 | 00:34.3–00:43.4 (9.1s) | L25 | cật lực như một cỗ máy hút bụi đáy đại dương, nuốt chửng hàng trăm cân sứa biển mỗi ngày! Nhưng nuốt một con sứa trơn tuột đầy chất nhầy vào bụng không hề đơn giản chút nào! Hãy |  | bác sĩ cá heo đeo ống nghe và kính viễn vọng, mặc áo blouse trắng hài hước cầm đèn pin soi sâu vào khoang miệng của chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim: Cụm răng họng nhọn hoắt xếp tầng tầng |
| b06 | 00:43.4–00:52.3 (8.9s) | L26 | cầm đèn pin soi sâu vào khoang miệng của bệnh nhân: Toàn bộ phần cuống họng của cá mặt trăng được trang bị những cụm răng họng nhọn hoắt xếp cong về phía sau! Khi gã hút |  | Mô phỏng máy ép ly tâm: Chiếc cuống họng cá co bóp ép kiệt nước biển phun ra hai bên nắp mang, giữ lại mảng thạch sứa đậm đặc đẩy xuống dạ dày. |
| b07 | 00:52.3–01:01.5 (9.2s) | L27 | nước nuốt sứa vào, chiếc cuống họng này hoạt động như một chiếc máy ép nước ly tâm: Răng họng giữ chặt con mồi không cho trôi ngược ra ngoài, đồng thời cơ họng co bóp cực mạnh để |  | chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim lặn thẳng xuống vực sâu thẳm: Ánh sáng mặt trời tắt lịm, đại dương chuyển sang màu tím than sâu thẳm, đồng hồ đo độ sâu chỉ tám trăm mét. |
| b08 | 01:01.5–01:11.0 (9.5s) | L28 | ép kiệt nước biển thừa ra khỏi mang trước khi tống cả tảng thạch sứa đậm đặc vào dạ dày tiêu hóa! Để săn được những con sứa khổng lồ giàu dinh dưỡng, cá mặt trăng phải thực hiện |  | Vùng nước sâu băng giá: Nhiệt kế cắm xuống hiển thị mức nhiệt độ buốt giá bốn độ C; chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim vẫn ung dung đớp những con sứa khổng lồ phát quang sinh học. |
| b09 | 01:11.0–01:20.4 (9.4s) | L29 | những chuyến lặn thám hiểm cực kỳ mạo hiểm: Gã lặn thẳng xuống độ sâu 800 mét dưới đáy biển tăm tối, nơi áp suất nước nghiền nát kim loại và nhiệt độ tụt dốc thê thảm xuống chỉ còn 4°C! | **800 M** · độ sâu lặn săn · L/380 · [0.3, 0.5]<br>**4°C** · nhiệt độ biển sâu · R/360 · [0.75, 0.5] | Lớp mỡ trắng ngà dày dưới da chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim phát sáng hào quang bảo vệ, giữ ấm cho các cơ quan bên trong cơ thể khỏi bị đóng băng. |
| b10 | 01:20.4–01:28.6 (8.2s) | L30 | Nhờ lớp mỡ dày dưới da đóng vai trò như một lớp áo cách nhiệt, gã có thể săn mồi trong vùng nước băng giá suốt hàng giờ liền trước khi cơ thể bị hạ thân nhiệt nguy kịch! |  | chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim no nê vỗ bụng dưới đáy sâu, bắt đầu quạt vây hướng mũi bơi thẳng lên mặt nước tìm kiếm ánh mặt trời. |

### scene04 · HÀNH VI NẰM NGHIÊNG PHƠI NẮNG VÀ KHÁCH SẠN KÝ SINH TRÙNG · 108.0s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:10.2 (10.2s) | L31 | Sau mỗi chuyến lặn sâu 800 mét buốt giá dưới đáy đại dương, Gã khổng lồ vô tri lập tức kích hoạt liệu trình hồi sức cấp cứu độc nhất vô nhị: Gã ngoi thẳng lên mặt biển thoáng, lật nghiêng |  | Mặt biển lấp lánh ánh nắng vàng: chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim ngoi lên mặt nước, lật nghiêng thân mình dẹt hai tấn nằm ngửa phơi bụng đón nắng như đang đi nghỉ dưỡng ở resort. |
| b02 | 00:10.2–00:19.4 (9.3s) | L32 | toàn bộ cơ thể dẹt 2 tấn nằm phơi bụng nổi bồng bềnh trên mặt nước! Dưới ánh nắng mặt trời rực rỡ, bề mặt cơ thể rộng lớn của gã hoạt động tựa như một tấm pin năng lượng mặt trời khổng |  | Cơ thể chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim biến thành tấm pin năng lượng mặt trời thu nhỏ, hấp thụ từng luồng nhiệt ấm áp từ mặt trời để sưởi ấm dòng nước màu lạnh giá. |
| b03 | 00:19.4–00:29.4 (10.0s) | L33 | lồ, hấp thụ nhiệt lượng từ ánh nắng để sưởi ấm lại dòng máu lạnh giá và tái kích hoạt hệ thống tiêu hóa sứa biển! Bác sĩ ơi, trên người con cá này lúc nhúc hàng 1.000 con bọ ghẻ kinh dị |  | cô trợ lý hải cẩu đeo tạp dề chữ thập đỏ bưng khay kim tiêm hoảng hốt chỉ tay vào kính phóng đại: Trên lưng và mang chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim là đàn ký sinh trùng nhiều chân lúc nh |
| b04 | 00:29.4–00:39.3 (9.8s) | L34 | lắm bác ơi! Đây chính là ca bệnh da liễu kinh hoàng nhất lịch sử phòng khám chúng ta! Do tốc độ di chuyển chậm rãi và lớp da nhớt không có vảy cứng, cơ thể cá mặt trăng trở thành một khách |  | Bảng tổng kết da liễu: Hình ảnh bốn mươi loài ký sinh trùng khác nhau từ rận biển, giun tròn đến giáp xác bám đầy thân chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim. |
| b05 | 00:39.3–00:47.5 (8.2s) | L35 | sạn năm sao di động cho hơn 40 loài ký sinh trùng khác nhau bu bám! Có những loài giáp xác ký sinh cắm sâu vào mang, thậm chí ký sinh trùng này lại bị một loài ký sinh trùng khác đẻ | **40 LOÀI** · ký sinh trùng bám da · R/360 · [0.75, 0.5] | Ký sinh lồng ký sinh: Một con rận biển to bám trên da cá, trên lưng con rận lại có một cụm giun biển nhỏ xíu đẻ trứng; bác sĩ cá heo đeo ống nghe và kính viễn vọng, mặc áo blouse trắng hài hước lắc đầu cười trừ. |
| b06 | 00:47.5–00:57.9 (10.4s) | L36 | trứng lên mình! Nhưng Gã khổng lồ vô tri đã giải quyết vấn nạn này bằng một dịch vụ spa ngoài trời vô cùng thông minh! Khi gã nằm nghiêng phơi nắng trên mặt biển, gã phát ra tín hiệu mời gọi các |  | Dịch vụ spa bãi biển mở màn: Đàn cá bướm và cá thiên thần sọc màu pastel rực rỡ bơi quanh chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim, chăm chỉ rỉa từng con rận biển. |
| b07 | 00:57.9–01:07.4 (9.6s) | L37 | bác sĩ làm đẹp tự nhiên: Từng đàn cá bướm và cá thiên thần bơi lại rỉa sạch những con rận biển bám trên da gã. Thậm chí các chú chim mòng biển còn thản nhiên đáp thẳng xuống sườn của chú cá mặt |  | chú chim mòng biển hoạt hình trắng muốt mỏ vàng tinh quái đậu rỉa spa thản nhiên hạ cánh đậu ngay trên má của chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim đang nổi ngửa, dùng mỏ mổ từng con ký sinh t |
| b08 | 01:07.4–01:18.6 (11.2s) | L38 | trăng nổi bồng bềnh, cần mẫn dùng mỏ mổ từng con ký sinh trùng béo ngậy! Một dịch vụ cộng sinh spa miễn phí đỉnh cao giữa bầu trời và biển cả! Đặc biệt hơn nữa, nếu liệu trình spa bằng chim mòng |  | Bức tranh toàn cảnh spa đại dương cộng sinh hài hòa giữa chim mòng biển trên trời, cá rỉa dưới nước và chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim phơi nắng hưởng thụ. |
| b09 | 01:18.6–01:28.4 (9.8s) | L39 | biển vẫn chưa giải quyết dứt điểm những con bọ bám dai dẳng, Gã khổng lồ vô tri sẽ kích hoạt tuyệt chiêu thể dục dưỡng sinh có 1 0 2: Gã lấy đà từ dưới làn nước sâu, quạt hai cánh vây |  | chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim lặn xuống lấy đà dưới làn nước xanh ngắt, quạt vây hết tốc lực chuẩn bị cho một cú nhảy vọt thể thao chấn động. |
| b10 | 01:28.4–01:38.1 (9.7s) | L40 | hết tốc lực rồi phóng vọt cả khối thân nặng 2 tấn bay thẳng lên khỏi mặt biển cao tới 3 mét! Sau đó, gã thả tự do rơi tự do rồi đập cả tấm thân dẹt khổng lồ xuống mặt nước | **3 MÉT** · cú phóng vọt mặt nước · L/380 · [0.28, 0.5] | Cú phóng vọt ngoạn mục: Khối thân hai tấn của chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim bay thẳng lên khỏi mặt biển cao ba mét giữa bầu trời nắng rực; bọt nước bắn tung tóe. |
| b11 | 01:38.1–01:48.0 (9.9s) | L41 | đánh BẸP một tiếng vang dội như một vụ nổ pháo hoa! Cú va chạm bề mặt kinh thiên động địa ấy đủ sức đánh văng hàng loạt loài rận biển cứng đầu ra khỏi da thịt trong sự ngỡ ngàng của giới quan sát! |  | chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim rơi tự do đập bẹp cả tấm thân dẹt xuống mặt biển tạo làn sóng cuộn trào; lũ ký sinh trùng bị chấn động văng tứ tung ra ngoài. |

### scene05 · KỶ LỤC SINH SẢN ĐỈNH CAO BÙ ĐẮP CHỈ SỐ SINH TỒN CỰC THẤP · 89.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.2 (8.2s) | L42 | Chẩn đoán y khoa cuối cùng giải mã lý do tại sao một sinh vật ngơ ngác, chậm chạp và không hề có vũ khí tự vệ lại không bị tuyệt chủng khỏi Trái Đất! Các thủy thủ viễn |  | chú hải cẩu xám béo tròn đang ngoạm cắn đuôi cá mặt trăng hung hăng lao tới cắn rách một mảng vây của chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim; chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn d |
| b02 | 00:08.2–00:16.3 (8.2s) | L43 | dương thường xuyên chứng kiến những cảnh tượng đau lòng: Khi bị hải cẩu hay sư tử biển tấn công, hải cẩu cắn đứt từng mảng vây của cá mặt trăng rồi xé toang lớp da, nhưng Gã khổng lồ |  | bác sĩ cá heo đeo ống nghe và kính viễn vọng, mặc áo blouse trắng hài hước và cô trợ lý hải cẩu đeo tạp dề chữ thập đỏ bưng khay kim tiêm ôm mặt xót xa trước cảnh tượng; trên màn hình hiển thị biểu đồ chỉ số tự vệ và phản xạ trốn chạy của chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc n |
| b03 | 00:16.3–00:25.3 (9.0s) | L44 | vô tri vẫn chỉ trơ mắt nhìn trời với vẻ mặt bình thản không chút hoảng loạn! Gã hoàn toàn không có phản xạ tự vệ hay tấn công đáp trả! Với tỷ lệ bị săn bắt tàn khốc như vậy, |  | Đại dương mênh mông bừng sáng: chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim mẹ phóng thích một đám mây trứng khổng lồ phát sáng lấp lánh như dải ngân hà dưới làn nước biển. |
| b04 | 00:25.3–00:33.8 (8.5s) | L45 | chỉ một trong số hàng trăm triệu cá con có thể sống sót đến tuổi trưởng thành. Nhưng tạo hóa đã ban tặng cho bệnh nhân này một cỗ máy sinh sản vô địch thiên hạ: Trong mỗi mùa sinh sản, |  | Bảng kỷ lục Guinness đại dương: Dòng chữ ba trăm triệu quả trứng vàng son rực rỡ; chiếc cúp vô địch sinh sản động vật có xương sống đặt cạnh chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim. |
| b05 | 00:33.8–00:41.8 (8.0s) | L46 | một con cá mặt trăng cái có thể phóng thích tới 300 triệu quả trứng vào làn nước biển! Đây là một kỷ lục vô tiền khoáng hậu, không 1 loài động vật có xương sống nào trên Trái | **300 TRIỆU** · kỷ lục sinh sản trứng · R/360 · [0.75, 0.5] | Bức ảnh siêu âm ấu trùng: chú ấu trùng cá mặt trăng tí hon tròn xoe như quả cầu gai phi thuyền ngoài hành tinh bé tí xíu chỉ dài hai mi-li-mét, nhỏ hơn hạt vừng đặt cạnh chiếc kim may áo của bác sĩ cá heo đeo ống nghe và kính viễn vọng, mặc áo blouse trắng hài hước. |
| b06 | 00:41.8–00:52.1 (10.3s) | L47 | Đất có thể so bì! Hãy nhìn vào bức ảnh siêu âm ấu trùng của bệnh nhân: Chú cá con lúc mới chui ra khỏi vỏ trứng chỉ dài vỏn vẹn 2 mm, nhỏ hơn cả đầu tăm nhưng lại mang | **2 MM** · kích thước ấu trùng · L/380 · [0.28, 0.5] | Phóng to chú ấu trùng cá mặt trăng tí hon tròn xoe như quả cầu gai phi thuyền ngoài hành tinh: Tròn ung ủng với hàng chục chiếc gai nhọn hoắt chìa ra xung quanh như một phi thuyền ngoài hành tinh mini dễ thương. |
| b07 | 00:52.1–01:00.7 (8.7s) | L48 | một ngoại hình cực kỳ tấu hài: Toàn thân chú cá con tròn ủng như một quả cầu gai, xung quanh mọc chìa ra hàng chục chiếc gai nhọn hoắt trông hệt như một chiếc phi thuyền người ngoài hành tinh |  | Đàn ấu trùng phi thuyền tí hon bơi lăng quăng giữa các loài sinh vật phù du, những chiếc gai nhọn giúp xua đuổi các loài tôm tép ăn thịt. |
| b08 | 01:00.7–01:10.8 (10.1s) | L49 | tí hon! Chiếc áo giáp gai nhọn ấy giúp ấu trùng trôi nổi như sinh vật phù du và bảo vệ chúng khỏi miệng những kẻ săn mồi tí hon dưới đáy biển sâu! Kỳ diệu hơn nữa, những chú |  | Biểu đồ tiến hóa tăng trưởng thể trọng: Từ ấu trùng 2mm rụng dần gai, lớn dần thành cá nhỏ rồi hóa thành gã khổng lồ hai tấn; mũi tên tăng trưởng gấp sáu mươi triệu lần. |
| b09 | 01:10.8–01:20.4 (9.5s) | L50 | cá mặt trăng sơ sinh vừa nở ra chỉ dài vỏn vẹn 2 mm, nhỏ hơn cả một hạt vừng và được bao bọc bởi những chiếc gai nhọn hoắt như một chú cá nóc mini! Từ kích thước 2 mm |  | chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim trưởng thành bơi bên cạnh đàn con tí hon; sự tương phản kích thước vĩ đại và kỳ diệu nhất của giới sinh vật biển. |
| b10 | 01:20.4–01:29.9 (9.5s) | L51 | bé tí xíu ấy, cá con phải tăng trưởng khối lượng gấp 60 triệu lần để trở thành một gã khổng lồ nặng 2 tấn! Một bước nhảy vọt thể trọng vĩ đại nhất trong toàn bộ thế giới sinh vật biển! | **X60 TRIỆU** · tăng trưởng thể trọng · R/360 · [0.75, 0.5] | bác sĩ cá heo đeo ống nghe và kính viễn vọng, mặc áo blouse trắng hài hước đặt bút ký con dấu ĐÃ KIỂM ĐỊNH vào hồ sơ sinh sản của bệnh nhân với nụ cười khâm phục. |

### scene06 · ĐƠN THUỐC TIẾN HÓA VÀ THỬ THÁCH ĐOÁN TẬP 45 · 55.3s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.6 (7.6s) | L52 | Hồ sơ bệnh án số 44 chính thức khép lại với kết luận chẩn đoán: Cá Mặt Trăng hoàn toàn khỏe mạnh và là một bài học sinh tồn triết lý sâu sắc |  | bác sĩ cá heo đeo ống nghe và kính viễn vọng, mặc áo blouse trắng hài hước đóng hồ sơ bệnh án số bốn mươi tư, mỉm cười gật gù; phía sau là bức tranh phong cảnh đại dương pastel tuyệt đẹp với chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi c |
| b02 | 00:07.6–00:15.4 (7.8s) | L53 | của mẹ thiên nhiên! Đôi khi trong cuộc sống, bạn không cần phải quá bon chen ganh đua, không cần phải trang bị móng vuốt nanh nhọn để gầm gừ đe dọa người khác. Gã khổng |  | Triết lý sống vô tri: chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim trôi nhẹ nhàng giữa biển cả sóng gió, ánh nắng ấm áp chiếu rọi gương mặt an yên không màng danh lợi. |
| b03 | 00:15.4–00:23.0 (7.6s) | L54 | lồ vô tri dạy chúng ta rằng: Cứ bình thản sống, cứ mở lòng phơi nắng đón nhận những điều tươi đẹp, và kiên trì mở lối đi riêng, đại dương bao la sẽ luôn dành |  | Màn hình tương tác người xem: Hai chiếc nút lựa chọn đồ họa pastel hài hước: Nút 1 là đầu cá hai tấn vô tư phơi nắng, Nút 2 là cỗ máy đẻ 300 triệu trứng. |
| b04 | 00:23.0–00:31.3 (8.3s) | L55 | cho bạn một chỗ đứng vững vàng! Nếu được sinh ra với một đặc tính của loài cá mặt trăng, bạn muốn sở hữu chiếc đầu khổng lồ 2 tấn vô tư phơi nắng hay cỗ |  | cô trợ lý hải cẩu đeo tạp dề chữ thập đỏ bưng khay kim tiêm giơ biển chỉ dẫn mời người xem để lại bình luận chẩn đoán bên dưới video. |
| b05 | 00:31.3–00:39.4 (8.1s) | L56 | máy sinh sản 300 triệu quả trứng? Hãy để lại bình luận chẩn đoán của bạn bên dưới nhé! Còn bây giờ, hãy chuẩn bị bước vào bản tin hiện trường trực tiếp của hồ |  | Hồ sơ mật tập 45 hé lộ: Một chú vẹt béo múp lông xanh rêu đang đứng đơ như bụi cây giữa khu rừng rậm New Zealand sương mù huyền ảo. |
| b06 | 00:39.4–00:47.8 (8.3s) | L57 | sơ số 45! Một chú vẹt béo múp 4 kg đến từ New Zealand, loài vẹt duy nhất trên thế giới đã hoàn toàn quên mất cách bay, đêm đêm đi bộ cả chục cây số, và |  | Chú vẹt béo trèo lên cành cây cao rồi nhảy ùm xuống đất đập mặt ngơ ngác hài hước; các dấu hỏi chấm xoay quanh đầu chú vẹt. |
| b07 | 00:47.8–00:55.3 (7.5s) | L58 | thỉnh thoảng lại thích trèo lên ngọn cây cao rồi nhảy ùm xuống đất đập mặt ngơ ngác! Bạn có biết phóng sự điều tra này sẽ đưa chúng ta gặp gỡ chú vẹt nào không? |  | Màn hình kết thúc: Dòng chữ HẸN GẶP LẠI Ở TẬP 45 VẸT KAKAPO lung linh với lời kêu gọi đăng ký kênh và ấn chuông theo dõi. |

## 5. Phân cảnh Shorts — từng beat

Banner: **NẶNG 2 TẤN VÔ TRI / BỊ CẮN VẪN PHƠI NẮNG?!** · giọng 40.9s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Nặng tới 2 tấn nhưng hiền đến mức bị hải cẩu bơi lại cắn đứt từng mảng vây nó cũng | **2 TẤN** · gã khổng lồ · L/500 · [0.3, 0.5] |
| s02 | 00:05.0 | S02 | chỉ nằm ngửa nhìn trời ngơ ngác! Đây là Cá Mặt Trăng, gã khổng lồ vô tri nặng nhất thế giới |  |
| s03 | 00:09.8 | S03 | loài cá có xương! To xác như chiếc ô tô tải nhưng gã hoàn toàn không có đuôi cá thật sự, |  |
| s04 | 00:14.8 | S04 | cơ thể cụt lủn chỉ có cái đầu tròn xoe bơi bằng hai cánh vây khổng lồ. Món ăn khoái khẩu của |  |
| s05 | 00:19.9 | S05 | gã là sứa biển chứa 99% nước, nên gã phải ăn cả tạ sứa mỗi ngày và lặn sâu 800 mét dưới |  |
| s06 | 00:25.4 | S06 | cái lạnh 4°C. Sau mỗi chuyến lặn buốt giá, gã ngoi lên mặt nước nằm nghiêng phơi nắng để sưởi |  |
| s07 | 00:30.5 | S07 | ấm dòng máu lạnh và cho chim mòng biển rỉa sạch ký sinh trùng. Đổi lại sự ngơ ngác ấy, cá |  |
| s08 | 00:35.6 | S08 | mẹ đẻ tới 300 triệu quả trứng mỗi lần, một kỷ lục vô địch tuyệt đối trong giới động vật có xương sống! | **300 TRIỆU** · kỷ lục sinh sản · R/520 · [0.7, 0.5] |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mời bệnh nhân tiếp theo bước vào phòng cấp cứu đa khoa sinh vật biển khơi! Y tá đâu, điều động ngay cho tôi một chiếc cần cẩu công nghiệp tải trọng 10 tấn và một bể nước muối dung". Bố cục: Phòng cấp cứu đa khoa sinh vật biển: bác sĩ cá heo đeo ống nghe và kính viễn vọng, mặc áo blouse trắng hài hước đang sốt sắng chỉ huy hiện trường, bên cạnh là một bể nước mặn khổng lồ bằng kính trong suốt phát sáng bọt khí pastel turquoise.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tích 100 m³ khẩn cấp! Bệnh nhân hôm nay của chúng ta là một ca bệnh tâm lý và giải phẫu kỳ quặc bậc nhất hành tinh: Một sinh vật biển nặng tương đương một chiếc xe ô tô tải". Bố cục: Cận cảnh hiện trường: chiếc cần cẩu công nghiệp màu vàng cam rực rỡ với dây cáp thép to bản đang từ từ hạ dây cáp cẩu xuống để chuẩn bị đón nhận một ca bệnh thể trọng khổng lồ; cô trợ lý hải cẩu đeo tạp dề chữ thập đỏ bưng khay kim tiêm bên cạnh hốt hoảng ôm sổ bệnh án.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bọc thép, nhưng gương mặt lúc nào cũng đờ đẫn ngơ ngác tựa như không hề có một gợn sóng suy nghĩ nào trong não bộ! Bác sĩ ơi, cái cân điện tử của bệnh viện vừa sập gãy đôi rồi". Bố cục: chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim lừng lững xuất hiện trên móc cẩu: Một thân hình tròn dẹt khổng lồ, hai mắt tròn xoe đờ đẫn nhìn vào hư không không chớp mắt.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "ạ! Con cá này nó to như cái bánh xe khổng lồ ấy bác ơi! Bệnh nhân mang mã số 44 của chúng ta có tên khoa học là Mola mola, hay còn gọi là Cá Mặt Trăng đại dương!". Bố cục: Chiếc bàn cân điện tử công nghiệp bị đè sập gãy đôi xịt khói; cô trợ lý hải cẩu đeo tạp dề chữ thập đỏ bưng khay kim tiêm ôm đầu kinh hãi; chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim vẫn giữ nguyên nụ cười ngây ngô vô số tội.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng tôi thường gọi thân mật ca bệnh khó đỡ này là: Gã khổng lồ vô tri! Trong khi các loài thủy quái biển sâu sở hữu hàm răng sắc nhọn, thân hình thuôn dài khí động học để săn". Bố cục: bác sĩ cá heo đeo ống nghe và kính viễn vọng, mặc áo blouse trắng hài hước cầm tấm bảng chẩn đoán phóng to hồ sơ bệnh án Mola mola; nền là bản đồ đại dương màu lam ngọc pastel với dòng chữ GÃ KHỔNG LỒ VÔ TRI.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "mồi chớp nhoáng, thì bệnh nhân này lại có một thân hình dẹt tròn lẳn cụt ngủn chẳng khác nào một cái đầu cá khổng lồ bị cắt cụt đuôi đang lềnh bềnh trôi dạt giữa đại dương bao la! Khám". Bố cục: So sánh hài hước: BÊN TRÁI là các loài thủy quái biển sâu cơ bắp răng nhọn hoắt khí động học; BÊN PHẢI là chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim tròn lẳn cụt lủn như cái đầu cá bị cắt rời lềnh bềnh trôi nước.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nghiệm thể trọng của gã sẽ khiến bạn phải ngã ngửa: Một con cá mặt trăng trưởng thành có thể đạt chiều dài hơn 3 mét, sải vây từ đỉnh vây lưng xuống vây bụng lên tới 4 mét, và". Bố cục: Sơ đồ giải phẫu thể trọng: chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim với các mũi tên đo kích thước chiều dài 3 mét và sải vây từ trên xuống dưới 4 mét trên nền giấy can đại dương pastel.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "cân nặng vượt mốc 2 tấn! Đây chính là loài cá có xương thật nặng nhất trên toàn bộ hành tinh Trái Đất! Nhưng nhìn vào đôi mắt tròn xoe vô hồn và chiếc miệng tròn vo lúc nào cũng". Bố cục: Cận cảnh gương mặt vô tri: Đôi mắt tròn xoe trống rỗng và chiếc miệng tròn vo há hốc ngơ ngác của chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim; vài bong bóng nước lững lờ bay ra.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "há hốc ra ngơ ngác, bạn sẽ tự hỏi: Làm thế nào mà một cỗ máy sinh học ngớ ngẩn nhường này lại có thể sinh tồn suốt hàng chục triệu năm qua giữa muôn trùng hiểm nguy của biển cả?". Bố cục: chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim thong dong trôi giữa đại dương bao la thời tiền sử, đàn cá cổ đại vây quanh tò mò; bác sĩ cá heo đeo ống nghe và kính viễn vọng, mặc áo blouse trắng hài hước giơ kính lúp nghiên cứu thắc mắc.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy đặt tấm phim chụp cắt lớp vi tính toàn thân của Gã khổng lồ vô tri lên màn hình chẩn đoán! Điều đầu tiên khiến toàn thể bác sĩ phẫu thuật phải dụi mắt hoài nghi: Con cá này hoàn toàn không có". Bố cục: Màn hình chẩn đoán chụp cắt lớp CT toàn thân của chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim: Khung xương cá lộ rõ nhưng phần đuôi sau hoàn toàn biến mất; bác sĩ cá heo đeo ống nghe và kính viễn vọng, mặc áo blouse trắng hài hước chỉ tay phân tích.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "đuôi cá thật sự! Trong giải phẫu học loài cá, chiếc vây đuôi phía sau là động cơ đẩy chính giúp cá tăng tốc rẽ sóng. Nhưng ở cá mặt trăng, xương đuôi và cuống đuôi đã bị teo biến hoàn toàn trong quá". Bố cục: Mô phỏng 3D cơ sinh học: Con cá ngừ rẽ sóng vùn vụt nhờ vây đuôi cơ bắp; đối diện là chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim không có đuôi chỉ bơi bằng cách lắc lư hai vây đứng.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "trình tiến hóa! Ủa bác sĩ ơi, thế cái rìa thịt lượn sóng phía sau mông của nó là cái gì thế ạ? Cô trợ lý đã phát hiện đúng dị tật độc nhất vô nhị của bệnh nhân! Phần viền thịt nhăn nheo phía". Bố cục: cô trợ lý hải cẩu đeo tạp dề chữ thập đỏ bưng khay kim tiêm cúi người soi kính lúp vào phần rìa thịt lượn sóng phía sau mông của chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim; biểu cảm hoang mang tột độ.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "sau đuôi gã được các nhà giải phẫu gọi là thùy clavus! Đây thực chất là phần vây lưng và vây phần đuôi bị kéo dài rồi hợp nhất lại thành một chiếc bánh lái thịt cụt lủn! Chiếc bánh lái này hoàn toàn". Bố cục: Phóng to cấu tạo giải phẫu thùy clavus: Phần vây lưng và vây phần đuôi hợp nhất thành chiếc bánh lái thịt nhăn nheo như diềm váy búp bê.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "không có lực đẩy về phía trước, mà chỉ đóng vai trò như một bánh lái tàu thủy lờ đờ rẽ hướng! Chưa hết đâu nhé, bộ xương của gã khổng lồ 2 tấn này phần lớn không phải là xương cứng đặc như cá". Bố cục: Minh họa bánh lái tàu thủy cổ điển gắn sau mông chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim, xoay nhẹ để rẽ hướng lờ đờ giữa làn nước xanh pastel.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chép hay cá ngừ, mà đã thoái hóa thành chất sụn xốp mềm chứa đầy nước, giúp cơ thể gã giảm thiểu tối đa trọng lượng riêng! Đặc biệt hơn nữa, Gã khổng lồ vô tri hoàn toàn không có bong bóng cá! Điều". Bố cục: Cắt lớp vi thể xương sụn: Bộ xương của chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim không phải xương cứng mà là những thớ sụn xốp chứa đầy nước; bác sĩ cá heo đeo ống nghe và kính viễn vọng, mặc áo blouse trắng hài hước dùng ngón tay ấn thử thấy đàn hồi như thạch.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "này đồng nghĩa với việc gã không thể điều chỉnh độ nổi nhẹ nhàng như các loài cá thông thường. Nhưng tạo hóa đã bù đắp cho gã một cặp động cơ phản lực sinh học thần sầu: Chiếc vây lưng cao vút và chiếc". Bố cục: Sơ đồ động lực học: chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim không có bong bóng cá nhưng sở hữu hai cánh vây lưng và vây bụng khổng lồ đang quạt nhịp nhàng từ trái qua phải như cánh chim cánh cụt bay lượn.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "vây phần đuôi dài ngoằng đập nhịp nhàng từ bên này sang bên kia giống hệt như đôi cánh của loài chim cánh cụt bay lượn dưới nước! Nhóm nghiên cứu của tiến sĩ Watanabe tại Đại học Tokyo đã gắn thẻ định vị". Bố cục: Thiết bị định vị GPS gắn trên vây lưng chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim: Đồng hồ đo tốc độ hiển thị kim chỉ vạch ba chấm hai ki-lô-mét một giờ; chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim lướt đi nhẹ nhàng thanh thoát.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "điện tử và phát hiện ra: Gã khổng lồ này có thể bơi với vận tốc 3.2 km/h, hoàn toàn không phải là một khúc gỗ mục trôi dạt vô định như người đời vẫn lầm tưởng! Chưa hết đâu nhé, hãy nhìn vào tấm". Bố cục: Tấm kính sinh thiết biểu bì da cá: Lớp da collagen dày cộp bảy chấm năm xăng-ti-mét như lốp xe tăng; bác sĩ cá heo đeo ống nghe và kính viễn vọng, mặc áo blouse trắng hài hước dùng thước kẹp đo độ dày.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "sinh thiết lớp biểu bì của gã! Cơ thể cá mặt trăng hoàn toàn không có vảy cá thông thường, mà được bọc kín bởi một lớp da collagen dày tới 7.5 cm, dẻo dai tựa như lớp lốp xe tải bọc thép! Phía". Bố cục: Kính hiển vi điện tử soi bề mặt da: Những chiếc gai vi thể li ti tiết ra màng chất nhờn trong suốt bao bọc cơ thể chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "trên bề mặt da phủ đầy những chiếc gai vi thể li ti tiết ra lớp chất nhờn kháng khuẩn trơn tuột, biến cơ thể gã thành một pháo đài đệm thịt êm ái hấp thụ mọi va đập giữa lòng đại dương sóng gió!". Bố cục: chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim bơi va vào tảng đá ngầm nhưng lớp da đệm đàn hồi bật nảy ra êm ru; chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim vẫn giữ nguyên ánh mắt vô tri cười toe toét.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chẩn đoán triệu chứng số ba dẫn chúng ta vào nhà bếp của Gã khổng lồ vô tri! Với thân hình đồ sộ nặng tới 2 tấn, bạn nghĩ thực đơn hằng ngày của gã phải là những". Bố cục: Nhà bếp hải dương: Bàn ăn ngập tràn các đĩa cá ngừ béo ngậy và mực ống thơm lừng, nhưng chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim lắc đầu chê bai; bác sĩ cá heo đeo ống nghe và kính viễn vọng, mặc áo blouse trắng hài hước đứng cạnh ngạc nhiên.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "đàn cá ngừ béo ngậy hay mực ống giàu đạm đúng không? Hoàn toàn sai lầm! Chiếc miệng của cá mặt trăng nhỏ xíu, các răng dính liền lại thành một chiếc mỏ vẹt cứng nhắc không thể nhai". Bố cục: Cận cảnh chiếc miệng nhỏ xíu của chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim: Các răng hợp nhất thành chiếc mỏ vẹt cứng nhắc; phía trước là đàn đàn sứa biển hoạt hình trong suốt phát sáng màu hồng pastel và tím nhạt trôi bồng bềnh trôi lững lờ.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nghiền con mồi lớn. Và món ăn khoái khẩu duy nhất chiếm tới 99% khẩu phần của gã chính là: Sứa biển! Ai cũng biết sứa biển là một món ăn thảm họa dinh dưỡng: Cơ thể sứa chứa". Bố cục: Thực đơn phân tích dinh dưỡng: Chiếc đĩa bày một con sứa trong suốt với nhãn dán thành phần gồm chín mươi chín phần trăm nước muối và một phần trăm thạch gelatin.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tới 99% là nước muối, hàm lượng calo và protein thấp đến mức gần như bằng không! Để nuôi sống cỗ máy sinh học nặng 2 tấn chỉ bằng sứa, Gã khổng lồ vô tri phải làm việc cật". Bố cục: chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim hóa thân thành chiếc máy hút bụi đại dương, há to mỏ hút trọn từng đàn sứa biển trôi nổi như mì sợi vào bụng.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "lực như một cỗ máy hút bụi đáy đại dương, nuốt chửng hàng trăm cân sứa biển mỗi ngày! Nhưng nuốt một con sứa trơn tuột đầy chất nhầy vào bụng không hề đơn giản chút nào! Hãy cầm". Bố cục: bác sĩ cá heo đeo ống nghe và kính viễn vọng, mặc áo blouse trắng hài hước cầm đèn pin soi sâu vào khoang miệng của chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim: Cụm răng họng nhọn hoắt xếp tầng tầng lớp lớp hướng cong vào trong như chiếc bẫy gai.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "đèn pin soi sâu vào khoang miệng của bệnh nhân: Toàn bộ phần cuống họng của cá mặt trăng được trang bị những cụm răng họng nhọn hoắt xếp cong về phía sau! Khi gã hút nước nuốt". Bố cục: Mô phỏng máy ép ly tâm: Chiếc cuống họng cá co bóp ép kiệt nước biển phun ra hai bên nắp mang, giữ lại mảng thạch sứa đậm đặc đẩy xuống dạ dày.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "sứa vào, chiếc cuống họng này hoạt động như một chiếc máy ép nước ly tâm: Răng họng giữ chặt con mồi không cho trôi ngược ra ngoài, đồng thời cơ họng co bóp cực mạnh để ép kiệt". Bố cục: chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim lặn thẳng xuống vực sâu thẳm: Ánh sáng mặt trời tắt lịm, đại dương chuyển sang màu tím than sâu thẳm, đồng hồ đo độ sâu chỉ tám trăm mét.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nước biển thừa ra khỏi mang trước khi tống cả tảng thạch sứa đậm đặc vào dạ dày tiêu hóa! Để săn được những con sứa khổng lồ giàu dinh dưỡng, cá mặt trăng phải thực hiện những chuyến". Bố cục: Vùng nước sâu băng giá: Nhiệt kế cắm xuống hiển thị mức nhiệt độ buốt giá bốn độ C; chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim vẫn ung dung đớp những con sứa khổng lồ phát quang sinh học.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "lặn thám hiểm cực kỳ mạo hiểm: Gã lặn thẳng xuống độ sâu 800 mét dưới đáy biển tăm tối, nơi áp suất nước nghiền nát kim loại và nhiệt độ tụt dốc thê thảm xuống chỉ còn 4°C!". Bố cục: Lớp mỡ trắng ngà dày dưới da chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim phát sáng hào quang bảo vệ, giữ ấm cho các cơ quan bên trong cơ thể khỏi bị đóng băng.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhờ lớp mỡ dày dưới da đóng vai trò như một lớp áo cách nhiệt, gã có thể săn mồi trong vùng nước băng giá suốt hàng giờ liền trước khi cơ thể bị hạ thân nhiệt nguy kịch!". Bố cục: chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim no nê vỗ bụng dưới đáy sâu, bắt đầu quạt vây hướng mũi bơi thẳng lên mặt nước tìm kiếm ánh mặt trời.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sau mỗi chuyến lặn sâu 800 mét buốt giá dưới đáy đại dương, Gã khổng lồ vô tri lập tức kích hoạt liệu trình hồi sức cấp cứu độc nhất vô nhị: Gã ngoi thẳng lên mặt biển thoáng, lật nghiêng toàn". Bố cục: Mặt biển lấp lánh ánh nắng vàng: chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim ngoi lên mặt nước, lật nghiêng thân mình dẹt hai tấn nằm ngửa phơi bụng đón nắng như đang đi nghỉ dưỡng ở resort.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bộ cơ thể dẹt 2 tấn nằm phơi bụng nổi bồng bềnh trên mặt nước! Dưới ánh nắng mặt trời rực rỡ, bề mặt cơ thể rộng lớn của gã hoạt động tựa như một tấm pin năng lượng mặt trời khổng lồ,". Bố cục: Cơ thể chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim biến thành tấm pin năng lượng mặt trời thu nhỏ, hấp thụ từng luồng nhiệt ấm áp từ mặt trời để sưởi ấm dòng nước màu lạnh giá.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "hấp thụ nhiệt lượng từ ánh nắng để sưởi ấm lại dòng nước màu lạnh giá và tái kích hoạt hệ thống tiêu hóa sứa biển! Bác sĩ ơi, trên người con cá này lúc nhúc hàng 1.000 con bọ ghẻ kinh dị lắm". Bố cục: cô trợ lý hải cẩu đeo tạp dề chữ thập đỏ bưng khay kim tiêm hoảng hốt chỉ tay vào kính phóng đại: Trên lưng và mang chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim là đàn ký sinh trùng nhiều chân lúc nhúc bò lổm ngổm.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bác ơi! Đây chính là ca bệnh da liễu kinh hoàng nhất lịch sử phòng khám chúng ta! Do tốc độ di chuyển chậm rãi và lớp da nhớt không có vảy cứng, cơ thể cá mặt trăng trở thành một khách sạn". Bố cục: Bảng tổng kết da liễu: Hình ảnh bốn mươi loài ký sinh trùng khác nhau từ rận biển, giun tròn đến giáp xác bám đầy thân chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "năm sao di động cho hơn 40 loài ký sinh trùng khác nhau bu bám! Có những loài giáp xác ký sinh cắm sâu vào mang, thậm chí ký sinh trùng này lại bị một loài ký sinh trùng khác đẻ trứng lên". Bố cục: Ký sinh lồng ký sinh: Một con rận biển to bám trên da cá, trên lưng con rận lại có một cụm giun biển nhỏ xíu đẻ trứng; bác sĩ cá heo đeo ống nghe và kính viễn vọng, mặc áo blouse trắng hài hước lắc đầu cười trừ.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "mình! Nhưng Gã khổng lồ vô tri đã giải quyết vấn nạn này bằng một dịch vụ spa ngoài trời vô cùng thông minh! Khi gã nằm nghiêng phơi nắng trên mặt biển, gã phát ra tín hiệu mời gọi các bác sĩ". Bố cục: Dịch vụ spa bãi biển mở màn: Đàn cá bướm và cá thiên thần sọc màu pastel rực rỡ bơi quanh chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim, chăm chỉ rỉa từng con rận biển.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "làm đẹp tự nhiên: Từng đàn cá bướm và cá thiên thần bơi lại rỉa sạch những con rận biển bám trên da gã. Thậm chí các chú chim mòng biển còn thản nhiên đáp thẳng xuống sườn của chú cá mặt trăng". Bố cục: chú chim mòng biển hoạt hình trắng muốt mỏ vàng tinh quái đậu rỉa spa thản nhiên hạ cánh đậu ngay trên má của chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim đang nổi ngửa, dùng mỏ mổ từng con ký sinh trùng béo mầm; chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim lim dim tận hưởng.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nổi bồng bềnh, cần mẫn dùng mỏ mổ từng con ký sinh trùng béo ngậy! Một dịch vụ cộng sinh spa miễn phí đỉnh cao giữa bầu trời và biển cả! Đặc biệt hơn nữa, nếu liệu trình spa bằng chim mòng biển". Bố cục: Bức tranh toàn cảnh spa đại dương cộng sinh hài hòa giữa chim mòng biển trên trời, cá rỉa dưới nước và chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim phơi nắng hưởng thụ.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "vẫn chưa giải quyết dứt điểm những con bọ bám dai dẳng, Gã khổng lồ vô tri sẽ kích hoạt tuyệt chiêu thể dục dưỡng sinh có 1 0 2: Gã lấy đà từ dưới làn nước sâu, quạt hai cánh vây hết". Bố cục: chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim lặn xuống lấy đà dưới làn nước xanh ngắt, quạt vây hết tốc lực chuẩn bị cho một cú nhảy vọt thể thao chấn động.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tốc lực rồi phóng vọt cả khối thân nặng 2 tấn bay thẳng lên khỏi mặt biển cao tới 3 mét! Sau đó, gã thả tự do rơi tự do rồi đập cả tấm thân dẹt khổng lồ xuống mặt nước đánh BẸP". Bố cục: Cú phóng vọt ngoạn mục: Khối thân hai tấn của chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim bay thẳng lên khỏi mặt biển cao ba mét giữa bầu trời nắng rực; bọt nước bắn tung tóe.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "một tiếng vang dội như một vụ nổ pháo hoa! Cú va chạm bề mặt kinh thiên động địa ấy đủ sức đánh văng hàng loạt loài rận biển cứng đầu ra khỏi da thịt trong sự ngỡ ngàng của giới quan sát!". Bố cục: chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim rơi tự do đập bẹp cả tấm thân dẹt xuống mặt biển tạo làn sóng cuộn trào; lũ ký sinh trùng bị chấn động văng tứ tung ra ngoài.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chẩn đoán y khoa cuối cùng giải mã lý do tại sao một sinh vật ngơ ngác, chậm chạp và không hề có vũ khí tự vệ lại không bị tuyệt chủng khỏi Trái Đất! Các thủy thủ viễn dương". Bố cục: chú hải cẩu xám béo tròn đang ngoạm cắn đuôi cá mặt trăng hung hăng lao tới cắn rách một mảng vây của chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim; chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim bị cắn nhưng gương mặt vẫn đờ đẫn mỉm cười nhìn lên bầu trời không chút phản xạ sợ hãi.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "thường xuyên chứng kiến những cảnh tượng đau lòng: Khi bị hải cẩu hay sư tử biển tấn công, hải cẩu cắn đứt từng mảng vây của cá mặt trăng rồi xé toang lớp da, nhưng Gã khổng lồ vô tri". Bố cục: bác sĩ cá heo đeo ống nghe và kính viễn vọng, mặc áo blouse trắng hài hước và cô trợ lý hải cẩu đeo tạp dề chữ thập đỏ bưng khay kim tiêm ôm mặt xót xa trước cảnh tượng; trên màn hình hiển thị biểu đồ chỉ số tự vệ và phản xạ trốn chạy của chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim ở mức số không tròn trĩnh.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "vẫn chỉ trơ mắt nhìn trời với vẻ mặt bình thản không chút hoảng loạn! Gã hoàn toàn không có phản xạ tự vệ hay tấn công đáp trả! Với tỷ lệ bị săn bắt tàn khốc như vậy, chỉ". Bố cục: Đại dương mênh mông bừng sáng: chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim mẹ phóng thích một đám mây trứng khổng lồ phát sáng lấp lánh như dải ngân hà dưới làn nước biển.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "một trong số hàng trăm triệu cá con có thể sống sót đến tuổi trưởng thành. Nhưng tạo hóa đã ban tặng cho bệnh nhân này một cỗ máy sinh sản vô địch thiên hạ: Trong mỗi mùa sinh sản, một". Bố cục: Bảng kỷ lục Guinness đại dương: Dòng chữ ba trăm triệu quả trứng vàng son rực rỡ; chiếc cúp vô địch sinh sản động vật có xương sống đặt cạnh chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "con cá mặt trăng cái có thể phóng thích tới 300 triệu quả trứng vào làn nước biển! Đây là một kỷ lục vô tiền khoáng hậu, không 1 loài động vật có xương sống nào trên Trái Đất có". Bố cục: Bức ảnh siêu âm ấu trùng: chú ấu trùng cá mặt trăng tí hon tròn xoe như quả cầu gai phi thuyền ngoài hành tinh bé tí xíu chỉ dài hai mi-li-mét, nhỏ hơn hạt vừng đặt cạnh chiếc kim may áo của bác sĩ cá heo đeo ống nghe và kính viễn vọng, mặc áo blouse trắng hài hước.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "thể so bì! Hãy nhìn vào bức ảnh siêu âm ấu trùng của bệnh nhân: Chú cá con lúc mới chui ra khỏi vỏ trứng chỉ dài vỏn vẹn 2 mm, nhỏ hơn cả đầu tăm nhưng lại mang một ngoại". Bố cục: Phóng to chú ấu trùng cá mặt trăng tí hon tròn xoe như quả cầu gai phi thuyền ngoài hành tinh: Tròn ung ủng với hàng chục chiếc gai nhọn hoắt chìa ra xung quanh như một phi thuyền ngoài hành tinh mini dễ thương.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "hình cực kỳ tấu hài: Toàn thân chú cá con tròn ủng như một quả cầu gai, xung quanh mọc chìa ra hàng chục chiếc gai nhọn hoắt trông hệt như một chiếc phi thuyền người ngoài hành tinh tí". Bố cục: Đàn ấu trùng phi thuyền tí hon bơi lăng quăng giữa các loài sinh vật phù du, những chiếc gai nhọn giúp xua đuổi các loài tôm tép ăn thịt.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "hon! Chiếc áo giáp gai nhọn ấy giúp ấu trùng trôi nổi như sinh vật phù du và bảo vệ chúng khỏi miệng những kẻ săn mồi tí hon dưới đáy biển sâu! Kỳ diệu hơn nữa, những chú cá mặt". Bố cục: Biểu đồ tiến hóa tăng trưởng thể trọng: Từ ấu trùng 2mm rụng dần gai, lớn dần thành cá nhỏ rồi hóa thành gã khổng lồ hai tấn; mũi tên tăng trưởng gấp sáu mươi triệu lần.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "trăng sơ sinh vừa nở ra chỉ dài vỏn vẹn 2 mm, nhỏ hơn cả một hạt vừng và được bao bọc bởi những chiếc gai nhọn hoắt như một chú cá nóc mini! Từ kích thước 2 mm bé". Bố cục: chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim trưởng thành bơi bên cạnh đàn con tí hon; sự tương phản kích thước vĩ đại và kỳ diệu nhất của giới sinh vật biển.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tí xíu ấy, cá con phải tăng trưởng khối lượng gấp 60 triệu lần để trở thành một gã khổng lồ nặng 2 tấn! Một bước nhảy vọt thể trọng vĩ đại nhất trong toàn bộ thế giới sinh vật biển!". Bố cục: bác sĩ cá heo đeo ống nghe và kính viễn vọng, mặc áo blouse trắng hài hước đặt bút ký con dấu ĐÃ KIỂM ĐỊNH vào hồ sơ sinh sản của bệnh nhân với nụ cười khâm phục.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hồ sơ bệnh án số 44 chính thức khép lại với kết luận chẩn đoán: Cá Mặt Trăng hoàn toàn khỏe mạnh và là một bài học sinh tồn triết lý sâu sắc của mẹ". Bố cục: bác sĩ cá heo đeo ống nghe và kính viễn vọng, mặc áo blouse trắng hài hước đóng hồ sơ bệnh án số bốn mươi tư, mỉm cười gật gù; phía sau là bức tranh phong cảnh đại dương pastel tuyệt đẹp với chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim đang bình thản bơi lượn.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "thiên nhiên! Đôi khi trong cuộc sống, bạn không cần phải quá bon chen ganh đua, không cần phải trang bị móng vuốt nanh nhọn để gầm gừ đe dọa người khác. Gã khổng lồ vô". Bố cục: Triết lý sống vô tri: chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim trôi nhẹ nhàng giữa biển cả sóng gió, ánh nắng ấm áp chiếu rọi gương mặt an yên không màng danh lợi.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tri dạy chúng ta rằng: Cứ bình thản sống, cứ mở lòng phơi nắng đón nhận những điều tươi đẹp, và kiên trì mở lối đi riêng, đại dương bao la sẽ luôn dành cho". Bố cục: Màn hình tương tác người xem: Hai chiếc nút lựa chọn đồ họa pastel hài hước: Nút 1 là đầu cá hai tấn vô tư phơi nắng, Nút 2 là cỗ máy đẻ 300 triệu trứng.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bạn một chỗ đứng vững vàng! Nếu được sinh ra với một đặc tính của loài cá mặt trăng, bạn muốn sở hữu chiếc đầu khổng lồ 2 tấn vô tư phơi nắng hay cỗ máy". Bố cục: cô trợ lý hải cẩu đeo tạp dề chữ thập đỏ bưng khay kim tiêm giơ biển chỉ dẫn mời người xem để lại bình luận chẩn đoán bên dưới video.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "sinh sản 300 triệu quả trứng? Hãy để lại bình luận chẩn đoán của bạn bên dưới nhé! Còn bây giờ, hãy chuẩn bị bước vào bản tin hiện trường trực tiếp của hồ sơ". Bố cục: Hồ sơ mật tập 45 hé lộ: Một chú vẹt béo múp lông xanh rêu đang đứng đơ như bụi cây giữa khu rừng rậm New Zealand sương mù huyền ảo.
```
</details>

<details><summary>L57</summary>

```text
HÌNH L57 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "số 45! Một chú vẹt béo múp 4 kg đến từ New Zealand, loài vẹt duy nhất trên thế giới đã hoàn toàn quên mất cách bay, đêm đêm đi bộ cả chục cây số, và". Bố cục: Chú vẹt béo trèo lên cành cây cao rồi nhảy ùm xuống đất đập mặt ngơ ngác hài hước; các dấu hỏi chấm xoay quanh đầu chú vẹt.
```
</details>

<details><summary>L58</summary>

```text
HÌNH L58 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "thỉnh thoảng lại thích trèo lên ngọn cây cao rồi nhảy ùm xuống đất đập mặt ngơ ngác! Bạn có biết phóng sự điều tra này sẽ đưa chúng ta gặp gỡ chú vẹt nào không?". Bố cục: Màn hình kết thúc: Dòng chữ HẸN GẶP LẠI Ở TẬP 45 VẸT KAKAPO lung linh với lời kêu gọi đăng ký kênh và ấn chuông theo dõi.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Nặng tới 2 tấn nhưng hiền đến mức bị hải cẩu bơi lại cắn đứt từng mảng vây nó cũng chỉ". Bố cục: Cận cảnh mở đầu: chú hải cẩu tinh nghịch bơi lại cắn vây cá bơi lại cắn xé vây của chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri nặng hai tấn vẫn nằm ngửa nhìn trời ngơ ngác vô cảm.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "nằm ngửa nhìn trời ngơ ngác! Đây là Cá Mặt Trăng, gã khổng lồ vô tri nặng nhất thế giới loài". Bố cục: chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri to lớn như một chiếc xe tải bọc thép trôi dạt giữa đại dương; cơ thể cụt lủn không có đuôi cá thật.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "cá có xương! To xác như chiếc ô tô tải nhưng gã hoàn toàn không có đuôi cá thật sự, cơ". Bố cục: chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri bơi bằng hai cánh vây khổng lồ quạt nhịp nhàng; chiếc miệng tròn vo há hốc hút trọn những con sứa trong suốt.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "thể cụt lủn chỉ có cái đầu tròn xoe bơi bằng hai cánh vây khổng lồ. Món ăn khoái khẩu của gã". Bố cục: chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri lặn xuống vực biển sâu thẳm đen ngòm tám trăm mét, xung quanh nhiệt kế chỉ vạch buốt giá bốn độ C.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "là sứa biển chứa 99% nước, nên gã phải ăn cả tạ sứa mỗi ngày và lặn sâu 800 mét dưới". Bố cục: chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri ngoi lên mặt biển thoáng nằm nghiêng phơi bụng đón nắng vàng sưởi ấm thân nhiệt.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "cái lạnh 4°C. Sau mỗi chuyến lặn buốt giá, gã ngoi lên mặt nước nằm nghiêng phơi nắng để sưởi ấm". Bố cục: chú chim mòng biển đậu trên lưng cá rỉa spa đáp xuống đậu trên thân chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri, cần mẫn mổ rỉa sạch những con ký sinh trùng bám trên da.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "dòng nước màu lạnh và cho chim mòng biển rỉa sạch ký sinh trùng. Đổi lại sự ngơ ngác ấy, cá mẹ". Bố cục: chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri mẹ phóng thích hàng triệu quả trứng vàng phát sáng lấp lánh như dải ngân hà dưới làn nước biển xanh.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "đẻ tới 300 triệu quả trứng mỗi lần, một kỷ lục vô địch tuyệt đối trong giới động vật có xương sống!". Bố cục: Kỷ lục vô địch tuyệt đối: chú cá mặt trăng hoạt hình khổng lồ tròn vo cụt đuôi, mắt tròn xoe ngơ ngác há mỏ vô tri cười toe toét bên chiếc cúp vàng sinh sản ba trăm triệu quả trứng; mời gọi đăng ký kênh xem trọn bộ tập 44.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/58 của video YouTube về Cá Mặt Trăng). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa vẽ tay đặc trưng cho chủ đề, nét mực sắc nét, màu sắc tương phản cuốn hút, tối giản giàu tính biểu tượng khoa học; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim. Nhân vật phụ cố định: chiếc cần cẩu công nghiệp màu vàng cam rực rỡ với dây cáp thép to bản; chú hải cẩu xám béo tròn đang ngoạm cắn đuôi cá mặt trăng; chú ấu trùng cá mặt trăng tí hon tròn xoe như quả cầu gai phi thuyền ngoài hành tinh. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/8 của video YouTube Shorts về Cá Mặt Trăng). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa vẽ tay đặc trưng cho chủ đề, nét mực sắc nét, màu sắc tương phản cuốn hút, tối giản giàu tính biểu tượng khoa học; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú cá mặt trăng hoạt hình khổng lồ hình đĩa tròn dẹt màu lam ngọc pastel mềm mại, cụt đuôi với thùy clavus lượn sóng, hai mắt tròn xoe ngơ ngác vô hồn, chiếc miệng tròn vo há hốc ngốc nghếch, hai cánh vây lưng và vây phần đuôi cao vút quạt nhịp nhàng như cánh chim. Nhân vật phụ: chú hải cẩu tinh nghịch bơi lại cắn vây cá; chú chim mòng biển đậu trên lưng cá rỉa spa. 
```
</details>

## 7. SEO

- **title:** Gã Khổng Lồ 2 Tấn Vô Tri: Bị Hải Cẩu Cắn Vẫn Nằm Phơi Nắng?! | Cá Mặt Trăng | Tập 44
- **hook_paragraph:** Khám phá bệnh án kỳ lạ của Cá Mặt Trăng (Mola mola) — gã khổng lồ vô tri nặng 2 tấn cụt ngủn như cái đầu biết bơi, lặn sâu 800m săn sứa biển, đẻ 300 triệu trứng và nằm phơi nắng cho chim mòng biển rỉa spa!
- **question:** Nếu được sở hữu một đặc tính của loài cá này, bạn muốn có cơ thể 2 tấn vô tri phơi nắng hay kỷ lục đẻ 300 triệu trứng?
- **next_teaser:** Tập 45: Nhật ký 24h của chú vẹt béo quên cách bay thích leo cây nhảy đập mặt — Vẹt Kakapo!
- **shorts_title:** Gã khổng lồ 2 tấn bị cắn vẫn nằm phơi nắng?! 🐟☀️ #shorts #dongvat #khoahoc
- **shorts_desc:** Khám phá bí mật sinh tồn của Cá Mặt Trăng nặng 2 tấn cụt đuôi ngơ ngác, đẻ 300 triệu trứng và nằm nghiêng phơi nắng giữa đại dương!
- **bullets:** Cơ thể dị hợm nặng 2 tấn hoàn toàn không có đuôi cá thật mà biến tính thành thùy clavus cụt lủn · Thực đơn 99% nước của sứa biển buộc cá phải ăn cả tạ sứa mỗi ngày · Lặn sâu 800 mét dưới đáy biển buốt giá 4°C để săn sứa rồi ngoi lên phơi nắng sưởi ấm · Khách sạn di động cho hơn 40 loài ký sinh trùng được chim mòng biển làm spa miễn phí · Kỷ lục sinh sản vô địch thế giới động vật có xương sống với 300 triệu quả trứng mỗi lần
- **tags:** cá mặt trăng, ca mat trang, mola mola, ocean sunfish, cá khổng lồ vô tri, cá đẻ 300 triệu trứng, thế giới động vật, vẽ chuyện hoang dã, tập 44
- **hashtags:** #CaMatTrang #MolaMola #TheGioiDongVat #VeChuyenHoangDa #KhoaHoc #DongVatKyThu

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-44-ca-mat-trang
python src/episode/pipeline.py tts    projects/tap-44-ca-mat-trang     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-44-ca-mat-trang     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-44-ca-mat-trang     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-44-ca-mat-trang              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-44-ca-mat-trang --force
python scripts/beat_sheet.py projects/tap-44-ca-mat-trang               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-44-ca-mat-trang/audio/shorts.wav projects/tap-44-ca-mat-trang/renders/tap-44-ca-mat-trang_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-44-ca-mat-trang
python src/episode/pipeline.py seo    projects/tap-44-ca-mat-trang
python src/episode/episode_doc.py     projects/tap-44-ca-mat-trang
```
