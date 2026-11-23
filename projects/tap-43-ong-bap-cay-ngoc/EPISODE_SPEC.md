# TẬP 43 — ONG BẮP CÀY NGỌC · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-43-ong-bap-cay-ngoc`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-43-ong-bap-cay-ngoc`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F3` · **Persona giọng:** `phien_toa` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Ong Bắp Cày Ngọc |
| Tiêu đề YouTube | Bác Sĩ Phẫu Thuật Thần Kinh: Thao Túng Gián Thành Zombie?! \| Ong Bắp Cày Ngọc \| Tập 43 |
| Video dài | `renders/tap-43-ong-bap-cay-ngoc_long.mp4` — 9:33.1 (573.1s) |
| Shorts | `renders/tap-43-ong-bap-cay-ngoc_shorts.mp4` — 0:44.1 (44.1s) |
| Thumbnail | `renders/tap-43-ong-bap-cay-ngoc_thumbnail.jpg` |
| Số hình | dài 64 beat / 64 ảnh riêng; Shorts 10 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.1**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/58 của video YouTube về Ong Bắp Cày Ngọc). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa vẽ tay đặc trưng cho chủ đề, nét mực sắc nét, màu sắc tương phản cuốn hút, tối giản giàu tính biểu tượng khoa học; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái). Nhân vật phụ cố định: chú gián to gấp sáu lần ong, màu nâu cánh gián bóng lưỡng, mắt xoắn ốc đờ đẫn ngoan ngoãn như Zombie, râu bị cắt ngắn một nửa; thẩm phán cú mèo uy nghiêm đội tóc giả quan tòa màu trắng, mặc áo thụng đen, tay cầm búa gõ. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — VỤ ÁN THAO TÚNG TÂM TRÍ CHẤN ĐỘNG GIỚI CÔN TRÙNG
*Thẻ chương:* BẢN CÁO TRẠNG THAO TÚNG NÃO BỘ VÀ TƯỚC ĐOẠT Ý CHÍ TỰ DO

*Badge:* `CÁO TRẠNG VỤ ÁN` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene01_p0.wav` (625 ký tự) · mood `tram_bi_an`

```text
Trật tự toàn thể phòng xử án hình sự sinh học tối cao! Đại diện Viện Kiểm Sát Tự Nhiên hôm nay chính thức công bố bản cáo trạng điều tra đặc biệt về một vụ án xâm phạm thân thể và thao túng tâm lý tàn bạo bậc nhất trong lịch sử tiến hóa động vật! Không dùng sức mạnh cơ bắp áp đảo, không xé xác nạn nhân tại chỗ, kẻ thủ ác này khoác lên mình một tấm áo choàng ngọc bích lộng lẫy kiêu sa nhưng lại sở hữu thủ đoạn giải phẫu thần kinh lạnh lùng đến rợn gáy! Gã không giết chết con mồi, mà biến một chiến binh gián khỏe mạnh, nhanh nhẹn bậc nhất hành tinh thành một xác sống Zombie ngoan ngoãn tự bước chân vào nấm mồ chôn sống!
```
**Part 1** → `audio/vs/scene01_p1.wav` (117 ký tự) · 🎭 cameo `tham_phan`

```text
Trật tự phiên tòa! Thẩm phán yêu cầu công tố viên công bố danh tính bị cáo và vạch trần thủ đoạn gây án ngay lập tức!
```
**Part 2** → `audio/vs/scene01_p2.wav` (702 ký tự) · mood `hao_hung`

```text
[surprise-oh] Thưa Hội đồng xét xử! Bị cáo mang mã số bốn mươi ba của chúng ta có tên khoa học là Ampulex compressa, thuộc bộ cánh màng, hay còn được gọi bằng cái tên hoa mỹ là Ong Bắp Cày Ngọc! Nhưng trong giới giang hồ tự nhiên, nạn nhân và các nhà khoa học gọi gã bằng một biệt danh rùng rợn: Bác sĩ phẫu thuật thần kinh! Chiều dài cơ thể của gã chỉ khoảng hai mươi mi-li-mét, khoác lớp vỏ chitin lấp lánh ánh kim màu xanh ngọc lục bảo và lam biếc tuyệt đẹp tựa như một viên đá quý di động! Nhưng đừng để vẻ ngoài kiều diễm ấy đánh lừa, bởi vì chiếc đuôi của gã cất giấu một chiếc kim tiêm vi phẫu tinh xảo đến mức khiến mọi giáo sư phẫu thuật sọ não loài người cũng phải ngả mũ bái phục! [laughter]
```
**Part 3** → `audio/vs/scene01_p3.wav` (555 ký tự) · mood `nghiem_trang_gia`

```text
Trước khi đi vào hiện trường gây án, Viện Kiểm Sát xin nhấn mạnh rằng: Nạn nhân của Bác sĩ phẫu thuật thần kinh không phải là những sâu bọ mềm yếu. Nạn nhân là loài gián nhà Mỹ Periplaneta americana, một loài sinh vật sống dai khét tiếng đã tồn tại hơn ba trăm triệu năm trên Trái Đất! Một loài côn trùng có thể sống sót sau bom nguyên tử, chạy trốn với vận tốc một mét rưỡi mỗi giây, và có thể sống cả tuần mà không cần đầu! Nhưng khi đối đầu với mũi kim của Bác sĩ phẫu thuật thần kinh, toàn bộ sức mạnh kiên cường ấy biến thành con số không tròn trĩnh!
```

### scene02 — MŨI TIÊM SỐ 1 KHÓA CHẶT KHỚP NGỰC NẠN NHÂN
*Thẻ chương:* PHÁT SÚNG GÂY MÊ TẠM THỜI VÀO HẠCH THẦN KINH NGỰC

*Badge:* `ĐÒN TẤN CÔNG #1` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene02_p0.wav` (538 ký tự) · mood `don_dap`

```text
Hãy lật lại từng trang hồ sơ khám nghiệm hiện trường vụ tấn công! Nạn nhân được lựa chọn ở đây là loài gián nhà nhiệt đới. Về tương quan thể lực, con gián to lớn và nặng gấp sáu lần Bác sĩ phẫu thuật thần kinh! Gián sở hữu hệ thống lông cảm biến siêu nhạy ở đuôi, phát hiện được cả những dao động không khí nhỏ nhất và có thể tăng tốc tẩu thoát chỉ trong vòng vài phần nghìn giây. Nếu lao vào một cuộc đấu vật tay đôi trực diện, chú ong nhỏ bé chắc chắn sẽ bị con gián khổng lồ đá văng hoặc nghiền nát dưới những chiếc chân gai nhọn hoắt!
```
**Part 1** → `audio/vs/scene02_p1.wav` (81 ký tự) · 🎭 cameo `tham_phan`

```text
Vậy bị cáo đã làm cách nào để khuất phục một gã khổng lồ to xác gấp sáu lần mình?
```
**Part 2** → `audio/vs/scene02_p2.wav` (774 ký tự) · mood `hao_hung`

```text
[surprise-wa] Đây chính là điểm khởi đầu của kế hoạch gây án bài bản đến kinh ngạc! Bác sĩ phẫu thuật thần kinh không hề chích bừa bãi! Gã phục kích từ trên cao, lao xuống như một tia chớp kim loại và dùng cặp hàm thép kẹp chặt lấy lưng con gián. Ngay trong tích tắc đối phương còn đang bàng hoàng, chiếc kim tiêm từ đuôi ong uốn cong, đâm một phát châm chuẩn xác đến từng mi-li-mét vào hạch thần kinh ngực trước của gián! Độc tố của phát thứ nhất chứa hàm lượng lớn chất ức chế dẫn truyền GABA, ngay lập tức làm tê liệt hoàn toàn hai chiếc chân trước của nạn nhân trong vòng hai đến ba phút! [laughter] Con gián dù vẫn còn tỉnh táo nhưng hai chân trước đã bị liệt hoàn toàn, không thể cựa quậy hay xoay người bỏ chạy! Chiếc áo giáp phản xạ của gián chính thức bị phong tỏa!
```
**Part 3** → `audio/vs/scene02_p3.wav` (584 ký tự) · mood `don_dap`

```text
Nhóm nghiên cứu của giáo sư Kenneth Catania tại Đại học Vanderbilt đã sử dụng máy quay tốc độ cao một ngàn khung hình mỗi giây để giải mã cuộc đụng độ này: Khi gián phát hiện bị ong tập kích, nó thường vung chân sau tung ra những cú đá hậu karate cực mạnh nhằm hất văng kẻ thù. Nhưng Bác sĩ phẫu thuật thần kinh cực kỳ ranh mãnh! Gã lượn vòng từ góc mù, túm chặt lấy mép khiên ngực bảo vệ của gián, biến chính điểm tựa của đối phương thành thế gọng kìm bất khả kháng cự! Cú châm kim số một diễn ra chỉ trong vòng nửa giây, nhanh như một mũi tên tẩm thuốc mê bắn trúng tim đen con mồi!
```

### scene03 — KỸ THUẬT CHÂM KIM NÃO BỘ TƯỚC ĐOẠT Ý CHÍ TỰ DO
*Thẻ chương:* VI PHẪU ĐỘC TỐ ỨC CHẾ NÃO BỘ BIẾN THÀNH XÁC SỐNG

*Badge:* `VI PHẪU THẦN KINH` · *mood mặc định:* `nghiem_trang_gia`

**Part 0** → `audio/vs/scene03_p0.wav` (648 ký tự) · mood `nghiem_trang_gia`

```text
Sau khi nạn nhân đã bị trói chặt hai chân trước trong trạng thái bất động tạm thời, ca phẫu thuật sọ não rùng rợn nhất hành tinh chính thức bắt đầu! Thưa Hội đồng xét xử, hãy nhìn vào màn hình phóng đại vi phẫu: Bác sĩ phẫu thuật thần kinh từ tốn buông ngực gián ra, bò lên phần đầu của nạn nhân. Gã dùng hàm giữ chặt mép sọ, rồi từ từ chọc chiếc kim tiêm dài luồn qua lớp màng mềm giữa đầu và cổ. Đây không phải là một cú đâm mù quáng! Các nghiên cứu của giáo sư Libersat tại Đại học Ben-Gurion đã phát hiện ra rằng: Trên đầu mũi kim của ong có chứa hàng loạt thụ thể hóa học và cơ học cực nhạy, đóng vai trò như một hệ thống định vị GPS sinh học!
```
**Part 1** → `audio/vs/scene03_p1.wav` (924 ký tự) · mood `tram_bi_an`

```text
Mũi kim vi phẫu luồn sâu vào trong hộp sọ, dò dẫm từng milimét mô não và chạm thẳng vào trung khu điều khiển vận động tối cao: Đó là hạch não dưới thực quản của gián! Tại đây, gã bơm vào một liều cocktail hóa chất độc quyền gồm dopamine và các hợp chất ức chế thụ thể octopamine. Hợp chất này có tác dụng gì? Nó không hề giết chết tế bào não, cũng không làm gián bị tê liệt toàn thân! Ngược lại, tim gián vẫn đập, cơ bắp vẫn hoạt động bình thường! Nhưng thụ thể octopamine chính là chiếc công tắc khởi động ý chí sinh tồn, động lực chạy trốn và phản xạ sợ hãi của loài gián. Khi công tắc này bị dập tắt, con gián hoàn toàn mất đi ý chí tự do! [surprise-oh] Nếu bạn thả con gián này vào một xô nước, phản xạ bản năng vẫn khiến nó bơi nổi; nhưng nếu để nó trên cạn, nó sẽ chỉ đứng đực mặt ra đó, ngoan ngoãn đến mức ai làm gì cũng cam chịu! Một xác sống Zombie thực thụ đã ra đời dưới ngòi kim của Bác sĩ phẫu thuật thần kinh!
```
**Part 2** → `audio/vs/scene03_p2.wav` (544 ký tự) · mood `hao_hung`

```text
Điều kỳ dị hơn nữa là ngay sau khi mũi kim rút ra khỏi não, lượng dopamine đậm đặc trong nọc độc bắt đầu phát huy tác dụng tâm lý bất ngờ: Con gián không hề bỏ chạy hay quằn quại đau đớn, mà đứng yên tại chỗ và bắt đầu chải chuốt cơ thể một cách cuồng loạn suốt ba mươi phút liên tục! Nó dùng chân lau chùi mắt, vuốt ve râu và làm sạch cơ thể như một kẻ mắc chứng ám ảnh cưỡng chế! Trong lúc nạn nhân đang mải mê làm đẹp trong vô thức, Bác sĩ phẫu thuật thần kinh thong dong bay đi tìm một chiếc hốc đất lý tưởng để chuẩn bị căn phòng giam giữ!
```

### scene04 — MÀN DẮT GIÁN NHƯ THÚ CƯNG ĐI VÀO NẤM MỒ NGẦM
*Thẻ chương:* CẮT TỈA CẶP ĂNG-TEN VÀ DẮT XÁC SỐNG TỰ BƯỚC ĐI

*Badge:* `HIỆN TRƯỜNG DẮT MỒI` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene04_p0.wav` (548 ký tự) · mood `hao_hung`

```text
Sau ca phẫu thuật não kéo dài chưa đầy ba mươi phút, tác dụng của mũi tiêm số một tan biến, hai chân trước của con gián cử động trở lại bình thường. Nhưng hỡi ôi, nạn nhân giờ đây chỉ còn là một cái xác không hồn biết thở! Bác sĩ phẫu thuật thần kinh lúc này tiến hành bước xử lý tiếp theo khiến các điều tra viên phải há hốc mồm: Thể trọng con gián quá nặng, gấp sáu lần ong, nên ong hoàn toàn không thể tha hay vác nạn nhân bay trên không trung. Thay vì tốn sức kéo lê con mồi khổng lồ, gã lại bắt con mồi phải tự đi bằng chính đôi chân của mình!
```
**Part 1** → `audio/vs/scene04_p1.wav` (98 ký tự) · 🎭 cameo `tham_phan`

```text
Con gián to xác tự bước đi theo sau kẻ thù sao?! Thật hoang đường, chuyện này diễn ra như thế nào?
```
**Part 2** → `audio/vs/scene04_p2.wav` (680 ký tự) · mood `don_dap`

```text
[surprise-wa] Đúng như Thẩm phán vừa kinh ngạc thốt lên! Bác sĩ phẫu thuật thần kinh tiến lại gần, dùng cặp hàm sắc lẻm cắt tỉa bớt một nửa chiều dài hai sợi râu dài của con gián. Gã ghé miệng vào vết cắt uống từng giọt dịch máu hemolymph tứa ra để nạp lại năng lượng calo sau ca mổ căng thẳng. Sau đó, gã ngậm chặt lấy phần gốc râu còn lại của con gián như cầm một sợi dây dắt chó đi dạo! [laughter] Gã lùi từng bước về phía trước, và con gián to xác răm rắp bước theo từng bước chân của kẻ đã cướp não mình! Nạn nhân thong thả bước xuống căn hầm mộ tối tăm do ong đào sẵn dưới lòng đất, ngoan ngoãn ngồi im trong góc tối mà không có lấy một chút ý định chạy trốn hay phản kháng!
```
**Part 3** → `audio/vs/scene04_p3.wav` (601 ký tự) · mood `nghiem_trang_gia`

```text
Nhà tự nhiên học Francis Williams khi quan sát hiện tượng này tại quần đảo Hawaii vào năm một ngàn chín trăm bốn mươi hai đã từng miêu tả: Đây là cảnh tượng siêu thực bậc nhất trong rừng nhiệt đới! Một chú ong nhỏ bằng hạt đậu ngọc bích, dùng hàm ngậm râu con gián khổng lồ dắt đi băng qua những đám lá khô mục nát. Con gián bước đi thảnh thơi tựa như đang dạo phố cùng bạn thân, thỉnh thoảng còn dừng lại đợi chú ong vượt qua chướng ngại vật! Toàn bộ hệ thống cơ bắp vận động của con gián vẫn hoạt động một trăm phần trăm công suất, nhưng bộ máy ý chí và bản năng tự vệ đã bị kẻ thù cầm tù vĩnh viễn!
```

### scene05 — CHIẾN LƯỢC BẢO QUẢN THỊT TƯƠI SỐNG ĐỈNH CAO CỦA ẤU TRÙNG
*Thẻ chương:* BẢO QUẢN THỰC PHẨM SỐNG SUỐT 8 NGÀY KHÔNG ÔI THIU

*Badge:* `TỦ LẠNH SINH HỌC` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene05_p0.wav` (495 ký tự) · mood `don_dap`

```text
Thưa Hội đồng xét xử, chương man rợ và tinh vi nhất của bản cáo trạng nằm ở căn hầm mộ này! Sau khi dắt được con gián vào hang, Bác sĩ phẫu thuật thần kinh không hề cắn chết nạn nhân. Gã đẻ cẩn thận đúng một quả trứng duy nhất dính chặt vào gốc chân giữa của gián. Sau đó, ong mẹ chui ra khỏi hang, cần mẫn nhặt từng viên sỏi nhỏ, mẩu lá cây và đất vụn lấp kín miệng hang lại để ngăn chặn mọi kẻ xâm nhập từ bên ngoài. Con gián bị nhốt kín bên trong bóng tối vĩnh cửu cùng với quả trứng tử thần!
```
**Part 1** → `audio/vs/scene05_p1.wav` (888 ký tự) · mood `nghiem_trang_gia`

```text
Sau hai đến ba ngày, quả trứng nở thành một ấu trùng ong nhỏ xíu màu trắng. Ấu trùng dùng hàm cắn thủng một lỗ nhỏ trên lớp vỏ gián để hút dịch cơ thể. Khi lớn hơn, nó chui tọt vào bên trong ổ bụng của gián và bắt đầu bữa tiệc sinh tồn! Hãy lắng nghe nguyên tắc y khoa của ấu trùng: Nếu nó cắn đứt tim hoặc hệ thần kinh trung ương, con gián sẽ chết ngay lập tức; và trong môi trường nhiệt đới nóng ẩm, cái xác sẽ thối rữa và bốc mùi chỉ sau hai mươi bốn giờ, đầu độc chết chính ấu trùng! Do đó, ấu trùng ong được lập trình bản năng chuẩn xác: Nó ăn toàn bộ lớp mỡ thừa và các cơ quan không thiết yếu trước, tuyệt đối tránh xa tim và mạch máu! Con gián vẫn sống, tim vẫn đập suốt tám đến mười ngày liên tục như một chiếc tủ lạnh sinh học bảo quản thịt tươi hoàn hảo! Cho đến khi ăn sạch mọi thứ, ấu trùng mới cắn đứt tim, đan kén nhộng bên trong xác gián khô rỗng rồi lột xác bay ra ngoài!
```
**Part 2** → `audio/vs/scene05_p2.wav` (554 ký tự) · mood `hao_hung`

```text
Chưa dừng lại ở đó, các nhà sinh vật học còn phát hiện ấu trùng ong tiết ra một loại hợp chất kháng sinh cực mạnh từ tuyến nước bọt. Hợp chất này phủ kín toàn bộ khoang bụng của gián, tiêu diệt sạch sẽ mọi vi khuẩn phân hủy và nấm mốc gây hại trong lòng đất ẩm ướt! Nói cách khác, con gián không những bị biến thành thức ăn tươi sống, mà còn được ấu trùng tắm rửa khử trùng đạt chuẩn phòng phẫu thuật vô khuẩn tuyệt đối! Một quy trình bảo quản thực phẩm đỉnh cao mà ngay cả các tập đoàn công nghệ thực phẩm hàng đầu thế giới cũng phải trầm trồ thán phục!
```

### scene06 — KHÉP LẠI VỤ ÁN THAO TÚNG NÃO BỘ KỲ VĨ CỦA TỰ NHIÊN
*Thẻ chương:* BẢN ÁN TIẾN HÓA VÀ LỜI GIẢI MÃ BÍ ẨN HỒ SƠ 44

*Badge:* `BẢN ÁN CUỐI CÙNG` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene06_p0.wav` (549 ký tự) · mood `am_ap`

```text
Phiên tòa xét xử hồ sơ số bốn mươi ba chính thức tuyên bố kết luận: Dưới lăng kính đạo đức con người, hành vi của Ong Bắp Cày Ngọc có thể khiến chúng ta rùng mình ớn lạnh. Nhưng dưới góc nhìn của khoa học tiến hóa, đây là một tuyệt tác cơ sinh học và hóa dược đỉnh cao! Tự nhiên không có thiện hay ác, chỉ có sự thích nghi tột cùng để sinh tồn. Bác sĩ phẫu thuật thần kinh đã chứng minh rằng: Một sinh vật nhỏ bé hoàn toàn có thể khuất phục những kẻ khổng lồ gấp nhiều lần bằng sự chính xác tuyệt đối, chiến lược bài bản và trí tuệ vi phẫu đỉnh cao!
```
**Part 1** → `audio/vs/scene06_p1.wav` (273 ký tự) · mood `hao_hung`

```text
Nếu trong cuộc sống bạn gặp phải những thử thách khổng lồ tưởng chừng không thể vượt qua, đừng vội dùng sức mạnh thô bạo để húc đầu vào đá: Hãy học tập sự sắc bén của ong bắp cày ngọc, tìm ra đúng mắt xích trọng tâm và giải quyết vấn đề bằng sự điềm tĩnh và chính xác nhất!
```
**Part 2** → `audio/vs/scene06_p2.wav` (183 ký tự) · mood `hao_hung`

```text
Nếu được sở hữu một kỹ năng của loài ong này, bạn muốn sở hữu chiếc áo ngọc bích lấp lánh hay khả năng vi phẫu thao túng tâm trí? Hãy để lại bình luận tranh luận của bạn bên dưới nhé!
```
**Part 3** → `audio/vs/scene06_p3.wav` (313 ký tự) · mood `tram_bi_an`

```text
Còn bây giờ, hãy chuẩn bị bước vào hồ sơ bệnh án số bốn mươi tư! Một gã khổng lồ nặng tới hai tấn trôi dạt giữa đại dương, cơ thể dị hợm như chỉ có một cái đầu cụt ngủn biết bơi, ngơ ngác đến mức bị hải cẩu bơi lại cắn đứt từng mảng vây vẫn nằm phơi nắng nhìn trời! Bạn có biết gã khổng lồ vô tri này là ai không?
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Bạn có tin một con ong bé tí chỉ bằng ngón tay lại có thể biến một con gián to gấp sáu lần thành một xác sống Zombie ngoan ngoãn nghe lời răm rắp? Đây là Ong Bắp Cày Ngọc, sát thủ mang biệt danh Bác sĩ phẫu thuật thần kinh! Thay vì giết con mồi, gã tung ra hai phát châm kim độc quyền: Phát thứ nhất châm thẳng vào ngực làm tê liệt hai chân trước của gián trong hai đến ba phút. Sau đó, gã chọc mũi kim xuyên qua sọ gián, tìm chính xác hạch não dưới thực quản để bơm độc tố ức chế ý chí sinh tồn! Hậu quả là con gián vẫn sống, tim vẫn đập, nhưng mất sạch một trăm phần trăm phản xạ sợ hãi và ý chí chạy trốn! Ong chỉ việc cắn bớt râu, ngậm gốc râu dắt con gián tự bước chân vào hang ngầm như dắt thú cưng đi dạo! Một kỳ tích vi phẫu não bộ thao túng tâm lý đỉnh cao và rùng rợn nhất thế giới côn trùng!
```

**Whisper prompt:** `Ong Bắp Cày Ngọc, Ampulex compressa, Bác sĩ phẫu thuật thần kinh, Sát thủ ngọc bích, gián Zombie, hạch não, sub-esophageal ganglion, octopamine, dopamine, 2-3 phút, 8-10 ngày, Thẩm phán`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| bốn mươi ba | 43 |
| Bốn mươi ba | 43 |
| Tập bốn mươi ba | Tập 43 |
| bốn mươi hai | 42 |
| Bốn mươi hai | 42 |
| bốn mươi tư | 44 |
| Bốn mươi tư | 44 |
| bốn mươi bốn | 44 |
| Bốn mươi bốn | 44 |
| số bốn mươi ba | số 43 |
| Số bốn mươi ba | Số 43 |
| hai mươi mi-li-mét | 20mm |
| Hai mươi mi-li-mét | 20mm |
| hai mi-li-mét | 2mm |
| Hai mi-li-mét | 2mm |
| hai đến ba phút | 2-3 phút |
| Hai đến ba phút | 2-3 phút |
| hai đến ba ngày | 2-3 ngày |
| Hai đến ba ngày | 2-3 ngày |
| tám đến mười ngày | 8-10 ngày |
| Tám đến mười ngày | 8-10 ngày |
| hai mươi bốn giờ | 24 giờ |
| Hai mươi bốn giờ | 24 giờ |
| hai tấn | 2 tấn |
| Hai tấn | 2 tấn |
| sáu lần | 6 lần |
| Sáu lần | 6 lần |
| hai tuần | 2 tuần |
| Hai tuần | 2 tuần |
| ba mươi phút | 30 phút |
| Ba mươi phút | 30 phút |
| một quả trứng | 1 quả trứng |
| Một quả trứng | 1 quả trứng |
| một trăm phần trăm | 100% |
| Một trăm phần trăm | 100% |
| tám mươi phần trăm | 80% |
| Tám mươi phần trăm | 80% |
| sáu mươi phần trăm | 60% |
| Sáu mươi phần trăm | 60% |
| hai phát | 2 phát |
| Hai phát | 2 phát |
| ba trăm triệu năm | 300 triệu năm |
| Ba trăm triệu năm | 300 triệu năm |
| một ngàn | 1.000 |
| Một ngàn | 1.000 |
| năm một ngàn chín trăm bốn mươi hai | năm 1942 |
| Năm một ngàn chín trăm bốn mươi hai | Năm 1942 |
| một mét rưỡi | 1.5 mét |
| Một mét rưỡi | 1.5 mét |
| phát thứ nhất | phát 1 |
| phát thứ hai | phát 2 |
| Phát thứ nhất | Phát 1 |
| Phát thứ hai | Phát 2 |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · VỤ ÁN THAO TÚNG TÂM TRÍ CHẤN ĐỘNG GIỚI CÔN TRÙNG · 99.5s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:11.9 (11.9s) | L01 | Trật tự toàn thể phòng xử án hình sự sinh học tối cao! Đại diện Viện Kiểm Sát Tự Nhiên hôm nay chính thức công bố bản cáo trạng điều tra đặc biệt về một vụ án xâm phạm thân thể và thao túng tâm lý tàn bạo bậc nhất trong lịch sử tiến hóa động vật! |  | Phòng xử án hình sự sinh học tối cao: Bàn công tố viên gỗ gụ trang nghiêm phủ đầy các hồ sơ vụ án gắn nhãn TỐI MẬT; KHÔNG có chú ong bắp cày ngọc trong cảnh này; BÊN TRÁI thẩm phán cú mèo uy nghiêm đội tóc giả quan tòa màu trắng, mặc áo thụng đen, tay cầm búa gõ đang ngồi trên bục thẩm phán uy nghiêm. |
| b02 | 00:11.9–00:23.6 (11.7s) | L02 | Không dùng sức mạnh cơ bắp áp đảo, không xé xác nạn nhân tại chỗ, kẻ thủ ác này khoác lên mình một tấm áo choàng ngọc bích lộng lẫy kiêu sa nhưng lại sở hữu thủ đoạn giải phẫu thần kinh lạnh lùng đến rợn gáy! Gã không giết chết con mồi, mà |  | Ánh sáng spotlight chiếu rọi: Một cái bóng đen bí ẩn khoác áo choàng ngọc bích lấp lánh cầm chiếc kim tiêm phát sáng; phía đối diện là bóng dáng một con gián to lớn đang ngoan ngoãn cúi đầu bước đi như xác sống; KHÔNG có chú ong bắp cày ngọc trong cảnh này. |
| b03 | 00:23.6–00:37.2 (13.7s) | L03b | biến một chiến binh gián khỏe mạnh, nhanh nhẹn bậc nhất hành tinh thành một xác sống Zombie ngoan ngoãn tự bước chân vào nấm mồ chôn sống! Trật tự phiên tòa! Thẩm phán yêu cầu công tố viên công bố danh tính bị cáo và vạch trần thủ đoạn gây án ngay lập tức! |  | Bảng mạch giải phẫu số mô tả thao tác kiểm soát xung thần kinh vận động. |
| b04 | 00:37.2–00:47.2 (10.0s) | L03 | Thưa Hội đồng xét xử! Bị cáo mang mã số 43 của chúng ta có tên khoa học là Ampulex compressa, thuộc bộ cánh màng, hay còn được gọi bằng cái tên hoa mỹ là Ong Bắp Cày Ngọc! | **SỐ 43** · hồ sơ hình sự · R/360 · [0.75, 0.5] | Bục bị cáo: chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) đứng trên bục gỗ, lớp vỏ ngọc bích xanh biếc lấp lánh kiêu sa, một tay chống nạnh, một tay xoay chiếc kim ti |
| b05 | 00:47.2–00:54.0 (6.8s) | L04 | Nhưng trong giới giang hồ tự nhiên, nạn nhân và các nhà khoa học gọi gã bằng một biệt danh rùng rợn: Bác sĩ phẫu thuật thần kinh! |  | Tấm thẻ bảng câu đố vui hoạt hình quốc tế: Ảnh chụp chân dung chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) đeo kính lúp vi phẫu, đóng dấu đỏ tươi BÁC SĨ PHẪU THUẬT T |
| b06 | 00:54.0–01:03.0 (8.9s) | L05 | Chiều dài cơ thể của gã chỉ khoảng 20mm, khoác lớp vỏ chitin lấp lánh ánh kim màu xanh ngọc lục bảo và lam biếc tuyệt đẹp tựa như một viên đá quý di động! | **20 MM** · chiều dài cơ thể · R/380 · [0.5, 0.5] | Thước đo vi phẫu: chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) đứng cạnh chiếc thước kẹp cơ khí hiển thị đúng 20mm; lớp vỏ cánh phản chiếu ánh kim ngũ sắc như kim lo |
| b07 | 01:03.0–01:13.8 (10.8s) | L06b | Nhưng đừng để vẻ ngoài kiều diễm ấy đánh lừa, bởi vì chiếc đuôi của gã cất giấu một chiếc kim tiêm vi phẫu tinh xảo đến mức khiến mọi giáo sư phẫu thuật sọ não loài người cũng phải ngả mũ bái phục! |  | Sơ đồ hiển vi đầu kim châm và các cảm biến cơ học siêu nhạy. |
| b08 | 01:13.8–01:27.2 (13.5s) | L06 | Trước khi đi vào hiện trường gây án, Viện Kiểm Sát xin nhấn mạnh rằng: Nạn nhân của Bác sĩ phẫu thuật thần kinh không phải là những sâu bọ mềm yếu. Nạn nhân là loài gián nhà Mỹ Periplaneta americana, một loài sinh vật sống dai khét tiếng đã tồn tại hơn 300 triệu năm trên Trái Đất! |  | Hồ sơ đối tượng nạn nhân: BÊN TRÁI ảnh chụp chú gián to gấp sáu lần ong, màu nâu cánh gián bóng lưỡng, mắt xoắn ốc đờ đẫn ngoan ngoãn như Zombie, râu bị cắt ngắn một nửa cơ bắp cuồn cuộn với các thông số tốc độ chạy và sức bền cực khủng; BÊN PHẢI thẩm phán cú mèo uy nghiêm đội tóc giả quan tòa màu trắng, mặc áo thụng đen, tay cầm búa gõ đang cầm kính lúp săm soi kinh ngạc. |
| b09 | 01:27.2–01:33.7 (6.5s) | L07 | Một loài côn trùng có thể sống sót sau bom nguyên tử, chạy trốn với vận tốc 1.5 mét mỗi giây, và có thể sống cả tuần mà không cần đầu! | **1.5 M/S** · tốc độ tẩu thoát · L/360 · [0.25, 0.5] | Biểu đồ sinh tồn siêu đẳng: Chú gián đang cười khẩy bước qua đám lửa và tia phóng xạ hạt nhân; đồng hồ đo tốc độ chỉ vọt lên 1.5 mét mỗi giây; KHÔNG có chú ong bắp cày ngọc trong cảnh này. |
| b10 | 01:33.7–01:36.0 (2.4s) | L08 | Nhưng khi đối đầu với mũi kim của Bác sĩ phẫu thuật thần |  | Khoảnh khắc đối đầu định mệnh: Chú gián khổng lồ giơ 6 chiếc chân gai góc nhọn hoắt nhưng run rẩy toát mồ hôi hột; phía trên không trung, chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng ph |
| b11 | 01:36.0–01:39.5 (3.4s) | L09 | kinh, toàn bộ sức mạnh kiên cường ấy biến thành con số không tròn trĩnh! |  | Biểu tượng sụp đổ: Chiếc khiên bảo vệ bằng chitin của loài gián bị mũi kim laser xuyên thủng, vỡ vụn thành các mảnh kính văng tung tóe; chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha  |

### scene02 · MŨI TIÊM SỐ 1 KHÓA CHẶT KHỚP NGỰC NẠN NHÂN · 98.0s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.9 (9.9s) | L10 | Hãy lật lại từng trang hồ sơ khám nghiệm hiện trường vụ tấn công! Nạn nhân được lựa chọn ở đây là loài gián nhà nhiệt đới. Về tương quan thể lực, con gián to lớn và nặng gấp 6 lần Bác sĩ phẫu thuật thần kinh! | **GẤP 6 LẦN** · thể trọng nạn nhân · R/360 · [0.75, 0.5] | Bàn mổ xẻ vụ án số 1: Sơ đồ tương quan lực lượng; BÊN TRÁI chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) nhỏ nhắn như hạt đậu; BÊN PHẢI chú gián to gấp sáu lần ong, m |
| b02 | 00:09.9–00:17.7 (7.9s) | L11 | Gián sở hữu hệ thống lông cảm biến siêu nhạy ở đuôi, phát hiện được cả những dao động không khí nhỏ nhất và có thể tăng tốc tẩu thoát chỉ trong vòng vài phần nghìn giây. |  | Cận cảnh lông cảm biến đuôi gián: Sóng âm dao động không khí phát sáng radar quanh hai chiếc râu đuôi cerci; chú gián to gấp sáu lần ong, màu nâu cánh gián bóng lưỡng, mắt xoắn ốc đờ đẫn ngoan ngoãn như Zombie, râu bị cắt ngắn một nửa vểnh tai sẵn sàng phóng đi như tên bắn; KHÔNG có chú ong bắp cày ngọc trong cảnh này. |
| b03 | 00:17.7–00:30.9 (13.1s) | L12 | Nếu lao vào một cuộc đấu vật tay đôi trực diện, chú ong nhỏ bé chắc chắn sẽ bị con gián khổng lồ đá văng hoặc nghiền nát dưới những chiếc chân gai nhọn hoắt! Vậy bị cáo đã làm cách nào để khuất phục một gã khổng lồ to xác gấp 6 lần mình? |  | Sàn đấu võ đài côn trùng: Con gián tung chân sau to khỏe đá văng một cành cây gãy đôi; cát bụi bay mù mịt; KHÔNG có chú ong bắp cày ngọc trong cảnh này. |
| b04 | 00:30.9–00:37.1 (6.3s) | L13 | Đây chính là điểm khởi đầu của kế hoạch gây án bài bản đến kinh ngạc! Bác sĩ phẫu thuật thần kinh không hề chích bừa bãi! |  | Chiến thuật phục kích tàng hình: chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) ẩn mình trên kẽ lá cây, đôi mắt qua kính lúp vi phẫu lấp lánh tính toán góc rơi và tọa  |
| b05 | 00:37.1–00:43.0 (5.9s) | L14 | Gã phục kích từ trên cao, lao xuống như một tia chớp kim loại và dùng cặp hàm thép kẹp chặt lấy lưng con gián. |  | Pha không kích ngoạn mục: chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) lao vút xuống cắm phập cặp hàm thép sắc lẹm vào lưng gián, khóa chặt điểm mù sau gáy khiến nạn |
| b06 | 00:43.0–00:52.0 (8.9s) | L15 | Ngay trong tích tắc đối phương còn đang bàng hoàng, chiếc kim tiêm từ đuôi ong uốn cong, đâm một phát châm chuẩn xác đến từng mi-li-mét vào hạch thần kinh ngực trước của gián! |  | Đòn châm kim sấm sét: Đuôi của chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) uốn cong chữ C, chiếc kim tiêm bạc đâm phập chính xác vào đốt ngực trước của chú gián to  |
| b07 | 00:52.0–01:01.5 (9.6s) | L16 | Độc tố của phát 1 chứa hàm lượng lớn chất ức chế dẫn truyền GABA, ngay lập tức làm tê liệt hoàn toàn hai chiếc chân trước của nạn nhân trong vòng 2-3 phút! | **2-3 PHÚT** · liệt chân trước · L/360 · [0.25, 0.5] | Sơ đồ giải phẫu hóa sinh: Độc tố chứa GABA khóa chặt các kênh dẫn truyền thần kinh vận động; hai chiếc chân trước của chú gián to gấp sáu lần ong, màu nâu cánh gián bóng lưỡng, mắt xoắn ốc đờ đẫn ngoan ngoãn như Zombie, râu bị cắt ngắn một nửa rũ rượi xụi lơ; đồng hồ cát đếm ngược 2-3 phút. |
| b08 | 01:01.5–01:10.6 (9.1s) | L17 | Con gián dù vẫn còn tỉnh táo nhưng hai chân trước đã bị liệt hoàn toàn, không thể cựa quậy hay xoay người bỏ chạy! Chiếc áo giáp phản xạ của gián chính thức bị phong tỏa! |  | Tình trạng bất động dở khóc dở cười: chú gián to gấp sáu lần ong, màu nâu cánh gián bóng lưỡng, mắt xoắn ốc đờ đẫn ngoan ngoãn như Zombie, râu bị cắt ngắn một nửa mắt tròn xoe kinh ngạc, hai chân trước mềm như cọng bún không thể chống đất, toàn thân đổ sụp về phía trước bất lực. |
| b09 | 01:10.6–01:17.8 (7.2s) | L18 | Nhóm nghiên cứu của giáo sư Kenneth Catania tại Đại học Vanderbilt đã sử dụng máy quay tốc độ cao 1.000 khung hình mỗi giây để giải mã cuộc đụng độ này: | **1.000 FPS** · máy quay siêu chậm · R/360 · [0.75, 0.5] | Phòng nghiên cứu sinh học đại học: Màn hình máy quay siêu chậm 1.000 khung hình/giây ghi lại khoảnh khắc gián tung cú đá hậu karate nhưng hụt trong gang tấc. |
| b10 | 01:17.8–01:26.0 (8.1s) | L19b | Khi gián phát hiện bị ong tập kích, nó thường vung chân sau tung ra những cú đá hậu karate cực mạnh nhằm hất văng kẻ thù. Nhưng Bác sĩ phẫu thuật thần kinh cực kỳ ranh mãnh! |  | Biểu đồ động lực học so sánh phản xạ thần kinh của gián và ong. |
| b11 | 01:26.0–01:32.1 (6.1s) | L19 | Gã lượn vòng từ góc mù, túm chặt lấy mép khiên ngực bảo vệ của gián, biến chính điểm tựa của đối phương thành thế gọng kìm bất khả kháng |  | Khóa khớp gọng kìm: chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) dùng chân bám chặt mép khiên ngực của gián như tay đua cưỡi bò tót; gián giãy giụa vô vọng không thể |
| b12 | 01:32.1–01:38.0 (5.9s) | L20 | cự! Cú châm kim số một diễn ra chỉ trong vòng nửa giây, nhanh như một mũi tên tẩm thuốc mê bắn trúng tim đen con mồi! |  | Đồng hồ bấm giờ nửa giây: Chiếc kim tiêm rút ra trong 0.5s; mũi tiêm để lại một chấm sáng màu xanh ngọc bích trên ngực gián; cánh cửa sổ thoát hiểm của gián chính thức sập lại. |

### scene03 · KỸ THUẬT CHÂM KIM NÃO BỘ TƯỚC ĐOẠT Ý CHÍ TỰ DO · 102.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:13.8 (13.8s) | L21 | Sau khi nạn nhân đã bị trói chặt hai chân trước trong trạng thái bất động tạm thời, ca phẫu thuật sọ não rùng rợn nhất hành tinh chính thức bắt đầu! Thưa Hội đồng xét xử, hãy nhìn vào màn hình phóng đại vi phẫu: Bác sĩ phẫu thuật thần kinh từ tốn buông ngực gián ra, bò lên phần đầu của nạn nhân. |  | Phòng mổ thần kinh tương lai: Màn hình quét sóng não điện não đồ EEG hiển thị hộp sọ gián; chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) đeo găng tay phẫu thuật đứng  |
| b02 | 00:13.8–00:20.4 (6.6s) | L22 | Gã dùng hàm giữ chặt mép sọ, rồi từ từ chọc chiếc kim tiêm dài luồn qua lớp màng mềm giữa đầu và cổ. Đây không phải là một cú đâm mù quáng! |  | Khoảnh khắc mở đường luồn kim: chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) giữ chặt mép cổ gián, chiếc kim tiêm siêu nhỏ luồn nhẹ qua lớp màng cổ mềm mại; ánh sáng  |
| b03 | 00:20.4–00:29.9 (9.5s) | L23 | Các nghiên cứu của giáo sư Libersat tại Đại học Ben-Gurion đã phát hiện ra rằng: Trên đầu mũi kim của ong có chứa hàng loạt thụ thể hóa học và cơ học cực nhạy, đóng vai trò như một hệ thống định vị GPS sinh học! |  | Đầu kim tiêm định vị GPS: Phóng to cực đại đầu ngòi châm của chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái); hàng trăm thụ thể cảm giác li ti phát sáng như ăng-ten rad |
| b04 | 00:29.9–00:38.1 (8.2s) | L24 | Mũi kim vi phẫu luồn sâu vào trong hộp sọ, dò dẫm từng milimét mô não và chạm thẳng vào trung khu điều khiển vận động tối cao: Đó là hạch não dưới thực quản của gián! |  | Bản đồ hạch não gián: Mũi kim chạm trúng hạch não dưới thực quản sub-esophageal ganglion; điểm tiếp xúc phát nổ tia sáng vàng kim rực rỡ; KHÔNG có chú ong bắp cày ngọc trong cảnh này. |
| b05 | 00:38.1–00:51.8 (13.6s) | L25 | Tại đây, gã bơm vào một liều cocktail hóa chất độc quyền gồm dopamine và các hợp chất ức chế thụ thể octopamine. Hợp chất này có tác dụng gì? Nó không hề giết chết tế bào não, cũng không làm gián bị tê liệt toàn thân! Ngược lại, tim gián vẫn đập, cơ bắp vẫn hoạt động bình thường! |  | Cocktail hóa chất thần kinh: Bình thuốc tiêm phát sáng chứa phân tử dopamine và chất chẹn octopamine tuôn trào vào synap thần kinh não gián. |
| b06 | 00:51.8–01:01.5 (9.8s) | L26 | Nhưng thụ thể octopamine chính là chiếc công tắc khởi động ý chí sinh tồn, động lực chạy trốn và phản xạ sợ hãi của loài gián. Khi công tắc này bị dập tắt, con gián hoàn toàn mất đi ý chí tự do! |  | Công tắc ý chí bị dập tắt: Bức tranh ẩn dụ chiếc cầu dao điện dán nhãn Ý CHÍ SINH TỒN bị một ngón tay gạt phắt xuống vị trí TẮT; bóng tối bao trùm đôi mắt gián; KHÔNG có chú ong bắp cày ngọc trong cảnh này. |
| b07 | 01:01.5–01:10.6 (9.1s) | L27 | Nếu bạn thả con gián này vào một xô nước, phản xạ bản năng vẫn khiến nó bơi nổi; nhưng nếu để nó trên cạn, nó sẽ chỉ đứng đực mặt ra đó, ngoan ngoãn đến mức ai làm gì cũng cam chịu! |  | Thí nghiệm đối chứng kỳ lạ: BÊN TRÁI gián rơi xuống xô nước vẫn bơi nổi như thường; BÊN PHẢI gián trên cạn đứng trơ như khúc gỗ mắt nhìn vô định; KHÔNG có chú ong bắp cày ngọc trong cảnh này. |
| b08 | 01:10.6–01:14.6 (4.0s) | L28 | Một xác sống Zombie thực thụ đã ra đời dưới ngòi kim của Bác sĩ phẫu thuật thần kinh! |  | Chân dung gián Zombie: chú gián to gấp sáu lần ong, màu nâu cánh gián bóng lưỡng, mắt xoắn ốc đờ đẫn ngoan ngoãn như Zombie, râu bị cắt ngắn một nửa hai mắt biến thành hình xoắn ốc thôi miên, khóe miệng chảy dãi ngây ngô; chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xan |
| b09 | 01:14.6–01:21.7 (7.1s) | L29 | Điều kỳ dị hơn nữa là ngay sau khi mũi kim rút ra khỏi não, lượng dopamine đậm đặc trong nọc độc bắt đầu phát huy tác dụng tâm lý bất ngờ: | **30 PHÚT** · chải chuốt vô thức · L/360 · [0.25, 0.5] | Cơn cuồng chải chuốt: chú gián to gấp sáu lần ong, màu nâu cánh gián bóng lưỡng, mắt xoắn ốc đờ đẫn ngoan ngoãn như Zombie, râu bị cắt ngắn một nửa đứng yên một chỗ, hai chân liên tục chùi mặt, vuốt râu, chải lông suốt 30 phút như bị ám ảnh cưỡng chế; đồng hồ cát quay tít. |
| b10 | 01:21.7–01:34.4 (12.7s) | L29b | Con gián không hề bỏ chạy hay quằn quại đau đớn, mà đứng yên tại chỗ và bắt đầu chải chuốt cơ thể một cách cuồng loạn suốt 30 phút liên tục! Nó dùng chân lau chùi mắt, vuốt ve râu và làm sạch cơ thể như một kẻ mắc chứng ám ảnh cưỡng chế! |  | Minh họa hiệu ứng sinh hóa phong tỏa ý chí tự vệ. |
| b11 | 01:34.4–01:42.9 (8.5s) | L30 | Trong lúc nạn nhân đang mải mê làm đẹp trong vô thức, Bác sĩ phẫu thuật thần kinh thong dong bay đi tìm một chiếc hốc đất lý tưởng để chuẩn bị căn phòng giam giữ! |  | Thảnh thơi chuẩn bị hầm ngục: chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) bay lượn trên đám rễ cây mục, dùng chân bới đất đào một chiếc hang ngầm nhỏ, miệng huýt sá |

### scene04 · MÀN DẮT GIÁN NHƯ THÚ CƯNG ĐI VÀO NẤM MỒ NGẦM · 93.5s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:13.0 (13.0s) | L31 | Sau ca phẫu thuật não kéo dài chưa đầy 30 phút, tác dụng của mũi tiêm số một tan biến, hai chân trước của con gián cử động trở lại bình thường. Nhưng hỡi ôi, nạn nhân giờ đây chỉ còn là một cái xác không hồn biết thở! Bác sĩ phẫu thuật |  | Hiện trường sau ca mổ: chú gián to gấp sáu lần ong, màu nâu cánh gián bóng lưỡng, mắt xoắn ốc đờ đẫn ngoan ngoãn như Zombie, râu bị cắt ngắn một nửa hai chân trước đã hết thuốc tê, đứng dậy cử động bình thường nhưng ánh mắt đờ đẫn hoàn toàn; chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng tron |
| b02 | 00:13.0–00:23.4 (10.4s) | L32 | thần kinh lúc này tiến hành bước xử lý tiếp theo khiến các điều tra viên phải há hốc mồm: Thể trọng con gián quá nặng, gấp 6 lần ong, nên ong hoàn toàn không thể tha hay vác nạn nhân bay trên không trung. |  | Bài toán vận tải nan giải: Chiếc cân đòn bẩy cho thấy gián nặng gấp 6 lần ong; chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) giơ một ngón tay lên trán mỉm cười lóe sá |
| b03 | 00:23.4–00:31.1 (7.7s) | L33 | Thay vì tốn sức kéo lê con mồi khổng lồ, gã lại bắt con mồi phải tự đi bằng chính đôi chân của mình! Con gián to xác tự bước đi theo sau kẻ thù |  | Màn cắt tỉa ăng-ten: chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) dùng cặp hàm kẹp đôi như chiếc kéo thợ may cắt phăng một nửa chiều dài hai sợi râu của chú gián to  |
| b04 | 00:31.1–00:42.7 (11.7s) | L33b | sao?! Thật hoang đường, chuyện này diễn ra như thế nào? Đúng như Thẩm phán vừa kinh ngạc thốt lên! Bác sĩ phẫu thuật thần kinh tiến lại gần, dùng cặp hàm sắc lẻm cắt tỉa bớt một nửa chiều dài hai sợi râu dài của con gián. |  | Hoạt cảnh điều khiển hành vi kỳ ảo giữa ong và gián. |
| b05 | 00:42.7–00:47.9 (5.1s) | L34 | Gã ghé miệng vào vết cắt uống từng giọt dịch máu hemolymph tứa ra để nạp lại năng lượng calo sau ca mổ căng thẳng. |  | Thưởng thức ly cocktail năng lượng: chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) ghé miệng uống giọt dịch hemolymph trong suốt rỉ ra từ cuống râu gián; biểu cảm khoa |
| b06 | 00:47.9–00:52.4 (4.5s) | L35 | Sau đó, gã ngậm chặt lấy phần gốc râu còn lại của con gián như cầm một sợi dây dắt chó đi dạo! |  | Màn dắt thú cưng đi dạo: chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) ngậm chặt gốc râu gián, hai tay cầm như cầm dây cương ngựa; chú gián to gấp sáu lần ong, màu nâ |
| b07 | 00:52.4–00:58.0 (5.6s) | L36 | Gã lùi từng bước về phía trước, và con gián to xác răm rắp bước theo từng bước chân của kẻ đã cướp não mình! |  | Đoàn diễu hành qua rừng lá khô: chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) đi lùi từng bước dẫn đường; chú gián to gấp sáu lần ong, màu nâu cánh gián bóng lưỡng, m |
| b08 | 00:58.0–01:05.7 (7.7s) | L37 | Nạn nhân thong thả bước xuống căn hầm mộ tối tăm do ong đào sẵn dưới lòng đất, ngoan ngoãn ngồi im trong góc tối mà không có lấy một chút ý định chạy trốn hay phản kháng! |  | Lối vào hầm mộ ngầm: chú gián to gấp sáu lần ong, màu nâu cánh gián bóng lưỡng, mắt xoắn ốc đờ đẫn ngoan ngoãn như Zombie, râu bị cắt ngắn một nửa ngoan ngoãn cúi đầu chui lọt qua miệng hang đất hẹp; chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim t |
| b09 | 01:05.7–01:20.6 (14.9s) | L38 | Nhà tự nhiên học Francis Williams khi quan sát hiện tượng này tại quần đảo Hawaii vào năm 1942 đã từng miêu tả: Đây là cảnh tượng siêu thực bậc nhất trong rừng nhiệt đới! Một chú ong nhỏ bằng hạt đậu ngọc bích, dùng hàm ngậm râu con gián khổng lồ dắt đi băng qua những đám lá khô mục nát. | **NĂM 1942** · ghi nhận tại Hawaii · L/360 · [0.25, 0.5] | Ghi chép lịch sử năm 1942: Cuốn sổ tay thám hiểm Hawaii với bức tranh vẽ mực tả thực cảnh chú ong ngọc bích dắt con gián khổng lồ đi dạo trên đảo nhiệt đới. |
| b10 | 01:20.6–01:25.9 (5.3s) | L39 | Con gián bước đi thảnh thơi tựa như đang dạo phố cùng bạn thân, thỉnh thoảng còn dừng lại đợi chú ong vượt qua chướng |  | Khoảnh khắc siêu thực: chú gián to gấp sáu lần ong, màu nâu cánh gián bóng lưỡng, mắt xoắn ốc đờ đẫn ngoan ngoãn như Zombie, râu bị cắt ngắn một nửa dừng chân chờ chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ las |
| b11 | 01:25.9–01:33.5 (7.6s) | L40 | ngại vật! Toàn bộ hệ thống cơ bắp vận động của con gián vẫn hoạt động 100% công suất, nhưng bộ máy ý chí và bản năng tự vệ đã bị kẻ thù cầm tù vĩnh viễn! | **100%** · cơ bắp bình thường · R/360 · [0.75, 0.5] | Cắt lớp buồng giam dưới lòng đất: chú gián to gấp sáu lần ong, màu nâu cánh gián bóng lưỡng, mắt xoắn ốc đờ đẫn ngoan ngoãn như Zombie, râu bị cắt ngắn một nửa ngồi im lìm trong góc tối của căn hầm ngầm, cơ bắp lành lặn nhưng đôi mắt hoàn toàn trống rỗng không hồn. |

### scene05 · CHIẾN LƯỢC BẢO QUẢN THỊT TƯƠI SỐNG ĐỈNH CAO CỦA ẤU TRÙNG · 93.0s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.3 (8.3s) | L41 | Thưa Hội đồng xét xử, chương man rợ và tinh vi nhất của bản cáo trạng nằm ở căn hầm mộ này! Sau khi dắt được con gián vào hang, Bác sĩ phẫu thuật thần kinh không hề cắn chết nạn nhân. |  | Căn hầm mộ sinh học: chú gián to gấp sáu lần ong, màu nâu cánh gián bóng lưỡng, mắt xoắn ốc đờ đẫn ngoan ngoãn như Zombie, râu bị cắt ngắn một nửa đứng im giữa lòng hang tối; chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng nh |
| b02 | 00:08.3–00:11.6 (3.2s) | L42 | Gã đẻ cẩn thận đúng 1 quả trứng duy nhất dính chặt vào gốc chân giữa của gián. | **1 TRỨNG** · dán vào chân gián · R/360 · [0.75, 0.5] | Quả trứng định mệnh: Cận cảnh một quả trứng ong nhỏ thuôn dài dán dính chắc chắn vào gốc chân giữa của chú gián to gấp sáu lần ong, màu nâu cánh gián bóng lưỡng, mắt xoắn ốc đờ đẫn ngoan ngoãn như Zombie, râu bị cắt ngắn một nửa; quả trứng phát sáng mờ ảo. |
| b03 | 00:11.6–00:23.0 (11.4s) | L43 | Sau đó, ong mẹ chui ra khỏi hang, cần mẫn nhặt từng viên sỏi nhỏ, mẩu lá cây và đất vụn lấp kín miệng hang lại để ngăn chặn mọi kẻ xâm nhập từ bên ngoài. Con gián bị nhốt kín bên trong bóng tối vĩnh cửu cùng với quả trứng tử thần! |  | Niêm phong cửa hầm: chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) tha từng viên sỏi nhỏ, mẩu lá cây vụn đắp kín miệng hang thành một bức tường đá kiên cố; không một s |
| b04 | 00:23.0–00:30.2 (7.2s) | L44 | Sau 2-3 ngày, quả trứng nở thành một ấu trùng ong nhỏ xíu màu trắng. Ấu trùng dùng hàm cắn thủng một lỗ nhỏ trên lớp vỏ gián để hút dịch cơ thể. | **2-3 NGÀY** · trứng nở ấu trùng · L/360 · [0.25, 0.5] | Ấu trùng chào đời: Quả trứng nứt vỏ, một chú ấu trùng sâu trắng ngọ nguậy thò đầu ra, dùng miệng cắn thủng lớp vỏ mềm chân gián để hút dịch; KHÔNG có chú ong bắp cày ngọc trong cảnh này. |
| b05 | 00:30.2–00:33.5 (3.4s) | L45 | Khi lớn hơn, nó chui tọt vào bên trong ổ bụng của gián và bắt đầu bữa tiệc sinh |  | Xâm nhập cơ thể: Ấu trùng chui tọt qua lỗ thủng vào bên trong ổ bụng của chú gián to gấp sáu lần ong, màu nâu cánh gián bóng lưỡng, mắt xoắn ốc đờ đẫn ngoan ngoãn như Zombie, râu bị cắt ngắn một nửa; con gián vẫn đứng im thở đều đặn như không hề hay biết; KHÔNG có chú ong bắp cày ngọc trong cảnh này. |
| b06 | 00:33.5–00:44.8 (11.3s) | L46 | tồn! Hãy lắng nghe nguyên tắc y khoa của ấu trùng: Nếu nó cắn đứt tim hoặc hệ thần kinh trung ương, con gián sẽ chết ngay lập tức; và trong môi trường nhiệt đới nóng ẩm, cái xác sẽ thối rữa và bốc mùi chỉ sau 24 giờ, đầu độc chết chính ấu | **24 GIỜ** · nguy cơ thối rữa · R/360 · [0.75, 0.5] | Nguy cơ thối rữa phân hủy: Chiếc đồng hồ 24 giờ đếm ngược biểu thị cái chết; nếu tim gián ngừng đập, vi khuẩn phân hủy sẽ đầu độc cả căn hầm; KHÔNG có chú ong bắp cày ngọc trong cảnh này. |
| b07 | 00:44.8–00:52.5 (7.7s) | L47 | trùng! Do đó, ấu trùng ong được lập trình bản năng chuẩn xác: Nó ăn toàn bộ lớp mỡ thừa và các cơ quan không thiết yếu trước, tuyệt đối tránh xa tim và mạch máu! |  | Sơ đồ ẩm thực chọn lọc: Ấu trùng gặm nhấm các mô mỡ thừa phát sáng xanh lục, né tránh hoàn toàn trái tim màu đỏ đang đập thình thịch và hệ dây thần kinh; KHÔNG có chú ong bắp cày ngọc trong cảnh này. |
| b08 | 00:52.5–00:57.6 (5.1s) | L48 | Con gián vẫn sống, tim vẫn đập suốt 8-10 ngày liên tục như một chiếc tủ lạnh sinh học bảo quản thịt tươi hoàn | **8-10 NGÀY** · thịt tươi sống · L/360 · [0.25, 0.5] | Tủ lạnh thịt tươi sống 10 ngày: Biểu tượng chiếc tủ lạnh sinh học bảo quản thực phẩm hoàn hảo suốt 8-10 ngày; nhịp tim gián hiển thị đều đặn trên màn hình theo dõi; KHÔNG có chú ong bắp cày ngọc trong cảnh này. |
| b09 | 00:57.6–01:03.9 (6.3s) | L49 | hảo! Cho đến khi ăn sạch mọi thứ, ấu trùng mới cắn đứt tim, đan kén nhộng bên trong xác gián khô rỗng rồi lột xác bay ra ngoài! |  | Chiếc kén nhộng bên trong vỏ gián: Ấu trùng đan một chiếc kén tơ nâu óng ánh chiếm trọn bên trong cái xác khô rỗng của gián; lớp vỏ gián bảo vệ kén khỏi kẻ thù; KHÔNG có chú ong bắp cày ngọc trong cảnh này. |
| b10 | 01:03.9–01:18.2 (14.4s) | L50 | Chưa dừng lại ở đó, các nhà sinh vật học còn phát hiện ấu trùng ong tiết ra một loại hợp chất kháng sinh cực mạnh từ tuyến nước bọt. Hợp chất này phủ kín toàn bộ khoang bụng của gián, tiêu diệt sạch sẽ mọi vi khuẩn phân hủy và nấm mốc gây hại trong lòng đất ẩm ướt! |  | Phòng mổ vô khuẩn ngầm: Các phân tử kháng sinh từ nước bọt ấu trùng phát sáng xanh neon quét sạch mọi bào tử nấm mốc và vi khuẩn trong khoang bụng gián; KHÔNG có chú ong bắp cày ngọc trong cảnh này. |
| b11 | 01:18.2–01:26.1 (7.9s) | L50b | Nói cách khác, con gián không những bị biến thành thức ăn tươi sống, mà còn được ấu trùng tắm rửa khử trùng đạt chuẩn phòng phẫu thuật vô khuẩn tuyệt đối! |  | Sơ đồ sinh học hiển vi về kháng sinh tự nhiên bảo vệ môi trường phát triển. |
| b12 | 01:26.1–01:33.0 (6.9s) | L51 | Một quy trình bảo quản thực phẩm đỉnh cao mà ngay cả các tập đoàn công nghệ thực phẩm hàng đầu thế giới cũng phải trầm trồ thán phục! |  | Sự tái sinh rực rỡ: Chiếc kén nứt ra, một chú ong bắp cày ngọc mới toanh với đôi cánh xanh biếc ánh kim chui ra khỏi xác gián, đục thủng lớp đất đá bay lên trời xanh. |

### scene06 · KHÉP LẠI VỤ ÁN THAO TÚNG NÃO BỘ KỲ VĨ CỦA TỰ NHIÊN · 66.0s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.2 (8.2s) | L52 | Phiên tòa xét xử hồ sơ số 43 chính thức tuyên bố kết luận: Dưới lăng kính đạo đức con người, hành vi của Ong Bắp Cày Ngọc có thể khiến chúng ta rùng mình ớn lạnh. |  | Bản án kết luận phiên tòa: Búa thẩm phán gõ vang trên bục gỗ; thẩm phán cú mèo uy nghiêm đội tóc giả quan tòa màu trắng, mặc áo thụng đen, tay cầm búa gõ tuyên án công nhận Ong Bắp Cày Ngọc là một kỳ tích vi phẫu tiến hóa; chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xa |
| b02 | 00:08.2–00:16.7 (8.6s) | L53 | Nhưng dưới góc nhìn của khoa học tiến hóa, đây là một tuyệt tác cơ sinh học và hóa dược đỉnh cao! Tự nhiên không có thiện hay ác, chỉ có sự thích nghi tột cùng để sinh tồn. |  | Bức tranh triết lý sinh thái học: Mạng lưới tiến hóa tự nhiên liên kết vạn vật; cán cân sinh tồn cân bằng giữa kẻ săn mồi tí hon và con mồi khổng lồ; KHÔNG có chú ong bắp cày ngọc trong cảnh này. |
| b03 | 00:16.7–00:26.7 (10.0s) | L54 | Bác sĩ phẫu thuật thần kinh đã chứng minh rằng: Một sinh vật nhỏ bé hoàn toàn có thể khuất phục những kẻ khổng lồ gấp nhiều lần bằng sự chính xác tuyệt đối, chiến lược bài bản và trí tuệ vi phẫu đỉnh cao! |  | Hình tượng vinh danh trí tuệ: chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) đứng trên đỉnh bục vinh quang, giơ cao ngòi kim vi phẫu lấp lánh như ngọn đuốc tri thức; b |
| b04 | 00:26.7–00:41.1 (14.4s) | L55 | Nếu trong cuộc sống bạn gặp phải những thử thách khổng lồ tưởng chừng không thể vượt qua, đừng vội dùng sức mạnh thô bạo để húc đầu vào đá: Hãy học tập sự sắc bén của ong bắp cày ngọc, tìm ra đúng mắt xích trọng tâm và giải quyết vấn đề bằng sự điềm tĩnh và chính xác nhất! |  | Bài học truyền cảm hứng cuộc sống: Hình ảnh một bạn nhỏ hoạt hình tự tin đối đầu với một tảng đá chướng ngại vật khổng lồ bằng một chiếc đòn bẩy nhỏ xíu; ánh mặt trời rạng rỡ phía sau. |
| b05 | 00:41.1–00:50.9 (9.8s) | L56 | Nếu được sở hữu một kỹ năng của loài ong này, bạn muốn sở hữu chiếc áo ngọc bích lấp lánh hay khả năng vi phẫu thao túng tâm trí? Hãy để lại bình luận tranh luận của bạn bên dưới nhé! |  | Tương tác khán giả: chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) cùng thẩm phán cú mèo uy nghiêm đội tóc giả quan tòa màu trắng, mặc áo thụng đen, tay cầm búa gõ đứn |
| b06 | 00:50.9–01:03.5 (12.6s) | L57 | Còn bây giờ, hãy chuẩn bị bước vào hồ sơ bệnh án số 44! Một gã khổng lồ nặng tới 2 tấn trôi dạt giữa đại dương, cơ thể dị hợm như chỉ có một cái đầu cụt ngủn biết bơi, ngơ ngác đến mức bị hải cẩu bơi lại cắn đứt từng mảng vây vẫn nằm phơi nắng nhìn trời! | **2 TẤN** · gã khổng lồ vô tri · R/360 · [0.75, 0.5] | Cận cảnh hình bóng teaser tập 44 (TASTE-68): Giữa đại dương bao la, bóng đen một con cá khổng lồ tròn xoe 2 tấn cụt ngủn như chỉ có cái đầu nổi lềnh bềnh trên mặt nước, gắn dấu hỏi '?' lớn màu vàng. |
| b07 | 01:03.5–01:06.0 (2.5s) | L58 | Bạn có biết gã khổng lồ vô tri này là ai không? |  | Poster đóng dấu hồ sơ 44: Chữ TẬP 44 phát sáng vàng rực trên nền biển xanh; bóng đen gã khổng lồ vô tri đang phơi nắng ngắm trời; KHÔNG có chú ong bắp cày ngọc trong cảnh này. |

## 5. Phân cảnh Shorts — từng beat

Banner: **ONG PHẪU THUẬT NÃO / BIẾN GIÁN THÀNH ZOMBIE?!** · giọng 42.6s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Bạn có tin một con ong bé tí chỉ bằng ngón tay lại có thể biến một con gián to gấp 6 |  |
| s02 | 00:04.9 | S01b | lần thành một xác sống Zombie ngoan ngoãn nghe lời răm rắp? |  |
| s03 | 00:07.9 | S02 | Đây là Ong Bắp Cày Ngọc, sát thủ mang biệt danh Bác sĩ phẫu thuật thần kinh! |  |
| s04 | 00:12.1 | S03 | Thay vì giết con mồi, | **PHÁT 1** · liệt chân trước · R/620 · [0.5, 0.4] |
| s05 | 00:13.6 | S03b | gã tung ra 2 phát châm kim độc quyền: Phát 1 châm thẳng vào ngực làm tê liệt hai chân trước của gián trong 2-3 phút. |  |
| s06 | 00:19.9 | S04 | Sau đó, gã chọc mũi kim xuyên qua sọ gián, tìm chính xác hạch não dưới thực quản để bơm độc tố ức chế ý chí sinh tồn! | **VI PHẪU** · hạch não gián · R/620 · [0.5, 0.4] |
| s07 | 00:26.3 | S05 | Hậu quả là con gián vẫn sống, tim vẫn đập, nhưng mất sạch 100% phản xạ sợ hãi và ý chí chạy trốn! | **100%** · mất ý chí · L/620 · [0.5, 0.4] |
| s08 | 00:32.2 | S06 | Ong chỉ việc cắn bớt râu, ngậm gốc |  |
| s09 | 00:33.9 | S07 | râu dắt con gián tự bước chân vào hang ngầm như dắt thú cưng đi dạo! |  |
| s10 | 00:37.9 | S08 | Một kỳ tích vi phẫu não bộ thao túng tâm lý đỉnh cao và rùng rợn nhất thế giới côn trùng! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trật tự toàn thể phòng xử án hình sự sinh học tối cao! Đại diện Viện Kiểm Sát Tự Nhiên hôm nay chính thức công bố bản cáo trạng điều tra đặc biệt về một vụ án xâm phạm thân thể và thao túng tâm lý tàn bạo bậc nhất trong lịch sử tiến hóa động vật!". Bố cục: Phòng xử án hình sự sinh học tối cao: Bàn công tố viên gỗ gụ trang nghiêm phủ đầy các hồ sơ vụ án gắn nhãn TỐI MẬT; KHÔNG có chú ong bắp cày ngọc trong cảnh này; BÊN TRÁI thẩm phán cú mèo uy nghiêm đội tóc giả quan tòa màu trắng, mặc áo thụng đen, tay cầm búa gõ đang ngồi trên bục thẩm phán uy nghiêm.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không dùng sức mạnh cơ bắp áp đảo, không chinh phục nạn nhân tại chỗ, kẻ thủ ác này khoác lên mình một tấm áo choàng ngọc bích lộng lẫy kiêu sa nhưng lại sở hữu thủ đoạn giải phẫu thần kinh lạnh lùng đến rợn gáy! Gã không chiến thắng con mồi, mà biến một chiến binh gián khỏe mạnh, nhanh nhẹn bậc nhất hành tinh thành một xác sống Zombie ngoan ngoãn tự bước chân vào nấm mồ chôn sống! Trật tự phiên tòa! Thẩm phán yêu cầu công tố viên công bố danh tính bị cáo và vạch trần thủ đoạn gây án ngay lập tức!". Bố cục: Ánh sáng spotlight chiếu rọi: Một cái bóng đen bí ẩn khoác áo choàng ngọc bích lấp lánh cầm chiếc kim tiêm phát sáng; phía đối diện là bóng dáng một con gián to lớn đang ngoan ngoãn cúi đầu bước đi như xác sống; KHÔNG có chú ong bắp cày ngọc trong cảnh này.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thưa Hội đồng xét xử! Bị cáo mang mã số 43 của chúng ta có tên khoa học là Ampulex compressa, thuộc bộ cánh màng, hay còn được gọi bằng cái tên hoa mỹ là Ong Bắp Cày Ngọc!". Bố cục: Bục bị cáo: chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) đứng trên bục gỗ, lớp vỏ ngọc bích xanh biếc lấp lánh kiêu sa, một tay chống nạnh, một tay xoay chiếc kim tiêm vi phẫu bạc tinh xảo; biểu cảm nửa cười nửa ngạo nghễ.
```
</details>

<details><summary>L03b</summary>

```text
HÌNH L03b (16:9 ngang, phong cách giải phẫu số Cyberpunk Bio-Surgery với các đường viền phát quang neon lục bảo quang phổ, mạch điện sinh học; minh họa chiến binh gián bị tác động thần kinh trở nên ngoan ngoãn; nền trắng tinh khiết, KHÔNG chữ, không số, không logo). Bố cục: Bảng mạch giải phẫu số mô tả thao tác kiểm soát xung thần kinh vận động.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng trong giới giang hồ tự nhiên, nạn nhân và các nhà khoa học gọi gã bằng một biệt danh rùng rợn: Bác sĩ phẫu thuật thần kinh!". Bố cục: Tấm thẻ bảng câu đố vui hoạt hình quốc tế: Ảnh chụp chân dung chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) đeo kính lúp vi phẫu, đóng dấu đỏ tươi BÁC SĨ PHẪU THUẬT THẦN KINH; bên cạnh là mô hình hộp sọ côn trùng phát sáng neon.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chiều dài cơ thể của gã chỉ khoảng 20mm, khoác lớp vỏ chitin lấp lánh ánh kim màu xanh ngọc lục bảo và lam biếc tuyệt đẹp tựa như một viên đá quý di động! Nhưng đừng để vẻ ngoài kiều diễm ấy đánh lừa, bởi vì chiếc đuôi của gã cất giấu một chiếc kim tiêm vi phẫu tinh xảo đến mức khiến mọi giáo sư phẫu thuật sọ não loài người cũng phải ngả mũ bái phục!". Bố cục: Thước đo vi phẫu: chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) đứng cạnh chiếc thước kẹp cơ khí hiển thị đúng 20mm; lớp vỏ cánh phản chiếu ánh kim ngũ sắc như kim loại titan đổi màu.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trước khi đi vào hiện trường gây án, Viện Kiểm Sát xin nhấn mạnh rằng: Nạn nhân của Bác sĩ phẫu thuật thần kinh không phải là những sâu bọ mềm yếu. Nạn nhân là loài gián nhà Mỹ Periplaneta americana, một loài sinh vật sống dai khét tiếng đã tồn tại hơn 300 triệu năm trên Trái Đất!". Bố cục: Hồ sơ đối tượng nạn nhân: BÊN TRÁI ảnh chụp chú gián to gấp sáu lần ong, màu nâu cánh gián bóng lưỡng, mắt xoắn ốc đờ đẫn ngoan ngoãn như Zombie, râu bị cắt ngắn một nửa cơ bắp cuồn cuộn với các thông số tốc độ chạy và sức bền cực khủng; BÊN PHẢI thẩm phán cú mèo uy nghiêm đội tóc giả quan tòa màu trắng, mặc áo thụng đen, tay cầm búa gõ đang cầm kính lúp săm soi kinh ngạc.
```
</details>

<details><summary>L06b</summary>

```text
HÌNH L06b (16:9 ngang, phong cách giải phẫu số Cyberpunk Bio-Surgery với ánh kim loại lục bảo và các chỉ số đo lường vi điện tử; cận cảnh đầu kim tiêm nọc độc tinh vi của ong bắp cày ngọc; nền trắng tinh khiết, KHÔNG chữ, không số, không logo). Bố cục: Sơ đồ hiển vi đầu kim châm và các cảm biến cơ học siêu nhạy.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một loài côn trùng có thể sống sót sau bom nguyên tử, chạy trốn với vận tốc 1.5 mét mỗi giây, và có thể sống cả tuần mà không cần đầu!". Bố cục: Biểu đồ sinh tồn siêu đẳng: Chú gián đang cười khẩy bước qua đám lửa và tia phóng xạ hạt nhân; đồng hồ đo tốc độ chỉ vọt lên 1.5 mét mỗi giây; KHÔNG có chú ong bắp cày ngọc trong cảnh này.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng khi đối đầu với mũi kim của Bác sĩ phẫu thuật thần kinh,". Bố cục: Khoảnh khắc đối đầu định mệnh: Chú gián khổng lồ giơ 6 chiếc chân gai góc nhọn hoắt nhưng run rẩy toát mồ hôi hột; phía trên không trung, chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) lao xuống như một phi cơ tiêm kích tàng hình với chiếc kim tiêm lóe sáng.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "toàn bộ sức mạnh kiên cường ấy biến thành con số không tròn trĩnh!". Bố cục: Biểu tượng sụp đổ: Chiếc khiên bảo vệ bằng chitin của loài gián bị mũi kim laser xuyên thủng, vỡ vụn thành các mảnh kính văng tung tóe; chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) lượn vòng đầy kiêu hãnh.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy lật lại từng trang hồ sơ khám nghiệm hiện trường vụ tấn công! Nạn nhân được lựa chọn ở đây là loài gián nhà nhiệt đới. Về tương quan thể lực, con gián to lớn và nặng gấp 6 lần Bác sĩ phẫu thuật thần kinh!". Bố cục: Bàn mổ xẻ vụ án số 1: Sơ đồ tương quan lực lượng; BÊN TRÁI chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) nhỏ nhắn như hạt đậu; BÊN PHẢI chú gián to gấp sáu lần ong, màu nâu cánh gián bóng lưỡng, mắt xoắn ốc đờ đẫn ngoan ngoãn như Zombie, râu bị cắt ngắn một nửa to đùng như chiếc xe bọc thép nặng gấp 6 lần.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gián sở hữu hệ thống lông cảm biến siêu nhạy ở đuôi, phát hiện được cả những dao động không khí nhỏ nhất và có thể tăng tốc tẩu thoát chỉ trong vòng vài phần nghìn giây.". Bố cục: Cận cảnh lông cảm biến đuôi gián: Sóng âm dao động không khí phát sáng radar quanh hai chiếc râu đuôi cerci; chú gián to gấp sáu lần ong, màu nâu cánh gián bóng lưỡng, mắt xoắn ốc đờ đẫn ngoan ngoãn như Zombie, râu bị cắt ngắn một nửa vểnh tai sẵn sàng phóng đi như tên bắn; KHÔNG có chú ong bắp cày ngọc trong cảnh này.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu lao vào một cuộc đấu vật tay đôi trực diện, chú ong nhỏ bé chắc chắn sẽ bị con gián khổng lồ đá văng hoặc nghiền nát dưới những chiếc chân gai nhọn hoắt! Vậy bị cáo đã làm cách nào để khuất phục một gã khổng lồ to xác gấp 6 lần mình?". Bố cục: Sàn đấu võ đài côn trùng: Con gián tung chân sau to khỏe đá văng một cành cây gãy đôi; cát bụi bay mù mịt; KHÔNG có chú ong bắp cày ngọc trong cảnh này.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đây chính là điểm khởi đầu của kế hoạch gây án bài bản đến kinh ngạc! Bác sĩ phẫu thuật thần kinh không hề chích bừa bãi!". Bố cục: Chiến thuật phục kích tàng hình: chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) ẩn mình trên kẽ lá cây, đôi mắt qua kính lúp vi phẫu lấp lánh tính toán góc rơi và tọa độ tiếp đất hoàn hảo.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gã phục kích từ trên cao, lao xuống như một tia chớp kim loại và dùng cặp hàm thép kẹp chặt lấy lưng con gián.". Bố cục: Pha không kích ngoạn mục: chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) lao vút xuống cắm phập cặp hàm thép sắc lẹm vào lưng gián, khóa chặt điểm mù sau gáy khiến nạn nhân không thể hất văng.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ngay trong tích tắc đối phương còn đang bàng hoàng, chiếc kim tiêm từ đuôi ong uốn cong, đâm một phát châm chuẩn xác đến từng mi-li-mét vào hạch thần kinh ngực trước của gián!". Bố cục: Đòn châm kim sấm sét: Đuôi của chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) uốn cong chữ C, chiếc kim tiêm bạc đâm phập chính xác vào đốt ngực trước của chú gián to gấp sáu lần ong, màu nâu cánh gián bóng lưỡng, mắt xoắn ốc đờ đẫn ngoan ngoãn như Zombie, râu bị cắt ngắn một nửa; luồng độc tố xanh lam bốc khói lan tỏa.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Độc tố của phát 1 chứa hàm lượng lớn chất ức chế dẫn truyền GABA, ngay lập tức làm tê liệt hoàn toàn hai chiếc chân trước của nạn nhân trong vòng 2-3 phút!". Bố cục: Sơ đồ giải phẫu hóa sinh: Độc tố chứa GABA khóa chặt các kênh dẫn truyền thần kinh vận động; hai chiếc chân trước của chú gián to gấp sáu lần ong, màu nâu cánh gián bóng lưỡng, mắt xoắn ốc đờ đẫn ngoan ngoãn như Zombie, râu bị cắt ngắn một nửa rũ rượi xụi lơ; đồng hồ cát đếm ngược 2-3 phút.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Con gián dù vẫn còn tỉnh táo nhưng hai chân trước đã bị liệt hoàn toàn, không thể cựa quậy hay xoay người bỏ chạy! Chiếc áo giáp phản xạ của gián chính thức bị phong tỏa!". Bố cục: Tình trạng bất động dở khóc dở cười: chú gián to gấp sáu lần ong, màu nâu cánh gián bóng lưỡng, mắt xoắn ốc đờ đẫn ngoan ngoãn như Zombie, râu bị cắt ngắn một nửa mắt tròn xoe kinh ngạc, hai chân trước mềm như cọng bún không thể chống đất, toàn thân đổ sụp về phía trước bất lực.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhóm nghiên cứu của giáo sư Kenneth Catania tại Đại học Vanderbilt đã sử dụng máy quay tốc độ cao 1.000 khung hình mỗi giây để giải mã cuộc đụng độ này: Khi gián phát hiện bị ong tập kích, nó thường vung chân sau tung ra những cú đá hậu karate cực mạnh nhằm hất văng kẻ thù. Nhưng Bác sĩ phẫu thuật thần kinh cực kỳ ranh mãnh!". Bố cục: Phòng nghiên cứu sinh học đại học: Màn hình máy quay siêu chậm 1.000 khung hình/giây ghi lại khoảnh khắc gián tung cú đá hậu karate nhưng hụt trong gang tấc.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gã lượn vòng từ góc mù, túm chặt lấy mép khiên ngực bảo vệ của gián, biến chính điểm tựa của đối phương thành thế gọng kìm bất khả kháng cự!". Bố cục: Khóa khớp gọng kìm: chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) dùng chân bám chặt mép khiên ngực của gián như tay đua cưỡi bò tót; gián giãy giụa vô vọng không thể chạm tới đối thủ.
```
</details>

<details><summary>L19b</summary>

```text
HÌNH L19b (16:9 ngang, phong cách giải phẫu số Cyberpunk Bio-Surgery với tia quét scanlines và lưới đo thời gian; mô phỏng phân tích chuyển động tốc độ cao 1000 khung hình/giây cú đá tự vệ của gián; nền trắng tinh khiết, KHÔNG chữ, không số, không logo). Bố cục: Biểu đồ động lực học so sánh phản xạ thần kinh của gián và ong.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cú châm kim số một diễn ra chỉ trong vòng nửa giây, nhanh như một mũi tên tẩm thuốc mê bắn trúng tim đen con mồi!". Bố cục: Đồng hồ bấm giờ nửa giây: Chiếc kim tiêm rút ra trong 0.5s; mũi tiêm để lại một chấm sáng màu xanh ngọc bích trên ngực gián; cánh cửa sổ thoát hiểm của gián chính thức sập lại.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sau khi nạn nhân đã bị trói chặt hai chân trước trong trạng thái bất động tạm thời, ca phẫu thuật sọ não rùng rợn nhất hành tinh chính thức bắt đầu! Thưa Hội đồng xét xử, hãy nhìn vào màn hình phóng đại vi phẫu: Bác sĩ phẫu thuật thần kinh từ tốn buông ngực gián ra, bò lên phần đầu của nạn nhân.". Bố cục: Phòng mổ thần kinh tương lai: Màn hình quét sóng não điện não đồ EEG hiển thị hộp sọ gián; chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) đeo găng tay phẫu thuật đứng trước đầu con gián bất động.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gã dùng hàm giữ chặt mép sọ, rồi từ từ chọc chiếc kim tiêm dài luồn qua lớp màng mềm giữa đầu và cổ. Đây không phải là một cú đâm mù quáng!". Bố cục: Khoảnh khắc mở đường luồn kim: chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) giữ chặt mép cổ gián, chiếc kim tiêm siêu nhỏ luồn nhẹ qua lớp màng cổ mềm mại; ánh sáng quét laser dẫn hướng.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nghiên cứu của giáo sư Libersat tại Đại học Ben-Gurion đã phát hiện ra rằng: Trên đầu mũi kim của ong có chứa hàng loạt thụ thể hóa học và cơ học cực nhạy, đóng vai trò như một hệ thống định vị GPS sinh học!". Bố cục: Đầu kim tiêm định vị GPS: Phóng to cực đại đầu ngòi châm của chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái); hàng trăm thụ thể cảm giác li ti phát sáng như ăng-ten radar tìm đường đi qua các khe hở mô não; KHÔNG có chú ong bắp cày ngọc trong cảnh này.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mũi kim vi phẫu luồn sâu vào trong hộp sọ, dò dẫm từng milimét mô não và chạm thẳng vào trung khu điều khiển vận động tối cao: Đó là hạch não dưới thực quản của gián!". Bố cục: Bản đồ hạch não gián: Mũi kim chạm trúng hạch não dưới thực quản sub-esophageal ganglion; điểm tiếp xúc phát nổ tia sáng vàng kim rực rỡ; KHÔNG có chú ong bắp cày ngọc trong cảnh này.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tại đây, gã bơm vào một liều cocktail hóa chất độc quyền gồm dopamine và các hợp chất ức chế thụ thể octopamine. Hợp chất này có tác dụng gì? Nó không hề chiến thắng tế bào não, cũng không làm gián bị tê liệt toàn thân! Ngược lại, tim gián vẫn đập, cơ bắp vẫn hoạt động bình thường!". Bố cục: Cocktail hóa chất thần kinh: Bình thuốc tiêm phát sáng chứa phân tử dopamine và chất chẹn octopamine tuôn trào vào synap thần kinh não gián.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng thụ thể octopamine chính là chiếc công tắc khởi động ý chí sinh tồn, động lực chạy trốn và phản xạ sợ hãi của loài gián. Khi công tắc này bị dập tắt, con gián hoàn toàn mất đi ý chí tự do!". Bố cục: Công tắc ý chí bị dập tắt: Bức tranh ẩn dụ chiếc cầu dao điện dán nhãn Ý CHÍ SINH TỒN bị một ngón tay gạt phắt xuống vị trí TẮT; bóng tối bao trùm đôi mắt gián; KHÔNG có chú ong bắp cày ngọc trong cảnh này.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu bạn thả con gián này vào một xô nước, phản xạ bản năng vẫn khiến nó bơi nổi; nhưng nếu để nó trên cạn, nó sẽ chỉ đứng đực mặt ra đó, ngoan ngoãn đến mức ai làm gì cũng cam chịu!". Bố cục: Thí nghiệm đối chứng kỳ lạ: BÊN TRÁI gián rơi xuống xô nước vẫn bơi nổi như thường; BÊN PHẢI gián trên cạn đứng trơ như khúc gỗ mắt nhìn vô định; KHÔNG có chú ong bắp cày ngọc trong cảnh này.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một xác sống Zombie thực thụ đã ra đời dưới ngòi kim của Bác sĩ phẫu thuật thần kinh!". Bố cục: Chân dung gián Zombie: chú gián to gấp sáu lần ong, màu nâu cánh gián bóng lưỡng, mắt xoắn ốc đờ đẫn ngoan ngoãn như Zombie, râu bị cắt ngắn một nửa hai mắt biến thành hình xoắn ốc thôi miên, khóe miệng chảy dãi ngây ngô; chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) đứng bên cạnh khoanh tay mỉm cười đắc thắng.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Điều kỳ dị hơn nữa là ngay sau khi mũi kim rút ra khỏi não, lượng dopamine đậm đặc trong nọc độc bắt đầu phát huy tác dụng tâm lý bất ngờ: Con gián không hề bỏ chạy hay quằn quại đau đớn, mà đứng yên tại chỗ và bắt đầu chải chuốt cơ thể một cách cuồng loạn suốt 30 phút liên tục! Nó dùng chân lau chùi mắt, vuốt ve râu và làm sạch cơ thể như một kẻ mắc chứng ám ảnh cưỡng chế!". Bố cục: Cơn cuồng chải chuốt: chú gián to gấp sáu lần ong, màu nâu cánh gián bóng lưỡng, mắt xoắn ốc đờ đẫn ngoan ngoãn như Zombie, râu bị cắt ngắn một nửa đứng yên một chỗ, hai chân liên tục chùi mặt, vuốt râu, chải lông suốt 30 phút như bị ám ảnh cưỡng chế; đồng hồ cát quay tít.
```
</details>

<details><summary>L29b</summary>

```text
HÌNH L29b (16:9 ngang, phong cách giải phẫu số Cyberpunk Bio-Surgery kết hợp đồ họa phân tử sinh học; chú gián đứng yên say sưa chải chuốt râu và chân dưới tác động của chất ức chế dopamine; nền trắng tinh khiết, KHÔNG chữ, không số, không logo). Bố cục: Minh họa hiệu ứng sinh hóa phong tỏa ý chí tự vệ.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong lúc nạn nhân đang mải mê làm đẹp trong vô thức, Bác sĩ phẫu thuật thần kinh thong dong bay đi tìm một chiếc hốc đất lý tưởng để chuẩn bị căn phòng giam giữ!". Bố cục: Thảnh thơi chuẩn bị hầm ngục: chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) bay lượn trên đám rễ cây mục, dùng chân bới đất đào một chiếc hang ngầm nhỏ, miệng huýt sáo thảnh thơi.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sau ca phẫu thuật não kéo dài chưa đầy 30 phút, tác dụng của mũi tiêm số một tan biến, hai chân trước của con gián cử động trở lại bình thường. Nhưng hỡi ôi, nạn nhân giờ đây chỉ còn là một cái xác không hồn biết thở! Bác sĩ phẫu thuật thần kinh". Bố cục: Hiện trường sau ca mổ: chú gián to gấp sáu lần ong, màu nâu cánh gián bóng lưỡng, mắt xoắn ốc đờ đẫn ngoan ngoãn như Zombie, râu bị cắt ngắn một nửa hai chân trước đã hết thuốc tê, đứng dậy cử động bình thường nhưng ánh mắt đờ đẫn hoàn toàn; chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) bay lượn xung quanh đánh giá con mồi.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "lúc này tiến hành bước xử lý tiếp theo khiến các điều tra viên phải há hốc mồm: Thể trọng con gián quá nặng, gấp 6 lần ong, nên ong hoàn toàn không thể tha hay vác nạn nhân bay trên không trung.". Bố cục: Bài toán vận tải nan giải: Chiếc cân đòn bẩy cho thấy gián nặng gấp 6 lần ong; chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) giơ một ngón tay lên trán mỉm cười lóe sáng ý tưởng thiên tài.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thay vì tốn sức kéo lê con mồi khổng lồ, gã lại bắt con mồi phải tự đi bằng chính đôi chân của mình! Con gián to xác tự bước đi theo sau kẻ thù sao?! Thật hoang đường, chuyện này diễn ra như thế nào? Đúng như Thẩm phán vừa kinh ngạc thốt lên! Bác sĩ phẫu thuật thần kinh tiến lại gần, dùng cặp hàm sắc lẻm cắt tỉa bớt một nửa chiều dài hai sợi râu dài của con gián.". Bố cục: Màn cắt tỉa ăng-ten: chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) dùng cặp hàm kẹp đôi như chiếc kéo thợ may cắt phăng một nửa chiều dài hai sợi râu của chú gián to gấp sáu lần ong, màu nâu cánh gián bóng lưỡng, mắt xoắn ốc đờ đẫn ngoan ngoãn như Zombie, râu bị cắt ngắn một nửa; hai đoạn râu thừa rơi xuống đất.
```
</details>

<details><summary>L33b</summary>

```text
HÌNH L33b (16:9 ngang, phong cách giải phẫu số Cyberpunk Bio-Surgery với đường truyền tín hiệu neon lục bảo; ong bắp cày ngọc ngậm râu dắt gián khổng lồ đi theo sau như một con cún ngoan ngoãn; nền trắng tinh khiết, KHÔNG chữ, không số, không logo). Bố cục: Hoạt cảnh điều khiển hành vi kỳ ảo giữa ong và gián.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gã ghé miệng vào vết cắt uống từng giọt dịch nước màu hemolymph tứa ra để nạp lại năng lượng calo sau ca mổ căng thẳng.". Bố cục: Thưởng thức ly cocktail năng lượng: chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) ghé miệng uống giọt dịch hemolymph trong suốt rỉ ra từ cuống râu gián; biểu cảm khoan khoái nạp đầy pin năng lượng.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sau đó, gã ngậm chặt lấy phần gốc râu còn lại của con gián như cầm một sợi dây dắt chó đi dạo!". Bố cục: Màn dắt thú cưng đi dạo: chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) ngậm chặt gốc râu gián, hai tay cầm như cầm dây cương ngựa; chú gián to gấp sáu lần ong, màu nâu cánh gián bóng lưỡng, mắt xoắn ốc đờ đẫn ngoan ngoãn như Zombie, râu bị cắt ngắn một nửa to xác lững thững bước theo sau như chú cún cưng vâng lời.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gã lùi từng bước về phía trước, và con gián to xác răm rắp bước theo từng bước chân của kẻ đã cướp não mình!". Bố cục: Đoàn diễu hành qua rừng lá khô: chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) đi lùi từng bước dẫn đường; chú gián to gấp sáu lần ong, màu nâu cánh gián bóng lưỡng, mắt xoắn ốc đờ đẫn ngoan ngoãn như Zombie, râu bị cắt ngắn một nửa nhấc từng chiếc chân dài cẩn thận theo sau, không hề chống cự hay rẽ ngang.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nạn nhân thong thả bước xuống căn hầm mộ tối tăm do ong đào sẵn dưới lòng đất, ngoan ngoãn ngồi im trong góc tối mà không có lấy một chút ý định chạy trốn hay phản kháng!". Bố cục: Lối vào hầm mộ ngầm: chú gián to gấp sáu lần ong, màu nâu cánh gián bóng lưỡng, mắt xoắn ốc đờ đẫn ngoan ngoãn như Zombie, râu bị cắt ngắn một nửa ngoan ngoãn cúi đầu chui lọt qua miệng hang đất hẹp; chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) đứng trên mép hang gật đầu tán thưởng.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhà tự nhiên học Francis Williams khi quan sát hiện tượng này tại quần đảo Hawaii vào năm 1942 đã từng miêu tả: Đây là cảnh tượng siêu thực bậc nhất trong rừng nhiệt đới! Một chú ong nhỏ bằng hạt đậu ngọc bích, dùng hàm ngậm râu con gián khổng lồ dắt đi băng qua những đám lá khô mục nát.". Bố cục: Ghi chép lịch sử năm 1942: Cuốn sổ tay thám hiểm Hawaii với bức tranh vẽ mực tả thực cảnh chú ong ngọc bích dắt con gián khổng lồ đi dạo trên đảo nhiệt đới.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Con gián bước đi thảnh thơi tựa như đang dạo phố cùng bạn thân, thỉnh thoảng còn dừng lại đợi chú ong vượt qua chướng ngại vật!". Bố cục: Khoảnh khắc siêu thực: chú gián to gấp sáu lần ong, màu nâu cánh gián bóng lưỡng, mắt xoắn ốc đờ đẫn ngoan ngoãn như Zombie, râu bị cắt ngắn một nửa dừng chân chờ chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) leo qua một hòn sỏi cản đường, rồi cả hai lại tiếp tục thong thả cùng nhau đi xuống hang.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Toàn bộ hệ thống cơ bắp vận động của con gián vẫn hoạt động 100% công suất, nhưng bộ máy ý chí và bản năng tự vệ đã bị kẻ thù cầm tù vĩnh viễn!". Bố cục: Cắt lớp buồng giam dưới lòng đất: chú gián to gấp sáu lần ong, màu nâu cánh gián bóng lưỡng, mắt xoắn ốc đờ đẫn ngoan ngoãn như Zombie, râu bị cắt ngắn một nửa ngồi im lìm trong góc tối của căn hầm ngầm, cơ bắp lành lặn nhưng đôi mắt hoàn toàn trống rỗng không hồn.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thưa Hội đồng xét xử, chương man rợ và tinh vi nhất của bản cáo trạng nằm ở căn hầm mộ này! Sau khi dắt được con gián vào hang, Bác sĩ phẫu thuật thần kinh không hề cắn chết nạn nhân.". Bố cục: Căn hầm mộ sinh học: chú gián to gấp sáu lần ong, màu nâu cánh gián bóng lưỡng, mắt xoắn ốc đờ đẫn ngoan ngoãn như Zombie, râu bị cắt ngắn một nửa đứng im giữa lòng hang tối; chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) đang cẩn thận gắn một vật thể nhỏ li ti màu trắng lên chân gián; ánh sáng lân tinh soi rọi.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gã đẻ cẩn thận đúng 1 quả trứng duy nhất dính chặt vào gốc chân giữa của gián.". Bố cục: Quả trứng định mệnh: Cận cảnh một quả trứng ong nhỏ thuôn dài dán dính chắc chắn vào gốc chân giữa của chú gián to gấp sáu lần ong, màu nâu cánh gián bóng lưỡng, mắt xoắn ốc đờ đẫn ngoan ngoãn như Zombie, râu bị cắt ngắn một nửa; quả trứng phát sáng mờ ảo.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sau đó, ong mẹ chui ra khỏi hang, cần mẫn nhặt từng viên sỏi nhỏ, mẩu lá cây và đất vụn lấp kín miệng hang lại để ngăn chặn mọi kẻ xâm nhập từ bên ngoài. Con gián bị nhốt kín bên trong bóng tối vĩnh cửu cùng với quả trứng tử thần!". Bố cục: Niêm phong cửa hầm: chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) tha từng viên sỏi nhỏ, mẩu lá cây vụn đắp kín miệng hang thành một bức tường đá kiên cố; không một sinh vật nào nhận ra lối vào.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sau 2-3 ngày, quả trứng nở thành một ấu trùng ong nhỏ xíu màu trắng. Ấu trùng dùng hàm cắn thủng một lỗ nhỏ trên lớp vỏ gián để hút dịch cơ thể.". Bố cục: Ấu trùng chào đời: Quả trứng nứt vỏ, một chú ấu trùng sâu trắng ngọ nguậy thò đầu ra, dùng miệng cắn thủng lớp vỏ mềm chân gián để hút dịch; KHÔNG có chú ong bắp cày ngọc trong cảnh này.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi lớn hơn, nó chui tọt vào bên trong ổ bụng của gián và bắt đầu bữa tiệc sinh tồn!". Bố cục: Xâm nhập cơ thể: Ấu trùng chui tọt qua lỗ thủng vào bên trong ổ bụng của chú gián to gấp sáu lần ong, màu nâu cánh gián bóng lưỡng, mắt xoắn ốc đờ đẫn ngoan ngoãn như Zombie, râu bị cắt ngắn một nửa; con gián vẫn đứng im thở đều đặn như không hề hay biết; KHÔNG có chú ong bắp cày ngọc trong cảnh này.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy lắng nghe nguyên tắc y khoa của ấu trùng: Nếu nó cắn đứt tim hoặc hệ thần kinh trung ương, con gián sẽ chết ngay lập tức; và trong môi trường nhiệt đới nóng ẩm, cái xác sẽ thối rữa và bốc mùi chỉ sau 24 giờ, đầu độc chết chính ấu trùng!". Bố cục: Nguy cơ thối rữa phân hủy: Chiếc đồng hồ 24 giờ đếm ngược biểu thị cái chết; nếu tim gián ngừng đập, vi khuẩn phân hủy sẽ đầu độc cả căn hầm; KHÔNG có chú ong bắp cày ngọc trong cảnh này.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Do đó, ấu trùng ong được lập trình bản năng chuẩn xác: Nó ăn toàn bộ lớp mỡ thừa và các cơ quan không thiết yếu trước, tuyệt đối tránh xa tim và mạch nước màu!". Bố cục: Sơ đồ ẩm thực chọn lọc: Ấu trùng gặm nhấm các mô mỡ thừa phát sáng xanh lục, né tránh hoàn toàn trái tim màu đỏ đang đập thình thịch và hệ dây thần kinh; KHÔNG có chú ong bắp cày ngọc trong cảnh này.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Con gián vẫn sống, tim vẫn đập suốt 8-10 ngày liên tục như một chiếc tủ lạnh sinh học bảo quản thịt tươi hoàn hảo!". Bố cục: Tủ lạnh thịt tươi sống 10 ngày: Biểu tượng chiếc tủ lạnh sinh học bảo quản thực phẩm hoàn hảo suốt 8-10 ngày; nhịp tim gián hiển thị đều đặn trên màn hình theo dõi; KHÔNG có chú ong bắp cày ngọc trong cảnh này.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cho đến khi ăn sạch mọi thứ, ấu trùng mới cắn đứt tim, đan kén nhộng bên trong xác gián khô rỗng rồi lột xác bay ra ngoài!". Bố cục: Chiếc kén nhộng bên trong vỏ gián: Ấu trùng đan một chiếc kén tơ nâu óng ánh chiếm trọn bên trong cái xác khô rỗng của gián; lớp vỏ gián bảo vệ kén khỏi kẻ thù; KHÔNG có chú ong bắp cày ngọc trong cảnh này.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa dừng lại ở đó, các nhà sinh vật học còn phát hiện ấu trùng ong tiết ra một loại hợp chất kháng sinh cực mạnh từ tuyến nước bọt. Hợp chất này phủ kín toàn bộ khoang bụng của gián, tiêu diệt sạch sẽ mọi vi khuẩn phân hủy và nấm mốc gây hại trong lòng đất ẩm ướt! Nói cách khác, con gián không những bị biến thành thức ăn tươi sống, mà còn được ấu trùng tắm rửa khử trùng đạt chuẩn phòng phẫu thuật vô khuẩn tuyệt đối!". Bố cục: Phòng mổ vô khuẩn ngầm: Các phân tử kháng sinh từ nước bọt ấu trùng phát sáng xanh neon quét sạch mọi bào tử nấm mốc và vi khuẩn trong khoang bụng gián; KHÔNG có chú ong bắp cày ngọc trong cảnh này.
```
</details>

<details><summary>L50b</summary>

```text
HÌNH L48b (16:9 ngang, phong cách giải phẫu số Cyberpunk Bio-Surgery với màng chắn kháng khuẩn bảo vệ; ấu trùng ong tiết nước bọt vô trùng quét sạch nấm mốc và vi khuẩn trong bụng gián; nền trắng tinh khiết, KHÔNG chữ, không số, không logo). Bố cục: Sơ đồ sinh học hiển vi về kháng sinh tự nhiên bảo vệ môi trường phát triển.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một quy trình bảo quản thực phẩm đỉnh cao mà ngay cả các tập đoàn công nghệ thực phẩm hàng đầu thế giới cũng phải trầm trồ thán phục!". Bố cục: Sự tái sinh rực rỡ: Chiếc kén nứt ra, một chú ong bắp cày ngọc mới toanh với đôi cánh xanh biếc ánh kim chui ra khỏi xác gián, đục thủng lớp đất đá bay lên trời xanh.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Phiên tòa xét xử hồ sơ số 43 chính thức tuyên bố kết luận: Dưới lăng kính đạo đức con người, hành vi của Ong Bắp Cày Ngọc có thể khiến chúng ta rùng mình ớn lạnh.". Bố cục: Bản án kết luận phiên tòa: Búa thẩm phán gõ vang trên bục gỗ; thẩm phán cú mèo uy nghiêm đội tóc giả quan tòa màu trắng, mặc áo thụng đen, tay cầm búa gõ tuyên án công nhận Ong Bắp Cày Ngọc là một kỳ tích vi phẫu tiến hóa; chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) đứng kiêu hãnh nhận bản tuyên dương.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng dưới góc nhìn của khoa học tiến hóa, đây là một tuyệt tác cơ sinh học và hóa dược đỉnh cao! Tự nhiên không có thiện hay ác, chỉ có sự thích nghi tột cùng để sinh tồn.". Bố cục: Bức tranh triết lý sinh thái học: Mạng lưới tiến hóa tự nhiên liên kết vạn vật; cán cân sinh tồn cân bằng giữa kẻ săn mồi tí hon và con mồi khổng lồ; KHÔNG có chú ong bắp cày ngọc trong cảnh này.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bác sĩ phẫu thuật thần kinh đã chứng minh rằng: Một sinh vật nhỏ bé hoàn toàn có thể khuất phục những kẻ khổng lồ gấp nhiều lần bằng sự chính xác tuyệt đối, chiến lược bài bản và trí tuệ vi phẫu đỉnh cao!". Bố cục: Hình tượng vinh danh trí tuệ: chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) đứng trên đỉnh bục vinh quang, giơ cao ngòi kim vi phẫu lấp lánh như ngọn đuốc tri thức; biểu trưng cho sức mạnh của sự chính xác tuyệt đối.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu trong cuộc sống bạn gặp phải những thử thách khổng lồ tưởng chừng không thể vượt qua, đừng vội dùng sức mạnh thô bạo để húc đầu vào đá: Hãy học tập sự sắc bén của ong bắp cày ngọc, tìm ra đúng mắt xích trọng tâm và giải quyết vấn đề bằng sự điềm tĩnh và chính xác nhất!". Bố cục: Bài học truyền cảm hứng cuộc sống: Hình ảnh một bạn nhỏ hoạt hình tự tin đối đầu với một tảng đá chướng ngại vật khổng lồ bằng một chiếc đòn bẩy nhỏ xíu; ánh mặt trời rạng rỡ phía sau.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu được sở hữu một kỹ năng của loài ong này, bạn muốn sở hữu chiếc áo ngọc bích lấp lánh hay khả năng vi phẫu thao túng tâm trí? Hãy để lại bình luận tranh luận của bạn bên dưới nhé!". Bố cục: Tương tác khán giả: chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái) cùng thẩm phán cú mèo uy nghiêm đội tóc giả quan tòa màu trắng, mặc áo thụng đen, tay cầm búa gõ đứng hai bên chiếc bảng câu hỏi nhấp nháy dòng chữ Áo ngọc bích hay Thao túng tâm trí?, cùng chỉ tay mời khán giả bình luận.
```
</details>

<details><summary>L57</summary>

```text
HÌNH L57 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn bây giờ, hãy chuẩn bị bước vào hồ sơ bệnh án số 44! Một gã khổng lồ nặng tới 2 tấn trôi dạt giữa đại dương, cơ thể dị hợm như chỉ có một cái đầu cụt ngủn biết bơi, ngơ ngác đến mức bị hải cẩu bơi lại cắn đứt từng mảng vây vẫn nằm phơi nắng nhìn trời!". Bố cục: Cận cảnh hình bóng teaser tập 44 (TASTE-68): Giữa đại dương bao la, bóng đen một con cá khổng lồ tròn xoe 2 tấn cụt ngủn như chỉ có cái đầu nổi lềnh bềnh trên mặt nước, gắn dấu hỏi '?' lớn màu vàng.
```
</details>

<details><summary>L58</summary>

```text
HÌNH L58 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bạn có biết gã khổng lồ vô tri này là ai không?". Bố cục: Poster đóng dấu hồ sơ 44: Chữ TẬP 44 phát sáng vàng rực trên nền biển xanh; bóng đen gã khổng lồ vô tri đang phơi nắng ngắm trời; KHÔNG có chú ong bắp cày ngọc trong cảnh này.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Bạn có tin một con ong bé tí chỉ bằng ngón tay lại có thể biến một con gián to gấp 6 lần thành một xác sống Zombie ngoan ngoãn nghe lời răm rắp?". Bố cục: Cận cảnh mở đầu: chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng cầm chiếc kim tiêm siêu nhỏ phát sáng laser nháy mắt tinh quái nhìn thẳng vào người xem; phía sau là bóng đen con gián to gấp sáu lần.
```
</details>

<details><summary>S01b</summary>

```text
HÌNH S01b (9:16 dọc, phong cách Cyberpunk Bio-Surgery neon lục bảo; gián khổng lồ bị thôi miên hóa thành xác sống ngoan ngoãn bên cạnh ong bắp cày ngọc; nền trắng tinh khiết, KHÔNG chữ, không số, không logo).
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Đây là Ong Bắp Cày Ngọc, sát thủ mang biệt danh Bác sĩ phẫu thuật thần kinh!". Bố cục: chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng bay lượn kiêu hãnh với lớp vỏ ngọc bích xanh biếc ánh kim lấp lánh; chữ BÁC SĨ PHẪU THUẬT THẦN KINH nổi bật.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Thay vì giết con mồi, gã tung ra 2 phát châm kim độc quyền: Phát 1 châm thẳng vào ngực làm tê liệt hai chân trước của gián trong 2-3 phút.". Bố cục: Pha không kích: chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng khóa chặt lưng chú gián to gấp sáu lần ong, màu nâu cánh gián bóng lưỡng, mắt xoắn ốc đờ đẫn ngoan ngoãn như Zombie, râu bị cắt ngắn một nửa, ngòi kim uốn cong đâm phập vào ngực gián; hai chân trước của gián xụi lơ tức thì.
```
</details>

<details><summary>S03b</summary>

```text
HÌNH S03b (9:16 dọc, phong cách Cyberpunk Bio-Surgery neon lục bảo; sơ đồ nhắm mục tiêu 2 phát châm kim vi phẫu vào ngực và hạch não gián; nền trắng tinh khiết, KHÔNG chữ, không số, không logo).
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Sau đó, gã chọc mũi kim xuyên qua sọ gián, tìm chính xác hạch não dưới thực quản để bơm độc tố ức chế ý chí sinh tồn!". Bố cục: Vi phẫu sọ não: Mũi kim xuyên qua cổ gián chạm đúng hạch não dưới thực quản; độc tố phát sáng khóa chặt công tắc sợ hãi.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Hậu quả là con gián vẫn sống, tim vẫn đập, nhưng mất sạch 100% phản xạ sợ hãi và ý chí chạy trốn!". Bố cục: chú gián to gấp sáu lần ong, màu nâu cánh gián bóng lưỡng, mắt xoắn ốc đờ đẫn ngoan ngoãn như Zombie, râu bị cắt ngắn một nửa mắt xoắn ốc thôi miên biến thành Zombie đờ đẫn; cơ bắp vẫn lành lặn nhưng mất sạch 100% ý chí chạy trốn.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Ong chỉ việc cắn bớt râu, ngậm gốc râu". Bố cục: Màn dắt thú cưng siêu thực: chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng dùng hàm ngậm chặt gốc râu gián, dắt con gián to xác đi theo như dắt cún cưng.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "dắt con gián tự bước chân vào hang ngầm như dắt thú cưng đi dạo!". Bố cục: chú gián to gấp sáu lần ong, màu nâu cánh gián bóng lưỡng, mắt xoắn ốc đờ đẫn ngoan ngoãn như Zombie, râu bị cắt ngắn một nửa tự giác bước từng bước chân vào cửa hang ngầm tối om dưới rễ cây mục.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Một kỳ tích vi phẫu não bộ thao túng tâm lý đỉnh cao và rùng rợn nhất thế giới côn trùng!". Bố cục: Hình ảnh kết thúc: chú ong bắp cày ngọc hoạt hình ánh kim xanh ngọc bích, kính lúp vi phẫu, kim tiêm phát sáng đứng oai phong trên miệng hang đã niêm phong bằng đá, giơ ngón tay cái cười rạng rỡ chào tạm biệt khán giả.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/58 của video YouTube về Ong Bắp Cày Ngọc). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa vẽ tay đặc trưng cho chủ đề, nét mực sắc nét, màu sắc tương phản cuốn hút, tối giản giàu tính biểu tượng khoa học; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái). Nhân vật phụ cố định: chú gián to gấp sáu lần ong, màu nâu cánh gián bóng lưỡng, mắt xoắn ốc đờ đẫn ngoan ngoãn như Zombie, râu bị cắt ngắn một nửa; thẩm phán cú mèo uy nghiêm đội tóc giả quan tòa màu trắng, mặc áo thụng đen, tay cầm búa gõ. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/8 của video YouTube Shorts về Ong Bắp Cày Ngọc). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa vẽ tay đặc trưng cho chủ đề, nét mực sắc nét, màu sắc tương phản cuốn hút, tối giản giàu tính biểu tượng khoa học; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú ong bắp cày ngọc hoạt hình ngộ nghĩnh (màu xanh ngọc lục bảo và lam biếc ánh kim lấp lánh như viên ngọc bích, đôi mắt to tròn đeo kính lúp vi phẫu màu bạc, hai cánh mỏng trong suốt viền neon xanh, tay cầm chiếc kim tiêm siêu nhỏ phát sáng như dao mổ laser, biểu cảm lạnh lùng pha chút tinh quái). Nhân vật phụ: chú gián to gấp sáu lần ong, màu nâu cánh gián bóng lưỡng, mắt xoắn ốc đờ đẫn ngoan ngoãn như Zombie, râu bị cắt ngắn một nửa. 
```
</details>

## 7. SEO

- **title:** Bác Sĩ Phẫu Thuật Thần Kinh: Thao Túng Gián Thành Zombie?! | Ong Bắp Cày Ngọc | Tập 43
- **hook_paragraph:** Khám phá vụ án chấn động tự nhiên của Ong Bắp Cày Ngọc (Ampulex compressa) — kẻ sở hữu ngòi kim vi phẫu châm chuẩn xác vào hạch não để tước đoạt ý chí tự do, biến con gián to gấp sáu lần thành một xác sống Zombie ngoan ngoãn tự bước vào mồ chôn!
- **question:** Nếu được sở hữu một kỹ năng của loài ong này, bạn muốn có bộ giáp ngọc bích kiêu sa hay khả năng vi phẫu thao túng tâm trí?
- **next_teaser:** Tập 44: Bệnh án gã khổng lồ 2 tấn ngơ ngác như cái đầu cụt bơi giữa đại dương — Cá Mặt Trăng!
- **shorts_title:** Ong phẫu thuật não biến gián thành Zombie?! 🐝🧠 #shorts #dongvat #khoahoc
- **shorts_desc:** Khám phá cách Ong Bắp Cày Ngọc chích kim vào hạch não tước đoạt ý chí tự do, biến con gián to gấp 6 lần thành xác sống Zombie tự đi vào hang ngầm!
- **bullets:** Chiếc áo choàng ngọc bích lấp lánh ẩn giấu ngòi kim vi phẫu sọ não tinh xảo nhất giới côn trùng · Phát tiêm số một vào hạch ngực phong tỏa hoàn toàn 2 chân trước trong 2-3 phút · Cú vi phẫu số hai vào hạch não dưới thực quản dập tắt hoàn toàn thụ thể ý chí sinh tồn · Cắt tỉa ăng-ten dắt gián khổng lồ tự đi bộ vào hầm mộ ngầm như dắt thú cưng · Ấu trùng ăn nội tạng có chọn lọc, giữ gián sống tươi ngon suốt 8-10 ngày trong hang
- **tags:** ong bắp cày ngọc, ong bap cay ngoc, ampulex compressa, emerald cockroach wasp, ong bien gian thanh zombie, gian zombie, phau thuat than kinh con trung, thế giới động vật, vẽ chuyện hoang dã, tập 43
- **hashtags:** #OngBapCayNgoc #AmpulexCompressa #TheGioiDongVat #VeChuyenHoangDa #KhoaHoc #DongVatKyThu

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-43-ong-bap-cay-ngoc
python src/episode/pipeline.py tts    projects/tap-43-ong-bap-cay-ngoc     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-43-ong-bap-cay-ngoc     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-43-ong-bap-cay-ngoc     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-43-ong-bap-cay-ngoc              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-43-ong-bap-cay-ngoc --force
python scripts/beat_sheet.py projects/tap-43-ong-bap-cay-ngoc               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-43-ong-bap-cay-ngoc/audio/shorts.wav projects/tap-43-ong-bap-cay-ngoc/renders/tap-43-ong-bap-cay-ngoc_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-43-ong-bap-cay-ngoc
python src/episode/pipeline.py seo    projects/tap-43-ong-bap-cay-ngoc
python src/episode/episode_doc.py     projects/tap-43-ong-bap-cay-ngoc
```
