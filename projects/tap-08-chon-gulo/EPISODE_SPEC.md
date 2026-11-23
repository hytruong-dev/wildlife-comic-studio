# TẬP 8 — CHỒN GULO · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-08-chon-gulo`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-08-chon-gulo`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Chồn Gulo |
| Tiêu đề YouTube | Nặng 15kg Dám Cướp Mồi Của Cả Đàn Sói Và Gấu Xám?! \| Chồn Gulo \| Tập 8 |
| Video dài | `renders/tap-08-chon-gulo_long.mp4` — 10:01.8 (601.8s) |
| Shorts | `renders/tap-08-chon-gulo_shorts.mp4` — 0:50.8 (50.8s) |
| Thumbnail | `renders/tap-08-chon-gulo_thumbnail.jpg` |
| Số hình | dài 67 beat / 67 ảnh riêng; Shorts 13 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.1**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |
| YouTube Video Dài | [https://youtu.be/R4S5wDrD-KQ](https://youtu.be/R4S5wDrD-KQ) — Lên lịch: `8 thg 11, 2026 19:00` |
| YouTube Shorts | [https://youtu.be/uNsCog9baqI](https://youtu.be/uNsCog9baqI) — Lên lịch: `8 thg 11, 2026 19:00` |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu; NỀN TRẮNG TINH hoàn toàn (#FFFFFF), không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: Chú Chồn Gulo (Wolverine - Gulo gulo) hoạt hình 2D comic, thân hình lùn mập chắc nịch như gấu bông lai chồn hương, lông nâu sẫm bóng mượt có hai dải sọc màu vàng kem chạy dọc từ hai bên vai qua sườn xuống đuôi, bốn chân ngắn nhưng bàn chân bè rất to xòe rộng như ủng trượt tuyết với móng vuốt sắc bén, đôi tai tròn nhỏ, đôi mắt tinh quái biểu cảm cộc cằn liều lĩnh hoặc tự tin ngông nghênh.
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — GÃ CHÍ PHÈO XỨ TUYẾT DÁM CƯỚP MỒI CỦA GẤU XÁM
*Thẻ chương:* Kẻ điên rồ nhất vùng băng giá Bắc Cực

**Part 0** → `audio/vs/scene01_p0.wav` (861 ký tự)

```text
[surprise-oh] Nếu bạn nghĩ chúa tể vùng băng tuyết phương Bắc là loài gấu trắng khổng lồ hay những đàn sói xám hung hãn, thì bạn vừa bỏ qua một kẻ điên khét tiếng nhất thế giới hoang dã! Một sinh vật thân hình cũn cỡn như con gấu bông lai chồn hương, nặng vỏn vẹn mười lăm ki-lô-gam, nhưng sở hữu lá gan to hơn cả ngọn núi lửa! Hãy làm quen với Chồn Gu-lô, hay còn gọi là Uân-vơ-rin, nhân vật nguyên mẫu đã truyền cảm hứng cho siêu anh hùng Người Sói móng vuốt kim loại của hãng Mác-vơn! Nhìn bề ngoài, chú ta lùn tịt, bốn chân ngắn củn, dáng đi lạch bạch lắc lư trông cực kỳ cù lần. Thế nhưng, ẩn sau ngoại hình lù khù đó là bản tính hung dữ, cục súc và liều lĩnh đến mức điên rồ! [laughter] Kẻ thù thấy nó thì phát hoảng, thợ săn nghe tên nó thì lắc đầu ngán ngẩm, còn các loài thú ăn thịt đầu bảng thì chỉ ước gì chưa từng chạm mặt gã giang hồ này trong đời!
```
**Part 1** → `audio/vs/scene01_p1.wav` (572 ký tự)

```text
Các nhà động vật học thường gọi Chồn Gu-lô là người anh em xứ tuyết của Lửng Mật. Nếu Lửng Mật là Chí Phèo của thảo nguyên châu Phi nóng rẫy, thì Chồn Gu-lô chính là trùm giang hồ bảo kê cả vùng rừng Tai-ga lạnh thấu xương! Lý do đơn giản: chú ta không hề có khái niệm sợ hãi trong từ điển sống! Dù đối thủ có là một con gấu xám Gờ-rít-zli nặng ba trăm ki-lô-gam hay cả một đàn sói đói đang vây quanh bữa ăn, gã lùn này vẫn sẵn sàng xông thẳng vào cướp trắng miếng thịt trước mũi đối phương! [laughter] Một gã tí hon mang dũng khí của một con quái vật không thể thuần hóa!
```
**Part 2** → `audio/vs/scene01_p2.wav` (545 ký tự)

```text
Chưa hết đâu, gã này còn là cơn ác mộng truyền kiếp của những người thợ săn và thợ bẫy thú rừng phương Bắc! Mỗi khi thợ săn dựng lều và đặt bẫy gỗ kiên cố trong rừng, Chồn Gu-lô sẽ lén đi theo sau, dùng răng cắn nát bẫy, cuỗm sạch thịt mồi, rồi đột nhập vào tận kho lều ăn sạch lương thực! Đỉnh điểm của sự trêu ngươi là trước khi bỏ đi, chú ta còn phun một bãi xạ hôi nồng nặc lên toàn bộ số đồ đạc còn lại coi như lời chào tạm biệt! [laughter] Thợ săn mở cửa lều chỉ biết ôm đầu khóc thét vì vừa mất của vừa phải ngửi mùi hôi suốt cả mùa đông!
```

### scene02 — BẢNG CHỈ SỐ RPG — LỖI GAME CỦA TẠO HÓA XỨ LẠNH
*Thẻ chương:* Khi thiên nhiên quên cài thanh tụt máu

**Part 0** → `audio/vs/scene02_p0.wav` (785 ký tự)

```text
[surprise-wa] Nếu đưa Chồn Gu-lô vào một tựa game nhập vai sinh tồn, chắc chắn nhân vật này sẽ bị gắn mác là kẻ gian lận chỉ số một cách trắng trợn! Hãy cùng bóc tách bảng chỉ số sinh tồn dị biệt của gã võ sĩ xứ tuyết: Sức mạnh tấn công A-T-K: chín mươi điểm! Đừng để thân hình dài sáu mươi lăm xăng-ti-mét đánh lừa bạn; lực cắn của nó đủ sức bẻ gãy xương đùi đông cứng của nai sừng tấm trong một tích tắc! Chỉ số phòng thủ D-E-F: chín mươi lăm điểm! Da của nó dày như tấm thảm bọc thép, lớp lông kỵ nước không bao giờ bị đóng băng dù nhiệt độ có hạ xuống âm bốn mươi độ C! Và đáng sợ nhất là chỉ số thể lực bền bỉ: chạm nóc tuyệt đối một ngàn điểm không đáy! Nó có thể chạy liên tục bảy mươi cây số qua các rặng núi dốc đứng ngập tuyết mà nhịp tim vẫn đập đều như một cỗ máy vĩnh cửu!
```
**Part 1** → `audio/vs/scene02_p1.wav` (595 ký tự)

```text
Để bạn dễ hình dung sự vi diệu của bộ khung cơ thể này: Chồn Gu-lô sở hữu bốn bàn chân bè cực rộng, có màng da và móng vuốt sắc nhọn hoạt động y hệt một đôi ủng trượt tuyết chuyên dụng! Trong khi những con mồi nặng nề như tuần lộc hay nai sừng tấm bị sa lầy tuyết ngập đến tận bụng và bất lực giãy giụa, gã lùn này lại lướt đi trên mặt tuyết mềm nhẹ nhàng như một nghệ sĩ trượt băng nghệ thuật! [laughter] Thế là một cuộc rượt đuổi không cân sức biến thành trò đùa: kẻ khổng lồ thì kiệt sức vì lún tuyết, còn kẻ tí hon thì thong thả chạy vòng quanh đợi con mồi hết pin rồi mới nhảy vào kết liễu!
```
**Part 2** → `audio/vs/scene02_p2.wav` (376 ký tự)

```text
Chưa hết đâu, cơ bắp cổ và hàm của Chồn Gu-lô phát triển khủng khiếp đến mức nó có thể tha một chiếc đầu nai nặng gấp đôi trọng lượng cơ thể mình leo phăng phăng lên vách núi dựng đứng! Cứ như thể một cậu bé mười tuổi nâng bổng chiếc xe máy phân khối lớn rồi chạy bộ lên đỉnh dốc vậy! [laughter] Thật là một thiết kế vật lý thách thức mọi định luật công thái học của tự nhiên!
```

### scene03 — CHIẾC RĂNG HÀM XOAY 90 ĐỘ & TUYẾN XẠ SKUNK BEAR
*Thẻ chương:* Cỗ máy nghiền xương đá và vũ khí sinh học

**Part 0** → `audio/vs/scene03_p0.wav` (771 ký tự)

```text
[surprise-oh] Nhưng vũ khí cơ học quái đản nhất của Chồn Gu-lô nằm ở bên trong khoang miệng của nó! Các nhà giải phẫu học từng kinh ngạc khi phát hiện chiếc răng hàm trên đặc biệt của nó được xoay ngang chín mươi độ hướng hẳn vào phía trong vòm họng! Chiếc răng này hoạt động như một chiếc kìm cộng lực bẻ sắt: nó cho phép Chồn Gu-lô ngoạm chặt và nghiền nát những khúc xương lớn đã bị đông cứng thành đá tảng ở âm năm mươi độ C! [surprise-ah] Vào mùa đông khắc nghiệt khi thức ăn khan hiếm cùng cực, tất cả các loài dã thú khác đều phải bỏ lại những bộ xương đóng băng vì sợ mẻ răng, thì Chồn Gu-lô ung dung bước tới, bẻ vụn từng mẩu xương và hút sạch tủy béo giàu dinh dưỡng bên trong! Đối với nó, xương đông lạnh chẳng khác nào những que kem đá bùi ngậy giữa mùa đông!
```
**Part 1** → `audio/vs/scene03_p1.wav` (633 ký tự)

```text
[surprise-wa] Bên cạnh chiếc răng kìm sắt, gã này còn sở hữu một vũ khí sinh học kinh hoàng khiến người ta đặt cho nó biệt danh Chồn Gấu Hôi, tức X-kâng Bia! Ngay dưới đuôi của nó là một tuyến xạ mùi cực nồng, có khả năng phun ra một hợp chất hóa học bốc mùi khủng khiếp! Mùi hôi này là sự kết hợp kinh dị giữa mùi trứng thối lưu huỳnh, mắm tôm ủ lâu ngày và mùi tất ướt của một đội bóng sau trận chung kết! [laughter] Khi cướp được thức ăn hoặc giấu mồi, chú ta sẽ lập tức tưới đẫm dung dịch hôi hám này lên miếng thịt. Kết quả là chẳng có con thú săn mồi nào, dù đói đến mấy, dám hạ mình chạm mồm vào đống thức ăn thối hoắc đó nữa!
```
**Part 2** → `audio/vs/scene03_p2.wav` (363 ký tự)

```text
Ngoài ra, khứu giác của Chồn Gu-lô nhạy bén đến mức khó tin: nó có thể đánh hơi thấy xác một con nai bị tuyết lở chôn vùi sâu tới sáu mét dưới lòng đất! Sau đó, nó dùng bốn móng vuốt cào bới như một chiếc máy xúc mini, đào xuyên qua lớp băng tuyết dày để lôi bữa ăn miễn phí lên thưởng thức! [laughter] Đúng là một chiếc ra-đa sống của thần chết vùng tuyết trắng!
```
**Part 3** → `audio/vs/scene03_p3.wav` (652 ký tự)

```text
Đặc biệt, bộ lông của Chồn Gu-lô là một kiệt tác cách nhiệt tối thượng của tự nhiên! Cấu trúc sợi lông rỗng và phủ lớp dầu kỵ nước hoàn hảo, khiến sương giá và hơi ẩm không thể bám dính hay đông đá. Người thợ săn bản địa Et-xki-mô từ ngàn xưa đã xem lông Chồn Gu-lô là thứ đắt giá nhất để may viền mũ trùm đầu mùa đông: khi thở ra ở âm bốn mươi độ C, hơi thở của con người sẽ lập tức đóng băng thành dải dao cạo sắc nhọn cứa vào mặt nếu dùng lông thú thường, nhưng với lông Chồn Gu-lô, bạn chỉ cần gạt nhẹ tay là toàn bộ tuyết đá rơi sạch như bụi! [laughter] Một chiếc áo giáp chống băng giá mà không hãng thời trang nào trên thế giới có thể bắt chước!
```

### scene04 — GÓT CHÂN A-SIN — QUÁI VẬT DẠ DÀY & ĐỘC HÀNH XỨ TUYẾT
*Thẻ chương:* Cái bụng không đáy và gã độc thân khó tính nhất hành tinh

**Part 0** → `audio/vs/scene04_p0.wav` (769 ký tự)

```text
[sigh] Nghe đến đây, bạn hẳn đang nghĩ Chồn Gu-lô là một cỗ máy sinh tồn hoàn hảo không một vết xước đúng không? Nhưng tạo hóa luôn cài cắm những trò hề trớ trêu! Tên khoa học của nó, Gu-lô Gu-lô, trong tiếng La-tinh có nghĩa đen là Kẻ Phàm Ăn! Tốc độ trao đổi chất của nó nhanh đến mức điên cuồng để duy trì thân nhiệt giữa cái lạnh âm bốn mươi độ C, biến nó thành một kẻ nô lệ của dạ dày! Nó phải ăn liên tục và thèm ăn đến phát rồ! Để không bị chết đói, nó biến cả khu rừng tuyết thành một chuỗi tủ lạnh siêu thị: bất cứ con mồi nào ăn không hết, nó xé nhỏ ra rồi chôn sâu vào các hốc băng tuyết để đông lạnh dự trữ! [laughter] Nhưng chính cái nết ăn như hổ đó khiến nó luôn trong trạng thái cáu kỉnh, gắt gỏng như người bị hạ đường huyết suốt hai mươi bốn trên bảy!
```
**Part 1** → `audio/vs/scene04_p1.wav` (647 ký tự)

```text
Và điểm yếu bi hài nhất của Chồn Gu-lô chính là bản tính cô độc đến mức cực đoan! Một con đực có thể cai quản lãnh thổ rộng tới một ngàn năm trăm cây số vuông, tức là rộng bằng cả một thành phố lớn, và nó không bao giờ chấp nhận bất kỳ sinh vật nào lai vãng! Ngay cả với đồng loại cùng loài, khuôn mặt chú ta lúc nào cũng nhăn nhó, cau có như mất sổ gạo! Chúng chỉ gặp nhau đúng vài ngày ngắn ngủi trong năm để duy trì nòi giống, rồi lập tức quay lưng bỏ chạy như thể không muốn nhìn mặt nhau thêm một giây nào nữa! [laughter] Một chiến binh vô địch thiên hạ, nhưng cả cuộc đời chỉ lủi thủi độc hành giữa rừng tuyết hoang vu không một bóng bạn bè!
```
**Part 2** → `audio/vs/scene04_p2.wav` (466 ký tự)

```text
Nhưng bạn có biết điều trớ trêu nhất của gã giang hồ này là gì không? Dù cả đời liều mạng đánh nhau với gấu và sói để bảo vệ miếng ăn, nhưng Chồn Gu-lô lại cực kỳ cưng chiều đàn con của mình! Chồn bố thỉnh thoảng vẫn quay lại thăm đàn con nhỏ, dẫn chúng đi săn và dạy chúng kỹ năng bẻ xương tuyết. Nghĩa là ngoài mặt thì cáu kỉnh cục súc với cả thế giới, nhưng bên trong lại là một người cha mẫu mực bí mật! [laughter] Đúng là giang hồ xứ tuyết cũng có lúc yếu lòng!
```

### scene05 — NHỮNG TRẬN CHIẾN CÓ THẬT — MỘT MÌNH ĐUỔI CẢ GẤU LẪN SÓI
*Thẻ chương:* Kẻ điên rồ biến chúa tể phương Bắc thành trò hề

**Part 0** → `audio/vs/scene05_p0.wav` (830 ký tự)

```text
[surprise-oh] Những giai thoại về độ liều của Chồn Gu-lô hoàn toàn được ghi lại bằng máy quay của các nhà sinh vật học thực địa! Tại Vườn quốc gia Yên-lâu-xtôn ở Mỹ, các nhà nghiên cứu từng ghi nhận một thước phim chấn động: một con Chồn Gu-lô nặng chưa đầy mười lăm ki-lô-gam dám hiên ngang lao thẳng vào một xác nai mà một con Gấu Xám Gờ-rít-zli nặng ba trăm ki-lô-gam đang thưởng thức! Chú chồn nhỏ không hề lùi bước, xù toàn bộ lông lên, nhe hàm răng kìm sắt gầm gừ những tiếng rít chói tai và lao tới đớp thẳng vào mõm gấu khổng lồ! [surprise-ah] Bị tấn công bất ngờ bởi một kẻ điên không sợ chết kèm theo mùi hôi nồng nặc bốc lên, con gấu xám khổng lồ nặng gấp hai mươi lần chỉ biết gầm gừ khó chịu rồi lùi lũi bỏ đi! [laughter] Đúng là một minh chứng sống cho câu nói: Kẻ mạnh sợ kẻ liều, kẻ liều sợ kẻ không cần mạng sống!
```
**Part 1** → `audio/vs/scene05_p1.wav` (461 ký tự)

```text
Chưa dừng lại ở đó, tại vùng lãnh nguyên A-lát-xka, người ta từng chứng kiến cảnh một con Chồn Gu-lô đơn độc đánh bật ba con sói xám to lớn khỏi miếng mồi! Sói xám nổi tiếng với chiến thuật bầy đàn thông minh, nhưng đứng trước một gã lùn vừa cắn đau, vừa hôi thối, lại vừa lăn xả như cảm tử quân, bầy sói đành ngậm ngùi rút lui vì nhận ra rằng: Dù có hạ được nó thì bản thân cũng mang thương tật nặng, hoàn toàn không đáng để đánh đổi giữa mùa đông khắc nghiệt!
```
**Part 2** → `audio/vs/scene05_p2.wav` (484 ký tự)

```text
Một nghiên cứu nổi tiếng khác theo dõi chú chồn mang mã số M-ba tại bang Mông-ta-na đã khiến giới khoa học ngả mũ: trong vòng chín mươi phút, chú ta đã leo thẳng đứng lên đỉnh núi Mông Cờ-li-vơ-lân cao hơn ba ngàn một trăm mét phủ đầy băng tuyết dựng đứng! Các vận động viên leo núi chuyên nghiệp phải mất cả ngày trời với đầy đủ dây bảo hiểm và rìu băng, còn chú ta chỉ coi đó là một buổi đi dạo buổi sáng trước khi ăn điểm tâm! [laughter] Thể lực của gã này đúng là ngoài hành tinh!
```

### scene06 — BÀI HỌC SINH TỒN TỪ CHỒN GULO & TEASER TẬP SAU
*Thẻ chương:* Ý chí thép của chiến binh xứ tuyết

**Part 0** → `audio/vs/scene06_p0.wav` (747 ký tự)

```text
Nhìn lại hành trình sinh tồn của Chồn Gu-lô giữa vùng địa đầu băng giá, chúng ta nhận ra một bài học sâu sắc: Kích thước cơ thể hay hoàn cảnh xuất phát điểm chưa bao giờ là yếu tố quyết định giới hạn của bạn! Sinh ra với thân hình nhỏ bé giữa một vùng đất ngập tràn những kẻ săn mồi khổng lồ, Chồn Gu-lô không chọn cách ẩn nấp sợ sệt, mà tự tôi luyện cho mình sức chịu đựng phi thường, lòng dũng cảm thép và sự bền bỉ không thể bị bẻ gãy! Nó biến cái lạnh chết người thành chiếc tủ lạnh bảo quản thức ăn, và biến sự nhỏ bé thành vũ khí cơ động lướt trên tuyết! Trong cuộc sống cũng vậy: Khi bạn dám đương đầu với những nghịch cảnh lớn hơn bản thân gấp nhiều lần và kiên trì bước tiếp mỗi ngày, cả thế giới sẽ phải nghiêng mình nhường bước cho bạn!
```
**Part 1** → `audio/vs/scene06_p1.wav` (455 ký tự)

```text
Nếu được chọn giữa sức mạnh thể lực bền bỉ leo núi không biết mệt của Chồn Gu-lô và cú đấm nóng ngang Mặt Trời của Tôm Tít ở tập trước, bạn sẽ chọn siêu năng lực nào để sinh tồn? Hãy để lại bình luận bên dưới cho chúng mình biết nhé! Đừng quên bấm Đăng ký kênh và chuông thông báo để không bỏ lỡ Tập chín: Chim Cánh Cụt — Đằng sau dáng đi lạch bạch dễ thương là những màn giao dịch đen tối nhất Nam Cực! Hẹn gặp lại các bạn trong cuộc phiêu lưu tiếp theo!
```

### Shorts → `audio/vs/shorts.wav`

```text
Nặng vỏn vẹn mười lăm ki-lô-gam, nhưng dám lao vào cướp mồi của một con Gấu Xám nặng ba trăm ki-lô-gam! Kẻ điên rồ bậc nhất xứ tuyết phương Bắc chính là Chồn Gu-lô, hay còn gọi là Uân-vơ-rin! Với bốn bàn chân bè rộng như đôi ủng trượt tuyết, gã tí hon này lướt nhẹ trên tuyết mềm, trong khi những con mồi khổng lồ sa lầy bất lực! Bộ lông kỵ nước không bao giờ đông đá ở âm bốn mươi độ C, còn chiếc răng hàm trên xoay ngang chín mươi độ thì hoạt động như kìm cộng lực, bẻ vụn cả xương đông đá! [surprise-wa] Nó có thể chạy liên tục bảy mươi cây số qua vách núi dựng đứng, và khi bị bao vây, nó xịt ra luồng xạ hôi kinh hoàng khiến cả bầy sói cũng phải ôm mũi bỏ chạy! [laughter] Nhưng nghịch lý hài hước là gã chiến binh bất bại này lại cô độc đến phát khóc, cả đời lủi thủi một mình vì tính tình quá cộc cằn! [question-ah] Muốn biết gã tí hon này đuổi Gấu Xám cướp mồi ra sao? Bấm xem ngay video dài Tập tám bên dưới nhé, vì gã này...
```

**Whisper prompt:** `Chồn Gulo, Wolverine, Gulo gulo, Gấu Xám Grizzly, Chồn hôi Skunk bear, Băng tuyết Taiga, Yellowstone, Alaska, Răng hàm xoay 90 độ, Đệm chân tuyết, M3, Bất tử xứ tuyết`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| mười lăm ki-lô-gam | 15kg |
| hai mươi lăm ki-lô-gam | 25kg |
| ba trăm ki-lô-gam | 300kg |
| bốn trăm ki-lô-gam | 400kg |
| sáu mươi lăm xăng-ti-mét | 65cm |
| một trăm lẻ năm xăng-ti-mét | 105cm |
| âm bốn mươi độ C | -40°C |
| âm năm mươi độ C | -50°C |
| chín mươi độ | 90° |
| sáu mét | 6m |
| hai mươi mét | 20m |
| bảy mươi cây số | 70km |
| bốn mươi lăm dặm | 45 dặm |
| chín mươi phút | 90 phút |
| ba ngàn một trăm mét | 3.100m |
| một ngàn năm trăm mét | 1.500m |
| một ngàn năm trăm cây số vuông | 1.500km² |
| một ngàn cây số vuông | 1.000km² |
| hai mươi lần | 20 lần |
| mười lần | 10 lần |
| ba con sói | 3 con sói |
| năm mươi mét | 50m |
| ba ngày | 3 ngày |
| hai mươi năm | 20 năm |
| hai mươi tuổi | 20 tuổi |
| Gu-lô | Gulo |
| Uân-vơ-rin | Wolverine |
| Gờ-rít-zli | Grizzly |
| Tai-ga | Taiga |
| Yên-lâu-xtôn | Yellowstone |
| Mác-vơn | Marvel |
| X-kâng Bia | Skunk Bear |
| Et-xki-mô | Eskimo |
| A-lát-xka | Alaska |
| Mông-ta-na | Montana |
| Mông Cờ-li-vơ-lân | Mount Cleveland |
| M-ba | M3 |
| hai mươi bốn trên bảy | 24/7 |
| A-T-K | ATK |
| S-P-D | SPD |
| D-E-F | DEF |
| H-P | HP |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · GÃ CHÍ PHÈO XỨ TUYẾT DÁM CƯỚP MỒI CỦA GẤU XÁM · 104.6s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.8 (9.8s) | L01 | Nếu bạn nghĩ chúa tể vùng băng tuyết phương Bắc là loài gấu trắng khổng lồ hay những đàn sói xám hung hãn, thì bạn vừa bỏ qua một kẻ điên khét tiếng nhất thế giới hoang dã! |  |  |
| b02 | 00:09.8–00:18.1 (8.3s) | L02 | Một sinh vật thân hình cũn cỡn như con gấu bông lai chồn hương, nặng vỏn vẹn 15kg, nhưng sở hữu lá gan to hơn cả ngọn núi lửa! | **15 kg** · cân nặng tí hon · L/380 · [0.35, 0.55] |  |
| b03 | 00:18.1–00:25.8 (7.7s) | L03 | Hãy làm quen với Chồn Gulo, hay còn gọi là Wolverine, nhân vật nguyên mẫu đã truyền cảm hứng cho siêu anh hùng Người Sói móng vuốt kim loại của hãng Marvel! | **MARVEL** · nguyên mẫu Người Sói · R/420 · [0.65, 0.45] |  |
| b04 | 00:25.8–00:31.0 (5.2s) | L04 | Nhìn bề ngoài, chú ta lùn tịt, bốn chân ngắn củn, dáng đi lạch bạch lắc lư trông cực kỳ cù lần. |  |  |
| b05 | 00:31.0–00:36.3 (5.3s) | L05 | Thế nhưng, ẩn sau ngoại hình lù khù đó là bản tính hung dữ, cục súc và liều lĩnh đến mức điên rồ! |  |  |
| b06 | 00:36.3–00:45.7 (9.4s) | L06 | Kẻ thù thấy nó thì phát hoảng, thợ săn nghe tên nó thì lắc đầu ngán ngẩm, còn các loài thú ăn thịt đầu bảng thì chỉ ước gì chưa từng chạm mặt gã giang hồ này trong đời! |  |  |
| b07 | 00:45.7–00:49.7 (4.0s) | L07 | Các nhà động vật học thường gọi Chồn Gulo là người anh em xứ tuyết của Lửng Mật. | **LỬNG MẬT** · anh em kết nghĩa · L/380 · [0.3, 0.5] |  |
| b08 | 00:49.7–00:57.1 (7.3s) | L08 | Nếu Lửng Mật là Chí Phèo của thảo nguyên châu Phi nóng rẫy, thì Chồn Gulo chính là trùm giang hồ bảo kê cả vùng rừng Taiga lạnh thấu xương! | **TAIGA** · địa bàn bảo kê · R/400 · [0.5, 0.5] |  |
| b09 | 00:57.1–01:01.2 (4.2s) | L09 | Lý do đơn giản: chú ta không hề có khái niệm sợ hãi trong từ điển sống! |  |  |
| b10 | 01:01.2–01:16.0 (14.8s) | L10 | Dù đối thủ có là một con gấu xám Grizzly nặng 300kg hay cả một đàn sói đói đang vây quanh bữa ăn, gã lùn này vẫn sẵn sàng xông thẳng vào cướp trắng miếng thịt trước mũi đối phương! Một gã tí hon mang dũng khí của một con quái vật không thể thuần hóa! | **300 kg** · Gấu Xám Grizzly · R/360 · [0.25, 0.45] |  |
| b11 | 01:16.0–01:21.5 (5.5s) | L11 | Chưa hết đâu, gã này còn là cơn ác mộng truyền kiếp của những người thợ săn và thợ bẫy thú rừng phương Bắc! |  |  |
| b12 | 01:21.5–01:31.3 (9.8s) | L12 | Mỗi khi thợ săn dựng lều và đặt bẫy gỗ kiên cố trong rừng, Chồn Gulo sẽ lén đi theo sau, dùng răng cắn nát bẫy, cuỗm sạch thịt mồi, rồi đột nhập vào tận kho lều ăn sạch lương thực! |  |  |
| b13 | 01:31.3–01:44.6 (13.2s) | L13 | Đỉnh điểm của sự trêu ngươi là trước khi bỏ đi, chú ta còn phun một bãi xạ hôi nồng nặc lên toàn bộ số đồ đạc còn lại coi như lời chào tạm biệt! Thợ săn mở cửa lều chỉ biết ôm đầu khóc thét vì vừa mất của vừa phải ngửi mùi hôi suốt cả mùa đông! | **SKUNK** · xạ hôi nồng nặc · R/420 · [0.65, 0.5] |  |

### scene02 · BẢNG CHỈ SỐ RPG — LỖI GAME CỦA TẠO HÓA XỨ LẠNH · 92.8s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:13.7 (13.7s) | L14 | Nếu đưa Chồn Gulo vào một tựa game nhập vai sinh tồn, chắc chắn nhân vật này sẽ bị gắn mác là kẻ gian lận chỉ số một cách trắng trợn! Hãy cùng bóc tách bảng chỉ số sinh tồn dị biệt của gã võ sĩ xứ tuyết: Sức mạnh tấn công ATK: chín mươi điểm! | **ATK 90** · sức tấn công · L/380 · [0.35, 0.45]<br>**DEF 95** · sức phòng thủ · R/420 · [0.65, 0.45] |  |
| b02 | 00:13.7–00:20.3 (6.6s) | L15 | Đừng để thân hình dài 65cm đánh lừa bạn; lực cắn của nó đủ sức bẻ gãy xương đùi đông cứng của nai sừng tấm trong một | **65 cm** · chiều dài cơ thể · L/380 · [0.45, 0.55] |  |
| b03 | 00:20.3–00:29.5 (9.1s) | L16 | tích tắc! Chỉ số phòng thủ DEF: chín mươi lăm điểm! Da của nó dày như tấm thảm bọc thép, lớp lông kỵ nước không bao giờ bị đóng băng dù nhiệt độ có hạ xuống -40°C! | **-40°C** · không đóng băng · R/420 · [0.5, 0.5] |  |
| b04 | 00:29.5–00:34.6 (5.1s) | L17 | Và đáng sợ nhất là chỉ số thể lực bền bỉ: chạm nóc tuyệt đối một ngàn điểm không đáy! | **STA 1000** · thể lực không đáy · R/420 · [0.65, 0.45] |  |
| b05 | 00:34.6–00:41.3 (6.7s) | L18 | Nó có thể chạy liên tục 70km qua các rặng núi dốc đứng ngập tuyết mà nhịp tim vẫn đập đều như một cỗ máy vĩnh cửu! | **70 km** · chạy bền bỉ · L/380 · [0.5, 0.5] |  |
| b06 | 00:41.3–00:51.2 (9.9s) | L19 | Để bạn dễ hình dung sự vi diệu của bộ khung cơ thể này: Chồn Gulo sở hữu bốn bàn chân bè cực rộng, có màng da và móng vuốt sắc nhọn hoạt động y hệt một đôi ủng trượt tuyết chuyên dụng! | **SNOWSHOE** · đệm chân rộng · R/440 · [0.55, 0.5] |  |
| b07 | 00:51.2–01:02.5 (11.3s) | L20 | Trong khi những con mồi nặng nề như tuần lộc hay nai sừng tấm bị sa lầy tuyết ngập đến tận bụng và bất lực giãy giụa, gã lùn này lại lướt đi trên mặt tuyết mềm nhẹ nhàng như một nghệ sĩ trượt băng nghệ thuật! |  |  |
| b08 | 01:02.5–01:13.1 (10.6s) | L21 | Thế là một cuộc rượt đuổi không cân sức biến thành trò đùa: kẻ khổng lồ thì kiệt sức vì lún tuyết, còn kẻ tí hon thì thong thả chạy vòng quanh đợi con mồi hết pin rồi mới nhảy vào kết liễu! |  |  |
| b09 | 01:13.1–01:22.7 (9.7s) | L22 | Chưa hết đâu, cơ bắp cổ và hàm của Chồn Gulo phát triển khủng khiếp đến mức nó có thể tha một chiếc đầu nai nặng gấp đôi trọng lượng cơ thể mình leo phăng phăng lên vách núi dựng đứng! | **200%** · trọng lượng cơ thể · L/380 · [0.5, 0.5] |  |
| b10 | 01:22.7–01:28.5 (5.8s) | L23 | Cứ như thể một cậu bé mười tuổi nâng bổng chiếc xe máy phân khối lớn rồi chạy bộ lên đỉnh dốc vậy! |  |  |
| b11 | 01:28.5–01:32.8 (4.3s) | L24 | Thật là một thiết kế vật lý thách thức mọi định luật công thái học của tự nhiên! |  |  |

### scene03 · CHIẾC RĂNG HÀM XOAY 90 ĐỘ & TUYẾN XẠ SKUNK BEAR · 127.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:05.7 (5.7s) | L25 | Nhưng vũ khí cơ học quái đản nhất của Chồn Gulo nằm ở bên trong khoang miệng của nó! |  |  |
| b02 | 00:05.7–00:13.3 (7.7s) | L26 | Các nhà giải phẫu học từng kinh ngạc khi phát hiện chiếc răng hàm trên đặc biệt của nó được xoay ngang 90° hướng hẳn vào phía trong vòm họng! | **90°** · răng hàm xoay ngang · R/380 · [0.5, 0.45] |  |
| b03 | 00:13.3–00:23.8 (10.5s) | L27 | Chiếc răng này hoạt động như một chiếc kìm cộng lực bẻ sắt: nó cho phép Chồn Gulo ngoạm chặt và nghiền nát những khúc xương lớn đã bị đông cứng thành đá tảng ở -50°C! | **-50°C** · xương đá đông cứng · L/400 · [0.5, 0.5] |  |
| b04 | 00:23.8–00:36.1 (12.3s) | L28 | Vào mùa đông khắc nghiệt khi thức ăn khan hiếm cùng cực, tất cả các loài dã thú khác đều phải bỏ lại những bộ xương đóng băng vì sợ mẻ răng, thì Chồn Gulo ung dung bước tới, bẻ vụn từng mẩu xương và hút sạch tủy béo giàu dinh dưỡng bên trong! |  |  |
| b05 | 00:36.1–00:41.6 (5.5s) | L29 | Đối với nó, xương đông lạnh chẳng khác nào những que kem đá bùi ngậy giữa mùa đông! |  |  |
| b06 | 00:41.6–00:48.9 (7.3s) | L30 | Bên cạnh chiếc răng kìm sắt, gã này còn sở hữu một vũ khí sinh học kinh hoàng khiến người ta đặt cho nó biệt danh Chồn Gấu Hôi, tức Skunk Bear! | **SKUNK BEAR** · chồn gấu hôi · R/380 · [0.5, 0.5] |  |
| b07 | 00:48.9–00:54.8 (5.9s) | L31 | Ngay dưới đuôi của nó là một tuyến xạ mùi cực nồng, có khả năng phun ra một hợp chất hóa học bốc mùi khủng khiếp! |  |  |
| b08 | 00:54.8–01:01.7 (6.9s) | L32 | Mùi hôi này là sự kết hợp kinh dị giữa mùi trứng thối lưu huỳnh, mắm tôm ủ lâu ngày và mùi tất ướt của một đội bóng sau trận chung |  |  |
| b09 | 01:01.7–01:07.9 (6.1s) | L33 | kết! Khi cướp được thức ăn hoặc giấu mồi, chú ta sẽ lập tức tưới đẫm dung dịch hôi hám này lên miếng thịt. |  |  |
| b10 | 01:07.9–01:13.9 (6.0s) | L34 | Kết quả là chẳng có con thú săn mồi nào, dù đói đến mấy, dám hạ mình chạm mồm vào đống thức ăn thối hoắc đó nữa! |  |  |
| b11 | 01:13.9–01:21.8 (8.0s) | L35 | Ngoài ra, khứu giác của Chồn Gulo nhạy bén đến mức khó tin: nó có thể đánh hơi thấy xác một con nai bị tuyết lở chôn vùi sâu tới 6m dưới lòng đất! | **6 m** · sâu dưới tuyết · L/400 · [0.5, 0.65] |  |
| b12 | 01:21.8–01:33.4 (11.5s) | L36 | Sau đó, nó dùng bốn móng vuốt cào bới như một chiếc máy xúc mini, đào xuyên qua lớp băng tuyết dày để lôi bữa ăn miễn phí lên thưởng thức! Đúng là một chiếc ra-đa sống của thần chết vùng tuyết trắng! |  |  |
| b13 | 01:33.4–01:43.9 (10.5s) | L37 | Đặc biệt, bộ lông của Chồn Gulo là một kiệt tác cách nhiệt tối thượng của tự nhiên! Cấu trúc sợi lông rỗng và phủ lớp dầu kỵ nước hoàn hảo, khiến sương giá và hơi ẩm không thể bám dính hay đông đá. |  |  |
| b14 | 01:43.9–01:57.4 (13.5s) | L38 | Người thợ săn bản địa Eskimo từ ngàn xưa đã xem lông Chồn Gulo là thứ đắt giá nhất để may viền mũ trùm đầu mùa đông: khi thở ra ở -40°C, hơi thở của con người sẽ lập tức đóng băng thành dải dao cạo sắc nhọn cứa vào mặt nếu dùng lông thú thường, | **-40°C** · viền mũ Eskimo · R/400 · [0.5, 0.5] |  |
| b15 | 01:57.4–02:07.7 (10.2s) | L38b | nhưng với lông Chồn Gulo, bạn chỉ cần gạt nhẹ tay là toàn bộ tuyết đá rơi sạch như bụi! Một chiếc áo giáp chống băng giá mà không hãng thời trang nào trên thế giới có thể bắt chước! | **SẠCH TUYẾT** · sợi lông kỵ nước · L/420 · [0.5, 0.5] |  |

### scene04 · GÓT CHÂN A-SIN — QUÁI VẬT DẠ DÀY & ĐỘC HÀNH XỨ TUYẾT · 99.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:13.1 (13.1s) | L39 | Nghe đến đây, bạn hẳn đang nghĩ Chồn Gulo là một cỗ máy sinh tồn hoàn hảo không một vết xước đúng không? Nhưng tạo hóa luôn cài cắm những trò hề trớ trêu! Tên khoa học của nó, Gulo Gulo, trong tiếng La-tinh có nghĩa đen là Kẻ Phàm Ăn! | **GULO GULO** · kẻ phàm ăn · L/380 · [0.5, 0.5] |  |
| b02 | 00:13.1–00:22.7 (9.6s) | L40 | Tốc độ trao đổi chất của nó nhanh đến mức điên cuồng để duy trì thân nhiệt giữa cái lạnh -40°C, biến nó thành một kẻ nô lệ của dạ dày! Nó phải ăn liên tục và thèm ăn đến phát rồ! | **-40°C** · đốt cháy năng lượng · R/420 · [0.5, 0.5] |  |
| b03 | 00:22.7–00:32.9 (10.2s) | L41 | Để không bị chết đói, nó biến cả khu rừng tuyết thành một chuỗi tủ lạnh siêu thị: bất cứ con mồi nào ăn không hết, nó xé nhỏ ra rồi chôn sâu vào các hốc băng tuyết để đông lạnh dự trữ! |  |  |
| b04 | 00:32.9–00:40.7 (7.7s) | L42 | Nhưng chính cái nết ăn như hổ đó khiến nó luôn trong trạng thái cáu kỉnh, gắt gỏng như người bị hạ đường huyết suốt 24/7! | **24/7** · cáu kỉnh vì đói · R/420 · [0.5, 0.5] |  |
| b05 | 00:40.7–00:53.8 (13.2s) | L43 | Và điểm yếu bi hài nhất của Chồn Gulo chính là bản tính cô độc đến mức cực đoan! Một con đực có thể cai quản lãnh thổ rộng tới 1.500km², tức là rộng bằng cả một thành phố lớn, và nó không bao giờ chấp nhận bất kỳ sinh vật nào lai | **1.500 km²** · lãnh thổ độc hành · L/380 · [0.5, 0.5] |  |
| b06 | 00:53.8–01:00.0 (6.2s) | L44 | vãng! Ngay cả với đồng loại cùng loài, khuôn mặt chú ta lúc nào cũng nhăn nhó, cau có như mất sổ gạo! |  |  |
| b07 | 01:00.0–01:08.3 (8.3s) | L45 | Chúng chỉ gặp nhau đúng vài ngày ngắn ngủi trong năm để duy trì nòi giống, rồi lập tức quay lưng bỏ chạy như thể không muốn nhìn mặt nhau thêm một giây nào nữa! |  |  |
| b08 | 01:08.3–01:15.0 (6.8s) | L46 | Một chiến binh vô địch thiên hạ, nhưng cả cuộc đời chỉ lủi thủi độc hành giữa rừng tuyết hoang vu không một bóng bạn bè! |  |  |
| b09 | 01:15.0–01:24.7 (9.7s) | L47 | Nhưng bạn có biết điều trớ trêu nhất của gã giang hồ này là gì không? Dù cả đời liều mạng đánh nhau với gấu và sói để bảo vệ miếng ăn, nhưng Chồn Gulo lại cực kỳ cưng chiều đàn con của mình! |  |  |
| b10 | 01:24.7–01:36.8 (12.0s) | L48 | Chồn bố thỉnh thoảng vẫn quay lại thăm đàn con nhỏ, dẫn chúng đi săn và dạy chúng kỹ năng bẻ xương tuyết. Nghĩa là ngoài mặt thì cáu kỉnh cục súc với cả thế giới, nhưng bên trong lại là một người cha mẫu mực bí mật! |  |  |
| b11 | 01:36.8–01:39.4 (2.7s) | L49 | Đúng là giang hồ xứ tuyết cũng có lúc yếu lòng! |  |  |

### scene05 · NHỮNG TRẬN CHIẾN CÓ THẬT — MỘT MÌNH ĐUỔI CẢ GẤU LẪN SÓI · 93.5s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:06.6 (6.6s) | L50a | Những giai thoại về độ liều của Chồn Gulo hoàn toàn được ghi lại bằng máy quay của các nhà sinh vật học thực địa! |  |  |
| b02 | 00:06.6–00:20.3 (13.7s) | L50 | Tại Vườn quốc gia Yellowstone ở Mỹ, các nhà nghiên cứu từng ghi nhận một thước phim chấn động: một con Chồn Gulo nặng chưa đầy 15kg dám hiên ngang lao thẳng vào một xác nai mà một con Gấu Xám Grizzly nặng 300kg đang thưởng thức! | **YELLOWSTONE** · địa danh ghi nhận · R/400 · [0.5, 0.5] |  |
| b03 | 00:20.3–00:29.1 (8.7s) | L51 | Chú chồn nhỏ không hề lùi bước, xù toàn bộ lông lên, nhe hàm răng kìm sắt gầm gừ những tiếng rít chói tai và lao tới đớp thẳng vào mõm gấu khổng lồ! |  |  |
| b04 | 00:29.1–00:43.8 (14.8s) | L52 | Bị tấn công bất ngờ bởi một kẻ điên không sợ chết kèm theo mùi hôi nồng nặc bốc lên, con gấu xám khổng lồ nặng gấp 20 lần chỉ biết gầm gừ khó chịu rồi lùi lũi bỏ đi! Đúng là một minh chứng sống cho câu nói: Kẻ mạnh sợ kẻ liều, kẻ liều sợ kẻ không cần mạng sống! | **x20** · gấu xám nặng gấp 20 lần · L/380 · [0.25, 0.45] |  |
| b05 | 00:43.8–00:52.3 (8.5s) | L53 | Chưa dừng lại ở đó, tại vùng lãnh nguyên Alaska, người ta từng chứng kiến cảnh một con Chồn Gulo đơn độc đánh bật 3 con sói xám to lớn khỏi miếng mồi! | **ALASKA** · lãnh nguyên băng giá · R/400 · [0.5, 0.5]<br>**1 vs 3** · đánh bật đàn sói · L/380 · [0.35, 0.5] |  |
| b06 | 00:52.3–00:59.2 (6.9s) | L54 | Sói xám nổi tiếng với chiến thuật bầy đàn thông minh, nhưng đứng trước một gã lùn vừa cắn đau, vừa hôi thối, lại vừa lăn xả như cảm tử quân, |  |  |
| b07 | 00:59.2–01:08.1 (8.9s) | L54b | bầy sói đành ngậm ngùi rút lui vì nhận ra rằng: Dù có hạ được nó thì bản thân cũng mang thương tật nặng, hoàn toàn không đáng để đánh đổi giữa mùa đông khắc nghiệt! | **RÚT LUI** · bầy sói chùn bước · L/380 · [0.5, 0.5] |  |
| b08 | 01:08.1–01:14.2 (6.1s) | L55 | Một nghiên cứu nổi tiếng khác theo dõi chú chồn mang mã số M3 tại bang Montana đã khiến giới khoa học ngả mũ: | **M3** · mã số theo dõi · L/380 · [0.5, 0.5] |  |
| b09 | 01:14.2–01:21.6 (7.4s) | L56 | trong vòng 90 phút, chú ta đã leo thẳng đứng lên đỉnh núi Mount Cleveland cao hơn 3.100m phủ đầy băng tuyết dựng đứng! | **90 PHÚT** · thời gian leo đỉnh · R/420 · [0.5, 0.5]<br>**3.100 m** · đỉnh Mount Cleveland · L/380 · [0.5, 0.35] |  |
| b10 | 01:21.6–01:33.5 (12.0s) | L57 | Các vận động viên leo núi chuyên nghiệp phải mất cả ngày trời với đầy đủ dây bảo hiểm và rìu băng, còn chú ta chỉ coi đó là một buổi đi dạo buổi sáng trước khi ăn điểm tâm! Thể lực của gã này đúng là ngoài hành tinh! |  |  |

### scene06 · BÀI HỌC SINH TỒN TỪ CHỒN GULO & TEASER TẬP SAU · 63.6s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:11.4 (11.4s) | L58 | Nhìn lại hành trình sinh tồn của Chồn Gulo giữa vùng địa đầu băng giá, chúng ta nhận ra một bài học sâu sắc: Kích thước cơ thể hay hoàn cảnh xuất phát điểm chưa bao giờ là yếu tố quyết định giới hạn của bạn! |  |  |
| b02 | 00:11.4–00:23.4 (12.0s) | L59 | Sinh ra với thân hình nhỏ bé giữa một vùng đất ngập tràn những kẻ săn mồi khổng lồ, Chồn Gulo không chọn cách ẩn nấp sợ sệt, mà tự tôi luyện cho mình sức chịu đựng phi thường, lòng dũng cảm thép và sự bền bỉ không thể bị bẻ gãy! |  |  |
| b03 | 00:23.4–00:30.0 (6.6s) | L60 | Nó biến cái lạnh chết người thành chiếc tủ lạnh bảo quản thức ăn, và biến sự nhỏ bé thành vũ khí cơ động lướt trên tuyết! |  |  |
| b04 | 00:30.0–00:40.1 (10.1s) | L61 | Trong cuộc sống cũng vậy: Khi bạn dám đương đầu với những nghịch cảnh lớn hơn bản thân gấp nhiều lần và kiên trì bước tiếp mỗi ngày, cả thế giới sẽ phải nghiêng mình nhường bước cho bạn! |  |  |
| b05 | 00:40.1–00:52.5 (12.3s) | L62 | Nếu được chọn giữa sức mạnh thể lực bền bỉ leo núi không biết mệt của Chồn Gulo và cú đấm nóng ngang Mặt Trời của Tôm Tít ở tập trước, bạn sẽ chọn siêu năng lực nào để sinh tồn? Hãy để lại bình luận bên dưới cho chúng mình biết nhé! | **BÌNH LUẬN** · Wolverine hay Tôm Tít? · R/400 · [0.5, 0.5] |  |
| b06 | 00:52.5–01:00.9 (8.5s) | L63 | Đừng quên bấm Đăng ký kênh và chuông thông báo để không bỏ lỡ Tập chín: Chim Cánh Cụt — Đằng sau dáng đi lạch bạch dễ thương là những màn giao dịch đen tối nhất Nam Cực! | **TẬP 9** · Chim Cánh Cụt Nam Cực · L/380 · [0.5, 0.5] |  |
| b07 | 01:00.9–01:03.6 (2.7s) | L64 | Hẹn gặp lại các bạn trong cuộc phiêu lưu tiếp theo! | **ĐĂNG KÝ** · Vẽ Chuyện Hoang Dã · R/420 · [0.5, 0.5] |  |

## 5. Phân cảnh Shorts — từng beat

Banner: **CHỒN GULO 15KG CƯỚP MỒI / GẤU XÁM 300KG?!** · giọng 49.3s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Nặng vỏn vẹn 15kg, nhưng dám lao vào cướp mồi của một con Gấu Xám nặng 300kg! | **15 KG** · Chồn Gulo tí hon · L/960 · [0.5, 0.75]<br>**300 KG** · Gấu Xám Grizzly · R/560 · [0.5, 0.3] |
| s02 | 00:05.2 | S02 | Kẻ điên rồ bậc nhất xứ tuyết phương Bắc chính là Chồn Gulo, hay còn gọi là Wolverine! | **WOLVERINE** · tên tiếng Anh · L/640 · [0.5, 0.35] |
| s03 | 00:10.1 | S11 | Với bốn bàn chân bè rộng như đôi ủng trượt tuyết, | **ỦNG TUYẾT** · bàn chân bè rộng · R/1000 · [0.45, 0.85] |
| s04 | 00:12.8 | S03 | gã tí hon này lướt nhẹ trên tuyết mềm, trong khi những con mồi khổng lồ sa lầy bất lực! | **SA LẦY!** · mồi khổng lồ · L/960 · [0.5, 0.75] |
| s05 | 00:17.2 | S12 | Bộ lông kỵ nước không bao giờ đông đá ở -40°C, | **-40°C** · lông không đóng băng · R/700 · [0.25, 0.5] |
| s06 | 00:20.4 | S04 | còn chiếc răng hàm trên xoay ngang 90° thì hoạt động như kìm cộng lực, bẻ vụn cả xương đông đá! | **90°** · răng hàm xoay ngang · L/700 · [0.5, 0.5] |
| s07 | 00:25.7 | S05 | Nó có thể chạy liên tục 70km qua vách núi dựng đứng, | **70 KM** · chạy không nghỉ · R/760 · [0.5, 0.45] |
| s08 | 00:29.3 | S06 | và khi bị bao vây, nó xịt ra luồng xạ hôi kinh hoàng khiến cả bầy sói cũng phải ôm mũi bỏ chạy! | **XẠ HÔI** · vũ khí hóa học · L/980 · [0.5, 0.75] |
| s09 | 00:35.3 | S13 | Nhưng nghịch lý hài hước là gã chiến binh bất bại này lại cô độc đến phát khóc, | **BẤT BẠI** · mà khóc nhè · R/700 · [0.5, 0.4] |
| s10 | 00:39.2 | S07 | cả đời lủi thủi một mình vì tính tình quá cộc cằn! | **CÔ ĐỘC** · cả đời một mình · L/800 · [0.5, 0.55] |
| s11 | 00:42.4 | S09 | Muốn biết gã tí hon này đuổi Gấu Xám cướp mồi ra sao? |  |
| s12 | 00:45.3 | S08 | Bấm xem ngay video dài Tập tám bên dưới nhé, | **XEM TẬP 8** · bản dài đầy đủ · R/700 · [0.5, 0.6] |
| s13 | 00:48.2 | S10 | vì gã này... |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>base_prompt</summary>

```text
QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu; NỀN TRẮNG TINH hoàn toàn (#FFFFFF), không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: Chú Chồn Gulo (Wolverine - Gulo gulo) hoạt hình 2D comic, thân hình lùn mập chắc nịch như gấu bông lai chồn hương, lông nâu sẫm bóng mượt có hai dải sọc màu vàng kem chạy dọc từ hai bên vai qua sườn xuống đuôi, bốn chân ngắn nhưng bàn chân bè rất to xòe rộng như ủng trượt tuyết với móng vuốt sắc bén, đôi tai tròn nhỏ, đôi mắt tinh quái biểu cảm cộc cằn liều lĩnh hoặc tự tin ngông nghênh.
```
</details>

<details><summary>longform</summary>

```text
[{'id': 'L01', 'quote': 'Nếu bạn nghĩ chúa tể vùng băng tuyết phương Bắc là loài gấu trắng khổng lồ hay những đàn sói xám hung hãn...', 'prompt': 'BÊN TRÁI: Một con gấu Bắc cực khổng lồ màu trắng và một con sói xám đang gầm rú uy phong giữa cơn bão tuyết. BÊN PHẢI: Một cái bóng đen nhỏ xíu có đôi mắt sáng quắc đang nhìn họ đầy thách thức.'}, {'id': 'L02', 'quote': 'Một sinh vật thân hình cũn cỡn như con gấu bông lai chồn hương, nặng vỏn vẹn mười lăm ki-lô-gam...', 'prompt': 'GIỮA: Chồn Gulo đứng trên chiếc cân bập bênh nhỏ, đối diện bên kia là một quả tạ sắt khổng lồ bốc khói hình ngọn núi lửa đang phun trào, biểu thị lá gan siêu to khổng lồ của chú chồn.'}, {'id': 'L03', 'quote': 'Hãy làm quen với Chồn Gu-lô, hay còn gọi là Uân-vơ-rin, nhân vật nguyên mẫu đã truyền cảm hứng cho siêu anh hùng Người Sói...', 'prompt': 'BÊN TRÁI: Chồn Gulo đứng giơ bàn chân xòe bộ móng vuốt sắc nhọn sáng loáng; BÊN PHẢI: Một chiến binh siêu anh hùng hoạt hình đeo găng vuốt kim loại sắc bén đang tạo dáng tương tự đối xứng.'}, {'id': 'L04', 'quote': 'Nhìn bề ngoài, chú ta lùn tịt, bốn chân ngắn củn, dáng đi lạch bạch lắc lư trông cực kỳ cù lần...', 'prompt': 'GIỮA: Chồn Gulo với thân hình lùn mập, bốn chân ngắn cũn, đang bước đi lắc lư lạch bạch trên nền tuyết trắng, mặt ngơ ngác buồn cười.'}, {'id': 'L05', 'quote': 'Thế nhưng, ẩn sau ngoại hình lù khù đó là bản tính hung dữ, cục súc và liều lĩnh đến mức điên rồ!...', 'prompt': 'GIỮA: Chồn Gulo bỗng xù toàn bộ lông lên, hai mắt bốc lửa đỏ rực, nhe răng nanh nhọn hoắt gầm gừ cực kỳ cục súc, tỏa ra luồng khí thế giang hồ đáng sợ.'}, {'id': 'L06', 'quote': 'Kẻ thù thấy nó thì phát hoảng, thợ săn nghe tên nó thì lắc đầu ngán ngẩm...', 'prompt': 'BÊN TRÁI: Bác thợ săn ôm súng run rẩy toát mồ hôi; BÊN PHẢI: Một con linh miêu và một con sói đang lấm lét dòm Chồn Gulo rồi lùi lũi quay đầu bỏ chạy.'}, {'id': 'L07', 'quote': 'Các nhà động vật học thường gọi Chồn Gu-lô là người anh em xứ tuyết của Lửng Mật...', 'prompt': 'BÊN TRÁI: Lửng Mật đeo kính râm mặc áo cộc tay châu Phi; BÊN PHẢI: Chồn Gulo quàng khăn len mùa đông; cả hai đập tay nhau (high-five) như hai đại ca giang hồ bắt tay kết nghĩa.'}, {'id': 'L08', 'quote': 'Nếu Lửng Mật là Chí Phèo của thảo nguyên châu Phi nóng rẫy, thì Chồn Gu-lô chính là trùm giang hồ bảo kê cả vùng rừng Tai-ga...', 'prompt': 'GIỮA: Chồn Gulo mặc áo khoác lông đại ca, đứng chống nạnh giữa rừng thông Taiga phủ đầy tuyết trắng, xung quanh có biển chỉ dẫn lãnh thổ đóng dấu bàn chân gấu.'}, {'id': 'L09', 'quote': 'Lý do đơn giản: chú ta không hề có khái niệm sợ hãi trong từ điển sống!...', 'prompt': "GIỮA: Chồn Gulo tung chân đạp bay cuốn từ điển bách khoa có dòng chữ gạch chéo biểu tượng 'Sợ hãi', mặt vênh lên kiêu hãnh bất cần đời."}, {'id': 'L10', 'quote': 'Dù đối thủ có là một con gấu xám Gờ-rít-zli nặng ba trăm ki-lô-gam hay cả một đàn sói đói đang vây quanh bữa ăn...', 'prompt': 'BÊN TRÁI: Con Gấu Xám Grizzly khổng lồ nặng 300kg đang há hốc mồm kinh ngạc; BÊN PHẢI: Chồn Gulo bé nhỏ nhảy bổ vào ngoạm lấy tảng thịt nai tươi ngon giật đi ngay trước mũi gấu.'}, {'id': 'L11', 'quote': 'Chưa hết đâu, gã này còn là cơn ác mộng truyền kiếp của những người thợ săn và thợ bẫy thú rừng phương Bắc!...', 'prompt': 'BÊN PHẢI: Bác thợ săn vác rìu đi phía trước; BÊN TRÁI: Chồn Gulo lén lút bám theo sau từng bước chân trên tuyết, nhe răng cười nham hiểm.'}, {'id': 'L12', 'quote': 'Mỗi khi thợ săn dựng lều và đặt bẫy gỗ kiên cố trong rừng, Chồn Gu-lô sẽ lén đi theo sau, dùng răng cắn nát bẫy...', 'prompt': 'GIỮA: Chiếc bẫy gỗ kiên cố bị Chồn Gulo cắn gãy vụn thành từng mảnh dăm bào, chú chồn đang giơ miếng thịt mồi lên nhai ngon lành như thưởng thức bữa tiệc.'}, {'id': 'L13', 'quote': 'Thợ săn mở cửa lều chỉ biết ôm đầu khóc thét vì vừa mất của vừa phải ngửi mùi hôi suốt cả mùa đông!...', 'prompt': 'BÊN TRÁI: Bác thợ săn mở cửa lều gỗ, hai tay ôm đầu khóc ròng nhìn kho lương thực trống trơn; BÊN PHẢI: Chồn Gulo để lại một đám khói màu vàng xanh bốc mùi hôi nồng nặc và dấu chân chạy trốn.'}, {'id': 'L14', 'quote': 'Nếu đưa Chồn Gu-lô vào một tựa game nhập vai sinh tồn, chắc chắn nhân vật này sẽ bị gắn mác là kẻ gian lận chỉ số...', 'prompt': 'GIỮA: Bảng chỉ số nhân vật RPG kiểu game với hình vẽ Chồn Gulo ở giữa, các thanh máu HP, tấn công ATK, phòng thủ DEF và thể lực STA đều sáng rực tràn viền màn hình.'}, {'id': 'L15', 'quote': 'Sức mạnh tấn công A-T-K: chín mươi điểm! Đừng để thân hình dài sáu mươi lăm xăng-ti-mét đánh lừa bạn...', 'prompt': "GIỮA: Chồn Gulo dùng hàm răng cắn đôi chiếc xương đùi nai sừng tấm đông cứng, chiếc xương gãy đôi kêu 'rắc' với các tia sét va đập màu vàng."}, {'id': 'L16', 'quote': 'Chỉ số phòng thủ D-E-F: chín mươi lăm điểm! Da của nó dày như tấm thảm bọc thép...', 'prompt': 'GIỮA: Chồn Gulo khoác trên mình lớp giáp thép sáng bóng bảo vệ bộ lông, những mũi tên băng nhọn hoắt bắn vào thân nó đều bị bật văng ra ngoài không để lại vết xước.'}, {'id': 'L17', 'quote': 'Và đáng sợ nhất là chỉ số thể lực bền bỉ: chạm nóc tuyệt đối một ngàn điểm không đáy!...', 'prompt': 'GIỮA: Đồng hồ đo thể lực của Chồn Gulo có kim chỉ vượt qua vạch tối đa 1.000, chú chồn đang chạy băng băng trên đỉnh núi tuyết với nụ cười tươi rói không hề mệt mỏi.'}, {'id': 'L18', 'quote': 'Nó có thể chạy liên tục bảy mươi cây số qua các rặng núi dốc đứng ngập tuyết...', 'prompt': 'TOÀN CẢNH: Một bản đồ thu nhỏ với vệt đường chạy ngoằn ngoèo dài 70km vượt qua 3 đỉnh núi tuyết nhấp nhô, chú Chồn Gulo đang chạy băng băng ở điểm cuối.'}, {'id': 'L19', 'quote': 'Để bạn dễ hình dung sự vi diệu của bộ khung cơ thể này: Chồn Gu-lô sở hữu bốn bàn chân bè cực rộng...', 'prompt': 'CẬN CẢNH: Bàn chân của Chồn Gulo đặt cạnh một chiếc ủng đi tuyết (snowshoe) đan bằng dây da của thổ dân, làm nổi bật cấu trúc ngón xòe rộng và màng da đệm thịt.'}, {'id': 'L20', 'quote': 'Trong khi những con mồi nặng nề như tuần lộc hay nai sừng tấm bị sa lầy tuyết ngập đến tận bụng...', 'prompt': 'BÊN TRÁI: Chú tuần lộc to lớn bị thụt lún xuống tuyết sâu ngập bụng, hai mắt lồi ra bất lực thở phì phò; BÊN PHẢI: Chồn Gulo đứng nhẹ tênh trên mặt tuyết mịn màng.'}, {'id': 'L21', 'quote': 'Thế là một cuộc rượt đuổi không cân sức biến thành trò đùa: kẻ khổng lồ thì kiệt sức vì lún tuyết...', 'prompt': 'GIỮA: Chồn Gulo đeo giày trượt băng đang lướt đi thoăn thoắt vòng quanh con nai sừng tấm đang mắc kẹt trong đụn tuyết, chú chồn thong thả vừa trượt vừa huýt sáo trêu chọc.'}, {'id': 'L22', 'quote': 'Chưa hết đâu, cơ bắp cổ và hàm của Chồn Gu-lô phát triển khủng khiếp đến mức nó có thể tha một chiếc đầu nai nặng gấp đôi...', 'prompt': 'GIỮA: Chồn Gulo ngậm một chiếc đầu nai sừng tấm có cặp sừng khổng lồ nặng trĩu, chú ta hiên ngang tha chiếc đầu bước thoăn thoắt lên vách đá dựng đứng.'}, {'id': 'L23', 'quote': 'Cứ như thể một cậu bé mười tuổi nâng bổng chiếc xe máy phân khối lớn rồi chạy bộ lên đỉnh dốc vậy!...', 'prompt': 'HÀI HƯỚC: Một cậu bé hoạt hình 10 tuổi nhỏ nhắn hai tay nâng bổng chiếc xe máy phân khối lớn to đùng, vừa cười toe toét vừa chạy phăng phăng lên con dốc cao.'}, {'id': 'L24', 'quote': 'Thật là một thiết kế vật lý thách thức mọi định luật công thái học của tự nhiên!...', 'prompt': 'GIỮA: Nhà bác học hoạt hình đeo kính cầm bảng tính toán vật lý rơi cả kính mắt kinh ngạc nhìn Chồn Gulo đang phô diễn cơ bắp cổ cuồn cuộn.'}, {'id': 'L25', 'quote': 'Nhưng vũ khí cơ học quái đản nhất của Chồn Gu-lô nằm ở bên trong khoang miệng của nó!...', 'prompt': 'CẬN CẢNH: Miệng Chồn Gulo há to nhe răng cười, một mũi tên phóng to chỉ vào chiếc răng hàm trên đặc biệt bên trong khoang miệng.'}, {'id': 'L26', 'quote': 'Các nhà giải phẫu học từng kinh ngạc khi phát hiện chiếc răng hàm trên đặc biệt của nó được xoay ngang chín mươi độ...', 'prompt': 'HỌA ĐỒ Y KHOA: Sơ đồ hàm răng Chồn Gulo với chiếc răng hàm trên xoay ngang 90 độ vào phía trong, có thước đo góc 90 độ màu vàng rực rỡ.'}, {'id': 'L27', 'quote': 'Chiếc răng này hoạt động như một chiếc kìm cộng lực bẻ sắt: nó cho phép Chồn Gu-lô ngoạm chặt và nghiền nát những khúc xương lớn...', 'prompt': 'MINH HỌA SO SÁNH: BÊN TRÁI: Một chiếc kìm cộng lực bằng thép đang cắt đôi thanh sắt; BÊN PHẢI: Hàm răng Chồn Gulo ngoạm bẻ đôi khúc xương đông lạnh đóng băng.'}, {'id': 'L28', 'quote': 'Vào mùa đông khắc nghiệt khi thức ăn khan hiếm cùng cực, tất cả các loài dã thú khác đều phải bỏ lại những bộ xương đóng băng...', 'prompt': 'BÊN TRÁI: Một con sói xám ôm mõm nhăn nhó vì cắn phải xương đá bị mẻ răng; BÊN PHẢI: Chồn Gulo ung dung bước tới với chiếc nĩa và khăn ăn cài cổ.'}, {'id': 'L29', 'quote': 'Đối với nó, xương đông lạnh chẳng khác nào những que kem đá bùi ngậy giữa mùa đông!...', 'prompt': 'HÀI HƯỚC: Chồn Gulo cầm khúc xương đóng băng dài như một que kem ốc quế, đang thè lưỡi liếm và hút tủy béo ngậy một cách ngon lành sảng khoái.'}, {'id': 'L30', 'quote': 'Bên cạnh chiếc răng kìm sắt, gã này còn sở hữu một vũ khí sinh học kinh hoàng khiến người ta đặt cho nó biệt danh Chồn Gấu Hôi...', 'prompt': "GIỮA: Chồn Gulo đứng chống nạnh đeo huy hiệu vương miện có dòng chữ 'Skunk Bear' (Chồn Gấu Hôi), đằng sau là một luồng khói xanh hình đầu lâu bốc mùi."}, {'id': 'L31', 'quote': 'Ngay dưới đuôi của nó là một tuyến xạ mùi cực nồng, có khả năng phun ra một hợp chất hóa học bốc mùi khủng khiếp!...', 'prompt': 'CẬN CẢNH: Phía dưới đuôi Chồn Gulo phun ra một luồng xịt khí màu vàng xanh như bình xịt hơi cay, tạo ra đám mây khói hôi mù mịt.'}, {'id': 'L32', 'quote': 'Mùi hôi này là sự kết hợp kinh dị giữa mùi trứng thối lưu huỳnh, mắm tôm ủ lâu ngày và mùi tất ướt...', 'prompt': 'HÀI HƯỚC: Ba biểu tượng độc hại gồm: quả trứng thối nứt đôi bốc khói, hũ mắm tôm mở nắp có ruồi bay, và đôi tất thể thao bốc mùi; hòa trộn vào luồng xạ của Chồn Gulo.'}, {'id': 'L33', 'quote': 'Khi cướp được thức ăn hoặc giấu mồi, chú ta sẽ lập tức tưới đẫm dung dịch hôi hám này lên miếng thịt...', 'prompt': "GIỮA: Chồn Gulo chổng mông tưới dung dịch xạ hôi lên tảng thịt nai đông lạnh, xung quanh cắm biển cấm 'Đã đánh dấu chủ quyền! Đố đứa nào dám ăn!'."}, {'id': 'L34', 'quote': 'Kết quả là chẳng có con thú săn mồi nào, dù đói đến mấy, dám hạ mình chạm mồm vào đống thức ăn thối hoắc đó nữa!...', 'prompt': 'BÊN TRÁI: Một con gấu xám to lớn và hai con sói đói đang lấy chân bịt chặt mũi, mặt xanh lét nôn nao quay đầu bỏ chạy khỏi đống thịt bốc mùi.'}, {'id': 'L35', 'quote': 'Ngoài ra, khứu giác của Chồn Gu-lô nhạy bén đến mức khó tin: nó có thể đánh hơi thấy xác một con nai bị tuyết lở chôn vùi sâu tới sáu mét...', 'prompt': 'MẶT CẮT ĐỊA CHẤT: Bên trên là mặt tuyết với Chồn Gulo đang hít hà bằng mũi; bên dưới lớp tuyết sâu 6m là xác một con nai bị vùi lấp, có sóng âm khứu giác nối từ mũi chồn xuống.'}, {'id': 'L36', 'quote': 'Sau đó, nó dùng bốn móng vuốt cào bới như một chiếc máy xúc mini, đào xuyên qua lớp băng tuyết dày...', 'prompt': 'GIỮA: Chồn Gulo biến hình thành một chiếc máy xúc mini với gầu múc là móng vuốt, đào tuyết bay tung tóe tạo thành một đường hầm sâu hoắm.'}, {'id': 'L37', 'quote': 'Đặc biệt, bộ lông của Chồn Gu-lô là một kiệt tác cách nhiệt tối thượng của tự nhiên! Cấu trúc sợi lông rỗng và phủ lớp dầu kỵ nước...', 'prompt': 'CẬN CẢNH KÍNH HIỂN VI: Sợi lông rỗng của Chồn Gulo với các giọt nước hình cầu lăn tròn tuột khỏi sợi lông mà không hề thấm ướt.'}, {'id': 'L38', 'quote': 'Người thợ săn bản địa Et-xki-mô từ ngàn xưa đã xem lông Chồn Gu-lô là thứ đắt giá nhất để may viền mũ trùm đầu mùa đông...', 'prompt': 'GIỮA: Một người Eskimo mặc áo ấm Bắc cực có viền mũ lông Chồn Gulo, thở ra làn khói ở -40°C nhưng viền mũ vẫn khô ráo sạch tuyết, chỉ cần gạt nhẹ tay là tuyết rơi sạch.'}, {'id': 'L39', 'quote': 'Tên khoa học của nó, Gu-lô Gu-lô, trong tiếng La-tinh có nghĩa đen là Kẻ Phàm Ăn!...', 'prompt': 'GIỮA: Chồn Gulo ngồi trước bàn ăn ngập tràn các tảng thịt nướng, xúc xích và xương đùi, hai tay cầm dao nĩa, bụng phình to tròn vo miệng vẫn đang nhồm nhoàm nhai.'}, {'id': 'L40', 'quote': 'Tốc độ trao đổi chất của nó nhanh đến mức điên cuồng để duy trì thân nhiệt giữa cái lạnh âm bốn mươi độ C...', 'prompt': 'HÀI HƯỚC: Trong bụng Chồn Gulo là một lò luyện than rực lửa bốc khói nghi ngút, các bánh răng động cơ đốt trong quay tít mù để giữ nhiệt độ cho cơ thể.'}, {'id': 'L41', 'quote': 'Để không bị chết đói, nó biến cả khu rừng tuyết thành một chuỗi tủ lạnh siêu thị: bất cứ con mồi nào ăn không hết, nó xé nhỏ ra rồi chôn sâu...', 'prompt': 'GIỮA: Khu rừng tuyết có các hốc băng được đánh số như các ngăn của tủ lạnh siêu thị, bên trong chứa các gói thịt nai được bọc tuyết cất giữ ngăn nắp.'}, {'id': 'L42', 'quote': 'Nhưng chính cái nết ăn như hổ đó khiến nó luôn trong trạng thái cáu kỉnh, gắt gỏng như người bị hạ đường huyết suốt hai mươi bốn trên bảy!...', 'prompt': 'GIỮA: Chồn Gulo mặt mày cau có nhăn nhó, trán nổi gân chữ thập đỏ, hai tay ôm bụng réo ùng ục, miệng gầm gừ cáu bẳn với một bông hoa tuyết vô tội.'}, {'id': 'L43', 'quote': 'Và điểm yếu bi hài nhất của Chồn Gu-lô chính là bản tính cô độc đến mức cực đoan!...', 'prompt': "BẢN ĐỒ LÃNH THỔ: Một vùng lãnh thổ rộng lớn 1.500km² có rào chắn gai nhọn bao quanh, ở chính giữa là Chồn Gulo ngồi một mình trên tảng đá cắm biển: 'CẤM BƯỚC VÀO!'."}, {'id': 'L44', 'quote': 'Ngay cả với đồng loại cùng loài, khuôn mặt chú ta lúc nào cũng nhăn nhó, cau có như mất sổ gạo!...', 'prompt': 'GIỮA: Hai con Chồn Gulo tình cờ gặp nhau trên đường mòn tuyết, cả hai cùng trừng mắt lườm nguýt, giơ nắm đấm và quay ngoắt lưng lại phùng phỉu bỏ đi.'}, {'id': 'L45', 'quote': 'Chúng chỉ gặp nhau đúng vài ngày ngắn ngủi trong năm để duy trì nòi giống, rồi lập tức quay lưng bỏ chạy...', 'prompt': 'HÀI HƯỚC: Chồn đực và chồn cái sau khi gặp nhau chớp nhoáng lập tức cắm đầu chạy thục mạng về hai hướng ngược nhau, để lại vệt bụi tuyết dài sau lưng.'}, {'id': 'L46', 'quote': 'Một chiến binh vô địch thiên hạ, nhưng cả cuộc đời chỉ lủi thủi độc hành giữa rừng tuyết hoang vu không một bóng bạn bè!...', 'prompt': 'CẢNH BUỒN HÀI: Chồn Gulo ngồi cô đơn trên mỏm đá tuyết nhìn trăng tròn mùa đông, thở dài tạo thành làn khói trắng, bên cạnh là một người tuyết do nó tự nặn để làm bạn.'}, {'id': 'L47', 'quote': 'Dù cả đời liều mạng đánh nhau với gấu và sói để bảo vệ miếng ăn, nhưng Chồn Gu-lô lại cực kỳ cưng chiều đàn con của mình!...', 'prompt': 'ẤM ÁP: Chồn bố Gulo đang dùng lưng cõng hai chú chồn con lông xù đáng yêu đi dạo trên nền tuyết trắng, ánh mắt bố dịu dàng khác hẳn vẻ cục súc thường ngày.'}, {'id': 'L48', 'quote': 'Chồn bố thỉnh thoảng vẫn quay lại thăm đàn con nhỏ, dẫn chúng đi săn và dạy chúng kỹ năng bẻ xương tuyết...', 'prompt': 'GIỮA: Chồn bố đang cầm que hướng dẫn ba chú chồn con tập bẻ một mẩu xương nhỏ, các bé chồn chăm chú lắng nghe và bắt chước rất ngộ nghĩnh.'}, {'id': 'L49', 'quote': 'Đúng là giang hồ xứ tuyết cũng có lúc yếu lòng!...', 'prompt': 'GIỮA: Chồn bố quay mặt đi lau một giọt nước mắt xúc động nhỏ giọt, trong khi tay vẫn nắm chặt tay chồn con, tạo sự tương phản cực kỳ đáng yêu.'}, {'id': 'L50', 'quote': 'Tại Vườn quốc gia Yên-lâu-xtôn ở Mỹ, các nhà nghiên cứu từng ghi nhận một thước phim chấn động: một con Chồn Gu-lô nặng chưa đầy mười lăm ki-lô-gam...', 'prompt': 'GIỮA: Một ống kính máy quay phim tài liệu thực địa hướng vào bối cảnh rừng thông tuyết Yellowstone, ghi lại cảnh Chồn Gulo đứng đối diện Gấu Xám khổng lồ.'}, {'id': 'L51', 'quote': 'Chú chồn nhỏ không hề lùi bước, xù toàn bộ lông lên, nhe hàm răng kìm sắt gầm gừ những tiếng rít chói tai và lao tới đớp thẳng vào mõm gấu khổng lồ!...', 'prompt': 'CẢNH HÀNH ĐỘNG: Chồn Gulo nhảy chồm lên không trung, nhe nanh đớp thẳng vào chóp mũi con Gấu Xám to xác đang hoảng hốt lùi lại ngửa đầu ra sau.'}, {'id': 'L52', 'quote': 'Bị tấn công bất ngờ bởi một kẻ điên không sợ chết kèm theo mùi hôi nồng nặc bốc lên, con gấu xám khổng lồ nặng gấp hai mươi lần chỉ biết gầm gừ khó chịu rồi lùi lũi bỏ đi!...', 'prompt': 'BÊN TRÁI: Chồn Gulo 15kg đứng giơ hai tay đắc thắng bên xác nai; BÊN PHẢI: Con gấu xám Grizzly 300kg cụp tai, lầm lũi quay đít bước đi với vẻ mặt ngao ngán.'}, {'id': 'L53', 'quote': 'Chưa dừng lại ở đó, tại vùng lãnh nguyên A-lát-xka, người ta từng chứng kiến cảnh một con Chồn Gu-lô đơn độc đánh bật ba con sói xám to lớn khỏi miếng mồi!...', 'prompt': 'GIỮA: Chồn Gulo đứng ở tâm vòng tròn nhe nanh xù lông gầm thét dữ dội; xung quanh là ba con sói xám to lớn đang chùn bước, e dè không dám áp sát.'}, {'id': 'L54', 'quote': 'Sói xám nổi tiếng với chiến thuật bầy đàn thông minh, nhưng đứng trước một gã lùn vừa cắn đau, vừa hôi thối, lại vừa lăn xả như cảm tử quân...', 'prompt': 'BÊN TRÁI: Ba con sói xám quay đầu rút lui, một con ngoái đầu lại nhìn với ánh mắt sợ hãi; BÊN PHẢI: Chồn Gulo chống nạnh ngoác miệng cười chế giễu.'}, {'id': 'L55', 'quote': 'Một nghiên cứu nổi tiếng khác theo dõi chú chồn mang mã số M-ba tại bang Mông-ta-na đã khiến giới khoa học ngả mũ...', 'prompt': "GIỮA: Chú chồn Gulo đeo vòng cổ định vị GPS nhỏ có mã số 'M3', đang đứng hiên ngang trên vách đá ngắm nhìn đỉnh núi tuyết cao chọc trời."}, {'id': 'L56', 'quote': 'Trong vòng chín mươi phút, chú ta đã leo thẳng đứng lên đỉnh núi Mông Cờ-li-vơ-lân cao hơn ba ngàn một trăm mét phủ đầy băng tuyết dựng đứng!...', 'prompt': 'TOÀN CẢNH: Ngọn núi Mount Cleveland cao 3.100m dốc đứng phủ đầy băng tuyết; một đường leo dốc đứng có mũi tên đỏ chỉ tốc độ 90 phút lên tận đỉnh chóp.'}, {'id': 'L57', 'quote': 'Các vận động viên leo núi chuyên nghiệp phải mất cả ngày trời với đầy đủ dây bảo hiểm và rìu băng, còn chú ta chỉ coi đó là một buổi đi dạo buổi sáng...', 'prompt': 'BÊN TRÁI: Hai vận động viên leo núi người thở dốc bám dây thừng rìu băng; BÊN PHẢI: Chồn Gulo đang ung dung cắn tảng thịt trên đỉnh núi tuyết ngắm bình minh.'}, {'id': 'L58', 'quote': 'Nhìn lại hành trình sinh tồn của Chồn Gu-lô giữa vùng địa đầu băng giá, chúng ta nhận ra một bài học sâu sắc: Kích thước cơ thể hay hoàn cảnh xuất phát điểm chưa bao giờ là yếu tố quyết định...', 'prompt': 'Ý NGHĨA: Chồn Gulo nhỏ bé đứng trên mỏm đá tuyết cao, bóng của chú ta in xuống nền tuyết lại là hình bóng một con sư tử dũng mãnh đội vương miện.'}, {'id': 'L59', 'quote': 'Sinh ra với thân hình nhỏ bé giữa một vùng đất ngập tràn những kẻ săn mồi khổng lồ, Chồn Gu-lô không chọn cách ẩn nấp sợ sệt, mà tự tôi luyện cho mình sức chịu đựng phi thường...', 'prompt': 'GIỮA: Chồn Gulo đang hăng say tập luyện: một tay chống đẩy trên tuyết lạnh, một tay cầm tạ đá, mặt kiên định không ngại gian khó.'}, {'id': 'L60', 'quote': 'Nó biến cái lạnh chết người thành chiếc tủ lạnh bảo quản thức ăn, và biến sự nhỏ bé thành vũ khí cơ động lướt trên tuyết!...', 'prompt': 'GIỮA: Chồn Gulo mỉm cười tự tin đứng giữa tâm bão tuyết, gió lốc băng giá thổi qua nhưng chú ta đứng vững như bàn thạch.'}, {'id': 'L61', 'quote': 'Trong cuộc sống cũng vậy: Khi bạn dám đương đầu với những nghịch cảnh lớn hơn bản thân gấp nhiều lần và kiên trì bước tiếp mỗi ngày, cả thế giới sẽ phải nghiêng mình nhường bước...', 'prompt': 'TRUYỀN CẢM HỨNG: Chồn Gulo bước đi hiên ngang trên con đường tuyết trắng hướng về ánh mặt trời rực rỡ, để lại dấu chân vững chãi phía sau.'}, {'id': 'L62', 'quote': 'Nếu được chọn giữa sức mạnh thể lực bền bỉ leo núi không biết mệt của Chồn Gu-lô và cú đấm nóng ngang Mặt Trời của Tôm Tít ở tập trước, bạn sẽ chọn siêu năng lực nào?...', 'prompt': 'BÊN TRÁI: Chồn Gulo leo núi tuyết hùng dũng; BÊN PHẢI: Tôm Tít (Tập 7) tung cú đấm quyền anh phát sáng rực rỡ; ở giữa là dấu hỏi chấm vàng to kích thích khán giả bình luận.'}, {'id': 'L63', 'quote': 'Đừng quên bấm Đăng ký kênh và chuông thông báo để không bỏ lỡ Tập chín: Chim Cánh Cụt — Đằng sau dáng đi lạch bạch dễ thương là những màn giao dịch đen tối nhất Nam Cực!...', 'prompt': 'TEASER TẬP 9: Một chú Chim Cánh Cụt Nam Cực lạch bạch dễ thương nhưng đeo kính râm đen bí hiểm, tay cầm một viên sỏi lấp lánh như đang làm giao dịch ngầm trên tảng băng trôi.'}, {'id': 'L64', 'quote': 'Hẹn gặp lại các bạn trong cuộc phiêu lưu tiếp theo!...', 'prompt': 'KẾT THÚC: Chồn Gulo tươi cười giơ tay vẫy chào khán giả, bên cạnh là biểu tượng nút Đăng Ký (Subscribe) và chiếc Chuông thông báo vẽ tay phong cách comic whiteboard.'}]
```
</details>

<details><summary>shorts</summary>

```text
[{'id': 'S01', 'quote': 'Nặng vỏn vẹn mười lăm ki-lô-gam nhưng dám lao vào cướp mồi của một con Gấu Xám nặng ba trăm ki-lô-gam!', 'prompt': '9:16 DỌC. BÊN TRÊN: Con Gấu Xám Grizzly 300kg to lớn hoảng hốt; BÊN DƯỚI: Chồn Gulo 15kg nhỏ bé xông thẳng vào cướp tảng thịt trên tuyết trắng.'}, {'id': 'S02', 'quote': 'Kẻ điên rồ bậc nhất xứ tuyết phương Bắc chính là Chồn Gu-lô, hay còn gọi là Uân-vơ-rin!', 'prompt': '9:16 DỌC. GIỮA: Chồn Gulo đứng dạng chân chống nạnh, xòe móng vuốt sắc nhọn, biểu cảm cực ngầu như siêu anh hùng Người Sói Wolverine.'}, {'id': 'S03', 'quote': 'Với bốn bàn chân bè rộng như đôi ủng trượt tuyết, gã tí hon này lướt nhẹ trên tuyết mềm trong khi những con mồi khổng lồ sa lầy bất lực!', 'prompt': '9:16 DỌC. BÊN DƯỚI: Nai sừng tấm to lớn lún ngập bụng trong tuyết; BÊN TRÊN: Chồn Gulo lướt nhẹ nhàng trên tuyết như trượt patin.'}, {'id': 'S04', 'quote': 'Bộ lông kỵ nước không bao giờ đông đá ở âm bốn mươi độ C, và chiếc răng hàm trên xoay ngang chín mươi độ hoạt động như kìm cộng lực...', 'prompt': '9:16 DỌC. CẬN CẢNH: Hàm răng Chồn Gulo với chiếc răng hàm xoay 90 độ bẻ đôi chiếc xương đóng băng, băng tuyết văng tung tóe.'}, {'id': 'S05', 'quote': 'Nó có thể chạy liên tục bảy mươi cây số qua vách núi dựng đứng...', 'prompt': '9:16 DỌC. TOÀN CẢNH DỌC: Chồn Gulo đang chạy phăng phăng leo thẳng lên vách núi tuyết dựng đứng dốc 90 độ một cách phi thường.'}, {'id': 'S06', 'quote': 'Và khi bị bao vây, nó sẽ phun ra luồng mùi hôi thối kinh hoàng khiến cả bầy sói cũng phải ôm mũi bỏ chạy!', 'prompt': '9:16 DỌC. BÊN TRÊN: Ba con sói lấy chân bịt mũi bỏ chạy tán loạn; BÊN DƯỚI: Chồn Gulo chổng đuôi xịt khói hôi mù mịt.'}, {'id': 'S07', 'quote': 'Nhưng nghịch lý hài hước là gã chiến binh bất bại này lại cô độc đến phát khóc, cả đời chỉ lủi thủi một mình vì tính tình quá cộc cằn!', 'prompt': '9:16 DỌC. GIỮA: Chồn Gulo ngồi co ro một mình trên mỏm đá tuyết nhìn trăng đêm, mặt cau có khó chịu nhưng đầy cô đơn.'}, {'id': 'S08', 'quote': 'Bạn muốn biết chú ta đã đuổi gấu xám cướp mồi như thế nào?', 'prompt': '9:16 DỌC. GIỮA: Mũi tên cong vẽ tay to màu đỏ chỉ thẳng xuống phía dưới màn hình (nơi có nút xem video dài liên quan).'}, {'id': 'S09', 'quote': 'Bấm xem ngay video dài Tập tám bên dưới kênh nhé!', 'prompt': '9:16 DỌC. GIỮA: Poster hoạt hình thu nhỏ của Tập 8 với hình Chồn Gulo và Gấu Xám, kèm bàn tay chỉ xuống nút link.'}, {'id': 'S10', 'quote': 'Nối vòng lặp: Nặng vỏn vẹn mười lăm ki-lô-gam nhưng dám lao vào cướp mồi của một con Gấu Xám...', 'prompt': '9:16 DỌC. GIỮA: Chồn Gulo há miệng gầm gừ lao vút về phía trước tiếp nối cú đấm cướp mồi (khớp hoàn hảo về giây 0:00).'}]
```
</details>

<details><summary>thumbnail</summary>

```text
{'id': 'T01', 'prompt': 'Tạo một ảnh thumbnail YouTube tỉ lệ 16:9 ngang (1920x1080), phong cách comic 2D hoạt hình, nét viền đen đậm, màu phẳng rực rỡ, tương phản rất mạnh, giống thumbnail kênh khoa học vui nhộn. BỐ CỤC: Bên TRÁI phía trên là tiêu đề chữ IN HOA tiếng Việt rất lớn, 2 dòng, màu vàng gradient viền đen cực dày, có bóng đổ: dòng 1 "NẶNG 15KG", dòng 2 "CƯỚP MỒI GẤU XÁM?!" (viết đúng chính tả và đúng dấu tiếng Việt). Góc trên cùng bên trái là huy hiệu comic hình nổ màu đỏ viền vàng ghi chữ "TẬP 8". Bên PHẢI và GIỮA là nhân vật chính: Chú Chồn Gulo (Wolverine) thân hình lùn mập chắc nịch, lông nâu sẫm sọc vàng kem, bàn chân to xòe móng vuốt sắc nhọn, mặt cực kỳ hung hăng, gầm gừ tự tin ngông nghênh, một tay giơ tảng thịt nai tươi, đang quát đuổi đối thủ. Phía sau bên trái là một con Gấu Xám Grizzly khổng lồ to gấp 20 lần đang hoảng hốt toát mồ hôi, cụp tai lùi bước. Nền: Rừng thông tuyết Taiga màu xanh đậm với các tia sáng tỏa ra kiểu sunburst comic phía sau nhân vật. Ít chi tiết, nhân vật to rõ, đọc được rõ ở kích thước nhỏ. Không có chữ nào khác ngoài "TẬP 8" và tiêu đề.'}
```
</details>

## 7. SEO

- **title:** Nặng 15kg Dám Cướp Mồi Của Cả Đàn Sói Và Gấu Xám?! | Chồn Gulo | Tập 8
- **hook_paragraph:** Chồn Gulo (Wolverine) chỉ nặng 15kg nhưng sở hữu lá gan to nhất thế giới động vật: răng hàm xoay 90 độ nghiền nát xương đông lạnh, chân như ủng trượt tuyết và dám đơn độc lao vào cướp mồi của Gấu Xám 300kg! Khám phá bí mật sinh tồn của chiến binh bất tử xứ tuyết.
- **question:** Nếu phải đối đầu giữa Chồn Gulo 15kg liều mạng và Gấu Xám 300kg trên núi tuyết, bạn sẽ chọn ai? Bình luận bên dưới nhé!
- **next_teaser:** Chim Cánh Cụt — Đằng sau dáng đi lạch bạch dễ thương là những màn giao dịch đen tối nhất Nam Cực
- **shorts_title:** Nặng 15kg Đuổi Cả Gấu Xám 300kg Khỏi Bữa Ăn?! ❄️ #shorts #chongulo
- **shorts_desc:** Chồn Gulo (Wolverine) chỉ nặng 15kg nhưng dám cướp mồi của gấu xám 300kg và cả bầy sói nhờ chiếc răng hàm xoay 90 độ bẻ xương đông lạnh! ❄️
👉 Xem bản đầy đủ vụ đại chiến xứ tuyết — video Tập 8 trên kênh Vẽ Chuyện Hoang Dã.

#shorts #ChonGulo #Wolverine #TheGioiDongVat #VeChuyenHoangDa #KhoaHoc
- **bullets:** Chiếc răng hàm carnassial xoay 90 độ bẻ vụn xương đông cứng ở -50°C · Bàn chân cấu trúc ủng trượt tuyết snowshoes lướt trên tuyết lún · Tuyến xạ hôi Skunk Bear khiến gấu xám và bầy sói bỏ chạy ngán ngẩm · Sức bền quái vật: chạy 70km/ngày và leo đỉnh núi tuyết 3.100m trong 90 phút
- **tags:** chồn gulo, chon gulo, wolverine, gulo gulo, người sói ngoài đời thực, chồn gấu hôi, skunk bear, gấu xám grizzly, thế giới động vật, động vật kỳ lạ, vẽ chuyện hoang dã, whiteboard animation, khoa học thú vị, băng tuyết bắc cực, sinh tồn hoang dã
- **hashtags:** #ChonGulo #Wolverine #TheGioiDongVat #VeChuyenHoangDa #KhoaHoc

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-08-chon-gulo
python src/episode/pipeline.py tts    projects/tap-08-chon-gulo     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-08-chon-gulo     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-08-chon-gulo     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-08-chon-gulo              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-08-chon-gulo --force
python scripts/beat_sheet.py projects/tap-08-chon-gulo               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-08-chon-gulo/audio/shorts.wav projects/tap-08-chon-gulo/renders/tap-08-chon-gulo_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-08-chon-gulo
python src/episode/pipeline.py seo    projects/tap-08-chon-gulo
python src/episode/episode_doc.py     projects/tap-08-chon-gulo
```
