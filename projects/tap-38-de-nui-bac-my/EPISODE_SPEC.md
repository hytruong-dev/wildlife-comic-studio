# TẬP 38 — DÊ NÚI BẮC MỸ · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-38-de-nui-bac-my`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-38-de-nui-bac-my`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F5` · **Persona giọng:** `nha_khoa_hoc` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Dê Núi Bắc Mỹ |
| Tiêu đề YouTube | Bản Vẽ Vách Đá 90°: Dê Núi Khinh Thường Trọng Lực 4.000m Nhờ Đôi Móng Kẹp Cao Su?! \| Tập 38 |
| Video dài | `renders/tap-38-de-nui-bac-my_long.mp4` — 9:30.5 (570.5s) |
| Shorts | `renders/tap-38-de-nui-bac-my_shorts.mp4` — 0:45.3 (45.3s) |
| Thumbnail | `renders/tap-38-de-nui-bac-my_thumbnail.jpg` |
| Số hình | dài 70 beat / 70 ảnh riêng; Shorts 12 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.11**, Shorts tempo tự tính (≥ 1.08) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/70 của video YouTube về Dê Núi Bắc Mỹ). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao Bắc Mỹ (Alpine Mountaineering Field Sketchbook & Topographic Art): nét vẽ bút chì than charcoal mộc mạc phong trần kết hợp các đường đồng mức địa hình cao trình topographic uốn lượn sắc sảo, vách đá vôi dựng đứng gồ ghề, cấu trúc móng guốc giác hút phỏng sinh học độc đáo, phối màu xám đá hoa cương, xanh thông alpine và viền vàng kim trắc địa; NỀN TRẮNG TINH hoàn toàn, không watermark, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — THÁCH THỨC TRỌNG LỰC GIỮA VỰC SÂU NGÀN MÉT
*Thẻ chương:* Sinh vật thách thức định luật vạn vật hấp dẫn của Newton

*Badge:* `ĐẤU TRƯỜNG 90°` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene01_p0.wav` (420 ký tự) · mood `hao_hung`

```text
Chào mừng toàn thể các vận động viên leo núi, các chuyên gia cơ học chuyển động và các bạn đam mê khoa học sinh thái bước vào Đấu trường vách đá tử thần trên dãy núi Rocky hùng vĩ! [laughter] Hôm nay, phòng thí nghiệm cơ sinh học dã ngoại của chúng tôi xin trân trọng giới thiệu một cỗ máy tự nhiên kỳ dị bậc nhất hành tinh, kẻ biến những định luật vạn vật hấp dẫn của ngài Isaac Newton thành một màn giải trí ngoạn mục!
```
**Part 1** → `audio/vs/scene01_p1.wav` (513 ký tự) · mood `don_dap`

```text
Trước ống kính viễn vọng của chúng ta là một bức tường đá hoa cương granite dựng đứng chín mươi độ, nhẵn thín và lạnh lẽo, cao chót vót bốn ngàn mét giữa tầng mây trắng xóa. Phía dưới chân vách đá là vực sâu thăm thẳm không đáy, nơi mà chỉ một cú trượt chân bằng nửa hạt cát cũng đủ khiến bất kỳ sinh vật to lớn nào rơi vào thảm kịch! Thế nhưng hãy phóng to ống kính lên mỏm đá nhọn hoắt kia: Một bóng dáng trắng muốt như tuyết đang ung dung gặm rêu cỏ, đứng vững vàng trên một gờ đá hẹp chưa đầy hai xăng-ti-mét!
```
**Part 2** → `audio/vs/scene01_p2.wav` (224 ký tự) · 🎭 cameo `phat_thanh_vien`

```text
[surprise-oh] Thưa Giáo sư phụ trách, trạm đo laser địa hình ghi nhận độ dốc sườn núi tại vị trí con vật đang đứng đạt tới tám mươi chín độ, gần như song song hoàn hảo với dây dọi thẳng đứng mà không hề có dây thừng trợ lực!
```
**Part 3** → `audio/vs/scene01_p3.wav` (581 ký tự) · mood `tram_bi_an`

```text
Một kết quả đo đạc chính xác đến từng mi-crô-mét thưa phát thanh viên hiện trường! Đối tượng nghiên cứu lừng danh này mang danh pháp khoa học Oreamnos americanus, nhưng toàn thể cộng đồng leo núi thế giới đều nghiêng mình gọi nó bằng danh hiệu kiệt xuất: Vua Trọng Lực Chín Mươi Độ! Trong khi các kiện tướng thể thao đỉnh cao của loài người phải nai nịt giày đinh đặc chế, dây bảo hiểm chuyên dụng, móc treo carabiner và thoa đầy bột chống trơn mới dám mon men leo dốc, thì chú dê núi này chỉ dựa vào bốn chiếc móng guốc bẩm sinh để biến bức tường tử thần thành đường tản bộ êm ái!
```
**Part 4** → `audio/vs/scene01_p4.wav` (369 ký tự) · mood `hao_hung`

```text
Không chỉ đứng yên một chỗ, sinh vật này còn có thể chạy nước rút, xoay xở chuyển hướng và thậm chí phóng mình qua các hố sụt chết chóc với phong thái thong dong như đang dạo chơi công viên! Đằng sau vẻ ngoài điềm tĩnh tựa một thiền sư trên đỉnh núi tuyết là hàng triệu năm tiến hóa khắc nghiệt đã tôi luyện nên một hệ thống khung gầm cơ khí hoàn hảo đến từng chi tiết.
```
**Part 5** → `audio/vs/scene01_p5.wav` (252 ký tự) · mood `hao_hung`

```text
Bí mật vật lý và sinh học nào đã biến Vua Trọng Lực Chín Mươi Độ thành kẻ cai trị tuyệt đối của những vách đá dựng đứng? Ngay bây giờ, xin mời quý vị cùng tôi mở hòm hồ sơ kỹ thuật tầng một để giải phẫu vũ khí kẹp đá đầu tiên mang tên bộ móng thủy lực!
```

### scene02 — BỘ MÓNG GUỐC HAI MẢNH KẸP ĐÁ NHƯ KÌM BẤM THỦY LỰC
*Thẻ chương:* Cấu trúc móng chẻ độc lập ôm trọn từng gờ đá siêu nhỏ

*Badge:* `VŨ KHÍ SỐ 1` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene02_p0.wav` (389 ký tự) · mood `hao_hung`

```text
Xin mời các kỹ sư cơ khí hãy zoom cận cảnh vào bộ phận tiếp xúc tiền tuyến của cỗ máy vượt dốc: Bộ móng guốc chẻ đôi kỳ ảo! Khác biệt hoàn toàn với móng ngựa là một khối sừng liền mạch tròn xoe rất dễ trượt té khi gặp đá nghiêng, bàn chân của Vua Trọng Lực Chín Mươi Độ được xẻ đôi thành hai nửa móng guốc riêng biệt, vận hành tự chủ tựa như hai ngón tay kìm bấm thủy lực cực kỳ linh hoạt!
```
**Part 1** → `audio/vs/scene02_p1.wav` (333 ký tự) · mood `don_dap`

```text
Mỗi nửa móng guốc được bao bọc bởi một lớp vỏ sừng chất đạm keratin cứng như thép tôi và sắc bén như lưỡi rìu đẽo đá. Khi bàn chân giẫm xuống bề mặt gồ ghề, hai nửa móng này lập tức xòe rộng ra theo hình chữ V để bao trọn lấy gờ đá, sau đó các bó gân gập ngón sẽ siết chặt hai nửa móng lại, khóa chặt điểm tì như gọng kìm kẹp ốc vít!
```
**Part 2** → `audio/vs/scene02_p2.wav` (408 ký tự) · mood `tram_bi_an`

```text
Chưa dừng lại ở đó, hai nửa móng này còn có khả năng cử động độc lập lệch pha nhau. Nghĩa là nửa móng bên trái có thể nâng cao lên ba mi-li-mét trong khi nửa móng bên phải hạ thấp xuống để thích ứng chính xác với độ mấp mô không đồng đều của mặt đá granite! Cơ chế vi chỉnh góc tiếp xúc này giúp phân bổ tải trọng đồng đều một trăm phần trăm, ngăn ngừa nguy cơ móng bị bẻ gãy khi tiếp đất với lực va đập lớn.
```
**Part 3** → `audio/vs/scene02_p3.wav` (386 ký tự) · mood `hao_hung`

```text
Và hãy nhìn kỹ ra phía sau cổ chân: Dê núi còn sở hữu hai chiếc móng phụ thoái hóa nằm ở vị trí cao hơn, dân gian hay gọi là móng huyền. Đừng vội coi thường hai mẩu xương nhỏ bé này nhé! [laughter] Khi con vật phải tụt dốc khẩn cấp hoặc sườn núi bị lở cát, hai chiếc móng phụ này sẽ cắm phập xuống lớp sỏi đá như một cặp mỏ neo phanh phụ trợ, dập tắt quán tính trượt dốc trong chớp mắt!
```
**Part 4** → `audio/vs/scene02_p4.wav` (394 ký tự) · mood `tram_bi_an`

```text
Nhờ bộ móng kẹp hai tầng này, dù một con dê đực trưởng thành mang khối lượng cơ thể lên tới một trăm bốn mươi kilôgam, toàn bộ áp lực khổng lồ đó vẫn được truyền dẫn an toàn qua các điểm tiếp xúc tí hon chỉ bằng hạt đậu! Nhưng nếu chỉ có lớp vỏ sừng cứng cáp thì móng guốc vẫn có thể bị trượt khi gặp đá trơn bóng. Vì vậy, thiên nhiên đã lắp đặt thêm một vũ khí bí mật ngay trong lòng bàn chân!
```

### scene03 — ĐỆM CAO SU MA SÁT CAO BÁM DÍNH SIÊU CẤP
*Thẻ chương:* Vật liệu phỏng sinh học lấy cảm hứng cho lốp xe đua

*Badge:* `VŨ KHÍ SỐ 2` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene03_p0.wav` (358 ký tự) · mood `hao_hung`

```text
Nếu viền sừng bên ngoài đóng vai trò là chiếc kẹp cơ học sắc lẹm, thì phần ruột bên trong lòng móng lại là một kiệt tác vật liệu sinh học đàn hồi: Lớp đệm thịt ma sát bám dính siêu cấp! Nằm lọt giữa hai nửa móng guốc là một khối mô xốp hữu cơ mềm dẻo đặc biệt, có bề mặt sần sùi chứa hàng vạn vi rãnh siêu nhỏ đóng vai trò như các giác hút chân không tí hon!
```
**Part 1** → `audio/vs/scene03_p1.wav` (423 ký tự) · mood `don_dap`

```text
Mỗi khi móng chân ấn mạnh xuống phiến đá, khối đệm đàn hồi này sẽ lập tức biến dạng linh hoạt, lấp đầy mọi khe nứt vi mô trên mặt đá hoa cương, biến diện tích tiếp xúc từ một điểm nhỏ thành một bề mặt tì đè rộng lớn. Thử nghiệm trong phòng thí nghiệm vật lý cho thấy: Hệ số ma sát tĩnh của lớp đệm thịt dê núi cao gấp ba lần so với các loại đế cao su tổng hợp đắt giá nhất trang bị trên giày leo núi hiện đại của con người!
```
**Part 2** → `audio/vs/scene03_p2.wav` (427 ký tự) · mood `tram_bi_an`

```text
Đặc tính đáng kinh ngạc nhất của vật liệu sinh học này chính là khả năng chịu nhiệt độ âm cực thấp. Trên đỉnh núi Rocky cao hàng ngàn mét, khi mùa đông gõ cửa khiến nhiệt độ tụt sâu xuống âm ba mươi độ và băng giá phủ kín các vách đá, lốp xe cao su thông thường sẽ bị hóa cứng và trở nên giòn vụn, mất sạch độ bám. Nhưng lớp đệm của Vua Trọng Lực Chín Mươi Độ vẫn giữ nguyên độ dẻo dai ấm áp, không hề đóng băng hay trơn trượt!
```
**Part 3** → `audio/vs/scene03_p3.wav` (290 ký tự) · mood `hao_hung`

```text
Sự kết hợp ăn ý tuyệt đối giữa khung sừng cứng bên ngoài để móc vào gờ nứt và lõi đệm mềm bên trong để hút dính ma sát đã tạo nên một hợp kim cơ sinh học vô tiền khoáng hậu. Dù mặt đá bị phủ một lớp rêu ướt trơn tuột như bôi mỡ, bước chân của nó vẫn bám chặt như được gắn nam châm vĩnh cửu!
```
**Part 4** → `audio/vs/scene03_p4.wav` (250 ký tự) · mood `tram_bi_an`

```text
Thế nhưng, sở hữu bộ móng thần thánh thôi vẫn chưa đủ để chinh phục bức tường chín mươi độ nếu cơ thể thiếu đi một trung tâm điều khiển cân bằng hoàn hảo. Xin mời các bạn cùng tôi nâng tầng phân tích để khám phá hệ thống khung gầm của chú dê núi này!
```

### scene04 — TRỌNG TÂM CƠ THỂ SIÊU THẤP VÀ KHỚP BẢ VAI XOAY LINH HOẠT
*Thẻ chương:* Giải phẫu học tối ưu hóa cân bằng động lực học

*Badge:* `VŨ KHÍ SỐ 3` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene04_p0.wav` (316 ký tự) · mood `hao_hung`

```text
Hãy tưởng tượng nếu một chú hươu cao cổ hay một vận động viên thể hình bình thường đứng tựa lưng vào vách đá dựng đứng: Trọng tâm cơ thể của họ nằm ở vị trí rất cao, cách xa điểm tựa mặt đất, tạo ra một cánh tay đòn mô-men lật đổ cực kỳ nguy hiểm, chỉ cần gió thổi nhẹ một cơn là ngã ngửa xuống vực sâu ngay lập tức!
```
**Part 1** → `audio/vs/scene04_p1.wav` (324 ký tự) · mood `don_dap`

```text
Để hóa giải nghịch lý trọng lực này, tạo hóa đã thiết kế cho dê núi Bắc Mỹ một cấu trúc giải phẫu học độc nhất vô nhị: Đôi chân trước của chúng ngắn hơn đáng kể so với đôi chân sau, lồng ngực nở rộng vạm vỡ dẹp ngang ép sát vào bề mặt đá, và toàn bộ khối lượng nội tạng nặng nề được dồn tụ xuống phần thân trước sát mặt đất!
```
**Part 2** → `audio/vs/scene04_p2.wav` (329 ký tự) · mood `tram_bi_an`

```text
Cấu tạo này kéo hạ thấp trọng tâm toàn bộ cơ thể xuống mức tối đa, dán chặt véc-tơ trọng lực vào lòng vách núi thay vì đẩy ra ngoài không trung. Khi đứng trên sườn dốc nghiêng tám mươi độ, cơ thể chú dê nghiêng nhẹ về phía vách đá, triệt tiêu hoàn toàn lực lật đổ, biến vách đá cheo leo thành chiếc giường tựa vững như bàn thạch!
```
**Part 3** → `audio/vs/scene04_p3.wav` (337 ký tự) · mood `hao_hung`

```text
Đặc biệt, khớp xương bả vai của dê núi sở hữu biên độ tự do xoay chuyển ngang rộng hơn bất kỳ loài thú móng guốc nào khác. Hai chân trước của nó có thể dang rộng sang hai bên như hai cánh tay người, ôm lấy những khối đá lồi để giữ thăng bằng và kéo toàn bộ cơ thể nặng hơn một tạ trèo lên gờ đá cao hơn một cách nhẹ nhàng như tập xà đơn!
```
**Part 4** → `audio/vs/scene04_p4.wav` (265 ký tự) · mood `don_dap`

```text
Chẳng có một cỗ máy việt dã bánh xích nào của con người có thể điều chỉnh trọng tâm linh hoạt đến mức ấy. Và khi đã đạt đến đỉnh cao của sự thăng bằng tĩnh, chú dê núi bắt đầu phô diễn tuyệt kỹ chuyển động đỉnh cao nhất: Kỹ thuật parkour búng tường giữa tầng không!
```

### scene05 — CÚ NHẢY BÚNG TƯỜNG NGOẠN MỤC XOAY NGƯỜI GIỮA KHÔNG TRUNG
*Thẻ chương:* Kỹ thuật parkour đỉnh cao của nhà vô địch vách đá

*Badge:* `VŨ KHÍ SỐ 4` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene05_p0.wav` (467 ký tự) · mood `hao_hung`

```text
Đỉnh cao nghệ thuật sinh tồn của Vua Trọng Lực Chín Mươi Độ chỉ thực sự phát hỏa rực rỡ nhất khi nó dồn mình vào bước đường cùng: Trước mặt là vách đá nhẵn thín không còn một gờ nứt nào để tiến bước, bên dưới là vực sâu ngàn trượng, và phía sau có thể là một con báo sư tử đang rình rập săn mồi! [dissatisfaction-hnn] Đối với mọi sinh vật khác, đây là bản án tử hình chắc chắn. Nhưng đối với dê núi, đây lại là thời khắc bắt đầu của màn trình diễn nhào lộn kinh điển!
```
**Part 1** → `audio/vs/scene05_p1.wav` (468 ký tự) · mood `don_dap`

```text
Chẳng hề do dự hay run rẩy, nó dồn toàn bộ sức nén vào đôi chân sau hoạt động như cặp lò xo giảm xóc cỡ lớn, tung mình nhảy vọt ra khỏi gờ đá bay ngang qua hẻm vực sâu thăm thẳm sang bức tường đá đối diện cách xa tới bốn mét! Ngay khi chạm vào mặt đá thẳng đứng bên kia, nó không hề tìm cách bám lại để dừng rơi mà lập tức dùng cả bốn móng guốc đạp mạnh vào vách đá như một vận động viên parkour, búng ngược cơ thể trở lại bức tường ban đầu ở một độ cao vượt trội hơn!
```
**Part 2** → `audio/vs/scene05_p2.wav` (180 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
[surprise-oh] Thưa Giáo sư, một cú nhào lộn xoay người một trăm tám mươi độ giữa khoảng không vực thẳm như vậy đòi hỏi thời gian xử lý não bộ và phản xạ cơ bắp nhanh đến mức nào ạ?
```
**Part 3** → `audio/vs/scene05_p3.wav` (465 ký tự) · mood `hao_hung`

```text
Toàn bộ cú búng tường xoay trục một trăm tám mươi độ ấy diễn ra trong vỏn vẹn chưa đầy nửa giây thưa bạn trẻ! Các xung thần kinh từ thị giác truyền thẳng về tiểu não khổng lồ để tính toán véc-tơ phản lực và điều chỉnh góc xòe của móng guốc với độ chính xác tuyệt đối. Bằng chuỗi động tác búng tường zig-zag liên hồi, nó có thể thăng tiến hàng chục mét vách đá dốc đứng chỉ trong vài giây ngắn ngủi, bỏ xa mọi kẻ săn mồi mặt đất đang run rẩy đứng nhìn dưới chân dốc!
```
**Part 4** → `audio/vs/scene05_p4.wav` (249 ký tự) · mood `tram_bi_an`

```text
Kẻ săn mồi dù dũng mãnh và nhanh nhẹn đến đâu cũng chỉ biết há hốc mồm bất lực trước bản lĩnh không gian ba chiều của chú dê núi tuyết. Nơi mà người ta nhìn thấy thần chết rình rập, sinh vật này lại tìm thấy một sân chơi tự do và bình yên tuyệt đối!
```

### scene06 — ĐỈNH CAO THỂ THAO MẠO HIỂM PHỎNG SINH HỌC
*Thẻ chương:* Tôn vinh cỗ máy vượt dốc vĩ đại nhất của tạo hóa

*Badge:* `TRAO HUY CHƯƠNG` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene06_p0.wav` (356 ký tự) · mood `hao_hung`

```text
Kính thưa toàn thể quý khán giả và các nhà khoa học theo dõi buổi tổng kết, sau khi thẩm định chi tiết toàn bộ bốn tuyệt kỹ cơ học từ móng chẻ thủy lực kẹp đá, đệm cao su ma sát siêu bám, trọng tâm cơ thể hạ thấp ép sát vách cho đến cú búng tường zig-zag thần sầu, ban giám khảo nhất trí tuyệt đối trao tấm Huy chương Vàng Cơ Học Vách Đá cho Dê Núi Bắc Mỹ!
```
**Part 1** → `audio/vs/scene06_p1.wav` (426 ký tự) · mood `tram_bi_an`

```text
Sinh vật kiệt xuất này ngày nay chính là nguồn cảm hứng vàng ngọc cho các kỹ sư nghiên cứu robot địa hình của cơ quan hàng không vũ trụ NASA nhằm chế tạo các cánh tay bám kẹp cơ học phục vụ thám hiểm các hẻm vực dốc đứng trên Sao Hỏa và Mặt Trăng. Các thương hiệu thể thao dã ngoại danh tiếng cũng đang nghiên cứu mô phỏng lớp đệm thịt đàn hồi của móng dê để phát triển thế hệ giày leo núi siêu ma sát cho thế kỷ hai mươi mốt.
```
**Part 2** → `audio/vs/scene06_p2.wav` (330 ký tự) · mood `am_ap`

```text
Bài học sinh tồn từ chú dê núi trên vách đá cheo leo nhắc nhở mỗi chúng ta rằng: Khi đối diện với những thử thách dựng đứng tưởng chừng như không thể vượt qua trong cuộc sống, việc tìm kiếm những điểm tựa vững chắc dù là nhỏ bé nhất, cùng một tinh thần thăng bằng kiên định, sẽ giúp chúng ta đứng vững và vươn lên đỉnh vinh quang!
```
**Part 3** → `audio/vs/scene06_p3.wav` (232 ký tự) · mood `hao_hung`

```text
Giữa bộ móng chẻ kìm bấm thủy lực và lớp đệm ma sát siêu cấp, cơ chế cơ sinh học nào của Vua Trọng Lực Chín Mươi Độ khiến bạn kinh ngạc và thán phục nhất? Hãy để lại cảm nghĩ và bình luận tâm đắc của bạn ngay bên dưới video này nhé!
```
**Part 4** → `audio/vs/scene06_p4.wav` (258 ký tự) · mood `am_ap`

```text
Và đừng quên nhấn nút Đăng Ký Kênh cùng chiếc chuông thông báo để đón xem Tập ba mươi chín: Giải mã sát thủ ngây thơ giấu mặt của Chim Bách Thanh! Xin chào tạm biệt và hẹn gặp lại toàn thể các bạn trong những hành trình khám phá thiên nhiên kỳ thú tiếp theo!
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Bạn có tin trên Trái Đất có một loài động vật nặng tới một trăm bốn mươi kilôgam nhưng có thể đứng vững trên vách đá dựng đứng chín mươi độ nhẵn thín không? [laughter] Đó chính là Dê Núi Bắc Mỹ — Vua Trọng Lực Chín Mươi Độ vô địch thiên nhiên! Bí mật chấn động nằm ở bộ móng guốc chẻ đôi kẹp gờ đá như kìm bấm thủy lực, kết hợp cùng lớp đệm thịt cao su ma sát cực đại có độ bám dính gấp ba lần đế giày leo núi chuyên nghiệp! [dissatisfaction-hnn] Khi gặp ngõ cụt giữa vực sâu ngàn mét, nó có thể tung mình nhảy xa bốn mét và búng tường xoay người một trăm tám mươi độ chỉ trong nửa giây! [laughter] Thậm chí, loài dê này còn thong dong leo thẳng lên các bức tường đập thủy điện dốc đứng cao hàng trăm mét chỉ để liếm từng vệt muối khoáng! Quả là bậc thầy khinh công thách thức mọi định luật vật lý của Newton!
```

**Whisper prompt:** `Dê Núi Bắc Mỹ, Oreamnos americanus, Vua Trọng Lực Chín Mươi Độ, vách đá dựng đứng, móng chẻ hai mảnh, đệm cao su ma sát, 90 độ, 4.000 mét, Rocky Mountains, NASA, cơ sinh học`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| Tập ba mươi tám | Tập 38 |
| Tập ba mươi chín | Tập 39 |
| chín mươi độ | 90° |
| tám mươi chín độ | 89° |
| tám mươi độ | 80° |
| sáu mươi độ | 60° |
| bốn mươi lăm độ | 45° |
| bốn ngàn mét | 4.000m |
| ba ngàn mét | 3.000m |
| một ngàn mét | 1.000m |
| bốn trăm mét | 400m |
| hai mét | 2m |
| bốn mét | 4m |
| năm mét | 5m |
| một mét | 1m |
| hai xăng-ti-mét | 2cm |
| ba xăng-ti-mét | 3cm |
| năm xăng-ti-mét | 5cm |
| một trăm bốn mươi kilôgam | 140 kg |
| bảy mươi kilôgam | 70 kg |
| một trăm | 100 |
| một trăm kilôgam | 100 kg |
| một trăm phần trăm | 100% |
| năm mươi phần trăm | 50% |
| sáu mươi phần trăm | 60% |
| hai mươi bốn giờ | 24 giờ |
| mười lần | 10 lần |
| ba lần | 3 lần |
| hai lần | 2 lần |
| năm lần | 5 lần |
| âm ba mươi độ | -30°C |
| một trăm tám mươi độ | 180° |
| thế kỷ hai mươi mốt | thế kỷ 21 |
| hàng triệu năm | hàng triệu năm |
| triệu năm | triệu năm |
| Vua Trọng Lực Chín Mươi Độ | Vua Trọng Lực 90° |
| Oreamnos | Oreamnos |
| americanus | americanus |
| Rocky | Rocky |
| NASA | NASA |
| Isaac Newton | Isaac Newton |
| keratin | keratin |
| carabiner | carabiner |
| polymer | polymer |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · THÁCH THỨC TRỌNG LỰC GIỮA VỰC SÂU NGÀN MÉT · 118.0s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:11.3 (11.3s) | L01 | Chào mừng toàn thể các vận động viên leo núi, các chuyên gia cơ học chuyển động và các bạn đam mê khoa học sinh thái bước vào Đấu trường vách đá tử thần trên dãy núi Rocky hùng vĩ! Hôm nay, |  | Toàn cảnh vách đá tuyết Rocky: chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực đứng trên đỉnh núi tuyết, giơ tay chào khán giả với kính bảo hộ tuyết màu cam viền titan. |
| b02 | 00:11.3–00:24.2 (12.8s) | L02 | phòng thí nghiệm cơ sinh học dã ngoại của chúng tôi xin trân trọng giới thiệu một cỗ máy tự nhiên kỳ dị bậc nhất hành tinh, kẻ biến những định luật vạn vật hấp dẫn của ngài Isaac Newton thành một màn giải trí ngoạn mục! Trước ống kính viễn vọng của chúng ta |  | Mô hình bàn vẽ sổ tay ký họa với sơ đồ cơ sinh học và quả táo rơi của Isaac Newton bị chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực gạt phắt sang một bên. |
| b03 | 00:24.2–00:31.7 (7.5s) | L03 | là một bức tường đá hoa cương granite dựng đứng 90°, nhẵn thín và lạnh lẽo, cao chót vót 4.000m giữa tầng mây trắng xóa. Phía dưới chân vách đá |  | Toàn cảnh vách đá hoa cương granite thẳng đứng chín mươi độ cao bốn ngàn mét giữa mây trời lộng gió. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này. |
| b04 | 00:31.7–00:38.9 (7.2s) | L04 | là vực sâu thăm thẳm không đáy, nơi mà chỉ một cú trượt chân bằng nửa hạt cát cũng đủ khiến bất kỳ sinh vật to lớn nào rơi vào thảm kịch! Thế nhưng hãy phóng to ống |  | Góc nhìn từ trên xuống vực sâu hun hút thăm thẳm với những tầng mây trôi bồng bềnh dưới chân. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này. |
| b05 | 00:38.9–00:47.8 (9.0s) | L05 | kính lên mỏm đá nhọn hoắt kia: Một bóng dáng trắng muốt như tuyết đang ung dung gặm rêu cỏ, đứng vững vàng trên một gờ đá hẹp chưa đầy 2cm! Thưa Giáo sư phụ trách, |  | Khung cảnh zoom cận cảnh: chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực đứng thăng bằng điềm nhiên trên một gờ đá hẹp chỉ bằng hai xăng-ti-mét. |
| b06 | 00:47.8–00:57.0 (9.1s) | L06 | trạm đo laser địa hình ghi nhận độ dốc sườn núi tại vị trí con vật đang đứng đạt tới 89°, gần như song song hoàn hảo với dây dọi thẳng đứng mà không hề có dây thừng trợ lực! |  | Chú sóc tuyết cầm máy đo khoảng cách laser chiếu tia đỏ quét góc dốc tám mươi chín độ của vách đá. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này. |
| b07 | 00:57.0–01:10.5 (13.6s) | L07 | Một kết quả đo đạc chính xác đến từng mi-crô-mét thưa phát thanh viên hiện trường! Đối tượng nghiên cứu lừng danh này mang danh pháp khoa học Oreamnos americanus, nhưng toàn thể cộng đồng leo núi thế giới đều nghiêng mình gọi nó bằng danh hiệu kiệt xuất: Vua Trọng Lực 90°! |  | Tấm huy hiệu vinh danh danh pháp khoa học Oreamnos americanus cùng dòng chữ phong tặng danh hiệu Vua Trọng Lực. chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ. |
| b08 | 01:10.5–01:22.6 (12.1s) | L08 | Trong khi các kiện tướng thể thao đỉnh cao của loài người phải nai nịt giày đinh đặc chế, dây bảo hiểm chuyên dụng, móc treo carabiner và thoa đầy bột chống trơn mới dám mon men leo dốc, thì chú dê núi này chỉ dựa vào bốn chiếc móng guốc bẩm sinh |  | Hình ảnh so sánh: Vận động viên leo núi đeo lỉnh kỉnh dây dù móc sắt thở dốc đối lập với chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực đi dạo thanh thản. |
| b09 | 01:22.6–01:30.6 (8.0s) | L09 | để biến bức tường tử thần thành đường tản bộ êm ái! Không chỉ đứng yên một chỗ, sinh vật này còn có thể chạy nước rút, xoay xở chuyển hướng và thậm |  | Bản vẽ động tác chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực phi nước kiệu nhẹ nhàng băng qua khe nứt hiểm trở trên sườn dốc tuyết. |
| b10 | 01:30.6–01:44.9 (14.3s) | L10 | chí phóng mình qua các hố sụt chết chóc với phong thái thong dong như đang dạo chơi công viên! Đằng sau vẻ ngoài điềm tĩnh tựa một thiền sư trên đỉnh núi tuyết là hàng triệu năm tiến hóa khắc nghiệt đã tôi luyện nên một hệ thống khung gầm cơ khí hoàn hảo đến từng chi tiết. |  | Sơ đồ tiến hóa hàng triệu năm với bộ khung xương vững chãi tôi luyện qua băng giá kỷ băng hà. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này. |
| b11 | 01:44.9–01:58.0 (13.1s) | L11 | Bí mật vật lý và sinh học nào đã biến Vua Trọng Lực 90° thành kẻ cai trị tuyệt đối của những vách đá dựng đứng? Ngay bây giờ, xin mời quý vị cùng tôi mở hòm hồ sơ kỹ thuật tầng một để giải phẫu vũ khí kẹp đá đầu tiên mang tên bộ móng thủy lực! |  | Bàn tay bác sĩ lật mở cuốn hồ sơ bệnh án ký họa mở màn cho chương giải phẫu đầu tiên. chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ. |

### scene02 · BỘ MÓNG GUỐC HAI MẢNH KẸP ĐÁ NHƯ KÌM BẤM THỦY LỰC · 94.8s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.3 (8.3s) | L12 | Xin mời các kỹ sư cơ khí hãy zoom cận cảnh vào bộ phận tiếp xúc tiền tuyến của cỗ máy vượt dốc: Bộ móng guốc chẻ đôi kỳ ảo! Khác biệt hoàn toàn |  | Kính lúp phóng to bộ móng guốc chẻ đôi kỳ lạ của chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực đang tiếp xúc với mặt đá nứt nẻ. |
| b02 | 00:08.3–00:22.1 (13.8s) | L13 | với móng ngựa là một khối sừng liền mạch tròn xoe rất dễ trượt té khi gặp đá nghiêng, bàn chân của Vua Trọng Lực 90° được xẻ đôi thành hai nửa móng guốc riêng biệt, vận hành tự chủ tựa như hai ngón tay kìm bấm thủy lực cực kỳ linh hoạt! Mỗi nửa móng guốc được bao bọc |  | Hình ảnh so sánh móng ngựa tròn trơn trượt ngã nhào đối lập với móng dê núi chẻ đôi kẹp chặt như kìm bấm. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này. |
| b03 | 00:22.1–00:28.5 (6.4s) | L14 | bởi một lớp vỏ sừng chất đạm keratin cứng như thép tôi và sắc bén như lưỡi rìu đẽo đá. Khi bàn chân giẫm xuống bề mặt gồ ghề, hai nửa móng |  | Cấu trúc vỏ sừng keratin cứng như thép tôi của móng guốc với lát cắt hiển vi phân tử đạm siêu bền. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này. |
| b04 | 00:28.5–00:38.4 (10.0s) | L15 | này lập tức xòe rộng ra theo hình chữ V để bao trọn lấy gờ đá, sau đó các bó gân gập ngón sẽ siết chặt hai nửa móng lại, khóa chặt điểm tì như gọng kìm kẹp ốc vít! Chưa dừng lại ở đó, hai nửa móng này còn có |  | Sơ đồ lực học hai nửa móng xòe rộng thành hình chữ V ôm trọn mỏm đá nhọn rồi siết chặt lại. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này. |
| b05 | 00:38.4–00:49.9 (11.5s) | L16 | khả năng cử động độc lập lệch pha nhau. Nghĩa là nửa móng bên trái có thể nâng cao lên ba mi-li-mét trong khi nửa móng bên phải hạ thấp xuống để thích ứng chính xác với độ mấp mô không đồng đều của mặt đá granite! Cơ chế vi chỉnh góc tiếp xúc này |  | Mô phỏng 3D hai nửa móng dịch chuyển so le: Một bên nhô cao, một bên thụt thấp bám theo gờ đá không đều. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này. |
| b06 | 00:49.9–00:56.7 (6.8s) | L17 | giúp phân bổ tải trọng đồng đều 100%, ngăn ngừa nguy cơ móng bị bẻ gãy khi tiếp đất với lực va đập lớn. Và hãy nhìn kỹ |  | Các mũi tên véc-tơ tải trọng chia đều một trăm phần trăm sang hai bên, bảo vệ móng không bị nứt vỡ. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này. |
| b07 | 00:56.7–01:04.4 (7.7s) | L18 | ra phía sau cổ chân: Dê núi còn sở hữu hai chiếc móng phụ thoái hóa nằm ở vị trí cao hơn, dân gian hay gọi là móng huyền. Đừng vội coi |  | Ống kính phóng to hai chiếc móng phụ móng huyền nằm phía sau cổ chân dê núi như móc câu sắt. chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ. |
| b08 | 01:04.4–01:13.4 (9.0s) | L19 | thường hai mẩu xương nhỏ bé này nhé! Khi con vật phải tụt dốc khẩn cấp hoặc sườn núi bị lở cát, hai chiếc móng phụ này sẽ cắm phập xuống lớp sỏi đá như một cặp mỏ neo phanh phụ |  | Cảnh chú dê núi trượt dốc trên đá lở và hai chiếc móng huyền lập tức cắm phập xuống đất làm phanh khẩn cấp. chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ. |
| b09 | 01:13.4–01:21.8 (8.4s) | L20 | trợ, dập tắt quán tính trượt dốc trong chớp mắt! Nhờ bộ móng kẹp hai tầng này, dù một con dê đực trưởng thành mang khối lượng cơ thể lên tới 140 kg, toàn |  | Biểu đồ cân nặng một trăm bốn mươi kilôgam của chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực dồn toàn bộ trọng lượng lên điểm tì nhỏ xíu. |
| b10 | 01:21.8–01:28.4 (6.6s) | L21 | bộ áp lực khổng lồ đó vẫn được truyền dẫn an toàn qua các điểm tiếp xúc tí hon chỉ bằng hạt đậu! Nhưng nếu chỉ có lớp vỏ sừng cứng cáp |  | Bản vẽ kỹ thuật mặt cắt ngang mô tả đường truyền lực xuyên qua các khớp ngón chân vững chãi. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này. |
| b11 | 01:28.4–01:32.6 (4.2s) | L22 | thì móng guốc vẫn có thể bị trượt khi gặp đá trơn bóng. Vì vậy, thiên nhiên đã lắp đặt |  | Mô phỏng hiện tượng móng sừng bị trượt trên đá ướt nếu thiếu đi độ bám dính của lớp vật liệu bên trong. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này. |
| b12 | 01:32.6–01:34.8 (2.2s) | L23 | thêm một vũ khí bí mật ngay trong lòng bàn chân! |  | Cánh cửa bí mật trong lòng bàn chân mở ra hé lộ lớp đệm thịt thần kỳ bước sang chương kế tiếp. chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ. |

### scene03 · ĐỆM CAO SU MA SÁT CAO BÁM DÍNH SIÊU CẤP · 86.6s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.2 (7.2s) | L24 | Nếu viền sừng bên ngoài đóng vai trò là chiếc kẹp cơ học sắc lẹm, thì phần ruột bên trong lòng móng lại là một kiệt tác vật liệu sinh học đàn hồi: |  | Hình ảnh đối lập viền sừng cứng cáp bao bọc lấy khối đệm thịt màu hồng xốp mềm mại bên trong. chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ. |
| b02 | 00:07.2–00:17.0 (9.8s) | L25 | Lớp đệm thịt ma sát bám dính siêu cấp! Nằm lọt giữa hai nửa móng guốc là một khối mô xốp hữu cơ mềm dẻo đặc biệt, có bề mặt sần sùi chứa hàng vạn vi rãnh siêu nhỏ đóng vai trò |  | Kính hiển vi soi rãnh vi mô trên bề mặt đệm chân với hàng ngàn giác hút chân không li ti. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này. |
| b03 | 00:17.0–00:29.4 (12.3s) | L26 | như các giác hút chân không tí hon! Mỗi khi móng chân ấn mạnh xuống phiến đá, khối đệm đàn hồi này sẽ lập tức biến dạng linh hoạt, lấp đầy mọi khe nứt vi mô trên mặt đá hoa cương, biến diện tích tiếp xúc từ một điểm nhỏ thành một bề mặt tì đè rộng lớn. Thử nghiệm |  | Hiệu ứng hoạt họa khối đệm mềm biến dạng đàn hồi lún sâu vào kẽ nứt li ti của phiến đá hoa cương. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này. |
| b04 | 00:29.4–00:41.4 (12.0s) | L27 | trong phòng thí nghiệm vật lý cho thấy: Hệ số ma sát tĩnh của lớp đệm thịt dê núi cao gấp 3 lần so với các loại đế cao su tổng hợp đắt giá nhất trang bị trên giày leo núi hiện đại của con người! Đặc tính đáng kinh ngạc nhất của vật liệu sinh học này chính là |  | Đồng hồ đo lực kế so sánh hệ số ma sát: Đế giày leo núi chỉ đạt một vạch trong khi đệm móng dê vọt lên ba vạch kịch kim. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này. |
| b05 | 00:41.4–00:49.5 (8.1s) | L28 | khả năng chịu nhiệt độ âm cực thấp. Trên đỉnh núi Rocky cao hàng ngàn mét, khi mùa đông gõ cửa khiến nhiệt độ tụt sâu xuống -30°C và băng giá phủ kín các vách đá, |  | Nhiệt kế thủy ngân tụt sâu xuống âm ba mươi độ giữa khung cảnh tuyết trắng rơi lất phất trên sườn núi. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này. |
| b06 | 00:49.5–00:55.8 (6.3s) | L29 | lốp xe cao su thông thường sẽ bị hóa cứng và trở nên giòn vụn, mất sạch độ bám. Nhưng lớp đệm của Vua Trọng Lực 90° |  | Lốp xe đua cao su bị đông cứng nứt toác dưới băng giá đối lập với đệm móng dê núi vẫn êm ái đàn hồi. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này. |
| b07 | 00:55.8–01:05.5 (9.7s) | L30 | vẫn giữ nguyên độ dẻo dai ấm áp, không hề đóng băng hay trơn trượt! Sự kết hợp ăn ý tuyệt đối giữa khung sừng cứng bên ngoài để móc vào gờ nứt và lõi đệm mềm bên trong để hút dính ma sát đã tạo |  | chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực bước đi tự tin trên mặt băng tuyết trơn trượt mà không hề có dấu hiệu loạng choạng. |
| b08 | 01:05.5–01:08.6 (3.1s) | L31 | nên một hợp kim cơ sinh học vô tiền khoáng hậu. Dù mặt |  | Sơ đồ hợp kim sinh học: Vỏ sừng cắm nứt cộng đệm mút hút dính tạo thành giác hút cơ học bất khả chiến bại. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này. |
| b09 | 01:08.6–01:11.1 (2.5s) | L32 | đá bị phủ một lớp rêu ướt trơn tuột như bôi mỡ, |  | Bàn chân dê dẫm lên tảng đá phủ rêu xanh ướt át nhưng dính chặt như có nam châm hút chặt. chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ. |
| b10 | 01:11.1–01:15.1 (4.0s) | L33 | bước chân của nó vẫn bám chặt như được gắn nam châm vĩnh cửu! Thế nhưng, |  | chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực đứng nghiêng người nhìn vào la bàn thăng bằng cơ thể đang nhấp nháy đèn xanh. |
| b11 | 01:15.1–01:19.3 (4.2s) | L34 | sở hữu bộ móng thần thánh thôi vẫn chưa đủ để chinh phục bức tường 90° nếu |  | Bản vẽ khung gầm giải phẫu học cơ thể dê núi với điểm trọng tâm màu đỏ rực rỡ chuẩn bị được phân tích. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này. |
| b12 | 01:19.3–01:26.6 (7.3s) | L35 | cơ thể thiếu đi một trung tâm điều khiển cân bằng hoàn hảo. Xin mời các bạn cùng tôi nâng tầng phân tích để khám phá hệ thống khung gầm của chú dê núi này! |  | Bác sĩ lật giở trang tài liệu thứ ba mô tả toàn bộ hệ thống khung gầm của bệnh nhân. chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ. |

### scene04 · TRỌNG TÂM CƠ THỂ SIÊU THẤP VÀ KHỚP BẢ VAI XOAY LINH HOẠT · 77.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:10.4 (10.4s) | L36 | Hãy tưởng tượng nếu một chú hươu cao cổ hay một vận động viên thể hình bình thường đứng tựa lưng vào vách đá dựng đứng: Trọng tâm cơ thể của họ nằm ở vị trí rất cao, cách xa điểm tựa mặt đất, tạo |  | Hình ảnh chú hươu cao cổ chân dài lêu nghêu cố leo vách đá và bị mất thăng bằng ngửa ra sau ngã nhào. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này. |
| b02 | 00:10.4–00:21.7 (11.3s) | L37 | ra một cánh tay đòn mô-men lật đổ cực kỳ nguy hiểm, chỉ cần gió thổi nhẹ một cơn là ngã ngửa xuống vực sâu ngay lập tức! Để hóa giải nghịch lý trọng lực này, tạo hóa đã thiết kế cho dê núi Bắc Mỹ một cấu trúc giải phẫu học độc nhất vô nhị: |  | Sơ đồ vật lý mô tả cánh tay đòn mô-men lật đổ khiến cơ thể cao kều dễ dàng bị lộn nhào xuống dốc. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này. |
| b03 | 00:21.7–00:27.7 (6.1s) | L38 | Đôi chân trước của chúng ngắn hơn đáng kể so với đôi chân sau, lồng ngực nở rộng vạm vỡ dẹp ngang ép sát vào bề mặt đá, |  | Bản vẽ giải phẫu dê núi với hai chân trước ngắn ngủn và lồng ngực vạm vỡ dẹp ngang áp sát vách đá. chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ. |
| b04 | 00:27.7–00:35.0 (7.3s) | L39 | và toàn bộ khối lượng nội tạng nặng nề được dồn tụ xuống phần thân trước sát mặt đất! Cấu tạo này kéo hạ thấp trọng tâm toàn bộ cơ thể xuống mức tối đa, |  | Khối lượng bên trong cơ thể được bố trí khoa học sát phần ngực dưới giúp trọng tâm rơi thẳng vào đế chân. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này. |
| b05 | 00:35.0–00:41.5 (6.4s) | L40 | dán chặt véc-tơ trọng lực vào lòng vách núi thay vì đẩy ra ngoài không trung. Khi đứng trên sườn dốc nghiêng 80°, cơ thể chú |  | Véc-tơ trọng lực màu đỏ từ tâm cơ thể chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực cắm thẳng vào tâm phiến đá thay vì hướng ra ngoài vực. |
| b06 | 00:41.5–00:48.6 (7.1s) | L41 | dê nghiêng nhẹ về phía vách đá, triệt tiêu hoàn toàn lực lật đổ, biến vách đá cheo leo thành chiếc giường tựa vững như bàn thạch! Đặc biệt, |  | chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực nghiêng nhẹ góc thân mình ép sát vách đá, tạo tư thế thăng bằng vững như một tảng đá nguyên khối. |
| b07 | 00:48.6–00:55.5 (6.8s) | L42 | khớp xương bả vai của dê núi sở hữu biên độ tự do xoay chuyển ngang rộng hơn bất kỳ loài thú móng guốc nào khác. Hai chân trước của nó có |  | Mô hình khớp bả vai xoay linh hoạt ba trăm sáu mươi độ với hệ thống dây chằng co giãn phi thường. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này. |
| b08 | 00:55.5–01:01.0 (5.5s) | L43 | thể dang rộng sang hai bên như hai cánh tay người, ôm lấy những khối đá lồi để giữ thăng bằng và kéo toàn bộ |  | chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực dang rộng hai chân trước bám lấy hai mỏm đá hai bên như vận động viên đang đu xà đơn. |
| b09 | 01:01.0–01:06.1 (5.1s) | L44 | cơ thể nặng hơn một tạ trèo lên gờ đá cao hơn một cách nhẹ nhàng như tập xà đơn! Chẳng |  | Khối cơ bắp vai cuồn cuộn gồng lên nhấc bổng toàn bộ thân hình nặng nề lên gờ đá cao một cách ngoạn mục. chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ. |
| b10 | 01:06.1–01:15.7 (9.6s) | L45 | có một cỗ máy việt dã bánh xích nào của con người có thể điều chỉnh trọng tâm linh hoạt đến mức ấy. Và khi đã đạt đến đỉnh cao của sự thăng bằng tĩnh, chú dê núi bắt đầu phô diễn tuyệt kỹ chuyển động đỉnh cao nhất: |  | Hình ảnh chiếc xe địa hình bánh xích leo dốc bị lật nghiêng đối lập với chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực bước thoăn thoắt. |
| b11 | 01:15.7–01:17.9 (2.2s) | L46 | Kỹ thuật parkour búng tường giữa tầng không! |  | chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực nhún người nén đôi chân sau như một bệ phóng tên lửa chuẩn bị khai hỏa màn parkour đỉnh cao. |

### scene05 · CÚ NHẢY BÚNG TƯỜNG NGOẠN MỤC XOAY NGƯỜI GIỮA KHÔNG TRUNG · 92.2s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:13.1 (13.1s) | L47 | Đỉnh cao nghệ thuật sinh tồn của Vua Trọng Lực 90° chỉ thực sự phát hỏa rực rỡ nhất khi nó dồn mình vào bước đường cùng: Trước mặt là vách đá nhẵn thín không còn một gờ nứt nào để tiến bước, bên dưới là vực sâu ngàn trượng, và phía sau có thể là |  | chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực đứng trước ngõ cụt: Vách đá phẳng lì phía trước, vực sâu bên dưới, ánh mắt lóe lên sự tự tin. |
| b02 | 00:13.1–00:27.4 (14.3s) | L48 | một con báo sư tử đang rình rập săn mồi! Đối với mọi sinh vật khác, đây là bản án tử hình chắc chắn. Nhưng đối với dê núi, đây lại là thời khắc bắt đầu của màn trình diễn nhào lộn kinh điển! Chẳng hề do dự hay run rẩy, nó dồn toàn bộ sức |  | Bóng đen của con báo sư tử rình mò từ trên đỉnh dốc nghĩ rằng con mồi đã cùng đường. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này. |
| b03 | 00:27.4–00:31.8 (4.4s) | L49 | nén vào đôi chân sau hoạt động như cặp lò xo giảm xóc cỡ lớn, tung mình nhảy vọt ra khỏi gờ |  | chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực co gập đôi chân sau nén tối đa lò xo cơ bắp, chuẩn bị bung mình vào không trung. |
| b04 | 00:31.8–00:39.4 (7.6s) | L50 | đá bay ngang qua hẻm vực sâu thăm thẳm sang bức tường đá đối diện cách xa tới 4m! Ngay khi chạm vào mặt đá thẳng đứng bên kia, nó không hề tìm cách bám lại để dừng rơi mà |  | Cú nhảy phi thân ngang qua khoảng không vực sâu bốn mét giữa hai bức tường đá song song. chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ. |
| b05 | 00:39.4–00:44.4 (4.9s) | L51 | lập tức dùng cả bốn móng guốc đạp mạnh vào vách đá như một vận động viên parkour, búng ngược cơ thể trở lại bức tường ban |  | Bốn móng guốc chạm vào mặt đá đối diện, tạo phản lực cực đại để búng ngược trở lại bức tường cũ. chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ. |
| b06 | 00:44.4–00:48.4 (4.1s) | L52 | đầu ở một độ cao vượt trội hơn! Thưa Giáo sư, một cú nhào |  | Quỹ đạo đường bay hình chữ Z đưa chú dê vọt lên vị trí cao hơn năm mét chỉ sau một cú búng tường. chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ. |
| b07 | 00:48.4–00:59.4 (11.0s) | L53 | lộn xoay người 180° giữa khoảng không vực thẳm như vậy đòi hỏi thời gian xử lý não bộ và phản xạ cơ bắp nhanh đến mức nào ạ? Toàn bộ cú búng tường xoay trục 180° ấy diễn |  | Chú thỏ tuyết trợ lý tròn mắt kinh ngạc cầm đồng hồ bấm giây ghi nhận kỷ lục tốc độ phản xạ. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này. |
| b08 | 00:59.4–01:03.0 (3.6s) | L54 | ra trong vỏn vẹn chưa đầy nửa giây thưa bạn trẻ! Các xung thần kinh từ thị |  | Đồng hồ chỉ mốc không phẩy bốn giây với hình bóng chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực xoay người uyển chuyển giữa trời tuyết. |
| b09 | 01:03.0–01:12.4 (9.4s) | L55 | giác truyền thẳng về tiểu não khổng lồ để tính toán véc-tơ phản lực và điều chỉnh góc xòe của móng guốc với độ chính xác tuyệt đối. Bằng chuỗi động tác búng tường zig-zag liên hồi, nó |  | Sơ đồ đường truyền thần kinh từ mắt đến tiểu não xử lý thuật toán quỹ đạo bay trong chớp mắt. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này. |
| b10 | 01:12.4–01:23.1 (10.7s) | L56 | có thể thăng tiến hàng chục mét vách đá dốc đứng chỉ trong vài giây ngắn ngủi, bỏ xa mọi kẻ săn mồi mặt đất đang run rẩy đứng nhìn dưới chân dốc! Kẻ săn mồi dù dũng mãnh và nhanh nhẹn đến đâu cũng chỉ |  | Hình ảnh liên hoàn ba cú nhảy búng tường hình chữ chi đưa chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực bay vút lên đỉnh núi lộng gió. |
| b11 | 01:23.1–01:30.0 (6.9s) | L57 | biết há hốc mồm bất lực trước bản lĩnh không gian ba chiều của chú dê núi tuyết. Nơi mà người ta nhìn thấy thần chết rình rập, sinh vật này lại tìm |  | Báo sư tử đứng trơ trọi bên bờ vực, mắt trợn tròn nhìn chú dê đã an tọa trên đỉnh mỏm đá cao vẫy đuôi. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này. |
| b12 | 01:30.0–01:32.2 (2.2s) | L58 | thấy một sân chơi tự do và bình yên tuyệt đối! |  | chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực đứng sừng sững trên đỉnh cao tuyết trắng, ánh hoàng hôn chiếu rọi hào quang kiêu hãnh. |

### scene06 · ĐỈNH CAO THỂ THAO MẠO HIỂM PHỎNG SINH HỌC · 80.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:05.1 (5.1s) | L59 | Kính thưa toàn thể quý khán giả và các nhà khoa học theo dõi buổi tổng kết, sau khi thẩm định chi |  | Hội đồng giám khảo gồm các con vật trao cúp vàng và huy chương vàng danh dự cho chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực. |
| b02 | 00:05.1–00:15.7 (10.6s) | L60 | tiết toàn bộ bốn tuyệt kỹ cơ học từ móng chẻ thủy lực kẹp đá, đệm cao su ma sát siêu bám, trọng tâm cơ thể hạ thấp ép sát vách cho đến cú búng tường zig-zag thần sầu, ban giám khảo nhất trí tuyệt đối trao |  | Tóm tắt bốn biểu tượng trên bảng xếp hạng: Móng kẹp, đệm ma sát, trọng tâm thấp, cú búng tường. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này. |
| b03 | 00:15.7–00:28.7 (13.0s) | L61 | tấm Huy chương Vàng Cơ Học Vách Đá cho Dê Núi Bắc Mỹ! Sinh vật kiệt xuất này ngày nay chính là nguồn cảm hứng vàng ngọc cho các kỹ sư nghiên cứu robot địa hình của cơ quan hàng không vũ trụ NASA nhằm chế tạo các cánh tay bám kẹp cơ học phục vụ thám hiểm |  | Bản thiết kế robot thám hiểm đa địa hình của NASA với chân mô phỏng móng dê leo vách đá Sao Hỏa. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này. |
| b04 | 00:28.7–00:36.6 (7.9s) | L62 | các hẻm vực dốc đứng trên Sao Hỏa và Mặt Trăng. Các thương hiệu thể thao dã ngoại danh tiếng cũng đang nghiên cứu mô phỏng lớp đệm thịt đàn hồi của móng dê để phát |  | Robot vũ trụ bám chặt vào miệng núi lửa trên Mặt Trăng nhờ cơ cấu móng kẹp phỏng sinh học. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này. |
| b05 | 00:36.6–00:44.9 (8.3s) | L63 | triển thế hệ giày leo núi siêu ma sát cho thế kỷ 21. Bài học sinh tồn từ chú dê núi trên vách đá cheo leo nhắc nhở mỗi chúng ta rằng: Khi đối diện |  | Phòng thiết kế giày leo núi với mẫu đế cao su mô phỏng vi rãnh đệm chân dê núi Bắc Mỹ. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này. |
| b06 | 00:44.9–00:48.9 (4.1s) | L64 | với những thử thách dựng đứng tưởng chừng như không thể vượt qua trong cuộc sống, việc tìm kiếm |  | Hình ảnh ẩn dụ: Con người kiên cường vượt qua các rào cản vách đá thử thách trong công việc và cuộc sống. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này. |
| b07 | 00:48.9–00:56.3 (7.4s) | L65 | những điểm tựa vững chắc dù là nhỏ bé nhất, cùng một tinh thần thăng bằng kiên định, sẽ giúp chúng ta đứng vững và vươn lên đỉnh vinh quang! Giữa |  | Ngọn hải đăng niềm tin soi sáng con đường vươn tới đỉnh cao vinh quang và tự do. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này. |
| b08 | 00:56.3–01:04.2 (7.8s) | L66 | bộ móng chẻ kìm bấm thủy lực và lớp đệm ma sát siêu cấp, cơ chế cơ sinh học nào của Vua Trọng Lực 90° khiến bạn kinh ngạc và thán phục nhất? |  | Khung hình so sánh hai phát minh sinh học kèm dấu chấm hỏi lớn mời gọi khán giả bình luận. chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ. |
| b09 | 01:04.2–01:08.7 (4.5s) | L67 | Hãy để lại cảm nghĩ và bình luận tâm đắc của bạn ngay bên dưới video này nhé! Và đừng |  | Biểu tượng hộp bình luận tương tác vui nhộn xuất hiện cùng chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực nháy mắt tinh nghịch. |
| b10 | 01:08.7–01:11.2 (2.5s) | L68 | quên nhấn nút Đăng Ký Kênh cùng chiếc chuông thông báo để đón |  | Ngón tay hoạt hình bấm nút Subscribe đỏ rực và rung chiếc chuông vàng thông báo. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này. |
| b11 | 01:11.2–01:14.1 (2.9s) | L69 | xem Tập 39: Giải mã sát thủ ngây thơ giấu |  | Hình ảnh teaser nhá hàng bóng đen bí ẩn và cành gai treo mồi của Chim Bách Thanh tập sau. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này. |
| b12 | 01:14.1–01:20.7 (6.6s) | L70 | mặt của Chim Bách Thanh! Xin chào tạm biệt và hẹn gặp lại toàn thể các bạn trong những hành trình khám phá thiên nhiên kỳ thú tiếp theo! |  | chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực vẫy tay chào tạm biệt khán giả giữa khung cảnh núi tuyết Rocky lấp lánh nắng mai. |

## 5. Phân cảnh Shorts — từng beat

Banner: **VUA TRỌNG LỰC 90 ĐỘ / BÍ KÍP VÁCH ĐÁ TỬ THẦN?!** · giọng 43.8s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Bạn có tin trên Trái Đất có một loài động vật nặng tới 140 kg nhưng có |  |
| s02 | 00:05.0 | S02 | thể đứng vững trên vách đá dựng đứng 90° nhẵn thín không? |  |
| s03 | 00:09.4 | S03 | Đó chính là Dê Núi Bắc Mỹ — Vua Trọng Lực 90° vô địch thiên nhiên! Bí mật chấn động nằm |  |
| s04 | 00:14.7 | S04 | ở bộ móng guốc chẻ đôi kẹp gờ đá như kìm bấm thủy lực, |  |
| s05 | 00:17.6 | S05 | kết hợp cùng lớp đệm thịt cao su ma sát cực đại có độ bám |  |
| s06 | 00:20.8 | S06 | dính gấp 3 lần đế giày leo núi chuyên nghiệp! |  |
| s07 | 00:24.0 | S07 | Khi gặp ngõ cụt giữa vực sâu ngàn mét, nó có thể tung |  |
| s08 | 00:27.1 | S08 | mình nhảy xa 4m và |  |
| s09 | 00:28.6 | S09 | búng tường xoay người 180° |  |
| s10 | 00:30.5 | S10 | chỉ trong nửa giây! Thậm chí, loài dê này còn thong |  |
| s11 | 00:34.9 | S11 | dong leo thẳng lên các bức tường đập thủy điện dốc đứng cao hàng trăm mét chỉ để liếm từng vệt muối khoáng! |  |
| s12 | 00:39.9 | S12 | Quả là bậc thầy khinh công thách thức mọi định luật vật lý của Newton! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chào mừng toàn thể các vận động viên leo núi, các chuyên gia cơ học chuyển động và các bạn đam mê khoa học sinh thái bước vào Đấu trường vách đá tử thần trên dãy núi Rocky hùng vĩ! Hôm nay,". Bố cục: Toàn cảnh vách đá tuyết Rocky: chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực đứng trên đỉnh núi tuyết, giơ tay chào khán giả với kính bảo hộ tuyết màu cam viền titan.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "phòng thí nghiệm cơ sinh học dã ngoại của chúng tôi xin trân trọng giới thiệu một cỗ máy tự nhiên kỳ dị bậc nhất hành tinh, kẻ biến những định luật vạn vật hấp dẫn của ngài Isaac Newton thành một màn giải trí ngoạn mục! Trước ống kính viễn vọng của chúng ta là một". Bố cục: Mô hình bàn vẽ sổ tay ký họa với sơ đồ cơ sinh học và quả táo rơi của Isaac Newton bị chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực gạt phắt sang một bên.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bức tường đá hoa cương granite dựng đứng 90°, nhẵn thín và lạnh lẽo, cao chót vót 4.000m giữa tầng mây trắng xóa. Phía dưới chân vách đá là". Bố cục: Toàn cảnh vách đá hoa cương granite thẳng đứng chín mươi độ cao bốn ngàn mét giữa mây trời lộng gió. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "vực sâu thăm thẳm không đáy, nơi mà chỉ một cú trượt chân bằng nửa hạt cát cũng đủ khiến bất kỳ sinh vật to lớn nào rơi vào thảm kịch! Thế nhưng hãy phóng to ống kính lên". Bố cục: Góc nhìn từ trên xuống vực sâu hun hút thăm thẳm với những tầng mây trôi bồng bềnh dưới chân. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "mỏm đá nhọn hoắt kia: Một bóng dáng trắng muốt như tuyết đang ung dung gặm rêu cỏ, đứng vững vàng trên một gờ đá hẹp chưa đầy 2cm! Thưa Giáo sư phụ trách,". Bố cục: Khung cảnh zoom cận cảnh: chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực đứng thăng bằng điềm nhiên trên một gờ đá hẹp chỉ bằng hai xăng-ti-mét.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "trạm đo laser địa hình ghi nhận độ dốc sườn núi tại vị trí con vật đang đứng đạt tới 89°, gần như song song hoàn hảo với dây dọi thẳng đứng mà không hề có dây thừng trợ lực! Một". Bố cục: Chú sóc tuyết cầm máy đo khoảng cách laser chiếu tia đỏ quét góc dốc tám mươi chín độ của vách đá. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "kết quả đo đạc chính xác đến từng mi-crô-mét thưa phát thanh viên hiện trường! Đối tượng nghiên cứu lừng danh này mang danh pháp khoa học Oreamnos americanus, nhưng toàn thể cộng đồng leo núi thế giới đều nghiêng mình gọi nó bằng danh hiệu kiệt xuất: Vua Trọng Lực 90°!". Bố cục: Tấm huy hiệu vinh danh danh pháp khoa học Oreamnos americanus cùng dòng chữ phong tặng danh hiệu Vua Trọng Lực. chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ.
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trong khi các kiện tướng thể thao đỉnh cao của loài người phải nai nịt giày đinh đặc chế, dây bảo hiểm chuyên dụng, móc treo carabiner và thoa đầy bột chống trơn mới dám mon men leo dốc, thì chú dê núi này chỉ dựa vào bốn chiếc móng guốc bẩm sinh để". Bố cục: Hình ảnh so sánh: Vận động viên leo núi đeo lỉnh kỉnh dây dù móc sắt thở dốc đối lập với chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực đi dạo thanh thản.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "biến bức tường tử thần thành đường tản bộ êm ái! Không chỉ đứng yên một chỗ, sinh vật này còn có thể chạy nước rút, xoay xở chuyển hướng và thậm chí". Bố cục: Bản vẽ động tác chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực phi nước kiệu nhẹ nhàng băng qua khe nứt hiểm trở trên sườn dốc tuyết.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "phóng mình qua các hố sụt chết chóc với phong thái thong dong như đang dạo chơi công viên! Đằng sau vẻ ngoài điềm tĩnh tựa một thiền sư trên đỉnh núi tuyết là hàng triệu năm tiến hóa khắc nghiệt đã tôi luyện nên một hệ thống khung gầm cơ khí hoàn hảo đến từng chi tiết.". Bố cục: Sơ đồ tiến hóa hàng triệu năm với bộ khung xương vững chãi tôi luyện qua băng giá kỷ băng hà. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bí mật vật lý và sinh học nào đã biến Vua Trọng Lực 90° thành kẻ cai trị tuyệt đối của những vách đá dựng đứng? Ngay bây giờ, xin mời quý vị cùng tôi mở hòm hồ sơ kỹ thuật tầng một để giải phẫu vũ khí kẹp đá đầu tiên mang tên bộ móng thủy lực!". Bố cục: Bàn tay bác sĩ lật mở cuốn hồ sơ bệnh án ký họa mở màn cho chương giải phẫu đầu tiên. chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Xin mời các kỹ sư cơ khí hãy zoom cận cảnh vào bộ phận tiếp xúc tiền tuyến của cỗ máy vượt dốc: Bộ móng guốc chẻ đôi kỳ ảo! Khác biệt hoàn toàn với". Bố cục: Kính lúp phóng to bộ móng guốc chẻ đôi kỳ lạ của chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực đang tiếp xúc với mặt đá nứt nẻ.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "móng ngựa là một khối sừng liền mạch tròn xoe rất dễ trượt té khi gặp đá nghiêng, bàn chân của Vua Trọng Lực 90° được xẻ đôi thành hai nửa móng guốc riêng biệt, vận hành tự chủ tựa như hai ngón tay kìm bấm thủy lực cực kỳ linh hoạt! Mỗi nửa móng guốc được bao bọc bởi một". Bố cục: Hình ảnh so sánh móng ngựa tròn trơn trượt ngã nhào đối lập với móng dê núi chẻ đôi kẹp chặt như kìm bấm. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "lớp vỏ sừng chất đạm keratin cứng như thép tôi và sắc bén như lưỡi rìu đẽo đá. Khi bàn chân giẫm xuống bề mặt gồ ghề, hai nửa móng này lập tức". Bố cục: Cấu trúc vỏ sừng keratin cứng như thép tôi của móng guốc với lát cắt hiển vi phân tử đạm siêu bền. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "xòe rộng ra theo hình chữ V để bao trọn lấy gờ đá, sau đó các bó gân gập ngón sẽ siết chặt hai nửa móng lại, khóa chặt điểm tì như gọng kìm kẹp ốc vít! Chưa dừng lại ở đó, hai nửa móng này còn có khả năng". Bố cục: Sơ đồ lực học hai nửa móng xòe rộng thành hình chữ V ôm trọn mỏm đá nhọn rồi siết chặt lại. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "cử động độc lập lệch pha nhau. Nghĩa là nửa móng bên trái có thể nâng cao lên ba mi-li-mét trong khi nửa móng bên phải hạ thấp xuống để thích ứng chính xác với độ mấp mô không đồng đều của mặt đá granite! Cơ chế vi chỉnh góc tiếp xúc này giúp". Bố cục: Mô phỏng 3D hai nửa móng dịch chuyển so le: Một bên nhô cao, một bên thụt thấp bám theo gờ đá không đều. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "phân bổ tải trọng đồng đều 100%, ngăn ngừa nguy cơ móng bị bẻ gãy khi tiếp đất với lực va đập lớn. Và hãy nhìn kỹ ra". Bố cục: Các mũi tên véc-tơ tải trọng chia đều một trăm phần trăm sang hai bên, bảo vệ móng không bị nứt vỡ. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "phía sau cổ chân: Dê núi còn sở hữu hai chiếc móng phụ thoái hóa nằm ở vị trí cao hơn, dân gian hay gọi là móng huyền. Đừng vội coi thường hai". Bố cục: Ống kính phóng to hai chiếc móng phụ móng huyền nằm phía sau cổ chân dê núi như móc câu sắt. chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "mẩu xương nhỏ bé này nhé! Khi con vật phải tụt dốc khẩn cấp hoặc sườn núi bị lở cát, hai chiếc móng phụ này sẽ cắm phập xuống lớp sỏi đá như một cặp mỏ neo phanh phụ trợ,". Bố cục: Cảnh chú dê núi trượt dốc trên đá lở và hai chiếc móng huyền lập tức cắm phập xuống đất làm phanh khẩn cấp. chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "dập tắt quán tính trượt dốc trong chớp mắt! Nhờ bộ móng kẹp hai tầng này, dù một con dê đực trưởng thành mang khối lượng cơ thể lên tới 140 kg, toàn bộ". Bố cục: Biểu đồ cân nặng một trăm bốn mươi kilôgam của chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực dồn toàn bộ trọng lượng lên điểm tì nhỏ xíu.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "áp lực khổng lồ đó vẫn được truyền dẫn an toàn qua các điểm tiếp xúc tí hon chỉ bằng hạt đậu! Nhưng nếu chỉ có lớp vỏ sừng cứng cáp thì". Bố cục: Bản vẽ kỹ thuật mặt cắt ngang mô tả đường truyền lực xuyên qua các khớp ngón chân vững chãi. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "móng guốc vẫn có thể bị trượt khi gặp đá trơn bóng. Vì vậy, thiên nhiên đã lắp đặt thêm một". Bố cục: Mô phỏng hiện tượng móng sừng bị trượt trên đá ướt nếu thiếu đi độ bám dính của lớp vật liệu bên trong. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "vũ khí bí mật ngay trong lòng bàn chân!". Bố cục: Cánh cửa bí mật trong lòng bàn chân mở ra hé lộ lớp đệm thịt thần kỳ bước sang chương kế tiếp. chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Nếu viền sừng bên ngoài đóng vai trò là chiếc kẹp cơ học sắc lẹm, thì phần ruột bên trong lòng móng lại là một kiệt tác vật liệu sinh học đàn hồi:". Bố cục: Hình ảnh đối lập viền sừng cứng cáp bao bọc lấy khối đệm thịt màu hồng xốp mềm mại bên trong. chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Lớp đệm thịt ma sát bám dính siêu cấp! Nằm lọt giữa hai nửa móng guốc là một khối mô xốp hữu cơ mềm dẻo đặc biệt, có bề mặt sần sùi chứa hàng vạn vi rãnh siêu nhỏ đóng vai trò như các". Bố cục: Kính hiển vi soi rãnh vi mô trên bề mặt đệm chân với hàng ngàn giác hút chân không li ti. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "giác hút chân không tí hon! Mỗi khi móng chân ấn mạnh xuống phiến đá, khối đệm đàn hồi này sẽ lập tức biến dạng linh hoạt, lấp đầy mọi khe nứt vi mô trên mặt đá hoa cương, biến diện tích tiếp xúc từ một điểm nhỏ thành một bề mặt tì đè rộng lớn. Thử nghiệm trong". Bố cục: Hiệu ứng hoạt họa khối đệm mềm biến dạng đàn hồi lún sâu vào kẽ nứt li ti của phiến đá hoa cương. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này.
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "phòng thí nghiệm vật lý cho thấy: Hệ số ma sát tĩnh của lớp đệm thịt dê núi cao gấp 3 lần so với các loại đế cao su tổng hợp đắt giá nhất trang bị trên giày leo núi hiện đại của con người! Đặc tính đáng kinh ngạc nhất của vật liệu sinh học này chính là khả năng". Bố cục: Đồng hồ đo lực kế so sánh hệ số ma sát: Đế giày leo núi chỉ đạt một vạch trong khi đệm móng dê vọt lên ba vạch kịch kim. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chịu nhiệt độ âm cực thấp. Trên đỉnh núi Rocky cao hàng ngàn mét, khi mùa đông gõ cửa khiến nhiệt độ tụt sâu xuống -30°C và băng giá phủ kín các vách đá,". Bố cục: Nhiệt kế thủy ngân tụt sâu xuống âm ba mươi độ giữa khung cảnh tuyết trắng rơi lất phất trên sườn núi. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "lốp xe cao su thông thường sẽ bị hóa cứng và trở nên giòn vụn, mất sạch độ bám. Nhưng lớp đệm của Vua Trọng Lực 90° vẫn". Bố cục: Lốp xe đua cao su bị đông cứng nứt toác dưới băng giá đối lập với đệm móng dê núi vẫn êm ái đàn hồi. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "giữ nguyên độ dẻo dai ấm áp, không hề đóng băng hay trơn trượt! Sự kết hợp ăn ý tuyệt đối giữa khung sừng cứng bên ngoài để móc vào gờ nứt và lõi đệm mềm bên trong để hút dính ma sát đã tạo nên một". Bố cục: chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực bước đi tự tin trên mặt băng tuyết trơn trượt mà không hề có dấu hiệu loạng choạng.
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "hợp kim cơ sinh học vô tiền khoáng hậu. Dù mặt đá bị". Bố cục: Sơ đồ hợp kim sinh học: Vỏ sừng cắm nứt cộng đệm mút hút dính tạo thành giác hút cơ học bất khả chiến bại. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này.
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "phủ một lớp rêu ướt trơn tuột như bôi mỡ,". Bố cục: Bàn chân dê dẫm lên tảng đá phủ rêu xanh ướt át nhưng dính chặt như có nam châm hút chặt. chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bước chân của nó vẫn bám chặt như được gắn nam châm vĩnh cửu! Thế nhưng,". Bố cục: chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực đứng nghiêng người nhìn vào la bàn thăng bằng cơ thể đang nhấp nháy đèn xanh.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "sở hữu bộ móng thần thánh thôi vẫn chưa đủ để chinh phục bức tường 90° nếu cơ thể". Bố cục: Bản vẽ khung gầm giải phẫu học cơ thể dê núi với điểm trọng tâm màu đỏ rực rỡ chuẩn bị được phân tích. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "thiếu đi một trung tâm điều khiển cân bằng hoàn hảo. Xin mời các bạn cùng tôi nâng tầng phân tích để khám phá hệ thống khung gầm của chú dê núi này!". Bố cục: Bác sĩ lật giở trang tài liệu thứ ba mô tả toàn bộ hệ thống khung gầm của bệnh nhân. chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ.
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Hãy tưởng tượng nếu một chú hươu cao cổ hay một vận động viên thể hình bình thường đứng tựa lưng vào vách đá dựng đứng: Trọng tâm cơ thể của họ nằm ở vị trí rất cao, cách xa điểm tựa mặt đất, tạo ra một". Bố cục: Hình ảnh chú hươu cao cổ chân dài lêu nghêu cố leo vách đá và bị mất thăng bằng ngửa ra sau ngã nhào. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "cánh tay đòn mô-men lật đổ cực kỳ nguy hiểm, chỉ cần gió thổi nhẹ một cơn là ngã ngửa xuống vực sâu ngay lập tức! Để hóa giải nghịch lý trọng lực này, tạo hóa đã thiết kế cho dê núi Bắc Mỹ một cấu trúc giải phẫu học độc nhất vô nhị:". Bố cục: Sơ đồ vật lý mô tả cánh tay đòn mô-men lật đổ khiến cơ thể cao kều dễ dàng bị lộn nhào xuống dốc. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này.
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đôi chân trước của chúng ngắn hơn đáng kể so với đôi chân sau, lồng ngực nở rộng vạm vỡ dẹp ngang ép sát vào bề mặt đá, và". Bố cục: Bản vẽ giải phẫu dê núi với hai chân trước ngắn ngủn và lồng ngực vạm vỡ dẹp ngang áp sát vách đá. chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "toàn bộ khối lượng bên trong cơ thể nặng nề được dồn tụ xuống phần thân trước sát mặt đất! Cấu tạo này kéo hạ thấp trọng tâm toàn bộ cơ thể xuống mức tối đa,". Bố cục: Khối lượng bên trong cơ thể được bố trí khoa học sát phần ngực dưới giúp trọng tâm rơi thẳng vào đế chân. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này.
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "dán chặt véc-tơ trọng lực vào lòng vách núi thay vì đẩy ra ngoài không trung. Khi đứng trên sườn dốc nghiêng 80°, cơ thể chú dê". Bố cục: Véc-tơ trọng lực màu đỏ từ tâm cơ thể chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực cắm thẳng vào tâm phiến đá thay vì hướng ra ngoài vực.
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nghiêng nhẹ về phía vách đá, triệt tiêu hoàn toàn lực lật đổ, biến vách đá cheo leo thành chiếc giường tựa vững như bàn thạch! Đặc biệt,". Bố cục: chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực nghiêng nhẹ góc thân mình ép sát vách đá, tạo tư thế thăng bằng vững như một tảng đá nguyên khối.
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "khớp xương bả vai của dê núi sở hữu biên độ tự do xoay chuyển ngang rộng hơn bất kỳ loài thú móng guốc nào khác. Hai chân trước của nó có thể". Bố cục: Mô hình khớp bả vai xoay linh hoạt ba trăm sáu mươi độ với hệ thống dây chằng co giãn phi thường. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này.
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "dang rộng sang hai bên như hai cánh tay người, ôm lấy những khối đá lồi để giữ thăng bằng và kéo toàn bộ cơ thể". Bố cục: chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực dang rộng hai chân trước bám lấy hai mỏm đá hai bên như vận động viên đang đu xà đơn.
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nặng hơn một tạ trèo lên gờ đá cao hơn một cách nhẹ nhàng như tập xà đơn! Chẳng có một". Bố cục: Khối cơ bắp vai cuồn cuộn gồng lên nhấc bổng toàn bộ thân hình nặng nề lên gờ đá cao một cách ngoạn mục. chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ.
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "cỗ máy việt dã bánh xích nào của con người có thể điều chỉnh trọng tâm linh hoạt đến mức ấy. Và khi đã đạt đến đỉnh cao của sự thăng bằng tĩnh, chú dê núi bắt đầu phô diễn tuyệt kỹ chuyển động đỉnh cao nhất:". Bố cục: Hình ảnh chiếc xe địa hình bánh xích leo dốc bị lật nghiêng đối lập với chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực bước thoăn thoắt.
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kỹ thuật parkour búng tường giữa tầng không!". Bố cục: chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực nhún người nén đôi chân sau như một bệ phóng tên lửa chuẩn bị khai hỏa màn parkour đỉnh cao.
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đỉnh cao nghệ thuật sinh tồn của Vua Trọng Lực 90° chỉ thực sự phát hỏa rực rỡ nhất khi nó dồn mình vào bước đường cùng: Trước mặt là vách đá nhẵn thín không còn một gờ nứt nào để tiến bước, bên dưới là vực sâu ngàn trượng, và phía sau có thể là một con". Bố cục: chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực đứng trước ngõ cụt: Vách đá phẳng lì phía trước, vực sâu bên dưới, ánh mắt lóe lên sự tự tin.
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "báo sư tử đang rình rập săn mồi! Đối với mọi sinh vật khác, đây là bản án tử hình chắc chắn. Nhưng đối với dê núi, đây lại là thời khắc bắt đầu của màn trình diễn nhào lộn kinh điển! Chẳng hề do dự hay run rẩy, nó dồn toàn bộ sức nén vào". Bố cục: Bóng đen của con báo sư tử rình mò từ trên đỉnh dốc nghĩ rằng con mồi đã cùng đường. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này.
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "đôi chân sau hoạt động như cặp lò xo giảm xóc cỡ lớn, tung mình nhảy vọt ra khỏi gờ đá". Bố cục: chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực co gập đôi chân sau nén tối đa lò xo cơ bắp, chuẩn bị bung mình vào không trung.
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bay ngang qua hẻm vực sâu thăm thẳm sang bức tường đá đối diện cách xa tới 4m! Ngay khi chạm vào mặt đá thẳng đứng bên kia, nó không hề tìm cách bám lại để dừng rơi mà lập tức". Bố cục: Cú nhảy phi thân ngang qua khoảng không vực sâu bốn mét giữa hai bức tường đá song song. chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ.
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "dùng cả bốn móng guốc đạp mạnh vào vách đá như một vận động viên parkour, búng ngược cơ thể trở lại bức tường ban đầu". Bố cục: Bốn móng guốc chạm vào mặt đá đối diện, tạo phản lực cực đại để búng ngược trở lại bức tường cũ. chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ.
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "ở một độ cao vượt trội hơn! Thưa Giáo sư, một cú nhào lộn". Bố cục: Quỹ đạo đường bay hình chữ Z đưa chú dê vọt lên vị trí cao hơn năm mét chỉ sau một cú búng tường. chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "xoay người 180° giữa khoảng không vực thẳm như vậy đòi hỏi thời gian xử lý não bộ và phản xạ cơ bắp nhanh đến mức nào ạ? Toàn bộ cú búng tường xoay trục 180° ấy diễn ra trong". Bố cục: Chú thỏ tuyết trợ lý tròn mắt kinh ngạc cầm đồng hồ bấm giây ghi nhận kỷ lục tốc độ phản xạ. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này.
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "vỏn vẹn chưa đầy nửa giây thưa bạn trẻ! Các xung thần kinh từ thị giác". Bố cục: Đồng hồ chỉ mốc không phẩy bốn giây với hình bóng chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực xoay người uyển chuyển giữa trời tuyết.
```
</details>

<details><summary>L55</summary>

```text
HÌNH L55 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "truyền thẳng về tiểu não khổng lồ để tính toán véc-tơ phản lực và điều chỉnh góc xòe của móng guốc với độ chính xác tuyệt đối. Bằng chuỗi động tác búng tường zig-zag liên hồi, nó có thể". Bố cục: Sơ đồ đường truyền thần kinh từ mắt đến tiểu não xử lý thuật toán quỹ đạo bay trong chớp mắt. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này.
```
</details>

<details><summary>L56</summary>

```text
HÌNH L56 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "thăng tiến hàng chục mét vách đá dốc đứng chỉ trong vài giây ngắn ngủi, bỏ xa mọi kẻ săn mồi mặt đất đang run rẩy đứng nhìn dưới chân dốc! Kẻ săn mồi dù dũng mãnh và nhanh nhẹn đến đâu cũng chỉ biết". Bố cục: Hình ảnh liên hoàn ba cú nhảy búng tường hình chữ chi đưa chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực bay vút lên đỉnh núi lộng gió.
```
</details>

<details><summary>L57</summary>

```text
HÌNH L57 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "há hốc mồm bất lực trước bản lĩnh không gian ba chiều của chú dê núi tuyết. Nơi mà người ta nhìn thấy thần chết rình rập, sinh vật này lại tìm thấy một". Bố cục: Báo sư tử đứng trơ trọi bên bờ vực, mắt trợn tròn nhìn chú dê đã an tọa trên đỉnh mỏm đá cao vẫy đuôi. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này.
```
</details>

<details><summary>L58</summary>

```text
HÌNH L58 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "sân chơi tự do và bình yên tuyệt đối!". Bố cục: chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực đứng sừng sững trên đỉnh cao tuyết trắng, ánh hoàng hôn chiếu rọi hào quang kiêu hãnh.
```
</details>

<details><summary>L59</summary>

```text
HÌNH L59 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Kính thưa toàn thể quý khán giả và các nhà khoa học theo dõi buổi tổng kết, sau khi thẩm định chi tiết". Bố cục: Hội đồng giám khảo gồm các con vật trao cúp vàng và huy chương vàng danh dự cho chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực.
```
</details>

<details><summary>L60</summary>

```text
HÌNH L60 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "toàn bộ bốn tuyệt kỹ cơ học từ móng chẻ thủy lực kẹp đá, đệm cao su ma sát siêu bám, trọng tâm cơ thể hạ thấp ép sát vách cho đến cú búng tường zig-zag thần sầu, ban giám khảo nhất trí tuyệt đối trao tấm". Bố cục: Tóm tắt bốn biểu tượng trên bảng xếp hạng: Móng kẹp, đệm ma sát, trọng tâm thấp, cú búng tường. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này.
```
</details>

<details><summary>L61</summary>

```text
HÌNH L61 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Huy chương Vàng Cơ Học Vách Đá cho Dê Núi Bắc Mỹ! Sinh vật kiệt xuất này ngày nay chính là nguồn cảm hứng vàng ngọc cho các kỹ sư nghiên cứu robot địa hình của cơ quan hàng không vũ trụ NASA nhằm chế tạo các cánh tay bám kẹp cơ học phục vụ thám hiểm các". Bố cục: Bản thiết kế robot thám hiểm đa địa hình của NASA với chân mô phỏng móng dê leo vách đá Sao Hỏa. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này.
```
</details>

<details><summary>L62</summary>

```text
HÌNH L62 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "hẻm vực dốc đứng trên Sao Hỏa và Mặt Trăng. Các thương hiệu thể thao dã ngoại danh tiếng cũng đang nghiên cứu mô phỏng lớp đệm thịt đàn hồi của móng dê để phát triển". Bố cục: Robot vũ trụ bám chặt vào miệng núi lửa trên Mặt Trăng nhờ cơ cấu móng kẹp phỏng sinh học. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này.
```
</details>

<details><summary>L63</summary>

```text
HÌNH L63 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "thế hệ giày leo núi siêu ma sát cho thế kỷ 21. Bài học sinh tồn từ chú dê núi trên vách đá cheo leo nhắc nhở mỗi chúng ta rằng: Khi đối diện với những". Bố cục: Phòng thiết kế giày leo núi với mẫu đế cao su mô phỏng vi rãnh đệm chân dê núi Bắc Mỹ. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này.
```
</details>

<details><summary>L64</summary>

```text
HÌNH L64 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "thử thách dựng đứng tưởng chừng như không thể vượt qua trong cuộc sống, việc tìm kiếm những". Bố cục: Hình ảnh ẩn dụ: Con người kiên cường vượt qua các rào cản vách đá thử thách trong công việc và cuộc sống. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này.
```
</details>

<details><summary>L65</summary>

```text
HÌNH L65 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "điểm tựa vững chắc dù là nhỏ bé nhất, cùng một tinh thần thăng bằng kiên định, sẽ giúp chúng ta đứng vững và vươn lên đỉnh vinh quang! Giữa bộ". Bố cục: Ngọn hải đăng niềm tin soi sáng con đường vươn tới đỉnh cao vinh quang và tự do. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này.
```
</details>

<details><summary>L66</summary>

```text
HÌNH L66 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "móng chẻ kìm bấm thủy lực và lớp đệm ma sát siêu cấp, cơ chế cơ sinh học nào của Vua Trọng Lực 90° khiến bạn kinh ngạc và thán phục nhất? Hãy". Bố cục: Khung hình so sánh hai phát minh sinh học kèm dấu chấm hỏi lớn mời gọi khán giả bình luận. chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ.
```
</details>

<details><summary>L67</summary>

```text
HÌNH L67 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "để lại cảm nghĩ và bình luận tâm đắc của bạn ngay bên dưới video này nhé! Và đừng quên". Bố cục: Biểu tượng hộp bình luận tương tác vui nhộn xuất hiện cùng chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực nháy mắt tinh nghịch.
```
</details>

<details><summary>L68</summary>

```text
HÌNH L68 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nhấn nút Đăng Ký Kênh cùng chiếc chuông thông báo để đón xem". Bố cục: Ngón tay hoạt hình bấm nút Subscribe đỏ rực và rung chiếc chuông vàng thông báo. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này.
```
</details>

<details><summary>L69</summary>

```text
HÌNH L69 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tập 39: Giải mã sát thủ ngây thơ giấu mặt của". Bố cục: Hình ảnh teaser nhá hàng bóng đen bí ẩn và cành gai treo mồi của Chim Bách Thanh tập sau. KHÔNG có chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết trong cảnh này.
```
</details>

<details><summary>L70</summary>

```text
HÌNH L70 (16:9 ngang, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chim Bách Thanh! Xin chào tạm biệt và hẹn gặp lại toàn thể các bạn trong những hành trình khám phá thiên nhiên kỳ thú tiếp theo!". Bố cục: chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực vẫy tay chào tạm biệt khán giả giữa khung cảnh núi tuyết Rocky lấp lánh nắng mai.
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Bạn có tin trên Trái Đất có một loài động vật nặng tới 140 kg nhưng có thể". Bố cục: Chú dê núi khổng lồ nặng hơn một tạ đứng trên bàn cân điện tử hiển thị con số 140 kg.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "đứng vững trên vách đá dựng đứng 90° nhẵn thín không?". Bố cục: Góc máy quay thẳng đứng cho thấy chú dê dạo bước trên bức tường đá hoa cương dốc 90°.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Đó chính là Dê Núi Bắc Mỹ — Vua Trọng Lực 90° vô địch thiên nhiên! Bí mật chấn động nằm ở". Bố cục: Hào quang vàng rực bao quanh chú dê núi trắng muốt cùng danh hiệu Vua Trọng Lực 90°.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "bộ móng guốc chẻ đôi kẹp gờ đá như kìm bấm thủy lực,". Bố cục: Kính lúp phóng to bộ móng hai nửa xòe rộng kẹp chặt gờ đá như kìm bấm thủy lực.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "kết hợp cùng lớp đệm thịt cao su ma sát cực đại có độ bám dính". Bố cục: Lớp đệm cao su vi mô sần sùi lún sâu vào kẽ nứt mặt đá tạo lực hút ma sát siêu dính.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "gấp 3 lần đế giày leo núi chuyên nghiệp!". Bố cục: Biểu đồ so sánh độ bám dính vượt trội gấp ba lần so với đế giày thể thao leo núi đắt tiền.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Khi gặp ngõ cụt giữa vực sâu ngàn mét, nó có thể tung mình". Bố cục: Chú dê đứng trước ngõ cụt hiểm trở giữa vực sâu thăm thẳm ngàn mét không lối thoát.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "nhảy xa 4m và". Bố cục: Cú phóng thân ngoạn mục bay ngang qua khoảng không vực sâu sang bức tường đối diện.
```
</details>

<details><summary>S09</summary>

```text
HÌNH S09 (DỌC 9:16, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "búng tường xoay người 180° chỉ". Bố cục: Bốn móng đạp mạnh vào vách đá búng ngược trở lại xoay một trăm tám mươi độ giữa tầng không.
```
</details>

<details><summary>S10</summary>

```text
HÌNH S10 (DỌC 9:16, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "trong nửa giây! Thậm chí, loài dê này còn thong dong". Bố cục: Đồng hồ bấm giây chỉ mốc không phẩy năm giây ghi nhận kỷ lục nhào lộn đỉnh cao thế giới.
```
</details>

<details><summary>S11</summary>

```text
HÌNH S11 (DỌC 9:16, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "leo thẳng lên các bức tường đập thủy điện dốc đứng cao hàng trăm mét chỉ để liếm từng vệt muối khoáng!". Bố cục: Chú dê núi tiếp đất an toàn trên đỉnh mỏm đá cao, tạo dáng nhà vô địch parkour.
```
</details>

<details><summary>S12</summary>

```text
HÌNH S12 (DỌC 9:16, phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao (Alpine Mountaineering Field Sketchbook) và nhân vật chú dê núi Bắc Mỹ đeo kính bảo hộ tuyết màu cam và khăn len đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Quả là bậc thầy khinh công thách thức mọi định luật vật lý của Newton!". Bố cục: Khung hình kết thúc mời gọi khán giả bấm tim, like và theo dõi trọn bộ tập dài trên kênh.
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/70 của video YouTube về Dê Núi Bắc Mỹ). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao Bắc Mỹ (Alpine Mountaineering Field Sketchbook & Topographic Art): nét vẽ bút chì than charcoal mộc mạc phong trần kết hợp các đường đồng mức địa hình cao trình topographic uốn lượn sắc sảo, vách đá vôi dựng đứng gồ ghề, cấu trúc móng guốc giác hút phỏng sinh học độc đáo, phối màu xám đá hoa cương, xanh thông alpine và viền vàng kim trắc địa; NỀN TRẮNG TINH hoàn toàn, không watermark, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/12 của video YouTube Shorts về Dê Núi Bắc Mỹ). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách sổ tay ký họa dã ngoại thám hiểm đỉnh núi cao Bắc Mỹ (Alpine Mountaineering Field Sketchbook & Topographic Art): nét vẽ bút chì than charcoal mộc mạc phong trần kết hợp các đường đồng mức địa hình cao trình topographic uốn lượn sắc sảo, vách đá vôi dựng đứng gồ ghề, cấu trúc móng guốc giác hút phỏng sinh học độc đáo, phối màu xám đá hoa cương, xanh thông alpine và viền vàng kim trắc địa; NỀN TRẮNG TINH hoàn toàn, không watermark, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú dê núi Bắc Mỹ (Oreamnos americanus) màu trắng muốt ngộ nghĩnh, đeo kính bảo hộ tuyết màu cam viền titan, quàng khăn len đỏ năng động, móng guốc chẻ đôi màu xám kim loại, thần thái tự tin thách thức trọng lực. 
```
</details>

## 7. SEO

- **title:** Bản Vẽ Vách Đá 90°: Dê Núi Khinh Thường Trọng Lực 4.000m Nhờ Đôi Móng Kẹp Cao Su?! | Tập 38
- **hook_paragraph:** Dê Núi Bắc Mỹ (Oreamnos americanus) di chuyển nhẹ nhàng như bay trên những vách đá dựng đứng 89° đến 90° ở độ cao 4.000 mét giữa rặng núi Rocky tuyết trắng. Điều gì giúp chúng bất chấp mọi định luật vật lý của Isaac Newton mà không hề trượt chân rơi xuống vực sâu? Cùng Giáo sư trưởng giải mã cấu trúc cơ sinh học đỉnh cao!
- **question:** Giữa móng chẻ khớp linh hoạt kẹp mấu đá và đệm chân ma sát nhám như lốp xe đua, vũ khí bám dính nào của Dê Núi khiến bạn choáng ngợp nhất?
- **next_teaser:** sát thủ bụi rậm với kỹ năng xiên cọc con mồi và phân giải độc tố
- **shorts_title:** Bí mật Dê Núi leo vách đá 90 độ ở độ cao 4.000 mét?!
- **shorts_desc:** Đôi móng chẻ uốn cong độc lập cùng đệm cao su ma sát cao giúp Dê Núi thách thức trọng lực!
- **bullets:** Móng chẻ hai mảnh độc lập: Tự động uốn cong và kẹp chặt từng mấu đá nhỏ 1 milimet · Lớp đệm lòng bàn chân ma sát cao: Da nhám đàn hồi triệt tiêu hoàn toàn lực trượt quán tính · Trọng tâm cơ thể cực thấp: Cặp chân trước lực lưỡng ôm sát vách đá như kìm kẹp cơ khí · Bật nhảy không gian hẹp 4 mét: Đảo chiều trên gờ đá chỉ bằng 1 đốt ngón tay · Bộ lông 2 lớp chịu rét âm 45°C: Lớp lông tơ cashmere dày 10cm chống gió bão Alpine · Ứng dụng robot địa hình: NASA và Boston Dynamics học tập cấu trúc móng kẹp thích ứng vách đá
- **tags:** dê núi bắc mỹ, oreamnos americanus, vua vách đá, cơ sinh học kỳ thú, vẽ chuyện hoang dã, whiteboard animation

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-38-de-nui-bac-my
python src/episode/pipeline.py tts    projects/tap-38-de-nui-bac-my     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-38-de-nui-bac-my     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-38-de-nui-bac-my     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-38-de-nui-bac-my              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-38-de-nui-bac-my --force
python scripts/beat_sheet.py projects/tap-38-de-nui-bac-my               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-38-de-nui-bac-my/audio/shorts.wav projects/tap-38-de-nui-bac-my/renders/tap-38-de-nui-bac-my_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-38-de-nui-bac-my
python src/episode/pipeline.py seo    projects/tap-38-de-nui-bac-my
python src/episode/episode_doc.py     projects/tap-38-de-nui-bac-my
```
