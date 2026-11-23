# -*- coding: utf-8 -*-
import json, os

chars = {
 "HERO": "chú Thằn Lằn Quỷ Gai hoạt hình màu vàng nâu cát sa mạc phủ đầy gai nón nhọn hoắt, mắt to tròn tinh ranh đeo chiếc mũ tai bèo thám hiểm safari kaki, cổ đeo chiếc nơ đỏ thắm dễ thương, biểu cảm tự tin ngộ nghĩnh",
 "HERO_S": "chú Thằn Lằn Quỷ Gai mũ safari nơ đỏ",
 "REPORTER": "phóng viên truyền hình 24h mặc áo gile thám hiểm nhiều túi, tay cầm micro có logo '24H WILD'",
 "DINGO": "chú chó hoang Dingo sa mạc lông vàng hung dữ, biểu cảm méo xệch ôm mõm vì cắn phải gai",
 "VARANUS": "chú kỳ đà sa mạc khổng lồ dài 2m da hoa văn xám đen, biểu cảm kinh ngạc lè lưỡi thụt lùi",
 "NO_HERO": "KHÔNG có Thằn Lằn Quỷ Gai trong cảnh này"
}

long_beats = [
 # --- SCENE 01: 05:00 SÁNG ---
 {
  "scene": "scene01", "at": 0,
  "layout": "Toàn cảnh sa mạc Red Centre nước Úc lúc bình minh: BÊN TRÁI {REPORTER} cầm micro phát sóng trực tiếp; Ở GIỮA đồng hồ cát khổng lồ hiện số 05:00 sáng; BÊN PHẢI những cồn cát đỏ rực trải dài vô tận. {NO_HERO}.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene01", "at": "Phóng viên truyền hình",
  "layout": "Nhiệt kế đo nhiệt độ sa mạc: cột nhiệt độ chỉ mức lạnh thấu xương lúc sáng sớm và mũi tên đỏ chỉ mức vọt lên 45°C lúc giữa trưa gay gắt. {NO_HERO}.",
  "stickers": [
   {"at": "45°C", "side": "R", "y": 380, "value": "45°C", "label": "CHẢO LỬA SA MẠC", "target": [0.75, 0.45]}
  ],
  "impacts": []
 },
 {
  "scene": "scene01", "at": "Trước mắt chúng ta",
  "layout": "Cận cảnh xuất hiện của {HERO}: toàn thân bọc kín hàng trăm chiếc gai nón nhọn hoắt như cỗ xe bọc thép thời cổ, chiếc mũ safari kaki đội ngay ngắn, nơ đỏ nổi bật trên cổ.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene01", "at": "Thân hình chỉ dài",
  "layout": "Thước đo so sánh: {HERO} dài vỏn vẹn 20cm đứng cạnh bàn chân người; toàn thân bao bọc bởi lớp gai nhọn xù xì đe dọa.",
  "stickers": [{"at": "20cm", "side": "L", "y": 390, "value": "DÀI 20CM", "label": "CHIẾN BINH GAI GÓC", "target": [0.28, 0.48]}],
  "impacts": []
 },
 {
  "scene": "scene01", "at": "Xin trân trọng giới", "id": "L52",
  "layout": "Chân dung hào hùng của {HERO}: đứng kiêu hãnh trên mỏm đá sa mạc đỏ rực, gió thổi bay dải nơ đỏ thắm, ánh mặt trời mọc rực rỡ phía sau.",
  "stickers": [{"at": "Chiến Binh Gai Góc", "side": "R", "y": 380, "value": "QUỶ GAI", "label": "CHIẾN BINH GAI GÓC", "target": [0.75, 0.45]}],
  "impacts": []
 },
 {
  "scene": "scene01", "at": "Giáo sư ơi",
  "layout": "Khán giả nhí hoạt hình ngơ ngác nhìn quanh cồn cát khô cằn nứt nẻ không một giọt nước, cầm chiếc bình nước rỗng tuếch lắc lắc tuyệt vọng. {NO_HERO}.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene01", "at": "Khán giả nhí vừa",
  "layout": "Camera quay siêu chậm: {HERO} thong thả đặt 4 bàn chân lên lớp cát ẩm sương mai; các hạt sương đọng lấp lánh quanh móng chân sắc nhọn.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene01", "at": "Toàn bộ bề mặt",
  "layout": "Kính hiển vi phóng đại da {HERO}: mạng lưới rãnh mao dẫn siêu hiển vi đan xen như mạng lưới kênh rạch thủy lợi giữa các chân gai nhọn phát sáng xanh lam.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene01", "at": "Theo định luật mao",
  "layout": "Mô phỏng lực mao dẫn vật lý: các giọt nước sương từ hạt cát ẩm tự động bị hút ngược chiều trọng lực, chảy thành dòng nước tí hon dọc cẳng chân và bụng.",
  "stickers": [{"at": "mao dẫn", "side": "L", "y": 390, "value": "MAO DẪN", "label": "HÚT NƯỚC NGƯỢC DÒNG", "target": [0.28, 0.48]}],
  "impacts": []
 },
 {
  "scene": "scene01", "at": "Nước chảy từ móng",
  "layout": "Sơ đồ dòng chảy trên cơ thể {HERO}: các mũi tên nước màu xanh dương chạy dọc từ 4 chân, leo qua bờ bụng, vượt sống lưng và đổ thẳng về hai khóe miệng.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene01", "at": "Các nhà vật lý",
  "layout": "Phòng thí nghiệm Viện nghiên cứu Đức: các nhà khoa học đang phân tích lớp da thằn lằn quỷ gai trên màn hình kính hiển vi điện tử quét SEM. {NO_HERO}.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene01", "at": "những rãnh mao dẫn", "id": "L53",
  "layout": "Mô phỏng 3D rãnh mao dẫn bất đối xứng bề rộng 5-150 μm: nước chảy cuồn cuộn một chiều về phía trước, khóa chặt không cho chảy ngược lại. {NO_HERO}.",
  "stickers": [{"at": "5-150 μm", "side": "R", "y": 380, "value": "5-150 μM", "label": "RÃNH MAO DẪN", "target": [0.75, 0.45]}],
  "impacts": []
 },
 {
  "scene": "scene01", "at": "Không cần bất kỳ",
  "layout": "Hình ảnh so sánh: một bên chiếc máy bơm cơ học bị gạch chéo đỏ; một bên là giọt nước tự động kết nối kéo nhau chạy trên da {HERO} kỳ diệu.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene01", "at": "Chú thằn lằn chỉ",
  "layout": "{HERO} đứng thong dong chớp mắt, hai hàm nhấp nháy nhịp nhàng như đang thưởng thức ly nước mát lạnh; nước sạch tự động chảy tọt vào họng sảng khoái.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene01", "at": "Thậm chí nếu bạn",
  "layout": "Thí nghiệm nhỏ giọt nước: một giọt nước rơi trúng lưng {HERO}, giọt nước lập tức phân nhánh chảy men theo các rãnh gai lao thẳng về miệng trong tích tắc.",
  "stickers": [], "impacts": []
 },

 # --- SCENE 02: 09:00 SÁNG ---
 {
  "scene": "scene02", "at": 0,
  "layout": "BÊN TRÁI đồng hồ chuyển sang mốc 09:00 sáng; Ở GIỮA ánh mặt trời bắt đầu gay gắt 35°C; BÊN PHẢI {HERO} bụng kêu 'ùng ục' xoa bụng đói meo hài hước.",
  "stickers": [{"at": "35°C", "side": "R", "y": 380, "value": "35°C", "label": "NẮNG NÓNG BẮT ĐẦU", "target": [0.75, 0.45]}],
  "impacts": []
 },
 {
  "scene": "scene02", "at": "Nhưng quý vị có",
  "layout": "Thực đơn sa mạc đặc biệt: 100% là loài kiến đen Iridomyrmex chứa đầy a-xít phoóc-mích; một con kiến đen hung hăng giơ hai càng đe dọa. {NO_HERO}.",
  "stickers": [{"at": "100%", "side": "L", "y": 390, "value": "100% KIẾN", "label": "THỰC ĐƠN ĐỘC NHẤT", "target": [0.28, 0.48]}],
  "impacts": []
 },
 {
  "scene": "scene02", "at": "Chiến Binh Gai Góc lạch bạch",
  "layout": "{HERO} ngồi xổm bất động bên cạnh đường mòn kiến đen chạy qua bãi cát, kiên nhẫn như ông cụ ngồi câu cá bên hồ.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene02", "at": "Và ngay khi đàn",
  "layout": "Đàn kiến đen nối đuôi nhau hành quân trên nền cát đỏ; bóng lưng {HERO} khổng lồ phủ bóng xuống như ngọn núi phục kích.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene02", "at": "Chiếc lưỡi dày phủ",
  "layout": "Tốc độ săn mồi chớp nhoáng: chiếc lưỡi dính màu hồng của {HERO} phóng ra như tia chớp, 1 giây thò thụt 2-3 lần tóm gọn từng chú kiến đen.",
  "stickers": [{"at": "1 giây", "side": "R", "y": 380, "value": "1 GIÂY", "label": "THÒ THỤT 2-3 LẦN", "target": [0.75, 0.45]}],
  "impacts": []
 },
 {
  "scene": "scene02", "at": "Ối cứu bọn em",
  "layout": "Cảnh tượng bi hài: cả trung đội kiến đen hoảng loạn tháo chạy tán loạn khi chiếc lưỡi khổng lồ của {HERO} quét sạch cả hàng ngũ. {NO_HERO}.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene02", "at": "Quý vị thử nghĩ",
  "layout": "Bình hóa chất a-xít phoóc-mích bốc khói độc hại; so sánh bên cạnh là các loài thú nhỏ sợ hãi lùi xa né tránh đàn kiến đen. {NO_HERO}.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene02", "at": "nhưng khi chui vào", "id": "L54",
  "layout": "Bên trong dạ dày {HERO}: lớp dịch nhầy đệm đặc biệt bao bọc trung hòa toàn bộ a-xít của kiến đen, biến chúng thành năng lượng tích tụ ở chiếc đuôi mập mạp.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene02", "at": "Thậm chí chiếc đuôi",
  "layout": "Chiếc đuôi mập mạp của {HERO} phình to chứa các hạt mỡ năng lượng vàng óng; biểu tượng bình ắc-quy tích lũy năng lượng cho mùa hạn hán.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene02", "at": "Tiếng kêu cứu thất",
  "layout": "Bầy kiến đen hoảng loạn tháo chạy bất lực trước máy hút bụi sinh học của {HERO}. {NO_HERO}.",
  "stickers": [],
  "impacts": []
 },
 {
  "scene": "scene02", "at": "Các nhà nghiên cứu", "id": "L63",
  "layout": "Bộ đếm kỷ lục ăn kiến: con số nhảy vọt từ 1.000 đến 2.500 con kiến đen; {HERO} ngồi liếm mép no nê thỏa mãn giữa bãi cát.",
  "stickers": [
   {"at": "2.500", "side": "R", "y": 400, "value": "2.500 CON", "label": "KỶ LỤC KIẾN/NGÀY", "target": [0.75, 0.5]}
  ],
  "impacts": []
 },
 {
  "scene": "scene02", "at": "Dạ dày của nó", "id": "L55",
  "layout": "Cấu tạo thành dạ dày bọc thép sinh học của {HERO}: lớp màng nhầy đệm dày dặn ngăn cách hoàn toàn các chất độc, bảo vệ cơ thể an toàn tuyệt đối.",
  "stickers": [], "impacts": []
 },

 # --- SCENE 03: 13:00 TRƯA ---
 {
  "scene": "scene03", "at": 0,
  "layout": "BÊN TRÁI đồng hồ điểm mốc 13:00 trưa; Ở GIỮA mặt cát bốc hơi nóng hầm hập vượt 50°C; BÊN PHẢI {REPORTER} lau mồ hôi nhễ nhại cảnh báo nguy hiểm. {NO_HERO}.",
  "stickers": [{"at": "50°C", "side": "R", "y": 380, "value": "50°C", "label": "CÁT BỐC LỬA", "target": [0.75, 0.45]}],
  "impacts": []
 },
 {
  "scene": "scene03", "at": "Trên bầu trời rực",
  "layout": "Bầu trời rực nắng chói chang: loài chim ưng săn mồi mắt sắc như dao cạo đang dang rộng cánh lượn vòng tìm kiếm con mồi. {NO_HERO}.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene03", "at": "còn dưới mặt đất, một", "id": "L56",
  "layout": "Chú kỳ đà {VARANUS} khổng lồ dài 2m da hoa văn xám đen đang bò trườn trên mặt cát sục sạo từng bụi cỏ khô tìm kiếm {HERO}.",
  "stickers": [{"at": "2m", "side": "L", "y": 390, "value": "KỲ ĐÀ 2M", "label": "SÁT THỦ SA MẠC", "target": [0.28, 0.48]}],
  "impacts": []
 },
 {
  "scene": "scene03", "at": "Chiến Binh Gai Góc lập tức",
  "layout": "Cận cảnh sau gáy {HERO}: chiếc bướu gai thịt nhô cao với hai chiếc gai sừng to tướng trông y hệt một chiếc đầu thứ hai đầy uy hiếp.",
  "stickers": [{"at": "đầu thứ hai", "side": "R", "y": 380, "value": "ĐẦU GIẢ", "label": "BƯỚU GAI SAU GÁY", "target": [0.75, 0.45]}],
  "impacts": []
 },
 {
  "scene": "scene03", "at": "Khi kẻ địch lao",
  "layout": "Tuyệt kỹ cúi đầu: {HERO} giấu đầu thật kín mít vào giữa hai chân trước áp sát đất; đồng thời ngóc chiếc đầu giả đầy gai nhọn lên cao làm mồi nhử.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene03", "at": "Thằng nhóc con trốn",
  "layout": "Kỳ đà {VARANUS} hung hăng há miệng táp mạnh xuống chiếc đầu giả đầy gai nhọn; mắt trợn trừng vì gai đâm thủng mép.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene03", "at": "Cú đớp chí mạng",
  "layout": "Hàm răng của kẻ săn mồi cắn ngập vào khối bướu gai cứng như đá tảng; răng nanh cắn phải đá toát tia lửa đau đớn. {NO_HERO}.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene03", "at": "Trong khi kẻ săn",
  "layout": "BÊN TRÁI kẻ săn mồi ôm mồm sưng vù vừa khóc vừa bỏ chạy; BÊN PHẢI {HERO} ngóc đầu thật lành lặn 100% lên nhếch mép cười đắc chí.",
  "stickers": [{"at": "100%", "side": "R", "y": 420, "value": "100% LÀNH", "label": "ĐẦU THẬT AN TOÀN", "target": [0.75, 0.52]}],
  "impacts": []
 },

 # --- SCENE 04: 17:00 HOÀNG HÔN ---
 {
  "scene": "scene04", "at": 0,
  "layout": "BÊN TRÁI đồng hồ điểm 17:00 hoàng hôn; BÊN PHẢI chú chó hoang {DINGO} lông vàng hung hăng nhe nanh đánh hơi xuất hiện trên cồn cát cam rực. {NO_HERO}.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene04", "at": "Nếu kẻ săn mồi",
  "layout": "Chú chó {DINGO} há toang mõm định nuốt trọn cả cơ thể thằn lằn vào bụng như một viên kẹo cứng. {NO_HERO}.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene04", "at": "Chiến Binh Gai Góc lập tức tung",
  "layout": "{HERO} hít căng không khí vào phổi, phồng to cơ thể gấp đôi bình thường; biến thành quả cầu gai bọc thép tròn xoe.",
  "stickers": [
   {"at": "gấp đôi", "side": "L", "y": 380, "value": "GẤP ĐÔI", "label": "PHỒNG QUẢ CẦU GAI", "target": [0.28, 0.45]}
  ],
  "impacts": []
 },
 {
  "scene": "scene04", "at": "Hàng trăm chiếc gai", "id": "L57",
  "layout": "Cận cảnh hàng trăm chiếc gai nón trên lưng {HERO} dựng đứng vuông góc 90°; toàn bộ cơ thể trở thành khối chông sắt bất khả xâm phạm.",
  "stickers": [
   {"at": "90°", "side": "R", "y": 420, "value": "DỰNG 90°", "label": "BỌC THÉP TOÀN THÂN", "target": [0.72, 0.5]}
  ],
  "impacts": []
 },
 {
  "scene": "scene04", "at": "Kẻ săn mồi há",
  "layout": "Chú chó {DINGO} bị gai nhọn chọc nghẹn cứng họng, vội vàng khạc nhè ra bãi cát, lắc đầu ngao ngán lè lưỡi bỏ chạy.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene04", "at": "Và sau khi thoát", "id": "L58",
  "layout": "{HERO} thở phào xẹp bớt không khí, đứng chớp mắt tinh nghịch giữa hoàng hôn sa mạc chuẩn bị phô diễn dáng đi tàng hình độc nhất vô nhị.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene04", "at": "Và nếu như cơn",
  "layout": "Bão cát sa mạc ập đến với những cuồng phong cát đỏ rực; {HERO} đứng trước bão cát không hề sợ hãi.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene04", "at": "Bốn bàn chân có",
  "layout": "Kỹ năng đào hầm thần tốc: 4 chân {HERO} cào cát xoay tít mù như máy xúc mini, trong 30 giây đã lặn mất tăm dưới lòng cát sâu 10cm tránh bão cát.",
  "stickers": [
   {"at": "30 giây", "side": "L", "y": 370, "value": "30 GIÂY", "label": "ĐÀO HẦM THẦN TỐC", "target": [0.25, 0.45]},
   {"at": "10cm", "side": "L", "y": 470, "value": "SÂU 10CM", "label": "LẶN DƯỚI LÒNG CÁT", "target": [0.25, 0.58]}
  ],
  "impacts": []
 },
 {
  "scene": "scene04", "at": "Nó bước một chân",
  "layout": "Vũ điệu robot lá khô: {HERO} bước 1 chân rồi giật cục lắc lư người 2-3 nhịp như cành cây khô trước gió, làm chim săn mồi mất dấu thị giác.",
  "stickers": [{"at": "2-3 nhịp", "side": "R", "y": 400, "value": "GIẬT CỤC", "label": "DÁNG ĐI LÁ KHÔ", "target": [0.75, 0.5]}],
  "impacts": []
 },
 {
  "scene": "scene04", "at": "Dáng đi robot giật",
  "layout": "Tầm nhìn từ trên cao của chim săn mồi: hình ảnh {HERO} nhấp nhô hòa tan vào chuyển động của bụi cỏ khô sa mạc, biến mất khỏi radar thị giác.",
  "stickers": [], "impacts": []
 },

 # --- SCENE 05: 21:00 ĐÊM ---
 {
  "scene": "scene05", "at": 0,
  "layout": "BÊN TRÁI đồng hồ điểm 21:00 đêm; Ở GIỮA cát sa mạc tỏa nhiệt cực nhanh; BÊN PHẢI nhiệt kế tụt dốc thê thảm xuống dưới 10°C lạnh giá. {NO_HERO}.",
  "stickers": [{"at": "dưới 10°C", "side": "L", "y": 390, "value": "< 10°C", "label": "ĐÊM LẠNH THẤU XƯƠNG", "target": [0.28, 0.48]}],
  "impacts": []
 },
 {
  "scene": "scene05", "at": "Giữa sự khắc nghiệt", "id": "L59",
  "layout": "{HERO} đứng trên mỏm đá đêm sa mạc, cơ thể bắt đầu biến đổi màu sắc kỳ ảo như một chú tắc kè hoa thông minh.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene05", "at": "Vào buổi trưa nắng",
  "layout": "So sánh hai màu áo giáp của {HERO}: BÊN TRÁI màu vàng cát nhạt phản xạ nhiệt trưa hè; BÊN PHẢI màu nâu xám sẫm hấp thụ nhiệt đêm lạnh.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene05", "at": "Màu da đen tối",
  "layout": "{HERO} ngụy trang thành một hòn đá vô tri giữa bãi cát đỏ sa mạc Red Centre; hấp thụ từng tia nhiệt lượng tàn dư giữ ấm cơ thể.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene05", "at": "Đồng thời, màu sắc", "id": "L60",
  "layout": "Bóng đêm sa mạc bao trùm: một con cú đêm bay lượn sát mặt đất nhưng không tài nào phát hiện ra {HERO} đang ẩn mình như tảng đá sa mạc.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene05", "at": "Đặc biệt vào những",
  "layout": "Trạng thái ngủ đông sa mạc: {HERO} nằm cuộn tròn dưới hang cát ấm áp, nhịp tim giảm xuống chỉ còn vài nhịp mỗi phút tiết kiệm năng lượng.",
  "stickers": [{"at": "vài nhịp", "side": "R", "y": 390, "value": "NGỦ ĐÔNG", "label": "NHỊP TIM TỐI THIỂU", "target": [0.75, 0.48]}],
  "impacts": []
 },
 {
  "scene": "scene05", "at": "Nó nằm bất động",
  "layout": "Chú thằn lằn bình yên ngủ say dưới lòng đất cát, bên trên là ánh trăng bạc rọi xuống cồn cát sa mạc tĩnh mịch huyền ảo.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene05", "at": "Và quý vị có",
  "layout": "Thằn lằn sừng Bắc Mỹ bắn tia máu đỏ rực từ khóe mắt xua đuổi chó sói; một bức tranh tư liệu so sánh sinh động. {NO_HERO}.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene05", "at": "còn Thằn Lằn Quỷ", "id": "L61",
  "layout": "{HERO} cười tươi vỗ ngực tự hào khẳng định: 'Thằn Lằn Quỷ Gai Úc tôi có giáp gai thép và đầu giả là đủ bá chủ sa mạc rồi!'.",
  "stickers": [], "impacts": []
 },

 # --- SCENE 06: 03:00 RẠNG SÁNG & BÓNG ĐEN ---
 {
  "scene": "scene06", "at": 0,
  "layout": "BÊN TRÁI đồng hồ điểm 03:00 rạng sáng; Ở GIỮA cồn cát lộng gió lạnh buốt; BÊN PHẢI {REPORTER} đang đứng tác nghiệp những phút cuối. {NO_HERO}.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene06", "at": "Một sinh vật nhỏ", "id": "L62",
  "layout": "Chân dung kiên cường của {HERO}: một chú thằn lằn nhỏ bé nhưng ngự trị sa mạc khắc nghiệt nhất hành tinh suốt hàng triệu năm qua.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene06", "at": "Biến làn da thành",
  "layout": "Bức tranh tôn vinh bản lĩnh tự nhiên: {HERO} đứng kiêu hãnh trên đỉnh cồn cát, biểu tượng cho sức sống kiên cường qua hàng triệu năm lịch sử.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene06", "at": "Hành trình 24 giờ",
  "layout": "Màn hình chiếu khổng lồ ở trung tâm sân khấu bật sáng với ánh hào quang nước màu xanh ngọc bích lung linh huyền ảo. {NO_HERO}.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene06", "at": "Xin gửi tới quý",
  "layout": "Manh mối số 1: BÓNG ĐEN BÍ ẨN (solid black silhouette) của một chú cá đang ngắm bắn tỉa tia nước nén cực mạnh hạ gục con mồi cách xa 3m kèm dấu hỏi '?'. {NO_HERO}.",
  "stickers": [
   {"at": "BÓNG ĐEN BÍ ẨN", "side": "R", "y": 360, "value": "BÓNG ĐEN", "label": "QUÁI KIỆT TẬP 20", "target": [0.75, 0.42]},
   {"at": "3m", "side": "L", "y": 420, "value": "BẮN XA 3M", "label": "TIA NƯỚC NÉN CAO", "target": [0.25, 0.5]}
  ],
  "impacts": []
 },
 {
  "scene": "scene06", "at": "Thứ hai, bộ não",
  "layout": "Manh mối số 2 & 3: Tia khúc xạ ánh sáng qua mặt nước được bộ não tính toán chính xác; rãnh vòm miệng nén nước xé toạc cánh côn trùng. {NO_HERO}.",
  "stickers": [{"at": "rãnh vòm miệng", "side": "R", "y": 390, "value": "ĐẠI BÁC", "label": "TÍNH TOÁN KHÚC XẠ", "target": [0.75, 0.48]}],
  "impacts": []
 },
 {
  "scene": "scene06", "at": "có nhận ra bóng đen",
  "layout": "BÓNG ĐEN BÍ ẨN dưới mặt nước với dấu hỏi chấm '?' nhấp nháy phát sáng; xung quanh là các bong bóng bình luận '? ? ?' kêu gọi khán giả dự đoán. {NO_HERO}.",
  "stickers": [], "impacts": []
 },
 {
  "scene": "scene06", "at": "Phóng viên sinh tồn",
  "layout": "BÊN TRÁI {REPORTER} và {HERO} vẫy tay chào tạm biệt; BÊN PHẢI tấm biển gỗ đề chữ 'HẸN GẶP LẠI Ở TẬP 20 VỚI SIÊU XẠ THỦ BẮN TỈA DƯỚI NƯỚC!'. {NO_HERO}.",
  "stickers": [], "impacts": []
 }
]

shorts_beats = [
 {
  "at": 0,
  "layout": "KHUNG HÌNH DỌC 9:16: {REPORTER} giơ chiếc đồng hồ 05:00 sáng giữa sa mạc đỏ rực, dòng chữ lớn 'UỐNG NƯỚC BẰNG BÀN CHÂN?!' xuất hiện nổi bật phía trên.",
  "stickers": []
 },
 {
  "at": "Một sinh vật không",
  "layout": "KHUNG HÌNH DỌC 9:16: Chân dung {HERO} đứng trên nền cát sa mạc khô khốc, ngửa mặt lên trời cười tự tin không cần cúi đầu tìm nước.",
  "stickers": []
 },
 {
  "at": "Đó chính là Thằn",
  "layout": "KHUNG HÌNH DỌC 9:16: {HERO} toàn thân phủ kín hàng trăm chiếc gai nón nhọn hoắt như cỗ xe tăng tí hon, chiếc mũ safari và nơ đỏ ngộ nghĩnh.",
  "stickers": [{"at": "20cm", "side": "L", "y": 620, "value": "DÀI 20CM", "label": "XE TĂNG SA MẠC", "target": [0.5, 0.45]}]
 },
 {
  "at": "Làn da của nó",
  "layout": "KHUNG HÌNH DỌC 9:16: Phóng to mạng lưới rãnh mao dẫn trên da {HERO}: các hạt sương đọng quanh chân bắt đầu được hút vào rãnh da.",
  "stickers": [{"at": "mao dẫn", "side": "R", "y": 640, "value": "MAO DẪN", "label": "RÃNH HÚT NƯỚC", "target": [0.55, 0.48]}]
 },
 {
  "at": "tự động hút từng", "id": "S11",
  "layout": "KHUNG HÌNH DỌC 9:16: Các giọt sương mai từ bàn chân tự động bị hút ngược chiều trọng lực chảy dọc sống lưng chạy thẳng vào miệng {HERO}.",
  "stickers": []
 },
 {
  "at": "Mỗi ngày, nó kiên",
  "layout": "KHUNG HÌNH DỌC 9:16: {HERO} phóng chiếc lưỡi dính màu hồng siêu tốc quét sạch đàn kiến đen Iridomyrmex chạy ngang qua bãi cát.",
  "stickers": [{"at": "2.500", "side": "L", "y": 630, "value": "2.500 CON", "label": "ĐẠI TIỆC KIẾN ĐEN", "target": [0.5, 0.46]}]
 },
 {
  "at": "Khi bị kẻ săn",
  "layout": "KHUNG HÌNH DỌC 9:16: {HERO} giấu đầu thật vào giữa 2 chân trước, ngóc chiếc bướu gai đầu giả sắc nhọn sau gáy lên lừa kẻ săn mồi cắn vào.",
  "stickers": [{"at": "đầu giả", "side": "R", "y": 650, "value": "ĐẦU GIẢ", "label": "LỪA KẺ SĂN MỒI", "target": [0.55, 0.5]}]
 },
 {
  "at": "lừa kẻ thù cắn",
  "layout": "KHUNG HÌNH DỌC 9:16: Chó hoang Dingo ngoạm trúng bướu gai nhọn hoắt, ôm mồm sưng vù khóc thét bỏ chạy.",
  "stickers": []
 },
 {
  "at": "Chưa hết, nó còn",
  "layout": "KHUNG HÌNH DỌC 9:16: {HERO} hít khí phồng to cơ thể gấp đôi thành một quả cầu gai bọc thép tròn xoe, gai nhọn chĩa tứ phía không thể nuốt.",
  "stickers": [{"at": "gấp đôi", "side": "L", "y": 640, "value": "GẤP ĐÔI", "label": "QUẢ CẦU GAI BỌC THÉP", "target": [0.5, 0.48]}]
 },
 {
  "at": "Vậy là bí mật",
  "layout": "KHUNG HÌNH DỌC 9:16: {HERO} bước đi trên đỉnh cồn cát đỏ sa mạc rực rỡ ánh bình minh, biểu tượng cho cỗ xe tăng sinh tồn hoàn hảo khép lại câu chuyện.",
  "stickers": []
 },
 {
  "at": "ngự trị chảo lửa sa mạc",
  "layout": "KHUNG HÌNH DỌC 9:16: Toàn cảnh sa mạc Red Centre nước Úc rực rỡ ánh rạng đông, Thằn Lằn Quỷ Gai uy nghi ngự trị khép lại câu chuyện trọn vẹn.",
  "stickers": []
 }
]

storyboard = {
 "_doc": "Storyboard for Episode 19 Than Lan Quy Gai",
 "characters": chars,
 "side_characters": [],
 "shorts_title_lines": ["UỐNG NƯỚC BẰNG CHÂN?!", "QUÁI KIỆT SA MẠC ÚC"],
 "skip_numbers": [],
 "long": long_beats,
 "shorts": shorts_beats
}

with open("projects/tap-19-than-lan-quy-gai/specs/storyboard.json", "w", encoding="utf8") as f:
    json.dump(storyboard, f, ensure_ascii=False, indent=1)

print(f"storyboard.json generated: {len(long_beats)} long beats, {len(shorts_beats)} shorts beats.")
