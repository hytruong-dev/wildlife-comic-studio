# TẬP ĐẶC BIỆT ĐẠI HỘI SINH TỒN #1 (SAU 10 TẬP ĐẦU) — 10 QUÁI KIỆT — ĐẠI HỘI SINH TỒN · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`mega-01-dai-hoi-sinh-ton`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/mega-01-dai-hoi-sinh-ton`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F_SPECIAL` · **Persona giọng:** `giai_dau` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | 10 quái kiệt — Đại Hội Sinh Tồn |
| Tiêu đề YouTube | [TẬP ĐẶC BIỆT {MINUTES} PHÚT] 10 Quái Kiệt Thi Đấu 8 Vòng Sinh Tồn: Ai Lên Ngôi Vô Địch? |
| Video dài | `renders/mega-01-dai-hoi-sinh-ton_long.mp4` — 60:07.5 (3607.5s) |
| Shorts | `renders/mega-01-dai-hoi-sinh-ton_shorts.mp4` — 0:48.6 (48.6s) |
| Thumbnail | `renders/mega-01-dai-hoi-sinh-ton_thumbnail.jpg` |
| Số hình | dài 471 beat / 471 ảnh riêng; Shorts 11 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.1**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 60:00.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/471 của video YouTube về 10 quái kiệt — Đại Hội Sinh Tồn). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: anh MC dẫn chương trình hoạt hình vui tính: tóc vuốt dựng, mặc bộ vest đỏ tươi, thắt nơ bướm vàng, cầm chiếc micro vàng, nụ cười rộng. Nhân vật phụ cố định: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — 10 QUÁI KIỆT BƯỚC VÀO ĐẠI HỘI SINH TỒN
*Thẻ chương:* 8 VÒNG THI – 1 VƯƠNG MIỆN

*Badge:* `LỄ KHAI MẠC` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene01_p0.wav` (368 ký tự) · mood `tram_bi_an`

```text
Một sân vận động khổng lồ chìm trong bóng tối... Mười chiếc bục thi đấu đứng im lặng giữa sân. Và ở chính giữa, một chiếc vương miện bé xíu đang lặng lẽ phát sáng. Đêm nay, mười sinh vật kỳ dị nhất từng bước qua kênh Vẽ Chuyện Hoang Dã sẽ quay trở lại. Nhưng lần này, không phải để kể chuyện của riêng mình... mà để thi đấu với nhau, trực tiếp, trên cùng một sân chơi!
```
**Part 1** → `audio/vs/scene01_p1.wav` (705 ký tự) · mood `hao_hung`

```text
[surprise-oh] Bật đèn! Chào mừng toàn thể khán đài đến với Đại Hội Sinh Tồn lần thứ nhất! Tôi là người dẫn chương trình đêm nay, và tôi xin hứa một điều: tất cả những gì bạn sắp nghe đều là chuyện chưa từng được kể trong mười tập phim lẻ. Hoàn toàn mới, có nguồn khoa học đàng hoàng, và... hơi điên rồ một chút! [laughter] Luật chơi rất đơn giản. Tám vòng thi, mỗi vòng một thử thách sinh tồn khác nhau. Chịu nóng và chịu lạnh. Chạy đường dài. Ăn uống. Giác quan. Nuôi con. Làm việc nhóm. Phúc khảo tin đồn. Và cuối cùng... ai giúp ích cho loài người nhiều nhất. Mỗi vòng, giám khảo sẽ trao ba tấm huy chương. Vàng được ba điểm, bạc được hai điểm, đồng được một điểm. Ai nhiều điểm nhất sẽ đội vương miện!
```
**Part 2** → `audio/vs/scene01_p2.wav` (72 ký tự) · 🎭 cameo `tham_phan`

```text
Giám khảo xin nhắc: không cắn, không đấm, không xịt mùi hôi vào đối thủ!
```
**Part 3** → `audio/vs/scene01_p3.wav` (148 ký tự) · mood `hao_hung`

```text
Nghe rõ chưa, toàn thể tuyển thủ? Đặc biệt là... một vài cá nhân có tiền sử hơi nóng tính! [laughter] Và bây giờ, xin mời các tuyển thủ bước ra sân!
```
**Part 4** → `audio/vs/scene01_p4.wav` (341 ký tự) · mood `don_dap`

```text
Tuyển thủ số một! Nặng chưa tới mười hai ki-lô-gam! Từng nhai rắn hổ mang như nhai bim bim! Lửng Mật! Tuyển thủ số hai! Võ sĩ có cú đấm nhanh nhất đại dương! Tôm Tít! Tuyển thủ số ba! Kẻ bất tử tí hon! Gấu Nước! Ban tổ chức phải phát kính lúp cho khán giả mới nhìn thấy cậu ấy! [laughter] Tuyển thủ số bốn! Gã liều mạng xứ tuyết! Chồn Gu-lô!
```
**Part 5** → `audio/vs/scene01_p5.wav` (238 ký tự) · mood `hao_hung`

```text
Tuyển thủ số năm, quý ông mặc vest của Nam Cực, Chim Cánh Cụt! Số sáu, Rái Cá Biển! Số bảy, Cá Heo! Tuyển thủ số tám, Chim Bồ Nông, và cái mỏ đi trước chủ nhân... hai giây! [laughter] Tuyển thủ số chín, Thú Mỏ Vịt! Và tuyển thủ số mười...
```
**Part 6** → `audio/vs/scene01_p6.wav` (84 ký tự) · mood `nghiem_trang_gia`

```text
Tuyển thủ số mười... xin lỗi toàn thể khán đài, tuyển thủ số mười hiện vẫn đang ngủ.
```
**Part 7** → `audio/vs/scene01_p7.wav` (69 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Ủa... đến lượt cháu chưa ạ? Cháu vừa mơ thấy một cái cây to ơi là to!
```
**Part 8** → `audio/vs/scene01_p8.wav` (177 ký tự) · mood `hao_hung`

```text
Rồi, Gấu Cô-a-la cũng đã có mặt! Nhưng trước khi xem dự đoán, theo đúng truyền thống của mọi giải đấu lớn, chúng ta có... lễ cân ký! Mời các tuyển thủ lần lượt bước lên bàn cân.
```
**Part 9** → `audio/vs/scene01_p9.wav` (435 ký tự) · mood `don_dap`

```text
Cá Heo bước lên! Kim cân quay vù vù! Một chú cá heo mũi chai trưởng thành có thể nặng từ một trăm năm mươi đến hơn sáu trăm ki-lô-gam! Tuyển thủ nặng ký nhất đại hội! Chim Bồ Nông bước lên! Cân nặng thì vừa phải, nhưng đôi cánh dang ra dài hơn hai mét rưỡi! Ban tổ chức phải mở rộng cả cửa phòng cân! [laughter] Rái Cá Biển bước lên, ôm theo hòn đá! Ban tổ chức yêu cầu bỏ hòn đá ra. Rái Cá... từ chối. Thôi, cân luôn cả đá! [laughter]
```
**Part 10** → `audio/vs/scene01_p10.wav` (508 ký tự) · mood `hao_hung`

```text
Lửng Mật và Chồn Gu-lô bước lên cùng lúc, vì không ai chịu nhường ai. Hai gã nặng chừng một bao gạo nhỏ, nhưng nhìn cách hai gã gườm nhau thì... tưởng nặng cả tấn! Chim Cánh Cụt, Cô-a-la, Thú Mỏ Vịt lần lượt bước lên. Thú Mỏ Vịt nhẹ nhất trong ba bạn, chỉ khoảng một đến hai ký, nhẹ hơn cả một con mèo nhà. Tôm Tít bước lên, dài chưa tới một gang tay. Và cuối cùng... Gấu Nước. Kim cân không nhúc nhích. Chiếc cân điện tử cũng không nhúc nhích. Ban tổ chức phải mang tới... một chiếc kính hiển vi. [laughter]
```
**Part 11** → `audio/vs/scene01_p11.wav` (169 ký tự) · mood `nghiem_trang_gia`

```text
Gấu Nước dài chưa tới một mi-li-mét. Chênh lệch giữa tuyển thủ nặng nhất và nhẹ nhất đại hội lớn đến mức... các nhà toán học của ban tổ chức đã xin nghỉ phép. [laughter]
```
**Part 12** → `audio/vs/scene01_p12.wav` (275 ký tự) · mood `hao_hung`

```text
Cân ký xong! Đủ mười tuyển thủ! Và trước khi vào vòng một, chúng ta cùng xem dự đoán của các chuyên gia. Theo dự đoán, Lửng Mật, Tôm Tít và Gấu Nước là ba ứng cử viên nặng ký nhất. Còn Thú Mỏ Vịt và Cô-a-la... chuyên gia chỉ ghi chú đúng một câu: tham gia cho vui. [laughter]
```
**Part 13** → `audio/vs/scene01_p13.wav` (227 ký tự) · mood `tram_bi_an`

```text
Nhưng các chuyên gia đâu phải lúc nào cũng đúng. Đêm nay, mọi con số sẽ được kiểm chứng lại từ đầu. Không có chuyện cũ. Không có huyền thoại. Chỉ có khoa học, chỉ có những bằng chứng được đo đạc thật... và một chiếc vương miện.
```
**Part 14** → `audio/vs/scene01_p14.wav` (100 ký tự) · mood `hao_hung`

```text
Vòng một bắt đầu ngay sau đây, và nó sẽ khiến các tuyển thủ... hoặc là đóng băng, hoặc là chín luôn!
```

### scene02 — THỬ THÁCH NÓNG VÀ LẠNH — AI GIỮ ẤM, AI GIẢI NHIỆT GIỎI NHẤT
*Thẻ chương:* ĐÓNG BĂNG HAY CHÍN LUÔN?

*Badge:* `VÒNG 1` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene02_p0.wav` (379 ký tự) · mood `hao_hung`

```text
Vòng một: thử thách nóng và lạnh! Câu hỏi rất đơn giản: khi trời nóng như lò nướng, hoặc lạnh như tủ đá, cơ thể bạn làm gì để sống sót? Ban giám khảo không chấm ai to khỏe nhất. Ban giám khảo chấm ai thông minh nhất trong việc điều khiển nhiệt độ của chính mình. Phần thi nóng mở màn. Và người đầu tiên bước vào sân là một tuyển thủ mà ai cũng nghĩ là... sẽ ngủ gật ngay lập tức.
```
**Part 1** → `audio/vs/scene02_p1.wav` (224 ký tự) · mood `nghiem_trang_gia`

```text
Hồ sơ tuyển thủ Gấu Cô-a-la. Bộ lông: dày. Nơi ở: trên cây, không có hang, không có điều hòa. Kế hoạch chống nóng: chưa rõ. Nhưng các nhà khoa học ở Úc đã phát hiện ra một bí mật mà chính Cô-a-la giữ kín suốt hàng triệu năm.
```
**Part 2** → `audio/vs/scene02_p2.wav` (811 ký tự) · mood `nghiem_trang_gia`

```text
Năm hai ngàn mười bốn, họ mang máy ảnh nhiệt vào rừng, theo dõi những con Cô-a-la hoang dã trong những ngày nắng gắt trên ba mươi độ C. Và họ thấy một hành động rất lạ: trời càng nóng, Cô-a-la càng leo xuống thấp, rồi dang tay dang chân... ôm chặt lấy thân cây như ôm gối ôm! Hình ảnh nhiệt cho thấy lý do: thân cây keo mát hơn không khí xung quanh hơn năm độ C. Cô-a-la đang dùng cái cây như một chiếc tủ lạnh khổng lồ! [laughter] Và đây không phải ôm cho vui. Theo tính toán của các nhà khoa học, chỉ riêng việc ôm cây đã giúp Cô-a-la tiết kiệm khoảng một nửa lượng nước cần để làm mát cơ thể trong một ngày nóng. Điều buồn cười nhất: cây keo này Cô-a-la không hề ăn. Nó leo sang cây keo chỉ để... ôm cho mát, xong lại leo về cây khuynh diệp để ăn. Một cây làm phòng ăn, một cây làm phòng điều hòa! [laughter]
```
**Part 3** → `audio/vs/scene02_p3.wav` (306 ký tự) · mood `tram_bi_an`

```text
Nhưng chống nóng mới chỉ là một nửa. Nửa còn lại là chuyện... uống nước. Trong hàng trăm năm, người ta tin rằng Cô-a-la lấy gần hết nước từ lá, chỉ uống khi nắng nóng khắc nghiệt. Cho đến năm hai ngàn hai mươi, khi một nhóm nhà khoa học tập hợp bốn mươi sáu lần quan sát Cô-a-la hoang dã... đang uống nước.
```
**Part 4** → `audio/vs/scene02_p4.wav` (333 ký tự) · mood `hao_hung`

```text
Và cách uống thì... không giống ai. Khi trời mưa, nước chảy thành dòng dọc theo thân cây trơn. Cô-a-la ôm cây, thè lưỡi... và liếm từng dòng nước mưa từ trên xuống! [laughter] Có một cô Cô-a-la mẹ đã uống liên tục như thế suốt mười lăm phút không nghỉ. Cây cối với Cô-a-la vừa là nhà, vừa là bếp, vừa là điều hòa, vừa là... vòi nước!
```
**Part 5** → `audio/vs/scene02_p5.wav` (72 ký tự) · 🎭 cameo `tham_phan`

```text
Giám khảo ghi nhận: chiến thuật tiết kiệm, khoa học, và... rất đáng yêu.
```
**Part 6** → `audio/vs/scene02_p6.wav` (284 ký tự) · mood `hao_hung`

```text
Phần thi nóng tiếp theo, chúng ta có hai tuyển thủ đến từ biển lạnh. Rái Cá Biển và Chim Cánh Cụt đều đứng nhìn nửa sân sa mạc với ánh mắt... không mấy thiện cảm. [laughter] Hai bạn xin phép chuyển sang phần thi lạnh. Và giám khảo đồng ý, vì phần thi lạnh mới là chiến trường thật sự!
```
**Part 7** → `audio/vs/scene02_p7.wav` (283 ký tự) · mood `tram_bi_an`

```text
Phần thi lạnh. Nhiệt độ nước: gần bằng không độ C. Ở mức này, một con người không được bảo hộ chỉ trụ được rất ngắn trước khi cơ thể bắt đầu mất kiểm soát. Tuyển thủ đầu tiên nhảy xuống, và cả sân vận động cùng... há hốc mồm. Không phải Rái Cá, không phải Cánh Cụt. Mà là Thú Mỏ Vịt!
```
**Part 8** → `audio/vs/scene02_p8.wav` (97 ký tự) · 🎭 cameo `phat_thanh_vien`

```text
Tin khẩn từ hồ băng: tuyển thủ được dự đoán "tham gia cho vui" vừa nhảy xuống nước lạnh nhất sân!
```
**Part 9** → `audio/vs/scene02_p9.wav` (491 ký tự) · mood `hao_hung`

```text
Nhiều người quên mất rằng Thú Mỏ Vịt không chỉ sống ở những con suối ấm. Ở đảo Ta-xma-ni-a và những dòng sông trên núi cao nước Úc, mùa đông nước sông lạnh gần bằng không độ C. Các nhà khoa học đã gắn thiết bị đo nhiệt độ vào những con Thú Mỏ Vịt hoang dã và theo dõi chúng suốt mùa đông. Kết quả khiến họ phải đo lại mấy lần. Một con Thú Mỏ Vịt đã bơi trong dòng nước không độ C ở một con sông đóng băng một phần suốt ít nhất năm tiếng liền, mà nhiệt độ cơ thể vẫn giữ nguyên, không hề tụt.
```
**Part 10** → `audio/vs/scene02_p10.wav` (235 ký tự) · mood `nghiem_trang_gia`

```text
Và nhiệt độ cơ thể ấy là bao nhiêu? Chỉ khoảng ba mươi hai độ C, thấp hơn người chúng ta khoảng năm độ. Tức là Thú Mỏ Vịt chạy máy sưởi ở mức tiết kiệm điện... mà vẫn ấm áp giữa nước đá. Nghe như quảng cáo điều hòa inverter! [laughter]
```
**Part 11** → `audio/vs/scene02_p11.wav` (581 ký tự) · mood `nghiem_trang_gia`

```text
Bí quyết nằm ở ba lớp bảo vệ. Thứ nhất là bộ lông: lớp lông tơ xoăn tít bên dưới giữ lại một lớp không khí sát da, giống chiếc áo phao bằng không khí. Theo các nhà nghiên cứu, khả năng cách nhiệt của bộ lông này còn cao hơn cả lông gấu Bắc Cực và lông hải ly! Thứ hai, ở gốc chân sau và gốc đuôi có một mạng lưới mạch máu đặc biệt, hoạt động như bộ trao đổi nhiệt: máu nóng chảy ra sưởi ấm cho máu lạnh chảy về, nên hơi ấm không bị thất thoát ra nước. Và thứ ba: khi lạnh hơn, Thú Mỏ Vịt chỉ đơn giản là... đốt năng lượng nhiều hơn. Lò sưởi bên trong cứ thế cháy đều, không hề tắt.
```
**Part 12** → `audio/vs/scene02_p12.wav` (85 ký tự) · 🎭 cameo `tham_phan`

```text
Giám khảo xin ghi nhận: tuyển thủ số chín... đã gây bất ngờ lớn đầu tiên của đêm nay.
```
**Part 13** → `audio/vs/scene02_p13.wav` (441 ký tự) · mood `don_dap`

```text
Rái Cá Biển cũng không chịu thua. Không có lớp mỡ dày như hải cẩu, Rái Cá có một mẹo giữ ấm cực kỳ đơn giản mà khán giả có thể tự quan sát. Khi nghỉ ngơi trên mặt nước, Rái Cá Biển giơ bàn tay và bàn chân lên khỏi mặt nước. Vì bàn tay ít lông, mà nước lại hút hơi nóng nhanh hơn không khí rất nhiều lần. Đôi khi Rái Cá còn úp hai bàn tay lên mắt khi ngủ, trông như đang ngại ngùng, nhưng thật ra là đang... giữ ấm cho đôi bàn tay! [laughter]
```
**Part 14** → `audio/vs/scene02_p14.wav` (413 ký tự) · mood `tram_bi_an`

```text
Tuyển thủ tiếp theo không cần nước lạnh. Hắn cần tuyết. Rất nhiều tuyết. Chồn Gu-lô bước vào khu băng giá, nhìn quanh... và bắt đầu đào. Các nhà khoa học đã đánh dấu toàn bộ năm trăm sáu mươi hai hang sinh con của Chồn Gu-lô từng được tìm thấy ở Bắc Mỹ và Bắc Âu lên bản đồ vệ tinh. Và kết quả trùng khớp đến kinh ngạc: tất cả các hang đều nằm ở nơi tuyết vẫn còn phủ dày cho đến cuối mùa xuân. Không có ngoại lệ.
```
**Part 15** → `audio/vs/scene02_p15.wav` (281 ký tự) · mood `am_ap`

```text
Chồn mẹ đào đường hầm dưới lớp tuyết dày hơn một mét, có khi là cả một mê cung nhiều ngã rẽ, để sinh con giữa mùa đông. Tuyết nghe thì lạnh, nhưng lớp tuyết dày lại là tấm chăn cách nhiệt tuyệt vời: bên ngoài gió bão gào thét, bên trong hang vẫn yên ổn như trong một chiếc túi ngủ.
```
**Part 16** → `audio/vs/scene02_p16.wav` (239 ký tự) · mood `bi_hai`

```text
[sigh] Và cũng vì thế mà Chồn Gu-lô sợ nhất là... mùa xuân đến quá sớm. Tuyết tan sớm thì hang sụp, nhà không còn, chồn con phơi mình giữa trời. Kẻ dám cướp mồi của gấu xám lại có một nỗi lo mà ai nghe cũng thấy thương: lo trái đất ấm lên.
```
**Part 17** → `audio/vs/scene02_p17.wav` (434 ký tự) · mood `hao_hung`

```text
Và cuối cùng, tuyển thủ được đặt cược nhiều nhất vòng này: Gấu Nước, kẻ từng sống sót ở nhiệt độ thấp đến khó tin. Cậu ấy bước vào tủ đông... Năm hai ngàn hai mươi hai, các nhà khoa học Đức làm một thí nghiệm thú vị: cứ một tuần cho Gấu Nước đông đá ở âm ba mươi độ C, rồi tuần sau rã đông, cho ăn, rồi lại đông đá. Lặp lại như vậy cho đến khi chúng chết vì tuổi già. Và nhóm Gấu Nước được đông đá sống lâu gấp đôi nhóm không đông đá!
```
**Part 18** → `audio/vs/scene02_p18.wav` (231 ký tự) · mood `nghiem_trang_gia`

```text
Nhưng phần thú vị nằm ở phép trừ: nếu bỏ đi thời gian nằm trong tủ đông, thì tuổi thọ của hai nhóm... bằng nhau. Nghĩa là khi bị đông đá, Gấu Nước không già đi chút nào. Đồng hồ sinh học dừng hẳn, như nàng công chúa ngủ trong rừng!
```
**Part 19** → `audio/vs/scene02_p19.wav` (95 ký tự) · 🎭 cameo `tham_phan`

```text
Giám khảo xin thông báo: tuyển thủ Gấu Nước hiện đang đông đá và... từ chối tham gia chấm điểm.
```
**Part 20** → `audio/vs/scene02_p20.wav` (126 ký tự) · mood `hao_hung`

```text
Đúng vậy! Đông đá thì không già, nhưng cũng không thi được! Gấu Nước tự loại mình khỏi vòng một vì... ngủ quá ngon! [laughter]
```
**Part 21** → `audio/vs/scene02_p21.wav` (318 ký tự) · mood `hao_hung`

```text
Và đây là kết quả vòng một! Huy chương đồng: Gấu Cô-a-la, bậc thầy ôm cây giải nhiệt và uống nước mưa! Huy chương bạc: Chồn Gu-lô, kiến trúc sư đường hầm dưới tuyết dày! Và huy chương vàng vòng một thuộc về... tuyển thủ mà chuyên gia nói tham gia cho vui: Thú Mỏ Vịt, người bơi năm tiếng trong nước không độ mà vẫn ấm!
```
**Part 22** → `audio/vs/scene02_p22.wav` (253 ký tự) · mood `hao_hung`

```text
Bảng điểm sau vòng một: Thú Mỏ Vịt ba điểm, Chồn Gu-lô hai điểm, Cô-a-la một điểm. Còn Lửng Mật và Tôm Tít, hai ứng cử viên nặng ký... vẫn chưa có điểm nào! Đừng lo, vòng hai sẽ là vòng của những đôi chân. Và có người sẽ phải đi bộ... nửa vòng trái đất!
```

### scene03 — MARATHON SINH TỒN — AI ĐI XA NHẤT, DI CHUYỂN LẠ NHẤT
*Thẻ chương:* AI ĐI XA NHẤT HÀNH TINH?

*Badge:* `VÒNG 2` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene03_p0.wav` (264 ký tự) · mood `hao_hung`

```text
Vòng hai: marathon sinh tồn! Trong tự nhiên, thức ăn không tự bò đến miệng. Muốn sống, phải đi. Và có những tuyển thủ đi xa đến mức... bản đồ phải vẽ thêm trang! Giám khảo sẽ chấm hai tiêu chí: quãng đường đi được, và độ khó của hành trình. Mời tuyển thủ đầu tiên!
```
**Part 1** → `audio/vs/scene03_p1.wav` (477 ký tự) · mood `don_dap`

```text
Lửng Mật xuất phát! Không cần khởi động! Không cần bản đồ! Chỉ cần cái mũi! Các nhà khoa học ở sa mạc Ka-la-ha-ri đã đeo vòng cổ định vị cho hai mươi lăm con Lửng Mật, rồi kiên nhẫn đi theo chúng suốt nhiều năm. Kết quả: mỗi đêm đi kiếm ăn, một con Lửng Mật đực đi trung bình gần mười bốn cây số. Có những ngày còn đi tới hai mươi bảy cây số! Và đi không phải để dạo chơi. Trong một lần đi kiếm ăn, Lửng Mật có thể đào tới năm mươi cái hố để lôi chuột và thằn lằn ra khỏi hang.
```
**Part 2** → `audio/vs/scene03_p2.wav` (467 ký tự) · mood `tram_bi_an`

```text
Và có một chuyện mà ít ai biết: Lửng Mật không bao giờ đi một mình. Trên đầu nó thường có... một đoàn tùy tùng bay theo! Đó là loài chim ưng xám có tiếng hót như đang hát. Chúng bám theo Lửng Mật, chờ nó đào hang. Con chuột nào hoảng hốt chạy thoát lên mặt đất... là chim ưng sà xuống chộp liền! [laughter] Các nhà khoa học đã từng thấy tới sáu con chim ưng cùng đi theo một con Lửng Mật. Và chim ưng săn mồi thành công hơn hẳn khi đi theo Lửng Mật so với khi tự săn.
```
**Part 3** → `audio/vs/scene03_p3.wav` (237 ký tự) · mood `nghiem_trang_gia`

```text
Còn Lửng Mật được gì từ đoàn tùy tùng này? Các nhà khoa học đo đạc kỹ và trả lời: không được gì cả. Không mất gì, cũng chẳng được gì. Một gã giang hồ đi đâu cũng có đàn em bám theo hưởng sái, mà bản thân gã... chẳng thèm để ý! [laughter]
```
**Part 4** → `audio/vs/scene03_p4.wav` (292 ký tự) · mood `tram_bi_an`

```text
Nhưng nếu Lửng Mật đi xa trong một đêm, thì có một tuyển thủ đi xa... trong cả một mùa xuân. Hồ sơ em năm mươi sáu. Mùa xuân năm hai ngàn lẻ chín, một chú Chồn Gu-lô đực còn trẻ, được đặt mã số em năm mươi sáu, rời khỏi vùng núi gần công viên quốc gia Grand Tê-tôn ở bang Uai-ô-minh, nước Mỹ.
```
**Part 5** → `audio/vs/scene03_p5.wav` (253 ký tự) · mood `don_dap`

```text
Nó đi về phía Nam. Băng qua núi đá! Băng qua đồng cỏ! Và băng qua cả đường cao tốc liên bang số tám mươi, nơi xe tải chạy ầm ầm ngày đêm! Hai tháng sau, các nhà nghiên cứu nhận được tín hiệu từ... bang Cô-lô-ra-đô. Chú chồn đã đi khoảng tám trăm cây số!
```
**Part 6** → `audio/vs/scene03_p6.wav` (280 ký tự) · mood `hao_hung`

```text
Và đây là điều khiến cả nước Mỹ xôn xao: đó là con Chồn Gu-lô đầu tiên được ghi nhận ở bang Cô-lô-ra-đô kể từ năm một ngàn chín trăm mười chín. Chín mươi năm vắng bóng! Có một nhiếp ảnh gia còn chụp được nó trong công viên quốc gia núi Rốc-ky, khiến giới yêu thiên nhiên phát sốt.
```
**Part 7** → `audio/vs/scene03_p7.wav` (257 ký tự) · mood `nghiem_trang_gia`

```text
Chuyện vui hơn nữa. Ở nước Mỹ, bang Mi-si-gân có biệt danh là "bang Chồn Gu-lô". Đội thể thao của trường đại học lớn nhất bang cũng tên là Chồn Gu-lô. Thế nhưng suốt hai trăm năm, chưa hề có ai chứng minh được Chồn Gu-lô thật sự sống ở Mi-si-gân! [laughter]
```
**Part 8** → `audio/vs/scene03_p8.wav` (359 ký tự) · mood `nghiem_trang_gia`

```text
Cho đến đầu năm hai ngàn lẻ bốn, một nhóm thợ săn đang đuổi theo dấu chân lạ thì thấy một con vật leo tót lên cây. Nhà sinh vật học được gọi đến, chụp ảnh, xác nhận: đó là một con Chồn Gu-lô thật! Bang Chồn Gu-lô cuối cùng cũng có một con Chồn Gu-lô thật, sau hai trăm năm chờ đợi. Như đội bóng đá cuối cùng cũng tìm được... linh vật thật của mình! [laughter]
```
**Part 9** → `audio/vs/scene03_p9.wav` (328 ký tự) · mood `hao_hung`

```text
Nhưng cả Lửng Mật lẫn Chồn Gu-lô đều phải ngả mũ trước tuyển thủ tiếp theo. Một chú chim cao chưa tới bảy mươi xăng-ti-mét. Không biết bay. Và đi bộ thì... lạch bạch. Các nhà khoa học đã gắn những thiết bị định vị nhỏ xíu lên những chú Chim Cánh Cụt A-đê-li ở đảo Rốt, vùng cực Nam của Trái Đất, và theo dõi chúng suốt mùa đông.
```
**Part 10** → `audio/vs/scene03_p10.wav` (286 ký tự) · mood `don_dap`

```text
Kết quả: mỗi năm, những chú chim này di chuyển trung bình khoảng mười ba ngàn cây số! Chuyến dài nhất được ghi nhận lên tới mười bảy ngàn sáu trăm cây số! Để dễ hình dung: quãng đường đó dài hơn đi từ Hà Nội sang tận nước Mỹ! Bằng đôi chân ngắn củn và cái bụng làm ván trượt! [laughter]
```
**Part 11** → `audio/vs/scene03_p11.wav` (292 ký tự) · mood `tram_bi_an`

```text
Vì sao phải đi xa đến thế? Vì mùa đông ở Nam Cực, mặt trời biến mất hoàn toàn. Không có ánh sáng, chim cánh cụt không nhìn thấy để săn mồi. Thế là chúng đi theo mặt trời. Cả đàn trôi trên những tảng băng, đi dần về phía Bắc, đến những nơi mỗi ngày còn vài tiếng chạng vạng, đủ sáng để bắt cá.
```
**Part 12** → `audio/vs/scene03_p12.wav` (152 ký tự) · mood `am_ap`

```text
Đến mùa xuân, chúng lại hối hả quay về đúng bãi đá cũ để làm tổ. Một chú chim không biết bay, đi theo mặt trời, mỗi năm một vòng lớn quanh đáy Trái Đất.
```
**Part 13** → `audio/vs/scene03_p13.wav` (343 ký tự) · mood `am_ap`

```text
Mà khoan, khán giả có biết vì sao loài chim này tên là A-đê-li không? Năm một ngàn tám trăm bốn mươi, nhà thám hiểm người Pháp Duy-moong Đuy-vin đặt tên cho một vùng đất ở Nam Cực theo tên vợ mình, bà A-đen. Và loài chim cánh cụt sống ở đó được đặt theo tên vùng đất. Vậy là Quý ông Vest Đuôi Tôm thật ra... mang tên của một quý bà! [laughter]
```
**Part 14** → `audio/vs/scene03_p14.wav` (259 ký tự) · mood `hao_hung`

```text
Trong khi đó, ở đường đua dưới nước, một tuyển thủ bị sóng đánh dạt lên bãi cát. Tôm Tít mắc cạn! Chân ngắn, không đi được trên cạn. Các đối thủ đã nghĩ: thế là xong. Nhưng ở bờ biển Pa-na-ma, có một loài tôm tít nhỏ tí xíu có cách thoát thân độc nhất vô nhị.
```
**Part 15** → `audio/vs/scene03_p15.wav` (317 ký tự) · mood `don_dap`

```text
Nó nằm ngửa, cong người lại thành một vòng tròn... rồi lộn nhào ra phía sau! Một vòng! Hai vòng! Rồi hàng chục vòng liên tục, có khi tới bốn mươi vòng không nghỉ! Bảy mươi hai vòng mỗi phút, lăn được tới hai mét để quay về biển! Các nhà khoa học công bố trên tạp chí Nây-chơ với tựa đề: Di chuyển như một cái bánh xe?
```
**Part 16** → `audio/vs/scene03_p16.wav` (112 ký tự) · mood `hao_hung`

```text
Loài người mất hàng ngàn năm mới phát minh ra cái bánh xe. Còn tôm tít... tự biến mình thành bánh xe! [laughter]
```
**Part 17** → `audio/vs/scene03_p17.wav` (468 ký tự) · mood `don_dap`

```text
Cuối cùng, Chim Bồ Nông bước vào đường đua... và không chạy. Nó dang cánh, lấy đà, và bay lên. Ban giám khảo cho phép, vì đây là cách di chuyển của nó. Bồ Nông rất ít khi đập cánh liên tục. Nó tìm những luồng khí nóng bốc lên từ mặt đất, rồi xoay vòng tròn để được nâng lên cao, như ngồi thang máy miễn phí. Bồ Nông Úc từng được ghi nhận bay ở độ cao hàng ngàn mét, cao đến mức người dưới đất không còn nhìn thấy, rồi lượn đi hàng chục cây số mà gần như không tốn sức.
```
**Part 18** → `audio/vs/scene03_p18.wav` (492 ký tự) · mood `tram_bi_an`

```text
Và đây là bí ẩn lớn nhất của vòng thi. Giữa nước Úc có một hồ nước mặn khổng lồ tên là hồ Ây-rơ. Phần lớn thời gian, hồ khô cạn, chỉ còn lớp muối trắng xóa. Nhưng cứ vài năm, mưa lớn ở tận phía Bắc lại đổ nước về hồ. Và chỉ ít lâu sau, hàng chục ngàn con Bồ Nông từ khắp nước Úc bỗng nhiên... bay đến, dù cách xa cả ngàn cây số. Năm một ngàn chín trăm tám mươi chín, các nhà khoa học ước tính đã có khoảng một trăm ngàn chú Bồ Nông con ra đời trên hồ này. Một trận bùng nổ dân số giữa sa mạc!
```
**Part 19** → `audio/vs/scene03_p19.wav` (321 ký tự) · mood `nghiem_trang_gia`

```text
Câu hỏi: làm sao Bồ Nông biết hồ có nước, khi nó cách xa cả ngàn cây số? Câu trả lời của khoa học hiện nay là: chưa ai biết chắc. Có giả thuyết cho rằng chúng ngửi được, có giả thuyết cho rằng chúng nghe được sóng âm từ xa, có giả thuyết cho rằng có những con bồ nông già đi do thám trước rồi về... rủ cả nhóm! [laughter]
```
**Part 20** → `audio/vs/scene03_p20.wav` (272 ký tự) · mood `hao_hung`

```text
Tổng kết đường đua: một gã đào hố mười bốn cây số mỗi đêm, một chú chồn băng qua cả đường cao tốc, một chú chim không biết bay đi vòng quanh Nam Cực, một chú tôm tự biến thành bánh xe, và một chú bồ nông đi tìm hồ nước bằng một giác quan mà khoa học còn chưa gọi được tên.
```
**Part 21** → `audio/vs/scene03_p21.wav` (88 ký tự) · 🎭 cameo `tham_phan`

```text
Giám khảo xin tuyên bố kết quả vòng hai. Đây là vòng thi khó chấm nhất từ trước đến nay.
```
**Part 22** → `audio/vs/scene03_p22.wav` (232 ký tự) · mood `hao_hung`

```text
Huy chương đồng: Tôm Tít, nhà phát minh ra bánh xe sống! Huy chương bạc: Chồn Gu-lô, tám trăm cây số và một tấm ảnh lên trang nhất! Và huy chương vàng: Chim Cánh Cụt, mười ba ngàn cây số mỗi năm, đi theo mặt trời quanh đáy Trái Đất!
```
**Part 23** → `audio/vs/scene03_p23.wav` (182 ký tự) · mood `hao_hung`

```text
Bảng điểm sau hai vòng: Chồn Gu-lô vươn lên dẫn đầu với bốn điểm! Thú Mỏ Vịt và Chim Cánh Cụt cùng ba điểm. Cô-a-la và Tôm Tít mỗi bạn một điểm. Còn Lửng Mật... vẫn chưa có điểm nào!
```
**Part 24** → `audio/vs/scene03_p24.wav` (55 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Ủa... đi bộ xa vậy có được ăn gì không ạ? Cháu đói rồi.
```
**Part 25** → `audio/vs/scene03_p25.wav` (72 ký tự) · mood `hao_hung`

```text
Câu hỏi hay lắm, tuyển thủ Cô-a-la! Vì vòng ba chính là... vòng ăn uống!
```

### scene04 — BẾP TRƯỞNG HOANG DÃ — AI ĂN KHÉO, ĂN NHIỀU, ĂN LẠ NHẤT
*Thẻ chương:* AI LÀ VUA ĂN UỐNG?

*Badge:* `VÒNG 3` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene04_p0.wav` (163 ký tự) · mood `hao_hung`

```text
Vòng ba: bếp trưởng hoang dã! Mỗi tuyển thủ phải trình bày cách mình kiếm ăn trước ban giám khảo. Điểm cộng cho sự khéo léo, cho sự sáng tạo, và cho... độ khó tin!
```
**Part 1** → `audio/vs/scene04_p1.wav` (280 ký tự) · mood `hao_hung`

```text
Mở màn là Thú Mỏ Vịt, nhà vô địch vòng một. Và bí mật đầu tiên của Thú Mỏ Vịt là: nó ăn khỏe đến mức khó tin. Một con Thú Mỏ Vịt trưởng thành ăn mỗi ngày lượng thức ăn bằng khoảng một phần năm trọng lượng cơ thể. Nhưng một Thú Mỏ Vịt mẹ đang nuôi con còn ăn khủng khiếp hơn nhiều!
```
**Part 2** → `audio/vs/scene04_p2.wav` (233 ký tự) · mood `nghiem_trang_gia`

```text
Có những tài liệu ghi nhận Thú Mỏ Vịt mẹ đang cho con bú có thể ăn gần bằng cả cân nặng của chính mình mỗi ngày. Tức là nếu một người mẹ nặng năm mươi ki-lô-gam ăn theo kiểu này, mỗi ngày phải ăn... năm mươi ki-lô-gam cơm! [laughter]
```
**Part 3** → `audio/vs/scene04_p3.wav` (541 ký tự) · mood `nghiem_trang_gia`

```text
Mà ăn khỏe như vậy là có lý do. Thú Mỏ Vịt mẹ không có núm vú, sữa tiết ra qua da bụng, nên con non phải liếm. Và chính sữa ấy đã làm các nhà khoa học bất ngờ vào năm hai ngàn mười tám. Các nhà khoa học ở Úc đã tách ra từ sữa Thú Mỏ Vịt một loại đạm có khả năng diệt vi khuẩn. Và khi nhìn hình dạng ba chiều của nó, họ thấy một cấu trúc chưa từng gặp bao giờ. Phân tử ấy xoăn tít như những lọn tóc lò xo, nên các nhà khoa học đặt tên cho kiểu cấu trúc này theo tên một ngôi sao nhí tóc xoăn nổi tiếng của Hollywood: Shơ-li Tem-pồ! [laughter]
```
**Part 4** → `audio/vs/scene04_p4.wav` (362 ký tự) · mood `hao_hung`

```text
Vì sao sữa Thú Mỏ Vịt cần chất diệt khuẩn mạnh như vậy? Vì sữa chảy ra ngoài da, dính đầy bụi bẩn và vi khuẩn, mà con non lại liếm trực tiếp. Không có lớp bảo vệ này, con non dễ bị nhiễm khuẩn. Ngày nay, các nhà khoa học hy vọng loại đạm này có thể giúp tìm ra cách mới chống lại những loại vi khuẩn kháng thuốc. Từ một con vật từng bị tưởng là đồ giả khâu ghép!
```
**Part 5** → `audio/vs/scene04_p5.wav` (86 ký tự) · 🎭 cameo `tham_phan`

```text
Giám khảo ghi nhận: món ăn chưa ngon, nhưng sữa thì... có thể cứu người. Rất ấn tượng.
```
**Part 6** → `audio/vs/scene04_p6.wav` (306 ký tự) · mood `hao_hung`

```text
Quầy bếp tiếp theo: Rái Cá Biển. Và Rái Cá mang theo một dụng cụ nấu ăn rất đặc biệt: một hòn đá. Năm hai ngàn hai mươi tư, các nhà khoa học công bố một nghiên cứu theo dõi một trăm chín mươi sáu con Rái Cá Biển ở bang Ca-li-phoóc-ni-a, nước Mỹ, trong nhiều năm. Họ muốn biết: dùng công cụ thì được lợi gì?
```
**Part 7** → `audio/vs/scene04_p7.wav` (341 ký tự) · mood `nghiem_trang_gia`

```text
Câu trả lời: những con dùng đá đập vỏ thì răng ít bị mẻ hơn hẳn những con chỉ dùng răng cắn. Và răng mà hỏng thì Rái Cá không ăn được, nghĩa là không sống nổi! Điều thú vị: rái cá cái dùng đá nhiều hơn rái cá đực. Nhờ hòn đá, những con cái nhỏ con hơn vẫn ăn được những con mồi vỏ cứng hơn gần gấp ba lần so với những con không dùng công cụ.
```
**Part 8** → `audio/vs/scene04_p8.wav` (142 ký tự) · mood `nghiem_trang_gia`

```text
Bài học từ bếp Rái Cá: nếu bạn bóc được vỏ cua bằng dụng cụ, đừng bao giờ dùng răng! Nha sĩ của kênh Vẽ Chuyện Hoang Dã xin cảm ơn. [laughter]
```
**Part 9** → `audio/vs/scene04_p9.wav` (391 ký tự) · mood `hao_hung`

```text
Quầy bếp số ba: Cá Heo. Và Cá Heo không nấu ăn. Cá Heo... chơi thể thao với đồ ăn! Ở vùng biển Phlo-ri-đa nước Mỹ, người ta quay được cảnh Cá Heo dùng chiếc đuôi quất mạnh vào con cá, khiến con cá bay vút lên không trung như một quả bóng bị sút! Con cá rơi xuống, choáng váng, và Cá Heo chỉ việc bơi tới ăn. Các nhà khoa học gọi đây là kỹ thuật "đá cá", và nó được học từ bố mẹ sang con cái.
```
**Part 10** → `audio/vs/scene04_p10.wav` (282 ký tự) · mood `hao_hung`

```text
Nhưng màn trình diễn đỉnh cao nhất của Cá Heo không phải đá cá. Mà là... làm việc cùng con người. Và nó diễn ra ở một thị trấn nhỏ của nước Bra-xin. Câu chuyện này sẽ được kể đầy đủ ở vòng sáu. Giờ thì xin mời thí sinh tiếp theo vào bếp. Thí sinh này có chiếc nồi lớn nhất cuộc thi!
```
**Part 11** → `audio/vs/scene04_p11.wav` (301 ký tự) · mood `hao_hung`

```text
Chim Bồ Nông! Và chiếc nồi chính là... cái mỏ của nó. Nhưng hôm nay, Bồ Nông không khoe cái mỏ. Nó muốn khoe một chiến thuật săn mồi bằng... cả đội. Đầu tiên, các bạn đã biết bồ nông bay theo hình chữ V. Nhưng chỉ đến năm hai ngàn lẻ một, các nhà khoa học mới đo được lợi ích thật sự của đội hình này.
```
**Part 12** → `audio/vs/scene04_p12.wav` (429 ký tự) · mood `tram_bi_an`

```text
Họ huấn luyện những con bồ nông trắng bay theo một chiếc thuyền máy và một chiếc máy bay siêu nhẹ, rồi gắn máy đo nhịp tim lên lưng chúng. Kết quả: khi bay theo đội hình, nhịp tim của bồ nông thấp hơn khoảng mười một đến mười bốn phần trăm so với khi bay một mình. Bay cùng nhau thì đỡ mệt hơn hẳn! Bí quyết là con bay sau lướt trên luồng khí bốc lên từ đầu cánh con bay trước, như người đạp xe nép sau lưng người khác để đỡ gió.
```
**Part 13** → `audio/vs/scene04_p13.wav` (162 ký tự) · mood `nghiem_trang_gia`

```text
Và con bồ nông bay đầu đàn thì sao? Nó vất vả nhất. Nhưng đừng lo, các thành viên trong đàn thường thay phiên nhau dẫn đầu. Rất công bằng, rất dân chủ. [laughter]
```
**Part 14** → `audio/vs/scene04_p14.wav` (278 ký tự) · mood `tram_bi_an`

```text
Quầy bếp tiếp theo... trống trơn. Tuyển thủ Lửng Mật đã biến mất. Và ở góc sân, có tiếng đào đất loạt soạt. Lửng Mật tên tiếng Anh là "lửng mật ong". Ai cũng nghĩ món khoái khẩu của nó là mật ong. Nhưng các nhà khoa học ở Ka-la-ha-ri đã ngồi đếm từng miếng nó ăn suốt nhiều năm.
```
**Part 15** → `audio/vs/scene04_p15.wav` (369 ký tự) · mood `nghiem_trang_gia`

```text
Và họ phát hiện ra: thứ Lửng Mật đào được nhiều nhất là chuột, thằn lằn, bọ cạp, và một món đặc biệt: những ấu trùng của một loài ong sống đơn độc dưới cát. Bốn con Lửng Mật đực đã được quan sát đào ấu trùng ong suốt hơn năm mươi tiếng, và ăn tổng cộng khoảng hai ngàn tám trăm con ấu trùng. Những con ấu trùng ấy nằm sâu tới năm mươi đến bảy mươi xăng-ti-mét dưới cát!
```
**Part 16** → `audio/vs/scene04_p16.wav` (165 ký tự) · mood `nghiem_trang_gia`

```text
Vậy còn câu chuyện nổi tiếng về loài chim dẫn mật dẫn đường cho Lửng Mật tới tổ ong, rồi hai bên chia nhau chiến lợi phẩm? Đây là lúc ban giám khảo... phải nói thật.
```
**Part 17** → `audio/vs/scene04_p17.wav` (384 ký tự) · mood `hao_hung`

```text
Năm một ngàn chín trăm chín mươi, ba nhà điểu học công bố một bài báo, viết rằng: hơn hai trăm năm nghiên cứu ở châu Phi, không có nhà khoa học nào tận mắt thấy chim dẫn mật dẫn đường cho Lửng Mật cả. Thậm chí có một bộ phim tài liệu cũ quay cảnh này, và sau này người làm phim kể lại: đó là một con lửng đã được thuần hóa, đi theo một con chim nhồi bông treo trên dây câu! [laughter]
```
**Part 18** → `audio/vs/scene04_p18.wav` (346 ký tự) · mood `tram_bi_an`

```text
Một nghiên cứu năm hai ngàn hai mươi ba đã phỏng vấn gần bốn trăm thợ săn mật ong ở chín nước châu Phi. Phần lớn họ không tin hai loài này hợp tác. Nhưng ở một vài cộng đồng ở Tan-da-ni-a, có những người kể rằng họ từng thấy. Nên kết luận cuối cùng của khoa học hiện nay là: có thể có, nhưng rất hiếm, và chưa ai quay được một bằng chứng rõ ràng.
```
**Part 19** → `audio/vs/scene04_p19.wav` (130 ký tự) · 🎭 cameo `tham_phan`

```text
Giám khảo kết luận: Lửng Mật được điểm cao vì đào giỏi, nhưng bị trừ điểm vì... nổi tiếng nhờ một câu chuyện chưa được kiểm chứng!
```
**Part 20** → `audio/vs/scene04_p20.wav` (280 ký tự) · mood `hao_hung`

```text
Kết quả vòng ba! Huy chương đồng: Rái Cá Biển, đầu bếp có hòn đá bảo vệ hàm răng! Huy chương bạc: Chim Bồ Nông, đội bay tiết kiệm sức nhất bầu trời! Và huy chương vàng vòng ba: Thú Mỏ Vịt! Ăn khỏe nhất cuộc thi, và có dòng sữa có thể giúp con người chống lại vi khuẩn kháng thuốc!
```
**Part 21** → `audio/vs/scene04_p21.wav` (176 ký tự) · mood `hao_hung`

```text
Bảng điểm sau ba vòng: Thú Mỏ Vịt vươn lên dẫn đầu với sáu điểm! Chồn Gu-lô bốn điểm. Chim Cánh Cụt ba điểm. Chim Bồ Nông hai điểm. Cô-a-la, Tôm Tít và Rái Cá mỗi bạn một điểm.
```
**Part 22** → `audio/vs/scene04_p22.wav` (102 ký tự) · mood `tram_bi_an`

```text
Còn Lửng Mật, ứng cử viên nặng ký nhất trước giải, vẫn chưa có điểm nào. Và Cá Heo, Gấu Nước cũng vậy.
```
**Part 23** → `audio/vs/scene04_p23.wav` (142 ký tự) · mood `hao_hung`

```text
Nhưng đừng vội loại họ. Đại hội mới đi được ba trên tám chặng đường. Và vòng bốn sẽ thử thách thứ mà cơ bắp không thể thay thế: các giác quan!
```

### scene05 — CĂNG TIN ĐẠI HỘI — MỖI TUYỂN THỦ UỐNG NƯỚC VÀ CHỌN MÓN THẾ NÀO
*Thẻ chương:* ĂN GÌ, UỐNG GÌ GIỮA HIỆP?

*Badge:* `GIỜ GIẢI LAO` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene05_p0.wav` (181 ký tự) · mood `hao_hung`

```text
Giờ giải lao! Sau ba vòng thi căng thẳng, các tuyển thủ được mời vào căng tin của đại hội. Và ngay tại đây, chúng ta phát hiện ra mỗi người có một kiểu ăn uống... không ai giống ai.
```
**Part 1** → `audio/vs/scene05_p1.wav` (309 ký tự) · mood `hao_hung`

```text
Cô-a-la đến quầy lá khuynh diệp đầu tiên. Nhưng thay vì ăn ngay, nó làm một việc rất lạ: cúi xuống... ngửi từng chiếc lá. Các nhà khoa học ở Nhật Bản đã quan sát mười chú Cô-a-la trong vườn thú và thấy rằng chúng ngửi lá nhiều hơn hẳn trước khi ăn. Và mùi hương của lá có thể dự đoán chú Cô-a-la sẽ ăn lá nào.
```
**Part 2** → `audio/vs/scene05_p2.wav` (372 ký tự) · mood `nghiem_trang_gia`

```text
Vì sao phải ngửi kỹ như vậy? Vì có những cây khuynh diệp chứa nhiều một nhóm chất gây buồn nôn. Ăn phải, Cô-a-la sẽ thấy khó chịu, và từ đó nó học cách nhận ra mùi của chiếc lá "có vấn đề". Một nghiên cứu theo dõi suốt mười năm trên đảo Phi-líp ở Úc còn cho thấy: Cô-a-la thích leo những cây to, nhưng tránh những cây có lá chứa nhiều chất gây buồn nôn, hoặc lá nghèo đạm.
```
**Part 3** → `audio/vs/scene05_p3.wav` (170 ký tự) · mood `hao_hung`

```text
Có nhà khoa học còn ví von: chọn cây để ăn đối với Cô-a-la giống như phải chọn một trong một ngàn nhà hàng khắp thành phố... mà không có ứng dụng đánh giá nào! [laughter]
```
**Part 4** → `audio/vs/scene05_p4.wav` (486 ký tự) · mood `hao_hung`

```text
Cá Heo đến quầy nước. Và lúc này, một câu hỏi được đặt ra: sống giữa biển nước mặn mênh mông, Cá Heo uống nước gì? Câu trả lời là: gần như không uống. Cá Heo lấy nước chủ yếu từ chính thức ăn, vì con cá và con mực chứa rất nhiều nước, và từ nước mà cơ thể tự tạo ra khi đốt cháy mỡ. Một nghiên cứu năm hai ngàn hai mươi ba dùng phương pháp đo đồng vị ô-xy trong máu cá heo đã tính ra: nước từ thức ăn và nước tự tạo trong cơ thể chiếm hơn chín mươi phần trăm lượng nước cá heo nhận vào.
```
**Part 5** → `audio/vs/scene05_p5.wav` (110 ký tự) · mood `hao_hung`

```text
Sống giữa đại dương mà không uống nước biển. Giống như người sống trên đảo mà chỉ uống... nước dừa! [laughter]
```
**Part 6** → `audio/vs/scene05_p6.wav` (333 ký tự) · mood `hao_hung`

```text
Chim Cánh Cụt thì ngược lại. Cánh Cụt nuốt nước biển mỗi lần ăn tôm, ăn cá. Nhưng nó có một bộ lọc muối riêng: một tuyến lọc nằm ngay phía trên mắt. Tuyến này lọc muối thừa ra khỏi máu, tạo thành một dung dịch nước muối đậm đặc chảy xuống mỏ. Rồi Cánh Cụt chỉ việc... hắt xì một cái, hoặc lắc đầu thật mạnh để vẩy muối ra! [laughter]
```
**Part 7** → `audio/vs/scene05_p7.wav` (180 ký tự) · mood `nghiem_trang_gia`

```text
Và chúng không uống nước biển bừa bãi. Những lúc có thể, cánh cụt vẫn thích uống nước tuyết tan, hoặc ăn tuyết cho đỡ khát. Có máy lọc trong người, nhưng vẫn thích nước tinh khiết!
```
**Part 8** → `audio/vs/scene05_p8.wav` (326 ký tự) · mood `hao_hung`

```text
Gấu Nước đến quầy... nhưng quầy nào cũng quá to. Ban tổ chức phải dùng kính hiển vi mới phục vụ được cậu ấy. Phần lớn các loài gấu nước ăn thực vật: rêu, tảo. Trong miệng chúng có một cặp kim nhọn cực nhỏ. Chúng dùng kim chọc thủng thành tế bào của cây rêu, rồi hút lấy dịch bên trong như uống... trà sữa trân châu! [laughter]
```
**Part 9** → `audio/vs/scene05_p9.wav` (151 ký tự) · mood `nghiem_trang_gia`

```text
Nhưng không phải gấu nước nào cũng ăn chay. Có những loài gấu nước ăn thịt, săn những sinh vật tí hon khác, và có loài còn ăn thịt... cả gấu nước khác!
```
**Part 10** → `audio/vs/scene05_p10.wav` (316 ký tự) · mood `hao_hung`

```text
Thú Mỏ Vịt, người đã có hai huy chương vàng, đến quầy cuối cùng. Và nó gọi... cả quầy! Vì như vòng ba đã kể, Thú Mỏ Vịt ăn khỏe không ai bằng. Để ăn được nhiều như vậy, Thú Mỏ Vịt dành khoảng mười đến mười hai tiếng mỗi ngày để lặn tìm mồi dưới đáy suối. Và mùa đông nước càng lạnh, nó càng phải kiếm ăn lâu hơn nữa.
```
**Part 11** → `audio/vs/scene05_p11.wav` (127 ký tự) · mood `hao_hung`

```text
Lửng Mật thì không đến quầy nào cả. Ban tổ chức tìm thấy Lửng Mật đang... đào tung sàn căng tin để tìm ấu trùng ong! [laughter]
```
**Part 12** → `audio/vs/scene05_p12.wav` (106 ký tự) · 🎭 cameo `tham_phan`

```text
Giám khảo xin nhắc tuyển thủ Lửng Mật: căng tin không phải là sa mạc Ka-la-ha-ri! Đề nghị lấp hố lại ngay!
```
**Part 13** → `audio/vs/scene05_p13.wav` (101 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Cháu ăn no rồi ạ! Nhưng mà cháu vẫn muốn ngửi thêm vài chiếc lá nữa, nhỡ đâu có chiếc nào thơm hơn...
```
**Part 14** → `audio/vs/scene05_p14.wav` (140 ký tự) · mood `hao_hung`

```text
Hết giờ giải lao! Ăn no, uống đủ, ngửi kỹ, hắt xì xong. Và giờ, các tuyển thủ quay lại sân cho vòng bốn: vòng của những giác quan siêu phàm!
```

### scene06 — GIÁC QUAN SIÊU PHÀM — AI NHÌN, NGHE, SỜ GIỎI NHẤT
*Thẻ chương:* MẮT THẦN, TAI THÍNH, TAY NHẠY

*Badge:* `VÒNG 4` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene06_p0.wav` (266 ký tự) · mood `hao_hung`

```text
Vòng bốn: giác quan siêu phàm! Trong thế giới hoang dã, ai phát hiện ra đồ ăn trước, và phát hiện ra kẻ thù trước, người đó sống sót. Ban giám khảo sẽ thử thách các tuyển thủ bằng những bài kiểm tra giác quan mà chính các nhà khoa học đã làm. Mời tuyển thủ đầu tiên!
```
**Part 1** → `audio/vs/scene06_p1.wav` (382 ký tự) · mood `hao_hung`

```text
Rái Cá Biển bước tới. Và Rái Cá được thử thách đúng thứ mà nó giỏi nhất: không phải nhìn, mà là... sờ. Ở bang Ca-li-phoóc-ni-a, các nhà khoa học huấn luyện một cô rái cá tên Xen-ca chạm tay vào những tấm bảng có rãnh, rồi chọn đúng tấm có rãnh rộng hai mi-li-mét. Kết quả: Xen-ca phân biệt được những rãnh chỉ chênh nhau khoảng ba phần mười mi-li-mét. Mỏng hơn cả... một sợi tóc to!
```
**Part 2** → `audio/vs/scene06_p2.wav` (156 ký tự) · mood `don_dap`

```text
Và Xen-ca quyết định cực nhanh! Chỉ khoảng hai phần mười giây cho mỗi lần chạm tay! Nhanh hơn những người tình nguyện làm cùng bài kiểm tra gần ba mươi lần!
```
**Part 3** → `audio/vs/scene06_p3.wav` (173 ký tự) · mood `tram_bi_an`

```text
Vì sao Rái Cá cần đôi tay nhanh như thế? Vì mỗi lần lặn chỉ kéo dài một hai phút, dưới đáy biển tối và đục. Nó phải sờ, chọn, và nhét đồ ăn vào túi dưới nách trong chớp mắt.
```
**Part 4** → `audio/vs/scene06_p4.wav` (94 ký tự) · 🎭 cameo `tham_phan`

```text
Giám khảo xin ghi nhận: đôi bàn tay của Rái Cá nhạy chẳng kém bàn tay người, mà nhanh gấp bội.
```
**Part 5** → `audio/vs/scene06_p5.wav` (289 ký tự) · mood `hao_hung`

```text
Tuyển thủ tiếp theo: Chim Cánh Cụt. Và thử thách của Cánh Cụt là... nhìn rõ ở cả hai thế giới. Trên cạn, và dưới nước. Bạn đã bao giờ mở mắt dưới nước chưa? Mọi thứ nhòe nhoẹt. Vì giác mạc của mắt người cong, nó chỉ hội tụ ánh sáng tốt trong không khí. Xuống nước, nó gần như mất tác dụng.
```
**Part 6** → `audio/vs/scene06_p6.wav` (370 ký tự) · mood `nghiem_trang_gia`

```text
Chim cánh cụt giải bài toán này bằng một mẹo khác: giác mạc của chúng phẳng hơn mắt người rất nhiều. Phần việc hội tụ được giao gần hết cho thủy tinh thể, một chiếc thấu kính mềm có thể bóp phồng lên khi cần. Nhờ vậy, Chim Cánh Cụt nhìn rõ trên băng để tìm đường về tổ, và nhìn rõ dưới nước để bắt cá. Như một chiếc máy ảnh tự động đổi ống kính khi lặn xuống! [laughter]
```
**Part 7** → `audio/vs/scene06_p7.wav` (360 ký tự) · mood `hao_hung`

```text
Tuyển thủ tiếp theo, Cô-a-la, bước lên với một bài thi... âm nhạc. Như các bạn đã biết, Cô-a-la đực có giọng rống trầm như quái vật. Nhưng giọng rống ấy còn chứa một bí mật. Năm hai ngàn mười một, các nhà khoa học thu âm tiếng rống của hai mươi chú Cô-a-la đực và phân tích bằng máy tính. Họ phát hiện mỗi chú có một chất giọng riêng, như dấu vân tay âm thanh.
```
**Part 8** → `audio/vs/scene06_p8.wav` (337 ký tự) · mood `nghiem_trang_gia`

```text
Và quan trọng hơn: chính những chú Cô-a-la khác cũng nhận ra sự khác nhau ấy. Khi nghe một giọng lạ, chúng lập tức quay đầu nhìn về phía loa lâu hơn hẳn. Các nghiên cứu sau đó còn cho thấy: giọng rống của con đực tiết lộ kích thước cơ thể. Giọng càng trầm, con đực càng to. Và các cô Cô-a-la cái... thích những giọng trầm hơn! [laughter]
```
**Part 9** → `audio/vs/scene06_p9.wav` (51 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Cháu biết rồi, cháu sẽ hát trầm hơn ạ! Ừm... ọ ọ ọ!
```
**Part 10** → `audio/vs/scene06_p10.wav` (354 ký tự) · mood `hao_hung`

```text
Tuyển thủ tiếp theo, Cá Heo, mang đến một bài thi về... sự tỉnh táo. Năm hai ngàn mười hai, các nhà khoa học ở Mỹ thử xem cá heo có thể canh gác liên tục được bao lâu. Nhiệm vụ: liên tục dùng tiếng định vị để quét quanh hồ, khi nào phát hiện mục tiêu giả do máy phát ra thì bấm nút báo. Mục tiêu xuất hiện bất ngờ, ở bất kỳ hướng nào, vào bất kỳ lúc nào.
```
**Part 11** → `audio/vs/scene06_p11.wav` (150 ký tự) · mood `don_dap`

```text
Một chú cá heo cái đã làm nhiệm vụ này suốt mười lăm ngày liền. Ngày lẫn đêm! Không nghỉ! Và độ chính xác gần như tuyệt đối từ ngày đầu đến ngày cuối!
```
**Part 12** → `audio/vs/scene06_p12.wav` (268 ký tự) · mood `nghiem_trang_gia`

```text
Và cuộc thử nghiệm chỉ dừng lại vì... một cơn bão mùa đông kéo đến. Không phải vì cá heo mệt! [laughter] Khán giả của kênh đã biết cá heo ngủ luân phiên từng nửa bộ não. Nhưng phải đến thí nghiệm này, người ta mới thấy cách ngủ ấy cho phép nó canh gác lâu đến mức nào.
```
**Part 13** → `audio/vs/scene06_p13.wav` (305 ký tự) · mood `hao_hung`

```text
Nhưng Chim Cánh Cụt không chịu thua ở môn ngủ! Năm hai ngàn hai mươi ba, các nhà khoa học gắn máy đo sóng não lên những chú chim cánh cụt quai mũ đang ấp trứng ở Nam Cực, họ hàng gần của A-đê-li. Và họ phát hiện: những chú chim này ngủ gật hơn mười ngàn lần mỗi ngày! Mỗi giấc chỉ kéo dài khoảng bốn giây!
```
**Part 14** → `audio/vs/scene06_p14.wav` (171 ký tự) · mood `hao_hung`

```text
Cộng tất cả những giấc ngủ bốn giây ấy lại, chúng ngủ được hơn mười một tiếng mỗi ngày. Mà vẫn kịp canh trứng trước những con chim cướp biển lượn ngay trên đầu! [laughter]
```
**Part 15** → `audio/vs/scene06_p15.wav` (168 ký tự) · 🎭 cameo `tham_phan`

```text
Giám khảo xin tổng kết vòng bốn: đôi tay nhạy, đôi mắt hai thế giới, giọng hát mang tên riêng, và người lính gác không bao giờ ngủ trọn giấc. Một vòng thi rất khó chấm!
```
**Part 16** → `audio/vs/scene06_p16.wav` (245 ký tự) · mood `hao_hung`

```text
Kết quả vòng bốn! Huy chương đồng: Chim Cánh Cụt, đôi mắt hai thế giới và giấc ngủ bốn giây! Huy chương bạc: Rái Cá Biển, bàn tay nhạy và nhanh gấp ba mươi lần người! Và huy chương vàng... Thuộc về Cá Heo, người lính gác mười lăm ngày không ngủ!
```
**Part 17** → `audio/vs/scene06_p17.wav` (224 ký tự) · mood `hao_hung`

```text
Bảng điểm sau bốn vòng: Thú Mỏ Vịt vẫn dẫn đầu với sáu điểm! Chồn Gu-lô bốn điểm. Chim Cánh Cụt bốn điểm. Rái Cá ba điểm. Cá Heo ba điểm. Bồ Nông hai điểm. Cô-a-la và Tôm Tít một điểm. Lửng Mật và Gấu Nước: vẫn chưa có điểm!
```
**Part 18** → `audio/vs/scene06_p18.wav` (144 ký tự) · mood `tram_bi_an`

```text
Vòng tiếp theo sẽ không chấm khả năng tìm đồ ăn. Mà chấm khả năng chăm sóc một sinh mạng nhỏ bé. Vòng năm: những người cha, người mẹ phi thường.
```

### scene07 — ĐÊM TRƯỚC VÒNG QUYẾT ĐỊNH — AI NGỦ, AI THỨC, AI TẬP LUYỆN
*Thẻ chương:* ĐÊM KHÔNG NGỦ Ở ĐẠI HỘI

*Badge:* `HẬU TRƯỜNG` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene07_p0.wav` (241 ký tự) · mood `tram_bi_an`

```text
Đêm buông xuống sân vận động. Đại hội tạm nghỉ trước bốn vòng cuối. Các tuyển thủ trở về khu nghỉ ngơi. Nhưng không phải ai cũng ngủ... Máy quay hậu trường của chúng tôi đi một vòng khu nghỉ ngơi. Và những gì nó ghi lại được... rất đáng xem.
```
**Part 1** → `audio/vs/scene07_p1.wav` (69 ký tự) · mood `hao_hung`

```text
Phòng số một: Chồn Gu-lô. Không ngủ. Đang... leo núi. Ngay trong đêm.
```
**Part 2** → `audio/vs/scene07_p2.wav` (0 ký tự) · mood `don_dap`

```text

```
**Part 3** → `audio/vs/scene07_p3.wav` (303 ký tự) · mood `nghiem_trang_gia`

```text
Ở công viên quốc gia Glây-xi-ơ nước Mỹ, các nhà nghiên cứu theo dõi bằng vòng cổ định vị nhận xét: Chồn Gu-lô có thể đi một trăm năm mươi đến hai trăm cây số mỗi tuần trong công viên. Và chúng rất ít khi đi đường vòng. Gặp núi thì leo, gặp đường thì băng qua. Đúng là đi đâu cũng... đi thẳng! [laughter]
```
**Part 4** → `audio/vs/scene07_p4.wav` (159 ký tự) · mood `tram_bi_an`

```text
Phòng số hai: Thú Mỏ Vịt. Đèn tắt. Tuyển thủ đang dẫn đầu bảng điểm đang ngủ say. Nhưng hãy nhìn kỹ... cái mỏ đang giật giật, và mắt đang đảo liên tục dưới mí.
```
**Part 5** → `audio/vs/scene07_p5.wav` (369 ký tự) · mood `hao_hung`

```text
Đó là giai đoạn ngủ mơ, giai đoạn mà ở người, chúng ta thường nằm mơ. Và Thú Mỏ Vịt giữ kỷ lục: hơn tám tiếng ngủ mơ mỗi ngày, nhiều hơn bất kỳ loài động vật nào từng được đo. Các nhà khoa học đoán rằng giấc ngủ mơ có thể đã xuất hiện từ rất sớm ở những loài thú đầu tiên, và Thú Mỏ Vịt, thuộc nhóm thú đẻ trứng đã tách ra từ rất xa xưa, có thể đang giữ lại dấu vết đó.
```
**Part 6** → `audio/vs/scene07_p6.wav` (289 ký tự) · mood `tram_bi_an`

```text
Phòng số ba: Chim Cánh Cụt. Mắt nhắm. Mở. Nhắm. Mở. Nó không ngủ một giấc dài. Nó ngủ... hàng ngàn giấc ngắn. Như vòng bốn đã kể, họ hàng của nó, chim cánh cụt quai mũ, có thể ngủ hơn mười ngàn giấc mỗi ngày, mỗi giấc khoảng bốn giây. Ngủ kiểu ấy để làm gì? Để không bao giờ lơ là canh tổ.
```
**Part 7** → `audio/vs/scene07_p7.wav` (335 ký tự) · mood `hao_hung`

```text
Phòng số bốn: Rái Cá Biển. Phòng này... có bể nước. Và Rái Cá đang nằm ngửa trên mặt nước, hai bàn tay úp lên mắt, ngủ ngon lành. Các nhà khoa học cho biết, mỗi ngày Rái Cá Biển dành khoảng mười một tiếng để nghỉ ngơi và ngủ, khoảng tám tiếng để kiếm ăn, và năm tiếng để chải lông và vui chơi. Một lịch trình... đáng mơ ước! [laughter]
```
**Part 8** → `audio/vs/scene07_p8.wav` (347 ký tự) · mood `hao_hung`

```text
Phòng số năm: Gấu Nước. Máy quay soi qua kính hiển vi... và thấy Gấu Nước đang tập thể dục! Nó đi tới đi lui trên tấm thảm thạch rau câu. Năm hai ngàn hai mươi mốt, các nhà khoa học đã quay phim gấu nước đi bộ trên những tấm thạch, và phát hiện ra một điều bất ngờ: gấu nước đi giống hệt... côn trùng! Dù côn trùng to gấp khoảng năm trăm ngàn lần.
```
**Part 9** → `audio/vs/scene07_p9.wav` (211 ký tự) · mood `nghiem_trang_gia`

```text
Lúc đi dạo, gấu nước đi khoảng nửa thân mình mỗi giây. Khi gấp gáp, nó có thể tăng tốc lên khoảng hai thân mình mỗi giây. Nghe thì chậm, nhưng với một sinh vật nhỏ hơn hạt cát, đó là... chạy nước rút! [laughter]
```
**Part 10** → `audio/vs/scene07_p10.wav` (136 ký tự) · mood `tram_bi_an`

```text
Phòng số sáu, phòng cuối cùng: Lửng Mật. Cửa phòng mở. Giường trống. Trên tường có một cái lỗ to. Lửng Mật... đã vượt ngục. Một lần nữa.
```
**Part 11** → `audio/vs/scene07_p11.wav` (150 ký tự) · mood `hao_hung`

```text
Máy quay chạy theo dấu chân và tìm thấy Lửng Mật đang ngồi ngoài sân, dưới ánh trăng, bên cạnh... chú lửng con của mình. Hai mẹ con đang tập đào hang.
```
**Part 12** → `audio/vs/scene07_p12.wav` (153 ký tự) · mood `am_ap`

```text
Hóa ra gã giang hồ nổi tiếng nhất đại hội, đêm nay không đi gây sự. Nó chỉ dành thời gian dạy con. Mai là vòng thi về cha mẹ. Và Lửng Mật... đã sẵn sàng.
```
**Part 13** → `audio/vs/scene07_p13.wav` (189 ký tự) · mood `hao_hung`

```text
Máy quay hậu trường xin phép tắt đèn đỏ, rút êm khỏi khu nghỉ ngơi. Vì nếu Lửng Mật phát hiện ra mình bị quay lén... thì người tiếp theo phải đào hầm trốn chính là đội quay phim! [laughter]
```
**Part 14** → `audio/vs/scene07_p14.wav` (79 ký tự) · mood `tram_bi_an`

```text
Trời sáng dần. Mặt trời mọc trên sân vận động. Và còn đúng... bốn vòng thi nữa.
```

### scene08 — CHA MẸ PHI THƯỜNG — AI NUÔI CON GIỎI NHẤT HOANG DÃ
*Thẻ chương:* NUÔI CON KIỂU HOANG DÃ

*Badge:* `VÒNG 5` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene08_p0.wav` (235 ký tự) · mood `am_ap`

```text
Vòng năm: cha mẹ phi thường! Sống sót một mình đã khó. Vừa sống sót, vừa nuôi một đứa con bé bỏng, còn khó hơn gấp bội. Giám khảo sẽ chấm: ai chăm con chu đáo nhất, ai dạy con kiên nhẫn nhất, và ai có chiêu nuôi con... độc nhất vô nhị.
```
**Part 1** → `audio/vs/scene08_p1.wav` (319 ký tự) · mood `hao_hung`

```text
Mở màn là Lửng Mật, tuyển thủ vẫn đang trắng điểm sau bốn vòng. Và Lửng Mật mẹ khiến cả khán đài bất ngờ: gã giang hồ dữ dằn ấy hóa ra là một bà mẹ... vô cùng cẩn thận. Ở sa mạc Ka-la-ha-ri, Lửng Mật mẹ thường chỉ nuôi một con mỗi lứa. Lửng con mới sinh không có lông, mắt nhắm nghiền, và phải hai tháng sau mới mở mắt.
```
**Part 2** → `audio/vs/scene08_p2.wav` (188 ký tự) · mood `am_ap`

```text
Và để giữ an toàn cho con, cứ vài ngày Lửng Mật mẹ lại ngậm con trong miệng, mang sang một cái hang mới. Trung bình chỉ ở mỗi hang khoảng ba ngày, hang này cách hang kia khoảng hai cây số!
```
**Part 3** → `audio/vs/scene08_p3.wav` (176 ký tự) · mood `am_ap`

```text
Lửng con ở với mẹ ít nhất mười bốn tháng. Suốt thời gian ấy, mẹ dạy con đào hang, leo cây, bắt chuột, và cả cách đối phó với rắn độc. Một khóa học sinh tồn kéo dài hơn một năm!
```
**Part 4** → `audio/vs/scene08_p4.wav` (82 ký tự) · 🎭 cameo `tham_phan`

```text
Giám khảo xin ghi nhận: bà mẹ chuyển nhà nhiều nhất, và dạy con lâu nhất cuộc thi.
```
**Part 5** → `audio/vs/scene08_p5.wav` (301 ký tự) · mood `hao_hung`

```text
Tuyển thủ tiếp theo, Thú Mỏ Vịt mẹ, trình bày cách làm tổ đẻ trứng. Đúng vậy, một loài thú có sữa... mà lại đẻ trứng! Trước khi đẻ, Thú Mỏ Vịt mẹ đào một đường hầm dài dọc bờ sông, có khi tới hai mươi mét. Rồi tha lá ướt và cành nhỏ vào trải ổ, bằng cách... kẹp chúng giữa đuôi và chân sau! [laughter]
```
**Part 6** → `audio/vs/scene08_p6.wav` (161 ký tự) · mood `nghiem_trang_gia`

```text
Và mỗi lần ra khỏi hang, mẹ lại đắp đất bịt kín đường hầm thành nhiều lớp, có khi tới chín lớp. Để ngăn kẻ thù, và để giữ cho ổ không bị ngập khi nước sông dâng.
```
**Part 7** → `audio/vs/scene08_p7.wav` (182 ký tự) · mood `am_ap`

```text
Thú Mỏ Vịt mẹ đẻ từ một đến ba trứng, thường là hai. Rồi mẹ cuộn tròn người, ôm trứng giữa bụng và đuôi suốt khoảng mười ngày để ấp, cho đến khi những chú con bé như hạt đậu chui ra.
```
**Part 8** → `audio/vs/scene08_p8.wav` (360 ký tự) · mood `hao_hung`

```text
Tuyển thủ tiếp theo, Rái Cá Biển mẹ, bước lên với một chú con nằm trên ngực. Rái cá con mới sinh có bộ lông xù đến mức... không thể lặn xuống nước được. Nó nổi bồng bềnh như cái phao! Nên khi mẹ phải lặn xuống đáy biển kiếm ăn, mẹ để con nổi trên mặt nước, có khi còn quấn con vào tảo bẹ cho khỏi trôi. Rồi mẹ ngoi lên, lại đặt con lên ngực, chải lông, cho bú.
```
**Part 9** → `audio/vs/scene08_p9.wav` (199 ký tự) · mood `am_ap`

```text
Rái cá con phụ thuộc vào mẹ khoảng sáu đến tám tháng. Mẹ dạy con lặn, dạy con chọn món ăn, và quan trọng nhất: dạy con dùng hòn đá đập vỏ. Rái cá con thường thích ăn những món giống hệt món mẹ thích!
```
**Part 10** → `audio/vs/scene08_p10.wav` (325 ký tự) · mood `hao_hung`

```text
Tuyển thủ tiếp theo, Cá Heo mẹ, trình bày một thứ mà các nhà khoa học mới phát hiện năm hai ngàn hai mươi ba: cá heo mẹ cũng nói giọng... nựng con! Các nhà khoa học ở bang Phlo-ri-đa đã ghi âm mười chín cá heo mẹ, khi có con bên cạnh, và khi không có con. Và tất cả các cá heo mẹ đều thay đổi tiếng huýt sáo khi có con ở gần.
```
**Part 11** → `audio/vs/scene08_p11.wav` (215 ký tự) · mood `am_ap`

```text
Tiếng huýt sáo cao hơn, và rộng giọng hơn. Giống hệt cách các bà mẹ con người tự nhiên nói giọng cao, ngân nga khi nựng em bé. Hai loài khác nhau, sống ở hai thế giới khác nhau, mà lại có chung một cách nói với con.
```
**Part 12** → `audio/vs/scene08_p12.wav` (433 ký tự) · mood `hao_hung`

```text
Và cuối cùng, Chồn Gu-lô mẹ. Như vòng một đã kể, chồn mẹ đào hang dưới lớp tuyết dày để sinh con. Nhưng chồn mẹ còn một chiêu nữa: khi cần, chồn mẹ dời con sang hang khác, có khi dùng nhiều hang khác nhau trước khi con cai sữa. Chồn con được nuôi trong hang đến khoảng chín, mười tuần tuổi, rồi mới bắt đầu theo mẹ ra ngoài. Và ở Bắc Mỹ, các nhà khoa học còn thấy chồn bố thỉnh thoảng quay lại thăm con, dẫn con đi khám phá lãnh thổ.
```
**Part 13** → `audio/vs/scene08_p13.wav` (204 ký tự) · mood `hao_hung`

```text
Tuyển thủ tiếp theo, Chim Cánh Cụt, trình bày một hệ thống chăm con kiểu... đổi ca trực. Chim Cánh Cụt A-đê-li thường đẻ hai trứng, và bố mẹ thay phiên nhau ấp, mỗi ca thường kéo dài khoảng mười hai ngày.
```
**Part 14** → `audio/vs/scene08_p14.wav` (179 ký tự) · mood `nghiem_trang_gia`

```text
Nhưng ca đầu tiên là ca khổ nhất. Chim bố ở lại ấp trong khi chim mẹ ra biển kiếm ăn. Tính cả mùa tán tỉnh trước đó, chim bố có thể nhịn đói khoảng một tháng liền mà không rời tổ.
```
**Part 15** → `audio/vs/scene08_p15.wav` (241 ký tự) · mood `am_ap`

```text
Khi chim con được khoảng ba tuần tuổi, chúng đã đủ lớn để không cần bố mẹ ủ ấm. Chúng tụ tập thành những nhóm đông gọi là "nhà trẻ", đứng sát vào nhau để giữ ấm và chống lại chim săn mồi. Còn bố mẹ thì cùng nhau ra biển, kiếm cá về nuôi con.
```
**Part 16** → `audio/vs/scene08_p16.wav` (428 ký tự) · mood `hao_hung`

```text
Và một bất ngờ đến từ Tôm Tít! Gã võ sĩ đại dương có một người họ hàng nhỏ xíu, loài tôm tít Pu-lô-xơ-qui-la, sống ở Ấn Độ Dương và Thái Bình Dương. Và loài này... nuôi con bằng cả bố lẫn mẹ! Cả bố và mẹ đều quạt nước cho trứng để trứng có đủ ô-xy, nhặt bỏ trứng hỏng, và di chuyển ổ trứng trong hang. Khi thức ăn dồi dào, tôm mẹ có thể đẻ thêm ổ thứ hai khi ổ thứ nhất chưa nở. Và lúc ấy, cả hai vợ chồng cùng chăm hai ổ trứng!
```
**Part 17** → `audio/vs/scene08_p17.wav` (189 ký tự) · mood `nghiem_trang_gia`

```text
Theo các nhà khoa học, trong số các loài giáp xác sống ở biển, đây là nhóm duy nhất từng được nghiên cứu kỹ về việc cả bố lẫn mẹ cùng chăm trứng. Võ sĩ ngoài đời, ông bố mẫu mực trong hang!
```
**Part 18** → `audio/vs/scene08_p18.wav` (119 ký tự) · mood `hao_hung`

```text
Ban giám khảo xin phép nghỉ giải lao một chút... để lau nước mắt. Đây là vòng thi xúc động nhất từ đầu đại hội đến giờ!
```
**Part 19** → `audio/vs/scene08_p19.wav` (250 ký tự) · mood `hao_hung`

```text
Kết quả vòng năm! Huy chương đồng: Cá Heo mẹ, giọng nựng con của đại dương! Huy chương bạc: Thú Mỏ Vịt mẹ, kỹ sư đường hầm chín lớp cửa! Và huy chương vàng... Thuộc về Lửng Mật! Bà mẹ ngậm con chuyển nhà mỗi ba ngày, và dạy con suốt hơn một năm trời!
```
**Part 20** → `audio/vs/scene08_p20.wav` (242 ký tự) · mood `hao_hung`

```text
Lửng Mật cuối cùng cũng có điểm! Bảng điểm sau năm vòng: Thú Mỏ Vịt tám điểm! Cá Heo bốn điểm, Chồn Gu-lô bốn điểm, Chim Cánh Cụt bốn điểm! Lửng Mật ba điểm. Rái Cá ba điểm. Bồ Nông hai điểm. Cô-a-la, Tôm Tít một điểm. Gấu Nước vẫn trắng tay.
```
**Part 21** → `audio/vs/scene08_p21.wav` (170 ký tự) · mood `tram_bi_an`

```text
Gấu Nước ngước nhìn bảng điểm, và lần đầu tiên, sinh vật bất tử ấy có vẻ... lo lắng. Vì vòng sáu sẽ không cần đến những siêu năng lực chịu đựng. Vòng sáu cần sự đoàn kết.
```

### scene09 — SỨC MẠNH ĐỒNG ĐỘI — AI BIẾT HỢP TÁC, AI NHỚ BẠN LÂU NHẤT
*Thẻ chương:* MỘT CÂY LÀM CHẲNG NÊN NON

*Badge:* `VÒNG 6` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene09_p0.wav` (236 ký tự) · mood `hao_hung`

```text
Vòng sáu: sức mạnh đồng đội! Một cây làm chẳng nên non, ba cây chụm lại... thì thành một đàn cá heo! [laughter] Giám khảo chấm ba tiêu chí: biết làm việc với đồng loại, biết hợp tác với loài khác, và quan trọng nhất: biết... nhớ bạn bè.
```
**Part 1** → `audio/vs/scene09_p1.wav` (339 ký tự) · mood `hao_hung`

```text
Cá Heo bước vào sân, và lần này, giám khảo đồng ý cho Cá Heo kể trọn câu chuyện còn dang dở ở vòng ba. Câu chuyện ở thị trấn La-gu-na, miền Nam nước Bra-xin. Ở đây, mỗi mùa cá đối di cư, những người đánh cá đứng thành hàng dưới nước, nước ngập ngang hông, tay cầm sẵn chiếc lưới quăng tròn. Nhưng họ không nhìn mặt nước. Họ nhìn... cá heo.
```
**Part 2** → `audio/vs/scene09_p2.wav` (275 ký tự) · mood `don_dap`

```text
Cá Heo dồn đàn cá đối vào sát bờ. Rồi bất ngờ, nó lặn sâu xuống thật nhanh, hoặc quẫy đầu, quẫy đuôi ngay trước mặt người đánh cá. Đó là tín hiệu! Người đánh cá lập tức quăng lưới! Lưới chụp xuống, cá đối hoảng loạn tán loạn, và Cá Heo lao vào bắt những con cá chạy khỏi đàn.
```
**Part 3** → `audio/vs/scene09_p3.wav` (514 ký tự) · mood `nghiem_trang_gia`

```text
Năm hai ngàn hai mươi ba, các nhà khoa học dùng máy bay không người lái, thiết bị định vị đeo tay và cả micro dưới nước để đo đạc sự hợp tác này. Và các con số khiến họ kinh ngạc. Khi có Cá Heo ra tín hiệu, người đánh cá có khả năng bắt được cá cao gấp mười bảy lần, và bắt được số cá nhiều gần gấp bốn lần so với khi không có Cá Heo! Và Cá Heo cũng được lợi: những con cá heo tham gia hợp tác có tỷ lệ sống sót cao hơn khoảng mười ba phần trăm, vì chúng ít phải đi kiếm ăn ở những vùng có lưới đánh bắt nguy hiểm.
```
**Part 4** → `audio/vs/scene09_p4.wav` (180 ký tự) · mood `am_ap`

```text
Điều kỳ diệu là sự hợp tác này đã diễn ra ở đây hơn một trăm năm, truyền từ đời ông sang đời cháu của cả người lẫn cá heo. Người dân còn đặt tên riêng cho từng chú cá heo quen mặt.
```
**Part 5** → `audio/vs/scene09_p5.wav` (244 ký tự) · mood `bi_hai`

```text
[sigh] Nhưng các nhà khoa học cũng cảnh báo: cá đối đang ít dần, và số lần hợp tác cũng ít dần. Đây là một trong những mối hợp tác hiếm hoi còn sót lại giữa con người và động vật hoang dã. Nếu cá biến mất, tình bạn ấy cũng có thể biến mất theo.
```
**Part 6** → `audio/vs/scene09_p6.wav` (330 ký tự) · mood `am_ap`

```text
Nhưng Cá Heo còn một tuyệt chiêu đồng đội nữa: trí nhớ. Mỗi chú cá heo có một tiếng huýt sáo riêng, hoạt động giống như... một cái tên. Năm hai ngàn mười ba, một nhà khoa học đã thu âm tiếng huýt sáo của năm mươi ba chú cá heo ở sáu thủy cung, rồi phát lại cho những chú cá heo từng sống chung với chúng... cách đây rất nhiều năm.
```
**Part 7** → `audio/vs/scene09_p7.wav` (301 ký tự) · mood `am_ap`

```text
Có một chú cá heo cái tên Bây-li, sống ở Bơ-mu-đa. Khi được nghe lại tiếng huýt sáo của người bạn cũ Ê-li, chú lập tức bơi nhanh đến chiếc loa, lượn quanh, và huýt sáo gọi lại. Hai bạn đã xa nhau hai mươi năm sáu tháng. Đó là trí nhớ xã hội dài nhất từng được ghi nhận ở một loài không phải con người.
```
**Part 8** → `audio/vs/scene09_p8.wav` (44 ký tự) · 🎭 cameo `tham_phan`

```text
Giám khảo... xin phép lau nước mắt một chút.
```
**Part 9** → `audio/vs/scene09_p9.wav` (335 ký tự) · mood `hao_hung`

```text
Tuyển thủ tiếp theo cũng sở hữu một đội hình huyền thoại: Rái Cá Biển. Khán giả đã biết rái cá nắm tay nhau ngủ thành "bè" để khỏi trôi. Nhưng một chiếc bè có thể lớn đến mức nào? Thông thường mỗi bè có từ mười đến một trăm con. Nhưng ở A-lát-xca từng ghi nhận những chiếc bè khổng lồ có tới hơn hai ngàn con Rái Cá Biển nằm cạnh nhau!
```
**Part 10** → `audio/vs/scene09_p10.wav` (170 ký tự) · mood `nghiem_trang_gia`

```text
Và bè rái cá có luật lệ rõ ràng: rái cá đực nằm một bè riêng, rái cá cái và con nhỏ nằm một bè riêng. Một ký túc xá nam, một ký túc xá nữ, ngay giữa đại dương! [laughter]
```
**Part 11** → `audio/vs/scene09_p11.wav` (365 ký tự) · mood `hao_hung`

```text
Tuyển thủ tiếp theo không phải là đội ở cùng nhau. Đó là cả một thành phố! Chim Cánh Cụt A-đê-li sống trong những đàn hàng chục ngàn, có khi hàng trăm ngàn cặp vợ chồng. Ở mũi đất Crô-di-ê trên đảo Rốt, các nhà khoa học đếm được khoảng một trăm năm mươi ngàn cặp chim cánh cụt làm tổ cùng một chỗ. Ồn ào, đông đúc, và... chật chội như phố cổ giờ tan tầm! [laughter]
```
**Part 12** → `audio/vs/scene09_p12.wav` (196 ký tự) · mood `am_ap`

```text
Trong một thành phố đông như thế, chim bố và chim mẹ vẫn tìm ra nhau, vẫn tìm ra con mình, chỉ bằng tiếng gọi. Mỗi cặp có một tiếng gọi riêng mà giữa hàng chục ngàn tiếng ồn ào, chúng vẫn nhận ra.
```
**Part 13** → `audio/vs/scene09_p13.wav` (161 ký tự) · mood `tram_bi_an`

```text
Và giờ, đến lượt những tuyển thủ thích... làm một mình. Chồn Gu-lô, Lửng Mật, Tôm Tít. Ba kẻ cô độc nổi tiếng nhất cuộc thi, đứng ở ba góc sân, không ai nhìn ai.
```
**Part 14** → `audio/vs/scene09_p14.wav` (314 ký tự) · mood `hao_hung`

```text
Nhưng giám khảo có một câu hỏi bất ngờ dành cho Tôm Tít: khi hai võ sĩ tôm tít tranh nhau một cái hang, chúng có đánh nhau đến chết không? Câu trả lời của khoa học: không. Các nhà nghiên cứu đã dàn dựng hơn sáu mươi trận tranh hang giữa những chú tôm tít, và thấy chúng đánh nhau theo một nghi thức rất... lịch sự.
```
**Part 15** → `audio/vs/scene09_p15.wav` (312 ký tự) · mood `don_dap`

```text
Đầu tiên, dang càng ra dọa nhau! Không ăn thua thì vẫy râu đánh hơi đối thủ! Vẫn không ăn thua, thì mới chuyển sang... đấm! Nhưng không phải đấm vào mặt. Mà là đấm vào tấm khiên ở đuôi! Con bị đánh cuộn đuôi lại, giơ tấm khiên dày cứng ra đỡ, hai bên thay nhau đấm vào khiên, như hai võ sĩ đấm vào găng của nhau.
```
**Part 16** → `audio/vs/scene09_p16.wav` (288 ký tự) · mood `nghiem_trang_gia`

```text
Và mục đích của màn đấm khiên này là để... đo sức nhau. Sau vài cú, con nào nhẹ cân hơn tự hiểu là mình yếu hơn, và lặng lẽ rút lui. Không ai phải chết. Một võ sĩ có cú đấm mạnh nhất đại dương, nhưng lại biết dùng nó để nói chuyện thay vì để giết nhau. Đúng là võ sĩ có võ đức! [laughter]
```
**Part 17** → `audio/vs/scene09_p17.wav` (164 ký tự) · mood `hao_hung`

```text
Còn Lửng Mật? Lửng Mật vẫn đi một mình... nhưng như vòng hai đã kể, phía sau nó luôn có sáu con chim ưng bám theo. Giám khảo hỏi: như vậy có tính là đồng đội không?
```
**Part 18** → `audio/vs/scene09_p18.wav` (114 ký tự) · 🎭 cameo `tham_phan`

```text
Giám khảo xin trả lời: không. Có người đi theo mình, nhưng mình không quan tâm tới họ, thì không phải là đồng đội.
```
**Part 19** → `audio/vs/scene09_p19.wav` (151 ký tự) · mood `nghiem_trang_gia`

```text
Vừa giành huy chương vàng ở vòng nuôi con, Lửng Mật lại trắng tay ở vòng này. Giỏi chăm con mình, nhưng làm việc với người ngoài thì... chưa biết cách!
```
**Part 20** → `audio/vs/scene09_p20.wav` (337 ký tự) · mood `hao_hung`

```text
Kết quả vòng sáu! Huy chương đồng: Rái Cá Biển, với những chiếc bè hai ngàn thành viên! Huy chương bạc: Tôm Tít, võ sĩ biết dùng nắm đấm để... thương lượng hòa bình! Và huy chương vàng... Thuộc về Cá Heo, huy chương vàng thứ hai! Đồng đội của cả con người suốt hơn một trăm năm, và là người bạn nhớ tên bạn mình sau hai mươi năm xa cách!
```
**Part 21** → `audio/vs/scene09_p21.wav` (217 ký tự) · mood `hao_hung`

```text
Bảng điểm sau sáu vòng: Thú Mỏ Vịt tám điểm! Cá Heo bám sát với bảy điểm! Chồn Gu-lô, Chim Cánh Cụt và Rái Cá cùng bốn điểm. Lửng Mật và Tôm Tít ba điểm. Bồ Nông hai điểm, Cô-a-la một điểm. Gấu Nước: vẫn chưa có điểm!
```
**Part 22** → `audio/vs/scene09_p22.wav` (283 ký tự) · mood `tram_bi_an`

```text
Nhưng vòng bảy sẽ đảo lộn tất cả. Vì vòng bảy sẽ không chấm năng lực. Vòng bảy là phiên phúc khảo: những tin đồn nổi tiếng nhất về các tuyển thủ sẽ được mang ra kiểm chứng. Và có những tuyển thủ sắp phát hiện ra rằng... danh tiếng của mình được xây trên một câu chuyện không có thật.
```

### scene10 — PHÓNG VIÊN HỎI KHÓ — TUYỂN THỦ TRẢ LỜI BẰNG SỰ THẬT
*Thẻ chương:* HỎI XOÁY, ĐÁP... KHOA HỌC

*Badge:* `HỌP BÁO` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene10_p0.wav` (140 ký tự) · mood `hao_hung`

```text
Trước vòng bảy, ban tổ chức mở một buổi họp báo. Phóng viên được hỏi bất cứ điều gì. Và các tuyển thủ phải trả lời... bằng sự thật khoa học!
```
**Part 1** → `audio/vs/scene10_p1.wav` (154 ký tự) · 🎭 cameo `phat_thanh_vien`

```text
Câu hỏi đầu tiên dành cho Tôm Tít: ở dưới đáy biển sâu, ánh sáng gần như chỉ còn màu xanh lam. Vậy những đốm màu trên người anh có còn ai nhìn thấy không?
```
**Part 2** → `audio/vs/scene10_p2.wav` (229 ký tự) · mood `tram_bi_an`

```text
Câu trả lời đến từ một lần lặn đêm năm hai ngàn lẻ hai ở vùng biển Ba-ha-mát. Một thợ lặn chiếu đèn xanh xuống một chú tôm tít đang thò đầu khỏi hang, và thấy hai đốm trên người nó... sáng rực lên màu vàng, như hai chiếc đèn pha.
```
**Part 3** → `audio/vs/scene10_p3.wav` (492 ký tự) · mood `nghiem_trang_gia`

```text
Các nhà khoa học giải thích: ở độ sâu khoảng bốn mươi mét, màu vàng gần như biến mất trong làn nước xanh. Nhưng những đốm này có chất phát quang, hấp thụ ánh sáng xanh rồi phát ra ánh sáng vàng. Nhờ vậy, tín hiệu vẫn rõ ràng ở dưới sâu. Và những đốm sáng ấy được dùng trong màn dọa nạt đối thủ. Tôm Tít dang càng, khoe đốm vàng phát sáng như muốn nói: "Đây là nhà của tôi, tránh ra!". Đây là trường hợp đầu tiên được ghi nhận về việc một sinh vật biển dùng ánh sáng phát quang để ra tín hiệu.
```
**Part 4** → `audio/vs/scene10_p4.wav` (118 ký tự) · mood `hao_hung`

```text
Tôm Tít trả lời xong, dang càng khoe đốm sáng ngay giữa phòng họp báo. Các phóng viên phải... đeo kính râm! [laughter]
```
**Part 5** → `audio/vs/scene10_p5.wav` (154 ký tự) · 🎭 cameo `phat_thanh_vien`

```text
Câu hỏi thứ hai dành cho Chim Bồ Nông: người ta đồn có một loài bồ nông lao đầu từ trên cao xuống biển để bắt cá. Lao mạnh như vậy, anh không đau đầu sao?
```
**Part 6** → `audio/vs/scene10_p6.wav` (202 ký tự) · mood `hao_hung`

```text
Đó là anh họ của Bồ Nông, loài bồ nông nâu ở châu Mỹ, loài bồ nông duy nhất săn mồi bằng cú bổ nhào ngoạn mục. Từ độ cao có khi tới hơn hai mươi mét, nó gập cánh và lao thẳng xuống biển như một mũi tên.
```
**Part 7** → `audio/vs/scene10_p7.wav` (162 ký tự) · mood `nghiem_trang_gia`

```text
Bí mật nằm ở những túi khí dưới da. Khi đập xuống mặt nước, các túi khí này đệm lại cú va chạm như túi khí ô tô, rồi giúp nó nổi bật trở lên như một cái nút chai.
```
**Part 8** → `audio/vs/scene10_p8.wav` (120 ký tự) · 🎭 cameo `phat_thanh_vien`

```text
Câu hỏi thứ ba dành cho Lửng Mật: ở Nam Phi, người ta còn gọi anh bằng một cái tên khác. Anh có biết đó là tên gì không?
```
**Part 9** → `audio/vs/scene10_p9.wav` (203 ký tự) · mood `hao_hung`

```text
Đó là tên "Ra-ten". Những người định cư Hà Lan ở Nam Phi đặt tên này theo tiếng gầm gừ lục cục rất đặc trưng mà Lửng Mật phát ra mỗi khi nổi giận. Nghe như tiếng... ai đó đang lắc một hộp sỏi! [laughter]
```
**Part 10** → `audio/vs/scene10_p10.wav` (144 ký tự) · mood `nghiem_trang_gia`

```text
Còn ở U-gan-đa, người Gan-đa gọi nó bằng một cái tên có nghĩa là "kẻ không nghe thấy", vì đôi tai của Lửng Mật rất nhỏ, gần như không nhìn thấy.
```
**Part 11** → `audio/vs/scene10_p11.wav` (103 ký tự) · mood `hao_hung`

```text
"Kẻ không nghe thấy"... Có lẽ đó là lý do vì sao Lửng Mật chưa bao giờ nghe lời ai can ngăn! [laughter]
```
**Part 12** → `audio/vs/scene10_p12.wav` (72 ký tự) · 🎭 cameo `phat_thanh_vien`

```text
Câu hỏi thứ tư dành cho Chồn Gu-lô: tên khoa học của anh có nghĩa là gì?
```
**Part 13** → `audio/vs/scene10_p13.wav` (85 ký tự) · mood `nghiem_trang_gia`

```text
Tên khoa học của Chồn Gu-lô bắt nguồn từ một chữ La-tinh có nghĩa là... "kẻ tham ăn".
```
**Part 14** → `audio/vs/scene10_p14.wav` (148 ký tự) · mood `hao_hung`

```text
Và cả phòng họp báo nhìn xuống khúc xương trên tay Chồn Gu-lô... Chồn Gu-lô lặng lẽ giấu khúc xương ra sau lưng. Không có gì để bàn thêm! [laughter]
```
**Part 15** → `audio/vs/scene10_p15.wav` (177 ký tự) · mood `nghiem_trang_gia`

```text
Nhưng các nhà khoa học cho rằng cái tên ấy có phần oan. Sống ở nơi lạnh giá, thức ăn khan hiếm, việc ăn được mọi thứ tìm thấy là một chiến lược sinh tồn chứ không phải tính xấu.
```
**Part 16** → `audio/vs/scene10_p16.wav` (135 ký tự) · 🎭 cameo `phat_thanh_vien`

```text
Câu hỏi cuối cùng dành cho Cô-a-la: có người nói túi của Cô-a-la mẹ mở ngược xuống dưới. Như vậy Cô-a-la con không bị rơi ra ngoài sao?
```
**Part 17** → `audio/vs/scene10_p17.wav` (177 ký tự) · mood `hao_hung`

```text
Đây là một hiểu lầm rất phổ biến. Theo Quỹ Cô-a-la Úc, khi mới sinh con, túi của Cô-a-la mẹ không mở ngược lên cũng không mở ngược xuống, mà mở thẳng ra phía trước, ở giữa bụng.
```
**Part 18** → `audio/vs/scene10_p18.wav` (208 ký tự) · mood `nghiem_trang_gia`

```text
Miệng túi có một cơ vòng rất khỏe mà mẹ có thể thắt chặt lại, giữ cho con không rơi ra ngoài. Chỉ khi con đã lớn và thò người ra ngoài, sức nặng của con mới kéo miệng túi trễ xuống, trông như túi... mở ngược.
```
**Part 19** → `audio/vs/scene10_p19.wav` (94 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Hồi nhỏ cháu toàn thò đầu ra ngắm cây đó ạ! Mẹ cháu bảo... đừng có thò ra nhiều quá, nặng lắm!
```
**Part 20** → `audio/vs/scene10_p20.wav` (110 ký tự) · 🎭 cameo `phat_thanh_vien`

```text
Xin cảm ơn các tuyển thủ. Và nhắn riêng tuyển thủ Chồn Gu-lô: phòng họp báo không cho phép mang xương vào nhé!
```
**Part 21** → `audio/vs/scene10_p21.wav` (172 ký tự) · mood `hao_hung`

```text
Buổi họp báo kết thúc! Năm câu hỏi, năm câu trả lời, và không ai phải... nói dối! Và giờ, đúng như tên gọi, chúng ta bước sang vòng thi về sự thật: phiên phúc khảo tin đồn!
```

### scene11 — PHÚC KHẢO TIN ĐỒN — HUYỀN THOẠI NÀO ĐÚNG, HUYỀN THOẠI NÀO SAI
*Thẻ chương:* TIN ĐỒN HAY SỰ THẬT?

*Badge:* `VÒNG 7` · *mood mặc định:* `nghiem_trang_gia`

**Part 0** → `audio/vs/scene11_p0.wav` (214 ký tự) · mood `nghiem_trang_gia`

```text
Vòng bảy: phúc khảo tin đồn. Luật chơi: giám khảo đọc một tin đồn nổi tiếng về tuyển thủ. Khoa học sẽ xác nhận hoặc bác bỏ. Tin đồn đúng: tuyển thủ được điểm. Tin đồn sai mà tuyển thủ dám thừa nhận: cũng được điểm!
```
**Part 1** → `audio/vs/scene11_p1.wav` (257 ký tự) · mood `tram_bi_an`

```text
Hồ sơ phúc khảo số một, và lần này kênh Vẽ Chuyện Hoang Dã tự phúc khảo chính mình! Trong tập phim về Tôm Tít, chúng tôi kể mắt nó có tới mười sáu loại tế bào cảm thụ ánh sáng. Và tin đồn đi kèm là: "Tôm Tít nhìn màu sắc rực rỡ hơn con người gấp nhiều lần".
```
**Part 2** → `audio/vs/scene11_p2.wav` (420 ký tự) · mood `hao_hung`

```text
Con số mười sáu là đúng, và trong đó có mười hai loại chuyên cảm nhận màu, trong khi mắt người chỉ có ba. Nhưng năm hai ngàn mười bốn, các nhà khoa học ở Úc làm một thí nghiệm đơn giản: dạy tôm tít nhận một màu để được thưởng đồ ăn, rồi cho chọn giữa hai màu gần giống nhau. Kết quả bất ngờ: khi hai màu khác nhau ít, kiểu như vàng với cam, Tôm Tít bắt đầu chọn sai. Có lúc chọn đúng không hơn gì... đoán bừa! [laughter]
```
**Part 3** → `audio/vs/scene11_p3.wav` (327 ký tự) · mood `nghiem_trang_gia`

```text
Hóa ra mười hai loại tế bào ấy không phối hợp để phân biệt sắc độ như mắt người. Mỗi loại làm việc riêng, giống như mười hai ngăn kéo phân loại màu: nhanh, nhưng không tinh. Các nhà khoa học cho rằng cách nhìn này giúp Tôm Tít nhận ra màu cực nhanh mà không cần não xử lý nhiều, rất hợp với cuộc sống chớp nhoáng dưới đáy biển.
```
**Part 4** → `audio/vs/scene11_p4.wav` (134 ký tự) · 🎭 cameo `tham_phan`

```text
Phán quyết: tin đồn "nhìn màu đẹp hơn người" là sai. Nhưng Tôm Tít có một cách nhìn màu độc nhất vô nhị. Tuyển thủ có chấp nhận không?
```
**Part 5** → `audio/vs/scene11_p5.wav` (121 ký tự) · mood `hao_hung`

```text
Tôm Tít gật đầu. Nó không cần nhìn màu đẹp hơn người. Nó chỉ cần nhìn thấy con mồi nhanh hơn con mồi kịp chạy! [laughter]
```
**Part 6** → `audio/vs/scene11_p6.wav` (136 ký tự) · mood `tram_bi_an`

```text
Hồ sơ phúc khảo số hai: Lửng Mật và chim dẫn mật. Như các bạn đã nghe ở vòng ba, khoa học hiện nay nói rằng: chưa có bằng chứng rõ ràng.
```
**Part 7** → `audio/vs/scene11_p7.wav` (103 ký tự) · mood `nghiem_trang_gia`

```text
Giám khảo hỏi Lửng Mật: tuyển thủ có thừa nhận câu chuyện chim dẫn đường là chưa được chứng minh không?
```
**Part 8** → `audio/vs/scene11_p8.wav` (155 ký tự) · mood `hao_hung`

```text
Lửng Mật im lặng một lúc lâu... rồi gật đầu. Gã giang hồ nổi tiếng không bao giờ lùi bước, lần đầu tiên chịu nhận là: ừ, chuyện đó chưa ai chứng minh được!
```
**Part 9** → `audio/vs/scene11_p9.wav` (116 ký tự) · 🎭 cameo `tham_phan`

```text
Phán quyết: tin đồn chưa được chứng minh. Nhưng tuyển thủ dám thừa nhận. Giám khảo ghi nhận tinh thần... trung thực!
```
**Part 10** → `audio/vs/scene11_p10.wav` (456 ký tự) · mood `tram_bi_an`

```text
Hồ sơ phúc khảo số ba: Gấu Nước. Tin đồn: "Năm hai ngàn mười chín, tàu vũ trụ Bê-rê-sít của I-xra-en rơi xuống Mặt Trăng, và hàng ngàn con Gấu Nước trên tàu hiện vẫn đang nằm ngủ trên Mặt Trăng, chờ ngày được hồi sinh". Khán giả của kênh còn nhớ: gấu nước từng bị bắn ra khỏi nòng súng cao tốc mà vẫn sống. Nhưng chính thí nghiệm ấy còn một phần hai ít ai kể. Năm hai ngàn hai mươi mốt, các nhà khoa học Anh tăng tốc độ bắn để tìm ra... giới hạn cuối cùng.
```
**Part 11** → `audio/vs/scene11_p11.wav` (354 ký tự) · mood `don_dap`

```text
Họ cho Gấu Nước ngủ đông, nhét vào viên đạn nhựa, rồi bắn vào bao cát, mỗi lần một nhanh hơn! Năm trăm mét mỗi giây! Bảy trăm! Tám trăm! Chín trăm! Kết quả: đến khoảng tám trăm hai mươi lăm mét mỗi giây, Gấu Nước vẫn sống. Nhưng chỉ nhích lên khoảng chín trăm mét mỗi giây, các nhà khoa học chỉ còn tìm thấy... những mảnh vụn. Siêu nhân cũng có giới hạn.
```
**Part 12** → `audio/vs/scene11_p12.wav` (206 ký tự) · mood `bi_hai`

```text
[sigh] Và cú va chạm khi tàu Bê-rê-sít rơi xuống Mặt Trăng tạo ra áp lực mạnh hơn rất nhiều so với giới hạn ấy. Kết luận của nhóm nghiên cứu: những chú Gấu Nước trên tàu gần như chắc chắn đã không sống sót.
```
**Part 13** → `audio/vs/scene11_p13.wav` (80 ký tự) · 🎭 cameo `tham_phan`

```text
Phán quyết: tin đồn Gấu Nước đang ngủ trên Mặt Trăng... khả năng rất cao là sai.
```
**Part 14** → `audio/vs/scene11_p14.wav` (198 ký tự) · mood `hao_hung`

```text
Nhưng khoan, Gấu Nước tỉnh dậy từ tủ đông và giơ tay xin phát biểu: "Tôi không bất tử. Tôi chỉ... rất, rất cứng". Và giám khảo đánh giá cao: dám nhận giới hạn của mình, đó cũng là một kiểu sức mạnh!
```
**Part 15** → `audio/vs/scene11_p15.wav` (305 ký tự) · mood `tram_bi_an`

```text
Hồ sơ phúc khảo số bốn: Chim Bồ Nông. Tin đồn này đã có từ hơn một ngàn năm trước. Người xưa tin rằng: khi không còn thức ăn, Bồ Nông mẹ sẽ tự mổ ngực mình, lấy máu nuôi con. Hình ảnh này nổi tiếng đến mức xuất hiện trên huy hiệu, trên cửa kính nhà thờ, trên biểu tượng của nhiều trường đại học ở châu Âu.
```
**Part 16** → `audio/vs/scene11_p16.wav` (348 ký tự) · mood `nghiem_trang_gia`

```text
Khoa học trả lời: không có chuyện đó. Khi cho con ăn, Bồ Nông mẹ ép cái túi họng vào ngực để đẩy cá đã nuốt ra cho con. Nhìn từ xa, trông như nó đang mổ vào ngực mình. Thêm nữa, đầu mỏ của một số loài bồ nông có màu đỏ, và có loài túi họng chuyển sang đỏ thẫm vào mùa sinh sản. Người xưa nhìn thấy màu đỏ ở ngực... thế là thêu dệt thành chuyện máu!
```
**Part 17** → `audio/vs/scene11_p17.wav` (155 ký tự) · 🎭 cameo `tham_phan`

```text
Phán quyết: tin đồn sai. Nhưng giám khảo ghi nhận: Bồ Nông là loài chim có biểu tượng tình mẫu tử... dễ thương nhất lịch sử, dù là nhờ hiểu lầm! [laughter]
```
**Part 18** → `audio/vs/scene11_p18.wav` (169 ký tự) · mood `tram_bi_an`

```text
Hồ sơ phúc khảo số năm, và là hồ sơ cuối cùng: Gấu Cô-a-la. Tin đồn: "Cô-a-la chỉ lấy nước từ lá, ngoài những ngày nắng nóng khắc nghiệt thì gần như không bao giờ uống".
```
**Part 19** → `audio/vs/scene11_p19.wav` (212 ký tự) · mood `hao_hung`

```text
Vòng một đã trả lời rồi! Năm hai ngàn hai mươi, khoa học đã ghi nhận bốn mươi sáu lần Cô-a-la hoang dã liếm nước mưa từ thân cây, kể cả những ngày trời không hề nóng. Cô-a-la uống thường xuyên hơn chúng ta tưởng!
```
**Part 20** → `audio/vs/scene11_p20.wav` (62 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Cháu có uống mà! Có điều... cháu chỉ uống khi trời mưa thôi ạ.
```
**Part 21** → `audio/vs/scene11_p21.wav` (137 ký tự) · mood `nghiem_trang_gia`

```text
Phán quyết: tin đồn "gần như không bao giờ uống" là chưa đúng. Và Cô-a-la chính là tuyển thủ giúp khoa học sửa lại một hiểu lầm trăm năm!
```
**Part 22** → `audio/vs/scene11_p22.wav` (361 ký tự) · mood `hao_hung`

```text
Kết quả vòng bảy, và đây là vòng có kết quả bất ngờ nhất đêm nay! Huy chương đồng: Gấu Nước, sinh vật siêu cứng dám thừa nhận mình không bất tử! Huy chương bạc: Cô-a-la, người giúp khoa học sửa sai! Và huy chương vàng vòng bảy thuộc về... Lửng Mật, huy chương vàng thứ hai! Vì lần đầu tiên trong lịch sử, gã giang hồ chịu nhận mình... chưa chắc đúng! [laughter]
```
**Part 23** → `audio/vs/scene11_p23.wav` (209 ký tự) · mood `hao_hung`

```text
Bảng điểm sau bảy vòng: Thú Mỏ Vịt tám điểm! Cá Heo bảy điểm! Lửng Mật bứt lên mạnh mẽ với sáu điểm! Chồn Gu-lô, Chim Cánh Cụt, Rái Cá bốn điểm. Tôm Tít và Cô-a-la ba điểm. Bồ Nông hai điểm, Gấu Nước một điểm.
```
**Part 24** → `audio/vs/scene11_p24.wav` (251 ký tự) · mood `tram_bi_an`

```text
Ba tuyển thủ dẫn đầu chỉ cách nhau đúng hai điểm! Chỉ còn một vòng cuối. Và vòng cuối có điểm nhân đôi: vàng sáu điểm, bạc bốn điểm, đồng hai điểm. Câu hỏi của vòng chung kết không phải là ai mạnh nhất. Mà là: ai đã giúp ích cho loài người nhiều nhất.
```

### scene12 — THỌ NHẤT, LẶN CHĂM NHẤT, ĂN KHỎE NHẤT, HỒI SINH NGOẠN MỤC NHẤT
*Thẻ chương:* NHỮNG KỶ LỤC BÊN LỀ

*Badge:* `GIẢI PHỤ` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene12_p0.wav` (182 ký tự) · mood `hao_hung`

```text
Trước khi bước vào vòng chung kết, ban tổ chức có một bất ngờ: lễ trao giải phụ! Những giải này không tính điểm, nhưng mỗi giải là một kỷ lục có thật mà khán giả xứng đáng được biết.
```
**Part 1** → `audio/vs/scene12_p1.wav` (342 ký tự) · mood `hao_hung`

```text
Giải phụ thứ nhất: tuyển thủ có thành viên sống thọ nhất! Và giải thuộc về... Cá Heo! Mời khán giả làm quen với bà cụ Ních-lô. Ních-lô là một cô cá heo hoang dã sống ở vịnh Xa-ra-xô-ta, bang Phlo-ri-đa. Một nhóm nghiên cứu đã theo dõi cá heo ở vịnh này từ năm một ngàn chín trăm bảy mươi, và họ đã nhìn thấy Ních-lô hơn tám trăm hai mươi lần.
```
**Part 2** → `audio/vs/scene12_p2.wav` (418 ký tự) · mood `am_ap`

```text
Để biết tuổi của cô, các nhà khoa học đã đếm các lớp vân trên một chiếc răng, giống như đếm vòng gỗ trên thân cây. Và lần cuối cùng Ních-lô được nhìn thấy, vào năm hai ngàn mười bảy, cô đã sáu mươi bảy tuổi. Ních-lô là cá heo hoang dã sống thọ nhất từng được ghi nhận. Cô sinh ít nhất bốn con, con út ra đời khi cô đã bốn mươi tám tuổi. Và đứa con út ấy sau này cũng có con, nối dài ba thế hệ trong cùng một vịnh biển.
```
**Part 3** → `audio/vs/scene12_p3.wav` (114 ký tự) · 🎭 cameo `tham_phan`

```text
Giám khảo xin cúi đầu chào bà cụ Ních-lô. Sáu mươi bảy năm giữa biển khơi, quả là một hành trình sinh tồn đáng nể.
```
**Part 4** → `audio/vs/scene12_p4.wav` (430 ký tự) · mood `hao_hung`

```text
Giải phụ thứ hai: thọ nhất trong nhóm... nhỏ con. Và giải thuộc về Thú Mỏ Vịt! Năm hai ngàn hai mươi ba, ở một con suối nhỏ gần thành phố Men-bơn, nước Úc, các nhà nghiên cứu bắt lại một chú Thú Mỏ Vịt đực đã được gắn thẻ từ hơn hai mươi năm trước. Chú được gắn thẻ khi mới khoảng một tuổi, và khi bị bắt lại, chú đã hai mươi bốn tuổi. Đây là Thú Mỏ Vịt hoang dã sống thọ nhất từng được ghi nhận, vượt kỷ lục cũ hai mươi mốt tuổi.
```
**Part 5** → `audio/vs/scene12_p5.wav` (160 ký tự) · mood `nghiem_trang_gia`

```text
Trong khi đó, ở sa mạc Ka-la-ha-ri, Lửng Mật hoang dã thường chỉ sống khoảng ba đến tám năm. Gã giang hồ dũng cảm nhất đại hội... lại có cuộc đời khá ngắn ngủi.
```
**Part 6** → `audio/vs/scene12_p6.wav` (209 ký tự) · mood `hao_hung`

```text
Giải phụ thứ ba: thợ lặn chăm chỉ nhất! Và lại là Thú Mỏ Vịt! Ở một hồ nước trên núi ở Ta-xma-ni-a, các nhà khoa học đã gắn thiết bị đo độ sâu lên mười một chú Thú Mỏ Vịt và ghi lại gần chín mươi ngàn lần lặn.
```
**Part 7** → `audio/vs/scene12_p7.wav` (201 ký tự) · mood `don_dap`

```text
Mỗi lần lặn trung bình chỉ khoảng ba mươi mốt giây! Ngoi lên thở mười giây, rồi lại lặn tiếp! Trung bình bảy mươi lăm lần mỗi giờ! Và có những chuyến kiếm ăn, nó lặn tới một ngàn sáu trăm lần liên tục!
```
**Part 8** → `audio/vs/scene12_p8.wav` (828 ký tự) · mood `hao_hung`

```text
Giải phụ thứ tư: lò sưởi bí ẩn nhất! Và giải thuộc về Rái Cá Biển. Khán giả của kênh đã biết Rái Cá đốt năng lượng rất nhanh để giữ ấm. Nhưng suốt nhiều chục năm, không ai biết chính xác hơi ấm ấy được tạo ra ở đâu trong cơ thể. Năm hai ngàn hai mươi mốt, các nhà khoa học lấy mẫu cơ bắp của hai mươi mốt chú Rái Cá Biển, từ con non đến con trưởng thành, và đo cách các tế bào cơ sử dụng ô-xy. Và họ phát hiện ra: những nhà máy năng lượng tí hon trong tế bào cơ của Rái Cá bị... rò rỉ, có chủ đích. Thay vì biến hết năng lượng thành sức để cử động, chúng để một phần lớn thoát ra dưới dạng nhiệt. Cơ bắp sưởi ấm cơ thể mà không cần cử động! Điều bất ngờ nhất: ngay cả Rái Cá con mới sinh, cơ bắp còn non nớt, các tế bào cơ đã có khả năng tạo nhiệt ngang bằng con trưởng thành. Lò sưởi được lắp sẵn... từ lúc chào đời! [laughter]
```
**Part 9** → `audio/vs/scene12_p9.wav` (211 ký tự) · mood `hao_hung`

```text
Giải phụ thứ năm: thiết kế không cần sửa lâu nhất! Và giải thuộc về... Chim Bồ Nông! Ở vùng Lu-bê-rông, miền Nam nước Pháp, người ta tìm thấy hóa thạch của một chú bồ nông sống cách đây khoảng ba mươi triệu năm.
```
**Part 10** → `audio/vs/scene12_p10.wav` (380 ký tự) · mood `nghiem_trang_gia`

```text
Và điều khiến các nhà khoa học kinh ngạc: chiếc mỏ của chú bồ nông ba mươi triệu năm tuổi ấy... gần như giống hệt mỏ bồ nông ngày nay. Ba mươi triệu năm, tạo hóa gần như không phải sửa gì thêm! Các nhà khoa học đoán rằng chiếc mỏ ấy đã quá phù hợp để bắt cá, nên không cần thay đổi. Một sản phẩm ra mắt từ ba mươi triệu năm trước... mà chưa từng phải tung bản cập nhật! [laughter]
```
**Part 11** → `audio/vs/scene12_p11.wav` (457 ký tự) · mood `hao_hung`

```text
Giải phụ thứ sáu: tên gọi thú vị nhất! Ban tổ chức đã tra tên khoa học của từng tuyển thủ, và phát hiện ra mỗi cái tên là một câu chuyện. Tên khoa học của Lửng Mật là Me-li-vo-ra ca-pen-xít. Me-li-vo-ra nghĩa là "kẻ ăn mật", còn ca-pen-xít là "đến từ mũi Hảo Vọng", nơi mẫu vật đầu tiên được thu thập ở Nam Phi. Tên của Tôm Tít trong khoa học là bộ Chân Miệng, vì những chiếc chân bắt mồi của nó nằm ngay gần miệng. Một võ sĩ mà tay nằm ở... cằm! [laughter]
```
**Part 12** → `audio/vs/scene12_p12.wav` (441 ký tự) · mood `tram_bi_an`

```text
Gấu Nước được mô tả lần đầu vào năm một ngàn bảy trăm bảy mươi ba bởi một mục sư người Đức. Ông nhìn qua kính hiển vi, thấy sinh vật này lạch bạch như một chú gấu, nên gọi nó là "chú gấu nước nhỏ". Ba năm sau, một nhà khoa học người Ý đặt cho nó cái tên khoa học có nghĩa là "kẻ bước chậm". Và hơn hai trăm năm sau, các nhà khoa học hiện đại đo được tốc độ đi dạo của nó: khoảng nửa thân mình mỗi giây. Đúng là danh bất hư truyền! [laughter]
```
**Part 13** → `audio/vs/scene12_p13.wav` (433 ký tự) · mood `nghiem_trang_gia`

```text
Còn Thú Mỏ Vịt? Ban đầu, nó được đặt tên khoa học là Pla-ti-pớt, nghĩa là "chân dẹt". Nhưng các nhà khoa học sớm phát hiện ra: cái tên ấy đã thuộc về... một loài bọ cánh cứng! Thế là Thú Mỏ Vịt phải nhận một tên khoa học mới, có nghĩa là "mỏ chim, giống vịt". Nhưng cái tên cũ "chân dẹt" vẫn ở lại làm tên gọi thường ngày bằng tiếng Anh đến tận bây giờ. Mất tên khoa học vào tay một con bọ... nhưng vẫn giữ được biệt danh! [laughter]
```
**Part 14** → `audio/vs/scene12_p14.wav` (426 ký tự) · mood `tram_bi_an`

```text
Giải phụ cuối cùng, và là giải mà ban tổ chức trân trọng nhất: giải hồi sinh ngoạn mục. Giải này thuộc về Rái Cá Biển, và câu chuyện của nó bắt đầu từ hơn hai trăm năm trước. Bộ lông dày nhất thế giới động vật từng khiến Rái Cá Biển trở thành món hàng săn lùng. Suốt hơn một thế kỷ rưỡi, người ta săn bắt chúng để lấy da. Đến năm một ngàn chín trăm mười một, trên toàn thế giới chỉ còn khoảng một đến hai ngàn con Rái Cá Biển.
```
**Part 15** → `audio/vs/scene12_p15.wav` (394 ký tự) · mood `am_ap`

```text
Và cũng chính năm một ngàn chín trăm mười một ấy, bốn quốc gia đã ký một hiệp ước cấm săn bắt. Những nhóm rái cá nhỏ bé còn sót lại bắt đầu sinh sôi trở lại. Ngày nay, đã có hơn một trăm ngàn con Rái Cá Biển trên khắp các vùng biển xưa của chúng. Từ một ngàn con lên hơn một trăm ngàn con. Đó là bằng chứng rõ ràng nhất rằng: khi con người dừng tay đúng lúc, thiên nhiên biết cách tự chữa lành.
```
**Part 16** → `audio/vs/scene12_p16.wav` (119 ký tự) · 🎭 cameo `tham_phan`

```text
Giám khảo xin trao giải đặc biệt này cho Rái Cá Biển. Và cũng xin gửi lời cảm ơn tới những người đã ký hiệp ước năm ấy.
```
**Part 17** → `audio/vs/scene12_p17.wav` (113 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Ủa, vậy là năm nay không có giải phụ nào cho người ngủ giỏi nhất hả chú? Cháu ngủ hai mươi hai tiếng mỗi ngày đó!
```
**Part 18** → `audio/vs/scene12_p18.wav` (186 ký tự) · mood `hao_hung`

```text
Câu hỏi rất hợp lý! Nhưng chuyện Cô-a-la ngủ hai mươi hai tiếng thì khán giả của kênh đã biết rồi. Đại hội này chỉ trao giải cho những điều mới. Hẹn bạn ở... đại hội ngủ trưa! [laughter]
```
**Part 19** → `audio/vs/scene12_p19.wav` (133 ký tự) · mood `hao_hung`

```text
Lễ trao giải phụ khép lại! Và giờ, xin mời tất cả các tuyển thủ bước vào sân khấu chính, cho vòng thi cuối cùng của Đại Hội Sinh Tồn!
```

### scene13 — AI ĐÃ GIÚP ÍCH CHO LOÀI NGƯỜI NHIỀU NHẤT
*Thẻ chương:* ĐIỂM NHÂN ĐÔI – AI LÊN NGÔI?

*Badge:* `CHUNG KẾT` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene13_p0.wav` (178 ký tự) · mood `hao_hung`

```text
Vòng chung kết: món quà cho loài người! Mỗi tuyển thủ sẽ trình bày một phát minh, một loại thuốc, hay một công nghệ mà con người đã học được, hoặc đang học, từ chính cơ thể mình.
```
**Part 1** → `audio/vs/scene13_p1.wav` (473 ký tự) · mood `hao_hung`

```text
Rái Cá Biển mở hộp quà đầu tiên. Bên trong là... một bộ đồ lặn có lông! [laughter] Năm hai ngàn mười sáu, các kỹ sư ở Viện Công nghệ Ma-xa-chu-xét đã làm những tấm cao su phủ lông nhân tạo, mô phỏng bộ lông của rái cá và hải ly, rồi nhúng chúng vào chất lỏng ở nhiều tốc độ khác nhau. Họ phát hiện: lông càng dày, lặn xuống càng nhanh, thì càng giữ lại được nhiều không khí. Từ đó, họ tìm ra công thức để có thể chế tạo những bộ đồ lặn ấm áp lấy cảm hứng từ bộ lông rái cá.
```
**Part 2** → `audio/vs/scene13_p2.wav` (524 ký tự) · mood `hao_hung`

```text
Chim Cánh Cụt mở hộp quà thứ hai: một tấm lưới thép nhỏ xíu, lấp lánh. Các nhà khoa học ở Ca-na-đa thắc mắc: tại sao chim cánh cụt sống giữa băng giá mà lông không bao giờ bị đóng băng? Họ soi lông chim cánh cụt dưới kính hiển vi, và thấy những sợi lông nhỏ đan móc vào nhau như một tấm lưới, trên bề mặt có những rãnh siêu nhỏ. Họ bắt chước cấu trúc ấy bằng lưới thép không gỉ, khắc thêm rãnh siêu nhỏ bằng tia la-de. Kết quả: băng bám vào tấm lưới yếu hơn khoảng chín mươi lăm phần trăm so với tấm thép phẳng thông thường!
```
**Part 3** → `audio/vs/scene13_p3.wav` (206 ký tự) · mood `am_ap`

```text
Các nhà khoa học hy vọng vật liệu này sẽ giúp chống đóng băng cho đường dây điện, tuabin gió và máy bay, mà không cần hóa chất. Quý ông Vest Đuôi Tôm... đang góp phần giữ điện cho cả một thành phố mùa đông!
```
**Part 4** → `audio/vs/scene13_p4.wav` (454 ký tự) · mood `hao_hung`

```text
Bồ Nông mở hộp quà thứ ba. Bên trong là... một chiếc máy bay đồ chơi! Từ việc nghiên cứu cách những đàn chim lớn bay theo hình chữ V để tiết kiệm sức, hãng máy bay Ê-bớt đã thử nghiệm cho hai chiếc máy bay chở khách cỡ lớn bay nối đuôi nhau, cách nhau khoảng ba cây số. Chiếc bay sau lướt trên luồng khí của chiếc bay trước, giống hệt bồ nông. Chuyến bay thử năm hai ngàn hai mươi mốt từ Pháp sang Ca-na-đa đã tiết kiệm được hơn sáu tấn khí thải cac-bon.
```
**Part 5** → `audio/vs/scene13_p5.wav` (392 ký tự) · mood `hao_hung`

```text
Tôm Tít mở hộp quà thứ tư, và bên trong là... một chiếc mũ bảo hiểm! Một chiếc càng búa của Tôm Tít phải chịu hàng chục ngàn cú đấm trong đời mà không vỡ. Các kỹ sư ở Đại học Ca-li-phoóc-ni-a đã soi vào bên trong để tìm hiểu bí mật. Họ thấy những lớp sợi xếp xoắn như cầu thang xoắn ốc. Mỗi khi có cú va chạm, vết nứt bị buộc phải đi vòng vèo theo các lớp xoắn, nên không thể xuyên thẳng qua.
```
**Part 6** → `audio/vs/scene13_p6.wav` (242 ký tự) · mood `nghiem_trang_gia`

```text
Cấu trúc xoắn ốc ấy đang được các kỹ sư bắt chước để làm ra những vật liệu nhẹ mà chịu va đập tốt, hướng tới mũ bảo hiểm, áo giáp và khung xe, khung máy bay. Giám khảo ghi nhận, nhưng xin để dành huy chương chờ những sản phẩm đầu tiên ra đời!
```
**Part 7** → `audio/vs/scene13_p7.wav` (194 ký tự) · mood `hao_hung`

```text
Cá Heo xin chen ngang mở một hộp quà... ngoài danh sách. Bên trong là một chiếc phao nhỏ màu cam. Và câu chuyện của chiếc phao này bắt đầu ở một bến cảng nước I-rắc, tháng Ba năm hai ngàn lẻ ba.
```
**Part 8** → `audio/vs/scene13_p8.wav` (481 ký tự) · mood `nghiem_trang_gia`

```text
Bến cảng ấy bị thả hơn một trăm quả thủy lôi và vật nổ dưới nước. Máy dò dưới nước đã phát hiện hơn hai trăm vật thể đáng ngờ, nhưng máy không phân biệt được đâu là thủy lôi, đâu là rác hay đá. Đó là lúc tám chú cá heo của Hải quân Mỹ được gửi xuống. Bằng tiếng định vị, cá heo phân biệt được vật thể tự nhiên và vật thể do con người làm ra, kể cả những thứ bị vùi trong bùn. Khi phát hiện thủy lôi, chúng bơi về báo cho người huấn luyện, rồi mang chiếc phao xuống đánh dấu vị trí.
```
**Part 9** → `audio/vs/scene13_p9.wav` (238 ký tự) · mood `am_ap`

```text
Nhờ vậy, chỉ khoảng một tuần sau, bến cảng đã được mở lại để những con tàu chở gạo và lương thực cập bến. Các nhà khoa học hải quân thừa nhận: trong vùng nước đục và nhiều vật cản, khả năng định vị của cá heo vẫn vượt mọi máy móc hiện có.
```
**Part 10** → `audio/vs/scene13_p10.wav` (131 ký tự) · 🎭 cameo `tham_phan`

```text
Giám khảo ghi nhận món quà ngoài danh sách của Cá Heo. Nhưng vì đây là phần chen ngang... nên chỉ được tính là điểm cộng tinh thần!
```
**Part 11** → `audio/vs/scene13_p11.wav` (268 ký tự) · mood `tram_bi_an`

```text
Gấu Nước mở hộp quà thứ năm. Bên trong là... một đoạn gen phát sáng. Năm hai ngàn mười sáu, các nhà khoa học Nhật Bản giải mã bộ gen của một loài gấu nước cực kỳ khỏe, và tìm thấy một loại đạm chỉ gấu nước mới có. Họ đặt tên nó là Đi-súp, nghĩa là "chất chống hư hại".
```
**Part 12** → `audio/vs/scene13_p12.wav` (307 ký tự) · mood `nghiem_trang_gia`

```text
Rồi họ làm một thí nghiệm táo bạo: đưa đoạn gen này vào tế bào người nuôi trong phòng thí nghiệm, rồi chiếu tia X. Kết quả: tế bào người có đạm Đi-súp bị hư hại ADN ít hơn khoảng bốn mươi phần trăm! Một chú gấu nước bé hơn hạt cát đã cho tế bào người... mượn tạm một chiếc áo giáp chống phóng xạ! [laughter]
```
**Part 13** → `audio/vs/scene13_p13.wav` (397 ký tự) · mood `hao_hung`

```text
Và cuối cùng, tuyển thủ dẫn đầu: Thú Mỏ Vịt. Ở vòng ba, Thú Mỏ Vịt đã kể về chất kháng khuẩn trong sữa. Hôm nay, nó mở hộp quà thứ sáu, và bên trong là... một giọt nọc độc. Thú Mỏ Vịt đực có chiếc cựa độc ở chân sau. Năm hai ngàn mười sáu, các nhà khoa học Úc phát hiện trong nọc độc ấy có một loại hóc-môn gọi là Gờ-lờ-pê-một. Ở người, hóc-môn này giúp cơ thể tiết ra in-su-lin để hạ đường huyết.
```
**Part 14** → `audio/vs/scene13_p14.wav` (402 ký tự) · mood `nghiem_trang_gia`

```text
Vấn đề là ở người, hóc-môn này bị phân hủy chỉ trong vài phút. Còn hóc-môn trong nọc Thú Mỏ Vịt thì bền hơn hẳn, vì nó vừa phải làm việc trong ruột, vừa phải làm việc trong nọc độc. Và một hóc-môn bền hơn chính là điều mà các nhà khoa học tìm kiếm để làm thuốc điều trị bệnh tiểu đường loại hai. Hiện nay các nhóm nghiên cứu ở Úc đang thử nghiệm những phân tử lấy cảm hứng từ nọc Thú Mỏ Vịt trên chuột.
```
**Part 15** → `audio/vs/scene13_p15.wav` (184 ký tự) · mood `hao_hung`

```text
Sữa có chất diệt khuẩn. Nọc độc có thể thành thuốc chữa tiểu đường. Con vật từng bị các nhà khoa học cầm kéo đi tìm đường chỉ khâu, hóa ra lại là một... hiệu thuốc biết bơi! [laughter]
```
**Part 16** → `audio/vs/scene13_p16.wav` (66 ký tự) · mood `tram_bi_an`

```text
Giám khảo ra hiệu chuẩn bị công bố. Cả sân vận động im phăng phắc.
```
**Part 17** → `audio/vs/scene13_p17.wav` (99 ký tự) · 🎭 cameo `tham_phan`

```text
Huy chương đồng vòng chung kết, hai điểm: Chim Bồ Nông, người thầy dạy máy bay cách bay đỡ tốn sức!
```
**Part 18** → `audio/vs/scene13_p18.wav` (72 ký tự) · 🎭 cameo `tham_phan`

```text
Huy chương bạc, bốn điểm: Gấu Nước, người cho tế bào người mượn áo giáp!
```
**Part 19** → `audio/vs/scene13_p19.wav` (68 ký tự) · 🎭 cameo `tham_phan`

```text
Và huy chương vàng vòng chung kết, sáu điểm, thuộc về... Thú Mỏ Vịt!
```
**Part 20** → `audio/vs/scene13_p20.wav` (64 ký tự) · mood `hao_hung`

```text
Và đây là bảng điểm cuối cùng của Đại Hội Sinh Tồn lần thứ nhất!
```
**Part 21** → `audio/vs/scene13_p21.wav` (293 ký tự) · mood `don_dap`

```text
Hạng ba: Lửng Mật, sáu điểm! Trắng tay suốt bốn vòng đầu, rồi bùng nổ với hai huy chương vàng: bà mẹ chuyển nhà mỗi ba ngày, và gã giang hồ dám nhận mình chưa chắc đúng! Hạng hai: Cá Heo, bảy điểm! Người lính gác mười lăm ngày không ngủ, và người bạn của ngư dân Bra-xin suốt hơn một trăm năm!
```
**Part 22** → `audio/vs/scene13_p22.wav` (180 ký tự) · mood `hao_hung`

```text
Và nhà vô địch Đại Hội Sinh Tồn lần thứ nhất, với ba huy chương vàng, một huy chương bạc và mười bốn điểm... Thú Mỏ Vịt! Tuyển thủ mà các chuyên gia dự đoán chỉ "tham gia cho vui"!
```

### scene14 — NHÀ VÔ ĐỊCH BẤT NGỜ VÀ BÀI HỌC CỦA ĐẠI HỘI
*Thẻ chương:* KẺ BỊ CHÊ LÊN NGÔI

*Badge:* `BẾ MẠC` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene14_p0.wav` (200 ký tự) · mood `am_ap`

```text
Thú Mỏ Vịt đứng trên bục cao nhất, chiếc vương miện bé xíu hơi lệch trên đầu. Hơn hai trăm năm trước, khi mẫu vật đầu tiên đến châu Âu, các nhà khoa học tưởng nó là đồ giả. Đêm nay, nó là nhà vô địch.
```
**Part 1** → `audio/vs/scene14_p1.wav` (87 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Ủa... vậy là bạn mỏ vịt thắng thật ạ? Chúc mừng bạn! Bạn có muốn ôm cây với cháu không?
```
**Part 2** → `audio/vs/scene14_p2.wav` (307 ký tự) · mood `hao_hung`

```text
Nhìn lại cả tám vòng thi, có một điều thú vị: những tuyển thủ được dự đoán là mạnh nhất, Tôm Tít và Gấu Nước, lại không lên được bục vinh quang. Vì sinh tồn không chỉ là đánh nhau. Sinh tồn còn là giữ ấm giữa nước đá, là đi theo mặt trời mười ba ngàn cây số, là hợp tác với người đánh cá, là ôm cây cho mát.
```
**Part 3** → `audio/vs/scene14_p3.wav` (362 ký tự) · mood `am_ap`

```text
Và có một điểm chung giữa những tuyển thủ chiến thắng ở vòng cuối: con người đã học được từ chúng. Từ lông rái cá, lông cánh cụt, đội hình bồ nông, đến gen gấu nước và sữa, nọc độc của thú mỏ vịt. Thiên nhiên không chỉ là nơi để chúng ta ngắm nhìn. Đó còn là một thư viện khổng lồ, nơi mỗi loài vật là một cuốn sách chứa những lời giải mà con người chưa nghĩ ra.
```
**Part 4** → `audio/vs/scene14_p4.wav` (535 ký tự) · mood `bi_hai`

```text
[sigh] Và cũng có những cuốn sách đang bị đe dọa. Ngày mười hai tháng Hai năm hai ngàn hai mươi hai, Cô-a-la ở ba bang miền Đông nước Úc chính thức bị xếp vào danh sách nguy cấp, sau hạn hán kéo dài, cháy rừng và mất nơi sống. Tháng Mười Một năm hai ngàn hai mươi ba, đến lượt Chồn Gu-lô ở lục địa nước Mỹ được đưa vào danh sách loài bị đe dọa, vì những lớp tuyết mùa xuân mà nó cần để sinh con đang ngày một ít đi. Chồn Gu-lô cần tuyết mùa xuân. Cá heo ở La-gu-na cần cá đối. Cô-a-la cần những cái cây để ôm, và những cơn mưa để uống.
```
**Part 5** → `audio/vs/scene14_p5.wav` (235 ký tự) · mood `am_ap`

```text
Nếu những loài vật này biến mất, chúng ta không chỉ mất đi những sinh vật đáng yêu. Chúng ta còn mất đi những lời giải mà có khi... chưa ai kịp đọc. Nhưng câu chuyện Rái Cá Biển ở lễ trao giải phụ đã cho thấy: chưa bao giờ là quá muộn.
```
**Part 6** → `audio/vs/scene14_p6.wav` (114 ký tự) · mood `hao_hung`

```text
Trước khi chia tay, mời toàn thể khán đài cùng nhìn lại bảng tổng sắp cuối cùng của Đại Hội Sinh Tồn lần thứ nhất!
```
**Part 7** → `audio/vs/scene14_p7.wav` (470 ký tự) · mood `don_dap`

```text
Vô địch: Thú Mỏ Vịt, mười bốn điểm! Ba huy chương vàng, một huy chương bạc! Bơi năm tiếng trong nước không độ, ăn khỏe nhất cuộc thi, và mang đến cho loài người cả sữa diệt khuẩn lẫn nọc độc chữa bệnh! Á quân: Cá Heo, bảy điểm! Người lính gác mười lăm ngày, đồng đội trăm năm của ngư dân Bra-xin, và bà cụ Ních-lô sáu mươi bảy tuổi! Hạng ba: Lửng Mật, sáu điểm! Trắng tay bốn vòng đầu, rồi bùng nổ với hai huy chương vàng nhờ làm mẹ giỏi và dám nhận mình chưa chắc đúng!
```
**Part 8** → `audio/vs/scene14_p8.wav` (455 ký tự) · mood `hao_hung`

```text
Hạng tư: Gấu Nước, năm điểm, tuyển thủ được dự đoán vô địch đã bứt phá ở hai vòng cuối. Tiếp theo là nhóm bám đuổi, cùng bốn điểm: Chồn Gu-lô với hai huy chương bạc, Chim Cánh Cụt với một vàng một đồng, Rái Cá Biển với một bạc hai đồng, và Chim Bồ Nông với một bạc một đồng. Và cuối bảng, cùng ba điểm: Tôm Tít, võ sĩ biết đấm khiên thay vì đấm người, và Cô-a-la, tuyển thủ ngủ nhiều nhất nhưng đã giúp khoa học sửa một hiểu lầm. Không ai ra về tay trắng!
```
**Part 9** → `audio/vs/scene14_p9.wav` (403 ký tự) · mood `am_ap`

```text
Và nếu phải chọn những khoảnh khắc đáng nhớ nhất của đại hội, thì đó là: Cô-a-la ôm cây keo làm điều hòa. Chồn Gu-lô đi bộ tám trăm cây số và trở thành con chồn đầu tiên ở Cô-lô-ra-đô sau chín mươi năm. Chim Cánh Cụt đi theo mặt trời mười ba ngàn cây số. Gấu Nước bị bắn khỏi nòng súng khí và dám thừa nhận mình không bất tử. Và ông lão ngư dân Bra-xin đứng dưới nước, chờ tín hiệu của người bạn cá heo.
```
**Part 10** → `audio/vs/scene14_p10.wav` (237 ký tự) · mood `hao_hung`

```text
Và bây giờ, đến lượt bạn làm giám khảo! Bạn đồng ý với kết quả này không? Nếu là bạn, bạn sẽ trao vương miện cho ai? Hãy viết tên nhà vô địch của riêng bạn ở phần bình luận nhé. Biết đâu, ở đại hội lần sau, kết quả sẽ thay đổi hoàn toàn!
```
**Part 11** → `audio/vs/scene14_p11.wav` (199 ký tự) · mood `tram_bi_an`

```text
Vì Đại Hội Sinh Tồn lần thứ hai đã có danh sách tuyển thủ. Mười gương mặt mới, đến từ khắp nơi trên thế giới: từ khu rừng tre ở Tứ Xuyên, đến dòng sông bùn ở châu Phi, đến những cánh rừng mưa Nam Mỹ.
```
**Part 12** → `audio/vs/scene14_p12.wav` (136 ký tự) · mood `hao_hung`

```text
Và lần này, có một tuyển thủ mang theo cả một khẩu đại bác nước trên càng! Hẹn gặp lại toàn thể khán đài ở Đại Hội Sinh Tồn lần thứ hai!
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Mười quái kiệt. Tám vòng thi. Một chiếc vương miện! Lửng Mật, Tôm Tít, Gấu Nước được dự đoán sẽ thắng. Còn Thú Mỏ Vịt... tham gia cho vui! [laughter] Vòng một: Thú Mỏ Vịt bơi năm tiếng trong nước không độ C mà thân nhiệt không hề tụt! Vòng hai: Chim Cánh Cụt đi mười ba ngàn cây số mỗi năm, theo mặt trời quanh Nam Cực! Vòng sáu: Cá Heo bắt cá cùng ngư dân Bra-xin, giúp họ bắt được cá cao gấp mười bảy lần! Vòng bảy: tin đồn gấu nước còn sống trên Mặt Trăng bị khoa học... bắn hạ bằng súng khí! Lửng Mật thì sao? Lần đầu tiên trong đời... chịu thừa nhận mình chưa chắc đúng! [laughter] Chung kết: ai giúp ích cho loài người nhiều nhất? Sữa Thú Mỏ Vịt diệt khuẩn, nọc độc có thể thành thuốc chữa tiểu đường! [surprise-wa] Và nhà vô địch là... con vật từng bị các nhà khoa học tưởng là đồ giả khâu ghép! [question-ah] Bạn có đồng ý không? Xem trọn tám vòng thi trong video dài nhé, vì ở đây chỉ có mười quái kiệt, tám vòng thi, và một chiếc vương miện!
```

**Whisper prompt:** `Đại Hội Sinh Tồn, Vẽ Chuyện Hoang Dã, Lửng Mật, Tôm Tít, Gấu Nước, Chồn Gu-lô, Chim Cánh Cụt, Rái Cá Biển, Cá Heo, Chim Bồ Nông, Thú Mỏ Vịt, Cô-a-la, Ka-la-ha-ri, Ta-xma-ni-a, Uai-ô-minh, Cô-lô-ra-đô, Mi-si-gân, A-đê-li, Pa-na-ma, Ây-rơ, La-gu-na, Bra-xin, Bây-li, Ê-li, A-lát-xca, Crô-di-ê, Bê-rê-sít, Shơ-li Tem-pồ, Đi-súp, Ê-bớt, Gờ-lờ-pê-một, in-su-lin`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| mười hai ki-lô-gam | 12kg |
| năm mươi ki-lô-gam | 50kg |
| hai giây | 2 giây |
| Năm hai ngàn mười bốn | Năm 2014 |
| năm hai ngàn mười bốn | năm 2014 |
| âm ba mươi độ C | -30°C |
| ba mươi hai độ C | 32°C |
| ba mươi độ C | 30°C |
| năm độ C | 5°C |
| không độ C | 0°C |
| năm độ | 5 độ |
| không độ | 0 độ |
| Năm hai ngàn hai mươi ba | Năm 2023 |
| năm hai ngàn hai mươi ba | năm 2023 |
| Năm hai ngàn hai mươi tư | Năm 2024 |
| Năm hai ngàn hai mươi hai | Năm 2022 |
| năm hai ngàn hai mươi mốt | năm 2021 |
| Năm hai ngàn hai mươi | Năm 2020 |
| năm hai ngàn hai mươi | năm 2020 |
| Năm hai ngàn mười chín | Năm 2019 |
| năm hai ngàn mười tám | năm 2018 |
| Năm hai ngàn mười sáu | Năm 2016 |
| Năm hai ngàn mười ba | Năm 2013 |
| năm hai ngàn lẻ chín | năm 2009 |
| năm hai ngàn lẻ bốn | năm 2004 |
| năm hai ngàn lẻ một | năm 2001 |
| Năm một ngàn chín trăm chín mươi | Năm 1990 |
| Năm một ngàn chín trăm tám mươi chín | Năm 1989 |
| năm một ngàn chín trăm mười chín | năm 1919 |
| Năm một ngàn tám trăm bốn mươi | Năm 1840 |
| bốn mươi sáu lần | 46 lần |
| mười lăm phút | 15 phút |
| năm tiếng | 5 tiếng |
| năm trăm sáu mươi hai | 562 |
| một mét | 1 mét |
| hai mét | 2 mét |
| hai mươi lăm con | 25 con |
| mười bốn cây số | 14km |
| hai mươi bảy cây số | 27km |
| năm mươi cái hố | 50 cái hố |
| sáu con | 6 con |
| số tám mươi | số 80 |
| tám trăm cây số | 800km |
| Chín mươi năm | 90 năm |
| hai trăm năm | 200 năm |
| bảy mươi xăng-ti-mét | 70cm |
| mười ba ngàn cây số | 13.000km |
| mười bảy ngàn sáu trăm cây số | 17.600km |
| bốn mươi vòng | 40 vòng |
| Bảy mươi hai vòng | 72 vòng |
| một trăm ngàn | 100.000 |
| một trăm chín mươi sáu con | 196 con |
| gần gấp ba lần | gần gấp 3 lần |
| Bốn con | 4 con |
| năm mươi tiếng | 50 tiếng |
| hai ngàn tám trăm con | 2.800 con |
| năm mươi đến bảy mươi xăng-ti-mét | 50 đến 70cm |
| bốn trăm thợ săn | 400 thợ săn |
| chín nước | 9 nước |
| mười bảy lần | 17 lần |
| gấp bốn lần | gấp 4 lần |
| mười ba phần trăm | 13% |
| một trăm năm | 100 năm |
| năm mươi ba | 53 |
| sáu thủy cung | 6 thủy cung |
| hai mươi năm sáu tháng | 20 năm 6 tháng |
| hai mươi năm | 20 năm |
| mười đến một trăm con | 10 đến 100 con |
| hai ngàn con | 2.000 con |
| một trăm năm mươi ngàn | 150.000 |
| sáu mươi trận | 60 trận |
| mười hai loại | 12 loại |
| mười hai ngăn | 12 ngăn |
| Năm trăm mét | 500 mét |
| Bảy trăm | 700 |
| Tám trăm | 800 |
| tám trăm hai mươi lăm mét | 825m |
| hai lần | 2 lần |
| một ngàn năm | 1.000 năm |
| chín mươi lăm phần trăm | 95% |
| ba cây số | 3km |
| bốn mươi phần trăm | 40% |
| sáu tấn | 6 tấn |
| Gờ-lờ-pê-một | GLP-1 |
| in-su-lin | insulin |
| Ka-la-ha-ri | Kalahari |
| Ta-xma-ni-a | Tasmania |
| Uai-ô-minh | Wyoming |
| Cô-lô-ra-đô | Colorado |
| Mi-si-gân | Michigan |
| Rốc-ky | Rocky |
| Tê-tôn | Teton |
| A-đê-li | Adélie |
| Duy-moong Đuy-vin | Dumont d'Urville |
| A-đen | Adèle |
| Pa-na-ma | Panama |
| Nây-chơ | Nature |
| Ây-rơ | Eyre |
| Shơ-li Tem-pồ | Shirley Temple |
| Ca-li-phoóc-ni-a | California |
| Phlo-ri-đa | Florida |
| Bra-xin | Brazil |
| La-gu-na | Laguna |
| Tan-da-ni-a | Tanzania |
| Bây-li | Bailey |
| Ê-li | Allie |
| Bơ-mu-đa | Bermuda |
| A-lát-xca | Alaska |
| Crô-di-ê | Crozier |
| Bê-rê-sít | Beresheet |
| I-xra-en | Israel |
| Ma-xa-chu-xét | Massachusetts |
| Ca-na-đa | Canada |
| Ê-bớt | Airbus |
| cac-bon | carbon |
| Đi-súp | Dsup |
| hóc-môn | hormone |
| la-de | laser |
| Cô-a-la | Koala |
| Gu-lô | Gulo |
| ba phần mười mi-li-mét | 0,3mm |
| hai mi-li-mét | 2mm |
| hai phần mười giây | 0,2 giây |
| ba mươi lần | 30 lần |
| một hai phút | 1-2 phút |
| Năm hai ngàn mười hai | Năm 2012 |
| năm hai ngàn mười một | năm 2011 |
| Năm hai ngàn mười một | Năm 2011 |
| hai mươi chú | 20 chú |
| mười lăm ngày | 15 ngày |
| mười ngàn lần | 10.000 lần |
| bốn giây | 4 giây |
| mười một tiếng | 11 tiếng |
| tám tiếng | 8 tiếng |
| ba ngày | 3 ngày |
| hai cây số | 2km |
| mười bốn tháng | 14 tháng |
| hai mươi mét | 20 mét |
| chín lớp | 9 lớp |
| một đến ba trứng | 1 đến 3 trứng |
| mười ngày | 10 ngày |
| sáu đến tám tháng | 6 đến 8 tháng |
| mười chín cá heo | 19 cá heo |
| chín, mười tuần | 9-10 tuần |
| mười một đến mười bốn phần trăm | 11 đến 14% |
| bảy điểm | 7 điểm |
| sáu điểm | 6 điểm |
| tám điểm | 8 điểm |
| mười bốn điểm | 14 điểm |
| bốn điểm | 4 điểm |
| ba điểm | 3 điểm |
| hai điểm | 2 điểm |
| một điểm | 1 điểm |
| Xen-ca | Selka |
| một trăm năm mươi đến hơn sáu trăm ki-lô-gam | 150 đến hơn 600kg |
| hai mét rưỡi | 2,5 mét |
| một đến hai ký | 1-2kg |
| một mi-li-mét | 1mm |
| mười chú Cô-a-la | 10 chú Koala |
| mười năm | 10 năm |
| chín mươi phần trăm | 90% |
| mười đến mười hai tiếng | 10-12 tiếng |
| một trăm năm mươi đến hai trăm cây số | 150-200km |
| năm trăm ngàn lần | 500.000 lần |
| mười hai ngày | 12 ngày |
| Chín trăm | 900 |
| chín trăm mét | 900 mét |
| năm một ngàn chín trăm bảy mươi | năm 1970 |
| tám trăm hai mươi lần | 820 lần |
| năm hai ngàn mười bảy | năm 2017 |
| sáu mươi bảy tuổi | 67 tuổi |
| Sáu mươi bảy năm | 67 năm |
| bốn con | 4 con |
| bốn mươi tám tuổi | 48 tuổi |
| hai mươi bốn tuổi | 24 tuổi |
| hai mươi mốt tuổi | 21 tuổi |
| ba đến tám năm | 3-8 năm |
| chín mươi ngàn lần | 90.000 lần |
| mười một chú | 11 chú |
| ba mươi mốt giây | 31 giây |
| mười giây | 10 giây |
| bảy mươi lăm lần | 75 lần |
| một ngàn sáu trăm lần | 1.600 lần |
| năm một ngàn chín trăm mười một | năm 1911 |
| một đến hai ngàn con | 1.000 đến 2.000 con |
| một ngàn con | 1.000 con |
| một trăm ngàn con | 100.000 con |
| mười hai tháng Hai năm hai ngàn hai mươi hai | 12/2/2022 |
| tháng Mười Một năm hai ngàn hai mươi ba | tháng 11/2023 |
| Tháng Mười Một năm hai ngàn hai mươi ba | Tháng 11/2023 |
| Ních-lô | Nicklo |
| Xa-ra-xô-ta | Sarasota |
| Men-bơn | Melbourne |
| Pu-lô-xơ-qui-la | Pullosquilla |
| Glây-xi-ơ | Glacier |
| Phi-líp | Phillip |
| em năm mươi sáu | M56 |
| hàng triệu năm | hàng triệu năm |
| hàng trăm năm | hàng trăm năm |
| mỗi năm một vòng | mỗi năm một vòng |
| hàng ngàn năm | hàng ngàn năm |
| một ngàn nhà hàng | 1.000 nhà hàng |
| mười ngàn giấc | 10.000 giấc |
| hơn một năm | hơn một năm |
| một trăm ngàn chú | 100.000 chú |
| mười sáu loại | 16 loại |
| hàng trăm ngàn | hàng trăm ngàn |
| hai ngàn thành viên | 2.000 thành viên |
| Con số mười sáu | Con số 16 |
| hiểu lầm trăm năm | hiểu lầm trăm năm |
| ba mươi triệu năm | 30 triệu năm |
| Ba mươi triệu năm | 30 triệu năm |
| năm một ngàn bảy trăm bảy mươi ba | năm 1773 |
| Lu-bê-rông | Luberon |
| Me-li-vo-ra ca-pen-xít | Mellivora capensis |
| Me-li-vo-ra | Mellivora |
| ca-pen-xít | capensis |
| Pla-ti-pớt | Platypus |
| Ba năm sau | Ba năm sau |
| năm hai ngàn lẻ hai | năm 2002 |
| bốn mươi mét | 40 mét |
| hơn hai mươi mét | hơn 20 mét |
| Ba-ha-mát | Bahamas |
| Ra-ten | Ratel |
| U-gan-đa | Uganda |
| Gan-đa | Ganda |
| chín mươi năm | 90 năm |
| đồng đội trăm năm | đồng đội trăm năm |
| hai mươi mốt chú | 21 chú |
| I-rắc | Iraq |
| tháng Ba năm hai ngàn lẻ ba | tháng 3/2003 |
| hơn một trăm quả | hơn 100 quả |
| hơn hai trăm vật thể | hơn 200 vật thể |
| tám chú cá heo | 8 chú cá heo |
| mười bốn cây số mỗi đêm | 14km mỗi đêm |
| hai mươi hai tiếng | 22 tiếng |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · 10 QUÁI KIỆT BƯỚC VÀO ĐẠI HỘI SINH TỒN · 197.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.2 (8.2s) | L01 | Một sân vận động khổng lồ chìm trong bóng tối... Mười chiếc bục thi đấu đứng im lặng giữa sân. Và ở chính giữa, một chiếc vương miện bé xíu đang lặng lẽ phát sáng. |  | Sân vận động hoạt hình khổng lồ chìm trong bóng tối ban đêm, mười chiếc bục thi đấu tròn xếp vòng cung giữa sân, chính giữa là một chiếc vương miện vàng bé xíu tỏa sáng trên bệ đá; KHÔNG có anh MC trong cảnh này. |
| b02 | 00:08.2–00:14.9 (6.7s) | L02 | Đêm nay, mười sinh vật kỳ dị nhất từng bước qua kênh Vẽ Chuyện Hoang Dã sẽ quay trở lại. Nhưng lần này, không phải để kể chuyện của riêng mình... |  | Mười chiếc bóng đen bí ẩn của các con vật (lửng, rái cá, cá heo, thú mỏ vịt, bồ nông, gấu nước tí hon, tôm tít, chồn, cánh cụt, koala) đứng ngược sáng ở cửa đường hầm sân vận động, khói mờ quanh chân; KHÔNG có anh MC trong cảnh này. |
| b03 | 00:14.9–00:18.4 (3.5s) | L03 | mà để thi đấu với nhau, trực tiếp, trên cùng một sân chơi! |  | Cận cảnh mười đôi mắt sáng lóe trong bóng tối của đường hầm, to nhỏ khác nhau, nhìn thẳng ra phía trước đầy quyết tâm; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:18.4–00:22.4 (4.0s) | L04 | Bật đèn! Chào mừng toàn thể khán đài đến với Đại Hội Sinh Tồn lần thứ nhất! |  | Đèn sân vận động bật sáng rực, pháo giấy nổ tung, anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đứng giữa sân giơ cao micro vàng, khán đài chật kín các loài thú nhỏ (thỏ, sóc, ếch, chim sẻ) vẫy cờ hò reo. |
| b05 | 00:22.4–00:30.1 (7.6s) | L05 | Tôi là người dẫn chương trình đêm nay, và tôi xin hứa một điều: tất cả những gì bạn sắp nghe đều là chuyện chưa từng được kể trong mười tập phim lẻ. |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đặt tay lên ngực hứa hẹn, phía sau là mười tấm áp phích tập phim cũ treo trên tường bị đóng dấu "ĐÃ KỂ" bằng biểu tượng dấu tích (không chữ). |
| b06 | 00:30.1–00:34.0 (3.9s) | L06 | Hoàn toàn mới, có nguồn khoa học đàng hoàng, và... hơi điên rồ một chút! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng nháy mắt, tay kia giơ một chồng tạp chí khoa học dày cộp có hình kính hiển vi, vệ tinh và chim cánh cụt trên bìa (không chữ). |
| b07 | 00:34.0–00:38.1 (4.0s) | L07 | Luật chơi rất đơn giản. Tám vòng thi, mỗi vòng một thử thách sinh tồn khác nhau. |  | tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) hiện tám ô biểu tượng xếp thành hai hàng: nhiệt kế, đôi giày chạy, cái bát và đôi đũa, con mắt, chiếc nôi em bé, hai bàn tay nắm nhau, chiếc kính lúp, trái tim đỏ. |
| b08 | 00:38.1–00:46.7 (8.6s) | L08 | Chịu nóng và chịu lạnh. Chạy đường dài. Ăn uống. Giác quan. Nuôi con. Làm việc nhóm. Phúc khảo tin đồn. Và cuối cùng... ai giúp ích cho loài người nhiều nhất. |  | Tám ô biểu tượng lần lượt sáng lên như đèn sân khấu, ô cuối có trái tim đỏ phát sáng mạnh nhất; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng chỉ tay theo từng ô. |
| b09 | 00:46.7–00:54.5 (7.8s) | L09 | Mỗi vòng, giám khảo sẽ trao ba tấm huy chương. Vàng được 3 điểm, bạc được 2 điểm, đồng được 1 điểm. Ai nhiều điểm nhất sẽ đội vương miện! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ ngồi ở bàn giám khảo trên cao, trước mặt là ba chiếc huy chương vàng, bạc, đồng lấp lánh xếp thành hàng, bà giơ một cánh ra hiệu nghiêm túc. |
| b10 | 00:54.5–00:58.8 (4.4s) | L10 | Giám khảo xin nhắc: không cắn, không đấm, không xịt mùi hôi vào đối thủ! |  | Cận cảnh bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ chỉnh kính, gõ búa gỗ xuống bàn, vẻ mặt nghiêm khắc. |
| b11 | 00:58.8–01:03.9 (5.0s) | L11 | Nghe rõ chưa, toàn thể tuyển thủ? Đặc biệt là... một vài cá nhân có tiền sử hơi nóng tính! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng liếc mắt nhìn sang chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần, chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh và chú Tôm Tít (peacock mantis |
| b12 | 01:03.9–01:06.7 (2.9s) | L12 | Và bây giờ, xin mời các tuyển thủ bước ra sân! |  | Cửa đường hầm mở toang, ánh đèn sân khấu chiếu thẳng vào lối đi trải thảm đỏ, khói trắng phun hai bên; KHÔNG có anh MC trong cảnh này. |
| b13 | 01:06.7–01:11.5 (4.7s) | L13 | Tuyển thủ số một! Nặng chưa tới 12kg! Từng nhai rắn hổ mang như nhai bim bim! |  | chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần bước ra thảm đỏ, đeo kính râm, vung tay chào khán đài đầy ngông nghênh, đèn flash nháy khắp nơi; KHÔNG có anh MC trong cảnh này. |
| b14 | 01:11.5–01:14.8 (3.4s) | L14 | Lửng Mật! Tuyển thủ số hai! Võ sĩ có cú đấm nhanh nhất đại dương! Tôm Tít! |  | chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh được đẩy ra trong một bể nước tròn có bánh xe, giơ hai càng búa như võ sĩ quyền anh khoe găng; KHÔNG có anh MC trong cảnh này. |
| b15 | 01:14.8–01:19.5 (4.6s) | L15 | Tuyển thủ số ba! Kẻ bất tử tí hon! Gấu Nước! Ban tổ chức phải phát kính lúp cho khán giả mới nhìn thấy cậu ấy! |  | Khán giả trên khán đài đồng loạt cầm kính lúp to soi xuống sân, trong vòng tròn kính lúp là chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương đang vẫy tay chào; KHÔNG có anh MC trong cảnh này. |
| b16 | 01:19.5–01:22.6 (3.1s) | L16 | Tuyển thủ số bốn! Gã liều mạng xứ tuyết! Chồn Gulo! |  | chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh bước ra, lông dựng đứng, nhe răng cười, tuyết rơi lất phất quanh người; KHÔNG có anh MC trong cảnh này. |
| b17 | 01:22.6–01:27.5 (4.9s) | L17 | Tuyển thủ số năm, quý ông mặc vest của Nam Cực, Chim Cánh Cụt! Số sáu, Rái Cá Biển! Số bảy, |  | Ba tuyển thủ cùng ra: chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ đi lạch bạch chỉnh nơ, chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách nằm ngửa trên chiếc phao, chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cườ |
| b18 | 01:27.5–01:31.7 (4.2s) | L18 | Cá Heo! Tuyển thủ số tám, Chim Bồ Nông, và cái mỏ đi trước chủ nhân... 2 giây! |  | chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn bước ra, chiếc mỏ dài thò vào khung hình trước, thân mình đi theo sau, khán giả hàng đầu ngửa người né; KHÔNG có anh MC trong cảnh này. |
| b19 | 01:31.7–01:34.8 (3.0s) | L19 | Tuyển thủ số chín, Thú Mỏ Vịt! Và tuyển thủ số mười... |  | chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá lạch bạch bước ra vẫy cái đuôi dẹt; bên cạnh, ô cửa đường hầm thứ mười vẫn tối om; KHÔNG có anh MC trong cảnh này. |
| b20 | 01:34.8–01:39.1 (4.3s) | L20 | Tuyển thủ số mười... xin lỗi toàn thể khán đài, tuyển thủ số mười hiện vẫn đang ngủ. |  | Một nhân viên hoạt hình đẩy chiếc xe đẩy chở nguyên một cành cây khuynh diệp ra sân, trên cành là chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ ôm cây ngủ say, bong bóng ngủ phồng ở mũi; KHÔNG có anh MC trong cảnh này. |
| b21 | 01:39.1–01:43.4 (4.3s) | L21 | Ủa... đến lượt cháu chưa ạ? Cháu vừa mơ thấy một cái cây to ơi là to! |  | Cận cảnh chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ mở một mắt lơ mơ, lông tai rối bù, ngáp dài; KHÔNG có anh MC trong cảnh này. |
| b22 | 01:43.4–01:52.7 (9.3s) | L22 | Rồi, Gấu Koala cũng đã có mặt! Nhưng trước khi xem dự đoán, theo đúng truyền thống của mọi giải đấu lớn, chúng ta có... lễ cân ký! Mời các tuyển thủ lần lượt bước lên bàn cân. |  | Một chiếc cân bàn khổng lồ hoạt hình kiểu võ đài quyền anh giữa sân, có kim chỉ tròn to, hai bên là đèn flash và phóng viên; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đứng cạnh cầm micro. |
| b23 | 01:52.7–01:59.8 (7.1s) | L23 | Cá Heo bước lên! Kim cân quay vù vù! Một chú cá heo mũi chai trưởng thành có thể nặng từ 150 đến hơn 600kg! Tuyển thủ nặng ký nhất đại hội! |  | chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái nằm trên chiếc cân bàn đặt trong bể nước, kim cân quay mấy vòng, chiếc cân kêu cót két, phóng viên lùi lại; KHÔNG có anh MC trong cảnh này. |
| b24 | 01:59.8–02:05.5 (5.7s) | L24 | Chim Bồ Nông bước lên! Cân nặng thì vừa phải, nhưng đôi cánh dang ra dài hơn 2,5 mét! Ban tổ chức phải mở rộng cả cửa |  | chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn đứng trên cân dang rộng đôi cánh dài quá cả khung cửa, đầu cánh đập trúng hai nhân viên đứng hai bên; KHÔNG có anh MC trong cảnh này. |
| b25 | 02:05.5–02:12.7 (7.1s) | L25 | phòng cân! Rái Cá Biển bước lên, ôm theo hòn đá! Ban tổ chức yêu cầu bỏ hòn đá ra. Rái Cá... từ chối. Thôi, cân luôn cả đá! |  | chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách đứng trên cân ôm chặt hòn đá xám vào ngực, lắc đầu nguầy nguậy, nhân viên cân giơ tay bất lực; KHÔNG có anh MC trong cảnh này. |
| b26 | 02:12.7–02:20.7 (8.0s) | L26 | Lửng Mật và Chồn Gulo bước lên cùng lúc, vì không ai chịu nhường ai. Hai gã nặng chừng một bao gạo nhỏ, nhưng nhìn cách hai gã gườm nhau thì... tưởng nặng |  | chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần và chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh cùng chen nhau trên một chiếc cân, trán chạm trán gườm gườm như hai võ sĩ trước trận đấu, kim cân ru |
| b27 | 02:20.7–02:27.7 (7.1s) | L27 | cả tấn! Chim Cánh Cụt, Koala, Thú Mỏ Vịt lần lượt bước lên. Thú Mỏ Vịt nhẹ nhất trong ba bạn, chỉ khoảng 1-2kg, nhẹ hơn cả một con mèo |  | Ba chiếc cân nhỏ xếp hàng: chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ đứng thẳng chỉnh nơ, chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ ôm cây cột cân ngủ gật, chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt m |
| b28 | 02:27.7–02:38.9 (11.1s) | L28 | nhà. Tôm Tít bước lên, dài chưa tới một gang tay. Và cuối cùng... Gấu Nước. Kim cân không nhúc nhích. Chiếc cân điện tử cũng không nhúc nhích. Ban tổ chức phải mang tới... một chiếc kính hiển vi. |  | chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương tí hon đứng giữa chiếc cân bàn khổng lồ trống trơn, nhân viên cúi sát soi kính lúp, màn hình cân hiện số không tròn trĩnh; KHÔNG có anh MC trong cảnh này. |
| b29 | 02:38.9–02:46.9 (8.0s) | L29 | Gấu Nước dài chưa tới 1mm. Chênh lệch giữa tuyển thủ nặng nhất và nhẹ nhất đại hội lớn đến mức... các nhà toán học của ban tổ chức đã xin nghỉ phép. | **< 1 MM** · Gấu Nước · R/360 · [0.5, 0.6] | Một nhà toán học hoạt hình đeo kính đứng trước tấm bảng đen kín đặc những con số và mũi tên, tóc dựng đứng, ôm đầu, phía sau là hình so sánh chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái khổng lồ và chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương như một chấm nhỏ; KHÔ |
| b30 | 02:46.9–02:52.2 (5.4s) | L30 | Cân ký xong! Đủ mười tuyển thủ! Và trước khi vào vòng một, chúng ta cùng xem dự đoán của các chuyên gia. |  | Mười tuyển thủ đứng thành hàng ngang giữa sân dưới pháo hoa, chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ đứng ngủ gật dựa vào vai chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá; anh MC hoạt hình vest đỏ nơ bướm v |
| b31 | 02:52.2–03:01.1 (8.9s) | L31 | Theo dự đoán, Lửng Mật, Tôm Tít và Gấu Nước là ba ứng cử viên nặng ký nhất. Còn Thú Mỏ Vịt và Koala... chuyên gia chỉ ghi chú đúng một câu: tham gia cho vui. |  | Màn hình lớn chiếu biểu đồ cột dự đoán: ba cột cao vút có hình đầu chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần, chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh, chú Gấu Nước (tardi |
| b32 | 03:01.1–03:08.0 (6.9s) | L32 | Nhưng các chuyên gia đâu phải lúc nào cũng đúng. Đêm nay, mọi con số sẽ được kiểm chứng lại từ đầu. Không có chuyện cũ. Không có huyền thoại. |  | Cận cảnh chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá lặng lẽ ngước nhìn cột điểm thấp tè của mình trên màn hình, ánh mắt quyết tâm lóe sáng, một giọt mồ hôi chảy trên trán; KHÔNG có anh MC trong cảnh này. |
| b33 | 03:08.0–03:12.2 (4.2s) | L33 | Chỉ có khoa học, chỉ có những bằng chứng được đo đạc thật... và một chiếc vương miện. |  | Chiếc vương miện bé xíu trên bệ đá giữa sân phát sáng rực rỡ, mười cái bóng tuyển thủ in dài trên mặt sân hướng về phía nó; KHÔNG có anh MC trong cảnh này. |
| b34 | 03:12.2–03:17.7 (5.4s) | L34 | Vòng một bắt đầu ngay sau đây, và nó sẽ khiến các tuyển thủ... hoặc là đóng băng, hoặc là chín luôn! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng chỉ tay về phía cổng sân vận động chia đôi: một nửa phủ băng tuyết xanh lạnh buốt có nhũ băng, một nửa tỏa nắng đỏ rực như sa mạc có ảo ảnh hơi nóng. |

### scene02 · THỬ THÁCH NÓNG VÀ LẠNH — AI GIỮ ẤM, AI GIẢI NHIỆT GIỎI NHẤT · 346.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.3 (8.3s) | L35 | Vòng một: thử thách nóng và lạnh! Câu hỏi rất đơn giản: khi trời nóng như lò nướng, hoặc lạnh như tủ đá, cơ thể bạn làm gì để sống sót? |  | Sân thi đấu được chia đôi: nửa trái là sa mạc đỏ rực có mặt trời chói chang và ảo ảnh hơi nóng, nửa phải là băng tuyết xanh trắng có nhũ băng; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đứng ngay đường ranh giữa hai nửa, một bên tóc dựng vì nóng, một bên râu đóng băng. |
| b02 | 00:08.3–00:13.6 (5.3s) | L36 | Ban giám khảo không chấm ai to khỏe nhất. Ban giám khảo chấm ai thông minh nhất trong việc điều khiển nhiệt độ của chính mình. |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ cầm một chiếc nhiệt kế khổng lồ như cây gậy chỉ huy, trước mặt là bảng chấm điểm có biểu tượng bộ não và nhiệt kế (không chữ). |
| b03 | 00:13.6–00:19.9 (6.3s) | L37 | Phần thi nóng mở màn. Và người đầu tiên bước vào sân là một tuyển thủ mà ai cũng nghĩ là... sẽ ngủ gật ngay lập tức. |  | Nửa sân sa mạc nóng rực, chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ đứng đơ trên cát, mồ hôi nhễ nhại, tay cầm chiếc quạt giấy nhỏ, mặt ngơ ngác nhìn mặt trời; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:19.9–00:25.6 (5.8s) | L38 | Hồ sơ tuyển thủ Gấu Koala. Bộ lông: dày. Nơi ở: trên cây, không có hang, không có điều hòa. Kế hoạch chống nóng: chưa rõ. |  | Một tấm hồ sơ kẹp giấy hoạt hình có ảnh chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ ở góc, bên dưới là ba biểu tượng: bộ lông, cái cây, chiếc máy điều hòa bị gạch chéo đỏ (không chữ); KHÔNG có anh MC trong cảnh này. |
| b05 | 00:25.6–00:30.4 (4.8s) | L39 | Nhưng các nhà khoa học ở Úc đã phát hiện ra một bí mật mà chính Koala giữ kín suốt hàng triệu năm. |  | Hai nhà khoa học hoạt hình đội mũ rộng vành đứng dưới gốc cây, chĩa chiếc máy ảnh nhiệt to bản lên ngọn cây nơi chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ đang ngồi; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:30.4–00:35.8 (5.4s) | L40 | Năm 2014, họ mang máy ảnh nhiệt vào rừng, theo dõi những con Koala hoang dã trong những ngày nắng gắt trên 30°C. |  | Màn hình máy ảnh nhiệt hiện cảnh rừng cây màu đỏ cam nóng rực, chính giữa là hình chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ màu vàng cam đang leo xuống thấp; KHÔNG có anh MC trong cảnh này. |
| b07 | 00:35.8–00:43.1 (7.3s) | L41 | Và họ thấy một hành động rất lạ: trời càng nóng, Koala càng leo xuống thấp, rồi dang tay dang chân... ôm chặt lấy thân cây như ôm gối ôm! |  | chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ nằm sấp ôm chặt thân cây to bằng cả tay lẫn chân, má áp vào vỏ cây, vẻ mặt sung sướng mãn nguyện như đang ôm gối ôm mát lạnh; KHÔNG có anh MC trong cảnh này. |
| b08 | 00:43.1–00:50.1 (7.1s) | L42 | Hình ảnh nhiệt cho thấy lý do: thân cây keo mát hơn không khí xung quanh hơn 5°C. Koala đang dùng cái cây như một chiếc tủ lạnh khổng lồ! | **-5°C** · thân cây mát hơn · R/360 · [0.55, 0.5] | Ảnh nhiệt chia đôi: không khí xung quanh màu đỏ rực, riêng thân cây màu xanh dương mát lạnh, chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ áp bụng vào phần xanh; một chiếc tủ lạnh hoạt hình nhỏ vẽ cạnh để so sánh; KHÔNG có anh MC trong cảnh này. |
| b09 | 00:50.1–00:58.1 (8.0s) | L43 | Và đây không phải ôm cho vui. Theo tính toán của các nhà khoa học, chỉ riêng việc ôm cây đã giúp Koala tiết kiệm khoảng một nửa lượng nước cần để làm mát cơ thể trong một ngày nóng. | **1/2** · nước làm mát · L/380 · [0.7, 0.5] | Hai giọt nước hoạt hình so sánh: giọt bên trái to (không ôm cây), giọt bên phải chỉ còn một nửa (có ôm cây), chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ giơ ngón cái tự hào; KHÔNG có anh MC trong cảnh này. |
| b10 | 00:58.1–01:07.7 (9.5s) | L44 | Điều buồn cười nhất: cây keo này Koala không hề ăn. Nó leo sang cây keo chỉ để... ôm cho mát, xong lại leo về cây khuynh diệp để ăn. Một cây làm phòng ăn, một cây làm phòng điều hòa! |  | Hai cái cây đứng cạnh nhau có cầu thang dây nối giữa: cây khuynh diệp bên trái có biểu tượng cái đĩa và đôi đũa, cây keo bên phải có biểu tượng bông tuyết; chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ đang leo qua cầu thang dây từ cây này sang cây kia; KHÔNG có anh MC trong cảnh này. |
| b11 | 01:07.7–01:16.1 (8.4s) | L45 | Nhưng chống nóng mới chỉ là một nửa. Nửa còn lại là chuyện... uống nước. Trong hàng trăm năm, người ta tin rằng Koala lấy gần hết nước từ lá, chỉ uống khi nắng nóng khắc |  | Một cuốn sách cổ dày bụi mở ra, trang sách vẽ hình chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ ôm chiếc lá to và một ly nước bị gạch chéo; một ngọn nến cháy leo lét bên cạnh; KHÔNG có anh MC trong cảnh này. |
| b12 | 01:16.1–01:22.5 (6.4s) | L46 | nghiệt. Cho đến năm 2020, khi một nhóm nhà khoa học tập hợp 46 lần quan sát Koala hoang dã... đang uống nước. | **46 LẦN** · quan sát uống nước · R/380 · [0.6, 0.5] | Một tấm bản đồ nước Úc ghim nhiều đinh ghim đỏ đánh dấu chỗ quan sát, bên cạnh là chồng ảnh chụp chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ; KHÔNG có anh MC trong cảnh này. |
| b13 | 01:22.5–01:31.2 (8.7s) | L47 | Và cách uống thì... không giống ai. Khi trời mưa, nước chảy thành dòng dọc theo thân cây trơn. Koala ôm cây, thè lưỡi... và liếm từng dòng nước mưa từ trên xuống! |  | Trời mưa lất phất, dòng nước chảy dọc thân cây khuynh diệp nhẵn, chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ ôm cây thè lưỡi liếm nước, mắt nhắm tận hưởng như đang uống nước suối; KHÔNG có anh MC trong cảnh này. |
| b14 | 01:31.2–01:39.6 (8.4s) | L48 | Có một cô Koala mẹ đã uống liên tục như thế suốt 15 phút không nghỉ. Cây cối với Koala vừa là nhà, vừa là bếp, vừa là điều hòa, vừa là... vòi nước! |  | Một cái cây hoạt hình được vẽ như căn hộ nhiều tầng: tầng trên là bếp lá, tầng giữa là điều hòa bông tuyết, tầng dưới là vòi nước, chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ mẹ cõng con nhỏ trên lưng ở giữa; KHÔNG có anh MC trong cảnh này. |
| b15 | 01:39.6–01:44.0 (4.4s) | L49 | Giám khảo ghi nhận: chiến thuật tiết kiệm, khoa học, và... rất đáng yêu. |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gật đầu ghi chép, đặt một ngôi sao vàng nhỏ lên bảng cạnh hình đầu chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ. |
| b16 | 01:44.0–01:53.0 (9.0s) | L50 | Phần thi nóng tiếp theo, chúng ta có hai tuyển thủ đến từ biển lạnh. Rái Cá Biển và Chim Cánh Cụt đều đứng nhìn nửa sân sa mạc với ánh mắt... không mấy thiện cảm. |  | chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách và chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ đứng ở mép sân sa mạc, nhìn mặt trời chói chang, cả hai đổ mồ hôi, chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng  |
| b17 | 01:53.0–01:59.0 (6.0s) | L51 | Hai bạn xin phép chuyển sang phần thi lạnh. Và giám khảo đồng ý, vì phần thi lạnh mới là chiến trường thật sự! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng mở cánh cửa lớn dẫn sang nửa sân băng tuyết, gió lạnh thổi tung cà vạt của anh, chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách và chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ vui mừn |
| b18 | 01:59.0–02:05.8 (6.9s) | L52 | Phần thi lạnh. Nhiệt độ nước: gần bằng 0°C. Ở mức này, một con người không được bảo hộ chỉ trụ được rất ngắn trước khi cơ thể bắt đầu mất kiểm | **0°C** · nước gần đóng băng · R/380 · [0.75, 0.55] | Một hồ nước băng giá đen sẫm có những tảng băng trôi, bên cạnh là chiếc nhiệt kế khổng lồ chỉ ở vạch thấp nhất màu xanh, hơi lạnh bốc lên mờ mờ; KHÔNG có anh MC trong cảnh này. |
| b19 | 02:05.8–02:12.7 (6.9s) | L53 | soát. Tuyển thủ đầu tiên nhảy xuống, và cả sân vận động cùng... há hốc mồm. Không phải Rái Cá, không phải Cánh Cụt. Mà là Thú Mỏ Vịt! |  | chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá đeo băng đô xanh lao người nhảy xuống hồ băng tõm một cái, nước bắn tung tóe; trên khán đài, đám khán giả thú nhỏ há hốc mồm sững sờ; KHÔNG có anh MC trong cảnh này. |
| b20 | 02:12.7–02:17.6 (4.9s) | L54 | Tin khẩn từ hồ băng: tuyển thủ được dự đoán "tham gia cho vui" vừa nhảy xuống nước lạnh nhất sân! |  | Cô phát thanh viên hoạt hình ngồi sau bàn tin tức, chỉ tay vào màn hình phía sau đang chiếu cảnh chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá bơi giữa hồ băng; KHÔNG có anh MC trong cảnh này. |
| b21 | 02:17.6–02:27.2 (9.6s) | L55 | Nhiều người quên mất rằng Thú Mỏ Vịt không chỉ sống ở những con suối ấm. Ở đảo Tasmania và những dòng sông trên núi cao nước Úc, mùa đông nước sông lạnh gần bằng 0°C. |  | Một dòng sông trên núi tuyết hoạt hình, hai bờ phủ tuyết trắng, mặt nước có vài mảng băng mỏng, chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá ló đầu lên từ giữa dòng; KHÔNG có anh MC trong cảnh này. |
| b22 | 02:27.2–02:34.4 (7.2s) | L56 | Các nhà khoa học đã gắn thiết bị đo nhiệt độ vào những con Thú Mỏ Vịt hoang dã và theo dõi chúng suốt mùa đông. Kết quả khiến họ phải đo lại mấy |  | Một nhà khoa học hoạt hình đeo kính cầm máy đo nhiệt độ cầm tay, nhìn màn hình rồi dụi mắt, nhìn lại lần nữa vẻ không tin nổi; KHÔNG có anh MC trong cảnh này. |
| b23 | 02:34.4–02:43.2 (8.8s) | L57 | lần. Một con Thú Mỏ Vịt đã bơi trong dòng nước 0°C ở một con sông đóng băng một phần suốt ít nhất 5 tiếng liền, mà nhiệt độ cơ thể vẫn giữ nguyên, không hề tụt. | **5 GIỜ** · bơi trong nước 0°C · L/360 · [0.6, 0.55] | chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá bơi thong thả giữa dòng sông có những mảng băng trôi, bên cạnh là chiếc đồng hồ cát lớn đang chảy, quanh người là vầng hào quang màu cam ấm áp; KHÔNG có anh MC trong cảnh này. |
| b24 | 02:43.2–02:47.6 (4.4s) | L58 | Và nhiệt độ cơ thể ấy là bao nhiêu? Chỉ khoảng 32°C, thấp hơn người chúng ta khoảng | **32°C** · thân nhiệt mỏ vịt · R/380 · [0.62, 0.5] | Hai chiếc nhiệt kế đặt cạnh nhau: nhiệt kế của người hoạt hình cao hơn, nhiệt kế của chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá thấp hơn một đoạn, chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá nhún vai tỉnh bơ; KHÔNG có anh MC tr |
| b25 | 02:47.6–02:54.2 (6.6s) | L59 | 5 độ. Tức là Thú Mỏ Vịt chạy máy sưởi ở mức tiết kiệm điện... mà vẫn ấm áp giữa nước đá. Nghe như quảng cáo điều hòa inverter! |  | chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá đeo kính râm nằm ngửa thư giãn giữa nước đá, trên bụng có một biểu tượng hình chiếc pin xanh lá đầy năng lượng và chiếc lá nhỏ tiết kiệm điện; KHÔNG có anh MC trong cảnh này. |
| b26 | 02:54.2–03:01.2 (7.0s) | L60 | Bí quyết nằm ở ba lớp bảo vệ. Thứ nhất là bộ lông: lớp lông tơ xoăn tít bên dưới giữ lại một lớp không khí sát da, giống chiếc áo phao bằng không khí. |  | Hình phóng to lát cắt bộ lông chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá: lớp lông tơ xoăn tít bên dưới kẹp những bong bóng khí nhỏ li ti, lớp lông dài bóng phía trên; nước xanh không chạm được vào da; KHÔNG có anh MC trong cảnh này. |
| b27 | 03:01.2–03:05.9 (4.7s) | L61 | Theo các nhà nghiên cứu, khả năng cách nhiệt của bộ lông này còn cao hơn cả lông gấu Bắc Cực và lông hải ly! |  | Ba chiếc áo khoác lông treo trên giá: áo gấu Bắc Cực, áo hải ly và áo Thú Mỏ Vịt; áo Thú Mỏ Vịt được gắn một chiếc huy hiệu ngôi sao vàng lấp lánh; KHÔNG có anh MC trong cảnh này. |
| b28 | 03:05.9–03:13.7 (7.8s) | L62 | Thứ hai, ở gốc chân sau và gốc đuôi có một mạng lưới mạch máu đặc biệt, hoạt động như bộ trao đổi nhiệt: máu nóng chảy ra sưởi ấm cho máu lạnh chảy về, nên hơi ấm không bị thất thoát |  | Sơ đồ giải phẫu hoạt hình gốc đuôi chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá: hai ống mạch máu đỏ và xanh nằm sát nhau ngược chiều, những mũi tên nhiệt màu cam truyền từ ống đỏ sang ống xanh; KHÔNG có anh MC trong cảnh này. |
| b29 | 03:13.7–03:20.7 (7.0s) | L63 | ra nước. Và thứ ba: khi lạnh hơn, Thú Mỏ Vịt chỉ đơn giản là... đốt năng lượng nhiều hơn. Lò sưởi bên trong cứ thế cháy đều, không hề tắt. |  | Bên trong bụng chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá vẽ một chiếc lò sưởi nhỏ ấm áp có ngọn lửa cam đều đặn, bên ngoài là nước đá lạnh buốt; KHÔNG có anh MC trong cảnh này. |
| b30 | 03:20.7–03:25.7 (5.0s) | L64 | Giám khảo xin ghi nhận: tuyển thủ số chín... đã gây bất ngờ lớn đầu tiên của đêm nay. |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ tháo kính ra lau, rồi đeo lại nhìn chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá với vẻ nể phục, ghi một dấu tích to vào sổ. |
| b31 | 03:25.7–03:32.5 (6.8s) | L65 | Rái Cá Biển cũng không chịu thua. Không có lớp mỡ dày như hải cẩu, Rái Cá có một mẹo giữ ấm cực kỳ đơn giản mà khán giả có thể tự quan sát. |  | chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách nằm ngửa trên mặt nước băng giá, hai bàn tay trước và hai bàn chân sau đều giơ cao khỏi mặt nước như đang tạo dáng chụp ảnh; KHÔNG có anh MC trong cảnh này. |
| b32 | 03:32.5–03:39.3 (6.8s) | L66 | Khi nghỉ ngơi trên mặt nước, Rái Cá Biển giơ bàn tay và bàn chân lên khỏi mặt nước. Vì bàn tay ít lông, mà nước lại hút hơi nóng nhanh hơn không khí rất nhiều lần. |  | Hình so sánh hoạt hình: một bàn tay rái cá nhúng nước có những mũi tên nhiệt đỏ thoát ra rất nhiều; một bàn tay giơ lên không khí chỉ có vài mũi tên nhỏ; KHÔNG có anh MC trong cảnh này. |
| b33 | 03:39.3–03:46.1 (6.7s) | L67 | Đôi khi Rái Cá còn úp hai bàn tay lên mắt khi ngủ, trông như đang ngại ngùng, nhưng thật ra là đang... giữ ấm cho đôi bàn tay! |  | Cận cảnh chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách ngủ ngửa trên sóng, hai bàn tay úp lên mắt cực đáng yêu, một bong bóng suy nghĩ nhỏ vẽ chiếc găng tay len ấm áp; KHÔNG có anh MC trong cảnh này. |
| b34 | 03:46.1–03:52.8 (6.7s) | L68 | Tuyển thủ tiếp theo không cần nước lạnh. Hắn cần tuyết. Rất nhiều tuyết. Chồn Gulo bước vào khu băng giá, nhìn quanh... và bắt đầu |  | chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh đứng giữa vùng tuyết trắng mênh mông, hai chân trước đào tung tuyết như máy xúc, tuyết bay tứ tung; KHÔNG có anh MC trong cảnh này. |
| b35 | 03:52.8–03:59.1 (6.3s) | L69 | đào. Các nhà khoa học đã đánh dấu toàn bộ 562 hang sinh con của Chồn Gulo từng được tìm thấy ở Bắc Mỹ và Bắc Âu lên bản đồ vệ | **562 HANG** · được đánh dấu · R/380 · [0.6, 0.45] | Một tấm bản đồ vệ tinh Bắc bán cầu hoạt hình phủ những chấm đỏ nhỏ li ti đánh dấu hang, phần lớn nằm trên vùng tuyết trắng; KHÔNG có anh MC trong cảnh này. |
| b36 | 03:59.1–04:06.1 (7.0s) | L70 | tinh. Và kết quả trùng khớp đến kinh ngạc: tất cả các hang đều nằm ở nơi tuyết vẫn còn phủ dày cho đến cuối mùa xuân. Không có ngoại lệ. |  | Bản đồ vệ tinh phủ lớp màu trắng tuyết mùa xuân, toàn bộ chấm đỏ đều nằm gọn bên trong vùng trắng, một chiếc kính lúp soi vào chứng minh; KHÔNG có anh MC trong cảnh này. |
| b37 | 04:06.1–04:12.0 (5.8s) | L71 | Chồn mẹ đào đường hầm dưới lớp tuyết dày hơn 1 mét, có khi là cả một mê cung nhiều ngã rẽ, để sinh con giữa mùa đông. | **> 1 M** · lớp tuyết phủ · L/360 · [0.5, 0.4] | Mặt cắt ngang lớp tuyết dày hoạt hình: bên dưới là một mê cung đường hầm tuyết nhiều ngã rẽ, ở cuối là căn phòng nhỏ ấm áp có chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh mẹ ôm hai chú chồn con; KHÔNG có anh MC trong cảnh này. |
| b38 | 04:12.0–04:20.0 (8.0s) | L72 | Tuyết nghe thì lạnh, nhưng lớp tuyết dày lại là tấm chăn cách nhiệt tuyệt vời: bên ngoài gió bão gào thét, bên trong hang vẫn yên ổn như trong một chiếc túi ngủ. |  | Chia đôi khung hình theo chiều dọc: phía trên mặt tuyết là bão tuyết gió thổi mạnh; phía dưới trong hang tuyết là chồn con nằm ngủ ngon lành trong ánh sáng ấm áp; KHÔNG có anh MC trong cảnh này. |
| b39 | 04:20.0–04:27.0 (7.0s) | L73 | Và cũng vì thế mà Chồn Gulo sợ nhất là... mùa xuân đến quá sớm. Tuyết tan sớm thì hang sụp, nhà không còn, chồn con phơi mình giữa trời. |  | chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh ngồi buồn bã nhìn những giọt nước nhỏ từ trần hang tuyết đang tan chảy, mặt trời mùa xuân chiếu qua lỗ thủng; KHÔNG có anh MC trong cảnh này. |
| b40 | 04:27.0–04:31.6 (4.7s) | L74 | Kẻ dám cướp mồi của gấu xám lại có một nỗi lo mà ai nghe cũng thấy thương: lo trái đất ấm lên. |  | chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh cầm một chiếc nhiệt kế nhỏ, nhìn lên quả địa cầu đang đổ mồ hôi, vẻ mặt lo lắng; KHÔNG có anh MC trong cảnh này. |
| b41 | 04:31.6–04:39.1 (7.5s) | L75 | Và cuối cùng, tuyển thủ được đặt cược nhiều nhất vòng này: Gấu Nước, kẻ từng sống sót ở nhiệt độ thấp đến khó tin. Cậu ấy bước vào tủ |  | chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương tí hon tự tin bước vào một chiếc tủ đông khổng lồ có hơi lạnh tỏa ra, quay lại vẫy tay chào khán giả trước khi cửa đóng; KHÔNG có anh MC trong cảnh này. |
| b42 | 04:39.1–04:47.9 (8.9s) | L76 | đông... Năm 2022, các nhà khoa học Đức làm một thí nghiệm thú vị: cứ một tuần cho Gấu Nước đông đá ở -30°C, rồi tuần sau rã đông, cho ăn, rồi lại đông đá. | **-30°C** · mỗi tuần đông đá · R/360 · [0.4, 0.5] | Lịch treo tường hoạt hình có các tuần xen kẽ: tuần biểu tượng bông tuyết xanh, tuần biểu tượng chiếc bát thức ăn, lặp lại; bên cạnh là chiếc tủ đông và ống nghiệm; KHÔNG có anh MC trong cảnh này. |
| b43 | 04:47.9–04:54.0 (6.0s) | L77 | Lặp lại như vậy cho đến khi chúng chết vì tuổi già. Và nhóm Gấu Nước được đông đá sống lâu gấp đôi nhóm không đông đá! | **x2** · tuổi thọ · L/380 · [0.65, 0.4] | Hai cột thời gian so sánh: cột ngắn của Gấu Nước bình thường và cột dài gấp đôi của Gấu Nước đông đá có những khối băng xen kẽ; chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương đứng trên đỉnh cột dài; KHÔNG có anh MC trong cảnh này. |
| b44 | 04:54.0–04:59.2 (5.2s) | L78 | Nhưng phần thú vị nằm ở phép trừ: nếu bỏ đi thời gian nằm trong tủ đông, thì tuổi thọ của hai nhóm... bằng nhau. |  | Một phép tính hoạt hình trên bảng đen: cột dài trừ đi các khối băng bằng đúng cột ngắn, bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ cầm phấn gạch dấu bằng; KHÔNG có anh MC trong cảnh này. |
| b45 | 04:59.2–05:04.8 (5.6s) | L79 | Nghĩa là khi bị đông đá, Gấu Nước không già đi chút nào. Đồng hồ sinh học dừng hẳn, như nàng công chúa ngủ trong rừng! |  | chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương nằm ngủ trong khối băng trong suốt như chiếc giường công chúa, trên đầu có chiếc đồng hồ dừng kim, xung quanh là hoa hồng và gai leo hoạt hình; KHÔNG có anh MC trong cảnh này. |
| b46 | 05:04.8–05:10.3 (5.5s) | L80 | Giám khảo xin thông báo: tuyển thủ Gấu Nước hiện đang đông đá và... từ chối tham gia chấm điểm. |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gõ cửa chiếc tủ đông, bên trong chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương nằm im trong khối băng, đầu có biểu tượng "zzz"; KHÔNG có anh MC trong cảnh này. |
| b47 | 05:10.3–05:17.3 (7.0s) | L81 | Đúng vậy! Đông đá thì không già, nhưng cũng không thi được! Gấu Nước tự loại mình khỏi vòng một vì... ngủ quá ngon! |  | Khán đài cười nghiêng ngả, anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng ôm bụng cười, phía sau tủ đông là khối băng chứa chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương có dán miếng băng dính vẽ biểu tượng tạm dừng. |
| b48 | 05:17.3–05:22.7 (5.4s) | L82 | Và đây là kết quả vòng một! Huy chương đồng: Gấu Koala, bậc thầy ôm cây giải nhiệt và uống nước |  | Bục trao giải ba bậc: chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ đứng ở bậc đồng, cổ đeo huy chương đồng, tay vẫn ôm một khúc cây nhỏ, mặt ngơ ngác; KHÔNG có anh MC trong cảnh này. |
| b49 | 05:22.7–05:26.4 (3.7s) | L83 | mưa! Huy chương bạc: Chồn Gulo, kiến trúc sư đường hầm dưới tuyết |  | chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh đứng ở bậc bạc, đeo huy chương bạc, giơ nắm tay ăn mừng, tuyết rơi trên vai; KHÔNG có anh MC trong cảnh này. |
| b50 | 05:26.4–05:34.0 (7.6s) | L84 | dày! Và huy chương vàng vòng một thuộc về... tuyển thủ mà chuyên gia nói tham gia cho vui: Thú Mỏ Vịt, người bơi 5 tiếng trong nước 0 độ mà vẫn ấm! |  | chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá đứng trên bậc vàng cao nhất, đeo huy chương vàng to, băng đô xanh, khóc vì xúc động, pháo giấy rơi khắp nơi; KHÔNG có anh MC trong cảnh này. |
| b51 | 05:34.0–05:41.8 (7.8s) | L85 | Bảng điểm sau vòng một: Thú Mỏ Vịt 3 điểm, Chồn Gulo 2 điểm, Koala 1 điểm. Còn Lửng Mật và Tôm Tít, hai ứng cử viên nặng ký... vẫn chưa có điểm |  | tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) sáng lên: cột đèn của chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá cao nhất, cột chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai b |
| b52 | 05:41.8–05:46.9 (5.1s) | L86 | nào! Đừng lo, vòng hai sẽ là vòng của những đôi chân. Và có người sẽ phải đi bộ... nửa vòng trái đất! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cầm micro đứng trước một tấm bản đồ thế giới khổng lồ có những đường chấm chấm uốn lượn rất dài, bên cạnh là một đôi giày chạy bộ. |

### scene03 · MARATHON SINH TỒN — AI ĐI XA NHẤT, DI CHUYỂN LẠ NHẤT · 350.8s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.6 (8.6s) | L87 | Vòng hai: marathon sinh tồn! Trong tự nhiên, thức ăn không tự bò đến miệng. Muốn sống, phải đi. Và có những tuyển thủ đi xa đến mức... bản đồ phải vẽ thêm trang! |  | Đường đua marathon hoạt hình chạy vòng quanh một quả địa cầu khổng lồ, vạch xuất phát có cổng bóng bay, anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cầm cờ hiệu đứng ở vạch xuất phát. |
| b02 | 00:08.6–00:13.9 (5.3s) | L88 | Giám khảo sẽ chấm hai tiêu chí: quãng đường đi được, và độ khó của hành trình. Mời tuyển thủ đầu tiên! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ cầm đồng hồ bấm giờ và chiếc thước dây cuộn tròn khổng lồ, ngồi trên chiếc ghế cao bên đường đua. |
| b03 | 00:13.9–00:17.5 (3.6s) | L89 | Lửng Mật xuất phát! Không cần khởi động! Không cần bản đồ! Chỉ cần cái |  | chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần lao ra khỏi vạch xuất phát, mũi dí sát mặt đất đánh hơi, bụi cát bay mù mịt phía sau; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:17.5–00:23.0 (5.5s) | L90 | mũi! Các nhà khoa học ở sa mạc Kalahari đã đeo vòng cổ định vị cho 25 con Lửng Mật, rồi kiên nhẫn đi theo chúng suốt | **25 CON** · được theo dõi · R/380 · [0.6, 0.55] | Một chiếc xe địa hình hoạt hình chạy theo sau một chú chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần đeo vòng cổ có ăng-ten nhỏ, giữa sa mạc cát đỏ có bụi gai; KHÔNG có anh MC trong cảnh này. |
| b05 | 00:23.0–00:28.9 (5.8s) | L91 | nhiều năm. Kết quả: mỗi đêm đi kiếm ăn, một con Lửng Mật đực đi trung bình gần 14km. Có những ngày còn đi tới 27km! | **14 KM** · mỗi đêm · L/360 · [0.55, 0.5] | Một tấm bản đồ sa mạc với đường đi ngoằn ngoèo zíc zắc rất dài màu đỏ, ở cuối đường là chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần thở hổn hển nhưng vẫn ngẩng cao đầu; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:28.9–00:35.8 (7.0s) | L92 | Và đi không phải để dạo chơi. Trong một lần đi kiếm ăn, Lửng Mật có thể đào tới 50 cái hố để lôi chuột và thằn lằn ra khỏi hang. | **50 HỐ** · một lần kiếm ăn · R/380 · [0.6, 0.6] | Mặt đất sa mạc lỗ chỗ hàng chục cái hố nhỏ như mặt bánh tổ ong, chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần chui đầu xuống một hố, chỉ thấy cái mông và cái đuôi vẫy vẫy; KHÔNG có anh MC trong cảnh này. |
| b07 | 00:35.8–00:41.2 (5.4s) | L93 | Và có một chuyện mà ít ai biết: Lửng Mật không bao giờ đi một mình. Trên đầu nó thường có... một đoàn tùy tùng bay theo! |  | chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần đang đào đất, phía trên trời có ba con chim ưng màu xám bạc chân đỏ lượn vòng theo sát như đoàn hộ tống; KHÔNG có anh MC trong cảnh này. |
| b08 | 00:41.2–00:50.5 (9.3s) | L94 | Đó là loài chim ưng xám có tiếng hót như đang hát. Chúng bám theo Lửng Mật, chờ nó đào hang. Con chuột nào hoảng hốt chạy thoát lên mặt đất... là chim ưng sà xuống chộp liền! |  | Một con chuột hoảng hốt chạy vọt ra khỏi miệng hố, một con chim ưng xám sà xuống chộp gọn; trong hố chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần vẫn đang đào hăng say không hề hay biết; KHÔNG có anh MC trong cảnh này. |
| b09 | 00:50.5–00:58.3 (7.8s) | L95 | Các nhà khoa học đã từng thấy tới 6 con chim ưng cùng đi theo một con Lửng Mật. Và chim ưng săn mồi thành công hơn hẳn khi đi theo Lửng Mật so với khi tự săn. | **6 CON** · chim ưng bám theo · R/360 · [0.55, 0.35] | Sáu con chim ưng xám đậu thành hàng trên cành cây khô, đầu đồng loạt quay theo chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần đang đi bên dưới, như hàng ghế khán giả theo dõi trận đấu; KHÔNG có anh MC trong cảnh này. |
| b10 | 00:58.3–01:04.6 (6.3s) | L96 | Còn Lửng Mật được gì từ đoàn tùy tùng này? Các nhà khoa học đo đạc kỹ và trả lời: không được gì cả. Không mất gì, cũng chẳng được gì. |  | chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần quay lại nhìn lên đàn chim ưng với vẻ mặt thờ ơ, nhún vai, trên đầu là bong bóng suy nghĩ vẽ con số không tròn trĩnh to tướng; KHÔNG có anh MC trong cảnh này. |
| b11 | 01:04.6–01:09.4 (4.8s) | L97 | Một gã giang hồ đi đâu cũng có đàn em bám theo hưởng sái, mà bản thân gã... chẳng thèm để ý! |  | Cảnh hài: chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần đi trước như đại ca, phía sau là sáu chim ưng đi bộ lạch bạch xếp hàng như đàn em, mỗi con ngậm một con chuột nhỏ; KHÔNG có anh MC trong cảnh này. |
| b12 | 01:09.4–01:13.6 (4.2s) | L98 | Nhưng nếu Lửng Mật đi xa trong một đêm, thì có một tuyển thủ đi xa... trong cả một mùa |  | Một tấm hồ sơ mật bìa nâu có con dấu hình móng vuốt, bên trong kẹp ảnh chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh trẻ đeo vòng cổ định vị; KHÔNG có anh MC trong cảnh này. |
| b13 | 01:13.6–01:23.5 (9.9s) | L99 | xuân. Hồ sơ M56. Mùa xuân năm 2009, một chú Chồn Gulo đực còn trẻ, được đặt mã số M56, rời khỏi vùng núi gần công viên quốc gia Grand Teton ở bang Wyoming, nước Mỹ. |  | Dãy núi đá tuyết hùng vĩ hoạt hình, chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh trẻ đứng trên mỏm đá nhìn về phía chân trời phía Nam, ba lô nhỏ trên lưng; KHÔNG có anh MC trong cảnh này. |
| b14 | 01:23.5–01:29.7 (6.2s) | L100 | Nó đi về phía Nam. Băng qua núi đá! Băng qua đồng cỏ! Và băng qua cả đường cao tốc liên bang số 80, nơi xe tải chạy ầm ầm |  | chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh chạy băng qua một đường cao tốc rộng, xe tải hoạt hình phanh kít hai bên, nó đã sang đến bên kia an toàn, bụi tung lên; KHÔNG có anh MC trong cảnh này. |
| b15 | 01:29.7–01:35.3 (5.6s) | L101 | ngày đêm! Hai tháng sau, các nhà nghiên cứu nhận được tín hiệu từ... bang Colorado. Chú chồn đã đi khoảng 800km! | **800 KM** · trong 2 tháng · R/360 · [0.55, 0.55] | Tấm bản đồ nước Mỹ hoạt hình với đường chấm đỏ kéo dài từ bang Uai-ô-minh xuống bang Cô-lô-ra-đô, có biểu tượng dấu chân chồn dọc đường; KHÔNG có anh MC trong cảnh này. |
| b16 | 01:35.3–01:44.0 (8.7s) | L102 | Và đây là điều khiến cả nước Mỹ xôn xao: đó là con Chồn Gulo đầu tiên được ghi nhận ở bang Colorado kể từ năm 1919. 90 năm vắng | **1919** · lần cuối thấy chồn · L/360 · [0.5, 0.4] | Một tờ báo hoạt hình bay phấp phới có ảnh lớn chụp chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh trên trang nhất (không chữ), xung quanh là đám đông người hoạt hình đang chỉ trỏ, đèn flash nháy; KHÔNG có anh MC trong cảnh này. |
| b17 | 01:44.0–01:49.7 (5.7s) | L103 | bóng! Có một nhiếp ảnh gia còn chụp được nó trong công viên quốc gia núi Rocky, khiến giới yêu thiên nhiên phát sốt. |  | chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh đứng trên mỏm đá giữa núi Rốc-ky, quay đầu nhìn thẳng vào ống kính máy ảnh của một nhiếp ảnh gia hoạt hình đang nấp sau tảng đá; KHÔNG có anh MC trong cảnh này. |
| b18 | 01:49.7–01:56.9 (7.2s) | L104 | Chuyện vui hơn nữa. Ở nước Mỹ, bang Michigan có biệt danh là "bang Chồn Gulo". Đội thể thao của trường đại học lớn nhất bang cũng tên là Chồn Gulo. |  | Một sân bóng bầu dục hoạt hình, đám cổ động viên mặc áo có hình đầu chồn, giơ cao lá cờ hình chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh; KHÔNG có anh MC trong cảnh này. |
| b19 | 01:56.9–02:01.8 (4.9s) | L105 | Thế nhưng suốt 200 năm, chưa hề có ai chứng minh được Chồn Gulo thật sự sống ở Michigan! |  | Một nhà khoa học hoạt hình cầm kính lúp lục tung một kho lưu trữ đầy hồ sơ bụi bặm, mồ hôi nhễ nhại, xung quanh chỉ toàn ảnh cổ động viên mặc đồ chồn; KHÔNG có anh MC trong cảnh này. |
| b20 | 02:01.8–02:11.1 (9.4s) | L106 | Cho đến đầu năm 2004, một nhóm thợ săn đang đuổi theo dấu chân lạ thì thấy một con vật leo tót lên cây. Nhà sinh vật học được gọi đến, chụp ảnh, xác nhận: đó là một con Chồn Gulo |  | Một cái cây trơ cành giữa cánh đồng tuyết, trên ngọn là chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh đang ôm cành nhìn xuống, dưới gốc là một nhà sinh vật học hoạt hình giơ máy ảnh chụp lia lịa với vẻ mặt sung sướng; KHÔNG có anh MC trong cảnh này. |
| b21 | 02:11.1–02:18.5 (7.3s) | L107 | thật! Bang Chồn Gulo cuối cùng cũng có một con Chồn Gulo thật, sau 200 năm chờ đợi. Như đội bóng đá cuối cùng cũng tìm được... linh vật thật của mình! |  | chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh đứng trên bục danh dự, được cổ động viên hoạt hình choàng khăn và đội mũ của đội bóng, vẻ mặt bối rối không hiểu chuyện gì; KHÔNG có anh MC trong cảnh này. |
| b22 | 02:18.5–02:27.9 (9.5s) | L108 | Nhưng cả Lửng Mật lẫn Chồn Gulo đều phải ngả mũ trước tuyển thủ tiếp theo. Một chú chim cao chưa tới 70cm. Không biết bay. Và đi bộ thì... lạch bạch. |  | chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ đứng ở vạch xuất phát, chỉnh lại nơ bướm, bên cạnh là chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần và chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải |
| b23 | 02:27.9–02:35.7 (7.8s) | L109 | Các nhà khoa học đã gắn những thiết bị định vị nhỏ xíu lên những chú Chim Cánh Cụt Adélie ở đảo Rốt, vùng cực Nam của Trái Đất, và theo dõi chúng suốt mùa đông. |  | Một nhà khoa học mặc áo khoác đỏ dày cộm giữa vùng băng, cẩn thận gắn thiết bị nhỏ như chiếc đồng hồ vào chân chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ, phía sau là đàn cánh cụt tò mò xếp hàng xem; KHÔNG có anh MC trong cảnh này. |
| b24 | 02:35.7–02:42.3 (6.7s) | L110 | Kết quả: mỗi năm, những chú chim này di chuyển trung bình khoảng 13.000km! Chuyến dài nhất được ghi nhận lên tới 17.600km! | **13.000 KM** · mỗi năm · R/360 · [0.55, 0.5] | Bản đồ Nam Cực hoạt hình với một vòng đường chấm đỏ cực lớn uốn quanh biển băng, chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ đứng ở điểm cuối giơ cánh chiến thắng; KHÔNG có anh MC trong cảnh này. |
| b25 | 02:42.3–02:49.2 (6.8s) | L111 | Để dễ hình dung: quãng đường đó dài hơn đi từ Hà Nội sang tận nước Mỹ! Bằng đôi chân ngắn củn và cái bụng làm ván trượt! |  | Quả địa cầu hoạt hình có một đường cong nối từ Việt Nam sang tận nước Mỹ, trên đường vẽ chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ vừa đi lạch bạch vừa nằm sấp trượt bụng trên băng; KHÔNG có anh MC trong cảnh này. |
| b26 | 02:49.2–02:55.9 (6.8s) | L112 | Vì sao phải đi xa đến thế? Vì mùa đông ở Nam Cực, mặt trời biến mất hoàn toàn. Không có ánh sáng, chim cánh cụt không nhìn thấy để săn |  | Bầu trời Nam Cực tối đen như mực, chỉ có vài ngôi sao, chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ đứng một mình trên tảng băng nhìn xung quanh lo lắng; KHÔNG có anh MC trong cảnh này. |
| b27 | 02:55.9–03:03.5 (7.6s) | L113 | mồi. Thế là chúng đi theo mặt trời. Cả đàn trôi trên những tảng băng, đi dần về phía Bắc, đến những nơi mỗi ngày còn vài tiếng chạng vạng, đủ sáng để bắt cá. |  | Một đàn chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ đứng trên những tảng băng trôi như những chiếc bè, cùng hướng về phía chân trời nơi có ánh hoàng hôn cam hồng le lói; KHÔNG có anh MC trong cảnh này. |
| b28 | 03:03.5–03:11.2 (7.6s) | L114 | Đến mùa xuân, chúng lại hối hả quay về đúng bãi đá cũ để làm tổ. Một chú chim không biết bay, đi theo mặt trời, mỗi năm một vòng lớn quanh đáy Trái Đất. |  | chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ đứng trên bãi sỏi quen thuộc nhìn lên mặt trời mùa xuân rực rỡ, bên cạnh là tổ sỏi cũ, ánh sáng ấm áp chiếu xuống; KHÔNG có anh MC trong cảnh này. |
| b29 | 03:11.2–03:21.0 (9.8s) | L115 | Mà khoan, khán giả có biết vì sao loài chim này tên là Adélie không? Năm 1840, nhà thám hiểm người Pháp Dumont d'Urville đặt tên cho một vùng đất ở Nam Cực theo tên vợ mình, bà Adèle. | **1840** · vùng đất A-đê-li · L/360 · [0.5, 0.45] | Một con tàu buồm cổ hoạt hình giữa biển băng, trên boong là nhà thám hiểm râu quai nón giơ tay chỉ về phía bờ biển trắng, tay kia cầm tấm ảnh chân dung người vợ trong khung tròn; KHÔNG có anh MC trong cảnh này. |
| b30 | 03:21.0–03:27.9 (6.9s) | L116 | Và loài chim cánh cụt sống ở đó được đặt theo tên vùng đất. Vậy là Quý ông Vest Đuôi Tôm thật ra... mang tên của một quý bà! |  | chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ nhìn vào gương thấy ảnh phản chiếu đeo nơ đỏ và đội thêm một chiếc mũ quý bà có lông chim, vẻ mặt ngớ ngẩn bất ngờ; KHÔNG có anh MC trong cảnh này. |
| b31 | 03:27.9–03:36.4 (8.4s) | L117 | Trong khi đó, ở đường đua dưới nước, một tuyển thủ bị sóng đánh dạt lên bãi cát. Tôm Tít mắc cạn! Chân ngắn, không đi được trên cạn. Các đối thủ đã nghĩ: thế là xong. |  | chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh nằm ngửa trên bãi cát ướt, sóng vừa rút đi, các chân nhỏ quơ quào trong không khí, mặt hoảng hốt; KHÔNG có anh MC trong cảnh này. |
| b32 | 03:36.4–03:41.3 (4.9s) | L118 | Nhưng ở bờ biển Panama, có một loài tôm tít nhỏ tí xíu có cách thoát thân độc nhất vô nhị. |  | Bãi biển nhiệt đới hoạt hình có cây dừa, một chú tôm tít nhỏ thân dài mảnh nằm trên cát, đang co mình chuẩn bị làm gì đó; KHÔNG có anh MC trong cảnh này. |
| b33 | 03:41.3–03:48.8 (7.5s) | L119 | Nó nằm ngửa, cong người lại thành một vòng tròn... rồi lộn nhào ra phía sau! Một vòng! Hai vòng! Rồi hàng chục vòng liên tục, có khi tới 40 vòng không nghỉ! |  | Chuỗi hình ảnh nhiều tư thế liên tiếp của chú tôm tít đang lộn nhào thành bánh xe trên cát, để lại vệt cát hình vòng tròn, các nét gió tốc độ phía sau; KHÔNG có anh MC trong cảnh này. |
| b34 | 03:48.8–03:56.1 (7.3s) | L120 | 72 vòng mỗi phút, lăn được tới 2 mét để quay về biển! Các nhà khoa học công bố trên tạp chí Nature với tựa đề: Di chuyển như một cái bánh xe? | **72 VÒNG** · mỗi phút · R/360 · [0.4, 0.6] | Một chiếc đồng hồ đếm vòng hoạt hình chạy số liên tục bên cạnh vệt lăn trên cát dẫn thẳng xuống mép nước, chú tôm tít lăn tõm xuống biển; KHÔNG có anh MC trong cảnh này. |
| b35 | 03:56.1–04:02.3 (6.2s) | L121 | Loài người mất hàng ngàn năm mới phát minh ra cái bánh xe. Còn tôm tít... tự biến mình thành bánh xe! |  | Một người tiền sử hoạt hình đang hì hục đục chiếc bánh xe đá, mồ hôi nhễ nhại, quay sang nhìn thấy chú tôm tít lăn vèo qua mặt thì há hốc mồm; KHÔNG có anh MC trong cảnh này. |
| b36 | 04:02.3–04:09.7 (7.4s) | L122 | Cuối cùng, Chim Bồ Nông bước vào đường đua... và không chạy. Nó dang cánh, lấy đà, và bay lên. Ban giám khảo cho phép, vì đây là cách di chuyển rất ít |  | chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn dang đôi cánh rộng lớn chạy lấy đà trên mặt nước rồi cất cánh bay lên trời xanh, bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ giơ biển hiệu dấu tích xanh cho phép. |
| b37 | 04:09.7–04:16.4 (6.7s) | L123 | của nó. Bồ Nông khi đập cánh liên tục. Nó tìm những luồng khí nóng bốc lên từ mặt đất, rồi xoay vòng tròn để được nâng lên cao, như ngồi thang máy miễn phí. |  | chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn bay vòng tròn trong một cột không khí nóng vẽ bằng những mũi tên xoắn ốc màu cam đi lên, phía dưới là mặt đất nắng nóng; KHÔNG có anh MC trong cảnh này. |
| b38 | 04:16.4–04:23.9 (7.5s) | L124 | Bồ Nông Úc từng được ghi nhận bay ở độ cao hàng ngàn mét, cao đến mức người dưới đất không còn nhìn thấy, rồi lượn đi hàng chục cây số mà gần như không tốn sức. |  | Một đàn chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn nhỏ li ti bay trên tầng mây cao, bên dưới là mặt đất xa tít tắp, một người hoạt hình dưới đất cầm ống nhòm tìm mãi không thấy; KHÔNG có anh MC trong cảnh này. |
| b39 | 04:23.9–04:31.9 (8.0s) | L125 | Và đây là bí ẩn lớn nhất của vòng thi. Giữa nước Úc có một hồ nước mặn khổng lồ tên là hồ Eyre. Phần lớn thời gian, hồ khô cạn, chỉ còn lớp muối trắng xóa. |  | Một hồ muối khô cạn trắng xóa mênh mông dưới nắng sa mạc, nứt nẻ thành những ô lục giác, chân trời rung rinh hơi nóng; KHÔNG có anh MC trong cảnh này. |
| b40 | 04:31.9–04:40.1 (8.2s) | L126 | Nhưng cứ vài năm, mưa lớn ở tận phía Bắc lại đổ nước về hồ. Và chỉ ít lâu sau, hàng chục ngàn con Bồ Nông từ khắp nước Úc bỗng nhiên... bay đến, dù cách xa cả ngàn cây số. |  | Hồ Ây-rơ đầy nước xanh lấp lánh, trên trời hàng trăm con chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn từ mọi hướng đang bay tới, hạ cánh xuống mặt nước; KHÔNG có anh MC trong cảnh này. |
| b41 | 04:40.1–04:47.3 (7.2s) | L127 | Năm 1989, các nhà khoa học ước tính đã có khoảng 100.000 chú Bồ Nông con ra đời trên hồ này. Một trận bùng nổ dân số giữa sa mạc! | **1989** · 100.000 chim con · L/360 · [0.5, 0.5] | Một hòn đảo giữa hồ chật kín tổ, hàng trăm chú bồ nông con lông xám há mỏ chờ mẹ cho ăn, bồ nông bố mẹ bay ra bay vào tấp nập; KHÔNG có anh MC trong cảnh này. |
| b42 | 04:47.3–04:53.3 (6.0s) | L128 | Câu hỏi: làm sao Bồ Nông biết hồ có nước, khi nó cách xa cả ngàn cây số? Câu trả lời của khoa học hiện nay là: chưa ai biết chắc. |  | chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn đứng giữa vũng nước, trên đầu là dấu chấm hỏi khổng lồ, xung quanh là các nhà khoa học hoạt hình gãi đầu, mỗi người cầm một tấm bảng có biểu tượng khác nhau (mũi, tai, la bàn, ống nhòm); KHÔNG có anh MC trong cảnh này. |
| b43 | 04:53.3–05:02.2 (8.9s) | L129 | Có giả thuyết cho rằng chúng ngửi được, có giả thuyết cho rằng chúng nghe được sóng âm từ xa, có giả thuyết cho rằng có những con bồ nông già đi do thám trước rồi về... rủ cả nhóm! |  | Một con chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn già đeo kính lão, đội mũ thám tử, bay về báo tin cho đàn bồ nông đang đứng chờ, cả đàn hào hứng vỗ cánh chuẩn bị xuất phát; KHÔNG có anh MC trong cảnh này. |
| b44 | 05:02.2–05:16.5 (14.3s) | L130 | Tổng kết đường đua: một gã đào hố 14km mỗi đêm, một chú chồn băng qua cả đường cao tốc, một chú chim không biết bay đi vòng quanh Nam Cực, một chú tôm tự biến thành bánh xe, và một chú bồ nông đi tìm hồ nước bằng một giác quan mà khoa học còn chưa gọi được tên. |  | Năm khung ảnh nhỏ hoạt hình xếp thành dải phim: chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần đào hố, chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh băng qua đường cao tốc, chú chim cánh cụt Adéli |
| b45 | 05:16.5–05:21.6 (5.2s) | L131 | Giám khảo xin tuyên bố kết quả vòng hai. Đây là vòng thi khó chấm nhất từ trước đến nay. |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ bối rối nhìn chiếc thước dây cuộn dài tràn ra khắp sàn nhà, quấn cả vào chân bàn giám khảo. |
| b46 | 05:21.6–05:28.2 (6.6s) | L132 | Huy chương đồng: Tôm Tít, nhà phát minh ra bánh xe sống! Huy chương bạc: Chồn Gulo, 800km và một tấm ảnh lên |  | Bục trao giải: chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh đứng bậc đồng trong bể nước nhỏ đeo huy chương đồng, chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái |
| b47 | 05:28.2–05:33.8 (5.6s) | L133 | trang nhất! Và huy chương vàng: Chim Cánh Cụt, 13.000km mỗi năm, đi theo mặt trời quanh đáy Trái Đất! |  | chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ đứng trên bậc vàng, đeo huy chương vàng, chỉnh nơ bướm đầy tự hào, mặt trời nhỏ hoạt hình mỉm cười chiếu sáng phía sau; KHÔNG có anh MC trong cảnh này. |
| b48 | 05:33.8–05:43.4 (9.6s) | L134 | Bảng điểm sau hai vòng: Chồn Gulo vươn lên dẫn đầu với 4 điểm! Thú Mỏ Vịt và Chim Cánh Cụt cùng 3 điểm. Koala và Tôm Tít mỗi bạn 1 điểm. Còn Lửng Mật... vẫn chưa có điểm nào! |  | tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) sáng lên: cột chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh cao nhất, cột chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như |
| b49 | 05:43.4–05:46.8 (3.4s) | L135 | Ủa... đi bộ xa vậy có được ăn gì không ạ? Cháu đói rồi. |  | chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ ngồi bệt dưới chân bảng điểm, xoa bụng, ánh mắt thèm thuồng nhìn về phía khu ẩm thực; KHÔNG có anh MC trong cảnh này. |
| b50 | 05:46.8–05:50.8 (4.0s) | L136 | Câu hỏi hay lắm, tuyển thủ Koala! Vì vòng ba chính là... vòng ăn uống! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cười tươi chỉ tay về phía một khu bếp khổng lồ có lò nướng, chảo, bát đĩa và thực đơn treo tường (chỉ có hình vẽ món ăn), hơi nóng bốc lên thơm phức. |

### scene04 · BẾP TRƯỞNG HOANG DÃ — AI ĂN KHÉO, ĂN NHIỀU, ĂN LẠ NHẤT · 320.2s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.7 (8.7s) | L137 | Vòng ba: bếp trưởng hoang dã! Mỗi tuyển thủ phải trình bày cách mình kiếm ăn trước ban giám khảo. Điểm cộng cho sự khéo léo, cho sự sáng tạo, và cho... độ khó tin! |  | Một khu bếp ngoài trời hoạt hình cực lớn, mỗi tuyển thủ có một quầy bếp riêng có biển hiệu hình con vật (không chữ), bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ đeo mũ đầu bếp trắng cao, cầm chiếc thìa nếm thử. |
| b02 | 00:08.7–00:14.9 (6.2s) | L138 | Mở màn là Thú Mỏ Vịt, nhà vô địch vòng một. Và bí mật đầu tiên của Thú Mỏ Vịt là: nó ăn khỏe đến mức khó |  | chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá đeo tạp dề, đứng trước quầy bếp chất cao như núi những con tôm, ấu trùng và giun nhỏ hoạt hình, vẻ mặt sẵn sàng; KHÔNG có anh MC trong cảnh này. |
| b03 | 00:14.9–00:23.5 (8.5s) | L139 | tin. Một con Thú Mỏ Vịt trưởng thành ăn mỗi ngày lượng thức ăn bằng khoảng một phần năm trọng lượng cơ thể. Nhưng một Thú Mỏ Vịt mẹ đang nuôi con còn ăn khủng khiếp hơn nhiều! | **1/5** · cân nặng mỗi ngày · R/360 · [0.7, 0.55] | Một chiếc cân đĩa hoạt hình: đĩa bên trái là chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá, đĩa bên phải là một đống thức ăn nhỏ bằng một phần năm; bên cạnh là chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá mẹ đeo nơ hồng cạnh một đố |
| b04 | 00:23.5–00:28.1 (4.7s) | L140 | Có những tài liệu ghi nhận Thú Mỏ Vịt mẹ đang cho con bú có thể ăn gần bằng cả cân nặng của chính mình mỗi |  | chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá mẹ ngồi trước một đống thức ăn cao bằng người nó, má phồng to, ăn liên tục không ngừng, trên đầu có chiếc đồng hồ chạy vèo vèo; KHÔNG có anh MC trong cảnh này. |
| b05 | 00:28.1–00:34.4 (6.3s) | L141 | ngày. Tức là nếu một người mẹ nặng 50kg ăn theo kiểu này, mỗi ngày phải ăn... 50kg cơm! |  | Một bà mẹ hoạt hình ngồi trước một nồi cơm khổng lồ cao hơn cả người, cầm đôi đũa ngơ ngác, xung quanh là chồng bát đĩa cao ngất; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:34.4–00:42.6 (8.2s) | L142 | Mà ăn khỏe như vậy là có lý do. Thú Mỏ Vịt mẹ không có núm vú, sữa tiết ra qua da bụng, nên con non phải liếm. Và chính sữa ấy đã làm các nhà khoa học bất ngờ vào năm 2018. |  | Phòng thí nghiệm hoạt hình hiện đại: một nhà khoa học nữ đeo kính bảo hộ nhỏ giọt sữa trắng vào đĩa petri, bên cạnh là ảnh chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá dán trên tường; KHÔNG có anh MC trong cảnh này. |
| b07 | 00:42.6–00:50.2 (7.5s) | L143 | Các nhà khoa học ở Úc đã tách ra từ sữa Thú Mỏ Vịt một loại đạm có khả năng diệt vi khuẩn. Và khi nhìn hình dạng ba chiều của nó, họ thấy một cấu trúc chưa từng gặp bao |  | Một mô hình phân tử ba chiều hoạt hình xoắn quăn như những lọn tóc lò xo màu xanh tím lơ lửng trên bàn thí nghiệm, phát sáng nhẹ; KHÔNG có anh MC trong cảnh này. |
| b08 | 00:50.2–00:59.1 (9.0s) | L144 | giờ. Phân tử ấy xoăn tít như những lọn tóc lò xo, nên các nhà khoa học đặt tên cho kiểu cấu trúc này theo tên một ngôi sao nhí tóc xoăn nổi tiếng của Hollywood: Shirley Temple! |  | Bên cạnh mô hình phân tử xoăn tít là một bé gái hoạt hình tóc vàng xoăn lò xo nhún nhảy, hai mái tóc trông giống hệt mô hình phân tử; KHÔNG có anh MC trong cảnh này. |
| b09 | 00:59.1–01:09.3 (10.2s) | L145 | Vì sao sữa Thú Mỏ Vịt cần chất diệt khuẩn mạnh như vậy? Vì sữa chảy ra ngoài da, dính đầy bụi bẩn và vi khuẩn, mà con non lại liếm trực tiếp. Không có lớp bảo vệ này, con non dễ bị nhiễm khuẩn. |  | Hình phóng to da bụng chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá mẹ có giọt sữa trắng, xung quanh là những con vi khuẩn hoạt hình mặt xấu xa đang tiến lại gần thì bị những lọn xoăn tím của đạm sữa quất bay; KHÔNG có anh MC trong cảnh này. |
| b10 | 01:09.3–01:17.9 (8.6s) | L146 | Ngày nay, các nhà khoa học hy vọng loại đạm này có thể giúp tìm ra cách mới chống lại những loại vi khuẩn kháng thuốc. Từ một con vật từng bị tưởng là đồ giả khâu ghép! |  | Một chai thuốc hoạt hình có hình chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá trên nhãn (không chữ), xung quanh là những vi khuẩn mặc áo giáp kháng thuốc đang hoảng sợ bỏ chạy; KHÔNG có anh MC trong cảnh này. |
| b11 | 01:17.9–01:22.9 (5.0s) | L147 | Giám khảo ghi nhận: món ăn chưa ngon, nhưng sữa thì... có thể cứu người. Rất ấn tượng. |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ cầm chiếc thìa, gật gù ghi chép, bên cạnh có một chiếc huy hiệu nhỏ hình chữ thập y tế màu xanh. |
| b12 | 01:22.9–01:28.2 (5.2s) | L148 | Quầy bếp tiếp theo: Rái Cá Biển. Và Rái Cá mang theo một dụng cụ nấu ăn rất đặc biệt: một hòn |  | chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách nằm ngửa trên mặt nước cạnh quầy bếp, giơ hòn đá xám lên như đầu bếp khoe con dao gia truyền, trên bụng là một con trai to; KHÔNG có anh MC trong cảnh này. |
| b13 | 01:28.2–01:39.0 (10.8s) | L149 | đá. Năm 2024, các nhà khoa học công bố một nghiên cứu theo dõi 196 con Rái Cá Biển ở bang California, nước Mỹ, trong nhiều năm. Họ muốn biết: dùng công cụ thì được lợi gì? | **196 CON** · được theo dõi · R/360 · [0.5, 0.55] | Hàng chục chú chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách hoạt hình nhỏ đeo vòng định vị nằm ngửa trên mặt biển, một nhà khoa học trên thuyền cầm sổ ghi chép và ống nhòm; KHÔNG có anh MC trong cảnh này. |
| b14 | 01:39.0–01:46.0 (7.0s) | L150 | Câu trả lời: những con dùng đá đập vỏ thì răng ít bị mẻ hơn hẳn những con chỉ dùng răng cắn. Và răng mà hỏng thì Rái Cá không ăn được, nghĩa là không sống |  | Hai bộ răng hoạt hình so sánh: bộ răng bên trái mẻ sứt nhiều chỗ (rái cá cắn vỏ), bộ răng bên phải trắng sáng lấp lánh (rái cá dùng đá); KHÔNG có anh MC trong cảnh này. |
| b15 | 01:46.0–01:54.7 (8.7s) | L151 | nổi! Điều thú vị: rái cá cái dùng đá nhiều hơn rái cá đực. Nhờ hòn đá, những con cái nhỏ con hơn vẫn ăn được những con mồi vỏ cứng hơn gần gấp 3 lần so với những con không dùng công cụ. | **~3 LẦN** · vỏ cứng hơn · R/360 · [0.4, 0.5] | chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách cái nhỏ con đập hòn đá xuống một con ốc vỏ cứng trên bụng, vỏ ốc vỡ toác; bên cạnh là một con rái cá đực to xác đang cắn vỏ đến méo cả mồm; KHÔNG có anh MC trong cảnh này. |
| b16 | 01:54.7–02:01.5 (6.8s) | L152 | Bài học từ bếp Rái Cá: nếu bạn bóc được vỏ cua bằng dụng cụ, đừng bao giờ dùng răng! Nha sĩ của kênh Vẽ Chuyện Hoang Dã xin cảm ơn. |  | Một nha sĩ hoạt hình mặc áo blouse trắng giơ ngón cái tán thưởng, cầm chiếc gương nha khoa, bên cạnh là chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách cười khoe hàm răng trắng bóng; KHÔNG có anh MC trong cảnh này. |
| b17 | 02:01.5–02:06.0 (4.5s) | L153 | Quầy bếp số ba: Cá Heo. Và Cá Heo không nấu ăn. Cá Heo... chơi thể thao với đồ ăn! |  | chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái nhô lên khỏi mặt nước, đội mũ đầu bếp lệch, nháy mắt tinh nghịch với ban giám khảo; KHÔNG có anh MC trong cảnh này. |
| b18 | 02:06.0–02:13.9 (7.9s) | L154 | Ở vùng biển Florida nước Mỹ, người ta quay được cảnh Cá Heo dùng chiếc đuôi quất mạnh vào con cá, khiến con cá bay vút lên không trung như một quả bóng bị sút! |  | chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái quẫy mạnh chiếc đuôi, một con cá đối bay vèo lên trời theo đường cong parabol, các nét vẽ tốc độ phía sau; KHÔNG có anh MC trong cảnh này. |
| b19 | 02:13.9–02:21.6 (7.7s) | L155 | Con cá rơi xuống, choáng váng, và Cá Heo chỉ việc bơi tới ăn. Các nhà khoa học gọi đây là kỹ thuật "đá cá", và nó được học từ bố mẹ sang con cái. |  | Con cá đối choáng váng nằm trên mặt nước, mắt xoay vòng, chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái con đang chăm chú nhìn chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái mẹ biểu diễn mẫu như một buổi học; KHÔNG có anh MC trong cảnh này. |
| b20 | 02:21.6–02:28.9 (7.3s) | L156 | Nhưng màn trình diễn đỉnh cao nhất của Cá Heo không phải đá cá. Mà là... làm việc cùng con người. Và nó diễn ra ở một thị trấn nhỏ của nước Brazil. |  | Một thị trấn ven biển hoạt hình của Bra-xin có những ngôi nhà nhiều màu sắc, một con kênh rộng nối ra biển, những người đánh cá đứng chờ ven bờ; KHÔNG có anh MC trong cảnh này. |
| b21 | 02:28.9–02:36.2 (7.3s) | L157 | Câu chuyện này sẽ được kể đầy đủ ở vòng sáu. Giờ thì xin mời thí sinh tiếp theo vào bếp. Thí sinh này có chiếc nồi lớn nhất cuộc thi! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng giơ tay ra hiệu "khoan đã" với chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái, rồi quay sang chỉ về phía một cái bóng đen khổng lồ có chiếc mỏ dài đang bước vào bếp. |
| b22 | 02:36.2–02:44.4 (8.2s) | L158 | Chim Bồ Nông! Và chiếc nồi chính là... cái mỏ của nó. Nhưng hôm nay, Bồ Nông không khoe cái mỏ. Nó muốn khoe một chiến thuật săn mồi bằng... cả đội. |  | chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn dắt theo năm con bồ nông khác, cả nhóm mặc đồng phục giống nhau như một đội bóng, xếp hàng ngang đứng trước quầy bếp; KHÔNG có anh MC trong cảnh này. |
| b23 | 02:44.4–02:51.8 (7.4s) | L159 | Đầu tiên, các bạn đã biết bồ nông bay theo hình chữ V. Nhưng chỉ đến năm 2001, các nhà khoa học mới đo được lợi ích thật sự của đội hình này. |  | Một đàn chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn bay thành hình chữ V gọn gàng trên bầu trời xanh, phía dưới là một chiếc thuyền máy chở các nhà khoa học đang ngước nhìn; KHÔNG có anh MC trong cảnh này. |
| b24 | 02:51.8–02:58.2 (6.4s) | L160 | Họ huấn luyện những con bồ nông trắng bay theo một chiếc thuyền máy và một chiếc máy bay siêu nhẹ, rồi gắn máy đo nhịp tim lên lưng chúng. |  | Một chiếc máy bay siêu nhẹ hoạt hình bay là là trên sông, phía sau là đàn chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn bay theo, mỗi con đeo một chiếc máy đo nhỏ trên lưng có hình trái tim đập; KHÔNG có anh MC trong cảnh này. |
| b25 | 02:58.2–03:06.4 (8.2s) | L161 | Kết quả: khi bay theo đội hình, nhịp tim của bồ nông thấp hơn khoảng 11 đến 14% so với khi bay một mình. Bay cùng nhau thì đỡ mệt hơn hẳn! | **-14%** · nhịp tim · R/360 · [0.7, 0.5] | Hai màn hình nhịp tim hoạt hình so sánh: màn hình bồ nông bay một mình có đường nhịp tim dày đặc gấp gáp, màn hình bồ nông bay đội hình có đường nhịp tim thưa thớt thư thái; KHÔNG có anh MC trong cảnh này. |
| b26 | 03:06.4–03:12.8 (6.3s) | L162 | Bí quyết là con bay sau lướt trên luồng khí bốc lên từ đầu cánh con bay trước, như người đạp xe nép sau lưng người khác để đỡ gió. |  | Sơ đồ hoạt hình hai con chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn bay nối đuôi, từ đầu cánh con trước tỏa ra những xoáy khí xoắn ốc màu xanh nhạt nâng cánh con sau lên; bên cạnh là hình hai người đạp xe nép sau nhau; KHÔNG có anh MC trong cảnh này. |
| b27 | 03:12.8–03:20.5 (7.8s) | L163 | Và con bồ nông bay đầu đàn thì sao? Nó vất vả nhất. Nhưng đừng lo, các thành viên trong đàn thường thay phiên nhau dẫn đầu. Rất công bằng, rất dân chủ. |  | Con chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn bay đầu đàn thở hổn hển mồ hôi nhễ nhại, quay đầu ra hiệu, một con khác bay lên thay thế, hai bên đập cánh chào nhau như đổi ca trực; KHÔNG có anh MC trong cảnh này. |
| b28 | 03:20.5–03:26.2 (5.6s) | L164 | Quầy bếp tiếp theo... trống trơn. Tuyển thủ Lửng Mật đã biến mất. Và ở góc sân, có tiếng đào đất loạt soạt. |  | Một quầy bếp bỏ trống chỉ còn chiếc tạp dề treo lủng lẳng, ở góc sân có một đống đất mới đào và những vụn đất bắn tung lên; KHÔNG có anh MC trong cảnh này. |
| b29 | 03:26.2–03:34.1 (7.9s) | L165 | Lửng Mật tên tiếng Anh là "lửng mật ong". Ai cũng nghĩ món khoái khẩu của nó là mật ong. Nhưng các nhà khoa học ở Kalahari đã ngồi đếm từng miếng nó ăn suốt nhiều năm. |  | chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần thò đầu ra khỏi hố đất, miệng ngậm một chiếc thìa mật ong, phía sau một nhà khoa học hoạt hình cầm sổ ghi chép và máy đếm bấm tay; KHÔNG có anh MC trong cảnh này. |
| b30 | 03:34.1–03:42.0 (7.9s) | L166 | Và họ phát hiện ra: thứ Lửng Mật đào được nhiều nhất là chuột, thằn lằn, bọ cạp, và một món đặc biệt: những ấu trùng của một loài ong sống đơn độc dưới cát. |  | Mặt cắt lòng đất cát hoạt hình: những khoang nhỏ chứa ấu trùng ong màu trắng nằm sâu trong cát, phía trên chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần đang đào xuống thẳng tới chỗ đó; KHÔNG có anh MC trong cảnh này. |
| b31 | 03:42.0–03:51.3 (9.3s) | L167 | 4 con Lửng Mật đực đã được quan sát đào ấu trùng ong suốt hơn 50 tiếng, và ăn tổng cộng khoảng 2.800 con ấu trùng. Những con ấu trùng ấy nằm sâu tới 50 đến 70cm dưới cát! | **2.800** · ấu trùng ong · R/360 · [0.5, 0.6] | Bốn chú chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần chui sâu dưới cát chỉ thò đuôi lên, xung quanh là những ấu trùng ong trắng nhỏ, một chiếc thước dây cắm thẳng xuống cát đo chiều sâu; KHÔNG có anh MC trong cảnh này. |
| b32 | 03:51.3–03:59.1 (7.8s) | L168 | Vậy còn câu chuyện nổi tiếng về loài chim dẫn mật dẫn đường cho Lửng Mật tới tổ ong, rồi hai bên chia nhau chiến lợi phẩm? Đây là lúc ban giám khảo... phải nói thật. |  | Một cuốn truyện tranh hoạt hình mở ra, trang sách vẽ một con chim nhỏ màu nâu dẫn đường cho chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần đi về phía tổ ong trên cây, xung quanh có những ngôi sao lấp lánh như truyện cổ tích; KHÔNG có anh MC trong cảnh này. |
| b33 | 03:59.1–04:09.4 (10.3s) | L169 | Năm 1990, ba nhà điểu học công bố một bài báo, viết rằng: hơn 200 năm nghiên cứu ở châu Phi, không có nhà khoa học nào tận mắt thấy chim dẫn mật dẫn đường cho Lửng Mật cả. | **1990** · bài báo phản bác · L/360 · [0.5, 0.5] | Ba nhà điểu học hoạt hình đeo kính ngồi quanh bàn, chỉ vào một tấm bản đồ châu Phi có dấu chấm hỏi to, trước mặt là chồng tài liệu cũ; KHÔNG có anh MC trong cảnh này. |
| b34 | 04:09.4–04:19.1 (9.7s) | L170 | Thậm chí có một bộ phim tài liệu cũ quay cảnh này, và sau này người làm phim kể lại: đó là một con lửng đã được thuần hóa, đi theo một con chim nhồi bông treo trên dây câu! |  | Hậu trường quay phim hoạt hình: một người cầm cần câu treo con chim nhồi bông lủng lẳng, chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần đeo vòng cổ ngoan ngoãn đi theo, đạo diễn cầm loa ra hiệu "cắt"; KHÔNG có anh MC trong cảnh này. |
| b35 | 04:19.1–04:26.0 (6.9s) | L171 | Một nghiên cứu năm 2023 đã phỏng vấn gần 400 thợ săn mật ong ở 9 nước châu Phi. Phần lớn họ không tin hai loài này hợp tác. |  | Một nhóm thợ săn mật ong hoạt hình ngồi quanh đống lửa, có người lắc đầu, có người khoanh tay nghi ngờ, một nhà nghiên cứu cầm sổ ghi chép; KHÔNG có anh MC trong cảnh này. |
| b36 | 04:26.0–04:35.9 (9.9s) | L172 | Nhưng ở một vài cộng đồng ở Tanzania, có những người kể rằng họ từng thấy. Nên kết luận cuối cùng của khoa học hiện nay là: có thể có, nhưng rất hiếm, và chưa ai quay được một bằng chứng rõ ràng. |  | Một tấm ảnh mờ nhòe như ảnh người tuyết bí ẩn, chỉ thấy lờ mờ một con chim và một con lửng, có kính lúp to đặt bên cạnh và dấu chấm hỏi; KHÔNG có anh MC trong cảnh này. |
| b37 | 04:35.9–04:43.5 (7.6s) | L173 | Giám khảo kết luận: Lửng Mật được điểm cao vì đào giỏi, nhưng bị trừ điểm vì... nổi tiếng nhờ một câu chuyện chưa được kiểm chứng! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gõ búa, giơ một tấm thẻ hình chiếc kính lúp; chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần đứng trước bàn giám khảo khoanh tay hậm hực. |
| b38 | 04:43.5–04:51.2 (7.7s) | L174 | Kết quả vòng ba! Huy chương đồng: Rái Cá Biển, đầu bếp có hòn đá bảo vệ hàm răng! Huy chương bạc: Chim Bồ Nông, đội bay tiết kiệm sức nhất bầu |  | Bục trao giải: chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách đứng bậc đồng ôm hòn đá đeo huy chương đồng, chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn đứng bậc bạc dang cánh đeo huy chương bạc; KHÔNG có anh MC trong cảnh này. |
| b39 | 04:51.2–04:58.0 (6.8s) | L175 | trời! Và huy chương vàng vòng ba: Thú Mỏ Vịt! Ăn khỏe nhất cuộc thi, và có dòng sữa có thể giúp con người chống lại vi khuẩn kháng thuốc! |  | chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá đứng trên bậc vàng, giờ đã đeo hai chiếc huy chương vàng, băng đô xanh, nhảy cẫng lên sung sướng, pháo giấy rơi khắp nơi; KHÔNG có anh MC trong cảnh này. |
| b40 | 04:58.0–05:07.3 (9.3s) | L176 | Bảng điểm sau ba vòng: Thú Mỏ Vịt vươn lên dẫn đầu với 6 điểm! Chồn Gulo 4 điểm. Chim Cánh Cụt 3 điểm. Chim Bồ Nông 2 điểm. Koala, Tôm Tít và Rái Cá mỗi bạn 1 điểm. |  | tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) sáng lên: cột chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá vọt lên cao nhất, cột chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai b |
| b41 | 05:07.3–05:12.5 (5.2s) | L177 | Còn Lửng Mật, ứng cử viên nặng ký nhất trước giải, vẫn chưa có điểm nào. Và Cá Heo, Gấu Nước cũng vậy. |  | chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần, chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái và một hộp kính lúp đựng chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương đứng  |
| b42 | 05:12.5–05:20.2 (7.7s) | L178 | Nhưng đừng vội loại họ. Đại hội mới đi được ba trên tám chặng đường. Và vòng bốn sẽ thử thách thứ mà cơ bắp không thể thay thế: các giác quan! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cầm một chiếc kính lúp khổng lồ soi vào mắt mình, mắt to phóng đại trông rất hài, tay kia đặt sau tai như đang lắng nghe. |

### scene05 · CĂNG TIN ĐẠI HỘI — MỖI TUYỂN THỦ UỐNG NƯỚC VÀ CHỌN MÓN THẾ NÀO · 176.3s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.8 (9.8s) | L179 | Giờ giải lao! Sau ba vòng thi căng thẳng, các tuyển thủ được mời vào căng tin của đại hội. Và ngay tại đây, chúng ta phát hiện ra mỗi người có một kiểu ăn uống... không ai giống ai. |  | Một căng tin hoạt hình rộng rãi có quầy buffet dài, mười tuyển thủ xếp hàng cầm khay, anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đứng ở cửa đeo tạp dề phục vụ, tay cầm chiếc muôi lớn. |
| b02 | 00:09.8–00:16.6 (6.8s) | L180 | Koala đến quầy lá khuynh diệp đầu tiên. Nhưng thay vì ăn ngay, nó làm một việc rất lạ: cúi xuống... ngửi từng chiếc lá. |  | chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ cúi sát mũi vào một rổ lá khuynh diệp, nhắm mắt hít hà như chuyên gia nếm rượu, bên cạnh có một chiếc kính lúp nhỏ; KHÔNG có anh MC trong cảnh này. |
| b03 | 00:16.6–00:25.9 (9.2s) | L181 | Các nhà khoa học ở Nhật Bản đã quan sát 10 chú Koala trong vườn thú và thấy rằng chúng ngửi lá nhiều hơn hẳn trước khi ăn. Và mùi hương của lá có thể dự đoán chú Koala sẽ ăn lá nào. | **10 CHÚ** · được quan sát · R/360 · [0.5, 0.5] | Một sở thú Nhật Bản hoạt hình có cây anh đào, nhân viên đặt sáu bó lá khuynh diệp khác loại trước mặt chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ, một nhà khoa học cầm máy đo mùi hương có biểu đồ nhiều cột; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:25.9–00:35.1 (9.3s) | L182 | Vì sao phải ngửi kỹ như vậy? Vì có những cây khuynh diệp chứa nhiều một nhóm chất gây buồn nôn. Ăn phải, Koala sẽ thấy khó chịu, và từ đó nó học cách nhận ra mùi của chiếc lá "có vấn đề". |  | Hai chiếc lá khuynh diệp hoạt hình: chiếc bên trái tỏa ra làn khói mùi màu xanh lá hình mặt nhăn nhó, chiếc bên phải tỏa ra làn khói mùi màu hồng hình mặt cười; chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ né chiếc bên trái; KHÔNG có anh MC trong cảnh này. |
| b05 | 00:35.1–00:43.2 (8.0s) | L183 | Một nghiên cứu theo dõi suốt 10 năm trên đảo Phillip ở Úc còn cho thấy: Koala thích leo những cây to, nhưng tránh những cây có lá chứa nhiều chất gây buồn nôn, hoặc lá nghèo đạm. | **10 NĂM** · theo dõi · L/360 · [0.5, 0.4] | Một khu rừng khuynh diệp hoạt hình nhìn từ trên cao, mỗi cây có một chấm màu xanh hoặc đỏ đánh dấu, những chú chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ chỉ trèo lên những cây có chấm xanh; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:43.2–00:52.4 (9.2s) | L184 | Có nhà khoa học còn ví von: chọn cây để ăn đối với Koala giống như phải chọn một trong 1.000 nhà hàng khắp thành phố... mà không có ứng dụng đánh giá nào! |  | chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ đứng trên ngã tư một thành phố hoạt hình đầy những nhà hàng hình cái cây, cầm chiếc điện thoại trống trơn không có ứng dụng, gãi đầu bối rối; KHÔNG có anh MC trong cảnh này. |
| b07 | 00:52.4–00:58.5 (6.1s) | L185 | Cá Heo đến quầy nước. Và lúc này, một câu hỏi được đặt ra: sống giữa biển nước mặn mênh mông, Cá Heo uống |  | chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái nhô lên trước quầy nước có ba bình: bình nước biển xanh có muối kết tinh, bình nước ngọt trong veo, bình nước cam; cá heo nhìn qua lại phân vân; KHÔNG có anh MC trong cảnh này. |
| b08 | 00:58.5–01:07.5 (9.1s) | L186 | nước gì? Câu trả lời là: gần như không uống. Cá Heo lấy nước chủ yếu từ chính thức ăn, vì con cá và con mực chứa rất nhiều nước, và từ nước mà cơ thể tự tạo ra khi đốt cháy mỡ. |  | Sơ đồ hoạt hình bên trong chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái: một con cá được ăn vào tỏa ra những giọt nước nhỏ, một khối mỡ đang cháy tỏa ra hơi nước, tất cả gom vào một chiếc bình chứa trong cơ thể; KHÔNG có anh MC trong cảnh này. |
| b09 | 01:07.5–01:17.5 (10.0s) | L187 | Một nghiên cứu năm 2023 dùng phương pháp đo đồng vị ô-xy trong máu cá heo đã tính ra: nước từ thức ăn và nước tự tạo trong cơ thể chiếm hơn 90% lượng nước cá heo nhận vào. | **> 90%** · nước từ thức ăn · R/360 · [0.4, 0.5] | Một biểu đồ tròn hoạt hình chia hai phần: phần rất lớn màu xanh có biểu tượng con cá và ngọn lửa, phần nhỏ xíu màu xám có biểu tượng giọt nước biển; chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái chỉ vào phần lớn; KHÔNG có anh MC trong cảnh này. |
| b10 | 01:17.5–01:23.7 (6.2s) | L188 | Sống giữa đại dương mà không uống nước biển. Giống như người sống trên đảo mà chỉ uống... nước dừa! |  | chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái nằm thư giãn trên chiếc phao giữa biển, cắm ống hút vào một quả dừa, đeo kính râm tận hưởng; KHÔNG có anh MC trong cảnh này. |
| b11 | 01:23.7–01:31.5 (7.8s) | L189 | Chim Cánh Cụt thì ngược lại. Cánh Cụt nuốt nước biển mỗi lần ăn tôm, ăn cá. Nhưng nó có một bộ lọc muối riêng: một tuyến lọc nằm ngay phía trên mắt. |  | chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ đứng trước quầy hải sản, đầu được vẽ cắt ngang như sơ đồ: phía trên mỗi mắt có một tuyến nhỏ màu hồng nối với những mạch máu li ti; KHÔNG có anh MC trong cảnh này. |
| b12 | 01:31.5–01:41.1 (9.7s) | L190 | Tuyến này lọc muối thừa ra khỏi máu, tạo thành một dung dịch nước muối đậm đặc chảy xuống mỏ. Rồi Cánh Cụt chỉ việc... hắt xì một cái, hoặc lắc đầu thật mạnh để vẩy muối ra! |  | Cận cảnh chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ hắt xì một cái thật mạnh, những giọt nước muối trong veo bay ra từ đầu mỏ, các tuyển thủ khác đứng gần giơ tay che mặt; KHÔNG có anh MC trong cảnh này. |
| b13 | 01:41.1–01:49.8 (8.7s) | L191 | Và chúng không uống nước biển bừa bãi. Những lúc có thể, cánh cụt vẫn thích uống nước tuyết tan, hoặc ăn tuyết cho đỡ khát. Có máy lọc trong người, nhưng vẫn thích nước tinh khiết! |  | chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ cúi xuống liếm một vũng nước tuyết tan trên băng, bên cạnh là một nắm tuyết trắng xốp như kem, vẻ mặt khoan khoái; KHÔNG có anh MC trong cảnh này. |
| b14 | 01:49.8–01:55.1 (5.3s) | L192 | Gấu Nước đến quầy... nhưng quầy nào cũng quá to. Ban tổ chức phải dùng kính hiển vi mới phục vụ được |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cúi người soi qua một kính hiển vi đặt trên quầy, trong vòng tròn phóng to là chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương đang đứng trên một chiếc lá rêu xanh; KHÔNG có anh MC trong cảnh này. |
| b15 | 01:55.1–02:06.9 (11.8s) | L193 | cậu ấy. Phần lớn các loài gấu nước ăn thực vật: rêu, tảo. Trong miệng chúng có một cặp kim nhọn cực nhỏ. Chúng dùng kim chọc thủng thành tế bào của cây rêu, rồi hút lấy dịch bên trong như uống... trà sữa trân châu! |  | Cận cảnh hoạt hình chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương áp miệng vào một tế bào rêu xanh như quả bóng, hai chiếc kim nhỏ chọc vào, chất lỏng xanh được hút lên như hút ống hút, bên cạnh vẽ một ly trà sữa để so sánh; KHÔNG có anh MC trong cảnh này. |
| b16 | 02:06.9–02:14.1 (7.2s) | L194 | Nhưng không phải gấu nước nào cũng ăn chay. Có những loài gấu nước ăn thịt, săn những sinh vật tí hon khác, và có loài còn ăn thịt... cả gấu nước khác! |  | Trong thế giới hiển vi hoạt hình, một chú gấu nước to hơn có vẻ mặt dữ dằn đang đuổi theo một sinh vật tí hon hình ống, chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương của chúng ta trốn sau chiếc lá rêu run rẩy; KHÔNG có anh MC trong cảnh này. |
| b17 | 02:14.1–02:21.6 (7.6s) | L195 | Thú Mỏ Vịt, người đã có hai huy chương vàng, đến quầy cuối cùng. Và nó gọi... cả quầy! Vì như vòng ba đã kể, Thú Mỏ Vịt ăn khỏe không ai |  | chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá đứng ở quầy, chỉ tay vào toàn bộ dãy khay đồ ăn, nhân viên căng tin há hốc mồm đẩy ra cả một xe đẩy chất đầy đồ ăn; KHÔNG có anh MC trong cảnh này. |
| b18 | 02:21.6–02:30.5 (8.8s) | L196 | bằng. Để ăn được nhiều như vậy, Thú Mỏ Vịt dành khoảng 10-12 tiếng mỗi ngày để lặn tìm mồi dưới đáy suối. Và mùa đông nước càng lạnh, nó càng phải kiếm ăn lâu hơn nữa. | **10-12 GIỜ** · kiếm ăn mỗi ngày · R/360 · [0.5, 0.5] | Dưới đáy suối hoạt hình, chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá đang dùng mỏ lật đá tìm mồi, hai má phồng to dần lên, bên cạnh là chiếc đồng hồ chỉ nhiều giờ trôi qua; KHÔNG có anh MC trong cảnh này. |
| b19 | 02:30.5–02:37.4 (7.0s) | L197 | Lửng Mật thì không đến quầy nào cả. Ban tổ chức tìm thấy Lửng Mật đang... đào tung sàn căng tin để tìm ấu trùng ong! |  | Sàn căng tin hoạt hình bị đào thủng một lỗ to, đất cát văng tung tóe lên quầy buffet, chỉ thấy cái mông và cái đuôi của chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần thò ra, nhân viên căng tin ôm đầu; KHÔNG có anh MC trong cảnh này. |
| b20 | 02:37.4–02:43.7 (6.3s) | L198 | Giám khảo xin nhắc tuyển thủ Lửng Mật: căng tin không phải là sa mạc Kalahari! Đề nghị lấp hố lại ngay! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ đứng bên miệng hố gõ búa, chỉ cây búa về phía cái hố, vẻ mặt nghiêm khắc nhưng khóe miệng nhếch cười. |
| b21 | 02:43.7–02:48.8 (5.1s) | L199 | Cháu ăn no rồi ạ! Nhưng mà cháu vẫn muốn ngửi thêm vài chiếc lá nữa, nhỡ đâu có chiếc nào thơm hơn... |  | chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ ngồi giữa đống lá khuynh diệp, cầm hai chiếc lá đưa lên mũi ngửi so sánh, vẻ mặt đắn đo như chuyên gia; KHÔNG có anh MC trong cảnh này. |
| b22 | 02:48.8–02:56.3 (7.5s) | L200 | Hết giờ giải lao! Ăn no, uống đủ, ngửi kỹ, hắt xì xong. Và giờ, các tuyển thủ quay lại sân cho vòng bốn: vòng của những giác quan siêu phàm! |  | Mười tuyển thủ no nê bước ra khỏi căng tin, chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ còn đang hắt xì, chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ còn ôm theo một bó lá, chú Lửng Mật hoạt hình thân đen, lư |

### scene06 · GIÁC QUAN SIÊU PHÀM — AI NHÌN, NGHE, SỜ GIỎI NHẤT · 230.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.4 (8.4s) | L201 | Vòng bốn: giác quan siêu phàm! Trong thế giới hoang dã, ai phát hiện ra đồ ăn trước, và phát hiện ra kẻ thù trước, người đó sống sót. |  | Một phòng thí nghiệm giác quan hoạt hình có năm khu: khu kính lúp, khu tai nghe, khu bàn tay, khu cái mũi, khu bóng đèn; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đứng ở giữa cầm micro. |
| b02 | 00:08.4–00:14.1 (5.7s) | L202 | Ban giám khảo sẽ thử thách các tuyển thủ bằng những bài kiểm tra giác quan mà chính các nhà khoa học đã làm. Mời tuyển thủ đầu tiên! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ đeo một chiếc kính lúp lớn trước mắt, trên bàn trước mặt là một bảng gỗ có những đường rãnh nhỏ khác nhau. |
| b03 | 00:14.1–00:20.2 (6.0s) | L203 | Rái Cá Biển bước tới. Và Rái Cá được thử thách đúng thứ mà nó giỏi nhất: không phải nhìn, mà là... sờ. |  | chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách nằm ngửa cạnh bàn thí nghiệm, giơ hai bàn tay trước nhỏ xíu lên, các ngón tay ngọ nguậy háo hức; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:20.2–00:27.5 (7.3s) | L204 | Ở bang California, các nhà khoa học huấn luyện một cô rái cá tên Selka chạm tay vào những tấm bảng có rãnh, rồi chọn đúng tấm có rãnh rộng 2mm. |  | Một bể nước hoạt hình có hai tấm bảng có rãnh đặt cạnh nhau, chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách cái chìa bàn tay chạm vào tấm bên trái, một nhà khoa học hoạt hình cầm sổ ghi chép bên cạnh; KHÔNG có anh MC trong cảnh này. |
| b05 | 00:27.5–00:34.0 (6.5s) | L205 | Kết quả: Selka phân biệt được những rãnh chỉ chênh nhau khoảng 0,3mm. Mỏng hơn cả... một sợi tóc to! | **0,3 MM** · rãnh chênh lệch · R/360 · [0.5, 0.5] | Hình phóng to hoạt hình hai đường rãnh gần như giống hệt nhau, ở giữa là một sợi tóc người để so sánh độ mỏng, một chiếc thước đo nhỏ xíu đặt bên dưới; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:34.0–00:41.7 (7.7s) | L206 | Và Selka quyết định cực nhanh! Chỉ khoảng 0,2 giây cho mỗi lần chạm tay! Nhanh hơn những người tình nguyện làm cùng bài kiểm tra gần 30 lần! | **x30** · nhanh hơn người · L/360 · [0.5, 0.5] | Một đồng hồ bấm giờ hoạt hình bên cạnh chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách chỉ một vạch nhỏ, bên cạnh là một người tình nguyện đeo kính đang sờ tấm bảng chậm chạp, mặt nhíu mày, chiếc đồng hồ của người đó quay nhiều vòng; KHÔNG có anh MC trong cảnh này. |
| b07 | 00:41.7–00:50.3 (8.6s) | L207 | Vì sao Rái Cá cần đôi tay nhanh như thế? Vì mỗi lần lặn chỉ kéo dài 1-2 phút, dưới đáy biển tối và đục. Nó phải sờ, chọn, và nhét đồ ăn vào túi dưới nách trong chớp mắt. |  | Dưới đáy biển đục ngầu hoạt hình, chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách nhắm mắt, hai bàn tay lướt nhanh qua cát và đá, nhặt một con nhím biển và một con ốc nhét vào túi dưới nách; KHÔNG có anh MC trong cảnh này. |
| b08 | 00:50.3–00:55.7 (5.4s) | L208 | Giám khảo xin ghi nhận: đôi bàn tay của Rái Cá nhạy chẳng kém bàn tay người, mà nhanh gấp bội. |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ chạm thử vào tấm bảng có rãnh bằng đầu cánh, nhíu mày, rồi nhìn sang chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách với vẻ thán phục. |
| b09 | 00:55.7–01:01.9 (6.2s) | L209 | Tuyển thủ tiếp theo: Chim Cánh Cụt. Và thử thách của Cánh Cụt là... nhìn rõ ở cả hai thế giới. Trên cạn, và dưới nước. |  | chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ đứng ở mép hồ, một nửa khung hình là không khí trong vắt có núi băng, một nửa là nước xanh sâu thẳm có đàn cá nhỏ; KHÔNG có anh MC trong cảnh này. |
| b10 | 01:01.9–01:10.7 (8.8s) | L210 | Bạn đã bao giờ mở mắt dưới nước chưa? Mọi thứ nhòe nhoẹt. Vì giác mạc của mắt người cong, nó chỉ hội tụ ánh sáng tốt trong không khí. Xuống nước, nó gần như mất tác dụng. |  | Một người hoạt hình lặn dưới nước mở mắt, mọi thứ xung quanh mờ nhòe như ảnh bị nhòe nước, trên đầu là dấu chấm hỏi; KHÔNG có anh MC trong cảnh này. |
| b11 | 01:10.7–01:19.6 (8.9s) | L211 | Chim cánh cụt giải bài toán này bằng một mẹo khác: giác mạc của chúng phẳng hơn mắt người rất nhiều. Phần việc hội tụ được giao gần hết cho thủy tinh thể, một chiếc thấu kính mềm có thể bóp phồng lên khi |  | Sơ đồ mắt hoạt hình so sánh: mắt người có giác mạc cong như mái vòm, mắt chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ có giác mạc phẳng như cửa kính, bên trong là thủy tinh thể tròn đang được những sợi cơ nhỏ bóp phồng; KHÔNG có anh MC trong cảnh này. |
| b12 | 01:19.6–01:28.0 (8.4s) | L212 | cần. Nhờ vậy, Chim Cánh Cụt nhìn rõ trên băng để tìm đường về tổ, và nhìn rõ dưới nước để bắt cá. Như một chiếc máy ảnh tự động đổi ống kính khi lặn xuống! |  | chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ đeo một chiếc máy ảnh hoạt hình trước ngực, ống kính tự động xoay đổi khi chú nhảy từ tảng băng xuống nước, chú cá nhỏ dưới nước giật mình; KHÔNG có anh MC trong cảnh này. |
| b13 | 01:28.0–01:37.3 (9.3s) | L213 | Tuyển thủ tiếp theo, Koala, bước lên với một bài thi... âm nhạc. Như các bạn đã biết, Koala đực có giọng rống trầm như quái vật. Nhưng giọng rống ấy còn chứa một bí mật. |  | chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ đứng trước một chiếc micro sân khấu, ngại ngùng chỉnh lại áo bệnh nhân, phía sau là dàn loa lớn; KHÔNG có anh MC trong cảnh này. |
| b14 | 01:37.3–01:46.8 (9.5s) | L214 | Năm 2011, các nhà khoa học thu âm tiếng rống của 20 chú Koala đực và phân tích bằng máy tính. Họ phát hiện mỗi chú có một chất giọng riêng, như dấu vân tay âm thanh. | **20 CHÚ** · thu âm tiếng rống · R/360 · [0.5, 0.5] | Màn hình máy tính hoạt hình hiện hai mươi đường sóng âm khác nhau xếp chồng, mỗi đường một màu, bên cạnh là hình hai mươi chú chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ nhỏ, mỗi chú cạnh một đường sóng; KHÔNG có anh MC trong cảnh này. |
| b15 | 01:46.8–01:53.9 (7.2s) | L215 | Và quan trọng hơn: chính những chú Koala khác cũng nhận ra sự khác nhau ấy. Khi nghe một giọng lạ, chúng lập tức quay đầu nhìn về phía loa lâu hơn hẳn. |  | Một chú chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ đang ngồi lim dim trên cây bỗng mở to mắt quay phắt về phía chiếc loa đặt dưới gốc cây, tai dựng lên; KHÔNG có anh MC trong cảnh này. |
| b16 | 01:53.9–02:02.5 (8.6s) | L216 | Các nghiên cứu sau đó còn cho thấy: giọng rống của con đực tiết lộ kích thước cơ thể. Giọng càng trầm, con đực càng to. Và các cô Koala cái... thích những giọng trầm hơn! |  | Một cô chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ cái ngồi trên cành, nghe hai chiếc loa: loa bên trái phát nốt nhạc nhỏ cao, loa bên phải phát nốt nhạc to trầm; cô quay về phía loa bên phải, trái tim nhỏ bay lên; KHÔNG có anh MC trong cảnh này. |
| b17 | 02:02.5–02:05.7 (3.2s) | L217 | Cháu biết rồi, cháu sẽ hát trầm hơn ạ! Ừm... ọ ọ ọ! |  | chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ cố hạ giọng, hai má phồng lên, mắt nhắm tịt, phát ra nốt nhạc vẽ to đùng nhưng méo xệch; KHÔNG có anh MC trong cảnh này. |
| b18 | 02:05.7–02:14.2 (8.5s) | L218 | Tuyển thủ tiếp theo, Cá Heo, mang đến một bài thi về... sự tỉnh táo. Năm 2012, các nhà khoa học ở Mỹ thử xem cá heo có thể canh gác liên tục được bao lâu. |  | chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái bơi trong một hồ nước có tám chiếc loa nhỏ đặt quanh viền hồ, một tấm bảng nút bấm nổi trên mặt nước, một nhà khoa học hoạt hình ngồi trên bờ với ly cà phê; KHÔNG có anh MC trong cảnh này. |
| b19 | 02:14.2–02:24.0 (9.8s) | L219 | Nhiệm vụ: liên tục dùng tiếng định vị để quét quanh hồ, khi nào phát hiện mục tiêu giả do máy phát ra thì bấm nút báo. Mục tiêu xuất hiện bất ngờ, ở bất kỳ hướng nào, vào bất kỳ lúc nào. |  | Sơ đồ hoạt hình nhìn từ trên xuống: chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái ở giữa hồ, những vòng sóng âm tỏa ra tám hướng, ở một hướng có một ngôi sao nhỏ lóe sáng là mục tiêu, cá heo đang bơi về phía nút bấm; KHÔNG có anh MC trong cảnh này. |
| b20 | 02:24.0–02:31.2 (7.3s) | L220 | Một chú cá heo cái đã làm nhiệm vụ này suốt 15 ngày liền. Ngày lẫn đêm! Không nghỉ! Và độ chính xác gần như tuyệt đối từ ngày đầu đến ngày cuối! | **15 NGÀY** · canh gác liên tục · R/360 · [0.5, 0.5] | Cuốn lịch hoạt hình lật liên tục mười lăm trang, xen kẽ mặt trời và mặt trăng, chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái vẫn tỉnh táo bấm nút báo chính xác, trong khi nhà khoa học trên bờ đã ngủ gục bên ly cà phê; KHÔNG có anh MC trong cảnh này. |
| b21 | 02:31.2–02:36.4 (5.1s) | L221 | Và cuộc thử nghiệm chỉ dừng lại vì... một cơn bão mùa đông kéo đến. Không phải vì cá heo mệt! |  | Bầu trời giông bão hoạt hình, mưa xối xả trên hồ, các nhà khoa học mặc áo mưa chạy thu dọn thiết bị, chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái vẫn nhô đầu lên nhìn họ như hỏi: sao dừng rồi?; KHÔNG có anh MC trong cảnh này. |
| b22 | 02:36.4–02:43.8 (7.5s) | L222 | Khán giả của kênh đã biết cá heo ngủ luân phiên từng nửa bộ não. Nhưng phải đến thí nghiệm này, người ta mới thấy cách ngủ ấy cho phép nó canh gác lâu đến mức nào. |  | Hình bộ não chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái hoạt hình chia đôi: nửa trái đội mũ ngủ và ngáy "zzz", nửa phải đeo kính và cầm ống nhòm canh gác; KHÔNG có anh MC trong cảnh này. |
| b23 | 02:43.8–02:53.8 (10.0s) | L223 | Nhưng Chim Cánh Cụt không chịu thua ở môn ngủ! Năm 2023, các nhà khoa học gắn máy đo sóng não lên những chú chim cánh cụt quai mũ đang ấp trứng ở Nam Cực, họ hàng gần của Adélie. |  | Một chú chim cánh cụt có dải lông đen mảnh vắt qua cằm như quai mũ, đang nằm ấp trứng trên tổ sỏi, trên lưng có gắn thiết bị nhỏ có ăng-ten; chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ đứng cạnh chỉ vào như giới thiệu người anh họ; KHÔNG có anh MC trong cảnh này. |
| b24 | 02:53.8–02:59.9 (6.1s) | L224 | Và họ phát hiện: những chú chim này ngủ gật hơn 10.000 lần mỗi ngày! Mỗi giấc chỉ kéo dài khoảng 4 giây! | **10.000** · giấc ngủ mỗi ngày · R/360 · [0.5, 0.5] | Chuỗi hình hoạt hình nhỏ liên tiếp: chú chim cánh cụt quai mũ nhắm mắt gục đầu, mở mắt, nhắm mắt, mở mắt, như đèn nhấp nháy, bên cạnh là đồng hồ bấm giờ chỉ bốn giây; KHÔNG có anh MC trong cảnh này. |
| b25 | 02:59.9–03:09.2 (9.3s) | L225 | Cộng tất cả những giấc ngủ 4 giây ấy lại, chúng ngủ được hơn 11 tiếng mỗi ngày. Mà vẫn kịp canh trứng trước những con chim cướp biển lượn ngay trên đầu! |  | Chú chim cánh cụt quai mũ đang gật gù ngủ thì giật mình mở mắt thấy một con chim cướp biển màu nâu đang lượn gần, chú lập tức xù lông dọa, rồi lại gục đầu ngủ tiếp; KHÔNG có anh MC trong cảnh này. |
| b26 | 03:09.2–03:18.8 (9.7s) | L226 | Giám khảo xin tổng kết vòng bốn: đôi tay nhạy, đôi mắt hai thế giới, giọng hát mang tên riêng, và người lính gác không bao giờ ngủ trọn giấc. Một vòng thi rất khó chấm! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ đặt bốn tấm thẻ lên bàn: bàn tay, con mắt, nốt nhạc, chiếc đèn pin, rồi gãi đầu suy nghĩ, chiếc bút chì kẹp sau tai. |
| b27 | 03:18.8–03:23.3 (4.5s) | L227 | Kết quả vòng bốn! Huy chương đồng: Chim Cánh Cụt, đôi mắt hai thế giới và giấc ngủ 4 |  | Bục trao giải: chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ đứng bậc đồng, đeo huy chương đồng, đeo kính lặn trên trán, mắt lim dim như sắp ngủ gật; KHÔNG có anh MC trong cảnh này. |
| b28 | 03:23.3–03:28.6 (5.3s) | L228 | giây! Huy chương bạc: Rái Cá Biển, bàn tay nhạy và nhanh gấp 30 lần người! Và huy chương vàng... |  | chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách đứng bậc bạc giơ hai bàn tay lên khoe, đeo huy chương bạc; bậc vàng phía trên có ánh đèn spotlight chiếu xuống, chưa ai đứng; KHÔNG có anh MC trong cảnh này. |
| b29 | 03:28.6–03:31.6 (3.0s) | L229 | Thuộc về Cá Heo, người lính gác 15 ngày không ngủ! |  | chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái nhảy vọt lên khỏi bể nước trên bậc vàng, đeo huy chương vàng, đội chiếc mũ lính gác nhỏ; KHÔNG có anh MC trong cảnh này. |
| b30 | 03:31.6–03:43.3 (11.7s) | L230 | Bảng điểm sau bốn vòng: Thú Mỏ Vịt vẫn dẫn đầu với 6 điểm! Chồn Gulo 4 điểm. Chim Cánh Cụt 4 điểm. Rái Cá 3 điểm. Cá Heo 3 điểm. Bồ Nông 2 điểm. Koala và Tôm Tít 1 điểm. Lửng Mật và Gấu Nước: vẫn chưa có điểm! |  | tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) sáng lên: cột chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá cao nhất, hai cột chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên s |
| b31 | 03:43.3–03:50.4 (7.1s) | L231 | Vòng tiếp theo sẽ không chấm khả năng tìm đồ ăn. Mà chấm khả năng chăm sóc một sinh mạng nhỏ bé. Vòng năm: những người cha, người mẹ phi thường. |  | Một chiếc tổ nhỏ hoạt hình nằm giữa ánh đèn sân khấu dịu nhẹ, bên trong là một quả trứng nhỏ, xung quanh tối dần; KHÔNG có anh MC trong cảnh này. |

### scene07 · ĐÊM TRƯỚC VÒNG QUYẾT ĐỊNH — AI NGỦ, AI THỨC, AI TẬP LUYỆN · 153.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:06.8 (6.8s) | L232 | Đêm buông xuống sân vận động. Đại hội tạm nghỉ trước bốn vòng cuối. Các tuyển thủ trở về khu nghỉ ngơi. Nhưng không phải ai cũng ngủ... |  | Sân vận động hoạt hình ban đêm, đèn đã tắt gần hết, chỉ còn ánh trăng, phía xa là khu nhà nghỉ của tuyển thủ với vài ô cửa sổ còn sáng đèn; KHÔNG có anh MC trong cảnh này. |
| b02 | 00:06.8–00:12.1 (5.2s) | L233 | Máy quay hậu trường của chúng tôi đi một vòng khu nghỉ ngơi. Và những gì nó ghi lại được... rất đáng xem. |  | Một chiếc máy quay hoạt hình có đèn đỏ nhấp nháy đang lén lút đi dọc hành lang tối, ống kính chĩa vào khe cửa một phòng nghỉ; KHÔNG có anh MC trong cảnh này. |
| b03 | 00:12.1–00:16.5 (4.5s) | L234 | Phòng số một: Chồn Gulo. Không ngủ. Đang... leo núi. Ngay trong đêm. |  | Qua cửa sổ phòng nghỉ, thấy chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh đang leo một bức tường leo núi trong nhà, phía sau cửa sổ là dãy núi tuyết dưới ánh trăng; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:16.5–00:24.4 (7.9s) | L235 | Ở công viên quốc gia Glacier nước Mỹ, các nhà nghiên cứu theo dõi bằng vòng cổ định vị nhận xét: Chồn Gulo có thể đi 150-200km mỗi tuần trong công | **150-200 KM** · mỗi tuần · R/360 · [0.5, 0.5] | Một bản đồ công viên quốc gia hoạt hình có núi tuyết, hồ nước và rừng thông, trên đó là đường đi dài màu đỏ của chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh đeo vòng cổ có ăng-ten; KHÔNG có anh MC trong cảnh này. |
| b05 | 00:24.4–00:30.8 (6.3s) | L236 | viên. Và chúng rất ít khi đi đường vòng. Gặp núi thì leo, gặp đường thì băng qua. Đúng là đi đâu cũng... đi thẳng! |  | Một bản đồ hoạt hình có nhiều đường thẳng tắp như kẻ thước cắt ngang qua núi, qua sông, qua đường; chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh đứng ở đầu một đường thẳng, đội mũ bảo hiểm leo núi, giơ ngón cái; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:30.8–00:38.7 (7.9s) | L237 | Phòng số hai: Thú Mỏ Vịt. Đèn tắt. Tuyển thủ đang dẫn đầu bảng điểm đang ngủ say. Nhưng hãy nhìn kỹ... cái mỏ đang giật giật, và mắt đang đảo liên tục dưới mí. |  | Trong phòng tối hoạt hình, chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá cuộn tròn ngủ trong ổ chăn, chiếc vương miện đồ chơi đặt trên bàn đầu giường, cái mỏ khẽ giật, mí mắt rung rung; KHÔNG có anh MC trong cảnh này. |
| b07 | 00:38.7–00:47.8 (9.1s) | L238 | Đó là giai đoạn ngủ mơ, giai đoạn mà ở người, chúng ta thường nằm mơ. Và Thú Mỏ Vịt giữ kỷ lục: hơn 8 tiếng ngủ mơ mỗi ngày, nhiều hơn bất kỳ loài động vật nào từng |  | Phía trên đầu chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá là bong bóng giấc mơ khổng lồ: Thú Mỏ Vịt đang đứng trên bục vô địch, xung quanh là những con tôm nhỏ vỗ tay; một chiếc cúp nhỏ ghi kỷ lục (không chữ) đặt cạnh giường; KHÔNG có anh MC trong cảnh này. |
| b08 | 00:47.8–00:57.7 (9.9s) | L239 | được đo. Các nhà khoa học đoán rằng giấc ngủ mơ có thể đã xuất hiện từ rất sớm ở những loài thú đầu tiên, và Thú Mỏ Vịt, thuộc nhóm thú đẻ trứng đã tách ra từ rất xa xưa, có thể đang giữ lại dấu vết đó. |  | Một cây gia phả hoạt hình cổ kính, ở gốc rễ là hình chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá đang ngủ với bong bóng giấc mơ, các cành phía trên là hình các loài thú khác cũng đang ngủ; KHÔNG có anh MC trong cảnh này. |
| b09 | 00:57.7–01:02.8 (5.1s) | L240 | Phòng số ba: Chim Cánh Cụt. Mắt nhắm. Mở. Nhắm. Mở. Nó không ngủ một giấc dài. Nó ngủ... hàng ngàn giấc |  | Trong phòng nghỉ hoạt hình, chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ đứng ngủ cạnh tổ sỏi nhỏ mang theo từ nhà, mắt nhấp nháy liên tục, xung quanh có những chữ "zzz" nhỏ xíu xuất hiện rồi biến mất; KHÔNG có anh MC trong cảnh này. |
| b10 | 01:02.8–01:11.7 (8.9s) | L241 | ngắn. Như vòng bốn đã kể, họ hàng của nó, chim cánh cụt quai mũ, có thể ngủ hơn 10.000 giấc mỗi ngày, mỗi giấc khoảng 4 giây. Ngủ kiểu ấy để làm gì? Để không bao giờ lơ là canh tổ. |  | chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ đang gật gù bỗng mở to mắt khi nghe tiếng động ngoài cửa sổ, nơi bóng một con chim cướp biển lượn qua dưới ánh trăng, chú lập tức che chắn tổ sỏi; KHÔNG có anh MC trong cảnh này. |
| b11 | 01:11.7–01:19.5 (7.8s) | L242 | Phòng số bốn: Rái Cá Biển. Phòng này... có bể nước. Và Rái Cá đang nằm ngửa trên mặt nước, hai bàn tay úp lên mắt, ngủ ngon lành. |  | Một phòng nghỉ hoạt hình có bồn tắm lớn, chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách nằm ngửa trên mặt nước, hai bàn tay úp lên mắt như đeo mặt nạ ngủ, một dải tảo bẹ quấn quanh bụng buộc vào vòi nước; KHÔNG có anh MC trong cảnh này. |
| b12 | 01:19.5–01:29.1 (9.6s) | L243 | Các nhà khoa học cho biết, mỗi ngày Rái Cá Biển dành khoảng 11 tiếng để nghỉ ngơi và ngủ, khoảng 8 tiếng để kiếm ăn, và 5 tiếng để chải lông và vui chơi. Một lịch trình... đáng mơ ước! |  | Một chiếc đồng hồ tròn hoạt hình chia ba phần màu: phần xanh có biểu tượng giường ngủ, phần cam có biểu tượng con cua, phần hồng có biểu tượng chiếc lược và quả bóng; chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách đứng cạnh giơ ngón cái; KHÔNG có anh MC trong cảnh này. |
| b13 | 01:29.1–01:36.7 (7.6s) | L244 | Phòng số năm: Gấu Nước. Máy quay soi qua kính hiển vi... và thấy Gấu Nước đang tập thể dục! Nó đi tới đi lui trên tấm thảm thạch rau |  | Qua kính hiển vi hoạt hình, chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương mặc chiếc áo thể thao tí hon đi tới đi lui trên một tấm thạch trong suốt, đeo băng đô thể thao; KHÔNG có anh MC trong cảnh này. |
| b14 | 01:36.7–01:47.1 (10.4s) | L245 | câu. Năm 2020 mốt, các nhà khoa học đã quay phim gấu nước đi bộ trên những tấm thạch, và phát hiện ra một điều bất ngờ: gấu nước đi giống hệt... côn trùng! Dù côn trùng to gấp khoảng 500.000 lần. | **x500.000** · côn trùng to hơn · R/360 · [0.75, 0.5] | Chia đôi khung hình: bên trái chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương đi bằng tám chân với những dấu chân đánh số thứ tự nhịp bước; bên phải một chú bọ cánh cứng to lớn đi với nhịp bước giống hệt; KHÔNG có anh MC trong cảnh này. |
| b15 | 01:47.1–01:57.2 (10.1s) | L246 | Lúc đi dạo, gấu nước đi khoảng nửa thân mình mỗi giây. Khi gấp gáp, nó có thể tăng tốc lên khoảng hai thân mình mỗi giây. Nghe thì chậm, nhưng với một sinh vật nhỏ hơn hạt cát, đó là... chạy nước rút! |  | chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương đang chạy nước rút trên đường chạy tí hon, mồ hôi bay ra, các nét gió tốc độ phía sau, ở vạch đích có một chiếc cờ nhỏ bằng hạt bụi; KHÔNG có anh MC trong cảnh này. |
| b16 | 01:57.2–02:03.9 (6.8s) | L247 | Phòng số sáu, phòng cuối cùng: Lửng Mật. Cửa phòng mở. Giường trống. Trên tường có một cái lỗ to. Lửng Mật... đã vượt ngục. Một lần nữa. |  | Một phòng nghỉ hoạt hình trống trơn, giường chăn gối xộc xệch, trên tường có một cái lỗ tròn to đào xuyên ra ngoài, đất cát rơi vãi, ánh trăng chiếu qua lỗ; KHÔNG có anh MC trong cảnh này. |
| b17 | 02:03.9–02:12.1 (8.1s) | L248 | Máy quay chạy theo dấu chân và tìm thấy Lửng Mật đang ngồi ngoài sân, dưới ánh trăng, bên cạnh... chú lửng con của mình. Hai mẹ con đang tập đào hang. |  | Ngoài sân dưới ánh trăng hoạt hình, chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần mẹ và lửng con cùng đào một cái hố nhỏ, mẹ làm mẫu, con bắt chước theo vụng về, hai mẹ con dính đầy đất cát nhưng rất vui vẻ; KHÔNG có anh MC trong cảnh này. |
| b18 | 02:12.1–02:19.6 (7.5s) | L249 | Hóa ra gã giang hồ nổi tiếng nhất đại hội, đêm nay không đi gây sự. Nó chỉ dành thời gian dạy con. Mai là vòng thi về cha mẹ. Và Lửng Mật... đã sẵn sàng. |  | Cận cảnh chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần mẹ ôm lửng con ngồi dưới ánh trăng, hai mẹ con nhìn lên bầu trời đầy sao, phía xa là sân vận động im lặng; KHÔNG có anh MC trong cảnh này. |
| b19 | 02:19.6–02:29.7 (10.2s) | L250 | Máy quay hậu trường xin phép tắt đèn đỏ, rút êm khỏi khu nghỉ ngơi. Vì nếu Lửng Mật phát hiện ra mình bị quay lén... thì người tiếp theo phải đào hầm trốn chính là đội quay phim! |  | Chiếc máy quay hoạt hình có đèn đỏ nhấp nháy rón rén lùi ra khỏi sân, phía sau hai mắt chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần sáng lóe trong bóng tối nhìn theo, người quay phim toát mồ hôi; KHÔNG có anh MC trong cảnh này. |
| b20 | 02:29.7–02:33.9 (4.2s) | L251 | Trời sáng dần. Mặt trời mọc trên sân vận động. Và còn đúng... bốn vòng thi nữa. |  | Bình minh hoạt hình rực rỡ trên sân vận động, ánh nắng đầu tiên chiếu lên chiếc vương miện bé xíu trên bệ đá giữa sân, chim hót trên mái khán đài; KHÔNG có anh MC trong cảnh này. |

### scene08 · CHA MẸ PHI THƯỜNG — AI NUÔI CON GIỎI NHẤT HOANG DÃ · 264.0s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:06.1 (6.1s) | L252 | Vòng năm: cha mẹ phi thường! Sống sót một mình đã khó. Vừa sống sót, vừa nuôi một đứa con bé bỏng, còn khó hơn gấp bội. |  | Sân khấu hoạt hình được trang trí như một căn phòng em bé ấm áp, có nôi, có thú bông, có những tổ chim nhỏ, anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đứng ở giữa nói nhỏ nhẹ. |
| b02 | 00:06.1–00:11.4 (5.3s) | L253 | Giám khảo sẽ chấm: ai chăm con chu đáo nhất, ai dạy con kiên nhẫn nhất, và ai có chiêu nuôi con... độc nhất vô nhị. |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ đeo chiếc tạp dề có hình trái tim, cầm bình sữa nhỏ, ngồi ở bàn giám khảo với vẻ hiền từ. |
| b03 | 00:11.4–00:20.8 (9.4s) | L254 | Mở màn là Lửng Mật, tuyển thủ vẫn đang trắng điểm sau bốn vòng. Và Lửng Mật mẹ khiến cả khán đài bất ngờ: gã giang hồ dữ dằn ấy hóa ra là một bà mẹ... vô cùng cẩn thận. |  | chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần mẹ bước lên sân khấu, miệng ngậm nhẹ nhàng một chú lửng con bé xíu hồng hào chưa có lông, vẻ mặt dịu dàng hiếm thấy; khán đài ồ lên ngạc nhiên; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:20.8–00:27.9 (7.1s) | L255 | Ở sa mạc Kalahari, Lửng Mật mẹ thường chỉ nuôi một con mỗi lứa. Lửng con mới sinh không có lông, mắt nhắm nghiền, và phải hai tháng sau mới mở mắt. |  | Trong hang đất hoạt hình, một chú lửng con bé xíu trụi lông, mắt nhắm, nằm cuộn tròn trên lớp cỏ khô, chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần mẹ nằm che chắn bên cạnh; KHÔNG có anh MC trong cảnh này. |
| b05 | 00:27.9–00:37.4 (9.5s) | L256 | Và để giữ an toàn cho con, cứ vài ngày Lửng Mật mẹ lại ngậm con trong miệng, mang sang một cái hang mới. Trung bình chỉ ở mỗi hang khoảng 3 ngày, hang này cách hang kia khoảng 2km! | **~2 KM** · mỗi lần chuyển hang · R/360 · [0.5, 0.5] | Bản đồ sa mạc hoạt hình có nhiều chấm hang nối bằng đường chấm chấm, chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần mẹ đang ngậm con đi trên đường giữa hai hang dưới ánh trăng; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:37.4–00:46.1 (8.7s) | L257 | Lửng con ở với mẹ ít nhất 14 tháng. Suốt thời gian ấy, mẹ dạy con đào hang, leo cây, bắt chuột, và cả cách đối phó với rắn độc. Một khóa học sinh tồn kéo dài hơn một năm! | **14 THÁNG** · học cùng mẹ · L/360 · [0.45, 0.5] | chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần mẹ đứng cạnh một tấm bảng đen hoạt hình vẽ hình cái xẻng, cái cây, con chuột và con rắn, lửng con ngồi chăm chú như học sinh, cầm bút chì ghi chép; KHÔNG có anh MC trong cảnh này. |
| b07 | 00:46.1–00:50.8 (4.8s) | L258 | Giám khảo xin ghi nhận: bà mẹ chuyển nhà nhiều nhất, và dạy con lâu nhất cuộc thi. |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gật đầu ghi chép, mắt hơi rưng rưng, đặt một ngôi sao vàng nhỏ lên bảng cạnh hình đầu chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần. |
| b08 | 00:50.8–00:57.1 (6.3s) | L259 | Tuyển thủ tiếp theo, Thú Mỏ Vịt mẹ, trình bày cách làm tổ đẻ trứng. Đúng vậy, một loài thú có sữa... mà lại đẻ trứng! |  | chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá mẹ đeo nơ hồng, cầm trên tay hai quả trứng nhỏ màu trắng ngà, vỏ mềm như giấy da, khán giả trên khán đài há hốc mồm; KHÔNG có anh MC trong cảnh này. |
| b09 | 00:57.1–01:06.4 (9.3s) | L260 | Trước khi đẻ, Thú Mỏ Vịt mẹ đào một đường hầm dài dọc bờ sông, có khi tới 20 mét. Rồi tha lá ướt và cành nhỏ vào trải ổ, bằng cách... kẹp chúng giữa đuôi và chân sau! |  | Mặt cắt ngang bờ sông hoạt hình có đường hầm dài ngoằn ngoèo, chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá mẹ đang đi giật lùi trong hầm, đuôi cuộn kẹp một bó lá ướt; KHÔNG có anh MC trong cảnh này. |
| b10 | 01:06.4–01:14.0 (7.6s) | L261 | Và mỗi lần ra khỏi hang, mẹ lại đắp đất bịt kín đường hầm thành nhiều lớp, có khi tới 9 lớp. Để ngăn kẻ thù, và để giữ cho ổ không bị ngập khi nước sông dâng. |  | Đường hầm hoạt hình có những bức tường đất nhỏ chắn ngang thành nhiều lớp như những cánh cửa, chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá mẹ đang dùng đuôi vỗ chặt lớp đất cuối cùng; KHÔNG có anh MC trong cảnh này. |
| b11 | 01:14.0–01:23.0 (9.0s) | L262 | Thú Mỏ Vịt mẹ đẻ từ 1 đến 3 trứng, thường là hai. Rồi mẹ cuộn tròn người, ôm trứng giữa bụng và đuôi suốt khoảng 10 ngày để ấp, cho đến khi những chú con bé như hạt đậu chui ra. |  | chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá mẹ cuộn tròn trong ổ lá, ôm hai quả trứng nhỏ giữa bụng và đuôi, ánh sáng ấm áp; một quả trứng đang nứt, lộ ra cái mỏ bé xíu; KHÔNG có anh MC trong cảnh này. |
| b12 | 01:23.0–01:32.2 (9.1s) | L263 | Tuyển thủ tiếp theo, Rái Cá Biển mẹ, bước lên với một chú con nằm trên ngực. Rái cá con mới sinh có bộ lông xù đến mức... không thể lặn xuống nước được. Nó nổi bồng bềnh như cái phao! |  | chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách mẹ nằm ngửa trên mặt biển, trên ngực là một chú rái cá con lông xù màu nâu nhạt tròn như quả bóng bông, đang ngủ ngon lành; KHÔNG có anh MC trong cảnh này. |
| b13 | 01:32.2–01:41.7 (9.5s) | L264 | Nên khi mẹ phải lặn xuống đáy biển kiếm ăn, mẹ để con nổi trên mặt nước, có khi còn quấn con vào tảo bẹ cho khỏi trôi. Rồi mẹ ngoi lên, lại đặt con lên ngực, chải lông, cho bú. |  | Chú rái cá con lông xù được quấn nhẹ trong dải tảo bẹ nổi trên mặt nước như trong chiếc nôi, dưới nước sâu chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách mẹ đang lặn tìm cua; KHÔNG có anh MC trong cảnh này. |
| b14 | 01:41.7–01:51.5 (9.8s) | L265 | Rái cá con phụ thuộc vào mẹ khoảng 6 đến 8 tháng. Mẹ dạy con lặn, dạy con chọn món ăn, và quan trọng nhất: dạy con dùng hòn đá đập vỏ. Rái cá con thường thích ăn những món giống hệt món mẹ thích! | **6-8 THÁNG** · học cùng mẹ · R/360 · [0.5, 0.5] | chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách mẹ và con nằm ngửa cạnh nhau, mỗi bạn kẹp một hòn đá, mẹ làm mẫu đập vỏ sò, con bắt chước theo với vẻ mặt chăm chú, trên bụng mỗi bạn là cùng một loại con sò; KHÔNG có anh MC trong cảnh này. |
| b15 | 01:51.5–01:58.8 (7.4s) | L266 | Tuyển thủ tiếp theo, Cá Heo mẹ, trình bày một thứ mà các nhà khoa học mới phát hiện năm 2023: cá heo mẹ cũng nói giọng... nựng con! |  | chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái mẹ bơi cạnh một chú cá heo con nhỏ xíu, từ miệng cá heo mẹ bay ra những nốt nhạc hình trái tim; KHÔNG có anh MC trong cảnh này. |
| b16 | 01:58.8–02:08.2 (9.3s) | L267 | Các nhà khoa học ở bang Florida đã ghi âm 19 cá heo mẹ, khi có con bên cạnh, và khi không có con. Và tất cả các cá heo mẹ đều thay đổi tiếng huýt sáo khi có con ở gần. | **19** · cá heo mẹ · R/360 · [0.5, 0.5] | Hai đường sóng âm hoạt hình so sánh: đường thứ nhất bình thường, đường thứ hai vọt lên cao hơn và rộng hơn, bên cạnh là hình cá heo mẹ có cá heo con bơi cạnh; KHÔNG có anh MC trong cảnh này. |
| b17 | 02:08.2–02:18.9 (10.8s) | L268 | Tiếng huýt sáo cao hơn, và rộng giọng hơn. Giống hệt cách các bà mẹ con người tự nhiên nói giọng cao, ngân nga khi nựng em bé. Hai loài khác nhau, sống ở hai thế giới khác nhau, mà lại có chung một cách nói với con. |  | Chia đôi khung hình: bên trái một bà mẹ người hoạt hình ôm em bé nói chuyện, những nốt nhạc nhỏ bay ra; bên phải chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái mẹ bơi cạnh con, những nốt nhạc giống hệt bay ra; KHÔNG có anh MC trong cảnh này. |
| b18 | 02:18.9–02:30.8 (11.9s) | L269 | Và cuối cùng, Chồn Gulo mẹ. Như vòng một đã kể, chồn mẹ đào hang dưới lớp tuyết dày để sinh con. Nhưng chồn mẹ còn một chiêu nữa: khi cần, chồn mẹ dời con sang hang khác, có khi dùng nhiều hang khác nhau trước khi con cai |  | chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh mẹ đang ngậm một chú chồn con lông trắng xám nhỏ xíu, đi trên tuyết dưới bầu trời sao từ một hang tuyết này sang một hang tuyết khác; KHÔNG có anh MC trong cảnh này. |
| b19 | 02:30.8–02:41.4 (10.6s) | L270 | sữa. Chồn con được nuôi trong hang đến khoảng 9-10 tuần tuổi, rồi mới bắt đầu theo mẹ ra ngoài. Và ở Bắc Mỹ, các nhà khoa học còn thấy chồn bố thỉnh thoảng quay lại thăm con, dẫn con đi khám phá lãnh thổ. |  | chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh bố dẫn hai chú chồn con đi trên sườn núi tuyết, chồn con lon ton theo sau, một chú bị trượt chân lăn tuyết, chồn bố quay lại nhìn; KHÔNG có anh MC trong cảnh này. |
| b20 | 02:41.4–02:52.2 (10.8s) | L271 | Tuyển thủ tiếp theo, Chim Cánh Cụt, trình bày một hệ thống chăm con kiểu... đổi ca trực. Chim Cánh Cụt Adélie thường đẻ hai trứng, và bố mẹ thay phiên nhau ấp, mỗi ca thường kéo dài khoảng 12 ngày. | **~12 NGÀY** · mỗi ca ấp · R/360 · [0.5, 0.5] | Một tấm lịch trực hoạt hình treo cạnh tổ sỏi, các ô xen kẽ hình chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ bố đeo nơ đỏ và chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ mẹ đeo nơ hồng, giữa tổ là hai quả trứng; KHÔNG có anh M |
| b21 | 02:52.2–03:00.8 (8.6s) | L272 | Nhưng ca đầu tiên là ca khổ nhất. Chim bố ở lại ấp trong khi chim mẹ ra biển kiếm ăn. Tính cả mùa tán tỉnh trước đó, chim bố có thể nhịn đói khoảng một tháng liền mà không rời tổ. |  | chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ bố gầy rộc đi, chiếc nơ đỏ trễ xuống, bụng kêu ọt ọt có vẽ bong bóng hình con tôm, nhưng vẫn ngồi im ôm hai quả trứng giữa trời gió tuyết; KHÔNG có anh MC trong cảnh này. |
| b22 | 03:00.8–03:12.6 (11.8s) | L273 | Khi chim con được khoảng ba tuần tuổi, chúng đã đủ lớn để không cần bố mẹ ủ ấm. Chúng tụ tập thành những nhóm đông gọi là "nhà trẻ", đứng sát vào nhau để giữ ấm và chống lại chim săn mồi. Còn bố mẹ thì cùng nhau ra biển, kiếm cá về nuôi con. |  | Một nhóm đông chim cánh cụt con lông xám bông xù đứng sát vào nhau như một nhà trẻ ngoài trời, có vài chú lớn đứng canh ngoài rìa, phía xa chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ bố mẹ cùng lạch bạch đi về phía biển; KHÔNG có anh MC trong cảnh này. |
| b23 | 03:12.6–03:22.8 (10.2s) | L274 | Và một bất ngờ đến từ Tôm Tít! Gã võ sĩ đại dương có một người họ hàng nhỏ xíu, loài tôm tít Pullosquilla, sống ở Ấn Độ Dương và Thái Bình Dương. Và loài này... nuôi con bằng cả bố lẫn mẹ! |  | Một chiếc hang chữ U dưới cát hoạt hình, bên trong có hai chú tôm tít nhỏ xíu nằm hai đầu hang, mỗi chú ôm một ổ trứng nhỏ màu hồng; chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh đứng bên ngoài chỉ vào như giới thiệu họ hàng; KHÔNG có anh MC trong cảnh này. |
| b24 | 03:22.8–03:34.5 (11.7s) | L275 | Cả bố và mẹ đều quạt nước cho trứng để trứng có đủ ô-xy, nhặt bỏ trứng hỏng, và di chuyển ổ trứng trong hang. Khi thức ăn dồi dào, tôm mẹ có thể đẻ thêm ổ thứ hai khi ổ thứ nhất chưa nở. Và lúc ấy, cả hai vợ chồng cùng chăm hai ổ trứng! |  | Hai chú tôm tít nhỏ trong hang quạt những chiếc chân bơi tạo dòng nước nhỏ thổi qua hai ổ trứng, một chú đang nhặt một quả trứng màu xám ra ngoài; KHÔNG có anh MC trong cảnh này. |
| b25 | 03:34.5–03:43.4 (8.9s) | L276 | Theo các nhà khoa học, trong số các loài giáp xác sống ở biển, đây là nhóm duy nhất từng được nghiên cứu kỹ về việc cả bố lẫn mẹ cùng chăm trứng. Võ sĩ ngoài đời, ông bố mẫu mực trong hang! |  | chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh đeo tạp dề hồng, một càng cầm chiếc quạt nhỏ, một càng bế ổ trứng, vẻ mặt nghiêm túc của một ông bố; KHÔNG có anh MC trong cảnh này. |
| b26 | 03:43.4–03:50.0 (6.6s) | L277 | Ban giám khảo xin phép nghỉ giải lao một chút... để lau nước mắt. Đây là vòng thi xúc động nhất từ đầu đại hội đến giờ! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ và anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cùng rút khăn tay ra lau mắt, khán đài hoạt hình cũng sụt sùi, có chú thỏ đang khóc nức nở vào vai chú sóc. |
| b27 | 03:50.0–03:54.4 (4.4s) | L278 | Kết quả vòng năm! Huy chương đồng: Cá Heo mẹ, giọng nựng con của đại dương! |  | Bục trao giải: chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái mẹ đứng bậc đồng cùng cá heo con, đeo huy chương đồng; KHÔNG có anh MC trong cảnh này. |
| b28 | 03:54.4–03:58.1 (3.7s) | L279 | Huy chương bạc: Thú Mỏ Vịt mẹ, kỹ sư đường hầm 9 lớp cửa! Và huy chương vàng... |  | chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá mẹ đeo nơ hồng đứng bậc bạc, ôm hai quả trứng; bậc vàng phía trên phủ ánh đèn ấm áp, khán đài nín thở; KHÔNG có anh MC trong cảnh này. |
| b29 | 03:58.1–04:03.1 (5.0s) | L280 | Thuộc về Lửng Mật! Bà mẹ ngậm con chuyển nhà mỗi 3 ngày, và dạy con suốt hơn một năm trời! |  | chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần mẹ đứng trên bậc vàng, đeo huy chương vàng, lửng con nhỏ xíu ngồi trên đầu mẹ đội chiếc mũ tốt nghiệp nhỏ, khán đài đứng dậy vỗ tay; KHÔNG có anh MC trong cảnh này. |
| b30 | 04:03.1–04:15.8 (12.7s) | L281 | Lửng Mật cuối cùng cũng có điểm! Bảng điểm sau năm vòng: Thú Mỏ Vịt 8 điểm! Cá Heo 4 điểm, Chồn Gulo 4 điểm, Chim Cánh Cụt 4 điểm! Lửng Mật 3 điểm. Rái Cá 3 điểm. Bồ Nông 2 điểm. Koala, Tôm Tít 1 điểm. Gấu Nước vẫn trắng tay. |  | tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) sáng lên: cột chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá vọt lên cao nhất, ba cột bằng nhau ở vị trí thứ hai, cột chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc  |
| b31 | 04:15.8–04:24.0 (8.2s) | L282 | Gấu Nước ngước nhìn bảng điểm, và lần đầu tiên, sinh vật bất tử ấy có vẻ... lo lắng. Vì vòng sáu sẽ không cần đến những siêu năng lực chịu đựng. Vòng sáu cần sự đoàn kết. |  | Cận cảnh chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương tí hon đứng một mình giữa sân thi đấu rộng mênh mông, cái bóng nhỏ xíu đổ dài, nhìn về phía những tuyển thủ khác đang đứng thành nhóm; KHÔNG có anh MC trong cảnh này. |

### scene09 · SỨC MẠNH ĐỒNG ĐỘI — AI BIẾT HỢP TÁC, AI NHỚ BẠN LÂU NHẤT · 292.5s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:05.9 (5.9s) | L283 | Vòng sáu: sức mạnh đồng đội! Một cây làm chẳng nên non, ba cây chụm lại... thì thành một đàn cá heo! |  | Ba cây nhỏ hoạt hình chụm lại thành ngọn núi, rồi biến hình thành ba chú chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái nhảy lên khỏi mặt nước cùng lúc; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đứng cạnh giơ ngón cái. |
| b02 | 00:05.9–00:12.5 (6.7s) | L284 | Giám khảo chấm ba tiêu chí: biết làm việc với đồng loại, biết hợp tác với loài khác, và quan trọng nhất: biết... nhớ bạn bè. |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ giơ lên ba tấm thẻ có biểu tượng: hai bàn tay nắm nhau, hai con vật khác loài bắt tay, và một bộ não có trái tim nhỏ bên trong. |
| b03 | 00:12.5–00:21.5 (9.0s) | L285 | Cá Heo bước vào sân, và lần này, giám khảo đồng ý cho Cá Heo kể trọn câu chuyện còn dang dở ở vòng ba. Câu chuyện ở thị trấn Laguna, miền Nam nước Brazil. |  | chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái nhô lên giữa một con kênh dẫn ra biển, hai bên bờ là những ngôi nhà sơn màu tươi sáng, người dân đứng dọc bờ cầm lưới; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:21.5–00:30.2 (8.7s) | L286 | Ở đây, mỗi mùa cá đối di cư, những người đánh cá đứng thành hàng dưới nước, nước ngập ngang hông, tay cầm sẵn chiếc lưới quăng tròn. Nhưng họ không nhìn mặt nước. Họ nhìn... cá heo. |  | Một hàng người đánh cá hoạt hình đội mũ rộng vành đứng dưới nước ngang hông, tay cầm lưới tròn, tất cả cùng chăm chú nhìn về phía chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái đang bơi tới; KHÔNG có anh MC trong cảnh này. |
| b05 | 00:30.2–00:37.0 (6.8s) | L287 | Cá Heo dồn đàn cá đối vào sát bờ. Rồi bất ngờ, nó lặn sâu xuống thật nhanh, hoặc quẫy đầu, quẫy đuôi ngay trước mặt người đánh cá. Đó là tín hiệu! |  | chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái lặn ngoắt xuống nước tạo bọt nước trắng, ngay trước mặt một người đánh cá; người đánh cá mở to mắt, cơ bắp căng ra chuẩn bị quăng lưới; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:37.0–00:43.1 (6.1s) | L288 | Người đánh cá lập tức quăng lưới! Lưới chụp xuống, cá đối hoảng loạn tán loạn, và Cá Heo lao vào bắt những con cá chạy khỏi đàn. |  | Chiếc lưới tròn bung ra giữa không trung chụp xuống mặt nước, dưới nước đàn cá đối tán loạn, chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái há miệng đớp một con cá đang chạy thoát; KHÔNG có anh MC trong cảnh này. |
| b07 | 00:43.1–00:51.6 (8.5s) | L289 | Năm 2023, các nhà khoa học dùng máy bay không người lái, thiết bị định vị đeo tay và cả micro dưới nước để đo đạc sự hợp tác này. Và các con số khiến họ kinh ngạc. |  | Một chiếc máy bay không người lái hoạt hình lơ lửng trên con kênh, dưới nước có chiếc micro nhỏ, một người đánh cá đeo đồng hồ định vị trên cổ tay; KHÔNG có anh MC trong cảnh này. |
| b08 | 00:51.6–00:58.3 (6.7s) | L290 | Khi có Cá Heo ra tín hiệu, người đánh cá có khả năng bắt được cá cao gấp 17 lần, và bắt được số cá nhiều gần gấp 4 lần so với khi không có Cá Heo! | **x17** · khả năng bắt cá · R/360 · [0.7, 0.5] | Hai chiếc giỏ cá hoạt hình so sánh: giỏ bên trái gần như trống chỉ có một con cá nhỏ, giỏ bên phải đầy ắp cá đối tràn ra ngoài; chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái nháy mắt bên cạnh giỏ đầy; KHÔNG có anh MC trong cảnh này. |
| b09 | 00:58.3–01:06.7 (8.3s) | L291 | Và Cá Heo cũng được lợi: những con cá heo tham gia hợp tác có tỷ lệ sống sót cao hơn khoảng 13%, vì chúng ít phải đi kiếm ăn ở những vùng có lưới đánh bắt nguy hiểm. | **+13%** · tỷ lệ sống sót · L/380 · [0.45, 0.5] | chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái bơi an toàn trong con kênh, phía xa ngoài biển là những tấm lưới kéo lớn nguy hiểm có biển báo cấm màu đỏ, chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái quay đầu tránh xa; KHÔNG có anh MC trong cảnh này. |
| b10 | 01:06.7–01:15.9 (9.2s) | L292 | Điều kỳ diệu là sự hợp tác này đã diễn ra ở đây hơn 100 năm, truyền từ đời ông sang đời cháu của cả người lẫn cá heo. Người dân còn đặt tên riêng cho từng chú cá heo quen mặt. |  | Một ông lão đánh cá hoạt hình râu bạc ngồi bên bờ kể chuyện cho cháu nhỏ, chỉ tay về phía chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái đang nhô lên vẫy vây; phía sau là tấm ảnh cũ đen trắng chụp cảnh y hệt; KHÔNG có anh MC trong cảnh này. |
| b11 | 01:15.9–01:27.5 (11.6s) | L293 | Nhưng các nhà khoa học cũng cảnh báo: cá đối đang ít dần, và số lần hợp tác cũng ít dần. Đây là một trong những mối hợp tác hiếm hoi còn sót lại giữa con người và động vật hoang dã. Nếu cá biến mất, tình bạn ấy cũng có thể biến mất theo. |  | Con kênh vắng vẻ hơn, chỉ còn một người đánh cá già và một chú chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái nhìn nhau buồn bã, mặt nước chỉ có vài con cá nhỏ; KHÔNG có anh MC trong cảnh này. |
| b12 | 01:27.5–01:34.1 (6.6s) | L294 | Nhưng Cá Heo còn một tuyệt chiêu đồng đội nữa: trí nhớ. Mỗi chú cá heo có một tiếng huýt sáo riêng, hoạt động giống như... một cái tên. |  | Ba chú chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái bơi cạnh nhau, trên đầu mỗi con là một bong bóng hình nốt nhạc khác nhau, mỗi nốt nhạc một màu riêng như chữ ký âm nhạc; KHÔNG có anh MC trong cảnh này. |
| b13 | 01:34.1–01:43.5 (9.4s) | L295 | Năm 2013, một nhà khoa học đã thu âm tiếng huýt sáo của 53 chú cá heo ở 6 thủy cung, rồi phát lại cho những chú cá heo từng sống chung với chúng... cách đây rất nhiều năm. | **53 CON** · được thử nghiệm · R/360 · [0.5, 0.6] | Một nhà khoa học hoạt hình cầm chiếc loa chống nước thả xuống bể, bên cạnh là chiếc máy ghi âm cổ có cuộn băng quay; chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái tò mò bơi lại gần; KHÔNG có anh MC trong cảnh này. |
| b14 | 01:43.5–01:51.8 (8.3s) | L296 | Có một chú cá heo cái tên Bailey, sống ở Bermuda. Khi được nghe lại tiếng huýt sáo của người bạn cũ Allie, chú lập tức bơi nhanh đến chiếc loa, lượn quanh, và huýt sáo gọi |  | chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái cái hào hứng bơi vòng quanh chiếc loa dưới nước, miệng phát ra những nốt nhạc nhỏ, ánh mắt vui mừng; trong bong bóng ký ức là hình ảnh hai chú cá heo con bơi cạnh nhau; KHÔNG có anh MC trong cảnh này. |
| b15 | 01:51.8–01:58.0 (6.2s) | L297 | lại. Hai bạn đã xa nhau 20 năm 6 tháng. Đó là trí nhớ xã hội dài nhất từng được ghi nhận ở một loài không phải con người. | **20 NĂM** · vẫn nhớ tên bạn · R/360 · [0.5, 0.45] | Một cuốn lịch hoạt hình lật nhanh từng trang bay tứ tung, ở cuối là hai chú chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái nhìn nhau qua khoảng cách xa, giữa hai con là sợi dây hình nốt nhạc nối liền; KHÔNG có anh MC trong cảnh này. |
| b16 | 01:58.0–02:00.8 (2.9s) | L298 | Giám khảo... xin phép lau nước mắt một chút. |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ rút khăn tay ra chấm nước mắt sau cặp kính tròn, mũi đỏ hoe, cây búa gỗ đặt sang một bên. |
| b17 | 02:00.8–02:10.1 (9.3s) | L299 | Tuyển thủ tiếp theo cũng sở hữu một đội hình huyền thoại: Rái Cá Biển. Khán giả đã biết rái cá nắm tay nhau ngủ thành "bè" để khỏi trôi. Nhưng một chiếc bè có thể lớn đến mức nào? |  | Một nhóm hàng chục chú chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách nằm ngửa cạnh nhau trên mặt biển giữa đám tảo bẹ, trông như một chiếc bè lông nâu khổng lồ trôi bồng bềnh; KHÔNG có anh MC trong cảnh này. |
| b18 | 02:10.1–02:18.5 (8.4s) | L300 | Thông thường mỗi bè có từ 10 đến 100 con. Nhưng ở Alaska từng ghi nhận những chiếc bè khổng lồ có tới hơn 2.000 con Rái Cá Biển nằm cạnh nhau! | **2.000** · rái cá một bè · R/360 · [0.5, 0.5] | Một cảnh nhìn từ trên cao hoạt hình: mặt biển phủ kín hàng ngàn chấm nâu nhỏ li ti là rái cá nằm ngửa, chiếc máy bay nhỏ bay ngang qua chụp ảnh; KHÔNG có anh MC trong cảnh này. |
| b19 | 02:18.5–02:26.5 (8.0s) | L301 | Và bè rái cá có luật lệ rõ ràng: rái cá đực nằm một bè riêng, rái cá cái và con nhỏ nằm một bè riêng. Một ký túc xá nam, một ký túc xá nữ, ngay giữa đại dương! |  | Hai chiếc bè rái cá trên mặt biển có tấm biển phao nổi đánh dấu: bè bên trái gồm toàn rái cá to xác có hình biểu tượng mặt trăng xanh, bè bên phải gồm rái cá mẹ ôm rái cá con có biểu tượng trái tim hồng; KHÔNG có anh MC trong cảnh này. |
| b20 | 02:26.5–02:34.9 (8.4s) | L302 | Tuyển thủ tiếp theo không phải là đội ở cùng nhau. Đó là cả một thành phố! Chim Cánh Cụt Adélie sống trong những đàn hàng chục ngàn, có khi hàng trăm ngàn cặp vợ chồng. |  | Toàn cảnh bãi đá Nam Cực hoạt hình chật kín hàng ngàn chú chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ nhỏ li ti đứng cạnh tổ sỏi, như một thành phố đông đúc nhìn từ trên cao; KHÔNG có anh MC trong cảnh này. |
| b21 | 02:34.9–02:45.6 (10.7s) | L303 | Ở mũi đất Crozier trên đảo Rốt, các nhà khoa học đếm được khoảng 150.000 cặp chim cánh cụt làm tổ cùng một chỗ. Ồn ào, đông đúc, và... chật chội như phố cổ giờ tan tầm! | **150.000** · cặp làm tổ · R/360 · [0.5, 0.55] | Cảnh đông nghịt hoạt hình: chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ chen chúc đi lạch bạch như dòng người giờ tan tầm, có chú đang đứng giữa đường chỉnh nơ, có chú đang cãi nhau vì giẫm chân; KHÔNG có anh MC trong cảnh này. |
| b22 | 02:45.6–02:55.2 (9.7s) | L304 | Trong một thành phố đông như thế, chim bố và chim mẹ vẫn tìm ra nhau, vẫn tìm ra con mình, chỉ bằng tiếng gọi. Mỗi cặp có một tiếng gọi riêng mà giữa hàng chục ngàn tiếng ồn ào, chúng vẫn nhận ra. |  | chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ vừa đi biển về, đứng giữa đám đông giơ mỏ cất tiếng gọi, từ xa một chú cánh cụt con lông xám quay đầu lại và chạy lạch bạch về phía bố, giữa hai con là dòng nốt nhạc nối liền; KHÔNG có anh MC trong cảnh này. |
| b23 | 02:55.2–03:03.1 (7.9s) | L305 | Và giờ, đến lượt những tuyển thủ thích... làm một mình. Chồn Gulo, Lửng Mật, Tôm Tít. Ba kẻ cô độc nổi tiếng nhất cuộc thi, đứng ở ba góc sân, không ai nhìn ai. |  | Ba góc sân thi đấu: chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh ở góc tuyết, chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần ở góc cát, chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọ |
| b24 | 03:03.1–03:10.6 (7.5s) | L306 | Nhưng giám khảo có một câu hỏi bất ngờ dành cho Tôm Tít: khi hai võ sĩ tôm tít tranh nhau một cái hang, chúng có đánh nhau đến chết không? |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ cúi người về phía bể nước, chỉ cây búa gỗ về phía chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh, chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và |
| b25 | 03:10.6–03:19.6 (9.0s) | L307 | Câu trả lời của khoa học: không. Các nhà nghiên cứu đã dàn dựng hơn 60 trận tranh hang giữa những chú tôm tít, và thấy chúng đánh nhau theo một nghi thức rất... lịch sự. |  | Hai chú chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh đứng đối diện nhau trước một cái hang đá, cả hai cúi chào nhau như hai võ sĩ trước trận đấu, một trọng tài hoạt hình nhỏ đứng giữa; KHÔNG có anh MC trong cảnh này. |
| b26 | 03:19.6–03:25.6 (6.0s) | L308 | Đầu tiên, dang càng ra dọa nhau! Không ăn thua thì vẫy râu đánh hơi đối thủ! Vẫn không ăn thua, thì mới chuyển sang... đấm! |  | Chuỗi ba hình nhỏ hoạt hình nối nhau: hai chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh dang càng như võ sĩ khoe cơ, rồi vẫy râu ngửi nhau, rồi tung cú đấm; KHÔNG có anh MC trong cảnh này. |
| b27 | 03:25.6–03:34.1 (8.5s) | L309 | Nhưng không phải đấm vào mặt. Mà là đấm vào tấm khiên ở đuôi! Con bị đánh cuộn đuôi lại, giơ tấm khiên dày cứng ra đỡ, hai bên thay nhau đấm vào khiên, như hai võ sĩ đấm vào găng của nhau. |  | Một chú chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh cuộn đuôi lên trước ngực thành tấm khiên tròn cứng có hoa văn, chú kia đấm cú vào tấm khiên tạo tiếng "bốp" hoạt hình, không ai bị thương; KHÔNG có anh MC trong cảnh này. |
| b28 | 03:34.1–03:41.3 (7.1s) | L310 | Và mục đích của màn đấm khiên này là để... đo sức nhau. Sau vài cú, con nào nhẹ cân hơn tự hiểu là mình yếu hơn, và lặng lẽ rút lui. Không ai phải |  | Chú chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh nhỏ hơn thở hổn hển, giơ một càng lên như cờ trắng đầu hàng rồi bơi đi, chú to hơn bước vào hang; hai bên vẫn gật đầu chào nhau lịch sự; KHÔNG có anh MC trong cảnh này. |
| b29 | 03:41.3–03:47.3 (6.1s) | L311 | chết. Một võ sĩ có cú đấm mạnh nhất đại dương, nhưng lại biết dùng nó để nói chuyện thay vì để giết nhau. Đúng là võ sĩ có võ đức! |  | chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh đeo đai đen võ thuật hoạt hình, cúi đầu chào khán giả theo kiểu võ đường, trên tường có tấm biển hình nắm đấm và trái tim; KHÔNG có anh MC trong cảnh này. |
| b30 | 03:47.3–03:55.9 (8.6s) | L312 | Còn Lửng Mật? Lửng Mật vẫn đi một mình... nhưng như vòng hai đã kể, phía sau nó luôn có 6 con chim ưng bám theo. Giám khảo hỏi: như vậy có tính là đồng đội không? |  | chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần đứng khoanh tay, phía sau sáu con chim ưng xám đứng thành hàng như dàn đồng ca; bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ nhìn qua kính với vẻ suy tư, tay gõ gõ bút vào cằm. |
| b31 | 03:55.9–04:02.5 (6.6s) | L313 | Giám khảo xin trả lời: không. Có người đi theo mình, nhưng mình không quan tâm tới họ, thì không phải là đồng đội. |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ lắc đầu, gõ búa, giơ tấm thẻ có biểu tượng hai bàn tay nắm nhau bị gạch chéo về phía chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần. |
| b32 | 04:02.5–04:09.7 (7.2s) | L314 | Vừa giành huy chương vàng ở vòng nuôi con, Lửng Mật lại trắng tay ở vòng này. Giỏi chăm con mình, nhưng làm việc với người ngoài thì... chưa biết cách! |  | chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần đứng trước bảng điểm, mặt đỏ gay, khói bốc lên từ tai, chân đá một viên sỏi nhỏ, lửng con ngồi trên đầu mẹ vỗ vai an ủi; xa xa chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng  |
| b33 | 04:09.7–04:14.8 (5.0s) | L315 | Kết quả vòng sáu! Huy chương đồng: Rái Cá Biển, với những chiếc bè 2.000 thành viên! |  | Bục trao giải: chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách nằm ngửa trên bậc đồng đeo thêm một huy chương đồng, tay nắm tay một chú rái cá khác; KHÔNG có anh MC trong cảnh này. |
| b34 | 04:14.8–04:19.6 (4.9s) | L316 | Huy chương bạc: Tôm Tít, võ sĩ biết dùng nắm đấm để... thương lượng hòa bình! Và huy chương vàng... |  | chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh ở bậc bạc trong bể nước nhỏ đeo huy chương bạc, giơ càng ăn mừng; bậc vàng phía trên đang phủ một tấm màn che bí ẩn; KHÔNG có anh MC trong cảnh này. |
| b35 | 04:19.6–04:27.3 (7.6s) | L317 | Thuộc về Cá Heo, huy chương vàng thứ hai! Đồng đội của cả con người suốt hơn 100 năm, và là người bạn nhớ tên bạn mình sau 20 năm xa cách! |  | chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái nhảy vọt lên khỏi bể nước trên bậc vàng, đeo hai huy chương vàng, xung quanh là những người đánh cá Bra-xin hoạt hình vỗ tay hoan hô; KHÔNG có anh MC trong cảnh này. |
| b36 | 04:27.3–04:38.6 (11.4s) | L318 | Bảng điểm sau sáu vòng: Thú Mỏ Vịt 8 điểm! Cá Heo bám sát với 7 điểm! Chồn Gulo, Chim Cánh Cụt và Rái Cá cùng 4 điểm. Lửng Mật và Tôm Tít 3 điểm. Bồ Nông 2 điểm, Koala 1 điểm. Gấu Nước: vẫn chưa có điểm! |  | tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) sáng lên: cột chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá cao nhất, cột chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái sát nút ngay bên cạnh, ba |
| b37 | 04:38.6–04:47.1 (8.5s) | L319 | Nhưng vòng bảy sẽ đảo lộn tất cả. Vì vòng bảy sẽ không chấm năng lực. Vòng bảy là phiên phúc khảo: những tin đồn nổi tiếng nhất về các tuyển thủ sẽ được mang ra kiểm |  | Một căn phòng tối hoạt hình, giữa phòng là chiếc bàn có chồng hồ sơ dày, trên cùng là chiếc kính lúp khổng lồ, ánh đèn bàn rọi xuống; KHÔNG có anh MC trong cảnh này. |
| b38 | 04:47.1–04:52.5 (5.4s) | L320 | chứng. Và có những tuyển thủ sắp phát hiện ra rằng... danh tiếng của mình được xây trên một câu chuyện không có thật. |  | Bóng đen của mười tuyển thủ in trên tường, một vài cái bóng đổ mồ hôi lo lắng, có cái bóng đang lén lút giấu một cuốn truyện tranh sau lưng; KHÔNG có anh MC trong cảnh này. |

### scene10 · PHÓNG VIÊN HỎI KHÓ — TUYỂN THỦ TRẢ LỜI BẰNG SỰ THẬT · 180.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.6 (7.6s) | L321 | Trước vòng bảy, ban tổ chức mở một buổi họp báo. Phóng viên được hỏi bất cứ điều gì. Và các tuyển thủ phải trả lời... bằng sự thật khoa học! |  | Một phòng họp báo hoạt hình có bàn dài phủ khăn xanh, mười chiếc micro nhỏ xếp hàng, phía dưới là hàng ghế phóng viên giơ tay, đèn flash nháy liên tục; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đứng ở bục điều phối. |
| b02 | 00:07.6–00:15.0 (7.4s) | L322 | Câu hỏi đầu tiên dành cho Tôm Tít: ở dưới đáy biển sâu, ánh sáng gần như chỉ còn màu xanh lam. Vậy những đốm màu trên người anh có còn ai nhìn thấy không? |  | Một cô phóng viên hoạt hình đứng dậy cầm micro hỏi, sổ tay trên tay, phía trước là chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh ngồi sau bàn họp báo nhướng mắt lắng nghe; KHÔNG có anh MC trong cảnh này. |
| b03 | 00:15.0–00:26.3 (11.3s) | L323 | Câu trả lời đến từ một lần lặn đêm năm 2002 ở vùng biển Bahamas. Một thợ lặn chiếu đèn xanh xuống một chú tôm tít đang thò đầu khỏi hang, và thấy hai đốm trên người nó... sáng rực lên màu vàng, như hai chiếc đèn pha. |  | Dưới đáy biển tối đêm hoạt hình, chùm đèn xanh của thợ lặn chiếu vào một chú tôm tít thò đầu khỏi hang cát, hai đốm vàng trên người phát sáng rực rỡ như đèn pha; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:26.3–00:37.2 (10.9s) | L324 | Các nhà khoa học giải thích: ở độ sâu khoảng 40 mét, màu vàng gần như biến mất trong làn nước xanh. Nhưng những đốm này có chất phát quang, hấp thụ ánh sáng xanh rồi phát ra ánh sáng vàng. Nhờ vậy, tín hiệu vẫn rõ ràng ở dưới sâu. | **40 M** · đốm vẫn sáng · R/360 · [0.5, 0.6] | Sơ đồ hoạt hình hai chú tôm tít ở hai độ sâu: chú ở nước nông có đốm vàng bình thường, chú ở nước sâu xanh thẫm có đốm vàng vẫn sáng nhờ những mũi tên ánh sáng xanh đi vào và ánh sáng vàng đi ra; KHÔNG có anh MC trong cảnh này. |
| b05 | 00:37.2–00:49.0 (11.8s) | L325 | Và những đốm sáng ấy được dùng trong màn dọa nạt đối thủ. Tôm Tít dang càng, khoe đốm vàng phát sáng như muốn nói: "Đây là nhà của tôi, tránh ra!". Đây là trường hợp đầu tiên được ghi nhận về việc một sinh vật biển dùng ánh sáng phát quang để ra tín hiệu. |  | chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh dang hai càng trước cửa hang, hai đốm vàng trên người sáng rực như biển báo, một chú tôm tít khác đang lùi lại sợ hãi; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:49.0–00:55.6 (6.6s) | L326 | Tôm Tít trả lời xong, dang càng khoe đốm sáng ngay giữa phòng họp báo. Các phóng viên phải... đeo kính râm! |  | Cả hàng ghế phóng viên hoạt hình đồng loạt đeo kính râm, chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh trên bàn họp báo phát sáng hai đốm vàng chói lóa, anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng giơ tay che mắt. |
| b07 | 00:55.6–01:03.0 (7.4s) | L327 | Câu hỏi thứ hai dành cho Chim Bồ Nông: người ta đồn có một loài bồ nông lao đầu từ trên cao xuống biển để bắt cá. Lao mạnh như vậy, anh không đau đầu sao? |  | Một anh phóng viên hoạt hình đeo kính cận đứng dậy hỏi, cầm máy ghi âm chĩa về phía chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn; KHÔNG có anh MC trong cảnh này. |
| b08 | 01:03.0–01:13.6 (10.6s) | L328 | Đó là anh họ của Bồ Nông, loài bồ nông nâu ở châu Mỹ, loài bồ nông duy nhất săn mồi bằng cú bổ nhào ngoạn mục. Từ độ cao có khi tới hơn 20 mét, nó gập cánh và lao thẳng xuống biển như một mũi tên. | **> 20 M** · độ cao bổ nhào · R/360 · [0.5, 0.35] | Một chú bồ nông nâu hoạt hình gập cánh lao thẳng từ trên trời xuống mặt biển như mũi tên, phía dưới là đàn cá nhỏ lấp lánh, nước bắn tung tóe; chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn đứng trên bờ chỉ tay giới thiệu; KHÔNG có anh MC trong cảnh này. |
| b09 | 01:13.6–01:21.1 (7.5s) | L329 | Bí mật nằm ở những túi khí dưới da. Khi đập xuống mặt nước, các túi khí này đệm lại cú va chạm như túi khí ô tô, rồi giúp nó nổi bật trở lên như một cái nút chai. |  | Hình mặt cắt hoạt hình cơ thể bồ nông nâu có những túi khí nhỏ màu xanh nhạt phồng lên dưới da như những quả bóng, bên cạnh là hình túi khí ô tô bung ra để so sánh; KHÔNG có anh MC trong cảnh này. |
| b10 | 01:21.1–01:26.9 (5.8s) | L330 | Câu hỏi thứ ba dành cho Lửng Mật: ở Nam Phi, người ta còn gọi anh bằng một cái tên khác. Anh có biết đó là tên gì không? |  | Cô phóng viên đứng dậy lần nữa, giơ một tấm thẻ có hình dấu chấm hỏi, chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần ngồi khoanh tay sau bàn họp báo nhướng mày; KHÔNG có anh MC trong cảnh này. |
| b11 | 01:26.9–01:37.6 (10.7s) | L331 | Đó là tên "Ratel". Những người định cư Hà Lan ở Nam Phi đặt tên này theo tiếng gầm gừ lục cục rất đặc trưng mà Lửng Mật phát ra mỗi khi nổi giận. Nghe như tiếng... ai đó đang lắc một hộp sỏi! |  | chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần gầm gừ, từ miệng bay ra những hình nốt nhạc gai góc hình viên sỏi, bên cạnh vẽ một chiếc hộp thiếc đầy sỏi đang được lắc mạnh; KHÔNG có anh MC trong cảnh này. |
| b12 | 01:37.6–01:44.5 (6.9s) | L332 | Còn ở Uganda, người Ganda gọi nó bằng một cái tên có nghĩa là "kẻ không nghe thấy", vì đôi tai của Lửng Mật rất nhỏ, gần như không nhìn thấy. |  | Cận cảnh đầu chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần hoạt hình với đôi tai nhỏ xíu gần như lẫn vào lớp lông, một chú chim nhỏ cầm loa thét vào tai nó mà chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần vẫn thản nhiên; KHÔNG |
| b13 | 01:44.5–01:50.1 (5.6s) | L333 | "Kẻ không nghe thấy"... Có lẽ đó là lý do vì sao Lửng Mật chưa bao giờ nghe lời ai can ngăn! |  | chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần đi thẳng qua tấm biển báo cấm có hình bàn tay đỏ, các con vật khác phía sau giơ tay ra can ngăn hoảng hốt, còn nó vẫn tỉnh bơ bước tiếp; KHÔNG có anh MC trong cảnh này. |
| b14 | 01:50.1–01:53.8 (3.8s) | L334 | Câu hỏi thứ tư dành cho Chồn Gulo: tên khoa học của anh có nghĩa là gì? |  | Anh phóng viên đeo kính cận đứng dậy, cầm cuốn từ điển La-tinh dày cộp, chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh ngồi sau bàn họp báo đang gặm một khúc xương; KHÔNG có anh MC trong cảnh này. |
| b15 | 01:53.8–01:58.0 (4.2s) | L335 | Tên khoa học của Chồn Gulo bắt nguồn từ một chữ La-tinh có nghĩa là... "kẻ tham ăn". |  | Cận cảnh chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh hoạt hình khựng lại giữa lúc gặm khúc xương, quay mặt nhìn vào ống kính với vẻ mặt bị bắt quả tang; KHÔNG có anh MC trong cảnh này. |
| b16 | 01:58.0–02:06.1 (8.1s) | L336 | Và cả phòng họp báo nhìn xuống khúc xương trên tay Chồn Gulo... Chồn Gulo lặng lẽ giấu khúc xương ra sau lưng. Không có gì để bàn thêm! |  | chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh giấu khúc xương ra sau lưng, huýt sáo nhìn lên trần nhà, cả phòng phóng viên cười ồ, đèn flash nháy liên tục; KHÔNG có anh MC trong cảnh này. |
| b17 | 02:06.1–02:14.5 (8.4s) | L337 | Nhưng các nhà khoa học cho rằng cái tên ấy có phần oan. Sống ở nơi lạnh giá, thức ăn khan hiếm, việc ăn được mọi thứ tìm thấy là một chiến lược sinh tồn chứ không phải tính xấu. |  | chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh đứng giữa vùng tuyết trắng mênh mông chỉ có vài dấu chân thưa thớt, trên tay là một miếng thịt nhỏ, ánh mắt cảnh giác nhìn quanh; KHÔNG có anh MC trong cảnh này. |
| b18 | 02:14.5–02:21.1 (6.6s) | L338 | Câu hỏi cuối cùng dành cho Koala: có người nói túi của Koala mẹ mở ngược xuống dưới. Như vậy Koala con không bị rơi ra ngoài sao? |  | Cô phóng viên đứng dậy hỏi, vẻ mặt lo lắng thật sự, chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ ngồi sau bàn họp báo đang lim dim ngủ thì giật mình mở mắt; KHÔNG có anh MC trong cảnh này. |
| b19 | 02:21.1–02:30.5 (9.5s) | L339 | Đây là một hiểu lầm rất phổ biến. Theo Quỹ Koala Úc, khi mới sinh con, túi của Koala mẹ không mở ngược lên cũng không mở ngược xuống, mà mở thẳng ra phía trước, ở giữa bụng. |  | Sơ đồ hoạt hình bụng của chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ mẹ nhìn nghiêng, miệng túi nằm giữa bụng hướng ra phía trước, bên trong có chú Cô-a-la con bé xíu bám vào; một mũi tên chỉ ra phía trước; KHÔNG có anh MC trong cảnh này. |
| b20 | 02:30.5–02:40.3 (9.8s) | L340 | Miệng túi có một cơ vòng rất khỏe mà mẹ có thể thắt chặt lại, giữ cho con không rơi ra ngoài. Chỉ khi con đã lớn và thò người ra ngoài, sức nặng của con mới kéo miệng túi trễ xuống, trông như túi... mở ngược. |  | Chú Cô-a-la con lớn hơn thò nửa người ra khỏi túi, kéo miệng túi trễ xuống, chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ mẹ vẫn ôm cây bình thản; bên cạnh vẽ một chiếc túi có dây rút được thắt chặt để minh họa cơ vòng; KHÔNG có anh MC trong cảnh này. |
| b21 | 02:40.3–02:45.8 (5.5s) | L341 | Hồi nhỏ cháu toàn thò đầu ra ngắm cây đó ạ! Mẹ cháu bảo... đừng có thò ra nhiều quá, nặng lắm! |  | chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ cười tươi giơ tay khoe, trong bong bóng ký ức là hình chú Cô-a-la con thò đầu ra khỏi túi mẹ ngắm cành lá, mẹ nhăn mặt vì nặng; KHÔNG có anh MC trong cảnh này. |
| b22 | 02:45.8–02:51.4 (5.6s) | L342 | Xin cảm ơn các tuyển thủ. Và nhắn riêng tuyển thủ Chồn Gulo: phòng họp báo không cho phép mang xương vào nhé! |  | Cô phóng viên mỉm cười cúi chào, phía sau chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh đang lén nhặt lại khúc xương dưới gầm bàn, giả vờ như không có chuyện gì; KHÔNG có anh MC trong cảnh này. |
| b23 | 02:51.4–03:00.4 (9.0s) | L343 | Buổi họp báo kết thúc! Năm câu hỏi, năm câu trả lời, và không ai phải... nói dối! Và giờ, đúng như tên gọi, chúng ta bước sang vòng thi về sự thật: phiên phúc khảo tin đồn! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đóng cuốn sổ ghi chép, các phóng viên đứng dậy vỗ tay, các tuyển thủ rời bàn họp báo đi về phía một cánh cửa gỗ lớn có hình chiếc kính lúp. |

### scene11 · PHÚC KHẢO TIN ĐỒN — HUYỀN THOẠI NÀO ĐÚNG, HUYỀN THOẠI NÀO SAI · 277.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:10.3 (10.3s) | L344 | Vòng bảy: phúc khảo tin đồn. Luật chơi: giám khảo đọc một tin đồn nổi tiếng về tuyển thủ. Khoa học sẽ xác nhận hoặc bác bỏ. Tin đồn đúng: tuyển thủ được điểm. Tin đồn sai mà tuyển thủ dám thừa nhận: cũng được điểm! |  | Phòng phúc khảo hoạt hình như phòng xử án nhỏ: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ ngồi giữa sau bàn cao, trước mặt là chiếc cân công lý, một bên đĩa cân là cuốn sách khoa học, bên kia là cuốn truyện tranh; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đứng một bên cầm micro. |
| b02 | 00:10.3–00:22.8 (12.5s) | L345 | Hồ sơ phúc khảo số một, và lần này kênh Vẽ Chuyện Hoang Dã tự phúc khảo chính mình! Trong tập phim về Tôm Tít, chúng tôi kể mắt nó có tới 16 loại tế bào cảm thụ ánh sáng. Và tin đồn đi kèm là: "Tôm Tít nhìn màu sắc rực rỡ hơn con người gấp nhiều lần". |  | Một tấm áp phích mạng xã hội hoạt hình phóng to đôi mắt chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh, bên trong là cầu vồng rực rỡ nhiều màu hơn hẳn, bên cạnh là đôi mắt người chỉ có ba màu đỏ xanh lá xanh dương; KHÔNG có anh MC trong cảnh này. |
| b03 | 00:22.8–00:36.4 (13.6s) | L346 | Con số 16 là đúng, và trong đó có 12 loại chuyên cảm nhận màu, trong khi mắt người chỉ có ba. Nhưng năm 2014, các nhà khoa học ở Úc làm một thí nghiệm đơn giản: dạy tôm tít nhận một màu để được thưởng đồ ăn, rồi cho chọn giữa hai màu gần giống nhau. | **2014** · thí nghiệm màu · L/360 · [0.5, 0.45] | Một bể thí nghiệm hoạt hình có hai sợi đèn màu, một vàng một cam rất gần nhau, chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh đứng giữa nhìn qua lại bối rối, một nhà khoa học cầm miếng tôm thưởng chờ bên cạnh; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:36.4–00:44.6 (8.2s) | L347 | Kết quả bất ngờ: khi hai màu khác nhau ít, kiểu như vàng với cam, Tôm Tít bắt đầu chọn sai. Có lúc chọn đúng không hơn gì... đoán bừa! |  | chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh nhắm mắt chỉ càng bừa vào một sợi đèn, trên đầu là đồng xu đang tung lên quay quay, nhà khoa học vỗ trán; KHÔNG có anh MC trong cảnh này. |
| b05 | 00:44.6–00:52.5 (7.9s) | L348 | Hóa ra 12 loại tế bào ấy không phối hợp để phân biệt sắc độ như mắt người. Mỗi loại làm việc riêng, giống như 12 ngăn kéo phân loại màu: nhanh, nhưng |  | Hình minh họa hoạt hình: mắt chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh như một chiếc tủ có mười hai ngăn kéo nhiều màu, mỗi ngăn bắt một màu rơi vào; bên cạnh là não người như một họa sĩ đang pha trộn màu tinh tế trên bảng màu; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:52.5–00:60.0 (7.4s) | L349 | không tinh. Các nhà khoa học cho rằng cách nhìn này giúp Tôm Tít nhận ra màu cực nhanh mà không cần não xử lý nhiều, rất hợp với cuộc sống chớp nhoáng dưới đáy biển. |  | chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh quét mắt qua một rạn san hô, những đốm màu được đánh dấu tức thì như đèn đỏ đèn xanh, một con cá nhỏ vừa ló ra đã bị phát hiện; KHÔNG có anh MC trong cảnh này. |
| b07 | 00:60.0–01:07.7 (7.7s) | L350 | Phán quyết: tin đồn "nhìn màu đẹp hơn người" là sai. Nhưng Tôm Tít có một cách nhìn màu độc nhất vô nhị. Tuyển thủ có chấp nhận không? |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gõ búa, giơ tấm thẻ có biểu tượng con mắt kèm dấu chấm hỏi. |
| b08 | 01:07.7–01:14.4 (6.7s) | L351 | Tôm Tít gật đầu. Nó không cần nhìn màu đẹp hơn người. Nó chỉ cần nhìn thấy con mồi nhanh hơn con mồi kịp chạy! |  | chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh khoanh hai càng gật đầu đầy tự tin, đeo chiếc kính râm hình mắt kép nhiều ngăn màu sắc; KHÔNG có anh MC trong cảnh này. |
| b09 | 01:14.4–01:21.2 (6.8s) | L352 | Hồ sơ phúc khảo số hai: Lửng Mật và chim dẫn mật. Như các bạn đã nghe ở vòng ba, khoa học hiện nay nói rằng: chưa có bằng chứng rõ ràng. |  | Hồ sơ màu đỏ có ảnh chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần và một chú chim nhỏ màu nâu được đặt lên bàn, có dấu đóng hình chiếc kính lúp và dấu chấm hỏi; KHÔNG có anh MC trong cảnh này. |
| b10 | 01:21.2–01:26.4 (5.1s) | L353 | Giám khảo hỏi Lửng Mật: tuyển thủ có thừa nhận câu chuyện chim dẫn đường là chưa được chứng minh không? |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ cúi người nhìn thẳng vào chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần qua cặp kính tròn, cả căn phòng im phăng phắc, một giọt mồ hôi chảy trên trán anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng. |
| b11 | 01:26.4–01:34.7 (8.3s) | L354 | Lửng Mật im lặng một lúc lâu... rồi gật đầu. Gã giang hồ nổi tiếng không bao giờ lùi bước, lần đầu tiên chịu nhận là: ừ, chuyện đó chưa ai chứng minh được! |  | chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần quay mặt đi, bĩu môi, nhưng vẫn gật đầu miễn cưỡng, một tay giơ lên như đầu hàng; khán đài sửng sốt há hốc mồm; KHÔNG có anh MC trong cảnh này. |
| b12 | 01:34.7–01:41.6 (6.9s) | L355 | Phán quyết: tin đồn chưa được chứng minh. Nhưng tuyển thủ dám thừa nhận. Giám khảo ghi nhận tinh thần... trung thực! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ mỉm cười gõ búa nhẹ, đặt một ngôi sao vàng nhỏ cạnh hình đầu chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần trên bàn. |
| b13 | 01:41.6–01:51.9 (10.4s) | L356 | Hồ sơ phúc khảo số ba: Gấu Nước. Tin đồn: "Năm 2019, tàu vũ trụ Beresheet của Israel rơi xuống Mặt Trăng, và hàng ngàn con Gấu Nước trên tàu hiện vẫn đang nằm ngủ trên Mặt Trăng, chờ ngày được hồi sinh". |  | Mặt Trăng hoạt hình xám bạc có miệng núi lửa, giữa một miệng núi lửa là xác con tàu vũ trụ nhỏ vỡ nát, những chấm nhỏ li ti rải rác xung quanh; Trái Đất xanh lơ lửng phía xa; KHÔNG có anh MC trong cảnh này. |
| b14 | 01:51.9–02:03.5 (11.6s) | L357 | Khán giả của kênh còn nhớ: gấu nước từng bị bắn ra khỏi nòng súng cao tốc mà vẫn sống. Nhưng chính thí nghiệm ấy còn một phần hai ít ai kể. Năm 2020 mốt, các nhà khoa học Anh tăng tốc độ bắn để tìm ra... giới hạn cuối cùng. |  | Một khẩu pháo khí dài hoạt hình trong phòng thí nghiệm, hai nhà khoa học đeo kính bảo hộ đứng cạnh, trên bàn là chiếc đạn nhựa nhỏ có chú chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương đang ngủ bên trong; KHÔNG có anh MC trong cảnh này. |
| b15 | 02:03.5–02:09.9 (6.4s) | L358 | Họ cho Gấu Nước ngủ đông, nhét vào viên đạn nhựa, rồi bắn vào bao cát, mỗi lần một nhanh hơn! 500 mét mỗi giây! 700! 800! |  | Viên đạn nhựa hoạt hình bay vèo qua những vòng đo tốc độ phát sáng, đâm vào bao cát tung bụi, chiếc đồng hồ đo tốc độ chạy vọt lên; KHÔNG có anh MC trong cảnh này. |
| b16 | 02:09.9–02:20.1 (10.1s) | L359 | 900! Kết quả: đến khoảng 825m mỗi giây, Gấu Nước vẫn sống. Nhưng chỉ nhích lên khoảng 900 mét mỗi giây, các nhà khoa học chỉ còn tìm thấy... những mảnh vụn. Siêu nhân cũng có giới hạn. | **825 M/S** · giới hạn sống sót · R/360 · [0.45, 0.55] | chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương bò ra khỏi bao cát, phủi bụi, choáng váng nhưng vẫn vẫy tay chào; bên cạnh là biển báo tốc độ có vạch giới hạn màu đỏ; KHÔNG có anh MC trong cảnh này. |
| b17 | 02:20.1–02:30.1 (10.1s) | L360 | Và cú va chạm khi tàu Beresheet rơi xuống Mặt Trăng tạo ra áp lực mạnh hơn rất nhiều so với giới hạn ấy. Kết luận của nhóm nghiên cứu: những chú Gấu Nước trên tàu gần như chắc chắn đã không sống sót. |  | Trên mặt Trăng xám bạc, một chiếc mũ phi hành gia tí hon nằm lặng lẽ giữa đống đổ nát của con tàu, một bông hoa nhỏ hoạt hình đặt bên cạnh; KHÔNG có anh MC trong cảnh này. |
| b18 | 02:30.1–02:34.9 (4.8s) | L361 | Phán quyết: tin đồn Gấu Nước đang ngủ trên Mặt Trăng... khả năng rất cao là sai. |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ cởi kính ra, khẽ cúi đầu, gõ búa thật nhẹ, ánh đèn trong phòng dịu xuống. |
| b19 | 02:34.9–02:45.3 (10.4s) | L362 | Nhưng khoan, Gấu Nước tỉnh dậy từ tủ đông và giơ tay xin phát biểu: "Tôi không bất tử. Tôi chỉ... rất, rất cứng". Và giám khảo đánh giá cao: dám nhận giới hạn của mình, đó cũng là một kiểu sức mạnh! |  | chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương đứng trên bục phát biểu tí hon, giơ một chân lên xin nói, sau lưng là biểu đồ tốc độ có mũi tên vượt qua hình chiếc máy bay phản lực; KHÔNG có anh MC trong cảnh này. |
| b20 | 02:45.3–02:54.3 (9.0s) | L363 | Hồ sơ phúc khảo số bốn: Chim Bồ Nông. Tin đồn này đã có từ hơn 1.000 năm trước. Người xưa tin rằng: khi không còn thức ăn, Bồ Nông mẹ sẽ tự mổ ngực mình, lấy máu nuôi con. |  | Một bức tranh kính màu nhà thờ cổ hoạt hình vẽ con bồ nông đứng trên tổ, cúi đầu mổ vào ngực, bên dưới là ba chú chim non há mỏ; ánh sáng chiếu xuyên qua kính màu; KHÔNG có anh MC trong cảnh này. |
| b21 | 02:54.3–03:00.2 (5.9s) | L364 | Hình ảnh này nổi tiếng đến mức xuất hiện trên huy hiệu, trên cửa kính nhà thờ, trên biểu tượng của nhiều trường đại học ở châu Âu. |  | Một bức tường hoạt hình treo nhiều tấm khiên huy hiệu cổ khác nhau, tấm nào cũng có hình con bồ nông mổ ngực cho con ăn (không chữ); KHÔNG có anh MC trong cảnh này. |
| b22 | 03:00.2–03:08.0 (7.7s) | L365 | Khoa học trả lời: không có chuyện đó. Khi cho con ăn, Bồ Nông mẹ ép cái túi họng vào ngực để đẩy cá đã nuốt ra cho con. Nhìn từ xa, trông như nó đang mổ vào ngực mình. |  | Cảnh thật hoạt hình: chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn mẹ cúi mỏ xuống ép túi họng vào ngực, mở mỏ cho chú bồ nông con chui đầu vào bên trong túi họng lấy cá; KHÔNG có anh MC trong cảnh này. |
| b23 | 03:08.0–03:16.3 (8.3s) | L366 | Thêm nữa, đầu mỏ của một số loài bồ nông có màu đỏ, và có loài túi họng chuyển sang đỏ thẫm vào mùa sinh sản. Người xưa nhìn thấy màu đỏ ở ngực... thế là thêu dệt thành chuyện máu! |  | Cận cảnh mỏ chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn có chóp mỏ đỏ và túi họng đỏ hồng, một người xưa hoạt hình đội mũ trùm đầu nhìn qua bụi rậm, mắt mở to kinh hãi, tưởng tượng ra cảnh máu trong bong bóng suy nghĩ; KHÔNG có anh MC trong cảnh này. |
| b24 | 03:16.3–03:25.1 (8.8s) | L367 | Phán quyết: tin đồn sai. Nhưng giám khảo ghi nhận: Bồ Nông là loài chim có biểu tượng tình mẫu tử... dễ thương nhất lịch sử, dù là nhờ hiểu lầm! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gõ búa rồi mỉm cười, giơ tấm thẻ có hình trái tim nhỏ. |
| b25 | 03:25.1–03:33.5 (8.4s) | L368 | Hồ sơ phúc khảo số năm, và là hồ sơ cuối cùng: Gấu Koala. Tin đồn: "Koala chỉ lấy nước từ lá, ngoài những ngày nắng nóng khắc nghiệt thì gần như không bao giờ uống". |  | Một cuốn sách cổ hoạt hình mở ra trang có hình chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ ôm chiếc lá to, bên cạnh là ly nước bị gạch chéo và chiếc lông vũ chấm mực; KHÔNG có anh MC trong cảnh này. |
| b26 | 03:33.5–03:44.7 (11.2s) | L369 | Vòng một đã trả lời rồi! Năm 2020, khoa học đã ghi nhận 46 lần Koala hoang dã liếm nước mưa từ thân cây, kể cả những ngày trời không hề nóng. Koala uống thường xuyên hơn chúng ta tưởng! |  | chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ ôm thân cây thè lưỡi liếm nước mưa chảy dọc thân, mắt nhắm tận hưởng, xung quanh có những giọt mưa lấp lánh; KHÔNG có anh MC trong cảnh này. |
| b27 | 03:44.7–03:48.6 (3.9s) | L370 | Cháu có uống mà! Có điều... cháu chỉ uống khi trời mưa thôi ạ. |  | chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ giơ tay phát biểu, đội chiếc mũ len nhỏ có quả bông, ánh mắt ngây thơ thành thật; KHÔNG có anh MC trong cảnh này. |
| b28 | 03:48.6–03:55.3 (6.7s) | L371 | Phán quyết: tin đồn "gần như không bao giờ uống" là chưa đúng. Và Koala chính là tuyển thủ giúp khoa học sửa lại một hiểu lầm trăm năm! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gõ búa dứt khoát, rồi gạch chéo một dòng trong cuốn sách cổ bằng bút đỏ, đặt ngôi sao vàng cạnh hình đầu chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ. |
| b29 | 03:55.3–04:02.2 (6.9s) | L372 | Kết quả vòng bảy, và đây là vòng có kết quả bất ngờ nhất đêm nay! Huy chương đồng: Gấu Nước, sinh vật siêu cứng dám thừa nhận mình không bất |  | Bục trao giải: chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương tí hon đứng trên bậc đồng, phải đứng trên một chiếc ghế nhỏ mới với tới huy chương đồng, cười rạng rỡ; KHÔNG có anh MC trong cảnh này. |
| b30 | 04:02.2–04:05.9 (3.7s) | L373 | tử! Huy chương bạc: Koala, người giúp khoa học sửa sai! |  | chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ đứng trên bậc bạc ôm huy chương bạc vào lòng như ôm gối, mặt vừa ngơ ngác vừa vui; KHÔNG có anh MC trong cảnh này. |
| b31 | 04:05.9–04:14.2 (8.3s) | L374 | Và huy chương vàng vòng bảy thuộc về... Lửng Mật, huy chương vàng thứ hai! Vì lần đầu tiên trong lịch sử, gã giang hồ chịu nhận mình... chưa chắc đúng! |  | chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần đứng trên bậc vàng, đeo hai huy chương vàng, mặt vừa ngượng vừa sung sướng, khán đài vỡ òa vỗ tay, sáu con chim ưng xám tung pháo giấy từ trên trời; KHÔNG có anh MC trong cảnh này. |
| b32 | 04:14.2–04:25.2 (11.0s) | L375 | Bảng điểm sau bảy vòng: Thú Mỏ Vịt 8 điểm! Cá Heo 7 điểm! Lửng Mật bứt lên mạnh mẽ với 6 điểm! Chồn Gulo, Chim Cánh Cụt, Rái Cá 4 điểm. Tôm Tít và Koala 3 điểm. Bồ Nông 2 điểm, Gấu Nước 1 điểm. |  | tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) sáng lên: ba cột chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá, chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái, chú Lửng Mật hoạt hình thân đen, l |
| b33 | 04:25.2–04:32.8 (7.7s) | L376 | Ba tuyển thủ dẫn đầu chỉ cách nhau đúng 2 điểm! Chỉ còn một vòng cuối. Và vòng cuối có điểm nhân đôi: vàng 6 điểm, bạc 4 điểm, đồng 2 điểm. |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ lật một tấm bảng mới, trên đó ba chiếc huy chương vàng bạc đồng đều có biểu tượng nhân đôi phát sáng; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng hít một hơi thật sâu. |
| b34 | 04:32.8–04:37.4 (4.6s) | L377 | Câu hỏi của vòng chung kết không phải là ai mạnh nhất. Mà là: ai đã giúp ích cho loài người nhiều nhất. |  | Một chiếc bàn tròn hoạt hình giữa sân khấu, trên bàn đặt một quả địa cầu nhỏ và một trái tim đỏ phát sáng, mười cái bóng tuyển thủ đứng vây quanh; KHÔNG có anh MC trong cảnh này. |

### scene12 · THỌ NHẤT, LẶN CHĂM NHẤT, ĂN KHỎE NHẤT, HỒI SINH NGOẠN MỤC NHẤT · 310.8s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.8 (9.8s) | L378 | Trước khi bước vào vòng chung kết, ban tổ chức có một bất ngờ: lễ trao giải phụ! Những giải này không tính điểm, nhưng mỗi giải là một kỷ lục có thật mà khán giả xứng đáng được biết. |  | Một sân khấu nhỏ hoạt hình bên cạnh sân chính, trang trí bóng bay và dải ruy băng, trên bàn là hàng cúp nhỏ đủ hình dáng (không chữ); anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đứng sau bục cầm phong bì. |
| b02 | 00:09.8–00:16.4 (6.5s) | L379 | Giải phụ thứ nhất: tuyển thủ có thành viên sống thọ nhất! Và giải thuộc về... Cá Heo! Mời khán giả làm quen với bà cụ Nicklo. |  | Một chú chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái cái già có vây lưng sứt một vết nhỏ, đeo cặp kính lão tròn, đội chiếc mũ len, bơi chậm rãi giữa vịnh biển, xung quanh là những chú cá heo nhỏ hơn; KHÔNG có anh MC trong cảnh này. |
| b03 | 00:16.4–00:27.6 (11.2s) | L380 | Nicklo là một cô cá heo hoang dã sống ở vịnh Sarasota, bang Florida. Một nhóm nghiên cứu đã theo dõi cá heo ở vịnh này từ năm 1970, và họ đã nhìn thấy Nicklo hơn 820 lần. | **820 LẦN** · được nhìn thấy · R/360 · [0.5, 0.5] | Một chiếc thuyền nghiên cứu hoạt hình trên vịnh, nhà khoa học cầm máy ảnh có ống kính dài chụp vây lưng của chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái già, trên thuyền là cuốn album dày cộp toàn ảnh vây lưng; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:27.6–00:37.2 (9.6s) | L381 | Để biết tuổi của cô, các nhà khoa học đã đếm các lớp vân trên một chiếc răng, giống như đếm vòng gỗ trên thân cây. Và lần cuối cùng Nicklo được nhìn thấy, vào năm 2017, cô đã 67 tuổi. | **67 TUỔI** · cá heo hoang dã · R/360 · [0.5, 0.45] | Hình phóng to hoạt hình mặt cắt một chiếc răng cá heo có những vòng vân đồng tâm như vòng gỗ, bên cạnh là mặt cắt một thân cây có vòng tuổi để so sánh; KHÔNG có anh MC trong cảnh này. |
| b05 | 00:37.2–00:47.7 (10.5s) | L382 | Nicklo là cá heo hoang dã sống thọ nhất từng được ghi nhận. Cô sinh ít nhất 4 con, con út ra đời khi cô đã 48 tuổi. Và đứa con út ấy sau này cũng có con, nối dài ba thế hệ trong cùng một vịnh biển. |  | Ba thế hệ chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái bơi nối đuôi nhau trong vịnh: bà Ních-lô đeo kính lão đi đầu, con gái ở giữa, cháu nhỏ ở cuối, ánh hoàng hôn ấm áp trên mặt nước; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:47.7–00:54.2 (6.5s) | L383 | Giám khảo xin cúi đầu chào bà cụ Nicklo. 67 năm giữa biển khơi, quả là một hành trình sinh tồn đáng nể. |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ đứng dậy, bỏ mũ ra cúi đầu kính cẩn, tay đặt lên ngực. |
| b07 | 00:54.2–01:07.4 (13.3s) | L384 | Giải phụ thứ hai: thọ nhất trong nhóm... nhỏ con. Và giải thuộc về Thú Mỏ Vịt! Năm 2023, ở một con suối nhỏ gần thành phố Melbourne, nước Úc, các nhà nghiên cứu bắt lại một chú Thú Mỏ Vịt đực đã được gắn thẻ từ hơn 20 năm trước. |  | Một con suối nhỏ hoạt hình ven thành phố, nhà nghiên cứu cầm máy quét nhỏ đưa lại gần chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá già có hàng lông mày bạc, máy quét kêu "bíp" và hiện biểu tượng ngôi sao; KHÔNG có anh MC trong cảnh này. |
| b08 | 01:07.4–01:16.2 (8.8s) | L385 | Chú được gắn thẻ khi mới khoảng một tuổi, và khi bị bắt lại, chú đã 24 tuổi. Đây là Thú Mỏ Vịt hoang dã sống thọ nhất từng được ghi nhận, vượt kỷ lục cũ 21 tuổi. | **24 TUỔI** · kỷ lục hoang dã · R/360 · [0.5, 0.45] | chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá già đội chiếc mũ sinh nhật nhỏ, trước mặt là chiếc bánh kem cắm nến, bên cạnh có một tấm bảng hai cột so sánh: cột cũ thấp hơn, cột mới cao hơn (không chữ); KHÔNG có anh MC trong cảnh này. |
| b09 | 01:16.2–01:23.9 (7.7s) | L386 | Trong khi đó, ở sa mạc Kalahari, Lửng Mật hoang dã thường chỉ sống khoảng 3-8 năm. Gã giang hồ dũng cảm nhất đại hội... lại có cuộc đời khá ngắn ngủi. | **3-8 NĂM** · tuổi thọ hoang dã · L/360 · [0.5, 0.5] | chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần ngồi trên mỏm đá sa mạc nhìn hoàng hôn, bên cạnh là chiếc đồng hồ cát nhỏ, vẻ mặt trầm ngâm nhưng không hề sợ hãi; KHÔNG có anh MC trong cảnh này. |
| b10 | 01:23.9–01:34.8 (10.9s) | L387 | Giải phụ thứ ba: thợ lặn chăm chỉ nhất! Và lại là Thú Mỏ Vịt! Ở một hồ nước trên núi ở Tasmania, các nhà khoa học đã gắn thiết bị đo độ sâu lên 11 chú Thú Mỏ Vịt và ghi lại gần 90.000 lần lặn. | **~90.000** · lần lặn · R/360 · [0.5, 0.5] | Mặt hồ trên núi hoạt hình phủ sương sớm, bên dưới là những đường lặn ngoằn ngoèo vẽ chi chít như bức tranh, mỗi đường kết thúc ở một chú chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá nhỏ; KHÔNG có anh MC trong cảnh này. |
| b11 | 01:34.8–01:44.5 (9.6s) | L388 | Mỗi lần lặn trung bình chỉ khoảng 31 giây! Ngoi lên thở 10 giây, rồi lại lặn tiếp! Trung bình 75 lần mỗi giờ! Và có những chuyến kiếm ăn, nó lặn tới 1.600 lần liên tục! | **1.600 LẦN** · một chuyến kiếm ăn · R/360 · [0.5, 0.5] | chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá lặn xuống, ngoi lên, lặn xuống, ngoi lên như chiếc pít-tông, bên cạnh là bộ đếm số hoạt hình đang nhảy liên tục, một chú vịt bên cạnh nhìn chóng cả mặt; KHÔNG có anh MC trong cảnh này. |
| b12 | 01:44.5–01:55.7 (11.2s) | L389 | Giải phụ thứ tư: lò sưởi bí ẩn nhất! Và giải thuộc về Rái Cá Biển. Khán giả của kênh đã biết Rái Cá đốt năng lượng rất nhanh để giữ ấm. Nhưng suốt nhiều chục năm, không ai biết chính xác hơi ấm ấy được tạo ra ở đâu trong |  | chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách nằm ngửa trên mặt nước lạnh, quanh người tỏa ra vầng hơi ấm màu cam, trên đầu là dấu chấm hỏi to, một nhà khoa học hoạt hình cầm đèn pin soi khắp người rái cá tìm kiếm; KHÔNG có anh MC trong cảnh này. |
| b13 | 01:55.7–02:04.2 (8.5s) | L390 | cơ thể. Năm 2020 mốt, các nhà khoa học lấy mẫu cơ bắp của 21 chú Rái Cá Biển, từ con non đến con trưởng thành, và đo cách các tế bào cơ sử dụng | **21 CHÚ** · mẫu cơ bắp · R/360 · [0.5, 0.5] | Phòng thí nghiệm hoạt hình có chiếc máy đo hô hấp tế bào với những ống nghiệm nhỏ, trên màn hình là hình tế bào cơ phóng to có những nhà máy năng lượng tí hon bên trong; KHÔNG có anh MC trong cảnh này. |
| b14 | 02:04.2–02:16.8 (12.5s) | L391 | ô-xy. Và họ phát hiện ra: những nhà máy năng lượng tí hon trong tế bào cơ của Rái Cá bị... rò rỉ, có chủ đích. Thay vì biến hết năng lượng thành sức để cử động, chúng để một phần lớn thoát ra dưới dạng nhiệt. Cơ bắp sưởi ấm cơ thể mà không cần cử động! |  | Hình hoạt hình bên trong tế bào cơ: một nhà máy năng lượng nhỏ có những lỗ rò cố ý, từ đó tỏa ra hơi nhiệt màu cam ấm áp; bên cạnh, chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách nằm im ngủ mà người vẫn tỏa ấm; KHÔNG có anh MC trong cảnh này. |
| b15 | 02:16.8–02:26.9 (10.2s) | L392 | Điều bất ngờ nhất: ngay cả Rái Cá con mới sinh, cơ bắp còn non nớt, các tế bào cơ đã có khả năng tạo nhiệt ngang bằng con trưởng thành. Lò sưởi được lắp sẵn... từ lúc chào đời! |  | Một chú rái cá con lông xù nằm trên ngực mẹ, bên trong cơ thể nhỏ bé vẽ một chiếc lò sưởi tí hon đã cháy đỏ, có gắn chiếc nơ quà tặng như món quà sinh nhật; KHÔNG có anh MC trong cảnh này. |
| b16 | 02:26.9–02:38.2 (11.2s) | L393 | Giải phụ thứ năm: thiết kế không cần sửa lâu nhất! Và giải thuộc về... Chim Bồ Nông! Ở vùng Luberon, miền Nam nước Pháp, người ta tìm thấy hóa thạch của một chú bồ nông sống cách đây khoảng 30 triệu năm. | **30 TRIỆU** · năm tuổi hóa thạch · R/360 · [0.5, 0.45] | Một phiến đá vôi hoạt hình màu kem có in hóa thạch bộ xương chim với chiếc mỏ dài gần như nguyên vẹn, một nhà cổ sinh vật học đeo kính lúp cúi soi, phía sau là những ngọn đồi miền Nam nước Pháp; KHÔNG có anh MC trong cảnh này. |
| b17 | 02:38.2–02:47.1 (9.0s) | L394 | Và điều khiến các nhà khoa học kinh ngạc: chiếc mỏ của chú bồ nông 30 triệu năm tuổi ấy... gần như giống hệt mỏ bồ nông ngày nay. 30 triệu năm, tạo hóa gần như không phải sửa gì thêm! |  | Hai chiếc mỏ đặt cạnh nhau hoạt hình: bên trái là mỏ hóa thạch màu đá xám, bên phải là mỏ của chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn ngày nay màu cam, giống nhau như đúc, chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn đứng cạnh nhìn hóa thạch như nhìn ảnh ông cố; KHÔNG có anh MC trong cảnh này. |
| b18 | 02:47.1–02:55.8 (8.7s) | L395 | Các nhà khoa học đoán rằng chiếc mỏ ấy đã quá phù hợp để bắt cá, nên không cần thay đổi. Một sản phẩm ra mắt từ 30 triệu năm trước... mà chưa từng phải tung bản cập nhật! |  | chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn cầm chiếc điện thoại hoạt hình, màn hình hiện biểu tượng mũi tên cập nhật bị gạch chéo, bên cạnh là chiếc mỏ được gắn huy hiệu ngôi sao vàng; KHÔNG có anh MC trong cảnh này. |
| b19 | 02:55.8–03:02.5 (6.7s) | L396 | Giải phụ thứ sáu: tên gọi thú vị nhất! Ban tổ chức đã tra tên khoa học của từng tuyển thủ, và phát hiện ra mỗi cái tên là một câu chuyện. |  | Một cuốn từ điển La-tinh khổng lồ hoạt hình mở ra giữa sân khấu, những dòng chữ (không đọc được, chỉ là nét gạch) bay lên thành hình bóng mười tuyển thủ; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cầm kính lúp soi. |
| b20 | 03:02.5–03:11.4 (8.9s) | L397 | Tên khoa học của Lửng Mật là Mellivora capensis. Mellivora nghĩa là "kẻ ăn mật", còn capensis là "đến từ mũi Hảo Vọng", nơi mẫu vật đầu tiên được thu thập ở Nam Phi. |  | chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần đứng trên mũi đất nhô ra biển có ngọn hải đăng, tay cầm hũ mật ong, phía sau là biển cả và sóng vỗ; KHÔNG có anh MC trong cảnh này. |
| b21 | 03:11.4–03:19.3 (7.9s) | L398 | Tên của Tôm Tít trong khoa học là bộ Chân Miệng, vì những chiếc chân bắt mồi của nó nằm ngay gần miệng. Một võ sĩ mà tay nằm ở... cằm! |  | Cận cảnh chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh chỉ vào hai chiếc càng búa gập ngay dưới miệng mình, vẻ mặt tự hào, bên cạnh là hình vẽ một võ sĩ người hoạt hình có hai nắm đấm mọc ra từ cằm trông rất buồn cười; KHÔNG có anh MC trong cảnh này. |
| b22 | 03:19.3–03:28.5 (9.1s) | L399 | Gấu Nước được mô tả lần đầu vào năm 1773 bởi một mục sư người Đức. Ông nhìn qua kính hiển vi, thấy sinh vật này lạch bạch như một chú gấu, nên gọi nó là "chú gấu nước | **1773** · lần đầu được mô tả · R/360 · [0.5, 0.4] | Một mục sư người Đức hoạt hình thế kỷ mười tám, tóc giả trắng, cúi nhìn qua chiếc kính hiển vi bằng đồng cổ, trong bong bóng phóng to là chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương đang lạch bạch vẫy tay; KHÔNG có anh MC trong cảnh này. |
| b23 | 03:28.5–03:40.5 (12.1s) | L400 | nhỏ". Ba năm sau, một nhà khoa học người Ý đặt cho nó cái tên khoa học có nghĩa là "kẻ bước chậm". Và hơn 200 năm sau, các nhà khoa học hiện đại đo được tốc độ đi dạo của nó: khoảng nửa thân mình mỗi giây. Đúng là danh bất hư truyền! |  | chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương đi chậm rãi trên một chiếc lá rêu, phía sau là một chú ốc sên hoạt hình đang vượt mặt và vẫy tay chào, chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ  |
| b24 | 03:40.5–03:48.9 (8.4s) | L401 | Còn Thú Mỏ Vịt? Ban đầu, nó được đặt tên khoa học là Platypus, nghĩa là "chân dẹt". Nhưng các nhà khoa học sớm phát hiện ra: cái tên ấy đã thuộc về... một loài bọ cánh cứng! |  | Một chú bọ cánh cứng nhỏ hoạt hình đeo bảng tên hình chữ nhật (không chữ) đứng khoanh tay trước cửa, chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá đứng ngoài nhìn vào ngơ ngác, tay cầm bảng tên giống hệt; KHÔNG có anh MC trong cảnh này. |
| b25 | 03:48.9–04:00.4 (11.4s) | L402 | Thế là Thú Mỏ Vịt phải nhận một tên khoa học mới, có nghĩa là "mỏ chim, giống vịt". Nhưng cái tên cũ "chân dẹt" vẫn ở lại làm tên gọi thường ngày bằng tiếng Anh đến tận bây giờ. Mất tên khoa học vào tay một con bọ... nhưng vẫn giữ được biệt danh! |  | chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá đeo hai chiếc bảng tên cùng lúc, một bảng nhỏ hình mỏ chim và một bảng lớn hình bàn chân dẹt, cười tươi tạo dáng chụp ảnh; KHÔNG có anh MC trong cảnh này. |
| b26 | 04:00.4–04:09.2 (8.8s) | L403 | Giải phụ cuối cùng, và là giải mà ban tổ chức trân trọng nhất: giải hồi sinh ngoạn mục. Giải này thuộc về Rái Cá Biển, và câu chuyện của nó bắt đầu từ hơn 200 năm trước. |  | Một con tàu buồm cổ hoạt hình màu xám u ám trên biển lạnh, trên boong là những chồng da lông chất cao, bầu trời phủ mây đen; KHÔNG có anh MC trong cảnh này. |
| b27 | 04:09.2–04:21.1 (11.9s) | L404 | Bộ lông dày nhất thế giới động vật từng khiến Rái Cá Biển trở thành món hàng săn lùng. Suốt hơn một thế kỷ rưỡi, người ta săn bắt chúng để lấy da. Đến năm 1911, trên toàn thế giới chỉ còn khoảng 1.000 đến 2.000 con Rái Cá Biển. | **~1.500** · còn lại năm 1911 · R/360 · [0.5, 0.5] | Một tấm bản đồ bờ biển Bắc Thái Bình Dương hoạt hình màu xám, chỉ còn vài chấm sáng nhỏ lẻ loi rải rác ở những hòn đảo xa, mỗi chấm là một nhóm rái cá nhỏ; KHÔNG có anh MC trong cảnh này. |
| b28 | 04:21.1–04:33.1 (12.0s) | L405 | Và cũng chính năm 1911 ấy, bốn quốc gia đã ký một hiệp ước cấm săn bắt. Những nhóm rái cá nhỏ bé còn sót lại bắt đầu sinh sôi trở lại. Ngày nay, đã có hơn 100.000 con Rái Cá Biển trên khắp các vùng biển xưa của chúng. | **> 100.000** · ngày nay · R/360 · [0.5, 0.5] | Bản đồ bờ biển hoạt hình dần dần sáng lên từ những chấm nhỏ lan rộng thành những dải màu xanh dài, trên mặt nước hàng ngàn chú chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách nằm ngửa vẫy tay; KHÔNG có anh MC trong cảnh này. |
| b29 | 04:33.1–04:40.3 (7.2s) | L406 | Từ 1.000 con lên hơn 100.000 con. Đó là bằng chứng rõ ràng nhất rằng: khi con người dừng tay đúng lúc, thiên nhiên biết cách tự chữa lành. |  | chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách mẹ ôm rái cá con nằm ngửa giữa rừng tảo bẹ xanh mướt dưới ánh nắng, xung quanh là cá bơi tung tăng, một chiếc ruy băng huy chương vàng lấp lánh lơ lửng phía trên; KHÔNG có anh MC trong cảnh này. |
| b30 | 04:40.3–04:47.6 (7.4s) | L407 | Giám khảo xin trao giải đặc biệt này cho Rái Cá Biển. Và cũng xin gửi lời cảm ơn tới những người đã ký hiệp ước năm ấy. |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ trao chiếc cúp nhỏ hình trái tim cho chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách, rái cá ôm chiếc cúp như ôm hòn đá yêu thích, khán đài vỗ tay. |
| b31 | 04:47.6–04:53.9 (6.2s) | L408 | Ủa, vậy là năm nay không có giải phụ nào cho người ngủ giỏi nhất hả chú? Cháu ngủ 22 tiếng mỗi ngày đó! |  | chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ giơ tay hỏi từ hàng ghế khán đài, mắt lim dim, ôm chiếc gối hình chiếc lá khuynh diệp; KHÔNG có anh MC trong cảnh này. |
| b32 | 04:53.9–05:03.7 (9.8s) | L409 | Câu hỏi rất hợp lý! Nhưng chuyện Koala ngủ 22 tiếng thì khán giả của kênh đã biết rồi. Đại hội này chỉ trao giải cho những điều mới. Hẹn bạn ở... đại hội ngủ trưa! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cúi người xoa đầu chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ, đưa cho bạn ấy một chiếc huy hiệu nhỏ hình mặt trăng, chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân t |
| b33 | 05:03.7–05:10.8 (7.1s) | L410 | Lễ trao giải phụ khép lại! Và giờ, xin mời tất cả các tuyển thủ bước vào sân khấu chính, cho vòng thi cuối cùng của Đại Hội Sinh Tồn! |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng giơ tay về phía sân khấu chính đang sáng rực ánh đèn, mười tuyển thủ xếp hàng bước vào, mỗi bạn ôm một hộp quà có nơ. |

### scene13 · AI ĐÃ GIÚP ÍCH CHO LOÀI NGƯỜI NHIỀU NHẤT · 299.5s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.6 (9.6s) | L411 | Vòng chung kết: món quà cho loài người! Mỗi tuyển thủ sẽ trình bày một phát minh, một loại thuốc, hay một công nghệ mà con người đã học được, hoặc đang học, từ chính cơ thể mình. |  | Sân khấu chung kết hoạt hình rực rỡ, phía sau là màn hình khổng lồ hình quả địa cầu, mười tuyển thủ đứng thành hàng, mỗi bạn ôm một chiếc hộp quà có nơ (không chữ); anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đứng giữa giơ micro. |
| b02 | 00:09.6–00:15.2 (5.6s) | L412 | Rái Cá Biển mở hộp quà đầu tiên. Bên trong là... một bộ đồ lặn có lông! |  | chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách mở hộp quà, lôi ra một bộ đồ lặn hoạt hình phủ đầy lông mềm xù xì như thú nhồi bông, khán giả bật cười; KHÔNG có anh MC trong cảnh này. |
| b03 | 00:15.2–00:24.5 (9.3s) | L413 | Năm 2016, các kỹ sư ở Viện Công nghệ Massachusetts đã làm những tấm cao su phủ lông nhân tạo, mô phỏng bộ lông của rái cá và hải ly, rồi nhúng chúng vào chất lỏng ở nhiều tốc độ khác nhau. | **2016** · lông nhân tạo · L/360 · [0.5, 0.5] | Phòng thí nghiệm kỹ thuật hoạt hình: một cánh tay máy nhúng tấm cao su phủ lông lăn tăn xuống bể chất lỏng trong suốt, camera tốc độ cao ghi hình, những bọt khí nhỏ bám trên lông; KHÔNG có anh MC trong cảnh này. |
| b04 | 00:24.5–00:33.9 (9.4s) | L414 | Họ phát hiện: lông càng dày, lặn xuống càng nhanh, thì càng giữ lại được nhiều không khí. Từ đó, họ tìm ra công thức để có thể chế tạo những bộ đồ lặn ấm áp lấy cảm hứng từ bộ lông rái cá. |  | Biểu đồ hoạt hình: ba mẫu lông thưa, vừa, dày, mẫu dày nhất giữ lớp bong bóng khí dày nhất; bên cạnh là phác thảo một bộ đồ lặn tương lai có lông bên trong; KHÔNG có anh MC trong cảnh này. |
| b05 | 00:33.9–00:38.1 (4.2s) | L415 | Chim Cánh Cụt mở hộp quà thứ hai: một tấm lưới thép nhỏ xíu, lấp lánh. |  | chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ mở hộp quà, giơ lên một tấm lưới kim loại mịn óng ánh như tấm vải bạc; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:38.1–00:50.8 (12.7s) | L416 | Các nhà khoa học ở Canada thắc mắc: tại sao chim cánh cụt sống giữa băng giá mà lông không bao giờ bị đóng băng? Họ soi lông chim cánh cụt dưới kính hiển vi, và thấy những sợi lông nhỏ đan móc vào nhau như một tấm lưới, trên bề mặt có những rãnh siêu nhỏ. |  | Hình phóng to dưới kính hiển vi hoạt hình: các sợi lông nhỏ đan móc vào nhau thành lưới, trên bề mặt có những rãnh song song li ti; một nhà khoa học hoạt hình nhìn qua kính hiển vi; KHÔNG có anh MC trong cảnh này. |
| b07 | 00:50.8–01:01.4 (10.5s) | L417 | Họ bắt chước cấu trúc ấy bằng lưới thép không gỉ, khắc thêm rãnh siêu nhỏ bằng tia laser. Kết quả: băng bám vào tấm lưới yếu hơn khoảng 95% so với tấm thép phẳng thông thường! | **-95%** · băng bám · R/360 · [0.72, 0.5] | Hai tấm kim loại hoạt hình so sánh dưới mưa băng: tấm thép phẳng bên trái bị đóng một lớp băng dày cứng; tấm lưới bên phải băng chỉ bám mỏng và đang nứt vỡ rơi xuống; KHÔNG có anh MC trong cảnh này. |
| b08 | 01:01.4–01:11.5 (10.1s) | L418 | Các nhà khoa học hy vọng vật liệu này sẽ giúp chống đóng băng cho đường dây điện, tuabin gió và máy bay, mà không cần hóa chất. Quý ông Vest Đuôi Tôm... đang góp phần giữ điện cho cả một thành phố mùa đông! |  | Một thành phố hoạt hình giữa mùa đông tuyết trắng, đường dây điện và cột điện được bọc lưới bạc lấp lánh, băng không bám được, đèn trong nhà vẫn sáng ấm áp; chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ đứng trên mái nhà tự hào; KHÔNG có anh MC trong cảnh này. |
| b09 | 01:11.5–01:16.5 (5.0s) | L419 | Bồ Nông mở hộp quà thứ ba. Bên trong là... một chiếc máy bay đồ chơi! |  | chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn dùng mỏ gắp từ hộp quà ra một chiếc máy bay chở khách đồ chơi màu trắng, vẻ mặt tự hào; KHÔNG có anh MC trong cảnh này. |
| b10 | 01:16.5–01:25.8 (9.3s) | L420 | Từ việc nghiên cứu cách những đàn chim lớn bay theo hình chữ V để tiết kiệm sức, hãng máy bay Airbus đã thử nghiệm cho hai chiếc máy bay chở khách cỡ lớn bay nối đuôi nhau, cách nhau khoảng 3km. |  | Bầu trời xanh hoạt hình có hai chiếc máy bay chở khách bay nối đuôi nhau, phía sau chiếc đầu có những luồng xoáy khí xoắn ốc màu xanh nhạt nâng chiếc sau lên; bên dưới một đàn bồ nông bay chữ V cùng hướng; KHÔNG có anh MC trong cảnh này. |
| b11 | 01:25.8–01:35.2 (9.4s) | L421 | Chiếc bay sau lướt trên luồng khí của chiếc bay trước, giống hệt bồ nông. Chuyến bay thử năm 2021 từ Pháp sang Canada đã tiết kiệm được hơn 6 tấn khí thải carbon. | **-6 TẤN** · khí thải CO2 · R/360 · [0.6, 0.5] | Hai chiếc máy bay hạ cánh xuống sân bay đầy tuyết, bên cạnh là một quả bóng bay hình đám mây xám có biểu tượng chiếc cân sáu khối, bị xì hơi nhỏ dần; KHÔNG có anh MC trong cảnh này. |
| b12 | 01:35.2–01:39.6 (4.4s) | L422 | Tôm Tít mở hộp quà thứ tư, và bên trong là... một chiếc mũ bảo hiểm! |  | chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh mở hộp quà, lôi ra một chiếc mũ bảo hiểm thể thao hoạt hình có hoa văn xoắn ốc bên trong vỏ, đội thử lên đầu; KHÔNG có anh MC trong cảnh này. |
| b13 | 01:39.6–01:47.6 (8.0s) | L423 | Một chiếc càng búa của Tôm Tít phải chịu hàng chục ngàn cú đấm trong đời mà không vỡ. Các kỹ sư ở Đại học California đã soi vào bên trong để tìm hiểu bí mật. |  | Một kỹ sư hoạt hình đeo kính bảo hộ soi chiếc càng búa của chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh dưới kính hiển vi điện tử lớn, màn hình bên cạnh hiện hình phóng to nhiều lớp; KHÔNG có anh MC trong cảnh này. |
| b14 | 01:47.6–01:55.6 (8.0s) | L424 | Họ thấy những lớp sợi xếp xoắn như cầu thang xoắn ốc. Mỗi khi có cú va chạm, vết nứt bị buộc phải đi vòng vèo theo các lớp xoắn, nên không thể xuyên thẳng qua. |  | Mặt cắt hoạt hình chiếc càng búa của chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh: bên trong là những lớp sợi xếp xoay dần như cầu thang xoắn ốc, một vết nứt màu đỏ cố chui vào nhưng bị lạc lối đi vòng vèo rồi dừng lại; KHÔNG có anh MC trong cảnh này. |
| b15 | 01:55.6–02:06.9 (11.2s) | L425 | Cấu trúc xoắn ốc ấy đang được các kỹ sư bắt chước để làm ra những vật liệu nhẹ mà chịu va đập tốt, hướng tới mũ bảo hiểm, áo giáp và khung xe, khung máy bay. Giám khảo ghi nhận, nhưng xin để dành huy chương chờ những sản phẩm đầu tiên ra đời! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ cẩn thận cất một chiếc huy chương vào hộp nhỏ có khóa, dán nhãn hình ngôi sao, đặt lên giá "để dành"; chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh gật đầu chấp nhận, vẫn đội chiếc mũ bả |
| b16 | 02:06.9–02:17.2 (10.4s) | L426 | Cá Heo xin chen ngang mở một hộp quà... ngoài danh sách. Bên trong là một chiếc phao nhỏ màu cam. Và câu chuyện của chiếc phao này bắt đầu ở một bến cảng nước Iraq, tháng 3/2003. |  | chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái dùng mũi đẩy ra một chiếc hộp quà nhỏ, bên trong là chiếc phao đánh dấu màu cam có dây buộc, phía sau là bến cảng hoạt hình với những con tàu lớn đang chờ ngoài khơi; KHÔNG có anh MC trong cảnh này. |
| b17 | 02:17.2–02:26.3 (9.1s) | L427 | Bến cảng ấy bị thả hơn 100 quả thủy lôi và vật nổ dưới nước. Máy dò dưới nước đã phát hiện hơn 200 vật thể đáng ngờ, nhưng máy không phân biệt được đâu là thủy lôi, đâu là rác hay đá. | **> 100** · thủy lôi và vật nổ · R/360 · [0.5, 0.5] | Mặt cắt đáy cảng hoạt hình đầy những vật thể lẫn lộn: thủy lôi tròn có gai, xe đẩy cũ, tảng đá, thùng phuy; phía trên một chiếc tàu ngầm robot nhỏ màu vàng chiếu đèn dò với dấu chấm hỏi; KHÔNG có anh MC trong cảnh này. |
| b18 | 02:26.3–02:34.8 (8.5s) | L428 | Đó là lúc 8 chú cá heo của Hải quân Mỹ được gửi xuống. Bằng tiếng định vị, cá heo phân biệt được vật thể tự nhiên và vật thể do con người làm ra, kể cả những thứ bị vùi trong bùn. |  | Một chiếc xuồng hơi hoạt hình chở người huấn luyện và một chú chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái đeo dây đai nhỏ, chú cá heo nhảy xuống nước, những vòng sóng âm tỏa ra hướng về đáy cảng đục ngầu; KHÔNG có anh MC trong cảnh này. |
| b19 | 02:34.8–02:39.5 (4.7s) | L429 | Khi phát hiện thủy lôi, chúng bơi về báo cho người huấn luyện, rồi mang chiếc phao xuống đánh dấu vị trí. |  | Một chú chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái dưới nước phát ra những vòng sóng âm hướng về một quả thủy lôi vùi nửa trong bùn, rồi ngậm chiếc phao cam đặt cạnh đó; trên mặt nước là chiếc xuồng có người huấn luyện chờ sẵn; KHÔNG có anh MC trong cảnh này. |
| b20 | 02:39.5–02:51.2 (11.7s) | L430 | Nhờ vậy, chỉ khoảng một tuần sau, bến cảng đã được mở lại để những con tàu chở gạo và lương thực cập bến. Các nhà khoa học hải quân thừa nhận: trong vùng nước đục và nhiều vật cản, khả năng định vị của cá heo vẫn vượt mọi máy móc hiện có. |  | Một con tàu chở hàng hoạt hình chở đầy bao gạo cập bến an toàn, người dân trên bờ vẫy tay, dưới nước chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái nhô lên mỉm cười; KHÔNG có anh MC trong cảnh này. |
| b21 | 02:51.2–02:58.6 (7.4s) | L431 | Giám khảo ghi nhận món quà ngoài danh sách của Cá Heo. Nhưng vì đây là phần chen ngang... nên chỉ được tính là điểm cộng tinh thần! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ mỉm cười gõ búa nhẹ, gắn một ngôi sao vàng nhỏ lên chiếc phao cam, chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái gật đầu vui vẻ. |
| b22 | 02:58.6–03:02.4 (3.8s) | L432 | Gấu Nước mở hộp quà thứ năm. Bên trong là... một đoạn gen phát sáng. |  | chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương mở chiếc hộp quà to hơn người nó, bên trong là một chuỗi xoắn ADN nhỏ phát ánh sáng xanh lam huyền ảo; KHÔNG có anh MC trong cảnh này. |
| b23 | 03:02.4–03:11.6 (9.2s) | L433 | Năm 2016, các nhà khoa học Nhật Bản giải mã bộ gen của một loài gấu nước cực kỳ khỏe, và tìm thấy một loại đạm chỉ gấu nước mới có. Họ đặt tên nó là Dsup, nghĩa là "chất chống hư hại". |  | Phòng thí nghiệm Nhật Bản hoạt hình có cây anh đào ngoài cửa sổ, một nhà khoa học đeo kính nhìn vào màn hình hiện chuỗi xoắn ADN và một tấm khiên nhỏ bọc quanh nó; KHÔNG có anh MC trong cảnh này. |
| b24 | 03:11.6–03:20.3 (8.7s) | L434 | Rồi họ làm một thí nghiệm táo bạo: đưa đoạn gen này vào tế bào người nuôi trong phòng thí nghiệm, rồi chiếu tia X. Kết quả: tế bào người có đạm Dsup bị hư hại ADN ít hơn khoảng 40%! | **-40%** · hư hại ADN · R/360 · [0.72, 0.5] | Hai đĩa tế bào hoạt hình dưới chùm tia X màu tím: đĩa bên trái tế bào người bị vỡ vụn nhiều mảnh; đĩa bên phải tế bào được bao bọc bởi những đám mây khiên xanh nhỏ của gấu nước, ít bị vỡ hơn hẳn; KHÔNG có anh MC trong cảnh này. |
| b25 | 03:20.3–03:26.0 (5.7s) | L435 | Một chú gấu nước bé hơn hạt cát đã cho tế bào người... mượn tạm một chiếc áo giáp chống phóng xạ! |  | chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương tí hon đang mặc cho một tế bào người hoạt hình to tròn một chiếc áo giáp màu xanh nhỏ xíu, tế bào nhìn xuống bối rối nhưng cảm động; KHÔNG có anh MC trong cảnh này. |
| b26 | 03:26.0–03:35.6 (9.6s) | L436 | Và cuối cùng, tuyển thủ dẫn đầu: Thú Mỏ Vịt. Ở vòng ba, Thú Mỏ Vịt đã kể về chất kháng khuẩn trong sữa. Hôm nay, nó mở hộp quà thứ sáu, và bên trong là... một giọt nọc độc. |  | chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá mở hộp quà, bên trong là một lọ thủy tinh nhỏ chứa một giọt chất lỏng màu tím lấp lánh, khán giả lùi lại vì sợ; KHÔNG có anh MC trong cảnh này. |
| b27 | 03:35.6–03:46.3 (10.7s) | L437 | Thú Mỏ Vịt đực có chiếc cựa độc ở chân sau. Năm 2016, các nhà khoa học Úc phát hiện trong nọc độc ấy có một loại hormone gọi là GLP-1. Ở người, hormone này giúp cơ thể tiết ra insulin để hạ đường huyết. |  | Sơ đồ hoạt hình: cựa độc ở chân sau chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá, một mũi tên chỉ sang một phân tử hóc-môn nhỏ, rồi mũi tên chỉ tiếp sang tuyến tụy hoạt hình đang tiết ra những giọt in-su-lin vàng; KHÔNG có anh MC trong cảnh này. |
| b28 | 03:46.3–03:55.3 (9.0s) | L438 | Vấn đề là ở người, hormone này bị phân hủy chỉ trong vài phút. Còn hormone trong nọc Thú Mỏ Vịt thì bền hơn hẳn, vì nó vừa phải làm việc trong ruột, vừa phải làm việc trong nọc độc. |  | Hai chiếc đồng hồ cát hoạt hình: đồng hồ của người cát chảy hết rất nhanh, đồng hồ của chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá cát chảy rất chậm, rất bền bỉ; KHÔNG có anh MC trong cảnh này. |
| b29 | 03:55.3–04:05.0 (9.7s) | L439 | Và một hormone bền hơn chính là điều mà các nhà khoa học tìm kiếm để làm thuốc điều trị bệnh tiểu đường loại hai. Hiện nay các nhóm nghiên cứu ở Úc đang thử nghiệm những phân tử lấy cảm hứng từ nọc Thú Mỏ Vịt trên chuột. |  | Một chú chuột thí nghiệm hoạt hình khỏe mạnh đứng trên chiếc cân, cạnh đó là ống nghiệm có hình chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá, một nhà khoa học ghi chép biểu đồ đường huyết đi xuống; KHÔNG có anh MC trong cảnh này. |
| b30 | 04:05.0–04:14.9 (9.9s) | L440 | Sữa có chất diệt khuẩn. Nọc độc có thể thành thuốc chữa tiểu đường. Con vật từng bị các nhà khoa học cầm kéo đi tìm đường chỉ khâu, hóa ra lại là một... hiệu thuốc biết bơi! |  | chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá mặc áo blouse trắng đứng sau quầy thuốc dưới nước, trên kệ phía sau là những lọ thuốc có hình giọt sữa và giọt nọc tím; KHÔNG có anh MC trong cảnh này. |
| b31 | 04:14.9–04:18.5 (3.7s) | L441 | Giám khảo ra hiệu chuẩn bị công bố. Cả sân vận động im phăng phắc. |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ đứng dậy trên bàn giám khảo, tay cầm phong bì, cả khán đài nín thở, ánh đèn sân khấu hội tụ về phía bà; KHÔNG có anh MC trong cảnh này. |
| b32 | 04:18.5–04:24.0 (5.5s) | L442 | Huy chương đồng vòng chung kết, 2 điểm: Chim Bồ Nông, người thầy dạy máy bay cách bay đỡ tốn sức! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ mở phong bì đầu tiên, phía dưới chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn bước lên bậc đồng, đôi cánh dang rộng, chiếc máy bay đồ chơi đậu trên mỏ. |
| b33 | 04:24.0–04:28.4 (4.4s) | L443 | Huy chương bạc, 4 điểm: Gấu Nước, người cho tế bào người mượn áo giáp! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ mở phong bì thứ hai, phía dưới chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương được nâng lên bậc bạc trên một chiếc đĩa nhỏ có kính lúp phóng to. |
| b34 | 04:28.4–04:32.6 (4.2s) | L444 | Và huy chương vàng vòng chung kết, 6 điểm, thuộc về... Thú Mỏ Vịt! |  | bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ mở phong bì cuối cùng, giơ cao tấm thiệp có hình chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá, pháo giấy vàng nổ tung khắp sân vận động. |
| b35 | 04:32.6–04:36.3 (3.7s) | L445 | Và đây là bảng điểm cuối cùng của Đại Hội Sinh Tồn lần thứ nhất! |  | tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) xoay vòng, đèn nhấp nháy liên hồi, mười cột điểm nhảy lên xuống hồi hộp trước khi dừng lại; KHÔNG có anh MC trong cảnh này. |
| b36 | 04:36.3–04:44.4 (8.1s) | L446 | Hạng ba: Lửng Mật, 6 điểm! Trắng tay suốt bốn vòng đầu, rồi bùng nổ với hai huy chương vàng: bà mẹ chuyển nhà mỗi 3 ngày, và gã giang hồ dám nhận mình chưa chắc đúng! |  | chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần bước lên bục hạng ba, đeo hai chiếc huy chương vàng, lửng con ngồi trên đầu, sáu con chim ưng xám bay lượn phía trên tung pháo giấy; KHÔNG có anh MC trong cảnh này. |
| b37 | 04:44.4–04:50.1 (5.7s) | L447 | Hạng hai: Cá Heo, 7 điểm! Người lính gác 15 ngày không ngủ, và người bạn của ngư dân Brazil suốt hơn 100 năm! |  | chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái nhảy vọt lên từ bể nước đặt trên bục hạng hai, đeo hai huy chương vàng và một huy chương đồng, những người đánh cá Bra-xin hoạt hình vẫy lưới chúc mừng; KHÔNG có anh MC trong cảnh này. |
| b38 | 04:50.1–04:55.0 (4.9s) | L448 | Và nhà vô địch Đại Hội Sinh Tồn lần thứ nhất, với ba huy chương vàng, một huy chương bạc và 14 |  | Đèn sân vận động tắt phụt, chỉ còn một vòng ánh sáng vàng rọi xuống chiếc vương miện bé xíu trên bệ đá giữa sân; KHÔNG có anh MC trong cảnh này. |
| b39 | 04:55.0–04:59.5 (4.5s) | L449 | điểm... Thú Mỏ Vịt! Tuyển thủ mà các chuyên gia dự đoán chỉ "tham gia cho vui"! |  | chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá đeo băng đô xanh và ba huy chương vàng bước lên bục cao nhất, anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đặt chiếc vương miện vàng bé xíu lên đầu, pháo hoa nổ rực trời, khán đài vỡ òa. |

### scene14 · NHÀ VÔ ĐỊCH BẤT NGỜ VÀ BÀI HỌC CỦA ĐẠI HỘI · 186.3s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.9 (9.9s) | L450 | Thú Mỏ Vịt đứng trên bục cao nhất, chiếc vương miện bé xíu hơi lệch trên đầu. Hơn 200 năm trước, khi mẫu vật đầu tiên đến châu Âu, các nhà khoa học tưởng nó là đồ giả. Đêm nay, nó là nhà vô địch. |  | chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá đứng trên bục vô địch, vương miện lệch trên đầu, khóc vì xúc động; bên cạnh là một khung ảnh cũ đen trắng vẽ nhà khoa học cầm kéo soi mẫu vật; KHÔNG có anh MC trong cảnh này. |
| b02 | 00:09.9–00:15.1 (5.2s) | L451 | Ủa... vậy là bạn mỏ vịt thắng thật ạ? Chúc mừng bạn! Bạn có muốn ôm cây với cháu không? |  | chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ chạy lạch bạch tới ôm chầm lấy chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá, hai bạn ôm nhau trên bục, vương miện suýt rơi; KHÔNG có anh MC trong cảnh này. |
| b03 | 00:15.1–00:22.3 (7.2s) | L452 | Nhìn lại cả tám vòng thi, có một điều thú vị: những tuyển thủ được dự đoán là mạnh nhất, Tôm Tít và Gấu Nước, lại không lên được bục vinh quang. |  | chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh và chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương đứng ở góc sân khoanh tay, nhìn lên bục vô địch, ban đầu hậm hực,  |
| b04 | 00:22.3–00:31.1 (8.7s) | L453 | Vì sinh tồn không chỉ là đánh nhau. Sinh tồn còn là giữ ấm giữa nước đá, là đi theo mặt trời 13.000km, là hợp tác với người đánh cá, là ôm cây cho mát. |  | Một bức tranh ghép nhiều ô hoạt hình: chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá bơi trong nước đá, chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ đi trên băng hướng về mặt trời, chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng |
| b05 | 00:31.1–00:40.9 (9.8s) | L454 | Và có 1 điểm chung giữa những tuyển thủ chiến thắng ở vòng cuối: con người đã học được từ chúng. Từ lông rái cá, lông cánh cụt, đội hình bồ nông, đến gen gấu nước và sữa, nọc độc của thú mỏ vịt. |  | Một nhà khoa học hoạt hình ngồi trên chiếc bàn tròn với mười tuyển thủ, mỗi tuyển thủ đưa cho nhà khoa học một món đồ nhỏ: chùm lông, tấm lưới, máy bay đồ chơi, ống nghiệm phát sáng, lọ thuốc; KHÔNG có anh MC trong cảnh này. |
| b06 | 00:40.9–00:48.6 (7.7s) | L455 | Thiên nhiên không chỉ là nơi để chúng ta ngắm nhìn. Đó còn là một thư viện khổng lồ, nơi mỗi loài vật là một cuốn sách chứa những lời giải mà con người chưa nghĩ ra. |  | Một thư viện hoạt hình khổng lồ có kệ sách là thân cây, mỗi cuốn sách trên kệ có gáy in hình một con vật khác nhau (không chữ), một em bé đang rút một cuốn ra đọc; KHÔNG có anh MC trong cảnh này. |
| b07 | 00:48.6–00:59.1 (10.5s) | L456 | Và cũng có những cuốn sách đang bị đe dọa. Ngày 12/2/2022, Koala ở ba bang miền Đông nước Úc chính thức bị xếp vào danh sách nguy cấp, sau hạn hán kéo dài, cháy rừng và mất nơi sống. |  | Một tấm hồ sơ hoạt hình màu đỏ có ảnh chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ ôm thân cây cháy sém, bên cạnh là con dấu hình chiếc khiên đỏ, phía sau là cánh rừng khô cháy; KHÔNG có anh MC trong cảnh này. |
| b08 | 00:59.1–01:07.3 (8.2s) | L457 | Tháng 11/2023, đến lượt Chồn Gulo ở lục địa nước Mỹ được đưa vào danh sách loài bị đe dọa, vì những lớp tuyết mùa xuân mà nó cần để sinh con đang ngày một ít đi. |  | Một tấm hồ sơ hoạt hình màu cam có ảnh chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh đứng trên sườn núi tuyết đang tan, nước chảy thành dòng, con dấu hình chiếc khiên cam; KHÔNG có anh MC trong cảnh này. |
| b09 | 01:07.3–01:14.3 (7.0s) | L458 | Chồn Gulo cần tuyết mùa xuân. Cá heo ở Laguna cần cá đối. Koala cần những cái cây để ôm, và những cơn mưa để uống. |  | Ba ô tranh hoạt hình buồn: tuyết tan sớm trên núi của chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh, con kênh vắng cá của chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái, cánh rừng khô hạn có chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép tr |
| b10 | 01:14.3–01:25.9 (11.6s) | L459 | Nếu những loài vật này biến mất, chúng ta không chỉ mất đi những sinh vật đáng yêu. Chúng ta còn mất đi những lời giải mà có khi... chưa ai kịp đọc. Nhưng câu chuyện Rái Cá Biển ở lễ trao giải phụ đã cho thấy: chưa bao giờ là quá muộn. |  | Một cuốn sách hoạt hình có bìa hình chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh đang mờ dần như sắp tan biến, một bàn tay em bé nhẹ nhàng giữ lấy nó; KHÔNG có anh MC trong cảnh này. |
| b11 | 01:25.9–01:32.1 (6.2s) | L460 | Trước khi chia tay, mời toàn thể khán đài cùng nhìn lại bảng tổng sắp cuối cùng của Đại Hội Sinh Tồn lần thứ nhất! |  | tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) lớn hiện lên giữa sân với mười cột sáng từ cao xuống thấp, pháo hoa nhỏ nổ hai bên, anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đứng cạnh giơ tay giới thiệu. |
| b12 | 01:32.1–01:41.0 (8.9s) | L461 | Vô địch: Thú Mỏ Vịt, 14 điểm! Ba huy chương vàng, một huy chương bạc! Bơi 5 tiếng trong nước 0 độ, ăn khỏe nhất cuộc thi, và mang đến cho loài người cả sữa diệt khuẩn lẫn nọc độc chữa bệnh! |  | chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá đội vương miện đứng trên đỉnh cột điểm cao nhất, đeo ba huy chương vàng và một huy chương bạc, băng đô xanh, hai tay giơ cao; KHÔNG có anh MC trong cảnh này. |
| b13 | 01:41.0–01:48.0 (7.0s) | L462 | Á quân: Cá Heo, 7 điểm! Người lính gác 15 ngày, đồng đội trăm năm của ngư dân Brazil, và bà cụ Nicklo 67 tuổi! |  | chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái nhảy vọt lên trên cột điểm thứ hai, đeo hai huy chương vàng và một huy chương đồng, nước bắn tung tóe lấp lánh; KHÔNG có anh MC trong cảnh này. |
| b14 | 01:48.0–01:53.8 (5.8s) | L463 | Hạng ba: Lửng Mật, 6 điểm! Trắng tay bốn vòng đầu, rồi bùng nổ với hai huy chương vàng nhờ làm mẹ giỏi và dám nhận mình chưa chắc đúng! |  | chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần đứng trên cột điểm thứ ba, lửng con ngồi trên đầu, đeo hai huy chương vàng, sáu con chim ưng xám bay lượn phía trên; KHÔNG có anh MC trong cảnh này. |
| b15 | 01:53.8–02:07.4 (13.6s) | L464 | Hạng tư: Gấu Nước, năm điểm, tuyển thủ được dự đoán vô địch đã bứt phá ở hai vòng cuối. Tiếp theo là nhóm bám đuổi, cùng 4 điểm: Chồn Gulo với hai huy chương bạc, Chim Cánh Cụt với một vàng một đồng, Rái Cá Biển với một bạc hai đồng, và Chim Bồ Nông với một bạc một đồng. |  | Ba cột điểm bằng nhau hoạt hình: chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương đứng trên cột hạng tư vẫy tay qua kính lúp; bên cạnh chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩn |
| b16 | 02:07.4–02:17.3 (10.0s) | L465 | Và cuối bảng, cùng 3 điểm: Tôm Tít, võ sĩ biết đấm khiên thay vì đấm người, và Koala, tuyển thủ ngủ nhiều nhất nhưng đã giúp khoa học sửa một hiểu lầm. Không ai ra về tay trắng! |  | Hai cột điểm cuối hoạt hình: chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh giơ càng chào kiểu võ sĩ, chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ ôm cột điểm ngủ g |
| b17 | 02:17.3–02:26.9 (9.6s) | L466 | Và nếu phải chọn những khoảnh khắc đáng nhớ nhất của đại hội, thì đó là: Koala ôm cây keo làm điều hòa. Chồn Gulo đi bộ 800km và trở thành con chồn đầu tiên ở Colorado sau 90 |  | Một cuốn album ảnh kỷ niệm hoạt hình mở ra: ảnh chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ ôm thân cây mát, ảnh chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh đứng trên đỉnh núi |
| b18 | 02:26.9–02:36.9 (10.0s) | L467 | năm. Chim Cánh Cụt đi theo mặt trời 13.000km. Gấu Nước bị bắn khỏi nòng súng khí và dám thừa nhận mình không bất tử. Và ông lão ngư dân Brazil đứng dưới nước, chờ tín hiệu của người bạn cá heo. |  | Trang album tiếp theo: ảnh chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ trên băng dưới hoàng hôn, ảnh chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương bò ra khỏi bao cát, ảnh người ngư dân Bra-xin và chú Cá Heo |
| b19 | 02:36.9–02:43.2 (6.3s) | L468 | Và bây giờ, đến lượt bạn làm giám khảo! Bạn đồng ý với kết quả này không? Nếu là bạn, bạn sẽ trao vương miện cho ai? |  | anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng chĩa micro vàng ra phía người xem, mỉm cười, phía sau là tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) với mười hình đầu tuyển thủ đang chờ bình chọn. |
| b20 | 02:43.2–02:49.2 (6.0s) | L469 | Hãy viết tên nhà vô địch của riêng bạn ở phần bình luận nhé. Biết đâu, ở đại hội lần sau, kết quả sẽ thay đổi hoàn toàn! |  | Mười tuyển thủ đứng dàn hàng ngang trên sân khấu vẫy tay chào khán giả, pháo giấy rơi, anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đứng giữa cúi chào. |
| b21 | 02:49.2–02:59.0 (9.8s) | L470 | Vì Đại Hội Sinh Tồn lần thứ hai đã có danh sách tuyển thủ. Mười gương mặt mới, đến từ khắp nơi trên thế giới: từ khu rừng tre ở Tứ Xuyên, đến dòng sông bùn ở châu Phi, đến những cánh rừng mưa Nam Mỹ. |  | Một cánh cửa đường hầm mới mở hé ánh sáng, bên trong là mười cái bóng đen mới: một con gấu tròn ôm cành tre, một con hà mã to lớn, một con lười treo ngược, và nhiều bóng khác; KHÔNG có anh MC trong cảnh này. |
| b22 | 02:59.0–03:06.3 (7.3s) | L471 | Và lần này, có một tuyển thủ mang theo cả một khẩu đại bác nước trên càng! Hẹn gặp lại toàn thể khán đài ở Đại Hội Sinh Tồn lần thứ hai! |  | Một chú tôm nhỏ có chiếc càng to quá khổ như khẩu súng đứng ở cửa đường hầm, phun một tia nước mạnh tạo bong bóng nổ "bụp" hoạt hình, anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đứng ngoài giật mình làm rơi micro. |

## 5. Phân cảnh Shorts — từng beat

Banner: **10 QUÁI KIỆT THI ĐẤU / AI LÊN NGÔI?!** · giọng 47.1s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Mười quái kiệt. Tám vòng thi. Một chiếc vương miện! |  |
| s02 | 00:02.9 | S02 | Lửng Mật, Tôm Tít, Gấu Nước được dự đoán sẽ thắng. Còn Thú Mỏ Vịt... tham gia cho |  |
| s03 | 00:07.2 | S03 | vui! Vòng một: Thú Mỏ Vịt bơi 5 tiếng trong nước 0°C mà thân nhiệt không hề | **0°C** · bơi 5 tiếng · R/640 · [0.5, 0.55] |
| s04 | 00:11.9 | S04 | tụt! Vòng hai: Chim Cánh Cụt đi 13.000km mỗi năm, theo mặt trời quanh Nam Cực! | **13.000 KM** · mỗi năm · L/620 · [0.5, 0.5] |
| s05 | 00:16.2 | S05 | Vòng sáu: Cá Heo bắt cá cùng ngư dân Brazil, giúp họ bắt được cá cao gấp 17 lần! |  |
| s06 | 00:20.5 | S06 | Vòng bảy: tin đồn gấu nước còn sống trên Mặt Trăng bị khoa học... bắn hạ bằng súng khí! |  |
| s07 | 00:24.6 | S07 | Lửng Mật thì sao? Lần đầu tiên trong đời... chịu thừa nhận mình chưa chắc đúng! |  |
| s08 | 00:28.6 | S08 | Chung kết: ai giúp ích cho loài người nhiều nhất? Sữa Thú Mỏ Vịt diệt khuẩn, nọc độc có thể thành thuốc chữa tiểu đường! |  |
| s09 | 00:35.2 | S09 | Và nhà vô địch là... con vật từng bị các nhà khoa học tưởng là đồ giả khâu ghép! |  |
| s10 | 00:40.1 | S10 | Bạn có đồng ý không? Xem trọn tám vòng thi trong video dài nhé, |  |
| s11 | 00:43.6 | S11 | vì ở đây chỉ có mười quái kiệt, tám vòng thi, và một chiếc vương miện! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một sân vận động khổng lồ chìm trong bóng tối... Mười chiếc bục thi đấu đứng im lặng giữa sân. Và ở chính giữa, một chiếc vương miện bé xíu đang lặng lẽ phát sáng.". Bố cục: Sân vận động hoạt hình khổng lồ chìm trong bóng tối ban đêm, mười chiếc bục thi đấu tròn xếp vòng cung giữa sân, chính giữa là một chiếc vương miện vàng bé xíu tỏa sáng trên bệ đá; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đêm nay, mười sinh vật kỳ dị nhất từng bước qua kênh Vẽ Chuyện Hoang Dã sẽ quay trở lại. Nhưng lần này, không phải để kể chuyện của riêng mình...". Bố cục: Mười chiếc bóng đen bí ẩn của các con vật (lửng, rái cá, cá heo, thú mỏ vịt, bồ nông, gấu nước tí hon, tôm tít, chồn, cánh cụt, koala) đứng ngược sáng ở cửa đường hầm sân vận động, khói mờ quanh chân; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "mà để thi đấu với nhau, trực tiếp, trên cùng một sân chơi!". Bố cục: Cận cảnh mười đôi mắt sáng lóe trong bóng tối của đường hầm, to nhỏ khác nhau, nhìn thẳng ra phía trước đầy quyết tâm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bật đèn! Chào mừng toàn thể khán đài đến với Đại Hội Sinh Tồn lần thứ nhất!". Bố cục: Đèn sân vận động bật sáng rực, pháo giấy nổ tung, anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đứng giữa sân giơ cao micro vàng, khán đài chật kín các loài thú nhỏ (thỏ, sóc, ếch, chim sẻ) vẫy cờ hò reo.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tôi là người dẫn chương trình đêm nay, và tôi xin hứa một điều: tất cả những gì bạn sắp nghe đều là chuyện chưa từng được kể trong mười tập phim lẻ.". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đặt tay lên ngực hứa hẹn, phía sau là mười tấm áp phích tập phim cũ treo trên tường bị đóng dấu "ĐÃ KỂ" bằng biểu tượng dấu tích (không chữ).
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hoàn toàn mới, có nguồn khoa học đàng hoàng, và... hơi điên rồ một chút!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng nháy mắt, tay kia giơ một chồng tạp chí khoa học dày cộp có hình kính hiển vi, vệ tinh và chim cánh cụt trên bìa (không chữ).
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Luật chơi rất đơn giản. Tám vòng thi, mỗi vòng một thử thách sinh tồn khác nhau.". Bố cục: tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) hiện tám ô biểu tượng xếp thành hai hàng: nhiệt kế, đôi giày chạy, cái bát và đôi đũa, con mắt, chiếc nôi em bé, hai bàn tay nắm nhau, chiếc kính lúp, trái tim đỏ.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chịu nóng và chịu lạnh. Chạy đường dài. Ăn uống. Giác quan. Nuôi con. Làm việc nhóm. Phúc khảo tin đồn. Và cuối cùng... ai giúp ích cho loài người nhiều nhất.". Bố cục: Tám ô biểu tượng lần lượt sáng lên như đèn sân khấu, ô cuối có trái tim đỏ phát sáng mạnh nhất; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng chỉ tay theo từng ô.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi vòng, giám khảo sẽ trao ba tấm huy chương. Vàng được 3 điểm, bạc được 2 điểm, đồng được 1 điểm. Ai nhiều điểm nhất sẽ đội vương miện!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ ngồi ở bàn giám khảo trên cao, trước mặt là ba chiếc huy chương vàng, bạc, đồng lấp lánh xếp thành hàng, bà giơ một cánh ra hiệu nghiêm túc.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giám khảo xin nhắc: không cắn, không đấm, không xịt mùi hôi vào đối thủ!". Bố cục: Cận cảnh bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ chỉnh kính, gõ búa gỗ xuống bàn, vẻ mặt nghiêm khắc.
```
</details>

<details><summary>L100</summary>

```text
HÌNH L100 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó đi về phía Nam. Băng qua núi đá! Băng qua đồng cỏ! Và băng qua cả đường cao tốc liên bang số 80, nơi xe tải chạy ầm ầm ngày đêm!". Bố cục: chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh chạy băng qua một đường cao tốc rộng, xe tải hoạt hình phanh kít hai bên, nó đã sang đến bên kia an toàn, bụi tung lên; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L101</summary>

```text
HÌNH L101 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hai tháng sau, các nhà nghiên cứu nhận được tín hiệu từ... bang Colorado. Chú chồn đã đi khoảng 800km!". Bố cục: Tấm bản đồ nước Mỹ hoạt hình với đường chấm đỏ kéo dài từ bang Uai-ô-minh xuống bang Cô-lô-ra-đô, có biểu tượng dấu chân chồn dọc đường; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L102</summary>

```text
HÌNH L102 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và đây là điều khiến cả nước Mỹ xôn xao: đó là con Chồn Gulo đầu tiên được ghi nhận ở bang Colorado kể từ năm 1919. 90 năm vắng bóng!". Bố cục: Một tờ báo hoạt hình bay phấp phới có ảnh lớn chụp chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh trên trang nhất (không chữ), xung quanh là đám đông người hoạt hình đang chỉ trỏ, đèn flash nháy; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L103</summary>

```text
HÌNH L103 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Có một nhiếp ảnh gia còn chụp được nó trong công viên quốc gia núi Rocky, khiến giới yêu thiên nhiên phát sốt.". Bố cục: chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh đứng trên mỏm đá giữa núi Rốc-ky, quay đầu nhìn thẳng vào ống kính máy ảnh của một nhiếp ảnh gia hoạt hình đang nấp sau tảng đá; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L104</summary>

```text
HÌNH L104 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chuyện vui hơn nữa. Ở nước Mỹ, bang Michigan có biệt danh là "bang Chồn Gulo". Đội thể thao của trường đại học lớn nhất bang cũng tên là Chồn Gulo.". Bố cục: Một sân bóng bầu dục hoạt hình, đám cổ động viên mặc áo có hình đầu chồn, giơ cao lá cờ hình chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L105</summary>

```text
HÌNH L105 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thế nhưng suốt 200 năm, chưa hề có ai chứng minh được Chồn Gulo thật sự sống ở Michigan!". Bố cục: Một nhà khoa học hoạt hình cầm kính lúp lục tung một kho lưu trữ đầy hồ sơ bụi bặm, mồ hôi nhễ nhại, xung quanh chỉ toàn ảnh cổ động viên mặc đồ chồn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L106</summary>

```text
HÌNH L106 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cho đến đầu năm 2004, một nhóm thợ săn đang đuổi theo dấu chân lạ thì thấy một con vật leo tót lên cây. Nhà sinh vật học được gọi đến, chụp ảnh, xác nhận: đó là một con Chồn Gulo thật!". Bố cục: Một cái cây trơ cành giữa cánh đồng tuyết, trên ngọn là chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh đang ôm cành nhìn xuống, dưới gốc là một nhà sinh vật học hoạt hình giơ máy ảnh chụp lia lịa với vẻ mặt sung sướng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L107</summary>

```text
HÌNH L107 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bang Chồn Gulo cuối cùng cũng có một con Chồn Gulo thật, sau 200 năm chờ đợi. Như đội bóng đá cuối cùng cũng tìm được... linh vật thật của mình!". Bố cục: chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh đứng trên bục danh dự, được cổ động viên hoạt hình choàng khăn và đội mũ của đội bóng, vẻ mặt bối rối không hiểu chuyện gì; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L108</summary>

```text
HÌNH L108 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng cả Lửng Mật lẫn Chồn Gulo đều phải ngả mũ trước tuyển thủ tiếp theo. Một chú chim cao chưa tới 70cm. Không biết bay. Và đi bộ thì... lạch bạch.". Bố cục: chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ đứng ở vạch xuất phát, chỉnh lại nơ bướm, bên cạnh là chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần và chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh đang khoanh tay cười khẩy coi thường; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L109</summary>

```text
HÌNH L109 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà khoa học đã gắn những thiết bị định vị nhỏ xíu lên những chú Chim Cánh Cụt Adélie ở đảo Rốt, vùng cực Nam của Trái Đất, và theo dõi chúng suốt mùa đông.". Bố cục: Một nhà khoa học mặc áo khoác đỏ dày cộm giữa vùng băng, cẩn thận gắn thiết bị nhỏ như chiếc đồng hồ vào chân chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ, phía sau là đàn cánh cụt tò mò xếp hàng xem; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nghe rõ chưa, toàn thể tuyển thủ? Đặc biệt là... một vài cá nhân có tiền sử hơi nóng tính!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng liếc mắt nhìn sang chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần, chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh và chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh đang đứng giả vờ huýt sáo ngây thơ, sau lưng giấu nắm đấm.
```
</details>

<details><summary>L110</summary>

```text
HÌNH L110 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kết quả: mỗi năm, những chú chim này di chuyển trung bình khoảng 13.000km! Chuyến dài nhất được ghi nhận lên tới 17.600km!". Bố cục: Bản đồ Nam Cực hoạt hình với một vòng đường chấm đỏ cực lớn uốn quanh biển băng, chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ đứng ở điểm cuối giơ cánh chiến thắng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L111</summary>

```text
HÌNH L111 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Để dễ hình dung: quãng đường đó dài hơn đi từ Hà Nội sang tận nước Mỹ! Bằng đôi chân ngắn củn và cái bụng làm ván trượt!". Bố cục: Quả địa cầu hoạt hình có một đường cong nối từ Việt Nam sang tận nước Mỹ, trên đường vẽ chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ vừa đi lạch bạch vừa nằm sấp trượt bụng trên băng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L112</summary>

```text
HÌNH L112 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vì sao phải đi xa đến thế? Vì mùa đông ở Nam Cực, mặt trời biến mất hoàn toàn. Không có ánh sáng, chim cánh cụt không nhìn thấy để săn mồi.". Bố cục: Bầu trời Nam Cực tối đen như mực, chỉ có vài ngôi sao, chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ đứng một mình trên tảng băng nhìn xung quanh lo lắng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L113</summary>

```text
HÌNH L113 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thế là chúng đi theo mặt trời. Cả đàn trôi trên những tảng băng, đi dần về phía Bắc, đến những nơi mỗi ngày còn vài tiếng chạng vạng, đủ sáng để bắt cá.". Bố cục: Một đàn chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ đứng trên những tảng băng trôi như những chiếc bè, cùng hướng về phía chân trời nơi có ánh hoàng hôn cam hồng le lói; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L114</summary>

```text
HÌNH L114 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đến mùa xuân, chúng lại hối hả quay về đúng bãi đá cũ để làm tổ. Một chú chim không biết bay, đi theo mặt trời, mỗi năm một vòng lớn quanh đáy Trái Đất.". Bố cục: chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ đứng trên bãi sỏi quen thuộc nhìn lên mặt trời mùa xuân rực rỡ, bên cạnh là tổ sỏi cũ, ánh sáng ấm áp chiếu xuống; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L115</summary>

```text
HÌNH L115 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mà khoan, khán giả có biết vì sao loài chim này tên là Adélie không? Năm 1840, nhà thám hiểm người Pháp Dumont d'Urville đặt tên cho một vùng đất ở Nam Cực theo tên vợ mình, bà Adèle.". Bố cục: Một con tàu buồm cổ hoạt hình giữa biển băng, trên boong là nhà thám hiểm râu quai nón giơ tay chỉ về phía bờ biển trắng, tay kia cầm tấm ảnh chân dung người vợ trong khung tròn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L116</summary>

```text
HÌNH L116 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và loài chim cánh cụt sống ở đó được đặt theo tên vùng đất. Vậy là Quý ông Vest Đuôi Tôm thật ra... mang tên của một quý bà!". Bố cục: chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ nhìn vào gương thấy ảnh phản chiếu đeo nơ đỏ và đội thêm một chiếc mũ quý bà có lông chim, vẻ mặt ngớ ngẩn bất ngờ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L117</summary>

```text
HÌNH L117 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong khi đó, ở đường đua dưới nước, một tuyển thủ bị sóng đánh dạt lên bãi cát. Tôm Tít mắc cạn! Chân ngắn, không đi được trên cạn. Các đối thủ đã nghĩ: thế là xong.". Bố cục: chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh nằm ngửa trên bãi cát ướt, sóng vừa rút đi, các chân nhỏ quơ quào trong không khí, mặt hoảng hốt; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L118</summary>

```text
HÌNH L118 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng ở bờ biển Panama, có một loài tôm tít nhỏ tí xíu có cách thoát thân độc nhất vô nhị.". Bố cục: Bãi biển nhiệt đới hoạt hình có cây dừa, một chú tôm tít nhỏ thân dài mảnh nằm trên cát, đang co mình chuẩn bị làm gì đó; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L119</summary>

```text
HÌNH L119 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó nằm ngửa, cong người lại thành một vòng tròn... rồi lộn nhào ra phía sau! Một vòng! Hai vòng! Rồi hàng chục vòng liên tục, có khi tới 40 vòng không nghỉ!". Bố cục: Chuỗi hình ảnh nhiều tư thế liên tiếp của chú tôm tít đang lộn nhào thành bánh xe trên cát, để lại vệt cát hình vòng tròn, các nét gió tốc độ phía sau; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và bây giờ, xin mời các tuyển thủ bước ra sân!". Bố cục: Cửa đường hầm mở toang, ánh đèn sân khấu chiếu thẳng vào lối đi trải thảm đỏ, khói trắng phun hai bên; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L120</summary>

```text
HÌNH L120 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "72 vòng mỗi phút, lăn được tới 2 mét để quay về biển! Các nhà khoa học công bố trên tạp chí Nature với tựa đề: Di chuyển như một cái bánh xe?". Bố cục: Một chiếc đồng hồ đếm vòng hoạt hình chạy số liên tục bên cạnh vệt lăn trên cát dẫn thẳng xuống mép nước, chú tôm tít lăn tõm xuống biển; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L121</summary>

```text
HÌNH L121 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Loài người mất hàng ngàn năm mới phát minh ra cái bánh xe. Còn tôm tít... tự biến mình thành bánh xe!". Bố cục: Một người tiền sử hoạt hình đang hì hục đục chiếc bánh xe đá, mồ hôi nhễ nhại, quay sang nhìn thấy chú tôm tít lăn vèo qua mặt thì há hốc mồm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L122</summary>

```text
HÌNH L122 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cuối cùng, Chim Bồ Nông bước vào đường đua... và không chạy. Nó dang cánh, lấy đà, và bay lên. Ban giám khảo cho phép, vì đây là cách di chuyển của nó.". Bố cục: chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn dang đôi cánh rộng lớn chạy lấy đà trên mặt nước rồi cất cánh bay lên trời xanh, bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ giơ biển hiệu dấu tích xanh cho phép.
```
</details>

<details><summary>L123</summary>

```text
HÌNH L123 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bồ Nông rất ít khi đập cánh liên tục. Nó tìm những luồng khí nóng bốc lên từ mặt đất, rồi xoay vòng tròn để được nâng lên cao, như ngồi thang máy miễn phí.". Bố cục: chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn bay vòng tròn trong một cột không khí nóng vẽ bằng những mũi tên xoắn ốc màu cam đi lên, phía dưới là mặt đất nắng nóng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L124</summary>

```text
HÌNH L124 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bồ Nông Úc từng được ghi nhận bay ở độ cao hàng ngàn mét, cao đến mức người dưới đất không còn nhìn thấy, rồi lượn đi hàng chục cây số mà gần như không tốn sức.". Bố cục: Một đàn chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn nhỏ li ti bay trên tầng mây cao, bên dưới là mặt đất xa tít tắp, một người hoạt hình dưới đất cầm ống nhòm tìm mãi không thấy; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L125</summary>

```text
HÌNH L125 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và đây là bí ẩn lớn nhất của vòng thi. Giữa nước Úc có một hồ nước mặn khổng lồ tên là hồ Eyre. Phần lớn thời gian, hồ khô cạn, chỉ còn lớp muối trắng xóa.". Bố cục: Một hồ muối khô cạn trắng xóa mênh mông dưới nắng sa mạc, nứt nẻ thành những ô lục giác, chân trời rung rinh hơi nóng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L126</summary>

```text
HÌNH L126 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng cứ vài năm, mưa lớn ở tận phía Bắc lại đổ nước về hồ. Và chỉ ít lâu sau, hàng chục ngàn con Bồ Nông từ khắp nước Úc bỗng nhiên... bay đến, dù cách xa cả ngàn cây số.". Bố cục: Hồ Ây-rơ đầy nước xanh lấp lánh, trên trời hàng trăm con chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn từ mọi hướng đang bay tới, hạ cánh xuống mặt nước; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L127</summary>

```text
HÌNH L127 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Năm 1989, các nhà khoa học ước tính đã có khoảng 100.000 chú Bồ Nông con ra đời trên hồ này. Một trận bùng nổ dân số giữa sa mạc!". Bố cục: Một hòn đảo giữa hồ chật kín tổ, hàng trăm chú bồ nông con lông xám há mỏ chờ mẹ cho ăn, bồ nông bố mẹ bay ra bay vào tấp nập; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L128</summary>

```text
HÌNH L128 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Câu hỏi: làm sao Bồ Nông biết hồ có nước, khi nó cách xa cả ngàn cây số? Câu trả lời của khoa học hiện nay là: chưa ai biết chắc.". Bố cục: chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn đứng giữa vũng nước, trên đầu là dấu chấm hỏi khổng lồ, xung quanh là các nhà khoa học hoạt hình gãi đầu, mỗi người cầm một tấm bảng có biểu tượng khác nhau (mũi, tai, la bàn, ống nhòm); KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L129</summary>

```text
HÌNH L129 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Có giả thuyết cho rằng chúng ngửi được, có giả thuyết cho rằng chúng nghe được sóng âm từ xa, có giả thuyết cho rằng có những con bồ nông già đi do thám trước rồi về... rủ cả nhóm!". Bố cục: Một con chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn già đeo kính lão, đội mũ thám tử, bay về báo tin cho đàn bồ nông đang đứng chờ, cả đàn hào hứng vỗ cánh chuẩn bị xuất phát; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyển thủ số một! Nặng chưa tới 12kg! Từng nhai rắn hổ mang như nhai bim bim! Lửng Mật!". Bố cục: chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần bước ra thảm đỏ, đeo kính râm, vung tay chào khán đài đầy ngông nghênh, đèn flash nháy khắp nơi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L130</summary>

```text
HÌNH L130 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tổng kết đường đua: một gã đào hố 14km mỗi đêm, một chú chồn băng qua cả đường cao tốc, một chú chim không biết bay đi vòng quanh Nam Cực, một chú tôm tự biến thành bánh xe, và một chú bồ nông đi tìm hồ nước bằng một giác quan mà khoa học còn chưa gọi được tên.". Bố cục: Năm khung ảnh nhỏ hoạt hình xếp thành dải phim: chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần đào hố, chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh băng qua đường cao tốc, chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ đi trên băng, chú tôm tít lộn bánh xe, chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn bay trên hồ muối; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cầm cuộn phim giơ lên.
```
</details>

<details><summary>L131</summary>

```text
HÌNH L131 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giám khảo xin tuyên bố kết quả vòng hai. Đây là vòng thi khó chấm nhất từ trước đến nay.". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ bối rối nhìn chiếc thước dây cuộn dài tràn ra khắp sàn nhà, quấn cả vào chân bàn giám khảo.
```
</details>

<details><summary>L132</summary>

```text
HÌNH L132 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Huy chương đồng: Tôm Tít, nhà phát minh ra bánh xe sống! Huy chương bạc: Chồn Gulo, 800km và một tấm ảnh lên trang nhất!". Bố cục: Bục trao giải: chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh đứng bậc đồng trong bể nước nhỏ đeo huy chương đồng, chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh đứng bậc bạc đeo huy chương bạc thứ hai lấp lánh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L133</summary>

```text
HÌNH L133 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và huy chương vàng: Chim Cánh Cụt, 13.000km mỗi năm, đi theo mặt trời quanh đáy Trái Đất!". Bố cục: chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ đứng trên bậc vàng, đeo huy chương vàng, chỉnh nơ bướm đầy tự hào, mặt trời nhỏ hoạt hình mỉm cười chiếu sáng phía sau; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L134</summary>

```text
HÌNH L134 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bảng điểm sau hai vòng: Chồn Gulo vươn lên dẫn đầu với 4 điểm! Thú Mỏ Vịt và Chim Cánh Cụt cùng 3 điểm. Koala và Tôm Tít mỗi bạn 1 điểm. Còn Lửng Mật... vẫn chưa có điểm nào!". Bố cục: tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) sáng lên: cột chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh cao nhất, cột chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá và chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ bằng nhau, cột chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ và chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh thấp; bên dưới chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần nghiến răng nhìn cột điểm trống trơn của mình; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L135</summary>

```text
HÌNH L135 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ủa... đi bộ xa vậy có được ăn gì không ạ? Cháu đói rồi.". Bố cục: chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ ngồi bệt dưới chân bảng điểm, xoa bụng, ánh mắt thèm thuồng nhìn về phía khu ẩm thực; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L136</summary>

```text
HÌNH L136 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Câu hỏi hay lắm, tuyển thủ Koala! Vì vòng ba chính là... vòng ăn uống!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cười tươi chỉ tay về phía một khu bếp khổng lồ có lò nướng, chảo, bát đĩa và thực đơn treo tường (chỉ có hình vẽ món ăn), hơi nóng bốc lên thơm phức.
```
</details>

<details><summary>L137</summary>

```text
HÌNH L137 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vòng ba: bếp trưởng hoang dã! Mỗi tuyển thủ phải trình bày cách mình kiếm ăn trước ban giám khảo. Điểm cộng cho sự khéo léo, cho sự sáng tạo, và cho... độ khó tin!". Bố cục: Một khu bếp ngoài trời hoạt hình cực lớn, mỗi tuyển thủ có một quầy bếp riêng có biển hiệu hình con vật (không chữ), bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ đeo mũ đầu bếp trắng cao, cầm chiếc thìa nếm thử.
```
</details>

<details><summary>L138</summary>

```text
HÌNH L138 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mở màn là Thú Mỏ Vịt, nhà vô địch vòng một. Và bí mật đầu tiên của Thú Mỏ Vịt là: nó ăn khỏe đến mức khó tin.". Bố cục: chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá đeo tạp dề, đứng trước quầy bếp chất cao như núi những con tôm, ấu trùng và giun nhỏ hoạt hình, vẻ mặt sẵn sàng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L139</summary>

```text
HÌNH L139 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một con Thú Mỏ Vịt trưởng thành ăn mỗi ngày lượng thức ăn bằng khoảng một phần năm trọng lượng cơ thể. Nhưng một Thú Mỏ Vịt mẹ đang nuôi con còn ăn khủng khiếp hơn nhiều!". Bố cục: Một chiếc cân đĩa hoạt hình: đĩa bên trái là chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá, đĩa bên phải là một đống thức ăn nhỏ bằng một phần năm; bên cạnh là chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá mẹ đeo nơ hồng cạnh một đống thức ăn to bằng chính nó; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyển thủ số hai! Võ sĩ có cú đấm nhanh nhất đại dương! Tôm Tít!". Bố cục: chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh được đẩy ra trong một bể nước tròn có bánh xe, giơ hai càng búa như võ sĩ quyền anh khoe găng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L140</summary>

```text
HÌNH L140 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Có những tài liệu ghi nhận Thú Mỏ Vịt mẹ đang cho con bú có thể ăn gần bằng cả cân nặng của chính mình mỗi ngày.". Bố cục: chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá mẹ ngồi trước một đống thức ăn cao bằng người nó, má phồng to, ăn liên tục không ngừng, trên đầu có chiếc đồng hồ chạy vèo vèo; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L141</summary>

```text
HÌNH L141 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tức là nếu một người mẹ nặng 50kg ăn theo kiểu này, mỗi ngày phải ăn... 50kg cơm!". Bố cục: Một bà mẹ hoạt hình ngồi trước một nồi cơm khổng lồ cao hơn cả người, cầm đôi đũa ngơ ngác, xung quanh là chồng bát đĩa cao ngất; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L142</summary>

```text
HÌNH L142 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mà ăn khỏe như vậy là có lý do. Thú Mỏ Vịt mẹ không có núm vú, sữa tiết ra qua da bụng, nên con non phải liếm. Và chính sữa ấy đã làm các nhà khoa học bất ngờ vào năm 2018.". Bố cục: Phòng thí nghiệm hoạt hình hiện đại: một nhà khoa học nữ đeo kính bảo hộ nhỏ giọt sữa trắng vào đĩa petri, bên cạnh là ảnh chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá dán trên tường; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L143</summary>

```text
HÌNH L143 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà khoa học ở Úc đã tách ra từ sữa Thú Mỏ Vịt một loại đạm có khả năng diệt vi khuẩn. Và khi nhìn hình dạng ba chiều của nó, họ thấy một cấu trúc chưa từng gặp bao giờ.". Bố cục: Một mô hình phân tử ba chiều hoạt hình xoắn quăn như những lọn tóc lò xo màu xanh tím lơ lửng trên bàn thí nghiệm, phát sáng nhẹ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L144</summary>

```text
HÌNH L144 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Phân tử ấy xoăn tít như những lọn tóc lò xo, nên các nhà khoa học đặt tên cho kiểu cấu trúc này theo tên một ngôi sao nhí tóc xoăn nổi tiếng của Hollywood: Shirley Temple!". Bố cục: Bên cạnh mô hình phân tử xoăn tít là một bé gái hoạt hình tóc vàng xoăn lò xo nhún nhảy, hai mái tóc trông giống hệt mô hình phân tử; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L145</summary>

```text
HÌNH L145 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vì sao sữa Thú Mỏ Vịt cần chất diệt khuẩn mạnh như vậy? Vì sữa chảy ra ngoài da, dính đầy bụi bẩn và vi khuẩn, mà con non lại liếm trực tiếp. Không có lớp bảo vệ này, con non dễ bị nhiễm khuẩn.". Bố cục: Hình phóng to da bụng chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá mẹ có giọt sữa trắng, xung quanh là những con vi khuẩn hoạt hình mặt xấu xa đang tiến lại gần thì bị những lọn xoăn tím của đạm sữa quất bay; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L146</summary>

```text
HÌNH L146 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ngày nay, các nhà khoa học hy vọng loại đạm này có thể giúp tìm ra cách mới chống lại những loại vi khuẩn kháng thuốc. Từ một con vật từng bị tưởng là đồ giả khâu ghép!". Bố cục: Một chai thuốc hoạt hình có hình chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá trên nhãn (không chữ), xung quanh là những vi khuẩn mặc áo giáp kháng thuốc đang hoảng sợ bỏ chạy; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L147</summary>

```text
HÌNH L147 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giám khảo ghi nhận: món ăn chưa ngon, nhưng sữa thì... có thể cứu người. Rất ấn tượng.". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ cầm chiếc thìa, gật gù ghi chép, bên cạnh có một chiếc huy hiệu nhỏ hình chữ thập y tế màu xanh.
```
</details>

<details><summary>L148</summary>

```text
HÌNH L148 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Quầy bếp tiếp theo: Rái Cá Biển. Và Rái Cá mang theo một dụng cụ nấu ăn rất đặc biệt: một hòn đá.". Bố cục: chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách nằm ngửa trên mặt nước cạnh quầy bếp, giơ hòn đá xám lên như đầu bếp khoe con dao gia truyền, trên bụng là một con trai to; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L149</summary>

```text
HÌNH L149 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Năm 2024, các nhà khoa học công bố một nghiên cứu theo dõi 196 con Rái Cá Biển ở bang California, nước Mỹ, trong nhiều năm. Họ muốn biết: dùng công cụ thì được lợi gì?". Bố cục: Hàng chục chú chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách hoạt hình nhỏ đeo vòng định vị nằm ngửa trên mặt biển, một nhà khoa học trên thuyền cầm sổ ghi chép và ống nhòm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyển thủ số ba! Kẻ bất tử tí hon! Gấu Nước! Ban tổ chức phải phát kính lúp cho khán giả mới nhìn thấy cậu ấy!". Bố cục: Khán giả trên khán đài đồng loạt cầm kính lúp to soi xuống sân, trong vòng tròn kính lúp là chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương đang vẫy tay chào; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L150</summary>

```text
HÌNH L150 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Câu trả lời: những con dùng đá đập vỏ thì răng ít bị mẻ hơn hẳn những con chỉ dùng răng cắn. Và răng mà hỏng thì Rái Cá không ăn được, nghĩa là không sống nổi!". Bố cục: Hai bộ răng hoạt hình so sánh: bộ răng bên trái mẻ sứt nhiều chỗ (rái cá cắn vỏ), bộ răng bên phải trắng sáng lấp lánh (rái cá dùng đá); KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L151</summary>

```text
HÌNH L151 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Điều thú vị: rái cá cái dùng đá nhiều hơn rái cá đực. Nhờ hòn đá, những con cái nhỏ con hơn vẫn ăn được những con mồi vỏ cứng hơn gần gấp 3 lần so với những con không dùng công cụ.". Bố cục: chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách cái nhỏ con đập hòn đá xuống một con ốc vỏ cứng trên bụng, vỏ ốc vỡ toác; bên cạnh là một con rái cá đực to xác đang cắn vỏ đến méo cả mồm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L152</summary>

```text
HÌNH L152 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bài học từ bếp Rái Cá: nếu bạn bóc được vỏ cua bằng dụng cụ, đừng bao giờ dùng răng! Nha sĩ của kênh Vẽ Chuyện Hoang Dã xin cảm ơn.". Bố cục: Một nha sĩ hoạt hình mặc áo blouse trắng giơ ngón cái tán thưởng, cầm chiếc gương nha khoa, bên cạnh là chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách cười khoe hàm răng trắng bóng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L153</summary>

```text
HÌNH L153 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Quầy bếp số ba: Cá Heo. Và Cá Heo không nấu ăn. Cá Heo... chơi thể thao với đồ ăn!". Bố cục: chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái nhô lên khỏi mặt nước, đội mũ đầu bếp lệch, nháy mắt tinh nghịch với ban giám khảo; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L154</summary>

```text
HÌNH L154 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ở vùng biển Florida nước Mỹ, người ta quay được cảnh Cá Heo dùng chiếc đuôi quất mạnh vào con cá, khiến con cá bay vút lên không trung như một quả bóng bị sút!". Bố cục: chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái quẫy mạnh chiếc đuôi, một con cá đối bay vèo lên trời theo đường cong parabol, các nét vẽ tốc độ phía sau; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L155</summary>

```text
HÌNH L155 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Con cá rơi xuống, choáng váng, và Cá Heo chỉ việc bơi tới ăn. Các nhà khoa học gọi đây là kỹ thuật "đá cá", và nó được học từ bố mẹ sang con cái.". Bố cục: Con cá đối choáng váng nằm trên mặt nước, mắt xoay vòng, chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái con đang chăm chú nhìn chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái mẹ biểu diễn mẫu như một buổi học; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L156</summary>

```text
HÌNH L156 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng màn trình diễn đỉnh cao nhất của Cá Heo không phải đá cá. Mà là... làm việc cùng con người. Và nó diễn ra ở một thị trấn nhỏ của nước Brazil.". Bố cục: Một thị trấn ven biển hoạt hình của Bra-xin có những ngôi nhà nhiều màu sắc, một con kênh rộng nối ra biển, những người đánh cá đứng chờ ven bờ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L157</summary>

```text
HÌNH L157 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Câu chuyện này sẽ được kể đầy đủ ở vòng sáu. Giờ thì xin mời thí sinh tiếp theo vào bếp. Thí sinh này có chiếc nồi lớn nhất cuộc thi!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng giơ tay ra hiệu "khoan đã" với chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái, rồi quay sang chỉ về phía một cái bóng đen khổng lồ có chiếc mỏ dài đang bước vào bếp.
```
</details>

<details><summary>L158</summary>

```text
HÌNH L158 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chim Bồ Nông! Và chiếc nồi chính là... cái mỏ của nó. Nhưng hôm nay, Bồ Nông không khoe cái mỏ. Nó muốn khoe một chiến thuật săn mồi bằng... cả đội.". Bố cục: chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn dắt theo năm con bồ nông khác, cả nhóm mặc đồng phục giống nhau như một đội bóng, xếp hàng ngang đứng trước quầy bếp; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L159</summary>

```text
HÌNH L159 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đầu tiên, các bạn đã biết bồ nông bay theo hình chữ V. Nhưng chỉ đến năm 2001, các nhà khoa học mới đo được lợi ích thật sự của đội hình này.". Bố cục: Một đàn chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn bay thành hình chữ V gọn gàng trên bầu trời xanh, phía dưới là một chiếc thuyền máy chở các nhà khoa học đang ngước nhìn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyển thủ số bốn! Gã liều mạng xứ tuyết! Chồn Gulo!". Bố cục: chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh bước ra, lông dựng đứng, nhe răng cười, tuyết rơi lất phất quanh người; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L160</summary>

```text
HÌNH L160 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Họ huấn luyện những con bồ nông trắng bay theo một chiếc thuyền máy và một chiếc máy bay siêu nhẹ, rồi gắn máy đo nhịp tim lên lưng chúng.". Bố cục: Một chiếc máy bay siêu nhẹ hoạt hình bay là là trên sông, phía sau là đàn chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn bay theo, mỗi con đeo một chiếc máy đo nhỏ trên lưng có hình trái tim đập; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L161</summary>

```text
HÌNH L161 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kết quả: khi bay theo đội hình, nhịp tim của bồ nông thấp hơn khoảng 11 đến 14% so với khi bay một mình. Bay cùng nhau thì đỡ mệt hơn hẳn!". Bố cục: Hai màn hình nhịp tim hoạt hình so sánh: màn hình bồ nông bay một mình có đường nhịp tim dày đặc gấp gáp, màn hình bồ nông bay đội hình có đường nhịp tim thưa thớt thư thái; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L162</summary>

```text
HÌNH L162 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bí quyết là con bay sau lướt trên luồng khí bốc lên từ đầu cánh con bay trước, như người đạp xe nép sau lưng người khác để đỡ gió.". Bố cục: Sơ đồ hoạt hình hai con chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn bay nối đuôi, từ đầu cánh con trước tỏa ra những xoáy khí xoắn ốc màu xanh nhạt nâng cánh con sau lên; bên cạnh là hình hai người đạp xe nép sau nhau; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L163</summary>

```text
HÌNH L163 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và con bồ nông bay đầu đàn thì sao? Nó vất vả nhất. Nhưng đừng lo, các thành viên trong đàn thường thay phiên nhau dẫn đầu. Rất công bằng, rất dân chủ.". Bố cục: Con chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn bay đầu đàn thở hổn hển mồ hôi nhễ nhại, quay đầu ra hiệu, một con khác bay lên thay thế, hai bên đập cánh chào nhau như đổi ca trực; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L164</summary>

```text
HÌNH L164 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Quầy bếp tiếp theo... trống trơn. Tuyển thủ Lửng Mật đã biến mất. Và ở góc sân, có tiếng đào đất loạt soạt.". Bố cục: Một quầy bếp bỏ trống chỉ còn chiếc tạp dề treo lủng lẳng, ở góc sân có một đống đất mới đào và những vụn đất bắn tung lên; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L165</summary>

```text
HÌNH L165 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lửng Mật tên tiếng Anh là "lửng mật ong". Ai cũng nghĩ món khoái khẩu của nó là mật ong. Nhưng các nhà khoa học ở Kalahari đã ngồi đếm từng miếng nó ăn suốt nhiều năm.". Bố cục: chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần thò đầu ra khỏi hố đất, miệng ngậm một chiếc thìa mật ong, phía sau một nhà khoa học hoạt hình cầm sổ ghi chép và máy đếm bấm tay; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L166</summary>

```text
HÌNH L166 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và họ phát hiện ra: thứ Lửng Mật đào được nhiều nhất là chuột, thằn lằn, bọ cạp, và một món đặc biệt: những ấu trùng của một loài ong sống đơn độc dưới cát.". Bố cục: Mặt cắt lòng đất cát hoạt hình: những khoang nhỏ chứa ấu trùng ong màu trắng nằm sâu trong cát, phía trên chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần đang đào xuống thẳng tới chỗ đó; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L167</summary>

```text
HÌNH L167 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "4 con Lửng Mật đực đã được quan sát đào ấu trùng ong suốt hơn 50 tiếng, và ăn tổng cộng khoảng 2.800 con ấu trùng. Những con ấu trùng ấy nằm sâu tới 50 đến 70cm dưới cát!". Bố cục: Bốn chú chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần chui sâu dưới cát chỉ thò đuôi lên, xung quanh là những ấu trùng ong trắng nhỏ, một chiếc thước dây cắm thẳng xuống cát đo chiều sâu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L168</summary>

```text
HÌNH L168 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vậy còn câu chuyện nổi tiếng về loài chim dẫn mật dẫn đường cho Lửng Mật tới tổ ong, rồi hai bên chia nhau chiến lợi phẩm? Đây là lúc ban giám khảo... phải nói thật.". Bố cục: Một cuốn truyện tranh hoạt hình mở ra, trang sách vẽ một con chim nhỏ màu nâu dẫn đường cho chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần đi về phía tổ ong trên cây, xung quanh có những ngôi sao lấp lánh như truyện cổ tích; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L169</summary>

```text
HÌNH L169 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Năm 1990, ba nhà điểu học công bố một bài báo, viết rằng: hơn 200 năm nghiên cứu ở châu Phi, không có nhà khoa học nào tận mắt thấy chim dẫn mật dẫn đường cho Lửng Mật cả.". Bố cục: Ba nhà điểu học hoạt hình đeo kính ngồi quanh bàn, chỉ vào một tấm bản đồ châu Phi có dấu chấm hỏi to, trước mặt là chồng tài liệu cũ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyển thủ số năm, quý ông mặc vest của Nam Cực, Chim Cánh Cụt! Số sáu, Rái Cá Biển! Số bảy, Cá Heo!". Bố cục: Ba tuyển thủ cùng ra: chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ đi lạch bạch chỉnh nơ, chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách nằm ngửa trên chiếc phao, chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái nhô lên từ bể nước có bánh xe cười tươi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L170</summary>

```text
HÌNH L170 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thậm chí có một bộ phim tài liệu cũ quay cảnh này, và sau này người làm phim kể lại: đó là một con lửng đã được thuần hóa, đi theo một con chim nhồi bông treo trên dây câu!". Bố cục: Hậu trường quay phim hoạt hình: một người cầm cần câu treo con chim nhồi bông lủng lẳng, chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần đeo vòng cổ ngoan ngoãn đi theo, đạo diễn cầm loa ra hiệu "cắt"; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L171</summary>

```text
HÌNH L171 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một nghiên cứu năm 2023 đã phỏng vấn gần 400 thợ săn mật ong ở 9 nước châu Phi. Phần lớn họ không tin hai loài này hợp tác.". Bố cục: Một nhóm thợ săn mật ong hoạt hình ngồi quanh đống lửa, có người lắc đầu, có người khoanh tay nghi ngờ, một nhà nghiên cứu cầm sổ ghi chép; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L172</summary>

```text
HÌNH L172 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng ở một vài cộng đồng ở Tanzania, có những người kể rằng họ từng thấy. Nên kết luận cuối cùng của khoa học hiện nay là: có thể có, nhưng rất hiếm, và chưa ai quay được một bằng chứng rõ ràng.". Bố cục: Một tấm ảnh mờ nhòe như ảnh người tuyết bí ẩn, chỉ thấy lờ mờ một con chim và một con lửng, có kính lúp to đặt bên cạnh và dấu chấm hỏi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L173</summary>

```text
HÌNH L173 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giám khảo kết luận: Lửng Mật được điểm cao vì đào giỏi, nhưng bị trừ điểm vì... nổi tiếng nhờ một câu chuyện chưa được kiểm chứng!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gõ búa, giơ một tấm thẻ hình chiếc kính lúp; chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần đứng trước bàn giám khảo khoanh tay hậm hực.
```
</details>

<details><summary>L174</summary>

```text
HÌNH L174 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kết quả vòng ba! Huy chương đồng: Rái Cá Biển, đầu bếp có hòn đá bảo vệ hàm răng! Huy chương bạc: Chim Bồ Nông, đội bay tiết kiệm sức nhất bầu trời!". Bố cục: Bục trao giải: chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách đứng bậc đồng ôm hòn đá đeo huy chương đồng, chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn đứng bậc bạc dang cánh đeo huy chương bạc; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L175</summary>

```text
HÌNH L175 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và huy chương vàng vòng ba: Thú Mỏ Vịt! Ăn khỏe nhất cuộc thi, và có dòng sữa có thể giúp con người chống lại vi khuẩn kháng thuốc!". Bố cục: chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá đứng trên bậc vàng, giờ đã đeo hai chiếc huy chương vàng, băng đô xanh, nhảy cẫng lên sung sướng, pháo giấy rơi khắp nơi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L176</summary>

```text
HÌNH L176 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bảng điểm sau ba vòng: Thú Mỏ Vịt vươn lên dẫn đầu với 6 điểm! Chồn Gulo 4 điểm. Chim Cánh Cụt 3 điểm. Chim Bồ Nông 2 điểm. Koala, Tôm Tít và Rái Cá mỗi bạn 1 điểm.". Bố cục: tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) sáng lên: cột chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá vọt lên cao nhất, cột chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh thứ hai, cột chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ thứ ba, các cột khác thấp hơn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L177</summary>

```text
HÌNH L177 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn Lửng Mật, ứng cử viên nặng ký nhất trước giải, vẫn chưa có điểm nào. Và Cá Heo, Gấu Nước cũng vậy.". Bố cục: chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần, chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái và một hộp kính lúp đựng chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương đứng cạnh nhau trước bảng điểm, cả ba nhìn lên ba cột điểm tắt ngúm của mình; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L178</summary>

```text
HÌNH L178 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng đừng vội loại họ. Đại hội mới đi được ba trên tám chặng đường. Và vòng bốn sẽ thử thách thứ mà cơ bắp không thể thay thế: các giác quan!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cầm một chiếc kính lúp khổng lồ soi vào mắt mình, mắt to phóng đại trông rất hài, tay kia đặt sau tai như đang lắng nghe.
```
</details>

<details><summary>L179</summary>

```text
HÌNH L179 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giờ giải lao! Sau ba vòng thi căng thẳng, các tuyển thủ được mời vào căng tin của đại hội. Và ngay tại đây, chúng ta phát hiện ra mỗi người có một kiểu ăn uống... không ai giống ai.". Bố cục: Một căng tin hoạt hình rộng rãi có quầy buffet dài, mười tuyển thủ xếp hàng cầm khay, anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đứng ở cửa đeo tạp dề phục vụ, tay cầm chiếc muôi lớn.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyển thủ số tám, Chim Bồ Nông, và cái mỏ đi trước chủ nhân... 2 giây!". Bố cục: chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn bước ra, chiếc mỏ dài thò vào khung hình trước, thân mình đi theo sau, khán giả hàng đầu ngửa người né; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L180</summary>

```text
HÌNH L180 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Koala đến quầy lá khuynh diệp đầu tiên. Nhưng thay vì ăn ngay, nó làm một việc rất lạ: cúi xuống... ngửi từng chiếc lá.". Bố cục: chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ cúi sát mũi vào một rổ lá khuynh diệp, nhắm mắt hít hà như chuyên gia nếm rượu, bên cạnh có một chiếc kính lúp nhỏ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L181</summary>

```text
HÌNH L181 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà khoa học ở Nhật Bản đã quan sát 10 chú Koala trong vườn thú và thấy rằng chúng ngửi lá nhiều hơn hẳn trước khi ăn. Và mùi hương của lá có thể dự đoán chú Koala sẽ ăn lá nào.". Bố cục: Một sở thú Nhật Bản hoạt hình có cây anh đào, nhân viên đặt sáu bó lá khuynh diệp khác loại trước mặt chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ, một nhà khoa học cầm máy đo mùi hương có biểu đồ nhiều cột; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L182</summary>

```text
HÌNH L182 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vì sao phải ngửi kỹ như vậy? Vì có những cây khuynh diệp chứa nhiều một nhóm chất gây buồn nôn. Ăn phải, Koala sẽ thấy khó chịu, và từ đó nó học cách nhận ra mùi của chiếc lá "có vấn đề".". Bố cục: Hai chiếc lá khuynh diệp hoạt hình: chiếc bên trái tỏa ra làn khói mùi màu xanh lá hình mặt nhăn nhó, chiếc bên phải tỏa ra làn khói mùi màu hồng hình mặt cười; chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ né chiếc bên trái; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L183</summary>

```text
HÌNH L183 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một nghiên cứu theo dõi suốt 10 năm trên đảo Phillip ở Úc còn cho thấy: Koala thích leo những cây to, nhưng tránh những cây có lá chứa nhiều chất gây buồn nôn, hoặc lá nghèo đạm.". Bố cục: Một khu rừng khuynh diệp hoạt hình nhìn từ trên cao, mỗi cây có một chấm màu xanh hoặc đỏ đánh dấu, những chú chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ chỉ trèo lên những cây có chấm xanh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L184</summary>

```text
HÌNH L184 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Có nhà khoa học còn ví von: chọn cây để ăn đối với Koala giống như phải chọn một trong 1.000 nhà hàng khắp thành phố... mà không có ứng dụng đánh giá nào!". Bố cục: chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ đứng trên ngã tư một thành phố hoạt hình đầy những nhà hàng hình cái cây, cầm chiếc điện thoại trống trơn không có ứng dụng, gãi đầu bối rối; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L185</summary>

```text
HÌNH L185 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cá Heo đến quầy nước. Và lúc này, một câu hỏi được đặt ra: sống giữa biển nước mặn mênh mông, Cá Heo uống nước gì?". Bố cục: chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái nhô lên trước quầy nước có ba bình: bình nước biển xanh có muối kết tinh, bình nước ngọt trong veo, bình nước cam; cá heo nhìn qua lại phân vân; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L186</summary>

```text
HÌNH L186 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Câu trả lời là: gần như không uống. Cá Heo lấy nước chủ yếu từ chính thức ăn, vì con cá và con mực chứa rất nhiều nước, và từ nước mà cơ thể tự tạo ra khi đốt cháy mỡ.". Bố cục: Sơ đồ hoạt hình bên trong chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái: một con cá được ăn vào tỏa ra những giọt nước nhỏ, một khối mỡ đang cháy tỏa ra hơi nước, tất cả gom vào một chiếc bình chứa trong cơ thể; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L187</summary>

```text
HÌNH L187 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một nghiên cứu năm 2023 dùng phương pháp đo đồng vị ô-xy trong máu cá heo đã tính ra: nước từ thức ăn và nước tự tạo trong cơ thể chiếm hơn 90% lượng nước cá heo nhận vào.". Bố cục: Một biểu đồ tròn hoạt hình chia hai phần: phần rất lớn màu xanh có biểu tượng con cá và ngọn lửa, phần nhỏ xíu màu xám có biểu tượng giọt nước biển; chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái chỉ vào phần lớn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L188</summary>

```text
HÌNH L188 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sống giữa đại dương mà không uống nước biển. Giống như người sống trên đảo mà chỉ uống... nước dừa!". Bố cục: chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái nằm thư giãn trên chiếc phao giữa biển, cắm ống hút vào một quả dừa, đeo kính râm tận hưởng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L189</summary>

```text
HÌNH L189 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chim Cánh Cụt thì ngược lại. Cánh Cụt nuốt nước biển mỗi lần ăn tôm, ăn cá. Nhưng nó có một bộ lọc muối riêng: một tuyến lọc nằm ngay phía trên mắt.". Bố cục: chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ đứng trước quầy hải sản, đầu được vẽ cắt ngang như sơ đồ: phía trên mỗi mắt có một tuyến nhỏ màu hồng nối với những mạch máu li ti; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyển thủ số chín, Thú Mỏ Vịt! Và tuyển thủ số mười...". Bố cục: chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá lạch bạch bước ra vẫy cái đuôi dẹt; bên cạnh, ô cửa đường hầm thứ mười vẫn tối om; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L190</summary>

```text
HÌNH L190 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyến này lọc muối thừa ra khỏi máu, tạo thành một dung dịch nước muối đậm đặc chảy xuống mỏ. Rồi Cánh Cụt chỉ việc... hắt xì một cái, hoặc lắc đầu thật mạnh để vẩy muối ra!". Bố cục: Cận cảnh chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ hắt xì một cái thật mạnh, những giọt nước muối trong veo bay ra từ đầu mỏ, các tuyển thủ khác đứng gần giơ tay che mặt; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L191</summary>

```text
HÌNH L191 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và chúng không uống nước biển bừa bãi. Những lúc có thể, cánh cụt vẫn thích uống nước tuyết tan, hoặc ăn tuyết cho đỡ khát. Có máy lọc trong người, nhưng vẫn thích nước tinh khiết!". Bố cục: chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ cúi xuống liếm một vũng nước tuyết tan trên băng, bên cạnh là một nắm tuyết trắng xốp như kem, vẻ mặt khoan khoái; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L192</summary>

```text
HÌNH L192 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gấu Nước đến quầy... nhưng quầy nào cũng quá to. Ban tổ chức phải dùng kính hiển vi mới phục vụ được cậu ấy.". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cúi người soi qua một kính hiển vi đặt trên quầy, trong vòng tròn phóng to là chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương đang đứng trên một chiếc lá rêu xanh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L193</summary>

```text
HÌNH L193 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Phần lớn các loài gấu nước ăn thực vật: rêu, tảo. Trong miệng chúng có một cặp kim nhọn cực nhỏ. Chúng dùng kim chọc thủng thành tế bào của cây rêu, rồi hút lấy dịch bên trong như uống... trà sữa trân châu!". Bố cục: Cận cảnh hoạt hình chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương áp miệng vào một tế bào rêu xanh như quả bóng, hai chiếc kim nhỏ chọc vào, chất lỏng xanh được hút lên như hút ống hút, bên cạnh vẽ một ly trà sữa để so sánh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L194</summary>

```text
HÌNH L194 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng không phải gấu nước nào cũng ăn chay. Có những loài gấu nước ăn thịt, săn những sinh vật tí hon khác, và có loài còn ăn thịt... cả gấu nước khác!". Bố cục: Trong thế giới hiển vi hoạt hình, một chú gấu nước to hơn có vẻ mặt dữ dằn đang đuổi theo một sinh vật tí hon hình ống, chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương của chúng ta trốn sau chiếc lá rêu run rẩy; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L195</summary>

```text
HÌNH L195 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thú Mỏ Vịt, người đã có hai huy chương vàng, đến quầy cuối cùng. Và nó gọi... cả quầy! Vì như vòng ba đã kể, Thú Mỏ Vịt ăn khỏe không ai bằng.". Bố cục: chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá đứng ở quầy, chỉ tay vào toàn bộ dãy khay đồ ăn, nhân viên căng tin há hốc mồm đẩy ra cả một xe đẩy chất đầy đồ ăn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L196</summary>

```text
HÌNH L196 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Để ăn được nhiều như vậy, Thú Mỏ Vịt dành khoảng 10-12 tiếng mỗi ngày để lặn tìm mồi dưới đáy suối. Và mùa đông nước càng lạnh, nó càng phải kiếm ăn lâu hơn nữa.". Bố cục: Dưới đáy suối hoạt hình, chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá đang dùng mỏ lật đá tìm mồi, hai má phồng to dần lên, bên cạnh là chiếc đồng hồ chỉ nhiều giờ trôi qua; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L197</summary>

```text
HÌNH L197 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lửng Mật thì không đến quầy nào cả. Ban tổ chức tìm thấy Lửng Mật đang... đào tung sàn căng tin để tìm ấu trùng ong!". Bố cục: Sàn căng tin hoạt hình bị đào thủng một lỗ to, đất cát văng tung tóe lên quầy buffet, chỉ thấy cái mông và cái đuôi của chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần thò ra, nhân viên căng tin ôm đầu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L198</summary>

```text
HÌNH L198 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giám khảo xin nhắc tuyển thủ Lửng Mật: căng tin không phải là sa mạc Kalahari! Đề nghị lấp hố lại ngay!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ đứng bên miệng hố gõ búa, chỉ cây búa về phía cái hố, vẻ mặt nghiêm khắc nhưng khóe miệng nhếch cười.
```
</details>

<details><summary>L199</summary>

```text
HÌNH L199 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cháu ăn no rồi ạ! Nhưng mà cháu vẫn muốn ngửi thêm vài chiếc lá nữa, nhỡ đâu có chiếc nào thơm hơn...". Bố cục: chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ ngồi giữa đống lá khuynh diệp, cầm hai chiếc lá đưa lên mũi ngửi so sánh, vẻ mặt đắn đo như chuyên gia; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyển thủ số mười... xin lỗi toàn thể khán đài, tuyển thủ số mười hiện vẫn đang ngủ.". Bố cục: Một nhân viên hoạt hình đẩy chiếc xe đẩy chở nguyên một cành cây khuynh diệp ra sân, trên cành là chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ ôm cây ngủ say, bong bóng ngủ phồng ở mũi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L200</summary>

```text
HÌNH L200 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hết giờ giải lao! Ăn no, uống đủ, ngửi kỹ, hắt xì xong. Và giờ, các tuyển thủ quay lại sân cho vòng bốn: vòng của những giác quan siêu phàm!". Bố cục: Mười tuyển thủ no nê bước ra khỏi căng tin, chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ còn đang hắt xì, chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ còn ôm theo một bó lá, chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần phủi đất trên người, anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng giơ cờ hiệu hướng về sân thi đấu.
```
</details>

<details><summary>L201</summary>

```text
HÌNH L201 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vòng bốn: giác quan siêu phàm! Trong thế giới hoang dã, ai phát hiện ra đồ ăn trước, và phát hiện ra kẻ thù trước, người đó sống sót.". Bố cục: Một phòng thí nghiệm giác quan hoạt hình có năm khu: khu kính lúp, khu tai nghe, khu bàn tay, khu cái mũi, khu bóng đèn; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đứng ở giữa cầm micro.
```
</details>

<details><summary>L202</summary>

```text
HÌNH L202 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ban giám khảo sẽ thử thách các tuyển thủ bằng những bài kiểm tra giác quan mà chính các nhà khoa học đã làm. Mời tuyển thủ đầu tiên!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ đeo một chiếc kính lúp lớn trước mắt, trên bàn trước mặt là một bảng gỗ có những đường rãnh nhỏ khác nhau.
```
</details>

<details><summary>L203</summary>

```text
HÌNH L203 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Rái Cá Biển bước tới. Và Rái Cá được thử thách đúng thứ mà nó giỏi nhất: không phải nhìn, mà là... sờ.". Bố cục: chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách nằm ngửa cạnh bàn thí nghiệm, giơ hai bàn tay trước nhỏ xíu lên, các ngón tay ngọ nguậy háo hức; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L204</summary>

```text
HÌNH L204 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ở bang California, các nhà khoa học huấn luyện một cô rái cá tên Selka chạm tay vào những tấm bảng có rãnh, rồi chọn đúng tấm có rãnh rộng 2mm.". Bố cục: Một bể nước hoạt hình có hai tấm bảng có rãnh đặt cạnh nhau, chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách cái chìa bàn tay chạm vào tấm bên trái, một nhà khoa học hoạt hình cầm sổ ghi chép bên cạnh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L205</summary>

```text
HÌNH L205 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kết quả: Selka phân biệt được những rãnh chỉ chênh nhau khoảng 0,3mm. Mỏng hơn cả... một sợi tóc to!". Bố cục: Hình phóng to hoạt hình hai đường rãnh gần như giống hệt nhau, ở giữa là một sợi tóc người để so sánh độ mỏng, một chiếc thước đo nhỏ xíu đặt bên dưới; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L206</summary>

```text
HÌNH L206 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và Selka quyết định cực nhanh! Chỉ khoảng 0,2 giây cho mỗi lần chạm tay! Nhanh hơn những người tình nguyện làm cùng bài kiểm tra gần 30 lần!". Bố cục: Một đồng hồ bấm giờ hoạt hình bên cạnh chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách chỉ một vạch nhỏ, bên cạnh là một người tình nguyện đeo kính đang sờ tấm bảng chậm chạp, mặt nhíu mày, chiếc đồng hồ của người đó quay nhiều vòng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L207</summary>

```text
HÌNH L207 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vì sao Rái Cá cần đôi tay nhanh như thế? Vì mỗi lần lặn chỉ kéo dài 1-2 phút, dưới đáy biển tối và đục. Nó phải sờ, chọn, và nhét đồ ăn vào túi dưới nách trong chớp mắt.". Bố cục: Dưới đáy biển đục ngầu hoạt hình, chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách nhắm mắt, hai bàn tay lướt nhanh qua cát và đá, nhặt một con nhím biển và một con ốc nhét vào túi dưới nách; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L208</summary>

```text
HÌNH L208 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giám khảo xin ghi nhận: đôi bàn tay của Rái Cá nhạy chẳng kém bàn tay người, mà nhanh gấp bội.". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ chạm thử vào tấm bảng có rãnh bằng đầu cánh, nhíu mày, rồi nhìn sang chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách với vẻ thán phục.
```
</details>

<details><summary>L209</summary>

```text
HÌNH L209 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyển thủ tiếp theo: Chim Cánh Cụt. Và thử thách của Cánh Cụt là... nhìn rõ ở cả hai thế giới. Trên cạn, và dưới nước.". Bố cục: chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ đứng ở mép hồ, một nửa khung hình là không khí trong vắt có núi băng, một nửa là nước xanh sâu thẳm có đàn cá nhỏ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ủa... đến lượt cháu chưa ạ? Cháu vừa mơ thấy một cái cây to ơi là to!". Bố cục: Cận cảnh chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ mở một mắt lơ mơ, lông tai rối bù, ngáp dài; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L210</summary>

```text
HÌNH L210 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bạn đã bao giờ mở mắt dưới nước chưa? Mọi thứ nhòe nhoẹt. Vì giác mạc của mắt người cong, nó chỉ hội tụ ánh sáng tốt trong không khí. Xuống nước, nó gần như mất tác dụng.". Bố cục: Một người hoạt hình lặn dưới nước mở mắt, mọi thứ xung quanh mờ nhòe như ảnh bị nhòe nước, trên đầu là dấu chấm hỏi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L211</summary>

```text
HÌNH L211 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chim cánh cụt giải bài toán này bằng một mẹo khác: giác mạc của chúng phẳng hơn mắt người rất nhiều. Phần việc hội tụ được giao gần hết cho thủy tinh thể, một chiếc thấu kính mềm có thể bóp phồng lên khi cần.". Bố cục: Sơ đồ mắt hoạt hình so sánh: mắt người có giác mạc cong như mái vòm, mắt chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ có giác mạc phẳng như cửa kính, bên trong là thủy tinh thể tròn đang được những sợi cơ nhỏ bóp phồng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L212</summary>

```text
HÌNH L212 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhờ vậy, Chim Cánh Cụt nhìn rõ trên băng để tìm đường về tổ, và nhìn rõ dưới nước để bắt cá. Như một chiếc máy ảnh tự động đổi ống kính khi lặn xuống!". Bố cục: chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ đeo một chiếc máy ảnh hoạt hình trước ngực, ống kính tự động xoay đổi khi chú nhảy từ tảng băng xuống nước, chú cá nhỏ dưới nước giật mình; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L213</summary>

```text
HÌNH L213 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyển thủ tiếp theo, Koala, bước lên với một bài thi... âm nhạc. Như các bạn đã biết, Koala đực có giọng rống trầm như quái vật. Nhưng giọng rống ấy còn chứa một bí mật.". Bố cục: chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ đứng trước một chiếc micro sân khấu, ngại ngùng chỉnh lại áo bệnh nhân, phía sau là dàn loa lớn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L214</summary>

```text
HÌNH L214 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Năm 2011, các nhà khoa học thu âm tiếng rống của 20 chú Koala đực và phân tích bằng máy tính. Họ phát hiện mỗi chú có một chất giọng riêng, như dấu vân tay âm thanh.". Bố cục: Màn hình máy tính hoạt hình hiện hai mươi đường sóng âm khác nhau xếp chồng, mỗi đường một màu, bên cạnh là hình hai mươi chú chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ nhỏ, mỗi chú cạnh một đường sóng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L215</summary>

```text
HÌNH L215 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và quan trọng hơn: chính những chú Koala khác cũng nhận ra sự khác nhau ấy. Khi nghe một giọng lạ, chúng lập tức quay đầu nhìn về phía loa lâu hơn hẳn.". Bố cục: Một chú chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ đang ngồi lim dim trên cây bỗng mở to mắt quay phắt về phía chiếc loa đặt dưới gốc cây, tai dựng lên; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L216</summary>

```text
HÌNH L216 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nghiên cứu sau đó còn cho thấy: giọng rống của con đực tiết lộ kích thước cơ thể. Giọng càng trầm, con đực càng to. Và các cô Koala cái... thích những giọng trầm hơn!". Bố cục: Một cô chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ cái ngồi trên cành, nghe hai chiếc loa: loa bên trái phát nốt nhạc nhỏ cao, loa bên phải phát nốt nhạc to trầm; cô quay về phía loa bên phải, trái tim nhỏ bay lên; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L217</summary>

```text
HÌNH L217 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cháu biết rồi, cháu sẽ hát trầm hơn ạ! Ừm... ọ ọ ọ!". Bố cục: chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ cố hạ giọng, hai má phồng lên, mắt nhắm tịt, phát ra nốt nhạc vẽ to đùng nhưng méo xệch; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L218</summary>

```text
HÌNH L218 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyển thủ tiếp theo, Cá Heo, mang đến một bài thi về... sự tỉnh táo. Năm 2012, các nhà khoa học ở Mỹ thử xem cá heo có thể canh gác liên tục được bao lâu.". Bố cục: chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái bơi trong một hồ nước có tám chiếc loa nhỏ đặt quanh viền hồ, một tấm bảng nút bấm nổi trên mặt nước, một nhà khoa học hoạt hình ngồi trên bờ với ly cà phê; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L219</summary>

```text
HÌNH L219 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhiệm vụ: liên tục dùng tiếng định vị để quét quanh hồ, khi nào phát hiện mục tiêu giả do máy phát ra thì bấm nút báo. Mục tiêu xuất hiện bất ngờ, ở bất kỳ hướng nào, vào bất kỳ lúc nào.". Bố cục: Sơ đồ hoạt hình nhìn từ trên xuống: chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái ở giữa hồ, những vòng sóng âm tỏa ra tám hướng, ở một hướng có một ngôi sao nhỏ lóe sáng là mục tiêu, cá heo đang bơi về phía nút bấm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Rồi, Gấu Koala cũng đã có mặt! Nhưng trước khi xem dự đoán, theo đúng truyền thống của mọi giải đấu lớn, chúng ta có... lễ cân ký! Mời các tuyển thủ lần lượt bước lên bàn cân.". Bố cục: Một chiếc cân bàn khổng lồ hoạt hình kiểu võ đài quyền anh giữa sân, có kim chỉ tròn to, hai bên là đèn flash và phóng viên; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đứng cạnh cầm micro.
```
</details>

<details><summary>L220</summary>

```text
HÌNH L220 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một chú cá heo cái đã làm nhiệm vụ này suốt 15 ngày liền. Ngày lẫn đêm! Không nghỉ! Và độ chính xác gần như tuyệt đối từ ngày đầu đến ngày cuối!". Bố cục: Cuốn lịch hoạt hình lật liên tục mười lăm trang, xen kẽ mặt trời và mặt trăng, chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái vẫn tỉnh táo bấm nút báo chính xác, trong khi nhà khoa học trên bờ đã ngủ gục bên ly cà phê; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L221</summary>

```text
HÌNH L221 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và cuộc thử nghiệm chỉ dừng lại vì... một cơn bão mùa đông kéo đến. Không phải vì cá heo mệt!". Bố cục: Bầu trời giông bão hoạt hình, mưa xối xả trên hồ, các nhà khoa học mặc áo mưa chạy thu dọn thiết bị, chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái vẫn nhô đầu lên nhìn họ như hỏi: sao dừng rồi?; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L222</summary>

```text
HÌNH L222 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khán giả của kênh đã biết cá heo ngủ luân phiên từng nửa bộ não. Nhưng phải đến thí nghiệm này, người ta mới thấy cách ngủ ấy cho phép nó canh gác lâu đến mức nào.". Bố cục: Hình bộ não chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái hoạt hình chia đôi: nửa trái đội mũ ngủ và ngáy "zzz", nửa phải đeo kính và cầm ống nhòm canh gác; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L223</summary>

```text
HÌNH L223 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng Chim Cánh Cụt không chịu thua ở môn ngủ! Năm 2023, các nhà khoa học gắn máy đo sóng não lên những chú chim cánh cụt quai mũ đang ấp trứng ở Nam Cực, họ hàng gần của Adélie.". Bố cục: Một chú chim cánh cụt có dải lông đen mảnh vắt qua cằm như quai mũ, đang nằm ấp trứng trên tổ sỏi, trên lưng có gắn thiết bị nhỏ có ăng-ten; chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ đứng cạnh chỉ vào như giới thiệu người anh họ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L224</summary>

```text
HÌNH L224 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và họ phát hiện: những chú chim này ngủ gật hơn 10.000 lần mỗi ngày! Mỗi giấc chỉ kéo dài khoảng 4 giây!". Bố cục: Chuỗi hình hoạt hình nhỏ liên tiếp: chú chim cánh cụt quai mũ nhắm mắt gục đầu, mở mắt, nhắm mắt, mở mắt, như đèn nhấp nháy, bên cạnh là đồng hồ bấm giờ chỉ bốn giây; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L225</summary>

```text
HÌNH L225 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cộng tất cả những giấc ngủ 4 giây ấy lại, chúng ngủ được hơn 11 tiếng mỗi ngày. Mà vẫn kịp canh trứng trước những con chim cướp biển lượn ngay trên đầu!". Bố cục: Chú chim cánh cụt quai mũ đang gật gù ngủ thì giật mình mở mắt thấy một con chim cướp biển màu nâu đang lượn gần, chú lập tức xù lông dọa, rồi lại gục đầu ngủ tiếp; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L226</summary>

```text
HÌNH L226 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giám khảo xin tổng kết vòng bốn: đôi tay nhạy, đôi mắt hai thế giới, giọng hát mang tên riêng, và người lính gác không bao giờ ngủ trọn giấc. Một vòng thi rất khó chấm!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ đặt bốn tấm thẻ lên bàn: bàn tay, con mắt, nốt nhạc, chiếc đèn pin, rồi gãi đầu suy nghĩ, chiếc bút chì kẹp sau tai.
```
</details>

<details><summary>L227</summary>

```text
HÌNH L227 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kết quả vòng bốn! Huy chương đồng: Chim Cánh Cụt, đôi mắt hai thế giới và giấc ngủ 4 giây!". Bố cục: Bục trao giải: chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ đứng bậc đồng, đeo huy chương đồng, đeo kính lặn trên trán, mắt lim dim như sắp ngủ gật; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L228</summary>

```text
HÌNH L228 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Huy chương bạc: Rái Cá Biển, bàn tay nhạy và nhanh gấp 30 lần người! Và huy chương vàng...". Bố cục: chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách đứng bậc bạc giơ hai bàn tay lên khoe, đeo huy chương bạc; bậc vàng phía trên có ánh đèn spotlight chiếu xuống, chưa ai đứng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L229</summary>

```text
HÌNH L229 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thuộc về Cá Heo, người lính gác 15 ngày không ngủ!". Bố cục: chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái nhảy vọt lên khỏi bể nước trên bậc vàng, đeo huy chương vàng, đội chiếc mũ lính gác nhỏ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cá Heo bước lên! Kim cân quay vù vù! Một chú cá heo mũi chai trưởng thành có thể nặng từ 150 đến hơn 600kg! Tuyển thủ nặng ký nhất đại hội!". Bố cục: chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái nằm trên chiếc cân bàn đặt trong bể nước, kim cân quay mấy vòng, chiếc cân kêu cót két, phóng viên lùi lại; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L230</summary>

```text
HÌNH L230 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bảng điểm sau bốn vòng: Thú Mỏ Vịt vẫn dẫn đầu với 6 điểm! Chồn Gulo 4 điểm. Chim Cánh Cụt 4 điểm. Rái Cá 3 điểm. Cá Heo 3 điểm. Bồ Nông 2 điểm. Koala và Tôm Tít 1 điểm. Lửng Mật và Gấu Nước: vẫn chưa có điểm!". Bố cục: tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) sáng lên: cột chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá cao nhất, hai cột chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh và chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ bằng nhau, các cột khác thấp dần, hai cột chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần và chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương tắt ngúm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L231</summary>

```text
HÌNH L231 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vòng tiếp theo sẽ không chấm khả năng tìm đồ ăn. Mà chấm khả năng chăm sóc một sinh mạng nhỏ bé. Vòng năm: những người cha, người mẹ phi thường.". Bố cục: Một chiếc tổ nhỏ hoạt hình nằm giữa ánh đèn sân khấu dịu nhẹ, bên trong là một quả trứng nhỏ, xung quanh tối dần; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L232</summary>

```text
HÌNH L232 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đêm buông xuống sân vận động. Đại hội tạm nghỉ trước bốn vòng cuối. Các tuyển thủ trở về khu nghỉ ngơi. Nhưng không phải ai cũng ngủ...". Bố cục: Sân vận động hoạt hình ban đêm, đèn đã tắt gần hết, chỉ còn ánh trăng, phía xa là khu nhà nghỉ của tuyển thủ với vài ô cửa sổ còn sáng đèn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L233</summary>

```text
HÌNH L233 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Máy quay hậu trường của chúng tôi đi một vòng khu nghỉ ngơi. Và những gì nó ghi lại được... rất đáng xem.". Bố cục: Một chiếc máy quay hoạt hình có đèn đỏ nhấp nháy đang lén lút đi dọc hành lang tối, ống kính chĩa vào khe cửa một phòng nghỉ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L234</summary>

```text
HÌNH L234 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Phòng số một: Chồn Gulo. Không ngủ. Đang... leo núi. Ngay trong đêm.". Bố cục: Qua cửa sổ phòng nghỉ, thấy chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh đang leo một bức tường leo núi trong nhà, phía sau cửa sổ là dãy núi tuyết dưới ánh trăng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L235</summary>

```text
HÌNH L235 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ở công viên quốc gia Glacier nước Mỹ, các nhà nghiên cứu theo dõi bằng vòng cổ định vị nhận xét: Chồn Gulo có thể đi 150-200km mỗi tuần trong công viên.". Bố cục: Một bản đồ công viên quốc gia hoạt hình có núi tuyết, hồ nước và rừng thông, trên đó là đường đi dài màu đỏ của chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh đeo vòng cổ có ăng-ten; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L236</summary>

```text
HÌNH L236 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và chúng rất ít khi đi đường vòng. Gặp núi thì leo, gặp đường thì băng qua. Đúng là đi đâu cũng... đi thẳng!". Bố cục: Một bản đồ hoạt hình có nhiều đường thẳng tắp như kẻ thước cắt ngang qua núi, qua sông, qua đường; chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh đứng ở đầu một đường thẳng, đội mũ bảo hiểm leo núi, giơ ngón cái; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L237</summary>

```text
HÌNH L237 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Phòng số hai: Thú Mỏ Vịt. Đèn tắt. Tuyển thủ đang dẫn đầu bảng điểm đang ngủ say. Nhưng hãy nhìn kỹ... cái mỏ đang giật giật, và mắt đang đảo liên tục dưới mí.". Bố cục: Trong phòng tối hoạt hình, chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá cuộn tròn ngủ trong ổ chăn, chiếc vương miện đồ chơi đặt trên bàn đầu giường, cái mỏ khẽ giật, mí mắt rung rung; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L238</summary>

```text
HÌNH L238 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đó là giai đoạn ngủ mơ, giai đoạn mà ở người, chúng ta thường nằm mơ. Và Thú Mỏ Vịt giữ kỷ lục: hơn 8 tiếng ngủ mơ mỗi ngày, nhiều hơn bất kỳ loài động vật nào từng được đo.". Bố cục: Phía trên đầu chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá là bong bóng giấc mơ khổng lồ: Thú Mỏ Vịt đang đứng trên bục vô địch, xung quanh là những con tôm nhỏ vỗ tay; một chiếc cúp nhỏ ghi kỷ lục (không chữ) đặt cạnh giường; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L239</summary>

```text
HÌNH L239 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà khoa học đoán rằng giấc ngủ mơ có thể đã xuất hiện từ rất sớm ở những loài thú đầu tiên, và Thú Mỏ Vịt, thuộc nhóm thú đẻ trứng đã tách ra từ rất xa xưa, có thể đang giữ lại dấu vết đó.". Bố cục: Một cây gia phả hoạt hình cổ kính, ở gốc rễ là hình chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá đang ngủ với bong bóng giấc mơ, các cành phía trên là hình các loài thú khác cũng đang ngủ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chim Bồ Nông bước lên! Cân nặng thì vừa phải, nhưng đôi cánh dang ra dài hơn 2,5 mét! Ban tổ chức phải mở rộng cả cửa phòng cân!". Bố cục: chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn đứng trên cân dang rộng đôi cánh dài quá cả khung cửa, đầu cánh đập trúng hai nhân viên đứng hai bên; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L240</summary>

```text
HÌNH L240 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Phòng số ba: Chim Cánh Cụt. Mắt nhắm. Mở. Nhắm. Mở. Nó không ngủ một giấc dài. Nó ngủ... hàng ngàn giấc ngắn.". Bố cục: Trong phòng nghỉ hoạt hình, chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ đứng ngủ cạnh tổ sỏi nhỏ mang theo từ nhà, mắt nhấp nháy liên tục, xung quanh có những chữ "zzz" nhỏ xíu xuất hiện rồi biến mất; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L241</summary>

```text
HÌNH L241 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Như vòng bốn đã kể, họ hàng của nó, chim cánh cụt quai mũ, có thể ngủ hơn 10.000 giấc mỗi ngày, mỗi giấc khoảng 4 giây. Ngủ kiểu ấy để làm gì? Để không bao giờ lơ là canh tổ.". Bố cục: chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ đang gật gù bỗng mở to mắt khi nghe tiếng động ngoài cửa sổ, nơi bóng một con chim cướp biển lượn qua dưới ánh trăng, chú lập tức che chắn tổ sỏi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L242</summary>

```text
HÌNH L242 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Phòng số bốn: Rái Cá Biển. Phòng này... có bể nước. Và Rái Cá đang nằm ngửa trên mặt nước, hai bàn tay úp lên mắt, ngủ ngon lành.". Bố cục: Một phòng nghỉ hoạt hình có bồn tắm lớn, chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách nằm ngửa trên mặt nước, hai bàn tay úp lên mắt như đeo mặt nạ ngủ, một dải tảo bẹ quấn quanh bụng buộc vào vòi nước; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L243</summary>

```text
HÌNH L243 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà khoa học cho biết, mỗi ngày Rái Cá Biển dành khoảng 11 tiếng để nghỉ ngơi và ngủ, khoảng 8 tiếng để kiếm ăn, và 5 tiếng để chải lông và vui chơi. Một lịch trình... đáng mơ ước!". Bố cục: Một chiếc đồng hồ tròn hoạt hình chia ba phần màu: phần xanh có biểu tượng giường ngủ, phần cam có biểu tượng con cua, phần hồng có biểu tượng chiếc lược và quả bóng; chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách đứng cạnh giơ ngón cái; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L244</summary>

```text
HÌNH L244 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Phòng số năm: Gấu Nước. Máy quay soi qua kính hiển vi... và thấy Gấu Nước đang tập thể dục! Nó đi tới đi lui trên tấm thảm thạch rau câu.". Bố cục: Qua kính hiển vi hoạt hình, chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương mặc chiếc áo thể thao tí hon đi tới đi lui trên một tấm thạch trong suốt, đeo băng đô thể thao; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L245</summary>

```text
HÌNH L245 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Năm 2020 mốt, các nhà khoa học đã quay phim gấu nước đi bộ trên những tấm thạch, và phát hiện ra một điều bất ngờ: gấu nước đi giống hệt... côn trùng! Dù côn trùng to gấp khoảng 500.000 lần.". Bố cục: Chia đôi khung hình: bên trái chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương đi bằng tám chân với những dấu chân đánh số thứ tự nhịp bước; bên phải một chú bọ cánh cứng to lớn đi với nhịp bước giống hệt; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L246</summary>

```text
HÌNH L246 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lúc đi dạo, gấu nước đi khoảng nửa thân mình mỗi giây. Khi gấp gáp, nó có thể tăng tốc lên khoảng hai thân mình mỗi giây. Nghe thì chậm, nhưng với một sinh vật nhỏ hơn hạt cát, đó là... chạy nước rút!". Bố cục: chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương đang chạy nước rút trên đường chạy tí hon, mồ hôi bay ra, các nét gió tốc độ phía sau, ở vạch đích có một chiếc cờ nhỏ bằng hạt bụi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L247</summary>

```text
HÌNH L247 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Phòng số sáu, phòng cuối cùng: Lửng Mật. Cửa phòng mở. Giường trống. Trên tường có một cái lỗ to. Lửng Mật... đã vượt ngục. Một lần nữa.". Bố cục: Một phòng nghỉ hoạt hình trống trơn, giường chăn gối xộc xệch, trên tường có một cái lỗ tròn to đào xuyên ra ngoài, đất cát rơi vãi, ánh trăng chiếu qua lỗ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L248</summary>

```text
HÌNH L248 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Máy quay chạy theo dấu chân và tìm thấy Lửng Mật đang ngồi ngoài sân, dưới ánh trăng, bên cạnh... chú lửng con của mình. Hai mẹ con đang tập đào hang.". Bố cục: Ngoài sân dưới ánh trăng hoạt hình, chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần mẹ và lửng con cùng đào một cái hố nhỏ, mẹ làm mẫu, con bắt chước theo vụng về, hai mẹ con dính đầy đất cát nhưng rất vui vẻ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L249</summary>

```text
HÌNH L249 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hóa ra gã giang hồ nổi tiếng nhất đại hội, đêm nay không đi gây sự. Nó chỉ dành thời gian dạy con. Mai là vòng thi về cha mẹ. Và Lửng Mật... đã sẵn sàng.". Bố cục: Cận cảnh chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần mẹ ôm lửng con ngồi dưới ánh trăng, hai mẹ con nhìn lên bầu trời đầy sao, phía xa là sân vận động im lặng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Rái Cá Biển bước lên, ôm theo hòn đá! Ban tổ chức yêu cầu bỏ hòn đá ra. Rái Cá... từ chối. Thôi, cân luôn cả đá!". Bố cục: chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách đứng trên cân ôm chặt hòn đá xám vào ngực, lắc đầu nguầy nguậy, nhân viên cân giơ tay bất lực; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L250</summary>

```text
HÌNH L250 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Máy quay hậu trường xin phép tắt đèn đỏ, rút êm khỏi khu nghỉ ngơi. Vì nếu Lửng Mật phát hiện ra mình bị quay lén... thì người tiếp theo phải đào hầm trốn chính là đội quay phim!". Bố cục: Chiếc máy quay hoạt hình có đèn đỏ nhấp nháy rón rén lùi ra khỏi sân, phía sau hai mắt chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần sáng lóe trong bóng tối nhìn theo, người quay phim toát mồ hôi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L251</summary>

```text
HÌNH L251 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trời sáng dần. Mặt trời mọc trên sân vận động. Và còn đúng... bốn vòng thi nữa.". Bố cục: Bình minh hoạt hình rực rỡ trên sân vận động, ánh nắng đầu tiên chiếu lên chiếc vương miện bé xíu trên bệ đá giữa sân, chim hót trên mái khán đài; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L252</summary>

```text
HÌNH L252 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vòng năm: cha mẹ phi thường! Sống sót một mình đã khó. Vừa sống sót, vừa nuôi một đứa con bé bỏng, còn khó hơn gấp bội.". Bố cục: Sân khấu hoạt hình được trang trí như một căn phòng em bé ấm áp, có nôi, có thú bông, có những tổ chim nhỏ, anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đứng ở giữa nói nhỏ nhẹ.
```
</details>

<details><summary>L253</summary>

```text
HÌNH L253 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giám khảo sẽ chấm: ai chăm con chu đáo nhất, ai dạy con kiên nhẫn nhất, và ai có chiêu nuôi con... độc nhất vô nhị.". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ đeo chiếc tạp dề có hình trái tim, cầm bình sữa nhỏ, ngồi ở bàn giám khảo với vẻ hiền từ.
```
</details>

<details><summary>L254</summary>

```text
HÌNH L254 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mở màn là Lửng Mật, tuyển thủ vẫn đang trắng điểm sau bốn vòng. Và Lửng Mật mẹ khiến cả khán đài bất ngờ: gã giang hồ dữ dằn ấy hóa ra là một bà mẹ... vô cùng cẩn thận.". Bố cục: chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần mẹ bước lên sân khấu, miệng ngậm nhẹ nhàng một chú lửng con bé xíu hồng hào chưa có lông, vẻ mặt dịu dàng hiếm thấy; khán đài ồ lên ngạc nhiên; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L255</summary>

```text
HÌNH L255 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ở sa mạc Kalahari, Lửng Mật mẹ thường chỉ nuôi một con mỗi lứa. Lửng con mới sinh không có lông, mắt nhắm nghiền, và phải hai tháng sau mới mở mắt.". Bố cục: Trong hang đất hoạt hình, một chú lửng con bé xíu trụi lông, mắt nhắm, nằm cuộn tròn trên lớp cỏ khô, chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần mẹ nằm che chắn bên cạnh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L256</summary>

```text
HÌNH L256 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và để giữ an toàn cho con, cứ vài ngày Lửng Mật mẹ lại ngậm con trong miệng, mang sang một cái hang mới. Trung bình chỉ ở mỗi hang khoảng 3 ngày, hang này cách hang kia khoảng 2km!". Bố cục: Bản đồ sa mạc hoạt hình có nhiều chấm hang nối bằng đường chấm chấm, chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần mẹ đang ngậm con đi trên đường giữa hai hang dưới ánh trăng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L257</summary>

```text
HÌNH L257 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lửng con ở với mẹ ít nhất 14 tháng. Suốt thời gian ấy, mẹ dạy con đào hang, leo cây, bắt chuột, và cả cách đối phó với rắn độc. Một khóa học sinh tồn kéo dài hơn một năm!". Bố cục: chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần mẹ đứng cạnh một tấm bảng đen hoạt hình vẽ hình cái xẻng, cái cây, con chuột và con rắn, lửng con ngồi chăm chú như học sinh, cầm bút chì ghi chép; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L258</summary>

```text
HÌNH L258 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giám khảo xin ghi nhận: bà mẹ chuyển nhà nhiều nhất, và dạy con lâu nhất cuộc thi.". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gật đầu ghi chép, mắt hơi rưng rưng, đặt một ngôi sao vàng nhỏ lên bảng cạnh hình đầu chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần.
```
</details>

<details><summary>L259</summary>

```text
HÌNH L259 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyển thủ tiếp theo, Thú Mỏ Vịt mẹ, trình bày cách làm tổ đẻ trứng. Đúng vậy, một loài thú có sữa... mà lại đẻ trứng!". Bố cục: chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá mẹ đeo nơ hồng, cầm trên tay hai quả trứng nhỏ màu trắng ngà, vỏ mềm như giấy da, khán giả trên khán đài há hốc mồm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lửng Mật và Chồn Gulo bước lên cùng lúc, vì không ai chịu nhường ai. Hai gã nặng chừng một bao gạo nhỏ, nhưng nhìn cách hai gã gườm nhau thì... tưởng nặng cả tấn!". Bố cục: chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần và chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh cùng chen nhau trên một chiếc cân, trán chạm trán gườm gườm như hai võ sĩ trước trận đấu, kim cân rung lắc; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L260</summary>

```text
HÌNH L260 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trước khi đẻ, Thú Mỏ Vịt mẹ đào một đường hầm dài dọc bờ sông, có khi tới 20 mét. Rồi tha lá ướt và cành nhỏ vào trải ổ, bằng cách... kẹp chúng giữa đuôi và chân sau!". Bố cục: Mặt cắt ngang bờ sông hoạt hình có đường hầm dài ngoằn ngoèo, chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá mẹ đang đi giật lùi trong hầm, đuôi cuộn kẹp một bó lá ướt; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L261</summary>

```text
HÌNH L261 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và mỗi lần ra khỏi hang, mẹ lại đắp đất bịt kín đường hầm thành nhiều lớp, có khi tới 9 lớp. Để ngăn kẻ thù, và để giữ cho ổ không bị ngập khi nước sông dâng.". Bố cục: Đường hầm hoạt hình có những bức tường đất nhỏ chắn ngang thành nhiều lớp như những cánh cửa, chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá mẹ đang dùng đuôi vỗ chặt lớp đất cuối cùng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L262</summary>

```text
HÌNH L262 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thú Mỏ Vịt mẹ đẻ từ 1 đến 3 trứng, thường là hai. Rồi mẹ cuộn tròn người, ôm trứng giữa bụng và đuôi suốt khoảng 10 ngày để ấp, cho đến khi những chú con bé như hạt đậu chui ra.". Bố cục: chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá mẹ cuộn tròn trong ổ lá, ôm hai quả trứng nhỏ giữa bụng và đuôi, ánh sáng ấm áp; một quả trứng đang nứt, lộ ra cái mỏ bé xíu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L263</summary>

```text
HÌNH L263 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyển thủ tiếp theo, Rái Cá Biển mẹ, bước lên với một chú con nằm trên ngực. Rái cá con mới sinh có bộ lông xù đến mức... không thể lặn xuống nước được. Nó nổi bồng bềnh như cái phao!". Bố cục: chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách mẹ nằm ngửa trên mặt biển, trên ngực là một chú rái cá con lông xù màu nâu nhạt tròn như quả bóng bông, đang ngủ ngon lành; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L264</summary>

```text
HÌNH L264 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nên khi mẹ phải lặn xuống đáy biển kiếm ăn, mẹ để con nổi trên mặt nước, có khi còn quấn con vào tảo bẹ cho khỏi trôi. Rồi mẹ ngoi lên, lại đặt con lên ngực, chải lông, cho bú.". Bố cục: Chú rái cá con lông xù được quấn nhẹ trong dải tảo bẹ nổi trên mặt nước như trong chiếc nôi, dưới nước sâu chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách mẹ đang lặn tìm cua; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L265</summary>

```text
HÌNH L265 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Rái cá con phụ thuộc vào mẹ khoảng 6 đến 8 tháng. Mẹ dạy con lặn, dạy con chọn món ăn, và quan trọng nhất: dạy con dùng hòn đá đập vỏ. Rái cá con thường thích ăn những món giống hệt món mẹ thích!". Bố cục: chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách mẹ và con nằm ngửa cạnh nhau, mỗi bạn kẹp một hòn đá, mẹ làm mẫu đập vỏ sò, con bắt chước theo với vẻ mặt chăm chú, trên bụng mỗi bạn là cùng một loại con sò; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L266</summary>

```text
HÌNH L266 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyển thủ tiếp theo, Cá Heo mẹ, trình bày một thứ mà các nhà khoa học mới phát hiện năm 2023: cá heo mẹ cũng nói giọng... nựng con!". Bố cục: chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái mẹ bơi cạnh một chú cá heo con nhỏ xíu, từ miệng cá heo mẹ bay ra những nốt nhạc hình trái tim; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L267</summary>

```text
HÌNH L267 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà khoa học ở bang Florida đã ghi âm 19 cá heo mẹ, khi có con bên cạnh, và khi không có con. Và tất cả các cá heo mẹ đều thay đổi tiếng huýt sáo khi có con ở gần.". Bố cục: Hai đường sóng âm hoạt hình so sánh: đường thứ nhất bình thường, đường thứ hai vọt lên cao hơn và rộng hơn, bên cạnh là hình cá heo mẹ có cá heo con bơi cạnh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L268</summary>

```text
HÌNH L268 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tiếng huýt sáo cao hơn, và rộng giọng hơn. Giống hệt cách các bà mẹ con người tự nhiên nói giọng cao, ngân nga khi nựng em bé. Hai loài khác nhau, sống ở hai thế giới khác nhau, mà lại có chung một cách nói với con.". Bố cục: Chia đôi khung hình: bên trái một bà mẹ người hoạt hình ôm em bé nói chuyện, những nốt nhạc nhỏ bay ra; bên phải chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái mẹ bơi cạnh con, những nốt nhạc giống hệt bay ra; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L269</summary>

```text
HÌNH L269 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và cuối cùng, Chồn Gulo mẹ. Như vòng một đã kể, chồn mẹ đào hang dưới lớp tuyết dày để sinh con. Nhưng chồn mẹ còn một chiêu nữa: khi cần, chồn mẹ dời con sang hang khác, có khi dùng nhiều hang khác nhau trước khi con cai sữa.". Bố cục: chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh mẹ đang ngậm một chú chồn con lông trắng xám nhỏ xíu, đi trên tuyết dưới bầu trời sao từ một hang tuyết này sang một hang tuyết khác; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chim Cánh Cụt, Koala, Thú Mỏ Vịt lần lượt bước lên. Thú Mỏ Vịt nhẹ nhất trong ba bạn, chỉ khoảng 1-2kg, nhẹ hơn cả một con mèo nhà.". Bố cục: Ba chiếc cân nhỏ xếp hàng: chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ đứng thẳng chỉnh nơ, chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ ôm cây cột cân ngủ gật, chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá đứng trên chiếc cân nhỏ nhất kim chỉ gần như không nhúc nhích; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L270</summary>

```text
HÌNH L270 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chồn con được nuôi trong hang đến khoảng 9-10 tuần tuổi, rồi mới bắt đầu theo mẹ ra ngoài. Và ở Bắc Mỹ, các nhà khoa học còn thấy chồn bố thỉnh thoảng quay lại thăm con, dẫn con đi khám phá lãnh thổ.". Bố cục: chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh bố dẫn hai chú chồn con đi trên sườn núi tuyết, chồn con lon ton theo sau, một chú bị trượt chân lăn tuyết, chồn bố quay lại nhìn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L271</summary>

```text
HÌNH L271 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyển thủ tiếp theo, Chim Cánh Cụt, trình bày một hệ thống chăm con kiểu... đổi ca trực. Chim Cánh Cụt Adélie thường đẻ hai trứng, và bố mẹ thay phiên nhau ấp, mỗi ca thường kéo dài khoảng 12 ngày.". Bố cục: Một tấm lịch trực hoạt hình treo cạnh tổ sỏi, các ô xen kẽ hình chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ bố đeo nơ đỏ và chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ mẹ đeo nơ hồng, giữa tổ là hai quả trứng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L272</summary>

```text
HÌNH L272 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng ca đầu tiên là ca khổ nhất. Chim bố ở lại ấp trong khi chim mẹ ra biển kiếm ăn. Tính cả mùa tán tỉnh trước đó, chim bố có thể nhịn đói khoảng một tháng liền mà không rời tổ.". Bố cục: chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ bố gầy rộc đi, chiếc nơ đỏ trễ xuống, bụng kêu ọt ọt có vẽ bong bóng hình con tôm, nhưng vẫn ngồi im ôm hai quả trứng giữa trời gió tuyết; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L273</summary>

```text
HÌNH L273 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi chim con được khoảng ba tuần tuổi, chúng đã đủ lớn để không cần bố mẹ ủ ấm. Chúng tụ tập thành những nhóm đông gọi là "nhà trẻ", đứng sát vào nhau để giữ ấm và chống lại chim săn mồi. Còn bố mẹ thì cùng nhau ra biển, kiếm cá về nuôi con.". Bố cục: Một nhóm đông chim cánh cụt con lông xám bông xù đứng sát vào nhau như một nhà trẻ ngoài trời, có vài chú lớn đứng canh ngoài rìa, phía xa chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ bố mẹ cùng lạch bạch đi về phía biển; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L274</summary>

```text
HÌNH L274 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và một bất ngờ đến từ Tôm Tít! Gã võ sĩ đại dương có một người họ hàng nhỏ xíu, loài tôm tít Pullosquilla, sống ở Ấn Độ Dương và Thái Bình Dương. Và loài này... nuôi con bằng cả bố lẫn mẹ!". Bố cục: Một chiếc hang chữ U dưới cát hoạt hình, bên trong có hai chú tôm tít nhỏ xíu nằm hai đầu hang, mỗi chú ôm một ổ trứng nhỏ màu hồng; chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh đứng bên ngoài chỉ vào như giới thiệu họ hàng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L275</summary>

```text
HÌNH L275 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cả bố và mẹ đều quạt nước cho trứng để trứng có đủ ô-xy, nhặt bỏ trứng hỏng, và di chuyển ổ trứng trong hang. Khi thức ăn dồi dào, tôm mẹ có thể đẻ thêm ổ thứ hai khi ổ thứ nhất chưa nở. Và lúc ấy, cả hai vợ chồng cùng chăm hai ổ trứng!". Bố cục: Hai chú tôm tít nhỏ trong hang quạt những chiếc chân bơi tạo dòng nước nhỏ thổi qua hai ổ trứng, một chú đang nhặt một quả trứng màu xám ra ngoài; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L276</summary>

```text
HÌNH L276 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Theo các nhà khoa học, trong số các loài giáp xác sống ở biển, đây là nhóm duy nhất từng được nghiên cứu kỹ về việc cả bố lẫn mẹ cùng chăm trứng. Võ sĩ ngoài đời, ông bố mẫu mực trong hang!". Bố cục: chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh đeo tạp dề hồng, một càng cầm chiếc quạt nhỏ, một càng bế ổ trứng, vẻ mặt nghiêm túc của một ông bố; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L277</summary>

```text
HÌNH L277 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ban giám khảo xin phép nghỉ giải lao một chút... để lau nước mắt. Đây là vòng thi xúc động nhất từ đầu đại hội đến giờ!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ và anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cùng rút khăn tay ra lau mắt, khán đài hoạt hình cũng sụt sùi, có chú thỏ đang khóc nức nở vào vai chú sóc.
```
</details>

<details><summary>L278</summary>

```text
HÌNH L278 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kết quả vòng năm! Huy chương đồng: Cá Heo mẹ, giọng nựng con của đại dương!". Bố cục: Bục trao giải: chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái mẹ đứng bậc đồng cùng cá heo con, đeo huy chương đồng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L279</summary>

```text
HÌNH L279 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Huy chương bạc: Thú Mỏ Vịt mẹ, kỹ sư đường hầm 9 lớp cửa! Và huy chương vàng...". Bố cục: chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá mẹ đeo nơ hồng đứng bậc bạc, ôm hai quả trứng; bậc vàng phía trên phủ ánh đèn ấm áp, khán đài nín thở; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tôm Tít bước lên, dài chưa tới một gang tay. Và cuối cùng... Gấu Nước. Kim cân không nhúc nhích. Chiếc cân điện tử cũng không nhúc nhích. Ban tổ chức phải mang tới... một chiếc kính hiển vi.". Bố cục: chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương tí hon đứng giữa chiếc cân bàn khổng lồ trống trơn, nhân viên cúi sát soi kính lúp, màn hình cân hiện số không tròn trĩnh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L280</summary>

```text
HÌNH L280 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thuộc về Lửng Mật! Bà mẹ ngậm con chuyển nhà mỗi 3 ngày, và dạy con suốt hơn một năm trời!". Bố cục: chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần mẹ đứng trên bậc vàng, đeo huy chương vàng, lửng con nhỏ xíu ngồi trên đầu mẹ đội chiếc mũ tốt nghiệp nhỏ, khán đài đứng dậy vỗ tay; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L281</summary>

```text
HÌNH L281 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lửng Mật cuối cùng cũng có điểm! Bảng điểm sau năm vòng: Thú Mỏ Vịt 8 điểm! Cá Heo 4 điểm, Chồn Gulo 4 điểm, Chim Cánh Cụt 4 điểm! Lửng Mật 3 điểm. Rái Cá 3 điểm. Bồ Nông 2 điểm. Koala, Tôm Tít 1 điểm. Gấu Nước vẫn trắng tay.". Bố cục: tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) sáng lên: cột chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá vọt lên cao nhất, ba cột bằng nhau ở vị trí thứ hai, cột chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần lần đầu tiên sáng đèn; chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương đứng dưới chân bảng ngước nhìn cột điểm tắt của mình; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L282</summary>

```text
HÌNH L282 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gấu Nước ngước nhìn bảng điểm, và lần đầu tiên, sinh vật bất tử ấy có vẻ... lo lắng. Vì vòng sáu sẽ không cần đến những siêu năng lực chịu đựng. Vòng sáu cần sự đoàn kết.". Bố cục: Cận cảnh chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương tí hon đứng một mình giữa sân thi đấu rộng mênh mông, cái bóng nhỏ xíu đổ dài, nhìn về phía những tuyển thủ khác đang đứng thành nhóm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L283</summary>

```text
HÌNH L283 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vòng sáu: sức mạnh đồng đội! Một cây làm chẳng nên non, ba cây chụm lại... thì thành một đàn cá heo!". Bố cục: Ba cây nhỏ hoạt hình chụm lại thành ngọn núi, rồi biến hình thành ba chú chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái nhảy lên khỏi mặt nước cùng lúc; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đứng cạnh giơ ngón cái.
```
</details>

<details><summary>L284</summary>

```text
HÌNH L284 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giám khảo chấm ba tiêu chí: biết làm việc với đồng loại, biết hợp tác với loài khác, và quan trọng nhất: biết... nhớ bạn bè.". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ giơ lên ba tấm thẻ có biểu tượng: hai bàn tay nắm nhau, hai con vật khác loài bắt tay, và một bộ não có trái tim nhỏ bên trong.
```
</details>

<details><summary>L285</summary>

```text
HÌNH L285 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cá Heo bước vào sân, và lần này, giám khảo đồng ý cho Cá Heo kể trọn câu chuyện còn dang dở ở vòng ba. Câu chuyện ở thị trấn Laguna, miền Nam nước Brazil.". Bố cục: chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái nhô lên giữa một con kênh dẫn ra biển, hai bên bờ là những ngôi nhà sơn màu tươi sáng, người dân đứng dọc bờ cầm lưới; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L286</summary>

```text
HÌNH L286 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ở đây, mỗi mùa cá đối di cư, những người đánh cá đứng thành hàng dưới nước, nước ngập ngang hông, tay cầm sẵn chiếc lưới quăng tròn. Nhưng họ không nhìn mặt nước. Họ nhìn... cá heo.". Bố cục: Một hàng người đánh cá hoạt hình đội mũ rộng vành đứng dưới nước ngang hông, tay cầm lưới tròn, tất cả cùng chăm chú nhìn về phía chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái đang bơi tới; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L287</summary>

```text
HÌNH L287 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cá Heo dồn đàn cá đối vào sát bờ. Rồi bất ngờ, nó lặn sâu xuống thật nhanh, hoặc quẫy đầu, quẫy đuôi ngay trước mặt người đánh cá. Đó là tín hiệu!". Bố cục: chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái lặn ngoắt xuống nước tạo bọt nước trắng, ngay trước mặt một người đánh cá; người đánh cá mở to mắt, cơ bắp căng ra chuẩn bị quăng lưới; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L288</summary>

```text
HÌNH L288 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Người đánh cá lập tức quăng lưới! Lưới chụp xuống, cá đối hoảng loạn tán loạn, và Cá Heo lao vào bắt những con cá chạy khỏi đàn.". Bố cục: Chiếc lưới tròn bung ra giữa không trung chụp xuống mặt nước, dưới nước đàn cá đối tán loạn, chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái há miệng đớp một con cá đang chạy thoát; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L289</summary>

```text
HÌNH L289 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Năm 2023, các nhà khoa học dùng máy bay không người lái, thiết bị định vị đeo tay và cả micro dưới nước để đo đạc sự hợp tác này. Và các con số khiến họ kinh ngạc.". Bố cục: Một chiếc máy bay không người lái hoạt hình lơ lửng trên con kênh, dưới nước có chiếc micro nhỏ, một người đánh cá đeo đồng hồ định vị trên cổ tay; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gấu Nước dài chưa tới 1mm. Chênh lệch giữa tuyển thủ nặng nhất và nhẹ nhất đại hội lớn đến mức... các nhà toán học của ban tổ chức đã xin nghỉ phép.". Bố cục: Một nhà toán học hoạt hình đeo kính đứng trước tấm bảng đen kín đặc những con số và mũi tên, tóc dựng đứng, ôm đầu, phía sau là hình so sánh chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái khổng lồ và chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương như một chấm nhỏ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L290</summary>

```text
HÌNH L290 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi có Cá Heo ra tín hiệu, người đánh cá có khả năng bắt được cá cao gấp 17 lần, và bắt được số cá nhiều gần gấp 4 lần so với khi không có Cá Heo!". Bố cục: Hai chiếc giỏ cá hoạt hình so sánh: giỏ bên trái gần như trống chỉ có một con cá nhỏ, giỏ bên phải đầy ắp cá đối tràn ra ngoài; chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái nháy mắt bên cạnh giỏ đầy; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L291</summary>

```text
HÌNH L291 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và Cá Heo cũng được lợi: những con cá heo tham gia hợp tác có tỷ lệ sống sót cao hơn khoảng 13%, vì chúng ít phải đi kiếm ăn ở những vùng có lưới đánh bắt nguy hiểm.". Bố cục: chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái bơi an toàn trong con kênh, phía xa ngoài biển là những tấm lưới kéo lớn nguy hiểm có biển báo cấm màu đỏ, chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái quay đầu tránh xa; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L292</summary>

```text
HÌNH L292 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Điều kỳ diệu là sự hợp tác này đã diễn ra ở đây hơn 100 năm, truyền từ đời ông sang đời cháu của cả người lẫn cá heo. Người dân còn đặt tên riêng cho từng chú cá heo quen mặt.". Bố cục: Một ông lão đánh cá hoạt hình râu bạc ngồi bên bờ kể chuyện cho cháu nhỏ, chỉ tay về phía chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái đang nhô lên vẫy vây; phía sau là tấm ảnh cũ đen trắng chụp cảnh y hệt; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L293</summary>

```text
HÌNH L293 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng các nhà khoa học cũng cảnh báo: cá đối đang ít dần, và số lần hợp tác cũng ít dần. Đây là một trong những mối hợp tác hiếm hoi còn sót lại giữa con người và động vật hoang dã. Nếu cá biến mất, tình bạn ấy cũng có thể biến mất theo.". Bố cục: Con kênh vắng vẻ hơn, chỉ còn một người đánh cá già và một chú chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái nhìn nhau buồn bã, mặt nước chỉ có vài con cá nhỏ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L294</summary>

```text
HÌNH L294 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng Cá Heo còn một tuyệt chiêu đồng đội nữa: trí nhớ. Mỗi chú cá heo có một tiếng huýt sáo riêng, hoạt động giống như... một cái tên.". Bố cục: Ba chú chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái bơi cạnh nhau, trên đầu mỗi con là một bong bóng hình nốt nhạc khác nhau, mỗi nốt nhạc một màu riêng như chữ ký âm nhạc; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L295</summary>

```text
HÌNH L295 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Năm 2013, một nhà khoa học đã thu âm tiếng huýt sáo của 53 chú cá heo ở 6 thủy cung, rồi phát lại cho những chú cá heo từng sống chung với chúng... cách đây rất nhiều năm.". Bố cục: Một nhà khoa học hoạt hình cầm chiếc loa chống nước thả xuống bể, bên cạnh là chiếc máy ghi âm cổ có cuộn băng quay; chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái tò mò bơi lại gần; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L296</summary>

```text
HÌNH L296 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Có một chú cá heo cái tên Bailey, sống ở Bermuda. Khi được nghe lại tiếng huýt sáo của người bạn cũ Allie, chú lập tức bơi nhanh đến chiếc loa, lượn quanh, và huýt sáo gọi lại.". Bố cục: chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái cái hào hứng bơi vòng quanh chiếc loa dưới nước, miệng phát ra những nốt nhạc nhỏ, ánh mắt vui mừng; trong bong bóng ký ức là hình ảnh hai chú cá heo con bơi cạnh nhau; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L297</summary>

```text
HÌNH L297 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hai bạn đã xa nhau 20 năm 6 tháng. Đó là trí nhớ xã hội dài nhất từng được ghi nhận ở một loài không phải con người.". Bố cục: Một cuốn lịch hoạt hình lật nhanh từng trang bay tứ tung, ở cuối là hai chú chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái nhìn nhau qua khoảng cách xa, giữa hai con là sợi dây hình nốt nhạc nối liền; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L298</summary>

```text
HÌNH L298 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giám khảo... xin phép lau nước mắt một chút.". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ rút khăn tay ra chấm nước mắt sau cặp kính tròn, mũi đỏ hoe, cây búa gỗ đặt sang một bên.
```
</details>

<details><summary>L299</summary>

```text
HÌNH L299 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyển thủ tiếp theo cũng sở hữu một đội hình huyền thoại: Rái Cá Biển. Khán giả đã biết rái cá nắm tay nhau ngủ thành "bè" để khỏi trôi. Nhưng một chiếc bè có thể lớn đến mức nào?". Bố cục: Một nhóm hàng chục chú chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách nằm ngửa cạnh nhau trên mặt biển giữa đám tảo bẹ, trông như một chiếc bè lông nâu khổng lồ trôi bồng bềnh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cân ký xong! Đủ mười tuyển thủ! Và trước khi vào vòng một, chúng ta cùng xem dự đoán của các chuyên gia.". Bố cục: Mười tuyển thủ đứng thành hàng ngang giữa sân dưới pháo hoa, chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ đứng ngủ gật dựa vào vai chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đứng một bên.
```
</details>

<details><summary>L300</summary>

```text
HÌNH L300 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thông thường mỗi bè có từ 10 đến 100 con. Nhưng ở Alaska từng ghi nhận những chiếc bè khổng lồ có tới hơn 2.000 con Rái Cá Biển nằm cạnh nhau!". Bố cục: Một cảnh nhìn từ trên cao hoạt hình: mặt biển phủ kín hàng ngàn chấm nâu nhỏ li ti là rái cá nằm ngửa, chiếc máy bay nhỏ bay ngang qua chụp ảnh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L301</summary>

```text
HÌNH L301 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và bè rái cá có luật lệ rõ ràng: rái cá đực nằm một bè riêng, rái cá cái và con nhỏ nằm một bè riêng. Một ký túc xá nam, một ký túc xá nữ, ngay giữa đại dương!". Bố cục: Hai chiếc bè rái cá trên mặt biển có tấm biển phao nổi đánh dấu: bè bên trái gồm toàn rái cá to xác có hình biểu tượng mặt trăng xanh, bè bên phải gồm rái cá mẹ ôm rái cá con có biểu tượng trái tim hồng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L302</summary>

```text
HÌNH L302 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyển thủ tiếp theo không phải là đội ở cùng nhau. Đó là cả một thành phố! Chim Cánh Cụt Adélie sống trong những đàn hàng chục ngàn, có khi hàng trăm ngàn cặp vợ chồng.". Bố cục: Toàn cảnh bãi đá Nam Cực hoạt hình chật kín hàng ngàn chú chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ nhỏ li ti đứng cạnh tổ sỏi, như một thành phố đông đúc nhìn từ trên cao; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L303</summary>

```text
HÌNH L303 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ở mũi đất Crozier trên đảo Rốt, các nhà khoa học đếm được khoảng 150.000 cặp chim cánh cụt làm tổ cùng một chỗ. Ồn ào, đông đúc, và... chật chội như phố cổ giờ tan tầm!". Bố cục: Cảnh đông nghịt hoạt hình: chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ chen chúc đi lạch bạch như dòng người giờ tan tầm, có chú đang đứng giữa đường chỉnh nơ, có chú đang cãi nhau vì giẫm chân; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L304</summary>

```text
HÌNH L304 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong một thành phố đông như thế, chim bố và chim mẹ vẫn tìm ra nhau, vẫn tìm ra con mình, chỉ bằng tiếng gọi. Mỗi cặp có một tiếng gọi riêng mà giữa hàng chục ngàn tiếng ồn ào, chúng vẫn nhận ra.". Bố cục: chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ vừa đi biển về, đứng giữa đám đông giơ mỏ cất tiếng gọi, từ xa một chú cánh cụt con lông xám quay đầu lại và chạy lạch bạch về phía bố, giữa hai con là dòng nốt nhạc nối liền; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L305</summary>

```text
HÌNH L305 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và giờ, đến lượt những tuyển thủ thích... làm một mình. Chồn Gulo, Lửng Mật, Tôm Tít. Ba kẻ cô độc nổi tiếng nhất cuộc thi, đứng ở ba góc sân, không ai nhìn ai.". Bố cục: Ba góc sân thi đấu: chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh ở góc tuyết, chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần ở góc cát, chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh ở góc bể nước, ba tuyển thủ quay lưng lại với nhau khoanh tay; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L306</summary>

```text
HÌNH L306 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng giám khảo có một câu hỏi bất ngờ dành cho Tôm Tít: khi hai võ sĩ tôm tít tranh nhau một cái hang, chúng có đánh nhau đến chết không?". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ cúi người về phía bể nước, chỉ cây búa gỗ về phía chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh, chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh giơ hai càng ngẩng lên lắng nghe; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L307</summary>

```text
HÌNH L307 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Câu trả lời của khoa học: không. Các nhà nghiên cứu đã dàn dựng hơn 60 trận tranh hang giữa những chú tôm tít, và thấy chúng đánh nhau theo một nghi thức rất... lịch sự.". Bố cục: Hai chú chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh đứng đối diện nhau trước một cái hang đá, cả hai cúi chào nhau như hai võ sĩ trước trận đấu, một trọng tài hoạt hình nhỏ đứng giữa; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L308</summary>

```text
HÌNH L308 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đầu tiên, dang càng ra dọa nhau! Không ăn thua thì vẫy râu đánh hơi đối thủ! Vẫn không ăn thua, thì mới chuyển sang... đấm!". Bố cục: Chuỗi ba hình nhỏ hoạt hình nối nhau: hai chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh dang càng như võ sĩ khoe cơ, rồi vẫy râu ngửi nhau, rồi tung cú đấm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L309</summary>

```text
HÌNH L309 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng không phải đấm vào mặt. Mà là đấm vào tấm khiên ở đuôi! Con bị đánh cuộn đuôi lại, giơ tấm khiên dày cứng ra đỡ, hai bên thay nhau đấm vào khiên, như hai võ sĩ đấm vào găng của nhau.". Bố cục: Một chú chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh cuộn đuôi lên trước ngực thành tấm khiên tròn cứng có hoa văn, chú kia đấm cú vào tấm khiên tạo tiếng "bốp" hoạt hình, không ai bị thương; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Theo dự đoán, Lửng Mật, Tôm Tít và Gấu Nước là ba ứng cử viên nặng ký nhất. Còn Thú Mỏ Vịt và Koala... chuyên gia chỉ ghi chú đúng một câu: tham gia cho vui.". Bố cục: Màn hình lớn chiếu biểu đồ cột dự đoán: ba cột cao vút có hình đầu chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần, chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh, chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương; hai cột thấp lè tè có hình đầu chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá và chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ; không chữ, không số; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L310</summary>

```text
HÌNH L310 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và mục đích của màn đấm khiên này là để... đo sức nhau. Sau vài cú, con nào nhẹ cân hơn tự hiểu là mình yếu hơn, và lặng lẽ rút lui. Không ai phải chết.". Bố cục: Chú chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh nhỏ hơn thở hổn hển, giơ một càng lên như cờ trắng đầu hàng rồi bơi đi, chú to hơn bước vào hang; hai bên vẫn gật đầu chào nhau lịch sự; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L311</summary>

```text
HÌNH L311 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một võ sĩ có cú đấm mạnh nhất đại dương, nhưng lại biết dùng nó để nói chuyện thay vì để giết nhau. Đúng là võ sĩ có võ đức!". Bố cục: chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh đeo đai đen võ thuật hoạt hình, cúi đầu chào khán giả theo kiểu võ đường, trên tường có tấm biển hình nắm đấm và trái tim; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L312</summary>

```text
HÌNH L312 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn Lửng Mật? Lửng Mật vẫn đi một mình... nhưng như vòng hai đã kể, phía sau nó luôn có 6 con chim ưng bám theo. Giám khảo hỏi: như vậy có tính là đồng đội không?". Bố cục: chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần đứng khoanh tay, phía sau sáu con chim ưng xám đứng thành hàng như dàn đồng ca; bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ nhìn qua kính với vẻ suy tư, tay gõ gõ bút vào cằm.
```
</details>

<details><summary>L313</summary>

```text
HÌNH L313 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giám khảo xin trả lời: không. Có người đi theo mình, nhưng mình không quan tâm tới họ, thì không phải là đồng đội.". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ lắc đầu, gõ búa, giơ tấm thẻ có biểu tượng hai bàn tay nắm nhau bị gạch chéo về phía chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần.
```
</details>

<details><summary>L314</summary>

```text
HÌNH L314 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vừa giành huy chương vàng ở vòng nuôi con, Lửng Mật lại trắng tay ở vòng này. Giỏi chăm con mình, nhưng làm việc với người ngoài thì... chưa biết cách!". Bố cục: chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần đứng trước bảng điểm, mặt đỏ gay, khói bốc lên từ tai, chân đá một viên sỏi nhỏ, lửng con ngồi trên đầu mẹ vỗ vai an ủi; xa xa chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh và chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh che miệng cười; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L315</summary>

```text
HÌNH L315 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kết quả vòng sáu! Huy chương đồng: Rái Cá Biển, với những chiếc bè 2.000 thành viên!". Bố cục: Bục trao giải: chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách nằm ngửa trên bậc đồng đeo thêm một huy chương đồng, tay nắm tay một chú rái cá khác; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L316</summary>

```text
HÌNH L316 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Huy chương bạc: Tôm Tít, võ sĩ biết dùng nắm đấm để... thương lượng hòa bình! Và huy chương vàng...". Bố cục: chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh ở bậc bạc trong bể nước nhỏ đeo huy chương bạc, giơ càng ăn mừng; bậc vàng phía trên đang phủ một tấm màn che bí ẩn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L317</summary>

```text
HÌNH L317 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thuộc về Cá Heo, huy chương vàng thứ hai! Đồng đội của cả con người suốt hơn 100 năm, và là người bạn nhớ tên bạn mình sau 20 năm xa cách!". Bố cục: chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái nhảy vọt lên khỏi bể nước trên bậc vàng, đeo hai huy chương vàng, xung quanh là những người đánh cá Bra-xin hoạt hình vỗ tay hoan hô; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L318</summary>

```text
HÌNH L318 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bảng điểm sau sáu vòng: Thú Mỏ Vịt 8 điểm! Cá Heo bám sát với 7 điểm! Chồn Gulo, Chim Cánh Cụt và Rái Cá cùng 4 điểm. Lửng Mật và Tôm Tít 3 điểm. Bồ Nông 2 điểm, Koala 1 điểm. Gấu Nước: vẫn chưa có điểm!". Bố cục: tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) sáng lên: cột chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá cao nhất, cột chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái sát nút ngay bên cạnh, ba cột bằng nhau ở giữa, cột chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương tắt ngúm; chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá và chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái liếc nhìn nhau đầy cạnh tranh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L319</summary>

```text
HÌNH L319 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng vòng bảy sẽ đảo lộn tất cả. Vì vòng bảy sẽ không chấm năng lực. Vòng bảy là phiên phúc khảo: những tin đồn nổi tiếng nhất về các tuyển thủ sẽ được mang ra kiểm chứng.". Bố cục: Một căn phòng tối hoạt hình, giữa phòng là chiếc bàn có chồng hồ sơ dày, trên cùng là chiếc kính lúp khổng lồ, ánh đèn bàn rọi xuống; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng các chuyên gia đâu phải lúc nào cũng đúng. Đêm nay, mọi con số sẽ được kiểm chứng lại từ đầu. Không có chuyện cũ. Không có huyền thoại.". Bố cục: Cận cảnh chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá lặng lẽ ngước nhìn cột điểm thấp tè của mình trên màn hình, ánh mắt quyết tâm lóe sáng, một giọt mồ hôi chảy trên trán; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L320</summary>

```text
HÌNH L320 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và có những tuyển thủ sắp phát hiện ra rằng... danh tiếng của mình được xây trên một câu chuyện không có thật.". Bố cục: Bóng đen của mười tuyển thủ in trên tường, một vài cái bóng đổ mồ hôi lo lắng, có cái bóng đang lén lút giấu một cuốn truyện tranh sau lưng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L321</summary>

```text
HÌNH L321 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trước vòng bảy, ban tổ chức mở một buổi họp báo. Phóng viên được hỏi bất cứ điều gì. Và các tuyển thủ phải trả lời... bằng sự thật khoa học!". Bố cục: Một phòng họp báo hoạt hình có bàn dài phủ khăn xanh, mười chiếc micro nhỏ xếp hàng, phía dưới là hàng ghế phóng viên giơ tay, đèn flash nháy liên tục; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đứng ở bục điều phối.
```
</details>

<details><summary>L322</summary>

```text
HÌNH L322 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Câu hỏi đầu tiên dành cho Tôm Tít: ở dưới đáy biển sâu, ánh sáng gần như chỉ còn màu xanh lam. Vậy những đốm màu trên người anh có còn ai nhìn thấy không?". Bố cục: Một cô phóng viên hoạt hình đứng dậy cầm micro hỏi, sổ tay trên tay, phía trước là chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh ngồi sau bàn họp báo nhướng mắt lắng nghe; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L323</summary>

```text
HÌNH L323 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Câu trả lời đến từ một lần lặn đêm năm 2002 ở vùng biển Bahamas. Một thợ lặn chiếu đèn xanh xuống một chú tôm tít đang thò đầu khỏi hang, và thấy hai đốm trên người nó... sáng rực lên màu vàng, như hai chiếc đèn pha.". Bố cục: Dưới đáy biển tối đêm hoạt hình, chùm đèn xanh của thợ lặn chiếu vào một chú tôm tít thò đầu khỏi hang cát, hai đốm vàng trên người phát sáng rực rỡ như đèn pha; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L324</summary>

```text
HÌNH L324 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà khoa học giải thích: ở độ sâu khoảng 40 mét, màu vàng gần như biến mất trong làn nước xanh. Nhưng những đốm này có chất phát quang, hấp thụ ánh sáng xanh rồi phát ra ánh sáng vàng. Nhờ vậy, tín hiệu vẫn rõ ràng ở dưới sâu.". Bố cục: Sơ đồ hoạt hình hai chú tôm tít ở hai độ sâu: chú ở nước nông có đốm vàng bình thường, chú ở nước sâu xanh thẫm có đốm vàng vẫn sáng nhờ những mũi tên ánh sáng xanh đi vào và ánh sáng vàng đi ra; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L325</summary>

```text
HÌNH L325 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và những đốm sáng ấy được dùng trong màn dọa nạt đối thủ. Tôm Tít dang càng, khoe đốm vàng phát sáng như muốn nói: "Đây là nhà của tôi, tránh ra!". Đây là trường hợp đầu tiên được ghi nhận về việc một sinh vật biển dùng ánh sáng phát quang để ra tín hiệu.". Bố cục: chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh dang hai càng trước cửa hang, hai đốm vàng trên người sáng rực như biển báo, một chú tôm tít khác đang lùi lại sợ hãi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L326</summary>

```text
HÌNH L326 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tôm Tít trả lời xong, dang càng khoe đốm sáng ngay giữa phòng họp báo. Các phóng viên phải... đeo kính râm!". Bố cục: Cả hàng ghế phóng viên hoạt hình đồng loạt đeo kính râm, chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh trên bàn họp báo phát sáng hai đốm vàng chói lóa, anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng giơ tay che mắt.
```
</details>

<details><summary>L327</summary>

```text
HÌNH L327 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Câu hỏi thứ hai dành cho Chim Bồ Nông: người ta đồn có một loài bồ nông lao đầu từ trên cao xuống biển để bắt cá. Lao mạnh như vậy, anh không đau đầu sao?". Bố cục: Một anh phóng viên hoạt hình đeo kính cận đứng dậy hỏi, cầm máy ghi âm chĩa về phía chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L328</summary>

```text
HÌNH L328 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đó là anh họ của Bồ Nông, loài bồ nông nâu ở châu Mỹ, loài bồ nông duy nhất săn mồi bằng cú bổ nhào ngoạn mục. Từ độ cao có khi tới hơn 20 mét, nó gập cánh và lao thẳng xuống biển như một mũi tên.". Bố cục: Một chú bồ nông nâu hoạt hình gập cánh lao thẳng từ trên trời xuống mặt biển như mũi tên, phía dưới là đàn cá nhỏ lấp lánh, nước bắn tung tóe; chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn đứng trên bờ chỉ tay giới thiệu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L329</summary>

```text
HÌNH L329 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bí mật nằm ở những túi khí dưới da. Khi đập xuống mặt nước, các túi khí này đệm lại cú va chạm như túi khí ô tô, rồi giúp nó nổi bật trở lên như một cái nút chai.". Bố cục: Hình mặt cắt hoạt hình cơ thể bồ nông nâu có những túi khí nhỏ màu xanh nhạt phồng lên dưới da như những quả bóng, bên cạnh là hình túi khí ô tô bung ra để so sánh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chỉ có khoa học, chỉ có những bằng chứng được đo đạc thật... và một chiếc vương miện.". Bố cục: Chiếc vương miện bé xíu trên bệ đá giữa sân phát sáng rực rỡ, mười cái bóng tuyển thủ in dài trên mặt sân hướng về phía nó; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L330</summary>

```text
HÌNH L330 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Câu hỏi thứ ba dành cho Lửng Mật: ở Nam Phi, người ta còn gọi anh bằng một cái tên khác. Anh có biết đó là tên gì không?". Bố cục: Cô phóng viên đứng dậy lần nữa, giơ một tấm thẻ có hình dấu chấm hỏi, chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần ngồi khoanh tay sau bàn họp báo nhướng mày; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L331</summary>

```text
HÌNH L331 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đó là tên "Ratel". Những người định cư Hà Lan ở Nam Phi đặt tên này theo tiếng gầm gừ lục cục rất đặc trưng mà Lửng Mật phát ra mỗi khi nổi giận. Nghe như tiếng... ai đó đang lắc một hộp sỏi!". Bố cục: chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần gầm gừ, từ miệng bay ra những hình nốt nhạc gai góc hình viên sỏi, bên cạnh vẽ một chiếc hộp thiếc đầy sỏi đang được lắc mạnh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L332</summary>

```text
HÌNH L332 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn ở Uganda, người Ganda gọi nó bằng một cái tên có nghĩa là "kẻ không nghe thấy", vì đôi tai của Lửng Mật rất nhỏ, gần như không nhìn thấy.". Bố cục: Cận cảnh đầu chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần hoạt hình với đôi tai nhỏ xíu gần như lẫn vào lớp lông, một chú chim nhỏ cầm loa thét vào tai nó mà chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần vẫn thản nhiên; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L333</summary>

```text
HÌNH L333 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: ""Kẻ không nghe thấy"... Có lẽ đó là lý do vì sao Lửng Mật chưa bao giờ nghe lời ai can ngăn!". Bố cục: chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần đi thẳng qua tấm biển báo cấm có hình bàn tay đỏ, các con vật khác phía sau giơ tay ra can ngăn hoảng hốt, còn nó vẫn tỉnh bơ bước tiếp; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L334</summary>

```text
HÌNH L334 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Câu hỏi thứ tư dành cho Chồn Gulo: tên khoa học của anh có nghĩa là gì?". Bố cục: Anh phóng viên đeo kính cận đứng dậy, cầm cuốn từ điển La-tinh dày cộp, chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh ngồi sau bàn họp báo đang gặm một khúc xương; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L335</summary>

```text
HÌNH L335 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tên khoa học của Chồn Gulo bắt nguồn từ một chữ La-tinh có nghĩa là... "kẻ tham ăn".". Bố cục: Cận cảnh chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh hoạt hình khựng lại giữa lúc gặm khúc xương, quay mặt nhìn vào ống kính với vẻ mặt bị bắt quả tang; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L336</summary>

```text
HÌNH L336 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và cả phòng họp báo nhìn xuống khúc xương trên tay Chồn Gulo... Chồn Gulo lặng lẽ giấu khúc xương ra sau lưng. Không có gì để bàn thêm!". Bố cục: chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh giấu khúc xương ra sau lưng, huýt sáo nhìn lên trần nhà, cả phòng phóng viên cười ồ, đèn flash nháy liên tục; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L337</summary>

```text
HÌNH L337 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng các nhà khoa học cho rằng cái tên ấy có phần oan. Sống ở nơi lạnh giá, thức ăn khan hiếm, việc ăn được mọi thứ tìm thấy là một chiến lược sinh tồn chứ không phải tính xấu.". Bố cục: chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh đứng giữa vùng tuyết trắng mênh mông chỉ có vài dấu chân thưa thớt, trên tay là một miếng thịt nhỏ, ánh mắt cảnh giác nhìn quanh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L338</summary>

```text
HÌNH L338 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Câu hỏi cuối cùng dành cho Koala: có người nói túi của Koala mẹ mở ngược xuống dưới. Như vậy Koala con không bị rơi ra ngoài sao?". Bố cục: Cô phóng viên đứng dậy hỏi, vẻ mặt lo lắng thật sự, chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ ngồi sau bàn họp báo đang lim dim ngủ thì giật mình mở mắt; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L339</summary>

```text
HÌNH L339 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đây là một hiểu lầm rất phổ biến. Theo Quỹ Koala Úc, khi mới sinh con, túi của Koala mẹ không mở ngược lên cũng không mở ngược xuống, mà mở thẳng ra phía trước, ở giữa bụng.". Bố cục: Sơ đồ hoạt hình bụng của chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ mẹ nhìn nghiêng, miệng túi nằm giữa bụng hướng ra phía trước, bên trong có chú Cô-a-la con bé xíu bám vào; một mũi tên chỉ ra phía trước; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vòng một bắt đầu ngay sau đây, và nó sẽ khiến các tuyển thủ... hoặc là đóng băng, hoặc là chín luôn!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng chỉ tay về phía cổng sân vận động chia đôi: một nửa phủ băng tuyết xanh lạnh buốt có nhũ băng, một nửa tỏa nắng đỏ rực như sa mạc có ảo ảnh hơi nóng.
```
</details>

<details><summary>L340</summary>

```text
HÌNH L340 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Miệng túi có một cơ vòng rất khỏe mà mẹ có thể thắt chặt lại, giữ cho con không rơi ra ngoài. Chỉ khi con đã lớn và thò người ra ngoài, sức nặng của con mới kéo miệng túi trễ xuống, trông như túi... mở ngược.". Bố cục: Chú Cô-a-la con lớn hơn thò nửa người ra khỏi túi, kéo miệng túi trễ xuống, chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ mẹ vẫn ôm cây bình thản; bên cạnh vẽ một chiếc túi có dây rút được thắt chặt để minh họa cơ vòng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L341</summary>

```text
HÌNH L341 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hồi nhỏ cháu toàn thò đầu ra ngắm cây đó ạ! Mẹ cháu bảo... đừng có thò ra nhiều quá, nặng lắm!". Bố cục: chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ cười tươi giơ tay khoe, trong bong bóng ký ức là hình chú Cô-a-la con thò đầu ra khỏi túi mẹ ngắm cành lá, mẹ nhăn mặt vì nặng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L342</summary>

```text
HÌNH L342 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Xin cảm ơn các tuyển thủ. Và nhắn riêng tuyển thủ Chồn Gulo: phòng họp báo không cho phép mang xương vào nhé!". Bố cục: Cô phóng viên mỉm cười cúi chào, phía sau chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh đang lén nhặt lại khúc xương dưới gầm bàn, giả vờ như không có chuyện gì; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L343</summary>

```text
HÌNH L343 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Buổi họp báo kết thúc! Năm câu hỏi, năm câu trả lời, và không ai phải... nói dối! Và giờ, đúng như tên gọi, chúng ta bước sang vòng thi về sự thật: phiên phúc khảo tin đồn!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đóng cuốn sổ ghi chép, các phóng viên đứng dậy vỗ tay, các tuyển thủ rời bàn họp báo đi về phía một cánh cửa gỗ lớn có hình chiếc kính lúp.
```
</details>

<details><summary>L344</summary>

```text
HÌNH L344 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vòng bảy: phúc khảo tin đồn. Luật chơi: giám khảo đọc một tin đồn nổi tiếng về tuyển thủ. Khoa học sẽ xác nhận hoặc bác bỏ. Tin đồn đúng: tuyển thủ được điểm. Tin đồn sai mà tuyển thủ dám thừa nhận: cũng được điểm!". Bố cục: Phòng phúc khảo hoạt hình như phòng xử án nhỏ: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ ngồi giữa sau bàn cao, trước mặt là chiếc cân công lý, một bên đĩa cân là cuốn sách khoa học, bên kia là cuốn truyện tranh; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đứng một bên cầm micro.
```
</details>

<details><summary>L345</summary>

```text
HÌNH L345 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hồ sơ phúc khảo số một, và lần này kênh Vẽ Chuyện Hoang Dã tự phúc khảo chính mình! Trong tập phim về Tôm Tít, chúng tôi kể mắt nó có tới 16 loại tế bào cảm thụ ánh sáng. Và tin đồn đi kèm là: "Tôm Tít nhìn màu sắc rực rỡ hơn con người gấp nhiều lần".". Bố cục: Một tấm áp phích mạng xã hội hoạt hình phóng to đôi mắt chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh, bên trong là cầu vồng rực rỡ nhiều màu hơn hẳn, bên cạnh là đôi mắt người chỉ có ba màu đỏ xanh lá xanh dương; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L346</summary>

```text
HÌNH L346 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Con số 16 là đúng, và trong đó có 12 loại chuyên cảm nhận màu, trong khi mắt người chỉ có ba. Nhưng năm 2014, các nhà khoa học ở Úc làm một thí nghiệm đơn giản: dạy tôm tít nhận một màu để được thưởng đồ ăn, rồi cho chọn giữa hai màu gần giống nhau.". Bố cục: Một bể thí nghiệm hoạt hình có hai sợi đèn màu, một vàng một cam rất gần nhau, chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh đứng giữa nhìn qua lại bối rối, một nhà khoa học cầm miếng tôm thưởng chờ bên cạnh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L347</summary>

```text
HÌNH L347 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kết quả bất ngờ: khi hai màu khác nhau ít, kiểu như vàng với cam, Tôm Tít bắt đầu chọn sai. Có lúc chọn đúng không hơn gì... đoán bừa!". Bố cục: chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh nhắm mắt chỉ càng bừa vào một sợi đèn, trên đầu là đồng xu đang tung lên quay quay, nhà khoa học vỗ trán; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L348</summary>

```text
HÌNH L348 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hóa ra 12 loại tế bào ấy không phối hợp để phân biệt sắc độ như mắt người. Mỗi loại làm việc riêng, giống như 12 ngăn kéo phân loại màu: nhanh, nhưng không tinh.". Bố cục: Hình minh họa hoạt hình: mắt chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh như một chiếc tủ có mười hai ngăn kéo nhiều màu, mỗi ngăn bắt một màu rơi vào; bên cạnh là não người như một họa sĩ đang pha trộn màu tinh tế trên bảng màu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L349</summary>

```text
HÌNH L349 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà khoa học cho rằng cách nhìn này giúp Tôm Tít nhận ra màu cực nhanh mà không cần não xử lý nhiều, rất hợp với cuộc sống chớp nhoáng dưới đáy biển.". Bố cục: chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh quét mắt qua một rạn san hô, những đốm màu được đánh dấu tức thì như đèn đỏ đèn xanh, một con cá nhỏ vừa ló ra đã bị phát hiện; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vòng một: thử thách nóng và lạnh! Câu hỏi rất đơn giản: khi trời nóng như lò nướng, hoặc lạnh như tủ đá, cơ thể bạn làm gì để sống sót?". Bố cục: Sân thi đấu được chia đôi: nửa trái là sa mạc đỏ rực có mặt trời chói chang và ảo ảnh hơi nóng, nửa phải là băng tuyết xanh trắng có nhũ băng; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đứng ngay đường ranh giữa hai nửa, một bên tóc dựng vì nóng, một bên râu đóng băng.
```
</details>

<details><summary>L350</summary>

```text
HÌNH L350 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Phán quyết: tin đồn "nhìn màu đẹp hơn người" là sai. Nhưng Tôm Tít có một cách nhìn màu độc nhất vô nhị. Tuyển thủ có chấp nhận không?". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gõ búa, giơ tấm thẻ có biểu tượng con mắt kèm dấu chấm hỏi.
```
</details>

<details><summary>L351</summary>

```text
HÌNH L351 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tôm Tít gật đầu. Nó không cần nhìn màu đẹp hơn người. Nó chỉ cần nhìn thấy con mồi nhanh hơn con mồi kịp chạy!". Bố cục: chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh khoanh hai càng gật đầu đầy tự tin, đeo chiếc kính râm hình mắt kép nhiều ngăn màu sắc; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L352</summary>

```text
HÌNH L352 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hồ sơ phúc khảo số hai: Lửng Mật và chim dẫn mật. Như các bạn đã nghe ở vòng ba, khoa học hiện nay nói rằng: chưa có bằng chứng rõ ràng.". Bố cục: Hồ sơ màu đỏ có ảnh chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần và một chú chim nhỏ màu nâu được đặt lên bàn, có dấu đóng hình chiếc kính lúp và dấu chấm hỏi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L353</summary>

```text
HÌNH L353 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giám khảo hỏi Lửng Mật: tuyển thủ có thừa nhận câu chuyện chim dẫn đường là chưa được chứng minh không?". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ cúi người nhìn thẳng vào chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần qua cặp kính tròn, cả căn phòng im phăng phắc, một giọt mồ hôi chảy trên trán anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng.
```
</details>

<details><summary>L354</summary>

```text
HÌNH L354 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lửng Mật im lặng một lúc lâu... rồi gật đầu. Gã giang hồ nổi tiếng không bao giờ lùi bước, lần đầu tiên chịu nhận là: ừ, chuyện đó chưa ai chứng minh được!". Bố cục: chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần quay mặt đi, bĩu môi, nhưng vẫn gật đầu miễn cưỡng, một tay giơ lên như đầu hàng; khán đài sửng sốt há hốc mồm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L355</summary>

```text
HÌNH L355 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Phán quyết: tin đồn chưa được chứng minh. Nhưng tuyển thủ dám thừa nhận. Giám khảo ghi nhận tinh thần... trung thực!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ mỉm cười gõ búa nhẹ, đặt một ngôi sao vàng nhỏ cạnh hình đầu chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần trên bàn.
```
</details>

<details><summary>L356</summary>

```text
HÌNH L356 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hồ sơ phúc khảo số ba: Gấu Nước. Tin đồn: "Năm 2019, tàu vũ trụ Beresheet của Israel rơi xuống Mặt Trăng, và hàng ngàn con Gấu Nước trên tàu hiện vẫn đang nằm ngủ trên Mặt Trăng, chờ ngày được hồi sinh".". Bố cục: Mặt Trăng hoạt hình xám bạc có miệng núi lửa, giữa một miệng núi lửa là xác con tàu vũ trụ nhỏ vỡ nát, những chấm nhỏ li ti rải rác xung quanh; Trái Đất xanh lơ lửng phía xa; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L357</summary>

```text
HÌNH L357 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khán giả của kênh còn nhớ: gấu nước từng bị bắn ra khỏi nòng súng cao tốc mà vẫn sống. Nhưng chính thí nghiệm ấy còn một phần hai ít ai kể. Năm 2020 mốt, các nhà khoa học Anh tăng tốc độ bắn để tìm ra... giới hạn cuối cùng.". Bố cục: Một khẩu pháo khí dài hoạt hình trong phòng thí nghiệm, hai nhà khoa học đeo kính bảo hộ đứng cạnh, trên bàn là chiếc đạn nhựa nhỏ có chú chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương đang ngủ bên trong; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L358</summary>

```text
HÌNH L358 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Họ cho Gấu Nước ngủ đông, nhét vào viên đạn nhựa, rồi bắn vào bao cát, mỗi lần một nhanh hơn! 500 mét mỗi giây! 700! 800! 900!". Bố cục: Viên đạn nhựa hoạt hình bay vèo qua những vòng đo tốc độ phát sáng, đâm vào bao cát tung bụi, chiếc đồng hồ đo tốc độ chạy vọt lên; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L359</summary>

```text
HÌNH L359 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kết quả: đến khoảng 825m mỗi giây, Gấu Nước vẫn sống. Nhưng chỉ nhích lên khoảng 900 mét mỗi giây, các nhà khoa học chỉ còn tìm thấy... những mảnh vụn. Siêu nhân cũng có giới hạn.". Bố cục: chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương bò ra khỏi bao cát, phủi bụi, choáng váng nhưng vẫn vẫy tay chào; bên cạnh là biển báo tốc độ có vạch giới hạn màu đỏ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ban giám khảo không chấm ai to khỏe nhất. Ban giám khảo chấm ai thông minh nhất trong việc điều khiển nhiệt độ của chính mình.". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ cầm một chiếc nhiệt kế khổng lồ như cây gậy chỉ huy, trước mặt là bảng chấm điểm có biểu tượng bộ não và nhiệt kế (không chữ).
```
</details>

<details><summary>L360</summary>

```text
HÌNH L360 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và cú va chạm khi tàu Beresheet rơi xuống Mặt Trăng tạo ra áp lực mạnh hơn rất nhiều so với giới hạn ấy. Kết luận của nhóm nghiên cứu: những chú Gấu Nước trên tàu gần như chắc chắn đã không sống sót.". Bố cục: Trên mặt Trăng xám bạc, một chiếc mũ phi hành gia tí hon nằm lặng lẽ giữa đống đổ nát của con tàu, một bông hoa nhỏ hoạt hình đặt bên cạnh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L361</summary>

```text
HÌNH L361 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Phán quyết: tin đồn Gấu Nước đang ngủ trên Mặt Trăng... khả năng rất cao là sai.". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ cởi kính ra, khẽ cúi đầu, gõ búa thật nhẹ, ánh đèn trong phòng dịu xuống.
```
</details>

<details><summary>L362</summary>

```text
HÌNH L362 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng khoan, Gấu Nước tỉnh dậy từ tủ đông và giơ tay xin phát biểu: "Tôi không bất tử. Tôi chỉ... rất, rất cứng". Và giám khảo đánh giá cao: dám nhận giới hạn của mình, đó cũng là một kiểu sức mạnh!". Bố cục: chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương đứng trên bục phát biểu tí hon, giơ một chân lên xin nói, sau lưng là biểu đồ tốc độ có mũi tên vượt qua hình chiếc máy bay phản lực; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L363</summary>

```text
HÌNH L363 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hồ sơ phúc khảo số bốn: Chim Bồ Nông. Tin đồn này đã có từ hơn 1.000 năm trước. Người xưa tin rằng: khi không còn thức ăn, Bồ Nông mẹ sẽ tự mổ ngực mình, lấy máu nuôi con.". Bố cục: Một bức tranh kính màu nhà thờ cổ hoạt hình vẽ con bồ nông đứng trên tổ, cúi đầu mổ vào ngực, bên dưới là ba chú chim non há mỏ; ánh sáng chiếu xuyên qua kính màu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L364</summary>

```text
HÌNH L364 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hình ảnh này nổi tiếng đến mức xuất hiện trên huy hiệu, trên cửa kính nhà thờ, trên biểu tượng của nhiều trường đại học ở châu Âu.". Bố cục: Một bức tường hoạt hình treo nhiều tấm khiên huy hiệu cổ khác nhau, tấm nào cũng có hình con bồ nông mổ ngực cho con ăn (không chữ); KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L365</summary>

```text
HÌNH L365 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khoa học trả lời: không có chuyện đó. Khi cho con ăn, Bồ Nông mẹ ép cái túi họng vào ngực để đẩy cá đã nuốt ra cho con. Nhìn từ xa, trông như nó đang mổ vào ngực mình.". Bố cục: Cảnh thật hoạt hình: chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn mẹ cúi mỏ xuống ép túi họng vào ngực, mở mỏ cho chú bồ nông con chui đầu vào bên trong túi họng lấy cá; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L366</summary>

```text
HÌNH L366 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thêm nữa, đầu mỏ của một số loài bồ nông có màu đỏ, và có loài túi họng chuyển sang đỏ thẫm vào mùa sinh sản. Người xưa nhìn thấy màu đỏ ở ngực... thế là thêu dệt thành chuyện máu!". Bố cục: Cận cảnh mỏ chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn có chóp mỏ đỏ và túi họng đỏ hồng, một người xưa hoạt hình đội mũ trùm đầu nhìn qua bụi rậm, mắt mở to kinh hãi, tưởng tượng ra cảnh máu trong bong bóng suy nghĩ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L367</summary>

```text
HÌNH L367 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Phán quyết: tin đồn sai. Nhưng giám khảo ghi nhận: Bồ Nông là loài chim có biểu tượng tình mẫu tử... dễ thương nhất lịch sử, dù là nhờ hiểu lầm!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gõ búa rồi mỉm cười, giơ tấm thẻ có hình trái tim nhỏ.
```
</details>

<details><summary>L368</summary>

```text
HÌNH L368 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hồ sơ phúc khảo số năm, và là hồ sơ cuối cùng: Gấu Koala. Tin đồn: "Koala chỉ lấy nước từ lá, ngoài những ngày nắng nóng khắc nghiệt thì gần như không bao giờ uống".". Bố cục: Một cuốn sách cổ hoạt hình mở ra trang có hình chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ ôm chiếc lá to, bên cạnh là ly nước bị gạch chéo và chiếc lông vũ chấm mực; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L369</summary>

```text
HÌNH L369 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vòng một đã trả lời rồi! Năm 2020, khoa học đã ghi nhận 46 lần Koala hoang dã liếm nước mưa từ thân cây, kể cả những ngày trời không hề nóng. Koala uống thường xuyên hơn chúng ta tưởng!". Bố cục: chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ ôm thân cây thè lưỡi liếm nước mưa chảy dọc thân, mắt nhắm tận hưởng, xung quanh có những giọt mưa lấp lánh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Phần thi nóng mở màn. Và người đầu tiên bước vào sân là một tuyển thủ mà ai cũng nghĩ là... sẽ ngủ gật ngay lập tức.". Bố cục: Nửa sân sa mạc nóng rực, chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ đứng đơ trên cát, mồ hôi nhễ nhại, tay cầm chiếc quạt giấy nhỏ, mặt ngơ ngác nhìn mặt trời; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L370</summary>

```text
HÌNH L370 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cháu có uống mà! Có điều... cháu chỉ uống khi trời mưa thôi ạ.". Bố cục: chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ giơ tay phát biểu, đội chiếc mũ len nhỏ có quả bông, ánh mắt ngây thơ thành thật; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L371</summary>

```text
HÌNH L371 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Phán quyết: tin đồn "gần như không bao giờ uống" là chưa đúng. Và Koala chính là tuyển thủ giúp khoa học sửa lại một hiểu lầm trăm năm!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gõ búa dứt khoát, rồi gạch chéo một dòng trong cuốn sách cổ bằng bút đỏ, đặt ngôi sao vàng cạnh hình đầu chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ.
```
</details>

<details><summary>L372</summary>

```text
HÌNH L372 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kết quả vòng bảy, và đây là vòng có kết quả bất ngờ nhất đêm nay! Huy chương đồng: Gấu Nước, sinh vật siêu cứng dám thừa nhận mình không bất tử!". Bố cục: Bục trao giải: chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương tí hon đứng trên bậc đồng, phải đứng trên một chiếc ghế nhỏ mới với tới huy chương đồng, cười rạng rỡ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L373</summary>

```text
HÌNH L373 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Huy chương bạc: Koala, người giúp khoa học sửa sai!". Bố cục: chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ đứng trên bậc bạc ôm huy chương bạc vào lòng như ôm gối, mặt vừa ngơ ngác vừa vui; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L374</summary>

```text
HÌNH L374 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và huy chương vàng vòng bảy thuộc về... Lửng Mật, huy chương vàng thứ hai! Vì lần đầu tiên trong lịch sử, gã giang hồ chịu nhận mình... chưa chắc đúng!". Bố cục: chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần đứng trên bậc vàng, đeo hai huy chương vàng, mặt vừa ngượng vừa sung sướng, khán đài vỡ òa vỗ tay, sáu con chim ưng xám tung pháo giấy từ trên trời; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L375</summary>

```text
HÌNH L375 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bảng điểm sau bảy vòng: Thú Mỏ Vịt 8 điểm! Cá Heo 7 điểm! Lửng Mật bứt lên mạnh mẽ với 6 điểm! Chồn Gulo, Chim Cánh Cụt, Rái Cá 4 điểm. Tôm Tít và Koala 3 điểm. Bồ Nông 2 điểm, Gấu Nước 1 điểm.". Bố cục: tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) sáng lên: ba cột chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá, chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái, chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần cao sát nhau ở đầu bảng, các cột khác thấp hơn; khán đài nín thở; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L376</summary>

```text
HÌNH L376 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ba tuyển thủ dẫn đầu chỉ cách nhau đúng 2 điểm! Chỉ còn một vòng cuối. Và vòng cuối có điểm nhân đôi: vàng 6 điểm, bạc 4 điểm, đồng 2 điểm.". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ lật một tấm bảng mới, trên đó ba chiếc huy chương vàng bạc đồng đều có biểu tượng nhân đôi phát sáng; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng hít một hơi thật sâu.
```
</details>

<details><summary>L377</summary>

```text
HÌNH L377 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Câu hỏi của vòng chung kết không phải là ai mạnh nhất. Mà là: ai đã giúp ích cho loài người nhiều nhất.". Bố cục: Một chiếc bàn tròn hoạt hình giữa sân khấu, trên bàn đặt một quả địa cầu nhỏ và một trái tim đỏ phát sáng, mười cái bóng tuyển thủ đứng vây quanh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L378</summary>

```text
HÌNH L378 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trước khi bước vào vòng chung kết, ban tổ chức có một bất ngờ: lễ trao giải phụ! Những giải này không tính điểm, nhưng mỗi giải là một kỷ lục có thật mà khán giả xứng đáng được biết.". Bố cục: Một sân khấu nhỏ hoạt hình bên cạnh sân chính, trang trí bóng bay và dải ruy băng, trên bàn là hàng cúp nhỏ đủ hình dáng (không chữ); anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đứng sau bục cầm phong bì.
```
</details>

<details><summary>L379</summary>

```text
HÌNH L379 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giải phụ thứ nhất: tuyển thủ có thành viên sống thọ nhất! Và giải thuộc về... Cá Heo! Mời khán giả làm quen với bà cụ Nicklo.". Bố cục: Một chú chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái cái già có vây lưng sứt một vết nhỏ, đeo cặp kính lão tròn, đội chiếc mũ len, bơi chậm rãi giữa vịnh biển, xung quanh là những chú cá heo nhỏ hơn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hồ sơ tuyển thủ Gấu Koala. Bộ lông: dày. Nơi ở: trên cây, không có hang, không có điều hòa. Kế hoạch chống nóng: chưa rõ.". Bố cục: Một tấm hồ sơ kẹp giấy hoạt hình có ảnh chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ ở góc, bên dưới là ba biểu tượng: bộ lông, cái cây, chiếc máy điều hòa bị gạch chéo đỏ (không chữ); KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L380</summary>

```text
HÌNH L380 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nicklo là một cô cá heo hoang dã sống ở vịnh Sarasota, bang Florida. Một nhóm nghiên cứu đã theo dõi cá heo ở vịnh này từ năm 1970, và họ đã nhìn thấy Nicklo hơn 820 lần.". Bố cục: Một chiếc thuyền nghiên cứu hoạt hình trên vịnh, nhà khoa học cầm máy ảnh có ống kính dài chụp vây lưng của chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái già, trên thuyền là cuốn album dày cộp toàn ảnh vây lưng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L381</summary>

```text
HÌNH L381 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Để biết tuổi của cô, các nhà khoa học đã đếm các lớp vân trên một chiếc răng, giống như đếm vòng gỗ trên thân cây. Và lần cuối cùng Nicklo được nhìn thấy, vào năm 2017, cô đã 67 tuổi.". Bố cục: Hình phóng to hoạt hình mặt cắt một chiếc răng cá heo có những vòng vân đồng tâm như vòng gỗ, bên cạnh là mặt cắt một thân cây có vòng tuổi để so sánh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L382</summary>

```text
HÌNH L382 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nicklo là cá heo hoang dã sống thọ nhất từng được ghi nhận. Cô sinh ít nhất 4 con, con út ra đời khi cô đã 48 tuổi. Và đứa con út ấy sau này cũng có con, nối dài ba thế hệ trong cùng một vịnh biển.". Bố cục: Ba thế hệ chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái bơi nối đuôi nhau trong vịnh: bà Ních-lô đeo kính lão đi đầu, con gái ở giữa, cháu nhỏ ở cuối, ánh hoàng hôn ấm áp trên mặt nước; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L383</summary>

```text
HÌNH L383 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giám khảo xin cúi đầu chào bà cụ Nicklo. 67 năm giữa biển khơi, quả là một hành trình sinh tồn đáng nể.". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ đứng dậy, bỏ mũ ra cúi đầu kính cẩn, tay đặt lên ngực.
```
</details>

<details><summary>L384</summary>

```text
HÌNH L384 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giải phụ thứ hai: thọ nhất trong nhóm... nhỏ con. Và giải thuộc về Thú Mỏ Vịt! Năm 2023, ở một con suối nhỏ gần thành phố Melbourne, nước Úc, các nhà nghiên cứu bắt lại một chú Thú Mỏ Vịt đực đã được gắn thẻ từ hơn 20 năm trước.". Bố cục: Một con suối nhỏ hoạt hình ven thành phố, nhà nghiên cứu cầm máy quét nhỏ đưa lại gần chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá già có hàng lông mày bạc, máy quét kêu "bíp" và hiện biểu tượng ngôi sao; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L385</summary>

```text
HÌNH L385 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chú được gắn thẻ khi mới khoảng một tuổi, và khi bị bắt lại, chú đã 24 tuổi. Đây là Thú Mỏ Vịt hoang dã sống thọ nhất từng được ghi nhận, vượt kỷ lục cũ 21 tuổi.". Bố cục: chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá già đội chiếc mũ sinh nhật nhỏ, trước mặt là chiếc bánh kem cắm nến, bên cạnh có một tấm bảng hai cột so sánh: cột cũ thấp hơn, cột mới cao hơn (không chữ); KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L386</summary>

```text
HÌNH L386 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong khi đó, ở sa mạc Kalahari, Lửng Mật hoang dã thường chỉ sống khoảng 3-8 năm. Gã giang hồ dũng cảm nhất đại hội... lại có cuộc đời khá ngắn ngủi.". Bố cục: chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần ngồi trên mỏm đá sa mạc nhìn hoàng hôn, bên cạnh là chiếc đồng hồ cát nhỏ, vẻ mặt trầm ngâm nhưng không hề sợ hãi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L387</summary>

```text
HÌNH L387 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giải phụ thứ ba: thợ lặn chăm chỉ nhất! Và lại là Thú Mỏ Vịt! Ở một hồ nước trên núi ở Tasmania, các nhà khoa học đã gắn thiết bị đo độ sâu lên 11 chú Thú Mỏ Vịt và ghi lại gần 90.000 lần lặn.". Bố cục: Mặt hồ trên núi hoạt hình phủ sương sớm, bên dưới là những đường lặn ngoằn ngoèo vẽ chi chít như bức tranh, mỗi đường kết thúc ở một chú chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá nhỏ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L388</summary>

```text
HÌNH L388 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi lần lặn trung bình chỉ khoảng 31 giây! Ngoi lên thở 10 giây, rồi lại lặn tiếp! Trung bình 75 lần mỗi giờ! Và có những chuyến kiếm ăn, nó lặn tới 1.600 lần liên tục!". Bố cục: chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá lặn xuống, ngoi lên, lặn xuống, ngoi lên như chiếc pít-tông, bên cạnh là bộ đếm số hoạt hình đang nhảy liên tục, một chú vịt bên cạnh nhìn chóng cả mặt; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L389</summary>

```text
HÌNH L389 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giải phụ thứ tư: lò sưởi bí ẩn nhất! Và giải thuộc về Rái Cá Biển. Khán giả của kênh đã biết Rái Cá đốt năng lượng rất nhanh để giữ ấm. Nhưng suốt nhiều chục năm, không ai biết chính xác hơi ấm ấy được tạo ra ở đâu trong cơ thể.". Bố cục: chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách nằm ngửa trên mặt nước lạnh, quanh người tỏa ra vầng hơi ấm màu cam, trên đầu là dấu chấm hỏi to, một nhà khoa học hoạt hình cầm đèn pin soi khắp người rái cá tìm kiếm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng các nhà khoa học ở Úc đã phát hiện ra một bí mật mà chính Koala giữ kín suốt hàng triệu năm.". Bố cục: Hai nhà khoa học hoạt hình đội mũ rộng vành đứng dưới gốc cây, chĩa chiếc máy ảnh nhiệt to bản lên ngọn cây nơi chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ đang ngồi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L390</summary>

```text
HÌNH L390 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Năm 2020 mốt, các nhà khoa học lấy mẫu cơ bắp của 21 chú Rái Cá Biển, từ con non đến con trưởng thành, và đo cách các tế bào cơ sử dụng ô-xy.". Bố cục: Phòng thí nghiệm hoạt hình có chiếc máy đo hô hấp tế bào với những ống nghiệm nhỏ, trên màn hình là hình tế bào cơ phóng to có những nhà máy năng lượng tí hon bên trong; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L391</summary>

```text
HÌNH L391 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và họ phát hiện ra: những nhà máy năng lượng tí hon trong tế bào cơ của Rái Cá bị... rò rỉ, có chủ đích. Thay vì biến hết năng lượng thành sức để cử động, chúng để một phần lớn thoát ra dưới dạng nhiệt. Cơ bắp sưởi ấm cơ thể mà không cần cử động!". Bố cục: Hình hoạt hình bên trong tế bào cơ: một nhà máy năng lượng nhỏ có những lỗ rò cố ý, từ đó tỏa ra hơi nhiệt màu cam ấm áp; bên cạnh, chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách nằm im ngủ mà người vẫn tỏa ấm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L392</summary>

```text
HÌNH L392 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Điều bất ngờ nhất: ngay cả Rái Cá con mới sinh, cơ bắp còn non nớt, các tế bào cơ đã có khả năng tạo nhiệt ngang bằng con trưởng thành. Lò sưởi được lắp sẵn... từ lúc chào đời!". Bố cục: Một chú rái cá con lông xù nằm trên ngực mẹ, bên trong cơ thể nhỏ bé vẽ một chiếc lò sưởi tí hon đã cháy đỏ, có gắn chiếc nơ quà tặng như món quà sinh nhật; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L393</summary>

```text
HÌNH L393 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giải phụ thứ năm: thiết kế không cần sửa lâu nhất! Và giải thuộc về... Chim Bồ Nông! Ở vùng Luberon, miền Nam nước Pháp, người ta tìm thấy hóa thạch của một chú bồ nông sống cách đây khoảng 30 triệu năm.". Bố cục: Một phiến đá vôi hoạt hình màu kem có in hóa thạch bộ xương chim với chiếc mỏ dài gần như nguyên vẹn, một nhà cổ sinh vật học đeo kính lúp cúi soi, phía sau là những ngọn đồi miền Nam nước Pháp; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L394</summary>

```text
HÌNH L394 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và điều khiến các nhà khoa học kinh ngạc: chiếc mỏ của chú bồ nông 30 triệu năm tuổi ấy... gần như giống hệt mỏ bồ nông ngày nay. 30 triệu năm, tạo hóa gần như không phải sửa gì thêm!". Bố cục: Hai chiếc mỏ đặt cạnh nhau hoạt hình: bên trái là mỏ hóa thạch màu đá xám, bên phải là mỏ của chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn ngày nay màu cam, giống nhau như đúc, chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn đứng cạnh nhìn hóa thạch như nhìn ảnh ông cố; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L395</summary>

```text
HÌNH L395 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà khoa học đoán rằng chiếc mỏ ấy đã quá phù hợp để bắt cá, nên không cần thay đổi. Một sản phẩm ra mắt từ 30 triệu năm trước... mà chưa từng phải tung bản cập nhật!". Bố cục: chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn cầm chiếc điện thoại hoạt hình, màn hình hiện biểu tượng mũi tên cập nhật bị gạch chéo, bên cạnh là chiếc mỏ được gắn huy hiệu ngôi sao vàng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L396</summary>

```text
HÌNH L396 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giải phụ thứ sáu: tên gọi thú vị nhất! Ban tổ chức đã tra tên khoa học của từng tuyển thủ, và phát hiện ra mỗi cái tên là một câu chuyện.". Bố cục: Một cuốn từ điển La-tinh khổng lồ hoạt hình mở ra giữa sân khấu, những dòng chữ (không đọc được, chỉ là nét gạch) bay lên thành hình bóng mười tuyển thủ; anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cầm kính lúp soi.
```
</details>

<details><summary>L397</summary>

```text
HÌNH L397 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tên khoa học của Lửng Mật là Mellivora capensis. Mellivora nghĩa là "kẻ ăn mật", còn capensis là "đến từ mũi Hảo Vọng", nơi mẫu vật đầu tiên được thu thập ở Nam Phi.". Bố cục: chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần đứng trên mũi đất nhô ra biển có ngọn hải đăng, tay cầm hũ mật ong, phía sau là biển cả và sóng vỗ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L398</summary>

```text
HÌNH L398 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tên của Tôm Tít trong khoa học là bộ Chân Miệng, vì những chiếc chân bắt mồi của nó nằm ngay gần miệng. Một võ sĩ mà tay nằm ở... cằm!". Bố cục: Cận cảnh chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh chỉ vào hai chiếc càng búa gập ngay dưới miệng mình, vẻ mặt tự hào, bên cạnh là hình vẽ một võ sĩ người hoạt hình có hai nắm đấm mọc ra từ cằm trông rất buồn cười; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L399</summary>

```text
HÌNH L399 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gấu Nước được mô tả lần đầu vào năm 1773 bởi một mục sư người Đức. Ông nhìn qua kính hiển vi, thấy sinh vật này lạch bạch như một chú gấu, nên gọi nó là "chú gấu nước nhỏ".". Bố cục: Một mục sư người Đức hoạt hình thế kỷ mười tám, tóc giả trắng, cúi nhìn qua chiếc kính hiển vi bằng đồng cổ, trong bong bóng phóng to là chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương đang lạch bạch vẫy tay; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Năm 2014, họ mang máy ảnh nhiệt vào rừng, theo dõi những con Koala hoang dã trong những ngày nắng gắt trên 30°C.". Bố cục: Màn hình máy ảnh nhiệt hiện cảnh rừng cây màu đỏ cam nóng rực, chính giữa là hình chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ màu vàng cam đang leo xuống thấp; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L400</summary>

```text
HÌNH L400 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ba năm sau, một nhà khoa học người Ý đặt cho nó cái tên khoa học có nghĩa là "kẻ bước chậm". Và hơn 200 năm sau, các nhà khoa học hiện đại đo được tốc độ đi dạo của nó: khoảng nửa thân mình mỗi giây. Đúng là danh bất hư truyền!". Bố cục: chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương đi chậm rãi trên một chiếc lá rêu, phía sau là một chú ốc sên hoạt hình đang vượt mặt và vẫy tay chào, chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương vẫn thong thả không vội; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L401</summary>

```text
HÌNH L401 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn Thú Mỏ Vịt? Ban đầu, nó được đặt tên khoa học là Platypus, nghĩa là "chân dẹt". Nhưng các nhà khoa học sớm phát hiện ra: cái tên ấy đã thuộc về... một loài bọ cánh cứng!". Bố cục: Một chú bọ cánh cứng nhỏ hoạt hình đeo bảng tên hình chữ nhật (không chữ) đứng khoanh tay trước cửa, chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá đứng ngoài nhìn vào ngơ ngác, tay cầm bảng tên giống hệt; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L402</summary>

```text
HÌNH L402 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thế là Thú Mỏ Vịt phải nhận một tên khoa học mới, có nghĩa là "mỏ chim, giống vịt". Nhưng cái tên cũ "chân dẹt" vẫn ở lại làm tên gọi thường ngày bằng tiếng Anh đến tận bây giờ. Mất tên khoa học vào tay một con bọ... nhưng vẫn giữ được biệt danh!". Bố cục: chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá đeo hai chiếc bảng tên cùng lúc, một bảng nhỏ hình mỏ chim và một bảng lớn hình bàn chân dẹt, cười tươi tạo dáng chụp ảnh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L403</summary>

```text
HÌNH L403 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giải phụ cuối cùng, và là giải mà ban tổ chức trân trọng nhất: giải hồi sinh ngoạn mục. Giải này thuộc về Rái Cá Biển, và câu chuyện của nó bắt đầu từ hơn 200 năm trước.". Bố cục: Một con tàu buồm cổ hoạt hình màu xám u ám trên biển lạnh, trên boong là những chồng da lông chất cao, bầu trời phủ mây đen; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L404</summary>

```text
HÌNH L404 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bộ lông dày nhất thế giới động vật từng khiến Rái Cá Biển trở thành món hàng săn lùng. Suốt hơn một thế kỷ rưỡi, người ta săn bắt chúng để lấy da. Đến năm 1911, trên toàn thế giới chỉ còn khoảng 1.000 đến 2.000 con Rái Cá Biển.". Bố cục: Một tấm bản đồ bờ biển Bắc Thái Bình Dương hoạt hình màu xám, chỉ còn vài chấm sáng nhỏ lẻ loi rải rác ở những hòn đảo xa, mỗi chấm là một nhóm rái cá nhỏ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L405</summary>

```text
HÌNH L405 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và cũng chính năm 1911 ấy, bốn quốc gia đã ký một hiệp ước cấm săn bắt. Những nhóm rái cá nhỏ bé còn sót lại bắt đầu sinh sôi trở lại. Ngày nay, đã có hơn 100.000 con Rái Cá Biển trên khắp các vùng biển xưa của chúng.". Bố cục: Bản đồ bờ biển hoạt hình dần dần sáng lên từ những chấm nhỏ lan rộng thành những dải màu xanh dài, trên mặt nước hàng ngàn chú chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách nằm ngửa vẫy tay; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L406</summary>

```text
HÌNH L406 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Từ 1.000 con lên hơn 100.000 con. Đó là bằng chứng rõ ràng nhất rằng: khi con người dừng tay đúng lúc, thiên nhiên biết cách tự chữa lành.". Bố cục: chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách mẹ ôm rái cá con nằm ngửa giữa rừng tảo bẹ xanh mướt dưới ánh nắng, xung quanh là cá bơi tung tăng, một chiếc ruy băng huy chương vàng lấp lánh lơ lửng phía trên; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L407</summary>

```text
HÌNH L407 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giám khảo xin trao giải đặc biệt này cho Rái Cá Biển. Và cũng xin gửi lời cảm ơn tới những người đã ký hiệp ước năm ấy.". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ trao chiếc cúp nhỏ hình trái tim cho chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách, rái cá ôm chiếc cúp như ôm hòn đá yêu thích, khán đài vỗ tay.
```
</details>

<details><summary>L408</summary>

```text
HÌNH L408 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ủa, vậy là năm nay không có giải phụ nào cho người ngủ giỏi nhất hả chú? Cháu ngủ 22 tiếng mỗi ngày đó!". Bố cục: chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ giơ tay hỏi từ hàng ghế khán đài, mắt lim dim, ôm chiếc gối hình chiếc lá khuynh diệp; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L409</summary>

```text
HÌNH L409 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Câu hỏi rất hợp lý! Nhưng chuyện Koala ngủ 22 tiếng thì khán giả của kênh đã biết rồi. Đại hội này chỉ trao giải cho những điều mới. Hẹn bạn ở... đại hội ngủ trưa!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cúi người xoa đầu chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ, đưa cho bạn ấy một chiếc huy hiệu nhỏ hình mặt trăng, chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ cười tươi rồi ngủ gục ngay trên vai chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và họ thấy một hành động rất lạ: trời càng nóng, Koala càng leo xuống thấp, rồi dang tay dang chân... ôm chặt lấy thân cây như ôm gối ôm!". Bố cục: chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ nằm sấp ôm chặt thân cây to bằng cả tay lẫn chân, má áp vào vỏ cây, vẻ mặt sung sướng mãn nguyện như đang ôm gối ôm mát lạnh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L410</summary>

```text
HÌNH L410 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lễ trao giải phụ khép lại! Và giờ, xin mời tất cả các tuyển thủ bước vào sân khấu chính, cho vòng thi cuối cùng của Đại Hội Sinh Tồn!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng giơ tay về phía sân khấu chính đang sáng rực ánh đèn, mười tuyển thủ xếp hàng bước vào, mỗi bạn ôm một hộp quà có nơ.
```
</details>

<details><summary>L411</summary>

```text
HÌNH L411 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vòng chung kết: món quà cho loài người! Mỗi tuyển thủ sẽ trình bày một phát minh, một loại thuốc, hay một công nghệ mà con người đã học được, hoặc đang học, từ chính cơ thể mình.". Bố cục: Sân khấu chung kết hoạt hình rực rỡ, phía sau là màn hình khổng lồ hình quả địa cầu, mười tuyển thủ đứng thành hàng, mỗi bạn ôm một chiếc hộp quà có nơ (không chữ); anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đứng giữa giơ micro.
```
</details>

<details><summary>L412</summary>

```text
HÌNH L412 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Rái Cá Biển mở hộp quà đầu tiên. Bên trong là... một bộ đồ lặn có lông!". Bố cục: chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách mở hộp quà, lôi ra một bộ đồ lặn hoạt hình phủ đầy lông mềm xù xì như thú nhồi bông, khán giả bật cười; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L413</summary>

```text
HÌNH L413 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Năm 2016, các kỹ sư ở Viện Công nghệ Massachusetts đã làm những tấm cao su phủ lông nhân tạo, mô phỏng bộ lông của rái cá và hải ly, rồi nhúng chúng vào chất lỏng ở nhiều tốc độ khác nhau.". Bố cục: Phòng thí nghiệm kỹ thuật hoạt hình: một cánh tay máy nhúng tấm cao su phủ lông lăn tăn xuống bể chất lỏng trong suốt, camera tốc độ cao ghi hình, những bọt khí nhỏ bám trên lông; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L414</summary>

```text
HÌNH L414 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Họ phát hiện: lông càng dày, lặn xuống càng nhanh, thì càng giữ lại được nhiều không khí. Từ đó, họ tìm ra công thức để có thể chế tạo những bộ đồ lặn ấm áp lấy cảm hứng từ bộ lông rái cá.". Bố cục: Biểu đồ hoạt hình: ba mẫu lông thưa, vừa, dày, mẫu dày nhất giữ lớp bong bóng khí dày nhất; bên cạnh là phác thảo một bộ đồ lặn tương lai có lông bên trong; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L415</summary>

```text
HÌNH L415 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chim Cánh Cụt mở hộp quà thứ hai: một tấm lưới thép nhỏ xíu, lấp lánh.". Bố cục: chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ mở hộp quà, giơ lên một tấm lưới kim loại mịn óng ánh như tấm vải bạc; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L416</summary>

```text
HÌNH L416 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà khoa học ở Canada thắc mắc: tại sao chim cánh cụt sống giữa băng giá mà lông không bao giờ bị đóng băng? Họ soi lông chim cánh cụt dưới kính hiển vi, và thấy những sợi lông nhỏ đan móc vào nhau như một tấm lưới, trên bề mặt có những rãnh siêu nhỏ.". Bố cục: Hình phóng to dưới kính hiển vi hoạt hình: các sợi lông nhỏ đan móc vào nhau thành lưới, trên bề mặt có những rãnh song song li ti; một nhà khoa học hoạt hình nhìn qua kính hiển vi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L417</summary>

```text
HÌNH L417 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Họ bắt chước cấu trúc ấy bằng lưới thép không gỉ, khắc thêm rãnh siêu nhỏ bằng tia laser. Kết quả: băng bám vào tấm lưới yếu hơn khoảng 95% so với tấm thép phẳng thông thường!". Bố cục: Hai tấm kim loại hoạt hình so sánh dưới mưa băng: tấm thép phẳng bên trái bị đóng một lớp băng dày cứng; tấm lưới bên phải băng chỉ bám mỏng và đang nứt vỡ rơi xuống; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L418</summary>

```text
HÌNH L418 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà khoa học hy vọng vật liệu này sẽ giúp chống đóng băng cho đường dây điện, tuabin gió và máy bay, mà không cần hóa chất. Quý ông Vest Đuôi Tôm... đang góp phần giữ điện cho cả một thành phố mùa đông!". Bố cục: Một thành phố hoạt hình giữa mùa đông tuyết trắng, đường dây điện và cột điện được bọc lưới bạc lấp lánh, băng không bám được, đèn trong nhà vẫn sáng ấm áp; chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ đứng trên mái nhà tự hào; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L419</summary>

```text
HÌNH L419 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bồ Nông mở hộp quà thứ ba. Bên trong là... một chiếc máy bay đồ chơi!". Bố cục: chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn dùng mỏ gắp từ hộp quà ra một chiếc máy bay chở khách đồ chơi màu trắng, vẻ mặt tự hào; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hình ảnh nhiệt cho thấy lý do: thân cây keo mát hơn không khí xung quanh hơn 5°C. Koala đang dùng cái cây như một chiếc tủ lạnh khổng lồ!". Bố cục: Ảnh nhiệt chia đôi: không khí xung quanh màu đỏ rực, riêng thân cây màu xanh dương mát lạnh, chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ áp bụng vào phần xanh; một chiếc tủ lạnh hoạt hình nhỏ vẽ cạnh để so sánh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L420</summary>

```text
HÌNH L420 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Từ việc nghiên cứu cách những đàn chim lớn bay theo hình chữ V để tiết kiệm sức, hãng máy bay Airbus đã thử nghiệm cho hai chiếc máy bay chở khách cỡ lớn bay nối đuôi nhau, cách nhau khoảng 3km.". Bố cục: Bầu trời xanh hoạt hình có hai chiếc máy bay chở khách bay nối đuôi nhau, phía sau chiếc đầu có những luồng xoáy khí xoắn ốc màu xanh nhạt nâng chiếc sau lên; bên dưới một đàn bồ nông bay chữ V cùng hướng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L421</summary>

```text
HÌNH L421 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chiếc bay sau lướt trên luồng khí của chiếc bay trước, giống hệt bồ nông. Chuyến bay thử năm 2021 từ Pháp sang Canada đã tiết kiệm được hơn 6 tấn khí thải carbon.". Bố cục: Hai chiếc máy bay hạ cánh xuống sân bay đầy tuyết, bên cạnh là một quả bóng bay hình đám mây xám có biểu tượng chiếc cân sáu khối, bị xì hơi nhỏ dần; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L422</summary>

```text
HÌNH L422 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tôm Tít mở hộp quà thứ tư, và bên trong là... một chiếc mũ bảo hiểm!". Bố cục: chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh mở hộp quà, lôi ra một chiếc mũ bảo hiểm thể thao hoạt hình có hoa văn xoắn ốc bên trong vỏ, đội thử lên đầu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L423</summary>

```text
HÌNH L423 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một chiếc càng búa của Tôm Tít phải chịu hàng chục ngàn cú đấm trong đời mà không vỡ. Các kỹ sư ở Đại học California đã soi vào bên trong để tìm hiểu bí mật.". Bố cục: Một kỹ sư hoạt hình đeo kính bảo hộ soi chiếc càng búa của chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh dưới kính hiển vi điện tử lớn, màn hình bên cạnh hiện hình phóng to nhiều lớp; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L424</summary>

```text
HÌNH L424 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Họ thấy những lớp sợi xếp xoắn như cầu thang xoắn ốc. Mỗi khi có cú va chạm, vết nứt bị buộc phải đi vòng vèo theo các lớp xoắn, nên không thể xuyên thẳng qua.". Bố cục: Mặt cắt hoạt hình chiếc càng búa của chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh: bên trong là những lớp sợi xếp xoay dần như cầu thang xoắn ốc, một vết nứt màu đỏ cố chui vào nhưng bị lạc lối đi vòng vèo rồi dừng lại; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L425</summary>

```text
HÌNH L425 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cấu trúc xoắn ốc ấy đang được các kỹ sư bắt chước để làm ra những vật liệu nhẹ mà chịu va đập tốt, hướng tới mũ bảo hiểm, áo giáp và khung xe, khung máy bay. Giám khảo ghi nhận, nhưng xin để dành huy chương chờ những sản phẩm đầu tiên ra đời!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ cẩn thận cất một chiếc huy chương vào hộp nhỏ có khóa, dán nhãn hình ngôi sao, đặt lên giá "để dành"; chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh gật đầu chấp nhận, vẫn đội chiếc mũ bảo hiểm.
```
</details>

<details><summary>L426</summary>

```text
HÌNH L426 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cá Heo xin chen ngang mở một hộp quà... ngoài danh sách. Bên trong là một chiếc phao nhỏ màu cam. Và câu chuyện của chiếc phao này bắt đầu ở một bến cảng nước Iraq, tháng 3/2003.". Bố cục: chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái dùng mũi đẩy ra một chiếc hộp quà nhỏ, bên trong là chiếc phao đánh dấu màu cam có dây buộc, phía sau là bến cảng hoạt hình với những con tàu lớn đang chờ ngoài khơi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L427</summary>

```text
HÌNH L427 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bến cảng ấy bị thả hơn 100 quả thủy lôi và vật nổ dưới nước. Máy dò dưới nước đã phát hiện hơn 200 vật thể đáng ngờ, nhưng máy không phân biệt được đâu là thủy lôi, đâu là rác hay đá.". Bố cục: Mặt cắt đáy cảng hoạt hình đầy những vật thể lẫn lộn: thủy lôi tròn có gai, xe đẩy cũ, tảng đá, thùng phuy; phía trên một chiếc tàu ngầm robot nhỏ màu vàng chiếu đèn dò với dấu chấm hỏi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L428</summary>

```text
HÌNH L428 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đó là lúc 8 chú cá heo của Hải quân Mỹ được gửi xuống. Bằng tiếng định vị, cá heo phân biệt được vật thể tự nhiên và vật thể do con người làm ra, kể cả những thứ bị vùi trong bùn.". Bố cục: Một chiếc xuồng hơi hoạt hình chở người huấn luyện và một chú chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái đeo dây đai nhỏ, chú cá heo nhảy xuống nước, những vòng sóng âm tỏa ra hướng về đáy cảng đục ngầu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L429</summary>

```text
HÌNH L429 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi phát hiện thủy lôi, chúng bơi về báo cho người huấn luyện, rồi mang chiếc phao xuống đánh dấu vị trí.". Bố cục: Một chú chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái dưới nước phát ra những vòng sóng âm hướng về một quả thủy lôi vùi nửa trong bùn, rồi ngậm chiếc phao cam đặt cạnh đó; trên mặt nước là chiếc xuồng có người huấn luyện chờ sẵn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và đây không phải ôm cho vui. Theo tính toán của các nhà khoa học, chỉ riêng việc ôm cây đã giúp Koala tiết kiệm khoảng một nửa lượng nước cần để làm mát cơ thể trong một ngày nóng.". Bố cục: Hai giọt nước hoạt hình so sánh: giọt bên trái to (không ôm cây), giọt bên phải chỉ còn một nửa (có ôm cây), chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ giơ ngón cái tự hào; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L430</summary>

```text
HÌNH L430 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhờ vậy, chỉ khoảng một tuần sau, bến cảng đã được mở lại để những con tàu chở gạo và lương thực cập bến. Các nhà khoa học hải quân thừa nhận: trong vùng nước đục và nhiều vật cản, khả năng định vị của cá heo vẫn vượt mọi máy móc hiện có.". Bố cục: Một con tàu chở hàng hoạt hình chở đầy bao gạo cập bến an toàn, người dân trên bờ vẫy tay, dưới nước chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái nhô lên mỉm cười; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L431</summary>

```text
HÌNH L431 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giám khảo ghi nhận món quà ngoài danh sách của Cá Heo. Nhưng vì đây là phần chen ngang... nên chỉ được tính là điểm cộng tinh thần!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ mỉm cười gõ búa nhẹ, gắn một ngôi sao vàng nhỏ lên chiếc phao cam, chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái gật đầu vui vẻ.
```
</details>

<details><summary>L432</summary>

```text
HÌNH L432 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gấu Nước mở hộp quà thứ năm. Bên trong là... một đoạn gen phát sáng.". Bố cục: chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương mở chiếc hộp quà to hơn người nó, bên trong là một chuỗi xoắn ADN nhỏ phát ánh sáng xanh lam huyền ảo; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L433</summary>

```text
HÌNH L433 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Năm 2016, các nhà khoa học Nhật Bản giải mã bộ gen của một loài gấu nước cực kỳ khỏe, và tìm thấy một loại đạm chỉ gấu nước mới có. Họ đặt tên nó là Dsup, nghĩa là "chất chống hư hại".". Bố cục: Phòng thí nghiệm Nhật Bản hoạt hình có cây anh đào ngoài cửa sổ, một nhà khoa học đeo kính nhìn vào màn hình hiện chuỗi xoắn ADN và một tấm khiên nhỏ bọc quanh nó; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L434</summary>

```text
HÌNH L434 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Rồi họ làm một thí nghiệm táo bạo: đưa đoạn gen này vào tế bào người nuôi trong phòng thí nghiệm, rồi chiếu tia X. Kết quả: tế bào người có đạm Dsup bị hư hại ADN ít hơn khoảng 40%!". Bố cục: Hai đĩa tế bào hoạt hình dưới chùm tia X màu tím: đĩa bên trái tế bào người bị vỡ vụn nhiều mảnh; đĩa bên phải tế bào được bao bọc bởi những đám mây khiên xanh nhỏ của gấu nước, ít bị vỡ hơn hẳn; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L435</summary>

```text
HÌNH L435 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một chú gấu nước bé hơn hạt cát đã cho tế bào người... mượn tạm một chiếc áo giáp chống phóng xạ!". Bố cục: chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương tí hon đang mặc cho một tế bào người hoạt hình to tròn một chiếc áo giáp màu xanh nhỏ xíu, tế bào nhìn xuống bối rối nhưng cảm động; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L436</summary>

```text
HÌNH L436 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và cuối cùng, tuyển thủ dẫn đầu: Thú Mỏ Vịt. Ở vòng ba, Thú Mỏ Vịt đã kể về chất kháng khuẩn trong sữa. Hôm nay, nó mở hộp quà thứ sáu, và bên trong là... một giọt nọc độc.". Bố cục: chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá mở hộp quà, bên trong là một lọ thủy tinh nhỏ chứa một giọt chất lỏng màu tím lấp lánh, khán giả lùi lại vì sợ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L437</summary>

```text
HÌNH L437 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thú Mỏ Vịt đực có chiếc cựa độc ở chân sau. Năm 2016, các nhà khoa học Úc phát hiện trong nọc độc ấy có một loại hormone gọi là GLP-1. Ở người, hormone này giúp cơ thể tiết ra insulin để hạ đường huyết.". Bố cục: Sơ đồ hoạt hình: cựa độc ở chân sau chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá, một mũi tên chỉ sang một phân tử hóc-môn nhỏ, rồi mũi tên chỉ tiếp sang tuyến tụy hoạt hình đang tiết ra những giọt in-su-lin vàng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L438</summary>

```text
HÌNH L438 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vấn đề là ở người, hormone này bị phân hủy chỉ trong vài phút. Còn hormone trong nọc Thú Mỏ Vịt thì bền hơn hẳn, vì nó vừa phải làm việc trong ruột, vừa phải làm việc trong nọc độc.". Bố cục: Hai chiếc đồng hồ cát hoạt hình: đồng hồ của người cát chảy hết rất nhanh, đồng hồ của chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá cát chảy rất chậm, rất bền bỉ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L439</summary>

```text
HÌNH L439 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và một hormone bền hơn chính là điều mà các nhà khoa học tìm kiếm để làm thuốc điều trị bệnh tiểu đường loại hai. Hiện nay các nhóm nghiên cứu ở Úc đang thử nghiệm những phân tử lấy cảm hứng từ nọc Thú Mỏ Vịt trên chuột.". Bố cục: Một chú chuột thí nghiệm hoạt hình khỏe mạnh đứng trên chiếc cân, cạnh đó là ống nghiệm có hình chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá, một nhà khoa học ghi chép biểu đồ đường huyết đi xuống; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Điều buồn cười nhất: cây keo này Koala không hề ăn. Nó leo sang cây keo chỉ để... ôm cho mát, xong lại leo về cây khuynh diệp để ăn. Một cây làm phòng ăn, một cây làm phòng điều hòa!". Bố cục: Hai cái cây đứng cạnh nhau có cầu thang dây nối giữa: cây khuynh diệp bên trái có biểu tượng cái đĩa và đôi đũa, cây keo bên phải có biểu tượng bông tuyết; chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ đang leo qua cầu thang dây từ cây này sang cây kia; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L440</summary>

```text
HÌNH L440 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sữa có chất diệt khuẩn. Nọc độc có thể thành thuốc chữa tiểu đường. Con vật từng bị các nhà khoa học cầm kéo đi tìm đường chỉ khâu, hóa ra lại là một... hiệu thuốc biết bơi!". Bố cục: chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá mặc áo blouse trắng đứng sau quầy thuốc dưới nước, trên kệ phía sau là những lọ thuốc có hình giọt sữa và giọt nọc tím; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L441</summary>

```text
HÌNH L441 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giám khảo ra hiệu chuẩn bị công bố. Cả sân vận động im phăng phắc.". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ đứng dậy trên bàn giám khảo, tay cầm phong bì, cả khán đài nín thở, ánh đèn sân khấu hội tụ về phía bà; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L442</summary>

```text
HÌNH L442 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Huy chương đồng vòng chung kết, 2 điểm: Chim Bồ Nông, người thầy dạy máy bay cách bay đỡ tốn sức!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ mở phong bì đầu tiên, phía dưới chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn bước lên bậc đồng, đôi cánh dang rộng, chiếc máy bay đồ chơi đậu trên mỏ.
```
</details>

<details><summary>L443</summary>

```text
HÌNH L443 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Huy chương bạc, 4 điểm: Gấu Nước, người cho tế bào người mượn áo giáp!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ mở phong bì thứ hai, phía dưới chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương được nâng lên bậc bạc trên một chiếc đĩa nhỏ có kính lúp phóng to.
```
</details>

<details><summary>L444</summary>

```text
HÌNH L444 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và huy chương vàng vòng chung kết, 6 điểm, thuộc về... Thú Mỏ Vịt!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ mở phong bì cuối cùng, giơ cao tấm thiệp có hình chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá, pháo giấy vàng nổ tung khắp sân vận động.
```
</details>

<details><summary>L445</summary>

```text
HÌNH L445 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và đây là bảng điểm cuối cùng của Đại Hội Sinh Tồn lần thứ nhất!". Bố cục: tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) xoay vòng, đèn nhấp nháy liên hồi, mười cột điểm nhảy lên xuống hồi hộp trước khi dừng lại; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L446</summary>

```text
HÌNH L446 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hạng ba: Lửng Mật, 6 điểm! Trắng tay suốt bốn vòng đầu, rồi bùng nổ với hai huy chương vàng: bà mẹ chuyển nhà mỗi 3 ngày, và gã giang hồ dám nhận mình chưa chắc đúng!". Bố cục: chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần bước lên bục hạng ba, đeo hai chiếc huy chương vàng, lửng con ngồi trên đầu, sáu con chim ưng xám bay lượn phía trên tung pháo giấy; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L447</summary>

```text
HÌNH L447 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hạng hai: Cá Heo, 7 điểm! Người lính gác 15 ngày không ngủ, và người bạn của ngư dân Brazil suốt hơn 100 năm!". Bố cục: chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái nhảy vọt lên từ bể nước đặt trên bục hạng hai, đeo hai huy chương vàng và một huy chương đồng, những người đánh cá Bra-xin hoạt hình vẫy lưới chúc mừng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L448</summary>

```text
HÌNH L448 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và nhà vô địch Đại Hội Sinh Tồn lần thứ nhất, với ba huy chương vàng, một huy chương bạc và 14 điểm...". Bố cục: Đèn sân vận động tắt phụt, chỉ còn một vòng ánh sáng vàng rọi xuống chiếc vương miện bé xíu trên bệ đá giữa sân; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L449</summary>

```text
HÌNH L449 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thú Mỏ Vịt! Tuyển thủ mà các chuyên gia dự đoán chỉ "tham gia cho vui"!". Bố cục: chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá đeo băng đô xanh và ba huy chương vàng bước lên bục cao nhất, anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đặt chiếc vương miện vàng bé xíu lên đầu, pháo hoa nổ rực trời, khán đài vỡ òa.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng chống nóng mới chỉ là một nửa. Nửa còn lại là chuyện... uống nước. Trong hàng trăm năm, người ta tin rằng Koala lấy gần hết nước từ lá, chỉ uống khi nắng nóng khắc nghiệt.". Bố cục: Một cuốn sách cổ dày bụi mở ra, trang sách vẽ hình chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ ôm chiếc lá to và một ly nước bị gạch chéo; một ngọn nến cháy leo lét bên cạnh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L450</summary>

```text
HÌNH L450 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thú Mỏ Vịt đứng trên bục cao nhất, chiếc vương miện bé xíu hơi lệch trên đầu. Hơn 200 năm trước, khi mẫu vật đầu tiên đến châu Âu, các nhà khoa học tưởng nó là đồ giả. Đêm nay, nó là nhà vô địch.". Bố cục: chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá đứng trên bục vô địch, vương miện lệch trên đầu, khóc vì xúc động; bên cạnh là một khung ảnh cũ đen trắng vẽ nhà khoa học cầm kéo soi mẫu vật; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L451</summary>

```text
HÌNH L451 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ủa... vậy là bạn mỏ vịt thắng thật ạ? Chúc mừng bạn! Bạn có muốn ôm cây với cháu không?". Bố cục: chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ chạy lạch bạch tới ôm chầm lấy chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá, hai bạn ôm nhau trên bục, vương miện suýt rơi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L452</summary>

```text
HÌNH L452 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhìn lại cả tám vòng thi, có một điều thú vị: những tuyển thủ được dự đoán là mạnh nhất, Tôm Tít và Gấu Nước, lại không lên được bục vinh quang.". Bố cục: chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh và chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương đứng ở góc sân khoanh tay, nhìn lên bục vô địch, ban đầu hậm hực, rồi từ từ mỉm cười và vỗ tay; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L453</summary>

```text
HÌNH L453 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vì sinh tồn không chỉ là đánh nhau. Sinh tồn còn là giữ ấm giữa nước đá, là đi theo mặt trời 13.000km, là hợp tác với người đánh cá, là ôm cây cho mát.". Bố cục: Một bức tranh ghép nhiều ô hoạt hình: chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá bơi trong nước đá, chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ đi trên băng hướng về mặt trời, chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái cùng người đánh cá, chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ ôm cây; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L454</summary>

```text
HÌNH L454 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và có 1 điểm chung giữa những tuyển thủ chiến thắng ở vòng cuối: con người đã học được từ chúng. Từ lông rái cá, lông cánh cụt, đội hình bồ nông, đến gen gấu nước và sữa, nọc độc của thú mỏ vịt.". Bố cục: Một nhà khoa học hoạt hình ngồi trên chiếc bàn tròn với mười tuyển thủ, mỗi tuyển thủ đưa cho nhà khoa học một món đồ nhỏ: chùm lông, tấm lưới, máy bay đồ chơi, ống nghiệm phát sáng, lọ thuốc; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L455</summary>

```text
HÌNH L455 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thiên nhiên không chỉ là nơi để chúng ta ngắm nhìn. Đó còn là một thư viện khổng lồ, nơi mỗi loài vật là một cuốn sách chứa những lời giải mà con người chưa nghĩ ra.". Bố cục: Một thư viện hoạt hình khổng lồ có kệ sách là thân cây, mỗi cuốn sách trên kệ có gáy in hình một con vật khác nhau (không chữ), một em bé đang rút một cuốn ra đọc; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L456</summary>

```text
HÌNH L456 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và cũng có những cuốn sách đang bị đe dọa. Ngày 12/2/2022, Koala ở ba bang miền Đông nước Úc chính thức bị xếp vào danh sách nguy cấp, sau hạn hán kéo dài, cháy rừng và mất nơi sống.". Bố cục: Một tấm hồ sơ hoạt hình màu đỏ có ảnh chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ ôm thân cây cháy sém, bên cạnh là con dấu hình chiếc khiên đỏ, phía sau là cánh rừng khô cháy; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L457</summary>

```text
HÌNH L457 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tháng 11/2023, đến lượt Chồn Gulo ở lục địa nước Mỹ được đưa vào danh sách loài bị đe dọa, vì những lớp tuyết mùa xuân mà nó cần để sinh con đang ngày một ít đi.". Bố cục: Một tấm hồ sơ hoạt hình màu cam có ảnh chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh đứng trên sườn núi tuyết đang tan, nước chảy thành dòng, con dấu hình chiếc khiên cam; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L458</summary>

```text
HÌNH L458 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chồn Gulo cần tuyết mùa xuân. Cá heo ở Laguna cần cá đối. Koala cần những cái cây để ôm, và những cơn mưa để uống.". Bố cục: Ba ô tranh hoạt hình buồn: tuyết tan sớm trên núi của chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh, con kênh vắng cá của chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái, cánh rừng khô hạn có chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ ôm thân cây trơ trụi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L459</summary>

```text
HÌNH L459 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu những loài vật này biến mất, chúng ta không chỉ mất đi những sinh vật đáng yêu. Chúng ta còn mất đi những lời giải mà có khi... chưa ai kịp đọc. Nhưng câu chuyện Rái Cá Biển ở lễ trao giải phụ đã cho thấy: chưa bao giờ là quá muộn.". Bố cục: Một cuốn sách hoạt hình có bìa hình chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh đang mờ dần như sắp tan biến, một bàn tay em bé nhẹ nhàng giữ lấy nó; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cho đến năm 2020, khi một nhóm nhà khoa học tập hợp 46 lần quan sát Koala hoang dã... đang uống nước.". Bố cục: Một tấm bản đồ nước Úc ghim nhiều đinh ghim đỏ đánh dấu chỗ quan sát, bên cạnh là chồng ảnh chụp chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L460</summary>

```text
HÌNH L460 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trước khi chia tay, mời toàn thể khán đài cùng nhìn lại bảng tổng sắp cuối cùng của Đại Hội Sinh Tồn lần thứ nhất!". Bố cục: tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) lớn hiện lên giữa sân với mười cột sáng từ cao xuống thấp, pháo hoa nhỏ nổ hai bên, anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đứng cạnh giơ tay giới thiệu.
```
</details>

<details><summary>L461</summary>

```text
HÌNH L461 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vô địch: Thú Mỏ Vịt, 14 điểm! Ba huy chương vàng, một huy chương bạc! Bơi 5 tiếng trong nước 0 độ, ăn khỏe nhất cuộc thi, và mang đến cho loài người cả sữa diệt khuẩn lẫn nọc độc chữa bệnh!". Bố cục: chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá đội vương miện đứng trên đỉnh cột điểm cao nhất, đeo ba huy chương vàng và một huy chương bạc, băng đô xanh, hai tay giơ cao; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L462</summary>

```text
HÌNH L462 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Á quân: Cá Heo, 7 điểm! Người lính gác 15 ngày, đồng đội trăm năm của ngư dân Brazil, và bà cụ Nicklo 67 tuổi!". Bố cục: chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái nhảy vọt lên trên cột điểm thứ hai, đeo hai huy chương vàng và một huy chương đồng, nước bắn tung tóe lấp lánh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L463</summary>

```text
HÌNH L463 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hạng ba: Lửng Mật, 6 điểm! Trắng tay bốn vòng đầu, rồi bùng nổ với hai huy chương vàng nhờ làm mẹ giỏi và dám nhận mình chưa chắc đúng!". Bố cục: chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần đứng trên cột điểm thứ ba, lửng con ngồi trên đầu, đeo hai huy chương vàng, sáu con chim ưng xám bay lượn phía trên; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L464</summary>

```text
HÌNH L464 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hạng tư: Gấu Nước, năm điểm, tuyển thủ được dự đoán vô địch đã bứt phá ở hai vòng cuối. Tiếp theo là nhóm bám đuổi, cùng 4 điểm: Chồn Gulo với hai huy chương bạc, Chim Cánh Cụt với một vàng một đồng, Rái Cá Biển với một bạc hai đồng, và Chim Bồ Nông với một bạc một đồng.". Bố cục: Ba cột điểm bằng nhau hoạt hình: chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương đứng trên cột hạng tư vẫy tay qua kính lúp; bên cạnh chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh khoanh tay, chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ chỉnh nơ, chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách ôm hòn đá, chú Chim Bồ Nông trắng hoạt hình to xác, chiếc mỏ dài màu cam vàng có túi da họng lớn dang cánh, bốn bạn đứng cạnh nhau cười tươi, mỗi bạn đeo những chiếc huy chương của mình; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L465</summary>

```text
HÌNH L465 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và cuối bảng, cùng 3 điểm: Tôm Tít, võ sĩ biết đấm khiên thay vì đấm người, và Koala, tuyển thủ ngủ nhiều nhất nhưng đã giúp khoa học sửa một hiểu lầm. Không ai ra về tay trắng!". Bố cục: Hai cột điểm cuối hoạt hình: chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh giơ càng chào kiểu võ sĩ, chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ ôm cột điểm ngủ gật, cả hai đeo huy chương và cười tươi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L466</summary>

```text
HÌNH L466 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và nếu phải chọn những khoảnh khắc đáng nhớ nhất của đại hội, thì đó là: Koala ôm cây keo làm điều hòa. Chồn Gulo đi bộ 800km và trở thành con chồn đầu tiên ở Colorado sau 90 năm.". Bố cục: Một cuốn album ảnh kỷ niệm hoạt hình mở ra: ảnh chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ ôm thân cây mát, ảnh chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh đứng trên đỉnh núi Rốc-ky, những tấm ảnh được dán bằng băng dính hoạt hình; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L467</summary>

```text
HÌNH L467 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chim Cánh Cụt đi theo mặt trời 13.000km. Gấu Nước bị bắn khỏi nòng súng khí và dám thừa nhận mình không bất tử. Và ông lão ngư dân Brazil đứng dưới nước, chờ tín hiệu của người bạn cá heo.". Bố cục: Trang album tiếp theo: ảnh chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ trên băng dưới hoàng hôn, ảnh chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương bò ra khỏi bao cát, ảnh người ngư dân Bra-xin và chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái cùng nhìn nhau; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L468</summary>

```text
HÌNH L468 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và bây giờ, đến lượt bạn làm giám khảo! Bạn đồng ý với kết quả này không? Nếu là bạn, bạn sẽ trao vương miện cho ai?". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng chĩa micro vàng ra phía người xem, mỉm cười, phía sau là tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) với mười hình đầu tuyển thủ đang chờ bình chọn.
```
</details>

<details><summary>L469</summary>

```text
HÌNH L469 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy viết tên nhà vô địch của riêng bạn ở phần bình luận nhé. Biết đâu, ở đại hội lần sau, kết quả sẽ thay đổi hoàn toàn!". Bố cục: Mười tuyển thủ đứng dàn hàng ngang trên sân khấu vẫy tay chào khán giả, pháo giấy rơi, anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đứng giữa cúi chào.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và cách uống thì... không giống ai. Khi trời mưa, nước chảy thành dòng dọc theo thân cây trơn. Koala ôm cây, thè lưỡi... và liếm từng dòng nước mưa từ trên xuống!". Bố cục: Trời mưa lất phất, dòng nước chảy dọc thân cây khuynh diệp nhẵn, chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ ôm cây thè lưỡi liếm nước, mắt nhắm tận hưởng như đang uống nước suối; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L470</summary>

```text
HÌNH L470 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vì Đại Hội Sinh Tồn lần thứ hai đã có danh sách tuyển thủ. Mười gương mặt mới, đến từ khắp nơi trên thế giới: từ khu rừng tre ở Tứ Xuyên, đến dòng sông bùn ở châu Phi, đến những cánh rừng mưa Nam Mỹ.". Bố cục: Một cánh cửa đường hầm mới mở hé ánh sáng, bên trong là mười cái bóng đen mới: một con gấu tròn ôm cành tre, một con hà mã to lớn, một con lười treo ngược, và nhiều bóng khác; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L471</summary>

```text
HÌNH L471 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và lần này, có một tuyển thủ mang theo cả một khẩu đại bác nước trên càng! Hẹn gặp lại toàn thể khán đài ở Đại Hội Sinh Tồn lần thứ hai!". Bố cục: Một chú tôm nhỏ có chiếc càng to quá khổ như khẩu súng đứng ở cửa đường hầm, phun một tia nước mạnh tạo bong bóng nổ "bụp" hoạt hình, anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng đứng ngoài giật mình làm rơi micro.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Có một cô Koala mẹ đã uống liên tục như thế suốt 15 phút không nghỉ. Cây cối với Koala vừa là nhà, vừa là bếp, vừa là điều hòa, vừa là... vòi nước!". Bố cục: Một cái cây hoạt hình được vẽ như căn hộ nhiều tầng: tầng trên là bếp lá, tầng giữa là điều hòa bông tuyết, tầng dưới là vòi nước, chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ mẹ cõng con nhỏ trên lưng ở giữa; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giám khảo ghi nhận: chiến thuật tiết kiệm, khoa học, và... rất đáng yêu.". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gật đầu ghi chép, đặt một ngôi sao vàng nhỏ lên bảng cạnh hình đầu chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Phần thi nóng tiếp theo, chúng ta có hai tuyển thủ đến từ biển lạnh. Rái Cá Biển và Chim Cánh Cụt đều đứng nhìn nửa sân sa mạc với ánh mắt... không mấy thiện cảm.". Bố cục: chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách và chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ đứng ở mép sân sa mạc, nhìn mặt trời chói chang, cả hai đổ mồ hôi, chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ giơ cánh che mắt, chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách ôm hòn đá che đầu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hai bạn xin phép chuyển sang phần thi lạnh. Và giám khảo đồng ý, vì phần thi lạnh mới là chiến trường thật sự!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng mở cánh cửa lớn dẫn sang nửa sân băng tuyết, gió lạnh thổi tung cà vạt của anh, chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách và chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ vui mừng chạy ào vào tuyết.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Phần thi lạnh. Nhiệt độ nước: gần bằng 0°C. Ở mức này, một con người không được bảo hộ chỉ trụ được rất ngắn trước khi cơ thể bắt đầu mất kiểm soát.". Bố cục: Một hồ nước băng giá đen sẫm có những tảng băng trôi, bên cạnh là chiếc nhiệt kế khổng lồ chỉ ở vạch thấp nhất màu xanh, hơi lạnh bốc lên mờ mờ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyển thủ đầu tiên nhảy xuống, và cả sân vận động cùng... há hốc mồm. Không phải Rái Cá, không phải Cánh Cụt. Mà là Thú Mỏ Vịt!". Bố cục: chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá đeo băng đô xanh lao người nhảy xuống hồ băng tõm một cái, nước bắn tung tóe; trên khán đài, đám khán giả thú nhỏ há hốc mồm sững sờ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tin khẩn từ hồ băng: tuyển thủ được dự đoán "tham gia cho vui" vừa nhảy xuống nước lạnh nhất sân!". Bố cục: Cô phát thanh viên hoạt hình ngồi sau bàn tin tức, chỉ tay vào màn hình phía sau đang chiếu cảnh chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá bơi giữa hồ băng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhiều người quên mất rằng Thú Mỏ Vịt không chỉ sống ở những con suối ấm. Ở đảo Tasmania và những dòng sông trên núi cao nước Úc, mùa đông nước sông lạnh gần bằng 0°C.". Bố cục: Một dòng sông trên núi tuyết hoạt hình, hai bờ phủ tuyết trắng, mặt nước có vài mảng băng mỏng, chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá ló đầu lên từ giữa dòng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà khoa học đã gắn thiết bị đo nhiệt độ vào những con Thú Mỏ Vịt hoang dã và theo dõi chúng suốt mùa đông. Kết quả khiến họ phải đo lại mấy lần.". Bố cục: Một nhà khoa học hoạt hình đeo kính cầm máy đo nhiệt độ cầm tay, nhìn màn hình rồi dụi mắt, nhìn lại lần nữa vẻ không tin nổi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L57</summary>

```text
HÌNH L57 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một con Thú Mỏ Vịt đã bơi trong dòng nước 0°C ở một con sông đóng băng một phần suốt ít nhất 5 tiếng liền, mà nhiệt độ cơ thể vẫn giữ nguyên, không hề tụt.". Bố cục: chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá bơi thong thả giữa dòng sông có những mảng băng trôi, bên cạnh là chiếc đồng hồ cát lớn đang chảy, quanh người là vầng hào quang màu cam ấm áp; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L58</summary>

```text
HÌNH L58 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và nhiệt độ cơ thể ấy là bao nhiêu? Chỉ khoảng 32°C, thấp hơn người chúng ta khoảng 5 độ.". Bố cục: Hai chiếc nhiệt kế đặt cạnh nhau: nhiệt kế của người hoạt hình cao hơn, nhiệt kế của chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá thấp hơn một đoạn, chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá nhún vai tỉnh bơ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L59</summary>

```text
HÌNH L59 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tức là Thú Mỏ Vịt chạy máy sưởi ở mức tiết kiệm điện... mà vẫn ấm áp giữa nước đá. Nghe như quảng cáo điều hòa inverter!". Bố cục: chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá đeo kính râm nằm ngửa thư giãn giữa nước đá, trên bụng có một biểu tượng hình chiếc pin xanh lá đầy năng lượng và chiếc lá nhỏ tiết kiệm điện; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L60</summary>

```text
HÌNH L60 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bí quyết nằm ở ba lớp bảo vệ. Thứ nhất là bộ lông: lớp lông tơ xoăn tít bên dưới giữ lại một lớp không khí sát da, giống chiếc áo phao bằng không khí.". Bố cục: Hình phóng to lát cắt bộ lông chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá: lớp lông tơ xoăn tít bên dưới kẹp những bong bóng khí nhỏ li ti, lớp lông dài bóng phía trên; nước xanh không chạm được vào da; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L61</summary>

```text
HÌNH L61 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Theo các nhà nghiên cứu, khả năng cách nhiệt của bộ lông này còn cao hơn cả lông gấu Bắc Cực và lông hải ly!". Bố cục: Ba chiếc áo khoác lông treo trên giá: áo gấu Bắc Cực, áo hải ly và áo Thú Mỏ Vịt; áo Thú Mỏ Vịt được gắn một chiếc huy hiệu ngôi sao vàng lấp lánh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L62</summary>

```text
HÌNH L62 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thứ hai, ở gốc chân sau và gốc đuôi có một mạng lưới mạch máu đặc biệt, hoạt động như bộ trao đổi nhiệt: máu nóng chảy ra sưởi ấm cho máu lạnh chảy về, nên hơi ấm không bị thất thoát ra nước.". Bố cục: Sơ đồ giải phẫu hoạt hình gốc đuôi chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá: hai ống mạch máu đỏ và xanh nằm sát nhau ngược chiều, những mũi tên nhiệt màu cam truyền từ ống đỏ sang ống xanh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L63</summary>

```text
HÌNH L63 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và thứ ba: khi lạnh hơn, Thú Mỏ Vịt chỉ đơn giản là... đốt năng lượng nhiều hơn. Lò sưởi bên trong cứ thế cháy đều, không hề tắt.". Bố cục: Bên trong bụng chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá vẽ một chiếc lò sưởi nhỏ ấm áp có ngọn lửa cam đều đặn, bên ngoài là nước đá lạnh buốt; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L64</summary>

```text
HÌNH L64 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giám khảo xin ghi nhận: tuyển thủ số chín... đã gây bất ngờ lớn đầu tiên của đêm nay.". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ tháo kính ra lau, rồi đeo lại nhìn chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá với vẻ nể phục, ghi một dấu tích to vào sổ.
```
</details>

<details><summary>L65</summary>

```text
HÌNH L65 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Rái Cá Biển cũng không chịu thua. Không có lớp mỡ dày như hải cẩu, Rái Cá có một mẹo giữ ấm cực kỳ đơn giản mà khán giả có thể tự quan sát.". Bố cục: chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách nằm ngửa trên mặt nước băng giá, hai bàn tay trước và hai bàn chân sau đều giơ cao khỏi mặt nước như đang tạo dáng chụp ảnh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L66</summary>

```text
HÌNH L66 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi nghỉ ngơi trên mặt nước, Rái Cá Biển giơ bàn tay và bàn chân lên khỏi mặt nước. Vì bàn tay ít lông, mà nước lại hút hơi nóng nhanh hơn không khí rất nhiều lần.". Bố cục: Hình so sánh hoạt hình: một bàn tay rái cá nhúng nước có những mũi tên nhiệt đỏ thoát ra rất nhiều; một bàn tay giơ lên không khí chỉ có vài mũi tên nhỏ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L67</summary>

```text
HÌNH L67 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đôi khi Rái Cá còn úp hai bàn tay lên mắt khi ngủ, trông như đang ngại ngùng, nhưng thật ra là đang... giữ ấm cho đôi bàn tay!". Bố cục: Cận cảnh chú Rái Cá Biển hoạt hình lông nâu sẫm, mặt tròn lông màu kem, râu trắng dài, hay nằm ngửa trên mặt nước, kẹp một hòn đá xám dưới nách ngủ ngửa trên sóng, hai bàn tay úp lên mắt cực đáng yêu, một bong bóng suy nghĩ nhỏ vẽ chiếc găng tay len ấm áp; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L68</summary>

```text
HÌNH L68 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyển thủ tiếp theo không cần nước lạnh. Hắn cần tuyết. Rất nhiều tuyết. Chồn Gulo bước vào khu băng giá, nhìn quanh... và bắt đầu đào.". Bố cục: chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh đứng giữa vùng tuyết trắng mênh mông, hai chân trước đào tung tuyết như máy xúc, tuyết bay tứ tung; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L69</summary>

```text
HÌNH L69 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà khoa học đã đánh dấu toàn bộ 562 hang sinh con của Chồn Gulo từng được tìm thấy ở Bắc Mỹ và Bắc Âu lên bản đồ vệ tinh.". Bố cục: Một tấm bản đồ vệ tinh Bắc bán cầu hoạt hình phủ những chấm đỏ nhỏ li ti đánh dấu hang, phần lớn nằm trên vùng tuyết trắng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L70</summary>

```text
HÌNH L70 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và kết quả trùng khớp đến kinh ngạc: tất cả các hang đều nằm ở nơi tuyết vẫn còn phủ dày cho đến cuối mùa xuân. Không có ngoại lệ.". Bố cục: Bản đồ vệ tinh phủ lớp màu trắng tuyết mùa xuân, toàn bộ chấm đỏ đều nằm gọn bên trong vùng trắng, một chiếc kính lúp soi vào chứng minh; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L71</summary>

```text
HÌNH L71 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chồn mẹ đào đường hầm dưới lớp tuyết dày hơn 1 mét, có khi là cả một mê cung nhiều ngã rẽ, để sinh con giữa mùa đông.". Bố cục: Mặt cắt ngang lớp tuyết dày hoạt hình: bên dưới là một mê cung đường hầm tuyết nhiều ngã rẽ, ở cuối là căn phòng nhỏ ấm áp có chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh mẹ ôm hai chú chồn con; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L72</summary>

```text
HÌNH L72 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tuyết nghe thì lạnh, nhưng lớp tuyết dày lại là tấm chăn cách nhiệt tuyệt vời: bên ngoài gió bão gào thét, bên trong hang vẫn yên ổn như trong một chiếc túi ngủ.". Bố cục: Chia đôi khung hình theo chiều dọc: phía trên mặt tuyết là bão tuyết gió thổi mạnh; phía dưới trong hang tuyết là chồn con nằm ngủ ngon lành trong ánh sáng ấm áp; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L73</summary>

```text
HÌNH L73 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và cũng vì thế mà Chồn Gulo sợ nhất là... mùa xuân đến quá sớm. Tuyết tan sớm thì hang sụp, nhà không còn, chồn con phơi mình giữa trời.". Bố cục: chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh ngồi buồn bã nhìn những giọt nước nhỏ từ trần hang tuyết đang tan chảy, mặt trời mùa xuân chiếu qua lỗ thủng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L74</summary>

```text
HÌNH L74 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kẻ dám cướp mồi của gấu xám lại có một nỗi lo mà ai nghe cũng thấy thương: lo trái đất ấm lên.". Bố cục: chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh cầm một chiếc nhiệt kế nhỏ, nhìn lên quả địa cầu đang đổ mồ hôi, vẻ mặt lo lắng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L75</summary>

```text
HÌNH L75 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và cuối cùng, tuyển thủ được đặt cược nhiều nhất vòng này: Gấu Nước, kẻ từng sống sót ở nhiệt độ thấp đến khó tin. Cậu ấy bước vào tủ đông...". Bố cục: chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương tí hon tự tin bước vào một chiếc tủ đông khổng lồ có hơi lạnh tỏa ra, quay lại vẫy tay chào khán giả trước khi cửa đóng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L76</summary>

```text
HÌNH L76 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Năm 2022, các nhà khoa học Đức làm một thí nghiệm thú vị: cứ một tuần cho Gấu Nước đông đá ở -30°C, rồi tuần sau rã đông, cho ăn, rồi lại đông đá.". Bố cục: Lịch treo tường hoạt hình có các tuần xen kẽ: tuần biểu tượng bông tuyết xanh, tuần biểu tượng chiếc bát thức ăn, lặp lại; bên cạnh là chiếc tủ đông và ống nghiệm; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L77</summary>

```text
HÌNH L77 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lặp lại như vậy cho đến khi chúng chết vì tuổi già. Và nhóm Gấu Nước được đông đá sống lâu gấp đôi nhóm không đông đá!". Bố cục: Hai cột thời gian so sánh: cột ngắn của Gấu Nước bình thường và cột dài gấp đôi của Gấu Nước đông đá có những khối băng xen kẽ; chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương đứng trên đỉnh cột dài; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L78</summary>

```text
HÌNH L78 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng phần thú vị nằm ở phép trừ: nếu bỏ đi thời gian nằm trong tủ đông, thì tuổi thọ của hai nhóm... bằng nhau.". Bố cục: Một phép tính hoạt hình trên bảng đen: cột dài trừ đi các khối băng bằng đúng cột ngắn, bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ cầm phấn gạch dấu bằng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L79</summary>

```text
HÌNH L79 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nghĩa là khi bị đông đá, Gấu Nước không già đi chút nào. Đồng hồ sinh học dừng hẳn, như nàng công chúa ngủ trong rừng!". Bố cục: chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương nằm ngủ trong khối băng trong suốt như chiếc giường công chúa, trên đầu có chiếc đồng hồ dừng kim, xung quanh là hoa hồng và gai leo hoạt hình; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L80</summary>

```text
HÌNH L80 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giám khảo xin thông báo: tuyển thủ Gấu Nước hiện đang đông đá và... từ chối tham gia chấm điểm.". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gõ cửa chiếc tủ đông, bên trong chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương nằm im trong khối băng, đầu có biểu tượng "zzz"; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L81</summary>

```text
HÌNH L81 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đúng vậy! Đông đá thì không già, nhưng cũng không thi được! Gấu Nước tự loại mình khỏi vòng một vì... ngủ quá ngon!". Bố cục: Khán đài cười nghiêng ngả, anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng ôm bụng cười, phía sau tủ đông là khối băng chứa chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương có dán miếng băng dính vẽ biểu tượng tạm dừng.
```
</details>

<details><summary>L82</summary>

```text
HÌNH L82 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và đây là kết quả vòng một! Huy chương đồng: Gấu Koala, bậc thầy ôm cây giải nhiệt và uống nước mưa!". Bố cục: Bục trao giải ba bậc: chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ đứng ở bậc đồng, cổ đeo huy chương đồng, tay vẫn ôm một khúc cây nhỏ, mặt ngơ ngác; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L83</summary>

```text
HÌNH L83 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Huy chương bạc: Chồn Gulo, kiến trúc sư đường hầm dưới tuyết dày!". Bố cục: chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh đứng ở bậc bạc, đeo huy chương bạc, giơ nắm tay ăn mừng, tuyết rơi trên vai; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L84</summary>

```text
HÌNH L84 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và huy chương vàng vòng một thuộc về... tuyển thủ mà chuyên gia nói tham gia cho vui: Thú Mỏ Vịt, người bơi 5 tiếng trong nước 0 độ mà vẫn ấm!". Bố cục: chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá đứng trên bậc vàng cao nhất, đeo huy chương vàng to, băng đô xanh, khóc vì xúc động, pháo giấy rơi khắp nơi; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L85</summary>

```text
HÌNH L85 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bảng điểm sau vòng một: Thú Mỏ Vịt 3 điểm, Chồn Gulo 2 điểm, Koala 1 điểm. Còn Lửng Mật và Tôm Tít, hai ứng cử viên nặng ký... vẫn chưa có điểm nào!". Bố cục: tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) sáng lên: cột đèn của chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá cao nhất, cột chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh thấp hơn, cột chú gấu Koala hoạt hình mập tròn lông xám, tai tròn to xù mép trắng, mũi đen to hình quả lê, mắt to ngơ ngác, mặc áo choàng bệnh nhân trắng có chữ thập đỏ nhỏ thấp nữa, các cột khác tắt; bên dưới chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần và chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh khoanh tay hậm hực; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L86</summary>

```text
HÌNH L86 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đừng lo, vòng hai sẽ là vòng của những đôi chân. Và có người sẽ phải đi bộ... nửa vòng trái đất!". Bố cục: anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cầm micro đứng trước một tấm bản đồ thế giới khổng lồ có những đường chấm chấm uốn lượn rất dài, bên cạnh là một đôi giày chạy bộ.
```
</details>

<details><summary>L87</summary>

```text
HÌNH L87 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vòng hai: marathon sinh tồn! Trong tự nhiên, thức ăn không tự bò đến miệng. Muốn sống, phải đi. Và có những tuyển thủ đi xa đến mức... bản đồ phải vẽ thêm trang!". Bố cục: Đường đua marathon hoạt hình chạy vòng quanh một quả địa cầu khổng lồ, vạch xuất phát có cổng bóng bay, anh MC hoạt hình vest đỏ nơ bướm vàng cầm micro vàng cầm cờ hiệu đứng ở vạch xuất phát.
```
</details>

<details><summary>L88</summary>

```text
HÌNH L88 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giám khảo sẽ chấm hai tiêu chí: quãng đường đi được, và độ khó của hành trình. Mời tuyển thủ đầu tiên!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ cầm đồng hồ bấm giờ và chiếc thước dây cuộn tròn khổng lồ, ngồi trên chiếc ghế cao bên đường đua.
```
</details>

<details><summary>L89</summary>

```text
HÌNH L89 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lửng Mật xuất phát! Không cần khởi động! Không cần bản đồ! Chỉ cần cái mũi!". Bố cục: chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần lao ra khỏi vạch xuất phát, mũi dí sát mặt đất đánh hơi, bụi cát bay mù mịt phía sau; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L90</summary>

```text
HÌNH L90 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà khoa học ở sa mạc Kalahari đã đeo vòng cổ định vị cho 25 con Lửng Mật, rồi kiên nhẫn đi theo chúng suốt nhiều năm.". Bố cục: Một chiếc xe địa hình hoạt hình chạy theo sau một chú chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần đeo vòng cổ có ăng-ten nhỏ, giữa sa mạc cát đỏ có bụi gai; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L91</summary>

```text
HÌNH L91 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kết quả: mỗi đêm đi kiếm ăn, một con Lửng Mật đực đi trung bình gần 14km. Có những ngày còn đi tới 27km!". Bố cục: Một tấm bản đồ sa mạc với đường đi ngoằn ngoèo zíc zắc rất dài màu đỏ, ở cuối đường là chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần thở hổn hển nhưng vẫn ngẩng cao đầu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L92</summary>

```text
HÌNH L92 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và đi không phải để dạo chơi. Trong một lần đi kiếm ăn, Lửng Mật có thể đào tới 50 cái hố để lôi chuột và thằn lằn ra khỏi hang.". Bố cục: Mặt đất sa mạc lỗ chỗ hàng chục cái hố nhỏ như mặt bánh tổ ong, chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần chui đầu xuống một hố, chỉ thấy cái mông và cái đuôi vẫy vẫy; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L93</summary>

```text
HÌNH L93 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và có một chuyện mà ít ai biết: Lửng Mật không bao giờ đi một mình. Trên đầu nó thường có... một đoàn tùy tùng bay theo!". Bố cục: chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần đang đào đất, phía trên trời có ba con chim ưng màu xám bạc chân đỏ lượn vòng theo sát như đoàn hộ tống; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L94</summary>

```text
HÌNH L94 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đó là loài chim ưng xám có tiếng hót như đang hát. Chúng bám theo Lửng Mật, chờ nó đào hang. Con chuột nào hoảng hốt chạy thoát lên mặt đất... là chim ưng sà xuống chộp liền!". Bố cục: Một con chuột hoảng hốt chạy vọt ra khỏi miệng hố, một con chim ưng xám sà xuống chộp gọn; trong hố chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần vẫn đang đào hăng say không hề hay biết; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L95</summary>

```text
HÌNH L95 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà khoa học đã từng thấy tới 6 con chim ưng cùng đi theo một con Lửng Mật. Và chim ưng săn mồi thành công hơn hẳn khi đi theo Lửng Mật so với khi tự săn.". Bố cục: Sáu con chim ưng xám đậu thành hàng trên cành cây khô, đầu đồng loạt quay theo chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần đang đi bên dưới, như hàng ghế khán giả theo dõi trận đấu; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L96</summary>

```text
HÌNH L96 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn Lửng Mật được gì từ đoàn tùy tùng này? Các nhà khoa học đo đạc kỹ và trả lời: không được gì cả. Không mất gì, cũng chẳng được gì.". Bố cục: chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần quay lại nhìn lên đàn chim ưng với vẻ mặt thờ ơ, nhún vai, trên đầu là bong bóng suy nghĩ vẽ con số không tròn trĩnh to tướng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L97</summary>

```text
HÌNH L97 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một gã giang hồ đi đâu cũng có đàn em bám theo hưởng sái, mà bản thân gã... chẳng thèm để ý!". Bố cục: Cảnh hài: chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần đi trước như đại ca, phía sau là sáu chim ưng đi bộ lạch bạch xếp hàng như đàn em, mỗi con ngậm một con chuột nhỏ; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L98</summary>

```text
HÌNH L98 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng nếu Lửng Mật đi xa trong một đêm, thì có một tuyển thủ đi xa... trong cả một mùa xuân. Hồ sơ M56.". Bố cục: Một tấm hồ sơ mật bìa nâu có con dấu hình móng vuốt, bên trong kẹp ảnh chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh trẻ đeo vòng cổ định vị; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>L99</summary>

```text
HÌNH L99 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mùa xuân năm 2009, một chú Chồn Gulo đực còn trẻ, được đặt mã số M56, rời khỏi vùng núi gần công viên quốc gia Grand Teton ở bang Wyoming, nước Mỹ.". Bố cục: Dãy núi đá tuyết hùng vĩ hoạt hình, chú Chồn Gulo (Wolverine) hoạt hình lùn mập chắc nịch, lông nâu sẫm có hai dải sọc vàng kem dọc hai bên sườn, bàn chân bè rất to như ủng trượt tuyết, mắt tinh quái liều lĩnh trẻ đứng trên mỏm đá nhìn về phía chân trời phía Nam, ba lô nhỏ trên lưng; KHÔNG có anh MC trong cảnh này.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Mười quái kiệt. Tám vòng thi. Một chiếc vương miện!". Bố cục: tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ (không có chữ, không có số) dựng giữa sân vận động ban đêm, phía trên lơ lửng chiếc vương miện vàng bé xíu phát sáng, mười cái bóng tuyển thủ đứng bên dưới.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Lửng Mật, Tôm Tít, Gấu Nước được dự đoán sẽ thắng. Còn Thú Mỏ Vịt... tham gia cho vui!". Bố cục: chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần, chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi điểm màu cầu vồng, hai mắt to lồi trên cuống, hai càng búa gập trước ngực như võ sĩ quyền anh và chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương đứng oai vệ trên ba cột điểm cao vút, bên dưới chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá đeo băng đô xanh đứng cạnh một cột điểm thấp lè tè.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Vòng một: Thú Mỏ Vịt bơi 5 tiếng trong nước 0°C mà thân nhiệt không hề tụt!". Bố cục: chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá bơi thong thả giữa dòng sông có băng trôi, quanh người là vầng hào quang cam ấm áp.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Vòng hai: Chim Cánh Cụt đi 13.000km mỗi năm, theo mặt trời quanh Nam Cực!". Bố cục: chú chim cánh cụt Adélie hoạt hình nhỏ tròn, đầu và lưng đen tuyền, bụng trắng, vòng trắng tròn quanh mắt, chân hồng cam, đeo nơ bướm đỏ ở cổ đi lạch bạch trên băng hướng về phía mặt trời hoàng hôn, phía sau là đường chấm đỏ uốn quanh bản đồ Nam Cực.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Vòng sáu: Cá Heo bắt cá cùng ngư dân Brazil, giúp họ bắt được cá cao gấp 17 lần!". Bố cục: chú Cá Heo mũi chai hoạt hình màu xám xanh, miệng luôn cong thành nụ cười tinh quái lặn ngoắt xuống nước trước mặt một người đánh cá đang quăng lưới tròn giữa không trung.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Vòng bảy: tin đồn gấu nước còn sống trên Mặt Trăng bị khoa học... bắn hạ bằng súng khí!". Bố cục: Viên đạn nhựa nhỏ bay vèo trong phòng thí nghiệm, bên trong là chú Gấu Nước (tardigrade) hoạt hình tí hon mũm mĩm như gấu bông 8 chân ngắn có móng nhỏ, thân màu be nhạt có nếp gấp, miệng tròn dạng ống, mắt chấm nhỏ dễ thương đang ngủ, đâm vào bao cát tung bụi.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Lửng Mật thì sao? Lần đầu tiên trong đời... chịu thừa nhận mình chưa chắc đúng!". Bố cục: chú Lửng Mật hoạt hình thân đen, lưng phủ một mảng lông trắng bạc từ đỉnh đầu xuống đuôi, chân ngắn móng vuốt dài, vẻ mặt ngông nghênh bất cần quay mặt đi bĩu môi nhưng vẫn gật đầu, giơ một tay lên như đầu hàng, bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ gõ búa phía sau.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Chung kết: ai giúp ích cho loài người nhiều nhất? Sữa Thú Mỏ Vịt diệt khuẩn, nọc độc có thể thành thuốc chữa tiểu đường!". Bố cục: chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá mặc áo blouse trắng đứng sau quầy thuốc dưới nước, kệ phía sau có lọ thuốc giọt sữa trắng và giọt nọc tím.
```
</details>

<details><summary>S09</summary>

```text
HÌNH S09 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Và nhà vô địch là... con vật từng bị các nhà khoa học tưởng là đồ giả khâu ghép!". Bố cục: chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá đứng trên bục cao nhất đội vương miện vàng bé xíu, đeo ba huy chương vàng, khóc vì sung sướng, pháo hoa nổ rực trời.
```
</details>

<details><summary>S10</summary>

```text
HÌNH S10 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Bạn có đồng ý không? Xem trọn tám vòng thi trong video dài nhé, vì ở đây chỉ có mười quái kiệt, tám vòng thi, và một chiếc vương miện!". Bố cục: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ và mười tuyển thủ cùng quay sang nhìn thẳng ra người xem, chú Thú Mỏ Vịt hoạt hình lông nâu bùn, mỏ vịt mềm màu xám đen, đuôi dẹt như đuôi hải ly, chân có màng bơi, đeo băng đô thể thao màu xanh lá ở giữa giơ vương miện lên như mời người xem.
```
</details>

<details><summary>S11</summary>

```text
HÌNH S11 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật anh MC vest đỏ nơ bướm vàng cầm micro vàng và 10 tuyển thủ động vật hoạt hình của Đại Hội Sinh Tồn; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "vì ở đây chỉ có mười quái kiệt, tám vòng thi, và một chiếc vương miện!". Bố cục: tấm bảng điểm khổng lồ hình chiếc khiên dựng giữa sân vận động, có 10 cột đèn màu bên cạnh 10 hình đầu con vật nhỏ, phía trên lơ lửng chiếc vương miện vàng bé xíu phát sáng lấp lánh, mười cái bóng tuyển thủ đứng phía dưới nhìn lên.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/471 của video YouTube về 10 quái kiệt — Đại Hội Sinh Tồn). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: anh MC dẫn chương trình hoạt hình vui tính: tóc vuốt dựng, mặc bộ vest đỏ tươi, thắt nơ bướm vàng, cầm chiếc micro vàng, nụ cười rộng. Nhân vật phụ cố định: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/10 của video YouTube Shorts về 10 quái kiệt — Đại Hội Sinh Tồn). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: anh MC dẫn chương trình hoạt hình vui tính: tóc vuốt dựng, mặc bộ vest đỏ tươi, thắt nơ bướm vàng, cầm chiếc micro vàng, nụ cười rộng. Nhân vật phụ: bà cú mèo giám khảo hoạt hình đeo kính tròn gọng vàng, khoác áo choàng tím, cầm búa gỗ nhỏ. 
```
</details>

## 7. SEO

- **title:** [TẬP ĐẶC BIỆT {MINUTES} PHÚT] 10 Quái Kiệt Thi Đấu 8 Vòng Sinh Tồn: Ai Lên Ngôi Vô Địch?
- **hook_paragraph:** Mười sinh vật kỳ dị nhất kênh Vẽ Chuyện Hoang Dã — Lửng Mật, Tôm Tít, Gấu Nước, Chồn Gulo, Chim Cánh Cụt, Rái Cá Biển, Cá Heo, Chim Bồ Nông, Thú Mỏ Vịt và Gấu Koala — bước vào Đại Hội Sinh Tồn với 8 vòng thi và giải phụ: chịu nóng lạnh, marathon, bếp trưởng, giác quan, cha mẹ, đồng đội, phúc khảo tin đồn, giải thưởng phụ và chung kết món quà cho loài người. Toàn bộ là sự thật khoa học MỚI chưa từng kể trong 10 tập lẻ, kèm nguồn nghiên cứu: Koala ôm cây làm điều hòa, chồn Gulo đi bộ 800km, cánh cụt đi 13.000km mỗi năm theo mặt trời, cá heo bắt cá cùng ngư dân Brazil, gấu nước bị bắn bằng súng khí… và một nhà vô địch không ai ngờ tới!
- **question:** Nếu bạn là giám khảo, bạn sẽ trao vương miện cho ai? Viết tên nhà vô địch của bạn ở phần bình luận nhé!
- **next_teaser:** Đại Hội Sinh Tồn #2 — 10 gương mặt mới, có cả tôm súng bắn đại bác nước
- **shorts_title:** 10 Quái Kiệt Thi Đấu – Ai Lên Ngôi?! 👑 #shorts #dongvat
- **shorts_desc:** Lửng Mật, Tôm Tít hay Gấu Nước? Kết quả Đại Hội Sinh Tồn khiến cả khán đài sững sờ — nhà vô địch là con vật từng bị tưởng là đồ giả! 👑
👉 Xem trọn Đại Hội Sinh Tồn — tập đặc biệt trên kênh Vẽ Chuyện Hoang Dã.
- **bullets:** Vòng 1 – Nóng & lạnh: Koala ôm cây mát hơn 5°C, Thú Mỏ Vịt bơi 5 tiếng trong nước 0°C, gấu nước không già khi đông đá · Vòng 2 – Marathon: Lửng Mật 14km/đêm, chồn Gulo M56 đi 800km, cánh cụt 13.000km/năm, tôm tít lăn như bánh xe · Vòng 3 – Bếp trưởng: sữa thú mỏ vịt diệt khuẩn, rái cá dùng đá giữ răng, bồ nông bay chữ V, sự thật chim dẫn mật · Vòng 4 – Giác quan: rái cá sờ nhanh gấp 30 lần người, cá heo canh gác 15 ngày không ngủ, cánh cụt ngủ 4 giây · Vòng 5 – Cha mẹ: lửng mẹ chuyển hang 3 ngày/lần, thú mỏ vịt ấp trứng 10 ngày, cá heo mẹ nói giọng nựng con · Vòng 6 – Đồng đội: cá heo bắt cá cùng ngư dân Laguna, cá heo nhớ tên bạn sau 20 năm, tôm tít đấm khiên đo sức · Vòng 7 – Phúc khảo: mắt tôm tít, gấu nước trên Mặt Trăng, bồ nông lấy máu nuôi con, Koala không uống nước · Giải phụ & Chung kết: cá heo Nicklo 67 tuổi, cơ bắp rái cá rò nhiệt, gen gấu nước, nọc thú mỏ vịt chữa tiểu đường
- **tags:** vẽ chuyện hoang dã, đại hội sinh tồn, thế giới động vật, động vật kỳ lạ, thú mỏ vịt, lửng mật, tôm tít, gấu nước, chồn gulo, chim cánh cụt, rái cá biển, cá heo, chim bồ nông, gấu koala, khoa học thú vị, whiteboard animation, sự thật động vật, nghe trước khi ngủ
- **hashtags:** #VeChuyenHoangDa #TheGioiDongVat #DaiHoiSinhTon #DongVatKyLa #KhoaHoc

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/mega-01-dai-hoi-sinh-ton
python src/episode/pipeline.py tts    projects/mega-01-dai-hoi-sinh-ton     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/mega-01-dai-hoi-sinh-ton     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/mega-01-dai-hoi-sinh-ton     # phải in 'spec OK'
python scripts/audit_beats.py projects/mega-01-dai-hoi-sinh-ton              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/mega-01-dai-hoi-sinh-ton --force
python scripts/beat_sheet.py projects/mega-01-dai-hoi-sinh-ton               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/mega-01-dai-hoi-sinh-ton/audio/shorts.wav projects/mega-01-dai-hoi-sinh-ton/renders/mega-01-dai-hoi-sinh-ton_shorts.mp4
python src/episode/pipeline.py qa     projects/mega-01-dai-hoi-sinh-ton
python src/episode/pipeline.py seo    projects/mega-01-dai-hoi-sinh-ton
python src/episode/episode_doc.py     projects/mega-01-dai-hoi-sinh-ton
```
