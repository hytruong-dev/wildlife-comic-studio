# TẬP 23 — HẢI SÂM · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-23-hai-sam`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-23-hai-sam`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F1` · **Persona giọng:** `bac_si` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Hải Sâm |
| Tiêu đề YouTube | Sinh Vật Không Não Bắn Cả Bộ Ruột Qua Hậu Môn Để Thoát Thân?! |
| Video dài | `renders/tap-23-hai-sam_long.mp4` — 9:38.9 (578.9s) |
| Shorts | `renders/tap-23-hai-sam_shorts.mp4` — 0:49.0 (49.0s) |
| Thumbnail | `renders/tap-23-hai-sam_thumbnail.jpg` |
| Số hình | dài 72 beat / 72 ảnh riêng; Shorts 12 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.1**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/72 của video YouTube về Hải Sâm). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán. Nhân vật phụ cố định: ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế; cô trợ lý phòng khám hoạt hình mặc áo blouse xanh nhạt; chú cá ngọc nhỏ nhắn màu bạc trong suốt trơn tuột với nụ cười láu cá tinh nghịch. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — CA CẤP CỨU SINH VẬT KHÔNG NÃO, KHÔNG MẮT, KHÔNG TIM
*Badge:* `BỆNH ÁN #23` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene01_p0.wav` (463 ký tự) · mood `tram_bi_an`

```text
Phòng cấp cứu y khoa dã thiết lập tại trạm nghiên cứu đáy biển sâu. Chuông báo động vang lên hồi còi gấp rút, đèn mổ bật sáng trên khay kim loại khử trùng. Bệnh nhân số hai mươi ba tự trườn vào phòng khám với dáng vẻ chậm rãi kỳ quặc đến mức không tưởng: một cục thịt dài ngoằng màu nâu đốm vàng, mềm oặt như chiếc xúc xích bị bỏ quên dưới đáy cát... Không có hộp sọ. Không có bộ não. Không có lấy một đôi mắt. Và thậm chí không có cả một trái tim để đập bơm máu!
```
**Part 1** → `audio/vs/scene01_p1.wav` (147 ký tự) · 🎭 cameo `co_tro_ly`

```text
Bác sĩ ơi, em đo nhịp tim mãi mà máy cứ kêu tút tút bằng phẳng, bệnh nhân này thực sự là một sinh vật sống hay là một khúc chả lụa dưới biển vậy ạ?
```
**Part 2** → `audio/vs/scene01_p2.wav` (481 ký tự) · mood `hao_hung`

```text
[surprise-oh] Trợ lý bình tĩnh, bệnh nhân vẫn đang sống nhăn răng... à quên, nó còn chẳng thèm có răng nữa cơ! [laughter] Xin giới thiệu với các đồng nghiệp: đây là Hải Sâm, sinh vật da gai thuộc lớp Động vật chân gai, họ hàng xa với sao biển và cầu gai. Kích thước trung bình dài khoảng hai mươi đến ba mươi xăng-ti-mét. Nhìn bề ngoài thì lù đù ngây ngô như khúc dưa chuột biển vô hại, nhưng trong giới sinh học biển, chúng tôi gọi thẳng tên nó bằng biệt danh: Quái Kiệt Ruột Mềm!
```
**Part 3** → `audio/vs/scene01_p3.wav` (483 ký tự) · mood `nghiem_trang_gia`

```text
Đừng để vẻ ngoài vô tri đó đánh lừa! Dù bị tước đoạt hầu hết các cơ quan nội tạng tiêu chuẩn của động vật có xương sống, Hải Sâm lại sở hữu những siêu năng lực tự vệ quái đản bậc nhất hành tinh: cơ thể tự hóa lỏng thành thạch nhớt trong tích tắc, thở trực tiếp bằng đường... hậu môn, và khi bị dồn vào chân tường, nó sẵn sàng bắn phăng toàn bộ ruột gan của mình ra ngoài để trói gô kẻ thù! Hôm nay, phòng khám của chúng ta sẽ mổ xẻ bốn hạng mục kỳ dị nhất của Quái Kiệt Ruột Mềm này!
```

### scene02 — CƠ THỂ TỰ CHUYỂN TỪ CỨNG NHƯ ĐÁ SANG LỎNG NHƯ NƯỚC
*Thẻ chương:* TỰ HÓA LỎNG CHUI QUA KHE ĐÁ VÀ CỨNG LẠI TRONG 1 GIÂY

*Badge:* `CHỤP CẮT LỚP` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene02_p0.wav` (365 ký tự) · mood `hao_hung`

```text
Hạng mục khám đầu tiên: Chụp cắt lớp mô da và kiểm tra độ đàn hồi! Bình thường khi một con cua biển hay tôm hùm đói bụng mò tới định cắn thử, Quái Kiệt Ruột Mềm sẽ lập tức gồng cơ thể lên: toàn bộ lớp da dày sần sùi của nó đột ngột cứng ngắc lại như một khúc gỗ hóa thạch, khiến chiếc càng cua kẹp vào chỉ nghe tiếng cộp cộp trượt ra ngoài mà không thể xuyên thủng!
```
**Part 1** → `audio/vs/scene02_p1.wav` (332 ký tự) · mood `don_dap`

```text
Nhưng điều làm toàn bộ hội đồng y bác sĩ phải trợn tròn mắt là hiện tượng diễn ra ngay sau đó! Nếu kẻ săn mồi cố tìm cách lôi nó ra khỏi hang hốc, cơ thể nó chỉ mất đúng một giây để kích hoạt phản xạ thần kinh đặc biệt: toàn bộ lớp thịt cứng như đá bỗng nhiên mềm nhũn ra, chảy nhão như một khối thạch rau câu ấm nóng! [surprise-wa]
```
**Part 2** → `audio/vs/scene02_p2.wav` (348 ký tự) · mood `don_dap`

```text
Nhờ trạng thái nhão nhớt tự hóa lỏng này, Hải Sâm có thể nhẹ nhàng luồn lách thân mình trượt qua những khe nứt đá ngầm hẹp chỉ bằng một nửa đường kính cơ thể nó! Vừa chui tọt vào bên trong khe đá an toàn xong, nó lại phóng điện hóa học và... cứng ngắc trở lại, chèn chặt vào vách đá khiến không có bất kỳ móng vuốt nào lôi nó ra được! [surprise-oh]
```
**Part 3** → `audio/vs/scene02_p3.wav` (517 ký tự) · mood `hao_hung`

```text
Bí mật đằng sau khả năng biến hình như người lỏng kẻ hủy diệt này là gì? Các nhà cơ sinh học phát hiện da của Hải Sâm được cấu tạo từ một loại vật liệu siêu đẳng mang tên mô liên kết biến tính, chủ yếu là các sợi cô-la-gen đan cài vào nhau. Nhưng thay vì dùng cơ bắp để co bóp, nó điều khiển các phân tử protein chuyên dụng như Ten-xi-lin và nồng độ ion canxi để chủ động khóa cứng hoặc tháo rời các liên kết sợi này trong chớp mắt! [laughter] Muốn cứng là cứng, muốn mềm là mềm, không tốn lấy một giọt calo vận động!
```
**Part 4** → `audio/vs/scene02_p4.wav` (652 ký tự) · mood `hao_hung`

```text
Để chứng minh điều kỳ diệu này, các nhà nghiên cứu từng làm một thí nghiệm trong phòng lab: khi ngâm một mẩu mô da của Hải Sâm vào dung dịch nước biển nhân tạo đã rút sạch ion canxi, toàn bộ cấu trúc da rã rời ra như một bát súp nhầy nhụa! Nhưng chỉ cần nhỏ vài giọt dung dịch canxi vào, các sợi cô-la-gen lập tức liên kết chéo trở lại, biến bát súp lỏng bỏng thành một khối thạch cứng đanh như gạch nung chỉ sau vài chục giây! [surprise-oh] Giới kỹ sư vật liệu sinh học hiện đại đang điên cuồng học hỏi cơ chế này để chế tạo áo giáp chống đạn thông minh: bình thường mặc mềm mại như áo phông, nhưng khi bị đạn bắn vào sẽ lập tức hóa cứng như thép tấm!
```

### scene03 — CÂY HÔ HẤP KỲ LẠ VÀ KHÁCH TRỌ CÁ NGỌC CHUI VÀO
*Thẻ chương:* THỞ BẰNG HẬU MÔN VÀ KHÁCH SẠN MIỄN PHÍ CHO CÁ NGỌC

*Badge:* `NỘI SOI HẬU MÔN` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene03_p0.wav` (272 ký tự) · mood `nghiem_trang_gia`

```text
Chuyển sang hạng mục khám thứ hai: Nội soi hệ hô hấp và kiểm tra khách trọ bất đắc dĩ! Nếu bạn hỏi Hải Sâm dùng mũi hay miệng để hít thở dưỡng khí, thì bác sĩ chúng tôi xin trả lời thẳng thắn: nó dùng đúng chiếc lỗ hậu môn để thở suốt hai mươi bốn giờ mỗi ngày! [laughter]
```
**Part 1** → `audio/vs/scene03_p1.wav` (388 ký tự) · mood `hao_hung`

```text
Bên trong khoang sau của Quái Kiệt Ruột Mềm gắn liền với một hệ thống ống phân nhánh chằng chịt như hai cành cây san hô gọi là cây hô hấp. Cứ đều đặn ba đến bốn lần mỗi phút, chiếc lỗ hậu môn phía sau sẽ mở to ra, hút đầy nước biển giàu oxy vào trong hai nhánh cây hô hấp để trao đổi khí, rồi lại co bóp tống dòng nước cũ ra ngoài! Đối với Hải Sâm, thở và bài tiết dùng chung một cửa ngõ!
```
**Part 2** → `audio/vs/scene03_p2.wav` (124 ký tự) · 🎭 cameo `co_tro_ly`

```text
Bác sĩ ơi, trong lúc đặt ống nội soi vào hậu môn bệnh nhân, em phát hiện có một cái đuôi cá đang ngọ nguậy thò ra thò vào ạ!
```
**Part 3** → `audio/vs/scene03_p3.wav` (374 ký tự) · mood `hao_hung`

```text
[surprise-oh] Đúng rồi đấy trợ lý ơi, đây là vụ việc trớ trêu và hài hước bậc nhất đại dương! [laughter] Lợi dụng chiếc cửa hậu môn mở ra đóng vào đều đặn để thở của Hải Sâm, một loài cá nhỏ nhắn trơn trượt tên là Cá Ngọc Ca-ra-pút đã nảy ra một ý tưởng sinh tồn siêu lười: nó bơi ngược dòng nước, dùng chiếc đầu nhọn hoặc đuôi trườn thẳng vào trong cơ thể Hải Sâm để ở nhờ!
```
**Part 4** → `audio/vs/scene03_p4.wav` (104 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Chào bác sĩ, em thuê phòng khách sạn ở đây mát mẻ an toàn lắm, kẻ thù bên ngoài không dám vào tìm đâu ạ!
```
**Part 5** → `audio/vs/scene03_p5.wav` (504 ký tự) · mood `bi_hai`

```text
Chú cá ngọc coi lòng mề Hải Sâm như một căn hộ chung cư cao cấp hoàn toàn miễn phí! Ban ngày trốn kỹ bên trong nội tạng của gia chủ để ngủ, ban đêm mới thò đầu ra ngoài đi săn mồi. Tệ hơn nữa, đôi khi đói bụng quá, chú cá này còn tiện mồm gặm nhấm luôn một phần tuyến sinh dục hoặc mô ruột của Hải Sâm để ăn lót dạ! Nhưng Quái Kiệt Ruột Mềm của chúng ta thì vẫn thản nhiên thở phì phò, vì chút mô bị cắn mất sẽ tự mọc lại nhanh như thổi! Đúng là lòng vị tha đến mức bác sĩ cũng phải chào thua! [laughter]
```
**Part 6** → `audio/vs/scene03_p6.wav` (526 ký tự) · mood `hao_hung`

```text
Các nhà sinh vật học biển từng ghi nhận một kỷ lục không tưởng khiến ai nấy đều phải ôm bụng cười: bên trong khoang cơ thể của một chú Hải Sâm dài bốn mươi xăng-ti-mét, người ta phát hiện có tới mười lăm con cá ngọc lớn nhỏ đang chen chúc nằm ngủ cùng một lúc! [surprise-wa] Chiếc lỗ hậu môn của Quái Kiệt Ruột Mềm bỗng chốc biến thành trạm xe buýt giờ cao điểm! Chưa hết, đôi khi cả những chú cua hạt đậu bé xíu cũng mò vào chiếm dụng không gian, biến cơ thể nó thành một khu bảo tồn sinh thái ngầm nhộn nhịp nhất rạn san hô!
```

### scene04 — PHÓNG BÚI ỐNG CUVIER NHƯ PHÁO HOA SỢI MÌ
*Thẻ chương:* BẮN BÙI TƠ BẠCH DÃN DÀI 20 LẦN DÍNH CHẶT KẺ THÙ

*Badge:* `GIÁM ĐỊNH VŨ KHÍ` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene04_p0.wav` (294 ký tự) · mood `tram_bi_an`

```text
Hạng mục khám thứ ba: Thử nghiệm vũ khí phòng vệ chủ động! Giả sử một con cá mập nhỏ hoặc một chú cua biển bạo lực vẫn quyết tâm không buông tha, dồn Hải Sâm vào thế ngàn cân treo sợi tóc. Không có chân để chạy trốn, không có hàm răng để cắn trả, chú Quái Kiệt Ruột Mềm sẽ làm gì? [question-oh]
```
**Part 1** → `audio/vs/scene04_p1.wav` (232 ký tự) · mood `don_dap`

```text
Nó lập tức quay đuôi lại phía kẻ thù, gồng mạnh cơ thành bụng và... bùm! Một loạt búi sợi màu trắng xóa mang tên ống Cu-vi-ê bắn tung tóe qua đường hậu môn phóng thẳng vào mặt đối thủ như một màn pháo hoa mì Ý kinh dị! [surprise-wa]
```
**Part 2** → `audio/vs/scene04_p2.wav` (406 ký tự) · mood `don_dap`

```text
Ngay khoảnh khắc chạm vào nước biển và cơ thể kẻ săn mồi, những ống Cu-vi-ê này lập tức dãn dài ra gấp hai mươi lần kích thước ban đầu! Đồng thời, lớp màng ngoài vỡ tung, giải phóng một loại chất keo sinh học siêu dính bám chặt vào vảy cá, mai cua và mắt mũi của kẻ địch! Kẻ tấn công càng giãy giụa hoảng loạn thì những sợi tơ dính càng quấn chặt như mạng nhện khổng lồ, khóa cứng hoàn toàn cử động của nó!
```
**Part 3** → `audio/vs/scene04_p3.wav` (350 ký tự) · mood `hao_hung`

```text
Chưa dừng lại ở đó, trong những sợi tơ phóng ra còn chứa hợp chất độc tố Hô-lô-thu-rin cực mạnh. Độc tố này làm tê liệt hệ thần kinh của các loài cá nhỏ, gây cảm giác bỏng rát cay xè mắt của kẻ săn mồi lớn! Trong lúc đối thủ đang bận quằn quại gỡ mớ mì tơ siêu dính ra khỏi mặt, Hải Sâm của chúng ta đã nhẹ nhàng trườn đi mất tăm mất tích! [laughter]
```
**Part 4** → `audio/vs/scene04_p4.wav` (537 ký tự) · mood `hao_hung`

```text
Độ dai dính kinh dị của ống Cu-vi-ê đã được người dân bản địa ở các hòn đảo Thái Bình Dương như Mi-crô-nê-xi-a khai thác từ thời xa xưa! Ngư dân đi biển khi chẳng may bị đá san hô cứa rách chân đã dùng chính những búi tơ trắng này để băng bó vết thương như một loại băng gạc cầm máu tự nhiên. Thậm chí trong trường hợp khẩn cấp, họ còn quấn những búi tơ keo này quanh lòng bàn chân để tạo thành một lớp đế giày bảo hộ siêu bền, giúp họ bước đi thoải mái trên những rạn san hô lởm chởm sắc như dao cạo mà không hề bị trầy xước! [laughter]
```

### scene05 — PHUN SẠCH RUỘT GAN VÀ CỖ MÁY LỌC SẠCH ĐÁY BIỂN
*Thẻ chương:* BẮN TOÀN BỘ RUỘT GAN VÀ TÁI TẠO NGUYÊN VẸN TRONG 35 NGÀY

*Badge:* `TỰ TỐNG NỘI TẠNG` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene05_p0.wav` (233 ký tự) · mood `don_dap`

```text
Hạng mục khám thứ tư: Pha thoát xác rùng rợn và vai trò sinh thái vĩ đại! Nhưng nếu ngay cả chiêu bắn ống Cu-vi-ê vẫn chưa đủ để dọa kẻ thù, Hải Sâm sẽ tung ra đòn hy sinh cuối cùng mang tên hiện tượng tự tống nội tạng! [surprise-oh]
```
**Part 1** → `audio/vs/scene05_p1.wav` (425 ký tự) · mood `bi_hai`

```text
Nó tự bẻ gãy các dây chằng nội tạng bên trong, tự làm rách thành hậu môn, và... nôn mửa tống thẳng toàn bộ dạ dày, đường ruột và các cơ quan nội tạng còn lại bắn ra ngoài biển! Kẻ săn mồi nhìn thấy đống thức ăn tươi sống béo ngậy trước mắt liền dừng lại chén no nê, hoàn toàn quên mất cái xác Hải Sâm rỗng tuếch vừa lủi trốn vào góc khuất! Đúng là kế kim thiền thoát xác phiên bản rùng mình nhất thế giới tự nhiên! [laughter]
```
**Part 2** → `audio/vs/scene05_p2.wav` (370 ký tự) · mood `hao_hung`

```text
Mất sạch toàn bộ ruột gan, liệu bệnh nhân này có chết không? Các nghiên cứu sinh học tế bào khẳng định: Hoàn toàn không! Chỉ sau ba mươi lăm ngày, tức là khoảng năm tuần ngắn ngủi, từ các mô mầm còn sót lại, Hải Sâm tự phân chia tế bào và tái tạo lại nguyên vẹn một trăm phần trăm toàn bộ hệ tiêu hóa mới toanh: từ miệng, dạ dày, ruột non cho đến ống hậu môn hoàn chỉnh!
```
**Part 3** → `audio/vs/scene05_p3.wav` (516 ký tự) · mood `am_ap`

```text
Và khi đã mọc lại đường ruột, Quái Kiệt Ruột Mềm lập tức quay trở lại công việc vĩ đại nhất của nó: làm sạch đại dương! Mỗi ngày, một chú Hải Sâm cần mẫn nuốt hàng trăm gam bùn cát dưới đáy biển, tiêu hóa sạch sẽ mọi vụn thức ăn hữu cơ thừa thãi và vi khuẩn thối rữa, rồi thải ra những hạt cát sạch tinh khiết. Mỗi năm, một cá thể có thể lọc sạch tới hơn năm mươi ki-lô-gam cát! [surprise-oh] Thậm chí phân của nó còn giàu canxi cacbonat giúp giảm độ axit của nước biển, bảo vệ các rạn san hô khỏi nguy cơ tẩy trắng!
```
**Part 4** → `audio/vs/scene05_p4.wav` (422 ký tự) · mood `am_ap`

```text
Trong các thí nghiệm sinh học phân tử, khi kiểm tra các mẫu nước nuôi trồng thủy sản bị ô nhiễm nặng đầy chất thải hữu cơ, người ta chỉ cần thả vào bể vài cá thể Hải Sâm. Sau đúng hai mươi bốn giờ cần mẫn cày xới, toàn bộ cặn bã ô nhiễm dưới đáy bể đã được lọc sạch bóng, nước trong vắt trở lại như nước suối nguồn! Chúng chính là những chiếc máy hút bụi cần cù và vĩ đại nhất bảo vệ sự sống còn của toàn bộ đáy đại dương!
```

### scene06 — ĐƠN THUỐC BẤT LỰC VÀ BÓNG ĐEN CỖ MÁY TẠO ĐỜM
*Thẻ chương:* ĐƠN THUỐC CHO BỆNH NHÂN KHÔNG Não VÀ BÓNG ĐEN TẠO ĐỜM

*Badge:* `KẾT LUẬN Y KHOA` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene06_p0.wav` (303 ký tự) · mood `am_ap`

```text
Tổng kết bệnh án số hai mươi ba. Từ một khối thịt mềm oặt không não, không mắt, không xương sống, Hải Sâm đã biến những điểm yếu tưởng chừng tuyệt vọng thành một bộ giáp sinh tồn đỉnh cao: tự hóa lỏng da như thạch, thở bằng hậu môn, cưu mang cá ngọc, và sẵn sàng hy sinh cả bộ ruột để giữ lấy mạng sống!
```
**Part 1** → `audio/vs/scene06_p1.wav` (222 ký tự) · mood `hao_hung`

```text
Kê đơn xuất viện: Cho bệnh nhân về lại đáy cát biển sâu, tiếp tục cày xới làm sạch đại dương và tuyệt đối nhắc nhở khách trọ cá ngọc... đừng có cắn trộm ruột chủ nhà nữa nhé! Ký tên: bác sĩ đã hoàn toàn bất lực! [laughter]
```
**Part 2** → `audio/vs/scene06_p2.wav` (234 ký tự) · mood `hao_hung`

```text
Còn các đồng nghiệp thì sao? Nếu được sở hữu một trong hai năng lực của Quái Kiệt Ruột Mềm: tự hóa lỏng cơ thể để lách qua khe hẹp, hay bắn mạng tơ keo siêu dính trói gô kẻ bắt nạt, bạn chọn cái nào? Hãy để lại bình luận bên dưới nhé!
```
**Part 3** → `audio/vs/scene06_p3.wav` (563 ký tự) · mood `am_ap`

```text
Hồ sơ bệnh án phòng khám hôm nay xin tạm gác lại. Nhưng tập sau, chúng ta sẽ quay trở lại phòng thí nghiệm năm cấp độ để đối đầu với một cỗ máy kinh dị đáy biển còn đáng sợ hơn nữa! Một sinh vật cổ đại trơn tuột như lươn, không có hàm, không có xương sống, nhưng khi bị cá mập cắn vào, nó có thể biến hai mươi lít nước biển xung quanh thành một khối keo nhớt đặc quánh chỉ trong đúng một giây làm nghẹt thở kẻ thù, rồi tự thắt nút cơ thể như một ảo thuật gia để tẩu thoát! Đố các bạn biết bóng đen bí ẩn kỳ sau là loài vật nào? Hãy đoán ngay ở phần bình luận nhé!
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Khi bị kẻ săn mồi dồn vào chân tường, loài vật này không chạy trốn, mà chọn cách... bắn thẳng toàn bộ ruột gan của mình qua đường hậu môn để tẩu thoát! [laughter] Xin giới thiệu Hải Sâm, sinh vật hình chiếc xúc xích dài ba mươi xăng-ti-mét sống dưới đáy biển sâu. Cơ thể nó không hề có não, không có mắt, không có tim, và thở bằng cách bơm nước vào ra chiếc lỗ hậu môn! [surprise-wa] Da của nó làm từ mô liên kết đặc biệt, có thể tự chuyển từ cứng ngắc như đá sang mềm nhão như thạch chỉ trong một giây để chui lọt qua khe đá hẹp! Khi bị tấn công, nó bắn ra những ống tơ trắng dãn dài gấp hai mươi lần dính chặt cứng lấy kẻ thù. Nếu vẫn chưa thoát, nó sẵn sàng nôn sạch toàn bộ đường ruột ra ngoài để kẻ địch mải ăn, rồi lủi trốn và tự mọc lại nguyên vẹn bộ ruột mới chỉ sau năm tuần! Một quái kiệt đáy biển vừa biết hóa lỏng, vừa thở bằng hậu môn, đúng là phép màu sinh học điên rồ nhất đại dương!
```

**Whisper prompt:** `Hải Sâm, Quái Kiệt Ruột Mềm, Holothuroidea, da gai, mô liên kết collagen, tensilin, ống Cuvier, Cuvierian, cá ngọc, Carapus, evisceration, cây hô hấp, canxi cacbonat, 20 lần, 35 ngày, 5 tuần, 1 giây, 50kg, 100%`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| hai mươi ba | 23 |
| hai mươi bốn | 24 |
| hai mươi bốn giờ | 24 giờ |
| bốn mươi xăng-ti-mét | 40cm |
| hai mươi lần | 20 lần |
| ba mươi lăm ngày | 35 ngày |
| mười lăm con | 15 con |
| bốn đến năm tuần | 4-5 tuần |
| năm tuần | 5 tuần |
| bốn tuần | 4 tuần |
| ba đến bốn lần | 3-4 lần |
| ba mươi xăng-ti-mét | 30cm |
| năm mươi ki-lô-gam | 50kg |
| hàng chục ki-lô-gam | hàng chục kg |
| năm trăm gam | 500g |
| hàng trăm gam | hàng trăm g |
| một trăm phần trăm | 100% |
| bốn hạng mục | 4 hạng mục |
| một giây | 1 giây |
| hai mươi | 20 |
| năm ngàn | 5.000 |
| hàng triệu | hàng triệu |
| hàng trăm | hàng trăm |
| năm cấp độ | 5 cấp độ |
| Cô-la-gen | Collagen |
| cô-la-gen | collagen |
| Ten-xi-lin | Tensilin |
| Cu-vi-ê | Cuvier |
| Hô-lô-thu-rin | Holothurin |
| Ca-ra-pút | Carapus |
| Mi-crô-nê-xi-a | Micronesia |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · CA CẤP CỨU SINH VẬT KHÔNG NÃO, KHÔNG MẮT, KHÔNG TIM · 77.1s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.9 (7.9s) | L01 | Phòng cấp cứu y khoa dã thiết lập tại trạm nghiên cứu đáy biển sâu. Chuông báo động vang lên hồi còi gấp rút, đèn mổ bật sáng trên khay kim loại khử trùng. |  | Trạm nghiên cứu y khoa dã chiến dựng dưới đáy biển sâu với các vòm kính nhìn ra rạn san hô, đèn mổ bật sáng trên bàn khám kim loại. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này. |
| b02 | 00:07.9–00:16.3 (8.4s) | L02 | Bệnh nhân số 23 tự trườn vào phòng khám với dáng vẻ chậm rãi kỳ quặc đến mức không tưởng: một cục thịt dài ngoằng màu nâu đốm vàng, mềm oặt như chiếc xúc xích bị bỏ quên dưới đáy cát... |  | chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán lững thững trườn chậm rãi vào phòng khám, thân hình dài ngoằng màu nâu đốm vàng mềm oặt như chiếc xúc xích khổng lồ bò trên nền cát. |
| b03 | 00:16.3–00:22.5 (6.2s) | L03 | Không có hộp sọ. Không có bộ não. Không có lấy một đôi mắt. Và thậm chí không có cả một trái tim để đập bơm máu! |  | Ba ô đồ họa chẩn đoán gạch chéo đỏ: hình hộp sọ bị gạch chéo, hình bộ não bị gạch chéo, hình đôi mắt và trái tim bị gạch chéo đỏ; dấu chấm hỏi to ở giữa. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này. |
| b04 | 00:22.5–00:30.8 (8.4s) | L04 | Bác sĩ ơi, em đo nhịp tim mãi mà máy cứ kêu tút tút bằng phẳng, bệnh nhân này thực sự là một sinh vật sống hay là một khúc chả lụa dưới biển vậy ạ? |  | BÊN TRÁI cô trợ lý phòng khám hoạt hình mặc áo blouse xanh nhạt cầm ống nghe y tế áp vào người chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán, màn hình máy đo điện tim bên cạnh chỉ là một đường thẳng tắp kêu tút tút kéo  |
| b05 | 00:30.8–00:36.4 (5.5s) | L05 | Trợ lý bình tĩnh, bệnh nhân vẫn đang sống nhăn răng... à quên, nó còn chẳng thèm có răng nữa cơ! |  | ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế đứng bên cạnh cười toe toét giơ ngón tay giải thích; chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán nằm trên bàn khám há miệng tròn x |
| b06 | 00:36.4–00:43.7 (7.4s) | L06 | Xin giới thiệu với các đồng nghiệp: đây là Hải Sâm, sinh vật da gai thuộc lớp Động vật chân gai, họ hàng xa với sao biển và cầu gai. |  | Cây phả hệ sinh vật biển da gai: chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán đứng giữa cùng họ hàng sao biển màu cam và cầu gai nhiều gai nhọn dưới đáy đại dương. |
| b07 | 00:43.7–00:46.5 (2.8s) | L07 | Kích thước trung bình dài khoảng 20 đến 30cm. | **20-30 CM** · chiều dài cơ thể · R/350 · [0.65, 0.5] | Ở GIỮA chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán nằm thẳng cạnh chiếc thước đo chiều cao màu vàng 30cm của phòng khám để đối chiếu kích thước. |
| b08 | 00:46.5–00:55.1 (8.5s) | L08 | Nhìn bề ngoài thì lù đù ngây ngô như khúc dưa chuột biển vô hại, nhưng trong giới sinh học biển, chúng tôi gọi thẳng tên nó bằng biệt danh: Quái Kiệt Ruột Mềm! |  | Chia đôi: BÊN TRÁI một quả dưa chuột xanh ngắt đặt trên thớt gỗ; BÊN PHẢI chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán khoác áo choàng bệnh nhân giơ dải băng danh hiệu Quái Kiệt Ruột Mềm. |
| b09 | 00:55.1–01:03.9 (8.8s) | L09 | Đừng để vẻ ngoài vô tri đó đánh lừa! Dù bị tước đoạt hầu hết các cơ quan nội tạng tiêu chuẩn của động vật có xương sống, Hải Sâm lại sở hữu những siêu năng lực tự vệ quái đản bậc nhất hành tinh: |  | chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán tạo dáng siêu anh hùng nhưng cơ thể mềm oặt như cục bột, các nốt sần gai mềm rung rinh ngộ nghĩnh. |
| b10 | 01:03.9–01:12.6 (8.7s) | L10 | cơ thể tự hóa lỏng thành thạch nhớt trong tích tắc, thở trực tiếp bằng đường... hậu môn, và khi bị dồn vào chân tường, nó sẵn sàng bắn phăng toàn bộ ruột gan của mình ra ngoài để trói gô kẻ thù! |  | Ba ô đồ họa năng lực tự vệ kỳ dị: ô một hóa lỏng như thạch, ô hai thở bằng hậu môn, ô ba bắn ruột qua đuôi; dấu chấm than đỏ rực. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này. |
| b11 | 01:12.6–01:17.1 (4.6s) | L11 | Hôm nay, phòng khám của chúng ta sẽ mổ xẻ 4 hạng mục kỳ dị nhất của Quái Kiệt Ruột Mềm này! |  | ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế bật chiếc đèn mổ công suất lớn soi thẳng vào chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán đang nằm thư thái trên bàn mổ, xung quanh |

### scene02 · CƠ THỂ TỰ CHUYỂN TỪ CỨNG NHƯ ĐÁ SANG LỎNG NHƯ NƯỚC · 111.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:04.4 (4.4s) | L12 | Hạng mục khám đầu tiên: Chụp cắt lớp mô da và kiểm tra độ đàn hồi! |  | Bảng điện tử phòng khám hiện HẠNG MỤC 1: CHỤP CẮT LỚP MÔ DA; ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế đeo găng tay cao su chuẩn bị kiểm tra độ đàn hồi. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này. |
| b02 | 00:04.4–00:14.8 (10.3s) | L13 | Bình thường khi một con cua biển hay tôm hùm đói bụng mò tới định cắn thử, Quái Kiệt Ruột Mềm sẽ lập tức gồng cơ thể lên: toàn bộ lớp da dày sần sùi của nó đột ngột cứng ngắc lại như một khúc gỗ hóa thạch, |  | Một con cua biển hung dữ giơ chiếc càng to kẹp mạnh vào lưng chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán, cơ thể chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng |
| b03 | 00:14.8–00:19.2 (4.5s) | L14 | khiến chiếc càng cua kẹp vào chỉ nghe tiếng cộp cộp trượt ra ngoài mà không thể xuyên thủng! |  | Chiếc càng cua biển kẹp vào lưng chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán bị trượt cộp cộp văng ra ngoài, không thể xuyên thủng lớp da sần sùi cứng đanh. |
| b04 | 00:19.2–00:23.9 (4.6s) | L15 | Nhưng điều làm toàn bộ hội đồng y bác sĩ phải trợn tròn mắt là hiện tượng diễn ra ngay sau đó! |  | ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế và cô trợ lý phòng khám hoạt hình mặc áo blouse xanh nhạt trợn tròn mắt kinh ngạc nhìn vào màn hình máy quét: hiện tượng biến đổi vật lý kỳ lạ bắt đầu diễn ra. |
| b05 | 00:23.9–00:29.3 (5.4s) | L16 | Nếu kẻ săn mồi cố tìm cách lôi nó ra khỏi hang hốc, cơ thể nó chỉ mất đúng 1 giây để kích hoạt phản xạ thần kinh đặc biệt: | **1 GIÂY** · hóa lỏng như thạch · R/350 · [0.62, 0.48] | Đồng hồ cát điện tử đếm 1 giây: chỉ trong 1 giây, phản xạ thần kinh đặc biệt kích hoạt làm thay đổi hoàn toàn cấu trúc cơ thể. |
| b06 | 00:29.3–00:34.8 (5.5s) | L17 | toàn bộ lớp thịt cứng như đá bỗng nhiên mềm nhũn ra, chảy nhão như một khối thạch rau câu ấm nóng! |  | Thân hình của chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán mềm mại uyển chuyển như đĩa thạch rau câu ngọt ngào đặt trên khay phòng lab. |
| b07 | 00:34.8–00:42.6 (7.8s) | L18 | Nhờ trạng thái nhão nhớt tự hóa lỏng này, Hải Sâm có thể nhẹ nhàng luồn lách thân mình trượt qua những khe nứt đá ngầm hẹp chỉ bằng một nửa đường kính cơ thể nó! |  | chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán ở trạng thái nhão nhớt tự hóa lỏng, nhẹ nhàng trườn cơ thể luồn lách qua một khe nứt đá ngầm hẹp chỉ bằng một nửa thân mình một cách êm ru. |
| b08 | 00:42.6–00:51.1 (8.6s) | L19 | Vừa chui tọt vào bên trong khe đá an toàn xong, nó lại phóng điện hóa học và... cứng ngắc trở lại, chèn chặt vào vách đá khiến không có bất kỳ móng vuốt nào lôi nó ra được! |  | Bên trong khe đá ngầm, chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán đột ngột đông cứng trở lại như tảng đá chèn chặt vào vách nứt; bên ngoài con cua biển thò càng vào lôi mãi không ra. |
| b09 | 00:51.1–01:03.0 (11.9s) | L20 | Bí mật đằng sau khả năng biến hình như người lỏng kẻ hủy diệt này là gì? Các nhà cơ sinh học phát hiện da của Hải Sâm được cấu tạo từ một loại vật liệu siêu đẳng mang tên mô liên kết biến tính, chủ yếu là các sợi collagen đan cài vào nhau. |  | Sơ đồ hiển vi phân tử da Hải Sâm: các sợi collagen đan cài vào nhau như lưới thép, protein Tensilin và các ion canxi phát sáng màu xanh điều hòa liên kết. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này. |
| b10 | 01:03.0–01:13.5 (10.5s) | L21 | Nhưng thay vì dùng cơ bắp để co bóp, nó điều khiển các phân tử protein chuyên dụng như Tensilin và nồng độ ion canxi để chủ động khóa cứng hoặc tháo rời các liên kết sợi này trong chớp mắt! |  | Mô hình protein Tensilin hoạt động như công tắc mở đóng các chốt khóa giữa các sợi collagen mà không tốn một chút năng lượng cơ bắp nào. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này. |
| b11 | 01:13.5–01:18.0 (4.4s) | L22 | Muốn cứng là cứng, muốn mềm là mềm, không tốn lấy một giọt calo vận động! |  | chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán chuyển đổi hai nửa thân mình: nửa bên trái cứng như đá tảng gõ keng keng, nửa bên phải mềm nhèo như thạch chảy, mặt cười tít mắt không tốn calo. |
| b12 | 01:18.0–01:30.4 (12.4s) | L23 | Để chứng minh điều kỳ diệu này, các nhà nghiên cứu từng làm một thí nghiệm trong phòng lab: khi ngâm một mẩu mô da của Hải Sâm vào dung dịch nước biển nhân tạo đã rút sạch ion canxi, toàn bộ cấu trúc da rã rời ra như một bát súp nhầy nhụa! |  | Trong phòng lab: một mẩu mô da hải sâm ngâm trong cốc thủy tinh nước biển nhân tạo rút sạch canxi bị rã rời ra như một bát súp nhầy nhụa lỏng bỏng. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này. |
| b13 | 01:30.4–01:41.0 (10.6s) | L24 | Nhưng chỉ cần nhỏ vài giọt dung dịch canxi vào, các sợi collagen lập tức liên kết chéo trở lại, biến bát súp lỏng bỏng thành một khối thạch cứng đanh như gạch nung chỉ sau vài chục giây! |  | Ống nhỏ giọt nhỏ vài giọt dung dịch canxi vào cốc, bát súp lỏng lập tức liên kết chéo đông cứng đanh lại thành khối thạch rắn rỏi như gạch nung. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này. |
| b14 | 01:41.0–01:51.9 (10.9s) | L25 | Giới kỹ sư vật liệu sinh học hiện đại đang điên cuồng học hỏi cơ chế này để chế tạo áo giáp chống đạn thông minh: bình thường mặc mềm mại như áo phông, nhưng khi bị đạn bắn vào sẽ lập tức hóa cứng như thép tấm! |  | Mô hình áo giáp chống đạn tương lai thông minh: bình thường mềm mại như chiếc áo phông co giãn, khi bị viên đạn chạm vào lập tức hóa cứng thành tấm thép. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này. |

### scene03 · CÂY HÔ HẤP KỲ LẠ VÀ KHÁCH TRỌ CÁ NGỌC CHUI VÀO · 116.6s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.2 (9.2s) | L26 | Chuyển sang hạng mục khám thứ hai: Nội soi hệ hô hấp và kiểm tra khách trọ bất đắc dĩ! Nếu bạn hỏi Hải Sâm dùng mũi hay miệng để hít thở dưỡng khí, thì bác sĩ chúng tôi xin trả lời thẳng thắn: |  | Bảng điện tử chuyển sang HẠNG MỤC 2: NỘI SOI HỆ HÔ HẤP; ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế cầm ống nội soi mềm chỉ về phía chiếc lỗ hậu môn của chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ  |
| b02 | 00:09.2–00:12.8 (3.6s) | L27 | nó dùng đúng chiếc lỗ hậu môn để thở suốt 24 giờ mỗi ngày! |  | Cận cảnh chiếc lỗ hậu môn phía sau của chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán co bóp thở phì phò, bên cạnh đồng hồ 24 giờ quay đều liên tục. |
| b03 | 00:12.8–00:19.5 (6.7s) | L28 | Bên trong khoang sau của Quái Kiệt Ruột Mềm gắn liền với một hệ thống ống phân nhánh chằng chịt như hai cành cây san hô gọi là cây hô hấp. |  | Mặt cắt giải phẫu bên trong cơ thể chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán: gắn liền với lỗ hậu môn là hai nhánh ống cây hô hấp phân nhánh chằng chịt rực rỡ như cành san hô đỏ. |
| b04 | 00:19.5–00:27.4 (7.9s) | L29 | Cứ đều đặn 3-4 lần mỗi phút, chiếc lỗ hậu môn phía sau sẽ mở to ra, hút đầy nước biển giàu oxy vào trong hai nhánh cây hô hấp để trao đổi khí, | **3-4 LẦN/P** · thở bằng hậu môn · R/350 · [0.65, 0.5] | Chiếc lỗ hậu môn phía sau của chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán mở to ra hút dòng nước biển giàu oxy xanh mát vào trong hai cây hô hấp để trao đổi dưỡng khí. |
| b05 | 00:27.4–00:33.0 (5.6s) | L30 | rồi lại co bóp tống dòng nước cũ ra ngoài! Đối với Hải Sâm, thở và bài tiết dùng chung một cửa ngõ! |  | Hậu môn co bóp tống dòng nước cũ ra ngoài thành dòng bong bóng khí; chiếc biển báo ghi dòng chữ: Thở và bài tiết dùng chung một cửa ngõ. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này. |
| b06 | 00:33.0–00:39.4 (6.4s) | L31 | Bác sĩ ơi, trong lúc đặt ống nội soi vào hậu môn bệnh nhân, em phát hiện có một cái đuôi cá đang ngọ nguậy thò ra thò vào ạ! |  | cô trợ lý phòng khám hoạt hình mặc áo blouse xanh nhạt giật nảy mình chỉ vào màn hình nội soi: từ lỗ hậu môn của chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán đang có một chiếc đuôi cá nhỏ nhắn ngọ nguậy thò ra thụt vào |
| b07 | 00:39.4–00:48.3 (8.9s) | L32 | Đúng rồi đấy trợ lý ơi, đây là vụ việc trớ trêu và hài hước bậc nhất đại dương! Lợi dụng chiếc cửa hậu môn mở ra đóng vào đều đặn để thở của Hải Sâm, |  | ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế bật cười vỗ trán chỉ lên màn hình: vụ việc trớ trêu và hài hước bậc nhất đại dương giữa hải sâm và chú cá ngọc. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này. |
| b08 | 00:48.3–00:58.8 (10.5s) | L33 | một loài cá nhỏ nhắn trơn trượt tên là Cá Ngọc Carapus đã nảy ra một ý tưởng sinh tồn siêu lười: nó bơi ngược dòng nước, dùng chiếc đầu nhọn hoặc đuôi trườn thẳng vào trong cơ thể Hải Sâm để ở nhờ! |  | Chú cá ngọc nhỏ màu bạc bơi lượn quanh chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán đang nằm thư thái trên cát biển, chuẩn bị tìm chỗ trú ẩn kết bạn (phong cách hoạt hình trẻ em đáng yêu). |
| b09 | 00:58.8–01:04.9 (6.1s) | L34 | Chào bác sĩ, em thuê phòng khách sạn ở đây mát mẻ an toàn lắm, kẻ thù bên ngoài không dám vào tìm đâu ạ! |  | chú cá ngọc nhỏ nhắn màu bạc trong suốt trơn tuột với nụ cười láu cá tinh nghịch nằm cuộn tròn mát mẻ trong khoang ruột của chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán, thò mỗi cái đầu ra cửa vẫy vẫy tay chào bác sĩ n |
| b10 | 01:04.9–01:13.8 (8.9s) | L35 | Chú cá ngọc coi lòng mề Hải Sâm như một căn hộ chung cư cao cấp hoàn toàn miễn phí! Ban ngày trốn kỹ bên trong nội tạng của gia chủ để ngủ, ban đêm mới thò đầu ra ngoài đi săn mồi. |  | Minh họa hài hước: cơ thể chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán biến thành tòa chung cư mini có bảng hiệu Khách Sạn Miễn Phí, cá ngọc ban ngày ngủ khò khò, ban đêm bơi ra đi chơi. |
| b11 | 01:13.8–01:20.2 (6.3s) | L36 | Tệ hơn nữa, đôi khi đói bụng quá, chú cá này còn tiện mồm gặm nhấm luôn một phần tuyến sinh dục hoặc mô ruột của Hải Sâm để ăn lót dạ! |  | chú cá ngọc nhỏ nhắn màu bạc trong suốt trơn tuột với nụ cười láu cá tinh nghịch đói bụng thò miệng cắn nhấm nháp một mẩu mô ruột của gia chủ; chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán vẫn nằm ngáy phì phò vì mô ruộ |
| b12 | 01:20.2–01:29.1 (9.0s) | L37 | Nhưng Quái Kiệt Ruột Mềm của chúng ta thì vẫn thản nhiên thở phì phò, vì chút mô bị cắn mất sẽ tự mọc lại nhanh như thổi! Đúng là lòng vị tha đến mức bác sĩ cũng phải chào thua! |  | chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán mỉm cười hiền lành vị tha như ông bụt, mô ruột bên trong tự tỏa hào quang xanh ngọc liền sẹo thần tốc. |
| b13 | 01:29.1–01:34.5 (5.3s) | L38 | Các nhà sinh vật học biển từng ghi nhận một kỷ lục không tưởng khiến ai nấy đều phải ôm bụng cười: |  | ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế giở cuốn sổ kỷ lục sinh vật biển ghi nhận một sự thật khó tin khiến cả phòng khám ôm bụng cười. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này. |
| b14 | 01:34.5–01:45.4 (10.9s) | L39 | bên trong khoang cơ thể của một chú Hải Sâm dài 40cm, người ta phát hiện có tới 15 con cá ngọc lớn nhỏ đang chen chúc nằm ngủ cùng một lúc! Chiếc lỗ hậu môn của Quái Kiệt Ruột Mềm | **15 CON CÁ** · trú cùng một lúc · L/350 · [0.42, 0.48]<br>**40 CM** · chiều dài hải sâm · R/480 · [0.72, 0.55] | Bên trong cơ thể chú Hải Sâm dài 40cm có tới 15 chú cá ngọc lớn nhỏ chen chúc nằm xếp lớp ngủ cùng một lúc. |
| b15 | 01:45.4–01:47.8 (2.4s) | L40 | bỗng chốc biến thành trạm xe buýt giờ cao điểm! |  | Minh họa chiếc lỗ hậu môn của chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán đông đúc như cửa trạm xe buýt giờ cao điểm, các chú cá ngọc xếp hàng trật tự chờ tới lượt vào. |
| b16 | 01:47.8–01:56.6 (8.9s) | L41 | Chưa hết, đôi khi cả những chú cua hạt đậu bé xíu cũng mò vào chiếm dụng không gian, biến cơ thể nó thành một khu bảo tồn sinh thái ngầm nhộn nhịp nhất rạn san hô! |  | Thêm một chú cua hạt đậu bé xíu cũng trèo vào góc ruột của chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán ngồi ké, cả hội sinh vật biển mở tiệc trà vui vẻ bên trong lòng mề gia chủ hiền lành. |

### scene04 · PHÓNG BÚI ỐNG CUVIER NHƯ PHÁO HOA SỢI MÌ · 90.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.5 (9.5s) | L42 | Hạng mục khám thứ ba: Thử nghiệm vũ khí phòng vệ chủ động! Giả sử một con cá mập nhỏ hoặc một chú cua biển bạo lực vẫn quyết tâm không buông tha, dồn Hải Sâm vào thế ngàn cân treo sợi tóc. |  | Bảng điện tử chuyển sang HẠNG MỤC 3: THỬ NGHIỆM VŨ KHÍ PHÒNG VỆ CHỦ ĐỘNG; một con cá mập nhỏ và cua biển hung hăng áp sát chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh n |
| b02 | 00:09.5–00:14.5 (5.0s) | L43 | Không có chân để chạy trốn, không có hàm răng để cắn trả, chú Quái Kiệt Ruột Mềm sẽ làm gì? |  | chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán nằm im bất động giữa vòng vây kẻ thù, không chân không răng, tình thế ngàn cân treo sợi tóc. |
| b03 | 00:14.5–00:18.3 (3.8s) | L44 | Nó lập tức quay đuôi lại phía kẻ thù, gồng mạnh cơ thành bụng và... bùm! |  | chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán quay phao câu về phía kẻ thù, gồng mạnh cơ thành bụng chuẩn bị khai hỏa cơ quan phòng vệ bí mật. |
| b04 | 00:18.3–00:25.5 (7.2s) | L45 | Một loạt búi sợi màu trắng xóa mang tên ống Cuvier bắn tung tóe qua đường hậu môn phóng thẳng vào mặt đối thủ như một màn pháo hoa mì Ý kinh dị! |  | Bùm! Một loạt búi sợi màu trắng xóa mang tên ống Cuvier bắn tung tóe qua đường hậu môn phóng thẳng vào mặt đối thủ như một màn pháo hoa mì Ý kinh dị. |
| b05 | 00:25.5–00:32.0 (6.5s) | L46 | Ngay khoảnh khắc chạm vào nước biển và cơ thể kẻ săn mồi, những ống Cuvier này lập tức dãn dài ra gấp 20 lần kích thước ban đầu! | **DÃN 20 LẦN** · kéo dài tức thì · R/350 · [0.65, 0.45] | Những ống Cuvier vừa chạm vào nước biển lập tức dãn dài ra gấp 20 lần như những sợi dây chun đàn hồi khổng lồ bao vây lấy con cua biển. |
| b06 | 00:32.0–00:37.9 (5.9s) | L47 | Đồng thời, lớp màng ngoài vỡ tung, giải phóng một loại chất keo sinh học siêu dính bám chặt vào vảy cá, mai cua và mắt mũi của kẻ địch! |  | Lớp màng ngoài ống Cuvier vỡ tung, giải phóng một loại chất keo sinh học siêu dính bám chặt vào vảy cá, mai cua và mắt mũi của kẻ địch. |
| b07 | 00:37.9–00:44.5 (6.6s) | L48 | Kẻ tấn công càng giãy giụa hoảng loạn thì những sợi tơ dính càng quấn chặt như mạng nhện khổng lồ, khóa cứng hoàn toàn cử động của nó! |  | Một chú cua biển hoạt hình ngộ nghĩnh bị những sợi dây tơ màu trắng quấn quanh chiếc càng như sợi len mềm mại, mặt ngơ ngác giơ hai càng lên bất động đầy hài hước (phong cách hoạt hình trẻ em, không bạo lực). |
| b08 | 00:44.5–00:55.4 (10.9s) | L49 | Chưa dừng lại ở đó, trong những sợi tơ phóng ra còn chứa hợp chất độc tố Holothurin cực mạnh. Độc tố này làm tê liệt hệ thần kinh của các loài cá nhỏ, gây cảm giác bỏng rát cay xè mắt của kẻ săn mồi lớn! |  | Kính hiển vi phân tích độc tố Holothurin tỏa khói tím cay xè làm tê liệt hệ thần kinh cá nhỏ và làm cay cay cay mắt kẻ săn mồi to xác. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này. |
| b09 | 00:55.4–01:02.7 (7.3s) | L50 | Trong lúc đối thủ đang bận quằn quại gỡ mớ mì tơ siêu dính ra khỏi mặt, Hải Sâm của chúng ta đã nhẹ nhàng trườn đi mất tăm mất tích! |  | Con cá mập và cua biển loay hoay gỡ mớ mì tơ dính chặt vào mặt; ở góc xa chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán đã nhẹ nhàng trườn đi mất tăm mất tích với vẻ mặt cười đắc thắng. |
| b10 | 01:02.7–01:10.1 (7.4s) | L51 | Độ dai dính kinh dị của ống Cuvier đã được người dân bản địa ở các hòn đảo Thái Bình Dương như Micronesia khai thác từ thời xa xưa! |  | Bản đồ các hòn đảo Thái Bình Dương như Micronesia nơi người dân bản địa từ thời xa xưa đã biết đến độ dai dính kỳ lạ của búi tơ ống Cuvier. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này. |
| b11 | 01:10.1–01:18.3 (8.2s) | L52 | Ngư dân đi biển khi chẳng may bị đá san hô cứa rách chân đã dùng chính những búi tơ trắng này để băng bó vết thương như một loại băng gạc cầm máu tự nhiên. |  | Ngư dân đi biển chẳng may bị đá san hô cứa rách chân đã dùng chính những búi tơ trắng này để băng bó vết thương như một loại băng gạc cầm máu tự nhiên. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này. |
| b12 | 01:18.3–01:30.7 (12.4s) | L53 | Thậm chí trong trường hợp khẩn cấp, họ còn quấn những búi tơ keo này quanh lòng bàn chân để tạo thành một lớp đế giày bảo hộ siêu bền, giúp họ bước đi thoải mái trên những rạn san hô lởm chởm sắc như dao cạo mà không hề bị trầy xước! |  | Ngư dân quấn các búi tơ dính của hải sâm quanh bàn chân làm thành đế giày bảo hộ dày dặn, tự tin bước đi trên rạn san hô lởm chởm sắc nhọn mà không trầy xước. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này. |

### scene05 · PHUN SẠCH RUỘT GAN VÀ CỖ MÁY LỌC SẠCH ĐÁY BIỂN · 96.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:11.1 (11.1s) | L54 | Hạng mục khám thứ tư: Pha thoát xác rùng rợn và vai trò sinh thái vĩ đại! Nhưng nếu ngay cả chiêu bắn ống Cuvier vẫn chưa đủ để dọa kẻ thù, Hải Sâm sẽ tung ra đòn hy sinh cuối cùng mang tên hiện tượng tự tống nội tạng! |  | Bảng điện tử chuyển sang HẠNG MỤC 4: HIỆN TƯỢNG TỰ TỐNG NỘI TẠNG VÀ VAI TRÒ SINH THÁI; ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế khoanh tay nghiêm túc chuẩn bị theo dõi. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này. |
| b02 | 00:11.1–00:20.0 (8.9s) | L55 | Nó tự bẻ gãy các dây chằng nội tạng bên trong, tự làm rách thành hậu môn, và... nôn mửa tống thẳng toàn bộ dạ dày, đường ruột và các cơ quan nội tạng còn lại bắn ra ngoài biển! |  | Theo phong cách hoạt hình hài hước thân thiện trẻ em không máu me: chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán nhẹ nhàng phóng ra khối đồ ăn màu cam vui nhộn; chú cá săn mồi dừng lại ăn vui vẻ, còn chú hải sâm lùi vào |
| b03 | 00:20.0–00:31.7 (11.7s) | L56 | Kẻ săn mồi nhìn thấy đống thức ăn tươi sống béo ngậy trước mắt liền dừng lại chén no nê, hoàn toàn quên mất cái xác Hải Sâm rỗng tuếch vừa lủi trốn vào góc khuất! Đúng là kế kim thiền thoát xác phiên bản rùng mình nhất thế giới tự nhiên! |  | Con cá săn mồi mải mê ăn đống ruột tươi; ở góc đá ngầm tối, cái xác chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán rỗng tuếch nhưng vẫn an toàn lủi trốn thoát thân một cách tài tình. |
| b04 | 00:31.7–00:37.9 (6.2s) | L57 | Mất sạch toàn bộ ruột gan, liệu bệnh nhân này có chết không? Các nghiên cứu sinh học tế bào khẳng định: Hoàn toàn không! |  | ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế soi kính hiển vi kiểm tra các mô mầm còn sót lại trong cơ thể rỗng tuếch của chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán, các tế b |
| b05 | 00:37.9–00:51.1 (13.1s) | L58 | Chỉ sau 35 ngày, tức là khoảng 5 tuần ngắn ngủi, từ các mô mầm còn sót lại, Hải Sâm tự phân chia tế bào và tái tạo lại nguyên vẹn 100% toàn bộ hệ tiêu hóa mới toanh: từ miệng, dạ dày, ruột non cho đến ống hậu môn hoàn chỉnh! | **35 NGÀY** · mọc lại cả bộ ruột · L/350 · [0.35, 0.45]<br>**5 TUẦN** · tái sinh 100% · R/480 · [0.68, 0.52] | Timeline 5 tuần bóc lịch: sau 35 ngày, toàn bộ hệ tiêu hóa mới toanh gồm miệng, dạ dày, ruột non và hậu môn của chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán đã mọc lại hoàn chỉnh 100%. |
| b06 | 00:51.1–00:56.7 (5.6s) | L59 | Và khi đã mọc lại đường ruột, Quái Kiệt Ruột Mềm lập tức quay trở lại công việc vĩ đại nhất của nó: làm sạch đại dương! |  | chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán bơi trở lại đáy biển, dùng những xúc tu quanh miệng cần mẫn nuốt từng vốc bùn cát bẩn thỉu chứa cặn bã hữu cơ thối rữa dưới đáy. |
| b07 | 00:56.7–01:05.6 (8.9s) | L60 | Mỗi ngày, một chú Hải Sâm cần mẫn nuốt hàng trăm g bùn cát dưới đáy biển, tiêu hóa sạch sẽ mọi vụn thức ăn hữu cơ thừa thãi và vi khuẩn thối rữa, rồi thải ra những hạt cát sạch tinh khiết. |  | chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán nuốt cát bẩn dưới đáy biển, tiêu hóa sạch sẽ mọi vụn thức ăn hữu cơ thừa thãi và vi khuẩn thối rữa. |
| b08 | 01:05.6–01:16.0 (10.4s) | L61 | Mỗi năm, một cá thể có thể lọc sạch tới hơn 50kg cát! Thậm chí phân của nó còn giàu canxi cacbonat giúp giảm độ axit của nước biển, bảo vệ các rạn san hô khỏi nguy cơ tẩy trắng! | **50 KG CÁT** · lọc sạch mỗi năm · R/350 · [0.65, 0.48] | Chiếc cân đồng hồ đo 50kg cát sạch tinh khiết tuôn ra từ đuôi chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán; san hô xung quanh rạng rỡ nhờ canxi cacbonat bảo vệ khỏi axit hóa. |
| b09 | 01:16.0–01:24.4 (8.4s) | L62 | Trong các thí nghiệm sinh học phân tử, khi kiểm tra các mẫu nước nuôi trồng thủy sản bị ô nhiễm nặng đầy chất thải hữu cơ, người ta chỉ cần thả vào bể vài cá thể Hải Sâm. |  | Bể nuôi thủy sản bị ô nhiễm chất thải đen ngòm, ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế thả vài cá thể chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán vào cày xới đáy bể. |
| b10 | 01:24.4–01:30.9 (6.5s) | L63 | Sau đúng 24 giờ cần mẫn cày xới, toàn bộ cặn bã ô nhiễm dưới đáy bể đã được lọc sạch bóng, nước trong vắt trở lại như nước suối nguồn! | **24 GIỜ** · lọc sạch bể nước · L/350 · [0.35, 0.45] | Sau đúng 24 giờ cần mẫn cày xới, toàn bộ cặn bã ô nhiễm dưới đáy bể đã được lọc sạch bóng, nước trong vắt trở lại như nước suối nguồn. |
| b11 | 01:30.9–01:36.4 (5.5s) | L64 | Chúng chính là những chiếc máy hút bụi cần cù và vĩ đại nhất bảo vệ sự sống còn của toàn bộ đáy đại dương! |  | chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán hóa thân thành chiếc máy hút bụi đại dương siêu cấp đáng yêu, đeo huy hiệu bảo vệ môi trường biển với nụ cười tự hào. |

### scene06 · ĐƠN THUỐC BẤT LỰC VÀ BÓNG ĐEN CỖ MÁY TẠO ĐỜM · 65.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:04.7 (4.7s) | L65 | Tổng kết bệnh án số 23. Từ một khối thịt mềm oặt không não, không mắt, không xương sống, |  | ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế đứng bên bàn tổng kết hồ sơ bệnh án số 23, mô tả một khối thịt mềm oặt không não, không mắt, không xương sống đang nằm trên bàn khám. |
| b02 | 00:04.7–00:14.9 (10.2s) | L66 | Hải Sâm đã biến những điểm yếu tưởng chừng tuyệt vọng thành một bộ giáp sinh tồn đỉnh cao: tự hóa lỏng da như thạch, thở bằng hậu môn, cưu mang cá ngọc, và sẵn sàng hy sinh cả bộ ruột để giữ lấy mạng sống! |  | Bốn ô đồ họa tóm tắt siêu năng lực: hóa lỏng da như thạch, thở bằng hậu môn, cưu mang cá ngọc, và tự tống nội tạng tái sinh. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này. |
| b03 | 00:14.9–00:26.6 (11.7s) | L67 | Kê đơn xuất viện: Cho bệnh nhân về lại đáy cát biển sâu, tiếp tục cày xới làm sạch đại dương và tuyệt đối nhắc nhở khách trọ cá ngọc... đừng có cắn trộm ruột chủ nhà nữa nhé! Ký tên: bác sĩ đã hoàn toàn bất lực! |  | ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế đóng dấu xuất viện cho chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán, đưa ngón tay nhắc nhở chú chú cá ngọc nhỏ nhắn màu bạc trong s |
| b04 | 00:26.6–00:39.0 (12.3s) | L68 | Còn các đồng nghiệp thì sao? Nếu được sở hữu một trong hai năng lực của Quái Kiệt Ruột Mềm: tự hóa lỏng cơ thể để lách qua khe hẹp, hay bắn mạng tơ keo siêu dính trói gô kẻ bắt nạt, bạn chọn cái nào? Hãy để lại bình luận bên dưới nhé! |  | Hai bàn cân lựa chọn: BÊN TRÁI biểu tượng cơ thể hóa lỏng như thạch lách qua khe hẹp; BÊN PHẢI biểu tượng bắn búi tơ keo siêu dính trói kẻ thù, các bạn nhỏ giơ thẻ bình luận có hình trái tim. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này. |
| b05 | 00:39.0–00:47.9 (9.0s) | L69 | Hồ sơ bệnh án phòng khám hôm nay xin tạm gác lại. Nhưng tập sau, chúng ta sẽ quay trở lại phòng thí nghiệm 5 cấp độ để đối đầu với một cỗ máy kinh dị đáy biển còn đáng sợ hơn nữa! |  | ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế gấp tập hồ sơ bệnh án số 23 lại, ánh đèn phòng khám chuyển sang ánh đèn neon xanh tím của phòng thí nghiệm 5 cấp độ với các cột thủy tinh phát sáng. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này. |
| b06 | 00:47.9–00:51.6 (3.6s) | L70 | Một sinh vật cổ đại trơn tuột như lươn, không có hàm, không có xương sống, |  | Một sinh vật bí ẩn được vẽ hoàn toàn bằng BÓNG ĐEN ĐẶC TUYỀN (solid black silhouette) dài ngoằng trơn tuột như con lươn, không có hàm, đang bơi giữa cột nước tối với dấu hỏi chấm vàng lớn phía trên; KHÔNG vẽ rõ mắt hay màu da. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này. |
| b07 | 00:51.6–01:00.9 (9.4s) | L71 | nhưng khi bị cá mập cắn vào, nó có thể biến 20 lít nước biển xung quanh thành một khối keo nhớt đặc quánh chỉ trong đúng 1 giây làm nghẹt thở kẻ thù, rồi tự thắt nút cơ thể như một ảo thuật gia để tẩu thoát! | **20 LÍT KEO** · đặc quánh trong 1 giây · R/350 · [0.65, 0.45] | Cũng chiếc BÓNG ĐEN ĐẶC TUYỀN (solid black silhouette) hình con lươn đó phóng ra cả một khối keo nhớt khổng lồ 20 lít bọc kín đầu một con cá mập, và tự thắt nút cơ thể mình như một nút thòng lọng ảo thuật; dấu hỏi chấm to tướng. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này. |
| b08 | 01:00.9–01:05.9 (5.0s) | L72 | Đố các bạn biết bóng đen bí ẩn kỳ sau là loài vật nào? Hãy đoán ngay ở phần bình luận nhé! |  | Chiếc BÓNG ĐEN ĐẶC TUYỀN bí ẩn có khả năng tạo keo nhớt khổng lồ nằm giữa ba dấu hỏi chấm vàng cam lấp lánh mời gọi khán giả bình luận đoán tên con vật kỳ sau. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này. |

## 5. Phân cảnh Shorts — từng beat

Banner: **BẮN CẢ BỘ RUỘT GAN / ĐỂ THOÁT THÂN?!** · giọng 47.5s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Khi bị kẻ săn mồi dồn vào chân tường, loài vật này không chạy trốn, |  |
| s02 | 00:03.9 | S02 | mà chọn cách... bắn thẳng toàn bộ ruột gan của mình qua đường hậu môn để tẩu thoát! |  |
| s03 | 00:08.4 | S03 | Xin giới thiệu Hải Sâm, sinh vật hình chiếc xúc xích dài 30cm sống dưới đáy biển sâu. | **30 CM** · xúc xích đáy biển · R/620 · [0.58, 0.5] |
| s04 | 00:14.3 | S04 | Cơ thể nó không hề có não, không có mắt, không có tim, |  |
| s05 | 00:17.2 | S05 | và thở bằng cách bơm nước vào ra chiếc lỗ hậu môn! |  |
| s06 | 00:20.4 | S06 | Da của nó làm từ mô liên kết đặc biệt, |  |
| s07 | 00:22.7 | S07 | có thể tự chuyển từ cứng ngắc như đá sang mềm nhão như thạch chỉ trong 1 giây để chui lọt qua khe đá hẹp! | **1 GIÂY** · hóa lỏng như thạch · R/650 · [0.55, 0.52] |
| s08 | 00:28.4 | S08 | Khi bị tấn công, nó bắn ra những ống tơ trắng dãn dài gấp 20 lần dính chặt cứng lấy kẻ thù. | **DÃN 20 LẦN** · tơ keo siêu dính · L/680 · [0.45, 0.5] |
| s09 | 00:33.4 | S09 | Nếu vẫn chưa thoát, nó sẵn sàng nôn sạch toàn bộ đường ruột ra ngoài để kẻ địch mải ăn, |  |
| s10 | 00:37.9 | S10 | rồi lủi trốn và tự mọc lại nguyên vẹn bộ ruột mới chỉ sau 5 | **5 TUẦN** · tái sinh bộ ruột · R/680 · [0.55, 0.5] |
| s11 | 00:41.2 | S11 | tuần! Một quái kiệt đáy biển vừa biết hóa lỏng, vừa thở bằng hậu môn, |  |
| s12 | 00:45.0 | S12 | đúng là phép màu sinh học điên rồ nhất đại dương! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Phòng cấp cứu y khoa dã thiết lập tại trạm nghiên cứu đáy biển sâu. Chuông báo động vang lên hồi còi gấp rút, đèn mổ bật sáng trên khay kim loại khử trùng.". Bố cục: Trạm nghiên cứu y khoa dã chiến dựng dưới đáy biển sâu với các vòm kính nhìn ra rạn san hô, đèn mổ bật sáng trên bàn khám kim loại. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bệnh nhân số 23 tự trườn vào phòng khám với dáng vẻ chậm rãi kỳ quặc đến mức không tưởng: một cục thịt dài ngoằng màu nâu đốm vàng, mềm oặt như chiếc xúc xích bị bỏ quên dưới đáy cát...". Bố cục: chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán lững thững trườn chậm rãi vào phòng khám, thân hình dài ngoằng màu nâu đốm vàng mềm oặt như chiếc xúc xích khổng lồ bò trên nền cát.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không có hộp sọ. Không có bộ não. Không có lấy một đôi mắt. Và thậm chí không có cả một trái tim để đập bơm máu!". Bố cục: Ba ô đồ họa chẩn đoán gạch chéo đỏ: hình hộp sọ bị gạch chéo, hình bộ não bị gạch chéo, hình đôi mắt và trái tim bị gạch chéo đỏ; dấu chấm hỏi to ở giữa. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bác sĩ ơi, em đo nhịp tim mãi mà máy cứ kêu tút tút bằng phẳng, bệnh nhân này thực sự là một sinh vật sống hay là một khúc chả lụa dưới biển vậy ạ?". Bố cục: BÊN TRÁI cô trợ lý phòng khám hoạt hình mặc áo blouse xanh nhạt cầm ống nghe y tế áp vào người chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán, màn hình máy đo điện tim bên cạnh chỉ là một đường thẳng tắp kêu tút tút kéo dài hài hước.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trợ lý bình tĩnh, bệnh nhân vẫn đang sống nhăn răng... à quên, nó còn chẳng thèm có răng nữa cơ!". Bố cục: ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế đứng bên cạnh cười toe toét giơ ngón tay giải thích; chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán nằm trên bàn khám há miệng tròn xoe không có lấy một chiếc răng nào.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Xin giới thiệu với các đồng nghiệp: đây là Hải Sâm, sinh vật da gai thuộc lớp Động vật chân gai, họ hàng xa với sao biển và cầu gai.". Bố cục: Cây phả hệ sinh vật biển da gai: chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán đứng giữa cùng họ hàng sao biển màu cam và cầu gai nhiều gai nhọn dưới đáy đại dương.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kích thước trung bình dài khoảng 20 đến 30cm.". Bố cục: Ở GIỮA chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán nằm thẳng cạnh chiếc thước đo chiều cao màu vàng 30cm của phòng khám để đối chiếu kích thước.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhìn bề ngoài thì lù đù ngây ngô như khúc dưa chuột biển vô hại, nhưng trong giới sinh học biển, chúng tôi gọi thẳng tên nó bằng biệt danh: Quái Kiệt Ruột Mềm!". Bố cục: Chia đôi: BÊN TRÁI một quả dưa chuột xanh ngắt đặt trên thớt gỗ; BÊN PHẢI chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán khoác áo choàng bệnh nhân giơ dải băng danh hiệu Quái Kiệt Ruột Mềm.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đừng để vẻ ngoài vô tri đó đánh lừa! Dù bị tước đoạt hầu hết các cơ quan nội tạng tiêu chuẩn của động vật có xương sống, Hải Sâm lại sở hữu những siêu năng lực tự vệ quái đản bậc nhất hành tinh:". Bố cục: chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán tạo dáng siêu anh hùng nhưng cơ thể mềm oặt như cục bột, các nốt sần gai mềm rung rinh ngộ nghĩnh.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "cơ thể tự hóa lỏng thành thạch nhớt trong tích tắc, thở trực tiếp bằng đường... hậu môn, và khi bị dồn vào chân tường, nó sẵn sàng bắn phăng toàn bộ ruột gan của mình ra ngoài để trói gô kẻ thù!". Bố cục: Ba ô đồ họa năng lực tự vệ kỳ dị: ô một hóa lỏng như thạch, ô hai thở bằng hậu môn, ô ba bắn ruột qua đuôi; dấu chấm than đỏ rực. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hôm nay, phòng khám của chúng ta sẽ mổ xẻ 4 hạng mục kỳ dị nhất của Quái Kiệt Ruột Mềm này!". Bố cục: ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế bật chiếc đèn mổ công suất lớn soi thẳng vào chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán đang nằm thư thái trên bàn mổ, xung quanh là 4 tấm bảng hồ sơ bệnh án chuẩn bị mở ra.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hạng mục khám đầu tiên: Chụp cắt lớp mô da và kiểm tra độ đàn hồi!". Bố cục: Bảng điện tử phòng khám hiện HẠNG MỤC 1: CHỤP CẮT LỚP MÔ DA; ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế đeo găng tay cao su chuẩn bị kiểm tra độ đàn hồi. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bình thường khi một con cua biển hay tôm hùm đói bụng mò tới định cắn thử, Quái Kiệt Ruột Mềm sẽ lập tức gồng cơ thể lên: toàn bộ lớp da dày sần sùi của nó đột ngột cứng ngắc lại như một khúc gỗ hóa thạch,". Bố cục: Một con cua biển hung dữ giơ chiếc càng to kẹp mạnh vào lưng chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán, cơ thể chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán đột ngột gồng cứng ngắc lại như một khúc gỗ hóa thạch.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "khiến chiếc càng cua kẹp vào chỉ nghe tiếng cộp cộp trượt ra ngoài mà không thể xuyên thủng!". Bố cục: Chiếc càng cua biển kẹp vào lưng chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán bị trượt cộp cộp văng ra ngoài, không thể xuyên thủng lớp da sần sùi cứng đanh.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng điều làm toàn bộ hội đồng y bác sĩ phải trợn tròn mắt là hiện tượng diễn ra ngay sau đó!". Bố cục: ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế và cô trợ lý phòng khám hoạt hình mặc áo blouse xanh nhạt trợn tròn mắt kinh ngạc nhìn vào màn hình máy quét: hiện tượng biến đổi vật lý kỳ lạ bắt đầu diễn ra.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu kẻ săn mồi cố tìm cách lôi nó ra khỏi hang hốc, cơ thể nó chỉ mất đúng 1 giây để kích hoạt phản xạ thần kinh đặc biệt:". Bố cục: Đồng hồ cát điện tử đếm 1 giây: chỉ trong 1 giây, phản xạ thần kinh đặc biệt kích hoạt làm thay đổi hoàn toàn cấu trúc cơ thể.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "toàn bộ lớp thịt cứng như đá bỗng nhiên mềm nhũn ra, chảy nhão như một khối thạch rau câu ấm nóng!". Bố cục: Thân hình của chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán mềm mại uyển chuyển như đĩa thạch rau câu ngọt ngào đặt trên khay phòng lab.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhờ trạng thái nhão nhớt tự hóa lỏng này, Hải Sâm có thể nhẹ nhàng luồn lách thân mình trượt qua những khe nứt đá ngầm hẹp chỉ bằng một nửa đường kính cơ thể nó!". Bố cục: chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán ở trạng thái nhão nhớt tự hóa lỏng, nhẹ nhàng trườn cơ thể luồn lách qua một khe nứt đá ngầm hẹp chỉ bằng một nửa thân mình một cách êm ru.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Vừa chui tọt vào bên trong khe đá an toàn xong, nó lại phóng điện hóa học và... cứng ngắc trở lại, chèn chặt vào vách đá khiến không có bất kỳ móng vuốt nào lôi nó ra được!". Bố cục: Bên trong khe đá ngầm, chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán đột ngột đông cứng trở lại như tảng đá chèn chặt vào vách nứt; bên ngoài con cua biển thò càng vào lôi mãi không ra.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bí mật đằng sau khả năng biến hình như người lỏng kẻ hủy diệt này là gì? Các nhà cơ sinh học phát hiện da của Hải Sâm được cấu tạo từ một loại vật liệu siêu đẳng mang tên mô liên kết biến tính, chủ yếu là các sợi collagen đan cài vào nhau.". Bố cục: Sơ đồ hiển vi phân tử da Hải Sâm: các sợi collagen đan cài vào nhau như lưới thép, protein Tensilin và các ion canxi phát sáng màu xanh điều hòa liên kết. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng thay vì dùng cơ bắp để co bóp, nó điều khiển các phân tử protein chuyên dụng như Tensilin và nồng độ ion canxi để chủ động khóa cứng hoặc tháo rời các liên kết sợi này trong chớp mắt!". Bố cục: Mô hình protein Tensilin hoạt động như công tắc mở đóng các chốt khóa giữa các sợi collagen mà không tốn một chút năng lượng cơ bắp nào. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Muốn cứng là cứng, muốn mềm là mềm, không tốn lấy một giọt calo vận động!". Bố cục: chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán chuyển đổi hai nửa thân mình: nửa bên trái cứng như đá tảng gõ keng keng, nửa bên phải mềm nhèo như thạch chảy, mặt cười tít mắt không tốn calo.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Để chứng minh điều kỳ diệu này, các nhà nghiên cứu từng làm một thí nghiệm trong phòng lab: khi ngâm một mẩu mô da của Hải Sâm vào dung dịch nước biển nhân tạo đã rút sạch ion canxi, toàn bộ cấu trúc da rã rời ra như một bát súp nhầy nhụa!". Bố cục: Trong phòng lab: một mẩu mô da hải sâm ngâm trong cốc thủy tinh nước biển nhân tạo rút sạch canxi bị rã rời ra như một bát súp nhầy nhụa lỏng bỏng. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng chỉ cần nhỏ vài giọt dung dịch canxi vào, các sợi collagen lập tức liên kết chéo trở lại, biến bát súp lỏng bỏng thành một khối thạch cứng đanh như gạch nung chỉ sau vài chục giây!". Bố cục: Ống nhỏ giọt nhỏ vài giọt dung dịch canxi vào cốc, bát súp lỏng lập tức liên kết chéo đông cứng đanh lại thành khối thạch rắn rỏi như gạch nung. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giới kỹ sư vật liệu sinh học hiện đại đang điên cuồng học hỏi cơ chế này để chế tạo áo giáp chống đạn thông minh: bình thường mặc mềm mại như áo phông, nhưng khi bị đạn bắn vào sẽ lập tức hóa cứng như thép tấm!". Bố cục: Mô hình áo giáp chống đạn tương lai thông minh: bình thường mềm mại như chiếc áo phông co giãn, khi bị viên đạn chạm vào lập tức hóa cứng thành tấm thép. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chuyển sang hạng mục khám thứ hai: Nội soi hệ hô hấp và kiểm tra khách trọ bất đắc dĩ! Nếu bạn hỏi Hải Sâm dùng mũi hay miệng để hít thở dưỡng khí, thì bác sĩ chúng tôi xin trả lời thẳng thắn:". Bố cục: Bảng điện tử chuyển sang HẠNG MỤC 2: NỘI SOI HỆ HÔ HẤP; ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế cầm ống nội soi mềm chỉ về phía chiếc lỗ hậu môn của chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nó dùng đúng chiếc lỗ hậu môn để thở suốt 24 giờ mỗi ngày!". Bố cục: Cận cảnh chiếc lỗ hậu môn phía sau của chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán co bóp thở phì phò, bên cạnh đồng hồ 24 giờ quay đều liên tục.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bên trong khoang sau của Quái Kiệt Ruột Mềm gắn liền với một hệ thống ống phân nhánh chằng chịt như hai cành cây san hô gọi là cây hô hấp.". Bố cục: Mặt cắt giải phẫu bên trong cơ thể chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán: gắn liền với lỗ hậu môn là hai nhánh ống cây hô hấp phân nhánh chằng chịt rực rỡ như cành san hô đỏ.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Cứ đều đặn 3-4 lần mỗi phút, chiếc lỗ hậu môn phía sau sẽ mở to ra, hút đầy nước biển giàu oxy vào trong hai nhánh cây hô hấp để trao đổi khí,". Bố cục: Chiếc lỗ hậu môn phía sau của chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán mở to ra hút dòng nước biển giàu oxy xanh mát vào trong hai cây hô hấp để trao đổi dưỡng khí.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "rồi lại co bóp tống dòng nước cũ ra ngoài! Đối với Hải Sâm, thở và bài tiết dùng chung một cửa ngõ!". Bố cục: Hậu môn co bóp tống dòng nước cũ ra ngoài thành dòng bong bóng khí; chiếc biển báo ghi dòng chữ: Thở và bài tiết dùng chung một cửa ngõ. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bác sĩ ơi, trong lúc đặt ống nội soi vào hậu môn bệnh nhân, em phát hiện có một cái đuôi cá đang ngọ nguậy thò ra thò vào ạ!". Bố cục: cô trợ lý phòng khám hoạt hình mặc áo blouse xanh nhạt giật nảy mình chỉ vào màn hình nội soi: từ lỗ hậu môn của chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán đang có một chiếc đuôi cá nhỏ nhắn ngọ nguậy thò ra thụt vào.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đúng rồi đấy trợ lý ơi, đây là vụ việc trớ trêu và hài hước bậc nhất đại dương! Lợi dụng chiếc cửa hậu môn mở ra đóng vào đều đặn để thở của Hải Sâm,". Bố cục: ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế bật cười vỗ trán chỉ lên màn hình: vụ việc trớ trêu và hài hước bậc nhất đại dương giữa hải sâm và chú cá ngọc. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "một loài cá nhỏ nhắn trơn trượt tên là Cá Ngọc Carapus đã nảy ra một ý tưởng sinh tồn siêu lười: nó bơi ngược dòng nước, dùng chiếc đầu nhọn hoặc đuôi trườn thẳng vào trong cơ thể Hải Sâm để ở nhờ!". Bố cục: Chú cá ngọc nhỏ màu bạc bơi lượn quanh chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán đang nằm thư thái trên cát biển, chuẩn bị tìm chỗ trú ẩn kết bạn (phong cách hoạt hình trẻ em đáng yêu).
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chào bác sĩ, em thuê phòng khách sạn ở đây mát mẻ an toàn lắm, kẻ thù bên ngoài không dám vào tìm đâu ạ!". Bố cục: chú cá ngọc nhỏ nhắn màu bạc trong suốt trơn tuột với nụ cười láu cá tinh nghịch nằm cuộn tròn mát mẻ trong khoang ruột của chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán, thò mỗi cái đầu ra cửa vẫy vẫy tay chào bác sĩ như ở trong phòng khách sạn hạng sang.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chú cá ngọc coi lòng mề Hải Sâm như một căn hộ chung cư cao cấp hoàn toàn miễn phí! Ban ngày trốn kỹ bên trong nội tạng của gia chủ để ngủ, ban đêm mới thò đầu ra ngoài đi săn mồi.". Bố cục: Minh họa hài hước: cơ thể chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán biến thành tòa chung cư mini có bảng hiệu Khách Sạn Miễn Phí, cá ngọc ban ngày ngủ khò khò, ban đêm bơi ra đi chơi.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tệ hơn nữa, đôi khi đói bụng quá, chú cá này còn tiện mồm gặm nhấm luôn một phần tuyến sinh dục hoặc mô ruột của Hải Sâm để ăn lót dạ!". Bố cục: chú cá ngọc nhỏ nhắn màu bạc trong suốt trơn tuột với nụ cười láu cá tinh nghịch đói bụng thò miệng cắn nhấm nháp một mẩu mô ruột của gia chủ; chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán vẫn nằm ngáy phì phò vì mô ruột bị cắn tự tái tạo lại ngay lập tức.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nhưng Quái Kiệt Ruột Mềm của chúng ta thì vẫn thản nhiên thở phì phò, vì chút mô bị cắn mất sẽ tự mọc lại nhanh như thổi! Đúng là lòng vị tha đến mức bác sĩ cũng phải chào thua!". Bố cục: chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán mỉm cười hiền lành vị tha như ông bụt, mô ruột bên trong tự tỏa hào quang xanh ngọc liền sẹo thần tốc.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các nhà sinh vật học biển từng ghi nhận một kỷ lục không tưởng khiến ai nấy đều phải ôm bụng cười:". Bố cục: ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế giở cuốn sổ kỷ lục sinh vật biển ghi nhận một sự thật khó tin khiến cả phòng khám ôm bụng cười. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bên trong khoang cơ thể của một chú Hải Sâm dài 40cm, người ta phát hiện có tới 15 con cá ngọc lớn nhỏ đang chen chúc nằm ngủ cùng một lúc! Chiếc lỗ hậu môn của Quái Kiệt Ruột Mềm". Bố cục: Bên trong cơ thể chú Hải Sâm dài 40cm có tới 15 chú cá ngọc lớn nhỏ chen chúc nằm xếp lớp ngủ cùng một lúc.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bỗng chốc biến thành trạm xe buýt giờ cao điểm!". Bố cục: Minh họa chiếc lỗ hậu môn của chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán đông đúc như cửa trạm xe buýt giờ cao điểm, các chú cá ngọc xếp hàng trật tự chờ tới lượt vào.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa hết, đôi khi cả những chú cua hạt đậu bé xíu cũng mò vào chiếm dụng không gian, biến cơ thể nó thành một khu bảo tồn sinh thái ngầm nhộn nhịp nhất rạn san hô!". Bố cục: Thêm một chú cua hạt đậu bé xíu cũng trèo vào góc ruột của chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán ngồi ké, cả hội sinh vật biển mở tiệc trà vui vẻ bên trong lòng mề gia chủ hiền lành.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hạng mục khám thứ ba: Thử nghiệm vũ khí phòng vệ chủ động! Giả sử một con cá mập nhỏ hoặc một chú cua biển bạo lực vẫn quyết tâm không buông tha, dồn Hải Sâm vào thế ngàn cân treo sợi tóc.". Bố cục: Bảng điện tử chuyển sang HẠNG MỤC 3: THỬ NGHIỆM VŨ KHÍ PHÒNG VỆ CHỦ ĐỘNG; một con cá mập nhỏ và cua biển hung hăng áp sát chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Không có chân để chạy trốn, không có hàm răng để cắn trả, chú Quái Kiệt Ruột Mềm sẽ làm gì?". Bố cục: chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán nằm im bất động giữa vòng vây kẻ thù, không chân không răng, tình thế ngàn cân treo sợi tóc.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó lập tức quay đuôi lại phía kẻ thù, gồng mạnh cơ thành bụng và... bùm!". Bố cục: chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán quay phao câu về phía kẻ thù, gồng mạnh cơ thành bụng chuẩn bị khai hỏa cơ quan phòng vệ bí mật.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một loạt búi sợi màu trắng xóa mang tên ống Cuvier bắn tung tóe qua đường hậu môn phóng thẳng vào mặt đối thủ như một màn pháo hoa mì Ý kinh dị!". Bố cục: Bùm! Một loạt búi sợi màu trắng xóa mang tên ống Cuvier bắn tung tóe qua đường hậu môn phóng thẳng vào mặt đối thủ như một màn pháo hoa mì Ý kinh dị.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ngay khoảnh khắc chạm vào nước biển và cơ thể kẻ săn mồi, những ống Cuvier này lập tức dãn dài ra gấp 20 lần kích thước ban đầu!". Bố cục: Những ống Cuvier vừa chạm vào nước biển lập tức dãn dài ra gấp 20 lần như những sợi dây chun đàn hồi khổng lồ bao vây lấy con cua biển.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đồng thời, lớp màng ngoài vỡ tung, giải phóng một loại chất keo sinh học siêu dính bám chặt vào vảy cá, mai cua và mắt mũi của kẻ địch!". Bố cục: Lớp màng ngoài ống Cuvier vỡ tung, giải phóng một loại chất keo sinh học siêu dính bám chặt vào vảy cá, mai cua và mắt mũi của kẻ địch.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kẻ tấn công càng giãy giụa hoảng loạn thì những sợi tơ dính càng quấn chặt như mạng nhện khổng lồ, khóa cứng hoàn toàn cử động của nó!". Bố cục: Một chú cua biển hoạt hình ngộ nghĩnh bị những sợi dây tơ màu trắng quấn quanh chiếc càng như sợi len mềm mại, mặt ngơ ngác giơ hai càng lên bất động đầy hài hước (phong cách hoạt hình trẻ em, không bạo lực).
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chưa dừng lại ở đó, trong những sợi tơ phóng ra còn chứa hợp chất độc tố Holothurin cực mạnh. Độc tố này làm tê liệt hệ thần kinh của các loài cá nhỏ, gây cảm giác bỏng rát cay xè mắt của kẻ săn mồi lớn!". Bố cục: Kính hiển vi phân tích độc tố Holothurin tỏa khói tím cay xè làm tê liệt hệ thần kinh cá nhỏ và làm cay cay cay mắt kẻ săn mồi to xác. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong lúc đối thủ đang bận quằn quại gỡ mớ mì tơ siêu dính ra khỏi mặt, Hải Sâm của chúng ta đã nhẹ nhàng trườn đi mất tăm mất tích!". Bố cục: Con cá mập và cua biển loay hoay gỡ mớ mì tơ dính chặt vào mặt; ở góc xa chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán đã nhẹ nhàng trườn đi mất tăm mất tích với vẻ mặt cười đắc thắng.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Độ dai dính kinh dị của ống Cuvier đã được người dân bản địa ở các hòn đảo Thái Bình Dương như Micronesia khai thác từ thời xa xưa!". Bố cục: Bản đồ các hòn đảo Thái Bình Dương như Micronesia nơi người dân bản địa từ thời xa xưa đã biết đến độ dai dính kỳ lạ của búi tơ ống Cuvier. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Ngư dân đi biển khi chẳng may bị đá san hô cứa rách chân đã dùng chính những búi tơ trắng này để băng bó vết thương như một loại băng gạc cầm máu tự nhiên.". Bố cục: Ngư dân đi biển chẳng may bị đá san hô cứa rách chân đã dùng chính những búi tơ trắng này để băng bó vết thương như một loại băng gạc cầm máu tự nhiên. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Thậm chí trong trường hợp khẩn cấp, họ còn quấn những búi tơ keo này quanh lòng bàn chân để tạo thành một lớp đế giày bảo hộ siêu bền, giúp họ bước đi thoải mái trên những rạn san hô lởm chởm sắc như dao cạo mà không hề bị trầy xước!". Bố cục: Ngư dân quấn các búi tơ dính của hải sâm quanh bàn chân làm thành đế giày bảo hộ dày dặn, tự tin bước đi trên rạn san hô lởm chởm sắc nhọn mà không trầy xước. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hạng mục khám thứ tư: Pha thoát xác rùng rợn và vai trò sinh thái vĩ đại! Nhưng nếu ngay cả chiêu bắn ống Cuvier vẫn chưa đủ để dọa kẻ thù, Hải Sâm sẽ tung ra đòn hy sinh cuối cùng mang tên hiện tượng tự tống nội tạng!". Bố cục: Bảng điện tử chuyển sang HẠNG MỤC 4: HIỆN TƯỢNG TỰ TỐNG NỘI TẠNG VÀ VAI TRÒ SINH THÁI; ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế khoanh tay nghiêm túc chuẩn bị theo dõi. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nó tự bẻ gãy các dây chằng nội tạng bên trong, tự làm rách thành hậu môn, và... nôn mửa tống thẳng toàn bộ dạ dày, đường ruột và các cơ quan nội tạng còn lại bắn ra ngoài biển!". Bố cục: Theo phong cách hoạt hình hài hước thân thiện trẻ em không máu me: chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán nhẹ nhàng phóng ra khối đồ ăn màu cam vui nhộn; chú cá săn mồi dừng lại ăn vui vẻ, còn chú hải sâm lùi vào góc đá an toàn.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kẻ săn mồi nhìn thấy đống thức ăn tươi sống béo ngậy trước mắt liền dừng lại chén no nê, hoàn toàn quên mất cái xác Hải Sâm rỗng tuếch vừa lủi trốn vào góc khuất! Đúng là kế kim thiền thoát xác phiên bản rùng mình nhất thế giới tự nhiên!". Bố cục: Con cá săn mồi mải mê ăn đống ruột tươi; ở góc đá ngầm tối, cái xác chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán rỗng tuếch nhưng vẫn an toàn lủi trốn thoát thân một cách tài tình.
```
</details>

<details><summary>L57</summary>

```text
HÌNH L57 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mất sạch toàn bộ ruột gan, liệu bệnh nhân này có chết không? Các nghiên cứu sinh học tế bào khẳng định: Hoàn toàn không!". Bố cục: ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế soi kính hiển vi kiểm tra các mô mầm còn sót lại trong cơ thể rỗng tuếch của chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán, các tế bào bắt đầu phân chia tái tạo lại từ đầu.
```
</details>

<details><summary>L58</summary>

```text
HÌNH L58 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chỉ sau 35 ngày, tức là khoảng 5 tuần ngắn ngủi, từ các mô mầm còn sót lại, Hải Sâm tự phân chia tế bào và tái tạo lại nguyên vẹn 100% toàn bộ hệ tiêu hóa mới toanh: từ miệng, dạ dày, ruột non cho đến ống hậu môn hoàn chỉnh!". Bố cục: Timeline 5 tuần bóc lịch: sau 35 ngày, toàn bộ hệ tiêu hóa mới toanh gồm miệng, dạ dày, ruột non và hậu môn của chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán đã mọc lại hoàn chỉnh 100%.
```
</details>

<details><summary>L59</summary>

```text
HÌNH L59 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Và khi đã mọc lại đường ruột, Quái Kiệt Ruột Mềm lập tức quay trở lại công việc vĩ đại nhất của nó: làm sạch đại dương!". Bố cục: chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán bơi trở lại đáy biển, dùng những xúc tu quanh miệng cần mẫn nuốt từng vốc bùn cát bẩn thỉu chứa cặn bã hữu cơ thối rữa dưới đáy.
```
</details>

<details><summary>L60</summary>

```text
HÌNH L60 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi ngày, một chú Hải Sâm cần mẫn nuốt hàng trăm g bùn cát dưới đáy biển, tiêu hóa sạch sẽ mọi vụn thức ăn hữu cơ thừa thãi và vi khuẩn thối rữa, rồi thải ra những hạt cát sạch tinh khiết.". Bố cục: chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán nuốt cát bẩn dưới đáy biển, tiêu hóa sạch sẽ mọi vụn thức ăn hữu cơ thừa thãi và vi khuẩn thối rữa.
```
</details>

<details><summary>L61</summary>

```text
HÌNH L61 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi năm, một cá thể có thể lọc sạch tới hơn 50kg cát! Thậm chí phân của nó còn giàu canxi cacbonat giúp giảm độ axit của nước biển, bảo vệ các rạn san hô khỏi nguy cơ tẩy trắng!". Bố cục: Chiếc cân đồng hồ đo 50kg cát sạch tinh khiết tuôn ra từ đuôi chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán; san hô xung quanh rạng rỡ nhờ canxi cacbonat bảo vệ khỏi axit hóa.
```
</details>

<details><summary>L62</summary>

```text
HÌNH L62 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong các thí nghiệm sinh học phân tử, khi kiểm tra các mẫu nước nuôi trồng thủy sản bị ô nhiễm nặng đầy chất thải hữu cơ, người ta chỉ cần thả vào bể vài cá thể Hải Sâm.". Bố cục: Bể nuôi thủy sản bị ô nhiễm chất thải đen ngòm, ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế thả vài cá thể chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán vào cày xới đáy bể.
```
</details>

<details><summary>L63</summary>

```text
HÌNH L63 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sau đúng 24 giờ cần mẫn cày xới, toàn bộ cặn bã ô nhiễm dưới đáy bể đã được lọc sạch bóng, nước trong vắt trở lại như nước suối nguồn!". Bố cục: Sau đúng 24 giờ cần mẫn cày xới, toàn bộ cặn bã ô nhiễm dưới đáy bể đã được lọc sạch bóng, nước trong vắt trở lại như nước suối nguồn.
```
</details>

<details><summary>L64</summary>

```text
HÌNH L64 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chúng chính là những chiếc máy hút bụi cần cù và vĩ đại nhất bảo vệ sự sống còn của toàn bộ đáy đại dương!". Bố cục: chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán hóa thân thành chiếc máy hút bụi đại dương siêu cấp đáng yêu, đeo huy hiệu bảo vệ môi trường biển với nụ cười tự hào.
```
</details>

<details><summary>L65</summary>

```text
HÌNH L65 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tổng kết bệnh án số 23. Từ một khối thịt mềm oặt không não, không mắt, không xương sống,". Bố cục: ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế đứng bên bàn tổng kết hồ sơ bệnh án số 23, mô tả một khối thịt mềm oặt không não, không mắt, không xương sống đang nằm trên bàn khám.
```
</details>

<details><summary>L66</summary>

```text
HÌNH L66 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hải Sâm đã biến những điểm yếu tưởng chừng tuyệt vọng thành một bộ giáp sinh tồn đỉnh cao: tự hóa lỏng da như thạch, thở bằng hậu môn, cưu mang cá ngọc, và sẵn sàng hy sinh cả bộ ruột để giữ lấy mạng sống!". Bố cục: Bốn ô đồ họa tóm tắt siêu năng lực: hóa lỏng da như thạch, thở bằng hậu môn, cưu mang cá ngọc, và tự tống nội tạng tái sinh. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này.
```
</details>

<details><summary>L67</summary>

```text
HÌNH L67 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kê đơn xuất viện: Cho bệnh nhân về lại đáy cát biển sâu, tiếp tục cày xới làm sạch đại dương và tuyệt đối nhắc nhở khách trọ cá ngọc... đừng có cắn trộm ruột chủ nhà nữa nhé! Ký tên: bác sĩ đã hoàn toàn bất lực!". Bố cục: ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế đóng dấu xuất viện cho chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán, đưa ngón tay nhắc nhở chú chú cá ngọc nhỏ nhắn màu bạc trong suốt trơn tuột với nụ cười láu cá tinh nghịch đang thò đầu ra từ đuôi hải sâm không được cắn trộm ruột nữa.
```
</details>

<details><summary>L68</summary>

```text
HÌNH L68 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Còn các đồng nghiệp thì sao? Nếu được sở hữu một trong hai năng lực của Quái Kiệt Ruột Mềm: tự hóa lỏng cơ thể để lách qua khe hẹp, hay bắn mạng tơ keo siêu dính trói gô kẻ bắt nạt, bạn chọn cái nào? Hãy để lại bình luận bên dưới nhé!". Bố cục: Hai bàn cân lựa chọn: BÊN TRÁI biểu tượng cơ thể hóa lỏng như thạch lách qua khe hẹp; BÊN PHẢI biểu tượng bắn búi tơ keo siêu dính trói kẻ thù, các bạn nhỏ giơ thẻ bình luận có hình trái tim. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này.
```
</details>

<details><summary>L69</summary>

```text
HÌNH L69 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hồ sơ bệnh án phòng khám hôm nay xin tạm gác lại. Nhưng tập sau, chúng ta sẽ quay trở lại phòng thí nghiệm 5 cấp độ để đối đầu với một cỗ máy kinh dị đáy biển còn đáng sợ hơn nữa!". Bố cục: ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế gấp tập hồ sơ bệnh án số 23 lại, ánh đèn phòng khám chuyển sang ánh đèn neon xanh tím của phòng thí nghiệm 5 cấp độ với các cột thủy tinh phát sáng. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này.
```
</details>

<details><summary>L70</summary>

```text
HÌNH L70 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một sinh vật cổ đại trơn tuột như lươn, không có hàm, không có xương sống,". Bố cục: Một sinh vật bí ẩn được vẽ hoàn toàn bằng BÓNG ĐEN ĐẶC TUYỀN (solid black silhouette) dài ngoằng trơn tuột như con lươn, không có hàm, đang bơi giữa cột nước tối với dấu hỏi chấm vàng lớn phía trên; KHÔNG vẽ rõ mắt hay màu da. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này.
```
</details>

<details><summary>L71</summary>

```text
HÌNH L71 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nhưng khi bị cá mập cắn vào, nó có thể biến 20 lít nước biển xung quanh thành một khối keo nhớt đặc quánh chỉ trong đúng 1 giây làm nghẹt thở kẻ thù, rồi tự thắt nút cơ thể như một ảo thuật gia để tẩu thoát!". Bố cục: Cũng chiếc BÓNG ĐEN ĐẶC TUYỀN (solid black silhouette) hình con lươn đó phóng ra cả một khối keo nhớt khổng lồ 20 lít bọc kín đầu một con cá mập, và tự thắt nút cơ thể mình như một nút thòng lọng ảo thuật; dấu hỏi chấm to tướng. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này.
```
</details>

<details><summary>L72</summary>

```text
HÌNH L72 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đố các bạn biết bóng đen bí ẩn kỳ sau là loài vật nào? Hãy đoán ngay ở phần bình luận nhé!". Bố cục: Chiếc BÓNG ĐEN ĐẶC TUYỀN bí ẩn có khả năng tạo keo nhớt khổng lồ nằm giữa ba dấu hỏi chấm vàng cam lấp lánh mời gọi khán giả bình luận đoán tên con vật kỳ sau. KHÔNG có chú hải sâm đeo gương bác sĩ trong cảnh này.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Khi bị kẻ săn mồi dồn vào chân tường, loài vật này không chạy trốn,". Bố cục: Khung dọc: con cua biển hung dữ kẹp vào chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán, chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán quay phao câu chuẩn bị khai hỏa cơ quan tự vệ.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "mà chọn cách... bắn thẳng toàn bộ ruột gan của mình qua đường hậu môn để tẩu thoát!". Bố cục: Từ đuôi chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán bắn thẳng toàn bộ ruột gan màu cam ra ngoài biển để kẻ thù mải ăn, còn chú lủi trốn thoát thân.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Xin giới thiệu Hải Sâm, sinh vật hình chiếc xúc xích dài 30cm sống dưới đáy biển sâu.". Bố cục: chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán nằm mũm mĩm hình chiếc xúc xích trên nền cát biển sâu, chiếc thước đo chiều cao màu vàng 30cm dựng thẳng đứng bên cạnh.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Cơ thể nó không hề có não, không có mắt, không có tim,". Bố cục: Khung dọc: hình đồ họa cơ thể chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán gạch chéo não, mắt, tim; không có xương sống.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "và thở bằng cách bơm nước vào ra chiếc lỗ hậu môn!". Bố cục: Chiếc lỗ hậu môn phía sau mở to hút nước biển vào hai cây hô hấp để trao đổi khí thở.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Da của nó làm từ mô liên kết đặc biệt,". Bố cục: chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán cứng như đá tảng gõ keng keng dưới đáy biển.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "có thể tự chuyển từ cứng ngắc như đá sang mềm nhão như thạch chỉ trong 1 giây để chui lọt qua khe đá hẹp!". Bố cục: chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán tự hóa lỏng như đĩa thạch rau câu ấm nóng trượt qua khe đá hẹp chỉ trong 1 giây.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Khi bị tấn công, nó bắn ra những ống tơ trắng dãn dài gấp 20 lần dính chặt cứng lấy kẻ thù.". Bố cục: Từ đuôi chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán bắn ra những búi tơ ống Cuvier màu trắng dãn dài gấp 20 lần như mạng nhện khổng lồ dính chặt cứng lấy con cua biển.
```
</details>

<details><summary>S09</summary>

```text
HÌNH S09 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Nếu vẫn chưa thoát, nó sẵn sàng nôn sạch toàn bộ đường ruột ra ngoài để kẻ địch mải ăn,". Bố cục: chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán tự tống toàn bộ dạ dày ruột gan ra ngoài cho kẻ địch mải ăn, còn cái xác rỗng tuếch nhanh chóng lủi trốn vào kẽ đá.
```
</details>

<details><summary>S10</summary>

```text
HÌNH S10 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "rồi lủi trốn và tự mọc lại nguyên vẹn bộ ruột mới chỉ sau 5 tuần!". Bố cục: Sau 5 tuần, toàn bộ hệ tiêu hóa ruột gan mới toanh của chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán đã mọc lại hoàn chỉnh 100% không để lại tì vết.
```
</details>

<details><summary>S11</summary>

```text
HÌNH S11 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Một quái kiệt đáy biển vừa biết hóa lỏng, vừa thở bằng hậu môn,". Bố cục: Chân dung chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán mũm mĩm tỏa hào quang dưới đáy biển: một nửa thân hóa lỏng như thạch, phía sau mở lỗ thở bằng hậu môn.
```
</details>

<details><summary>S12</summary>

```text
HÌNH S12 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Hải Sâm nâu đốm vàng mũm mĩm, nốt gai mềm, gương soi bác sĩ bạc trên trán; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "đúng là phép màu sinh học điên rồ nhất đại dương!". Bố cục: chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán mỉm cười toe toét ngây thơ đáng yêu giữa rạn san hô rực rỡ, hai tay giơ biểu tượng trái tim phép màu sinh học kỳ diệu.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/72 của video YouTube về Hải Sâm). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán. Nhân vật phụ cố định: ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế; cô trợ lý phòng khám hoạt hình mặc áo blouse xanh nhạt; chú cá ngọc nhỏ nhắn màu bạc trong suốt trơn tuột với nụ cười láu cá tinh nghịch. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/12 của video YouTube Shorts về Hải Sâm). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Hải Sâm (Holothuroidea) hoạt hình màu nâu đốm vàng mũm mĩm tròn lẳn như chiếc xúc xích khổng lồ đáng yêu, hai đầu bo tròn, thân có các nốt sần gai thịt mềm mại, hai mắt to tròn ngộ nghĩnh, đeo một chiếc gương soi bác sĩ tròn màu bạc trên trán. Nhân vật phụ: ông bác sĩ hoạt hình tóc muối tiêu mặc áo blouse trắng, đeo kính tròn và ống nghe y tế. 
```
</details>

## 7. SEO

- **title:** Sinh Vật Không Não Bắn Cả Bộ Ruột Qua Hậu Môn Để Thoát Thân?!
- **hook_paragraph:** Hải Sâm (Sea Cucumber) dài 30cm không có não, không mắt, không tim nhưng sở hữu siêu năng lực kỳ dị bậc nhất đáy biển: tự hóa lỏng da như thạch trong 1 giây, thở bằng hậu môn, cưu mang cá ngọc trong mông và bắn sạch ruột gan để trói kẻ thù rồi tự mọc lại sau 5 tuần!
- **question:** Nếu được sở hữu 1 năng lực của Hải Sâm: tự hóa lỏng cơ thể như thạch hay bắn tơ keo siêu dính trói kẻ thù, bạn chọn cái nào? Và đoán xem bóng đen tập sau là loài nào?
- **next_teaser:** Bóng đen bí ẩn cổ đại: biến 20 lít nước thành keo nhớt đặc quánh trong 1 giây làm ngạt cá mập và tự thắt nút cơ thể!
- **shorts_title:** Sinh Vật Bắn Cả Bộ Ruột Qua Hậu Môn Để Thoát Thân?! 🥒 #độngvật #hảisâm
- **shorts_desc:** Hải Sâm dài 30cm không não, không mắt, thở bằng hậu môn, tự hóa lỏng da như thạch trong 1 giây và sẵn sàng bắn sạch ruột gan để trói chặt kẻ thù rồi tự mọc lại sau 5 tuần! Khám phá bí mật Quái Kiệt Ruột Mềm.
- **bullets:** Chụp cắt lớp: Mô liên kết collagen tự hóa lỏng như thạch để chui qua khe đá và cứng lại trong 1 giây · Nội soi hậu môn: Thở bằng 2 cây hô hấp qua hậu môn và câu chuyện cá ngọc chui vào ở nhờ · Giám định vũ khí: Bắn búi ống Cuvier dãn dài gấp 20 lần dính chặt kẻ thù kèm độc tố Holothurin · Tự tống nội tạng: Phun sạch ruột gan để thoát thân rồi tự tái sinh 100% trong 5 tuần (35 ngày)
- **tags:** hải sâm, hai sam, sea cucumber, holothuroidea, hải sâm bắn ruột, hóa lỏng cơ thể, cá ngọc hải sâm, động vật kỳ lạ, thế giới động vật, động vật hài hước, vẽ chuyện hoang dã, whiteboard animation, khoa học thú vị, bệnh án tiến hóa
- **hashtags:** #độngvật #hảisâm #VẽChuyệnHoangDã

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-23-hai-sam
python src/episode/pipeline.py tts    projects/tap-23-hai-sam     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-23-hai-sam     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-23-hai-sam     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-23-hai-sam              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-23-hai-sam --force
python scripts/beat_sheet.py projects/tap-23-hai-sam               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-23-hai-sam/audio/shorts.wav projects/tap-23-hai-sam/renders/tap-23-hai-sam_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-23-hai-sam
python src/episode/pipeline.py seo    projects/tap-23-hai-sam
python src/episode/episode_doc.py     projects/tap-23-hai-sam
```
