# TẬP 27 — CHUỘT CHŨI SAO · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-27-chuot-chui-sao`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-27-chuot-chui-sao`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F4` · **Persona giọng:** `phong_vien_24h` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Chuột Chũi Sao |
| Tiêu đề YouTube | Cỗ Máy Mù Lòa Ăn Mồi Trong 0,12 Giây & Ngửi Mùi Dưới Nước?! |
| Video dài | `renders/tap-27-chuot-chui-sao_long.mp4` — 8:59.1 (539.1s) |
| Shorts | `renders/tap-27-chuot-chui-sao_shorts.mp4` — 0:48.1 (48.1s) |
| Thumbnail | `renders/tap-27-chuot-chui-sao_thumbnail.jpg` |
| Số hình | dài 58 beat / 58 ảnh riêng; Shorts 10 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.1**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/58 của video YouTube về Chuột Chũi Sao). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ. Nhân vật phụ cố định: anh chàng phóng viên truyền hình 24H hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H; cô phát thanh viên bản tin trực tiếp hoạt hình đeo tai nghe. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — 00 SÁNG: MỞ MÀN CUỘC ĐUA SINH TỒN VÀ CHIẾC MŨI QUÁI VẬT NGOÀI HÀNH TINH
*Badge:* `06:00 SÁNG` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene01_p0.wav` (437 ký tự) · mood `hao_hung`

```text
Bây giờ là không sáu giờ sáng! Chúng tôi đang có mặt trực tiếp tại một đầm lầy ẩm ướt vùng Đông Bắc Bắc Mỹ. Sương mù mờ ảo giăng kín mặt đất, tiếng đồng hồ tích tắc báo hiệu cuộc đua sinh tồn nghẹt thở hai mươi bốn giờ chính thức khai hỏa! Dưới lớp bùn đất nhão nhoẹt, mặt đất bắt đầu rung chuyển nhẹ... Một cỗ máy khoan đất tí hon chỉ nặng khoảng năm mươi gam, dài chưa đầy mười lăm đến hai mươi xăng-ti-mét, bỗng chốc đùn đất trồi lên!
```
**Part 1** → `audio/vs/scene01_p1.wav` (145 ký tự) · 🎭 cameo `phat_thanh_vien`

```text
Báo cáo phóng viên hiện trường: Mục tiêu vừa lộ diện nhưng trên mặt nó không có mắt, mà gắn một bông hoa thịt màu đỏ hồng đang ngoe nguẩy dữ dội!
```
**Part 2** → `audio/vs/scene01_p2.wav` (509 ký tự) · mood `hao_hung`

```text
[surprise-oh] Quý vị khán giả của đài truyền hình Vẽ Chuyện Hoang Dã đừng vội hoảng sợ! Đây không phải quái vật ngoài hành tinh xâm lăng Trái Đất, mà là Chuột Chũi Sao, loài động vật có vú sở hữu cơ quan cảm giác kỳ dị bậc nhất hành tinh! Hai mắt của nó thoái hóa mù tịt, hai tai không có vành, nhưng ngay trên đầu mũi lại xòe ra hai mươi hai xúc tu thịt màu hồng tươi rung rinh liên tục như một bông hoa sao biển! Trong bản tin trực tiếp hôm nay, chúng tôi gọi thẳng tên nó bằng biệt danh: Tia Chớp Lòng Đất!
```
**Part 3** → `audio/vs/scene01_p3.wav` (330 ký tự) · mood `nghiem_trang_gia`

```text
Điều gì đã khiến một sinh vật nhỏ bé mù lòa lại được Tổ chức Kỷ lục Thế giới Ghi-nét phong tặng danh hiệu cỗ máy săn mồi nhanh nhất hành tinh? Chiếc mũi sao kia vận hành thần tốc ra sao để giúp nó sinh tồn suốt một ngày dài đói khát? Hãy cùng trường quay của chúng tôi theo sát từng mốc thời gian trong ngày của Tia Chớp Lòng Đất!
```

### scene02 — 00 TRƯA: KỶ LỤC GUINNESS 120 MILI-GIÂY VÀ 25.000 THỤ THỂ EIMER
*Thẻ chương:* ĂN MỒI NHANH HƠN CHỚP MẮT: 120 MILI-GIÂY

*Badge:* `12:00 TRƯA` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene02_p0.wav` (300 ký tự) · mood `don_dap`

```text
Đồng hồ điểm mười hai giờ trưa! Ánh nắng mặt trời rọi thẳng đứng nhưng dưới lòng địa đạo tăm tối, Tia Chớp Lòng Đất đang bắt đầu bữa tiệc trưa tốc độ ánh sáng! Hãy chuẩn bị tinh thần theo dõi camera quay chậm một ngàn khung hình mỗi giây, vì mắt thường của quý vị hoàn toàn bất lực trước vận tốc này!
```
**Part 1** → `audio/vs/scene02_p1.wav` (366 ký tự) · mood `don_dap`

```text
Giáo sư Ken-nét Ca-ta-ni-a tại Đại học Ban-đơ-bin đã đưa chuột chũi sao vào phòng thí nghiệm với máy quay tốc độ cao và phát hiện một kỷ lục thế giới kinh hoàng: thời gian trung bình để nó dùng mũi chạm vào con mồi, nhận diện ăn được hay không, rồi há miệng ngoạm nuốt chửng... chỉ mất đúng một trăm hai mươi mili-giây, tức là không phẩy mười hai giây! [surprise-wa]
```
**Part 2** → `audio/vs/scene02_p2.wav` (419 ký tự) · mood `hao_hung`

```text
Quý vị có biết một cái chớp mắt của con người mất bao lâu không? Mất khoảng ba trăm đến bốn trăm mili-giây! Nghĩa là trong lúc quý vị vừa chớp mắt một cái nhẹ tênh, chú Chuột Chũi Sao đã kịp chén sạch sành sanh ba con giun liên tiếp! [laughter] Thậm chí bộ não của nó chỉ mất đúng tám mili-giây để phân tích tín hiệu thần kinh và đưa ra quyết định ăn hay bỏ — nhanh ngang ngửa tốc độ xử lý của vi mạch máy tính tối tân!
```
**Part 3** → `audio/vs/scene02_p3.wav` (364 ký tự) · mood `don_dap`

```text
Bí mật đằng sau tốc độ bàn thờ này nằm trọn trên chiếc mũi hoa sao: trên hai mươi hai chiếc xúc tu thịt nhỏ xíu chứa tới hơn hai mươi lăm ngàn thụ thể xúc giác siêu nhạy gọi là thụ thể Ai-mơ, được nuôi dưỡng bởi hơn một trăm ngàn sợi dây thần kinh — tức là dày đặc gấp sáu lần toàn bộ dây thần kinh trên cả hai bàn tay của một con người trưởng thành! [surprise-oh]
```
**Part 4** → `audio/vs/scene02_p4.wav` (477 ký tự) · mood `hao_hung`

```text
Khi đi săn trong bóng tối mù mịt, chiếc mũi của Tia Chớp Lòng Đất gõ liên hồi xuống bùn đất với tần số khó tin: chạm tới mười hai vị trí khác nhau trong vỏn vẹn một giây! Mười cặp xúc tu bên ngoài làm nhiệm vụ dò đường quét rộng, khi phát hiện thứ gì nghi ngờ là thức ăn, nó lập tức điều phối cặp xúc tu số mười một chụp lấy kiểm tra cận cảnh! Chẳng một hạt cát, chẳng một con ấu trùng bọ cánh cứng nào có thể trốn thoát trước chiếc máy quét xúc giác quét từng milimet đất này!
```
**Part 5** → `audio/vs/scene02_p5.wav` (402 ký tự) · mood `don_dap`

```text
Không những thế, bộ hàm của nó còn trang bị những chiếc răng cửa nhọn hoắt đan chéo vào nhau như chiếc nhíp gắp siêu nhỏ! Ngay khi cặp xúc tu số mười một xác nhận con mồi, chiếc nhíp răng liền phóng ra ngoạm chặt và kéo thẳng con mồi vào họng, kết hợp với tuyến nước bọt có chất gây tê nhẹ làm con giun đất bất động ngay tức khắc! Đúng là dây chuyền bắt và chế biến thức ăn tự động nhanh nhất thế giới!
```

### scene03 — 00 HOÀNG HÔN: LẶN SUỐI DƯỚI BĂNG VÀ TUYỆT KỸ NGỬI MÙI BẰNG BONG BÓNG
*Thẻ chương:* ĐỘNG VẬT CÓ VÚ DUY NHẤT NGỬI MÙI DƯỚI NƯỚC

*Badge:* `18:00 HOÀNG HÔN` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene03_p0.wav` (335 ký tự) · mood `tram_bi_an`

```text
Bầu trời hoàng hôn buông xuống, đồng hồ chuyển sang mốc mười tám giờ hoàng hôn. Đừng nghĩ chuột chũi chỉ biết quanh quẩn đào đất trong bóng tối khô ráo. Tia Chớp Lòng Đất của chúng ta là một vận động viên bơi lội bán thủy sinh cừ khôi, và địa bàn hoạt động buổi chiều tà của gã chuyển thẳng xuống những dòng suối lạnh buốt ven đầm lầy!
```
**Part 1** → `audio/vs/scene03_p1.wav` (381 ký tự) · mood `tram_bi_an`

```text
Hai bàn chân trước to bè như hai mái chèo xẻ nước, chiếc đuôi dày cộp đóng vai trò bánh lái đưa gã lặn sâu xuống đáy nước mò tìm ấu trùng chuồn chuồn và cá nhỏ. Nhưng điều làm chấn động toàn bộ giới sinh học thế giới — được công bố trên tạp chí Nature năm hai ngàn lẻ sáu — là câu hỏi: làm thế nào một loài thú lại có thể đánh hơi tìm mồi dưới nước khi không thể hít nước vào phổi?
```
**Part 2** → `audio/vs/scene03_p2.wav` (150 ký tự) · 🎭 cameo `phat_thanh_vien`

```text
Báo cáo hiện trường: Camera hồng ngoại dưới nước ghi nhận mẫu vật liên tục thổi những quả bong bóng khí tròn xoe ra khỏi lỗ mũi rồi hít ngược trở lại!
```
**Part 3** → `audio/vs/scene03_p3.wav` (436 ký tự) · mood `don_dap`

```text
[surprise-oh] Quý vị đang chứng kiến một kỳ quan vật lý sinh học độc nhất vô nhị! Chuột Chũi Sao chính là loài động vật có vú đầu tiên trên hành tinh được chứng minh có khả năng ngửi mùi dưới nước! Nó thổi những bong bóng khí nhỏ từ mũi chạm vào thức ăn, các phân tử mùi trong nước lập tức khuếch tán bám vào bề mặt bong bóng, và trong chớp mắt, nó hít ngược bong bóng vào khoang mũi để cơ quan khứu giác phân tích mùi vị! [surprise-wa]
```
**Part 4** → `audio/vs/scene03_p4.wav` (322 ký tự) · mood `hao_hung`

```text
Tần số thổi và hít lại bong bóng này đạt từ năm đến mười lần mỗi giây — nhanh và nhịp nhàng hệt như cách một chú chuột cống hít hà đánh hơi trên cạn! Nhờ chiếc máy thở bong bóng tuần hoàn này, dù đáy suối tối om không nhìn thấy gì, Tia Chớp Lòng Đất vẫn bơi theo dấu vết mùi của con mồi chuẩn xác từng centimet! [laughter]
```
**Part 5** → `audio/vs/scene03_p5.wav` (385 ký tự) · mood `hao_hung`

```text
Thậm chí vào mùa đông khi mặt nước đầm lầy đóng thành những tảng băng dày cứng ngắc, gã vẫn lặn ngụp dưới băng, thổi những quả bong bóng khí chạm vào mặt dưới của tảng băng để gom mùi hương của tôm tép đang bơi lội! Các nhà vật lý chất lưu thán phục rằng cơ chế bắt dính phân tử mùi qua sức căng bề mặt của bong bóng là một phát kiến tự nhiên siêu việt mà con người chưa từng nghĩ tới!
```

### scene04 — 00 NỬA ĐÊM: CẶP XÚC TU SỐ 11 VÀ BẢN ĐỒ XÚC GIÁC CHIẾM TRỌN VỎ NÃO
*Thẻ chương:* BẢN ĐỒ NÃO BỘ KHỔNG LỒ DÀNH RIÊNG CHO MŨI SAO

*Badge:* `00:00 NỬA ĐÊM` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene04_p0.wav` (245 ký tự) · mood `tram_bi_an`

```text
Đồng hồ điểm không không giờ nửa đêm! Rừng đầm lầy chìm trong bóng tối dày đặc, tiếng cú mèo rúc vang trên cành cây báo hiệu giờ săn mồi của những kẻ thù nguy hiểm nhất: chồn ec-min, rắn nước và chim săn đêm đang rình rập quanh các cửa hầm ngầm.
```
**Part 1** → `audio/vs/scene04_p1.wav` (316 ký tự) · mood `don_dap`

```text
Bên trong lòng đất, Tia Chớp Lòng Đất vẫn miệt mài vận hành cỗ máy thần kinh tinh vi nhất. Khi các nhà khoa học chụp bản đồ quét não bộ của nó, họ phát hiện một hiện tượng giải phẫu làm kinh ngạc toàn ngành thần kinh học: toàn bộ vùng vỏ não cảm giác bản thể của nó hầu như bị chiếc mũi hoa sao chiếm trọn hoàn toàn!
```
**Part 2** → `audio/vs/scene04_p2.wav` (460 ký tự) · mood `don_dap`

```text
Đặc biệt nhất là cặp xúc tu ở vị trí thứ mười một — cặp xúc tu nhỏ nhất nằm ở chính giữa phía dưới của bông hoa sao! Cặp xúc tu thứ mười một này hoạt động y hệt như hoàng điểm Pho-vê-a trên võng mạc mắt người — tức là vùng có độ phân giải thị giác sắc nét nhất! Khi hai mươi xúc tu bên ngoài chạm lướt qua phát hiện vật thể khả nghi, chiếc mũi lập tức hướng cặp xúc tu thứ mười một vào kiểm tra cận cảnh với độ phóng đại não bộ lớn gấp nhiều lần! [surprise-oh]
```
**Part 3** → `audio/vs/scene04_p3.wav` (354 ký tự) · mood `hao_hung`

```text
Các nghiên cứu giải phẫu thần kinh cho thấy hơn năm mươi phần trăm diện tích của vùng não cảm giác bản thể dành trọn vẹn để xử lý thông tin từ chiếc mũi chỉ rộng chưa đầy một centimet này! Nếu vẽ lại cơ thể chuột chũi sao theo tỷ lệ diện tích não bộ điều khiển, chiếc mũi của nó sẽ to đùng bằng cả tòa nhà, còn thân mình và chân tay chỉ bé bằng hạt vừng!
```
**Part 4** → `audio/vs/scene04_p4.wav` (351 ký tự) · mood `hao_hung`

```text
Thế nên dù không có mắt để nhìn, thế giới trong đầu của Chuột Chũi Sao lại rực rỡ và chi tiết đến từng milimet qua những bức tranh xúc giác ba đê sống động! Nó nhìn thấy thế giới bằng chính chiếc mũi sao của mình, định vị không gian và phát hiện kẻ thù đào đất mò tới từ khoảng cách hàng mét để kịp thời bịt kín ngách hầm tẩu thoát an toàn! [laughter]
```

### scene05 — 00 RẠNG SÁNG: CƠN ĐÓI LIÊN TỤC VÀ CHIẾC ĐUÔI PHÌNH TO TRỮ MỠ MÙA ĐÔNG
*Thẻ chương:* ĂN LƯỢNG THỨC ĂN BẰNG CẢ TRỌNG LƯỢNG CƠ THỂ MỖI NGÀY

*Badge:* `04:00 RẠNG SÁNG` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene05_p0.wav` (289 ký tự) · mood `tram_bi_an`

```text
Bây giờ là không bốn giờ rạng sáng. Nhiệt độ ngoài trời giảm xuống mức đóng băng, hơi lạnh buốt giá bắt đầu luồn vào từng kẽ đất. Lúc này, Tia Chớp Lòng Đất phải đối mặt với kẻ thù nguy hiểm nhất đe dọa sự sống còn của chính mình: Cơn đói cồn cào của cỗ máy chuyển hóa năng lượng siêu tốc!
```
**Part 1** → `audio/vs/scene05_p1.wav` (389 ký tự) · mood `don_dap`

```text
Với một cơ thể nhỏ bé năm mươi gam nhưng vận động đào bới liên tục với nhịp tim và trao đổi chất cao ngất ngưởng, nó không thể nhịn ăn quá vài giờ đồng hồ. Mỗi ngày, một chú Chuột Chũi Sao phải tiêu thụ lượng thức ăn tương đương từ một nửa cho đến gần bằng một trăm phần trăm trọng lượng cơ thể của chính mình! Nếu ngừng ăn là pin năng lượng sẽ cạn sạch và cơ thể sẽ hạ thân nhiệt tử vong!
```
**Part 2** → `audio/vs/scene05_p2.wav` (333 ký tự) · mood `hao_hung`

```text
Thế nhưng khi mùa đông tuyết trắng phủ dày cả mét và mặt hồ đóng băng cứng ngắc, làm sao nó sống sót? Hãy nhìn ra phía sau chiếc đuôi của nó: vào mùa thu trù phú, chiếc đuôi của Chuột Chũi Sao phình to gấp ba đến bốn lần kích thước bình thường, biến thành một bình ắc-quy sinh học tích trữ đầy mỡ béo dự trữ năng lượng! [surprise-oh]
```
**Part 3** → `audio/vs/scene05_p3.wav` (266 ký tự) · mood `hao_hung`

```text
Nhờ chiếc đuôi tích mỡ thần kỳ kết hợp với bộ lông nhung không thấm nước dày dặn, gã thản nhiên bơi lặn săn mồi bên dưới lớp băng tuyết mùa đông lạnh thấu xương mà không hề biết đến khái niệm ngủ đông là gì! Đúng là chiến binh bốn mùa bất khuất của thế giới đầm lầy!
```
**Part 4** → `audio/vs/scene05_p4.wav` (310 ký tự) · mood `hao_hung`

```text
Đặc biệt là vào những đợt bão tuyết khắc nghiệt, nhiệt độ dưới lớp băng có thể giảm sâu xuống gần không độ C, nhưng nhiệt độ cơ thể của Tia Chớp Lòng Đất vẫn duy trì ổn định ở ba mươi bảy độ C! Toàn bộ mỡ dự trữ trong chiếc đuôi phình to được đốt cháy từng phần để sưởi ấm các cơ quan nội tạng quan trọng nhất!
```

### scene06 — CHIẾC ĐỒNG HỒ KHÉP VÒNG VÀ BÓNG ĐEN KIẾN NỔ CẢM TỬ
*Thẻ chương:* VÒNG XOAY 24H KHÉP LẠI VÀ BÓNG ĐEN QUÂN ĐOÀN CẢM TỬ

*Badge:* `KẾT THÚC 24H` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene06_p0.wav` (248 ký tự) · mood `am_ap`

```text
Đồng hồ lại điểm không sáu giờ sáng! Tròn hai mươi bốn giờ nghẹt thở đã trôi qua. Sương sớm lại giăng kín đầm lầy, và cuộc đua sinh tồn của Tia Chớp Lòng Đất lại khép lại một vòng quay Trái Đất để rồi tiếp tục bắt đầu một ngày mới không ngừng nghỉ.
```
**Part 1** → `audio/vs/scene06_p1.wav` (249 ký tự) · mood `hao_hung`

```text
Từ một sinh vật mù lòa xấu xí bị xem là dị hợm, Chuột Chũi Sao đã biến chiếc mũi hoa sao thành một tuyệt tác tiến hóa đỉnh cao: ăn mồi trong không phẩy mười hai giây, ngửi mùi dưới nước bằng bong bóng và vẽ nên bản đồ thế giới bằng xúc giác kỳ diệu!
```
**Part 2** → `audio/vs/scene06_p2.wav` (311 ký tự) · mood `hao_hung`

```text
Phóng sự hai mươi bốn giờ của chúng tôi xin được khép lại tại đây. Còn quý vị khán giả thì sao? Nếu được sở hữu một siêu năng lực của Tia Chớp Lòng Đất: tốc độ ăn tối nhanh hơn cái chớp mắt không lo trễ giờ, hay khả năng ngửi mùi dưới nước bằng bong bóng, quý vị chọn cái nào? Hãy để lại bình luận bên dưới nhé!
```
**Part 3** → `audio/vs/scene06_p3.wav` (545 ký tự) · mood `am_ap`

```text
Và bây giờ, bản tin đặc biệt xin được bật mí bóng đen bí ẩn của tập tiếp theo! Rời khỏi đầm lầy Bắc Mỹ, chúng ta sẽ bước vào rừng mưa nhiệt đới Đông Nam Á để chứng kiến một đội quân đế chế khét tiếng tàn bạo! Những chiến binh bé nhỏ mang trong mình lòng trung thành tuyệt đối với bà trùm: khi kẻ thù tấn công tổ, chúng sẵn sàng tự gồng cơ bụng nổ tung cơ thể mình như những quả bom cảm tử, phun ra dòng chất độc màu vàng dính chặt kẻ thù cùng chết chung! Đố các bạn biết bóng đen bí ẩn kỳ sau là loài vật nào? Hãy đoán ngay ở phần bình luận nhé!
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Sinh vật mù lòa này ăn tối nhanh đến mức khó tin: chỉ mất đúng không phẩy mười hai giây để nhận diện và nuốt chửng con mồi, nhanh hơn cả một cái chớp mắt của con người! [laughter] Xin giới thiệu Chuột Chũi Sao, cỗ máy săn mồi dài hai mươi xăng-ti-mét sống dưới các đầm lầy Bắc Mỹ. Hai mắt của nó thoái hóa mù tịt, nhưng trên mũi lại mọc ra hai mươi hai xúc tu thịt màu hồng xòe rộng như một bông hoa sao biển! [surprise-wa] Chiếc mũi quái đản này chứa hơn hai mươi lăm ngàn thụ thể cảm giác, gõ xuống bùn đất tới mười hai vị trí mỗi giây để dò mồi! Thậm chí khi lặn xuống nước, nó là loài thú duy nhất biết thổi những quả bong bóng khí ra khỏi mũi rồi hít ngược trở lại để ngửi mùi con mồi dưới đáy suối! Bộ não của nó chỉ mất đúng tám mili-giây để quyết định ăn hay bỏ! Một tia chớp lòng đất với chiếc mũi quái vật ngoài hành tinh sở hữu tốc độ săn mồi nhanh nhất hành tinh!
```

**Whisper prompt:** `Chuột Chũi Sao, Tia Chớp Lòng Đất, Condylura cristata, Ken-nét Ca-ta-ni-a, Kenneth Catania, Ban-đơ-bin, Vanderbilt, Eimer, thụ thể Eimer, fovea, vỏ não, somatosensory cortex, 22 xúc tu, 25.000, 100.000, 0,12 giây, 120 mili-giây, 8 mili-giây, 12 vị trí, 10 lần, 50g, 24 giờ, 06:00, 12:00, 18:00, 00:00, 04:00`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| hai mươi bảy | 27 |
| hai mươi tám | 28 |
| hai mươi hai xúc tu | 22 xúc tu |
| hai mươi hai | 22 |
| hai mươi xúc tu | 20 xúc tu |
| hai mươi | 20 |
| hai mươi mốt | 21 |
| hai mươi ba | 23 |
| hai mươi bốn | 24 |
| hai mươi lăm ngàn | 25.000 |
| hai mươi lăm | 25 |
| một trăm ngàn | 100.000 |
| một ngàn | 1.000 |
| ba trăm | 300 |
| bốn trăm | 400 |
| ba trăm đến bốn trăm mili-giây | 300-400 mili-giây |
| không phẩy mười hai giây | 0,12 giây |
| một trăm hai mươi mili-giây | 120 mili-giây |
| tám mili-giây | 8 mili-giây |
| mười hai vị trí | 12 vị trí |
| mười hai | 12 |
| mười vị trí | 10 vị trí |
| năm đến mười lần | 5-10 lần |
| mười lần | 10 lần |
| mười một cặp | 11 cặp |
| mười cặp | 10 cặp |
| năm lần | 5 lần |
| sáu lần | 6 lần |
| năm mươi gam | 50g |
| năm mươi phần trăm | 50% |
| mười lăm đến hai mươi xăng-ti-mét | 15-20cm |
| mười lăm xăng-ti-mét | 15cm |
| hai mươi xăng-ti-mét | 20cm |
| hai mươi bốn giờ | 24 giờ |
| không sáu giờ sáng | 06:00 |
| mười hai giờ trưa | 12:00 |
| mười tám giờ hoàng hôn | 18:00 |
| không không giờ nửa đêm | 00:00 |
| không bốn giờ rạng sáng | 04:00 |
| năm hai ngàn lẻ sáu | 2006 |
| một trăm phần trăm | 100% |
| hàng ngàn | hàng ngàn |
| hàng trăm | hàng trăm |
| thứ nhất | thứ 1 |
| thứ hai | thứ 2 |
| thứ ba | thứ 3 |
| thứ tư | thứ 4 |
| không độ C | 0°C |
| ba mươi bảy độ C | 37°C |
| số mười một | số 11 |
| mười một | 11 |
| thứ mười một | thứ 11 |
| thứ 11 | thứ 11 |
| ba đê | 3D |
| Ghi-nét | Guinness |
| Ken-nét | Kenneth |
| Ca-ta-ni-a | Catania |
| Ban-đơ-bin | Vanderbilt |
| Ai-mơ | Eimer |
| Pho-vê-a | Fovea |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · 00 SÁNG: MỞ MÀN CUỘC ĐUA SINH TỒN VÀ CHIẾC MŨI QUÁI VẬT NGOÀI HÀNH TINH · 71.2s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.2 (7.2s) | L01 | Bây giờ là 06:00! Chúng tôi đang có mặt trực tiếp tại một đầm lầy ẩm ướt vùng Đông Bắc Bắc Mỹ. Sương mù mờ ảo giăng kín |  | Bầu trời sáng sớm đầm lầy sương mù mờ ảo: chiếc đồng hồ kim lớn điểm đúng 06:00 sáng; anh chàng phóng viên truyền hình 24H hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H cầm micro phát sóng trực tiếp bên bãi bùn ẩm ướt. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này. |
| b02 | 00:07.2–00:15.6 (8.4s) | L02 | mặt đất, tiếng đồng hồ tích tắc báo hiệu cuộc đua sinh tồn nghẹt thở 24 giờ chính thức khai hỏa! Dưới lớp bùn đất nhão nhoẹt, mặt đất bắt đầu rung chuyển nhẹ... |  | Đồng hồ cát 24 giờ đếm ngược phát sáng cam; mặt đất đầm lầy ẩm ướt bắt đầu rung chuyển nhẹ có những vết nứt nhỏ. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này. |
| b03 | 00:15.6–00:18.5 (2.9s) | L03 | Một cỗ máy khoan đất tí hon chỉ nặng khoảng 50g, | **NẶNG 50G** · cỗ máy khoan đất · L/350 · [0.35, 0.45] | Mặt đất ẩm ướt đùn lên một ụ đất tròn; từ dưới hang tối, một cỗ máy khoan đất tí hon nặng 50g với bộ lông nhung đen trồi đầu lên mặt đất. |
| b04 | 00:18.5–00:22.9 (4.4s) | L04 | dài chưa đầy 15-20cm, bỗng chốc đùn đất trồi lên! | **15-20 CM** · kích thước cơ thể · R/350 · [0.65, 0.5] | Ở GIỮA chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ đứng cạnh chiếc thước đo chiều cao màu vàng 15-2 |
| b05 | 00:22.9–00:30.6 (7.7s) | L05 | Báo cáo phóng viên hiện trường: Mục tiêu vừa lộ diện nhưng trên mặt nó không có mắt, mà gắn một bông hoa thịt màu đỏ hồng đang ngoe nguẩy dữ dội! |  | Màn hình trường quay: cô phát thanh viên bản tin trực tiếp hoạt hình đeo tai nghe chỉ tay vào hình ảnh phóng to cận cảnh chiếc mũi đỏ hồng xòe ra 22 xúc tu đang ngoe nguẩy dữ dội. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này. |
| b06 | 00:30.6–00:41.2 (10.6s) | L06 | Quý vị khán giả của đài truyền hình Vẽ Chuyện Hoang Dã đừng vội hoảng sợ! Đây không phải quái vật ngoài hành tinh xâm lăng Trái Đất, mà là Chuột Chũi Sao, loài động vật có vú sở hữu cơ quan cảm giác kỳ dị bậc nhất hành tinh! |  | chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ đứng trên gò đất đầm lầy, chiếc mũi sao biển hồng rung  |
| b07 | 00:41.2–00:50.6 (9.4s) | L07 | Hai mắt của nó thoái hóa mù tịt, hai tai không có vành, nhưng ngay trên đầu mũi lại xòe ra 22 xúc tu thịt màu hồng tươi rung rinh liên tục như một bông hoa sao biển! | **22 XÚC TU** · mũi hình hoa sao · R/350 · [0.65, 0.48] | Cận cảnh đầu của chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ: hai mắt thoái hóa thành hai đốm nhỏ x |
| b08 | 00:50.6–00:55.9 (5.3s) | L08 | Trong bản tin trực tiếp hôm nay, chúng tôi gọi thẳng tên nó bằng biệt danh: Tia Chớp Lòng Đất! |  | chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ hóa thân thành siêu anh hùng đeo chiếc đồng hồ bấm giờ  |
| b09 | 00:55.9–01:07.2 (11.2s) | L09 | Điều gì đã khiến một sinh vật nhỏ bé mù lòa lại được Tổ chức Kỷ lục Thế giới Guinness phong tặng danh hiệu cỗ máy săn mồi nhanh nhất hành tinh? Chiếc mũi sao kia vận hành thần tốc ra sao để giúp nó sinh tồn suốt một ngày dài đói khát? | **GUINNESS** · kỷ lục thế giới · L/350 · [0.35, 0.45] | Cuốn sách Kỷ lục Thế giới Guinness mở ra biểu tượng cúp vàng trao cho chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ m |
| b10 | 01:07.2–01:11.2 (4.1s) | L10 | Hãy cùng trường quay của chúng tôi theo sát từng mốc thời gian trong ngày của Tia Chớp Lòng Đất! |  | anh chàng phóng viên truyền hình 24H hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H chỉ vào chiếc đồng hồ 24 giờ đang chạy tích tắc; chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng  |

### scene02 · 00 TRƯA: KỶ LỤC GUINNESS 120 MILI-GIÂY VÀ 25.000 THỤ THỂ EIMER · 114.0s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:14.3 (14.3s) | L11 | Đồng hồ điểm 12:00! Ánh nắng mặt trời rọi thẳng đứng nhưng dưới lòng địa đạo tăm tối, Tia Chớp Lòng Đất đang bắt đầu bữa tiệc trưa tốc độ ánh sáng! Hãy chuẩn bị tinh thần theo dõi camera quay chậm 1.000 khung hình mỗi giây, vì mắt thường của quý vị hoàn toàn bất lực trước vận tốc này! | **1.000 FPS** · máy quay siêu tốc · R/350 · [0.65, 0.48] | Đồng hồ trường quay điểm đúng 12:00 trưa; anh chàng phóng viên truyền hình 24H hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H đang đứng cạnh máy quay tốc độ cao 1.000 khung hình mỗi giây chiếu vào lòng địa đạo tăm tối. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này. |
| b02 | 00:14.3–00:22.1 (7.8s) | L12 | Giáo sư Kenneth Catania tại Đại học Vanderbilt đã đưa chuột chũi sao vào phòng thí nghiệm với máy quay tốc độ cao và phát hiện một kỷ lục thế giới kinh hoàng: | **VANDERBILT** · Đại học danh tiếng · L/350 · [0.35, 0.45] | Phòng thí nghiệm Đại học Vanderbilt: Giáo sư Kenneth Catania quan sát màn hình camera quay chậm cận cảnh chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một  |
| b03 | 00:22.1–00:31.6 (9.5s) | L13 | thời gian trung bình để nó dùng mũi chạm vào con mồi, nhận diện ăn được hay không, rồi há miệng ngoạm nuốt chửng... chỉ mất đúng 120 mili-giây, tức là 0,12 giây! | **120 MS** · thời gian ăn mồi · R/350 · [0.65, 0.45]<br>**0,12 GIÂY** · kỷ lục Guinness · L/480 · [0.32, 0.55] | Đồng hồ bấm giờ điện tử dừng lại ở con số 120 mili-giây (0,12 giây) bốc khói: chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện  |
| b04 | 00:31.6–00:44.1 (12.5s) | L14 | Quý vị có biết một cái chớp mắt của con người mất bao lâu không? Mất khoảng 300-400 mili-giây! Nghĩa là trong lúc quý vị vừa chớp mắt một cái nhẹ tênh, chú Chuột Chũi Sao đã kịp chén sạch sành sanh ba con giun liên tiếp! | **300-400 MS** · một cái chớp mắt · L/350 · [0.35, 0.45] | Mắt người đang chớp một cái mất 300-400 mili-giây; ở bên cạnh chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam t |
| b05 | 00:44.1–00:53.2 (9.1s) | L15 | Thậm chí bộ não của nó chỉ mất đúng 8 mili-giây để phân tích tín hiệu thần kinh và đưa ra quyết định ăn hay bỏ — nhanh ngang ngửa tốc độ xử lý của vi mạch máy tính tối tân! | **8 MS** · phân tích não bộ · R/350 · [0.65, 0.48] | Sơ đồ não bộ phát xung điện thần kinh siêu tốc chỉ trong 8 mili-giây đưa ra quyết định ăn mồi, ngang ngửa tốc độ xử lý của vi mạch máy tính. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này. |
| b06 | 00:53.2–01:02.7 (9.4s) | L16 | Bí mật đằng sau tốc độ bàn thờ này nằm trọn trên chiếc mũi hoa sao: trên 22 chiếc xúc tu thịt nhỏ xíu chứa tới hơn 25.000 thụ thể xúc giác siêu nhạy gọi là thụ thể Eimer, | **25.000 THỂ** · thụ thể Eimer · R/350 · [0.68, 0.48] | Kính hiển vi phóng to chiếc mũi hoa sao: 22 xúc tu thịt chứa hơn 25.000 thụ thể Eimer hình vòm nhỏ li ti và 100.000 sợi dây thần kinh dày đặc. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này. |
| b07 | 01:02.7–01:10.3 (7.6s) | L17 | được nuôi dưỡng bởi hơn 100.000 sợi dây thần kinh — tức là dày đặc gấp 6 lần toàn bộ dây thần kinh trên cả hai bàn tay của một con người trưởng thành! | **100.000** · gấp 6 lần tay người · L/350 · [0.3, 0.5] | So sánh hệ thần kinh: chiếc mũi hoa sao nhỏ bé có mật độ dây thần kinh dày đặc gấp 6 lần toàn bộ dây thần kinh trên cả hai bàn tay của một con người trưởng thành. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này. |
| b08 | 01:10.3–01:19.7 (9.4s) | L18 | Khi đi săn trong bóng tối mù mịt, chiếc mũi của Tia Chớp Lòng Đất gõ liên hồi xuống bùn đất với tần số khó tin: chạm tới 12 vị trí khác nhau trong vỏn vẹn một giây! | **12 ĐIỂM/S** · tần số chạm mũi · R/350 · [0.65, 0.5] | chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ gõ liên hồi chiếc mũi hoa sao xuống nền bùn đất ẩm ướt  |
| b09 | 01:19.7–01:28.7 (9.0s) | L19 | Mười cặp xúc tu bên ngoài làm nhiệm vụ dò đường quét rộng, khi phát hiện thứ gì nghi ngờ là thức ăn, nó lập tức điều phối cặp xúc tu số 11 chụp lấy kiểm tra cận cảnh! | **CẶP SỐ 11** · kiểm tra vi mô · L/350 · [0.35, 0.45] | Sơ đồ chiếc mũi sao: 10 cặp xúc tu bên ngoài làm radar quét rộng; cặp xúc tu số 11 ở đáy lập tức chộp lấy con mồi để kiểm tra vi mô. |
| b10 | 01:28.7–01:35.2 (6.5s) | L20 | Chẳng một hạt cát, chẳng một con ấu trùng bọ cánh cứng nào có thể trốn thoát trước chiếc máy quét xúc giác quét từng milimet đất này! |  | Kính hiển vi quét cận cảnh: chẳng một hạt cát hay ấu trùng bọ cánh cứng nào có thể trốn thoát trước chiếc máy quét xúc giác quét từng milimet đất này. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này. |
| b11 | 01:35.2–01:46.8 (11.5s) | L21 | Không những thế, bộ hàm của nó còn trang bị những chiếc răng cửa nhọn hoắt đan chéo vào nhau như chiếc nhíp gắp siêu nhỏ! Ngay khi cặp xúc tu số 11 xác nhận con mồi, chiếc nhíp răng liền phóng ra ngoạm chặt và kéo thẳng con mồi vào họng, |  | Cận cảnh bộ hàm răng cửa sắc nhọn của chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ đan chéo vào nhau |
| b12 | 01:46.8–01:54.0 (7.3s) | L22 | kết hợp với tuyến nước bọt có chất gây tê nhẹ làm con giun đất bất động ngay tức khắc! Đúng là dây chuyền bắt và chế biến thức ăn tự động nhanh nhất thế giới! |  | Tuyến nước bọt của chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ tiết ra chất gây tê nhẹ làm con giun |

### scene03 · 00 HOÀNG HÔN: LẶN SUỐI DƯỚI BĂNG VÀ TUYỆT KỸ NGỬI MÙI BẰNG BONG BÓNG · 99.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.6 (7.6s) | L23 | Bầu trời hoàng hôn buông xuống, đồng hồ chuyển sang mốc 18:00. Đừng nghĩ chuột chũi chỉ biết quanh quẩn đào đất trong bóng tối khô ráo. |  | Đồng hồ chuyển sang 18:00 hoàng hôn rực ánh cam tím trên mặt hồ đầm lầy; anh chàng phóng viên truyền hình 24H hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H đứng bên bờ suối chỉ tay về phía dòng nước chảy. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này. |
| b02 | 00:07.6–00:16.6 (9.0s) | L24 | Tia Chớp Lòng Đất của chúng ta là một vận động viên bơi lội bán thủy sinh cừ khôi, và địa bàn hoạt động buổi chiều tà của gã chuyển thẳng xuống những dòng suối lạnh buốt ven đầm lầy! |  | chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ hóa thân thành vận động viên bơi lội bán thủy sinh cừ k |
| b03 | 00:16.6–00:24.7 (8.1s) | L25 | Hai bàn chân trước to bè như hai mái chèo xẻ nước, chiếc đuôi dày cộp đóng vai trò bánh lái đưa gã lặn sâu xuống đáy nước mò tìm ấu trùng chuồn chuồn và cá nhỏ. |  | chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ bơi lội điêu luyện dưới dòng nước lạnh, hai chân trước  |
| b04 | 00:24.7–00:35.1 (10.4s) | L26 | Nhưng điều làm chấn động toàn bộ giới sinh học thế giới — được công bố trên tạp chí Nature 2006 — là câu hỏi: làm thế nào một loài thú lại có thể đánh hơi tìm mồi dưới nước khi không thể hít nước vào phổi? | **NATURE '06** · phát hiện chấn động · L/350 · [0.35, 0.45] | Bìa bài báo tạp chí Nature năm 2006 mở ra câu hỏi bí ẩn: làm thế nào một loài thú có vú có thể đánh hơi tìm mồi dưới nước. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này. |
| b05 | 00:35.1–00:43.2 (8.1s) | L27 | Báo cáo hiện trường: Camera hồng ngoại dưới nước ghi nhận mẫu vật liên tục thổi những quả bong bóng khí tròn xoe ra khỏi lỗ mũi rồi hít ngược trở lại! |  | Màn hình camera hồng ngoại dưới nước: cô phát thanh viên bản tin trực tiếp hoạt hình đeo tai nghe chỉ vào cảnh chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đe |
| b06 | 00:43.2–00:51.4 (8.2s) | L28 | Quý vị đang chứng kiến một kỳ quan vật lý sinh học độc nhất vô nhị! Chuột Chũi Sao chính là loài động vật có vú đầu tiên trên hành tinh được chứng minh có khả năng ngửi mùi dưới nước! |  | Kỳ quan sinh học: loài thú đầu tiên trên hành tinh được chứng minh có khả năng ngửi mùi dưới nước mà không cần hít nước vào phổi. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này. |
| b07 | 00:51.4–01:02.7 (11.3s) | L29 | Nó thổi những bong bóng khí nhỏ từ mũi chạm vào thức ăn, các phân tử mùi trong nước lập tức khuếch tán bám vào bề mặt bong bóng, và trong chớp mắt, nó hít ngược bong bóng vào khoang mũi để cơ quan khứu giác phân tích mùi vị! |  | Phóng to dưới nước: chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ thổi bong bóng khí chạm vào thức ăn |
| b08 | 01:02.7–01:10.8 (8.1s) | L30 | Tần số thổi và hít lại bong bóng này đạt từ 5-10 lần mỗi giây — nhanh và nhịp nhàng hệt như cách một chú chuột cống hít hà đánh hơi trên cạn! | **5-10 LẦN/S** · thổi hít bong bóng · R/350 · [0.65, 0.48] | Đồ họa nhịp thở bong bóng dưới nước đạt tần số 5-10 lần mỗi giây, so sánh với chú chuột cống đang hít hà đánh hơi trên cạn. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này. |
| b09 | 01:10.8–01:19.7 (8.9s) | L31 | Nhờ chiếc máy thở bong bóng tuần hoàn này, dù đáy suối tối om không nhìn thấy gì, Tia Chớp Lòng Đất vẫn bơi theo dấu vết mùi của con mồi chuẩn xác từng centimet! |  | Dưới đáy suối tối đen như mực: chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ bơi theo luồng phân tử m |
| b10 | 01:19.7–01:31.8 (12.1s) | L32 | Thậm chí vào mùa đông khi mặt nước đầm lầy đóng thành những tảng băng dày cứng ngắc, gã vẫn lặn ngụp dưới băng, thổi những quả bong bóng khí chạm vào mặt dưới của tảng băng để gom mùi hương của tôm tép đang bơi lội! |  | Dưới lớp băng tuyết dày mùa đông: chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ bơi lặn bên dưới tảng |
| b11 | 01:31.8–01:39.9 (8.1s) | L33 | Các nhà vật lý chất lưu thán phục rằng cơ chế bắt dính phân tử mùi qua sức căng bề mặt của bong bóng là một phát kiến tự nhiên siêu việt mà con người chưa từng nghĩ tới! |  | Mô hình vật lý chất lưu: sức căng bề mặt bong bóng khí bắt dính phân tử mùi trong nước; bảng 18:00 Hoàng hôn bật PASS. |

### scene04 · 00 NỬA ĐÊM: CẶP XÚC TU SỐ 11 VÀ BẢN ĐỒ XÚC GIÁC CHIẾM TRỌN VỎ NÃO · 85.0s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.9 (7.9s) | L34 | Đồng hồ điểm 00:00! Rừng đầm lầy chìm trong bóng tối dày đặc, tiếng cú mèo rúc vang trên cành cây báo hiệu giờ săn mồi của những kẻ thù nguy hiểm nhất: |  | Đồng hồ điểm đúng 00:00 nửa đêm; rừng đầm lầy chìm trong bóng đêm đen đặc, con cú mèo mắt phát sáng rình rập trên cành cây khô. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này. |
| b02 | 00:07.9–00:12.3 (4.3s) | L35 | chồn ec-min, rắn nước và chim săn đêm đang rình rập quanh các cửa hầm ngầm. |  | Bên ngoài các cửa hầm ngầm, chồn ec-min và rắn nước lượn lờ săn mồi trong đêm lạnh; nguy hiểm bủa vây tứ phía. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này. |
| b03 | 00:12.3–00:27.1 (14.9s) | L36 | Bên trong lòng đất, Tia Chớp Lòng Đất vẫn miệt mài vận hành cỗ máy thần kinh tinh vi nhất. Khi các nhà khoa học chụp bản đồ quét não bộ của nó, họ phát hiện một hiện tượng giải phẫu làm kinh ngạc toàn ngành thần kinh học: toàn bộ vùng vỏ não cảm giác bản thể của nó hầu như bị chiếc mũi hoa sao chiếm trọn hoàn toàn! |  | Bản đồ quét cộng hưởng từ não bộ của chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ: toàn bộ vùng vỏ n |
| b04 | 00:27.1–00:39.4 (12.3s) | L37 | Đặc biệt nhất là cặp xúc tu ở vị trí thứ 11 — cặp xúc tu nhỏ nhất nằm ở chính giữa phía dưới của bông hoa sao! Cặp xúc tu thứ 11 này hoạt động y hệt như hoàng điểm Fovea trên võng mạc mắt người — tức là vùng có độ phân giải thị giác sắc nét nhất! | **XÚC TU 11** · hoàng điểm xúc giác · R/350 · [0.65, 0.5] | Cận cảnh cặp xúc tu số 11 nhỏ nhất ở đáy chiếc mũi hoa sao, phát sáng màu vàng cam như hoàng điểm võng mạc mắt người. |
| b05 | 00:39.4–00:48.2 (8.8s) | L38 | Khi 20 xúc tu bên ngoài chạm lướt qua phát hiện vật thể khả nghi, chiếc mũi lập tức hướng cặp xúc tu thứ 11 vào kiểm tra cận cảnh với độ phóng đại não bộ lớn gấp nhiều lần! |  | Sơ đồ điều phối xúc giác: khi 20 xúc tu bên ngoài chạm lướt phát hiện vật thể, cặp số 11 lập tức chụp vào kiểm tra cận cảnh với độ phóng đại não bộ tối đa. |
| b06 | 00:48.2–00:57.6 (9.4s) | L39 | Các nghiên cứu giải phẫu thần kinh cho thấy hơn 50% diện tích của vùng não cảm giác bản thể dành trọn vẹn để xử lý thông tin từ chiếc mũi chỉ rộng chưa đầy một centimet này! | **50% VỎ NÃO** · dành riêng cho mũi · L/350 · [0.35, 0.45] | Biểu đồ não bộ: hơn 50% diện tích vỏ não cảm giác bản thể phục vụ cho chiếc mũi rộng chưa đầy 1cm; mô hình người chuột kỳ dị với chiếc mũi khổng lồ. |
| b07 | 00:57.6–01:06.5 (9.0s) | L40 | Nếu vẽ lại cơ thể chuột chũi sao theo tỷ lệ diện tích não bộ điều khiển, chiếc mũi của nó sẽ to đùng bằng cả tòa nhà, còn thân mình và chân tay chỉ bé bằng hạt vừng! |  | Mô hình tỷ lệ Homunculus kỳ dị: chiếc mũi hoa sao của chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ p |
| b08 | 01:06.5–01:15.0 (8.5s) | L41 | Thế nên dù không có mắt để nhìn, thế giới trong đầu của Chuột Chũi Sao lại rực rỡ và chi tiết đến từng milimet qua những bức tranh xúc giác 3D sống động! |  | chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ đào hầm trong đêm, thế giới trong đầu hiện lên như bức  |
| b09 | 01:15.0–01:25.0 (10.0s) | L42 | Nó nhìn thấy thế giới bằng chính chiếc mũi sao của mình, định vị không gian và phát hiện kẻ thù đào đất mò tới từ khoảng cách hàng mét để kịp thời bịt kín ngách hầm tẩu thoát an toàn! |  | chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ phát hiện kẻ thù đang đào đất mò tới từ xa qua sóng run |

### scene05 · 00 RẠNG SÁNG: CƠN ĐÓI LIÊN TỤC VÀ CHIẾC ĐUÔI PHÌNH TO TRỮ MỠ MÙA ĐÔNG · 80.6s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:14.3 (14.3s) | L43 | Bây giờ là 04:00. Nhiệt độ ngoài trời giảm xuống mức đóng băng, hơi lạnh buốt giá bắt đầu luồn vào từng kẽ đất. Lúc này, Tia Chớp Lòng Đất phải đối mặt với kẻ thù nguy hiểm nhất đe dọa sự sống còn của chính mình: Cơn đói cồn cào của cỗ máy chuyển hóa năng lượng siêu tốc! |  | Đồng hồ điểm 04:00 rạng sáng; ngoài trời đóng băng lạnh buốt, hơi sương trắng luồn vào từng kẽ đất nơi chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một ch |
| b02 | 00:14.3–00:28.1 (13.7s) | L44 | Với một cơ thể nhỏ bé 50g nhưng vận động đào bới liên tục với nhịp tim và trao đổi chất cao ngất ngưởng, nó không thể nhịn ăn quá vài giờ đồng hồ. Mỗi ngày, một chú Chuột Chũi Sao phải tiêu thụ lượng thức ăn tương đương từ một nửa cho đến gần bằng 100% trọng lượng cơ thể của chính mình! | **50-100%** · lượng ăn mỗi ngày · R/350 · [0.65, 0.5] | chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ nhỏ bé 50g đứng cạnh chiếc cân đo lượng thức ăn: mỗi ng |
| b03 | 00:28.1–00:32.6 (4.5s) | L45 | Nếu ngừng ăn là pin năng lượng sẽ cạn sạch và cơ thể sẽ hạ thân nhiệt tử vong! |  | Biểu tượng viên pin năng lượng nhấp nháy vạch đỏ cạn kiệt biểu thị mức pin năng lượng khi chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ b |
| b04 | 00:32.6–00:40.3 (7.7s) | L46 | Thế nhưng khi mùa đông tuyết trắng phủ dày cả mét và mặt hồ đóng băng cứng ngắc, làm sao nó sống sót? Hãy nhìn ra phía sau chiếc đuôi của nó: |  | Mặt hồ đóng băng cứng ngắc, tuyết phủ dày cả mét khắp cánh rừng đầm lầy; cái lạnh giá bao trùm vạn vật. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này. |
| b05 | 00:40.3–00:50.2 (9.9s) | L47 | vào mùa thu trù phú, chiếc đuôi của Chuột Chũi Sao phình to gấp ba đến bốn lần kích thước bình thường, biến thành một bình ắc-quy sinh học tích trữ đầy mỡ béo dự trữ năng lượng! |  | Cận cảnh chiếc đuôi của chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ phình to gấp 3-4 lần như bình ắ |
| b06 | 00:50.2–01:04.4 (14.2s) | L48 | Nhờ chiếc đuôi tích mỡ thần kỳ kết hợp với bộ lông nhung không thấm nước dày dặn, gã thản nhiên bơi lặn săn mồi bên dưới lớp băng tuyết mùa đông lạnh thấu xương mà không hề biết đến khái niệm ngủ đông là gì! Đúng là chiến binh bốn mùa bất khuất của thế giới đầm lầy! |  | chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ bơi lội thoải mái dưới lớp băng giá lạnh thấu xương nhờ |
| b07 | 01:04.4–01:14.6 (10.2s) | L49 | Đặc biệt là vào những đợt bão tuyết khắc nghiệt, nhiệt độ dưới lớp băng có thể giảm sâu xuống gần 0°C, nhưng nhiệt độ cơ thể của Tia Chớp Lòng Đất vẫn duy trì ổn định ở 37°C! | **NƯỚC 0°C** · lạnh dưới băng tuyết · L/350 · [0.35, 0.45]<br>**THÂN 37°C** · duy trì ổn định · R/350 · [0.68, 0.45] | Hai chiếc nhiệt kế: nhiệt độ nước dưới băng là 0°C, nhưng nhiệt độ cơ thể chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử n |
| b08 | 01:14.6–01:20.6 (6.0s) | L50 | Toàn bộ mỡ dự trữ trong chiếc đuôi phình to được đốt cháy từng phần để sưởi ấm các cơ quan nội tạng quan trọng nhất! |  | Mô hình nhiệt sinh học: mỡ dự trữ trong chiếc đuôi phình to được đốt cháy từng phần sưởi ấm tim phổi và nội tạng của chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao bi |

### scene06 · CHIẾC ĐỒNG HỒ KHÉP VÒNG VÀ BÓNG ĐEN KIẾN NỔ CẢM TỬ · 68.0s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:04.6 (4.6s) | L51 | Đồng hồ lại điểm 06:00! Tròn 24 giờ nghẹt thở đã trôi qua. |  | Đồng hồ trường quay khép lại tròn 24 giờ điểm đúng 06:00 sáng hôm sau; anh chàng phóng viên truyền hình 24H hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H đứng trước ống kính truyền hình mỉm cười tổng kết phóng sự. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này. |
| b02 | 00:04.6–00:12.4 (7.8s) | L52 | Sương sớm lại giăng kín đầm lầy, và cuộc đua sinh tồn của Tia Chớp Lòng Đất lại khép lại một vòng quay Trái Đất để rồi tiếp tục bắt đầu một ngày mới không ngừng nghỉ. |  | Sương sớm giăng kín đầm lầy, chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ lại bắt đầu một ngày mới đ |
| b03 | 00:12.4–00:25.6 (13.2s) | L53 | Từ một sinh vật mù lòa xấu xí bị xem là dị hợm, Chuột Chũi Sao đã biến chiếc mũi hoa sao thành một tuyệt tác tiến hóa đỉnh cao: ăn mồi trong 0,12 giây, ngửi mùi dưới nước bằng bong bóng và vẽ nên bản đồ thế giới bằng xúc giác kỳ diệu! |  | chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ đứng trên bục vinh danh của thế giới tự nhiên, chiếc mũ |
| b04 | 00:25.6–00:30.6 (4.9s) | L54 | Phóng sự 24 giờ của chúng tôi xin được khép lại tại đây. Còn quý vị khán giả thì sao? |  | anh chàng phóng viên truyền hình 24H hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H mỉm cười chuẩn bị khép lại bản tin thực tế 24 giờ nghẹt thở dưới lòng đầm lầy. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này. |
| b05 | 00:30.6–00:41.7 (11.2s) | L55 | Nếu được sở hữu một siêu năng lực của Tia Chớp Lòng Đất: tốc độ ăn tối nhanh hơn cái chớp mắt không lo trễ giờ, hay khả năng ngửi mùi dưới nước bằng bong bóng, quý vị chọn cái nào? Hãy để lại bình luận bên dưới nhé! |  | Hai bàn cân lựa chọn: BÊN TRÁI biểu tượng tốc độ ăn mồi 0,12 giây; BÊN PHẢI biểu tượng ngửi mùi dưới nước bằng bong bóng, khán giả giơ thẻ bình chọn. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này. |
| b06 | 00:41.7–00:52.0 (10.3s) | L56 | Và bây giờ, bản tin đặc biệt xin được bật mí bóng đen bí ẩn của tập tiếp theo! Rời khỏi đầm lầy Bắc Mỹ, chúng ta sẽ bước vào rừng mưa nhiệt đới Đông Nam Á để chứng kiến một đội quân đế chế khét tiếng tàn bạo! |  | Ống kính máy quay chuyển sang rừng mưa nhiệt đới Đông Nam Á tăm tối bí hiểm với bóng cây rậm rạp. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này. |
| b07 | 00:52.0–01:03.1 (11.1s) | L57 | Những chiến binh bé nhỏ mang trong mình lòng trung thành tuyệt đối với bà trùm: khi kẻ thù tấn công tổ, chúng sẵn sàng tự gồng cơ bụng nổ tung cơ thể mình như những quả bom cảm tử, phun ra dòng chất độc màu vàng dính chặt kẻ thù cùng chết chung! |  | Một sinh vật bí ẩn được vẽ hoàn toàn bằng BÓNG ĐEN ĐẶC TUYỀN (solid black silhouette) hình chú kiến thợ nhỏ bé đang gồng cơ bụng nổ tung cơ thể phát ra tia chớp nổ tung; kèm dấu hỏi chấm vàng to tướng; KHÔNG vẽ mắt mũi lông. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này. |
| b08 | 01:03.1–01:08.0 (4.9s) | L58 | Đố các bạn biết bóng đen bí ẩn kỳ sau là loài vật nào? Hãy đoán ngay ở phần bình luận nhé! |  | Chiếc BÓNG ĐEN ĐẶC TUYỀN bí ẩn của loài kiến nổ cảm tử nằm giữa ba dấu hỏi chấm lớn màu vàng cam lấp lánh mời gọi khán giả bình luận đoán tên con vật tập sau. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này. |

## 5. Phân cảnh Shorts — từng beat

Banner: **ĂN MỒI TRONG 0,12 GIÂY / & NGỬI DƯỚI NƯỚC?!** · giọng 46.6s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Sinh vật mù lòa này ăn tối nhanh đến mức khó tin: |  |
| s02 | 00:03.2 | S02 | chỉ mất đúng 0,12 giây để nhận diện và nuốt chửng con mồi, nhanh hơn cả một cái chớp mắt của con người! | **0,12 GIÂY** · ăn mồi siêu tốc · R/560 · [0.6, 0.48] |
| s03 | 00:09.7 | S03 | Xin giới thiệu Chuột Chũi Sao, cỗ máy săn mồi dài 20cm sống dưới các đầm lầy Bắc Mỹ. | **20 CM** · chiều dài cơ thể · R/720 · [0.62, 0.5] |
| s04 | 00:15.6 | S04 | Hai mắt của nó thoái hóa mù tịt, |  |
| s05 | 00:17.2 | S05 | nhưng trên mũi lại mọc ra 22 xúc tu thịt màu hồng xòe rộng như một bông hoa sao biển! | **22 XÚC TU** · mũi hoa sao · L/620 · [0.45, 0.52] |
| s06 | 00:22.8 | S06 | Chiếc mũi quái đản này chứa hơn 25.000 thụ thể cảm giác, gõ xuống bùn đất tới 12 vị trí mỗi giây để dò mồi! | **25.000 THỂ** · 12 vị trí mỗi giây · R/650 · [0.6, 0.5] |
| s07 | 00:29.3 | S07 | Thậm chí khi lặn xuống nước, nó là loài thú duy nhất biết thổi những quả bong bóng khí ra khỏi mũi |  |
| s08 | 00:34.1 | S08 | rồi hít ngược trở lại để ngửi mùi con mồi dưới đáy suối! |  |
| s09 | 00:37.2 | S09 | Bộ não của nó chỉ mất đúng 8 mili-giây để quyết định ăn hay bỏ! | **8 MS** · phân tích não bộ · L/680 · [0.4, 0.5] |
| s10 | 00:41.0 | S10 | Một tia chớp lòng đất với chiếc mũi quái vật ngoài hành tinh sở hữu tốc độ săn mồi nhanh nhất hành tinh! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bây giờ là 06:00! Chúng tôi đang có mặt trực tiếp tại một đầm lầy ẩm ướt vùng Đông Bắc Bắc Mỹ. Sương mù mờ ảo giăng kín mặt đất,". Bố cục: Bầu trời sáng sớm đầm lầy sương mù mờ ảo: chiếc đồng hồ kim lớn điểm đúng 06:00 sáng; anh chàng phóng viên truyền hình 24H hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H cầm micro phát sóng trực tiếp bên bãi bùn ẩm ướt. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tiếng đồng hồ tích tắc báo hiệu cuộc đua sinh tồn nghẹt thở 24 giờ chính thức khai hỏa! Dưới lớp bùn đất nhão nhoẹt, mặt đất bắt đầu rung chuyển nhẹ...". Bố cục: Đồng hồ cát 24 giờ đếm ngược phát sáng cam; mặt đất đầm lầy ẩm ướt bắt đầu rung chuyển nhẹ có những vết nứt nhỏ. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một cỗ máy khoan đất tí hon chỉ nặng khoảng 50g,". Bố cục: Mặt đất ẩm ướt đùn lên một ụ đất tròn; từ dưới hang tối, một cỗ máy khoan đất tí hon nặng 50g với bộ lông nhung đen trồi đầu lên mặt đất.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "dài chưa đầy 15-20cm, bỗng chốc đùn đất trồi lên!". Bố cục: Ở GIỮA chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ đứng cạnh chiếc thước đo chiều cao màu vàng 15-20cm của phóng viên hiện trường.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo phóng viên hiện trường: Mục tiêu vừa lộ diện nhưng trên mặt nó không có mắt, mà gắn một bông hoa thịt màu đỏ hồng đang ngoe nguẩy dữ dội!". Bố cục: Màn hình trường quay: cô phát thanh viên bản tin trực tiếp hoạt hình đeo tai nghe chỉ tay vào hình ảnh phóng to cận cảnh chiếc mũi đỏ hồng xòe ra 22 xúc tu đang ngoe nguẩy dữ dội. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Quý vị khán giả của đài truyền hình Vẽ Chuyện Hoang Dã đừng vội hoảng sợ! Đây không phải quái vật ngoài hành tinh xâm lăng Trái Đất, mà là Chuột Chũi Sao, loài động vật có vú sở hữu cơ quan cảm giác kỳ dị bậc nhất hành tinh!". Bố cục: chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ đứng trên gò đất đầm lầy, chiếc mũi sao biển hồng rung rinh tỏa sáng, hai chân trước xòe rộng như hai chiếc xẻng đào đất ngộ nghĩnh.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hai mắt của nó thoái hóa mù tịt, hai tai không có vành, nhưng ngay trên đầu mũi lại xòe ra 22 xúc tu thịt màu hồng tươi rung rinh liên tục như một bông hoa sao biển!". Bố cục: Cận cảnh đầu của chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ: hai mắt thoái hóa thành hai đốm nhỏ xíu mờ đục, hai tai không có vành, mũi xòe 22 xúc tu rực rỡ như bông hoa sao biển.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong bản tin trực tiếp hôm nay, chúng tôi gọi thẳng tên nó bằng biệt danh: Tia Chớp Lòng Đất!". Bố cục: chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ hóa thân thành siêu anh hùng đeo chiếc đồng hồ bấm giờ cam, xung quanh bùng nổ tia chớp điện quang với danh hiệu Tia Chớp Lòng Đất.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Điều gì đã khiến một sinh vật nhỏ bé mù lòa lại được Tổ chức Kỷ lục Thế giới Guinness phong tặng danh hiệu cỗ máy săn mồi nhanh nhất hành tinh? Chiếc mũi sao kia vận hành thần tốc ra sao để giúp nó sinh tồn suốt một ngày dài đói khát?". Bố cục: Cuốn sách Kỷ lục Thế giới Guinness mở ra biểu tượng cúp vàng trao cho chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ danh hiệu cỗ máy săn mồi nhanh nhất hành tinh.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy cùng trường quay của chúng tôi theo sát từng mốc thời gian trong ngày của Tia Chớp Lòng Đất!". Bố cục: anh chàng phóng viên truyền hình 24H hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H chỉ vào chiếc đồng hồ 24 giờ đang chạy tích tắc; chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ chui tọt xuống đường hầm ngầm bắt đầu cuộc đua sinh tồn.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đồng hồ điểm 12:00! Ánh nắng mặt trời rọi thẳng đứng nhưng dưới lòng địa đạo tăm tối, Tia Chớp Lòng Đất đang bắt đầu bữa tiệc trưa tốc độ ánh sáng! Hãy chuẩn bị tinh thần theo dõi camera quay chậm 1.000 khung hình mỗi giây, vì mắt thường của quý vị hoàn toàn bất lực trước vận tốc này!". Bố cục: Đồng hồ trường quay điểm đúng 12:00 trưa; anh chàng phóng viên truyền hình 24H hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H đang đứng cạnh máy quay tốc độ cao 1.000 khung hình mỗi giây chiếu vào lòng địa đạo tăm tối. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giáo sư Kenneth Catania tại Đại học Vanderbilt đã đưa chuột chũi sao vào phòng thí nghiệm với máy quay tốc độ cao và phát hiện một kỷ lục thế giới kinh hoàng:". Bố cục: Phòng thí nghiệm Đại học Vanderbilt: Giáo sư Kenneth Catania quan sát màn hình camera quay chậm cận cảnh chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ đang chạm mũi vào con mồi. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "thời gian trung bình để nó dùng mũi chạm vào con mồi, nhận diện ăn được hay không, rồi há miệng ngoạm nuốt chửng... chỉ mất đúng 120 mili-giây, tức là 0,12 giây!". Bố cục: Đồng hồ bấm giờ điện tử dừng lại ở con số 120 mili-giây (0,12 giây) bốc khói: chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ chạm mũi nhận diện và nuốt chửng một con giun đất cực nhanh.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Quý vị có biết một cái chớp mắt của con người mất bao lâu không? Mất khoảng 300-400 mili-giây! Nghĩa là trong lúc quý vị vừa chớp mắt một cái nhẹ tênh, chú Chuột Chũi Sao đã kịp chén sạch sành sanh ba con giun liên tiếp!". Bố cục: Mắt người đang chớp một cái mất 300-400 mili-giây; ở bên cạnh chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ đã kịp nuốt chửng ba con giun đất liên tiếp trong cùng một khoảng thời gian.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thậm chí bộ não của nó chỉ mất đúng 8 mili-giây để phân tích tín hiệu thần kinh và đưa ra quyết định ăn hay bỏ — nhanh ngang ngửa tốc độ xử lý của vi mạch máy tính tối tân!". Bố cục: Sơ đồ não bộ phát xung điện thần kinh siêu tốc chỉ trong 8 mili-giây đưa ra quyết định ăn mồi, ngang ngửa tốc độ xử lý của vi mạch máy tính. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bí mật đằng sau tốc độ bàn thờ này nằm trọn trên chiếc mũi hoa sao: trên 22 chiếc xúc tu thịt nhỏ xíu chứa tới hơn 25.000 thụ thể xúc giác siêu nhạy gọi là thụ thể Eimer,". Bố cục: Kính hiển vi phóng to chiếc mũi hoa sao: 22 xúc tu thịt chứa hơn 25.000 thụ thể Eimer hình vòm nhỏ li ti và 100.000 sợi dây thần kinh dày đặc. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "được nuôi dưỡng bởi hơn 100.000 sợi dây thần kinh — tức là dày đặc gấp 6 lần toàn bộ dây thần kinh trên cả hai bàn tay của một con người trưởng thành!". Bố cục: So sánh hệ thần kinh: chiếc mũi hoa sao nhỏ bé có mật độ dây thần kinh dày đặc gấp 6 lần toàn bộ dây thần kinh trên cả hai bàn tay của một con người trưởng thành. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi đi săn trong bóng tối mù mịt, chiếc mũi của Tia Chớp Lòng Đất gõ liên hồi xuống bùn đất với tần số khó tin: chạm tới 12 vị trí khác nhau trong vỏn vẹn một giây!". Bố cục: chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ gõ liên hồi chiếc mũi hoa sao xuống nền bùn đất ẩm ướt với tốc độ chạm 12 vị trí khác nhau trong đúng một giây.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mười cặp xúc tu bên ngoài làm nhiệm vụ dò đường quét rộng, khi phát hiện thứ gì nghi ngờ là thức ăn, nó lập tức điều phối cặp xúc tu số 11 chụp lấy kiểm tra cận cảnh!". Bố cục: Sơ đồ chiếc mũi sao: 10 cặp xúc tu bên ngoài làm radar quét rộng; cặp xúc tu số 11 ở đáy lập tức chộp lấy con mồi để kiểm tra vi mô.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chẳng một hạt cát, chẳng một con ấu trùng bọ cánh cứng nào có thể trốn thoát trước chiếc máy quét xúc giác quét từng milimet đất này!". Bố cục: Kính hiển vi quét cận cảnh: chẳng một hạt cát hay ấu trùng bọ cánh cứng nào có thể trốn thoát trước chiếc máy quét xúc giác quét từng milimet đất này. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không những thế, bộ hàm của nó còn trang bị những chiếc răng cửa nhọn hoắt đan chéo vào nhau như chiếc nhíp gắp siêu nhỏ! Ngay khi cặp xúc tu số 11 xác nhận con mồi, chiếc nhíp răng liền phóng ra ngoạm chặt và kéo thẳng con mồi vào họng,". Bố cục: Cận cảnh bộ hàm răng cửa sắc nhọn của chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ đan chéo vào nhau như chiếc nhíp gắp siêu nhỏ, ngoạm chặt con giun đất kéo tuột vào họng.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "kết hợp với tuyến nước bọt có chất gây tê nhẹ làm con giun đất bất động ngay tức khắc! Đúng là dây chuyền bắt và chế biến thức ăn tự động nhanh nhất thế giới!". Bố cục: Tuyến nước bọt của chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ tiết ra chất gây tê nhẹ làm con giun đất bất động ngay tức khắc; bảng 12:00 Trưa bật PASS.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bầu trời hoàng hôn buông xuống, đồng hồ chuyển sang mốc 18:00. Đừng nghĩ chuột chũi chỉ biết quanh quẩn đào đất trong bóng tối khô ráo.". Bố cục: Đồng hồ chuyển sang 18:00 hoàng hôn rực ánh cam tím trên mặt hồ đầm lầy; anh chàng phóng viên truyền hình 24H hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H đứng bên bờ suối chỉ tay về phía dòng nước chảy. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tia Chớp Lòng Đất của chúng ta là một vận động viên bơi lội bán thủy sinh cừ khôi, và địa bàn hoạt động buổi chiều tà của gã chuyển thẳng xuống những dòng suối lạnh buốt ven đầm lầy!". Bố cục: chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ hóa thân thành vận động viên bơi lội bán thủy sinh cừ khôi, lặn ngụp xuống dòng suối lạnh buốt ven đầm lầy săn mồi buổi chiều tà.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hai bàn chân trước to bè như hai mái chèo xẻ nước, chiếc đuôi dày cộp đóng vai trò bánh lái đưa gã lặn sâu xuống đáy nước mò tìm ấu trùng chuồn chuồn và cá nhỏ.". Bố cục: chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ bơi lội điêu luyện dưới dòng nước lạnh, hai chân trước to bè quạt nước như mái chèo, chiếc đuôi dày đóng vai trò bánh lái.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng điều làm chấn động toàn bộ giới sinh học thế giới — được công bố trên tạp chí Nature 2006 — là câu hỏi: làm thế nào một loài thú lại có thể đánh hơi tìm mồi dưới nước khi không thể hít nước vào phổi?". Bố cục: Bìa bài báo tạp chí Nature năm 2006 mở ra câu hỏi bí ẩn: làm thế nào một loài thú có vú có thể đánh hơi tìm mồi dưới nước. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo hiện trường: Camera hồng ngoại dưới nước ghi nhận mẫu vật liên tục thổi những quả bong bóng khí tròn xoe ra khỏi lỗ mũi rồi hít ngược trở lại!". Bố cục: Màn hình camera hồng ngoại dưới nước: cô phát thanh viên bản tin trực tiếp hoạt hình đeo tai nghe chỉ vào cảnh chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ liên tục thổi những quả bong bóng khí tròn xoe ra khỏi mũi rồi hít lại.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Quý vị đang chứng kiến một kỳ quan vật lý sinh học độc nhất vô nhị! Chuột Chũi Sao chính là loài động vật có vú đầu tiên trên hành tinh được chứng minh có khả năng ngửi mùi dưới nước!". Bố cục: Kỳ quan sinh học: loài thú đầu tiên trên hành tinh được chứng minh có khả năng ngửi mùi dưới nước mà không cần hít nước vào phổi. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó thổi những bong bóng khí nhỏ từ mũi chạm vào thức ăn, các phân tử mùi trong nước lập tức khuếch tán bám vào bề mặt bong bóng, và trong chớp mắt, nó hít ngược bong bóng vào khoang mũi để cơ quan khứu giác phân tích mùi vị!". Bố cục: Phóng to dưới nước: chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ thổi bong bóng khí chạm vào thức ăn, phân tử mùi bám vào màng bong bóng rồi được hít ngược vào khoang mũi.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tần số thổi và hít lại bong bóng này đạt từ 5-10 lần mỗi giây — nhanh và nhịp nhàng hệt như cách một chú chuột cống hít hà đánh hơi trên cạn!". Bố cục: Đồ họa nhịp thở bong bóng dưới nước đạt tần số 5-10 lần mỗi giây, so sánh với chú chuột cống đang hít hà đánh hơi trên cạn. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhờ chiếc máy thở bong bóng tuần hoàn này, dù đáy suối tối om không nhìn thấy gì, Tia Chớp Lòng Đất vẫn bơi theo dấu vết mùi của con mồi chuẩn xác từng centimet!". Bố cục: Dưới đáy suối tối đen như mực: chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ bơi theo luồng phân tử mùi của con mồi chuẩn xác từng centimet nhờ chiếc máy thở bong bóng tuần hoàn.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thậm chí vào mùa đông khi mặt nước đầm lầy đóng thành những tảng băng dày cứng ngắc, gã vẫn lặn ngụp dưới băng, thổi những quả bong bóng khí chạm vào mặt dưới của tảng băng để gom mùi hương của tôm tép đang bơi lội!". Bố cục: Dưới lớp băng tuyết dày mùa đông: chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ bơi lặn bên dưới tảng băng, thổi bong bóng chạm vào mặt dưới lớp băng để gom mùi hương của tôm cá.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà vật lý chất lưu thán phục rằng cơ chế bắt dính phân tử mùi qua sức căng bề mặt của bong bóng là một phát kiến tự nhiên siêu việt mà con người chưa từng nghĩ tới!". Bố cục: Mô hình vật lý chất lưu: sức căng bề mặt bong bóng khí bắt dính phân tử mùi trong nước; bảng 18:00 Hoàng hôn bật PASS.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đồng hồ điểm 00:00! Rừng đầm lầy chìm trong bóng tối dày đặc, tiếng cú mèo rúc vang trên cành cây báo hiệu giờ săn mồi của những kẻ thù nguy hiểm nhất:". Bố cục: Đồng hồ điểm đúng 00:00 nửa đêm; rừng đầm lầy chìm trong bóng đêm đen đặc, con cú mèo mắt phát sáng rình rập trên cành cây khô. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chồn ec-min, rắn nước và chim săn đêm đang rình rập quanh các cửa hầm ngầm.". Bố cục: Bên ngoài các cửa hầm ngầm, chồn ec-min và rắn nước lượn lờ săn mồi trong đêm lạnh; nguy hiểm bủa vây tứ phía. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bên trong lòng đất, Tia Chớp Lòng Đất vẫn miệt mài vận hành cỗ máy thần kinh tinh vi nhất. Khi các nhà khoa học chụp bản đồ quét não bộ của nó, họ phát hiện một hiện tượng giải phẫu làm kinh ngạc toàn ngành thần kinh học: toàn bộ vùng vỏ não cảm giác bản thể của nó hầu như bị chiếc mũi hoa sao chiếm trọn hoàn toàn!". Bố cục: Bản đồ quét cộng hưởng từ não bộ của chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ: toàn bộ vùng vỏ não cảm giác bản thể sáng rực rỡ hình chiếc mũi hoa sao. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đặc biệt nhất là cặp xúc tu ở vị trí thứ 11 — cặp xúc tu nhỏ nhất nằm ở chính giữa phía dưới của bông hoa sao! Cặp xúc tu thứ 11 này hoạt động y hệt như hoàng điểm Fovea trên võng mạc mắt người — tức là vùng có độ phân giải thị giác sắc nét nhất!". Bố cục: Cận cảnh cặp xúc tu số 11 nhỏ nhất ở đáy chiếc mũi hoa sao, phát sáng màu vàng cam như hoàng điểm võng mạc mắt người.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi 20 xúc tu bên ngoài chạm lướt qua phát hiện vật thể khả nghi, chiếc mũi lập tức hướng cặp xúc tu thứ 11 vào kiểm tra cận cảnh với độ phóng đại não bộ lớn gấp nhiều lần!". Bố cục: Sơ đồ điều phối xúc giác: khi 20 xúc tu bên ngoài chạm lướt phát hiện vật thể, cặp số 11 lập tức chụp vào kiểm tra cận cảnh với độ phóng đại não bộ tối đa.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nghiên cứu giải phẫu thần kinh cho thấy hơn 50% diện tích của vùng não cảm giác bản thể dành trọn vẹn để xử lý thông tin từ chiếc mũi chỉ rộng chưa đầy một centimet này!". Bố cục: Biểu đồ não bộ: hơn 50% diện tích vỏ não cảm giác bản thể phục vụ cho chiếc mũi rộng chưa đầy 1cm; mô hình người chuột kỳ dị với chiếc mũi khổng lồ.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu vẽ lại cơ thể chuột chũi sao theo tỷ lệ diện tích não bộ điều khiển, chiếc mũi của nó sẽ to đùng bằng cả tòa nhà, còn thân mình và chân tay chỉ bé bằng hạt vừng!". Bố cục: Mô hình tỷ lệ Homunculus kỳ dị: chiếc mũi hoa sao của chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ phình to khổng lồ bằng cả tòa nhà, trong khi thân hình và chân tay teo nhỏ tí hon như hạt vừng.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thế nên dù không có mắt để nhìn, thế giới trong đầu của Chuột Chũi Sao lại rực rỡ và chi tiết đến từng milimet qua những bức tranh xúc giác 3D sống động!". Bố cục: chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ đào hầm trong đêm, thế giới trong đầu hiện lên như bức tranh 3D sống động từng hạt đất và ngách hầm.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó nhìn thấy thế giới bằng chính chiếc mũi sao của mình, định vị không gian và phát hiện kẻ thù đào đất mò tới từ khoảng cách hàng mét để kịp thời bịt kín ngách hầm tẩu thoát an toàn!". Bố cục: chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ phát hiện kẻ thù đang đào đất mò tới từ xa qua sóng rung chấn của chiếc mũi hoa sao, kịp thời lấp kín ngách hầm tẩu thoát an toàn; bảng 00:00 Nửa đêm bật PASS.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bây giờ là 04:00. Nhiệt độ ngoài trời giảm xuống mức đóng băng, hơi lạnh buốt giá bắt đầu luồn vào từng kẽ đất. Lúc này, Tia Chớp Lòng Đất phải đối mặt với kẻ thù nguy hiểm nhất đe dọa sự sống còn của chính mình: Cơn đói cồn cào của cỗ máy chuyển hóa năng lượng siêu tốc!". Bố cục: Đồng hồ điểm 04:00 rạng sáng; ngoài trời đóng băng lạnh buốt, hơi sương trắng luồn vào từng kẽ đất nơi chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ đang đói cồn cào.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Với một cơ thể nhỏ bé 50g nhưng vận động đào bới liên tục với nhịp tim và trao đổi chất cao ngất ngưởng, nó không thể nhịn ăn quá vài giờ đồng hồ. Mỗi ngày, một chú Chuột Chũi Sao phải tiêu thụ lượng thức ăn tương đương từ một nửa cho đến gần bằng 100% trọng lượng cơ thể của chính mình!". Bố cục: chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ nhỏ bé 50g đứng cạnh chiếc cân đo lượng thức ăn: mỗi ngày phải ăn lượng thức ăn bằng 50% đến 100% trọng lượng cơ thể.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu ngừng ăn là pin năng lượng sẽ cạn sạch và cơ thể sẽ cạn kiệt năng lượng!". Bố cục: Biểu tượng viên pin năng lượng nhấp nháy vạch đỏ cạn kiệt biểu thị mức pin năng lượng khi chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ ngừng nạp thức ăn trong vài giờ. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thế nhưng khi mùa đông tuyết trắng phủ dày cả mét và mặt hồ đóng băng cứng ngắc, làm sao nó sống sót? Hãy nhìn ra phía sau chiếc đuôi của nó:". Bố cục: Mặt hồ đóng băng cứng ngắc, tuyết phủ dày cả mét khắp cánh rừng đầm lầy; cái lạnh giá bao trùm vạn vật. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "vào mùa thu trù phú, chiếc đuôi của Chuột Chũi Sao phình to gấp ba đến bốn lần kích thước bình thường, biến thành một bình ắc-quy sinh học tích trữ đầy mỡ béo dự trữ năng lượng!". Bố cục: Cận cảnh chiếc đuôi của chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ phình to gấp 3-4 lần như bình ắc quy sinh học màu vàng tích trữ đầy mỡ béo dự trữ năng lượng mùa đông.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhờ chiếc đuôi tích mỡ thần kỳ kết hợp với bộ lông nhung không thấm nước dày dặn, gã thản nhiên bơi lặn săn mồi bên dưới lớp băng tuyết mùa đông lạnh thấu xương mà không hề biết đến khái niệm ngủ đông là gì! Đúng là chiến binh bốn mùa bất khuất của thế giới đầm lầy!". Bố cục: chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ bơi lội thoải mái dưới lớp băng giá lạnh thấu xương nhờ bộ lông nhung không thấm nước và chiếc đuôi dự trữ mỡ ấm áp.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đặc biệt là vào những đợt bão tuyết khắc nghiệt, nhiệt độ dưới lớp băng có thể giảm sâu xuống gần 0°C, nhưng nhiệt độ cơ thể của Tia Chớp Lòng Đất vẫn duy trì ổn định ở 37°C!". Bố cục: Hai chiếc nhiệt kế: nhiệt độ nước dưới băng là 0°C, nhưng nhiệt độ cơ thể chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ vẫn duy trì 37°C ấm áp.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Toàn bộ mỡ dự trữ trong chiếc đuôi phình to được đốt cháy từng phần để sưởi ấm các cơ quan nội tạng quan trọng nhất!". Bố cục: Mô hình nhiệt sinh học: mỡ dự trữ trong chiếc đuôi phình to được đốt cháy từng phần sưởi ấm tim phổi và nội tạng của chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ; bảng 04:00 Rạng sáng bật PASS.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đồng hồ lại điểm 06:00! Tròn 24 giờ nghẹt thở đã trôi qua.". Bố cục: Đồng hồ trường quay khép lại tròn 24 giờ điểm đúng 06:00 sáng hôm sau; anh chàng phóng viên truyền hình 24H hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H đứng trước ống kính truyền hình mỉm cười tổng kết phóng sự. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sương sớm lại giăng kín đầm lầy, và cuộc đua sinh tồn của Tia Chớp Lòng Đất lại khép lại một vòng quay Trái Đất để rồi tiếp tục bắt đầu một ngày mới không ngừng nghỉ.". Bố cục: Sương sớm giăng kín đầm lầy, chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ lại bắt đầu một ngày mới đào hầm săn mồi không ngừng nghỉ.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Từ một sinh vật mù lòa xấu xí bị xem là dị hợm, Chuột Chũi Sao đã biến chiếc mũi hoa sao thành một tuyệt tác tiến hóa đỉnh cao: ăn mồi trong 0,12 giây, ngửi mùi dưới nước bằng bong bóng và vẽ nên bản đồ thế giới bằng xúc giác kỳ diệu!". Bố cục: chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ đứng trên bục vinh danh của thế giới tự nhiên, chiếc mũi hoa sao 22 xúc tu rực rỡ lấp lánh như chiếc vương miện giác quan.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Phóng sự 24 giờ của chúng tôi xin được khép lại tại đây. Còn quý vị khán giả thì sao?". Bố cục: anh chàng phóng viên truyền hình 24H hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H mỉm cười chuẩn bị khép lại bản tin thực tế 24 giờ nghẹt thở dưới lòng đầm lầy. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu được sở hữu một siêu năng lực của Tia Chớp Lòng Đất: tốc độ ăn tối nhanh hơn cái chớp mắt không lo trễ giờ, hay khả năng ngửi mùi dưới nước bằng bong bóng, quý vị chọn cái nào? Hãy để lại bình luận bên dưới nhé!". Bố cục: Hai bàn cân lựa chọn: BÊN TRÁI biểu tượng tốc độ ăn mồi 0,12 giây; BÊN PHẢI biểu tượng ngửi mùi dưới nước bằng bong bóng, khán giả giơ thẻ bình chọn. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và bây giờ, bản tin đặc biệt xin được bật mí bóng đen bí ẩn của tập tiếp theo! Rời khỏi đầm lầy Bắc Mỹ, chúng ta sẽ bước vào rừng mưa nhiệt đới Đông Nam Á để chứng kiến một đội quân đế chế khét tiếng tàn bạo!". Bố cục: Ống kính máy quay chuyển sang rừng mưa nhiệt đới Đông Nam Á tăm tối bí hiểm với bóng cây rậm rạp. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này.
```
</details>

<details><summary>L57</summary>

```text
HÌNH L57 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Những chiến binh bé nhỏ mang trong mình lòng trung thành tuyệt đối với bà trùm: khi kẻ thù tấn công tổ, chúng sẵn sàng tự gồng cơ bụng nổ tung cơ thể mình như những quả bom cảm tử, phun ra dòng chất độc màu vàng dính chặt kẻ thù cùng chết chung!". Bố cục: Một sinh vật bí ẩn được vẽ hoàn toàn bằng BÓNG ĐEN ĐẶC TUYỀN (solid black silhouette) hình chú kiến thợ nhỏ bé đang gồng cơ bụng nổ tung cơ thể phát ra tia chớp nổ tung; kèm dấu hỏi chấm vàng to tướng; KHÔNG vẽ mắt mũi lông. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này.
```
</details>

<details><summary>L58</summary>

```text
HÌNH L58 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đố các bạn biết bóng đen bí ẩn kỳ sau là loài vật nào? Hãy đoán ngay ở phần bình luận nhé!". Bố cục: Chiếc BÓNG ĐEN ĐẶC TUYỀN bí ẩn của loài kiến nổ cảm tử nằm giữa ba dấu hỏi chấm lớn màu vàng cam lấp lánh mời gọi khán giả bình luận đoán tên con vật tập sau. KHÔNG có chú chuột chũi sao mũi hoa hồng trong cảnh này.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Sinh vật mù lòa này ăn tối nhanh đến mức khó tin:". Bố cục: Khung dọc: chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ nhỏ bé mù lòa đang đào bới dưới bùn đầm lầy, chuẩn bị cho bữa ăn tối thần tốc.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "chỉ mất đúng 0,12 giây để nhận diện và nuốt chửng con mồi, nhanh hơn cả một cái chớp mắt của con người!". Bố cục: Khung dọc: chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ chạm mũi hoa sao vào con mồi, chiếc đồng hồ điện tử đếm 0,12 giây bốc khói nuốt chửng con giun đất nhanh hơn chớp mắt.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Xin giới thiệu Chuột Chũi Sao, cỗ máy săn mồi dài 20cm sống dưới các đầm lầy Bắc Mỹ.". Bố cục: chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ mập mạp bơi lội trên bãi bùn ẩm ướt, chiếc thước đo chiều cao màu vàng 20cm dựng thẳng đứng bên cạnh.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Hai mắt của nó thoái hóa mù tịt,". Bố cục: Cận cảnh khung dọc: hai mắt thoái hóa mờ đục hoàn toàn của chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "nhưng trên mũi lại mọc ra 22 xúc tu thịt màu hồng xòe rộng như một bông hoa sao biển!". Bố cục: Cận cảnh khung dọc: chiếc mũi xòe 22 xúc tu màu hồng tươi rực rỡ như bông hoa sao biển.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Chiếc mũi sao biển kỳ thú này chứa hơn 25.000 thụ thể cảm giác, gõ xuống bùn đất tới 12 vị trí mỗi giây để dò mồi!". Bố cục: Kính hiển vi phóng to 25.000 thụ thể Eimer trên xúc tu, chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra 22 tia xúc tu màu hồng nhạt ngộ nghĩnh như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ gõ mũi xuống bùn đất 12 vị trí mỗi giây để quét tìm con mồi.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Thậm chí khi lặn xuống nước, nó là loài thú duy nhất biết thổi những quả bong bóng khí ra khỏi mũi". Bố cục: chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ lặn dưới nước suối, liên tục thổi các quả bong bóng khí chạm vào thức ăn.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "rồi hít ngược trở lại để ngửi mùi con mồi dưới đáy suối!". Bố cục: chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ hít ngược bong bóng khí vào khoang mũi để ngửi mùi con mồi dưới đáy suối.
```
</details>

<details><summary>S09</summary>

```text
HÌNH S09 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Bộ não của nó chỉ mất đúng 8 mili-giây để quyết định ăn hay bỏ!". Bố cục: Đồ họa não bộ phát sáng xung điện thần kinh chỉ mất đúng 8 mili-giây để đưa ra quyết định ăn hay bỏ.
```
</details>

<details><summary>S10</summary>

```text
HÌNH S10 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chuột Chũi Sao lông đen nhung, mũi hoa sao 22 xúc tu hồng, đồng hồ bấm giờ cam; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Một tia chớp lòng đất với chiếc mũi quái vật ngoài hành tinh sở hữu tốc độ săn mồi nhanh nhất hành tinh!". Bố cục: Chân dung chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ ngầu lòi giữa tia chớp điện quang, 22 xúc tu mũi sao phát sáng rực rỡ, đeo chiếc đồng hồ cam tự hào kỷ lục Guinness.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/58 của video YouTube về Chuột Chũi Sao). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ. Nhân vật phụ cố định: anh chàng phóng viên truyền hình 24H hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H; cô phát thanh viên bản tin trực tiếp hoạt hình đeo tai nghe. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/10 của video YouTube Shorts về Chuột Chũi Sao). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Chuột Chũi Sao (Condylura cristata) hoạt hình lông màu đen nhung mượt mà, thân hình mập mạp mũm mĩm, hai chân trước to bè hình mái chèo xẻ nước với móng vuốt đào đất khỏe khoắn, hai mắt nhỏ mờ đục ngộ nghĩnh, đầu mũi xòe ra hai mươi hai chiếc xúc tu thịt màu hồng tươi rực rỡ như một bông hoa sao biển, đeo một chiếc đồng hồ bấm giờ điện tử nhỏ màu cam trên cổ. Nhân vật phụ: anh chàng phóng viên truyền hình 24H hoạt hình mặc áo khoác dã ngoại màu be, tay cầm micro có logo 24H. 
```
</details>

## 7. SEO

- **title:** Cỗ Máy Mù Lòa Ăn Mồi Trong 0,12 Giây & Ngửi Mùi Dưới Nước?!
- **hook_paragraph:** Chuột Chũi Sao (Condylura cristata) nắm giữ Kỷ lục Guinness động vật có vú ăn mồi nhanh nhất hành tinh: chỉ mất 0,12 giây (120 mili-giây) để nuốt chửng con mồi nhờ chiếc mũi 22 xúc tu chứa 25.000 thụ thể Eimer và khả năng thổi bong bóng ngửi mùi dưới nước!
- **question:** Nếu được sở hữu 1 năng lực của Chuột Chũi Sao: tốc độ ăn mồi trong 0,12 giây hay kỹ năng thổi bong bóng ngửi mùi dưới nước, bạn chọn cái nào? Và đoán xem bóng đen tập sau là loài nào?
- **next_teaser:** Bóng đen quân đoàn cảm tử: những chiến binh tự kích nổ tung cơ thể phun chất độc vàng bảo vệ bà trùm!
- **shorts_title:** Cỗ Máy Mù Lòa Ăn Mồi Trong 0,12 Giây & Ngửi Mùi Dưới Nước?! 🌟 #độngvật #chuộtchũisao
- **shorts_desc:** Chuột Chũi Sao ăn mồi trong 0,12 giây nhanh hơn chớp mắt nhờ chiếc mũi 22 xúc tu chứa 25.000 thụ thể Eimer và khả năng thổi bong bóng ngửi mùi dưới nước! Kỷ lục Guinness động vật có vú nhanh nhất hành tinh.
- **bullets:** Kỷ lục Guinness: Ăn con mồi trong 120 mili-giây (0,12s), não phân tích chỉ mất 8 mili-giây · Chiếc mũi hoa sao: 22 xúc tu chứa 25.000 thụ thể Eimer chạm 12 điểm mỗi giây · Động vật có vú duy nhất ngửi mùi dưới nước bằng cơ chế thổi và hít lại bong bóng khí (Nature 2006) · Nhật ký 24h: Bơi lội dưới băng mùa đông nhờ chiếc đuôi phình to tích trữ mỡ dự trữ
- **tags:** chuột chũi sao, chuot chui sao, star nosed mole, condylura cristata, ăn mồi 0.12 giây, ngửi mùi dưới nước, mũi 22 xúc tu, động vật kỳ lạ, thế giới động vật, động vật hài hước, vẽ chuyện hoang dã, whiteboard animation, khoa học thú vị
- **hashtags:** #độngvật #chuộtchũisao #VẽChuyệnHoangDã

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-27-chuot-chui-sao
python src/episode/pipeline.py tts    projects/tap-27-chuot-chui-sao     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-27-chuot-chui-sao     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-27-chuot-chui-sao     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-27-chuot-chui-sao              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-27-chuot-chui-sao --force
python scripts/beat_sheet.py projects/tap-27-chuot-chui-sao               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-27-chuot-chui-sao/audio/shorts.wav projects/tap-27-chuot-chui-sao/renders/tap-27-chuot-chui-sao_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-27-chuot-chui-sao
python src/episode/pipeline.py seo    projects/tap-27-chuot-chui-sao
python src/episode/episode_doc.py     projects/tap-27-chuot-chui-sao
```
