# TẬP 50 — KHỈ ĐỘT LƯNG BẠC · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-50-khi-dot-lung-bac`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-50-khi-dot-lung-bac`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F7` · **Persona giọng:** `binh_luan_vien` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Khỉ Đột Lưng Bạc |
| Tiêu đề YouTube | Bí Mật Khỉ Đột Lưng Bạc: Ăn Chay Nhưng Cơ Bắp 800KG Gấp 10 Lần Người?! \| Tập 50 |
| Video dài | `renders/tap-50-khi-dot-lung-bac_long.mp4` — 10:35.6 (635.6s) |
| Shorts | `renders/tap-50-khi-dot-lung-bac_shorts.mp4` — 0:49.5 (49.5s) |
| Thumbnail | `renders/tap-50-khi-dot-lung-bac_thumbnail.jpg` |
| Số hình | dài 53 beat / 53 ảnh riêng; Shorts 11 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.12**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/53 của video YouTube về Khỉ Đột Lưng Bạc). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa vẽ tay đặc trưng cho chủ đề, nét mực sắc nét, màu sắc tương phản cuốn hút, tối giản giàu tính biểu tượng khoa học; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh). Nhân vật phụ cố định: bình luận viên thể thao mặc vest lịch lãm cầm micro hò hét cuồng nhiệt; cụ già kể chuyện vuốt râu trầm trồ trước lực cắn của khỉ đột; chàng trai ngơ ngác ôm xô bột đạm whey protein đứng ngỡ ngàng; bé con tò mò ngước nhìn gã khổng lồ hiền lành nằm chơi với con nhỏ; báo hoa mai gầm gừ hoảng hốt lùi bước trước bóng lưng bạc; thân cây chuối rừng to bằng bắp đùi bị bẻ gãy gập làm đôi; sơ đồ lò phản ứng vi sinh vật manh tràng ruột già tỏa năng lượng đỏ rực trong bụng khỉ đột. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — VỊ VUA QUYỀN ANH CỦA DÃY NÚI VIRUNGA
*Thẻ chương:* CỖ MÁY CƠ BẮP GẤP 10 LẦN NGƯỜI

*Badge:* `ĐẤU TRƯỜNG UFC` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene01_p0.wav` (1175 ký tự) · mood `hao_hung`

```text
Chào mừng toàn thể hàng triệu khán giả cuồng nhiệt đang theo dõi buổi phát sóng trực tiếp từ đài thể thao đỉnh cao thế giới hoang dã! Tôi là bình luận viên chuyên nghiệp đang có mặt tại sàn đấu núi lửa Virunga mù sương ở Trung Phi. Hãy nhìn vào góc võ đài màu đỏ đằng kia xem, một võ sĩ giác đấu khổng lồ nặng tới hai trăm ki-lô-gam đang lừng lững bước ra với chiếc lưng ánh bạc lấp lánh như thép tôi! Cánh tay vượn dài hai mét với những bó cơ bắp cuồn cuộn gân guốc, cơ ngực nở nang săn chắc như hai tấm khiên đồng La Mã. Người đời gọi nó là Khỉ Đột Lưng Bạc, nhưng trên bảng xếp hạng các nhà vô địch sinh tồn của chúng tôi, đây chính là Vua Đấu Trường Rừng Rậm! Một cú đấm sấm sét của gã có thể làm cong vênh thanh xà beng bằng thép đặc và nâng bổng một chiếc xe hơi nặng tám trăm ki-lô-gam lên không trung một cách nhẹ nhàng! Hãy nhớ rằng các lực sĩ cử tạ khỏe nhất thế giới loài người phải đeo đai lưng bảo hộ, quấn băng cổ tay và hít thở trợ lực cật lực mới có thể nâng được mức tạ năm trăm ki-lô-gam trong vài giây ngắn ngủi. Trong khi đó, gã khổng lồ này chỉ cần dùng một tay nhấc bổng khúc gỗ nặng tám trăm ki-lô-gam một cách thong thả như chúng ta cầm một cuốn sách!
```
**Part 1** → `audio/vs/scene01_p1.wav` (108 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Alo bình luận viên ơi, võ sĩ khổng lồ này ngày nào cũng nốc hàng chục xô đạm whey protein để nuôi cơ bắp hả?
```
**Part 2** → `audio/vs/scene01_p2.wav` (968 ký tự) · mood `don_dap`

```text
[laughter] Nhầm to rồi người anh em ngơ ngác ơi, một sự nhầm lẫn thế kỷ của dân tập gym! [surprise-oh] Võ sĩ vô địch Vua Đấu Trường Rừng Rậm của chúng ta là một người ăn chay thuần túy một trăm phần trăm! Cả cuộc đời của nó chưa từng chạm vào một miếng ức gà, chẳng hề đụng đến một muỗng bột đạm công nghiệp, mà thức ăn hàng ngày chỉ toàn là lá cây rừng cay đắng, chồi tre non xơ xác và cọng cần tây dại! Vậy mà khối cơ bắp của nó lại khỏe gấp bốn đến chín lần một người đàn ông lực lưỡng nhất hành tinh! Bí mật đen tối nào đang được che giấu bên trong chiếc bụng to tròn lùm lùm như một quả bom nổ chậm kia? Ngay bây giờ, hãy nổi hồi chuông bắt đầu trận đấu và cùng chúng tôi đột nhập vào khoang lò phản ứng sinh học bí mật này! Mật độ xương đùi và xương cẳng tay của nó dày đặc gấp ba lần xương người, được bọc ngoài bởi những dải gân dày như dây cáp tời thép, tạo nên một khung đỡ cơ học hoàn hảo để truyền tải những nguồn động năng khổng lồ mà không sợ bị gãy nứt.
```

### scene02 — CHIẾC BỤNG BIA CHỨA HÀNG TỶ VI KHUẨN
*Thẻ chương:* CHUYỂN HÓA CHẤT XƠ THÀNH NĂNG LƯỢNG

*Badge:* `LÒ LÊN MEN BỤNG BỰ` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene02_p0.wav` (736 ký tự) · mood `hao_hung`

```text
Các khán giả sành sỏi hãy nhìn kỹ vào vóc dáng của Vua Đấu Trường Rừng Rậm! Mặc dù sở hữu đôi bắp tay cuồn cuộn như đá tảng, nhưng vòng eo của nó hoàn toàn không hề có cơ bụng sáu múi săn chắc như các người mẫu thể hình thời nay. Ngược lại, nó vác một chiếc bụng to tròn, căng phồng và lùm lùm như một chiếc trống cái. Đừng vội chê nó béo phì nhé quý vị! Chiếc bụng bự ấy chính là một khoang lò phản ứng sinh học tối tân mang tên hệ thống lên men ruột sau, nơi hàng ngàn tỷ vi sinh vật kỵ khí đang làm việc tăng ca hai mươi tư trên hai mươi tư giờ không ngừng nghỉ! Chiếc bụng to tròn ấy chiếm tới gần sáu mươi phần trăm tổng thể tích toàn bộ đường tiêu hóa, trong khi ở con người chúng ta ruột già chỉ chiếm vỏn vẹn hai mươi phần trăm.
```
**Part 1** → `audio/vs/scene02_p1.wav` (767 ký tự) · mood `don_dap`

```text
Mỗi ngày, chú khỉ đột trưởng thành này phải nhai ngấu nghiến tới hai mươi ki-lô-gam lá cây và cỏ dại. Trong dạ dày người chúng ta, chất xơ thô cellulose là thứ hoàn toàn không thể tiêu hóa được và bị tống thẳng ra ngoài. Nhưng ở Vua Đấu Trường Rừng Rậm, đoạn manh tràng và ruột già khổng lồ của nó lại là một thùng ủ bia sinh học hoàn hảo. Hàng tỷ vi khuẩn chuyên biệt tại đây sẽ tiết ra các enzym cắt vụn các liên kết chất xơ cellulose cứng đầu, biến chúng thành các phân tử axit béo chuỗi ngắn cực kỳ giàu năng lượng! Không chỉ chuyển hóa chất xơ thành calo, đàn vi sinh vật kỵ khí này còn có khả năng tự tổng hợp ra các axit amin thiết yếu và các loại vitamin nhóm B quan trọng, trực tiếp tái tạo các khối protein nuôi dưỡng từng tế bào cơ bắp nạc cho chú khỉ đột.
```
**Part 2** → `audio/vs/scene02_p2.wav` (696 ký tự) · mood `hao_hung`

```text
Những axit béo kỳ diệu này được niêm mạc ruột hấp thụ trực tiếp và cung cấp tới bảy mươi phần trăm tổng nhu cầu calo mỗi ngày cho toàn bộ cơ thể khổng lồ hai trăm ki-lô-gam. Nó không cần ăn mỡ động vật hay uống sữa tăng cơ, bởi vì chính đàn vi sinh vật trong bụng đã tự tay sản xuất ra nguồn năng lượng tinh khiết nhất để nuôi dưỡng từng thớ cơ bắp thép nguội. Chiếc bụng to tướng ấy không phải mỡ thừa, mà là một nhà máy phát điện sinh học độc nhất vô nhị của rừng rậm nhiệt đới! Mỗi ngày nó dành tới bốn đến sáu tiếng đồng hồ chỉ để thong dong ngồi nhai và tiêu hóa, biến những cánh rừng tre trúc xanh tươi thành nguồn nhiên liệu sinh học vô tận nuôi dưỡng cỗ máy chiến tranh bất khả chiến bại.
```

### scene03 — SỨC MẠNH BẮP TAY XÉ TOẠC THÂN CÂY
*Thẻ chương:* LỰC CẮN 1300 PSI NGHIỀN NÁT XƯƠNG

*Badge:* `LỰC ĐẤM TÀN PHÁ` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene03_p0.wav` (765 ký tự) · mood `don_dap`

```text
Bây giờ mời quý khán giả hướng mắt về bảng đo lực điện tử đặt ngay giữa sàn đấu! Khi một con khỉ đột đực vào cơn thịnh nộ, nó có thể tung ra những đòn đánh với sức công phá làm sập cả một bức tường gạch dày. Cấu trúc bắp tay của Vua Đấu Trường Rừng Rậm được cấu tạo chủ yếu từ các sợi cơ co rút nhanh màu trắng, tối ưu hóa cho những cú bộc phát sức mạnh tột đỉnh trong tích tắc. Một con đực trưởng thành có thể dùng hai tay không bẻ gãy gập một thân cây chuối rừng to bằng bắp đùi người lớn chỉ bằng một cú vặn nhẹ nhàng như bẻ một que tăm! Chiều dài sải tay vượt trội cùng với khớp vai linh hoạt tuyệt đối cho phép nó tung ra những cú đấm móc vòng cung với vận tốc bộc phát xé toạc không gian, tạo ra một vùng sát thương cận chiến tuyệt đối trong bán kính hai mét.
```
**Part 1** → `audio/vs/scene03_p1.wav` (117 ký tự) · 🎭 cameo `ong_gia_ke`

```text
Này các cháu ơi, ngày xưa ông từng thấy nó cắn nát quả dừa khô cứng ngắc trong một nốt nhạc, răng có bọc titan không?
```
**Part 2** → `audio/vs/scene03_p2.wav` (763 ký tự) · mood `hao_hung`

```text
[laughter] Kính thưa cụ già kể chuyện, hàm răng của nó còn đáng sợ hơn cả kim loại nhân tạo nữa ạ! [surprise-oh] Nhờ có một gờ xương đỉnh đầu nhô cao như một chiếc mào gà bằng đá, nơi bám của những bó cơ nhai khổng lồ, lực cắn của Vua Đấu Trường Rừng Rậm đo được lên tới một ngàn ba trăm đơn vị, tức là mạnh gấp đôi lực cắn của một con sư tử châu Phi và gấp bốn lần một người trưởng thành! Một cú cắn của nó thừa sức nghiền nát cành gỗ lim cứng nhất hoặc nghiền vụn xương ống chân của thú dữ trong chớp mắt mà không hề mẻ một chiếc răng nanh nào! Khi hai hàm răng này khép chặt lại, áp lực tại điểm tiếp xúc tương đương với việc đặt một chiếc xe hơi bốn chỗ đè nặng lên một diện tích nhỏ bằng đầu ngón tay cái, đủ sức bóp vụn mọi lớp vỏ giáp bảo vệ cứng cáp nhất.
```
**Part 3** → `audio/vs/scene03_p3.wav` (563 ký tự) · mood `don_dap`

```text
Kết hợp với sải tay dài hơn hai mét rưỡi và trọng tâm cơ thể cực thấp vững chãi như một chiếc xe tăng lội nước, con vật có thể nâng bổng những tảng đá hoa cương nặng tới tám trăm ki-lô-gam rồi ném xa hàng mét. Bất kỳ đối thủ nào dám bước chân vào cự ly cận chiến với gã khổng lồ này đều sẽ phải nếm trải cảm giác bị một cỗ máy nghiền đá ép nát toàn bộ khung xương! Trọng tâm cơ thể cực thấp dồn vào bốn chi vững chãi như bốn cột trụ móng nhà, khiến nó hầu như không bao giờ bị mất thăng bằng hay bị quật ngã trong bất kỳ cuộc giao tranh sinh tử nào giữa núi rừng.
```

### scene04 — NGHI THỨC VỖ NGỰC RỀN VANG
*Thẻ chương:* TÚI KHÍ KHÍ QUẢN CỘNG HƯỞNG ÂM

*Badge:* `TIẾNG ĐẬP NGỰC SẤM RỀN` · *mood mặc định:* `nghiem_trang_gia`

**Part 0** → `audio/vs/scene04_p0.wav` (638 ký tự) · mood `nghiem_trang_gia`

```text
Bùm! Bùm! Bùm! Bùm! Tiếng sấm rền từ đâu vang lên làm rung chuyển cả thung lũng sương mù Virunga! Hãy nhìn vào màn sương dày đặc kia, Vua Đấu Trường Rừng Rậm đang đứng thẳng bằng hai chân sau, vươn cao lồng ngực vĩ đại và dùng hai bàn tay khum lại đập liên hồi vào ngực với tốc độ hai mươi cú đập mỗi giây! Đây chính là nghi thức vỗ ngực kinh điển mang tính thương hiệu toàn cầu của loài khỉ đột lưng bạc! Màn trình diễn này bắt đầu bằng việc con vật đứng thẳng người, nhổ bật một bụi cây xung quanh rồi ném mạnh về phía trước, tiếp theo là một màn bứt tốc chạy ngang đầy thị uy trước khi tung ra cú đập ngực sấm sét rung chuyển trời đất.
```
**Part 1** → `audio/vs/scene04_p1.wav` (682 ký tự) · mood `hao_hung`

```text
Nhiều người lầm tưởng rằng chúng dùng nắm đấm thép đấm huỳnh huỵch vào ngực để khoe khoang sự hung bạo. Nhưng góc quay phân tích chuyển động chậm của chúng tôi cho thấy: Bàn tay của nó khum tròn lại như một chiếc bát úp! Bên dưới lớp da ngực dày cộp là các túi khí thanh quản khổng lồ hoạt động giống hệt như những chiếc trống lục lạc cộng hưởng âm thanh. Mỗi cú đập khum tay tạo ra những luồng sóng âm trầm đục vang xa tới hơn một cây số xuyên qua rừng rậm dày đặc! Những túi khí thanh quản này có thể tích chứa lên tới vài lít không khí, hoạt động đồng điệu với nhịp đập bàn tay để tạo nên những tần số âm thanh cộng hưởng trầm sâu có sức xuyên thấu phi thường qua tán lá rậm rạp.
```
**Part 2** → `audio/vs/scene04_p2.wav` (690 ký tự) · mood `hao_hung`

```text
Âm thanh trầm đục này chứa đựng các thông số sinh học chính xác về kích thước cơ thể, dung tích phổi và đẳng cấp sức mạnh của con đực đầu đàn. Những con đực trẻ tuổi ngỗ nghịch khi nghe thấy tiếng trống ngực uy dũng này từ xa sẽ lập tức biết thân biết phận mà cúi đầu rút lui, tránh được những cuộc chiến đẫm máu không cần thiết. Đó là một giải pháp ngoại giao bằng âm thanh đỉnh cao, vừa phô diễn sức mạnh vô song, vừa bảo tồn sinh lực cho toàn thể bầy đàn! Đây chính là nghệ thuật chiến tranh tâm lý đỉnh cao: Đánh bại đối thủ từ trong tư tưởng trước khi một giọt máu nào kịp rơi, khẳng định vị thế thủ lĩnh tối cao mà không làm tiêu hao dù chỉ một phần trăm sinh lực quý giá của bầy đàn.
```

### scene05 — BẢN CHẤT VỊ THA CỦA NHÀ VÔ ĐỊCH
*Thẻ chương:* SẴN SÀNG HY SINH VÌ ĐÀN CON

*Badge:* `TÂM HỒN NGƯỜI KHỔNG LỒ` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene05_p0.wav` (712 ký tự) · mood `hao_hung`

```text
Mặc dù sở hữu sức mạnh hủy diệt có thể hạ gục cả một con báo hoa mai trưởng thành chỉ bằng một cú tát trời giáng, nhưng bản chất thực sự của Vua Đấu Trường Rừng Rậm lại là một người khổng lồ cực kỳ hiền lành, trầm tĩnh và giàu lòng trắc ẩn. Chúng dành phần lớn thời gian trong ngày để nằm phơi nắng trên những thảm cỏ xanh, nhẹ nhàng chải lông cho những chú khỉ đột con tinh nghịch trèo lên đầu lên cổ mình, và chia sẻ những chồi măng non ngon lành cho các con mái trong bầy. Những nhà linh trưởng học huyền thoại từng dành cả đời sống cạnh các gia đình khỉ đột hoang dã đều khẳng định rằng: Đây là một trong những loài sinh vật sống tình cảm, thấu hiểu và hòa bình nhất từng bước đi trên hành tinh của chúng ta.
```
**Part 1** → `audio/vs/scene05_p1.wav` (102 ký tự) · 🎭 cameo `be_con`

```text
Ủa chú ơi, gã khổng lồ cơ bắp cuồn cuộn này cũng dịu dàng nằm chơi với con nhỏ giống bố cháu ở nhà hả?
```
**Part 2** → `audio/vs/scene05_p2.wav` (746 ký tự) · mood `don_dap`

```text
Chúng không bao giờ chủ động gây chiến hay ức hiếp những sinh vật nhỏ bé xung quanh. Những màn gầm rú hay đập ngực thị uy thực chất chỉ là những lời cảnh cáo nhân từ cuối cùng để kẻ xâm nhập biết đường rút lui trong hòa bình. Nhưng một khi gia đình của nó bị đe dọa bởi những tên săn trộm tàn độc hay bầy thú ăn thịt đói khát, gã khổng lồ hiền lành ấy sẽ lập tức hóa thân thành một bức tường thành bất khả xâm phạm, sẵn sàng hứng trọn mọi mũi giáo và đạn lửa để che chở cho từng đứa con bé bỏng đến hơi thở cuối cùng! Ánh mắt trầm tư đầy thấu cảm của một con đực đầu đàn khi nhìn đứa con thơ chập chững biết đi chứa đựng một vẻ đẹp nhân văn sâu sắc, xóa tan hoàn toàn mọi định kiến thô bạo về quái thú King Kong hung dữ trong phim ảnh viễn tưởng.
```
**Part 3** → `audio/vs/scene05_p3.wav` (494 ký tự) · mood `hao_hung`

```text
Một trái tim quả cảm đầy tình phụ tử nằm bên trong khối cơ bắp thép nguội hai trăm ki-lô-gam! Đó chính là phẩm chất cao quý nhất làm nên vị thế của một vị vua chân chính của núi rừng bao la, khiến con người chúng ta khi đứng trước chúng cũng phải nghiêng mình kính phục! Sức mạnh càng lớn thì lòng vị tha và tinh thần che chở càng phải cao thượng! Đó chính là nguyên lý sinh tồn cốt lõi giúp giống loài khỉ đột lưng bạc tồn tại kiên cường qua suốt bao kỷ nguyên thăng trầm của lịch sử tự nhiên.
```

### scene06 — KHÉP LẠI MÙA GIẢI 50 TẬP HUYỀN THOẠI
*Thẻ chương:* BẢN LĨNH CỦA KẺ MẠNH ĐÍCH THỰC

*Badge:* `KẾT LUẬN` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene06_p0.wav` (678 ký tự) · mood `am_ap`

```text
Từ chiếc bụng lò phản ứng vi sinh vật biến lá cây thành sức mạnh tám trăm ki-lô-gam phi thường, lực cắn sấm sét một ngàn ba trăm đơn vị vượt xa chúa sơn lâm, tiếng đập ngực rền vang một cây số rung chuyển rừng già, cho đến tâm hồn nhân từ của một vị vua bảo hộ gia đình, Vua Đấu Trường Rừng Rậm đã chứng minh cho toàn thế giới thấy rằng: Sức mạnh cơ bắp đích thực bắt nguồn từ sự giản dị thuần khiết của tự nhiên, và quyền lực tối thượng luôn đi liền với lòng vị tha và tinh thần trách nhiệm bảo vệ kẻ yếu! Khối cơ bắp phi thường tám trăm ki-lô-gam ấy không phải là công cụ để thống trị hay áp bức, mà là tấm lá chắn thiêng liêng để bảo bọc sự bình yên cho cả gia đình thân yêu.
```
**Part 1** → `audio/vs/scene06_p1.wav` (979 ký tự) · mood `am_ap`

```text
Tập phim thứ năm mươi ngày hôm nay cũng chính là mốc son chói lọi khép lại trọn vẹn chuỗi hành trình năm mươi tập phim khám phá thế giới động vật kỳ thú của kênh chúng tôi! Trải qua năm mươi bài học sinh tồn phi thường, từ những sinh vật biển sâu tăm tối cho đến những pháo đài rải gai và đấu trường rừng rậm, chúng ta đã cùng nhau chứng kiến những tuyệt tác tiến hóa vĩ đại nhất của tạo hóa. Xin chân thành cảm ơn sự đồng hành cuồng nhiệt của toàn thể quý vị khán giả! Hãy tiếp tục rèn luyện cho mình một thể lực sung mãn, một ý chí kiên định và một trái tim nhân ái như chú khỉ đột lưng bạc nhé! Đừng quên để lại bình luận và chia sẻ tình yêu thiên nhiên kỳ diệu này! Hẹn gặp lại các bạn trong những siêu phẩm hoang dã tiếp theo! Nhìn lại chặng đường năm mươi tập phim đã qua, chúng tôi vô cùng tự hào và xúc động khi được cùng các bạn mở toang những cánh cửa kỳ diệu nhất của thế giới tự nhiên. Hãy giữ vững ngọn lửa đam mê khám phá và sống một cuộc đời tràn đầy bản lĩnh nhé!
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Chỉ ăn toàn lá cây rừng và chồi tre non xơ xác, tại sao Khỉ Đột Lưng Bạc lại sở hữu cơ bắp cuồn cuộn nâng được vật nặng tám trăm ki-lô-gam?! Hãy nhìn Vua Đấu Trường Rừng Rậm nặng tới hai trăm ki-lô-gam này xem! Cơ bắp của nó khỏe gấp bốn đến chín lần một người đàn ông lực lưỡng, với lực cắn một ngàn ba trăm đơn vị mạnh gấp đôi cả chúa sơn lâm sư tử châu Phi! Bí mật sức mạnh không nằm ở thức ăn giàu đạm mà ẩn giấu bên trong chiếc bụng bự tròn vo của nó! Bên trong ruột già khổng lồ chứa hàng ngàn tỷ vi khuẩn kỵ khí lên men, biến chất xơ cellulose khó tiêu của hai mươi ki-lô-gam lá cây mỗi ngày thành các phân tử axit béo giàu năng lượng, cung cấp tới bảy mươi phần trăm tổng calo cho toàn bộ cơ thể! Khi thị uy, nó đứng thẳng hai chân đập khum tay vào ngực, tạo ra những đợt sóng âm sấm sét vang xa hơn một cây số để cảnh cáo kẻ thù! Một cỗ máy cơ bắp ăn chay thuần túy bất khả chiến bại của tạo hóa!
```

**Whisper prompt:** `Khỉ Đột Lưng Bạc, Gorilla beringei`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| tám trăm ki-lô-gam | 800kg |
| hai trăm ki-lô-gam | 200kg |
| hai mươi ki-lô-gam | 20kg |
| năm trăm ki-lô-gam | 500kg |
| mười lần | 10 lần |
| bốn đến chín lần | 4-9 lần |
| bảy mươi phần trăm | 70% |
| sáu mươi phần trăm | 60% |
| hai mươi phần trăm | 20% |
| một phần trăm | 1% |
| bốn đến sáu tiếng | 4-6 tiếng |
| hai mét | 2m |
| hai mét rưỡi | 2.5m |
| một ngàn ba trăm | 1300 PSI |
| hai mươi tư giờ | 24h |
| năm mươi tập | 50 tập |
| một trăm phần trăm | 100% |
| sáu múi | 6 múi |
| hai mươi cú đập | 20 cú đập |
| ngàn tỷ | ngàn tỷ |
| hai mươi tư trên hai mươi tư | 24/24 |
| năm mươi | 50 |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · VỊ VUA QUYỀN ANH CỦA DÃY NÚI VIRUNGA · 112.0s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.7 (9.7s) | L01 | Chào mừng toàn thể hàng triệu khán giả cuồng nhiệt đang theo dõi buổi phát sóng trực tiếp từ đài thể thao đỉnh cao thế giới hoang dã! Tôi là bình luận viên chuyên nghiệp đang có mặt |  | bình luận viên thể thao mặc vest lịch lãm cầm micro hò hét cuồng nhiệt: bình luận viên thể thao cuồng nhiệt chĩa micro gào thét trước sàn đấu sương mù Virunga |
| b02 | 00:09.7–00:22.9 (13.2s) | L02 | tại sàn đấu núi lửa Virunga mù sương ở Trung Phi. Hãy nhìn vào góc võ đài màu đỏ đằng kia xem, một võ sĩ giác đấu khổng lồ nặng tới 200kg đang lừng lững bước ra với chiếc lưng ánh bạc lấp lánh như thép tôi! Cánh tay vượn dài 2m với |  | chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): võ sĩ khổng lồ 200kg bước ra sàn đấu với chiếc lưng ánh bạc lấp lánh như thép tôi |
| b03 | 00:22.9–00:35.6 (12.6s) | L03 | những bó cơ bắp cuồn cuộn gân guốc, cơ ngực nở nang săn chắc như hai tấm khiên đồng La Mã. Người đời gọi nó là Khỉ Đột Lưng Bạc, nhưng trên bảng xếp hạng các nhà vô địch sinh tồn của chúng tôi, đây chính là Vua Đấu Trường Rừng Rậm! Một cú đấm |  | chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): cánh tay vượn dài 2 mét với những bó cơ bắp cuồn cuộn gân guốc bẻ cong xà beng thép |
| b04 | 00:35.6–00:48.5 (12.9s) | L04 | sấm sét của gã có thể làm cong vênh thanh xà beng bằng thép đặc và nâng bổng một chiếc xe hơi nặng 800kg lên không trung một cách nhẹ nhàng! Hãy nhớ rằng các lực sĩ cử tạ khỏe nhất thế giới loài người phải đeo đai lưng bảo hộ, quấn băng cổ | **800kg** · Sức nâng bắp tay · R/320 · [0.8, 0.4] | chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): khỉ đột dùng một tay nhấc bổng khúc gỗ nặng 800kg thong thả như cầm một cuốn sách |
| b05 | 00:48.5–01:02.9 (14.4s) | L05 | tay và hít thở trợ lực cật lực mới có thể nâng được mức tạ 500kg trong vài giây ngắn ngủi. Trong khi đó, gã khổng lồ này chỉ cần dùng một tay nhấc bổng khúc gỗ nặng 800kg một cách thong thả như chúng ta cầm một cuốn sách! Alo bình luận viên ơi, |  | chàng trai ngơ ngác ôm xô bột đạm whey protein đứng ngỡ ngàng: chú ngơ ngác ôm xô đạm whey protein đứng chết trân trước khẩu phần ăn chay của khỉ đột |
| b06 | 01:02.9–01:14.9 (12.0s) | L06 | võ sĩ khổng lồ này ngày nào cũng nốc hàng chục xô đạm whey protein để nuôi cơ bắp hả? Nhầm to rồi người anh em ngơ ngác ơi, một sự nhầm lẫn thế kỷ của dân tập gym! Võ sĩ vô địch Vua Đấu Trường Rừng Rậm của chúng ta là |  | chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): khỉ đột ngồi nhai lá cây rừng chồi tre non xơ xác với nụ cười sảng khoái |
| b07 | 01:14.9–01:26.7 (11.8s) | L07 | một người ăn chay thuần túy 100%! Cả cuộc đời của nó chưa từng chạm vào một miếng ức gà, chẳng hề đụng đến một muỗng bột đạm công nghiệp, mà thức ăn hàng ngày chỉ toàn là lá cây rừng cay đắng, chồi tre non xơ xác và cọng cần tây dại! Vậy |  | chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): sơ đồ so sánh sức mạnh cơ bắp gấp 4-9 lần người đàn ông lực lưỡng nhất |
| b08 | 01:26.7–01:38.0 (11.3s) | L08 | mà khối cơ bắp của nó lại khỏe gấp 4-9 lần một người đàn ông lực lưỡng nhất hành tinh! Bí mật đen tối nào đang được che giấu bên trong chiếc bụng to tròn lùm lùm như một quả bom nổ chậm kia? Ngay bây giờ, hãy nổi hồi chuông bắt đầu trận đấu |  | chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): mật độ xương dày đặc gấp 3 lần và dây gân bọc thép chịu tải động năng cực hạn |
| b09 | 01:38.0–01:52.0 (14.0s) | L09 | và cùng chúng tôi đột nhập vào khoang lò phản ứng sinh học bí mật này! Mật độ xương đùi và xương cẳng tay của nó dày đặc gấp ba lần xương người, được bọc ngoài bởi những dải gân dày như dây cáp tời thép, tạo nên một khung đỡ cơ học hoàn hảo để truyền tải những nguồn động năng khổng lồ mà không sợ bị gãy nứt. |  | bình luận viên thể thao mặc vest lịch lãm cầm micro hò hét cuồng nhiệt chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): bình luận viên chỉ tay vào chiếc bụng to tròn căng phồng như lò phản ứng sinh học |

### scene02 · CHIẾC BỤNG BIA CHỨA HÀNG TỶ VI KHUẨN · 110.6s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.1 (8.1s) | L10 | Các khán giả sành sỏi hãy nhìn kỹ vào vóc dáng của Vua Đấu Trường Rừng Rậm! Mặc dù sở hữu đôi bắp tay cuồn cuộn như đá tảng, nhưng vòng eo của nó hoàn |  | chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): vóc dáng bệ vệ của khỉ đột với chiếc bụng to tròn căng phồng lùm lùm như chiếc trống cái |
| b02 | 00:08.1–00:19.9 (11.9s) | L11 | toàn không hề có cơ bụng 6 múi săn chắc như các người mẫu thể hình thời nay. Ngược lại, nó vác một chiếc bụng to tròn, căng phồng và lùm lùm như một chiếc trống cái. Đừng vội chê nó béo phì nhé quý vị! Chiếc bụng bự ấy |  | sơ đồ lò phản ứng vi sinh vật manh tràng ruột già tỏa năng lượng đỏ rực trong bụng khỉ đột: sơ đồ cắt ngang khoang bụng cho thấy lò phản ứng lên men ruột sau tỏa sáng rực lửa |
| b03 | 00:19.9–00:33.4 (13.4s) | L12 | chính là một khoang lò phản ứng sinh học tối tân mang tên hệ thống lên men ruột sau, nơi hàng ngàn tỷ vi sinh vật kỵ khí đang làm việc tăng ca 24/24 giờ không ngừng nghỉ! Chiếc bụng to tròn ấy chiếm tới gần 60% tổng thể tích toàn bộ |  | sơ đồ lò phản ứng vi sinh vật manh tràng ruột già tỏa năng lượng đỏ rực trong bụng khỉ đột: ruột già khổng lồ chiếm 60% thể tích tiêu hóa với hàng tỷ vi sinh vật kỵ khí tăng ca |
| b04 | 00:33.4–00:46.7 (13.3s) | L13 | đường tiêu hóa, trong khi ở con người chúng ta ruột già chỉ chiếm vỏn vẹn 20%. Mỗi ngày, chú khỉ đột trưởng thành này phải nhai ngấu nghiến tới 20kg lá cây và cỏ dại. Trong dạ dày người chúng ta, chất xơ thô cellulose là thứ hoàn toàn không | **20kg** · Lá cây mỗi ngày · L/360 · [0.35, 0.5] | chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): đống lá cây 20kg được nhai vụn đưa vào thùng ủ bia sinh học manh tràng |
| b05 | 00:46.7–00:57.1 (10.4s) | L14 | thể tiêu hóa được và bị tống thẳng ra ngoài. Nhưng ở Vua Đấu Trường Rừng Rậm, đoạn manh tràng và ruột già khổng lồ của nó lại là một thùng ủ bia sinh học hoàn hảo. Hàng tỷ vi khuẩn chuyên biệt tại đây sẽ tiết ra các enzym cắt |  | sơ đồ lò phản ứng vi sinh vật manh tràng ruột già tỏa năng lượng đỏ rực trong bụng khỉ đột: các enzym vi khuẩn cắt đứt liên kết xen-lu-lô-zơ tạo ra axit béo chuỗi ngắn giàu năng lượng |
| b06 | 00:57.1–01:10.1 (13.0s) | L15 | vụn các liên kết chất xơ cellulose cứng đầu, biến chúng thành các phân tử axit béo chuỗi ngắn cực kỳ giàu năng lượng! Không chỉ chuyển hóa chất xơ thành calo, đàn vi sinh vật kỵ khí này còn có khả năng tự tổng hợp ra các axit amin thiết yếu và các loại vitamin nhóm B quan trọng, |  | sơ đồ lò phản ứng vi sinh vật manh tràng ruột già tỏa năng lượng đỏ rực trong bụng khỉ đột: đàn vi khuẩn tự tổng hợp axit amin thiết yếu và vitamin B nuôi dưỡng tế bào cơ bắp nạc |
| b07 | 01:10.1–01:24.9 (14.8s) | L16 | trực tiếp tái tạo các khối protein nuôi dưỡng từng tế bào cơ bắp nạc cho chú khỉ đột. Những axit béo kỳ diệu này được niêm mạc ruột hấp thụ trực tiếp và cung cấp tới 70% tổng nhu cầu calo mỗi ngày cho toàn bộ cơ thể khổng lồ 200kg. Nó không cần ăn mỡ động vật hay | **70% CALO** · Năng lượng từ chất xơ · R/320 · [0.8, 0.4] | chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): dòng năng lượng tinh khiết hấp thụ qua niêm mạc ruột cung cấp 70% tổng calo cơ thể |
| b08 | 01:24.9–01:38.8 (13.8s) | L17 | uống sữa tăng cơ, bởi vì chính đàn vi sinh vật trong bụng đã tự tay sản xuất ra nguồn năng lượng tinh khiết nhất để nuôi dưỡng từng thớ cơ bắp thép nguội. Chiếc bụng to tướng ấy không phải mỡ thừa, mà là một nhà máy phát điện sinh học độc nhất vô nhị của rừng rậm nhiệt |  | chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): khỉ đột ngồi thong dong 4-6 tiếng mỗi ngày nhai lá tre trúc nuôi dưỡng khối cơ bắp thép |
| b09 | 01:38.8–01:50.6 (11.8s) | L18 | đới! Mỗi ngày nó dành tới 4-6 tiếng đồng hồ chỉ để thong dong ngồi nhai và tiêu hóa, biến những cánh rừng tre trúc xanh tươi thành nguồn nhiên liệu sinh học vô tận nuôi dưỡng cỗ máy chiến tranh bất khả chiến bại. |  | chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): nhà máy phát điện sinh học độc nhất vô nhị biến lá cây thành sức mạnh vô song |

### scene03 · SỨC MẠNH BẮP TAY XÉ TOẠC THÂN CÂY · 107.6s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.5 (7.5s) | L19 | Bây giờ mời quý khán giả hướng mắt về bảng đo lực điện tử đặt ngay giữa sàn đấu! Khi một con khỉ đột đực vào cơn thịnh nộ, nó có thể tung ra những đòn đánh |  | chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): bảng đo lực điện tử vỡ nát trước cú đấm tàn phá làm sập bức tường gạch dày |
| b02 | 00:07.5–00:18.4 (10.9s) | L20 | với sức công phá làm sập cả một bức tường gạch dày. Cấu trúc bắp tay của Vua Đấu Trường Rừng Rậm được cấu tạo chủ yếu từ các sợi cơ co rút nhanh màu trắng, tối ưu hóa cho những cú bộc phát sức mạnh tột đỉnh trong tích tắc. Một con đực |  | chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): sợi cơ co rút nhanh màu trắng bộc phát sức mạnh tột đỉnh trong tích tắc |
| b03 | 00:18.4–00:29.6 (11.2s) | L21 | trưởng thành có thể dùng hai tay không bẻ gãy gập một thân cây chuối rừng to bằng bắp đùi người lớn chỉ bằng một cú vặn nhẹ nhàng như bẻ một que tăm! Chiều dài sải tay vượt trội cùng với khớp vai linh hoạt tuyệt đối cho phép nó tung ra những cú |  | chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh) thân cây chuối rừng to bằng bắp đùi bị bẻ gãy gập làm đôi: khỉ đột dùng hai tay không bẻ gãy gập thân cây chuối to bằng bắp đùi người lớn |
| b04 | 00:29.6–00:43.1 (13.5s) | L22 | đấm móc vòng cung với vận tốc bộc phát xé toạc không gian, tạo ra một vùng sát thương cận chiến tuyệt đối trong bán kính 2m. Này các cháu ơi, ngày xưa ông từng thấy nó cắn nát quả dừa khô cứng ngắc trong một nốt nhạc, răng có bọc titan không? Kính |  | chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): sải tay dài 2.5 mét tạo ra vùng sát thương cận chiến tuyệt đối quét sạch đối thủ |
| b05 | 00:43.1–00:55.5 (12.4s) | L23 | thưa cụ già kể chuyện, hàm răng của nó còn đáng sợ hơn cả kim loại nhân tạo nữa ạ! Nhờ có một gờ xương đỉnh đầu nhô cao như một chiếc mào gà bằng đá, nơi bám của những bó cơ nhai khổng lồ, lực cắn của Vua Đấu Trường Rừng Rậm đo |  | cụ già kể chuyện vuốt râu trầm trồ trước lực cắn của khỉ đột: cụ già kể chuyện vuốt râu nhớ lại cảnh khỉ đột cắn nát quả dừa khô cứng ngắc |
| b06 | 00:55.5–01:07.8 (12.2s) | L24 | được lên tới 1300 PSI đơn vị, tức là mạnh gấp đôi lực cắn của một con sư tử châu Phi và gấp bốn lần một người trưởng thành! Một cú cắn của nó thừa sức nghiền nát cành gỗ lim cứng nhất hoặc nghiền vụn xương ống chân của thú dữ trong chớp | **1300 PSI** · Lực cắn nghiền xương · R/320 · [0.8, 0.4] | chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): gờ xương đỉnh đầu nhô cao như mào gà bằng đá làm điểm tựa cho cơ nhai khổng lồ |
| b07 | 01:07.8–01:20.0 (12.3s) | L25 | mắt mà không hề mẻ một chiếc răng nanh nào! Khi hai hàm răng này khép chặt lại, áp lực tại điểm tiếp xúc tương đương với việc đặt một chiếc xe hơi bốn chỗ đè nặng lên một diện tích nhỏ bằng đầu ngón tay cái, đủ sức bóp vụn mọi lớp vỏ |  | chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): đồng hồ đo lực cắn chỉ con số 1300 PSI mạnh gấp đôi chúa sơn lâm sư tử |
| b08 | 01:20.0–01:33.0 (13.0s) | L26 | giáp bảo vệ cứng cáp nhất. Kết hợp với sải tay dài hơn 2.5m và trọng tâm cơ thể cực thấp vững chãi như một chiếc xe tăng lội nước, con vật có thể nâng bổng những tảng đá hoa cương nặng tới 800kg rồi ném xa hàng mét. Bất kỳ đối thủ nào dám bước chân vào |  | chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): khỉ đột nâng bổng tảng đá hoa cương 800kg ném xa hàng mét với trọng tâm vững chãi |
| b09 | 01:33.0–01:47.6 (14.6s) | L27 | cự ly cận chiến với gã khổng lồ này đều sẽ phải nếm trải cảm giác bị một cỗ máy nghiền đá ép nát toàn bộ khung xương! Trọng tâm cơ thể cực thấp dồn vào bốn chi vững chãi như bốn cột trụ móng nhà, khiến nó hầu như không bao giờ bị mất thăng bằng hay bị quật ngã trong bất kỳ cuộc giao tranh sinh tử nào giữa núi rừng. |  | bình luận viên thể thao mặc vest lịch lãm cầm micro hò hét cuồng nhiệt: bình luận viên ngả mũ thán phục trước cỗ máy nghiền đá bất khả chiến bại |

### scene04 · NGHI THỨC VỖ NGỰC RỀN VANG · 101.6s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.3 (7.3s) | L28 | Bùm! Bùm! Bùm! Bùm! Tiếng sấm rền từ đâu vang lên làm rung chuyển cả thung lũng sương mù Virunga! Hãy nhìn vào màn sương dày đặc kia, Vua Đấu Trường Rừng |  | chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): sấm rền vang dội thung lũng khi khỉ đột vươn cao lồng ngực vĩ đại đập liên hồi 20 cú mỗi giây |
| b02 | 00:07.3–00:17.7 (10.4s) | L29 | Rậm đang đứng thẳng bằng hai chân sau, vươn cao lồng ngực vĩ đại và dùng hai bàn tay khum lại đập liên hồi vào ngực với tốc độ 20 cú đập mỗi giây! Đây chính là nghi thức vỗ ngực kinh điển mang tính thương hiệu toàn |  | chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): con vật nhổ bật bụi cây ném về phía trước chạy ngang thị uy dũng mãnh |
| b03 | 00:17.7–00:27.6 (9.9s) | L30 | cầu của loài khỉ đột lưng bạc! Màn trình diễn này bắt đầu bằng việc con vật đứng thẳng người, nhổ bật một bụi cây xung quanh rồi ném mạnh về phía trước, tiếp theo là một màn bứt tốc chạy ngang đầy thị uy trước khi tung |  | chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): góc quay chậm cho thấy bàn tay khum tròn như chiếc bát úp tạo luồng sóng âm trầm đục |
| b04 | 00:27.6–00:39.8 (12.2s) | L31 | ra cú đập ngực sấm sét rung chuyển trời đất. Nhiều người lầm tưởng rằng chúng dùng nắm đấm thép đấm huỳnh huỵch vào ngực để khoe khoang sự hung bạo. Nhưng góc quay phân tích chuyển động chậm của chúng tôi cho thấy: Bàn tay của nó |  | chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): sơ đồ túi khí thanh quản khổng lồ dung tích vài lít đóng vai trò buồng cộng hưởng âm thanh |
| b05 | 00:39.8–00:50.7 (10.9s) | L32 | khum tròn lại như một chiếc bát úp! Bên dưới lớp da ngực dày cộp là các túi khí thanh quản khổng lồ hoạt động giống hệt như những chiếc trống lục lạc cộng hưởng âm thanh. Mỗi cú đập khum tay tạo ra những luồng sóng |  | chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): luồng sóng âm trầm sâu xuyên thấu qua tán lá rậm rạp vang xa hơn 1 kilomet |
| b06 | 00:50.7–01:01.5 (10.8s) | L33 | âm trầm đục vang xa tới hơn một cây số xuyên qua rừng rậm dày đặc! Những túi khí thanh quản này có thể tích chứa lên tới vài lít không khí, hoạt động đồng điệu với nhịp đập bàn tay để tạo nên những tần số âm thanh | **1 KM** · Âm thanh vỗ ngực · L/350 · [0.4, 0.5] | chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh) báo hoa mai gầm gừ hoảng hốt lùi bước trước bóng lưng bạc: những con đực trẻ và báo hoa mai nghe tiếng sấm rền từ xa lập tức cúi đầu rút lui |
| b07 | 01:01.5–01:14.4 (12.9s) | L34 | cộng hưởng trầm sâu có sức xuyên thấu phi thường qua tán lá rậm rạp. Âm thanh trầm đục này chứa đựng các thông số sinh học chính xác về kích thước cơ thể, dung tích phổi và đẳng cấp sức mạnh của con đực đầu đàn. Những con đực trẻ |  | chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): giải pháp ngoại giao bằng âm thanh đỉnh cao bảo tồn sinh lực cho toàn thể bầy đàn |
| b08 | 01:14.4–01:27.6 (13.2s) | L35 | tuổi ngỗ nghịch khi nghe thấy tiếng trống ngực uy dũng này từ xa sẽ lập tức biết thân biết phận mà cúi đầu rút lui, tránh được những cuộc chiến đẫm máu không cần thiết. Đó là một giải pháp ngoại giao bằng âm thanh đỉnh cao, vừa phô diễn sức mạnh vô song, |  | bình luận viên thể thao mặc vest lịch lãm cầm micro hò hét cuồng nhiệt: bình luận viên nín thở thán phục bản lĩnh của vị vua đầu đàn rừng rậm |
| b09 | 01:27.6–01:41.6 (14.0s) | L36 | vừa bảo tồn sinh lực cho toàn thể bầy đàn! Đây chính là nghệ thuật chiến tranh tâm lý đỉnh cao: Đánh bại đối thủ từ trong tư tưởng trước khi một giọt máu nào kịp rơi, khẳng định vị thế thủ lĩnh tối cao mà không làm tiêu hao dù chỉ 1% sinh lực quý giá của bầy đàn. |  | chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): khỉ đột đứng sừng sững giữa đỉnh đèo Virunga uy nghiêm bất khả xâm phạm |

### scene05 · BẢN CHẤT VỊ THA CỦA NHÀ VÔ ĐỊCH · 103.3s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.6 (7.6s) | L37 | Mặc dù sở hữu sức mạnh hủy diệt có thể hạ gục cả một con báo hoa mai trưởng thành chỉ bằng một cú tát trời giáng, nhưng bản chất thực sự của |  | chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): gã khổng lồ nằm phơi nắng trên thảm cỏ xanh nhẹ nhàng chải lông cho khỉ con tinh nghịch |
| b02 | 00:07.6–00:19.8 (12.3s) | L38 | Vua Đấu Trường Rừng Rậm lại là một người khổng lồ cực kỳ hiền lành, trầm tĩnh và giàu lòng trắc ẩn. Chúng dành phần lớn thời gian trong ngày để nằm phơi nắng trên những thảm cỏ xanh, nhẹ nhàng chải lông cho những chú khỉ đột con tinh nghịch |  | bé con tò mò ngước nhìn gã khổng lồ hiền lành nằm chơi với con nhỏ: bé con tò mò mỉm cười thích thú thấy gã khổng lồ nằm chơi đùa cùng bầy con nhỏ |
| b03 | 00:19.8–00:32.1 (12.3s) | L39 | trèo lên đầu lên cổ mình, và chia sẻ những chồi măng non ngon lành cho các con mái trong bầy. Những nhà linh trưởng học huyền thoại từng dành cả đời sống cạnh các gia đình khỉ đột hoang dã đều khẳng định rằng: Đây là một trong những |  | chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): khỉ đột chia sẻ chồi măng non ngon lành cho các con mái và con non trong bầy |
| b04 | 00:32.1–00:43.9 (11.8s) | L40 | loài sinh vật sống tình cảm, thấu hiểu và hòa bình nhất từng bước đi trên hành tinh của chúng ta. Ủa chú ơi, gã khổng lồ cơ bắp cuồn cuộn này cũng dịu dàng nằm chơi với con nhỏ giống bố cháu ở nhà hả? Chúng không bao |  | chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): ánh mắt trầm tư đầy thấu cảm của vị vua đầu đàn xóa tan định kiến quái vật chú khỉ đột hoạt hình khổng lồ |
| b05 | 00:43.9–00:54.4 (10.4s) | L41 | giờ chủ động gây chiến hay ức hiếp những sinh vật nhỏ bé xung quanh. Những màn gầm rú hay đập ngực thị uy thực chất chỉ là những lời cảnh cáo nhân từ cuối cùng để kẻ xâm nhập biết đường rút lui trong hòa bình. Nhưng một khi |  | chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): khi bầy con bị đe dọa khỉ đột hóa thân thành bức tường thành che chở đàn con đến cùng |
| b06 | 00:54.4–01:04.3 (10.0s) | L42 | gia đình của nó bị đe dọa bởi những tên săn trộm tàn độc hay bầy thú ăn thịt đói khát, gã khổng lồ hiền lành ấy sẽ lập tức hóa thân thành một bức tường thành bất khả xâm phạm, sẵn sàng hứng trọn mọi mũi giáo và đạn lửa |  | chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): nắm đấm thép sẵn sàng nghênh chiến lũ săn trộm để bảo vệ bình yên gia đình |
| b07 | 01:04.3–01:16.6 (12.3s) | L43 | để che chở cho từng đứa con bé bỏng đến hơi thở cuối cùng! Ánh mắt trầm tư đầy thấu cảm của một con đực đầu đàn khi nhìn đứa con thơ chập chững biết đi chứa đựng một vẻ đẹp nhân văn sâu sắc, xóa tan hoàn toàn mọi định kiến thô bạo về quái thú King Kong hung dữ trong |  | chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): trái tim nhân hậu đầy tình phụ tử bên trong khối cơ bắp 200kg làm con người nghiêng mình |
| b08 | 01:16.6–01:30.4 (13.8s) | L44 | phim ảnh viễn tưởng. Một trái tim quả cảm đầy tình phụ tử nằm bên trong khối cơ bắp thép nguội 200kg! Đó chính là phẩm chất cao quý nhất làm nên vị thế của một vị vua chân chính của núi rừng bao la, khiến con người chúng ta khi đứng trước chúng | **200kg** · Khối lượng nhà vô địch · R/320 · [0.8, 0.4] | chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): bản lĩnh của kẻ mạnh đích thực: Sức mạnh càng lớn lòng vị tha càng cao thượng |
| b09 | 01:30.4–01:43.3 (12.9s) | L45 | cũng phải nghiêng mình kính phục! Sức mạnh càng lớn thì lòng vị tha và tinh thần che chở càng phải cao thượng! Đó chính là nguyên lý sinh tồn cốt lõi giúp giống loài khỉ đột lưng bạc tồn tại kiên cường qua suốt bao kỷ nguyên thăng trầm của lịch sử tự nhiên. |  | bình luận viên thể thao mặc vest lịch lãm cầm micro hò hét cuồng nhiệt: bình luận viên nghẹn ngào xúc động tôn vinh vị vua nhân từ của núi rừng |

### scene06 · KHÉP LẠI MÙA GIẢI 50 TẬP HUYỀN THOẠI · 80.2s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.2 (7.2s) | L46 | Từ chiếc bụng lò phản ứng vi sinh vật biến lá cây thành sức mạnh 800kg phi thường, lực cắn sấm sét 1300 PSI đơn vị vượt xa chúa |  | chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): bức chân dung toàn cảnh khỉ đột lưng bạc với chiếc đai vàng vô địch trên đỉnh núi |
| b02 | 00:07.2–00:17.0 (9.8s) | L47 | sơn lâm, tiếng đập ngực rền vang một cây số rung chuyển rừng già, cho đến tâm hồn nhân từ của một vị vua bảo hộ gia đình, Vua Đấu Trường Rừng Rậm đã chứng minh cho toàn thế giới thấy rằng: Sức mạnh cơ |  | chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): sơ đồ tổng kết cơ khí sinh học: cơ bắp 800kg, lò vi sinh 70% calo, lực cắn 1300 PSI |
| b03 | 00:17.0–00:27.4 (10.4s) | L48 | bắp đích thực bắt nguồn từ sự giản dị thuần khiết của tự nhiên, và quyền lực tối thượng luôn đi liền với lòng vị tha và tinh thần trách nhiệm bảo vệ kẻ yếu! Khối cơ bắp phi thường 800kg ấy không phải |  | bình luận viên thể thao mặc vest lịch lãm cầm micro hò hét cuồng nhiệt: bình luận viên tuyên bố khép lại mốc son chói lọi 50 tập phim huyền thoại |
| b04 | 00:27.4–00:37.1 (9.7s) | L49 | là công cụ để thống trị hay áp bức, mà là tấm lá chắn thiêng liêng để bảo bọc sự bình yên cho cả gia đình thân yêu. Tập phim thứ 50 ngày hôm nay cũng chính là mốc son chói lọi khép lại trọn vẹn |  | chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): khỉ đột giơ cao hai nắm đấm thép hướng lên bầu trời rực sáng pháo hoa chiến thắng |
| b05 | 00:37.1–00:47.3 (10.2s) | L50 | chuỗi hành trình 50 tập phim khám phá thế giới động vật kỳ thú của kênh chúng tôi! Trải qua 50 bài học sinh tồn phi thường, từ những sinh vật biển sâu tăm tối cho đến những pháo đài rải gai và đấu trường |  | bình luận viên thể thao mặc vest lịch lãm cầm micro hò hét cuồng nhiệt: bài học về sức mạnh bắt nguồn từ sự giản dị thuần khiết và trách nhiệm bảo vệ kẻ yếu |
| b06 | 00:47.3–00:57.3 (10.0s) | L51 | rừng rậm, chúng ta đã cùng nhau chứng kiến những tuyệt tác tiến hóa vĩ đại nhất của tạo hóa. Xin chân thành cảm ơn sự đồng hành cuồng nhiệt của toàn thể quý vị khán giả! Hãy tiếp tục rèn luyện cho mình một |  | bình luận viên thể thao mặc vest lịch lãm cầm micro hò hét cuồng nhiệt cụ già kể chuyện vuốt râu trầm trồ trước lực cắn của khỉ đột chàng trai ngơ ngác ôm xô bột đạm whey protein đứng ngỡ ngàng bé con tò mò ngước nhìn gã khổng lồ hiền lành nằm chơi với con nhỏ: toàn bộ đại gia đình nhân vật cùng khỉ đột vẫy tay chào tạm biệt khán giả |
| b07 | 00:57.3–01:06.8 (9.5s) | L52 | thể lực sung mãn, một ý chí kiên định và một trái tim nhân ái như chú khỉ đột lưng bạc nhé! Đừng quên để lại bình luận và chia sẻ tình yêu thiên nhiên kỳ diệu này! Hẹn gặp lại các bạn trong những |  | chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): khỉ đột khẽ mỉm cười thân thiện gửi lời cảm ơn tới hàng triệu khán giả đồng hành |
| b08 | 01:06.8–01:20.2 (13.4s) | L53 | siêu phẩm hoang dã tiếp theo! Nhìn lại chặng đường 50 tập phim đã qua, chúng tôi vô cùng tự hào và xúc động khi được cùng các bạn mở toang những cánh cửa kỳ diệu nhất của thế giới tự nhiên. Hãy giữ vững ngọn lửa đam mê khám phá và sống một cuộc đời tràn đầy bản lĩnh nhé! |  | chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép: logo vàng rực 50 TẬP PHIM HOÀN TẤT nhá hàng những chuỗi video tổng hợp Mega đặc biệt |

## 5. Phân cảnh Shorts — từng beat

Banner: **CHỈ ĂN LÁ CÂY / CƠ BẮP 800KG?!** · giọng 48.0s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Chỉ ăn toàn lá cây rừng và chồi tre non xơ |  |
| s02 | 00:02.6 | S01b | xác, tại sao Khỉ Đột Lưng Bạc lại sở hữu cơ bắp cuồn cuộn nâng được vật nặng 800kg?! |  |
| s03 | 00:08.0 | S02 | Hãy nhìn Vua Đấu Trường Rừng Rậm nặng tới 200kg này xem! |  |
| s04 | 00:11.7 | S03 | Cơ bắp của nó khỏe gấp 4-9 lần một người đàn ông lực lưỡng, |  |
| s05 | 00:15.1 | S03b | với lực cắn 1300 PSI đơn vị mạnh gấp đôi cả chúa sơn lâm sư tử châu Phi! |  |
| s06 | 00:19.3 | S04 | Bí mật sức mạnh không nằm ở thức ăn giàu đạm mà ẩn giấu bên trong chiếc bụng bự tròn vo của |  |
| s07 | 00:23.9 | S05 | nó! Bên trong ruột già khổng lồ chứa hàng ngàn tỷ vi khuẩn kỵ khí lên men, biến chất xơ cellulose khó tiêu của 20kg |  |
| s08 | 00:30.6 | S05b | lá cây mỗi ngày thành các phân tử axit béo giàu năng lượng, cung cấp tới 70% tổng calo cho toàn bộ cơ thể! |  |
| s09 | 00:37.1 | S06 | Khi thị uy, nó đứng thẳng hai chân đập khum tay vào ngực, tạo ra những |  |
| s10 | 00:40.8 | S07 | đợt sóng âm sấm sét vang xa hơn một cây số để cảnh cáo kẻ thù! |  |
| s11 | 00:44.4 | S08 | Một cỗ máy cơ bắp ăn chay thuần túy bất khả chiến bại của tạo hóa! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chào mừng toàn thể hàng triệu khán giả cuồng nhiệt đang theo dõi buổi phát sóng trực tiếp từ đài thể thao đỉnh cao thế giới hoang dã! Tôi là bình luận viên chuyên nghiệp đang có mặt tại". Bố cục: bình luận viên thể thao mặc vest lịch lãm cầm micro hò hét cuồng nhiệt: bình luận viên thể thao cuồng nhiệt chĩa micro gào thét trước sàn đấu sương mù Virunga
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "sàn đấu núi lửa Virunga mù sương ở Trung Phi. Hãy nhìn vào góc võ đài màu đỏ đằng kia xem, một võ sĩ giác đấu khổng lồ nặng tới 200kg đang lừng lững bước ra với chiếc lưng ánh bạc lấp lánh như thép tôi! Cánh tay vượn dài 2m với những bó". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): võ sĩ khổng lồ 200kg bước ra sàn đấu với chiếc lưng ánh bạc lấp lánh như thép tôi
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "cơ bắp cuồn cuộn gân guốc, cơ ngực nở nang săn chắc như hai tấm khiên đồng La Mã. Người đời gọi nó là Khỉ Đột Lưng Bạc, nhưng trên bảng xếp hạng các nhà vô địch sinh tồn của chúng tôi, đây chính là Vua Đấu Trường Rừng Rậm! Một cú đấm sấm". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): cánh tay vượn dài 2 mét với những bó cơ bắp cuồn cuộn gân guốc bẻ cong xà beng thép
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "sét của gã có thể làm cong vênh thanh xà beng bằng thép đặc và nâng bổng một chiếc xe hơi nặng 800kg lên không trung một cách nhẹ nhàng! Hãy nhớ rằng các lực sĩ cử tạ khỏe nhất thế giới loài người phải đeo đai lưng bảo hộ, quấn băng cổ tay". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): khỉ đột dùng một tay nhấc bổng khúc gỗ nặng 800kg thong thả như cầm một cuốn sách
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "và hít thở trợ lực cật lực mới có thể nâng được mức tạ 500kg trong vài giây ngắn ngủi. Trong khi đó, gã khổng lồ này chỉ cần dùng một tay nhấc bổng khúc gỗ nặng 800kg một cách thong thả như chúng ta cầm một cuốn sách! Alo bình luận viên ơi,". Bố cục: chàng trai ngơ ngác ôm xô bột đạm whey protein đứng ngỡ ngàng: chú ngơ ngác ôm xô đạm whey protein đứng chết trân trước khẩu phần ăn chay của khỉ đột
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "võ sĩ khổng lồ này ngày nào cũng nốc hàng chục xô đạm whey protein để nuôi cơ bắp hả? Nhầm to rồi người anh em ngơ ngác ơi, một sự nhầm lẫn thế kỷ của dân tập gym! Võ sĩ vô địch Vua Đấu Trường Rừng Rậm của chúng ta là một người". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): khỉ đột ngồi nhai lá cây rừng chồi tre non xơ xác với nụ cười sảng khoái
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "ăn chay thuần túy 100%! Cả cuộc đời của nó chưa từng chạm vào một miếng ức gà, chẳng hề đụng đến một muỗng bột đạm công nghiệp, mà thức ăn hàng ngày chỉ toàn là lá cây rừng cay đắng, chồi tre non xơ xác và cọng cần tây dại! Vậy mà khối". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): sơ đồ so sánh sức mạnh cơ bắp gấp 4-9 lần người đàn ông lực lưỡng nhất
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "cơ bắp của nó lại khỏe gấp 4-9 lần một người đàn ông lực lưỡng nhất hành tinh! Bí mật đen tối nào đang được che giấu bên trong chiếc bụng to tròn lùm lùm như một quả bom nổ chậm kia? Ngay bây giờ, hãy nổi hồi chuông bắt đầu trận đấu và". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): mật độ xương dày đặc gấp 3 lần và dây gân bọc thép chịu tải động năng cực hạn
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "cùng chúng tôi đột nhập vào khoang lò phản ứng sinh học bí mật này! Mật độ xương đùi và xương cẳng tay của nó dày đặc gấp ba lần xương người, được bọc ngoài bởi những dải gân dày như dây cáp tời thép, tạo nên một khung đỡ cơ học hoàn hảo để truyền tải những nguồn động năng khổng lồ mà không sợ bị gãy nứt.". Bố cục: bình luận viên thể thao mặc vest lịch lãm cầm micro hò hét cuồng nhiệt chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): bình luận viên chỉ tay vào chiếc bụng to tròn căng phồng như lò phản ứng sinh học
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Các khán giả sành sỏi hãy nhìn kỹ vào vóc dáng của Vua Đấu Trường Rừng Rậm! Mặc dù sở hữu đôi bắp tay cuồn cuộn như đá tảng, nhưng vòng eo của nó hoàn toàn". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): vóc dáng bệ vệ của khỉ đột với chiếc bụng to tròn căng phồng lùm lùm như chiếc trống cái
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "không hề có cơ bụng 6 múi săn chắc như các người mẫu thể hình thời nay. Ngược lại, nó vác một chiếc bụng to tròn, căng phồng và lùm lùm như một chiếc trống cái. Đừng vội chê nó béo phì nhé quý vị! Chiếc bụng bự ấy chính là". Bố cục: sơ đồ lò phản ứng vi sinh vật manh tràng ruột già tỏa năng lượng đỏ rực trong bụng khỉ đột: sơ đồ cắt ngang khoang bụng cho thấy lò phản ứng lên men ruột sau tỏa sáng rực lửa
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "một khoang lò phản ứng sinh học tối tân mang tên hệ thống lên men ruột sau, nơi hàng ngàn tỷ vi sinh vật kỵ khí đang làm việc tăng ca 24/24 giờ không ngừng nghỉ! Chiếc bụng to tròn ấy chiếm tới gần 60% tổng thể tích toàn bộ đường". Bố cục: sơ đồ lò phản ứng vi sinh vật manh tràng ruột già tỏa năng lượng đỏ rực trong bụng khỉ đột: ruột già khổng lồ chiếm 60% thể tích tiêu hóa với hàng tỷ vi sinh vật kỵ khí tăng ca
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tiêu hóa, trong khi ở con người chúng ta ruột già chỉ chiếm vỏn vẹn 20%. Mỗi ngày, chú khỉ đột trưởng thành này phải nhai ngấu nghiến tới 20kg lá cây và cỏ dại. Trong dạ dày người chúng ta, chất xơ thô cellulose là thứ hoàn toàn không thể". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): đống lá cây 20kg được nhai vụn đưa vào thùng ủ bia sinh học manh tràng
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tiêu hóa được và bị tống thẳng ra ngoài. Nhưng ở Vua Đấu Trường Rừng Rậm, đoạn manh tràng và ruột già khổng lồ của nó lại là một thùng ủ bia sinh học hoàn hảo. Hàng tỷ vi khuẩn chuyên biệt tại đây sẽ tiết ra các enzym cắt vụn". Bố cục: sơ đồ lò phản ứng vi sinh vật manh tràng ruột già tỏa năng lượng đỏ rực trong bụng khỉ đột: các enzym vi khuẩn cắt đứt liên kết xen-lu-lô-zơ tạo ra axit béo chuỗi ngắn giàu năng lượng
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "các liên kết chất xơ cellulose cứng đầu, biến chúng thành các phân tử axit béo chuỗi ngắn cực kỳ giàu năng lượng! Không chỉ chuyển hóa chất xơ thành calo, đàn vi sinh vật kỵ khí này còn có khả năng tự tổng hợp ra các axit amin thiết yếu và các loại vitamin nhóm B quan trọng,". Bố cục: sơ đồ lò phản ứng vi sinh vật manh tràng ruột già tỏa năng lượng đỏ rực trong bụng khỉ đột: đàn vi khuẩn tự tổng hợp axit amin thiết yếu và vitamin B nuôi dưỡng tế bào cơ bắp nạc
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "trực tiếp tái tạo các khối protein nuôi dưỡng từng tế bào cơ bắp nạc cho chú khỉ đột. Những axit béo kỳ diệu này được niêm mạc ruột hấp thụ trực tiếp và cung cấp tới 70% tổng nhu cầu calo mỗi ngày cho toàn bộ cơ thể khổng lồ 200kg. Nó không cần ăn mỡ động vật hay uống". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): dòng năng lượng tinh khiết hấp thụ qua niêm mạc ruột cung cấp 70% tổng calo cơ thể
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "sữa tăng cơ, bởi vì chính đàn vi sinh vật trong bụng đã tự tay sản xuất ra nguồn năng lượng tinh khiết nhất để nuôi dưỡng từng thớ cơ bắp thép nguội. Chiếc bụng to tướng ấy không phải mỡ thừa, mà là một nhà máy phát điện sinh học độc nhất vô nhị của rừng rậm nhiệt đới!". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): khỉ đột ngồi thong dong 4-6 tiếng mỗi ngày nhai lá tre trúc nuôi dưỡng khối cơ bắp thép
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mỗi ngày nó dành tới 4-6 tiếng đồng hồ chỉ để thong dong ngồi nhai và tiêu hóa, biến những cánh rừng tre trúc xanh tươi thành nguồn nhiên liệu sinh học vô tận nuôi dưỡng cỗ máy trò chơi đuổi bắt bất khả chiến bại.". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): nhà máy phát điện sinh học độc nhất vô nhị biến lá cây thành sức mạnh vô song
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bây giờ mời quý khán giả hướng mắt về bảng đo lực điện tử đặt ngay giữa sàn đấu! Khi một con khỉ đột đực vào cơn thịnh nộ, nó có thể tung ra những đòn đánh với sức". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): bảng đo lực điện tử vỡ nát trước cú đấm tàn phá làm sập bức tường gạch dày
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "công phá làm sập cả một bức tường gạch dày. Cấu trúc bắp tay của Vua Đấu Trường Rừng Rậm được cấu tạo chủ yếu từ các sợi cơ co rút nhanh màu trắng, tối ưu hóa cho những cú bộc phát sức mạnh tột đỉnh trong tích tắc. Một con đực trưởng thành". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): sợi cơ co rút nhanh màu trắng bộc phát sức mạnh tột đỉnh trong tích tắc
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "có thể dùng hai tay không bẻ gãy gập một thân cây chuối rừng to bằng bắp đùi người lớn chỉ bằng một cú vặn nhẹ nhàng như bẻ một que tăm! Chiều dài sải tay vượt trội cùng với khớp vai linh hoạt tuyệt đối cho phép nó tung ra những cú đấm". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh) thân cây chuối rừng to bằng bắp đùi bị bẻ gãy gập làm đôi: khỉ đột dùng hai tay không bẻ gãy gập thân cây chuối to bằng bắp đùi người lớn
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "móc vòng cung với vận tốc bộc phát xé toạc không gian, tạo ra một vùng sát thương cận chiến tuyệt đối trong bán kính 2m. Này các cháu ơi, ngày xưa ông từng thấy nó cắn nát quả dừa khô cứng ngắc trong một nốt nhạc, răng có bọc titan không? Kính thưa". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): sải tay dài 2.5 mét tạo ra vùng sát thương cận chiến tuyệt đối quét sạch đối thủ
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "cụ già kể chuyện, hàm răng của nó còn đáng sợ hơn cả kim loại nhân tạo nữa ạ! Nhờ có một gờ xương đỉnh đầu nhô cao như một chiếc mào gà bằng đá, nơi bám của những bó cơ nhai khổng lồ, lực cắn của Vua Đấu Trường Rừng Rậm đo được". Bố cục: cụ già kể chuyện vuốt râu trầm trồ trước lực cắn của khỉ đột: cụ già kể chuyện vuốt râu nhớ lại cảnh khỉ đột cắn nát quả dừa khô cứng ngắc
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "lên tới 1300 PSI đơn vị, tức là mạnh gấp đôi lực cắn của một con sư tử châu Phi và gấp bốn lần một người trưởng thành! Một cú cắn của nó thừa sức nghiền nát cành gỗ lim cứng nhất hoặc nghiền vụn xương ống chân của thú dữ trong chớp mắt". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): gờ xương đỉnh đầu nhô cao như mào gà bằng đá làm điểm tựa cho cơ nhai khổng lồ
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "mà không hề mẻ một chiếc răng nanh nào! Khi hai hàm răng này khép chặt lại, áp lực tại điểm tiếp xúc tương đương với việc đặt một chiếc xe hơi bốn chỗ đè nặng lên một diện tích nhỏ bằng đầu ngón tay cái, đủ sức bóp vụn mọi lớp vỏ giáp". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): đồng hồ đo lực cắn chỉ con số 1300 PSI mạnh gấp đôi chúa sơn lâm sư tử
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bảo vệ cứng cáp nhất. Kết hợp với sải tay dài hơn 2.5m và trọng tâm cơ thể cực thấp vững chãi như một chiếc xe tăng lội nước, con vật có thể nâng bổng những tảng đá hoa cương nặng tới 800kg rồi ném xa hàng mét. Bất kỳ đối thủ nào dám bước chân vào cự ly". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): khỉ đột nâng bổng tảng đá hoa cương 800kg ném xa hàng mét với trọng tâm vững chãi
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "cận chiến với gã khổng lồ này đều sẽ phải nếm trải cảm giác bị một cỗ máy nghiền đá ép nát toàn bộ khung xương! Trọng tâm cơ thể cực thấp dồn vào bốn chi vững chãi như bốn cột trụ móng nhà, khiến nó hầu như không bao giờ bị mất thăng bằng hay bị quật ngã trong bất kỳ cuộc giao tranh sinh tử nào giữa núi rừng.". Bố cục: bình luận viên thể thao mặc vest lịch lãm cầm micro hò hét cuồng nhiệt: bình luận viên ngả mũ thán phục trước cỗ máy nghiền đá bất khả chiến bại
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bùm! Bùm! Bùm! Bùm! Tiếng sấm rền từ đâu vang lên làm rung chuyển cả thung lũng sương mù Virunga! Hãy nhìn vào màn sương dày đặc kia, Vua Đấu Trường Rừng Rậm". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): sấm rền vang dội thung lũng khi khỉ đột vươn cao lồng ngực vĩ đại đập liên hồi 20 cú mỗi giây
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "đang đứng thẳng bằng hai chân sau, vươn cao lồng ngực vĩ đại và dùng hai bàn tay khum lại đập liên hồi vào ngực với tốc độ 20 cú đập mỗi giây! Đây chính là nghi thức vỗ ngực kinh điển mang tính thương hiệu toàn cầu". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): con vật nhổ bật bụi cây ném về phía trước chạy ngang thị uy dũng mãnh
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "của loài khỉ đột lưng bạc! Màn trình diễn này bắt đầu bằng việc con vật đứng thẳng người, nhổ bật một bụi cây xung quanh rồi ném mạnh về phía trước, tiếp theo là một màn bứt tốc chạy ngang đầy thị uy trước khi tung ra". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): góc quay chậm cho thấy bàn tay khum tròn như chiếc bát úp tạo luồng sóng âm trầm đục
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "cú đập ngực sấm sét rung chuyển trời đất. Nhiều người lầm tưởng rằng chúng dùng nắm đấm thép đấm huỳnh huỵch vào ngực để khoe khoang sự hung bạo. Nhưng góc quay phân tích chuyển động chậm của chúng tôi cho thấy: Bàn tay của nó khum". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): sơ đồ túi khí thanh quản khổng lồ dung tích vài lít đóng vai trò buồng cộng hưởng âm thanh
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tròn lại như một chiếc bát úp! Bên dưới lớp da ngực dày cộp là các túi khí thanh quản khổng lồ hoạt động giống hệt như những chiếc trống lục lạc cộng hưởng âm thanh. Mỗi cú đập khum tay tạo ra những luồng sóng âm trầm". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): luồng sóng âm trầm sâu xuyên thấu qua tán lá rậm rạp vang xa hơn 1 kilomet
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "đục vang xa tới hơn một cây số xuyên qua rừng rậm dày đặc! Những túi khí thanh quản này có thể tích chứa lên tới vài lít không khí, hoạt động đồng điệu với nhịp đập bàn tay để tạo nên những tần số âm thanh cộng". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh) báo hoa mai gầm gừ hoảng hốt lùi bước trước bóng lưng bạc: những con đực trẻ và báo hoa mai nghe tiếng sấm rền từ xa lập tức cúi đầu rút lui
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "hưởng trầm sâu có sức xuyên thấu phi thường qua tán lá rậm rạp. Âm thanh trầm đục này chứa đựng các thông số sinh học chính xác về kích thước cơ thể, dung tích phổi và đẳng cấp sức mạnh của con đực đầu đàn. Những con đực trẻ tuổi". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): giải pháp ngoại giao bằng âm thanh đỉnh cao bảo tồn sinh lực cho toàn thể bầy đàn
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "ngỗ nghịch khi nghe thấy tiếng trống ngực uy dũng này từ xa sẽ lập tức biết thân biết phận mà cúi đầu rút lui, tránh được những cuộc chiến đẫm nước màu không cần thiết. Đó là một giải pháp ngoại giao bằng âm thanh đỉnh cao, vừa phô diễn sức mạnh vô song,". Bố cục: bình luận viên thể thao mặc vest lịch lãm cầm micro hò hét cuồng nhiệt: bình luận viên nín thở thán phục bản lĩnh của vị vua đầu đàn rừng rậm
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "vừa bảo tồn sinh lực cho toàn thể bầy đàn! Đây chính là nghệ thuật trò chơi đuổi bắt tâm lý đỉnh cao: Đánh bại đối thủ từ trong tư tưởng trước khi một giọt nước màu nào kịp rơi, khẳng định vị thế thủ lĩnh tối cao mà không làm tiêu hao dù chỉ 1% sinh lực quý giá của bầy đàn.". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): khỉ đột đứng sừng sững giữa đỉnh đèo Virunga uy nghiêm bất khả xâm phạm
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Mặc dù sở hữu sức mạnh hủy diệt có thể hạ gục cả một con báo hoa mai trưởng thành chỉ bằng một cú tát trời giáng, nhưng bản chất thực sự của Vua Đấu". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): gã khổng lồ nằm phơi nắng trên thảm cỏ xanh nhẹ nhàng chải lông cho khỉ con tinh nghịch
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trường Rừng Rậm lại là một người khổng lồ cực kỳ hiền lành, trầm tĩnh và giàu lòng trắc ẩn. Chúng dành phần lớn thời gian trong ngày để nằm phơi nắng trên những thảm cỏ xanh, nhẹ nhàng chải lông cho những chú khỉ đột con tinh nghịch trèo". Bố cục: bé con tò mò ngước nhìn gã khổng lồ hiền lành nằm chơi với con nhỏ: bé con tò mò mỉm cười thích thú thấy gã khổng lồ nằm chơi đùa cùng bầy con nhỏ
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "lên đầu lên cổ mình, và chia sẻ những chồi măng non ngon lành cho các con mái trong bầy. Những nhà linh trưởng học huyền thoại từng dành cả đời sống cạnh các gia đình khỉ đột hoang dã đều khẳng định rằng: Đây là một trong những loài". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): khỉ đột chia sẻ chồi măng non ngon lành cho các con mái và con non trong bầy
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "sinh vật sống tình cảm, thấu hiểu và hòa bình nhất từng bước đi trên hành tinh của chúng ta. Ủa chú ơi, gã khổng lồ cơ bắp cuồn cuộn này cũng dịu dàng nằm chơi với con nhỏ giống bố cháu ở nhà hả? Chúng không bao giờ chủ". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): ánh mắt trầm tư đầy thấu cảm của vị vua đầu đàn xóa tan định kiến quái vật chú khỉ đột hoạt hình khổng lồ
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "động gây chiến hay ức hiếp những sinh vật nhỏ bé xung quanh. Những màn gầm rú hay đập ngực thị uy thực chất chỉ là những lời cảnh cáo nhân từ cuối cùng để kẻ xâm nhập biết đường rút lui trong hòa bình. Nhưng một khi gia đình". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): khi bầy con bị đe dọa khỉ đột hóa thân thành bức tường thành che chở đàn con đến cùng
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "của nó bị đe dọa bởi những tên săn trộm tàn độc hay bầy thú ăn thịt đói khát, gã khổng lồ hiền lành ấy sẽ lập tức hóa thân thành một bức tường thành bất khả xâm phạm, sẵn sàng hứng trọn mọi mũi giáo và đạn lửa". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): nắm đấm thép sẵn sàng nghênh chiến lũ săn trộm để bảo vệ bình yên gia đình
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "để che chở cho từng đứa con bé bỏng đến hơi thở cuối cùng! Ánh mắt trầm tư đầy thấu cảm của một con đực đầu đàn khi nhìn đứa con thơ chập chững biết đi chứa đựng một vẻ đẹp nhân văn sâu sắc, xóa tan hoàn toàn mọi định kiến thô bạo về quái thú chú khỉ đột hoạt hình khổng lồ hung dữ trong phim ảnh". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): trái tim nhân hậu đầy tình phụ tử bên trong khối cơ bắp 200kg làm con người nghiêng mình
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "viễn tưởng. Một trái tim quả cảm đầy tình phụ tử nằm bên trong khối cơ bắp thép nguội 200kg! Đó chính là phẩm chất cao quý nhất làm nên vị thế của một vị vua chân chính của núi rừng bao la, khiến con người chúng ta khi đứng trước chúng cũng phải". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): bản lĩnh của kẻ mạnh đích thực: Sức mạnh càng lớn lòng vị tha càng cao thượng
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nghiêng mình kính phục! Sức mạnh càng lớn thì lòng vị tha và tinh thần che chở càng phải cao thượng! Đó chính là nguyên lý sinh tồn cốt lõi giúp giống loài khỉ đột lưng bạc tồn tại kiên cường qua suốt bao kỷ nguyên thăng trầm của lịch sử tự nhiên.". Bố cục: bình luận viên thể thao mặc vest lịch lãm cầm micro hò hét cuồng nhiệt: bình luận viên nghẹn ngào xúc động tôn vinh vị vua nhân từ của núi rừng
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Từ chiếc bụng lò phản ứng vi sinh vật biến lá cây thành sức mạnh 800kg phi thường, lực cắn sấm sét 1300 PSI đơn vị vượt xa chúa sơn". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): bức chân dung toàn cảnh khỉ đột lưng bạc với chiếc đai vàng vô địch trên đỉnh núi
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "lâm, tiếng đập ngực rền vang một cây số rung chuyển rừng già, cho đến tâm hồn nhân từ của một vị vua bảo hộ gia đình, Vua Đấu Trường Rừng Rậm đã chứng minh cho toàn thế giới thấy rằng: Sức mạnh cơ bắp". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): sơ đồ tổng kết cơ khí sinh học: cơ bắp 800kg, lò vi sinh 70% calo, lực cắn 1300 PSI
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "đích thực bắt nguồn từ sự giản dị thuần khiết của tự nhiên, và quyền lực tối thượng luôn đi liền với lòng vị tha và tinh thần trách nhiệm bảo vệ kẻ yếu! Khối cơ bắp phi thường 800kg ấy không phải là công". Bố cục: bình luận viên thể thao mặc vest lịch lãm cầm micro hò hét cuồng nhiệt: bình luận viên tuyên bố khép lại mốc son chói lọi 50 tập phim huyền thoại
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "cụ để thống trị hay áp bức, mà là tấm lá chắn thiêng liêng để bảo bọc sự bình yên cho cả gia đình thân yêu. Tập phim thứ 50 ngày hôm nay cũng chính là mốc son chói lọi khép lại trọn vẹn chuỗi". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): khỉ đột giơ cao hai nắm đấm thép hướng lên bầu trời rực sáng pháo hoa chiến thắng
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "hành trình 50 tập phim khám phá thế giới động vật kỳ thú của kênh chúng tôi! Trải qua 50 bài học sinh tồn phi thường, từ những sinh vật biển sâu tăm tối cho đến những pháo đài rải gai và đấu trường rừng". Bố cục: bình luận viên thể thao mặc vest lịch lãm cầm micro hò hét cuồng nhiệt: bài học về sức mạnh bắt nguồn từ sự giản dị thuần khiết và trách nhiệm bảo vệ kẻ yếu
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "rậm, chúng ta đã cùng nhau chứng kiến những tuyệt tác tiến hóa vĩ đại nhất của tạo hóa. Xin chân thành cảm ơn sự đồng hành cuồng nhiệt của toàn thể quý vị khán giả! Hãy tiếp tục rèn luyện cho mình một thể". Bố cục: bình luận viên thể thao mặc vest lịch lãm cầm micro hò hét cuồng nhiệt cụ già kể chuyện vuốt râu trầm trồ trước lực cắn của khỉ đột chàng trai ngơ ngác ôm xô bột đạm whey protein đứng ngỡ ngàng bé con tò mò ngước nhìn gã khổng lồ hiền lành nằm chơi với con nhỏ: toàn bộ đại gia đình nhân vật cùng khỉ đột vẫy tay chào tạm biệt khán giả
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "lực sung mãn, một ý chí kiên định và một trái tim nhân ái như chú khỉ đột lưng bạc nhé! Đừng quên để lại bình luận và chia sẻ tình yêu thiên nhiên kỳ diệu này! Hẹn gặp lại các bạn trong những siêu". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): khỉ đột khẽ mỉm cười thân thiện gửi lời cảm ơn tới hàng triệu khán giả đồng hành
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "phẩm hoang dã tiếp theo! Nhìn lại chặng đường 50 tập phim đã qua, chúng tôi vô cùng tự hào và xúc động khi được cùng các bạn mở toang những cánh cửa kỳ diệu nhất của thế giới tự nhiên. Hãy giữ vững ngọn lửa đam mê khám phá và sống một cuộc đời tràn đầy bản lĩnh nhé!". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép: logo vàng rực 50 TẬP PHIM HOÀN TẤT nhá hàng những chuỗi video tổng hợp Mega đặc biệt
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Chỉ ăn toàn lá cây rừng và chồi tre non xơ xác,". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): khỉ đột lưng bạc hoạt hình ngồi thong thả nhai lá cây rừng và chồi tre non
```
</details>

<details><summary>S01b</summary>

```text
HÌNH S01b (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "tại sao Khỉ Đột Lưng Bạc lại sở hữu cơ bắp cuồn cuộn nâng được vật nặng 800kg?!". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép: cận cảnh khỉ đột lưng bạc gồng bắp tay cuồn cuộn nâng tảng đá 800kg
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Hãy nhìn Vua Đấu Trường Rừng Rậm nặng tới 200kg này xem!". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép: toàn cảnh khỉ đột 200kg đứng sừng sững uy nghi trên đỉnh núi Virunga
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Cơ bắp của nó khỏe gấp 4-9 lần một người đàn ông lực lưỡng,". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): so sánh cơ bắp khỉ đột gấp 4-9 lần người đàn ông lực lưỡng
```
</details>

<details><summary>S03b</summary>

```text
HÌNH S03b (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "với lực cắn 1300 PSI đơn vị mạnh gấp đôi cả chúa sơn lâm sư tử châu Phi!". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): khỉ đột há miệng khoe răng nanh cắn nát quả dừa khô với lực cắn 1300 PSI gấp đôi sư tử
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Bí mật sức mạnh không nằm ở thức ăn giàu đạm mà ẩn giấu bên trong chiếc bụng bự tròn vo của nó!". Bố cục: sơ đồ lò phản ứng vi sinh vật manh tràng ruột già tỏa năng lượng đỏ rực trong bụng khỉ đột: chiếc bụng to tròn chứa lò phản ứng lên men hàng ngàn tỷ vi khuẩn
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Bên trong ruột già khổng lồ chứa hàng ngàn tỷ vi khuẩn kỵ khí lên men, biến chất xơ cellulose khó tiêu của 20kg". Bố cục: sơ đồ lò phản ứng vi sinh vật manh tràng ruột già tỏa năng lượng đỏ rực trong bụng khỉ đột: ruột già khổng lồ chứa hàng ngàn tỷ vi khuẩn kỵ khí lên men chất xơ
```
</details>

<details><summary>S05b</summary>

```text
HÌNH S05b (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "lá cây mỗi ngày thành các phân tử axit béo giàu năng lượng, cung cấp tới 70% tổng calo cho toàn bộ cơ thể!". Bố cục: sơ đồ lò phản ứng vi sinh vật manh tràng ruột già tỏa năng lượng đỏ rực trong bụng khỉ đột: chất xơ 20kg lá cây biến thành axit béo cung cấp 70% calo cho cơ bắp
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Khi thị uy, nó đứng thẳng hai chân đập khum tay vào ngực, tạo ra những đợt". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh): khỉ đột đứng thẳng đập khum tay vào ngực tạo sóng âm rền vang 1 kilomet
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "sóng âm sấm sét vang xa hơn một cây số để cảnh cáo kẻ thù!". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép: khỉ đột đeo đai vô địch WWE mạ vàng mỉm cười nâng cúp chiến thắng
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Một cỗ máy cơ bắp ăn chay thuần túy bất khả chiến bại của tạo hóa!". Bố cục: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh đeo đai vô địch WWE mạ vàng giơ nắm đấm thép bình luận viên thể thao mặc vest lịch lãm cầm micro hò hét cuồng nhiệt: bình luận viên cùng khỉ đột giơ hai tay ăn mừng cột mốc 50 tập phim huyền thoại
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/53 của video YouTube về Khỉ Đột Lưng Bạc). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa vẽ tay đặc trưng cho chủ đề, nét mực sắc nét, màu sắc tương phản cuốn hút, tối giản giàu tính biểu tượng khoa học; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh). Nhân vật phụ cố định: bình luận viên thể thao mặc vest lịch lãm cầm micro hò hét cuồng nhiệt; cụ già kể chuyện vuốt râu trầm trồ trước lực cắn của khỉ đột; chàng trai ngơ ngác ôm xô bột đạm whey protein đứng ngỡ ngàng; bé con tò mò ngước nhìn gã khổng lồ hiền lành nằm chơi với con nhỏ; báo hoa mai gầm gừ hoảng hốt lùi bước trước bóng lưng bạc; thân cây chuối rừng to bằng bắp đùi bị bẻ gãy gập làm đôi; sơ đồ lò phản ứng vi sinh vật manh tràng ruột già tỏa năng lượng đỏ rực trong bụng khỉ đột. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/11 của video YouTube Shorts về Khỉ Đột Lưng Bạc). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa vẽ tay đặc trưng cho chủ đề, nét mực sắc nét, màu sắc tương phản cuốn hút, tối giản giàu tính biểu tượng khoa học; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú khỉ đột lưng bạc hoạt hình ngộ nghĩnh (thân hình khổng lồ 200kg, cơ bắp cuồn cuộn gân guốc, lưng ánh bạc lấp lánh như thép tôi, chiếc bụng to tròn chứa lò vi sinh). Nhân vật phụ: bình luận viên thể thao mặc vest lịch lãm cầm micro hò hét cuồng nhiệt; sơ đồ lò phản ứng vi sinh vật manh tràng ruột già tỏa năng lượng đỏ rực trong bụng khỉ đột. 
```
</details>

## 7. SEO

- **title:** Bí Mật Khỉ Đột Lưng Bạc: Ăn Chay Nhưng Cơ Bắp 800KG Gấp 10 Lần Người?! | Tập 50
- **hook_paragraph:** Khỉ Đột Lưng Bạc nặng 200kg chỉ ăn lá cây nhưng sở hữu cơ bắp nâng 800kg và lực cắn 1300 PSI gấp đôi sư tử. Làm thế nào chiếc bụng lò phản ứng lên men biến chất xơ thành khối cơ bắp siêu nhân?
- **question:** Bạn thấy điều gì ở Khỉ Đột Lưng Bạc ấn tượng nhất: Cơ bắp nâng 800kg chỉ nhờ ăn lá cây hay cú đập ngực rền vang 1km?
- **next_teaser:** Chúc mừng cột mốc 50 tập phim hoàn chỉnh! Hãy đón chờ chuỗi video tổng hợp Mega đặc biệt tiếp theo!
- **shorts_title:** Chỉ ăn lá cây nhưng cơ bắp nâng được 800kg?! 🦍 #shorts #khidot
- **shorts_desc:** Khỉ Đột Lưng Bạc chỉ ăn lá cây nhưng sở hữu cơ bắp nâng 800kg nhờ chiếc bụng lò phản ứng vi khuẩn lên men biến chất xơ thành năng lượng!
- **bullets:** Khối lượng 200kg với sức nâng 800kg gấp 4-9 lần người khỏe nhất · Hệ thống lên men ruột sau biến chất xơ thành 70% calo năng lượng · Lực cắn 1300 PSI nghiền nát thân cây và xương thú dữ · Nghi thức khum tay đập ngực tạo buồng âm vang xa hơn 1 km
- **tags:** khỉ đột lưng bạc, khi dot lung bac, silverback gorilla, co bap khi dot, khi dot an chay, the gioi dong vat, ve chuyen hoang da, dong vat ky thu, khoa hoc vui, suc manh khi dot, binh luan vien, tap 50
- **hashtags:** #KhiDotLungBac #SilverbackGorilla #TheGioiDongVat #VeChuyenHoangDa #KhoaHoc #Tap50

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-50-khi-dot-lung-bac
python src/episode/pipeline.py tts    projects/tap-50-khi-dot-lung-bac     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-50-khi-dot-lung-bac     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-50-khi-dot-lung-bac     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-50-khi-dot-lung-bac              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-50-khi-dot-lung-bac --force
python scripts/beat_sheet.py projects/tap-50-khi-dot-lung-bac               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-50-khi-dot-lung-bac/audio/shorts.wav projects/tap-50-khi-dot-lung-bac/renders/tap-50-khi-dot-lung-bac_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-50-khi-dot-lung-bac
python src/episode/pipeline.py seo    projects/tap-50-khi-dot-lung-bac
python src/episode/episode_doc.py     projects/tap-50-khi-dot-lung-bac
```
