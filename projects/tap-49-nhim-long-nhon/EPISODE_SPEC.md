# TẬP 49 — NHÍM LÔNG NHỌN · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-49-nhim-long-nhon`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-49-nhim-long-nhon`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F2` · **Persona giọng:** `ky_su_vu_khi` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Nhím Lông Nhọn |
| Tiêu đề YouTube | Bí Mật 30.000 Mũi Tên Nhím: Tự Rút Sâu Vào Thịt Hạ Gục Báo Hoa Mai?! \| Tập 49 |
| Video dài | `renders/tap-49-nhim-long-nhon_long.mp4` — 10:05.3 (605.3s) |
| Shorts | `renders/tap-49-nhim-long-nhon_shorts.mp4` — 0:49.0 (49.0s) |
| Thumbnail | `renders/tap-49-nhim-long-nhon_thumbnail.jpg` |
| Số hình | dài 53 beat / 53 ảnh riêng; Shorts 9 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.12**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/53 của video YouTube về Nhím Lông Nhọn). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa vẽ tay đặc trưng cho chủ đề, nét mực sắc nét, màu sắc tương phản cuốn hút, tối giản giàu tính biểu tượng khoa học; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú nhím lông nhọn Bắc Mỹ hoạt hình ngộ nghĩnh (lưng mang bộ giáp 30.000 gai nhọn đính ngạnh ngược, biểu cảm tự tin đắc thắng). 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — BẢN VẼ PHÁO ĐÀI RẢI GAI SỐNG
*Thẻ chương:* PHÁO ĐÀI GAi TỰ ĐỘNG BỎNG MÔN

*Badge:* `SƠ ĐỒ VŨ KHÍ` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene01_p0.wav` (881 ký tự) · mood `tram_bi_an`

```text
Chào mừng toàn thể các chuyên gia vũ khí đạn đạo và các kỹ sư sinh học đã quay trở lại với xưởng giải mã công nghệ quốc phòng tự nhiên! Hãy nhìn vào buồng thử nghiệm vật liệu đằng kia xem, một cỗ máy bọc thép sinh học nhỏ gọn nặng vỏn vẹn mười ki-lô-gam đang lững thững bước đi với vẻ bất cần đời. Nó không cần hàm răng nanh sắc nhọn như hổ dữ, cũng chẳng cần tốc độ bứt phá bốn mươi cây số một giờ như linh dương. Toàn bộ lưng và đuôi của nó được bọc kín bởi một kho vũ khí di động gồm ba mươi ngàn mũi tên chết chóc. Dân gian gọi nó là Nhím Lông Nhọn, nhưng trên bàn thiết kế đạn đạo quân sự của chúng tôi, đây đích thị là Pháo Đài Tự Hành sở hữu công nghệ bẫy chông phản công tàn khốc nhất từng được ghi nhận trong lịch sử! Mỗi bước đi của nó chậm rãi, ung dung và điềm tĩnh như thể toàn bộ thế giới dã thú ngoài kia chẳng có lấy một thứ gì đủ tư cách làm nó phải bận tâm lo sợ.
```
**Part 1** → `audio/vs/scene01_p1.wav` (118 ký tự) · 🎭 cameo `co_tro_ly`

```text
Báo cáo chỉ huy trưởng, phim hoạt hình thường vẽ con nhím này có thể bắn lông vèo vèo như cung tên từ xa đúng không ạ?
```
**Part 2** → `audio/vs/scene01_p2.wav` (805 ký tự) · mood `hao_hung`

```text
[laughter] Một quan niệm sai lầm kinh điển suốt nhiều thế kỷ đấy cô trợ lý ơi! [surprise-oh] Pháo Đài Tự Hành hoàn toàn không hề có cơ chế lò xo hay khí nén nào để phóng lông từ xa như những mũi tên bắn tỉa. Nhưng cơ chế thực tế của nó còn nguy hiểm gấp vạn lần trò bắn tỉa vu vơ ấy! Lông của nó là những chiếc mũi lao ngạnh ngược thụ động, chỉ cần chạm khẽ là tự tách gốc và tự động di chuyển sâu vào thớ thịt của kẻ địch như một mũi khoan cơ học tự động. Ngay bây giờ, hãy đeo kính bảo hộ và cùng chúng tôi đưa một chiếc lông nhím lên kính hiển vi điện tử quét để bóc trần bí mật cơ khí vi mô này! Chỉ cần một kẻ đi săn dại dột đưa mõm lại gần ngửi ngửi, chiếc đuôi ngắn ngủn nặng trịch của nó sẽ quất ra một cú chớp nhoáng khiến hàng trăm mũi giáo cắm phập vào mũi đối phương trong sự ngỡ ngàng tột độ.
```

### scene02 — CÔNG NGHỆ NGẠNH MÓC MICROSCOPIC
*Thẻ chương:* LƯỠI LAO XUYÊN THỦNG VÀ KHÓA CHẶT

*Badge:* `VI NGẠNH NGƯỢC SEM` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene02_p0.wav` (668 ký tự) · mood `hao_hung`

```text
Dưới độ phóng đại hàng ngàn lần của kính hiển vi điện tử quét SEM, phần đầu của chiếc lông nhím dài ba mươi xăng-ti-mét này không hề trơn nhẵn như một cây kim may vá thông thường. Ở khoảng bốn mi-li-mét ngoài cùng phần mũi nhọn, bề mặt được bao phủ bởi từ bảy trăm đến tám trăm vẩy ngạnh ngược microscopic xếp lớp gối lên nhau giống hệt như vẩy cá hay những chiếc mũi móc câu sắc lẹm. Các nhà khoa học vật liệu tại Đại học Harvard đã phát hiện ra một điều kỳ diệu làm chấn động giới kỹ thuật cơ khí quốc tế! Những chiếc vẩy ngạnh này có kích thước siêu nhỏ chỉ khoảng mười đến hai mươi mi-crô-mét, xếp nghiêng một góc bốn mươi lăm độ hoàn hảo hướng về phía chuôi lông.
```
**Part 1** → `audio/vs/scene02_p1.wav` (103 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Trời ơi kính hiển vi phóng to nhìn gai góc ghê rợn quá, trông y như bầy dao găm thu nhỏ vậy các bác ơi!
```
**Part 2** → `audio/vs/scene02_p2.wav` (723 ký tự) · mood `don_dap`

```text
Khi đâm vào da thịt kẻ thù, các lớp ngạnh ngược này nép chặt vào thân lông theo chiều xuôi, hoạt động như những lưỡi dao rọc thu nhỏ tập trung ứng suất vào một điểm cực hẹp. Nhờ cơ chế thông minh này, lực cần thiết để chiếc lông đâm thủng lớp da dày của thú dữ giảm tới năm mươi tư phần trăm so với một cây kim thép y tế thông thường! Tức là chỉ cần một cú quất nhẹ từ chiếc đuôi của Pháo Đài Tự Hành, hàng chục mũi tên đã dễ dàng cắm sâu xuyên qua da thịt đối phương mà hầu như không gặp phải bất kỳ lực cản đáng kể nào. Cơ chế tập trung ứng suất này làm cho các mô thịt xung quanh bị rẽ sang hai bên một cách êm ái mà không bị dập nát, giúp mũi tên lướt vào bên trong sâu thẳm như một nhát dao rọc giấy đi qua lớp bơ mềm.
```
**Part 3** → `audio/vs/scene02_p3.wav` (725 ký tự) · mood `hao_hung`

```text
Nhưng bi kịch thực sự chỉ bắt đầu khi con thú săn mồi tìm cách nhổ chiếc lông ra! Ngay khoảnh khắc có lực kéo ngược ra ngoài, hàng trăm chiếc vẩy ngạnh ngược lập tức xòe bung ra và móc chặt vào các thớ cơ thịt xung quanh. Lực cần thiết để rút chiếc lông này ra tăng vọt lên gấp ba lần so với lực đâm vào! Càng cố giật mạnh, các ngạnh móc càng xé toạc mô thịt, gây ra cơn đau đớn tột cùng và chảy máu dữ dội, biến chiếc lông thành một chiếc neo sắt vĩnh viễn khóa chặt bên trong cơ thể con mồi. Đây chính là nguyên lý của lưỡi câu cá cổ xưa nhưng đã được tự nhiên hoàn thiện đến cấp độ hiển vi phân tử, khiến mọi nỗ lực dùng móng vuốt hay cọ mõm vào gốc cây của con thú chỉ làm chiếc lông bị gãy thân và cắm chặt hơn vào thịt.
```

### scene03 — MŨI KHOAN SINH HỌC DI ĐỘNG
*Thẻ chương:* ĐI XUYÊN TIM PHỔI BÁO HOA MAI

*Badge:* `CƠ CHẾ TỰ RÚT SÂU` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene03_p0.wav` (770 ký tự) · mood `don_dap`

```text
Bây giờ mới là cơ chế sát thương tinh vi và tàn độc nhất khiến loài báo hoa mai và sư tử châu Phi phải kinh hồn bạt vía. Sau khi chiếc lông cắm vào thịt và gãy gốc, nó không hề nằm yên một chỗ. Các chuyển động co bóp cơ bắp tự nhiên của con thú săn mồi khi di chuyển hay thở sẽ vô tình kích hoạt hệ thống bánh cóc một chiều của các ngạnh ngược. Do các ngạnh chỉ cho phép chiếc lông trượt theo chiều tiến lên mà không thể tụt lùi, mỗi cú co cơ của con vật bị nạn sẽ đẩy chiếc lông nhọn tự rút sâu hơn vào bên trong với tốc độ khoảng một mi-li-mét mỗi giờ! Đây chính là cơ chế bánh cóc sinh học tự nhiên tinh xảo nhất từng được phát hiện trên cơ thể sinh vật, biến chính năng lượng cử động của nạn nhân thành động cơ đẩy đưa vũ khí hủy diệt vào sâu trong lục phủ ngũ tạng.
```
**Part 1** → `audio/vs/scene03_p1.wav` (94 ký tự) · 🎭 cameo `be_con`

```text
Ủa các bác kỹ sư ơi, vậy nếu bị cắm vào mõm thì chiếc lông đó sẽ chui đi đâu mất tiêu luôn hả?
```
**Part 2** → `audio/vs/scene03_p2.wav` (760 ký tự) · mood `hao_hung`

```text
[laughter] Câu hỏi rất hay của bé con đấy! [surprise-oh] Chiếc lông nhọn sẽ từ từ xuyên thủng các lớp cơ má, đâm xuyên qua vòm họng, thậm chí di chuyển sâu vào trong lồng ngực làm thủng phổi hoặc đâm rách tâm thất của tim! Đã có rất nhiều ghi nhận thực địa về những con báo hoa mai trưởng thành khỏe mạnh bị chết đói thảm khốc chỉ vì vài chiếc lông nhím cắm sâu vào hàm dưới làm nhiễm trùng mưng mủ, khiến miệng sưng to biến dạng không thể nào há ra để nhai thịt được nữa. Một đòn trả đũa tàn nhẫn được lập trình để kết liễu kẻ săn mồi sau nhiều ngày hành hạ! Những kẻ săn mồi khát máu như báo sư tử hay chó sói đồng cỏ một khi dính phải bẫy chông này thường phải trải qua những tuần lễ đau đớn tột cùng trước khi bị cướp đi hơi thở cuối cùng trong sự bất lực.
```
**Part 3** → `audio/vs/scene03_p3.wav` (654 ký tự) · mood `don_dap`

```text
Đặc biệt hơn nữa, phần gốc của lông nhím nối với nang lông rất lỏng lẻo. Lớp màng cơ dưới da của Pháo Đài Tự Hành có khả năng chủ động co thắt để dựng đứng toàn bộ ba mươi ngàn mũi tên lên khi bị đe dọa, tạo ra tiếng xào xạc đanh thép cảnh báo. Khi kẻ địch chạm phải, các sợi lông này sẽ tự động tách rời khỏi gốc một cách êm ái, chuyển giao toàn bộ gánh nặng vũ khí sang cơ thể đối thủ mà không làm tổn thương dù chỉ một tế bào biểu bì của chú nhím! Hệ thống cơ dựng lông này được điều khiển bởi các xung thần kinh cực kỳ nhạy bén, chỉ mất chưa đầy không phẩy một giây để chuyển từ trạng thái nằm xuôi sang tư thế pháo đài xòe gai sẵn sàng nghênh chiến.
```

### scene04 — THUỐC KHÁNG SINH QUÉT TRÊN MŨI TÊN
*Thẻ chương:* TỰ CHỮA LÀNH KHI NGÃ CÂY

*Badge:* `LỚP MỠ KHÁNG SINH` · *mood mặc định:* `nghiem_trang_gia`

**Part 0** → `audio/vs/scene04_p0.wav` (680 ký tự) · mood `nghiem_trang_gia`

```text
Có một nghịch lý kỹ thuật vô cùng hóc búa được đặt ra cho ban thiết kế sinh học: Nếu mang trên mình ba mươi ngàn mũi tên chết chóc có ngạnh ngược nguy hiểm như vậy, làm thế nào để Pháo Đài Tự Hành không vô tình tự đâm chết chính mình trong những sinh hoạt hàng ngày? Loài nhím này rất thích leo trèo lên những cành cây cao để gặm vỏ cây non và ăn quả ngọt, nhưng chúng lại nổi tiếng là những kẻ vụng về, thường xuyên bị trượt chân và ngã từ trên ngọn cây cao chót vót xuống mặt đất đá lởm chởm. Trọng lượng mười ki-lô-gam với đôi chân ngắn cũn cỡn khiến những bước leo trèo trên các cành cây sồi hay phong cao vút luôn tiềm ẩn rủi ro té ngã cực kỳ cao đối với cỗ máy bọc thép này.
```
**Part 1** → `audio/vs/scene04_p1.wav` (746 ký tự) · mood `hao_hung`

```text
Khi ngã từ trên cao xuống, không ít lần những chiếc lông nhọn của chính nó bị gãy gập và đâm ngược vào đùi hoặc bụng của nó. Nhưng kỳ diệu thay, các vết thương này hầu như không bao giờ bị nhiễm trùng hay mưng mủ! Các nhà hóa sinh học phát hiện ra rằng, bao phủ bên ngoài mỗi chiếc lông nhím là một lớp màng axit béo tự nhiên đậm đặc, chứa các hợp chất kháng khuẩn cực mạnh có khả năng tiêu diệt hoàn toàn các loại vi khuẩn gram dương nguy hiểm. Lớp mỡ kháng sinh này hoạt động như một loại thuốc mỡ bôi vết thương được quét sẵn lên từng mũi tên! Lớp mỡ kháng khuẩn này gồm hỗn hợp các chuỗi axit béo tự do phức tạp, có khả năng ức chế màng tế bào của các loại vi khuẩn nguy hiểm nhất như tụ cầu vàng hay liên cầu khuẩn trong môi trường tự nhiên.
```
**Part 2** → `audio/vs/scene04_p2.wav` (652 ký tự) · mood `hao_hung`

```text
Khi chiếc lông đâm vào chính cơ thể nó, lớp mỡ kháng khuẩn lập tức khử trùng vết thương tại chỗ, giúp mô thịt tự co lại và phục hồi nhanh chóng mà không gây nguy hiểm tính mạng. Thiên nhiên không chỉ trang bị cho Pháo Đài Tự Hành một kho vũ khí công phá hàng đầu, mà còn chu đáo dán sẵn tem bảo hiểm y tế tự động cho người sử dụng, đảm bảo tính an toàn tuyệt đối cho người lính mang vũ khí trong mọi tình huống rủi ro nghề nghiệp! Nhờ có lớp lá chắn hóa học này, những con nhím dù bị hàng chục vết đâm thủng do chính lông của mình gây ra khi rơi từ độ cao mười mét vẫn thong thả đứng dậy, phủi bụi và tiếp tục kiếm ăn như chưa từng có chuyện gì xảy ra.
```

### scene05 — KIẾN TRÚC VẬT LIỆU COMPOSITE
*Thẻ chương:* BẬP BỀNH NHƯ PHAO CỨU SINH

*Badge:* `LÕI XỐP BỌC THÉP` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene05_p0.wav` (617 ký tự) · mood `hao_hung`

```text
Hãy cầm một nắm lông nhím lên tay và các bạn sẽ phải kinh ngạc trước trọng lượng của chúng! Ba mươi ngàn mũi tên bọc kín toàn thân nhưng tổng khối lượng của chúng chỉ chiếm chưa đầy năm phần trăm trọng lượng cơ thể chú nhím. Nếu những chiếc lông này là những thanh xương đặc cứng, Pháo Đài Tự Hành sẽ bị đè bẹp dí dưới sức nặng của chính mình và không thể nào nhấc nổi bốn chân để di chuyển. Bí quyết nằm ở cấu trúc vật liệu rỗng bên trong thân lông! Một chuẩn mực trọng lượng vàng mà các kỹ sư chế tạo áo giáp chống đạn quân sự hiện đại luôn khao khát đạt được nhưng vẫn chưa thể tối ưu hóa trọn vẹn như thiên nhiên.
```
**Part 1** → `audio/vs/scene05_p1.wav` (686 ký tự) · mood `don_dap`

```text
Cắt ngang thân của một chiếc lông, chúng ta sẽ thấy một lớp vỏ ngoài bằng chất sừng keratin cực kỳ cứng cáp và chịu lực uốn nắn tuyệt vời. Nhưng bên trong lòng ống lại là một ma trận bọt xốp khí rỗng li ti, đan xen nhau theo cấu trúc tổ ong tổ mối. Cấu trúc composite này vừa tối ưu hóa độ cứng chống cong vênh khi va đập, vừa biến từng chiếc lông thành một khoang chứa khí tí hon. Nhờ có hàng chục ngàn khoang khí này, chú nhím khi rơi xuống nước sẽ nổi bồng bềnh như một chiếc phao cứu sinh tự nhiên! Tỷ trọng của mỗi chiếc lông chỉ đạt khoảng không phẩy ba gam trên một xăng-ti-mét khối, nhẹ hơn cả gỗ bấc và hoàn toàn nổi trên mặt nước mà không cần bất kỳ sự hỗ trợ cơ học nào khác.
```
**Part 2** → `audio/vs/scene05_p2.wav` (487 ký tự) · mood `hao_hung`

```text
Nó có thể thong thả bơi qua những con sông lớn mà không sợ bị chìm nghỉm, vừa có thể xòe gai đẩy lùi lũ cá săn mồi dưới nước. Một thiết kế vật lý siêu nhẹ, siêu cứng và đa năng vượt xa những tấm áo giáp chống đạn tân tiến nhất mà con người từng chế tạo trong các phòng thí nghiệm quân sự tối tân! Khi mùa lũ về trên những cánh rừng Bắc Mỹ, hình ảnh những chú nhím bập bềnh trôi qua dòng nước cuộn xiết chính là minh chứng sống động nhất cho đỉnh cao của công nghệ phao sinh học tự nhiên.
```

### scene06 — BÀI HỌC TỪ PHÁO ĐÀI RẢI GAI
*Thẻ chương:* SỨC MẠNH TỪ SỰ TỰ VỆ CHỦ ĐỘNG

*Badge:* `KẾT LUẬN` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene06_p0.wav` (740 ký tự) · mood `am_ap`

```text
Từ ba mươi ngàn mũi tên ngạnh ngược giảm lực đâm năm mươi tư phần trăm, cơ chế bánh cóc một chiều tự rút sâu vào thớ thịt kẻ thù, lớp mỡ kháng khuẩn tự chữa lành vết thương khi ngã cây, cho đến cấu trúc lõi xốp composite siêu nhẹ bập bềnh trên mặt nước, Pháo Đài Tự Hành đã dạy cho chúng ta một bài học sâu sắc về nghệ thuật phòng thủ trong tự nhiên. Nó không bao giờ chủ động gây hấn hay tấn công ai trước, nó chỉ lẳng lặng gặm vỏ cây giữa rừng già, nhưng bất kỳ kẻ nào ngạo mạn muốn biến nó thành con mồi đều sẽ phải trả giá bằng cả mạng sống của mình. Nó không cần phải phô trương nanh vuốt hay rống lên những tiếng gầm gừ đe dọa, bởi vì tự bản thân lớp áo giáp của nó đã là một lời cảnh cáo đanh thép nhất cho mọi kẻ nuôi ý đồ xâm phạm.
```
**Part 1** → `audio/vs/scene06_p1.wav` (879 ký tự) · mood `am_ap`

```text
Trong cuộc sống và thương trường cũng vậy! Sức mạnh đích thực không nằm ở việc bạn đi đe dọa hay lấn lướt người khác, mà nằm ở năng lực tự bảo vệ vững chắc và những ranh giới thép không thể bị xâm phạm! Hãy trang bị cho mình một nội lực thâm hậu, sự điềm tĩnh kiên định và một cơ chế bảo vệ thông minh như chú nhím nhỏ bé giữa rừng sâu nhé! Bạn thấy chi tiết kỹ thuật nào của Pháo Đài Tự Hành tinh vi nhất: Những chiếc ngạnh ngược microscopic hay lớp mỡ kháng sinh tự chữa lành? Hãy chia sẻ quan điểm của bạn bên dưới nhé! Còn ở tập tiếp theo, chúng ta sẽ bước vào đấu trường La Mã đỉnh cao để giải mã một gã khổng lồ nâng vật nặng tám trăm ki-lô-gam dù chỉ ăn chay nhai lá cây! Hãy học cách xây dựng những giá trị vững chắc từ bên trong và thiết lập những ranh giới bảo vệ kiên cố cho bản thân, để có thể tự tin vững bước giữa một thế giới đầy biến động và cạnh tranh khốc liệt!
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Tại sao chỉ một chiếc lông nhím nhỏ bé cắm vào mõm cũng đủ sức hạ gục cả một con báo hoa mai hung dữ?! Hãy nhìn Pháo Đài Tự Hành với ba mươi ngàn mũi tên chết chóc này xem! Nhím hoàn toàn không hề bắn lông từ xa như trong phim hoạt hình đâu nhé! Dưới kính hiển vi điện tử quét, đầu mỗi chiếc lông nhím chứa tới tám trăm chiếc ngạnh ngược siêu nhỏ xếp lớp như lưỡi móc câu! Khi đâm vào thịt, các ngạnh này nép sát giúp giảm năm mươi tư phần trăm lực đâm, nhưng khi rút ra thì bung nở móc chặt, làm tăng lực rút lên gấp ba lần! Đáng sợ hơn cả, các cử động cơ bắp của con thú săn mồi sẽ vô tình đẩy chiếc lông tự rút sâu vào bên trong cơ thể với tốc độ một mi-li-mét mỗi giờ, đâm thủng vòm họng và tim phổi kẻ địch! Đã thế, trên thân lông còn phủ lớp mỡ kháng sinh tự nhiên để nhím tự chữa lành khi lỡ bị lông đâm vào người! Một cỗ máy bọc thép sinh học với đòn phản công tàn khốc bậc nhất tự nhiên!
```

**Whisper prompt:** `Nhím Lông Nhọn, Erethizon dorsatum`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| ba mươi ngàn | 30.000 |
| Ba mươi ngàn | 30.000 |
| năm mươi tư phần trăm | 54% |
| ba lần | 3 lần |
| ba mươi xăng-ti-mét | 30cm |
| mười ki-lô-gam | 10kg |
| một mi-li-mét | 1mm |
| hai mươi tư giờ | 24h |
| bốn mươi cây số | 40km/h |
| bảy trăm đến tám trăm | 700-800 |
| tám trăm | 800 |
| mười mét | 10m |
| tám trăm ki-lô-gam | 800kg |
| bốn mươi lăm độ | 45° |
| mười đến hai mươi mi-crô-mét | 10-20 µm |
| bốn mi-li-mét | 4mm |
| năm phần trăm | 5% |
| không phẩy một giây | 0.1s |
| không phẩy ba gam | 0.3g |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · BẢN VẼ PHÁO ĐÀI RẢI GAI SỐNG · 89.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:06.1 (6.1s) | L01 | Chào mừng toàn thể các chuyên gia vũ khí đạn đạo và các kỹ sư sinh học đã quay trở lại với xưởng giải mã công nghệ quốc phòng |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: kỹ sư trưởng xưởng vũ khí mặc áo giáp chống đâm cầm kính hiển vi soi ngạnh gai: kỹ sư trưởng mở hồ sơ th |
| b02 | 00:06.1–00:16.2 (10.2s) | L02 | tự nhiên! Hãy nhìn vào buồng thử nghiệm vật liệu đằng kia xem, một cỗ máy bọc thép sinh học nhỏ gọn nặng vỏn vẹn 10kg đang lững thững bước đi với vẻ bất cần đời. Nó không cần hàm răng nanh sắc nhọn |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: chú nhím lông nhọn Bắc Mỹ hoạt hình ngộ nghĩnh (lưng mang bộ giáp 30.000 gai nhọn đính ngạnh ngược, biểu |
| b03 | 00:16.2–00:26.4 (10.2s) | L03 | như hổ dữ, cũng chẳng cần tốc độ bứt phá 40km/h một giờ như linh dương. Toàn bộ lưng và đuôi của nó được bọc kín bởi một kho vũ khí di động gồm 30.000 mũi tên chết chóc. Dân gian gọi nó là Nhím Lông | **30.000 GAI** · KHO VŨ KHÍ GAI · right/420 · [650, 400] | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: chú nhím lông nhọn Bắc Mỹ hoạt hình ngộ nghĩnh (lưng mang bộ giáp 30.000 gai nhọn đính ngạnh ngược, biểu |
| b04 | 00:26.4–00:35.9 (9.4s) | L04 | Nhọn, nhưng trên bàn thiết kế đạn đạo quân sự của chúng tôi, đây đích thị là Pháo Đài Tự Hành sở hữu công nghệ bẫy chông phản công tàn khốc nhất từng được ghi nhận trong lịch sử! Mỗi bước đi của nó chậm |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: kỹ sư trưởng xưởng vũ khí mặc áo giáp chống đâm cầm kính hiển vi soi ngạnh gai: kỹ sư chỉ thước đo laser |
| b05 | 00:35.9–00:45.2 (9.3s) | L05 | rãi, ung dung và điềm tĩnh như thể toàn bộ thế giới dã thú ngoài kia chẳng có lấy một thứ gì đủ tư cách làm nó phải bận tâm lo sợ. Báo cáo chỉ huy trưởng, phim hoạt hình thường vẽ con nhím này |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: cô trợ lý kỹ thuật đeo kính bảo hộ cầm bảng kẹp ghi chép lực cắm đâm xuyên: cô trợ lý kiểm tra bảng thôn |
| b06 | 00:45.2–00:56.1 (11.0s) | L06 | có thể bắn lông vèo vèo như cung tên từ xa đúng không ạ? Một quan niệm sai lầm kinh điển suốt nhiều thế kỷ đấy cô trợ lý ơi! Pháo Đài Tự Hành hoàn toàn không hề có cơ chế lò xo hay |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: sơ đồ cắt lớp vi phẫu mũi gai 30.000 ngạnh vảy xếp chồng kiểu lưỡi câu ngạnh ngược: sơ đồ mặt cắt mũi tê |
| b07 | 00:56.1–01:06.3 (10.2s) | L07 | khí nén nào để phóng lông từ xa như những mũi tên bắn tỉa. Nhưng cơ chế thực tế của nó còn nguy hiểm gấp vạn lần trò bắn tỉa vu vơ ấy! Lông của nó là những chiếc mũi lao ngạnh ngược thụ động, chỉ |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: chú ngơ ngác gãi đầu hoảng hốt khi chạm phải đầu gai nhọn: chú ngơ ngác hoang mang lùi xa khi thấy nhím  |
| b08 | 01:06.3–01:15.6 (9.3s) | L08 | cần chạm khẽ là tự tách gốc và tự động di chuyển sâu vào thớ thịt của kẻ địch như một mũi khoan cơ học tự động. Ngay bây giờ, hãy đeo kính bảo hộ và cùng chúng tôi đưa một chiếc lông nhím |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: chú nhím lông nhọn Bắc Mỹ hoạt hình ngộ nghĩnh (lưng mang bộ giáp 30.000 gai nhọn đính ngạnh ngược, biểu |
| b09 | 01:15.6–01:29.9 (14.3s) | L09 | lên kính hiển vi điện tử quét để bóc trần bí mật cơ khí vi mô này! Chỉ cần một kẻ đi săn dại dột đưa mõm lại gần ngửi ngửi, chiếc đuôi ngắn ngủn nặng trịch của nó sẽ quất ra một cú chớp nhoáng khiến hàng trăm mũi giáo cắm phập vào mũi đối phương trong sự ngỡ ngàng tột độ. |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: kỹ sư trưởng xưởng vũ khí mặc áo giáp chống đâm cầm kính hiển vi soi ngạnh gai chú nhím lông nhọn Bắc Mỹ |

### scene02 · CÔNG NGHỆ NGẠNH MÓC MICROSCOPIC · 112.5s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.4 (9.4s) | L10 | Dưới độ phóng đại hàng ngàn lần của kính hiển vi điện tử quét SEM, phần đầu của chiếc lông nhím dài 30cm này không hề trơn nhẵn như một cây kim may vá thông thường. |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: sơ đồ cắt lớp vi phẫu mũi gai 30.000 ngạnh vảy xếp chồng kiểu lưỡi câu ngạnh ngược: kính hiển vi điện tử |
| b02 | 00:09.4–00:23.7 (14.4s) | L11 | Ở khoảng 4mm ngoài cùng phần mũi nhọn, bề mặt được bao phủ bởi từ 700-800 vẩy ngạnh ngược microscopic xếp lớp gối lên nhau giống hệt như vẩy cá hay những chiếc mũi móc câu sắc lẹm. Các nhà khoa học vật liệu tại Đại học Harvard đã phát hiện |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: kính hiển vi điện tử phóng đại các vảy sừng xếp vát chĩa ngược chiều: sơ đồ cấu trúc vảy ngạnh xếp chồng |
| b03 | 00:23.7–00:36.8 (13.1s) | L12 | ra một điều kỳ diệu làm chấn động giới kỹ thuật cơ khí quốc tế! Những chiếc vẩy ngạnh này có kích thước siêu nhỏ chỉ khoảng 10-20 µm, xếp nghiêng một góc 45° hoàn hảo hướng về phía chuôi lông. Trời ơi kính hiển |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: kỹ sư trưởng xưởng vũ khí mặc áo giáp chống đâm cầm kính hiển vi soi ngạnh gai: kỹ sư thử nghiệm đâm mũi |
| b04 | 00:36.8–00:50.2 (13.4s) | L13 | vi phóng to nhìn gai góc ghê rợn quá, trông y như bầy dao găm thu nhỏ vậy các bác ơi! Khi đâm vào da thịt kẻ thù, các lớp ngạnh ngược này nép chặt vào thân lông theo chiều xuôi, hoạt động như những lưỡi dao rọc thu nhỏ tập trung ứng suất vào một điểm cực hẹp. Nhờ cơ |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: cô trợ lý kỹ thuật đeo kính bảo hộ cầm bảng kẹp ghi chép lực cắm đâm xuyên: cô trợ lý đo cảm biến lực nh |
| b05 | 00:50.2–01:01.4 (11.2s) | L14 | chế thông minh này, lực cần thiết để chiếc lông đâm thủng lớp da dày của thú dữ giảm tới 54% so với một cây kim thép y tế thông thường! Tức là chỉ cần một cú quất nhẹ từ chiếc đuôi của Pháo Đài Tự Hành, hàng chục mũi tên đã dễ | **-54%** · LỰC ĐÂM XUYÊN · left/420 · [350, 420] | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: chú nhím lông nhọn Bắc Mỹ hoạt hình ngộ nghĩnh (lưng mang bộ giáp 30.000 gai nhọn đính ngạnh ngược, biểu |
| b06 | 01:01.4–01:11.7 (10.2s) | L15 | dàng cắm sâu xuyên qua da thịt đối phương mà hầu như không gặp phải bất kỳ lực cản đáng kể nào. Cơ chế tập trung ứng suất này làm cho các mô thịt xung quanh bị rẽ sang hai bên một cách êm ái mà không bị dập nát, giúp mũi tên |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: báo hoa mai há hốc mồm ôm mũi đầy gai nhọn kêu la thảm thiết: kẻ săn mồi cố dùng móng vuốt cào mũi gai n |
| b07 | 01:11.7–01:23.8 (12.2s) | L16 | lướt vào bên trong sâu thẳm như một nhát dao rọc giấy đi qua lớp bơ mềm. Nhưng bi kịch thực sự chỉ bắt đầu khi con thú săn mồi tìm cách nhổ chiếc lông ra! Ngay khoảnh khắc có lực kéo ngược ra ngoài, hàng trăm chiếc vẩy ngạnh ngược lập tức xòe |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: bé con đội mũ bảo hộ tò mò chỉ tay vào chùm gai nhím xòe nan quạt: bé con đội mũ bảo hộ tròn mắt thán ph |
| b08 | 01:23.8–01:38.1 (14.3s) | L17 | bung ra và móc chặt vào các thớ cơ thịt xung quanh. Lực cần thiết để rút chiếc lông này ra tăng vọt lên gấp 3 lần so với lực đâm vào! Càng cố giật mạnh, các ngạnh móc càng xé toạc mô thịt, gây ra cơn đau đớn tột cùng và chảy máu dữ dội, biến chiếc lông thành một chiếc neo sắt vĩnh | **+300%** · LỰC CẢN NHỔ · right/420 · [700, 450] | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: sơ đồ cắt lớp vi phẫu mũi gai 30.000 ngạnh vảy xếp chồng kiểu lưỡi câu ngạnh ngược: mô hình so sánh mũi  |
| b09 | 01:38.1–01:52.5 (14.4s) | L18 | viễn khóa chặt bên trong cơ thể con mồi. Đây chính là nguyên lý của lưỡi câu cá cổ xưa nhưng đã được tự nhiên hoàn thiện đến cấp độ hiển vi phân tử, khiến mọi nỗ lực dùng móng vuốt hay cọ mõm vào gốc cây của con thú chỉ làm chiếc lông bị gãy thân và cắm chặt hơn vào thịt. |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: kỹ sư trưởng xưởng vũ khí mặc áo giáp chống đâm cầm kính hiển vi soi ngạnh gai: kỹ sư ghi chép sáng chế  |

### scene03 · MŨI KHOAN SINH HỌC DI ĐỘNG · 110.2s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.0 (7.0s) | L19 | Bây giờ mới là cơ chế sát thương tinh vi và tàn độc nhất khiến loài báo hoa mai và sư tử châu Phi phải kinh hồn bạt vía. Sau khi chiếc lông cắm vào thịt |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: chú nhím lông nhọn Bắc Mỹ hoạt hình ngộ nghĩnh (lưng mang bộ giáp 30.000 gai nhọn đính ngạnh ngược, biểu |
| b02 | 00:07.0–00:18.7 (11.7s) | L20 | và gãy gốc, nó không hề nằm yên một chỗ. Các chuyển động co bóp cơ bắp tự nhiên của con thú săn mồi khi di chuyển hay thở sẽ vô tình kích hoạt hệ thống bánh cóc một chiều của các ngạnh ngược. Do các ngạnh chỉ cho phép chiếc lông trượt theo chiều tiến lên mà |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: sơ đồ cắt lớp vi phẫu mũi gai 30.000 ngạnh vảy xếp chồng kiểu lưỡi câu ngạnh ngược: sơ đồ cơ học co bóp  |
| b03 | 00:18.7–00:30.6 (11.9s) | L21 | không thể tụt lùi, mỗi cú co cơ của con vật bị nạn sẽ đẩy chiếc lông nhọn tự rút sâu hơn vào bên trong với tốc độ khoảng 1mm mỗi giờ! Đây chính là cơ chế bánh cóc sinh học tự nhiên tinh xảo nhất từng được phát hiện trên cơ thể sinh vật, | **1 mm/h** · TỰ KHOAN SÂU · left/420 · [400, 380] | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: kỹ sư trưởng xưởng vũ khí mặc áo giáp chống đâm cầm kính hiển vi soi ngạnh gai: kỹ sư phân tích chuyển đ |
| b04 | 00:30.6–00:44.0 (13.4s) | L22 | biến chính năng lượng cử động của nạn nhân thành động cơ đẩy đưa vũ khí hủy diệt vào sâu trong lục phủ ngũ tạng. Ủa các bác kỹ sư ơi, vậy nếu bị cắm vào mõm thì chiếc lông đó sẽ chui đi đâu mất tiêu luôn hả? Câu hỏi rất hay của bé con đấy! |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: cô trợ lý kỹ thuật đeo kính bảo hộ cầm bảng kẹp ghi chép lực cắm đâm xuyên: cô trợ lý hoảng hốt trước đồ |
| b05 | 00:44.0–00:56.4 (12.4s) | L23 | Chiếc lông nhọn sẽ từ từ xuyên thủng các lớp cơ má, đâm xuyên qua vòm họng, thậm chí di chuyển sâu vào trong lồng ngực làm thủng phổi hoặc đâm rách tâm thất của tim! Đã có rất nhiều ghi nhận thực địa về những con báo hoa mai trưởng thành khỏe mạnh |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: báo hoa mai há hốc mồm ôm mũi đầy gai nhọn kêu la thảm thiết: báo hoa mai nằm bẹp gí ôm mõm sưng phù vì  |
| b06 | 00:56.4–01:09.8 (13.4s) | L24 | bị chết đói thảm khốc chỉ vì vài chiếc lông nhím cắm sâu vào hàm dưới làm nhiễm trùng mưng mủ, khiến miệng sưng to biến dạng không thể nào há ra để nhai thịt được nữa. Một đòn trả đũa tàn nhẫn được lập trình để kết liễu kẻ săn mồi sau nhiều ngày hành hạ! |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: chú ngơ ngác gãi đầu hoảng hốt khi chạm phải đầu gai nhọn: chú ngơ ngác toát mồ hôi hột rụt tay lại khôn |
| b07 | 01:09.8–01:22.4 (12.6s) | L25 | Những kẻ săn mồi khát máu như báo sư tử hay chó sói đồng cỏ một khi dính phải bẫy chông này thường phải trải qua những tuần lễ đau đớn tột cùng trước khi bị cướp đi hơi thở cuối cùng trong sự bất lực. Đặc biệt hơn nữa, phần gốc của lông nhím nối |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: sơ đồ cắt lớp vi phẫu mũi gai 30.000 ngạnh vảy xếp chồng kiểu lưỡi câu ngạnh ngược: mô hình 3D cho thấy  |
| b08 | 01:22.4–01:36.1 (13.7s) | L26 | với nang lông rất lỏng lẻo. Lớp màng cơ dưới da của Pháo Đài Tự Hành có khả năng chủ động co thắt để dựng đứng toàn bộ 30.000 mũi tên lên khi bị đe dọa, tạo ra tiếng xào xạc đanh thép cảnh báo. Khi kẻ địch chạm phải, các sợi lông này sẽ tự động tách rời khỏi gốc một cách êm ái, chuyển giao toàn |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: chú nhím lông nhọn Bắc Mỹ hoạt hình ngộ nghĩnh (lưng mang bộ giáp 30.000 gai nhọn đính ngạnh ngược, biểu |
| b09 | 01:36.1–01:50.2 (14.1s) | L27 | bộ gánh nặng vũ khí sang cơ thể đối thủ mà không làm tổn thương dù chỉ một tế bào biểu bì của chú nhím! Hệ thống cơ dựng lông này được điều khiển bởi các xung thần kinh cực kỳ nhạy bén, chỉ mất chưa đầy 0.1s để chuyển từ trạng thái nằm xuôi sang tư thế pháo đài xòe gai sẵn sàng nghênh chiến. |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: kỹ sư trưởng xưởng vũ khí mặc áo giáp chống đâm cầm kính hiển vi soi ngạnh gai chú nhím lông nhọn Bắc Mỹ |

### scene04 · THUỐC KHÁNG SINH QUÉT TRÊN MŨI TÊN · 104.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.2 (7.2s) | L28 | Có một nghịch lý kỹ thuật vô cùng hóc búa được đặt ra cho ban thiết kế sinh học: Nếu mang trên mình 30.000 mũi tên chết chóc có ngạnh ngược nguy hiểm |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: sơ đồ màng bọc axit béo kháng sinh tự nhiên phủ bóng loáng thân gai: sơ đồ quang phổ huỳnh quang phát hi |
| b02 | 00:07.2–00:17.7 (10.6s) | L29 | như vậy, làm thế nào để Pháo Đài Tự Hành không vô tình tự đâm chết chính mình trong những sinh hoạt hàng ngày? Loài nhím này rất thích leo trèo lên những cành cây cao để gặm vỏ cây non và ăn quả ngọt, nhưng chúng lại nổi tiếng |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: kỹ sư trưởng xưởng vũ khí mặc áo giáp chống đâm cầm kính hiển vi soi ngạnh gai: kỹ sư nhỏ giọt vi khuẩn  |
| b03 | 00:17.7–00:28.9 (11.1s) | L30 | là những kẻ vụng về, thường xuyên bị trượt chân và ngã từ trên ngọn cây cao chót vót xuống mặt đất đá lởm chởm. Trọng lượng 10kg với đôi chân ngắn cũn cỡn khiến những bước leo trèo trên các cành cây sồi hay phong cao vút luôn tiềm ẩn |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: cô trợ lý kỹ thuật đeo kính bảo hộ cầm bảng kẹp ghi chép lực cắm đâm xuyên: cô trợ lý ngạc nhiên trước c |
| b04 | 00:28.9–00:40.5 (11.7s) | L31 | rủi ro té ngã cực kỳ cao đối với cỗ máy bọc thép này. Khi ngã từ trên cao xuống, không ít lần những chiếc lông nhọn của chính nó bị gãy gập và đâm ngược vào đùi hoặc bụng của nó. Nhưng kỳ diệu thay, các vết thương này hầu |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: chú nhím lông nhọn Bắc Mỹ hoạt hình ngộ nghĩnh (lưng mang bộ giáp 30.000 gai nhọn đính ngạnh ngược, biểu |
| b05 | 00:40.5–00:52.9 (12.4s) | L32 | như không bao giờ bị nhiễm trùng hay mưng mủ! Các nhà hóa sinh học phát hiện ra rằng, bao phủ bên ngoài mỗi chiếc lông nhím là một lớp màng axit béo tự nhiên đậm đặc, chứa các hợp chất kháng khuẩn cực mạnh có khả năng tiêu diệt hoàn toàn |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: chú ngơ ngác gãi đầu hoảng hốt khi chạm phải đầu gai nhọn: chú ngơ ngác ôm đầu thở phào khi biết nhím tự |
| b06 | 00:52.9–01:04.9 (12.0s) | L33 | các loại vi khuẩn gram dương nguy hiểm. Lớp mỡ kháng sinh này hoạt động như một loại thuốc mỡ bôi vết thương được quét sẵn lên từng mũi tên! Lớp mỡ kháng khuẩn này gồm hỗn hợp các chuỗi axit béo tự do phức tạp, có khả năng ức chế |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: sơ đồ màng bọc axit béo kháng sinh tự nhiên phủ bóng loáng thân gai: công thức hóa học của axit free fat |
| b07 | 01:04.9–01:17.2 (12.2s) | L34 | màng tế bào của các loại vi khuẩn nguy hiểm nhất như tụ cầu vàng hay liên cầu khuẩn trong môi trường tự nhiên. Khi chiếc lông đâm vào chính cơ thể nó, lớp mỡ kháng khuẩn lập tức khử trùng vết thương tại chỗ, giúp mô thịt tự co lại |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: bé con đội mũ bảo hộ tò mò chỉ tay vào chùm gai nhím xòe nan quạt: bé con giơ ngón tay cái tán thưởng tr |
| b08 | 01:17.2–01:30.8 (13.6s) | L35 | và phục hồi nhanh chóng mà không gây nguy hiểm tính mạng. Thiên nhiên không chỉ trang bị cho Pháo Đài Tự Hành một kho vũ khí công phá hàng đầu, mà còn chu đáo dán sẵn tem bảo hiểm y tế tự động cho người sử dụng, đảm bảo tính an toàn tuyệt đối cho người lính mang vũ |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: chú nhím lông nhọn Bắc Mỹ hoạt hình ngộ nghĩnh (lưng mang bộ giáp 30.000 gai nhọn đính ngạnh ngược, biểu |
| b09 | 01:30.8–01:44.4 (13.7s) | L36 | khí trong mọi tình huống rủi ro nghề nghiệp! Nhờ có lớp lá chắn hóa học này, những con nhím dù bị hàng chục vết đâm thủng do chính lông của mình gây ra khi rơi từ độ cao 10m vẫn thong thả đứng dậy, phủi bụi và tiếp tục kiếm ăn như chưa từng có chuyện gì xảy ra. | **10 MÉT** · ĐỘ CAO TRÈO · right/420 · [680, 420] | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: kỹ sư trưởng xưởng vũ khí mặc áo giáp chống đâm cầm kính hiển vi soi ngạnh gai: kỹ sư chuẩn bị bóc tách  |

### scene05 · KIẾN TRÚC VẬT LIỆU COMPOSITE · 89.6s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.0 (8.0s) | L37 | Hãy cầm một nắm lông nhím lên tay và các bạn sẽ phải kinh ngạc trước trọng lượng của chúng! 30.000 mũi tên bọc kín toàn thân nhưng |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: sơ đồ cắt lớp vi phẫu mũi gai 30.000 ngạnh vảy xếp chồng kiểu lưỡi câu ngạnh ngược: sơ đồ cắt ngang lõi  |
| b02 | 00:08.0–00:17.8 (9.7s) | L38 | tổng khối lượng của chúng chỉ chiếm chưa đầy 5% trọng lượng cơ thể chú nhím. Nếu những chiếc lông này là những thanh xương đặc cứng, Pháo Đài Tự Hành sẽ bị đè bẹp dí dưới sức nặng của chính mình và |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: kỹ sư trưởng xưởng vũ khí mặc áo giáp chống đâm cầm kính hiển vi soi ngạnh gai: kỹ sư dùng máy ép thủy l |
| b03 | 00:17.8–00:28.1 (10.3s) | L39 | không thể nào nhấc nổi bốn chân để di chuyển. Bí quyết nằm ở cấu trúc vật liệu rỗng bên trong thân lông! Một chuẩn mực trọng lượng vàng mà các kỹ sư chế tạo áo giáp chống đạn quân sự hiện đại luôn |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: cô trợ lý kỹ thuật đeo kính bảo hộ cầm bảng kẹp ghi chép lực cắm đâm xuyên: cô trợ lý cân mẫu gai chỉ nặ |
| b04 | 00:28.1–00:37.7 (9.6s) | L40 | khao khát đạt được nhưng vẫn chưa thể tối ưu hóa trọn vẹn như thiên nhiên. Cắt ngang thân của một chiếc lông, chúng ta sẽ thấy một lớp vỏ ngoài bằng chất sừng keratin cực kỳ cứng cáp và chịu |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: chú nhím lông nhọn Bắc Mỹ hoạt hình ngộ nghĩnh (lưng mang bộ giáp 30.000 gai nhọn đính ngạnh ngược, biểu |
| b05 | 00:37.7–00:46.8 (9.1s) | L41 | lực uốn nắn tuyệt vời. Nhưng bên trong lòng ống lại là một ma trận bọt xốp khí rỗng li ti, đan xen nhau theo cấu trúc tổ ong tổ mối. Cấu trúc composite này vừa tối ưu hóa độ cứng chống cong vênh |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: báo hoa mai há hốc mồm ôm mũi đầy gai nhọn kêu la thảm thiết: báo hoa mai ngậm ngùi bỏ đi với cái mũi nh |
| b06 | 00:46.8–00:56.4 (9.6s) | L42 | khi va đập, vừa biến từng chiếc lông thành một khoang chứa khí tí hon. Nhờ có hàng chục ngàn khoang khí này, chú nhím khi rơi xuống nước sẽ nổi bồng bềnh như một chiếc phao cứu sinh tự nhiên! Tỷ |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: sơ đồ cắt lớp vi phẫu mũi gai 30.000 ngạnh vảy xếp chồng kiểu lưỡi câu ngạnh ngược: ứng dụng vật liệu ph |
| b07 | 00:56.4–01:06.0 (9.7s) | L43 | trọng của mỗi chiếc lông chỉ đạt khoảng 0.3g trên một xăng-ti-mét khối, nhẹ hơn cả gỗ bấc và hoàn toàn nổi trên mặt nước mà không cần bất kỳ sự hỗ trợ cơ học nào khác. Nó có thể thong thả bơi qua | **0.3 GAM** · TRỌNG LƯỢNG GAI · left/420 · [380, 430] | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: chú ngơ ngác gãi đầu hoảng hốt khi chạm phải đầu gai nhọn: chú ngơ ngác vỗ tay thán phục bộ giáp composi |
| b08 | 01:06.0–01:15.7 (9.7s) | L44 | những con sông lớn mà không sợ bị chìm nghỉm, vừa có thể xòe gai đẩy lùi lũ cá săn mồi dưới nước. Một thiết kế vật lý siêu nhẹ, siêu cứng và đa năng vượt xa những tấm áo giáp chống đạn |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: chú nhím lông nhọn Bắc Mỹ hoạt hình ngộ nghĩnh (lưng mang bộ giáp 30.000 gai nhọn đính ngạnh ngược, biểu |
| b09 | 01:15.7–01:29.6 (13.9s) | L45 | tân tiến nhất mà con người từng chế tạo trong các phòng thí nghiệm quân sự tối tân! Khi mùa lũ về trên những cánh rừng Bắc Mỹ, hình ảnh những chú nhím bập bềnh trôi qua dòng nước cuộn xiết chính là minh chứng sống động nhất cho đỉnh cao của công nghệ phao sinh học tự nhiên. |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: kỹ sư trưởng xưởng vũ khí mặc áo giáp chống đâm cầm kính hiển vi soi ngạnh gai chú nhím lông nhọn Bắc Mỹ |

### scene06 · BÀI HỌC TỪ PHÁO ĐÀI RẢI GAI · 78.3s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.6 (7.6s) | L46 | Từ 30.000 mũi tên ngạnh ngược giảm lực đâm 54%, cơ chế bánh cóc một chiều tự rút sâu vào thớ thịt kẻ thù, lớp mỡ kháng khuẩn tự |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: chú nhím lông nhọn Bắc Mỹ hoạt hình ngộ nghĩnh (lưng mang bộ giáp 30.000 gai nhọn đính ngạnh ngược, biểu |
| b02 | 00:07.6–00:16.7 (9.1s) | L47 | chữa lành vết thương khi ngã cây, cho đến cấu trúc lõi xốp composite siêu nhẹ bập bềnh trên mặt nước, Pháo Đài Tự Hành đã dạy cho chúng ta một bài học sâu sắc về nghệ thuật phòng thủ trong tự nhiên. |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: sơ đồ cắt lớp vi phẫu mũi gai 30.000 ngạnh vảy xếp chồng kiểu lưỡi câu ngạnh ngược: tổng kết 4 công nghệ |
| b03 | 00:16.7–00:26.3 (9.6s) | L48 | Nó không bao giờ chủ động gây hấn hay tấn công ai trước, nó chỉ lẳng lặng gặm vỏ cây giữa rừng già, nhưng bất kỳ kẻ nào ngạo mạn muốn biến nó thành con mồi đều sẽ phải trả giá bằng cả mạng |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: kỹ sư trưởng xưởng vũ khí mặc áo giáp chống đâm cầm kính hiển vi soi ngạnh gai: kỹ sư trưởng giơ bản thi |
| b04 | 00:26.3–00:35.0 (8.7s) | L49 | sống của mình. Nó không cần phải phô trương nanh vuốt hay rống lên những tiếng gầm gừ đe dọa, bởi vì tự bản thân lớp áo giáp của nó đã là một lời cảnh cáo đanh thép nhất cho mọi kẻ nuôi ý |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: cô trợ lý kỹ thuật đeo kính bảo hộ cầm bảng kẹp ghi chép lực cắm đâm xuyên: cô trợ lý chào tạm biệt khán |
| b05 | 00:35.0–00:44.9 (9.9s) | L50 | đồ xâm phạm. Trong cuộc sống và thương trường cũng vậy! Sức mạnh đích thực không nằm ở việc bạn đi đe dọa hay lấn lướt người khác, mà nằm ở năng lực tự bảo vệ vững chắc và những ranh giới thép không |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: bé con đội mũ bảo hộ tò mò chỉ tay vào chùm gai nhím xòe nan quạt: bé con mỉm cười giơ biểu tượng like k |
| b06 | 00:44.9–00:54.4 (9.5s) | L51 | thể bị xâm phạm! Hãy trang bị cho mình một nội lực thâm hậu, sự điềm tĩnh kiên định và một cơ chế bảo vệ thông minh như chú nhím nhỏ bé giữa rừng sâu nhé! Bạn thấy chi tiết kỹ thuật nào của |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: chú nhím lông nhọn Bắc Mỹ hoạt hình ngộ nghĩnh (lưng mang bộ giáp 30.000 gai nhọn đính ngạnh ngược, biểu |
| b07 | 00:54.4–01:04.2 (9.8s) | L52 | Pháo Đài Tự Hành tinh vi nhất: Những chiếc ngạnh ngược microscopic hay lớp mỡ kháng sinh tự chữa lành? Hãy chia sẻ quan điểm của bạn bên dưới nhé! Còn ở tập tiếp theo, chúng ta sẽ bước vào đấu trường La Mã đỉnh |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: : poster nghệ thuật tổng kết Pháo Đài Tự Hành với dòng chữ khoa học ấn tượng. |
| b08 | 01:04.2–01:18.3 (14.1s) | L53 | cao để giải mã một gã khổng lồ nâng vật nặng 800kg dù chỉ ăn chay nhai lá cây! Hãy học cách xây dựng những giá trị vững chắc từ bên trong và thiết lập những ranh giới bảo vệ kiên cố cho bản thân, để có thể tự tin vững bước giữa một thế giới đầy biến động và cạnh tranh khốc liệt! |  | Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: kỹ sư trưởng xưởng vũ khí mặc áo giáp chống đâm cầm kính hiển vi soi ngạnh gai: khung hình chuyển tiếp h |

## 5. Phân cảnh Shorts — từng beat

Banner: **30.000 MŨI TÊN / TỰ RÚT SÂU?!** · giọng 47.5s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Tại sao chỉ một chiếc lông nhím nhỏ bé cắm vào mõm cũng đủ sức |  |
| s02 | 00:03.9 | S02 | hạ gục cả một con báo hoa mai hung dữ?! Hãy nhìn Pháo Đài Tự Hành với 30.000 mũi tên chết chóc này xem! | **30.000 GAI** · VŨ KHÍ TỰ VỆ · R/540 · [350, 600] |
| s03 | 00:10.2 | S03 | Nhím hoàn toàn không hề bắn lông từ xa như trong phim hoạt hình đâu nhé! Dưới kính hiển vi điện tử quét, đầu |  |
| s04 | 00:15.8 | S04 | mỗi chiếc lông nhím chứa tới 800 chiếc ngạnh ngược siêu nhỏ xếp lớp như lưỡi móc câu! Khi đâm vào thịt, các ngạnh |  |
| s05 | 00:21.9 | S05 | này nép sát giúp giảm 54% lực đâm, nhưng khi rút ra thì bung nở móc chặt, làm tăng lực rút lên gấp 3 lần! |  |
| s06 | 00:28.6 | S06 | Đáng sợ hơn cả, các cử động cơ bắp của con thú săn mồi sẽ vô tình đẩy chiếc lông tự rút |  |
| s07 | 00:33.1 | S07 | sâu vào bên trong cơ thể với tốc độ 1mm mỗi giờ, đâm thủng vòm họng và tim phổi kẻ địch! Đã thế, trên thân |  |
| s08 | 00:39.0 | S08 | lông còn phủ lớp mỡ kháng sinh tự nhiên để nhím tự chữa lành khi lỡ bị lông đâm vào người! |  |
| s09 | 00:43.7 | S08b | Một cỗ máy bọc thép sinh học với đòn phản công tàn khốc bậc nhất tự nhiên! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chào mừng toàn thể các chuyên gia vũ khí đạn đạo và các kỹ sư sinh học đã quay trở lại với xưởng giải mã công nghệ quốc phòng tự". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: kỹ sư trưởng xưởng vũ khí mặc áo giáp chống đâm cầm kính hiển vi soi ngạnh gai: kỹ sư trưởng mở hồ sơ thiết kế vũ khí phòng thủ pháo đài tự hành trên bàn kỹ thuật.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nhiên! Hãy nhìn vào buồng thử nghiệm vật liệu đằng kia xem, một cỗ máy bọc thép sinh học nhỏ gọn nặng vỏn vẹn 10kg đang lững thững bước đi với vẻ bất cần đời. Nó không cần hàm răng nanh sắc nhọn như hổ". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: chú nhím lông nhọn Bắc Mỹ hoạt hình ngộ nghĩnh (lưng mang bộ giáp 30.000 gai nhọn đính ngạnh ngược, biểu cảm tự tin đắc thắng): chú nhím lông nhọn bước đi lừng lững trong rừng thông như chiếc xe bọc thép rải gai.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "dữ, cũng chẳng cần tốc độ bứt phá 40km/h một giờ như linh dương. Toàn bộ lưng và đuôi của nó được bọc kín bởi một kho vũ khí di động gồm 30.000 mũi tên chết chóc. Dân gian gọi nó là Nhím Lông Nhọn,". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: chú nhím lông nhọn Bắc Mỹ hoạt hình ngộ nghĩnh (lưng mang bộ giáp 30.000 gai nhọn đính ngạnh ngược, biểu cảm tự tin đắc thắng) báo hoa mai há hốc mồm ôm mũi đầy gai nhọn kêu la thảm thiết: báo hoa mai lao tới định vồ nhưng khựng lại hoảng hốt trước tấm khiên gai xòe rộng.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nhưng trên bàn thiết kế đạn đạo thế giới tự nhiên của chúng tôi, đây đích thị là Pháo Đài Tự Hành sở hữu công nghệ bẫy chông phản công tàn khốc nhất từng được ghi nhận trong lịch sử! Mỗi bước đi của nó chậm rãi,". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: kỹ sư trưởng xưởng vũ khí mặc áo giáp chống đâm cầm kính hiển vi soi ngạnh gai: kỹ sư chỉ thước đo laser vào chùm gai đuôi rung lắc tạo tiếng xào xạc cảnh báo.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "ung dung và điềm tĩnh như thể toàn bộ thế giới dã thú ngoài kia chẳng có lấy một thứ gì đủ tư cách làm nó phải bận tâm lo sợ. Báo cáo chỉ huy trưởng, phim hoạt hình thường vẽ con nhím này có". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: cô trợ lý kỹ thuật đeo kính bảo hộ cầm bảng kẹp ghi chép lực cắm đâm xuyên: cô trợ lý kiểm tra bảng thông số 30.000 mũi tên sống sẵn sàng phóng thích.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "thể bắn lông vèo vèo như cung tên từ xa đúng không ạ? Một quan niệm sai lầm kinh điển suốt nhiều thế kỷ đấy cô trợ lý ơi! Pháo Đài Tự Hành hoàn toàn không hề có cơ chế lò xo hay khí nén". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: sơ đồ cắt lớp vi phẫu mũi gai 30.000 ngạnh vảy xếp chồng kiểu lưỡi câu ngạnh ngược: sơ đồ mặt cắt mũi tên sinh học gắn lỏng lẻo vào nang lông chờ tiếp xúc.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nào để phóng lông từ xa như những mũi tên phun tia nước tầm xa. Nhưng cơ chế thực tế của nó còn nguy hiểm gấp vạn lần trò phun tia nước tầm xa vu vơ ấy! Lông của nó là những chiếc mũi lao ngạnh ngược thụ động, chỉ cần". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: chú ngơ ngác gãi đầu hoảng hốt khi chạm phải đầu gai nhọn: chú ngơ ngác hoang mang lùi xa khi thấy nhím quay đuôi xù lông phòng ngự.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chạm khẽ là tự tách gốc và tự động di chuyển sâu vào thớ thịt của kẻ địch như một mũi khoan cơ học tự động. Ngay bây giờ, hãy đeo kính bảo hộ và cùng chúng tôi đưa một chiếc lông nhím lên kính". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: chú nhím lông nhọn Bắc Mỹ hoạt hình ngộ nghĩnh (lưng mang bộ giáp 30.000 gai nhọn đính ngạnh ngược, biểu cảm tự tin đắc thắng): chú nhím ngậm cành cây gặm vỏ thông bình thản bất chấp kẻ săn mồi vây quanh.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "hiển vi điện tử quét để bóc trần bí mật cơ khí vi mô này! Chỉ cần một kẻ đi săn dại dột đưa mõm lại gần ngửi ngửi, chiếc đuôi ngắn ngủn nặng trịch của nó sẽ quất ra một cú chớp nhoáng khiến hàng trăm mũi giáo cắm phập vào mũi đối phương trong sự ngỡ ngàng tột độ.". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: kỹ sư trưởng xưởng vũ khí mặc áo giáp chống đâm cầm kính hiển vi soi ngạnh gai chú nhím lông nhọn Bắc Mỹ hoạt hình ngộ nghĩnh (lưng mang bộ giáp 30.000 gai nhọn đính ngạnh ngược, biểu cảm tự tin đắc thắng): kỹ sư chuẩn bị mở kính hiển vi điện tử quét sâu vào bí mật ngạnh ngược.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Dưới độ phóng đại hàng ngàn lần của kính hiển vi điện tử quét SEM, phần đầu của chiếc lông nhím dài 30cm này không hề trơn nhẵn như một cây kim may vá thông thường.". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: sơ đồ cắt lớp vi phẫu mũi gai 30.000 ngạnh vảy xếp chồng kiểu lưỡi câu ngạnh ngược: kính hiển vi điện tử SEM quét độ phân giải nano vào 4mm đầu nhọn mũi gai.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ở khoảng 4mm ngoài cùng phần mũi nhọn, bề mặt được bao phủ bởi từ 700-800 vẩy ngạnh ngược microscopic xếp lớp gối lên nhau giống hệt như vẩy cá hay những chiếc mũi móc câu sắc lẹm. Các nhà khoa học vật liệu tại Đại học Harvard đã phát hiện ra một". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: kính hiển vi điện tử phóng đại các vảy sừng xếp vát chĩa ngược chiều: sơ đồ cấu trúc vảy ngạnh xếp chồng vát ngược 45 độ như hàng ngàn lưỡi câu cá mập.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "điều kỳ diệu làm chấn động giới kỹ thuật cơ khí quốc tế! Những chiếc vẩy ngạnh này có kích thước siêu nhỏ chỉ khoảng 10-20 µm, xếp nghiêng một góc 45° hoàn hảo hướng về phía chuôi lông. Trời ơi kính hiển vi phóng to nhìn gai góc ghê rợn quá, trông". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: kỹ sư trưởng xưởng vũ khí mặc áo giáp chống đâm cầm kính hiển vi soi ngạnh gai: kỹ sư thử nghiệm đâm mũi gai vào bia thịt thấy lực xuyên giảm 54% nhờ ngạnh hướng dẫn.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "y như bầy dao găm thu nhỏ vậy các bác ơi! Khi đâm vào da thịt kẻ thù, các lớp ngạnh ngược này nép chặt vào thân lông theo chiều xuôi, hoạt động như những lưỡi dao rọc thu nhỏ tập trung ứng suất vào một điểm cực hẹp. Nhờ cơ chế thông". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: cô trợ lý kỹ thuật đeo kính bảo hộ cầm bảng kẹp ghi chép lực cắm đâm xuyên: cô trợ lý đo cảm biến lực nhổ thấy lực cản tăng gấp 3 lần do vảy bung xòe móc chặt.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "minh này, lực cần thiết để chiếc lông đâm thủng lớp da dày của thú dữ giảm tới 54% so với một cây kim thép y tế thông thường! Tức là chỉ cần một cú quất nhẹ từ chiếc đuôi của Pháo Đài Tự Hành, hàng chục mũi tên đã dễ dàng cắm". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: chú nhím lông nhọn Bắc Mỹ hoạt hình ngộ nghĩnh (lưng mang bộ giáp 30.000 gai nhọn đính ngạnh ngược, biểu cảm tự tin đắc thắng): chú nhím rung lắc bộ áo giáp gai phát ra ánh kim loại đen bóng đầy kiêu hãnh.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "sâu xuyên qua da thịt đối phương mà hầu như không gặp phải bất kỳ lực cản đáng kể nào. Cơ chế tập trung ứng suất này làm cho các mô thịt xung quanh bị rẽ sang hai bên một cách êm ái mà không bị dập nát, giúp mũi tên lướt vào". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: báo hoa mai há hốc mồm ôm mũi đầy gai nhọn kêu la thảm thiết: kẻ săn mồi cố dùng móng vuốt cào mũi gai nhưng càng cào gai càng lún sâu vào da.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bên trong sâu thẳm như một nhát dao rọc giấy đi qua lớp bơ mềm. Nhưng bi kịch thực sự chỉ bắt đầu khi con thú săn mồi tìm cách nhổ chiếc lông ra! Ngay khoảnh khắc có lực kéo ngược ra ngoài, hàng trăm chiếc vẩy ngạnh ngược lập tức xòe bung". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: bé con đội mũ bảo hộ tò mò chỉ tay vào chùm gai nhím xòe nan quạt: bé con đội mũ bảo hộ tròn mắt thán phục trước công nghệ nano tự nhiên.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "ra và móc chặt vào các thớ cơ thịt xung quanh. Lực cần thiết để rút chiếc lông này ra tăng vọt lên gấp 3 lần so với lực đâm vào! Càng cố giật mạnh, các ngạnh móc càng xé toạc mô thịt, gây ra cơn đau đớn tột cùng và chảy nước màu". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: sơ đồ cắt lớp vi phẫu mũi gai 30.000 ngạnh vảy xếp chồng kiểu lưỡi câu ngạnh ngược: mô hình so sánh mũi kim tiêm y tế thông thường với mũi gai nhím sinh học.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "dữ dội, biến chiếc lông thành một chiếc neo sắt vĩnh viễn khóa chặt bên trong cơ thể con mồi. Đây chính là nguyên lý của lưỡi câu cá cổ xưa nhưng đã được tự nhiên hoàn thiện đến cấp độ hiển vi phân tử, khiến mọi nỗ lực dùng móng vuốt hay cọ mõm vào gốc cây của con thú chỉ làm chiếc lông bị gãy thân và cắm chặt hơn vào thịt.". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: kỹ sư trưởng xưởng vũ khí mặc áo giáp chống đâm cầm kính hiển vi soi ngạnh gai: kỹ sư ghi chép sáng chế kim tiêm giảm đau mô phỏng ngạnh gai nhím vào sổ tay.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bây giờ mới là cơ chế sát thương tinh vi và tàn độc nhất khiến loài báo hoa mai và sư tử châu Phi phải kinh hồn bạt vía. Sau khi chiếc lông cắm vào thịt và gãy". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: chú nhím lông nhọn Bắc Mỹ hoạt hình ngộ nghĩnh (lưng mang bộ giáp 30.000 gai nhọn đính ngạnh ngược, biểu cảm tự tin đắc thắng): chú nhím vung chiếc đuôi gai đập mạnh vào thân cây thử độ bền va chạm.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "gốc, nó không hề nằm yên một chỗ. Các chuyển động co bóp cơ bắp tự nhiên của con thú săn mồi khi di chuyển hay thở sẽ vô tình kích hoạt hệ thống bánh cóc một chiều của các ngạnh ngược. Do các ngạnh chỉ cho phép chiếc lông trượt theo chiều tiến lên mà". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: sơ đồ cắt lớp vi phẫu mũi gai 30.000 ngạnh vảy xếp chồng kiểu lưỡi câu ngạnh ngược: sơ đồ cơ học co bóp mô cơ khiến mũi gai tự khoan sâu 1mm mỗi giờ vào vết thương.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "không thể tụt lùi, mỗi cú co cơ của con vật bị nạn sẽ đẩy chiếc lông nhọn tự rút sâu hơn vào bên trong với tốc độ khoảng 1mm mỗi giờ! Đây chính là cơ chế bánh cóc sinh học tự nhiên tinh xảo nhất từng được phát hiện trên cơ thể sinh vật, biến". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: kỹ sư trưởng xưởng vũ khí mặc áo giáp chống đâm cầm kính hiển vi soi ngạnh gai: kỹ sư phân tích chuyển động một chiều của mũi tên sinh học không thể rút ngược.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chính năng lượng cử động của nạn nhân thành động cơ đẩy đưa vũ khí hủy diệt vào sâu trong lục phủ ngũ tạng. Ủa các bác kỹ sư ơi, vậy nếu bị cắm vào mõm thì chiếc lông đó sẽ chui đi đâu mất tiêu luôn hả? Câu hỏi rất hay của bé con đấy!". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: cô trợ lý kỹ thuật đeo kính bảo hộ cầm bảng kẹp ghi chép lực cắm đâm xuyên: cô trợ lý hoảng hốt trước đồ thị vết rách lan rộng nếu cố kéo giật gai ra.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chiếc lông nhọn sẽ từ từ xuyên thủng các lớp cơ má, đâm xuyên qua vòm họng, thậm chí di chuyển sâu vào trong lồng ngực làm thủng phổi hoặc đâm rách tâm thất của tim! Đã có rất nhiều ghi nhận thực địa về những con báo hoa mai trưởng thành khỏe mạnh bị chết". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: báo hoa mai há hốc mồm ôm mũi đầy gai nhọn kêu la thảm thiết: báo hoa mai nằm bẹp gí ôm mõm sưng phù vì hàng chục mũi gai găm sâu.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "đói thảm khốc chỉ vì vài chiếc lông nhím cắm sâu vào hàm dưới làm nhiễm trùng mưng mủ, khiến miệng sưng to biến dạng không thể nào há ra để nhai thịt được nữa. Một đòn trả đũa tàn nhẫn được lập trình để kết liễu kẻ săn mồi sau nhiều ngày hành hạ! Những". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: chú ngơ ngác gãi đầu hoảng hốt khi chạm phải đầu gai nhọn: chú ngơ ngác toát mồ hôi hột rụt tay lại không dám chạm vào đuôi nhím.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "kẻ săn mồi khát nước màu như báo sư tử hay chó sói đồng cỏ một khi dính phải bẫy chông này thường phải trải qua những tuần lễ đau đớn tột cùng trước khi bị cướp đi hơi thở cuối cùng trong sự bất lực. Đặc biệt hơn nữa, phần gốc của lông nhím nối với". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: sơ đồ cắt lớp vi phẫu mũi gai 30.000 ngạnh vảy xếp chồng kiểu lưỡi câu ngạnh ngược: mô hình 3D cho thấy mũi gai xuyên qua lớp mỡ tiến dần đến mạch nước màu lớn.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nang lông rất lỏng lẻo. Lớp màng cơ dưới da của Pháo Đài Tự Hành có khả năng chủ động co thắt để dựng đứng toàn bộ 30.000 mũi tên lên khi bị đe dọa, tạo ra tiếng xào xạc đanh thép cảnh báo. Khi kẻ địch chạm phải, các sợi lông này sẽ tự động". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: chú nhím lông nhọn Bắc Mỹ hoạt hình ngộ nghĩnh (lưng mang bộ giáp 30.000 gai nhọn đính ngạnh ngược, biểu cảm tự tin đắc thắng): chú nhím quay lưng vẫy đuôi chào tạm biệt kẻ bại trận đầy ung dung.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tách rời khỏi gốc một cách êm ái, chuyển giao toàn bộ gánh nặng vũ khí sang cơ thể đối thủ mà không làm tổn thương dù chỉ một tế bào biểu bì của chú nhím! Hệ thống cơ dựng lông này được điều khiển bởi các xung thần kinh cực kỳ nhạy bén, chỉ mất chưa đầy 0.1s để chuyển từ trạng thái nằm xuôi sang tư thế pháo đài xòe gai sẵn sàng nghênh chiến.". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: kỹ sư trưởng xưởng vũ khí mặc áo giáp chống đâm cầm kính hiển vi soi ngạnh gai chú nhím lông nhọn Bắc Mỹ hoạt hình ngộ nghĩnh (lưng mang bộ giáp 30.000 gai nhọn đính ngạnh ngược, biểu cảm tự tin đắc thắng): kỹ sư chuyển hồ sơ sang phân tích thành phần hóa học của lớp phủ thân gai.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Có một nghịch lý kỹ thuật vô cùng hóc búa được đặt ra cho ban thiết kế sinh học: Nếu mang trên mình 30.000 mũi tên chết chóc có ngạnh ngược nguy hiểm như". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: sơ đồ màng bọc axit béo kháng sinh tự nhiên phủ bóng loáng thân gai: sơ đồ quang phổ huỳnh quang phát hiện lớp màng axit béo kháng sinh bọc ngoài thân gai.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "vậy, làm thế nào để Pháo Đài Tự Hành không vô tình tự đâm chết chính mình trong những sinh hoạt hàng ngày? Loài nhím này rất thích leo trèo lên những cành cây cao để gặm vỏ cây non và ăn quả ngọt, nhưng chúng lại nổi tiếng là những". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: kỹ sư trưởng xưởng vũ khí mặc áo giáp chống đâm cầm kính hiển vi soi ngạnh gai: kỹ sư nhỏ giọt vi khuẩn tụ cầu lên thân gai thấy vi khuẩn bị tiêu diệt hoàn toàn.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "kẻ vụng về, thường xuyên bị trượt chân và ngã từ trên ngọn cây cao chót vót xuống mặt đất đá lởm chởm. Trọng lượng 10kg với đôi chân ngắn cũn cỡn khiến những bước leo trèo trên các cành cây sồi hay phong cao vút luôn tiềm ẩn rủi ro". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: cô trợ lý kỹ thuật đeo kính bảo hộ cầm bảng kẹp ghi chép lực cắm đâm xuyên: cô trợ lý ngạc nhiên trước cơ chế tự bảo vệ: nhím ngã từ cây cao gai tự cắm vào mình không bị nhiễm trùng.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "té ngã cực kỳ cao đối với cỗ máy bọc thép này. Khi ngã từ trên cao xuống, không ít lần những chiếc lông nhọn của chính nó bị gãy gập và đâm ngược vào đùi hoặc bụng của nó. Nhưng kỳ diệu thay, các vết thương này hầu như không". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: chú nhím lông nhọn Bắc Mỹ hoạt hình ngộ nghĩnh (lưng mang bộ giáp 30.000 gai nhọn đính ngạnh ngược, biểu cảm tự tin đắc thắng): chú nhím trèo tót lên ngọn cây cao 10 mét ăn búp non vô tư không sợ ngã.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bao giờ bị nhiễm trùng hay mưng mủ! Các nhà hóa sinh học phát hiện ra rằng, bao phủ bên ngoài mỗi chiếc lông nhím là một lớp màng axit béo tự nhiên đậm đặc, chứa các hợp chất kháng khuẩn cực mạnh có khả năng tiêu diệt hoàn toàn các". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: chú ngơ ngác gãi đầu hoảng hốt khi chạm phải đầu gai nhọn: chú ngơ ngác ôm đầu thở phào khi biết nhím tự trang bị bảo hiểm y tế cho chính mình.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "loại vi khuẩn gram dương nguy hiểm. Lớp mỡ kháng sinh này hoạt động như một loại thuốc mỡ bôi vết thương được quét sẵn lên từng mũi tên! Lớp mỡ kháng khuẩn này gồm hỗn hợp các chuỗi axit béo tự do phức tạp, có khả năng ức chế màng". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: sơ đồ màng bọc axit béo kháng sinh tự nhiên phủ bóng loáng thân gai: công thức hóa học của axit free fatty acid phủ đều bề mặt từng chiếc gai nhọn.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tế bào của các loại vi khuẩn nguy hiểm nhất như tụ cầu vàng hay liên cầu khuẩn trong môi trường tự nhiên. Khi chiếc lông đâm vào chính cơ thể nó, lớp mỡ kháng khuẩn lập tức khử trùng vết thương tại chỗ, giúp mô thịt tự co lại và". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: bé con đội mũ bảo hộ tò mò chỉ tay vào chùm gai nhím xòe nan quạt: bé con giơ ngón tay cái tán thưởng trí thông minh kỳ diệu của mẹ thiên nhiên.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "phục hồi nhanh chóng mà không gây nguy hiểm tính mạng. Thiên nhiên không chỉ trang bị cho Pháo Đài Tự Hành một kho vũ khí công phá hàng đầu, mà còn chu đáo dán sẵn tem bảo hiểm y tế tự động cho người sử dụng, đảm bảo tính an". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: chú nhím lông nhọn Bắc Mỹ hoạt hình ngộ nghĩnh (lưng mang bộ giáp 30.000 gai nhọn đính ngạnh ngược, biểu cảm tự tin đắc thắng): chú nhím chải chuốt bộ lông gai bóng mượt dưới ánh hoàng hôn rừng lá kim.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "toàn tuyệt đối cho người lính mang vũ khí trong mọi tình huống rủi ro nghề nghiệp! Nhờ có lớp lá chắn hóa học này, những con nhím dù bị hàng chục vết đâm thủng do chính lông của mình gây ra khi rơi từ độ cao 10m vẫn thong thả đứng dậy, phủi bụi và tiếp tục kiếm ăn như chưa từng có chuyện gì xảy ra.". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: kỹ sư trưởng xưởng vũ khí mặc áo giáp chống đâm cầm kính hiển vi soi ngạnh gai: kỹ sư chuẩn bị bóc tách cấu trúc vật liệu xốp hấp thụ xung lực bên trong lõi gai.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy cầm một nắm lông nhím lên tay và các bạn sẽ phải kinh ngạc trước trọng lượng của chúng! 30.000 mũi tên bọc kín toàn thân nhưng tổng". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: sơ đồ cắt lớp vi phẫu mũi gai 30.000 ngạnh vảy xếp chồng kiểu lưỡi câu ngạnh ngược: sơ đồ cắt ngang lõi gai nhím: vỏ keratin cứng bọc ngoài cấu trúc xốp bọt biển siêu nhẹ.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "khối lượng của chúng chỉ chiếm chưa đầy 5% trọng lượng cơ thể chú nhím. Nếu những chiếc lông này là những thanh xương đặc cứng, Pháo Đài Tự Hành sẽ bị đè bẹp dí dưới sức nặng của chính mình và không". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: kỹ sư trưởng xưởng vũ khí mặc áo giáp chống đâm cầm kính hiển vi soi ngạnh gai: kỹ sư dùng máy ép thủy lực kiểm tra độ chịu uốn cong đàn hồi tuyệt vời của gai.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "thể nào nhấc nổi bốn chân để di chuyển. Bí quyết nằm ở cấu trúc vật liệu rỗng bên trong thân lông! Một chuẩn mực trọng lượng vàng mà các kỹ sư chế tạo áo giáp chống đạn thế giới tự nhiên hiện đại luôn". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: cô trợ lý kỹ thuật đeo kính bảo hộ cầm bảng kẹp ghi chép lực cắm đâm xuyên: cô trợ lý cân mẫu gai chỉ nặng 0.3g nhưng chịu được tải trọng uốn gấp hàng trăm lần.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "khao khát đạt được nhưng vẫn chưa thể tối ưu hóa trọn vẹn như thiên nhiên. Cắt ngang thân của một chiếc lông, chúng ta sẽ thấy một lớp vỏ ngoài bằng chất sừng keratin cực kỳ cứng cáp và chịu lực uốn". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: chú nhím lông nhọn Bắc Mỹ hoạt hình ngộ nghĩnh (lưng mang bộ giáp 30.000 gai nhọn đính ngạnh ngược, biểu cảm tự tin đắc thắng): chú nhím cuộn tròn thành quả cầu gai bất khả xâm phạm trước mọi cú cắn xé.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nắn tuyệt vời. Nhưng bên trong lòng ống lại là một ma trận bọt xốp khí rỗng li ti, đan xen nhau theo cấu trúc tổ ong tổ mối. Cấu trúc composite này vừa tối ưu hóa độ cứng chống cong vênh khi". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: báo hoa mai há hốc mồm ôm mũi đầy gai nhọn kêu la thảm thiết: báo hoa mai ngậm ngùi bỏ đi với cái mũi nham nhở gai không thể đụng vào pháo đài.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "va đập, vừa biến từng chiếc lông thành một khoang chứa khí tí hon. Nhờ có hàng chục ngàn khoang khí này, chú nhím khi rơi xuống nước sẽ nổi bồng bềnh như một chiếc phao cứu sinh tự nhiên! Tỷ trọng của". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: sơ đồ cắt lớp vi phẫu mũi gai 30.000 ngạnh vảy xếp chồng kiểu lưỡi câu ngạnh ngược: ứng dụng vật liệu phỏng sinh học vào áo giáp chống đạn và mũ bảo hiểm tương lai.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "mỗi chiếc lông chỉ đạt khoảng 0.3g trên một xăng-ti-mét khối, nhẹ hơn cả gỗ bấc và hoàn toàn nổi trên mặt nước mà không cần bất kỳ sự hỗ trợ cơ học nào khác. Nó có thể thong thả bơi qua những". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: chú ngơ ngác gãi đầu hoảng hốt khi chạm phải đầu gai nhọn: chú ngơ ngác vỗ tay thán phục bộ giáp composite đẳng cấp vũ trụ.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "con sông lớn mà không sợ bị chìm nghỉm, vừa có thể xòe gai đẩy lùi lũ cá săn mồi dưới nước. Một thiết kế vật lý siêu nhẹ, siêu cứng và đa năng vượt xa những tấm áo giáp chống đạn tân". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: chú nhím lông nhọn Bắc Mỹ hoạt hình ngộ nghĩnh (lưng mang bộ giáp 30.000 gai nhọn đính ngạnh ngược, biểu cảm tự tin đắc thắng): chú nhím nháy mắt tự tin giữa vòng hào quang laser bảo vệ.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tiến nhất mà con người từng chế tạo trong các phòng thí nghiệm thế giới tự nhiên tối tân! Khi mùa lũ về trên những cánh rừng Bắc Mỹ, hình ảnh những chú nhím bập bềnh trôi qua dòng nước cuộn xiết chính là minh chứng sống động nhất cho đỉnh cao của công nghệ phao sinh học tự nhiên.". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: kỹ sư trưởng xưởng vũ khí mặc áo giáp chống đâm cầm kính hiển vi soi ngạnh gai chú nhím lông nhọn Bắc Mỹ hoạt hình ngộ nghĩnh (lưng mang bộ giáp 30.000 gai nhọn đính ngạnh ngược, biểu cảm tự tin đắc thắng): kỹ sư đóng bản vẽ thiết kế hoàn thành ca đánh giá pháo đài rải gai.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Từ 30.000 mũi tên ngạnh ngược giảm lực đâm 54%, cơ chế bánh cóc một chiều tự rút sâu vào thớ thịt kẻ thù, lớp mỡ kháng khuẩn tự chữa". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: chú nhím lông nhọn Bắc Mỹ hoạt hình ngộ nghĩnh (lưng mang bộ giáp 30.000 gai nhọn đính ngạnh ngược, biểu cảm tự tin đắc thắng): chú nhím lông nhọn bước ra tiền cảnh uy nghiêm giữa ánh sáng hoàng hôn rừng ôn đới.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "lành vết thương khi ngã cây, cho đến cấu trúc lõi xốp composite siêu nhẹ bập bềnh trên mặt nước, Pháo Đài Tự Hành đã dạy cho chúng ta một bài học sâu sắc về nghệ thuật phòng thủ trong tự nhiên. Nó không". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: sơ đồ cắt lớp vi phẫu mũi gai 30.000 ngạnh vảy xếp chồng kiểu lưỡi câu ngạnh ngược: tổng kết 4 công nghệ lõi: ngạnh nano một chiều, tự khoan sâu, kháng sinh tự thân và lõi composite.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bao giờ chủ động gây hấn hay tấn công ai trước, nó chỉ lẳng lặng gặm vỏ cây giữa rừng già, nhưng bất kỳ kẻ nào ngạo mạn muốn biến nó thành con mồi đều sẽ phải trả giá bằng cả mạng sống của". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: kỹ sư trưởng xưởng vũ khí mặc áo giáp chống đâm cầm kính hiển vi soi ngạnh gai: kỹ sư trưởng giơ bản thiết kế hoàn hảo lấy cảm hứng từ bậc thầy cơ khí thiên nhiên.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "mình. Nó không cần phải phô trương nanh vuốt hay rống lên những tiếng gầm gừ đe dọa, bởi vì tự bản thân lớp áo giáp của nó đã là một lời cảnh cáo đanh thép nhất cho mọi kẻ nuôi ý đồ xâm". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: cô trợ lý kỹ thuật đeo kính bảo hộ cầm bảng kẹp ghi chép lực cắm đâm xuyên: cô trợ lý chào tạm biệt khán giả cùng chú nhím đáng yêu.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "phạm. Trong cuộc sống và thương trường cũng vậy! Sức mạnh đích thực không nằm ở việc bạn đi đe dọa hay lấn lướt người khác, mà nằm ở năng lực tự bảo vệ vững chắc và những ranh giới thép không thể bị". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: bé con đội mũ bảo hộ tò mò chỉ tay vào chùm gai nhím xòe nan quạt: bé con mỉm cười giơ biểu tượng like kêu gọi bảo vệ động vật hoang dã.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "xâm phạm! Hãy trang bị cho mình một nội lực thâm hậu, sự điềm tĩnh kiên định và một cơ chế bảo vệ thông minh như chú nhím nhỏ bé giữa rừng sâu nhé! Bạn thấy chi tiết kỹ thuật nào của Pháo Đài". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: chú nhím lông nhọn Bắc Mỹ hoạt hình ngộ nghĩnh (lưng mang bộ giáp 30.000 gai nhọn đính ngạnh ngược, biểu cảm tự tin đắc thắng): chú nhím quay đầu nháy mắt lắc đuôi xào xạc tạo âm thanh thương hiệu.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tự Hành tinh vi nhất: Những chiếc ngạnh ngược microscopic hay lớp mỡ kháng sinh tự chữa lành? Hãy chia sẻ quan điểm của bạn bên dưới nhé! Còn ở tập tiếp theo, chúng ta sẽ bước vào đấu trường La Mã đỉnh cao". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: : poster nghệ thuật tổng kết Pháo Đài Tự Hành với dòng chữ khoa học ấn tượng.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "để giải mã một gã khổng lồ nâng vật nặng 800kg dù chỉ ăn chay nhai lá cây! Hãy học cách xây dựng những giá trị vững chắc từ bên trong và thiết lập những ranh giới bảo vệ kiên cố cho bản thân, để có thể tự tin vững bước giữa một thế giới đầy biến động và cạnh tranh khốc liệt!". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: kỹ sư trưởng xưởng vũ khí mặc áo giáp chống đâm cầm kính hiển vi soi ngạnh gai: khung hình chuyển tiếp hé lộ hồ sơ bí ẩn của võ sĩ giác đấu rừng già tập tiếp theo.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Tại sao chỉ một chiếc lông nhím nhỏ bé cắm vào mõm cũng đủ sức hạ". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng: chú nhím lông nhọn Bắc Mỹ hoạt hình đội mũ bảo hộ kỹ sư cầm mũi lao gai phát sáng nháy mắt tự tin.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "gục cả một con báo hoa mai hung dữ?! Hãy nhìn Pháo Đài Tự Hành với 30.000 mũi tên chết chóc này xem! Nhím". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng báo hoa mai há hốc mồm ôm mũi đầy gai nhọn kêu la thảm thiết: báo hoa mai lao vào vồ nhưng bị 30.000 mũi gai nhọn xòe nan quạt chặn đứng.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "hoàn toàn không hề bắn lông từ xa như trong phim hoạt hình đâu nhé! Dưới kính hiển vi điện tử quét, đầu mỗi". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: sơ đồ cắt lớp vi phẫu mũi gai 30.000 ngạnh vảy xếp chồng kiểu lưỡi câu ngạnh ngược: kính hiển vi điện tử SEM phóng đại ngọn gai với hàng nghìn ngạnh vảy xếp ngược vát 45 độ.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "chiếc lông nhím chứa tới 800 chiếc ngạnh ngược siêu nhỏ xếp lớp như lưỡi móc câu! Khi đâm vào thịt, các ngạnh này". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: kỹ sư trưởng xưởng vũ khí mặc áo giáp chống đâm cầm kính hiển vi soi ngạnh gai: kỹ sư đo cảm biến lực: cắm vào giảm 54% lực nhưng rút ra cần lực gấp 3 lần.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "nép sát giúp giảm 54% lực đâm, nhưng khi rút ra thì bung nở móc chặt, làm tăng lực rút lên gấp 3 lần!". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: sơ đồ cắt lớp vi phẫu mũi gai 30.000 ngạnh vảy xếp chồng kiểu lưỡi câu ngạnh ngược: mô hình mô cơ rung giật khiến ngạnh gai tự khoan sâu 1mm mỗi giờ không thể rút.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Đáng sợ hơn cả, các cử động cơ bắp của con thú săn mồi sẽ vô tình đẩy chiếc lông tự rút sâu vào". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: sơ đồ màng bọc axit béo kháng sinh tự nhiên phủ bóng loáng thân gai: thân gai phủ lớp axit béo kháng sinh tự nhiên giúp nhím ngã trúng gai mình không nhiễm trùng.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "bên trong cơ thể với tốc độ 1mm mỗi giờ, đâm thủng vòm họng và tim phổi kẻ địch! Đã thế, trên thân lông". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: sơ đồ cắt lớp vi phẫu mũi gai 30.000 ngạnh vảy xếp chồng kiểu lưỡi câu ngạnh ngược: cấu trúc vật liệu composite lõi xốp bọt biển siêu nhẹ chịu lực va đập cực đỉnh.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "còn phủ lớp mỡ kháng sinh tự nhiên để nhím tự chữa lành khi lỡ bị lông đâm vào người! Một cỗ máy bọc thép sinh học với đòn phản công tàn khốc bậc nhất tự nhiên!". Bố cục: Tactical Weapon Arsenal & Microscopic Bio-Armor Diagram style, carbon black blueprint and hazard yellow accents, bold graphic ink contours, technical weapon schematics, microscopic SEM electron microscope zoom overlays, sharp high-contrast studio lighting, clean solid background with tactical engineering callouts: chú nhím lông nhọn hoạt hình đeo kính bảo hộ kỹ sư cầm mũi lao gai phát sáng: chú nhím nháy mắt lắc đuôi xào xạc gửi thông điệp đỉnh cao pháo đài tự hành thiên nhiên.
```
</details>

<details><summary>S08b</summary>

```text
HÌNH S08b (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản phong cách Tactical Weapon Arsenal; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: Một cỗ máy bọc thép sinh học với đòn phản công tàn khốc bậc nhất tự nhiên! Bố cục: chú nhím hoạt hình ngộ nghĩnh kiêu hãnh xù trọn bộ giáp 30.000 gai nhọn phát sáng uy lực, tư thế phòng thủ bất khả xâm phạm
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/53 của video YouTube về Nhím Lông Nhọn). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa vẽ tay đặc trưng cho chủ đề, nét mực sắc nét, màu sắc tương phản cuốn hút, tối giản giàu tính biểu tượng khoa học; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú nhím lông nhọn Bắc Mỹ hoạt hình ngộ nghĩnh (lưng mang bộ giáp 30.000 gai nhọn đính ngạnh ngược, biểu cảm tự tin đắc thắng). 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/8 của video YouTube Shorts về Nhím Lông Nhọn). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa vẽ tay đặc trưng cho chủ đề, nét mực sắc nét, màu sắc tương phản cuốn hút, tối giản giàu tính biểu tượng khoa học; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú nhím lông nhọn Bắc Mỹ hoạt hình ngộ nghĩnh (lưng mang bộ giáp 30.000 gai nhọn đính ngạnh ngược, biểu cảm tự tin đắc thắng). 
```
</details>

## 7. SEO

- **title:** Bí Mật 30.000 Mũi Tên Nhím: Tự Rút Sâu Vào Thịt Hạ Gục Báo Hoa Mai?! | Tập 49
- **hook_paragraph:** Nhím Lông Nhọn mang trên mình 30.000 mũi tên tự tách gốc với cấu trúc vi ngạnh ngược giảm 54% lực đâm nhưng tăng gấp 3 lực rút. Tại sao cử động của con mồi lại khiến chiếc lông tự đâm sâu 1mm mỗi giờ xuyên thủng tim phổi?
- **question:** Bạn thấy cơ chế nào của Nhím Lông Nhọn đỉnh nhất: Vi ngạnh tự rút sâu hay lớp mỡ kháng sinh tự nhiên?
- **next_teaser:** Ở tập tiếp theo, chúng ta sẽ giải mã khối cơ bắp 800kg của Khỉ Đột Lưng Bạc dù chỉ ăn chay!
- **shorts_title:** Tại sao một chiếc lông nhím đủ sức hạ gục cả báo hoa mai?! 🦔 #shorts #nhim
- **shorts_desc:** Đầu lông nhím chứa 800 vi ngạnh ngược tự rút sâu 1mm mỗi giờ vào cơ thịt kẻ thù khiến báo hoa mai cũng phải chết thảm!
- **bullets:** 30.000 mũi tên chất sừng keratin tự tách gốc thụ động · Cấu trúc 800 ngạnh ngược microscopic giảm 54% lực đâm xuyên · Cơ chế bánh cóc tự rút sâu 1mm mỗi giờ vào thớ thịt kẻ thù · Lớp mỡ axit béo kháng sinh tự nhiên tự chữa lành vết thương khi ngã
- **tags:** nhím lông nhọn, nhim long nhon, porcupine, long nhim, nganh nguoc long nhim, the gioi dong vat, ve chuyen hoang da, dong vat ky thu, khoa hoc vui, giai ma dong vat, ky su vu khi, phao dai tu hanh
- **hashtags:** #NhimLongNhon #Porcupine #TheGioiDongVat #VeChuyenHoangDa #KhoaHoc #KySuVuKhi

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-49-nhim-long-nhon
python src/episode/pipeline.py tts    projects/tap-49-nhim-long-nhon     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-49-nhim-long-nhon     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-49-nhim-long-nhon     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-49-nhim-long-nhon              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-49-nhim-long-nhon --force
python scripts/beat_sheet.py projects/tap-49-nhim-long-nhon               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-49-nhim-long-nhon/audio/shorts.wav projects/tap-49-nhim-long-nhon/renders/tap-49-nhim-long-nhon_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-49-nhim-long-nhon
python src/episode/pipeline.py seo    projects/tap-49-nhim-long-nhon
python src/episode/episode_doc.py     projects/tap-49-nhim-long-nhon
```
