# TẬP 12 — HÀ MÃ · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-12-ha-ma`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-12-ha-ma`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F7` · **Persona giọng:** `binh_luan_vien` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Hà Mã |
| Tiêu đề YouTube | Cỗ Xe Tăng 3 Tấn Cắn Đôi Cá Sấu Nhưng Không Biết Bơi?! \| Hà Mã \| Tập 12 |
| Video dài | `renders/tap-12-ha-ma_long.mp4` — 9:04.2 (544.2s) |
| Shorts | `renders/tap-12-ha-ma_shorts.mp4` — 0:43.9 (43.9s) |
| Thumbnail | `renders/tap-12-ha-ma_thumbnail.jpg` |
| Số hình | dài 68 beat / 68 ảnh riêng; Shorts 10 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.1**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/68 của video YouTube về Hà Mã). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực. Nhân vật phụ cố định: anh chàng bình luận viên esports hoạt hình đeo tai nghe gaming có micro, mặc áo vest thể thao sành điệu, hào hứng bình luận; cô phát thanh viên tin tức hoạt hình xinh đẹp ngồi sau bàn trường quay; gã đấu sĩ gấu xám khổng lồ cơ bắp cuồn cuộn đang đứng khoanh tay ngạc nhiên. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — TUYỂN THỦ XE TĂNG XUẤT ĐÀI & CÚ LỪA KHÔNG BIẾT BƠI
*Thẻ chương:* CỖ XE TĂNG BỌC THỊT BƯỚC VÀO SÀN ĐẤU

*Badge:* `VÕ ĐÀI CHÂU PHI` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene01_p0.wav` (682 ký tự) · mood `hao_hung`

```text
Kính thưa quý vị khán giả đang theo dõi Đấu Trường Sinh Tồn! Tuyển thủ hạng siêu nặng của chúng ta đã chính thức bước vào sàn đấu! Hãy hướng ống kính về phía dòng sông châu Phi rực lửa, nơi một khối cơ bắp khổng lồ nặng tới ba tấn vừa trồi lên khỏi mặt nước! Đó chính là Hà Mã — sinh vật được mệnh danh là Cỗ xe tăng bọc thịt của giới tự nhiên! Nhìn dáng vẻ tròn ủng, lùn tịt và bốn cái chân ngắn cũn cỡn, nhiều khán giả trên khán đài có thể tưởng rằng gã béo này vô hại như một chú heo mọi khổng lồ. Nhưng xin cảnh báo ngay: đây là cỗ máy chiến đấu cục súc và nguy hiểm bậc nhất lục địa đen, sở hữu bảng chỉ số khiến mọi kẻ săn mồi thượng thừa cũng phải toát mồ hôi hột! [laughter]
```
**Part 1** → `audio/vs/scene01_p1.wav` (112 ký tự) · 🎭 cameo `phat_thanh_vien`

```text
Alo bình luận viên ơi, nghe đồn tuyển thủ này sống dưới nước suốt ngày nhưng lại... hoàn toàn không biết bơi hả?
```
**Part 2** → `audio/vs/scene01_p2.wav` (568 ký tự) · mood `don_dap`

```text
[surprise-oh] Báo cáo trường quay, đó là sự thật một trăm phần trăm! Đây chính là cú lừa kinh điển nhất mà tạo hóa dành cho giới sinh học: một loài vật ngâm mình dưới nước tới mười sáu tiếng mỗi ngày, nhưng lại tuyệt đối không biết bơi, thậm chí không thể tự nổi trên mặt nước! Khung xương của nó quá đặc và nặng đến mức ném xuống nước là chìm nghỉm như một khối đá tảng! Vậy làm thế nào Cỗ xe tăng bọc thịt có thể di chuyển thần tốc dưới lòng sông? [question-ah] Hãy cùng chúng tôi mở bảng chỉ số RPG để giải mã toàn bộ bí mật sức mạnh điên rồ của đấu sĩ vô địch này!
```

### scene02 — BẢNG THÔNG SỐ RPG CỰC HẠN CỦA QUÁI VẬT 3 TẤN
*Thẻ chương:* BẢNG CHỈ SỐ RPG CHẠM NÓC ĐẤU TRƯỜNG

*Badge:* `CHỈ SỐ CHIẾN ĐẤU` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene02_p0.wav` (515 ký tự) · mood `don_dap`

```text
Chỉ số chiến đấu đã lên bảng điện tử! Xin mời toàn thể khán đài nín thở theo dõi thông số kỹ thuật của Cỗ xe tăng bọc thịt! Về lượng máu sinh lực HP: chạm nóc chín ngàn chín trăm điểm! Với trọng lượng cơ thể dao động từ một tấn rưỡi đến ba tấn, cơ thể của nó là một khối thịt và mỡ đồ sộ, được nâng đỡ bởi hệ thống xương đặc biệt dày và nặng nhất thế giới động vật trên cạn. Khối lượng khủng khiếp này biến nó thành một bức tường thành di động mà chẳng có loài săn mồi nào có thể húc đổ trong một đòn! [surprise-wa]
```
**Part 1** → `audio/vs/scene02_p1.wav` (490 ký tự) · mood `hao_hung`

```text
Về sức mạnh tấn công ATK: đạt mức tối đa chín ngàn tám trăm điểm! Được trang bị lực cắn kinh hoàng lên tới một ngàn tám trăm PSI, kết hợp với cặp răng nanh hàm dưới dài tới năm mươi xăng-ti-mét nhọn hoắt như hai lưỡi giáo thép! Về phòng thủ DEF: chín ngàn năm trăm điểm nhờ lớp da dày tới năm xăng-ti-mét! Còn về tốc độ SPD thì sao? Đừng để thân hình béo tròn đánh lừa: trên cạn nó có thể bứt tốc ba mươi cây số một giờ, nhanh hơn cả vận động viên chạy nước rút của con người! [surprise-oh]
```
**Part 2** → `audio/vs/scene02_p2.wav` (528 ký tự) · mood `don_dap`

```text
Nhưng nghịch lý hài hước nhất nằm ở chỉ số bơi lội: bằng không điểm tròn trĩnh! Thay vì bơi quẫy đạp như cá hay rái cá, Cỗ xe tăng bọc thịt chọn cách... chạy bộ và phi nước đại dưới đáy sông với tốc độ tám cây số một giờ! Các nhà giải phẫu học phát hiện xương chân và xương sườn của hà mã đặc quánh gần như không có khoang tủy xốp, đóng vai trò y hệt chiếc đai chì của thợ lặn chuyên nghiệp. Nó nhẹ nhàng nhún ngón chân xuống nền cát đáy nước rồi đẩy cả khối thân ba tấn lướt đi êm ái như một vũ công ba-lê dưới nước! [laughter]
```
**Part 3** → `audio/vs/scene02_p3.wav` (527 ký tự) · mood `hao_hung`

```text
Mỗi lần chìm xuống, nó có thể nhịn thở liên tục năm phút đồng hồ. Thậm chí khi ngủ gật dưới nước, một phản xạ vô thức tự động đẩy cơ thể nó trồi lên mặt nước hít một hơi rồi lại chìm xuống ngủ tiếp mà không hề tỉnh giấc! Chưa hết, âm thanh gầm rú của tuyển thủ dưới nước có thể đạt mức một trăm mười lăm đề-xi-ben ngang ngửa một buổi hòa nhạc nhạc rock, truyền đồng thời qua cả môi trường nước lẫn không khí để răn đe mọi đối thủ trong bán kính hàng cây số! Đúng là phong cách của bậc thầy lười biếng thượng thừa! [surprise-wa]
```

### scene03 — DA DÀY 5CM VÀ LỚP KEM CHỐNG NẮNG MỒ HÔI MÁU
*Thẻ chương:* LỚP GIÁP BỌC THÉP VÀ DUNG DỊCH MỒ HÔI MÁU

*Badge:* `GIÁP PHÒNG THỦ` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene03_p0.wav` (487 ký tự) · mood `hao_hung`

```text
Chuyển sang phân tích hệ thống phòng thủ độc quyền của tuyển thủ! Quý vị hãy nhìn vào lớp da trần trụi không có lông của Cỗ xe tăng bọc thịt! Đây không phải là da thịt thông thường, mà là một tấm giáp bọc thép sinh học dày tới năm xăng-ti-mét! Lớp da dày và dai như lốp xe tải này có thể chống đỡ răng nanh sắc nhọn của cả đàn sư tử đói, và trong quá khứ, ngay cả những viên đạn chì súng trường cổ điển bắn vào cũng bị trượt văng ra ngoài mà không thể xuyên thủng nội tạng! [surprise-wa]
```
**Part 1** → `audio/vs/scene03_p1.wav` (116 ký tự) · 🎭 cameo `ga_khong_lo`

```text
Khoan đã bình luận viên ơi, nhìn trên người tuyển thủ kìa, có phải nó đang bị chảy máu đầm đìa khắp toàn thân không?
```
**Part 2** → `audio/vs/scene03_p2.wav` (572 ký tự) · mood `don_dap`

```text
Bác đấu sĩ khổng lồ chớ vội hốt hoảng! Đó không phải là máu, mà là một trong những phát minh hóa học vi diệu nhất hành tinh: lớp mồ hôi máu huyền thoại! Tuyển thủ của chúng ta không có tuyến mồ hôi thông thường. Khi trời nắng gắt, các lỗ chân lông đặc biệt trên da sẽ tiết ra một chất lỏng nhớt màu đỏ rực như máu. Các nhà khoa học phân tích phát hiện dung dịch này chứa hai loại axit cực hiếm: một loại hấp thụ hoàn toàn tia cực tím độc hại, hoạt động như một lớp kem chống nắng tự nhiên chỉ số cực cao; loại còn lại là chất kháng sinh diệt khuẩn siêu mạnh! [surprise-oh]
```
**Part 3** → `audio/vs/scene03_p3.wav` (619 ký tự) · mood `hao_hung`

```text
Tại sao lại cần trang bị kỳ lạ này? Bởi vì lớp da của hà mã mất nước nhanh gấp bảy lần da con người nếu rời khỏi môi trường ẩm ướt! Nếu không ngâm mình dưới nước hoặc bôi lớp kem mồ hôi đỏ này, da nó sẽ nứt toác và rỉ máu thật sự dưới cái nắng thiêu đốt của châu Phi! Nhờ có lớp kem chống nắng kiêm thuốc sát trùng thần thánh này, Cỗ xe tăng bọc thịt có thể ngâm mình hàng giờ trong những vũng bùn bẩn thỉu đầy vi khuẩn mà vết thương cắn xé nhau không bao giờ bị nhiễm trùng! Vừa bọc giáp năm xăng-ti-mét, vừa tự bôi kem chống nắng kiêm thuốc sát trùng, đúng là tuyển thủ biết yêu chiều bản thân nhất võ đài! [laughter]
```

### scene04 — LỰC CẮN 1.800 PSI VÀ CÚ CHẠY BỘ 30KM/H
*Thẻ chương:* CÚ ĐỚP 1.800 PSI BẺ ĐÔI MỌI VẬT CẢN

*Badge:* `VŨ KHÍ TỬ THẦN` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene04_p0.wav` (564 ký tự) · mood `don_dap`

```text
Bây giờ, xin mời quý vị chiêm ngưỡng vũ khí sát thương khủng khiếp nhất của tuyển thủ! Hãy nhìn vào chiếc mồm khổng lồ kia: nó có thể mở rộng tới một góc một trăm tám mươi độ — tức là mở toang hoác thành một đường thẳng tắp rộng hơn một mét! Bên trong chiếc mồm đỏ lòm là một kho vũ khí cận chiến chết chóc: hai chiếc răng nanh hàm dưới dài tới năm mươi xăng-ti-mét, cong vút và sắc nhọn như hai mũi ngọn giáo kim loại! Đôi răng này không dùng để nhai cỏ, mà là vũ khí chiến đấu thuần túy, liên tục tự mài sắc vào nhau mỗi khi tuyển thủ ngậm mồm lại! [surprise-oh]
```
**Part 1** → `audio/vs/scene04_p1.wav` (438 ký tự) · mood `don_dap`

```text
Và khi chiếc hàm cơ bắp kia đóng sập xuống, nó tạo ra một lực cắn khủng khiếp: một ngàn tám trăm PSI! Con số này mạnh gấp ba lần lực cắn của một con sư tử đực trưởng thành, và mạnh gấp mười lần cú cắn của con người! Một cú đớp toàn lực của Cỗ xe tăng bọc thịt đủ sức bẻ gãy đôi một chiếc thuyền độc mộc của ngư dân, nghiền nát mai rùa cứng như đá, hoặc cắn đứt đôi thân mình một con cá sấu dài ba mét chỉ trong một chớp mắt! [surprise-wa]
```
**Part 2** → `audio/vs/scene04_p2.wav` (365 ký tự) · mood `hao_hung`

```text
Để nhắm bắn chuẩn xác, đầu của hà mã còn có một thiết kế radar đỉnh cao: mắt, tai và lỗ mũi nằm trên cùng một đường thẳng ngang ở đỉnh đầu! Thiết kế này hoạt động y hệt kính tiềm vọng của tàu ngầm quân sự, cho phép tuyển thủ giấu chín mươi lăm phần trăm cơ thể khổng lồ dưới mặt nước mà vẫn quan sát trọn vẹn ba trăm sáu mươi độ mọi động tĩnh trên bờ! [surprise-oh]
```
**Part 3** → `audio/vs/scene04_p3.wav` (459 ký tự) · mood `hao_hung`

```text
Và điều trớ trêu nhất là gì? Dù sở hữu vũ khí hủy diệt hạng nặng như vậy, tuyển thủ của chúng ta lại là một... kẻ ăn chay chính hiệu! Ban đêm khi mặt trời lặn, nó lững thững leo lên bờ và dành suốt sáu tiếng đồng hồ chỉ để gặm cỏ non, nạp khoảng bốn mươi lăm cân cỏ mỗi đêm! Răng nanh năm mươi xăng-ti-mét để cắn đôi kẻ thù, nhưng dạ dày thì chỉ thích chứa cỏ xanh! Một sự kết hợp đầy mâu thuẫn giữa vẻ ngoài hung tợn và tâm hồn ăn chay thanh tịnh! [laughter]
```

### scene05 — CẮN ĐÔI CÁ SẤU VÀ TUYỆT CHIÊU QUẠT ĐUÔI PHÂN
*Thẻ chương:* CÁ SẤU CHÂU PHI TOÁT MỒ HÔI TRÁNH XA

*Badge:* `ĐẠI CHIẾN NẢY LỬA` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene05_p0.wav` (588 ký tự) · mood `don_dap`

```text
Hãy cùng theo dõi những thước phim thực chiến nghẹt thở từ võ đài sông Nile! Trong thế giới hoang dã châu Phi, cá sấu sông Nile được coi là bạo chúa đầm lầy, nhưng khi gặp Cỗ xe tăng bọc thịt, mọi định kiến đều bị đập tan tành! Đã có vô số cảnh quay ghi lại cảnh những con cá sấu khổng lồ bơi lỡ bước vào lãnh địa của đàn hà mã, và ngay lập tức bị tuyển thủ của chúng ta lao tới ngoạm ngang lưng, cắn nát bộ giáp gai và quăng quật như một món đồ chơi! Ngay cả loài sư tử dũng mãnh, nếu dám bén mảng lại gần hà mã con, cũng sẽ bị cả bầy hà mã lao lên bờ rượt đuổi chạy tóe khói! [laughter]
```
**Part 1** → `audio/vs/scene05_p1.wav` (427 ký tự) · mood `nghiem_trang_gia`

```text
Theo thống kê của các nhà bảo tồn, Cỗ xe tăng bọc thịt là loài động vật có vú nguy hiểm bậc nhất châu Phi, khiến khoảng năm trăm người thiệt mạng mỗi năm — nhiều hơn cả sư tử, báo hoa mai và voi gộp lại! Tính khí của nó cực kỳ thất thường và có tính sở hữu lãnh thổ cực đoan: bất kỳ ai dám đứng chắn giữa nó và dòng nước cứu sinh đều sẽ phải đối mặt với một cỗ xe ba tấn lao tới với tốc độ ba mươi cây số một giờ! [surprise-wa]
```
**Part 2** → `audio/vs/scene05_p2.wav` (580 ký tự) · mood `bi_hai`

```text
Nhưng chiêu thức hài hước và bốc mùi nhất võ đài chính là tuyệt kỹ đánh dấu chủ quyền: cỗ máy quạt đuôi phân thần thánh! Tuyển thủ sở hữu một chiếc đuôi ngắn dẹt hoạt động y hệt một chiếc cánh quạt trực thăng. Mỗi khi đi vệ sinh, nó sẽ vừa xả phân vừa vung chiếc đuôi quay tít mù với tốc độ cao, quạt tung tóe các mảnh phân và nước tiểu bắn xa từ hai đến ba mét xung quanh để thông báo cho cả vùng biết: lãnh địa này đã có chủ! [laughter] Kẻ thù nhìn thấy cảnh tượng đó không chỉ khiếp sợ sức mạnh, mà còn phải ôm mũi bỏ chạy vì mức độ ô nhiễm không khí quá nặng nề! [surprise-oh]
```
**Part 3** → `audio/vs/scene05_p3.wav` (415 ký tự) · mood `hao_hung`

```text
Ấy thế mà, thỉnh thoảng gã cục súc này lại có những hành động trượng nghĩa khó tin! Các nhà thám hiểm từng ghi lại cảnh hà mã lao vào tấn công cá sấu để giải cứu một chú linh dương đầu bò đang bị kéo xuống nước, thậm chí xua đuổi cả đàn linh cẩu để bảo vệ một chú ngựa vằn bị thương! Dữ dằn số một châu Phi, nhưng đôi khi lại hành xử như một vị cảnh sát trưởng đầy nghĩa khí giữa thiên nhiên hoang dã! [surprise-wa]
```

### scene06 — ĐAI VÔ ĐỊCH VÀ BÓNG ĐEN BÍ ẨN TẬP TIẾP THEO
*Thẻ chương:* BẬT MÍ BÓNG ĐEN BÍ ẨN CỦA ĐẤU THỦ TẬP 13

*Badge:* `BẢNG VÀNG & BÓNG ĐEN` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene06_p0.wav` (556 ký tự) · mood `am_ap`

```text
Và trận đấu đã khép lại! Trọng tài xin trịnh trọng trao chiếc đai vô địch hạng siêu nặng cho Cỗ xe tăng bọc thịt Hà Mã! Một đấu sĩ hội tụ đủ mọi yếu tố không tưởng: ba tấn cơ bắp, mồ hôi chống nắng màu đỏ, lực cắn một ngàn tám trăm PSI nghiền nát cá sấu, và một gia tộc có họ hàng ruột thịt gần gũi nhất với loài cá voi đại dương! Chúng tách ra từ một tổ tiên chung cách đây năm mươi lăm triệu năm: một nhánh bơi hẳn ra biển khơi tiến hóa thành cá voi khổng lồ, còn nhánh kia ở lại đầm lầy châu Phi trở thành cỗ xe tăng bất khả chiến bại này! [surprise-oh]
```
**Part 1** → `audio/vs/scene06_p1.wav` (249 ký tự) · mood `hao_hung`

```text
Chiếc đai vô địch Tập mười hai đã có chủ! Nhưng đấu trường sinh tồn sẽ không bao giờ dừng lại! Ngay bây giờ, xin mời toàn thể khán đài hướng mắt lên màn hình lớn để chiêm ngưỡng BÓNG ĐEN BÍ ẨN của tuyển thủ tiếp theo trong Tập mười ba! [surprise-oh]
```
**Part 2** → `audio/vs/scene06_p2.wav` (537 ký tự) · mood `don_dap`

```text
Xin đưa ra ba manh mối chấn động về bóng đen bí ẩn này: Thứ nhất, đây là sinh vật sống chậm chạp bậc nhất hành tinh, với tốc độ kỷ lục chỉ không phẩy hai cây số một giờ, đến mức rêu xanh và cả một hệ sinh thái bướm đêm mọc um tùm ngay trên lớp lông của nó! Thứ hai, mỗi tuần nó chỉ chịu leo xuống đất đi vệ sinh đúng một lần duy nhất, mỗi lần đi xả tới một phần ba trọng lượng cơ thể! Và thứ ba, nghịch lý bi hài nhất: hơn một nửa số cái chết trong cuộc đời của sinh vật này đều xảy ra... đúng vào lúc nó xuống đất đi vệ sinh! [laughter]
```
**Part 3** → `audio/vs/scene06_p3.wav` (258 ký tự) · mood `hao_hung`

```text
Quý vị khán giả có đoán ra bóng đen bí ẩn này là quái kiệt nào của thế giới tự nhiên không? Hãy để lại dự đoán và phán quyết của bạn ngay dưới phần bình luận nhé! Bình luận viên xin chào tạm biệt và hẹn gặp lại toàn thể quý vị trên sàn đấu rực lửa tiếp theo!
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Một sinh vật nặng tới ba tấn ngâm mình dưới nước mười sáu tiếng mỗi ngày, nhưng lại hoàn toàn không biết bơi! Đó chính là Hà Mã, cỗ xe tăng bọc thịt hung hãn nhất đầm lầy châu Phi! Xương của nó đặc và nặng đến mức ném xuống nước là chìm nghỉm như một khối đá tảng, nên thay vì bơi, nó chọn cách chạy bộ dưới đáy sông với tốc độ tám cây số một giờ! [surprise-wa] Trên bờ, nó có thể bứt tốc ba mươi cây số một giờ, sở hữu lớp da dày năm xăng-ti-mét chống đạn và tự tiết ra lớp mồ hôi đỏ rực như máu để chống nắng kiêm diệt khuẩn. Đáng sợ nhất là lực cắn một ngàn tám trăm PSI gấp ba lần sư tử, kết hợp cặp răng nanh năm mươi xăng-ti-mét đủ sức cắn đứt đôi một con cá sấu dài ba mét chỉ trong một chớp mắt! [laughter] Vậy là bí mật đã rõ: hà mã không cần học bơi, vì dưới đáy sông hay trên cạn, nó sinh ra đã là một cỗ xe bọc thép bất khả chiến bại của tự nhiên!
```

**Whisper prompt:** `Hà Mã, Cỗ xe tăng bọc thịt, Hippopotamus, 1.800 PSI, 50cm, 180 độ, 3 tấn, 5cm, 30km/h, 8km/h, mồ hôi máu, blood sweat, cá voi, Cetacea, quạt đuôi phân, cá sấu, Châu Phi, đai vô địch, bóng đen bí ẩn`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| một ngàn tám trăm | 1.800 |
| Một ngàn tám trăm | 1.800 |
| năm mươi xăng-ti-mét | 50cm |
| Năm mươi xăng-ti-mét | 50cm |
| một trăm tám mươi độ | 180° |
| Một trăm tám mươi độ | 180° |
| ba tấn | 3 tấn |
| Ba tấn | 3 tấn |
| một tấn rưỡi | 1,5 tấn |
| Một tấn rưỡi | 1,5 tấn |
| năm xăng-ti-mét | 5cm |
| Năm xăng-ti-mét | 5cm |
| ba mươi cây số một giờ | 30km/h |
| Ba mươi cây số một giờ | 30km/h |
| tám cây số một giờ | 8km/h |
| Tám cây số một giờ | 8km/h |
| năm phút | 5 phút |
| Năm phút | 5 phút |
| bốn mươi lăm cân | 45kg |
| Bốn mươi lăm cân | 45kg |
| năm trăm | 500 |
| Năm trăm | 500 |
| năm mươi lăm triệu năm | 55 triệu năm |
| Năm mươi lăm triệu năm | 55 triệu năm |
| ba mét | 3m |
| Ba mét | 3m |
| hai mét | 2m |
| Hai mét | 2m |
| ba mét rưỡi | 3,5m |
| hai đến ba mét | 2-3m |
| ba lần | 3 lần |
| Ba lần | 3 lần |
| bảy lần | 7 lần |
| Bảy lần | 7 lần |
| mười lần | 10 lần |
| Mười lần | 10 lần |
| chín mươi lăm phần trăm | 95% |
| một trăm phần trăm | 100% |
| chín ngàn chín trăm điểm | 9.900 điểm |
| chín ngàn tám trăm điểm | 9.800 điểm |
| chín ngàn năm trăm điểm | 9.500 điểm |
| mười sáu tiếng | 16 tiếng |
| Mười sáu tiếng | 16 tiếng |
| sáu tiếng | 6 tiếng |
| Sáu tiếng | 6 tiếng |
| hai mươi tư trên bảy | 24/7 |
| một tuần | 1 tuần |
| Một tuần | 1 tuần |
| một lần | 1 lần |
| Một lần | 1 lần |
| một phần ba | 1/3 |
| Một phần ba | 1/3 |
| không phẩy hai cây số một giờ | 0,2km/h |
| Không phẩy hai cây số một giờ | 0,2km/h |
| một trăm mười lăm | 115 |
| ba trăm sáu mươi | 360 |
| Tập mười hai | Tập 12 |
| Tập mười ba | Tập 13 |
| hàng triệu năm | hàng triệu năm |
| triệu năm | triệu năm |
| Hà Mã | Hà Mã |
| P-S-I | PSI |
| A-T-K | ATK |
| D-E-F | DEF |
| H-P | HP |
| S-P-D | SPD |
| Xê-ta-xê-a | Cetacea |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · TUYỂN THỦ XE TĂNG XUẤT ĐÀI & CÚ LỪA KHÔNG BIẾT BƠI · 67.3s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:03.4 (3.4s) | L01 | Kính thưa quý vị khán giả đang theo dõi Đấu Trường Sinh Tồn! |  | Sàn đấu võ đài hoang dã sông Nile châu Phi lúc hoàng hôn: ánh đèn rực lửa, cờ phướn bay phấp phới; anh chàng bình luận viên esports hoạt hình đeo tai nghe gaming có micro, mặc áo vest thể thao sành điệu, hào hứng bình luận đeo tai nghe gaming đứng trước bục micro phát thanh viên giơ tay chỉ xuống dòng sông. |
| b02 | 00:03.4–00:06.7 (3.3s) | L02 | Tuyển thủ hạng siêu nặng của chúng ta đã chính thức bước vào sàn đấu! |  | Mặt nước sông Nile sủi bọt cuồn cuộn như có núi lửa ngầm; các loài chim nước bay tán loạn giật mình hoảng hốt. |
| b03 | 00:06.7–00:13.6 (6.9s) | L03 | Hãy hướng ống kính về phía dòng sông châu Phi rực lửa, nơi một khối cơ bắp khổng lồ nặng tới 3 tấn vừa trồi lên khỏi mặt nước! | **3 TẤN** · khối lượng cơ bắp · R/360 · [0.72, 0.45] | chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực khổng lồ nặng tới 3 tấn từ từ trồi người lên khỏi mặt nước sông rực lửa, hai cánh tay đ |
| b04 | 00:13.6–00:17.9 (4.3s) | L04 | Đó chính là Hà Mã — sinh vật được mệnh danh là Cỗ xe tăng bọc thịt của giới tự nhiên! |  | Chân dung cận cảnh oai phong của chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực: thân hình tròn ủng đồ sộ như một cỗ xe tăng bọc thép  |
| b05 | 00:17.9–00:26.0 (8.1s) | L05 | Nhìn dáng vẻ tròn ủng, lùn tịt và bốn cái chân ngắn cũn cỡn, nhiều khán giả trên khán đài có thể tưởng rằng gã béo này vô hại như một chú heo mọi khổng lồ. |  | So sánh hài hước: BÊN TRÁI một chú heo mọi mũm mĩm hiền lành ăn cám; BÊN PHẢI chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực đứng sừng |
| b06 | 00:26.0–00:35.5 (9.5s) | L06 | Nhưng xin cảnh báo ngay: đây là cỗ máy chiến đấu cục súc và nguy hiểm bậc nhất lục địa đen, sở hữu bảng chỉ số khiến mọi kẻ săn mồi thượng thừa cũng phải toát mồ hôi hột! |  | Bản đồ lục địa Châu Phi đỏ rực lửa: hình bóng chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực phủ bóng đen khổng lồ lên khắp thảo nguyê |
| b07 | 00:35.5–00:41.7 (6.2s) | L07 | Alo bình luận viên ơi, nghe đồn tuyển thủ này sống dưới nước suốt ngày nhưng lại... hoàn toàn không biết bơi hả? |  | Trường quay tin tức thời sự: cô phát thanh viên tin tức hoạt hình xinh đẹp ngồi sau bàn trường quay ngồi sau bàn kính hiện đại cầm bút chỉ lên màn hình kết nối hiện trường, ngơ ngác đặt câu hỏi. |
| b08 | 00:41.7–00:54.1 (12.4s) | L09 | Báo cáo trường quay, đó là sự thật 100%! Đây chính là cú lừa kinh điển nhất mà tạo hóa dành cho giới sinh học: một loài vật ngâm mình dưới nước tới 16 tiếng mỗi ngày, nhưng lại tuyệt đối không biết bơi, thậm chí không thể tự nổi trên mặt nước! | **100%** · sự thật khó tin · L/380 · [0.4, 0.5]<br>**16 TIẾNG** · ngâm nước mỗi ngày · R/360 · [0.65, 0.45] | Cảnh sông nước: chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực ngâm mình dưới nước 16 tiếng mỗi ngày, xung quanh nổi bóng đồng hồ báo  |
| b09 | 00:54.1–00:58.2 (4.1s) | L10 | Khung xương của nó quá đặc và nặng đến mức ném xuống nước là chìm nghỉm như một khối đá tảng! |  | Cảnh minh họa vật lý: một hòn đá tảng to đùng rơi xuống nước chìm nghỉm tận đáy; bên cạnh bộ xương hà mã dày đặc cũng chìm thẳng đứng xuống đáy sông không chút nổi bồng bềnh. |
| b10 | 00:58.2–01:02.4 (4.2s) | L11 | Vậy làm thế nào Cỗ xe tăng bọc thịt có thể di chuyển thần tốc dưới lòng sông? |  | chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực bước đi thoăn thoắt dưới đáy sông trong làn nước xanh trong vắt, bụi cát đáy sông bốc l |
| b11 | 01:02.4–01:07.3 (5.0s) | L12 | Hãy cùng chúng tôi mở bảng chỉ số RPG để giải mã toàn bộ bí mật sức mạnh điên rồ của đấu sĩ vô địch này! |  | anh chàng bình luận viên esports hoạt hình đeo tai nghe gaming có micro, mặc áo vest thể thao sành điệu, hào hứng bình luận vung tay kích hoạt bảng điện tử RPG phát sáng rực rỡ; thanh đo HP, ATK, DEF, SPD hiện lên lấp lánh như trò chơi điện tử đấu trường. |

### scene02 · BẢNG THÔNG SỐ RPG CỰC HẠN CỦA QUÁI VẬT 3 TẤN · 101.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:02.2 (2.2s) | L13 | Chỉ số chiến đấu đã lên bảng điện tử! |  | Bảng giao diện chỉ số RPG võ đài hiện ra hoành tráng: chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực đứng ở trung tâm sàn đấu, hai bên |
| b02 | 00:02.2–00:06.1 (3.9s) | L14 | Xin mời toàn thể khán đài nín thở theo dõi thông số kỹ thuật của Cỗ xe tăng bọc |  | Khán đài hàng ngàn khán giả thú rừng và các bạn nhỏ hoạt hình nín thở ngước nhìn màn hình LED khổng lồ rực rỡ. |
| b03 | 00:06.1–00:09.1 (3.0s) | L15 | thịt! Về lượng máu sinh lực HP: chạm nóc 9.900 điểm! | **HP 9.900** · sinh lực tối thượng · L/360 · [0.35, 0.45] | Thanh máu HP đỏ rực chạm nóc tối đa: con số 9.900 điểm nhấp nháy phát sáng; chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực đứng vỗ ngự |
| b04 | 00:09.1–00:17.9 (8.7s) | L16 | Với trọng lượng cơ thể dao động từ 1,5 tấn đến 3 tấn, cơ thể của nó là một khối thịt và mỡ đồ sộ, được nâng đỡ bởi hệ thống xương đặc biệt dày và nặng nhất thế giới động vật trên cạn. | **1,5 TẤN** · cân nặng tối thiểu · L/380 · [0.35, 0.6]<br>**3 TẤN** · cân nặng tối đa · R/480 · [0.7, 0.5] | Cân tải trọng khổng lồ: chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực đứng lên chiếc cân làm kim đồng hồ quay tít mù chỉ vào mốc 1,5  |
| b05 | 00:17.9–00:24.0 (6.2s) | L17 | Khối lượng khủng khiếp này biến nó thành một bức tường thành di động mà chẳng có loài săn mồi nào có thể húc đổ trong một đòn! |  | chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực đứng vững như bàn thạch; một chú tê giác hung hãn lao vào húc nhưng bị dội ngược lại ng |
| b06 | 00:24.0–00:28.6 (4.5s) | L18 | Về sức mạnh tấn công ATK: đạt mức tối đa 9.800 điểm! | **ATK 9.800** · sức tấn công cực hạn · L/360 · [0.35, 0.45] | Thanh chỉ số ATK màu cam bốc cháy hừng hực: đạt 9.800 điểm; chiếc mồm khổng lồ mở rộng khoe cặp răng nanh nhọn hoắt như hai ngọn giáo thép. |
| b07 | 00:28.6–00:36.1 (7.6s) | L19 | Được trang bị lực cắn kinh hoàng lên tới 1.800 PSI, kết hợp với cặp răng nanh hàm dưới dài tới 50cm nhọn hoắt như hai lưỡi giáo thép! | **1.800 PSI** · lực cắn cực hạn · L/360 · [0.35, 0.5]<br>**50 CM** · chiều dài răng nanh · R/480 · [0.72, 0.45] | Máy đo lực cắn phát nổ tóe lửa: kim đo chỉ mốc 1.800 PSI; bên dưới là thước đo cặp răng nanh dài 50cm cắm sâu vào tảng đá. |
| b08 | 00:36.1–00:39.9 (3.8s) | L20 | Về phòng thủ DEF: 9.500 điểm nhờ lớp da dày tới 5cm! | **DEF 9.500** · phòng thủ bọc thép · L/360 · [0.35, 0.45]<br>**5 CM** · độ dày lớp da · R/480 · [0.65, 0.55] | Thanh DEF màu xanh dương đạt 9.500 điểm; lớp da dày 5cm được vẽ như tấm giáp thép bọc quanh người tuyển thủ. |
| b09 | 00:39.9–00:49.5 (9.6s) | L21 | Còn về tốc độ SPD thì sao? Đừng để thân hình béo tròn đánh lừa: trên cạn nó có thể bứt tốc 30km/h, nhanh hơn cả vận động viên chạy nước rút của con người! | **30 KM/H** · bứt tốc trên cạn · R/380 · [0.7, 0.45] | chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực bứt tốc chạy nước rút trên đồng cỏ châu Phi: bụi đất mù mịt phía sau, vượt qua một vận  |
| b10 | 00:49.5–00:56.2 (6.7s) | L22 | Nhưng nghịch lý hài hước nhất nằm ở chỉ số bơi lội: bằng không điểm tròn trĩnh! Thay vì bơi quẫy đạp như cá hay rái cá, Cỗ |  | Thanh bơi lội SWIM hiện số 0 điểm tròn trĩnh nhấp nháy màu đỏ; chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực chìm nghỉm dưới đáy sông |
| b11 | 00:56.2–01:00.2 (4.0s) | L23 | xe tăng bọc thịt chọn cách... chạy bộ và phi nước đại dưới đáy sông với tốc độ 8km/h! | **8 KM/H** · phi nước đại đáy sông · L/380 · [0.4, 0.5] | Đáy sông trong vắt: chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực đang nhún ngón chân nhẹ nhàng phi nước đại lướt trên cát đáy nước v |
| b12 | 01:00.2–01:14.0 (13.8s) | L24 | Các nhà giải phẫu học phát hiện xương chân và xương sườn của hà mã đặc quánh gần như không có khoang tủy xốp, đóng vai trò y hệt chiếc đai chì của thợ lặn chuyên nghiệp. Nó nhẹ nhàng nhún ngón chân xuống nền cát đáy nước rồi đẩy cả khối thân 3 tấn lướt đi êm ái như một vũ công ba-lê dưới nước! |  | Sơ đồ X-quang xương hà mã: các thanh xương sườn và xương ống chân đặc quánh màu trắng đặc không có lỗ xốp, cạnh đó là chiếc đai chì của thợ lặn. |
| b13 | 01:14.0–01:17.5 (3.5s) | L25 | Mỗi lần chìm xuống, nó có thể nhịn thở liên tục 5 phút đồng hồ. | **5 PHÚT** · nhịn thở dưới nước · R/380 · [0.65, 0.5] | chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực ngồi thiền dưới đáy nước nhắm mắt thư giãn, chiếc đồng hồ bấm giờ bên cạnh đếm đủ 5 phú |
| b14 | 01:17.5–01:25.3 (7.8s) | L26 | Thậm chí khi ngủ gật dưới nước, một phản xạ vô thức tự động đẩy cơ thể nó trồi lên mặt nước hít một hơi rồi lại chìm xuống ngủ tiếp mà không hề tỉnh giấc! |  | Mặt cắt tầng nước: chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực đang ngủ say dưới đáy tự động nổi lên mặt nước thở một hơi 'phù' rồi |
| b15 | 01:25.3–01:32.4 (7.1s) | L27 | Chưa hết, âm thanh gầm rú của tuyển thủ dưới nước có thể đạt mức 115 đề-xi-ben ngang ngửa một buổi hòa nhạc nhạc rock, | **115 DB** · tiếng gầm xuyên nước · L/380 · [0.35, 0.5] | Loa phóng thanh dưới nước phát sóng âm thanh khổng lồ 115 decibel rung chuyển cả lòng sông và mặt nước; cá mập và cá sấu giật mình bơi toán loạn. |
| b16 | 01:32.4–01:41.7 (9.3s) | L68 | truyền đồng thời qua cả môi trường nước lẫn không khí để răn đe mọi đối thủ trong bán kính hàng cây số! Đúng là phong cách của bậc thầy lười biếng thượng thừa! |  | Mặt cắt dòng sông và không khí: luồng sóng âm thanh lan tỏa đồng thời cả trên cạn lẫn dưới nước; các đối thủ trong bán kính hàng cây số đều co rúm khiếp sợ. |

### scene03 · DA DÀY 5CM VÀ LỚP KEM CHỐNG NẮNG MỒ HÔI MÁU · 91.2s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.4 (7.4s) | L28 | Chuyển sang phân tích hệ thống phòng thủ độc quyền của tuyển thủ! Quý vị hãy nhìn vào lớp da trần trụi không có lông của Cỗ xe tăng bọc thịt! |  | anh chàng bình luận viên esports hoạt hình đeo tai nghe gaming có micro, mặc áo vest thể thao sành điệu, hào hứng bình luận cầm kính lúp và đèn pin đặc biệt soi vào lớp da dày bóng loáng của chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choà |
| b02 | 00:07.4–00:12.5 (5.1s) | L29 | Đây không phải là da thịt thông thường, mà là một tấm giáp bọc thép sinh học dày tới 5cm! | **5 CM** · giáp da bọc thép · L/380 · [0.4, 0.5] | Mặt cắt da hà mã phóng đại: lớp da và mỡ dày 5cm như lốp xe tải hạng nặng; một mũi tên sắt bắn vào bị cong gãy dội ngược ra ngoài. |
| b03 | 00:12.5–00:25.5 (13.0s) | L30 | Lớp da dày và dai như lốp xe tải này có thể chống đỡ răng nanh sắc nhọn của cả đàn sư tử đói, và trong quá khứ, ngay cả những viên đạn chì súng trường cổ điển bắn vào cũng bị trượt văng ra ngoài mà không thể xuyên thủng nội tạng! |  | Một con sư tử đói nhảy lên cắn vào lưng chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực nhưng răng nanh sư tử bị trượt trên lớp da dày  |
| b04 | 00:25.5–00:32.0 (6.5s) | L31 | Khoan đã bình luận viên ơi, nhìn trên người tuyển thủ kìa, có phải nó đang bị chảy máu đầm đìa khắp toàn thân không? |  | gã đấu sĩ gấu xám khổng lồ cơ bắp cuồn cuộn đang đứng khoanh tay ngạc nhiên giơ ngón tay to lớn chỉ vào màn hình thắc mắc vẻ mặt hốt hoảng: trên người hà mã phủ đầy chất lỏng màu đỏ tươi rỉ ra từ các lỗ chân lông. |
| b05 | 00:32.0–00:41.7 (9.7s) | L32 | Bác đấu sĩ khổng lồ chớ vội hốt hoảng! Đó không phải là máu, mà là một trong những phát minh hóa học vi diệu nhất hành tinh: lớp mồ hôi máu huyền thoại! Tuyển thủ của chúng ta không có tuyến mồ hôi thông thường. |  | anh chàng bình luận viên esports hoạt hình đeo tai nghe gaming có micro, mặc áo vest thể thao sành điệu, hào hứng bình luận cười tươi khoát tay giải thích; chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy |
| b06 | 00:41.7–00:46.7 (5.0s) | L33 | Khi trời nắng gắt, các lỗ chân lông đặc biệt trên da sẽ tiết ra một chất lỏng nhớt màu đỏ rực như máu. |  | Cận cảnh lỗ chân lông phóng đại: các giọt chất lỏng màu đỏ tươi đặc quánh như si-rô rỉ ra bao phủ toàn bộ cơ thể tạo lớp màng bảo vệ. |
| b07 | 00:46.7–01:01.1 (14.4s) | L34 | Các nhà khoa học phân tích phát hiện dung dịch này chứa hai loại axit cực hiếm: một loại hấp thụ hoàn toàn tia cực tím độc hại, hoạt động như một lớp kem chống nắng tự nhiên chỉ số cực cao; loại còn lại là chất kháng sinh diệt khuẩn siêu mạnh! Tại sao lại cần trang bị kỳ lạ này? |  | Hai ống nghiệm hóa học phát sáng: ống một chứa axit chống tia UV mặt trời như kem chống nắng; ống hai chứa chất kháng sinh tiêu diệt vi khuẩn. |
| b08 | 01:01.1–01:13.1 (12.0s) | L35 | Bởi vì lớp da của hà mã mất nước nhanh gấp 7 lần da con người nếu rời khỏi môi trường ẩm ướt! Nếu không ngâm mình dưới nước hoặc bôi lớp kem mồ hôi đỏ này, da nó sẽ nứt toác và rỉ máu thật sự dưới cái nắng thiêu đốt của châu Phi! | **GẤP 7 LẦN** · tốc độ mất nước · R/380 · [0.65, 0.5] | Biểu đồ so sánh bốc hơi nước: BÊN TRÁI da người mất nước bình thường; BÊN PHẢI da hà mã bốc hơi nước nhanh gấp 7 lần nếu không có lớp mồ hôi đỏ bảo vệ. |
| b09 | 01:13.1–01:23.2 (10.1s) | L36 | Nhờ có lớp kem chống nắng kiêm thuốc sát trùng thần thánh này, Cỗ xe tăng bọc thịt có thể ngâm mình hàng giờ trong những vũng bùn bẩn thỉu đầy vi khuẩn mà vết thương cắn xé nhau không bao giờ bị nhiễm trùng! |  | chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực ngâm mình thảnh thơi trong vũng bùn lầy lội đầy bọ gậy và vi khuẩn; những vết xước cọ x |
| b10 | 01:23.2–01:31.2 (8.0s) | L37 | Vừa bọc giáp 5cm, vừa tự bôi kem chống nắng kiêm thuốc sát trùng, đúng là tuyển thủ biết yêu chiều bản thân nhất võ đài! |  | chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực nằm trên ghế dài ven sông đeo kính râm, một tay cầm lọ kem chống nắng màu đỏ tự bôi lên |

### scene04 · LỰC CẮN 1.800 PSI VÀ CÚ CHẠY BỘ 30KM/H · 89.2s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:03.6 (3.6s) | L38 | Bây giờ, xin mời quý vị chiêm ngưỡng vũ khí sát thương khủng khiếp nhất của tuyển |  | Đèn pha rọi thẳng vào khuôn mặt chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực; chú bắt đầu há chiếc mồm khổng lồ ra từ từ, khói hơi t |
| b02 | 00:03.6–00:11.0 (7.4s) | L39 | thủ! Hãy nhìn vào chiếc mồm khổng lồ kia: nó có thể mở rộng tới một góc 180° — tức là mở toang hoác thành một đường thẳng tắp rộng hơn một | **180 ĐỘ** · độ mở rộng của hàm · L/360 · [0.35, 0.45] | Cận cảnh chiếc mồm mở rộng tới 180 độ: hai hàm mở toang hoác thẳng tắp rộng hơn một mét; bên trong là vòm họng đỏ rực và hàm răng đồ sộ. |
| b03 | 00:11.0–00:19.1 (8.2s) | L40 | mét! Bên trong chiếc mồm đỏ lòm là một kho vũ khí cận chiến chết chóc: hai chiếc răng nanh hàm dưới dài tới 50cm, cong vút và sắc nhọn như hai mũi ngọn giáo kim | **50 CM** · ngọn giáo cận chiến · R/360 · [0.65, 0.45] | Cận cảnh cặp răng nanh hàm dưới dài 50cm: cong vút, trắng ngà sắc lẹm như hai mũi giáo thép đâm thẳng lên trời; KHÔNG có chú Hà Mã áo giác đấu trong cảnh này. |
| b04 | 00:19.1–00:26.4 (7.2s) | L41 | loại! Đôi răng này không dùng để nhai cỏ, mà là vũ khí chiến đấu thuần túy, liên tục tự mài sắc vào nhau mỗi khi tuyển thủ ngậm mồm lại! |  | Cơ chế tự mài sắc: hai chiếc răng nanh trên và dưới cọ xát vào nhau tóe tia lửa điện như mài dao kéo mỗi khi ngậm mồm lại. |
| b05 | 00:26.4–00:31.8 (5.4s) | L42 | Và khi chiếc hàm cơ bắp kia đóng sập xuống, nó tạo ra một lực cắn khủng khiếp: 1.800 PSI! | **1.800 PSI** · lực nghiền nát · L/360 · [0.35, 0.5] | Chiếc hàm hà mã đóng sập xuống nghe tiếng 'RẮP!' long trời lở đất; một chiếc đồng hồ đo áp lực nổ tung mốc 1.800 PSI tóe khói. |
| b06 | 00:31.8–00:36.6 (4.8s) | L43 | Con số này mạnh gấp 3 lần lực cắn của một con sư tử đực trưởng thành, và mạnh gấp 10 lần cú cắn của con người! | **GẤP 3 LẦN** · uy lực so với sư tử · R/380 · [0.72, 0.45] | Biểu đồ lực cắn đối đầu: BÊN TRÁI cú cắn của người chỉ 162 PSI; Ở GIỮA sư tử 650 PSI; BÊN PHẢI cú cắn hà mã 1.800 PSI cao vút gấp ba lần sư tử. |
| b07 | 00:36.6–00:46.5 (10.0s) | L44 | Một cú đớp toàn lực của Cỗ xe tăng bọc thịt đủ sức bẻ gãy đôi một chiếc thuyền độc mộc của ngư dân, nghiền nát mai rùa cứng như đá, hoặc cắn đứt đôi thân mình một con cá sấu dài 3m chỉ trong một chớp mắt! |  | chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực cắn đứt đôi một khúc gỗ tròn khổng lồ và bẻ gãy chiếc thuyền gỗ mục một cách nhẹ nhàng  |
| b08 | 00:46.5–00:54.5 (8.0s) | L45 | Để nhắm bắn chuẩn xác, đầu của hà mã còn có một thiết kế radar đỉnh cao: mắt, tai và lỗ mũi nằm trên cùng một đường thẳng ngang ở đỉnh đầu! |  | Mặt cắt mặt nước: chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực giấu 95% cơ thể khổng lồ chìm dưới nước, chỉ nhô mắt, tai và lỗ mũi t |
| b09 | 00:54.5–01:05.6 (11.1s) | L69 | Thiết kế này hoạt động y hệt kính tiềm vọng của tàu ngầm quân sự, cho phép tuyển thủ giấu 95% cơ thể khổng lồ dưới mặt nước mà vẫn quan sát trọn vẹn 360 độ mọi động tĩnh trên bờ! | **95%** · cơ thể ẩn dưới nước · L/380 · [0.35, 0.5]<br>**360 ĐỘ** · tầm nhìn toàn cảnh · R/380 · [0.65, 0.45] | Mô hình tàu ngầm quân sự có ống kính tiềm vọng thò lên mặt nước quan sát 360 độ; bên cạnh chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ r |
| b10 | 01:05.6–01:12.5 (6.9s) | L46 | Và điều trớ trêu nhất là gì? Dù sở hữu vũ khí hủy diệt hạng nặng như vậy, tuyển thủ của chúng ta lại là một... kẻ ăn chay chính hiệu! |  | anh chàng bình luận viên esports hoạt hình đeo tai nghe gaming có micro, mặc áo vest thể thao sành điệu, hào hứng bình luận ôm trán cười ngả nghiêng chỉ vào bàn ăn của chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đ |
| b11 | 01:12.5–01:19.7 (7.2s) | L47 | Ban đêm khi mặt trời lặn, nó lững thững leo lên bờ và dành suốt 6 tiếng đồng hồ chỉ để gặm cỏ non, nạp khoảng 45kg cỏ mỗi đêm! | **45 KG** · cỏ gặm mỗi đêm · R/380 · [0.65, 0.5] | Đêm trăng sáng: chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực thong dong đi dạo trên bờ cỏ, cần mẫn gặm từng búi cỏ non mềm; chiếc xe |
| b12 | 01:19.7–01:29.2 (9.5s) | L48 | Răng nanh 50cm để cắn đôi kẻ thù, nhưng dạ dày thì chỉ thích chứa cỏ xanh! Một sự kết hợp đầy mâu thuẫn giữa vẻ ngoài hung tợn và tâm hồn ăn chay thanh tịnh! |  | chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực ngồi nhai một cọng cỏ nhỏ xíu vắt ngang khóe mồm, hai mắt lim dim hiền khô như một đạo  |

### scene05 · CẮN ĐÔI CÁ SẤU VÀ TUYỆT CHIÊU QUẠT ĐUÔI PHÂN · 96.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:03.1 (3.1s) | L49 | Hãy cùng theo dõi những thước phim thực chiến nghẹt thở từ võ đài |  | Màn hình lớn phát lại thước phim thực chiến kịch tính tại đầm lầy sông Nile: nước sông cuộn sóng dữ dội. |
| b02 | 00:03.1–00:10.3 (7.2s) | L50 | sông Nile! Trong thế giới hoang dã châu Phi, cá sấu sông Nile được coi là bạo chúa đầm lầy, nhưng khi gặp Cỗ xe tăng bọc thịt, mọi định kiến đều bị đập tan |  | Một con cá sấu sông Nile dài 3m hung dữ bơi lạc vào giữa đàn hà mã đang tắm mát, mắt cá sấu trừng trừng đe dọa. |
| b03 | 00:10.3–00:20.5 (10.2s) | L51 | tành! Đã có vô số cảnh quay ghi lại cảnh những con cá sấu khổng lồ bơi lỡ bước vào lãnh địa của đàn hà mã, và ngay lập tức bị tuyển thủ của chúng ta lao tới ngoạm ngang lưng, cắn nát bộ giáp gai và quăng quật như một món đồ chơi! |  | chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực lao tới ngoạm ngang lưng con cá sấu, quăng quật con cá sấu văng lên không trung như một |
| b04 | 00:20.5–00:27.2 (6.7s) | L52 | Ngay cả loài sư tử dũng mãnh, nếu dám bén mảng lại gần hà mã con, cũng sẽ bị cả bầy hà mã lao lên bờ rượt đuổi chạy tóe khói! |  | Trên bờ sông: hai chú sư tử đực đang lén lút rình rập liền bị cả đàn hà mã khổng lồ đồng loạt rống lên lao lên bờ rượt đuổi chạy tóe khói. |
| b05 | 00:27.2–00:39.8 (12.6s) | L53 | Theo thống kê của các nhà bảo tồn, Cỗ xe tăng bọc thịt là loài động vật có vú nguy hiểm bậc nhất châu Phi, khiến khoảng 500 người thiệt mạng mỗi năm — nhiều hơn cả sư tử, báo hoa mai và voi gộp lại! Tính khí của nó cực kỳ thất thường và có tính sở hữu lãnh thổ cực đoan: | **500 NGƯỜI** · nạn nhân mỗi năm · L/380 · [0.35, 0.5] | Tấm bảng cảnh báo nguy hiểm hình đầu lâu: con số 500 nạn nhân mỗi năm ở Châu Phi; biển báo vẽ biểu tượng xe bọc thép ba tấn đang lao tới. |
| b06 | 00:39.8–00:46.8 (7.0s) | L54 | bất kỳ ai dám đứng chắn giữa nó và dòng nước cứu sinh đều sẽ phải đối mặt với một cỗ xe 3 tấn lao tới với tốc độ 30km/h! | **30 KM/H** · tốc độ truy cản · R/380 · [0.65, 0.45] | chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực bứt tốc 30km/h lao thẳng về phía dòng nước cứu sinh như một quả tên lửa mặt đất, bụi cá |
| b07 | 00:46.8–00:56.6 (9.8s) | L55 | Nhưng chiêu thức hài hước và bốc mùi nhất võ đài chính là tuyệt kỹ đánh dấu chủ quyền: cỗ máy quạt đuôi phân thần thánh! Tuyển thủ sở hữu một chiếc đuôi ngắn dẹt hoạt động y hệt một chiếc cánh quạt trực thăng. |  | anh chàng bình luận viên esports hoạt hình đeo tai nghe gaming có micro, mặc áo vest thể thao sành điệu, hào hứng bình luận phải đeo một chiếc mặt nạ phòng độc hài hước nhăn mũi; phía sau là đám mây khói mùi bay mù mịt. |
| b08 | 00:56.6–01:07.6 (11.0s) | L56 | Mỗi khi đi vệ sinh, nó sẽ vừa xả phân vừa vung chiếc đuôi quay tít mù với tốc độ cao, quạt tung tóe các mảnh phân và nước tiểu bắn xa từ 2-3m xung quanh để thông báo cho cả vùng biết: lãnh địa này đã có chủ! | **2-3 MÉT** · bán kính quạt phân · R/360 · [0.68, 0.45] | Cận cảnh chiếc đuôi dẹt của chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực quay tít mù như cánh quạt máy bay trực thăng, quạt các mảnh |
| b09 | 01:07.6–01:14.9 (7.3s) | L57 | Kẻ thù nhìn thấy cảnh tượng đó không chỉ khiếp sợ sức mạnh, mà còn phải ôm mũi bỏ chạy vì mức độ ô nhiễm không khí quá nặng nề! |  | Cá sấu và linh cẩu đứng cách xa 3 mét đều bịt mũi ôm đầu bỏ chạy thục mạng vì không chịu nổi mùi ô nhiễm nồng nặc. |
| b10 | 01:14.9–01:29.4 (14.5s) | L58 | Ấy thế mà, thỉnh thoảng gã cục súc này lại có những hành động trượng nghĩa khó tin! Các nhà thám hiểm từng ghi lại cảnh hà mã lao vào tấn công cá sấu để giải cứu một chú linh dương đầu bò đang bị kéo xuống nước, thậm chí xua đuổi cả đàn linh cẩu để bảo vệ một chú ngựa vằn bị thương! |  | chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực dũng cảm đứng chắn giữa cá sấu và một chú linh dương đầu bò con vừa bị trượt chân xuống |
| b11 | 01:29.4–01:36.4 (7.0s) | L59 | Dữ dằn số một châu Phi, nhưng đôi khi lại hành xử như một vị cảnh sát trưởng đầy nghĩa khí giữa thiên nhiên hoang dã! |  | chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực đội một chiếc mũ cảnh sát trưởng hoạt hình, đeo huy hiệu ngôi sao bạc lấp lánh, đứng ca |

### scene06 · ĐAI VÔ ĐỊCH VÀ BÓNG ĐEN BÍ ẨN TẬP TIẾP THEO · 78.3s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:06.3 (6.3s) | L60 | Và trận đấu đã khép lại! Trọng tài xin trịnh trọng trao chiếc đai vô địch hạng siêu nặng cho Cỗ xe tăng bọc thịt Hà Mã! |  | Sân khấu bế mạc võ đài rực rỡ pháo hoa vàng: anh chàng bình luận viên esports hoạt hình đeo tai nghe gaming có micro, mặc áo vest thể thao sành điệu, hào hứng bình luận trịnh trọng giơ cao chiếc đai vô địch hạng siêu nặng mạ vàng lấp lánh trao cho chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trê |
| b02 | 00:06.3–00:16.7 (10.4s) | L61 | Một đấu sĩ hội tụ đủ mọi yếu tố không tưởng: 3 tấn cơ bắp, mồ hôi chống nắng màu đỏ, lực cắn 1.800 PSI nghiền nát cá sấu, và một gia tộc có họ hàng ruột thịt gần gũi nhất với loài cá voi đại dương! |  | chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực đeo đai vô địch quanh chiếc bụng béo tròn, giơ găng tay boxing đỏ vẫy chào trong tiếng  |
| b03 | 00:16.7–00:28.0 (11.3s) | L62 | Chúng tách ra từ một tổ tiên chung cách đây 55 triệu năm: một nhánh bơi hẳn ra biển khơi tiến hóa thành cá voi khổng lồ, còn nhánh kia ở lại đầm lầy châu Phi trở thành cỗ xe tăng bất khả chiến bại này! Chiếc đai | **55 TR NĂM** · họ hàng ruột cá voi · L/380 · [0.4, 0.45] | Cây gia phả 55 triệu năm: tổ tiên chung ở giữa, rẽ một nhánh sang bên trái là chú Cá Voi xanh khổng lồ dưới đại dương, rẽ sang bên phải là chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàn |
| b04 | 00:28.0–00:40.2 (12.2s) | L63 | vô địch Tập 12 đã có chủ! Nhưng đấu trường sinh tồn sẽ không bao giờ dừng lại! Ngay bây giờ, xin mời toàn thể khán đài hướng mắt lên màn hình lớn để chiêm ngưỡng BÓNG ĐEN BÍ ẨN của tuyển thủ tiếp theo trong Tập 13! |  | Màn hình LED võ đài bỗng phụt tắt đèn màu, chuyển sang ánh sáng tím huyền bí mờ ảo; cả khán đài ồ lên tò mò hướng mắt nhìn. |
| b05 | 00:40.2–00:51.6 (11.4s) | L64 | Xin đưa ra ba manh mối chấn động về bóng đen bí ẩn này: Thứ nhất, đây là sinh vật sống chậm chạp bậc nhất hành tinh, với tốc độ kỷ lục chỉ 0,2km/h, đến mức rêu xanh và cả một hệ sinh thái bướm đêm mọc um tùm ngay trên lớp lông của nó! | **0,2 KM/H** · siêu tốc độ rùa bò · R/380 · [0.65, 0.5] | Trên màn hình LED lớn xuất hiện một BÓNG ĐEN HOÀN TOÀN (solid black silhouette) của một sinh vật bí ẩn đang treo ngược hai chân trên cành cây, xung quanh bóng đen tỏa ra hào quang màu tím bí ẩn và một dấu hỏi chấm khổng lồ màu vàng phát sáng rực rỡ ở giữa. KHÔNG có chú Hà Mã áo giác đấu trong cảnh này. |
| b06 | 00:51.6–00:57.4 (5.7s) | L65 | Thứ hai, mỗi tuần nó chỉ chịu leo xuống đất đi vệ sinh đúng 1 lần duy nhất, mỗi lần đi xả tới 1/3 trọng lượng cơ thể! | **1 TUẦN** · đi vệ sinh 1 lần · L/360 · [0.35, 0.45]<br>**1/3** · trọng lượng xả thải · R/480 · [0.65, 0.55] | Vẫn là BÓNG ĐEN HOÀN TOÀN (solid black silhouette) treo ngược trên cành cây, trên lớp lông đen mọc ra các đám rêu xanh lá cây và đàn bướm đêm nhỏ bay quanh, bên dưới có chiếc cân đo mất 1/3 cân nặng và tờ lịch 1 tuần. KHÔNG có chú Hà Mã áo giác đấu trong cảnh này. |
| b07 | 00:57.4–01:04.7 (7.4s) | L66 | Và thứ ba, nghịch lý bi hài nhất: hơn một nửa số cái chết trong cuộc đời của sinh vật này đều xảy ra... đúng vào lúc nó xuống đất đi vệ sinh! |  | BÓNG ĐEN HOÀN TOÀN (solid black silhouette) đang từ từ leo xuống đất trong bóng đêm, bên cạnh có biển báo nguy hiểm sinh tử giật mình hài hước; dấu hỏi chấm to tướng xoay tròn. KHÔNG có chú Hà Mã áo giác đấu trong cảnh này. |
| b08 | 01:04.7–01:18.3 (13.6s) | L67 | Quý vị khán giả có đoán ra bóng đen bí ẩn này là quái kiệt nào của thế giới tự nhiên không? Hãy để lại dự đoán và phán quyết của bạn ngay dưới phần bình luận nhé! Bình luận viên xin chào tạm biệt và hẹn gặp lại toàn thể quý vị trên sàn đấu rực lửa tiếp theo! |  | Khán đài sôi động: các bạn nhỏ và muông thú giơ các tấm bảng dấu hỏi chấm, mặt hào hứng suy đoán tên quái kiệt bóng đen; anh chàng bình luận viên esports hoạt hình đeo tai nghe gaming có micro, mặc áo vest thể thao sành điệu, hào hứng bình luận giơ tay mời gọi khán giả bình luận. |

## 5. Phân cảnh Shorts — từng beat

Banner: **CỖ XE TĂNG 3 TẤN / NHƯNG KHÔNG BIẾT BƠI?!** · giọng 42.4s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Một sinh vật nặng tới 3 tấn ngâm mình dưới nước 16 tiếng mỗi ngày, nhưng lại hoàn toàn không biết | **3 TẤN** · cỗ xe tăng · L/560 · [0.35, 0.4]<br>**16 TIẾNG** · ngâm nước/ngày · R/820 · [0.65, 0.65] |
| s02 | 00:04.9 | S02 | bơi! Đó chính là Hà Mã, cỗ xe tăng bọc thịt hung hãn nhất đầm lầy châu |  |
| s03 | 00:09.0 | S03 | Phi! Xương của nó đặc và nặng đến mức ném xuống nước là chìm nghỉm như một khối đá |  |
| s04 | 00:13.2 | S09 | tảng, nên thay vì bơi, nó chọn cách chạy bộ dưới đáy sông với tốc độ 8km/h! | **8 KM/H** · chạy bộ đáy sông · L/650 · [0.4, 0.5] |
| s05 | 00:18.0 | S04 | Trên bờ, nó có thể bứt tốc 30km/h, sở hữu lớp da dày 5cm chống | **30 KM/H** · tốc độ trên cạn · R/580 · [0.65, 0.45]<br>**5 CM** · da dày chống đạn · L/880 · [0.35, 0.7] |
| s06 | 00:22.7 | S05 | đạn và tự tiết ra lớp mồ hôi đỏ rực như máu để chống nắng kiêm diệt khuẩn. |  |
| s07 | 00:26.4 | S06 | Đáng sợ nhất là lực cắn 1.800 PSI gấp 3 lần sư | **1.800 PSI** · lực cắn cực hạn · L/600 · [0.35, 0.45] |
| s08 | 00:29.7 | S07 | tử, kết hợp cặp răng nanh 50cm đủ sức cắn đứt đôi một con cá sấu dài 3m chỉ trong một chớp | **50 CM** · răng nanh giáo thép · L/650 · [0.4, 0.5]<br>**3 MÉT** · cắn đôi cá sấu · R/900 · [0.65, 0.7] |
| s09 | 00:34.4 | S08 | mắt! Vậy là bí mật đã rõ: hà mã không cần học |  |
| s10 | 00:37.2 | S10 | bơi, vì dưới đáy sông hay trên cạn, nó sinh ra đã là một cỗ xe bọc thép bất khả chiến bại của tự nhiên! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kính thưa quý vị khán giả đang theo dõi Đấu Trường Sinh Tồn!". Bố cục: Sàn đấu võ đài hoang dã sông Nile châu Phi lúc hoàng hôn: ánh đèn rực lửa, cờ phướn bay phấp phới; anh chàng bình luận viên esports hoạt hình đeo tai nghe gaming có micro, mặc áo vest thể thao sành điệu, hào hứng bình luận đeo tai nghe gaming đứng trước bục micro phát thanh viên giơ tay chỉ xuống dòng sông.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyển thủ hạng siêu nặng của chúng ta đã chính thức bước vào sàn đấu!". Bố cục: Mặt nước sông Nile sủi bọt cuồn cuộn như có núi lửa ngầm; các loài chim nước bay tán loạn giật mình hoảng hốt.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy hướng ống kính về phía dòng sông châu Phi rực lửa, nơi một khối cơ bắp khổng lồ nặng tới 3 tấn vừa trồi lên khỏi mặt nước!". Bố cục: chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực khổng lồ nặng tới 3 tấn từ từ trồi người lên khỏi mặt nước sông rực lửa, hai cánh tay đeo găng đấm bốc đỏ rực giơ cao thị uy sức mạnh; bọt nước bắn tung tóe.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đó chính là Hà Mã — sinh vật được mệnh danh là Cỗ xe tăng bọc thịt của giới tự nhiên!". Bố cục: Chân dung cận cảnh oai phong của chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực: thân hình tròn ủng đồ sộ như một cỗ xe tăng bọc thép hạng nặng, hai lỗ mũi phì hơi nước nóng hầm hố, áo choàng đỏ tung bay.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhìn dáng vẻ tròn ủng, lùn tịt và bốn cái chân ngắn cũn cỡn, nhiều khán giả trên khán đài có thể tưởng rằng gã béo này vô hại như một chú heo mọi khổng lồ.". Bố cục: So sánh hài hước: BÊN TRÁI một chú heo mọi mũm mĩm hiền lành ăn cám; BÊN PHẢI chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực đứng sừng sững to gấp mười lần với vẻ mặt bặm trợn uy dũng.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng xin cảnh báo ngay: đây là cỗ máy chiến đấu cục súc và nguy hiểm bậc nhất lục địa đen, sở hữu bảng chỉ số khiến mọi kẻ săn mồi thượng thừa cũng phải toát mồ hôi hột!". Bố cục: Bản đồ lục địa Châu Phi đỏ rực lửa: hình bóng chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực phủ bóng đen khổng lồ lên khắp thảo nguyên; xung quanh đàn sư tử và linh cẩu co rúm toát mồ hôi hột né tránh.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Alo bình luận viên ơi, nghe đồn tuyển thủ này sống dưới nước suốt ngày nhưng lại... hoàn toàn không biết bơi hả?". Bố cục: Trường quay tin tức thời sự: cô phát thanh viên tin tức hoạt hình xinh đẹp ngồi sau bàn trường quay ngồi sau bàn kính hiện đại cầm bút chỉ lên màn hình kết nối hiện trường, ngơ ngác đặt câu hỏi.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Báo cáo trường quay, đó là sự thật 100%! Đây chính là cú lừa kinh điển nhất mà tạo hóa dành cho giới sinh học: một loài vật ngâm mình dưới nước tới 16 tiếng mỗi ngày, nhưng lại tuyệt đối không biết bơi, thậm chí không thể tự nổi trên mặt nước!". Bố cục: Cảnh sông nước: chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực ngâm mình dưới nước 16 tiếng mỗi ngày, xung quanh nổi bóng đồng hồ báo 16 tiếng; nhưng một chiếc phao bơi vịt vàng trôi qua trêu chọc chú không biết bơi.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khung xương của nó quá đặc và nặng đến mức ném xuống nước là chìm nghỉm như một khối đá tảng!". Bố cục: Cảnh minh họa vật lý: một hòn đá tảng to đùng rơi xuống nước chìm nghỉm tận đáy; bên cạnh bộ xương hà mã dày đặc cũng chìm thẳng đứng xuống đáy sông không chút nổi bồng bềnh.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vậy làm thế nào Cỗ xe tăng bọc thịt có thể di chuyển thần tốc dưới lòng sông?". Bố cục: chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực bước đi thoăn thoắt dưới đáy sông trong làn nước xanh trong vắt, bụi cát đáy sông bốc lên sau gót chân như vận động viên điền kinh.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy cùng chúng tôi mở bảng chỉ số RPG để giải mã toàn bộ bí mật sức mạnh điên rồ của đấu sĩ vô địch này!". Bố cục: anh chàng bình luận viên esports hoạt hình đeo tai nghe gaming có micro, mặc áo vest thể thao sành điệu, hào hứng bình luận vung tay kích hoạt bảng điện tử RPG phát sáng rực rỡ; thanh đo HP, ATK, DEF, SPD hiện lên lấp lánh như trò chơi điện tử đấu trường.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chỉ số chiến đấu đã lên bảng điện tử!". Bố cục: Bảng giao diện chỉ số RPG võ đài hiện ra hoành tráng: chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực đứng ở trung tâm sàn đấu, hai bên là các cột thông số nhảy số điện tử vun vút.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Xin mời toàn thể khán đài nín thở theo dõi thông số kỹ thuật của Cỗ xe tăng bọc thịt!". Bố cục: Khán đài hàng ngàn khán giả thú rừng và các bạn nhỏ hoạt hình nín thở ngước nhìn màn hình LED khổng lồ rực rỡ.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Về lượng máu sinh lực HP: chạm nóc 9.900 điểm!". Bố cục: Thanh máu HP đỏ rực chạm nóc tối đa: con số 9.900 điểm nhấp nháy phát sáng; chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực đứng vỗ ngực rầm rập như bức tường thành sừng sững.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Với trọng lượng cơ thể dao động từ 1,5 tấn đến 3 tấn, cơ thể của nó là một khối thịt và mỡ đồ sộ, được nâng đỡ bởi hệ thống xương đặc biệt dày và nặng nhất thế giới động vật trên cạn.". Bố cục: Cân tải trọng khổng lồ: chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực đứng lên chiếc cân làm kim đồng hồ quay tít mù chỉ vào mốc 1,5 tấn đến 3 tấn; một chiếc xe ô tô con ngồi bên cạnh để so sánh cân nặng.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khối lượng khủng khiếp này biến nó thành một bức tường thành di động mà chẳng có loài săn mồi nào có thể húc đổ trong một đòn!". Bố cục: chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực đứng vững như bàn thạch; một chú tê giác hung hãn lao vào húc nhưng bị dội ngược lại ngã chỏng vó ra đất.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Về sức mạnh tấn công ATK: đạt mức tối đa 9.800 điểm!". Bố cục: Thanh chỉ số ATK màu cam bốc cháy hừng hực: đạt 9.800 điểm; chiếc mồm khổng lồ mở rộng khoe cặp răng nanh nhọn hoắt như hai ngọn giáo thép.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Được trang bị lực cắn kinh hoàng lên tới 1.800 PSI, kết hợp với cặp răng nanh hàm dưới dài tới 50cm nhọn hoắt như hai lưỡi giáo thép!". Bố cục: Máy đo lực cắn phát nổ tóe lửa: kim đo chỉ mốc 1.800 PSI; bên dưới là thước đo cặp răng nanh dài 50cm cắm sâu vào tảng đá.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Về phòng thủ DEF: 9.500 điểm nhờ lớp da dày tới 5cm!". Bố cục: Thanh DEF màu xanh dương đạt 9.500 điểm; lớp da dày 5cm được vẽ như tấm giáp thép bọc quanh người tuyển thủ.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn về tốc độ SPD thì sao? Đừng để thân hình béo tròn đánh lừa: trên cạn nó có thể bứt tốc 30km/h, nhanh hơn cả vận động viên chạy nước rút của con người!". Bố cục: chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực bứt tốc chạy nước rút trên đồng cỏ châu Phi: bụi đất mù mịt phía sau, vượt qua một vận động viên điền kinh đang há hốc mồm kinh ngạc.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng nghịch lý hài hước nhất nằm ở chỉ số bơi lội: bằng không điểm tròn trĩnh! Thay vì bơi quẫy đạp như cá hay rái cá, Cỗ xe tăng bọc thịt chọn cách...". Bố cục: Thanh bơi lội SWIM hiện số 0 điểm tròn trĩnh nhấp nháy màu đỏ; chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực chìm nghỉm dưới đáy sông ngồi đọc sách tỉnh bơ.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chạy bộ và phi nước đại dưới đáy sông với tốc độ 8km/h!". Bố cục: Đáy sông trong vắt: chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực đang nhún ngón chân nhẹ nhàng phi nước đại lướt trên cát đáy nước với tốc độ 8km/h như một vũ công ba-lê uyển chuyển.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà giải phẫu học phát hiện xương chân và xương sườn của hà mã đặc quánh gần như không có khoang tủy xốp, đóng vai trò y hệt chiếc đai chì của thợ lặn chuyên nghiệp. Nó nhẹ nhàng nhún ngón chân xuống nền cát đáy nước rồi đẩy cả khối thân 3 tấn lướt đi êm ái như một vũ công ba-lê dưới nước!". Bố cục: Sơ đồ X-quang xương hà mã: các thanh xương sườn và xương ống chân đặc quánh màu trắng đặc không có lỗ xốp, cạnh đó là chiếc đai chì của thợ lặn.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi lần chìm xuống, nó có thể nhịn thở liên tục 5 phút đồng hồ.". Bố cục: chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực ngồi thiền dưới đáy nước nhắm mắt thư giãn, chiếc đồng hồ bấm giờ bên cạnh đếm đủ 5 phút nhịn thở; cá nhỏ bơi quanh mồm.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thậm chí khi ngủ gật dưới nước, một phản xạ vô thức tự động đẩy cơ thể nó trồi lên mặt nước hít một hơi rồi lại chìm xuống ngủ tiếp mà không hề tỉnh giấc!". Bố cục: Mặt cắt tầng nước: chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực đang ngủ say dưới đáy tự động nổi lên mặt nước thở một hơi 'phù' rồi lại chìm xuống ngủ tiếp mà mắt vẫn nhắm nghiền.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa hết, âm thanh gầm rú của tuyển thủ dưới nước có thể đạt mức 115 đề-xi-ben ngang ngửa một buổi hòa nhạc nhạc rock,". Bố cục: Loa phóng thanh dưới nước phát sóng âm thanh khổng lồ 115 decibel rung chuyển cả lòng sông và mặt nước; cá mập và cá sấu giật mình bơi toán loạn.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chuyển sang phân tích hệ thống phòng thủ độc quyền của tuyển thủ! Quý vị hãy nhìn vào lớp da trần trụi không có lông của Cỗ xe tăng bọc thịt!". Bố cục: anh chàng bình luận viên esports hoạt hình đeo tai nghe gaming có micro, mặc áo vest thể thao sành điệu, hào hứng bình luận cầm kính lúp và đèn pin đặc biệt soi vào lớp da dày bóng loáng của chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực; chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực đứng gồng mình khoe lớp giáp cơ bắp.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đây không phải là da thịt thông thường, mà là một tấm giáp bọc thép sinh học dày tới 5cm!". Bố cục: Mặt cắt da hà mã phóng đại: lớp da và mỡ dày 5cm như lốp xe tải hạng nặng; một mũi tên sắt bắn vào bị cong gãy dội ngược ra ngoài.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lớp da dày và dai như lốp xe tải này có thể chống đỡ răng nanh sắc nhọn của cả đàn sư tử đói, và trong quá khứ, ngay cả những viên đạn chì súng trường cổ điển bắn vào cũng bị trượt văng ra ngoài mà không thể xuyên thủng nội tạng!". Bố cục: Một con sư tử đói nhảy lên cắn vào lưng chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực nhưng răng nanh sư tử bị trượt trên lớp da dày trơn láng, sư tử trượt ngã nhào xuống đất vẻ mặt ê ẩm.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khoan đã bình luận viên ơi, nhìn trên người tuyển thủ kìa, có phải nó đang bị chảy máu đầm đìa khắp toàn thân không?". Bố cục: gã đấu sĩ gấu xám khổng lồ cơ bắp cuồn cuộn đang đứng khoanh tay ngạc nhiên giơ ngón tay to lớn chỉ vào màn hình thắc mắc vẻ mặt hốt hoảng: trên người hà mã phủ đầy chất lỏng màu đỏ tươi rỉ ra từ các lỗ chân lông.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bác đấu sĩ khổng lồ chớ vội hốt hoảng! Đó không phải là máu, mà là một trong những phát minh hóa học vi diệu nhất hành tinh: lớp mồ hôi máu huyền thoại! Tuyển thủ của chúng ta không có tuyến mồ hôi thông thường.". Bố cục: anh chàng bình luận viên esports hoạt hình đeo tai nghe gaming có micro, mặc áo vest thể thao sành điệu, hào hứng bình luận cười tươi khoát tay giải thích; chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực đứng lau mặt mỉm cười tự tin, lớp mồ hôi đỏ ánh lên lấp lánh dưới ánh mặt trời.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi trời nắng gắt, các lỗ chân lông đặc biệt trên da sẽ tiết ra một chất lỏng nhớt màu đỏ rực như máu.". Bố cục: Cận cảnh lỗ chân lông phóng đại: các giọt chất lỏng màu đỏ tươi đặc quánh như si-rô rỉ ra bao phủ toàn bộ cơ thể tạo lớp màng bảo vệ.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà khoa học phân tích phát hiện dung dịch này chứa hai loại axit cực hiếm: một loại hấp thụ hoàn toàn tia cực tím độc hại, hoạt động như một lớp kem chống nắng tự nhiên chỉ số cực cao; loại còn lại là chất kháng sinh diệt khuẩn siêu mạnh! Tại sao lại cần trang bị kỳ lạ này?". Bố cục: Hai ống nghiệm hóa học phát sáng: ống một chứa axit chống tia UV mặt trời như kem chống nắng; ống hai chứa chất kháng sinh tiêu diệt vi khuẩn.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bởi vì lớp da của hà mã mất nước nhanh gấp 7 lần da con người nếu rời khỏi môi trường ẩm ướt! Nếu không ngâm mình dưới nước hoặc bôi lớp kem mồ hôi đỏ này, da nó sẽ nứt toác và rỉ máu thật sự dưới cái nắng thiêu đốt của châu Phi!". Bố cục: Biểu đồ so sánh bốc hơi nước: BÊN TRÁI da người mất nước bình thường; BÊN PHẢI da hà mã bốc hơi nước nhanh gấp 7 lần nếu không có lớp mồ hôi đỏ bảo vệ.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhờ có lớp kem chống nắng kiêm thuốc sát trùng thần thánh này, Cỗ xe tăng bọc thịt có thể ngâm mình hàng giờ trong những vũng bùn bẩn thỉu đầy vi khuẩn mà vết thương cắn xé nhau không bao giờ bị nhiễm trùng!". Bố cục: chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực ngâm mình thảnh thơi trong vũng bùn lầy lội đầy bọ gậy và vi khuẩn; những vết xước cọ xát tự lành lặn nhanh chóng không hề bị nhiễm trùng.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vừa bọc giáp 5cm, vừa tự bôi kem chống nắng kiêm thuốc sát trùng, đúng là tuyển thủ biết yêu chiều bản thân nhất võ đài!". Bố cục: chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực nằm trên ghế dài ven sông đeo kính râm, một tay cầm lọ kem chống nắng màu đỏ tự bôi lên người, vẻ mặt hưởng thụ như đại gia đi nghỉ dưỡng.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bây giờ, xin mời quý vị chiêm ngưỡng vũ khí sát thương khủng khiếp nhất của tuyển thủ!". Bố cục: Đèn pha rọi thẳng vào khuôn mặt chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực; chú bắt đầu há chiếc mồm khổng lồ ra từ từ, khói hơi thở phì ra hầm hố.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy nhìn vào chiếc mồm khổng lồ kia: nó có thể mở rộng tới một góc 180° — tức là mở toang hoác thành một đường thẳng tắp rộng hơn một mét!". Bố cục: Cận cảnh chiếc mồm mở rộng tới 180 độ: hai hàm mở toang hoác thẳng tắp rộng hơn một mét; bên trong là vòm họng đỏ rực và hàm răng đồ sộ.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bên trong chiếc mồm đỏ lòm là một kho vũ khí cận chiến chết chóc: hai chiếc răng nanh hàm dưới dài tới 50cm, cong vút và sắc nhọn như hai mũi ngọn giáo kim loại!". Bố cục: Cận cảnh cặp răng nanh hàm dưới dài 50cm: cong vút, trắng ngà sắc lẹm như hai mũi giáo thép đâm thẳng lên trời; KHÔNG có chú Hà Mã áo giác đấu trong cảnh này.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đôi răng này không dùng để nhai cỏ, mà là vũ khí chiến đấu thuần túy, liên tục tự mài sắc vào nhau mỗi khi tuyển thủ ngậm mồm lại!". Bố cục: Cơ chế tự mài sắc: hai chiếc răng nanh trên và dưới cọ xát vào nhau tóe tia lửa điện như mài dao kéo mỗi khi ngậm mồm lại.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và khi chiếc hàm cơ bắp kia đóng sập xuống, nó tạo ra một lực cắn khủng khiếp: 1.800 PSI!". Bố cục: Chiếc hàm hà mã đóng sập xuống nghe tiếng 'RẮP!' long trời lở đất; một chiếc đồng hồ đo áp lực nổ tung mốc 1.800 PSI tóe khói.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Con số này mạnh gấp 3 lần lực cắn của một con sư tử đực trưởng thành, và mạnh gấp 10 lần cú cắn của con người!". Bố cục: Biểu đồ lực cắn đối đầu: BÊN TRÁI cú cắn của người chỉ 162 PSI; Ở GIỮA sư tử 650 PSI; BÊN PHẢI cú cắn hà mã 1.800 PSI cao vút gấp ba lần sư tử.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một cú đớp toàn lực của Cỗ xe tăng bọc thịt đủ sức bẻ gãy đôi một chiếc thuyền độc mộc của ngư dân, nghiền nát mai rùa cứng như đá, hoặc cắn đứt đôi thân mình một con cá sấu dài 3m chỉ trong một chớp mắt!". Bố cục: chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực cắn đứt đôi một khúc gỗ tròn khổng lồ và bẻ gãy chiếc thuyền gỗ mục một cách nhẹ nhàng như bẻ que tăm.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Để nhắm bắn chuẩn xác, đầu của hà mã còn có một thiết kế radar đỉnh cao: mắt, tai và lỗ mũi nằm trên cùng một đường thẳng ngang ở đỉnh đầu!". Bố cục: Mặt cắt mặt nước: chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực giấu 95% cơ thể khổng lồ chìm dưới nước, chỉ nhô mắt, tai và lỗ mũi thẳng hàng trên đỉnh đầu như kính tiềm vọng tàu ngầm.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và điều trớ trêu nhất là gì? Dù sở hữu vũ khí hủy diệt hạng nặng như vậy, tuyển thủ của chúng ta lại là một... kẻ ăn chay chính hiệu!". Bố cục: anh chàng bình luận viên esports hoạt hình đeo tai nghe gaming có micro, mặc áo vest thể thao sành điệu, hào hứng bình luận ôm trán cười ngả nghiêng chỉ vào bàn ăn của chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực: một đống cỏ xanh mướt thơm phức thay vì thịt cá.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ban đêm khi mặt trời lặn, nó lững thững leo lên bờ và dành suốt 6 tiếng đồng hồ chỉ để gặm cỏ non, nạp khoảng 45kg cỏ mỗi đêm!". Bố cục: Đêm trăng sáng: chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực thong dong đi dạo trên bờ cỏ, cần mẫn gặm từng búi cỏ non mềm; chiếc xe cút kít bên cạnh chất đầy 45kg cỏ xanh.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Răng nanh 50cm để cắn đôi kẻ thù, nhưng dạ dày thì chỉ thích chứa cỏ xanh! Một sự kết hợp đầy mâu thuẫn giữa vẻ ngoài hung tợn và tâm hồn ăn chay thanh tịnh!". Bố cục: chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực ngồi nhai một cọng cỏ nhỏ xíu vắt ngang khóe mồm, hai mắt lim dim hiền khô như một đạo sĩ tu hành giữa rừng đêm.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy cùng theo dõi những thước phim thực chiến nghẹt thở từ võ đài sông Nile!". Bố cục: Màn hình lớn phát lại thước phim thực chiến kịch tính tại đầm lầy sông Nile: nước sông cuộn sóng dữ dội.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong thế giới hoang dã châu Phi, cá sấu sông Nile được coi là bạo chúa đầm lầy, nhưng khi gặp Cỗ xe tăng bọc thịt, mọi định kiến đều bị đập tan tành!". Bố cục: Một con cá sấu sông Nile dài 3m hung dữ bơi lạc vào giữa đàn hà mã đang tắm mát, mắt cá sấu trừng trừng đe dọa.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đã có vô số cảnh quay ghi lại cảnh những con cá sấu khổng lồ bơi lỡ bước vào lãnh địa của đàn hà mã, và ngay lập tức bị tuyển thủ của chúng ta lao tới ngoạm ngang lưng, cắn nát bộ giáp gai và quăng quật như một món đồ chơi!". Bố cục: chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực lao tới ngoạm ngang lưng con cá sấu, quăng quật con cá sấu văng lên không trung như một chú thằn lằn đồ chơi; cá sấu hốt hoảng vùng vẫy thoát thân.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ngay cả loài sư tử dũng mãnh, nếu dám bén mảng lại gần hà mã con, cũng sẽ bị cả bầy hà mã lao lên bờ rượt đuổi chạy tóe khói!". Bố cục: Trên bờ sông: hai chú sư tử đực đang lén lút rình rập liền bị cả đàn hà mã khổng lồ đồng loạt rống lên lao lên bờ rượt đuổi chạy tóe khói.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Theo thống kê của các nhà bảo tồn, Cỗ xe tăng bọc thịt là loài động vật có vú nguy hiểm bậc nhất châu Phi, khiến khoảng 500 người thiệt mạng mỗi năm — nhiều hơn cả sư tử, báo hoa mai và voi gộp lại! Tính khí của nó cực kỳ thất thường và có tính sở hữu lãnh thổ cực đoan:". Bố cục: Tấm bảng cảnh báo nguy hiểm hình đầu lâu: con số 500 nạn nhân mỗi năm ở Châu Phi; biển báo vẽ biểu tượng xe bọc thép ba tấn đang lao tới.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bất kỳ ai dám đứng chắn giữa nó và dòng nước cứu sinh đều sẽ phải đối mặt với một cỗ xe 3 tấn lao tới với tốc độ 30km/h!". Bố cục: chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực bứt tốc 30km/h lao thẳng về phía dòng nước cứu sinh như một quả tên lửa mặt đất, bụi cát cuộn xoáy dữ dội.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng chiêu thức hài hước và bốc mùi nhất võ đài chính là tuyệt kỹ đánh dấu chủ quyền: cỗ máy quạt đuôi phân thần thánh! Tuyển thủ sở hữu một chiếc đuôi ngắn dẹt hoạt động y hệt một chiếc cánh quạt trực thăng.". Bố cục: anh chàng bình luận viên esports hoạt hình đeo tai nghe gaming có micro, mặc áo vest thể thao sành điệu, hào hứng bình luận phải đeo một chiếc mặt nạ phòng độc hài hước nhăn mũi; phía sau là đám mây khói mùi bay mù mịt.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi khi đi vệ sinh, nó sẽ vừa xả phân vừa vung chiếc đuôi quay tít mù với tốc độ cao, quạt tung tóe các mảnh phân và nước tiểu bắn xa từ 2-3m xung quanh để thông báo cho cả vùng biết: lãnh địa này đã có chủ!". Bố cục: Cận cảnh chiếc đuôi dẹt của chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực quay tít mù như cánh quạt máy bay trực thăng, quạt các mảnh phân và nước văng tung tóe ra xa 2 đến 3 mét xung quanh.
```
</details>

<details><summary>L57</summary>

```text
HÌNH L57 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kẻ thù nhìn thấy cảnh tượng đó không chỉ khiếp sợ sức mạnh, mà còn phải ôm mũi bỏ chạy vì mức độ ô nhiễm không khí quá nặng nề!". Bố cục: Cá sấu và linh cẩu đứng cách xa 3 mét đều bịt mũi ôm đầu bỏ chạy thục mạng vì không chịu nổi mùi ô nhiễm nồng nặc.
```
</details>

<details><summary>L58</summary>

```text
HÌNH L58 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ấy thế mà, thỉnh thoảng gã cục súc này lại có những hành động trượng nghĩa khó tin! Các nhà thám hiểm từng ghi lại cảnh hà mã lao vào tấn công cá sấu để giải cứu một chú linh dương đầu bò đang bị kéo xuống nước, thậm chí xua đuổi cả đàn linh cẩu để bảo vệ một chú ngựa vằn bị thương!". Bố cục: chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực dũng cảm đứng chắn giữa cá sấu và một chú linh dương đầu bò con vừa bị trượt chân xuống nước, gầm lên bảo vệ chú linh dương an toàn lên bờ.
```
</details>

<details><summary>L59</summary>

```text
HÌNH L59 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Dữ dằn số một châu Phi, nhưng đôi khi lại hành xử như một vị cảnh sát trưởng đầy nghĩa khí giữa thiên nhiên hoang dã!". Bố cục: chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực đội một chiếc mũ cảnh sát trưởng hoạt hình, đeo huy hiệu ngôi sao bạc lấp lánh, đứng canh gác dòng sông bảo vệ các loài thú nhỏ.
```
</details>

<details><summary>L60</summary>

```text
HÌNH L60 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và trận đấu đã khép lại! Trọng tài xin trịnh trọng trao chiếc đai vô địch hạng siêu nặng cho Cỗ xe tăng bọc thịt Hà Mã!". Bố cục: Sân khấu bế mạc võ đài rực rỡ pháo hoa vàng: anh chàng bình luận viên esports hoạt hình đeo tai nghe gaming có micro, mặc áo vest thể thao sành điệu, hào hứng bình luận trịnh trọng giơ cao chiếc đai vô địch hạng siêu nặng mạ vàng lấp lánh trao cho chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực.
```
</details>

<details><summary>L61</summary>

```text
HÌNH L61 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một đấu sĩ hội tụ đủ mọi yếu tố không tưởng: 3 tấn cơ bắp, mồ hôi chống nắng màu đỏ, lực cắn 1.800 PSI nghiền nát cá sấu, và một gia tộc có họ hàng ruột thịt gần gũi nhất với loài cá voi đại dương!". Bố cục: chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực đeo đai vô địch quanh chiếc bụng béo tròn, giơ găng tay boxing đỏ vẫy chào trong tiếng hò reo vang dội của toàn thể khán đài.
```
</details>

<details><summary>L62</summary>

```text
HÌNH L62 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chúng tách ra từ một tổ tiên chung cách đây 55 triệu năm: một nhánh bơi hẳn ra biển khơi tiến hóa thành cá voi khổng lồ, còn nhánh kia ở lại đầm lầy châu Phi trở thành cỗ xe tăng bất khả chiến bại này! Chiếc đai vô địch". Bố cục: Cây gia phả 55 triệu năm: tổ tiên chung ở giữa, rẽ một nhánh sang bên trái là chú Cá Voi xanh khổng lồ dưới đại dương, rẽ sang bên phải là chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực trên đầm lầy châu Phi.
```
</details>

<details><summary>L63</summary>

```text
HÌNH L63 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tập 12 đã có chủ! Nhưng đấu trường sinh tồn sẽ không bao giờ dừng lại! Ngay bây giờ, xin mời toàn thể khán đài hướng mắt lên màn hình lớn để chiêm ngưỡng BÓNG ĐEN BÍ ẨN của tuyển thủ tiếp theo trong Tập 13!". Bố cục: Màn hình LED võ đài bỗng phụt tắt đèn màu, chuyển sang ánh sáng tím huyền bí mờ ảo; cả khán đài ồ lên tò mò hướng mắt nhìn.
```
</details>

<details><summary>L64</summary>

```text
HÌNH L64 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Xin đưa ra ba manh mối chấn động về bóng đen bí ẩn này: Thứ nhất, đây là sinh vật sống chậm chạp bậc nhất hành tinh, với tốc độ kỷ lục chỉ 0,2km/h, đến mức rêu xanh và cả một hệ sinh thái bướm đêm mọc um tùm ngay trên lớp lông của nó!". Bố cục: Trên màn hình LED lớn xuất hiện một BÓNG ĐEN HOÀN TOÀN (solid black silhouette) của một sinh vật bí ẩn đang treo ngược hai chân trên cành cây, xung quanh bóng đen tỏa ra hào quang màu tím bí ẩn và một dấu hỏi chấm khổng lồ màu vàng phát sáng rực rỡ ở giữa. KHÔNG có chú Hà Mã áo giác đấu trong cảnh này.
```
</details>

<details><summary>L65</summary>

```text
HÌNH L65 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thứ hai, mỗi tuần nó chỉ chịu leo xuống đất đi vệ sinh đúng 1 lần duy nhất, mỗi lần đi xả tới 1/3 trọng lượng cơ thể!". Bố cục: Vẫn là BÓNG ĐEN HOÀN TOÀN (solid black silhouette) treo ngược trên cành cây, trên lớp lông đen mọc ra các đám rêu xanh lá cây và đàn bướm đêm nhỏ bay quanh, bên dưới có chiếc cân đo mất 1/3 cân nặng và tờ lịch 1 tuần. KHÔNG có chú Hà Mã áo giác đấu trong cảnh này.
```
</details>

<details><summary>L66</summary>

```text
HÌNH L66 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và thứ ba, nghịch lý bi hài nhất: hơn một nửa số cái chết trong cuộc đời của sinh vật này đều xảy ra... đúng vào lúc nó xuống đất đi vệ sinh!". Bố cục: BÓNG ĐEN HOÀN TOÀN (solid black silhouette) đang từ từ leo xuống đất trong bóng đêm, bên cạnh có biển báo nguy hiểm sinh tử giật mình hài hước; dấu hỏi chấm to tướng xoay tròn. KHÔNG có chú Hà Mã áo giác đấu trong cảnh này.
```
</details>

<details><summary>L67</summary>

```text
HÌNH L67 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Quý vị khán giả có đoán ra bóng đen bí ẩn này là quái kiệt nào của thế giới tự nhiên không? Hãy để lại dự đoán và phán quyết của bạn ngay dưới phần bình luận nhé! Bình luận viên xin chào tạm biệt và hẹn gặp lại toàn thể quý vị trên sàn đấu rực lửa tiếp theo!". Bố cục: Khán đài sôi động: các bạn nhỏ và muông thú giơ các tấm bảng dấu hỏi chấm, mặt hào hứng suy đoán tên quái kiệt bóng đen; anh chàng bình luận viên esports hoạt hình đeo tai nghe gaming có micro, mặc áo vest thể thao sành điệu, hào hứng bình luận giơ tay mời gọi khán giả bình luận.
```
</details>

<details><summary>L68</summary>

```text
HÌNH L68 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "truyền đồng thời qua cả môi trường nước lẫn không khí để răn đe mọi đối thủ trong bán kính hàng cây số! Đúng là phong cách của bậc thầy lười biếng thượng thừa!". Bố cục: Mặt cắt dòng sông và không khí: luồng sóng âm thanh lan tỏa đồng thời cả trên cạn lẫn dưới nước; các đối thủ trong bán kính hàng cây số đều co rúm khiếp sợ.
```
</details>

<details><summary>L69</summary>

```text
HÌNH L69 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thiết kế này hoạt động y hệt kính tiềm vọng của tàu ngầm quân sự, cho phép tuyển thủ giấu 95% cơ thể khổng lồ dưới mặt nước mà vẫn quan sát trọn vẹn 360 độ mọi động tĩnh trên bờ!". Bố cục: Mô hình tàu ngầm quân sự có ống kính tiềm vọng thò lên mặt nước quan sát 360 độ; bên cạnh chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực ẩn mình quan sát mọi động tĩnh trên bờ.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Một sinh vật nặng tới 3 tấn ngâm mình dưới nước 16 tiếng mỗi ngày, nhưng lại hoàn toàn không biết bơi!". Bố cục: Dọc 9:16: chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực to béo nặng 3 tấn ngâm mình dưới nước sông Nile, chiếc phao vịt vàng bơi qua; anh chàng bình luận viên esports hoạt hình đeo tai nghe gaming có micro, mặc áo vest thể thao sành điệu, hào hứng bình luận chỉ tay ngạc nhiên.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Đó chính là Hà Mã, cỗ xe tăng bọc thịt hung hãn nhất đầm lầy châu Phi!". Bố cục: Dọc: chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực khổng lồ da xám hồng khoác áo choàng đỏ đứng trên bờ sông đầm lầy châu Phi, vẻ mặt bặm trợn uy dũng.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Xương của nó đặc và nặng đến mức ném xuống nước là chìm nghỉm như một khối đá tảng,". Bố cục: Mặt cắt dòng nước dọc: hòn đá tảng chìm thẳng đứng xuống đáy sông không chút nổi bồng bềnh.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Trên bờ, nó có thể bứt tốc 30km/h, sở hữu lớp da dày 5cm chống đạn". Bố cục: Dọc: chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực bứt tốc 30km/h trên cạn, bụi đất mù mịt; lớp da dày 5cm bọc thép chống đạn súng trường.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "và tự tiết ra lớp mồ hôi đỏ rực như máu để chống nắng kiêm diệt khuẩn.". Bố cục: Dọc: Cận cảnh các giọt mồ hôi màu đỏ rực như máu rỉ ra từ da chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực, ánh lên bảo vệ chống nắng và diệt khuẩn.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Đáng sợ nhất là lực cắn 1.800 PSI gấp 3 lần sư tử,". Bố cục: Dọc: chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực há to mồm khoe cặp răng nanh nhọn hoắt như hai mũi giáo thép đâm lên trời.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "kết hợp cặp răng nanh 50cm đủ sức cắn đứt đôi một con cá sấu dài 3m chỉ trong một chớp mắt!". Bố cục: Dọc: Chiếc hàm hà mã cắn sập xuống máy đo lực cắn nổ tung tóe lửa; cá sấu dài 3m bị cắn đứt đôi khúc gỗ.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Vậy là bí mật đã rõ: hà mã không cần học bơi,". Bố cục: Dọc: chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực khoanh tay mỉm cười tự tin trên bục chiến thắng, phía sau là dòng sông Nile; không cần học bơi.
```
</details>

<details><summary>S09</summary>

```text
HÌNH S09 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "nên thay vì bơi, nó chọn cách chạy bộ dưới đáy sông với tốc độ 8km/h!". Bố cục: Dưới đáy sông: chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực đang nhún chân phi nước đại chạy bộ dưới đáy sông với tốc độ 8km/h như vũ công ba-lê.
```
</details>

<details><summary>S10</summary>

```text
HÌNH S10 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hà Mã béo tròn da xám hồng, áo choàng giác đấu đỏ cam, găng tay boxing đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "vì dưới đáy sông hay trên cạn, nó sinh ra đã là một cỗ xe bọc thép bất khả chiến bại của tự nhiên!". Bố cục: Dọc: chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực đứng hiên ngang trên bờ sông đầm lầy châu Phi, áo choàng đỏ tung bay trong gió hoàng hôn rực rỡ, vẻ mặt bất khả chiến bại của một cỗ xe bọc thép tự nhiên.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/68 của video YouTube về Hà Mã). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực. Nhân vật phụ cố định: anh chàng bình luận viên esports hoạt hình đeo tai nghe gaming có micro, mặc áo vest thể thao sành điệu, hào hứng bình luận; cô phát thanh viên tin tức hoạt hình xinh đẹp ngồi sau bàn trường quay; gã đấu sĩ gấu xám khổng lồ cơ bắp cuồn cuộn đang đứng khoanh tay ngạc nhiên. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/10 của video YouTube Shorts về Hà Mã). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Hà Mã hoạt hình khổng lồ béo tròn mập mạp: da màu xám hồng nhạt bóng bẩy, chiếc mồm to bự phúng phính đáng yêu, hai mắt lồi nhỏ tròn xoe, hai tai nhỏ xíu ngoe nguẩy trên đỉnh đầu, bốn chân ngắn cũn cỡn tròn ủng, khoác áo choàng giác đấu La Mã màu đỏ cam có huy hiệu nắm đấm vàng và đeo một cặp găng tay đấm bốc boxing màu đỏ rực. Nhân vật phụ: anh chàng bình luận viên esports hoạt hình đeo tai nghe gaming có micro, mặc áo vest thể thao sành điệu, hào hứng bình luận. 
```
</details>

## 7. SEO

- **title:** Cỗ Xe Tăng 3 Tấn Cắn Đôi Cá Sấu Nhưng Không Biết Bơi?! | Hà Mã | Tập 12
- **hook_paragraph:** Hà Mã nặng tới 3 tấn sở hữu lực cắn 1.800 PSI cắn đứt đôi cá sấu, da dày 5cm, mồ hôi đỏ chống nắng tự nhiên nhưng lại hoàn toàn không biết bơi! Khám phá bí mật sinh tồn và bảng chỉ số RPG cực hạn của Cỗ xe tăng bọc thịt châu Phi.
- **question:** Bạn có đoán ra BÓNG ĐEN BÍ ẨN ở cuối video là quái kiệt nào không? (Gợi ý: chậm 0.2km/h, rêu mọc trên lưng). Bình luận dự đoán nhé!
- **next_teaser:** Bóng đen bí ẩn — sinh vật chậm 0.2km/h mọc rêu trên lưng và suýt mất mạng mỗi lần đi vệ sinh
- **shorts_title:** Cỗ Xe Tăng 3 Tấn Cắn Đôi Cá Sấu Nhưng... Không Biết Bơi?! 🦛 #shorts #hama
- **shorts_desc:** Hà Mã nặng 3 tấn cắn đôi cá sấu với lực cắn 1.800 PSI, da dày 5cm chống đạn nhưng lại hoàn toàn không biết bơi! Bí mật cỗ xe tăng chạy bộ dưới đáy sông! 🦛🌊
- **bullets:** Chỉ số HP: Nặng 3 tấn, xương đặc chìm nghỉm chạy bộ dưới đáy sông 8km/h · Phòng thủ DEF: Da dày 5cm và lớp mồ hôi máu chống nắng kiêm diệt khuẩn · Vũ khí ATK: Lực cắn 1.800 PSI gấp 3 lần sư tử, răng nanh 50cm cắn đôi cá sấu · Tuyệt chiêu bốc mùi: Quạt đuôi phân văng xa 3 mét đánh dấu lãnh thổ
- **tags:** hà mã, ha ma, hippo, hippopotamus, hà mã cắn cá sấu, hà mã không biết bơi, lực cắn hà mã, thế giới động vật, động vật hoang dã, vẽ chuyện hoang dã, whiteboard animation, khoa học thú vị, đấu trường sinh tồn
- **hashtags:** #HaMa #Hippo #TheGioiDongVat #VeChuyenHoangDa #KhoaHoc

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-12-ha-ma
python src/episode/pipeline.py tts    projects/tap-12-ha-ma     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-12-ha-ma     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-12-ha-ma     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-12-ha-ma              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-12-ha-ma --force
python scripts/beat_sheet.py projects/tap-12-ha-ma               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-12-ha-ma/audio/shorts.wav projects/tap-12-ha-ma/renders/tap-12-ha-ma_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-12-ha-ma
python src/episode/pipeline.py seo    projects/tap-12-ha-ma
python src/episode/episode_doc.py     projects/tap-12-ha-ma
```
