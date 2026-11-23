# -*- coding: utf-8 -*-
import json, os

chars = {
 "HERO": "chú Lươn Điện hoạt hình màu nâu xám đậm, mắt to tròn đeo kính bảo hộ nhà khoa học màu cam, trên cổ đeo chiếc nơ phát sáng tia sét màu vàng, biểu cảm tự tin tinh quái, thân hình dài uốn lượn phát ra các tia điện xanh neon lấp lánh",
 "HERO_S": "chú Lươn Điện đeo kính bảo hộ cam nơ tia sét vàng",
 "PROFESSOR": "giáo sư nhà khoa học điên tóc bạc bù xù mặc áo blouse trắng, đeo găng tay cao su cách điện dày cộp màu đỏ, tay cầm vôn kế đo điện",
 "ASSISTANT": "cô trợ lý phòng thí nghiệm đeo kính cận tròn, tóc đuôi ngựa buộc gọn, tay cầm bảng kẹp tài liệu kiểm tra thông số",
 "CAIMAN": "chú cá sấu Caiman Nam Mỹ dài 2m da xanh vảy sừng, biểu cảm hoảng hốt mắt xoay tròn bị giật cháy đen xù lông",
 "NO_HERO": "KHÔNG có Lươn Điện trong cảnh này"
}

long_beats = [
 # --- SCENE 01: KHỞI ĐỘNG THỬ THÁCH ---
 {
  "scene": "scene01", "at": 0,
  "layout": "BÊN TRÁI {PROFESSOR} đang háo hức bật các công tắc nguồn; Ở GIỮA tấm biển neon khổng lồ nhấp nháy phát sáng 'PHÒNG THÍ NGHIỆM SINH HỌC TỐI MẬT'; BÊN PHẢI {ASSISTANT} đang nhìn vào đồng hồ đo điện áp nhảy số điên cuồng. {NO_HERO}.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene01", "at": "Tiếng hồ quang điện",
  "layout": "Cận cảnh bảng điều khiển phòng thí nghiệm: các tia hồ quang điện màu xanh tím nổ lách tách chói lòa; một chiếc vôn kế kim điện áp đang vọt qua vạch đỏ nguy hiểm. {NO_HERO}.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene01", "at": "Đằng sau tấm kính",
  "layout": "Góc nhìn qua tấm kính cường lực chống điện dày 10cm: một bể nước ngầm khổng lồ tăm tối, bóng dáng dài ngoằng của {HERO} đang bơi lượn uốn lượn tỏa ra ánh sáng điện ma mị.",
  "stickers": [{"at": "10cm", "side": "L", "y": 380, "value": "KÍNH 10CM", "label": "CHỐNG ĐIỆN CAO THẾ", "target": [0.25, 0.45]}],
  "impacts": []
 },
 {
  "scene": "scene01", "at": "Báo cáo giáo sư",
  "layout": "BÊN TRÁI {ASSISTANT} ôm bảng kẹp tài liệu toát mồ hôi hột chỉ tay về phía bể chứa; BÊN PHẢI dàn đèn cảnh báo hình tam giác tia sét đang nhấp nháy đỏ rực khẩn cấp. {NO_HERO}.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene01", "at": "Bình tĩnh nào cô",
  "layout": "BÊN TRÁI {PROFESSOR} cười lớn tự tin đưa chiếc kính cách điện màu cam cho trợ lý; BÊN PHẢI {HERO} bơi sát mặt kính nhếch mép chào một cách tinh quái.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene01", "at": "Nhưng tôi xin tiết",
  "layout": "Cây phả hệ sinh học hài hước: BÊN TRÁI hình ảnh con lươn đồng bị gạch chéo đỏ; BÊN PHẢI {HERO} đứng cạnh một chú cá trê da trơn có râu với dấu tích xanh xác nhận họ hàng gần gũi.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene01", "at": "Nhưng tại sao chúng",
  "layout": "Chân dung phóng to của {HERO}: toàn thân bao bọc bởi mạng lưới mạch điện phát sáng vàng và xanh neon, bên cạnh là biểu tượng nhà máy phát điện mini đang hoạt động hết công suất.",
  "stickers": [{"at": "Nhà Máy Điện Sống", "side": "R", "y": 380, "value": "PIN SỐNG", "label": "NHÀ MÁY ĐIỆN SỐNG", "target": [0.75, 0.45]}],
  "impacts": []
 },
 {
  "scene": "scene01", "at": "Hơn 80% chiều dài",
  "layout": "Sơ đồ giải phẫu cắt lớp: 80% thân hình {HERO} được chia thành hàng ngàn ngăn pin xếp nối tiếp; so sánh BÊN PHẢI với 4 ổ cắm điện 220V gia đình tóe lửa.",
  "stickers": [
   {"at": "80%", "side": "L", "y": 420, "value": "80% PIN", "label": "THÂN CHỨA ĐIỆN", "target": [0.28, 0.5]},
   {"at": "860V", "side": "R", "y": 370, "value": "860V", "label": "GẤP 4 LẦN 220V", "target": [0.72, 0.45]}
  ],
  "impacts": []
 },
 {
  "scene": "scene01", "at": "Hôm nay, tôi sẽ",
  "layout": "Bảng thang đo 5 cấp độ thử thách sáng đèn rực rỡ từ Cấp 1 đến Cấp 5; {PROFESSOR} cầm chiếc cần gạt công suất chuẩn bị gạt nấc đầu tiên. {NO_HERO}.",
  "stickers": [{"at": "5 cấp độ", "side": "R", "y": 390, "value": "5 CẤP ĐỘ", "label": "QUY TRÌNH THÍ NGHIỆM", "target": [0.75, 0.45]}],
  "impacts": []
 },
 {
  "scene": "scene01", "at": "Hãy siết chặt dây",
  "layout": "BÊN TRÁI {PROFESSOR} và {ASSISTANT} thắt dây an toàn ngồi trên ghế thí nghiệm; BÊN PHẢI dòng điện từ bể nước bắt đầu phóng ra những tia lửa sáng lóa mở màn.",
  "stickers": [], "impacts": []
 },

 # --- SCENE 02: CẤP ĐỘ 1 ---
 {
  "scene": "scene02", "at": 0,
  "layout": "BÊN TRÁI tấm biển phát sáng 'CẤP ĐỘ 1: PHÂN TÍCH PIN & RADAR BÙN LẦY'; BÊN PHẢI thước đo chiều dài hiển thị 2m và chiếc cân hiển thị 20kg. {NO_HERO}.",
  "stickers": [
   {"at": "2m", "side": "R", "y": 360, "value": "DÀI 2M", "label": "KÍCH THƯỚC KHỦNG", "target": [0.75, 0.42]},
   {"at": "20kg", "side": "R", "y": 460, "value": "NẶNG 20KG", "label": "THỂ TRỌNG KHỔNG LỒ", "target": [0.75, 0.55]}
  ],
  "impacts": []
 },
 {
  "scene": "scene02", "at": "Tất cả các cơ",
  "layout": "Sơ đồ X-quang sinh học: chỉ 20% phần đầu chứa tim, não, dạ dày nhỏ xíu được đóng khung bảo vệ; 80% còn lại là 3 cơ quan phát điện đồ sộ chiếm trọn thân thể.",
  "stickers": [{"at": "20%", "side": "L", "y": 380, "value": "20% ĐẦU", "label": "DỒN MỌI NỘI TẠNG", "target": [0.28, 0.45]}],
  "impacts": []
 },
 {
  "scene": "scene02", "at": "Cơ quan phát điện",
  "layout": "Ba khối cơ quan phát điện được tô màu khác nhau: Cơ quan Chính màu đỏ cam, cơ quan Hunter màu vàng, và cơ quan Sachs màu xanh lam chạy dọc suốt thân {HERO}.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene02", "at": "Bên trong ba khối",
  "layout": "Kính hiển vi phóng to hàng ngàn lần: 6.000 tế bào electrocyte hình đĩa dẹp xếp chồng ngay ngắn như cọc tiền xu pin nối tiếp nhau phát sáng điện tích âm và dương.",
  "stickers": [{"at": "6.000", "side": "L", "y": 380, "value": "6.000 PIN", "label": "TẾ BÀO ELECTROCYTE", "target": [0.28, 0.45]}],
  "impacts": []
 },
 {
  "scene": "scene02", "at": "Mỗi tế bào này",
  "layout": "Mô phỏng vật lý: một tế bào electrocyte đơn lẻ sinh ra 0,15V như pin đồng hồ cúc áo; mũi tên dẫn sang hàng ngàn tế bào cộng dồn điện áp tăng vọt theo cấp số nhân.",
  "stickers": [{"at": "0,15V", "side": "R", "y": 420, "value": "0,15V/PIN", "label": "CỘNG DỒN NỐI TIẾP", "target": [0.72, 0.5]}],
  "impacts": []
 },
 {
  "scene": "scene02", "at": "Nhưng ở chế độ",
  "layout": "Chế độ radar sinh học: từ phần đuôi của {HERO}, những vòng sóng điện áp thấp 10V màu xanh dương lan tỏa đều đặn ra làn nước xung quanh như sóng radar quét vòng.",
  "stickers": [{"at": "10V", "side": "L", "y": 380, "value": "10V RADAR", "label": "ĐỊNH VỊ ĐIỆN ÁP THẤP", "target": [0.25, 0.45]}],
  "impacts": []
 },
 {
  "scene": "scene02", "at": "Vùng nước sông Amazon",
  "layout": "Lòng sông Amazon đục ngầu đen kịt đầy bùn lầy; đôi mắt {HERO} đeo kính râm mù lòa nhưng các thụ thể điện trên đầu vẫn vẽ ra bản đồ 3D xung quanh rõ mồn một.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene02", "at": "Giáo sư ơi",
  "layout": "Màn hình radar phòng thí nghiệm: các chấm xanh nhấp nháy phát hiện đàn cá nhỏ vùi sâu 30cm dưới lớp bùn; {ASSISTANT} kinh ngạc tròn mắt theo dõi. {NO_HERO}.",
  "stickers": [{"at": "30cm", "side": "R", "y": 390, "value": "SÂU 30CM", "label": "DƯỚI BÙN ĐẶC", "target": [0.75, 0.48]}],
  "impacts": []
 },
 {
  "scene": "scene02", "at": "Đã đến lúc chuyển",
  "layout": "BÊN TRÁI {PROFESSOR} giơ tay chỉ lên bảng điều khiển; bảng đèn chuyển sang màu cam sáng rực báo hiệu 'CẤP ĐỘ 2: HACK NÃO TỪ XA'. {NO_HERO}.",
  "stickers": [], "impacts": []
 },

 # --- SCENE 03: CẤP ĐỘ 2 ---
 {
  "scene": "scene03", "at": 0,
  "layout": "BÊN TRÁI tấm biển 'CẤP ĐỘ 2: VŨ KHÍ HACK NÃO CON MỒI'; BÊN PHẢI hình minh họa một bộ não cá bị các xung điện điều khiển từ xa như con rối dây. {NO_HERO}.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene03", "at": "Năm 2014, nhà sinh",
  "layout": "Trang bìa tạp chí khoa học danh giá Science năm 2014: giáo sư Kenneth Catania tại Đại học Vanderbilt đang tiến hành thí nghiệm xung điện kép với máy hiện sóng. {NO_HERO}.",
  "stickers": [{"at": "Kenneth Catania", "side": "L", "y": 400, "value": "CATANIA 14", "label": "KHOA HỌC SCIENCE", "target": [0.28, 0.5]}],
  "impacts": []
 },
 {
  "scene": "scene03", "at": "Khi nghi ngờ có",
  "layout": "{HERO} phóng ra hai xung điện chớp nhoáng (doublets) cách nhau chỉ 2 mili-giây; các tia sóng điện màu tím xuyên thẳng xuống lớp bùn chạm vào đàn cá đang trốn.",
  "stickers": [{"at": "2-3 phần nghìn giây", "side": "R", "y": 380, "value": "XUNG KÉP", "label": "CÁCH NHAU 2MS", "target": [0.75, 0.45]}],
  "impacts": []
 },
 {
  "scene": "scene03", "at": "Tín hiệu này xâm",
  "layout": "Mô phỏng 3D hệ thần kinh: tín hiệu xung điện của lươn chạy dọc tủy sống con cá, chiếm quyền kiểm soát các bó cơ ép cơ thể co thắt dữ dội ngoài ý muốn. {NO_HERO}.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene03", "at": "Ối giời ơi",
  "layout": "Cận cảnh chú cá nhỏ dưới bùn: mắt trợn ngược, toàn thân giật nảy tanh tách như bị ai giật dây cót, đuôi vẫy loạn xạ làm bùn nước văng tung tóe hài hước. {NO_HERO}.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene03", "at": "Con cá nhỏ vừa",
  "layout": "Vị trí con mồi phát sáng như ngọn hải đăng giữa bùn; cảm biến của {HERO} khóa chặt mục tiêu với tâm ngắm màu đỏ rực rỡ.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene03", "at": "Nhà Máy Điện Sống lập tức",
  "layout": "Đòn kết liễu cao thế: {HERO} xả ra loạt xung điện 400V với tốc độ 400 nhịp/giây; dòng điện sáng rực như sấm sét bao trùm toàn bộ đáy hồ.",
  "stickers": [
   {"at": "400V", "side": "L", "y": 370, "value": "400V", "label": "ĐÒN ĐIỆN TÊ LIỆT", "target": [0.25, 0.45]},
   {"at": "400 nhịp", "side": "R", "y": 420, "value": "400 NHỊP/S", "label": "TẦN SỐ TỬ THẦN", "target": [0.75, 0.5]}
  ],
  "impacts": []
 },
 {
  "scene": "scene03", "at": "Toàn bộ cơ bắp",
  "layout": "Con cá mồi bị đông cứng đơ như một thanh gỗ hóa đá, mắt đờ đẫn không cử động được một chiếc vây; các dòng điện nhỏ vẫn chạy râm ran trên da. {NO_HERO}.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene03", "at": "Và trước khi con",
  "layout": "{HERO} há toang chiếc miệng tạo ra lực xoáy hút chân không cực mạnh; con cá bị hút tọt thẳng vào miệng lươn trong một phần chớp mắt.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene03", "at": "Một cơ chế săn",
  "layout": "BÊN TRÁI {PROFESSOR} và {ASSISTANT} đứng vỗ tay tán thưởng trước màn hình phân tích; BÊN PHẢI {HERO} xoa bụng no nê chớp mắt tinh nghịch.",
  "stickers": [], "impacts": []
 },

 # --- SCENE 04: CẤP ĐỘ 3 ---
 {
  "scene": "scene04", "at": 0,
  "layout": "BÊN TRÁI bảng báo động cấp 3 màu đỏ rực 'CẤP ĐỘ 3: ĐỐI ĐẦU BẠO CHÚA CÁ SẤU'; BÊN PHẢI hình vẽ cá sấu Caiman khổng lồ với hàm răng sắc nhọn. {NO_HERO}.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene04", "at": "Hơn 200 năm trước,",
  "layout": "Bức tranh lịch sử thế kỷ 19: nhà thám hiểm Alexander von Humboldt đứng trên bờ sông vẽ lại cảnh đàn ngựa hí vang nhảy cẫng lên giữa dòng nước sông Nam Mỹ. {NO_HERO}.",
  "stickers": [{"at": "200 năm", "side": "L", "y": 390, "value": "200 NĂM", "label": "BÍ ẨN VON HUMBOLDT", "target": [0.28, 0.48]}],
  "impacts": []
 },
 {
  "scene": "scene04", "at": "Cho đến tận năm",
  "layout": "Phòng thí nghiệm hiện đại của giáo sư Kenneth Catania: các thiết bị cảm biến ghi lại dòng điện và camera quay siêu chậm phân tích chuyển động của lươn điện. {NO_HERO}.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene04", "at": "Nhưng khi bị một",
  "layout": "So sánh môi trường: BÊN TRÁI dòng điện dưới nước sâu bị rò rỉ phân tán ra bốn phương tám hướng; BÊN PHẢI lươn điện trong nước nông đang chuẩn bị bật nhảy.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene04", "at": "Nó không nằm dưới",
  "layout": "Khoảnh khắc ngoạn mục: {HERO} uốn đuôi bật tung người phóng vọt lên khỏi mặt nước cao 0,5m; cằm dẫn điện cực dương dí sát thẳng vào ngực con cá sấu khổng lồ.",
  "stickers": [{"at": "0,5m", "side": "L", "y": 370, "value": "NHẢY 0,5M", "label": "CÚ NHẢY DÍ CẰM", "target": [0.25, 0.45]}],
  "impacts": []
 },
 {
  "scene": "scene04", "at": "Toàn bộ nguồn điện",
  "layout": "Mạch điện kín không suy hao: đầu lươn cực dương dí vào ngực cá sấu, đuôi lươn cực âm cắm dưới nước; toàn bộ luồng sét chạy thẳng xuyên qua tim {CAIMAN}.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene04", "at": "Này con lươn trơn",
  "layout": "Cảnh tượng bi hài: chú cá sấu {CAIMAN} dài 2m bị điện giật cứng đờ toàn thân, các vảy dựng đứng, mắt trợn tròn xoay vòng, khói bốc nghi ngút từ đầu.",
  "stickers": [{"at": "2m", "side": "R", "y": 420, "value": "CÁ SẤU 2M", "label": "GIẬT TÉ KHÓI", "target": [0.75, 0.5]}],
  "impacts": []
 },
 {
  "scene": "scene04", "at": "Cú nhảy dí cằm trực",
  "layout": "Sơ đồ giải phẫu tim cá sấu bị ngừng đập tạm thời do dòng điện cao thế xuyên qua; cá sấu ngã ngửa bất tỉnh nhân sự trên bãi bùn. {NO_HERO}.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene04", "at": "Chưa hết, khi gặp",
  "layout": "Chiến thuật hình chữ U: {HERO} uốn cong người ôm trọn con mồi vào giữa đầu và đuôi; điện trường giữa hai cực nhân đôi cường độ ép chết con mồi trong gọng kìm điện.",
  "stickers": [{"at": "hình chữ U", "side": "L", "y": 380, "value": "CHỮ U", "label": "NHÂN ĐÔI ĐIỆN TRƯỜNG", "target": [0.25, 0.45]}],
  "impacts": []
 },
 {
  "scene": "scene04", "at": "Một chiến thuật chiến",
  "layout": "BÊN TRÁI cá sấu Caiman lủi thủi bò trốn lên bờ với chiếc đuôi còn giật giật; BÊN PHẢI {HERO} bơi ngạo nghễ như chúa tể đầm lầy không đối thủ.",
  "stickers": [], "impacts": []
 },

 # --- SCENE 05: CẤP ĐỘ 4 ---
 {
  "scene": "scene05", "at": 0,
  "layout": "BÊN TRÁI tấm biển 'CẤP ĐỘ 4: BÍ MẬT KHÔNG BỊ GIẬT CHẾT'; BÊN PHẢI {HERO} đứng khoanh tay tự tin trước tia sét với chiếc khiên bảo vệ phát sáng. {NO_HERO}.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene05", "at": "Câu trả lời nằm ở ba",
  "layout": "Hình minh họa 3 tấm lá chắn năng lượng phát sáng xếp trước mặt {HERO}: lá chắn điện trở vật lý, lá chắn vị trí cơ quan, và lá chắn kích thước cơ thể.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene05", "at": "Lá chắn thứ nhất",
  "layout": "Sơ đồ vật lý định luật Ohm: lớp da và mỡ của lươn có điện trở cực cao R-cao; mô phỏng dòng điện gặp vật cản cách điện an toàn.",
  "stickers": [{"at": "điện trở", "side": "L", "y": 390, "value": "ĐIỆN TRỞ", "label": "MỠ CÁCH ĐIỆN", "target": [0.28, 0.48]}],
  "impacts": []
 },
 {
  "scene": "scene05", "at": "Trong khi đó, dòng",
  "layout": "Đường đi của dòng điện: dòng điện chọn con đường nước sông Amazon có điện trở cực thấp, thoát ào ạt ra ngoài làn nước xung quanh mà không đi vào nội tạng lươn. {NO_HERO}.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene05", "at": "Lá chắn thứ hai",
  "layout": "Bản đồ phân vùng an toàn sinh học: phần đầu chứa não và tim được bọc trong kén cách điện chuyên dụng; cách xa khu vực 3 cơ quan phát điện ở thân sau.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene05", "at": "Dòng điện đi từ",
  "layout": "Dòng điện cao thế chạy từ cực dương ở đầu tới cực âm ở đuôi nhưng chỉ lướt trên bề mặt mô cơ ngoài; nội tạng bên trong hoàn toàn bình an vô sự.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene05", "at": "Và lá chắn thứ",
  "layout": "So sánh kích thước: thân hình lươn dài 2m làm loãng mật độ điện trường; các thớ cơ của lươn chỉ chịu một phần rất nhỏ dòng điện.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene05", "at": "trong khi những con cá nhỏ",
  "layout": "Con cá nhỏ đối diện hứng trọn mật độ điện dày đặc hàng chục nghìn vôn/m2; cơ thể cá nhỏ sáng rực lên vì điện trường tập trung cực cao. {NO_HERO}.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene05", "at": "80% lượng oxy của",
  "layout": "Điểm yếu chết người: khoang miệng {HERO} chứa đầy mao mạch đỏ rực hấp thụ 80% oxy không khí; mang cá teo nhỏ không thể thở trong nước.",
  "stickers": [{"at": "80%", "side": "R", "y": 380, "value": "80% OXY", "label": "THỞ BẰNG MIỆNG", "target": [0.75, 0.45]}],
  "impacts": []
 },
 {
  "scene": "scene05", "at": "Cứ mười đến 15",
  "layout": "{HERO} thò đầu lên khỏi mặt nước hít một hơi không khí sảng khoái; đồng hồ đếm ngược 10-15 phút báo hiệu chu kỳ ngoi lên mặt nước bắt buộc.",
  "stickers": [{"at": "15 phút", "side": "L", "y": 410, "value": "10-15 PHÚT", "label": "PHẢI NGOI LÊN THỞ", "target": [0.25, 0.5]}],
  "impacts": []
 },
 {
  "scene": "scene05", "at": "Nếu bạn giữ chặt",
  "layout": "Nghịch lý bi hài: một quả tạ giữ lươn dưới nước, chú lươn điện sặc nước ho sặc sụa với bóng thoại 'Cứu tôi, tôi chết đuối mất!'; {PROFESSOR} và {ASSISTANT} cười nghiêng ngả.",
  "stickers": [], "impacts": []
 },

 # --- SCENE 06: CẤP ĐỘ TỐI THƯỢNG ---
 {
  "scene": "scene06", "at": 0,
  "layout": "BÊN TRÁI bảng đèn sáng rực rỡ 'CẤP ĐỘ TỐI THƯỢNG: KỶ LỤC 860 VÔN'; BÊN PHẢI hình ảnh các nhà khoa học đang đo đạc nguồn điện kỷ lục trên sông Amazon. {NO_HERO}.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene06", "at": "Nhưng vào năm 2019,",
  "layout": "Bài báo khoa học Nature Communications năm 2019 của tiến sĩ de Santana tại Viện Smithsonian, công bố phát hiện loài lươn điện mới Electrophorus voltai. {NO_HERO}.",
  "stickers": [{"at": "2019", "side": "R", "y": 380, "value": "2019", "label": "DE SANTANA NATURE", "target": [0.75, 0.45]}],
  "impacts": []
 },
 {
  "scene": "scene06", "at": "Khi gắn thiết bị",
  "layout": "Cận cảnh chiếc vôn kế đo điện tử hiện số 860V màu vàng rực; {HERO} loài Electrophorus voltai tỏa ra các luồng sét cực quang tuyệt đẹp khắp bể nước.",
  "stickers": [{"at": "860V", "side": "L", "y": 370, "value": "KỶ LỤC", "label": "MẠNH NHẤT HÀNH TINH", "target": [0.25, 0.45]}],
  "impacts": []
 },
 {
  "scene": "scene06", "at": "Tiến hóa không chỉ",
  "layout": "Bức tranh hoang dã sông rừng Amazon: lươn điện bơi lượn như vị thần sấm sét dưới làn nước, biểu tượng cho kỳ quan công nghệ sinh học vĩ đại của tự nhiên.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene06", "at": "Báo cáo giáo sư",
  "layout": "{ASSISTANT} bấm nút lưu trữ dữ liệu; màn hình radar góc phòng thí nghiệm đột nhiên phát tín hiệu cảnh báo nhấp nháy màu đỏ tía dữ dội. {NO_HERO}.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene06", "at": "Tuyệt vời lắm cô",
  "layout": "Ánh đèn phòng thí nghiệm dịu xuống; chiếc màn hình chiếu khổng lồ ở trung tâm bật sáng với ánh hào quang màu cam lửa rực cháy kịch tính. {NO_HERO}.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene06", "at": "Xin gửi tới các",
  "layout": "Manh mối số 1: BÓNG ĐEN BÍ ẨN của một chú bọ cánh cứng tí hon đang nã pháo liên thanh 500 phát/giây ở 100°C kèm dấu hỏi chấm '?' màu đỏ phát sáng. {NO_HERO}.",
  "stickers": [
   {"at": "BÓNG ĐEN BÍ ẨN", "side": "R", "y": 360, "value": "BÓNG ĐEN", "label": "QUÁI KIỆT TẬP 18", "target": [0.75, 0.42]},
   {"at": "500 lần/giây", "side": "L", "y": 420, "value": "500 PHÁT/S", "label": "NÃ ĐẠN LIÊN THANH", "target": [0.25, 0.5]}
  ],
  "impacts": []
 },
 {
  "scene": "scene06", "at": "Thứ hai, phản ứng",
  "layout": "Manh mối số 2: Sơ đồ cấu tạo hệ thống 2 buồng đốt áp suất cực cao bên trong cơ thể bọ cánh cứng đẩy lùi kẻ thù. {NO_HERO}.",
  "stickers": [
   {"at": "hai buồng đốt", "side": "R", "y": 400, "value": "2 BUỒNG", "label": "ĐỘNG CƠ TÊN LỬA MINI", "target": [0.75, 0.48]}
  ],
  "impacts": []
 },
 {
  "scene": "scene06", "at": "Và thứ ba, kỷ",
  "layout": "Manh mối số 3: Một con cóc khổng lồ ôm bụng nôn thốc nôn tháo; BÓNG ĐEN BÍ ẨN chui từ miệng cóc ra ngoài sau 1 tiếng vẫn sống nhăn nhở giơ hai càng ăn mừng. {NO_HERO}.",
  "stickers": [{"at": "1 tiếng", "side": "L", "y": 400, "value": "SỐNG 1 GIỜ", "label": "XẢ ĐỘC THOÁT CHẾT", "target": [0.25, 0.5]}],
  "impacts": []
 },
 {
  "scene": "scene06", "at": "Các trợ lý khoa",
  "layout": "BÓNG ĐEN BÍ ẨN đứng sừng sững giữa màn hình với dấu hỏi chấm '?' khổng lồ; xung quanh là các bong bóng bình luận '? ? ?' kêu gọi khán giả dự đoán. {NO_HERO}.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene06", "at": "Giáo sư phòng thí",
  "layout": "BÊN TRÁI {PROFESSOR} và {ASSISTANT} vẫy tay chào tạm biệt; BÊN PHẢI tấm biển gỗ đề chữ 'HẸN GẶP LẠI Ở TẬP 18 VỚI SIÊU PHÁO THỦ TÍ HON!'. {NO_HERO}.",
  "stickers": [], "impacts": []
 }
]

shorts_beats = [
 {
  "at": 0,
  "layout": "KHUNG HÌNH DỌC 9:16: {PROFESSOR} đeo kính bảo hộ giơ cần gạt công suất, dòng chữ lớn 'TRỢ LÝ, TĂNG ĐIỆN ÁP TỐI ĐA!' xuất hiện rực rỡ phía trên.",
  "stickers": []
 },
 {
  "at": "Một sinh vật có",
  "layout": "KHUNG HÌNH DỌC 9:16: Dòng điện 860V màu xanh neon nổ lách tách chói lòa trong hồ nước, con cá sấu Caiman 2m bên cạnh bị giật cứng đơ người.",
  "stickers": [{"at": "860V", "side": "L", "y": 620, "value": "860V", "label": "GIẬT NGẤT CÁ SẤU", "target": [0.5, 0.45]}]
 },
 {
  "at": "nhưng tại sao chính nó",
  "layout": "KHUNG HÌNH DỌC 9:16: Chú Lươn Điện bơi ung dung bình an vô sự trong vầng hào quang điện, đôi mắt tròn xoe ngây thơ chớp chớp.",
  "stickers": []
 },
 {
  "at": "Đó chính là Lươn",
  "layout": "KHUNG HÌNH DỌC 9:16: Chân dung {HERO} uốn lượn uy dũng giữa dòng nước Amazon, cơ thể tỏa ra các tia sét màu vàng và xanh neon tuyệt đẹp.",
  "stickers": []
 },
 {
  "at": "Hơn 80% cơ thể",
  "layout": "KHUNG HÌNH DỌC 9:16: Sơ đồ cơ thể {HERO}: 80% thân chứa 6.000 tế bào pin sinh học electrocyte nối tiếp nhau phát sáng rực rỡ.",
  "stickers": [{"at": "80%", "side": "L", "y": 640, "value": "80% PIN", "label": "6.000 TẾ BÀO ĐIỆN", "target": [0.5, 0.48]}]
 },
 {
  "at": "tích tụ điện thế mạnh",
  "layout": "KHUNG HÌNH DỌC 9:16: So sánh điện áp: cột điện thế của lươn vọt cao gấp 4 lần ổ cắm điện gia đình 220V đang tóe lửa.",
  "stickers": [{"at": "gấp 4 lần", "side": "R", "y": 740, "value": "GẤP 4 LẦN", "label": "Ổ CẮM 220V", "target": [0.55, 0.55]}]
 },
 {
  "at": "Khi săn mồi, nó",
  "layout": "KHUNG HÌNH DỌC 9:16: Xung điện kép phóng ra từ {HERO} chạm vào con cá nhỏ dưới bùn, ép toàn bộ cơ bắp con cá giật nảy phát lộ vị trí.",
  "stickers": [{"at": "xung điện kép", "side": "L", "y": 630, "value": "HACK NÃO", "label": "ÉP CO GIẬT TỪ XA", "target": [0.5, 0.46]}]
 },
 {
  "at": "rồi tung cú nhảy",
  "layout": "KHUNG HÌNH DỌC 9:16: {HERO} phóng vọt lên khỏi mặt nước dí cằm trực tiếp vào ngực kẻ thù; luồng sét chạy thẳng xuyên qua tim không bị phân tán.",
  "stickers": [{"at": "nhảy dí cằm", "side": "R", "y": 650, "value": "DÍ CẰM", "label": "TRUYỀN TRỰC TIẾP", "target": [0.55, 0.5]}]
 },
 {
  "at": "Nhưng sở dĩ nó",
  "layout": "KHUNG HÌNH DỌC 9:16: Sơ đồ giải phẫu cắt ngang: lớp mỡ dày cách điện bảo vệ nội tạng, não và tim dồn hết lên đầu an toàn tuyệt đối.",
  "stickers": [{"at": "cách điện", "side": "L", "y": 640, "value": "CÁCH ĐIỆN", "label": "BẢO VỆ NỘI TẠNG", "target": [0.5, 0.48]}]
 },
 {
  "at": "và dòng điện luôn",
  "layout": "KHUNG HÌNH DỌC 9:16: Dòng điện chọn thoát thẳng ra nước có điện trở thấp hơn thay vì đi vào cơ thể lươn, tạo thành vầng hào quang điện rực rỡ.",
  "stickers": []
 },
 {
  "at": "Vậy là bí mật",
  "layout": "KHUNG HÌNH DỌC 9:16: {HERO} bơi kiêu hãnh giữa dòng nước sông Amazon rạng rỡ ánh bình minh, biểu tượng cho vũ khí sinh học hoàn hảo của tự nhiên.",
  "stickers": []
 },
 {
  "at": "biến thịt da thành vũ khí",
  "layout": "KHUNG HÌNH DỌC 9:16: Toàn cảnh dòng sông rừng Amazon tuyệt đẹp lúc rạng đông, Lươn Điện lướt sóng uy nghi khép lại câu chuyện trọn vẹn.",
  "stickers": []
 }
]

storyboard = {
 "_doc": "Storyboard for Episode 17 Luon Dien",
 "characters": chars,
 "side_characters": [],
 "shorts_title_lines": ["860 VÔN GIẬT CÁ SẤU?!", "VÌ SAO KHÔNG TỰ GIẬT?"],
 "skip_numbers": [],
 "long": long_beats,
 "shorts": shorts_beats
}

with open("projects/tap-17-luon-dien/specs/storyboard.json", "w", encoding="utf8") as f:
    json.dump(storyboard, f, ensure_ascii=False, indent=1)

print(f"storyboard.json generated: {len(long_beats)} long beats, {len(shorts_beats)} shorts beats.")
