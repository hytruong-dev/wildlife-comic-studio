# TẬP 31 — CHIM CẮT LỚN · TÀI LIỆU SẢN XUẤT ĐẦY ĐỦ (`tap-31-chim-cat-lon`)

> Tài liệu sinh tự động từ dữ liệu thật của tập bằng `python src/episode/episode_doc.py projects/tap-31-chim-cat-lon`.
> Dùng nó làm **khuôn mẫu đối chiếu** khi làm lại/làm tập mới: mỗi câu thoại ↔ 1 hình ↔ 1 prompt ↔ sticker chỉ đúng chi tiết.
> Quy trình chuẩn: `.agents/skills/core/episode-production/SKILL.md` · Hướng dẫn tổng: `docs/QUY_TRINH_SAN_XUAT_TAP_CHUAN.md`.

> **Format kể chuyện:** `F2` · **Persona giọng:** `ky_su_vu_khi` (`docs/strategy/FORMAT_KE_CHUYEN.md`, `docs/HE_THONG_GIONG_DOC_DA_PHONG_CACH.md`).

## 1. Tổng quan & kết quả

| Mục | Giá trị |
|---|---|
| Con vật | Chim Cắt Lớn |
| Tiêu đề YouTube | Sinh Vật Bổ Nhào 389 km/h & Nón Nén Khí Chống Nổ Phổi?! \| Tập 31 |
| Video dài | `renders/tap-31-chim-cat-lon_long.mp4` — 8:48.0 (528.0s) |
| Shorts | `renders/tap-31-chim-cat-lon_shorts.mp4` — 0:52.5 (52.5s) |
| Thumbnail | `renders/tap-31-chim-cat-lon_thumbnail.jpg` |
| Số hình | dài 54 beat / 54 ảnh riêng; Shorts 13 beat |
| Giọng | VoiceStudio OmniVoice, clone `assets/voice_refs/adam_funny_ep1.wav`, speed 1.05, steps 32, **tempo dài 1.1**, Shorts tempo tự tính (≥ 1.1) |
| Thời lượng tối thiểu video dài | 08:30.0 (TASTE-61) |

## 2. Nhân vật & quy chuẩn hình

Prompt mở đầu chat Gemini (quy chuẩn chung + nhân vật cố định) đã dùng thật:

```text
Tạo hình ảnh (cảnh 1/54 của video YouTube về Chim Cắt Lớn). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles). Nhân vật phụ cố định: chú chim bồ câu hoạt hình lông xám mập mạp ngơ ngác, cầm máy đo tốc độ đồ chơi màu vàng; cô trợ lý sóc hoạt hình đeo kính cận to tròn, mặc áo blouse trắng phòng thí nghiệm, cầm bản vẽ blueprint khí động học; chú báo săn cheetah hoạt hình màu vàng đốm đen, đi giày thể thao đỏ, đang thở dốc ôm đầu gối mệt mỏi; chú phi công gấu hoạt hình mặc đồ bay G-suit màu xanh, mặt tái mét ôm túi nôn ngộ nghĩnh. 
```

Prompt các hình sau theo mẫu: `HÌNH Lxx (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật …; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Lời thoại: "<câu>". Bố cục: <TRÁI/GIỮA/PHẢI, ai làm gì, biểu cảm, đạo cụ hình ảnh hóa con số>`

## 3. Lời đọc đưa vào VoiceStudio (nguyên văn, có tag cảm xúc)

Tag chỉ dành cho giọng đọc, **không bao giờ hiện trên phụ đề** (pipeline tự bỏ). Số đọc bằng chữ, phụ đề hiện số qua `display_fix`.

### scene01 — TIÊM KÍCH LÔNG VŨ ĐẠT KỶ LỤC 389 KM/H BỔ NHÀO XÉ TOẠC BẦU TRỜI
*Thẻ chương:* HỒ SƠ MẬT CẤP ĐỘ ĐỎ: KỶ LỤC TỐC ĐỘ NHANH NHẤT HÀNH TINH

*Badge:* `HỒ SƠ MẬT` · *mood mặc định:* `tram_bi_an`

**Part 0** → `audio/vs/scene01_p0.wav` (409 ký tự) · mood `tram_bi_an`

```text
Hồ sơ mật cấp độ đỏ. Mở khóa! Chào mừng toàn thể đội ngũ kỹ thuật quay trở lại phòng nghiên cứu vũ khí sinh học. Hôm nay chúng ta giải mật một cỗ máy bay không người lái tự nhiên có tốc độ kinh hoàng nhất lịch sử tiến hóa: Chim Cắt Lớn, danh pháp khoa học Phan-cô Pê-rê-gri-nút. Nếu bạn nghĩ báo hoa mai chạy một trăm ki-lô-mét một giờ đã là đỉnh chóp, thì cỗ máy này sẽ biến báo đốm thành một trò đùa rùa bò.
```
**Part 1** → `audio/vs/scene01_p1.wav` (136 ký tự) · 🎭 cameo `phat_thanh_vien`

```text
Báo cáo radar phòng không: Phát hiện vật thể lạ bổ nhào từ độ cao năm ngàn mét! Vận tốc đo được ba trăm tám mươi chín ki-lô-mét một giờ!
```
**Part 2** → `audio/vs/scene01_p2.wav` (568 ký tự) · mood `hao_hung`

```text
[surprise-oh] Ba trăm tám mươi chín ki-lô-mét một giờ! Đúng vậy các đồng chí, đây không phải thông số chém gió trong phim viễn tưởng. Năm hai ngàn không trăm linh năm, phi công nhảy dù Ken Phơ-răng-clin đã cùng chú chim cắt mang tên Phrai-phun thực hiện một cú nhảy từ máy bay ở độ cao năm ngàn mét. Khi Ken nhảy dù tự do, chú chim cắt gập cánh lao theo và thiết bị đo gắn trên đuôi chim đã chạm mốc không tưởng: ba trăm tám mươi chín ki-lô-mét một giờ! Tốc độ này nhanh hơn cả xe đua công thức một ép một và vượt xa mọi phương tiện giao thông trên mặt đất! [laughter]
```
**Part 3** → `audio/vs/scene01_p3.wav` (391 ký tự) · mood `don_dap`

```text
Nhưng khoan đã các kỹ sư. Ở tốc độ gần bốn trăm ki-lô-mét một giờ, theo định luật vật lý cơ bản, bất kỳ sinh vật bình thường nào cũng sẽ bị luồng gió nén cực mạnh xé toạc màng nhĩ, rách toạc giác mạc và thổi nổ tung hai lá phổi ngay trên không trung! Vậy bản thiết kế giải phẫu của Tiêm Kích Lông Vũ này giấu những linh kiện tối mật gì? Mời đội kỹ thuật bước ngay vào bóc tách bản vẽ cơ khí!
```

### scene02 — NÓN GIẢM ÁP NẸP MŨI CHỐNG NỔ PHỔI VÀ KÍNH BẢO HỘ SINH HỌC
*Thẻ chương:* BẢN VẼ KỸ THUẬT: CƠ CHẾ NÉN KHÍ VÀ MÀNG BẢO VỆ MẮT SIÊU THANH

*Badge:* `BẢN VẼ CƠ KHÍ` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene02_p0.wav` (358 ký tự) · mood `hao_hung`

```text
Bản vẽ kỹ thuật tầng một: Hệ thống điều hòa áp suất khí quyển. Các bạn hãy nhìn thẳng vào lỗ mũi của Chim Cắt Lớn. Bình thường lỗ mũi chim chỉ là một cái khe trơn nhẵn, nhưng ở Tiêm Kích Lông Vũ, ngay chính giữa mỗi lỗ mũi lại mọc ra một nón xương nhô lên hình xoắn ốc gọi là tu-béc-cơ. Đây chính là kiệt tác khí động học trị giá triệu đô của mẹ thiên nhiên!
```
**Part 1** → `audio/vs/scene02_p1.wav` (480 ký tự) · mood `don_dap`

```text
Khi chim cắt bổ nhào với vận tốc ba trăm tám mươi chín ki-lô-mét một giờ, luồng không khí dội vào mũi với áp lực khổng lồ. Nếu không có vật cản, luồng khí nén này sẽ tràn thẳng vào khí quản như một quả bom nổ chậm, làm vỡ tan các phế nang phổi trong nửa giây. Nhưng chiếc nón tu-béc-cơ đóng vai trò như một van giảm chấn siêu cấp, chia nhỏ luồng gió thành các xoáy khí chậm dần, giúp chim hít thở êm ái như đang ngồi uống trà sữa ở vận tốc ba trăm ki-lô-mét một giờ! [surprise-wa]
```
**Part 2** → `audio/vs/scene02_p2.wav` (254 ký tự) · mood `tram_bi_an`

```text
Chi tiết này thông minh đến mức các kỹ sư hàng không vũ trụ khi thiết kế động cơ phản lực cho siêu máy bay do thám ét-sơ-rờ bảy mươi mốt Bờ-lách-bớt đã phải mô phỏng y hệt chiếc nón giảm áp này ở cửa hút gió để động cơ không bị nghẹt khí khi bay siêu âm!
```
**Part 3** → `audio/vs/scene02_p3.wav` (648 ký tự) · mood `hao_hung`

```text
Bản vẽ kỹ thuật tầng hai: Cánh khí động học chống rung gãy. Toàn bộ bộ lông của chim cắt được phủ một lớp vảy vi mô đặc biệt. Khi chim gập cánh tạo hình lưỡi liềm, các hàng lông cánh tự động khóa chặt vào nhau thành một bề mặt cứng cáp liền khối, triệt tiêu hoàn toàn hiện tượng rung lắc khí động học vốn có thể xé toạc đôi cánh của những loài chim thông thường! Không chỉ có vậy, ở chóp cánh chim cắt còn có các sợi lông tơ đóng vai trò như cảm biến vi chấn. Khi phát hiện luồng khí nhiễu loạn ở rìa cánh, các sợi lông này lập tức dựng đứng lên một góc nhỏ để tái định hướng dòng khí, giống hệt như cánh nhỏ ở đầu cánh của máy bay Bo-ing hiện đại!
```
**Part 4** → `audio/vs/scene02_p4.wav` (426 ký tự) · mood `hao_hung`

```text
Chưa hết đâu đội kỹ thuật! Khi lao qua tầng mây với vận tốc tên lửa, bụi cát và gió lốc sẽ cào xước mắt bạn ra sao? Chim cắt không hề lo chuyện đó vì nó sở hữu một mí mắt thứ ba trong suốt, tựa như một chiếc kính bảo hộ sinh học. Mí mắt này quét ngang nhấp nháy liên tục, vừa bôi trơn nước mắt chống khô rát, vừa đóng vai trò như kính chắn gió trong suốt cho phép chim nhìn rõ từng cọng lông của con mồi mà không cần chớp mắt!
```

### scene03 — HỐC MẮT ĐÔI FOVEA VÀ QUỸ ĐẠO BAY XOẮN ỐC LOGARIT
*Thẻ chương:* HỆ THỐNG NGẮM BẮN: QUỸ ĐẠO XOẮN ỐC LOGARIT KHÓA MỤC TIÊU CÁCH 3KM

*Badge:* `HỆ THỐNG RADAR` · *mood mặc định:* `don_dap`

**Part 0** → `audio/vs/scene03_p0.wav` (401 ký tự) · mood `don_dap`

```text
Chuyển sang bản vẽ tầng ba: Hệ thống ngắm bắn và cảm biến quang học tầm xa. Đôi mắt của Chim Cắt Lớn chiếm tới gần nửa trọng lượng hộp sọ. Trong khi mắt người chỉ có một điểm vàng hội tụ ánh sáng sắc nét nhất, thì mắt chim cắt lại trang bị hẳn hai hốc mắt sâu gọi là pho-ve-a đôi: một hốc nhìn thẳng để định vị cự ly và một hốc nhìn xéo sang hai bên với độ phân giải siêu nét gấp tám lần mắt phi công!
```
**Part 1** → `audio/vs/scene03_p1.wav` (121 ký tự) · 🎭 cameo `phat_thanh_vien`

```text
Cảm biến quang học báo cáo: Khóa mục tiêu là một chú bồ câu béo múp ở khoảng cách ba ki-lô-mét! Tọa độ đã lưu vào bộ nhớ!
```
**Part 2** → `audio/vs/scene03_p2.wav` (436 ký tự) · mood `hao_hung`

```text
[laughter] Nhìn thấy mục tiêu cách ba ki-lô-mét là một chuyện, nhưng làm sao để lao xuống đớp mồi lại nảy sinh một nghịch lý vật lý vô cùng đau đầu. Giáo sư Van-xơ Tắc-cơ thuộc Đại học Duke qua các bài báo trên tạp chí Thực nghiệm Sinh học đã phát hiện ra bí mật chấn động: Hốc mắt nhìn nét nhất của chim cắt nằm lệch một góc bốn mươi độ sang bên cạnh. Nếu chim bay thẳng tắp cắm đầu xuống, nó sẽ phải ngoẹo cổ sang một bên để nhìn mồi!
```
**Part 3** → `audio/vs/scene03_p3.wav` (538 ký tự) · mood `tram_bi_an`

```text
Mà các kỹ sư biết đấy, đang lao ba trăm ki-lô-mét một giờ mà ngoẹo đầu sang bên thì lực cản gió sẽ bẻ gãy cổ hoặc làm chim xoay mòng mòng mất lái ngay lập tức! Để giải bài toán hóc búa này, Tiêm Kích Lông Vũ đã lập trình sẵn trong não bộ một đường bay xoắn ốc logarit hoàn hảo. Nó giữ đầu thẳng tắp để triệt tiêu tối đa lực cản, đồng thời nghiêng thân lượn theo một đường cong hình học chính xác tuyệt đối, giữ cho mắt luôn nhìn chằm chằm vào con mồi suốt từ độ cao ba ngàn mét xuống đất! Quả là một thuật toán dẫn đường tên lửa đỉnh cao!
```
**Part 4** → `audio/vs/scene03_p4.wav` (372 ký tự) · mood `hao_hung`

```text
Đặc biệt hơn nữa, não bộ của chim cắt xử lý hình ảnh với tần số lên tới một trăm ba mươi khung hình một giây, cao hơn gấp đôi mức sáu mươi khung hình một giây của con người! Nhờ khả năng siêu xử lý này, toàn bộ quỹ đạo của con mồi bay lượn bên dưới đều hiện ra như những cảnh quay chậm chậm rãi, cho phép chim cắt căn chỉnh góc tấn công mượt mà như trong trò chơi điện tử!
```

### scene04 — CÚ KÉO LÊN 25G VÀ NẮM ĐẤM MÓNG VUỐT HẠ GỤC CON MỒI
*Thẻ chương:* THỰC CHIẾN TÀN KHỐC: CHỊU ĐỰNG GIA TỐC 25G VÀ CÚ VA CHẠM KINH HOÀNG

*Badge:* `ĐÒN THỰC CHIẾN` · *mood mặc định:* `hao_hung`

**Part 0** → `audio/vs/scene04_p0.wav` (377 ký tự) · mood `hao_hung`

```text
Bây giờ, mời đội kỹ thuật chứng kiến khoảnh khắc khai hỏa đòn tấn công thực chiến. Khi đã áp sát con mồi ở cự ly ba trăm mét, chim cắt gập chặt hai cánh vào sát thân mình, biến toàn bộ cơ thể thành một viên đạn hình giọt nước khí động học hoàn hảo. Lúc này, tim của nó đập điên cuồng từ sáu trăm đến chín trăm nhịp một phút để bơm oxy tới từng thớ cơ ngực săn chắc như đá tảng.
```
**Part 1** → `audio/vs/scene04_p1.wav` (358 ký tự) · mood `don_dap`

```text
Nhưng điều đáng kinh ngạc nhất nằm ở cách nó hạ gục con mồi. Nó không hề xòe móng ra để quắp như đại bàng hay diều hâu. Ở vận tốc ba trăm ki-lô-mét một giờ, nếu xòe móng quắp mồi, quán tính dữ dội sẽ bẻ gãy ngón chân chim cắt ngay lập tức! Thay vào đó, nó cuộn tròn các ngón chân lại thành một nắm đấm đặc sệt bọc sừng, biến thành một quả đấm thép bay tự do!
```
**Part 2** → `audio/vs/scene04_p2.wav` (399 ký tự) · mood `hao_hung`

```text
Rầm! Nắm đấm móng vuốt giáng thẳng vào lưng hoặc cánh của con mồi với động năng tương đương một viên đạn chì bắn ra từ súng hơi. Hãy tưởng tượng một quả tạ kim loại nặng gần một ki-lô-gam đập thẳng vào bạn ở tốc độ ba trăm ki-lô-mét một giờ! Cú va chạm kinh hoàng làm con mồi gãy cổ rụng rơi tự do trong không trung, trước khi chim cắt lộn một vòng ngoạn mục để đón lấy chiến lợi phẩm giữa tầng mây!
```
**Part 3** → `audio/vs/scene04_p3.wav` (266 ký tự) · mood `don_dap`

```text
Ngay sau cú va chạm nổ tung, chim cắt phải thực hiện một động tác hãm phanh kéo ngược cơ thể lên trên không trung. Đây chính là thời khắc sinh tử: Nếu tính toán sai chỉ một phần mười giây không phẩy một giây, nó sẽ cắm thẳng đầu xuống đất và nát vụn thành trăm mảnh!
```
**Part 4** → `audio/vs/scene04_p4.wav` (406 ký tự) · mood `don_dap`

```text
[surprise-oh] Và hãy nhìn vào thông số gia tốc kéo lên: Hai mươi lăm G! Một phi công lái máy bay chiến đấu hiện đại nhất chỉ chịu được tối đa chín G trong vài giây là mạch máu tụ xuống chân, mắt tối sầm ngất xỉu. Ấy thế mà Tiêm Kích Lông Vũ chịu đựng hai mươi lăm G mà mắt vẫn sáng quắc, đầu vẫn tỉnh queo! Khung xương đòn chữ V liền khối của nó cứng vững gấp mười lần vật liệu hợp kim nhân tạo! [laughter]
```

### scene05 — DÁNG ĐI VỤNG VỀ DƯỚI MẶT ĐẤT VÀ CUỘC KHỦNG HOẢNG DDT
*Thẻ chương:* ĐIỂM YẾU BẤT NGỜ: TIÊM KÍCH VỤNG VỀ TRÊN MẶT ĐẤT VÀ HIỂM HỌA TUYỆT CHỦNG

*Badge:* `TỬ HUYỆT VŨ KHÍ` · *mood mặc định:* `bi_hai`

**Part 0** → `audio/vs/scene05_p0.wav` (275 ký tự) · mood `bi_hai`

```text
Thưa các kỹ sư, theo đúng quy chuẩn báo cáo hồ sơ vũ khí ép hai, không có vũ khí nào là hoàn hảo tuyệt đối. Mọi cỗ máy tối tân đều phải đánh đổi bằng những điểm yếu kỹ thuật dở khóc dở cười. Điểm yếu thứ nhất của Chim Cắt Lớn chính là: Đừng bao giờ bắt nó đi bộ dưới mặt đất!
```
**Part 1** → `audio/vs/scene05_p1.wav` (481 ký tự) · mood `hao_hung`

```text
Vì toàn bộ thiết kế tiến hóa dồn hết cho việc bay liệng siêu tốc, đôi chân của chim cắt rất ngắn, cơ đùi yếu và móng vuốt quá cong dài. Khi hạ cánh xuống bãi cỏ, từ một tiêm kích bầu trời oai phong lẫm liệt, nó bỗng biến hình thành một chú bồ câu say rượu đi lạch bạch vụng về, nhảy chồm chồm như vừa dẫm phải đinh! Nếu con mồi chạy ngoằn ngoèo trong bụi rậm dưới đất, tỷ lệ tóm mồi của chim cắt tụt dốc thê thảm từ chín mươi phần trăm xuống dưới hai mươi lăm phần trăm! [laughter]
```
**Part 2** → `audio/vs/scene05_p2.wav` (229 ký tự) · mood `bi_hai`

```text
Chưa dừng lại ở đó, kỹ năng cận chiến trên mặt đất của nó tệ đến mức thường xuyên bị quạ đen, hải âu hay bồ nông nhảy vào bắt nạt và cướp trắng bữa ăn vừa săn được, khiến sát thủ siêu thanh chỉ biết đứng trơ mắt nhìn đầy bất lực!
```
**Part 3** → `audio/vs/scene05_p3.wav` (360 ký tự) · mood `tram_bi_an`

```text
Nhưng bi kịch đen tối nhất trong lịch sử của Tiêm Kích Lông Vũ lại không đến từ thiên địch tự nhiên, mà đến từ một hóa chất vô hình do con người tạo ra vào thập niên một ngàn chín trăm sáu mươi: Thuốc trừ sâu Đê Đê Tê. Khi chim cắt ăn các loài chim nhỏ tích tụ hóa chất này, chất độc phá hủy cơ chế chuyển hóa canxi, khiến vỏ trứng chim cắt mỏng đi trông thấy.
```
**Part 4** → `audio/vs/scene05_p4.wav` (303 ký tự) · mood `tram_bi_an`

```text
Hậu quả là mỗi khi chim bố mẹ ấp trứng, chính sức nặng cơ thể chúng lại vô tình đè bẹp nát những đứa con chưa kịp chào đời. Toàn bộ quần thể chim cắt ở Bắc Mỹ và châu Âu sụt giảm nghiêm trọng đến mức suýt bị xóa sổ vĩnh viễn khỏi bản đồ sinh học, gióng lên hồi chuông cảnh tỉnh đau đớn cho cả nhân loại!
```

### scene06 — BÀI HỌC PHỤC HỒI VÀ CÂU ĐỐ BÓNG ĐEN QUÁI KIỆT TẬP 32
*Thẻ chương:* TỔNG KẾT HỒ SƠ: SỰ HỒI SINH NGOẠN MỤC VÀ DỰ BÁO TẬP KẾ TIẾP

*Badge:* `NGHIỆM THU HỒ SƠ` · *mood mặc định:* `am_ap`

**Part 0** → `audio/vs/scene06_p0.wav` (392 ký tự) · mood `am_ap`

```text
May mắn thay, chiến dịch bảo tồn quy mô toàn cầu sau lệnh cấm Đê Đê Tê năm một ngàn chín trăm bảy mươi hai đã tạo nên một kỳ tích phục hồi ngoạn mục. Các nhà khoa học đã nhân giống thả chim về tự nhiên, và giờ đây Tiêm Kích Lông Vũ lại kiêu hãnh chao lượn trên bầu trời các tòa nhà chọc trời từ Nữu Ước tới Luân Đôn, biến nó thành biểu tượng bất diệt cho khả năng phục hồi của mẹ thiên nhiên.
```
**Part 1** → `audio/vs/scene06_p1.wav` (117 ký tự) · 🎭 cameo `phat_thanh_vien`

```text
Báo cáo nghiệm thu kỹ thuật: Vũ khí siêu thanh hoàn toàn đạt chuẩn! Đề nghị lưu trữ vào kho dữ liệu khoa học bảo tồn!
```
**Part 2** → `audio/vs/scene06_p2.wav` (250 ký tự) · mood `hao_hung`

```text
Đội kỹ thuật thân mến, bạn thấy ấn tượng nhất với trang bị nào của Chim Cắt Lớn: Nón xương chống nổ phổi trong lỗ mũi, hốc mắt đôi xoắn ốc logarit hay quả đấm thép chịu gia lực hai mươi lăm G? Hãy để lại bình luận phân tích của bạn ngay bên dưới nhé!
```
**Part 3** → `audio/vs/scene06_p3.wav` (482 ký tự) · mood `tram_bi_an`

```text
Và ngay trong hồ sơ giải mật tập ba mươi hai tiếp theo, chúng ta sẽ rời bầu trời cao vời vợi để chui sâu xuống lòng đất tối tăm, gặp gỡ một bóng đen bí ẩn dị hợm bậc nhất hành tinh! Sinh vật này hoàn toàn trụi lông, da nhăn nheo như củ khoai tây luộc, không hề biết cảm giác đau đớn trước axit đậm đặc và sở hữu bộ gen miễn nhiễm ung thư kỳ diệu giúp nó sống thọ tới hơn ba mươi năm, gấp mười lần họ hàng loài gặm nhấm! Đố các kỹ sư đoán được bóng đen quái kiệt tiếp theo này là ai?
```

### Shorts → `audio/vs/shorts.wav`

```text
Hồ sơ mật cấp độ đỏ. Mở khóa! [surprise-oh] Tại sao khi lao xuống từ độ cao năm ngàn mét với vận tốc ba trăm tám mươi chín ki-lô-mét một giờ, hai lá phổi của Chim Cắt Lớn không hề bị nổ tung? Đây chính là Tiêm Kích Lông Vũ, sinh vật bay nhanh nhất lịch sử hành tinh chúng ta! Ở tốc độ khủng khiếp gần bốn trăm ki-lô-mét một giờ, áp lực không khí mạnh đến mức có thể thổi rách toạc khí quản của bất kỳ con thú nào. Nhưng mẹ thiên nhiên đã bí mật lắp đặt ngay trong lỗ mũi chim cắt một chiếc nón xương xoắn ốc tí hon gọi là tu-béc-cơ. Chiếc nón giảm áp này chia nhỏ luồng gió nén thành các xoáy khí chậm, giúp chim hít thở êm ái như đang ngồi hóng gió mát! Đến cả siêu máy bay do thám ét-sơ-rờ bảy mươi mốt Bờ-lách-bớt của con người cũng phải học lỏm thiết kế nón cản sốc này để bay siêu âm. Chưa hết, chim cắt còn cuộn ngón chân thành quả đấm thép giáng thẳng vào con mồi, chịu gia lực tới hai mươi lăm G mà mắt vẫn tỉnh queo! Một kiệt tác khí động học đỉnh chóp của tự nhiên!
```

**Whisper prompt:** `Chim Cắt Lớn, Tiêm Kích Lông Vũ, Falco peregrinus, Ken Franklin, Frightful, Vance Tucker, SR-71, Blackbird, 389 km/h, 400 km/h, 300 km/h, 200 km/h, 100 km/h, 25G, 9G, 5.000m, 3.000m, 3km, 300m, 40 độ, 600 nhịp/phút, 900 nhịp/phút, 130 khung hình/giây, 60 khung hình/giây, tubercle, fovea, DDT, Chuột Chũi Trũi`

**display_fix (chữ đọc → chữ hiện trên phụ đề):**

| Lời đọc | Phụ đề |
|---|---|
| ba trăm tám mươi chín ki-lô-mét một giờ | 389 km/h |
| Ba trăm tám mươi chín ki-lô-mét một giờ | 389 km/h |
| ba trăm tám chín ki-lô-mét một giờ | 389 km/h |
| Ba trăm tám chín ki-lô-mét một giờ | 389 km/h |
| gần bốn trăm ki-lô-mét một giờ | gần 400 km/h |
| Gần bốn trăm ki-lô-mét một giờ | gần 400 km/h |
| bốn trăm ki-lô-mét một giờ | 400 km/h |
| Bốn trăm ki-lô-mét một giờ | 400 km/h |
| ba trăm ki-lô-mét một giờ | 300 km/h |
| Ba trăm ki-lô-mét một giờ | 300 km/h |
| hai trăm ki-lô-mét một giờ | 200 km/h |
| Hai trăm ki-lô-mét một giờ | 200 km/h |
| một trăm ki-lô-mét một giờ | 100 km/h |
| Một trăm ki-lô-mét một giờ | 100 km/h |
| năm ngàn mét | 5.000m |
| Năm ngàn mét | 5.000m |
| năm nghìn mét | 5.000m |
| Năm nghìn mét | 5.000m |
| ba ngàn mét | 3.000m |
| Ba ngàn mét | 3.000m |
| ba ki-lô-mét | 3km |
| Ba ki-lô-mét | 3km |
| ba trăm mét | 300m |
| Ba trăm mét | 300m |
| hai mươi lăm G | 25G |
| Hai mươi lăm G | 25G |
| chín G | 9G |
| Chín G | 9G |
| sáu trăm đến chín trăm nhịp một phút | 600-900 nhịp/phút |
| Sáu trăm đến chín trăm nhịp một phút | 600-900 nhịp/phút |
| một trăm ba mươi khung hình một giây | 130 khung hình/giây |
| Một trăm ba mươi khung hình một giây | 130 khung hình/giây |
| sáu mươi khung hình một giây | 60 khung hình/giây |
| Sáu mươi khung hình một giây | 60 khung hình/giây |
| bốn mươi độ | 40 độ |
| Bốn mươi độ | 40 độ |
| nửa giây | 0,5 giây |
| Nửa giây | 0,5 giây |
| không phẩy một giây | 0,1 giây |
| Không phẩy một giây | 0,1 giây |
| hai mươi lăm phần trăm | 25% |
| Hai mươi lăm phần trăm | 25% |
| chín mươi phần trăm | 90% |
| Chín mươi phần trăm | 90% |
| năm hai ngàn không trăm linh năm | năm 2005 |
| Năm hai ngàn không trăm linh năm | Năm 2005 |
| thập niên một ngàn chín trăm sáu mươi | thập niên 1960 |
| Thập niên một ngàn chín trăm sáu mươi | Thập niên 1960 |
| năm một ngàn chín trăm bảy mươi hai | năm 1972 |
| Năm một ngàn chín trăm bảy mươi hai | Năm 1972 |
| tập ba mươi hai | Tập 32 |
| Tập ba mươi hai | Tập 32 |
| ba mươi hai | 32 |
| Ba mươi hai | 32 |
| ba mươi năm | 30 năm |
| Ba mươi năm | 30 năm |
| mười lần | 10 lần |
| Mười lần | 10 lần |
| tám lần | 8 lần |
| Tám lần | 8 lần |
| một ki-lô-gam | 1kg |
| Một ki-lô-gam | 1kg |
| Bo-ing | Boeing |
| Phan-cô Pê-rê-gri-nút | Falco peregrinus |
| Ken Phơ-răng-clin | Ken Franklin |
| Phrai-phun | Frightful |
| Van-xơ Tắc-cơ | Vance Tucker |
| Đê Đê Tê | DDT |
| ép một | F1 |
| Ép một | F1 |
| ép hai | F2 |
| Ép hai | F2 |
| ét-sơ-rờ bảy mươi mốt | SR-71 |
| Bờ-lách-bớt | Blackbird |
| pho-ve-a | fovea |
| tu-béc-cơ | tubercle |

## 4. Phân cảnh video dài — từng beat

Cột *Lời thoại lúc hình hiện* lấy từ `audio/long_words_fixed.json` (đúng những chữ giọng đọc nói khi hình trên màn hình). Sticker: `giá trị · nhãn · bên/y · target[x,y]` (tỉ lệ 0..1 trên ảnh gốc, là điểm mũi tên chỉ vào).

### scene01 · TIÊM KÍCH LÔNG VŨ ĐẠT KỶ LỤC 389 KM/H BỔ NHÀO XÉ TOẠC BẦU TRỜI · 74.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:02.4 (2.4s) | L01 | Hồ sơ mật cấp độ đỏ. Mở |  | Phòng nghiên cứu khí động học công nghệ cao: một tập hồ sơ tài liệu đóng dấu đỏ tươi 'BÁO CÁO GIẢI MÃ SỐ 31' đặt giữa bàn kính, màn hình lớn phía sau hiển thị bầu trời mây trắng bao la. KHÔNG có chú Chim Cắt Lớn trong cảnh này. |
| b02 | 00:02.4–00:10.6 (8.1s) | L02 | khóa! Chào mừng toàn thể đội ngũ kỹ thuật quay trở lại phòng nghiên cứu vũ khí sinh học. Hôm nay chúng ta giải mật một cỗ máy bay không người lái tự nhiên có tốc độ kinh hoàng nhất lịch sử tiến hóa: |  | Phòng thí nghiệm khoa học vui nhộn: cô trợ lý sóc hoạt hình đeo kính cận to tròn, mặc áo blouse trắng phòng thí nghiệm, cầm bản vẽ blueprint khí động học đang gõ bàn phím máy tính phân tích biểu đồ khí động học, bên cạnh là mô hình máy bay phản lực đồ chơi. KHÔNG có chú Chim Cắt Lớn trong cảnh này. |
| b03 | 00:10.6–00:13.3 (2.7s) | L03 | Chim Cắt Lớn, danh pháp khoa học Falco peregrinus. |  | Chân dung oai phong của chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) đứng trên đỉnh vách đá cheo leo, bộ lông xám bạc óng ả, ngực ưỡn tự tin nhìn về phía đường chân trời rực nắng. |
| b04 | 00:13.3–00:20.0 (6.8s) | L04 | Nếu bạn nghĩ báo hoa mai chạy 100 km/h đã là đỉnh chóp, thì cỗ máy này sẽ biến báo đốm thành một trò đùa rùa bò. | **100 km/h** · báo săn chạy bộ · R/360 · [0.75, 0.55] | Đường đua đồng cỏ savan châu Phi: chú báo săn cheetah hoạt hình màu vàng đốm đen, đi giày thể thao đỏ, đang thở dốc ôm đầu gối mệt mỏi đang vừa chạy vừa lè lưỡi thở dốc, đồng hồ đo tốc độ hiện 100 km/h, nhưng trên bầu trời cao chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and fl |
| b05 | 00:20.0–00:27.2 (7.2s) | L05 | Báo cáo radar phòng không: Phát hiện vật thể lạ bổ nhào từ độ cao 5.000m! Vận tốc đo được 389 km/h! | **5.000m** · độ cao bổ nhào · L/360 · [0.3, 0.55] | Trạm quan sát radar trên đài chỉ huy: màn hình radar quét xanh lá cây nhấp nháy một chấm sáng đỏ lao vun vút từ độ cao 5.000m xuống với góc bổ nhào dựng đứng. KHÔNG có chú Chim Cắt Lớn trong cảnh này. |
| b06 | 00:27.2–00:34.0 (6.8s) | L06 | 389 km/h! Đúng vậy các đồng chí, đây không phải thông số chém gió trong phim viễn tưởng. | **389 km/h** · kỷ lục bổ nhào · R/360 · [0.75, 0.55] | Bầu trời xanh mây trắng cuộn sóng: chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) gập cánh bổ nhào cực nhanh xé toạc các đám mây, phía sau là vệt sóng âm khí động học màu cam rực rỡ, kèm bảng số đo điện tử hiện số khổng lồ '389 km/h'. |
| b07 | 00:34.0–00:42.2 (8.2s) | L07 | Năm 2005, phi công nhảy dù Ken Franklin đã cùng chú chim cắt mang tên Frightful thực hiện một cú nhảy từ máy bay ở độ cao 5.000m. | **Năm 2005** · thử nghiệm lịch sử · L/360 · [0.3, 0.55] | Thí nghiệm thực địa năm 2005: Một chuyên gia nhảy dù mặc đồ bảo hộ lượn giữa tầng mây, bên cạnh là chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) đang lao vút song song với thiết bị máy đo vi cơ gắn gọn gàng ở đuôi lông chim. chú Chim Cắt Lớn hoạt hình lông ng |
| b08 | 00:42.2–00:50.5 (8.3s) | L39 | Khi Ken nhảy dù tự do, chú chim cắt gập cánh lao theo và thiết bị đo gắn trên đuôi chim đã chạm mốc không tưởng: 389 km/h! |  | chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) gập cánh lao vun vút bên cạnh chiếc dù của phi công, thiết bị đo tốc độ gắn đuôi hiển thị chỉ số 389 km/h |
| b09 | 00:50.5–00:56.3 (5.9s) | L08 | Tốc độ này nhanh hơn cả xe đua công thức một F1 và vượt xa mọi phương tiện giao thông trên mặt đất! |  | Đồ thị so sánh tốc độ vui nhộn: Chiếc xe đua công thức một màu đỏ cắm cờ F1 trên đường đua chạy hết ga ở dưới, nhưng trên cao chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) vượt qua nhẹ như một mũi tên xé gió. KHÔNG có chú Chim Cắt Lớn trong cảnh này. |
| b10 | 00:56.3–01:07.8 (11.5s) | L09 | Nhưng khoan đã các kỹ sư. Ở tốc độ gần 400 km/h, theo định luật vật lý cơ bản, bất kỳ sinh vật bình thường nào cũng sẽ bị luồng gió nén cực mạnh xé toạc màng nhĩ, rách toạc giác mạc và thổi nổ tung hai lá phổi ngay trên không trung! | **400 km/h** · áp lực gió cực đại · R/360 · [0.75, 0.55] | Mô phỏng áp lực gió kinh hoàng: Một hình nộm thí nghiệm bị luồng gió bão cực mạnh thổi bay tóc, thổi phồng má và nứt toác kính, minh họa cho áp lực không khí tàn phá ở 400 km/h. KHÔNG có chú Chim Cắt Lớn trong cảnh này. |
| b11 | 01:07.8–01:14.4 (6.6s) | L10 | Vậy bản thiết kế giải phẫu của Tiêm Kích Lông Vũ này giấu những linh kiện tối mật gì? Mời đội kỹ thuật bước ngay vào bóc tách bản vẽ cơ khí! |  | Phòng thí nghiệm: cô trợ lý sóc hoạt hình đeo kính cận to tròn, mặc áo blouse trắng phòng thí nghiệm, cầm bản vẽ blueprint khí động học trải rộng một tấm bản vẽ blueprint màu xanh lam phát sáng, trên đó vẽ chi tiết cấu trúc xương và khí động học của chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leathe |

### scene02 · NÓN GIẢM ÁP NẸP MŨI CHỐNG NỔ PHỔI VÀ KÍNH BẢO HỘ SINH HỌC · 109.4s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:06.5 (6.5s) | L11 | Bản vẽ kỹ thuật tầng một: Hệ thống điều hòa áp suất khí quyển. Các bạn hãy nhìn thẳng vào lỗ mũi của Chim Cắt Lớn. |  | Bản vẽ cấu tạo đầu chim cắt: chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) nghiêng đầu khoe cận cảnh chiếc mỏ quặp màu xám thép, mũi tên kỹ thuật màu vàng phát sáng chỉ thẳng vào lỗ mũi tròn của chim. |
| b02 | 00:06.5–00:18.8 (12.4s) | L12 | Bình thường lỗ mũi chim chỉ là một cái khe trơn nhẵn, nhưng ở Tiêm Kích Lông Vũ, ngay chính giữa mỗi lỗ mũi lại mọc ra một nón xương nhô lên hình xoắn ốc gọi là tubercle. Đây chính là kiệt tác khí động học trị giá triệu đô của mẹ thiên nhiên! | **TUBERCLE** · nón xương giảm áp · L/360 · [0.35, 0.5] | Kính phóng đại giải phẫu: So sánh hai lỗ mũi, bên trái là lỗ mũi trơn của chim bồ câu, bên phải là lỗ mũi của chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) có chiếc nón xương xoắn ốc tí hon tubercle màu kem nhô lên kiêu hãnh. KHÔNG có chú Chim Cắt Lớn trong c |
| b03 | 00:18.8–00:30.7 (11.9s) | L13 | Khi chim cắt bổ nhào với vận tốc 389 km/h, luồng không khí dội vào mũi với áp lực khổng lồ. Nếu không có vật cản, luồng khí nén này sẽ tràn thẳng vào khí quản như một quả bom nổ chậm, làm vỡ tan các phế nang phổi trong 0,5 giây. | **0,5 GIÂY** · thời gian vỡ phổi · R/360 · [0.75, 0.55] | Mô phỏng đường hầm khí động học: Luồng gió mạnh màu xanh lam lao vào mũi chim, khi gặp nón xương tubercle thì lập tức bị phân tách thành các xoáy khí nhỏ cuộn tròn chậm rãi, nhẹ nhàng đi vào khí quản. KHÔNG có chú Chim Cắt Lớn trong cảnh này. |
| b04 | 00:30.7–00:41.2 (10.5s) | L40 | Nhưng chiếc nón tubercle đóng vai trò như một van giảm chấn siêu cấp, chia nhỏ luồng gió thành các xoáy khí chậm dần, giúp chim hít thở êm ái như đang ngồi uống trà sữa ở vận tốc 300 km/h! |  | chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) cấu trúc nón giảm chấn tubercle hoạt hình ở mũi chia nhỏ luồng gió xoáy cực đại thành các dòng khí êm ái |
| b05 | 00:41.2–00:53.5 (12.3s) | L14 | Chi tiết này thông minh đến mức các kỹ sư hàng không vũ trụ khi thiết kế động cơ phản lực cho siêu máy bay do thám SR-71 Blackbird đã phải mô phỏng y hệt chiếc nón giảm áp này ở cửa hút gió để động cơ không bị nghẹt khí khi bay siêu âm! | **SR-71** · học tập nón cản sốc · L/360 · [0.3, 0.55] | Màn hình so sánh công nghệ sinh học và hàng không: Bên trái là nón mũi của chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles), bên phải là cửa hút gió của siêu máy bay phản lực SR-71 Blackbird với chiếc nón cản sốc shock-cone y hệt. KHÔNG có chú Chim Cắt Lớn trong |
| b06 | 00:53.5–01:00.5 (7.0s) | L15 | Bản vẽ kỹ thuật tầng hai: Cánh khí động học chống rung gãy. Toàn bộ bộ lông của chim cắt được phủ một lớp vảy vi mô đặc biệt. |  | Cận cảnh đôi cánh khí động học của chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles): Đôi cánh dang rộng hình lưỡi liềm nhọn hoắt, các lớp lông vũ màu xám đen xếp chồng khít khao như vảy giáp, các sợi lông cảm biến ở rìa cánh dựng nhẹ điều hướng gió. |
| b07 | 01:00.5–01:12.2 (11.7s) | L41 | Khi chim gập cánh tạo hình lưỡi liềm, các hàng lông cánh tự động khóa chặt vào nhau thành một bề mặt cứng cáp liền khối, triệt tiêu hoàn toàn hiện tượng rung lắc khí động học vốn có thể xé toạc đôi cánh của những loài chim thông thường! |  | chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) gập cánh hình lưỡi liềm gọn gàng, các lớp lông cánh xếp khít mượt mà bảo vệ đôi cánh an toàn tuyệt đối |
| b08 | 01:12.2–01:19.9 (7.8s) | L42 | Không chỉ có vậy, ở chóp cánh chim cắt còn có các sợi lông tơ đóng vai trò như cảm biến vi chấn. Khi phát hiện luồng khí nhiễu loạn ở rìa cánh, |  | chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) chóp cánh xòe các sợi lông cảm biến nhỏ xíu như vi chấn |
| b09 | 01:19.9–01:27.3 (7.3s) | L53 | các sợi lông này lập tức dựng đứng lên một góc nhỏ để tái định hướng dòng khí, giống hệt như cánh nhỏ ở đầu cánh của máy bay Boeing hiện đại! |  | chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) các sợi lông ở chóp cánh dựng đứng lên tái định hướng dòng khí như cánh nhỏ winglet máy bay hiện đại |
| b10 | 01:27.3–01:39.5 (12.2s) | L16 | Chưa hết đâu đội kỹ thuật! Khi lao qua tầng mây với vận tốc tên lửa, bụi cát và gió lốc sẽ cào xước mắt bạn ra sao? Chim cắt không hề lo chuyện đó vì nó sở hữu một mí mắt thứ ba trong suốt, tựa như một chiếc kính bảo hộ sinh học. | **MÍ MẮT 3** · kính bảo hộ sinh học · L/360 · [0.3, 0.5] | Cận cảnh đôi mắt của chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles): Một màng bảo vệ mí mắt thứ ba mỏng như gương trong suốt quét ngang qua nhãn cầu, làm sạch giọt bụi và ngăn gió lốc, hai hàng nước mắt sinh học làm trơn bóng bề mặt mắt. |
| b11 | 01:39.5–01:49.4 (9.9s) | L43 | Mí mắt này quét ngang nhấp nháy liên tục, vừa bôi trơn nước mắt chống khô rát, vừa đóng vai trò như kính chắn gió trong suốt cho phép chim nhìn rõ từng cọng lông của con mồi mà không cần chớp mắt! |  | chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) cận cảnh mắt chim cắt với màng mắt thứ ba trong suốt quét ngang như kính bảo hộ phi công chống bụi lốc |

### scene03 · HỐC MẮT ĐÔI FOVEA VÀ QUỸ ĐẠO BAY XOẮN ỐC LOGARIT · 92.2s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:06.6 (6.6s) | L17 | Chuyển sang bản vẽ tầng ba: Hệ thống ngắm bắn và cảm biến quang học tầm xa. Đôi mắt của Chim Cắt Lớn chiếm tới gần nửa trọng lượng hộp sọ. |  | Bản vẽ giải phẫu hộp sọ: Đôi mắt của chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) chiếm trọn gần nửa khoang sọ, có hai tia laser xanh định vị phát ra từ hai hốc mắt sâu fovea trên võng mạc. |
| b02 | 00:06.6–00:18.7 (12.1s) | L18 | Trong khi mắt người chỉ có một điểm vàng hội tụ ánh sáng sắc nét nhất, thì mắt chim cắt lại trang bị hẳn hai hốc mắt sâu gọi là fovea đôi: một hốc nhìn thẳng để định vị cự ly và một hốc nhìn xéo sang hai bên với độ phân giải siêu nét gấp 8 lần mắt phi công! | **x8 LẦN** · độ nét mắt phi công · L/360 · [0.3, 0.55] | Bảng phân tích độ phân giải quang học: Mắt người nhìn phong cảnh nhòe ở cự ly xa, còn màn hình của chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) chia đôi với hốc mắt fovea đôi phóng to sắc nét gấp 8 lần thấy rõ từng cử động. KHÔNG có chú Chim Cắt Lớn trong cả |
| b03 | 00:18.7–00:32.2 (13.5s) | L19 | Cảm biến quang học báo cáo: Khóa mục tiêu là một chú bồ câu béo múp ở khoảng cách 3km! Tọa độ đã lưu vào bộ nhớ! Nhìn thấy mục tiêu cách 3km là một chuyện, nhưng làm sao để lao xuống đớp mồi lại nảy sinh một nghịch lý vật lý vô cùng đau đầu. | **3 KM** · cự ly khóa mục tiêu · R/360 · [0.75, 0.55] | Góc nhìn ngắm bắn từ trên cao 3.000m: chú chim bồ câu hoạt hình lông xám mập mạp ngơ ngác, cầm máy đo tốc độ đồ chơi màu vàng ở dưới mặt đất đang ngậm mẩu bánh mì ngơ ngác, hồng tâm kính ngắm đồ chơi màu đỏ khóa tròn vào người bồ câu. chú chim bồ câu hoạt hình lông xám mập mạp ngơ ngác, cầm máy đo tốc độ đồ chơi màu vàng. |
| b04 | 00:32.2–00:42.3 (10.1s) | L20 | Giáo sư Vance Tucker thuộc Đại học Duke qua các bài báo trên tạp chí Thực nghiệm Sinh học đã phát hiện ra bí mật chấn động: Hốc mắt nhìn nét nhất của chim cắt nằm lệch một góc 40 độ sang bên cạnh. | **40 ĐỘ** · góc lệch hốc mắt sâu · L/360 · [0.3, 0.55] | Phòng thực nghiệm sinh học Đại học Duke: Giáo sư thỏ đeo kính lão chỉ lên bảng đen vẽ hình một con chim bổ nhào bị ngoẹo cổ lệch 40 độ tạo luồng cản gió lớn màu đỏ cảnh báo. KHÔNG có chú Chim Cắt Lớn trong cảnh này. |
| b05 | 00:42.3–00:55.4 (13.1s) | L44 | Nếu chim bay thẳng tắp cắm đầu xuống, nó sẽ phải ngoẹo cổ sang một bên để nhìn mồi! Mà các kỹ sư biết đấy, đang lao 300 km/h mà ngoẹo đầu sang bên thì lực cản gió sẽ bẻ gãy cổ hoặc làm chim xoay mòng mòng mất lái ngay lập tức! |  | chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) hoạt hình hài hước chim cắt nghiêng đầu 40 độ cố liếc nhìn mục tiêu bên dưới giữa luồng gió tạt méo mỏ |
| b06 | 00:55.4–01:00.8 (5.5s) | L21 | Để giải bài toán hóc búa này, Tiêm Kích Lông Vũ đã lập trình sẵn trong não bộ một đường bay xoắn ốc logarit hoàn hảo. |  | Mô hình toán học trên nền trời xanh: chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) nghiêng thân lượn theo một đường cong xoắn ốc logarit màu vàng óng tuyệt đẹp từ trên cao xoắn dần xuống, đầu giữ thẳng tắp hướng gió, mắt khóa chặt mục tiêu. |
| b07 | 01:00.8–01:13.2 (12.3s) | L45 | Nó giữ đầu thẳng tắp để triệt tiêu tối đa lực cản, đồng thời nghiêng thân lượn theo một đường cong hình học chính xác tuyệt đối, giữ cho mắt luôn nhìn chằm chằm vào con mồi suốt từ độ cao 3.000m xuống đất! Quả là một thuật toán dẫn đường tên lửa đỉnh cao! |  | chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) đường bay xoắn ốc logarit uốn lượn hình học vàng từ độ cao 3.000m xuống đất, mắt luôn găm vào con mồi |
| b08 | 01:13.2–01:22.2 (9.1s) | L22 | Đặc biệt hơn nữa, não bộ của chim cắt xử lý hình ảnh với tần số lên tới 130 khung hình/giây, cao hơn gấp đôi mức 60 khung hình/giây của con người! | **130 FPS** · tốc độ xử lý mắt · R/360 · [0.75, 0.55] | Màn hình hiển thị tần số quét mắt: Đồng hồ 130 fps nhảy nhót, chú chim bồ câu hoạt hình lông xám mập mạp ngơ ngác, cầm máy đo tốc độ đồ chơi màu vàng bên dưới bay chậm rì rì như đang trôi trong bong bóng nước, chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) ung |
| b09 | 01:22.2–01:32.2 (9.9s) | L46 | Nhờ khả năng siêu xử lý này, toàn bộ quỹ đạo của con mồi bay lượn bên dưới đều hiện ra như những cảnh quay chậm chậm rãi, cho phép chim cắt căn chỉnh góc tấn công mượt mà như trong trò chơi điện tử! |  | chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) mắt chim nhìn thế giới con mồi chuyển động siêu chậm slow-motion 130 khung hình mỗi giây mượt mà |

### scene04 · CÚ KÉO LÊN 25G VÀ NẮM ĐẤM MÓNG VUỐT HẠ GỤC CON MỒI · 88.8s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:12.7 (12.7s) | L23 | Bây giờ, mời đội kỹ thuật chứng kiến khoảnh khắc khai hỏa đòn tấn công thực chiến. Khi đã áp sát con mồi ở cự ly 300m, chim cắt gập chặt hai cánh vào sát thân mình, biến toàn bộ cơ thể thành một viên đạn hình giọt nước khí động học hoàn hảo. | **300 MÉT** · cự ly gập cánh · L/360 · [0.3, 0.55] | Cận cảnh tư thế bổ nhào hoàn hảo: chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) khép chặt hai cánh ôm trọn lấy thân hình giọt nước khí động học, đuôi xòe hẹp như bánh lái tên lửa, lao vun vút thẳng đứng từ trên trời cao. |
| b02 | 00:12.7–00:19.8 (7.1s) | L24 | Lúc này, tim của nó đập điên cuồng từ 600-900 nhịp/phút để bơm oxy tới từng thớ cơ ngực săn chắc như đá tảng. | **900 BPM** · nhịp tim cực đại · R/360 · [0.75, 0.55] | Màn hình sinh trắc học y khoa: Nhịp tim điện tâm đồ của chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) nhảy múa dữ dội ở mức 900 nhịp/phút, cơ ngực nổi cơ bắp cuồn cuộn đỏ rực năng lượng dồi dào. KHÔNG có chú Chim Cắt Lớn trong cảnh này. |
| b03 | 00:19.8–00:25.5 (5.7s) | L25 | Nhưng điều đáng kinh ngạc nhất nằm ở cách nó hạ gục con mồi. Nó không hề xòe móng ra để quắp như đại bàng hay diều hâu. |  | Cận cảnh bàn chân của chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles): Bốn ngón chân có móng vuốt sắc nhọn cuộn tròn thành một nắm đấm bọc sừng cứng như quả cầu sắt đặc, giương thẳng ra phía trước như một võ sĩ quyền anh. |
| b04 | 00:25.5–00:36.4 (11.0s) | L47 | Ở vận tốc 300 km/h, nếu xòe móng quắp mồi, quán tính dữ dội sẽ bẻ gãy ngón chân chim cắt ngay lập tức! Thay vào đó, nó cuộn tròn các ngón chân lại thành một nắm đấm đặc sệt bọc sừng, biến thành một quả đấm thép bay tự do! |  | chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) bàn chân chim cắt co tròn các ngón lại thành nắm đấm bọc giáp sắt cực ngầu chuẩn bị giáng đòn |
| b05 | 00:36.4–00:43.2 (6.7s) | L26 | Rầm! Nắm đấm móng vuốt giáng thẳng vào lưng hoặc cánh của con mồi với động năng tương đương một viên đạn chì bắn ra từ súng hơi. |  | Khoảnh khắc va chạm rung chuyển bầu trời: Nắm đấm của chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) giáng trúng cánh con mồi, tạo ra luồng sóng xung kích sao vàng bay tứ tung, chú chim bồ câu hoạt hình lông xám mập mạp ngơ ngác, cầm máy đo tốc độ đồ chơi màu  |
| b06 | 00:43.2–00:57.3 (14.1s) | L48 | Hãy tưởng tượng một quả tạ kim loại nặng gần 1kg đập thẳng vào bạn ở tốc độ 300 km/h! Cú va chạm kinh hoàng làm con mồi gãy cổ rụng rơi tự do trong không trung, trước khi chim cắt lộn một vòng ngoạn mục để đón lấy chiến lợi phẩm giữa tầng mây! | **1kg** · quả tạ kim loại · R/360 · [0.75, 0.55] | chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) minh họa động năng va chạm kinh hoàng như quả tạ kim loại 1kg giáng sấm sét vào con mồi |
| b07 | 00:57.3–01:10.6 (13.3s) | L27 | Ngay sau cú va chạm nổ tung, chim cắt phải thực hiện một động tác hãm phanh kéo ngược cơ thể lên trên không trung. Đây chính là thời khắc sinh tử: Nếu tính toán sai chỉ một phần mười giây 0,1 giây, nó sẽ cắm thẳng đầu xuống đất và nát vụn thành trăm mảnh! |  | Khoảnh khắc kéo phanh sinh tử: Chỉ cách mặt đất rặng cây vài mét, chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) bất ngờ dang rộng đôi cánh hình lưỡi liềm bẻ góc kéo ngược thân mình vút lên bầu trời, tạo luồng gió hất tung bụi cỏ. |
| b08 | 01:10.6–01:20.0 (9.4s) | L28 | Và hãy nhìn vào thông số gia tốc kéo lên: 25G! Một phi công lái máy bay chiến đấu hiện đại nhất chỉ chịu được tối đa 9G trong vài giây là mạch máu tụ xuống chân, mắt tối sầm ngất xỉu. | **25G** · gia tốc kéo lên · R/360 · [0.75, 0.55]<br>**9G** · phi công ngất xỉu · L/360 · [0.3, 0.55] | Bảng đo gia tốc G-force: Bên trái là chú phi công gấu hoạt hình mặc đồ bay G-suit màu xanh, mặt tái mét ôm túi nôn ngộ nghĩnh ngồi trên ghế lái tiêm kích chịu 9G mặt mày xám ngoét ngất xỉu ôm túi nôn; bên phải là chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles)  |
| b09 | 01:20.0–01:28.8 (8.9s) | L49 | Ấy thế mà Tiêm Kích Lông Vũ chịu đựng 25G mà mắt vẫn sáng quắc, đầu vẫn tỉnh queo! Khung xương đòn chữ V liền khối của nó cứng vững gấp 10 lần vật liệu hợp kim nhân tạo! | **10 LẦN** · độ cứng xương đòn · L/360 · [0.3, 0.55] | chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) chim cắt tươi cười ngạo nghễ chịu lực kéo 25G với bộ khung xương đòn chữ V cứng vững gấp 10 lần hợp kim |

### scene05 · DÁNG ĐI VỤNG VỀ DƯỚI MẶT ĐẤT VÀ CUỘC KHỦNG HOẢNG DDT · 81.7s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:13.3 (13.3s) | L29 | Thưa các kỹ sư, theo đúng quy chuẩn báo cáo hồ sơ vũ khí F2, không có vũ khí nào là hoàn hảo tuyệt đối. Mọi cỗ máy tối tân đều phải đánh đổi bằng những điểm yếu kỹ thuật dở khóc dở cười. Điểm yếu thứ nhất của Chim Cắt Lớn chính là: Đừng bao giờ bắt nó đi bộ dưới mặt đất! |  | Bảng phân tích kỹ thuật đóng dấu đỏ: 'ĐIỂM YẾU KỸ THUẬT': cô trợ lý sóc hoạt hình đeo kính cận to tròn, mặc áo blouse trắng phòng thí nghiệm, cầm bản vẽ blueprint khí động học cầm thước chỉ vào hình vẽ đôi chân ngắn tủn của chim cắt đặt trên mặt đất. KHÔNG có chú Chim Cắt Lớn trong cảnh này. |
| b02 | 00:13.3–00:21.0 (7.7s) | L30 | Vì toàn bộ thiết kế tiến hóa dồn hết cho việc bay liệng siêu tốc, đôi chân của chim cắt rất ngắn, cơ đùi yếu và móng vuốt quá cong dài. |  | Bãi cỏ xanh mướt: chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) đứng dưới đất với đôi chân ngắn củn, dáng đi lạch bạch ngả nghiêng như say rượu, móng vuốt quắp vào cỏ làm chú vấp ngã chúi mũi ngố không tả nổi. chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắn |
| b03 | 00:21.0–00:30.1 (9.1s) | L50 | Khi hạ cánh xuống bãi cỏ, từ một tiêm kích bầu trời oai phong lẫm liệt, nó bỗng biến hình thành một chú bồ câu say rượu đi lạch bạch vụng về, nhảy chồm chồm như vừa dẫm phải đinh! |  | chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) chim cắt đứng dưới đất với đôi chân ngắn tũn đi lạch bạch vụng về như chim bồ câu say rượu |
| b04 | 00:30.1–00:38.4 (8.4s) | L54 | Nếu con mồi chạy ngoằn ngoèo trong bụi rậm dưới đất, tỷ lệ tóm mồi của chim cắt tụt dốc thê thảm từ 90% xuống dưới 25%! | **25%** · tỷ lệ tóm mồi mặt đất · R/360 · [0.75, 0.55] | chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) con mồi chạy ngoằn ngoèo vào bụi cỏ, chim cắt nhảy lò cò lúng túng tỷ lệ bắt mồi giảm tụt dốc |
| b05 | 00:38.4–00:49.5 (11.1s) | L31 | Chưa dừng lại ở đó, kỹ năng cận chiến trên mặt đất của nó tệ đến mức thường xuyên bị quạ đen, hải âu hay bồ nông nhảy vào bắt nạt và cướp trắng bữa ăn vừa săn được, khiến sát thủ siêu thanh chỉ biết đứng trơ mắt nhìn đầy bất lực! |  | Tình huống trớ trêu: chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) vừa săn được mẩu thịt đặt trên tảng đá thì một chú quạ đen và chú mòng biển hung hăng nhảy vào vỗ cánh cướp mất, chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông mi |
| b06 | 00:49.5–01:00.0 (10.5s) | L32 | Nhưng bi kịch đen tối nhất trong lịch sử của Tiêm Kích Lông Vũ lại không đến từ thiên địch tự nhiên, mà đến từ một hóa chất vô hình do con người tạo ra vào thập niên 1960: Thuốc trừ sâu DDT. | **DDT** · hóa chất mỏng vỏ · R/360 · [0.75, 0.55] | Đồng ruộng thập niên 1960 u ám: Máy bay nông nghiệp phun những đám khói hóa chất thuốc trừ sâu DDT mù mịt xuống cánh đồng lúa, các loài chim nhỏ ăn phải hạt giống nhiễm độc. KHÔNG có chú Chim Cắt Lớn trong cảnh này. |
| b07 | 01:00.0–01:07.1 (7.1s) | L51 | Khi chim cắt ăn các loài chim nhỏ tích tụ hóa chất này, chất độc phá hủy cơ chế chuyển hóa canxi, khiến vỏ trứng chim cắt mỏng đi trông thấy. |  | chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) chai thuốc trừ sâu hóa chất hoạt hình và chiếc tổ chim với quả trứng vỏ mỏng manh dễ vỡ |
| b08 | 01:07.1–01:21.7 (14.6s) | L33 | Hậu quả là mỗi khi chim bố mẹ ấp trứng, chính sức nặng cơ thể chúng lại vô tình đè bẹp nát những đứa con chưa kịp chào đời. Toàn bộ quần thể chim cắt ở Bắc Mỹ và châu Âu sụt giảm nghiêm trọng đến mức suýt bị xóa sổ vĩnh viễn khỏi bản đồ sinh học, gióng lên hồi chuông cảnh tỉnh đau đớn cho cả nhân loại! |  | Tổ chim cắt trên gờ đá vách núi: Chim bố mẹ ấp trứng trong buồn rầu, những quả trứng chim cắt có lớp vỏ mỏng dính bị nứt toác rạn vỡ vì thiếu hụt canxi, khung cảnh đầy thương cảm. KHÔNG có chú Chim Cắt Lớn trong cảnh này. |

### scene06 · BÀI HỌC PHỤC HỒI VÀ CÂU ĐỐ BÓNG ĐEN QUÁI KIỆT TẬP 32 · 61.3s
| Beat | Thời gian | Ảnh | Lời thoại lúc hình hiện | Sticker | Prompt Gemini (bố cục) |
|---|---|---|---|---|---|
| b01 | 00:00.0–00:10.0 (10.0s) | L34 | May mắn thay, chiến dịch bảo tồn quy mô toàn cầu sau lệnh cấm DDT năm 1972 đã tạo nên một kỳ tích phục hồi ngoạn mục. Các nhà khoa học đã nhân giống thả chim về tự | **NĂM 1972** · lệnh cấm toàn cầu · L/360 · [0.3, 0.55] | Chiến dịch bảo tồn năm 1972: Các nhà khoa học nâng niu chăm sóc những chú chim cắt con mới nở trong lồng ấp hiện đại, rồi đeo vòng định vị thả chim về lại bầu trời tự do. KHÔNG có chú Chim Cắt Lớn trong cảnh này. |
| b02 | 00:10.0–00:19.1 (9.1s) | L35 | nhiên, và giờ đây Tiêm Kích Lông Vũ lại kiêu hãnh chao lượn trên bầu trời các tòa nhà chọc trời từ Nữu Ước tới Luân Đôn, biến nó thành biểu tượng bất diệt cho khả năng phục hồi của mẹ thiên nhiên. |  | Đô thị hiện đại rực rỡ nắng vàng: chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) đậu hiên ngang trên đỉnh tòa tháp chọc trời ngắm nhìn thành phố nhộn nhịp bên dưới, sau đó sải cánh bay lượn kiêu hãnh giữa trời xanh. chú Chim Cắt Lớn hoạt hình lông ngực vằn xám |
| b03 | 00:19.1–00:24.9 (5.8s) | L36 | Báo cáo nghiệm thu kỹ thuật: Vũ khí siêu thanh hoàn toàn đạt chuẩn! Đề nghị lưu trữ vào kho dữ liệu khoa học bảo tồn! |  | Bàn làm việc kỹ thuật: Hồ sơ giải mật số 31 được đóng con dấu xanh lá cây tròn xoe ghi 'ĐÃ NGHIỆM THU XUẤT SẮC', cô trợ lý sóc hoạt hình đeo kính cận to tròn, mặc áo blouse trắng phòng thí nghiệm, cầm bản vẽ blueprint khí động học tươi cười cất hồ sơ vào tủ lưu trữ khoa học. KHÔNG có chú Chim Cắt Lớn trong cảnh này. |
| b04 | 00:24.9–00:38.1 (13.2s) | L37 | Đội kỹ thuật thân mến, bạn thấy ấn tượng nhất với trang bị nào của Chim Cắt Lớn: Nón xương chống nổ phổi trong lỗ mũi, hốc mắt đôi xoắn ốc logarit hay quả đấm thép chịu gia lực 25G? Hãy để lại bình luận phân tích của bạn ngay bên dưới nhé! |  | chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) nghiêng đầu vẫy cánh chào khán giả, bên cạnh là biểu tượng hộp bình luận YouTube kèm các dấu hỏi chấm rực rỡ mời gọi ý kiến của người xem. chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thô |
| b05 | 00:38.1–00:46.9 (8.8s) | L38 | Và ngay trong hồ sơ giải mật Tập 32 tiếp theo, chúng ta sẽ rời bầu trời cao vời vợi để chui sâu xuống lòng đất tối tăm, gặp gỡ một bóng đen bí ẩn dị hợm bậc nhất hành tinh! |  | Đường hầm hang ngầm tối tăm huyền bí dưới lòng đất: Một BÓNG ĐEN BÍ ẨN (solid black silhouette) hình dạng sinh vật gặm nhấm trụi lông kỳ dị với hai chiếc răng cửa to tướng nhô ra, xung quanh là dấu hỏi chấm phát sáng lấp lánh và ký hiệu miễn nhiễm bệnh tật. KHÔNG có chú Chim Cắt Lớn trong cảnh này. |
| b06 | 00:46.9–01:01.3 (14.4s) | L52 | Sinh vật này hoàn toàn trụi lông, da nhăn nheo như củ khoai tây luộc, không hề biết cảm giác đau đớn trước axit đậm đặc và sở hữu bộ gen miễn nhiễm ung thư kỳ diệu giúp nó sống thọ tới hơn 30 năm, gấp 10 lần họ hàng loài gặm nhấm! Đố các kỹ sư đoán được bóng đen quái kiệt tiếp theo này là ai? | **30 năm** · tuổi thọ bất tử · L/360 · [0.3, 0.55] | bóng đen bí ẩn (solid black silhouette) của một sinh vật gặm nhấm trụi lông có răng nanh lớn dưới hang ngầm tối, dấu chấm hỏi vàng phát sáng khổng lồ |

## 5. Phân cảnh Shorts — từng beat

Banner: **BỔ NHÀO 389 KM/H: / NÓN NÉN KHÍ CHỐNG NỔ PHỔI!** · giọng 51.0s + đệm 1.5s

| Beat | Bắt đầu | Ảnh | Lời thoại | Sticker |
|---|---|---|---|---|
| s01 | 00:00.0 | S01 | Hồ sơ mật cấp độ đỏ. Mở khóa! |  |
| s02 | 00:01.9 | S02 | Tại sao khi lao xuống từ độ cao 5.000m với vận tốc 389 km/h, | **5.000m** · độ cao bổ nhào · L/360 · [0.3, 0.55] |
| s03 | 00:06.9 | S11 | hai lá phổi của Chim Cắt Lớn không hề bị nổ tung? |  |
| s04 | 00:09.7 | S03 | Đây chính là Tiêm Kích Lông Vũ, sinh vật bay nhanh nhất lịch sử hành tinh chúng ta! |  |
| s05 | 00:14.2 | S04 | Ở tốc độ khủng khiếp gần 400 km/h, |  |
| s06 | 00:17.0 | S12 | áp lực không khí mạnh đến mức có thể thổi rách toạc khí quản của bất kỳ con thú nào. |  |
| s07 | 00:21.4 | S05 | Nhưng mẹ thiên nhiên đã bí mật lắp đặt ngay trong lỗ mũi chim cắt một chiếc nón xương xoắn ốc tí hon gọi là tubercle. | **TUBERCLE** · nón nén khí · R/360 · [0.75, 0.5] |
| s08 | 00:27.5 | S06 | Chiếc nón giảm áp này chia nhỏ luồng gió nén thành các xoáy khí chậm, giúp chim hít thở êm ái như đang ngồi hóng gió mát! |  |
| s09 | 00:34.2 | S07 | Đến cả siêu máy bay do thám SR-71 Blackbird của con | **SR-71** · học tập tự nhiên · R/360 · [0.75, 0.55] |
| s10 | 00:37.7 | S13 | người cũng phải học lỏm thiết kế nón cản sốc này để bay siêu âm. Chưa hết, |  |
| s11 | 00:42.1 | S08 | chim cắt còn cuộn ngón chân thành quả đấm thép giáng thẳng vào con mồi, |  |
| s12 | 00:45.5 | S09 | chịu gia lực tới 25G mà mắt vẫn tỉnh queo! | **25G** · chịu lực 25G · R/360 · [0.75, 0.55] |
| s13 | 00:48.4 | S10 | Một kiệt tác khí động học đỉnh chóp của tự nhiên! |  |

## 6. Prompt Gemini đầy đủ (nguyên văn đã gửi)

<details><summary>L01</summary>

```text
HÌNH L01 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Hồ sơ mật cấp độ đỏ. Mở khóa!". Bố cục: Phòng nghiên cứu khí động học công nghệ cao: một tập hồ sơ tài liệu đóng dấu đỏ tươi 'BÁO CÁO GIẢI MÃ SỐ 31' đặt giữa bàn kính, màn hình lớn phía sau hiển thị bầu trời mây trắng bao la. KHÔNG có chú Chim Cắt Lớn trong cảnh này.
```
</details>

<details><summary>L02</summary>

```text
HÌNH L02 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chào mừng toàn thể đội ngũ kỹ thuật quay trở lại phòng nghiên cứu vũ khí sinh học. Hôm nay chúng ta giải mật một cỗ máy bay không người lái tự nhiên có tốc độ kinh hoàng nhất lịch sử tiến hóa:". Bố cục: Phòng thí nghiệm khoa học vui nhộn: cô trợ lý sóc hoạt hình đeo kính cận to tròn, mặc áo blouse trắng phòng thí nghiệm, cầm bản vẽ blueprint khí động học đang gõ bàn phím máy tính phân tích biểu đồ khí động học, bên cạnh là mô hình máy bay phản lực đồ chơi. KHÔNG có chú Chim Cắt Lớn trong cảnh này.
```
</details>

<details><summary>L03</summary>

```text
HÌNH L03 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chim Cắt Lớn, danh pháp khoa học Falco peregrinus.". Bố cục: Chân dung oai phong của chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) đứng trên đỉnh vách đá cheo leo, bộ lông xám bạc óng ả, ngực ưỡn tự tin nhìn về phía đường chân trời rực nắng.
```
</details>

<details><summary>L04</summary>

```text
HÌNH L04 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nếu bạn nghĩ báo hoa mai chạy 100 km/h đã là đỉnh chóp, thì cỗ máy này sẽ biến báo đốm thành một trò đùa rùa bò.". Bố cục: Đường đua đồng cỏ savan châu Phi: chú báo săn cheetah hoạt hình màu vàng đốm đen, đi giày thể thao đỏ, đang thở dốc ôm đầu gối mệt mỏi đang vừa chạy vừa lè lưỡi thở dốc, đồng hồ đo tốc độ hiện 100 km/h, nhưng trên bầu trời cao chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) đã lướt qua để lại vệt gió xoáy làm bay mũ của báo. chú báo săn cheetah hoạt hình màu vàng đốm đen, đi giày thể thao đỏ, đang thở dốc ôm đầu gối mệt mỏi.
```
</details>

<details><summary>L05</summary>

```text
HÌNH L05 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Báo cáo radar phòng không: Phát hiện vật thể lạ bổ nhào từ độ cao 5.000m! Vận tốc đo được 389 km/h!". Bố cục: Trạm quan sát radar trên đài chỉ huy: màn hình radar quét xanh lá cây nhấp nháy một chấm sáng đỏ lao vun vút từ độ cao 5.000m xuống với góc bổ nhào dựng đứng. KHÔNG có chú Chim Cắt Lớn trong cảnh này.
```
</details>

<details><summary>L06</summary>

```text
HÌNH L06 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "389 km/h! Đúng vậy các đồng chí, đây không phải thông số chém gió trong phim viễn tưởng.". Bố cục: Bầu trời xanh mây trắng cuộn sóng: chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) gập cánh bổ nhào cực nhanh xé toạc các đám mây, phía sau là vệt sóng âm khí động học màu cam rực rỡ, kèm bảng số đo điện tử hiện số khổng lồ '389 km/h'.
```
</details>

<details><summary>L07</summary>

```text
HÌNH L07 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Năm 2005, phi công nhảy dù Ken Franklin đã cùng chú chim cắt mang tên Frightful thực hiện một cú nhảy từ máy bay ở độ cao 5.000m.". Bố cục: Thí nghiệm thực địa năm 2005: Một chuyên gia nhảy dù mặc đồ bảo hộ lượn giữa tầng mây, bên cạnh là chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) đang lao vút song song với thiết bị máy đo vi cơ gắn gọn gàng ở đuôi lông chim. chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles).
```
</details>

<details><summary>L08</summary>

```text
HÌNH L08 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Tốc độ này nhanh hơn cả xe đua công thức một F1 và vượt xa mọi phương tiện giao thông trên mặt đất!". Bố cục: Đồ thị so sánh tốc độ vui nhộn: Chiếc xe đua công thức một màu đỏ cắm cờ F1 trên đường đua chạy hết ga ở dưới, nhưng trên cao chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) vượt qua nhẹ như một mũi tên xé gió. KHÔNG có chú Chim Cắt Lớn trong cảnh này.
```
</details>

<details><summary>L09</summary>

```text
HÌNH L09 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nhưng khoan đã các kỹ sư. Ở tốc độ gần 400 km/h, theo định luật vật lý cơ bản, bất kỳ sinh vật bình thường nào cũng sẽ bị luồng gió nén cực mạnh xé toạc màng nhĩ, rách toạc giác mạc và thổi nổ tung hai lá phổi ngay trên không trung!". Bố cục: Mô phỏng áp lực gió kinh hoàng: Một hình nộm thí nghiệm bị luồng gió bão cực mạnh thổi bay tóc, thổi phồng má và nứt toác kính, minh họa cho áp lực không khí tàn phá ở 400 km/h. KHÔNG có chú Chim Cắt Lớn trong cảnh này.
```
</details>

<details><summary>L10</summary>

```text
HÌNH L10 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Vậy bản thiết kế giải phẫu của Tiêm Kích Lông Vũ này giấu những linh kiện tối mật gì? Mời đội kỹ thuật bước ngay vào bóc tách bản vẽ cơ khí!". Bố cục: Phòng thí nghiệm: cô trợ lý sóc hoạt hình đeo kính cận to tròn, mặc áo blouse trắng phòng thí nghiệm, cầm bản vẽ blueprint khí động học trải rộng một tấm bản vẽ blueprint màu xanh lam phát sáng, trên đó vẽ chi tiết cấu trúc xương và khí động học của chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles). KHÔNG có chú Chim Cắt Lớn trong cảnh này.
```
</details>

<details><summary>L11</summary>

```text
HÌNH L11 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Bản vẽ kỹ thuật tầng một: Hệ thống điều hòa áp suất khí quyển. Các bạn hãy nhìn thẳng vào lỗ mũi của Chim Cắt Lớn.". Bố cục: Bản vẽ cấu tạo đầu chim cắt: chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) nghiêng đầu khoe cận cảnh chiếc mỏ quặp màu xám thép, mũi tên kỹ thuật màu vàng phát sáng chỉ thẳng vào lỗ mũi tròn của chim.
```
</details>

<details><summary>L12</summary>

```text
HÌNH L12 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Bình thường lỗ mũi chim chỉ là một cái khe trơn nhẵn, nhưng ở Tiêm Kích Lông Vũ, ngay chính giữa mỗi lỗ mũi lại mọc ra một nón xương nhô lên hình xoắn ốc gọi là tubercle. Đây chính là kiệt tác khí động học trị giá triệu đô của mẹ thiên nhiên!". Bố cục: Kính phóng đại giải phẫu: So sánh hai lỗ mũi, bên trái là lỗ mũi trơn của chim bồ câu, bên phải là lỗ mũi của chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) có chiếc nón xương xoắn ốc tí hon tubercle màu kem nhô lên kiêu hãnh. KHÔNG có chú Chim Cắt Lớn trong cảnh này.
```
</details>

<details><summary>L13</summary>

```text
HÌNH L13 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Khi chim cắt bổ nhào với vận tốc 389 km/h, luồng không khí dội vào mũi với áp lực khổng lồ. Nếu không có vật cản, luồng khí nén này sẽ tràn thẳng vào khí quản như một quả bom nổ chậm, làm vỡ tan các phế nang phổi trong 0,5 giây.". Bố cục: Mô phỏng đường hầm khí động học: Luồng gió mạnh màu xanh lam lao vào mũi chim, khi gặp nón xương tubercle thì lập tức bị phân tách thành các xoáy khí nhỏ cuộn tròn chậm rãi, nhẹ nhàng đi vào khí quản. KHÔNG có chú Chim Cắt Lớn trong cảnh này.
```
</details>

<details><summary>L14</summary>

```text
HÌNH L14 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chi tiết này thông minh đến mức các kỹ sư hàng không vũ trụ khi thiết kế động cơ phản lực cho siêu máy bay do thám SR-71 Blackbird đã phải mô phỏng y hệt chiếc nón giảm áp này ở cửa hút gió để động cơ không bị nghẹt khí khi bay siêu âm!". Bố cục: Màn hình so sánh công nghệ sinh học và hàng không: Bên trái là nón mũi của chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles), bên phải là cửa hút gió của siêu máy bay phản lực SR-71 Blackbird với chiếc nón cản sốc shock-cone y hệt. KHÔNG có chú Chim Cắt Lớn trong cảnh này.
```
</details>

<details><summary>L15</summary>

```text
HÌNH L15 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Bản vẽ kỹ thuật tầng hai: Cánh khí động học chống rung gãy. Toàn bộ bộ lông của chim cắt được phủ một lớp vảy vi mô đặc biệt.". Bố cục: Cận cảnh đôi cánh khí động học của chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles): Đôi cánh dang rộng hình lưỡi liềm nhọn hoắt, các lớp lông vũ màu xám đen xếp chồng khít khao như vảy giáp, các sợi lông cảm biến ở rìa cánh dựng nhẹ điều hướng gió.
```
</details>

<details><summary>L16</summary>

```text
HÌNH L16 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chưa hết đâu đội kỹ thuật! Khi lao qua tầng mây với vận tốc tên lửa, bụi cát và gió lốc sẽ cào xước mắt bạn ra sao? Chim cắt không hề lo chuyện đó vì nó sở hữu một mí mắt thứ ba trong suốt, tựa như một chiếc kính bảo hộ sinh học.". Bố cục: Cận cảnh đôi mắt của chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles): Một màng bảo vệ mí mắt thứ ba mỏng như gương trong suốt quét ngang qua nhãn cầu, làm sạch giọt bụi và ngăn gió lốc, hai hàng nước mắt sinh học làm trơn bóng bề mặt mắt.
```
</details>

<details><summary>L17</summary>

```text
HÌNH L17 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chuyển sang bản vẽ tầng ba: Hệ thống ngắm bắn và cảm biến quang học tầm xa. Đôi mắt của Chim Cắt Lớn chiếm tới gần nửa trọng lượng hộp sọ.". Bố cục: Bản vẽ giải phẫu hộp sọ: Đôi mắt của chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) chiếm trọn gần nửa khoang sọ, có hai tia laser xanh định vị phát ra từ hai hốc mắt sâu fovea trên võng mạc.
```
</details>

<details><summary>L18</summary>

```text
HÌNH L18 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Trong khi mắt người chỉ có một điểm vàng hội tụ ánh sáng sắc nét nhất, thì mắt chim cắt lại trang bị hẳn hai hốc mắt sâu gọi là fovea đôi: một hốc nhìn thẳng để định vị cự ly và một hốc nhìn xéo sang hai bên với độ phân giải siêu nét gấp 8 lần mắt phi công!". Bố cục: Bảng phân tích độ phân giải quang học: Mắt người nhìn phong cảnh nhòe ở cự ly xa, còn màn hình của chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) chia đôi với hốc mắt fovea đôi phóng to sắc nét gấp 8 lần thấy rõ từng cử động. KHÔNG có chú Chim Cắt Lớn trong cảnh này.
```
</details>

<details><summary>L19</summary>

```text
HÌNH L19 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Cảm biến quang học báo cáo: nhìn thẳng mục tiêu ngộ nghĩnh là một chú bồ câu béo múp ở khoảng cách 3km! Tọa độ đã lưu vào bộ nhớ! Nhìn thấy mục tiêu cách 3km là một chuyện, nhưng làm sao để lao xuống đớp mồi lại nảy sinh một nghịch lý vật lý vô cùng đau đầu.". Bố cục: Góc nhìn ngắm bắn từ trên cao 3.000m: chú chim bồ câu hoạt hình lông xám mập mạp ngơ ngác, cầm máy đo tốc độ đồ chơi màu vàng ở dưới mặt đất đang ngậm mẩu bánh mì ngơ ngác, hồng tâm kính ngắm đồ chơi màu đỏ khóa tròn vào người bồ câu. chú chim bồ câu hoạt hình lông xám mập mạp ngơ ngác, cầm máy đo tốc độ đồ chơi màu vàng.
```
</details>

<details><summary>L20</summary>

```text
HÌNH L20 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Giáo sư Vance Tucker thuộc Đại học Duke qua các bài báo trên tạp chí Thực nghiệm Sinh học đã phát hiện ra bí mật chấn động: Hốc mắt nhìn nét nhất của chim cắt nằm lệch một góc 40 độ sang bên cạnh.". Bố cục: Phòng thực nghiệm sinh học Đại học Duke: Giáo sư thỏ đeo kính lão chỉ lên bảng đen vẽ hình một con chim bổ nhào bị ngoẹo cổ lệch 40 độ tạo luồng cản gió lớn màu đỏ cảnh báo. KHÔNG có chú Chim Cắt Lớn trong cảnh này.
```
</details>

<details><summary>L21</summary>

```text
HÌNH L21 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Để giải bài toán hóc búa này, Tiêm Kích Lông Vũ đã lập trình sẵn trong não bộ một đường bay xoắn ốc logarit hoàn hảo.". Bố cục: Mô hình toán học trên nền trời xanh: chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) nghiêng thân lượn theo một đường cong xoắn ốc logarit màu vàng óng tuyệt đẹp từ trên cao xoắn dần xuống, đầu giữ thẳng tắp hướng gió, mắt khóa chặt mục tiêu.
```
</details>

<details><summary>L22</summary>

```text
HÌNH L22 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Đặc biệt hơn nữa, não bộ của chim cắt xử lý hình ảnh với tần số lên tới 130 khung hình/giây, cao hơn gấp đôi mức 60 khung hình/giây của con người!". Bố cục: Màn hình hiển thị tần số quét mắt: Đồng hồ 130 fps nhảy nhót, chú chim bồ câu hoạt hình lông xám mập mạp ngơ ngác, cầm máy đo tốc độ đồ chơi màu vàng bên dưới bay chậm rì rì như đang trôi trong bong bóng nước, chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) ung dung chỉnh cánh lượn quanh mục tiêu.
```
</details>

<details><summary>L23</summary>

```text
HÌNH L23 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Bây giờ, mời đội kỹ thuật chứng kiến khoảnh khắc khai hỏa đòn tấn công thực chiến. Khi đã áp sát con mồi ở cự ly 300m, chim cắt gập chặt hai cánh vào sát thân mình, biến toàn bộ cơ thể thành một viên đạn hình giọt nước khí động học hoàn hảo.". Bố cục: Cận cảnh tư thế bổ nhào hoàn hảo: chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) khép chặt hai cánh ôm trọn lấy thân hình giọt nước khí động học, đuôi xòe hẹp như bánh lái tên lửa, lao vun vút thẳng đứng từ trên trời cao.
```
</details>

<details><summary>L24</summary>

```text
HÌNH L24 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Lúc này, tim của nó đập điên cuồng từ 600-900 nhịp/phút để bơm oxy tới từng thớ cơ ngực săn chắc như đá tảng.". Bố cục: Màn hình sinh trắc học y khoa: Nhịp tim điện tâm đồ của chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) nhảy múa dữ dội ở mức 900 nhịp/phút, cơ ngực nổi cơ bắp cuồn cuộn đỏ rực năng lượng dồi dào. KHÔNG có chú Chim Cắt Lớn trong cảnh này.
```
</details>

<details><summary>L25</summary>

```text
HÌNH L25 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nhưng điều đáng kinh ngạc nhất nằm ở cách nó hạ gục con mồi. Nó không hề xòe móng ra để quắp như đại bàng hay diều hâu.". Bố cục: Cận cảnh bàn chân của chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles): Bốn ngón chân có móng vuốt sắc nhọn cuộn tròn thành một nắm đấm bọc sừng cứng như quả cầu sắt đặc, giương thẳng ra phía trước như một võ sĩ quyền anh.
```
</details>

<details><summary>L26</summary>

```text
HÌNH L26 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Rầm! Nắm đấm móng vuốt giáng thẳng vào lưng hoặc cánh của con mồi với động năng tương đương một viên đạn chì bắn ra từ súng hơi.". Bố cục: Khoảnh khắc va chạm rung chuyển bầu trời: Nắm đấm của chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) giáng trúng cánh con mồi, tạo ra luồng sóng xung kích sao vàng bay tứ tung, chú chim bồ câu hoạt hình lông xám mập mạp ngơ ngác, cầm máy đo tốc độ đồ chơi màu vàng giật mình hoa mắt bay lộn nhào rơi tự do. chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles).
```
</details>

<details><summary>L27</summary>

```text
HÌNH L27 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Ngay sau cú va chạm nổ tung, chim cắt phải thực hiện một động tác hãm phanh kéo ngược cơ thể lên trên không trung. Đây chính là thời khắc sinh tử: Nếu tính toán sai chỉ một phần mười giây 0,1 giây, nó sẽ cắm thẳng đầu xuống đất và nát vụn thành trăm mảnh!". Bố cục: Khoảnh khắc kéo phanh sinh tử: Chỉ cách mặt đất rặng cây vài mét, chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) bất ngờ dang rộng đôi cánh hình lưỡi liềm bẻ góc kéo ngược thân mình vút lên bầu trời, tạo luồng gió hất tung bụi cỏ.
```
</details>

<details><summary>L28</summary>

```text
HÌNH L28 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và hãy nhìn vào thông số gia tốc kéo lên: 25G! Một phi công lái máy bay chiến đấu hiện đại nhất chỉ chịu được tối đa 9G trong vài giây là mạch nước màu tụ xuống chân, mắt tối sầm ngất xỉu.". Bố cục: Bảng đo gia tốc G-force: Bên trái là chú phi công gấu hoạt hình mặc đồ bay G-suit màu xanh, mặt tái mét ôm túi nôn ngộ nghĩnh ngồi trên ghế lái tiêm kích chịu 9G mặt mày xám ngoét ngất xỉu ôm túi nôn; bên phải là chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) chịu 25G vẫn cười tươi toe toét giơ ngón cái ngầu lòi. chú phi công gấu hoạt hình mặc đồ bay G-suit màu xanh, mặt tái mét ôm túi nôn ngộ nghĩnh.
```
</details>

<details><summary>L29</summary>

```text
HÌNH L29 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Thưa các kỹ sư, theo đúng quy chuẩn báo cáo hồ sơ vũ khí F2, không có vũ khí nào là hoàn hảo tuyệt đối. Mọi cỗ máy tối tân đều phải đánh đổi bằng những điểm yếu kỹ thuật dở khóc dở cười. Điểm yếu thứ nhất của Chim Cắt Lớn chính là: Đừng bao giờ bắt nó đi bộ dưới mặt đất!". Bố cục: Bảng phân tích kỹ thuật đóng dấu đỏ: 'ĐIỂM YẾU KỸ THUẬT': cô trợ lý sóc hoạt hình đeo kính cận to tròn, mặc áo blouse trắng phòng thí nghiệm, cầm bản vẽ blueprint khí động học cầm thước chỉ vào hình vẽ đôi chân ngắn tủn của chim cắt đặt trên mặt đất. KHÔNG có chú Chim Cắt Lớn trong cảnh này.
```
</details>

<details><summary>L30</summary>

```text
HÌNH L30 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Vì toàn bộ thiết kế tiến hóa dồn hết cho việc bay liệng siêu tốc, đôi chân của chim cắt rất ngắn, cơ đùi yếu và móng vuốt quá cong dài.". Bố cục: Bãi cỏ xanh mướt: chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) đứng dưới đất với đôi chân ngắn củn, dáng đi lạch bạch ngả nghiêng như say rượu, móng vuốt quắp vào cỏ làm chú vấp ngã chúi mũi ngố không tả nổi. chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles).
```
</details>

<details><summary>L31</summary>

```text
HÌNH L31 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Chưa dừng lại ở đó, kỹ năng cận chiến trên mặt đất của nó tệ đến mức thường xuyên bị quạ đen, hải âu hay bồ nông nhảy vào bắt nạt và cướp trắng bữa ăn vừa săn được, khiến sát thủ siêu thanh chỉ biết đứng trơ mắt nhìn đầy bất lực!". Bố cục: Tình huống trớ trêu: chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) vừa săn được mẩu thịt đặt trên tảng đá thì một chú quạ đen và chú mòng biển hung hăng nhảy vào vỗ cánh cướp mất, chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) chỉ biết đứng gãi đầu bẽn lẽn. chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles).
```
</details>

<details><summary>L32</summary>

```text
HÌNH L32 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nhưng bi kịch đen tối nhất trong lịch sử của Tiêm Kích Lông Vũ lại không đến từ thiên địch tự nhiên, mà đến từ một hóa chất vô hình do con người tạo ra vào thập niên 1960: Thuốc trừ sâu DDT.". Bố cục: Đồng ruộng thập niên 1960 u ám: Máy bay nông nghiệp phun những đám khói hóa chất thuốc trừ sâu DDT mù mịt xuống cánh đồng lúa, các loài chim nhỏ ăn phải hạt giống nhiễm độc. KHÔNG có chú Chim Cắt Lớn trong cảnh này.
```
</details>

<details><summary>L33</summary>

```text
HÌNH L33 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Hậu quả là mỗi khi chim bố mẹ ấp trứng, chính sức nặng cơ thể chúng lại vô tình đè bẹp nát những đứa con chưa kịp chào đời. Toàn bộ quần thể chim cắt ở Bắc Mỹ và châu Âu sụt giảm nghiêm trọng đến mức suýt bị xóa sổ vĩnh viễn khỏi bản đồ sinh học, gióng lên hồi chuông cảnh tỉnh đau đớn cho cả nhân loại!". Bố cục: Tổ chim cắt trên gờ đá vách núi: Chim bố mẹ ấp trứng trong buồn rầu, những quả trứng chim cắt có lớp vỏ mỏng dính bị nứt toác rạn vỡ vì thiếu hụt canxi, khung cảnh đầy thương cảm. KHÔNG có chú Chim Cắt Lớn trong cảnh này.
```
</details>

<details><summary>L34</summary>

```text
HÌNH L34 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "May mắn thay, chiến dịch bảo tồn quy mô toàn cầu sau lệnh cấm DDT năm 1972 đã tạo nên một kỳ tích phục hồi ngoạn mục. Các nhà khoa học đã nhân giống thả chim về tự nhiên,". Bố cục: Chiến dịch bảo tồn năm 1972: Các nhà khoa học nâng niu chăm sóc những chú chim cắt con mới nở trong lồng ấp hiện đại, rồi đeo vòng định vị thả chim về lại bầu trời tự do. KHÔNG có chú Chim Cắt Lớn trong cảnh này.
```
</details>

<details><summary>L35</summary>

```text
HÌNH L35 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "và giờ đây Tiêm Kích Lông Vũ lại kiêu hãnh chao lượn trên bầu trời các tòa nhà chọc trời từ Nữu Ước tới Luân Đôn, biến nó thành biểu tượng bất diệt cho khả năng phục hồi của mẹ thiên nhiên.". Bố cục: Đô thị hiện đại rực rỡ nắng vàng: chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) đậu hiên ngang trên đỉnh tòa tháp chọc trời ngắm nhìn thành phố nhộn nhịp bên dưới, sau đó sải cánh bay lượn kiêu hãnh giữa trời xanh. chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles).
```
</details>

<details><summary>L36</summary>

```text
HÌNH L36 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Báo cáo nghiệm thu kỹ thuật: Vũ khí siêu thanh hoàn toàn đạt chuẩn! Đề nghị lưu trữ vào kho dữ liệu khoa học bảo tồn!". Bố cục: Bàn làm việc kỹ thuật: Hồ sơ giải mật số 31 được đóng con dấu xanh lá cây tròn xoe ghi 'ĐÃ NGHIỆM THU XUẤT SẮC', cô trợ lý sóc hoạt hình đeo kính cận to tròn, mặc áo blouse trắng phòng thí nghiệm, cầm bản vẽ blueprint khí động học tươi cười cất hồ sơ vào tủ lưu trữ khoa học. KHÔNG có chú Chim Cắt Lớn trong cảnh này.
```
</details>

<details><summary>L37</summary>

```text
HÌNH L37 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Đội kỹ thuật thân mến, bạn thấy ấn tượng nhất với trang bị nào của Chim Cắt Lớn: Nón xương chống nổ phổi trong lỗ mũi, hốc mắt đôi xoắn ốc logarit hay quả đấm thép chịu gia lực 25G? Hãy để lại bình luận phân tích của bạn ngay bên dưới nhé!". Bố cục: chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) nghiêng đầu vẫy cánh chào khán giả, bên cạnh là biểu tượng hộp bình luận YouTube kèm các dấu hỏi chấm rực rỡ mời gọi ý kiến của người xem. chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles).
```
</details>

<details><summary>L38</summary>

```text
HÌNH L38 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Và ngay trong hồ sơ giải mật Tập 32 tiếp theo, chúng ta sẽ rời bầu trời cao vời vợi để chui sâu xuống lòng đất tối tăm, gặp gỡ một bóng đen bí ẩn dị hợm bậc nhất hành tinh!". Bố cục: Đường hầm hang ngầm tối tăm huyền bí dưới lòng đất: Một BÓNG ĐEN BÍ ẨN (solid black silhouette) hình dạng sinh vật gặm nhấm trụi lông kỳ dị với hai chiếc răng cửa to tướng nhô ra, xung quanh là dấu hỏi chấm phát sáng lấp lánh và ký hiệu miễn nhiễm bệnh tật. KHÔNG có chú Chim Cắt Lớn trong cảnh này.
```
</details>

<details><summary>L39</summary>

```text
HÌNH L39 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Khi Ken nhảy dù tự do, chú chim cắt gập cánh lao theo và thiết bị đo gắn trên đuôi chim đã chạm mốc không tưởng: 389 km/h!". Bố cục: chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) gập cánh lao vun vút bên cạnh chiếc dù của phi công, thiết bị đo tốc độ gắn đuôi hiển thị chỉ số 389 km/h
```
</details>

<details><summary>L40</summary>

```text
HÌNH L40 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nhưng chiếc nón tubercle đóng vai trò như một van giảm chấn siêu cấp, chia nhỏ luồng gió thành các xoáy khí chậm dần, giúp chim hít thở êm ái như đang ngồi uống trà sữa ở vận tốc 300 km/h!". Bố cục: chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) cấu trúc nón giảm chấn tubercle hoạt hình ở mũi chia nhỏ luồng gió xoáy cực đại thành các dòng khí êm ái
```
</details>

<details><summary>L41</summary>

```text
HÌNH L41 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Khi chim gập cánh tạo hình lưỡi liềm, các hàng lông cánh tự động khóa chặt vào nhau thành một bề mặt cứng cáp liền khối, triệt tiêu hoàn toàn hiện tượng rung lắc khí động học vốn có thể xé toạc đôi cánh của những loài chim thông thường!". Bố cục: chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) gập cánh hình lưỡi liềm gọn gàng, các lớp lông cánh xếp khít mượt mà bảo vệ đôi cánh an toàn tuyệt đối
```
</details>

<details><summary>L42</summary>

```text
HÌNH L42 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Không chỉ có vậy, ở chóp cánh chim cắt còn có các sợi lông tơ đóng vai trò như cảm biến vi chấn. Khi phát hiện luồng khí nhiễu loạn ở rìa cánh,". Bố cục: chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) chóp cánh xòe các sợi lông cảm biến nhỏ xíu như vi chấn
```
</details>

<details><summary>L43</summary>

```text
HÌNH L43 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Mí mắt này quét ngang nhấp nháy liên tục, vừa bôi trơn nước mắt chống khô rát, vừa đóng vai trò như kính chắn gió trong suốt cho phép chim nhìn rõ từng cọng lông của con mồi mà không cần chớp mắt!". Bố cục: chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) cận cảnh mắt chim cắt với màng mắt thứ ba trong suốt quét ngang như kính bảo hộ phi công chống bụi lốc
```
</details>

<details><summary>L44</summary>

```text
HÌNH L44 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nếu chim bay thẳng tắp cắm đầu xuống, nó sẽ phải ngoẹo cổ sang một bên để nhìn mồi! Mà các kỹ sư biết đấy, đang lao 300 km/h mà ngoẹo đầu sang bên thì lực cản gió sẽ bẻ gãy cổ hoặc làm chim xoay mòng mòng mất lái ngay lập tức!". Bố cục: chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) hoạt hình hài hước chim cắt nghiêng đầu 40 độ cố liếc nhìn mục tiêu bên dưới giữa luồng gió tạt méo mỏ
```
</details>

<details><summary>L45</summary>

```text
HÌNH L45 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nó giữ đầu thẳng tắp để triệt tiêu tối đa lực cản, đồng thời nghiêng thân lượn theo một đường cong hình học chính xác tuyệt đối, giữ cho mắt luôn nhìn chằm chằm vào con mồi suốt từ độ cao 3.000m xuống đất! Quả là một thuật toán dẫn đường tên lửa đỉnh cao!". Bố cục: chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) đường bay xoắn ốc logarit uốn lượn hình học vàng từ độ cao 3.000m xuống đất, mắt luôn găm vào con mồi
```
</details>

<details><summary>L46</summary>

```text
HÌNH L46 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nhờ khả năng siêu xử lý này, toàn bộ quỹ đạo của con mồi bay lượn bên dưới đều hiện ra như những cảnh quay chậm chậm rãi, cho phép chim cắt căn chỉnh góc tấn công mượt mà như trong trò chơi điện tử!". Bố cục: chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) mắt chim nhìn thế giới con mồi chuyển động siêu chậm slow-motion 130 khung hình mỗi giây mượt mà
```
</details>

<details><summary>L47</summary>

```text
HÌNH L47 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Ở vận tốc 300 km/h, nếu xòe móng quắp mồi, quán tính dữ dội sẽ bẻ gãy ngón chân chim cắt ngay lập tức! Thay vào đó, nó cuộn tròn các ngón chân lại thành một nắm đấm đặc sệt bọc sừng, biến thành một quả đấm thép bay tự do!". Bố cục: chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) bàn chân chim cắt co tròn các ngón lại thành nắm đấm bọc giáp sắt cực ngầu chuẩn bị giáng đòn
```
</details>

<details><summary>L48</summary>

```text
HÌNH L48 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Hãy tưởng tượng một quả tạ kim loại nặng gần 1kg đập thẳng vào bạn ở tốc độ 300 km/h! Cú va chạm kinh hoàng làm con mồi gãy cổ rụng rơi tự do trong không trung, trước khi chim cắt lộn một vòng ngoạn mục để đón lấy chiến lợi phẩm giữa tầng mây!". Bố cục: chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) minh họa động năng va chạm kinh hoàng như quả tạ kim loại 1kg giáng sấm sét vào con mồi
```
</details>

<details><summary>L49</summary>

```text
HÌNH L49 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Ấy thế mà Tiêm Kích Lông Vũ chịu đựng 25G mà mắt vẫn sáng quắc, đầu vẫn tỉnh queo! Khung xương đòn chữ V liền khối của nó cứng vững gấp 10 lần vật liệu hợp kim nhân tạo!". Bố cục: chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) chim cắt tươi cười ngạo nghễ chịu lực kéo 25G với bộ khung xương đòn chữ V cứng vững gấp 10 lần hợp kim
```
</details>

<details><summary>L50</summary>

```text
HÌNH L50 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Khi hạ cánh xuống bãi cỏ, từ một tiêm kích bầu trời oai phong lẫm liệt, nó bỗng biến hình thành một chú bồ câu say rượu đi lạch bạch vụng về, nhảy chồm chồm như vừa dẫm phải đinh!". Bố cục: chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) chim cắt đứng dưới đất với đôi chân ngắn tũn đi lạch bạch vụng về như chim bồ câu say rượu
```
</details>

<details><summary>L51</summary>

```text
HÌNH L51 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Khi chim cắt ăn các loài chim nhỏ tích tụ hóa chất này, chất độc phá hủy cơ chế chuyển hóa canxi, khiến vỏ trứng chim cắt mỏng đi trông thấy.". Bố cục: chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) chai thuốc trừ sâu hóa chất hoạt hình và chiếc tổ chim với quả trứng vỏ mỏng manh dễ vỡ
```
</details>

<details><summary>L52</summary>

```text
HÌNH L52 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Sinh vật này hoàn toàn trụi lông, da nhăn nheo như củ khoai tây luộc, không hề biết cảm giác đau đớn trước axit đậm đặc và sở hữu bộ gen miễn nhiễm ung thư kỳ diệu giúp nó sống thọ tới hơn 30 năm, gấp 10 lần họ hàng loài gặm nhấm! Đố các kỹ sư đoán được bóng đen quái kiệt tiếp theo này là ai?". Bố cục: bóng đen bí ẩn (solid black silhouette) của một sinh vật gặm nhấm trụi lông có răng nanh lớn dưới hang ngầm tối, dấu chấm hỏi vàng phát sáng khổng lồ
```
</details>

<details><summary>L53</summary>

```text
HÌNH L53 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "các sợi lông này lập tức dựng đứng lên một góc nhỏ để tái định hướng dòng khí, giống hệt như cánh nhỏ ở đầu cánh của máy bay Boeing hiện đại!". Bố cục: chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) các sợi lông ở chóp cánh dựng đứng lên tái định hướng dòng khí như cánh nhỏ winglet máy bay hiện đại
```
</details>

<details><summary>L54</summary>

```text
HÌNH L54 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị). Lời thoại: "Nếu con mồi chạy ngoằn ngoèo trong bụi rậm dưới đất, tỷ lệ tóm mồi của chim cắt tụt dốc thê thảm từ 90% xuống dưới 25%!". Bố cục: chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) con mồi chạy ngoằn ngoèo vào bụi cỏ, chim cắt nhảy lò cò lúng túng tỷ lệ bắt mồi giảm tụt dốc
```
</details>

<details><summary>S01</summary>

```text
HÌNH S01 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Hồ sơ mật cấp độ đỏ. Mở khóa!". Bố cục: Màn hình radar phòng không báo động đỏ: Một chấm sáng lao vút từ độ cao 5.000m với tốc độ 389 km/h xé toạc bầu trời. KHÔNG có chú Chim Cắt Lớn trong cảnh này.
```
</details>

<details><summary>S02</summary>

```text
HÌNH S02 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Tại sao khi lao xuống từ độ cao 5.000m với vận tốc 389 km/h,". Bố cục: Mô phỏng áp lực gió cực lớn dội vào một hình nộm thí nghiệm làm thổi bay tóc và nứt kính bảo hộ. KHÔNG có chú Chim Cắt Lớn trong cảnh này.
```
</details>

<details><summary>S03</summary>

```text
HÌNH S03 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Đây chính là Tiêm Kích Lông Vũ, sinh vật bay nhanh nhất lịch sử hành tinh chúng ta!". Bố cục: Chân dung ngầu lòi của chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công đeo kính phi công và mũ da cổ điển, đứng oai vệ trên mỏm đá cao.
```
</details>

<details><summary>S04</summary>

```text
HÌNH S04 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Ở tốc độ khủng khiếp gần 400 km/h,". Bố cục: Luồng gió nén cuồng bạo thổi ầm ầm vào mô hình khí quản hai lá phổi đỏ rực minh họa nguy cơ nổ tung. KHÔNG có chú Chim Cắt Lớn trong cảnh này.
```
</details>

<details><summary>S05</summary>

```text
HÌNH S05 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Nhưng mẹ thiên nhiên đã bí mật lắp đặt ngay trong lỗ mũi chim cắt một chiếc nón xương xoắn ốc tí hon gọi là tubercle.". Bố cục: Cận cảnh lỗ mũi của chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công: Mũi tên phát sáng chỉ vào chiếc nón xương xoắn ốc tubercle nhỏ xíu bên trong lỗ mũi.
```
</details>

<details><summary>S06</summary>

```text
HÌNH S06 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Chiếc nón giảm áp này chia nhỏ luồng gió nén thành các xoáy khí chậm, giúp chim hít thở êm ái như đang ngồi hóng gió mát!". Bố cục: Mô phỏng luồng gió nén gặp nón xương biến thành các xoáy khí chậm cuộn tròn êm ái đi vào phổi. KHÔNG có chú Chim Cắt Lớn trong cảnh này.
```
</details>

<details><summary>S07</summary>

```text
HÌNH S07 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Đến cả siêu máy bay do thám SR-71 Blackbird của con người". Bố cục: So sánh màn hình chia đôi giữa nón mũi của chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công và cửa hút gió của siêu máy bay trinh sát SR-71 Blackbird. KHÔNG có chú Chim Cắt Lớn trong cảnh này.
```
</details>

<details><summary>S08</summary>

```text
HÌNH S08 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "chim cắt còn cuộn ngón chân thành quả đấm thép giáng thẳng vào con mồi,". Bố cục: Bàn chân của chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công cuộn tròn bốn ngón thành quả đấm bọc sừng thép đặc quánh giương ra phía trước như võ sĩ quyền anh.
```
</details>

<details><summary>S09</summary>

```text
HÌNH S09 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "chịu gia lực tới 25G mà mắt vẫn tỉnh queo!". Bố cục: Màn hình đo gia tốc: chú phi công gấu hoạt hình mặc đồ bay G-suit màu xanh, mặt tái mét ôm túi nôn ngộ nghĩnh ngồi trên tiêm kích ngất xỉu vì 9G, trong khi chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công chịu 25G vẫn cười toe toét giơ ngón tay ngầu lòi. chú phi công gấu hoạt hình mặc đồ bay G-suit màu xanh, mặt tái mét ôm túi nôn ngộ nghĩnh.
```
</details>

<details><summary>S10</summary>

```text
HÌNH S10 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "Một kiệt tác khí động học đỉnh chóp của tự nhiên!". Bố cục: chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công sải cánh liềm chao lượn kiêu hãnh trên bầu trời hoàng hôn rực rỡ, để lại vệt sáng vàng óng tuyệt đẹp.
```
</details>

<details><summary>S11</summary>

```text
HÌNH S11 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "hai lá phổi của Chim Cắt Lớn không hề bị nổ tung?". Bố cục: chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) hình vẽ minh họa lá phổi của chim cắt với luồng gió mạnh nhưng có van bảo vệ an toàn
```
</details>

<details><summary>S12</summary>

```text
HÌNH S12 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "áp lực không khí mạnh đến mức có thể thổi rách toạc khí quản của bất kỳ con thú nào.". Bố cục: chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) chiếc nón giảm áp xoắn ốc ở mũi chia nhỏ luồng gió xoáy thành các dòng khí êm ái màu xanh dương
```
</details>

<details><summary>S13</summary>

```text
HÌNH S13 (DỌC 9:16, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể to rõ chiếm phần giữa khung dọc). Lời thoại: "cũng phải học lỏm thiết kế nón cản sốc này để bay siêu âm. Chưa hết,". Bố cục: chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles) hình vẽ máy bay phản lực SR-71 Blackbird với chiếc nón cản sốc hình nón trước cửa hút gió
```
</details>

<details><summary>_first_long</summary>

```text
Tạo hình ảnh (cảnh 1/54 của video YouTube về Chim Cắt Lớn). QUY CHUẨN CHUNG cho mọi cảnh tôi sẽ gửi: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles). Nhân vật phụ cố định: chú chim bồ câu hoạt hình lông xám mập mạp ngơ ngác, cầm máy đo tốc độ đồ chơi màu vàng; cô trợ lý sóc hoạt hình đeo kính cận to tròn, mặc áo blouse trắng phòng thí nghiệm, cầm bản vẽ blueprint khí động học; chú báo săn cheetah hoạt hình màu vàng đốm đen, đi giày thể thao đỏ, đang thở dốc ôm đầu gối mệt mỏi; chú phi công gấu hoạt hình mặc đồ bay G-suit màu xanh, mặt tái mét ôm túi nôn ngộ nghĩnh. 
```
</details>

<details><summary>_first_shorts</summary>

```text
Tạo hình ảnh (cảnh 1/13 của video YouTube Shorts về Chim Cắt Lớn). QUY CHUẨN CHUNG cho mọi cảnh: tỉ lệ DỌC 9:16; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo, phong cách hoạt hình thiếu nhi vui nhộn, tuyệt đối không bạo lực, không kinh dị; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles). Nhân vật phụ: chú chim bồ câu hoạt hình lông xám mập mạp ngơ ngác, cầm máy đo tốc độ đồ chơi màu vàng; chú phi công gấu hoạt hình mặc đồ bay G-suit màu xanh, mặt tái mét ôm túi nôn ngộ nghĩnh. 
```
</details>

## 7. SEO

- **title:** Sinh Vật Bổ Nhào 389 km/h & Nón Nén Khí Chống Nổ Phổi?! | Tập 31
- **hook_paragraph:** Chim Cắt Lớn (Falco peregrinus) đạt kỷ lục tốc độ bổ nhào không tưởng 389 km/h xé toạc bầu trời. Tại sao lá phổi của nó không bị nổ tung trước áp lực gió cực lớn và làm thế nào để nó khóa mục tiêu con mồi cách 3km bằng quỹ đạo xoắn ốc logarit kỳ diệu?
- **question:** Trong các trang bị khí động học của Chim Cắt Lớn, bạn thấy chi tiết nào thông minh nhất: Nón nén khí trong mũi, quỹ đạo xoắn ốc logarit hay quả đấm thép chịu lực 25G?
- **next_teaser:** bóng đen quái kiệt trụi lông dưới lòng đất, không biết đau đớn và miễn nhiễm ung thư
- **shorts_title:** Tại Sao Phổi Chim Cắt Không Nổ Tung Ở Tốc Độ 389 km/h?!
- **shorts_desc:** Chim Cắt Lớn (Falco peregrinus) lao xuống từ độ cao 5.000m với tốc độ 389 km/h mà hai lá phổi không hề bị áp lực gió thổi nổ tung nhờ chiếc nón giảm áp tubercle tối mật trong lỗ mũi! Khám phá kiệt tác khí động học tự nhiên truyền cảm hứng cho siêu tiêm kích SR-71 Blackbird.
- **bullets:** Kỷ lục bổ nhào 389 km/h từ độ cao 5.000m đo đạc bằng thiết bị gắn trên cơ thể chim năm 2005 · Bản vẽ nón giảm áp tubercle trong lỗ mũi giúp hít thở an toàn mà không nổ phổi · Đôi mắt fovea đôi nhìn xa 3km và thuật toán quỹ đạo bay xoắn ốc logarit của Vance Tucker · Cú đấm móng vuốt mid-air hạ gục con mồi và khả năng chịu gia lực 25G gấp 3 lần phi công chiến đấu · Tử huyệt dáng đi lạch bạch dưới đất và bài học bảo tồn sau thảm họa thuốc trừ sâu DDT
- **tags:** chim cắt lớn, chim cắt, peregrine falcon, falco peregrinus, chim bay nhanh nhất thế giới, động vật nhanh nhất hành tinh, bổ nhào 389 km/h, nón giảm áp tubercle, xoắn ốc logarit, gia tốc 25G, vũ khí sinh học, thế giới động vật, vẽ chuyện hoang dã, whiteboard animation, khoa học vui
- **hashtags:** #độngvật #chimcắt #VẽChuyệnHoangDã

## 8. Lệnh tái tạo tập này (theo thứ tự)

```bash
python src/episode/pipeline.py check  projects/tap-31-chim-cat-lon
python src/episode/pipeline.py tts    projects/tap-31-chim-cat-lon     # chạy nền; part đã có trong audio/vs/ được giữ
python src/episode/pipeline.py align  projects/tap-31-chim-cat-lon     # match >= 0.9 mỗi chương
python src/episode/pipeline.py spec   projects/tap-31-chim-cat-lon     # phải in 'spec OK'
python scripts/audit_beats.py projects/tap-31-chim-cat-lon              # Image reuse: {} ; mọi hold 3-15s
python src/episode/pipeline.py render projects/tap-31-chim-cat-lon --force
python scripts/beat_sheet.py projects/tap-31-chim-cat-lon               # xem renders/beat_audit/sceneXX.jpg
python scripts/hum_probe.py projects/tap-31-chim-cat-lon/audio/shorts.wav projects/tap-31-chim-cat-lon/renders/tap-31-chim-cat-lon_shorts.mp4
python src/episode/pipeline.py qa     projects/tap-31-chim-cat-lon
python src/episode/pipeline.py seo    projects/tap-31-chim-cat-lon
python src/episode/episode_doc.py     projects/tap-31-chim-cat-lon
```
