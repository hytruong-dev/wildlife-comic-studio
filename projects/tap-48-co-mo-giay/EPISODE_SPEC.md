# TẬP 48 — CÒ MỎ GIÀY · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-48-co-mo-giay`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-48-co-mo-giay`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F4` · **Persona giọng:** `phong_vien_24h` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Cò Mỏ Giày |
| Tiêu đề YouTube | Tượng Đá Tiền Sử Cò Mỏ Giày: Cúi Chào Người Nhưng Tàn Nhẫn Với Em Ruột?! \| Tập 48 |
| Video dài | `renders/tap-48-co-mo-giay_long.mp4` — 10:05.1 (605.1s) |
| Shorts | `renders/tap-48-co-mo-giay_shorts.mp4` — 0:50.3 (50.3s) |
| Thumbnail | `renders/tap-48-co-mo-giay_thumbnail.jpg` |
| Số hình | dài 53 beat / 53 ảnh riêng; Shorts 10 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.12**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/53 của video YouTube về Cò Mỏ Giày). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa vẽ tay đặc trưng cho chủ đề, nét mực sắc nét, màu sắc tương phản cuốn hút, tối giản giàu tính biểu tượng khoa học; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động). Nhân vật phụ cố định: phóng viên chiến trường mặc áo gile chống đạn cầm sổ tay và micro; phát thanh viên tin tức trường quay đeo tai nghe chuyên nghiệp; chú ngơ ngác giật mình hoảng hốt bịt tai trước tiếng súng máy; chú cá phổi châu phi trơn trượt vây như mái chèo đang ngoi lên thở; cá sấu con hoảng sợ rụt đầu xuống bùn lầy; chú cò con anh lông xám hung hăng to lớn trong tổ; chú cò con em yếu ớt tội nghiệp kêu chít chít cầu cứu. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — 24 GIỜ THÂM NHẬP VÙNG ĐẤT CHẾT
*Thẻ chương:* SÁT THỦ ĐỨNG BẤT ĐỘNG 5 TIẾNG

*Badge:* `NHẬT KÝ CHIẾN TRƯỜNG` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene01_p0.wav` (960 ký tự) · mood `tram_bi_an`

```text
Chào mừng quý vị khán giả đang theo dõi bản tin hiện trường trực tiếp của kênh Truyền hình Sinh tồn Hoang dã! Tôi là phóng viên chiến trường đang có mặt tại đầm lầy Bangweulu heo hút giữa lục địa châu Phi, nơi màn sương mù dày đặc che phủ những vũng nước đen ngòm từ thời tiền sử. Hãy hạ thấp ống kính máy quay xuống mép lau sậy đằng kia xem! Trong làn sương mờ ảo, một bóng đen sừng sững cao gần một mét rưỡi đang đứng sừng sững như một tảng đá cẩm thạch xám xịt. Đôi mắt vàng đục vô cảm, bất động tuyệt đối, chẳng một sợi lông tơ lay động dù gió lốc đang thổi qua. Dân địa phương gọi nó là Cò Mỏ Giày, nhưng trong sổ tay tác nghiệp của tôi, sinh vật này mang mật danh rùng rợn: Tượng Đá Tiền Sử. Nó đang làm gì thế kia? Liệu nó còn sống hay đã hóa thạch từ kỷ Phấn Trắng? Mỗi hơi thở của nó chậm rãi đến mức mặt nước xung quanh phẳng lặng như tờ gương chẳng một gợn sóng lăn tăn, khiến mọi sinh vật bơi lội dưới chân đều hoàn toàn mất đi cảnh giác phòng thủ.
```
**Part 1** → `audio/vs/scene01_p1.wav` (93 ký tự) · 🎭 cameo `phat_thanh_vien`

```text
Alo trường quay nhắc phóng viên giữ an toàn, cảm biến báo nó vẫn thở nhưng nhịp tim cực thấp!
```
**Part 2** → `audio/vs/scene01_p2.wav` (869 ký tự) · mood `hao_hung`

```text
[laughter] Cảm ơn trường quay đã cảnh báo! [surprise-oh] Quý vị không nghe nhầm đâu, cỗ máy săn mồi này có thể đứng im như một khúc gỗ chết suốt ba tiếng, thậm chí năm tiếng đồng hồ liên tục mà không hề chớp mắt lấy một lần! Thậm chí những chú chim sẻ ngây thơ còn tưởng đây là cọc gỗ mục nên đã thản nhiên bay tới đậu lên đỉnh đầu của nó để rỉa lông. Nhưng đừng để sự tĩnh lặng ma mị này đánh lừa các giác quan của bạn! Dưới lớp vỏ bọc bằng đá ấy là một sát thủ phục kích tàn độc nhất thế giới đầm lầy, sẵn sàng kích hoạt một đòn tấn công sấm sét có thể chẻ đôi cả một con cá sấu non! Hãy cùng chúng tôi bật máy quay hồng ngoại và bám sát đối tượng trong hai mươi tư giờ nghẹt thở ngay sau đây! Chẳng một chuyển động thừa, chẳng một cái chớp mí mắt, con quái vật này đã biến sự nhẫn nại thành một thứ nghệ thuật rình mồi tối thượng chưa từng có trong lịch sử tự nhiên.
```

### scene02 — GIẢI MÃ CHIẾC GUỐC TỬ THẦN
*Thẻ chương:* LƯỠI DAO PHAY CHÉM ĐÔI CON MỒI

*Badge:* `VŨ KHÍ MỎ GUỐC GỖ` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene02_p0.wav` (779 ký tự) · mood `hao_hung`

```text
Bây giờ ống kính siêu cận cảnh của chúng tôi đã bắt trọn cấu trúc kinh dị nhất trên cơ thể Tượng Đá Tiền Sử: Chiếc mỏ khổng lồ độc nhất vô nhị trong thế giới loài chim! Dài tới hai mươi tư xăng-ti-mét, chu vi đo được hơn năm mươi xăng-ti-mét, chiếc mỏ này phình to tròn trịa trông giống hệt như một chiếc guốc gỗ của những người thợ Hà Lan cổ đại. Tên khoa học của nó là Ba-la-ê-ni-xép rếch, dịch nôm na là Vua Đầu Cá Voi. Nhưng khác xa với vẻ ngoài cục mịch hài hước, chiếc mỏ này thực chất là một cỗ máy chém sinh học được tôi luyện qua suốt bao kỷ nguyên tiến hóa! Khối sừng khổng lồ này có thể tích buồng chứa lớn thứ ba trong toàn bộ các loài chim biết bay trên thế giới, tạo ra một trọng tâm lệch hẳn về phía trước nhưng lại được cân bằng tuyệt đối bởi chiếc đuôi xòe rộng.
```
**Part 1** → `audio/vs/scene02_p1.wav` (617 ký tự) · mood `don_dap`

```text
Hãy quan sát thật kỹ hai mép mỏ! Chúng sắc lẹm không khác gì một cặp lưỡi dao phay công nghiệp, có khả năng cắt đứt các sợi gân dai nhất chỉ bằng một lực khép nhẹ. Và ở ngay đầu mỏ trên, một chiếc móc sừng nhọn hoắt quặp ngược xuống dưới như một chiếc mỏ neo sắt. Khi chiếc mỏ này đập sập lại, chiếc móc sừng sẽ cắm phập vào hộp sọ con mồi, khóa chặt mục tiêu không cho bất kỳ giọt chất lỏng hay sinh lực nào có cơ hội thoát ra ngoài. Lực bấm của bộ hàm này khi khép chặt có thể nghiền nát cả những lớp mai rùa nước ngọt dày cộp hay những bộ vảy cứng như giáp sắt của các loài cá cổ đại bơi lội dưới tầng đáy bùn lầy.
```
**Part 2** → `audio/vs/scene02_p2.wav` (719 ký tự) · mood `hao_hung`

```text
Với một khối lượng mỏ nặng trịch như thế, chiếc cổ của hươu hay cò bình thường sẽ bị gãy gập vì mất cân bằng trọng tâm. Nhưng thiên nhiên đã đúc cho Tượng Đá Tiền Sử một hệ thống đốt sống cổ cứng như thép nguội, kết hợp với các bó cơ gáy cuồn cuộn có khả năng giật ngược chiếc mỏ nặng cả ki-lô-gam với gia tốc cực lớn. Chiếc guốc gỗ này không chỉ dùng để mổ, nó là một chiếc xẻng xúc bùn, một chiếc kẹp tạ nặng tấn và là một vũ khí hủy diệt chuyên biệt để nuốt trọn những con quái vật trơn trượt dưới đáy đầm lầy tăm tối! Cấu trúc xương sọ của nó có mật độ canxi dày đặc gấp ba lần các loài cò bình thường, hấp thụ hoàn toàn xung chấn khi va đập mạnh xuống đáy đầm nước mà không làm tổn thương các mô mềm bên trong não.
```

### scene03 — TIẾNG NỔ XÉ TOẠC MÀN ĐÊM
*Thẻ chương:* TIẾNG KHẨU SÚNG TIỂU LIÊN AK

*Badge:* `TIẾNG NỔ SÚNG MÁY` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene03_p0.wav` (668 ký tự) · mood `don_dap`

```text
Trời đã về chiều, màn đêm đen đặc đang bao trùm lấy đầm lầy châu Phi. Đột nhiên, một tràng âm thanh chát chúa vang dội xé toạc không gian yên tĩnh! Bằng! Bằng! Tạch tạch tạch tạch! Cả đoàn phóng viên chúng tôi hoảng hốt nằm rạp xuống bùn lầy vì tưởng chừng như đang có một cuộc đấu súng ác liệt giữa các tay súng phiến quân trang bị súng trường tự động AK! Nhưng khi ngẩng đầu lên qua ống nhòm nhìn đêm, nguồn gốc của âm thanh kinh hoàng ấy lại phát ra từ chính chiếc mỏ của Tượng Đá Tiền Sử! Từng tràng tiếng nổ đanh gọn, dứt khoát và khô khốc vang dội từ bờ sậy bên này sang đảo lau bên kia, khiến cả bầy chim nước hoảng hốt vỗ cánh bay tán loạn lên bầu trời mờ mịt.
```
**Part 1** → `audio/vs/scene03_p1.wav` (111 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Trời ơi tiếng gì đanh thép như súng máy liên thanh nổ giòn giã thế, có nguy hiểm tính mạng không phóng viên ơi?
```
**Part 2** → `audio/vs/scene03_p2.wav` (738 ký tự) · mood `hao_hung`

```text
[laughter] Bình tĩnh nào người anh em ngơ ngác, đó là tiếng gõ mỏ chào sân của chú chim đấy! [surprise-oh] Hiện tượng này trong giới điểu học được gọi là Bill-clattering. Khi muốn khẳng định chủ quyền lãnh thổ hoặc giao tiếp với bạn tình, Tượng Đá Tiền Sử sẽ ngửa cổ ra sau rồi dập hai hàm mỏ vào nhau với tốc độ siêu thanh. Do bên trong mỏ có cấu trúc khoang rỗng hoạt động như một buồng cộng hưởng âm thanh, mỗi cú đập tạo ra tiếng nổ vang dội lên tới hơn một trăm đề-xi-ben, tương đương với tiếng súng máy quân dụng nhả đạn cự ly gần! Tần số rung động của tiếng gõ mỏ này mạnh đến mức làm rung chuyển cả những mặt lá súng nổi trên mặt nước xung quanh, tạo nên một hiệu ứng áp chế tâm lý nghẹt thở giữa không gian tĩnh mịch của màn đêm.
```
**Part 3** → `audio/vs/scene03_p3.wav` (583 ký tự) · mood `don_dap`

```text
Âm thanh chát chúa này có thể truyền xa tới cả cây số qua làn sương mù đầm lầy, làm cho lũ cá sấu, linh cẩu và cả những đàn báo đốm đi săn đêm cũng phải giật mình kinh sợ mà dạt ra xa. Đó là lời tuyên ngôn đanh thép khẳng định rằng: Vùng đầm lầy tăm tối này đã có chủ nhân, và bất kỳ kẻ nào dám xâm phạm vùng nước phục kích của nó sẽ phải đối diện với chiếc kẹp tử thần! Đối với những con chim trưởng thành khác cùng loài, tiếng gõ mỏ này mang thông điệp cấm xâm phạm bất khả xâm phạm, giúp chúng phân chia lãnh thổ rộng lớn hàng chục cây số vuông mà không cần phải đổ máu trực diện.
```

### scene04 — CÚ BỔ NHÀO NUỐT TRỌN CÁ PHỔI
*Thẻ chương:* ĐÒN SỤP ĐỔ TÀN KHỐC 7KG

*Badge:* `CÚ LAO SẬP COLLAPSE` · *mood mặc định:* `nghiem_trang_gia`

**Part 0** → `audio/vs/scene04_p0.wav` (651 ký tự) · mood `nghiem_trang_gia`

```text
Bây giờ là khoảnh khắc săn mồi đắt giá nhất mà đoàn làm phim chúng tôi đã phải phục kích ròng rã suốt mười tiếng đồng hồ dưới đầm nước hôi thối để ghi lại. Dưới lớp bèo hoa dâu đục ngầu, một con cá phổi châu Phi khổng lồ dài gần một mét đang từ từ trồi lên mặt nước để đớp không khí. Nó hoàn toàn không hề hay biết rằng, cách đó chỉ hai bước chân, Tượng Đá Tiền Sử đã khóa mục tiêu bằng đôi mắt vàng rực có thị giác lập thể ba chiều hoàn hảo. Đôi mắt to tròn màu vàng rơm của nó không nằm lệch sang hai bên như chim bồ câu hay gà vịt, mà hướng thẳng về phía trước giống hệt mắt cú vẹo hay mắt người, cho phép đo đạc cự ly chính xác đến từng mi-li-mét.
```
**Part 1** → `audio/vs/scene04_p1.wav` (679 ký tự) · mood `hao_hung`

```text
Và rồi, bùm! Không hề có một động tác nhấp nhử hay chuẩn bị, toàn bộ cơ thể nặng bảy ki-lô-gam của Tượng Đá Tiền Sử đổ ụp thẳng xuống mặt nước như một tòa nhà bê tông sụp đổ! Tuyệt kỹ săn mồi này được các nhà khoa học gọi là Collapse strike, tức là đòn bổ nhào sụp đổ. Con chim phóng cả thân hình, sải cánh rộng hai mét rưỡi và chiếc mỏ nặng trịch cắm thẳng xuống bùn lầy với vận tốc ba mươi lăm cây số một giờ. Lực va chạm mạnh đến mức nước bắn tung tóe mù mịt như một quả mìn nổ chậm dưới lòng hồ! Cú rơi tự do này sử dụng chính trọng lượng cơ thể đồ sộ bảy ki-lô-gam làm gia tốc rơi, biến toàn bộ cơ thể thành một khối chùy công phá dội thẳng xuống đầu con mồi trong chớp mắt.
```
**Part 2** → `audio/vs/scene04_p2.wav` (554 ký tự) · mood `hao_hung`

```text
Khi con chim ngẩng đầu lên khỏi làn nước đục ngầu, con cá phổi giãy giụa tuyệt vọng đã nằm gọn trong chiếc mỏ khổng lồ. Con chim dùng cạnh mỏ sắc như dao phay nghiền nát hộp sọ con mồi, giũ sạch bùn đất và bèo rác rồi nuốt trọn cả con cá dài cả mét vào dạ dày chỉ sau ba cú ực. Một màn trình diễn săn mồi bạo lực, chính xác và tàn khốc đến nghẹt thở! Con chim dùng đầu lưỡi hình ngọn giáo đẩy con mồi vào họng, rồi hớp một ngụm nước trong để súc sạch cặn bùn, thể hiện một sự điềm tĩnh lạnh lùng đến rợn gáy sau khi vừa thực hiện một pha sát hại đẫm máu.
```

### scene05 — GÓC KHUẤT ĐEN TỐI TRONG TỔ CHIM
*Thẻ chương:* BI KỊCH SÁT HẠI CON THỨ CAINISM

*Badge:* `NGHỊCH LÝ TỔNG HỢP` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene05_p0.wav` (752 ký tự) · mood `hao_hung`

```text
Đến đây, quý vị khán giả sẽ thấy một nghịch lý tâm lý cực kỳ kỳ quặc ở loài chim này. Khi tiếp xúc với con người, đặc biệt là trong các trung tâm bảo tồn hay vườn thú, Tượng Đá Tiền Sử lại cư xử như một quý ông người Anh cực kỳ lịch lãm. Nếu một người chăm sóc cúi gập người chào nó một cách cung kính, chú chim sẽ lập tức cúi thấp đầu xuống đáp lễ, lắc lư chiếc mỏ nhẹ nhàng và phát ra những tiếng rù rù êm ái như một lời chào mừng nồng nhiệt. Nhiều du khách đã phải thốt lên rằng đây là loài chim lễ phép và đáng yêu nhất hành tinh! Sự tương phản giữa ngoại hình hung dữ như khủng long tiền sử và phong thái cúi đầu chào lịch thiệp này đã tạo nên một cơn sốt kỳ thú trên toàn mạng xã hội, biến nó thành biểu tượng văn hóa độc đáo ở đất nước Nhật Bản.
```
**Part 1** → `audio/vs/scene05_p1.wav` (101 ký tự) · 🎭 cameo `phat_thanh_vien`

```text
Alo phóng viên, sổ tay thực địa có ghi chương đen tối rùng rợn về chúng trong tổ hoang dã đúng không?
```
**Part 2** → `audio/vs/scene05_p2.wav` (737 ký tự) · mood `don_dap`

```text
[laughter] Đáng tiếc là đúng như vậy thưa trường quay! [surprise-oh] Ẩn sau vẻ ngoài lịch thiệp ấy là một sự thật tàn khốc đến lạnh người trong tổ đẻ, mang tên hiện tượng Cainism, tức là sát hại anh em ruột. Chim mẹ luôn đẻ hai quả trứng để dự phòng rủi ro. Khi quả trứng đầu tiên nở ra một con non khỏe mạnh, và vài ngày sau quả trứng thứ hai nở ra đứa em bé nhỏ, một cuộc chiến sinh tồn đẫm máu bắt đầu. Con chim anh to lớn hơn sẽ liên tục dùng mỏ mổ vào đầu em mình, cắn xé lông tơ và đẩy đứa em ra mép tổ dưới nắng thiêu đốt. Tiếng kêu chít chít cầu cứu yếu ớt của đứa em nhỏ bé lọt thỏm giữa tiếng gió rít qua đầm lầy, trong khi người anh lớn liên tục giáng những cú mổ sắc nhọn để xua đuổi kẻ cạnh tranh sinh tồn duy nhất của mình.
```
**Part 3** → `audio/vs/scene05_p3.wav` (647 ký tự) · mood `tram_bi_an`

```text
Đau lòng hơn cả, chim mẹ đứng ngay bên cạnh chứng kiến toàn bộ sự việc nhưng tuyệt đối không can thiệp. Toàn bộ thức ăn và nước uống đều được dồn hết cho đứa con lớn, trong khi đứa em yếu ớt dần kiệt sức và chết đói trong sự cô độc tàn nhẫn. Đó là quy luật chọn lọc tự nhiên khắc nghiệt của đầm lầy: Nguồn thức ăn quá khan hiếm, và chim bố mẹ chỉ đủ sức nuôi duy nhất một cỗ máy chiến tranh hoàn hảo để duy trì nòi giống! Sự chọn lọc tự nhiên không có chỗ cho lòng thương hại hay những giọt nước mắt ủy mị. Chỉ những cá thể mạnh nhất, tàn nhẫn nhất và có sức đề kháng cao nhất mới xứng đáng đại diện cho giống loài tiếp tục thống trị vùng đầm lầy.
```

### scene06 — BÀI HỌC TỪ TƯỢNG ĐÁ BẤT TỬ
*Thẻ chương:* BẢN LĨNH KIÊN ĐỊNH CHỜ THỜI

*Badge:* `KẾT LUẬN` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene06_p0.wav` (698 ký tự) · mood `am_ap`

```text
Sau hai mươi tư giờ theo chân Tượng Đá Tiền Sử giữa đầm lầy châu Phi hoang dã, chúng tôi nhận ra rằng đây không đơn thuần là một loài chim, mà là một hóa thạch sống kiên cường mang linh hồn của những loài khủng long ăn thịt từ kỷ Jura còn sót lại giữa thời hiện đại. Từ sự nhẫn nại đứng im hàng giờ không chớp mắt, chiếc mỏ guốc gỗ sắc lẹm chém đôi con mồi, tiếng gõ mỏ vang dội như súng máy quân dụng, cho đến sự lạnh lùng tàn nhẫn để sinh tồn, tất cả đã tạo nên một kiệt tác thích nghi đỉnh cao của tạo hóa. Nó đứng đó như một tượng đài bất hoại chứng kiến sự thăng trầm của lịch sử tự nhiên, nhắc nhở chúng ta về sức mạnh kỳ diệu của sự kiên định trước những biến đổi khắc nghiệt của môi trường.
```
**Part 1** → `audio/vs/scene06_p1.wav` (870 ký tự) · mood `am_ap`

```text
Cuộc đời của chú chim Mỏ Giày mang lại cho chúng ta một bài học sâu sắc về sự kiên nhẫn và thời cơ trong cuộc sống: Đôi khi, điều làm nên sự vĩ đại không phải là việc bạn chạy nhảy lăng xăng khắp nơi, mà là khả năng giữ vững sự tĩnh lặng tuyệt đối, kiên định chờ đợi thời điểm chín muồi để tung ra một đòn quyết định thay đổi toàn bộ cục diện! Bạn ấn tượng nhất với đặc điểm nào của Tượng Đá Tiền Sử: Tiếng gõ mỏ nổ giòn như súng máy AK hay sự kiên nhẫn đứng bất động năm tiếng đồng hồ? Hãy để lại bình luận chia sẻ cảm nghĩ nhé! Còn ở tập tiếp theo, xưởng vũ khí tự nhiên sẽ đưa các bạn diện kiến một pháo đài di động với ba mươi ngàn mũi tên ngạnh ngược có khả năng tự găm sâu vào thịt mãnh thú! Hãy học cách đứng vững trước sóng gió cuộc đời như chú chim mỏ giày giữa đầm lầy hoang dã, để khi thời cơ đến, bạn sẽ bứt phá mạnh mẽ và làm nên những điều phi thường nhất!
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Gặp người thì cúi đầu chào lịch sự như một quý ông, nhưng với em ruột trong tổ thì ra tay tàn nhẫn đến lạnh người?! Hãy nhìn chú Cò Mỏ Giày kỳ dị giữa đầm lầy châu Phi này xem! Mang mật danh Tượng Đá Tiền Sử, nó có thể đứng bất động giữa bãi lau sậy suốt năm tiếng liên tục mà không thèm chớp mắt lấy một lần! Chiếc mỏ dài hai mươi tư xăng-ti-mét của nó trông như chiếc guốc gỗ nhưng mép sắc lẹm như dao phay, sẵn sàng tung cú bổ nhào ba mươi lăm cây số một giờ chém đôi cá phổi và cá sấu non! Mỗi khi đêm xuống, nó dập mỏ tạo ra tiếng nổ đanh thép như súng máy liên thanh nổ giòn vang xa hàng cây số! Ở vườn thú, nếu bạn cúi chào, nó sẽ lập tức cúi gập đầu đáp lễ cực kỳ đáng yêu. Thế nhưng trong tự nhiên hoang dã, chim non mới nở sẽ liên tục mổ, cắn xé và bỏ đói đứa em ruột của mình đến chết để độc chiếm nguồn thức ăn, dưới sự làm ngơ tuyệt đối của chim mẹ! Một nghịch lý sinh tồn rùng mình đến nghẹt thở của tự nhiên!
```

**Whisper prompt:** `Cò Mỏ Giày, Balaeniceps rex`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| hai mươi tư giờ | 24h |
| hai mươi tư xăng-ti-mét | 24cm |
| năm mươi xăng-ti-mét | 50cm |
| ba mươi lăm cây số | 35km/h |
| bảy ki-lô-gam | 7kg |
| ba tiếng | 3 tiếng |
| năm tiếng | 5 tiếng |
| một trăm đề-xi-ben | 100 dB |
| ba mươi ngàn | 30.000 |
| Ba-la-ê-ni-xép rếch | Balaeniceps rex |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · 24 GIỜ THÂM NHẬP VÙNG ĐẤT CHẾT · 96.1s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:06.6 (6.6s) | L01 | Chào mừng quý vị khán giả đang theo dõi bản tin hiện trường trực tiếp của kênh Truyền hình Sinh tồn Hoang dã! Tôi là phóng viên chiến trường |  | phóng viên chiến trường mặc áo gile chống đạn cầm sổ tay và micro: phóng viên đang lội bùn giữa đầm lầy Bangweulu mịt mù sương trắng chĩa micro tường thuật |
| b02 | 00:06.6–00:17.0 (10.4s) | L02 | đang có mặt tại đầm lầy Bangweulu heo hút giữa lục địa châu Phi, nơi màn sương mù dày đặc che phủ những vũng nước đen ngòm từ thời tiền sử. Hãy hạ thấp ống kính máy quay xuống mép lau sậy đằng kia xem! Trong làn |  | chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): cò mỏ giày đứng bất động như tảng đá cẩm thạch giữa làn sương khói đầm lầy tiền sử |
| b03 | 00:17.0–00:26.6 (9.6s) | L03 | sương mờ ảo, một bóng đen sừng sững cao gần một mét rưỡi đang đứng sừng sững như một tảng đá cẩm thạch xám xịt. Đôi mắt vàng đục vô cảm, bất động tuyệt đối, chẳng một sợi lông tơ lay động dù gió lốc đang |  | chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): cận cảnh đôi mắt vàng đục bất động không một cái chớp mí mắt của cò mỏ giày |
| b04 | 00:26.6–00:36.3 (9.7s) | L04 | thổi qua. Dân địa phương gọi nó là Cò Mỏ Giày, nhưng trong sổ tay tác nghiệp của tôi, sinh vật này mang mật danh rùng rợn: Tượng Đá Tiền Sử. Nó đang làm gì thế kia? Liệu nó còn sống hay đã hóa thạch |  | phát thanh viên tin tức trường quay đeo tai nghe chuyên nghiệp: phát thanh viên trường quay khẩn thiết nhắc nhở giữ an toàn trước sát thủ tiền sử |
| b05 | 00:36.3–00:47.1 (10.8s) | L05 | từ kỷ Phấn Trắng? Mỗi hơi thở của nó chậm rãi đến mức mặt nước xung quanh phẳng lặng như tờ gương chẳng một gợn sóng lăn tăn, khiến mọi sinh vật bơi lội dưới chân đều hoàn toàn mất đi cảnh giác phòng thủ. Alo trường |  | chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): chú chim sẻ thơ ngây bay tới thản nhiên đậu lên đỉnh đầu cò mỏ giày để rỉa lông |
| b06 | 00:47.1–00:58.9 (11.8s) | L06 | quay nhắc phóng viên giữ an toàn, cảm biến báo nó vẫn thở nhưng nhịp tim cực thấp! Cảm ơn trường quay đã cảnh báo! Quý vị không nghe nhầm đâu, cỗ máy săn mồi này có thể đứng im như một khúc gỗ chết suốt |  | chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): mặt nước xung quanh phẳng lặng như tờ gương không một gợn sóng lăn tăn |
| b07 | 00:58.9–01:08.7 (9.9s) | L07 | 3 tiếng, thậm chí 5 tiếng đồng hồ liên tục mà không hề chớp mắt lấy một lần! Thậm chí những chú chim sẻ ngây thơ còn tưởng đây là cọc gỗ mục nên đã thản nhiên bay tới đậu lên đỉnh đầu của nó để |  | chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động) cá sấu con hoảng sợ rụt đầu xuống bùn lầy: cá sấu non sợ hãi nép mình dưới rễ cây đước nhìn lên bóng đen khổng lồ |
| b08 | 01:08.7–01:22.2 (13.5s) | L08 | rỉa lông. Nhưng đừng để sự tĩnh lặng ma mị này đánh lừa các giác quan của bạn! Dưới lớp vỏ bọc bằng đá ấy là một sát thủ phục kích tàn độc nhất thế giới đầm lầy, sẵn sàng kích hoạt một đòn tấn công sấm sét có thể chẻ đôi cả một con cá sấu non! Hãy cùng chúng |  | phóng viên chiến trường mặc áo gile chống đạn cầm sổ tay và micro chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): phóng viên giơ ống nhòm hồng ngoại quan sát cò mỏ giày đứng im như khúc gỗ chết |
| b09 | 01:22.2–01:36.1 (13.9s) | L09 | tôi bật máy quay hồng ngoại và bám sát đối tượng trong 24h nghẹt thở ngay sau đây! Chẳng một chuyển động thừa, chẳng một cái chớp mí mắt, con quái vật này đã biến sự nhẫn nại thành một thứ nghệ thuật rình mồi tối thượng chưa từng có trong lịch sử tự nhiên. |  | chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): bóng đen cò mỏ giày cao 1.5m in hằn trên nền trời xám tro đầy vẻ ma mị |

### scene02 · GIẢI MÃ CHIẾC GUỐC TỬ THẦN · 106.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.6 (7.6s) | L10 | Bây giờ ống kính siêu cận cảnh của chúng tôi đã bắt trọn cấu trúc kinh dị nhất trên cơ thể Tượng Đá Tiền Sử: Chiếc mỏ khổng lồ độc nhất vô nhị trong |  | chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): chiếc mỏ khổng lồ hình guốc gỗ Hà Lan choán hết nửa khung hình với các đường vân đá |
| b02 | 00:07.6–00:22.2 (14.6s) | L11 | thế giới loài chim! Dài tới 24cm, chu vi đo được hơn 50cm, chiếc mỏ này phình to tròn trịa trông giống hệt như một chiếc guốc gỗ của những người thợ Hà Lan cổ đại. Tên khoa học của nó là Balaeniceps rex, dịch nôm na là Vua Đầu Cá Voi. | **24cm** · Chiều dài mỏ guốc · R/320 · [0.8, 0.4]<br>**50cm** · Chu vi mỏ khổng lồ · L/360 · [0.35, 0.5] | chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): thước đo kỹ thuật đo chiều dài mỏ 24cm và chu vi hơn 50cm |
| b03 | 00:22.2–00:33.9 (11.7s) | L12 | Nhưng khác xa với vẻ ngoài cục mịch hài hước, chiếc mỏ này thực chất là một cỗ máy chém sinh học được tôi luyện qua suốt bao kỷ nguyên tiến hóa! Khối sừng khổng lồ này có thể tích buồng chứa lớn thứ ba trong toàn bộ các loài chim |  | chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): mép mỏ sắc lẹm như hai lưỡi dao phay công nghiệp phản chiếu ánh thép lạnh lùng |
| b04 | 00:33.9–00:45.8 (11.9s) | L13 | biết bay trên thế giới, tạo ra một trọng tâm lệch hẳn về phía trước nhưng lại được cân bằng tuyệt đối bởi chiếc đuôi xòe rộng. Hãy quan sát thật kỹ hai mép mỏ! Chúng sắc lẹm không khác gì một cặp lưỡi dao phay công nghiệp, có khả |  | chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): chiếc móc sừng nhọn hoắt quặp ngược xuống ở đầu mỏ như chiếc mỏ neo sắt |
| b05 | 00:45.8–00:55.9 (10.1s) | L14 | năng cắt đứt các sợi gân dai nhất chỉ bằng một lực khép nhẹ. Và ở ngay đầu mỏ trên, một chiếc móc sừng nhọn hoắt quặp ngược xuống dưới như một chiếc mỏ neo sắt. Khi chiếc mỏ này đập sập lại, chiếc móc sừng sẽ cắm phập vào hộp |  | chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): sơ đồ cơ bắp cuồn cuộn ở gáy và đốt sống cổ cứng như thép chịu lực |
| b06 | 00:55.9–01:06.2 (10.2s) | L15 | sọ con mồi, khóa chặt mục tiêu không cho bất kỳ giọt chất lỏng hay sinh lực nào có cơ hội thoát ra ngoài. Lực bấm của bộ hàm này khi khép chặt có thể nghiền nát cả những lớp mai rùa nước ngọt dày cộp hay những bộ vảy cứng như |  | chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): bộ hàm khép chặt nghiền nát mai rùa nước ngọt và giáp sắt của cá cổ đại |
| b07 | 01:06.2–01:17.9 (11.7s) | L16 | giáp sắt của các loài cá cổ đại bơi lội dưới tầng đáy bùn lầy. Với một khối lượng mỏ nặng trịch như thế, chiếc cổ của hươu hay cò bình thường sẽ bị gãy gập vì mất cân bằng trọng tâm. Nhưng thiên nhiên đã đúc cho Tượng Đá Tiền Sử |  | chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): xương sọ dày đặc canxi gấp 3 lần hấp thụ xung chấn va đập cực mạnh |
| b08 | 01:17.9–01:32.0 (14.1s) | L17 | một hệ thống đốt sống cổ cứng như thép nguội, kết hợp với các bó cơ gáy cuồn cuộn có khả năng giật ngược chiếc mỏ nặng cả ki-lô-gam với gia tốc cực lớn. Chiếc guốc gỗ này không chỉ dùng để mổ, nó là một chiếc xẻng xúc bùn, một chiếc kẹp tạ nặng tấn và là một vũ khí hủy |  | chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động) chú cá phổi châu phi trơn trượt vây như mái chèo đang ngoi lên thở: cò mỏ giày giơ cao chiếc mỏ xúc bùn đe dọa lũ quái vật trơn trượt |
| b09 | 01:32.0–01:46.7 (14.7s) | L18 | diệt chuyên biệt để nuốt trọn những con quái vật trơn trượt dưới đáy đầm lầy tăm tối! Cấu trúc xương sọ của nó có mật độ canxi dày đặc gấp ba lần các loài cò bình thường, hấp thụ hoàn toàn xung chấn khi va đập mạnh xuống đáy đầm nước mà không làm tổn thương các mô mềm bên trong não. |  | phóng viên chiến trường mặc áo gile chống đạn cầm sổ tay và micro: phóng viên kinh ngạc ghi chép vào sổ tay về cỗ máy chém sinh học hoàn hảo |

### scene03 · TIẾNG NỔ XÉ TOẠC MÀN ĐÊM · 102.8s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.9 (7.9s) | L19 | Trời đã về chiều, màn đêm đen đặc đang bao trùm lấy đầm lầy châu Phi. Đột nhiên, một tràng âm thanh chát chúa vang dội xé toạc không gian yên tĩnh! Bằng! Bằng! |  | phóng viên chiến trường mặc áo gile chống đạn cầm sổ tay và micro: màn đêm buông xuống đầm lầy, cả đoàn phóng viên hoảng hốt nằm rạp xuống bùn |
| b02 | 00:07.9–00:18.4 (10.5s) | L20 | Tạch tạch tạch tạch! Cả đoàn phóng viên chúng tôi hoảng hốt nằm rạp xuống bùn lầy vì tưởng chừng như đang có một cuộc đấu súng ác liệt giữa các tay súng phiến quân trang bị súng trường tự động AK! Nhưng khi ngẩng đầu lên qua ống |  | chú ngơ ngác giật mình hoảng hốt bịt tai trước tiếng súng máy: chú ngơ ngác giật mình hoảng hốt bịt tai tưởng đấu súng trường tự động AK |
| b03 | 00:18.4–00:28.7 (10.3s) | L21 | nhòm nhìn đêm, nguồn gốc của âm thanh kinh hoàng ấy lại phát ra từ chính chiếc mỏ của Tượng Đá Tiền Sử! Từng tràng tiếng nổ đanh gọn, dứt khoát và khô khốc vang dội từ bờ sậy bên này sang đảo lau bên kia, khiến cả bầy chim nước |  | chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): cò mỏ giày ngửa cổ ra sau dập hai hàm mỏ vào nhau với tốc độ siêu thanh |
| b04 | 00:28.7–00:41.5 (12.9s) | L22 | hoảng hốt vỗ cánh bay tán loạn lên bầu trời mờ mịt. Trời ơi tiếng gì đanh thép như súng máy liên thanh nổ giòn giã thế, có nguy hiểm tính mạng không phóng viên ơi? Bình tĩnh nào người anh em ngơ ngác, đó là tiếng gõ mỏ chào |  | chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): sơ đồ khoang rỗng buồng cộng hưởng âm thanh bên trong mỏ phát ra tiếng nổ 100 dB |
| b05 | 00:41.5–00:54.7 (13.1s) | L23 | sân của chú chim đấy! Hiện tượng này trong giới điểu học được gọi là Bill-clattering. Khi muốn khẳng định chủ quyền lãnh thổ hoặc giao tiếp với bạn tình, Tượng Đá Tiền Sử sẽ ngửa cổ ra sau rồi dập hai hàm mỏ vào nhau với tốc độ siêu thanh. |  | chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): tần số rung động của tiếng gõ mỏ làm rung chuyển mặt lá súng trên đầm nước |
| b06 | 00:54.7–01:06.3 (11.6s) | L24 | Do bên trong mỏ có cấu trúc khoang rỗng hoạt động như một buồng cộng hưởng âm thanh, mỗi cú đập tạo ra tiếng nổ vang dội lên tới hơn 100 dB, tương đương với tiếng súng máy quân dụng nhả đạn cự ly gần! Tần số rung | **100 dB** · Tiếng gõ mỏ súng máy · R/320 · [0.8, 0.4] | chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): lũ linh cẩu và báo đốm giật mình kinh hãi tháo chạy khỏi tiếng gõ mỏ đanh thép |
| b07 | 01:06.3–01:17.6 (11.3s) | L25 | động của tiếng gõ mỏ này mạnh đến mức làm rung chuyển cả những mặt lá súng nổi trên mặt nước xung quanh, tạo nên một hiệu ứng áp chế tâm lý nghẹt thở giữa không gian tĩnh mịch của màn đêm. Âm thanh chát chúa này có thể truyền xa |  | chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): cò mỏ giày sừng sững tuyên bố chủ quyền lãnh thổ giữa làn sương mù đêm |
| b08 | 01:17.6–01:29.2 (11.6s) | L26 | tới cả cây số qua làn sương mù đầm lầy, làm cho lũ cá sấu, linh cẩu và cả những đàn báo đốm đi săn đêm cũng phải giật mình kinh sợ mà dạt ra xa. Đó là lời tuyên ngôn đanh thép khẳng định rằng: Vùng đầm lầy tăm tối này đã có chủ nhân, và bất kỳ kẻ |  | phóng viên chiến trường mặc áo gile chống đạn cầm sổ tay và micro: phóng viên thở phào nhẹ nhõm khi nhận ra vũ khí chỉ là chiếc mỏ gõ liên thanh |
| b09 | 01:29.2–01:42.8 (13.6s) | L27 | nào dám xâm phạm vùng nước phục kích của nó sẽ phải đối diện với chiếc kẹp tử thần! Đối với những con chim trưởng thành khác cùng loài, tiếng gõ mỏ này mang thông điệp cấm xâm phạm bất khả xâm phạm, giúp chúng phân chia lãnh thổ rộng lớn hàng chục cây số vuông mà không cần phải đổ máu trực diện. |  | chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): cò mỏ giày thu cổ lại trở về trạng thái tượng đá im lìm trong bóng tối |

### scene04 · CÚ BỔ NHÀO NUỐT TRỌN CÁ PHỔI · 94.0s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:06.1 (6.1s) | L28 | Bây giờ là khoảnh khắc săn mồi đắt giá nhất mà đoàn làm phim chúng tôi đã phải phục kích ròng rã suốt mười tiếng đồng hồ dưới đầm nước hôi |  | chú cá phổi châu phi trơn trượt vây như mái chèo đang ngoi lên thở: chú cá phổi châu phi khổng lồ dài cả mét ngoi lên mặt nước đớp không khí |
| b02 | 00:06.1–00:16.1 (10.0s) | L29 | thối để ghi lại. Dưới lớp bèo hoa dâu đục ngầu, một con cá phổi châu Phi khổng lồ dài gần một mét đang từ từ trồi lên mặt nước để đớp không khí. Nó hoàn toàn không hề hay biết rằng, cách đó chỉ hai bước chân, |  | chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): đôi mắt vàng rực của cò mỏ giày khóa chặt mục tiêu với thị giác 3D lập thể |
| b03 | 00:16.1–00:25.1 (9.1s) | L30 | Tượng Đá Tiền Sử đã khóa mục tiêu bằng đôi mắt vàng rực có thị giác lập thể ba chiều hoàn hảo. Đôi mắt to tròn màu vàng rơm của nó không nằm lệch sang hai bên như chim bồ câu hay gà vịt, mà hướng |  | chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): toàn bộ cơ thể 7kg của cò mỏ giày đổ ụp xuống mặt nước như tòa nhà sụp đổ Collapse strike |
| b04 | 00:25.1–00:36.2 (11.0s) | L31 | thẳng về phía trước giống hệt mắt cú vẹo hay mắt người, cho phép đo đạc cự ly chính xác đến từng mi-li-mét. Và rồi, bùm! Không hề có một động tác nhấp nhử hay chuẩn bị, toàn bộ cơ thể nặng 7kg của Tượng Đá Tiền | **7kg** · Khối lượng cơ thể · L/360 · [0.35, 0.5] | chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): nước bắn tung tóe mù mịt như bom mìn phát nổ dưới tốc độ lao mồi 35km/h |
| b05 | 00:36.2–00:47.0 (10.9s) | L32 | Sử đổ ụp thẳng xuống mặt nước như một tòa nhà bê tông sụp đổ! Tuyệt kỹ săn mồi này được các nhà khoa học gọi là Collapse strike, tức là đòn bổ nhào sụp đổ. Con chim phóng cả thân hình, sải cánh rộng hai mét |  | chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động) chú cá phổi châu phi trơn trượt vây như mái chèo đang ngoi lên thở: cá phổi giãy giụa trong chiếc kẹp mỏ khổng lồ bị nghiền nát hộp sọ |
| b06 | 00:47.0–00:57.9 (10.8s) | L33 | rưỡi và chiếc mỏ nặng trịch cắm thẳng xuống bùn lầy với vận tốc 35km/h một giờ. Lực va chạm mạnh đến mức nước bắn tung tóe mù mịt như một quả mìn nổ chậm dưới lòng hồ! Cú rơi tự do này sử dụng chính trọng | **35km/h** · Tốc độ bổ nhào · R/320 · [0.8, 0.4] | chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): cò mỏ giày giũ sạch bùn rác và bèo hoa dâu trên mình con mồi |
| b07 | 00:57.9–01:09.1 (11.3s) | L34 | lượng cơ thể đồ sộ 7kg làm gia tốc rơi, biến toàn bộ cơ thể thành một khối chùy công phá dội thẳng xuống đầu con mồi trong chớp mắt. Khi con chim ngẩng đầu lên khỏi làn nước đục ngầu, con cá phổi giãy giụa tuyệt |  | chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): cò mỏ giày nuốt trọn cả con cá dài cả mét vào dạ dày chỉ sau 3 cú ực |
| b08 | 01:09.1–01:20.2 (11.1s) | L35 | vọng đã nằm gọn trong chiếc mỏ khổng lồ. Con chim dùng cạnh mỏ sắc như dao phay nghiền nát hộp sọ con mồi, giũ sạch bùn đất và bèo rác rồi nuốt trọn cả con cá dài cả mét vào dạ dày chỉ sau ba cú ực. |  | chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): con chim hớp một ngụm nước trong súc sạch mỏ với vẻ điềm tĩnh rợn người |
| b09 | 01:20.2–01:34.0 (13.8s) | L36 | Một màn trình diễn săn mồi bạo lực, chính xác và tàn khốc đến nghẹt thở! Con chim dùng đầu lưỡi hình ngọn giáo đẩy con mồi vào họng, rồi hớp một ngụm nước trong để súc sạch cặn bùn, thể hiện một sự điềm tĩnh lạnh lùng đến rợn gáy sau khi vừa thực hiện một pha sát hại đẫm máu. |  | phóng viên chiến trường mặc áo gile chống đạn cầm sổ tay và micro: phóng viên nín thở kinh hoàng trước màn săn mồi tàn khốc vừa ghi hình được |

### scene05 · GÓC KHUẤT ĐEN TỐI TRONG TỔ CHIM · 109.5s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.8 (8.8s) | L37 | Đến đây, quý vị khán giả sẽ thấy một nghịch lý tâm lý cực kỳ kỳ quặc ở loài chim này. Khi tiếp xúc với con người, đặc biệt là trong các trung tâm bảo tồn hay vườn thú, |  | chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): cò mỏ giày ở vườn thú cúi gập đầu đáp lễ chào người chăm sóc như một quý ông Anh quốc |
| b02 | 00:08.8–00:21.5 (12.7s) | L38 | Tượng Đá Tiền Sử lại cư xử như một quý ông người Anh cực kỳ lịch lãm. Nếu một người chăm sóc cúi gập người chào nó một cách cung kính, chú chim sẽ lập tức cúi thấp đầu xuống đáp lễ, lắc lư chiếc mỏ nhẹ nhàng và phát ra những tiếng rù rù êm ái |  | chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): khách tham quan thích thú chụp ảnh cùng chú chim lễ phép đáng yêu nhất thế giới |
| b03 | 00:21.5–00:34.4 (12.8s) | L39 | như một lời chào mừng nồng nhiệt. Nhiều du khách đã phải thốt lên rằng đây là loài chim lễ phép và đáng yêu nhất hành tinh! Sự tương phản giữa ngoại hình hung dữ như khủng long tiền sử và phong thái cúi đầu chào lịch thiệp này đã tạo nên một cơn sốt kỳ |  | phát thanh viên tin tức trường quay đeo tai nghe chuyên nghiệp: phát thanh viên hé lộ bí mật đen tối rùng rợn trong tổ đẻ hoang dã |
| b04 | 00:34.4–00:47.9 (13.5s) | L40 | thú trên toàn mạng xã hội, biến nó thành biểu tượng văn hóa độc đáo ở đất nước Nhật Bản. Alo phóng viên, sổ tay thực địa có ghi chương đen tối rùng rợn về chúng trong tổ hoang dã đúng không? Đáng tiếc là đúng như vậy thưa trường quay! Ẩn sau vẻ ngoài |  | chú cò con anh lông xám hung hăng to lớn trong tổ chú cò con em yếu ớt tội nghiệp kêu chít chít cầu cứu: trong tổ chim hoang dã con chim anh to lớn hung hăng mổ tới tấp vào đầu đứa em nhỏ |
| b05 | 00:47.9–00:59.3 (11.4s) | L41 | lịch thiệp ấy là một sự thật tàn khốc đến lạnh người trong tổ đẻ, mang tên hiện tượng Cainism, tức là sát hại anh em ruột. Chim mẹ luôn đẻ hai quả trứng để dự phòng rủi ro. Khi quả trứng đầu tiên nở ra một con non khỏe mạnh, và vài ngày sau quả | **CAINISM** · Sát hại con thứ · R/340 · [0.8, 0.45] | chú cò con em yếu ớt tội nghiệp kêu chít chít cầu cứu: chim con em yếu ớt rách lông kêu chít chít cầu cứu trong tuyệt vọng |
| b06 | 00:59.3–01:10.2 (11.0s) | L42 | trứng thứ hai nở ra đứa em bé nhỏ, một cuộc chiến sinh tồn đẫm máu bắt đầu. Con chim anh to lớn hơn sẽ liên tục dùng mỏ mổ vào đầu em mình, cắn xé lông tơ và đẩy đứa em ra mép tổ dưới nắng thiêu đốt. Tiếng kêu chít chít cầu cứu yếu |  | chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động) chú cò con anh lông xám hung hăng to lớn trong tổ: chim mẹ đứng nhìn lạnh lùng không hề can thiệp để mặc con lớn bạo hành em |
| b07 | 01:10.2–01:22.1 (11.9s) | L43 | ớt của đứa em nhỏ bé lọt thỏm giữa tiếng gió rít qua đầm lầy, trong khi người anh lớn liên tục giáng những cú mổ sắc nhọn để xua đuổi kẻ cạnh tranh sinh tồn duy nhất của mình. Đau lòng hơn cả, chim mẹ đứng ngay bên cạnh chứng kiến toàn bộ sự việc |  | chú cò con anh lông xám hung hăng to lớn trong tổ: con chim anh nuốt trọn toàn bộ thức ăn và nước uống độc chiếm sự sống |
| b08 | 01:22.1–01:35.7 (13.6s) | L44 | nhưng tuyệt đối không can thiệp. Toàn bộ thức ăn và nước uống đều được dồn hết cho đứa con lớn, trong khi đứa em yếu ớt dần kiệt sức và chết đói trong sự cô độc tàn nhẫn. Đó là quy luật chọn lọc tự nhiên khắc nghiệt của đầm lầy: Nguồn thức ăn quá khan hiếm, và chim bố mẹ chỉ đủ sức nuôi duy nhất |  | chú cò con em yếu ớt tội nghiệp kêu chít chít cầu cứu: đứa em bé bỏng kiệt sức chết đói dưới cái nắng thiêu đốt của đầm lầy |
| b09 | 01:35.7–01:49.5 (13.8s) | L45 | một cỗ máy chiến tranh hoàn hảo để duy trì nòi giống! Sự chọn lọc tự nhiên không có chỗ cho lòng thương hại hay những giọt nước mắt ủy mị. Chỉ những cá thể mạnh nhất, tàn nhẫn nhất và có sức đề kháng cao nhất mới xứng đáng đại diện cho giống loài tiếp tục thống trị vùng đầm lầy. |  | chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): quy luật sinh tồn khắc nghiệt Cainism chỉ giữ lại một chiến binh mạnh nhất |

### scene06 · BÀI HỌC TỪ TƯỢNG ĐÁ BẤT TỬ · 75.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:06.9 (6.9s) | L46 | Sau 24h theo chân Tượng Đá Tiền Sử giữa đầm lầy châu Phi hoang dã, chúng tôi nhận ra rằng đây không đơn thuần là một loài chim, |  | chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): cò mỏ giày sừng sững như hóa thạch sống thời tiền sử giữa đầm lầy bình minh |
| b02 | 00:06.9–00:16.1 (9.2s) | L47 | mà là một hóa thạch sống kiên cường mang linh hồn của những loài khủng long ăn thịt từ kỷ Jura còn sót lại giữa thời hiện đại. Từ sự nhẫn nại đứng im hàng giờ không chớp mắt, chiếc mỏ guốc |  | chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): bức chân dung nghệ thuật tượng đá bất tử kiên định chờ đợi thời cơ |
| b03 | 00:16.1–00:25.2 (9.1s) | L48 | gỗ sắc lẹm chém đôi con mồi, tiếng gõ mỏ vang dội như súng máy quân dụng, cho đến sự lạnh lùng tàn nhẫn để sinh tồn, tất cả đã tạo nên một kiệt tác thích nghi đỉnh cao của tạo hóa. Nó |  | phóng viên chiến trường mặc áo gile chống đạn cầm sổ tay và micro: phóng viên đứng trên mũi thuyền đầm lầy tổng kết bài học về sự nhẫn nại |
| b04 | 00:25.2–00:34.8 (9.6s) | L49 | đứng đó như một tượng đài bất hoại chứng kiến sự thăng trầm của lịch sử tự nhiên, nhắc nhở chúng ta về sức mạnh kỳ diệu của sự kiên định trước những biến đổi khắc nghiệt của môi trường. Cuộc đời |  | phóng viên chiến trường mặc áo gile chống đạn cầm sổ tay và micro: bài học về sự tĩnh lặng kiên định để tung đòn quyết định thay đổi cục diện |
| b05 | 00:34.8–00:43.8 (9.0s) | L50 | của chú chim Mỏ Giày mang lại cho chúng ta một bài học sâu sắc về sự kiên nhẫn và thời cơ trong cuộc sống: Đôi khi, điều làm nên sự vĩ đại không phải là việc bạn chạy nhảy lăng xăng khắp nơi, |  | chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): màn hình bình chọn: Tiếng gõ mỏ súng máy AK đối đầu sự kiên nhẫn đứng im 5 tiếng |
| b06 | 00:43.8–00:52.4 (8.6s) | L51 | mà là khả năng giữ vững sự tĩnh lặng tuyệt đối, kiên định chờ đợi thời điểm chín muồi để tung ra một đòn quyết định thay đổi toàn bộ cục diện! Bạn ấn tượng nhất với đặc điểm nào của Tượng Đá |  | phóng viên chiến trường mặc áo gile chống đạn cầm sổ tay và micro phát thanh viên tin tức trường quay đeo tai nghe chuyên nghiệp chú ngơ ngác giật mình hoảng hốt bịt tai trước tiếng súng máy: dàn nhân vật vẫy tay chào khán giả và kêu gọi để lại bình luận |
| b07 | 00:52.4–01:01.9 (9.5s) | L52 | Tiền Sử: Tiếng gõ mỏ nổ giòn như súng máy AK hay sự kiên nhẫn đứng bất động 5 tiếng đồng hồ? Hãy để lại bình luận chia sẻ cảm nghĩ nhé! Còn ở tập tiếp theo, xưởng vũ khí tự nhiên |  | chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): cò mỏ giày chầm chậm cúi đầu chào tạm biệt khán giả theo nghi thức quý ông |
| b08 | 01:01.9–01:15.9 (14.0s) | L53 | sẽ đưa các bạn diện kiến một pháo đài di động với 30.000 mũi tên ngạnh ngược có khả năng tự găm sâu vào thịt mãnh thú! Hãy học cách đứng vững trước sóng gió cuộc đời như chú chim mỏ giày giữa đầm lầy hoang dã, để khi thời cơ đến, bạn sẽ bứt phá mạnh mẽ và làm nên những điều phi thường nhất! |  | NO_HERO: hình ảnh bí ẩn của Nhím Lông Nhọn với 30.000 mũi tên tự rút sâu nhá hàng tập sau |

## 5. Phân cảnh Shorts — từng beat

Banner: **TƯỢNG ĐÁ ĐẦM LẦY / SÚNG MÁY GÕ MỎ?!** · giọng 48.8s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Gặp người thì cúi đầu chào lịch sự như một quý ông, nhưng với em ruột trong tổ thì ra tay tàn nhẫn đến lạnh người?! |  |
| s02 | 00:06.5 | S02 | Hãy nhìn chú Cò Mỏ Giày kỳ dị giữa đầm lầy châu Phi này xem! Mang mật danh Tượng Đá Tiền Sử, nó |  |
| s03 | 00:12.0 | S02b | có thể đứng bất động giữa bãi lau sậy suốt 5 tiếng liên tục mà không thèm chớp mắt lấy một lần! |  |
| s04 | 00:16.9 | S03 | Chiếc mỏ dài 24cm của nó trông như chiếc guốc gỗ nhưng mép sắc lẹm như dao phay, |  |
| s05 | 00:22.3 | S03b | sẵn sàng tung cú bổ nhào 35km/h một giờ chém đôi cá phổi và cá sấu |  |
| s06 | 00:26.0 | S04 | non! Mỗi khi đêm xuống, nó dập mỏ tạo ra tiếng nổ đanh thép như súng máy liên thanh nổ giòn vang xa hàng cây số! |  |
| s07 | 00:31.8 | S05 | Ở vườn thú, nếu bạn cúi chào, nó sẽ lập tức cúi gập đầu đáp lễ cực kỳ đáng yêu. |  |
| s08 | 00:36.4 | S06 | Thế nhưng trong tự nhiên hoang dã, chim non mới nở sẽ liên tục mổ, cắn xé và bỏ |  |
| s09 | 00:40.8 | S07 | đói đứa em ruột của mình đến chết để độc chiếm nguồn thức ăn, dưới sự làm ngơ tuyệt đối của chim mẹ! |  |
| s10 | 00:45.5 | S08 | Một nghịch lý sinh tồn rùng mình đến nghẹt thở của tự nhiên! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chào mừng quý vị khán giả đang theo dõi bản tin hiện trường trực tiếp của kênh Truyền hình Sinh tồn Hoang dã! Tôi là phóng viên chiến trường đang có". Bố cục: phóng viên chiến trường mặc áo gile chống đạn cầm sổ tay và micro: phóng viên đang lội bùn giữa đầm lầy Bangweulu mịt mù sương trắng chĩa micro tường thuật
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "mặt tại đầm lầy Bangweulu heo hút giữa lục địa châu Phi, nơi màn sương mù dày đặc che phủ những vũng nước đen ngòm từ thời tiền sử. Hãy hạ thấp ống kính máy quay xuống mép lau sậy đằng kia xem! Trong làn sương". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): cò mỏ giày đứng bất động như tảng đá cẩm thạch giữa làn sương khói đầm lầy tiền sử
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "mờ ảo, một bóng đen sừng sững cao gần một mét rưỡi đang đứng sừng sững như một tảng đá cẩm thạch xám xịt. Đôi mắt vàng đục vô cảm, bất động tuyệt đối, chẳng một sợi lông tơ lay động dù gió lốc đang thổi". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): cận cảnh đôi mắt vàng đục bất động không một cái chớp mí mắt của cò mỏ giày
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "qua. Dân địa phương gọi nó là Cò Mỏ Giày, nhưng trong sổ tay tác nghiệp của tôi, sinh vật này mang mật danh rùng rợn: Tượng Đá Tiền Sử. Nó đang làm gì thế kia? Liệu nó còn sống hay đã hóa thạch từ kỷ". Bố cục: phát thanh viên tin tức trường quay đeo tai nghe chuyên nghiệp: phát thanh viên trường quay khẩn thiết nhắc nhở giữ an toàn trước sát thủ tiền sử
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Phấn Trắng? Mỗi hơi thở của nó chậm rãi đến mức mặt nước xung quanh phẳng lặng như tờ gương chẳng một gợn sóng lăn tăn, khiến mọi sinh vật bơi lội dưới chân đều hoàn toàn mất đi cảnh giác phòng thủ. Alo trường quay". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): chú chim sẻ thơ ngây bay tới thản nhiên đậu lên đỉnh đầu cò mỏ giày để rỉa lông
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nhắc phóng viên giữ an toàn, cảm biến báo nó vẫn thở nhưng nhịp tim cực thấp! Cảm ơn trường quay đã cảnh báo! Quý vị không nghe nhầm đâu, cỗ máy săn mồi này có thể đứng im như một khúc gỗ chết suốt 3". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): mặt nước xung quanh phẳng lặng như tờ gương không một gợn sóng lăn tăn
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tiếng, thậm chí 5 tiếng đồng hồ liên tục mà không hề chớp mắt lấy một lần! Thậm chí những chú chim sẻ ngây thơ còn tưởng đây là cọc gỗ mục nên đã thản nhiên bay tới đậu lên đỉnh đầu của nó để rỉa". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động) cá sấu con hoảng sợ rụt đầu xuống bùn lầy: cá sấu non sợ hãi nép mình dưới rễ cây đước nhìn lên bóng đen khổng lồ
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "lông. Nhưng đừng để sự tĩnh lặng ma mị này đánh lừa các giác quan của bạn! Dưới lớp vỏ bọc bằng đá ấy là một sát thủ phục kích tàn độc nhất thế giới đầm lầy, sẵn sàng kích hoạt một đòn tấn công sấm". Bố cục: phóng viên chiến trường mặc áo gile chống đạn cầm sổ tay và micro chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): phóng viên giơ ống nhòm hồng ngoại quan sát cò mỏ giày đứng im như khúc gỗ chết
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "sét có thể chẻ đôi cả một con cá sấu non! Hãy cùng chúng tôi bật máy quay hồng ngoại và bám sát đối tượng trong 24h nghẹt thở ngay sau đây! Chẳng một chuyển động thừa, chẳng một cái chớp mí mắt, con quái vật này đã biến sự nhẫn nại thành một thứ nghệ thuật rình mồi tối thượng chưa từng có trong lịch sử tự nhiên.". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): bóng đen cò mỏ giày cao 1.5m in hằn trên nền trời xám tro đầy vẻ ma mị
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bây giờ ống kính siêu cận cảnh của chúng tôi đã bắt trọn cấu trúc kinh dị nhất trên cơ thể Tượng Đá Tiền Sử: Chiếc mỏ khổng lồ độc nhất vô nhị trong thế giới". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): chiếc mỏ khổng lồ hình guốc gỗ Hà Lan choán hết nửa khung hình với các đường vân đá
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "loài chim! Dài tới 24cm, chu vi đo được hơn 50cm, chiếc mỏ này phình to tròn trịa trông giống hệt như một chiếc guốc gỗ của những người thợ Hà Lan cổ đại. Tên khoa học của nó là Balaeniceps rex, dịch nôm na là Vua Đầu Cá Voi. Nhưng". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): thước đo kỹ thuật đo chiều dài mỏ 24cm và chu vi hơn 50cm
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "khác xa với vẻ ngoài cục mịch hài hước, chiếc mỏ này thực chất là một cỗ máy chém sinh học được tôi luyện qua suốt bao kỷ nguyên tiến hóa! Khối sừng khổng lồ này có thể tích buồng chứa lớn thứ ba trong toàn bộ các loài chim biết". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): mép mỏ sắc lẹm như hai lưỡi dao phay công nghiệp phản chiếu ánh thép lạnh lùng
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "bay trên thế giới, tạo ra một trọng tâm lệch hẳn về phía trước nhưng lại được cân bằng tuyệt đối bởi chiếc đuôi xòe rộng. Hãy quan sát thật kỹ hai mép mỏ! Chúng sắc lẹm không khác gì một cặp lưỡi dao phay công nghiệp, có khả năng cắt". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): chiếc móc sừng nhọn hoắt quặp ngược xuống ở đầu mỏ như chiếc mỏ neo sắt
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "đứt các sợi gân dai nhất chỉ bằng một lực khép nhẹ. Và ở ngay đầu mỏ trên, một chiếc móc sừng nhọn hoắt quặp ngược xuống dưới như một chiếc mỏ neo sắt. Khi chiếc mỏ này đập sập lại, chiếc móc sừng sẽ cắm phập vào hộp sọ con". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): sơ đồ cơ bắp cuồn cuộn ở gáy và đốt sống cổ cứng như thép chịu lực
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "mồi, khóa chặt mục tiêu không cho bất kỳ giọt chất lỏng hay sinh lực nào có cơ hội thoát ra ngoài. Lực bấm của bộ hàm này khi khép chặt có thể nghiền nát cả những lớp mai rùa nước ngọt dày cộp hay những bộ vảy cứng như giáp". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): bộ hàm khép chặt nghiền nát mai rùa nước ngọt và giáp sắt của cá cổ đại
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "sắt của các loài cá cổ đại bơi lội dưới tầng đáy bùn lầy. Với một khối lượng mỏ nặng trịch như thế, chiếc cổ của hươu hay cò bình thường sẽ bị gãy gập vì mất cân bằng trọng tâm. Nhưng thiên nhiên đã đúc cho Tượng Đá Tiền Sử". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): xương sọ dày đặc canxi gấp 3 lần hấp thụ xung chấn va đập cực mạnh
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "một hệ thống đốt sống cổ cứng như thép nguội, kết hợp với các bó cơ gáy cuồn cuộn có khả năng giật ngược chiếc mỏ nặng cả ki-lô-gam với gia tốc cực lớn. Chiếc guốc gỗ này không chỉ dùng để mổ, nó là một chiếc xẻng xúc bùn, một". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động) chú cá phổi châu phi trơn trượt vây như mái chèo đang ngoi lên thở: cò mỏ giày giơ cao chiếc mỏ xúc bùn đe dọa lũ quái vật trơn trượt
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chiếc kẹp tạ nặng tấn và là một vũ khí hủy diệt chuyên biệt để nuốt trọn những con quái vật trơn trượt dưới đáy đầm lầy tăm tối! Cấu trúc xương sọ của nó có mật độ canxi dày đặc gấp ba lần các loài cò bình thường, hấp thụ hoàn toàn xung chấn khi va đập mạnh xuống đáy đầm nước mà không làm tổn thương các mô mềm bên trong não.". Bố cục: phóng viên chiến trường mặc áo gile chống đạn cầm sổ tay và micro: phóng viên kinh ngạc ghi chép vào sổ tay về cỗ máy chém sinh học hoàn hảo
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Trời đã về chiều, màn đêm đen đặc đang bao trùm lấy đầm lầy châu Phi. Đột nhiên, một tràng âm thanh chát chúa vang dội xé toạc không gian yên tĩnh! Bằng! Bằng! Tạch". Bố cục: phóng viên chiến trường mặc áo gile chống đạn cầm sổ tay và micro: màn đêm buông xuống đầm lầy, cả đoàn phóng viên hoảng hốt nằm rạp xuống bùn
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tạch tạch tạch! Cả đoàn phóng viên chúng tôi hoảng hốt nằm rạp xuống bùn lầy vì tưởng chừng như đang có một cuộc đấu súng ác liệt giữa các tay súng phiến quân trang bị súng trường tự động AK! Nhưng khi ngẩng đầu lên qua ống nhòm nhìn". Bố cục: chú ngơ ngác giật mình hoảng hốt bịt tai trước tiếng súng máy: chú ngơ ngác giật mình hoảng hốt bịt tai tưởng đấu súng trường tự động AK
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "đêm, nguồn gốc của âm thanh kinh hoàng ấy lại phát ra từ chính chiếc mỏ của Tượng Đá Tiền Sử! Từng tràng tiếng nổ đanh gọn, dứt khoát và khô khốc vang dội từ bờ sậy bên này sang đảo lau bên kia, khiến cả bầy chim nước hoảng". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): cò mỏ giày ngửa cổ ra sau dập hai hàm mỏ vào nhau với tốc độ siêu thanh
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "hốt vỗ cánh bay tán loạn lên bầu trời mờ mịt. Trời ơi tiếng gì đanh thép như súng máy liên thanh nổ giòn giã thế, có nguy hiểm tính mạng không phóng viên ơi? Bình tĩnh nào người anh em ngơ ngác, đó là tiếng gõ mỏ chào sân". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): sơ đồ khoang rỗng buồng cộng hưởng âm thanh bên trong mỏ phát ra tiếng nổ 100 dB
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "của chú chim đấy! Hiện tượng này trong giới điểu học được gọi là Bill-clattering. Khi muốn khẳng định chủ quyền lãnh thổ hoặc giao tiếp với bạn tình, Tượng Đá Tiền Sử sẽ ngửa cổ ra sau rồi dập hai hàm mỏ vào nhau với tốc độ siêu thanh.". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): tần số rung động của tiếng gõ mỏ làm rung chuyển mặt lá súng trên đầm nước
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Do bên trong mỏ có cấu trúc khoang rỗng hoạt động như một buồng cộng hưởng âm thanh, mỗi cú đập tạo ra tiếng nổ vang dội lên tới hơn 100 dB, tương đương với tiếng súng máy quân dụng nhả đạn cự ly gần! Tần số rung động của". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): lũ linh cẩu và báo đốm giật mình kinh hãi tháo chạy khỏi tiếng gõ mỏ đanh thép
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tiếng gõ mỏ này mạnh đến mức làm rung chuyển cả những mặt lá súng nổi trên mặt nước xung quanh, tạo nên một hiệu ứng áp chế tâm lý nghẹt thở giữa không gian tĩnh mịch của màn đêm. Âm thanh chát chúa này có thể truyền xa tới". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): cò mỏ giày sừng sững tuyên bố chủ quyền lãnh thổ giữa làn sương mù đêm
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "cả cây số qua làn sương mù đầm lầy, làm cho lũ cá sấu, linh cẩu và cả những đàn báo đốm đi săn đêm cũng phải giật mình kinh sợ mà dạt ra xa. Đó là lời tuyên ngôn đanh thép khẳng định rằng: Vùng đầm lầy tăm tối". Bố cục: phóng viên chiến trường mặc áo gile chống đạn cầm sổ tay và micro: phóng viên thở phào nhẹ nhõm khi nhận ra vũ khí chỉ là chiếc mỏ gõ liên thanh
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "này đã có chủ nhân, và bất kỳ kẻ nào dám xâm phạm vùng nước phục kích của nó sẽ phải đối diện với chiếc kẹp tử thần! Đối với những con chim trưởng thành khác cùng loài, tiếng gõ mỏ này mang thông điệp cấm xâm phạm bất khả xâm phạm, giúp chúng phân chia lãnh thổ rộng lớn hàng chục cây số vuông mà không cần phải đổ nước màu trực diện.". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): cò mỏ giày thu cổ lại trở về trạng thái tượng đá im lìm trong bóng tối
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bây giờ là khoảnh khắc săn mồi đắt giá nhất mà đoàn làm phim chúng tôi đã phải phục kích ròng rã suốt mười tiếng đồng hồ dưới đầm nước hôi thối". Bố cục: chú cá phổi châu phi trơn trượt vây như mái chèo đang ngoi lên thở: chú cá phổi châu phi khổng lồ dài cả mét ngoi lên mặt nước đớp không khí
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "để ghi lại. Dưới lớp bèo hoa dâu đục ngầu, một con cá phổi châu Phi khổng lồ dài gần một mét đang từ từ trồi lên mặt nước để đớp không khí. Nó hoàn toàn không hề hay biết rằng, cách đó chỉ hai bước chân,". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): đôi mắt vàng rực của cò mỏ giày khóa chặt mục tiêu với thị giác 3D lập thể
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tượng Đá Tiền Sử đã nhìn thẳng mục tiêu ngộ nghĩnh bằng đôi mắt vàng rực có thị giác lập thể ba chiều hoàn hảo. Đôi mắt to tròn màu vàng rơm của nó không nằm lệch sang hai bên như chim bồ câu hay gà vịt, mà hướng thẳng". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): toàn bộ cơ thể 7kg của cò mỏ giày đổ ụp xuống mặt nước như tòa nhà sụp đổ Collapse strike
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "về phía trước giống hệt mắt cú vẹo hay mắt người, cho phép đo đạc cự ly chính xác đến từng mi-li-mét. Và rồi, bùm! Không hề có một động tác nhấp nhử hay chuẩn bị, toàn bộ cơ thể nặng 7kg của Tượng Đá Tiền Sử". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): nước bắn tung tóe mù mịt như bom mìn phát nổ dưới tốc độ lao mồi 35km/h
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "đổ ụp thẳng xuống mặt nước như một tòa nhà bê tông sụp đổ! Tuyệt kỹ săn mồi này được các nhà khoa học gọi là Collapse strike, tức là đòn bổ nhào sụp đổ. Con chim phóng cả thân hình, sải cánh rộng hai mét rưỡi". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động) chú cá phổi châu phi trơn trượt vây như mái chèo đang ngoi lên thở: cá phổi giãy giụa trong chiếc kẹp mỏ khổng lồ bị nghiền nát hộp sọ
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "và chiếc mỏ nặng trịch cắm thẳng xuống bùn lầy với vận tốc 35km/h một giờ. Lực va chạm mạnh đến mức nước bắn tung tóe mù mịt như một quả mìn nổ chậm dưới lòng hồ! Cú rơi tự do này sử dụng chính trọng lượng". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): cò mỏ giày giũ sạch bùn rác và bèo hoa dâu trên mình con mồi
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "cơ thể đồ sộ 7kg làm gia tốc rơi, biến toàn bộ cơ thể thành một khối chùy công phá dội thẳng xuống đầu con mồi trong chớp mắt. Khi con chim ngẩng đầu lên khỏi làn nước đục ngầu, con cá phổi giãy giụa tuyệt vọng". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): cò mỏ giày nuốt trọn cả con cá dài cả mét vào dạ dày chỉ sau 3 cú ực
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "đã nằm gọn trong chiếc mỏ khổng lồ. Con chim dùng cạnh mỏ sắc như dao phay nghiền nát hộp sọ con mồi, giũ sạch bùn đất và bèo rác rồi nuốt trọn cả con cá dài cả mét vào dạ dày chỉ sau ba cú ực.". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): con chim hớp một ngụm nước trong súc sạch mỏ với vẻ điềm tĩnh rợn người
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Một màn trình diễn săn mồi bạo lực, chính xác và tàn khốc đến nghẹt thở! Con chim dùng đầu lưỡi hình ngọn giáo đẩy con mồi vào họng, rồi hớp một ngụm nước trong để súc sạch cặn bùn, thể hiện một sự điềm tĩnh lạnh lùng đến rợn gáy sau khi vừa thực hiện một pha sát hại đẫm nước màu.". Bố cục: phóng viên chiến trường mặc áo gile chống đạn cầm sổ tay và micro: phóng viên nín thở kinh hoàng trước màn săn mồi tàn khốc vừa ghi hình được
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đến đây, quý vị khán giả sẽ thấy một nghịch lý tâm lý cực kỳ kỳ quặc ở loài chim này. Khi tiếp xúc với con người, đặc biệt là trong các trung tâm bảo tồn hay vườn thú, Tượng Đá". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): cò mỏ giày ở vườn thú cúi gập đầu đáp lễ chào người chăm sóc như một quý ông Anh quốc
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tiền Sử lại cư xử như một quý ông người Anh cực kỳ lịch lãm. Nếu một người chăm sóc cúi gập người chào nó một cách cung kính, chú chim sẽ lập tức cúi thấp đầu xuống đáp lễ, lắc lư chiếc mỏ nhẹ nhàng và phát ra những tiếng rù rù êm ái như". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): khách tham quan thích thú chụp ảnh cùng chú chim lễ phép đáng yêu nhất thế giới
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "một lời chào mừng nồng nhiệt. Nhiều du khách đã phải thốt lên rằng đây là loài chim lễ phép và đáng yêu nhất hành tinh! Sự tương phản giữa ngoại hình hung dữ như khủng long tiền sử và phong thái cúi đầu chào lịch thiệp này đã tạo nên một cơn sốt kỳ thú". Bố cục: phát thanh viên tin tức trường quay đeo tai nghe chuyên nghiệp: phát thanh viên hé lộ bí mật đen tối rùng rợn trong tổ đẻ hoang dã
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "trên toàn mạng xã hội, biến nó thành biểu tượng văn hóa độc đáo ở đất nước Nhật Bản. Alo phóng viên, sổ tay thực địa có ghi chương đen tối rùng rợn về chúng trong tổ hoang dã đúng không? Đáng tiếc là đúng như vậy thưa trường quay! Ẩn sau vẻ ngoài lịch thiệp". Bố cục: chú cò con anh lông xám hung hăng to lớn trong tổ chú cò con em yếu ớt tội nghiệp kêu chít chít cầu cứu: trong tổ chim hoang dã con chim anh to lớn hung hăng mổ tới tấp vào đầu đứa em nhỏ
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "ấy là một sự thật tàn khốc đến lạnh người trong tổ đẻ, mang tên hiện tượng Cainism, tức là sát hại anh em ruột. Chim mẹ luôn đẻ hai quả trứng để dự phòng rủi ro. Khi quả trứng đầu tiên nở ra một con non khỏe mạnh, và vài ngày sau quả trứng thứ". Bố cục: chú cò con em yếu ớt tội nghiệp kêu chít chít cầu cứu: chim con em yếu ớt rách lông kêu chít chít cầu cứu trong tuyệt vọng
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "hai nở ra đứa em bé nhỏ, một cuộc chiến sinh tồn đẫm nước màu bắt đầu. Con chim anh to lớn hơn sẽ liên tục dùng mỏ mổ vào đầu em mình, cắn xé lông tơ và đẩy đứa em ra mép tổ dưới nắng thiêu đốt. Tiếng kêu chít chít cầu cứu yếu ớt của". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động) chú cò con anh lông xám hung hăng to lớn trong tổ: chim mẹ đứng nhìn lạnh lùng không hề can thiệp để mặc con lớn bạo hành em
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "đứa em nhỏ bé lọt thỏm giữa tiếng gió rít qua đầm lầy, trong khi người anh lớn liên tục giáng những cú mổ sắc nhọn để xua đuổi kẻ cạnh tranh sinh tồn duy nhất của mình. Đau lòng hơn cả, chim mẹ đứng ngay bên cạnh chứng kiến toàn bộ sự việc nhưng tuyệt". Bố cục: chú cò con anh lông xám hung hăng to lớn trong tổ: con chim anh nuốt trọn toàn bộ thức ăn và nước uống độc chiếm sự sống
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "đối không can thiệp. Toàn bộ thức ăn và nước uống đều được dồn hết cho đứa con lớn, trong khi đứa em yếu ớt dần kiệt sức và chết đói trong sự cô độc tàn nhẫn. Đó là quy luật chọn lọc tự nhiên khắc nghiệt của đầm lầy: Nguồn thức ăn quá khan hiếm,". Bố cục: chú cò con em yếu ớt tội nghiệp kêu chít chít cầu cứu: đứa em bé bỏng kiệt sức chết đói dưới cái nắng thiêu đốt của đầm lầy
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "và chim bố mẹ chỉ đủ sức nuôi duy nhất một cỗ máy trò chơi đuổi bắt hoàn hảo để duy trì nòi giống! Sự chọn lọc tự nhiên không có chỗ cho lòng thương hại hay những giọt nước mắt ủy mị. Chỉ những cá thể mạnh nhất, tàn nhẫn nhất và có sức đề kháng cao nhất mới xứng đáng đại diện cho giống loài tiếp tục thống trị vùng đầm lầy.". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): quy luật sinh tồn khắc nghiệt Cainism chỉ giữ lại một chiến binh mạnh nhất
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sau 24h theo chân Tượng Đá Tiền Sử giữa đầm lầy châu Phi hoang dã, chúng tôi nhận ra rằng đây không đơn thuần là một loài chim,". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): cò mỏ giày sừng sững như hóa thạch sống thời tiền sử giữa đầm lầy bình minh
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "mà là một hóa thạch sống kiên cường mang linh hồn của những loài khủng long ăn thịt từ kỷ Jura còn sót lại giữa thời hiện đại. Từ sự nhẫn nại đứng im hàng giờ không chớp mắt, chiếc mỏ guốc gỗ". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): bức chân dung nghệ thuật tượng đá bất tử kiên định chờ đợi thời cơ
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "sắc lẹm chém đôi con mồi, tiếng gõ mỏ vang dội như súng máy quân dụng, cho đến sự lạnh lùng tàn nhẫn để sinh tồn, tất cả đã tạo nên một kiệt tác thích nghi đỉnh cao của tạo hóa. Nó đứng". Bố cục: phóng viên chiến trường mặc áo gile chống đạn cầm sổ tay và micro: phóng viên đứng trên mũi thuyền đầm lầy tổng kết bài học về sự nhẫn nại
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "đó như một tượng đài bất hoại chứng kiến sự thăng trầm của lịch sử tự nhiên, nhắc nhở chúng ta về sức mạnh kỳ diệu của sự kiên định trước những biến đổi khắc nghiệt của môi trường. Cuộc đời của chú". Bố cục: phóng viên chiến trường mặc áo gile chống đạn cầm sổ tay và micro: bài học về sự tĩnh lặng kiên định để tung đòn quyết định thay đổi cục diện
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chim Mỏ Giày mang lại cho chúng ta một bài học sâu sắc về sự kiên nhẫn và thời cơ trong cuộc sống: Đôi khi, điều làm nên sự vĩ đại không phải là việc bạn chạy nhảy lăng xăng khắp nơi, mà". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): màn hình bình chọn: Tiếng gõ mỏ súng máy AK đối đầu sự kiên nhẫn đứng im 5 tiếng
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "là khả năng giữ vững sự tĩnh lặng tuyệt đối, kiên định chờ đợi thời điểm chín muồi để tung ra một đòn quyết định thay đổi toàn bộ cục diện! Bạn ấn tượng nhất với đặc điểm nào của Tượng Đá Tiền". Bố cục: phóng viên chiến trường mặc áo gile chống đạn cầm sổ tay và micro phát thanh viên tin tức trường quay đeo tai nghe chuyên nghiệp chú ngơ ngác giật mình hoảng hốt bịt tai trước tiếng súng máy: dàn nhân vật vẫy tay chào khán giả và kêu gọi để lại bình luận
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Sử: Tiếng gõ mỏ nổ giòn như súng máy AK hay sự kiên nhẫn đứng bất động 5 tiếng đồng hồ? Hãy để lại bình luận chia sẻ cảm nghĩ nhé! Còn ở tập tiếp theo, xưởng vũ khí tự nhiên sẽ đưa". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): cò mỏ giày chầm chậm cúi đầu chào tạm biệt khán giả theo nghi thức quý ông
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "các bạn diện kiến một pháo đài di động với 30.000 mũi tên ngạnh ngược có khả năng tự găm sâu vào thịt mãnh thú! Hãy học cách đứng vững trước sóng gió cuộc đời như chú chim mỏ giày giữa đầm lầy hoang dã, để khi thời cơ đến, bạn sẽ bứt phá mạnh mẽ và làm nên những điều phi thường nhất!". Bố cục: NO_HERO: hình ảnh bí ẩn của Nhím Lông Nhọn với 30.000 mũi tên tự rút sâu nhá hàng tập sau
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Gặp người thì cúi đầu chào lịch sự như một quý ông, nhưng với em ruột trong tổ thì ra tay tàn nhẫn đến lạnh người?!". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường: cận cảnh cò mỏ giày cúi đầu đáp lễ người chăm sóc như một quý ông Anh quốc
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Hãy nhìn chú Cò Mỏ Giày kỳ dị giữa đầm lầy châu Phi này xem! Mang mật danh Tượng Đá Tiền Sử, nó có thể đứng bất động giữa bãi lau sậy suốt 5 tiếng liên tục mà không thèm chớp mắt lấy một lần!". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường: toàn cảnh cò mỏ giày đứng bất động như tượng đá giữa đầm lầy Bangweulu
```
</details>

<details><summary>S02b</summary>

```text
HÌNH S02b (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: Mang mật danh Tượng Đá Tiền Sử, nó có thể đứng bất động giữa bãi lau sậy suốt 5 tiếng liên tục mà không thèm chớp mắt lấy một lần! Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường: cò mỏ giày đứng bất động giữa bãi lau sậy, đôi mắt vàng hổ phách trừng trừng không chớp, không khí tĩnh mịch cổ xưa
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Chiếc mỏ dài 24cm của nó trông như chiếc guốc gỗ nhưng mép sắc lẹm như dao phay, sẵn sàng tung cú bổ nhào 35km/h một giờ chém đôi cá phổi và cá sấu non!". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường: chiếc mỏ guốc gỗ dài 24cm mép sắc lẹm như dao phay đe dọa con mồi
```
</details>

<details><summary>S03b</summary>

```text
HÌNH S03b (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: sẵn sàng tung cú bổ nhào 35km/h một giờ chém đôi cá phổi và cá sấu non! Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường: cú bổ nhào thần tốc tạo sóng nước dữ dội, mỏ cắm phập chém đôi con mồi
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Mỗi khi đêm xuống, nó dập mỏ tạo ra tiếng nổ đanh thép như súng máy liên thanh nổ giòn vang xa hàng cây số!". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động): cò mỏ giày dập mỏ tạo ra tiếng nổ súng máy 100 dB xé toạc màn đêm
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Ở vườn thú, nếu bạn cúi chào, nó sẽ lập tức cúi gập đầu đáp lễ cực kỳ đáng yêu.". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường: cò mỏ giày cúi đầu gập người chào hỏi du khách cực kỳ lịch thiệp
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Thế nhưng trong tự nhiên hoang dã, chim non mới nở sẽ liên tục mổ, cắn xé và bỏ đói". Bố cục: chú cò con anh lông xám hung hăng to lớn trong tổ chú cò con em yếu ớt tội nghiệp kêu chít chít cầu cứu: chim con anh to lớn trong tổ hung hăng mổ vào đầu đứa em ruột
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "đứa em ruột của mình đến chết để độc chiếm nguồn thức ăn, dưới sự làm ngơ tuyệt đối của chim mẹ!". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động) chú cò con em yếu ớt tội nghiệp kêu chít chít cầu cứu: chim mẹ đứng nhìn lạnh lùng để mặc đứa em kiệt sức chết đói
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Một nghịch lý sinh tồn rùng mình đến nghẹt thở của tự nhiên!". Bố cục: chú cò mỏ giày hoạt hình ngộ nghĩnh đeo thẻ phóng viên cầm micro chiến trường phóng viên chiến trường mặc áo gile chống đạn cầm sổ tay và micro: phóng viên chiến trường cùng cò mỏ giày giơ cánh chào kết màn ấn tượng
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/53 của video YouTube về Cò Mỏ Giày). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa vẽ tay đặc trưng cho chủ đề, nét mực sắc nét, màu sắc tương phản cuốn hút, tối giản giàu tính biểu tượng khoa học; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động). Nhân vật phụ cố định: phóng viên chiến trường mặc áo gile chống đạn cầm sổ tay và micro; phát thanh viên tin tức trường quay đeo tai nghe chuyên nghiệp; chú ngơ ngác giật mình hoảng hốt bịt tai trước tiếng súng máy; chú cá phổi châu phi trơn trượt vây như mái chèo đang ngoi lên thở; cá sấu con hoảng sợ rụt đầu xuống bùn lầy; chú cò con anh lông xám hung hăng to lớn trong tổ; chú cò con em yếu ớt tội nghiệp kêu chít chít cầu cứu. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/8 của video YouTube Shorts về Cò Mỏ Giày). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa vẽ tay đặc trưng cho chủ đề, nét mực sắc nét, màu sắc tương phản cuốn hút, tối giản giàu tính biểu tượng khoa học; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú cò mỏ giày hoạt hình ngộ nghĩnh (cao lớn, chiếc mỏ guốc gỗ khổng lồ, lông xám tro đá phiến, đôi mắt vàng đục bất động). Nhân vật phụ: phóng viên chiến trường mặc áo gile chống đạn cầm sổ tay và micro; chú cò con anh lông xám hung hăng to lớn trong tổ; chú cò con em yếu ớt tội nghiệp kêu chít chít cầu cứu. 
```
</details>

## 7. SEO

- **title:** Tượng Đá Tiền Sử Cò Mỏ Giày: Cúi Chào Người Nhưng Tàn Nhẫn Với Em Ruột?! | Tập 48
- **hook_paragraph:** Cò Mỏ Giày (Shoebill) cao 1.5m có thể đứng im 5 tiếng không chớp mắt, sở hữu chiếc mỏ guốc sắc bén gõ đanh thép như súng máy AK. Tại sao loài chim lịch sự cúi đầu chào người này lại có bí mật rùng rợn sát hại em ruột trong tổ?
- **question:** Bạn thấy điều gì ở Cò Mỏ Giày gây sốc nhất: Tiếng gõ mỏ như súng máy AK hay hành vi sát hại em ruột?
- **next_teaser:** Ở tập tiếp theo, chúng ta sẽ giải mã Nhím Lông Nhọn với 30.000 mũi tên tự rút sâu vào thịt báo hoa mai!
- **shorts_title:** Cò mỏ giày: Chào người lịch sự nhưng tàn nhẫn với em ruột?! 🪶 #shorts #comogiay
- **shorts_desc:** Cò Mỏ Giày đứng im 5 tiếng như tượng đá, tiếng gõ mỏ như súng máy AK, gặp người cúi đầu chào nhưng lại sát hại em ruột trong tổ!
- **bullets:** Đứng bất động 5 tiếng đồng hồ như tượng đá giữa đầm lầy châu Phi · Chiếc mỏ dài 24cm nặng trịch sắc như dao phay nuốt trọn cá phổi · Tiếng gõ mỏ đanh thép 100 dB vang dội như tiếng súng máy quân dụng · Nghi thức cúi chào lịch sự với người nhưng tàn nhẫn sát hại con thứ Cainism
- **tags:** cò mỏ giày, co mo giay, shoebill, balaeniceps rex, tieng go mo shoebill, the gioi dong vat, ve chuyen hoang da, dong vat ky thu, khoa hoc vui, sat hai con thu, cainism, chim tien su
- **hashtags:** #CoMoGiay #Shoebill #TheGioiDongVat #VeChuyenHoangDa #KhoaHoc #DongVatKyThu

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-48-co-mo-giay
python src/episode/pipeline.py tts    projects/tap-48-co-mo-giay     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-48-co-mo-giay     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-48-co-mo-giay     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-48-co-mo-giay              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-48-co-mo-giay --force
python scripts/beat_sheet.py projects/tap-48-co-mo-giay               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-48-co-mo-giay/audio/shorts.wav projects/tap-48-co-mo-giay/renders/tap-48-co-mo-giay_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-48-co-mo-giay
python src/episode/pipeline.py seo    projects/tap-48-co-mo-giay
python src/episode/episode_doc.py     projects/tap-48-co-mo-giay
```
