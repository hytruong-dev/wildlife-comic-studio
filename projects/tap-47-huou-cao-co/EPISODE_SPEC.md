# TẬP 47 — HƯƠU CAO CỔ · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-47-huou-cao-co`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-47-huou-cao-co`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F2` · **Persona giọng:** `ky_su_vu_khi` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Hươu Cao Cổ |
| Tiêu đề YouTube | Bí Ẩn Cổ Dài 2 Mét: Cúi Đầu Uống Nước Sao Không Bị Nổ Não?! \| Hươu Cao Cổ \| Tập 47 |
| Video dài | `renders/tap-47-huou-cao-co_long.mp4` — 11:59.8 (719.8s) |
| Shorts | `renders/tap-47-huou-cao-co_shorts.mp4` — 0:52.0 (52.0s) |
| Thumbnail | `renders/tap-47-huou-cao-co_thumbnail.jpg` |
| Số hình | dài 68 beat / 68 ảnh riêng; Shorts 11 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.12**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/53 của video YouTube về Hươu Cao Cổ). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa vẽ tay đặc trưng cho chủ đề, nét mực sắc nét, màu sắc tương phản cuốn hút, tối giản giàu tính biểu tượng khoa học; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động). Nhân vật phụ cố định: kỹ sư trưởng mặc đồ bảo hộ xưởng cơ khí, cầm cờ lê và bản vẽ đường ống thủy lực; cô trợ lý kỹ thuật đeo kính bảo hộ cầm bảng kẹp tài liệu ghi chép áp suất; chú ngơ ngác gãi đầu hoảng hốt trước đồng hồ đo áp suất; bé con đội mũ safari đeo ba lô tò mò chỉ tay hỏi; sư tử châu phi bờm rậm hoảng hốt né đòn đạp hậu của hươu; mô hình quả tim thép 11kg với đồng hồ đo áp suất 300 mmHg; sơ đồ mạng lưới vi mạch xốp giảm áp búa nước dưới đáy sọ. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — BẢN VẼ THÁP CẨU 5 MÉT GIỮA SAVANNAH
*Thẻ chương:* MỔ XẺ THÁP CẨU SAVANNAH 2M

*Badge:* `SƠ ĐỒ THỦY LỰC` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene01_p0.wav` (1017 ký tự) · mood `tram_bi_an`

```text
Chào mừng toàn thể các kỹ sư cơ khí sinh học và các chuyên gia giải mã vũ khí tự nhiên đã quay trở lại với xưởng nghiên cứu tối mật của chúng tôi! Hôm nay, ống nhòm viễn vọng của chúng ta sẽ hướng thẳng ra thảo nguyên châu Phi nắng cháy rực lửa, nơi một công trình kiến trúc cơ động cao nhất trên cạn đang lừng lững sải bước giữa đường chân trời. Hãy quan sát thật kỹ khối kết cấu sinh học đồ sộ ấy! Một khối lượng lừng lững nặng tới gần hai tấn, đỉnh đầu chót vót cách mặt đất hơn năm mét, vươn cao ngạo nghễ như một tháp truyền hình di động giữa bầy thú ăn cỏ. Giới động vật học thông thường gọi nó bằng cái tên quen thuộc là Hươu Cao Cổ, nhưng trong mắt ban thiết kế công trình của chúng tôi, đây đích thị là cỗ máy Tháp Cẩu Di Động vĩ đại nhất từng được tự nhiên tạo tác. Bạn có bao giờ tự đặt câu hỏi dưới góc nhìn vật lý thuần túy: Làm thế nào để bơm một cột máu đỏ nặng trịch ngược chiều trọng lực trái đất lên độ cao hai mét suốt hai mươi tư trên hai mươi tư giờ không ngừng nghỉ mà không làm nổ tung động cơ?
```
**Part 1** → `audio/vs/scene01_p1.wav` (107 ký tự) · 🎭 cameo `co_tro_ly`

```text
Báo cáo chỉ huy, nếu dùng máy bơm bình thường đẩy nước lên tầng năm, ống nhựa sẽ nổ tung vì áp lực quá tải!
```
**Part 2** → `audio/vs/scene01_p2.wav` (959 ký tự) · mood `hao_hung`

```text
[laughter] Nhận định hoàn toàn chuẩn xác không cần chỉnh cô trợ lý kỹ thuật ạ! [surprise-oh] Định luật thủy tĩnh cơ bản quy định rằng cứ mỗi mét chất lỏng dâng cao, áp suất đáy sẽ tăng lên dữ dội. Nếu cơ thể một người bình thường chúng ta bị kéo giãn chiếc cổ ra hai mét như thế này, quả tim con người sẽ bất lực hoàn toàn, không thể bơm nổi một giọt máu nào lên tới đỉnh đầu, và toàn bộ hệ thần kinh trung ương sẽ chết đói vì cạn kiệt oxy chỉ sau đúng ba giây ngắn ngủi. Ấy vậy mà Tháp Cẩu Di Động không những không hề choáng váng, nó còn thong dong vươn chiếc lưỡi dài nửa mét màu tím đen để tước từng chiếc lá gai nhọn hoắt của cây keo bao báp, thậm chí khi cần nó có thể bứt tốc phi nước đại với vận tốc năm mươi cây số một giờ. Mọi linh kiện bên trong con vật này đều được tôi luyện với dung sai cực hạn, vượt xa mọi tiêu chuẩn công nghiệp cơ khí nặng hiện đại nhất. Ngay bây giờ, hãy cầm cờ-lê tháo bu-lông và mở tung bản vẽ khoang động cơ chính ra xem!
```

### scene02 — ĐỘNG CƠ V8 BƠM MÁU CAO ÁP
*Thẻ chương:* TRÁI TIM GẤP ĐÔI ÁP LỰC NGƯỜI

*Badge:* `ĐỘNG CƠ TIM 11KG` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene02_p0.wav` (878 ký tự) · mood `hao_hung`

```text
Để nâng được một cột chất lỏng nhớt có tỷ trọng nặng hơn nước lên độ cao thẳng đứng hai mét ngược chiều gia tốc trọng trường, yêu cầu tiên quyết đầu tiên trên bản vẽ chính là một khối động cơ bơm áp lực siêu cường. Trái tim của Tháp Cẩu Di Động hoàn toàn không phải dạng vừa, nó là một khối cơ bắp rắn rỏi nặng tới mười một ki-lô-gam, dài hơn sáu mươi xăng-ti-mét và sở hữu thể tích buồng chứa cực lớn, có khả năng luân chuyển hàng chục lít máu mỗi phút. Đặc biệt nhất chính là thành tâm thất trái của nó, nơi trực tiếp tạo ra lực đẩy lên động mạch chủ, dày tới bảy xăng-ti-mét, đanh chắc và kiên cố như một tấm lốp xe tải bọc thép chuyên dụng. Khi cỗ máy sinh học này thực hiện một chu kỳ co bóp toàn phần, nó tạo ra một áp lực tâm thu khủng khiếp lên tới ba trăm mi-li-mét thủy ngân, tức là gấp đôi mức huyết áp đỉnh cao của một vận động viên điền kinh Olympic khỏe mạnh nhất!
```
**Part 1** → `audio/vs/scene02_p1.wav` (991 ký tự) · mood `don_dap`

```text
Tại sao hệ thống này lại bắt buộc phải vận hành ở mức áp lực bạo lực đến như vậy? Bởi vì định luật thủy tĩnh không hề có sự nhân nhượng cho bất kỳ sinh vật nào! Dòng máu đỏ xuất phát từ van tim ở lồng ngực phải leo dốc thẳng đứng vượt qua lực hút trái đất trên quãng đường dài hai mét để chạm tới vỏ não. Cứ mỗi ba mươi xăng-ti-mét chiều cao tăng thêm, áp suất thủy tĩnh sẽ sụt giảm khoảng hai mươi lăm mi-li-mét thủy ngân. Nếu như áp lực bơm tim của hươu chỉ duy trì ở mức một trăm hai mươi như con người chúng ta, thì khi dòng máu leo tới nửa đoạn cổ, áp suất đẩy đã giảm về mức số không, khiến máu ngừng chảy và chảy ngược trở lại, dẫn đến tình trạng thiếu máu não tức thì. Nhờ việc duy trì công suất cực đại ba trăm mi-li-mét thủy ngân ngay tại cửa xả của tim, khi dòng máu chạm tới đỉnh đầu sau hành trình leo dốc gian nan, áp suất còn lại ở não bộ vẫn duy trì hoàn hảo ở mức một trăm mi-li-mét thủy ngân, vừa vặn tuyệt đối để hệ thần kinh trung ương xử lý tín hiệu sắc bén như dao cạo.
```
**Part 2** → `audio/vs/scene02_p2.wav` (820 ký tự) · mood `hao_hung`

```text
Nhưng các kỹ sư cơ khí hãy đặc biệt chú ý đến một bí mật thiết kế đắt giá này! Một khối động cơ tim áp suất cao như vậy nếu đập dồn dập liên tục thì chẳng mấy chốc sẽ bị nổ van hoặc suy tim sớm. Thiên nhiên đã lập trình cho trái tim của Tháp Cẩu Di Động một nhịp đập cực kỳ điềm tĩnh, dao động từ bốn mươi đến chín mươi nhịp mỗi phút. Mỗi nhịp co bóp tống đi một thể tích máu khổng lồ vào gốc động mạch chủ. Thành của động mạch chủ ở hươu được gia cố bằng nhiều lớp sợi elastin siêu đàn hồi, hoạt động giống hệt như một bình tích áp thủy lực Windkessel trong kỹ thuật cơ khí đường ống. Bình tích áp này giãn nở để hấp thụ chấn động từ mỗi cú nén cao áp cực mạnh của tim, rồi co lại nhịp nhàng để duy trì dòng chảy liên tục và êm ái, biến dòng máu giật cục thành một dòng chảy ổn định tuần hoàn khắp cơ thể đồ sộ năm mét.
```

### scene03 — HỆ THỐNG XẢ ÁP RETE MIRABILE
*Thẻ chương:* HỆ THỐNG RETE MIRABILE XẢ ÁP

*Badge:* `MẠNG LƯỚI VAN KỲ DIỆU` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene03_p0.wav` (1013 ký tự) · mood `don_dap`

```text
Bây giờ mới thực sự là bài kiểm tra ứng suất kinh hoàng nhất trong toàn bộ quy trình vận hành của Tháp Cẩu Di Động. Mặc dù sở hữu chiều cao năm mét để với tới những cành cây cao chót vót, nhưng vũng nước uống duy nhất giữa sa mạc lại nằm sát sàn sạt dưới mặt đất. Để uống được nước, con vật không thể quỳ gối quá lâu vì dễ bị thú săn mồi phục kích. Nó buộc phải xoạc rộng hai chân trước sang hai bên rồi hạ thấp phần đầu xuống trong một cú rơi tự do sâu tới gần ba mét. Các bạn hãy làm một phép tính vật lý đơn giản: Một hệ thống ống dẫn đang chịu áp suất ba trăm mi-li-mét thủy ngân, nay lại được cộng dồn thêm toàn bộ trọng lượng của cột máu cao hai mét đổ dồn thẳng đứng từ trên ngực xuống đáy hộp sọ theo chiều gia tốc trọng trường. Áp lực máu tại khoang não lúc này sẽ lập tức tăng vọt lên tới gần năm trăm mi-li-mét thủy ngân! Ở bất kỳ loài động vật có vú nào khác, mức áp suất bạo tàn này thừa sức phá hủy toàn bộ mạng lưới mao mạch não mỏng manh, gây xuất huyết ồ ạt và tử vong tại chỗ chỉ trong tích tắc!
```
**Part 1** → `audio/vs/scene03_p1.wav` (116 ký tự) · 🎭 cameo `chu_ngo_ngac`

```text
Khoan đã thầy ơi, vậy tại sao đầu của nó không phát nổ tung toé như một quả bóng bay bằng cao su bị bơm quá áp suất?
```
**Part 2** → `audio/vs/scene03_p2.wav` (793 ký tự) · mood `hao_hung`

```text
[laughter] Một câu hỏi vô cùng thực tế và đáng giá triệu đô đấy người anh em ngơ ngác! [surprise-oh] Bí mật sống còn nằm ở một cụm chi tiết cơ khí sinh học tối mật được giấu kín ngay dưới đáy hộp sọ của hươu, mang tên khoa học là Rete Mirabile, tiếng Latin có nghĩa là Mạng Lưới Kỳ Diệu. Đây là một ma trận chằng chịt gồm hàng ngàn mạch máu nhỏ li ti, lồng ghép đan xen vào nhau giống hệt như một miếng bọt biển hấp thụ lực va đập thủy tĩnh. Khi Tháp Cẩu Di Động hạ thấp đầu xuống vũng nước, lượng máu áp suất cao ồ ạt đổ xuống sẽ lập tức bị mạng lưới này phân tán vào vô số nhánh rẽ nhỏ li ti. Thiết diện tổng của dòng chảy tăng vọt làm vận tốc dòng máu giảm xuống đột ngột, triệt tiêu hoàn toàn xung lực búa nước va đập trước khi những giọt máu có thể chạm tới các tế bào thần kinh nhạy cảm.
```
**Part 3** → `audio/vs/scene03_p3.wav` (1043 ký tự) · mood `don_dap`

```text
Chưa dừng lại ở đó đâu nhé! Dọc theo suốt chiều dài hai mét của tĩnh mạch cổ là cả một hệ thống các van một chiều cơ học đóng mở tự động cực kỳ tinh xảo. Ngay khoảnh khắc chiếc đầu hạ thấp quá tim, các van tĩnh mạch một chiều này lập tức sập chặt lại, ngăn chặn tuyệt đối tình trạng máu đen ứ đọng từ khoang ngực chảy ngược trở lại đầu gây tăng áp nội sọ. Và điều kỳ diệu nhất diễn ra khi con vật bất ngờ phát hiện thấy một con sư tử đang rình rập trong bụi rậm! Nó lập tức giật phắt chiếc đầu nặng nề cao vụt lên trời ở độ cao năm mét chỉ trong vòng chưa đầy một giây. Một cú giật ngược đột ngột như thế bình thường sẽ làm toàn bộ máu tụt dốc về tim, khiến não bộ rơi vào trạng thái thiếu oxy cục bộ và gây ngất xỉu ngay tức thì. Nhưng mạng lưới Rete Mirabile lại đóng vai trò như một kho dự trữ máu khẩn cấp, từ từ xả lượng máu tích trữ ra để nuôi dưỡng não trong lúc tim điều chỉnh lại nhịp đập, giúp con vật giữ vững sự tỉnh táo hoàn toàn để phóng nước đại tẩu thoát. Đó là một cơ chế giảm chấn thủy lực hai chiều hoàn mỹ đến từng phân tử!
```

### scene04 — BỘ ĐỒ PHI HÀNH GIA Ở CẲNG CHÂN
*Thẻ chương:* LỚP DA BẢO HỘ CHỐNG TĨNH MẠCH

*Badge:* `TẤT ÁP LỰC CHỐNG PHÙ` · *mood mặc định:* `nghiem_trang_gia`

**Part 0** → `audio/vs/scene04_p0.wav` (841 ký tự) · mood `nghiem_trang_gia`

```text
Giải quyết xong bài toán áp suất phức tạp ở phần đỉnh tháp, bây giờ mời toàn thể ban kỹ sư cùng chuyển ống kính xuống kiểm tra phần gầm của cỗ máy Tháp Cẩu Di Động. Với một sinh vật có tầm vóc khổng lồ đứng thẳng trên bốn chiếc chân khẳng khiu cao tới gần hai mét, áp lực thủy tĩnh ở cẳng chân dưới là một cơn ác mộng kỹ thuật không kém phần nan giải. Trọng lực đè nặng toàn bộ thể tích máu trong cơ thể dồn xuống các mao mạch ở bàn chân, tạo ra một áp suất nội mạch thường xuyên vượt ngưỡng hai trăm mi-li-mét thủy ngân. Để các bạn dễ hình dung, ở cơ thể con người chúng ta, chỉ cần phải đứng im bất động trong vài giờ liên tục, máu sẽ dồn xuống bàn chân làm tăng áp suất mao mạch, khiến huyết tương rò rỉ vào khoang gian bào gây phù nề mắt cá chân, suy giãn tĩnh mạch hoặc thậm chí vỡ mao mạch tạo thành các vết xuất huyết bầm tím dưới da.
```
**Part 1** → `audio/vs/scene04_p1.wav` (863 ký tự) · mood `hao_hung`

```text
Vậy thì điều kỳ diệu gì đã bảo vệ bốn chiếc chân khẳng khiu như những que tăm của hươu không bị nứt toác và phù nề sau hàng chục năm đứng liên tục giữa thảo nguyên? Câu trả lời là thiên nhiên đã trang bị cho nó một bộ tất áp lực sinh học hoàn hảo bậc nhất thế giới! Đây chính là cấu trúc cơ học mà sau này các nhà khoa học của cơ quan hàng không vũ trụ NASA đã phải cất công nghiên cứu tỉ mỉ để chế tạo ra bộ đồ kháng áp G-suit dành cho phi công tiêm kích siêu âm và các phi hành gia khi chịu gia tốc phóng cực đại. Bao bọc lấy toàn bộ phần cẳng chân của hươu là một lớp da dày cộm, cứng cáp và có độ đàn hồi cực kỳ thấp, ôm sát rạt lấy cơ thể giống như một lớp vỏ bọc bằng sợi carbon composite. Ngay bên dưới lớp da dày ấy là một màng cân cơ dày đặc và rắn chắc, bọc kín lấy từng thớ cơ và mạch máu như một chiếc băng cuốn y tế chuyên dụng được siết chặt tối đa.
```
**Part 2** → `audio/vs/scene04_p2.wav` (787 ký tự) · mood `hao_hung`

```text
Lớp vỏ bọc cơ học siêu bền này tạo ra một lực ép ngoại sinh cực mạnh tác động ngược trở lại thành mạch, cân bằng hoàn hảo với áp lực thủy tĩnh nội mạch đang đẩy từ bên trong ra. Nhờ có áp suất đối kháng này, huyết tương và dịch lỏng hoàn toàn không thể thoát ra ngoài khoang mô để gây sưng phù chân. Hơn thế nữa, thành của các tiểu động mạch và mao mạch ở chân hươu dày hơn bất kỳ loài động vật có vú nào từng được ghi nhận, kết hợp với các cơ vòng tiền mao mạch hoạt động như những chiếc van tiết lưu thông minh, chủ động ngắt dòng máu khi áp suất cục bộ vượt ngưỡng cho phép. Cỗ máy Tháp Cẩu Di Động có thể thong thả đứng cả ngày lẫn đêm dưới ánh mặt trời thiêu đốt mà bốn cẳng chân vẫn khô ráo, thanh thoát, chẳng hề bị phù nề, luôn trong tư thế sẵn sàng tung ra những cú đạp sấm sét.
```

### scene05 — CỖ MÁY ĐẬP PHÁ NẶNG HAI TẤN
*Thẻ chương:* CẶP SỪNG BỌC DA VÀ ĐÒN BẨY

*Badge:* `VŨ KHÍ CỔ BÚA ĐẬP TẤN` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene05_p0.wav` (900 ký tự) · mood `hao_hung`

```text
Đừng bao giờ để vẻ bề ngoài hiền lành, đôi mắt to tròn ngơ ngác và dáng điệu nhai lá cây chậm rãi của Tháp Cẩu Di Động ru ngủ bạn! Khi mùa giao phối tranh giành lãnh thổ bắt đầu hoặc khi con vật bị dồn vào bước đường cùng đối đầu với bầy dã thú săn mồi, chiếc cần cẩu dài hai mét thanh mảnh này sẽ ngay lập tức chuyển hóa thành một thứ vũ khí va đập hạng nặng với sức tàn phá kinh hoàng bậc nhất thảo nguyên châu Phi. Những con hươu đực không hề húc đầu trực diện như trâu rừng hay dùng móng guốc cào xé, mà chúng triển khai một tuyệt kỹ cận chiến tàn bạo mang tên khoa học là Necking, tức là màn giao đấu quăng cổ búa tạ. Chiếc cổ dài hai mét tuy chỉ gồm đúng bảy đốt sống cổ giống như loài người chúng ta, nhưng mỗi đốt sống lại dài tới gần ba mươi xăng-ti-mét, liên kết với nhau bằng các khớp cầu linh hoạt biến toàn bộ chiếc cổ thành một cánh tay đòn bẩy khổng lồ gia tốc cho phần đầu hồi chuyển.
```
**Part 1** → `audio/vs/scene05_p1.wav` (105 ký tự) · 🎭 cameo `be_con`

```text
Ủa các bác kỹ sư ơi, sừng của nó bọc da đặc xương, trán dày cộm như một khối đá tảng nguyên khối luôn hả?
```
**Part 2** → `audio/vs/scene05_p2.wav` (992 ký tự) · mood `don_dap`

```text
[laughter] Rất chuẩn xác bác thợ máy ơi, đó chính là đầu búa công phá đấy! [surprise-oh] Khi một con hươu đực trưởng thành gồng mình vung chiếc cổ dài hai mét hết biên độ vòng cung, phần đầu sọ của nó có thể xé toạc không khí và đạt vận tốc va đập lên tới hơn một trăm cây số một giờ. Hãy tưởng tượng một quả tạ đặc bằng xương và sừng nặng gần hai mươi ki-lô-gam được phóng đi với vận tốc đó và nện thẳng vào mạn sườn hoặc cuống họng của đối thủ! Lực xung kích sinh ra từ cú quất búa tạ này tương đương với hàng tấn động năng tập trung vào một điểm tiếp xúc nhỏ hẹp. Cú va chạm kinh hoàng ấy thừa sức bẻ gãy vụn các xương sườn, đâm thủng lá phổi, hoặc thậm chí làm gãy gập cột sống của đối thủ khiến nó gục ngã tức tưởi tại chỗ. Và chưa hết đâu nhé, nếu một con sư tử châu Phi đói khát dại dột tiếp cận từ phía sau trong góc chết, chiếc chân sau dài hai mét nặng như cột đình của hươu có thể tung ra một cú đạp hậu sấm sét, thừa đủ lực để làm nát vụn xương sọ của chúa sơn lâm trong chớp mắt!
```

### scene06 — BÀI HỌC TỪ THÁP CẨU TỰ NHIÊN
*Thẻ chương:* BÀI HỌC CÂN BẰNG ÁP LỰC SỐNG

*Badge:* `KẾT LUẬN` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene06_p0.wav` (866 ký tự) · mood `am_ap`

```text
Từ khối động cơ tim áp lực cao mười một ki-lô-gam, mạng lưới van xả chấn động kỳ diệu Rete Mirabile bảo vệ não bộ khỏi nguy cơ nổ mạch máu, bộ đồ nén sinh học ở cẳng chân truyền cảm hứng chế tạo trang phục phi hành gia cho NASA, cho đến hệ thống dây chằng gáy đàn hồi dày như cáp treo nâng đỡ chiếc cổ hai mét, Tháp Cẩu Di Động chính là một minh chứng hùng hồn nhất cho thấy thiên nhiên chính là vị tổng công trình sư vĩ đại và tinh tế nhất của vũ trụ. Để có thể vươn tầm mắt lên độ cao năm mét và thưởng thức những chồi non ngọt ngào nhất trên đỉnh ngọn cây keo gai mà chẳng có loài động vật ăn cỏ nào khác trên thảo nguyên có thể với tới, con vật đã dũng cảm chấp nhận sống chung với một môi trường áp suất khắc nghiệt gấp đôi bình thường, và nó đã tự trang bị cho mình những giải pháp cơ khí tối ưu nhất để biến áp lực hiểm nghèo thành lợi thế sinh tồn tuyệt đối.
```
**Part 1** → `audio/vs/scene06_p1.wav` (1097 ký tự) · mood `am_ap`

```text
Trong hành trình cuộc sống và sự nghiệp của mỗi chúng ta cũng vậy! Bất kỳ ai khao khát đứng ở một vị trí cao hơn, nhìn xa trông rộng hơn đám đông và chạm tới những đỉnh cao rực rỡ đều sẽ phải đối diện với những áp lực vô hình cực kỳ dữ dội và những thử thách khắc nghiệt đè nặng lên vai. Nhưng thay vì than vãn hay để áp lực cuộc sống đè bẹp ý chí, chúng ta hãy học hỏi cỗ máy Tháp Cẩu Di Động kiên cường: Tôi luyện cho mình một trái tim quả cảm đầy nhiệt huyết, xây dựng một cơ chế xả stress thông minh để cân bằng cảm xúc, và khoác lên mình một bản lĩnh vững vàng để vượt qua mọi bão giông thử thách! Các bạn cảm thấy ấn tượng và khâm phục bộ phận cơ khí nào nhất của chú hươu: Khối động cơ tim ba trăm mi-li-mét thủy ngân phi thường, hay mạng lưới xả áp Rete Mirabile tài tình chống nổ não? Hãy chia sẻ quan điểm thú vị của bạn ở phần bình luận bên dưới nhé! Còn trong tập tiếp theo, chúng ta sẽ cùng nhau bay tới những đầm lầy tiền sử rậm rạp ở châu Phi để giải mã một sát thủ đứng im như tượng đá hàng giờ liền với chiếc mỏ khổng lồ gõ đanh thép như súng máy liên thanh! Hãy cùng đón chờ nhé!
```

### Shorts → `audio/vs/shorts.wav`

```text
[surprise-oh] Bạn có biết một con Hươu Cao Cổ nặng hai tấn có thể bị nổ tung mạch máu não mỗi khi cúi đầu xuống đất uống nước không?! Hãy nhìn chiếc cổ dài hai mét của Tháp Cẩu Di Động lừng lững giữa thảo nguyên này xem! Để bơm máu đỏ ngược chiều trọng lực lên độ cao năm mét, quả tim của nó nặng tới mười một ki-lô-gam và tạo ra áp lực tâm thu ba trăm mi-li-mét thủy ngân, gấp đôi người khỏe mạnh nhất! Khi nó hạ đầu rơi tự do ba mét xuống vũng nước, áp suất dồn xuống não sẽ tăng vọt lên năm trăm mi-li-mét thủy ngân, đủ để làm vỡ toang mạch máu ngay tức khắc! Nhưng kỳ diệu thay, dưới đáy hộp sọ của nó có một mạng lưới mạch máu xốp mang tên Rete Mirabile cùng chuỗi van một chiều cơ học. Khi đầu chúi xuống, mạng lưới này lập tức phình to hấp thụ toàn bộ xung lực búa nước, triệt tiêu áp suất thừa! Chưa hết, cẳng chân của nó được bọc lớp da siêu căng như bộ đồ phi hành gia NASA, chống phù nề tuyệt đối! Đúng là một tuyệt tác cơ khí thủy lực đỉnh cao của tạo hóa!
```

**Whisper prompt:** `Hươu Cao Cổ, Giraffa camelopardalis`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| hai mươi tư trên hai mươi tư | 24/24 |
| mười một ki-lô-gam | 11kg |
| ba trăm mi-li-mét thủy ngân | 300 mmHg |
| năm trăm mi-li-mét thủy ngân | 500 mmHg |
| hai trăm mi-li-mét thủy ngân | 200 mmHg |
| một trăm hai mươi | 120 |
| một trăm mi-li-mét thủy ngân | 100 mmHg |
| hai mươi lăm mi-li-mét thủy ngân | 25 mmHg |
| hai mươi ki-lô-gam | 20kg |
| sáu mươi xăng-ti-mét | 60cm |
| bảy xăng-ti-mét | 7cm |
| ba mươi xăng-ti-mét | 30cm |
| hai mét | 2m |
| năm mét | 5m |
| hai tấn | 2 tấn |
| mười lít | 10 lít |
| năm mươi cây số | 50km/h |
| một trăm cây số | 100km/h |
| bốn mươi đến chín mươi nhịp | 40-90 nhịp |
| Re-te Mi-ra-bi-le | Rete Mirabile |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · BẢN VẼ THÁP CẨU 5 MÉT GIỮA SAVANNAH · 104.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.3 (7.3s) | L01 | Chào mừng toàn thể các kỹ sư cơ khí sinh học và các chuyên gia giải mã vũ khí tự nhiên đã quay trở lại với xưởng nghiên cứu tối mật của chúng tôi! |  | kỹ sư trưởng mặc đồ bảo hộ xưởng cơ khí, cầm cờ lê và bản vẽ đường ống thủy lực: kỹ sư trưởng mở cuộn bản vẽ tháp cẩu 5 mét trên bàn vẽ kỹ thuật |
| b02 | 00:07.3–00:18.5 (11.2s) | L02 | Hôm nay, ống nhòm viễn vọng của chúng ta sẽ hướng thẳng ra thảo nguyên châu Phi nắng cháy rực lửa, nơi một công trình kiến trúc cơ động cao nhất trên cạn đang lừng lững sải bước giữa đường chân trời. Hãy quan sát thật kỹ khối kết cấu |  | chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): chú hươu cao cổ bước đi uy nghiêm giữa thảo nguyên hoàng hôn như cỗ máy tháp cẩu di động |
| b03 | 00:18.5–00:29.4 (11.0s) | L03 | sinh học đồ sộ ấy! Một khối lượng lừng lững nặng tới gần 2 tấn, đỉnh đầu chót vót cách mặt đất hơn 5m, vươn cao ngạo nghễ như một tháp truyền hình di động giữa bầy thú ăn cỏ. Giới động vật học thông thường gọi nó bằng |  | chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): sơ đồ giải phẫu chịu lực của cơ thể 2 tấn trên 4 cẳng chân khẳng khiu |
| b04 | 00:29.4–00:40.1 (10.7s) | L04 | cái tên quen thuộc là Hươu Cao Cổ, nhưng trong mắt ban thiết kế công trình của chúng tôi, đây đích thị là cỗ máy Tháp Cẩu Di Động vĩ đại nhất từng được tự nhiên tạo tác. Bạn có bao giờ tự đặt câu hỏi dưới góc nhìn vật lý |  | chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động) kỹ sư trưởng mặc đồ bảo hộ xưởng cơ khí, cầm cờ lê và bản vẽ đường ống thủy lực: kỹ sư chỉ thước đo vào chiếc cổ 2m với nhãn kỹ thuật THÁP CẨU SAVANNAH |
| b05 | 00:40.1–00:52.7 (12.6s) | L05 | thuần túy: Làm thế nào để bơm một cột máu đỏ nặng trịch ngược chiều trọng lực trái đất lên độ cao 2m suốt 24/24 giờ không ngừng nghỉ mà không làm nổ tung động cơ? Báo cáo chỉ huy, nếu dùng máy bơm bình thường đẩy nước lên tầng năm, |  | chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): sơ đồ cắt dọc cổ cho thấy cột nước màu đỏ rực leo dốc 2m ngược chiều trọng lực |
| b06 | 00:52.7–01:05.6 (12.9s) | L06 | ống nhựa sẽ nổ tung vì áp lực quá tải! Nhận định hoàn toàn chuẩn xác không cần chỉnh cô trợ lý kỹ thuật ạ! Định luật thủy tĩnh cơ bản quy định rằng cứ mỗi mét chất lỏng dâng cao, áp suất đáy sẽ tăng lên dữ dội. Nếu |  | cô trợ lý kỹ thuật đeo kính bảo hộ cầm bảng kẹp tài liệu ghi chép áp suất: cô trợ lý cầm đường ống vỡ tung tóe vì áp lực quá tải cảnh báo nguy cơ nổ ống |
| b07 | 01:05.6–01:16.8 (11.2s) | L07 | cơ thể một người bình thường chúng ta bị kéo giãn chiếc cổ ra 2m như thế này, quả tim con người sẽ bất lực hoàn toàn, không thể bơm nổi một giọt máu nào lên tới đỉnh đầu, và toàn bộ hệ thần kinh trung ương sẽ chết |  | chú ngơ ngác gãi đầu hoảng hốt trước đồng hồ đo áp suất: chú ngơ ngác hoa mắt chóng mặt khi tưởng tượng cổ mình dài 2m thiếu nước màu não |
| b08 | 01:16.8–01:28.4 (11.6s) | L08 | đói vì cạn kiệt oxy chỉ sau đúng ba giây ngắn ngủi. Ấy vậy mà Tháp Cẩu Di Động không những không hề choáng váng, nó còn thong dong vươn chiếc lưỡi dài nửa mét màu tím đen để tước từng chiếc lá gai nhọn hoắt của cây keo bao báp, |  | chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): cận cảnh chiếc lưỡi dài 50cm màu tím đen tước lá gai keo nhọn hoắt không hề hấn |
| b09 | 01:28.4–01:33.9 (5.5s) | L09 | thậm chí khi cần nó có thể bứt tốc phi nước đại với vận tốc 50km/h một giờ. Mọi linh kiện |  | kỹ sư trưởng mặc đồ bảo hộ xưởng cơ khí, cầm cờ lê và bản vẽ đường ống thủy lực chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): kỹ sư vặn van khóa áp suất mở toang khoang động cơ tim phổi của hươu |
| b10 | 01:33.9–01:44.7 (10.8s) | L09b | bên trong con vật này đều được tôi luyện với dung sai cực hạn, vượt xa mọi tiêu chuẩn công nghiệp cơ khí nặng hiện đại nhất. Ngay bây giờ, hãy cầm cờ-lê tháo bu-lông và mở tung bản vẽ khoang động cơ chính ra xem! |  | HÌNH L09b (16:9 ngang, bản vẽ kỹ thuật đường ống công nghiệp và thủy lực (Industrial Piping Schematic & Hydraulic Blueprint), nền xanh đậm blueprint kỹ thuật #0C1824, các đường nét sơ đồ phát sáng dạ quang cyan #00F0FF và cam neon #FF8800, bản vẽ chi tiết các van, ống dẫn, đồng hồ đo áp suất, KHÔNG chữ, không logo). Minh họa sơ đồ chi tiết các chi tiết cơ khí và vật liệu chịu lực cao được tôi luyện với dung sai cực h |

### scene02 · ĐỘNG CƠ V8 BƠM MÁU CAO ÁP · 133.9s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:12.2 (12.2s) | L10 | Để nâng được một cột chất lỏng nhớt có tỷ trọng nặng hơn nước lên độ cao thẳng đứng 2m ngược chiều gia tốc trọng trường, yêu cầu tiên quyết đầu tiên trên bản vẽ chính là một khối động cơ bơm áp lực siêu cường. Trái |  | mô hình quả tim thép 11kg với đồng hồ đo áp suất 300 mmHg: mô hình quả tim 11kg khổng lồ đập thình thịch với các ống dẫn áp lực cao |
| b02 | 00:12.2–00:19.7 (7.5s) | L11 | tim của Tháp Cẩu Di Động hoàn toàn không phải dạng vừa, nó là một khối cơ bắp rắn rỏi nặng tới 11kg, dài hơn 60cm và sở | **11 kg** · Động cơ tim siêu áp · L/360 · [0.35, 0.5] | mô hình quả tim thép 11kg với đồng hồ đo áp suất 300 mmHg kỹ sư trưởng mặc đồ bảo hộ xưởng cơ khí, cầm cờ lê và bản vẽ đường ống thủy lực: kỹ sư đo kích thước quả tim dài 60cm nặng 11kg so với tim người tí hon |
| b03 | 00:19.7–00:27.8 (8.1s) | L11b | hữu thể tích buồng chứa cực lớn, có khả năng luân chuyển hàng chục lít máu mỗi phút. Đặc biệt nhất chính là thành tâm thất trái của nó, nơi trực tiếp tạo ra lực |  | HÌNH L11b (16:9 ngang, bản vẽ kỹ thuật đường ống công nghiệp và thủy lực (Industrial Piping Schematic & Hydraulic Blueprint), nền xanh đậm blueprint kỹ thuật #0C1824, các đường nét sơ đồ phát sáng dạ quang cyan #00F0FF và cam neon #FF8800, bản vẽ chi tiết các van, ống dẫn, đồng hồ đo áp suất, KHÔNG chữ, không logo). Mặt cắt buồng tim khổng lồ dài hơn 60cm với thể tích buồng chứa cực lớn và van tim cơ học áp lực cao. |
| b04 | 00:27.8–00:34.6 (6.8s) | L12 | đẩy lên động mạch chủ, dày tới 7cm, đanh chắc và kiên cố như một tấm lốp xe tải bọc thép chuyên dụng. Khi cỗ máy sinh | **300 mmHg** · Áp lực bơm cực đại · R/320 · [0.8, 0.4] | mô hình quả tim thép 11kg với đồng hồ đo áp suất 300 mmHg: mặt cắt thành tâm thất trái dày 7cm đanh chắc như lốp xe tải bọc thép |
| b05 | 00:34.6–00:43.4 (8.8s) | L12b | học này thực hiện một chu kỳ co bóp toàn phần, nó tạo ra một áp lực tâm thu khủng khiếp lên tới 300 mmHg, tức là gấp đôi mức huyết áp đỉnh cao của |  | HÌNH L12b (16:9 ngang, bản vẽ kỹ thuật đường ống công nghiệp và thủy lực (Industrial Piping Schematic & Hydraulic Blueprint), nền xanh đậm blueprint kỹ thuật #0C1824, các đường nét sơ đồ phát sáng dạ quang cyan #00F0FF và cam neon #FF8800, bản vẽ chi tiết các van, ống dẫn, đồng hồ đo áp suất, KHÔNG chữ, không logo). Sơ đồ chu kỳ co bóp tâm thu của khối cơ tim tạo áp lực tống máu 300 mmHg vào động mạch chủ vươn cao. |
| b06 | 00:43.4–00:56.5 (13.0s) | L13 | một vận động viên điền kinh Olympic khỏe mạnh nhất! Tại sao hệ thống này lại bắt buộc phải vận hành ở mức áp lực bạo lực đến như vậy? Bởi vì định luật thủy tĩnh không hề có sự nhân nhượng cho bất kỳ sinh vật nào! Dòng máu đỏ xuất phát từ van tim ở lồng ngực phải leo dốc thẳng đứng |  | mô hình quả tim thép 11kg với đồng hồ đo áp suất 300 mmHg: đồng hồ đo áp suất kim loại chỉ vạch đỏ 300 mmHg xả hơi nước cảnh báo |
| b07 | 00:56.5–01:02.5 (6.0s) | L14 | vượt qua lực hút trái đất trên quãng đường dài 2m để chạm tới vỏ não. Cứ mỗi 30cm chiều cao tăng thêm, |  | chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): sơ đồ sụt giảm áp suất thủy tĩnh: từ 300 mmHg ở ngực giảm dần còn 100 mmHg ở não |
| b08 | 01:02.5–01:11.9 (9.5s) | L14b | áp suất thủy tĩnh sẽ sụt giảm khoảng 25 mmHg. Nếu như áp lực bơm tim của hươu chỉ duy trì ở mức 120 như con người chúng ta, thì khi dòng máu leo tới nửa đoạn cổ, áp |  | HÌNH L14b (16:9 ngang, bản vẽ kỹ thuật đường ống công nghiệp và thủy lực (Industrial Piping Schematic & Hydraulic Blueprint), nền xanh đậm blueprint kỹ thuật #0C1824, các đường nét sơ đồ phát sáng dạ quang cyan #00F0FF và cam neon #FF8800, bản vẽ chi tiết các van, ống dẫn, đồng hồ đo áp suất, KHÔNG chữ, không logo). Đồ thị cột thủy ngân và sơ đồ sụt giảm áp suất thủy tĩnh theo từng mét độ cao của chiếc cổ dài. |
| b09 | 01:11.9–01:25.1 (13.2s) | L15 | suất đẩy đã giảm về mức số không, khiến máu ngừng chảy và chảy ngược trở lại, dẫn đến tình trạng thiếu máu não tức thì. Nhờ việc duy trì công suất cực đại 300 mmHg ngay tại cửa xả của tim, khi dòng máu chạm tới đỉnh đầu sau hành trình leo dốc gian nan, áp suất còn lại ở não bộ |  | chú ngơ ngác gãi đầu hoảng hốt trước đồng hồ đo áp suất chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): sơ đồ so sánh huyết áp người 120 mmHg bị tắc nghẽn giữa chừng ở độ cao 1m |
| b10 | 01:25.1–01:39.1 (14.0s) | L16 | vẫn duy trì hoàn hảo ở mức 100 mmHg, vừa vặn tuyệt đối để hệ thần kinh trung ương xử lý tín hiệu sắc bén như dao cạo. Nhưng các kỹ sư cơ khí hãy đặc biệt chú ý đến một bí mật thiết kế đắt giá này! Một khối động cơ tim áp suất cao như vậy nếu đập dồn dập liên tục |  | chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): não bộ hươu trên đỉnh đầu sáng rực nhận dòng nước màu 100 mmHg êm ái hoàn hảo |
| b11 | 01:39.1–01:46.2 (7.1s) | L17 | thì chẳng mấy chốc sẽ bị nổ van hoặc suy tim sớm. Thiên nhiên đã lập trình cho trái tim của Tháp Cẩu Di Động một nhịp đập cực kỳ điềm tĩnh, |  | mô hình quả tim thép 11kg với đồng hồ đo áp suất 300 mmHg: biểu đồ sóng điện tim nhịp đập chậm rãi uy nghi 40-90 nhịp mỗi phút |
| b12 | 01:46.2–01:54.2 (8.0s) | L17b | dao động từ 40-90 nhịp mỗi phút. Mỗi nhịp co bóp tống đi một thể tích máu khổng lồ vào gốc động mạch chủ. Thành của động mạch chủ ở hươu |  | HÌNH L17b (16:9 ngang, bản vẽ kỹ thuật đường ống công nghiệp và thủy lực (Industrial Piping Schematic & Hydraulic Blueprint), nền xanh đậm blueprint kỹ thuật #0C1824, các đường nét sơ đồ phát sáng dạ quang cyan #00F0FF và cam neon #FF8800, bản vẽ chi tiết các van, ống dẫn, đồng hồ đo áp suất, KHÔNG chữ, không logo). Đồng hồ đo nhịp đập sinh học điềm tĩnh 40-90 nhịp mỗi phút điều phối dòng chảy thủy lực ổn định. |
| b13 | 01:54.2–02:02.0 (7.8s) | L18 | được gia cố bằng nhiều lớp sợi elastin siêu đàn hồi, hoạt động giống hệt như một bình tích áp thủy lực Windkessel trong kỹ thuật cơ khí đường ống. |  | chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động) kỹ sư trưởng mặc đồ bảo hộ xưởng cơ khí, cầm cờ lê và bản vẽ đường ống thủy lực: kỹ sư kiểm tra buồng giãn nở đàn hồi Windkessel của động mạch chủ duy trì dòng chảy liên tục |
| b14 | 02:02.0–02:13.9 (11.9s) | L18b | Bình tích áp này giãn nở để hấp thụ chấn động từ mỗi cú nén cao áp cực mạnh của tim, rồi co lại nhịp nhàng để duy trì dòng chảy liên tục và êm ái, biến dòng máu giật cục thành một dòng chảy ổn định tuần hoàn khắp cơ thể đồ sộ 5m. |  | HÌNH L18b (16:9 ngang, bản vẽ kỹ thuật đường ống công nghiệp và thủy lực (Industrial Piping Schematic & Hydraulic Blueprint), nền xanh đậm blueprint kỹ thuật #0C1824, các đường nét sơ đồ phát sáng dạ quang cyan #00F0FF và cam neon #FF8800, bản vẽ chi tiết các van, ống dẫn, đồng hồ đo áp suất, KHÔNG chữ, không logo). Cụm bình tích áp Windkessel giãn nở đàn hồi hấp thụ chấn động áp lực máu dọc động mạch chủ. |

### scene03 · HỆ THỐNG XẢ ÁP RETE MIRABILE · 143.1s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:11.9 (11.9s) | L19 | Bây giờ mới thực sự là bài kiểm tra ứng suất kinh hoàng nhất trong toàn bộ quy trình vận hành của Tháp Cẩu Di Động. Mặc dù sở hữu chiều cao 5m để với tới những cành cây cao chót vót, nhưng vũng nước uống duy nhất giữa sa mạc lại nằm sát sàn sạt dưới |  | chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): hươu xoạc rộng hai chân trước cúi chiếc cổ 2m rơi tự do xuống vũng nước |
| b02 | 00:11.9–00:18.6 (6.7s) | L20 | mặt đất. Để uống được nước, con vật không thể quỳ gối quá lâu vì dễ bị thú săn mồi phục kích. Nó buộc phải xoạc rộng hai chân trước sang hai bên |  | chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): mô phỏng áp suất dồn xuống đầu vọt lên 500 mmHg với biểu tượng cảnh báo nguy hiểm |
| b03 | 00:18.6–00:27.5 (8.9s) | L20b | rồi hạ thấp phần đầu xuống trong một cú rơi tự do sâu tới gần ba mét. Các bạn hãy làm một phép tính vật lý đơn giản: Một hệ thống ống dẫn đang chịu áp suất 300 mmHg, nay |  | HÌNH L20b (16:9 ngang, bản vẽ kỹ thuật đường ống công nghiệp và thủy lực (Industrial Piping Schematic & Hydraulic Blueprint), nền xanh đậm blueprint kỹ thuật #0C1824, các đường nét sơ đồ phát sáng dạ quang cyan #00F0FF và cam neon #FF8800, bản vẽ chi tiết các van, ống dẫn, đồng hồ đo áp suất, KHÔNG chữ, không logo). Tư thế hươu cao cổ xoạc rộng hai chân trước hạ thấp đầu xuống gần mặt nước uống nước. |
| b04 | 00:27.5–00:34.1 (6.7s) | L21 | lại được cộng dồn thêm toàn bộ trọng lượng của cột máu cao 2m đổ dồn thẳng đứng từ trên ngực xuống đáy hộp sọ theo chiều gia tốc trọng trường. | **500 mmHg** · Áp lực dồn đỉnh sọ · R/320 · [0.8, 0.4] | chú ngơ ngác gãi đầu hoảng hốt trước đồng hồ đo áp suất: chú ngơ ngác ôm đầu hoảng hốt sợ đầu hươu nổ tung như quả bóng cao su bơm căng |
| b05 | 00:34.1–00:43.1 (8.9s) | L21b | Áp lực máu tại khoang não lúc này sẽ lập tức tăng vọt lên tới gần 500 mmHg! Ở bất kỳ loài động vật có vú nào khác, mức áp suất bạo tàn này thừa sức phá hủy toàn bộ mạng |  | HÌNH L21b (16:9 ngang, bản vẽ kỹ thuật đường ống công nghiệp và thủy lực (Industrial Piping Schematic & Hydraulic Blueprint), nền xanh đậm blueprint kỹ thuật #0C1824, các đường nét sơ đồ phát sáng dạ quang cyan #00F0FF và cam neon #FF8800, bản vẽ chi tiết các van, ống dẫn, đồng hồ đo áp suất, KHÔNG chữ, không logo). Mô phỏng dòng thủy lực tăng áp đột ngột do gia tốc trọng trường khi đầu dốc ngược xuống đất. |
| b06 | 00:43.1–00:48.9 (5.9s) | L22 | lưới mao mạch não mỏng manh, gây xuất huyết ồ ạt và tử vong tại chỗ chỉ trong tích tắc! Khoan đã thầy ơi, vậy tại sao đầu |  | sơ đồ mạng lưới vi mạch xốp giảm áp búa nước dưới đáy sọ kỹ sư trưởng mặc đồ bảo hộ xưởng cơ khí, cầm cờ lê và bản vẽ đường ống thủy lực: kỹ sư soi kính lúp vào mạng lưới Rete Mirabile dưới đáy sọ hươu |
| b07 | 00:48.9–01:00.1 (11.2s) | L22b | của nó không phát nổ tung toé như một quả bóng bay bằng cao su bị bơm quá áp suất? Một câu hỏi vô cùng thực tế và đáng giá triệu đô đấy người anh em ngơ ngác! Bí mật sống còn nằm ở một cụm |  | HÌNH L22b (16:9 ngang, bản vẽ kỹ thuật đường ống công nghiệp và thủy lực (Industrial Piping Schematic & Hydraulic Blueprint), nền xanh đậm blueprint kỹ thuật #0C1824, các đường nét sơ đồ phát sáng dạ quang cyan #00F0FF và cam neon #FF8800, bản vẽ chi tiết các van, ống dẫn, đồng hồ đo áp suất, KHÔNG chữ, không logo). Sơ đồ bảo vệ chống nổ vỡ mạch máu não trước áp suất thủy tĩnh khổng lồ 500 mmHg. |
| b08 | 01:00.1–01:07.7 (7.6s) | L23 | chi tiết cơ khí sinh học tối mật được giấu kín ngay dưới đáy hộp sọ của hươu, mang tên khoa học là Rete Mirabile, tiếng Latin có nghĩa | **RETE** · Ma trận xả áp não · L/340 · [0.4, 0.45] | sơ đồ mạng lưới vi mạch xốp giảm áp búa nước dưới đáy sọ: kính hiển vi phóng đại ma trận vi mạch xốp Rete Mirabile phình to hấp thụ xung lực búa nước |
| b09 | 01:07.7–01:17.7 (9.9s) | L23b | là Mạng Lưới Kỳ Diệu. Đây là một ma trận chằng chịt gồm hàng ngàn mạch máu nhỏ li ti, lồng ghép đan xen vào nhau giống hệt như một miếng bọt biển hấp thụ lực va đập thủy tĩnh. Khi Tháp Cẩu |  | HÌNH L23b (16:9 ngang, bản vẽ kỹ thuật đường ống công nghiệp và thủy lực (Industrial Piping Schematic & Hydraulic Blueprint), nền xanh đậm blueprint kỹ thuật #0C1824, các đường nét sơ đồ phát sáng dạ quang cyan #00F0FF và cam neon #FF8800, bản vẽ chi tiết các van, ống dẫn, đồng hồ đo áp suất, KHÔNG chữ, không logo). Cận cảnh cấu tạo mạng lưới mạch máu xốp Rete Mirabile đan xen dày đặc như bọt biển dưới nền sọ. |
| b10 | 01:17.7–01:24.5 (6.8s) | L24 | Di Động hạ thấp đầu xuống vũng nước, lượng máu áp suất cao ồ ạt đổ xuống sẽ lập tức bị mạng lưới này phân tán vào vô số nhánh rẽ nhỏ li ti. |  | chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): mặt cắt tĩnh mạch cổ 2m với chuỗi van một chiều cơ học sập chặt khóa dòng nước màu đen |
| b11 | 01:24.5–01:34.0 (9.5s) | L24b | Thiết diện tổng của dòng chảy tăng vọt làm vận tốc dòng máu giảm xuống đột ngột, triệt tiêu hoàn toàn xung lực búa nước va đập trước khi những giọt máu có thể chạm tới các tế bào thần |  | HÌNH L24b (16:9 ngang, bản vẽ kỹ thuật đường ống công nghiệp và thủy lực (Industrial Piping Schematic & Hydraulic Blueprint), nền xanh đậm blueprint kỹ thuật #0C1824, các đường nét sơ đồ phát sáng dạ quang cyan #00F0FF và cam neon #FF8800, bản vẽ chi tiết các van, ống dẫn, đồng hồ đo áp suất, KHÔNG chữ, không logo). Sơ đồ thiết diện tổng của dòng chảy tăng vọt gấp trăm lần làm giảm vận tốc và áp lực máu. |
| b12 | 01:34.0–01:39.5 (5.5s) | L25 | kinh nhạy cảm. Chưa dừng lại ở đó đâu nhé! Dọc theo suốt chiều dài 2m của tĩnh mạch cổ là cả một |  | chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động) sư tử châu phi bờm rậm hoảng hốt né đòn đạp hậu của hươu: hươu giật phắt đầu vụt cao 5m trong 1 giây khi sư tử phục kích trong bụi rậm |
| b13 | 01:39.5–01:49.3 (9.8s) | L25b | hệ thống các van một chiều cơ học đóng mở tự động cực kỳ tinh xảo. Ngay khoảnh khắc chiếc đầu hạ thấp quá tim, các van tĩnh mạch một chiều này lập tức sập chặt lại, ngăn chặn tuyệt đối tình trạng máu đen ứ đọng từ khoang ngực |  | HÌNH L25b (16:9 ngang, bản vẽ kỹ thuật đường ống công nghiệp và thủy lực (Industrial Piping Schematic & Hydraulic Blueprint), nền xanh đậm blueprint kỹ thuật #0C1824, các đường nét sơ đồ phát sáng dạ quang cyan #00F0FF và cam neon #FF8800, bản vẽ chi tiết các van, ống dẫn, đồng hồ đo áp suất, KHÔNG chữ, không logo). Cận cảnh van một chiều cơ học tự động khép chặt chặn đứng dòng máu dội ngược về tĩnh mạch cổ. |
| b14 | 01:49.3–02:04.0 (14.7s) | L26 | chảy ngược trở lại đầu gây tăng áp nội sọ. Và điều kỳ diệu nhất diễn ra khi con vật bất ngờ phát hiện thấy một con sư tử đang rình rập trong bụi rậm! Nó lập tức giật phắt chiếc đầu nặng nề cao vụt lên trời ở độ cao 5m chỉ trong vòng chưa đầy một giây. Một cú giật ngược đột ngột như thế bình thường sẽ làm toàn bộ |  | sơ đồ mạng lưới vi mạch xốp giảm áp búa nước dưới đáy sọ chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): mạng lưới Rete Mirabile xả lượng nước màu dự trữ nuôi não giúp hươu tỉnh táo phóng chạy |
| b15 | 02:04.0–02:10.8 (6.8s) | L27 | máu tụt dốc về tim, khiến não bộ rơi vào trạng thái thiếu oxy cục bộ và gây ngất xỉu ngay tức thì. Nhưng mạng lưới Rete Mirabile lại đóng |  | kỹ sư trưởng mặc đồ bảo hộ xưởng cơ khí, cầm cờ lê và bản vẽ đường ống thủy lực: kỹ sư giơ ngón tay cái tán thưởng cơ chế giảm chấn thủy lực hai chiều hoàn mỹ |
| b16 | 02:10.8–02:23.1 (12.3s) | L27b | vai trò như một kho dự trữ máu khẩn cấp, từ từ xả lượng máu tích trữ ra để nuôi dưỡng não trong lúc tim điều chỉnh lại nhịp đập, giúp con vật giữ vững sự tỉnh táo hoàn toàn để phóng nước đại tẩu thoát. Đó là một cơ chế giảm chấn thủy lực hai chiều hoàn mỹ đến từng phân tử! |  | HÌNH L27b (16:9 ngang, bản vẽ kỹ thuật đường ống công nghiệp và thủy lực (Industrial Piping Schematic & Hydraulic Blueprint), nền xanh đậm blueprint kỹ thuật #0C1824, các đường nét sơ đồ phát sáng dạ quang cyan #00F0FF và cam neon #FF8800, bản vẽ chi tiết các van, ống dẫn, đồng hồ đo áp suất, KHÔNG chữ, không logo). Kho dự trữ máu khẩn cấp nhả từ từ lượng máu đã lọc nuôi não khi hươu ngẩng đầu vút lên cao. |

### scene04 · BỘ ĐỒ PHI HÀNH GIA Ở CẲNG CHÂN · 124.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:09.4 (9.4s) | L28 | Giải quyết xong bài toán áp suất phức tạp ở phần đỉnh tháp, bây giờ mời toàn thể ban kỹ sư cùng chuyển ống kính xuống kiểm tra phần gầm của cỗ máy Tháp Cẩu Di Động. Với một sinh vật có tầm vóc khổng lồ |  | kỹ sư trưởng mặc đồ bảo hộ xưởng cơ khí, cầm cờ lê và bản vẽ đường ống thủy lực chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): kỹ sư rọi đèn pin vào đôi chân khẳng khiu chịu áp lực thủy tĩnh khổng lồ |
| b02 | 00:09.4–00:22.2 (12.8s) | L29 | đứng thẳng trên bốn chiếc chân khẳng khiu cao tới gần 2m, áp lực thủy tĩnh ở cẳng chân dưới là một cơn ác mộng kỹ thuật không kém phần nan giải. Trọng lực đè nặng toàn bộ thể tích máu trong cơ thể dồn xuống các mao mạch ở bàn chân, tạo ra một áp suất nội mạch thường xuyên vượt |  | chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): sơ đồ cột nước màu dồn xuống bàn chân với áp lực vượt ngưỡng 200 mmHg |
| b03 | 00:22.2–00:36.2 (14.0s) | L30 | ngưỡng 200 mmHg. Để các bạn dễ hình dung, ở cơ thể con người chúng ta, chỉ cần phải đứng im bất động trong vài giờ liên tục, máu sẽ dồn xuống bàn chân làm tăng áp suất mao mạch, khiến huyết tương rò rỉ vào khoang gian bào gây phù nề mắt cá chân, suy giãn tĩnh mạch hoặc thậm chí |  | chú ngơ ngác gãi đầu hoảng hốt trước đồng hồ đo áp suất: chú ngơ ngác ôm mắt cá chân sưng phù đau đớn vì đứng lâu tụ nước màu |
| b04 | 00:36.2–00:50.2 (14.0s) | L31 | vỡ mao mạch tạo thành các vết xuất huyết bầm tím dưới da. Vậy thì điều kỳ diệu gì đã bảo vệ bốn chiếc chân khẳng khiu như những que tăm của hươu không bị nứt toác và phù nề sau hàng chục năm đứng liên tục giữa thảo nguyên? Câu trả lời là thiên nhiên đã trang bị cho nó một |  | chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): cận cảnh cẳng chân hươu khô ráo thanh thoát không hề có một vết phù nề |
| b05 | 00:50.2–01:03.6 (13.5s) | L32 | bộ tất áp lực sinh học hoàn hảo bậc nhất thế giới! Đây chính là cấu trúc cơ học mà sau này các nhà khoa học của cơ quan hàng không vũ trụ NASA đã phải cất công nghiên cứu tỉ mỉ để chế tạo ra bộ đồ kháng áp G-suit dành cho phi công tiêm kích siêu âm và các | **G-SUIT** · Đồ nén chân NASA · R/350 · [0.8, 0.5] | kỹ sư trưởng mặc đồ bảo hộ xưởng cơ khí, cầm cờ lê và bản vẽ đường ống thủy lực cô trợ lý kỹ thuật đeo kính bảo hộ cầm bảng kẹp tài liệu ghi chép áp suất: cô trợ lý giới thiệu bộ đồ phi hành gia G-suit NASA lấy cảm hứng từ chân hươu |
| b06 | 01:03.6–01:16.9 (13.2s) | L33 | phi hành gia khi chịu gia tốc phóng cực đại. Bao bọc lấy toàn bộ phần cẳng chân của hươu là một lớp da dày cộm, cứng cáp và có độ đàn hồi cực kỳ thấp, ôm sát rạt lấy cơ thể giống như một lớp vỏ bọc bằng sợi carbon composite. Ngay bên dưới lớp da dày ấy là một màng cân |  | chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): mặt cắt lớp da dày và bao cân cơ siêu căng bó chặt như sợi carbon composite |
| b07 | 01:16.9–01:30.9 (14.0s) | L34 | cơ dày đặc và rắn chắc, bọc kín lấy từng thớ cơ và mạch máu như một chiếc băng cuốn y tế chuyên dụng được siết chặt tối đa. Lớp vỏ bọc cơ học siêu bền này tạo ra một lực ép ngoại sinh cực mạnh tác động ngược trở lại thành mạch, cân bằng hoàn hảo với áp lực thủy |  | chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): mũi tên áp lực ngoại sinh ép ngược lại triệt tiêu áp lực thủy tĩnh nội mạch |
| b08 | 01:30.9–01:45.2 (14.3s) | L35 | tĩnh nội mạch đang đẩy từ bên trong ra. Nhờ có áp suất đối kháng này, huyết tương và dịch lỏng hoàn toàn không thể thoát ra ngoài khoang mô để gây sưng phù chân. Hơn thế nữa, thành của các tiểu động mạch và mao mạch ở chân hươu dày hơn bất kỳ loài động vật có vú nào từng được ghi |  | chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): cơ vòng tiền mao mạch co thắt như van tiết lưu thông minh điều hòa lưu lượng nước màu |
| b09 | 01:45.2–01:55.0 (9.8s) | L36 | nhận, kết hợp với các cơ vòng tiền mao mạch hoạt động như những chiếc van tiết lưu thông minh, chủ động ngắt dòng máu khi áp suất cục bộ vượt ngưỡng cho phép. Cỗ máy Tháp Cẩu Di Động |  | chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): hươu đứng vững chãi giữa nắng gắt sa mạc sẵn sàng phi nước đại 50km/h |
| b10 | 01:55.0–02:04.4 (9.5s) | L36b | có thể thong thả đứng cả ngày lẫn đêm dưới ánh mặt trời thiêu đốt mà bốn cẳng chân vẫn khô ráo, thanh thoát, chẳng hề bị phù nề, luôn trong tư thế sẵn sàng tung ra những cú đạp sấm sét. |  | HÌNH L36b (16:9 ngang, bản vẽ kỹ thuật đường ống công nghiệp và thủy lực (Industrial Piping Schematic & Hydraulic Blueprint), nền xanh đậm blueprint kỹ thuật #0C1824, các đường nét sơ đồ phát sáng dạ quang cyan #00F0FF và cam neon #FF8800, bản vẽ chi tiết các van, ống dẫn, đồng hồ đo áp suất, KHÔNG chữ, không logo). Cỗ máy Tháp Cẩu Di Động uy nghi vươn cao giữa thảo nguyên savan với hệ thống cảm biến áp suất toàn diệ |

### scene05 · CỖ MÁY ĐẬP PHÁ NẶNG HAI TẤN · 98.0s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:07.5 (7.5s) | L37 | Đừng bao giờ để vẻ bề ngoài hiền lành, đôi mắt to tròn ngơ ngác và dáng điệu nhai lá cây chậm rãi của Tháp Cẩu Di Động ru ngủ bạn! Khi |  | chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): ánh mắt hươu biến chuyển sắc lạnh đầy sát khí bước vào trận chiến lãnh thổ |
| b02 | 00:07.5–00:18.2 (10.7s) | L38 | mùa giao phối tranh giành lãnh thổ bắt đầu hoặc khi con vật bị dồn vào bước đường cùng đối đầu với bầy dã thú săn mồi, chiếc cần cẩu dài 2m thanh mảnh này sẽ ngay lập tức chuyển hóa thành một thứ vũ khí va đập |  | chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): hai con hươu đực giao đấu quăng cổ búa tạ Necking với vòng cung khổng lồ |
| b03 | 00:18.2–00:29.5 (11.3s) | L39 | hạng nặng với sức tàn phá kinh hoàng bậc nhất thảo nguyên châu Phi. Những con hươu đực không hề húc đầu trực diện như trâu rừng hay dùng móng guốc cào xé, mà chúng triển khai một tuyệt kỹ cận chiến tàn bạo mang tên khoa |  | chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động) kỹ sư trưởng mặc đồ bảo hộ xưởng cơ khí, cầm cờ lê và bản vẽ đường ống thủy lực: kỹ sư giơ bản vẽ 7 đốt sống cổ khổng lồ dài 30cm khớp nối linh hoạt |
| b04 | 00:29.5–00:42.1 (12.6s) | L40 | học là Necking, tức là màn giao đấu quăng cổ búa tạ. Chiếc cổ dài 2m tuy chỉ gồm đúng bảy đốt sống cổ giống như loài người chúng ta, nhưng mỗi đốt sống lại dài tới gần 30cm, liên kết với nhau bằng các khớp cầu linh hoạt |  | bé con đội mũ safari đeo ba lô tò mò chỉ tay hỏi: bé con đội mũ safari nhòm ống nhòm thấy cặp sừng bọc da đặc xương và xương trán gồ ghề |
| b05 | 00:42.1–00:53.9 (11.8s) | L41 | biến toàn bộ chiếc cổ thành một cánh tay đòn bẩy khổng lồ gia tốc cho phần đầu hồi chuyển. Ủa các bác kỹ sư ơi, sừng của nó bọc da đặc xương, trán dày cộm như một khối đá tảng nguyên khối luôn hả? Rất chuẩn |  | chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): đồ họa vệt sáng chuyển động cho thấy đầu sọ hươu quất với vận tốc 100km/h xé gió |
| b06 | 00:53.9–01:04.2 (10.3s) | L42 | xác bác thợ máy ơi, đó chính là đầu búa công phá đấy! Khi một con hươu đực trưởng thành gồng mình vung chiếc cổ dài 2m hết biên độ vòng cung, phần đầu sọ của nó có thể xé toạc không khí và đạt vận tốc va đập |  | chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): hình ảnh nổ tung động năng: quả tạ xương 20kg nện xuống mạn sườn với lực hàng tấn |
| b07 | 01:04.2–01:14.6 (10.3s) | L43 | lên tới hơn 100km/h một giờ. Hãy tưởng tượng một quả tạ đặc bằng xương và sừng nặng gần 20kg được phóng đi với vận tốc đó và nện thẳng vào mạn sườn hoặc cuống họng của đối thủ! Lực xung kích sinh ra từ cú quất búa | **100 km/h** · Vận tốc búa sừng · R/320 · [0.8, 0.4] | chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): tia X quét qua khung xương đối thủ gãy rạn trước uy lực của cú quật búa tạ |
| b08 | 01:14.6–01:24.4 (9.9s) | L44 | tạ này tương đương với hàng tấn động năng tập trung vào một điểm tiếp xúc nhỏ hẹp. Cú va chạm kinh hoàng ấy thừa sức bẻ gãy vụn các xương sườn, đâm thủng lá phổi, hoặc thậm chí làm gãy gập cột sống của đối thủ |  | chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động) sư tử châu phi bờm rậm hoảng hốt né đòn đạp hậu của hươu: hươu tung cú đạp hậu sấm sét bằng chiếc chân sau nặng như cột đình hất văng sư tử |
| b09 | 01:24.4–01:38.0 (13.6s) | L45 | khiến nó gục ngã tức tưởi tại chỗ. Và chưa hết đâu nhé, nếu một con sư tử châu Phi đói khát dại dột tiếp cận từ phía sau trong góc chết, chiếc chân sau dài 2m nặng như cột đình của hươu có thể tung ra một cú đạp hậu sấm sét, thừa đủ lực để làm nát vụn xương sọ của chúa sơn lâm trong chớp mắt! |  | kỹ sư trưởng mặc đồ bảo hộ xưởng cơ khí, cầm cờ lê và bản vẽ đường ống thủy lực: kỹ sư đóng dấu đỏ ĐÒN BẨY HẠNG NẶNG vào hồ sơ năng lực chiến đấu của hươu |

### scene06 · BÀI HỌC TỪ THÁP CẨU TỰ NHIÊN · 95.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:08.8 (8.8s) | L46 | Từ khối động cơ tim áp lực cao 11kg, mạng lưới van xả chấn động kỳ diệu Rete Mirabile bảo vệ não bộ khỏi nguy cơ nổ mạch máu, bộ đồ nén sinh học ở cẳng chân |  | chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động) mô hình quả tim thép 11kg với đồng hồ đo áp suất 300 mmHg sơ đồ mạng lưới vi mạch xốp giảm áp búa nước dưới đáy sọ: bản tổng hợp sơ đồ cơ khí: tim 11kg, mạng xả áp Rete, tất nén chân và đòn bẩy cổ |
| b02 | 00:08.8–00:20.4 (11.5s) | L47 | truyền cảm hứng chế tạo trang phục phi hành gia cho NASA, cho đến hệ thống dây chằng gáy đàn hồi dày như cáp treo nâng đỡ chiếc cổ 2m, Tháp Cẩu Di Động chính là một minh chứng hùng hồn nhất cho thấy thiên nhiên chính là vị tổng công trình sư vĩ đại |  | chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): hươu vươn cao ngạo nghễ ăn chồi non trên đỉnh cây keo bao báp dưới ánh bình minh rực rỡ |
| b03 | 00:20.4–00:32.3 (11.9s) | L48 | và tinh tế nhất của vũ trụ. Để có thể vươn tầm mắt lên độ cao 5m và thưởng thức những chồi non ngọt ngào nhất trên đỉnh ngọn cây keo gai mà chẳng có loài động vật ăn cỏ nào khác trên thảo nguyên có thể với tới, con vật đã dũng cảm |  | chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): chân dung hươu trầm tĩnh bất khả chiến bại làm chủ áp lực khắc nghiệt của tự nhiên |
| b04 | 00:32.3–00:43.8 (11.5s) | L49 | chấp nhận sống chung với một môi trường áp suất khắc nghiệt gấp đôi bình thường, và nó đã tự trang bị cho mình những giải pháp cơ khí tối ưu nhất để biến áp lực hiểm nghèo thành lợi thế sinh tồn tuyệt đối. Trong hành trình cuộc sống và sự nghiệp |  | kỹ sư trưởng mặc đồ bảo hộ xưởng cơ khí, cầm cờ lê và bản vẽ đường ống thủy lực cô trợ lý kỹ thuật đeo kính bảo hộ cầm bảng kẹp tài liệu ghi chép áp suất: kỹ sư và cô trợ lý đứng trên đỉnh núi đón ánh dương chia sẻ bài học về áp lực cuộc sống |
| b05 | 00:43.8–00:55.1 (11.3s) | L50 | của mỗi chúng ta cũng vậy! Bất kỳ ai khao khát đứng ở một vị trí cao hơn, nhìn xa trông rộng hơn đám đông và chạm tới những đỉnh cao rực rỡ đều sẽ phải đối diện với những áp lực vô hình cực kỳ dữ dội và những thử thách khắc nghiệt đè |  | kỹ sư trưởng mặc đồ bảo hộ xưởng cơ khí, cầm cờ lê và bản vẽ đường ống thủy lực: kỹ sư cầm trái tim bánh răng vàng lan tỏa năng lượng bản lĩnh vượt qua thử thách |
| b06 | 00:55.1–01:06.4 (11.3s) | L51 | nặng lên vai. Nhưng thay vì than vãn hay để áp lực cuộc sống đè bẹp ý chí, chúng ta hãy học hỏi cỗ máy Tháp Cẩu Di Động kiên cường: Tôi luyện cho mình một trái tim quả cảm đầy nhiệt huyết, xây dựng một cơ chế xả stress thông minh để |  | mô hình quả tim thép 11kg với đồng hồ đo áp suất 300 mmHg sơ đồ mạng lưới vi mạch xốp giảm áp búa nước dưới đáy sọ: màn hình bình chọn đối kháng: tim 300 mmHg đối đầu mạng lưới xả áp Rete Mirabile |
| b07 | 01:06.4–01:12.1 (5.7s) | L52 | cân bằng cảm xúc, và khoác lên mình một bản lĩnh vững vàng để vượt qua mọi bão giông thử thách! Các bạn cảm thấy ấn tượng |  | kỹ sư trưởng mặc đồ bảo hộ xưởng cơ khí, cầm cờ lê và bản vẽ đường ống thủy lực cô trợ lý kỹ thuật đeo kính bảo hộ cầm bảng kẹp tài liệu ghi chép áp suất chú ngơ ngác gãi đầu hoảng hốt trước đồng hồ đo áp suất bé con đội mũ safari đeo ba lô tò mò chỉ tay hỏi: toàn bộ dàn nhân vật vẫy tay chào khán giả và chỉ xuống phần bình luận |
| b08 | 01:12.1–01:25.8 (13.7s) | L52b | và khâm phục bộ phận cơ khí nào nhất của chú hươu: Khối động cơ tim 300 mmHg phi thường, hay mạng lưới xả áp Rete Mirabile tài tình chống nổ não? Hãy chia sẻ quan điểm thú vị của bạn ở phần bình luận bên dưới nhé! Còn trong tập tiếp theo, chúng ta sẽ cùng nhau bay |  | HÌNH L52b (16:9 ngang, bản vẽ kỹ thuật đường ống công nghiệp và thủy lực (Industrial Piping Schematic & Hydraulic Blueprint), nền xanh đậm blueprint kỹ thuật #0C1824, các đường nét sơ đồ phát sáng dạ quang cyan #00F0FF và cam neon #FF8800, bản vẽ chi tiết các van, ống dẫn, đồng hồ đo áp suất, KHÔNG chữ, không logo). Phác họa bóng dáng kỳ bí của đầm lầy tiền sử và loài chim khổng lồ ở tập tiếp theo. |
| b09 | 01:25.8–01:35.4 (9.6s) | L53 | tới những đầm lầy tiền sử rậm rạp ở châu Phi để giải mã một sát thủ đứng im như tượng đá hàng giờ liền với chiếc mỏ khổng lồ gõ đanh thép như súng máy liên thanh! Hãy cùng đón chờ nhé! |  | NO_HERO: hình bóng bí ẩn của Cò Mỏ Giày đứng bất động trong đầm lầy tiền sử nhá hàng tập sau |

## 5. Phân cảnh Shorts — từng beat

Banner: **CÚI ĐẦU 2M / NỔ NÃO KHÔNG?!** · giọng 50.5s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Bạn có biết một con Hươu Cao Cổ nặng 2 tấn có thể |  |
| s02 | 00:03.5 | S01b | bị nổ tung mạch máu não mỗi khi cúi đầu xuống đất uống nước không?! |  |
| s03 | 00:07.2 | S02 | Hãy nhìn chiếc cổ dài 2m của Tháp Cẩu Di Động lừng lững giữa thảo nguyên này xem! |  |
| s04 | 00:11.6 | S03 | Để bơm máu đỏ ngược chiều trọng lực lên độ cao 5m, quả tim của nó nặng |  |
| s05 | 00:15.3 | S03b | tới 11kg và tạo ra áp lực tâm thu 300 mmHg, gấp đôi người khỏe mạnh nhất! |  |
| s06 | 00:20.8 | S04 | Khi nó hạ đầu rơi tự do ba mét xuống vũng nước, áp suất dồn xuống não sẽ tăng vọt |  |
| s07 | 00:25.3 | S04b | lên 500 mmHg, đủ để làm vỡ toang mạch máu ngay tức khắc! |  |
| s08 | 00:29.4 | S05 | Nhưng kỳ diệu thay, dưới đáy hộp sọ của nó có một mạng lưới mạch máu xốp mang tên Rete Mirabile cùng chuỗi van một chiều cơ |  |
| s09 | 00:35.6 | S06 | học. Khi đầu chúi xuống, mạng lưới này lập tức phình to hấp thụ toàn bộ xung lực búa nước, triệt tiêu áp suất thừa! |  |
| s10 | 00:41.8 | S07 | Chưa hết, cẳng chân của nó được bọc lớp da siêu căng như bộ đồ phi hành gia NASA, chống phù nề tuyệt đối! |  |
| s11 | 00:47.4 | S08 | Đúng là một tuyệt tác cơ khí thủy lực đỉnh cao của tạo hóa! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Chào mừng toàn thể các kỹ sư cơ khí sinh học và các chuyên gia giải mã vũ khí tự nhiên đã quay trở lại với xưởng nghiên cứu tối mật của chúng tôi! Hôm". Bố cục: kỹ sư trưởng mặc đồ bảo hộ xưởng cơ khí, cầm cờ lê và bản vẽ đường ống thủy lực: kỹ sư trưởng mở cuộn bản vẽ tháp cẩu 5 mét trên bàn vẽ kỹ thuật
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nay, ống nhòm viễn vọng của chúng ta sẽ hướng thẳng ra thảo nguyên châu Phi nắng cháy rực lửa, nơi một công trình kiến trúc cơ động cao nhất trên cạn đang lừng lững sải bước giữa đường chân trời. Hãy quan sát thật kỹ khối kết cấu sinh". Bố cục: chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): chú hươu cao cổ bước đi uy nghiêm giữa thảo nguyên hoàng hôn như cỗ máy tháp cẩu di động
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "học đồ sộ ấy! Một khối lượng lừng lững nặng tới gần 2 tấn, đỉnh đầu chót vót cách mặt đất hơn 5m, vươn cao ngạo nghễ như một tháp truyền hình di động giữa bầy thú ăn cỏ. Giới động vật học thông thường gọi nó bằng cái tên". Bố cục: chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): sơ đồ giải phẫu chịu lực của cơ thể 2 tấn trên 4 cẳng chân khẳng khiu
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "quen thuộc là Hươu Cao Cổ, nhưng trong mắt ban thiết kế công trình của chúng tôi, đây đích thị là cỗ máy Tháp Cẩu Di Động vĩ đại nhất từng được tự nhiên tạo tác. Bạn có bao giờ tự đặt câu hỏi dưới góc nhìn vật lý thuần". Bố cục: chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động) kỹ sư trưởng mặc đồ bảo hộ xưởng cơ khí, cầm cờ lê và bản vẽ đường ống thủy lực: kỹ sư chỉ thước đo vào chiếc cổ 2m với nhãn kỹ thuật THÁP CẨU SAVANNAH
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "túy: Làm thế nào để bơm một cột nước màu đỏ nặng trịch ngược chiều trọng lực trái đất lên độ cao 2m suốt 24/24 giờ không ngừng nghỉ mà không làm nổ tung động cơ? Báo cáo chỉ huy, nếu dùng máy bơm bình thường đẩy nước lên tầng năm,". Bố cục: chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): sơ đồ cắt dọc cổ cho thấy cột nước màu đỏ rực leo dốc 2m ngược chiều trọng lực
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "ống nhựa sẽ nổ tung vì áp lực quá tải! Nhận định hoàn toàn chuẩn xác không cần chỉnh cô trợ lý kỹ thuật ạ! Định luật thủy tĩnh cơ bản quy định rằng cứ mỗi mét chất lỏng dâng cao, áp suất đáy sẽ tăng lên dữ dội. Nếu". Bố cục: cô trợ lý kỹ thuật đeo kính bảo hộ cầm bảng kẹp tài liệu ghi chép áp suất: cô trợ lý cầm đường ống vỡ tung tóe vì áp lực quá tải cảnh báo nguy cơ nổ ống
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "cơ thể một người bình thường chúng ta bị kéo giãn chiếc cổ ra 2m như thế này, quả tim con người sẽ bất lực hoàn toàn, không thể bơm nổi một giọt nước màu nào lên tới đỉnh đầu, và toàn bộ hệ thần kinh trung ương sẽ chết đói". Bố cục: chú ngơ ngác gãi đầu hoảng hốt trước đồng hồ đo áp suất: chú ngơ ngác hoa mắt chóng mặt khi tưởng tượng cổ mình dài 2m thiếu nước màu não
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "vì cạn kiệt oxy chỉ sau đúng ba giây ngắn ngủi. Ấy vậy mà Tháp Cẩu Di Động không những không hề choáng váng, nó còn thong dong vươn chiếc lưỡi dài nửa mét màu tím đen để tước từng chiếc lá gai nhọn hoắt của cây keo bao báp,". Bố cục: chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): cận cảnh chiếc lưỡi dài 50cm màu tím đen tước lá gai keo nhọn hoắt không hề hấn
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "thậm chí khi cần nó có thể bứt tốc phi nước đại với vận tốc 50km/h một giờ. Mọi linh kiện bên trong con vật này đều được tôi luyện với dung sai cực hạn, vượt xa mọi tiêu chuẩn công nghiệp cơ khí nặng hiện đại nhất. Ngay bây giờ, hãy cầm cờ-lê tháo bu-lông và mở tung bản vẽ khoang động cơ chính ra xem!". Bố cục: kỹ sư trưởng mặc đồ bảo hộ xưởng cơ khí, cầm cờ lê và bản vẽ đường ống thủy lực chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): kỹ sư vặn van khóa áp suất mở toang khoang động cơ tim phổi của hươu
```
</details>

<details><summary>L09b</summary>

```text
HÌNH L09b (16:9 ngang, bản vẽ kỹ thuật đường ống công nghiệp và thủy lực (Industrial Piping Schematic & Hydraulic Blueprint), nền xanh đậm blueprint kỹ thuật #0C1824, các đường nét sơ đồ phát sáng dạ quang cyan #00F0FF và cam neon #FF8800, bản vẽ chi tiết các van, ống dẫn, đồng hồ đo áp suất, KHÔNG chữ, không logo). Minh họa sơ đồ chi tiết các chi tiết cơ khí và vật liệu chịu lực cao được tôi luyện với dung sai cực hạn của cỗ máy hươu cao cổ.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Để nâng được một cột chất lỏng nhớt có tỷ trọng nặng hơn nước lên độ cao thẳng đứng 2m ngược chiều gia tốc trọng trường, yêu cầu tiên quyết đầu tiên trên bản vẽ chính là một khối động cơ bơm áp lực siêu cường. Trái tim của". Bố cục: mô hình quả tim thép 11kg với đồng hồ đo áp suất 300 mmHg: mô hình quả tim 11kg khổng lồ đập thình thịch với các ống dẫn áp lực cao
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Tháp Cẩu Di Động hoàn toàn không phải dạng vừa, nó là một khối cơ bắp rắn rỏi nặng tới 11kg, dài hơn 60cm và sở hữu thể tích buồng chứa cực lớn, có khả năng luân chuyển hàng chục lít nước màu mỗi phút. Đặc biệt nhất chính là thành tâm thất trái của nó, nơi trực tiếp tạo ra lực đẩy". Bố cục: mô hình quả tim thép 11kg với đồng hồ đo áp suất 300 mmHg kỹ sư trưởng mặc đồ bảo hộ xưởng cơ khí, cầm cờ lê và bản vẽ đường ống thủy lực: kỹ sư đo kích thước quả tim dài 60cm nặng 11kg so với tim người tí hon
```
</details>

<details><summary>L11b</summary>

```text
HÌNH L11b (16:9 ngang, bản vẽ kỹ thuật đường ống công nghiệp và thủy lực (Industrial Piping Schematic & Hydraulic Blueprint), nền xanh đậm blueprint kỹ thuật #0C1824, các đường nét sơ đồ phát sáng dạ quang cyan #00F0FF và cam neon #FF8800, bản vẽ chi tiết các van, ống dẫn, đồng hồ đo áp suất, KHÔNG chữ, không logo). Mặt cắt buồng tim khổng lồ dài hơn 60cm với thể tích buồng chứa cực lớn và van tim cơ học áp lực cao.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "lên động mạch chủ, dày tới 7cm, đanh chắc và kiên cố như một tấm lốp xe tải bọc thép chuyên dụng. Khi cỗ máy sinh học này thực hiện một chu kỳ co bóp toàn phần, nó tạo ra một áp lực tâm thu khủng khiếp lên tới 300 mmHg, tức là gấp đôi mức huyết áp đỉnh cao của một vận". Bố cục: mô hình quả tim thép 11kg với đồng hồ đo áp suất 300 mmHg: mặt cắt thành tâm thất trái dày 7cm đanh chắc như lốp xe tải bọc thép
```
</details>

<details><summary>L12b</summary>

```text
HÌNH L12b (16:9 ngang, bản vẽ kỹ thuật đường ống công nghiệp và thủy lực (Industrial Piping Schematic & Hydraulic Blueprint), nền xanh đậm blueprint kỹ thuật #0C1824, các đường nét sơ đồ phát sáng dạ quang cyan #00F0FF và cam neon #FF8800, bản vẽ chi tiết các van, ống dẫn, đồng hồ đo áp suất, KHÔNG chữ, không logo). Sơ đồ chu kỳ co bóp tâm thu của khối cơ tim tạo áp lực tống máu 300 mmHg vào động mạch chủ vươn cao.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "động viên điền kinh Olympic khỏe mạnh nhất! Tại sao hệ thống này lại bắt buộc phải vận hành ở mức áp lực bạo lực đến như vậy? Bởi vì định luật thủy tĩnh không hề có sự nhân nhượng cho bất kỳ sinh vật nào! Dòng nước màu đỏ xuất phát từ van tim ở lồng ngực phải leo dốc thẳng đứng vượt". Bố cục: mô hình quả tim thép 11kg với đồng hồ đo áp suất 300 mmHg: đồng hồ đo áp suất kim loại chỉ vạch đỏ 300 mmHg xả hơi nước cảnh báo
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "qua lực hút trái đất trên quãng đường dài 2m để chạm tới vỏ não. Cứ mỗi 30cm chiều cao tăng thêm, áp suất thủy tĩnh sẽ sụt giảm khoảng 25 mmHg. Nếu như áp lực bơm tim của hươu chỉ duy trì ở mức 120 như con người chúng ta, thì khi dòng nước màu leo tới nửa đoạn cổ, áp suất đẩy". Bố cục: chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): sơ đồ sụt giảm áp suất thủy tĩnh: từ 300 mmHg ở ngực giảm dần còn 100 mmHg ở não
```
</details>

<details><summary>L14b</summary>

```text
HÌNH L14b (16:9 ngang, bản vẽ kỹ thuật đường ống công nghiệp và thủy lực (Industrial Piping Schematic & Hydraulic Blueprint), nền xanh đậm blueprint kỹ thuật #0C1824, các đường nét sơ đồ phát sáng dạ quang cyan #00F0FF và cam neon #FF8800, bản vẽ chi tiết các van, ống dẫn, đồng hồ đo áp suất, KHÔNG chữ, không logo). Đồ thị cột thủy ngân và sơ đồ sụt giảm áp suất thủy tĩnh theo từng mét độ cao của chiếc cổ dài.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "đã giảm về mức số không, khiến nước màu ngừng chảy và chảy ngược trở lại, dẫn đến tình trạng thiếu nước màu não tức thì. Nhờ việc duy trì công suất cực đại 300 mmHg ngay tại cửa xả của tim, khi dòng nước màu chạm tới đỉnh đầu sau hành trình leo dốc gian nan, áp suất còn lại ở não bộ vẫn duy". Bố cục: chú ngơ ngác gãi đầu hoảng hốt trước đồng hồ đo áp suất chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): sơ đồ so sánh huyết áp người 120 mmHg bị tắc nghẽn giữa chừng ở độ cao 1m
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "trì hoàn hảo ở mức 100 mmHg, vừa vặn tuyệt đối để hệ thần kinh trung ương xử lý tín hiệu sắc bén như dao cạo. Nhưng các kỹ sư cơ khí hãy đặc biệt chú ý đến một bí mật thiết kế đắt giá này! Một khối động cơ tim áp suất cao như vậy nếu đập dồn dập liên tục thì". Bố cục: chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): não bộ hươu trên đỉnh đầu sáng rực nhận dòng nước màu 100 mmHg êm ái hoàn hảo
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chẳng mấy chốc sẽ bị nổ van hoặc suy tim sớm. Thiên nhiên đã lập trình cho trái tim của Tháp Cẩu Di Động một nhịp đập cực kỳ điềm tĩnh, dao động từ 40-90 nhịp mỗi phút. Mỗi nhịp co bóp tống đi một thể tích nước màu khổng lồ vào gốc động mạch chủ. Thành của động mạch chủ ở hươu được". Bố cục: mô hình quả tim thép 11kg với đồng hồ đo áp suất 300 mmHg: biểu đồ sóng điện tim nhịp đập chậm rãi uy nghi 40-90 nhịp mỗi phút
```
</details>

<details><summary>L17b</summary>

```text
HÌNH L17b (16:9 ngang, bản vẽ kỹ thuật đường ống công nghiệp và thủy lực (Industrial Piping Schematic & Hydraulic Blueprint), nền xanh đậm blueprint kỹ thuật #0C1824, các đường nét sơ đồ phát sáng dạ quang cyan #00F0FF và cam neon #FF8800, bản vẽ chi tiết các van, ống dẫn, đồng hồ đo áp suất, KHÔNG chữ, không logo). Đồng hồ đo nhịp đập sinh học điềm tĩnh 40-90 nhịp mỗi phút điều phối dòng chảy thủy lực ổn định.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "gia cố bằng nhiều lớp sợi elastin siêu đàn hồi, hoạt động giống hệt như một bình tích áp thủy lực Windkessel trong kỹ thuật cơ khí đường ống. Bình tích áp này giãn nở để hấp thụ chấn động từ mỗi cú nén cao áp cực mạnh của tim, rồi co lại nhịp nhàng để duy trì dòng chảy liên tục và êm ái, biến dòng nước màu giật cục thành một dòng chảy ổn định tuần hoàn khắp cơ thể đồ sộ 5m.". Bố cục: chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động) kỹ sư trưởng mặc đồ bảo hộ xưởng cơ khí, cầm cờ lê và bản vẽ đường ống thủy lực: kỹ sư kiểm tra buồng giãn nở đàn hồi Windkessel của động mạch chủ duy trì dòng chảy liên tục
```
</details>

<details><summary>L18b</summary>

```text
HÌNH L18b (16:9 ngang, bản vẽ kỹ thuật đường ống công nghiệp và thủy lực (Industrial Piping Schematic & Hydraulic Blueprint), nền xanh đậm blueprint kỹ thuật #0C1824, các đường nét sơ đồ phát sáng dạ quang cyan #00F0FF và cam neon #FF8800, bản vẽ chi tiết các van, ống dẫn, đồng hồ đo áp suất, KHÔNG chữ, không logo). Cụm bình tích áp Windkessel giãn nở đàn hồi hấp thụ chấn động áp lực máu dọc động mạch chủ.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Bây giờ mới thực sự là bài kiểm tra ứng suất kinh hoàng nhất trong toàn bộ quy trình vận hành của Tháp Cẩu Di Động. Mặc dù sở hữu chiều cao 5m để với tới những cành cây cao chót vót, nhưng vũng nước uống duy nhất giữa sa mạc lại nằm sát sàn sạt dưới mặt". Bố cục: chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): hươu xoạc rộng hai chân trước cúi chiếc cổ 2m rơi tự do xuống vũng nước
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "đất. Để uống được nước, con vật không thể quỳ gối quá lâu vì dễ bị thú săn mồi phục kích. Nó buộc phải xoạc rộng hai chân trước sang hai bên rồi hạ thấp phần đầu xuống trong một cú rơi tự do sâu tới gần ba mét. Các bạn hãy làm một phép tính vật lý đơn giản: Một hệ thống ống dẫn đang chịu áp suất 300 mmHg, nay lại". Bố cục: chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): mô phỏng áp suất dồn xuống đầu vọt lên 500 mmHg với biểu tượng cảnh báo nguy hiểm
```
</details>

<details><summary>L20b</summary>

```text
HÌNH L20b (16:9 ngang, bản vẽ kỹ thuật đường ống công nghiệp và thủy lực (Industrial Piping Schematic & Hydraulic Blueprint), nền xanh đậm blueprint kỹ thuật #0C1824, các đường nét sơ đồ phát sáng dạ quang cyan #00F0FF và cam neon #FF8800, bản vẽ chi tiết các van, ống dẫn, đồng hồ đo áp suất, KHÔNG chữ, không logo). Tư thế hươu cao cổ xoạc rộng hai chân trước hạ thấp đầu xuống gần mặt nước uống nước.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "được cộng dồn thêm toàn bộ trọng lượng của cột nước màu cao 2m đổ dồn thẳng đứng từ trên ngực xuống đáy hộp sọ theo chiều gia tốc trọng trường. Áp lực nước màu tại khoang não lúc này sẽ lập tức tăng vọt lên tới gần 500 mmHg! Ở bất kỳ loài động vật có vú nào khác, mức áp suất bạo tàn này thừa sức phá hủy toàn bộ mạng lưới mao". Bố cục: chú ngơ ngác gãi đầu hoảng hốt trước đồng hồ đo áp suất: chú ngơ ngác ôm đầu hoảng hốt sợ đầu hươu nổ tung như quả bóng cao su bơm căng
```
</details>

<details><summary>L21b</summary>

```text
HÌNH L21b (16:9 ngang, bản vẽ kỹ thuật đường ống công nghiệp và thủy lực (Industrial Piping Schematic & Hydraulic Blueprint), nền xanh đậm blueprint kỹ thuật #0C1824, các đường nét sơ đồ phát sáng dạ quang cyan #00F0FF và cam neon #FF8800, bản vẽ chi tiết các van, ống dẫn, đồng hồ đo áp suất, KHÔNG chữ, không logo). Mô phỏng dòng thủy lực tăng áp đột ngột do gia tốc trọng trường khi đầu dốc ngược xuống đất.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "mạch não mỏng manh, gây xuất huyết ồ ạt và tử vong tại chỗ chỉ trong tích tắc! Khoan đã thầy ơi, vậy tại sao đầu của nó không phát nổ tung toé như một quả bóng bay bằng cao su bị bơm quá áp suất? Một câu hỏi vô cùng thực tế và đáng giá triệu đô đấy người anh em ngơ ngác! Bí mật sống còn nằm ở một cụm chi". Bố cục: sơ đồ mạng lưới vi mạch xốp giảm áp búa nước dưới đáy sọ kỹ sư trưởng mặc đồ bảo hộ xưởng cơ khí, cầm cờ lê và bản vẽ đường ống thủy lực: kỹ sư soi kính lúp vào mạng lưới Rete Mirabile dưới đáy sọ hươu
```
</details>

<details><summary>L22b</summary>

```text
HÌNH L22b (16:9 ngang, bản vẽ kỹ thuật đường ống công nghiệp và thủy lực (Industrial Piping Schematic & Hydraulic Blueprint), nền xanh đậm blueprint kỹ thuật #0C1824, các đường nét sơ đồ phát sáng dạ quang cyan #00F0FF và cam neon #FF8800, bản vẽ chi tiết các van, ống dẫn, đồng hồ đo áp suất, KHÔNG chữ, không logo). Sơ đồ bảo vệ chống nổ vỡ mạch máu não trước áp suất thủy tĩnh khổng lồ 500 mmHg.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tiết cơ khí sinh học tối mật được giấu kín ngay dưới đáy hộp sọ của hươu, mang tên khoa học là Rete Mirabile, tiếng Latin có nghĩa là Mạng Lưới Kỳ Diệu. Đây là một ma trận chằng chịt gồm hàng ngàn mạch nước màu nhỏ li ti, lồng ghép đan xen vào nhau giống hệt như một miếng bọt biển hấp thụ lực va đập thủy tĩnh. Khi Tháp Cẩu Di Động". Bố cục: sơ đồ mạng lưới vi mạch xốp giảm áp búa nước dưới đáy sọ: kính hiển vi phóng đại ma trận vi mạch xốp Rete Mirabile phình to hấp thụ xung lực búa nước
```
</details>

<details><summary>L23b</summary>

```text
HÌNH L23b (16:9 ngang, bản vẽ kỹ thuật đường ống công nghiệp và thủy lực (Industrial Piping Schematic & Hydraulic Blueprint), nền xanh đậm blueprint kỹ thuật #0C1824, các đường nét sơ đồ phát sáng dạ quang cyan #00F0FF và cam neon #FF8800, bản vẽ chi tiết các van, ống dẫn, đồng hồ đo áp suất, KHÔNG chữ, không logo). Cận cảnh cấu tạo mạng lưới mạch máu xốp Rete Mirabile đan xen dày đặc như bọt biển dưới nền sọ.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "hạ thấp đầu xuống vũng nước, lượng nước màu áp suất cao ồ ạt đổ xuống sẽ lập tức bị mạng lưới này phân tán vào vô số nhánh rẽ nhỏ li ti. Thiết diện tổng của dòng chảy tăng vọt làm vận tốc dòng nước màu giảm xuống đột ngột, triệt tiêu hoàn toàn xung lực búa nước va đập trước khi những giọt nước màu có thể chạm tới các tế bào thần kinh". Bố cục: chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): mặt cắt tĩnh mạch cổ 2m với chuỗi van một chiều cơ học sập chặt khóa dòng nước màu đen
```
</details>

<details><summary>L24b</summary>

```text
HÌNH L24b (16:9 ngang, bản vẽ kỹ thuật đường ống công nghiệp và thủy lực (Industrial Piping Schematic & Hydraulic Blueprint), nền xanh đậm blueprint kỹ thuật #0C1824, các đường nét sơ đồ phát sáng dạ quang cyan #00F0FF và cam neon #FF8800, bản vẽ chi tiết các van, ống dẫn, đồng hồ đo áp suất, KHÔNG chữ, không logo). Sơ đồ thiết diện tổng của dòng chảy tăng vọt gấp trăm lần làm giảm vận tốc và áp lực máu.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nhạy cảm. Chưa dừng lại ở đó đâu nhé! Dọc theo suốt chiều dài 2m của tĩnh mạch cổ là cả một hệ thống các van một chiều cơ học đóng mở tự động cực kỳ tinh xảo. Ngay khoảnh khắc chiếc đầu hạ thấp quá tim, các van tĩnh mạch một chiều này lập tức sập chặt lại, ngăn chặn tuyệt đối tình trạng nước màu đen ứ đọng từ khoang ngực chảy". Bố cục: chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động) sư tử châu phi bờm rậm hoảng hốt né đòn đạp hậu của hươu: hươu giật phắt đầu vụt cao 5m trong 1 giây khi sư tử phục kích trong bụi rậm
```
</details>

<details><summary>L25b</summary>

```text
HÌNH L25b (16:9 ngang, bản vẽ kỹ thuật đường ống công nghiệp và thủy lực (Industrial Piping Schematic & Hydraulic Blueprint), nền xanh đậm blueprint kỹ thuật #0C1824, các đường nét sơ đồ phát sáng dạ quang cyan #00F0FF và cam neon #FF8800, bản vẽ chi tiết các van, ống dẫn, đồng hồ đo áp suất, KHÔNG chữ, không logo). Cận cảnh van một chiều cơ học tự động khép chặt chặn đứng dòng máu dội ngược về tĩnh mạch cổ.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "ngược trở lại đầu gây tăng áp nội sọ. Và điều kỳ diệu nhất diễn ra khi con vật bất ngờ phát hiện thấy một con sư tử đang rình rập trong bụi rậm! Nó lập tức giật phắt chiếc đầu nặng nề cao vụt lên trời ở độ cao 5m chỉ trong vòng chưa đầy một giây. Một cú giật ngược đột ngột như thế bình thường sẽ làm toàn bộ nước màu". Bố cục: sơ đồ mạng lưới vi mạch xốp giảm áp búa nước dưới đáy sọ chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): mạng lưới Rete Mirabile xả lượng nước màu dự trữ nuôi não giúp hươu tỉnh táo phóng chạy
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tụt dốc về tim, khiến não bộ rơi vào trạng thái thiếu oxy cục bộ và gây ngất xỉu ngay tức thì. Nhưng mạng lưới Rete Mirabile lại đóng vai trò như một kho dự trữ nước màu khẩn cấp, từ từ xả lượng nước màu tích trữ ra để nuôi dưỡng não trong lúc tim điều chỉnh lại nhịp đập, giúp con vật giữ vững sự tỉnh táo hoàn toàn để phóng nước đại tẩu thoát. Đó là một cơ chế giảm chấn thủy lực hai chiều hoàn mỹ đến từng phân tử!". Bố cục: kỹ sư trưởng mặc đồ bảo hộ xưởng cơ khí, cầm cờ lê và bản vẽ đường ống thủy lực: kỹ sư giơ ngón tay cái tán thưởng cơ chế giảm chấn thủy lực hai chiều hoàn mỹ
```
</details>

<details><summary>L27b</summary>

```text
HÌNH L27b (16:9 ngang, bản vẽ kỹ thuật đường ống công nghiệp và thủy lực (Industrial Piping Schematic & Hydraulic Blueprint), nền xanh đậm blueprint kỹ thuật #0C1824, các đường nét sơ đồ phát sáng dạ quang cyan #00F0FF và cam neon #FF8800, bản vẽ chi tiết các van, ống dẫn, đồng hồ đo áp suất, KHÔNG chữ, không logo). Kho dự trữ máu khẩn cấp nhả từ từ lượng máu đã lọc nuôi não khi hươu ngẩng đầu vút lên cao.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Giải quyết xong bài toán áp suất phức tạp ở phần đỉnh tháp, bây giờ mời toàn thể ban kỹ sư cùng chuyển ống kính xuống kiểm tra phần gầm của cỗ máy Tháp Cẩu Di Động. Với một sinh vật có tầm vóc khổng lồ đứng". Bố cục: kỹ sư trưởng mặc đồ bảo hộ xưởng cơ khí, cầm cờ lê và bản vẽ đường ống thủy lực chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): kỹ sư rọi đèn pin vào đôi chân khẳng khiu chịu áp lực thủy tĩnh khổng lồ
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "thẳng trên bốn chiếc chân khẳng khiu cao tới gần 2m, áp lực thủy tĩnh ở cẳng chân dưới là một cơn ác mộng kỹ thuật không kém phần nan giải. Trọng lực đè nặng toàn bộ thể tích nước màu trong cơ thể dồn xuống các mao mạch ở bàn chân, tạo ra một áp suất nội mạch thường xuyên vượt ngưỡng". Bố cục: chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): sơ đồ cột nước màu dồn xuống bàn chân với áp lực vượt ngưỡng 200 mmHg
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "200 mmHg. Để các bạn dễ hình dung, ở cơ thể con người chúng ta, chỉ cần phải đứng im bất động trong vài giờ liên tục, nước màu sẽ dồn xuống bàn chân làm tăng áp suất mao mạch, khiến huyết tương rò rỉ vào khoang gian bào gây phù nề mắt cá chân, suy giãn tĩnh mạch hoặc thậm chí vỡ". Bố cục: chú ngơ ngác gãi đầu hoảng hốt trước đồng hồ đo áp suất: chú ngơ ngác ôm mắt cá chân sưng phù đau đớn vì đứng lâu tụ nước màu
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "mao mạch tạo thành các vết xuất huyết bầm tím dưới da. Vậy thì điều kỳ diệu gì đã bảo vệ bốn chiếc chân khẳng khiu như những que tăm của hươu không bị nứt toác và phù nề sau hàng chục năm đứng liên tục giữa thảo nguyên? Câu trả lời là thiên nhiên đã trang bị cho nó một bộ". Bố cục: chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): cận cảnh cẳng chân hươu khô ráo thanh thoát không hề có một vết phù nề
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tất áp lực sinh học hoàn hảo bậc nhất thế giới! Đây chính là cấu trúc cơ học mà sau này các nhà khoa học của cơ quan hàng không vũ trụ NASA đã phải cất công nghiên cứu tỉ mỉ để chế tạo ra bộ đồ kháng áp G-suit dành cho phi công tiêm kích siêu âm và các phi hành". Bố cục: kỹ sư trưởng mặc đồ bảo hộ xưởng cơ khí, cầm cờ lê và bản vẽ đường ống thủy lực cô trợ lý kỹ thuật đeo kính bảo hộ cầm bảng kẹp tài liệu ghi chép áp suất: cô trợ lý giới thiệu bộ đồ phi hành gia G-suit NASA lấy cảm hứng từ chân hươu
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "gia khi chịu gia tốc phóng cực đại. Bao bọc lấy toàn bộ phần cẳng chân của hươu là một lớp da dày cộm, cứng cáp và có độ đàn hồi cực kỳ thấp, ôm sát rạt lấy cơ thể giống như một lớp vỏ bọc bằng sợi carbon composite. Ngay bên dưới lớp da dày ấy là một màng cân cơ". Bố cục: chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): mặt cắt lớp da dày và bao cân cơ siêu căng bó chặt như sợi carbon composite
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "dày đặc và rắn chắc, bọc kín lấy từng thớ cơ và mạch nước màu như một chiếc băng cuốn y tế chuyên dụng được siết chặt tối đa. Lớp vỏ bọc cơ học siêu bền này tạo ra một lực ép ngoại sinh cực mạnh tác động ngược trở lại thành mạch, cân bằng hoàn hảo với áp lực thủy tĩnh nội". Bố cục: chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): mũi tên áp lực ngoại sinh ép ngược lại triệt tiêu áp lực thủy tĩnh nội mạch
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "mạch đang đẩy từ bên trong ra. Nhờ có áp suất đối kháng này, huyết tương và dịch lỏng hoàn toàn không thể thoát ra ngoài khoang mô để gây sưng phù chân. Hơn thế nữa, thành của các tiểu động mạch và mao mạch ở chân hươu dày hơn bất kỳ loài động vật có vú nào từng được ghi nhận,". Bố cục: chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): cơ vòng tiền mao mạch co thắt như van tiết lưu thông minh điều hòa lưu lượng nước màu
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "kết hợp với các cơ vòng tiền mao mạch hoạt động như những chiếc van tiết lưu thông minh, chủ động ngắt dòng nước màu khi áp suất cục bộ vượt ngưỡng cho phép. Cỗ máy Tháp Cẩu Di Động có thể thong thả đứng cả ngày lẫn đêm dưới ánh mặt trời thiêu đốt mà bốn cẳng chân vẫn khô ráo, thanh thoát, chẳng hề bị phù nề, luôn trong tư thế sẵn sàng tung ra những cú đạp sấm sét.". Bố cục: chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): hươu đứng vững chãi giữa nắng gắt sa mạc sẵn sàng phi nước đại 50km/h
```
</details>

<details><summary>L36b</summary>

```text
HÌNH L36b (16:9 ngang, bản vẽ kỹ thuật đường ống công nghiệp và thủy lực (Industrial Piping Schematic & Hydraulic Blueprint), nền xanh đậm blueprint kỹ thuật #0C1824, các đường nét sơ đồ phát sáng dạ quang cyan #00F0FF và cam neon #FF8800, bản vẽ chi tiết các van, ống dẫn, đồng hồ đo áp suất, KHÔNG chữ, không logo). Cỗ máy Tháp Cẩu Di Động uy nghi vươn cao giữa thảo nguyên savan với hệ thống cảm biến áp suất toàn diện.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Đừng bao giờ để vẻ bề ngoài hiền lành, đôi mắt to tròn ngơ ngác và dáng điệu nhai lá cây chậm rãi của Tháp Cẩu Di Động ru ngủ bạn! Khi mùa". Bố cục: chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): ánh mắt hươu biến chuyển sắc lạnh đầy sát khí bước vào trận chiến lãnh thổ
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "giao phối tranh giành lãnh thổ bắt đầu hoặc khi con vật bị dồn vào bước đường cùng đối đầu với bầy dã thú săn mồi, chiếc cần cẩu dài 2m thanh mảnh này sẽ ngay lập tức chuyển hóa thành một thứ vũ khí va đập hạng". Bố cục: chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): hai con hươu đực giao đấu quăng cổ búa tạ Necking với vòng cung khổng lồ
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nặng với sức tàn phá kinh hoàng bậc nhất thảo nguyên châu Phi. Những con hươu đực không hề húc đầu trực diện như trâu rừng hay dùng móng guốc cào xé, mà chúng triển khai một tuyệt kỹ cận chiến tàn bạo mang tên khoa học là". Bố cục: chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động) kỹ sư trưởng mặc đồ bảo hộ xưởng cơ khí, cầm cờ lê và bản vẽ đường ống thủy lực: kỹ sư giơ bản vẽ 7 đốt sống cổ khổng lồ dài 30cm khớp nối linh hoạt
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Necking, tức là màn giao đấu quăng cổ búa tạ. Chiếc cổ dài 2m tuy chỉ gồm đúng bảy đốt sống cổ giống như loài người chúng ta, nhưng mỗi đốt sống lại dài tới gần 30cm, liên kết với nhau bằng các khớp cầu linh hoạt biến". Bố cục: bé con đội mũ safari đeo ba lô tò mò chỉ tay hỏi: bé con đội mũ safari nhòm ống nhòm thấy cặp sừng bọc da đặc xương và xương trán gồ ghề
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "toàn bộ chiếc cổ thành một cánh tay đòn bẩy khổng lồ gia tốc cho phần đầu hồi chuyển. Ủa các bác kỹ sư ơi, sừng của nó bọc da đặc xương, trán dày cộm như một khối đá tảng nguyên khối luôn hả? Rất chuẩn xác bác". Bố cục: chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): đồ họa vệt sáng chuyển động cho thấy đầu sọ hươu quất với vận tốc 100km/h xé gió
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "thợ máy ơi, đó chính là đầu búa công phá đấy! Khi một con hươu đực trưởng thành gồng mình vung chiếc cổ dài 2m hết biên độ vòng cung, phần đầu sọ của nó có thể xé toạc không khí và đạt vận tốc va đập lên". Bố cục: chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): hình ảnh nổ tung động năng: quả tạ xương 20kg nện xuống mạn sườn với lực hàng tấn
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tới hơn 100km/h một giờ. Hãy tưởng tượng một quả tạ đặc bằng xương và sừng nặng gần 20kg được phóng đi với vận tốc đó và nện thẳng vào mạn sườn hoặc cuống họng của đối thủ! Lực xung kích sinh ra từ cú quất búa tạ". Bố cục: chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): tia X quét qua khung xương đối thủ gãy rạn trước uy lực của cú quật búa tạ
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "này tương đương với hàng tấn động năng tập trung vào một điểm tiếp xúc nhỏ hẹp. Cú va chạm kinh hoàng ấy thừa sức bẻ gãy vụn các xương sườn, đâm thủng lá phổi, hoặc thậm chí làm gãy gập cột sống của đối thủ khiến nó". Bố cục: chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động) sư tử châu phi bờm rậm hoảng hốt né đòn đạp hậu của hươu: hươu tung cú đạp hậu sấm sét bằng chiếc chân sau nặng như cột đình hất văng sư tử
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "gục ngã tức tưởi tại chỗ. Và chưa hết đâu nhé, nếu một con sư tử châu Phi đói khát dại dột tiếp cận từ phía sau trong góc chết, chiếc chân sau dài 2m nặng như cột đình của hươu có thể tung ra một cú đạp hậu sấm sét, thừa đủ lực để làm nát vụn xương sọ của chúa sơn lâm trong chớp mắt!". Bố cục: kỹ sư trưởng mặc đồ bảo hộ xưởng cơ khí, cầm cờ lê và bản vẽ đường ống thủy lực: kỹ sư đóng dấu đỏ ĐÒN BẨY HẠNG NẶNG vào hồ sơ năng lực chiến đấu của hươu
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "Từ khối động cơ tim áp lực cao 11kg, mạng lưới van xả chấn động kỳ diệu Rete Mirabile bảo vệ não bộ khỏi nguy cơ nổ mạch nước màu, bộ đồ nén sinh học ở cẳng chân truyền cảm". Bố cục: chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động) mô hình quả tim thép 11kg với đồng hồ đo áp suất 300 mmHg sơ đồ mạng lưới vi mạch xốp giảm áp búa nước dưới đáy sọ: bản tổng hợp sơ đồ cơ khí: tim 11kg, mạng xả áp Rete, tất nén chân và đòn bẩy cổ
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "hứng chế tạo trang phục phi hành gia cho NASA, cho đến hệ thống dây chằng gáy đàn hồi dày như cáp treo nâng đỡ chiếc cổ 2m, Tháp Cẩu Di Động chính là một minh chứng hùng hồn nhất cho thấy thiên nhiên chính là vị tổng công trình sư vĩ đại và". Bố cục: chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): hươu vươn cao ngạo nghễ ăn chồi non trên đỉnh cây keo bao báp dưới ánh bình minh rực rỡ
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "tinh tế nhất của vũ trụ. Để có thể vươn tầm mắt lên độ cao 5m và thưởng thức những chồi non ngọt ngào nhất trên đỉnh ngọn cây keo gai mà chẳng có loài động vật ăn cỏ nào khác trên thảo nguyên có thể với tới, con vật đã dũng cảm chấp". Bố cục: chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động): chân dung hươu trầm tĩnh bất khả chiến bại làm chủ áp lực khắc nghiệt của tự nhiên
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "nhận sống chung với một môi trường áp suất khắc nghiệt gấp đôi bình thường, và nó đã tự trang bị cho mình những giải pháp cơ khí tối ưu nhất để biến áp lực hiểm nghèo thành lợi thế sinh tồn tuyệt đối. Trong hành trình cuộc sống và sự nghiệp của mỗi". Bố cục: kỹ sư trưởng mặc đồ bảo hộ xưởng cơ khí, cầm cờ lê và bản vẽ đường ống thủy lực cô trợ lý kỹ thuật đeo kính bảo hộ cầm bảng kẹp tài liệu ghi chép áp suất: kỹ sư và cô trợ lý đứng trên đỉnh núi đón ánh dương chia sẻ bài học về áp lực cuộc sống
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chúng ta cũng vậy! Bất kỳ ai khao khát đứng ở một vị trí cao hơn, nhìn xa trông rộng hơn đám đông và chạm tới những đỉnh cao rực rỡ đều sẽ phải đối diện với những áp lực vô hình cực kỳ dữ dội và những thử thách khắc nghiệt đè nặng". Bố cục: kỹ sư trưởng mặc đồ bảo hộ xưởng cơ khí, cầm cờ lê và bản vẽ đường ống thủy lực: kỹ sư cầm trái tim bánh răng vàng lan tỏa năng lượng bản lĩnh vượt qua thử thách
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "lên vai. Nhưng thay vì than vãn hay để áp lực cuộc sống đè bẹp ý chí, chúng ta hãy học hỏi cỗ máy Tháp Cẩu Di Động kiên cường: Tôi luyện cho mình một trái tim quả cảm đầy nhiệt huyết, xây dựng một cơ chế xả stress thông minh để cân bằng". Bố cục: mô hình quả tim thép 11kg với đồng hồ đo áp suất 300 mmHg sơ đồ mạng lưới vi mạch xốp giảm áp búa nước dưới đáy sọ: màn hình bình chọn đối kháng: tim 300 mmHg đối đầu mạng lưới xả áp Rete Mirabile
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "cảm xúc, và khoác lên mình một bản lĩnh vững vàng để vượt qua mọi bão giông thử thách! Các bạn cảm thấy ấn tượng và khâm phục bộ phận cơ khí nào nhất của chú hươu: Khối động cơ tim 300 mmHg phi thường, hay mạng lưới xả áp Rete Mirabile tài tình". Bố cục: kỹ sư trưởng mặc đồ bảo hộ xưởng cơ khí, cầm cờ lê và bản vẽ đường ống thủy lực cô trợ lý kỹ thuật đeo kính bảo hộ cầm bảng kẹp tài liệu ghi chép áp suất chú ngơ ngác gãi đầu hoảng hốt trước đồng hồ đo áp suất bé con đội mũ safari đeo ba lô tò mò chỉ tay hỏi: toàn bộ dàn nhân vật vẫy tay chào khán giả và chỉ xuống phần bình luận
```
</details>

<details><summary>L52b</summary>

```text
HÌNH L52b (16:9 ngang, bản vẽ kỹ thuật đường ống công nghiệp và thủy lực (Industrial Piping Schematic & Hydraulic Blueprint), nền xanh đậm blueprint kỹ thuật #0C1824, các đường nét sơ đồ phát sáng dạ quang cyan #00F0FF và cam neon #FF8800, bản vẽ chi tiết các van, ống dẫn, đồng hồ đo áp suất, KHÔNG chữ, không logo). Phác họa bóng dáng kỳ bí của đầm lầy tiền sử và loài chim khổng lồ ở tập tiếp theo.
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "chống nổ não? Hãy chia sẻ quan điểm thú vị của bạn ở phần bình luận bên dưới nhé! Còn trong tập tiếp theo, chúng ta sẽ cùng nhau bay tới những đầm lầy tiền sử rậm rạp ở châu Phi để giải mã một sát thủ đứng im như tượng đá hàng giờ liền với chiếc mỏ khổng lồ gõ đanh thép như súng máy liên thanh! Hãy cùng đón chờ nhé!". Bố cục: NO_HERO: hình bóng bí ẩn của Cò Mỏ Giày đứng bất động trong đầm lầy tiền sử nhá hàng tập sau
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Bạn có biết một con Hươu Cao Cổ nặng 2 tấn có thể bị nổ tung mạch nước màu não mỗi khi cúi đầu xuống đất uống nước không?!". Bố cục: chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất: cận cảnh hươu cao cổ cúi đầu uống nước đối diện nguy cơ nổ mạch nước màu não
```
</details>

<details><summary>S01b</summary>

```text
HÌNH S01b (9:16 dọc, bản vẽ kỹ thuật đường ống công nghiệp và thủy lực (Industrial Piping Schematic & Hydraulic Blueprint), nền xanh đậm blueprint kỹ thuật #0C1824, các đường nét sơ đồ phát sáng dạ quang cyan #00F0FF và cam neon #FF8800, chi tiết van áp lực và ống dẫn thủy lực, KHÔNG chữ, không logo). Áp lực máu dồn nén cực độ có nguy cơ làm vỡ toang mạch máu não của chú hươu cao cổ.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Hãy nhìn chiếc cổ dài 2m của Tháp Cẩu Di Động lừng lững giữa thảo nguyên này xem!". Bố cục: chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất: toàn cảnh hươu cao cổ 5 mét với thước đo cổ 2 mét vươn cao
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Để bơm nước màu đỏ ngược chiều trọng lực lên độ cao 5m, quả tim của nó nặng tới 11kg và tạo ra áp lực tâm thu 300 mmHg, gấp đôi người khỏe mạnh nhất!". Bố cục: mô hình quả tim thép 11kg với đồng hồ đo áp suất 300 mmHg: quả tim khổng lồ 11kg bơm áp lực tâm thu 300 mmHg
```
</details>

<details><summary>S03b</summary>

```text
HÌNH S03b (9:16 dọc, bản vẽ kỹ thuật đường ống công nghiệp và thủy lực (Industrial Piping Schematic & Hydraulic Blueprint), nền xanh đậm blueprint kỹ thuật #0C1824, các đường nét sơ đồ phát sáng dạ quang cyan #00F0FF và cam neon #FF8800, chi tiết van áp lực và ống dẫn thủy lực, KHÔNG chữ, không logo). Cận cảnh khối tim 11kg khổng lồ như một cỗ máy bơm công nghiệp tạo áp lực 300 mmHg.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Khi nó hạ đầu rơi tự do ba mét xuống vũng nước, áp suất dồn xuống não sẽ tăng vọt lên 500 mmHg, đủ để làm vỡ toang mạch nước màu ngay tức khắc!". Bố cục: chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất: hươu cúi đầu rơi tự do làm áp lực nước màu dồn xuống não tăng vọt 500 mmHg
```
</details>

<details><summary>S04b</summary>

```text
HÌNH S04b (9:16 dọc, bản vẽ kỹ thuật đường ống công nghiệp và thủy lực (Industrial Piping Schematic & Hydraulic Blueprint), nền xanh đậm blueprint kỹ thuật #0C1824, các đường nét sơ đồ phát sáng dạ quang cyan #00F0FF và cam neon #FF8800, chi tiết van áp lực và ống dẫn thủy lực, KHÔNG chữ, không logo). Cảnh báo áp suất đỉnh điểm 500 mmHg dồn xuống hộp sọ khi hạ đầu uống nước.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Nhưng kỳ diệu thay, dưới đáy hộp sọ của nó có một mạng lưới mạch nước màu xốp mang tên Rete Mirabile cùng chuỗi van một chiều cơ học.". Bố cục: sơ đồ mạng lưới vi mạch xốp giảm áp búa nước dưới đáy sọ: mạng lưới mạch nước màu xốp Rete Mirabile dưới đáy sọ hấp thụ xung lực búa nước
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Khi đầu chúi xuống, mạng lưới này lập tức phình to hấp thụ toàn bộ xung lực búa nước, triệt tiêu áp suất thừa!". Bố cục: chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất: chuỗi van một chiều tĩnh mạch cổ sập chặt ngăn nước màu đen trào ngược
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Chưa hết, cẳng chân của nó được bọc lớp da siêu căng như bộ đồ phi hành gia NASA, chống phù nề tuyệt đối!". Bố cục: chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất: so sánh chân hươu bọc màng cân cơ siêu căng với bộ đồ G-suit phi hành gia NASA
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, quy chuẩn minh họa nghệ thuật độc bản và nhân vật chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Đúng là một tuyệt tác cơ khí thủy lực đỉnh cao của tạo hóa!". Bố cục: chú hươu cao cổ hoạt hình ngộ nghĩnh đeo kính bảo hộ kỹ sư cầm đồng hồ áp suất kỹ sư trưởng mặc đồ bảo hộ xưởng cơ khí, cầm cờ lê và bản vẽ đường ống thủy lực: hươu cao cổ ngẩng cao đầu kiêu hãnh cùng kỹ sư trưởng giơ cúp chiến thắng
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/53 của video YouTube về Hươu Cao Cổ). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa vẽ tay đặc trưng cho chủ đề, nét mực sắc nét, màu sắc tương phản cuốn hút, tối giản giàu tính biểu tượng khoa học; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động). Nhân vật phụ cố định: kỹ sư trưởng mặc đồ bảo hộ xưởng cơ khí, cầm cờ lê và bản vẽ đường ống thủy lực; cô trợ lý kỹ thuật đeo kính bảo hộ cầm bảng kẹp tài liệu ghi chép áp suất; chú ngơ ngác gãi đầu hoảng hốt trước đồng hồ đo áp suất; bé con đội mũ safari đeo ba lô tò mò chỉ tay hỏi; sư tử châu phi bờm rậm hoảng hốt né đòn đạp hậu của hươu; mô hình quả tim thép 11kg với đồng hồ đo áp suất 300 mmHg; sơ đồ mạng lưới vi mạch xốp giảm áp búa nước dưới đáy sọ. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/8 của video YouTube Shorts về Hươu Cao Cổ). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa vẽ tay đặc trưng cho chủ đề, nét mực sắc nét, màu sắc tương phản cuốn hút, tối giản giàu tính biểu tượng khoa học; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú hươu cao cổ hoạt hình ngộ nghĩnh (cao lớn, cổ dài 2m với các van thủy lực phát sáng, biểu cảm sinh động). Nhân vật phụ: kỹ sư trưởng mặc đồ bảo hộ xưởng cơ khí, cầm cờ lê và bản vẽ đường ống thủy lực; mô hình quả tim thép 11kg với đồng hồ đo áp suất 300 mmHg; sơ đồ mạng lưới vi mạch xốp giảm áp búa nước dưới đáy sọ. 
```
</details>

## 7. SEO

- **title:** Bí Ẩn Cổ Dài 2 Mét: Cúi Đầu Uống Nước Sao Không Bị Nổ Não?! | Hươu Cao Cổ | Tập 47
- **hook_paragraph:** Hươu Cao Cổ cao hơn 5m với chiếc cổ dài 2m sở hữu trái tim nặng 11kg và huyết áp 300 mmHg gấp đôi con người. Làm thế nào mạng lưới xả áp Rete Mirabile cứu nó thoát khỏi thảm cảnh nổ mạch máu não mỗi khi cúi đầu?
- **question:** Bạn thấy cơ chế nào của Hươu Cao Cổ đỉnh cao nhất: Động cơ tim 11kg hay mạng lưới xả áp Rete Mirabile?
- **next_teaser:** Ở tập tiếp theo, chúng ta sẽ diện kiến tượng đá đầm lầy Cò Mỏ Giày với tiếng gõ mỏ như súng máy liên thanh!
- **shorts_title:** Cúi đầu 2m uống nước: Sao hươu cao cổ không bị nổ não?! 🦒 #shorts #huoucaco
- **shorts_desc:** Hươu cao cổ sở hữu huyết áp 300 mmHg gấp đôi con người nhưng cúi cổ 2m uống nước lại không bị nổ mạch máu não nhờ mạng lưới Rete Mirabile kỳ diệu!
- **bullets:** Trái tim 11kg với áp lực máu 300 mmHg bơm máu leo dốc 2m · Mạng lưới kỳ diệu Rete Mirabile hấp thụ áp suất cực hạn khi cúi đầu · Lớp da cẳng chân bó chặt như bộ đồ phi hành gia chống phù nề · Đòn quăng cổ búa tạ Necking đạt vận tốc 100km/h hạ gục đối thủ
- **tags:** hươu cao cổ, huou cao co, giraffe, tim huou cao co, rete mirabile, the gioi dong vat, ve chuyen hoang da, dong vat ky thu, khoa hoc vui, giai ma dong vat, ky su vu khi, ap suat mau
- **hashtags:** #HuouCaoCo #TheGioiDongVat #VeChuyenHoangDa #KhoaHoc #DongVatKyThu #KySuVuKhi

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-47-huou-cao-co
python src/episode/pipeline.py tts    projects/tap-47-huou-cao-co     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-47-huou-cao-co     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-47-huou-cao-co     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-47-huou-cao-co              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-47-huou-cao-co --force
python scripts/beat_sheet.py projects/tap-47-huou-cao-co               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-47-huou-cao-co/audio/shorts.wav projects/tap-47-huou-cao-co/renders/tap-47-huou-cao-co_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-47-huou-cao-co
python src/episode/pipeline.py seo    projects/tap-47-huou-cao-co
python src/episode/episode_doc.py     projects/tap-47-huou-cao-co
```
