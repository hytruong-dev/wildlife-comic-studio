# TẬP 25 — BẠCH TUỘC MIMIC · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-25-bach-tuoc-mimic`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-25-bach-tuoc-mimic`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F6` · **Persona giọng:** `ong_trum` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Bạch Tuộc Mimic |
| Tiêu đề YouTube | Sinh Vật 9 Bộ Não Biến Hình Thành 15 Loài Kịch Độc Dưới Đáy Biển?! |
| Video dài | `renders/tap-25-bach-tuoc-mimic_long.mp4` — 9:09.7 (549.7s) |
| Shorts | `renders/tap-25-bach-tuoc-mimic_shorts.mp4` — 0:51.5 (51.5s) |
| Thumbnail | `renders/tap-25-bach-tuoc-mimic_thumbnail.jpg` |
| Số hình | dài 74 beat / 74 ảnh riêng; Shorts 10 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.1**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/74 của video YouTube về Bạch Tuộc Mimic). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn. Nhân vật phụ cố định: ông trùm điệp báo thế giới ngầm hoạt hình mặc áo măng-tô đen; cô đặc vụ tình báo hoạt hình đeo tai nghe bộ đàm. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — BẬC THẦY HÓA TRANG THẾ GIỚI NGẦM ĐÁY CÁT
*Badge:* `HỒ SƠ ĐIỆP BÁO` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene01_p0.wav` (400 ký tự) · mood `tram_bi_an`

```text
Trong thế giới ngầm của đại dương bao la, có những luật lệ sinh tồn khắc nghiệt... không bao giờ được viết thành văn. Kẻ yếu thì phải biết ẩn mình trong bóng tối, kẻ mạnh thì phô trương nanh vuốt săn lùng. Nhưng gia đình này thì chọn một con đường hoàn toàn khác: không có vỏ bọc cứng, không có nanh vuốt nhọn, không có độc tố chết người, nhưng bất kỳ ai trong thế giới ngầm cũng phải ngả mũ kính sợ!
```
**Part 1** → `audio/vs/scene01_p1.wav` (83 ký tự) · 🎭 cameo `co_tro_ly`

```text
Chào đại ca, hôm nay có mục tiêu nào cần đội tình báo chúng em đi điều tra không ạ?
```
**Part 2** → `audio/vs/scene01_p2.wav` (614 ký tự) · mood `hao_hung`

```text
[surprise-oh] Bật màn hình máy quét bảo mật lên, hôm nay chúng ta giải mã hồ sơ của một siêu điệp viên thực thụ! [laughter] Xin giới thiệu với toàn thể anh em: đây là Bạch Tuộc Mimic, tên khoa học là Thaumoctopus mimicus. Loài sinh vật bí ẩn này chỉ mới được các thợ lặn phát hiện lần đầu tiên vào năm một ngàn chín trăm chín mươi tám ngoài khơi đảo Xu-la-wê-xi thuộc In-đô-nê-xi-a. Chiều dài sải tay khi bung rộng khoảng sáu mươi xăng-ti-mét. Nhìn bề ngoài nó giống hệt những chú bạch tuộc thân mềm thông thường, nhưng trong thế giới ngầm đại dương, chúng tôi gọi thẳng tên nó bằng biệt danh: Điệp Viên Đại Dương!
```
**Part 3** → `audio/vs/scene01_p3.wav` (524 ký tự) · mood `nghiem_trang_gia`

```text
Điều khiến mọi cơ quan tình báo biển sâu phải kinh ngạc là gã không chọn cách lẩn trốn trong hang hốc tối tăm như các loài bạch tuộc khác! Điệp Viên Đại Dương chọn lộ diện ban ngày ngay giữa những bãi cát ngầm trống trải, nơi đầy rẫy những con cá săn mồi đói khát lượn lờ. Và vũ khí sinh tồn tối thượng của gã chính là tài năng hóa trang vô tiền khoáng hậu: có thể biến hình mượt mà thành mười lăm loài sinh vật kịch độc khác nhau! Đêm nay, tôi mời anh em cùng lật mở từng trang hồ sơ tuyệt mật của gã điệp viên đại tài này!
```

### scene02 — HÓA THÂN RẮN BIỂN CẠP NONG VÀ CÁ SƯ TỬ GAI ĐỘC
*Thẻ chương:* BIẾN 2 XÚC TU THÀNH RẮN BIỂN KỊCH ĐỘC

*Badge:* `DANH TÍNH GIẢ #1` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene02_p0.wav` (311 ký tự) · mood `tram_bi_an`

```text
Lật mở trang hồ sơ đầu tiên: Tuyệt kỹ hóa thân thành sát thủ kịch độc! Hãy quan sát một hiện trường thực tế dưới đáy cát: một đàn cá thia hung hăng phát hiện ra Điệp Viên Đại Dương và bắt đầu bao vây lao tới định tấn công rỉa thịt. Ở một góc ngách không có đường lui, gã điệp viên làm gì? Chạy trốn ư? Không hề!
```
**Part 1** → `audio/vs/scene02_p1.wav` (437 ký tự) · mood `don_dap`

```text
Gã lập tức thụt sáu chiếc xúc tu và toàn bộ phần thân đầu chui tọt vào trong một chiếc hang cát hẹp! Chỉ chừa lại đúng hai chiếc xúc tu thò ra ngoài, uốn éo theo hai hướng đối diện nhau. Đồng thời, làn da chuyển đổi sang họa tiết khoang đen trắng xen kẽ nổi bật... Trong vòng chưa đầy một giây, trước mắt đàn cá thia không còn là một con bạch tuộc mềm yếu nữa, mà là một con Rắn Biển Cạp Nong kịch độc đang le lưỡi săn mồi! [surprise-wa]
```
**Part 2** → `audio/vs/scene02_p2.wav` (368 ký tự) · mood `hao_hung`

```text
Cá thia nhìn thấy tử thần rắn biển thì hồn xiêu phách lạc, lập tức quay đầu tháo chạy bạt mạng! Điều chấn động giới khoa học được tiến sĩ Norman công bố năm hai ngàn lẻ một: Điệp Viên Đại Dương không bắt chước ngẫu nhiên! Khi bị loài cá nào đe dọa, gã lập tức phân tích và chọn đúng loài thiên địch kịch độc của chính kẻ tấn công đó để hóa trang dọa lại! [surprise-oh]
```
**Part 3** → `audio/vs/scene02_p3.wav` (440 ký tự) · mood `don_dap`

```text
Và nếu kẻ thù lần này là một con cá nhồng hung dữ bơi lượn ở tầng nước lơ lửng thì sao? Gã liền kích hoạt danh tính giả số hai: bơi nhấc mình lên khỏi đáy cát, xòe rộng cả tám chiếc xúc tu tỏa ra xung quanh như những chiếc gai nhọn phấp phới, đổi màu da sang vệt nâu sọc trắng! Bùm! Trước mắt kẻ săn mồi bỗng xuất hiện một chú Cá Sư Tử gai độc đầy gai nhọn chết người! Kẻ địch nhìn thấy gai độc liền ngán ngẩm bỏ đi ngay lập tức! [laughter]
```
**Part 4** → `audio/vs/scene02_p4.wav` (425 ký tự) · mood `hao_hung`

```text
Các thợ lặn chuyên nghiệp từng quay được khoảnh khắc gã điệp viên này đang ung dung bơi thì chạm trán một con cá đuối lớn. Trong tích tắc không cần suy nghĩ, gã lập tức gập các xúc tu lại, phè thân mình ra phẳng lì và uốn lượn hệt như một con cá đuối gai độc con! Con cá đuối lớn nhìn thấy tưởng đồng loại đang đi dạo liền bơi lướt qua luôn mà không hề nghi ngờ! Nghệ thuật đánh lừa thị giác đã đạt tới cảnh giới thượng thừa!
```

### scene03 — GIẢ DẠNG CÁ BƠN LƯỚT CÁT VÀ SỨA BIỂN BỒNG BỀNH
*Thẻ chương:* ÉP TOÀN BỘ CƠ THỂ THÀNH CHIẾC LÁ CÁ BƠN

*Badge:* `DANH TÍNH GIẢ #2` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene03_p0.wav` (361 ký tự) · mood `tram_bi_an`

```text
Chuyển sang trang hồ sơ thứ hai: Tuyệt chiêu tàng hình khi di chuyển đường dài! Trong thế giới ngầm, việc di chuyển băng qua những bãi cát trống trải mênh mông là nhiệm vụ nguy hiểm nhất, vì bóng dáng bạch tuộc bơi lội rất dễ thu hút ánh nhìn của lũ cá mập từ xa. Nhưng Điệp Viên Đại Dương của chúng ta lại có một bộ trang phục ngụy trang đường trường đỉnh cao!
```
**Part 1** → `audio/vs/scene03_p1.wav` (435 ký tự) · mood `hao_hung`

```text
Gã ép sát toàn bộ thân mình xuống sát mặt cát, chụm cả tám chiếc xúc tu kéo dài ra phía sau thành hình giọt nước dẹt như một chiếc lá cây. Làn da chuyển sang màu nâu cát lốm đốm, và dùng chiếc phễu đẩy nước lướt nhẹ nhàng là là trên mặt đáy biển... Trông gã lúc này chẳng khác nào một con Cá Bơn độc đang bơi lướt sóng cát! [surprise-oh] Kẻ săn mồi từ trên cao nhìn xuống chỉ thấy một con cá bơn nhạt nhẽo chán ngấy liền lướt qua luôn!
```
**Part 2** → `audio/vs/scene03_p2.wav` (111 ký tự) · 🎭 cameo `co_tro_ly`

```text
Đại ca ơi, thế nếu đang bơi giữa dòng nước mà gặp nguy hiểm không có cát để bám thì anh em tẩu thoát kiểu gì ạ?
```
**Part 3** → `audio/vs/scene03_p3.wav` (474 ký tự) · mood `hao_hung`

```text
[laughter] Yên tâm đi trợ lý! Nếu bị đẩy lên tầng nước giữa, gã lập tức cuộn tròn các xúc tu lại, phồng to phần đầu như một chiếc ô dù trong suốt rồi bập bùng co bóp bơi giật lùi... Biến hình ngay thành một chú Sứa Biển trôi dạt lững lờ! Kẻ thù thấy sứa đầy nọc châm thì tránh xa cả chục mét! Chưa hết, gã còn có thể giả thành cá đuối gai độc, hải quỳ khổng lồ, thậm chí cả tôm tít gập càng! Mười lăm khuôn mặt, mười lăm danh tính giả hoàn hảo cho mọi tình huống hiểm nghèo!
```
**Part 4** → `audio/vs/scene03_p4.wav` (406 ký tự) · mood `don_dap`

```text
Thậm chí khi cần đi săn những chú cua nhỏ nhút nhát nấp trong hang đá, Điệp Viên Đại Dương còn dùng chiêu hóa trang ngược: biến hình thành một chú cua biển thân thiện giơ hai càng vẫy chào mời gọi bạn ra chơi! Con mồi vừa tò mò bước ra khỏi hang liền bị tám chiếc xúc tu thò ra tóm gọn sạch sẽ! Đúng là gã giang hồ vừa đóng vai cảnh sát, vừa đóng vai cướp biển, không ai lường trước được nước đi tiếp theo!
```

### scene04 — MẠNG LƯỚI THẦN KINH PHI TẬP TRUNG SIÊU ĐẲNG
*Thẻ chương:* 8 XÚC TU HOẠT ĐỘNG NHƯ 8 BỘ NÃO RIÊNG BIỆT

*Badge:* `ĐẾ CHẾ 9 BỘ NÃO` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene04_p0.wav` (266 ký tự) · mood `tram_bi_an`

```text
Bước vào trang hồ sơ tối mật thứ ba: Bí mật phần cứng siêu máy tính sinh học! Làm thế nào mà một sinh vật thân mềm không xương lại có thể nhớ và điều khiển trơn tru tới mười lăm hình thái biến hình phức tạp đến từng chuyển động gợn sóng cơ bắp như vậy? [question-oh]
```
**Part 1** → `audio/vs/scene04_p1.wav` (278 ký tự) · mood `don_dap`

```text
Câu trả lời nằm ở cấu tạo hệ thần kinh kỳ dị bậc nhất hành tinh: Điệp Viên Đại Dương sở hữu tới chín bộ não độc lập! Một bộ não trung tâm hình bánh vòng nằm quanh thực quản ở phần đầu, và tám cụm hạch thần kinh khổng lồ nằm dọc suốt chiều dài của tám chiếc xúc tu! [surprise-wa]
```
**Part 2** → `audio/vs/scene04_p2.wav` (446 ký tự) · mood `hao_hung`

```text
Trong tổng số hơn năm trăm triệu tế bào nơ-ron thần kinh của cơ thể — tương đương số lượng nơ-ron của một chú chó thông minh — thì có tới hai phần ba số nơ-ron nằm rải rác bên trong tám chiếc xúc tu! Điều này có nghĩa là mỗi xúc tu của gã hoạt động như một thực thể độc lập có ý thức riêng: tự nếm vị giác bằng các giác hút, tự cảm nhận nhiệt độ, tự quyết định luồn lách vào khe đá săn mồi mà không cần chờ lệnh từ não bộ trung tâm! [surprise-oh]
```
**Part 3** → `audio/vs/scene04_p3.wav` (350 ký tự) · mood `hao_hung`

```text
Não trung tâm chỉ đưa ra mệnh lệnh chiến lược tối cao: Giả thành rắn biển! Ngay lập tức, hai xúc tu nhận lệnh tự động phối hợp màu sắc và cử động uốn lượn nhịp nhàng, trong khi sáu xúc tu còn lại tự tìm khe cát giấu mình! Sự phân quyền chỉ huy thần kinh tuyệt đỉnh này giúp gã phản xạ biến hình chỉ trong vòng chưa đầy không phẩy hai giây! [laughter]
```
**Part 4** → `audio/vs/scene04_p4.wav` (390 ký tự) · mood `nghiem_trang_gia`

```text
Các nhà khoa học thần kinh từng làm thí nghiệm thử thách trí tuệ của loài bạch tuộc: đặt thức ăn bên trong một chiếc lọ thủy tinh có nắp vặn ren kín mít. Không cần ai dạy bảo, các xúc tu của gã tự phối hợp vặn mở nắp lọ chỉ trong vài chục giây để lấy thức ăn! Trí thông minh phân tán này đang là nguồn cảm hứng số một cho các kỹ sư chế tạo robot mềm và hệ thống trí tuệ nhân tạo thế hệ mới!
```

### scene05 — MÁU XANH LAM GỐC ĐỒNG VÀ 3 TẦNG TẾ BÀO ĐỔI MÀU
*Thẻ chương:* ĐỔI MÀU CƠ HỌC BẰNG HÀNG TRIỆU TÚI SẮC TỐ TRONG 0,2 GIÂY

*Badge:* `MÀN HÌNH NANO` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene05_p0.wav` (427 ký tự) · mood `nghiem_trang_gia`

```text
Lật sang trang hồ sơ thứ tư: Công nghệ màn hình hiển thị nano trên da và dòng máu quý tộc! Khác với tắc kè hoa đổi màu chậm chạp nhờ hoóc-môn trong máu mất hàng phút, da của Điệp Viên Đại Dương là một chiếc màn hình tinh thể lỏng sinh học độ phân giải siêu nét! Làn da của gã chứa ba tầng tế bào đổi màu đặc biệt: tầng trên cùng là hàng triệu túi sắc tố Crô-ma-tô-pho màu nâu, đen, vàng, đỏ được bao quanh bởi các sợi cơ li ti.
```
**Part 1** → `audio/vs/scene05_p1.wav` (428 ký tự) · mood `don_dap`

```text
Chỉ cần sợi thần kinh giật nhẹ một xung điện, các sợi cơ lập tức co lại, kéo căng túi sắc tố to ra gấp mười lần để hiện màu! Cơ thả lỏng thì túi co lại biến mất! Quá trình đổi màu diễn ra hoàn toàn bằng cơ học thuần túy trong chưa đầy không phẩy hai giây! Phía dưới còn có tầng tế bào khúc xạ ánh sáng và phản chiếu ánh sáng trắng, giúp gã pha trộn mọi dải màu và tạo vân da sần sùi hệt như hạt cát hay rạn san hô! [surprise-oh]
```
**Part 2** → `audio/vs/scene05_p2.wav` (347 ký tự) · mood `hao_hung`

```text
Và dòng máu chảy bên trong cơ thể gã điệp viên này cũng mang sắc màu huyền thoại: Máu có màu xanh lam óng ánh! [surprise-wa] Vì sống dưới đáy biển sâu lạnh giá nghèo oxy, cơ thể gã không dùng chất sắt hemoglobin màu đỏ như con người, mà sử dụng phân tử protein Hê-mô-xy-a-nin chứa nguyên tử đồng để vận chuyển oxy hiệu quả gấp bội trong nước lạnh!
```
**Part 3** → `audio/vs/scene05_p3.wav` (462 ký tự) · mood `nghiem_trang_gia`

```text
Để bơm dòng máu xanh lam này đi khắp chín bộ não và tám xúc tu, gã trang bị tới ba quả tim độc lập: hai quả tim mang chuyên hút máu đẩy qua hai bên mang để nạp oxy, và một quả tim chính khỏe khoắn bơm máu đi nuôi toàn bộ cơ thể! Nhưng khi gã bơi nước rút với tốc độ cao, quả tim chính sẽ tạm thời ngừng đập để dồn toàn lực cho cơ bắp, khiến gã nhanh kiệt sức và chỉ bơi từng đoạn ngắn rồi lại tàng hình ẩn nấp! Đúng là phong cách điệp viên hành động chớp nhoáng!
```
**Part 4** → `audio/vs/scene05_p4.wav` (365 ký tự) · mood `hao_hung`

```text
Không chỉ đổi màu sắc, làn da của gã còn có thể thay đổi kết cấu vật lý ba đê trong nháy mắt! Bằng cách co thắt các bó cơ biểu bì dưới da, gã có thể làm nổi lên những chiếc gai nhọn sần sùi như rạn san hô đá, hoặc làm phẳng lì trơn láng như hạt cát mịn. Mắt người nhìn vào không tài nào phân biệt nổi đâu là rạn đá tự nhiên và đâu là gã điệp viên đang nằm rình mồi!
```

### scene06 — TRÍ TUỆ MỀM VÀ BÓNG ĐEN MÔNG BỌC THÉP KỲ SAU
*Thẻ chương:* BÁO CÁO CUỐI CÙNG VÀ BÓNG ĐEN MÔNG BỌC THÉP TẬP 26

*Badge:* `KẾT LUẬN ĐIỆP BÁO` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene06_p0.wav` (351 ký tự) · mood `am_ap`

```text
Tổng kết hồ sơ điệp báo số hai mươi lăm. Giữa đại dương khắc nghiệt nơi mọi sinh vật đều chạy đua trang bị giáp dày gai nhọn, Điệp Viên Đại Dương đã chọn một con đường tiến hóa phi thường: lấy sự mềm mại linh hoạt làm vũ khí, lấy trí thông minh của chín bộ não làm khiên chắn, và dùng mười lăm danh tính giả để làm chủ hoàn toàn thế giới ngầm đáy cát!
```
**Part 1** → `audio/vs/scene06_p1.wav` (288 ký tự) · mood `hao_hung`

```text
Một sinh vật không hề có xương sống, nhưng lại sở hữu trí tuệ khiến con người phải kinh ngạc và tôn trọng sâu sắc! Đơn báo cáo cuối cùng: Cho phép điệp viên tiếp tục hoạt động ngầm tại vùng biển In-đô-nê-xi-a và tuyệt đối bảo mật danh tính! Ký tên: trùm điệp báo thế giới ngầm! [laughter]
```
**Part 2** → `audio/vs/scene06_p2.wav` (275 ký tự) · mood `hao_hung`

```text
Còn anh em thì sao? Nếu được sở hữu một trong hai năng lực của Điệp Viên Đại Dương: có chín bộ não để làm nhiều việc cùng lúc không lo quá tải, hay tài hóa trang biến hình thành người khác chỉ trong không phẩy hai giây, anh em chọn cái nào? Hãy để lại bình luận bên dưới nhé!
```
**Part 3** → `audio/vs/scene06_p3.wav` (627 ký tự) · mood `am_ap`

```text
Hồ sơ điệp viên số hai mươi lăm xin được niêm phong tại đây. Nhưng tập sau, chúng ta sẽ chuyển thẳng sang hồ sơ vũ khí tối mật trên đất liền để giải mã một chiến binh xe bọc thép lùn tịt cực kỳ lầy lội! Một sinh vật mũm mĩm đào hang ở nước Úc, nhưng sở hữu chiếc mông bọc thép dày cứng như bê tông cốt thép, chuyên lừa kẻ thù đuổi vào hang rồi gồng mông dập nát hộp sọ đối thủ vào trần hang đá! Chưa hết, nó là sinh vật duy nhất trên thế giới có dây chuyền cơ học thải ra những viên phân hình khối lập phương vuông vức như viên xúc xắc! Đố các bạn biết bóng đen bí ẩn kỳ sau là loài vật nào? Hãy đoán ngay ở phần bình luận nhé!
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Khi bị kẻ thù bao vây, con vật này không chạy trốn, mà lập tức biến hai chiếc xúc tu của mình thành một con rắn biển kịch độc le lưỡi dọa lại kẻ đi săn! [laughter] Xin giới thiệu Bạch Tuộc Mimic, siêu điệp viên sải tay sáu mươi xăng-ti-mét sống dưới đáy cát ở In-đô-nê-xi-a. Nó sở hữu tới chín bộ não độc lập, ba trái tim bơm dòng máu màu xanh lam óng ánh, và tài năng hóa trang vô tiền khoáng hậu: có thể biến hình mượt mà thành mười lăm loài sinh vật kịch độc khác nhau! [surprise-wa] Bị cá thia tấn công? Thụt thân vào hang, biến hai xúc tu thành rắn biển cạp nong! Gặp cá nhồng hung dữ? Xòe tám xúc tu bơi lơ lửng thành cá sư tử đầy gai độc! Cần di chuyển qua bãi cát trống? Ép dẹt toàn thân thành chiếc lá lướt sóng giả dạng cá bơn độc! [surprise-oh] Làn da của nó chứa hàng triệu túi sắc tố đổi màu cơ học chỉ trong không phẩy hai giây! Một bậc thầy tình báo thế giới ngầm không cần nanh vuốt vẫn khiến cả đại dương phải ngả mũ kính sợ!
```

**Whisper prompt:** `Bạch Tuộc Mimic, Điệp Viên Đại Dương, Thaumoctopus mimicus, Xu-la-wê-xi, Sulawesi, In-đô-nê-xi-a, Indonesia, rạn san hô, rắn biển cạp nong, cá sư tử, cá bơn, đĩa lưỡi, 9 bộ não, 3 trái tim, máu xanh lam, hemocyanin, sắc tố chromatophores, 60cm, 15 loài, 500 triệu, 0,2 giây, 1998, 2001`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| hai mươi lăm | 25 |
| hai mươi sáu | 26 |
| Mười lăm khuôn mặt | 15 khuôn mặt |
| Mười lăm danh tính | 15 danh tính |
| Mười lăm | 15 |
| mười lăm loài | 15 loài |
| mười lăm khuôn mặt | 15 khuôn mặt |
| mười lăm danh tính | 15 danh tính |
| mười lăm hình thái | 15 hình thái |
| mười lăm | 15 |
| chín bộ não | 9 bộ não |
| chín não | 9 não |
| ba trái tim | 3 trái tim |
| ba quả tim | 3 quả tim |
| tám xúc tu | 8 xúc tu |
| sáu xúc tu | 6 xúc tu |
| hai xúc tu | 2 xúc tu |
| hai chiếc xúc tu | 2 chiếc xúc tu |
| sáu mươi xăng-ti-mét | 60cm |
| hai mươi xăng-ti-mét | 20cm |
| cả chục mét | 10m |
| mười mét | 10m |
| hai phần ba | 2/3 |
| năm trăm triệu | 500 triệu |
| không phẩy hai giây | 0,2 giây |
| một giây | 1 giây |
| hai giây | 2 giây |
| ba mươi | 30 |
| năm hai ngàn lẻ một | 2001 |
| năm một ngàn chín trăm chín mươi tám | 1998 |
| hàng triệu | hàng triệu |
| hàng ngàn | hàng ngàn |
| một trăm phần trăm | 100% |
| mười lần | 10 lần |
| bốn mươi | 40 |
| bốn mươi loài | 40 loài |
| bốn hạng mục | 4 hạng mục |
| năm cấp độ | 5 cấp độ |
| thứ nhất | thứ 1 |
| thứ hai | thứ 2 |
| thứ ba | thứ 3 |
| thứ tư | thứ 4 |
| thứ năm | thứ 5 |
| ba đê | 3D |
| Xu-la-wê-xi | Sulawesi |
| In-đô-nê-xi-a | Indonesia |
| Hê-mô-xy-a-nin | Hemocyanin |
| hê-mô-xy-a-nin | hemocyanin |
| Crô-ma-tô-pho | Chromatophores |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · BẬC THẦY HÓA TRANG THẾ GIỚI NGẦM ĐÁY CÁT · 80.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:05.9 (5.9s) | L01 | Trong thế giới ngầm của đại dương bao la, có những luật lệ sinh tồn khắc nghiệt... không bao giờ được viết thành văn. |  | Đáy đại dương sâu thẳm trong bóng tối huyền bí: những vệt sáng lờ mờ chiếu qua rạn san hô đen, không khí thế giới ngầm căng thẳng. KHÔNG có chú bạch tuộc đội mũ phớt trong cảnh này. |
| b02 | 00:05.9–00:12.9 (7.0s) | L02 | Kẻ yếu thì phải biết ẩn mình trong bóng tối, kẻ mạnh thì phô trương nanh vuốt săn lùng. Nhưng gia đình này thì chọn một con đường hoàn toàn khác: |  | Chia đôi: BÊN TRÁI những chú cá nhỏ nhút nhát trốn sâu trong hốc đá tối; BÊN PHẢI con cá mập hổ dữ tợn giơ nanh vuốt săn lùng. KHÔNG có chú bạch tuộc đội mũ phớt trong cảnh này. |
| b03 | 00:12.9–00:19.6 (6.7s) | L03 | không có vỏ bọc cứng, không có nanh vuốt nhọn, không có độc tố chết người, nhưng bất kỳ ai trong thế giới ngầm cũng phải ngả mũ kính sợ! |  | chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn bơi lững lờ giữa làn nước sâu, khoanh tay ngạo nghễ, không vỏ cứng không gai nhọn nhưng toát lên thần thái của một đại ca thế giới ngầm. |
| b04 | 00:19.6–00:24.9 (5.3s) | L04 | Chào đại ca, hôm nay có mục tiêu nào cần đội tình báo chúng em đi điều tra không ạ? |  | cô đặc vụ tình báo hoạt hình đeo tai nghe bộ đàm đeo tai nghe bộ đàm giơ chiếc cặp tài liệu tuyệt mật màu đen cúi đầu chào chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn đang ngồi trên bục chỉ huy san hô. |
| b05 | 00:24.9–00:36.0 (11.1s) | L05 | Bật màn hình máy quét bảo mật lên, hôm nay chúng ta giải mã hồ sơ của một siêu điệp viên thực thụ! Xin giới thiệu với toàn thể anh em: đây là Bạch Tuộc Mimic, tên khoa học là Thaumoctopus mimicus. |  | ông trùm điệp báo thế giới ngầm hoạt hình mặc áo măng-tô đen mở màn hình máy quét bảo mật công nghệ cao, hiển thị bản đồ hồ sơ điệp viên Thaumoctopus mimicus phát sáng xanh lam. KHÔNG có chú bạch tuộc đội mũ phớt trong cảnh này. |
| b06 | 00:36.0–00:44.3 (8.3s) | L06 | Loài sinh vật bí ẩn này chỉ mới được các thợ lặn phát hiện lần đầu tiên vào 1998 ngoài khơi đảo Sulawesi thuộc Indonesia. | **1998** · phát hiện Sulawesi · L/350 · [0.35, 0.45] | Bản đồ Indonesia phóng to vùng biển Sulawesi và Bali năm 1998; các thợ lặn chuyên nghiệp cầm đèn pin ngỡ ngàng phát hiện chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn. |
| b07 | 00:44.3–00:47.3 (3.0s) | L07 | Chiều dài sải tay khi bung rộng khoảng 60cm. | **60 CM** · sải tay bung rộng · R/350 · [0.65, 0.5] | Ở GIỮA chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn bung rộng tám chiếc xúc tu vằn nâu trắng cạnh chiếc thước đo chiều cao 60cm màu vàng của cơ quan tình báo. |
| b08 | 00:47.3–00:56.6 (9.3s) | L08 | Nhìn bề ngoài nó giống hệt những chú bạch tuộc thân mềm thông thường, nhưng trong thế giới ngầm đại dương, chúng tôi gọi thẳng tên nó bằng biệt danh: Điệp Viên Đại Dương! |  | chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn tạo dáng điệp viên đeo kính râm đen giơ huy hiệu tình báo Điệp Viên Đại Dương lấp lánh màu vàng quyền lực. |
| b09 | 00:56.6–01:02.8 (6.2s) | L09 | Điều khiến mọi cơ quan tình báo biển sâu phải kinh ngạc là gã không chọn cách lẩn trốn trong hang hốc tối tăm như các loài bạch tuộc khác! |  | Bản đồ vệ tinh các hang hốc ngầm tối tăm nơi các loài bạch tuộc bình thường lẩn trốn trong bóng đêm. KHÔNG có chú bạch tuộc đội mũ phớt trong cảnh này. |
| b10 | 01:02.8–01:09.1 (6.2s) | L10 | Điệp Viên Đại Dương chọn lộ diện ban ngày ngay giữa những bãi cát ngầm trống trải, nơi đầy rẫy những con cá săn mồi đói khát lượn lờ. |  | chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn ngạo nghễ lướt đi giữa bãi cát ngầm trống trải ban ngày đầy nắng, xung quanh có bóng cá săn mồi lượn lờ từ xa. |
| b11 | 01:09.1–01:15.7 (6.7s) | L11 | Và vũ khí sinh tồn tối thượng của gã chính là tài năng hóa trang vô tiền khoáng hậu: có thể biến hình mượt mà thành 15 loài sinh vật kịch độc khác | **15 LOÀI** · danh tính biến hình · R/350 · [0.65, 0.48] | Vòng tròn 15 chiếc mặt nạ danh tính kịch độc xoay quanh chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn: rắn biển, cá sư tử, cá bơn, sứa biển, cá đuối tỏa hào quang biến hình. |
| b12 | 01:15.7–01:20.9 (5.2s) | L12 | nhau! Đêm nay, tôi mời anh em cùng lật mở từng trang hồ sơ tuyệt mật của gã điệp viên đại tài này! |  | ông trùm điệp báo thế giới ngầm hoạt hình mặc áo măng-tô đen lật mở cuốn hồ sơ bìa da đóng dấu TUYỆT MẬT màu đỏ rực, chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn uốn xúc tu sẵn sàng bước vào nhiệm vụ đầu tiên. |

### scene02 · HÓA THÂN RẮN BIỂN CẠP NONG VÀ CÁ SƯ TỬ GAI ĐỘC · 97.8s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:03.9 (3.9s) | L13 | Lật mở trang hồ sơ đầu tiên: Tuyệt kỹ hóa thân thành sát thủ kịch độc! |  | Bảng hồ sơ hiện DANH TÍNH GIẢ SỐ 1: HÓA THÂN SÁT THỦ KỊCH ĐỘC; ông trùm điệp báo thế giới ngầm hoạt hình mặc áo măng-tô đen chỉ tay vào hình ảnh con rắn biển vằn đen trắng. KHÔNG có chú bạch tuộc đội mũ phớt trong cảnh này. |
| b02 | 00:03.9–00:11.2 (7.3s) | L14 | Hãy quan sát một hiện trường thực tế dưới đáy cát: một đàn cá thia hung hăng phát hiện ra Điệp Viên Đại Dương và bắt đầu bao vây lao tới định tấn công rỉa thịt. |  | Đáy cát biển nhiệt đới: một đàn cá thia hung hăng giương vây bao vây lấy chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn định tấn công rỉa thịt. |
| b03 | 00:11.2–00:15.3 (4.1s) | L15 | Ở một góc ngách không có đường lui, gã điệp viên làm gì? Chạy trốn ư? Không hề! |  | chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn bị dồn vào chân tường cát, mặt vẫn lạnh lùng nhếch mép kéo chiếc kính râm đen, không hề có dấu hiệu sợ hãi. |
| b04 | 00:15.3–00:19.9 (4.6s) | L16 | Gã lập tức thụt sáu chiếc xúc tu và toàn bộ phần thân đầu chui tọt vào trong một chiếc hang cát hẹp! |  | chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn thụt toàn bộ thân đầu và 6 xúc tu chui tọt vào hang cát hẹp biến mất khỏi tầm mắt kẻ thù. |
| b05 | 00:19.9–00:27.5 (7.6s) | L17 | Chỉ chừa lại đúng 2 chiếc xúc tu thò ra ngoài, uốn éo theo hai hướng đối diện nhau. Đồng thời, làn da chuyển đổi sang họa tiết khoang đen trắng xen kẽ nổi | **2 XÚC TU** · giả rắn biển · R/350 · [0.65, 0.5] | Từ miệng hang cát, đúng 2 chiếc xúc tu vằn đen trắng thò ra ngoài uốn éo theo hai hướng đối diện nhau như hai con rắn. |
| b06 | 00:27.5–00:35.6 (8.1s) | L18 | bật... Trong vòng chưa đầy 1 giây, trước mắt đàn cá thia không còn là một con bạch tuộc mềm yếu nữa, mà là một con Rắn Biển Cạp Nong kịch độc đang le lưỡi săn mồi! | **1 GIÂY** · biến hình tức thì · L/350 · [0.35, 0.45] | Hai xúc tu biến hình hoàn hảo thành hai con rắn biển cạp nong vằn đen trắng le lưỡi ngoằn ngoèo khiến đàn cá thia giật bắn mình hoảng loạn. |
| b07 | 00:35.6–00:41.1 (5.5s) | L19 | Cá thia nhìn thấy tử thần rắn biển thì hồn xiêu phách lạc, lập tức quay đầu tháo chạy bạt mạng! |  | Đàn cá thia hồn xiêu phách lạc quay đầu tháo chạy té khói; ông trùm điệp báo thế giới ngầm hoạt hình mặc áo măng-tô đen mỉm cười gật gù khen ngợi chiến thuật. |
| b08 | 00:41.1–00:47.4 (6.3s) | L20 | Điều chấn động giới khoa học được tiến sĩ Norman công bố 2001: Điệp Viên Đại Dương không bắt chước ngẫu nhiên! | **2001** · công bố Norman · L/350 · [0.35, 0.45] | Bài báo khoa học của tiến sĩ Norman năm 2001 trên tạp chí Hoàng Gia Anh: biểu đồ phân tích bạch tuộc bắt chước có chủ đích. KHÔNG có chú bạch tuộc đội mũ phớt trong cảnh này. |
| b09 | 00:47.4–00:55.1 (7.7s) | L21 | Khi bị loài cá nào đe dọa, gã lập tức phân tích và chọn đúng loài thiên địch kịch độc của chính kẻ tấn công đó để hóa trang dọa lại! |  | Sơ đồ radar chiến thuật: chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn quét nhận diện cá thia và chọn đúng thiên địch rắn biển cạp nong để dọa lại. |
| b10 | 00:55.1–00:59.3 (4.2s) | L22 | Và nếu kẻ thù lần này là một con cá nhồng hung dữ bơi lượn ở tầng nước lơ lửng thì sao? |  | Một con cá nhồng hung dữ răng nhọn hoắt bơi lững lờ ở tầng nước giữa lăm le tấn công. |
| b11 | 00:59.3–01:07.4 (8.1s) | L23 | Gã liền kích hoạt danh tính giả số hai: bơi nhấc mình lên khỏi đáy cát, xòe rộng cả tám chiếc xúc tu tỏa ra xung quanh như những chiếc gai nhọn phấp phới, đổi màu da sang vệt nâu sọc trắng! |  | chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn bơi nhấc mình lên khỏi đáy cát, xòe rộng cả 8 chiếc xúc tu tỏa ra xung quanh như những chiếc gai nhọn phấp phới, da đổi vệt nâu sọc trắng. |
| b12 | 01:07.4–01:15.5 (8.0s) | L24 | Bùm! Trước mắt kẻ săn mồi bỗng xuất hiện một chú Cá Sư Tử gai độc đầy gai nhọn chết người! Kẻ địch nhìn thấy gai độc liền ngán ngẩm bỏ đi ngay lập tức! |  | Bùm! Trước mắt cá nhồng xuất hiện một chú Cá Sư Tử gai độc đầy gai nhọn chết người; con cá nhồng toát mồ hôi ngán ngẩm quay đầu bơi đi. |
| b13 | 01:15.5–01:21.7 (6.2s) | L25 | Các thợ lặn chuyên nghiệp từng quay được khoảnh khắc gã điệp viên này đang ung dung bơi thì chạm trán một con cá đuối lớn. |  | Ống kính máy quay của thợ lặn dưới đáy biển: chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn đang bơi thì gặp một con cá đuối lớn từ xa tiến lại gần. |
| b14 | 01:21.7–01:30.2 (8.4s) | L26 | Trong tích tắc không cần suy nghĩ, gã lập tức gập các xúc tu lại, phè thân mình ra phẳng lì và uốn lượn hệt như một con cá đuối gai độc con! Con cá đuối |  | chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn gập các xúc tu ra sau, phè thân mình phẳng lì uốn lượn hệt như một con cá đuối gai độc con lướt sóng cát êm ái. |
| b15 | 01:30.2–01:37.8 (7.6s) | L27 | lớn nhìn thấy tưởng đồng loại đang đi dạo liền bơi lướt qua luôn mà không hề nghi ngờ! Nghệ thuật đánh lừa thị giác đã đạt tới cảnh giới thượng thừa! |  | Con cá đuối lớn bơi lướt qua chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn mà không hề nghi ngờ, tưởng đồng loại đi dạo; bảng Danh tính số 1 bật đèn xanh PASS. |

### scene03 · GIẢ DẠNG CÁ BƠN LƯỚT CÁT VÀ SỨA BIỂN BỒNG BỀNH · 89.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:04.2 (4.2s) | L28 | Chuyển sang trang hồ sơ thứ 2: Tuyệt chiêu tàng hình khi di chuyển đường dài! |  | Bảng hồ sơ chuyển sang DANH TÍNH GIẢ SỐ 2: NGHỆ THUẬT TÀNG HÌNH ĐƯỜNG TRƯỜNG. KHÔNG có chú bạch tuộc đội mũ phớt trong cảnh này. |
| b02 | 00:04.2–00:13.1 (8.9s) | L29 | Trong thế giới ngầm, việc di chuyển băng qua những bãi cát trống trải mênh mông là nhiệm vụ nguy hiểm nhất, vì bóng dáng bạch tuộc bơi lội rất dễ thu hút ánh nhìn của lũ cá mập từ xa. |  | Bãi cát ngầm mênh mông trống trải ban ngày, bóng cá mập bơi lượn trên cao tìm kiếm con mồi. KHÔNG có chú bạch tuộc đội mũ phớt trong cảnh này. |
| b03 | 00:13.1–00:17.8 (4.7s) | L30 | Nhưng Điệp Viên Đại Dương của chúng ta lại có một bộ trang phục ngụy trang đường trường đỉnh cao! |  | chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn khoác bộ trang phục ngụy trang đường trường màu nâu cát, nở nụ cười bí hiểm chuẩn bị lướt sóng. |
| b04 | 00:17.8–00:27.4 (9.7s) | L31 | Gã ép sát toàn bộ thân mình xuống sát mặt cát, chụm cả tám chiếc xúc tu kéo dài ra phía sau thành hình giọt nước dẹt như một chiếc lá cây. Làn da chuyển sang màu nâu cát lốm đốm, |  | chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn ép sát thân xuống mặt cát, chụm cả 8 chiếc xúc tu kéo dài ra phía sau thành hình giọt nước dẹt như một chiếc lá cây, da đổi màu cát lốm đốm. |
| b05 | 00:27.4–00:35.4 (7.9s) | L32 | và dùng chiếc phễu đẩy nước lướt nhẹ nhàng là là trên mặt đáy biển... Trông gã lúc này chẳng khác nào một con Cá Bơn độc đang bơi lướt sóng cát! |  | Chiếc phễu đẩy nước phụt nhẹ đưa chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn lướt là là trên mặt cát giống hệt một con Cá Bơn độc đang bơi lướt sóng cát. |
| b06 | 00:35.4–00:40.5 (5.1s) | L33 | Kẻ săn mồi từ trên cao nhìn xuống chỉ thấy một con cá bơn nhạt nhẽo chán ngấy liền lướt qua luôn! |  | Con cá săn mồi từ trên cao nhìn xuống đáy cát chỉ thấy một con cá bơn nhạt nhẽo chán ngắt liền lướt qua luôn. |
| b07 | 00:40.5–00:48.4 (7.9s) | L34 | Đại ca ơi, thế nếu đang bơi giữa dòng nước mà gặp nguy hiểm không có cát để bám thì anh em tẩu thoát kiểu gì ạ? Yên tâm đi trợ lý! |  | cô đặc vụ tình báo hoạt hình đeo tai nghe bộ đàm cầm sổ ghi chép thắc mắc; ông trùm điệp báo thế giới ngầm hoạt hình mặc áo măng-tô đen bật cười vỗ vai trấn an chuẩn bị hé lộ tuyệt chiêu tầng nước giữa. |
| b08 | 00:48.4–00:55.8 (7.5s) | L35 | Nếu bị đẩy lên tầng nước giữa, gã lập tức cuộn tròn các xúc tu lại, phồng to phần đầu như một chiếc ô dù trong suốt rồi bập bùng co bóp bơi giật lùi... |  | chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn cuộn tròn xúc tu lại, phồng to phần đầu như chiếc ô dù trong suốt rồi bập bùng co bóp bơi giật lùi giữa tầng nước. |
| b09 | 00:55.8–01:01.0 (5.2s) | L36 | Biến hình ngay thành một chú Sứa Biển trôi dạt lững lờ! Kẻ thù thấy sứa đầy nọc châm thì tránh xa 10m! | **NÉ 10 MÉT** · sợ nọc sứa biển · R/350 · [0.65, 0.48] | chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn biến hình hoàn hảo thành một chú Sứa Biển trôi dạt lững lờ, tỏa xúc tu mờ ảo; kẻ thù thấy nọc châm né xa 10m. |
| b10 | 01:01.0–01:10.7 (9.7s) | L37 | Chưa hết, gã còn có thể giả thành cá đuối gai độc, hải quỳ khổng lồ, thậm chí cả tôm tít gập càng! 15 khuôn mặt, 15 danh tính giả hoàn hảo cho mọi tình huống hiểm nghèo! | **15 MẶT NẠ** · danh tính biến hình · L/350 · [0.35, 0.45] | Bộ sưu tập 15 danh tính giả xoay quanh chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn: cá đuối gai, hải quỳ khổng lồ, tôm tít gập búa; bảng Danh tính số 2 bật PASS. |
| b11 | 01:10.7–01:20.3 (9.6s) | L38 | Thậm chí khi cần đi săn những chú cua nhỏ nhút nhát nấp trong hang đá, Điệp Viên Đại Dương còn dùng chiêu hóa trang ngược: biến hình thành một chú cua biển thân thiện giơ hai càng vẫy chào mời gọi bạn ra chơi! |  | chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn dùng chiêu hóa trang ngược: biến hình thành một chú cua biển thân thiện giơ hai càng vẫy chào trước cửa hang đá mời gọi bạn ra chơi. |
| b12 | 01:20.3–01:29.7 (9.4s) | L39 | Con mồi vừa tò mò bước ra khỏi hang liền bị tám chiếc xúc tu thò ra tóm gọn sạch sẽ! Đúng là gã giang hồ vừa đóng vai cảnh sát, vừa đóng vai cướp biển, không ai lường trước được nước đi tiếp theo! |  | Chú cua nhỏ vừa bước ra liền bị 8 chiếc xúc tu thò ra tóm gọn sạch sẽ; chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn nháy mắt kéo kính râm cười đắc ý. |

### scene04 · MẠNG LƯỚI THẦN KINH PHI TẬP TRUNG SIÊU ĐẲNG · 85.8s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:04.4 (4.4s) | L40 | Bước vào trang hồ sơ tối mật thứ 3: Bí mật phần cứng siêu máy tính sinh học! |  | Bảng hồ sơ chuyển sang ĐẾ CHẾ 9 BỘ NÃO: MẠNG LƯỚI THẦN KINH PHI TẬP TRUNG; mô hình siêu máy tính sinh học mở ra. KHÔNG có chú bạch tuộc đội mũ phớt trong cảnh này. |
| b02 | 00:04.4–00:13.1 (8.7s) | L41 | Làm thế nào mà một sinh vật thân mềm không xương lại có thể nhớ và điều khiển trơn tru tới 15 hình thái biến hình phức tạp đến từng chuyển động gợn sóng cơ bắp như vậy? |  | ông trùm điệp báo thế giới ngầm hoạt hình mặc áo măng-tô đen chỉ vào mô hình giải phẫu đặt dấu hỏi lớn: làm sao sinh vật không xương nhớ và điều khiển 15 hình thái phức tạp. |
| b03 | 00:13.1–00:18.9 (5.8s) | L42 | Câu trả lời nằm ở cấu tạo hệ thần kinh kỳ dị bậc nhất hành tinh: Điệp Viên Đại Dương sở hữu tới 9 bộ não độc lập! | **9 BỘ NÃO** · mạng lưới độc lập · R/350 · [0.65, 0.48] | Mặt cắt giải phẫu trong suốt của chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn: một bộ não trung tâm hình bánh vòng quanh thực quản và 8 hạch não lớn dọc suốt 8 chiếc xúc tu phát sáng xanh. |
| b04 | 00:18.9–00:26.2 (7.4s) | L43 | Một bộ não trung tâm hình bánh vòng nằm quanh thực quản ở phần đầu, và tám cụm hạch thần kinh khổng lồ nằm dọc suốt chiều dài của tám chiếc xúc tu! |  | Sơ đồ kết nối: não trung tâm hình bánh vòng ở giữa liên kết cáp thần kinh với 8 cụm não xúc tu rực rỡ. |
| b05 | 00:26.2–00:36.4 (10.2s) | L44 | Trong tổng số hơn 500 triệu tế bào nơ-ron thần kinh của cơ thể — tương đương số lượng nơ-ron của một chú chó thông minh — thì có tới 2/3 số nơ-ron nằm rải rác bên trong tám chiếc xúc tu! | **500 TRIỆU** · nơ-ron như loài chó · L/350 · [0.35, 0.45]<br>**2/3 NƠ-RON** · trong 8 chiếc xúc tu · R/480 · [0.68, 0.55] | Thước đo 500 triệu nơ-ron: 2/3 số nơ-ron nằm bên trong 8 chiếc xúc tu; hình chú chó thông minh đặt cạnh để so sánh trí tuệ tương đương. |
| b06 | 00:36.4–00:43.8 (7.3s) | L45 | Điều này có nghĩa là mỗi xúc tu của gã hoạt động như một thực thể độc lập có ý thức riêng: tự nếm vị giác bằng các giác hút, tự cảm nhận nhiệt độ, |  | Mỗi xúc tu của chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn hoạt động như một thám tử độc lập: giác hút tự nếm vị giác, tự cảm nhận nhiệt độ. |
| b07 | 00:43.8–00:49.4 (5.7s) | L46 | tự quyết định luồn lách vào khe đá săn mồi mà không cần chờ lệnh từ não bộ trung tâm! |  | Các xúc tu tự quyết định luồn lách vào khe đá săn cua mà không cần chờ lệnh từ não bộ trung tâm. |
| b08 | 00:49.4–00:53.7 (4.3s) | L47 | Não trung tâm chỉ đưa ra mệnh lệnh chiến lược tối cao: Giả thành rắn biển! |  | Não trung tâm phát tín hiệu chiến lược tối cao: Giả thành rắn biển! |
| b09 | 00:53.7–01:01.8 (8.1s) | L48 | Ngay lập tức, 2 xúc tu nhận lệnh tự động phối hợp màu sắc và cử động uốn lượn nhịp nhàng, trong khi 6 xúc tu còn lại tự tìm khe cát giấu mình! |  | 2 xúc tu nhận lệnh tự động phối hợp màu sắc uốn lượn thành rắn biển, 6 xúc tu còn lại tự tìm khe cát giấu mình. |
| b10 | 01:01.8–01:07.8 (6.0s) | L49 | Sự phân quyền chỉ huy thần kinh tuyệt đỉnh này giúp gã phản xạ biến hình chỉ trong vòng chưa đầy 0,2 giây! | **0,2 GIÂY** · phản xạ biến hình · L/350 · [0.35, 0.45] | Đồng hồ siêu tốc đếm 0,2 giây: sự phân quyền chỉ huy thần kinh tuyệt đỉnh giúp phản xạ biến hình chỉ trong tích tắc. |
| b11 | 01:07.8–01:14.6 (6.7s) | L50 | Các nhà khoa học thần kinh từng làm thí nghiệm thử thách trí tuệ của loài bạch tuộc: đặt thức ăn bên trong một chiếc lọ thủy tinh có nắp vặn ren kín mít. |  | Thí nghiệm trí tuệ: một chiếc lọ thủy tinh có nắp vặn ren kín mít chứa thức ăn bên trong được đặt trước mặt chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn. |
| b12 | 01:14.6–01:19.5 (5.0s) | L51 | Không cần ai dạy bảo, các xúc tu của gã tự phối hợp vặn mở nắp lọ chỉ trong vài chục giây để lấy thức ăn! |  | chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn dùng các xúc tu tự phối hợp vặn mở nắp ren lọ thủy tinh kín mít lấy thức ăn ngon lành chỉ trong vài chục giây. |
| b13 | 01:19.5–01:25.8 (6.2s) | L52 | Trí thông minh phân tán này đang là nguồn cảm hứng số một cho các kỹ sư chế tạo robot mềm và hệ thống trí tuệ nhân tạo thế hệ mới! |  | Các kỹ sư chế tạo robot mềm và hệ thống trí tuệ nhân tạo thế hệ mới đang nghiên cứu mô hình cánh tay bạch tuộc; bảng Đế Chế 9 Não bật PASS. |

### scene05 · MÁU XANH LAM GỐC ĐỒNG VÀ 3 TẦNG TẾ BÀO ĐỔI MÀU · 98.1s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:04.5 (4.5s) | L53 | Lật sang trang hồ sơ thứ 4: Công nghệ màn hình hiển thị nano trên da và dòng máu |  | Bảng hồ sơ chuyển sang MÀN HÌNH NANO VÀ DÒNG MÁU QUÝ TỘC. KHÔNG có chú bạch tuộc đội mũ phớt trong cảnh này. |
| b02 | 00:04.5–00:11.6 (7.2s) | L54 | quý tộc! Khác với tắc kè hoa đổi màu chậm chạp nhờ hoóc-môn trong máu mất hàng phút, da của Điệp Viên Đại Dương là một chiếc màn hình tinh thể lỏng sinh học độ phân giải siêu nét! |  | So sánh: tắc kè hoa đổi màu chậm chạp nhờ hoóc-môn mất hàng phút; da của chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn là màn hình tinh thể lỏng sinh học đổi màu tức thì. |
| b03 | 00:11.6–00:19.8 (8.2s) | L55 | Làn da của gã chứa ba tầng tế bào đổi màu đặc biệt: tầng trên cùng là hàng triệu túi sắc tố Chromatophores màu nâu, đen, vàng, đỏ được bao quanh bởi các sợi cơ li ti. |  | Kính hiển vi phóng to 3 tầng tế bào da: tầng trên cùng là hàng triệu túi sắc tố Chromatophores màu nâu, đen, vàng, đỏ có sợi cơ bao quanh. |
| b04 | 00:19.8–00:26.0 (6.1s) | L56 | Chỉ cần sợi thần kinh giật nhẹ một xung điện, các sợi cơ lập tức co lại, kéo căng túi sắc tố to ra gấp 10 lần để hiện màu! | **KÉO TO 10X** · đổi màu cơ học · R/350 · [0.65, 0.48] | Xung điện thần kinh giật nhẹ làm sợi cơ co lại, kéo căng túi sắc tố to gấp 10 lần hiện màu rực rỡ chỉ trong 0,2 giây. |
| b05 | 00:26.0–00:31.5 (5.5s) | L57 | Cơ thả lỏng thì túi co lại biến mất! Quá trình đổi màu diễn ra hoàn toàn bằng cơ học thuần túy trong chưa đầy 0,2 giây! |  | Cơ thả lỏng thì túi sắc tố co lại biến mất; quá trình đổi màu diễn ra hoàn toàn bằng cơ học thuần túy trong chưa đầy 0,2 giây. |
| b06 | 00:31.5–00:39.7 (8.2s) | L58 | Phía dưới còn có tầng tế bào khúc xạ ánh sáng và phản chiếu ánh sáng trắng, giúp gã pha trộn mọi dải màu và tạo vân da sần sùi hệt như hạt cát hay rạn san hô! |  | Tầng tế bào phản quang và tán xạ ánh sáng giúp chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn pha trộn mọi màu sắc và tạo vân da sần sùi hệt như rạn san hô đá xung quanh. |
| b07 | 00:39.7–00:45.8 (6.1s) | L59 | Và dòng máu chảy bên trong cơ thể gã điệp viên này cũng mang sắc màu huyền thoại: Máu có màu xanh lam óng ánh! |  | Ống nghiệm chứa mẫu máu của chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn màu xanh lam óng ánh quý tộc, cấu trúc protein Hemocyanin chứa nguyên tử đồng phát sáng. |
| b08 | 00:45.8–00:58.0 (12.3s) | L60 | Vì sống dưới đáy biển sâu lạnh giá nghèo oxy, cơ thể gã không dùng chất sắt hemoglobin màu đỏ như con người, mà sử dụng phân tử protein Hemocyanin chứa nguyên tử đồng để vận chuyển oxy hiệu quả gấp bội trong nước lạnh! |  | Dưới đáy biển lạnh giá nghèo oxy: phân tử Hemocyanin gốc đồng của chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn vận chuyển oxy hiệu quả gấp bội hemoglobin trong nước lạnh. |
| b09 | 00:58.0–01:02.9 (4.8s) | L61 | Để bơm dòng máu xanh lam này đi khắp 9 bộ não và 8 xúc tu, gã trang bị tới 3 quả tim độc lập: | **3 TRÁI TIM** · 2 tim mang 1 tim chính · R/350 · [0.65, 0.48] | Mặt cắt 3 quả tim trong thân chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn: 2 quả tim mang màu xanh đẩy máu nạp oxy, 1 quả tim chính bơm máu đi khắp 9 não và 8 xúc tu. |
| b10 | 01:02.9–01:08.8 (5.9s) | L62 | hai quả tim mang chuyên hút máu đẩy qua hai bên mang để nạp oxy, và một quả tim chính khỏe khoắn bơm máu đi nuôi toàn bộ cơ thể! |  | Sơ đồ tuần hoàn: 2 quả tim mang hút máu đẩy qua mang nạp oxy, 1 quả tim chính khỏe khoắn bơm máu đi nuôi toàn cơ thể. |
| b11 | 01:08.8–01:19.3 (10.5s) | L63 | Nhưng khi gã bơi nước rút với tốc độ cao, quả tim chính sẽ tạm thời ngừng đập để dồn toàn lực cho cơ bắp, khiến gã nhanh kiệt sức và chỉ bơi từng đoạn ngắn rồi lại tàng hình ẩn nấp! Đúng là phong cách điệp viên hành động chớp nhoáng! |  | Khi chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn bơi nước rút với tốc độ cao, quả tim chính tạm dừng đập dồn toàn lực cho cơ bắp; bơi một đoạn ngắn gã liền tàng hình ẩn nấp nghỉ ngơi. |
| b12 | 01:19.3–01:24.2 (5.0s) | L64 | Không chỉ đổi màu sắc, làn da của gã còn có thể thay đổi kết cấu vật lý 3D trong nháy mắt! |  | chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn co thắt cơ dưới da làm nổi lên những chiếc gai nhọn 3D sần sùi như rạn san hô đá. |
| b13 | 01:24.2–01:32.5 (8.3s) | L65 | Bằng cách co thắt các bó cơ biểu bì dưới da, gã có thể làm nổi lên những chiếc gai nhọn sần sùi như rạn san hô đá, hoặc làm phẳng lì trơn láng như hạt cát mịn. |  | chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn co thắt các bó cơ biểu bì dưới da làm nổi lên những chiếc gai nhọn 3D sần sùi hoặc làm phẳng lì trơn láng. |
| b14 | 01:32.5–01:38.1 (5.6s) | L66 | Mắt người nhìn vào không tài nào phân biệt nổi đâu là rạn đá tự nhiên và đâu là gã điệp viên đang nằm rình mồi! |  | Mặt cát mịn màng trơn láng: mắt người thường nhìn vào không thể phân biệt nổi đâu là rạn đá tự nhiên và đâu là gã điệp viên đang nằm rình mồi; bảng Màn Hình Nano bật PASS. |

### scene06 · TRÍ TUỆ MỀM VÀ BÓNG ĐEN MÔNG BỌC THÉP KỲ SAU · 77.2s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.6 (8.6s) | L67 | Tổng kết hồ sơ điệp báo số 25. Giữa đại dương khắc nghiệt nơi mọi sinh vật đều chạy đua trang bị giáp dày gai nhọn, Điệp Viên Đại Dương đã chọn một con đường tiến hóa phi |  | ông trùm điệp báo thế giới ngầm hoạt hình mặc áo măng-tô đen đứng bên bàn tổng kết hồ sơ điệp báo số 25: giữa đại dương nơi các loài chạy đua mang giáp dày gai nhọn, chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn bơi ngạo nghễ với trí t |
| b02 | 00:08.6–00:17.4 (8.7s) | L68 | thường: lấy sự mềm mại linh hoạt làm vũ khí, lấy trí thông minh của 9 bộ não làm khiên chắn, và dùng 15 danh tính giả để làm chủ hoàn toàn thế giới ngầm đáy cát! |  | 15 danh tính giả xoay quanh chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn: sự mềm mại làm vũ khí, trí thông minh làm khiên chắn làm chủ thế giới ngầm đáy cát. |
| b03 | 00:17.4–00:22.7 (5.3s) | L69 | Một sinh vật không hề có xương sống, nhưng lại sở hữu trí tuệ khiến con người phải kinh ngạc và tôn trọng sâu |  | ông trùm điệp báo thế giới ngầm hoạt hình mặc áo măng-tô đen đóng dấu ĐÃ DUYỆT màu đỏ lên tập hồ sơ, trao lại cho chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn đang bơi lượn vẫy chào tạm biệt căn cứ tình báo. |
| b04 | 00:22.7–00:32.7 (10.0s) | L70 | sắc! Đơn báo cáo cuối cùng: Cho phép điệp viên tiếp tục hoạt động ngầm tại vùng biển Indonesia và tuyệt đối bảo mật danh tính! Ký tên: trùm điệp báo thế giới ngầm! |  | Bản báo cáo đóng dấu TUYỆT MẬT cho phép siêu điệp viên tiếp tục hoạt động ngầm tại vùng biển Indonesia. |
| b05 | 00:32.7–00:47.0 (14.3s) | L71 | Còn anh em thì sao? Nếu được sở hữu một trong hai năng lực của Điệp Viên Đại Dương: có 9 bộ não để làm nhiều việc cùng lúc không lo quá tải, hay tài hóa trang biến hình thành người khác chỉ trong 0,2 giây, anh em chọn cái nào? Hãy để lại bình luận bên dưới nhé! |  | Hai bàn cân lựa chọn: BÊN TRÁI biểu tượng 9 bộ não thông thái; BÊN PHẢI biểu tượng tài hóa trang biến hình 0,2 giây, các thám tử nhỏ hào hứng giơ thẻ bình chọn. |
| b06 | 00:47.0–00:56.2 (9.2s) | L72 | Hồ sơ điệp viên số 25 xin được niêm phong tại đây. Nhưng tập sau, chúng ta sẽ chuyển thẳng sang hồ sơ vũ khí tối mật trên đất liền để giải mã một chiến binh xe bọc thép lùn tịt cực kỳ lầy |  | ông trùm điệp báo thế giới ngầm hoạt hình mặc áo măng-tô đen khóa chặt tủ sắt hồ sơ số 25, trên bàn mở ra bản đồ nước Úc với chiếc xe bọc thép đào hang bí ẩn. KHÔNG có chú bạch tuộc đội mũ phớt trong cảnh này. |
| b07 | 00:56.2–01:05.3 (9.1s) | L73 | lội! Một sinh vật mũm mĩm đào hang ở nước Úc, nhưng sở hữu chiếc mông bọc thép dày cứng như bê tông cốt thép, chuyên lừa kẻ thù đuổi vào hang rồi gồng mông dập nát hộp sọ đối thủ vào trần hang |  | Một sinh vật bí ẩn được vẽ hoàn toàn bằng BÓNG ĐEN ĐẶC TUYỀN (solid black silhouette) hình thú có túi mập mạp đang đào hang ở nước Úc, phần mông phát sáng cứng như thép tấm; có dấu hỏi chấm vàng lớn; KHÔNG vẽ rõ mắt mũi lông. KHÔNG có chú bạch tuộc đội mũ phớt trong cảnh này. |
| b08 | 01:05.3–01:17.2 (11.8s) | L74 | đá! Chưa hết, nó là sinh vật duy nhất trên thế giới có dây chuyền cơ học thải ra những viên phân hình khối lập phương vuông vức như viên xúc xắc! Đố các bạn biết bóng đen bí ẩn kỳ sau là loài vật nào? Hãy đoán ngay ở phần bình luận nhé! |  | Cũng chiếc BÓNG ĐEN ĐẶC TUYỀN (solid black silhouette) mập mạp đó thải ra những viên phân hình khối lập phương vuông vức như viên xúc xắc; ba dấu hỏi chấm lớn lấp lánh vàng cam mời gọi khán giả đoán tên. KHÔNG có chú bạch tuộc đội mũ phớt trong cảnh này. |

## 5. Phân cảnh Shorts — từng beat

Banner: **9 BỘ NÃO VÀ 15 / KHUÔN MẶT BIẾN HÌNH?!** · giọng 50.0s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Khi bị kẻ thù bao vây, con vật này không chạy trốn, |  |
| s02 | 00:03.3 | S02 | mà lập tức biến 2 chiếc xúc tu của mình thành một con rắn biển kịch độc le lưỡi dọa lại kẻ đi săn! |  |
| s03 | 00:09.0 | S03 | Xin giới thiệu Bạch Tuộc Mimic, siêu điệp viên sải tay 60cm sống dưới đáy cát ở Indonesia. | **60 CM** · sải tay bãi cát · R/620 · [0.62, 0.5] |
| s04 | 00:15.1 | S04 | Nó sở hữu tới 9 bộ não độc lập, 3 trái tim bơm dòng máu màu xanh lam óng ánh, | **9 BỘ NÃO** · 3 tim máu xanh · L/620 · [0.4, 0.52] |
| s05 | 00:19.2 | S05 | và tài năng hóa trang vô tiền khoáng hậu: có thể biến hình mượt mà thành 15 loài sinh vật kịch độc khác nhau! |  |
| s06 | 00:25.3 | S06 | Bị cá thia tấn công? Thụt thân vào hang, biến 2 xúc tu thành rắn biển cạp nong! |  |
| s07 | 00:29.6 | S07 | Gặp cá nhồng hung dữ? Xòe 8 xúc tu bơi lơ lửng thành cá sư tử đầy gai độc! |  |
| s08 | 00:34.4 | S08 | Cần di chuyển qua bãi cát trống? Ép dẹt toàn thân thành chiếc lá lướt sóng giả dạng cá bơn độc! |  |
| s09 | 00:40.2 | S09 | Làn da của nó chứa hàng triệu túi sắc tố đổi màu cơ học chỉ trong 0,2 giây! | **0,2 GIÂY** · đổi màu cơ học · R/680 · [0.6, 0.5] |
| s10 | 00:44.8 | S10 | Một bậc thầy tình báo thế giới ngầm không cần nanh vuốt vẫn khiến cả đại dương phải ngả mũ kính sợ! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong thế giới ngầm của đại dương bao la, có những luật lệ sinh tồn khắc nghiệt... không bao giờ được viết thành văn.". Bố cục: Đáy đại dương sâu thẳm trong bóng tối huyền bí: những vệt sáng lờ mờ chiếu qua rạn san hô đen, không khí thế giới ngầm căng thẳng. KHÔNG có chú bạch tuộc đội mũ phớt trong cảnh này.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kẻ yếu thì phải biết ẩn mình trong bóng tối, kẻ mạnh thì phô trương nanh vuốt săn lùng. Nhưng gia đình này thì chọn một con đường hoàn toàn khác:". Bố cục: Chia đôi: BÊN TRÁI những chú cá nhỏ nhút nhát trốn sâu trong hốc đá tối; BÊN PHẢI con cá mập hổ dữ tợn giơ nanh vuốt săn lùng. KHÔNG có chú bạch tuộc đội mũ phớt trong cảnh này.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "không có vỏ bọc cứng, không có nanh vuốt nhọn, không có độc tố chết người, nhưng bất kỳ ai trong thế giới ngầm cũng phải ngả mũ kính sợ!". Bố cục: chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn bơi lững lờ giữa làn nước sâu, khoanh tay ngạo nghễ, không vỏ cứng không gai nhọn nhưng toát lên thần thái của một đại ca thế giới ngầm.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chào đại ca, hôm nay có mục tiêu nào cần đội tình báo chúng em đi điều tra không ạ?". Bố cục: cô đặc vụ tình báo hoạt hình đeo tai nghe bộ đàm đeo tai nghe bộ đàm giơ chiếc cặp tài liệu tuyệt mật màu đen cúi đầu chào chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn đang ngồi trên bục chỉ huy san hô.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bật màn hình máy quét bảo mật lên, hôm nay chúng ta giải mã hồ sơ của một siêu điệp viên thực thụ! Xin giới thiệu với toàn thể anh em: đây là Bạch Tuộc Mimic, tên khoa học là Thaumoctopus mimicus.". Bố cục: ông trùm điệp báo thế giới ngầm hoạt hình mặc áo măng-tô đen mở màn hình máy quét bảo mật công nghệ cao, hiển thị bản đồ hồ sơ điệp viên Thaumoctopus mimicus phát sáng xanh lam. KHÔNG có chú bạch tuộc đội mũ phớt trong cảnh này.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Loài sinh vật bí ẩn này chỉ mới được các thợ lặn phát hiện lần đầu tiên vào 1998 ngoài khơi đảo Sulawesi thuộc Indonesia.". Bố cục: Bản đồ Indonesia phóng to vùng biển Sulawesi và Bali năm 1998; các thợ lặn chuyên nghiệp cầm đèn pin ngỡ ngàng phát hiện chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chiều dài sải tay khi bung rộng khoảng 60cm.". Bố cục: Ở GIỮA chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn bung rộng tám chiếc xúc tu vằn nâu trắng cạnh chiếc thước đo chiều cao 60cm màu vàng của cơ quan tình báo.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhìn bề ngoài nó giống hệt những chú bạch tuộc thân mềm thông thường, nhưng trong thế giới ngầm đại dương, chúng tôi gọi thẳng tên nó bằng biệt danh: Điệp Viên Đại Dương!". Bố cục: chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn tạo dáng điệp viên đeo kính râm đen giơ huy hiệu tình báo Điệp Viên Đại Dương lấp lánh màu vàng quyền lực.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Điều khiến mọi cơ quan tình báo biển sâu phải kinh ngạc là gã không chọn cách lẩn trốn trong hang hốc tối tăm như các loài bạch tuộc khác!". Bố cục: Bản đồ vệ tinh các hang hốc ngầm tối tăm nơi các loài bạch tuộc bình thường lẩn trốn trong bóng đêm. KHÔNG có chú bạch tuộc đội mũ phớt trong cảnh này.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Điệp Viên Đại Dương chọn lộ diện ban ngày ngay giữa những bãi cát ngầm trống trải, nơi đầy rẫy những con cá săn mồi đói khát lượn lờ.". Bố cục: chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn ngạo nghễ lướt đi giữa bãi cát ngầm trống trải ban ngày đầy nắng, xung quanh có bóng cá săn mồi lượn lờ từ xa.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và vũ khí sinh tồn tối thượng của gã chính là tài năng hóa trang vô tiền khoáng hậu: có thể biến hình mượt mà thành 15 loài sinh vật kịch độc khác nhau!". Bố cục: Vòng tròn 15 chiếc mặt nạ danh tính kịch độc xoay quanh chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn: rắn biển, cá sư tử, cá bơn, sứa biển, cá đuối tỏa hào quang biến hình.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đêm nay, tôi mời anh em cùng lật mở từng trang hồ sơ tuyệt mật của gã điệp viên đại tài này!". Bố cục: ông trùm điệp báo thế giới ngầm hoạt hình mặc áo măng-tô đen lật mở cuốn hồ sơ bìa da đóng dấu TUYỆT MẬT màu đỏ rực, chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn uốn xúc tu sẵn sàng bước vào nhiệm vụ đầu tiên.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lật mở trang hồ sơ đầu tiên: Tuyệt kỹ hóa thân thành sát thủ kịch độc!". Bố cục: Bảng hồ sơ hiện DANH TÍNH GIẢ SỐ 1: HÓA THÂN SÁT THỦ KỊCH ĐỘC; ông trùm điệp báo thế giới ngầm hoạt hình mặc áo măng-tô đen chỉ tay vào hình ảnh con rắn biển vằn đen trắng. KHÔNG có chú bạch tuộc đội mũ phớt trong cảnh này.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy quan sát một hiện trường thực tế dưới đáy cát: một đàn cá thia hung hăng phát hiện ra Điệp Viên Đại Dương và bắt đầu bao vây lao tới định tấn công rỉa thịt.". Bố cục: Đáy cát biển nhiệt đới: một đàn cá thia hung hăng giương vây bao vây lấy chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn định tấn công rỉa thịt.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ở một góc ngách không có đường lui, gã điệp viên làm gì? Chạy trốn ư? Không hề!". Bố cục: chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn bị dồn vào chân tường cát, mặt vẫn lạnh lùng nhếch mép kéo chiếc kính râm đen, không hề có dấu hiệu sợ hãi.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gã lập tức thụt sáu chiếc xúc tu và toàn bộ phần thân đầu chui tọt vào trong một chiếc hang cát hẹp!". Bố cục: chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn thụt toàn bộ thân đầu và 6 xúc tu chui tọt vào hang cát hẹp biến mất khỏi tầm mắt kẻ thù.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chỉ chừa lại đúng 2 chiếc xúc tu thò ra ngoài, uốn éo theo hai hướng đối diện nhau. Đồng thời, làn da chuyển đổi sang họa tiết khoang đen trắng xen kẽ nổi bật...". Bố cục: Từ miệng hang cát, đúng 2 chiếc xúc tu vằn đen trắng thò ra ngoài uốn éo theo hai hướng đối diện nhau như hai con rắn.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong vòng chưa đầy 1 giây, trước mắt đàn cá thia không còn là một con bạch tuộc mềm yếu nữa, mà là một con Rắn Biển Cạp Nong kịch độc đang le lưỡi săn mồi!". Bố cục: Hai xúc tu biến hình hoàn hảo thành hai con rắn biển cạp nong vằn đen trắng le lưỡi ngoằn ngoèo khiến đàn cá thia giật bắn mình hoảng loạn.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cá thia nhìn thấy tử thần rắn biển thì hồn xiêu phách lạc, lập tức quay đầu tháo chạy bạt mạng!". Bố cục: Đàn cá thia hồn xiêu phách lạc quay đầu tháo chạy té khói; ông trùm điệp báo thế giới ngầm hoạt hình mặc áo măng-tô đen mỉm cười gật gù khen ngợi chiến thuật.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Điều chấn động giới khoa học được tiến sĩ Norman công bố 2001: Điệp Viên Đại Dương không bắt chước ngẫu nhiên!". Bố cục: Bài báo khoa học của tiến sĩ Norman năm 2001 trên tạp chí Hoàng Gia Anh: biểu đồ phân tích bạch tuộc bắt chước có chủ đích. KHÔNG có chú bạch tuộc đội mũ phớt trong cảnh này.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi bị loài cá nào đe dọa, gã lập tức phân tích và chọn đúng loài thiên địch kịch độc của chính kẻ tấn công đó để hóa trang dọa lại!". Bố cục: Sơ đồ radar chiến thuật: chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn quét nhận diện cá thia và chọn đúng thiên địch rắn biển cạp nong để dọa lại.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và nếu kẻ thù lần này là một con cá nhồng hung dữ bơi lượn ở tầng nước lơ lửng thì sao?". Bố cục: Một con cá nhồng hung dữ răng nhọn hoắt bơi lững lờ ở tầng nước giữa lăm le tấn công.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gã liền kích hoạt danh tính giả số hai: bơi nhấc mình lên khỏi đáy cát, xòe rộng cả tám chiếc xúc tu tỏa ra xung quanh như những chiếc gai nhọn phấp phới, đổi màu da sang vệt nâu sọc trắng!". Bố cục: chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn bơi nhấc mình lên khỏi đáy cát, xòe rộng cả 8 chiếc xúc tu tỏa ra xung quanh như những chiếc gai nhọn phấp phới, da đổi vệt nâu sọc trắng.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bùm! Trước mắt kẻ săn mồi bỗng xuất hiện một chú Cá Sư Tử gai độc đầy gai nhọn chết người! Kẻ địch nhìn thấy gai độc liền ngán ngẩm bỏ đi ngay lập tức!". Bố cục: Bùm! Trước mắt cá nhồng xuất hiện một chú Cá Sư Tử gai độc đầy gai nhọn chết người; con cá nhồng toát mồ hôi ngán ngẩm quay đầu bơi đi.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các thợ lặn chuyên nghiệp từng quay được khoảnh khắc gã điệp viên này đang ung dung bơi thì chạm trán một con cá đuối lớn.". Bố cục: Ống kính máy quay của thợ lặn dưới đáy biển: chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn đang bơi thì gặp một con cá đuối lớn từ xa tiến lại gần.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong tích tắc không cần suy nghĩ, gã lập tức gập các xúc tu lại, phè thân mình ra phẳng lì và uốn lượn hệt như một con cá đuối gai độc con! Con cá đuối lớn". Bố cục: chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn gập các xúc tu ra sau, phè thân mình phẳng lì uốn lượn hệt như một con cá đuối gai độc con lướt sóng cát êm ái.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nhìn thấy tưởng đồng loại đang đi dạo liền bơi lướt qua luôn mà không hề nghi ngờ! Nghệ thuật đánh lừa thị giác đã đạt tới cảnh giới thượng thừa!". Bố cục: Con cá đuối lớn bơi lướt qua chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn mà không hề nghi ngờ, tưởng đồng loại đi dạo; bảng Danh tính số 1 bật đèn xanh PASS.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chuyển sang trang hồ sơ thứ 2: Tuyệt chiêu tàng hình khi di chuyển đường dài!". Bố cục: Bảng hồ sơ chuyển sang DANH TÍNH GIẢ SỐ 2: NGHỆ THUẬT TÀNG HÌNH ĐƯỜNG TRƯỜNG. KHÔNG có chú bạch tuộc đội mũ phớt trong cảnh này.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong thế giới ngầm, việc di chuyển băng qua những bãi cát trống trải mênh mông là nhiệm vụ nguy hiểm nhất, vì bóng dáng bạch tuộc bơi lội rất dễ thu hút ánh nhìn của lũ cá mập từ xa.". Bố cục: Bãi cát ngầm mênh mông trống trải ban ngày, bóng cá mập bơi lượn trên cao tìm kiếm con mồi. KHÔNG có chú bạch tuộc đội mũ phớt trong cảnh này.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng Điệp Viên Đại Dương của chúng ta lại có một bộ trang phục ngụy trang đường trường đỉnh cao!". Bố cục: chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn khoác bộ trang phục ngụy trang đường trường màu nâu cát, nở nụ cười bí hiểm chuẩn bị lướt sóng.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Gã ép sát toàn bộ thân mình xuống sát mặt cát, chụm cả tám chiếc xúc tu kéo dài ra phía sau thành hình giọt nước dẹt như một chiếc lá cây. Làn da chuyển sang màu nâu cát lốm đốm,". Bố cục: chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn ép sát thân xuống mặt cát, chụm cả 8 chiếc xúc tu kéo dài ra phía sau thành hình giọt nước dẹt như một chiếc lá cây, da đổi màu cát lốm đốm.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "và dùng chiếc phễu đẩy nước lướt nhẹ nhàng là là trên mặt đáy biển... Trông gã lúc này chẳng khác nào một con Cá Bơn độc đang bơi lướt sóng cát!". Bố cục: Chiếc phễu đẩy nước phụt nhẹ đưa chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn lướt là là trên mặt cát giống hệt một con Cá Bơn độc đang bơi lướt sóng cát.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kẻ săn mồi từ trên cao nhìn xuống chỉ thấy một con cá bơn nhạt nhẽo chán ngấy liền lướt qua luôn!". Bố cục: Con cá săn mồi từ trên cao nhìn xuống đáy cát chỉ thấy một con cá bơn nhạt nhẽo chán ngắt liền lướt qua luôn.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đại ca ơi, thế nếu đang bơi giữa dòng nước mà gặp nguy hiểm không có cát để bám thì anh em tẩu thoát kiểu gì ạ? Yên tâm đi trợ lý!". Bố cục: cô đặc vụ tình báo hoạt hình đeo tai nghe bộ đàm cầm sổ ghi chép thắc mắc; ông trùm điệp báo thế giới ngầm hoạt hình mặc áo măng-tô đen bật cười vỗ vai trấn an chuẩn bị hé lộ tuyệt chiêu tầng nước giữa.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu bị đẩy lên tầng nước giữa, gã lập tức cuộn tròn các xúc tu lại, phồng to phần đầu như một chiếc ô dù trong suốt rồi bập bùng co bóp bơi giật lùi...". Bố cục: chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn cuộn tròn xúc tu lại, phồng to phần đầu như chiếc ô dù trong suốt rồi bập bùng co bóp bơi giật lùi giữa tầng nước.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Biến hình ngay thành một chú Sứa Biển trôi dạt lững lờ! Kẻ thù thấy sứa đầy nọc châm thì tránh xa 10m!". Bố cục: chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn biến hình hoàn hảo thành một chú Sứa Biển trôi dạt lững lờ, tỏa xúc tu mờ ảo; kẻ thù thấy nọc châm né xa 10m.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa hết, gã còn có thể giả thành cá đuối gai độc, hải quỳ khổng lồ, thậm chí cả tôm tít gập càng! 15 khuôn mặt, 15 danh tính giả hoàn hảo cho mọi tình huống hiểm nghèo!". Bố cục: Bộ sưu tập 15 danh tính giả xoay quanh chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn: cá đuối gai, hải quỳ khổng lồ, tôm tít gập búa; bảng Danh tính số 2 bật PASS.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thậm chí khi cần đi săn những chú cua nhỏ nhút nhát nấp trong hang đá, Điệp Viên Đại Dương còn dùng chiêu hóa trang ngược: biến hình thành một chú cua biển thân thiện giơ hai càng vẫy chào mời gọi bạn ra chơi!". Bố cục: chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn dùng chiêu hóa trang ngược: biến hình thành một chú cua biển thân thiện giơ hai càng vẫy chào trước cửa hang đá mời gọi bạn ra chơi.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Con mồi vừa tò mò bước ra khỏi hang liền bị tám chiếc xúc tu thò ra tóm gọn sạch sẽ! Đúng là gã giang hồ vừa đóng vai cảnh sát, vừa đóng vai cướp biển, không ai lường trước được nước đi tiếp theo!". Bố cục: Chú cua nhỏ vừa bước ra liền bị 8 chiếc xúc tu thò ra tóm gọn sạch sẽ; chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn nháy mắt kéo kính râm cười đắc ý.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bước vào trang hồ sơ tối mật thứ 3: Bí mật phần cứng siêu máy tính sinh học!". Bố cục: Bảng hồ sơ chuyển sang ĐẾ CHẾ 9 BỘ NÃO: MẠNG LƯỚI THẦN KINH PHI TẬP TRUNG; mô hình siêu máy tính sinh học mở ra. KHÔNG có chú bạch tuộc đội mũ phớt trong cảnh này.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Làm thế nào mà một sinh vật thân mềm không xương lại có thể nhớ và điều khiển trơn tru tới 15 hình thái biến hình phức tạp đến từng chuyển động gợn sóng cơ bắp như vậy?". Bố cục: ông trùm điệp báo thế giới ngầm hoạt hình mặc áo măng-tô đen chỉ vào mô hình giải phẫu đặt dấu hỏi lớn: làm sao sinh vật không xương nhớ và điều khiển 15 hình thái phức tạp.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Câu trả lời nằm ở cấu tạo hệ thần kinh kỳ dị bậc nhất hành tinh: Điệp Viên Đại Dương sở hữu tới 9 bộ não độc lập!". Bố cục: Mặt cắt giải phẫu trong suốt của chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn: một bộ não trung tâm hình bánh vòng quanh thực quản và 8 hạch não lớn dọc suốt 8 chiếc xúc tu phát sáng xanh.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một bộ não trung tâm hình bánh vòng nằm quanh thực quản ở phần đầu, và tám cụm hạch thần kinh khổng lồ nằm dọc suốt chiều dài của tám chiếc xúc tu!". Bố cục: Sơ đồ kết nối: não trung tâm hình bánh vòng ở giữa liên kết cáp thần kinh với 8 cụm não xúc tu rực rỡ.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong tổng số hơn 500 triệu tế bào nơ-ron thần kinh của cơ thể — tương đương số lượng nơ-ron của một chú chó thông minh — thì có tới 2/3 số nơ-ron nằm rải rác bên trong tám chiếc xúc tu!". Bố cục: Thước đo 500 triệu nơ-ron: 2/3 số nơ-ron nằm bên trong 8 chiếc xúc tu; hình chú chó thông minh đặt cạnh để so sánh trí tuệ tương đương.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Điều này có nghĩa là mỗi xúc tu của gã hoạt động như một thực thể độc lập có ý thức riêng: tự nếm vị giác bằng các giác hút, tự cảm nhận nhiệt độ,". Bố cục: Mỗi xúc tu của chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn hoạt động như một thám tử độc lập: giác hút tự nếm vị giác, tự cảm nhận nhiệt độ.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tự quyết định luồn lách vào khe đá săn mồi mà không cần chờ lệnh từ não bộ trung tâm!". Bố cục: Các xúc tu tự quyết định luồn lách vào khe đá săn cua mà không cần chờ lệnh từ não bộ trung tâm.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Não trung tâm chỉ đưa ra mệnh lệnh chiến lược tối cao: Giả thành rắn biển!". Bố cục: Não trung tâm phát tín hiệu chiến lược tối cao: Giả thành rắn biển!
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ngay lập tức, 2 xúc tu nhận lệnh tự động phối hợp màu sắc và cử động uốn lượn nhịp nhàng, trong khi 6 xúc tu còn lại tự tìm khe cát giấu mình!". Bố cục: 2 xúc tu nhận lệnh tự động phối hợp màu sắc uốn lượn thành rắn biển, 6 xúc tu còn lại tự tìm khe cát giấu mình.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sự phân quyền chỉ huy thần kinh tuyệt đỉnh này giúp gã phản xạ biến hình chỉ trong vòng chưa đầy 0,2 giây!". Bố cục: Đồng hồ siêu tốc đếm 0,2 giây: sự phân quyền chỉ huy thần kinh tuyệt đỉnh giúp phản xạ biến hình chỉ trong tích tắc.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà khoa học thần kinh từng làm thí nghiệm thử thách trí tuệ của loài bạch tuộc: đặt thức ăn bên trong một chiếc lọ thủy tinh có nắp vặn ren kín mít.". Bố cục: Thí nghiệm trí tuệ: một chiếc lọ thủy tinh có nắp vặn ren kín mít chứa thức ăn bên trong được đặt trước mặt chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không cần ai dạy bảo, các xúc tu của gã tự phối hợp vặn mở nắp lọ chỉ trong vài chục giây để lấy thức ăn!". Bố cục: chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn dùng các xúc tu tự phối hợp vặn mở nắp ren lọ thủy tinh kín mít lấy thức ăn ngon lành chỉ trong vài chục giây.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trí thông minh phân tán này đang là nguồn cảm hứng số một cho các kỹ sư chế tạo robot mềm và hệ thống trí tuệ nhân tạo thế hệ mới!". Bố cục: Các kỹ sư chế tạo robot mềm và hệ thống trí tuệ nhân tạo thế hệ mới đang nghiên cứu mô hình cánh tay bạch tuộc; bảng Đế Chế 9 Não bật PASS.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lật sang trang hồ sơ thứ 4: Công nghệ màn hình hiển thị nano trên da và dòng máu quý tộc!". Bố cục: Bảng hồ sơ chuyển sang MÀN HÌNH NANO VÀ DÒNG MÁU QUÝ TỘC. KHÔNG có chú bạch tuộc đội mũ phớt trong cảnh này.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khác với tắc kè hoa đổi màu chậm chạp nhờ hoóc-môn trong máu mất hàng phút, da của Điệp Viên Đại Dương là một chiếc màn hình tinh thể lỏng sinh học độ phân giải siêu nét!". Bố cục: So sánh: tắc kè hoa đổi màu chậm chạp nhờ hoóc-môn mất hàng phút; da của chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn là màn hình tinh thể lỏng sinh học đổi màu tức thì.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Làn da của gã chứa ba tầng tế bào đổi màu đặc biệt: tầng trên cùng là hàng triệu túi sắc tố Chromatophores màu nâu, đen, vàng, đỏ được bao quanh bởi các sợi cơ li ti.". Bố cục: Kính hiển vi phóng to 3 tầng tế bào da: tầng trên cùng là hàng triệu túi sắc tố Chromatophores màu nâu, đen, vàng, đỏ có sợi cơ bao quanh.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chỉ cần sợi thần kinh giật nhẹ một xung điện, các sợi cơ lập tức co lại, kéo căng túi sắc tố to ra gấp 10 lần để hiện màu!". Bố cục: Xung điện thần kinh giật nhẹ làm sợi cơ co lại, kéo căng túi sắc tố to gấp 10 lần hiện màu rực rỡ chỉ trong 0,2 giây.
```
</details>

<details><summary>L57</summary>

```text
HÌNH L57 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cơ thả lỏng thì túi co lại biến mất! Quá trình đổi màu diễn ra hoàn toàn bằng cơ học thuần túy trong chưa đầy 0,2 giây!". Bố cục: Cơ thả lỏng thì túi sắc tố co lại biến mất; quá trình đổi màu diễn ra hoàn toàn bằng cơ học thuần túy trong chưa đầy 0,2 giây.
```
</details>

<details><summary>L58</summary>

```text
HÌNH L58 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Phía dưới còn có tầng tế bào khúc xạ ánh sáng và phản chiếu ánh sáng trắng, giúp gã pha trộn mọi dải màu và tạo vân da sần sùi hệt như hạt cát hay rạn san hô!". Bố cục: Tầng tế bào phản quang và tán xạ ánh sáng giúp chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn pha trộn mọi màu sắc và tạo vân da sần sùi hệt như rạn san hô đá xung quanh.
```
</details>

<details><summary>L59</summary>

```text
HÌNH L59 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và dòng máu chảy bên trong cơ thể gã điệp viên này cũng mang sắc màu huyền thoại: Máu có màu xanh lam óng ánh!". Bố cục: Ống nghiệm chứa mẫu máu của chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn màu xanh lam óng ánh quý tộc, cấu trúc protein Hemocyanin chứa nguyên tử đồng phát sáng.
```
</details>

<details><summary>L60</summary>

```text
HÌNH L60 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vì sống dưới đáy biển sâu lạnh giá nghèo oxy, cơ thể gã không dùng chất sắt hemoglobin màu đỏ như con người, mà sử dụng phân tử protein Hemocyanin chứa nguyên tử đồng để vận chuyển oxy hiệu quả gấp bội trong nước lạnh!". Bố cục: Dưới đáy biển lạnh giá nghèo oxy: phân tử Hemocyanin gốc đồng của chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn vận chuyển oxy hiệu quả gấp bội hemoglobin trong nước lạnh.
```
</details>

<details><summary>L61</summary>

```text
HÌNH L61 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Để bơm dòng máu xanh lam này đi khắp 9 bộ não và 8 xúc tu, gã trang bị tới 3 quả tim độc lập:". Bố cục: Mặt cắt 3 quả tim trong thân chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn: 2 quả tim mang màu xanh đẩy máu nạp oxy, 1 quả tim chính bơm máu đi khắp 9 não và 8 xúc tu.
```
</details>

<details><summary>L62</summary>

```text
HÌNH L62 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "hai quả tim mang chuyên hút máu đẩy qua hai bên mang để nạp oxy, và một quả tim chính khỏe khoắn bơm máu đi nuôi toàn bộ cơ thể!". Bố cục: Sơ đồ tuần hoàn: 2 quả tim mang hút máu đẩy qua mang nạp oxy, 1 quả tim chính khỏe khoắn bơm máu đi nuôi toàn cơ thể.
```
</details>

<details><summary>L63</summary>

```text
HÌNH L63 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng khi gã bơi nước rút với tốc độ cao, quả tim chính sẽ tạm thời ngừng đập để dồn toàn lực cho cơ bắp, khiến gã nhanh kiệt sức và chỉ bơi từng đoạn ngắn rồi lại tàng hình ẩn nấp! Đúng là phong cách điệp viên hành động chớp nhoáng!". Bố cục: Khi chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn bơi nước rút với tốc độ cao, quả tim chính tạm dừng đập dồn toàn lực cho cơ bắp; bơi một đoạn ngắn gã liền tàng hình ẩn nấp nghỉ ngơi.
```
</details>

<details><summary>L64</summary>

```text
HÌNH L64 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không chỉ đổi màu sắc, làn da của gã còn có thể thay đổi kết cấu vật lý 3D trong nháy mắt!". Bố cục: chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn co thắt cơ dưới da làm nổi lên những chiếc gai nhọn 3D sần sùi như rạn san hô đá.
```
</details>

<details><summary>L65</summary>

```text
HÌNH L65 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bằng cách co thắt các bó cơ biểu bì dưới da, gã có thể làm nổi lên những chiếc gai nhọn sần sùi như rạn san hô đá, hoặc làm phẳng lì trơn láng như hạt cát mịn.". Bố cục: chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn co thắt các bó cơ biểu bì dưới da làm nổi lên những chiếc gai nhọn 3D sần sùi hoặc làm phẳng lì trơn láng.
```
</details>

<details><summary>L66</summary>

```text
HÌNH L66 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mắt người nhìn vào không tài nào phân biệt nổi đâu là rạn đá tự nhiên và đâu là gã điệp viên đang nằm rình mồi!". Bố cục: Mặt cát mịn màng trơn láng: mắt người thường nhìn vào không thể phân biệt nổi đâu là rạn đá tự nhiên và đâu là gã điệp viên đang nằm rình mồi; bảng Màn Hình Nano bật PASS.
```
</details>

<details><summary>L67</summary>

```text
HÌNH L67 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tổng kết hồ sơ điệp báo số 25. Giữa đại dương khắc nghiệt nơi mọi sinh vật đều chạy đua trang bị giáp dày gai nhọn, Điệp Viên Đại Dương đã chọn một con đường tiến hóa phi thường:". Bố cục: ông trùm điệp báo thế giới ngầm hoạt hình mặc áo măng-tô đen đứng bên bàn tổng kết hồ sơ điệp báo số 25: giữa đại dương nơi các loài chạy đua mang giáp dày gai nhọn, chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn bơi ngạo nghễ với trí tuệ 9 bộ não tỏa sáng.
```
</details>

<details><summary>L68</summary>

```text
HÌNH L68 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "lấy sự mềm mại linh hoạt làm vũ khí, lấy trí thông minh của 9 bộ não làm khiên chắn, và dùng 15 danh tính giả để làm chủ hoàn toàn thế giới ngầm đáy cát!". Bố cục: 15 danh tính giả xoay quanh chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn: sự mềm mại làm vũ khí, trí thông minh làm khiên chắn làm chủ thế giới ngầm đáy cát.
```
</details>

<details><summary>L69</summary>

```text
HÌNH L69 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một sinh vật không hề có xương sống, nhưng lại sở hữu trí tuệ khiến con người phải kinh ngạc và tôn trọng sâu sắc!". Bố cục: ông trùm điệp báo thế giới ngầm hoạt hình mặc áo măng-tô đen đóng dấu ĐÃ DUYỆT màu đỏ lên tập hồ sơ, trao lại cho chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn đang bơi lượn vẫy chào tạm biệt căn cứ tình báo.
```
</details>

<details><summary>L70</summary>

```text
HÌNH L70 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đơn báo cáo cuối cùng: Cho phép điệp viên tiếp tục hoạt động ngầm tại vùng biển Indonesia và tuyệt đối bảo mật danh tính! Ký tên: trùm điệp báo thế giới ngầm!". Bố cục: Bản báo cáo đóng dấu TUYỆT MẬT cho phép siêu điệp viên tiếp tục hoạt động ngầm tại vùng biển Indonesia.
```
</details>

<details><summary>L71</summary>

```text
HÌNH L71 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn anh em thì sao? Nếu được sở hữu một trong hai năng lực của Điệp Viên Đại Dương: có 9 bộ não để làm nhiều việc cùng lúc không lo quá tải, hay tài hóa trang biến hình thành người khác chỉ trong 0,2 giây, anh em chọn cái nào? Hãy để lại bình luận bên dưới nhé!". Bố cục: Hai bàn cân lựa chọn: BÊN TRÁI biểu tượng 9 bộ não thông thái; BÊN PHẢI biểu tượng tài hóa trang biến hình 0,2 giây, các thám tử nhỏ hào hứng giơ thẻ bình chọn.
```
</details>

<details><summary>L72</summary>

```text
HÌNH L72 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hồ sơ điệp viên số 25 xin được niêm phong tại đây. Nhưng tập sau, chúng ta sẽ chuyển thẳng sang hồ sơ vũ khí tối mật trên đất liền để giải mã một chiến binh xe bọc thép lùn tịt cực kỳ lầy lội!". Bố cục: ông trùm điệp báo thế giới ngầm hoạt hình mặc áo măng-tô đen khóa chặt tủ sắt hồ sơ số 25, trên bàn mở ra bản đồ nước Úc với chiếc xe bọc thép đào hang bí ẩn. KHÔNG có chú bạch tuộc đội mũ phớt trong cảnh này.
```
</details>

<details><summary>L73</summary>

```text
HÌNH L73 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một sinh vật mũm mĩm đào hang ở nước Úc, nhưng sở hữu chiếc mông bọc thép dày cứng như bê tông cốt thép, chuyên lừa kẻ thù đuổi vào hang rồi gồng mông dập nát hộp sọ đối thủ vào trần hang đá!". Bố cục: Một sinh vật bí ẩn được vẽ hoàn toàn bằng BÓNG ĐEN ĐẶC TUYỀN (solid black silhouette) hình thú có túi mập mạp đang đào hang ở nước Úc, phần mông phát sáng cứng như thép tấm; có dấu hỏi chấm vàng lớn; KHÔNG vẽ rõ mắt mũi lông. KHÔNG có chú bạch tuộc đội mũ phớt trong cảnh này.
```
</details>

<details><summary>L74</summary>

```text
HÌNH L74 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa hết, nó là sinh vật duy nhất trên thế giới có dây chuyền cơ học thải ra những viên phân hình khối lập phương vuông vức như viên xúc xắc! Đố các bạn biết bóng đen bí ẩn kỳ sau là loài vật nào? Hãy đoán ngay ở phần bình luận nhé!". Bố cục: Cũng chiếc BÓNG ĐEN ĐẶC TUYỀN (solid black silhouette) mập mạp đó thải ra những viên phân hình khối lập phương vuông vức như viên xúc xắc; ba dấu hỏi chấm lớn lấp lánh vàng cam mời gọi khán giả đoán tên. KHÔNG có chú bạch tuộc đội mũ phớt trong cảnh này.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Khi bị kẻ thù bao vây, con vật này không chạy trốn,". Bố cục: Khung dọc: kẻ thù bao vây chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn, chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn rút 6 xúc tu vào hang.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "mà lập tức biến 2 chiếc xúc tu của mình thành một con rắn biển kịch độc le lưỡi dọa lại kẻ đi săn!". Bố cục: Phóng 2 xúc tu vằn đen trắng ra ngoài biến thành rắn biển cạp nong le lưỡi dọa lại kẻ đi săn.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Xin giới thiệu Bạch Tuộc Mimic, siêu điệp viên sải tay 60cm sống dưới đáy cát ở Indonesia.". Bố cục: chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn sải tay 60cm bơi bảnh bao đội mũ phớt kính râm trên nền cát Indonesia, chiếc thước đo chiều cao màu vàng dựng thẳng.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Nó sở hữu tới 9 bộ não độc lập, 3 trái tim bơm dòng máu màu xanh lam óng ánh,". Bố cục: Khung dọc trong suốt: đồ họa 9 bộ não phát sáng, 3 quả tim bơm máu xanh lam óng ánh.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "và tài năng hóa trang vô tiền khoáng hậu: có thể biến hình mượt mà thành 15 loài sinh vật kịch độc khác nhau!". Bố cục: 15 chiếc mặt nạ danh tính kịch độc xoay quanh chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn phát sáng biến hình rực rỡ.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Bị cá thia tấn công? Thụt thân vào hang, biến 2 xúc tu thành rắn biển cạp nong!". Bố cục: chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn thụt thân vào hang, 2 xúc tu vằn đen trắng thò ra uốn éo thành rắn biển cạp nong khiến cá thia bỏ chạy.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Gặp cá nhồng hung dữ? Xòe 8 xúc tu bơi lơ lửng thành cá sư tử đầy gai độc!". Bố cục: chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn xòe 8 xúc tu bơi lơ lửng, da đổi sọc nâu trắng biến thành chú Cá Sư Tử gai độc đầy gai nhọn làm cá nhồng dè chừng.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Cần di chuyển qua bãi cát trống? Ép dẹt toàn thân thành chiếc lá lướt sóng giả dạng cá bơn độc!". Bố cục: chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn ép dẹt toàn thân sát cát thành hình chiếc lá lướt sóng nhẹ nhàng giả dạng con Cá Bơn độc.
```
</details>

<details><summary>S09</summary>

```text
HÌNH S09 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Làn da của nó chứa hàng triệu túi sắc tố đổi màu cơ học chỉ trong 0,2 giây!". Bố cục: Kính hiển vi phóng to hàng triệu túi sắc tố trên da chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn đổi màu cơ học chỉ trong 0,2 giây.
```
</details>

<details><summary>S10</summary>

```text
HÌNH S10 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Bạch Tuộc Mimic nâu vằn trắng, mũ phớt fedora, kính râm đen thám tử; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Một bậc thầy tình báo thế giới ngầm không cần nanh vuốt vẫn khiến cả đại dương phải ngả mũ kính sợ!". Bố cục: Chân dung chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn ngầu lòi giữa đại dương, đội mũ phớt kính râm đen, 8 xúc tu uốn lượn uy quyền của siêu điệp viên thế giới ngầm.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/74 của video YouTube về Bạch Tuộc Mimic). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn. Nhân vật phụ cố định: ông trùm điệp báo thế giới ngầm hoạt hình mặc áo măng-tô đen; cô đặc vụ tình báo hoạt hình đeo tai nghe bộ đàm. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/10 của video YouTube Shorts về Bạch Tuộc Mimic). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Bạch Tuộc Mimic (Thaumoctopus mimicus) hoạt hình màu nâu vằn trắng sọc nổi bật, thân mềm mại, mắt to tròn đeo kính râm đen thám tử, đầu đội chiếc mũ phớt fedora màu xám đen ngầu lòi, tám chiếc xúc tu dẻo dai linh hoạt uốn lượn. Nhân vật phụ: ông trùm điệp báo thế giới ngầm hoạt hình mặc áo măng-tô đen. 
```
</details>

## 7. SEO

- **title:** Sinh Vật 9 Bộ Não Biến Hình Thành 15 Loài Kịch Độc Dưới Đáy Biển?!
- **hook_paragraph:** Bạch Tuộc Mimic (Thaumoctopus mimicus) sở hữu 9 bộ não độc lập, 3 trái tim, máu xanh lam và tài hóa trang đỉnh cao: tự biến hình thành 15 loài sinh vật kịch độc (rắn biển, cá sư tử, cá bơn...) trong 0,2 giây để khắc chế kẻ thù!
- **question:** Nếu được sở hữu 1 siêu năng lực của Bạch Tuộc Mimic: 9 bộ não hoạt động độc lập hay tài hóa trang biến hình trong 0,2 giây, bạn chọn cái nào? Và đoán xem bóng đen tập sau là loài nào?
- **next_teaser:** Bóng đen bí ẩn nước Úc: mông bọc thép nghiền nát hộp sọ kẻ thù và thải ra những viên phân hình lập phương vuông vức!
- **shorts_title:** Sinh Vật 9 Bộ Não Biến Hình Thành 15 Loài Kịch Độc?! 🐙 #độngvật #bạchtuộcmimic
- **shorts_desc:** Bạch Tuộc Mimic sở hữu 9 bộ não, 3 tim, máu xanh lam và khả năng biến hình thành 15 loài kịch độc (rắn biển, cá sư tử...) chỉ trong 0,2 giây! Khám phá bí mật siêu điệp viên đại dương.
- **bullets:** Danh tính giả #1: Hóa thân rắn biển cạp nong và cá sư tử gai độc để dọa kẻ săn mồi · Danh tính giả #2: Ép toàn bộ cơ thể dẹt thành cá bơn lướt cát và sứa biển bồng bềnh · Đế chế 9 não: 500 triệu nơ-ron với 2/3 nằm trong 8 xúc tu hoạt động độc lập · Màn hình nano: Máu xanh lam chứa hemocyanin gốc đồng và hàng triệu túi sắc tố đổi màu trong 0,2s
- **tags:** bạch tuộc mimic, bach tuoc mimic, mimic octopus, thaumoctopus mimicus, bạch tuộc biến hình, bạch tuộc 9 não, động vật kỳ lạ, thế giới động vật, động vật hài hước, vẽ chuyện hoang dã, whiteboard animation, khoa học thú vị
- **hashtags:** #độngvật #bạchtuộcmimic #VẽChuyệnHoangDã

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-25-bach-tuoc-mimic
python src/episode/pipeline.py tts    projects/tap-25-bach-tuoc-mimic     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-25-bach-tuoc-mimic     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-25-bach-tuoc-mimic     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-25-bach-tuoc-mimic              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-25-bach-tuoc-mimic --force
python scripts/beat_sheet.py projects/tap-25-bach-tuoc-mimic               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-25-bach-tuoc-mimic/audio/shorts.wav projects/tap-25-bach-tuoc-mimic/renders/tap-25-bach-tuoc-mimic_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-25-bach-tuoc-mimic
python src/episode/pipeline.py seo    projects/tap-25-bach-tuoc-mimic
python src/episode/episode_doc.py     projects/tap-25-bach-tuoc-mimic
```
