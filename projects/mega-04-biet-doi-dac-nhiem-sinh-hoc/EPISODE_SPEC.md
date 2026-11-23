# TẬP ĐẶC BIỆT BIỆT ĐỘI ĐẶC NHIỆM SINH HỌC #4 (SAU 40 TẬP) — 10 ĐẶC VỤ — BIỆT ĐỘI ĐẶC NHIỆM SINH HỌC · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`mega-04-biet-doi-dac-nhiem-sinh-hoc`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/mega-04-biet-doi-dac-nhiem-sinh-hoc`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F_SPECIAL` · **Persona giọng:** `chi_huy_mat_vu` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | 10 đặc vụ — Biệt Đội Đặc Nhiệm Sinh Học |
| Tiêu đề YouTube | [TẬP ĐẶC BIỆT] Phi Vụ Thế Kỷ: Biệt Đội Đặc Nhiệm Sinh Học Đột Nhập Pháo Đài Tự Nhiên |
| Video dài | `renders/mega-04-biet-doi-dac-nhiem-sinh-hoc_long.mp4` — 60:12.1 (3612.1s) |
| Shorts | `renders/mega-04-biet-doi-dac-nhiem-sinh-hoc_shorts.mp4` — 0:54.5 (54.5s) |
| Thumbnail | `renders/mega-04-biet-doi-dac-nhiem-sinh-hoc_thumbnail.jpg` |
| Số hình | dài 478 beat / 478 ảnh riêng; Shorts 11 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.1**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 60:00.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/478 của video YouTube về 10 đặc vụ — Biệt Đội Đặc Nhiệm Sinh Học). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa vẽ tay đặc trưng cho chủ đề, nét mực sắc nét, màu sắc tương phản cuốn hút, tối giản giàu tính biểu tượng khoa học; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: anh Chỉ Huy Mật Vụ điệp viên cú mèo hoạt hình đeo kính râm đen ngầu, mặc áo măng-tô đen cổ đứng có gắn huy hiệu đặc nhiệm bạc, tai đeo tai nghe bộ đàm điệp viên, cầm máy tính bảng hologram phát sáng xanh. Nhân vật phụ cố định: anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — TRIỆU TẬP BIỆT ĐỘI ĐẶC NHIỆM SINH HỌC
*Thẻ chương:* BẢN MẬT LỆNH ĐỘT NHẬP

*Badge:* `HỒ SƠ TỐI MẬT` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene01_p0.wav` (837 ký tự) · mood `tram_bi_an`

```text
Một căn hầm ngầm bê tông tối om dưới lòng đất sâu một trăm mét. Chỉ có ánh sáng xanh lục từ chiếc máy chiếu hologram quét chầm chậm qua các góc phòng. Chào mừng toàn thể các điệp viên đến với Tổng Cục Tiến Hóa Tối Mật. Nếu các bạn nghe được tín hiệu này, có nghĩa là phi vụ thế kỷ đã chính thức bắt đầu. Trước mặt chúng ta là mục tiêu tối thượng chưa từng có sinh vật nào xuyên thủng được suốt năm trăm triệu năm qua: Pháo Đài Tự Nhiên. Nơi đây giấu kín Bản Thiết Kế Tiến Hóa Tối Thượng, cội nguồn sức mạnh của toàn bộ giới sinh vật trên Trái Đất. Nhưng để chạm tới chiếc két sắt trung tâm, Biệt Đội Đặc Nhiệm Sinh Học phải vượt qua bảy cửa ải an ninh sinh tử kiên cố nhất. Và để giải mã bảy cánh cửa bất khả thi này, tôi đã đích thân tuyển chọn mười đặc vụ bất hảo và quái kiệt nhất hành tinh. Không một ai trong số họ là kẻ tầm thường.
```
**Part 1** → `audio/vs/scene01_p1.wav` (834 ký tự) · mood `hao_hung`

```text
Đặc vụ số một! Mật danh Tia Chớp Bầu Trời, kẻ sở hữu vũ khí xuyên phá hàng rào laser trên không: Chim Cắt Lớn! Hồ sơ tác chiến ghi rõ: anh chàng này từng đạt tốc độ bổ nhào xé gió ba trăm tám mươi chín cây số một giờ, nhanh hơn cả một chiếc siêu xe đua Công Thức Một! Đặc vụ số hai! Mật danh Bóng Ma Hầm Ngầm, chuyên gia thâm nhập các địa đạo không có không khí và đầy sương axit: Chuột Chũi Trũi! Sinh vật không lông này có thể sống phây phây mười tám phút không cần oxy, và hoàn toàn miễn nhiễm với mọi cảm giác đau đớn do axit gây ra! Đặc vụ số ba! Mật danh Điệp Viên Băng Giá, sinh vật duy nhất có khả năng tự biến mình thành tảng băng để đánh lừa cảm biến tầm nhiệt: Ếch Gỗ Bắc Cực! Anh chàng có thể để sáu mươi lăm phần trăm cơ thể đóng băng cứng ngắc suốt bảy tháng mùa đông, tim ngừng đập hoàn toàn mà vẫn hồi sinh nguyên vẹn!
```
**Part 2** → `audio/vs/scene01_p2.wav` (844 ký tự) · mood `don_dap`

```text
Đặc vụ số bốn! Mật danh Bộ Não Cơ Học, bậc thầy giải mã các chuỗi khóa bẫy đa bước phức tạp nhất: Quạ Đen! Tài liệu của viện nghiên cứu khẳng định: bộ não của quạ đen có thể tự giải các câu đố logic cơ học tám bước liên hoàn trong vòng ba mươi giây mà không cần dạy trước! Đặc vụ số năm! Mật danh Thủy Thần Đại Dương, chỉ huy phân đội tác chiến đường nước với sóng âm phá hủy công sự: Cá Voi Sát Thủ! Cỗ máy săn mồi sáu tấn này sở hữu chùm sóng sonar công suất hai trăm hai mươi lăm đê-xi-ben, đủ sức quét xuyên lòng đá và tạo nên những cơn sóng thần dập tắt mọi chốt chặn! Đặc vụ số sáu! Mật danh Búa Khoan Thần Tốc, kẻ có thể đập nát cửa boong-ke dày cộp bằng chính hộp sọ của mình: Chim Gõ Kiến! Cơ chế đai an toàn xương móng quấn quanh đầu cho phép anh chàng chịu đựng lực gia tốc va đập lên tới một ngàn hai trăm G mà không hề choáng váng!
```
**Part 3** → `audio/vs/scene01_p3.wav` (1140 ký tự) · mood `hao_hung`

```text
Đặc vụ số bảy! Mật danh Cỗ Xe Tăng Sa Mạc, pháo đài di động vượt qua vùng bẫy nhiệt độ năm mươi độ C mà không cần tiếp tế một giọt nước: Lạc Đà Sa Mạc! Hồng cầu hình oval độc nhất vô nhị giãn nở hai trăm bốn mươi phần trăm thể tích giúp anh chàng trữ một trăm lít nước và hành quân qua chảo lửa sa mạc dễ dàng! Đặc vụ số tám! Mật danh Thánh Leo Vách Đứng, kẻ thách thức mọi định luật vật lý trên những bức tường dựng đứng chín mươi độ: Dê Núi Bắc Mỹ! Bốn chiếc móng guốc cao su đàn hồi kép giúp anh chàng phi thân ngược vách đá thẳng đứng ba mươi mét trong nháy mắt! Đặc vụ số chín! Mật danh Sát Thủ Gai Nhọn, tay súng bắn tỉa và phục kích cắm chốt tầm xa: Chim Bách Thanh! Mấu răng tomium sắc bén và kỹ thuật găm gai nhọn cho phép anh chàng hạ gục đối thủ to gấp đôi và cất giữ chiến lợi phẩm an toàn suốt ba ngày! Và lực lượng công binh bí mật cuối cùng! Đặc vụ số mười: Đại Đội Công Binh Kiến Cắt Lá, hàng triệu chiến sĩ tí hon sở hữu hàm răng thép tẩm kim loại nặng có thể khoét rỗng chân móng pháo đài! Lớp kim loại kẽm và mangan nguyên chất tẩm vào đầu răng biến bầy kiến này thành những chiếc máy cắt kim cương di động dưới lòng đất!
```
**Part 4** → `audio/vs/scene01_p4.wav` (115 ký tự) · mood `tram_bi_an`

```text
Đủ mười đặc vụ. Bảy cửa ải. Và đúng sáu mươi phút trước khi hệ thống phòng thủ của pháo đài khóa vĩnh viễn lối vào.
```
**Part 5** → `audio/vs/scene01_p5.wav` (132 ký tự) · 🎭 cameo `phat_thanh_vien`

```text
Thông báo khẩn từ trung tâm giám sát vệ tinh: pháo đài vừa kích hoạt toàn bộ lưới phòng vệ cấp độ đỏ! Toàn đội vào vị trí tác chiến!
```
**Part 6** → `audio/vs/scene01_p6.wav` (247 ký tự) · mood `tram_bi_an`

```text
Các đặc vụ nghe rõ: phi vụ này tuyệt đối không có chỗ cho sự sai sót. Không có thử lại. Không có cứu viện. Mọi chi tiết trong kế hoạch này đều dựa trên những báo cáo sinh học tối tân nhất vừa được giải mã từ các phòng thí nghiệm hàng đầu thế giới.
```
**Part 7** → `audio/vs/scene01_p7.wav` (477 ký tự) · mood `hao_hung`

```text
Chúng ta không dùng súng đạn. Vũ khí tối thượng của biệt đội chính là những tuyệt kỹ tiến hóa hàng trăm triệu năm của tạo hóa! Cửa Ải Một đã hiện ra trên màn hình radar: Không phận tử thần với áp suất gió kinh hoàng và lưới quét quang học. Mật danh Tia Chớp, đến lượt cậu cất cánh! Biệt Đội Đặc Nhiệm Sinh Học chính thức xuất kích! Không một kẻ thù nào có thể cản bước mười quái kiệt của tự nhiên! Mục tiêu là chiếc chìa khóa tối thượng. Thời gian đang đếm ngược từng giây một!
```
**Part 8** → `audio/vs/scene01_p8.wav` (627 ký tự) · mood `tram_bi_an`

```text
Pháo Đài Tự Nhiên được xây dựng dựa trên những định luật khắc nghiệt nhất của hành tinh, nơi những kẻ yếu đuối sẽ bị đào thải không thương tiếc. Mỗi một cửa ải đại diện cho một thảm họa sinh học tự nhiên: từ áp suất chân không đến cực hạn giá rét, từ sa mạc lửa cháy đến hào nước áp lực cao. Chỉ có sức mạnh thích nghi tối thượng của muôn loài mới có thể tìm ra kẽ hở giữa những công sự kiên cố này! Các kỹ sư của Tổng Cục đã phân tích dữ liệu địa tầng suốt ba năm ròng để vẽ nên sơ đồ tiến công chuẩn xác nhất cho biệt đội! Mọi thiết bị hỗ trợ và vũ khí ngụy trang đều đã được kiểm tra nghiêm ngặt, sẵn sàng cho giờ xuất kích!
```

### scene02 — KHÔNG PHẬN SIÊU THANH & CHIM CẮT LỚN
*Thẻ chương:* BỔ NHÀO XÉ GIÓ 389 KM/H

*Badge:* `CỬA ẢI 1` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene02_p0.wav` (635 ký tự) · mood `don_dap`

```text
Bầu trời đêm phía trên Pháo Đài Tự Nhiên không hề yên bình như vẻ bề ngoài. Đây là vành đai phòng không khắc nghiệt nhất hành tinh. Hàng ngàn cảm biến gió áp suất cao đang quét liên tục ở tầng đối lưu. Bất kỳ vật thể bay nào lao vào đây với tốc độ cao đều sẽ bị luồng khí nén cực mạnh xé nát phổi ngay lập tức. Đặc vụ Chim Cắt Lớn đang lượn vòng ở độ cao hơn ba ngàn mét. Gió rít gào bên tai, nhưng nhịp tim của anh chàng vẫn ổn định như một cỗ máy đếm giờ. Đôi mắt của chim cắt sở hữu hai hố thị giác riêng biệt trên mỗi võng mạc, cho phép anh chàng vừa phóng to mục tiêu như kính viễn vọng vừa quan sát toàn cảnh ba trăm sáu mươi độ!
```
**Part 1** → `audio/vs/scene02_p1.wav` (168 ký tự) · mood `tram_bi_an`

```text
Bộ đàm trung tâm rè lên giọng Chỉ Huy Mật Vụ: "Mật danh Tia Chớp, mục tiêu là chiếc rơ-le nguồn laser đặt ngay trên đỉnh vòm kính. Cậu chỉ có đúng một cơ hội duy nhất."
```
**Part 2** → `audio/vs/scene02_p2.wav` (157 ký tự) · 🎭 cameo `ba_trum`

```text
Nhắc nhở nhẹ nhàng từ bộ phận giám sát: nếu cậu bay thẳng, áp lực gió sẽ thổi bung cả mắt lẫn mũi cậu đấy! Cẩn thận kẻo biến thành món chim nướng siêu thanh!
```
**Part 3** → `audio/vs/scene02_p3.wav` (738 ký tự) · mood `hao_hung`

```text
Chim Cắt Lớn chỉ nhếch mép cười khẩy qua bộ đàm. Những kẻ nghiệp dư luôn nghĩ bay nhanh chỉ cần đôi cánh khỏe, nhưng họ đâu biết bí mật nằm ở chính chiếc mũi của anh chàng! Hãy nhìn sâu vào lỗ mũi của Chim Cắt Lớn. Các nhà khoa học tại đại học công nghệ vừa giải mã một kỳ quan kỹ thuật sinh học: một mấu lồi hình nón nhỏ bằng xương nằm ngay chính giữa khoang mũi! Khi lao xuống với tốc độ xé gió, mấu xương này đóng vai trò như chiếc van điều áp của động cơ máy bay phản lực, làm chậm và đổi hướng luồng gió xoáy cực mạnh, giúp anh chàng hít thở nhẹ nhàng như đang ngồi uống trà! Không chỉ có mũi, cấu trúc lông cánh của chim cắt còn có những khe rãnh vi mô tự động nâng lên khi gặp áp lực lớn, triệt tiêu toàn bộ lực cản xoáy không khí!
```
**Part 4** → `audio/vs/scene02_p4.wav` (602 ký tự) · mood `don_dap`

```text
Tọa độ đã khóa! Chim Cắt Lớn thu gọn hai cánh sát vào thân, biến toàn bộ cơ thể thành một đầu đạn khí động học hoàn hảo! Gia tốc tăng vọt! Một trăm cây số một giờ... Hai trăm cây số một giờ... Ba trăm cây số một giờ! Kim đo tốc độ radar bên dưới phòng chỉ huy quay tít mù! Và đây là con số kỷ lục từng được các nhà khoa học gắn chip đo đạc thực tế trên cơ thể một chú chim cắt: ba trăm tám mươi chín cây số một giờ! Vận tốc nhanh nhất trong toàn bộ thế giới động vật! Tiếng rít xé rách không khí vang lên như một tiếng nổ siêu thanh trầm đục, làm rung chuyển cả những vách kính trên đỉnh tháp pháo đài!
```
**Part 5** → `audio/vs/scene02_p5.wav` (584 ký tự) · mood `tram_bi_an`

```text
Ở tốc độ ba trăm tám mươi chín cây số một giờ, chỉ một hạt bụi nhỏ bay vào mắt cũng đủ làm nổ tung giác mạc. Nhưng Chim Cắt Lớn vẫn mở to mắt nhìn rõ từng chi tiết của mục tiêu! Bí quyết là chiếc màng nháy trong suốt che phủ mắt, nhấp nháy với tần số chóng mặt: một trăm hai mươi lần một phút! Chiếc màng này vừa bôi trơn liên tục vừa lọc bụi bẩn, cho phép Chim Cắt Lớn duy trì tầm nhìn sắc như kính hiển vi điện tử giữa cơn bão gió! Tuyến lệ của chim cắt liên tục tiết ra một chất dịch nhầy đặc biệt có sức căng bề mặt cực lớn, không hề bị gió cuốn bay dù ở vận tốc xé rách âm thanh!
```
**Part 6** → `audio/vs/scene02_p6.wav` (631 ký tự) · mood `don_dap`

```text
Khoảng cách còn một trăm mét! Cột laser phòng vệ phát hiện mục tiêu và quét chéo qua! Chim Cắt Lớn khẽ nghiêng một góc bốn mươi lăm độ theo đường xoắn ốc toán học, lượn né tia laser chỉ trong một phần mười giây! Đường bay xoắn ốc này được lập trình tự nhiên theo quy luật đường cong lô-ga-rít, giúp mắt chim luôn hướng thẳng vào mục tiêu trong khi toàn thân nghiêng né đạn! Khoảng cách còn mười mét! Anh chàng duỗi thẳng cặp móng vuốt vàng sắc nhọn, bọc mạ lớp thép bảo hộ, đạp thẳng vào công tắc nguồn điện tử! Xoẹt! Tiếng điện nổ râm ran, toàn bộ mạng lưới laser bảo vệ trên không vụt tắt đen ngòm! Vòm kính pháo đài từ từ hé mở!
```
**Part 7** → `audio/vs/scene02_p7.wav` (471 ký tự) · mood `hao_hung`

```text
Chim Cắt Lớn dang rộng đôi cánh phanh gấp giữa không trung, nhẹ nhàng hạ cánh xuống mép thành đá, giơ một ngón cánh làm dấu hiệu thắng lợi qua camera ngực. Thanh tiến độ Cửa Ải Một trên bản đồ chuyển sang màu xanh ngọc bích! Không phận tử thần đã bị vô hiệu hóa hoàn toàn trong vòng chưa đầy hai phút! Nhưng niềm vui chưa kịp trọn vẹn thì dưới chân tháp, một tiếng còi báo động trầm đục vang lên từ lòng đất. Hệ thống phòng thủ tự động vừa đóng sập toàn bộ cửa thông gió!
```
**Part 8** → `audio/vs/scene02_p8.wav` (496 ký tự) · mood `tram_bi_an`

```text
Lối vào duy nhất lúc này là hệ thống đường ống xả ngầm sâu dưới lòng đất, nơi không hề có dưỡng khí và ngập tràn sương axit. Chỉ Huy Mật Vụ bấm nút gọi nội bộ: "Đặc vụ Chuột Chũi Trũi, khoang yếm khí đã sẵn sàng cho cậu. Đừng có mải ngủ gật đấy nhé!" Từ dưới đáy một đường ống kim loại gỉ sét, một cái mũi màu hồng nhăn nheo khẽ thò ra, hắt xì một cái rõ to. Cuộc đột nhập tầng hầm bắt đầu! Đặc vụ Chuột Chũi xoa hai chân trước, chuẩn bị kích hoạt vũ khí sinh học chống ngạt thở vô song của mình!
```
**Part 9** → `audio/vs/scene02_p9.wav` (708 ký tự) · mood `hao_hung`

```text
Các phi công lái máy bay siêu thanh của quân đội từng thử nghiệm mô phỏng đường bay của chim cắt trên máy tính và đều phải lắc đầu chịu thua! Ở góc bổ nhào bốn mươi lăm độ, gia tốc trọng trường kéo chú chim lao đi nhanh hơn bất kỳ mũi tên bắn tỉa nào từng được phóng ra! Đôi mắt chim cắt với lớp màng nháy siêu việt vẫn liên tục truyền về trung tâm chỉ huy những hình ảnh tĩnh nét đến từng con ốc vít của trạm phát laser! Nhịp đập của đôi cánh chim cắt khi lấy thăng bằng sau cú bổ nhào phát ra tiếng rít xé gió khiến cả đàn chim đêm xung quanh phải nể sợ! Bộ cảm biến gia tốc trên ngực áo truyền về trung tâm chỉ huy xác nhận: cấu trúc xương đòn của chim cắt đã hấp thụ hoàn hảo mọi xung chấn của không khí!
```

### scene03 — HẦM NGẦM 0% OXY & CHUỘT CHŨI TRŨI
*Thẻ chương:* SỐNG SÓT 18 PHÚT KHÔNG DƯỠNG KHÍ

*Badge:* `CỬA ẢI 2` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene03_p0.wav` (710 ký tự) · mood `tram_bi_an`

```text
Địa đạo ngầm dưới chân Pháo Đài Tự Nhiên là một cái bẫy chết chóc được thiết kế để tiêu diệt bất kỳ sinh vật hiếu khí nào dám bén mảng tới. Cửa thép phía sau vừa sập xuống, máy hút chân không lập tức khởi động rên rỉ ầm ầm. Nồng độ dưỡng khí trong ống tụt dốc không phanh: hai mươi phần trăm... mười phần trăm... năm phần trăm... rồi chạm đáy số không tròn trĩnh! Không có lấy một phân tử khí thở. Bất kỳ loài thú nào, kể cả con người hay sư tử, chỉ cần hít thở trong môi trường này bốn mươi lăm giây là sẽ bất tỉnh nhân sự, tế bào não chết vĩnh viễn sau ba phút. Khí các-bon-nic và nồng độ axit trong hầm tăng vọt lên mức kịch độc, đủ sức làm bỏng cháy niêm mạc phổi của bất kỳ kẻ xâm nhập nào trong tích tắc!
```
**Part 1** → `audio/vs/scene03_p1.wav` (527 ký tự) · mood `hao_hung`

```text
Nhưng kẻ đang bò trong đường ống này lại là một sinh vật coi việc thiếu dưỡng khí... chỉ là một buổi dạo chơi nhẹ nhàng sau bữa trưa! [laughter] Đặc vụ Chuột Chũi Trũi thong dong bước đi, không hề tỏ ra hoảng loạn hay ngột ngạt. Bí mật sinh học chấn động gì đã giúp anh chàng này thách thức quy luật hô hấp của muôn loài? Cơ thể không lông của anh chàng được bao bọc bởi một lớp da siêu đàn hồi chứa đầy phân tử axit hyaluronic trọng lượng cực cao, giúp da trơn tuột không hề trầy xước khi cọ xát vào mép ống kim loại sắc nhọn!
```
**Part 2** → `audio/vs/scene03_p2.wav` (781 ký tự) · mood `tram_bi_an`

```text
Năm hai ngàn mười bảy, một nghiên cứu đột phá đăng trên tạp chí Khoa Học danh giá đã vén màn bí mật: khi hết sạch dưỡng khí, cơ thể Chuột Chũi Trũi tự động chuyển sang chế độ hoạt động của... thực vật! Đúng vậy, bạn không nghe nhầm đâu! Bộ não và trái tim của các loài động vật có vú thông thường chỉ có thể đốt đường glucose bằng dưỡng khí để tạo năng lượng. Không có dưỡng khí, cỗ máy ngừng chạy ngay lập tức. Nhưng Chuột Chũi Trũi lại sở hữu những thụ thể vận chuyển đường đặc biệt có tên gọi là phân tử vận chuyển đường hoa quả Gờ-lút năm, giúp chúng kích hoạt việc đốt trực tiếp đường fructose mà không cần đến một phân tử dưỡng khí nào! Đường fructose đi thẳng vào chu trình đường phân ở cơ tim và vỏ não, sản sinh năng lượng duy trì sự sống bền bỉ ngay giữa vùng chân không!
```
**Part 3** → `audio/vs/scene03_p3.wav` (517 ký tự) · mood `don_dap`

```text
Thử nghiệm khoa học chấn động tại phòng thí nghiệm đã chứng minh: Chuột Chũi Trũi có thể sống sót khỏe mạnh suốt mười tám phút trong môi trường hoàn toàn không phần trăm oxy! Khi có dưỡng khí trở lại, chúng đứng dậy phủi bụi và đi lại bình thường như chưa từng có chuyện gì xảy ra, không hề tổn thương dù chỉ một tế bào thần kinh! Nhịp tim của chuột chũi tự động hạ từ hai trăm nhịp một phút xuống còn năm mươi nhịp một phút để tiết kiệm tối đa năng lượng, đưa cơ thể vào trạng thái ngủ đông cục bộ cực kỳ thông minh!
```
**Part 4** → `audio/vs/scene03_p4.wav` (421 ký tự) · mood `tram_bi_an`

```text
Nhưng thử thách của Cửa Ải Hai chưa dừng lại ở đó. Hệ thống phòng thủ tự động phát hiện kẻ xâm nhập vẫn còn sống, liền kích hoạt tầng bẫy thứ hai: vòi phun axit! Làn sương axit có độ pH ba cực kỳ ăn mòn và bỏng rát, đủ sức làm phồng rộp làn da của bất kỳ kẻ đột nhập nào trong nháy mắt. Sương axit bắn thẳng vào thân mình không một sợi lông của Chuột Chũi Trũi. Bộ đàm phòng chỉ huy nín thở! Chỉ Huy Mật Vụ siết chặt tay!
```
**Part 5** → `audio/vs/scene03_p5.wav` (599 ký tự) · mood `hao_hung`

```text
Nhưng Chuột Chũi Trũi... chỉ khẽ gãi gãi nách rồi tiếp tục bò! Anh chàng thậm chí còn không thèm chớp mắt! [laughter] Bởi vì tạo hóa đã tặng cho loài vật này một món quà vô giá: chúng hoàn toàn mất tín hiệu dẫn truyền cơn đau của chất hóa học P và thụ thể thần kinh cảm giác! Axit hay ớt cay hay lửa rát chạm vào da chuột chũi trũi cũng chẳng khác gì nước lã gội đầu! Chúng không hề biết đau là cái gì trên cõi đời này! Các nhà thần kinh học tại đại học Cambridge phát hiện ra rằng thụ thể kênh ion TrkA của chuột chũi đã bị đột biến, biến chúng thành loài động vật có vú duy nhất trơ lì trước axit!
```
**Part 6** → `audio/vs/scene03_p6.wav` (694 ký tự) · mood `don_dap`

```text
Lối đi phía trước đột ngột bị một tảng đá cản đường, và đường ống quá hẹp khiến chuột chũi không thể xoay người quay đầu lại! Không cần quay đầu! Chuột Chũi Trũi cài số lùi, chạy lùi với tốc độ nhanh y hệt như chạy tiến nhờ chiếc đuôi nhạy bén như chiếc ăng-ten cảm biến lùi ô tô! Anh chàng đổi hướng bò sang một nhánh rẽ thông hơi, tiếp cận chiếc van khóa áp lực chính của pháo đài! Cặp răng cửa khổng lồ dài ngoằng thò ra ngoài môi bắt đầu phát huy tác dụng. Chuột chũi có thể cử động hai chiếc răng cửa độc lập như một đôi đũa gắp thức ăn! Rắc! Chiếc chốt khóa bằng đồng thau bị cắn đứt đôi! Chuột chũi không hề nuốt phải một hạt bụi kim loại nào vì môi của anh chàng khép kín phía sau răng!
```
**Part 7** → `audio/vs/scene03_p7.wav` (433 ký tự) · mood `hao_hung`

```text
Đèn báo động đỏ chuyển sang màu xanh lá dịu mát! Hệ thống hút chân không bị vô hiệu hóa! Cửa Ải Hai đã được dọn sạch hoàn toàn! Chuột Chũi Trũi ngoi đầu lên từ một lỗ thông gió ở sàn tầng trệt, giơ hai chân trước phủi mũi, phát ra một tiếng rít vui tai qua bộ đàm. Nhưng ngay khi cửa mở ra, một luồng khí lạnh buốt xương tủy bất ngờ ùa tới từ cánh cửa hành lang tiếp theo, làm đóng băng ngay lập tức những giọt nước đọng trên sàn đá!
```
**Part 8** → `audio/vs/scene03_p8.wav` (496 ký tự) · mood `tram_bi_an`

```text
Cửa Ải Ba: Kho Lạnh Cực Hạn với nhiệt độ âm hai mươi độ C và hệ thống cảm biến hồng ngoại tầm nhiệt tinh vi nhất thế giới! Mọi cơ thể ấm áp bước vào đây sẽ bị phát hiện trong vòng nửa giây. Chỉ có một sinh vật có thể biến mình thành một tảng băng vô tri vô giác để vượt qua cửa ải này. "Đặc vụ Ếch Gỗ Bắc Cực, đã đến lúc cho cả pháo đài thấy thế nào là nghệ thuật ngủ đông bất tử!" Và phía sau lưng, tiếng cãi cọ qua kênh bộ đàm bắt đầu bùng nổ, báo hiệu một sự cố hài hước không thể lường trước!
```
**Part 9** → `audio/vs/scene03_p9.wav` (738 ký tự) · mood `tram_bi_an`

```text
Kỳ tích chuyển hóa đường fructose của Chuột Chũi Trũi đang mở ra một cuộc cách mạng y học lớn trong việc điều trị các bệnh nhân bị nhồi máu cơ tim và đột quỵ do thiếu oxy! Khi oxy cạn kiệt, các tế bào tim của chuột chũi không hề bị co thắt hay hoại tử, mà vẫn đập êm ả nhờ dòng năng lượng fructose ngọt ngào! Cơ thể không lông của chúng còn chứa một loại gen đặc biệt giúp sửa chữa tế bào thần kinh với tốc độ nhanh gấp năm lần các loài chuột thông thường! Nhờ tốc độ tiêu thụ đường fructose cực kỳ chậm rãi, chuột chũi có thể duy trì hoạt động của các cơ quan nội tạng mà không hề tạo ra độc tố axit lactic gây mỏi cơ! Đặc vụ Chuột Chũi Trũi quệt mồ hôi trên mũi, nở một nụ cười rạng rỡ của một nhà quán quân sinh tồn không biết mệt mỏi!
```

### scene04 — CHUỘT CHŨI ĐÀO NHẦM KHO BÁNH & QUẠ ĐEN ĐÒI TĂNG LƯƠNG
*Thẻ chương:* TÌNH HUỐNG DỞ KHÓC DỞ CƯỜI

*Badge:* `HẬU TRƯỜNG 1` · *mood mặc định:* `bi_hai`

**Part 0** → `audio/vs/scene04_p0.wav` (442 ký tự) · mood `bi_hai`

```text
[sigh] Điệp vụ thế kỷ tưởng chừng như đang diễn ra hoàn hảo đến từng tích tắc... thì kênh bộ đàm nội bộ bắt đầu phát ra những âm thanh cực kỳ bất thường. Tiếng nhai chóp chép giòn tan vang lên rành rọt qua chiếc loa điều khiển trung tâm, to đến mức át cả tiếng còi báo động của pháo đài! "Báo cáo Chỉ Huy! Tôi vừa đột nhập thành công vào phòng chứa tài liệu bí mật! Nhưng ở đây không có tài liệu... chỉ có toàn là khoai tây sấy bơ thơm lừng!"
```
**Part 1** → `audio/vs/scene04_p1.wav` (254 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Khoai tây này ngọt lắm sếp ơi! Có cần tôi vận chuyển về phòng chỉ huy năm bao làm quà lưu niệm cho Biệt Đội Đặc Nhiệm Sinh Học không ạ? Sau phi vụ này tôi định mở một chuỗi nhà hàng khoai nướng yếm khí dưới lòng đất, sếp nhớ đến cắt băng khánh thành nhé!
```
**Part 2** → `audio/vs/scene04_p2.wav` (410 ký tự) · mood `nghiem_trang_gia`

```text
Chỉ Huy Mật Vụ hít một hơi thật sâu, giọng lạnh như băng truyền qua mic: "Đặc vụ Chuột Chũi... cậu vừa đào nhầm vào kho bếp của bảo vệ pháo đài rồi đấy." "Nếu trong vòng ba mươi giây nữa cậu không kéo cái thân nhăn nheo của mình ra khỏi kho khoai tây, tôi sẽ ghi tên cậu vào danh sách cắt khẩu phần ăn ba tháng!" "Và đừng bao giờ mơ đến chuyện mở nhà hàng khoai nướng khi đang trong giờ làm việc của Tổng Cục!"
```
**Part 3** → `audio/vs/scene04_p3.wav` (88 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Ối sếp ơi! Tôi đi ngay đây! Nhưng cho tôi xin nhét thêm một củ nhỏ vào túi áo khoác nhé!
```
**Part 4** → `audio/vs/scene04_p4.wav` (156 ký tự) · mood `hao_hung`

```text
Chưa kịp thở phào thì một tiếng rít chói tai khác lại chèn ngang vào tần số liên lạc tối mật. Lần này là giọng nói đanh đá và đậm chất con buôn của Quạ Đen!
```
**Part 5** → `audio/vs/scene04_p5.wav` (475 ký tự) · 🎭 cameo `cong_to_vien`

```text
A lô Chỉ Huy nghe rõ không? Kênh mã hóa này tín hiệu tốt đấy! Tiện thể tôi xin gửi báo cáo tài chính cập nhật trước khi bước vào Cửa Ải Ba và Cửa Ải Bốn! Hợp đồng ban đầu chỉ ghi giải mã ba cái ổ khóa cơ học đơn giản. Đằng này toàn là bẫy gương tâm lý với khóa liên hoàn tám bước của các kỹ sư thiên tài! Tôi yêu cầu tăng lương gấp đôi! Cộng thêm điều khoản bảo hiểm gãy mỏ khi tác chiến và một thùng hạt dẻ thượng hạng! Nếu không thì tự đi mà giải mã mê cung nhé! [laughter]
```
**Part 6** → `audio/vs/scene04_p6.wav` (448 ký tự) · mood `nghiem_trang_gia`

```text
Toàn bộ phòng chỉ huy rơi vào im lặng sượng sùng. Chỉ Huy Cú Mèo từ từ với tay lấy một tập hồ sơ có dán nhãn đỏ: "Hồ sơ quậy phá nơi công cộng của Quạ Đen". "Đặc vụ Quạ Đen, cậu có muốn tôi nhắc lại vụ án trộm mất sáu mươi chiếc thìa bạc tại dinh thự thị trưởng năm ngoái không?" "Bằng chứng vẫn còn nằm nguyên trong két sắt của tôi đấy. Nếu phi vụ này thành công, hồ sơ đó sẽ biến mất trong lò thiêu hủy. Cậu thấy mức lương đó đã đủ hấp dẫn chưa?"
```
**Part 7** → `audio/vs/scene04_p7.wav` (156 ký tự) · 🎭 cameo `cong_to_vien`

```text
Ấy ấy Chỉ Huy bình tĩnh! Đùa tí cho không khí bớt căng thẳng thôi mà! Làm gì mà nóng tính thế! [laughter] Tôi đang chuẩn bị sẵn bộ đồ nghề phá khóa rồi đây!
```
**Part 8** → `audio/vs/scene04_p8.wav` (647 ký tự) · mood `hao_hung`

```text
Đúng lúc đó, Chim Cắt Lớn cũng chêm vào một câu qua sóng vô tuyến: "Đề nghị mọi người nói nhỏ giùm! Gió trên đỉnh tháp vừa làm bay mất một sợi lông đuôi quý giá của tôi rồi đây này!" "Đồng đội gì mà người thì mê ăn khoai, kẻ thì đòi tăng lương, làm mất hết cả hình tượng điệp viên ngầu lòi của tôi!" Chim Cắt phụng phịu lắc đầu. Dưới bể nước dã chiến, Cá Voi Sát Thủ phun lên một cột nước cao ba mét qua lỗ thở, phát ra tiếng cười khùng khục qua mic: "Mấy đứa trên cạn ồn ào quá! Bao giờ mới đến lượt đại ca biển cả ra tay đây?" Dê Núi và Lạc Đà cũng tranh thủ nhảy vào kênh chat tổng bàn tán về việc loại cỏ sa mạc nào ngọt hơn cỏ trên núi tuyết!
```
**Part 9** → `audio/vs/scene04_p9.wav` (671 ký tự) · mood `tram_bi_an`

```text
Chỉ Huy Mật Vụ gõ ngón tay xuống bàn ba tiếng cộc cộc cộc để lập lại trật tự: "Đủ rồi! Tất cả chuyển sang kênh tác chiến im lặng!" Sự hài hước chấm dứt ngay khi cánh cửa ngăn cách Cửa Ải Ba từ từ nâng lên. Hơi lạnh âm hai mươi độ C tràn ra ngoài làm ngưng đọng toàn bộ hơi nước thành những bông hoa tuyết rơi lả tả. Đây không phải là chỗ để đùa giỡn nữa. Bất kỳ một bước chân sai lầm nào cũng sẽ biến cơ thể thành một bức tượng đá vĩnh cửu. Đặc vụ Ếch Gỗ Bắc Cực đã bước vào phòng lạnh. Chiếc khăn quàng đỏ tung bay trong gió tuyết, ánh mắt anh chàng kiên định nhìn thẳng vào tâm điểm bẫy nhiệt độ. Sinh mệnh của cả biệt đội đang nằm trong bàn tay của chú ếch nhỏ bé này!
```
**Part 10** → `audio/vs/scene04_p10.wav` (711 ký tự) · mood `bi_hai`

```text
[sigh] "Báo cáo Chỉ Huy, tôi vừa phát hiện thêm một bao hạt dẻ rang muối ở góc bếp! Tôi có thể mang theo để phòng khi đói bụng không ạ?" Quạ Đen lập tức nhảy vào can thiệp: "Chia đôi! Nếu không tôi sẽ báo cáo lên Tổng Cục về tội danh ăn vụng quân lương của cậu!" [laughter] Dê Núi Bắc Mỹ thở dài qua mic: "Mấy người suốt ngày chỉ nghĩ đến ăn uống! Nhìn tôi đây này, chỉ cần gặm một mẩu rêu đá là đủ leo vách chín mươi độ cả ngày rồi!" Chỉ Huy Cú Mèo lắc đầu ngao ngán: "Giá như tinh thần đòi tăng lương của Quạ Đen được chuyển hóa thành tốc độ giải mã thì chúng ta đã xong nhiệm vụ từ lâu rồi!" [laughter] Toàn đội cười òa lên qua kênh bộ đàm, xua tan đi bầu không khí ngột ngạt của những căn hầm ngầm pháo đài!
```

### scene05 — KHO ĐÔNG LẠNH -20°C & ẾCH GỖ BẮC CỰC
*Thẻ chương:* ĐÓNG BĂNG 65% CƠ THỂ HỒI SINH

*Badge:* `CỬA ẢI 3` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene05_p0.wav` (604 ký tự) · mood `tram_bi_an`

```text
Căn hầm Kho Lạnh Cực Hạn là nơi giam giữ những bí mật được bảo quản nghiêm ngặt nhất của Pháo Đài Tự Nhiên. Nhiệt độ bên trong duy trì ổn định ở mức âm hai mươi độ C. Mọi thiết bị điện tử thông thường mang vào đây đều sẽ bị cạn pin trong vòng năm phút, các khớp kim loại co rút lại và kẹt cứng. Và điều nguy hiểm nhất là mạng lưới máy quét quang phổ hồng ngoại tầm nhiệt giăng kín mọi ngóc ngách. Chỉ cần phát hiện một điểm nhiệt trên không độ, súng đông lạnh tự động sẽ bắn nát mục tiêu! Hệ thống cảm biến nhạy đến mức có thể phát hiện thân nhiệt của một chú ruồi nhỏ bay qua ở khoảng cách hai mươi mét!
```
**Part 1** → `audio/vs/scene05_p1.wav` (539 ký tự) · mood `hao_hung`

```text
Đặc vụ Ếch Gỗ Bắc Cực bước từng bước chậm rãi trên mặt băng trơn trượt. Làn da nâu vàng điểm vệt đen ngang mắt của anh chàng trông như một hiệp sĩ đeo mặt nạ kiên cường. Bộ đàm phòng chỉ huy vang lên giọng Chỉ Huy Cú Mèo: "Đặc vụ Ếch Gỗ, khoảng cách tới bàn điều khiển là ba mươi mét. Cậu chỉ có thể vượt qua nếu cơ thể hoàn toàn nguội lạnh như một tảng đá." Ếch Gỗ gật đầu nhẹ nhàng. Anh chàng ngồi xổm xuống giữa sàn băng, thu hai chân sau sát vào bụng, nhắm nghiền hai mắt lại và bắt đầu kích hoạt cơ chế sinh học kỳ diệu nhất của mình!
```
**Part 2** → `audio/vs/scene05_p2.wav` (687 ký tự) · mood `tram_bi_an`

```text
Hãy quan sát kỳ quan sinh học đang diễn ra bên trong từng tế bào của chú ếch nhỏ bé này. Các nhà khoa học nghiên cứu sinh học vùng cực đã phải kinh ngạc thốt lên: đây là thuật giả kim đỉnh cao của tự nhiên! Ngay khi tinh thể băng đầu tiên chạm vào da, gan của ếch gỗ lập tức hoạt động hết công suất, bơm một lượng khổng lồ đường glucose và chất urea vào toàn bộ hệ tuần hoàn! Nồng độ đường bên trong tế bào tăng vọt gấp năm mươi đến một trăm lần so với bình thường, biến dịch nội bào thành một loại si-rô đậm đặc không thể bị đông cứng! Chất urea đóng vai trò như chiếc phao cứu sinh thứ hai, giữ nước bên trong tế bào không bị hút cạn ra ngoài khi các tinh thể đá hình thành xung quanh!
```
**Part 3** → `audio/vs/scene05_p3.wav` (584 ký tự) · mood `don_dap`

```text
Trong khi đó, ở khoảng không gian bên ngoài tế bào, điều kỳ diệu xảy ra: sáu mươi lăm phần trăm toàn bộ lượng nước trong cơ thể ếch gỗ bắt đầu đông cứng thành băng! Toàn bộ cơ thể Ếch Gỗ Bắc Cực cứng đờ lại như một viên sỏi đá. Đôi mắt đục ngầu như ngọc bích, các chi bất động, làn da phủ kín một lớp băng tuyết dày! Trái tim của anh chàng từ từ chậm lại: sáu mươi nhịp một phút... ba mươi nhịp một phút... mười nhịp một phút... rồi dừng hẳn lại! Phổi ngừng thở! Dòng máu ngừng chảy! Não bộ ngừng phát sóng điện từ! Ở góc độ y học thông thường, chú ếch này đã chết lâm sàng hoàn toàn!
```
**Part 4** → `audio/vs/scene05_p4.wav` (508 ký tự) · mood `tram_bi_an`

```text
Nhưng chính trạng thái chết giả thần kỳ này đã cứu sống anh chàng! Nhiệt độ cơ thể của Ếch Gỗ lúc này tụt xuống đúng âm hai mươi độ C, bằng chằn chặn với nhiệt độ của căn phòng băng! Hệ thống máy quét tầm nhiệt coi khối băng hình chú ếch chỉ là một tảng nhũ đá rơi xuống từ trần nhà, và thản nhiên bỏ qua không kích hoạt súng laser! Một cơn gió lốc của hệ thống điều hòa thổi mạnh qua sàn nhà, làm khối băng chứa Ếch Gỗ trượt ro ro trên mặt sàn băng nhẵn thín, lăn thẳng về phía chân bàn điều khiển nhiệt độ!
```
**Part 5** → `audio/vs/scene05_p5.wav` (763 ký tự) · mood `hao_hung`

```text
Đã tiếp cận mục tiêu! Bây giờ là giai đoạn hai: nghệ thuật hồi sinh sau giấc ngủ đông dài bảy tháng ở vùng cực bắc! Khi nhiệt độ môi trường nhích nhẹ lên trên mức đóng băng, các phân tử đường glucose bắt đầu hấp thụ nhiệt lượng. Lớp băng ngoại bào tan chảy dần dần! Kỳ tích xuất hiện: quả tim tí hon của Ếch Gỗ tự động phát ra một xung điện sinh học bí ẩn và bắt đầu co bóp trở lại! Thình thịch... thình thịch... thình thịch! Dòng máu ấm rã đông các tế bào thần kinh, đánh thức não bộ chỉ trong vòng vài phút ngắn ngủi! Các nhà khoa học ghi nhận: chỉ trong vòng chưa đầy một giờ đồng hồ sau khi tan băng, ếch gỗ có thể hồi phục toàn bộ chức năng sống và nhảy nhót như chưa từng bị đông cứng! Bẹp! Bàn chân có màng của Ếch Gỗ đạp trúng nút xả đông khẩn cấp màu đỏ!
```
**Part 6** → `audio/vs/scene05_p6.wav` (384 ký tự) · mood `don_dap`

```text
Hơi nóng bắt đầu ùa ra từ các họng thông gió, các cột băng khổng lồ tan chảy ầm ầm thành những dòng suối nhỏ chảy dọc sàn đá! Cửa Ải Ba chính thức bị bẻ khóa! Biểu tượng hoa tuyết trên bảng điều khiển {BOARD} vụt sáng chuyển sang màu xanh ngọc bích! Ếch Gỗ Bắc Cực đứng trên bàn điều khiển, khẽ hất chiếc khăn quàng len đỏ ra sau vai, nở một nụ cười đắc thắng về phía ống kính camera.
```
**Part 7** → `audio/vs/scene05_p7.wav` (353 ký tự) · mood `tram_bi_an`

```text
Nhưng tiếng vỗ tay vừa dứt thì cánh cửa tiếp theo mở toang ra một căn phòng kỳ dị chưa từng thấy: Mê Cung Bẫy Giải Mã của Cửa Ải Bốn! Đây không phải là bài toán về cơ bắp hay tốc độ. Đây là cuộc đấu trí cân não với các bẫy cơ học liên hoàn và mê cung gương quang học! Đã đến lúc cho các kỹ sư của pháo đài biết thế nào là chỉ số thông minh của loài quạ!
```
**Part 8** → `audio/vs/scene05_p8.wav` (774 ký tự) · mood `tram_bi_an`

```text
Nghiên cứu của giáo sư Storey tại đại học Carleton đã chứng minh: ếch gỗ Bắc Cực là bậc thầy số một thế giới về công nghệ bảo quản lạnh sinh học! Khi dịch cơ thể đông cứng, các tế bào của ếch gỗ mất đi bốn mươi phần trăm thể tích nước nhưng không hề bị vỡ màng tế bào nhờ lớp đệm phân tử glucose siêu đậm đặc! Chất urea tái hấp thu từ nước tiểu được giữ lại trong cơ bắp, đóng vai trò như chiếc phanh hãm tốc độ đóng băng, ngăn các tinh thể đá phát triển quá nhanh! Sau khi rã đông hoàn toàn, các tế bào của ếch gỗ lập tức kích hoạt chu trình thanh lọc lượng đường dư thừa, đưa nồng độ đường trong máu trở lại mức bình thường! Khả năng điều hòa trao đổi chất linh hoạt này khiến các nhà khoa học vũ trụ phải trầm trồ nghiên cứu để ứng dụng cho các chuyến bay liên hành tinh!
```

### scene06 — CÂU ĐỐ 8 BƯỚC, BẪY NƯỚC & QUẠ ĐEN
*Thẻ chương:* BẬC THẦY CHẾ TẠO CÔNG CỤ

*Badge:* `CỬA ẢI 4` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene06_p0.wav` (665 ký tự) · mood `don_dap`

```text
Cửa Ải Bốn không dùng áp suất gió, không dùng khí độc, cũng chẳng cần đến nhiệt độ băng giá. Đây là một mê cung cơ học được thiết kế để giam cầm những bộ não thông minh nhất! Ở trung tâm căn phòng là chiếc hộp điều khiển chính khóa chặt cánh cổng bước vào nửa sau pháo đài. Muốn mở được nó, kẻ đột nhập phải giải một chuỗi câu đố liên hoàn tám bước cực kỳ hóc búa! Các kỹ sư an ninh của pháo đài từng tự hào tuyên bố: nếu không có sách hướng dẫn sử dụng, một người trưởng thành cũng phải mất ít nhất hai ngày mới mò ra được quy luật! Bất kỳ một sai sót nào trong trình tự các bước cũng sẽ kích hoạt cơ chế khóa vĩnh viễn, chôn vùi chiếc chìa khóa xuống đáy hầm sâu!
```
**Part 1** → `audio/vs/scene06_p1.wav` (708 ký tự) · mood `hao_hung`

```text
Nhưng họ đã quên mất một điều: loài người không phải là sinh vật duy nhất biết tư duy logic trên hành tinh này! [laughter] Đặc vụ Quạ Đen chỉ mất đúng ba mươi giây để quan sát. Não bộ của loài quạ sở hữu mật độ tế bào thần kinh dày đặc ngang ngửa với các loài linh trưởng cấp cao, cho phép chúng hiểu rõ quy luật nhân quả trong chớp mắt! Nghiên cứu khoa học kinh điển của các nhà động vật học tại đại học Oxford và Cambridge đã chứng minh: quạ có thể tự mình giải câu đố cơ học tám bước liên hoàn ngay trong lần thử đầu tiên mà không cần bất kỳ sự huấn luyện nào! Chúng hiểu rõ khái niệm về công cụ gián tiếp: dùng công cụ A để lấy công cụ B, rồi dùng công cụ B để lấy mục tiêu C một cách hoàn toàn tự nhiên!
```
**Part 2** → `audio/vs/scene06_p2.wav` (506 ký tự) · mood `don_dap`

```text
Bước một: Quạ Đen nhặt một que gỗ ngắn trên sàn, thò mỏ khều chiếc que sắt dài hơn bị giấu sâu trong khe đá hẹp! Bước hai: chiếc que thép dài quá thẳng không móc được chốt? Không thành vấn đề! Quạ Đen kẹp đầu que vào kẽ nứt sàn đá, dùng mỏ uốn cong nó thành một chiếc lưỡi câu hoàn hảo! Bước ba: anh chàng dùng chiếc móc câu vừa chế tạo câu một túi sỏi đá nặng trĩu đặt trên giá cao xuống sàn! Bước bốn: tháo túi lấy sỏi, bay vút tới bên cạnh chiếc ống thủy tinh hẹp chứa chiếc chìa khóa nổi trên mặt nước!
```
**Part 3** → `audio/vs/scene06_p3.wav` (566 ký tự) · mood `tram_bi_an`

```text
Đây là bài kiểm tra trí tuệ ngụ ngôn Ê-dốp trứ danh trong giới khoa học sinh học! Quạ Đen có hiểu được quy luật dâng mực nước theo định luật thể tích hay không? Nếu thả xốp vào, xốp sẽ nổi lềnh bềnh và không làm dâng nước. Chỉ có sỏi đá đặc mới chiếm chỗ chất lỏng và đẩy chiếc chìa khóa lên miệng ống! Quạ Đen thậm chí còn không thèm liếc nhìn đĩa xốp nhựa! Anh chàng chỉ chọn đúng những viên sỏi đá đặc màu xám nặng nhất! Khả năng ước lượng thể tích chất lỏng của quạ chuẩn xác đến mức kinh ngạc, anh chàng dừng thả sỏi ngay khi chiếc chìa khóa vừa chạm miệng ống!
```
**Part 4** → `audio/vs/scene06_p4.wav` (458 ký tự) · mood `don_dap`

```text
Mực nước dâng lên! Chiếc chìa khóa đồng từ từ nổi lên sát miệng ống! Quạ Đen chỉ việc thò mỏ cắp lấy chìa khóa một cách ngon ơ! Bước năm: cắm chìa khóa vào ổ khóa số một, mở ngăn kéo chứa quả tạ sắt! Bước sáu và bước bảy: đẩy quả tạ sắt lăn qua máng trượt nghiêng, đè sập chiếc bẫy kẹp và nhả chốt hãm của ròng rọc trung tâm! Và bước tám cuối cùng: Quạ Đen bay lên ấn mạnh cần gạt tổng lực! Răng rắc... ầm! Cánh cổng sắt nặng hai tấn từ từ cuốn lên trần nhà!
```
**Part 5** → `audio/vs/scene06_p5.wav` (718 ký tự) · mood `tram_bi_an`

```text
Nhưng ngay khi cổng vừa mở, hệ thống camera nhận diện khuôn mặt của mê cung gương bắt đầu nhấp nháy đèn đỏ, cố gắng quét chân dung kẻ đột nhập để phát lệnh truy nã toàn cầu! Loài quạ có khả năng nhận diện và ghi nhớ khuôn mặt con người suốt hơn năm năm trời, và chúng cũng thừa biết camera hoạt động theo nguyên lý nào! Quạ Đen thò mỏ kẹp lấy một tấm gương nhỏ trên sàn, xoay ngược góc phản chiếu ánh sáng đèn pha chiếu thẳng vào ống kính camera giám sát! Chưa hết, anh chàng còn dùng mỏ cạy tung tấm ốp bảo vệ phía sau, làm ngắn mạch dây nguồn điều khiển khiến toàn bộ hệ thống camera nổ lách tách! Xèo xèo! Cảm biến camera bị lóa sáng chập mạch bốc khói đen! Toàn bộ hệ thống mê cung gương sụp đổ tín hiệu hoàn toàn!
```
**Part 6** → `audio/vs/scene06_p6.wav` (659 ký tự) · mood `hao_hung`

```text
Biểu tượng câu đố cơ học trên {BOARD} chuyển sang màu xanh ngọc bích rực rỡ! Bốn trên bảy cửa ải đã bị biệt đội đặc nhiệm chinh phục thành công! Quạ Đen bay sà xuống vai tượng đá, mỏ huýt sáo một điệu nhạc điệp viên vui nhộn, không quên vẫy cánh chào khán giả theo dõi qua màn hình. Nhưng từ sâu bên trong đường dẫn tới Cửa Ải Năm, tiếng nước chảy xiết ầm ầm như thác đổ bắt đầu vọng lại, làm rung chuyển cả sàn đá hoa cương. Hào nước ngầm áp lực cao của pháo đài đã mở van xả lũ! Lần này, chỉ có một bá chủ thực sự của đại dương mới có thể đối đầu với cơn thịnh nộ của thủy triều! Đại ca biển cả chuẩn bị xuất chiêu với những đợt sóng thần áp lực kinh hoàng!
```
**Part 7** → `audio/vs/scene06_p7.wav` (755 ký tự) · mood `don_dap`

```text
Trí tuệ của loài quạ đã vượt xa những gì con người từng tưởng tượng về thế giới loài chim! Chúng có thể nhớ mặt từng kẻ thù và truyền lại mối đe dọa này cho các thế hệ con cháu suốt nhiều năm trời! Khi đối đầu với mê cung gương, quạ đen hoàn toàn hiểu rằng hình ảnh trong gương chỉ là sự phản chiếu quang học chứ không phải là một con quạ đối thủ! Khả năng tư duy trừu tượng này cho phép chúng giải quyết các bài toán hóc búa một cách bình tĩnh, không hề mắc bẫy tâm lý của các kỹ sư pháo đài! Mỗi một bước đi trong mê cung giải đố của Quạ Đen đều được tính toán chuẩn xác như một đại kiện tướng cờ vua quốc tế! Anh chàng không chỉ mở được cổng mà còn thu gom luôn một mẩu dây đồng sáng loáng nhét vào túi áo làm kỷ niệm cho bộ sưu tập cá nhân! [laughter]
```

### scene07 — LẠC ĐÀ NHAI XƯƠNG RỒNG & BÁCH THANH CẮM GAI NHẦM CHÌA KHÓA
*Thẻ chương:* TAI NẠN KỸ THUẬT CƯỜI RA NƯỚC MẮT

*Badge:* `HẬU TRƯỜNG 2` · *mood mặc định:* `bi_hai`

**Part 0** → `audio/vs/scene07_p0.wav` (619 ký tự) · mood `bi_hai`

```text
[sigh] Nếu bạn nghĩ một biệt đội đặc nhiệm gồm mười loài động vật hoang dã có thể phối hợp ăn ý như quân đội hoàng gia... thì bạn đã đánh giá quá cao tính kỷ luật của giới tự nhiên rồi! [laughter] Ngay giữa thời khắc căng thẳng chuẩn bị bước vào trận chiến đường thủy của Cửa Ải Năm, một chuỗi âm thanh rùng rợn bỗng nhiên nổ ra trên kênh liên lạc tần số cao. Rộp! Rộp! Xoàn xoạt! Rộp! Tiếng động kinh hoàng đến mức Chim Cắt Lớn giật thót mình suýt ngã khỏi thành đá, còn Quạ Đen thì vội vàng ôm đầu tưởng pháo đài sập! "Báo động đỏ! Kẻ địch đang dùng súng máy nghiền nát công sự của chúng ta! Yêu cầu hỗ trợ khẩn cấp!"
```
**Part 1** → `audio/vs/scene07_p1.wav` (684 ký tự) · mood `nghiem_trang_gia`

```text
Chỉ Huy Mật Vụ vội vàng điều chỉnh tần số thu âm, phóng to nguồn phát tín hiệu trên radar định vị vệ tinh. Và hình ảnh hiện lên trên màn hình chính khiến tất cả ngã ngửa! Chiếc micro dã chiến gắn trên cổ áo của Lạc Đà Sa Mạc đang thu trọn từng tiếng nhai giòn rụm của những chiếc gai xương rồng dài năm phân bị nghiền nát thành bã! Bên trong vòm miệng và má của lạc đà có hàng trăm mấu thịt hình nón bằng chất sừng cứng ngắc, hướng thẳng vào phía cuống họng giúp bẻ gãy mọi mũi gai nhọn mà không làm xước niêm mạc miệng! "Đặc vụ Lạc Đà! Cậu có biết chiếc micro đó có giá bằng cả năm tiền trợ cấp đi lại của cậu không hả? Tắt mic ngay trước khi tôi biến cậu thành chiếc thảm trải sàn!"
```
**Part 2** → `audio/vs/scene07_p2.wav` (259 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Dạ... cháu xin lỗi Chỉ Huy! Tại nhai xương rồng đỡ khát nước quá nên cháu quên mất là mic vẫn đang bật ạ! Cháu xin hứa nhai khẽ lại ạ! [laughter] Xương rồng này ngọt lắm sếp ơi, có nhiều nước chuyển hóa giúp tế bào máu oval của cháu căng tràn sức sống luôn ạ!
```
**Part 3** → `audio/vs/scene07_p3.wav` (521 ký tự) · mood `tram_bi_an`

```text
Cơn giận của Chỉ Huy còn chưa kịp hạ nhiệt thì tai họa thứ hai ập đến từ vị trí cảnh giới trên cây cổ thụ ngoài sân pháo đài. Lần này là từ Đặc vụ Chim Bách Thanh! Bách Thanh có một bản năng nghề nghiệp ăn sâu vào máu: hễ nhìn thấy bất kỳ vật thể nào có giá trị hoặc con mồi nào, anh chàng đều phải mang đi cắm chặt lên một chiếc gai nhọn để cất giữ làm kho lương thực dự trữ! Và bi kịch là chiếc thẻ từ màu đỏ đó chính là chiếc chìa khóa dự phòng duy nhất của Tổng Cục Trưởng Mật Vụ để kích hoạt cửa thoát hiểm khẩn cấp!
```
**Part 4** → `audio/vs/scene07_p4.wav` (347 ký tự) · 🎭 cameo `tham_phan`

```text
Báo cáo Chỉ Huy: tôi vừa phát hiện một vật thể hình chữ nhật có nguy cơ rơi vào tay kẻ địch! Tôi đã thực hiện biện pháp nghiệp vụ tiêu chuẩn: xiên nó lên chiếc gai cao mười mét để bảo quản an toàn suốt ba ngày tới! Đây là kỹ thuật lưu trữ an toàn cấp độ năm sao của dòng họ nhà tôi, bảo đảm chim ưng hay cáo hoang cũng không thể nào lấy trộm được!
```
**Part 5** → `audio/vs/scene07_p5.wav` (530 ký tự) · mood `bi_hai`

```text
[sigh] "Bách Thanh ơi là Bách Thanh! Đó là chiếc thẻ từ mở cửa thoát hiểm của cả đội đấy! Cậu xiên thủng nó thế kia thì lát nữa chúng ta thoát bằng niềm tin à?" Chưa hết, thảm kịch hậu trường thứ ba lại xuất hiện ngay dưới chân bàn làm việc của phòng tác chiến ngầm. Lực lượng Kiến Cắt Lá vừa hoàn thành một chiến dịch bất ngờ! Chim Cắt Lớn vừa bay về nghỉ chân, cúi xuống nhìn chiếc áo khoác điệp viên sang trọng của mình thì phát hiện: toàn bộ phần vạt áo và chiếc cà vạt lụa đắt tiền đã bị xẻo nham nhở không còn một manh giáp!
```
**Part 6** → `audio/vs/scene07_p6.wav` (338 ký tự) · 🎭 cameo `be_con`

```text
Báo cáo: đơn vị công binh chúng em phát hiện loại vải này có hàm lượng xen-lu-lô-zơ siêu cao, rất thích hợp để mang về hầm làm phân bón trồng vườn nấm cộng sinh ạ! Cảm ơn bác chim cắt đã tài trợ! Vườn nấm Leucocoprinus của chúng em được bón lụa thượng hạng này sẽ cho ra những mẻ nấm ngon nhất lịch sử năm mươi triệu năm nông nghiệp kiến!
```
**Part 7** → `audio/vs/scene07_p7.wav` (319 ký tự) · mood `hao_hung`

```text
Chim Cắt tức đến nỗi lông đầu dựng đứng, xòe cánh đòi lao vào mổ kiến, trong khi bầy kiến tí hon thì giơ hàm răng kim loại lên thách thức! "Trật tự ngay! Tất cả lập tức về vị trí chiến đấu trước khi tôi trừ toàn bộ lương thưởng của cả mười đứa!" Tiếng quát uy lực của Chỉ Huy Mật Vụ vang dội làm rung chuyển cả căn hầm.
```
**Part 8** → `audio/vs/scene07_p8.wav` (560 ký tự) · mood `tram_bi_an`

```text
Toàn đội lập tức nín thở, đứng nghiêm như những bức tượng. Trò đùa chấm dứt khi màn hình theo dõi hào nước ngầm chuyển sang màu đỏ báo động lũ quét! Cửa Ải Năm: Hào Nước Áp Lực Cao đang đón chờ. Bể nước dã chiến từ từ hạ xuống mép đập nước ngầm. Cá Voi Sát Thủ lặn sâu xuống làn nước lạnh, vây lưng nhô cao rẽ sóng, chiếc ăng-ten phát sóng sonar bắt đầu phát ra những tiếng nhấp chuột đanh gọn xuyên qua lòng đá. Trận hải chiến dưới lòng đất chính thức khai hỏa! Đại ca biển cả chuẩn bị thể hiện sức mạnh của sóng âm sonar và cú quất đuôi sóng thần kinh hoàng!
```
**Part 9** → `audio/vs/scene07_p9.wav` (754 ký tự) · mood `bi_hai`

```text
[sigh] "Chỉ Huy ơi, nhai xương rồng này đã lắm, hay là Tổng Cục nhập khẩu cho cháu một tấn về để ở căng-tin dã chiến đi ạ!" Chim Bách Thanh thì nghiêm túc giải thích: "Xiên đồ lên gai là biện pháp bảo mật sinh học tối tân nhất! Không một tên trộm nào dám leo lên bụi gai bồ kết cao mười mét để lấy trộm thẻ từ đâu ạ!" [laughter] Đại Đội Kiến Cắt Lá cũng gửi báo cáo phụ: "Mảnh vải áo lụa của bác chim cắt đã được đưa vào khoang ủ nấm số một, dự kiến sẽ thu hoạch được mẻ nấm siêu to khổng lồ vào sáng mai ạ!" Lạc Đà Sa Mạc hứa chắc nịch: "Lần sau cháu sẽ nhai cỏ khô êm dịu như nhung, bảo đảm không làm rè sóng bộ đàm của cả đội nữa đâu ạ!" Chỉ Huy Cú Mèo chỉ biết thở dài bật cười: "Thôi được rồi, nhớ giữ lời hứa đấy, anh chàng xe tăng sa mạc của tôi!"
```

### scene08 — CHIẾN HÀO THỦY QUÂN & CÁ VOI SÁT THỦ
*Thẻ chương:* XUNG SONAR 225 DB VÀ SÓNG THẦN MINI

*Badge:* `CỬA ẢI 5` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene08_p0.wav` (700 ký tự) · mood `don_dap`

```text
Hào nước ngầm của Pháo Đài Tự Nhiên là một mê cung thủy lực tối tăm và hung hãn. Dòng nước đen kịt cuộn xoáy với vận tốc kinh hoàng, tạo nên những dòng xoáy ngầm có thể xé toạc bất kỳ tàu ngầm quân sự nào! Độ sâu hơn bốn mươi mét dưới mặt đất, ánh sáng mặt trời không bao giờ rọi tới được đây. Tầm nhìn quang học bằng không tròn trĩnh. Các camera thủy văn chỉ thu về một màu đen đặc quánh như mực! Nhưng trong bóng tối vĩnh cửu ấy, một bóng đen khổng lồ nặng sáu tấn mang hai màu đen trắng tương phản đang lướt đi nhẹ nhàng như một chiếc bóng ma đại dương! Cơ thể thủy động lực học hình thoi giúp cá voi sát thủ giảm thiểu tối đa lực ma sát nhớt của nước, lướt đi êm ái như một quả ngư lôi tàng hình!
```
**Part 1** → `audio/vs/scene08_p1.wav` (647 ký tự) · mood `tram_bi_an`

```text
Cản đường phía trước là một cánh cửa van ngăn lũ bằng thép tôi dày nửa mét, khóa chặt bởi ba chiếc chốt thủy lực áp suất cao. Không có chìa khóa, cũng không có chỗ để gài thuốc nổ. "Đặc vụ Cá Voi Sát Thủ, chúng ta không nhìn thấy điểm yếu của cánh cửa đập. Cậu phải tự tìm đường phá chốt trong bóng tối!" Giọng Chỉ Huy vang lên qua bộ đàm chống nước. Cá Voi Sát Thủ không cần mắt để nhìn. Anh chàng sở hữu cỗ máy radar âm thanh sinh học tối tân nhất từng được tạo hóa tạo ra! Khối mỡ dưa hấu đặc biệt trên trán cá voi hoạt động như một thấu kính quang học âm thanh, hội tụ các sóng siêu âm phân tán thành một chùm tia hẹp có độ phân giải siêu nét!
```
**Part 2** → `audio/vs/scene08_p2.wav` (767 ký tự) · mood `don_dap`

```text
Tách! Tách! Tách! Những chùm xung âm thanh định vị cực ngắn bắt đầu được bắn ra liên hồi từ khối dầu trán của cá voi sát thủ! Cường độ âm thanh tăng vọt lên mức cực đại: hai trăm hai mươi lăm đê-xi-ben! Đây là mức áp suất âm thanh dưới nước khủng khiếp nhất trong thế giới sinh vật! Các chùm sóng âm thanh hai trăm hai mươi lăm đê-xi-ben chạm vào cánh cửa đập bằng thép, dội ngược trở lại hàm dưới của cá voi và truyền thẳng vào tai trong với độ phân giải siêu nét! Phát hiện mục tiêu! Điểm yếu nằm ở chiếc then cài thủy lực số hai bên dưới góc phải, nơi các bu-lông kim loại đã bị nước xói mòn tạo ra một kẽ hở đúng năm mi-li-mét! Âm thanh dội về chi tiết đến mức cá voi có thể phân biệt được độ dày của lớp rỉ sét và hướng ứng suất của từng chiếc đinh tán kim loại!
```
**Part 3** → `audio/vs/scene08_p3.wav` (564 ký tự) · mood `hao_hung`

```text
Cá Voi Sát Thủ lùi lại năm mươi mét để lấy đà. Không cần súng phóng lựu, vũ khí của đại ca đại dương chính là kỹ thuật tạo sóng thần đồng bộ trứ danh từng khiến các nhà khoa học biển kinh ngạc! Các nghiên cứu tại vùng biển Nam Cực ghi nhận: loài cá voi sát thủ có thể phối hợp bơi nước rút và quất mạnh chiếc vây đuôi để tạo nên những bức tường sóng thần cao hơn một mét rưỡi, thổi bay mục tiêu trên các tảng băng trôi! Và hôm nay, trong không gian khép kín của hào ngầm, uy lực của con sóng này sẽ bị nén lại thành một cú đấm thủy lực có sức tàn phá gấp mười lần!
```
**Part 4** → `audio/vs/scene08_p4.wav` (762 ký tự) · mood `don_dap`

```text
Tăng tốc! Cá Voi Sát Thủ phóng vút đi với vận tốc nước rút kinh hoàng: năm mươi sáu cây số một giờ! Thân hình sáu tấn lao đi như một quả ngư lôi sống! Cách cánh cửa đập đúng năm mét, anh chàng bất ngờ thực hiện một cú quay ngoắt một trăm tám mươi độ điệu nghệ, quất toàn bộ sức mạnh của cơ đuôi khổng lồ xuống mặt nước! Ầm! Một bức tường sóng thủy lực cao vút bị ép chặt trong khe đá, lao thẳng vào chiếc then cài bị nứt với áp suất hàng trăm tấn trên một mét vuông! Răng rắc... rầm! Chiếc then cài thủy lực bị uốn cong rồi gãy vụn! Cánh cửa van thép khổng lồ bị sức nước xô ngã ngửa ra sau, mở toang một lỗ hổng đường kính ba mét! Áp suất nước giải phóng tạo nên một cơn lốc xoáy nước xoáy tròn cuốn phăng toàn bộ rác rưởi và chướng ngại vật dưới lòng hào ngầm!
```
**Part 5** → `audio/vs/scene08_p5.wav` (461 ký tự) · mood `hao_hung`

```text
Mực nước trong hào ngầm tụt dốc không phanh! Lòng hào trơ ra những phiến đá cuội trơn nhẵn, mở ra một lối đi bộ khô ráo cho toàn bộ biệt đội đặc nhiệm! Cá Voi Sát Thủ nhô nửa thân mình lên mặt nước ở đoạn kênh thông thoáng, phun một cột nước trắng xóa lên trần hang, cất tiếng kêu éc éc đắc thắng qua micro! Biểu tượng sóng nước của Cửa Ải Năm trên {BOARD} nhấp nháy rồi chuyển sang màu xanh ngọc bích rực rỡ! Năm trên bảy cửa ải đã bị biệt đội hạ gục gọn gàng!
```
**Part 6** → `audio/vs/scene08_p6.wav` (452 ký tự) · mood `tram_bi_an`

```text
Nhưng thử thách phía trước mới thực sự là bài kiểm tra độ cứng của hộp sọ và tinh thần đồng đội: Boong-ke Bê Tông Cốt Thép của Cửa Ải Sáu! Đạn pháo thông thường bắn vào đây chỉ để lại một vết xước nhỏ. Muốn phá vỡ bức tường này, chúng ta cần sự kết hợp giữa một chiếc búa khoan sinh học có lực gia tốc hàng ngàn G và một đại đội công binh tí hon có hàm răng thép! Cặp đôi búa khoan và máy đào đất chuẩn bị thực hiện màn công phá ngoạn mục chưa từng có!
```
**Part 7** → `audio/vs/scene08_p7.wav` (785 ký tự) · mood `don_dap`

```text
Sóng âm sonar của cá voi sát thủ mạnh đến mức có thể làm choáng váng các loài cá nhỏ xung quanh chỉ bằng một tiếng nhấp chuột âm thanh đanh thép! Hệ thống não bộ khổng lồ nặng tới năm ki-lô-gam của cá voi sát thủ có thể phân tích hàng triệu tín hiệu âm thanh dội về trong một phần nghìn giây, tái hiện lại cấu trúc không gian ba chiều hoàn hảo! Cú quất đuôi sóng thần của đại ca biển cả đã chứng minh sức mạnh cơ học vô song của loài động vật có vú thống trị toàn bộ chuỗi thức ăn đại dương! Sức mạnh của bầy cá voi sát thủ không chỉ nằm ở cơ bắp mà còn nằm ở sự truyền thừa tri thức săn mồi qua hàng trăm thế hệ gia tộc mẫu hệ! Cánh cửa van đập nước ngầm bị đánh sập là minh chứng hùng hồn cho thấy không một công trình nhân tạo nào có thể ngăn cản được sức mạnh của đại dương bao la!
```

### scene09 — BOONG-KE ĐÁ GRANITE, CHIM GÕ KIẾN & KIẾN CẮT LÁ
*Thẻ chương:* TRIỆT TIÊU 1200G VÀ CÔNG BINH RĂNG THÉP

*Badge:* `CỬA ẢI 6` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene09_p0.wav` (723 ký tự) · mood `don_dap`

```text
Bức tường Boong-ke của Cửa Ải Sáu là chướng ngại vật vật lý kiên cố nhất trong toàn bộ Pháo Đài Tự Nhiên. Các khối đá granite đen dày hai mét được ghép khít khao đến mức một lưỡi dao cạo cũng không thể lách qua! Độ cứng của đá granite nằm ở thang điểm bảy trên thang độ cứng khoáng vật, chỉ đứng sau ngọc bích và kim cương. Mọi nỗ lực dùng búa tạ của con người đập vào đây sẽ chỉ làm mẻ búa và gãy tay kẻ đập! Nhưng đêm nay, pháo đài phải đối đầu với một cỗ máy khoan sinh học sở hữu chiếc đầu có khả năng triệt tiêu xung chấn thần kỳ nhất vũ trụ: Đặc vụ Chim Gõ Kiến! Cơ bắp cổ của chim gõ kiến được cấu tạo từ các bó cơ xoắn siêu dày, có thể phát ra lực đẩy tương đương với một chiếc búa tạ mini bổ xuống bề mặt mục tiêu!
```
**Part 1** → `audio/vs/scene09_p1.wav` (796 ký tự) · mood `tram_bi_an`

```text
Hãy tưởng tượng lực va chạm khủng khiếp mà đầu chim gõ kiến phải chịu đựng trong mỗi cú mổ. Các nhà cơ sinh học tại đại học Bắc Kinh đã gắn các cảm biến siêu vi để đo đạc và thu về những con số rùng mình! Khi gõ vào thân cây gỗ hay đá cứng, đầu của chim gõ kiến phải chịu một lực gia tốc va đập lên tới một ngàn hai trăm G! Và anh chàng không chỉ gõ một lần rồi nghỉ. Tần số mổ của chim gõ kiến đạt tới hai mươi lần một giây, với vận tốc đầu mỏ lao tới sáu mét một giây! Với lực đập một ngàn hai trăm G lặp lại hai mươi lần một giây, bất kỳ bộ não sinh vật nào cũng sẽ bị dập nát thành cháo. Nhưng Chim Gõ Kiến vẫn tỉnh táo, minh mẫn và mắt sáng như sao! Màng nháy mắt của chim gõ kiến tự động đóng sập lại một phần nghìn giây trước mỗi cú va chạm, giữ cho nhãn cầu không bị văng ra khỏi hốc mắt!
```
**Part 2** → `audio/vs/scene09_p2.wav` (615 ký tự) · mood `hao_hung`

```text
Bí mật nằm ở bộ giáp chống rung chấn ba lớp tinh vi mà tạo hóa đã ban tặng cho loài chim này! Thứ nhất, chiếc xương móng hyoid của chim gõ kiến không nằm ở cuống họng như người, mà dài ngoằng, quấn một vòng từ đáy hàm vòng qua sau gáy lên tận đỉnh đầu rồi chui vào lỗ mũi! Thứ hai, mỏ trên dài hơn mỏ dưới đúng một mi-li-mét, giúp chuyển hướng các sóng xung kích gây hại thành sóng trượt vô hại đi xuống thân mình! Và thứ ba, xương sọ của chim gõ kiến là một cấu trúc xốp vi mô chứa vô số lỗ rỗng chứa không khí, đóng vai trò như chiếc đệm khí lò xo đàn hồi triệt tiêu toàn bộ chấn động trước khi chạm tới màng não!
```
**Part 3** → `audio/vs/scene09_p3.wav` (569 ký tự) · mood `don_dap`

```text
Tọa độ điểm yếu của bức tường đã được quét xong! Đó là ba điểm nứt ứng suất ngầm nơi ba khối đá granite giao nhau! Khai hỏa! Chim Gõ Kiến bám chặt bốn móng vuốt vào vách đá, đuôi tì làm điểm tựa kiên cố, bắt đầu chuỗi khoan phá thần tốc! Cốc cốc cốc cốc cốc cốc cốc! Tiếng mỏ va chạm vào đá granite rít lên như tiếng súng máy liên thanh, các tia lửa điện nổ lách tách chói lòa trong bóng tối! Chỉ trong vòng bốn mươi lăm giây, ba lỗ khoan tròn sâu mười phân đã xuất hiện ngay trên tim của các khối đá! Các vết nứt chân chim bắt đầu lan rộng ra xung quanh như mạng nhện!
```
**Part 4** → `audio/vs/scene09_p4.wav` (776 ký tự) · mood `hao_hung`

```text
Đến lượt lực lượng công binh bí mật vào sân! Chim Gõ Kiến lùi lại nhường đường cho Đại Đội Kiến Cắt Lá xuất kích! Đừng coi thường những chú kiến nhỏ bé này! Nghiên cứu mới nhất đăng trên tạp chí Báo Cáo Khoa Học của Nature đã phát hiện: hàm răng của kiến cắt lá được tẩm một lớp kim loại nặng gồm kẽm và mangan nguyên chất! Lớp kim loại nặng này biến chiếc hàm răng chitin của kiến cắt lá thành những lưỡi cưa tẩm thép không gỉ, sắc bén và bền bỉ gấp ba lần răng của côn trùng thông thường! Hàng ngàn chú kiến cắt lá cùng lúc thò hàm răng thép vào các kẽ nứt do chim gõ kiến vừa tạo ra, bắt đầu nghiền nát và bốc dỡ từng hạt bụi đá granite ra ngoài! Khả năng khuân vác gấp năm mươi lần trọng lượng cơ thể giúp bầy kiến dọn sạch hàng tạ đá vụn chỉ trong vòng chưa đầy hai phút!
```
**Part 5** → `audio/vs/scene09_p5.wav` (451 ký tự) · mood `don_dap`

```text
Khoét móng! Đục rãnh! Bẩy then! Đại đội công binh kiến cắt lá đào khoét chân tường đá với tốc độ của một cỗ máy xúc công nghiệp hiện đại! Toàn bộ khối đá granite nặng mười tấn bắt đầu nghiêng dần về phía trước. Chim Gõ Kiến bay lên, tung cú mổ quyết định cuối cùng vào chiếc chốt bản lề trên đỉnh! Rầm! Khối đá granite khổng lồ đổ sập xuống sàn đá, vỡ tan thành những mảnh đá vụn vô hại, mở toang một cửa vòm rộng thênh thang dẫn thẳng vào Cửa Ải Bảy!
```
**Part 6** → `audio/vs/scene09_p6.wav` (336 ký tự) · mood `hao_hung`

```text
Biểu tượng boong-ke đá trên {BOARD} chuyển sang màu xanh ngọc bích rực rỡ! Sáu trên bảy cửa ải đã bị biệt đội đặc nhiệm đánh sập không còn một dấu vết! Chim Gõ Kiến đậu trên đống đá vụn, giơ chiếc mỏ nhọn hoắt lên trời làm động tác gõ tạ ơn khán giả, bên cạnh là đàn kiến cắt lá đang vẫy những mảnh lá xanh ăn mừng chiến thắng vang dội!
```
**Part 7** → `audio/vs/scene09_p7.wav` (481 ký tự) · mood `tram_bi_an`

```text
Nhưng cánh cửa cuối cùng ngăn cách biệt đội với kho báu trung tâm đang hiện ra trước mắt: Cửa Ải Bảy — Bức Tường Vách Đứng Chín Mươi Độ và Lò Lửa Sa Mạc Năm Mươi Độ C! Không thể bay qua vì bão nhiệt cuốn phăng mọi luồng khí, cũng không thể đào hầm vì nền cát lún di động. Chỉ có sự phối hợp giữa một cỗ xe tăng chịu nhiệt và một bậc thầy leo vách đá mới có thể giải mã cánh cửa tối thượng này! Cặp đôi sa mạc và vách đá chuẩn bị bước vào cuộc chinh phục đỉnh cao nhất của pháo đài!
```
**Part 8** → `audio/vs/scene09_p8.wav` (796 ký tự) · mood `hao_hung`

```text
Để bảo vệ đôi mắt khỏi bụi đá và chấn động cực mạnh, mi mắt của chim gõ kiến có thể tự động co thắt các mạch máu quanh võng mạc để duy trì huyết áp ổn định trong từng cú mổ! Trong khi đó, lớp kim loại kẽm và mangan trên răng của kiến cắt lá được phân bố đồng đều đến mức độ nguyên tử, giúp chiếc răng không bao giờ bị mẻ dù cắn vào đá granite cứng nhất! Sự kết hợp giữa công nghệ khoan va đập của loài chim và công nghệ cưa cắt kim loại của loài kiến đã tạo nên một kỳ tích công binh chưa từng có trong lịch sử điệp viên! Nhịp gõ búa thần tốc hai mươi lần một giây của chim gõ kiến tạo nên một bản hòa âm cơ học rộn rã làm bừng tỉnh cả góc pháo đài tối tăm! Hàng ngàn chú kiến cắt lá đồng loạt vác đá diễu hành dưới ánh đèn pin thợ mỏ, tạo nên một cảnh tượng công binh hoành tráng chưa từng thấy!
```

### scene10 — DÊ NÚI LEO VÁCH 90° & LẠC ĐÀ VƯỢT SA MẠC 50°C
*Thẻ chương:* MÓNG CAO SU GIÁC HÚT VÀ MÁU OVAL GIÃN NỞ

*Badge:* `CỬA ẢI 7` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene10_p0.wav` (567 ký tự) · mood `don_dap`

```text
Cửa Ải Bảy là phòng tuyến cuối cùng và khắc nghiệt nhất của Pháo Đài Tự Nhiên: Lò Lửa Sa Mạc kết hợp với Bức Tường Vách Đứng Chín Mươi Độ! Nhiệt độ trên mặt cát sa mạc lúc này đo được là năm mươi độ C! Không khí khô khốc như lò nung có thể hút cạn từng giọt nước trong cơ thể của bất kỳ sinh vật nào chỉ trong vòng chưa đầy mười lăm phút! Mọi phương tiện cơ giới mang vào đây đều sẽ bị cát lún nuốt chửng bánh xe, động cơ quá nhiệt và bốc cháy. Gió sa mạc cuốn theo những cơn bão bụi silic sắc nhọn có thể làm xước rách giác mạc và phá hủy hệ hô hấp của người thường!
```
**Part 1** → `audio/vs/scene10_p1.wav` (505 ký tự) · mood `hao_hung`

```text
Nhưng kẻ đang ung dung sải bước trên chảo cát nóng rẫy này lại chính là cỗ xe tăng sinh học tối thượng của hoang mạc: Đặc vụ Lạc Đà Sa Mạc! Trên lưng Lạc Đà không chở súng đạn, mà đang cõng theo người đồng đội leo núi cừ khôi nhất: Đặc vụ Dê Núi Bắc Mỹ! Cặp bài trùng này chuẩn bị thực hiện màn phối hợp ngoạn mục nhất lịch sử điệp viên! Bí mật nào giúp Lạc Đà Sa Mạc thản nhiên vượt qua vùng nhiệt độ năm mươi độ C mà không hề nhỏ một giọt mồ hôi? Hãy nhìn sâu vào hệ tuần hoàn kỳ diệu của anh chàng này!
```
**Part 2** → `audio/vs/scene10_p2.wav` (1127 ký tự) · mood `tram_bi_an`

```text
Tất cả các loài động vật có vú trên Trái Đất, bao gồm cả con người, đều có tế bào hồng cầu hình tròn dẹt. Khi cơ thể mất nước, hồng cầu tròn sẽ dính bết lại làm tắc nghẽn mạch máu, dẫn đến đột quỵ. Nhưng hồng cầu của Lạc Đà lại có hình bầu dục thuôn dài! Cấu trúc oval đặc biệt này cho phép chúng tiếp tục lưu thông trơn tru ngay cả khi máu trở nên đặc quánh do cơ thể mất tới hai mươi lăm phần trăm lượng nước! Và khi gặp nguồn nước, hồng cầu hình bầu dục của lạc đà có thể giãn nở tới hai trăm bốn mươi phần trăm thể tích mà không hề bị vỡ! Anh chàng có thể nạp một trăm lít nước chỉ trong mười phút ngắn ngủi! Chưa hết, thân nhiệt của Lạc Đà Sa Mạc là một cỗ máy điều hòa nhiệt độ sinh học tự động: ban đêm hạ xuống ba mươi tư độ C để tích trữ khí lạnh, ban ngày tăng dần lên bốn mươi mốt độ C mà không cần đổ mồ hôi làm mát! Cộng thêm chiếc mũi xoắn ốc khổng lồ tái hấp thu tới sáu mươi phần trăm hơi ẩm từ hơi thở ra, Lạc Đà có thể đi bộ xuyên qua chảo lửa sa mạc mà chẳng tốn lấy một giọt mồ hôi! Bướu mỡ trên lưng khi bị oxy hóa còn sản sinh ra hơn một trăm gam nước chuyển hóa cho mỗi một trăm gam chất béo bị tiêu hao!
```
**Part 3** → `audio/vs/scene10_p3.wav` (485 ký tự) · mood `don_dap`

```text
Lạc Đà sải những bước chân thần tốc, đưa Dê Núi tiếp cận sát chân ngọn tháp đá granite nguyên khối trong tiếng reo hò của phòng chỉ huy! Trước mặt họ là bức tường thành dựng đứng chín mươi độ cao ba mươi mét! Bề mặt đá nhẵn thín như gương, không một kẽ nứt, không một mấu gờ nhô ra quá ba mi-li-mét! Bất kỳ một vận động viên leo núi chuyên nghiệp nào nhìn vào vách đá này cũng phải lắc đầu bỏ cuộc. Nhưng đối với Dê Núi Bắc Mỹ, đây chỉ là một cầu thang quen thuộc hàng ngày! [laughter]
```
**Part 4** → `audio/vs/scene10_p4.wav` (625 ký tự) · mood `hao_hung`

```text
Vũ khí bí mật của Đặc vụ Dê Núi nằm ở bốn chiếc móng guốc thách thức mọi định luật vật lý! Viền ngoài của móng là lớp sừng cứng sắc nhọn có thể găm chặt vào những vi gờ đá chỉ dày một mi-li-mét. Trong khi phần lòng móng là lớp đệm cao su dẻo ma sát cực cao, hoạt động như những chiếc giác hút chân không bám dính vào mặt đá! Cộng thêm tầm nhìn bao quát ba trăm hai mươi độ và cấu trúc khớp vai lực lưỡng, dê núi có thể kéo toàn bộ trọng lượng cơ thể lên chỉ bằng hai chiếc móng trước! Trọng tâm cơ thể đặt cực thấp cùng xương sườn hẹp giúp dê núi ép sát ngực vào vách đá, triệt tiêu hoàn toàn mô-men quay làm lật ngửa cơ thể!
```
**Part 5** → `audio/vs/scene10_p5.wav` (653 ký tự) · mood `don_dap`

```text
Xuất kích! Dê Núi Bắc Mỹ nhún mình bật nhảy một cú ngoạn mục lên vách đá dựng đứng chín mươi độ! Một bước... hai bước... ba bước! Dê Núi leo ngược lên vách đá thẳng đứng với tốc độ thoăn thoắt như đang chạy trên mặt đất bằng phẳng! Gió lốc sa mạc thổi giật từng cơn dữ dội, nhưng bốn chiếc móng giác hút cao su của anh chàng vẫn bám dính chặt chẽ không hề lung lay dù chỉ một ly! Cách đỉnh tháp năm mét! Mỏm đá cuối cùng bị gãy vụn dưới chân! Dê Núi treo lơ lửng trên không trung chỉ bằng hai chiếc móng trước! Cả phòng chỉ huy nín thở! Gồng cơ vai! Dê Núi vung một chân sau lên mỏm đá, tung cú bật nhảy tối thượng cuối cùng phi thẳng lên sàn đỉnh tháp!
```
**Part 6** → `audio/vs/scene10_p6.wav` (409 ký tự) · mood `hao_hung`

```text
Đến lượt hạ cầu! Dê Núi đạp mạnh vào chiếc cần gạt tời cáp khổng lồ đặt trên đỉnh tháp! Rầm! Chiếc cầu treo rút khổng lồ bắc ngang qua thung lũng sa mạc hạ xuống, nối liền lối vào thẳng vào cổng chính của Phòng Châu Báu Trung Tâm! Toàn bộ bảy biểu tượng cửa ải trên {BOARD} đồng loạt chuyển sang màu xanh ngọc bích rực rỡ! Một trăm phần trăm hệ thống an ninh của Pháo Đài Tự Nhiên đã bị vô hiệu hóa hoàn toàn!
```
**Part 7** → `audio/vs/scene10_p7.wav` (401 ký tự) · mood `tram_bi_an`

```text
Cả mười đặc vụ tập hợp trước cánh cổng sắt mạ vàng của Phòng Châu Báu. Nhưng đúng lúc này, từ trong bóng tối của hành lang ngoại vi, một đội tuần tra người máy tự động bất ngờ xuất hiện bao vây lối thoát! Chỉ Huy Mật Vụ khẽ nhếch mép: "Đừng lo. Chúng ta vẫn còn một tay súng bắn tỉa đang ẩn nấp trên cao chưa từng lộ diện!" Tay súng bắn tỉa bí mật chuẩn bị khai hỏa dọn sạch hậu phương trong chớp mắt!
```
**Part 8** → `audio/vs/scene10_p8.wav` (738 ký tự) · mood `hao_hung`

```text
Lạc Đà Sa Mạc có thể mất tới ba mươi phần trăm trọng lượng cơ thể do mất nước mà vẫn đi bộ bình thường, trong khi các loài thú khác sẽ chết vì trụy tim nếu mất mười lăm phần trăm nước! Dê Núi Bắc Mỹ thì sở hữu cặp sừng đen rỗng bên trong giúp phân tán nhiệt lượng cơ thể khi vận động mạnh trên vách đá cheo leo! Bộ đôi sa mạc và vách đá đã chứng minh rằng không có địa hình nào trên Trái Đất có thể ngăn cản bước chân của những kẻ nắm vững nghệ thuật thích nghi! Bức tường đá dựng đứng chín mươi độ từng là nỗi khiếp sợ của muôn loài nay đã in dấu bốn móng guốc cao su kiêu hãnh của Dê Núi Bắc Mỹ! Lạc Đà Sa Mạc đứng dưới chân tháp ngước nhìn người đồng đội trên cao, cất tiếng kêu hò reo cổ vũ nồng nhiệt vang vọng khắp lòng chảo sa mạc!
```

### scene11 — SÁT THỦ BÁCH THANH & CHIẾN THUẬT CẮM GAI NHỌN
*Thẻ chương:* VÔ HIỆU HÓA TOÀN BỘ ĐỘI TUẦN TRA

*Badge:* `TRẠM GÁC NGOẠI VI` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene11_p0.wav` (691 ký tự) · mood `tram_bi_an`

```text
Bên ngoài cổng Phòng Châu Báu, không khí căng thẳng đến nghẹt thở. Đội tuần tra an ninh tự động của Pháo Đài Tự Nhiên đã phát hiện ra các dấu vết xâm nhập bất thường! Những chiếc loa phát thanh trên tường chuẩn bị phát tín hiệu báo động đỏ toàn căn cứ. Nếu tiếng còi báo động vang lên, toàn bộ các lối thoát hiểm sẽ bị đánh sập vĩnh viễn, chôn vùi cả biệt đội trong lòng đất! Toàn bộ mười đặc vụ bên dưới đều đang tập trung trước cánh cổng kho báu, không kịp quay lại ứng cứu. Khoảng cách giữa họ và đội tuần tra chỉ còn chưa đầy ba mươi mét! Các tia quét tầm nhiệt của đội tuần tra đang lia dần về phía bóng lưng của Chim Cắt và Quạ Đen, chỉ còn vài giây nữa là chuông báo động sẽ réo vang!
```
**Part 1** → `audio/vs/scene11_p1.wav` (670 ký tự) · mood `hao_hung`

```text
Nhưng trên cành cao của cây bồ kết cổ thụ ngoài cửa sổ hành lang, một bóng đen nhỏ bé mang đôi cánh xám trắng đang lặng lẽ quan sát từng cử động của kẻ địch: Đặc vụ Chim Bách Thanh! Đừng để vẻ bề ngoài nhỏ nhắn như một chú chim sẻ đánh lừa bạn! Trong giới điểu học, Chim Bách Thanh được mệnh danh là "Gã Đồ Tể Rừng Xanh", sát thủ sở hữu kỹ thuật phục kích tàn nhẫn và thông minh bậc nhất tự nhiên! Bách Thanh là loài chim duy nhất không có móng vuốt đại bàng nhưng lại có thể săn bắt và hạ gục những con mồi to gấp đôi trọng lượng cơ thể mình! Cơ cổ cực khỏe cho phép chim bách thanh thực hiện cú giật xoắn cực mạnh làm trật khớp cổ con mồi chỉ trong một phần mười giây!
```
**Part 2** → `audio/vs/scene11_p2.wav` (902 ký tự) · mood `tram_bi_an`

```text
Và vũ khí đáng sợ nhất của Bách Thanh chính là kỹ thuật cắm gai nhọn độc nhất vô nhị! Các nhà khoa học tại đại học Florida đã ghi nhận những phát hiện chấn động về tập tính này! Khi bắt được những loài côn trùng có nọc độc chết người như cào cào Lubber khổng lồ, bách thanh không bao giờ ăn ngay. Anh chàng sẽ cắp con mồi đem cắm chặt lên một chiếc gai nhọn sắc bén! Con mồi được phơi trên gai suốt ba ngày trời! Dưới ánh nắng và gió, toàn bộ chất độc tự nhiên trong cơ thể con mồi sẽ bị phân hủy hoàn toàn, biến một bữa ăn kịch độc thành món ăn thơm ngon bổ dưỡng an toàn tuyệt đối! Chưa hết, Bách Thanh sở hữu một bản đồ không gian thiên tài trong não bộ: anh chàng có thể ghi nhớ vị trí của hàng chục chốt gai nhọn khác nhau rải rác trong bán kính năm trăm mét mà không bao giờ nhầm lẫn! Anh chàng biết chính xác món mồi nào đã được cắm bao nhiêu ngày, món nào đã hết độc tố và sẵn sàng thưởng thức!
```
**Part 3** → `audio/vs/scene11_p3.wav` (779 ký tự) · mood `don_dap`

```text
Tọa độ đã khóa! Mục tiêu là năm chiếc camera cảm biến và chiếc cần gạt báo động khẩn cấp! Bách Thanh tung cánh lao vút qua khung cửa sổ hành lang như một mũi tên xé gió, không phát ra một tiếng động nhỏ nào! Vút! Vút! Vút! Bách Thanh phóng ra những chiếc gai thép sắc nhọn găm thẳng vào năm ống kính camera cảm biến của đội tuần tra người máy! Đội tuần tra bị mù hoàn toàn! Người máy chỉ huy hoảng hốt vung tay định kéo cần gạt còi báo động khẩn cấp! Không kịp nữa rồi! Bách Thanh bay vọt lên, chiếc mỏ sắc bén có mấu răng giả tomium bổ thẳng một cú mổ thần tốc vào khớp ngón tay kim loại của người máy! Anh chàng nhanh như chớp dùng mỏ quặp lấy một chiếc cọc gai thép dài hai mươi phân, đóng chặt xuyên qua chiếc cần gạt báo động, ghim cứng nó vào tường đá không thể nhúc nhích!
```
**Part 4** → `audio/vs/scene11_p4.wav` (435 ký tự) · mood `hao_hung`

```text
Đội tuần tra người máy mất phương hướng, quay mòng mòng va đập vào nhau rồi đổ rạp xuống sàn hành lang như những quân cờ domino đổ sập! Bách Thanh đậu nhẹ nhàng trên đỉnh chiếc mũ sắt của người máy chỉ huy, nghiêng đầu chỉnh lại dải lông đen ngang mắt, phát ra một tiếng kêu lách cách báo cáo Chỉ Huy Mật Vụ. "Ngoại vi đã dọn sạch! Toàn bộ hệ thống còi báo động đã bị khóa cứng bằng gai thép!" Giọng Bách Thanh đanh gọn truyền qua mic.
```
**Part 5** → `audio/vs/scene11_p5.wav` (411 ký tự) · mood `tram_bi_an`

```text
Mối đe dọa từ phía sau đã được hóa giải hoàn toàn. Giờ đây, chỉ còn lại cánh cổng sắt mạ vàng của Phòng Châu Báu Trung Tâm sừng sững trước mặt mười đặc vụ. Tất cả các ổ khóa đã mở. Toàn bộ bảy cửa ải đã bị xuyên thủng. Chiếc két sắt chứa Bản Thiết Kế Tiến Hóa Tối Thượng chỉ còn cách họ đúng một bước chân. Giờ phút lịch sử đã điểm! Chiếc két sắt tối thượng của tạo hóa chuẩn bị hé lộ bí mật lớn nhất hành tinh!
```
**Part 6** → `audio/vs/scene11_p6.wav` (748 ký tự) · mood `tram_bi_an`

```text
Kỹ thuật săn mồi và quản lý kho dự trữ của Chim Bách Thanh là minh chứng rõ nét nhất cho trí thông minh sinh thái học của loài chim ăn thịt nhỏ bé này! Nhờ chiếc mỏ có mấu răng giả tomium, bách thanh có thể truyền toàn bộ lực cắn vào một điểm duy nhất trên đốt sống cổ của mục tiêu, tạo nên một lực phá hủy tập trung cực kỳ chết chóc! Sau khi vô hiệu hóa hoàn toàn đội tuần tra, anh chàng khẽ lau mỏ vào cành cây, tiếp tục giữ vai trò sát thủ thầm lặng bảo vệ toàn bộ đội hình rút lui an toàn! Khả năng ẩn nấp ngụy trang tài tình giúp Chim Bách Thanh hoàn toàn hòa mình vào màu vỏ cây bồ kết xám xịt, biến mất khỏi tầm mắt kẻ thù! Toàn bộ hành lang ngoại vi đã rơi vào im lặng tuyệt đối, mở đường cho giờ phút khai mở kho báu lịch sử của muôn loài!
```

### scene12 — CÚ LẬT KÈO CHẤN ĐỘNG — KHO BÁU THẬT SỰ CỦA PHÁO ĐÀI
*Thẻ chương:* BẢN THIẾT KẾ TIẾN HÓA TỐI THƯỢNG

*Badge:* `PHÒNG CHÂU BÁU TRUNG TÂM` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene12_p0.wav` (642 ký tự) · mood `tram_bi_an`

```text
Cánh cổng vàng ròng nặng mười tấn của Phòng Châu Báu Trung Tâm từ từ mở ra, kèm theo một tiếng rít trầm đục vang vọng khắp các vách đá. Mười đặc vụ cùng bước vào trong sự ngỡ ngàng tột độ. Không khí bên trong căn phòng thơm ngát mùi thảo mộc cổ xưa, hoàn toàn đối lập với mùi khói súng và sắt thép lạnh lẽo bên ngoài. Chính giữa căn phòng là một chiếc bệ đá hoa cương đen tuyền, trên đó đặt chiếc két sắt tối thượng được rèn bằng hợp kim siêu bền bất khả xâm phạm. Bốn bức bích họa khổng lồ trên tường tái hiện lại lịch sử tiến hóa năm trăm triệu năm của Trái Đất, từ những sinh vật phù du cổ đại cho đến những loài động vật kỳ diệu ngày nay!
```
**Part 1** → `audio/vs/scene12_p1.wav` (754 ký tự) · mood `hao_hung`

```text
Các đặc vụ bắt đầu xì xào bàn tán về món kho báu đang nằm bên trong. Mỗi người đều có một giấc mơ riêng sau khi hoàn thành phi vụ thế kỷ! Chuột Chũi Trũi chảy nước miếng mơ về một kho chứa một triệu tấn khoai tây mật ngọt lịm ăn không bao giờ hết! Quạ Đen thì xoa xoa hai cánh mắt sáng như sao, đòi một núi thìa bạc nạm kim cương để xây cái tổ đắt giá nhất hành tinh! [laughter] Cá Voi Sát Thủ nhô đầu lên cười khùng khục đòi một biển đầy cá hồi béo ngậy và chiếc vương miện thống trị đại dương! Còn Lạc Đà Sa Mạc chỉ khẽ chớp mắt mơ về một hồ nước ngọt mát lạnh quanh năm với những rặng xương rồng không bao giờ tàn! Dê Núi mong ước có một ngọn núi tuyết riêng tư để tha hồ phi thân, trong khi đàn kiến cắt lá mơ về một cánh rừng lá phong non xanh mướt!
```
**Part 2** → `audio/vs/scene12_p2.wav` (478 ký tự) · mood `tram_bi_an`

```text
Chỉ Huy Mật Vụ bước tới trước chiếc két sắt, nhẹ nhàng đặt chiếc máy tính bảng mật mã vào ổ nhận dạng trung tâm. Tách! Tách! Tách! Chiếc két sắt từ từ bật nắp! Một luồng ánh sáng chói lòa bừng lên, khiến tất cả phải đưa tay lên che mắt. Nhưng khi làn khói tan dần... cả mười đặc vụ đều sững sờ chết lặng! Bên trong chiếc két sắt tối thượng... không hề có một thỏi vàng nào! Không có kim cương, không có súng laser tối tân, cũng chẳng có lấy một cọng khoai tây nào cả! [laughter]
```
**Part 3** → `audio/vs/scene12_p3.wav` (124 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Ủa... kho báu của chúng ta đâu rồi sếp ơi? Bị ai nẫng tay trên trước rồi hả sếp? Hay là chúng ta đột nhập nhầm pháo đài rồi?
```
**Part 4** → `audio/vs/scene12_p4.wav` (308 ký tự) · mood `nghiem_trang_gia`

```text
Chỉ Huy Mật Vụ không hề ngạc nhiên. Anh chàng cú mèo nhẹ nhàng cầm chiếc gương tròn lên, xoay mặt gương hướng về phía toàn thể mười đặc vụ. "Các bạn hãy nhìn kỹ vào trong gương đi. Kho báu thật sự của Pháo Đài Tự Nhiên... đang đứng ngay trước mặt các bạn đấy." Giọng Chỉ Huy trầm ấm và trang nghiêm vang lên.
```
**Part 5** → `audio/vs/scene12_p5.wav` (1100 ký tự) · mood `am_ap`

```text
Chỉ Huy từ từ mở cuộn da cừu cổ xưa ra, đọc to những dòng chữ được khắc ghi từ hàng trăm triệu năm trước: "Vàng bạc rồi cũng sẽ bị chôn vùi dưới cát bụi. Súng đạn rồi cũng sẽ bị rỉ sét mục nát theo thời gian. Nhưng khả năng thích nghi và vươn lên của sự sống thì bất tử." Kho báu vĩ đại nhất của tự nhiên không phải là những thứ vật chất vô tri, mà chính là Bản Thiết Kế Tiến Hóa nằm ngay trong cơ thể của mỗi loài sinh vật! Chiếc mũi nén khí siêu thanh ba trăm tám mươi chín cây số một giờ của Chim Cắt. Khả năng thở bằng đường hoa quả sống sót mười tám phút không oxy của Chuột Chũi. Thuật đóng băng sáu mươi lăm phần trăm cơ thể hồi sinh sau bảy tháng của Ếch Gỗ. Trí tuệ chế tạo công cụ giải câu đố tám bước của Quạ Đen. Sóng âm sonar hai trăm hai mươi lăm đê-xi-ben quất sóng thần của Cá Voi Sát Thủ. Hộp sọ giảm chấn một ngàn hai trăm G của Chim Gõ Kiến. Tế bào máu hình oval giãn nở hai trăm bốn mươi phần trăm của Lạc Đà Sa Mạc. Móng guốc giác hút cao su bám vách đá chín mươi độ của Dê Núi. Kỹ thuật cắm gai khử độc của Chim Bách Thanh. Và hàm răng tẩm kim loại nặng của Đại Đội Kiến Cắt Lá!
```
**Part 6** → `audio/vs/scene12_p6.wav` (620 ký tự) · mood `hao_hung`

```text
Mỗi loài trong số mười quái kiệt này tự thân đã là một kiệt tác kỹ thuật đỉnh cao mà không một phòng thí nghiệm hay cỗ máy tối tân nào của con người có thể sao chép hoàn hảo được! Và điều kỳ diệu nhất: không một cá nhân nào có thể một mình vượt qua cả bảy cửa ải của pháo đài. Chỉ khi mười loài vật cùng đoàn kết, bù đắp điểm yếu cho nhau, cánh cửa bất khả thi mới được mở toang! Đó chính là thông điệp tối thượng của Bản Thiết Kế Tiến Hóa: Đa dạng sinh học chính là chiếc khiên hộ mệnh duy nhất bảo vệ sự sống trên hành tinh xanh này! Biệt Đội Đặc Nhiệm Sinh Học đã hoàn thành sứ mệnh lịch sử vĩ đại nhất của muôn loài!
```
**Part 7** → `audio/vs/scene12_p7.wav` (558 ký tự) · mood `tram_bi_an`

```text
Nhưng khoảnh khắc lắng đọng đầy ý nghĩa vừa kết thúc... thì một tiếng nổ chát chúa vang lên từ trần phòng châu báu! Chiếc bệ đá tự động tụt xuống lòng đất, kích hoạt hệ thống tự hủy cuối cùng của pháo đài: "Cảnh báo khẩn cấp! Bản Thiết Kế đã được mở khóa! Pháo đài sẽ tự hủy hoàn toàn sau đúng ba phút nữa!" Cuộc đột nhập đã hoàn tất. Bây giờ là bài toán sinh tử cuối cùng: Chiến Dịch Tháo Chạy Nghẹt Thở để thoát khỏi đống đổ nát trước khi chiếc cổng thành đóng vĩnh viễn! Cả căn cứ đang sụp đổ sau lưng, thời gian chỉ còn tính bằng từng tích tắc ngắn ngủi!
```
**Part 8** → `audio/vs/scene12_p8.wav` (788 ký tự) · mood `am_ap`

```text
Hàng trăm triệu năm qua, Trái Đất đã trải qua biết bao kỷ băng hà buốt giá, bao đợt tuyệt chủng khắc nghiệt và núi lửa phun trào ngút trời. Nhưng sự sống chưa bao giờ chịu khuất phục. Mỗi một loài sinh vật, từ chú kiến nhỏ bé dưới chân đến chú cá voi khổng lồ ngoài khơi xa, đều là một mảnh ghép không thể thiếu của bức tranh thiên nhiên hoàn mỹ! Biệt Đội Đặc Nhiệm Sinh Học đã chứng minh rằng khi chúng ta cùng thấu hiểu và tôn trọng những giá trị tiến hóa của tự nhiên, không có thử thách nào là không thể vượt qua! Khoảnh khắc chiếc gương đồng phản chiếu khuôn mặt của cả mười quái kiệt sẽ mãi mãi là bức tranh đẹp nhất trong lịch sử sinh tồn của Trái Đất! Bản Thiết Kế Tiến Hóa Tối Thượng đã tìm được những chủ nhân xứng đáng nhất, những đại sứ xuất sắc của thế giới tự nhiên kỳ diệu!
```

### scene13 — PHÁO ĐÀI ĐẾM NGƯỢC 3 PHÚT & MÀN COMBO ĐÀO TẨU
*Thẻ chương:* CUỘC ĐUA VỚI THỜI GIAN

*Badge:* `CHIẾN DỊCH RÚT LUI` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene13_p0.wav` (644 ký tự) · mood `don_dap`

```text
Đồng hồ đếm ngược tự hủy đang nhấp nháy đỏ rực: hai phút năm mươi giây! Toàn bộ Pháo Đài Tự Nhiên rung chuyển dữ dội như vừa trải qua một trận động đất mười độ Rích-te! Các hệ thống phòng vệ tự động bị chập điện, phóng ra những tia lửa điện xanh lè đan chéo nhau như một lưới điện tử thần. Các cánh cửa sắt chống cháy bắt đầu sập xuống ầm ầm! "Không được bỏ lại bất kỳ ai! Toàn đội kích hoạt đội hình combo giải cứu khẩn cấp!" Tiếng quát vang rền của Chỉ Huy Mật Vụ truyền thẳng vào tai nghe của từng đặc vụ. Cửa sập số một rơi xuống chặn đứng lối ra của hành lang chính! Kẹt cứng! Khe hở dưới đáy chỉ còn chưa đầy nửa mét và đang hạ xuống dần!
```
**Part 1** → `audio/vs/scene13_p1.wav` (522 ký tự) · mood `hao_hung`

```text
Đến lượt cặp bài trùng công binh ra tay! Chim Gõ Kiến lao vút tới, mỏ kẹp chiếc đục sắt gõ liên hoàn hai mươi lần một giây vào rãnh trượt của cánh cửa! Ngay lập tức, Đại Đội Kiến Cắt Lá dùng hàm răng tẩm kẽm và mangan ngoạm chặt lấy dây cáp tời phụ, kéo căng hết cỡ để giữ cánh cửa không bị rơi sập thêm! Dê Núi Bắc Mỹ cúi rạp người xuống: "Chuột Chũi, Ếch Gỗ, nhảy lên lưng tôi mau!" Dê Núi co bốn chân, tung một cú phi thân trượt bụng điệu nghệ qua khe hở chỉ vài xăng-ti-mét trước khi cánh cửa sập hẳn xuống mặt sàn đá!
```
**Part 2** → `audio/vs/scene13_p2.wav` (704 ký tự) · mood `don_dap`

```text
Thời gian còn lại: một phút bốn mươi giây! Hành lang phía trước bốc cháy dữ dội do ống dẫn khí gas của lò nhiệt sa mạc bị vỡ toang! "Dạt ra hai bên hết cho đại ca làm việc!" Tiếng gầm của Cá Voi Sát Thủ vang lên qua hệ thống cống thoát nước ngầm bên dưới sàn đá! Cá Voi Sát Thủ hít một hơi thật sâu làn nước lạnh, phóng ra một cột nước áp lực cao khổng lồ qua lỗ thở như một chiếc vòi rồng cứu hỏa tối tân! Lạc Đà Sa Mạc lập tức sải những bước chân dài vượt lên dẫn đầu, xòe hai bên hông che chắn cho các đồng đội nhỏ bé tránh khỏi những tảng đá nhọn đang rơi rụng từ trần hang! Các tảng đá rơi trúng lưng lạc đà bị dội ngược ra ngoài nhờ lớp mỡ đàn hồi dày cộp, không gây tổn thương dù chỉ một vết xước!
```
**Part 3** → `audio/vs/scene13_p3.wav` (421 ký tự) · mood `tram_bi_an`

```text
Thời gian còn lại: năm mươi giây! Toàn bộ căn cứ chìm trong khói đen đặc quánh! Hệ thống định vị vệ tinh mất tín hiệu hoàn toàn! Lối ra ở hướng nào? Quạ Đen bay vút lên cao sát trần hang, dùng đôi mắt tinh tường quan sát hướng di chuyển của những luồng gió tươi mát luồn qua các khe nứt! "Rẽ phải! Cổng vòm số ba! Chạy theo luồng gió tươi! Nhanh lên!" Quạ Đen vừa bay vừa kêu quạ quạ dẫn đường chuẩn xác cho cả đoàn quân!
```
**Part 4** → `audio/vs/scene13_p4.wav` (522 ký tự) · mood `don_dap`

```text
Thời gian còn lại: hai mươi giây! Cánh cửa sắt thoát hiểm cuối cùng của pháo đài đã hiện ra trước mắt! Nhưng bi kịch thay: cửa đã bị khóa chặt bằng ổ khóa điện tử khẩn cấp! "Chiếc thẻ từ dự phòng! Thẻ từ đang ở đâu?" Chỉ Huy Mật Vụ lục lọi túi áo hoảng hốt kêu lên! Cách đó năm mươi mét ngoài cửa sổ, chiếc thẻ từ màu đỏ vẫn đang bị cắm chặt trên cành gai cao chót vót của Chim Bách Thanh! Thời gian còn lại: mười giây! Chín... tám... bảy! Tiếng còi tự hủy bắt đầu rít lên từng hồi liên tục báo hiệu đợt phát nổ cuối cùng!
```
**Part 5** → `audio/vs/scene13_p5.wav` (566 ký tự) · mood `hao_hung`

```text
"Để đó cho tôi!" Một tia chớp xám đen xé toạc màn đêm lao vút qua khung cửa sổ với vận tốc ba trăm tám mươi chín cây số một giờ: Chim Cắt Lớn! Móng vuốt vàng sắc lẹm của Chim Cắt quặp chuẩn xác vào mép chiếc thẻ từ, bẻ gãy cành gai nhọn trong chớp mắt, rồi lượn một vòng tròn ngoạn mục ném thẳng chiếc thẻ vào tay Chỉ Huy! Xoẹt! Chỉ Huy Mật Vụ quẹt mạnh chiếc thẻ qua khe nhận dạng! Tách! Cánh cửa sắt thoát hiểm bật mở toang ra bầu trời đêm bao la! Thời gian còn lại: hai giây! Một giây! Toàn bộ mười đặc vụ cùng Chỉ Huy cùng lúc tung mình nhảy bổ ra khỏi cửa hang!
```
**Part 6** → `audio/vs/scene13_p6.wav` (431 ký tự) · mood `don_dap`

```text
ẦM! ĐOÀNG! Pháo Đài Tự Nhiên phát nổ sau lưng thành một quả cầu lửa khổng lồ rực sáng cả một góc trời, toàn bộ công sự bằng đá granite sụp đổ chôn vùi vĩnh viễn trong lòng đất! Toàn đội lấm lem bùn đất, nhưng không một ai bị thương nặng! Chiếc máy tính bảng của Chỉ Huy vang lên một tiếng bíp êm ái: "Điệp vụ hoàn tất một trăm phần trăm! Toàn đội an toàn!" Biệt Đội Đặc Nhiệm Sinh Học đã sống sót qua phi vụ nghẹt thở nhất lịch sử!
```
**Part 7** → `audio/vs/scene13_p7.wav` (715 ký tự) · mood `don_dap`

```text
Từng giây phút trong cuộc tháo chạy nghẹt thở này là một bài học mẫu mực về tinh thần đoàn kết và sự phối hợp tác chiến đỉnh cao giữa các loài động vật! Không có sự đố kỵ, không có sự phân biệt to nhỏ hay mạnh yếu, mỗi cá thể đều đem hết sở trường sinh học của mình ra để cứu lấy những người đồng đội! Cú nhảy ngoạn mục ra ngoài miệng vực trong tiếng nổ rung trời lở đất sẽ mãi mãi đi vào huyền thoại của những phi vụ giải cứu vĩ đại nhất giới sinh vật học! Những bước chân tháo chạy cuối cùng trên thảm cỏ xanh mướt là minh chứng cho sự kiên cường và lòng quả cảm phi thường của mười đặc vụ sinh học! Pháo Đài Tự Nhiên đã sụp đổ, nhưng tinh thần đồng đội và những kỳ quan tiến hóa của họ sẽ sống mãi với thời gian!
```

### scene14 — ĐÓNG HỒ SƠ, CHIA THÙ LAO & HÉ LỘ HỒ SƠ MEGA 05
*Thẻ chương:* MẬT MÃ MÙA SAU: PHÒNG CẤP CỨU TẠO HÓA

*Badge:* `HỒ SƠ HOÀN TẤT` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene14_p0.wav` (706 ký tự) · mood `am_ap`

```text
Ánh bình minh đầu tiên của buổi sớm mai bắt đầu ló rạng trên đường chân trời, dát một màu vàng mật ong ấm áp lên khắp thung lũng xanh mướt. Căn phòng tác chiến ngầm dã chiến của Tổng Cục Mật Vụ lại rộn rã tiếng cười nói sau một đêm căng thẳng đến từng sợi tóc. Chỉ Huy Mật Vụ Cú Mèo cầm con dấu gỗ khắc nổi, nhúng vào khay mực đỏ tươi, đóng một phát thật mạnh xuống trang bìa của tập hồ sơ: CỘC! Dấu mực đỏ hiện rõ dòng chữ: HOÀN TẤT XUẤT SẮC — LƯU TRỮ TUYỆT MẬT! "Các đặc vụ của tôi! Đêm nay, các bạn không chỉ hoàn thành một phi vụ bất khả thi, mà còn chứng minh cho toàn thế giới thấy sức mạnh vô song của sự sống và tình đồng đội!" Biệt Đội Đặc Nhiệm Sinh Học đã hoàn thành xuất sắc nhiệm vụ được giao!
```
**Part 1** → `audio/vs/scene14_p1.wav` (544 ký tự) · mood `hao_hung`

```text
Và bây giờ là phần được mong chờ nhất trong mọi bộ phim điệp viên: lễ trao thù lao và giải tán lực lượng! [laughter] Đặc vụ Chuột Chũi Trũi được trao tặng ba bao tải khoai tây mật sấy bơ thượng hạng, cộng thêm một giấy chứng nhận: "Thợ đào hầm hảo hạng không bao giờ biết đau"! Đặc vụ Quạ Đen nhận một xô hạt dẻ rang bơ khổng lồ cùng một bộ kìm kẹp đa năng mạ vàng hai mươi bốn ca-ra để tha hồ chế tạo công cụ mới! Đặc vụ Chim Cắt Lớn được đền bù một bộ áo khoác da phi công hàng hiệu mới tinh, kèm một chiếc cà vạt lụa chống kiến cắn siêu bền!
```
**Part 2** → `audio/vs/scene14_p2.wav` (963 ký tự) · mood `hao_hung`

```text
Đặc vụ Ếch Gỗ Bắc Cực được quàng một chiếc khăn len đỏ ca-sơ-mia mềm mại chống rét âm năm mươi độ C, kèm một bình si-rô ngọt ngào bổ dưỡng! Đặc vụ Cá Voi Sát Thủ nhận một tấm thẻ hội viên VIP bơi lội trọn đời tại toàn bộ các rạn san hô đẹp nhất thế giới, kèm một tấn cá hồi tươi rói! Đặc vụ Chim Gõ Kiến nhận một chiếc mũ bảo hộ bằng sợi các-bon siêu nhẹ có giảm chấn ba lớp, giúp anh chàng gõ đá mà êm như gõ gối bông! Lạc Đà Sa Mạc nhận một xe tải xương rồng non mọng nước đã được nhổ sạch gai, tha hồ nhai rôm rốp mà không sợ làm phiền bộ đàm của ai nữa! [laughter] Dê Núi Bắc Mỹ nhận bốn chiếc đệm móng guốc cao su thể thao hàng hiệu chống trượt tối tân để tha hồ leo vách đá chín mươi độ! Chim Bách Thanh được trang bị một giàn gai thép không gỉ chuyên dụng gắn camera hành trình để bảo quản chiến lợi phẩm an toàn! Và Đại Đội Kiến Cắt Lá được trao tặng một nông trại nấm hữu cơ ngầm rộng năm trăm mét vuông để phát triển nông nghiệp bền vững cho cả tổ kiến!
```
**Part 3** → `audio/vs/scene14_p3.wav` (300 ký tự) · mood `am_ap`

```text
Mười quái kiệt, mười số phận kỳ lạ của tự nhiên đã hoàn thành sứ mệnh lịch sử. Họ lại quay trở về với bầu trời, rừng sâu, biển cả và lòng đất của riêng mình. Nhưng những bài học tiến hóa kỳ diệu và tinh thần đồng đội của họ sẽ mãi mãi được lưu giữ trong kho tàng tri thức của kênh Vẽ Chuyện Hoang Dã.
```
**Part 4** → `audio/vs/scene14_p4.wav` (407 ký tự) · mood `tram_bi_an`

```text
Căn phòng tác chiến trở lại yên tĩnh. Chỉ còn lại Chỉ Huy Mật Vụ Cú Mèo ngồi một mình bên bàn làm việc dưới ánh đèn bàn ấm áp. Anh chàng mở chiếc ngăn kéo bàn có khóa mật mã hai lớp, cẩn thận cất tập hồ sơ của Biệt Đội Đặc Nhiệm vào góc an toàn. Và rồi, ngón tay của Chỉ Huy dừng lại ở một tập tài liệu bìa màu xanh phẫu thuật y tế còn niêm phong bằng sáp đỏ, có gắn dòng chữ cảnh báo: HỒ SƠ TỐI MẬT SỐ NĂM!
```
**Part 5** → `audio/vs/scene14_p5.wav` (838 ký tự) · mood `nghiem_trang_gia`

```text
Một nụ cười bí hiểm nở trên môi vị Chỉ Huy: "Trận chiến này vừa kết thúc... nhưng ca trực đêm kinh hoàng nhất của lịch sử tiến hóa thì chỉ mới bắt đầu." Đêm nay, tại Bệnh Viện Đa Khoa Tiến Hóa, mười bệnh nhân mang những triệu chứng sinh học trái ngược hoàn toàn với quy luật thông thường đang đồng loạt nhập viện cấp cứu! Một chú Nhện Lặn Chuông tự dệt bình dưỡng khí bằng tơ để thở dưới nước. Một chú Cá Thoi Loi trèo cây hít thở bằng da. Một nàng Ong Bắp Cày Ngọc cầm dao phẫu thuật điều khiển não gián. Một chú Cá Mặt Trăng ba tấn không não trôi dạt giữa đại dương. Và một chú Vẹt Ca-ca-pô béo ú quên mất cách bay, đêm đêm nhảy từ ngọn cây xuống đất tìm bạn đời! [laughter] Cùng với Lợn Rừng Ba-bi-ru-sa mang răng nanh tự đâm sọ, Hươu Cao Cổ huyết áp ba trăm, Cò Mỏ Giày đứng như tượng đá và Nhím Lông Nhọn mang ba mươi ngàn chiếc gai!
```
**Part 6** → `audio/vs/scene14_p6.wav` (558 ký tự) · mood `am_ap`

```text
Hẹn gặp lại quý vị khán giả trong Mega số năm: Phòng Cấp Cứu Tạo Hóa — Ca Trực Đêm Kinh Hoàng của mười bệnh nhân tiến hóa kỳ lạ nhất hành tinh! Còn bây giờ, nếu bạn được quyền tuyển chọn một đặc vụ trong Biệt Đội Đặc Nhiệm Sinh Học tối nay làm bạn đồng hành, bạn sẽ chọn quái kiệt nào? Hãy để lại mật mã của bạn ở phần bình luận bên dưới nhé! Đừng quên bấm thích video, đăng ký kênh Vẽ Chuyện Hoang Dã và nhấn chuông thông báo để không bỏ lỡ những phi vụ sinh tồn chấn động tiếp theo. Chúc các bạn một giấc ngủ thật ngon và những giấc mơ phiêu lưu tuyệt đẹp!
```
**Part 7** → `audio/vs/scene14_p7.wav` (783 ký tự) · mood `am_ap`

```text
Bệnh Viện Đa Khoa Tiến Hóa trong Mega số năm hứa hẹn sẽ mang đến những câu chuyện y khoa hài hước và kỳ thú chưa từng có về mười sinh vật mang thiết kế ngược đời nhất hành tinh! Quý vị sẽ được giải mã vì sao chú vẹt Kakapo béo ú lại quên cách bay, vì sao chú lợn rừng Babirusa lại có răng nanh tự đâm vào sọ, và vì sao hươu cao cổ cúi đầu uống nước mà không bị vỡ mạch máu não! Hãy tiếp tục đồng hành cùng kênh Vẽ Chuyện Hoang Dã để khám phá những điều kỳ diệu bất tận của thế giới tự nhiên xung quanh chúng ta! Mỗi một tập phim của kênh Vẽ Chuyện Hoang Dã là một hành trình kỳ thú đưa quý vị khán giả đến với những bí mật chưa từng được kể của muôn loài! Hãy chuẩn bị tinh thần cho những ca trực đêm nghẹt thở và những chẩn đoán y khoa cười ra nước mắt trong mùa phim tiếp theo nhé!
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Mười đặc vụ quái kiệt. Bảy cửa ải an ninh. Một phi vụ thế kỷ đột nhập Pháo Đài Tự Nhiên! Cửa Ải Một: Chim Cắt Lớn bổ nhào xé gió ba trăm tám mươi chín cây số một giờ vô hiệu hóa lưới laser! Cửa Ải Hai: Chuột Chũi Trũi thở bằng đường hoa quả sống sót mười tám phút ở mức không phần trăm oxy! Cửa Ải Ba: Ếch Gỗ Bắc Cực chủ động đóng băng sáu mươi lăm phần trăm cơ thể, tim ngừng đập qua mặt cảm biến tầm nhiệt! Cửa Ải Bốn: Quạ Đen dùng trí tuệ giải mã chuỗi bẫy cơ học tám bước và lóa mắt camera an ninh! Cửa Ải Năm: Cá Voi Sát Thủ bắn xung sonar hai trăm hai mươi lăm đê-xi-ben quất sóng thần phá đập nước ngầm! Cửa Ải Sáu: Chim Gõ Kiến triệt tiêu một ngàn hai trăm G cùng Đại Đội Kiến Cắt Lá dùng răng thép đục sập boong-ke! Cửa Ải Bảy: Dê Núi phi thân leo vách đứng chín mươi độ và Lạc Đà vượt sa mạc năm mươi độ C hạ cầu treo! Và kho báu tối thượng là gì? Không phải vàng bạc, mà là kiệt tác tiến hóa nằm ngay trong chính bản thân mỗi loài! [question-ah] Bạn ấn tượng với siêu năng lực của đặc vụ nào nhất? Xem trọn bộ phi vụ thế kỷ trong video dài nhé, vì ở đây chỉ có mười đặc vụ quái kiệt, bảy cửa ải sinh tử, và một phi vụ thế kỷ!
```

**Whisper prompt:** `Vẽ Chuyện Hoang Dã, Pháo Đài Tự Nhiên`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| ba trăm tám mươi chín cây số một giờ | 389 km/h |
| ba trăm tám mươi chín ki-lô-mét một giờ | 389 km/h |
| ba trăm tám mươi chín | 389 |
| một ngàn hai trăm G | 1200G |
| một ngàn hai trăm | 1200 |
| hai mươi lần một giây | 20 lần/giây |
| hai mươi lần | 20 lần |
| hai trăm hai mươi lăm đê-xi-ben | 225 dB |
| hai trăm hai mươi lăm | 225 |
| âm hai mươi độ C | -20°C |
| âm hai mươi độ | -20° |
| năm mươi độ C | 50°C |
| năm mươi độ | 50° |
| ba mươi tư độ C | 34°C |
| bốn mươi mốt độ C | 41°C |
| không phần trăm oxy | 0% oxy |
| không phần trăm | 0% |
| sáu mươi lăm phần trăm | 65% |
| bảy mươi phần trăm | 70% |
| hai trăm bốn mươi phần trăm | 240% |
| sáu mươi phần trăm | 60% |
| chín mươi độ | 90° |
| tám mươi độ | 80° |
| ba trăm hai mươi độ | 320° |
| một trăm hai mươi lần một phút | 120 lần/phút |
| mười tám phút | 18 phút |
| bảy tháng | 7 tháng |
| tám bước | 8 bước |
| năm năm | 5 năm |
| hai mét | 2 mét |
| tám mét | 8 mét |
| năm trăm mét | 500 mét |
| một trăm lít nước | 100 lít nước |
| ba ngày | 3 ngày |
| năm mươi triệu năm | 50 triệu năm |
| bảy cửa ải | 7 cửa ải |
| mười đặc vụ | 10 đặc vụ |
| Cửa Ải Một | Cửa Ải 1 |
| Cửa Ải Hai | Cửa Ải 2 |
| Cửa Ải Ba | Cửa Ải 3 |
| Cửa Ải Bốn | Cửa Ải 4 |
| Cửa Ải Năm | Cửa Ải 5 |
| Cửa Ải Sáu | Cửa Ải 6 |
| Cửa Ải Bảy | Cửa Ải 7 |
| Đặc vụ số một | Đặc vụ 01 |
| Đặc vụ số hai | Đặc vụ 02 |
| Đặc vụ số ba | Đặc vụ 03 |
| Đặc vụ số bốn | Đặc vụ 04 |
| Đặc vụ số năm | Đặc vụ 05 |
| Đặc vụ số sáu | Đặc vụ 06 |
| Đặc vụ số bảy | Đặc vụ 07 |
| Đặc vụ số tám | Đặc vụ 08 |
| Đặc vụ số chín | Đặc vụ 09 |
| Đặc vụ số mười | Đặc vụ 10 |
| năm trăm triệu năm | 500 triệu năm |
| trăm triệu năm | trăm triệu năm |
| Không một | Không một |
| không một | không một |
| Một trăm | 100 |
| một trăm | 100 |
| Hai trăm | 200 |
| hai trăm | 200 |
| Ba trăm | 300 |
| ba trăm | 300 |
| Năm Mươi | 50 |
| năm mươi | 50 |
| Chín Mươi | 90 |
| chín mươi | 90 |
| ba ngàn mét | 3.000m |
| ba ngàn | 3.000 |
| ba mươi ngàn | 30.000 |
| ba mươi mét | 30m |
| ba mươi giây | 30 giây |
| ba mươi | 30 |
| bốn mươi lăm giây | 45 giây |
| bốn mươi lăm | 45 |
| bốn mươi mét | 40m |
| bốn mươi xăng-ti-mét | 40cm |
| bốn mươi | 40 |
| năm mươi sáu cây số một giờ | 56 km/h |
| năm mươi sáu | 56 |
| hai mươi bốn ca-ra | 24K |
| hai mươi bốn | 24 |
| hai mươi lăm phần trăm | 25% |
| hai mươi lăm | 25 |
| hai mươi phân | 20cm |
| hai mươi mét | 20m |
| hai mươi | 20 |
| mười lăm phút | 15 phút |
| mười lăm | 15 |
| sáu mươi phút | 60 phút |
| sáu mươi giây | 60 giây |
| sáu mươi chiếc | 60 chiếc |
| sáu mươi nhịp | 60 nhịp |
| sáu mươi | 60 |
| Năm hai ngàn mười bảy | Năm 2017 |
| năm hai ngàn mười bảy | năm 2017 |
| ba trăm sáu mươi độ | 360° |
| ba trăm sáu mươi | 360 |
| một triệu tấn | 1 triệu tấn |
| một triệu | 1 triệu |
| năm trăm mét vuông | 500m² |
| năm trăm | 500 |
| ba mét | 3 mét |
| năm mét | 5 mét |
| mười mét | 10 mét |
| năm phân | 5cm |
| mười phân | 10cm |
| năm xăng-ti-mét | 5cm |
| ba tấc | 3 tấc |
| nửa mét | 0,5m |
| ba phút | 3 phút |
| hai phút | 2 phút |
| hai giây | 2 giây |
| ba giây | 3 giây |
| một phần mười giây | 0,1 giây |
| một phần nghìn giây | 0,001 giây |
| một phần mười | 0,1 |
| sáu tấn | 6 tấn |
| mười tấn | 10 tấn |
| hàng tạ | hàng tạ |
| năm ki-lô-gam | 5kg |
| hai mươi nhịp | 20 nhịp |
| năm mươi nhịp | 50 nhịp |
| Gờ-lút năm | GLUT5 |
| khí các-bon-nic | CO₂ |
| Khí các-bon-nic | CO₂ |
| ba năm ròng | 3 năm ròng |
| ba năm | 3 năm |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · TRIỆU TẬP BIỆT ĐỘI ĐẶC NHIỆM SINH HỌC · 266.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.8 (7.8s) | L01 | Một căn hầm ngầm bê tông tối om dưới lòng đất sâu 100 mét. Chỉ có ánh sáng xanh lục từ chiếc máy chiếu hologram quét chầm chậm qua các góc phòng. |  | Căn phòng tác chiến ngầm tối tân phong cách Cold War thập niên 1960 với tường bê tông xám, màn hình radar xanh lục quét vòng tròn, anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm đứng quay lưng lại nhìn tấm bản đồ phát sáng. |
| b02 | 00:07.8–00:14.9 (7.2s) | L02 | Chào mừng toàn thể các điệp viên đến với Tổng Cục Tiến Hóa Tối Mật. Nếu các bạn nghe được tín hiệu này, có nghĩa là phi vụ thế kỷ đã chính thức bắt đầu. |  | Cận cảnh anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm từ từ xoay người lại, bàn tay vuốt chỉnh ve áo măng-tô đen, chiếc kính râm phản chiếu các dòng dữ liệu mật mã màu xanh lục lướt qua mặt kính. |
| b03 | 00:14.9–00:21.1 (6.2s) | L03 | Trước mặt chúng ta là mục tiêu tối thượng chưa từng có sinh vật nào xuyên thủng được suốt 500 triệu năm qua: Pháo Đài Tự Nhiên. |  | bản đồ hologram 3D của Pháo Đài Tự Nhiên nổi lơ lửng trong không khí, hiển thị 7 cửa ải an ninh phát sáng đỏ và thanh tiến độ phá khóa màu xanh ngọc (không có chữ, không có số) bật sáng rực rỡ giữa phòng, mô hình 3D của một pháo đài khổng lồ bằng đá granite đen và băng tuyết bao quanh thung lũng hiểm trở, có bảy vòng rào an ninh nhấp nháy đỏ rực. |
| b04 | 00:21.1–00:26.4 (5.3s) | L04 | Nơi đây giấu kín Bản Thiết Kế Tiến Hóa Tối Thượng, cội nguồn sức mạnh của toàn bộ giới sinh vật trên Trái Đất. |  | Cận cảnh mô hình hologram thu nhỏ của cuộn tài liệu phát sáng vàng kim lơ lửng giữa tâm điểm pháo đài, bao quanh là các lớp lưới bảo vệ; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b05 | 00:26.4–00:32.0 (5.6s) | L05 | Nhưng để chạm tới chiếc két sắt trung tâm, Biệt Đội Đặc Nhiệm Sinh Học phải vượt qua 7 cửa ải an ninh sinh tử kiên |  | Bảy biểu tượng cửa ải lần lượt chớp sáng trên bản đồ: vòi rồng gió lốc, đường hầm yếm khí, hầm băng vĩnh cửu, mê cung bẫy rập, hào nước áp lực cao, boong-ke bê tông và vách đá dựng đứng; anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm chỉ đầu ngón tay vào từng vị trí. |
| b06 | 00:32.0–00:41.2 (9.2s) | L06 | cố nhất. Và để giải mã bảy cánh cửa bất khả thi này, tôi đã đích thân tuyển chọn 10 đặc vụ bất hảo và quái kiệt nhất hành tinh. Không một ai trong số họ là kẻ tầm thường. |  | Mười tập hồ sơ tài liệu mật bìa giấy kraft ngả vàng xếp xòe hình cánh quạt trên mặt bàn kim loại, trên mỗi bìa có dán một bức ảnh chân dung đen trắng và đóng dấu mực đỏ TỐI MẬT; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b07 | 00:41.2–00:47.1 (5.9s) | L07 | Đặc vụ 01! Mật danh Tia Chớp Bầu Trời, kẻ sở hữu vũ khí xuyên phá hàng rào laser trên không: Chim Cắt Lớn! |  | chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng bước vào phòng họp, mặc áo giáp phi công siêu thanh, đeo kính bảo hộ trên trán, một tay kéo khóa áo khoác da, ánh mắt sắc lẹm như lưỡi dao cạo; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b08 | 00:47.1–00:54.4 (7.3s) | L08 | Hồ sơ tác chiến ghi rõ: anh chàng này từng đạt tốc độ bổ nhào xé gió 389 km/h, nhanh hơn cả một chiếc siêu xe đua Công |  | Bức ảnh tư liệu mật chụp chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng đang lao vun vút trên nền trời xanh, bên cạnh có đồ thị tốc độ nhảy vọt lên đỉnh cao nhất; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b09 | 00:54.4–01:02.1 (7.7s) | L09 | Thức Một! Đặc vụ 02! Mật danh Bóng Ma Hầm Ngầm, chuyên gia thâm nhập các địa đạo không có không khí và đầy sương axit: Chuột Chũi Trũi! |  | chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên chui tọt từ một nắp cống ngầm dưới sàn nhà lên, hai răng cửa to chìa ra ngoài, đẩy chiếc kính nhìn đêm hồng ngoại to bản lên mũi, ngơ ngác nhìn quanh; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b10 | 01:02.1–01:09.2 (7.1s) | L10 | Sinh vật không lông này có thể sống phây phây 18 phút không cần oxy, và hoàn toàn miễn nhiễm với mọi cảm giác đau đớn do axit gây ra! |  | Bản chụp X-quang sinh học của chuột chũi trũi với các biểu tượng lá chắn chống axit và biểu tượng tim đập bền bỉ trong môi trường yếm khí; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b11 | 01:09.2–01:16.8 (7.6s) | L11 | Đặc vụ 03! Mật danh Điệp Viên Băng Giá, sinh vật duy nhất có khả năng tự biến mình thành tảng băng để đánh lừa cảm biến tầm nhiệt: Ếch Gỗ Bắc Cực! |  | chú Ếch Gỗ Bắc Cực hoạt hình da nâu vàng có vệt đen qua mắt như mặt nạ Zorro, đeo khăn quàng cổ đỏ thắm chống rét, người phủ lớp sương tuyết lấp lánh bước ra từ trong làn sương mù lạnh buốt, quấn chiếc khăn len đỏ chót quanh cổ, trên da đọng những hạt sương băng lấp lánh như kim cương; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b12 | 01:16.8–01:25.1 (8.3s) | L12 | Anh chàng có thể để 65% cơ thể đóng băng cứng ngắc suốt 7 tháng mùa đông, tim ngừng đập hoàn toàn mà vẫn hồi sinh nguyên vẹn! |  | Đồ họa y tế mô phỏng chú ếch gỗ nằm ngủ đông dưới lớp tuyết dày, các phân tử đường glucose bảo vệ tế bào phát sáng màu hổ phách; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b13 | 01:25.1–01:30.6 (5.5s) | L13 | Đặc vụ 04! Mật danh Bộ Não Cơ Học, bậc thầy giải mã các chuỗi khóa bẫy đa bước phức tạp nhất: Quạ Đen! |  | chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép bay lượn sà xuống đậu trên lưng ghế kim loại, mỏ quắp chiếc kìm cắt dây thép siêu nhỏ, ánh mắt láu cá liếc ngang liếc dọc tìm ống kính quan sát hoạt hình vui nhộn; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b14 | 01:30.6–01:37.8 (7.1s) | L14 | Tài liệu của viện nghiên cứu khẳng định: bộ não của quạ đen có thể tự giải các câu đố logic cơ học 8 bước liên hoàn trong vòng 30 giây mà không cần dạy trước! |  | Sơ đồ tư duy phức tạp của loài quạ với các khớp nối logic công cụ và hình ảnh chiếc que sắt được uốn cong thành lưỡi câu; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b15 | 01:37.8–01:43.7 (6.0s) | L15 | Đặc vụ 05! Mật danh Thủy Thần Đại Dương, chỉ huy phân đội tác chiến đường nước với sóng âm phá hủy công sự: Cá Voi Sát Thủ! |  | Một bể kính dã chiến bọc thép trượt vào góc phòng, chú Cá Voi Sát Thủ hoạt hình thân đen bóng bụng trắng tinh, vây lưng cao vút cắm ăng-ten định vị sonar nhỏ xíu, miệng cười nhếch mép kiểu trùm mafia biển cả nhô đầu lên khỏi mặt nước nở nụ cười nhếch mép ngạo nghễ, chiếc ăng-ten định vị sonar trên vây lưng nhấp nháy đèn xanh; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b16 | 01:43.7–01:51.2 (7.5s) | L16 | Cỗ máy săn mồi 6 tấn này sở hữu chùm sóng sonar công suất 225 dB, đủ sức quét xuyên lòng đá và tạo nên những cơn sóng thần dập tắt mọi chốt chặn! |  | Màn hình radar thủy âm hiển thị các luồng sóng âm thanh cực mạnh hình bán nguyệt lan tỏa từ trán cá voi sát thủ; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b17 | 01:51.2–01:57.1 (5.9s) | L17 | Đặc vụ 06! Mật danh Búa Khoan Thần Tốc, kẻ có thể đập nát cửa boong-ke dày cộp bằng chính hộp sọ của mình: Chim Gõ Kiến! |  | chú Chim Gõ Kiến hoạt hình mào lông đỏ rực dựng đứng, mỏ dài sắc nhọn như mũi khoan titan, đội mũ bảo hộ lao động màu vàng có gắn đèn pin thợ mỏ đứng nghiêm chào kiểu quân đội, chiếc mũ bảo hộ màu vàng có gắn đèn pin thợ mỏ hơi lệch sang một bên, chiếc mỏ nhọn hoắt gõ lách cách xuống bàn tạo thành tia lửa nhỏ; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b18 | 01:57.1–02:04.7 (7.6s) | L18 | Cơ chế đai an toàn xương móng quấn quanh đầu cho phép anh chàng chịu đựng lực gia tốc va đập lên tới 1200G mà không hề choáng váng! |  | Bản vẽ kỹ thuật chiếc xương móng hyoid của chim gõ kiến quấn trọn hộp sọ như chiếc đai an toàn xe đua; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b19 | 02:04.7–02:12.6 (7.9s) | L19 | Đặc vụ 07! Mật danh Cỗ Xe Tăng Sa Mạc, pháo đài di động vượt qua vùng bẫy nhiệt độ 50°C mà không cần tiếp tế một giọt nước: Lạc Đà Sa Mạc! |  | chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao thong thả bước vào, hai bên hông thồ hai bình nước dã chiến áp lực cao, miệng vừa nhai tóp tép một cành xương rồng gai góc vừa chớp chớp hàng mi cong vút; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b20 | 02:12.6–02:20.4 (7.7s) | L20 | Hồng cầu hình oval độc nhất vô nhị giãn nở 240% thể tích giúp anh chàng trữ 100 lít nước và hành quân qua chảo lửa sa mạc dễ dàng! |  | Kính hiển vi mô phỏng tế bào hồng cầu hình oval màu đỏ tươi bơi lội trơn tru trong mạch nước màu lạc đà; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b21 | 02:20.4–02:28.2 (7.8s) | L21 | Đặc vụ 08! Mật danh Thánh Leo Vách Đứng, kẻ thách thức mọi định luật vật lý trên những bức tường dựng đứng 90°: Dê Núi Bắc Mỹ! |  | chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt đứng kiêu hãnh trên đỉnh chiếc tủ sắt cao chót vót, bốn móng guốc bọc đệm cao su đặc chủng bám dính như giác hút chân không; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b22 | 02:28.2–02:33.7 (5.5s) | L22 | Bốn chiếc móng guốc cao su đàn hồi kép giúp anh chàng phi thân ngược vách đá thẳng đứng 30m trong nháy mắt! |  | Hình vẽ phóng to mặt dưới của chiếc móng dê núi với lớp đệm dẻo bám dính vào vi gờ đá; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b23 | 02:33.7–02:40.0 (6.3s) | L23 | Đặc vụ 09! Mật danh Sát Thủ Gai Nhọn, tay súng bắn tỉa và phục kích cắm chốt tầm xa: Chim Bách Thanh! |  | chú Chim Bách Thanh hoạt hình lông xám trắng có dải lông đen vắt ngang mắt như dải băng cướp biển, mỏ có móc câu sắc nhọn, chân cầm một nhánh gai nhọn công nghệ đậu trên bóng đèn trần phòng họp, mỏ găm một chiếc móc sắt nhọn hoắt, dải lông đen ngang mắt trông như một sát thủ chuyên nghiệp đang quan sát con mồi; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b24 | 02:40.0–02:46.4 (6.5s) | L24 | Mấu răng tomium sắc bén và kỹ thuật găm gai nhọn cho phép anh chàng hạ gục đối thủ to gấp đôi và cất giữ chiến lợi phẩm an toàn suốt |  | Bức ảnh tư liệu mật về chiếc mỏ khoằm có mấu răng giả của chim bách thanh; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b25 | 02:46.4–02:56.7 (10.3s) | L25 | 3 ngày! Và lực lượng công binh bí mật cuối cùng! Đặc vụ 10: Đại Đội Công Binh Kiến Cắt Lá, hàng triệu chiến sĩ tí hon sở hữu hàm răng thép tẩm kim loại nặng có thể khoét rỗng chân móng pháo đài! |  | tiểu đội ba chú Kiến Cắt Lá hoạt hình màu nâu đỏ, đầu to mang hàm răng kim loại sáng loáng, đội mũ cối công binh màu xanh lá, đang vác những mảnh lá xanh như chiếc khiên chắn xếp thành đội hình thế giới tự nhiên ngay ngắn trên mặt bàn, mỗi chú vác một chiếc cờ lê mini và một phiến đá nhỏ như những người lính công binh tinh nhuệ; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b26 | 02:56.7–03:04.4 (7.7s) | L26 | Lớp kim loại kẽm và mangan nguyên chất tẩm vào đầu răng biến bầy kiến này thành những chiếc máy cắt kim cương di động dưới lòng đất! |  | Hình ảnh hiển vi quét điện tử đầu răng kiến phát sáng ánh thép kim loại; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b27 | 03:04.4–03:11.0 (6.6s) | L27 | Đủ 10 đặc vụ. Bảy cửa ải. Và đúng 60 phút trước khi hệ thống phòng thủ của pháo đài khóa vĩnh viễn lối vào. |  | Toàn bộ mười đặc vụ đứng quây quần quanh bàn tác chiến, nhìn chằm chằm vào bản đồ hologram phát sáng; anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm chống hai tay xuống bàn, ánh mắt sắc lạnh. |
| b28 | 03:11.0–03:18.1 (7.1s) | L28 | Thông báo khẩn từ trung tâm giám sát vệ tinh: pháo đài vừa kích hoạt toàn bộ lưới phòng vệ cấp độ đỏ! Toàn đội vào vị trí tác chiến! |  | Màn hình điều khiển trung tâm chuyển sang màu đỏ rực, các dòng chữ cảnh báo mã hóa chạy liên hồi trên màn hình (không chữ, không số); KHÔNG có anh Chỉ Huy trong cảnh này. |
| b29 | 03:18.1–03:23.8 (5.8s) | L29 | Các đặc vụ nghe rõ: phi vụ này tuyệt đối không có chỗ cho sự sai sót. Không có thử lại. Không có cứu viện. |  | anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm giơ chiếc máy tính bảng mật mã lên ngang ngực, ngón tay bấm nút xác nhận màu đỏ; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b30 | 03:23.8–03:30.8 (7.0s) | L30 | Mọi chi tiết trong kế hoạch này đều dựa trên những báo cáo sinh học tối tân nhất vừa được giải mã từ các phòng thí nghiệm hàng đầu thế giới. |  | Cận cảnh một tập tài liệu nghiên cứu khoa học có hình ảnh phóng to của vòi nén khí chim cắt, tế bào nước màu lạc đà và hàm răng kiến bọc kim loại nặng nằm dưới đèn soi UV; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b31 | 03:30.8–03:37.2 (6.4s) | L31 | Chúng ta không dùng súng đạn. Vũ khí tối thượng của biệt đội chính là những tuyệt kỹ tiến hóa hàng trăm triệu năm của tạo hóa! |  | Mười đặc vụ cùng giơ nắm tay hoặc giơ móng vuốt chạm vào nhau ở giữa bàn họp, ánh sáng xanh từ hologram chiếu rực rỡ lên khuôn mặt đầy quyết tâm; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b32 | 03:37.2–03:46.0 (8.8s) | L32 | Cửa Ải 1 đã hiện ra trên màn hình radar: Không phận tử thần với áp suất gió kinh hoàng và lưới quét quang học. Mật danh Tia Chớp, đến lượt cậu |  | Cánh cửa hầm ngầm từ từ mở toang ra bầu trời đêm đầy mây đen vần vũ, phía xa là ngọn tháp canh sừng sững của pháo đài; chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng sải rộng đôi cánh lao vút lên không trung xé toạc màn đêm. |
| b33 | 03:46.0–03:51.7 (5.7s) | L33 | cất cánh! Biệt Đội Đặc Nhiệm Sinh Học chính thức xuất kích! Không một kẻ thù nào có thể cản bước mười quái kiệt của tự nhiên! |  | Hình ảnh bóng lưng mười đặc vụ lao ra khỏi căn cứ ngầm tiến về phía pháo đài sừng sững trong đêm bão tố. |
| b34 | 03:51.7–03:56.6 (4.9s) | L34 | Mục tiêu là chiếc chìa khóa tối thượng. Thời gian đang đếm ngược từng giây một! |  | bản đồ hologram 3D của Pháo Đài Tự Nhiên nổi lơ lửng trong không khí, hiển thị 7 cửa ải an ninh phát sáng đỏ và thanh tiến độ phá khóa màu xanh ngọc (không có chữ, không có số) chớp sáng con số đếm ngược màu xanh lục, toàn bộ hệ thống máy móc ngầm bắt đầu khởi động rền vang. |
| b35 | 03:56.6–04:03.3 (6.7s) | L35 | Pháo Đài Tự Nhiên được xây dựng dựa trên những định luật khắc nghiệt nhất của hành tinh, nơi những kẻ yếu đuối sẽ bị đào thải không thương tiếc. |  | Mô hình hologram hiển thị các lớp đá sa thạch và granite cổ xưa bao bọc quanh pháo đài ngầm; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b36 | 04:03.3–04:11.0 (7.7s) | L36 | Mỗi một cửa ải đại diện cho một thảm họa sinh học tự nhiên: từ áp suất chân không đến cực hạn giá rét, từ sa mạc lửa cháy đến hào nước áp lực cao. |  | Bảy biểu tượng cửa ải nhấp nháy phát sáng thành một vòng tròn bảo vệ xung quanh pháo đài; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b37 | 04:11.0–04:15.8 (4.8s) | L37 | Chỉ có sức mạnh thích nghi tối thượng của muôn loài mới có thể tìm ra kẽ hở giữa những công sự kiên cố này! |  | anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm chỉ ngón tay vào tâm điểm bản đồ, ánh mắt kiên định thúc giục mười đặc vụ chuẩn bị sẵn sàng. |
| b38 | 04:15.8–04:21.8 (6.0s) | L38 | Các kỹ sư của Tổng Cục đã phân tích dữ liệu địa tầng suốt 3 năm ròng để vẽ nên sơ đồ tiến công chuẩn xác nhất cho biệt đội! |  | Bản thiết kế địa chất cổ đại với các tầng địa chất phát sáng nhiều màu sắc khác nhau; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b39 | 04:21.8–04:26.7 (4.9s) | L39 | Mọi thiết bị hỗ trợ và vũ khí ngụy trang đều đã được kiểm tra nghiêm ngặt, sẵn sàng cho giờ xuất kích! |  | Các vali dụng cụ điệp viên màu đen mở nắp, bên trong xếp ngay ngắn những chiếc kính nhìn đêm và móc câu chuyên dụng; KHÔNG có anh Chỉ Huy trong cảnh này. |

### scene02 · KHÔNG PHẬN SIÊU THANH & CHIM CẮT LỚN · 261.6s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:06.1 (6.1s) | L40 | Bầu trời đêm phía trên Pháo Đài Tự Nhiên không hề yên bình như vẻ bề ngoài. Đây là vành đai phòng không khắc nghiệt nhất hành tinh. |  | Cảnh bầu trời đêm bão tố cuồn cuộn mây xám, những cột tia laser màu đỏ rực đan chéo nhau như một chiếc lồng ánh sáng khổng lồ bao trùm lấy đỉnh tháp pháo đài; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b02 | 00:06.1–00:14.5 (8.4s) | L41 | Hàng ngàn cảm biến gió áp suất cao đang quét liên tục ở tầng đối lưu. Bất kỳ vật thể bay nào lao vào đây với tốc độ cao đều sẽ bị luồng khí nén cực mạnh xé nát phổi ngay lập tức. |  | Hình vẽ cắt lớp kỹ thuật của một hệ thống phòng không thế giới tự nhiên cổ điển, các luồng sóng xung kích không khí màu vàng cam xoáy tròn dữ dội quanh miệng phễu thu cảm biến; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b03 | 00:14.5–00:21.0 (6.6s) | L42 | Đặc vụ Chim Cắt Lớn đang lượn vòng ở độ cao hơn 3.000m. Gió rít gào bên tai, nhưng nhịp tim của anh chàng vẫn ổn định như một cỗ máy đếm giờ. |  | chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng bay lơ lửng giữa tầng mây mỏng ngược sáng dưới ánh trăng lưỡi liềm, kính phi công hạ xuống che mắt, đôi cánh khép hờ định hình tư thế tác chiến; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b04 | 00:21.0–00:30.0 (9.0s) | L43 | Đôi mắt của chim cắt sở hữu hai hố thị giác riêng biệt trên mỗi võng mạc, cho phép anh chàng vừa phóng to mục tiêu như kính viễn vọng vừa quan sát toàn cảnh 360°! |  | Sơ đồ giải phẫu mắt chim cắt với hai tiêu cự fovea phát sáng hai chùm tia nhìn quét qua không gian ban đêm; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b05 | 00:30.0–00:39.0 (9.0s) | L44 | Bộ đàm trung tâm rè lên giọng Chỉ Huy Mật Vụ: "Mật danh Tia Chớp, mục tiêu là chiếc rơ-le nguồn laser đặt ngay trên đỉnh vòm kính. Cậu chỉ có đúng một cơ hội duy nhất." |  | Cận cảnh anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm đứng trong phòng điều khiển, một tay giữ tai nghe bộ đàm, mắt nhìn vào màn hình hiển thị tọa độ điểm đỏ nhấp nháy trên đỉnh tháp; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b06 | 00:39.0–00:48.6 (9.6s) | L45 | Nhắc nhở nhẹ nhàng từ bộ phận giám sát: nếu cậu bay thẳng, áp lực gió sẽ thổi bung cả mắt lẫn mũi cậu đấy! Cẩn thận kẻo biến thành món chim nướng siêu thanh! |  | chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép chõ mỏ vào micro phòng truyền tin, vẻ mặt nhăn nhở cà khịa nhưng ánh mắt vẫn chăm chú theo dõi màn hình tín hiệu; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b07 | 00:48.6–00:57.3 (8.7s) | L46 | Chim Cắt Lớn chỉ nhếch mép cười khẩy qua bộ đàm. Những kẻ nghiệp dư luôn nghĩ bay nhanh chỉ cần đôi cánh khỏe, nhưng họ đâu biết bí mật nằm ở chính chiếc mũi của anh chàng! |  | Cận cảnh gương mặt sắc lạnh của chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng, chiếc mỏ khoằm vàng óng ánh ánh trăng, ánh mắt tập trung cao độ vào mục tiêu bên dưới; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b08 | 00:57.3–01:07.0 (9.7s) | L47 | Hãy nhìn sâu vào lỗ mũi của Chim Cắt Lớn. Các nhà khoa học tại đại học công nghệ vừa giải mã một kỳ quan kỹ thuật sinh học: một mấu lồi hình nón nhỏ bằng xương nằm ngay chính giữa khoang mũi! |  | Bản vẽ phóng to chi tiết giải phẫu học bên trong khoang mũi của chim cắt, hiện rõ cấu trúc mấu lồi hình nón tubercle bằng xương chia đôi dòng khí lao vào (không chữ, không số); KHÔNG có anh Chỉ Huy trong cảnh này. |
| b09 | 01:07.0–01:18.3 (11.3s) | L48 | Khi lao xuống với tốc độ xé gió, mấu xương này đóng vai trò như chiếc van điều áp của động cơ máy bay phản lực, làm chậm và đổi hướng luồng gió xoáy cực mạnh, giúp anh chàng hít thở nhẹ nhàng như đang ngồi uống trà! |  | Mô phỏng động lực học chất lưu sinh học: các mũi tên luồng khí đỏ lao thẳng vào mũi chim cắt bị bẻ cong thành các đường lượn sóng màu xanh êm dịu đi sâu vào phổi; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b10 | 01:18.3–01:27.5 (9.2s) | L49 | Không chỉ có mũi, cấu trúc lông cánh của chim cắt còn có những khe rãnh vi mô tự động nâng lên khi gặp áp lực lớn, triệt tiêu toàn bộ lực cản xoáy không khí! |  | Cận cảnh mép lông cánh của chim cắt tự động điều chỉnh độ cong khi gió rít qua, giữ cho cánh cứng cáp như cánh máy bay chiến đấu; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b11 | 01:27.5–01:33.5 (6.0s) | L50 | Tọa độ đã khóa! Chim Cắt Lớn thu gọn hai cánh sát vào thân, biến toàn bộ cơ thể thành một đầu đạn khí động học hoàn hảo! |  | chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng gập hẳn hai cánh thành hình giọt nước khí động học, đuôi ép chặt, cả thân mình lao dốc thẳng đứng chín mươi độ xuống màn đêm đen kịt; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b12 | 01:33.5–01:40.0 (6.5s) | L51 | Gia tốc tăng vọt! 100 cây số một giờ... 200 cây số một giờ... 300 cây số một giờ! Kim đo tốc độ radar bên dưới phòng chỉ huy quay tít mù! |  | Màn hình radar thế giới tự nhiên trong phòng điều khiển: kim đồng hồ đo vận tốc nhảy số liên tục từ vạch xanh sang vạch đỏ rực, phát ra tiếng tít tít dồn dập; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b13 | 01:40.0–01:48.9 (8.9s) | L52 | Và đây là con số kỷ lục từng được các nhà khoa học gắn chip đo đạc thực tế trên cơ thể một chú chim cắt: 389 km/h! Vận tốc nhanh nhất trong toàn bộ thế giới động vật! | **389 KM/H** · Vận tốc kỷ lục · R/380 · [0.5, 0.5] | Hình ảnh đồ họa ngoạn mục: chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng lao xuống như một quả tên lửa xé toạc màn mây, sóng xung kích hình nón màu trắng ngưng tụ quanh thân chim cắt xé rách không gian; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b14 | 01:48.9–01:55.9 (7.0s) | L53 | Tiếng rít xé rách không khí vang lên như một tiếng nổ siêu thanh trầm đục, làm rung chuyển cả những vách kính trên đỉnh tháp pháo đài! |  | Sóng âm thanh lan tỏa hình gợn sóng làm rung rinh các thanh xà kim loại trên vòm kính pháo đài; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b15 | 01:55.9–02:04.9 (9.0s) | L54 | Ở tốc độ 389 km/h, chỉ một hạt bụi nhỏ bay vào mắt cũng đủ làm nổ tung giác mạc. Nhưng Chim Cắt Lớn vẫn mở to mắt nhìn rõ từng chi tiết của mục tiêu! |  | Cận cảnh đôi mắt tròn đen láy của chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng, con ngươi co lại cực đại, phản chiếu hình ảnh chiếc công tắc nguồn điện tử bên dưới; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b16 | 02:04.9–02:10.0 (5.1s) | L55 | Bí quyết là chiếc màng nháy trong suốt che phủ mắt, nhấp nháy với tần số chóng mặt: 120 lần/phút! | **120 LẦN/P** · Màng nháy mắt · L/420 · [0.4, 0.5] | Sơ đồ giải phẫu mắt chim cắt: chiếc màng nháy mỏng trong suốt quét qua nhãn cầu như chiếc gạt nước kính ô tô siêu tốc, giữ ẩm và bảo vệ mắt hoàn hảo; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b17 | 02:10.0–02:16.3 (6.4s) | L56 | Chiếc màng này vừa bôi trơn liên tục vừa lọc bụi bẩn, cho phép Chim Cắt Lớn duy trì tầm nhìn sắc như kính hiển vi điện tử giữa cơn bão gió! |  | Góc nhìn từ mắt chim cắt qua kính ngắm quang học: mục tiêu chiếc rơ-le điện nhỏ bằng chiếc hộp quẹt trên nóc pháo đài hiện lên rõ mồn một không một vệt mờ; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b18 | 02:16.3–02:24.6 (8.2s) | L57 | Tuyến lệ của chim cắt liên tục tiết ra một chất dịch nhầy đặc biệt có sức căng bề mặt cực lớn, không hề bị gió cuốn bay dù ở vận tốc xé rách âm thanh! |  | Giọt dịch nhầy bảo vệ mắt lấp lánh như một lớp tráng gương nano trên giác mạc của chim; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b19 | 02:24.6–02:28.9 (4.3s) | L58 | Khoảng cách còn 100 mét! Cột laser phòng vệ phát hiện mục tiêu và quét chéo qua! |  | Hai luồng tia laser đỏ rực từ tháp canh phóng vút tới cắt ngang đường bay, không khí xung quanh bốc khói khét lẹt; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b20 | 02:28.9–02:34.8 (5.9s) | L59 | Chim Cắt Lớn khẽ nghiêng một góc 45 độ theo đường xoắn ốc toán học, lượn né tia laser chỉ trong 0,1 giây! |  | chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng thực hiện cú bẻ lái lượn vòng xoắn ốc điệu nghệ trên không, tia laser sượt qua mép lông cánh làm rụng một sợi lông tơ nhỏ; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b21 | 02:34.8–02:41.8 (6.9s) | L60 | Đường bay xoắn ốc này được lập trình tự nhiên theo quy luật đường cong lô-ga-rít, giúp mắt chim luôn hướng thẳng vào mục tiêu trong khi toàn thân nghiêng né đạn! |  | Mô phỏng đường bay xoắn ốc màu vàng kim lượn lách qua các chùm tia laser đỏ rực đan chéo nhau; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b22 | 02:41.8–02:48.5 (6.7s) | L61 | Khoảng cách còn 10 mét! Anh chàng duỗi thẳng cặp móng vuốt vàng sắc nhọn, bọc mạ lớp thép bảo hộ, đạp thẳng vào công tắc nguồn điện tử! |  | Cận cảnh đôi móng vuốt sắc nhọn của chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng đạp trúng chiếc hộp cầu dao trung tâm, các tia lửa điện nổ tung tóe chói lòa; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b23 | 02:48.5–02:54.8 (6.3s) | L62 | Xoẹt! Tiếng điện nổ râm ran, toàn bộ mạng lưới laser bảo vệ trên không vụt tắt đen ngòm! Vòm kính pháo đài từ từ hé mở! |  | Toàn bộ hệ thống đèn laser trên tháp pháo đài chớp nháy rồi phụt tắt, cánh cửa vòm kính khổng lồ kêu kẽo kẹt trượt mở ra một lối vào tối om; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b24 | 02:54.8–03:03.6 (8.8s) | L63 | Chim Cắt Lớn dang rộng đôi cánh phanh gấp giữa không trung, nhẹ nhàng hạ cánh xuống mép thành đá, giơ một ngón cánh làm dấu hiệu thắng lợi qua camera ngực. |  | chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng đứng trên lan can đá ngẩng cao đầu chỉnh lại kính phi công, giơ ngón cánh ra hiệu OK về phía ống kính camera nhỏ trên ngực áo; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b25 | 03:03.6–03:10.1 (6.6s) | L64 | Thanh tiến độ Cửa Ải 1 trên bản đồ chuyển sang màu xanh ngọc bích! Không phận tử thần đã bị vô hiệu hóa hoàn toàn trong vòng chưa đầy 2 phút! |  | bản đồ hologram 3D của Pháo Đài Tự Nhiên nổi lơ lửng trong không khí, hiển thị 7 cửa ải an ninh phát sáng đỏ và thanh tiến độ phá khóa màu xanh ngọc (không có chữ, không có số) cập nhật tín hiệu: biểu tượng gió lốc Cửa Ải 1 đổi từ màu đỏ rực sang màu xanh ngọc phát sáng êm dịu, thanh tiến độ nhích lên một nấc; anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm gật đầu hài lòng. |
| b26 | 03:10.1–03:20.2 (10.1s) | L65 | Nhưng niềm vui chưa kịp trọn vẹn thì dưới chân tháp, một tiếng còi báo động trầm đục vang lên từ lòng đất. Hệ thống phòng thủ tự động vừa đóng sập toàn bộ cửa thông gió! |  | Cửa sắt dày cộp dưới chân tháp đóng ầm xuống, đèn cảnh báo màu vàng chớp liên hồi, khói xám bắt đầu tỏa ra từ các kẽ đá; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b27 | 03:20.2–03:25.4 (5.2s) | L66 | Lối vào duy nhất lúc này là hệ thống đường ống xả ngầm sâu dưới lòng đất, nơi không hề có dưỡng khí và ngập tràn sương |  | Bản đồ hologram hiển thị một mạng lưới đường ống ngoằn ngoèo màu xám chì nằm sâu dưới lòng đá, đầy biểu tượng khí độc và bình axit; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b28 | 03:25.4–03:32.3 (6.9s) | L67 | axit. Chỉ Huy Mật Vụ bấm nút gọi nội bộ: "Đặc vụ Chuột Chũi Trũi, khoang yếm khí đã sẵn sàng cho cậu. Đừng có mải ngủ gật đấy nhé!" |  | Cận cảnh anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm nhìn vào micro, bên cạnh là chiếc ghế trống của chuột chũi với một lỗ hổng tròn vo vừa bị đào khoét dưới gầm bàn; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b29 | 03:32.3–03:39.0 (6.7s) | L68 | Từ dưới đáy một đường ống kim loại gỉ sét, một cái mũi màu hồng nhăn nheo khẽ thò ra, hắt xì một cái rõ to. Cuộc đột nhập tầng hầm bắt đầu! |  | Dưới đường ống tối tăm, chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên thò đầu ra khịt khịt mũi, hai chiếc răng cửa sáng loáng dưới ánh đèn pin mini, chuẩn bị bò vào mê cung tăm tối. |
| b30 | 03:39.0–03:44.7 (5.7s) | L69 | Đặc vụ Chuột Chũi xoa hai chân trước, chuẩn bị kích hoạt vũ khí sinh học chống ngạt thở vô song của mình! |  | chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên chỉnh lại cặp kính nhìn đêm, cười toe toét khoe hai chiếc răng cửa dài ngoằng chuẩn bị đối đầu với hầm ngầm không dưỡng khí. |
| b31 | 03:44.7–03:51.8 (7.1s) | L70 | Các phi công lái máy bay siêu thanh của quân đội từng thử nghiệm mô phỏng đường bay của chim cắt trên máy tính và đều phải lắc đầu chịu thua! |  | Màn hình mô phỏng máy bay chiến đấu phản lực bay song song với một chú chim cắt lớn đang lao dốc; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b32 | 03:51.8–03:59.1 (7.3s) | L71 | Ở góc bổ nhào 45 độ, gia tốc trọng trường kéo chú chim lao đi nhanh hơn bất kỳ mũi tên bắn tỉa nào từng được phóng ra! |  | Đường bay đỏ rực của chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng cắt ngang các tầng mây đen, tạo nên một vệt khói ngưng tụ trắng xóa; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b33 | 03:59.1–04:06.2 (7.1s) | L72 | Đôi mắt chim cắt với lớp màng nháy siêu việt vẫn liên tục truyền về trung tâm chỉ huy những hình ảnh tĩnh nét đến từng con ốc vít của trạm phát laser! |  | Màn hình nhận tín hiệu từ camera gắn trên trán chim cắt hiển thị rõ nét từng rãnh ren của bu-lông công tắc; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b34 | 04:06.2–04:13.7 (7.4s) | L73 | Nhịp đập của đôi cánh chim cắt khi lấy thăng bằng sau cú bổ nhào phát ra tiếng rít xé gió khiến cả đàn chim đêm xung quanh phải nể sợ! |  | chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng bay vút ngang qua đỉnh tháp pháo đài, để lại một vệt hào quang xám bạc lấp lánh; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b35 | 04:13.7–04:21.6 (8.0s) | L74 | Bộ cảm biến gia tốc trên ngực áo truyền về trung tâm chỉ huy xác nhận: cấu trúc xương đòn của chim cắt đã hấp thụ hoàn hảo mọi xung chấn của không khí! |  | Đồ thị phân tích lực cản khí động học hiển thị mức cân bằng tuyệt đối không một điểm dao động bất thường; KHÔNG có anh Chỉ Huy trong cảnh này. |

### scene03 · HẦM NGẦM 0% OXY & CHUỘT CHŨI TRŨI · 296.1s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.0 (7.0s) | L75 | Địa đạo ngầm dưới chân Pháo Đài Tự Nhiên là một cái bẫy chết chóc được thiết kế để tiêu diệt bất kỳ sinh vật hiếu khí nào dám bén mảng tới. |  | Khung cảnh đường hầm ngầm bằng kim loại rỉ sét u ám, các vòi phun sương tự động đang phun ra những làn sương màu vàng chanh đậm đặc mùi axit, trên tường có các cảm biến đo nồng độ dưỡng khí; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b02 | 00:07.0–00:17.2 (10.2s) | L76 | Cửa thép phía sau vừa sập xuống, máy hút chân không lập tức khởi động rên rỉ ầm ầm. Nồng độ dưỡng khí trong ống tụt dốc không phanh: 20 phần trăm... mười phần trăm... năm phần trăm... rồi chạm đáy số không tròn trĩnh! |  | Đồng hồ đo nồng độ oxy trên tường tụt nhanh về vạch số không đỏ rực, tiếng hút gió rít lên chói tai trong đường ống chật hẹp tối tăm; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b03 | 00:17.2–00:27.0 (9.7s) | L77 | Không có lấy một phân tử khí thở. Bất kỳ loài thú nào, kể cả con người hay sư tử, chỉ cần hít thở trong môi trường này 45 giây là sẽ bất tỉnh nhân sự, tế bào não chết vĩnh viễn sau 3 phút. |  | Một mô hình đồ họa y khoa giải thích sự ngạt thở: các tế bào não thông thường bị thiếu oxy teo lại và phát tín hiệu cảnh báo màu đỏ chớp nháy (không chữ, không số); KHÔNG có anh Chỉ Huy trong cảnh này. |
| b04 | 00:27.0–00:34.9 (7.9s) | L78 | CO₂ và nồng độ axit trong hầm tăng vọt lên mức kịch độc, đủ sức làm bỏng cháy niêm mạc phổi của bất kỳ kẻ xâm nhập nào trong tích tắc! |  | Khói độc màu xám xịt cuộn tròn quanh các vách ống kim loại, rỉ sét ăn mòn bề mặt tạo thành những vệt rỗ loang lổ; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b05 | 00:34.9–00:42.7 (7.9s) | L79 | Nhưng kẻ đang bò trong đường ống này lại là một sinh vật coi việc thiếu dưỡng khí... chỉ là một buổi dạo chơi nhẹ nhàng sau bữa trưa! |  | chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên lắc lư cái đầu nhăn nheo, bốn chân ngắn thoăn thoắt bò tới tấp trong đường ống kim loại, cặp kính hồng ngoại to sụ chớp chớp đèn xanh; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b06 | 00:42.7–00:51.5 (8.7s) | L80 | Đặc vụ Chuột Chũi Trũi thong dong bước đi, không hề tỏ ra hoảng loạn hay ngột ngạt. Bí mật sinh học chấn động gì đã giúp anh chàng này thách thức quy luật hô hấp của muôn loài? |  | Cận cảnh gương mặt của chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên, hai chiếc răng cửa to tướng gõ lách cách vào thành ống thép, chiếc đuôi ngắn ngoe nguẩy điều hướng; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b07 | 00:51.5–01:03.2 (11.7s) | L81 | Cơ thể không lông của anh chàng được bao bọc bởi một lớp da siêu đàn hồi chứa đầy phân tử axit hyaluronic trọng lượng cực cao, giúp da trơn tuột không hề trầy xước khi cọ xát vào mép ống kim loại sắc nhọn! |  | Kính hiển vi quét màng tế bào da chuột chũi: các chuỗi phân tử cao phân tử HMM-HA đan chéo nhau như một mạng lưới bảo vệ dẻo dai chống lại mọi ma sát; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b08 | 01:03.2–01:12.5 (9.3s) | L82 | Năm 2017, một nghiên cứu đột phá đăng trên tạp chí Khoa Học danh giá đã vén màn bí mật: khi hết sạch dưỡng khí, cơ thể Chuột Chũi Trũi tự động chuyển sang chế độ hoạt động của... thực vật! |  | Tranh minh họa sinh học so sánh hai nhánh tiến hóa: một bên là cây xanh quang hợp rực rỡ, một bên là chú chuột chũi trũi đang phát sáng các hạt phân tử đường màu xanh lục bên trong tế bào; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b09 | 01:12.5–01:23.2 (10.8s) | L83 | Đúng vậy, bạn không nghe nhầm đâu! Bộ não và trái tim của các loài động vật có vú thông thường chỉ có thể đốt đường glucose bằng dưỡng khí để tạo năng lượng. Không có dưỡng khí, cỗ máy ngừng chạy ngay lập tức. |  | Sơ đồ phân tử: chu trình phân giải đường glucose thông thường bị dấu chéo đỏ chặn đứng khi thiếu oxy, biểu tượng pin năng lượng cạn kiệt; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b10 | 01:23.2–01:34.3 (11.1s) | L84 | Nhưng Chuột Chũi Trũi lại sở hữu những thụ thể vận chuyển đường đặc biệt có tên gọi là phân tử vận chuyển đường hoa quả GLUT5, giúp chúng kích hoạt việc đốt trực tiếp đường fructose mà không cần đến một phân tử dưỡng khí nào! |  | Các phân tử đường fructose hình ngôi sao màu tím lấp lánh tràn vào tế bào tim và não của chuột chũi, tái kích hoạt bộ máy năng lượng hoạt động trơn tru; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b11 | 01:34.3–01:42.0 (7.7s) | L85 | Đường fructose đi thẳng vào chu trình đường phân ở cơ tim và vỏ não, sản sinh năng lượng duy trì sự sống bền bỉ ngay giữa vùng chân không! |  | Mô phỏng các hạt năng lượng ATP màu vàng sáng bừng lên bên trong tế bào não chuột chũi, nuôi dưỡng các xung thần kinh hoạt động bình thường; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b12 | 01:42.0–01:49.5 (7.5s) | L86 | Thử nghiệm khoa học chấn động tại phòng thí nghiệm đã chứng minh: Chuột Chũi Trũi có thể sống sót khỏe mạnh suốt 18 phút trong môi trường hoàn toàn 0% oxy! | **18 PHÚT** · Sống ở 0% Oxy · R/390 · [0.5, 0.6] | chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên nằm thư thái trong một buồng kính thí nghiệm chân không kín mít, xung quanh là các nhà khoa học trố mắt nhìn đồng hồ bấm giờ chạm mốc 18:00 (không chữ); KHÔNG có anh Chỉ Huy trong cảnh này. |
| b13 | 01:49.5–01:57.0 (7.6s) | L87 | Khi có dưỡng khí trở lại, chúng đứng dậy phủi bụi và đi lại bình thường như chưa từng có chuyện gì xảy ra, không hề tổn thương dù chỉ một tế bào thần kinh! |  | chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên vươn vai ngáp một cái thật dài, phủi hai móng trước vào bụng rồi tiếp tục bò thoăn thoắt trên mặt sàn; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b14 | 01:57.0–02:06.7 (9.6s) | L88 | Nhịp tim của chuột chũi tự động hạ từ 200 nhịp một phút xuống còn 50 nhịp một phút để tiết kiệm tối đa năng lượng, đưa cơ thể vào trạng thái ngủ đông cục bộ cực kỳ thông minh! |  | Biểu đồ nhịp tim co giãn chậm rãi và ổn định, duy trì áp lực nước màu hoàn hảo đến các cơ quan trọng yếu; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b15 | 02:06.7–02:14.0 (7.4s) | L89 | Nhưng thử thách của Cửa Ải 2 chưa dừng lại ở đó. Hệ thống phòng thủ tự động phát hiện kẻ xâm nhập vẫn còn sống, liền kích hoạt tầng bẫy thứ hai: vòi phun |  | Các đầu phun trên trần đường ống tự động xoay nòng, phun ra từng luồng sương axit châm chích mù mịt phủ kín toàn bộ lối đi; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b16 | 02:14.0–02:20.3 (6.2s) | L90 | axit! Làn sương axit có độ pH ba cực kỳ ăn mòn và bỏng rát, đủ sức làm phồng rộp làn da của bất kỳ kẻ đột nhập nào trong nháy |  | Những giọt axit màu xanh vàng rơi xuống sàn kim loại kêu xèo xèo, bốc lên những làn khói cay nồng mù mịt; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b17 | 02:20.3–02:27.6 (7.4s) | L91 | mắt. Sương axit bắn thẳng vào thân mình không một sợi lông của Chuột Chũi Trũi. Bộ đàm phòng chỉ huy nín thở! Chỉ Huy Mật Vụ siết chặt tay! |  | Màn hình theo dõi nhiệt độ cơ thể trong phòng điều khiển chao đảo, anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm nhíu mày áp sát mặt vào màn hình kính râm; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b18 | 02:27.6–02:33.8 (6.2s) | L92 | Nhưng Chuột Chũi Trũi... chỉ khẽ gãi gãi nách rồi tiếp tục bò! Anh chàng thậm chí còn không thèm chớp mắt! |  | chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên đứng giữa làn sương axit mù mịt, lấy một chân sau gãi gãi bụng vẻ mặt tỉnh bơ ngây thơ như đang tắm suối nước nóng; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b19 | 02:33.8–02:41.3 (7.5s) | L93 | Bởi vì tạo hóa đã tặng cho loài vật này một món quà vô giá: chúng hoàn toàn mất tín hiệu dẫn truyền cơn đau của chất hóa học P và thụ thể thần kinh |  | Hình vẽ hiển vi phóng to sợi dây thần kinh dưới da của chuột chũi: tín hiệu đau hình tia sét màu đỏ bị chặn đứng hoàn toàn bởi một nút công tắc sinh học tự nhiên màu xanh ngọc; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b20 | 02:41.3–02:49.6 (8.3s) | L94 | cảm giác! Axit hay ớt cay hay lửa rát chạm vào da chuột chũi trũi cũng chẳng khác gì nước lã gội đầu! Chúng không hề biết đau là cái gì trên cõi đời này! |  | chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên tiếp tục bò qua vũng axit bốc khói, thản nhiên như một chiến binh mang giáp hộ thân tàng hình; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b21 | 02:49.6–02:59.6 (10.0s) | L95 | Các nhà thần kinh học tại đại học Cambridge phát hiện ra rằng thụ thể kênh ion TrkA của chuột chũi đã bị đột biến, biến chúng thành loài động vật có vú duy nhất trơ lì trước axit! |  | Sơ đồ kênh ion trên màng tế bào thần kinh: phân tử axit chạm vào thụ thể nhưng không thể kích hoạt xung điện thần kinh truyền về tủy sống; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b22 | 02:59.6–03:05.3 (5.8s) | L96 | Lối đi phía trước đột ngột bị một tảng đá cản đường, và đường ống quá hẹp khiến chuột chũi không thể xoay người quay đầu lại! |  | Một khối đá xám to đùng rơi chắn ngang đường ống chật chội, khe hở chỉ vừa khít thân hình chuột chũi, không có chỗ để quay đầu xe; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b23 | 03:05.3–03:12.9 (7.6s) | L97 | Không cần quay đầu! Chuột Chũi Trũi cài số lùi, chạy lùi với tốc độ nhanh y hệt như chạy tiến nhờ chiếc đuôi nhạy bén như chiếc ăng-ten cảm biến lùi ô tô! |  | chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên chạy giật lùi thoăn thoắt về phía sau, chiếc đuôi ngắn ngỏng lên chạm nhẹ vào hai bên vách ống để dò đường cực kỳ chuẩn xác; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b24 | 03:12.9–03:17.6 (4.7s) | L98 | Anh chàng đổi hướng bò sang một nhánh rẽ thông hơi, tiếp cận chiếc van khóa áp lực chính của pháo đài! |  | chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên chui vào một ngách thông gió thẳng đứng, trèo ngược lên bằng bốn chân có móng vuốt chắc khỏe; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b25 | 03:17.6–03:24.3 (6.7s) | L99 | Cặp răng cửa khổng lồ dài ngoằng thò ra ngoài môi bắt đầu phát huy tác dụng. Chuột chũi có thể cử động hai chiếc răng cửa độc lập như một đôi đũa gắp thức ăn! |  | Cận cảnh hai chiếc răng cửa to tướng của chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên kẹp chặt lấy chiếc chốt khóa van kim loại, cơ hàm nghiền nghiến với lực cắn khủng khiếp; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b26 | 03:24.3–03:32.7 (8.4s) | L100 | Rắc! Chiếc chốt khóa bằng đồng thau bị cắn đứt đôi! Chuột chũi không hề nuốt phải một hạt bụi kim loại nào vì môi của anh chàng khép kín phía sau răng! |  | Chiếc then cài kim loại gãy vụn rơi lanh canh, chiếc van xoay tròn mở bung ra, luồng không khí sạch bên ngoài ùa vào đường hầm rào rào; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b27 | 03:32.7–03:39.9 (7.2s) | L101 | Đèn báo động đỏ chuyển sang màu xanh lá dịu mát! Hệ thống hút chân không bị vô hiệu hóa! Cửa Ải 2 đã được dọn sạch hoàn toàn! |  | Màn hình trung tâm bản đồ hologram 3D của Pháo Đài Tự Nhiên nổi lơ lửng trong không khí, hiển thị 7 cửa ải an ninh phát sáng đỏ và thanh tiến độ phá khóa màu xanh ngọc (không có chữ, không có số) phát ra âm thanh êm dịu, biểu tượng đường ống yếm khí chuyển sang màu xanh ngọc, thanh tiến độ phá khóa nhảy lên nấc thứ hai; anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm khẽ mỉm cười gậ |
| b28 | 03:39.9–03:46.9 (7.0s) | L102 | Chuột Chũi Trũi ngoi đầu lên từ một lỗ thông gió ở sàn tầng trệt, giơ hai chân trước phủi mũi, phát ra một tiếng rít vui tai qua bộ đàm. |  | chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên ló đầu lên mặt sàn đá sạch sẽ, giơ hai móng trước làm dấu chiến thắng, cặp kính nhìn đêm hồng ngoại lóe lên ánh sáng xanh tinh nghịch. |
| b29 | 03:46.9–03:55.9 (9.1s) | L103 | Nhưng ngay khi cửa mở ra, một luồng khí lạnh buốt xương tủy bất ngờ ùa tới từ cánh cửa hành lang tiếp theo, làm đóng băng ngay lập tức những giọt nước đọng trên sàn đá! |  | Hơi sương lạnh buốt màu trắng xóa tràn qua khe cửa hầm, mặt sàn đá đóng một lớp băng trơn nhẵn bóng, các nhũ băng nhọn hoắt rủ xuống từ trần nhà; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b30 | 03:55.9–04:02.2 (6.2s) | L104 | Cửa Ải 3: Kho Lạnh Cực Hạn với nhiệt độ -20°C và hệ thống cảm biến hồng ngoại tầm nhiệt tinh vi nhất thế giới! |  | Bản đồ bản đồ hologram 3D của Pháo Đài Tự Nhiên nổi lơ lửng trong không khí, hiển thị 7 cửa ải an ninh phát sáng đỏ và thanh tiến độ phá khóa màu xanh ngọc (không có chữ, không có số) hiển thị căn phòng tiếp theo phủ đầy hoa tuyết màu xanh băng giá, các máy quét thân nhiệt màu đỏ cam đang lia khắp sàn nhà; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b31 | 04:02.2–04:09.4 (7.3s) | L105 | Mọi cơ thể ấm áp bước vào đây sẽ bị phát hiện trong vòng nửa giây. Chỉ có một sinh vật có thể biến mình thành một tảng băng vô tri vô giác để vượt qua cửa ải này. |  | Cận cảnh anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm quay sang nhìn chú Ếch Gỗ Bắc Cực hoạt hình da nâu vàng có vệt đen qua mắt như mặt nạ Zorro, đeo khăn quàng cổ đỏ thắm chống rét, người phủ lớp sương tuyết lấp lánh đang bình thản nhấp một ngụm nước đá trong góc phòng. |
| b32 | 04:09.4–04:13.3 (3.8s) | L106 | "Đặc vụ Ếch Gỗ Bắc Cực, đã đến lúc cho cả pháo đài thấy thế nào là nghệ thuật ngủ đông bất |  | chú Ếch Gỗ Bắc Cực hoạt hình da nâu vàng có vệt đen qua mắt như mặt nạ Zorro, đeo khăn quàng cổ đỏ thắm chống rét, người phủ lớp sương tuyết lấp lánh thắt lại chiếc khăn quàng cổ màu đỏ, bước ra ánh đèn, đôi mắt tròn to lấp lánh sự tự tin của một chuyên gia sinh tồn vùng cực. |
| b33 | 04:13.3–04:20.2 (6.9s) | L107 | tử!" Và phía sau lưng, tiếng cãi cọ qua kênh bộ đàm bắt đầu bùng nổ, báo hiệu một sự cố hài hước không thể lường trước! |  | Chiếc máy bộ đàm trên bàn tác chiến nhấp nháy đèn vàng báo hiệu cuộc gọi khẩn cấp từ các đặc vụ hậu trường. |
| b34 | 04:20.2–04:28.5 (8.2s) | L108 | Kỳ tích chuyển hóa đường fructose của Chuột Chũi Trũi đang mở ra một cuộc cách mạng y học lớn trong việc điều trị các bệnh nhân bị nhồi máu cơ tim và đột quỵ do thiếu oxy! |  | Tranh vẽ nghiên cứu y khoa hiện đại: hình ảnh trái tim người được bảo vệ bởi cơ chế chuyển hóa đường fructose mô phỏng từ chuột chũi; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b35 | 04:28.5–04:35.7 (7.3s) | L109 | Khi oxy cạn kiệt, các tế bào tim của chuột chũi không hề bị co thắt hay hoại tử, mà vẫn đập êm ả nhờ dòng năng lượng fructose ngọt ngào! |  | Mô phỏng các tế bào cơ tim chuột chũi co bóp đều đặn dưới ánh sáng huỳnh quang y tế; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b36 | 04:35.7–04:41.9 (6.1s) | L110 | Cơ thể không lông của chúng còn chứa một loại gen đặc biệt giúp sửa chữa tế bào thần kinh với tốc độ nhanh gấp năm lần các loài chuột thông |  | Chuỗi xoắn kép ADN của chuột chũi phát sáng các điểm liên kết tự phục hồi màu xanh ngọc bích; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b37 | 04:41.9–04:50.5 (8.7s) | L111 | thường! Nhờ tốc độ tiêu thụ đường fructose cực kỳ chậm rãi, chuột chũi có thể duy trì hoạt động của các cơ quan nội tạng mà không hề tạo ra độc tố axit lactic gây mỏi cơ! |  | Kính hiển vi hiển thị tế bào cơ chuột chũi không hề tích tụ axit lactic sau mười tám phút vận động trong buồng chân không; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b38 | 04:50.5–04:56.1 (5.6s) | L112 | Đặc vụ Chuột Chũi Trũi quệt mồ hôi trên mũi, nở một nụ cười rạng rỡ của một nhà quán quân sinh tồn không biết mệt mỏi! |  | chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên giơ hai ngón chân trước lên làm dấu chữ V chiến thắng trước ống kính camera thông hơi; KHÔNG có anh Chỉ Huy trong cảnh này. |

### scene04 · CHUỘT CHŨI ĐÀO NHẦM KHO BÁNH & QUẠ ĐEN ĐÒI TĂNG LƯƠNG · 226.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.0 (7.0s) | L113 | Điệp vụ thế kỷ tưởng chừng như đang diễn ra hoàn hảo đến từng tích tắc... thì kênh bộ đàm nội bộ bắt đầu phát ra những âm thanh cực kỳ bất |  | Căn phòng chỉ huy của anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm, chiếc máy bộ đàm để bàn bắt đầu phát ra những tiếng rè rè lẹt xẹt, xen lẫn tiếng nhai nhồm nhoàm và tiếng cãi cọ ầm ĩ; anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm ôm trán thở dài bất lực. |
| b02 | 00:07.0–00:13.5 (6.5s) | L114 | thường. Tiếng nhai chóp chép giòn tan vang lên rành rọt qua chiếc loa điều khiển trung tâm, to đến mức át cả tiếng còi báo động của pháo |  | Chiếc loa truyền tin phóng đại sóng âm thanh dạng răng cưa, các nhân viên kỹ thuật đeo tai nghe phải nhăn mặt giật tai nghe ra; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b03 | 00:13.5–00:22.4 (8.8s) | L115 | đài! "Báo cáo Chỉ Huy! Tôi vừa đột nhập thành công vào phòng chứa tài liệu bí mật! Nhưng ở đây không có tài liệu... chỉ có toàn là khoai tây sấy bơ thơm lừng!" |  | chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên ngồi lọt thỏm giữa một kho lương thực đầy ắp các bao tải ngũ cốc và củ quả của pháo đài, hai tay ôm một củ khoai tây to gấp đôi người mình, mải mê gặm lấy gặm để; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b04 | 00:22.4–00:30.8 (8.4s) | L116 | Khoai tây này ngọt lắm sếp ơi! Có cần tôi vận chuyển về phòng chỉ huy năm bao làm quà lưu niệm cho Biệt Đội Đặc Nhiệm Sinh Học không ạ? |  | Cận cảnh chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên mồm dính đầy vụn khoai tây, hai mắt hí tít sau cặp kính nhìn đêm, giơ củ khoai tây lên vẫy vẫy trước camera; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b05 | 00:30.8–00:37.1 (6.3s) | L117 | Sau phi vụ này tôi định mở một chuỗi nhà hàng khoai nướng yếm khí dưới lòng đất, sếp nhớ đến cắt băng khánh thành nhé! |  | chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên giơ một ngón chân cái lên làm dáng quảng cáo nhà hàng tương lai đầy tự tin; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b06 | 00:37.1–00:44.5 (7.4s) | L118 | Chỉ Huy Mật Vụ hít một hơi thật sâu, giọng lạnh như băng truyền qua mic: "Đặc vụ Chuột Chũi... cậu vừa đào nhầm vào kho bếp của bảo vệ pháo đài |  | Cận cảnh anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm nghiến răng, chiếc kính râm trượt xuống sống mũi để lộ ánh mắt hình viên đạn, ngón tay gõ nhịp lách cách đe dọa lên micro; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b07 | 00:44.5–00:51.3 (6.9s) | L119 | rồi đấy." "Nếu trong vòng 30 giây nữa cậu không kéo cái thân nhăn nheo của mình ra khỏi kho khoai tây, tôi sẽ ghi tên cậu vào danh sách cắt khẩu phần ăn ba |  | anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm cầm cây bút lông đỏ vạch một đường thật đậm vào trang hồ sơ có dán ảnh chuột chũi trũi; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b08 | 00:51.3–00:56.6 (5.2s) | L120 | tháng!" "Và đừng bao giờ mơ đến chuyện mở nhà hàng khoai nướng khi đang trong giờ làm việc của Tổng Cục!" |  | anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm đập cây bút lông xuống bàn làm mực đỏ bắn tung tóe lên mặt bàn kính; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b09 | 00:56.6–01:02.6 (6.0s) | L121 | Ối sếp ơi! Tôi đi ngay đây! Nhưng cho tôi xin nhét thêm một củ nhỏ vào túi áo khoác nhé! |  | chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên giật mình nhảy cẫng lên, vội vã nhét vội một củ khoai tây vào túi thắt lưng rồi cong đuôi lặn mất tăm xuống lỗ đất vừa đào; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b10 | 01:02.6–01:11.6 (9.0s) | L122 | Chưa kịp thở phào thì một tiếng rít chói tai khác lại chèn ngang vào tần số liên lạc tối mật. Lần này là giọng nói đanh đá và đậm chất con buôn của Quạ Đen! |  | chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép xuất hiện trên màn hình camera phụ, đang dùng một chiếc móng chân gảy gảy vào mic bộ đàm, chiếc mỏ kẹp một tập giấy ghi chép chi phí; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b11 | 01:11.6–01:19.2 (7.6s) | L123 | A lô Chỉ Huy nghe rõ không? Kênh mã hóa này tín hiệu tốt đấy! Tiện thể tôi xin gửi báo cáo tài chính cập nhật trước khi bước vào Cửa Ải 3 và Cửa Ải 4! |  | Cận cảnh chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép nghiêng đầu chớp mắt tinh quái, tay kia xòe ra một tờ hóa đơn thanh toán dài ngoằng vẽ nguệch ngoạc bằng mực tím; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b12 | 01:19.2–01:26.8 (7.5s) | L124 | Hợp đồng ban đầu chỉ ghi giải mã ba cái ổ khóa cơ học đơn giản. Đằng này toàn là bẫy gương tâm lý với khóa liên hoàn 8 bước của các kỹ sư thiên tài! |  | chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép chỉ mỏ vào sơ đồ bẫy rập phức tạp trên màn hình, vẻ mặt đầy bất mãn đòi quyền lợi chính đáng của một chuyên gia công nghệ; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b13 | 01:26.8–01:35.8 (9.0s) | L125 | Tôi yêu cầu tăng lương gấp đôi! Cộng thêm điều khoản bảo hiểm gãy mỏ khi tác chiến và một thùng hạt dẻ thượng hạng! Nếu không thì tự đi mà giải mã mê cung nhé! |  | chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép khoanh hai cánh trước ngực quay lưng lại camera, làm bộ dỗi hờn không thèm hợp tác; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b14 | 01:35.8–01:43.4 (7.6s) | L126 | Toàn bộ phòng chỉ huy rơi vào im lặng sượng sùng. Chỉ Huy Cú Mèo từ từ với tay lấy một tập hồ sơ có dán nhãn đỏ: "Hồ sơ quậy phá nơi công cộng của Quạ Đen". |  | anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm thong thả mở tập hồ sơ dày cộp, bên trong có dán ảnh chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép đang trộm bóng đèn xe cảnh sát và trêu chọc chó nhà hàng xóm; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b15 | 01:43.4–01:48.5 (5.1s) | L127 | "Đặc vụ Quạ Đen, cậu có muốn tôi nhắc lại vụ án trộm mất 60 chiếc thìa bạc tại dinh thự thị trưởng năm ngoái không?" |  | anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm cầm kính lúp soi vào bức ảnh đen trắng chụp chiếc tổ quạ chứa đầy thìa nĩa bằng bạc lấp lánh; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b16 | 01:48.5–01:57.0 (8.5s) | L128 | "Bằng chứng vẫn còn nằm nguyên trong két sắt của tôi đấy. Nếu phi vụ này thành công, hồ sơ đó sẽ biến mất trong lò thiêu hủy. Cậu thấy mức lương đó đã đủ hấp dẫn chưa?" |  | anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm khẽ cười nửa miệng, quẹt que diêm dí sát vào góc tập hồ sơ làm mép giấy hơi bén lửa; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b17 | 01:57.0–02:05.6 (8.6s) | L129 | Ấy ấy Chỉ Huy bình tĩnh! Đùa tí cho không khí bớt căng thẳng thôi mà! Làm gì mà nóng tính thế! Tôi đang chuẩn bị sẵn bộ đồ nghề phá khóa rồi đây! |  | chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép hoảng hốt xua xua đôi cánh, mồm liến thoắng cười trừ, nhanh tay giấu nhẹm tờ hóa đơn vào trong túi áo; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b18 | 02:05.6–02:14.9 (9.3s) | L130 | Đúng lúc đó, Chim Cắt Lớn cũng chêm vào một câu qua sóng vô tuyến: "Đề nghị mọi người nói nhỏ giùm! Gió trên đỉnh tháp vừa làm bay mất một sợi lông đuôi quý giá của tôi rồi đây này!" |  | chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng đứng trên cột cờ tháp canh đang bận rộn dùng mỏ chải chuốt lại từng sợi lông vũ trên cánh, vẻ mặt cằn nhằn vì phong độ bị ảnh hưởng; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b19 | 02:14.9–02:22.5 (7.6s) | L131 | "Đồng đội gì mà người thì mê ăn khoai, kẻ thì đòi tăng lương, làm mất hết cả hình tượng điệp viên ngầu lòi của tôi!" Chim Cắt phụng phịu lắc đầu. |  | chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng soi bóng mình vào kính bảo hộ phi công, vuốt lại chùm lông đầu cho thật mượt mà; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b20 | 02:22.5–02:33.0 (10.5s) | L132 | Dưới bể nước dã chiến, Cá Voi Sát Thủ phun lên một cột nước cao 3 mét qua lỗ thở, phát ra tiếng cười khùng khục qua mic: "Mấy đứa trên cạn ồn ào quá! Bao giờ mới đến lượt đại ca biển cả ra tay đây?" |  | chú Cá Voi Sát Thủ hoạt hình thân đen bóng bụng trắng tinh, vây lưng cao vút cắm ăng-ten định vị sonar nhỏ xíu, miệng cười nhếch mép kiểu trùm mafia biển cả nhấp nhô vây lưng trên mặt nước, ngoác miệng cười để lộ hàm răng trắng bóng, đập vây đuôi tạo thành những đợt sóng dập dềnh; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b21 | 02:33.0–02:39.5 (6.5s) | L133 | Dê Núi và Lạc Đà cũng tranh thủ nhảy vào kênh chat tổng bàn tán về việc loại cỏ sa mạc nào ngọt hơn cỏ trên núi tuyết! |  | chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt và chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao cùng chia sẻ một cành cỏ khô qua màn hình chia đôi, vừa nhai vừa gật gù tâm đắc; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b22 | 02:39.5–02:45.8 (6.3s) | L134 | Chỉ Huy Mật Vụ gõ ngón tay xuống bàn ba tiếng cộc cộc cộc để lập lại trật tự: "Đủ rồi! Tất cả chuyển sang kênh tác chiến im lặng!" |  | anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm chỉnh lại micro cổ áo, ánh mắt trở lại vẻ uy nghiêm sắt đá của một thủ lĩnh mật vụ; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b23 | 02:45.8–02:54.5 (8.7s) | L135 | Sự hài hước chấm dứt ngay khi cánh cửa ngăn cách Cửa Ải 3 từ từ nâng lên. Hơi lạnh -20°C tràn ra ngoài làm ngưng đọng toàn bộ hơi nước thành những bông hoa tuyết rơi lả tả. |  | Cánh cửa thép dày ba tấc phủ đầy băng giá mở ra, bên trong là một căn phòng lạnh thấu xương với ánh sáng xanh lam ma quái phản chiếu từ những bức tường băng vĩnh cửu; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b24 | 02:54.5–03:00.6 (6.1s) | L136 | Đây không phải là chỗ để đùa giỡn nữa. Bất kỳ một bước chân sai lầm nào cũng sẽ biến cơ thể thành một bức tượng đá vĩnh cửu. |  | Các cảm biến hồng ngoại trên tường quét những chùm tia sáng vô hình qua lại như những mạng nhện tử thần giăng kín lối đi; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b25 | 03:00.6–03:08.1 (7.5s) | L137 | Đặc vụ Ếch Gỗ Bắc Cực đã bước vào phòng lạnh. Chiếc khăn quàng đỏ tung bay trong gió tuyết, ánh mắt anh chàng kiên định nhìn thẳng vào tâm điểm bẫy nhiệt độ. |  | chú Ếch Gỗ Bắc Cực hoạt hình da nâu vàng có vệt đen qua mắt như mặt nạ Zorro, đeo khăn quàng cổ đỏ thắm chống rét, người phủ lớp sương tuyết lấp lánh đứng trước ngưỡng cửa hầm băng, hít một hơi thật sâu làn không khí buốt giá, chuẩn bị bước vào cuộc thử nghiệm sinh học kỳ diệu nhất trong lịch sử sinh tồn. |
| b26 | 03:08.1–03:12.5 (4.4s) | L138 | Sinh mệnh của cả biệt đội đang nằm trong bàn tay của chú ếch nhỏ bé này! |  | Cận cảnh bàn chân có màng của chú Ếch Gỗ Bắc Cực hoạt hình da nâu vàng có vệt đen qua mắt như mặt nạ Zorro, đeo khăn quàng cổ đỏ thắm chống rét, người phủ lớp sương tuyết lấp lánh chạm nhẹ vào mặt băng buốt giá, chuẩn bị cho màn trình diễn đóng băng hồi sinh thần kỳ. |
| b27 | 03:12.5–03:18.8 (6.3s) | L139 | "Báo cáo Chỉ Huy, tôi vừa phát hiện thêm một bao hạt dẻ rang muối ở góc bếp! Tôi có thể mang theo để phòng khi đói bụng không ạ?" |  | chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên thò đầu ra từ bao hạt dẻ, hai má phồng to như hai chiếc bánh bao nhỏ; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b28 | 03:18.8–03:25.1 (6.3s) | L140 | Quạ Đen lập tức nhảy vào can thiệp: "Chia đôi! Nếu không tôi sẽ báo cáo lên Tổng Cục về tội danh ăn vụng quân lương của cậu!" |  | chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép giơ chiếc kìm mạ vàng lên gõ lách cách đòi chia phần chiến lợi phẩm; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b29 | 03:25.1–03:32.3 (7.1s) | L141 | Dê Núi Bắc Mỹ thở dài qua mic: "Mấy người suốt ngày chỉ nghĩ đến ăn uống! Nhìn tôi đây này, chỉ cần gặm một mẩu rêu đá là đủ leo vách 90° cả ngày |  | chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt đứng ngẩng cao đầu nhai nhóp nhép một mẩu rêu xanh, vẻ mặt đầy kiêu hãnh của một vận động viên ăn chay trường; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b30 | 03:32.3–03:41.1 (8.8s) | L142 | rồi!" Chỉ Huy Cú Mèo lắc đầu ngao ngán: "Giá như tinh thần đòi tăng lương của Quạ Đen được chuyển hóa thành tốc độ giải mã thì chúng ta đã xong nhiệm vụ từ lâu rồi!" |  | anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm nhấp một ngụm trà thảo mộc, khẽ mỉm cười châm biếm nhìn chiếc hóa đơn thanh toán của quạ; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b31 | 03:41.1–03:46.4 (5.4s) | L143 | Toàn đội cười òa lên qua kênh bộ đàm, xua tan đi bầu không khí ngột ngạt của những căn hầm ngầm pháo đài! |  | Tiếng cười rộn rã phát ra từ các góc liên lạc dã chiến, gắn kết tình đồng đội của mười quái kiệt thêm bền chặt; KHÔNG có anh Chỉ Huy trong cảnh này. |

### scene05 · KHO ĐÔNG LẠNH -20°C & ẾCH GỖ BẮC CỰC · 259.5s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.4 (8.4s) | L144 | Căn hầm Kho Lạnh Cực Hạn là nơi giam giữ những bí mật được bảo quản nghiêm ngặt nhất của Pháo Đài Tự Nhiên. Nhiệt độ bên trong duy trì ổn định ở mức -20°C. | **-20°C** · Kho Lạnh Cực Hạn · R/410 · [0.5, 0.6] | Căn phòng mái vòm bằng đá phủ kín một lớp băng dày trong suốt, các cột băng khổng lồ chống đỡ trần nhà, hơi lạnh mù mịt cuộn trào trên mặt sàn băng nhẵn thín; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b02 | 00:08.4–00:14.5 (6.1s) | L145 | Mọi thiết bị điện tử thông thường mang vào đây đều sẽ bị cạn pin trong vòng năm phút, các khớp kim loại co rút lại và kẹt cứng. |  | Một chiếc nhiệt kế điện tử gắn trên tường hiển thị cột thủy ngân tụt sâu xuống vạch âm hai mươi độ C phát ra tiếng bíp cảnh báo khô khốc; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b03 | 00:14.5–00:23.2 (8.7s) | L146 | Và điều nguy hiểm nhất là mạng lưới máy quét quang phổ hồng ngoại tầm nhiệt giăng kín mọi ngóc ngách. Chỉ cần phát hiện một điểm nhiệt trên không độ, súng đông lạnh tự động sẽ bắn nát mục |  | Màn hình radar tầm nhiệt hồng ngoại hiển thị toàn bộ căn phòng có màu xanh dương đậm buốt giá, bất kỳ một đốm sáng đỏ ấm áp nào xuất hiện cũng sẽ bị một vòng tròn ngắm bắn khóa chặt; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b04 | 00:23.2–00:30.0 (6.8s) | L147 | tiêu! Hệ thống cảm biến nhạy đến mức có thể phát hiện thân nhiệt của một chú ruồi nhỏ bay qua ở khoảng cách 20m! |  | Một chú bọ nhỏ bay vào cửa hầm lập tức bị một tia laser xanh quét trúng, đóng băng thành một viên đá nhỏ rơi xuống sàn vỡ tan; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b05 | 00:30.0–00:38.2 (8.2s) | L148 | Đặc vụ Ếch Gỗ Bắc Cực bước từng bước chậm rãi trên mặt băng trơn trượt. Làn da nâu vàng điểm vệt đen ngang mắt của anh chàng trông như một hiệp sĩ đeo mặt nạ kiên |  | chú Ếch Gỗ Bắc Cực hoạt hình da nâu vàng có vệt đen qua mắt như mặt nạ Zorro, đeo khăn quàng cổ đỏ thắm chống rét, người phủ lớp sương tuyết lấp lánh bước đi vững chãi trên mặt băng trơn nhẵn, chiếc khăn len đỏ bay nhẹ, ánh mắt bình thản nhìn về phía bàn điều khiển nhiệt độ nằm ở góc xa của căn hầm; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b06 | 00:38.2–00:48.1 (9.9s) | L149 | cường. Bộ đàm phòng chỉ huy vang lên giọng Chỉ Huy Cú Mèo: "Đặc vụ Ếch Gỗ, khoảng cách tới bàn điều khiển là 30m. Cậu chỉ có thể vượt qua nếu cơ thể hoàn toàn nguội lạnh như một tảng |  | anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm theo dõi sát sao qua màn hình hồng ngoại, các thông số nhịp tim của ếch gỗ đang hiển thị trên bảng đo lường y tế dã chiến; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b07 | 00:48.1–00:58.7 (10.6s) | L150 | đá." Ếch Gỗ gật đầu nhẹ nhàng. Anh chàng ngồi xổm xuống giữa sàn băng, thu hai chân sau sát vào bụng, nhắm nghiền hai mắt lại và bắt đầu kích hoạt cơ chế sinh học kỳ diệu nhất của mình! |  | chú Ếch Gỗ Bắc Cực hoạt hình da nâu vàng có vệt đen qua mắt như mặt nạ Zorro, đeo khăn quàng cổ đỏ thắm chống rét, người phủ lớp sương tuyết lấp lánh ngồi co tròn như một hòn sỏi trên mặt băng tuyết, một lớp màng sương tuyết trắng xóa bắt đầu lan dần từ đầu ngón chân lên khắp cơ thể; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b08 | 00:58.7–01:08.7 (10.0s) | L151 | Hãy quan sát kỳ quan sinh học đang diễn ra bên trong từng tế bào của chú ếch nhỏ bé này. Các nhà khoa học nghiên cứu sinh học vùng cực đã phải kinh ngạc thốt lên: đây là thuật giả kim đỉnh cao của tự nhiên! |  | Tranh vẽ hiển vi cắt lớp cơ thể chú ếch: gan của ếch gỗ bắt đầu phát sáng rực rỡ và phình to gấp ba lần kích thước bình thường; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b09 | 01:08.7–01:17.5 (8.8s) | L152 | Ngay khi tinh thể băng đầu tiên chạm vào da, gan của ếch gỗ lập tức hoạt động hết công suất, bơm một lượng khổng lồ đường glucose và chất urea vào toàn bộ hệ tuần hoàn! |  | Dòng nước màu mang hàng triệu phân tử đường glucose màu vàng óng ả và phân tử urea tỏa đi khắp các mao mạch, tràn vào bên trong từng tế bào của mọi cơ quan bên trong cơ thể; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b10 | 01:17.5–01:24.8 (7.3s) | L153 | Nồng độ đường bên trong tế bào tăng vọt gấp 50 đến 100 lần so với bình thường, biến dịch nội bào thành một loại si-rô đậm đặc không thể bị đông cứng! |  | Các tế bào bên trong cơ thể được bảo vệ an toàn bởi lớp màng si-rô đường tự nhiên, căng tròn và mềm mại dù nhiệt độ xung quanh đang hạ xuống âm hai mươi độ C; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b11 | 01:24.8–01:32.8 (7.9s) | L154 | Chất urea đóng vai trò như chiếc phao cứu sinh thứ hai, giữ nước bên trong tế bào không bị hút cạn ra ngoài khi các tinh thể đá hình thành xung quanh! |  | Kính hiển vi 3D mô phỏng phân tử urea liên kết với màng tế bào, ngăn ngừa hiện tượng co rút áp suất thẩm thấu gây chết tế bào; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b12 | 01:32.8–01:40.1 (7.3s) | L155 | Trong khi đó, ở khoảng không gian bên ngoài tế bào, điều kỳ diệu xảy ra: 65% toàn bộ lượng nước trong cơ thể ếch gỗ bắt đầu đông cứng thành băng! | **65% NƯỚC** · Đóng băng ngoại bào · L/380 · [0.4, 0.5] | Đồ họa 3D hiển vi: các tinh thể băng hình lục giác sắc nhọn mọc lên chi chít ở các mô liên kết ngoại bào xung quanh tế bào nhưng không thể xuyên thủng màng tế bào được bảo vệ; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b13 | 01:40.1–01:47.6 (7.5s) | L156 | Toàn bộ cơ thể Ếch Gỗ Bắc Cực cứng đờ lại như một viên sỏi đá. Đôi mắt đục ngầu như ngọc bích, các chi bất động, làn da phủ kín một lớp băng tuyết dày! |  | Cận cảnh chú Ếch Gỗ Bắc Cực hoạt hình da nâu vàng có vệt đen qua mắt như mặt nạ Zorro, đeo khăn quàng cổ đỏ thắm chống rét, người phủ lớp sương tuyết lấp lánh đã biến thành một bức tượng băng hoàn hảo, cứng ngắc không hề nhúc nhích, ánh sáng phản chiếu lấp lánh trên lưng; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b14 | 01:47.6–01:52.8 (5.1s) | L157 | Trái tim của anh chàng từ từ chậm lại: 60 nhịp một phút... 30 nhịp một phút... mười nhịp một phút... rồi dừng hẳn |  | Biểu đồ điện tâm đồ hiển thị đường sóng nhịp tim tụt dần và phẳng lì thành một đường thẳng tắp không còn dao động; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b15 | 01:52.8–02:00.3 (7.5s) | L158 | lại! Phổi ngừng thở! Dòng máu ngừng chảy! Não bộ ngừng phát sóng điện từ! Ở góc độ y học thông thường, chú ếch này đã chết lâm sàng hoàn toàn! |  | Màn hình theo dõi sự sống trong phòng chỉ huy báo tín hiệu phẳng lặng, không một dấu hiệu tuần hoàn; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b16 | 02:00.3–02:09.2 (9.0s) | L159 | Nhưng chính trạng thái chết giả thần kỳ này đã cứu sống anh chàng! Nhiệt độ cơ thể của Ếch Gỗ lúc này tụt xuống đúng -20°C, bằng chằn chặn với nhiệt độ của căn phòng băng! |  | Màn hình quét hồng ngoại của hệ thống an ninh quét qua vị trí của chú ếch: chú ếch hiện lên với màu xanh dương thẫm giống hệt như sàn đá xung quanh, hoàn toàn tàng hình; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b17 | 02:09.2–02:16.5 (7.3s) | L160 | Hệ thống máy quét tầm nhiệt coi khối băng hình chú ếch chỉ là một tảng nhũ đá rơi xuống từ trần nhà, và thản nhiên bỏ qua không kích hoạt súng laser! |  | Chùm tia laser cảnh báo quét qua lưng chú ếch băng rồi lướt đi nơi khác mà không hề phát ra tiếng còi báo động nào; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b18 | 02:16.5–02:25.6 (9.1s) | L161 | Một cơn gió lốc của hệ thống điều hòa thổi mạnh qua sàn nhà, làm khối băng chứa Ếch Gỗ trượt ro ro trên mặt sàn băng nhẵn thín, lăn thẳng về phía chân bàn điều khiển nhiệt độ! |  | Bức tượng băng của chú Ếch Gỗ Bắc Cực hoạt hình da nâu vàng có vệt đen qua mắt như mặt nạ Zorro, đeo khăn quàng cổ đỏ thắm chống rét, người phủ lớp sương tuyết lấp lánh trượt như một hòn bi trên mặt sàn băng trơn láng, dừng lại êm ái ngay dưới chân cột trụ điều khiển trung tâm; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b19 | 02:25.6–02:31.9 (6.3s) | L162 | Đã tiếp cận mục tiêu! Bây giờ là giai đoạn hai: nghệ thuật hồi sinh sau giấc ngủ đông dài 7 tháng ở vùng cực bắc! |  | chú Ếch Gỗ Bắc Cực hoạt hình da nâu vàng có vệt đen qua mắt như mặt nạ Zorro, đeo khăn quàng cổ đỏ thắm chống rét, người phủ lớp sương tuyết lấp lánh nằm yên dưới chân bàn điều khiển, một dòng nước ấm nhỏ giọt từ ống tản nhiệt phía trên khẽ rơi trúng đầu chú ếch; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b20 | 02:31.9–02:39.6 (7.7s) | L163 | Khi nhiệt độ môi trường nhích nhẹ lên trên mức đóng băng, các phân tử đường glucose bắt đầu hấp thụ nhiệt lượng. Lớp băng ngoại bào tan chảy dần dần! |  | Lớp băng phủ ngoài da chú ếch tan biến thành những giọt nước long lanh, các khớp chân bắt đầu mềm trở lại và co giãn linh hoạt; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b21 | 02:39.6–02:47.3 (7.7s) | L164 | Kỳ tích xuất hiện: quả tim tí hon của Ếch Gỗ tự động phát ra một xung điện sinh học bí ẩn và bắt đầu co bóp trở lại! Thình thịch... thình thịch... thình thịch! |  | Cận cảnh trái tim nhỏ bé màu đỏ hồng của chú ếch đập nhịp nhàng trở lại, bơm dòng nước màu ấm áp đi khắp cơ thể; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b22 | 02:47.3–02:52.2 (5.0s) | L165 | Dòng máu ấm rã đông các tế bào thần kinh, đánh thức não bộ chỉ trong vòng vài phút ngắn ngủi! |  | Các xung điện thần kinh màu xanh lục chạy dọc tủy sống của chú ếch, đôi mắt chớp chớp trở lại ánh nhìn thông minh; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b23 | 02:52.2–03:00.8 (8.5s) | L166 | Các nhà khoa học ghi nhận: chỉ trong vòng chưa đầy một giờ đồng hồ sau khi tan băng, ếch gỗ có thể hồi phục toàn bộ chức năng sống và nhảy nhót như chưa từng bị đông cứng! |  | chú Ếch Gỗ Bắc Cực hoạt hình da nâu vàng có vệt đen qua mắt như mặt nạ Zorro, đeo khăn quàng cổ đỏ thắm chống rét, người phủ lớp sương tuyết lấp lánh chớp mắt một cái, chiếc mồm khẽ đớp lấy không khí, bốn chân bật mạnh một cú nhảy ngoạn mục lên bàn điều khiển; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b24 | 03:00.8–03:05.6 (4.8s) | L167 | Bẹp! Bàn chân có màng của Ếch Gỗ đạp trúng nút xả đông khẩn cấp màu đỏ! |  | Bàn chân của chú Ếch Gỗ Bắc Cực hoạt hình da nâu vàng có vệt đen qua mắt như mặt nạ Zorro, đeo khăn quàng cổ đỏ thắm chống rét, người phủ lớp sương tuyết lấp lánh ấn mạnh xuống nút bấm khẩn cấp to đùng, còi báo động nhiệt độ vang lên một hồi ngắn báo hiệu chu trình sưởi ấm; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b25 | 03:05.6–03:11.9 (6.3s) | L168 | Hơi nóng bắt đầu ùa ra từ các họng thông gió, các cột băng khổng lồ tan chảy ầm ầm thành những dòng suối nhỏ chảy dọc sàn đá! |  | Các bức tường băng tan rã rào rào, hệ thống súng laser tầm nhiệt bị chập điện tóe lửa do ngập nước, căn hầm trở lại nhiệt độ bình thường; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b26 | 03:11.9–03:16.9 (5.0s) | L169 | Cửa Ải 3 chính thức bị bẻ khóa! Biểu tượng hoa tuyết trên bảng điều khiển {BOARD} vụt sáng chuyển sang màu xanh ngọc bích! |  | bản đồ hologram 3D của Pháo Đài Tự Nhiên nổi lơ lửng trong không khí, hiển thị 7 cửa ải an ninh phát sáng đỏ và thanh tiến độ phá khóa màu xanh ngọc (không có chữ, không có số) cập nhật kết quả: thanh tiến độ phá khóa nhảy lên nấc thứ ba, ánh sáng xanh ngọc bích tỏa sáng rực rỡ khắp phòng chỉ huy; anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm vỗ tay khen ngợi. |
| b27 | 03:16.9–03:24.3 (7.3s) | L170 | Ếch Gỗ Bắc Cực đứng trên bàn điều khiển, khẽ hất chiếc khăn quàng len đỏ ra sau vai, nở một nụ cười đắc thắng về phía ống kính camera. |  | chú Ếch Gỗ Bắc Cực hoạt hình da nâu vàng có vệt đen qua mắt như mặt nạ Zorro, đeo khăn quàng cổ đỏ thắm chống rét, người phủ lớp sương tuyết lấp lánh tạo dáng ngầu như một điệp viên sau khi hoàn thành nhiệm vụ bất khả thi, vẫy tay chào các đồng đội qua màn hình liên lạc. |
| b28 | 03:24.3–03:30.9 (6.7s) | L171 | Nhưng tiếng vỗ tay vừa dứt thì cánh cửa tiếp theo mở toang ra một căn phòng kỳ dị chưa từng thấy: Mê Cung Bẫy Giải Mã của Cửa Ải 4! |  | Căn phòng tiếp theo hiện ra với hàng trăm tấm gương phản chiếu, những chiếc hộp gỗ cơ học gắn ròng rọc phức tạp và những sợi dây bẫy giăng chằng chịt trong không gian; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b29 | 03:30.9–03:37.2 (6.3s) | L172 | Đây không phải là bài toán về cơ bắp hay tốc độ. Đây là cuộc đấu trí cân não với các bẫy cơ học liên hoàn và mê cung gương quang học! |  | anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm nhìn sang chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép đang đậu trên lưng ghế, tay đã cầm sẵn chiếc kẹp kim loại siêu nhỏ; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b30 | 03:37.2–03:41.8 (4.6s) | L173 | Đã đến lúc cho các kỹ sư của pháo đài biết thế nào là chỉ số thông minh của loài quạ! |  | chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép bay vút lên trần nhà, lượn một vòng điệu nghệ chuẩn bị cho màn phá khóa kinh điển; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b31 | 03:41.8–03:48.6 (6.8s) | L174 | Nghiên cứu của giáo sư Storey tại đại học Carleton đã chứng minh: ếch gỗ Bắc Cực là bậc thầy số một thế giới về công nghệ bảo quản lạnh sinh |  | Hình ảnh phòng thí nghiệm hiện đại với các ống nghiệm bảo quản mẫu sinh học ở nhiệt độ âm hai mươi độ C; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b32 | 03:48.6–03:56.9 (8.3s) | L175 | học! Khi dịch cơ thể đông cứng, các tế bào của ếch gỗ mất đi 40 phần trăm thể tích nước nhưng không hề bị vỡ màng tế bào nhờ lớp đệm phân tử glucose siêu đậm đặc! |  | Kính hiển vi 3D mô phỏng sự co giãn đàn hồi hoàn hảo của màng tế bào ếch dưới áp lực băng giá; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b33 | 03:56.9–04:04.0 (7.1s) | L176 | Chất urea tái hấp thu từ nước tiểu được giữ lại trong cơ bắp, đóng vai trò như chiếc phanh hãm tốc độ đóng băng, ngăn các tinh thể đá phát triển quá |  | Các phân tử urea đan xen giữa các tinh thể đá, làm tròn các góc cạnh nhọn của đá để không đâm thủng mạch nước màu; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b34 | 04:04.0–04:12.4 (8.3s) | L177 | nhanh! Sau khi rã đông hoàn toàn, các tế bào của ếch gỗ lập tức kích hoạt chu trình thanh lọc lượng đường dư thừa, đưa nồng độ đường trong máu trở lại mức bình thường! |  | Đồ họa y tế mô phỏng gan ếch gỗ thu hồi đường glucose và đưa lượng urea trở về bàng quang một cách nhịp nhàng; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b35 | 04:12.4–04:19.5 (7.1s) | L178 | Khả năng điều hòa trao đổi chất linh hoạt này khiến các nhà khoa học vũ trụ phải trầm trồ nghiên cứu để ứng dụng cho các chuyến bay liên hành tinh! |  | Hình ảnh phi hành gia tương lai bước vào buồng ngủ đông mô phỏng theo cơ chế của chú ếch gỗ Bắc Cực; KHÔNG có anh Chỉ Huy trong cảnh này. |

### scene06 · CÂU ĐỐ 8 BƯỚC, BẪY NƯỚC & QUẠ ĐEN · 248.6s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.8 (8.8s) | L179 | Cửa Ải 4 không dùng áp suất gió, không dùng khí độc, cũng chẳng cần đến nhiệt độ băng giá. Đây là một mê cung cơ học được thiết kế để giam cầm những bộ não thông minh nhất! |  | Khung cảnh căn phòng Mê Cung Bẫy Giải Mã rộng lớn với các vách tường gương bóng loáng phản chiếu vô tận, ở giữa là một hệ thống ròng rọc, hộp gỗ khóa số và các ống thủy tinh phức tạp; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b02 | 00:08.8–00:17.6 (8.7s) | L180 | Ở trung tâm căn phòng là chiếc hộp điều khiển chính khóa chặt cánh cổng bước vào nửa sau pháo đài. Muốn mở được nó, kẻ đột nhập phải giải một chuỗi câu đố liên hoàn 8 bước cực kỳ hóc búa! | **8 BƯỚC** · Câu đố liên hoàn · R/400 · [0.5, 0.6] | Cận cảnh một cỗ máy cơ học cổ điển tinh xảo bằng đồng và gỗ: có các ngăn kéo bí mật bị khóa xích, các rãnh trượt bi kim loại và một chiếc ống thủy tinh dài chứa chiếc chìa khóa nổi; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b03 | 00:17.6–00:25.0 (7.4s) | L181 | Các kỹ sư an ninh của pháo đài từng tự hào tuyên bố: nếu không có sách hướng dẫn sử dụng, một người trưởng thành cũng phải mất ít nhất hai ngày mới mò ra được quy luật! |  | Hình vẽ bản thiết kế kỹ thuật của cỗ máy câu đố với các mũi tên chỉ hướng chuyển động của bánh răng và đòn bẩy cơ học phức tạp (không chữ, không số); KHÔNG có anh Chỉ Huy trong cảnh này. |
| b04 | 00:25.0–00:31.8 (6.8s) | L182 | Bất kỳ một sai sót nào trong trình tự các bước cũng sẽ kích hoạt cơ chế khóa vĩnh viễn, chôn vùi chiếc chìa khóa xuống đáy hầm sâu! |  | Một chiếc bẫy lồng sắt treo lơ lửng trên trần nhà nhấp nháy đèn cảnh báo đỏ rực sẵn sàng sập xuống; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b05 | 00:31.8–00:38.3 (6.5s) | L183 | Nhưng họ đã quên mất một điều: loài người không phải là sinh vật duy nhất biết tư duy logic trên hành tinh này! |  | chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép sà xuống đậu trên đỉnh cỗ máy, nghiêng đầu nhìn ngắm toàn bộ hệ thống bánh răng với ánh mắt tinh quái, mỏ kẹp chiếc kìm kim loại nhỏ; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b06 | 00:38.3–00:49.5 (11.2s) | L184 | Đặc vụ Quạ Đen chỉ mất đúng 30 giây để quan sát. Não bộ của loài quạ sở hữu mật độ tế bào thần kinh dày đặc ngang ngửa với các loài linh trưởng cấp cao, cho phép chúng hiểu rõ quy luật nhân quả trong chớp mắt! |  | Đồ họa so sánh bộ não của quạ đen và não khỉ đột: các vùng xử lý logic và công cụ của quạ phát sáng rực rỡ các mạng lưới nơ-ron thần kinh màu vàng ánh kim; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b07 | 00:49.5–01:00.6 (11.1s) | L185 | Nghiên cứu khoa học kinh điển của các nhà động vật học tại đại học Oxford và Cambridge đã chứng minh: quạ có thể tự mình giải câu đố cơ học 8 bước liên hoàn ngay trong lần thử đầu tiên mà không cần bất kỳ sự huấn luyện |  | Tranh minh họa thí nghiệm khoa học nổi tiếng: một chú quạ đen thông minh đang dùng mỏ gắp từng món dụng cụ để mở lần lượt tám ngăn hộp gỗ theo thứ tự chuẩn xác; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b08 | 01:00.6–01:09.2 (8.6s) | L186 | nào! Chúng hiểu rõ khái niệm về công cụ gián tiếp: dùng công cụ A để lấy công cụ B, rồi dùng công cụ B để lấy mục tiêu C một cách hoàn toàn tự nhiên! |  | Sơ đồ các bước tư duy liên kết hình chuỗi xích màu xanh lục trong tâm trí chú quạ thông minh; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b09 | 01:09.2–01:14.7 (5.5s) | L187 | Bước một: Quạ Đen nhặt một que gỗ ngắn trên sàn, thò mỏ khều chiếc que sắt dài hơn bị giấu sâu trong khe đá hẹp! |  | chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép dùng mỏ cắp chiếc que ngắn, khéo léo luồn vào khe nứt trên vách tường đá, kéo ra một chiếc que thép dài hơn; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b10 | 01:14.7–01:22.6 (7.9s) | L188 | Bước hai: chiếc que thép dài quá thẳng không móc được chốt? Không thành vấn đề! Quạ Đen kẹp đầu que vào kẽ nứt sàn đá, dùng mỏ uốn cong nó thành một chiếc lưỡi câu hoàn hảo! |  | Cận cảnh chiếc mỏ đen bóng của chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép bẻ cong đầu sợi dây thép thành hình móc câu chuẩn xác như một người thợ rèn điêu luyện; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b11 | 01:22.6–01:27.4 (4.8s) | L189 | Bước ba: anh chàng dùng chiếc móc câu vừa chế tạo câu một túi sỏi đá nặng trĩu đặt trên giá cao xuống sàn! |  | chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép ngậm móc câu kéo đứt sợi dây treo, thả rơi chiếc túi chứa các viên sỏi đặc xuống đất một cách nhẹ nhàng; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b12 | 01:27.4–01:33.2 (5.8s) | L190 | Bước bốn: tháo túi lấy sỏi, bay vút tới bên cạnh chiếc ống thủy tinh hẹp chứa chiếc chìa khóa nổi trên mặt nước! |  | chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép đậu trên miệng ống thủy tinh cao và hẹp, bên dưới đáy ống là chiếc chìa khóa đồng thau đang nổi bập bềnh ngoài tầm với của mỏ chim; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b13 | 01:33.2–01:41.0 (7.8s) | L191 | Đây là bài kiểm tra trí tuệ ngụ ngôn Ê-dốp trứ danh trong giới khoa học sinh học! Quạ Đen có hiểu được quy luật dâng mực nước theo định luật thể tích hay không? |  | Trên bàn có hai đĩa đồ vật: một đĩa chứa các mẩu xốp nhựa nhẹ nổi trên mặt nước, một đĩa chứa những viên sỏi đá đặc chìm sâu; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b14 | 01:41.0–01:48.0 (7.0s) | L192 | Nếu thả xốp vào, xốp sẽ nổi lềnh bềnh và không làm dâng nước. Chỉ có sỏi đá đặc mới chiếm chỗ chất lỏng và đẩy chiếc chìa khóa lên miệng ống! |  | Mô hình so sánh: thả xốp thì mực nước không đổi, thả sỏi đặc thì mực nước dâng cao theo định luật Ac-si-mét; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b15 | 01:48.0–01:53.4 (5.4s) | L193 | Quạ Đen thậm chí còn không thèm liếc nhìn đĩa xốp nhựa! Anh chàng chỉ chọn đúng những viên sỏi đá đặc màu xám nặng |  | chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép dùng mỏ gắp từng viên sỏi đá đặc, thả từng viên từng viên một vào trong ống thủy tinh: tõm... tõm... tõm! KHÔNG có anh Chỉ Huy trong cảnh này. |
| b16 | 01:53.4–02:01.6 (8.2s) | L194 | nhất! Khả năng ước lượng thể tích chất lỏng của quạ chuẩn xác đến mức kinh ngạc, anh chàng dừng thả sỏi ngay khi chiếc chìa khóa vừa chạm miệng ống! |  | Mặt nước dâng lên vừa khít mép bình, chiếc chìa khóa nổi lên trong tầm với hoàn hảo của mỏ quạ; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b17 | 02:01.6–02:07.4 (5.8s) | L195 | Mực nước dâng lên! Chiếc chìa khóa đồng từ từ nổi lên sát miệng ống! Quạ Đen chỉ việc thò mỏ cắp lấy chìa khóa một cách ngon ơ! |  | Chiếc chìa khóa trồi lên sát miệng bình thủy tinh, chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép ngậm lấy chiếc chìa khóa đồng, nháy mắt tinh nghịch về phía ống kính quan sát hoạt hình vui nhộn; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b18 | 02:07.4–02:10.8 (3.4s) | L196 | Bước năm: cắm chìa khóa vào ổ khóa số một, mở ngăn kéo chứa quả tạ sắt! |  | chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép tra chìa khóa vào ổ, vặn một vòng kêu tách, ngăn kéo tự động trượt ra để lộ một quả tạ sắt tròn; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b19 | 02:10.8–02:15.7 (4.9s) | L197 | Bước sáu và bước bảy: đẩy quả tạ sắt lăn qua máng trượt nghiêng, đè sập chiếc bẫy kẹp và nhả chốt hãm của ròng rọc trung tâm! |  | Quả tạ sắt lăn rầm rập trên rãnh trượt kim loại, đè bẹp chiếc bẫy kẹp nguy hiểm và làm bật tung chiếc then cài cửa chính; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b20 | 02:15.7–02:23.2 (7.6s) | L198 | Và bước tám cuối cùng: Quạ Đen bay lên ấn mạnh cần gạt tổng lực! Răng rắc... ầm! Cánh cổng sắt nặng hai tấn từ từ cuốn lên trần nhà! |  | Hệ thống ròng rọc khổng lồ chuyển động kéo cánh cổng sắt lớn mở toang, ánh sáng từ nửa sau pháo đài rọi vào mê cung; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b21 | 02:23.2–02:31.5 (8.2s) | L199 | Nhưng ngay khi cổng vừa mở, hệ thống camera nhận diện khuôn mặt của mê cung gương bắt đầu nhấp nháy đèn đỏ, cố gắng quét chân dung kẻ đột nhập để phát lệnh truy nã toàn |  | Các camera giám sát tự động gắn trên các vách gương xoay nòng lia về phía chú quạ đen, các tia quét nhận dạng khuôn mặt màu đỏ quét qua quét lại; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b22 | 02:31.5–02:38.2 (6.7s) | L200 | cầu! Loài quạ có khả năng nhận diện và ghi nhớ khuôn mặt con người suốt hơn 5 năm trời, và chúng cũng thừa biết camera hoạt động theo nguyên lý | **5 NĂM** · Trí nhớ nhận diện · L/430 · [0.4, 0.5] | chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép nhìn thẳng vào ống kính camera với vẻ mặt đầy thách thức, không một chút bối rối sợ hãi; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b23 | 02:38.2–02:44.8 (6.7s) | L201 | nào! Quạ Đen thò mỏ kẹp lấy một tấm gương nhỏ trên sàn, xoay ngược góc phản chiếu ánh sáng đèn pha chiếu thẳng vào ống kính camera giám sát! |  | chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép dùng mỏ nghiêng tấm gương kính, hắt luồng ánh sáng chói lòa làm mù hoàn toàn cảm biến quang học của ống kính quan sát hoạt hình vui nhộn; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b24 | 02:44.8–02:51.7 (6.9s) | L202 | Chưa hết, anh chàng còn dùng mỏ cạy tung tấm ốp bảo vệ phía sau, làm ngắn mạch dây nguồn điều khiển khiến toàn bộ hệ thống camera nổ lách tách! |  | Dây cáp điện bên trong camera tóe lửa chập mạch, tia lửa điện bắn ra rực rỡ trong bóng tối; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b25 | 02:51.7–02:58.7 (7.0s) | L203 | Xèo xèo! Cảm biến camera bị lóa sáng chập mạch bốc khói đen! Toàn bộ hệ thống mê cung gương sụp đổ tín hiệu hoàn toàn! |  | Màn hình điều khiển camera của pháo đài nhiễu loạn thành các vạch sọc trắng đen vô định, không thể ghi lại bất kỳ hình ảnh nào của biệt đội; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b26 | 02:58.7–03:06.2 (7.6s) | L204 | Biểu tượng câu đố cơ học trên {BOARD} chuyển sang màu xanh ngọc bích rực rỡ! Bốn trên 7 cửa ải đã bị biệt đội đặc nhiệm chinh phục thành công! |  | bản đồ hologram 3D của Pháo Đài Tự Nhiên nổi lơ lửng trong không khí, hiển thị 7 cửa ải an ninh phát sáng đỏ và thanh tiến độ phá khóa màu xanh ngọc (không có chữ, không có số) cập nhật tín hiệu: thanh tiến độ phá khóa đã vượt qua mốc một nửa, ánh sáng xanh ngọc bích chiếm lĩnh bản đồ pháo đài; anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm gật đầu tán thưởng. |
| b27 | 03:06.2–03:13.2 (6.9s) | L205 | Quạ Đen bay sà xuống vai tượng đá, mỏ huýt sáo một điệu nhạc điệp viên vui nhộn, không quên vẫy cánh chào khán giả theo dõi qua màn hình. |  | chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép đậu trên vai bức tượng đá cẩm thạch, đầu nghiêng ngả điệu đà, vẻ mặt tự mãn của một bậc thầy trí tuệ vừa phá giải cỗ máy thế kỷ. |
| b28 | 03:13.2–03:19.8 (6.7s) | L206 | Nhưng từ sâu bên trong đường dẫn tới Cửa Ải 5, tiếng nước chảy xiết ầm ầm như thác đổ bắt đầu vọng lại, làm rung chuyển cả sàn đá hoa |  | Nước ngầm bắt đầu rỉ qua các khe nứt sàn đá, tiếng gầm gào của dòng nước áp lực cao vang lên đe dọa từ sâu trong lòng pháo đài; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b29 | 03:19.8–03:28.8 (9.0s) | L207 | cương. Hào nước ngầm áp lực cao của pháo đài đã mở van xả lũ! Lần này, chỉ có một bá chủ thực sự của đại dương mới có thể đối đầu với cơn thịnh nộ của thủy triều! |  | Cận cảnh anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm nhìn vào bể nước dã chiến: "Đặc vụ Cá Voi Sát Thủ, căn hầm ngập nước đã chuẩn bị xong. Cho chúng thấy thế nào là sức mạnh của hải quân bầy đàn!" |
| b30 | 03:28.8–03:33.6 (4.7s) | L208 | Đại ca biển cả chuẩn bị xuất chiêu với những đợt sóng thần áp lực kinh hoàng! |  | chú Cá Voi Sát Thủ hoạt hình thân đen bóng bụng trắng tinh, vây lưng cao vút cắm ăng-ten định vị sonar nhỏ xíu, miệng cười nhếch mép kiểu trùm mafia biển cả nhô vây lưng lên khỏi mặt nước, ánh mắt rực lửa chuẩn bị xé toạc cánh cửa van đập nước ngầm. |
| b31 | 03:33.6–03:42.8 (9.2s) | L209 | Trí tuệ của loài quạ đã vượt xa những gì con người từng tưởng tượng về thế giới loài chim! Chúng có thể nhớ mặt từng kẻ thù và truyền lại mối đe dọa này cho các thế hệ con cháu suốt nhiều năm trời! |  | Hình ảnh một đàn quạ đen bay lượn trên ngọn cây, cùng phát tín hiệu cảnh báo khi nhìn thấy bóng dáng kẻ thù xuất hiện; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b32 | 03:42.8–03:50.0 (7.2s) | L210 | Khi đối đầu với mê cung gương, quạ đen hoàn toàn hiểu rằng hình ảnh trong gương chỉ là sự phản chiếu quang học chứ không phải là một con quạ đối thủ! |  | chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép nghiêng đầu nhìn vào gương, dùng mỏ chạm nhẹ vào mặt kính rồi quay lưng lại tìm công tắc thật sự; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b33 | 03:50.0–03:56.1 (6.1s) | L211 | Khả năng tư duy trừu tượng này cho phép chúng giải quyết các bài toán hóc búa một cách bình tĩnh, không hề mắc bẫy tâm lý của các kỹ sư |  | chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép nháy mắt tinh nghịch, ngậm chiếc kìm cắt đứt sợi dây bẫy cuối cùng; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b34 | 03:56.1–04:01.9 (5.9s) | L212 | pháo đài! Mỗi một bước đi trong mê cung giải đố của Quạ Đen đều được tính toán chuẩn xác như một đại kiện tướng cờ vua quốc tế! |  | Bàn cờ vua bằng đá với quân cờ hình chú quạ đen chiếu tướng vua cờ cơ học của pháo đài; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b35 | 04:01.9–04:08.6 (6.6s) | L213 | Anh chàng không chỉ mở được cổng mà còn thu gom luôn một mẩu dây đồng sáng loáng nhét vào túi áo làm kỷ niệm cho bộ sưu tập cá nhân! |  | chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép giấu mẩu dây đồng vào dưới cánh, nháy mắt tinh quái trước khi sải cánh bay tiếp; KHÔNG có anh Chỉ Huy trong cảnh này. |

### scene07 · LẠC ĐÀ NHAI XƯƠNG RỒNG & BÁCH THANH CẮM GAI NHẦM CHÌA KHÓA · 248.5s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:10.0 (10.0s) | L214 | Nếu bạn nghĩ một biệt đội đặc nhiệm gồm mười loài động vật hoang dã có thể phối hợp ăn ý như quân đội hoàng gia... thì bạn đã đánh giá quá cao tính kỷ luật của giới tự nhiên rồi! |  | Căn phòng chỉ huy của anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm, bàn điều khiển bừa bộn những vỏ chai nước tăng lực, lông chim bay lả tả và màn hình liên lạc đang nhấp nháy đèn báo lỗi âm thanh; anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm đỡ trán bất lực. |
| b02 | 00:10.0–00:17.5 (7.5s) | L215 | Ngay giữa thời khắc căng thẳng chuẩn bị bước vào trận chiến đường thủy của Cửa Ải 5, một chuỗi âm thanh rùng rợn bỗng nhiên nổ ra trên kênh liên lạc tần số cao. |  | Chiếc loa truyền thanh rung bần bật, phát ra những tiếng rôm rốp rào rạo chói tai như tiếng một tảng đá đang bị máy nghiền xi măng nghiền nát; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b03 | 00:17.5–00:24.8 (7.3s) | L216 | Rộp! Rộp! Xoàn xoạt! Rộp! Tiếng động kinh hoàng đến mức Chim Cắt Lớn giật thót mình suýt ngã khỏi thành đá, còn Quạ Đen thì vội vàng ôm đầu tưởng pháo đài sập! |  | chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng trượt chân bám chặt móng vào gờ đá, chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép chui tọt vào trong một chiếc mũ sắt thế giới tự nhiên trốn; KHÔNG có anh C |
| b04 | 00:24.8–00:30.7 (5.8s) | L217 | "Báo động đỏ! Kẻ địch đang dùng súng máy nghiền nát công sự của chúng ta! Yêu cầu hỗ trợ khẩn cấp!" |  | Chim Cắt hét to vào bộ đàm trong tư thế sẵn sàng kích hoạt ba lô phản lực để bay thoát thân; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b05 | 00:30.7–00:38.7 (8.1s) | L218 | Chỉ Huy Mật Vụ vội vàng điều chỉnh tần số thu âm, phóng to nguồn phát tín hiệu trên radar định vị vệ tinh. Và hình ảnh hiện lên trên màn hình chính khiến tất cả ngã ngửa! |  | Màn hình chính phóng to cận cảnh khuôn mặt của chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao: anh chàng đang đứng ung dung tự tại, hai hàm răng to tướng nhai tóp tép một nhánh xương rồng sa mạc đầy gai nhọn hoắt ngay sát mic thu âm; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b06 | 00:38.7–00:46.0 (7.2s) | L219 | Chiếc micro dã chiến gắn trên cổ áo của Lạc Đà Sa Mạc đang thu trọn từng tiếng nhai giòn rụm của những chiếc gai xương rồng dài 5cm bị nghiền nát thành bã! |  | Cận cảnh miệng của chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao với các mấu sừng hình nón cứng như đá bên trong má, nghiền nát những chiếc gai nhọn sắc bén một cách ngon lành như nhai bim bim; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b07 | 00:46.0–00:54.6 (8.7s) | L220 | Bên trong vòm miệng và má của lạc đà có hàng trăm mấu thịt hình nón bằng chất sừng cứng ngắc, hướng thẳng vào phía cuống họng giúp bẻ gãy mọi mũi gai nhọn mà không làm xước niêm mạc miệng! |  | Hình vẽ giải phẫu vòm miệng lạc đà với các gai sừng nhú papillae xếp lớp như những chiếc khiên che chở bảo vệ mô mềm; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b08 | 00:54.6–01:03.1 (8.5s) | L221 | "Đặc vụ Lạc Đà! Cậu có biết chiếc micro đó có giá bằng cả năm tiền trợ cấp đi lại của cậu không hả? Tắt mic ngay trước khi tôi biến cậu thành chiếc thảm trải sàn!" |  | Cận cảnh anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm đập mạnh tay xuống bàn làm chiếc bút nhảy tưng lên, mắt tóe lửa giận dữ; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b09 | 01:03.1–01:11.5 (8.4s) | L222 | Dạ... cháu xin lỗi Chỉ Huy! Tại nhai xương rồng đỡ khát nước quá nên cháu quên mất là mic vẫn đang bật ạ! Cháu xin hứa nhai khẽ lại ạ! |  | chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao chớp chớp hàng mi dày rợp bóng, nở nụ cười hiền lành ngơ ngác, thè chiếc lưỡi dài liếm mép giấu nhánh xương rồng ra sau lưng; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b10 | 01:11.5–01:18.8 (7.4s) | L223 | Xương rồng này ngọt lắm sếp ơi, có nhiều nước chuyển hóa giúp tế bào máu oval của cháu căng tràn sức sống luôn ạ! |  | chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao thò đầu vào ống kính camera nháy mắt tinh nghịch làm cả phòng chỉ huy phì cười; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b11 | 01:18.8–01:26.9 (8.1s) | L224 | Cơn giận của Chỉ Huy còn chưa kịp hạ nhiệt thì tai họa thứ hai ập đến từ vị trí cảnh giới trên cây cổ thụ ngoài sân pháo đài. Lần này là từ Đặc vụ Chim Bách Thanh! |  | Khung cảnh ban đêm ngoài sân pháo đài, một cây gai bồ kết khổng lồ với những chiếc gai nhọn hoắt cắm tua tủa, chú Chim Bách Thanh hoạt hình lông xám trắng có dải lông đen vắt ngang mắt như dải băng cướp biển, mỏ có móc câu sắc nhọn, chân cầm một nhánh gai nhọn công nghệ đang đậu trên cành cao đảo mắt nhìn quanh; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b12 | 01:26.9–01:37.1 (10.1s) | L225 | Bách Thanh có một bản năng nghề nghiệp ăn sâu vào máu: hễ nhìn thấy bất kỳ vật thể nào có giá trị hoặc con mồi nào, anh chàng đều phải mang đi cắm chặt lên một chiếc gai nhọn để cất giữ làm kho lương thực dự trữ! |  | Cành cây gai của bách thanh cắm đầy những chiến lợi phẩm kỳ dị: một mẩu dây đồng, một chiếc cúc áo kim loại, một con thằn lằn khô và... một chiếc thẻ từ màu đỏ phát sáng; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b13 | 01:37.1–01:44.5 (7.5s) | L226 | Và bi kịch là chiếc thẻ từ màu đỏ đó chính là chiếc chìa khóa dự phòng duy nhất của Tổng Cục Trưởng Mật Vụ để kích hoạt cửa thoát hiểm khẩn cấp! |  | Cận cảnh chiếc thẻ từ dập nổi biểu tượng điệp viên màu bạc bị một chiếc gai nhọn đâm xuyên thủng qua góc thẻ, đung đưa trong gió đêm lạnh lẽo; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b14 | 01:44.5–01:56.3 (11.8s) | L227 | Báo cáo Chỉ Huy: tôi vừa phát hiện một vật thể hình chữ nhật có nguy cơ rơi vào tay kẻ địch! Tôi đã thực hiện biện pháp nghiệp vụ tiêu chuẩn: xiên nó lên chiếc gai cao 10 mét để bảo quản an toàn suốt 3 ngày tới! | **3 NGÀY** · Bản năng cắm gai · L/420 · [0.4, 0.5] | chú Chim Bách Thanh hoạt hình lông xám trắng có dải lông đen vắt ngang mắt như dải băng cướp biển, mỏ có móc câu sắc nhọn, chân cầm một nhánh gai nhọn công nghệ tự hào ưỡn ngực báo cáo qua bộ đàm, chiếc mỏ khoằm sắc như dao găm vỗ vỗ vào chiếc thẻ từ đung đưa trên gai; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b15 | 01:56.3–02:04.6 (8.3s) | L228 | Đây là kỹ thuật lưu trữ an toàn cấp độ năm sao của dòng họ nhà tôi, bảo đảm chim ưng hay cáo hoang cũng không thể nào lấy trộm được! |  | chú Chim Bách Thanh hoạt hình lông xám trắng có dải lông đen vắt ngang mắt như dải băng cướp biển, mỏ có móc câu sắc nhọn, chân cầm một nhánh gai nhọn công nghệ khoanh hai cánh trước ngực vẻ mặt cực kỳ tự mãn với chiến tích bảo vệ tài sản; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b16 | 02:04.6–02:12.1 (7.5s) | L229 | "Bách Thanh ơi là Bách Thanh! Đó là chiếc thẻ từ mở cửa thoát hiểm của cả đội đấy! Cậu xiên thủng nó thế kia thì lát nữa chúng ta thoát bằng niềm tin à?" |  | anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm ngửa mặt lên trần nhà than trời, hai cánh ôm lấy đầu, chiếc kính râm suýt rơi xuống sàn; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b17 | 02:12.1–02:19.7 (7.6s) | L230 | Chưa hết, thảm kịch hậu trường thứ ba lại xuất hiện ngay dưới chân bàn làm việc của phòng tác chiến ngầm. Lực lượng Kiến Cắt Lá vừa hoàn thành một chiến dịch bất ngờ! |  | Dưới chân bàn, một hàng dài hàng ngàn chú kiến cắt lá đang hối hả diễu hành, vác trên lưng những mảnh vải màu đen tuyền cắt tỉa cực kỳ vuông vắn; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b18 | 02:19.7–02:30.4 (10.7s) | L231 | Chim Cắt Lớn vừa bay về nghỉ chân, cúi xuống nhìn chiếc áo khoác điệp viên sang trọng của mình thì phát hiện: toàn bộ phần vạt áo và chiếc cà vạt lụa đắt tiền đã bị xẻo nham nhở không còn một manh giáp! |  | chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng nhìn xuống ngực áo rách tơi tả, chiếc cà vạt cụt lủn chỉ còn lại đúng cái củ ấu quanh cổ, miệng há hốc không thốt nên lời; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b19 | 02:30.4–02:40.8 (10.3s) | L232 | Báo cáo: đơn vị công binh chúng em phát hiện loại vải này có hàm lượng xen-lu-lô-zơ siêu cao, rất thích hợp để mang về hầm làm phân bón trồng vườn nấm cộng sinh ạ! Cảm ơn bác chim cắt đã tài trợ! |  | tiểu đội ba chú Kiến Cắt Lá hoạt hình màu nâu đỏ, đầu to mang hàm răng kim loại sáng loáng, đội mũ cối công binh màu xanh lá, đang vác những mảnh lá xanh như chiếc khiên chắn giơ cao chiếc kéo hàm răng thép bóng loáng, đồng thanh hô to vẻ mặt hớn hở của những người nông dân được mùa lá tốt; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b20 | 02:40.8–02:48.1 (7.4s) | L233 | Vườn nấm Leucocoprinus của chúng em được bón lụa thượng hạng này sẽ cho ra những mẻ nấm ngon nhất lịch sử 50 triệu năm nông nghiệp kiến! |  | Những chú kiến tí hon reo hò nhảy múa quanh mảnh vải lụa đen vừa cắt được; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b21 | 02:48.1–02:55.4 (7.3s) | L234 | Chim Cắt tức đến nỗi lông đầu dựng đứng, xòe cánh đòi lao vào mổ kiến, trong khi bầy kiến tí hon thì giơ hàm răng kim loại lên thách thức! |  | chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng xù lông quát tháo, đàn kiến xếp thành hình chiếc khiên lá chắn phòng thủ kiên cố, Quạ Đen đứng bên cạnh ôm bụng cười ngặt nghẽo; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b22 | 02:55.4–03:05.2 (9.8s) | L235 | "Trật tự ngay! Tất cả lập tức về vị trí chiến đấu trước khi tôi trừ toàn bộ lương thưởng của cả mười đứa!" Tiếng quát uy lực của Chỉ Huy Mật Vụ vang dội làm rung chuyển cả căn hầm. |  | anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm đứng phắt dậy, đập bàn cái rầm, chiếc máy tính bảng hologram phát ra một tiếng bíp đanh thép lập lại kỷ cương quân ngũ; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b23 | 03:05.2–03:12.6 (7.4s) | L236 | Toàn đội lập tức nín thở, đứng nghiêm như những bức tượng. Trò đùa chấm dứt khi màn hình theo dõi hào nước ngầm chuyển sang màu đỏ báo động lũ quét! |  | Màn hình trung tâm hiện lên hình ảnh một đập nước ngầm khổng lồ bằng bê tông cốt thép, dòng nước cuồn cuộn chảy xiết với áp suất hàng trăm át-mốt-phe sẵn sàng cuốn phăng mọi thứ; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b24 | 03:12.6–03:17.3 (4.7s) | L237 | Cửa Ải 5: Hào Nước Áp Lực Cao đang đón chờ. Bể nước dã chiến từ từ hạ xuống mép đập nước ngầm. |  | Khung cảnh cửa van xả lũ khổng lồ mở ra, dòng nước đen ngòm xoáy tròn dữ dội dưới đáy vực sâu; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b25 | 03:17.3–03:27.3 (10.0s) | L238 | Cá Voi Sát Thủ lặn sâu xuống làn nước lạnh, vây lưng nhô cao rẽ sóng, chiếc ăng-ten phát sóng sonar bắt đầu phát ra những tiếng nhấp chuột đanh gọn xuyên qua lòng đá. Trận hải chiến dưới lòng đất chính thức khai |  | chú Cá Voi Sát Thủ hoạt hình thân đen bóng bụng trắng tinh, vây lưng cao vút cắm ăng-ten định vị sonar nhỏ xíu, miệng cười nhếch mép kiểu trùm mafia biển cả lướt đi dũng mãnh trong làn nước ngầm cuồn cuộn, ánh mắt lóe lên sự thống trị tuyệt đối của kẻ săn mồi đỉnh cao đại dương. |
| b26 | 03:27.3–03:33.2 (5.9s) | L239 | hỏa! Đại ca biển cả chuẩn bị thể hiện sức mạnh của sóng âm sonar và cú quất đuôi sóng thần kinh hoàng! |  | Bọt nước cuộn trào quanh thân cá voi sát thủ khi anh chàng bắt đầu lặn xuống đáy sâu của con hào. |
| b27 | 03:33.2–03:39.0 (5.8s) | L240 | "Chỉ Huy ơi, nhai xương rồng này đã lắm, hay là Tổng Cục nhập khẩu cho cháu một tấn về để ở căng-tin dã chiến đi ạ!" |  | chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao thò đầu vào ống kính camera nhai nhồm nhoàm làm cả phòng điều khiển lại một phen ôm đầu; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b28 | 03:39.0–03:48.6 (9.6s) | L241 | Chim Bách Thanh thì nghiêm túc giải thích: "Xiên đồ lên gai là biện pháp bảo mật sinh học tối tân nhất! Không một tên trộm nào dám leo lên bụi gai bồ kết cao 10 mét để lấy trộm thẻ từ đâu ạ!" |  | chú Chim Bách Thanh hoạt hình lông xám trắng có dải lông đen vắt ngang mắt như dải băng cướp biển, mỏ có móc câu sắc nhọn, chân cầm một nhánh gai nhọn công nghệ đứng trên cành gai ưỡn ngực thuyết minh về triết lý bảo vệ tài sản của dòng họ mình; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b29 | 03:48.6–03:57.0 (8.4s) | L242 | Đại Đội Kiến Cắt Lá cũng gửi báo cáo phụ: "Mảnh vải áo lụa của bác chim cắt đã được đưa vào khoang ủ nấm số một, dự kiến sẽ thu hoạch được mẻ nấm siêu to khổng lồ vào sáng mai ạ!" |  | Những chú kiến cắt lá giơ hai càng ăn mừng rộn rã dưới lòng hầm ngầm; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b30 | 03:57.0–04:03.1 (6.1s) | L243 | Lạc Đà Sa Mạc hứa chắc nịch: "Lần sau cháu sẽ nhai cỏ khô êm dịu như nhung, bảo đảm không làm rè sóng bộ đàm của cả đội nữa đâu ạ!" |  | chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao thề thốt giơ một chân trước lên, miệng vẫn còn dính một cọng hoa xương rồng màu vàng rực rỡ; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b31 | 04:03.1–04:08.5 (5.4s) | L244 | Chỉ Huy Cú Mèo chỉ biết thở dài bật cười: "Thôi được rồi, nhớ giữ lời hứa đấy, anh chàng xe tăng sa mạc của tôi!" |  | anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm vỗ nhẹ vào vai lạc đà qua màn hình hologram, bầu không khí lại trở nên ấm cúng lạ thường; KHÔNG có anh Chỉ Huy trong cảnh này. |

### scene08 · CHIẾN HÀO THỦY QUÂN & CÁ VOI SÁT THỦ · 250.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.8 (9.8s) | L245 | Hào nước ngầm của Pháo Đài Tự Nhiên là một mê cung thủy lực tối tăm và hung hãn. Dòng nước đen kịt cuộn xoáy với vận tốc kinh hoàng, tạo nên những dòng xoáy ngầm có thể xé toạc bất kỳ tàu ngầm quân sự nào! |  | Dòng nước ngầm đen ngòm cuồn cuộn chảy xiết giữa hai vách đá dựng đứng sâu hun hút, các xoáy nước khổng lồ sủi bọt trắng xóa cuốn trôi những thanh gỗ vụn; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b02 | 00:09.8–00:18.2 (8.5s) | L246 | Độ sâu hơn 40m dưới mặt đất, ánh sáng mặt trời không bao giờ rọi tới được đây. Tầm nhìn quang học bằng không tròn trĩnh. Các camera thủy văn chỉ thu về một màu đen đặc quánh như |  | Màn hình quan sát dưới nước tối om, chỉ có những đốm bọt khí trắng xóa lướt qua ống kính máy quay; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b03 | 00:18.2–00:26.1 (7.8s) | L247 | mực! Nhưng trong bóng tối vĩnh cửu ấy, một bóng đen khổng lồ nặng 6 tấn mang hai màu đen trắng tương phản đang lướt đi nhẹ nhàng như một chiếc bóng ma đại dương! |  | chú Cá Voi Sát Thủ hoạt hình thân đen bóng bụng trắng tinh, vây lưng cao vút cắm ăng-ten định vị sonar nhỏ xíu, miệng cười nhếch mép kiểu trùm mafia biển cả bơi lướt đi uyển chuyển dưới làn nước sâu, thân hình thon dài hình thoi hoàn hảo rẽ nước không một tiếng động, vây lưng cao vút rẽ sóng kiêu hãnh; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b04 | 00:26.1–00:33.4 (7.3s) | L248 | Cơ thể thủy động lực học hình thoi giúp cá voi sát thủ giảm thiểu tối đa lực ma sát nhớt của nước, lướt đi êm ái như một quả ngư lôi tàng hình! |  | Bản vẽ kỹ thuật động lực học chất lưu: các dòng nước màu xanh lam lướt mượt mà quanh thân cá voi mà không tạo ra các xoáy cuộn cản trở; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b05 | 00:33.4–00:42.2 (8.8s) | L249 | Cản đường phía trước là một cánh cửa van ngăn lũ bằng thép tôi dày 0,5m, khóa chặt bởi ba chiếc chốt thủy lực áp suất cao. Không có chìa khóa, cũng không có chỗ để gài thuốc nổ. |  | Cận cảnh cánh cửa van đập nước bằng thép khổng lồ bị đóng chặt, trên mặt thép có những vết gỉ sét và các khớp nối thủy lực to bằng bắp đùi người lớn; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b06 | 00:42.2–00:50.1 (7.9s) | L250 | "Đặc vụ Cá Voi Sát Thủ, chúng ta không nhìn thấy điểm yếu của cánh cửa đập. Cậu phải tự tìm đường phá chốt trong bóng tối!" Giọng Chỉ Huy vang lên qua bộ đàm chống nước. |  | anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm theo dõi tín hiệu định vị phát ra từ chiếc ăng-ten gắn trên vây lưng cá voi, trên màn hình radar chỉ là một đốm sáng cô độc giữa lòng hào nước; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b07 | 00:50.1–00:56.3 (6.2s) | L251 | Cá Voi Sát Thủ không cần mắt để nhìn. Anh chàng sở hữu cỗ máy radar âm thanh sinh học tối tân nhất từng được tạo hóa tạo ra! |  | Cận cảnh phần trán vồ tròn trịa chứa đầy khối dầu sinh học của chú Cá Voi Sát Thủ hoạt hình thân đen bóng bụng trắng tinh, vây lưng cao vút cắm ăng-ten định vị sonar nhỏ xíu, miệng cười nhếch mép kiểu trùm mafia biển cả, nơi phát ra các xung âm thanh định vị siêu âm; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b08 | 00:56.3–01:05.2 (9.0s) | L252 | Khối mỡ dưa hấu đặc biệt trên trán cá voi hoạt động như một thấu kính quang học âm thanh, hội tụ các sóng siêu âm phân tán thành một chùm tia hẹp có độ phân giải siêu nét! |  | Hình cắt lớp 3D khối mỡ trán melon của cá voi: các sóng siêu âm màu vàng kim bị khúc xạ và hội tụ thành một luồng tia âm thanh định hướng chính xác cao; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b09 | 01:05.2–01:11.2 (6.0s) | L253 | Tách! Tách! Tách! Những chùm xung âm thanh định vị cực ngắn bắt đầu được bắn ra liên hồi từ khối dầu trán của cá voi sát thủ! |  | Các vòng sóng âm thanh siêu âm hình bán cầu màu xanh neon phát ra từ trán cá voi, lan tỏa cực nhanh qua làn nước tối đen; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b10 | 01:11.2–01:18.3 (7.1s) | L254 | Cường độ âm thanh tăng vọt lên mức cực đại: 225 dB! Đây là mức áp suất âm thanh dưới nước khủng khiếp nhất trong thế giới sinh vật! | **225 DB** · Xung Sonar đỉnh cao · R/390 · [0.5, 0.6] | Đồ họa sóng âm hiển thị cột đo áp lực âm thanh chạm đỉnh 225 dB, sóng xung kích âm thanh làm rung chuyển cả những hạt cát dưới đáy hào nước; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b11 | 01:18.3–01:26.5 (8.2s) | L255 | Các chùm sóng âm thanh 225 dB chạm vào cánh cửa đập bằng thép, dội ngược trở lại hàm dưới của cá voi và truyền thẳng vào tai trong với độ phân giải siêu |  | Các tia sóng dội ngược màu vàng kim thu về hàm dưới của chú Cá Voi Sát Thủ hoạt hình thân đen bóng bụng trắng tinh, vây lưng cao vút cắm ăng-ten định vị sonar nhỏ xíu, miệng cười nhếch mép kiểu trùm mafia biển cả, vẽ nên một bản đồ 3D chi tiết đến từng vết nứt vi mô trên cánh cửa thép trong tâm trí chú cá voi; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b12 | 01:26.5–01:34.5 (8.0s) | L256 | nét! Phát hiện mục tiêu! Điểm yếu nằm ở chiếc then cài thủy lực số hai bên dưới góc phải, nơi các bu-lông kim loại đã bị nước xói mòn tạo ra một kẽ hở đúng năm mi-li-mét! |  | Hình vẽ quét 3D của chiếc then cài bằng thép hiển thị một vệt nứt màu đỏ nhấp nháy ngay tại khớp xoay bản lề; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b13 | 01:34.5–01:41.5 (7.0s) | L257 | Âm thanh dội về chi tiết đến mức cá voi có thể phân biệt được độ dày của lớp rỉ sét và hướng ứng suất của từng chiếc đinh tán kim loại! |  | Màn hình mô phỏng não bộ cá voi xử lý tín hiệu âm thanh thành hình ảnh 3D chân thực như chụp cắt lớp vi tính; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b14 | 01:41.5–01:51.9 (10.5s) | L258 | Cá Voi Sát Thủ lùi lại 50 mét để lấy đà. Không cần súng phóng lựu, vũ khí của đại ca đại dương chính là kỹ thuật tạo sóng thần đồng bộ trứ danh từng khiến các nhà khoa học biển kinh ngạc! |  | chú Cá Voi Sát Thủ hoạt hình thân đen bóng bụng trắng tinh, vây lưng cao vút cắm ăng-ten định vị sonar nhỏ xíu, miệng cười nhếch mép kiểu trùm mafia biển cả bơi lùi lại vùng nước sâu, uốn mình uyển chuyển tích tụ một lượng động năng khổng lồ vào chiếc vây đuôi rộng hai mét; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b15 | 01:51.9–02:03.1 (11.1s) | L259 | Các nghiên cứu tại vùng biển Nam Cực ghi nhận: loài cá voi sát thủ có thể phối hợp bơi nước rút và quất mạnh chiếc vây đuôi để tạo nên những bức tường sóng thần cao hơn một mét rưỡi, thổi bay mục tiêu trên các tảng băng trôi! |  | Tranh minh họa tư liệu sinh học: đàn cá voi sát thủ bơi dàn hàng ngang quất đuôi đồng nhịp, tạo nên một con sóng khổng lồ cuộn trào dâng cao đánh sập mục tiêu; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b16 | 02:03.1–02:11.5 (8.4s) | L260 | Và hôm nay, trong không gian khép kín của hào ngầm, uy lực của con sóng này sẽ bị nén lại thành một cú đấm thủy lực có sức tàn phá gấp mười lần! |  | Sơ đồ động lực học: sóng nước bị hai vách đá thu hẹp lại, tạo thành một mũi nhọn áp lực nước cực lớn hướng thẳng vào then cài; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b17 | 02:11.5–02:18.6 (7.1s) | L261 | Tăng tốc! Cá Voi Sát Thủ phóng vút đi với vận tốc nước rút kinh hoàng: 56 km/h! Thân hình 6 tấn lao đi như một quả ngư lôi |  | chú Cá Voi Sát Thủ hoạt hình thân đen bóng bụng trắng tinh, vây lưng cao vút cắm ăng-ten định vị sonar nhỏ xíu, miệng cười nhếch mép kiểu trùm mafia biển cả rẽ nước lao đi như tên bắn, bọt nước sủi tung trắng xóa dọc hai bên thân mình đen bóng, ánh mắt rực lửa quyết chiến; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b18 | 02:18.6–02:25.8 (7.3s) | L262 | sống! Cách cánh cửa đập đúng 5 mét, anh chàng bất ngờ thực hiện một cú quay ngoắt 100 80° điệu nghệ, quất toàn bộ sức mạnh của cơ đuôi khổng lồ xuống mặt |  | chú Cá Voi Sát Thủ hoạt hình thân đen bóng bụng trắng tinh, vây lưng cao vút cắm ăng-ten định vị sonar nhỏ xíu, miệng cười nhếch mép kiểu trùm mafia biển cả xoay mình quật mạnh chiếc vây đuôi khổng lồ xuống nước với một lực hàng chục tấn, tạo ra một tiếng nổ ục kinh hoàng chấn động đáy hào; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b19 | 02:25.8–02:32.0 (6.2s) | L263 | nước! Ầm! Một bức tường sóng thủy lực cao vút bị ép chặt trong khe đá, lao thẳng vào chiếc then cài bị nứt với áp suất hàng trăm tấn trên một mét |  | Con sóng thủy lực cực mạnh đập thẳng vào khớp bản lề cánh cửa van thép, tạo nên một vụ nổ bọt khí chói lòa và tiếng kim loại gãy răng rắc; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b20 | 02:32.0–02:40.6 (8.5s) | L264 | vuông! Răng rắc... rầm! Chiếc then cài thủy lực bị uốn cong rồi gãy vụn! Cánh cửa van thép khổng lồ bị sức nước xô ngã ngửa ra sau, mở toang một lỗ hổng đường kính 3 mét! |  | Cánh cửa van thép bật tung khỏi bản lề, dòng nước ngầm ầm ầm đổ qua lỗ hổng thoát ra ngoài hạ lưu, mực nước trong hào ngầm bắt đầu rút xuống nhanh chóng; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b21 | 02:40.6–02:47.2 (6.7s) | L265 | Áp suất nước giải phóng tạo nên một cơn lốc xoáy nước xoáy tròn cuốn phăng toàn bộ rác rưởi và chướng ngại vật dưới lòng hào ngầm! |  | Dòng nước thoát nhanh tạo ra tiếng gầm vang dội khắp căn hầm ngầm của pháo đài; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b22 | 02:47.2–02:55.2 (7.9s) | L266 | Mực nước trong hào ngầm tụt dốc không phanh! Lòng hào trơ ra những phiến đá cuội trơn nhẵn, mở ra một lối đi bộ khô ráo cho toàn bộ biệt đội đặc nhiệm! |  | Nước rút hết để lộ đáy hào bằng phẳng, các bậc thang đá dẫn thẳng lên cửa tầng sáu của pháo đài xuất hiện rõ mồn một; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b23 | 02:55.2–03:03.1 (8.0s) | L267 | Cá Voi Sát Thủ nhô nửa thân mình lên mặt nước ở đoạn kênh thông thoáng, phun một cột nước trắng xóa lên trần hang, cất tiếng kêu éc éc đắc thắng qua micro! |  | chú Cá Voi Sát Thủ hoạt hình thân đen bóng bụng trắng tinh, vây lưng cao vút cắm ăng-ten định vị sonar nhỏ xíu, miệng cười nhếch mép kiểu trùm mafia biển cả ngửa cổ phun nước tạo thành một chiếc cầu vồng nhỏ dưới ánh đèn pin, vẫy hai vây ngực chào Chỉ Huy Mật Vụ đầy ngạo nghễ. |
| b24 | 03:03.1–03:11.9 (8.8s) | L268 | Biểu tượng sóng nước của Cửa Ải 5 trên {BOARD} nhấp nháy rồi chuyển sang màu xanh ngọc bích rực rỡ! Năm trên 7 cửa ải đã bị biệt đội hạ gục gọn gàng! |  | bản đồ hologram 3D của Pháo Đài Tự Nhiên nổi lơ lửng trong không khí, hiển thị 7 cửa ải an ninh phát sáng đỏ và thanh tiến độ phá khóa màu xanh ngọc (không có chữ, không có số) cập nhật tín hiệu: năm biểu tượng cửa ải đã chuyển sang màu xanh ngọc, thanh tiến độ phá khóa đã đạt hơn bảy mươi phần trăm; anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm đứng dậy vỗ tay tán thưởng. |
| b25 | 03:11.9–03:18.9 (7.0s) | L269 | Nhưng thử thách phía trước mới thực sự là bài kiểm tra độ cứng của hộp sọ và tinh thần đồng đội: Boong-ke Bê Tông Cốt Thép của Cửa Ải 6! |  | Trước mặt biệt đội là một bức tường thành khổng lồ xây bằng các khối đá granite đen dày hai mét, không có kẽ hở, không có cửa sổ, trơn lỳ như một khối đá nguyên khối; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b26 | 03:18.9–03:29.5 (10.6s) | L270 | Đạn pháo thông thường bắn vào đây chỉ để lại một vết xước nhỏ. Muốn phá vỡ bức tường này, chúng ta cần sự kết hợp giữa một chiếc búa khoan sinh học có lực gia tốc hàng ngàn G và một đại đội công binh tí hon có hàm răng thép! |  | anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm nhìn sang chú Chim Gõ Kiến hoạt hình mào lông đỏ rực dựng đứng, mỏ dài sắc nhọn như mũi khoan titan, đội mũ bảo hộ lao động màu vàng có gắn đèn pin thợ mỏ đang đội mũ bảo hộ vàng và tiểu đội ba chú Kiến Cắt Lá hoạt hình màu nâu đỏ, đầu to mang hàm răng kim loại sáng loáng, đội mũ cối công binh màu xanh lá, đang vác những mảnh lá xanh n |
| b27 | 03:29.5–03:34.4 (4.9s) | L271 | Cặp đôi búa khoan và máy đào đất chuẩn bị thực hiện màn công phá ngoạn mục chưa từng có! |  | chú Chim Gõ Kiến hoạt hình mào lông đỏ rực dựng đứng, mỏ dài sắc nhọn như mũi khoan titan, đội mũ bảo hộ lao động màu vàng có gắn đèn pin thợ mỏ và tiểu đội ba chú Kiến Cắt Lá hoạt hình màu nâu đỏ, đầu to mang hàm răng kim loại sáng loáng, đội mũ cối công binh màu xanh lá, đang vác những mảnh lá xanh như chiếc khiên chắn cùng đứng trước bức tường đá granite đen tuyền, ánh mắt quyết tâm sẵn sàng cho trận đánh lớn. |
| b28 | 03:34.4–03:41.6 (7.1s) | L272 | Sóng âm sonar của cá voi sát thủ mạnh đến mức có thể làm choáng váng các loài cá nhỏ xung quanh chỉ bằng một tiếng nhấp chuột âm thanh đanh thép! |  | Các luồng sóng âm thanh màu xanh dương lan tỏa làm rung chuyển các khối đá ngầm dưới đáy hào nước; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b29 | 03:41.6–03:50.8 (9.2s) | L273 | Hệ thống não bộ khổng lồ nặng tới 5kg của cá voi sát thủ có thể phân tích hàng triệu tín hiệu âm thanh dội về trong 0,001 giây, tái hiện lại cấu trúc không gian ba chiều hoàn hảo! |  | Đồ họa máy tính mô phỏng não bộ cá voi xử lý bản đồ 3D đáy nước ngầm; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b30 | 03:50.8–03:57.4 (6.7s) | L274 | Cú quất đuôi sóng thần của đại ca biển cả đã chứng minh sức mạnh cơ học vô song của loài động vật có vú thống trị toàn bộ chuỗi thức ăn đại dương! |  | chú Cá Voi Sát Thủ hoạt hình thân đen bóng bụng trắng tinh, vây lưng cao vút cắm ăng-ten định vị sonar nhỏ xíu, miệng cười nhếch mép kiểu trùm mafia biển cả lượn một vòng điệu nghệ dưới làn nước trong vắt sau khi đập tan cánh cửa đập; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b31 | 03:57.4–04:03.7 (6.2s) | L275 | Sức mạnh của bầy cá voi sát thủ không chỉ nằm ở cơ bắp mà còn nằm ở sự truyền thừa tri thức săn mồi qua hàng trăm thế hệ gia tộc mẫu hệ! |  | Đàn cá voi sát thủ bơi uốn lượn dưới đại dương xanh biếc, cá voi mẹ dẫn đầu truyền dạy kỹ năng bơi lội cho cá voi con; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b32 | 04:03.7–04:10.9 (7.3s) | L276 | Cánh cửa van đập nước ngầm bị đánh sập là minh chứng hùng hồn cho thấy không một công trình nhân tạo nào có thể ngăn cản được sức mạnh của đại dương bao la! |  | Dòng nước ngầm trong vắt phản chiếu ánh trăng rọi qua khe đá, mở ra con đường thẳng tiến lên các tầng cao; KHÔNG có anh Chỉ Huy trong cảnh này. |

### scene09 · BOONG-KE ĐÁ GRANITE, CHIM GÕ KIẾN & KIẾN CẮT LÁ · 279.3s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:10.3 (10.3s) | L277 | Bức tường Boong-ke của Cửa Ải 6 là chướng ngại vật vật lý kiên cố nhất trong toàn bộ Pháo Đài Tự Nhiên. Các khối đá granite đen dày 2 mét được ghép khít khao đến mức một lưỡi dao cạo cũng không thể lách qua! |  | Bức tường thành khổng lồ xây bằng đá granite đen bóng sừng sững chắn ngang lối đi, bề mặt đá nhẵn thín không một kẽ hở, ánh sáng đèn pha phản chiếu lạnh lùng trên mặt đá; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b02 | 00:10.3–00:19.2 (8.9s) | L278 | Độ cứng của đá granite nằm ở thang điểm bảy trên thang độ cứng khoáng vật, chỉ đứng sau ngọc bích và kim cương. Mọi nỗ lực dùng búa tạ của con người đập vào đây sẽ chỉ làm mẻ búa và gãy tay kẻ đập! |  | Một chiếc búa sắt bổ xuống mặt đá granite nảy ngược trở lại tóe lửa, mặt đá chỉ để lại một vệt trắng mờ nhạt không hề suy suyển; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b03 | 00:19.2–00:26.4 (7.3s) | L279 | Nhưng đêm nay, pháo đài phải đối đầu với một cỗ máy khoan sinh học sở hữu chiếc đầu có khả năng triệt tiêu xung chấn thần kỳ nhất vũ trụ: Đặc vụ Chim Gõ Kiến! |  | chú Chim Gõ Kiến hoạt hình mào lông đỏ rực dựng đứng, mỏ dài sắc nhọn như mũi khoan titan, đội mũ bảo hộ lao động màu vàng có gắn đèn pin thợ mỏ đứng chỉnh lại chiếc mũ bảo hộ màu vàng có gắn đèn pin thợ mỏ, vươn chiếc cổ thon dài chắc nịch, chiếc mỏ nhọn hoắt bóng loáng như một mũi khoan bằng hợp kim titan; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b04 | 00:26.4–00:34.4 (7.9s) | L280 | Cơ bắp cổ của chim gõ kiến được cấu tạo từ các bó cơ xoắn siêu dày, có thể phát ra lực đẩy tương đương với một chiếc búa tạ mini bổ xuống bề mặt mục tiêu! |  | Hình cắt lớp giải phẫu cơ cổ của chim gõ kiến với các bó cơ màu đỏ sẫm đan chéo nhau hình mạng lưới trợ lực; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b05 | 00:34.4–00:44.0 (9.7s) | L281 | Hãy tưởng tượng lực va chạm khủng khiếp mà đầu chim gõ kiến phải chịu đựng trong mỗi cú mổ. Các nhà cơ sinh học tại đại học Bắc Kinh đã gắn các cảm biến siêu vi để đo đạc và thu về những con số rùng mình! |  | Sơ đồ giải phẫu sọ chim gõ kiến với các đường sóng xung kích màu đỏ lan tỏa từ đỉnh mỏ qua hộp sọ, các thông số kỹ thuật hiển thị chi tiết (không chữ, không số); KHÔNG có anh Chỉ Huy trong cảnh này. |
| b06 | 00:44.0–00:49.5 (5.4s) | L282 | Khi gõ vào thân cây gỗ hay đá cứng, đầu của chim gõ kiến phải chịu một lực gia tốc va đập lên tới 1200G! | **1200G** · Gia tốc va đập · R/390 · [0.5, 0.6] | Đồ họa đo lực va chạm: mũi tên lực hướng thẳng vào đầu chim chỉ mức 1200G, gấp một trăm lần lực gia tốc khiến một phi công chiến đấu tinh nhuệ bất tỉnh nhân sự! KHÔNG có anh Chỉ Huy trong cảnh này. |
| b07 | 00:49.5–00:56.9 (7.4s) | L283 | Và anh chàng không chỉ gõ một lần rồi nghỉ. Tần số mổ của chim gõ kiến đạt tới 20 lần/giây, với vận tốc đầu mỏ lao tới sáu mét một giây! | **20 LẦN/S** · Tần số mổ · L/410 · [0.4, 0.5] | Đồng hồ đo tần số dao động hiển thị vạch kim rung liên tục ở mức 20 chu kỳ một giây, hình ảnh mỏ chim chuyển động nhanh đến mức nhòe mờ như cánh quạt máy bay; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b08 | 00:56.9–01:06.0 (9.1s) | L284 | Với lực đập 1200G lặp lại 20 lần/giây, bất kỳ bộ não sinh vật nào cũng sẽ bị dập nát thành cháo. Nhưng Chim Gõ Kiến vẫn tỉnh táo, minh mẫn và mắt sáng như sao! |  | Cận cảnh gương mặt tươi rói của chú Chim Gõ Kiến hoạt hình mào lông đỏ rực dựng đứng, mỏ dài sắc nhọn như mũi khoan titan, đội mũ bảo hộ lao động màu vàng có gắn đèn pin thợ mỏ, đôi mắt tròn xoe linh hoạt, không hề có bất kỳ dấu hiệu hoa mắt chóng mặt nào; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b09 | 01:06.0–01:13.2 (7.2s) | L285 | Màng nháy mắt của chim gõ kiến tự động đóng sập lại 0,001 giây trước mỗi cú va chạm, giữ cho nhãn cầu không bị văng ra khỏi hốc mắt! |  | Chiếc màng nháy dày bảo vệ mắt chim đóng lại như một chiếc kính bảo hộ thể thao trong khoảnh khắc mỏ chạm đá; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b10 | 01:13.2–01:18.6 (5.4s) | L286 | Bí mật nằm ở bộ giáp chống rung chấn ba lớp tinh vi mà tạo hóa đã ban tặng cho loài chim này! |  | Bản vẽ kỹ thuật phóng to ba tầng bảo vệ bên trong hộp sọ chim gõ kiến: xương mỏ đàn hồi, xương móng hyoid và lớp xương xốp vi mô; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b11 | 01:18.6–01:27.7 (9.1s) | L287 | Thứ nhất, chiếc xương móng hyoid của chim gõ kiến không nằm ở cuống họng như người, mà dài ngoằng, quấn một vòng từ đáy hàm vòng qua sau gáy lên tận đỉnh đầu rồi chui vào lỗ mũi! |  | Cấu trúc chiếc xương móng hyoid màu vàng nhạt quấn trọn quanh hộp sọ như chiếc dây đai an toàn ba điểm của xe đua Công Thức Một, siết chặt và giữ cố định não bộ; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b12 | 01:27.7–01:35.2 (7.5s) | L288 | Thứ hai, mỏ trên dài hơn mỏ dưới đúng một mi-li-mét, giúp chuyển hướng các sóng xung kích gây hại thành sóng trượt vô hại đi xuống thân mình! |  | Hình phóng to hai đầu mỏ lệch nhau một mi-li-mét: sóng xung kích màu đỏ bị bẻ gãy và trượt dọc theo xương ức chim mà không truyền thẳng vào hộp sọ; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b13 | 01:35.2–01:45.8 (10.6s) | L289 | Và thứ ba, xương sọ của chim gõ kiến là một cấu trúc xốp vi mô chứa vô số lỗ rỗng chứa không khí, đóng vai trò như chiếc đệm khí lò xo đàn hồi triệt tiêu toàn bộ chấn động trước khi chạm tới màng não! |  | Lát cắt hiển vi lớp xương xốp hộp sọ trông như một miếng bọt biển kim loại siêu bền, hấp thụ năng lượng va đập trong chớp mắt; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b14 | 01:45.8–01:51.2 (5.4s) | L290 | Tọa độ điểm yếu của bức tường đã được quét xong! Đó là ba điểm nứt ứng suất ngầm nơi ba khối đá granite giao nhau! |  | Đèn pin thợ mỏ trên mũ của chú Chim Gõ Kiến hoạt hình mào lông đỏ rực dựng đứng, mỏ dài sắc nhọn như mũi khoan titan, đội mũ bảo hộ lao động màu vàng có gắn đèn pin thợ mỏ chiếu luồng ánh sáng vàng rực vào ba điểm giao nhau giữa các khối đá granite; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b15 | 01:51.2–01:56.9 (5.7s) | L291 | Khai hỏa! Chim Gõ Kiến bám chặt bốn móng vuốt vào vách đá, đuôi tì làm điểm tựa kiên cố, bắt đầu chuỗi khoan phá thần tốc! |  | chú Chim Gõ Kiến hoạt hình mào lông đỏ rực dựng đứng, mỏ dài sắc nhọn như mũi khoan titan, đội mũ bảo hộ lao động màu vàng có gắn đèn pin thợ mỏ vào tư thế tác chiến vững như bàn thạch, chiếc đầu bắt đầu lao vào mổ liên hoàn với tốc độ ánh sáng; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b16 | 01:56.9–02:04.0 (7.1s) | L292 | Cốc cốc cốc cốc cốc cốc cốc! Tiếng mỏ va chạm vào đá granite rít lên như tiếng súng máy liên thanh, các tia lửa điện nổ lách tách chói lòa trong bóng tối! |  | Đầu mỏ gõ liên hồi vào vách đá tạo thành những chùm tia lửa vàng cam rực rỡ, bụi đá mịn bay mù mịt quanh thân chim; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b17 | 02:04.0–02:12.9 (8.9s) | L293 | Chỉ trong vòng 45 giây, ba lỗ khoan tròn sâu 10cm đã xuất hiện ngay trên tim của các khối đá! Các vết nứt chân chim bắt đầu lan rộng ra xung quanh như mạng nhện! |  | Bề mặt đá granite rạn nứt thành các đường vân nứt gãy lớn, phát ra những tiếng răng rắc báo hiệu kết cấu bắt đầu suy yếu; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b18 | 02:12.9–02:19.0 (6.1s) | L294 | Đến lượt lực lượng công binh bí mật vào sân! Chim Gõ Kiến lùi lại nhường đường cho Đại Đội Kiến Cắt Lá xuất kích! |  | chú Chim Gõ Kiến hoạt hình mào lông đỏ rực dựng đứng, mỏ dài sắc nhọn như mũi khoan titan, đội mũ bảo hộ lao động màu vàng có gắn đèn pin thợ mỏ gạt mồ hôi trên trán gật đầu ra hiệu, từ khe đá phía dưới, hàng ngàn chú kiến cắt lá ùa ra thành một dòng thác màu nâu đỏ; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b19 | 02:19.0–02:30.0 (11.0s) | L295 | Đừng coi thường những chú kiến nhỏ bé này! Nghiên cứu mới nhất đăng trên tạp chí Báo Cáo Khoa Học của Nature đã phát hiện: hàm răng của kiến cắt lá được tẩm một lớp kim loại nặng gồm kẽm và mangan nguyên chất! |  | Bản chụp kính hiển vi điện tử quét chiếc răng kìm của kiến cắt lá: đầu răng phát sáng ánh kim loại thép siêu cứng nhờ sự phân bố đồng đều của các nguyên tử kẽm và mangan; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b20 | 02:30.0–02:38.2 (8.2s) | L296 | Lớp kim loại nặng này biến chiếc hàm răng chitin của kiến cắt lá thành những lưỡi cưa tẩm thép không gỉ, sắc bén và bền bỉ gấp ba lần răng của côn trùng thông |  | Mô phỏng chiếc răng kiến cắt xuyên qua khoáng vật đá cứng dễ như cắt một lát bơ mềm; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b21 | 02:38.2–02:46.9 (8.7s) | L297 | thường! Hàng ngàn chú kiến cắt lá cùng lúc thò hàm răng thép vào các kẽ nứt do chim gõ kiến vừa tạo ra, bắt đầu nghiền nát và bốc dỡ từng hạt bụi đá granite ra ngoài! |  | Đàn kiến phối hợp nhịp nhàng: những chú kiến to lớn dùng hàm bẩy các mảnh đá vụn, những chú kiến nhỏ hơn khuân vác các mẩu đá chạy ra xa; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b22 | 02:46.9–02:54.2 (7.2s) | L298 | Khả năng khuân vác gấp 50 lần trọng lượng cơ thể giúp bầy kiến dọn sạch hàng tạ đá vụn chỉ trong vòng chưa đầy 2 phút! |  | Dòng kiến di chuyển thoăn thoắt mang theo những viên sỏi đá ra khỏi kẽ nứt, làm rỗng hoàn toàn chân móng bức tường thành; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b23 | 02:54.2–03:00.4 (6.2s) | L299 | Khoét móng! Đục rãnh! Bẩy then! Đại đội công binh kiến cắt lá đào khoét chân tường đá với tốc độ của một cỗ máy xúc công nghiệp hiện đại! |  | Chân móng của khối đá granite khổng lồ bị khoét rỗng một khoảng trống lớn, mất đi điểm tựa thăng bằng trọng lực; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b24 | 03:00.4–03:07.4 (7.0s) | L300 | Toàn bộ khối đá granite nặng 10 tấn bắt đầu nghiêng dần về phía trước. Chim Gõ Kiến bay lên, tung cú mổ quyết định cuối cùng vào chiếc chốt bản lề trên đỉnh! |  | chú Chim Gõ Kiến hoạt hình mào lông đỏ rực dựng đứng, mỏ dài sắc nhọn như mũi khoan titan, đội mũ bảo hộ lao động màu vàng có gắn đèn pin thợ mỏ lấy đà từ trên cao bổ thẳng một cú mổ trời giáng vào đỉnh khối đá đang mất thăng bằng; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b25 | 03:07.4–03:15.8 (8.4s) | L301 | Rầm! Khối đá granite khổng lồ đổ sập xuống sàn đá, vỡ tan thành những mảnh đá vụn vô hại, mở toang một cửa vòm rộng thênh thang dẫn thẳng vào Cửa Ải 7! |  | Bức tường boong-ke sụp đổ hoàn toàn trong làn khói bụi mù mịt, ánh sáng đỏ rực từ sa mạc bên ngoài ùa vào soi rọi con đường tiến bước; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b26 | 03:15.8–03:23.7 (7.9s) | L302 | Biểu tượng boong-ke đá trên {BOARD} chuyển sang màu xanh ngọc bích rực rỡ! Sáu trên 7 cửa ải đã bị biệt đội đặc nhiệm đánh sập không còn một dấu vết! |  | bản đồ hologram 3D của Pháo Đài Tự Nhiên nổi lơ lửng trong không khí, hiển thị 7 cửa ải an ninh phát sáng đỏ và thanh tiến độ phá khóa màu xanh ngọc (không có chữ, không có số) sáng bừng lên với sáu biểu tượng màu xanh ngọc, thanh tiến độ phá khóa đã chạm mốc tám mươi lăm phần trăm; anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm nở nụ cười tự hào. |
| b27 | 03:23.7–03:34.1 (10.4s) | L303 | Chim Gõ Kiến đậu trên đống đá vụn, giơ chiếc mỏ nhọn hoắt lên trời làm động tác gõ tạ ơn khán giả, bên cạnh là đàn kiến cắt lá đang vẫy những mảnh lá xanh ăn mừng chiến thắng vang dội! |  | chú Chim Gõ Kiến hoạt hình mào lông đỏ rực dựng đứng, mỏ dài sắc nhọn như mũi khoan titan, đội mũ bảo hộ lao động màu vàng có gắn đèn pin thợ mỏ cùng tiểu đội ba chú Kiến Cắt Lá hoạt hình màu nâu đỏ, đầu to mang hàm răng kim loại sáng loáng, đội mũ cối công binh màu xanh lá, đang vác những mảnh lá xanh như chiếc khiên chắn tạo dáng chụp ảnh lưu niệm trên đống đổ nát của bức tường đá granite, vẻ mặt rạng rỡ của những  |
| b28 | 03:34.1–03:41.9 (7.7s) | L304 | Nhưng cánh cửa cuối cùng ngăn cách biệt đội với kho báu trung tâm đang hiện ra trước mắt: Cửa Ải 7 — Bức Tường Vách Đứng 90 Độ và Lò Lửa Sa Mạc 50 Độ |  | Khung cảnh Cửa Ải Bảy hiện ra: một thung lũng lòng chảo sa mạc cát đỏ rực bốc hơi nóng hầm hập năm mươi độ C, ở giữa là ngọn tháp nhẵn thín dựng đứng chín mươi độ cao chót vót không một gờ bám; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b29 | 03:41.9–03:52.8 (10.9s) | L305 | C! Không thể bay qua vì bão nhiệt cuốn phăng mọi luồng khí, cũng không thể đào hầm vì nền cát lún di động. Chỉ có sự phối hợp giữa một cỗ xe tăng chịu nhiệt và một bậc thầy leo vách đá mới có thể giải mã cánh cửa tối thượng |  | anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm quay sang nhìn chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao và chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt: "Đặc vụ Lạc Đà và Đặc vụ Dê |
| b30 | 03:52.8–03:58.0 (5.2s) | L306 | này! Cặp đôi sa mạc và vách đá chuẩn bị bước vào cuộc chinh phục đỉnh cao nhất của pháo đài! |  | chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao và chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt cùng bước qua đống đổ nát, tiến vào chảo lửa sa mạc với ánh mắt kiên định không hề sợ hãi. |
| b31 | 03:58.0–04:06.7 (8.7s) | L307 | Để bảo vệ đôi mắt khỏi bụi đá và chấn động cực mạnh, mi mắt của chim gõ kiến có thể tự động co thắt các mạch máu quanh võng mạc để duy trì huyết áp ổn định trong từng cú mổ! |  | Bản vẽ cắt lớp mắt chim gõ kiến với hệ thống mạch nước màu co giãn thông minh bảo vệ thị lực tuyệt đối; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b32 | 04:06.7–04:16.4 (9.8s) | L308 | Trong khi đó, lớp kim loại kẽm và mangan trên răng của kiến cắt lá được phân bố đồng đều đến mức độ nguyên tử, giúp chiếc răng không bao giờ bị mẻ dù cắn vào đá granite cứng nhất! |  | Kính hiển vi lực nguyên tử quét lớp phủ kim loại nặng trên bề mặt răng kiến; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b33 | 04:16.4–04:25.1 (8.7s) | L309 | Sự kết hợp giữa công nghệ khoan va đập của loài chim và công nghệ cưa cắt kim loại của loài kiến đã tạo nên một kỳ tích công binh chưa từng có trong lịch sử điệp viên! |  | chú Chim Gõ Kiến hoạt hình mào lông đỏ rực dựng đứng, mỏ dài sắc nhọn như mũi khoan titan, đội mũ bảo hộ lao động màu vàng có gắn đèn pin thợ mỏ và tiểu đội ba chú Kiến Cắt Lá hoạt hình màu nâu đỏ, đầu to mang hàm răng kim loại sáng loáng, đội mũ cối công binh màu xanh lá, đang vác những mảnh lá xanh như chiếc khiên chắn cùng đứng trên đống đá vụn mỉm cười tự hào. |
| b34 | 04:25.1–04:31.9 (6.8s) | L310 | Nhịp gõ búa thần tốc 20 lần/giây của chim gõ kiến tạo nên một bản hòa âm cơ học rộn rã làm bừng tỉnh cả góc pháo đài tối tăm! |  | chú Chim Gõ Kiến hoạt hình mào lông đỏ rực dựng đứng, mỏ dài sắc nhọn như mũi khoan titan, đội mũ bảo hộ lao động màu vàng có gắn đèn pin thợ mỏ gõ mỏ nhịp nhàng như một nghệ sĩ đánh trống cự phách, các tia lửa vàng cam nhảy múa theo từng cú mổ; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b35 | 04:31.9–04:39.3 (7.3s) | L311 | Hàng ngàn chú kiến cắt lá đồng loạt vác đá diễu hành dưới ánh đèn pin thợ mỏ, tạo nên một cảnh tượng công binh hoành tráng chưa từng thấy! |  | tiểu đội ba chú Kiến Cắt Lá hoạt hình màu nâu đỏ, đầu to mang hàm răng kim loại sáng loáng, đội mũ cối công binh màu xanh lá, đang vác những mảnh lá xanh như chiếc khiên chắn xếp hàng dài ngay ngắn như những người lính tí hon kỷ luật và kiên cường; KHÔNG có anh Chỉ Huy trong cảnh này. |

### scene10 · DÊ NÚI LEO VÁCH 90° & LẠC ĐÀ VƯỢT SA MẠC 50°C · 276.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:06.7 (6.7s) | L312 | Cửa Ải 7 là phòng tuyến cuối cùng và khắc nghiệt nhất của Pháo Đài Tự Nhiên: Lò Lửa Sa Mạc kết hợp với Bức Tường Vách Đứng 90 Độ! |  | Cảnh thung lũng lòng chảo sa mạc cát đỏ rực bốc lên những làn sóng nhiệt méo mó dưới ánh nắng gắt, nhiệt kế chỉ vạch năm mươi độ C đỏ rực; chính giữa là ngọn tháp đá granite dựng đứng chín mươi độ nhẵn bóng như gương; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b02 | 00:06.7–00:15.8 (9.2s) | L313 | Nhiệt độ trên mặt cát sa mạc lúc này đo được là 50°C! Không khí khô khốc như lò nung có thể hút cạn từng giọt nước trong cơ thể của bất kỳ sinh vật nào chỉ trong vòng chưa đầy 15 phút! | **50°C** · Lò lửa sa mạc · R/390 · [0.5, 0.6] | Mặt cát sa mạc đỏ rực nứt nẻ, ảo ảnh hơi nóng bốc lên ngùn ngụt làm mờ ảo khung cảnh phía trước; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b03 | 00:15.8–00:20.7 (4.9s) | L314 | Mọi phương tiện cơ giới mang vào đây đều sẽ bị cát lún nuốt chửng bánh xe, động cơ quá nhiệt và bốc cháy. |  | Một chiếc xe bọc thép hoạt hình nằm lún ngập nửa thân trong cát đỏ, nắp ca-pô bốc khói đen nghi ngút; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b04 | 00:20.7–00:27.2 (6.5s) | L315 | Gió sa mạc cuốn theo những cơn bão bụi silic sắc nhọn có thể làm xước rách giác mạc và phá hủy hệ hô hấp của người thường! |  | Bão cát mù mịt quét qua thung lũng, cát bụi bay ràn rạt như những hạt đạn thủy tinh; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b05 | 00:27.2–00:34.7 (7.5s) | L316 | Nhưng kẻ đang ung dung sải bước trên chảo cát nóng rẫy này lại chính là cỗ xe tăng sinh học tối thượng của hoang mạc: Đặc vụ Lạc Đà Sa Mạc! |  | chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao thong thả bước từng bước dài vững chãi trên cát lún đỏ rực, bàn chân xòe rộng có đệm thịt đàn hồi nâng đỡ cơ thể không hề bị lún; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b06 | 00:34.7–00:44.5 (9.7s) | L317 | Trên lưng Lạc Đà không chở súng đạn, mà đang cõng theo người đồng đội leo núi cừ khôi nhất: Đặc vụ Dê Núi Bắc Mỹ! Cặp bài trùng này chuẩn bị thực hiện màn phối hợp ngoạn mục nhất lịch sử điệp viên! |  | chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt đứng vững vàng trên lưng lạc đà, bốn móng guốc bám chắc vào khung đai thồ hàng, bộ lông trắng muốt bay nhẹ trong gió sa mạc; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b07 | 00:44.5–00:54.0 (9.6s) | L318 | Bí mật nào giúp Lạc Đà Sa Mạc thản nhiên vượt qua vùng nhiệt độ 50°C mà không hề nhỏ một giọt mồ hôi? Hãy nhìn sâu vào hệ tuần hoàn kỳ diệu của anh chàng này! |  | Bản vẽ y khoa hiển vi phóng to giọt nước màu của lạc đà dưới kính hiển vi: các tế bào hồng cầu có hình bầu dục độc nhất vô nhị đang phát sáng óng ánh; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b08 | 00:54.0–01:03.3 (9.2s) | L319 | Tất cả các loài động vật có vú trên Trái Đất, bao gồm cả con người, đều có tế bào hồng cầu hình tròn dẹt. Khi cơ thể mất nước, hồng cầu tròn sẽ dính bết lại làm tắc nghẽn mạch máu, dẫn đến đột quỵ. |  | Sơ đồ so sánh: hồng cầu hình tròn của người bị biến dạng và vón cục lại khi thiếu nước, trong khi hồng cầu hình oval của lạc đà vẫn trôi chảy mượt mà qua các mao mạch nhỏ; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b09 | 01:03.3–01:13.7 (10.4s) | L320 | Nhưng hồng cầu của Lạc Đà lại có hình bầu dục thuôn dài! Cấu trúc oval đặc biệt này cho phép chúng tiếp tục lưu thông trơn tru ngay cả khi máu trở nên đặc quánh do cơ thể mất tới 25% lượng nước! |  | Dòng tế bào nước màu hình oval màu đỏ tươi lướt đi êm ả qua các mạch nước màu ngoằn ngoèo, duy trì việc vận chuyển oxy đến từng tế bào mà không hề bị tắc nghẽn; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b10 | 01:13.7–01:23.1 (9.4s) | L321 | Và khi gặp nguồn nước, hồng cầu hình bầu dục của lạc đà có thể giãn nở tới 240% thể tích mà không hề bị vỡ! Anh chàng có thể nạp 100 lít nước chỉ trong mười phút ngắn ngủi! | **240% NỞ** · Hồng cầu Oval · L/380 · [0.4, 0.5] | Hình mô phỏng một tế bào hồng cầu oval phồng to gấp đôi như một quả bóng cao su bền bỉ mà không hề bị thủng rách; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b11 | 01:23.1–01:33.6 (10.5s) | L322 | Chưa hết, thân nhiệt của Lạc Đà Sa Mạc là một cỗ máy điều hòa nhiệt độ sinh học tự động: ban đêm hạ xuống 34°C để tích trữ khí lạnh, ban ngày tăng dần lên 41°C mà không cần đổ mồ hôi làm mát! |  | Biểu đồ nhiệt kế sinh học dao động tự nhiên từ 34°C đến 41°C, giữ cho cơ thể luôn mát mẻ tiết kiệm tối đa nguồn nước quý giá; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b12 | 01:33.6–01:41.4 (7.8s) | L323 | Cộng thêm chiếc mũi xoắn ốc khổng lồ tái hấp thu tới 60% hơi ẩm từ hơi thở ra, Lạc Đà có thể đi bộ xuyên qua chảo lửa sa mạc mà chẳng tốn lấy một giọt |  | Cắt lớp khoang mũi xoắn ốc của lạc đà: các luồng hơi nước thở ra bị giữ lại bởi lớp màng nhầy và tái hấp thu ngược trở lại cơ thể; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b13 | 01:41.4–01:48.6 (7.2s) | L324 | mồ hôi! Bướu mỡ trên lưng khi bị oxy hóa còn sản sinh ra hơn 100 gam nước chuyển hóa cho mỗi 100 gam chất béo bị tiêu hao! |  | Hình mô phỏng các phân tử mỡ trong bướu lạc đà chuyển hóa thành các giọt nước tinh khiết nuôi dưỡng cơ thể; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b14 | 01:48.6–01:55.0 (6.3s) | L325 | Lạc Đà sải những bước chân thần tốc, đưa Dê Núi tiếp cận sát chân ngọn tháp đá granite nguyên khối trong tiếng reo hò của phòng chỉ huy! |  | chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao dừng lại ngay sát chân tháp đá, quỳ hai chân trước xuống thật êm ái để Dê Núi bước xuống đất; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b15 | 01:55.0–02:02.7 (7.7s) | L326 | Trước mặt họ là bức tường thành dựng đứng 90° cao 30m! Bề mặt đá nhẵn thín như gương, không một kẽ nứt, không một mấu gờ nhô ra quá ba mi-li-mét! | **VÁCH 90°** · Thách thức trọng lực · R/410 · [0.5, 0.6] | Góc nhìn từ chân tháp nhìn thẳng lên đỉnh: vách đá granite dựng đứng chín mươi độ chót vót, nhẵn bóng không một bậc thang, đỉnh tháp là chiếc cầu treo đóng chặt; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b16 | 02:02.7–02:11.9 (9.3s) | L327 | Bất kỳ một vận động viên leo núi chuyên nghiệp nào nhìn vào vách đá này cũng phải lắc đầu bỏ cuộc. Nhưng đối với Dê Núi Bắc Mỹ, đây chỉ là một cầu thang quen thuộc hàng ngày! |  | chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt ngẩng cao đầu nhìn lên đỉnh tháp, ánh mắt tự tin của kẻ thống trị những đỉnh núi cheo leo nhất thế giới; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b17 | 02:11.9–02:16.7 (4.8s) | L328 | Vũ khí bí mật của Đặc vụ Dê Núi nằm ở bốn chiếc móng guốc thách thức mọi định luật vật lý! |  | Hình vẽ phóng to mặt dưới của chiếc móng guốc dê núi: viền ngoài là lớp sừng cứng như thép, bên trong là lớp đệm cao su mềm màu đen có khả năng đàn hồi và bám dính cực mạnh; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b18 | 02:16.7–02:28.7 (11.9s) | L329 | Viền ngoài của móng là lớp sừng cứng sắc nhọn có thể găm chặt vào những vi gờ đá chỉ dày một mi-li-mét. Trong khi phần lòng móng là lớp đệm cao su dẻo ma sát cực cao, hoạt động như những chiếc giác hút chân không bám dính vào mặt đá! |  | Cận cảnh chiếc móng guốc bám chặt vào một gờ đá siêu nhỏ, lớp đệm cao su ép sát vào bề mặt đá tạo thành lực hút chân không giữ chặt bàn chân; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b19 | 02:28.7–02:37.0 (8.3s) | L330 | Cộng thêm tầm nhìn bao quát 320° và cấu trúc khớp vai lực lưỡng, dê núi có thể kéo toàn bộ trọng lượng cơ thể lên chỉ bằng hai chiếc móng trước! |  | Sơ đồ cơ học khớp vai và cơ lưng của dê núi đang gồng lực kéo toàn thân vươn lên trên vách đá thẳng đứng; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b20 | 02:37.0–02:45.1 (8.1s) | L331 | Trọng tâm cơ thể đặt cực thấp cùng xương sườn hẹp giúp dê núi ép sát ngực vào vách đá, triệt tiêu hoàn toàn mô-men quay làm lật ngửa cơ thể! |  | Bản vẽ mô phỏng trọng tâm cơ thể dê núi nằm sát sạt mặt đá thẳng đứng; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b21 | 02:45.1–02:49.6 (4.6s) | L332 | Xuất kích! Dê Núi Bắc Mỹ nhún mình bật nhảy một cú ngoạn mục lên vách đá dựng đứng 90°! |  | chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt phi thân lên không trung, hai móng trước găm chặt vào một gờ đá vô hình trên bề mặt vách đá nhẵn thín; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b22 | 02:49.6–02:55.6 (6.0s) | L333 | Một bước... hai bước... ba bước! Dê Núi leo ngược lên vách đá thẳng đứng với tốc độ thoăn thoắt như đang chạy trên mặt đất bằng phẳng! |  | chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt thoăn thoắt di chuyển lên cao trên vách đá dựng đứng chín mươi độ, các chân chuyển động nhịp nhàng chuẩn xác đến từng milimet; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b23 | 02:55.6–03:02.5 (6.8s) | L334 | Gió lốc sa mạc thổi giật từng cơn dữ dội, nhưng bốn chiếc móng giác hút cao su của anh chàng vẫn bám dính chặt chẽ không hề lung lay dù chỉ một ly! |  | Cơn bão cát sa mạc quét qua vách đá, nhưng chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt vẫn dán chặt thân mình vào mặt đá, kiên định leo từng mét một; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b24 | 03:02.5–03:09.4 (6.9s) | L335 | Cách đỉnh tháp 5 mét! Mỏm đá cuối cùng bị gãy vụn dưới chân! Dê Núi treo lơ lửng trên không trung chỉ bằng hai chiếc móng trước! Cả phòng chỉ huy nín thở! |  | Hai móng trước của chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt bám vào mép đá cuối cùng, thân mình đung đưa giữa không trung trên vực sâu hun hút; anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm siết chặt nắm tay! |
| b25 | 03:09.4–03:15.8 (6.4s) | L336 | Gồng cơ vai! Dê Núi vung một chân sau lên mỏm đá, tung cú bật nhảy tối thượng cuối cùng phi thẳng lên sàn đỉnh tháp! |  | chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt bật người một cú ngoạn mục vượt qua mép lan can đá, tiếp đất an toàn trên đỉnh tháp trong tiếng reo hò vang dội của toàn đội; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b26 | 03:15.8–03:20.3 (4.5s) | L337 | Đến lượt hạ cầu! Dê Núi đạp mạnh vào chiếc cần gạt tời cáp khổng lồ đặt trên đỉnh |  | Cặp sừng đen của chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt húc mạnh vào chiếc cần gạt cáp tời, hệ thống bánh răng rên rỉ quay vòng nhả xích; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b27 | 03:20.3–03:27.7 (7.4s) | L338 | tháp! Rầm! Chiếc cầu treo rút khổng lồ bắc ngang qua thung lũng sa mạc hạ xuống, nối liền lối vào thẳng vào cổng chính của Phòng Châu Báu Trung Tâm! |  | Cầu treo bằng thép dày hạ xuống bắc qua miệng vực sa mạc, tạo nên một con đường đại lộ thênh thang cho toàn bộ biệt đội tiến bước; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b28 | 03:27.7–03:38.0 (10.3s) | L339 | Toàn bộ bảy biểu tượng cửa ải trên {BOARD} đồng loạt chuyển sang màu xanh ngọc bích rực rỡ! 100 phần trăm hệ thống an ninh của Pháo Đài Tự Nhiên đã bị vô hiệu hóa hoàn toàn! |  | bản đồ hologram 3D của Pháo Đài Tự Nhiên nổi lơ lửng trong không khí, hiển thị 7 cửa ải an ninh phát sáng đỏ và thanh tiến độ phá khóa màu xanh ngọc (không có chữ, không có số) sáng rực rỡ với đủ bảy biểu tượng màu xanh ngọc bích, tiếng chuông báo hiệu thành công vang lên giòn giã khắp phòng chỉ huy; anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm mỉm cười giơ ngón tay cái tán thưởn |
| b29 | 03:38.0–03:47.4 (9.5s) | L340 | Cả 10 đặc vụ tập hợp trước cánh cổng sắt mạ vàng của Phòng Châu Báu. Nhưng đúng lúc này, từ trong bóng tối của hành lang ngoại vi, một đội tuần tra người máy tự động bất ngờ xuất hiện bao vây lối thoát! |  | Đội lính tuần tra người máy mang súng điện tử và đèn pin pha cực sáng xuất hiện từ các góc hành lang tối, bắt đầu khép chặt vòng vây quanh cổng kho báu; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b30 | 03:47.4–03:53.5 (6.1s) | L341 | Chỉ Huy Mật Vụ khẽ nhếch mép: "Đừng lo. Chúng ta vẫn còn một tay súng bắn tỉa đang ẩn nấp trên cao chưa từng lộ diện!" |  | anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm nhìn lên màn hình phụ góc trên: chú Chim Bách Thanh hoạt hình lông xám trắng có dải lông đen vắt ngang mắt như dải băng cướp biển, mỏ có móc câu sắc nhọn, chân cầm một nhánh gai nhọn công nghệ đang ẩn mình trong bóng tối của cành cây bồ kết, ánh mắt sắc như dao găm đã khóa chặt toàn bộ mục tiêu lính gác. |
| b31 | 03:53.5–03:58.0 (4.5s) | L342 | Tay súng bắn tỉa bí mật chuẩn bị khai hỏa dọn sạch hậu phương trong chớp mắt! |  | Cận cảnh chiếc mỏ khoằm sắc như lưỡi liềm của chim bách thanh sáng loáng dưới ánh trăng rằm. |
| b32 | 03:58.0–04:07.7 (9.6s) | L343 | Lạc Đà Sa Mạc có thể mất tới 30 phần trăm trọng lượng cơ thể do mất nước mà vẫn đi bộ bình thường, trong khi các loài thú khác sẽ chết vì trụy tim nếu mất 15 phần trăm nước! |  | Biểu đồ so sánh khả năng chịu mất nước phi thường của lạc đà so với các loài động vật khác; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b33 | 04:07.7–04:13.9 (6.2s) | L344 | Dê Núi Bắc Mỹ thì sở hữu cặp sừng đen rỗng bên trong giúp phân tán nhiệt lượng cơ thể khi vận động mạnh trên vách đá cheo |  | Cận cảnh cặp sừng đen nhọn hoắt của chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt với các rãnh tản nhiệt tự nhiên lấp lánh dưới nắng; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b34 | 04:13.9–04:21.6 (7.7s) | L345 | leo! Bộ đôi sa mạc và vách đá đã chứng minh rằng không có địa hình nào trên Trái Đất có thể ngăn cản bước chân của những kẻ nắm vững nghệ thuật thích |  | chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao và chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt cùng nhìn lên đỉnh tháp cao chót vót với nụ cười chiến thắng. |
| b35 | 04:21.6–04:29.2 (7.6s) | L346 | nghi! Bức tường đá dựng đứng 90° từng là nỗi khiếp sợ của muôn loài nay đã in dấu bốn móng guốc cao su kiêu hãnh của Dê Núi Bắc Mỹ! |  | Dấu móng guốc sắc nét in trên vách đá granite thẳng đứng như những chiếc huân chương danh dự của bậc thầy leo núi; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b36 | 04:29.2–04:36.4 (7.2s) | L347 | Lạc Đà Sa Mạc đứng dưới chân tháp ngước nhìn người đồng đội trên cao, cất tiếng kêu hò reo cổ vũ nồng nhiệt vang vọng khắp lòng chảo sa mạc! |  | chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao vẫy tai mừng rỡ, hai bướu mỡ rung rinh nhịp nhàng dưới ánh mặt trời rực rỡ; KHÔNG có anh Chỉ Huy trong cảnh này. |

### scene11 · SÁT THỦ BÁCH THANH & CHIẾN THUẬT CẮM GAI NHỌN · 231.1s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.5 (8.5s) | L348 | Bên ngoài cổng Phòng Châu Báu, không khí căng thẳng đến nghẹt thở. Đội tuần tra an ninh tự động của Pháo Đài Tự Nhiên đã phát hiện ra các dấu vết xâm nhập bất thường! |  | Hành lang đá mờ ảo ánh đèn đỏ báo động, một tiểu đội năm người máy tuần tra mang súng điện tử và đèn rọi đang bước đều bước lùng sục khắp các ngóc ngách; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b02 | 00:08.5–00:18.1 (9.6s) | L349 | Những chiếc loa phát thanh trên tường chuẩn bị phát tín hiệu báo động đỏ toàn căn cứ. Nếu tiếng còi báo động vang lên, toàn bộ các lối thoát hiểm sẽ bị đánh sập vĩnh viễn, chôn vùi cả biệt đội trong |  | Bàn tay kim loại của người máy chỉ huy chuẩn bị gạt chiếc cần báo động tổng lực màu đỏ gắn trên cột trụ hành lang; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b03 | 00:18.1–00:26.1 (8.0s) | L350 | lòng đất! Toàn bộ 10 đặc vụ bên dưới đều đang tập trung trước cánh cổng kho báu, không kịp quay lại ứng cứu. Khoảng cách giữa họ và đội tuần tra chỉ còn chưa đầy 30m! |  | Cận cảnh các đặc vụ quay lưng lại, chưa hay biết nguy hiểm đang cận kề phía sau lưng; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b04 | 00:26.1–00:34.4 (8.3s) | L351 | Các tia quét tầm nhiệt của đội tuần tra đang lia dần về phía bóng lưng của Chim Cắt và Quạ Đen, chỉ còn vài giây nữa là chuông báo động sẽ réo vang! |  | Những chấm đỏ la-de ngắm bắn dịch chuyển từng tấc một trên sàn đá hoa cương; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b05 | 00:34.4–00:43.9 (9.5s) | L352 | Nhưng trên cành cao của cây bồ kết cổ thụ ngoài cửa sổ hành lang, một bóng đen nhỏ bé mang đôi cánh xám trắng đang lặng lẽ quan sát từng cử động của kẻ địch: Đặc vụ Chim Bách Thanh! |  | chú Chim Bách Thanh hoạt hình lông xám trắng có dải lông đen vắt ngang mắt như dải băng cướp biển, mỏ có móc câu sắc nhọn, chân cầm một nhánh gai nhọn công nghệ đậu ẩn mình sau tán lá rậm rạp, dải lông đen ngang mắt trông sắc lạnh như một tay súng phun tia nước tầm xa huyền thoại, mỏ ngậm một chùm gai nhọn thép công nghệ cao; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b06 | 00:43.9–00:54.7 (10.7s) | L353 | Đừng để vẻ bề ngoài nhỏ nhắn như một chú chim sẻ đánh lừa bạn! Trong giới điểu học, Chim Bách Thanh được mệnh danh là "Gã Đồ Tể Rừng Xanh", sát thủ sở hữu kỹ thuật phục kích tàn nhẫn và thông minh bậc nhất tự |  | Tranh vẽ phong cách đồ họa Cold War: bóng đen của chim bách thanh in lên vách tường với chiếc mỏ khoằm có móc câu sắc nhọn đáng sợ như một chiếc lưỡi liềm nhỏ; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b07 | 00:54.7–01:02.9 (8.2s) | L354 | nhiên! Bách Thanh là loài chim duy nhất không có móng vuốt đại bàng nhưng lại có thể săn bắt và hạ gục những con mồi to gấp đôi trọng lượng cơ thể mình! |  | Sơ đồ giải phẫu chiếc mỏ của bách thanh: trên mỏ trên có một chiếc mấu xương sắc nhọn gọi là răng giả tomium, hoạt động như một chiếc kìm bấm chuyên bẻ gãy đốt sống con mồi; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b08 | 01:02.9–01:10.1 (7.2s) | L355 | Cơ cổ cực khỏe cho phép chim bách thanh thực hiện cú giật xoắn cực mạnh làm trật khớp cổ con mồi chỉ trong 0,1 giây! |  | Hình mô phỏng hướng chuyển động xoắn vặn lực cơ học của đầu chim bách thanh khi tấn công mục tiêu; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b09 | 01:10.1–01:18.5 (8.3s) | L356 | Và vũ khí đáng sợ nhất của Bách Thanh chính là kỹ thuật cắm gai nhọn độc nhất vô nhị! Các nhà khoa học tại đại học Florida đã ghi nhận những phát hiện chấn động về tập tính |  | Tranh minh họa tư liệu nghiên cứu: một bụi gai sa mạc cắm đầy những con mồi được treo lơ lửng ngay ngắn như một kho hàng dự trữ; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b10 | 01:18.5–01:27.1 (8.7s) | L357 | này! Khi bắt được những loài côn trùng có nọc độc chết người như cào cào Lubber khổng lồ, bách thanh không bao giờ ăn ngay. Anh chàng sẽ cắp con mồi đem cắm chặt lên một chiếc gai nhọn |  | Cận cảnh chú chim bách thanh dùng mỏ xiên chặt một con cào cào độc lên cành gai nhọn của bụi cây một cách điêu luyện; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b11 | 01:27.1–01:37.8 (10.7s) | L358 | sắc bén! Con mồi được phơi trên gai suốt 3 ngày trời! Dưới ánh nắng và gió, toàn bộ chất độc tự nhiên trong cơ thể con mồi sẽ bị phân hủy hoàn toàn, biến một bữa ăn kịch độc thành món ăn thơm ngon bổ dưỡng an toàn tuyệt |  | Sơ đồ phân hủy chất độc: các phân tử độc tố màu xanh lá cây bốc hơi dần theo thời gian ba ngày, để lại phần thịt an toàn cho chim; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b12 | 01:37.8–01:47.8 (9.9s) | L359 | đối! Chưa hết, Bách Thanh sở hữu một bản đồ không gian thiên tài trong não bộ: anh chàng có thể ghi nhớ vị trí của hàng chục chốt gai nhọn khác nhau rải rác trong bán kính 500 mét mà không bao giờ nhầm | **500 MÉT** · Bản đồ chốt gai · R/400 · [0.5, 0.6] | Bản đồ vệ tinh hiển thị bán kính 500 mét quanh tổ chim, hàng chục chấm đỏ đánh dấu các kho gai nhọn sáng lên đồng loạt trong trí nhớ của chú chim; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b13 | 01:47.8–01:54.3 (6.5s) | L360 | lẫn! Anh chàng biết chính xác món mồi nào đã được cắm bao nhiêu ngày, món nào đã hết độc tố và sẵn sàng thưởng thức! |  | Đồ thị quản lý chuỗi cung ứng thực phẩm tự nhiên trong trí não chim bách thanh; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b14 | 01:54.3–01:58.7 (4.4s) | L361 | Tọa độ đã khóa! Mục tiêu là năm chiếc camera cảm biến và chiếc cần gạt báo động khẩn cấp! |  | Cận cảnh ánh mắt sắc lẹm của chú Chim Bách Thanh hoạt hình lông xám trắng có dải lông đen vắt ngang mắt như dải băng cướp biển, mỏ có móc câu sắc nhọn, chân cầm một nhánh gai nhọn công nghệ qua kính ngắm quang học, tâm ngắm khóa chặt chiếc công tắc báo động trên tường hành lang; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b15 | 01:58.7–02:03.4 (4.8s) | L362 | Bách Thanh tung cánh lao vút qua khung cửa sổ hành lang như một mũi tên xé gió, không phát ra một tiếng động |  | chú Chim Bách Thanh hoạt hình lông xám trắng có dải lông đen vắt ngang mắt như dải băng cướp biển, mỏ có móc câu sắc nhọn, chân cầm một nhánh gai nhọn công nghệ sà xuống cực nhanh theo đường bay sát mặt đất, thân hình lướt đi thoăn thoắt trong bóng tối mờ ảo; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b16 | 02:03.4–02:09.8 (6.4s) | L363 | nhỏ nào! Vút! Vút! Vút! Bách Thanh phóng ra những chiếc gai thép sắc nhọn găm thẳng vào năm ống kính camera cảm biến của đội tuần tra người máy! |  | Những chiếc gai thép nhọn hoắt cắm chuẩn xác vào tâm điểm thấu kính của các camera giám sát, tia lửa điện chập mạch nổ tanh tách làm tối đen hệ thống quan sát; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b17 | 02:09.8–02:14.9 (5.1s) | L364 | Đội tuần tra bị mù hoàn toàn! Người máy chỉ huy hoảng hốt vung tay định kéo cần gạt còi báo động khẩn cấp! |  | Người máy chỉ huy đưa bàn tay kim loại ra sát chiếc cần gạt màu đỏ chỉ còn cách đúng năm xăng-ti-mét; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b18 | 02:14.9–02:22.5 (7.6s) | L365 | Không kịp nữa rồi! Bách Thanh bay vọt lên, chiếc mỏ sắc bén có mấu răng giả tomium bổ thẳng một cú mổ thần tốc vào khớp ngón tay kim loại của người máy! |  | Cú mổ chuẩn xác của chú Chim Bách Thanh hoạt hình lông xám trắng có dải lông đen vắt ngang mắt như dải băng cướp biển, mỏ có móc câu sắc nhọn, chân cầm một nhánh gai nhọn công nghệ đánh gãy khớp nối ngón tay robot, chiếc then cài rơi rụng lanh canh xuống sàn đá; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b19 | 02:22.5–02:31.2 (8.6s) | L366 | Anh chàng nhanh như chớp dùng mỏ quặp lấy một chiếc cọc gai thép dài 20cm, đóng chặt xuyên qua chiếc cần gạt báo động, ghim cứng nó vào tường đá không thể nhúc nhích! |  | Chiếc cọc gai thép găm chặt chiếc cần gạt báo động vào sâu trong vách đá, khóa chết công tắc còi hú ở vị trí tắt vĩnh viễn; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b20 | 02:31.2–02:38.6 (7.5s) | L367 | Đội tuần tra người máy mất phương hướng, quay mòng mòng va đập vào nhau rồi đổ rạp xuống sàn hành lang như những quân cờ domino đổ sập! |  | Năm người máy tuần tra va vào nhau kêu loảng xoảng, chập mạch điện tóe lửa nằm bất động trên sàn đá; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b21 | 02:38.6–02:46.8 (8.1s) | L368 | Bách Thanh đậu nhẹ nhàng trên đỉnh chiếc mũ sắt của người máy chỉ huy, nghiêng đầu chỉnh lại dải lông đen ngang mắt, phát ra một tiếng kêu lách cách báo cáo Chỉ Huy Mật Vụ. |  | chú Chim Bách Thanh hoạt hình lông xám trắng có dải lông đen vắt ngang mắt như dải băng cướp biển, mỏ có móc câu sắc nhọn, chân cầm một nhánh gai nhọn công nghệ đứng hiên ngang trên đống tàn tích của đội tuần tra, mỏ ngậm một chiếc cúc áo kim loại chiến lợi phẩm, giơ một ngón cánh chào báo cáo chiến công hiển hách. |
| b22 | 02:46.8–02:54.6 (7.8s) | L369 | "Ngoại vi đã dọn sạch! Toàn bộ hệ thống còi báo động đã bị khóa cứng bằng gai thép!" Giọng Bách Thanh đanh gọn truyền qua mic. |  | anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm trong phòng điều khiển thở phào nhẹ nhõm, mỉm cười gật đầu: "Làm tốt lắm Đặc vụ Bách Thanh. Đường lui đã hoàn toàn an toàn!" |
| b23 | 02:54.6–03:01.8 (7.2s) | L370 | Mối đe dọa từ phía sau đã được hóa giải hoàn toàn. Giờ đây, chỉ còn lại cánh cổng sắt mạ vàng của Phòng Châu Báu Trung Tâm sừng sững trước mặt 10 đặc vụ. |  | Khung cảnh cánh cổng vòm khổng lồ bằng vàng ròng và đá quý của Phòng Châu Báu phát sáng lung linh huyền ảo giữa lòng pháo đài u tối; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b24 | 03:01.8–03:09.4 (7.6s) | L371 | Tất cả các ổ khóa đã mở. Toàn bộ 7 cửa ải đã bị xuyên thủng. Chiếc két sắt chứa Bản Thiết Kế Tiến Hóa Tối Thượng chỉ còn cách họ đúng một bước chân. |  | Cả mười đặc vụ đứng xếp hàng ngay ngắn trước cánh cổng vàng, ánh mắt hồi hộp và tò mò nhìn vào khe cửa đang từ từ hé mở... KHÔNG có anh Chỉ Huy trong cảnh này. |
| b25 | 03:09.4–03:15.2 (5.8s) | L372 | Giờ phút lịch sử đã điểm! Chiếc két sắt tối thượng của tạo hóa chuẩn bị hé lộ bí mật lớn nhất hành tinh! |  | Ánh sáng vàng kim từ khe cửa chiếu rọi lên khuôn mặt đầy háo hức của mười chiến binh dũng cảm. |
| b26 | 03:15.2–03:22.2 (7.1s) | L373 | Kỹ thuật săn mồi và quản lý kho dự trữ của Chim Bách Thanh là minh chứng rõ nét nhất cho trí thông minh sinh thái học của loài chim ăn thịt nhỏ bé này! |  | Bản đồ sinh thái mô phỏng các chốt gai dự trữ thức ăn của chim bách thanh trải dài khắp lãnh thổ săn mồi; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b27 | 03:22.2–03:31.3 (9.0s) | L374 | Nhờ chiếc mỏ có mấu răng giả tomium, bách thanh có thể truyền toàn bộ lực cắn vào một điểm duy nhất trên đốt sống cổ của mục tiêu, tạo nên một lực phá hủy tập trung cực kỳ chết chóc! |  | Mô hình cơ học lực cắn tập trung tại đỉnh mấu răng tomium của chim bách thanh; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b28 | 03:31.3–03:39.0 (7.7s) | L375 | Sau khi vô hiệu hóa hoàn toàn đội tuần tra, anh chàng khẽ lau mỏ vào cành cây, tiếp tục giữ vai trò sát thủ thầm lặng bảo vệ toàn bộ đội hình rút lui an toàn! |  | chú Chim Bách Thanh hoạt hình lông xám trắng có dải lông đen vắt ngang mắt như dải băng cướp biển, mỏ có móc câu sắc nhọn, chân cầm một nhánh gai nhọn công nghệ đứng bất động trên cành cao, đôi mắt sắc lẹm canh chừng mọi biến động từ xa. |
| b29 | 03:39.0–03:45.4 (6.4s) | L376 | Khả năng ẩn nấp ngụy trang tài tình giúp Chim Bách Thanh hoàn toàn hòa mình vào màu vỏ cây bồ kết xám xịt, biến mất khỏi tầm mắt kẻ thù! |  | Bộ lông xám trắng của chú Chim Bách Thanh hoạt hình lông xám trắng có dải lông đen vắt ngang mắt như dải băng cướp biển, mỏ có móc câu sắc nhọn, chân cầm một nhánh gai nhọn công nghệ tiệp màu hoàn hảo với thân cây cổ thụ, chỉ có đôi mắt sáng quắc là chuyển động; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b30 | 03:45.4–03:51.1 (5.7s) | L377 | Toàn bộ hành lang ngoại vi đã rơi vào im lặng tuyệt đối, mở đường cho giờ phút khai mở kho báu lịch sử của muôn loài! |  | Hành lang đá thông thoáng không còn bóng dáng một người máy tuần tra nào, ánh đèn êm dịu dẫn đường vào phòng trung tâm; KHÔNG có anh Chỉ Huy trong cảnh này. |

### scene12 · CÚ LẬT KÈO CHẤN ĐỘNG — KHO BÁU THẬT SỰ CỦA PHÁO ĐÀI · 270.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:06.8 (6.8s) | L378 | Cánh cổng vàng ròng nặng 10 tấn của Phòng Châu Báu Trung Tâm từ từ mở ra, kèm theo một tiếng rít trầm đục vang vọng khắp các vách đá. |  | Cánh cổng vòm mạ vàng khổng lồ mở toang ra một căn phòng mái vòm tráng lệ, ánh sáng vàng kim và hào quang tím huyền bí tỏa ra từ trung tâm căn phòng; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b02 | 00:06.8–00:15.9 (9.1s) | L379 | Mười đặc vụ cùng bước vào trong sự ngỡ ngàng tột độ. Không khí bên trong căn phòng thơm ngát mùi thảo mộc cổ xưa, hoàn toàn đối lập với mùi khói súng và sắt thép lạnh lẽo bên ngoài. |  | Toàn bộ mười đặc vụ bước vào căn phòng, ánh mắt sáng rực đầy tò mò và thán phục nhìn quanh những bức tường cẩm thạch khắc hoa văn cổ đại; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b03 | 00:15.9–00:22.3 (6.4s) | L380 | Chính giữa căn phòng là một chiếc bệ đá hoa cương đen tuyền, trên đó đặt chiếc két sắt tối thượng được rèn bằng hợp kim siêu bền bất khả xâm |  | Một chiếc bệ đá đen bóng bẩy đặt chiếc két sắt hình lập phương cổ kính, bốn góc két sắt có chạm khắc biểu tượng của bốn nguyên tố: gió, nước, đất và lửa; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b04 | 00:22.3–00:32.0 (9.7s) | L381 | phạm. Bốn bức bích họa khổng lồ trên tường tái hiện lại lịch sử tiến hóa 500 triệu năm của Trái Đất, từ những sinh vật phù du cổ đại cho đến những loài động vật kỳ diệu ngày nay! |  | Tranh tường mosaic phát sáng tái hiện cây phả hệ tiến hóa sinh học rực rỡ với hàng ngàn nhánh sinh vật; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b05 | 00:32.0–00:39.7 (7.7s) | L382 | Các đặc vụ bắt đầu xì xào bàn tán về món kho báu đang nằm bên trong. Mỗi người đều có một giấc mơ riêng sau khi hoàn thành phi vụ thế kỷ! |  | Cả đội quây quanh chiếc bệ đá, ánh mắt lấp lánh sự phấn khích của những người sắp được nhận phần thưởng xứng đáng; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b06 | 00:39.7–00:45.1 (5.3s) | L383 | Chuột Chũi Trũi chảy nước miếng mơ về một kho chứa 1 triệu tấn khoai tây mật ngọt lịm ăn không bao giờ hết! |  | chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên chảy nước miếng mơ màng ôm hai tay trước ngực; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b07 | 00:45.1–00:51.4 (6.4s) | L384 | Quạ Đen thì xoa xoa hai cánh mắt sáng như sao, đòi một núi thìa bạc nạm kim cương để xây cái tổ đắt giá nhất hành tinh! |  | chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép đứng xoa xoa hai cánh mắt sáng lấp lánh tưởng tượng chiếc tổ bằng vàng bạc; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b08 | 00:51.4–00:57.3 (5.8s) | L385 | Cá Voi Sát Thủ nhô đầu lên cười khùng khục đòi một biển đầy cá hồi béo ngậy và chiếc vương miện thống trị đại |  | chú Cá Voi Sát Thủ hoạt hình thân đen bóng bụng trắng tinh, vây lưng cao vút cắm ăng-ten định vị sonar nhỏ xíu, miệng cười nhếch mép kiểu trùm mafia biển cả nhô đầu lên ngoác miệng cười để lộ hàm răng trắng bóng; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b09 | 00:57.3–01:03.9 (6.6s) | L386 | dương! Còn Lạc Đà Sa Mạc chỉ khẽ chớp mắt mơ về một hồ nước ngọt mát lạnh quanh năm với những rặng xương rồng không bao giờ tàn! |  | chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao chớp chớp hàng mi cong vút mỉm cười hiền lành; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b10 | 01:03.9–01:11.7 (7.8s) | L387 | Dê Núi mong ước có một ngọn núi tuyết riêng tư để tha hồ phi thân, trong khi đàn kiến cắt lá mơ về một cánh rừng lá phong non xanh mướt! |  | chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt và tiểu đội ba chú Kiến Cắt Lá hoạt hình màu nâu đỏ, đầu to mang hàm răng kim loại sáng loáng, đội mũ cối công binh màu xanh lá, đang vác những mảnh lá xanh như chiếc khiên chắn cùng hướng mắt về chiếc két sắt với nụ cười rạng rỡ; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b11 | 01:11.7–01:19.8 (8.1s) | L388 | Chỉ Huy Mật Vụ bước tới trước chiếc két sắt, nhẹ nhàng đặt chiếc máy tính bảng mật mã vào ổ nhận dạng trung tâm. Tách! Tách! Tách! Chiếc két sắt từ từ bật nắp! |  | anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm bấm nút xác nhận cuối cùng, các chốt khóa nặng nề kêu lách cách trượt mở, nắp chiếc két sắt từ từ mở bung ra với một làn khói trắng mờ ảo; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b12 | 01:19.8–01:26.8 (7.0s) | L389 | Một luồng ánh sáng chói lòa bừng lên, khiến tất cả phải đưa tay lên che mắt. Nhưng khi làn khói tan dần... cả 10 đặc vụ đều sững sờ chết lặng! |  | Mười đặc vụ cùng trố mắt nhìn vào bên trong lòng chiếc két sắt, miệng há hốc không thốt nên lời; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b13 | 01:26.8–01:35.6 (8.7s) | L390 | Bên trong chiếc két sắt tối thượng... không hề có một thỏi vàng nào! Không có kim cương, không có súng laser tối tân, cũng chẳng có lấy một cọng khoai tây nào cả! |  | Lòng chiếc két sắt chỉ có một chiếc bệ nhung đỏ đơn sơ, trên đó đặt một chiếc gương tròn cổ kính bằng đồng và một cuộn da cừu cũ kỹ ngả vàng; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b14 | 01:35.6–01:43.4 (7.8s) | L391 | Ủa... kho báu của chúng ta đâu rồi sếp ơi? Bị ai nẫng tay trên trước rồi hả sếp? Hay là chúng ta đột nhập nhầm pháo đài rồi? |  | chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên ngơ ngác thò đầu vào trong lòng két sắt ngó nghiêng, hai chân trước cào cào lớp vải nhung trống không; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b15 | 01:43.4–01:50.0 (6.6s) | L392 | Chỉ Huy Mật Vụ không hề ngạc nhiên. Anh chàng cú mèo nhẹ nhàng cầm chiếc gương tròn lên, xoay mặt gương hướng về phía toàn thể 10 đặc vụ. |  | anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm nâng chiếc gương đồng sáng bóng lên cao, mặt gương phản chiếu rõ mồn một khuôn mặt của mười loài động vật đang đứng quây quần xung quanh; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b16 | 01:50.0–01:58.4 (8.5s) | L393 | "Các bạn hãy nhìn kỹ vào trong gương đi. Kho báu thật sự của Pháo Đài Tự Nhiên... đang đứng ngay trước mặt các bạn đấy." Giọng Chỉ Huy trầm ấm và trang nghiêm vang lên. |  | Cận cảnh mặt gương phản chiếu đôi mắt rực lửa của chim cắt, hàm răng của chuột chũi, khăn len của ếch gỗ, mỏ quạ đen, vây cá voi, mỏ chim gõ kiến, bướu lạc đà, sừng dê núi, móc gai bách thanh và hàm răng thép của kiến; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b17 | 01:58.4–02:03.6 (5.2s) | L394 | Chỉ Huy từ từ mở cuộn da cừu cổ xưa ra, đọc to những dòng chữ được khắc ghi từ hàng trăm triệu năm trước: |  | anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm giở cuộn da cừu phát sáng những dòng chữ cổ màu vàng kim rực rỡ, ánh sáng ấm áp lan tỏa khắp gian phòng; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b18 | 02:03.6–02:11.7 (8.1s) | L395 | "Vàng bạc rồi cũng sẽ bị chôn vùi dưới cát bụi. Súng đạn rồi cũng sẽ bị rỉ sét mục nát theo thời gian. Nhưng khả năng thích nghi và vươn lên của sự sống thì bất tử." |  | Tranh minh họa lịch sử tiến hóa của Trái Đất: từ những sinh vật đơn bào cổ đại vượt qua kỷ băng hà, núi lửa phun trào để tiến hóa thành muôn loài kỳ diệu ngày nay; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b19 | 02:11.7–02:18.8 (7.2s) | L396 | Kho báu vĩ đại nhất của tự nhiên không phải là những thứ vật chất vô tri, mà chính là Bản Thiết Kế Tiến Hóa nằm ngay trong cơ thể của mỗi loài sinh vật! |  | Hình ảnh đồ họa hào quang bao quanh từng đặc vụ: mỗi loài vật tỏa sáng một vầng hào quang rực rỡ tượng trưng cho sức mạnh tiến hóa của mình; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b20 | 02:18.8–02:30.3 (11.5s) | L397 | Chiếc mũi nén khí siêu thanh 389 km/h của Chim Cắt. Khả năng thở bằng đường hoa quả sống sót 18 phút không oxy của Chuột Chũi. Thuật đóng băng 65% cơ thể hồi sinh sau 7 tháng của Ếch Gỗ. |  | Ba biểu tượng sinh học tuyệt mỹ xuất hiện lơ lửng trên không trung: luồng khí nén chim cắt, phân tử đường fructose của chuột chũi và tinh thể băng ngọc bích của ếch gỗ; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b21 | 02:30.3–02:39.9 (9.6s) | L398 | Trí tuệ chế tạo công cụ giải câu đố 8 bước của Quạ Đen. Sóng âm sonar 225 dB quất sóng thần của Cá Voi Sát Thủ. Hộp sọ giảm chấn 1200G của Chim Gõ Kiến. |  | Ba kỳ quan kỹ thuật tiếp theo bay lượn trên không: chiếc móc câu của quạ, sóng âm thanh cá voi và chiếc đai an toàn sọ não của chim gõ kiến; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b22 | 02:39.9–02:52.0 (12.1s) | L399 | Tế bào máu hình oval giãn nở 240% của Lạc Đà Sa Mạc. Móng guốc giác hút cao su bám vách đá 90° của Dê Núi. Kỹ thuật cắm gai khử độc của Chim Bách Thanh. Và hàm răng tẩm kim loại nặng của Đại Đội Kiến Cắt Lá! |  | Bốn mảnh ghép cuối cùng hòa quyện vào nhau tạo thành một quả cầu ánh sáng sinh học khổng lồ rực rỡ giữa phòng châu báu; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b23 | 02:52.0–03:01.1 (9.1s) | L400 | Mỗi loài trong số mười quái kiệt này tự thân đã là một kiệt tác kỹ thuật đỉnh cao mà không một phòng thí nghiệm hay cỗ máy tối tân nào của con người có thể sao chép hoàn hảo được! |  | Toàn bộ mười đặc vụ nhìn nhau, ánh mắt từ thất vọng chuyển sang sự tự hào khôn xiết khi nhận ra giá trị vô giá của chính bản thân mình; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b24 | 03:01.1–03:12.0 (10.9s) | L401 | Và điều kỳ diệu nhất: không một cá nhân nào có thể một mình vượt qua cả 7 cửa ải của pháo đài. Chỉ khi mười loài vật cùng đoàn kết, bù đắp điểm yếu cho nhau, cánh cửa bất khả thi mới được mở toang! |  | Mười đặc vụ cùng khoác vai nhau, nắm lấy tay nhau tạo thành một vòng tròn gắn kết bền chặt quanh bệ đá cổ xưa; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b25 | 03:12.0–03:19.2 (7.2s) | L402 | Đó chính là thông điệp tối thượng của Bản Thiết Kế Tiến Hóa: Đa dạng sinh học chính là chiếc khiên hộ mệnh duy nhất bảo vệ sự sống trên hành tinh xanh |  | Quả cầu ánh sáng nở bung ra thành hình ảnh Trái Đất xanh ngắt bao la với muôn loài muôn thú cùng chung sống hòa bình dưới ánh mặt trời rực rỡ; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b26 | 03:19.2–03:25.0 (5.8s) | L403 | này! Biệt Đội Đặc Nhiệm Sinh Học đã hoàn thành sứ mệnh lịch sử vĩ đại nhất của muôn loài! |  | anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm nâng ly chúc mừng mười người đồng đội anh hùng trong hào quang rực rỡ của căn phòng châu báu. |
| b27 | 03:25.0–03:30.5 (5.5s) | L404 | Nhưng khoảnh khắc lắng đọng đầy ý nghĩa vừa kết thúc... thì một tiếng nổ chát chúa vang lên từ trần phòng châu báu! |  | Trần nhà rung chuyển dữ dội, bụi đá rơi lả tả xuống sàn, một chiếc đèn báo động màu tím than bắt đầu quay tít mù kèm theo tiếng còi hú đinh tai nhức óc! KHÔNG có anh Chỉ Huy trong cảnh này. |
| b28 | 03:30.5–03:39.6 (9.1s) | L405 | Chiếc bệ đá tự động tụt xuống lòng đất, kích hoạt hệ thống tự hủy cuối cùng của pháo đài: "Cảnh báo khẩn cấp! Bản Thiết Kế đã được mở khóa! Pháo đài sẽ tự hủy hoàn toàn sau đúng 3 phút nữa!" |  | Một chiếc đồng hồ đếm ngược kỹ thuật số khổng lồ màu đỏ rực xuất hiện trên vách tường đá, bắt đầu đếm lùi từng giây: 03:00... 02:59... 02:58! KHÔNG có anh Chỉ Huy trong cảnh này. |
| b29 | 03:39.6–03:46.8 (7.2s) | L406 | Cuộc đột nhập đã hoàn tất. Bây giờ là bài toán sinh tử cuối cùng: Chiến Dịch Tháo Chạy Nghẹt Thở để thoát khỏi đống đổ nát trước khi chiếc cổng thành đóng vĩnh |  | anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm hét lớn vào bộ đàm: "Toàn đội kích hoạt phương án thoát hiểm khẩn cấp! Chạy ngay!" Cả mười đặc vụ cùng quay đầu lao vút ra ngoài hành lang trong tiếng nổ rung chuyển đất trời! |
| b30 | 03:46.8–03:52.6 (5.8s) | L407 | viễn! Cả căn cứ đang sụp đổ sau lưng, thời gian chỉ còn tính bằng từng tích tắc ngắn ngủi! |  | Cảnh mười đặc vụ cùng phóng nhanh qua cánh cửa vòm khi các khối đá khổng lồ bắt đầu rơi rụng như mưa. |
| b31 | 03:52.6–03:59.4 (6.9s) | L408 | Hàng trăm triệu năm qua, Trái Đất đã trải qua biết bao kỷ băng hà buốt giá, bao đợt tuyệt chủng khắc nghiệt và núi lửa phun trào ngút trời. |  | Tranh minh họa Trái Đất qua các kỷ địa chất lịch sử: từ đại cổ sinh cho đến kỷ băng hà và sự trỗi dậy của các loài thú; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b32 | 03:59.4–04:09.5 (10.1s) | L409 | Nhưng sự sống chưa bao giờ chịu khuất phục. Mỗi một loài sinh vật, từ chú kiến nhỏ bé dưới chân đến chú cá voi khổng lồ ngoài khơi xa, đều là một mảnh ghép không thể thiếu của bức tranh thiên nhiên hoàn mỹ! |  | Toàn bộ mười đặc vụ đứng quây quần bên nhau, ánh sáng từ cuộn Bản Thiết Kế Tiến Hóa soi rọi khuôn mặt đầy xúc động; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b33 | 04:09.5–04:17.8 (8.2s) | L410 | Biệt Đội Đặc Nhiệm Sinh Học đã chứng minh rằng khi chúng ta cùng thấu hiểu và tôn trọng những giá trị tiến hóa của tự nhiên, không có thử thách nào là không thể vượt qua! |  | Mười đặc vụ cùng đặt tay lên cuộn da cừu cổ xưa, tuyên thệ bảo vệ sự sống muôn loài trên hành tinh. |
| b34 | 04:17.8–04:24.2 (6.4s) | L411 | Khoảnh khắc chiếc gương đồng phản chiếu khuôn mặt của cả mười quái kiệt sẽ mãi mãi là bức tranh đẹp nhất trong lịch sử sinh tồn của Trái Đất! |  | Mười đặc vụ cùng soi bóng vào chiếc gương đồng cổ kính, nụ cười rạng rỡ của những người chiến thắng nở trên môi; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b35 | 04:24.2–04:30.9 (6.8s) | L412 | Bản Thiết Kế Tiến Hóa Tối Thượng đã tìm được những chủ nhân xứng đáng nhất, những đại sứ xuất sắc của thế giới tự nhiên kỳ diệu! |  | Ánh sáng vàng kim từ cuộn da cừu bao trùm lấy toàn bộ căn phòng, sưởi ấm tâm hồn của mỗi người chiến sĩ điệp viên; KHÔNG có anh Chỉ Huy trong cảnh này. |

### scene13 · PHÁO ĐÀI ĐẾM NGƯỢC 3 PHÚT & MÀN COMBO ĐÀO TẨU · 220.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.3 (8.3s) | L413 | Đồng hồ đếm ngược tự hủy đang nhấp nháy đỏ rực: 2 phút 50 giây! Toàn bộ Pháo Đài Tự Nhiên rung chuyển dữ dội như vừa trải qua một trận động đất mười độ Rích-te! |  | Trần hang đá nứt toác từng mảng lớn, những khối đá nặng hàng tấn rơi ầm ầm xuống sàn hành lang, khói bụi mịt mù che khuất toàn bộ tầm nhìn; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b02 | 00:08.3–00:16.1 (7.8s) | L414 | Các hệ thống phòng vệ tự động bị chập điện, phóng ra những tia lửa điện xanh lè đan chéo nhau như một lưới điện tử thần. Các cánh cửa sắt chống cháy bắt đầu sập xuống ầm ầm! |  | Những cánh cửa thép ngăn cháy dày cộp lần lượt rơi thẳng đứng từ trên trần xuống sàn đá kêu rầm rầm, từng lối đi dần dần bị bịt kín; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b03 | 00:16.1–00:23.5 (7.5s) | L415 | "Không được bỏ lại bất kỳ ai! Toàn đội kích hoạt đội hình combo giải cứu khẩn cấp!" Tiếng quát vang rền của Chỉ Huy Mật Vụ truyền thẳng vào tai nghe của từng đặc vụ. |  | anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm vừa chạy vừa ôm chặt chiếc máy tính bảng và cuộn da cừu cổ, liên tục quan sát bản đồ thoát hiểm đang chớp đỏ liên hồi; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b04 | 00:23.5–00:30.8 (7.2s) | L416 | Cửa sập số một rơi xuống chặn đứng lối ra của hành lang chính! Kẹt cứng! Khe hở dưới đáy chỉ còn chưa đầy 0,5m và đang hạ xuống dần! |  | Cánh cửa thép nặng nề chỉ còn cách mặt đất đúng bốn mươi xăng-ti-mét, chuẩn bị khóa chết đường thoát của cả đội; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b05 | 00:30.8–00:38.3 (7.6s) | L417 | Đến lượt cặp bài trùng công binh ra tay! Chim Gõ Kiến lao vút tới, mỏ kẹp chiếc đục sắt gõ liên hoàn 20 lần/giây vào rãnh trượt của cánh cửa! |  | chú Chim Gõ Kiến hoạt hình mào lông đỏ rực dựng đứng, mỏ dài sắc nhọn như mũi khoan titan, đội mũ bảo hộ lao động màu vàng có gắn đèn pin thợ mỏ bổ mỏ thần tốc vào khe trượt bản lề, các tia lửa nổ tung tóe chêm cứng một góc cửa làm cánh cửa khựng lại trong tích tắc; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b06 | 00:38.3–00:46.2 (7.8s) | L418 | Ngay lập tức, Đại Đội Kiến Cắt Lá dùng hàm răng tẩm kẽm và mangan ngoạm chặt lấy dây cáp tời phụ, kéo căng hết cỡ để giữ cánh cửa không bị rơi sập thêm! |  | Hàng ngàn chú kiến cắt lá cùng gồng mình kéo căng sợi dây thép chịu lực, tạo ra một khoảng trống vừa đủ cho đồng đội chui qua; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b07 | 00:46.2–00:50.1 (3.9s) | L419 | Dê Núi Bắc Mỹ cúi rạp người xuống: "Chuột Chũi, Ếch Gỗ, nhảy lên lưng tôi |  | chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt nhanh nhẹn quỳ chân xuống, chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên và chú Ếch Gỗ Bắc Cực hoạt hình da nâu vàng có vệt đen qua mắt như mặt nạ Zorro, đ |
| b08 | 00:50.1–00:58.3 (8.2s) | L420 | mau!" Dê Núi co bốn chân, tung một cú phi thân trượt bụng điệu nghệ qua khe hở chỉ vài xăng-ti-mét trước khi cánh cửa sập hẳn xuống mặt sàn đá! |  | chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt trượt qua khe cửa hẹp ngoạn mục như một vận động viên trượt băng, cánh cửa sắt đóng sầm sau lưng kêu rầm một tiếng đinh tai! KHÔNG có anh Chỉ Huy trong cảnh này. |
| b09 | 00:58.3–01:04.5 (6.2s) | L421 | Thời gian còn lại: một phút 40 giây! Hành lang phía trước bốc cháy dữ dội do ống dẫn khí gas của lò nhiệt sa mạc bị vỡ toang! |  | Một bức tường lửa đỏ rực bốc cao ba mét chắn ngang lối đi duy nhất, hơi nóng bốc lên ngùn ngụt sẵn sàng thiêu rụi bất kỳ ai bước tới gần; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b10 | 01:04.5–01:10.5 (6.1s) | L422 | "Dạt ra hai bên hết cho đại ca làm việc!" Tiếng gầm của Cá Voi Sát Thủ vang lên qua hệ thống cống thoát nước ngầm bên dưới sàn đá! |  | Một nắp cống kim loại bật tung lên trời, chú Cá Voi Sát Thủ hoạt hình thân đen bóng bụng trắng tinh, vây lưng cao vút cắm ăng-ten định vị sonar nhỏ xíu, miệng cười nhếch mép kiểu trùm mafia biển cả nhô đầu lên từ kênh nước áp lực cao chạy dọc hành lang; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b11 | 01:10.5–01:17.1 (6.6s) | L423 | Cá Voi Sát Thủ hít một hơi thật sâu làn nước lạnh, phóng ra một cột nước áp lực cao khổng lồ qua lỗ thở như một chiếc vòi rồng cứu hỏa tối tân! |  | Cột nước trắng xóa bắn vút ra từ lưng chú Cá Voi Sát Thủ hoạt hình thân đen bóng bụng trắng tinh, vây lưng cao vút cắm ăng-ten định vị sonar nhỏ xíu, miệng cười nhếch mép kiểu trùm mafia biển cả dập thẳng vào tâm điểm đám cháy, hơi nước bốc lên xèo xèo làm tắt ngấm ngọn lửa trong vòng ba giây! KHÔNG có anh Chỉ Huy trong cảnh này. |
| b12 | 01:17.1–01:24.5 (7.4s) | L424 | Lạc Đà Sa Mạc lập tức sải những bước chân dài vượt lên dẫn đầu, xòe hai bên hông che chắn cho các đồng đội nhỏ bé tránh khỏi những tảng đá nhọn đang rơi rụng từ trần hang! |  | chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao chạy chắn ngang phía trên, lớp lông dày và bướu mỡ kiên cố như một tấm khiên chống đạn bảo vệ toàn bộ đội hình; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b13 | 01:24.5–01:31.4 (6.9s) | L425 | Các tảng đá rơi trúng lưng lạc đà bị dội ngược ra ngoài nhờ lớp mỡ đàn hồi dày cộp, không gây tổn thương dù chỉ một vết xước! |  | Đá dăm nảy tưng tưng trên lưng lạc đà rơi xuống sàn mà chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao vẫn thản nhiên phi nước kiệu; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b14 | 01:31.4–01:39.0 (7.6s) | L426 | Thời gian còn lại: 50 giây! Toàn bộ căn cứ chìm trong khói đen đặc quánh! Hệ thống định vị vệ tinh mất tín hiệu hoàn toàn! Lối ra ở hướng nào? |  | Màn hình radar quét lối thoát bị nhiễu loạn hoàn toàn thành một màu xám xịt, không ai nhìn thấy đường đi trong làn khói đen mù mịt; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b15 | 01:39.0–01:44.7 (5.8s) | L427 | Quạ Đen bay vút lên cao sát trần hang, dùng đôi mắt tinh tường quan sát hướng di chuyển của những luồng gió tươi mát luồn qua các |  | chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép bay lượn trên cao, phát hiện một luồng khí trong lành màu xanh lam đang hút về phía cuối hành lang bên phải; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b16 | 01:44.7–01:52.4 (7.7s) | L428 | khe nứt! "Rẽ phải! Cổng vòm số ba! Chạy theo luồng gió tươi! Nhanh lên!" Quạ Đen vừa bay vừa kêu quạ quạ dẫn đường chuẩn xác cho cả đoàn quân! |  | chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép bay dẫn đầu như một ngọn hải đăng trong đêm, toàn bộ biệt đội nối đuôi nhau chạy thục mạng theo hướng chú quạ chỉ dẫn; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b17 | 01:52.4–02:00.3 (7.9s) | L429 | Thời gian còn lại: 20 giây! Cánh cửa sắt thoát hiểm cuối cùng của pháo đài đã hiện ra trước mắt! Nhưng bi kịch thay: cửa đã bị khóa chặt bằng ổ khóa điện tử khẩn cấp! |  | Cánh cửa thép thoát hiểm dẫn ra bầu trời đêm đang đóng kín mít, trên ổ khóa có một khe quẹt thẻ từ nhấp nháy đèn đỏ chờ mã kích hoạt; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b18 | 02:00.3–02:04.4 (4.1s) | L430 | "Chiếc thẻ từ dự phòng! Thẻ từ đang ở đâu?" Chỉ Huy Mật Vụ lục lọi túi áo hoảng hốt kêu lên! |  | anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm sờ vào túi áo khoác trống rỗng, mặt biến sắc khi nhớ lại tai nạn cắm gai ở cây bồ kết ngoài sân! KHÔNG có anh Chỉ Huy trong cảnh này. |
| b19 | 02:04.4–02:09.4 (5.0s) | L431 | Cách đó 50 mét ngoài cửa sổ, chiếc thẻ từ màu đỏ vẫn đang bị cắm chặt trên cành gai cao chót vót của Chim Bách Thanh! |  | Cận cảnh chiếc thẻ từ đung đưa trên cành gai sắc nhọn ngoài sân, cách quá xa tầm tay của bất kỳ ai dưới mặt đất; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b20 | 02:09.4–02:16.9 (7.5s) | L432 | Thời gian còn lại: mười giây! Chín... tám... bảy! Tiếng còi tự hủy bắt đầu rít lên từng hồi liên tục báo hiệu đợt phát nổ cuối cùng! |  | Đồng hồ đếm ngược nhấp nháy đỏ rực: 00:07... 00:06... 00:05! KHÔNG có anh Chỉ Huy trong cảnh này. |
| b21 | 02:16.9–02:24.8 (7.9s) | L433 | "Để đó cho tôi!" Một tia chớp xám đen xé toạc màn đêm lao vút qua khung cửa sổ với vận tốc 389 km/h: Chim Cắt Lớn! |  | chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng kích hoạt toàn bộ sức mạnh động cơ cánh, bổ nhào một đường cong hoàn hảo qua ngọn cây bồ kết; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b22 | 02:24.8–02:33.4 (8.6s) | L434 | Móng vuốt vàng sắc lẹm của Chim Cắt quặp chuẩn xác vào mép chiếc thẻ từ, bẻ gãy cành gai nhọn trong chớp mắt, rồi lượn một vòng tròn ngoạn mục ném thẳng chiếc thẻ vào tay Chỉ Huy! |  | Chiếc thẻ từ màu đỏ bay vút trong không trung, rơi trúng vào lòng bàn tay của anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm một cách hoàn hảo đến từng mi-li-mét; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b23 | 02:33.4–02:39.3 (5.8s) | L435 | Xoẹt! Chỉ Huy Mật Vụ quẹt mạnh chiếc thẻ qua khe nhận dạng! Tách! Cánh cửa sắt thoát hiểm bật mở toang ra bầu trời đêm |  | Cánh cửa bật mở, luồng gió đêm mát rượi ùa vào, phía dưới là con dốc thoải dẫn ra thung lũng an toàn; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b24 | 02:39.3–02:47.0 (7.7s) | L436 | bao la! Thời gian còn lại: 2 giây! Một giây! Toàn bộ 10 đặc vụ cùng Chỉ Huy cùng lúc tung mình nhảy bổ ra khỏi cửa hang! |  | Mười đặc vụ và Chỉ Huy cùng phi thân ra ngoài không trung trong một cú nhảy điện ảnh ngoạn mục, dưới ánh trăng vằng vặc; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b25 | 02:47.0–02:55.4 (8.4s) | L437 | ẦM! ĐOÀNG! Pháo Đài Tự Nhiên phát nổ sau lưng thành một quả cầu lửa khổng lồ rực sáng cả một góc trời, toàn bộ công sự bằng đá granite sụp đổ chôn vùi vĩnh viễn trong lòng đất! |  | Quả cầu lửa nổ tung rực rỡ phía sau lưng, khói bụi bốc cao ngùn ngụt soi sáng hình bóng mười đặc vụ đang lăn tròn tiếp đất an toàn trên sườn cỏ xanh mướt; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b26 | 02:55.4–03:03.6 (8.3s) | L438 | Toàn đội lấm lem bùn đất, nhưng không một ai bị thương nặng! Chiếc máy tính bảng của Chỉ Huy vang lên một tiếng bíp êm ái: "Điệp vụ hoàn tất 100 phần trăm! Toàn đội an toàn!" |  | Mười đặc vụ nằm thở hổn hển trên thảm cỏ xanh, nhìn ngọn lửa phía xa rồi nhìn nhau, đồng loạt bật cười sảng khoái và đập tay ăn mừng chiến thắng ngoạn mục! KHÔNG có anh Chỉ Huy trong cảnh này. |
| b27 | 03:03.6–03:07.7 (4.1s) | L439 | Biệt Đội Đặc Nhiệm Sinh Học đã sống sót qua phi vụ nghẹt thở nhất lịch sử! |  | Hình ảnh toàn đội đứng bên nhau ngắm ánh lửa xa xa, một cái kết mãn nhãn cho chiến dịch thế kỷ. |
| b28 | 03:07.7–03:14.6 (6.9s) | L440 | Từng giây phút trong cuộc tháo chạy nghẹt thở này là một bài học mẫu mực về tinh thần đoàn kết và sự phối hợp tác chiến đỉnh cao giữa các loài động vật! |  | Cảnh mười đặc vụ phối hợp nhịp nhàng vượt qua từng chướng ngại vật trong lòng pháo đài đang sụp lở; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b29 | 03:14.6–03:22.1 (7.5s) | L441 | Không có sự đố kỵ, không có sự phân biệt to nhỏ hay mạnh yếu, mỗi cá thể đều đem hết sở trường sinh học của mình ra để cứu lấy những người đồng đội! |  | Hình ảnh chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao chở các bạn nhỏ, chú Cá Voi Sát Thủ hoạt hình thân đen bóng bụng trắng tinh, vây lưng cao vút cắm ăng-ten định vị sonar nhỏ xíu, miệng cười nhếch mép kiểu trùm mafia biển cả dập lửa, chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc  |
| b30 | 03:22.1–03:29.0 (7.0s) | L442 | Cú nhảy ngoạn mục ra ngoài miệng vực trong tiếng nổ rung trời lở đất sẽ mãi mãi đi vào huyền thoại của những phi vụ giải cứu vĩ đại nhất giới sinh vật học! |  | Mười bóng đen đặc vụ in trên nền quả cầu lửa nổ tung rực sáng cả bầu trời đêm. |
| b31 | 03:29.0–03:35.5 (6.5s) | L443 | Những bước chân tháo chạy cuối cùng trên thảm cỏ xanh mướt là minh chứng cho sự kiên cường và lòng quả cảm phi thường của 10 đặc vụ sinh học! |  | Hình ảnh mười đặc vụ dìu nhau bước đi trên triền đồi hoa dại dưới ánh trăng thanh bình sau trận nổ kinh hoàng; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b32 | 03:35.5–03:40.9 (5.4s) | L444 | Pháo Đài Tự Nhiên đã sụp đổ, nhưng tinh thần đồng đội và những kỳ quan tiến hóa của họ sẽ sống mãi với thời gian! |  | Bầu trời đêm lấp lánh ngàn vì sao sáng, soi rọi con đường trở về căn cứ bình yên của biệt đội anh hùng; KHÔNG có anh Chỉ Huy trong cảnh này. |

### scene14 · ĐÓNG HỒ SƠ, CHIA THÙ LAO & HÉ LỘ HỒ SƠ MEGA 05 · 254.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.2 (7.2s) | L445 | Ánh bình minh đầu tiên của buổi sớm mai bắt đầu ló rạng trên đường chân trời, dát một màu vàng mật ong ấm áp lên khắp thung lũng xanh mướt. |  | Cảnh bình minh rạng rỡ sau cơn bão lửa, ánh mặt trời vàng ấm áp chiếu rọi thung lũng hoa dại thanh bình, xa xa là làn khói mờ ảo của pháo đài đã sụp đổ; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b02 | 00:07.2–00:12.9 (5.8s) | L446 | Căn phòng tác chiến ngầm dã chiến của Tổng Cục Mật Vụ lại rộn rã tiếng cười nói sau một đêm căng thẳng đến từng sợi tóc. |  | Căn phòng chỉ huy dã chiến bằng lều bạt thế giới tự nhiên ấm cúng, ánh đèn vàng ấm áp, bàn tác chiến đã được dọn sạch sẽ, bày biện các món ăn ngon; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b03 | 00:12.9–00:22.4 (9.5s) | L447 | Chỉ Huy Mật Vụ Cú Mèo cầm con dấu gỗ khắc nổi, nhúng vào khay mực đỏ tươi, đóng một phát thật mạnh xuống trang bìa của tập hồ sơ: CỘC! Dấu mực đỏ hiện rõ dòng chữ: HOÀN TẤT XUẤT SẮC — LƯU TRỮ TUYỆT MẬT! |  | Cận cảnh con dấu mực đỏ hình tròn "HOÀN TẤT XUẤT SẮC" in đậm nét trên bìa tập hồ sơ kraft vàng ngả bóng có ảnh chụp tập thể mười đặc vụ; anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm mỉm cười hài lòng. |
| b04 | 00:22.4–00:31.1 (8.7s) | L448 | "Các đặc vụ của tôi! Đêm nay, các bạn không chỉ hoàn thành một phi vụ bất khả thi, mà còn chứng minh cho toàn thế giới thấy sức mạnh vô song của sự sống và tình đồng đội!" |  | anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm nâng ly nước quả lên cao chúc mừng, mười đặc vụ đứng quây quần xung quanh vỗ tay reo hò rộn rã; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b05 | 00:31.1–00:35.0 (3.8s) | L449 | Biệt Đội Đặc Nhiệm Sinh Học đã hoàn thành xuất sắc nhiệm vụ được giao! |  | Toàn đội cùng nâng ly chúc mừng trong ánh sáng ban mai rực rỡ. |
| b06 | 00:35.0–00:41.2 (6.3s) | L450 | Và bây giờ là phần được mong chờ nhất trong mọi bộ phim điệp viên: lễ trao thù lao và giải tán lực lượng! |  | Mười chiếc hộp quà bọc giấy màu sắc rực rỡ xếp hàng dài trên bàn, mỗi hộp có dán một chiếc nhãn tên riêng biệt; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b07 | 00:41.2–00:49.2 (7.9s) | L451 | Đặc vụ Chuột Chũi Trũi được trao tặng ba bao tải khoai tây mật sấy bơ thượng hạng, cộng thêm một giấy chứng nhận: "Thợ đào hầm hảo hạng không bao giờ biết đau"! |  | chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên sung sướng ôm chặt bao khoai tây to tướng, hai chân trước vẫy vẫy, đeo chiếc huy chương bạc hình củ khoai tây lấp lánh trước ngực; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b08 | 00:49.2–00:56.2 (7.0s) | L452 | Đặc vụ Quạ Đen nhận một xô hạt dẻ rang bơ khổng lồ cùng một bộ kìm kẹp đa năng mạ vàng 24K để tha hồ chế tạo công cụ mới! |  | chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép ngậm chiếc kìm mạ vàng sáng loáng, đầu nghiêng ngả điệu đà, khoái chí cất tiếng kêu quạ quạ khoe khoang với cả đội; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b09 | 00:56.2–01:03.6 (7.4s) | L453 | Đặc vụ Chim Cắt Lớn được đền bù một bộ áo khoác da phi công hàng hiệu mới tinh, kèm một chiếc cà vạt lụa chống kiến cắn siêu bền! |  | chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng đứng trước gương chỉnh lại chiếc cà vạt lụa màu xanh hải quân mới toanh, vuốt lại bộ lông cánh bóng bẩy vẻ mặt vô cùng mãn nguyện; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b10 | 01:03.6–01:11.0 (7.4s) | L454 | Đặc vụ Ếch Gỗ Bắc Cực được quàng một chiếc khăn len đỏ ca-sơ-mia mềm mại chống rét âm 50°C, kèm một bình si-rô ngọt ngào bổ dưỡng! |  | chú Ếch Gỗ Bắc Cực hoạt hình da nâu vàng có vệt đen qua mắt như mặt nạ Zorro, đeo khăn quàng cổ đỏ thắm chống rét, người phủ lớp sương tuyết lấp lánh quàng chiếc khăn len đỏ mới tinh mỉm cười tít mắt, hai má phồng tròn rung rinh hạnh phúc; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b11 | 01:11.0–01:18.6 (7.6s) | L455 | Đặc vụ Cá Voi Sát Thủ nhận một tấm thẻ hội viên VIP bơi lội trọn đời tại toàn bộ các rạn san hô đẹp nhất thế giới, kèm một tấn cá hồi tươi rói! |  | chú Cá Voi Sát Thủ hoạt hình thân đen bóng bụng trắng tinh, vây lưng cao vút cắm ăng-ten định vị sonar nhỏ xíu, miệng cười nhếch mép kiểu trùm mafia biển cả nhô đầu lên khỏi bể nước ngậm một chú cá hồi tươi, vẫy vẫy chiếc thẻ VIP màu vàng kim trên vây ngực; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b12 | 01:18.6–01:25.1 (6.5s) | L456 | Đặc vụ Chim Gõ Kiến nhận một chiếc mũ bảo hộ bằng sợi các-bon siêu nhẹ có giảm chấn ba lớp, giúp anh chàng gõ đá mà êm như gõ gối bông! |  | chú Chim Gõ Kiến hoạt hình mào lông đỏ rực dựng đứng, mỏ dài sắc nhọn như mũi khoan titan, đội mũ bảo hộ lao động màu vàng có gắn đèn pin thợ mỏ đội chiếc mũ bảo hộ mới toanh bóng loáng, gõ mỏ lách cách vào mặt bàn để kiểm tra độ êm; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b13 | 01:25.1–01:32.8 (7.7s) | L457 | Lạc Đà Sa Mạc nhận một xe tải xương rồng non mọng nước đã được nhổ sạch gai, tha hồ nhai rôm rốp mà không sợ làm phiền bộ đàm của ai nữa! |  | chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao đứng nhai tóp tép đống xương rồng mọng nước ngọt ngào, miệng cười toe toét không chớp mắt; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b14 | 01:32.8–01:39.3 (6.5s) | L458 | Dê Núi Bắc Mỹ nhận bốn chiếc đệm móng guốc cao su thể thao hàng hiệu chống trượt tối tân để tha hồ leo vách đá 90°! |  | chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt giơ một móng trước lên khoe lớp đệm cao su mới tinh màu xanh lá cây đầy phong cách; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b15 | 01:39.3–01:45.5 (6.2s) | L459 | Chim Bách Thanh được trang bị một giàn gai thép không gỉ chuyên dụng gắn camera hành trình để bảo quản chiến lợi phẩm an |  | chú Chim Bách Thanh hoạt hình lông xám trắng có dải lông đen vắt ngang mắt như dải băng cướp biển, mỏ có móc câu sắc nhọn, chân cầm một nhánh gai nhọn công nghệ cắm một chiếc cúc áo lưu niệm lên giàn gai mới, mắt sáng lên đầy tự hào; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b16 | 01:45.5–01:54.2 (8.6s) | L460 | toàn! Và Đại Đội Kiến Cắt Lá được trao tặng một nông trại nấm hữu cơ ngầm rộng 500m² để phát triển nông nghiệp bền vững cho cả tổ kiến! |  | tiểu đội ba chú Kiến Cắt Lá hoạt hình màu nâu đỏ, đầu to mang hàm răng kim loại sáng loáng, đội mũ cối công binh màu xanh lá, đang vác những mảnh lá xanh như chiếc khiên chắn cùng nhau nâng một cây nấm khổng lồ màu trắng sữa diễu hành vòng quanh bàn tiệc ăn mừng rộn rã; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b17 | 01:54.2–02:02.4 (8.2s) | L461 | Mười quái kiệt, mười số phận kỳ lạ của tự nhiên đã hoàn thành sứ mệnh lịch sử. Họ lại quay trở về với bầu trời, rừng sâu, biển cả và lòng đất của riêng mình. |  | Hình ảnh chia tay đầy xúc động: mười đặc vụ lần lượt vẫy tay chào nhau, chim cắt tung cánh lên trời cao, cá voi bơi về biển lớn, dê núi sải bước lên đỉnh núi tuyết; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b18 | 02:02.4–02:09.6 (7.2s) | L462 | Nhưng những bài học tiến hóa kỳ diệu và tinh thần đồng đội của họ sẽ mãi mãi được lưu giữ trong kho tàng tri thức của kênh Vẽ Chuyện Hoang Dã. |  | Cuộn da cừu Bản Thiết Kế Tiến Hóa được đặt trang trọng trong lồng kính của thư viện tự nhiên, tỏa ánh sáng vàng kim êm đềm; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b19 | 02:09.6–02:15.4 (5.8s) | L463 | Căn phòng tác chiến trở lại yên tĩnh. Chỉ còn lại Chỉ Huy Mật Vụ Cú Mèo ngồi một mình bên bàn làm việc dưới ánh đèn bàn ấm áp. |  | anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm ngồi dựa lưng vào ghế xoay, khẽ tháo chiếc kính râm xuống để lộ đôi mắt tròn to sáng quắc đầy suy tư; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b20 | 02:15.4–02:20.7 (5.4s) | L464 | Anh chàng mở chiếc ngăn kéo bàn có khóa mật mã hai lớp, cẩn thận cất tập hồ sơ của Biệt Đội Đặc Nhiệm vào góc an toàn. |  | Chiếc ngăn kéo gỗ trượt mở, bên trong xếp ngay ngắn các tập hồ sơ mật của các mùa trước; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b21 | 02:20.7–02:29.7 (9.0s) | L465 | Và rồi, ngón tay của Chỉ Huy dừng lại ở một tập tài liệu bìa màu xanh phẫu thuật y tế còn niêm phong bằng sáp đỏ, có gắn dòng chữ cảnh báo: HỒ SƠ TỐI MẬT SỐ NĂM! |  | Bàn tay anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm nhấc một tập hồ sơ mới tinh màu xanh ngọc bích y khoa, trên bìa dán con dấu sáp đỏ hình ống nghe bác sĩ và nhịp tim điện tâm đồ; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b22 | 02:29.7–02:36.6 (6.9s) | L466 | Một nụ cười bí hiểm nở trên môi vị Chỉ Huy: "Trận chiến này vừa kết thúc... nhưng ca trực đêm kinh hoàng nhất của lịch sử tiến hóa thì chỉ mới bắt đầu." |  | Cận cảnh anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm mở hé phong bì niêm phong, ánh sáng xanh lơ lạnh lẽo từ bên trong hồ sơ hắt lên khuôn mặt; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b23 | 02:36.6–02:44.0 (7.4s) | L467 | Đêm nay, tại Bệnh Viện Đa Khoa Tiến Hóa, mười bệnh nhân mang những triệu chứng sinh học trái ngược hoàn toàn với quy luật thông thường đang đồng loạt nhập viện cấp cứu! |  | Tranh vẽ phong cách Vintage Hospital thập niên 1950: hành lang bệnh viện dã chiến đêm khuya với các bóng đen bệnh nhân kỳ dị đang nằm trên cáng và xe lăn; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b24 | 02:44.0–02:53.2 (9.1s) | L468 | Một chú Nhện Lặn Chuông tự dệt bình dưỡng khí bằng tơ để thở dưới nước. Một chú Cá Thoi Loi trèo cây hít thở bằng da. Một nàng Ong Bắp Cày Ngọc cầm dao phẫu thuật điều khiển não gián. |  | Ba bức hình phác thảo y khoa đen trắng: chú nhện ôm bọc bong bóng nước, chú cá nhảy nhót trên rễ cây đước và chú ong đang châm ngòi nọc chính xác vào hạch thần kinh gián; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b25 | 02:53.2–03:00.8 (7.6s) | L469 | Một chú Cá Mặt Trăng ba tấn không não trôi dạt giữa đại dương. Và một chú Vẹt Ca-ca-pô béo ú quên mất cách bay, đêm đêm nhảy từ ngọn cây xuống đất tìm bạn đời! |  | Hai bức phác thảo tiếp theo: chú cá mặt trăng tròn vo khổng lồ nằm ngửa phơi nắng và chú vẹt mập ú màu xanh lá đang vụng về leo cây; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b26 | 03:00.8–03:09.2 (8.5s) | L470 | Cùng với Lợn Rừng Ba-bi-ru-sa mang răng nanh tự đâm sọ, Hươu Cao Cổ huyết áp 300, Cò Mỏ Giày đứng như tượng đá và Nhím Lông Nhọn mang 30.000 chiếc gai! |  | Bức ảnh ghép tổng thể mười bệnh nhân kỳ dị của phòng cấp cứu tiến hóa; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b27 | 03:09.2–03:16.1 (6.9s) | L471 | Hẹn gặp lại quý vị khán giả trong Mega số năm: Phòng Cấp Cứu Tạo Hóa — Ca Trực Đêm Kinh Hoàng của mười bệnh nhân tiến hóa kỳ lạ nhất hành tinh! |  | Màn hình hiện lên dòng chữ hẹn ước đầy tò mò với hình ảnh chiếc ống nghe y tế và bóng lưng bác sĩ trưởng khoa bước vào phòng mổ; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b28 | 03:16.1–03:25.3 (9.2s) | L472 | Còn bây giờ, nếu bạn được quyền tuyển chọn một đặc vụ trong Biệt Đội Đặc Nhiệm Sinh Học tối nay làm bạn đồng hành, bạn sẽ chọn quái kiệt nào? Hãy để lại mật mã của bạn ở phần bình luận bên dưới nhé! |  | Mười đặc vụ cùng xếp hàng chào khán giả trên màn hình kết thúc, vẫy tay và nháy mắt tinh nghịch; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b29 | 03:25.3–03:36.9 (11.6s) | L473 | Đừng quên bấm thích video, đăng ký kênh Vẽ Chuyện Hoang Dã và nhấn chuông thông báo để không bỏ lỡ những phi vụ sinh tồn chấn động tiếp theo. Chúc các bạn một giấc ngủ thật ngon và những giấc mơ phiêu lưu tuyệt đẹp! |  | Logo kênh Vẽ Chuyện Hoang Dã hiện lên rực rỡ cùng các nút bấm đăng ký hoạt hình ngộ nghĩnh, ánh đèn mờ dần khép lại một đêm phi vụ thế kỷ hoàn hảo. |
| b30 | 03:36.9–03:45.0 (8.1s) | L474 | Bệnh Viện Đa Khoa Tiến Hóa trong Mega số năm hứa hẹn sẽ mang đến những câu chuyện y khoa hài hước và kỳ thú chưa từng có về mười sinh vật mang thiết kế ngược đời nhất hành tinh! |  | Hình ảnh phác thảo hài hước về phòng khám bệnh viện tiến hóa với bác sĩ trưởng khoa đang khám bệnh cho chú cá mặt trăng ba tấn nằm trên giường cấp cứu; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b31 | 03:45.0–03:56.1 (11.1s) | L475 | Quý vị sẽ được giải mã vì sao chú vẹt Kakapo béo ú lại quên cách bay, vì sao chú lợn rừng Babirusa lại có răng nanh tự đâm vào sọ, và vì sao hươu cao cổ cúi đầu uống nước mà không bị vỡ mạch máu não! |  | Tranh vẽ mười ca bệnh kỳ lạ xếp hàng trước cửa phòng khám cấp cứu tiến hóa; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b32 | 03:56.1–04:01.1 (5.0s) | L476 | Hãy tiếp tục đồng hành cùng kênh Vẽ Chuyện Hoang Dã để khám phá những điều kỳ diệu bất tận của thế giới tự nhiên xung quanh |  | Mười đặc vụ của Mega 04 cùng vẫy tay chào tạm biệt khán giả trong tiếng nhạc điệp viên vui nhộn và hào hùng. |
| b33 | 04:01.1–04:08.8 (7.6s) | L477 | chúng ta! Mỗi một tập phim của kênh Vẽ Chuyện Hoang Dã là một hành trình kỳ thú đưa quý vị khán giả đến với những bí mật chưa từng được kể của muôn loài! |  | Logo kênh phát sáng lung linh giữa bầu trời đêm đầy sao, các nhân vật hoạt hình ngộ nghĩnh cùng vẫy tay chào khán giả; KHÔNG có anh Chỉ Huy trong cảnh này. |
| b34 | 04:08.8–04:14.7 (6.0s) | L478 | Hãy chuẩn bị tinh thần cho những ca trực đêm nghẹt thở và những chẩn đoán y khoa cười ra nước mắt trong mùa phim tiếp theo nhé! |  | Chiếc xe cứu thương hoạt hình của Bệnh Viện Tiến Hóa lăn bánh vào màn đêm, nhấp nháy đèn xanh báo hiệu một hành trình mới đầy hấp dẫn. |

## 5. Phân cảnh Shorts — từng beat

Banner: **BIỆT ĐỘI ĐẶC NHIỆM / PHI VỤ THẾ KỶ** · giọng 53.0s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Mười đặc vụ quái kiệt. Bảy cửa ải an ninh. Một phi vụ thế kỷ đột nhập Pháo Đài Tự Nhiên! |  |
| s02 | 00:04.5 | S02 | Cửa Ải 1: Chim Cắt Lớn bổ nhào xé gió 389 km/h vô hiệu hóa lưới laser! | **389 KM/H** · Bổ nhào kỷ lục · R/640 · [0.5, 0.55] |
| s03 | 00:08.8 | S03 | Cửa Ải 2: Chuột Chũi Trũi thở bằng đường hoa quả sống sót 18 phút ở mức 0% oxy! | **18 PHÚT** · Sống ở 0% Oxy · L/620 · [0.5, 0.5] |
| s04 | 00:13.9 | S04 | Cửa Ải 3: Ếch Gỗ Bắc Cực chủ động đóng băng 65% cơ thể, tim ngừng đập qua mặt cảm biến tầm nhiệt! | **65% NƯỚC** · Đóng băng cơ thể · R/640 · [0.5, 0.55] |
| s05 | 00:19.1 | S05 | Cửa Ải 4: Quạ Đen dùng trí tuệ giải mã chuỗi bẫy cơ học 8 bước và lóa mắt camera an ninh! |  |
| s06 | 00:23.8 | S06 | Cửa Ải 5: Cá Voi Sát Thủ bắn xung sonar 225 dB quất sóng thần phá đập nước ngầm! | **225 DB** · Xung Sonar đỉnh · L/620 · [0.5, 0.5] |
| s07 | 00:28.6 | S07 | Cửa Ải 6: Chim Gõ Kiến triệt tiêu 1200G cùng Đại Đội Kiến Cắt Lá dùng răng thép đục sập boong-ke! | **1200G** · Lực chịu va đập · R/640 · [0.5, 0.55] |
| s08 | 00:33.8 | S08 | Cửa Ải 7: Dê Núi phi thân leo vách đứng 90° và Lạc Đà vượt sa mạc 50°C hạ cầu treo! | **VÁCH 90°** · Móng giác hút · L/620 · [0.5, 0.5] |
| s09 | 00:38.7 | S09 | Và kho báu tối thượng là gì? Không phải vàng bạc, mà là kiệt tác tiến hóa nằm ngay trong chính bản thân mỗi loài! |  |
| s10 | 00:44.5 | S10 | Bạn ấn tượng với siêu năng lực của đặc vụ nào nhất? Xem trọn bộ phi vụ thế kỷ trong video dài nhé, |  |
| s11 | 00:49.0 | S11 | vì ở đây chỉ có 10 đặc vụ quái kiệt, 7 cửa ải sinh tử, và một phi vụ thế kỷ! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một căn hầm ngầm bê tông tối om dưới lòng đất sâu 100 mét. Chỉ có ánh sáng xanh lục từ chiếc máy chiếu hologram quét chầm chậm qua các góc phòng.". Bố cục: Căn phòng tác chiến ngầm tối tân phong cách Cold War thập niên 1960 với tường bê tông xám, màn hình radar xanh lục quét vòng tròn, anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm đứng quay lưng lại nhìn tấm bản đồ phát sáng.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chào mừng toàn thể các điệp viên đến với Tổng Cục Tiến Hóa Tối Mật. Nếu các bạn nghe được tín hiệu này, có nghĩa là phi vụ thế kỷ đã chính thức bắt đầu.". Bố cục: Cận cảnh anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm từ từ xoay người lại, bàn tay vuốt chỉnh ve áo măng-tô đen, chiếc kính râm phản chiếu các dòng dữ liệu mật mã màu xanh lục lướt qua mặt kính.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trước mặt chúng ta là mục tiêu tối thượng chưa từng có sinh vật nào xuyên thủng được suốt 500 triệu năm qua: Pháo Đài Tự Nhiên.". Bố cục: bản đồ hologram 3D của Pháo Đài Tự Nhiên nổi lơ lửng trong không khí, hiển thị 7 cửa ải an ninh phát sáng đỏ và thanh tiến độ phá khóa màu xanh ngọc (không có chữ, không có số) bật sáng rực rỡ giữa phòng, mô hình 3D của một pháo đài khổng lồ bằng đá granite đen và băng tuyết bao quanh thung lũng hiểm trở, có bảy vòng rào an ninh nhấp nháy đỏ rực.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nơi đây giấu kín Bản Thiết Kế Tiến Hóa Tối Thượng, cội nguồn sức mạnh của toàn bộ giới sinh vật trên Trái Đất.". Bố cục: Cận cảnh mô hình hologram thu nhỏ của cuộn tài liệu phát sáng vàng kim lơ lửng giữa tâm điểm pháo đài, bao quanh là các lớp lưới bảo vệ; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng để chạm tới chiếc két sắt trung tâm, Biệt Đội Đặc Nhiệm Sinh Học phải vượt qua 7 cửa ải an ninh sinh tử kiên cố nhất.". Bố cục: Bảy biểu tượng cửa ải lần lượt chớp sáng trên bản đồ: vòi rồng gió lốc, đường hầm yếm khí, hầm băng vĩnh cửu, mê cung bẫy rập, hào nước áp lực cao, boong-ke bê tông và vách đá dựng đứng; anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm chỉ đầu ngón tay vào từng vị trí.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và để giải mã bảy cánh cửa bất khả thi này, tôi đã đích thân tuyển chọn 10 đặc vụ bất hảo và quái kiệt nhất hành tinh. Không một ai trong số họ là kẻ tầm thường.". Bố cục: Mười tập hồ sơ tài liệu mật bìa giấy kraft ngả vàng xếp xòe hình cánh quạt trên mặt bàn kim loại, trên mỗi bìa có dán một bức ảnh chân dung đen trắng và đóng dấu mực đỏ TỐI MẬT; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đặc vụ 01! Mật danh Tia Chớp Bầu Trời, kẻ sở hữu vũ khí xuyên phá hàng rào laser trên không: Chim Cắt Lớn!". Bố cục: chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng bước vào phòng họp, mặc áo giáp phi công siêu thanh, đeo kính bảo hộ trên trán, một tay kéo khóa áo khoác da, ánh mắt sắc lẹm như lưỡi dao cạo; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hồ sơ tác chiến ghi rõ: anh chàng này từng đạt tốc độ bổ nhào xé gió 389 km/h, nhanh hơn cả một chiếc siêu xe đua Công Thức Một!". Bố cục: Bức ảnh tư liệu mật chụp chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng đang lao vun vút trên nền trời xanh, bên cạnh có đồ thị tốc độ nhảy vọt lên đỉnh cao nhất; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đặc vụ 02! Mật danh Bóng Ma Hầm Ngầm, chuyên gia thâm nhập các địa đạo không có không khí và đầy sương axit: Chuột Chũi Trũi!". Bố cục: chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên chui tọt từ một nắp cống ngầm dưới sàn nhà lên, hai răng cửa to chìa ra ngoài, đẩy chiếc kính nhìn đêm hồng ngoại to bản lên mũi, ngơ ngác nhìn quanh; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sinh vật không lông này có thể sống phây phây 18 phút không cần oxy, và hoàn toàn miễn nhiễm với mọi cảm giác đau đớn do axit gây ra!". Bố cục: Bản chụp X-quang sinh học của chuột chũi trũi với các biểu tượng lá chắn chống axit và biểu tượng tim đập bền bỉ trong môi trường yếm khí; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L100</summary>

```text
HÌNH L100 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Rắc! Chiếc chốt khóa bằng đồng thau bị cắn đứt đôi! Chuột chũi không hề nuốt phải một hạt bụi kim loại nào vì môi của anh chàng khép kín phía sau răng!". Bố cục: Chiếc then cài kim loại gãy vụn rơi lanh canh, chiếc van xoay tròn mở bung ra, luồng không khí sạch bên ngoài ùa vào đường hầm rào rào; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L101</summary>

```text
HÌNH L101 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đèn báo động đỏ chuyển sang màu xanh lá dịu mát! Hệ thống hút chân không bị vô hiệu hóa! Cửa Ải 2 đã được dọn sạch hoàn toàn!". Bố cục: Màn hình trung tâm bản đồ hologram 3D của Pháo Đài Tự Nhiên nổi lơ lửng trong không khí, hiển thị 7 cửa ải an ninh phát sáng đỏ và thanh tiến độ phá khóa màu xanh ngọc (không có chữ, không có số) phát ra âm thanh êm dịu, biểu tượng đường ống yếm khí chuyển sang màu xanh ngọc, thanh tiến độ phá khóa nhảy lên nấc thứ hai; anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm khẽ mỉm cười gật đầu.
```
</details>

<details><summary>L102</summary>

```text
HÌNH L102 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chuột Chũi Trũi ngoi đầu lên từ một lỗ thông gió ở sàn tầng trệt, giơ hai chân trước phủi mũi, phát ra một tiếng rít vui tai qua bộ đàm.". Bố cục: chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên ló đầu lên mặt sàn đá sạch sẽ, giơ hai móng trước làm dấu chiến thắng, cặp kính nhìn đêm hồng ngoại lóe lên ánh sáng xanh tinh nghịch.
```
</details>

<details><summary>L103</summary>

```text
HÌNH L103 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng ngay khi cửa mở ra, một luồng khí lạnh buốt xương tủy bất ngờ ùa tới từ cánh cửa hành lang tiếp theo, làm đóng băng ngay lập tức những giọt nước đọng trên sàn đá!". Bố cục: Hơi sương lạnh buốt màu trắng xóa tràn qua khe cửa hầm, mặt sàn đá đóng một lớp băng trơn nhẵn bóng, các nhũ băng nhọn hoắt rủ xuống từ trần nhà; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L104</summary>

```text
HÌNH L104 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cửa Ải 3: Kho Lạnh Cực Hạn với nhiệt độ -20°C và hệ thống cảm biến hồng ngoại tầm nhiệt tinh vi nhất thế giới!". Bố cục: Bản đồ bản đồ hologram 3D của Pháo Đài Tự Nhiên nổi lơ lửng trong không khí, hiển thị 7 cửa ải an ninh phát sáng đỏ và thanh tiến độ phá khóa màu xanh ngọc (không có chữ, không có số) hiển thị căn phòng tiếp theo phủ đầy hoa tuyết màu xanh băng giá, các máy quét thân nhiệt màu đỏ cam đang lia khắp sàn nhà; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L105</summary>

```text
HÌNH L105 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mọi cơ thể ấm áp bước vào đây sẽ bị phát hiện trong vòng nửa giây. Chỉ có một sinh vật có thể biến mình thành một tảng băng vô tri vô giác để vượt qua cửa ải này.". Bố cục: Cận cảnh anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm quay sang nhìn chú Ếch Gỗ Bắc Cực hoạt hình da nâu vàng có vệt đen qua mắt như mặt nạ Zorro, đeo khăn quàng cổ đỏ thắm chống rét, người phủ lớp sương tuyết lấp lánh đang bình thản nhấp một ngụm nước đá trong góc phòng.
```
</details>

<details><summary>L106</summary>

```text
HÌNH L106 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: ""Đặc vụ Ếch Gỗ Bắc Cực, đã đến lúc cho cả pháo đài thấy thế nào là nghệ thuật ngủ đông bất tử!"". Bố cục: chú Ếch Gỗ Bắc Cực hoạt hình da nâu vàng có vệt đen qua mắt như mặt nạ Zorro, đeo khăn quàng cổ đỏ thắm chống rét, người phủ lớp sương tuyết lấp lánh thắt lại chiếc khăn quàng cổ màu đỏ, bước ra ánh đèn, đôi mắt tròn to lấp lánh sự tự tin của một chuyên gia sinh tồn vùng cực.
```
</details>

<details><summary>L107</summary>

```text
HÌNH L107 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và phía sau lưng, tiếng cãi cọ qua kênh bộ đàm bắt đầu bùng nổ, báo hiệu một sự cố hài hước không thể lường trước!". Bố cục: Chiếc máy bộ đàm trên bàn tác chiến nhấp nháy đèn vàng báo hiệu cuộc gọi khẩn cấp từ các đặc vụ hậu trường.
```
</details>

<details><summary>L108</summary>

```text
HÌNH L108 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kỳ tích chuyển hóa đường fructose của Chuột Chũi Trũi đang mở ra một cuộc cách mạng y học lớn trong việc điều trị các bệnh nhân bị nhồi nước màu cơ tim và đột quỵ do thiếu oxy!". Bố cục: Tranh vẽ nghiên cứu y khoa hiện đại: hình ảnh trái tim người được bảo vệ bởi cơ chế chuyển hóa đường fructose mô phỏng từ chuột chũi; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L109</summary>

```text
HÌNH L109 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi oxy cạn kiệt, các tế bào tim của chuột chũi không hề bị co thắt hay hoại tử, mà vẫn đập êm ả nhờ dòng năng lượng fructose ngọt ngào!". Bố cục: Mô phỏng các tế bào cơ tim chuột chũi co bóp đều đặn dưới ánh sáng huỳnh quang y tế; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đặc vụ 03! Mật danh Điệp Viên Băng Giá, sinh vật duy nhất có khả năng tự biến mình thành tảng băng để đánh lừa cảm biến tầm nhiệt: Ếch Gỗ Bắc Cực!". Bố cục: chú Ếch Gỗ Bắc Cực hoạt hình da nâu vàng có vệt đen qua mắt như mặt nạ Zorro, đeo khăn quàng cổ đỏ thắm chống rét, người phủ lớp sương tuyết lấp lánh bước ra từ trong làn sương mù lạnh buốt, quấn chiếc khăn len đỏ chót quanh cổ, trên da đọng những hạt sương băng lấp lánh như kim cương; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L110</summary>

```text
HÌNH L110 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cơ thể không lông của chúng còn chứa một loại gen đặc biệt giúp sửa chữa tế bào thần kinh với tốc độ nhanh gấp năm lần các loài chuột thông thường!". Bố cục: Chuỗi xoắn kép ADN của chuột chũi phát sáng các điểm liên kết tự phục hồi màu xanh ngọc bích; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L111</summary>

```text
HÌNH L111 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhờ tốc độ tiêu thụ đường fructose cực kỳ chậm rãi, chuột chũi có thể duy trì hoạt động của các cơ quan bên trong cơ thể mà không hề tạo ra độc tố axit lactic gây mỏi cơ!". Bố cục: Kính hiển vi hiển thị tế bào cơ chuột chũi không hề tích tụ axit lactic sau mười tám phút vận động trong buồng chân không; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L112</summary>

```text
HÌNH L112 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đặc vụ Chuột Chũi Trũi quệt mồ hôi trên mũi, nở một nụ cười rạng rỡ của một nhà quán quân sinh tồn không biết mệt mỏi!". Bố cục: chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên giơ hai ngón chân trước lên làm dấu chữ V chiến thắng trước ống kính camera thông hơi; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L113</summary>

```text
HÌNH L113 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Điệp vụ thế kỷ tưởng chừng như đang diễn ra hoàn hảo đến từng tích tắc... thì kênh bộ đàm nội bộ bắt đầu phát ra những âm thanh cực kỳ bất thường.". Bố cục: Căn phòng chỉ huy của anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm, chiếc máy bộ đàm để bàn bắt đầu phát ra những tiếng rè rè lẹt xẹt, xen lẫn tiếng nhai nhồm nhoàm và tiếng cãi cọ ầm ĩ; anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm ôm trán thở dài bất lực.
```
</details>

<details><summary>L114</summary>

```text
HÌNH L114 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tiếng nhai chóp chép giòn tan vang lên rành rọt qua chiếc loa điều khiển trung tâm, to đến mức át cả tiếng còi báo động của pháo đài!". Bố cục: Chiếc loa truyền tin phóng đại sóng âm thanh dạng răng cưa, các nhân viên kỹ thuật đeo tai nghe phải nhăn mặt giật tai nghe ra; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L115</summary>

```text
HÌNH L115 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: ""Báo cáo Chỉ Huy! Tôi vừa đột nhập thành công vào phòng chứa tài liệu bí mật! Nhưng ở đây không có tài liệu... chỉ có toàn là khoai tây sấy bơ thơm lừng!"". Bố cục: chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên ngồi lọt thỏm giữa một kho lương thực đầy ắp các bao tải ngũ cốc và củ quả của pháo đài, hai tay ôm một củ khoai tây to gấp đôi người mình, mải mê gặm lấy gặm để; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L116</summary>

```text
HÌNH L116 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khoai tây này ngọt lắm sếp ơi! Có cần tôi vận chuyển về phòng chỉ huy năm bao làm quà lưu niệm cho Biệt Đội Đặc Nhiệm Sinh Học không ạ?". Bố cục: Cận cảnh chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên mồm dính đầy vụn khoai tây, hai mắt hí tít sau cặp kính nhìn đêm, giơ củ khoai tây lên vẫy vẫy trước camera; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L117</summary>

```text
HÌNH L117 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sau phi vụ này tôi định mở một chuỗi nhà hàng khoai nướng yếm khí dưới lòng đất, sếp nhớ đến cắt băng khánh thành nhé!". Bố cục: chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên giơ một ngón chân cái lên làm dáng quảng cáo nhà hàng tương lai đầy tự tin; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L118</summary>

```text
HÌNH L118 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chỉ Huy Mật Vụ hít một hơi thật sâu, giọng lạnh như băng truyền qua mic: "Đặc vụ Chuột Chũi... cậu vừa đào nhầm vào kho bếp của bảo vệ pháo đài rồi đấy."". Bố cục: Cận cảnh anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm nghiến răng, chiếc kính râm trượt xuống sống mũi để lộ ánh mắt hình viên đạn, ngón tay gõ nhịp lách cách đe dọa lên micro; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L119</summary>

```text
HÌNH L119 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: ""Nếu trong vòng 30 giây nữa cậu không kéo cái thân nhăn nheo của mình ra khỏi kho khoai tây, tôi sẽ ghi tên cậu vào danh sách cắt khẩu phần ăn ba tháng!"". Bố cục: anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm cầm cây bút lông đỏ vạch một đường thật đậm vào trang hồ sơ có dán ảnh chuột chũi trũi; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Anh chàng có thể để 65% cơ thể đóng băng cứng ngắc suốt 7 tháng mùa đông, tim ngừng đập hoàn toàn mà vẫn hồi sinh nguyên vẹn!". Bố cục: Đồ họa y tế mô phỏng chú ếch gỗ nằm ngủ đông dưới lớp tuyết dày, các phân tử đường glucose bảo vệ tế bào phát sáng màu hổ phách; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L120</summary>

```text
HÌNH L120 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: ""Và đừng bao giờ mơ đến chuyện mở nhà hàng khoai nướng khi đang trong giờ làm việc của Tổng Cục!"". Bố cục: anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm đập cây bút lông xuống bàn làm mực đỏ bắn tung tóe lên mặt bàn kính; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L121</summary>

```text
HÌNH L121 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ối sếp ơi! Tôi đi ngay đây! Nhưng cho tôi xin nhét thêm một củ nhỏ vào túi áo khoác nhé!". Bố cục: chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên giật mình nhảy cẫng lên, vội vã nhét vội một củ khoai tây vào túi thắt lưng rồi cong đuôi lặn mất tăm xuống lỗ đất vừa đào; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L122</summary>

```text
HÌNH L122 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa kịp thở phào thì một tiếng rít chói tai khác lại chèn ngang vào tần số liên lạc tối mật. Lần này là giọng nói đanh đá và đậm chất con buôn của Quạ Đen!". Bố cục: chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép xuất hiện trên màn hình camera phụ, đang dùng một chiếc móng chân gảy gảy vào mic bộ đàm, chiếc mỏ kẹp một tập giấy ghi chép chi phí; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L123</summary>

```text
HÌNH L123 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "A lô Chỉ Huy nghe rõ không? Kênh mã hóa này tín hiệu tốt đấy! Tiện thể tôi xin gửi báo cáo tài chính cập nhật trước khi bước vào Cửa Ải 3 và Cửa Ải 4!". Bố cục: Cận cảnh chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép nghiêng đầu chớp mắt tinh quái, tay kia xòe ra một tờ hóa đơn thanh toán dài ngoằng vẽ nguệch ngoạc bằng mực tím; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L124</summary>

```text
HÌNH L124 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hợp đồng ban đầu chỉ ghi giải mã ba cái ổ khóa cơ học đơn giản. Đằng này toàn là bẫy gương tâm lý với khóa liên hoàn 8 bước của các kỹ sư thiên tài!". Bố cục: chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép chỉ mỏ vào sơ đồ bẫy rập phức tạp trên màn hình, vẻ mặt đầy bất mãn đòi quyền lợi chính đáng của một chuyên gia công nghệ; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L125</summary>

```text
HÌNH L125 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tôi yêu cầu tăng lương gấp đôi! Cộng thêm điều khoản bảo hiểm gãy mỏ khi tác chiến và một thùng hạt dẻ thượng hạng! Nếu không thì tự đi mà giải mã mê cung nhé!". Bố cục: chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép khoanh hai cánh trước ngực quay lưng lại camera, làm bộ dỗi hờn không thèm hợp tác; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L126</summary>

```text
HÌNH L126 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Toàn bộ phòng chỉ huy rơi vào im lặng sượng sùng. Chỉ Huy Cú Mèo từ từ với tay lấy một tập hồ sơ có dán nhãn đỏ: "Hồ sơ quậy phá nơi công cộng của Quạ Đen".". Bố cục: anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm thong thả mở tập hồ sơ dày cộp, bên trong có dán ảnh chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép đang trộm bóng đèn xe cảnh sát và trêu chọc chó nhà hàng xóm; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L127</summary>

```text
HÌNH L127 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: ""Đặc vụ Quạ Đen, cậu có muốn tôi nhắc lại vụ án trộm mất 60 chiếc thìa bạc tại dinh thự thị trưởng năm ngoái không?"". Bố cục: anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm cầm kính lúp soi vào bức ảnh đen trắng chụp chiếc tổ quạ chứa đầy thìa nĩa bằng bạc lấp lánh; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L128</summary>

```text
HÌNH L128 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: ""Bằng chứng vẫn còn nằm nguyên trong két sắt của tôi đấy. Nếu phi vụ này thành công, hồ sơ đó sẽ biến mất trong lò thiêu hủy. Cậu thấy mức lương đó đã đủ hấp dẫn chưa?"". Bố cục: anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm khẽ cười nửa miệng, quẹt que diêm dí sát vào góc tập hồ sơ làm mép giấy hơi bén lửa; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L129</summary>

```text
HÌNH L129 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ấy ấy Chỉ Huy bình tĩnh! Đùa tí cho không khí bớt căng thẳng thôi mà! Làm gì mà nóng tính thế! Tôi đang chuẩn bị sẵn bộ đồ nghề phá khóa rồi đây!". Bố cục: chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép hoảng hốt xua xua đôi cánh, mồm liến thoắng cười trừ, nhanh tay giấu nhẹm tờ hóa đơn vào trong túi áo; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đặc vụ 04! Mật danh Bộ Não Cơ Học, bậc thầy giải mã các chuỗi khóa bẫy đa bước phức tạp nhất: Quạ Đen!". Bố cục: chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép bay lượn sà xuống đậu trên lưng ghế kim loại, mỏ quắp chiếc kìm cắt dây thép siêu nhỏ, ánh mắt láu cá liếc ngang liếc dọc tìm ống kính quan sát hoạt hình vui nhộn; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L130</summary>

```text
HÌNH L130 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đúng lúc đó, Chim Cắt Lớn cũng chêm vào một câu qua sóng vô tuyến: "Đề nghị mọi người nói nhỏ giùm! Gió trên đỉnh tháp vừa làm bay mất một sợi lông đuôi quý giá của tôi rồi đây này!"". Bố cục: chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng đứng trên cột cờ tháp canh đang bận rộn dùng mỏ chải chuốt lại từng sợi lông vũ trên cánh, vẻ mặt cằn nhằn vì phong độ bị ảnh hưởng; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L131</summary>

```text
HÌNH L131 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: ""Đồng đội gì mà người thì mê ăn khoai, kẻ thì đòi tăng lương, làm mất hết cả hình tượng điệp viên ngầu lòi của tôi!" Chim Cắt phụng phịu lắc đầu.". Bố cục: chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng soi bóng mình vào kính bảo hộ phi công, vuốt lại chùm lông đầu cho thật mượt mà; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L132</summary>

```text
HÌNH L132 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Dưới bể nước dã chiến, Cá Voi Sát Thủ phun lên một cột nước cao 3 mét qua lỗ thở, phát ra tiếng cười khùng khục qua mic: "Mấy đứa trên cạn ồn ào quá! Bao giờ mới đến lượt đại ca biển cả ra tay đây?"". Bố cục: chú Cá Voi Sát Thủ hoạt hình thân đen bóng bụng trắng tinh, vây lưng cao vút cắm ăng-ten định vị sonar nhỏ xíu, miệng cười nhếch mép kiểu trùm mafia biển cả nhấp nhô vây lưng trên mặt nước, ngoác miệng cười để lộ hàm răng trắng bóng, đập vây đuôi tạo thành những đợt sóng dập dềnh; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L133</summary>

```text
HÌNH L133 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Dê Núi và Lạc Đà cũng tranh thủ nhảy vào kênh chat tổng bàn tán về việc loại cỏ sa mạc nào ngọt hơn cỏ trên núi tuyết!". Bố cục: chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt và chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao cùng chia sẻ một cành cỏ khô qua màn hình chia đôi, vừa nhai vừa gật gù tâm đắc; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L134</summary>

```text
HÌNH L134 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chỉ Huy Mật Vụ gõ ngón tay xuống bàn ba tiếng cộc cộc cộc để lập lại trật tự: "Đủ rồi! Tất cả chuyển sang kênh tác chiến im lặng!"". Bố cục: anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm chỉnh lại micro cổ áo, ánh mắt trở lại vẻ uy nghiêm sắt đá của một thủ lĩnh mật vụ; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L135</summary>

```text
HÌNH L135 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sự hài hước chấm dứt ngay khi cánh cửa ngăn cách Cửa Ải 3 từ từ nâng lên. Hơi lạnh -20°C tràn ra ngoài làm ngưng đọng toàn bộ hơi nước thành những bông hoa tuyết rơi lả tả.". Bố cục: Cánh cửa thép dày ba tấc phủ đầy băng giá mở ra, bên trong là một căn phòng lạnh thấu xương với ánh sáng xanh lam ma quái phản chiếu từ những bức tường băng vĩnh cửu; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L136</summary>

```text
HÌNH L136 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đây không phải là chỗ để đùa giỡn nữa. Bất kỳ một bước chân sai lầm nào cũng sẽ biến cơ thể thành một bức tượng đá vĩnh cửu.". Bố cục: Các cảm biến hồng ngoại trên tường quét những chùm tia sáng vô hình qua lại như những mạng nhện tử thần giăng kín lối đi; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L137</summary>

```text
HÌNH L137 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đặc vụ Ếch Gỗ Bắc Cực đã bước vào phòng lạnh. Chiếc khăn quàng đỏ tung bay trong gió tuyết, ánh mắt anh chàng kiên định nhìn thẳng vào tâm điểm bẫy nhiệt độ.". Bố cục: chú Ếch Gỗ Bắc Cực hoạt hình da nâu vàng có vệt đen qua mắt như mặt nạ Zorro, đeo khăn quàng cổ đỏ thắm chống rét, người phủ lớp sương tuyết lấp lánh đứng trước ngưỡng cửa hầm băng, hít một hơi thật sâu làn không khí buốt giá, chuẩn bị bước vào cuộc thử nghiệm sinh học kỳ diệu nhất trong lịch sử sinh tồn.
```
</details>

<details><summary>L138</summary>

```text
HÌNH L138 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sinh mệnh của cả biệt đội đang nằm trong bàn tay của chú ếch nhỏ bé này!". Bố cục: Cận cảnh bàn chân có màng của chú Ếch Gỗ Bắc Cực hoạt hình da nâu vàng có vệt đen qua mắt như mặt nạ Zorro, đeo khăn quàng cổ đỏ thắm chống rét, người phủ lớp sương tuyết lấp lánh chạm nhẹ vào mặt băng buốt giá, chuẩn bị cho màn trình diễn đóng băng hồi sinh thần kỳ.
```
</details>

<details><summary>L139</summary>

```text
HÌNH L139 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: ""Báo cáo Chỉ Huy, tôi vừa phát hiện thêm một bao hạt dẻ rang muối ở góc bếp! Tôi có thể mang theo để phòng khi đói bụng không ạ?"". Bố cục: chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên thò đầu ra từ bao hạt dẻ, hai má phồng to như hai chiếc bánh bao nhỏ; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tài liệu của viện nghiên cứu khẳng định: bộ não của quạ đen có thể tự giải các câu đố logic cơ học 8 bước liên hoàn trong vòng 30 giây mà không cần dạy trước!". Bố cục: Sơ đồ tư duy phức tạp của loài quạ với các khớp nối logic công cụ và hình ảnh chiếc que sắt được uốn cong thành lưỡi câu; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L140</summary>

```text
HÌNH L140 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Quạ Đen lập tức nhảy vào can thiệp: "Chia đôi! Nếu không tôi sẽ báo cáo lên Tổng Cục về tội danh ăn vụng quân lương của cậu!"". Bố cục: chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép giơ chiếc kìm mạ vàng lên gõ lách cách đòi chia phần chiến lợi phẩm; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L141</summary>

```text
HÌNH L141 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Dê Núi Bắc Mỹ thở dài qua mic: "Mấy người suốt ngày chỉ nghĩ đến ăn uống! Nhìn tôi đây này, chỉ cần gặm một mẩu rêu đá là đủ leo vách 90° cả ngày rồi!"". Bố cục: chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt đứng ngẩng cao đầu nhai nhóp nhép một mẩu rêu xanh, vẻ mặt đầy kiêu hãnh của một vận động viên ăn chay trường; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L142</summary>

```text
HÌNH L142 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chỉ Huy Cú Mèo lắc đầu ngao ngán: "Giá như tinh thần đòi tăng lương của Quạ Đen được chuyển hóa thành tốc độ giải mã thì chúng ta đã xong nhiệm vụ từ lâu rồi!"". Bố cục: anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm nhấp một ngụm trà thảo mộc, khẽ mỉm cười châm biếm nhìn chiếc hóa đơn thanh toán của quạ; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L143</summary>

```text
HÌNH L143 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Toàn đội cười òa lên qua kênh bộ đàm, xua tan đi bầu không khí ngột ngạt của những căn hầm ngầm pháo đài!". Bố cục: Tiếng cười rộn rã phát ra từ các góc liên lạc dã chiến, gắn kết tình đồng đội của mười quái kiệt thêm bền chặt; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L144</summary>

```text
HÌNH L144 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Căn hầm Kho Lạnh Cực Hạn là nơi giam giữ những bí mật được bảo quản nghiêm ngặt nhất của Pháo Đài Tự Nhiên. Nhiệt độ bên trong duy trì ổn định ở mức -20°C.". Bố cục: Căn phòng mái vòm bằng đá phủ kín một lớp băng dày trong suốt, các cột băng khổng lồ chống đỡ trần nhà, hơi lạnh mù mịt cuộn trào trên mặt sàn băng nhẵn thín; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L145</summary>

```text
HÌNH L145 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mọi thiết bị điện tử thông thường mang vào đây đều sẽ bị cạn pin trong vòng năm phút, các khớp kim loại co rút lại và kẹt cứng.". Bố cục: Một chiếc nhiệt kế điện tử gắn trên tường hiển thị cột thủy ngân tụt sâu xuống vạch âm hai mươi độ C phát ra tiếng bíp cảnh báo khô khốc; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L146</summary>

```text
HÌNH L146 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và điều nguy hiểm nhất là mạng lưới máy quét quang phổ hồng ngoại tầm nhiệt giăng kín mọi ngóc ngách. Chỉ cần phát hiện một điểm nhiệt trên không độ, súng đông lạnh tự động sẽ bắn nát mục tiêu!". Bố cục: Màn hình radar tầm nhiệt hồng ngoại hiển thị toàn bộ căn phòng có màu xanh dương đậm buốt giá, bất kỳ một đốm sáng đỏ ấm áp nào xuất hiện cũng sẽ bị một vòng tròn ngắm bắn khóa chặt; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L147</summary>

```text
HÌNH L147 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hệ thống cảm biến nhạy đến mức có thể phát hiện thân nhiệt của một chú ruồi nhỏ bay qua ở khoảng cách 20m!". Bố cục: Một chú bọ nhỏ bay vào cửa hầm lập tức bị một tia laser xanh quét trúng, đóng băng thành một viên đá nhỏ rơi xuống sàn vỡ tan; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L148</summary>

```text
HÌNH L148 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đặc vụ Ếch Gỗ Bắc Cực bước từng bước chậm rãi trên mặt băng trơn trượt. Làn da nâu vàng điểm vệt đen ngang mắt của anh chàng trông như một hiệp sĩ đeo mặt nạ kiên cường.". Bố cục: chú Ếch Gỗ Bắc Cực hoạt hình da nâu vàng có vệt đen qua mắt như mặt nạ Zorro, đeo khăn quàng cổ đỏ thắm chống rét, người phủ lớp sương tuyết lấp lánh bước đi vững chãi trên mặt băng trơn nhẵn, chiếc khăn len đỏ bay nhẹ, ánh mắt bình thản nhìn về phía bàn điều khiển nhiệt độ nằm ở góc xa của căn hầm; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L149</summary>

```text
HÌNH L149 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bộ đàm phòng chỉ huy vang lên giọng Chỉ Huy Cú Mèo: "Đặc vụ Ếch Gỗ, khoảng cách tới bàn điều khiển là 30m. Cậu chỉ có thể vượt qua nếu cơ thể hoàn toàn nguội lạnh như một tảng đá."". Bố cục: anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm theo dõi sát sao qua màn hình hồng ngoại, các thông số nhịp tim của ếch gỗ đang hiển thị trên bảng đo lường y tế dã chiến; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đặc vụ 05! Mật danh Thủy Thần Đại Dương, chỉ huy phân đội tác chiến đường nước với sóng âm phá hủy công sự: Cá Voi Sát Thủ!". Bố cục: Một bể kính dã chiến bọc thép trượt vào góc phòng, chú Cá Voi Sát Thủ hoạt hình thân đen bóng bụng trắng tinh, vây lưng cao vút cắm ăng-ten định vị sonar nhỏ xíu, miệng cười nhếch mép kiểu trùm mafia biển cả nhô đầu lên khỏi mặt nước nở nụ cười nhếch mép ngạo nghễ, chiếc ăng-ten định vị sonar trên vây lưng nhấp nháy đèn xanh; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L150</summary>

```text
HÌNH L150 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ếch Gỗ gật đầu nhẹ nhàng. Anh chàng ngồi xổm xuống giữa sàn băng, thu hai chân sau sát vào bụng, nhắm nghiền hai mắt lại và bắt đầu kích hoạt cơ chế sinh học kỳ diệu nhất của mình!". Bố cục: chú Ếch Gỗ Bắc Cực hoạt hình da nâu vàng có vệt đen qua mắt như mặt nạ Zorro, đeo khăn quàng cổ đỏ thắm chống rét, người phủ lớp sương tuyết lấp lánh ngồi co tròn như một hòn sỏi trên mặt băng tuyết, một lớp màng sương tuyết trắng xóa bắt đầu lan dần từ đầu ngón chân lên khắp cơ thể; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L151</summary>

```text
HÌNH L151 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy quan sát kỳ quan sinh học đang diễn ra bên trong từng tế bào của chú ếch nhỏ bé này. Các nhà khoa học nghiên cứu sinh học vùng cực đã phải kinh ngạc thốt lên: đây là thuật giả kim đỉnh cao của tự nhiên!". Bố cục: Tranh vẽ hiển vi cắt lớp cơ thể chú ếch: gan của ếch gỗ bắt đầu phát sáng rực rỡ và phình to gấp ba lần kích thước bình thường; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L152</summary>

```text
HÌNH L152 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ngay khi tinh thể băng đầu tiên chạm vào da, gan của ếch gỗ lập tức hoạt động hết công suất, bơm một lượng khổng lồ đường glucose và chất urea vào toàn bộ hệ tuần hoàn!". Bố cục: Dòng nước màu mang hàng triệu phân tử đường glucose màu vàng óng ả và phân tử urea tỏa đi khắp các mao mạch, tràn vào bên trong từng tế bào của mọi cơ quan bên trong cơ thể; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L153</summary>

```text
HÌNH L153 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nồng độ đường bên trong tế bào tăng vọt gấp 50 đến 100 lần so với bình thường, biến dịch nội bào thành một loại si-rô đậm đặc không thể bị đông cứng!". Bố cục: Các tế bào bên trong cơ thể được bảo vệ an toàn bởi lớp màng si-rô đường tự nhiên, căng tròn và mềm mại dù nhiệt độ xung quanh đang hạ xuống âm hai mươi độ C; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L154</summary>

```text
HÌNH L154 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chất urea đóng vai trò như chiếc phao cứu sinh thứ hai, giữ nước bên trong tế bào không bị hút cạn ra ngoài khi các tinh thể đá hình thành xung quanh!". Bố cục: Kính hiển vi 3D mô phỏng phân tử urea liên kết với màng tế bào, ngăn ngừa hiện tượng co rút áp suất thẩm thấu gây chết tế bào; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L155</summary>

```text
HÌNH L155 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong khi đó, ở khoảng không gian bên ngoài tế bào, điều kỳ diệu xảy ra: 65% toàn bộ lượng nước trong cơ thể ếch gỗ bắt đầu đông cứng thành băng!". Bố cục: Đồ họa 3D hiển vi: các tinh thể băng hình lục giác sắc nhọn mọc lên chi chít ở các mô liên kết ngoại bào xung quanh tế bào nhưng không thể xuyên thủng màng tế bào được bảo vệ; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L156</summary>

```text
HÌNH L156 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Toàn bộ cơ thể Ếch Gỗ Bắc Cực cứng đờ lại như một viên sỏi đá. Đôi mắt đục ngầu như ngọc bích, các chi bất động, làn da phủ kín một lớp băng tuyết dày!". Bố cục: Cận cảnh chú Ếch Gỗ Bắc Cực hoạt hình da nâu vàng có vệt đen qua mắt như mặt nạ Zorro, đeo khăn quàng cổ đỏ thắm chống rét, người phủ lớp sương tuyết lấp lánh đã biến thành một bức tượng băng hoàn hảo, cứng ngắc không hề nhúc nhích, ánh sáng phản chiếu lấp lánh trên lưng; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L157</summary>

```text
HÌNH L157 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trái tim của anh chàng từ từ chậm lại: 60 nhịp một phút... 30 nhịp một phút... mười nhịp một phút... rồi dừng hẳn lại!". Bố cục: Biểu đồ điện tâm đồ hiển thị đường sóng nhịp tim tụt dần và phẳng lì thành một đường thẳng tắp không còn dao động; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L158</summary>

```text
HÌNH L158 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Phổi ngừng thở! Dòng nước màu ngừng chảy! Não bộ ngừng phát sóng điện từ! Ở góc độ y học thông thường, chú ếch này đã chết lâm sàng hoàn toàn!". Bố cục: Màn hình theo dõi sự sống trong phòng chỉ huy báo tín hiệu phẳng lặng, không một dấu hiệu tuần hoàn; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L159</summary>

```text
HÌNH L159 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng chính trạng thái chết giả thần kỳ này đã cứu sống anh chàng! Nhiệt độ cơ thể của Ếch Gỗ lúc này tụt xuống đúng -20°C, bằng chằn chặn với nhiệt độ của căn phòng băng!". Bố cục: Màn hình quét hồng ngoại của hệ thống an ninh quét qua vị trí của chú ếch: chú ếch hiện lên với màu xanh dương thẫm giống hệt như sàn đá xung quanh, hoàn toàn tàng hình; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cỗ máy săn mồi 6 tấn này sở hữu chùm sóng sonar công suất 225 dB, đủ sức quét xuyên lòng đá và tạo nên những cơn sóng thần dập tắt mọi chốt chặn!". Bố cục: Màn hình radar thủy âm hiển thị các luồng sóng âm thanh cực mạnh hình bán nguyệt lan tỏa từ trán cá voi sát thủ; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L160</summary>

```text
HÌNH L160 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hệ thống máy quét tầm nhiệt coi khối băng hình chú ếch chỉ là một tảng nhũ đá rơi xuống từ trần nhà, và thản nhiên bỏ qua không kích hoạt súng laser!". Bố cục: Chùm tia laser cảnh báo quét qua lưng chú ếch băng rồi lướt đi nơi khác mà không hề phát ra tiếng còi báo động nào; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L161</summary>

```text
HÌNH L161 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một cơn gió lốc của hệ thống điều hòa thổi mạnh qua sàn nhà, làm khối băng chứa Ếch Gỗ trượt ro ro trên mặt sàn băng nhẵn thín, lăn thẳng về phía chân bàn điều khiển nhiệt độ!". Bố cục: Bức tượng băng của chú Ếch Gỗ Bắc Cực hoạt hình da nâu vàng có vệt đen qua mắt như mặt nạ Zorro, đeo khăn quàng cổ đỏ thắm chống rét, người phủ lớp sương tuyết lấp lánh trượt như một hòn bi trên mặt sàn băng trơn láng, dừng lại êm ái ngay dưới chân cột trụ điều khiển trung tâm; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L162</summary>

```text
HÌNH L162 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đã tiếp cận mục tiêu! Bây giờ là giai đoạn hai: nghệ thuật hồi sinh sau giấc ngủ đông dài 7 tháng ở vùng cực bắc!". Bố cục: chú Ếch Gỗ Bắc Cực hoạt hình da nâu vàng có vệt đen qua mắt như mặt nạ Zorro, đeo khăn quàng cổ đỏ thắm chống rét, người phủ lớp sương tuyết lấp lánh nằm yên dưới chân bàn điều khiển, một dòng nước ấm nhỏ giọt từ ống tản nhiệt phía trên khẽ rơi trúng đầu chú ếch; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L163</summary>

```text
HÌNH L163 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi nhiệt độ môi trường nhích nhẹ lên trên mức đóng băng, các phân tử đường glucose bắt đầu hấp thụ nhiệt lượng. Lớp băng ngoại bào tan chảy dần dần!". Bố cục: Lớp băng phủ ngoài da chú ếch tan biến thành những giọt nước long lanh, các khớp chân bắt đầu mềm trở lại và co giãn linh hoạt; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L164</summary>

```text
HÌNH L164 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kỳ tích xuất hiện: quả tim tí hon của Ếch Gỗ tự động phát ra một xung điện sinh học bí ẩn và bắt đầu co bóp trở lại! Thình thịch... thình thịch... thình thịch!". Bố cục: Cận cảnh trái tim nhỏ bé màu đỏ hồng của chú ếch đập nhịp nhàng trở lại, bơm dòng nước màu ấm áp đi khắp cơ thể; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L165</summary>

```text
HÌNH L165 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Dòng nước màu ấm rã đông các tế bào thần kinh, đánh thức não bộ chỉ trong vòng vài phút ngắn ngủi!". Bố cục: Các xung điện thần kinh màu xanh lục chạy dọc tủy sống của chú ếch, đôi mắt chớp chớp trở lại ánh nhìn thông minh; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L166</summary>

```text
HÌNH L166 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà khoa học ghi nhận: chỉ trong vòng chưa đầy một giờ đồng hồ sau khi tan băng, ếch gỗ có thể hồi phục toàn bộ chức năng sống và nhảy nhót như chưa từng bị đông cứng!". Bố cục: chú Ếch Gỗ Bắc Cực hoạt hình da nâu vàng có vệt đen qua mắt như mặt nạ Zorro, đeo khăn quàng cổ đỏ thắm chống rét, người phủ lớp sương tuyết lấp lánh chớp mắt một cái, chiếc mồm khẽ đớp lấy không khí, bốn chân bật mạnh một cú nhảy ngoạn mục lên bàn điều khiển; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L167</summary>

```text
HÌNH L167 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bẹp! Bàn chân có màng của Ếch Gỗ đạp trúng nút xả đông khẩn cấp màu đỏ!". Bố cục: Bàn chân của chú Ếch Gỗ Bắc Cực hoạt hình da nâu vàng có vệt đen qua mắt như mặt nạ Zorro, đeo khăn quàng cổ đỏ thắm chống rét, người phủ lớp sương tuyết lấp lánh ấn mạnh xuống nút bấm khẩn cấp to đùng, còi báo động nhiệt độ vang lên một hồi ngắn báo hiệu chu trình sưởi ấm; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L168</summary>

```text
HÌNH L168 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hơi nóng bắt đầu ùa ra từ các họng thông gió, các cột băng khổng lồ tan chảy ầm ầm thành những dòng suối nhỏ chảy dọc sàn đá!". Bố cục: Các bức tường băng tan rã rào rào, hệ thống súng laser tầm nhiệt bị chập điện tóe lửa do ngập nước, căn hầm trở lại nhiệt độ bình thường; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L169</summary>

```text
HÌNH L169 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cửa Ải 3 chính thức bị bẻ khóa! Biểu tượng hoa tuyết trên bảng điều khiển {BOARD} vụt sáng chuyển sang màu xanh ngọc bích!". Bố cục: bản đồ hologram 3D của Pháo Đài Tự Nhiên nổi lơ lửng trong không khí, hiển thị 7 cửa ải an ninh phát sáng đỏ và thanh tiến độ phá khóa màu xanh ngọc (không có chữ, không có số) cập nhật kết quả: thanh tiến độ phá khóa nhảy lên nấc thứ ba, ánh sáng xanh ngọc bích tỏa sáng rực rỡ khắp phòng chỉ huy; anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm vỗ tay khen ngợi.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đặc vụ 06! Mật danh Búa Khoan Thần Tốc, kẻ có thể đập nát cửa boong-ke dày cộp bằng chính hộp sọ của mình: Chim Gõ Kiến!". Bố cục: chú Chim Gõ Kiến hoạt hình mào lông đỏ rực dựng đứng, mỏ dài sắc nhọn như mũi khoan titan, đội mũ bảo hộ lao động màu vàng có gắn đèn pin thợ mỏ đứng nghiêm chào kiểu quân đội, chiếc mũ bảo hộ màu vàng có gắn đèn pin thợ mỏ hơi lệch sang một bên, chiếc mỏ nhọn hoắt gõ lách cách xuống bàn tạo thành tia lửa nhỏ; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L170</summary>

```text
HÌNH L170 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ếch Gỗ Bắc Cực đứng trên bàn điều khiển, khẽ hất chiếc khăn quàng len đỏ ra sau vai, nở một nụ cười đắc thắng về phía ống kính camera.". Bố cục: chú Ếch Gỗ Bắc Cực hoạt hình da nâu vàng có vệt đen qua mắt như mặt nạ Zorro, đeo khăn quàng cổ đỏ thắm chống rét, người phủ lớp sương tuyết lấp lánh tạo dáng ngầu như một điệp viên sau khi hoàn thành nhiệm vụ bất khả thi, vẫy tay chào các đồng đội qua màn hình liên lạc.
```
</details>

<details><summary>L171</summary>

```text
HÌNH L171 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng tiếng vỗ tay vừa dứt thì cánh cửa tiếp theo mở toang ra một căn phòng kỳ dị chưa từng thấy: Mê Cung Bẫy Giải Mã của Cửa Ải 4!". Bố cục: Căn phòng tiếp theo hiện ra với hàng trăm tấm gương phản chiếu, những chiếc hộp gỗ cơ học gắn ròng rọc phức tạp và những sợi dây bẫy giăng chằng chịt trong không gian; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L172</summary>

```text
HÌNH L172 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đây không phải là bài toán về cơ bắp hay tốc độ. Đây là cuộc đấu trí cân não với các bẫy cơ học liên hoàn và mê cung gương quang học!". Bố cục: anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm nhìn sang chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép đang đậu trên lưng ghế, tay đã cầm sẵn chiếc kẹp kim loại siêu nhỏ; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L173</summary>

```text
HÌNH L173 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đã đến lúc cho các kỹ sư của pháo đài biết thế nào là chỉ số thông minh của loài quạ!". Bố cục: chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép bay vút lên trần nhà, lượn một vòng điệu nghệ chuẩn bị cho màn phá khóa kinh điển; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L174</summary>

```text
HÌNH L174 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nghiên cứu của giáo sư Storey tại đại học Carleton đã chứng minh: ếch gỗ Bắc Cực là bậc thầy số một thế giới về công nghệ bảo quản lạnh sinh học!". Bố cục: Hình ảnh phòng thí nghiệm hiện đại với các ống nghiệm bảo quản mẫu sinh học ở nhiệt độ âm hai mươi độ C; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L175</summary>

```text
HÌNH L175 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi dịch cơ thể đông cứng, các tế bào của ếch gỗ mất đi 40 phần trăm thể tích nước nhưng không hề bị vỡ màng tế bào nhờ lớp đệm phân tử glucose siêu đậm đặc!". Bố cục: Kính hiển vi 3D mô phỏng sự co giãn đàn hồi hoàn hảo của màng tế bào ếch dưới áp lực băng giá; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L176</summary>

```text
HÌNH L176 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chất urea tái hấp thu từ nước tiểu được giữ lại trong cơ bắp, đóng vai trò như chiếc phanh hãm tốc độ đóng băng, ngăn các tinh thể đá phát triển quá nhanh!". Bố cục: Các phân tử urea đan xen giữa các tinh thể đá, làm tròn các góc cạnh nhọn của đá để không đâm thủng mạch nước màu; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L177</summary>

```text
HÌNH L177 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sau khi rã đông hoàn toàn, các tế bào của ếch gỗ lập tức kích hoạt chu trình thanh lọc lượng đường dư thừa, đưa nồng độ đường trong nước màu trở lại mức bình thường!". Bố cục: Đồ họa y tế mô phỏng gan ếch gỗ thu hồi đường glucose và đưa lượng urea trở về bàng quang một cách nhịp nhàng; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L178</summary>

```text
HÌNH L178 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khả năng điều hòa trao đổi chất linh hoạt này khiến các nhà khoa học vũ trụ phải trầm trồ nghiên cứu để ứng dụng cho các chuyến bay liên hành tinh!". Bố cục: Hình ảnh phi hành gia tương lai bước vào buồng ngủ đông mô phỏng theo cơ chế của chú ếch gỗ Bắc Cực; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L179</summary>

```text
HÌNH L179 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cửa Ải 4 không dùng áp suất gió, không dùng khí độc, cũng chẳng cần đến nhiệt độ băng giá. Đây là một mê cung cơ học được thiết kế để giam cầm những bộ não thông minh nhất!". Bố cục: Khung cảnh căn phòng Mê Cung Bẫy Giải Mã rộng lớn với các vách tường gương bóng loáng phản chiếu vô tận, ở giữa là một hệ thống ròng rọc, hộp gỗ khóa số và các ống thủy tinh phức tạp; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cơ chế đai an toàn xương móng quấn quanh đầu cho phép anh chàng chịu đựng lực gia tốc va đập lên tới 1200G mà không hề choáng váng!". Bố cục: Bản vẽ kỹ thuật chiếc xương móng hyoid của chim gõ kiến quấn trọn hộp sọ như chiếc đai an toàn xe đua; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L180</summary>

```text
HÌNH L180 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ở trung tâm căn phòng là chiếc hộp điều khiển chính khóa chặt cánh cổng bước vào nửa sau pháo đài. Muốn mở được nó, kẻ đột nhập phải giải một chuỗi câu đố liên hoàn 8 bước cực kỳ hóc búa!". Bố cục: Cận cảnh một cỗ máy cơ học cổ điển tinh xảo bằng đồng và gỗ: có các ngăn kéo bí mật bị khóa xích, các rãnh trượt bi kim loại và một chiếc ống thủy tinh dài chứa chiếc chìa khóa nổi; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L181</summary>

```text
HÌNH L181 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các kỹ sư an ninh của pháo đài từng tự hào tuyên bố: nếu không có sách hướng dẫn sử dụng, một người trưởng thành cũng phải mất ít nhất hai ngày mới mò ra được quy luật!". Bố cục: Hình vẽ bản thiết kế kỹ thuật của cỗ máy câu đố với các mũi tên chỉ hướng chuyển động của bánh răng và đòn bẩy cơ học phức tạp (không chữ, không số); KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L182</summary>

```text
HÌNH L182 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bất kỳ một sai sót nào trong trình tự các bước cũng sẽ kích hoạt cơ chế khóa vĩnh viễn, chôn vùi chiếc chìa khóa xuống đáy hầm sâu!". Bố cục: Một chiếc bẫy lồng sắt treo lơ lửng trên trần nhà nhấp nháy đèn cảnh báo đỏ rực sẵn sàng sập xuống; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L183</summary>

```text
HÌNH L183 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng họ đã quên mất một điều: loài người không phải là sinh vật duy nhất biết tư duy logic trên hành tinh này!". Bố cục: chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép sà xuống đậu trên đỉnh cỗ máy, nghiêng đầu nhìn ngắm toàn bộ hệ thống bánh răng với ánh mắt tinh quái, mỏ kẹp chiếc kìm kim loại nhỏ; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L184</summary>

```text
HÌNH L184 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đặc vụ Quạ Đen chỉ mất đúng 30 giây để quan sát. Não bộ của loài quạ sở hữu mật độ tế bào thần kinh dày đặc ngang ngửa với các loài linh trưởng cấp cao, cho phép chúng hiểu rõ quy luật nhân quả trong chớp mắt!". Bố cục: Đồ họa so sánh bộ não của quạ đen và não khỉ đột: các vùng xử lý logic và công cụ của quạ phát sáng rực rỡ các mạng lưới nơ-ron thần kinh màu vàng ánh kim; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L185</summary>

```text
HÌNH L185 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nghiên cứu khoa học kinh điển của các nhà động vật học tại đại học Oxford và Cambridge đã chứng minh: quạ có thể tự mình giải câu đố cơ học 8 bước liên hoàn ngay trong lần thử đầu tiên mà không cần bất kỳ sự huấn luyện nào!". Bố cục: Tranh minh họa thí nghiệm khoa học nổi tiếng: một chú quạ đen thông minh đang dùng mỏ gắp từng món dụng cụ để mở lần lượt tám ngăn hộp gỗ theo thứ tự chuẩn xác; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L186</summary>

```text
HÌNH L186 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chúng hiểu rõ khái niệm về công cụ gián tiếp: dùng công cụ A để lấy công cụ B, rồi dùng công cụ B để lấy mục tiêu C một cách hoàn toàn tự nhiên!". Bố cục: Sơ đồ các bước tư duy liên kết hình chuỗi xích màu xanh lục trong tâm trí chú quạ thông minh; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L187</summary>

```text
HÌNH L187 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bước một: Quạ Đen nhặt một que gỗ ngắn trên sàn, thò mỏ khều chiếc que sắt dài hơn bị giấu sâu trong khe đá hẹp!". Bố cục: chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép dùng mỏ cắp chiếc que ngắn, khéo léo luồn vào khe nứt trên vách tường đá, kéo ra một chiếc que thép dài hơn; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L188</summary>

```text
HÌNH L188 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bước hai: chiếc que thép dài quá thẳng không móc được chốt? Không thành vấn đề! Quạ Đen kẹp đầu que vào kẽ nứt sàn đá, dùng mỏ uốn cong nó thành một chiếc lưỡi câu hoàn hảo!". Bố cục: Cận cảnh chiếc mỏ đen bóng của chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép bẻ cong đầu sợi dây thép thành hình móc câu chuẩn xác như một người thợ rèn điêu luyện; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L189</summary>

```text
HÌNH L189 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bước ba: anh chàng dùng chiếc móc câu vừa chế tạo câu một túi sỏi đá nặng trĩu đặt trên giá cao xuống sàn!". Bố cục: chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép ngậm móc câu kéo đứt sợi dây treo, thả rơi chiếc túi chứa các viên sỏi đặc xuống đất một cách nhẹ nhàng; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đặc vụ 07! Mật danh Cỗ Xe Tăng Sa Mạc, pháo đài di động vượt qua vùng bẫy nhiệt độ 50°C mà không cần tiếp tế một giọt nước: Lạc Đà Sa Mạc!". Bố cục: chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao thong thả bước vào, hai bên hông thồ hai bình nước dã chiến áp lực cao, miệng vừa nhai tóp tép một cành xương rồng gai góc vừa chớp chớp hàng mi cong vút; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L190</summary>

```text
HÌNH L190 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bước bốn: tháo túi lấy sỏi, bay vút tới bên cạnh chiếc ống thủy tinh hẹp chứa chiếc chìa khóa nổi trên mặt nước!". Bố cục: chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép đậu trên miệng ống thủy tinh cao và hẹp, bên dưới đáy ống là chiếc chìa khóa đồng thau đang nổi bập bềnh ngoài tầm với của mỏ chim; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L191</summary>

```text
HÌNH L191 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đây là bài kiểm tra trí tuệ ngụ ngôn Ê-dốp trứ danh trong giới khoa học sinh học! Quạ Đen có hiểu được quy luật dâng mực nước theo định luật thể tích hay không?". Bố cục: Trên bàn có hai đĩa đồ vật: một đĩa chứa các mẩu xốp nhựa nhẹ nổi trên mặt nước, một đĩa chứa những viên sỏi đá đặc chìm sâu; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L192</summary>

```text
HÌNH L192 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu thả xốp vào, xốp sẽ nổi lềnh bềnh và không làm dâng nước. Chỉ có sỏi đá đặc mới chiếm chỗ chất lỏng và đẩy chiếc chìa khóa lên miệng ống!". Bố cục: Mô hình so sánh: thả xốp thì mực nước không đổi, thả sỏi đặc thì mực nước dâng cao theo định luật Ac-si-mét; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L193</summary>

```text
HÌNH L193 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Quạ Đen thậm chí còn không thèm liếc nhìn đĩa xốp nhựa! Anh chàng chỉ chọn đúng những viên sỏi đá đặc màu xám nặng nhất!". Bố cục: chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép dùng mỏ gắp từng viên sỏi đá đặc, thả từng viên từng viên một vào trong ống thủy tinh: tõm... tõm... tõm! KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L194</summary>

```text
HÌNH L194 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khả năng ước lượng thể tích chất lỏng của quạ chuẩn xác đến mức kinh ngạc, anh chàng dừng thả sỏi ngay khi chiếc chìa khóa vừa chạm miệng ống!". Bố cục: Mặt nước dâng lên vừa khít mép bình, chiếc chìa khóa nổi lên trong tầm với hoàn hảo của mỏ quạ; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L195</summary>

```text
HÌNH L195 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mực nước dâng lên! Chiếc chìa khóa đồng từ từ nổi lên sát miệng ống! Quạ Đen chỉ việc thò mỏ cắp lấy chìa khóa một cách ngon ơ!". Bố cục: Chiếc chìa khóa trồi lên sát miệng bình thủy tinh, chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép ngậm lấy chiếc chìa khóa đồng, nháy mắt tinh nghịch về phía ống kính quan sát hoạt hình vui nhộn; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L196</summary>

```text
HÌNH L196 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bước năm: cắm chìa khóa vào ổ khóa số một, mở ngăn kéo chứa quả tạ sắt!". Bố cục: chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép tra chìa khóa vào ổ, vặn một vòng kêu tách, ngăn kéo tự động trượt ra để lộ một quả tạ sắt tròn; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L197</summary>

```text
HÌNH L197 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bước sáu và bước bảy: đẩy quả tạ sắt lăn qua máng trượt nghiêng, đè sập chiếc bẫy kẹp và nhả chốt hãm của ròng rọc trung tâm!". Bố cục: Quả tạ sắt lăn rầm rập trên rãnh trượt kim loại, đè bẹp chiếc bẫy kẹp nguy hiểm và làm bật tung chiếc then cài cửa chính; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L198</summary>

```text
HÌNH L198 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và bước tám cuối cùng: Quạ Đen bay lên ấn mạnh cần gạt tổng lực! Răng rắc... ầm! Cánh cổng sắt nặng hai tấn từ từ cuốn lên trần nhà!". Bố cục: Hệ thống ròng rọc khổng lồ chuyển động kéo cánh cổng sắt lớn mở toang, ánh sáng từ nửa sau pháo đài rọi vào mê cung; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L199</summary>

```text
HÌNH L199 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng ngay khi cổng vừa mở, hệ thống camera nhận diện các hình vẽ hoạt hình ngộ nghĩnh của mê cung gương bắt đầu nhấp nháy đèn đỏ, cố gắng quét chân dung kẻ đột nhập để phát lệnh truy nã toàn cầu!". Bố cục: Các camera giám sát tự động gắn trên các vách gương xoay nòng lia về phía chú quạ đen, các tia quét nhận dạng khuôn mặt màu đỏ quét qua quét lại; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hồng cầu hình oval độc nhất vô nhị giãn nở 240% thể tích giúp anh chàng trữ 100 lít nước và hành quân qua chảo lửa sa mạc dễ dàng!". Bố cục: Kính hiển vi mô phỏng tế bào hồng cầu hình oval màu đỏ tươi bơi lội trơn tru trong mạch nước màu lạc đà; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L200</summary>

```text
HÌNH L200 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Loài quạ có khả năng nhận diện và ghi nhớ khuôn mặt con người suốt hơn 5 năm trời, và chúng cũng thừa biết camera hoạt động theo nguyên lý nào!". Bố cục: chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép nhìn thẳng vào ống kính camera với vẻ mặt đầy thách thức, không một chút bối rối sợ hãi; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L201</summary>

```text
HÌNH L201 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Quạ Đen thò mỏ kẹp lấy một tấm gương nhỏ trên sàn, xoay ngược góc phản chiếu ánh sáng đèn pha chiếu thẳng vào ống kính camera giám sát!". Bố cục: chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép dùng mỏ nghiêng tấm gương kính, hắt luồng ánh sáng chói lòa làm mù hoàn toàn cảm biến quang học của ống kính quan sát hoạt hình vui nhộn; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L202</summary>

```text
HÌNH L202 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa hết, anh chàng còn dùng mỏ cạy tung tấm ốp bảo vệ phía sau, làm ngắn mạch dây nguồn điều khiển khiến toàn bộ hệ thống camera nổ lách tách!". Bố cục: Dây cáp điện bên trong camera tóe lửa chập mạch, tia lửa điện bắn ra rực rỡ trong bóng tối; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L203</summary>

```text
HÌNH L203 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Xèo xèo! Cảm biến camera bị lóa sáng chập mạch bốc khói đen! Toàn bộ hệ thống mê cung gương sụp đổ tín hiệu hoàn toàn!". Bố cục: Màn hình điều khiển camera của pháo đài nhiễu loạn thành các vạch sọc trắng đen vô định, không thể ghi lại bất kỳ hình ảnh nào của biệt đội; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L204</summary>

```text
HÌNH L204 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Biểu tượng câu đố cơ học trên {BOARD} chuyển sang màu xanh ngọc bích rực rỡ! Bốn trên 7 cửa ải đã bị biệt đội đặc nhiệm chinh phục thành công!". Bố cục: bản đồ hologram 3D của Pháo Đài Tự Nhiên nổi lơ lửng trong không khí, hiển thị 7 cửa ải an ninh phát sáng đỏ và thanh tiến độ phá khóa màu xanh ngọc (không có chữ, không có số) cập nhật tín hiệu: thanh tiến độ phá khóa đã vượt qua mốc một nửa, ánh sáng xanh ngọc bích chiếm lĩnh bản đồ pháo đài; anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm gật đầu tán thưởng.
```
</details>

<details><summary>L205</summary>

```text
HÌNH L205 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Quạ Đen bay sà xuống vai tượng đá, mỏ huýt sáo một điệu nhạc điệp viên vui nhộn, không quên vẫy cánh chào khán giả theo dõi qua màn hình.". Bố cục: chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép đậu trên vai bức tượng đá cẩm thạch, đầu nghiêng ngả điệu đà, vẻ mặt tự mãn của một bậc thầy trí tuệ vừa phá giải cỗ máy thế kỷ.
```
</details>

<details><summary>L206</summary>

```text
HÌNH L206 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng từ sâu bên trong đường dẫn tới Cửa Ải 5, tiếng nước chảy xiết ầm ầm như thác đổ bắt đầu vọng lại, làm rung chuyển cả sàn đá hoa cương.". Bố cục: Nước ngầm bắt đầu rỉ qua các khe nứt sàn đá, tiếng gầm gào của dòng nước áp lực cao vang lên đe dọa từ sâu trong lòng pháo đài; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L207</summary>

```text
HÌNH L207 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hào nước ngầm áp lực cao của pháo đài đã mở van xả lũ! Lần này, chỉ có một bá chủ thực sự của đại dương mới có thể đối đầu với cơn thịnh nộ của thủy triều!". Bố cục: Cận cảnh anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm nhìn vào bể nước dã chiến: "Đặc vụ Cá Voi Sát Thủ, căn hầm ngập nước đã chuẩn bị xong. Cho chúng thấy thế nào là sức mạnh của hải quân bầy đàn!"
```
</details>

<details><summary>L208</summary>

```text
HÌNH L208 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đại ca biển cả chuẩn bị xuất chiêu với những đợt sóng thần áp lực kinh hoàng!". Bố cục: chú Cá Voi Sát Thủ hoạt hình thân đen bóng bụng trắng tinh, vây lưng cao vút cắm ăng-ten định vị sonar nhỏ xíu, miệng cười nhếch mép kiểu trùm mafia biển cả nhô vây lưng lên khỏi mặt nước, ánh mắt rực lửa chuẩn bị xé toạc cánh cửa van đập nước ngầm.
```
</details>

<details><summary>L209</summary>

```text
HÌNH L209 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trí tuệ của loài quạ đã vượt xa những gì con người từng tưởng tượng về thế giới loài chim! Chúng có thể nhớ mặt từng kẻ thù và truyền lại mối đe dọa này cho các thế hệ con cháu suốt nhiều năm trời!". Bố cục: Hình ảnh một đàn quạ đen bay lượn trên ngọn cây, cùng phát tín hiệu cảnh báo khi nhìn thấy bóng dáng kẻ thù xuất hiện; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đặc vụ 08! Mật danh Thánh Leo Vách Đứng, kẻ thách thức mọi định luật vật lý trên những bức tường dựng đứng 90°: Dê Núi Bắc Mỹ!". Bố cục: chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt đứng kiêu hãnh trên đỉnh chiếc tủ sắt cao chót vót, bốn móng guốc bọc đệm cao su đặc chủng bám dính như giác hút chân không; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L210</summary>

```text
HÌNH L210 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi đối đầu với mê cung gương, quạ đen hoàn toàn hiểu rằng hình ảnh trong gương chỉ là sự phản chiếu quang học chứ không phải là một con quạ đối thủ!". Bố cục: chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép nghiêng đầu nhìn vào gương, dùng mỏ chạm nhẹ vào mặt kính rồi quay lưng lại tìm công tắc thật sự; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L211</summary>

```text
HÌNH L211 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khả năng tư duy trừu tượng này cho phép chúng giải quyết các bài toán hóc búa một cách bình tĩnh, không hề mắc bẫy tâm lý của các kỹ sư pháo đài!". Bố cục: chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép nháy mắt tinh nghịch, ngậm chiếc kìm cắt đứt sợi dây bẫy cuối cùng; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L212</summary>

```text
HÌNH L212 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi một bước đi trong mê cung giải đố của Quạ Đen đều được tính toán chuẩn xác như một đại kiện tướng cờ vua quốc tế!". Bố cục: Bàn cờ vua bằng đá với quân cờ hình chú quạ đen chiếu tướng vua cờ cơ học của pháo đài; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L213</summary>

```text
HÌNH L213 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Anh chàng không chỉ mở được cổng mà còn thu gom luôn một mẩu dây đồng sáng loáng nhét vào túi áo làm kỷ niệm cho bộ sưu tập cá nhân!". Bố cục: chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép giấu mẩu dây đồng vào dưới cánh, nháy mắt tinh quái trước khi sải cánh bay tiếp; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L214</summary>

```text
HÌNH L214 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu bạn nghĩ một biệt đội đặc nhiệm gồm mười loài động vật hoang dã có thể phối hợp ăn ý như quân đội hoàng gia... thì bạn đã đánh giá quá cao tính kỷ luật của giới tự nhiên rồi!". Bố cục: Căn phòng chỉ huy của anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm, bàn điều khiển bừa bộn những vỏ chai nước tăng lực, lông chim bay lả tả và màn hình liên lạc đang nhấp nháy đèn báo lỗi âm thanh; anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm đỡ trán bất lực.
```
</details>

<details><summary>L215</summary>

```text
HÌNH L215 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ngay giữa thời khắc căng thẳng chuẩn bị bước vào trận chiến đường thủy của Cửa Ải 5, một chuỗi âm thanh rùng rợn bỗng nhiên nổ ra trên kênh liên lạc tần số cao.". Bố cục: Chiếc loa truyền thanh rung bần bật, phát ra những tiếng rôm rốp rào rạo chói tai như tiếng một tảng đá đang bị máy nghiền xi măng nghiền nát; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L216</summary>

```text
HÌNH L216 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Rộp! Rộp! Xoàn xoạt! Rộp! Tiếng động kinh hoàng đến mức Chim Cắt Lớn giật thót mình suýt ngã khỏi thành đá, còn Quạ Đen thì vội vàng ôm đầu tưởng pháo đài sập!". Bố cục: chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng trượt chân bám chặt móng vào gờ đá, chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép chui tọt vào trong một chiếc mũ sắt thế giới tự nhiên trốn; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L217</summary>

```text
HÌNH L217 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: ""Báo động đỏ! Kẻ địch đang dùng súng máy nghiền nát công sự của chúng ta! Yêu cầu hỗ trợ khẩn cấp!"". Bố cục: Chim Cắt hét to vào bộ đàm trong tư thế sẵn sàng kích hoạt ba lô phản lực để bay thoát thân; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L218</summary>

```text
HÌNH L218 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chỉ Huy Mật Vụ vội vàng điều chỉnh tần số thu âm, phóng to nguồn phát tín hiệu trên radar định vị vệ tinh. Và hình ảnh hiện lên trên màn hình chính khiến tất cả ngã ngửa!". Bố cục: Màn hình chính phóng to cận cảnh khuôn mặt của chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao: anh chàng đang đứng ung dung tự tại, hai hàm răng to tướng nhai tóp tép một nhánh xương rồng sa mạc đầy gai nhọn hoắt ngay sát mic thu âm; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L219</summary>

```text
HÌNH L219 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chiếc micro dã chiến gắn trên cổ áo của Lạc Đà Sa Mạc đang thu trọn từng tiếng nhai giòn rụm của những chiếc gai xương rồng dài 5cm bị nghiền nát thành bã!". Bố cục: Cận cảnh miệng của chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao với các mấu sừng hình nón cứng như đá bên trong má, nghiền nát những chiếc gai nhọn sắc bén một cách ngon lành như nhai bim bim; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bốn chiếc móng guốc cao su đàn hồi kép giúp anh chàng phi thân ngược vách đá thẳng đứng 30m trong nháy mắt!". Bố cục: Hình vẽ phóng to mặt dưới của chiếc móng dê núi với lớp đệm dẻo bám dính vào vi gờ đá; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L220</summary>

```text
HÌNH L220 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bên trong vòm miệng và má của lạc đà có hàng trăm mấu thịt hình nón bằng chất sừng cứng ngắc, hướng thẳng vào phía cuống họng giúp bẻ gãy mọi mũi gai nhọn mà không làm xước niêm mạc miệng!". Bố cục: Hình vẽ giải phẫu vòm miệng lạc đà với các gai sừng nhú papillae xếp lớp như những chiếc khiên che chở bảo vệ mô mềm; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L221</summary>

```text
HÌNH L221 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: ""Đặc vụ Lạc Đà! Cậu có biết chiếc micro đó có giá bằng cả năm tiền trợ cấp đi lại của cậu không hả? Tắt mic ngay trước khi tôi biến cậu thành chiếc thảm trải sàn!"". Bố cục: Cận cảnh anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm đập mạnh tay xuống bàn làm chiếc bút nhảy tưng lên, mắt tóe lửa giận dữ; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L222</summary>

```text
HÌNH L222 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Dạ... cháu xin lỗi Chỉ Huy! Tại nhai xương rồng đỡ khát nước quá nên cháu quên mất là mic vẫn đang bật ạ! Cháu xin hứa nhai khẽ lại ạ!". Bố cục: chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao chớp chớp hàng mi dày rợp bóng, nở nụ cười hiền lành ngơ ngác, thè chiếc lưỡi dài liếm mép giấu nhánh xương rồng ra sau lưng; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L223</summary>

```text
HÌNH L223 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Xương rồng này ngọt lắm sếp ơi, có nhiều nước chuyển hóa giúp tế bào nước màu oval của cháu căng tràn sức sống luôn ạ!". Bố cục: chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao thò đầu vào ống kính camera nháy mắt tinh nghịch làm cả phòng chỉ huy phì cười; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L224</summary>

```text
HÌNH L224 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cơn giận của Chỉ Huy còn chưa kịp hạ nhiệt thì tai họa thứ hai ập đến từ vị trí cảnh giới trên cây cổ thụ ngoài sân pháo đài. Lần này là từ Đặc vụ Chim Bách Thanh!". Bố cục: Khung cảnh ban đêm ngoài sân pháo đài, một cây gai bồ kết khổng lồ với những chiếc gai nhọn hoắt cắm tua tủa, chú Chim Bách Thanh hoạt hình lông xám trắng có dải lông đen vắt ngang mắt như dải băng cướp biển, mỏ có móc câu sắc nhọn, chân cầm một nhánh gai nhọn công nghệ đang đậu trên cành cao đảo mắt nhìn quanh; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L225</summary>

```text
HÌNH L225 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bách Thanh có một bản năng nghề nghiệp ăn sâu vào nước màu: hễ nhìn thấy bất kỳ vật thể nào có giá trị hoặc con mồi nào, anh chàng đều phải mang đi cắm chặt lên một chiếc gai nhọn để cất giữ làm kho lương thực dự trữ!". Bố cục: Cành cây gai của bách thanh cắm đầy những chiến lợi phẩm kỳ dị: một mẩu dây đồng, một chiếc cúc áo kim loại, một con thằn lằn khô và... một chiếc thẻ từ màu đỏ phát sáng; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L226</summary>

```text
HÌNH L226 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và bi kịch là chiếc thẻ từ màu đỏ đó chính là chiếc chìa khóa dự phòng duy nhất của Tổng Cục Trưởng Mật Vụ để kích hoạt cửa thoát hiểm khẩn cấp!". Bố cục: Cận cảnh chiếc thẻ từ dập nổi biểu tượng điệp viên màu bạc bị một chiếc gai nhọn đâm xuyên thủng qua góc thẻ, đung đưa trong gió đêm lạnh lẽo; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L227</summary>

```text
HÌNH L227 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo Chỉ Huy: tôi vừa phát hiện một vật thể hình chữ nhật có nguy cơ rơi vào tay kẻ địch! Tôi đã thực hiện biện pháp nghiệp vụ tiêu chuẩn: xiên nó lên chiếc gai cao 10 mét để bảo quản an toàn suốt 3 ngày tới!". Bố cục: chú Chim Bách Thanh hoạt hình lông xám trắng có dải lông đen vắt ngang mắt như dải băng cướp biển, mỏ có móc câu sắc nhọn, chân cầm một nhánh gai nhọn công nghệ tự hào ưỡn ngực báo cáo qua bộ đàm, chiếc mỏ khoằm sắc như dao găm vỗ vỗ vào chiếc thẻ từ đung đưa trên gai; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L228</summary>

```text
HÌNH L228 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đây là kỹ thuật lưu trữ an toàn cấp độ năm sao của dòng họ nhà tôi, bảo đảm chim ưng hay cáo hoang cũng không thể nào lấy trộm được!". Bố cục: chú Chim Bách Thanh hoạt hình lông xám trắng có dải lông đen vắt ngang mắt như dải băng cướp biển, mỏ có móc câu sắc nhọn, chân cầm một nhánh gai nhọn công nghệ khoanh hai cánh trước ngực vẻ mặt cực kỳ tự mãn với chiến tích bảo vệ tài sản; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L229</summary>

```text
HÌNH L229 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: ""Bách Thanh ơi là Bách Thanh! Đó là chiếc thẻ từ mở cửa thoát hiểm của cả đội đấy! Cậu xiên thủng nó thế kia thì lát nữa chúng ta thoát bằng niềm tin à?"". Bố cục: anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm ngửa mặt lên trần nhà than trời, hai cánh ôm lấy đầu, chiếc kính râm suýt rơi xuống sàn; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đặc vụ 09! Mật danh Sát Thủ Gai Nhọn, tay súng phun tia nước tầm xa và phục kích cắm chốt tầm xa: Chim Bách Thanh!". Bố cục: chú Chim Bách Thanh hoạt hình lông xám trắng có dải lông đen vắt ngang mắt như dải băng cướp biển, mỏ có móc câu sắc nhọn, chân cầm một nhánh gai nhọn công nghệ đậu trên bóng đèn trần phòng họp, mỏ găm một chiếc móc sắt nhọn hoắt, dải lông đen ngang mắt trông như một sát thủ chuyên nghiệp đang quan sát con mồi; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L230</summary>

```text
HÌNH L230 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa hết, thảm kịch hậu trường thứ ba lại xuất hiện ngay dưới chân bàn làm việc của phòng tác chiến ngầm. Lực lượng Kiến Cắt Lá vừa hoàn thành một chiến dịch bất ngờ!". Bố cục: Dưới chân bàn, một hàng dài hàng ngàn chú kiến cắt lá đang hối hả diễu hành, vác trên lưng những mảnh vải màu đen tuyền cắt tỉa cực kỳ vuông vắn; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L231</summary>

```text
HÌNH L231 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chim Cắt Lớn vừa bay về nghỉ chân, cúi xuống nhìn chiếc áo khoác điệp viên sang trọng của mình thì phát hiện: toàn bộ phần vạt áo và chiếc cà vạt lụa đắt tiền đã bị xẻo nham nhở không còn một manh giáp!". Bố cục: chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng nhìn xuống ngực áo rách tơi tả, chiếc cà vạt cụt lủn chỉ còn lại đúng cái củ ấu quanh cổ, miệng há hốc không thốt nên lời; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L232</summary>

```text
HÌNH L232 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo: đơn vị công binh chúng em phát hiện loại vải này có hàm lượng xen-lu-lô-zơ siêu cao, rất thích hợp để mang về hầm làm phân bón trồng vườn nấm cộng sinh ạ! Cảm ơn bác chim cắt đã tài trợ!". Bố cục: tiểu đội ba chú Kiến Cắt Lá hoạt hình màu nâu đỏ, đầu to mang hàm răng kim loại sáng loáng, đội mũ cối công binh màu xanh lá, đang vác những mảnh lá xanh như chiếc khiên chắn giơ cao chiếc kéo hàm răng thép bóng loáng, đồng thanh hô to vẻ mặt hớn hở của những người nông dân được mùa lá tốt; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L233</summary>

```text
HÌNH L233 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vườn nấm Leucocoprinus của chúng em được bón lụa thượng hạng này sẽ cho ra những mẻ nấm ngon nhất lịch sử 50 triệu năm nông nghiệp kiến!". Bố cục: Những chú kiến tí hon reo hò nhảy múa quanh mảnh vải lụa đen vừa cắt được; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L234</summary>

```text
HÌNH L234 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chim Cắt tức đến nỗi lông đầu dựng đứng, xòe cánh đòi lao vào mổ kiến, trong khi bầy kiến tí hon thì giơ hàm răng kim loại lên thách thức!". Bố cục: chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng xù lông quát tháo, đàn kiến xếp thành hình chiếc khiên lá chắn phòng thủ kiên cố, Quạ Đen đứng bên cạnh ôm bụng cười ngặt nghẽo; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L235</summary>

```text
HÌNH L235 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: ""Trật tự ngay! Tất cả lập tức về vị trí chiến đấu trước khi tôi trừ toàn bộ lương thưởng của cả mười đứa!" Tiếng quát uy lực của Chỉ Huy Mật Vụ vang dội làm rung chuyển cả căn hầm.". Bố cục: anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm đứng phắt dậy, đập bàn cái rầm, chiếc máy tính bảng hologram phát ra một tiếng bíp đanh thép lập lại kỷ cương quân ngũ; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L236</summary>

```text
HÌNH L236 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Toàn đội lập tức nín thở, đứng nghiêm như những bức tượng. Trò đùa chấm dứt khi màn hình theo dõi hào nước ngầm chuyển sang màu đỏ báo động lũ quét!". Bố cục: Màn hình trung tâm hiện lên hình ảnh một đập nước ngầm khổng lồ bằng bê tông cốt thép, dòng nước cuồn cuộn chảy xiết với áp suất hàng trăm át-mốt-phe sẵn sàng cuốn phăng mọi thứ; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L237</summary>

```text
HÌNH L237 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cửa Ải 5: Hào Nước Áp Lực Cao đang đón chờ. Bể nước dã chiến từ từ hạ xuống mép đập nước ngầm.". Bố cục: Khung cảnh cửa van xả lũ khổng lồ mở ra, dòng nước đen ngòm xoáy tròn dữ dội dưới đáy vực sâu; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L238</summary>

```text
HÌNH L238 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cá Voi Sát Thủ lặn sâu xuống làn nước lạnh, vây lưng nhô cao rẽ sóng, chiếc ăng-ten phát sóng sonar bắt đầu phát ra những tiếng nhấp chuột đanh gọn xuyên qua lòng đá. Trận hải chiến dưới lòng đất chính thức khai hỏa!". Bố cục: chú Cá Voi Sát Thủ hoạt hình thân đen bóng bụng trắng tinh, vây lưng cao vút cắm ăng-ten định vị sonar nhỏ xíu, miệng cười nhếch mép kiểu trùm mafia biển cả lướt đi dũng mãnh trong làn nước ngầm cuồn cuộn, ánh mắt lóe lên sự thống trị tuyệt đối của kẻ săn mồi đỉnh cao đại dương.
```
</details>

<details><summary>L239</summary>

```text
HÌNH L239 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đại ca biển cả chuẩn bị thể hiện sức mạnh của sóng âm sonar và cú quất đuôi sóng thần kinh hoàng!". Bố cục: Bọt nước cuộn trào quanh thân cá voi sát thủ khi anh chàng bắt đầu lặn xuống đáy sâu của con hào.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mấu răng tomium sắc bén và kỹ thuật găm gai nhọn cho phép anh chàng vượt qua thử thách to gấp đôi và cất giữ chiến lợi phẩm an toàn suốt 3 ngày!". Bố cục: Bức ảnh tư liệu mật về chiếc mỏ khoằm có mấu răng giả của chim bách thanh; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L240</summary>

```text
HÌNH L240 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: ""Chỉ Huy ơi, nhai xương rồng này đã lắm, hay là Tổng Cục nhập khẩu cho cháu một tấn về để ở căng-tin dã chiến đi ạ!"". Bố cục: chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao thò đầu vào ống kính camera nhai nhồm nhoàm làm cả phòng điều khiển lại một phen ôm đầu; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L241</summary>

```text
HÌNH L241 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chim Bách Thanh thì nghiêm túc giải thích: "Xiên đồ lên gai là biện pháp bảo mật sinh học tối tân nhất! Không một tên trộm nào dám leo lên bụi gai bồ kết cao 10 mét để lấy trộm thẻ từ đâu ạ!"". Bố cục: chú Chim Bách Thanh hoạt hình lông xám trắng có dải lông đen vắt ngang mắt như dải băng cướp biển, mỏ có móc câu sắc nhọn, chân cầm một nhánh gai nhọn công nghệ đứng trên cành gai ưỡn ngực thuyết minh về triết lý bảo vệ tài sản của dòng họ mình; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L242</summary>

```text
HÌNH L242 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đại Đội Kiến Cắt Lá cũng gửi báo cáo phụ: "Mảnh vải áo lụa của bác chim cắt đã được đưa vào khoang ủ nấm số một, dự kiến sẽ thu hoạch được mẻ nấm siêu to khổng lồ vào sáng mai ạ!"". Bố cục: Những chú kiến cắt lá giơ hai càng ăn mừng rộn rã dưới lòng hầm ngầm; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L243</summary>

```text
HÌNH L243 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lạc Đà Sa Mạc hứa chắc nịch: "Lần sau cháu sẽ nhai cỏ khô êm dịu như nhung, bảo đảm không làm rè sóng bộ đàm của cả đội nữa đâu ạ!"". Bố cục: chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao thề thốt giơ một chân trước lên, miệng vẫn còn dính một cọng hoa xương rồng màu vàng rực rỡ; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L244</summary>

```text
HÌNH L244 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chỉ Huy Cú Mèo chỉ biết thở dài bật cười: "Thôi được rồi, nhớ giữ lời hứa đấy, anh chàng xe tăng sa mạc của tôi!"". Bố cục: anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm vỗ nhẹ vào vai lạc đà qua màn hình hologram, bầu không khí lại trở nên ấm cúng lạ thường; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L245</summary>

```text
HÌNH L245 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hào nước ngầm của Pháo Đài Tự Nhiên là một mê cung thủy lực tối tăm và hung hãn. Dòng nước đen kịt cuộn xoáy với vận tốc kinh hoàng, tạo nên những dòng xoáy ngầm có thể xé toạc bất kỳ tàu ngầm thế giới tự nhiên nào!". Bố cục: Dòng nước ngầm đen ngòm cuồn cuộn chảy xiết giữa hai vách đá dựng đứng sâu hun hút, các xoáy nước khổng lồ sủi bọt trắng xóa cuốn trôi những thanh gỗ vụn; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L246</summary>

```text
HÌNH L246 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Độ sâu hơn 40m dưới mặt đất, ánh sáng mặt trời không bao giờ rọi tới được đây. Tầm nhìn quang học bằng không tròn trĩnh. Các camera thủy văn chỉ thu về một màu đen đặc quánh như mực!". Bố cục: Màn hình quan sát dưới nước tối om, chỉ có những đốm bọt khí trắng xóa lướt qua ống kính máy quay; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L247</summary>

```text
HÌNH L247 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng trong bóng tối vĩnh cửu ấy, một bóng đen khổng lồ nặng 6 tấn mang hai màu đen trắng tương phản đang lướt đi nhẹ nhàng như một chiếc bóng ma đại dương!". Bố cục: chú Cá Voi Sát Thủ hoạt hình thân đen bóng bụng trắng tinh, vây lưng cao vút cắm ăng-ten định vị sonar nhỏ xíu, miệng cười nhếch mép kiểu trùm mafia biển cả bơi lướt đi uyển chuyển dưới làn nước sâu, thân hình thon dài hình thoi hoàn hảo rẽ nước không một tiếng động, vây lưng cao vút rẽ sóng kiêu hãnh; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L248</summary>

```text
HÌNH L248 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cơ thể thủy động lực học hình thoi giúp cá voi sát thủ giảm thiểu tối đa lực ma sát nhớt của nước, lướt đi êm ái như một quả ngư lôi tàng hình!". Bố cục: Bản vẽ kỹ thuật động lực học chất lưu: các dòng nước màu xanh lam lướt mượt mà quanh thân cá voi mà không tạo ra các xoáy cuộn cản trở; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L249</summary>

```text
HÌNH L249 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cản đường phía trước là một cánh cửa van ngăn lũ bằng thép tôi dày 0,5m, khóa chặt bởi ba chiếc chốt thủy lực áp suất cao. Không có chìa khóa, cũng không có chỗ để gài thuốc nổ.". Bố cục: Cận cảnh cánh cửa van đập nước bằng thép khổng lồ bị đóng chặt, trên mặt thép có những vết gỉ sét và các khớp nối thủy lực to bằng bắp đùi người lớn; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và lực lượng công binh bí mật cuối cùng! Đặc vụ 10: Đại Đội Công Binh Kiến Cắt Lá, hàng triệu chiến sĩ tí hon sở hữu hàm răng thép tẩm kim loại nặng có thể khoét rỗng chân móng pháo đài!". Bố cục: tiểu đội ba chú Kiến Cắt Lá hoạt hình màu nâu đỏ, đầu to mang hàm răng kim loại sáng loáng, đội mũ cối công binh màu xanh lá, đang vác những mảnh lá xanh như chiếc khiên chắn xếp thành đội hình thế giới tự nhiên ngay ngắn trên mặt bàn, mỗi chú vác một chiếc cờ lê mini và một phiến đá nhỏ như những người lính công binh tinh nhuệ; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L250</summary>

```text
HÌNH L250 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: ""Đặc vụ Cá Voi Sát Thủ, chúng ta không nhìn thấy điểm yếu của cánh cửa đập. Cậu phải tự tìm đường phá chốt trong bóng tối!" Giọng Chỉ Huy vang lên qua bộ đàm chống nước.". Bố cục: anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm theo dõi tín hiệu định vị phát ra từ chiếc ăng-ten gắn trên vây lưng cá voi, trên màn hình radar chỉ là một đốm sáng cô độc giữa lòng hào nước; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L251</summary>

```text
HÌNH L251 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cá Voi Sát Thủ không cần mắt để nhìn. Anh chàng sở hữu cỗ máy radar âm thanh sinh học tối tân nhất từng được tạo hóa tạo ra!". Bố cục: Cận cảnh phần trán vồ tròn trịa chứa đầy khối dầu sinh học của chú Cá Voi Sát Thủ hoạt hình thân đen bóng bụng trắng tinh, vây lưng cao vút cắm ăng-ten định vị sonar nhỏ xíu, miệng cười nhếch mép kiểu trùm mafia biển cả, nơi phát ra các xung âm thanh định vị siêu âm; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L252</summary>

```text
HÌNH L252 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khối mỡ dưa hấu đặc biệt trên trán cá voi hoạt động như một thấu kính quang học âm thanh, hội tụ các sóng siêu âm phân tán thành một chùm tia hẹp có độ phân giải siêu nét!". Bố cục: Hình cắt lớp 3D khối mỡ trán melon của cá voi: các sóng siêu âm màu vàng kim bị khúc xạ và hội tụ thành một luồng tia âm thanh định hướng chính xác cao; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L253</summary>

```text
HÌNH L253 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tách! Tách! Tách! Những chùm xung âm thanh định vị cực ngắn bắt đầu được bắn ra liên hồi từ khối dầu trán của cá voi sát thủ!". Bố cục: Các vòng sóng âm thanh siêu âm hình bán cầu màu xanh neon phát ra từ trán cá voi, lan tỏa cực nhanh qua làn nước tối đen; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L254</summary>

```text
HÌNH L254 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cường độ âm thanh tăng vọt lên mức cực đại: 225 dB! Đây là mức áp suất âm thanh dưới nước khủng khiếp nhất trong thế giới sinh vật!". Bố cục: Đồ họa sóng âm hiển thị cột đo áp lực âm thanh chạm đỉnh 225 dB, sóng xung kích âm thanh làm rung chuyển cả những hạt cát dưới đáy hào nước; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L255</summary>

```text
HÌNH L255 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các chùm sóng âm thanh 225 dB chạm vào cánh cửa đập bằng thép, dội ngược trở lại hàm dưới của cá voi và truyền thẳng vào tai trong với độ phân giải siêu nét!". Bố cục: Các tia sóng dội ngược màu vàng kim thu về hàm dưới của chú Cá Voi Sát Thủ hoạt hình thân đen bóng bụng trắng tinh, vây lưng cao vút cắm ăng-ten định vị sonar nhỏ xíu, miệng cười nhếch mép kiểu trùm mafia biển cả, vẽ nên một bản đồ 3D chi tiết đến từng vết nứt vi mô trên cánh cửa thép trong tâm trí chú cá voi; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L256</summary>

```text
HÌNH L256 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Phát hiện mục tiêu! Điểm yếu nằm ở chiếc then cài thủy lực số hai bên dưới góc phải, nơi các bu-lông kim loại đã bị nước xói mòn tạo ra một kẽ hở đúng năm mi-li-mét!". Bố cục: Hình vẽ quét 3D của chiếc then cài bằng thép hiển thị một vệt nứt màu đỏ nhấp nháy ngay tại khớp xoay bản lề; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L257</summary>

```text
HÌNH L257 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Âm thanh dội về chi tiết đến mức cá voi có thể phân biệt được độ dày của lớp rỉ sét và hướng ứng suất của từng chiếc đinh tán kim loại!". Bố cục: Màn hình mô phỏng não bộ cá voi xử lý tín hiệu âm thanh thành hình ảnh 3D chân thực như chụp cắt lớp vi tính; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L258</summary>

```text
HÌNH L258 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cá Voi Sát Thủ lùi lại 50 mét để lấy đà. Không cần súng phóng lựu, vũ khí của đại ca đại dương chính là kỹ thuật tạo sóng thần đồng bộ trứ danh từng khiến các nhà khoa học biển kinh ngạc!". Bố cục: chú Cá Voi Sát Thủ hoạt hình thân đen bóng bụng trắng tinh, vây lưng cao vút cắm ăng-ten định vị sonar nhỏ xíu, miệng cười nhếch mép kiểu trùm mafia biển cả bơi lùi lại vùng nước sâu, uốn mình uyển chuyển tích tụ một lượng động năng khổng lồ vào chiếc vây đuôi rộng hai mét; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L259</summary>

```text
HÌNH L259 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nghiên cứu tại vùng biển Nam Cực ghi nhận: loài cá voi sát thủ có thể phối hợp bơi nước rút và quất mạnh chiếc vây đuôi để tạo nên những bức tường sóng thần cao hơn một mét rưỡi, thổi bay mục tiêu trên các tảng băng trôi!". Bố cục: Tranh minh họa tư liệu sinh học: đàn cá voi sát thủ bơi dàn hàng ngang quất đuôi đồng nhịp, tạo nên một con sóng khổng lồ cuộn trào dâng cao đánh sập mục tiêu; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lớp kim loại kẽm và mangan nguyên chất tẩm vào đầu răng biến bầy kiến này thành những chiếc máy cắt kim cương di động dưới lòng đất!". Bố cục: Hình ảnh hiển vi quét điện tử đầu răng kiến phát sáng ánh thép kim loại; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L260</summary>

```text
HÌNH L260 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và hôm nay, trong không gian khép kín của hào ngầm, uy lực của con sóng này sẽ bị nén lại thành một cú đấm thủy lực có sức tàn phá gấp mười lần!". Bố cục: Sơ đồ động lực học: sóng nước bị hai vách đá thu hẹp lại, tạo thành một mũi nhọn áp lực nước cực lớn hướng thẳng vào then cài; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L261</summary>

```text
HÌNH L261 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tăng tốc! Cá Voi Sát Thủ phóng vút đi với vận tốc nước rút kinh hoàng: 56 km/h! Thân hình 6 tấn lao đi như một quả ngư lôi sống!". Bố cục: chú Cá Voi Sát Thủ hoạt hình thân đen bóng bụng trắng tinh, vây lưng cao vút cắm ăng-ten định vị sonar nhỏ xíu, miệng cười nhếch mép kiểu trùm mafia biển cả rẽ nước lao đi như tên bắn, bọt nước sủi tung trắng xóa dọc hai bên thân mình đen bóng, ánh mắt rực lửa quyết chiến; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L262</summary>

```text
HÌNH L262 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cách cánh cửa đập đúng 5 mét, anh chàng bất ngờ thực hiện một cú quay ngoắt 100 80° điệu nghệ, quất toàn bộ sức mạnh của cơ đuôi khổng lồ xuống mặt nước!". Bố cục: chú Cá Voi Sát Thủ hoạt hình thân đen bóng bụng trắng tinh, vây lưng cao vút cắm ăng-ten định vị sonar nhỏ xíu, miệng cười nhếch mép kiểu trùm mafia biển cả xoay mình quật mạnh chiếc vây đuôi khổng lồ xuống nước với một lực hàng chục tấn, tạo ra một tiếng nổ ục kinh hoàng chấn động đáy hào; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L263</summary>

```text
HÌNH L263 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ầm! Một bức tường sóng thủy lực cao vút bị ép chặt trong khe đá, lao thẳng vào chiếc then cài bị nứt với áp suất hàng trăm tấn trên một mét vuông!". Bố cục: Con sóng thủy lực cực mạnh đập thẳng vào khớp bản lề cánh cửa van thép, tạo nên một vụ nổ bọt khí chói lòa và tiếng kim loại gãy răng rắc; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L264</summary>

```text
HÌNH L264 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Răng rắc... rầm! Chiếc then cài thủy lực bị uốn cong rồi gãy vụn! Cánh cửa van thép khổng lồ bị sức nước xô ngã ngửa ra sau, mở toang một lỗ hổng đường kính 3 mét!". Bố cục: Cánh cửa van thép bật tung khỏi bản lề, dòng nước ngầm ầm ầm đổ qua lỗ hổng thoát ra ngoài hạ lưu, mực nước trong hào ngầm bắt đầu rút xuống nhanh chóng; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L265</summary>

```text
HÌNH L265 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Áp suất nước giải phóng tạo nên một cơn lốc xoáy nước xoáy tròn cuốn phăng toàn bộ rác rưởi và chướng ngại vật dưới lòng hào ngầm!". Bố cục: Dòng nước thoát nhanh tạo ra tiếng gầm vang dội khắp căn hầm ngầm của pháo đài; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L266</summary>

```text
HÌNH L266 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mực nước trong hào ngầm tụt dốc không phanh! Lòng hào trơ ra những phiến đá cuội trơn nhẵn, mở ra một lối đi bộ khô ráo cho toàn bộ biệt đội đặc nhiệm!". Bố cục: Nước rút hết để lộ đáy hào bằng phẳng, các bậc thang đá dẫn thẳng lên cửa tầng sáu của pháo đài xuất hiện rõ mồn một; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L267</summary>

```text
HÌNH L267 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cá Voi Sát Thủ nhô nửa thân mình lên mặt nước ở đoạn kênh thông thoáng, phun một cột nước trắng xóa lên trần hang, cất tiếng kêu éc éc đắc thắng qua micro!". Bố cục: chú Cá Voi Sát Thủ hoạt hình thân đen bóng bụng trắng tinh, vây lưng cao vút cắm ăng-ten định vị sonar nhỏ xíu, miệng cười nhếch mép kiểu trùm mafia biển cả ngửa cổ phun nước tạo thành một chiếc cầu vồng nhỏ dưới ánh đèn pin, vẫy hai vây ngực chào Chỉ Huy Mật Vụ đầy ngạo nghễ.
```
</details>

<details><summary>L268</summary>

```text
HÌNH L268 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Biểu tượng sóng nước của Cửa Ải 5 trên {BOARD} nhấp nháy rồi chuyển sang màu xanh ngọc bích rực rỡ! Năm trên 7 cửa ải đã bị biệt đội hạ gục gọn gàng!". Bố cục: bản đồ hologram 3D của Pháo Đài Tự Nhiên nổi lơ lửng trong không khí, hiển thị 7 cửa ải an ninh phát sáng đỏ và thanh tiến độ phá khóa màu xanh ngọc (không có chữ, không có số) cập nhật tín hiệu: năm biểu tượng cửa ải đã chuyển sang màu xanh ngọc, thanh tiến độ phá khóa đã đạt hơn bảy mươi phần trăm; anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm đứng dậy vỗ tay tán thưởng.
```
</details>

<details><summary>L269</summary>

```text
HÌNH L269 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng thử thách phía trước mới thực sự là bài kiểm tra độ cứng của hộp sọ và tinh thần đồng đội: Boong-ke Bê Tông Cốt Thép của Cửa Ải 6!". Bố cục: Trước mặt biệt đội là một bức tường thành khổng lồ xây bằng các khối đá granite đen dày hai mét, không có kẽ hở, không có cửa sổ, trơn lỳ như một khối đá nguyên khối; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đủ 10 đặc vụ. Bảy cửa ải. Và đúng 60 phút trước khi hệ thống phòng thủ của pháo đài khóa vĩnh viễn lối vào.". Bố cục: Toàn bộ mười đặc vụ đứng quây quần quanh bàn tác chiến, nhìn chằm chằm vào bản đồ hologram phát sáng; anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm chống hai tay xuống bàn, ánh mắt sắc lạnh.
```
</details>

<details><summary>L270</summary>

```text
HÌNH L270 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đạn pháo thông thường bắn vào đây chỉ để lại một vết xước nhỏ. Muốn phá vỡ bức tường này, chúng ta cần sự kết hợp giữa một chiếc búa khoan sinh học có lực gia tốc hàng ngàn G và một đại đội công binh tí hon có hàm răng thép!". Bố cục: anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm nhìn sang chú Chim Gõ Kiến hoạt hình mào lông đỏ rực dựng đứng, mỏ dài sắc nhọn như mũi khoan titan, đội mũ bảo hộ lao động màu vàng có gắn đèn pin thợ mỏ đang đội mũ bảo hộ vàng và tiểu đội ba chú Kiến Cắt Lá hoạt hình màu nâu đỏ, đầu to mang hàm răng kim loại sáng loáng, đội mũ cối công binh màu xanh lá, đang vác những mảnh lá xanh như chiếc khiên chắn đang xếp hàng chỉnh tề: "Đặc vụ Gõ Kiến và Đại Đội Kiến Cắt Lá, mục tiêu công sự kiên cố nhất đã xuất hiện. Chuẩn bị khai hỏa!"
```
</details>

<details><summary>L271</summary>

```text
HÌNH L271 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cặp đôi búa khoan và máy đào đất chuẩn bị thực hiện màn công phá ngoạn mục chưa từng có!". Bố cục: chú Chim Gõ Kiến hoạt hình mào lông đỏ rực dựng đứng, mỏ dài sắc nhọn như mũi khoan titan, đội mũ bảo hộ lao động màu vàng có gắn đèn pin thợ mỏ và tiểu đội ba chú Kiến Cắt Lá hoạt hình màu nâu đỏ, đầu to mang hàm răng kim loại sáng loáng, đội mũ cối công binh màu xanh lá, đang vác những mảnh lá xanh như chiếc khiên chắn cùng đứng trước bức tường đá granite đen tuyền, ánh mắt quyết tâm sẵn sàng cho trận đánh lớn.
```
</details>

<details><summary>L272</summary>

```text
HÌNH L272 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sóng âm sonar của cá voi sát thủ mạnh đến mức có thể làm choáng váng các loài cá nhỏ xung quanh chỉ bằng một tiếng nhấp chuột âm thanh đanh thép!". Bố cục: Các luồng sóng âm thanh màu xanh dương lan tỏa làm rung chuyển các khối đá ngầm dưới đáy hào nước; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L273</summary>

```text
HÌNH L273 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hệ thống não bộ khổng lồ nặng tới 5kg của cá voi sát thủ có thể phân tích hàng triệu tín hiệu âm thanh dội về trong 0,001 giây, tái hiện lại cấu trúc không gian ba chiều hoàn hảo!". Bố cục: Đồ họa máy tính mô phỏng não bộ cá voi xử lý bản đồ 3D đáy nước ngầm; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L274</summary>

```text
HÌNH L274 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cú quất đuôi sóng thần của đại ca biển cả đã chứng minh sức mạnh cơ học vô song của loài động vật có vú thống trị toàn bộ chuỗi thức ăn đại dương!". Bố cục: chú Cá Voi Sát Thủ hoạt hình thân đen bóng bụng trắng tinh, vây lưng cao vút cắm ăng-ten định vị sonar nhỏ xíu, miệng cười nhếch mép kiểu trùm mafia biển cả lượn một vòng điệu nghệ dưới làn nước trong vắt sau khi đập tan cánh cửa đập; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L275</summary>

```text
HÌNH L275 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sức mạnh của bầy cá voi sát thủ không chỉ nằm ở cơ bắp mà còn nằm ở sự truyền thừa tri thức săn mồi qua hàng trăm thế hệ gia tộc mẫu hệ!". Bố cục: Đàn cá voi sát thủ bơi uốn lượn dưới đại dương xanh biếc, cá voi mẹ dẫn đầu truyền dạy kỹ năng bơi lội cho cá voi con; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L276</summary>

```text
HÌNH L276 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cánh cửa van đập nước ngầm bị đánh sập là minh chứng hùng hồn cho thấy không một công trình nhân tạo nào có thể ngăn cản được sức mạnh của đại dương bao la!". Bố cục: Dòng nước ngầm trong vắt phản chiếu ánh trăng rọi qua khe đá, mở ra con đường thẳng tiến lên các tầng cao; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L277</summary>

```text
HÌNH L277 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bức tường Boong-ke của Cửa Ải 6 là chướng ngại vật vật lý kiên cố nhất trong toàn bộ Pháo Đài Tự Nhiên. Các khối đá granite đen dày 2 mét được ghép khít khao đến mức một lưỡi dao cạo cũng không thể lách qua!". Bố cục: Bức tường thành khổng lồ xây bằng đá granite đen bóng sừng sững chắn ngang lối đi, bề mặt đá nhẵn thín không một kẽ hở, ánh sáng đèn pha phản chiếu lạnh lùng trên mặt đá; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L278</summary>

```text
HÌNH L278 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Độ cứng của đá granite nằm ở thang điểm bảy trên thang độ cứng khoáng vật, chỉ đứng sau ngọc bích và kim cương. Mọi nỗ lực dùng búa tạ của con người đập vào đây sẽ chỉ làm mẻ búa và gãy tay kẻ đập!". Bố cục: Một chiếc búa sắt bổ xuống mặt đá granite nảy ngược trở lại tóe lửa, mặt đá chỉ để lại một vệt trắng mờ nhạt không hề suy suyển; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L279</summary>

```text
HÌNH L279 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng đêm nay, pháo đài phải đối đầu với một cỗ máy khoan sinh học sở hữu chiếc đầu có khả năng triệt tiêu xung chấn thần kỳ nhất vũ trụ: Đặc vụ Chim Gõ Kiến!". Bố cục: chú Chim Gõ Kiến hoạt hình mào lông đỏ rực dựng đứng, mỏ dài sắc nhọn như mũi khoan titan, đội mũ bảo hộ lao động màu vàng có gắn đèn pin thợ mỏ đứng chỉnh lại chiếc mũ bảo hộ màu vàng có gắn đèn pin thợ mỏ, vươn chiếc cổ thon dài chắc nịch, chiếc mỏ nhọn hoắt bóng loáng như một mũi khoan bằng hợp kim titan; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thông báo khẩn từ trung tâm giám sát vệ tinh: pháo đài vừa kích hoạt toàn bộ lưới phòng vệ cấp độ đỏ! Toàn đội vào vị trí tác chiến!". Bố cục: Màn hình điều khiển trung tâm chuyển sang màu đỏ rực, các dòng chữ cảnh báo mã hóa chạy liên hồi trên màn hình (không chữ, không số); KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L280</summary>

```text
HÌNH L280 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cơ bắp cổ của chim gõ kiến được cấu tạo từ các bó cơ xoắn siêu dày, có thể phát ra lực đẩy tương đương với một chiếc búa tạ mini bổ xuống bề mặt mục tiêu!". Bố cục: Hình cắt lớp giải phẫu cơ cổ của chim gõ kiến với các bó cơ màu đỏ sẫm đan chéo nhau hình mạng lưới trợ lực; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L281</summary>

```text
HÌNH L281 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy tưởng tượng lực va chạm khủng khiếp mà đầu chim gõ kiến phải chịu đựng trong mỗi cú mổ. Các nhà cơ sinh học tại đại học Bắc Kinh đã gắn các cảm biến siêu vi để đo đạc và thu về những con số rùng mình!". Bố cục: Sơ đồ giải phẫu sọ chim gõ kiến với các đường sóng xung kích màu đỏ lan tỏa từ đỉnh mỏ qua hộp sọ, các thông số kỹ thuật hiển thị chi tiết (không chữ, không số); KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L282</summary>

```text
HÌNH L282 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi gõ vào thân cây gỗ hay đá cứng, đầu của chim gõ kiến phải chịu một lực gia tốc va đập lên tới 1200G!". Bố cục: Đồ họa đo lực va chạm: mũi tên lực hướng thẳng vào đầu chim chỉ mức 1200G, gấp một trăm lần lực gia tốc khiến một phi công chiến đấu tinh nhuệ bất tỉnh nhân sự! KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L283</summary>

```text
HÌNH L283 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và anh chàng không chỉ gõ một lần rồi nghỉ. Tần số mổ của chim gõ kiến đạt tới 20 lần/giây, với vận tốc đầu mỏ lao tới sáu mét một giây!". Bố cục: Đồng hồ đo tần số dao động hiển thị vạch kim rung liên tục ở mức 20 chu kỳ một giây, hình ảnh mỏ chim chuyển động nhanh đến mức nhòe mờ như cánh quạt máy bay; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L284</summary>

```text
HÌNH L284 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Với lực đập 1200G lặp lại 20 lần/giây, bất kỳ bộ não sinh vật nào cũng sẽ bị dập nát thành cháo. Nhưng Chim Gõ Kiến vẫn tỉnh táo, minh mẫn và mắt sáng như sao!". Bố cục: Cận cảnh gương mặt tươi rói của chú Chim Gõ Kiến hoạt hình mào lông đỏ rực dựng đứng, mỏ dài sắc nhọn như mũi khoan titan, đội mũ bảo hộ lao động màu vàng có gắn đèn pin thợ mỏ, đôi mắt tròn xoe linh hoạt, không hề có bất kỳ dấu hiệu hoa mắt chóng mặt nào; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L285</summary>

```text
HÌNH L285 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Màng nháy mắt của chim gõ kiến tự động đóng sập lại 0,001 giây trước mỗi cú va chạm, giữ cho nhãn cầu không bị văng ra khỏi hốc mắt!". Bố cục: Chiếc màng nháy dày bảo vệ mắt chim đóng lại như một chiếc kính bảo hộ thể thao trong khoảnh khắc mỏ chạm đá; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L286</summary>

```text
HÌNH L286 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bí mật nằm ở bộ giáp chống rung chấn ba lớp tinh vi mà tạo hóa đã ban tặng cho loài chim này!". Bố cục: Bản vẽ kỹ thuật phóng to ba tầng bảo vệ bên trong hộp sọ chim gõ kiến: xương mỏ đàn hồi, xương móng hyoid và lớp xương xốp vi mô; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L287</summary>

```text
HÌNH L287 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thứ nhất, chiếc xương móng hyoid của chim gõ kiến không nằm ở cuống họng như người, mà dài ngoằng, quấn một vòng từ đáy hàm vòng qua sau gáy lên tận đỉnh đầu rồi chui vào lỗ mũi!". Bố cục: Cấu trúc chiếc xương móng hyoid màu vàng nhạt quấn trọn quanh hộp sọ như chiếc dây đai an toàn ba điểm của xe đua Công Thức Một, siết chặt và giữ cố định não bộ; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L288</summary>

```text
HÌNH L288 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thứ hai, mỏ trên dài hơn mỏ dưới đúng một mi-li-mét, giúp chuyển hướng các sóng xung kích gây hại thành sóng trượt vô hại đi xuống thân mình!". Bố cục: Hình phóng to hai đầu mỏ lệch nhau một mi-li-mét: sóng xung kích màu đỏ bị bẻ gãy và trượt dọc theo xương ức chim mà không truyền thẳng vào hộp sọ; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L289</summary>

```text
HÌNH L289 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và thứ ba, xương sọ của chim gõ kiến là một cấu trúc xốp vi mô chứa vô số lỗ rỗng chứa không khí, đóng vai trò như chiếc đệm khí lò xo đàn hồi triệt tiêu toàn bộ chấn động trước khi chạm tới màng não!". Bố cục: Lát cắt hiển vi lớp xương xốp hộp sọ trông như một miếng bọt biển kim loại siêu bền, hấp thụ năng lượng va đập trong chớp mắt; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các đặc vụ nghe rõ: phi vụ này tuyệt đối không có chỗ cho sự sai sót. Không có thử lại. Không có cứu viện.". Bố cục: anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm giơ chiếc máy tính bảng mật mã lên ngang ngực, ngón tay bấm nút xác nhận màu đỏ; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L290</summary>

```text
HÌNH L290 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tọa độ điểm yếu của bức tường đã được quét xong! Đó là ba điểm nứt ứng suất ngầm nơi ba khối đá granite giao nhau!". Bố cục: Đèn pin thợ mỏ trên mũ của chú Chim Gõ Kiến hoạt hình mào lông đỏ rực dựng đứng, mỏ dài sắc nhọn như mũi khoan titan, đội mũ bảo hộ lao động màu vàng có gắn đèn pin thợ mỏ chiếu luồng ánh sáng vàng rực vào ba điểm giao nhau giữa các khối đá granite; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L291</summary>

```text
HÌNH L291 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khai hỏa! Chim Gõ Kiến bám chặt bốn móng vuốt vào vách đá, đuôi tì làm điểm tựa kiên cố, bắt đầu chuỗi khoan phá thần tốc!". Bố cục: chú Chim Gõ Kiến hoạt hình mào lông đỏ rực dựng đứng, mỏ dài sắc nhọn như mũi khoan titan, đội mũ bảo hộ lao động màu vàng có gắn đèn pin thợ mỏ vào tư thế tác chiến vững như bàn thạch, chiếc đầu bắt đầu lao vào mổ liên hoàn với tốc độ ánh sáng; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L292</summary>

```text
HÌNH L292 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cốc cốc cốc cốc cốc cốc cốc! Tiếng mỏ va chạm vào đá granite rít lên như tiếng súng máy liên thanh, các tia lửa điện nổ lách tách chói lòa trong bóng tối!". Bố cục: Đầu mỏ gõ liên hồi vào vách đá tạo thành những chùm tia lửa vàng cam rực rỡ, bụi đá mịn bay mù mịt quanh thân chim; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L293</summary>

```text
HÌNH L293 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chỉ trong vòng 45 giây, ba lỗ khoan tròn sâu 10cm đã xuất hiện ngay trên tim của các khối đá! Các vết nứt chân chim bắt đầu lan rộng ra xung quanh như mạng nhện!". Bố cục: Bề mặt đá granite rạn nứt thành các đường vân nứt gãy lớn, phát ra những tiếng răng rắc báo hiệu kết cấu bắt đầu suy yếu; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L294</summary>

```text
HÌNH L294 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đến lượt lực lượng công binh bí mật vào sân! Chim Gõ Kiến lùi lại nhường đường cho Đại Đội Kiến Cắt Lá xuất kích!". Bố cục: chú Chim Gõ Kiến hoạt hình mào lông đỏ rực dựng đứng, mỏ dài sắc nhọn như mũi khoan titan, đội mũ bảo hộ lao động màu vàng có gắn đèn pin thợ mỏ gạt mồ hôi trên trán gật đầu ra hiệu, từ khe đá phía dưới, hàng ngàn chú kiến cắt lá ùa ra thành một dòng thác màu nâu đỏ; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L295</summary>

```text
HÌNH L295 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đừng coi thường những chú kiến nhỏ bé này! Nghiên cứu mới nhất đăng trên tạp chí Báo Cáo Khoa Học của Nature đã phát hiện: hàm răng của kiến cắt lá được tẩm một lớp kim loại nặng gồm kẽm và mangan nguyên chất!". Bố cục: Bản chụp kính hiển vi điện tử quét chiếc răng kìm của kiến cắt lá: đầu răng phát sáng ánh kim loại thép siêu cứng nhờ sự phân bố đồng đều của các nguyên tử kẽm và mangan; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L296</summary>

```text
HÌNH L296 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lớp kim loại nặng này biến chiếc hàm răng chitin của kiến cắt lá thành những lưỡi cưa tẩm thép không gỉ, sắc bén và bền bỉ gấp ba lần răng của côn trùng thông thường!". Bố cục: Mô phỏng chiếc răng kiến cắt xuyên qua khoáng vật đá cứng dễ như cắt một lát bơ mềm; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L297</summary>

```text
HÌNH L297 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hàng ngàn chú kiến cắt lá cùng lúc thò hàm răng thép vào các kẽ nứt do chim gõ kiến vừa tạo ra, bắt đầu nghiền nát và bốc dỡ từng hạt bụi đá granite ra ngoài!". Bố cục: Đàn kiến phối hợp nhịp nhàng: những chú kiến to lớn dùng hàm bẩy các mảnh đá vụn, những chú kiến nhỏ hơn khuân vác các mẩu đá chạy ra xa; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L298</summary>

```text
HÌNH L298 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khả năng khuân vác gấp 50 lần trọng lượng cơ thể giúp bầy kiến dọn sạch hàng tạ đá vụn chỉ trong vòng chưa đầy 2 phút!". Bố cục: Dòng kiến di chuyển thoăn thoắt mang theo những viên sỏi đá ra khỏi kẽ nứt, làm rỗng hoàn toàn chân móng bức tường thành; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L299</summary>

```text
HÌNH L299 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khoét móng! Đục rãnh! Bẩy then! Đại đội công binh kiến cắt lá đào khoét chân tường đá với tốc độ của một cỗ máy xúc công nghiệp hiện đại!". Bố cục: Chân móng của khối đá granite khổng lồ bị khoét rỗng một khoảng trống lớn, mất đi điểm tựa thăng bằng trọng lực; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mọi chi tiết trong kế hoạch này đều dựa trên những báo cáo sinh học tối tân nhất vừa được giải mã từ các phòng thí nghiệm hàng đầu thế giới.". Bố cục: Cận cảnh một tập tài liệu nghiên cứu khoa học có hình ảnh phóng to của vòi nén khí chim cắt, tế bào nước màu lạc đà và hàm răng kiến bọc kim loại nặng nằm dưới đèn soi UV; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L300</summary>

```text
HÌNH L300 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Toàn bộ khối đá granite nặng 10 tấn bắt đầu nghiêng dần về phía trước. Chim Gõ Kiến bay lên, tung cú mổ quyết định cuối cùng vào chiếc chốt bản lề trên đỉnh!". Bố cục: chú Chim Gõ Kiến hoạt hình mào lông đỏ rực dựng đứng, mỏ dài sắc nhọn như mũi khoan titan, đội mũ bảo hộ lao động màu vàng có gắn đèn pin thợ mỏ lấy đà từ trên cao bổ thẳng một cú mổ trời giáng vào đỉnh khối đá đang mất thăng bằng; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L301</summary>

```text
HÌNH L301 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Rầm! Khối đá granite khổng lồ đổ sập xuống sàn đá, vỡ tan thành những mảnh đá vụn vô hại, mở toang một cửa vòm rộng thênh thang dẫn thẳng vào Cửa Ải 7!". Bố cục: Bức tường boong-ke sụp đổ hoàn toàn trong làn khói bụi mù mịt, ánh sáng đỏ rực từ sa mạc bên ngoài ùa vào soi rọi con đường tiến bước; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L302</summary>

```text
HÌNH L302 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Biểu tượng boong-ke đá trên {BOARD} chuyển sang màu xanh ngọc bích rực rỡ! Sáu trên 7 cửa ải đã bị biệt đội đặc nhiệm đánh sập không còn một dấu vết!". Bố cục: bản đồ hologram 3D của Pháo Đài Tự Nhiên nổi lơ lửng trong không khí, hiển thị 7 cửa ải an ninh phát sáng đỏ và thanh tiến độ phá khóa màu xanh ngọc (không có chữ, không có số) sáng bừng lên với sáu biểu tượng màu xanh ngọc, thanh tiến độ phá khóa đã chạm mốc tám mươi lăm phần trăm; anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm nở nụ cười tự hào.
```
</details>

<details><summary>L303</summary>

```text
HÌNH L303 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chim Gõ Kiến đậu trên đống đá vụn, giơ chiếc mỏ nhọn hoắt lên trời làm động tác gõ tạ ơn khán giả, bên cạnh là đàn kiến cắt lá đang vẫy những mảnh lá xanh ăn mừng chiến thắng vang dội!". Bố cục: chú Chim Gõ Kiến hoạt hình mào lông đỏ rực dựng đứng, mỏ dài sắc nhọn như mũi khoan titan, đội mũ bảo hộ lao động màu vàng có gắn đèn pin thợ mỏ cùng tiểu đội ba chú Kiến Cắt Lá hoạt hình màu nâu đỏ, đầu to mang hàm răng kim loại sáng loáng, đội mũ cối công binh màu xanh lá, đang vác những mảnh lá xanh như chiếc khiên chắn tạo dáng chụp ảnh lưu niệm trên đống đổ nát của bức tường đá granite, vẻ mặt rạng rỡ của những anh hùng công binh.
```
</details>

<details><summary>L304</summary>

```text
HÌNH L304 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng cánh cửa cuối cùng ngăn cách biệt đội với kho báu trung tâm đang hiện ra trước mắt: Cửa Ải 7 — Bức Tường Vách Đứng 90 Độ và Lò Lửa Sa Mạc 50 Độ C!". Bố cục: Khung cảnh Cửa Ải Bảy hiện ra: một thung lũng lòng chảo sa mạc cát đỏ rực bốc hơi nóng hầm hập năm mươi độ C, ở giữa là ngọn tháp nhẵn thín dựng đứng chín mươi độ cao chót vót không một gờ bám; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L305</summary>

```text
HÌNH L305 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không thể bay qua vì bão nhiệt cuốn phăng mọi luồng khí, cũng không thể đào hầm vì nền cát lún di động. Chỉ có sự phối hợp giữa một cỗ xe tăng chịu nhiệt và một bậc thầy leo vách đá mới có thể giải mã cánh cửa tối thượng này!". Bố cục: anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm quay sang nhìn chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao và chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt: "Đặc vụ Lạc Đà và Đặc vụ Dê Núi, cánh cửa kho báu nằm trên đỉnh ngọn tháp đó. Hãy cho thế giới thấy thế nào là đỉnh cao sinh tồn!"
```
</details>

<details><summary>L306</summary>

```text
HÌNH L306 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cặp đôi sa mạc và vách đá chuẩn bị bước vào cuộc chinh phục đỉnh cao nhất của pháo đài!". Bố cục: chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao và chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt cùng bước qua đống đổ nát, tiến vào chảo lửa sa mạc với ánh mắt kiên định không hề sợ hãi.
```
</details>

<details><summary>L307</summary>

```text
HÌNH L307 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Để bảo vệ đôi mắt khỏi bụi đá và chấn động cực mạnh, mi mắt của chim gõ kiến có thể tự động co thắt các mạch nước màu quanh võng mạc để duy trì huyết áp ổn định trong từng cú mổ!". Bố cục: Bản vẽ cắt lớp mắt chim gõ kiến với hệ thống mạch nước màu co giãn thông minh bảo vệ thị lực tuyệt đối; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L308</summary>

```text
HÌNH L308 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong khi đó, lớp kim loại kẽm và mangan trên răng của kiến cắt lá được phân bố đồng đều đến mức độ nguyên tử, giúp chiếc răng không bao giờ bị mẻ dù cắn vào đá granite cứng nhất!". Bố cục: Kính hiển vi lực nguyên tử quét lớp phủ kim loại nặng trên bề mặt răng kiến; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L309</summary>

```text
HÌNH L309 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sự kết hợp giữa công nghệ khoan va đập của loài chim và công nghệ cưa cắt kim loại của loài kiến đã tạo nên một kỳ tích công binh chưa từng có trong lịch sử điệp viên!". Bố cục: chú Chim Gõ Kiến hoạt hình mào lông đỏ rực dựng đứng, mỏ dài sắc nhọn như mũi khoan titan, đội mũ bảo hộ lao động màu vàng có gắn đèn pin thợ mỏ và tiểu đội ba chú Kiến Cắt Lá hoạt hình màu nâu đỏ, đầu to mang hàm răng kim loại sáng loáng, đội mũ cối công binh màu xanh lá, đang vác những mảnh lá xanh như chiếc khiên chắn cùng đứng trên đống đá vụn mỉm cười tự hào.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chúng ta không dùng súng đạn. Vũ khí tối thượng của biệt đội chính là những tuyệt kỹ tiến hóa hàng trăm triệu năm của tạo hóa!". Bố cục: Mười đặc vụ cùng giơ nắm tay hoặc giơ móng vuốt chạm vào nhau ở giữa bàn họp, ánh sáng xanh từ hologram chiếu rực rỡ lên khuôn mặt đầy quyết tâm; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L310</summary>

```text
HÌNH L310 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhịp gõ búa thần tốc 20 lần/giây của chim gõ kiến tạo nên một bản hòa âm cơ học rộn rã làm bừng tỉnh cả góc pháo đài tối tăm!". Bố cục: chú Chim Gõ Kiến hoạt hình mào lông đỏ rực dựng đứng, mỏ dài sắc nhọn như mũi khoan titan, đội mũ bảo hộ lao động màu vàng có gắn đèn pin thợ mỏ gõ mỏ nhịp nhàng như một nghệ sĩ đánh trống cự phách, các tia lửa vàng cam nhảy múa theo từng cú mổ; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L311</summary>

```text
HÌNH L311 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hàng ngàn chú kiến cắt lá đồng loạt vác đá diễu hành dưới ánh đèn pin thợ mỏ, tạo nên một cảnh tượng công binh hoành tráng chưa từng thấy!". Bố cục: tiểu đội ba chú Kiến Cắt Lá hoạt hình màu nâu đỏ, đầu to mang hàm răng kim loại sáng loáng, đội mũ cối công binh màu xanh lá, đang vác những mảnh lá xanh như chiếc khiên chắn xếp hàng dài ngay ngắn như những người lính tí hon kỷ luật và kiên cường; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L312</summary>

```text
HÌNH L312 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cửa Ải 7 là phòng tuyến cuối cùng và khắc nghiệt nhất của Pháo Đài Tự Nhiên: Lò Lửa Sa Mạc kết hợp với Bức Tường Vách Đứng 90 Độ!". Bố cục: Cảnh thung lũng lòng chảo sa mạc cát đỏ rực bốc lên những làn sóng nhiệt méo mó dưới ánh nắng gắt, nhiệt kế chỉ vạch năm mươi độ C đỏ rực; chính giữa là ngọn tháp đá granite dựng đứng chín mươi độ nhẵn bóng như gương; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L313</summary>

```text
HÌNH L313 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhiệt độ trên mặt cát sa mạc lúc này đo được là 50°C! Không khí khô khốc như lò nung có thể hút cạn từng giọt nước trong cơ thể của bất kỳ sinh vật nào chỉ trong vòng chưa đầy 15 phút!". Bố cục: Mặt cát sa mạc đỏ rực nứt nẻ, ảo ảnh hơi nóng bốc lên ngùn ngụt làm mờ ảo khung cảnh phía trước; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L314</summary>

```text
HÌNH L314 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mọi phương tiện cơ giới mang vào đây đều sẽ bị cát lún nuốt chửng bánh xe, động cơ quá nhiệt và bốc cháy.". Bố cục: Một chiếc xe bọc thép hoạt hình nằm lún ngập nửa thân trong cát đỏ, nắp ca-pô bốc khói đen nghi ngút; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L315</summary>

```text
HÌNH L315 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gió sa mạc cuốn theo những cơn bão bụi silic sắc nhọn có thể làm xước rách giác mạc và phá hủy hệ hô hấp của người thường!". Bố cục: Bão cát mù mịt quét qua thung lũng, cát bụi bay ràn rạt như những hạt đạn thủy tinh; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L316</summary>

```text
HÌNH L316 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng kẻ đang ung dung sải bước trên chảo cát nóng rẫy này lại chính là cỗ xe tăng sinh học tối thượng của hoang mạc: Đặc vụ Lạc Đà Sa Mạc!". Bố cục: chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao thong thả bước từng bước dài vững chãi trên cát lún đỏ rực, bàn chân xòe rộng có đệm thịt đàn hồi nâng đỡ cơ thể không hề bị lún; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L317</summary>

```text
HÌNH L317 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trên lưng Lạc Đà không chở súng đạn, mà đang cõng theo người đồng đội leo núi cừ khôi nhất: Đặc vụ Dê Núi Bắc Mỹ! Cặp bài trùng này chuẩn bị thực hiện màn phối hợp ngoạn mục nhất lịch sử điệp viên!". Bố cục: chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt đứng vững vàng trên lưng lạc đà, bốn móng guốc bám chắc vào khung đai thồ hàng, bộ lông trắng muốt bay nhẹ trong gió sa mạc; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L318</summary>

```text
HÌNH L318 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bí mật nào giúp Lạc Đà Sa Mạc thản nhiên vượt qua vùng nhiệt độ 50°C mà không hề nhỏ một giọt mồ hôi? Hãy nhìn sâu vào hệ tuần hoàn kỳ diệu của anh chàng này!". Bố cục: Bản vẽ y khoa hiển vi phóng to giọt nước màu của lạc đà dưới kính hiển vi: các tế bào hồng cầu có hình bầu dục độc nhất vô nhị đang phát sáng óng ánh; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L319</summary>

```text
HÌNH L319 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tất cả các loài động vật có vú trên Trái Đất, bao gồm cả con người, đều có tế bào hồng cầu hình tròn dẹt. Khi cơ thể mất nước, hồng cầu tròn sẽ dính bết lại làm tắc nghẽn mạch nước màu, dẫn đến đột quỵ.". Bố cục: Sơ đồ so sánh: hồng cầu hình tròn của người bị biến dạng và vón cục lại khi thiếu nước, trong khi hồng cầu hình oval của lạc đà vẫn trôi chảy mượt mà qua các mao mạch nhỏ; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cửa Ải 1 đã hiện ra trên màn hình radar: Không phận tử thần với áp suất gió kinh hoàng và lưới quét quang học. Mật danh Tia Chớp, đến lượt cậu cất cánh!". Bố cục: Cánh cửa hầm ngầm từ từ mở toang ra bầu trời đêm đầy mây đen vần vũ, phía xa là ngọn tháp canh sừng sững của pháo đài; chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng sải rộng đôi cánh lao vút lên không trung xé toạc màn đêm.
```
</details>

<details><summary>L320</summary>

```text
HÌNH L320 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng hồng cầu của Lạc Đà lại có hình bầu dục thuôn dài! Cấu trúc oval đặc biệt này cho phép chúng tiếp tục lưu thông trơn tru ngay cả khi nước màu trở nên đặc quánh do cơ thể mất tới 25% lượng nước!". Bố cục: Dòng tế bào nước màu hình oval màu đỏ tươi lướt đi êm ả qua các mạch nước màu ngoằn ngoèo, duy trì việc vận chuyển oxy đến từng tế bào mà không hề bị tắc nghẽn; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L321</summary>

```text
HÌNH L321 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và khi gặp nguồn nước, hồng cầu hình bầu dục của lạc đà có thể giãn nở tới 240% thể tích mà không hề bị vỡ! Anh chàng có thể nạp 100 lít nước chỉ trong mười phút ngắn ngủi!". Bố cục: Hình mô phỏng một tế bào hồng cầu oval phồng to gấp đôi như một quả bóng cao su bền bỉ mà không hề bị thủng rách; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L322</summary>

```text
HÌNH L322 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa hết, thân nhiệt của Lạc Đà Sa Mạc là một cỗ máy điều hòa nhiệt độ sinh học tự động: ban đêm hạ xuống 34°C để tích trữ khí lạnh, ban ngày tăng dần lên 41°C mà không cần đổ mồ hôi làm mát!". Bố cục: Biểu đồ nhiệt kế sinh học dao động tự nhiên từ 34°C đến 41°C, giữ cho cơ thể luôn mát mẻ tiết kiệm tối đa nguồn nước quý giá; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L323</summary>

```text
HÌNH L323 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cộng thêm chiếc mũi xoắn ốc khổng lồ tái hấp thu tới 60% hơi ẩm từ hơi thở ra, Lạc Đà có thể đi bộ xuyên qua chảo lửa sa mạc mà chẳng tốn lấy một giọt mồ hôi!". Bố cục: Cắt lớp khoang mũi xoắn ốc của lạc đà: các luồng hơi nước thở ra bị giữ lại bởi lớp màng nhầy và tái hấp thu ngược trở lại cơ thể; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L324</summary>

```text
HÌNH L324 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bướu mỡ trên lưng khi bị oxy hóa còn sản sinh ra hơn 100 gam nước chuyển hóa cho mỗi 100 gam chất béo bị tiêu hao!". Bố cục: Hình mô phỏng các phân tử mỡ trong bướu lạc đà chuyển hóa thành các giọt nước tinh khiết nuôi dưỡng cơ thể; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L325</summary>

```text
HÌNH L325 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lạc Đà sải những bước chân thần tốc, đưa Dê Núi tiếp cận sát chân ngọn tháp đá granite nguyên khối trong tiếng reo hò của phòng chỉ huy!". Bố cục: chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao dừng lại ngay sát chân tháp đá, quỳ hai chân trước xuống thật êm ái để Dê Núi bước xuống đất; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L326</summary>

```text
HÌNH L326 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trước mặt họ là bức tường thành dựng đứng 90° cao 30m! Bề mặt đá nhẵn thín như gương, không một kẽ nứt, không một mấu gờ nhô ra quá ba mi-li-mét!". Bố cục: Góc nhìn từ chân tháp nhìn thẳng lên đỉnh: vách đá granite dựng đứng chín mươi độ chót vót, nhẵn bóng không một bậc thang, đỉnh tháp là chiếc cầu treo đóng chặt; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L327</summary>

```text
HÌNH L327 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bất kỳ một vận động viên leo núi chuyên nghiệp nào nhìn vào vách đá này cũng phải lắc đầu bỏ cuộc. Nhưng đối với Dê Núi Bắc Mỹ, đây chỉ là một cầu thang quen thuộc hàng ngày!". Bố cục: chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt ngẩng cao đầu nhìn lên đỉnh tháp, ánh mắt tự tin của kẻ thống trị những đỉnh núi cheo leo nhất thế giới; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L328</summary>

```text
HÌNH L328 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vũ khí bí mật của Đặc vụ Dê Núi nằm ở bốn chiếc móng guốc thách thức mọi định luật vật lý!". Bố cục: Hình vẽ phóng to mặt dưới của chiếc móng guốc dê núi: viền ngoài là lớp sừng cứng như thép, bên trong là lớp đệm cao su mềm màu đen có khả năng đàn hồi và bám dính cực mạnh; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L329</summary>

```text
HÌNH L329 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Viền ngoài của móng là lớp sừng cứng sắc nhọn có thể găm chặt vào những vi gờ đá chỉ dày một mi-li-mét. Trong khi phần lòng móng là lớp đệm cao su dẻo ma sát cực cao, hoạt động như những chiếc giác hút chân không bám dính vào mặt đá!". Bố cục: Cận cảnh chiếc móng guốc bám chặt vào một gờ đá siêu nhỏ, lớp đệm cao su ép sát vào bề mặt đá tạo thành lực hút chân không giữ chặt bàn chân; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Biệt Đội Đặc Nhiệm Sinh Học chính thức xuất kích! Không một kẻ thù nào có thể cản bước mười quái kiệt của tự nhiên!". Bố cục: Hình ảnh bóng lưng mười đặc vụ lao ra khỏi căn cứ ngầm tiến về phía pháo đài sừng sững trong đêm bão tố.
```
</details>

<details><summary>L330</summary>

```text
HÌNH L330 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cộng thêm tầm nhìn bao quát 320° và cấu trúc khớp vai lực lưỡng, dê núi có thể kéo toàn bộ trọng lượng cơ thể lên chỉ bằng hai chiếc móng trước!". Bố cục: Sơ đồ cơ học khớp vai và cơ lưng của dê núi đang gồng lực kéo toàn thân vươn lên trên vách đá thẳng đứng; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L331</summary>

```text
HÌNH L331 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trọng tâm cơ thể đặt cực thấp cùng xương sườn hẹp giúp dê núi ép sát ngực vào vách đá, triệt tiêu hoàn toàn mô-men quay làm lật ngửa cơ thể!". Bố cục: Bản vẽ mô phỏng trọng tâm cơ thể dê núi nằm sát sạt mặt đá thẳng đứng; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L332</summary>

```text
HÌNH L332 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Xuất kích! Dê Núi Bắc Mỹ nhún mình bật nhảy một cú ngoạn mục lên vách đá dựng đứng 90°!". Bố cục: chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt phi thân lên không trung, hai móng trước găm chặt vào một gờ đá vô hình trên bề mặt vách đá nhẵn thín; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L333</summary>

```text
HÌNH L333 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một bước... hai bước... ba bước! Dê Núi leo ngược lên vách đá thẳng đứng với tốc độ thoăn thoắt như đang chạy trên mặt đất bằng phẳng!". Bố cục: chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt thoăn thoắt di chuyển lên cao trên vách đá dựng đứng chín mươi độ, các chân chuyển động nhịp nhàng chuẩn xác đến từng milimet; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L334</summary>

```text
HÌNH L334 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gió lốc sa mạc thổi giật từng cơn dữ dội, nhưng bốn chiếc móng giác hút cao su của anh chàng vẫn bám dính chặt chẽ không hề lung lay dù chỉ một ly!". Bố cục: Cơn bão cát sa mạc quét qua vách đá, nhưng chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt vẫn dán chặt thân mình vào mặt đá, kiên định leo từng mét một; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L335</summary>

```text
HÌNH L335 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cách đỉnh tháp 5 mét! Mỏm đá cuối cùng bị gãy vụn dưới chân! Dê Núi treo lơ lửng trên không trung chỉ bằng hai chiếc móng trước! Cả phòng chỉ huy nín thở!". Bố cục: Hai móng trước của chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt bám vào mép đá cuối cùng, thân mình đung đưa giữa không trung trên vực sâu hun hút; anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm siết chặt nắm tay!
```
</details>

<details><summary>L336</summary>

```text
HÌNH L336 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gồng cơ vai! Dê Núi vung một chân sau lên mỏm đá, tung cú bật nhảy tối thượng cuối cùng phi thẳng lên sàn đỉnh tháp!". Bố cục: chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt bật người một cú ngoạn mục vượt qua mép lan can đá, tiếp đất an toàn trên đỉnh tháp trong tiếng reo hò vang dội của toàn đội; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L337</summary>

```text
HÌNH L337 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đến lượt hạ cầu! Dê Núi đạp mạnh vào chiếc cần gạt tời cáp khổng lồ đặt trên đỉnh tháp!". Bố cục: Cặp sừng đen của chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt húc mạnh vào chiếc cần gạt cáp tời, hệ thống bánh răng rên rỉ quay vòng nhả xích; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L338</summary>

```text
HÌNH L338 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Rầm! Chiếc cầu treo rút khổng lồ bắc ngang qua thung lũng sa mạc hạ xuống, nối liền lối vào thẳng vào cổng chính của Phòng Châu Báu Trung Tâm!". Bố cục: Cầu treo bằng thép dày hạ xuống bắc qua miệng vực sa mạc, tạo nên một con đường đại lộ thênh thang cho toàn bộ biệt đội tiến bước; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L339</summary>

```text
HÌNH L339 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Toàn bộ bảy biểu tượng cửa ải trên {BOARD} đồng loạt chuyển sang màu xanh ngọc bích rực rỡ! 100 phần trăm hệ thống an ninh của Pháo Đài Tự Nhiên đã bị vô hiệu hóa hoàn toàn!". Bố cục: bản đồ hologram 3D của Pháo Đài Tự Nhiên nổi lơ lửng trong không khí, hiển thị 7 cửa ải an ninh phát sáng đỏ và thanh tiến độ phá khóa màu xanh ngọc (không có chữ, không có số) sáng rực rỡ với đủ bảy biểu tượng màu xanh ngọc bích, tiếng chuông báo hiệu thành công vang lên giòn giã khắp phòng chỉ huy; anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm mỉm cười giơ ngón tay cái tán thưởng.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mục tiêu là chiếc chìa khóa tối thượng. Thời gian đang đếm ngược từng giây một!". Bố cục: bản đồ hologram 3D của Pháo Đài Tự Nhiên nổi lơ lửng trong không khí, hiển thị 7 cửa ải an ninh phát sáng đỏ và thanh tiến độ phá khóa màu xanh ngọc (không có chữ, không có số) chớp sáng con số đếm ngược màu xanh lục, toàn bộ hệ thống máy móc ngầm bắt đầu khởi động rền vang.
```
</details>

<details><summary>L340</summary>

```text
HÌNH L340 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cả 10 đặc vụ tập hợp trước cánh cổng sắt mạ vàng của Phòng Châu Báu. Nhưng đúng lúc này, từ trong bóng tối của hành lang ngoại vi, một đội tuần tra người máy tự động bất ngờ xuất hiện bao vây lối thoát!". Bố cục: Đội lính tuần tra người máy mang súng điện tử và đèn pin pha cực sáng xuất hiện từ các góc hành lang tối, bắt đầu khép chặt vòng vây quanh cổng kho báu; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L341</summary>

```text
HÌNH L341 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chỉ Huy Mật Vụ khẽ nhếch mép: "Đừng lo. Chúng ta vẫn còn một tay súng phun tia nước tầm xa đang ẩn nấp trên cao chưa từng lộ diện!"". Bố cục: anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm nhìn lên màn hình phụ góc trên: chú Chim Bách Thanh hoạt hình lông xám trắng có dải lông đen vắt ngang mắt như dải băng cướp biển, mỏ có móc câu sắc nhọn, chân cầm một nhánh gai nhọn công nghệ đang ẩn mình trong bóng tối của cành cây bồ kết, ánh mắt sắc như dao găm đã khóa chặt toàn bộ mục tiêu lính gác.
```
</details>

<details><summary>L342</summary>

```text
HÌNH L342 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tay súng phun tia nước tầm xa bí mật chuẩn bị khai hỏa dọn sạch hậu phương trong chớp mắt!". Bố cục: Cận cảnh chiếc mỏ khoằm sắc như lưỡi liềm của chim bách thanh sáng loáng dưới ánh trăng rằm.
```
</details>

<details><summary>L343</summary>

```text
HÌNH L343 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lạc Đà Sa Mạc có thể mất tới 30 phần trăm trọng lượng cơ thể do mất nước mà vẫn đi bộ bình thường, trong khi các loài thú khác sẽ chết vì trụy tim nếu mất 15 phần trăm nước!". Bố cục: Biểu đồ so sánh khả năng chịu mất nước phi thường của lạc đà so với các loài động vật khác; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L344</summary>

```text
HÌNH L344 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Dê Núi Bắc Mỹ thì sở hữu cặp sừng đen rỗng bên trong giúp phân tán nhiệt lượng cơ thể khi vận động mạnh trên vách đá cheo leo!". Bố cục: Cận cảnh cặp sừng đen nhọn hoắt của chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt với các rãnh tản nhiệt tự nhiên lấp lánh dưới nắng; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L345</summary>

```text
HÌNH L345 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bộ đôi sa mạc và vách đá đã chứng minh rằng không có địa hình nào trên Trái Đất có thể ngăn cản bước chân của những kẻ nắm vững nghệ thuật thích nghi!". Bố cục: chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao và chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt cùng nhìn lên đỉnh tháp cao chót vót với nụ cười chiến thắng.
```
</details>

<details><summary>L346</summary>

```text
HÌNH L346 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bức tường đá dựng đứng 90° từng là nỗi khiếp sợ của muôn loài nay đã in dấu bốn móng guốc cao su kiêu hãnh của Dê Núi Bắc Mỹ!". Bố cục: Dấu móng guốc sắc nét in trên vách đá granite thẳng đứng như những chiếc huân chương danh dự của bậc thầy leo núi; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L347</summary>

```text
HÌNH L347 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lạc Đà Sa Mạc đứng dưới chân tháp ngước nhìn người đồng đội trên cao, cất tiếng kêu hò reo cổ vũ nồng nhiệt vang vọng khắp lòng chảo sa mạc!". Bố cục: chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao vẫy tai mừng rỡ, hai bướu mỡ rung rinh nhịp nhàng dưới ánh mặt trời rực rỡ; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L348</summary>

```text
HÌNH L348 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bên ngoài cổng Phòng Châu Báu, không khí căng thẳng đến nghẹt thở. Đội tuần tra an ninh tự động của Pháo Đài Tự Nhiên đã phát hiện ra các dấu vết xâm nhập bất thường!". Bố cục: Hành lang đá mờ ảo ánh đèn đỏ báo động, một tiểu đội năm người máy tuần tra mang súng điện tử và đèn rọi đang bước đều bước lùng sục khắp các ngóc ngách; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L349</summary>

```text
HÌNH L349 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Những chiếc loa phát thanh trên tường chuẩn bị phát tín hiệu báo động đỏ toàn căn cứ. Nếu tiếng còi báo động vang lên, toàn bộ các lối thoát hiểm sẽ bị đánh sập vĩnh viễn, chôn vùi cả biệt đội trong lòng đất!". Bố cục: Bàn tay kim loại của người máy chỉ huy chuẩn bị gạt chiếc cần báo động tổng lực màu đỏ gắn trên cột trụ hành lang; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Pháo Đài Tự Nhiên được xây dựng dựa trên những định luật khắc nghiệt nhất của hành tinh, nơi những kẻ yếu đuối sẽ bị đào thải không thương tiếc.". Bố cục: Mô hình hologram hiển thị các lớp đá sa thạch và granite cổ xưa bao bọc quanh pháo đài ngầm; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L350</summary>

```text
HÌNH L350 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Toàn bộ 10 đặc vụ bên dưới đều đang tập trung trước cánh cổng kho báu, không kịp quay lại ứng cứu. Khoảng cách giữa họ và đội tuần tra chỉ còn chưa đầy 30m!". Bố cục: Cận cảnh các đặc vụ quay lưng lại, chưa hay biết nguy hiểm đang cận kề phía sau lưng; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L351</summary>

```text
HÌNH L351 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các tia quét tầm nhiệt của đội tuần tra đang lia dần về phía bóng lưng của Chim Cắt và Quạ Đen, chỉ còn vài giây nữa là chuông báo động sẽ réo vang!". Bố cục: Những chấm đỏ la-de ngắm bắn dịch chuyển từng tấc một trên sàn đá hoa cương; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L352</summary>

```text
HÌNH L352 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng trên cành cao của cây bồ kết cổ thụ ngoài cửa sổ hành lang, một bóng đen nhỏ bé mang đôi cánh xám trắng đang lặng lẽ quan sát từng cử động của kẻ địch: Đặc vụ Chim Bách Thanh!". Bố cục: chú Chim Bách Thanh hoạt hình lông xám trắng có dải lông đen vắt ngang mắt như dải băng cướp biển, mỏ có móc câu sắc nhọn, chân cầm một nhánh gai nhọn công nghệ đậu ẩn mình sau tán lá rậm rạp, dải lông đen ngang mắt trông sắc lạnh như một tay súng phun tia nước tầm xa huyền thoại, mỏ ngậm một chùm gai nhọn thép công nghệ cao; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L353</summary>

```text
HÌNH L353 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đừng để vẻ bề ngoài nhỏ nhắn như một chú chim sẻ đánh lừa bạn! Trong giới điểu học, Chim Bách Thanh được mệnh danh là "Gã Đồ Tể Rừng Xanh", sát thủ sở hữu kỹ thuật phục kích tàn nhẫn và thông minh bậc nhất tự nhiên!". Bố cục: Tranh vẽ phong cách đồ họa Cold War: bóng đen của chim bách thanh in lên vách tường với chiếc mỏ khoằm có móc câu sắc nhọn đáng sợ như một chiếc lưỡi liềm nhỏ; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L354</summary>

```text
HÌNH L354 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bách Thanh là loài chim duy nhất không có móng vuốt đại bàng nhưng lại có thể săn bắt và hạ gục những con mồi to gấp đôi trọng lượng cơ thể mình!". Bố cục: Sơ đồ giải phẫu chiếc mỏ của bách thanh: trên mỏ trên có một chiếc mấu xương sắc nhọn gọi là răng giả tomium, hoạt động như một chiếc kìm bấm chuyên bẻ gãy đốt sống con mồi; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L355</summary>

```text
HÌNH L355 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cơ cổ cực khỏe cho phép chim bách thanh thực hiện cú giật xoắn cực mạnh làm trật khớp cổ con mồi chỉ trong 0,1 giây!". Bố cục: Hình mô phỏng hướng chuyển động xoắn vặn lực cơ học của đầu chim bách thanh khi tấn công mục tiêu; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L356</summary>

```text
HÌNH L356 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và vũ khí đáng sợ nhất của Bách Thanh chính là kỹ thuật cắm gai nhọn độc nhất vô nhị! Các nhà khoa học tại đại học Florida đã ghi nhận những phát hiện chấn động về tập tính này!". Bố cục: Tranh minh họa tư liệu nghiên cứu: một bụi gai sa mạc cắm đầy những con mồi được treo lơ lửng ngay ngắn như một kho hàng dự trữ; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L357</summary>

```text
HÌNH L357 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi bắt được những loài côn trùng có nọc độc chết người như cào cào Lubber khổng lồ, bách thanh không bao giờ ăn ngay. Anh chàng sẽ cắp con mồi đem cắm chặt lên một chiếc gai nhọn sắc bén!". Bố cục: Cận cảnh chú chim bách thanh dùng mỏ xiên chặt một con cào cào độc lên cành gai nhọn của bụi cây một cách điêu luyện; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L358</summary>

```text
HÌNH L358 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Con mồi được phơi trên gai suốt 3 ngày trời! Dưới ánh nắng và gió, toàn bộ chất độc tự nhiên trong cơ thể con mồi sẽ bị phân hủy hoàn toàn, biến một bữa ăn kịch độc thành món ăn thơm ngon bổ dưỡng an toàn tuyệt đối!". Bố cục: Sơ đồ phân hủy chất độc: các phân tử độc tố màu xanh lá cây bốc hơi dần theo thời gian ba ngày, để lại phần thịt an toàn cho chim; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L359</summary>

```text
HÌNH L359 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa hết, Bách Thanh sở hữu một bản đồ không gian thiên tài trong não bộ: anh chàng có thể ghi nhớ vị trí của hàng chục chốt gai nhọn khác nhau rải rác trong bán kính 500 mét mà không bao giờ nhầm lẫn!". Bố cục: Bản đồ vệ tinh hiển thị bán kính 500 mét quanh tổ chim, hàng chục chấm đỏ đánh dấu các kho gai nhọn sáng lên đồng loạt trong trí nhớ của chú chim; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi một cửa ải đại diện cho một thảm họa sinh học tự nhiên: từ áp suất chân không đến cực hạn giá rét, từ sa mạc lửa cháy đến hào nước áp lực cao.". Bố cục: Bảy biểu tượng cửa ải nhấp nháy phát sáng thành một vòng tròn bảo vệ xung quanh pháo đài; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L360</summary>

```text
HÌNH L360 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Anh chàng biết chính xác món mồi nào đã được cắm bao nhiêu ngày, món nào đã hết độc tố và sẵn sàng thưởng thức!". Bố cục: Đồ thị quản lý chuỗi cung ứng thực phẩm tự nhiên trong trí não chim bách thanh; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L361</summary>

```text
HÌNH L361 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tọa độ đã khóa! Mục tiêu là năm chiếc camera cảm biến và chiếc cần gạt báo động khẩn cấp!". Bố cục: Cận cảnh ánh mắt sắc lẹm của chú Chim Bách Thanh hoạt hình lông xám trắng có dải lông đen vắt ngang mắt như dải băng cướp biển, mỏ có móc câu sắc nhọn, chân cầm một nhánh gai nhọn công nghệ qua kính ngắm quang học, tâm ngắm khóa chặt chiếc công tắc báo động trên tường hành lang; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L362</summary>

```text
HÌNH L362 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bách Thanh tung cánh lao vút qua khung cửa sổ hành lang như một mũi tên xé gió, không phát ra một tiếng động nhỏ nào!". Bố cục: chú Chim Bách Thanh hoạt hình lông xám trắng có dải lông đen vắt ngang mắt như dải băng cướp biển, mỏ có móc câu sắc nhọn, chân cầm một nhánh gai nhọn công nghệ sà xuống cực nhanh theo đường bay sát mặt đất, thân hình lướt đi thoăn thoắt trong bóng tối mờ ảo; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L363</summary>

```text
HÌNH L363 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vút! Vút! Vút! Bách Thanh phóng ra những chiếc gai thép sắc nhọn găm thẳng vào năm ống kính camera cảm biến của đội tuần tra người máy!". Bố cục: Những chiếc gai thép nhọn hoắt cắm chuẩn xác vào tâm điểm thấu kính của các camera giám sát, tia lửa điện chập mạch nổ tanh tách làm tối đen hệ thống quan sát; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L364</summary>

```text
HÌNH L364 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đội tuần tra bị mù hoàn toàn! Người máy chỉ huy hoảng hốt vung tay định kéo cần gạt còi báo động khẩn cấp!". Bố cục: Người máy chỉ huy đưa bàn tay kim loại ra sát chiếc cần gạt màu đỏ chỉ còn cách đúng năm xăng-ti-mét; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L365</summary>

```text
HÌNH L365 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không kịp nữa rồi! Bách Thanh bay vọt lên, chiếc mỏ sắc bén có mấu răng giả tomium bổ thẳng một cú mổ thần tốc vào khớp ngón tay kim loại của người máy!". Bố cục: Cú mổ chuẩn xác của chú Chim Bách Thanh hoạt hình lông xám trắng có dải lông đen vắt ngang mắt như dải băng cướp biển, mỏ có móc câu sắc nhọn, chân cầm một nhánh gai nhọn công nghệ đánh gãy khớp nối ngón tay robot, chiếc then cài rơi rụng lanh canh xuống sàn đá; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L366</summary>

```text
HÌNH L366 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Anh chàng nhanh như chớp dùng mỏ quặp lấy một chiếc cọc gai thép dài 20cm, đóng chặt xuyên qua chiếc cần gạt báo động, ghim cứng nó vào tường đá không thể nhúc nhích!". Bố cục: Chiếc cọc gai thép găm chặt chiếc cần gạt báo động vào sâu trong vách đá, khóa chết công tắc còi hú ở vị trí tắt vĩnh viễn; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L367</summary>

```text
HÌNH L367 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đội tuần tra người máy mất phương hướng, quay mòng mòng va đập vào nhau rồi đổ rạp xuống sàn hành lang như những quân cờ domino đổ sập!". Bố cục: Năm người máy tuần tra va vào nhau kêu loảng xoảng, chập mạch điện tóe lửa nằm bất động trên sàn đá; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L368</summary>

```text
HÌNH L368 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bách Thanh đậu nhẹ nhàng trên đỉnh chiếc mũ sắt của người máy chỉ huy, nghiêng đầu chỉnh lại dải lông đen ngang mắt, phát ra một tiếng kêu lách cách báo cáo Chỉ Huy Mật Vụ.". Bố cục: chú Chim Bách Thanh hoạt hình lông xám trắng có dải lông đen vắt ngang mắt như dải băng cướp biển, mỏ có móc câu sắc nhọn, chân cầm một nhánh gai nhọn công nghệ đứng hiên ngang trên đống tàn tích của đội tuần tra, mỏ ngậm một chiếc cúc áo kim loại chiến lợi phẩm, giơ một ngón cánh chào báo cáo chiến công hiển hách.
```
</details>

<details><summary>L369</summary>

```text
HÌNH L369 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: ""Ngoại vi đã dọn sạch! Toàn bộ hệ thống còi báo động đã bị khóa cứng bằng gai thép!" Giọng Bách Thanh đanh gọn truyền qua mic.". Bố cục: anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm trong phòng điều khiển thở phào nhẹ nhõm, mỉm cười gật đầu: "Làm tốt lắm Đặc vụ Bách Thanh. Đường lui đã hoàn toàn an toàn!"
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chỉ có sức mạnh thích nghi tối thượng của muôn loài mới có thể tìm ra kẽ hở giữa những công sự kiên cố này!". Bố cục: anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm chỉ ngón tay vào tâm điểm bản đồ, ánh mắt kiên định thúc giục mười đặc vụ chuẩn bị sẵn sàng.
```
</details>

<details><summary>L370</summary>

```text
HÌNH L370 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mối đe dọa từ phía sau đã được hóa giải hoàn toàn. Giờ đây, chỉ còn lại cánh cổng sắt mạ vàng của Phòng Châu Báu Trung Tâm sừng sững trước mặt 10 đặc vụ.". Bố cục: Khung cảnh cánh cổng vòm khổng lồ bằng vàng ròng và đá quý của Phòng Châu Báu phát sáng lung linh huyền ảo giữa lòng pháo đài u tối; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L371</summary>

```text
HÌNH L371 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tất cả các ổ khóa đã mở. Toàn bộ 7 cửa ải đã bị xuyên thủng. Chiếc két sắt chứa Bản Thiết Kế Tiến Hóa Tối Thượng chỉ còn cách họ đúng một bước chân.". Bố cục: Cả mười đặc vụ đứng xếp hàng ngay ngắn trước cánh cổng vàng, ánh mắt hồi hộp và tò mò nhìn vào khe cửa đang từ từ hé mở... KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L372</summary>

```text
HÌNH L372 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giờ phút lịch sử đã điểm! Chiếc két sắt tối thượng của tạo hóa chuẩn bị hé lộ bí mật lớn nhất hành tinh!". Bố cục: Ánh sáng vàng kim từ khe cửa chiếu rọi lên khuôn mặt đầy háo hức của mười chiến binh dũng cảm.
```
</details>

<details><summary>L373</summary>

```text
HÌNH L373 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kỹ thuật săn mồi và quản lý kho dự trữ của Chim Bách Thanh là minh chứng rõ nét nhất cho trí thông minh sinh thái học của loài chim ăn thịt nhỏ bé này!". Bố cục: Bản đồ sinh thái mô phỏng các chốt gai dự trữ thức ăn của chim bách thanh trải dài khắp lãnh thổ săn mồi; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L374</summary>

```text
HÌNH L374 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhờ chiếc mỏ có mấu răng giả tomium, bách thanh có thể truyền toàn bộ lực cắn vào một điểm duy nhất trên đốt sống cổ của mục tiêu, tạo nên một lực phá hủy tập trung cực kỳ chết chóc!". Bố cục: Mô hình cơ học lực cắn tập trung tại đỉnh mấu răng tomium của chim bách thanh; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L375</summary>

```text
HÌNH L375 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sau khi vô hiệu hóa hoàn toàn đội tuần tra, anh chàng khẽ lau mỏ vào cành cây, tiếp tục giữ vai trò sát thủ thầm lặng bảo vệ toàn bộ đội hình rút lui an toàn!". Bố cục: chú Chim Bách Thanh hoạt hình lông xám trắng có dải lông đen vắt ngang mắt như dải băng cướp biển, mỏ có móc câu sắc nhọn, chân cầm một nhánh gai nhọn công nghệ đứng bất động trên cành cao, đôi mắt sắc lẹm canh chừng mọi biến động từ xa.
```
</details>

<details><summary>L376</summary>

```text
HÌNH L376 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khả năng ẩn nấp ngụy trang tài tình giúp Chim Bách Thanh hoàn toàn hòa mình vào màu vỏ cây bồ kết xám xịt, biến mất khỏi tầm mắt kẻ thù!". Bố cục: Bộ lông xám trắng của chú Chim Bách Thanh hoạt hình lông xám trắng có dải lông đen vắt ngang mắt như dải băng cướp biển, mỏ có móc câu sắc nhọn, chân cầm một nhánh gai nhọn công nghệ tiệp màu hoàn hảo với thân cây cổ thụ, chỉ có đôi mắt sáng quắc là chuyển động; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L377</summary>

```text
HÌNH L377 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Toàn bộ hành lang ngoại vi đã rơi vào im lặng tuyệt đối, mở đường cho giờ phút khai mở kho báu lịch sử của muôn loài!". Bố cục: Hành lang đá thông thoáng không còn bóng dáng một người máy tuần tra nào, ánh đèn êm dịu dẫn đường vào phòng trung tâm; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L378</summary>

```text
HÌNH L378 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cánh cổng vàng ròng nặng 10 tấn của Phòng Châu Báu Trung Tâm từ từ mở ra, kèm theo một tiếng rít trầm đục vang vọng khắp các vách đá.". Bố cục: Cánh cổng vòm mạ vàng khổng lồ mở toang ra một căn phòng mái vòm tráng lệ, ánh sáng vàng kim và hào quang tím huyền bí tỏa ra từ trung tâm căn phòng; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L379</summary>

```text
HÌNH L379 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mười đặc vụ cùng bước vào trong sự ngỡ ngàng tột độ. Không khí bên trong căn phòng thơm ngát mùi thảo mộc cổ xưa, hoàn toàn đối lập với mùi khói súng và sắt thép lạnh lẽo bên ngoài.". Bố cục: Toàn bộ mười đặc vụ bước vào căn phòng, ánh mắt sáng rực đầy tò mò và thán phục nhìn quanh những bức tường cẩm thạch khắc hoa văn cổ đại; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các kỹ sư của Tổng Cục đã phân tích dữ liệu địa tầng suốt 3 năm ròng để vẽ nên sơ đồ tiến công chuẩn xác nhất cho biệt đội!". Bố cục: Bản thiết kế địa chất cổ đại với các tầng địa chất phát sáng nhiều màu sắc khác nhau; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L380</summary>

```text
HÌNH L380 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chính giữa căn phòng là một chiếc bệ đá hoa cương đen tuyền, trên đó đặt chiếc két sắt tối thượng được rèn bằng hợp kim siêu bền bất khả xâm phạm.". Bố cục: Một chiếc bệ đá đen bóng bẩy đặt chiếc két sắt hình lập phương cổ kính, bốn góc két sắt có chạm khắc biểu tượng của bốn nguyên tố: gió, nước, đất và lửa; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L381</summary>

```text
HÌNH L381 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bốn bức bích họa khổng lồ trên tường tái hiện lại lịch sử tiến hóa 500 triệu năm của Trái Đất, từ những sinh vật phù du cổ đại cho đến những loài động vật kỳ diệu ngày nay!". Bố cục: Tranh tường mosaic phát sáng tái hiện cây phả hệ tiến hóa sinh học rực rỡ với hàng ngàn nhánh sinh vật; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L382</summary>

```text
HÌNH L382 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các đặc vụ bắt đầu xì xào bàn tán về món kho báu đang nằm bên trong. Mỗi người đều có một giấc mơ riêng sau khi hoàn thành phi vụ thế kỷ!". Bố cục: Cả đội quây quanh chiếc bệ đá, ánh mắt lấp lánh sự phấn khích của những người sắp được nhận phần thưởng xứng đáng; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L383</summary>

```text
HÌNH L383 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chuột Chũi Trũi chảy nước miếng mơ về một kho chứa 1 triệu tấn khoai tây mật ngọt lịm ăn không bao giờ hết!". Bố cục: chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên chảy nước miếng mơ màng ôm hai tay trước ngực; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L384</summary>

```text
HÌNH L384 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Quạ Đen thì xoa xoa hai cánh mắt sáng như sao, đòi một núi thìa bạc nạm kim cương để xây cái tổ đắt giá nhất hành tinh!". Bố cục: chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép đứng xoa xoa hai cánh mắt sáng lấp lánh tưởng tượng chiếc tổ bằng vàng bạc; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L385</summary>

```text
HÌNH L385 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cá Voi Sát Thủ nhô đầu lên cười khùng khục đòi một biển đầy cá hồi béo ngậy và chiếc vương miện thống trị đại dương!". Bố cục: chú Cá Voi Sát Thủ hoạt hình thân đen bóng bụng trắng tinh, vây lưng cao vút cắm ăng-ten định vị sonar nhỏ xíu, miệng cười nhếch mép kiểu trùm mafia biển cả nhô đầu lên ngoác miệng cười để lộ hàm răng trắng bóng; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L386</summary>

```text
HÌNH L386 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn Lạc Đà Sa Mạc chỉ khẽ chớp mắt mơ về một hồ nước ngọt mát lạnh quanh năm với những rặng xương rồng không bao giờ tàn!". Bố cục: chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao chớp chớp hàng mi cong vút mỉm cười hiền lành; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L387</summary>

```text
HÌNH L387 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Dê Núi mong ước có một ngọn núi tuyết riêng tư để tha hồ phi thân, trong khi đàn kiến cắt lá mơ về một cánh rừng lá phong non xanh mướt!". Bố cục: chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt và tiểu đội ba chú Kiến Cắt Lá hoạt hình màu nâu đỏ, đầu to mang hàm răng kim loại sáng loáng, đội mũ cối công binh màu xanh lá, đang vác những mảnh lá xanh như chiếc khiên chắn cùng hướng mắt về chiếc két sắt với nụ cười rạng rỡ; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L388</summary>

```text
HÌNH L388 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chỉ Huy Mật Vụ bước tới trước chiếc két sắt, nhẹ nhàng đặt chiếc máy tính bảng mật mã vào ổ nhận dạng trung tâm. Tách! Tách! Tách! Chiếc két sắt từ từ bật nắp!". Bố cục: anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm bấm nút xác nhận cuối cùng, các chốt khóa nặng nề kêu lách cách trượt mở, nắp chiếc két sắt từ từ mở bung ra với một làn khói trắng mờ ảo; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L389</summary>

```text
HÌNH L389 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một luồng ánh sáng chói lòa bừng lên, khiến tất cả phải đưa tay lên che mắt. Nhưng khi làn khói tan dần... cả 10 đặc vụ đều sững sờ chết lặng!". Bố cục: Mười đặc vụ cùng trố mắt nhìn vào bên trong lòng chiếc két sắt, miệng há hốc không thốt nên lời; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mọi thiết bị hỗ trợ và vũ khí ngụy trang đều đã được kiểm tra nghiêm ngặt, sẵn sàng cho giờ xuất kích!". Bố cục: Các vali dụng cụ điệp viên màu đen mở nắp, bên trong xếp ngay ngắn những chiếc kính nhìn đêm và móc câu chuyên dụng; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L390</summary>

```text
HÌNH L390 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bên trong chiếc két sắt tối thượng... không hề có một thỏi vàng nào! Không có kim cương, không có súng laser tối tân, cũng chẳng có lấy một cọng khoai tây nào cả!". Bố cục: Lòng chiếc két sắt chỉ có một chiếc bệ nhung đỏ đơn sơ, trên đó đặt một chiếc gương tròn cổ kính bằng đồng và một cuộn da cừu cũ kỹ ngả vàng; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L391</summary>

```text
HÌNH L391 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ủa... kho báu của chúng ta đâu rồi sếp ơi? Bị ai nẫng tay trên trước rồi hả sếp? Hay là chúng ta đột nhập nhầm pháo đài rồi?". Bố cục: chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên ngơ ngác thò đầu vào trong lòng két sắt ngó nghiêng, hai chân trước cào cào lớp vải nhung trống không; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L392</summary>

```text
HÌNH L392 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chỉ Huy Mật Vụ không hề ngạc nhiên. Anh chàng cú mèo nhẹ nhàng cầm chiếc gương tròn lên, xoay mặt gương hướng về phía toàn thể 10 đặc vụ.". Bố cục: anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm nâng chiếc gương đồng sáng bóng lên cao, mặt gương phản chiếu rõ mồn một khuôn mặt của mười loài động vật đang đứng quây quần xung quanh; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L393</summary>

```text
HÌNH L393 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: ""Các bạn hãy nhìn kỹ vào trong gương đi. Kho báu thật sự của Pháo Đài Tự Nhiên... đang đứng ngay trước mặt các bạn đấy." Giọng Chỉ Huy trầm ấm và trang nghiêm vang lên.". Bố cục: Cận cảnh mặt gương phản chiếu đôi mắt rực lửa của chim cắt, hàm răng của chuột chũi, khăn len của ếch gỗ, mỏ quạ đen, vây cá voi, mỏ chim gõ kiến, bướu lạc đà, sừng dê núi, móc gai bách thanh và hàm răng thép của kiến; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L394</summary>

```text
HÌNH L394 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chỉ Huy từ từ mở cuộn da cừu cổ xưa ra, đọc to những dòng chữ được khắc ghi từ hàng trăm triệu năm trước:". Bố cục: anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm giở cuộn da cừu phát sáng những dòng chữ cổ màu vàng kim rực rỡ, ánh sáng ấm áp lan tỏa khắp gian phòng; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L395</summary>

```text
HÌNH L395 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: ""Vàng bạc rồi cũng sẽ bị chôn vùi dưới cát bụi. Súng đạn rồi cũng sẽ bị rỉ sét mục nát theo thời gian. Nhưng khả năng thích nghi và vươn lên của sự sống thì bất tử."". Bố cục: Tranh minh họa lịch sử tiến hóa của Trái Đất: từ những sinh vật đơn bào cổ đại vượt qua kỷ băng hà, núi lửa phun trào để tiến hóa thành muôn loài kỳ diệu ngày nay; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L396</summary>

```text
HÌNH L396 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kho báu vĩ đại nhất của tự nhiên không phải là những thứ vật chất vô tri, mà chính là Bản Thiết Kế Tiến Hóa nằm ngay trong cơ thể của mỗi loài sinh vật!". Bố cục: Hình ảnh đồ họa hào quang bao quanh từng đặc vụ: mỗi loài vật tỏa sáng một vầng hào quang rực rỡ tượng trưng cho sức mạnh tiến hóa của mình; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L397</summary>

```text
HÌNH L397 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chiếc mũi nén khí siêu thanh 389 km/h của Chim Cắt. Khả năng thở bằng đường hoa quả sống sót 18 phút không oxy của Chuột Chũi. Thuật đóng băng 65% cơ thể hồi sinh sau 7 tháng của Ếch Gỗ.". Bố cục: Ba biểu tượng sinh học tuyệt mỹ xuất hiện lơ lửng trên không trung: luồng khí nén chim cắt, phân tử đường fructose của chuột chũi và tinh thể băng ngọc bích của ếch gỗ; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L398</summary>

```text
HÌNH L398 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trí tuệ chế tạo công cụ giải câu đố 8 bước của Quạ Đen. Sóng âm sonar 225 dB quất sóng thần của Cá Voi Sát Thủ. Hộp sọ giảm chấn 1200G của Chim Gõ Kiến.". Bố cục: Ba kỳ quan kỹ thuật tiếp theo bay lượn trên không: chiếc móc câu của quạ, sóng âm thanh cá voi và chiếc đai an toàn sọ não của chim gõ kiến; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L399</summary>

```text
HÌNH L399 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tế bào nước màu hình oval giãn nở 240% của Lạc Đà Sa Mạc. Móng guốc giác hút cao su bám vách đá 90° của Dê Núi. Kỹ thuật cắm gai khử độc của Chim Bách Thanh. Và hàm răng tẩm kim loại nặng của Đại Đội Kiến Cắt Lá!". Bố cục: Bốn mảnh ghép cuối cùng hòa quyện vào nhau tạo thành một quả cầu ánh sáng sinh học khổng lồ rực rỡ giữa phòng châu báu; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bầu trời đêm phía trên Pháo Đài Tự Nhiên không hề yên bình như vẻ bề ngoài. Đây là vành đai phòng không khắc nghiệt nhất hành tinh.". Bố cục: Cảnh bầu trời đêm bão tố cuồn cuộn mây xám, những cột tia laser màu đỏ rực đan chéo nhau như một chiếc lồng ánh sáng khổng lồ bao trùm lấy đỉnh tháp pháo đài; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L400</summary>

```text
HÌNH L400 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi loài trong số mười quái kiệt này tự thân đã là một kiệt tác kỹ thuật đỉnh cao mà không một phòng thí nghiệm hay cỗ máy tối tân nào của con người có thể sao chép hoàn hảo được!". Bố cục: Toàn bộ mười đặc vụ nhìn nhau, ánh mắt từ thất vọng chuyển sang sự tự hào khôn xiết khi nhận ra giá trị vô giá của chính bản thân mình; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L401</summary>

```text
HÌNH L401 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và điều kỳ diệu nhất: không một cá nhân nào có thể một mình vượt qua cả 7 cửa ải của pháo đài. Chỉ khi mười loài vật cùng đoàn kết, bù đắp điểm yếu cho nhau, cánh cửa bất khả thi mới được mở toang!". Bố cục: Mười đặc vụ cùng khoác vai nhau, nắm lấy tay nhau tạo thành một vòng tròn gắn kết bền chặt quanh bệ đá cổ xưa; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L402</summary>

```text
HÌNH L402 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đó chính là thông điệp tối thượng của Bản Thiết Kế Tiến Hóa: Đa dạng sinh học chính là chiếc khiên hộ mệnh duy nhất bảo vệ sự sống trên hành tinh xanh này!". Bố cục: Quả cầu ánh sáng nở bung ra thành hình ảnh Trái Đất xanh ngắt bao la với muôn loài muôn thú cùng chung sống hòa bình dưới ánh mặt trời rực rỡ; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L403</summary>

```text
HÌNH L403 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Biệt Đội Đặc Nhiệm Sinh Học đã hoàn thành sứ mệnh lịch sử vĩ đại nhất của muôn loài!". Bố cục: anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm nâng ly chúc mừng mười người đồng đội anh hùng trong hào quang rực rỡ của căn phòng châu báu.
```
</details>

<details><summary>L404</summary>

```text
HÌNH L404 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng khoảnh khắc lắng đọng đầy ý nghĩa vừa kết thúc... thì một tiếng nổ chát chúa vang lên từ trần phòng châu báu!". Bố cục: Trần nhà rung chuyển dữ dội, bụi đá rơi lả tả xuống sàn, một chiếc đèn báo động màu tím than bắt đầu quay tít mù kèm theo tiếng còi hú đinh tai nhức óc! KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L405</summary>

```text
HÌNH L405 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chiếc bệ đá tự động tụt xuống lòng đất, kích hoạt hệ thống tự hủy cuối cùng của pháo đài: "Cảnh báo khẩn cấp! Bản Thiết Kế đã được mở khóa! Pháo đài sẽ tự hủy hoàn toàn sau đúng 3 phút nữa!"". Bố cục: Một chiếc đồng hồ đếm ngược kỹ thuật số khổng lồ màu đỏ rực xuất hiện trên vách tường đá, bắt đầu đếm lùi từng giây: 03:00... 02:59... 02:58! KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L406</summary>

```text
HÌNH L406 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cuộc đột nhập đã hoàn tất. Bây giờ là bài toán sinh tử cuối cùng: Chiến Dịch Tháo Chạy Nghẹt Thở để thoát khỏi đống đổ nát trước khi chiếc cổng thành đóng vĩnh viễn!". Bố cục: anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm hét lớn vào bộ đàm: "Toàn đội kích hoạt phương án thoát hiểm khẩn cấp! Chạy ngay!" Cả mười đặc vụ cùng quay đầu lao vút ra ngoài hành lang trong tiếng nổ rung chuyển đất trời!
```
</details>

<details><summary>L407</summary>

```text
HÌNH L407 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cả căn cứ đang sụp đổ sau lưng, thời gian chỉ còn tính bằng từng tích tắc ngắn ngủi!". Bố cục: Cảnh mười đặc vụ cùng phóng nhanh qua cánh cửa vòm khi các khối đá khổng lồ bắt đầu rơi rụng như mưa.
```
</details>

<details><summary>L408</summary>

```text
HÌNH L408 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hàng trăm triệu năm qua, Trái Đất đã trải qua biết bao kỷ băng hà buốt giá, bao đợt tuyệt chủng khắc nghiệt và núi lửa phun trào ngút trời.". Bố cục: Tranh minh họa Trái Đất qua các kỷ địa chất lịch sử: từ đại cổ sinh cho đến kỷ băng hà và sự trỗi dậy của các loài thú; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L409</summary>

```text
HÌNH L409 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng sự sống chưa bao giờ chịu khuất phục. Mỗi một loài sinh vật, từ chú kiến nhỏ bé dưới chân đến chú cá voi khổng lồ ngoài khơi xa, đều là một mảnh ghép không thể thiếu của bức tranh thiên nhiên hoàn mỹ!". Bố cục: Toàn bộ mười đặc vụ đứng quây quần bên nhau, ánh sáng từ cuộn Bản Thiết Kế Tiến Hóa soi rọi khuôn mặt đầy xúc động; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hàng ngàn cảm biến gió áp suất cao đang quét liên tục ở tầng đối lưu. Bất kỳ vật thể bay nào lao vào đây với tốc độ cao đều sẽ bị luồng khí nén cực mạnh xé nát phổi ngay lập tức.". Bố cục: Hình vẽ cắt lớp kỹ thuật của một hệ thống phòng không thế giới tự nhiên cổ điển, các luồng sóng xung kích không khí màu vàng cam xoáy tròn dữ dội quanh miệng phễu thu cảm biến; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L410</summary>

```text
HÌNH L410 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Biệt Đội Đặc Nhiệm Sinh Học đã chứng minh rằng khi chúng ta cùng thấu hiểu và tôn trọng những giá trị tiến hóa của tự nhiên, không có thử thách nào là không thể vượt qua!". Bố cục: Mười đặc vụ cùng đặt tay lên cuộn da cừu cổ xưa, tuyên thệ bảo vệ sự sống muôn loài trên hành tinh.
```
</details>

<details><summary>L411</summary>

```text
HÌNH L411 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khoảnh khắc chiếc gương đồng phản chiếu khuôn mặt của cả mười quái kiệt sẽ mãi mãi là bức tranh đẹp nhất trong lịch sử sinh tồn của Trái Đất!". Bố cục: Mười đặc vụ cùng soi bóng vào chiếc gương đồng cổ kính, nụ cười rạng rỡ của những người chiến thắng nở trên môi; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L412</summary>

```text
HÌNH L412 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bản Thiết Kế Tiến Hóa Tối Thượng đã tìm được những chủ nhân xứng đáng nhất, những đại sứ xuất sắc của thế giới tự nhiên kỳ diệu!". Bố cục: Ánh sáng vàng kim từ cuộn da cừu bao trùm lấy toàn bộ căn phòng, sưởi ấm tâm hồn của mỗi người chiến sĩ điệp viên; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L413</summary>

```text
HÌNH L413 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đồng hồ đếm ngược tự hủy đang nhấp nháy đỏ rực: 2 phút 50 giây! Toàn bộ Pháo Đài Tự Nhiên rung chuyển dữ dội như vừa trải qua một trận động đất mười độ Rích-te!". Bố cục: Trần hang đá nứt toác từng mảng lớn, những khối đá nặng hàng tấn rơi ầm ầm xuống sàn hành lang, khói bụi mịt mù che khuất toàn bộ tầm nhìn; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L414</summary>

```text
HÌNH L414 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các hệ thống phòng vệ tự động bị chập điện, phóng ra những tia lửa điện xanh lè đan chéo nhau như một lưới điện tử thần. Các cánh cửa sắt chống cháy bắt đầu sập xuống ầm ầm!". Bố cục: Những cánh cửa thép ngăn cháy dày cộp lần lượt rơi thẳng đứng từ trên trần xuống sàn đá kêu rầm rầm, từng lối đi dần dần bị bịt kín; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L415</summary>

```text
HÌNH L415 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: ""Không được bỏ lại bất kỳ ai! Toàn đội kích hoạt đội hình combo giải cứu khẩn cấp!" Tiếng quát vang rền của Chỉ Huy Mật Vụ truyền thẳng vào tai nghe của từng đặc vụ.". Bố cục: anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm vừa chạy vừa ôm chặt chiếc máy tính bảng và cuộn da cừu cổ, liên tục quan sát bản đồ thoát hiểm đang chớp đỏ liên hồi; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L416</summary>

```text
HÌNH L416 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cửa sập số một rơi xuống chặn đứng lối ra của hành lang chính! Kẹt cứng! Khe hở dưới đáy chỉ còn chưa đầy 0,5m và đang hạ xuống dần!". Bố cục: Cánh cửa thép nặng nề chỉ còn cách mặt đất đúng bốn mươi xăng-ti-mét, chuẩn bị khóa chết đường thoát của cả đội; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L417</summary>

```text
HÌNH L417 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đến lượt cặp bài trùng công binh ra tay! Chim Gõ Kiến lao vút tới, mỏ kẹp chiếc đục sắt gõ liên hoàn 20 lần/giây vào rãnh trượt của cánh cửa!". Bố cục: chú Chim Gõ Kiến hoạt hình mào lông đỏ rực dựng đứng, mỏ dài sắc nhọn như mũi khoan titan, đội mũ bảo hộ lao động màu vàng có gắn đèn pin thợ mỏ bổ mỏ thần tốc vào khe trượt bản lề, các tia lửa nổ tung tóe chêm cứng một góc cửa làm cánh cửa khựng lại trong tích tắc; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L418</summary>

```text
HÌNH L418 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ngay lập tức, Đại Đội Kiến Cắt Lá dùng hàm răng tẩm kẽm và mangan ngoạm chặt lấy dây cáp tời phụ, kéo căng hết cỡ để giữ cánh cửa không bị rơi sập thêm!". Bố cục: Hàng ngàn chú kiến cắt lá cùng gồng mình kéo căng sợi dây thép chịu lực, tạo ra một khoảng trống vừa đủ cho đồng đội chui qua; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L419</summary>

```text
HÌNH L419 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Dê Núi Bắc Mỹ cúi rạp người xuống: "Chuột Chũi, Ếch Gỗ, nhảy lên lưng tôi mau!"". Bố cục: chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt nhanh nhẹn quỳ chân xuống, chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên và chú Ếch Gỗ Bắc Cực hoạt hình da nâu vàng có vệt đen qua mắt như mặt nạ Zorro, đeo khăn quàng cổ đỏ thắm chống rét, người phủ lớp sương tuyết lấp lánh thoăn thoắt nhảy tót lên lưng chú dê núi bám chặt vào bờm lông dày; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đặc vụ Chim Cắt Lớn đang lượn vòng ở độ cao hơn 3.000m. Gió rít gào bên tai, nhưng nhịp tim của anh chàng vẫn ổn định như một cỗ máy đếm giờ.". Bố cục: chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng bay lơ lửng giữa tầng mây mỏng ngược sáng dưới ánh trăng lưỡi liềm, kính phi công hạ xuống che mắt, đôi cánh khép hờ định hình tư thế tác chiến; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L420</summary>

```text
HÌNH L420 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Dê Núi co bốn chân, tung một cú phi thân trượt bụng điệu nghệ qua khe hở chỉ vài xăng-ti-mét trước khi cánh cửa sập hẳn xuống mặt sàn đá!". Bố cục: chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt trượt qua khe cửa hẹp ngoạn mục như một vận động viên trượt băng, cánh cửa sắt đóng sầm sau lưng kêu rầm một tiếng đinh tai! KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L421</summary>

```text
HÌNH L421 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thời gian còn lại: một phút 40 giây! Hành lang phía trước bốc cháy dữ dội do ống dẫn khí gas của lò nhiệt sa mạc bị vỡ toang!". Bố cục: Một bức tường lửa đỏ rực bốc cao ba mét chắn ngang lối đi duy nhất, hơi nóng bốc lên ngùn ngụt sẵn sàng thiêu rụi bất kỳ ai bước tới gần; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L422</summary>

```text
HÌNH L422 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: ""Dạt ra hai bên hết cho đại ca làm việc!" Tiếng gầm của Cá Voi Sát Thủ vang lên qua hệ thống cống thoát nước ngầm bên dưới sàn đá!". Bố cục: Một nắp cống kim loại bật tung lên trời, chú Cá Voi Sát Thủ hoạt hình thân đen bóng bụng trắng tinh, vây lưng cao vút cắm ăng-ten định vị sonar nhỏ xíu, miệng cười nhếch mép kiểu trùm mafia biển cả nhô đầu lên từ kênh nước áp lực cao chạy dọc hành lang; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L423</summary>

```text
HÌNH L423 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cá Voi Sát Thủ hít một hơi thật sâu làn nước lạnh, phóng ra một cột nước áp lực cao khổng lồ qua lỗ thở như một chiếc vòi rồng cứu hỏa tối tân!". Bố cục: Cột nước trắng xóa bắn vút ra từ lưng chú Cá Voi Sát Thủ hoạt hình thân đen bóng bụng trắng tinh, vây lưng cao vút cắm ăng-ten định vị sonar nhỏ xíu, miệng cười nhếch mép kiểu trùm mafia biển cả dập thẳng vào tâm điểm đám cháy, hơi nước bốc lên xèo xèo làm tắt ngấm ngọn lửa trong vòng ba giây! KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L424</summary>

```text
HÌNH L424 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lạc Đà Sa Mạc lập tức sải những bước chân dài vượt lên dẫn đầu, xòe hai bên hông che chắn cho các đồng đội nhỏ bé tránh khỏi những tảng đá nhọn đang rơi rụng từ trần hang!". Bố cục: chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao chạy chắn ngang phía trên, lớp lông dày và bướu mỡ kiên cố như một tấm khiên chống đạn bảo vệ toàn bộ đội hình; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L425</summary>

```text
HÌNH L425 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các tảng đá rơi trúng lưng lạc đà bị dội ngược ra ngoài nhờ lớp mỡ đàn hồi dày cộp, không gây tổn thương dù chỉ một vết xước!". Bố cục: Đá dăm nảy tưng tưng trên lưng lạc đà rơi xuống sàn mà chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao vẫn thản nhiên phi nước kiệu; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L426</summary>

```text
HÌNH L426 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thời gian còn lại: 50 giây! Toàn bộ căn cứ chìm trong khói đen đặc quánh! Hệ thống định vị vệ tinh mất tín hiệu hoàn toàn! Lối ra ở hướng nào?". Bố cục: Màn hình radar quét lối thoát bị nhiễu loạn hoàn toàn thành một màu xám xịt, không ai nhìn thấy đường đi trong làn khói đen mù mịt; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L427</summary>

```text
HÌNH L427 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Quạ Đen bay vút lên cao sát trần hang, dùng đôi mắt tinh tường quan sát hướng di chuyển của những luồng gió tươi mát luồn qua các khe nứt!". Bố cục: chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép bay lượn trên cao, phát hiện một luồng khí trong lành màu xanh lam đang hút về phía cuối hành lang bên phải; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L428</summary>

```text
HÌNH L428 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: ""Rẽ phải! Cổng vòm số ba! Chạy theo luồng gió tươi! Nhanh lên!" Quạ Đen vừa bay vừa kêu quạ quạ dẫn đường chuẩn xác cho cả đoàn quân!". Bố cục: chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép bay dẫn đầu như một ngọn hải đăng trong đêm, toàn bộ biệt đội nối đuôi nhau chạy thục mạng theo hướng chú quạ chỉ dẫn; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L429</summary>

```text
HÌNH L429 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thời gian còn lại: 20 giây! Cánh cửa sắt thoát hiểm cuối cùng của pháo đài đã hiện ra trước mắt! Nhưng bi kịch thay: cửa đã bị khóa chặt bằng ổ khóa điện tử khẩn cấp!". Bố cục: Cánh cửa thép thoát hiểm dẫn ra bầu trời đêm đang đóng kín mít, trên ổ khóa có một khe quẹt thẻ từ nhấp nháy đèn đỏ chờ mã kích hoạt; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đôi mắt của chim cắt sở hữu hai hố thị giác riêng biệt trên mỗi võng mạc, cho phép anh chàng vừa phóng to mục tiêu như kính viễn vọng vừa quan sát toàn cảnh 360°!". Bố cục: Sơ đồ giải phẫu mắt chim cắt với hai tiêu cự fovea phát sáng hai chùm tia nhìn quét qua không gian ban đêm; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L430</summary>

```text
HÌNH L430 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: ""Chiếc thẻ từ dự phòng! Thẻ từ đang ở đâu?" Chỉ Huy Mật Vụ lục lọi túi áo hoảng hốt kêu lên!". Bố cục: anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm sờ vào túi áo khoác trống rỗng, mặt biến sắc khi nhớ lại tai nạn cắm gai ở cây bồ kết ngoài sân! KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L431</summary>

```text
HÌNH L431 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cách đó 50 mét ngoài cửa sổ, chiếc thẻ từ màu đỏ vẫn đang bị cắm chặt trên cành gai cao chót vót của Chim Bách Thanh!". Bố cục: Cận cảnh chiếc thẻ từ đung đưa trên cành gai sắc nhọn ngoài sân, cách quá xa tầm tay của bất kỳ ai dưới mặt đất; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L432</summary>

```text
HÌNH L432 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thời gian còn lại: mười giây! Chín... tám... bảy! Tiếng còi tự hủy bắt đầu rít lên từng hồi liên tục báo hiệu đợt phát nổ cuối cùng!". Bố cục: Đồng hồ đếm ngược nhấp nháy đỏ rực: 00:07... 00:06... 00:05! KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L433</summary>

```text
HÌNH L433 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: ""Để đó cho tôi!" Một tia chớp xám đen xé toạc màn đêm lao vút qua khung cửa sổ với vận tốc 389 km/h: Chim Cắt Lớn!". Bố cục: chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng kích hoạt toàn bộ sức mạnh động cơ cánh, bổ nhào một đường cong hoàn hảo qua ngọn cây bồ kết; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L434</summary>

```text
HÌNH L434 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Móng vuốt vàng sắc lẹm của Chim Cắt quặp chuẩn xác vào mép chiếc thẻ từ, bẻ gãy cành gai nhọn trong chớp mắt, rồi lượn một vòng tròn ngoạn mục ném thẳng chiếc thẻ vào tay Chỉ Huy!". Bố cục: Chiếc thẻ từ màu đỏ bay vút trong không trung, rơi trúng vào lòng bàn tay của anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm một cách hoàn hảo đến từng mi-li-mét; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L435</summary>

```text
HÌNH L435 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Xoẹt! Chỉ Huy Mật Vụ quẹt mạnh chiếc thẻ qua khe nhận dạng! Tách! Cánh cửa sắt thoát hiểm bật mở toang ra bầu trời đêm bao la!". Bố cục: Cánh cửa bật mở, luồng gió đêm mát rượi ùa vào, phía dưới là con dốc thoải dẫn ra thung lũng an toàn; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L436</summary>

```text
HÌNH L436 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thời gian còn lại: 2 giây! Một giây! Toàn bộ 10 đặc vụ cùng Chỉ Huy cùng lúc tung mình nhảy bổ ra khỏi cửa hang!". Bố cục: Mười đặc vụ và Chỉ Huy cùng phi thân ra ngoài không trung trong một cú nhảy điện ảnh ngoạn mục, dưới ánh trăng vằng vặc; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L437</summary>

```text
HÌNH L437 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "ẦM! ĐOÀNG! Pháo Đài Tự Nhiên phát nổ sau lưng thành một quả cầu lửa khổng lồ rực sáng cả một góc trời, toàn bộ công sự bằng đá granite sụp đổ chôn vùi vĩnh viễn trong lòng đất!". Bố cục: Quả cầu lửa nổ tung rực rỡ phía sau lưng, khói bụi bốc cao ngùn ngụt soi sáng hình bóng mười đặc vụ đang lăn tròn tiếp đất an toàn trên sườn cỏ xanh mướt; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L438</summary>

```text
HÌNH L438 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Toàn đội lấm lem bùn đất, nhưng không một ai bị thương nặng! Chiếc máy tính bảng của Chỉ Huy vang lên một tiếng bíp êm ái: "Điệp vụ hoàn tất 100 phần trăm! Toàn đội an toàn!"". Bố cục: Mười đặc vụ nằm thở hổn hển trên thảm cỏ xanh, nhìn ngọn lửa phía xa rồi nhìn nhau, đồng loạt bật cười sảng khoái và đập tay ăn mừng chiến thắng ngoạn mục! KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L439</summary>

```text
HÌNH L439 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Biệt Đội Đặc Nhiệm Sinh Học đã sống sót qua phi vụ nghẹt thở nhất lịch sử!". Bố cục: Hình ảnh toàn đội đứng bên nhau ngắm ánh lửa xa xa, một cái kết mãn nhãn cho chiến dịch thế kỷ.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bộ đàm trung tâm rè lên giọng Chỉ Huy Mật Vụ: "Mật danh Tia Chớp, mục tiêu là chiếc rơ-le nguồn laser đặt ngay trên đỉnh vòm kính. Cậu chỉ có đúng một cơ hội duy nhất."". Bố cục: Cận cảnh anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm đứng trong phòng điều khiển, một tay giữ tai nghe bộ đàm, mắt nhìn vào màn hình hiển thị tọa độ điểm đỏ nhấp nháy trên đỉnh tháp; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L440</summary>

```text
HÌNH L440 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Từng giây phút trong cuộc tháo chạy nghẹt thở này là một bài học mẫu mực về tinh thần đoàn kết và sự phối hợp tác chiến đỉnh cao giữa các loài động vật!". Bố cục: Cảnh mười đặc vụ phối hợp nhịp nhàng vượt qua từng chướng ngại vật trong lòng pháo đài đang sụp lở; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L441</summary>

```text
HÌNH L441 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không có sự đố kỵ, không có sự phân biệt to nhỏ hay mạnh yếu, mỗi cá thể đều đem hết sở trường sinh học của mình ra để cứu lấy những người đồng đội!". Bố cục: Hình ảnh chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao chở các bạn nhỏ, chú Cá Voi Sát Thủ hoạt hình thân đen bóng bụng trắng tinh, vây lưng cao vút cắm ăng-ten định vị sonar nhỏ xíu, miệng cười nhếch mép kiểu trùm mafia biển cả dập lửa, chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép dẫn đường và chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng bay xé gió chộp thẻ từ; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L442</summary>

```text
HÌNH L442 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cú nhảy ngoạn mục ra ngoài miệng vực trong tiếng nổ rung trời lở đất sẽ mãi mãi đi vào huyền thoại của những phi vụ giải cứu vĩ đại nhất giới sinh vật học!". Bố cục: Mười bóng đen đặc vụ in trên nền quả cầu lửa nổ tung rực sáng cả bầu trời đêm.
```
</details>

<details><summary>L443</summary>

```text
HÌNH L443 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Những bước chân tháo chạy cuối cùng trên thảm cỏ xanh mướt là minh chứng cho sự kiên cường và lòng quả cảm phi thường của 10 đặc vụ sinh học!". Bố cục: Hình ảnh mười đặc vụ dìu nhau bước đi trên triền đồi hoa dại dưới ánh trăng thanh bình sau trận nổ kinh hoàng; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L444</summary>

```text
HÌNH L444 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Pháo Đài Tự Nhiên đã sụp đổ, nhưng tinh thần đồng đội và những kỳ quan tiến hóa của họ sẽ sống mãi với thời gian!". Bố cục: Bầu trời đêm lấp lánh ngàn vì sao sáng, soi rọi con đường trở về căn cứ bình yên của biệt đội anh hùng; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L445</summary>

```text
HÌNH L445 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ánh bình minh đầu tiên của buổi sớm mai bắt đầu ló rạng trên đường chân trời, dát một màu vàng mật ong ấm áp lên khắp thung lũng xanh mướt.". Bố cục: Cảnh bình minh rạng rỡ sau cơn bão lửa, ánh mặt trời vàng ấm áp chiếu rọi thung lũng hoa dại thanh bình, xa xa là làn khói mờ ảo của pháo đài đã sụp đổ; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L446</summary>

```text
HÌNH L446 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Căn phòng tác chiến ngầm dã chiến của Tổng Cục Mật Vụ lại rộn rã tiếng cười nói sau một đêm căng thẳng đến từng sợi tóc.". Bố cục: Căn phòng chỉ huy dã chiến bằng lều bạt thế giới tự nhiên ấm cúng, ánh đèn vàng ấm áp, bàn tác chiến đã được dọn sạch sẽ, bày biện các món ăn ngon; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L447</summary>

```text
HÌNH L447 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chỉ Huy Mật Vụ Cú Mèo cầm con dấu gỗ khắc nổi, nhúng vào khay mực đỏ tươi, đóng một phát thật mạnh xuống trang bìa của tập hồ sơ: CỘC! Dấu mực đỏ hiện rõ dòng chữ: HOÀN TẤT XUẤT SẮC — LƯU TRỮ TUYỆT MẬT!". Bố cục: Cận cảnh con dấu mực đỏ hình tròn "HOÀN TẤT XUẤT SẮC" in đậm nét trên bìa tập hồ sơ kraft vàng ngả bóng có ảnh chụp tập thể mười đặc vụ; anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm mỉm cười hài lòng.
```
</details>

<details><summary>L448</summary>

```text
HÌNH L448 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: ""Các đặc vụ của tôi! Đêm nay, các bạn không chỉ hoàn thành một phi vụ bất khả thi, mà còn chứng minh cho toàn thế giới thấy sức mạnh vô song của sự sống và tình đồng đội!"". Bố cục: anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm nâng ly nước quả lên cao chúc mừng, mười đặc vụ đứng quây quần xung quanh vỗ tay reo hò rộn rã; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L449</summary>

```text
HÌNH L449 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Biệt Đội Đặc Nhiệm Sinh Học đã hoàn thành xuất sắc nhiệm vụ được giao!". Bố cục: Toàn đội cùng nâng ly chúc mừng trong ánh sáng ban mai rực rỡ.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhắc nhở nhẹ nhàng từ bộ phận giám sát: nếu cậu bay thẳng, áp lực gió sẽ thổi bung cả mắt lẫn mũi cậu đấy! Cẩn thận kẻo biến thành món chim nướng siêu thanh!". Bố cục: chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép chõ mỏ vào micro phòng truyền tin, vẻ mặt nhăn nhở cà khịa nhưng ánh mắt vẫn chăm chú theo dõi màn hình tín hiệu; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L450</summary>

```text
HÌNH L450 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và bây giờ là phần được mong chờ nhất trong mọi bộ phim điệp viên: lễ trao thù lao và giải tán lực lượng!". Bố cục: Mười chiếc hộp quà bọc giấy màu sắc rực rỡ xếp hàng dài trên bàn, mỗi hộp có dán một chiếc nhãn tên riêng biệt; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L451</summary>

```text
HÌNH L451 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đặc vụ Chuột Chũi Trũi được trao tặng ba bao tải khoai tây mật sấy bơ thượng hạng, cộng thêm một giấy chứng nhận: "Thợ đào hầm hảo hạng không bao giờ biết đau"!". Bố cục: chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên sung sướng ôm chặt bao khoai tây to tướng, hai chân trước vẫy vẫy, đeo chiếc huy chương bạc hình củ khoai tây lấp lánh trước ngực; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L452</summary>

```text
HÌNH L452 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đặc vụ Quạ Đen nhận một xô hạt dẻ rang bơ khổng lồ cùng một bộ kìm kẹp đa năng mạ vàng 24K để tha hồ chế tạo công cụ mới!". Bố cục: chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép ngậm chiếc kìm mạ vàng sáng loáng, đầu nghiêng ngả điệu đà, khoái chí cất tiếng kêu quạ quạ khoe khoang với cả đội; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L453</summary>

```text
HÌNH L453 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đặc vụ Chim Cắt Lớn được đền bù một bộ áo khoác da phi công hàng hiệu mới tinh, kèm một chiếc cà vạt lụa chống kiến cắn siêu bền!". Bố cục: chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng đứng trước gương chỉnh lại chiếc cà vạt lụa màu xanh hải quân mới toanh, vuốt lại bộ lông cánh bóng bẩy vẻ mặt vô cùng mãn nguyện; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L454</summary>

```text
HÌNH L454 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đặc vụ Ếch Gỗ Bắc Cực được quàng một chiếc khăn len đỏ ca-sơ-mia mềm mại chống rét âm 50°C, kèm một bình si-rô ngọt ngào bổ dưỡng!". Bố cục: chú Ếch Gỗ Bắc Cực hoạt hình da nâu vàng có vệt đen qua mắt như mặt nạ Zorro, đeo khăn quàng cổ đỏ thắm chống rét, người phủ lớp sương tuyết lấp lánh quàng chiếc khăn len đỏ mới tinh mỉm cười tít mắt, hai má phồng tròn rung rinh hạnh phúc; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L455</summary>

```text
HÌNH L455 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đặc vụ Cá Voi Sát Thủ nhận một tấm thẻ hội viên VIP bơi lội trọn đời tại toàn bộ các rạn san hô đẹp nhất thế giới, kèm một tấn cá hồi tươi rói!". Bố cục: chú Cá Voi Sát Thủ hoạt hình thân đen bóng bụng trắng tinh, vây lưng cao vút cắm ăng-ten định vị sonar nhỏ xíu, miệng cười nhếch mép kiểu trùm mafia biển cả nhô đầu lên khỏi bể nước ngậm một chú cá hồi tươi, vẫy vẫy chiếc thẻ VIP màu vàng kim trên vây ngực; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L456</summary>

```text
HÌNH L456 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đặc vụ Chim Gõ Kiến nhận một chiếc mũ bảo hộ bằng sợi các-bon siêu nhẹ có giảm chấn ba lớp, giúp anh chàng gõ đá mà êm như gõ gối bông!". Bố cục: chú Chim Gõ Kiến hoạt hình mào lông đỏ rực dựng đứng, mỏ dài sắc nhọn như mũi khoan titan, đội mũ bảo hộ lao động màu vàng có gắn đèn pin thợ mỏ đội chiếc mũ bảo hộ mới toanh bóng loáng, gõ mỏ lách cách vào mặt bàn để kiểm tra độ êm; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L457</summary>

```text
HÌNH L457 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lạc Đà Sa Mạc nhận một xe tải xương rồng non mọng nước đã được nhổ sạch gai, tha hồ nhai rôm rốp mà không sợ làm phiền bộ đàm của ai nữa!". Bố cục: chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao đứng nhai tóp tép đống xương rồng mọng nước ngọt ngào, miệng cười toe toét không chớp mắt; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L458</summary>

```text
HÌNH L458 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Dê Núi Bắc Mỹ nhận bốn chiếc đệm móng guốc cao su thể thao hàng hiệu chống trượt tối tân để tha hồ leo vách đá 90°!". Bố cục: chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt giơ một móng trước lên khoe lớp đệm cao su mới tinh màu xanh lá cây đầy phong cách; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L459</summary>

```text
HÌNH L459 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chim Bách Thanh được trang bị một giàn gai thép không gỉ chuyên dụng gắn camera hành trình để bảo quản chiến lợi phẩm an toàn!". Bố cục: chú Chim Bách Thanh hoạt hình lông xám trắng có dải lông đen vắt ngang mắt như dải băng cướp biển, mỏ có móc câu sắc nhọn, chân cầm một nhánh gai nhọn công nghệ cắm một chiếc cúc áo lưu niệm lên giàn gai mới, mắt sáng lên đầy tự hào; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chim Cắt Lớn chỉ nhếch mép cười khẩy qua bộ đàm. Những kẻ nghiệp dư luôn nghĩ bay nhanh chỉ cần đôi cánh khỏe, nhưng họ đâu biết bí mật nằm ở chính chiếc mũi của anh chàng!". Bố cục: Cận cảnh gương mặt sắc lạnh của chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng, chiếc mỏ khoằm vàng óng ánh ánh trăng, ánh mắt tập trung cao độ vào mục tiêu bên dưới; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L460</summary>

```text
HÌNH L460 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và Đại Đội Kiến Cắt Lá được trao tặng một nông trại nấm hữu cơ ngầm rộng 500m² để phát triển nông nghiệp bền vững cho cả tổ kiến!". Bố cục: tiểu đội ba chú Kiến Cắt Lá hoạt hình màu nâu đỏ, đầu to mang hàm răng kim loại sáng loáng, đội mũ cối công binh màu xanh lá, đang vác những mảnh lá xanh như chiếc khiên chắn cùng nhau nâng một cây nấm khổng lồ màu trắng sữa diễu hành vòng quanh bàn tiệc ăn mừng rộn rã; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L461</summary>

```text
HÌNH L461 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mười quái kiệt, mười số phận kỳ lạ của tự nhiên đã hoàn thành sứ mệnh lịch sử. Họ lại quay trở về với bầu trời, rừng sâu, biển cả và lòng đất của riêng mình.". Bố cục: Hình ảnh chia tay đầy xúc động: mười đặc vụ lần lượt vẫy tay chào nhau, chim cắt tung cánh lên trời cao, cá voi bơi về biển lớn, dê núi sải bước lên đỉnh núi tuyết; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L462</summary>

```text
HÌNH L462 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng những bài học tiến hóa kỳ diệu và tinh thần đồng đội của họ sẽ mãi mãi được lưu giữ trong kho tàng tri thức của kênh Vẽ Chuyện Hoang Dã.". Bố cục: Cuộn da cừu Bản Thiết Kế Tiến Hóa được đặt trang trọng trong lồng kính của thư viện tự nhiên, tỏa ánh sáng vàng kim êm đềm; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L463</summary>

```text
HÌNH L463 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Căn phòng tác chiến trở lại yên tĩnh. Chỉ còn lại Chỉ Huy Mật Vụ Cú Mèo ngồi một mình bên bàn làm việc dưới ánh đèn bàn ấm áp.". Bố cục: anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm ngồi dựa lưng vào ghế xoay, khẽ tháo chiếc kính râm xuống để lộ đôi mắt tròn to sáng quắc đầy suy tư; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L464</summary>

```text
HÌNH L464 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Anh chàng mở chiếc ngăn kéo bàn có khóa mật mã hai lớp, cẩn thận cất tập hồ sơ của Biệt Đội Đặc Nhiệm vào góc an toàn.". Bố cục: Chiếc ngăn kéo gỗ trượt mở, bên trong xếp ngay ngắn các tập hồ sơ mật của các mùa trước; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L465</summary>

```text
HÌNH L465 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và rồi, ngón tay của Chỉ Huy dừng lại ở một tập tài liệu bìa màu xanh phẫu thuật y tế còn niêm phong bằng sáp đỏ, có gắn dòng chữ cảnh báo: HỒ SƠ TỐI MẬT SỐ NĂM!". Bố cục: Bàn tay anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm nhấc một tập hồ sơ mới tinh màu xanh ngọc bích y khoa, trên bìa dán con dấu sáp đỏ hình ống nghe bác sĩ và nhịp tim điện tâm đồ; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L466</summary>

```text
HÌNH L466 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một nụ cười bí hiểm nở trên môi vị Chỉ Huy: "Trận chiến này vừa kết thúc... nhưng ca trực đêm kinh hoàng nhất của lịch sử tiến hóa thì chỉ mới bắt đầu."". Bố cục: Cận cảnh anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm mở hé phong bì niêm phong, ánh sáng xanh lơ lạnh lẽo từ bên trong hồ sơ hắt lên khuôn mặt; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L467</summary>

```text
HÌNH L467 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đêm nay, tại Bệnh Viện Đa Khoa Tiến Hóa, mười bệnh nhân mang những triệu chứng sinh học trái ngược hoàn toàn với quy luật thông thường đang đồng loạt nhập viện cấp cứu!". Bố cục: Tranh vẽ phong cách Vintage Hospital thập niên 1950: hành lang bệnh viện dã chiến đêm khuya với các bóng đen bệnh nhân kỳ dị đang nằm trên cáng và xe lăn; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L468</summary>

```text
HÌNH L468 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một chú Nhện Lặn Chuông tự dệt bình dưỡng khí bằng tơ để thở dưới nước. Một chú Cá Thoi Loi trèo cây hít thở bằng da. Một nàng Ong Bắp Cày Ngọc cầm dao phẫu thuật điều khiển não gián.". Bố cục: Ba bức hình phác thảo y khoa đen trắng: chú nhện ôm bọc bong bóng nước, chú cá nhảy nhót trên rễ cây đước và chú ong đang châm ngòi nọc chính xác vào hạch thần kinh gián; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L469</summary>

```text
HÌNH L469 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một chú Cá Mặt Trăng ba tấn không não trôi dạt giữa đại dương. Và một chú Vẹt Ca-ca-pô béo ú quên mất cách bay, đêm đêm nhảy từ ngọn cây xuống đất tìm bạn đời!". Bố cục: Hai bức phác thảo tiếp theo: chú cá mặt trăng tròn vo khổng lồ nằm ngửa phơi nắng và chú vẹt mập ú màu xanh lá đang vụng về leo cây; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy nhìn sâu vào lỗ mũi của Chim Cắt Lớn. Các nhà khoa học tại đại học công nghệ vừa giải mã một kỳ quan kỹ thuật sinh học: một mấu lồi hình nón nhỏ bằng xương nằm ngay chính giữa khoang mũi!". Bố cục: Bản vẽ phóng to chi tiết giải phẫu học bên trong khoang mũi của chim cắt, hiện rõ cấu trúc mấu lồi hình nón tubercle bằng xương chia đôi dòng khí lao vào (không chữ, không số); KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L470</summary>

```text
HÌNH L470 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cùng với Lợn Rừng Ba-bi-ru-sa mang răng nanh tự đâm sọ, Hươu Cao Cổ huyết áp 300, Cò Mỏ Giày đứng như tượng đá và Nhím Lông Nhọn mang 30.000 chiếc gai!". Bố cục: Bức ảnh ghép tổng thể mười bệnh nhân kỳ dị của phòng cấp cứu tiến hóa; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L471</summary>

```text
HÌNH L471 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hẹn gặp lại quý vị khán giả trong Mega số năm: Phòng Cấp Cứu Tạo Hóa — Ca Trực Đêm Kinh Hoàng của mười bệnh nhân tiến hóa kỳ lạ nhất hành tinh!". Bố cục: Màn hình hiện lên dòng chữ hẹn ước đầy tò mò với hình ảnh chiếc ống nghe y tế và bóng lưng bác sĩ trưởng khoa bước vào phòng mổ; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L472</summary>

```text
HÌNH L472 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn bây giờ, nếu bạn được quyền tuyển chọn một đặc vụ trong Biệt Đội Đặc Nhiệm Sinh Học tối nay làm bạn đồng hành, bạn sẽ chọn quái kiệt nào? Hãy để lại mật mã của bạn ở phần bình luận bên dưới nhé!". Bố cục: Mười đặc vụ cùng xếp hàng chào khán giả trên màn hình kết thúc, vẫy tay và nháy mắt tinh nghịch; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L473</summary>

```text
HÌNH L473 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đừng quên bấm thích video, đăng ký kênh Vẽ Chuyện Hoang Dã và nhấn chuông thông báo để không bỏ lỡ những phi vụ sinh tồn chấn động tiếp theo. Chúc các bạn một giấc ngủ thật ngon và những giấc mơ phiêu lưu tuyệt đẹp!". Bố cục: Logo kênh Vẽ Chuyện Hoang Dã hiện lên rực rỡ cùng các nút bấm đăng ký hoạt hình ngộ nghĩnh, ánh đèn mờ dần khép lại một đêm phi vụ thế kỷ hoàn hảo.
```
</details>

<details><summary>L474</summary>

```text
HÌNH L474 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bệnh Viện Đa Khoa Tiến Hóa trong Mega số năm hứa hẹn sẽ mang đến những câu chuyện y khoa hài hước và kỳ thú chưa từng có về mười sinh vật mang thiết kế ngược đời nhất hành tinh!". Bố cục: Hình ảnh phác thảo hài hước về phòng khám bệnh viện tiến hóa với bác sĩ trưởng khoa đang khám bệnh cho chú cá mặt trăng ba tấn nằm trên giường cấp cứu; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L475</summary>

```text
HÌNH L475 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Quý vị sẽ được giải mã vì sao chú vẹt Kakapo béo ú lại quên cách bay, vì sao chú lợn rừng Babirusa lại có răng nanh tự đâm vào sọ, và vì sao hươu cao cổ cúi đầu uống nước mà không bị vỡ mạch nước màu não!". Bố cục: Tranh vẽ mười ca bệnh kỳ lạ xếp hàng trước cửa phòng khám cấp cứu tiến hóa; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L476</summary>

```text
HÌNH L476 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy tiếp tục đồng hành cùng kênh Vẽ Chuyện Hoang Dã để khám phá những điều kỳ diệu bất tận của thế giới tự nhiên xung quanh chúng ta!". Bố cục: Mười đặc vụ của Mega 04 cùng vẫy tay chào tạm biệt khán giả trong tiếng nhạc điệp viên vui nhộn và hào hùng.
```
</details>

<details><summary>L477</summary>

```text
HÌNH L477 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi một tập phim của kênh Vẽ Chuyện Hoang Dã là một hành trình kỳ thú đưa quý vị khán giả đến với những bí mật chưa từng được kể của muôn loài!". Bố cục: Logo kênh phát sáng lung linh giữa bầu trời đêm đầy sao, các nhân vật hoạt hình ngộ nghĩnh cùng vẫy tay chào khán giả; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L478</summary>

```text
HÌNH L478 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy chuẩn bị tinh thần cho những ca trực đêm nghẹt thở và những chẩn đoán y khoa cười ra nước mắt trong mùa phim tiếp theo nhé!". Bố cục: Chiếc xe cứu thương hoạt hình của Bệnh Viện Tiến Hóa lăn bánh vào màn đêm, nhấp nháy đèn xanh báo hiệu một hành trình mới đầy hấp dẫn.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi lao xuống với tốc độ xé gió, mấu xương này đóng vai trò như chiếc van điều áp của động cơ máy bay phản lực, làm chậm và đổi hướng luồng gió xoáy cực mạnh, giúp anh chàng hít thở nhẹ nhàng như đang ngồi uống trà!". Bố cục: Mô phỏng động lực học chất lưu sinh học: các mũi tên luồng khí đỏ lao thẳng vào mũi chim cắt bị bẻ cong thành các đường lượn sóng màu xanh êm dịu đi sâu vào phổi; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không chỉ có mũi, cấu trúc lông cánh của chim cắt còn có những khe rãnh vi mô tự động nâng lên khi gặp áp lực lớn, triệt tiêu toàn bộ lực cản xoáy không khí!". Bố cục: Cận cảnh mép lông cánh của chim cắt tự động điều chỉnh độ cong khi gió rít qua, giữ cho cánh cứng cáp như cánh máy bay chiến đấu; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tọa độ đã khóa! Chim Cắt Lớn thu gọn hai cánh sát vào thân, biến toàn bộ cơ thể thành một đầu đạn khí động học hoàn hảo!". Bố cục: chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng gập hẳn hai cánh thành hình giọt nước khí động học, đuôi ép chặt, cả thân mình lao dốc thẳng đứng chín mươi độ xuống màn đêm đen kịt; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gia tốc tăng vọt! 100 cây số một giờ... 200 cây số một giờ... 300 cây số một giờ! Kim đo tốc độ radar bên dưới phòng chỉ huy quay tít mù!". Bố cục: Màn hình radar thế giới tự nhiên trong phòng điều khiển: kim đồng hồ đo vận tốc nhảy số liên tục từ vạch xanh sang vạch đỏ rực, phát ra tiếng tít tít dồn dập; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và đây là con số kỷ lục từng được các nhà khoa học gắn chip đo đạc thực tế trên cơ thể một chú chim cắt: 389 km/h! Vận tốc nhanh nhất trong toàn bộ thế giới động vật!". Bố cục: Hình ảnh đồ họa ngoạn mục: chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng lao xuống như một quả tên lửa xé toạc màn mây, sóng xung kích hình nón màu trắng ngưng tụ quanh thân chim cắt xé rách không gian; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tiếng rít xé rách không khí vang lên như một tiếng nổ siêu thanh trầm đục, làm rung chuyển cả những vách kính trên đỉnh tháp pháo đài!". Bố cục: Sóng âm thanh lan tỏa hình gợn sóng làm rung rinh các thanh xà kim loại trên vòm kính pháo đài; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ở tốc độ 389 km/h, chỉ một hạt bụi nhỏ bay vào mắt cũng đủ làm nổ tung giác mạc. Nhưng Chim Cắt Lớn vẫn mở to mắt nhìn rõ từng chi tiết của mục tiêu!". Bố cục: Cận cảnh đôi mắt tròn đen láy của chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng, con ngươi co lại cực đại, phản chiếu hình ảnh chiếc công tắc nguồn điện tử bên dưới; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bí quyết là chiếc màng nháy trong suốt che phủ mắt, nhấp nháy với tần số chóng mặt: 120 lần/phút!". Bố cục: Sơ đồ giải phẫu mắt chim cắt: chiếc màng nháy mỏng trong suốt quét qua nhãn cầu như chiếc gạt nước kính ô tô siêu tốc, giữ ẩm và bảo vệ mắt hoàn hảo; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chiếc màng này vừa bôi trơn liên tục vừa lọc bụi bẩn, cho phép Chim Cắt Lớn duy trì tầm nhìn sắc như kính hiển vi điện tử giữa cơn bão gió!". Bố cục: Góc nhìn từ mắt chim cắt qua kính ngắm quang học: mục tiêu chiếc rơ-le điện nhỏ bằng chiếc hộp quẹt trên nóc pháo đài hiện lên rõ mồn một không một vệt mờ; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L57</summary>

```text
HÌNH L57 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyến lệ của chim cắt liên tục tiết ra một chất dịch nhầy đặc biệt có sức căng bề mặt cực lớn, không hề bị gió cuốn bay dù ở vận tốc xé rách âm thanh!". Bố cục: Giọt dịch nhầy bảo vệ mắt lấp lánh như một lớp tráng gương nano trên giác mạc của chim; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L58</summary>

```text
HÌNH L58 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khoảng cách còn 100 mét! Cột laser phòng vệ phát hiện mục tiêu và quét chéo qua!". Bố cục: Hai luồng tia laser đỏ rực từ tháp canh phóng vút tới cắt ngang đường bay, không khí xung quanh bốc khói khét lẹt; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L59</summary>

```text
HÌNH L59 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chim Cắt Lớn khẽ nghiêng một góc 45 độ theo đường xoắn ốc toán học, lượn né tia laser chỉ trong 0,1 giây!". Bố cục: chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng thực hiện cú bẻ lái lượn vòng xoắn ốc điệu nghệ trên không, tia laser sượt qua mép lông cánh làm rụng một sợi lông tơ nhỏ; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L60</summary>

```text
HÌNH L60 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đường bay xoắn ốc này được lập trình tự nhiên theo quy luật đường cong lô-ga-rít, giúp mắt chim luôn hướng thẳng vào mục tiêu trong khi toàn thân nghiêng né đạn!". Bố cục: Mô phỏng đường bay xoắn ốc màu vàng kim lượn lách qua các chùm tia laser đỏ rực đan chéo nhau; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L61</summary>

```text
HÌNH L61 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khoảng cách còn 10 mét! Anh chàng duỗi thẳng cặp móng vuốt vàng sắc nhọn, bọc mạ lớp thép bảo hộ, đạp thẳng vào công tắc nguồn điện tử!". Bố cục: Cận cảnh đôi móng vuốt sắc nhọn của chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng đạp trúng chiếc hộp cầu dao trung tâm, các tia lửa điện nổ tung tóe chói lòa; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L62</summary>

```text
HÌNH L62 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Xoẹt! Tiếng điện nổ râm ran, toàn bộ mạng lưới laser bảo vệ trên không vụt tắt đen ngòm! Vòm kính pháo đài từ từ hé mở!". Bố cục: Toàn bộ hệ thống đèn laser trên tháp pháo đài chớp nháy rồi phụt tắt, cánh cửa vòm kính khổng lồ kêu kẽo kẹt trượt mở ra một lối vào tối om; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L63</summary>

```text
HÌNH L63 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chim Cắt Lớn dang rộng đôi cánh phanh gấp giữa không trung, nhẹ nhàng hạ cánh xuống mép thành đá, giơ một ngón cánh làm dấu hiệu thắng lợi qua camera ngực.". Bố cục: chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng đứng trên lan can đá ngẩng cao đầu chỉnh lại kính phi công, giơ ngón cánh ra hiệu OK về phía ống kính camera nhỏ trên ngực áo; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L64</summary>

```text
HÌNH L64 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thanh tiến độ Cửa Ải 1 trên bản đồ chuyển sang màu xanh ngọc bích! Không phận tử thần đã bị vô hiệu hóa hoàn toàn trong vòng chưa đầy 2 phút!". Bố cục: bản đồ hologram 3D của Pháo Đài Tự Nhiên nổi lơ lửng trong không khí, hiển thị 7 cửa ải an ninh phát sáng đỏ và thanh tiến độ phá khóa màu xanh ngọc (không có chữ, không có số) cập nhật tín hiệu: biểu tượng gió lốc Cửa Ải 1 đổi từ màu đỏ rực sang màu xanh ngọc phát sáng êm dịu, thanh tiến độ nhích lên một nấc; anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm gật đầu hài lòng.
```
</details>

<details><summary>L65</summary>

```text
HÌNH L65 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng niềm vui chưa kịp trọn vẹn thì dưới chân tháp, một tiếng còi báo động trầm đục vang lên từ lòng đất. Hệ thống phòng thủ tự động vừa đóng sập toàn bộ cửa thông gió!". Bố cục: Cửa sắt dày cộp dưới chân tháp đóng ầm xuống, đèn cảnh báo màu vàng chớp liên hồi, khói xám bắt đầu tỏa ra từ các kẽ đá; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L66</summary>

```text
HÌNH L66 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lối vào duy nhất lúc này là hệ thống đường ống xả ngầm sâu dưới lòng đất, nơi không hề có dưỡng khí và ngập tràn sương axit.". Bố cục: Bản đồ hologram hiển thị một mạng lưới đường ống ngoằn ngoèo màu xám chì nằm sâu dưới lòng đá, đầy biểu tượng khí độc và bình axit; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L67</summary>

```text
HÌNH L67 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chỉ Huy Mật Vụ bấm nút gọi nội bộ: "Đặc vụ Chuột Chũi Trũi, khoang yếm khí đã sẵn sàng cho cậu. Đừng có mải ngủ gật đấy nhé!"". Bố cục: Cận cảnh anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm nhìn vào micro, bên cạnh là chiếc ghế trống của chuột chũi với một lỗ hổng tròn vo vừa bị đào khoét dưới gầm bàn; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L68</summary>

```text
HÌNH L68 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Từ dưới đáy một đường ống kim loại gỉ sét, một cái mũi màu hồng nhăn nheo khẽ thò ra, hắt xì một cái rõ to. Cuộc đột nhập tầng hầm bắt đầu!". Bố cục: Dưới đường ống tối tăm, chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên thò đầu ra khịt khịt mũi, hai chiếc răng cửa sáng loáng dưới ánh đèn pin mini, chuẩn bị bò vào mê cung tăm tối.
```
</details>

<details><summary>L69</summary>

```text
HÌNH L69 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đặc vụ Chuột Chũi xoa hai chân trước, chuẩn bị kích hoạt vũ khí sinh học chống ngạt thở vô song của mình!". Bố cục: chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên chỉnh lại cặp kính nhìn đêm, cười toe toét khoe hai chiếc răng cửa dài ngoằng chuẩn bị đối đầu với hầm ngầm không dưỡng khí.
```
</details>

<details><summary>L70</summary>

```text
HÌNH L70 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các phi công lái máy bay siêu thanh của quân đội từng thử nghiệm mô phỏng đường bay của chim cắt trên máy tính và đều phải lắc đầu chịu thua!". Bố cục: Màn hình mô phỏng máy bay chiến đấu phản lực bay song song với một chú chim cắt lớn đang lao dốc; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L71</summary>

```text
HÌNH L71 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ở góc bổ nhào 45 độ, gia tốc trọng trường kéo chú chim lao đi nhanh hơn bất kỳ mũi tên phun tia nước tầm xa nào từng được phóng ra!". Bố cục: Đường bay đỏ rực của chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng cắt ngang các tầng mây đen, tạo nên một vệt khói ngưng tụ trắng xóa; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L72</summary>

```text
HÌNH L72 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đôi mắt chim cắt với lớp màng nháy siêu việt vẫn liên tục truyền về trung tâm chỉ huy những hình ảnh tĩnh nét đến từng con ốc vít của trạm phát laser!". Bố cục: Màn hình nhận tín hiệu từ camera gắn trên trán chim cắt hiển thị rõ nét từng rãnh ren của bu-lông công tắc; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L73</summary>

```text
HÌNH L73 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhịp đập của đôi cánh chim cắt khi lấy thăng bằng sau cú bổ nhào phát ra tiếng rít xé gió khiến cả đàn chim đêm xung quanh phải nể sợ!". Bố cục: chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng bay vút ngang qua đỉnh tháp pháo đài, để lại một vệt hào quang xám bạc lấp lánh; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L74</summary>

```text
HÌNH L74 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bộ cảm biến gia tốc trên ngực áo truyền về trung tâm chỉ huy xác nhận: cấu trúc xương đòn của chim cắt đã hấp thụ hoàn hảo mọi xung chấn của không khí!". Bố cục: Đồ thị phân tích lực cản khí động học hiển thị mức cân bằng tuyệt đối không một điểm dao động bất thường; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L75</summary>

```text
HÌNH L75 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Địa đạo ngầm dưới chân Pháo Đài Tự Nhiên là một cái bẫy chết chóc được thiết kế để tiêu diệt bất kỳ sinh vật hiếu khí nào dám bén mảng tới.". Bố cục: Khung cảnh đường hầm ngầm bằng kim loại rỉ sét u ám, các vòi phun sương tự động đang phun ra những làn sương màu vàng chanh đậm đặc mùi axit, trên tường có các cảm biến đo nồng độ dưỡng khí; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L76</summary>

```text
HÌNH L76 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cửa thép phía sau vừa sập xuống, máy hút chân không lập tức khởi động rên rỉ ầm ầm. Nồng độ dưỡng khí trong ống tụt dốc không phanh: 20 phần trăm... mười phần trăm... năm phần trăm... rồi chạm đáy số không tròn trĩnh!". Bố cục: Đồng hồ đo nồng độ oxy trên tường tụt nhanh về vạch số không đỏ rực, tiếng hút gió rít lên chói tai trong đường ống chật hẹp tối tăm; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L77</summary>

```text
HÌNH L77 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không có lấy một phân tử khí thở. Bất kỳ loài thú nào, kể cả con người hay sư tử, chỉ cần hít thở trong môi trường này 45 giây là sẽ bất tỉnh nhân sự, tế bào não chết vĩnh viễn sau 3 phút.". Bố cục: Một mô hình đồ họa y khoa giải thích sự ngạt thở: các tế bào não thông thường bị thiếu oxy teo lại và phát tín hiệu cảnh báo màu đỏ chớp nháy (không chữ, không số); KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L78</summary>

```text
HÌNH L78 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "CO₂ và nồng độ axit trong hầm tăng vọt lên mức kịch độc, đủ sức làm bỏng cháy niêm mạc phổi của bất kỳ kẻ xâm nhập nào trong tích tắc!". Bố cục: Khói độc màu xám xịt cuộn tròn quanh các vách ống kim loại, rỉ sét ăn mòn bề mặt tạo thành những vệt rỗ loang lổ; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L79</summary>

```text
HÌNH L79 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng kẻ đang bò trong đường ống này lại là một sinh vật coi việc thiếu dưỡng khí... chỉ là một buổi dạo chơi nhẹ nhàng sau bữa trưa!". Bố cục: chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên lắc lư cái đầu nhăn nheo, bốn chân ngắn thoăn thoắt bò tới tấp trong đường ống kim loại, cặp kính hồng ngoại to sụ chớp chớp đèn xanh; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L80</summary>

```text
HÌNH L80 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đặc vụ Chuột Chũi Trũi thong dong bước đi, không hề tỏ ra hoảng loạn hay ngột ngạt. Bí mật sinh học chấn động gì đã giúp anh chàng này thách thức quy luật hô hấp của muôn loài?". Bố cục: Cận cảnh gương mặt của chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên, hai chiếc răng cửa to tướng gõ lách cách vào thành ống thép, chiếc đuôi ngắn ngoe nguẩy điều hướng; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L81</summary>

```text
HÌNH L81 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cơ thể không lông của anh chàng được bao bọc bởi một lớp da siêu đàn hồi chứa đầy phân tử axit hyaluronic trọng lượng cực cao, giúp da trơn tuột không hề trầy xước khi cọ xát vào mép ống kim loại sắc nhọn!". Bố cục: Kính hiển vi quét màng tế bào da chuột chũi: các chuỗi phân tử cao phân tử HMM-HA đan chéo nhau như một mạng lưới bảo vệ dẻo dai chống lại mọi ma sát; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L82</summary>

```text
HÌNH L82 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Năm 2017, một nghiên cứu đột phá đăng trên tạp chí Khoa Học danh giá đã vén màn bí mật: khi hết sạch dưỡng khí, cơ thể Chuột Chũi Trũi tự động chuyển sang chế độ hoạt động của... thực vật!". Bố cục: Tranh minh họa sinh học so sánh hai nhánh tiến hóa: một bên là cây xanh quang hợp rực rỡ, một bên là chú chuột chũi trũi đang phát sáng các hạt phân tử đường màu xanh lục bên trong tế bào; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L83</summary>

```text
HÌNH L83 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đúng vậy, bạn không nghe nhầm đâu! Bộ não và trái tim của các loài động vật có vú thông thường chỉ có thể đốt đường glucose bằng dưỡng khí để tạo năng lượng. Không có dưỡng khí, cỗ máy ngừng chạy ngay lập tức.". Bố cục: Sơ đồ phân tử: chu trình phân giải đường glucose thông thường bị dấu chéo đỏ chặn đứng khi thiếu oxy, biểu tượng pin năng lượng cạn kiệt; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L84</summary>

```text
HÌNH L84 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng Chuột Chũi Trũi lại sở hữu những thụ thể vận chuyển đường đặc biệt có tên gọi là phân tử vận chuyển đường hoa quả GLUT5, giúp chúng kích hoạt việc đốt trực tiếp đường fructose mà không cần đến một phân tử dưỡng khí nào!". Bố cục: Các phân tử đường fructose hình ngôi sao màu tím lấp lánh tràn vào tế bào tim và não của chuột chũi, tái kích hoạt bộ máy năng lượng hoạt động trơn tru; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L85</summary>

```text
HÌNH L85 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đường fructose đi thẳng vào chu trình đường phân ở cơ tim và vỏ não, sản sinh năng lượng duy trì sự sống bền bỉ ngay giữa vùng chân không!". Bố cục: Mô phỏng các hạt năng lượng ATP màu vàng sáng bừng lên bên trong tế bào não chuột chũi, nuôi dưỡng các xung thần kinh hoạt động bình thường; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L86</summary>

```text
HÌNH L86 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thử nghiệm khoa học chấn động tại phòng thí nghiệm đã chứng minh: Chuột Chũi Trũi có thể sống sót khỏe mạnh suốt 18 phút trong môi trường hoàn toàn 0% oxy!". Bố cục: chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên nằm thư thái trong một buồng kính thí nghiệm chân không kín mít, xung quanh là các nhà khoa học trố mắt nhìn đồng hồ bấm giờ chạm mốc 18:00 (không chữ); KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L87</summary>

```text
HÌNH L87 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi có dưỡng khí trở lại, chúng đứng dậy phủi bụi và đi lại bình thường như chưa từng có chuyện gì xảy ra, không hề tổn thương dù chỉ một tế bào thần kinh!". Bố cục: chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên vươn vai ngáp một cái thật dài, phủi hai móng trước vào bụng rồi tiếp tục bò thoăn thoắt trên mặt sàn; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L88</summary>

```text
HÌNH L88 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhịp tim của chuột chũi tự động hạ từ 200 nhịp một phút xuống còn 50 nhịp một phút để tiết kiệm tối đa năng lượng, đưa cơ thể vào trạng thái ngủ đông cục bộ cực kỳ thông minh!". Bố cục: Biểu đồ nhịp tim co giãn chậm rãi và ổn định, duy trì áp lực nước màu hoàn hảo đến các cơ quan trọng yếu; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L89</summary>

```text
HÌNH L89 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng thử thách của Cửa Ải 2 chưa dừng lại ở đó. Hệ thống phòng thủ tự động phát hiện kẻ xâm nhập vẫn còn sống, liền kích hoạt tầng bẫy thứ hai: vòi phun axit!". Bố cục: Các đầu phun trên trần đường ống tự động xoay nòng, phun ra từng luồng sương axit châm chích mù mịt phủ kín toàn bộ lối đi; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L90</summary>

```text
HÌNH L90 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Làn sương axit có độ pH ba cực kỳ ăn mòn và bỏng rát, đủ sức làm phồng rộp làn da của bất kỳ kẻ đột nhập nào trong nháy mắt.". Bố cục: Những giọt axit màu xanh vàng rơi xuống sàn kim loại kêu xèo xèo, bốc lên những làn khói cay nồng mù mịt; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L91</summary>

```text
HÌNH L91 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sương axit bắn thẳng vào thân mình không một sợi lông của Chuột Chũi Trũi. Bộ đàm phòng chỉ huy nín thở! Chỉ Huy Mật Vụ siết chặt tay!". Bố cục: Màn hình theo dõi nhiệt độ cơ thể trong phòng điều khiển chao đảo, anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm nhíu mày áp sát mặt vào màn hình kính râm; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L92</summary>

```text
HÌNH L92 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng Chuột Chũi Trũi... chỉ khẽ gãi gãi nách rồi tiếp tục bò! Anh chàng thậm chí còn không thèm chớp mắt!". Bố cục: chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên đứng giữa làn sương axit mù mịt, lấy một chân sau gãi gãi bụng vẻ mặt tỉnh bơ ngây thơ như đang tắm suối nước nóng; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L93</summary>

```text
HÌNH L93 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bởi vì tạo hóa đã tặng cho loài vật này một món quà vô giá: chúng hoàn toàn mất tín hiệu dẫn truyền cơn đau của chất hóa học P và thụ thể thần kinh cảm giác!". Bố cục: Hình vẽ hiển vi phóng to sợi dây thần kinh dưới da của chuột chũi: tín hiệu đau hình tia sét màu đỏ bị chặn đứng hoàn toàn bởi một nút công tắc sinh học tự nhiên màu xanh ngọc; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L94</summary>

```text
HÌNH L94 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Axit hay ớt cay hay lửa rát chạm vào da chuột chũi trũi cũng chẳng khác gì nước lã gội đầu! Chúng không hề biết đau là cái gì trên cõi đời này!". Bố cục: chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên tiếp tục bò qua vũng axit bốc khói, thản nhiên như một chiến binh mang giáp hộ thân tàng hình; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L95</summary>

```text
HÌNH L95 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà thần kinh học tại đại học Cambridge phát hiện ra rằng thụ thể kênh ion TrkA của chuột chũi đã bị đột biến, biến chúng thành loài động vật có vú duy nhất trơ lì trước axit!". Bố cục: Sơ đồ kênh ion trên màng tế bào thần kinh: phân tử axit chạm vào thụ thể nhưng không thể kích hoạt xung điện thần kinh truyền về tủy sống; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L96</summary>

```text
HÌNH L96 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lối đi phía trước đột ngột bị một tảng đá cản đường, và đường ống quá hẹp khiến chuột chũi không thể xoay người quay đầu lại!". Bố cục: Một khối đá xám to đùng rơi chắn ngang đường ống chật chội, khe hở chỉ vừa khít thân hình chuột chũi, không có chỗ để quay đầu xe; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L97</summary>

```text
HÌNH L97 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không cần quay đầu! Chuột Chũi Trũi cài số lùi, chạy lùi với tốc độ nhanh y hệt như chạy tiến nhờ chiếc đuôi nhạy bén như chiếc ăng-ten cảm biến lùi ô tô!". Bố cục: chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên chạy giật lùi thoăn thoắt về phía sau, chiếc đuôi ngắn ngỏng lên chạm nhẹ vào hai bên vách ống để dò đường cực kỳ chuẩn xác; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L98</summary>

```text
HÌNH L98 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Anh chàng đổi hướng bò sang một nhánh rẽ thông hơi, tiếp cận chiếc van khóa áp lực chính của pháo đài!". Bố cục: chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên chui vào một ngách thông gió thẳng đứng, trèo ngược lên bằng bốn chân có móng vuốt chắc khỏe; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>L99</summary>

```text
HÌNH L99 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cặp răng cửa khổng lồ dài ngoằng thò ra ngoài môi bắt đầu phát huy tác dụng. Chuột chũi có thể cử động hai chiếc răng cửa độc lập như một đôi đũa gắp thức ăn!". Bố cục: Cận cảnh hai chiếc răng cửa to tướng của chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên kẹp chặt lấy chiếc chốt khóa van kim loại, cơ hàm nghiền nghiến với lực cắn khủng khiếp; KHÔNG có anh Chỉ Huy trong cảnh này.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Mười đặc vụ quái kiệt. Bảy cửa ải an ninh. Một phi vụ thế kỷ đột nhập Pháo Đài Tự Nhiên!". Bố cục: bản đồ hologram 3D của Pháo Đài Tự Nhiên nổi lơ lửng trong không khí, hiển thị 7 cửa ải an ninh phát sáng đỏ và thanh tiến độ phá khóa màu xanh ngọc (không có chữ, không có số) sáng rực với bảy cửa ải đỏ rực giữa căn phòng tối, anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm đứng chỉ tay vào bản đồ cùng bóng đen của mười đặc vụ.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Cửa Ải 1: Chim Cắt Lớn bổ nhào xé gió 389 km/h vô hiệu hóa lưới laser!". Bố cục: chú Chim Cắt Lớn hoạt hình mắt sắc lạnh, lông xám đen bụng vân ngang, mỏ khoằm vàng, đeo kính bảo hộ phi công siêu thanh và ba-lô phản lực mini gập gọn sau lưng lao xuống như quả tên lửa xé toạc màn đêm, sóng xung kích trắng xóa quanh thân.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Cửa Ải 2: Chuột Chũi Trũi thở bằng đường hoa quả sống sót 18 phút ở mức 0% oxy!". Bố cục: chú Chuột Chũi Trũi hoạt hình da hồng nhăn nheo không lông, hai răng cửa to chìa ra ngoài, đeo kính nhìn đêm hồng ngoại ngộ nghĩnh và đai thắt lưng công cụ điệp viên bò thoăn thoắt trong đường ống ngập sương axit, cặp kính hồng ngoại chớp sáng.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Cửa Ải 3: Ếch Gỗ Bắc Cực chủ động đóng băng 65% cơ thể, tim ngừng đập qua mặt cảm biến tầm nhiệt!". Bố cục: chú Ếch Gỗ Bắc Cực hoạt hình da nâu vàng có vệt đen qua mắt như mặt nạ Zorro, đeo khăn quàng cổ đỏ thắm chống rét, người phủ lớp sương tuyết lấp lánh biến thành một bức tượng băng trong suốt trượt êm ái trên sàn băng tuyết.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Cửa Ải 4: Quạ Đen dùng trí tuệ giải mã chuỗi bẫy cơ học 8 bước và lóa mắt ống kính quan sát hoạt hình vui nhộn!". Bố cục: chú Quạ Đen hoạt hình lông đen ánh tím bóng bẩy, mắt tròn tinh quái, mỏ kẹp chiếc kẹp gắp kim loại, đeo tạp dề kỹ sư mini chứa đầy cờ-lê và dây thép ngậm móc câu thép mở ngăn kéo bí mật, nháy mắt tinh nghịch trước ống kính.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Cửa Ải 5: Cá Voi Sát Thủ bắn xung sonar 225 dB quất sóng thần phá đập nước ngầm!". Bố cục: chú Cá Voi Sát Thủ hoạt hình thân đen bóng bụng trắng tinh, vây lưng cao vút cắm ăng-ten định vị sonar nhỏ xíu, miệng cười nhếch mép kiểu trùm mafia biển cả rẽ nước quất mạnh vây đuôi tạo sóng thần áp lực đập tung cửa van thép.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Cửa Ải 6: Chim Gõ Kiến triệt tiêu 1200G cùng Đại Đội Kiến Cắt Lá dùng răng thép đục sập boong-ke!". Bố cục: chú Chim Gõ Kiến hoạt hình mào lông đỏ rực dựng đứng, mỏ dài sắc nhọn như mũi khoan titan, đội mũ bảo hộ lao động màu vàng có gắn đèn pin thợ mỏ gõ mỏ tóe lửa vào vách đá granite, bên dưới là đàn kiến cắt lá mang hàm thép hỗ trợ.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Cửa Ải 7: Dê Núi phi thân leo vách đứng 90° và Lạc Đà vượt sa mạc 50°C hạ cầu treo!". Bố cục: chú Dê Núi Bắc Mỹ hoạt hình lông trắng muốt bờm cổ dày, cặp sừng đen nhọn cong nhẹ, bốn móng guốc bọc đệm cao su leo núi chuyên dụng chống trượt bám móng giác hút leo vách đá chín mươi độ, phía dưới chú Lạc Đà hai bướu hoạt hình lông vàng cát dày mịn, mắt to hàng mi cong dài, cổ quấn khăn rằn sa mạc, lưng thồ hai bình nước dã chiến áp lực cao đứng kiêu hãnh trên cát đỏ.
```
</details>

<details><summary>S09</summary>

```text
HÌNH S09 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Và kho báu tối thượng là gì? Không phải vàng bạc, mà là kiệt tác tiến hóa nằm ngay trong chính bản thân mỗi loài!". Bố cục: anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm mở nắp két sắt tối thượng, một quả cầu ánh sáng sinh học rực rỡ bừng nở soi rọi cả mười đặc vụ.
```
</details>

<details><summary>S10</summary>

```text
HÌNH S10 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Bạn ấn tượng với siêu năng lực của đặc vụ nào nhất? Xem trọn bộ phi vụ thế kỷ trong video dài nhé,". Bố cục: Mười đặc vụ cùng tạo dáng cực ngầu dưới ánh trăng, anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm giơ huy hiệu điệp viên chào khán giả.
```
</details>

<details><summary>S11</summary>

```text
HÌNH S11 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật anh Chỉ Huy Mật Vụ điệp viên cú mèo mặc áo măng-tô đen đeo kính râm cùng 10 đặc vụ động vật hoạt hình mặc giáp điệp viên; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "vì ở đây chỉ có 10 đặc vụ quái kiệt, 7 cửa ải sinh tử, và một phi vụ thế kỷ!". Bố cục: bản đồ hologram 3D của Pháo Đài Tự Nhiên nổi lơ lửng trong không khí, hiển thị 7 cửa ải an ninh phát sáng đỏ và thanh tiến độ phá khóa màu xanh ngọc (không có chữ, không có số) sáng rực với bảy biểu tượng màu xanh ngọc bích, mười đặc vụ cùng nhảy lên ăn mừng chiến thắng.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/478 của video YouTube về 10 đặc vụ — Biệt Đội Đặc Nhiệm Sinh Học). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa vẽ tay đặc trưng cho chủ đề, nét mực sắc nét, màu sắc tương phản cuốn hút, tối giản giàu tính biểu tượng khoa học; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: anh Chỉ Huy Mật Vụ điệp viên cú mèo hoạt hình đeo kính râm đen ngầu, mặc áo măng-tô đen cổ đứng có gắn huy hiệu đặc nhiệm bạc, tai đeo tai nghe bộ đàm điệp viên, cầm máy tính bảng hologram phát sáng xanh. Nhân vật phụ cố định: anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/11 của video YouTube Shorts về 10 đặc vụ — Biệt Đội Đặc Nhiệm Sinh Học). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa vẽ tay đặc trưng cho chủ đề, nét mực sắc nét, màu sắc tương phản cuốn hút, tối giản giàu tính biểu tượng khoa học; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: anh Chỉ Huy Mật Vụ điệp viên cú mèo hoạt hình đeo kính râm đen ngầu, mặc áo măng-tô đen cổ đứng có gắn huy hiệu đặc nhiệm bạc, tai đeo tai nghe bộ đàm điệp viên, cầm máy tính bảng hologram phát sáng xanh. Nhân vật phụ: anh Chỉ Huy Mật Vụ cú mèo hoạt hình áo măng-tô đen đeo kính râm và tai nghe bộ đàm. 
```
</details>

## 7. SEO

- **title:** [TẬP ĐẶC BIỆT] Phi Vụ Thế Kỷ: Biệt Đội Đặc Nhiệm Sinh Học Đột Nhập Pháo Đài Tự Nhiên
- **hook_paragraph:** Mười đặc vụ quái kiệt nhất hành tinh — Chim Cắt Lớn, Chuột Chũi Trũi, Ếch Gỗ Bắc Cực, Quạ Đen, Cá Voi Sát Thủ, Chim Gõ Kiến, Lạc Đà Sa Mạc, Dê Núi Bắc Mỹ, Chim Bách Thanh và Kiến Cắt Lá — được Tổng Cục Mật Vụ triệu tập vào phi vụ thế kỷ: Đột nhập Pháo Đài Tự Nhiên qua 7 Cửa Ải An Ninh sinh tử! Toàn bộ đều dựa trên các công trình nghiên cứu khoa học MỚI 100%: Chim Cắt có vòi xoáy nén khí 389 km/h, Chuột Chũi thở bằng đường ăn fructose khi cạn oxy, Ếch Gỗ đóng băng tim ngừng đập 7 tháng, Quạ Đen giải mã câu đố 8 bước, Cá Voi Sát Thủ bắn sóng sonar 225 dB, Chim Gõ Kiến chịu lực xung chấn 1200G, và Dê Núi phi thân vách đá 90 độ... Liệu biệt đội có phá khóa thành công kho báu tiến hóa tối thượng?
- **question:** Nếu được chọn một đặc vụ đồng hành trong phi vụ thế kỷ này, bạn sẽ chọn quái kiệt nào? Bình luận mật mã của bạn bên dưới nhé!
- **next_teaser:** Mega 05 — Phòng Cấp Cứu Tạo Hóa: Ca Trực Đêm Kinh Hoàng của 10 Bệnh Nhân Tiến Hóa
- **shorts_title:** Biệt Đội Điệp Viên Động Vật Đột Nhập Pháo Đài Tối Mật! 🕶️💥 #shorts #dongvat
- **shorts_desc:** Chim Cắt bổ nhào 389 km/h, Chuột Chũi sống 0% oxy, Quạ Đen bẻ khóa 8 bước... Biệt đội đặc nhiệm sinh học thực hiện phi vụ thế kỷ đột nhập Pháo Đài Tự Nhiên! 🕶️🔥
👉 Xem trọn bộ Mega 04 — tập đặc biệt trên kênh Vẽ Chuyện Hoang Dã.
- **bullets:** Hồ sơ mật: Triệu tập 10 đặc vụ sinh học bất hảo nhất vào phòng tác chiến tối mật · Cửa Ải 1 – Không phận tử thần: Chim Cắt Lớn bổ nhào 389 km/h xé toạc luồng khí nén · Cửa Ải 2 – Địa đạo yếm khí: Chuột Chũi Trũi kích hoạt chuyển hóa fructose sống sót 0% oxy · Hậu trường 1: Chuột Chũi đào nhầm vào kho thức ăn và Quạ Đen đòi tăng lương bộ đàm · Cửa Ải 3 – Kho lạnh âm hai mươi độ C: Ếch Gỗ Bắc Cực đông đá cơ thể qua mặt cảm biến tầm nhiệt · Cửa Ải 4 – Mê cung bẫy giải mã: Quạ Đen bẻ khóa cơ học 8 bước và đọc vị bẫy camera · Hậu trường 2: Lạc Đà nhai xương rồng rộp rộp làm nhiễu sóng và Bách Thanh cắm gai nhầm chìa khóa · Cửa Ải 5 – Hào nước áp lực: Cá Voi Sát Thủ dùng sonar 225 dB định vị và quất sóng thần phá đập · Cửa Ải 6 – Boong-ke xung chấn: Chim Gõ Kiến triệt tiêu 1200G cùng Đại đội Kiến Cắt Lá khoét móng đá · Cửa Ải 7 – Bức tường dựng đứng 90 độ: Dê Núi đệm móng cao su bám đá cùng Lạc Đà vượt lò nhiệt 50 độ C · Trạm gác ngoại vi: Sát thủ Bách Thanh vô hiệu hóa lính gác bằng kỹ thuật cắm gai nhọn · Phòng châu báu: Cú lật kèo chấn động — kho báu thật sự của Pháo Đài Tự Nhiên · Tháo chạy nghẹt thở: Pháo đài đếm ngược tự hủy 3 phút và màn phối hợp đào tẩu ngoạn mục · Hồ sơ mật kết thúc: Giải tán biệt đội, chia thù lao và hé lộ hồ sơ mật Mùa sau
- **tags:** vẽ chuyện hoang dã, biệt đội đặc nhiệm sinh học, phi vụ thế kỷ, thế giới động vật, động vật kỳ lạ, chim cắt lớn, chuột chũi trũi, ếch gỗ bắc cực, quạ đen, cá voi sát thủ, chim gõ kiến, lạc đà sa mạc, dê núi bắc mỹ, chim bách thanh, kiến cắt lá, khoa học thú vị, whiteboard animation, nghe trước khi ngủ
- **hashtags:** #VeChuyenHoangDa #TheGioiDongVat #BietDoiDacNhiem #DongVatKyLa #KhoaHoc

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/mega-04-biet-doi-dac-nhiem-sinh-hoc
python src/episode/pipeline.py tts    projects/mega-04-biet-doi-dac-nhiem-sinh-hoc     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/mega-04-biet-doi-dac-nhiem-sinh-hoc     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/mega-04-biet-doi-dac-nhiem-sinh-hoc     # phải in 'spec OK'
python scripts/audit_beats.py projects/mega-04-biet-doi-dac-nhiem-sinh-hoc              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/mega-04-biet-doi-dac-nhiem-sinh-hoc --force
python scripts/beat_sheet.py projects/mega-04-biet-doi-dac-nhiem-sinh-hoc               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/mega-04-biet-doi-dac-nhiem-sinh-hoc/audio/shorts.wav projects/mega-04-biet-doi-dac-nhiem-sinh-hoc/renders/mega-04-biet-doi-dac-nhiem-sinh-hoc_shorts.mp4
python src/episode/pipeline.py qa     projects/mega-04-biet-doi-dac-nhiem-sinh-hoc
python src/episode/pipeline.py seo    projects/mega-04-biet-doi-dac-nhiem-sinh-hoc
python src/episode/episode_doc.py     projects/mega-04-biet-doi-dac-nhiem-sinh-hoc
```
