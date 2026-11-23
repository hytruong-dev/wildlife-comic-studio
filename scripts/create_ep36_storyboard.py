import json, re
from pathlib import Path

ep_path = Path("projects/tap-36-chim-go-kien/episode.json")
with open(ep_path, "r", encoding="utf-8") as f:
    ep = json.load(f)

storyboard_data = {
    "_doc": "Mỗi câu/ý thoại = 1 beat = 1 ảnh riêng. at = 3-5 chữ CHÉP NGUYÊN VĂN lời đọc dạng phụ đề, DUY NHẤT trong chương.",
    "visual_style": "tỉ lệ {AR}; phong cách Steampunk Mechanical Blueprint & Kinetic Crosshatch (bản vẽ kỹ thuật cơ khí steampunk kết hợp hoạt hình comic 2D whiteboard, nét bút kim kỹ thuật và nét cắt chéo crosshatch sắc sảo, chi tiết bánh răng đồng thau, thước kẹp, đồng hồ đo áp lực, vạch đo gia tốc G tinh tế, màu sắc giấy da kỹ thuật nâu vàng sepia điểm xuyết xanh lam cyan blueprint); NỀN TRẮNG TINH hoàn toàn, không watermark, không logo; chủ thể nằm gọn trong khung, chừa lề trắng",
    "style_label": "Steampunk Mechanical Blueprint & Kinetic Crosshatch",
    "characters": {
        "HERO": "chú chim gõ kiến hoạt hình với bộ lông đen sọc trắng sắc nét, chỏm mào đỏ rực như ngọn lửa đội mũ bảo hộ kỹ sư tí hon màu vàng đồng, đeo kính lúp cơ khí steampunk một mắt bên phải, chiếc mỏ nhọn cứng cáp màu xám thép, biểu cảm thông minh lém lỉnh",
        "HERO_S": "chú chim gõ kiến mào đỏ rực đội mũ bảo hộ kỹ sư tí hon, đeo kính lúp steampunk",
        "NO_HERO": "KHÔNG có chú chim gõ kiến mào đỏ trong cảnh này"
    },
    "side_characters": [
        "Kỹ sư Cú Vọ già đeo kính lão tròn đọc tài liệu",
        "Chuột chũi thợ mỏ mặc yếm cầm máy khoan mini",
        "Sóc bay thợ hàn đeo kính đen cầm que hàn",
        "Khỉ đầu chó thanh tra an toàn lao động cầm bảng kẹp hồ sơ"
    ],
    "shorts_side_characters": [
        "Người que ngất xỉu vì va đầu vào gỗ",
        "Kỹ sư cơ khí choáng váng đo gia tốc"
    ],
    "shorts_title_lines": [
        "CỖ MÁY GIẢM CHẤN",
        "1.200 G ĐỈNH CAO"
    ],
    "skip_numbers": [],
    "long": [],
    "shorts": []
}

# Scene 1: Khởi động phòng thử nghiệm: Bài toán gia tốc 1.200 G (12 beats)
s1_beats = [
    {"at": 0, "layout": "Phòng thử nghiệm cơ khí thiên nhiên hoang dã mở ra: {HERO} đứng trên bục giảng trước tấm bảng vẽ kỹ thuật blueprint khổng lồ, tay cầm thước chỉ bản vẽ động lực học va đập.", "stickers": [], "impacts": []},
    {"at": "bóc tách bản vẽ kỹ thuật", "layout": "Cận cảnh bàn mổ cơ khí: Bản vẽ giải phẫu chim gõ kiến phóng to với các đường nét blueprint xanh cyan và thông số bánh răng steampunk tinh xảo. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "Đối tượng thí nghiệm trên bàn mổ", "layout": "{HERO} tạo dáng hiên ngang bên cạnh một khúc gỗ sồi cổ thụ dày cộp, chiếc mỏ nhọn lấp lánh như mũi khoan kim cương.", "stickers": [], "impacts": []},
    {"at": "va đầu vào cánh cửa tủ bếp", "layout": "Một anh chàng người que ngốc nghếch ôm trán nhăn nhó vì đập đầu vào cánh tủ bếp, trên đầu bay vòng vòng mấy ngôi sao choáng váng. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "Báo cáo thông số kỹ thuật", "layout": "Khỉ đầu chó thanh tra cầm máy đo gia tốc kỹ thuật số, mắt trợn tròn trước màn hình hiển thị số nhảy loạn xạ. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "1.200 G thưa các đồng nghiệp", "layout": "Đồng hồ đo áp lực và gia tốc steampunk kim chỉ vạch đỏ rực ở mức cực đại: {HERO} chỉ tay vào con số 1.200 G với nụ cười tự tin.", "stickers": [{"at": "1.200 G", "side": "R", "y": 360, "value": "1.200 G", "label": "gia tốc va chạm cực đại", "target": [0.65, 0.45]}], "impacts": []},
    {"at": "phi công tiêm kích quân sự", "layout": "Một phi công quân sự trong buồng lái phản lực bị lực ép dính chặt vào ghế ngồi, khuôn mặt méo mó chịu tải gia tốc 9 G. {NO_HERO}.", "stickers": [{"at": "chín G", "side": "L", "y": 400, "value": "9 G", "label": "giới hạn người ngất xỉu", "target": [0.35, 0.45]}], "impacts": []},
    {"at": "tai nạn giao thông xe hơi", "layout": "Hiện trường thử nghiệm va chạm ô tô crash-test: Đầu xe bẹp dúm khi đâm vào tường bê tông ở vận tốc cao, hình nộm vỡ vụn. {NO_HERO}.", "stickers": [{"at": "100 G", "side": "R", "y": 380, "value": "100 G", "label": "tai nạn xe hơi tử vong", "target": [0.68, 0.42]}], "impacts": []},
    {"at": "đập đầu vào thân gỗ", "layout": "{HERO} mổ liên thanh như súng máy vào thân gỗ, tốc độ nhanh đến mức tạo thành vệt mờ chuyển động ngoạn mục.", "stickers": [], "impacts": []},
    {"at": "12.000 lần mỗi ngày", "layout": "Đồng hồ đếm nhịp cơ khí steampunk nhảy số liên hồi, ghi nhận kỷ lục 12.000 cú đập: {HERO} vừa đập mỏ vừa huýt sáo thảnh thơi.", "stickers": [{"at": "12.000 lần", "side": "R", "y": 370, "value": "12.000 LẦN", "label": "tần suất đập mỗi ngày", "target": [0.65, 0.45]}], "impacts": []},
    {"at": "Nếu các kỹ sư chế tạo xe hơi", "layout": "Một chiếc xe bọc thép viễn tưởng bọc lớp vỏ xốp giảm chấn đặc biệt lăn bánh hất tung chướng ngại vật mà không hề móp méo. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "Mỗi cú va chạm chỉ diễn ra", "layout": "Đồ thị sóng âm và xung lực dao động cực nhanh: {HERO} đứng bên biểu đồ va chạm một phần ngàn giây siêu ngắn.", "stickers": [{"at": "một phần ngàn giây", "side": "L", "y": 390, "value": "1 MS", "label": "thời gian 1 cú va chạm", "target": [0.35, 0.45]}], "impacts": []}
]

# Scene 2: Lớp phòng vệ số 1: Chiếc lưỡi quấn quanh sọ não như dây đai xe đua (12 beats)
s2_beats = [
    {"at": 0, "layout": "Bản vẽ bóc tách lớp phòng vệ số 1: Mô hình cơ khí hệ cơ xương móng Hyoid phát sáng màu vàng đồng trên nền giấy blueprint. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "lưỡi bên trong cũng ngắn ngủn", "layout": "Một chú gà con hoạt hình ngơ ngác thè chiếc lưỡi ngắn cũn cỡn ra so sánh với chiếc mỏ dài ngoằng của {HERO}.", "stickers": [], "impacts": []},
    {"at": "rạch lớp da đầu của Cỗ Máy", "layout": "Kỹ sư Cú Vọ già đeo kính lúp soi vào kính hiển vi, hai mắt mở to kinh ngạc tột độ. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "chiếc lưỡi của nó không nằm trong họng", "layout": "Sóc bay thợ hàn cầm đèn chiếu soi vào bản vẽ sọ não: Lưỡi chạy ngược ra sau gáy kỳ lạ. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "dài gấp ba lần chiều dài chiếc mỏ", "layout": "{HERO} há mỏ thè chiếc lưỡi dài ngoằng quấn lượn như sợi dây thừng ma thuật khiến muôn loài tròn mắt thán phục.", "stickers": [{"at": "gấp ba lần", "side": "R", "y": 370, "value": "GẤP 3 LẦN", "label": "chiều dài lưỡi so với mỏ", "target": [0.68, 0.45]}], "impacts": []},
    {"at": "tách ra làm hai nhánh", "layout": "Sơ đồ giải phẫu 3D: Hai nhánh xương móng Hyoid chạy qua lỗ mũi, tách đôi luồn vòng qua đỉnh đầu rồi hợp lại sau gáy. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "dây đai an toàn năm điểm", "layout": "Một tay đua xe công thức 1 ngồi trong buồng lái thắt chặt bộ dây đai an toàn 5 điểm nhiều lớp chắc chắn. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "Trong đúng một phần ngàn giây", "layout": "Cận cảnh siêu tốc cơ bắp Hyoid thắt chặt: Hệ thống dây chằng co rút khóa chặt khối óc trước khi mỏ chạm gỗ. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "ghìm chặt khối não bộ", "layout": "{HERO} tập trung cao độ, toàn bộ hệ cơ đầu và gáy gồng cứng như một khối thép đúc vững chãi.", "stickers": [], "impacts": []},
    {"at": "không bị đập dội vào thành xương", "layout": "Hình ảnh so sánh hộp sọ: Bộ não của chim gõ kiến được khóa chặt êm ái, hoàn toàn không có dao động lắc lư. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "chứa các sợi gân đàn hồi", "layout": "Mô hình lò xo vi mô và sợi cơ đàn hồi giảm chấn steampunk co giãn mềm dẻo như cao su tự nhiên. {NO_HERO}.", "stickers": [{"at": "50%", "side": "L", "y": 380, "value": "50%", "label": "độ dãn gân đàn hồi", "target": [0.35, 0.45]}], "impacts": []},
    {"at": "thò lưỡi sâu vào tổ kiến", "layout": "{HERO} luồn chiếc lưỡi dẻo dai vào mê cung trong thân cây mục, đầu lưỡi có ngạnh sắc bắt gọn đàn mối béo ngậy.", "stickers": [], "impacts": []}
]

# Scene 3: Lớp phòng vệ số 2: Vật liệu xốp bọt khí nano hấp thụ 99% xung lực (12 beats)
s3_beats = [
    {"at": 0, "layout": "Bản vẽ bóc tách tầng 2: Hộp sọ chim gõ kiến được chiếu sáng mặt cắt ngang, để lộ lớp cấu trúc xốp bọt khí phức tạp. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "xương sọ là một khối xương đặc", "layout": "Mô hình sọ người bằng thạch cao đặc cứng và giòn rụm bị búa gõ nhẹ đã nứt toác một đường. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "xung lực truyền thẳng qua lớp xương cứng", "layout": "Sóng chấn động màu đỏ rực dội thẳng vào mô não mềm của con người gây chấn động não nghiêm trọng. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "dưới kính hiển vi điện tử quét nano", "layout": "{HERO} chỉnh tiêu cự kính hiển vi nano steampunk, hình ảnh phóng to hàng triệu lần hiện ra trên màn hình tinh thể lỏng.", "stickers": [], "impacts": []},
    {"at": "chứa hàng triệu khoang rỗng", "layout": "Cấu trúc vi mô xốp như tổ ong với hàng triệu vi bọt khí nano xếp so le đa hướng cực kỳ tinh vi. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "Đại học Công nghệ Bắc Kinh", "layout": "Phòng thí nghiệm vật liệu tiên tiến: Các nhà khoa học phân tích biểu đồ hấp thụ xung lực của xương chim gõ kiến. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "đệm cao su giảm chấn", "layout": "Khối vật liệu xốp phỏng sinh học đàn hồi ấn xuống rồi bung nở lại nguyên trạng không tì vết. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "99,7% năng lượng cơ học", "layout": "{HERO} giơ bảng thống kê năng lượng: 99,7% lực va đập bị triệt tiêu, chỉ còn vệt sóng nhỏ xíu 0,3% sót lại.", "stickers": [{"at": "99,7%", "side": "R", "y": 360, "value": "99,7%", "label": "xung lực bị hấp thụ", "target": [0.65, 0.45]}, {"at": "0,3%", "side": "L", "y": 420, "value": "0,3%", "label": "lực còn sót lại vào não", "target": [0.35, 0.5]}], "impacts": []},
    {"at": "chuyển hóa trực tiếp thành nhiệt năng", "layout": "Bản đồ nhiệt hồng ngoại: Đầu của {HERO} hơi ấm lên màu vàng cam nhẹ khi năng lượng cơ học biến thành nhiệt.", "stickers": [], "impacts": []},
    {"at": "gõ liên hồi 20 nhịp", "layout": "{HERO} ngừng gõ mỏ, lấy chiếc khăn bông lau mồ hôi trên trán và uống một ngụm nước làm mát máy móc.", "stickers": [{"at": "20 nhịp", "side": "R", "y": 380, "value": "20 NHỊP", "label": "mỗi đợt gõ liên hồi", "target": [0.68, 0.45]}], "impacts": []},
    {"at": "mô phỏng phần tử hữu hạn ba chiều", "layout": "Màn hình 3D xoay vòng mô hình hộp sọ với các dải màu phân tích ứng suất uốn và chịu nén tuyệt hảo. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "tối ưu hóa cấu trúc chịu lực", "layout": "Một chiếc mũ bảo hiểm phi hành gia công nghệ cao được thiết kế lớp lót phỏng sinh học mô phỏng xương sọ chim gõ kiến. {NO_HERO}.", "stickers": [], "impacts": []}
]

# Scene 4: Lớp phòng vệ số 3: Thiết kế mỏ lệch hướng chuyển dòng năng lượng xuống thân (11 beats)
s4_beats = [
    {"at": 0, "layout": "Ống kính phóng đại zoom thẳng vào chiếc mỏ của {HERO}: Mũi mỏ sắc lạnh màu xám kim loại với các thước đo micromet bao quanh.", "stickers": [], "impacts": []},
    {"at": "hai nửa mỏ trên và mỏ dưới", "layout": "Hình vẽ chiếc kẹp gắp đối xứng đơn giản bị đánh dấu chéo màu đỏ: Sai lầm cơ bản của mắt thường. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "máy quét laser công nghiệp", "layout": "Máy chụp cắt lớp và quét laser công nghiệp xoay vòng quanh mỏ chim gõ kiến, bộc lộ sai lệch kích thước bất ngờ. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "mỏ dưới của nó dài hơn mỏ trên", "layout": "Chuột chũi thợ mỏ cầm thước kẹp điện tử đo đạc mỏ dưới dài hơn mỏ trên một đoạn rõ ràng. {NO_HERO}.", "stickers": [{"at": "mỏ dưới của nó dài hơn mỏ trên", "side": "R", "y": 380, "value": "LỆCH PHA", "label": "hàm dưới dài hơn", "target": [0.65, 0.45]}], "impacts": []},
    {"at": "chạm vào mặt gỗ trước", "layout": "Mô phỏng va chạm slow-motion: Hàm dưới chạm mặt gỗ trước phân số giây, bẻ gãy đường truyền lực trực diện. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "góc bẻ hướng lực 60°", "layout": "Sơ đồ véc-tơ lực học màu xanh lam bẻ cong một góc 60 độ, hướng dòng chấn động đi xuống vùng ức và sống lưng. {NO_HERO}.", "stickers": [{"at": "60°", "side": "L", "y": 390, "value": "60 ĐỘ", "label": "góc bẻ hướng lực xung", "target": [0.35, 0.45]}], "impacts": []},
    {"at": "phiến sừng keratin xếp lớp", "layout": "Kính hiển vi bóc tách lớp vỏ keratin xếp vảy lợp ngói như áo giáp rồng, trượt nhẹ lên nhau phân tán chấn động. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "nguyên mẫu hoàn hảo mà các kỹ sư quân sự", "layout": "Mũi khoan công nghiệp và đầu đạn xuyên giáp hiện đại được rèn theo thiết kế vát góc mỏ chim gõ kiến. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "cơ bắp vùng cổ", "layout": "{HERO} gồng cơ bắp vùng cổ cuồn cuộn như lực sĩ thể hình, hai gân cổ nổi rõ khỏe khoắn.", "stickers": [], "impacts": []},
    {"at": "lao về phía trước", "layout": "Quỹ đạo chuyển động của mỏ chim gõ kiến: Đường thẳng tắp tuyệt đối như tia laser, không hề có rung lắc phương ngang. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "không bị vặn xoắn sang hai bên", "layout": "{HERO} giơ ngón tay cái số một khẳng định độ chuẩn xác cơ học của đường khoan thẳng hàng.", "stickers": [], "impacts": []}
]

# Scene 5: Lớp phòng vệ số 4: Màng chớp một mili-giây bảo vệ nhãn cầu không văng ra ngoài (12 beats)
s5_beats = [
    {"at": 0, "layout": "Chi tiết giải phẫu mắt mở ra: Một nhãn cầu lớn long lanh với hệ thống cơ vận nhãn phức tạp bao quanh. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "giảm tốc đột ngột trong nháy mắt", "layout": "Đồ thị giảm tốc cắm thẳng đứng xuống đáy vực: Biểu tượng áp lực nội nhãn tăng vọt màu đỏ cảnh báo nguy hiểm. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "nhãn cầu sẽ lập tức văng ra", "layout": "Một chiếc kính bơi bị áp lực thổi bung văng ra xa để minh họa thảm họa áp lực va đập. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "mắt của nó vẫn mở to thao láo", "layout": "{HERO} đeo kính bảo hộ kỹ sư, hai mắt sáng quắc chăm chú ngắm sâu bọ bên trong kẽ gỗ.", "stickers": [], "impacts": []},
    {"at": "cửa chập quang học siêu tốc", "layout": "Mô hình cửa trập ống kính máy ảnh cơ khí steampunk đóng mở xoạch xoạch với tốc độ ánh sáng. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "mí mắt thứ ba trong suốt", "layout": "Cận cảnh mắt {HERO}: Lớp màng chớp mỏng dính trong suốt hạ xuống che kín toàn bộ con ngươi.", "stickers": [], "impacts": []},
    {"at": "10.000 khung hình trên giây", "layout": "Máy quay điện ảnh tốc độ siêu cao ghi lại từng mili-giây khoảnh khắc màng chớp hạ xuống trước cú va đập. {NO_HERO}.", "stickers": [{"at": "10.000 khung hình", "side": "R", "y": 380, "value": "10.000 FPS", "label": "tốc độ máy quay siêu tốc", "target": [0.65, 0.45]}], "impacts": []},
    {"at": "chiếc kính bảo hộ lao động", "layout": "Màng chớp ngăn chặn mọi vụn gỗ và dăm mùn cưa li ti không thể bắn vào giác mạc. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "trong tích tắc 1 mili-giây", "layout": "Đồng hồ bấm giờ điện tử đếm 0.001 giây: Màng chớp mở bung ra ngay khi mỏ vừa nảy khỏi mặt gỗ. {NO_HERO}.", "stickers": [{"at": "1 mili-giây", "side": "L", "y": 390, "value": "1 MS", "label": "tốc độ mở màng chớp", "target": [0.35, 0.45]}], "impacts": []},
    {"at": "20 lần mỗi giây", "layout": "{HERO} chớp mắt lia lịa 20 nhịp một giây đồng bộ hoàn hảo với từng cú gõ mỏ không hề trễ một nhịp.", "stickers": [{"at": "20 lần", "side": "R", "y": 370, "value": "20 LẦN/S", "label": "tần suất chớp mắt đồng bộ", "target": [0.68, 0.45]}], "impacts": []},
    {"at": "robot công nghiệp nào hiện nay", "layout": "Một cánh tay robot công nghiệp hiện đại bị kẹt khớp bánh răng tóe lửa vì quá tải chu kỳ vận hành. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "vận hành liên tục 12.000 chu kỳ", "layout": "{HERO} tự hào lau kính lúp cơ khí, nở nụ cười rạng rỡ của một nhà vô địch bền bỉ.", "stickers": [], "impacts": []}
]

# Scene 6: Nghiệm thu bản vẽ: Đỉnh cao cơ chế giảm chấn phỏng sinh học (11 beats)
s6_beats = [
    {"at": 0, "layout": "Toàn cảnh phòng hội đồng kỹ thuật: Bản vẽ tổng thể 4 tầng giảm chấn của {HERO} được treo trang trọng ở giữa phòng.", "stickers": [], "impacts": []},
    {"at": "không chỉ là một loài chim kiếm ăn", "layout": "Hình ảnh {HERO} đứng bên cạnh các biểu tượng công nghệ đỉnh cao: Tàu vũ trụ, xe đua và giáp chiến đấu. {HERO_S}.", "stickers": [], "impacts": []},
    {"at": "Tuyên bố nghiệm thu", "layout": "Dấu mộc đỏ đóng 'NGHIỆM THU ĐẠT CHUẨN XUẤT SẮC' cộp xuống bản thiết kế chim gõ kiến. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "kỹ sư vũ trụ của NASA", "layout": "Trạm vũ trụ quốc tế và hộp đen tàu con thoi được bọc vật liệu xốp phỏng sinh học chống va đập rơi tự do. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "tập đoàn thiết bị thể thao", "layout": "Một chiếc mũ bảo hiểm bóng bầu dục và xe đua F1 thế hệ mới gắn đai Hyoid bảo vệ đốt sống cổ tối ưu. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "tiếng gõ cốc cốc vang dội", "layout": "Khu rừng nguyên sinh thanh bình buổi sớm mai: Bóng dáng {HERO} cần mẫn gõ mỏ trên thân cây cổ thụ.", "stickers": [], "impacts": []},
    {"at": "bài ca thử nghiệm va chạm", "layout": "Các nốt nhạc cơ khí steampunk và bánh răng vàng bay bổng xung quanh chiếc mỏ thần kỳ của {HERO}.", "stickers": [], "impacts": []},
    {"at": "chiếc lưỡi quấn quanh sọ", "layout": "Mô hình đồ họa tương tác hiển thị lại 2 vũ khí đỉnh cao: Dây đai Hyoid và Hộp sọ xốp bọt khí nano. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "bình luận bên dưới nhé", "layout": "{HERO} cầm bảng vẽ chỉ vào ô bình luận nhấp nháy, mời gọi các kỹ sư cùng thảo luận sôi nổi.", "stickers": [], "impacts": []},
    {"at": "bấm đăng ký kênh để đón xem Tập 37", "layout": "Banner giới thiệu bí ẩn của Tập 37: Bóng dáng chú Lạc Đà Sa Mạc bước đi trên cồn cát mênh mông. {NO_HERO}.", "stickers": [], "impacts": []},
    {"at": "tôn vinh những kỳ quan kỹ thuật", "layout": "{HERO} đứng cùng toàn thể đội ngũ kỹ sư hoang dã vẫy tay chào khán giả với nụ cười tự hào.", "stickers": [], "impacts": []}
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
    {"at": 0, "layout": "Cận cảnh anh chàng người que ngốc nghếch đập đầu vào thân gỗ với tần số cực nhanh, mắt nổ đom đóm.", "stickers": [{"at": "hai mươi lần", "side": "R", "y": 620, "value": "20 LẦN/S", "label": "tần số đập đầu", "target": [0.65, 0.45]}]},
    {"at": "Hộp sọ sẽ vỡ vụn", "layout": "Mô hình sọ người vỡ vụn từng mảnh với tia sét chấn động đỏ rực cảnh báo tử vong ngay tức khắc. {NO_HERO}.", "stickers": []},
    {"at": "Thế nhưng loài Chim Gõ Kiến", "layout": "{HERO} xuất hiện oai phong lẫm liệt, đội mũ kỹ sư tí hon và đeo kính lúp cơ khí steampunk một mắt.", "stickers": []},
    {"at": "12.000 lần mỗi ngày", "layout": "{HERO} gõ mỏ liên thanh như súng máy cơ khí vào thân gỗ sồi, đồng hồ đếm số nhảy vọt lên mười hai ngàn lần.", "stickers": [{"at": "12.000 lần", "side": "R", "y": 600, "value": "12.000 LẦN", "label": "mỗi ngày", "target": [0.65, 0.45]}]},
    {"at": "1.200 G", "layout": "Đồng hồ đo gia tốc rung lắc dữ dội kim chỉ vạch đỏ rực 1.200 G cực hạn: {HERO} vẫn nháy mắt thảnh thơi.", "stickers": [{"at": "1.200 G", "side": "L", "y": 620, "value": "1.200 G", "label": "gia tốc va chạm", "target": [0.35, 0.45]}]},
    {"at": "120 lần giới hạn tử vong", "layout": "Cột mốc so sánh lực va đập: Con người gục ngã ở 10 G trong khi chim gõ kiến đứng hiên ngang ở đỉnh 1.200 G. {NO_HERO}.", "stickers": [{"at": "120 lần", "side": "R", "y": 640, "value": "GẤP 120 LẦN", "label": "chịu tải người", "target": [0.68, 0.45]}]},
    {"at": "chiếc lưỡi kỳ dị dài gấp ba", "layout": "{HERO} há mỏ phóng ra chiếc lưỡi dài ngoằng uốn lượn kỳ ảo gấp 3 lần mỏ của mình.", "stickers": [{"at": "gấp ba lần", "side": "L", "y": 620, "value": "DÀI GẤP 3", "label": "chiều dài lưỡi", "target": [0.35, 0.45]}]},
    {"at": "luồn ngược ra sau gáy", "layout": "Mặt cắt sọ 3D: Chiếc lưỡi tách đôi luồn vòng quanh hộp sọ như chiếc đai an toàn xe đua chuyên nghiệp. {NO_HERO}.", "stickers": []},
    {"at": "ghìm chặt não bộ", "layout": "Toàn bộ hệ cơ bắp đầu và cổ gồng cứng khóa chặt bộ não nằm im thin thít không hề rung rơ một ly. {NO_HERO}.", "stickers": []},
    {"at": "hộp sọ xốp bọt khí", "layout": "Kính hiển vi bóc tách vật liệu nano xốp bọt khí của hộp sọ đang hấp thụ sóng chấn động. {NO_HERO}.", "stickers": []},
    {"at": "99,7%", "layout": "Toàn bộ 99,7% xung lực va chạm cơ học chuyển hóa lập tức thành nhiệt năng tỏa ra êm dịu. {NO_HERO}.", "stickers": [{"at": "99,7%", "side": "R", "y": 620, "value": "99,7%", "label": "tiêu tán lực", "target": [0.65, 0.45]}]},
    {"at": "kỳ quan cơ khí giảm chấn", "layout": "{HERO} mỉm cười giơ ngón tay cái kiêu hãnh giữa khung cảnh rừng xanh tươi sáng.", "stickers": []}
]

storyboard_data["shorts"] = shorts_beats

out_path = Path("projects/tap-36-chim-go-kien/specs/storyboard.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(storyboard_data, f, ensure_ascii=False, indent=2)

print(f"Generated {len(storyboard_data['long'])} long beats and {len(storyboard_data['shorts'])} shorts beats to {out_path}")
