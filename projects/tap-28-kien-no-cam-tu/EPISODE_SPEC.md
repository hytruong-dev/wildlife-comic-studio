# TẬP 28 — KIẾN NỔ CẢM TỬ · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-28-kien-no-cam-tu`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-28-kien-no-cam-tu`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F6` · **Persona giọng:** `ong_trum` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Kiến Nổ Cảm Tử |
| Tiêu đề YouTube | Loài Kiến Tự Kích Nổ Tung Cơ Thể Phun Keo Độc Bảo Vệ Tổ?! |
| Video dài | `renders/tap-28-kien-no-cam-tu_long.mp4` — 8:57.3 (537.3s) |
| Shorts | `renders/tap-28-kien-no-cam-tu_shorts.mp4` — 0:45.5 (45.5s) |
| Thumbnail | `renders/tap-28-kien-no-cam-tu_thumbnail.jpg` |
| Số hình | dài 65 beat / 65 ảnh riêng; Shorts 10 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.1**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/65 của video YouTube về Kiến Nổ Cảm Tử). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu. Nhân vật phụ cố định: chú kiến lính đầu phẳng phragmotic hoạt hình màu nâu đậm, đầu hình chiếc đĩa tròn phẳng lì như nút chai; bà trùm kiến chúa khổng lồ màu vàng nâu quý phái đội vương miện nhỏ; con kiến vàng dệt lá Oecophylla hung dữ nhiều gai. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — QUY TẮC SINH TỬ CỦA GIA TỘC KIẾN VÒM RỪNG
*Badge:* `HỒ SƠ ĐẾ CHẾ` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene01_p0.wav` (398 ký tự) · mood `tram_bi_an`

```text
Trong thế giới ngầm của rừng mưa nhiệt đới Borneo, có những gia tộc sinh tồn bằng những đạo luật nghiệt ngã đến rợn người. Tại những ngọn cây cổ thụ cao bốn mươi đến năm mươi mét chọc thủng tầng mây, một đế chế khổng lồ với hàng trăm ngàn thần dân đang vận hành theo một nguyên tắc tối thượng: Kẻ sinh ra ở tầng đáy thấp nhất... phải là kẻ sẵn sàng nổ tung thân xác để bảo vệ ngai vàng của bà trùm!
```
**Part 1** → `audio/vs/scene01_p1.wav` (100 ký tự) · 🎭 cameo `co_tro_ly`

```text
Báo cáo bà trùm, đội lính thợ dò đường đã tiến vào khu vực tranh chấp, sẵn sàng nhận lệnh tử vì đạo!
```
**Part 2** → `audio/vs/scene01_p2.wav` (456 ký tự) · mood `hao_hung`

```text
[surprise-oh] Bật màn hình chỉ huy lên, hôm nay chúng ta giải mã hồ sơ của đội quân cảm tử trung thành nhất hành tinh! [laughter] Xin giới thiệu với toàn thể anh em: đây là Kiến Nổ Cảm Tử, tên khoa học là Colobopsis explodens, thuộc nhóm kiến thợ nổ đặc hữu của vùng rừng mưa Đông Nam Á như Brunei, Malaysia và Thái Lan. Dù kích thước cơ thể chỉ bé bằng hạt gạo, nhưng trong giới côn trùng học, chúng tôi gọi thẳng tên nó bằng biệt danh: Chiến Binh Cảm Tử!
```
**Part 3** → `audio/vs/scene01_p3.wav` (375 ký tự) · mood `nghiem_trang_gia`

```text
Điều gì đã khiến một loài kiến nhỏ bé không hề có nọc châm độc ở đuôi lại khiến những tập đoàn kiến vàng dệt lá hung hãn nhất phải khiếp vía bỏ chạy? Bí mật nằm ở thứ vũ khí tự hủy giấu kín bên trong khoang bụng: một quả bom sinh học chứa keo độc màu vàng sẵn sàng phát nổ trong chớp mắt! Đêm nay, tôi mời anh em cùng lật mở bốn tầng cấu trúc quyền lực của đế chế cảm tử này!
```
**Part 4** → `audio/vs/scene01_p4.wav` (382 ký tự) · mood `tram_bi_an`

```text
Trên những tầng tán rừng rậm rạp cao chót vót cách mặt đất tới năm mươi đến sáu mươi mét, sự tranh giành từng giọt mật hoa và từng tấc cành cây diễn ra tàn bạo từng giây từng phút. Không có chỗ cho sự khoan nhượng hay đàm phán hòa bình. Một khi đã bước chân vào hàng ngũ lính thợ cảm tử, mỗi cá thể đều hiểu rõ bản án sinh tử đã được định sẵn ngay từ ngày chui ra khỏi kén ấu trùng!
```

### scene02 — LÍNH THỢ MINOR VÀ KHO VŨ KHÍ TUYẾN HÀM DƯỚI
*Thẻ chương:* KHO VŨ KHÍ HÓA CHẤT DÀI SUỐT DỌC CƠ THỂ

*Badge:* `CẤP BẬC ĐÁY` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene02_p0.wav` (357 ký tự) · mood `hao_hung`

```text
Tầng cấu trúc thứ nhất: Đội quân lính thợ mang quả bom cơ thể! Trong hệ thống phân cấp của gia tộc Colobopsis, những chú kiến thợ nhỏ bé này chiếm số lượng đông đảo nhất, ngày đêm bò trên những cành cây cao chót vót để kiếm mật hoa và tìm kiếm nguồn thức ăn thừa. Nhưng đằng sau vẻ ngoài cần mẫn ấy là một cấu tạo giải phẫu kỳ dị bậc nhất thế giới động vật!
```
**Part 1** → `audio/vs/scene02_p1.wav` (316 ký tự) · mood `don_dap`

```text
Năm hai ngàn mười tám, một công trình chấn động công bố trên tạp chí ZooKeys bởi tiến sĩ Alice Laciny đã giải mã hoàn chỉnh cấu trúc bên trong cơ thể Chiến Binh Cảm Tử: chạy dọc suốt từ phần hàm dưới xuyên qua lồng ngực xuống tận khoang bụng là một cặp túi dự trữ chất nhầy khổng lồ của tuyến hàm dưới! [surprise-wa]
```
**Part 2** → `audio/vs/scene02_p2.wav` (412 ký tự) · mood `hao_hung`

```text
Cặp túi hóa chất này phình to đến mức chiếm phần lớn thể tích bên trong cơ thể chú kiến, đẩy các cơ quan nội tạng khác dồn về một góc chật chội! Bên trong túi chứa đầy một dung dịch keo dính màu vàng tươi có mùi cay nồng nặc như gia vị cà ri, chứa đầy các hợp chất hữu cơ độc hại đủ sức thiêu đốt và làm tê liệt các loài chân khớp khác! Nó sống cả cuộc đời để nuôi dưỡng một kho hóa chất tự hủy sẵn sàng kích nổ!
```
**Part 3** → `audio/vs/scene02_p3.wav` (345 ký tự) · mood `hao_hung`

```text
Điều kỳ thú là bên trong dung dịch keo độc này còn nuôi dưỡng những quần thể vi khuẩn cộng sinh đặc biệt giúp ổn định độc tính và giữ cho khối keo luôn ở trạng thái lỏng nhớt hoàn hảo. Chừng nào túi tuyến còn nguyên vẹn, chú kiến vẫn sinh hoạt bươn chải bình thường. Nhưng chiếc ngòi nổ sinh học thì luôn được cài sẵn ở chế độ nhạy cảm cao nhất!
```
**Part 4** → `audio/vs/scene02_p4.wav` (326 ký tự) · mood `nghiem_trang_gia`

```text
Các nhà khoa học từng quan sát thấy những chú kiến thợ già cỗi khi khả năng kiếm ăn giảm sút sẽ tự nguyện nhận những nhiệm vụ tuần tra nguy hiểm nhất ở bìa ngoài cùng của lãnh thổ. Một sự phân công lao động tàn khốc nhưng hoàn hảo đến mức lạnh gáy: đem những quả bom sắp hết hạn ra tiền tuyến làm lá chắn đầu tiên cho tổ quốc!
```
**Part 5** → `audio/vs/scene02_p5.wav` (343 ký tự) · mood `hao_hung`

```text
Để tiếp cận và nghiên cứu được biệt đội cảm tử này, các nhà côn trùng học quốc tế đã phải trèo lên những chiếc cẩu tháp nghiên cứu vòm rừng dựng giữa rừng nguyên sinh Brunei ở độ cao hơn năm mươi mét! Họ phải đu dây lơ lửng giữa không trung suốt hàng tuần liền để đặt bẫy và ghi hình từng hành vi nhỏ nhất của những quả bom di động tí hon này!
```

### scene03 — CÚ GỒNG CƠ BỤNG NỔ TUNG CƠ THỂ AUTOTHYSIS
*Thẻ chương:* TỰ XÉ RÁCH VỎ BỤNG NỔ TUNG KEO DÍNH TRÓI KẺ THÙ

*Badge:* `ĐỘI QUÂN CẢM TỬ` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene03_p0.wav` (291 ký tự) · mood `tram_bi_an`

```text
Tầng cấu trúc thứ hai: Hiện tượng tự nổ tung cơ thể Autothysis! Khi đang tuần tra đơn độc trên tán lá rừng, nếu chẳng may bị một con nhện săn mồi hay một con kiến quân đội đối thủ bao vây áp sát không lối thoát, Chiến Binh Cảm Tử sẽ không hề van xin tha mạng hay tìm cách tháo chạy hèn nhát!
```
**Part 1** → `audio/vs/scene03_p1.wav` (349 ký tự) · mood `don_dap`

```text
Gã lập tức áp sát vào cơ thể kẻ địch, dùng hàm dưới cắn chặt vào chân hoặc râu của đối phương để khóa chết mục tiêu! Sau đó, gã gồng cực mạnh toàn bộ các bó cơ thành bụng... Bùm! Áp lực co bóp kinh hoàng làm nứt toạc lớp vỏ chitin ở phần bụng, xé rách màng túi tuyến và phóng ra một dòng keo độc màu vàng tươi bắn thẳng vào mặt kẻ thù! [surprise-wa]
```
**Part 2** → `audio/vs/scene03_p2.wav` (347 ký tự) · mood `don_dap`

```text
Dòng keo dính màu vàng này bám chặt cứng vào mắt, râu và các khớp chân của đối thủ, đông cứng lại như một lớp keo dán sắt cực độc chỉ sau vài giây! Kẻ săn mồi hoảng loạn giãy giụa nhưng càng cựa quậy thì các khớp chân càng bị keo dính chặt khóa bất động! Hóa chất cay nồng ngấm vào các lỗ thở làm kẻ địch ngạt thở tê liệt và chết gục ngay tại chỗ!
```
**Part 3** → `audio/vs/scene03_p3.wav` (262 ký tự) · mood `hao_hung`

```text
Chiến Binh Cảm Tử đã hy sinh ngay khoảnh khắc vụ nổ diễn ra. Nhưng gã đã hoàn thành xuất sắc nhiệm vụ của một quả bom sống: tiêu diệt sạch sẽ mối đe dọa và gửi đi một thông điệp đẫm máu tới toàn bộ kẻ thù trong rừng: Đừng bao giờ đụng vào gia tộc này! [laughter]
```
**Part 4** → `audio/vs/scene03_p4.wav` (329 ký tự) · mood `don_dap`

```text
Mùi hương cay nồng giải phóng từ vụ nổ không chỉ thiêu đốt kẻ địch mà còn đóng vai trò như một tín hiệu báo động đỏ lan tỏa trong không khí. Những chú kiến thợ tuần tra xung quanh ngửi thấy mùi đặc trưng liền lập tức giương râu cảnh giác, tạo thành một hàng rào phòng ngự thứ hai sẵn sàng tiếp ứng nếu đối thủ kéo thêm viện binh!
```
**Part 5** → `audio/vs/scene03_p5.wav` (311 ký tự) · mood `hao_hung`

```text
Trong lịch sử sinh học, tập tính tự sát bảo vệ bầy đàn này được nhà tự nhiên học người Đức ghi nhận lần đầu tiên từ năm một ngàn chín trăm mười sáu. Trải qua hơn một thế kỷ nghiên cứu, con người vẫn chưa hết bàng hoàng trước cái giá sinh tồn nghiệt ngã mà tự nhiên đã tôi luyện nên cho loài kiến thợ nhỏ bé này!
```

### scene04 — HIỆN TƯỢNG PHRAGMOSIS DÙNG ĐẦU LÀM CÁNH CỬA SỐNG
*Thẻ chương:* LÍNH ĐẦU PHẲNG CẮM CHẶT LỖ CÂY NHƯ NẮP NÚT CHAI

*Badge:* `KẺ GÁC CỔNG` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene04_p0.wav` (252 ký tự) · mood `hao_hung`

```text
Tầng cấu trúc thứ ba: Kẻ gác cổng hình nút chai sống! Nếu bên ngoài vòm cây là nơi lính thợ nhỏ nổ tung thân xác, thì ngay tại cửa tổ sổ gỗ trên thân cây cổ thụ, gia tộc này bố trí một lực lượng phòng thủ thụ động đỉnh cao mang tên kiến lính đầu phẳng!
```
**Part 1** → `audio/vs/scene04_p1.wav` (345 ký tự) · mood `hao_hung`

```text
Hãy quan sát hiện tượng cơ thể Phragmosis: phần đầu của những chú kiến lính này tiến hóa thành một chiếc đĩa tròn dẹt phẳng lì, phủ lớp vỏ cứng như gỗ và có kích thước khít khao một trăm phần trăm với lỗ khoét cửa tổ trên thân cây! Gã lính gác dùng chính chiếc đầu của mình cắm chặt vào lỗ cây như một chiếc nút chai rượu vang đóng chặt cửa hầm!
```
**Part 2** → `audio/vs/scene04_p2.wav` (109 ký tự) · 🎭 cameo `ga_khong_lo`

```text
Báo cáo gác cổng: Có kẻ địch đang cào cấu bên ngoài đòi đột nhập, chiếc đầu thép của em vẫn chốt cứng kín kẽ!
```
**Part 3** → `audio/vs/scene04_p3.wav` (386 ký tự) · mood `hao_hung`

```text
[laughter] Kẻ thù bên ngoài dù có hung hãn đến đâu cũng chỉ nhìn thấy một mảng vỏ cây phẳng lì trơn trượt, cắn không có chỗ bám, đẩy không tài nào lay chuyển nổi! Chỉ khi nào những chú kiến thợ cùng tổ đi kiếm ăn trở về, dùng râu gõ đúng nhịp mật mã bí mật lên trán, gã lính gác mới lùi nhẹ đầu vào trong mở lối cho đồng đội bước vào rồi lập tức cắm chốt đóng sập cửa lại! [surprise-oh]
```
**Part 4** → `audio/vs/scene04_p4.wav` (323 ký tự) · mood `nghiem_trang_gia`

```text
Suốt cả cuộc đời mình, những gã kiến lính đầu phẳng này hầu như không bao giờ bước chân ra khỏi ngưỡng cửa tổ! Chúng ăn thức ăn do kiến thợ mớm lại qua đường miệng, và nhiệm vụ duy nhất từ lúc trưởng thành đến lúc nhắm mắt xuôi tay là làm một chiếc then cửa sống kiên cố bảo vệ sự bình yên cho hàng ngàn ấu trùng bên trong!
```
**Part 5** → `audio/vs/scene04_p5.wav` (285 ký tự) · mood `hao_hung`

```text
Nếu gã lính gác chẳng may bị kẻ thù dùng càng nhổ ra ngoài hoặc tử trận, một chú lính đầu phẳng dự bị ở phía sau sẽ lập tức tiến lên trám đúng vị trí, cắm đầu bịt kín lỗ cây chỉ trong vài giây! Một hệ thống cửa hầm phòng thủ tự động thay thế không bao giờ để lộ khe hở cho kẻ đột nhập!
```

### scene05 — CUỘC CHIẾN VỚI KIẾN VÀNG OECOPHYLLA VÀ BÀ TRÙM
*Thẻ chương:* CHIẾN TRANH BẦY ĐÀN VÀ SỰ HY SINH BẢO VỆ KIẾN CHÚA

*Badge:* `ĐẠI CHIẾN BẦY ĐÀN` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene05_p0.wav` (395 ký tự) · mood `don_dap`

```text
Tầng cấu trúc thứ tư: Cuộc chiến tranh lãnh thổ khốc liệt nhất vòm rừng! Kẻ thù truyền kiếp số một của gia tộc Colobopsis là những đạo quân kiến vàng dệt lá Ô-cô-phi-la khổng lồ và hung bạo. Trong những trận đụng độ giáp lá cà trên tán lá cao năm mươi mét, hàng trăm Chiến Binh Cảm Tử sẵn sàng đồng loạt kích nổ bụng, biến chiến trường thành một bãi mìn keo vàng chết chóc để ngăn bước quân thù!
```
**Part 1** → `audio/vs/scene05_p1.wav` (380 ký tự) · mood `hao_hung`

```text
Sự hy sinh vị tha tột cùng này chỉ phục vụ cho một mục tiêu thiêng liêng duy nhất: Bảo vệ ngai vàng của Bà Trùm — kiến chúa mẫu nghi thiên hạ đang nằm sâu trong lõi thân cây gỗ cổ thụ! Kiến chúa là trái tim của cả đế chế, người đẻ ra hàng ngàn quả trứng mỗi ngày để liên tục bổ sung lực lượng cảm tử mới. Mất đi vài ngàn lính thợ chẳng là gì, miễn là bà trùm vẫn an toàn đẻ trứng!
```
**Part 2** → `audio/vs/scene05_p2.wav` (253 ký tự) · mood `hao_hung`

```text
Đây là đỉnh cao của sự tiến hóa xã hội bậc cao: một cá thể sẵn sàng tự hủy diệt bản thân để duy trì sự trường tồn vĩnh cửu của cả tổ chức gia tộc! Đúng là tinh thần trung thành tuyệt đối khiến con người khi nhìn vào cũng phải rùng mình nể sợ! [laughter]
```
**Part 3** → `audio/vs/scene05_p3.wav` (324 ký tự) · mood `am_ap`

```text
Vào mùa giao phối sau những cơn mưa rào nhiệt đới, đế chế sẽ cho ra đời những công chúa và hoàng tử kiến có cánh bay vút lên bầu trời đêm để tìm kiếm bạn đời lập nên những vương quốc mới. Những thế hệ cảm tử tiếp theo lại tiếp tục sinh ra, kế thừa trọn vẹn bản thiết kế bom sinh học để tiếp tục thống trị vòm rừng nhiệt đới!
```
**Part 4** → `audio/vs/scene05_p4.wav` (343 ký tự) · mood `hao_hung`

```text
Một tổ kiến Colobopsis trưởng thành có thể chiếm giữ cả một cụm cây dầu cổ thụ khổng lồ, kết nối với nhau bằng những tuyến đường mòn hóa học chạy dọc theo các nhánh dây leo trên không. Hàng trăm ngàn cá thể phối hợp nhịp nhàng như một siêu sinh vật duy nhất, nơi lợi ích của cá nhân hoàn toàn biến mất trước sự tồn vong bất diệt của cả đế chế!
```

### scene06 — LÒNG TRUNG THÀNH TUYỆT ĐỐI VÀ BÓNG ĐEN ĐẢO NGƯỢC THỜI GIAN
*Thẻ chương:* BÁO CÁO CUỐI CÙNG VÀ BÓNG ĐEN SỨA BẤT TỬ TẬP 29

*Badge:* `BÁO CÁO GIA TỘC` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene06_p0.wav` (285 ký tự) · mood `am_ap`

```text
Tổng kết hồ sơ đế chế số hai mươi tám. Từ một loài côn trùng nhỏ bé trên vòm cây rừng Borneo, Kiến Nổ Cảm Tử đã viết nên một bản hùng ca sinh tồn bi tráng bậc nhất tự nhiên: biến cơ thể thành bom, lấy sự hy sinh làm lá chắn và dùng chiếc đầu phẳng làm bức tường thành bất khả xâm phạm!
```
**Part 1** → `audio/vs/scene06_p1.wav` (133 ký tự) · mood `hao_hung`

```text
Báo cáo điệp báo gia tộc: Đạt điểm mười cho lòng trung thành và kỷ luật quân đội thép! Ký tên: ông trùm thế giới vòm rừng! [laughter]
```
**Part 2** → `audio/vs/scene06_p2.wav` (199 ký tự) · mood `hao_hung`

```text
Còn anh em thì sao? Nếu được chỉ huy một đội quân sinh học: anh em chọn đội cảm tử nổ tung keo độc vàng, hay đội lính gác đầu phẳng hình phích cắm bất khả xâm phạm? Hãy để lại bình luận bên dưới nhé!
```
**Part 3** → `audio/vs/scene06_p3.wav` (572 ký tự) · mood `am_ap`

```text
Hồ sơ đế chế số hai mươi tám xin được khép lại tại đây. Nhưng tập sau, chúng ta sẽ quay trở lại phòng thí nghiệm năm cấp độ để chứng kiến một phép màu sinh học đảo ngược quy luật thời gian của vũ trụ! Một sinh vật nhỏ xíu trong suốt như giọt nước trôi lơ lửng giữa đại dương, nhưng nắm giữ bí mật bất tử vĩ đại nhất: khi già yếu hoặc bị thương nặng, nó không chết đi mà tự đảo ngược toàn bộ tế bào của mình quay trở lại thời kỳ ấu trùng sơ sinh để sống lại từ đầu một cuộc đời mới! Đố các bạn biết bóng đen bí ẩn kỳ sau là loài vật nào? Hãy đoán ngay ở phần bình luận nhé!
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Những chiến binh kiến nhỏ bé này sẵn sàng tự gồng cơ bụng nổ tung cơ thể mình như bom cảm tử để tiêu diệt kẻ thù! [laughter] Xin giới thiệu Kiến Nổ Cảm Tử, sinh vật sống trên những ngọn cây cao năm mươi mét ở rừng mưa Đông Nam Á. Cơ thể nó mang một cặp túi dự trữ chất nhầy khổng lồ chạy dọc từ hàm xuống tận khoang bụng. Khi bị kẻ săn mồi bao vây, nó lao tới cắn chặt đối thủ rồi gồng rách lớp vỏ bụng để phóng ra một dòng keo độc màu vàng tươi cực dính! [surprise-wa] Dòng keo này khóa cứng hoàn toàn chân tay và làm ngạt thở kẻ địch chỉ trong vài giây! Trong khi đó, ở cửa tổ, những chú kiến lính có chiếc đầu phẳng lì hình nút chai sẽ cắm chặt đầu vào lỗ cây để làm cánh cửa sống chặn đứng mọi kẻ đột nhập! Một đế chế cảm tử vừa biết nổ tung tự sát, vừa dùng đầu làm cửa thành, đúng là đội quân liều chết kỳ quặc nhất hành tinh!
```

**Whisper prompt:** `Kiến Nổ Cảm Tử, Chiến Binh Cảm Tử, Colobopsis explodens, Colobopsis saundersi, Bo-nê-ô, Borneo, Bru-nây, Brunei, Ma-lai-xi-a, Malaysia, Thái Lan, autothysis, phragmosis, tuyến hàm dưới, gaster, Oecophylla, kiến vàng dệt lá, 40m, 50m, 60m, 1 giây, 100%, 1916, 2018, Sứa Bất Tử, Turritopsis`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| hai mươi tám | 28 |
| hai mươi chín | 29 |
| bốn mươi đến năm mươi mét | 40-50m |
| năm mươi đến sáu mươi mét | 50-60m |
| bốn mươi mét | 40m |
| năm mươi mét | 50m |
| sáu mươi mét | 60m |
| hàng trăm ngàn | hàng trăm ngàn |
| trăm ngàn | trăm ngàn |
| hàng ngàn | hàng ngàn |
| hàng triệu | hàng triệu |
| hàng trăm | hàng trăm |
| hàng chục | hàng chục |
| một giây | 1 giây |
| hai giây | 2 giây |
| vài giây | vài giây |
| một trăm phần trăm | 100% |
| bốn tầng | 4 tầng |
| bốn hạng mục | 4 hạng mục |
| năm cấp độ | 5 cấp độ |
| thứ nhất | thứ 1 |
| thứ hai | thứ 2 |
| thứ ba | thứ 3 |
| thứ tư | thứ 4 |
| thứ năm | thứ 5 |
| điểm mười | điểm 10 |
| Bo-nê-ô | Borneo |
| Bru-nây | Brunei |
| Ma-lai-xi-a | Malaysia |
| Thái Lan | Thái Lan |
| Ô-cô-phi-la | Oecophylla |
| Năm hai ngàn mười tám | 2018 |
| năm hai ngàn mười tám | 2018 |
| năm một ngàn chín trăm mười sáu | 1916 |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · QUY TẮC SINH TỬ CỦA GIA TỘC KIẾN VÒM RỪNG · 84.2s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:05.8 (5.8s) | L01 | Trong thế giới ngầm của rừng mưa nhiệt đới Borneo, có những gia tộc sinh tồn bằng những đạo luật nghiệt ngã đến rợn người. |  | Đáy rừng mưa nhiệt đới Borneo tăm tối mù sương: những thân cây đại thụ vươn thẳng lên trời xanh chọc thủng tầng mây, không khí rừng thiêng nước độc bí hiểm. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này. |
| b02 | 00:05.8–00:19.5 (13.7s) | L02 | Tại những ngọn cây cổ thụ cao 40-50m chọc thủng tầng mây, một đế chế khổng lồ với hàng trăm ngàn thần dân đang vận hành theo một nguyên tắc tối thượng: Kẻ sinh ra ở tầng đáy thấp nhất... phải là kẻ sẵn sàng nổ tung thân xác để bảo vệ ngai vàng của bà trùm! | **CAO 40-50M** · vòm cây cổ thụ · R/350 · [0.65, 0.45] | Trên những ngọn cây cổ thụ cao 40-50m chọc thủng tầng mây, hàng trăm ngàn chú kiến đang di chuyển tấp nập như một đế chế quân đội vĩ đại. |
| b03 | 00:19.5–00:25.4 (5.9s) | L03 | Báo cáo bà trùm, đội lính thợ dò đường đã tiến vào khu vực tranh chấp, sẵn sàng nhận lệnh tử vì đạo! |  | BÊN TRÁI một chú kiến thợ nhỏ bé đeo tai nghe bộ đàm cúi đầu chào; BÊN PHẢI bà trùm kiến chúa khổng lồ màu vàng nâu quý phái đội vương miện nhỏ nằm uy nghi trên ngai vàng trong thân gỗ. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này. |
| b04 | 00:25.4–00:31.2 (5.9s) | L04 | Bật màn hình chỉ huy lên, hôm nay chúng ta giải mã hồ sơ của đội quân cảm tử trung thành nhất hành tinh! |  | Màn hình radar chỉ huy hiển thị bản đồ tổ kiến trên các tán cây rừng mưa nhiệt đới Borneo phát sáng huỳnh quang. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này. |
| b05 | 00:31.2–00:41.0 (9.8s) | L05 | Xin giới thiệu với toàn thể anh em: đây là Kiến Nổ Cảm Tử, tên khoa học là Colobopsis explodens, thuộc nhóm kiến thợ nổ đặc hữu của vùng rừng mưa Đông Nam Á như Brunei, Malaysia và Thái Lan. |  | chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu đứng oai vệ trên cành cây lá xanh, thắt chiếc băng đô đỏ cảm tử trên trán, dáng đứng kiêu hãnh của một chiến binh thực thụ. |
| b06 | 00:41.0–00:48.3 (7.3s) | L06 | Dù kích thước cơ thể chỉ bé bằng hạt gạo, nhưng trong giới côn trùng học, chúng tôi gọi thẳng tên nó bằng biệt danh: Chiến Binh Cảm Tử! |  | Ở GIỮA chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu đứng cạnh một hạt gạo trắng tinh để so sánh kích thước bé nhỏ bằng nhau, xung quanh có dải ruy băng danh hiệu Chiến Binh Cảm Tử. |
| b07 | 00:48.3–00:54.6 (6.3s) | L07 | Điều gì đã khiến một loài kiến nhỏ bé không hề có nọc châm độc ở đuôi lại khiến những tập đoàn kiến vàng dệt lá hung hãn nhất phải khiếp vía bỏ chạy? |  | Chia đôi: BÊN TRÁI đạo quân kiến vàng dệt lá hung dữ giơ càng to; BÊN PHẢI chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu nhỏ bé nhưng khiến đối phương hoảng sợ lùi bước. |
| b08 | 00:54.6–01:01.5 (6.9s) | L08 | Bí mật nằm ở thứ vũ khí tự hủy giấu kín bên trong khoang bụng: một quả bom sinh học chứa keo độc màu vàng sẵn sàng phát nổ trong chớp mắt! |  | Mặt cắt giải phẫu trong suốt của chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu: bên trong khoang bụng gaster chứa một quả bom sinh học màu vàng tươi phát sáng rực rỡ chuẩn bị kích nổ. |
| b09 | 01:01.5–01:05.6 (4.1s) | L09 | Đêm nay, tôi mời anh em cùng lật mở 4 tầng cấu trúc quyền lực của đế chế cảm tử này! | **4 TẦNG** · cấu trúc đế chế · L/350 · [0.35, 0.45] | Mô hình 4 tầng cấu trúc quyền lực của đế chế kiến mở ra như một pháo đài nhiều tầng trên thân cây cổ thụ. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này. |
| b10 | 01:05.6–01:14.3 (8.7s) | L10 | Trên những tầng tán rừng rậm rạp cao chót vót cách mặt đất tới 50-60m, sự tranh giành từng giọt mật hoa và từng tấc cành cây diễn ra tàn bạo từng giây từng phút. | **50-60 MÉT** · độ cao sinh tồn · R/350 · [0.65, 0.45] | Cảnh tượng vòm cây rậm rạp cao 50-60m: các nhánh cây đan xen nhau giữa lưng chừng trời, nơi diễn ra cuộc chiến tranh giành mật hoa tàn bạo. |
| b11 | 01:14.3–01:16.8 (2.5s) | L11 | Không có chỗ cho sự khoan nhượng hay đàm phán hòa bình. |  | Hai chú kiến đối địch trừng mắt nhìn nhau trên cành cây hẹp, không khí căng thẳng nghẹt thở không có chỗ cho khoan nhượng. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này. |
| b12 | 01:16.8–01:24.2 (7.4s) | L12 | Một khi đã bước chân vào hàng ngũ lính thợ cảm tử, mỗi cá thể đều hiểu rõ bản án sinh tử đã được định sẵn ngay từ ngày chui ra khỏi kén ấu trùng! |  | chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu vừa chui ra khỏi chiếc kén ấu trùng màu trắng, lập tức được thắt chiếc băng đô đỏ cảm tử trên đầu, đôi mắt ánh lên quyết tâm sắt đá. |

### scene02 · LÍNH THỢ MINOR VÀ KHO VŨ KHÍ TUYẾN HÀM DƯỚI · 106.8s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:14.0 (14.0s) | L13 | Tầng cấu trúc thứ 1: Đội quân lính thợ mang quả bom cơ thể! Trong hệ thống phân cấp của gia tộc Colobopsis, những chú kiến thợ nhỏ bé này chiếm số lượng đông đảo nhất, ngày đêm bò trên những cành cây cao chót vót để kiếm mật hoa và tìm kiếm nguồn thức ăn thừa. |  | Bảng hồ sơ hiện TẦNG CẤU TRÚC 1: ĐỘI QUÂN LÍNH THỢ MANG QUẢ BOM CƠ THỂ; hàng ngàn chú kiến thợ nhỏ bé bò trên cành cây kiếm mật hoa. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này. |
| b02 | 00:14.0–00:19.4 (5.5s) | L14 | Nhưng đằng sau vẻ ngoài cần mẫn ấy là một cấu tạo giải phẫu kỳ dị bậc nhất thế giới động vật! |  | Kính hiển vi phóng to cấu tạo giải phẫu kỳ dị bên trong cơ thể chú kiến thợ nhỏ bé cần mẫn. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này. |
| b03 | 00:19.4–00:34.0 (14.6s) | L15 | 2018, một công trình chấn động công bố trên tạp chí ZooKeys bởi tiến sĩ Alice Laciny đã giải mã hoàn chỉnh cấu trúc bên trong cơ thể Chiến Binh Cảm Tử: chạy dọc suốt từ phần hàm dưới xuyên qua lồng ngực xuống tận khoang bụng là một cặp túi dự trữ chất nhầy khổng lồ của tuyến hàm dưới! | **NĂM 2018** · nghiên cứu Laciny · L/350 · [0.35, 0.45] | Bìa tạp chí ZooKeys năm 2018 mở ra bản vẽ giải phẫu của tiến sĩ Alice Laciny: cặp túi dự trữ chất nhầy khổng lồ chạy từ hàm xuống bụng. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này. |
| b04 | 00:34.0–00:41.8 (7.8s) | L16 | Cặp túi hóa chất này phình to đến mức chiếm phần lớn thể tích bên trong cơ thể chú kiến, đẩy các cơ quan nội tạng khác dồn về một góc chật chội! |  | Sơ đồ cơ thể chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu: cặp túi tuyến phình to chiếm hầu hết không gian trong thân, đẩy dạ dày và ruột dồn nép vào một góc chật chội. |
| b05 | 00:41.8–00:51.4 (9.5s) | L17 | Bên trong túi chứa đầy một dung dịch keo dính màu vàng tươi có mùi cay nồng nặc như gia vị cà ri, chứa đầy các hợp chất hữu cơ độc hại đủ sức thiêu đốt và làm tê liệt các loài chân khớp khác! |  | Dung dịch keo dính màu vàng tươi bốc khói cay nồng như gia vị cà ri bên trong túi tuyến, chứa các phân tử hóa chất độc hại phát sáng. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này. |
| b06 | 00:51.4–00:55.5 (4.2s) | L18 | Nó sống cả cuộc đời để nuôi dưỡng một kho hóa chất tự hủy sẵn sàng kích nổ! |  | chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu vừa đi kiếm ăn vừa mang vác kho hóa chất tự hủy căng phồng trong bụng, luôn sẵn sàng kích nổ. |
| b07 | 00:55.5–01:05.5 (9.9s) | L19 | Điều kỳ thú là bên trong dung dịch keo độc này còn nuôi dưỡng những quần thể vi khuẩn cộng sinh đặc biệt giúp ổn định độc tính và giữ cho khối keo luôn ở trạng thái lỏng nhớt hoàn hảo. |  | Kính hiển vi siêu vi khuẩn: những quần thể vi khuẩn cộng sinh đặc biệt sống bên trong túi keo giúp bảo quản độ nhớt hoàn hảo. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này. |
| b08 | 01:05.5–01:13.5 (8.1s) | L20 | Chừng nào túi tuyến còn nguyên vẹn, chú kiến vẫn sinh hoạt bươn chải bình thường. Nhưng chiếc ngòi nổ sinh học thì luôn được cài sẵn ở chế độ nhạy cảm cao nhất! |  | chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu sinh hoạt bình thường trên tán lá nhưng chiếc ngòi nổ sinh học màu đỏ trên bụng luôn chớp sáng nhạy bén. |
| b09 | 01:13.5–01:21.4 (7.9s) | L21 | Các nhà khoa học từng quan sát thấy những chú kiến thợ già cỗi khi khả năng kiếm ăn giảm sút sẽ tự nguyện nhận những nhiệm vụ tuần tra nguy hiểm nhất ở bìa ngoài cùng của lãnh thổ. |  | Những chú kiến thợ già cỗi râu bạc bước ra ranh giới ngoài cùng của lãnh thổ để tuần tra canh gác tiền tuyến. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này. |
| b10 | 01:21.4–01:28.7 (7.2s) | L22 | Một sự phân công lao động tàn khốc nhưng hoàn hảo đến mức lạnh gáy: đem những quả bom sắp hết hạn ra tiền tuyến làm lá chắn đầu tiên cho tổ quốc! |  | Hàng rào lính thợ già dũng cảm đứng chắn bảo vệ bầy đàn phía sau; một sự phân công lao động hoàn hảo và lạnh gáy. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này. |
| b11 | 01:28.7–01:39.8 (11.1s) | L23 | Để tiếp cận và nghiên cứu được biệt đội cảm tử này, các nhà côn trùng học quốc tế đã phải trèo lên những chiếc cẩu tháp nghiên cứu vòm rừng dựng giữa rừng nguyên sinh Brunei ở độ cao hơn 50m! | **THÁP 50M** · cẩu tháp Brunei · R/350 · [0.65, 0.45] | Chiếc cẩu tháp nghiên cứu vòm rừng cao hơn 50m dựng giữa rừng nguyên sinh Brunei chọc thẳng lên mây xanh. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này. |
| b12 | 01:39.8–01:46.8 (7.0s) | L24 | Họ phải đu dây lơ lửng giữa không trung suốt hàng tuần liền để đặt bẫy và ghi hình từng hành vi nhỏ nhất của những quả bom di động tí hon này! |  | Các nhà khoa học quốc tế đu dây lơ lửng giữa không trung cách mặt đất 50m, cầm kính lúp và máy quay quan sát những chú kiến tí hon. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này. |

### scene03 · CÚ GỒNG CƠ BỤNG NỔ TUNG CƠ THỂ AUTOTHYSIS · 92.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:03.5 (3.5s) | L25 | Tầng cấu trúc thứ 2: Hiện tượng tự nổ tung cơ thể Autothysis! |  | Bảng hồ sơ hiện TẦNG CẤU TRÚC 2: HIỆN TƯỢNG TỰ NỔ TUNG AUTOTHYSIS; chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu đơn độc tuần tra trên phiến lá xanh biếc. |
| b02 | 00:03.5–00:14.2 (10.7s) | L26 | Khi đang tuần tra đơn độc trên tán lá rừng, nếu chẳng may bị một con nhện săn mồi hay một con kiến quân đội đối thủ bao vây áp sát không lối thoát, Chiến Binh Cảm Tử sẽ không hề van xin tha mạng hay tìm cách tháo chạy hèn nhát! |  | Một con nhện săn mồi lông lá to lớn và kiến đối thủ bất ngờ xuất hiện bao vây chặn đứng đường lui của chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu. |
| b03 | 00:14.2–00:19.7 (5.5s) | L27 | Gã lập tức áp sát vào cơ thể kẻ địch, dùng hàm dưới cắn chặt vào chân hoặc râu của đối phương để khóa chết mục tiêu! |  | chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu lao thẳng vào kẻ địch, dùng hai chiếc hàm dưới sắc bén cắn chặt cứng vào chân con nhện để khóa chặt mục tiêu. |
| b04 | 00:19.7–00:30.4 (10.8s) | L28 | Sau đó, gã gồng cực mạnh toàn bộ các bó cơ thành bụng... Bùm! Áp lực co bóp kinh hoàng làm nứt toạc lớp vỏ chitin ở phần bụng, xé rách màng túi tuyến và phóng ra một dòng keo độc màu vàng tươi bắn thẳng vào mặt kẻ thù! |  | Bùm! chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu gồng cực mạnh cơ bụng làm nứt toạc lớp vỏ chitin, xé rách túi tuyến và phát nổ giải phóng dòng keo độc màu vàng rực rỡ. |
| b05 | 00:30.4–00:37.6 (7.2s) | L29 | Dòng keo dính màu vàng này bám chặt cứng vào mắt, râu và các khớp chân của đối thủ, đông cứng lại như một lớp keo dán sắt cực độc chỉ sau vài giây! | **ĐÔNG CỨNG** · keo độc dán sắt · R/350 · [0.65, 0.48] | Dòng keo vàng tươi dính chặt cứng bọc kín mắt, râu và chân của con nhện săn mồi, keo đông cứng lại như lớp keo dán sắt chỉ sau vài giây. |
| b06 | 00:37.6–00:46.7 (9.1s) | L30 | Kẻ săn mồi hoảng loạn giãy giụa nhưng càng cựa quậy thì các khớp chân càng bị keo dính chặt khóa bất động! Hóa chất cay nồng ngấm vào các lỗ thở làm kẻ địch ngạt thở tê liệt và chết gục ngay tại chỗ! |  | Con nhện giãy giụa bất lực trong đống keo dính vàng đặc quánh, hóa chất cay nồng ngấm vào lỗ thở làm nó tê liệt ngã gục tại chỗ. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này. |
| b07 | 00:46.7–00:54.0 (7.4s) | L31 | Chiến Binh Cảm Tử đã hy sinh ngay khoảnh khắc vụ nổ diễn ra. Nhưng gã đã hoàn thành xuất sắc nhiệm vụ của một quả bom sống: tiêu diệt sạch sẽ mối đe |  | Ánh sáng hào quang tôn vinh sự hy sinh oanh liệt của quả bom sống chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu, tiêu diệt hoàn toàn kẻ thù hung ác. |
| b08 | 00:54.0–01:00.5 (6.4s) | L32 | dọa và gửi đi một thông điệp đẫm máu tới toàn bộ kẻ thù trong rừng: Đừng bao giờ đụng vào gia tộc này! |  | Biển cảnh báo màu đỏ hình chiếc đầu lâu cắm trên cành cây: thông điệp đẫm máu khiến muôn loài kẻ thù không dám xâm phạm. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này. |
| b09 | 01:00.5–01:07.5 (7.0s) | L33 | Mùi hương cay nồng giải phóng từ vụ nổ không chỉ thiêu đốt kẻ địch mà còn đóng vai trò như một tín hiệu báo động đỏ lan tỏa trong không khí. |  | Những làn sóng mùi hương cay nồng màu vàng lan tỏa trong không khí như tín hiệu báo động đỏ khẩn cấp khắp vòm lá. |
| b10 | 01:07.5–01:16.1 (8.6s) | L34 | Những chú kiến thợ tuần tra xung quanh ngửi thấy mùi đặc trưng liền lập tức giương râu cảnh giác, tạo thành một hàng rào phòng ngự thứ 2 sẵn sàng tiếp ứng nếu đối thủ kéo thêm viện binh! |  | Đội quân kiến thợ tuần tra xung quanh đồng loạt giương râu cảnh giác, tạo thành một hàng rào phòng ngự thứ 2 kiên cố sẵn sàng chiến đấu. |
| b11 | 01:16.1–01:23.9 (7.8s) | L35 | Trong lịch sử sinh học, tập tính tự sát bảo vệ bầy đàn này được nhà tự nhiên học người Đức ghi nhận lần đầu tiên từ 1916. | **NĂM 1916** · phát hiện đầu tiên · L/350 · [0.35, 0.45] | Cuốn sổ tay ghi chép cổ điển của nhà tự nhiên học người Đức năm 1916 với hình vẽ chú kiến tự nổ tung cơ thể đầu tiên. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này. |
| b12 | 01:23.9–01:32.4 (8.5s) | L36 | Trải qua hơn một thế kỷ nghiên cứu, con người vẫn chưa hết bàng hoàng trước cái giá sinh tồn nghiệt ngã mà tự nhiên đã tôi luyện nên cho loài kiến thợ nhỏ bé này! |  | Dòng thời gian một thế kỷ nghiên cứu: loài người nghiêng mình thán phục trước giá trị sinh tồn nghiệt ngã của loài kiến cảm tử; bảng Tầng 2 bật PASS. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này. |

### scene04 · HIỆN TƯỢNG PHRAGMOSIS DÙNG ĐẦU LÀM CÁNH CỬA SỐNG · 88.6s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:13.4 (13.4s) | L37 | Tầng cấu trúc thứ 3: Kẻ gác cổng hình nút chai sống! Nếu bên ngoài vòm cây là nơi lính thợ nhỏ nổ tung thân xác, thì ngay tại cửa tổ sổ gỗ trên thân cây cổ thụ, gia tộc này bố trí một lực lượng phòng thủ thụ động đỉnh cao mang tên kiến lính đầu phẳng! |  | Bảng hồ sơ hiện TẦNG CẤU TRÚC 3: KẺ GÁC CỔNG HÌNH NÚT CHAI SỐNG; cửa tổ sổ gỗ hình tròn trên thân cây cổ thụ. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này. |
| b02 | 00:13.4–00:26.0 (12.6s) | L38 | Hãy quan sát hiện tượng cơ thể Phragmosis: phần đầu của những chú kiến lính này tiến hóa thành một chiếc đĩa tròn dẹt phẳng lì, phủ lớp vỏ cứng như gỗ và có kích thước khít khao 100% với lỗ khoét cửa tổ trên thân cây! | **KHÍT 100%** · đầu phẳng phragmosis · R/350 · [0.65, 0.48] | Cận cảnh đầu của chú kiến lính đầu phẳng phragmotic hoạt hình màu nâu đậm, đầu hình chiếc đĩa tròn phẳng lì như nút chai: chiếc đầu tiến hóa thành một chiếc đĩa tròn dẹt phẳng lì phủ lớp vỏ cứng như gỗ, khít khao 100% với miệng lỗ tổ cây. |
| b03 | 00:26.0–00:31.7 (5.7s) | L39 | Gã lính gác dùng chính chiếc đầu của mình cắm chặt vào lỗ cây như một chiếc nút chai rượu vang đóng chặt cửa hầm! |  | chú kiến lính đầu phẳng phragmotic hoạt hình màu nâu đậm, đầu hình chiếc đĩa tròn phẳng lì như nút chai cắm chặt đầu mình vào lỗ cây tròn như chiếc nút bần đóng chặt miệng chai rượu vang, thân mình giấu kín bên trong hầm. |
| b04 | 00:31.7–00:38.9 (7.2s) | L40 | Báo cáo gác cổng: Có kẻ địch đang cào cấu bên ngoài đòi đột nhập, chiếc đầu thép của em vẫn chốt cứng kín kẽ! |  | Bên ngoài kẻ thù cào cấu điên cuồng lên chiếc đầu phẳng lì của chú kiến lính đầu phẳng phragmotic hoạt hình màu nâu đậm, đầu hình chiếc đĩa tròn phẳng lì như nút chai, chiếc đầu chốt cứng kín kẽ như bức tường gỗ bất khả xâm phạm. |
| b05 | 00:38.9–00:46.8 (7.9s) | L41 | Kẻ thù bên ngoài dù có hung hãn đến đâu cũng chỉ nhìn thấy một mảng vỏ cây phẳng lì trơn trượt, cắn không có chỗ bám, đẩy không tài nào lay chuyển nổi! |  | Kẻ địch hung hãn dùng hàm cắn trượt trên mảng đầu phẳng trơn trượt của chú kiến lính đầu phẳng phragmotic hoạt hình màu nâu đậm, đầu hình chiếc đĩa tròn phẳng lì như nút chai, đẩy mãi không lay chuyển nổi. |
| b06 | 00:46.8–00:52.8 (6.0s) | L42 | Chỉ khi nào những chú kiến thợ cùng tổ đi kiếm ăn trở về, dùng râu gõ đúng nhịp mật mã bí mật lên trán, |  | chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu đi kiếm ăn trở về, dùng hai chiếc râu gõ đúng nhịp mật mã bí mật lên trán chú kiến lính đầu phẳng phragmotic hoạt hình màu nâu đậm, đầu hình chiếc đĩa tròn phẳng lì như nút chai để xin mở  |
| b07 | 00:52.8–00:58.5 (5.7s) | L43 | gã lính gác mới lùi nhẹ đầu vào trong mở lối cho đồng đội bước vào rồi lập tức cắm chốt đóng sập cửa lại! |  | chú kiến lính đầu phẳng phragmotic hoạt hình màu nâu đậm, đầu hình chiếc đĩa tròn phẳng lì như nút chai lùi nhẹ đầu vào trong mở khe hở cho đồng đội bước vào rồi lập tức cắm đầu đóng sập cửa hầm lại an toàn. |
| b08 | 00:58.5–01:03.9 (5.4s) | L44 | Suốt cả cuộc đời mình, những gã kiến lính đầu phẳng này hầu như không bao giờ bước chân ra khỏi ngưỡng cửa tổ! |  | chú kiến lính đầu phẳng phragmotic hoạt hình màu nâu đậm, đầu hình chiếc đĩa tròn phẳng lì như nút chai cả đời đứng im bên ngưỡng cửa tổ, thân mình to bè làm then cửa sống bảo vệ hàng ngàn ấu trùng nhỏ bé bên trong. |
| b09 | 01:03.9–01:13.8 (9.8s) | L45 | Chúng ăn thức ăn do kiến thợ mớm lại qua đường miệng, và nhiệm vụ duy nhất từ lúc trưởng thành đến lúc nhắm mắt xuôi tay là làm một chiếc then cửa sống kiên cố bảo vệ sự bình yên cho hàng ngàn ấu trùng bên trong! |  | Kiến thợ mớm thức ăn giọt mật qua miệng cho chú kiến lính đầu phẳng phragmotic hoạt hình màu nâu đậm, đầu hình chiếc đĩa tròn phẳng lì như nút chai thưởng thức bữa ăn ấm cúng ngay tại vị trí chốt gác. |
| b10 | 01:13.8–01:28.6 (14.8s) | L46 | Nếu gã lính gác chẳng may bị kẻ thù dùng càng nhổ ra ngoài hoặc tử trận, một chú lính đầu phẳng dự bị ở phía sau sẽ lập tức tiến lên trám đúng vị trí, cắm đầu bịt kín lỗ cây chỉ trong vài giây! Một hệ thống cửa hầm phòng thủ tự động thay thế không bao giờ để lộ khe hở cho kẻ đột nhập! |  | Một chú lính đầu phẳng dự bị từ phía sau lập tức tiến lên cắm đầu trám đúng vị trí chỉ trong vài giây; bảng Tầng 3 bật PASS. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này. |

### scene05 · CUỘC CHIẾN VỚI KIẾN VÀNG OECOPHYLLA VÀ BÀ TRÙM · 85.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:04.0 (4.0s) | L47 | Tầng cấu trúc thứ 4: Cuộc chiến tranh lãnh thổ khốc liệt nhất vòm rừng! |  | Bảng hồ sơ hiện TẦNG CẤU TRÚC 4: CUỘC CHIẾN TRANH LÃNH THỔ KHỐC LIỆT NHẤT VÒM RỪNG; hai đạo quân kiến đối đầu nghẹt thở. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này. |
| b02 | 00:04.0–00:10.1 (6.1s) | L48 | Kẻ thù truyền kiếp số một của gia tộc Colobopsis là những đạo quân kiến vàng dệt lá Oecophylla khổng lồ và hung bạo. |  | Đạo quân con kiến vàng dệt lá Oecophylla hung dữ nhiều gai kiến vàng dệt lá khổng lồ hung tợn tràn ngập các cành cây giương hàm đe dọa lãnh thổ. |
| b03 | 00:10.1–00:12.7 (2.6s) | L49 | Trong những trận đụng độ giáp lá cà trên tán lá cao 50m, | **TÁN LÁ 50M** · chiến trường đẫm máu · R/350 · [0.65, 0.45] | Chiến trường giáp lá cà trên tán lá cao 50m: những quả bom cảm tử của chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu đồng loạt kích nổ bùng lên những vệt sáng vàng rực. |
| b04 | 00:12.7–00:18.8 (6.1s) | L50 | hàng trăm Chiến Binh Cảm Tử sẵn sàng đồng loạt kích nổ bụng, biến chiến trường thành một bãi mìn keo vàng chết chóc để ngăn bước quân thù! |  | Bãi mìn keo vàng chết chóc phong tỏa toàn bộ cành cây, bọc cứng hàng chục con kiến vàng dệt lá xâm lăng ngăn bước quân thù. |
| b05 | 00:18.8–00:28.1 (9.4s) | L51 | Sự hy sinh vị tha tột cùng này chỉ phục vụ cho một mục tiêu thiêng liêng duy nhất: Bảo vệ ngai vàng của Bà Trùm — kiến chúa mẫu nghi thiên hạ đang nằm sâu trong lõi thân cây gỗ cổ thụ! |  | Sâu trong lõi thân cây gỗ cổ thụ: bà trùm kiến chúa khổng lồ màu vàng nâu quý phái đội vương miện nhỏ nằm uy nghi trên ngai vàng lộng lẫy được bảo vệ an toàn tuyệt đối. |
| b06 | 00:28.1–00:38.6 (10.4s) | L52 | Kiến chúa là trái tim của cả đế chế, người đẻ ra hàng ngàn quả trứng mỗi ngày để liên tục bổ sung lực lượng cảm tử mới. Mất đi vài ngàn lính thợ chẳng là gì, miễn là bà trùm vẫn an toàn đẻ trứng! | **1.000 QUẢ** · trứng đẻ mỗi ngày · L/350 · [0.35, 0.45] | bà trùm kiến chúa khổng lồ màu vàng nâu quý phái đội vương miện nhỏ cần mẫn đẻ ra hàng ngàn quả trứng nhỏ màu trắng mỗi ngày, các vú nuôi chăm sóc cẩn thận bổ sung quân đoàn mới. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này. |
| b07 | 00:38.6–00:52.0 (13.4s) | L53 | Đây là đỉnh cao của sự tiến hóa xã hội bậc cao: một cá thể sẵn sàng tự hủy diệt bản thân để duy trì sự trường tồn vĩnh cửu của cả tổ chức gia tộc! Đúng là tinh thần trung thành tuyệt đối khiến con người khi nhìn vào cũng phải rùng mình nể sợ! |  | Biểu tượng gia tộc kiến với tinh thần đoàn kết bất diệt: hàng ngàn bàn tay kiến nắm chặt bảo vệ vương miện đế chế. |
| b08 | 00:52.0–01:01.2 (9.2s) | L54 | Vào mùa giao phối sau những cơn mưa rào nhiệt đới, đế chế sẽ cho ra đời những công chúa và hoàng tử kiến có cánh bay vút lên bầu trời đêm để tìm kiếm bạn đời lập nên những vương quốc mới. |  | Bầu trời đêm sau cơn mưa rào: những công chúa và hoàng tử kiến có cánh bay lượn rực rỡ tìm kiếm bạn đời lập vương quốc mới. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này. |
| b09 | 01:01.2–01:07.7 (6.6s) | L55 | Những thế hệ cảm tử tiếp theo lại tiếp tục sinh ra, kế thừa trọn vẹn bản thiết kế bom sinh học để tiếp tục thống trị vòm rừng nhiệt đới! |  | Những thế hệ kiến cảm tử tiếp theo liên tục chui ra khỏi kén ấu trùng, kế thừa trọn vẹn bản thiết kế bom sinh học để tiếp tục thống trị vòm rừng. |
| b10 | 01:07.7–01:17.7 (9.9s) | L56 | Một tổ kiến Colobopsis trưởng thành có thể chiếm giữ cả một cụm cây dầu cổ thụ khổng lồ, kết nối với nhau bằng những tuyến đường mòn hóa học chạy dọc theo các nhánh dây leo trên không. |  | Cụm cây dầu cổ thụ khổng lồ liên kết với nhau bằng những con đường mòn hóa học chạy dọc các nhánh dây leo trên không. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này. |
| b11 | 01:17.7–01:25.9 (8.2s) | L57 | Hàng trăm ngàn cá thể phối hợp nhịp nhàng như một siêu sinh vật duy nhất, nơi lợi ích của cá nhân hoàn toàn biến mất trước sự tồn vong bất diệt của cả đế chế! |  | Hàng trăm ngàn cá thể phối hợp nhịp nhàng như một cỗ máy siêu sinh vật duy nhất; bảng Tầng 4 bật PASS rực rỡ. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này. |

### scene06 · LÒNG TRUNG THÀNH TUYỆT ĐỐI VÀ BÓNG ĐEN ĐẢO NGƯỢC THỜI GIAN · 59.3s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:02.4 (2.4s) | L58 | Tổng kết hồ sơ đế chế số 28. |  | Bàn chỉ huy thế giới ngầm vòm rừng: bản tổng kết hồ sơ đế chế số 28 mở ra với biểu tượng chú kiến nổ quả cảm. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này. |
| b02 | 00:02.4–00:14.1 (11.8s) | L59 | Từ một loài côn trùng nhỏ bé trên vòm cây rừng Borneo, Kiến Nổ Cảm Tử đã viết nên một bản hùng ca sinh tồn bi tráng bậc nhất tự nhiên: biến cơ thể thành bom, lấy sự hy sinh làm lá chắn và dùng chiếc đầu phẳng làm bức tường thành bất khả xâm phạm! |  | Bản hùng ca sinh tồn: chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu đứng giữa ánh hào quang chiến thắng với biểu tượng quả bom tự hủy và bức tường thành đầu phẳng. |
| b03 | 00:14.1–00:21.4 (7.3s) | L60 | Báo cáo điệp báo gia tộc: Đạt điểm 10 cho lòng trung thành và kỷ luật quân đội thép! Ký tên: ông trùm thế giới vòm rừng! | **ĐIỂM 10** · kỷ luật quân đội thép · R/350 · [0.65, 0.45] | Dấu mộc đỏ ĐẠT ĐIỂM 10 đóng lên tập hồ sơ đế chế; cả gia tộc kiến vòm rừng vẫy cờ ăn mừng kỷ luật quân đội thép. |
| b04 | 00:21.4–00:33.3 (11.9s) | L61 | Còn anh em thì sao? Nếu được chỉ huy một đội quân sinh học: anh em chọn đội cảm tử nổ tung keo độc vàng, hay đội lính gác đầu phẳng hình phích cắm bất khả xâm phạm? Hãy để lại bình luận bên dưới nhé! Hồ sơ đế chế số 28 |  | Hai bàn cân lựa chọn: BÊN TRÁI biểu tượng quả bom nổ keo vàng; BÊN PHẢI biểu tượng chiếc đầu phẳng cắm chốt cửa hang, khán giả giơ thẻ bình chọn. |
| b05 | 00:33.3–00:41.2 (7.9s) | L62 | xin được khép lại tại đây. Nhưng tập sau, chúng ta sẽ quay trở lại phòng thí nghiệm 5 cấp độ để chứng kiến một phép màu sinh học đảo ngược quy luật thời gian của vũ trụ! |  | Tập hồ sơ số 28 được niêm phong cẩn thận, ánh đèn chuyển sang ánh sáng neon tím của phòng thí nghiệm 5 cấp độ sinh tử. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này. |
| b06 | 00:41.2–00:46.5 (5.3s) | L63 | Một sinh vật nhỏ xíu trong suốt như giọt nước trôi lơ lửng giữa đại dương, nhưng nắm giữ bí mật bất tử vĩ đại nhất: |  | Một sinh vật bí ẩn được vẽ hoàn toàn bằng BÓNG ĐEN ĐẶC TUYỀN (solid black silhouette) hình chiếc chuông sứa nhỏ xíu trong suốt như giọt nước đang bơi lơ lửng giữa biển xanh; kèm dấu hỏi chấm vàng to tướng; KHÔNG vẽ mắt miệng hay màu thật. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này. |
| b07 | 00:46.5–00:54.5 (8.0s) | L64 | khi già yếu hoặc bị thương nặng, nó không chết đi mà tự đảo ngược toàn bộ tế bào của mình quay trở lại thời kỳ ấu trùng sơ sinh để sống lại từ đầu một cuộc đời mới! |  | Cũng chiếc BÓNG ĐEN ĐẶC TUYỀN (solid black silhouette) hình chuông sứa đó tự co cụm lại, xoay ngược bánh xe thời gian biến thành một khối búp polyp ấu trùng sơ sinh để sống lại từ đầu; dấu hỏi chấm to tướng. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này. |
| b08 | 00:54.5–00:59.3 (4.8s) | L65 | Đố các bạn biết bóng đen bí ẩn kỳ sau là loài vật nào? Hãy đoán ngay ở phần bình luận nhé! |  | Chiếc BÓNG ĐEN ĐẶC TUYỀN bí ẩn có khả năng đảo ngược thời gian bất tử nằm giữa ba dấu hỏi chấm lớn lấp lánh vàng cam mời gọi khán giả đoán tên con vật tập sau. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này. |

## 5. Phân cảnh Shorts — từng beat

Banner: **TỰ NỔ TUNG CƠ THỂ / PHUN KEO ĐỘC BẢO VỆ TỔ?!** · giọng 44.0s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Những chiến binh kiến nhỏ bé này sẵn sàng tự gồng cơ bụng nổ tung cơ thể mình như bom cảm tử để tiêu diệt kẻ thù! |  |
| s02 | 00:06.5 | S02 | Xin giới thiệu Kiến Nổ Cảm Tử, sinh vật sống trên những ngọn cây cao 50m ở rừng mưa Đông Nam Á. | **CAO 50M** · vòm rừng nhiệt đới · R/620 · [0.62, 0.5] |
| s03 | 00:12.5 | S03 | Cơ thể nó mang một cặp túi dự trữ chất nhầy khổng lồ chạy dọc từ hàm xuống tận khoang bụng. |  |
| s04 | 00:17.1 | S04 | Khi bị kẻ săn mồi bao vây, nó lao tới cắn chặt đối thủ rồi gồng rách lớp vỏ bụng |  |
| s05 | 00:21.5 | S05 | để phóng ra một dòng keo độc màu vàng tươi cực dính! |  |
| s06 | 00:24.9 | S06 | Dòng keo này khóa cứng hoàn toàn chân tay và làm ngạt thở kẻ địch chỉ trong vài giây! |  |
| s07 | 00:29.4 | S07 | Trong khi đó, ở cửa tổ, những chú kiến lính có chiếc đầu phẳng lì hình nút chai |  |
| s08 | 00:33.5 | S08 | sẽ cắm chặt đầu vào lỗ cây để làm cánh cửa sống chặn đứng mọi kẻ đột nhập! |  |
| s09 | 00:37.6 | S09 | Một đế chế cảm tử vừa biết nổ tung tự sát, vừa dùng đầu làm cửa |  |
| s10 | 00:41.1 | S10 | thành, đúng là đội quân liều chết kỳ quặc nhất hành tinh! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong thế giới ngầm của rừng mưa nhiệt đới Borneo, có những gia tộc sinh tồn bằng những đạo luật nghiệt ngã đến rợn người.". Bố cục: Đáy rừng mưa nhiệt đới Borneo tăm tối mù sương: những thân cây đại thụ vươn thẳng lên trời xanh chọc thủng tầng mây, không khí rừng thiêng nước độc bí hiểm. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tại những ngọn cây cổ thụ cao 40-50m chọc thủng tầng mây, một đế chế khổng lồ với hàng trăm ngàn thần dân đang vận hành theo một nguyên tắc tối thượng: Kẻ sinh ra ở tầng đáy thấp nhất... phải là kẻ sẵn sàng nổ tung thân xác để bảo vệ ngai vàng của bà trùm!". Bố cục: Trên những ngọn cây cổ thụ cao 40-50m chọc thủng tầng mây, hàng trăm ngàn chú kiến đang di chuyển tấp nập như một đế chế quân đội vĩ đại.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo bà trùm, đội lính thợ dò đường đã tiến vào khu vực tranh chấp, sẵn sàng nhận lệnh tử vì đạo!". Bố cục: BÊN TRÁI một chú kiến thợ nhỏ bé đeo tai nghe bộ đàm cúi đầu chào; BÊN PHẢI bà trùm kiến chúa khổng lồ màu vàng nâu quý phái đội vương miện nhỏ nằm uy nghi trên ngai vàng trong thân gỗ. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bật màn hình chỉ huy lên, hôm nay chúng ta giải mã hồ sơ của đội quân cảm tử trung thành nhất hành tinh!". Bố cục: Màn hình radar chỉ huy hiển thị bản đồ tổ kiến trên các tán cây rừng mưa nhiệt đới Borneo phát sáng huỳnh quang. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Xin giới thiệu với toàn thể anh em: đây là Kiến Nổ Cảm Tử, tên khoa học là Colobopsis explodens, thuộc nhóm kiến thợ nổ đặc hữu của vùng rừng mưa Đông Nam Á như Brunei, Malaysia và Thái Lan.". Bố cục: chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu đứng oai vệ trên cành cây lá xanh, thắt chiếc băng đô đỏ cảm tử trên trán, dáng đứng kiêu hãnh của một chiến binh thực thụ.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Dù kích thước cơ thể chỉ bé bằng hạt gạo, nhưng trong giới côn trùng học, chúng tôi gọi thẳng tên nó bằng biệt danh: Chiến Binh Cảm Tử!". Bố cục: Ở GIỮA chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu đứng cạnh một hạt gạo trắng tinh để so sánh kích thước bé nhỏ bằng nhau, xung quanh có dải ruy băng danh hiệu Chiến Binh Cảm Tử.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Điều gì đã khiến một loài kiến nhỏ bé không hề có nọc châm độc ở đuôi lại khiến những tập đoàn kiến vàng dệt lá hung hãn nhất phải khiếp vía bỏ chạy?". Bố cục: Chia đôi: BÊN TRÁI đạo quân kiến vàng dệt lá hung dữ giơ càng to; BÊN PHẢI chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu nhỏ bé nhưng khiến đối phương hoảng sợ lùi bước.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bí mật nằm ở thứ vũ khí tự hủy giấu kín bên trong khoang bụng: một quả bom sinh học chứa keo độc màu vàng sẵn sàng phát nổ trong chớp mắt!". Bố cục: Mặt cắt giải phẫu trong suốt của chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu: bên trong khoang bụng gaster chứa một quả bom sinh học màu vàng tươi phát sáng rực rỡ chuẩn bị kích nổ.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đêm nay, tôi mời anh em cùng lật mở 4 tầng cấu trúc quyền lực của đế chế cảm tử này!". Bố cục: Mô hình 4 tầng cấu trúc quyền lực của đế chế kiến mở ra như một pháo đài nhiều tầng trên thân cây cổ thụ. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trên những tầng tán rừng rậm rạp cao chót vót cách mặt đất tới 50-60m, sự tranh giành từng giọt mật hoa và từng tấc cành cây diễn ra tàn bạo từng giây từng phút.". Bố cục: Cảnh tượng vòm cây rậm rạp cao 50-60m: các nhánh cây đan xen nhau giữa lưng chừng trời, nơi diễn ra cuộc chiến tranh giành mật hoa tàn bạo.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không có chỗ cho sự khoan nhượng hay đàm phán hòa bình.". Bố cục: Hai chú kiến đối địch trừng mắt nhìn nhau trên cành cây hẹp, không khí căng thẳng nghẹt thở không có chỗ cho khoan nhượng. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một khi đã bước chân vào hàng ngũ lính thợ cảm tử, mỗi cá thể đều hiểu rõ bản án sinh tử đã được định sẵn ngay từ ngày chui ra khỏi kén ấu trùng!". Bố cục: chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu vừa chui ra khỏi chiếc kén ấu trùng màu trắng, lập tức được thắt chiếc băng đô đỏ cảm tử trên đầu, đôi mắt ánh lên quyết tâm sắt đá.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tầng cấu trúc thứ 1: Đội quân lính thợ mang quả bom cơ thể! Trong hệ thống phân cấp của gia tộc Colobopsis, những chú kiến thợ nhỏ bé này chiếm số lượng đông đảo nhất, ngày đêm bò trên những cành cây cao chót vót để kiếm mật hoa và tìm kiếm nguồn thức ăn thừa.". Bố cục: Bảng hồ sơ hiện TẦNG CẤU TRÚC 1: ĐỘI QUÂN LÍNH THỢ MANG QUẢ BOM CƠ THỂ; hàng ngàn chú kiến thợ nhỏ bé bò trên cành cây kiếm mật hoa. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng đằng sau vẻ ngoài cần mẫn ấy là một cấu tạo giải phẫu kỳ dị bậc nhất thế giới động vật!". Bố cục: Kính hiển vi phóng to cấu tạo giải phẫu kỳ dị bên trong cơ thể chú kiến thợ nhỏ bé cần mẫn. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "2018, một công trình chấn động công bố trên tạp chí ZooKeys bởi tiến sĩ Alice Laciny đã giải mã hoàn chỉnh cấu trúc bên trong cơ thể Chiến Binh Cảm Tử: chạy dọc suốt từ phần hàm dưới xuyên qua lồng ngực xuống tận khoang bụng là một cặp túi dự trữ chất nhầy khổng lồ của tuyến hàm dưới!". Bố cục: Bìa tạp chí ZooKeys năm 2018 mở ra bản vẽ giải phẫu của tiến sĩ Alice Laciny: cặp túi dự trữ chất nhầy khổng lồ chạy từ hàm xuống bụng. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cặp túi hóa chất này phình to đến mức chiếm phần lớn thể tích bên trong cơ thể chú kiến, đẩy các cơ quan nội tạng khác dồn về một góc chật chội!". Bố cục: Sơ đồ cơ thể chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu: cặp túi tuyến phình to chiếm hầu hết không gian trong thân, đẩy dạ dày và ruột dồn nép vào một góc chật chội.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bên trong túi chứa đầy một dung dịch keo dính màu vàng tươi có mùi cay nồng nặc như gia vị cà ri, chứa đầy các hợp chất hữu cơ độc hại đủ sức thiêu đốt và làm tê liệt các loài chân khớp khác!". Bố cục: Dung dịch keo dính màu vàng tươi bốc khói cay nồng như gia vị cà ri bên trong túi tuyến, chứa các phân tử hóa chất độc hại phát sáng. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó sống cả cuộc đời để nuôi dưỡng một kho hóa chất tự hủy sẵn sàng kích nổ!". Bố cục: chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu vừa đi kiếm ăn vừa mang vác kho hóa chất tự hủy căng phồng trong bụng, luôn sẵn sàng kích nổ.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Điều kỳ thú là bên trong dung dịch keo độc này còn nuôi dưỡng những quần thể vi khuẩn cộng sinh đặc biệt giúp ổn định độc tính và giữ cho khối keo luôn ở trạng thái lỏng nhớt hoàn hảo.". Bố cục: Kính hiển vi siêu vi khuẩn: những quần thể vi khuẩn cộng sinh đặc biệt sống bên trong túi keo giúp bảo quản độ nhớt hoàn hảo. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chừng nào túi tuyến còn nguyên vẹn, chú kiến vẫn sinh hoạt bươn chải bình thường. Nhưng chiếc ngòi nổ sinh học thì luôn được cài sẵn ở chế độ nhạy cảm cao nhất!". Bố cục: chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu sinh hoạt bình thường trên tán lá nhưng chiếc ngòi nổ sinh học màu đỏ trên bụng luôn chớp sáng nhạy bén.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà khoa học từng quan sát thấy những chú kiến thợ già cỗi khi khả năng kiếm ăn giảm sút sẽ tự nguyện nhận những nhiệm vụ tuần tra nguy hiểm nhất ở bìa ngoài cùng của lãnh thổ.". Bố cục: Những chú kiến thợ già cỗi râu bạc bước ra ranh giới ngoài cùng của lãnh thổ để tuần tra canh gác tiền tuyến. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một sự phân công lao động tàn khốc nhưng hoàn hảo đến mức lạnh gáy: đem những quả bom sắp hết hạn ra tiền tuyến làm lá chắn đầu tiên cho tổ quốc!". Bố cục: Hàng rào lính thợ già dũng cảm đứng chắn bảo vệ bầy đàn phía sau; một sự phân công lao động hoàn hảo và lạnh gáy. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Để tiếp cận và nghiên cứu được biệt đội cảm tử này, các nhà côn trùng học quốc tế đã phải trèo lên những chiếc cẩu tháp nghiên cứu vòm rừng dựng giữa rừng nguyên sinh Brunei ở độ cao hơn 50m!". Bố cục: Chiếc cẩu tháp nghiên cứu vòm rừng cao hơn 50m dựng giữa rừng nguyên sinh Brunei chọc thẳng lên mây xanh. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Họ phải đu dây lơ lửng giữa không trung suốt hàng tuần liền để đặt bẫy và ghi hình từng hành vi nhỏ nhất của những quả bom di động tí hon này!". Bố cục: Các nhà khoa học quốc tế đu dây lơ lửng giữa không trung cách mặt đất 50m, cầm kính lúp và máy quay quan sát những chú kiến tí hon. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tầng cấu trúc thứ 2: Hiện tượng tự nổ tung cơ thể Autothysis!". Bố cục: Bảng hồ sơ hiện TẦNG CẤU TRÚC 2: HIỆN TƯỢNG TỰ NỔ TUNG AUTOTHYSIS; chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu đơn độc tuần tra trên phiến lá xanh biếc.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi đang tuần tra đơn độc trên tán lá rừng, nếu chẳng may bị một con nhện săn mồi hay một con kiến quân đội đối thủ bao vây áp sát không lối thoát, Chiến Binh Cảm Tử sẽ không hề van xin tha mạng hay tìm cách tháo chạy hèn nhát!". Bố cục: Một con nhện săn mồi lông lá to lớn và kiến đối thủ bất ngờ xuất hiện bao vây chặn đứng đường lui của chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gã lập tức áp sát vào cơ thể kẻ địch, dùng hàm dưới cắn chặt vào chân hoặc râu của đối phương để khóa chết mục tiêu!". Bố cục: chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu lao thẳng vào kẻ địch, dùng hai chiếc hàm dưới sắc bén cắn chặt cứng vào chân con nhện để khóa chặt mục tiêu.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sau đó, gã gồng cực mạnh toàn bộ các bó cơ thành bụng... Bùm! Áp lực co bóp kinh hoàng làm nứt toạc lớp vỏ chitin ở phần bụng, xé rách màng túi tuyến và phóng ra một dòng keo độc màu vàng tươi bắn thẳng vào mặt kẻ thù!". Bố cục: Bùm! chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu gồng cực mạnh cơ bụng làm nứt toạc lớp vỏ chitin, xé rách túi tuyến và phát nổ giải phóng dòng keo độc màu vàng rực rỡ.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Dòng keo dính màu vàng này bám chặt cứng vào mắt, râu và các khớp chân của đối thủ, đông cứng lại như một lớp keo dán sắt cực độc chỉ sau vài giây!". Bố cục: Dòng keo vàng tươi dính chặt cứng bọc kín mắt, râu và chân của con nhện săn mồi, keo đông cứng lại như lớp keo dán sắt chỉ sau vài giây.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kẻ săn mồi hoảng loạn giãy giụa nhưng càng cựa quậy thì các khớp chân càng bị keo dính chặt khóa bất động! Hóa chất cay nồng ngấm vào các lỗ thở làm kẻ địch ngạt thở tê liệt và chết gục ngay tại chỗ!". Bố cục: Con nhện giãy giụa bất lực trong đống keo dính vàng đặc quánh, hóa chất cay nồng ngấm vào lỗ thở làm nó tê liệt ngã gục tại chỗ. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chiến Binh Cảm Tử đã hy sinh ngay khoảnh khắc vụ nổ diễn ra. Nhưng gã đã hoàn thành xuất sắc nhiệm vụ của một quả bom sống: tiêu diệt sạch sẽ mối đe dọa và". Bố cục: Ánh sáng hào quang tôn vinh sự hy sinh oanh liệt của quả bom sống chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu, tiêu diệt hoàn toàn kẻ thù hung ác.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "gửi đi một thông điệp đẫm máu tới toàn bộ kẻ thù trong rừng: Đừng bao giờ đụng vào gia tộc này!". Bố cục: Biển cảnh báo màu đỏ hình chiếc đầu lâu cắm trên cành cây: thông điệp đẫm máu khiến muôn loài kẻ thù không dám xâm phạm. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mùi hương cay nồng giải phóng từ vụ nổ không chỉ thiêu đốt kẻ địch mà còn đóng vai trò như một tín hiệu báo động đỏ lan tỏa trong không khí.". Bố cục: Những làn sóng mùi hương cay nồng màu vàng lan tỏa trong không khí như tín hiệu báo động đỏ khẩn cấp khắp vòm lá.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Những chú kiến thợ tuần tra xung quanh ngửi thấy mùi đặc trưng liền lập tức giương râu cảnh giác, tạo thành một hàng rào phòng ngự thứ 2 sẵn sàng tiếp ứng nếu đối thủ kéo thêm viện binh!". Bố cục: Đội quân kiến thợ tuần tra xung quanh đồng loạt giương râu cảnh giác, tạo thành một hàng rào phòng ngự thứ 2 kiên cố sẵn sàng chiến đấu.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong lịch sử sinh học, tập tính tự sát bảo vệ bầy đàn này được nhà tự nhiên học người Đức ghi nhận lần đầu tiên từ 1916.". Bố cục: Cuốn sổ tay ghi chép cổ điển của nhà tự nhiên học người Đức năm 1916 với hình vẽ chú kiến tự nổ tung cơ thể đầu tiên. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trải qua hơn một thế kỷ nghiên cứu, con người vẫn chưa hết bàng hoàng trước cái giá sinh tồn nghiệt ngã mà tự nhiên đã tôi luyện nên cho loài kiến thợ nhỏ bé này!". Bố cục: Dòng thời gian một thế kỷ nghiên cứu: loài người nghiêng mình thán phục trước giá trị sinh tồn nghiệt ngã của loài kiến cảm tử; bảng Tầng 2 bật PASS. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tầng cấu trúc thứ 3: Kẻ gác cổng hình nút chai sống! Nếu bên ngoài vòm cây là nơi lính thợ nhỏ nổ tung thân xác, thì ngay tại cửa tổ sổ gỗ trên thân cây cổ thụ, gia tộc này bố trí một lực lượng phòng thủ thụ động đỉnh cao mang tên kiến lính đầu phẳng!". Bố cục: Bảng hồ sơ hiện TẦNG CẤU TRÚC 3: KẺ GÁC CỔNG HÌNH NÚT CHAI SỐNG; cửa tổ sổ gỗ hình tròn trên thân cây cổ thụ. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy quan sát hiện tượng cơ thể Phragmosis: phần đầu của những chú kiến lính này tiến hóa thành một chiếc đĩa tròn dẹt phẳng lì, phủ lớp vỏ cứng như gỗ và có kích thước khít khao 100% với lỗ khoét cửa tổ trên thân cây!". Bố cục: Cận cảnh đầu của chú kiến lính đầu phẳng phragmotic hoạt hình màu nâu đậm, đầu hình chiếc đĩa tròn phẳng lì như nút chai: chiếc đầu tiến hóa thành một chiếc đĩa tròn dẹt phẳng lì phủ lớp vỏ cứng như gỗ, khít khao 100% với miệng lỗ tổ cây.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gã lính gác dùng chính chiếc đầu của mình cắm chặt vào lỗ cây như một chiếc nút chai rượu vang đóng chặt cửa hầm!". Bố cục: chú kiến lính đầu phẳng phragmotic hoạt hình màu nâu đậm, đầu hình chiếc đĩa tròn phẳng lì như nút chai cắm chặt đầu mình vào lỗ cây tròn như chiếc nút bần đóng chặt miệng chai rượu vang, thân mình giấu kín bên trong hầm.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo gác cổng: Có kẻ địch đang cào cấu bên ngoài đòi đột nhập, chiếc đầu thép của em vẫn chốt cứng kín kẽ!". Bố cục: Bên ngoài kẻ thù cào cấu điên cuồng lên chiếc đầu phẳng lì của chú kiến lính đầu phẳng phragmotic hoạt hình màu nâu đậm, đầu hình chiếc đĩa tròn phẳng lì như nút chai, chiếc đầu chốt cứng kín kẽ như bức tường gỗ bất khả xâm phạm.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kẻ thù bên ngoài dù có hung hãn đến đâu cũng chỉ nhìn thấy một mảng vỏ cây phẳng lì trơn trượt, cắn không có chỗ bám, đẩy không tài nào lay chuyển nổi!". Bố cục: Kẻ địch hung hãn dùng hàm cắn trượt trên mảng đầu phẳng trơn trượt của chú kiến lính đầu phẳng phragmotic hoạt hình màu nâu đậm, đầu hình chiếc đĩa tròn phẳng lì như nút chai, đẩy mãi không lay chuyển nổi.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chỉ khi nào những chú kiến thợ cùng tổ đi kiếm ăn trở về, dùng râu gõ đúng nhịp mật mã bí mật lên trán,". Bố cục: chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu đi kiếm ăn trở về, dùng hai chiếc râu gõ đúng nhịp mật mã bí mật lên trán chú kiến lính đầu phẳng phragmotic hoạt hình màu nâu đậm, đầu hình chiếc đĩa tròn phẳng lì như nút chai để xin mở cửa.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "gã lính gác mới lùi nhẹ đầu vào trong mở lối cho đồng đội bước vào rồi lập tức cắm chốt đóng sập cửa lại!". Bố cục: chú kiến lính đầu phẳng phragmotic hoạt hình màu nâu đậm, đầu hình chiếc đĩa tròn phẳng lì như nút chai lùi nhẹ đầu vào trong mở khe hở cho đồng đội bước vào rồi lập tức cắm đầu đóng sập cửa hầm lại an toàn.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Suốt cả cuộc đời mình, những gã kiến lính đầu phẳng này hầu như không bao giờ bước chân ra khỏi ngưỡng cửa tổ!". Bố cục: chú kiến lính đầu phẳng phragmotic hoạt hình màu nâu đậm, đầu hình chiếc đĩa tròn phẳng lì như nút chai cả đời đứng im bên ngưỡng cửa tổ, thân mình to bè làm then cửa sống bảo vệ hàng ngàn ấu trùng nhỏ bé bên trong.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chúng ăn thức ăn do kiến thợ mớm lại qua đường miệng, và nhiệm vụ duy nhất từ lúc trưởng thành đến lúc nhắm mắt xuôi tay là làm một chiếc then cửa sống kiên cố bảo vệ sự bình yên cho hàng ngàn ấu trùng bên trong!". Bố cục: Kiến thợ mớm thức ăn giọt mật qua miệng cho chú kiến lính đầu phẳng phragmotic hoạt hình màu nâu đậm, đầu hình chiếc đĩa tròn phẳng lì như nút chai thưởng thức bữa ăn ấm cúng ngay tại vị trí chốt gác.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu gã lính gác chẳng may bị kẻ thù dùng càng nhổ ra ngoài hoặc tử trận, một chú lính đầu phẳng dự bị ở phía sau sẽ lập tức tiến lên trám đúng vị trí, cắm đầu bịt kín lỗ cây chỉ trong vài giây! Một hệ thống cửa hầm phòng thủ tự động thay thế không bao giờ để lộ khe hở cho kẻ đột nhập!". Bố cục: Một chú lính đầu phẳng dự bị từ phía sau lập tức tiến lên cắm đầu trám đúng vị trí chỉ trong vài giây; bảng Tầng 3 bật PASS. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tầng cấu trúc thứ 4: Cuộc chiến tranh lãnh thổ khốc liệt nhất vòm rừng!". Bố cục: Bảng hồ sơ hiện TẦNG CẤU TRÚC 4: CUỘC CHIẾN TRANH LÃNH THỔ KHỐC LIỆT NHẤT VÒM RỪNG; hai đạo quân kiến đối đầu nghẹt thở. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kẻ thù truyền kiếp số một của gia tộc Colobopsis là những đạo quân kiến vàng dệt lá Oecophylla khổng lồ và hung bạo.". Bố cục: Đạo quân con kiến vàng dệt lá Oecophylla hung dữ nhiều gai kiến vàng dệt lá khổng lồ hung tợn tràn ngập các cành cây giương hàm đe dọa lãnh thổ.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong những trận đụng độ giáp lá cà trên tán lá cao 50m,". Bố cục: Chiến trường giáp lá cà trên tán lá cao 50m: những quả bom cảm tử của chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu đồng loạt kích nổ bùng lên những vệt sáng vàng rực.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "hàng trăm Chiến Binh Cảm Tử sẵn sàng đồng loạt kích nổ bụng, biến chiến trường thành một bãi mìn keo vàng chết chóc để ngăn bước quân thù!". Bố cục: Bãi mìn keo vàng chết chóc phong tỏa toàn bộ cành cây, bọc cứng hàng chục con kiến vàng dệt lá xâm lăng ngăn bước quân thù.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sự hy sinh vị tha tột cùng này chỉ phục vụ cho một mục tiêu thiêng liêng duy nhất: Bảo vệ ngai vàng của Bà Trùm — kiến chúa mẫu nghi thiên hạ đang nằm sâu trong lõi thân cây gỗ cổ thụ!". Bố cục: Sâu trong lõi thân cây gỗ cổ thụ: bà trùm kiến chúa khổng lồ màu vàng nâu quý phái đội vương miện nhỏ nằm uy nghi trên ngai vàng lộng lẫy được bảo vệ an toàn tuyệt đối.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kiến chúa là trái tim của cả đế chế, người đẻ ra hàng ngàn quả trứng mỗi ngày để liên tục bổ sung lực lượng cảm tử mới. Mất đi vài ngàn lính thợ chẳng là gì, miễn là bà trùm vẫn an toàn đẻ trứng!". Bố cục: bà trùm kiến chúa khổng lồ màu vàng nâu quý phái đội vương miện nhỏ cần mẫn đẻ ra hàng ngàn quả trứng nhỏ màu trắng mỗi ngày, các vú nuôi chăm sóc cẩn thận bổ sung quân đoàn mới. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đây là đỉnh cao của sự tiến hóa xã hội bậc cao: một cá thể sẵn sàng tự hủy diệt bản thân để duy trì sự trường tồn vĩnh cửu của cả tổ chức gia tộc! Đúng là tinh thần trung thành tuyệt đối khiến con người khi nhìn vào cũng phải rùng mình nể sợ!". Bố cục: Biểu tượng gia tộc kiến với tinh thần đoàn kết bất diệt: hàng ngàn bàn tay kiến nắm chặt bảo vệ vương miện đế chế.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vào mùa giao phối sau những cơn mưa rào nhiệt đới, đế chế sẽ cho ra đời những công chúa và hoàng tử kiến có cánh bay vút lên bầu trời đêm để tìm kiếm bạn đời lập nên những vương quốc mới.". Bố cục: Bầu trời đêm sau cơn mưa rào: những công chúa và hoàng tử kiến có cánh bay lượn rực rỡ tìm kiếm bạn đời lập vương quốc mới. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Những thế hệ cảm tử tiếp theo lại tiếp tục sinh ra, kế thừa trọn vẹn bản thiết kế bom sinh học để tiếp tục thống trị vòm rừng nhiệt đới!". Bố cục: Những thế hệ kiến cảm tử tiếp theo liên tục chui ra khỏi kén ấu trùng, kế thừa trọn vẹn bản thiết kế bom sinh học để tiếp tục thống trị vòm rừng.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một tổ kiến Colobopsis trưởng thành có thể chiếm giữ cả một cụm cây dầu cổ thụ khổng lồ, kết nối với nhau bằng những tuyến đường mòn hóa học chạy dọc theo các nhánh dây leo trên không.". Bố cục: Cụm cây dầu cổ thụ khổng lồ liên kết với nhau bằng những con đường mòn hóa học chạy dọc các nhánh dây leo trên không. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này.
```
</details>

<details><summary>L57</summary>

```text
HÌNH L57 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hàng trăm ngàn cá thể phối hợp nhịp nhàng như một siêu sinh vật duy nhất, nơi lợi ích của cá nhân hoàn toàn biến mất trước sự tồn vong bất diệt của cả đế chế!". Bố cục: Hàng trăm ngàn cá thể phối hợp nhịp nhàng như một cỗ máy siêu sinh vật duy nhất; bảng Tầng 4 bật PASS rực rỡ. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này.
```
</details>

<details><summary>L58</summary>

```text
HÌNH L58 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tổng kết hồ sơ đế chế số 28.". Bố cục: Bàn chỉ huy thế giới ngầm vòm rừng: bản tổng kết hồ sơ đế chế số 28 mở ra với biểu tượng chú kiến nổ quả cảm. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này.
```
</details>

<details><summary>L59</summary>

```text
HÌNH L59 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Từ một loài côn trùng nhỏ bé trên vòm cây rừng Borneo, Kiến Nổ Cảm Tử đã viết nên một bản hùng ca sinh tồn bi tráng bậc nhất tự nhiên: biến cơ thể thành bom, lấy sự hy sinh làm lá chắn và dùng chiếc đầu phẳng làm bức tường thành bất khả xâm phạm!". Bố cục: Bản hùng ca sinh tồn: chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu đứng giữa ánh hào quang chiến thắng với biểu tượng quả bom tự hủy và bức tường thành đầu phẳng.
```
</details>

<details><summary>L60</summary>

```text
HÌNH L60 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo điệp báo gia tộc: Đạt điểm 10 cho lòng trung thành và kỷ luật quân đội thép! Ký tên: ông trùm thế giới vòm rừng!". Bố cục: Dấu mộc đỏ ĐẠT ĐIỂM 10 đóng lên tập hồ sơ đế chế; cả gia tộc kiến vòm rừng vẫy cờ ăn mừng kỷ luật quân đội thép.
```
</details>

<details><summary>L61</summary>

```text
HÌNH L61 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn anh em thì sao? Nếu được chỉ huy một đội quân sinh học: anh em chọn đội cảm tử nổ tung keo độc vàng, hay đội lính gác đầu phẳng hình phích cắm bất khả xâm phạm? Hãy để lại bình luận bên dưới nhé! Hồ sơ đế chế số 28". Bố cục: Hai bàn cân lựa chọn: BÊN TRÁI biểu tượng quả bom nổ keo vàng; BÊN PHẢI biểu tượng chiếc đầu phẳng cắm chốt cửa hang, khán giả giơ thẻ bình chọn.
```
</details>

<details><summary>L62</summary>

```text
HÌNH L62 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "xin được khép lại tại đây. Nhưng tập sau, chúng ta sẽ quay trở lại phòng thí nghiệm 5 cấp độ để chứng kiến một phép màu sinh học đảo ngược quy luật thời gian của vũ trụ!". Bố cục: Tập hồ sơ số 28 được niêm phong cẩn thận, ánh đèn chuyển sang ánh sáng neon tím của phòng thí nghiệm 5 cấp độ sinh tử. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này.
```
</details>

<details><summary>L63</summary>

```text
HÌNH L63 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một sinh vật nhỏ xíu trong suốt như giọt nước trôi lơ lửng giữa đại dương, nhưng nắm giữ bí mật bất tử vĩ đại nhất:". Bố cục: Một sinh vật bí ẩn được vẽ hoàn toàn bằng BÓNG ĐEN ĐẶC TUYỀN (solid black silhouette) hình chiếc chuông sứa nhỏ xíu trong suốt như giọt nước đang bơi lơ lửng giữa biển xanh; kèm dấu hỏi chấm vàng to tướng; KHÔNG vẽ mắt miệng hay màu thật. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này.
```
</details>

<details><summary>L64</summary>

```text
HÌNH L64 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "khi già yếu hoặc bị thương nặng, nó không chết đi mà tự đảo ngược toàn bộ tế bào của mình quay trở lại thời kỳ ấu trùng sơ sinh để sống lại từ đầu một cuộc đời mới!". Bố cục: Cũng chiếc BÓNG ĐEN ĐẶC TUYỀN (solid black silhouette) hình chuông sứa đó tự co cụm lại, xoay ngược bánh xe thời gian biến thành một khối búp polyp ấu trùng sơ sinh để sống lại từ đầu; dấu hỏi chấm to tướng. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này.
```
</details>

<details><summary>L65</summary>

```text
HÌNH L65 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đố các bạn biết bóng đen bí ẩn kỳ sau là loài vật nào? Hãy đoán ngay ở phần bình luận nhé!". Bố cục: Chiếc BÓNG ĐEN ĐẶC TUYỀN bí ẩn có khả năng đảo ngược thời gian bất tử nằm giữa ba dấu hỏi chấm lớn lấp lánh vàng cam mời gọi khán giả đoán tên con vật tập sau. KHÔNG có chú kiến đeo băng đô đỏ trong cảnh này.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Những chiến binh kiến nhỏ bé này sẵn sàng tự gồng cơ bụng nổ tung cơ thể mình như bom cảm tử để tiêu diệt kẻ thù!". Bố cục: Khung dọc: chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu lao tới con nhện săn mồi, gồng cơ bụng phát nổ tung cơ thể như bom cảm tử.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Xin giới thiệu Kiến Nổ Cảm Tử, sinh vật sống trên những ngọn cây cao 50m ở rừng mưa Đông Nam Á.". Bố cục: chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu đứng kiêu hãnh trên ngọn cây cao 50m vòm rừng Đông Nam Á, chiếc thước đo chiều cao màu vàng dựng thẳng bên cạnh.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Cơ thể nó mang một cặp túi dự trữ chất nhầy khổng lồ chạy dọc từ hàm xuống tận khoang bụng.". Bố cục: Đồ họa giải phẫu trong suốt: cặp túi nhầy khổng lồ màu vàng chạy dọc từ hàm dưới xuống tận khoang bụng.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Khi bị kẻ săn mồi bao vây, nó lao tới cắn chặt đối thủ rồi gồng rách lớp vỏ bụng để". Bố cục: chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu cắn chặt vào chân kẻ thù rồi gồng nứt toạc lớp vỏ bụng phát ra tiếng nổ bùm.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "phóng ra một dòng keo độc màu vàng tươi cực dính!". Bố cục: Dòng keo độc màu vàng tươi cực dính bắn xối xả vào mắt và chân kẻ thù, dán chặt đối phương bất động.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Dòng keo này khóa cứng hoàn toàn chân tay và làm ngạt thở kẻ địch chỉ trong vài giây!". Bố cục: Kẻ địch giãy giụa trong mớ keo dán sắt vàng đặc quánh, các lỗ thở bị bít kín nghẹt thở.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Trong khi đó, ở cửa tổ, những chú kiến lính có chiếc đầu phẳng lì hình nút chai sẽ". Bố cục: chú kiến lính đầu phẳng phragmotic hoạt hình màu nâu đậm, đầu hình chiếc đĩa tròn phẳng lì như nút chai với chiếc đầu phẳng dẹt hình nút chai đứng chốt tại miệng tổ cây.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "cắm chặt đầu vào lỗ cây để làm cánh cửa sống chặn đứng mọi kẻ đột nhập!". Bố cục: chú kiến lính đầu phẳng phragmotic hoạt hình màu nâu đậm, đầu hình chiếc đĩa tròn phẳng lì như nút chai cắm đầu bịt kín mít lỗ cây như nắp nút chai, kẻ thù cào cấu bên ngoài không tài nào đột nhập.
```
</details>

<details><summary>S09</summary>

```text
HÌNH S09 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Một đế chế cảm tử vừa biết nổ tung tự sát, vừa dùng đầu làm cửa thành,". Bố cục: Hai nửa khung dọc: phía trên là bom cảm tử nổ tung; phía dưới là then cửa đầu phẳng kiên cố bảo vệ bà trùm.
```
</details>

<details><summary>S10</summary>

```text
HÌNH S10 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Kiến Nổ Cảm Tử nâu đỏ, bụng cam căng tròn, băng đô đỏ cảm tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "đúng là đội quân liều chết kỳ quặc nhất hành tinh!". Bố cục: Chân dung chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu thắt băng đô đỏ cảm tử giơ nắm tay quả cảm, ánh hào quang chiến binh anh hùng rực sáng.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/65 của video YouTube về Kiến Nổ Cảm Tử). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu. Nhân vật phụ cố định: chú kiến lính đầu phẳng phragmotic hoạt hình màu nâu đậm, đầu hình chiếc đĩa tròn phẳng lì như nút chai; bà trùm kiến chúa khổng lồ màu vàng nâu quý phái đội vương miện nhỏ; con kiến vàng dệt lá Oecophylla hung dữ nhiều gai. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/10 của video YouTube Shorts về Kiến Nổ Cảm Tử). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Kiến Nổ Cảm Tử (Colobopsis explodens) hoạt hình màu nâu đỏ, đầu to tròn với đôi mắt đen sắc sảo, cặp râu cong linh hoạt, phần bụng gaster căng tròn màu cam đỏ, đeo một chiếc băng đô đỏ thắt nơ kiểu cảm tử quân dũng cảm trên đầu. Nhân vật phụ: chú kiến lính đầu phẳng phragmotic hoạt hình màu nâu đậm, đầu hình chiếc đĩa tròn phẳng lì như nút chai. 
```
</details>

## 7. SEO

- **title:** Loài Kiến Tự Kích Nổ Tung Cơ Thể Phun Keo Độc Bảo Vệ Tổ?!
- **hook_paragraph:** Kiến Nổ Cảm Tử (Colobopsis explodens) ở rừng mưa Borneo sở hữu cơ chế tự sát Autothysis rùng rợn: tự gồng rách vỏ bụng nổ tung phóng dòng keo độc màu vàng dính chặt kẻ thù, cùng đội lính gác đầu phẳng hình nút chai dùng đầu làm cửa sống!
- **question:** Nếu được chỉ huy 1 lực lượng của Kiến Nổ: đội quân cảm tử nổ tung keo độc hay đội lính gác đầu phẳng cắm chốt cửa hang, bạn chọn bên nào? Và đoán xem bóng đen tập sau là loài nào?
- **next_teaser:** Bóng đen sinh vật bất tử: khi già yếu tự đảo ngược toàn bộ tế bào thành ấu trùng sơ sinh để sống lại từ đầu!
- **shorts_title:** Loài Kiến Tự Nổ Tung Cơ Thể Phun Keo Độc?! 🐜 #độngvật #kiếnnổcảmtử
- **shorts_desc:** Kiến Nổ Cảm Tử tự gồng rách vỏ bụng nổ tung phóng dòng keo độc vàng khóa chặt kẻ thù, cùng kiến lính đầu phẳng dùng đầu làm cánh cửa sống! Giải mã đội quân cảm tử rừng mưa Đông Nam Á.
- **bullets:** Hồ sơ đế chế: Tuyến hàm dưới khổng lồ chạy dọc cơ thể chứa keo độc màu vàng · Cú nổ Autothysis: Gồng rách vỏ bụng chitin phóng keo dính khóa cứng kẻ săn mồi · Hiện tượng Phragmosis: Kiến lính đầu phẳng cắm chốt bịt kín lỗ cây như nắp nút chai · Đại chiến vòm cây: Hy sinh bầy đàn trước kiến vàng Oecophylla để bảo vệ kiến chúa
- **tags:** kiến nổ cảm tử, kien no cam tu, colobopsis explodens, exploding ants, kiến tự nổ, kiến đầu phẳng, động vật kỳ lạ, thế giới động vật, động vật hài hước, vẽ chuyện hoang dã, whiteboard animation, khoa học thú vị
- **hashtags:** #độngvật #kiếnnổcảmtử #VẽChuyệnHoangDã

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-28-kien-no-cam-tu
python src/episode/pipeline.py tts    projects/tap-28-kien-no-cam-tu     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-28-kien-no-cam-tu     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-28-kien-no-cam-tu     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-28-kien-no-cam-tu              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-28-kien-no-cam-tu --force
python scripts/beat_sheet.py projects/tap-28-kien-no-cam-tu               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-28-kien-no-cam-tu/audio/shorts.wav projects/tap-28-kien-no-cam-tu/renders/tap-28-kien-no-cam-tu_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-28-kien-no-cam-tu
python src/episode/pipeline.py seo    projects/tap-28-kien-no-cam-tu
python src/episode/episode_doc.py     projects/tap-28-kien-no-cam-tu
```
