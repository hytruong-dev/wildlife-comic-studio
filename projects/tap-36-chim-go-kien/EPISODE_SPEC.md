# TẬP 36 — CHIM GÕ KIẾN · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-36-chim-go-kien`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-36-chim-go-kien`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F2` · **Persona giọng:** `ky_su_vu_khi` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Chim Gõ Kiến |
| Tiêu đề YouTube | Bản Vẽ Giảm Chấn Hộp Sọ: Đập Đầu 12.000 Lần/Ngày Với Lực 1.200G Nhờ Chiếc Lưỡi Quấn Não?! \| Tập 36 |
| Video dài | `renders/tap-36-chim-go-kien_long.mp4` — 9:18.0 (558.0s) |
| Shorts | `renders/tap-36-chim-go-kien_shorts.mp4` — 0:43.5 (43.5s) |
| Thumbnail | `renders/tap-36-chim-go-kien_thumbnail.jpg` |
| Số hình | dài 70 beat / 70 ảnh riêng; Shorts 12 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.11**, Shorts tempo tự tính (≥ 1.12) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/70 của video YouTube về Chim Gõ Kiến). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách bản vẽ kỹ thuật cơ khí Leonardo Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch & Blueprint): nét bút kim kỹ thuật chuẩn xác từng milimét, các đường nét gạch bóng crosshatch cơ học tinh vi, chi tiết bánh răng đồng thau lộ cơ chế, thước kẹp caliper, vòng đo chấn động shockwave 1200G, sơ đồ vạch kích thước CAD màu nâu mực sepia và xanh lam blueprint kỹ thuật; NỀN TRẮNG TINH hoàn toàn, không watermark, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba. Nhân vật phụ cố định: Kỹ sư Cú Vọ già đeo kính lão tròn đọc tài liệu; Chuột chũi thợ mỏ mặc yếm cầm máy khoan mini; Sóc bay thợ hàn đeo kính đen cầm que hàn; Khỉ đầu chó thanh tra an toàn lao động cầm bảng kẹp hồ sơ. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — BÀI TOÁN GIA TỐC MỘT NGÀN HAI TRĂM G
*Thẻ chương:* KỸ SƯ TRƯỞNG KHỞI ĐỘNG MÁY ĐO GIA TỐC: ĐẬP ĐẦU HAI MƯƠI LẦN MỖI GIÂY VỚI LỰC 1.200G VẪN BÌNH AN VÔ SỰ

*Badge:* `HỒ SƠ THỬ NGHIỆM VA ĐẬP` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene01_p0.wav` (621 ký tự) · mood `hao_hung`

```text
Chào mừng toàn thể các kỹ sư, chuyên gia cơ khí và các bạn đam mê công nghệ vật liệu bước vào Phòng thử nghiệm động lực học va đập của thiên nhiên hoang dã! [laughter] Hôm nay, chúng ta sẽ cùng nhau bóc tách bản vẽ kỹ thuật của một cỗ máy khoan đục kỳ vĩ nhất mà mẹ thiên nhiên từng sáng tạo ra. Đối tượng thí nghiệm trên bàn mổ cơ khí của chúng ta hôm nay mang tên Chim Gõ Kiến, hay được các kỹ sư vũ khí gọi bằng mật danh Cỗ Máy Giảm Chấn Rừng Xanh! Nếu các bạn từng bị va đầu vào cánh cửa tủ bếp và cảm thấy hoa mắt chóng mặt suốt nửa ngày, thì xin hãy chuẩn bị tinh thần để lắng nghe những thông số chấn động sau đây!
```
**Part 1** → `audio/vs/scene01_p1.wav` (89 ký tự) · 🎭 cameo `co_tro_ly`

```text
Báo cáo thông số kỹ thuật: Cảm biến gia tốc ghi nhận va đập đạt đỉnh một ngàn hai trăm G!
```
**Part 2** → `audio/vs/scene01_p2.wav` (718 ký tự) · mood `hao_hung`

```text
[surprise-oh] Một ngàn hai trăm G thưa các đồng nghiệp! Để tôi làm một phép so sánh cơ học cho các bạn dễ hình dung: Một phi công tiêm kích quân sự lão luyện khi thực hiện động tác ngoặt gấp chỉ chịu được tối đa chín G trước khi máu dồn xuống chân và ngất lịm hoàn toàn. Một vụ tai nạn giao thông xe hơi thảm khốc với lực va chạm khoảng một trăm G đã đủ sức làm hộp sọ người vỡ vụn và tử vong ngay tại chỗ! Thế nhưng, Cỗ Máy Giảm Chấn Rừng Xanh của chúng ta đập đầu vào thân gỗ lim cứng như đá với vận tốc hai mươi lăm kilômét trên giờ, tần số hai mươi lần mỗi giây, và lặp lại liên tục mười hai ngàn lần mỗi ngày mà không hề bị xuất huyết não, không choáng váng và cũng chẳng cần uống lấy một viên thuốc giảm đau nào!
```
**Part 3** → `audio/vs/scene01_p3.wav` (418 ký tự) · mood `don_dap`

```text
Nếu các kỹ sư chế tạo xe hơi của loài người áp dụng những tiêu chuẩn an toàn thông thường lên loài chim này, họ chắc chắn sẽ tuyên bố đây là một điều bất khả thi về mặt vật lý. Nhưng đối với thiên nhiên, không có gì là bất khả thi một khi bài toán phân tán xung lực đã được giải quyết bằng bốn tầng giảm chấn cơ học hoàn hảo! Hãy cùng tôi lật giở từng trang bản vẽ giải phẫu để khám phá bí mật kinh thiên động địa này!
```
**Part 4** → `audio/vs/scene01_p4.wav` (342 ký tự) · mood `hao_hung`

```text
Các số liệu đo đạc cho thấy: Mỗi cú va chạm chỉ diễn ra trong vòng chưa đầy một phần ngàn giây. Nhưng lực cản quán tính sinh ra lại tương đương với việc một chiếc xe bọc thép hạng nặng đâm trực diện vào bức tường bê tông cốt thép ở tốc độ tối đa! Sự bền bỉ phi thường này chính là nguồn cảm hứng vô tận cho ngành chế tạo giáp bảo vệ hiện đại!
```

### scene02 — CHIẾC LƯỠI QUẤN QUANH SỌ NÃO NHƯ DÂY ĐAI XE ĐUA
*Thẻ chương:* GIẢI PHÃU HỆ CƠ XƯƠNG HYOID: CHIẾC LƯỠI KỲ LẠ DÀI GẤP BA LẦN MỎ QUẤN TRỌN MỘT VÒNG HỘP SỌ

*Badge:* `LỚP GIẢM CHẤN #1` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene02_p0.wav` (439 ký tự) · mood `tram_bi_an`

```text
Hãy bắt đầu với chi tiết cơ khí kỳ dị và độc nhất vô nhị nhất trong toàn bộ giới động vật có xương sống: Hệ cơ xương móng mang tên Hyoid. Khi nhìn vào chiếc mỏ nhọn hoắt của chim gõ kiến, nhiều người cứ nghĩ rằng chiếc lưỡi bên trong cũng ngắn ngủn như lưỡi của loài gà hay chim sẻ thông thường. [laughter] Nhưng khi các nhà giải phẫu học rạch lớp da đầu của Cỗ Máy Giảm Chấn Rừng Xanh, họ đã hoàn toàn chết lặng trước phát hiện chấn động!
```
**Part 1** → `audio/vs/scene02_p1.wav` (85 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Thưa Kỹ sư trưởng, chiếc lưỡi của nó không nằm trong họng mà chạy ngược lên đỉnh đầu!
```
**Part 2** → `audio/vs/scene02_p2.wav` (550 ký tự) · mood `hao_hung`

```text
[surprise-oh] Quá chính xác thưa trợ lý tập sự! Chiếc lưỡi của chim gõ kiến dài gấp ba lần chiều dài chiếc mỏ của nó. Gốc của chiếc lưỡi không bắt đầu từ cuống họng mà tách ra làm hai nhánh cơ xương đàn hồi, luồn ngược qua phía sau cổ, bò vòng lên tận đỉnh hộp sọ, đi qua giữa hai hốc mắt rồi mới chui tọt vào lỗ mũi bên phải! Các bạn hãy tưởng tượng xem: Toàn bộ hộp sọ chứa bộ não non nớt được ôm chặt lấy bởi một hệ thống dây đai cơ bắp siêu co giãn, hệt như chiếc dây đai an toàn năm điểm của một chiếc xe đua Công thức Một ôm chặt lấy người lái!
```
**Part 3** → `audio/vs/scene02_p3.wav` (409 ký tự) · mood `don_dap`

```text
Trong đúng một phần ngàn giây trước khoảnh khắc chiếc mỏ va chạm vào thân cây gỗ, toàn bộ hệ cơ xương móng Hyoid này lập tức gồng cứng lại và co thắt đồng bộ. Chúng ghìm chặt khối não bộ vào vị trí cố định, triệt tiêu hoàn toàn chuyển động rung lắc quán tính qua lại. Nhờ đó, não bộ của chim gõ kiến không bị đập dội vào thành xương sọ bên trong, loại bỏ hoàn toàn nguy cơ dập não và chấn động nội sọ tử thần!
```
**Part 4** → `audio/vs/scene02_p4.wav` (313 ký tự) · mood `hao_hung`

```text
Chưa dừng lại ở đó, hai nhánh xương móng này còn chứa các sợi gân đàn hồi cực đại có thể kéo dài thêm năm mươi phần trăm chiều dài nghỉ ngơi. Khi chim gõ kiến thò lưỡi sâu vào tổ kiến trong thân cây, hệ thống này đóng vai trò như chiếc cần cẩu thủy lực vươn xa, vừa bắt mồi vừa là hệ thống treo giảm xóc chủ động!
```

### scene03 — VẬT LIỆU XỐP BỌT KHÍ NANO HẤP THỤ CHÍN MƯƠI CHÍN PHẦN TRĂM XUNG LỰC
*Thẻ chương:* BẢN VẼ CẤU TRÚC VẬT LIỆU COMPOSITE: XƯƠNG SỌ ĐỆM KHÍ PHÂN TÁN 99,7% NĂNG LƯỢNG VA ĐẬP THÀNH NHIỆT

*Badge:* `LỚP GIẢM CHẤN #2` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene03_p0.wav` (486 ký tự) · mood `tram_bi_an`

```text
Nếu chiếc dây đai cơ bắp Hyoid đảm nhận vai trò giữ chặt bộ não không bị xô lệch, thì bức tường bảo vệ thứ hai lại nằm ở chính cấu trúc vật liệu làm nên hộp sọ của loài chim này. Ở con người chúng ta, xương sọ là một khối xương đặc cứng và giòn. Khi đầu chúng ta va chạm mạnh, xung lực truyền thẳng qua lớp xương cứng và dội trực tiếp vào mô não mềm mại. Nhưng dưới kính hiển vi điện tử quét nano, hộp sọ của Cỗ Máy Giảm Chấn Rừng Xanh lại là một tuyệt tác vật liệu composite siêu việt!
```
**Part 1** → `audio/vs/scene03_p1.wav` (95 ký tự) · 🎭 cameo `cong_to_vien`

```text
Báo cáo phân tích vật liệu: Xương sọ chứa hàng triệu khoang rỗng xốp xơ xốp như miếng bọt biển!
```
**Part 2** → `audio/vs/scene03_p2.wav` (503 ký tự) · mood `hao_hung`

```text
[laughter] Rất chính xác! Các nhà khoa học tại Đại học Công nghệ Bắc Kinh đã phát hiện xương trán và xương chẩm của chim gõ kiến có cấu trúc xốp dạng tổ ong với mật độ rỗng cực kỳ dày đặc. Lớp xương xốp này hoạt động hệt như lớp đệm cao su giảm chấn hoặc lớp bọt xốp EPS bên trong mũ bảo hiểm cao cấp của các phi hành gia NASA! Khi cú va đập kinh hoàng một ngàn hai trăm G xảy ra, chín mươi chín phẩy bảy phần trăm năng lượng cơ học bị hấp thụ và tiêu tán hoàn toàn bên trong các vi khoang rỗng xốp này!
```
**Part 3** → `audio/vs/scene03_p3.wav` (392 ký tự) · mood `don_dap`

```text
Chỉ có vỏn vẹn không phẩy ba phần trăm năng lượng va đập còn sót lại truyền được tới não bộ! Toàn bộ lượng xung lực khổng lồ bị hấp thụ sẽ chuyển hóa trực tiếp thành nhiệt năng làm nóng hộp sọ lên. Đó chính là lý do vì sao sau mỗi đợt gõ liên hồi hai mươi nhịp, chim gõ kiến bắt buộc phải dừng lại nghỉ vài giây để não bộ tỏa nhiệt làm mát, tránh cho các tế bào thần kinh bị sốt nhiệt cục bộ!
```
**Part 4** → `audio/vs/scene03_p4.wav` (293 ký tự) · mood `hao_hung`

```text
Các mô hình mô phỏng phần tử hữu hạn ba chiều khẳng định: Sự phân bố mật độ xương xốp không hề ngẫu nhiên mà dày đặc nhất tại đúng điểm tiếp nhận véc-tơ lực chính diện. Thiên nhiên đã tối ưu hóa cấu trúc chịu lực này hoàn hảo hơn bất kỳ thuật toán trí tuệ nhân tạo nào của thế kỷ hai mươi mốt!
```

### scene04 — THIẾT KẾ MỎ LỆCH HƯỚNG CHUYỂN DÒNG NĂNG LƯỢNG XUỐNG THÂN
*Thẻ chương:* KỸ THUẬT PHÂN TÁN DÒNG LỰC: HÀM DƯỚI DÀI HƠN HÀM TRÊN DẪN SÓNG XUNG KÍCH VỀ CỘT SỐNG

*Badge:* `LỚP GIẢM CHẤN #3` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene04_p0.wav` (404 ký tự) · mood `tram_bi_an`

```text
Bây giờ, xin mời các kỹ sư chuyển ống kính quan sát xuống bộ phận tiền tuyến chịu trận đầu tiên: Chiếc mỏ nhọn hoắt như mũi đục kim cương. Bằng mắt thường nhìn lướt qua, ai cũng nghĩ hai nửa mỏ trên và mỏ dưới của chim gõ kiến đối xứng hoàn hảo như một chiếc kẹp gắp. [laughter] Nhưng các phép đo đạc ba chiều siêu chính xác bằng máy quét laser công nghiệp đã lật tẩy một bí mật thiết kế cơ khí tài tình!
```
**Part 1** → `audio/vs/scene04_p1.wav` (84 ký tự) · 🎭 cameo `ga_khong_lo`

```text
Ủa Kỹ sư trưởng ơi, tôi đo thấy mỏ dưới của nó dài hơn mỏ trên một đoạn rõ ràng kìa!
```
**Part 2** → `audio/vs/scene04_p2.wav` (483 ký tự) · mood `hao_hung`

```text
[surprise-oh] Mắt nhìn rất chuẩn thưa bác thợ cả! Hàm dưới của chim gõ kiến luôn dài hơn hàm trên và có cấu trúc xương đặc hơn hẳn. Khi chiếc mỏ gõ mạnh vào thân cây gỗ, hàm dưới sẽ chạm vào mặt gỗ trước hàm trên trong một phần triệu giây. Cú va chạm lệch pha này tạo ra một góc bẻ hướng lực sáu mươi độ, hướng toàn bộ sóng xung kích uốn cong đi xuống dưới vòm họng, truyền dọc theo cột sống cổ dày đặc cơ bắp và tiêu tán xuống lồng ngực to lớn, thay vì truyền thẳng băng lên hộp sọ!
```
**Part 3** → `audio/vs/scene04_p3.wav` (336 ký tự) · mood `don_dap`

```text
Chưa hết, lớp vỏ ngoài của mỏ được cấu tạo từ các phiến sừng keratin xếp lớp chồng lên nhau như vảy cá, có khả năng biến dạng đàn hồi để triệt tiêu chấn động trước khi lực truyền vào xương hàm. Đây chính là nguyên mẫu hoàn hảo mà các kỹ sư quân sự hiện đại đã sao chép để chế tạo mũi khoan bê tông và đầu đạn xuyên giáp chống dội ngược!
```
**Part 4** → `audio/vs/scene04_p4.wav` (353 ký tự) · mood `hao_hung`

```text
Hơn thế nữa, các cơ bắp vùng cổ của chim gõ kiến rất nở nang và hoạt động như những pít-tông thủy lực đối trọng. Khi đầu lao về phía trước, cơ cổ co rút với độ chuẩn xác tuyệt đối để giữ quỹ đạo chuyển động thẳng tắp một trăm phần trăm, không bị vặn xoắn sang hai bên — bởi vì lực vặn xoắn mới chính là thủ phạm nguy hiểm nhất gây đứt rách mạch máu não!
```

### scene05 — MÀNG CHỚP MỘT MILI-GIÂY BẢO VỆ NHÃN CẦU KHÔNG VĂNG RA NGOÀI
*Thẻ chương:* TỐC ĐỘ ĐÓNG CỬA CHỚP THẦN TỐC: MÍ MẮT THỨ BA KHÓA CHẶT MẮT TRƯỚC VA CHẠM ĐỂ CHỐNG ÁP SUẤT

*Badge:* `LỚP GIẢM CHẤN #4` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene05_p0.wav` (428 ký tự) · mood `tram_bi_an`

```text
Nếu các bạn nghĩ rằng bảo vệ được bộ não là cỗ máy đã có thể yên tâm vận hành, thì các bạn đã quên mất một chi tiết giải phẫu cực kỳ mỏng manh và nguy hiểm: Đôi mắt! Với gia tốc va chạm một ngàn hai trăm G cùng sự giảm tốc đột ngột trong nháy mắt, áp lực nội nhãn sẽ tăng vọt lên mức khủng khiếp. Nếu là mắt người, nhãn cầu sẽ lập tức văng ra khỏi hốc mắt hoặc bị đứt cuống võng mạc gây mù lòa vĩnh viễn ngay từ cú đập đầu tiên!
```
**Part 1** → `audio/vs/scene05_p1.wav` (85 ký tự) · 🎭 cameo `ong_gia_ke`

```text
Vậy làm sao mà mắt của nó vẫn mở to thao láo nhìn thấy sâu bọ trong hốc cây thưa sếp?
```
**Part 2** → `audio/vs/scene05_p2.wav` (543 ký tự) · mood `hao_hung`

```text
[laughter] Đó là nhờ một công nghệ cảm biến và cửa chập quang học siêu tốc thưa bác già! Chim gõ kiến sở hữu một lớp mí mắt thứ ba trong suốt gọi là màng chớp. Máy quay siêu tốc mười ngàn khung hình trên giây của các nhà khoa học đã ghi lại được: Đúng một mili-giây trước khi mỏ chạm vào gỗ, lớp màng chớp này lập tức sập xuống khóa chặt nhãn cầu vào hốc mắt! Nó hoạt động hệt như một chiếc kính bảo hộ lao động kiêm đai nẹp cơ học, vừa ngăn không cho bụi gỗ bắn vào giác mạc, vừa ghìm chặt nhãn cầu chống lại lực quán tính văng ra phía trước!
```
**Part 3** → `audio/vs/scene05_p3.wav` (309 ký tự) · mood `don_dap`

```text
Và ngay khi cú va chạm kết thúc, trong tích tắc một mili-giây tiếp theo, màng chớp lại tự động mở ra để mắt chim gõ kiến tiếp tục quan sát con mồi đang cựa quậy bên trong thớ gỗ! Toàn bộ chu trình đóng mở thần tốc đó diễn ra hai mươi lần mỗi giây mà mắt thường con người chỉ thấy như một cái chớp nhẹ vô hình!
```
**Part 4** → `audio/vs/scene05_p4.wav` (332 ký tự) · mood `am_ap`

```text
Một hệ thống kiểm soát cơ học tinh vi đến từng phần ngàn giây như vậy đòi hỏi sự đồng bộ hoàn hảo giữa tín hiệu xung thần kinh thị giác và cơ vận nhãn. Không có một hệ thống robot công nghiệp nào hiện nay có thể đạt được độ tin cậy vận hành liên tục mười hai ngàn chu kỳ mỗi ngày mà không xảy ra sai số như đôi mắt của chim gõ kiến!
```

### scene06 — ĐỈNH CAO CƠ CHẾ GIẢM CHẤN PHỎNG SINH HỌC
*Thẻ chương:* BẢN GIAO HƯỞNG CƠ KHÍ HOÀN MỸ: BÀI HỌC VÔ GIÁ MÀ KỸ SƯ LOÀI NGƯỜI ĐANG HỌC TẬP TỪ THIÊN NHIÊN

*Badge:* `NGHIỆM THU CÔNG TRÌNH` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene06_p0.wav` (441 ký tự) · mood `hao_hung`

```text
Thưa toàn thể hội đồng kỹ thuật, sau khi bóc tách toàn bộ bốn tầng giảm chấn từ dây đai an toàn Hyoid quấn quanh sọ, hộp sọ xốp bọt khí nano, chiếc mỏ dẫn dòng lực lệch pha cho đến mí mắt cửa chập một mili-giây, chúng ta phải nghiêng mình ngả mũ trước thiên tài thiết kế của tạo hóa! Cỗ Máy Giảm Chấn Rừng Xanh không chỉ là một loài chim kiếm ăn, mà là một kỳ quan cơ học và là mẫu hình chuẩn mực cho ngành kỹ thuật phỏng sinh học tương lai!
```
**Part 1** → `audio/vs/scene06_p1.wav` (92 ký tự) · 🎭 cameo `tham_phan`

```text
Tuyên bố nghiệm thu: Bản thiết kế chống va đập của Chim Gõ Kiến đạt điểm xuất sắc tuyệt đối!
```
**Part 2** → `audio/vs/scene06_p2.wav` (426 ký tự) · mood `am_ap`

```text
[laughter] Hoàn toàn xứng đáng thưa thẩm phán danh dự! Ngày nay, các kỹ sư vũ trụ của NASA đã ứng dụng cấu trúc hộp sọ chim gõ kiến để chế tạo hộp đen máy bay chịu được va đập cực hạn và các bộ phận tiếp đất của tàu thám hiểm không gian. Các tập đoàn thiết bị thể thao cũng dựa trên hệ cơ xương Hyoid để thiết kế mũ bảo hiểm xe đua Công thức Một và bóng bầu dục nhằm giảm thiểu tối đa chấn thương sọ não cho các vận động viên!
```
**Part 3** → `audio/vs/scene06_p3.wav` (471 ký tự) · mood `don_dap`

```text
Lần tới khi bạn đi dạo trong rừng và nghe thấy tiếng gõ cốc cốc vang dội khắp tán cây, hãy nhớ rằng bạn đang lắng nghe bài ca thử nghiệm va chạm đỉnh cao nhất của hành tinh Trái Đất! Còn bây giờ, giữa chiếc lưỡi quấn quanh sọ và hộp sọ xốp bọt khí tiêu tán xung lực, giải pháp cơ khí nào khiến bạn thán phục nhất? Hãy để lại bình luận bên dưới nhé! Và đừng quên bấm đăng ký kênh để đón xem Tập ba mươi bảy khám phá cỗ máy lọc nước và túi mỡ kỳ diệu của Lạc Đà Sa Mạc nhé!
```
**Part 4** → `audio/vs/scene06_p4.wav` (160 ký tự) · mood `am_ap`

```text
Hãy cùng tôn vinh những kỳ quan kỹ thuật vĩ đại của tự nhiên, nơi mỗi sinh vật đều mang trong mình những giải pháp công nghệ vượt trước thời đại hàng triệu năm!
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Bạn có biết điều gì sẽ xảy ra nếu một con người đập đầu vào thân gỗ với tần số hai mươi lần mỗi giây không? Hộp sọ sẽ vỡ vụn và tử vong ngay tức khắc! [dissatisfaction-hnn] Thế nhưng loài Chim Gõ Kiến lại làm việc đó mười hai ngàn lần mỗi ngày với lực va chạm lên tới một ngàn hai trăm G — gấp một trăm hai mươi lần giới hạn tử vong của con người! Bí mật kinh thiên động địa nằm ở chiếc lưỡi kỳ dị dài gấp ba lần mỏ của nó: Chiếc lưỡi không nằm trong họng mà luồn ngược ra sau gáy, quấn trọn một vòng quanh hộp sọ như chiếc dây đai an toàn xe hơi! Mỗi khi mỏ đập vào gỗ, chiếc lưỡi gồng cứng lại ghìm chặt não bộ không bị rung lắc, kết hợp cùng hộp sọ xốp bọt khí hấp thụ chín mươi chín phẩy bảy phần trăm xung lực thành nhiệt năng! [laughter] Thật là một kỳ quan cơ khí giảm chấn đỉnh cao của rừng xanh!
```

**Whisper prompt:** `Chim Gõ Kiến, Cỗ Máy Giảm Chấn Rừng Xanh, Picidae, Hyoid, 1.200G, giảm chấn hộp sọ, xương móng, sọ xốp bọt khí, mí mắt thứ ba, NASA, F1`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| Tập ba mươi sáu | Tập 36 |
| Tập ba mươi bảy | Tập 37 |
| mười hai ngàn lần | 12.000 lần |
| mười hai ngàn chu kỳ | 12.000 chu kỳ |
| hai mươi lần | 20 lần |
| hai mươi nhịp | 20 nhịp |
| thế kỷ hai mươi mốt | thế kỷ 21 |
| một giây | 1 giây |
| một mili-giây | 1 mili-giây |
| hai mươi lăm kilômét trên giờ | 25 km/h |
| Một ngàn hai trăm | 1.200 |
| một ngàn hai trăm | 1.200 |
| một trăm hai mươi lần | 120 lần |
| một trăm | 100 |
| mười lần | 10 lần |
| mười ngàn khung hình | 10.000 khung hình |
| ba lớp | 3 lớp |
| bốn cơ chế | 4 cơ chế |
| sáu mươi độ | 60° |
| năm mươi phần trăm | 50% |
| chín mươi chín phần trăm | 99% |
| chín mươi chín phẩy bảy phần trăm | 99,7% |
| không phẩy ba phần trăm | 0,3% |
| hàng triệu năm | hàng triệu năm |
| triệu năm | triệu năm |
| Hyoid | Hyoid |
| Picidae | Picidae |
| Black & Decker | Black & Decker |
| NASA | NASA |
| F1 | F1 |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · BÀI TOÁN GIA TỐC MỘT NGÀN HAI TRĂM G · 111.8s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:10.4 (10.4s) | L01 | Chào mừng toàn thể các kỹ sư, chuyên gia cơ khí và các bạn đam mê công nghệ vật liệu bước vào Phòng thử nghiệm động lực học va đập của thiên nhiên hoang dã! Hôm nay, chúng ta sẽ cùng |  | Phòng thử nghiệm cơ khí thiên nhiên hoang dã mở ra: chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba đứng trên bục giảng trước tấm bảng vẽ kỹ thuật blueprint khổng lồ, tay cầm thư |
| b02 | 00:10.4–00:16.0 (5.6s) | L02 | nhau bóc tách bản vẽ kỹ thuật của một cỗ máy khoan đục kỳ vĩ nhất mà mẹ thiên nhiên từng sáng tạo ra. |  | Cận cảnh bàn mổ cơ khí: Bản vẽ giải phẫu chim gõ kiến phóng to với các đường nét blueprint xanh cyan và thông số bánh răng steampunk tinh xảo. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b03 | 00:16.0–00:25.1 (9.1s) | L03 | Đối tượng thí nghiệm trên bàn mổ cơ khí của chúng ta hôm nay mang tên Chim Gõ Kiến, hay được các kỹ sư vũ khí gọi bằng mật danh Cỗ Máy Giảm Chấn Rừng Xanh! Nếu các bạn từng |  | chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba tạo dáng hiên ngang bên cạnh một khúc gỗ sồi cổ thụ dày cộp, chiếc mỏ nhọn lấp lánh như mũi khoan kim cương. |
| b04 | 00:25.1–00:32.4 (7.4s) | L04 | bị va đầu vào cánh cửa tủ bếp và cảm thấy hoa mắt chóng mặt suốt nửa ngày, thì xin hãy chuẩn bị tinh thần để lắng nghe những thông số chấn động sau đây! |  | Một anh chàng người que ngốc nghếch ôm trán nhăn nhó vì đập đầu vào cánh tủ bếp, trên đầu bay vòng vòng mấy ngôi sao choáng váng. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b05 | 00:32.4–00:37.3 (4.9s) | L05 | Báo cáo thông số kỹ thuật: Cảm biến gia tốc ghi nhận va đập đạt đỉnh 1.200 |  | Khỉ đầu chó thanh tra cầm máy đo gia tốc kỹ thuật số, mắt trợn tròn trước màn hình hiển thị số nhảy loạn xạ. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b06 | 00:37.3–00:43.5 (6.2s) | L06 | G! 1.200 G thưa các đồng nghiệp! Để tôi làm một phép so sánh cơ học cho các bạn dễ hình dung: | **1.200 G** · gia tốc va chạm · R/360 · [0.65, 0.45] | Đồng hồ đo áp lực và gia tốc steampunk kim chỉ vạch đỏ rực ở mức cực đại: chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba chỉ tay vào con số 1.200 G với nụ cười tự tin. |
| b07 | 00:43.5–00:51.4 (7.9s) | L07 | Một phi công tiêm kích quân sự lão luyện khi thực hiện động tác ngoặt gấp chỉ chịu được tối đa chín G trước khi máu dồn xuống chân và ngất lịm hoàn toàn. | **9 G** · giới hạn người ngất · L/400 · [0.35, 0.45] | Một phi công thế giới tự nhiên trong buồng lái phản lực bị lực ép dính chặt vào ghế ngồi, khuôn mặt méo mó chịu tải gia tốc 9 G. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b08 | 00:51.4–01:00.6 (9.2s) | L08 | Một vụ tai nạn giao thông xe hơi thảm khốc với lực va chạm khoảng 100 G đã đủ sức làm hộp sọ người vỡ vụn và tử vong ngay tại chỗ! Thế nhưng, Cỗ Máy Giảm Chấn Rừng Xanh của chúng | **100 G** · tai nạn xe hơi tử vong · R/380 · [0.68, 0.42] | Hiện trường thử nghiệm va chạm ô tô crash-test: Đầu xe bẹp dúm khi đâm vào tường bê tông ở vận tốc cao, hình nộm vỡ vụn. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b09 | 01:00.6–01:14.4 (13.8s) | L09 | ta đập đầu vào thân gỗ lim cứng như đá với vận tốc 25 km/h, tần số 20 lần mỗi giây, và lặp lại liên tục 12.000 lần mỗi ngày mà không hề bị xuất huyết não, không choáng váng và cũng chẳng cần uống lấy một viên thuốc giảm đau nào! | **12.000 LẦN** · tần suất đập mỗi ngày · R/370 · [0.65, 0.45] | chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba mổ liên thanh như súng máy vào thân gỗ, tốc độ nhanh đến mức tạo thành vệt mờ chuyển động ngoạn mục. |
| b10 | 01:14.4–01:25.6 (11.2s) | L10 | Nếu các kỹ sư chế tạo xe hơi của loài người áp dụng những tiêu chuẩn an toàn thông thường lên loài chim này, họ chắc chắn sẽ tuyên bố đây là một điều bất khả thi về mặt vật lý. Nhưng đối với thiên nhiên, không có gì là bất khả thi |  | Đồng hồ đếm nhịp cơ khí steampunk nhảy số liên hồi, ghi nhận kỷ lục 12.000 cú đập: chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba vừa đập mỏ vừa huýt sáo thảnh thơi. |
| b11 | 01:25.6–01:38.2 (12.5s) | L11 | một khi bài toán phân tán xung lực đã được giải quyết bằng bốn tầng giảm chấn cơ học hoàn hảo! Hãy cùng tôi lật giở từng trang bản vẽ giải phẫu để khám phá bí mật kinh thiên động địa này! Các số liệu đo đạc cho thấy: Mỗi cú va chạm chỉ diễn ra trong vòng chưa |  | Một chiếc xe bọc thép viễn tưởng bọc lớp vỏ xốp giảm chấn đặc biệt lăn bánh hất tung chướng ngại vật mà không hề móp méo. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b12 | 01:38.2–01:51.8 (13.7s) | L12 | đầy một phần ngàn giây. Nhưng lực cản quán tính sinh ra lại tương đương với việc một chiếc xe bọc thép hạng nặng đâm trực diện vào bức tường bê tông cốt thép ở tốc độ tối đa! Sự bền bỉ phi thường này chính là nguồn cảm hứng vô tận cho ngành chế tạo giáp bảo vệ hiện đại! | **1 MS** · thời gian 1 cú va chạm · L/390 · [0.35, 0.45] | Đồ thị sóng âm và xung lực dao động cực nhanh: chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba đứng bên biểu đồ va chạm một phần ngàn giây siêu ngắn. |

### scene02 · CHIẾC LƯỠI QUẤN QUANH SỌ NÃO NHƯ DÂY ĐAI XE ĐUA · 90.2s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:10.9 (10.9s) | L13 | Hãy bắt đầu với chi tiết cơ khí kỳ dị và độc nhất vô nhị nhất trong toàn bộ giới động vật có xương sống: Hệ cơ xương móng mang tên Hyoid. Khi nhìn vào chiếc mỏ nhọn hoắt của chim gõ kiến, nhiều người cứ nghĩ rằng |  | Bản vẽ bóc tách lớp phòng vệ số 1: Mô hình cơ khí hệ cơ xương móng Hyoid phát sáng màu vàng đồng trên nền giấy blueprint. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b02 | 00:10.9–00:16.5 (5.6s) | L14 | chiếc lưỡi bên trong cũng ngắn ngủn như lưỡi của loài gà hay chim sẻ thông thường. Nhưng khi các nhà giải phẫu |  | Một chú gà con hoạt hình ngơ ngác thè chiếc lưỡi ngắn cũn cỡn ra so sánh với chiếc mỏ dài ngoằng của chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba. |
| b03 | 00:16.5–00:23.4 (6.9s) | L15 | học rạch lớp da đầu của Cỗ Máy Giảm Chấn Rừng Xanh, họ đã hoàn toàn chết lặng trước phát hiện chấn động! Thưa Kỹ sư trưởng, |  | Kỹ sư Cú Vọ già đeo kính lúp soi vào kính hiển vi, hai mắt mở to kinh ngạc tột độ. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b04 | 00:23.4–00:30.6 (7.2s) | L16 | chiếc lưỡi của nó không nằm trong họng mà chạy ngược lên đỉnh đầu! Quá chính xác thưa trợ lý tập sự! Chiếc lưỡi của chim gõ |  | Sóc bay thợ hàn cầm đèn chiếu soi vào bản vẽ sọ não: Lưỡi chạy ngược ra sau gáy kỳ lạ. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b05 | 00:30.6–00:38.7 (8.1s) | L17 | kiến dài gấp ba lần chiều dài chiếc mỏ của nó. Gốc của chiếc lưỡi không bắt đầu từ cuống họng mà tách ra làm hai nhánh cơ xương đàn hồi, luồn ngược qua phía sau cổ, | **GẤP 3 LẦN** · dài gấp 3 lần mỏ · R/370 · [0.68, 0.45] | chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba há mỏ thè chiếc lưỡi dài ngoằng quấn lượn như sợi dây thừng ma thuật khiến muôn loài tròn mắt thán phục. |
| b06 | 00:38.7–00:50.4 (11.7s) | L18 | bò vòng lên tận đỉnh hộp sọ, đi qua giữa hai hốc mắt rồi mới chui tọt vào lỗ mũi bên phải! Các bạn hãy tưởng tượng xem: Toàn bộ hộp sọ chứa bộ não non nớt được ôm chặt lấy bởi một hệ thống dây đai cơ bắp siêu co giãn, hệt như |  | Sơ đồ giải phẫu 3D: Hai nhánh xương móng Hyoid chạy qua lỗ mũi, tách đôi luồn vòng qua đỉnh đầu rồi hợp lại sau gáy. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b07 | 00:50.4–00:54.9 (4.5s) | L19 | chiếc dây đai an toàn năm điểm của một chiếc xe đua Công thức Một ôm chặt lấy người lái! |  | Một tay đua xe công thức 1 ngồi trong buồng lái thắt chặt bộ dây đai an toàn 5 điểm nhiều lớp chắc chắn. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b08 | 00:54.9–01:02.5 (7.6s) | L20 | Trong đúng một phần ngàn giây trước khoảnh khắc chiếc mỏ va chạm vào thân cây gỗ, toàn bộ hệ cơ xương móng Hyoid này lập tức gồng cứng lại và co thắt đồng bộ. |  | Cận cảnh siêu tốc cơ bắp Hyoid thắt chặt: Hệ thống dây chằng co rút khóa chặt khối óc trước khi mỏ chạm gỗ. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b09 | 01:02.5–01:08.5 (6.1s) | L21 | Chúng ghìm chặt khối não bộ vào vị trí cố định, triệt tiêu hoàn toàn chuyển động rung lắc quán tính qua lại. Nhờ đó, não bộ của chim gõ |  | chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba tập trung cao độ, toàn bộ hệ cơ đầu và gáy gồng cứng như một khối thép đúc vững chãi. |
| b10 | 01:08.5–01:16.6 (8.0s) | L22 | kiến không bị đập dội vào thành xương sọ bên trong, loại bỏ hoàn toàn nguy cơ dập não và chấn động nội sọ tử thần! Chưa dừng lại ở đó, hai nhánh xương móng này |  | Hình ảnh so sánh hộp sọ: Bộ não của chim gõ kiến được khóa chặt êm ái, hoàn toàn không có dao động lắc lư. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b11 | 01:16.6–01:21.9 (5.4s) | L23 | còn chứa các sợi gân đàn hồi cực đại có thể kéo dài thêm 50% chiều dài nghỉ ngơi. Khi chim gõ | **50%** · độ dãn gân đàn hồi · L/380 · [0.35, 0.45] | Mô hình lò xo vi mô và sợi cơ đàn hồi giảm chấn steampunk co giãn mềm dẻo như cao su tự nhiên. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b12 | 01:21.9–01:30.2 (8.3s) | L24 | kiến thò lưỡi sâu vào tổ kiến trong thân cây, hệ thống này đóng vai trò như chiếc cần cẩu thủy lực vươn xa, vừa bắt mồi vừa là hệ thống treo giảm xóc chủ động! |  | chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba luồn chiếc lưỡi dẻo dai vào mê cung trong thân cây mục, đầu lưỡi có ngạnh sắc bắt gọn đàn mối béo ngậy. |

### scene03 · VẬT LIỆU XỐP BỌT KHÍ NANO HẤP THỤ CHÍN MƯƠI CHÍN PHẦN TRĂM XUNG LỰC · 88.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.6 (9.6s) | L25 | Nếu chiếc dây đai cơ bắp Hyoid đảm nhận vai trò giữ chặt bộ não không bị xô lệch, thì bức tường bảo vệ thứ hai lại nằm ở chính cấu trúc vật liệu làm nên hộp sọ của loài chim này. Ở con người chúng ta, |  | Bản vẽ bóc tách tầng 2: Hộp sọ chim gõ kiến được chiếu sáng mặt cắt ngang, để lộ lớp cấu trúc xốp bọt khí phức tạp. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b02 | 00:09.6–00:13.1 (3.6s) | L26 | xương sọ là một khối xương đặc cứng và giòn. Khi đầu chúng ta va chạm |  | Mô hình sọ người bằng thạch cao đặc cứng và giòn rụm bị búa gõ nhẹ đã nứt toác một đường. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b03 | 00:13.1–00:17.0 (3.9s) | L27 | mạnh, xung lực truyền thẳng qua lớp xương cứng và dội trực tiếp vào mô não mềm mại. |  | Sóng chấn động màu đỏ rực dội thẳng vào mô não mềm của con người gây chấn động não nghiêm trọng. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b04 | 00:17.0–00:25.7 (8.7s) | L28 | Nhưng dưới kính hiển vi điện tử quét nano, hộp sọ của Cỗ Máy Giảm Chấn Rừng Xanh lại là một tuyệt tác vật liệu composite siêu việt! Báo cáo phân tích vật liệu: Xương |  | chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba chỉnh tiêu cự kính hiển vi nano steampunk, hình ảnh phóng to hàng triệu lần hiện ra trên màn hình tinh thể lỏng. |
| b05 | 00:25.7–00:31.4 (5.7s) | L29 | sọ chứa hàng triệu khoang rỗng xốp xơ xốp như miếng bọt biển! Rất chính xác! Các nhà khoa |  | Cấu trúc vi mô xốp như tổ ong với hàng triệu vi bọt khí nano xếp so le đa hướng cực kỳ tinh vi. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b06 | 00:31.4–00:40.6 (9.2s) | L30 | học tại Đại học Công nghệ Bắc Kinh đã phát hiện xương trán và xương chẩm của chim gõ kiến có cấu trúc xốp dạng tổ ong với mật độ rỗng cực kỳ dày đặc. Lớp xương xốp này hoạt động hệt như |  | Phòng thí nghiệm vật liệu tiên tiến: Các nhà khoa học phân tích biểu đồ hấp thụ xung lực của xương chim gõ kiến. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b07 | 00:40.6–00:49.0 (8.4s) | L31 | lớp đệm cao su giảm chấn hoặc lớp bọt xốp EPS bên trong mũ bảo hiểm cao cấp của các phi hành gia NASA! Khi cú va đập kinh hoàng 1.200 G xảy ra, |  | Khối vật liệu xốp phỏng sinh học đàn hồi ấn xuống rồi bung nở lại nguyên trạng không tì vết. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b08 | 00:49.0–01:01.5 (12.5s) | L32 | 99,7% năng lượng cơ học bị hấp thụ và tiêu tán hoàn toàn bên trong các vi khoang rỗng xốp này! Chỉ có vỏn vẹn 0,3% năng lượng va đập còn sót lại truyền được tới não bộ! Toàn bộ lượng xung lực khổng lồ bị hấp thụ | **99,7%** · xung lực bị hấp thụ · R/360 · [0.65, 0.45]<br>**0,3%** · lực sót lại vào não · L/420 · [0.35, 0.5] | chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba giơ bảng thống kê năng lượng: 99,7% lực va đập bị triệt tiêu, chỉ còn vệt sóng nhỏ xíu 0,3% sót lại. |
| b09 | 01:01.5–01:05.8 (4.3s) | L33 | sẽ chuyển hóa trực tiếp thành nhiệt năng làm nóng hộp sọ lên. Đó chính là lý do vì sao sau mỗi |  | Bản đồ nhiệt hồng ngoại: Đầu của chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba hơi ấm lên màu vàng cam nhẹ khi năng lượng cơ học biến thành nhiệt. |
| b10 | 01:05.8–01:14.2 (8.3s) | L34 | đợt gõ liên hồi 20 nhịp, chim gõ kiến bắt buộc phải dừng lại nghỉ vài giây để não bộ tỏa nhiệt làm mát, tránh cho các tế bào thần kinh bị sốt nhiệt cục bộ! Các | **20 NHỊP** · mỗi đợt gõ liên hồi · R/380 · [0.68, 0.45] | chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba ngừng gõ mỏ, lấy chiếc khăn bông lau mồ hôi trên trán và uống một ngụm nước làm mát máy móc. |
| b11 | 01:14.2–01:23.5 (9.3s) | L35 | mô hình mô phỏng phần tử hữu hạn ba chiều khẳng định: Sự phân bố mật độ xương xốp không hề ngẫu nhiên mà dày đặc nhất tại đúng điểm tiếp nhận véc-tơ lực chính diện. Thiên nhiên |  | Màn hình 3D xoay vòng mô hình hộp sọ với các dải màu phân tích ứng suất uốn và chịu nén tuyệt hảo. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b12 | 01:23.5–01:28.7 (5.2s) | L36 | đã tối ưu hóa cấu trúc chịu lực này hoàn hảo hơn bất kỳ thuật toán trí tuệ nhân tạo nào của thế kỷ 21! |  | Một chiếc mũ bảo hiểm phi hành gia công nghệ cao được thiết kế lớp lót phỏng sinh học mô phỏng xương sọ chim gõ kiến. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |

### scene04 · THIẾT KẾ MỎ LỆCH HƯỚNG CHUYỂN DÒNG NĂNG LƯỢNG XUỐNG THÂN · 84.0s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.1 (9.1s) | L37 | Bây giờ, xin mời các kỹ sư chuyển ống kính quan sát xuống bộ phận tiền tuyến chịu trận đầu tiên: Chiếc mỏ nhọn hoắt như mũi đục kim cương. Bằng mắt thường nhìn lướt qua, ai |  | Ống kính phóng đại zoom thẳng vào chiếc mỏ của chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba: Mũi mỏ sắc lạnh màu xám kim loại với các thước đo micromet bao quanh. |
| b02 | 00:09.1–00:15.7 (6.6s) | L38 | cũng nghĩ hai nửa mỏ trên và mỏ dưới của chim gõ kiến đối xứng hoàn hảo như một chiếc kẹp gắp. Nhưng các phép đo đạc ba chiều siêu chính xác bằng |  | Hình vẽ chiếc kẹp gắp đối xứng đơn giản bị đánh dấu chéo màu đỏ: Sai lầm cơ bản của mắt thường. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b03 | 00:15.7–00:21.9 (6.2s) | L39 | máy quét laser công nghiệp đã lật tẩy một bí mật thiết kế cơ khí tài tình! Ủa Kỹ sư trưởng ơi, tôi |  | Máy chụp cắt lớp và quét laser công nghiệp xoay vòng quanh mỏ chim gõ kiến, bộc lộ sai lệch kích thước bất ngờ. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b04 | 00:21.9–00:33.2 (11.3s) | L40 | đo thấy mỏ dưới của nó dài hơn mỏ trên một đoạn rõ ràng kìa! Mắt nhìn rất chuẩn thưa bác thợ cả! Hàm dưới của chim gõ kiến luôn dài hơn hàm trên và có cấu trúc xương đặc hơn hẳn. Khi chiếc mỏ gõ mạnh vào thân cây gỗ, hàm dưới | **LỆCH PHA** · hàm dưới dài hơn · R/380 · [0.65, 0.45] | Chuột chũi thợ mỏ cầm thước kẹp điện tử đo đạc mỏ dưới dài hơn mỏ trên một đoạn rõ ràng. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b05 | 00:33.2–00:38.4 (5.2s) | L41 | sẽ chạm vào mặt gỗ trước hàm trên trong một phần triệu giây. Cú va chạm lệch pha này tạo |  | Mô phỏng va chạm slow-motion: Hàm dưới chạm mặt gỗ trước phân số giây, bẻ gãy đường truyền lực trực diện. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b06 | 00:38.4–00:52.4 (14.0s) | L42 | ra một góc bẻ hướng lực 60°, hướng toàn bộ sóng xung kích uốn cong đi xuống dưới vòm họng, truyền dọc theo cột sống cổ dày đặc cơ bắp và tiêu tán xuống lồng ngực to lớn, thay vì truyền thẳng băng lên hộp sọ! Chưa hết, lớp vỏ ngoài của mỏ được cấu tạo | **60 ĐỘ** · góc bẻ hướng lực xung · L/390 · [0.35, 0.45] | Sơ đồ véc-tơ lực học màu xanh lam bẻ cong một góc 60 độ, hướng dòng chấn động đi xuống vùng ức và sống lưng. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b07 | 00:52.4–00:59.5 (7.1s) | L43 | từ các phiến sừng keratin xếp lớp chồng lên nhau như vảy cá, có khả năng biến dạng đàn hồi để triệt tiêu chấn động trước khi lực truyền vào xương hàm. Đây |  | Kính hiển vi bóc tách lớp vỏ keratin xếp vảy lợp ngói như áo giáp rồng, trượt nhẹ lên nhau phân tán chấn động. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b08 | 00:59.5–01:06.8 (7.4s) | L44 | chính là nguyên mẫu hoàn hảo mà các kỹ sư quân sự hiện đại đã sao chép để chế tạo mũi khoan bê tông và đầu đạn xuyên giáp chống dội ngược! Hơn thế nữa, |  | Mũi khoan công nghiệp và đầu đạn xuyên giáp hiện đại được rèn theo thiết kế vát góc mỏ chim gõ kiến. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b09 | 01:06.8–01:12.0 (5.2s) | L45 | các cơ bắp vùng cổ của chim gõ kiến rất nở nang và hoạt động như những pít-tông thủy lực đối trọng. Khi |  | chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba gồng cơ bắp vùng cổ cuồn cuộn như lực sĩ thể hình, hai gân cổ nổi rõ khỏe khoắn. |
| b10 | 01:12.0–01:17.5 (5.5s) | L46 | đầu lao về phía trước, cơ cổ co rút với độ chuẩn xác tuyệt đối để giữ quỹ đạo chuyển động thẳng tắp 100 |  | Quỹ đạo chuyển động của mỏ chim gõ kiến: Đường thẳng tắp tuyệt đối như tia laser, không hề có rung lắc phương ngang. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b11 | 01:17.5–01:24.0 (6.5s) | L47 | phần trăm, không bị vặn xoắn sang hai bên — bởi vì lực vặn xoắn mới chính là thủ phạm nguy hiểm nhất gây đứt rách mạch máu não! |  | chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba giơ ngón tay cái số một khẳng định độ chuẩn xác cơ học của đường khoan thẳng hàng. |

### scene05 · MÀNG CHỚP MỘT MILI-GIÂY BẢO VỆ NHÃN CẦU KHÔNG VĂNG RA NGOÀI · 83.8s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.9 (9.9s) | L48 | Nếu các bạn nghĩ rằng bảo vệ được bộ não là cỗ máy đã có thể yên tâm vận hành, thì các bạn đã quên mất một chi tiết giải phẫu cực kỳ mỏng manh và nguy hiểm: Đôi mắt! Với gia tốc va chạm 1.200 G cùng |  | Chi tiết giải phẫu mắt mở ra: Một nhãn cầu lớn long lanh với hệ thống cơ vận nhãn phức tạp bao quanh. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b02 | 00:09.9–00:14.9 (4.9s) | L49 | sự giảm tốc đột ngột trong nháy mắt, áp lực nội nhãn sẽ tăng vọt lên mức khủng khiếp. Nếu là |  | Đồ thị giảm tốc cắm thẳng đứng xuống đáy vực: Biểu tượng áp lực nội nhãn tăng vọt màu đỏ cảnh báo nguy hiểm. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b03 | 00:14.9–00:21.2 (6.4s) | L50 | mắt người, nhãn cầu sẽ lập tức văng ra khỏi hốc mắt hoặc bị đứt cuống võng mạc gây mù lòa vĩnh viễn ngay từ cú đập đầu tiên! Vậy làm |  | Một chiếc kính bơi bị áp lực thổi bung văng ra xa để minh họa thảm họa áp lực va đập. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b04 | 00:21.2–00:27.6 (6.4s) | L51 | sao mà mắt của nó vẫn mở to thao láo nhìn thấy sâu bọ trong hốc cây thưa sếp? Đó là nhờ một công nghệ cảm biến |  | chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba đeo kính bảo hộ kỹ sư, hai mắt sáng quắc chăm chú ngắm sâu bọ bên trong kẽ gỗ. |
| b05 | 00:27.6–00:31.3 (3.6s) | L52 | và cửa chập quang học siêu tốc thưa bác già! Chim gõ kiến sở hữu |  | Mô hình cửa trập ống kính máy ảnh cơ khí steampunk đóng mở xoạch xoạch với tốc độ ánh sáng. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b06 | 00:31.3–00:34.7 (3.4s) | L53 | một lớp mí mắt thứ ba trong suốt gọi là màng chớp. Máy quay siêu |  | Cận cảnh mắt chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba: Lớp màng chớp mỏng dính trong suốt hạ xuống che kín toàn bộ con ngươi. |
| b07 | 00:34.7–00:44.9 (10.2s) | L54 | tốc 10.000 khung hình trên giây của các nhà khoa học đã ghi lại được: Đúng 1 mili-giây trước khi mỏ chạm vào gỗ, lớp màng chớp này lập tức sập xuống khóa chặt nhãn cầu vào hốc mắt! Nó hoạt động hệt | **10.000 FPS** · máy quay siêu tốc · R/380 · [0.65, 0.45] | Máy quay điện ảnh tốc độ siêu cao ghi lại từng mili-giây khoảnh khắc màng chớp hạ xuống trước cú va đập. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b08 | 00:44.9–00:55.1 (10.3s) | L55 | như một chiếc kính bảo hộ lao động kiêm đai nẹp cơ học, vừa ngăn không cho bụi gỗ bắn vào giác mạc, vừa ghìm chặt nhãn cầu chống lại lực quán tính văng ra phía trước! Và ngay khi cú va chạm kết thúc, |  | Màng chớp ngăn chặn mọi vụn gỗ và dăm mùn cưa li ti không thể bắn vào giác mạc. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b09 | 00:55.1–01:03.9 (8.7s) | L56 | trong tích tắc 1 mili-giây tiếp theo, màng chớp lại tự động mở ra để mắt chim gõ kiến tiếp tục quan sát con mồi đang cựa quậy bên trong thớ gỗ! Toàn bộ chu trình đóng mở thần tốc đó diễn | **1 MS** · tốc độ mở màng chớp · L/390 · [0.35, 0.45] | Đồng hồ bấm giờ điện tử đếm 0.001 giây: Màng chớp mở bung ra ngay khi mỏ vừa nảy khỏi mặt gỗ. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b10 | 01:03.9–01:15.9 (12.0s) | L57 | ra 20 lần mỗi giây mà mắt thường con người chỉ thấy như một cái chớp nhẹ vô hình! Một hệ thống kiểm soát cơ học tinh vi đến từng phần ngàn giây như vậy đòi hỏi sự đồng bộ hoàn hảo giữa tín hiệu xung thần kinh thị giác và cơ vận nhãn. Không có một | **20 LẦN/S** · chớp mắt đồng bộ · R/370 · [0.68, 0.45] | chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba chớp mắt lia lịa 20 nhịp một giây đồng bộ hoàn hảo với từng cú gõ mỏ không hề trễ một nhịp. |
| b11 | 01:15.9–01:18.3 (2.4s) | L58 | hệ thống robot công nghiệp nào hiện nay có thể đạt được độ tin |  | Một cánh tay robot công nghiệp hiện đại bị kẹt khớp bánh răng tóe lửa vì quá tải chu kỳ vận hành. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b12 | 01:18.3–01:23.8 (5.5s) | L59 | cậy vận hành liên tục 12.000 chu kỳ mỗi ngày mà không xảy ra sai số như đôi mắt của chim gõ kiến! |  | chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba tự hào lau kính lúp cơ khí, nở nụ cười rạng rỡ của một nhà vô địch bền bỉ. |

### scene06 · ĐỈNH CAO CƠ CHẾ GIẢM CHẤN PHỎNG SINH HỌC · 79.2s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:11.8 (11.8s) | L60 | Thưa toàn thể hội đồng kỹ thuật, sau khi bóc tách toàn bộ bốn tầng giảm chấn từ dây đai an toàn Hyoid quấn quanh sọ, hộp sọ xốp bọt khí nano, chiếc mỏ dẫn dòng lực lệch pha cho đến mí mắt cửa chập 1 mili-giây, |  | Toàn cảnh phòng hội đồng kỹ thuật: Bản vẽ tổng thể 4 tầng giảm chấn của chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba được treo trang trọng ở giữa phòng. |
| b02 | 00:11.8–00:23.2 (11.5s) | L61 | chúng ta phải nghiêng mình ngả mũ trước thiên tài thiết kế của tạo hóa! Cỗ Máy Giảm Chấn Rừng Xanh không chỉ là một loài chim kiếm ăn, mà là một kỳ quan cơ học và là mẫu hình chuẩn mực cho ngành kỹ thuật phỏng sinh học tương lai! |  | Hình ảnh chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba đứng bên cạnh các biểu tượng công nghệ đỉnh cao: Tàu vũ trụ, xe đua và giáp chiến đấu. chú chim kỹ sư hoạt hình đội mũ bả |
| b03 | 00:23.2–00:32.0 (8.7s) | L62 | Tuyên bố nghiệm thu: Bản thiết kế chống va đập của Chim Gõ Kiến đạt điểm xuất sắc tuyệt đối! Hoàn toàn xứng đáng thưa thẩm phán danh dự! Ngày nay, |  | Dấu mộc đỏ đóng 'NGHIỆM THU ĐẠT CHUẨN XUẤT SẮC' cộp xuống bản thiết kế chim gõ kiến. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b04 | 00:32.0–00:40.6 (8.6s) | L63 | các kỹ sư vũ trụ của NASA đã ứng dụng cấu trúc hộp sọ chim gõ kiến để chế tạo hộp đen máy bay chịu được va đập cực hạn và các bộ phận tiếp đất của tàu thám hiểm không gian. |  | Trạm vũ trụ quốc tế và hộp đen tàu con thoi được bọc vật liệu xốp phỏng sinh học chống va đập rơi tự do. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b05 | 00:40.6–00:51.4 (10.8s) | L64 | Các tập đoàn thiết bị thể thao cũng dựa trên hệ cơ xương Hyoid để thiết kế mũ bảo hiểm xe đua Công thức Một và bóng bầu dục nhằm giảm thiểu tối đa chấn thương sọ não cho các vận động viên! Lần tới khi bạn đi dạo trong rừng và |  | Một chiếc mũ bảo hiểm bóng bầu dục và xe đua F1 thế hệ mới gắn đai Hyoid bảo vệ đốt sống cổ tối ưu. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b06 | 00:51.4–00:54.8 (3.4s) | L65 | nghe thấy tiếng gõ cốc cốc vang dội khắp tán cây, hãy nhớ rằng bạn đang lắng |  | Khu rừng nguyên sinh thanh bình buổi sớm mai: Bóng dáng chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba cần mẫn gõ mỏ trên thân cây cổ thụ. |
| b07 | 00:54.8–00:58.6 (3.7s) | L66 | nghe bài ca thử nghiệm va chạm đỉnh cao nhất của hành tinh Trái Đất! Còn bây giờ, |  | Các nốt nhạc cơ khí steampunk và bánh răng vàng bay bổng xung quanh chiếc mỏ thần kỳ của chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba. |
| b08 | 00:58.6–01:01.5 (2.9s) | L67 | giữa chiếc lưỡi quấn quanh sọ và hộp sọ xốp bọt khí tiêu tán xung lực, |  | Mô hình đồ họa tương tác hiển thị lại 2 vũ khí đỉnh cao: Dây đai Hyoid và Hộp sọ xốp bọt khí nano. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b09 | 01:01.5–01:06.0 (4.5s) | L68 | giải pháp cơ khí nào khiến bạn thán phục nhất? Hãy để lại bình luận bên dưới nhé! Và đừng quên |  | chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba cầm bảng vẽ chỉ vào ô bình luận nhấp nháy, mời gọi các kỹ sư cùng thảo luận sôi nổi. |
| b10 | 01:06.0–01:11.7 (5.7s) | L69 | bấm đăng ký kênh để đón xem Tập 37 khám phá cỗ máy lọc nước và túi mỡ kỳ diệu của Lạc Đà Sa Mạc nhé! Hãy |  | Banner giới thiệu bí ẩn của Tập 37: Bóng dáng chú Lạc Đà Sa Mạc bước đi trên cồn cát mênh mông. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này. |
| b11 | 01:11.7–01:19.2 (7.5s) | L70 | cùng tôn vinh những kỳ quan kỹ thuật vĩ đại của tự nhiên, nơi mỗi sinh vật đều mang trong mình những giải pháp công nghệ vượt trước thời đại hàng triệu năm! |  | chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba đứng cùng toàn thể đội ngũ kỹ sư hoang dã vẫy tay chào khán giả với nụ cười tự hào. |

## 5. Phân cảnh Shorts — từng beat

Banner: **CỖ MÁY GIẢM CHẤN / 1.200 G ĐỈNH CAO** · giọng 42.0s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Bạn có biết điều gì sẽ xảy ra nếu một con người đập đầu vào thân gỗ với tần số 20 lần mỗi giây không? | **20 LẦN/S** · tần số đập đầu · R/620 · [0.65, 0.45] |
| s02 | 00:05.6 | S02 | Hộp sọ sẽ vỡ vụn và tử vong ngay tức khắc! |  |
| s03 | 00:08.5 | S03 | Thế nhưng loài Chim Gõ Kiến lại làm việc |  |
| s04 | 00:10.8 | S04 | đó 12.000 lần mỗi ngày với lực va chạm | **12.000 LẦN** · mỗi ngày · R/600 · [0.65, 0.45] |
| s05 | 00:13.8 | S05 | lên tới 1.200 G — | **1.200 G** · gia tốc va chạm · L/620 · [0.35, 0.45] |
| s06 | 00:15.7 | S06 | gấp 120 lần giới hạn tử vong của con người! Bí mật kinh thiên động địa nằm | **120 LẦN** · chịu tải người · R/640 · [0.68, 0.45] |
| s07 | 00:20.0 | S07 | ở chiếc lưỡi kỳ dị dài gấp ba lần mỏ của nó: Chiếc lưỡi không nằm trong họng | **DÀI GẤP 3** · chiều dài lưỡi · L/620 · [0.35, 0.45] |
| s08 | 00:24.0 | S08 | mà luồn ngược ra sau gáy, quấn trọn một vòng quanh hộp sọ như chiếc dây đai an toàn xe hơi! Mỗi khi mỏ đập vào gỗ, chiếc lưỡi gồng cứng |  |
| s09 | 00:30.9 | S09 | lại ghìm chặt não bộ không bị rung lắc, kết |  |
| s10 | 00:33.4 | S10 | hợp cùng hộp sọ xốp bọt khí hấp |  |
| s11 | 00:35.0 | S11 | thụ 99,7% xung lực thành nhiệt năng! Thật | **99,7%** · tiêu tán lực · R/620 · [0.65, 0.45] |
| s12 | 00:39.1 | S12 | là một kỳ quan cơ khí giảm chấn đỉnh cao của rừng xanh! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chào mừng toàn thể các kỹ sư, chuyên gia cơ khí và các bạn đam mê công nghệ vật liệu bước vào Phòng thử nghiệm động lực học va đập của thiên nhiên hoang dã! Hôm nay, chúng ta sẽ cùng nhau". Bố cục: Phòng thử nghiệm cơ khí thiên nhiên hoang dã mở ra: chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba đứng trên bục giảng trước tấm bảng vẽ kỹ thuật blueprint khổng lồ, tay cầm thước chỉ bản vẽ động lực học va đập.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bóc tách bản vẽ kỹ thuật của một cỗ máy khoan đục kỳ vĩ nhất mà mẹ thiên nhiên từng sáng tạo ra.". Bố cục: Cận cảnh bàn mổ cơ khí: Bản vẽ giải phẫu chim gõ kiến phóng to với các đường nét blueprint xanh cyan và thông số bánh răng steampunk tinh xảo. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đối tượng thí nghiệm trên bàn mổ cơ khí của chúng ta hôm nay mang tên Chim Gõ Kiến, hay được các kỹ sư vũ khí gọi bằng mật danh Cỗ Máy Giảm Chấn Rừng Xanh! Nếu các bạn từng bị". Bố cục: chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba tạo dáng hiên ngang bên cạnh một khúc gỗ sồi cổ thụ dày cộp, chiếc mỏ nhọn lấp lánh như mũi khoan kim cương.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "va đầu vào cánh cửa tủ bếp và cảm thấy hoa mắt chóng mặt suốt nửa ngày, thì xin hãy chuẩn bị tinh thần để lắng nghe những thông số chấn động sau đây!". Bố cục: Một anh chàng người que ngốc nghếch ôm trán nhăn nhó vì đập đầu vào cánh tủ bếp, trên đầu bay vòng vòng mấy ngôi sao choáng váng. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo thông số kỹ thuật: Cảm biến gia tốc ghi nhận va đập đạt đỉnh 1.200 G!". Bố cục: Khỉ đầu chó thanh tra cầm máy đo gia tốc kỹ thuật số, mắt trợn tròn trước màn hình hiển thị số nhảy loạn xạ. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "1.200 G thưa các đồng nghiệp! Để tôi làm một phép so sánh cơ học cho các bạn dễ hình dung: Một". Bố cục: Đồng hồ đo áp lực và gia tốc steampunk kim chỉ vạch đỏ rực ở mức cực đại: chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba chỉ tay vào con số 1.200 G với nụ cười tự tin.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "phi công tiêm kích thế giới tự nhiên lão luyện khi thực hiện động tác ngoặt gấp chỉ chịu được tối đa chín G trước khi nước màu dồn xuống chân và ngất lịm hoàn toàn. Một vụ". Bố cục: Một phi công thế giới tự nhiên trong buồng lái phản lực bị lực ép dính chặt vào ghế ngồi, khuôn mặt méo mó chịu tải gia tốc 9 G. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tai nạn giao thông xe hơi thảm khốc với lực va chạm khoảng 100 G đã đủ sức làm hộp sọ người vỡ vụn và tử vong ngay tại chỗ! Thế nhưng, Cỗ Máy Giảm Chấn Rừng Xanh của chúng ta". Bố cục: Hiện trường thử nghiệm va chạm ô tô crash-test: Đầu xe bẹp dúm khi đâm vào tường bê tông ở vận tốc cao, hình nộm vỡ vụn. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "đập đầu vào thân gỗ lim cứng như đá với vận tốc 25 km/h, tần số 20 lần mỗi giây, và lặp lại liên tục 12.000 lần mỗi ngày mà không hề bị xuất huyết não, không choáng váng và cũng chẳng cần uống lấy một viên thuốc giảm đau nào!". Bố cục: chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba mổ liên thanh như súng máy vào thân gỗ, tốc độ nhanh đến mức tạo thành vệt mờ chuyển động ngoạn mục.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu các kỹ sư chế tạo xe hơi của loài người áp dụng những tiêu chuẩn an toàn thông thường lên loài chim này, họ chắc chắn sẽ tuyên bố đây là một điều bất khả thi về mặt vật lý. Nhưng đối với thiên nhiên, không có gì là bất khả thi một khi". Bố cục: Đồng hồ đếm nhịp cơ khí steampunk nhảy số liên hồi, ghi nhận kỷ lục 12.000 cú đập: chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba vừa đập mỏ vừa huýt sáo thảnh thơi.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bài toán phân tán xung lực đã được giải quyết bằng bốn tầng giảm chấn cơ học hoàn hảo! Hãy cùng tôi lật giở từng trang bản vẽ giải phẫu để khám phá bí mật kinh thiên động địa này! Các số liệu đo đạc cho thấy: Mỗi cú va chạm chỉ diễn ra trong vòng chưa đầy". Bố cục: Một chiếc xe bọc thép viễn tưởng bọc lớp vỏ xốp giảm chấn đặc biệt lăn bánh hất tung chướng ngại vật mà không hề móp méo. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "một phần ngàn giây. Nhưng lực cản quán tính sinh ra lại tương đương với việc một chiếc xe bọc thép hạng nặng đâm trực diện vào bức tường bê tông cốt thép ở tốc độ tối đa! Sự bền bỉ phi thường này chính là nguồn cảm hứng vô tận cho ngành chế tạo giáp bảo vệ hiện đại!". Bố cục: Đồ thị sóng âm và xung lực dao động cực nhanh: chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba đứng bên biểu đồ va chạm một phần ngàn giây siêu ngắn.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy bắt đầu với chi tiết cơ khí kỳ dị và độc nhất vô nhị nhất trong toàn bộ giới động vật có xương sống: Hệ cơ xương móng mang tên Hyoid. Khi nhìn vào chiếc mỏ nhọn hoắt của chim gõ kiến, nhiều người cứ nghĩ rằng chiếc". Bố cục: Bản vẽ bóc tách lớp phòng vệ số 1: Mô hình cơ khí hệ cơ xương móng Hyoid phát sáng màu vàng đồng trên nền giấy blueprint. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "lưỡi bên trong cũng ngắn ngủn như lưỡi của loài gà hay chim sẻ thông thường. Nhưng khi các nhà giải phẫu học". Bố cục: Một chú gà con hoạt hình ngơ ngác thè chiếc lưỡi ngắn cũn cỡn ra so sánh với chiếc mỏ dài ngoằng của chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "rạch lớp da đầu của Cỗ Máy Giảm Chấn Rừng Xanh, họ đã hoàn toàn chết lặng trước phát hiện chấn động! Thưa Kỹ sư trưởng,". Bố cục: Kỹ sư Cú Vọ già đeo kính lúp soi vào kính hiển vi, hai mắt mở to kinh ngạc tột độ. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chiếc lưỡi của nó không nằm trong họng mà chạy ngược lên đỉnh đầu! Quá chính xác thưa trợ lý tập sự! Chiếc lưỡi của chim gõ kiến". Bố cục: Sóc bay thợ hàn cầm đèn chiếu soi vào bản vẽ sọ não: Lưỡi chạy ngược ra sau gáy kỳ lạ. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "dài gấp ba lần chiều dài chiếc mỏ của nó. Gốc của chiếc lưỡi không bắt đầu từ cuống họng mà tách ra làm hai nhánh cơ xương đàn hồi, luồn ngược qua phía sau cổ,". Bố cục: chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba há mỏ thè chiếc lưỡi dài ngoằng quấn lượn như sợi dây thừng ma thuật khiến muôn loài tròn mắt thán phục.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bò vòng lên tận đỉnh hộp sọ, đi qua giữa hai hốc mắt rồi mới chui tọt vào lỗ mũi bên phải! Các bạn hãy tưởng tượng xem: Toàn bộ hộp sọ chứa bộ não non nớt được ôm chặt lấy bởi một hệ thống dây đai cơ bắp siêu co giãn, hệt như chiếc". Bố cục: Sơ đồ giải phẫu 3D: Hai nhánh xương móng Hyoid chạy qua lỗ mũi, tách đôi luồn vòng qua đỉnh đầu rồi hợp lại sau gáy. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "dây đai an toàn năm điểm của một chiếc xe đua Công thức Một ôm chặt lấy người lái!". Bố cục: Một tay đua xe công thức 1 ngồi trong buồng lái thắt chặt bộ dây đai an toàn 5 điểm nhiều lớp chắc chắn. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong đúng một phần ngàn giây trước khoảnh khắc chiếc mỏ va chạm vào thân cây gỗ, toàn bộ hệ cơ xương móng Hyoid này lập tức gồng cứng lại và co thắt đồng bộ. Chúng". Bố cục: Cận cảnh siêu tốc cơ bắp Hyoid thắt chặt: Hệ thống dây chằng co rút khóa chặt khối óc trước khi mỏ chạm gỗ. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "ghìm chặt khối não bộ vào vị trí cố định, triệt tiêu hoàn toàn chuyển động rung lắc quán tính qua lại. Nhờ đó, não bộ của chim gõ kiến". Bố cục: chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba tập trung cao độ, toàn bộ hệ cơ đầu và gáy gồng cứng như một khối thép đúc vững chãi.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "không bị đập dội vào thành xương sọ bên trong, loại bỏ hoàn toàn nguy cơ dập não và chấn động nội sọ tử thần! Chưa dừng lại ở đó, hai nhánh xương móng này còn". Bố cục: Hình ảnh so sánh hộp sọ: Bộ não của chim gõ kiến được khóa chặt êm ái, hoàn toàn không có dao động lắc lư. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chứa các sợi gân đàn hồi cực đại có thể kéo dài thêm 50% chiều dài nghỉ ngơi. Khi chim gõ kiến". Bố cục: Mô hình lò xo vi mô và sợi cơ đàn hồi giảm chấn steampunk co giãn mềm dẻo như cao su tự nhiên. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "thò lưỡi sâu vào tổ kiến trong thân cây, hệ thống này đóng vai trò như chiếc cần cẩu thủy lực vươn xa, vừa bắt mồi vừa là hệ thống treo giảm xóc chủ động!". Bố cục: chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba luồn chiếc lưỡi dẻo dai vào mê cung trong thân cây mục, đầu lưỡi có ngạnh sắc bắt gọn đàn mối béo ngậy.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu chiếc dây đai cơ bắp Hyoid đảm nhận vai trò giữ chặt bộ não không bị xô lệch, thì bức tường bảo vệ thứ hai lại nằm ở chính cấu trúc vật liệu làm nên hộp sọ của loài chim này. Ở con người chúng ta,". Bố cục: Bản vẽ bóc tách tầng 2: Hộp sọ chim gõ kiến được chiếu sáng mặt cắt ngang, để lộ lớp cấu trúc xốp bọt khí phức tạp. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "xương sọ là một khối xương đặc cứng và giòn. Khi đầu chúng ta va chạm mạnh,". Bố cục: Mô hình sọ người bằng thạch cao đặc cứng và giòn rụm bị búa gõ nhẹ đã nứt toác một đường. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "xung lực truyền thẳng qua lớp xương cứng và dội trực tiếp vào mô não mềm mại. Nhưng". Bố cục: Sóng chấn động màu đỏ rực dội thẳng vào mô não mềm của con người gây chấn động não nghiêm trọng. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "dưới kính hiển vi điện tử quét nano, hộp sọ của Cỗ Máy Giảm Chấn Rừng Xanh lại là một tuyệt tác vật liệu composite siêu việt! Báo cáo phân tích vật liệu: Xương sọ". Bố cục: chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba chỉnh tiêu cự kính hiển vi nano steampunk, hình ảnh phóng to hàng triệu lần hiện ra trên màn hình tinh thể lỏng.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chứa hàng triệu khoang rỗng xốp xơ xốp như miếng bọt biển! Rất chính xác! Các nhà khoa học tại". Bố cục: Cấu trúc vi mô xốp như tổ ong với hàng triệu vi bọt khí nano xếp so le đa hướng cực kỳ tinh vi. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đại học Công nghệ Bắc Kinh đã phát hiện xương trán và xương chẩm của chim gõ kiến có cấu trúc xốp dạng tổ ong với mật độ rỗng cực kỳ dày đặc. Lớp xương xốp này hoạt động hệt như lớp". Bố cục: Phòng thí nghiệm vật liệu tiên tiến: Các nhà khoa học phân tích biểu đồ hấp thụ xung lực của xương chim gõ kiến. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "đệm cao su giảm chấn hoặc lớp bọt xốp EPS bên trong mũ bảo hiểm cao cấp của các phi hành gia NASA! Khi cú va đập kinh hoàng 1.200 G xảy ra,". Bố cục: Khối vật liệu xốp phỏng sinh học đàn hồi ấn xuống rồi bung nở lại nguyên trạng không tì vết. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "99,7% năng lượng cơ học bị hấp thụ và tiêu tán hoàn toàn bên trong các vi khoang rỗng xốp này! Chỉ có vỏn vẹn 0,3% năng lượng va đập còn sót lại truyền được tới não bộ! Toàn bộ lượng xung lực khổng lồ bị hấp thụ sẽ". Bố cục: chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba giơ bảng thống kê năng lượng: 99,7% lực va đập bị triệt tiêu, chỉ còn vệt sóng nhỏ xíu 0,3% sót lại.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chuyển hóa trực tiếp thành nhiệt năng làm nóng hộp sọ lên. Đó chính là lý do vì sao sau mỗi đợt". Bố cục: Bản đồ nhiệt hồng ngoại: Đầu của chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba hơi ấm lên màu vàng cam nhẹ khi năng lượng cơ học biến thành nhiệt.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "gõ liên hồi 20 nhịp, chim gõ kiến bắt buộc phải dừng lại nghỉ vài giây để não bộ tỏa nhiệt làm mát, tránh cho các tế bào thần kinh bị sốt nhiệt cục bộ! Các mô hình". Bố cục: chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba ngừng gõ mỏ, lấy chiếc khăn bông lau mồ hôi trên trán và uống một ngụm nước làm mát máy móc.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "mô phỏng phần tử hữu hạn ba chiều khẳng định: Sự phân bố mật độ xương xốp không hề ngẫu nhiên mà dày đặc nhất tại đúng điểm tiếp nhận véc-tơ lực chính diện. Thiên nhiên đã". Bố cục: Màn hình 3D xoay vòng mô hình hộp sọ với các dải màu phân tích ứng suất uốn và chịu nén tuyệt hảo. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tối ưu hóa cấu trúc chịu lực này hoàn hảo hơn bất kỳ thuật toán trí tuệ nhân tạo nào của thế kỷ 21!". Bố cục: Một chiếc mũ bảo hiểm phi hành gia công nghệ cao được thiết kế lớp lót phỏng sinh học mô phỏng xương sọ chim gõ kiến. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bây giờ, xin mời các kỹ sư chuyển ống kính quan sát xuống bộ phận tiền tuyến chịu trận đầu tiên: Chiếc mỏ nhọn hoắt như mũi đục kim cương. Bằng mắt thường nhìn lướt qua, ai cũng nghĩ". Bố cục: Ống kính phóng đại zoom thẳng vào chiếc mỏ của chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba: Mũi mỏ sắc lạnh màu xám kim loại với các thước đo micromet bao quanh.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "hai nửa mỏ trên và mỏ dưới của chim gõ kiến đối xứng hoàn hảo như một chiếc kẹp gắp. Nhưng các phép đo đạc ba chiều siêu chính xác bằng". Bố cục: Hình vẽ chiếc kẹp gắp đối xứng đơn giản bị đánh dấu chéo màu đỏ: Sai lầm cơ bản của mắt thường. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "máy quét laser công nghiệp đã lật tẩy một bí mật thiết kế cơ khí tài tình! Ủa Kỹ sư trưởng ơi, tôi đo thấy". Bố cục: Máy chụp cắt lớp và quét laser công nghiệp xoay vòng quanh mỏ chim gõ kiến, bộc lộ sai lệch kích thước bất ngờ. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "mỏ dưới của nó dài hơn mỏ trên một đoạn rõ ràng kìa! Mắt nhìn rất chuẩn thưa bác thợ cả! Hàm dưới của chim gõ kiến luôn dài hơn hàm trên và có cấu trúc xương đặc hơn hẳn. Khi chiếc mỏ gõ mạnh vào thân cây gỗ, hàm dưới sẽ". Bố cục: Chuột chũi thợ mỏ cầm thước kẹp điện tử đo đạc mỏ dưới dài hơn mỏ trên một đoạn rõ ràng. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chạm vào mặt gỗ trước hàm trên trong một phần triệu giây. Cú va chạm lệch pha này tạo ra một". Bố cục: Mô phỏng va chạm slow-motion: Hàm dưới chạm mặt gỗ trước phân số giây, bẻ gãy đường truyền lực trực diện. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "góc bẻ hướng lực 60°, hướng toàn bộ sóng xung kích uốn cong đi xuống dưới vòm họng, truyền dọc theo cột sống cổ dày đặc cơ bắp và tiêu tán xuống lồng ngực to lớn, thay vì truyền thẳng băng lên hộp sọ! Chưa hết, lớp vỏ ngoài của mỏ được cấu tạo từ các". Bố cục: Sơ đồ véc-tơ lực học màu xanh lam bẻ cong một góc 60 độ, hướng dòng chấn động đi xuống vùng ức và sống lưng. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "phiến sừng keratin xếp lớp chồng lên nhau như vảy cá, có khả năng biến dạng đàn hồi để triệt tiêu chấn động trước khi lực truyền vào xương hàm. Đây chính là". Bố cục: Kính hiển vi bóc tách lớp vỏ keratin xếp vảy lợp ngói như áo giáp rồng, trượt nhẹ lên nhau phân tán chấn động. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nguyên mẫu hoàn hảo mà các kỹ sư thế giới tự nhiên hiện đại đã sao chép để chế tạo mũi khoan bê tông và đầu đạn xuyên giáp chống dội ngược! Hơn thế nữa, các". Bố cục: Mũi khoan công nghiệp và đầu đạn xuyên giáp hiện đại được rèn theo thiết kế vát góc mỏ chim gõ kiến. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "cơ bắp vùng cổ của chim gõ kiến rất nở nang và hoạt động như những pít-tông thủy lực đối trọng. Khi đầu". Bố cục: chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba gồng cơ bắp vùng cổ cuồn cuộn như lực sĩ thể hình, hai gân cổ nổi rõ khỏe khoắn.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "lao về phía trước, cơ cổ co rút với độ chuẩn xác tuyệt đối để giữ quỹ đạo chuyển động thẳng tắp 100 phần trăm,". Bố cục: Quỹ đạo chuyển động của mỏ chim gõ kiến: Đường thẳng tắp tuyệt đối như tia laser, không hề có rung lắc phương ngang. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "không bị vặn xoắn sang hai bên — bởi vì lực vặn xoắn mới chính là thủ phạm nguy hiểm nhất gây đứt rách mạch nước màu não!". Bố cục: chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba giơ ngón tay cái số một khẳng định độ chuẩn xác cơ học của đường khoan thẳng hàng.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu các bạn nghĩ rằng bảo vệ được bộ não là cỗ máy đã có thể yên tâm vận hành, thì các bạn đã quên mất một chi tiết giải phẫu cực kỳ mỏng manh và nguy hiểm: Đôi mắt! Với gia tốc va chạm 1.200 G cùng sự". Bố cục: Chi tiết giải phẫu mắt mở ra: Một nhãn cầu lớn long lanh với hệ thống cơ vận nhãn phức tạp bao quanh. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "giảm tốc đột ngột trong nháy mắt, áp lực nội nhãn sẽ tăng vọt lên mức khủng khiếp. Nếu là mắt người,". Bố cục: Đồ thị giảm tốc cắm thẳng đứng xuống đáy vực: Biểu tượng áp lực nội nhãn tăng vọt màu đỏ cảnh báo nguy hiểm. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nhãn cầu sẽ lập tức văng ra khỏi hốc mắt hoặc bị đứt cuống võng mạc gây mù lòa vĩnh viễn ngay từ cú đập đầu tiên! Vậy làm sao mà". Bố cục: Một chiếc kính bơi bị áp lực thổi bung văng ra xa để minh họa thảm họa áp lực va đập. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "mắt của nó vẫn mở to thao láo nhìn thấy sâu bọ trong hốc cây thưa sếp? Đó là nhờ một công nghệ cảm biến và". Bố cục: chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba đeo kính bảo hộ kỹ sư, hai mắt sáng quắc chăm chú ngắm sâu bọ bên trong kẽ gỗ.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "cửa chập quang học siêu tốc thưa bác già! Chim gõ kiến sở hữu một lớp". Bố cục: Mô hình cửa trập ống kính máy ảnh cơ khí steampunk đóng mở xoạch xoạch với tốc độ ánh sáng. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "mí mắt thứ ba trong suốt gọi là màng chớp. Máy quay siêu tốc". Bố cục: Cận cảnh mắt chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba: Lớp màng chớp mỏng dính trong suốt hạ xuống che kín toàn bộ con ngươi.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "10.000 khung hình trên giây của các nhà khoa học đã ghi lại được: Đúng 1 mili-giây trước khi mỏ chạm vào gỗ, lớp màng chớp này lập tức sập xuống khóa chặt nhãn cầu vào hốc mắt! Nó hoạt động hệt như một". Bố cục: Máy quay điện ảnh tốc độ siêu cao ghi lại từng mili-giây khoảnh khắc màng chớp hạ xuống trước cú va đập. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chiếc kính bảo hộ lao động kiêm đai nẹp cơ học, vừa ngăn không cho bụi gỗ bắn vào giác mạc, vừa ghìm chặt nhãn cầu chống lại lực quán tính văng ra phía trước! Và ngay khi cú va chạm kết thúc,". Bố cục: Màng chớp ngăn chặn mọi vụn gỗ và dăm mùn cưa li ti không thể bắn vào giác mạc. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "trong tích tắc 1 mili-giây tiếp theo, màng chớp lại tự động mở ra để mắt chim gõ kiến tiếp tục quan sát con mồi đang cựa quậy bên trong thớ gỗ! Toàn bộ chu trình đóng mở thần tốc đó diễn ra". Bố cục: Đồng hồ bấm giờ điện tử đếm 0.001 giây: Màng chớp mở bung ra ngay khi mỏ vừa nảy khỏi mặt gỗ. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L57</summary>

```text
HÌNH L57 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "20 lần mỗi giây mà mắt thường con người chỉ thấy như một cái chớp nhẹ vô hình! Một hệ thống kiểm soát cơ học tinh vi đến từng phần ngàn giây như vậy đòi hỏi sự đồng bộ hoàn hảo giữa tín hiệu xung thần kinh thị giác và cơ vận nhãn. Không có một hệ thống". Bố cục: chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba chớp mắt lia lịa 20 nhịp một giây đồng bộ hoàn hảo với từng cú gõ mỏ không hề trễ một nhịp.
```
</details>

<details><summary>L58</summary>

```text
HÌNH L58 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "robot công nghiệp nào hiện nay có thể đạt được độ tin cậy". Bố cục: Một cánh tay robot công nghiệp hiện đại bị kẹt khớp bánh răng tóe lửa vì quá tải chu kỳ vận hành. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L59</summary>

```text
HÌNH L59 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "vận hành liên tục 12.000 chu kỳ mỗi ngày mà không xảy ra sai số như đôi mắt của chim gõ kiến!". Bố cục: chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba tự hào lau kính lúp cơ khí, nở nụ cười rạng rỡ của một nhà vô địch bền bỉ.
```
</details>

<details><summary>L60</summary>

```text
HÌNH L60 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thưa toàn thể hội đồng kỹ thuật, sau khi bóc tách toàn bộ bốn tầng giảm chấn từ dây đai an toàn Hyoid quấn quanh sọ, hộp sọ xốp bọt khí nano, chiếc mỏ dẫn dòng lực lệch pha cho đến mí mắt cửa chập 1 mili-giây,". Bố cục: Toàn cảnh phòng hội đồng kỹ thuật: Bản vẽ tổng thể 4 tầng giảm chấn của chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba được treo trang trọng ở giữa phòng.
```
</details>

<details><summary>L61</summary>

```text
HÌNH L61 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chúng ta phải nghiêng mình ngả mũ trước thiên tài thiết kế của tạo hóa! Cỗ Máy Giảm Chấn Rừng Xanh không chỉ là một loài chim kiếm ăn, mà là một kỳ quan cơ học và là mẫu hình chuẩn mực cho ngành kỹ thuật phỏng sinh học tương lai!". Bố cục: Hình ảnh chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba đứng bên cạnh các biểu tượng công nghệ đỉnh cao: Tàu vũ trụ, xe đua và giáp chiến đấu. chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk.
```
</details>

<details><summary>L62</summary>

```text
HÌNH L62 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyên bố nghiệm thu: Bản thiết kế chống va đập của Chim Gõ Kiến đạt điểm xuất sắc tuyệt đối! Hoàn toàn xứng đáng thưa thẩm phán danh dự! Ngày nay, các". Bố cục: Dấu mộc đỏ đóng 'NGHIỆM THU ĐẠT CHUẨN XUẤT SẮC' cộp xuống bản thiết kế chim gõ kiến. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L63</summary>

```text
HÌNH L63 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "kỹ sư vũ trụ của NASA đã ứng dụng cấu trúc hộp sọ chim gõ kiến để chế tạo hộp đen máy bay chịu được va đập cực hạn và các bộ phận tiếp đất của tàu thám hiểm không gian. Các". Bố cục: Trạm vũ trụ quốc tế và hộp đen tàu con thoi được bọc vật liệu xốp phỏng sinh học chống va đập rơi tự do. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L64</summary>

```text
HÌNH L64 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tập đoàn thiết bị thể thao cũng dựa trên hệ cơ xương Hyoid để thiết kế mũ bảo hiểm xe đua Công thức Một và bóng bầu dục nhằm giảm thiểu tối đa chấn thương sọ não cho các vận động viên! Lần tới khi bạn đi dạo trong rừng và nghe thấy". Bố cục: Một chiếc mũ bảo hiểm bóng bầu dục và xe đua F1 thế hệ mới gắn đai Hyoid bảo vệ đốt sống cổ tối ưu. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L65</summary>

```text
HÌNH L65 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tiếng gõ cốc cốc vang dội khắp tán cây, hãy nhớ rằng bạn đang lắng nghe". Bố cục: Khu rừng nguyên sinh thanh bình buổi sớm mai: Bóng dáng chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba cần mẫn gõ mỏ trên thân cây cổ thụ.
```
</details>

<details><summary>L66</summary>

```text
HÌNH L66 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bài ca thử nghiệm va chạm đỉnh cao nhất của hành tinh Trái Đất! Còn bây giờ, giữa". Bố cục: Các nốt nhạc cơ khí steampunk và bánh răng vàng bay bổng xung quanh chiếc mỏ thần kỳ của chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba.
```
</details>

<details><summary>L67</summary>

```text
HÌNH L67 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chiếc lưỡi quấn quanh sọ và hộp sọ xốp bọt khí tiêu tán xung lực,". Bố cục: Mô hình đồ họa tương tác hiển thị lại 2 vũ khí đỉnh cao: Dây đai Hyoid và Hộp sọ xốp bọt khí nano. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L68</summary>

```text
HÌNH L68 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "giải pháp cơ khí nào khiến bạn thán phục nhất? Hãy để lại bình luận bên dưới nhé! Và đừng quên". Bố cục: chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba cầm bảng vẽ chỉ vào ô bình luận nhấp nháy, mời gọi các kỹ sư cùng thảo luận sôi nổi.
```
</details>

<details><summary>L69</summary>

```text
HÌNH L69 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bấm đăng ký kênh để đón xem Tập 37 khám phá cỗ máy lọc nước và túi mỡ kỳ diệu của Lạc Đà Sa Mạc nhé! Hãy cùng". Bố cục: Banner giới thiệu bí ẩn của Tập 37: Bóng dáng chú Lạc Đà Sa Mạc bước đi trên cồn cát mênh mông. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>L70</summary>

```text
HÌNH L70 (16:9 ngang, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tôn vinh những kỳ quan kỹ thuật vĩ đại của tự nhiên, nơi mỗi sinh vật đều mang trong mình những giải pháp công nghệ vượt trước thời đại hàng triệu năm!". Bố cục: chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba đứng cùng toàn thể đội ngũ kỹ sư hoang dã vẫy tay chào khán giả với nụ cười tự hào.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Bạn có biết điều gì sẽ xảy ra nếu một con người đập đầu vào thân gỗ với tần số 20 lần mỗi giây không?". Bố cục: Cận cảnh anh chàng người que ngốc nghếch đập đầu vào thân gỗ với tần số cực nhanh, mắt nổ đom đóm.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Hộp sọ sẽ vỡ vụn và tử vong ngay tức khắc!". Bố cục: Mô hình sọ người vỡ vụn từng mảnh với tia sét chấn động đỏ rực cảnh báo tử vong ngay tức khắc. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Thế nhưng loài Chim Gõ Kiến lại làm việc đó". Bố cục: chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba xuất hiện oai phong lẫm liệt, đội mũ kỹ sư tí hon và đeo kính lúp cơ khí steampunk một mắt.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "12.000 lần mỗi ngày với lực va chạm lên tới". Bố cục: chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba gõ mỏ liên thanh như súng máy cơ khí vào thân gỗ sồi, đồng hồ đếm số nhảy vọt lên mười hai ngàn lần.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "1.200 G — gấp". Bố cục: Đồng hồ đo gia tốc rung lắc dữ dội kim chỉ vạch đỏ rực 1.200 G cực hạn: chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba vẫn nháy mắt thảnh thơi.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "120 lần giới hạn tử vong của con người! Bí mật kinh thiên động địa nằm ở". Bố cục: Cột mốc so sánh lực va đập: Con người gục ngã ở 10 G trong khi chim gõ kiến đứng hiên ngang ở đỉnh 1.200 G. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "chiếc lưỡi kỳ dị dài gấp ba lần mỏ của nó: Chiếc lưỡi không nằm trong họng mà". Bố cục: chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba há mỏ phóng ra chiếc lưỡi dài ngoằng uốn lượn kỳ ảo gấp 3 lần mỏ của mình.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "luồn ngược ra sau gáy, quấn trọn một vòng quanh hộp sọ như chiếc dây đai an toàn xe hơi! Mỗi khi mỏ đập vào gỗ, chiếc lưỡi gồng cứng lại". Bố cục: Mặt cắt sọ 3D: Chiếc lưỡi tách đôi luồn vòng quanh hộp sọ như chiếc đai an toàn xe đua chuyên nghiệp. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>S09</summary>

```text
HÌNH S09 (DỌC 9:16, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "ghìm chặt não bộ không bị rung lắc, kết hợp cùng". Bố cục: Toàn bộ hệ cơ bắp đầu và cổ gồng cứng khóa chặt bộ não nằm im thin thít không hề rung rơ một ly. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>S10</summary>

```text
HÌNH S10 (DỌC 9:16, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "hộp sọ xốp bọt khí hấp thụ". Bố cục: Kính hiển vi bóc tách vật liệu nano xốp bọt khí của hộp sọ đang hấp thụ sóng chấn động. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>S11</summary>

```text
HÌNH S11 (DỌC 9:16, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "99,7% xung lực thành nhiệt năng! Thật là một". Bố cục: Toàn bộ 99,7% xung lực va chạm cơ học chuyển hóa lập tức thành nhiệt năng tỏa ra êm dịu. KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này.
```
</details>

<details><summary>S12</summary>

```text
HÌNH S12 (DỌC 9:16, phong cách bản vẽ kỹ thuật cơ khí Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch) và nhân vật chú chim kỹ sư hoạt hình đội mũ bảo hộ và kính lúp steampunk; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "kỳ quan cơ khí giảm chấn đỉnh cao của rừng xanh!". Bố cục: chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba mỉm cười giơ ngón tay cái kiêu hãnh giữa khung cảnh rừng xanh tươi sáng.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/70 của video YouTube về Chim Gõ Kiến). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách bản vẽ kỹ thuật cơ khí Leonardo Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch & Blueprint): nét bút kim kỹ thuật chuẩn xác từng milimét, các đường nét gạch bóng crosshatch cơ học tinh vi, chi tiết bánh răng đồng thau lộ cơ chế, thước kẹp caliper, vòng đo chấn động shockwave 1200G, sơ đồ vạch kích thước CAD màu nâu mực sepia và xanh lam blueprint kỹ thuật; NỀN TRẮNG TINH hoàn toàn, không watermark, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba. Nhân vật phụ cố định: Kỹ sư Cú Vọ già đeo kính lão tròn đọc tài liệu; Chuột chũi thợ mỏ mặc yếm cầm máy khoan mini; Sóc bay thợ hàn đeo kính đen cầm que hàn; Khỉ đầu chó thanh tra an toàn lao động cầm bảng kẹp hồ sơ. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/12 của video YouTube Shorts về Chim Gõ Kiến). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách bản vẽ kỹ thuật cơ khí Leonardo Da Vinci & Steampunk Schematic (Kinetic Technical Crosshatch & Blueprint): nét bút kim kỹ thuật chuẩn xác từng milimét, các đường nét gạch bóng crosshatch cơ học tinh vi, chi tiết bánh răng đồng thau lộ cơ chế, thước kẹp caliper, vòng đo chấn động shockwave 1200G, sơ đồ vạch kích thước CAD màu nâu mực sepia và xanh lam blueprint kỹ thuật; NỀN TRẮNG TINH hoàn toàn, không watermark, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú chim hoạt hình kỹ sư cơ khí sáng tạo độc bản, chỏm lông đầu đỏ cam nghệ thuật, đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp steampunk một mắt, chiếc mỏ cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh; tranh vẽ 2D comic nguyên bản tự do sáng tác không bản quyền bên thứ ba. Nhân vật phụ: Người que ngất xỉu vì va đầu vào gỗ; Kỹ sư cơ khí choáng váng đo gia tốc. 
```
</details>

## 7. SEO

- **title:** Bản Vẽ Giảm Chấn Hộp Sọ: Đập Đầu 12.000 Lần/Ngày Với Lực 1.200G Nhờ Chiếc Lưỡi Quấn Não?! | Tập 36
- **hook_paragraph:** Chim Gõ Kiến (Picidae) đập đầu vào thân cây gỗ cứng với tần số hai mươi lần mỗi giây và gia tốc cực hạn lên tới một ngàn hai trăm G — gấp một trăm hai mươi lần lực gây tử vong cho con người. Điều gì giúp cỗ máy cơ khí này không bị chấn thương sọ não hay xuất huyết nội sọ? Hãy cùng Kỹ sư trưởng giải mã bốn lớp phòng vệ sinh học đỉnh cao!
- **question:** Giữa chiếc lưỡi quấn quanh sọ làm dây đai an toàn và cấu trúc xương xốp hấp thụ 99,7% xung lực, giải pháp cơ khí nào của Chim Gõ Kiến khiến bạn kinh ngạc nhất?
- **next_teaser:** bác sĩ cấp cứu sa mạc mang túi mỡ dự trữ kỳ diệu và vòm họng nhai nuốt gai xương rồng
- **shorts_title:** Bí kíp Chim Gõ Kiến đập đầu 1.200G mà não không tổn thương?!
- **shorts_desc:** Chiếc lưỡi của Chim Gõ Kiến dài gấp 3 lần mỏ và quấn trọn quanh hộp sọ như chiếc dây đai an toàn xe hơi!
- **bullets:** Gia tốc va chạm 1.200G: Đập đầu 12.000 lần mỗi ngày với vận tốc 25 km/h không hề đau đầu · Chiếc lưỡi Hyoid thần thánh: Dài gấp 3 lần mỏ, quấn trọn vòng quanh hộp sọ đóng vai trò dây đai an toàn · Cấu trúc xương sọ xốp bọt khí: Hấp thụ và phân tán 99,7% xung lực va đập thành nhiệt năng · Mỏ bất đối xứng: Hàm dưới dài hơn hàm trên dẫn hướng sóng xung kích đi xuống cột sống thay vì não bộ · Mí mắt thứ ba chớp trong 1 mili-giây: Khóa chặt nhãn cầu chống áp suất đẩy mắt văng ra ngoài · Ứng dụng quân sự và thể thao: NASA và các hãng mũ bảo hiểm F1 học tập cấu trúc chống sốc của loài chim
- **tags:** chim gõ kiến, picidae, giảm chấn hộp sọ, cơ khí sinh học, khoa học kỳ thú, vẽ chuyện hoang dã, whiteboard animation

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-36-chim-go-kien
python src/episode/pipeline.py tts    projects/tap-36-chim-go-kien     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-36-chim-go-kien     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-36-chim-go-kien     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-36-chim-go-kien              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-36-chim-go-kien --force
python scripts/beat_sheet.py projects/tap-36-chim-go-kien               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-36-chim-go-kien/audio/shorts.wav projects/tap-36-chim-go-kien/renders/tap-36-chim-go-kien_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-36-chim-go-kien
python src/episode/pipeline.py seo    projects/tap-36-chim-go-kien
python src/episode/episode_doc.py     projects/tap-36-chim-go-kien
```
