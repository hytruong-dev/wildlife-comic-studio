# TẬP 7 — TÔM TÍT · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-07-tom-tit`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-07-tom-tit`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Tôm Tít |
| Tiêu đề YouTube | Cú Đấm Nóng Bằng Mặt Trời... Đấm Nát Bể Kính Thủy Cung! \| Tôm Tít \| Tập 7 |
| Video dài | `renders/tap-07-tom-tit_long.mp4` — 8:48.2 (528.2s) |
| Shorts | `renders/tap-07-tom-tit_shorts.mp4` — 0:46.5 (46.5s) |
| Thumbnail | `renders/tap-07-tom-tit_thumbnail.jpg` |
| Số hình | dài 63 beat / 63 ảnh riêng; Shorts 11 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.1**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh L33 của video YouTube về Tôm Tít). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoat hình hài hước cường điệu; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi có điểm màu cầu vồng, hai mắt to lồi trên cuống biểu cảm, hai càng búa (club) gập trước ngực như võ sĩ. NỘI DUNG CẢNH L33 (lời thoại: "Bất kỳ ai tò mò thò tay xuống hốc đá tóm thử gã võ sĩ này sẽ lập tức nhận ngay một cú đấm nhanh đến mức mắt thường không kịp chớp, đủ sức đập vỡ nát móng tay
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — VÕ SĨ QUYỀN ANH LÒE LOẸT NHẤT ĐẠI DƯƠNG
**Part 0** → `audio/vs/scene01_p0.wav` (1014 ký tự)

```text
[surprise-oh] Nếu bạn nghĩ một sinh vật dài chưa đầy hai mươi xăng-ti-mét, khoác lên mình bộ cánh sặc sỡ đủ bảy sắc cầu vồng thì chỉ biết làm cảnh dưới đáy biển, thì bạn vừa phạm phải sai lầm chết người nhất cuộc đời! Hãy làm quen với Tôm Tít, kẻ được giới sinh vật học và các thợ lặn kính cẩn gọi bằng cái tên: Mike Tyson của đại dương! Nhìn từ xa, chú ta lộng lẫy như một nàng công chúa vũ hội với mai xanh ngọc, râu đỏ cam và đôi mắt lồi đảo liên tục như hai chiếc ra-đa của người ngoài hành tinh. Thế nhưng, ẩn dưới bộ cánh điệu đà đó là thứ vũ khí cơ học đáng sợ bậc nhất thế giới tự nhiên: một cặp càng búa gập trước ngực với tốc độ ra đòn nhanh ngang ngửa một viên đạn súng trường bắn ra khỏi nòng! Cua biển mai dày ư? Một đấm vỡ nát! Vỏ ốc xà cừ cứng như đá ư? Hai đấm thành bột vụn! Thậm chí ngay cả mặt kính bể cá dày vài xăng-ti-mét cũng từng bị gã này đấm nứt toác khiến các viện hải dương học phải toát mồ hôi hột! [laughter] Đúng là đừng bao giờ đánh giá một võ sĩ qua bộ quần áo lòe loẹt của anh ta!
```
**Part 1** → `audio/vs/scene01_p1.wav` (382 ký tự)

```text
Các thợ lặn biển từ lâu đã đặt cho Tôm Tít biệt danh rùng rợn là Kẻ Chẻ Ngón Tay. Lý do vô cùng đơn giản: bất kỳ ai tò mò thò tay xuống hốc đá tóm thử gã võ sĩ này sẽ lập tức nhận ngay một cú đấm nhanh đến mức mắt thường không kịp chớp, đủ sức đập vỡ nát móng tay và toạc thịt đến tận xương! Một gã tí hon dưới đáy cát nhưng lại mang tâm hồn của một tay giang hồ cục súc khét tiếng!
```

### scene02 — BẢNG CHỈ SỐ RPG — LỖI GAME CỦA TẠO HÓA
*Thẻ chương:* KHI THIÊN NHIÊN QUÊN CÀI GIỚI HẠN SÁT THƯƠNG

**Part 0** → `audio/vs/scene02_p0.wav` (1054 ký tự)

```text
[surprise-wa] Nếu đưa Tôm Tít vào một tựa game nhập vai thế giới mở, chắc chắn nhà phát triển game sẽ bị cộng đồng người chơi tẩy chay kịch liệt vì đã tạo ra một nhân vật gian lận chỉ số đến mức phi lý! Hãy cùng bóc tách bảng chỉ số sinh tồn của gã võ sĩ này: Sức mạnh tấn công A-T-K: chạm nóc chín ngàn chín trăm chín mươi chín điểm! Một cú vung càng của nó tạo ra lực va chạm lên tới một ngàn năm trăm Newton, gấp hàng ngàn lần trọng lượng cơ thể! Tốc độ vung đòn S-P-D: chín trăm chín mươi chín điểm! Nó chỉ mất chưa đầy ba phần ngàn giây để tung ra cú đấm, đạt gia tốc mười ngàn bốn trăm g, nghĩa là còn nhanh hơn cả gia tốc của viên đạn hai mươi hai ly! [question-ah] Bạn chớp mắt mất một phần mười giây đúng không? Trong một cái chớp mắt của bạn, Tôm Tít đã kịp đấm con mồi tới ba mươi lần liên tiếp! Chỉ số phòng thủ D-E-F: tám mươi lăm điểm! Càng của nó được bọc lớp giáp cấu trúc sợi nano chống nứt cực kỳ tinh xảo. Và chỉ số thị giác: phá vỡ mọi thang đo với mười sáu loại tế bào cảm thụ màu sắc, nhìn thấu cả tia cực tím lẫn ánh sáng phân cực!
```
**Part 1** → `audio/vs/scene02_p1.wav` (450 ký tự)

```text
Để bạn dễ hình dung sự khủng khiếp của con số mười ngàn bốn trăm g, một phi công lái máy bay tiêm kích chỉ cần chịu gia tốc chín g là máu đã dồn hết xuống chân và ngất lịm ngay trên bầu trời. Vậy mà đôi càng tí hon này lại phóng đi với gia tốc gấp hơn một ngàn lần giới hạn của con người! Nếu cánh tay của bạn cũng có thể vung nhanh như càng tôm tít, bạn hoàn toàn có thể ném một quả bóng chày bay thẳng vào quỹ đạo Trái Đất mà không cần tên lửa đẩy!
```
**Part 2** → `audio/vs/scene02_p2.wav` (281 ký tự)

```text
Mà khoan đã, đó mới chỉ là phe đấm thôi! Họ hàng nhà Tôm Tít còn có cả phe đâm, mang đôi càng đầy gai nhọn như chiếc xiên nướng, phóng ra xiên trúng con cá đang bơi ngang chỉ trong tích tắc. [laughter] Một phe đấm bốc, một phe đấu kiếm, đúng là cả một gia tộc võ lâm dưới đáy biển!
```

### scene03 — CÚ ĐẤM CAVITATION & GIÁP NANO BOULIGAND
*Thẻ chương:* TẠO RA SỨC NÓNG NGANG BỀ MẶT MẶT TRỜI

**Part 0** → `audio/vs/scene03_p0.wav` (1063 ký tự)

```text
[surprise-oh] Nhưng sự thật điên rồ nhất vẫn chưa dừng lại ở đó! Cú đấm của Tôm Tít uy lực đến mức nó tạo ra một hiện tượng vật lý kỳ dị mang tên Cáp-vi-tây-sơn, tức Bọt Khí Xâm Thực! Do chiếc càng vung đi với tốc độ xé gió dưới nước, áp suất nước phía sau chiếc càng sụt giảm đột ngột xuống mức gần như chân không, làm nước sôi ngay lập tức ở nhiệt độ phòng và sinh ra một bọt khí cực nhỏ! Ngay khoảnh khắc tiếp theo, khi bọt khí này sụp đổ dưới áp suất nước xung quanh, nó tạo ra một vụ nổ sóng xung kích khủng khiếp, sinh ra nhiệt độ cục bộ lên tới bốn ngàn bảy trăm độ C, gần bằng bề mặt của Mặt Trời! [surprise-ah] Vụ nổ này thậm chí còn phát ra một tia sáng le lói mà giới khoa học gọi là hiện tượng phát quang do âm thanh Xô-nô-lu-mi-nét-xen! Nghĩa là mỗi cú ra đòn của Tôm Tít thực chất là một đòn tấn công kép: đòn thứ nhất là cú đập của chiếc càng cứng, và đòn thứ hai là sóng xung kích từ vụ nổ nhiệt độ Mặt Trời! [laughter] Dù nó có đấm trượt mục tiêu thì sóng xung kích của bọt khí sụp đổ vẫn biến con mồi thành đĩa thức ăn nướng chín trong nháy mắt!
```
**Part 1** → `audio/vs/scene03_p1.wav` (617 ký tự)

```text
[surprise-wa] Vậy câu hỏi đặt ra là: Tại sao chiếc càng của Tôm Tít không bị vỡ vụn khi phải chịu hàng ngàn cú va chạm kinh hoàng như vậy? Bí mật nằm ở cấu trúc nano Bu-li-găng! Bên trong chiếc càng búa, các sợi khoáng chất nano được xếp chồng chéo lên nhau theo hình xoắn ốc giống như hàng ngàn lớp ván ép siêu cứng. Khi một vết nứt nhỏ hình thành, nó không thể lan thẳng mà bị bẻ cong theo các rãnh xoắn, tự tiêu tán năng lượng va đập! Quân đội Mỹ và các kỹ sư hàng không vũ trụ hiện đang nghiên cứu cấu trúc chiếc càng của Tôm Tít để chế tạo thế hệ áo giáp chống đạn và vỏ máy bay siêu nhẹ tiếp theo cho nhân loại!
```
**Part 2** → `audio/vs/scene03_p2.wav` (273 ký tự)

```text
Mà cái hay nhất là gì biết không? Đôi búa ấy chẳng bao giờ phải đem đi sửa! Cứ mỗi lần lột xác, Tôm Tít lại được thay luôn một cặp búa mới tinh, cứ như võ sĩ được tài trợ đôi găng mới sau mỗi mùa giải vậy! [laughter] Nhưng cái giá của món quà đó thì... lát nữa bạn sẽ biết!
```

### scene04 — GÓT CHÂN A-SIN — MÙA LỘT XÁC MỀM NHƯ THẠCH
*Thẻ chương:* VÕ SĨ VÔ ĐỊCH BIẾN THÀNH MIẾNG THẠCH BƠ

**Part 0** → `audio/vs/scene04_p0.wav` (846 ký tự)

```text
[sigh] Nghe đến đây, bạn hẳn đang nghĩ Tôm Tít chính là vị vua bất khả chiến bại của rạn san hô, không sợ trời không sợ đất đúng không? Nhưng tạo hóa luôn rất thích trêu đùa những kẻ mạnh! Võ sĩ Mike Tyson đại dương này có một điểm yếu chí mạng khiến nó phải ôm hận suốt đời: Mùa lột xác! Giống như loài tôm cua, để lớn lên, Tôm Tít bắt buộc phải rũ bỏ toàn bộ lớp vỏ cứng bên ngoài, bao gồm cả đôi càng búa thần thánh của mình. Và bạn đoán xem điều gì xảy ra? Ngay sau khi lột xác, toàn bộ cơ thể lẫn đôi càng của nó mềm nhũn ra như một miếng thạch dừa hay bánh flan mới ra lò! [laughter] Kẻ từng đấm nứt kính bể cá giờ đây mềm yếu đến mức một con cá nhỏ hay một chú ốc sên bò qua cũng có thể xơi tái nó ngon lành! Trong suốt vài tuần chờ lớp vỏ mới cứng lại, gã giang hồ này phải trốn chui trốn lủi tận đáy hang sâu, nhịn đói và run rẩy sợ hãi!
```
**Part 1** → `audio/vs/scene04_p1.wav` (676 ký tự)

```text
Điều hài hước nhất là nghệ thuật dọa ma của nó trong giai đoạn này! Nếu chẳng may có kẻ thù mò vào miệng hang, Tôm Tít sẽ lập tức phùng mang trợn mắt, giương đôi càng mềm oặt ra đe dọa giống như đang nói: Nhìn càng tao đây này, bước vào là nát người đấy nhé! Nhưng thực chất đó hoàn toàn là một đòn nghi binh trắng trợn. Nếu kẻ thù liều lĩnh xông vào, chiếc càng mềm của nó chạm nhẹ vào đá cũng đau thấu trời xanh! Ngoài ra, gã này còn là nỗi ác mộng kinh hoàng của những người chơi cá cảnh biển: lỡ mua nhầm một chú tôm tít về thả vào bể, sáng hôm sau bạn sẽ thấy toàn bộ tôm, cua, ốc đắt tiền đã bị đấm vỡ nát, và bể kính thì nứt một vệt dài sẵn sàng vỡ tung tóe ra sàn nhà!
```

### scene05 — VỤ ÁN THỦY CUNG BỂ NÁT & ĐÔI MẮT THẦN 16 MÀU
*Thẻ chương:* ĐẤM NỨT KÍNH THỦY CUNG VÀ NHÌN THẤY TẾ BÀO UNG THƯ

**Part 0** → `audio/vs/scene05_p0.wav` (845 ký tự)

```text
[surprise-oh] Những giai thoại về sức mạnh của Tôm Tít hoàn toàn không phải lời đồn thổi trên bàn nhậu! Vào tháng tư năm 1998, tại một thủy cung nổi tiếng ở hạt Norfolk nước Anh, một chú tôm tít dài vỏn vẹn mười xăng-ti-mét được đặt tên là Tyson đã làm nên một vụ bê bối chấn động! Có vẻ như bực mình vì tấm gương phản chiếu chính mình trên vách bể, chú ta đã tung ra một cú đấm thép thẳng vào tấm kính dày hơn sáu mi-li-mét! Kết quả là mặt kính nứt đôi thành hình mạng nhện, nước biển bắt đầu phun ra xối xả và toàn bộ nhân viên thủy cung phải kích hoạt còi báo động khẩn cấp để sơ tán du khách và cứu vớt các loài sinh vật khác! Từ đó, các viện hải dương học trên khắp thế giới ban hành một luật bất thành văn: Tuyệt đối không bao giờ nuôi Tôm Tít trong bể kính thủy tinh thông thường, mà bắt buộc phải dùng bể nhựa acrylic chống đạn siêu dày!
```
**Part 1** → `audio/vs/scene05_p1.wav` (738 ký tự)

```text
[surprise-wa] Bên cạnh cú đấm thần sầu, Tôm Tít còn sở hữu đôi mắt kỳ dị bậc nhất hành tinh! Con người chúng ta chỉ có ba loại tế bào cảm thụ màu sắc là đỏ, lục và lam. Nhưng Tôm Tít sở hữu tới mười sáu loại thụ thể màu sắc khác nhau! Nó không chỉ nhìn thấy dải màu rực rỡ gấp năm lần chúng ta, mà còn nhìn thấu cả tia cực tím U-V và là sinh vật duy nhất trên Trái Đất nhìn được ánh sáng phân cực tròn! Mỗi con mắt của nó có thể chuyển động độc lập ba trăm sáu mươi độ và tự đo khoảng cách không gian ba chiều mà không cần đến mắt còn lại. Các nhà khoa học hiện đang sao chép cấu trúc mắt của Tôm Tít để chế tạo các loại cảm biến y tế siêu nhạy, có khả năng phát hiện sớm các tế bào ung thư trong cơ thể người từ những giai đoạn đầu tiên!
```
**Part 2** → `audio/vs/scene05_p2.wav` (365 ký tự)

```text
[surprise-oh] Chưa hết đâu! Tôm Tít còn dùng chính ánh sáng phân cực để nhắn tin bí mật cho nhau, trên cơ thể có những mảng phát tín hiệu mà kẻ thù nhìn vào chẳng thấy gì. Và gã giang hồ cục súc này hóa ra lại là một người chồng chung thủy: có loài sống thành cặp trong cùng một hang tới hai mươi năm! [laughter] Ra ngoài thì đấm nứt kính, về nhà thì ngoan như mèo!
```

### scene06 — BÀI HỌC SINH TỒN TỪ TÔM TÍT
*Thẻ chương:* BIẾT THU MÌNH KHI YẾU MỀM MỚI LÀ KẺ KHÔN NGOAN

**Part 0** → `audio/vs/scene06_p0.wav` (698 ký tự)

```text
Từ những rạn san hô nhiệt đới nông cạn cho đến những đáy bùn tăm tối ngoài đại dương, Tôm Tít đã dạy cho chúng ta một bài học sinh tồn vô cùng sâu sắc của mẹ thiên nhiên: Sở hữu sức mạnh vô song như cú đấm viên đạn không có nghĩa là bạn luôn luôn bất khả chiến bại. Đỉnh cao thực sự của kẻ sinh tồn không phải là lúc khoe khoang sức mạnh, mà là biết nhẫn nhịn, thu mình trốn kỹ trong hang tối khi cơ thể đang lột xác yếu mềm nhất, kiên nhẫn chờ đợi lớp áo giáp mới cứng cáp hơn rồi mới bước ra làm chủ cuộc chơi! [question-oh] Bạn ấn tượng nhất với điều gì ở gã võ sĩ đại dương này: Cú đấm bọt khí nóng ngang Mặt Trời hay đôi mắt nhìn thấu cả tế bào ung thư? Hãy để lại bình luận cho mình biết nhé!
```
**Part 1** → `audio/vs/scene06_p1.wav` (334 ký tự)

```text
Ở tập tiếp theo, chúng ta sẽ rời xa đáy biển sâu để đến với một sinh vật kỳ dị không kém: một loài cá nhưng lại biết trèo cây, biết nhảy nhót trên bùn và có thể thở bằng da suốt nhiều giờ trên cạn! Bạn có đoán được đó là ai không? Đừng quên bấm Đăng ký kênh Vẽ Chuyện Hoang Dã và bật Chuông thông báo để không bỏ lỡ tập tiếp theo nhé!
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Một cú đấm dưới nước mạnh ngang một viên đạn súng trường, sinh ra nhiệt độ bốn ngàn bảy trăm độ C gần bằng bề mặt Mặt Trời! [surprise-wa] Kẻ sở hữu siêu năng lực điên rồ đó chính là Tôm Tít, võ sĩ Mike Tyson khét tiếng của đại dương! Với đôi càng búa tí hon, nó phóng đòn với gia tốc mười ngàn bốn trăm g, đập vỡ nát mai cua, vỏ ốc xà cừ và thậm chí từng đấm nứt toác cả mặt kính bể cá dày cộp của một thủy cung ở nước Anh! Cú vung càng nhanh đến mức làm sôi nước biển, tạo ra vụ nổ bọt khí xâm thực nướng chín con mồi trong nháy mắt! Thế nhưng, cứ mỗi mùa lột xác, gã võ sĩ bất khả chiến bại này lại biến thành một miếng thạch bơ mềm nhũn, phải trốn chui trốn lủi sợ cả một con ốc sên bò ngang qua! [laughter] Bí mật về đôi mắt mười sáu dải màu giúp phát hiện ung thư của gã này đã có ở video dài bên dưới. Bấm xem ngay màn đại chiến siêu hài hước này nhé!
```

**Whisper prompt:** `Tôm Tít Mantis Shrimp, Mike Tyson đại dương, Cavitation, Bouligand, 10400g, 80 cây số một giờ, 1500 Newton, Sonoluminescence, Mặt Trời, UV, phân cực tròn, ngón tay chẻ đôi`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| hai mươi xăng-ti-mét | 20cm |
| bảy sắc cầu vồng | 7 sắc cầu vồng |
| vài xăng-ti-mét | vài cm |
| chín ngàn chín trăm chín mươi chín | 9.999 |
| một ngàn năm trăm | 1.500 |
| chín trăm chín mươi chín | 999 |
| ba phần ngàn giây | 0,003s |
| mười ngàn bốn trăm g | 10.400g |
| hai mươi hai ly | 22 ly |
| một phần mười giây | 0,1s |
| ba mươi lần | 30 lần |
| tám mươi lăm | 85 |
| mười sáu loại | 16 loại |
| mười sáu dải màu | 16 dải màu |
| mười sáu | 16 |
| chín g | 9g |
| một ngàn lần | 1.000 lần |
| bốn ngàn bảy trăm độ C | 4.700°C |
| tháng tư năm 1998 | tháng 4 năm 1998 |
| mười xăng-ti-mét | 10cm |
| sáu mi-li-mét | 6mm |
| ba loại | 3 loại |
| ba trăm sáu mươi độ | 360° |
| ba chiều | 3D |
| Mơn-ti-xơ | Mantis |
| S-cu-la-rút | Scyllarus |
| Bu-li-găng | Bouligand |
| Cáp-vi-tây-sơn | Cavitation |
| Xô-nô-lu-mi-nét-xen | Sonoluminescence |
| A-T-K | ATK |
| S-P-D | SPD |
| D-E-F | DEF |
| I-Q | IQ |
| U-V | UV |
| hai mươi năm | 20 năm |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · VÕ SĨ QUYỀN ANH LÒE LOẸT NHẤT ĐẠI DƯƠNG · 73.3s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:11.5 (11.5s) | L01 | Nếu bạn nghĩ một sinh vật dài chưa đầy 20cm, khoác lên mình bộ cánh sặc sỡ đủ 7 sắc cầu vồng thì chỉ biết làm cảnh dưới đáy biển, thì bạn vừa phạm phải sai lầm chết người nhất cuộc đời! | **< 20 cm** · chiều dài tí hon · L/380 · [0.45, 0.55] | _(nội dung ảnh)_ Tôm Tít đứng giới thiệu, mai xanh ngọc, mắt lồi, càng gập trước ngực |
| b02 | 00:11.5–00:18.2 (6.7s) | L02 | Hãy làm quen với Tôm Tít, kẻ được giới sinh vật học và các thợ lặn kính cẩn gọi bằng cái tên: Mike Tyson của đại dương! | **TYSON** · võ sĩ đại dương · R/420 · [0.65, 0.45] | _(nội dung ảnh)_ Tôm Tít võ sĩ Mike Tyson: găng đỏ, đai vô địch |
| b03 | 00:18.2–00:25.9 (7.7s) | L19 | Nhìn từ xa, chú ta lộng lẫy như một nàng công chúa vũ hội với mai xanh ngọc, râu đỏ cam và đôi mắt lồi đảo liên tục như hai chiếc ra-đa của người ngoài | **RA-ĐA** · mắt lồi xoay độc lập · R/380 · [0.55, 0.35] | Cận cảnh chú Tôm Tít hoạt hình đầy màu sắc sặc sỡ, hai con mắt to tròn lồi hẳn ra ngoài đang xoay theo hai hướng khác nhau, trên mỗi con mắt có hình vẽ chiếc chảo vệ tinh ra-đa công nghệ cao đang phát ra các vòng sóng vô tuyến quét không gian, biểu cảm cực kỳ tò mò và hài hước. |
| b04 | 00:25.9–00:36.3 (10.4s) | L03 | hành tinh. Thế nhưng, ẩn dưới bộ cánh điệu đà đó là thứ vũ khí cơ học đáng sợ bậc nhất thế giới tự nhiên: một cặp càng búa gập trước ngực với tốc độ ra đòn nhanh ngang ngửa một viên đạn súng trường bắn ra khỏi nòng! | **NHƯ ĐẠN** · tốc độ súng trường · R/380 · [0.65, 0.45] | _(nội dung ảnh)_ Càng búa phóng nhanh như viên đạn bay song song, vệt tốc độ |
| b05 | 00:36.3–00:41.9 (5.6s) | L32 | Cua biển mai dày ư? Một đấm vỡ nát! Vỏ ốc xà cừ cứng như đá ư? Hai đấm thành bột vụn! | **1 ĐẤM** · vỡ nát mai cua · L/380 · [0.6, 0.5]<br>**2 ĐẤM** · nghiền nát vỏ ốc · R/420 · [0.75, 0.6] | Chú Tôm Tít hoạt hình tung một cú đấm búa cực mạnh vào chính giữa chiếc mai của một con cua biển to lớn, chiếc mai cua dày cứng nứt toác thành nhiều mảnh vỡ vụn văng ra, bên cạnh là một chiếc vỏ ốc xà cừ bị đập nát thành bột trắng, các vệt sóng chấn động màu vàng cam nổ tung tóe, con cua mắt hoa đầu óc choáng váng. |
| b06 | 00:41.9–00:53.5 (11.6s) | L05 | Thậm chí ngay cả mặt kính bể cá dày vài cm cũng từng bị gã này đấm nứt toác khiến các viện hải dương học phải toát mồ hôi hột! Đúng là đừng bao giờ đánh giá một võ sĩ qua bộ quần áo lòe loẹt của anh ta! | **NỨT KÍNH** · bể cá dày vài cm · L/400 · [0.55, 0.45] | _(nội dung ảnh)_ Bể kính thủy cung nứt mạng nhện, nước phun, nhân viên hoảng hốt |
| b07 | 00:53.5–00:59.2 (5.8s) | L06 | Các thợ lặn biển từ lâu đã đặt cho Tôm Tít biệt danh rùng rợn là Kẻ Chẻ Ngón Tay. Lý do vô cùng đơn giản: | **CẢNH BÁO** · kẻ chẻ ngón tay · L/380 · [0.45, 0.5] | _(nội dung ảnh)_ Thợ lặn rụt tay, ngón cái băng bó; tôm trong hốc đá trừng mắt kiểu giang hồ |
| b08 | 00:59.2–01:08.9 (9.6s) | L33 | bất kỳ ai tò mò thò tay xuống hốc đá tóm thử gã võ sĩ này sẽ lập tức nhận ngay một cú đấm nhanh đến mức mắt thường không kịp chớp, đủ sức đập vỡ nát móng tay và toạc thịt đến tận xương! | **TOẠC THỊT** · tới tận xương · R/420 · [0.6, 0.55] | Tạo hình ảnh (cảnh L33 của video YouTube về Tôm Tít). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoat hình hài hước cường điệu; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố  |
| b09 | 01:08.9–01:13.3 (4.4s) | L20 | Một gã tí hon dưới đáy cát nhưng lại mang tâm hồn của một tay giang hồ cục súc khét tiếng! | **GIANG HỒ** · gã tí hon cục súc · R/420 · [0.5, 0.55] | Chú Tôm Tít hoạt hình nhỏ xíu đứng trên bãi cát trắng, mặc chiếc áo khoác da màu đen phong cách giang hồ cực ngầu, đeo kính râm đen bóng, miệng ngậm một que tăm, hai tay chống hông biểu cảm ngang tàng thách thức, phía sau có vài vỏ sò nhỏ đang co rúm sợ hãi. |

### scene02 · BẢNG CHỈ SỐ RPG — LỖI GAME CỦA TẠO HÓA · 93.5s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:10.2 (10.2s) | L07 | Nếu đưa Tôm Tít vào một tựa game nhập vai thế giới mở, chắc chắn nhà phát triển game sẽ bị cộng đồng người chơi tẩy chay kịch liệt vì đã tạo ra một nhân vật gian lận chỉ số đến mức phi lý! |  | _(nội dung ảnh)_ Màn hình chỉ số RPG, thanh chỉ số tràn, nhà phát triển ôm đầu |
| b02 | 00:10.2–00:23.6 (13.4s) | L21 | Hãy cùng bóc tách bảng chỉ số sinh tồn của gã võ sĩ này: Sức mạnh tấn công ATK: chạm nóc 9.999 điểm! Một cú vung càng của nó tạo ra lực va chạm lên tới 1.500 Newton, gấp hàng ngàn lần trọng lượng cơ thể! | **ATK 9999** · sức mạnh tối đa · L/360 · [0.35, 0.45]<br>**1.500 N** · lực va chạm · R/420 · [0.7, 0.5] | Nửa trái là Tôm Tít võ sĩ cơ bắp vung chiếc càng búa bọc lửa đỏ cam giáng một đòn cực mạnh xuống. Nửa phải là một quả tạ sắt khổng lồ bị đập lõm sâu biến dạng bẹp dúm, xung quanh tỏa ra các tia sét màu vàng và sóng xung kích bùng nổ dữ dội. |
| b03 | 00:23.6–00:35.0 (11.4s) | L22 | Tốc độ vung đòn SPD: 999 điểm! Nó chỉ mất chưa đầy 0,003s để tung ra cú đấm, đạt gia tốc 10.400g, nghĩa là còn nhanh hơn cả gia tốc của viên đạn 22 ly! | **SPD 999** · tốc độ tối đa · L/360 · [0.25, 0.4]<br>**10.400 g** · nhanh hơn đạn 22 ly · R/420 · [0.65, 0.45] | Nửa trái một chiếc đồng hồ bấm giờ siêu tốc kim đang nhích một vạch cực nhỏ. Nửa phải là đường đua tốc độ: một viên đạn đồng sáng loáng đang bay xé gió bốc khói phía sau, nhưng phía trước nó là chiếc càng búa của Tôm Tít đang phóng vút vượt lên dẫn trước với những vệt tốc độ màu vàng cam. |
| b04 | 00:35.0–00:41.8 (6.8s) | L23 | Bạn chớp mắt mất 0,1s đúng không? Trong một cái chớp mắt của bạn, Tôm Tít đã kịp đấm con mồi tới 30 lần liên tiếp! | **0,1s** · 1 cái chớp mắt · L/380 · [0.3, 0.45]<br>**30 ĐẤM** · liên hoàn cước · R/420 · [0.7, 0.45] | Chia đôi so sánh hài hước: Bên TRÁI là khuôn mặt một người hoạt hình đang từ từ chớp mắt lại, mí mắt mới khép một nửa. Bên PHẢI là Tôm Tít đang biến thành một cơn lốc cú đấm ảo diệu, hàng chục chiếc càng bóng ma tung ra liên hoàn như mưa sao băng, con cua đối diện chóng mặt mắt quay mòng mòng đầy sao bay quanh đầu. |
| b05 | 00:41.8–00:48.1 (6.3s) | L34 | Chỉ số phòng thủ DEF: 85 điểm! Càng của nó được bọc lớp giáp cấu trúc sợi nano chống nứt cực kỳ tinh xảo. | **DEF 85** · giáp nano chống nứt · L/360 · [0.5, 0.5] | Ở GIỮA chú Tôm Tít giơ chiếc càng búa lên đỡ như khiên, mặt tự tin nháy mắt. Lớp vỏ càng có họa tiết các sợi đan xoắn lưới phát sáng xanh ngọc như áo giáp công nghệ. BÊN PHẢI một chiếc búa tạ sắt khổng lồ đang nện thẳng vào càng nhưng chính cán búa gãy đôi, đầu búa nứt vỡ văng mảnh. Càng tôm không một vết xước, có vài tia lấp lánh. |
| b06 | 00:48.1–00:55.0 (7.0s) | L31 | Và chỉ số thị giác: phá vỡ mọi thang đo với 16 loại tế bào cảm thụ màu sắc, nhìn thấu cả tia cực tím lẫn ánh sáng phân cực! | **16 MÀU** · quang phổ cực tím & UV · R/400 · [0.7, 0.45] | _(nội dung ảnh)_ Tầm nhìn người 3 màu vs tôm 16 màu + UV + phân cực |
| b07 | 00:55.0–01:05.3 (10.3s) | L35 | Để bạn dễ hình dung sự khủng khiếp của con số 10.400g, một phi công lái máy bay tiêm kích chỉ cần chịu gia tốc 9g là máu đã dồn hết xuống chân và ngất lịm ngay trên bầu trời. | **9 G** · giới hạn phi công tiêm kích · L/420 · [0.45, 0.45] | Một chiếc máy bay phản lực tiêm kích màu xám bạc đang ngoặt gắt trên trời với vệt khói trắng cong. Phóng to buồng lái kính trong suốt: phi công đội mũ bảo hiểm trắng, đeo mặt nạ dưỡng khí, mắt xoắn ốc ngất lịm đầu gục sang bên, má xệ xuống vì lực G. Vài mũi tên đỏ cong chỉ xuống chân phi công thể hiện máu dồn xuống. KHÔNG có Tôm Tít trong cảnh này. |
| b08 | 01:05.3–01:10.2 (4.9s) | L36 | Vậy mà đôi càng tí hon này lại phóng đi với gia tốc gấp hơn 1.000 lần giới hạn của con người! | **x1000 LẦN** · vượt giới hạn con người · L/380 · [0.6, 0.45] | Chia đôi hài hước: BÊN TRÁI nhỏ là phi công ngất xỉu nằm bẹp trên ghế lái. BÊN PHẢI lớn: chú Tôm Tít tí hon tỉnh bơ, một càng phóng đấm ra với các vệt siêu tốc dày đặc màu vàng cam và luồng sóng xé nước, tay kia cầm cốc trà sữa, mặt thản nhiên huýt sáo, không hề chóng mặt. |
| b09 | 01:10.2–01:18.9 (8.7s) | L24 | Nếu cánh tay của bạn cũng có thể vung nhanh như càng tôm tít, bạn hoàn toàn có thể ném một quả bóng chày bay thẳng vào quỹ đạo Trái Đất mà không cần tên lửa đẩy! | **VŨ TRỤ** · ném bóng vào quỹ đạo · R/380 · [0.65, 0.4] | Chú Tôm Tít hoạt hình mặc trang phục cầu thủ bóng chày màu đỏ trắng, vung chiếc càng búa ném một quả bóng chày bay vút xé toạc bầu khí quyển bay thẳng vào không gian vũ trụ quay quanh Trái Đất bên cạnh các vệ tinh nhân tạo, có vệt lửa và các vì sao lấp lánh. |
| b10 | 01:18.9–01:29.3 (10.4s) | L60 | Mà khoan đã, đó mới chỉ là phe đấm thôi! Họ hàng nhà Tôm Tít còn có cả phe đâm, mang đôi càng đầy gai nhọn như chiếc xiên nướng, phóng ra xiên trúng con cá đang bơi ngang chỉ trong tích tắc. | **PHE ĐÂM** · càng gai như xiên nướng · L/380 · [0.62, 0.5] | Dưới đáy cát, một chú tôm tít KHÁC (họ hàng phe đâm: thân dài màu nâu vàng sọc, cùng kiểu mắt lồi trên cuống) thò nửa người ra khỏi hang cát, phóng đôi càng dài mảnh đầy gai nhọn như chiếc xiên nướng thịt về phía BÊN PHẢI, xiên trúng một con cá nhỏ màu xanh đang bơi ngang, con cá mắt xoắn ngạc nhiên. Vệt tốc độ màu vàng cam sau càng. Mặt chú tôm phe đâm tập trung như kiếm sĩ. |
| b11 | 01:29.3–01:33.5 (4.2s) | L61 | Một phe đấm bốc, một phe đấu kiếm, đúng là cả một gia tộc võ lâm dưới đáy biển! |  | Cảnh hài kiểu phim võ hiệp: BÊN TRÁI chú Tôm Tít mai xanh ngọc đeo găng đấm bốc đỏ thủ thế quyền anh; BÊN PHẢI chú tôm tít họ hàng màu nâu vàng sọc cầm đôi càng gai như hai thanh kiếm, thủ thế đấu kiếm. Hai bên cúi chào nhau theo kiểu võ lâm trên một võ đài bằng tảng đá phẳng dưới đáy biển. Phía sau là một hàng tôm tít nhỏ đủ màu ngồi xem như đệ tử môn phái, vài con cá cổ vũ. |

### scene03 · CÚ ĐẤM CAVITATION & GIÁP NANO BOULIGAND · 102.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.6 (9.6s) | L37 | Nhưng sự thật điên rồ nhất vẫn chưa dừng lại ở đó! Cú đấm của Tôm Tít uy lực đến mức nó tạo ra một hiện tượng vật lý kỳ dị mang tên Cavitation, tức Bọt Khí Xâm Thực! | **CAVITATION** · bọt khí xâm thực · L/380 · [0.55, 0.5] | Cận cảnh dưới nước: chú Tôm Tít vừa tung cú đấm càng búa sang phải, ngay phía sau đầu càng xuất hiện một chuỗi bọt khí tròn trong suốt lấp lánh kỳ lạ đang hình thành trong vệt nước xoáy. Tôm Tít quay đầu nhìn các bọt khí với mắt tròn xoe kinh ngạc. Phía trên có vài dấu chấm than vẽ tay. |
| b02 | 00:09.6–00:20.7 (11.0s) | L38 | Do chiếc càng vung đi với tốc độ xé gió dưới nước, áp suất nước phía sau chiếc càng sụt giảm đột ngột xuống mức gần như chân không, làm nước sôi ngay lập tức ở nhiệt độ phòng và sinh ra một bọt khí cực nhỏ! | **CHÂN KHÔNG** · áp suất sụt giảm · L/380 · [0.35, 0.45]<br>**NƯỚC SÔI** · ngay nhiệt độ phòng · R/420 · [0.65, 0.5] | Bố cục giải thích khoa học: Ở GIỮA chiếc càng búa đang vung sang phải cực nhanh để lại vệt nước. Ngay sau đuôi càng là một vùng trống xoáy tròn (vùng chân không) với nước đang sủi bọt sùng sục như nồi nước sôi. BÊN TRÁI một chiếc nhiệt kế màu xanh dương mát lạnh chỉ mức thấp (nhiệt độ phòng) có bông tuyết nhỏ, cạnh đó một bình áp suất có kim đồng hồ tụt về 0. Tương phản: nước sôi mà nhiệt kế vẫn mát. |
| b03 | 00:20.7–00:32.2 (11.5s) | L25 | Ngay khoảnh khắc tiếp theo, khi bọt khí này sụp đổ dưới áp suất nước xung quanh, nó tạo ra một vụ nổ sóng xung kích khủng khiếp, sinh ra nhiệt độ cục bộ lên tới 4.700°C, gần bằng bề mặt của Mặt Trời! | **4.700°C** · nóng ngang Mặt Trời · R/380 · [0.65, 0.45] | Bố cục 16:9 chia đôi đối chiếu kịch tính: Bên trái là vụ nổ bọt khí nước phát sáng chói lòa tỏa nhiệt đỏ rực dưới nước, bên phải là vầng Mặt Trời rực lửa với các quầng lửa plasma cuồn cuộn, ở giữa có một cột nhiệt kế đo nhiệt độ kịch trần bốc khói dữ dội. |
| b04 | 00:32.2–00:38.9 (6.7s) | L26 | Vụ nổ này thậm chí còn phát ra một tia sáng le lói mà giới khoa học gọi là hiện tượng phát quang do âm thanh Sonoluminescence! | **PHÁT QUANG** · âm thanh sinh ánh sáng · L/400 · [0.5, 0.5] | Dưới đáy biển, một bọt khí cực nhỏ phát sáng lấp lánh như một ngôi sao nhỏ phát ra tia sáng xanh lam rực rỡ, xung quanh là các vòng sóng âm thanh tròn đồng tâm lan tỏa, bên cạnh có một nhà khoa học hoạt hình đeo kính lúp soi vào và kinh ngạc tròn mắt há hốc mồm. |
| b05 | 00:38.9–00:49.2 (10.4s) | L39 | Nghĩa là mỗi cú ra đòn của Tôm Tít thực chất là một đòn tấn công kép: đòn thứ nhất là cú đập của chiếc càng cứng, và đòn thứ hai là sóng xung kích từ vụ nổ nhiệt độ Mặt Trời! | **ĐÒN KÉP** · càng đập + sóng nhiệt · R/420 · [0.65, 0.45] | Chia đôi thành hai khung tròn nối nhau bằng mũi tên cong cam: KHUNG TRÁI chiếc càng búa cứng đập trúng vỏ một con cua, tia va chạm vàng. KHUNG PHẢI ngay sau đó một bọt khí nổ tung thành quả cầu lửa nhỏ rực sáng như Mặt Trời tí hon, sóng xung kích vòng tròn hất văng con cua lần nữa, cua mắt xoắn. Chú Tôm Tít đứng giữa hai khung giơ hai càng hình chữ V chiến thắng. |
| b06 | 00:49.2–00:56.6 (7.4s) | L27 | Dù nó có đấm trượt mục tiêu thì sóng xung kích của bọt khí sụp đổ vẫn biến con mồi thành đĩa thức ăn nướng chín trong nháy mắt! | **NƯỚNG CHÍN** · sóng xung kích nấu chín · L/380 · [0.65, 0.55] | Bố cục 16:9 hài hước: Chú Tôm Tít vung càng đấm trượt sang một bên, nhưng luồng sóng xung kích bốc hơi nóng làm một con cua đối diện biến thành màu đỏ cam chín thơm phức, trên mai cua bốc khói nghi ngút và có một lát chanh bên cạnh như đĩa hải sản nướng, mắt con cua quay tròn chóng mặt ngơ ngác. |
| b07 | 00:56.6–01:04.6 (8.0s) | L40 | Vậy câu hỏi đặt ra là: Tại sao chiếc càng của Tôm Tít không bị vỡ vụn khi phải chịu hàng ngàn cú va chạm kinh hoàng như vậy? Bí mật nằm ở cấu trúc nano Bouligand! | **BOULIGAND** · cấu trúc nano chống nứt · R/400 · [0.5, 0.5] | Chú Tôm Tít ngồi trên đống vỏ ốc, vỏ cua và đá vụn vỡ nát chất cao như núi, nó giơ chiếc càng búa lên ngắm nghía bằng kính lúp với vẻ thắc mắc, trên đầu có dấu chấm hỏi cam to vẽ tay. Chiếc càng vẫn nhẵn bóng nguyên vẹn không một vết nứt, lấp lánh. |
| b08 | 01:04.6–01:12.3 (7.7s) | L10 | Bên trong chiếc càng búa, các sợi khoáng chất nano được xếp chồng chéo lên nhau theo hình xoắn ốc giống như hàng ngàn lớp ván ép siêu cứng. | **XOẮN ỐC** · hàng ngàn lớp ván ép · L/400 · [0.5, 0.5] | _(nội dung ảnh)_ Mặt cắt càng: sợi nano xoắn Bouligand bẻ cong vết nứt; kỹ sư quân sự + nhà khoa học soi kính lúp |
| b09 | 01:12.3–01:18.9 (6.6s) | L41 | Khi một vết nứt nhỏ hình thành, nó không thể lan thẳng mà bị bẻ cong theo các rãnh xoắn, tự tiêu tán năng lượng va đập! | **TIÊU TÁN** · tự bẻ cong vết nứt · R/420 · [0.6, 0.55] | Sơ đồ khoa học vẽ tay mặt cắt lớp vỏ càng: nhiều lớp sợi mỏng xếp xoay dần như cầu thang xoắn ốc (màu xanh ngọc, cam, vàng xen kẽ). Một vết nứt màu đỏ hình tia sét đi vào từ mép trái, bị bẻ cong uốn lượn ngoằn ngoèo theo các lớp xoắn, càng vào sâu càng mảnh và mờ dần rồi tắt hẳn thành vài đốm sáng nhỏ. Một chú Tôm Tít mini đeo kính bảo hộ đứng góc phải chỉ que vào điểm vết nứt tắt. |
| b10 | 01:18.9–01:28.5 (9.5s) | L42 | Quân đội Mỹ và các kỹ sư hàng không vũ trụ hiện đang nghiên cứu cấu trúc chiếc càng của Tôm Tít để chế tạo thế hệ áo giáp chống đạn và vỏ máy bay siêu nhẹ tiếp theo cho nhân loại! | **ÁO GIÁP** · công nghệ quân sự & vũ trụ · R/380 · [0.5, 0.5] | BÊN TRÁI một người lính mặc áo giáp chống đạn màu xanh rêu có họa tiết sợi xoắn giống càng tôm, viên đạn bẹp dí rơi xuống trước ngực. BÊN PHẢI một kỹ sư áo blouse trắng đội mũ bảo hộ đang lắp một tấm vỏ máy bay nhẹ như lông vũ lên mô hình máy bay. Ở GIỮA trên bục cao chú Tôm Tít đeo kính gọng tròn, khoanh càng làm cố vấn tự hào, hai người cùng ngước nhìn nó ngưỡng mộ. |
| b11 | 01:28.5–01:39.3 (10.9s) | L62 | Mà cái hay nhất là gì biết không? Đôi búa ấy chẳng bao giờ phải đem đi sửa! Cứ mỗi lần lột xác, Tôm Tít lại được thay luôn một cặp búa mới tinh, cứ như võ sĩ được tài trợ đôi găng mới sau mỗi mùa giải vậy! | **BÚA MỚI** · thay sau mỗi lần lột xác · L/380 · [0.5, 0.45] | Chú Tôm Tít mai xanh ngọc vui sướng đứng giữa, hai càng búa mới tinh sáng bóng lấp lánh có tia sao. BÊN TRÁI dưới đất là đôi càng búa cũ sứt mẻ, mòn vẹt, dán băng keo, bị vứt vào thùng rác nhỏ. BÊN PHẢI một chú cua quản lý đeo kính đen trao tặng một hộp quà mở nắp đựng đôi găng đỏ mới, kèm pháo giấy nhiều màu tung bay như lễ trao giải. |
| b12 | 01:39.3–01:42.7 (3.4s) | L63 | Nhưng cái giá của món quà đó thì... lát nữa bạn sẽ biết! |  | Chú Tôm Tít mai xanh ngọc đang hớn hở ôm hộp quà đựng đôi càng búa mới, hoàn toàn không để ý. Phía sau lưng nó, trên vách đá, một chiếc đồng hồ cát lớn đang chảy cát, và từ bóng tối góc phải một con cá mú to xám lấp ló hé mắt rình mò với nụ cười gian. Không khí hài hước nhưng có chút báo trước điềm chẳng lành, có một dấu chấm hỏi cam nhỏ. |

### scene04 · GÓT CHÂN A-SIN — MÙA LỘT XÁC MỀM NHƯ THẠCH · 80.2s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:10.4 (10.4s) | L43 | Nghe đến đây, bạn hẳn đang nghĩ Tôm Tít chính là vị vua bất khả chiến bại của rạn san hô, không sợ trời không sợ đất đúng không? Nhưng tạo hóa luôn rất thích trêu đùa những kẻ mạnh! |  | Chú Tôm Tít đội vương miện vàng, khoác áo choàng đỏ, ngồi vắt chân trên ngai vàng làm từ san hô hồng giữa rạn san hô, các loài cá nhỏ cúi đầu phục tùng. Phía trên góc phải, một bàn tay khổng lồ lấp lánh thò ra từ đám mây (đấng tạo hóa) đang cầm chiếc lông vũ cù nhẹ vào đầu Tôm Tít với vẻ tinh nghịch, Tôm Tít chưa hay biết gì. |
| b02 | 00:10.4–00:15.6 (5.3s) | L11 | Võ sĩ Mike Tyson đại dương này có một điểm yếu chí mạng khiến nó phải ôm hận suốt đời: Mùa lột xác! | **LỘT XÁC** · điểm yếu chí mạng · L/380 · [0.5, 0.55] | _(nội dung ảnh)_ Lột xác: vỏ cũ rỗng, thân + càng mới mềm như thạch, khóc |
| b03 | 00:15.6–00:24.2 (8.6s) | L44 | Giống như loài tôm cua, để lớn lên, Tôm Tít bắt buộc phải rũ bỏ toàn bộ lớp vỏ cứng bên ngoài, bao gồm cả đôi càng búa thần thánh của mình. Và bạn đoán xem điều gì xảy |  | Chú Tôm Tít đang chui ra khỏi lớp vỏ cũ cứng xanh ngọc từ phía sau như cởi một bộ đồ bó sát, cơ thể mới bên trong màu nhạt hơn ướt át. Đôi càng búa cũ rỗng đang tuột khỏi càng mới như tháo đôi găng tay đấm bốc. Biểu cảm vừa gắng sức vừa ngượng ngùng, vài giọt mồ hôi. |
| b04 | 00:24.2–00:30.5 (6.3s) | L28 | ra? Ngay sau khi lột xác, toàn bộ cơ thể lẫn đôi càng của nó mềm nhũn ra như một miếng thạch dừa hay bánh flan mới ra lò! | **MỀM NHƯ BƠ** · như bánh flan thạch dừa · R/400 · [0.5, 0.55] | _(nội dung ảnh)_ Tôm mềm như bánh flan trên đĩa, vỏ cũ bên cạnh |
| b05 | 00:30.5–00:37.7 (7.2s) | L29 | Kẻ từng đấm nứt kính bể cá giờ đây mềm yếu đến mức một con cá nhỏ hay một chú ốc sên bò qua cũng có thể xơi tái nó ngon lành! | **SỢ ỐC SÊN** · kẻ thù đáng sợ nhất · L/420 · [0.65, 0.55] | Chú Tôm Tít mềm oặt đang co rúm người toát mồ hôi hột sợ hãi ở một góc rạn san hô, đối diện là một chú ốc sên nhỏ xíu đang chậm rãi bò tới với nụ cười tinh quái, có dải chất nhầy lấp lánh phía sau, biểu cảm tương phản cực kỳ buồn cười. |
| b06 | 00:37.7–00:44.8 (7.1s) | L12 | Trong suốt vài tuần chờ lớp vỏ mới cứng lại, gã giang hồ này phải trốn chui trốn lủi tận đáy hang sâu, nhịn đói và run rẩy sợ hãi! | **TRỐN HANG** · nhịn đói & run rẩy · R/380 · [0.5, 0.55] | _(nội dung ảnh)_ Tôm mềm trốn sâu trong hang tối run rẩy; ốc sên + cá nhỏ bò ngang ngoài cửa hang |
| b07 | 00:44.8–00:52.5 (7.8s) | L46 | Điều hài hước nhất là nghệ thuật dọa ma của nó trong giai đoạn này! Nếu chẳng may có kẻ thù mò vào miệng hang, Tôm Tít sẽ lập tức phùng mang trợn mắt, | **DỌA MA** · nghệ thuật dọa ma · L/380 · [0.45, 0.45] | BÊN TRÁI một con cá mú to xám với hàm răng nhọn đang tò mò ló đầu vào miệng hang đá. BÊN PHẢI trong hang tối, chú Tôm Tít mềm oặt màu nhạt đang phùng má phồng mang to tròn, hai mắt lồi trợn to hết cỡ với các đường gân đỏ, cố tỏ ra hung dữ, nhưng vài giọt mồ hôi lạnh lộ rõ. |
| b08 | 00:52.5–00:58.6 (6.0s) | L13 | giương đôi càng mềm oặt ra đe dọa giống như đang nói: Nhìn càng tao đây này, bước vào là nát người đấy nhé! | **CÀNG MỀM** · giương càng đe dọa · R/420 · [0.6, 0.5] | _(nội dung ảnh)_ Tôm mềm dọa ma ở cửa hang: phùng mang, giương càng mềm như mì, cá săn mồi tiến tới |
| b09 | 00:58.6–01:01.6 (3.0s) | L45 | Nhưng thực chất đó hoàn toàn là một đòn nghi binh trắng trợn. | **NGHI BINH** · đòn nghi binh trắng trợn · L/380 · [0.5, 0.55] | Cảnh hài hước kiểu so sánh thật - giả: trên vách hang đá là một CÁI BÓNG đen khổng lồ đáng sợ hình con quái vật càng to sừng sững do đèn chiếu ngược lên. Nhưng ở dưới đất, kẻ tạo ra cái bóng chỉ là chú Tôm Tít mềm oặt nhỏ xíu đang kiễng chân, giương hai càng mềm rũ như sợi mì, mồ hôi chảy ròng ròng, mặt cố làm dữ nhưng chân run lẩy bẩy. |
| b10 | 01:01.6–01:06.6 (5.0s) | L47 | Nếu kẻ thù liều lĩnh xông vào, chiếc càng mềm của nó chạm nhẹ vào đá cũng đau thấu trời xanh! | **ĐAU ĐỚN** · càng mềm chạm đá · R/400 · [0.5, 0.55] | Chú Tôm Tít mềm oặt vừa vung chiếc càng mềm chạm nhẹ vào một hòn đá nhỏ, chiếc càng mềm cong gập lại như cọng mì. Tôm Tít nhảy dựng lên, ôm càng, mặt méo xệch đau đớn, nước mắt phun ra như vòi, nhiều ngôi sao và tia đau đớn bay quanh. Hòn đá nhỏ không hề hấn gì. Con cá mú ngoài hang há hốc ngạc nhiên. |
| b11 | 01:06.6–01:13.2 (6.6s) | L48 | Ngoài ra, gã này còn là nỗi ác mộng kinh hoàng của những người chơi cá cảnh biển: lỡ mua nhầm một chú tôm tít về thả vào bể, | **ÁC MỘNG** · người nuôi cá cảnh · R/380 · [0.7, 0.45] | Một người chơi cá cảnh mặc áo thun vui vẻ huýt sáo, nghiêng túi ni lông thả một chú Tôm Tít nhỏ vào bể cá cảnh biển rất đẹp với san hô, cá hề, cua, tôm và ốc đắt tiền đang bơi. Chú Tôm Tít đang rơi vào bể quay đầu liếc gian xảo nhìn đám cua ốc, khóe miệng nhếch cười nham hiểm, hai càng xoa vào nhau. Ánh trăng ngoài cửa sổ báo hiệu đêm xuống. |
| b12 | 01:13.2–01:20.2 (7.0s) | L30 | sáng hôm sau bạn sẽ thấy toàn bộ tôm, cua, ốc đắt tiền đã bị đấm vỡ nát, và bể kính thì nứt một vệt dài sẵn sàng vỡ tung tóe ra sàn nhà! | **VỠ BỂ** · bể nứt tung tóe · L/420 · [0.45, 0.5] | Trong một bể cá cảnh biển, mặt kính trước bị nứt toác một đường dài nước rò rỉ xịt ra ngoài sàn, bên trong bể vỏ sò vỏ cua đắt tiền vỡ nát trôi nổi, chú Tôm Tít đứng oai phong giơ hai càng búa đắc thắng, bên ngoài bể người chủ ôm đầu mặt cắt không còn giọt máu la hét kinh hoàng. |

### scene05 · VỤ ÁN THỦY CUNG BỂ NÁT & ĐÔI MẮT THẦN 16 MÀU · 103.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:05.6 (5.6s) | L49 | Những giai thoại về sức mạnh của Tôm Tít hoàn toàn không phải lời đồn thổi trên bàn nhậu! |  | BÊN TRÁI hai ông chú ngồi bàn nhậu nhỏ có đĩa mồi, một ông dang rộng hai tay kể chuyện phóng đại, bong bóng suy nghĩ phía trên vẽ cảnh con tôm nhỏ đấm vỡ bể kính, ông kia cười ngờ vực xua tay. BÊN PHẢI một cuốn hồ sơ tài liệu khoa học mở ra có ảnh dán (vẽ) chú Tôm Tít và bể kính nứt, được đóng một dấu tick xanh lá to xác nhận là sự thật. Không có chữ. |
| b02 | 00:05.6–00:16.1 (10.6s) | L50 | Vào tháng 4 năm 1998, tại một thủy cung nổi tiếng ở hạt Norfolk nước Anh, một chú tôm tít dài vỏn vẹn 10cm được đặt tên là Tyson đã làm nên một vụ bê bối chấn động! | **NĂM 1998** · thủy cung Norfolk · L/380 · [0.35, 0.45]<br>**10 cm** · chú tôm Tyson · R/420 · [0.65, 0.5] | BÊN TRÁI một tòa nhà thủy cung kiểu Anh cổ điển bằng gạch đỏ với mái vòm, lá cờ Anh nhỏ bay trên nóc, một chiếc xe buýt hai tầng màu đỏ đỗ phía trước, bầu trời mưa phùn xám nhẹ. BÊN PHẢI một khung tròn phóng to bên trong bể kính: chú Tôm Tít nhỏ xíu đeo đôi găng đấm bốc đỏ, bên cạnh một chiếc thước kẻ vàng (không số) cho thấy nó chỉ nhỏ bằng bàn tay, mặt hầm hố. |
| b03 | 00:16.1–00:23.3 (7.2s) | L14 | Có vẻ như bực mình vì tấm gương phản chiếu chính mình trên vách bể, chú ta đã tung ra một cú đấm thép thẳng vào tấm kính dày hơn 6mm! | **> 6 mm** · kính cường lực · R/400 · [0.65, 0.45] | _(nội dung ảnh)_ Tôm "Tyson" 10cm trong bể đấm vào hình phản chiếu, kính nứt, chuông báo động, nhân viên xách xô |
| b04 | 00:23.3–00:33.4 (10.1s) | L51 | Kết quả là mặt kính nứt đôi thành hình mạng nhện, nước biển bắt đầu phun ra xối xả và toàn bộ nhân viên thủy cung phải kích hoạt còi báo động khẩn cấp để sơ tán du khách và cứu vớt các loài sinh vật khác! | **SƠ TÁN** · báo động khẩn cấp · L/420 · [0.55, 0.5] | Toàn cảnh sảnh thủy cung hỗn loạn: bức tường bể kính lớn nứt hình mạng nhện, nước biển phun thành nhiều tia xối xả ra sàn. Đèn còi báo động đỏ quay trên trần phát vòng sáng. Du khách gồm gia đình có trẻ em hoảng hốt bỏ chạy ra cửa thoát hiểm. Hai nhân viên áo xanh dùng vợt và xô cứu những con cá và rùa biển đang dãy dụa. Góc bể chú Tôm Tít nhỏ khoanh càng vô tội huýt sáo. |
| b05 | 00:33.4–00:46.3 (12.9s) | L52 | Từ đó, các viện hải dương học trên khắp thế giới ban hành một luật bất thành văn: Tuyệt đối không bao giờ nuôi Tôm Tít trong bể kính thủy tinh thông thường, mà bắt buộc phải dùng bể nhựa acrylic chống đạn siêu dày! | **ACRYLIC** · chống đạn siêu dày · R/380 · [0.5, 0.5] | Chia đôi: BÊN TRÁI một bể kính thủy tinh mỏng thông thường nứt vỡ, bị gạch chéo bằng dấu X đỏ to vẽ tay. BÊN PHẢI một bể nhựa acrylic trong suốt với vách cực kỳ dày như bức tường hầm ngân hàng, có bu lông to ở góc, được đánh dấu tick xanh lá. Bên trong bể acrylic chú Tôm Tít phụng phịu đấm thử vào vách nhưng chỉ nảy ngược lại, mặt hờn dỗi. |
| b06 | 00:46.3–00:57.8 (11.5s) | L15 | Bên cạnh cú đấm thần sầu, Tôm Tít còn sở hữu đôi mắt kỳ dị bậc nhất hành tinh! Con người chúng ta chỉ có 3 loại tế bào cảm thụ màu sắc là đỏ, lục và lam. Nhưng Tôm Tít sở hữu tới 16 loại thụ thể màu sắc khác nhau! | **3 MÀU** · con người · L/400 · [0.45, 0.35] | _(nội dung ảnh)_ So sánh mắt người RGB vs mắt tôm 16 màu + UV + phân cực tròn |
| b07 | 00:57.8–01:06.7 (8.9s) | L53 | Nó không chỉ nhìn thấy dải màu rực rỡ gấp năm lần chúng ta, mà còn nhìn thấu cả tia cực tím UV và là sinh vật duy nhất trên Trái Đất nhìn được ánh sáng phân cực tròn! | **x5 LẦN** · rực rỡ hơn người · R/360 · [0.65, 0.45]<br>**CỰC TÍM UV** · ánh sáng phân cực · L/420 · [0.35, 0.5] | Chú Tôm Tít đứng trên bục cao nhất có đôi mắt lồi phát sáng cầu vồng, nhìn lên bầu trời thấy những dải sáng xoắn ốc lò xo (phân cực tròn) và tia tím huỳnh quang (UV) lấp lánh rực rỡ. Bên dưới bục, một con người, một con mèo và một con chim đại bàng đang ngó cùng hướng nhưng chỉ thấy khoảng trống, mặt ngơ ngác với dấu chấm hỏi. |
| b08 | 01:06.7–01:13.6 (6.9s) | L54 | Mỗi con mắt của nó có thể chuyển động độc lập 360° và tự đo khoảng cách không gian 3D mà không cần đến mắt còn lại. | **360°** · xoay độc lập & 3D · R/380 · [0.7, 0.45] | Cận cảnh đầu chú Tôm Tít: con mắt bên trái xoay nhìn thẳng lên trên, con mắt bên phải xoay nhìn ngược ra phía sau, mỗi con mắt có một vòng tròn mũi tên xoay tròn đầy đủ màu cam quanh nó. Từ con mắt phải phóng ra một lưới hình hộp 3D phối cảnh màu xanh dương chạm tới một con cá nhỏ ở xa, như máy đo khoảng cách. Biểu cảm vui nhộn lác mắt. |
| b09 | 01:13.6–01:24.7 (11.1s) | L16 | Các nhà khoa học hiện đang sao chép cấu trúc mắt của Tôm Tít để chế tạo các loại cảm biến y tế siêu nhạy, có khả năng phát hiện sớm các tế bào ung thư trong cơ thể người từ những giai đoạn đầu tiên! | **Y HỌC** · phát hiện sớm ung thư · L/400 · [0.55, 0.45] | _(nội dung ảnh)_ Bác sĩ dùng máy quét mô phỏng mắt tôm phát hiện tế bào ung thư |
| b10 | 01:24.7–01:32.8 (8.1s) | L64 | Chưa hết đâu! Tôm Tít còn dùng chính ánh sáng phân cực để nhắn tin bí mật cho nhau, trên cơ thể có những mảng phát tín hiệu mà kẻ thù nhìn vào chẳng thấy gì. | **PHÂN CỰC** · tin nhắn bí mật · L/380 · [0.33, 0.45] | BÊN TRÁI và Ở GIỮA hai chú Tôm Tít mai xanh ngọc đứng đối diện nhau, trên thân mỗi con có vài mảng phát sáng lấp lánh xoắn ốc cầu vồng, giữa chúng là các dải sóng ánh sáng xoắn lò xo màu tím-xanh bay qua lại như đang nhắn tin, cả hai cười khúc khích che miệng bằng càng. BÊN PHẢI một con cá săn mồi to nhìn vào cùng chỗ đó nhưng trong mắt nó chỉ thấy hai con tôm bình thường, mặt ngơ ngác với dấu chấm hỏi. |
| b11 | 01:32.8–01:40.1 (7.3s) | L65 | Và gã giang hồ cục súc này hóa ra lại là một người chồng chung thủy: có loài sống thành cặp trong cùng một hang tới 20 năm! | **20 NĂM** · chung một hang · R/400 · [0.5, 0.55] | Bên trong một căn hang cát ấm cúng dưới đáy biển được trang trí như ngôi nhà nhỏ: một cặp vợ chồng Tôm Tít mai xanh ngọc ngồi cạnh nhau, con chồng đeo nơ, con vợ đội nơ hồng, cùng nhìn nhau trìu mến, trái tim đỏ nhỏ bay lên. Trên vách hang treo khung ảnh cưới vẽ hai con tôm và một dãy nhiều vạch khắc đếm thời gian dài trên đá (không số). Trước hang có hàng rào vỏ sò nhỏ. |
| b12 | 01:40.1–01:43.4 (3.3s) | L66 | Ra ngoài thì đấm nứt kính, về nhà thì ngoan như mèo! |  | Chia đôi hài hước: BÊN TRÁI chú Tôm Tít mai xanh ngọc đeo găng đỏ mặt hầm hố đấm nứt mặt kính bể cá hình mạng nhện, mảnh kính bắn ra. BÊN PHẢI cũng chính chú Tôm Tít ấy ở nhà trong hang, đeo tạp dề hồng, ngoan ngoãn rửa chén vỏ sò, mắt to long lanh cười hiền như mèo con, bên cạnh tôm vợ khoanh càng hài lòng. Một đường chia đôi vẽ tay ở giữa. |

### scene06 · BÀI HỌC SINH TỒN TỪ TÔM TÍT · 54.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.4 (9.4s) | L55 | Từ những rạn san hô nhiệt đới nông cạn cho đến những đáy bùn tăm tối ngoài đại dương, Tôm Tít đã dạy cho chúng ta một bài học sinh tồn vô cùng sâu sắc của mẹ thiên nhiên: |  | Dải toàn cảnh ngang: BÊN TRÁI rạn san hô nhiệt đới nông sáng rực đầy màu sắc với ánh nắng xuyên mặt nước, chuyển dần sang BÊN PHẢI là đáy bùn tối xanh thẫm sâu thẳm. Ở GIỮA chú Tôm Tít đeo kính gọng tròn như thầy giáo, cầm que chỉ, đứng cạnh một tấm bảng đen nhỏ (bảng trống, không chữ), mỉm cười hiền từ. |
| b02 | 00:09.4–00:14.5 (5.1s) | L56 | Sở hữu sức mạnh vô song như cú đấm viên đạn không có nghĩa là bạn luôn luôn bất khả chiến bại. | **BÀI HỌC** · không bất khả chiến bại · L/380 · [0.5, 0.5] | Chú Tôm Tít võ sĩ đeo găng đỏ và đai vô địch vàng đứng tạo dáng cơ bắp oai vệ phía trước. Nhưng cái bóng in trên nền phía sau nó lại là hình một chú tôm mềm oặt như thạch đang run rẩy khóc. Tương phản hai mặt của kẻ mạnh, không khí suy ngẫm. |
| b03 | 00:14.5–00:22.9 (8.4s) | L57 | Đỉnh cao thực sự của kẻ sinh tồn không phải là lúc khoe khoang sức mạnh, mà là biết nhẫn nhịn, thu mình trốn kỹ trong hang tối khi cơ thể đang lột xác yếu mềm nhất, | **KHIÊM TỐN** · nhẫn nhịn chờ thời · R/380 · [0.5, 0.55] | Trong hang đá tối ấm cúng, chú Tôm Tít mềm màu nhạt ngồi khoanh chân thiền định bình thản, mắt nhắm, bên cạnh là một chiếc đồng hồ cát đang chảy và lớp vỏ cũ rỗng treo trên móc như bộ áo. Ngoài miệng hang lũ cá săn mồi bơi qua nhưng không thấy nó. Không khí yên tĩnh, kiên nhẫn. |
| b04 | 00:22.9–00:27.5 (4.6s) | L17 | kiên nhẫn chờ đợi lớp áo giáp mới cứng cáp hơn rồi mới bước ra làm chủ cuộc chơi! |  | _(nội dung ảnh)_ Tôm bước ra khỏi hang với giáp mới cứng cáp, tự tin, rạn san hô nắng |
| b05 | 00:27.5–00:37.3 (9.8s) | L58 | Bạn ấn tượng nhất với điều gì ở gã võ sĩ đại dương này: Cú đấm bọt khí nóng ngang Mặt Trời hay đôi mắt nhìn thấu cả tế bào ung thư? Hãy để lại bình luận cho mình biết nhé! | **BÌNH LUẬN** · chia sẻ cảm nghĩ · R/400 · [0.5, 0.5] | Bố cục bình chọn: hai khung tròn lớn hai bên. KHUNG TRÁI viền cam: cú đấm càng búa tạo bọt khí nổ thành quả cầu lửa như Mặt Trời tí hon. KHUNG PHẢI viền tím: đôi mắt lồi cầu vồng của Tôm Tít phát tia sáng quét lên các tế bào ung thư màu tím đang phát sáng. Ở GIỮA dưới hai khung, chú Tôm Tít gãi đầu bối rối, hai càng chỉ hai bên, dấu chấm hỏi trên đầu. |
| b06 | 00:37.3–00:49.8 (12.5s) | L18 | Ở tập tiếp theo, chúng ta sẽ rời xa đáy biển sâu để đến với một sinh vật kỳ dị không kém: một loài cá nhưng lại biết trèo cây, biết nhảy nhót trên bùn và có thể thở bằng da suốt nhiều giờ trên cạn! Bạn có đoán được đó là ai không? | **TẬP 8** · Cá Thòi Lòi biết trèo cây · L/380 · [0.55, 0.5] | _(nội dung ảnh)_ Cá Thòi Lòi ngồi trên cành đước vẫy vây (teaser tập 8) |
| b07 | 00:49.8–00:54.7 (4.9s) | L59 | Đừng quên bấm Đăng ký kênh Vẽ Chuyện Hoang Dã và bật Chuông thông báo để không bỏ lỡ tập tiếp theo nhé! | **ĐĂNG KÝ** · Vẽ Chuyện Hoang Dã · R/380 · [0.5, 0.5] | Chú Tôm Tít vui vẻ đeo găng đỏ, một càng đấm nhẹ vào một nút tròn đỏ lớn (biểu tượng play hình tam giác trắng), càng kia vẫy chào tạm biệt, bên cạnh là một chiếc chuông vàng đang rung leng keng với các đường rung. Vài ngôi sao lấp lánh, nụ cười tươi nháy mắt. |

## 5. Phân cảnh Shorts — từng beat

Banner: **CÚ ĐẤM NÓNG BẰNG MẶT TRỜI / ĐẤM VỠ CẢ BỂ KÍNH?!** · giọng 45.0s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Một cú đấm dưới nước mạnh ngang một viên đạn súng trường, | **1 VIÊN ĐẠN** · súng trường dưới nước · L/800 · [0.65, 0.5] |
| s02 | 00:03.0 | S05 | sinh ra nhiệt độ 4.700°C gần bằng bề mặt Mặt Trời! | **4.700°C** · nóng ngang Mặt Trời · R/700 · [0.55, 0.45] |
| s03 | 00:07.5 | S02 | Kẻ sở hữu siêu năng lực điên rồ đó chính là Tôm Tít, võ sĩ Mike Tyson khét tiếng của đại | **TYSON** · võ sĩ đại dương · L/750 · [0.5, 0.45] |
| s04 | 00:12.3 | S03 | dương! Với đôi càng búa tí hon, nó phóng đòn với gia tốc 10.400g, đập vỡ nát mai cua, vỏ ốc xà | **10.400 g** · gia tốc thần sầu · R/720 · [0.6, 0.45] |
| s05 | 00:18.4 | S04 | cừ và thậm chí từng đấm nứt toác cả mặt kính bể cá dày cộp của một thủy cung ở nước | **NỨT KÍNH** · thủy cung nước Anh · L/780 · [0.5, 0.5] |
| s06 | 00:22.1 | S11 | Anh! Cú vung càng nhanh đến mức làm sôi nước biển, tạo ra vụ nổ bọt khí xâm thực nướng chín con mồi trong nháy | **SÔI NƯỚC** · nướng chín con mồi · R/740 · [0.55, 0.45] |
| s07 | 00:27.6 | S06 | mắt! Thế nhưng, cứ mỗi mùa lột xác, gã võ sĩ bất khả chiến bại này lại biến thành một miếng thạch bơ mềm nhũn, | **MỀM NHƯ THẠCH** · mùa lột xác · L/750 · [0.5, 0.55] |
| s08 | 00:33.5 | S07 | phải trốn chui trốn lủi sợ cả một con ốc sên bò ngang qua! | **SỢ ỐC SÊN** · trốn trong hang sâu · R/780 · [0.65, 0.55] |
| s09 | 00:37.2 | S08 | Bí mật về đôi mắt 16 dải | **16 MÀU** · thị giác siêu cấp · L/720 · [0.55, 0.35] |
| s10 | 00:39.0 | S09 | màu giúp phát hiện ung thư của gã | **Y HỌC** · tầm soát ung thư · R/750 · [0.55, 0.5] |
| s11 | 00:40.4 | S10 | này đã có ở video dài bên dưới. Bấm xem ngay màn đại chiến siêu hài hước này nhé! | **XEM NGAY** · Tập 7 bản đầy đủ · R/750 · [0.5, 0.5] |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard, nét mực đen đậm, màu phẳng tươi sáng, nền trắng tinh hoàn toàn, không chữ, không số, không logo). Lời thoại: "Đôi mắt lồi đảo liên tục như hai chiếc ra-đa của người ngoài hành tinh". Bố cục: Cận cảnh chú Tôm Tít hoạt hình đầy màu sắc sặc sỡ, hai con mắt to tròn lồi hẳn ra ngoài đang xoay theo hai hướng khác nhau, trên mỗi con mắt có hình vẽ chiếc chảo vệ tinh ra-đa công nghệ cao đang phát ra các vòng sóng vô tuyến quét không gian, biểu cảm cực kỳ tò mò và hài hước.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard, nét mực đen đậm, màu phẳng tươi sáng, nền trắng tinh hoàn toàn, không chữ, không số, không logo). Lời thoại: "Một gã tí hon dưới đáy cát nhưng lại mang tâm hồn của một tay giang hồ cục súc khét tiếng". Bố cục: Chú Tôm Tít hoạt hình nhỏ xíu đứng trên bãi cát trắng, mặc chiếc áo khoác da màu đen phong cách giang hồ cực ngầu, đeo kính râm đen bóng, miệng ngậm một que tăm, hai tay chống hông biểu cảm ngang tàng thách thức, phía sau có vài vỏ sò nhỏ đang co rúm sợ hãi.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard, nét mực đen đậm, màu phẳng tươi sáng, nền trắng tinh hoàn toàn, không chữ, không số, không logo). Lời thoại: "Sức mạnh tấn công ATK: chạm nóc chín ngàn chín trăm chín mươi chín điểm! Một cú vung càng của nó tạo ra lực va chạm lên tới một ngàn năm trăm Newton". Bố cục: Nửa trái là Tôm Tít võ sĩ cơ bắp vung chiếc càng búa bọc lửa đỏ cam giáng một đòn cực mạnh xuống. Nửa phải là một quả tạ sắt khổng lồ bị đập lõm sâu biến dạng bẹp dúm, xung quanh tỏa ra các tia sét màu vàng và sóng xung kích bùng nổ dữ dội.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard, nét mực đen đậm, màu phẳng tươi sáng, nền trắng tinh hoàn toàn, không chữ, không số, không logo). Lời thoại: "Nó chỉ mất chưa đầy ba phần ngàn giây để tung ra cú đấm, đạt gia tốc mười ngàn bốn trăm g, nghĩa là còn nhanh hơn cả gia tốc của viên đạn hai mươi hai ly". Bố cục: Nửa trái một chiếc đồng hồ bấm giờ siêu tốc kim đang nhích một vạch cực nhỏ. Nửa phải là đường đua tốc độ: một viên đạn đồng sáng loáng đang bay xé gió bốc khói phía sau, nhưng phía trước nó là chiếc càng búa của Tôm Tít đang phóng vút vượt lên dẫn trước với những vệt tốc độ màu vàng cam.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard, nét mực đen đậm, màu phẳng tươi sáng, nền trắng tinh hoàn toàn, không chữ, không số, không logo). Lời thoại: "Trong một cái chớp mắt của bạn, Tôm Tít đã kịp đấm con mồi tới ba mươi lần liên tiếp". Bố cục: Chia đôi so sánh hài hước: Bên TRÁI là khuôn mặt một người hoạt hình đang từ từ chớp mắt lại, mí mắt mới khép một nửa. Bên PHẢI là Tôm Tít đang biến thành một cơn lốc cú đấm ảo diệu, hàng chục chiếc càng bóng ma tung ra liên hoàn như mưa sao băng, con cua đối diện chóng mặt mắt quay mòng mòng đầy sao bay quanh đầu.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard, nét mực đen đậm, màu phẳng tươi sáng, nền trắng tinh hoàn toàn, không chữ, không số, không logo). Lời thoại: "Nếu cánh tay của bạn cũng có thể vung nhanh như càng tôm tít, bạn hoàn toàn có thể ném một quả bóng chày bay thẳng vào quỹ đạo Trái Đất mà không cần tên lửa đẩy". Bố cục: Chú Tôm Tít hoạt hình mặc trang phục cầu thủ bóng chày màu đỏ trắng, vung chiếc càng búa ném một quả bóng chày bay vút xé toạc bầu khí quyển bay thẳng vào không gian vũ trụ quay quanh Trái Đất bên cạnh các vệ tinh nhân tạo, có vệt lửa và các vì sao lấp lánh.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard, nét mực đen đậm, màu phẳng tươi sáng, nền trắng tinh hoàn toàn, không chữ, không số, không logo). Lời thoại: "Ngay khoảnh khắc tiếp theo, khi bọt khí này sụp đổ dưới áp suất nước xung quanh, nó tạo ra một vụ nổ sóng xung kích khủng khiếp, sinh ra nhiệt độ cục bộ lên tới bốn ngàn bảy trăm độ C, gần bằng bề mặt của Mặt Trời!". Bố cục: Bố cục 16:9 chia đôi đối chiếu kịch tính: Bên trái là vụ nổ bọt khí nước phát sáng chói lòa tỏa nhiệt đỏ rực dưới nước, bên phải là vầng Mặt Trời rực lửa với các quầng lửa plasma cuồn cuộn, ở giữa có một cột nhiệt kế đo nhiệt độ kịch trần bốc khói dữ dội.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard, nét mực đen đậm, màu phẳng tươi sáng, nền trắng tinh hoàn toàn, không chữ, không số, không logo). Lời thoại: "Vụ nổ này thậm chí còn phát ra một tia sáng le lói mà giới khoa học gọi là hiện tượng phát quang do âm thanh Sonoluminescence!". Bố cục: Dưới đáy biển, một bọt khí cực nhỏ phát sáng lấp lánh như một ngôi sao nhỏ phát ra tia sáng xanh lam rực rỡ, xung quanh là các vòng sóng âm thanh tròn đồng tâm lan tỏa, bên cạnh có một nhà khoa học hoạt hình đeo kính lúp soi vào và kinh ngạc tròn mắt há hốc mồm.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard, nét mực đen đậm, màu phẳng tươi sáng, nền trắng tinh hoàn toàn, không chữ, không số, không logo). Lời thoại: "Dù nó có đấm trượt mục tiêu thì sóng xung kích của bọt khí sụp đổ vẫn biến con mồi thành đĩa thức ăn nướng chín trong nháy mắt!". Bố cục: Bố cục 16:9 hài hước: Chú Tôm Tít vung càng đấm trượt sang một bên, nhưng luồng sóng xung kích bốc hơi nóng làm một con cua đối diện biến thành màu đỏ cam chín thơm phức, trên mai cua bốc khói nghi ngút và có một lát chanh bên cạnh như đĩa hải sản nướng, mắt con cua quay tròn chóng mặt ngơ ngác.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard, nét mực đen đậm, màu phẳng tươi sáng, nền trắng tinh hoàn toàn, không chữ, không số, không logo). Lời thoại: "Kẻ từng đấm nứt kính bể cá giờ đây mềm yếu đến mức một con cá nhỏ hay một chú ốc sên bò qua cũng có thể xơi tái nó ngon lành!". Bố cục: Chú Tôm Tít mềm oặt đang co rúm người toát mồ hôi hột sợ hãi ở một góc rạn san hô, đối diện là một chú ốc sên nhỏ xíu đang chậm rãi bò tới với nụ cười tinh quái, có dải chất nhầy lấp lánh phía sau, biểu cảm tương phản cực kỳ buồn cười.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard, nét mực đen đậm, màu phẳng tươi sáng, nền trắng tinh hoàn toàn, không chữ, không số, không logo). Lời thoại: "Ngoài ra, gã này còn là nỗi ác mộng kinh hoàng của những người chơi cá cảnh biển: lỡ mua nhầm một chú tôm tít về thả vào bể, sáng hôm sau bạn sẽ thấy toàn bộ tôm, cua, ốc đắt tiền đã bị đấm vỡ nát, và bể kính thì nứt một vệt dài sẵn sàng vỡ tung tóe ra sàn nhà!". Bố cục: Trong một bể cá cảnh biển, mặt kính trước bị nứt toác một đường dài nước rò rỉ xịt ra ngoài sàn, bên trong bể vỏ sò vỏ cua đắt tiền vỡ nát trôi nổi, chú Tôm Tít đứng oai phong giơ hai càng búa đắc thắng, bên ngoài bể người chủ ôm đầu mặt cắt không còn giọt máu la hét kinh hoàng.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard, nét mực đen đậm, màu phẳng tươi sáng, nền trắng tinh hoàn toàn, không chữ, không số, không logo). Lời thoại: "Cua biển mai dày ư? Một đấm vỡ nát! Vỏ ốc xà cừ cứng như đá ư? Hai đấm thành bột vụn!". Bố cục: Chú Tôm Tít hoạt hình tung một cú đấm búa cực mạnh vào chính giữa chiếc mai của một con cua biển to lớn, chiếc mai cua dày cứng nứt toác thành nhiều mảnh vỡ vụn văng ra, bên cạnh là một chiếc vỏ ốc xà cừ bị đập nát thành bột trắng, các vệt sóng chấn động màu vàng cam nổ tung tóe, con cua mắt hoa đầu óc choáng váng.
```
</details>

<details><summary>L33</summary>

```text
Tạo hình ảnh (cảnh L33 của video YouTube về Tôm Tít). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoat hình hài hước cường điệu; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Tôm Tít (peacock mantis shrimp) hoạt hình, mai xanh ngọc lục bảo, râu đỏ cam, chân và đuôi có điểm màu cầu vồng, hai mắt to lồi trên cuống biểu cảm, hai càng búa (club) gập trước ngực như võ sĩ. NỘI DUNG CẢNH L33 (lời thoại: "Bất kỳ ai tò mò thò tay xuống hốc đá tóm thử gã võ sĩ này sẽ lập tức nhận ngay một cú đấm nhanh đến mức mắt thường không kịp chớp, đủ sức đập vỡ nát móng tay
```
</details>

<details><summary>L34</summary>

```text
Lời thoại: "Chỉ số phòng thủ DEF: 85 điểm! Càng của nó được bọc lớp giáp cấu trúc sợi nano chống nứt cực kỳ tinh xảo.". Bố cục: Ở GIỮA chú Tôm Tít giơ chiếc càng búa lên đỡ như khiên, mặt tự tin nháy mắt. Lớp vỏ càng có họa tiết các sợi đan xoắn lưới phát sáng xanh ngọc như áo giáp công nghệ. BÊN PHẢI một chiếc búa tạ sắt khổng lồ đang nện thẳng vào càng nhưng chính cán búa gãy đôi, đầu búa nứt vỡ văng mảnh. Càng tôm không một vết xước, có vài tia lấp lánh.
```
</details>

<details><summary>L35</summary>

```text
Lời thoại: "Một phi công lái máy bay tiêm kích chỉ cần chịu gia tốc 9g là máu đã dồn hết xuống chân và ngất lịm ngay trên bầu trời.". Bố cục: Một chiếc máy bay phản lực tiêm kích màu xám bạc đang ngoặt gắt trên trời với vệt khói trắng cong. Phóng to buồng lái kính trong suốt: phi công đội mũ bảo hiểm trắng, đeo mặt nạ dưỡng khí, mắt xoắn ốc ngất lịm đầu gục sang bên, má xệ xuống vì lực G. Vài mũi tên đỏ cong chỉ xuống chân phi công thể hiện máu dồn xuống. KHÔNG có Tôm Tít trong cảnh này.
```
</details>

<details><summary>L36</summary>

```text
Lời thoại: "Vậy mà đôi càng tí hon này lại phóng đi với gia tốc gấp hơn 1.000 lần giới hạn của con người!". Bố cục: Chia đôi hài hước: BÊN TRÁI nhỏ là phi công ngất xỉu nằm bẹp trên ghế lái. BÊN PHẢI lớn: chú Tôm Tít tí hon tỉnh bơ, một càng phóng đấm ra với các vệt siêu tốc dày đặc màu vàng cam và luồng sóng xé nước, tay kia cầm cốc trà sữa, mặt thản nhiên huýt sáo, không hề chóng mặt.
```
</details>

<details><summary>L37</summary>

```text
Lời thoại: "Cú đấm của Tôm Tít uy lực đến mức nó tạo ra một hiện tượng vật lý kỳ dị mang tên Cavitation, tức Bọt Khí Xâm Thực!". Bố cục: Cận cảnh dưới nước: chú Tôm Tít vừa tung cú đấm càng búa sang phải, ngay phía sau đầu càng xuất hiện một chuỗi bọt khí tròn trong suốt lấp lánh kỳ lạ đang hình thành trong vệt nước xoáy. Tôm Tít quay đầu nhìn các bọt khí với mắt tròn xoe kinh ngạc. Phía trên có vài dấu chấm than vẽ tay.
```
</details>

<details><summary>L38</summary>

```text
Lời thoại: "Áp suất nước phía sau chiếc càng sụt giảm đột ngột xuống mức gần như chân không, làm nước sôi ngay lập tức ở nhiệt độ phòng và sinh ra một bọt khí cực nhỏ!". Bố cục: Bố cục giải thích khoa học: Ở GIỮA chiếc càng búa đang vung sang phải cực nhanh để lại vệt nước. Ngay sau đuôi càng là một vùng trống xoáy tròn (vùng chân không) với nước đang sủi bọt sùng sục như nồi nước sôi. BÊN TRÁI một chiếc nhiệt kế màu xanh dương mát lạnh chỉ mức thấp (nhiệt độ phòng) có bông tuyết nhỏ, cạnh đó một bình áp suất có kim đồng hồ tụt về 0. Tương phản: nước sôi mà nhiệt kế vẫn mát.
```
</details>

<details><summary>L39</summary>

```text
Lời thoại: "Mỗi cú ra đòn của Tôm Tít thực chất là một đòn tấn công kép: đòn thứ nhất là cú đập của chiếc càng cứng, và đòn thứ hai là sóng xung kích từ vụ nổ nhiệt độ Mặt Trời!". Bố cục: Chia đôi thành hai khung tròn nối nhau bằng mũi tên cong cam: KHUNG TRÁI chiếc càng búa cứng đập trúng vỏ một con cua, tia va chạm vàng. KHUNG PHẢI ngay sau đó một bọt khí nổ tung thành quả cầu lửa nhỏ rực sáng như Mặt Trời tí hon, sóng xung kích vòng tròn hất văng con cua lần nữa, cua mắt xoắn. Chú Tôm Tít đứng giữa hai khung giơ hai càng hình chữ V chiến thắng.
```
</details>

<details><summary>L40</summary>

```text
Lời thoại: "Tại sao chiếc càng của Tôm Tít không bị vỡ vụn khi phải chịu hàng ngàn cú va chạm kinh hoàng như vậy?". Bố cục: Chú Tôm Tít ngồi trên đống vỏ ốc, vỏ cua và đá vụn vỡ nát chất cao như núi, nó giơ chiếc càng búa lên ngắm nghía bằng kính lúp với vẻ thắc mắc, trên đầu có dấu chấm hỏi cam to vẽ tay. Chiếc càng vẫn nhẵn bóng nguyên vẹn không một vết nứt, lấp lánh.
```
</details>

<details><summary>L41</summary>

```text
Lời thoại: "Khi một vết nứt nhỏ hình thành, nó không thể lan thẳng mà bị bẻ cong theo các rãnh xoắn, tự tiêu tán năng lượng va đập!". Bố cục: Sơ đồ khoa học vẽ tay mặt cắt lớp vỏ càng: nhiều lớp sợi mỏng xếp xoay dần như cầu thang xoắn ốc (màu xanh ngọc, cam, vàng xen kẽ). Một vết nứt màu đỏ hình tia sét đi vào từ mép trái, bị bẻ cong uốn lượn ngoằn ngoèo theo các lớp xoắn, càng vào sâu càng mảnh và mờ dần rồi tắt hẳn thành vài đốm sáng nhỏ. Một chú Tôm Tít mini đeo kính bảo hộ đứng góc phải chỉ que vào điểm vết nứt tắt.
```
</details>

<details><summary>L42</summary>

```text
Lời thoại: "Quân đội Mỹ và các kỹ sư hàng không vũ trụ hiện đang nghiên cứu cấu trúc chiếc càng của Tôm Tít để chế tạo thế hệ áo giáp chống đạn và vỏ máy bay siêu nhẹ tiếp theo cho nhân loại!". Bố cục: BÊN TRÁI một người lính mặc áo giáp chống đạn màu xanh rêu có họa tiết sợi xoắn giống càng tôm, viên đạn bẹp dí rơi xuống trước ngực. BÊN PHẢI một kỹ sư áo blouse trắng đội mũ bảo hộ đang lắp một tấm vỏ máy bay nhẹ như lông vũ lên mô hình máy bay. Ở GIỮA trên bục cao chú Tôm Tít đeo kính gọng tròn, khoanh càng làm cố vấn tự hào, hai người cùng ngước nhìn nó ngưỡng mộ.
```
</details>

<details><summary>L43</summary>

```text
Lời thoại: "Bạn hẳn đang nghĩ Tôm Tít chính là vị vua bất khả chiến bại của rạn san hô, không sợ trời không sợ đất đúng không? Nhưng tạo hóa luôn rất thích trêu đùa những kẻ mạnh!". Bố cục: Chú Tôm Tít đội vương miện vàng, khoác áo choàng đỏ, ngồi vắt chân trên ngai vàng làm từ san hô hồng giữa rạn san hô, các loài cá nhỏ cúi đầu phục tùng. Phía trên góc phải, một bàn tay khổng lồ lấp lánh thò ra từ đám mây (đấng tạo hóa) đang cầm chiếc lông vũ cù nhẹ vào đầu Tôm Tít với vẻ tinh nghịch, Tôm Tít chưa hay biết gì.
```
</details>

<details><summary>L44</summary>

```text
Lời thoại: "Để lớn lên, Tôm Tít bắt buộc phải rũ bỏ toàn bộ lớp vỏ cứng bên ngoài, bao gồm cả đôi càng búa thần thánh của mình.". Bố cục: Chú Tôm Tít đang chui ra khỏi lớp vỏ cũ cứng xanh ngọc từ phía sau như cởi một bộ đồ bó sát, cơ thể mới bên trong màu nhạt hơn ướt át. Đôi càng búa cũ rỗng đang tuột khỏi càng mới như tháo đôi găng tay đấm bốc. Biểu cảm vừa gắng sức vừa ngượng ngùng, vài giọt mồ hôi.
```
</details>

<details><summary>L45</summary>

```text
Lời thoại: "Nhưng thực chất đó hoàn toàn là một đòn nghi binh trắng trợn.". Bố cục: Cảnh hài hước kiểu so sánh thật - giả: trên vách hang đá là một CÁI BÓNG đen khổng lồ đáng sợ hình con quái vật càng to sừng sững do đèn chiếu ngược lên. Nhưng ở dưới đất, kẻ tạo ra cái bóng chỉ là chú Tôm Tít mềm oặt nhỏ xíu đang kiễng chân, giương hai càng mềm rũ như sợi mì, mồ hôi chảy ròng ròng, mặt cố làm dữ nhưng chân run lẩy bẩy.
```
</details>

<details><summary>L46</summary>

```text
Lời thoại: "Nếu chẳng may có kẻ thù mò vào miệng hang, Tôm Tít sẽ lập tức phùng mang trợn mắt,". Bố cục: BÊN TRÁI một con cá mú to xám với hàm răng nhọn đang tò mò ló đầu vào miệng hang đá. BÊN PHẢI trong hang tối, chú Tôm Tít mềm oặt màu nhạt đang phùng má phồng mang to tròn, hai mắt lồi trợn to hết cỡ với các đường gân đỏ, cố tỏ ra hung dữ, nhưng vài giọt mồ hôi lạnh lộ rõ.
```
</details>

<details><summary>L47</summary>

```text
Lời thoại: "Nếu kẻ thù liều lĩnh xông vào, chiếc càng mềm của nó chạm nhẹ vào đá cũng đau thấu trời xanh!". Bố cục: Chú Tôm Tít mềm oặt vừa vung chiếc càng mềm chạm nhẹ vào một hòn đá nhỏ, chiếc càng mềm cong gập lại như cọng mì. Tôm Tít nhảy dựng lên, ôm càng, mặt méo xệch đau đớn, nước mắt phun ra như vòi, nhiều ngôi sao và tia đau đớn bay quanh. Hòn đá nhỏ không hề hấn gì. Con cá mú ngoài hang há hốc ngạc nhiên.
```
</details>

<details><summary>L48</summary>

```text
Lời thoại: "Lỡ mua nhầm một chú tôm tít về thả vào bể". Bố cục: Một người chơi cá cảnh mặc áo thun vui vẻ huýt sáo, nghiêng túi ni lông thả một chú Tôm Tít nhỏ vào bể cá cảnh biển rất đẹp với san hô, cá hề, cua, tôm và ốc đắt tiền đang bơi. Chú Tôm Tít đang rơi vào bể quay đầu liếc gian xảo nhìn đám cua ốc, khóe miệng nhếch cười nham hiểm, hai càng xoa vào nhau. Ánh trăng ngoài cửa sổ báo hiệu đêm xuống.
```
</details>

<details><summary>L49</summary>

```text
Lời thoại: "Những giai thoại về sức mạnh của Tôm Tít hoàn toàn không phải lời đồn thổi trên bàn nhậu!". Bố cục: BÊN TRÁI hai ông chú ngồi bàn nhậu nhỏ có đĩa mồi, một ông dang rộng hai tay kể chuyện phóng đại, bong bóng suy nghĩ phía trên vẽ cảnh con tôm nhỏ đấm vỡ bể kính, ông kia cười ngờ vực xua tay. BÊN PHẢI một cuốn hồ sơ tài liệu khoa học mở ra có ảnh dán (vẽ) chú Tôm Tít và bể kính nứt, được đóng một dấu tick xanh lá to xác nhận là sự thật. Không có chữ.
```
</details>

<details><summary>L50</summary>

```text
Lời thoại: "Vào tháng 4 năm 1998, tại một thủy cung nổi tiếng ở hạt Norfolk nước Anh, một chú tôm tít dài vỏn vẹn 10cm được đặt tên là Tyson đã làm nên một vụ bê bối chấn động!". Bố cục: BÊN TRÁI một tòa nhà thủy cung kiểu Anh cổ điển bằng gạch đỏ với mái vòm, lá cờ Anh nhỏ bay trên nóc, một chiếc xe buýt hai tầng màu đỏ đỗ phía trước, bầu trời mưa phùn xám nhẹ. BÊN PHẢI một khung tròn phóng to bên trong bể kính: chú Tôm Tít nhỏ xíu đeo đôi găng đấm bốc đỏ, bên cạnh một chiếc thước kẻ vàng (không số) cho thấy nó chỉ nhỏ bằng bàn tay, mặt hầm hố.
```
</details>

<details><summary>L51</summary>

```text
Lời thoại: "Kết quả là mặt kính nứt đôi thành hình mạng nhện, nước biển bắt đầu phun ra xối xả và toàn bộ nhân viên thủy cung phải kích hoạt còi báo động khẩn cấp để sơ tán du khách và cứu vớt các loài sinh vật khác!". Bố cục: Toàn cảnh sảnh thủy cung hỗn loạn: bức tường bể kính lớn nứt hình mạng nhện, nước biển phun thành nhiều tia xối xả ra sàn. Đèn còi báo động đỏ quay trên trần phát vòng sáng. Du khách gồm gia đình có trẻ em hoảng hốt bỏ chạy ra cửa thoát hiểm. Hai nhân viên áo xanh dùng vợt và xô cứu những con cá và rùa biển đang dãy dụa. Góc bể chú Tôm Tít nhỏ khoanh càng vô tội huýt sáo.
```
</details>

<details><summary>L52</summary>

```text
Lời thoại: "Tuyệt đối không bao giờ nuôi Tôm Tít trong bể kính thủy tinh thông thường, mà bắt buộc phải dùng bể nhựa acrylic chống đạn siêu dày!". Bố cục: Chia đôi: BÊN TRÁI một bể kính thủy tinh mỏng thông thường nứt vỡ, bị gạch chéo bằng dấu X đỏ to vẽ tay. BÊN PHẢI một bể nhựa acrylic trong suốt với vách cực kỳ dày như bức tường hầm ngân hàng, có bu lông to ở góc, được đánh dấu tick xanh lá. Bên trong bể acrylic chú Tôm Tít phụng phịu đấm thử vào vách nhưng chỉ nảy ngược lại, mặt hờn dỗi.
```
</details>

<details><summary>L53</summary>

```text
Lời thoại: "Nó không chỉ nhìn thấy dải màu rực rỡ gấp năm lần chúng ta, mà còn nhìn thấu cả tia cực tím UV và là sinh vật duy nhất trên Trái Đất nhìn được ánh sáng phân cực tròn!". Bố cục: Chú Tôm Tít đứng trên bục cao nhất có đôi mắt lồi phát sáng cầu vồng, nhìn lên bầu trời thấy những dải sáng xoắn ốc lò xo (phân cực tròn) và tia tím huỳnh quang (UV) lấp lánh rực rỡ. Bên dưới bục, một con người, một con mèo và một con chim đại bàng đang ngó cùng hướng nhưng chỉ thấy khoảng trống, mặt ngơ ngác với dấu chấm hỏi.
```
</details>

<details><summary>L54</summary>

```text
Lời thoại: "Mỗi con mắt của nó có thể chuyển động độc lập 360° và tự đo khoảng cách không gian 3D mà không cần đến mắt còn lại.". Bố cục: Cận cảnh đầu chú Tôm Tít: con mắt bên trái xoay nhìn thẳng lên trên, con mắt bên phải xoay nhìn ngược ra phía sau, mỗi con mắt có một vòng tròn mũi tên xoay tròn đầy đủ màu cam quanh nó. Từ con mắt phải phóng ra một lưới hình hộp 3D phối cảnh màu xanh dương chạm tới một con cá nhỏ ở xa, như máy đo khoảng cách. Biểu cảm vui nhộn lác mắt.
```
</details>

<details><summary>L55</summary>

```text
Lời thoại: "Từ những rạn san hô nhiệt đới nông cạn cho đến những đáy bùn tăm tối ngoài đại dương, Tôm Tít đã dạy cho chúng ta một bài học sinh tồn vô cùng sâu sắc của mẹ thiên nhiên.". Bố cục: Dải toàn cảnh ngang: BÊN TRÁI rạn san hô nhiệt đới nông sáng rực đầy màu sắc với ánh nắng xuyên mặt nước, chuyển dần sang BÊN PHẢI là đáy bùn tối xanh thẫm sâu thẳm. Ở GIỮA chú Tôm Tít đeo kính gọng tròn như thầy giáo, cầm que chỉ, đứng cạnh một tấm bảng đen nhỏ (bảng trống, không chữ), mỉm cười hiền từ.
```
</details>

<details><summary>L56</summary>

```text
Lời thoại: "Sở hữu sức mạnh vô song như cú đấm viên đạn không có nghĩa là bạn luôn luôn bất khả chiến bại.". Bố cục: Chú Tôm Tít võ sĩ đeo găng đỏ và đai vô địch vàng đứng tạo dáng cơ bắp oai vệ phía trước. Nhưng cái bóng in trên nền phía sau nó lại là hình một chú tôm mềm oặt như thạch đang run rẩy khóc. Tương phản hai mặt của kẻ mạnh, không khí suy ngẫm.
```
</details>

<details><summary>L57</summary>

```text
Lời thoại: "Biết nhẫn nhịn, thu mình trốn kỹ trong hang tối khi cơ thể đang lột xác yếu mềm nhất". Bố cục: Trong hang đá tối ấm cúng, chú Tôm Tít mềm màu nhạt ngồi khoanh chân thiền định bình thản, mắt nhắm, bên cạnh là một chiếc đồng hồ cát đang chảy và lớp vỏ cũ rỗng treo trên móc như bộ áo. Ngoài miệng hang lũ cá săn mồi bơi qua nhưng không thấy nó. Không khí yên tĩnh, kiên nhẫn.
```
</details>

<details><summary>L58</summary>

```text
Lời thoại: "Bạn ấn tượng nhất với điều gì ở gã võ sĩ đại dương này: Cú đấm bọt khí nóng ngang Mặt Trời hay đôi mắt nhìn thấu cả tế bào ung thư?". Bố cục: Bố cục bình chọn: hai khung tròn lớn hai bên. KHUNG TRÁI viền cam: cú đấm càng búa tạo bọt khí nổ thành quả cầu lửa như Mặt Trời tí hon. KHUNG PHẢI viền tím: đôi mắt lồi cầu vồng của Tôm Tít phát tia sáng quét lên các tế bào ung thư màu tím đang phát sáng. Ở GIỮA dưới hai khung, chú Tôm Tít gãi đầu bối rối, hai càng chỉ hai bên, dấu chấm hỏi trên đầu.
```
</details>

<details><summary>L59</summary>

```text
Lời thoại: "Đừng quên bấm Đăng ký kênh Vẽ Chuyện Hoang Dã và bật Chuông thông báo để không bỏ lỡ tập tiếp theo nhé!". Bố cục: Chú Tôm Tít vui vẻ đeo găng đỏ, một càng đấm nhẹ vào một nút tròn đỏ lớn (biểu tượng play hình tam giác trắng), càng kia vẫy chào tạm biệt, bên cạnh là một chiếc chuông vàng đang rung leng keng với các đường rung. Vài ngôi sao lấp lánh, nụ cười tươi nháy mắt.
```
</details>

<details><summary>L60</summary>

```text
Lời thoại: "Họ hàng nhà Tôm Tít còn có cả phe đâm, mang đôi càng đầy gai nhọn như chiếc xiên nướng, phóng ra xiên trúng con cá đang bơi ngang chỉ trong tích tắc.". Bố cục: Dưới đáy cát, một chú tôm tít KHÁC (họ hàng phe đâm: thân dài màu nâu vàng sọc, cùng kiểu mắt lồi trên cuống) thò nửa người ra khỏi hang cát, phóng đôi càng dài mảnh đầy gai nhọn như chiếc xiên nướng thịt về phía BÊN PHẢI, xiên trúng một con cá nhỏ màu xanh đang bơi ngang, con cá mắt xoắn ngạc nhiên. Vệt tốc độ màu vàng cam sau càng. Mặt chú tôm phe đâm tập trung như kiếm sĩ.
```
</details>

<details><summary>L61</summary>

```text
Lời thoại: "Một phe đấm bốc, một phe đấu kiếm, đúng là cả một gia tộc võ lâm dưới đáy biển!". Bố cục: Cảnh hài kiểu phim võ hiệp: BÊN TRÁI chú Tôm Tít mai xanh ngọc đeo găng đấm bốc đỏ thủ thế quyền anh; BÊN PHẢI chú tôm tít họ hàng màu nâu vàng sọc cầm đôi càng gai như hai thanh kiếm, thủ thế đấu kiếm. Hai bên cúi chào nhau theo kiểu võ lâm trên một võ đài bằng tảng đá phẳng dưới đáy biển. Phía sau là một hàng tôm tít nhỏ đủ màu ngồi xem như đệ tử môn phái, vài con cá cổ vũ.
```
</details>

<details><summary>L62</summary>

```text
Lời thoại: "Cứ mỗi lần lột xác, Tôm Tít lại được thay luôn một cặp búa mới tinh, cứ như võ sĩ được tài trợ đôi găng mới sau mỗi mùa giải vậy!". Bố cục: Chú Tôm Tít mai xanh ngọc vui sướng đứng giữa, hai càng búa mới tinh sáng bóng lấp lánh có tia sao. BÊN TRÁI dưới đất là đôi càng búa cũ sứt mẻ, mòn vẹt, dán băng keo, bị vứt vào thùng rác nhỏ. BÊN PHẢI một chú cua quản lý đeo kính đen trao tặng một hộp quà mở nắp đựng đôi găng đỏ mới, kèm pháo giấy nhiều màu tung bay như lễ trao giải.
```
</details>

<details><summary>L63</summary>

```text
Lời thoại: "Nhưng cái giá của món quà đó thì... lát nữa bạn sẽ biết!". Bố cục: Chú Tôm Tít mai xanh ngọc đang hớn hở ôm hộp quà đựng đôi càng búa mới, hoàn toàn không để ý. Phía sau lưng nó, trên vách đá, một chiếc đồng hồ cát lớn đang chảy cát, và từ bóng tối góc phải một con cá mú to xám lấp ló hé mắt rình mò với nụ cười gian. Không khí hài hước nhưng có chút báo trước điềm chẳng lành, có một dấu chấm hỏi cam nhỏ.
```
</details>

<details><summary>L64</summary>

```text
Lời thoại: "Tôm Tít còn dùng chính ánh sáng phân cực để nhắn tin bí mật cho nhau, trên cơ thể có những mảng phát tín hiệu mà kẻ thù nhìn vào chẳng thấy gì.". Bố cục: BÊN TRÁI và Ở GIỮA hai chú Tôm Tít mai xanh ngọc đứng đối diện nhau, trên thân mỗi con có vài mảng phát sáng lấp lánh xoắn ốc cầu vồng, giữa chúng là các dải sóng ánh sáng xoắn lò xo màu tím-xanh bay qua lại như đang nhắn tin, cả hai cười khúc khích che miệng bằng càng. BÊN PHẢI một con cá săn mồi to nhìn vào cùng chỗ đó nhưng trong mắt nó chỉ thấy hai con tôm bình thường, mặt ngơ ngác với dấu chấm hỏi.
```
</details>

<details><summary>L65</summary>

```text
Lời thoại: "Gã giang hồ cục súc này hóa ra lại là một người chồng chung thủy: có loài sống thành cặp trong cùng một hang tới 20 năm!". Bố cục: Bên trong một căn hang cát ấm cúng dưới đáy biển được trang trí như ngôi nhà nhỏ: một cặp vợ chồng Tôm Tít mai xanh ngọc ngồi cạnh nhau, con chồng đeo nơ, con vợ đội nơ hồng, cùng nhìn nhau trìu mến, trái tim đỏ nhỏ bay lên. Trên vách hang treo khung ảnh cưới vẽ hai con tôm và một dãy nhiều vạch khắc đếm thời gian dài trên đá (không số). Trước hang có hàng rào vỏ sò nhỏ.
```
</details>

<details><summary>L66</summary>

```text
Lời thoại: "Ra ngoài thì đấm nứt kính, về nhà thì ngoan như mèo!". Bố cục: Chia đôi hài hước: BÊN TRÁI chú Tôm Tít mai xanh ngọc đeo găng đỏ mặt hầm hố đấm nứt mặt kính bể cá hình mạng nhện, mảnh kính bắn ra. BÊN PHẢI cũng chính chú Tôm Tít ấy ở nhà trong hang, đeo tạp dề hồng, ngoan ngoãn rửa chén vỏ sò, mắt to long lanh cười hiền như mèo con, bên cạnh tôm vợ khoanh càng hài lòng. Một đường chia đôi vẽ tay ở giữa.
```
</details>

## 7. SEO

- **title:** Cú Đấm Nóng Bằng Mặt Trời... Đấm Nát Bể Kính Thủy Cung! | Tôm Tít | Tập 7
- **hook_paragraph:** Tôm Tít (Mantis Shrimp) dài chưa đầy 20cm nhưng sở hữu cú đấm gia tốc 10.400g nhanh ngang đạn súng trường, tạo ra bọt khí Cavitation nóng tới 4.700°C gần bằng bề mặt Mặt Trời! Vậy mà mỗi mùa lột xác, võ sĩ Mike Tyson đại dương lại mềm nhũn như thạch bơ trốn trong hang...
- **question:** Nếu được chọn giữa cú đấm nóng bằng Mặt Trời và đôi mắt 16 màu nhìn thấu ung thư, bạn sẽ chọn siêu năng lực nào? Bình luận bên dưới nhé!
- **next_teaser:** Cá Thòi Lòi — loài cá biết trèo cây và chạy trên cạn!
- **shorts_title:** Cú Đấm Nóng Bằng Mặt Trời Đấm Vỡ Cả Bể Kính?! 🥊 #shorts #tomtit
- **shorts_desc:** Gia tốc 10.400g nhanh như đạn súng trường, tạo nhiệt 4.700°C nướng chín con mồi… nhưng Tôm Tít lại mềm như thạch khi lột xác! 🥊
👉 Xem bản đầy đủ: vụ án đấm nứt bể kính thủy cung và mắt 16 màu — video Tập 7 trên kênh Vẽ Chuyện Hoang Dã.
- **bullets:** Cú đấm 1.500 Newton gia tốc 10.400g xé toạc nước biển như đạn 22 ly · Hiện tượng Cavitation bọt khí xâm thực sinh nhiệt 4.700°C và phát quang · Càng cấu trúc nano Bouligand chống nứt quân đội Mỹ đang học hỏi · Vụ án chú tôm Tyson đấm nứt bể kính thủy cung năm 1998 và đôi mắt 16 màu
- **tags:** tôm tít, tom tit, mantis shrimp, tôm bọ ngựa, peacock mantis shrimp, cú đấm tôm tít, cavitation, bouligand, mike tyson đại dương, động vật kỳ lạ, thế giới động vật, khám phá động vật, vẽ chuyện hoang dã, whiteboard animation, khoa học thú vị, vũ khí tự nhiên, sinh vật biển
- **hashtags:** #TomTit #MantisShrimp #TheGioiDongVat #VeChuyenHoangDa #KhoaHoc

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-07-tom-tit
python src/episode/pipeline.py tts    projects/tap-07-tom-tit     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-07-tom-tit     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-07-tom-tit     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-07-tom-tit              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-07-tom-tit --force
python scripts/beat_sheet.py projects/tap-07-tom-tit               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-07-tom-tit/audio/shorts.wav projects/tap-07-tom-tit/renders/tap-07-tom-tit_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-07-tom-tit
python src/episode/pipeline.py seo    projects/tap-07-tom-tit
python src/episode/episode_doc.py     projects/tap-07-tom-tit
```
