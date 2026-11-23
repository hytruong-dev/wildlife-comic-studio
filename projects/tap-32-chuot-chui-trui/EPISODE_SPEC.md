# TẬP 32 — CHUỘT CHŨI TRŨI · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-32-chuot-chui-trui`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-32-chuot-chui-trui`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F5` · **Persona giọng:** `nha_khoa_hoc` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Chuột Chũi Trũi |
| Tiêu đề YouTube | Sinh Vật Sống Ở Mức 0% Oxy & Miễn Nhiễm Hoàn Toàn Ung Thư?! \| Tập 32 |
| Video dài | `renders/tap-32-chuot-chui-trui_long.mp4` — 9:02.7 (542.7s) |
| Shorts | `renders/tap-32-chuot-chui-trui_shorts.mp4` — 0:50.5 (50.5s) |
| Thumbnail | `renders/tap-32-chuot-chui-trui_thumbnail.jpg` |
| Số hình | dài 79 beat / 79 ảnh riêng; Shorts 11 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.1**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/79 của video YouTube về Chuột Chũi Trũi). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa 2D Bio-Lab Schematic kết hợp hoạt hình châm biếm hài hước (Dark Comedy Scientific Illustration): nét mực đen đậm sắc sảo, phối hợp các chi tiết sơ đồ giải phẫu sinh học, bình thí nghiệm, lưới tọa độ tế bào và mảng màu tươi sáng tương phản cao (tím phòng lab, xanh lục bảo neon, vàng hổ phách và hồng phấn nhân vật); biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles). Nhân vật phụ cố định: cô trợ lý mèo hoạt hình đeo kính cận tròn, mặc áo blouse trắng phòng thí nghiệm, cầm bảng kẹp hồ sơ sinh học phát sáng; chú chuột bạch hoạt hình lông trắng mập mạp đeo nơ xanh, biểu cảm nhát gan hay giật mình thót tim; Nữ Hoàng Chuột Chũi hoạt hình to gấp đôi, đội vương miện vàng lấp lánh, mặc áo choàng nhung đỏ oai vệ chống nạnh hét ra lửa; nhân vật quái vật tế bào đột biến hoạt hình màu tím tròn xoe ngộ nghĩnh đội mũ sừng nhỏ, mặt mếu máo bất lực. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — CHÂN DUNG CỦ KHOAI TÂY BIẾT ĐI VÀ BỘ HÀM XUYÊN MÔI ĐÀO BÊ TÔNG
*Thẻ chương:* PHÒNG THÍ NGHIỆM CẤP 5: GIẢI MÃ MẪU VẬT XẤU XÍ NHẤT HÀNH TINH

*Badge:* `MẪU VẬT #32` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene01_p0.wav` (485 ký tự) · mood `tram_bi_an`

```text
Cảnh báo sinh học cấp độ năm! Chào mừng toàn thể hội đồng khoa học đã bước xuống phòng thí nghiệm ngầm tối mật của chúng tôi. Hôm nay, nằm trong lồng kính cường lực trước mặt quý vị không phải là một quái thú săn mồi hào nhoáng, mà là mẫu vật kỳ dị bậc nhất lịch sử tiến hóa: Chuột Chũi Trũi Đông Phi, danh pháp khoa học Hê-tê-rô-xê-pha-lút gla-bơ. Nhìn thoáng qua, chắc chắn ai cũng tưởng ai đó vừa đánh rơi một củ khoai tây luộc bị héo hoặc một cây xúc xích hồng nhăn nheo biết chạy!
```
**Part 1** → `audio/vs/scene01_p1.wav` (155 ký tự) · 🎭 cameo `co_tro_ly`

```text
Trợ lý phòng lab báo cáo: Mẫu vật dài tám đến mười xăng-ti-mét, nặng ba mươi lăm gam, trụi lông hoàn toàn nhưng chỉ số sinh tồn vượt mọi giới hạn sinh học!
```
**Part 2** → `audio/vs/scene01_p2.wav` (419 ký tự) · mood `hao_hung`

```text
[laughter] Đừng để vẻ ngoài xấu xí ma chê quỷ hờn của gã Dị Nhân Khoai Tây này đánh lừa các bạn! Dù cơ thể chỉ nhỉnh hơn ngón tay cái người lớn và đôi mắt ti hí gần như mù tịt dưới lòng đất tối đen, cơ thể nó lại là một cỗ máy đào hầm siêu hạng. Hãy nhìn vào hai chiếc răng cửa khổng lồ trắng hếu của nó mà xem: Răng của nó không mọc trong miệng như thú bình thường, mà đâm xuyên thẳng qua lớp môi nhô hẳn ra bên ngoài!
```
**Part 3** → `audio/vs/scene01_p3.wav` (427 ký tự) · mood `don_dap`

```text
Thiết kế kỳ quặc này cho phép đôi môi của chuột chũi khép chặt hoàn toàn phía sau răng. Nhờ vậy, khi nó dùng răng đục khoét lớp đất cứng như bê tông khô dưới lòng đất châu Phi, chẳng có hạt đất cát nào có thể lọt vào cổ họng! Đỉnh cao hơn nữa, khối cơ hàm của nó chiếm tới hai mươi lăm phần trăm tổng lượng cơ bắp toàn cơ thể, và hai chiếc răng cửa hàm dưới có thể điều khiển tách rời độc lập y hệt như một đôi đũa gắp thức ăn!
```
**Part 4** → `audio/vs/scene01_p4.wav` (381 ký tự) · mood `hao_hung`

```text
Chưa dừng lại ở đó, dù cơ thể trụi lủi nhưng dọc sườn và đuôi của nó lại mọc lưa thưa khoảng bốn mươi sợi lông xúc giác cực nhạy hoạt động như một dàn radar ba trăm sáu mươi độ. Nhờ dàn cảm biến này, nó có thể chạy lùi trong đường hầm tối đen với tốc độ nhanh chẳng kém gì khi chạy tiến! Nhưng đó mới chỉ là màn khởi động trước khi bước vào năm bài thử nghiệm cực hạn điên rồ nhất!
```

### scene02 — VÔ CẢM TRƯỚC AXIT ĂN MÒN VÀ CHẤT CAY ỚT HIỂM NHỜ KHÓA KÊNH THẦN KINH
*Thẻ chương:* THỬ NGHIỆM CẤP ĐỘ 1: TẠT AXIT VÀ ỚT HIỂM — PHẢN ỨNG BẰNG KHÔNG

*Badge:* `THỬ NGHIỆM CẤP 1` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene02_p0.wav` (421 ký tự) · mood `don_dap`

```text
Bắt đầu bài thử nghiệm khắc nghiệt cấp độ một: Kiểm tra ngưỡng chịu đau hóa học! Năm hai ngàn không trăm linh tám, giáo sư Tô-mát Pác tại Đại học Y-li-noi và giáo sư Ga-ri Lê-uyn đã tiến hành một thí nghiệm khiến giới thần kinh học sững sờ. Khi nhỏ dung dịch axit nồng độ thấp hoặc bôi hoạt chất cáp-xai-xin siêu cay chiết xuất từ ớt hiểm lên da các loài chuột bình thường, chúng lập tức nhảy dựng lên vì bỏng rát dữ dội.
```
**Part 1** → `audio/vs/scene02_p1.wav` (107 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Ủa các bác sĩ nhỏ nước gì mát thế? Cho xin thêm vài giọt ớt hiểm làm nước chấm củ rễ cây luôn được không ạ?
```
**Part 2** → `audio/vs/scene02_p2.wav` (396 ký tự) · mood `hao_hung`

```text
[surprise-oh] Chẳng hề nhăn mặt, chẳng hề giật mình! Mẫu vật Chuột Chũi Trũi hoàn toàn trơ lì như không hề có chuyện gì xảy ra! Khi mổ xẻ hệ thần kinh dưới kính hiển vi phân tử, các nhà khoa học phát hiện sợi thần kinh cảm giác dưới da của nó hoàn toàn thiếu vắng một hợp chất truyền tin mang tên Sắp-xtần Pê — vốn là chất phát tín hiệu báo động cảm giác bỏng rát lên não bộ ở mọi loài thú có vú.
```
**Part 3** → `audio/vs/scene02_p3.wav` (529 ký tự) · mood `tram_bi_an`

```text
Độc đáo hơn nữa, nghiên cứu năm hai ngàn không trăm mười một trên tạp chí Sai-ần đã chỉ ra rằng kênh truyền tín hiệu đau Na Vê một chấm bảy của loài chuột này đã bị đột biến đảo ngược. Ở con người, khi gặp axit, kênh này mở toang để bắn tín hiệu đau đớn điên cuồng. Nhưng ở Chuột Chũi Trũi, chính phân tử axit lại biến thành chiếc chìa khóa đóng sập kênh Na Vê một chấm bảy lại! Tức là axit đối với nó chẳng khác nào thuốc gây tê miễn phí, giúp nó sống khỏe re dưới đáy hang ngầm ngập tràn khí các-bô-níc đậm đặc gây axit hóa mô!
```

### scene03 — HÓA THÀNH THỰC VẬT ĐỐT ĐƯỜNG FRUCTOSE SỐNG 18 PHÚT Ở MỨC 0% OXY
*Thẻ chương:* THỬ NGHIỆM CẤP ĐỘ 2: RÚT CẠN 100% OXY TRONG BUỒNG KÍN SUỐT 18 PHÚT

*Badge:* `THỬ NGHIỆM CẤP 2` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene03_p0.wav` (411 ký tự) · mood `tram_bi_an`

```text
Nếu bài kiểm tra hóa chất vẫn chưa đủ làm khó mẫu vật, chúng ta nâng mức độ lên thử nghiệm cấp độ hai: Buồng chân không rút cạn sạch không phần trăm oxy! Hãy tưởng tượng dưới lòng đất sâu hai mét, ba trăm con chuột chũi chen chúc nhau trong một đường hầm bịt kín bưng chẳng có khe gió. Nồng độ oxy ở đó thấp đến mức bất kỳ người hay con chuột bạch nào bước vào cũng sẽ ngất lịm và tử vong chỉ sau sáu mươi giây.
```
**Part 1** → `audio/vs/scene03_p1.wav` (156 ký tự) · 🎭 cameo `co_tro_ly`

```text
Cảnh báo đỏ: Nồng độ oxy trong buồng thử nghiệm đã tụt về không phần trăm! Nhịp tim mẫu vật giảm từ hai trăm nhịp một phút xuống còn năm mươi nhịp một phút!
```
**Part 2** → `audio/vs/scene03_p2.wav` (436 ký tự) · mood `don_dap`

```text
Một phút trôi qua... năm phút... mười phút... rồi đúng mười tám phút hoàn toàn chẳng có lấy một phân tử oxy nào! Mẫu vật nằm bất động trong trạng thái đình trệ sinh học. Thế nhưng ngay khoảnh khắc van oxy được mở trở lại, gã Dị Nhân Khoai Tây lập tức vươn vai đứng dậy đi lại tỉnh bơ mà không hề bị tổn thương một tế bào não hay cơ tim nào! Bí mật nằm ở công trình chấn động công bố trên tạp chí Sai-ần năm hai ngàn không trăm mười bảy.
```
**Part 3** → `audio/vs/scene03_p3.wav` (580 ký tự) · mood `hao_hung`

```text
[surprise-wa] Khi thiếu oxy, mọi loài động vật có vú đều bị tắc nghẽn dây chuyền đốt đường gờ-lu-cô-zơ làm tế bào não chết ngạt. Nhưng Chuột Chũi Trũi đã thực hiện một cú chuyển đổi sinh học không tưởng: Nó bật công tắc chuyển sang đốt đường phờ-rắc-tô-zơ — tức là loại đường trái cây — thông qua các bơm phân tử chuyên biệt để nuôi sống não bộ mà không cần oxy! Đây vốn là cơ chế trao đổi chất độc quyền của giới thực vật! Nói cách khác, khi hết sạch không khí, nó tạm thời biến thành một củ khoai tây thực thụ để chờ thời, rồi lại hoàn hồn làm động vật khi có gió về! [laughter]
```

### scene04 — SIÊU KEO HYALURONIC ACID HMW-HA VÀ KHÓA KÉP CHỐNG UNG THƯ TUYỆT ĐỐI
*Thẻ chương:* THỬ NGHIỆM CẤP ĐỘ 3: KHIÊN CHẮN PHÂN TỬ BÓP NGHẸT MỌI KHỐI U

*Badge:* `THỬ NGHIỆM CẤP 3` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene04_p0.wav` (435 ký tự) · mood `hao_hung`

```text
Chuyển sang thử nghiệm cấp độ ba: Khả năng kháng bệnh nan y! Thông thường, tới hơn bảy mươi phần trăm các loài chuột trong phòng thí nghiệm sẽ tử vong vì các khối u ung thư khi về già. Thế nhưng khi giáo sư Vê-ra Goóc-bu-nô-va và cộng sự tại Đại học Rô-chét-xtơ theo dõi hàng ngàn cá thể Chuột Chũi Trũi suốt hàng chục năm trời, họ phát hiện một con số gây chấn động y học thế giới: Hầu như không có bất kỳ cá thể nào mắc bệnh ung thư!
```
**Part 1** → `audio/vs/scene04_p1.wav` (479 ký tự) · mood `don_dap`

```text
Khi kiểm tra dịch nuôi cấy tế bào của chúng vào năm hai ngàn không trăm mười ba, các nhà nghiên cứu thấy dung dịch cứ đặc quánh và nhớt nhầy như hồ dán làm tắc nghẽn cả ống hút phòng lab! Thủ phạm chính là hợp chất đường siêu phân tử Hy-a-lu-rô-níc A-xít khối lượng cực cao, viết tắt là Hát Mờ Đắp-bờ-liu Hát A. Ở con người, hợp chất này vốn được dùng làm chất giữ ẩm trong mỹ phẩm dưỡng da, nhưng ở Chuột Chũi Trũi, chuỗi phân tử của nó dài và nặng gấp năm lần so với của người!
```
**Part 2** → `audio/vs/scene04_p2.wav` (340 ký tự) · mood `am_ap`

```text
Lớp siêu keo Hát Mờ Đắp-bờ-liu Hát A này tạo thành một mạng lưới lồng sắt đàn hồi cực kỳ dày đặc bao bọc quanh từng tế bào của Dị Nhân Khoai Tây. Nhờ lớp đệm siêu đàn hồi đó mà làn da của nó mới nhăn nheo và co giãn rộng thùng thình, giúp nó luồn lách và quay đầu một trăm tám mươi độ ngay trong lòng đường hầm chật hẹp mà không bị rách da!
```
**Part 3** → `audio/vs/scene04_p3.wav` (517 ký tự) · mood `tram_bi_an`

```text
Quan trọng hơn cả, mạng lưới siêu keo này kích hoạt cơ chế ức chế tiếp xúc sớm thông qua bộ khóa bảo vệ kép gồm hai gen pê mười sáu và pê hai mươi bảy. Ở cơ thể người, chúng ta chỉ có một ổ khóa pê hai mươi bảy, nên khi tế bào đột biến nhân lên chật chội, khối u vẫn có thể phá khóa phát triển. Còn ở Chuột Chũi Trũi, ngay khi vài tế bào bất thường vừa chạm nhẹ vào nhau, ổ khóa thứ hai pê mười sáu lập tức sập xuống, ra lệnh đóng băng toàn bộ quá trình phân chia, bóp nghẹt mầm mống ung thư ngay từ trong trứng nước!
```

### scene05 — ĐẾ CHẾ NỮ HOÀNG ĐỘC TÀI, NHÀ VỆ SINH CHUNG VÀ TỬ HUYỆT MÁU LẠNH
*Thẻ chương:* THỬ NGHIỆM CẤP ĐỘ 4: BÍ MẬT XÃ HỘI CÔN TRÙNG & TỬ HUYỆT TRỜI ĐÁNH

*Badge:* `THỬ NGHIỆM CẤP 4` · *mood mặc định:* `bi_hai`

**Part 0** → `audio/vs/scene05_p0.wav` (434 ký tự) · mood `hao_hung`

```text
Bước vào thử nghiệm cấp độ bốn: Quan sát hành vi xã hội! Năm một ngàn chín trăm tám mươi mốt, nhà sinh vật học Gien-ni-phơ Gia-vít đã phát hiện Chuột Chũi Trũi là loài thú có vú hiếm hoi trên Trái Đất sống theo mô hình xã hội côn trùng chân chính y hệt loài kiến và mối! Một vương quốc ngầm dài từ ba đến năm ki-lô-mét chứa tới ba trăm cá thể, nhưng chỉ có duy nhất một Nữ Hoàng tối cao được phép sinh con đẻ cái cùng ba gã hoàng phu!
```
**Part 1** → `audio/vs/scene05_p1.wav` (144 ký tự) · 🎭 cameo `ba_trum`

```text
Tất cả nghe lệnh ta! Đội công nhân xếp hàng đào đất! Đội chiến binh ra chặn cửa hang! Đứa nào dám yêu đương lén lút ta húc cho văng vào vách đá!
```
**Part 2** → `audio/vs/scene05_p2.wav` (485 ký tự) · mood `bi_hai`

```text
[laughter] Nữ Hoàng cai trị bằng nắm đấm sắt đúng nghĩa đen! Mỗi lần mang thai, các đốt xương sống của Nữ Hoàng tự động kéo dài ra như lò xo để chứa tới gần ba mươi đứa con trong bụng. Trong khi đó, hàng trăm thần dân còn lại bị Nữ Hoàng dùng áp lực cơ học húc đẩy liên tục khiến hormone sinh sản bị khóa chặt suốt đời! Đội công nhân phải xếp thành một dây chuyền băng tải sống: con đầu tiên dùng răng khoét đất, hàng chục con phía sau cứ thế đá đất qua háng nhau chạy tít ra cửa hang!
```
**Part 3** → `audio/vs/scene05_p3.wav` (370 ký tự) · mood `bi_hai`

```text
Và chi tiết lầy lội nhất của đế chế này chính là quy định nhận diện công dân: Vì dưới hang tối đen như mực không nhìn thấy mặt nhau, cả ba trăm con chuột trong đàn đều phải lăn lộn vào chung một buồng nhà vệ sinh duy nhất! Nhờ tắm chung mùi chất thải đặc trưng của gia tộc, chúng nhận ra đồng đội ngay lập tức, kẻ lạ nào khác mùi mò vào sẽ bị đội chiến binh tóm cổ ngay!
```
**Part 4** → `audio/vs/scene05_p4.wav` (556 ký tự) · mood `tram_bi_an`

```text
Thế nhưng vị hoàng đế ngầm này lại mang một tử huyệt chí mạng: Chúng đã đánh mất hoàn toàn lớp mỡ nâu và khả năng tự điều chỉnh thân nhiệt của loài thú có vú, trở thành sinh vật biến nhiệt chẳng khác nào loài bò sát máu lạnh! Ở trong hang sâu nhiệt độ luôn ổn định quanh mức ba mươi độ C, nhưng nếu bị lôi ra ngoài trời lạnh dưới mười lăm độ C hoặc nắng nóng trên ba mươi lăm độ C, siêu dị nhân chống axit và ung thư của chúng ta sẽ lập tức đơ cứng vì sốc nhiệt! Để giữ ấm, cả đàn chỉ còn cách rúc vào nhau nằm chồng chất thành một đống khoai tây khổng lồ!
```

### scene06 — TUỔI THỌ 37 NĂM PHÁ VỠ ĐỊNH LUẬT LÃO HÓA GOMPERTZ VÀ HÉ LỘ TẬP 33
*Thẻ chương:* BÁO CÁO NGHIỆM THU CẤP 5: BÍ MẬT TRƯỜNG THỌ BẤT TỬ & CÂU ĐỐ TẬP 33

*Badge:* `THỬ NGHIỆM CẤP 5` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene06_p0.wav` (448 ký tự) · mood `hao_hung`

```text
Cuối cùng, bài thử nghiệm cấp độ năm cũng là đỉnh cao vĩ đại nhất của Dị Nhân Khoai Tây mang mã số ba mươi hai: Thử thách thời gian! Một con chuột nhắt có cùng kích thước chỉ sống được tối đa từ hai đến ba năm là già yếu qua đời. Thế nhưng Chuột Chũi Trũi có thể sống khỏe mạnh tới ba mươi bảy năm — tức là gấp hơn mười hai lần tuổi thọ dự kiến! Nếu quy đổi sang thước đo của con người, nó tương đương với một cụ già sống thọ tới hơn tám trăm tuổi!
```
**Part 1** → `audio/vs/scene06_p1.wav` (561 ký tự) · mood `am_ap`

```text
Năm hai ngàn không trăm mười tám, nhà sinh học Rô-sen Bắp-phen-xtên đã công bố dữ liệu theo dõi hơn ba ngàn cá thể suốt ba thập kỷ và chứng minh Chuột Chũi Trũi đã đập tan định luật lão hóa Gôm-pớt. Ở mọi sinh vật khác, càng lớn tuổi thì nguy cơ tử vong càng tăng theo cấp số nhân. Nhưng ở loài chuột này, một cụ chuột ba mươi tuổi vẫn có trái tim khỏe mạnh, mật độ xương rắn chắc và tế bào tự dọn rác hoàn hảo y hệt một thanh niên hai tuổi! Nó chính là chìa khóa vàng giúp y học nhân loại giải mã giấc mơ trường thọ và chiến thắng bệnh ung thư trong tương lai.
```
**Part 2** → `audio/vs/scene06_p2.wav` (365 ký tự) · mood `hao_hung`

```text
Hội đồng khoa học thân mến, sau năm cấp độ thử nghiệm điên rồ vừa rồi, bạn thấy siêu năng lực nào của Chuột Chũi Trũi đỉnh chóp nhất: Vô cảm trước axit nhờ khóa kênh thần kinh, hóa thành thực vật sống mười tám phút không cần oxy, hay lớp siêu keo Hát Mờ Đắp-bờ-liu Hát A bóp nghẹt mọi khối u ung thư? Hãy ghi ngay đánh giá của bạn xuống phần bình luận bên dưới nhé!
```
**Part 3** → `audio/vs/scene06_p3.wav` (484 ký tự) · mood `tram_bi_an`

```text
Và ngay trong hồ sơ tập ba mươi ba tiếp theo, chúng ta sẽ rời căn hầm nóng bức Đông Phi để bay tới vùng băng giá Bắc Cực lạnh âm hai mươi độ C! Tại đó có một quái kiệt lưỡng cư tự biến hai phần ba lượng nước trong cơ thể thành một cục nước đá cứng ngắc suốt tám tháng mùa đông: Tim ngừng đập hoàn toàn, máu ngừng chảy, não bộ tắt nguồn như đã chết, nhưng ngay khi nắng xuân vừa chạm tới lại tự rã đông nhảy nhót tỉnh bơ! Đố bạn đoán được sinh vật đóng băng bất tử tiếp theo này là ai?
```

### Shorts → `audio/vs/shorts.wav`

```text
Cảnh báo sinh học cấp độ năm! [surprise-oh] Tại sao loài chuột xấu xí nhăn nheo như củ khoai tây luộc này lại miễn nhiễm hoàn toàn với bệnh ung thư và sống sót mười tám phút không cần một giọt oxy nào? Đây là Chuột Chũi Trũi Đông Phi, siêu dị nhân bất tử dưới lòng đất! Khi các nhà khoa học theo dõi hàng ngàn cá thể suốt ba mươi bảy năm, họ sững sờ khi thấy chúng gần như không bao giờ mắc ung thư. Bí mật nằm ở chỗ tế bào của chúng tiết ra một chất siêu keo tên là Hy-a-lu-rô-níc A-xít có phân tử nặng gấp năm lần con người! Lớp siêu keo này kết hợp cùng bộ khóa gen kép pê mười sáu và pê hai mươi bảy, tạo thành chiếc lồng sắt khóa chặt và bóp nghẹt mọi tế bào khối u ngay từ khi mới chớm! Chưa hết, khi bị nhốt trong hầm kín không phần trăm oxy suốt mười tám phút, nó lập tức biến hình thành thực vật, đốt đường trái cây phờ-rắc-tô-zơ để nuôi não bộ mà chẳng cần hít thở! Một kiệt tác y sinh học giúp nó sống thọ tới ba mươi bảy năm!
```

**Whisper prompt:** `Chuột Chũi Trũi, Dị Nhân Khoai Tây, Heterocephalus glaber, Thomas Park, Gary Lewin, Vera Gorbunova, Andrei Seluanov, Rochelle Buffenstein, Jennifer Jarvis, Substance P, capsaicin, NaV1.7, Fructose, Glucose, GLUT5, Hyaluronic Acid, HMW-HA, p16, p27, Gompertz, Eusocial, 18 phút, 37 năm, 30 năm, 300 cá thể, 5km, 25%, 0% oxy, 200 nhịp/phút, 50 nhịp/phút, Ếch Gỗ Bắc Cực`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| mười tám phút | 18 phút |
| Mười tám phút | 18 phút |
| ba mươi bảy năm | 37 năm |
| Ba mươi bảy năm | 37 năm |
| ba mươi năm | 30 năm |
| Ba mươi năm | 30 năm |
| hai đến ba năm | 2-3 năm |
| Hai đến ba năm | 2-3 năm |
| hai mươi lăm phần trăm | 25% |
| Hai mươi lăm phần trăm | 25% |
| không phần trăm | 0% |
| Không phần trăm | 0% |
| năm phần trăm | 5% |
| Năm phần trăm | 5% |
| hai trăm nhịp một phút | 200 nhịp/phút |
| Hai trăm nhịp một phút | 200 nhịp/phút |
| năm mươi nhịp một phút | 50 nhịp/phút |
| Năm mươi nhịp một phút | 50 nhịp/phút |
| bảy mươi đến ba trăm | 70-300 |
| Bảy mươi đến ba trăm | 70-300 |
| ba trăm cá thể | 300 cá thể |
| Ba trăm cá thể | 300 cá thể |
| hai mươi bảy đến ba mươi | 27-30 |
| năm ki-lô-mét | 5km |
| Năm ki-lô-mét | 5km |
| ba đến năm ki-lô-mét | 3-5km |
| hai mét | 2m |
| Hai mét | 2m |
| tám đến mười xăng-ti-mét | 8-10cm |
| ba mươi lăm gam | 35g |
| mười lăm độ C | 15°C |
| ba mươi lăm độ C | 35°C |
| ba mươi độ C | 30°C |
| âm hai mươi độ C | -20°C |
| bốn mươi | 40 |
| bảy mươi phần trăm | 70% |
| một trăm tám mươi độ | 180° |
| ba trăm sáu mươi độ | 360° |
| tám trăm tuổi | 800 tuổi |
| tám tháng | 8 tháng |
| năm lần | 5 lần |
| Năm lần | 5 lần |
| mười lần | 10 lần |
| Mười lần | 10 lần |
| mười hai lần | 12 lần |
| sáu mươi giây | 60 giây |
| Sáu mươi giây | 60 giây |
| ba trăm con | 300 con |
| gần ba mươi | gần 30 |
| ba mươi tuổi | 30 tuổi |
| hai tuổi | 2 tuổi |
| một phút | 1 phút |
| năm phút | 5 phút |
| mười phút | 10 phút |
| năm một ngàn chín trăm tám mươi mốt | năm 1981 |
| năm hai ngàn không trăm linh tám | năm 2008 |
| năm hai ngàn không trăm mười một | năm 2011 |
| năm hai ngàn không trăm mười ba | năm 2013 |
| năm hai ngàn không trăm mười bảy | năm 2017 |
| năm hai ngàn không trăm mười tám | năm 2018 |
| ba ngàn | 3.000 |
| Ba ngàn | 3.000 |
| số ba mươi hai | số 32 |
| ba mươi hai | 32 |
| Ba mươi hai | 32 |
| tập ba mươi ba | Tập 33 |
| Tập ba mươi ba | Tập 33 |
| Hê-tê-rô-xê-pha-lút gla-bơ | Heterocephalus glaber |
| Tô-mát Pác | Thomas Park |
| Ga-ri Lê-uyn | Gary Lewin |
| Vê-ra Goóc-bu-nô-va | Vera Gorbunova |
| Rô-sen Bắp-phen-xtên | Rochelle Buffenstein |
| Gien-ni-phơ Gia-vít | Jennifer Jarvis |
| Y-li-noi | Illinois |
| Rô-chét-xtơ | Rochester |
| Sai-ần | Science |
| các-bô-níc | CO2 |
| Sắp-xtần Pê | Substance P |
| cáp-xai-xin | capsaicin |
| phờ-rắc-tô-zơ | Fructose |
| gờ-lu-cô-zơ | Glucose |
| Hy-a-lu-rô-níc A-xít | Hyaluronic Acid |
| Hát Mờ Đắp-bờ-liu Hát A | HMW-HA |
| Gôm-pớt | Gompertz |
| pê mười sáu | p16 |
| pê hai mươi bảy | p27 |
| Na Vê một chấm bảy | NaV1.7 |
| Hai mươi bảy đến ba mươi | 27-30 |
| Ba đến năm ki-lô-mét | 3-5km |
| Tám đến mười xăng-ti-mét | 8-10cm |
| Ba mươi lăm gam | 35g |
| Mười lăm độ C | 15°C |
| Ba mươi lăm độ C | 35°C |
| Ba mươi độ C | 30°C |
| Âm hai mươi độ C | -20°C |
| Bốn mươi | 40 |
| Bảy mươi phần trăm | 70% |
| Một trăm tám mươi độ | 180° |
| Ba trăm sáu mươi độ | 360° |
| Tám trăm tuổi | 800 tuổi |
| Tám tháng | 8 tháng |
| Mười hai lần | 12 lần |
| Ba trăm con | 300 con |
| Gần ba mươi | Gần 30 |
| Ba mươi tuổi | 30 tuổi |
| Hai tuổi | 2 tuổi |
| Một phút | 1 phút |
| Năm phút | 5 phút |
| Mười phút | 10 phút |
| Năm một ngàn chín trăm tám mươi mốt | Năm 1981 |
| Năm hai ngàn không trăm linh tám | Năm 2008 |
| Năm hai ngàn không trăm mười một | Năm 2011 |
| Năm hai ngàn không trăm mười ba | Năm 2013 |
| Năm hai ngàn không trăm mười bảy | Năm 2017 |
| Năm hai ngàn không trăm mười tám | Năm 2018 |
| Số ba mươi hai | Số 32 |
| hê-tê-rô-xê-pha-lút gla-bơ | Heterocephalus glaber |
| tô-mát Pác | Thomas Park |
| ga-ri Lê-uyn | Gary Lewin |
| vê-ra Goóc-bu-nô-va | Vera Gorbunova |
| rô-sen Bắp-phen-xtên | Rochelle Buffenstein |
| gien-ni-phơ Gia-vít | Jennifer Jarvis |
| y-li-noi | Illinois |
| rô-chét-xtơ | Rochester |
| sai-ần | Science |
| Các-bô-níc | CO2 |
| sắp-xtần Pê | Substance P |
| Cáp-xai-xin | Capsaicin |
| Phờ-rắc-tô-zơ | Fructose |
| Gờ-lu-cô-zơ | Glucose |
| hy-a-lu-rô-níc A-xít | Hyaluronic Acid |
| hát Mờ Đắp-bờ-liu Hát A | HMW-HA |
| gôm-pớt | Gompertz |
| Pê mười sáu | P16 |
| Pê hai mươi bảy | P27 |
| na Vê một chấm bảy | NaV1.7 |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · CHÂN DUNG CỦ KHOAI TÂY BIẾT ĐI VÀ BỘ HÀM XUYÊN MÔI ĐÀO BÊ TÔNG · 93.1s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:05.5 (5.5s) | L02 | Cảnh báo sinh học cấp độ năm! Chào mừng toàn thể hội đồng khoa học đã bước xuống phòng thí nghiệm ngầm tối mật của chúng tôi. |  | Bàn điều khiển phòng thí nghiệm sinh học: cô trợ lý mèo hoạt hình đeo kính cận tròn, mặc áo blouse trắng phòng thí nghiệm, cầm bảng kẹp hồ sơ sinh học phát sáng đang thuyết trình trước màn hình hologram chiếu sơ đồ giải phẫu bí ẩn, xung quanh là các bình thủy tinh sủi bọt xanh ngọc. KHÔNG có chú Chuột Chũi Trũi trong cảnh này. |
| b02 | 00:05.5–00:12.8 (7.3s) | L03 | Hôm nay, nằm trong lồng kính cường lực trước mặt quý vị không phải là một quái thú săn mồi hào nhoáng, mà là mẫu vật kỳ dị bậc nhất lịch sử tiến hóa: |  | Chiếc bệ kính cường lực phát sáng trong phòng lab: chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) đang nằm vắt chân chữ ngũ thư giãn, vừa gặm củ rễ cây vừa nháy mắt tinh nghịch dưới ánh đèn quét laser xa |
| b03 | 00:12.8–00:16.7 (4.0s) | L04 | Chuột Chũi Trũi Đông Phi, danh pháp khoa học Heterocephalus glaber. |  | Sơ đồ hồ sơ định danh Bio-Lab: Chân dung cận cảnh chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) nằm giữa khung lưới tọa độ giải phẫu màu tím, bên cạnh là bản đồ vùng sừng Đông Phi khô cằn. |
| b04 | 00:16.7–00:23.5 (6.8s) | L05 | Nhìn thoáng qua, chắc chắn ai cũng tưởng ai đó vừa đánh rơi một củ khoai tây luộc bị héo hoặc một cây xúc xích hồng nhăn nheo biết chạy! |  | Phép so sánh hài hước trên đĩa cân phòng lab: Một bên là củ khoai tây luộc nhăn nheo và cây xúc xích hồng, bên kia là chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) đang tạo dáng y hệt khiến cô trợ lý mè |
| b05 | 00:23.5–00:32.2 (8.7s) | L06 | Trợ lý phòng lab báo cáo: Mẫu vật dài 8-10cm, nặng 35g, trụi lông hoàn toàn nhưng chỉ số sinh tồn vượt mọi giới hạn sinh học! | **8-10cm** · chiều dài cơ thể · L/340 · [0.45, 0.55]<br>**35g** · cân nặng tí hon · R/400 · [0.65, 0.65] | Màn hình quét thông số sinh trắc học: Thước đo laser đo chiều dài chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) từ mũi tới đuôi là 8-10cm và cân điện tử hiện 35g, kèm biểu đồ sức bền vọt lên kịch trần. |
| b06 | 00:32.2–00:36.7 (4.5s) | L07 | Đừng để vẻ ngoài xấu xí ma chê quỷ hờn của gã Dị Nhân Khoai Tây này đánh lừa các bạn! |  | chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) đứng chống nạnh tự hào khoe cơ bắp tí hon, phía sau là bóng đổ hologram khổng lồ của một chiếc máy khoan hầm ngầm công suất lớn. |
| b07 | 00:36.7–00:41.7 (5.0s) | L08 | Dù cơ thể chỉ nhỉnh hơn ngón tay cái người lớn và đôi mắt ti hí gần như mù tịt dưới lòng đất tối đen, |  | So sánh kích thước trực quan: chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) nằm gọn lỏn bên cạnh hình vẽ ngón tay cái hoạt hình khổng lồ, đôi mắt ti hí đeo kính bảo hộ xanh neon. |
| b08 | 00:41.7–00:44.5 (2.8s) | L09 | cơ thể nó lại là một cỗ máy đào hầm siêu hạng. |  | chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) đội thêm chiếc mũ công trường tí hon, hai tay cầm bản thiết kế địa đạo ngầm phức tạp dưới lòng đất Đông Phi. |
| b09 | 00:44.5–00:53.3 (8.8s) | L10 | Hãy nhìn vào hai chiếc răng cửa khổng lồ trắng hếu của nó mà xem: Răng của nó không mọc trong miệng như thú bình thường, mà đâm xuyên thẳng qua lớp môi nhô hẳn ra bên ngoài! |  | Bản vẽ giải phẫu Bio-Lab cắt dọc vùng miệng chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles): Hai chiếc răng cửa trắng bóng khổng lồ mọc xuyên qua lớp môi nhô hẳn ra phía trước như hai lưỡi xẻng. |
| b10 | 00:53.3–00:57.5 (4.2s) | L11 | Thiết kế kỳ quặc này cho phép đôi môi của chuột chũi khép chặt hoàn toàn phía sau răng. |  | Cận cảnh cơ chế khép môi thông minh: Đôi môi của chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) đóng kín mít ngay phía sau răng cửa như cánh cửa chống bụi trong khi răng phía trước đang cạp đất. |
| b11 | 00:57.5–01:04.1 (6.6s) | L12 | Nhờ vậy, khi nó dùng răng đục khoét lớp đất cứng như bê tông khô dưới lòng đất châu Phi, chẳng có hạt đất cát nào có thể lọt vào cổ họng! |  | chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) đang hăng say dùng hai răng cửa đục xuyên qua bức tường đất cứng như bê tông, đất đá văng tứ tung nhưng bên trong khoang miệng vẫn sạch bong. |
| b12 | 01:04.1–01:08.3 (4.3s) | L13 | Đỉnh cao hơn nữa, khối cơ hàm của nó chiếm tới 25% tổng lượng cơ bắp toàn cơ thể, | **25% CƠ BẮP** · dồn vào bộ hàm · R/360 · [0.55, 0.48] | Sơ đồ cơ học bộ hàm: Khối cơ hàm màu cam phát sáng chiếm tới 25% cơ thể chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles), nổi cuồn cuộn trên bản vẽ giải phẫu đầu. |
| b13 | 01:08.3–01:13.2 (4.8s) | L14 | và hai chiếc răng cửa hàm dưới có thể điều khiển tách rời độc lập y hệt như một đôi đũa gắp thức ăn! |  | Cảnh siêu hài hước: chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) điều khiển hai chiếc răng cửa hàm dưới tách mở linh hoạt kẹp gọn một viên sỏi tròn y hệt như đôi đũa gắp thức ăn. |
| b14 | 01:13.2–01:22.8 (9.6s) | L15 | Chưa dừng lại ở đó, dù cơ thể trụi lủi nhưng dọc sườn và đuôi của nó lại mọc lưa thưa khoảng 40 sợi lông xúc giác cực nhạy hoạt động như một dàn radar 360°. | **40 SỢI RÂU** · radar cảm biến 360° · L/360 · [0.5, 0.55] | Sơ đồ cảm biến xúc giác: Dọc hai bên sườn và đuôi của chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) có 40 sợi lông cảm ứng phát ra các vòng sóng radar 360° màu xanh lục bảo trong lòng hang tối. |
| b15 | 01:22.8–01:33.1 (10.3s) | L16 | Nhờ dàn cảm biến này, nó có thể chạy lùi trong đường hầm tối đen với tốc độ nhanh chẳng kém gì khi chạy tiến! Nhưng đó mới chỉ là màn khởi động trước khi bước vào năm bài thử nghiệm cực hạn điên rồ nhất! |  | chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) đang cài số lùi chạy ngược chiều siêu tốc trong đường hầm hẹp, cái đuôi vẫy vẫy dò đường điệu nghệ trước sự kinh ngạc của cô trợ lý mèo hoạt hình đeo kính c |

### scene02 · VÔ CẢM TRƯỚC AXIT ĂN MÒN VÀ CHẤT CAY ỚT HIỂM NHỜ KHÓA KÊNH THẦN KINH · 72.6s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:04.8 (4.8s) | L17 | Bắt đầu bài thử nghiệm khắc nghiệt cấp độ một: Kiểm tra ngưỡng chịu đau hóa học! |  | Buồng thử nghiệm cấp 1 trong phòng lab: Bảng đèn hiệu bật sáng dòng chữ kiểm tra hóa học, xung quanh là các bình thủy tinh đựng dung dịch chanh chua và quả ớt hiểm đỏ chót. KHÔNG có chú Chuột Chũi Trũi trong cảnh này. |
| b02 | 00:04.8–00:11.4 (6.6s) | L18 | Năm 2008, giáo sư Thomas Park tại Đại học Illinois và giáo sư Gary Lewin đã tiến hành một thí nghiệm khiến giới thần kinh học sững sờ. | **NĂM 2008** · phát hiện chấn động · L/350 · [0.45, 0.5] | Sơ đồ nghiên cứu thần kinh học năm 2008: cô trợ lý mèo hoạt hình đeo kính cận tròn, mặc áo blouse trắng phòng thí nghiệm, cầm bảng kẹp hồ sơ sinh học phát sáng cầm ống nhỏ giọt thí nghiệm bên cạnh bảng phân tích xung thần kinh cảm giác trên màn hình phòng lab. KHÔNG có chú Chuột Chũi Trũi trong cảnh này. |
| b03 | 00:11.4–00:19.6 (8.2s) | L19 | Khi nhỏ dung dịch axit nồng độ thấp hoặc bôi hoạt chất capsaicin siêu cay chiết xuất từ ớt hiểm lên da các loài chuột bình thường, chúng lập tức nhảy dựng lên vì bỏng rát dữ dội. |  | Cảnh đối chứng hài hước: chú chuột bạch hoạt hình lông trắng mập mạp đeo nơ xanh, biểu cảm nhát gan hay giật mình thót tim chỉ mới ngửi thấy giọt tinh chất ớt hiểm capsaicin đã nhảy dựng lên trời, mặt đỏ bừng lè lưỡi quạt liên tục. |
| b04 | 00:19.6–00:26.6 (7.0s) | L20 | Ủa các bác sĩ nhỏ nước gì mát thế? Cho xin thêm vài giọt ớt hiểm làm nước chấm củ rễ cây luôn được không ạ? |  | chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) ngồi ung dung trong khay kính, giọt dung dịch thử nghiệm và quả ớt hiểm đặt ngay bên cạnh mà chú vẫn cười tươi rói cầm củ rễ cây chấm ăn ngon lành. |
| b05 | 00:26.6–00:33.4 (6.8s) | L21 | Chẳng hề nhăn mặt, chẳng hề giật mình! Mẫu vật Chuột Chũi Trũi hoàn toàn trơ lì như không hề có chuyện gì xảy ra! |  | Đồng hồ đo phản ứng đau đớn trong phòng lab chỉ con số 0 tròn trĩnh, trong khi chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) nằm phơi bụng ngáp ngủ bình thản trước ống kính quan sát. |
| b06 | 00:33.4–00:38.8 (5.4s) | L22 | Khi mổ xẻ hệ thần kinh dưới kính hiển vi phân tử, các nhà khoa học phát hiện sợi thần kinh cảm giác dưới da của nó |  | Sơ đồ phóng đại sợi thần kinh C-fiber dưới kính hiển vi Bio-Lab: cô trợ lý mèo hoạt hình đeo kính cận tròn, mặc áo blouse trắng phòng thí nghiệm, cầm bảng kẹp hồ sơ sinh học phát sáng soi kính lúp vào sợi dây thần kinh dưới da của chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng th |
| b07 | 00:38.8–00:46.8 (8.0s) | L23 | hoàn toàn thiếu vắng một hợp chất truyền tin mang tên Substance P — vốn là chất phát tín hiệu báo động cảm giác bỏng rát lên não bộ ở mọi loài thú có vú. |  | Bản vẽ so sánh phân tử thần kinh: Sợi thần kinh của chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) trống trơn, không hề có các hạt truyền tin báo động Substance P màu đỏ. KHÔNG có chú Chuột Chũi Trũi tro |
| b08 | 00:46.8–00:55.0 (8.1s) | L24 | Độc đáo hơn nữa, nghiên cứu năm 2011 trên tạp chí Science đã chỉ ra rằng kênh truyền tín hiệu đau NaV1.7 của loài chuột này đã bị đột biến đảo ngược. | **NĂM 2011** · giải mã kênh NaV1.7 · R/350 · [0.55, 0.5] | Bản vẽ phân tử năm 2011 trên tạp chí Science: Cấu trúc cổng kênh ion NaV1.7 trên màng tế bào thần kinh được phóng to như một cánh cổng cơ khí công nghệ cao. KHÔNG có chú Chuột Chũi Trũi trong cảnh này. |
| b09 | 00:55.0–00:59.2 (4.2s) | L25 | Ở con người, khi gặp axit, kênh này mở toang để bắn tín hiệu đau đớn điên cuồng. |  | Sơ đồ so sánh bên trái: Khi các hạt axit màu xanh lá chạm vào cổng thần kinh thông thường, cánh cổng mở toang phát ra tia chớp báo động đỏ rực. KHÔNG có chú Chuột Chũi Trũi trong cảnh này. |
| b10 | 00:59.2–01:04.5 (5.3s) | L26 | Nhưng ở Chuột Chũi Trũi, chính phân tử axit lại biến thành chiếc chìa khóa đóng sập kênh NaV1.7 lại! |  | Sơ đồ so sánh bên phải: Ở chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles), các hạt axit lại biến thành chiếc ổ khóa vàng sập chặt cánh cổng NaV1.7 lại, chặn đứng mọi tia báo động. |
| b11 | 01:04.5–01:07.8 (3.3s) | L27 | Tức là axit đối với nó chẳng khác nào thuốc gây tê miễn phí, |  | chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) đội mũ tắm hoa sen vui vẻ đứng dưới vòi phun sương axit nhẹ trong phòng thí nghiệm như đang được mát-xa gây tê thư giãn. |
| b12 | 01:07.8–01:12.6 (4.8s) | L28 | giúp nó sống khỏe re dưới đáy hang ngầm ngập tràn khí CO2 đậm đặc gây axit hóa mô! |  | Trong lòng hang sâu đầy những đám mây khí CO2 màu tím nhạt: chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) vẫn vui vẻ đào đất và ca hát thoải mái như đang ở trong phòng điều hòa mát rượi. |

### scene03 · HÓA THÀNH THỰC VẬT ĐỐT ĐƯỜNG FRUCTOSE SỐNG 18 PHÚT Ở MỨC 0% OXY · 78.5s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.7 (7.7s) | L29 | Nếu bài kiểm tra hóa chất vẫn chưa đủ làm khó mẫu vật, chúng ta nâng mức độ lên thử nghiệm cấp độ hai: Buồng chân không rút cạn sạch 0% oxy! |  | Buồng chân không thủy tinh cấp độ 2 trong phòng lab: Đồng hồ áp suất khí quyển và van khóa khí khổng lồ phát sáng màu đỏ cảnh báo. KHÔNG có chú Chuột Chũi Trũi trong cảnh này. |
| b02 | 00:07.7–00:13.8 (6.1s) | L30 | Hãy tưởng tượng dưới lòng đất sâu 2m, 300 con chuột chũi chen chúc nhau trong một đường hầm bịt kín bưng chẳng có khe gió. | **SÂU 2M** · hầm kín dưới đất · L/340 · [0.35, 0.5]<br>**300 CÁ THỂ** · chen chúc thiếu khí · R/420 · [0.65, 0.6] | Mặt cắt địa chất dưới độ sâu 2m: 300 con chuột chũi giống chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) đang chen chúc chật kín trong một căn phòng đất chật hẹp không một khe thông gió. |
| b03 | 00:13.8–00:20.2 (6.4s) | L31 | Nồng độ oxy ở đó thấp đến mức bất kỳ người hay con chuột bạch nào bước vào cũng sẽ ngất lịm và tử vong chỉ sau 60 giây. | **60 GIÂY** · giới hạn chuột thường · R/360 · [0.55, 0.5] | chú chuột bạch hoạt hình lông trắng mập mạp đeo nơ xanh, biểu cảm nhát gan hay giật mình thót tim đội mũ bảo hiểm oxy đứng nhìn vào cửa hang tối om với vẻ mặt xanh mét, đồng hồ đo thời gian chịu đựng chỉ vỏn vẹn 60 giây. KHÔNG có chú Chuột Chũi Trũi trong cảnh này. |
| b04 | 00:20.2–00:28.3 (8.1s) | L32 | Cảnh báo đỏ: Nồng độ oxy trong buồng thử nghiệm đã tụt về 0%! Nhịp tim mẫu vật giảm từ 200 nhịp/phút xuống còn 50 nhịp/phút! | **0% OXY** · môi trường chân không · L/330 · [0.3, 0.45]<br>**50 NHỊP/P** · nhịp tim tiết kiệm · R/410 · [0.7, 0.55] | Bảng điện tử buồng thử nghiệm nhấp nháy: Chỉ số O2 tụt thẳng về 0%, màn hình nhịp tim của chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) hạ từ 200 nhịp/phút xuống 50 nhịp/phút để tiết kiệm năng lượng. |
| b05 | 00:28.3–00:36.6 (8.4s) | L33 | 1 phút trôi qua... 5 phút... 10 phút... rồi đúng 18 phút hoàn toàn chẳng có lấy một phân tử oxy nào! Mẫu vật nằm bất động trong trạng thái đình trệ sinh học. | **18 PHÚT** · sống sót ở 0% oxy · R/360 · [0.5, 0.45] | Đồng hồ bấm giờ kỹ thuật số trong phòng lab quay vùn vụt từ 1 phút, 5 phút, 10 phút tới mốc 18 phút đỏ rực, bên trong lồng kính chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) nằm im như đang ngủ say. |
| b06 | 00:36.6–00:44.2 (7.6s) | L34 | Thế nhưng ngay khoảnh khắc van oxy được mở trở lại, gã Dị Nhân Khoai Tây lập tức vươn vai đứng dậy đi lại tỉnh bơ mà không hề bị tổn thương một tế bào não hay cơ tim nào! |  | Khi luồng khí oxy màu xanh da trời vừa được bơm vào lồng kính, chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) lập tức bật dậy vươn vai tập thể dục khỏe re trước đôi mắt tròn xoe kinh ngạc của cô trợ lý m |
| b07 | 00:44.2–00:49.2 (5.0s) | L35 | Bí mật nằm ở công trình chấn động công bố trên tạp chí Science năm 2017. | **NĂM 2017** · giải mã trên Science · L/360 · [0.45, 0.5] | Trang bìa tạp chí khoa học Science năm 2017 đặt trên bàn thí nghiệm với biểu đồ phân tích quá trình chuyển hóa năng lượng thần kỳ của não bộ chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles). |
| b08 | 00:49.2–00:55.4 (6.2s) | L36 | Khi thiếu oxy, mọi loài động vật có vú đều bị tắc nghẽn dây chuyền đốt đường Glucose làm tế bào não chết ngạt. |  | Sơ đồ nhà máy tế bào thông thường: Dây chuyền đốt đường Glucose bị khóa đứng với biển báo 'HẾT OXY - NGỪNG HOẠT ĐỘNG', đèn điện tắt phụt. KHÔNG có chú Chuột Chũi Trũi trong cảnh này. |
| b09 | 00:55.4–01:03.2 (7.8s) | L37 | Nhưng Chuột Chũi Trũi đã thực hiện một cú chuyển đổi sinh học không tưởng: Nó bật công tắc chuyển sang đốt đường Fructose — tức là loại đường trái cây |  | Sơ đồ nhà máy tế bào của chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles): Chú gạt cần công tắc dự phòng màu xanh lá cây, mở cổng bơm phân tử đưa các viên đường trái cây Fructose phát sáng vào lò năng lượn |
| b10 | 01:03.2–01:07.0 (3.9s) | L38 | — thông qua các bơm phân tử chuyên biệt để nuôi sống não bộ mà không cần oxy! |  | Bản vẽ giải phẫu não và tim của chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles): Các đường ống dẫn đường Fructose phát sáng màu vàng cam cung cấp năng lượng liên tục giữ cho não và tim sáng rực. |
| b11 | 01:07.0–01:10.1 (3.1s) | L39 | Đây vốn là cơ chế trao đổi chất độc quyền của giới thực vật! |  | Bản vẽ so sánh Bio-Lab: Một bên là chậu cây xanh và củ khoai tây, bên kia là chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) với chiếc mầm lá xanh ngộ nghĩnh mọc trên mũ bảo hộ, cả hai cùng phát sáng năng |
| b12 | 01:10.1–01:18.5 (8.3s) | L40 | Nói cách khác, khi hết sạch không khí, nó tạm thời biến thành một củ khoai tây thực thụ để chờ thời, rồi lại hoàn hồn làm động vật khi có gió về! |  | Cảnh bi hài hai trạng thái: Khi hết gió chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) hóa trang thành củ khoai tây nằm im thin thít, vừa có làn gió mát thổi qua đã bật dậy nhảy điệu disco sôi động. |

### scene04 · SIÊU KEO HYALURONIC ACID HMW-HA VÀ KHÓA KÉP CHỐNG UNG THƯ TUYỆT ĐỐI · 85.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:03.0 (3.0s) | L41 | Chuyển sang thử nghiệm cấp độ ba: Khả năng kháng bệnh |  | Phòng thí nghiệm y sinh học cấp độ 3: Màn hình lớn hiển thị biểu đồ lá chắn bảo vệ tế bào màu xanh lục bảo lấp lánh. KHÔNG có chú Chuột Chũi Trũi trong cảnh này. |
| b02 | 00:03.0–00:09.0 (5.9s) | L42 | nan y! Thông thường, tới hơn 70% các loài chuột trong phòng thí nghiệm sẽ tử vong vì các khối u ung thư khi về già. | **70%** · tỷ lệ u ở chuột thường · L/360 · [0.35, 0.5] | Biểu đồ thống kê y khoa trong phòng lab: Cột tỷ lệ mắc khối u ở loài chuột thường cao vọt lên mức 70% khiến chú chuột bạch hoạt hình lông trắng mập mạp đeo nơ xanh, biểu cảm nhát gan hay giật mình thót tim nhìn biểu đồ lo lắng. KHÔNG có chú Chuột Chũi Trũi trong cảnh này. |
| b03 | 00:09.0–00:16.6 (7.6s) | L43 | Thế nhưng khi giáo sư Vera Gorbunova và cộng sự tại Đại học Rochester theo dõi hàng ngàn cá thể Chuột Chũi Trũi suốt hàng chục năm trời, |  | Bảng theo dõi hàng ngàn hồ sơ sức khỏe của chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) tại Đại học Rochester: Tất cả các ô kiểm tra đều đóng dấu tích xanh hoàn hảo 'KHỎE MẠNH 100%'. |
| b04 | 00:16.6–00:22.3 (5.7s) | L44 | họ phát hiện một con số gây chấn động y học thế giới: Hầu như không có bất kỳ cá thể nào mắc bệnh ung thư! |  | chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) đeo huy chương vàng 'ZERO UNG THƯ' đứng hiên ngang trên bục kính hiển vi trước sự thán phục của cô trợ lý mèo hoạt hình đeo kính cận tròn, mặc áo blouse trắ |
| b05 | 00:22.3–00:30.2 (7.9s) | L45 | Khi kiểm tra dịch nuôi cấy tế bào của chúng vào năm 2013, các nhà nghiên cứu thấy dung dịch cứ đặc quánh và nhớt nhầy như hồ dán làm tắc nghẽn cả ống hút phòng lab! | **NĂM 2013** · phát hiện siêu keo · R/350 · [0.55, 0.5] | Cảnh phòng lab năm 2013 vui nhộn: cô trợ lý mèo hoạt hình đeo kính cận tròn, mặc áo blouse trắng phòng thí nghiệm, cầm bảng kẹp hồ sơ sinh học phát sáng đang cố bóp ống hút thủy tinh nhưng dung dịch nuôi cấy tế bào của chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu |
| b06 | 00:30.2–00:35.9 (5.6s) | L46 | Thủ phạm chính là hợp chất đường siêu phân tử Hyaluronic Acid khối lượng cực cao, viết tắt là HMW-HA. |  | Sơ đồ cấu trúc hóa học phát sáng: Các chuỗi phân tử đường Hyaluronic Acid (HMW-HA) xoắn lại như những sợi dây thừng vàng khổng lồ bao quanh tế bào của chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles). |
| b07 | 00:35.9–00:44.5 (8.7s) | L47 | Ở con người, hợp chất này vốn được dùng làm chất giữ ẩm trong mỹ phẩm dưỡng da, nhưng ở Chuột Chũi Trũi, chuỗi phân tử của nó dài và nặng gấp 5 lần so với của người! | **GẤP 5 LẦN** · siêu keo HMW-HA · R/360 · [0.65, 0.5] | Phép so sánh kích thước phân tử trực quan: Một bên là lọ kem dưỡng ẩm nhỏ xíu với sợi phân tử ngắn ngủn của người, bên kia là chuỗi siêu phân tử HMW-HA của chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles)  |
| b08 | 00:44.5–00:51.5 (7.0s) | L48 | Lớp siêu keo HMW-HA này tạo thành một mạng lưới lồng sắt đàn hồi cực kỳ dày đặc bao bọc quanh từng tế bào của Dị Nhân Khoai Tây. |  | Mặt cắt kính hiển vi: Các tế bào khỏe mạnh được bao bọc bởi một hàng rào lưới gel đàn hồi màu xanh ngọc cực kỳ vững chắc như pháo đài. |
| b09 | 00:51.5–01:00.6 (9.1s) | L49 | Nhờ lớp đệm siêu đàn hồi đó mà làn da của nó mới nhăn nheo và co giãn rộng thùng thình, giúp nó luồn lách và quay đầu 180° ngay trong lòng đường hầm chật hẹp mà không bị rách da! | **QUAY 180°** · nhờ lớp da siêu giãn · L/360 · [0.5, 0.55] | chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) đang biểu diễn màn nhào lộn quay đầu 180° ngay bên trong một chiếc ống nhựa hẹp, lớp da rộng thùng thình co giãn dẻo dai như cao su. |
| b10 | 01:00.6–01:08.5 (7.9s) | L50 | Quan trọng hơn cả, mạng lưới siêu keo này kích hoạt cơ chế ức chế tiếp xúc sớm thông qua bộ khóa bảo vệ kép gồm hai gen p16 và p27. |  | Bản vẽ cơ chế phòng thủ tế bào: Cánh cửa nhân đôi tế bào được gắn tới 2 chiếc ổ khóa kim loại kiên cố khắc nhãn 'p16' và 'p27'. KHÔNG có chú Chuột Chũi Trũi trong cảnh này. |
| b11 | 01:08.5–01:15.0 (6.5s) | L51 | Ở cơ thể người, chúng ta chỉ có một ổ khóa p27, nên khi tế bào đột biến nhân lên chật chội, khối u vẫn có thể phá khóa phát triển. |  | Sơ đồ đối chiếu: Cánh cửa chỉ có 1 ổ khóa p27 đơn lẻ đang bị nhân vật quái vật tế bào đột biến hoạt hình màu tím tròn xoe ngộ nghĩnh đội mũ sừng nhỏ, mặt mếu máo bất lực lén dùng xà beng cậy ra để chen lấn nhân bản. KHÔNG có chú Chuột Chũi Trũi trong cảnh này. |
| b12 | 01:15.0–01:21.3 (6.2s) | L52 | Còn ở Chuột Chũi Trũi, ngay khi vài tế bào bất thường vừa chạm nhẹ vào nhau, ổ khóa thứ hai p16 lập tức sập xuống, |  | Ngay khi nhân vật quái vật tế bào đột biến hoạt hình màu tím tròn xoe ngộ nghĩnh đội mũ sừng nhỏ, mặt mếu máo bất lực vừa chạm nhẹ vào hàng rào siêu keo HMW-HA, chiếc khóa thép khổng lồ p16 lập tức sập xuống. |
| b13 | 01:21.3–01:25.9 (4.6s) | L53 | ra lệnh đóng băng toàn bộ quá trình phân chia, bóp nghẹt mầm mống ung thư ngay từ trong trứng nước! |  | nhân vật quái vật tế bào đột biến hoạt hình màu tím tròn xoe ngộ nghĩnh đội mũ sừng nhỏ, mặt mếu máo bất lực bị giam chặt cứng trong lồng kính siêu keo HMW-HA đứng hình mếu máo, bên cạnh chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon |

### scene05 · ĐẾ CHẾ NỮ HOÀNG ĐỘC TÀI, NHÀ VỆ SINH CHUNG VÀ TỬ HUYỆT MÁU LẠNH · 99.3s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:03.6 (3.6s) | L54 | Bước vào thử nghiệm cấp độ bốn: Quan sát hành vi xã hội! |  | Sơ đồ mặt cắt địa chất khổng lồ cấp độ 4: Một mê cung thành phố ngầm chằng chịt dưới lòng đất được quan sát qua màn hình radar địa chấn. KHÔNG có chú Chuột Chũi Trũi trong cảnh này. |
| b02 | 00:03.6–00:14.2 (10.6s) | L55 | Năm 1981, nhà sinh vật học Jennifer Jarvis đã phát hiện Chuột Chũi Trũi là loài thú có vú hiếm hoi trên Trái Đất sống theo mô hình xã hội côn trùng chân chính y hệt loài kiến và mối! | **NĂM 1981** · xã hội côn trùng · L/350 · [0.45, 0.5] | Bản vẽ so sánh sinh thái học năm 1981: Một bên là tổ kiến và tổ mối, bên kia là đàn của chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) với cấu trúc phân tầng xã hội giống hệt nhau. |
| b03 | 00:14.2–00:22.8 (8.6s) | L56 | Một vương quốc ngầm dài từ 3-5km chứa tới 300 cá thể, nhưng chỉ có duy nhất một Nữ Hoàng tối cao được phép sinh con đẻ cái cùng ba gã hoàng phu! | **DÀI 3-5KM** · mạng lưới địa đạo · L/340 · [0.35, 0.5]<br>**300 CON** · 1 Nữ Hoàng duy nhất · R/410 · [0.65, 0.55] | Bản đồ toàn cảnh vương quốc ngầm trải dài 3-5km dưới lòng đất chứa 300 cá thể, ở trung tâm là cung điện hoàng gia nơi Nữ Hoàng Chuột Chũi hoạt hình to gấp đôi, đội vương miện vàng lấp lánh, mặc áo choàng nhung đỏ oai vệ chống nạnh hét ra lửa ngự trị trên ngai vàng rễ cây. |
| b04 | 00:22.8–00:31.6 (8.8s) | L57 | Tất cả nghe lệnh ta! Đội công nhân xếp hàng đào đất! Đội chiến binh ra chặn cửa hang! Đứa nào dám yêu đương lén lút ta húc cho văng vào vách đá! |  | Nữ Hoàng Chuột Chũi hoạt hình to gấp đôi, đội vương miện vàng lấp lánh, mặc áo choàng nhung đỏ oai vệ chống nạnh hét ra lửa đội vương miện vàng đứng trên bục đất cao cầm loa phóng thanh hét lớn, phía dưới là đội công nhân đội mũ bảo hộ vàng và đội chiến binh cầm khiên rễ cây xếp hàng răm rắp. |
| b05 | 00:31.6–00:40.0 (8.5s) | L58 | Nữ Hoàng cai trị bằng nắm đấm sắt đúng nghĩa đen! Mỗi lần mang thai, các đốt xương sống của Nữ Hoàng tự động kéo dài ra như lò xo để chứa tới gần 30 đứa con trong bụng. | **~30 CON** · cột sống tự kéo dài · R/360 · [0.55, 0.5] | Sơ đồ X-quang giải phẫu Nữ Hoàng Chuột Chũi hoạt hình to gấp đôi, đội vương miện vàng lấp lánh, mặc áo choàng nhung đỏ oai vệ chống nạnh hét ra lửa: Các đốt xương sống của Nữ Hoàng tự động giãn dài ra như lò xo để chứa ổ bụng khổng lồ mang tới gần 30 đứa con. KHÔNG có chú Chuột Chũi Trũi trong cảnh này. |
| b06 | 00:40.0–00:46.5 (6.4s) | L59 | Trong khi đó, hàng trăm thần dân còn lại bị Nữ Hoàng dùng áp lực cơ học húc đẩy liên tục khiến hormone sinh sản bị khóa chặt suốt đời! |  | Nữ Hoàng Chuột Chũi hoạt hình to gấp đôi, đội vương miện vàng lấp lánh, mặc áo choàng nhung đỏ oai vệ chống nạnh hét ra lửa đi tuần tra trong đường hầm, dùng cái mũi húc nhẹ thị uy khiến các chú chuột công nhân xung quanh lập tức cúi rạp người chăm chỉ làm việc. KHÔNG có chú Chuột Chũi Trũi trong cảnh này. |
| b07 | 00:46.5–00:54.5 (8.0s) | L60 | Đội công nhân phải xếp thành một dây chuyền băng tải sống: con đầu tiên dùng răng khoét đất, hàng chục con phía sau cứ thế đá đất qua háng nhau chạy tít ra cửa hang! |  | Dây chuyền băng tải đào hầm siêu hài hước: chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) ở đầu hàng dùng răng khoét đất, 5 chú chuột phía sau xếp hàng dọc đồng loạt đá đất qua háng nhau bay vèo ra cửa h |
| b08 | 00:54.5–01:05.2 (10.7s) | L61 | Và chi tiết lầy lội nhất của đế chế này chính là quy định nhận diện công dân: Vì dưới hang tối đen như mực không nhìn thấy mặt nhau, cả 300 con chuột trong đàn đều phải lăn lộn vào chung một buồng nhà vệ sinh duy nhất! |  | Căn phòng nhà vệ sinh chung của vương quốc ngầm: Biển hiệu 'PHÒNG NƯỚC HOA GIA TỘC' treo trên vách đất, các chú chuột xếp hàng xịt mùi hương đồng bộ để nhận diện đồng hương. |
| b09 | 01:05.2–01:12.5 (7.3s) | L62 | Nhờ tắm chung mùi chất thải đặc trưng của gia tộc, chúng nhận ra đồng đội ngay lập tức, kẻ lạ nào khác mùi mò vào sẽ bị đội chiến binh tóm cổ ngay! |  | Hai chú chuột chiến binh gác cổng đeo kính râm đang dùng máy quét mùi hương kiểm tra chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles), đèn xanh bật sáng cho phép qua cổng an toàn. |
| b10 | 01:12.5–01:23.2 (10.7s) | L63 | Thế nhưng vị hoàng đế ngầm này lại mang một tử huyệt chí mạng: Chúng đã đánh mất hoàn toàn lớp mỡ nâu và khả năng tự điều chỉnh thân nhiệt của loài thú có vú, trở thành sinh vật biến nhiệt chẳng khác nào loài bò sát máu lạnh! |  | Sơ đồ nhiệt kế sinh học Bio-Lab: Cơ thể chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) không có lớp mỡ nâu giữ nhiệt, vạch nhiệt độ biến đổi y hệt một chú thằn lằn nước màu lạnh bên cạnh. |
| b11 | 01:23.2–01:26.0 (2.8s) | L64 | Ở trong hang sâu nhiệt độ luôn ổn định quanh mức 30°C, | **30°C ẤM ÁP** · nhiệt độ trong hang · L/350 · [0.45, 0.5] | Nhiệt kế trong đường hầm đất sâu chỉ đúng 30°C ấm áp, chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) đang ngồi uống trà thư giãn dễ chịu. |
| b12 | 01:26.0–01:34.3 (8.4s) | L65 | nhưng nếu bị lôi ra ngoài trời lạnh dưới 15°C hoặc nắng nóng trên 35°C, siêu dị nhân chống axit và ung thư của chúng ta sẽ lập tức đơ cứng vì sốc nhiệt! | **< 15°C** · lạnh cóng đơ người · L/350 · [0.3, 0.55]<br>**> 35°C** · sốc nhiệt ngay lập tức · R/410 · [0.7, 0.55] | Cảnh đối lập nhiệt độ hài hước: Dưới mức 15°C chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) quấn chăn run cầm cập đóng băng, còn trên mức 35°C thì lè lưỡi quạt phành phạch vì sốc nhiệt. |
| b13 | 01:34.3–01:39.3 (4.9s) | L66 | Để giữ ấm, cả đàn chỉ còn cách rúc vào nhau nằm chồng chất thành một đống khoai tây khổng lồ! |  | Trong hang đất ấm áp: Hàng chục chú chuột chũi cùng chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) ôm chặt lấy nhau chồng chất thành một ngọn núi khoai tây hồng khổng lồ tỏa ra những trái tim ấm áp. |

### scene06 · TUỔI THỌ 37 NĂM PHÁ VỠ ĐỊNH LUẬT LÃO HÓA GOMPERTZ VÀ HÉ LỘ TẬP 33 · 93.1s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.0 (7.0s) | L67 | Cuối cùng, bài thử nghiệm cấp độ năm cũng là đỉnh cao vĩ đại nhất của Dị Nhân Khoai Tây mang mã số 32: Thử thách thời gian! |  | Phòng thí nghiệm thời gian cấp độ 5: Chiếc đồng hồ cát vàng khổng lồ và biểu đồ trường thọ phát sáng rực rỡ trên màn hình chính. KHÔNG có chú Chuột Chũi Trũi trong cảnh này. |
| b02 | 00:07.0–00:11.9 (4.9s) | L68 | Một con chuột nhắt có cùng kích thước chỉ sống được tối đa từ 2-3 năm là già yếu qua đời. | **2-3 NĂM** · tuổi thọ chuột thường · L/350 · [0.4, 0.55] | Bên trái sơ đồ thời gian: chú chuột bạch hoạt hình lông trắng mập mạp đeo nơ xanh, biểu cảm nhát gan hay giật mình thót tim chống gậy râu bạc trắng sau 2-3 năm tuổi, bên cạnh là cuốn lịch bàn đã hết trang. KHÔNG có chú Chuột Chũi Trũi trong cảnh này. |
| b03 | 00:11.9–00:18.1 (6.2s) | L69 | Thế nhưng Chuột Chũi Trũi có thể sống khỏe mạnh tới 37 năm — tức là gấp hơn 12 lần tuổi thọ dự kiến! | **37 NĂM!** · kỷ lục Chuột Chũi · R/340 · [0.6, 0.5]<br>**X12 TUỔI** · tuổi thọ họ gặm nhấm · L/410 · [0.35, 0.55] | Bên phải sơ đồ thời gian: chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) đeo dải băng kỷ niệm 37 năm (gấp 12 lần) vẫn đang nhảy hip-hop sung sức trên bàn thí nghiệm! |
| b04 | 00:18.1–00:23.4 (5.3s) | L70 | Nếu quy đổi sang thước đo của con người, nó tương đương với một cụ già sống thọ tới hơn 800 tuổi! | **~800 TUỔI** · quy đổi sang người · R/360 · [0.6, 0.5] | chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) mặc bộ đồ tiên ông trường thọ cưỡi hạc giấy, tay cầm quả đào tiên bên cạnh tấm biển kỷ lục quy đổi tương đương 800 tuổi ở con người. |
| b05 | 00:23.4–00:33.0 (9.6s) | L71 | Năm 2018, nhà sinh học Rochelle Buffenstein đã công bố dữ liệu theo dõi hơn 3.000 cá thể suốt ba thập kỷ và chứng minh Chuột Chũi Trũi đã đập tan định luật lão hóa Gompertz. | **3.000 CON** · kiểm chứng 30 năm · L/360 · [0.45, 0.5] | Đồ thị toán học năm 2018 trên màn hình Bio-Lab: Nhà nghiên cứu chỉ vào dữ liệu theo dõi hơn 3.000 cá thể chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) suốt ba thập kỷ. |
| b06 | 00:33.0–00:37.1 (4.1s) | L72 | Ở mọi sinh vật khác, càng lớn tuổi thì nguy cơ tử vong càng tăng theo cấp số nhân. |  | Biểu đồ so sánh Định luật lão hóa Gompertz: Đường màu đỏ của thú thông thường dốc dựng đứng lên cao, còn đường màu xanh lục của chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) chạy ngang phẳng lì! |
| b07 | 00:37.1–00:44.5 (7.4s) | L73 | Nhưng ở loài chuột này, một cụ chuột 30 tuổi vẫn có trái tim khỏe mạnh, mật độ xương rắn chắc và tế bào tự dọn rác hoàn hảo y hệt một thanh niên 2 | **30 TUỔI** · trẻ khỏe như 2 tuổi · R/360 · [0.55, 0.5] | chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) ở tuổi 30 tuổi đang nâng tạ đôi trong phòng lab, chỉ số tim mạch, xương khớp và bộ máy dọn rác tế bào đều trẻ khỏe như 2 tuổi. |
| b08 | 00:44.5–00:50.6 (6.1s) | L74 | tuổi! Nó chính là chìa khóa vàng giúp y học nhân loại giải mã giấc mơ trường thọ và chiến thắng bệnh ung thư trong tương lai. |  | chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) đứng trên bục vinh danh khoa học, trao chiếc chìa khóa vàng khắc hình chuỗi DNA trường thọ cho cô trợ lý mèo hoạt hình đeo kính cận tròn, mặc áo blouse trắn |
| b09 | 00:50.6–00:57.2 (6.6s) | L75 | Hội đồng khoa học thân mến, sau năm cấp độ thử nghiệm điên rồ vừa rồi, bạn thấy siêu năng lực nào của Chuột Chũi Trũi đỉnh chóp nhất: |  | Hội đồng giám khảo trong phòng thí nghiệm nhìn lên màn hình tổng kết 5 bài kiểm tra sinh tồn của chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles). |
| b10 | 00:57.2–01:06.4 (9.2s) | L80 | Vô cảm trước axit nhờ khóa kênh thần kinh, hóa thành thực vật sống 18 phút không cần oxy, hay lớp siêu keo HMW-HA bóp nghẹt mọi khối u ung thư? |  | Bảng tổng kết 3 siêu năng lực đỉnh chóp của chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles): (1) Khiên chống axit NaV1.7, (2) Lá cây Fructose sống 18 phút 0% oxy, (3) Lồng sắt siêu keo HMW-HA khóa ung thư |
| b11 | 01:06.4–01:09.8 (3.4s) | L76 | Hãy ghi ngay đánh giá của bạn xuống phần bình luận bên dưới nhé! |  | chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) và cô trợ lý mèo hoạt hình đeo kính cận tròn, mặc áo blouse trắng phòng thí nghiệm, cầm bảng kẹp hồ sơ sinh học phát sáng vẫy tay chào khán giả bên cạnh hòm |
| b12 | 01:09.8–01:16.5 (6.7s) | L77 | Và ngay trong hồ sơ Tập 33 tiếp theo, chúng ta sẽ rời căn hầm nóng bức Đông Phi để bay tới vùng băng giá Bắc Cực lạnh -20°C! | **-20°C** · băng giá Bắc Cực · L/350 · [0.45, 0.55] | Khung cảnh chuyển sang vùng rừng tuyết Bắc Cực lạnh -20°C: Bão tuyết trắng xóa bao phủ những gốc cây thông đóng băng. KHÔNG có chú Chuột Chũi Trũi trong cảnh này. |
| b13 | 01:16.5–01:22.7 (6.3s) | L78 | Tại đó có một quái kiệt lưỡng cư tự biến hai phần ba lượng nước trong cơ thể thành một cục nước đá cứng ngắc suốt 8 tháng mùa đông: | **8 THÁNG** · đóng băng thành đá · R/360 · [0.55, 0.5] | Một bóng đen chú ếch nhỏ nằm bất động bên trong khối băng tinh thể trong suốt lấp lánh suốt 8 tháng mùa đông dưới ánh cực quang. KHÔNG có chú Chuột Chũi Trũi trong cảnh này. |
| b14 | 01:22.7–01:33.1 (10.4s) | L79 | Tim ngừng đập hoàn toàn, máu ngừng chảy, não bộ tắt nguồn như đã chết, nhưng ngay khi nắng xuân vừa chạm tới lại tự rã đông nhảy nhót tỉnh bơ! Đố bạn đoán được sinh vật đóng băng bất tử tiếp theo này là ai? |  | Khối băng bọc quanh bóng đen chú ếch bí ẩn nứt ra khi tia nắng mùa xuân chiếu rọi, đôi mắt chú ếch bất ngờ mở bừng sáng lấp lánh kèm dấu chấm hỏi lớn. KHÔNG có chú Chuột Chũi Trũi trong cảnh này. |

## 5. Phân cảnh Shorts — từng beat

Banner: **CHUỘT XẤU XÍ NHẤT: / MIỄN NHIỄM 100% UNG THƯ?!** · giọng 49.0s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Cảnh báo sinh học cấp độ năm! |  |
| s02 | 00:02.4 | S02 | Tại sao loài chuột xấu xí nhăn nheo như củ khoai tây luộc này |  |
| s03 | 00:05.4 | S11 | lại miễn nhiễm hoàn toàn với bệnh ung thư và sống sót 18 phút không cần một giọt oxy nào? |  |
| s04 | 00:10.5 | S03 | Đây là Chuột Chũi Trũi Đông Phi, siêu dị nhân bất tử dưới lòng đất! |  |
| s05 | 00:14.3 | S04 | Khi các nhà khoa học theo dõi hàng ngàn cá thể suốt 37 năm, họ sững sờ khi thấy chúng gần như không bao giờ mắc ung thư. | **37 NĂM** · không mắc ung thư · R/820 · [0.55, 0.5] |
| s06 | 00:20.9 | S05 | Bí mật nằm ở chỗ tế bào của chúng tiết ra một chất siêu keo tên là Hyaluronic Acid có phân tử nặng gấp 5 lần con | **GẤP 5 LẦN** · siêu keo phân tử · L/820 · [0.45, 0.55] |
| s07 | 00:27.2 | S06 | người! Lớp siêu keo này kết hợp cùng bộ khóa gen kép p16 và p27, |  |
| s08 | 00:31.5 | S07 | tạo thành chiếc lồng sắt khóa chặt và bóp nghẹt mọi tế bào khối u ngay từ khi mới chớm! |  |
| s09 | 00:36.7 | S08 | Chưa hết, khi bị nhốt trong hầm kín 0% oxy suốt 18 phút, | **0% OXY** · buồng kín khí · L/780 · [0.35, 0.5]<br>**18 PHÚT** · vẫn sống khỏe · R/880 · [0.65, 0.55] |
| s10 | 00:40.5 | S09 | nó lập tức biến hình thành thực vật, đốt đường trái cây Fructose để nuôi não bộ mà chẳng cần hít thở! |  |
| s11 | 00:45.9 | S10 | Một kiệt tác y sinh học giúp nó sống thọ tới 37 năm! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cảnh báo sinh học cấp độ năm! Chào mừng toàn thể hội đồng khoa học đã bước xuống phòng thí nghiệm ngầm tối mật của chúng tôi.". Bố cục: Bàn điều khiển phòng thí nghiệm sinh học: cô trợ lý mèo hoạt hình đeo kính cận tròn, mặc áo blouse trắng phòng thí nghiệm, cầm bảng kẹp hồ sơ sinh học phát sáng đang thuyết trình trước màn hình hologram chiếu sơ đồ giải phẫu bí ẩn, xung quanh là các bình thủy tinh sủi bọt xanh ngọc. KHÔNG có chú Chuột Chũi Trũi trong cảnh này.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hôm nay, nằm trong lồng kính cường lực trước mặt quý vị không phải là một quái thú săn mồi hào nhoáng, mà là mẫu vật kỳ dị bậc nhất lịch sử tiến hóa:". Bố cục: Chiếc bệ kính cường lực phát sáng trong phòng lab: chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) đang nằm vắt chân chữ ngũ thư giãn, vừa gặm củ rễ cây vừa nháy mắt tinh nghịch dưới ánh đèn quét laser xanh.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chuột Chũi Trũi Đông Phi, danh pháp khoa học Heterocephalus glaber.". Bố cục: Sơ đồ hồ sơ định danh Bio-Lab: Chân dung cận cảnh chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) nằm giữa khung lưới tọa độ giải phẫu màu tím, bên cạnh là bản đồ vùng sừng Đông Phi khô cằn.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhìn thoáng qua, chắc chắn ai cũng tưởng ai đó vừa đánh rơi một củ khoai tây luộc bị héo hoặc một cây xúc xích hồng nhăn nheo biết chạy!". Bố cục: Phép so sánh hài hước trên đĩa cân phòng lab: Một bên là củ khoai tây luộc nhăn nheo và cây xúc xích hồng, bên kia là chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) đang tạo dáng y hệt khiến cô trợ lý mèo hoạt hình đeo kính cận tròn, mặc áo blouse trắng phòng thí nghiệm, cầm bảng kẹp hồ sơ sinh học phát sáng nhìn qua kính lúp bối rối.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trợ lý phòng lab báo cáo: Mẫu vật dài 8-10cm, nặng 35g, trụi lông hoàn toàn nhưng chỉ số sinh tồn vượt mọi giới hạn sinh học!". Bố cục: Màn hình quét thông số sinh trắc học: Thước đo laser đo chiều dài chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) từ mũi tới đuôi là 8-10cm và cân điện tử hiện 35g, kèm biểu đồ sức bền vọt lên kịch trần.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đừng để vẻ ngoài xấu xí ma chê quỷ hờn của gã Dị Nhân Khoai Tây này đánh lừa các bạn!". Bố cục: chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) đứng chống nạnh tự hào khoe cơ bắp tí hon, phía sau là bóng đổ hologram khổng lồ của một chiếc máy khoan hầm ngầm công suất lớn.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Dù cơ thể chỉ nhỉnh hơn ngón tay cái người lớn và đôi mắt ti hí gần như mù tịt dưới lòng đất tối đen,". Bố cục: So sánh kích thước trực quan: chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) nằm gọn lỏn bên cạnh hình vẽ ngón tay cái hoạt hình khổng lồ, đôi mắt ti hí đeo kính bảo hộ xanh neon.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "cơ thể nó lại là một cỗ máy đào hầm siêu hạng.". Bố cục: chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) đội thêm chiếc mũ công trường tí hon, hai tay cầm bản thiết kế địa đạo ngầm phức tạp dưới lòng đất Đông Phi.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy nhìn vào hai chiếc răng cửa khổng lồ trắng hếu của nó mà xem: Răng của nó không mọc trong miệng như thú bình thường, mà đâm xuyên thẳng qua lớp môi nhô hẳn ra bên ngoài!". Bố cục: Bản vẽ giải phẫu Bio-Lab cắt dọc vùng miệng chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles): Hai chiếc răng cửa trắng bóng khổng lồ mọc xuyên qua lớp môi nhô hẳn ra phía trước như hai lưỡi xẻng.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thiết kế kỳ quặc này cho phép đôi môi của chuột chũi khép chặt hoàn toàn phía sau răng.". Bố cục: Cận cảnh cơ chế khép môi thông minh: Đôi môi của chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) đóng kín mít ngay phía sau răng cửa như cánh cửa chống bụi trong khi răng phía trước đang cạp đất.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhờ vậy, khi nó dùng răng đục khoét lớp đất cứng như bê tông khô dưới lòng đất châu Phi, chẳng có hạt đất cát nào có thể lọt vào cổ họng!". Bố cục: chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) đang hăng say dùng hai răng cửa đục xuyên qua bức tường đất cứng như bê tông, đất đá văng tứ tung nhưng bên trong khoang miệng vẫn sạch bong.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đỉnh cao hơn nữa, khối cơ hàm của nó chiếm tới 25% tổng lượng cơ bắp toàn cơ thể,". Bố cục: Sơ đồ cơ học bộ hàm: Khối cơ hàm màu cam phát sáng chiếm tới 25% cơ thể chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles), nổi cuồn cuộn trên bản vẽ giải phẫu đầu.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "và hai chiếc răng cửa hàm dưới có thể điều khiển tách rời độc lập y hệt như một đôi đũa gắp thức ăn!". Bố cục: Cảnh siêu hài hước: chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) điều khiển hai chiếc răng cửa hàm dưới tách mở linh hoạt kẹp gọn một viên sỏi tròn y hệt như đôi đũa gắp thức ăn.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa dừng lại ở đó, dù cơ thể trụi lủi nhưng dọc sườn và đuôi của nó lại mọc lưa thưa khoảng 40 sợi lông xúc giác cực nhạy hoạt động như một dàn radar 360°.". Bố cục: Sơ đồ cảm biến xúc giác: Dọc hai bên sườn và đuôi của chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) có 40 sợi lông cảm ứng phát ra các vòng sóng radar 360° màu xanh lục bảo trong lòng hang tối.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhờ dàn cảm biến này, nó có thể chạy lùi trong đường hầm tối đen với tốc độ nhanh chẳng kém gì khi chạy tiến! Nhưng đó mới chỉ là màn khởi động trước khi bước vào năm bài thử nghiệm cực hạn điên rồ nhất!". Bố cục: chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) đang cài số lùi chạy ngược chiều siêu tốc trong đường hầm hẹp, cái đuôi vẫy vẫy dò đường điệu nghệ trước sự kinh ngạc của cô trợ lý mèo hoạt hình đeo kính cận tròn, mặc áo blouse trắng phòng thí nghiệm, cầm bảng kẹp hồ sơ sinh học phát sáng.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bắt đầu bài thử nghiệm khắc nghiệt cấp độ một: Kiểm tra ngưỡng chịu đau hóa học!". Bố cục: Buồng thử nghiệm cấp 1 trong phòng lab: Bảng đèn hiệu bật sáng dòng chữ kiểm tra hóa học, xung quanh là các bình thủy tinh đựng dung dịch chanh chua và quả ớt hiểm đỏ chót. KHÔNG có chú Chuột Chũi Trũi trong cảnh này.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Năm 2008, giáo sư Thomas Park tại Đại học Illinois và giáo sư Gary Lewin đã tiến hành một thí nghiệm khiến giới thần kinh học sững sờ.". Bố cục: Sơ đồ nghiên cứu thần kinh học năm 2008: cô trợ lý mèo hoạt hình đeo kính cận tròn, mặc áo blouse trắng phòng thí nghiệm, cầm bảng kẹp hồ sơ sinh học phát sáng cầm ống nhỏ giọt thí nghiệm bên cạnh bảng phân tích xung thần kinh cảm giác trên màn hình phòng lab. KHÔNG có chú Chuột Chũi Trũi trong cảnh này.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi nhỏ dung dịch axit nồng độ thấp hoặc bôi hoạt chất capsaicin siêu cay chiết xuất từ ớt hiểm lên da các loài chuột bình thường, chúng lập tức nhảy dựng lên vì bỏng rát dữ dội.". Bố cục: Cảnh đối chứng hài hước: chú chuột bạch hoạt hình lông trắng mập mạp đeo nơ xanh, biểu cảm nhát gan hay giật mình thót tim chỉ mới ngửi thấy giọt tinh chất ớt hiểm capsaicin đã nhảy dựng lên trời, mặt đỏ bừng lè lưỡi quạt liên tục.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ủa các bác sĩ nhỏ nước gì mát thế? Cho xin thêm vài giọt ớt hiểm làm nước chấm củ rễ cây luôn được không ạ?". Bố cục: chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) ngồi ung dung trong khay kính, giọt dung dịch thử nghiệm và quả ớt hiểm đặt ngay bên cạnh mà chú vẫn cười tươi rói cầm củ rễ cây chấm ăn ngon lành.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chẳng hề nhăn mặt, chẳng hề giật mình! Mẫu vật Chuột Chũi Trũi hoàn toàn trơ lì như không hề có chuyện gì xảy ra!". Bố cục: Đồng hồ đo phản ứng đau đớn trong phòng lab chỉ con số 0 tròn trĩnh, trong khi chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) nằm phơi bụng ngáp ngủ bình thản trước ống kính quan sát.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi mổ xẻ hệ thần kinh dưới kính hiển vi phân tử, các nhà khoa học phát hiện sợi thần kinh cảm giác dưới da của nó". Bố cục: Sơ đồ phóng đại sợi thần kinh C-fiber dưới kính hiển vi Bio-Lab: cô trợ lý mèo hoạt hình đeo kính cận tròn, mặc áo blouse trắng phòng thí nghiệm, cầm bảng kẹp hồ sơ sinh học phát sáng soi kính lúp vào sợi dây thần kinh dưới da của chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles).
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "hoàn toàn thiếu vắng một hợp chất truyền tin mang tên Substance P — vốn là chất phát tín hiệu báo động cảm giác bỏng rát lên não bộ ở mọi loài thú có vú.". Bố cục: Bản vẽ so sánh phân tử thần kinh: Sợi thần kinh của chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) trống trơn, không hề có các hạt truyền tin báo động Substance P màu đỏ. KHÔNG có chú Chuột Chũi Trũi trong cảnh này.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Độc đáo hơn nữa, nghiên cứu năm 2011 trên tạp chí Science đã chỉ ra rằng kênh truyền tín hiệu đau NaV1.7 của loài chuột này đã bị đột biến đảo ngược.". Bố cục: Bản vẽ phân tử năm 2011 trên tạp chí Science: Cấu trúc cổng kênh ion NaV1.7 trên màng tế bào thần kinh được phóng to như một cánh cổng cơ khí công nghệ cao. KHÔNG có chú Chuột Chũi Trũi trong cảnh này.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ở con người, khi gặp axit, kênh này mở toang để bắn tín hiệu đau đớn điên cuồng.". Bố cục: Sơ đồ so sánh bên trái: Khi các hạt axit màu xanh lá chạm vào cổng thần kinh thông thường, cánh cổng mở toang phát ra tia chớp báo động đỏ rực. KHÔNG có chú Chuột Chũi Trũi trong cảnh này.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng ở Chuột Chũi Trũi, chính phân tử axit lại biến thành chiếc chìa khóa đóng sập kênh NaV1.7 lại!". Bố cục: Sơ đồ so sánh bên phải: Ở chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles), các hạt axit lại biến thành chiếc ổ khóa vàng sập chặt cánh cổng NaV1.7 lại, chặn đứng mọi tia báo động.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tức là axit đối với nó chẳng khác nào thuốc gây tê miễn phí,". Bố cục: chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) đội mũ tắm hoa sen vui vẻ đứng dưới vòi phun sương axit nhẹ trong phòng thí nghiệm như đang được mát-xa gây tê thư giãn.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "giúp nó sống khỏe re dưới đáy hang ngầm ngập tràn khí CO2 đậm đặc gây axit hóa mô!". Bố cục: Trong lòng hang sâu đầy những đám mây khí CO2 màu tím nhạt: chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) vẫn vui vẻ đào đất và ca hát thoải mái như đang ở trong phòng điều hòa mát rượi.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu bài kiểm tra hóa chất vẫn chưa đủ làm khó mẫu vật, chúng ta nâng mức độ lên thử nghiệm cấp độ hai: Buồng chân không rút cạn sạch 0% oxy!". Bố cục: Buồng chân không thủy tinh cấp độ 2 trong phòng lab: Đồng hồ áp suất khí quyển và van khóa khí khổng lồ phát sáng màu đỏ cảnh báo. KHÔNG có chú Chuột Chũi Trũi trong cảnh này.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy tưởng tượng dưới lòng đất sâu 2m, 300 con chuột chũi chen chúc nhau trong một đường hầm bịt kín bưng chẳng có khe gió.". Bố cục: Mặt cắt địa chất dưới độ sâu 2m: 300 con chuột chũi giống chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) đang chen chúc chật kín trong một căn phòng đất chật hẹp không một khe thông gió.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nồng độ oxy ở đó thấp đến mức bất kỳ người hay con chuột bạch nào bước vào cũng sẽ ngất lịm và tử vong chỉ sau 60 giây.". Bố cục: chú chuột bạch hoạt hình lông trắng mập mạp đeo nơ xanh, biểu cảm nhát gan hay giật mình thót tim đội mũ bảo hiểm oxy đứng nhìn vào cửa hang tối om với vẻ mặt xanh mét, đồng hồ đo thời gian chịu đựng chỉ vỏn vẹn 60 giây. KHÔNG có chú Chuột Chũi Trũi trong cảnh này.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cảnh báo đỏ: Nồng độ oxy trong buồng thử nghiệm đã tụt về 0%! Nhịp tim mẫu vật giảm từ 200 nhịp/phút xuống còn 50 nhịp/phút!". Bố cục: Bảng điện tử buồng thử nghiệm nhấp nháy: Chỉ số O2 tụt thẳng về 0%, màn hình nhịp tim của chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) hạ từ 200 nhịp/phút xuống 50 nhịp/phút để tiết kiệm năng lượng.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "1 phút trôi qua... 5 phút... 10 phút... rồi đúng 18 phút hoàn toàn chẳng có lấy một phân tử oxy nào! Mẫu vật nằm bất động trong trạng thái đình trệ sinh học.". Bố cục: Đồng hồ bấm giờ kỹ thuật số trong phòng lab quay vùn vụt từ 1 phút, 5 phút, 10 phút tới mốc 18 phút đỏ rực, bên trong lồng kính chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) nằm im như đang ngủ say.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thế nhưng ngay khoảnh khắc van oxy được mở trở lại, gã Dị Nhân Khoai Tây lập tức vươn vai đứng dậy đi lại tỉnh bơ mà không hề bị tổn thương một tế bào não hay cơ tim nào!". Bố cục: Khi luồng khí oxy màu xanh da trời vừa được bơm vào lồng kính, chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) lập tức bật dậy vươn vai tập thể dục khỏe re trước đôi mắt tròn xoe kinh ngạc của cô trợ lý mèo hoạt hình đeo kính cận tròn, mặc áo blouse trắng phòng thí nghiệm, cầm bảng kẹp hồ sơ sinh học phát sáng.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bí mật nằm ở công trình chấn động công bố trên tạp chí Science năm 2017.". Bố cục: Trang bìa tạp chí khoa học Science năm 2017 đặt trên bàn thí nghiệm với biểu đồ phân tích quá trình chuyển hóa năng lượng thần kỳ của não bộ chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles).
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi thiếu oxy, mọi loài động vật có vú đều bị tắc nghẽn dây chuyền đốt đường Glucose làm tế bào não chết ngạt.". Bố cục: Sơ đồ nhà máy tế bào thông thường: Dây chuyền đốt đường Glucose bị khóa đứng với biển báo 'HẾT OXY - NGỪNG HOẠT ĐỘNG', đèn điện tắt phụt. KHÔNG có chú Chuột Chũi Trũi trong cảnh này.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng Chuột Chũi Trũi đã thực hiện một cú chuyển đổi sinh học không tưởng: Nó bật công tắc chuyển sang đốt đường Fructose — tức là loại đường trái cây —". Bố cục: Sơ đồ nhà máy tế bào của chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles): Chú gạt cần công tắc dự phòng màu xanh lá cây, mở cổng bơm phân tử đưa các viên đường trái cây Fructose phát sáng vào lò năng lượng.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "thông qua các bơm phân tử chuyên biệt để nuôi sống não bộ mà không cần oxy!". Bố cục: Bản vẽ giải phẫu não và tim của chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles): Các đường ống dẫn đường Fructose phát sáng màu vàng cam cung cấp năng lượng liên tục giữ cho não và tim sáng rực.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đây vốn là cơ chế trao đổi chất độc quyền của giới thực vật!". Bố cục: Bản vẽ so sánh Bio-Lab: Một bên là chậu cây xanh và củ khoai tây, bên kia là chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) với chiếc mầm lá xanh ngộ nghĩnh mọc trên mũ bảo hộ, cả hai cùng phát sáng năng lượng Fructose.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nói cách khác, khi hết sạch không khí, nó tạm thời biến thành một củ khoai tây thực thụ để chờ thời, rồi lại hoàn hồn làm động vật khi có gió về!". Bố cục: Cảnh bi hài hai trạng thái: Khi hết gió chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) hóa trang thành củ khoai tây nằm im thin thít, vừa có làn gió mát thổi qua đã bật dậy nhảy điệu disco sôi động.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chuyển sang thử nghiệm cấp độ ba: Khả năng kháng bệnh nan y!". Bố cục: Phòng thí nghiệm y sinh học cấp độ 3: Màn hình lớn hiển thị biểu đồ lá chắn bảo vệ tế bào màu xanh lục bảo lấp lánh. KHÔNG có chú Chuột Chũi Trũi trong cảnh này.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thông thường, tới hơn 70% các loài chuột trong phòng thí nghiệm sẽ tử vong vì các khối u ung thư khi về già.". Bố cục: Biểu đồ thống kê y khoa trong phòng lab: Cột tỷ lệ mắc khối u ở loài chuột thường cao vọt lên mức 70% khiến chú chuột bạch hoạt hình lông trắng mập mạp đeo nơ xanh, biểu cảm nhát gan hay giật mình thót tim nhìn biểu đồ lo lắng. KHÔNG có chú Chuột Chũi Trũi trong cảnh này.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thế nhưng khi giáo sư Vera Gorbunova và cộng sự tại Đại học Rochester theo dõi hàng ngàn cá thể Chuột Chũi Trũi suốt hàng chục năm trời,". Bố cục: Bảng theo dõi hàng ngàn hồ sơ sức khỏe của chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) tại Đại học Rochester: Tất cả các ô kiểm tra đều đóng dấu tích xanh hoàn hảo 'KHỎE MẠNH 100%'.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "họ phát hiện một con số gây chấn động y học thế giới: Hầu như không có bất kỳ cá thể nào mắc bệnh ung thư!". Bố cục: chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) đeo huy chương vàng 'ZERO UNG THƯ' đứng hiên ngang trên bục kính hiển vi trước sự thán phục của cô trợ lý mèo hoạt hình đeo kính cận tròn, mặc áo blouse trắng phòng thí nghiệm, cầm bảng kẹp hồ sơ sinh học phát sáng.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Khi kiểm tra dịch nuôi cấy tế bào của chúng vào năm 2013, các nhà nghiên cứu thấy dung dịch cứ đặc quánh và nhớt nhầy như hồ dán làm tắc nghẽn cả ống hút phòng lab!". Bố cục: Cảnh phòng lab năm 2013 vui nhộn: cô trợ lý mèo hoạt hình đeo kính cận tròn, mặc áo blouse trắng phòng thí nghiệm, cầm bảng kẹp hồ sơ sinh học phát sáng đang cố bóp ống hút thủy tinh nhưng dung dịch nuôi cấy tế bào của chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) đặc quánh và dẻo quẹo như keo dán làm tắc cả ống.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thủ phạm chính là hợp chất đường siêu phân tử Hyaluronic Acid khối lượng cực cao, viết tắt là HMW-HA.". Bố cục: Sơ đồ cấu trúc hóa học phát sáng: Các chuỗi phân tử đường Hyaluronic Acid (HMW-HA) xoắn lại như những sợi dây thừng vàng khổng lồ bao quanh tế bào của chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles).
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ở con người, hợp chất này vốn được dùng làm chất giữ ẩm trong mỹ phẩm dưỡng da, nhưng ở Chuột Chũi Trũi, chuỗi phân tử của nó dài và nặng gấp 5 lần so với của người!". Bố cục: Phép so sánh kích thước phân tử trực quan: Một bên là lọ kem dưỡng ẩm nhỏ xíu với sợi phân tử ngắn ngủn của người, bên kia là chuỗi siêu phân tử HMW-HA của chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) dài và nặng gấp 5 lần!
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lớp siêu keo HMW-HA này tạo thành một mạng lưới lồng sắt đàn hồi cực kỳ dày đặc bao bọc quanh từng tế bào của Dị Nhân Khoai Tây.". Bố cục: Mặt cắt kính hiển vi: Các tế bào khỏe mạnh được bao bọc bởi một hàng rào lưới gel đàn hồi màu xanh ngọc cực kỳ vững chắc như pháo đài.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhờ lớp đệm siêu đàn hồi đó mà làn da của nó mới nhăn nheo và co giãn rộng thùng thình, giúp nó luồn lách và quay đầu 180° ngay trong lòng đường hầm chật hẹp mà không bị rách da!". Bố cục: chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) đang biểu diễn màn nhào lộn quay đầu 180° ngay bên trong một chiếc ống nhựa hẹp, lớp da rộng thùng thình co giãn dẻo dai như cao su.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Quan trọng hơn cả, mạng lưới siêu keo này kích hoạt cơ chế ức chế tiếp xúc sớm thông qua bộ khóa bảo vệ kép gồm hai gen p16 và p27.". Bố cục: Bản vẽ cơ chế phòng thủ tế bào: Cánh cửa nhân đôi tế bào được gắn tới 2 chiếc ổ khóa kim loại kiên cố khắc nhãn 'p16' và 'p27'. KHÔNG có chú Chuột Chũi Trũi trong cảnh này.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ở cơ thể người, chúng ta chỉ có một ổ khóa p27, nên khi tế bào đột biến nhân lên chật chội, khối u vẫn có thể phá khóa phát triển.". Bố cục: Sơ đồ đối chiếu: Cánh cửa chỉ có 1 ổ khóa p27 đơn lẻ đang bị nhân vật quái vật tế bào đột biến hoạt hình màu tím tròn xoe ngộ nghĩnh đội mũ sừng nhỏ, mặt mếu máo bất lực lén dùng xà beng cậy ra để chen lấn nhân bản. KHÔNG có chú Chuột Chũi Trũi trong cảnh này.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn ở Chuột Chũi Trũi, ngay khi vài tế bào bất thường vừa chạm nhẹ vào nhau, ổ khóa thứ hai p16 lập tức sập xuống,". Bố cục: Ngay khi nhân vật quái vật tế bào đột biến hoạt hình màu tím tròn xoe ngộ nghĩnh đội mũ sừng nhỏ, mặt mếu máo bất lực vừa chạm nhẹ vào hàng rào siêu keo HMW-HA, chiếc khóa thép khổng lồ p16 lập tức sập xuống.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "ra lệnh đóng băng toàn bộ quá trình phân chia, bóp nghẹt mầm mống ung thư ngay từ trong trứng nước!". Bố cục: nhân vật quái vật tế bào đột biến hoạt hình màu tím tròn xoe ngộ nghĩnh đội mũ sừng nhỏ, mặt mếu máo bất lực bị giam chặt cứng trong lồng kính siêu keo HMW-HA đứng hình mếu máo, bên cạnh chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) giơ ngón cái chiến thắng.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bước vào thử nghiệm cấp độ bốn: Quan sát hành vi xã hội!". Bố cục: Sơ đồ mặt cắt địa chất khổng lồ cấp độ 4: Một mê cung thành phố ngầm chằng chịt dưới lòng đất được quan sát qua màn hình radar địa chấn. KHÔNG có chú Chuột Chũi Trũi trong cảnh này.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Năm 1981, nhà sinh vật học Jennifer Jarvis đã phát hiện Chuột Chũi Trũi là loài thú có vú hiếm hoi trên Trái Đất sống theo mô hình xã hội côn trùng chân chính y hệt loài kiến và mối!". Bố cục: Bản vẽ so sánh sinh thái học năm 1981: Một bên là tổ kiến và tổ mối, bên kia là đàn của chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) với cấu trúc phân tầng xã hội giống hệt nhau.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một vương quốc ngầm dài từ 3-5km chứa tới 300 cá thể, nhưng chỉ có duy nhất một Nữ Hoàng tối cao được phép sinh con đẻ cái cùng ba gã hoàng phu!". Bố cục: Bản đồ toàn cảnh vương quốc ngầm trải dài 3-5km dưới lòng đất chứa 300 cá thể, ở trung tâm là cung điện hoàng gia nơi Nữ Hoàng Chuột Chũi hoạt hình to gấp đôi, đội vương miện vàng lấp lánh, mặc áo choàng nhung đỏ oai vệ chống nạnh hét ra lửa ngự trị trên ngai vàng rễ cây.
```
</details>

<details><summary>L57</summary>

```text
HÌNH L57 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tất cả nghe lệnh ta! Đội công nhân xếp hàng đào đất! Đội chiến binh ra chặn cửa hang! Đứa nào dám yêu đương lén lút ta húc cho văng vào vách đá!". Bố cục: Nữ Hoàng Chuột Chũi hoạt hình to gấp đôi, đội vương miện vàng lấp lánh, mặc áo choàng nhung đỏ oai vệ chống nạnh hét ra lửa đội vương miện vàng đứng trên bục đất cao cầm loa phóng thanh hét lớn, phía dưới là đội công nhân đội mũ bảo hộ vàng và đội chiến binh cầm khiên rễ cây xếp hàng răm rắp.
```
</details>

<details><summary>L58</summary>

```text
HÌNH L58 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nữ Hoàng cai trị bằng nắm đấm sắt đúng nghĩa đen! Mỗi lần mang thai, các đốt xương sống của Nữ Hoàng tự động kéo dài ra như lò xo để chứa tới gần 30 đứa con trong bụng.". Bố cục: Sơ đồ X-quang giải phẫu Nữ Hoàng Chuột Chũi hoạt hình to gấp đôi, đội vương miện vàng lấp lánh, mặc áo choàng nhung đỏ oai vệ chống nạnh hét ra lửa: Các đốt xương sống của Nữ Hoàng tự động giãn dài ra như lò xo để chứa ổ bụng khổng lồ mang tới gần 30 đứa con. KHÔNG có chú Chuột Chũi Trũi trong cảnh này.
```
</details>

<details><summary>L59</summary>

```text
HÌNH L59 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong khi đó, hàng trăm thần dân còn lại bị Nữ Hoàng dùng áp lực cơ học húc đẩy liên tục khiến hormone sinh sản bị khóa chặt suốt đời!". Bố cục: Nữ Hoàng Chuột Chũi hoạt hình to gấp đôi, đội vương miện vàng lấp lánh, mặc áo choàng nhung đỏ oai vệ chống nạnh hét ra lửa đi tuần tra trong đường hầm, dùng cái mũi húc nhẹ thị uy khiến các chú chuột công nhân xung quanh lập tức cúi rạp người chăm chỉ làm việc. KHÔNG có chú Chuột Chũi Trũi trong cảnh này.
```
</details>

<details><summary>L60</summary>

```text
HÌNH L60 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đội công nhân phải xếp thành một dây chuyền băng tải sống: con đầu tiên dùng răng khoét đất, hàng chục con phía sau cứ thế đá đất qua háng nhau chạy tít ra cửa hang!". Bố cục: Dây chuyền băng tải đào hầm siêu hài hước: chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) ở đầu hàng dùng răng khoét đất, 5 chú chuột phía sau xếp hàng dọc đồng loạt đá đất qua háng nhau bay vèo ra cửa hang.
```
</details>

<details><summary>L61</summary>

```text
HÌNH L61 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và chi tiết lầy lội nhất của đế chế này chính là quy định nhận diện công dân: Vì dưới hang tối đen như mực không nhìn thấy mặt nhau, cả 300 con chuột trong đàn đều phải lăn lộn vào chung một buồng nhà vệ sinh duy nhất!". Bố cục: Căn phòng nhà vệ sinh chung của vương quốc ngầm: Biển hiệu 'PHÒNG NƯỚC HOA GIA TỘC' treo trên vách đất, các chú chuột xếp hàng xịt mùi hương đồng bộ để nhận diện đồng hương.
```
</details>

<details><summary>L62</summary>

```text
HÌNH L62 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhờ tắm chung mùi chất thải đặc trưng của gia tộc, chúng nhận ra đồng đội ngay lập tức, kẻ lạ nào khác mùi mò vào sẽ bị đội chiến binh tóm cổ ngay!". Bố cục: Hai chú chuột chiến binh gác cổng đeo kính râm đang dùng máy quét mùi hương kiểm tra chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles), đèn xanh bật sáng cho phép qua cổng an toàn.
```
</details>

<details><summary>L63</summary>

```text
HÌNH L63 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thế nhưng vị hoàng đế ngầm này lại mang một tử huyệt chí mạng: Chúng đã đánh mất hoàn toàn lớp mỡ nâu và khả năng tự điều chỉnh thân nhiệt của loài thú có vú, trở thành sinh vật biến nhiệt chẳng khác nào loài bò sát nước màu lạnh!". Bố cục: Sơ đồ nhiệt kế sinh học Bio-Lab: Cơ thể chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) không có lớp mỡ nâu giữ nhiệt, vạch nhiệt độ biến đổi y hệt một chú thằn lằn nước màu lạnh bên cạnh.
```
</details>

<details><summary>L64</summary>

```text
HÌNH L64 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ở trong hang sâu nhiệt độ luôn ổn định quanh mức 30°C,". Bố cục: Nhiệt kế trong đường hầm đất sâu chỉ đúng 30°C ấm áp, chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) đang ngồi uống trà thư giãn dễ chịu.
```
</details>

<details><summary>L65</summary>

```text
HÌNH L65 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nhưng nếu bị lôi ra ngoài trời lạnh dưới 15°C hoặc nắng nóng trên 35°C, siêu dị nhân chống axit và ung thư của chúng ta sẽ lập tức đơ cứng vì sốc nhiệt!". Bố cục: Cảnh đối lập nhiệt độ hài hước: Dưới mức 15°C chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) quấn chăn run cầm cập đóng băng, còn trên mức 35°C thì lè lưỡi quạt phành phạch vì sốc nhiệt.
```
</details>

<details><summary>L66</summary>

```text
HÌNH L66 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Để giữ ấm, cả đàn chỉ còn cách rúc vào nhau nằm chồng chất thành một đống khoai tây khổng lồ!". Bố cục: Trong hang đất ấm áp: Hàng chục chú chuột chũi cùng chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) ôm chặt lấy nhau chồng chất thành một ngọn núi khoai tây hồng khổng lồ tỏa ra những trái tim ấm áp.
```
</details>

<details><summary>L67</summary>

```text
HÌNH L67 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cuối cùng, bài thử nghiệm cấp độ năm cũng là đỉnh cao vĩ đại nhất của Dị Nhân Khoai Tây mang mã số 32: Thử thách thời gian!". Bố cục: Phòng thí nghiệm thời gian cấp độ 5: Chiếc đồng hồ cát vàng khổng lồ và biểu đồ trường thọ phát sáng rực rỡ trên màn hình chính. KHÔNG có chú Chuột Chũi Trũi trong cảnh này.
```
</details>

<details><summary>L68</summary>

```text
HÌNH L68 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một con chuột nhắt có cùng kích thước chỉ sống được tối đa từ 2-3 năm là già yếu qua đời.". Bố cục: Bên trái sơ đồ thời gian: chú chuột bạch hoạt hình lông trắng mập mạp đeo nơ xanh, biểu cảm nhát gan hay giật mình thót tim chống gậy râu bạc trắng sau 2-3 năm tuổi, bên cạnh là cuốn lịch bàn đã hết trang. KHÔNG có chú Chuột Chũi Trũi trong cảnh này.
```
</details>

<details><summary>L69</summary>

```text
HÌNH L69 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thế nhưng Chuột Chũi Trũi có thể sống khỏe mạnh tới 37 năm — tức là gấp hơn 12 lần tuổi thọ dự kiến!". Bố cục: Bên phải sơ đồ thời gian: chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) đeo dải băng kỷ niệm 37 năm (gấp 12 lần) vẫn đang nhảy hip-hop sung sức trên bàn thí nghiệm!
```
</details>

<details><summary>L70</summary>

```text
HÌNH L70 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu quy đổi sang thước đo của con người, nó tương đương với một cụ già sống thọ tới hơn 800 tuổi!". Bố cục: chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) mặc bộ đồ tiên ông trường thọ cưỡi hạc giấy, tay cầm quả đào tiên bên cạnh tấm biển kỷ lục quy đổi tương đương 800 tuổi ở con người.
```
</details>

<details><summary>L71</summary>

```text
HÌNH L71 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Năm 2018, nhà sinh học Rochelle Buffenstein đã công bố dữ liệu theo dõi hơn 3.000 cá thể suốt ba thập kỷ và chứng minh Chuột Chũi Trũi đã đập tan định luật lão hóa Gompertz.". Bố cục: Đồ thị toán học năm 2018 trên màn hình Bio-Lab: Nhà nghiên cứu chỉ vào dữ liệu theo dõi hơn 3.000 cá thể chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) suốt ba thập kỷ.
```
</details>

<details><summary>L72</summary>

```text
HÌNH L72 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ở mọi sinh vật khác, càng lớn tuổi thì nguy cơ tử vong càng tăng theo cấp số nhân.". Bố cục: Biểu đồ so sánh Định luật lão hóa Gompertz: Đường màu đỏ của thú thông thường dốc dựng đứng lên cao, còn đường màu xanh lục của chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) chạy ngang phẳng lì!
```
</details>

<details><summary>L73</summary>

```text
HÌNH L73 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng ở loài chuột này, một cụ chuột 30 tuổi vẫn có trái tim khỏe mạnh, mật độ xương rắn chắc và tế bào tự dọn rác hoàn hảo y hệt một thanh niên 2 tuổi!". Bố cục: chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) ở tuổi 30 tuổi đang nâng tạ đôi trong phòng lab, chỉ số tim mạch, xương khớp và bộ máy dọn rác tế bào đều trẻ khỏe như 2 tuổi.
```
</details>

<details><summary>L74</summary>

```text
HÌNH L74 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó chính là chìa khóa vàng giúp y học nhân loại giải mã giấc mơ trường thọ và chiến thắng bệnh ung thư trong tương lai.". Bố cục: chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) đứng trên bục vinh danh khoa học, trao chiếc chìa khóa vàng khắc hình chuỗi DNA trường thọ cho cô trợ lý mèo hoạt hình đeo kính cận tròn, mặc áo blouse trắng phòng thí nghiệm, cầm bảng kẹp hồ sơ sinh học phát sáng trong tiếng pháo giấy chúc mừng.
```
</details>

<details><summary>L75</summary>

```text
HÌNH L75 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hội đồng khoa học thân mến, sau năm cấp độ thử nghiệm điên rồ vừa rồi, bạn thấy siêu năng lực nào của Chuột Chũi Trũi đỉnh chóp nhất:". Bố cục: Hội đồng giám khảo trong phòng thí nghiệm nhìn lên màn hình tổng kết 5 bài kiểm tra sinh tồn của chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles).
```
</details>

<details><summary>L76</summary>

```text
HÌNH L76 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy ghi ngay đánh giá của bạn xuống phần bình luận bên dưới nhé!". Bố cục: chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) và cô trợ lý mèo hoạt hình đeo kính cận tròn, mặc áo blouse trắng phòng thí nghiệm, cầm bảng kẹp hồ sơ sinh học phát sáng vẫy tay chào khán giả bên cạnh hòm phiếu bình chọn phát sáng trong phòng lab.
```
</details>

<details><summary>L77</summary>

```text
HÌNH L77 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và ngay trong hồ sơ Tập 33 tiếp theo, chúng ta sẽ rời căn hầm nóng bức Đông Phi để bay tới vùng băng giá Bắc Cực lạnh -20°C!". Bố cục: Khung cảnh chuyển sang vùng rừng tuyết Bắc Cực lạnh -20°C: Bão tuyết trắng xóa bao phủ những gốc cây thông đóng băng. KHÔNG có chú Chuột Chũi Trũi trong cảnh này.
```
</details>

<details><summary>L78</summary>

```text
HÌNH L78 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tại đó có một quái kiệt lưỡng cư tự biến hai phần ba lượng nước trong cơ thể thành một cục nước đá cứng ngắc suốt 8 tháng mùa đông:". Bố cục: Một bóng đen chú ếch nhỏ nằm bất động bên trong khối băng tinh thể trong suốt lấp lánh suốt 8 tháng mùa đông dưới ánh cực quang. KHÔNG có chú Chuột Chũi Trũi trong cảnh này.
```
</details>

<details><summary>L79</summary>

```text
HÌNH L79 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tim ngừng đập hoàn toàn, nước màu ngừng chảy, não bộ tắt nguồn như đã chết, nhưng ngay khi nắng xuân vừa chạm tới lại tự rã đông nhảy nhót tỉnh bơ! Đố bạn đoán được sinh vật đóng băng bất tử tiếp theo này là ai?". Bố cục: Khối băng bọc quanh bóng đen chú ếch bí ẩn nứt ra khi tia nắng mùa xuân chiếu rọi, đôi mắt chú ếch bất ngờ mở bừng sáng lấp lánh kèm dấu chấm hỏi lớn. KHÔNG có chú Chuột Chũi Trũi trong cảnh này.
```
</details>

<details><summary>L80</summary>

```text
HÌNH L80 (16:9 ngang, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vô cảm trước axit nhờ khóa kênh thần kinh, hóa thành thực vật sống 18 phút không cần oxy, hay lớp siêu keo HMW-HA bóp nghẹt mọi khối u ung thư?". Bố cục: Bảng tổng kết 3 siêu năng lực đỉnh chóp của chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles): (1) Khiên chống axit NaV1.7, (2) Lá cây Fructose sống 18 phút 0% oxy, (3) Lồng sắt siêu keo HMW-HA khóa ung thư.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Cảnh báo sinh học cấp độ năm!". Bố cục: Cận cảnh giữa khung dọc: chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) ngồi trong lồng kính Bio-Lab phát sáng màu tím-xanh neon, tay cầm bảng hồ sơ 'BẤT TỬ UNG THƯ', gương mặt nhăn nheo cười khẩy cực ngầu.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Tại sao loài chuột xấu xí nhăn nheo như củ khoai tây luộc này". Bố cục: Phép so sánh vui nhộn: Một bên là củ khoai tây luộc nhăn nheo, bên kia là chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) đang tập tạ giữa vòng khiên bảo vệ xanh lục bảo.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Đây là Chuột Chũi Trũi Đông Phi, siêu dị nhân bất tử dưới lòng đất!". Bố cục: chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) đứng trên bục thí nghiệm giữa lòng đất Đông Phi, khoe hai chiếc răng cửa trắng to mọc xuyên qua môi và chiếc kính bảo hộ xanh neon.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Khi các nhà khoa học theo dõi hàng ngàn cá thể suốt 37 năm, họ sững sờ khi thấy chúng gần như không bao giờ mắc ung thư.". Bố cục: cô trợ lý mèo hoạt hình đeo kính cận tròn, mặc áo blouse trắng phòng thí nghiệm, cầm bảng kẹp hồ sơ sinh học phát sáng cầm kính lúp soi vào bảng theo dõi 37 năm của chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles), mọi chỉ số sức khỏe đều đóng dấu khiên xanh miễn nhiễm bệnh tật.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Bí mật nằm ở chỗ tế bào của chúng tiết ra một chất siêu keo tên là Hyaluronic Acid có phân tử nặng gấp 5 lần con người!". Bố cục: Sơ đồ phóng đại tế bào của chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles): Các chuỗi phân tử siêu keo Hyaluronic Acid màu vàng óng xoắn dày đặc, dài và nặng gấp 5 lần phân tử thông thường.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Lớp siêu keo này kết hợp cùng bộ khóa gen kép p16 và p27,". Bố cục: Hai chiếc ổ khóa kim loại khổng lồ khắc chữ 'p16' và 'p27' gắn trên hàng rào lưới gel xanh ngọc bao quanh tế bào của chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles).
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "tạo thành chiếc lồng sắt khóa chặt và bóp nghẹt mọi tế bào khối u ngay từ khi mới chớm!". Bố cục: Chiếc lồng sắt siêu keo sập xuống khóa chặt nhân vật quái vật tế bào đột biến hoạt hình màu tím tròn xoe ngộ nghĩnh đội mũ sừng nhỏ, mặt mếu máo bất lực bên trong khiến nó mếu máo đứng hình, bên cạnh chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) giơ ngón cái chiến thắng.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Chưa hết, khi bị nhốt trong hầm kín 0% oxy suốt 18 phút,". Bố cục: Buồng chân không thí nghiệm báo 0% oxy: Đồng hồ đếm tới mốc 18 phút, trong khi chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) nằm thư giãn bình thản bên trong.
```
</details>

<details><summary>S09</summary>

```text
HÌNH S09 (DỌC 9:16, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "nó lập tức biến hình thành thực vật, đốt đường trái cây Fructose để nuôi não bộ mà chẳng cần hít thở!". Bố cục: chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) bật công tắc sinh học màu xanh lá, trên đầu mọc lên chiếc mầm cây phát sáng đang hút các phân tử đường trái cây Fructose nuôi não bộ.
```
</details>

<details><summary>S10</summary>

```text
HÌNH S10 (DỌC 9:16, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Một kiệt tác y sinh học giúp nó sống thọ tới 37 năm!". Bố cục: chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) đội vương miện trường thọ 37 năm đứng trên đỉnh cúp vàng y sinh học, giơ hai ngón tay chiến thắng rạng rỡ.
```
</details>

<details><summary>S11</summary>

```text
HÌNH S11 (DỌC 9:16, cùng phong cách Bio-Lab Schematic hoạt hình 2D và cùng nhân vật chú Chuột Chũi Trũi da hồng nhăn nheo đeo kính bảo hộ phòng lab màu xanh neon; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "lại miễn nhiễm hoàn toàn với bệnh ung thư và sống sót 18 phút không cần một giọt oxy nào?". Bố cục: chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles) đứng trong buồng thí nghiệm với lá chắn chống khối u sáng chói và đồng hồ 18 phút không oxy.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/79 của video YouTube về Chuột Chũi Trũi). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa 2D Bio-Lab Schematic kết hợp hoạt hình châm biếm hài hước (Dark Comedy Scientific Illustration): nét mực đen đậm sắc sảo, phối hợp các chi tiết sơ đồ giải phẫu sinh học, bình thí nghiệm, lưới tọa độ tế bào và mảng màu tươi sáng tương phản cao (tím phòng lab, xanh lục bảo neon, vàng hổ phách và hồng phấn nhân vật); biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles). Nhân vật phụ cố định: cô trợ lý mèo hoạt hình đeo kính cận tròn, mặc áo blouse trắng phòng thí nghiệm, cầm bảng kẹp hồ sơ sinh học phát sáng; chú chuột bạch hoạt hình lông trắng mập mạp đeo nơ xanh, biểu cảm nhát gan hay giật mình thót tim; Nữ Hoàng Chuột Chũi hoạt hình to gấp đôi, đội vương miện vàng lấp lánh, mặc áo choàng nhung đỏ oai vệ chống nạnh hét ra lửa; nhân vật quái vật tế bào đột biến hoạt hình màu tím tròn xoe ngộ nghĩnh đội mũ sừng nhỏ, mặt mếu máo bất lực. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/11 của video YouTube Shorts về Chuột Chũi Trũi). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa 2D Bio-Lab Schematic kết hợp hoạt hình châm biếm hài hước (Dark Comedy Scientific Illustration): nét mực đen đậm sắc sảo, phối hợp các chi tiết sơ đồ giải phẫu sinh học, bình thí nghiệm, lưới tọa độ tế bào và mảng màu tươi sáng tương phản cao (tím phòng lab, xanh lục bảo neon, vàng hổ phách và hồng phấn nhân vật); biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Chuột Chũi Trũi hoạt hình da hồng phấn nhăn nheo đáng yêu như củ khoai tây, thân hình trụi lông mũm mĩm, hai chiếc răng cửa trắng to nhô ra ngoài môi, đầu đeo chiếc kính bảo hộ phòng thí nghiệm màu xanh neon ngộ nghĩnh (cute neon-green bio-lab safety goggles). Nhân vật phụ: cô trợ lý mèo hoạt hình đeo kính cận tròn, mặc áo blouse trắng phòng thí nghiệm, cầm bảng kẹp hồ sơ sinh học phát sáng; nhân vật quái vật tế bào đột biến hoạt hình màu tím tròn xoe ngộ nghĩnh đội mũ sừng nhỏ, mặt mếu máo bất lực. 
```
</details>

## 7. SEO

- **title:** Sinh Vật Sống Ở Mức 0% Oxy & Miễn Nhiễm Hoàn Toàn Ung Thư?! | Tập 32
- **hook_paragraph:** Chuột Chũi Trũi (Heterocephalus glaber) trông nhăn nheo như củ khoai tây luộc nhưng sở hữu 5 siêu năng lực thách thức mọi định luật sinh học: vô cảm trước axit, hóa thành thực vật sống 18 phút ở mức 0% oxy, miễn nhiễm ung thư nhờ siêu keo phân tử HMW-HA và sống thọ tới 37 năm!
- **question:** Trong 5 siêu năng lực của Chuột Chũi Trũi, bạn thấy khả năng nào phi thường nhất: Vô cảm trước axit, hóa thực vật sống 18 phút 0% oxy, hay lớp siêu keo HMW-HA khóa chặt ung thư?
- **next_teaser:** sinh vật Bắc Cực tự đóng băng cơ thể thành cục đá suốt mùa đông, tim ngừng đập nhưng mùa xuân lại tự rã đông sống dậy
- **shorts_title:** Tại Sao Loài Chuột Xấu Xí Nhất Hành Tinh Không Bao Giờ Bị Ung Thư?!
- **shorts_desc:** Chuột Chũi Trũi (Heterocephalus glaber) tiết ra hợp chất siêu keo Hyaluronic Acid (HMW-HA) nặng gấp 5 lần con người kết hợp khóa gen kép p16/p27 bóp nghẹt mọi khối u ung thư, đồng thời hóa thành thực vật sống 18 phút không cần oxy và thọ tới 37 năm!
- **bullets:** Bộ răng cửa mọc xuyên qua lớp môi và cơ hàm chiếm 25% cơ thể chuyên đục đất cứng như bê tông · Đột biến khóa kênh thần kinh NaV1.7 và thiếu chất Substance P giúp vô cảm hoàn toàn trước axit và chất cay ớt hiểm · Chuyển đổi trao đổi chất sang đốt đường Fructose kỵ khí như thực vật để sống sót 18 phút ở môi trường 0% oxy · Hợp chất siêu keo Hyaluronic Acid HMW-HA nặng gấp 5 lần người và khóa kép p16/p27 chặn đứng 100% khối u ung thư · Đế chế Nữ Hoàng độc tài dưới lòng đất và tuổi thọ kỷ lục 37 năm phá vỡ định luật lão hóa Gompertz
- **tags:** chuột chũi trũi, chuột chũi, naked mole rat, heterocephalus glaber, động vật miễn nhiễm ung thư, sống không cần oxy, hyaluronic acid hmw-ha, động vật bất tử, chuột sống 37 năm, sinh vật kỳ lạ nhất thế giới, thế giới động vật, vẽ chuyện hoang dã, whiteboard animation, khoa học vui
- **hashtags:** #độngvật #chuộtchũi #VẽChuyệnHoangDã

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-32-chuot-chui-trui
python src/episode/pipeline.py tts    projects/tap-32-chuot-chui-trui     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-32-chuot-chui-trui     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-32-chuot-chui-trui     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-32-chuot-chui-trui              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-32-chuot-chui-trui --force
python scripts/beat_sheet.py projects/tap-32-chuot-chui-trui               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-32-chuot-chui-trui/audio/shorts.wav projects/tap-32-chuot-chui-trui/renders/tap-32-chuot-chui-trui_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-32-chuot-chui-trui
python src/episode/pipeline.py seo    projects/tap-32-chuot-chui-trui
python src/episode/episode_doc.py     projects/tap-32-chuot-chui-trui
```
