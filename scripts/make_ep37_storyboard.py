import json, re
from pathlib import Path

ep_path = Path("projects/tap-37-lac-da-sa-mac/episode.json")
with open(ep_path, "r", encoding="utf-8") as f:
    ep = json.load(f)

storyboard_data = {
    "_doc": "Mỗi câu/ý thoại = 1 beat = 1 ảnh riêng. at = 3-5 chữ CHÉP NGUYÊN VĂN lời đọc dạng phụ đề, DUY NHẤT trong chương.",
    "visual_style": "tỉ lệ {AR}; phong cách Mirage Oasis & Arabian Caravan Watercolor (tranh màu nước sa mạc Ả Rập kết hợp hoạt hình comic 2D whiteboard, nét cọ loang màu nước mềm mại ấm áp, chi tiết thảm dệt Ba Tư cổ điển, ống nghiệm, nhiệt kế sa mạc, biểu đồ điện tâm đồ nhịp sinh học tinh tế, màu sắc vàng cát chói chang điểm xuyết lam ngọc turquoise óng ánh; NỀN TRẮNG TINH hoàn toàn, không watermark, không logo; chủ thể nằm gọn trong khung, chừa lề trắng)",
    "style_label": "Mirage Oasis & Arabian Caravan Watercolor",
    "characters": {
        "HERO": "chú lạc đà một bướu hoạt hình ngộ nghĩnh, bộ lông màu vàng cát mịn màng, quàng chiếc khăn rằn sa mạc hoa văn Ả Rập màu đỏ-trắng quanh cổ, đeo tai nghe ống nghe y tế của bác sĩ, biểu cảm thong dong điềm tĩnh, chiếc bướu cao vút trên lưng",
        "HERO_S": "chú lạc đà một bướu đeo ống nghe bác sĩ và khăn rằn sa mạc",
        "NO_HERO": "KHÔNG có chú lạc đà một bướu quàng khăn rằn trong cảnh này",
        "Y_TA_FENNEC": "Cô y tá Cáo Sa Mạc Fennec tai to mặc áo blouse trắng cầm bảng kẹp nhiệt độ",
        "BAC_SI_GERBIL": "Bác sĩ nội trú Chuột Nhảy Gerbil đeo kính tròn cầm ống tiêm mini",
        "CHUYEN_GIA_KEN_KEN": "Bác sĩ Kền Kền già đeo kính lão cầm biểu đồ điện tâm đồ",
        "DU_MUC_BEDOUIN": "Người du mục Bedouin mặc áo choàng thong dong nhóm lửa",
        "BENH_NHAN_NGUOI": "Bệnh nhân người que choáng váng vì sốc nhiệt sa mạc",
        "BAC_SI_CAP_CUU": "Bác sĩ cấp cứu hối hả đo nhịp tim"
    },
    "side_characters": ["Y_TA_FENNEC", "BAC_SI_GERBIL", "CHUYEN_GIA_KEN_KEN", "DU_MUC_BEDOUIN"],
    "shorts_side_characters": ["BENH_NHAN_NGUOI", "BAC_SI_CAP_CUU"],
    "shorts_title_lines": [
        "CỖ MÁY LỌC NƯỚC",
        "SA MẠC 50°C"
    ],
    "skip_numbers": [],
    "long": [],
    "shorts": []
}

# Scene 1: Nhập viện cấp cứu (12 beats)
s1_beats = [
    {"at": 0, "layout": "Phòng cấp cứu dã chiến Sahara mở ra: Bác sĩ trưởng {HERO} đứng bên bàn hội chẩn, tay chỉ vào biểu đồ điện tâm đồ sa mạc màu nước lung linh.", "stickers": [], "impacts": []},
    {"at": "tiếp nhận một bệnh nhân vô cùng kỳ lạ", "layout": "Bệnh nhân lạc đà thong dong bước vào lều y tế dã chiến, xung quanh là cồn cát sa mạc vàng rực phản chiếu ánh mặt trời. {HERO_S}.", "stickers": [], "impacts": []},
    {"at": "chảo lửa 50°C", "layout": "Nhiệt kế sa mạc thủy ngân dâng cao chạm mốc 50 độ C đỏ rực: Cát bốc hơi nóng hầm hập. {NO_HERO}.", "stickers": [{"at": "50°C", "side": "R", "y": 360, "value": "50°C", "label": "chảo lửa sa mạc", "target": [0.65, 0.45]}], "impacts": []},
    {"at": "hai tuần ròng rã", "layout": "Bản đồ vệ tinh sa mạc Sahara kéo dài hai tuần không có bóng một giọt nước: {HERO} vẫn nhai cỏ khô thảnh thơi.", "stickers": [{"at": "2 tuần", "side": "L", "y": 400, "value": "2 TUẦN", "label": "nhịn nước liên tục", "target": [0.35, 0.45]}], "impacts": []},
    {"at": "huyết áp ổn định tuyệt đối", "layout": "Máy đo huyết áp y tế kim chỉ vạch xanh an toàn tuyệt đối: {HERO} mỉm cười nháy mắt với các bác sĩ.", "stickers": [], "impacts": []},
    {"at": "mang tên khoa học Camelus dromedarius", "layout": "Hồ sơ bệnh án bìa da cổ phong cách Ả Rập mở ra, ghi rõ danh pháp khoa học Camelus dromedarius với hoa văn màu nước lam ngọc. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "Cỗ Máy Lọc Nước Sa Mạc", "layout": "{HERO} tạo dáng kiêu hãnh với chiếc ống nghe bác sĩ lấp lánh dưới ánh nắng sa mạc rực rỡ.", "stickers": [], "impacts": []},
    {"at": "rơi vào trạng thái sốc nhiệt", "layout": "Một anh chàng người que ngất lịm trên cát nóng vì kiệt nước, trên đầu hiện biểu tượng giọt nước cạn kiệt màu đỏ báo động. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "48 giờ đồng hồ", "layout": "Đồng hồ cát thời gian 48 giờ chảy xiết: Mô hình tim người que ngừng đập vì trụy tuần hoàn. {NO_HERO}.", "stickers": [{"at": "48 giờ", "side": "R", "y": 380, "value": "48 GIỜ", "label": "giới hạn người tử vong", "target": [0.68, 0.45]}], "impacts": []},
    {"at": "chỉ số sinh tồn của bệnh nhân", "layout": "Cô y tá Cáo Fennec tai to cầm bảng kẹp hồ sơ báo cáo chỉ số mất nước vượt ngưỡng 25% an toàn. {NO_HERO}.", "stickers": [{"at": "25%", "side": "L", "y": 390, "value": "25%", "label": "mất nước cơ thể", "target": [0.35, 0.45]}], "impacts": []},
    {"at": "15% lượng nước trong cơ thể", "layout": "Cột mốc so sánh tử vong: Người ngừng thở ở mức mất nước 15%, còn lạc đà vẫn chịu tải tới 40% trọng lượng. {NO_HERO}.", "stickers": [{"at": "15%", "side": "R", "y": 370, "value": "15%", "label": "người trụy tim", "target": [0.65, 0.45]}, {"at": "40%", "side": "L", "y": 420, "value": "40%", "label": "lạc đà chịu tải", "target": [0.35, 0.5]}], "impacts": []},
    {"at": "mở tập hồ sơ bệnh án số một", "layout": "{HERO} lật giở trang hồ sơ bệnh án số 1 có con dấu sáp đỏ uy tín, chuẩn bị bóc tách bí ẩn chiếc bướu.", "stickers": [], "impacts": []}
]

# Scene 2: Bệnh án số 1: Chiếc bướu mỡ (12 beats)
s2_beats = [
    {"at": 0, "layout": "Bức tranh giải phẫu bướu lạc đà màu nước phong cách cổ điển: Chiếc bướu cao sừng sững phát sáng màu vàng kim ấm áp. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "bồn chứa nước di động khổng lồ", "layout": "Hình vẽ hài hước một chiếc bồn inox chứa nước gắn trên lưng lạc đà bị đánh dấu gạch chéo màu đỏ to tướng: Lầm tưởng kinh điển. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "chụp cộng hưởng từ và sinh thiết", "layout": "Màn hình máy MRI y tế chiếu rõ cấu trúc bên trong chiếc bướu: Toàn bộ là mô mỡ lipid vàng óng, không hề có giọt nước nào. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "nặng tới 40 kg", "layout": "Cân y tế đo trọng lượng bướu mỡ nhảy số từ 40 kg đến 80 kg: {HERO} đứng vỗ vỗ chiếc bướu kiêu hãnh.", "stickers": [{"at": "40 kg", "side": "R", "y": 370, "value": "40 KG", "label": "khối lượng bướu mỡ", "target": [0.65, 0.45]}], "impacts": []},
    {"at": "sinh tồn suốt cả tháng trời", "layout": "{HERO} thong thả bước đi trên con đường tơ lụa giữa sa mạc mênh mông suốt 30 ngày đêm không cần dừng ăn. {HERO_S}.", "stickers": [{"at": "30 ngày", "side": "L", "y": 390, "value": "30 NGÀY", "label": "nhịn ăn liên tục", "target": [0.35, 0.45]}], "impacts": []},
    {"at": "tại sao mỡ lại tập trung hết lên lưng", "layout": "Bác sĩ nội trú Chuột Nhảy Gerbil đeo kính tròn thắc mắc chỉ tay vào lưng {HERO}.", "stickers": [], "impacts": []},
    {"at": "phân bố đều dưới da", "layout": "Hình ảnh chú gấu bắc cực béo múp míp mặc áo phao dày cộp toát mồ hôi đầm đìa dưới nắng sa mạc. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "nấu chín từ bên trong", "layout": "Mô phỏng nhiệt học: Cơ thể bị om nhiệt màu đỏ rực như nồi áp suất nếu mỡ bao quanh toàn thân. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "gom toàn bộ lượng mỡ cách nhiệt", "layout": "Sơ đồ luồng nhiệt: Bướu mỡ trên lưng hoạt động như chiếc ô dù phản xạ toàn bộ tia nắng mặt trời gay gắt. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "nhiệt lượng tỏa thẳng ra môi trường", "layout": "Vùng bụng và bốn chân của {HERO} tỏa ra các luồng khí mát màu xanh lam, giúp cơ thể tản nhiệt siêu tốc.", "stickers": [], "impacts": []},
    {"at": "oxy hóa chất béo diễn ra", "layout": "Phương trình phản ứng sinh hóa phát sáng: 1 gam mỡ lipid phân giải tạo ra 1,1 gam nước chuyển hóa nội sinh. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "tự cấp ẩm cho từng tế bào", "layout": "{HERO} mỉm cười sảng khoái như vừa được uống một ly nước mát ngọt lành ngay giữa biển cát.", "stickers": [], "impacts": []}
]

# Scene 3: Bệnh án số 2: Tế bào hồng cầu oval (12 beats)
s3_beats = [
    {"at": 0, "layout": "Kính hiển vi y khoa phóng đại giọt máu màu nước đỏ thắm: Các tế bào hồng cầu hình oval bơi lội mềm mại. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "hình đĩa lõm hai mặt tròn trịa", "layout": "Hồng cầu hình tròn của con người bị vón cục tắc nghẽn trong lòng mao mạch máu hẹp màu đỏ sẫm. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "hồng cầu của lạc đà lại có hình oval", "layout": "Cận cảnh tế bào hồng cầu hình oval của {HERO} lướt nhẹ nhàng qua ngã ba mao mạch như những chiếc ca nô siêu tốc. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "đặc quánh lại như si-rô", "layout": "Ống nghiệm chứa máu sánh đặc màu đỏ thẫm nhưng các hồng cầu oval vẫn tự do chuyển động không hề đông tụ. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "uống một lượng nước khổng lồ", "layout": "Cô y tá Fennec mở to mắt kinh ngạc trước bể nước 200 lít khổng lồ đang cạn dần. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "130 lít nước", "layout": "{HERO} cúi đầu uống nước ừng ực tại ốc đảo xanh tươi, đồng hồ bấm giờ nhảy vọt đến con số 200 lít nước chỉ trong 15 phút.", "stickers": [{"at": "130 lít nước", "side": "R", "y": 360, "value": "130 LÍT", "label": "uống trong tích tắc", "target": [0.65, 0.45]}, {"at": "15 phút", "side": "L", "y": 420, "value": "15 PHÚT", "label": "thời gian uống", "target": [0.35, 0.5]}], "impacts": []},
    {"at": "ngộ độc nước sẽ xảy ra tức khắc", "layout": "Mô hình tế bào hồng cầu người bị nạp nước quá nhanh căng phồng rồi vỡ bùm như bong bóng nước. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "phồng to gấp 240%", "layout": "Hồng cầu hình oval của lạc đà giãn nở đàn hồi kỳ diệu từ kích thước nhỏ phồng to gấp 240% vẫn nguyên vẹn. {NO_HERO}.", "stickers": [{"at": "240%", "side": "R", "y": 370, "value": "240%", "label": "độ giãn nở hồng cầu", "target": [0.68, 0.45]}], "impacts": []},
    {"at": "những quả bóng bay co giãn vô hạn", "layout": "Đồ họa so sánh: Hồng cầu oval như những quả bóng cao su siêu dẻo bảo vệ toàn diện hệ tuần hoàn. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "thể tích máu của nó có thể tăng vọt gấp đôi", "layout": "Bác sĩ Chuột Nhảy Gerbil kiểm tra biểu đồ dung tích tuần hoàn dâng cao ngoạn mục. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "lớp cơ trơn đàn hồi siêu đẳng", "layout": "Mặt cắt động mạch chủ co giãn nhịp nhàng, hấp thụ trọn vẹn lưu lượng máu khổng lồ mà không hề tăng huyết áp. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "hồ chứa di động đàn hồi vô song", "layout": "{HERO} tràn đầy sinh lực sau khi uống no nước, đôi mắt sáng bừng sẵn sàng cho chuyến vượt sa mạc mới.", "stickers": [], "impacts": []}
]

# Scene 4: Bệnh án số 3: Quả thận siêu lọc (11 beats)
s4_beats = [
    {"at": 0, "layout": "Sơ đồ giải phẫu hệ tiết niệu màu nước: Hai quả thận của lạc đà phát sáng màu lam ngọc turquoise với cấu trúc siêu lọc phức tạp. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "quai Henle dài gấp nhiều lần", "layout": "Kính hiển vi bóc tách ống thận: Quai Henle kéo dài sâu vào tủy thận tạo gradient nồng độ muối cực cao. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "vắt kiệt từng phân tử nước", "layout": "Mô phỏng 3D dòng dịch lọc: Từng giọt nước li ti bị hút ngược trở lại mao mạch máu, chỉ giữ lại cặn bã đậm đặc. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "sánh đặc như si-rô đặc quẹt", "layout": "Ống nghiệm hứng giọt nước tiểu cô đặc sánh như mật ong với nồng độ muối gấp đôi nước biển. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "chất thải rắn của bệnh nhân khô khốc", "layout": "Cô y tá Fennec nhặt một viên phân lạc đà khô cong như viên sỏi tròn không hề dính tay. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "nhóm lửa đun nấu ngay tại chỗ", "layout": "Người du mục Bedouin dùng phân lạc đà khô nhóm bếp lửa bập bùng đun ấm trà sa mạc nghi ngút khói. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "hiệu suất tái sử dụng lên tới 99%", "layout": "{HERO} đứng bên biểu đồ tuần hoàn nước khép kín đạt hiệu suất tái hấp thu 99% kỷ lục. {HERO_S}.", "stickers": [{"at": "99%", "side": "R", "y": 380, "value": "99%", "label": "tái hấp thu nước", "target": [0.65, 0.45]}], "impacts": []},
    {"at": "nhà máy xử lý nước tuần hoàn", "layout": "Mô hình đồ họa nhà máy lọc nước vi mô lồng ghép bên trong cơ thể khỏe mạnh của {HERO}.", "stickers": [], "impacts": []},
    {"at": "cấu trúc ba ngăn chuyên biệt", "layout": "Dạ dày 3 ngăn của lạc đà với lớp niêm mạc dày cộp tiết chất nhầy bảo vệ chống gai góc đâm thủng. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "cây xương rồng sa mạc", "layout": "{HERO} thản nhiên nhai cành xương rồng đầy gai nhọn hoắt như đang thưởng thức món kẹo giòn tan.", "stickers": [], "impacts": []},
    {"at": "niêm mạc không hề bị xước xát", "layout": "Cận cảnh khoang miệng khỏe khoắn của {HERO} với những gai thịt sừng hóa bền chắc như da thuộc.", "stickers": [], "impacts": []}
]

# Scene 5: Bệnh án số 4: Ống thở ngưng tụ hơi nước (12 beats)
s5_beats = [
    {"at": 0, "layout": "Hình ảnh giải phẫu đường hô hấp: Khoang mũi và khí quản của lạc đà được vẽ bằng nét màu nước mềm mại tinh xảo. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "bốc hơi vô hình nhưng cực kỳ nguy hiểm", "layout": "Hơi thở người que phả ra làn sương trắng mang theo hơi ẩm quý giá bốc hơi tan biến vào không khí sa mạc. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "vách xoắn ốc cuộn nhiều tầng", "layout": "Mặt cắt khoang mũi lạc đà: Mê cung xương xoăn phủ lớp niêm mạc hút ẩm phức tạp nhiều tầng như tổ ong. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "ngưng tụ hơi nước lại lập tức", "layout": "Hơi nước ấm trong luồng khí thở ra chạm vào vách mũi lạnh ngưng tụ thành các giọt nước li ti lăn ngược vào trong. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "tái hấp thu vào máu", "layout": "Mạng lưới mao mạch niêm mạc mũi hút trọn các giọt nước ngưng tụ, chỉ thải khí khô ra ngoài. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "bão cát có tràn vào phổi", "layout": "Bão cát sa mạc cuồn cuộn đỏ rực ập đến che khuất cả bầu trời, gió rít dữ dội. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "cơ vòng van một chiều", "layout": "Cận cảnh mũi {HERO}: Hai lỗ mũi tự động khép chặt lại như chiếc van khí nén ngăn mọi hạt cát lọt vào.", "stickers": [], "impacts": []},
    {"at": "hàng mi dày hai tầng", "layout": "Đôi mắt to tròn của {HERO} chớp nhẹ với hai tầng lông mi dài rậm rạp và màng chớp trong suốt chắn bụi. {HERO_S}.", "stickers": [], "impacts": []},
    {"at": "dao động linh hoạt từ 34°C", "layout": "Đồ thị thân nhiệt sinh học: Đường cong nhiệt độ cơ thể dao động từ 34°C đêm lạnh lên 41°C trưa hè bỏng rát. {NO_HERO}.", "stickers": [{"at": "34°C", "side": "L", "y": 380, "value": "34°C", "label": "thân nhiệt ban đêm", "target": [0.35, 0.45]}, {"at": "41°C", "side": "R", "y": 380, "value": "41°C", "label": "thân nhiệt trưa hè", "target": [0.65, 0.45]}], "impacts": []},
    {"at": "hoàn toàn không cần đổ mồ hôi", "layout": "{HERO} bước đi khô ráo mát mẻ, tiết kiệm hàng chục lít nước mồ hôi quý giá mỗi ngày.", "stickers": [], "impacts": []},
    {"at": "hệ thống điều hòa sinh học", "layout": "Biểu tượng âm dương cân bằng giữa ánh nắng mặt trời và làn gió sa mạc ôn hòa bao quanh {HERO}.", "stickers": [], "impacts": []},
    {"at": "hòa làm một với nhịp điệu nhiệt độ", "layout": "{HERO} ung dung rảo bước trên đỉnh cồn cát vàng óng ả, toát lên phong thái bậc thầy sinh tồn.", "stickers": [], "impacts": []}
]

# Scene 6: Ra viện an toàn (11 beats)
s6_beats = [
    {"at": 0, "layout": "Phòng hội đồng y khoa trang nghiêm: Toàn thể y bác sĩ đứng nghiêm chào đón buổi lễ ký kết giấy xuất viện danh dự. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "ký giấy xuất viện cho bệnh nhân", "layout": "Dấu mộc y tế đỏ thắm đóng cộp chữ 'XUẤT VIỆN — THỂ LỰC PHI THƯỜNG' xuống hồ sơ bệnh án của {HERO}.", "stickers": [], "impacts": []},
    {"at": "đỉnh cao của công nghệ phỏng sinh học", "layout": "Mô hình nghiên cứu y học hiện đại kết hợp hình ảnh vi mô tế bào hồng cầu lạc đà trên màn hình số 3D. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "nhà khoa học NASA", "layout": "Tàu con thoi vũ trụ bay vào không gian sâu: Túi dịch truyền nhân tạo phỏng sinh học mô phỏng hồng cầu oval lạc đà. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "bậc thầy sinh tồn vĩ đại của tự nhiên", "layout": "Bác sĩ Kền Kền già nâng ly trà thảo mộc sa mạc chúc mừng kỳ tích sinh học của {HERO}.", "stickers": [], "impacts": []},
    {"at": "thong dong sải bước trên những đồi cát", "layout": "Toàn cảnh đoàn lữ hành lạc đà bước đi thong thả lúc hoàng hôn sa mạc buông xuống đỏ rực tuyệt đẹp. {HERO_S}.", "stickers": [], "impacts": []},
    {"at": "cỗ máy sinh học tinh vi bậc nhất", "layout": "Hình bóng {HERO} in bóng trên cồn cát mênh mông, tỏa sáng hào quang của thiên tài tạo hóa.", "stickers": [], "impacts": []},
    {"at": "giải pháp y sinh nào làm bạn kinh ngạc nhất", "layout": "Mô hình đồ họa tổng hợp 4 vũ khí: Bướu mỡ, Hồng cầu oval, Thận siêu lọc và Mũi ngưng tụ hơi thở. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "bình luận bên dưới nhé", "layout": "{HERO} mỉm cười cầm chiếc bảng kẹp hồ sơ chỉ vào ô bình luận mời gọi khán giả tương tác.", "stickers": [], "impacts": []},
    {"at": "bấm đăng ký kênh để đón xem Tập 38", "layout": "Banner giới thiệu bí ẩn của Tập 38: Bóng dáng chú Dê Núi Bắc Mỹ đứng thăng bằng trên vách đá 90 độ thẳng đứng. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "chuyến hành trình khám phá những kỳ quan sinh học", "layout": "{HERO} cùng toàn thể đội ngũ y bác sĩ sa mạc vẫy tay chào tạm biệt khán giả trong ánh hoàng hôn ấm áp.", "stickers": [], "impacts": []}
]

# Set scene IDs
for b in s1_beats: b["scene"] = "scene01"
for b in s2_beats: b["scene"] = "scene02"
for b in s3_beats: b["scene"] = "scene03"
for b in s4_beats: b["scene"] = "scene04"
for b in s5_beats: b["scene"] = "scene05"
for b in s6_beats: b["scene"] = "scene06"

storyboard_data["long"] = [
    *s1_beats,
    *s2_beats,
    *s3_beats,
    *s4_beats,
    *s5_beats,
    *s6_beats
]

# Shorts (12 beats)
shorts_beats = [
    {"at": 0, "layout": "Cận cảnh hồ nước sa mạc với đồng hồ đếm ngược: Lạc đà há miệng uống nước như vòi rồng cuốn sạch 200 lít nước.", "stickers": [{"at": "200 lít nước", "side": "R", "y": 620, "value": "200 LÍT", "label": "dung tích uống", "target": [0.65, 0.45]}]},
    {"at": "vỡ hồng cầu chết ngay lập tức", "layout": "Tế bào hồng cầu người bị nổ tung từng mảnh với tia sét cảnh báo tử vong ngay tức khắc. {NO_HERO}.", "stickers": []},
    {"at": "Đó chính là Lạc Đà Sa Mạc", "layout": "{HERO} xuất hiện oai vệ, quàng khăn rằn Ả Rập đỏ-trắng và đeo ống nghe bác sĩ lấp lánh.", "stickers": []},
    {"at": "không hề chứa một giọt nước nào", "layout": "Chiếc bướu trên lưng được bóc tách tia X: Một khối mỡ năng lượng 40 kg màu vàng óng chống sốc nhiệt. {NO_HERO}.", "stickers": [{"at": "40 kg", "side": "R", "y": 600, "value": "40 KG", "label": "bướu mỡ năng lượng", "target": [0.65, 0.45]}]},
    {"at": "năm mươi độ C", "layout": "Nhiệt kế sa mạc chạm ngưỡng 50 độ C bỏng rát: Cát sa mạc bốc hơi nóng nhưng {HERO} vẫn nhai cỏ thảnh thơi.", "stickers": [{"at": "50°C", "side": "L", "y": 620, "value": "50°C", "label": "nhiệt độ môi trường", "target": [0.35, 0.45]}]},
    {"at": "tế bào hồng cầu hình oval", "layout": "Kính hiển vi bóc tách các tế bào hồng cầu hình oval thuôn dài lướt nhẹ nhàng qua mao mạch máu. {NO_HERO}.", "stickers": []},
    {"at": "phồng to gấp 240%", "layout": "Hồng cầu oval phồng to gấp 240% như quả bóng cao su hấp thụ nước an toàn tuyệt đối. {NO_HERO}.", "stickers": [{"at": "240%", "side": "R", "y": 620, "value": "240%", "label": "giãn nở hồng cầu", "target": [0.68, 0.45]}]},
    {"at": "quả thận siêu lọc", "layout": "Mô phỏng quả thận siêu lọc với quai Henle dài vắt kiệt từng giọt ẩm quý giá. {NO_HERO}.", "stickers": []},
    {"at": "cô đặc nước tiểu thành si-rô", "layout": "Ống nghiệm nước tiểu sánh đặc như si-rô chứng minh khả năng giữ nước tuyệt đỉnh. {NO_HERO}.", "stickers": []},
    {"at": "nhịn uống suốt 30 ngày", "layout": "{HERO} bước đi hiên ngang giữa chảo lửa sa mạc suốt 30 ngày đêm không cần uống một giọt nước.", "stickers": [{"at": "30 ngày", "side": "L", "y": 620, "value": "30 NGÀY", "label": "nhịn uống tối đa", "target": [0.35, 0.45]}]},
    {"at": "giữa chảo lửa sa mạc", "layout": "Toàn cảnh cồn cát Sahara trải dài vô tận dưới ánh hoàng hôn sa mạc rực rỡ tuyệt mỹ. {NO_HERO}.", "stickers": []},
    {"at": "vẫn sống khỏe re", "layout": "{HERO} mỉm cười giơ ngón tay cái số một khẳng định danh hiệu Cỗ Máy Lọc Nước vô địch thiên nhiên.", "stickers": []}
]

storyboard_data["shorts"] = shorts_beats

out_path = Path("projects/tap-37-lac-da-sa-mac/specs/storyboard.json")
out_path.parent.mkdir(parents=True, exist_ok=True)
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(storyboard_data, f, ensure_ascii=False, indent=2)

print(f"Generated {len(storyboard_data['long'])} long beats and {len(storyboard_data['shorts'])} shorts beats to {out_path}")

