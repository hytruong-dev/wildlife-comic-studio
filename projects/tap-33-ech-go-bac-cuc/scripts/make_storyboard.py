# -*- coding: utf-8 -*-
"""Generate complete specs/storyboard.json for Episode 33: Ếch Gỗ Bắc Cực (Wood Frog)
Format: F4 (Sinh Tồn 24h / Cực Hạn) | Visual Style: Cryo-Noir Graphic Novel & Frost Woodblock
Theme Effects (TASTE-75): cryo_survival (Frost Crystalline Stickers, Ice-Beam Spear Arrows, 6-Point Snowflake Reticles)
Strict Prompt Safety (TASTE-71): Zero copyright, Zero violence/gore, 100% funny cartoon arctic survival graphic novel.
TASTE-47 Compliant: All holds <= 15.0s (72 long beats). TASTE-56 Compliant: All holds <= 7.0s (13 shorts beats).
"""
import json
from pathlib import Path

P = Path("projects/tap-33-ech-go-bac-cuc")
(P / "specs").mkdir(parents=True, exist_ok=True)

storyboard = {
    "_doc": "Storyboard Tập 33 — Ếch Gỗ Bắc Cực (Wood Frog) F4 Sinh Tồn 24h Vùng Cực. Chạy: python src/episode/build_plans.py projects/tap-33-ech-go-bac-cuc",
    "characters": {
        "HERO": "chú Ếch Gỗ Bắc Cực hoạt hình da màu nâu đồng ngộ nghĩnh, đeo chiếc khăn len ấm áp màu xanh dương và cặp kính bảo hộ vùng cực (cute cartoon Alaskan wood frog wearing a cozy wool scarf and arctic safety goggles)",
        "HERO_S": "chú Ếch Gỗ Bắc Cực da màu nâu đồng đeo khăn len xanh dương và kính bảo hộ vùng cực",
        "NO_HERO": "KHÔNG có chú Ếch Gỗ trong cảnh này",
        "REPORTER": "chú chim cánh cụt phóng viên hoạt hình mặc áo phao lông thú ấm áp, cầm micro phỏng vấn run rẩy giữa trời tuyết rơi",
        "BEAR": "chú gấu Bắc Cực hoạt hình lông trắng to lớn mập mạp ngơ ngác, cầm một cành cây nhỏ gõ vào khối đá lạnh",
        "HEART_ICE": "nhân vật trái tim hoạt hình màu đỏ đội mũ len nhỏ bị bọc trong tinh thể băng xanh lam trong suốt",
        "DOCTOR": "bác sĩ cú mèo hoạt hình đeo kính cận tròn, mặc áo blouse trắng và cầm bảng theo dõi thông số sinh tồn"
    },
    "side_characters": [
        "REPORTER",
        "BEAR",
        "HEART_ICE",
        "DOCTOR"
    ],
    "shorts_side_characters": [
        "REPORTER",
        "BEAR",
        "DOCTOR"
    ],
    "shorts_title_lines": [
        "TIM NGỪNG ĐẬP 7 THÁNG:",
        "TỰ RÃ ĐÔNG BẬT NHẢY?!"
    ],
    "skip_numbers": [1],
    "long": [
        # ==================== SCENE 01: BÁO ĐỘNG VÙNG CỰC | ÂM 20 ĐỘ C Ở ALASKA ====================
        {
            "scene": "scene01",
            "at": 0,
            "layout": "Hiện trường bão tuyết Alaska mù mịt: {REPORTER} trùm áo phao lông thú to sụ, hai tay run bần bật cầm micro truyền hình trực tiếp giữa cơn lốc tuyết trắng xóa. {NO_HERO}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene01",
            "at": "tiểu bang Alaska",
            "layout": "Cận cảnh cột nhiệt kế sinh tồn cắm ngập trong đụn tuyết: Cột thủy ngân tụt dốc không phanh thẳng đứng xuống vạch âm hai mươi độ C đỏ rực với sương tuyết bám quanh. {NO_HERO}.",
            "stickers": [{"at": "-20°C", "value": "-20°C", "label": "nhiệt độ bắc cực", "side": "L", "y": 340, "target": [0.45, 0.55]}],
            "impacts": ["-20°C"]
        },
        {
            "scene": "scene01",
            "at": "Gió bắc cực gầm rú",
            "layout": "Minh họa cơn gió lốc vùng cực đóng băng mọi thứ: Luồng hơi nước thở ra từ miệng biến ngay thành chùm tinh thể băng rơi lả tả xuống mặt đất tuyết. {NO_HERO}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene01",
            "at": "và các mặt hồ",
            "layout": "Mặt cắt hồ nước ngọt Bắc Cực: Toàn bộ tầng nước mặt đóng băng thành một khối đá hoa cương dày đặc, bên dưới các sinh vật đều chìm vào giấc ngủ im lìm. {NO_HERO}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene01",
            "at": "Lũ gấu Bắc Cực",
            "layout": "Bức tranh so sánh sinh tồn mùa đông: {BEAR} cuộn tròn trong hang tuyết ấm áp, phía trên là đàn chim di cư bay về phương Nam theo hình chữ V. {NO_HERO}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene01",
            "at": "còn lũ chuột đồng",
            "layout": "Sơ đồ mặt cắt đất rừng taiga: Chú chuột đồng cuộn tròn trong chiếc tổ đào sâu cả mét dưới lòng đất ấm cúng, xung quanh chất đầy hạt dẻ dự trữ. {NO_HERO}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene01",
            "at": "Tôi không có lông vũ",
            "layout": "Hình ảnh hài hước: {HERO} đứng trên tảng băng trôi, mặc mỗi chiếc quần đùi da cóc tí hon, hai tay chống nạnh cười toe toét nhìn về phía {REPORTER}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene01",
            "at": "Ấy thế mà ngay dưới chân",
            "layout": "Lớp lá rụng và rêu mục trên mặt đất rừng: {HERO} đang thong thả nằm tựa lưng vào hòn đá nhỏ, đắp chiếc chăn lá cây mỏng manh như đang đi nghỉ dưỡng.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene01",
            "at": "Xin giới thiệu nhân vật chính",
            "layout": "Tấm áp phích hồ sơ định danh vùng cực Cryo-Noir: Chân dung dũng mãnh của {HERO} với huy hiệu Quái Kiệt Băng Giá phát sáng rực rỡ trên nền tinh thể băng tuyết.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene01",
            "at": "toàn cầu ngả mũ",
            "id": "L54",
            "layout": "Biểu đồ vinh danh Quái Kiệt Băng Giá: Chân dung {HERO} đứng trên bục vinh quang giữa các huân chương băng tuyết và cờ hiệu sinh tồn vùng cực.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene01",
            "at": "Toàn thân chú ếch gỗ",
            "layout": "Màn hình thước đo sinh trắc học vùng cực: Thước đo laser hiển thị chiều dài 5-7cm và chiếc cân đá mini hiện 8-15g của {HERO} bên cạnh một quả nho nhỏ.",
            "stickers": [
                {"at": "5-7cm", "value": "5-7CM", "label": "chiều dài cơ thể", "side": "L", "y": 330, "target": [0.4, 0.5]},
                {"at": "8-15g", "value": "8-15G", "label": "trọng lượng tí hon", "side": "R", "y": 410, "target": [0.65, 0.6]}
            ],
            "impacts": []
        },
        {
            "scene": "scene01",
            "at": "Làn da của nó",
            "id": "L55",
            "layout": "Bản vẽ phối màu ngụy trang vùng cực: Cận cảnh lớp da sần sùi màu nâu đồng của {HERO} hòa lẫn hoàn hảo vào thảm rêu rừng taiga và vỏ cây thông tuyết.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene01",
            "at": "như chiếc mặt nạ",
            "layout": "Cận cảnh đôi mắt của {HERO}: Hai vệt sọc đen sẫm kéo dài qua mắt như mặt nạ hiệp sĩ Zorro, đôi mắt tinh anh lấp lánh ánh nhìn kiên định trước bão tuyết.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene01",
            "at": "ở xứ ôn đới",
            "id": "L56",
            "layout": "So sánh sinh thái: Các chú ếch xanh thông thường co ro rúc dưới đáy bùn hồ nước lạnh run rẩy, nhìn lên thán phục lòng dũng cảm của {HERO} trên mặt đất.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene01",
            "at": "ở lì ngay trên nền rừng",
            "layout": "Đồng hồ sinh tồn đếm ngược: {HERO} khoanh tay ngồi thiền trên lớp rêu rừng taiga, xung quanh những bông tuyết bắt đầu phủ kín người biến thành một khối băng tảng.",
            "stickers": [],
            "impacts": []
        },

        # ==================== SCENE 02: MẦM ĐÁ NGOẠI BÀO | TỰ ĐÓNG BĂNG 70% CƠ THỂ ====================
        {
            "scene": "scene02",
            "at": 0,
            "layout": "Sơ đồ khoa học phân tử Cryo-Noir: Một giọt nước tinh khiết đang đóng băng, các phân tử nước kết tinh giãn nở và mọc ra những mũi gai băng nhọn hoắt như dao găm. {NO_HERO}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene02",
            "at": "dưới 0°C",
            "id": "L57",
            "layout": "Mô hình vật lý giãn nở thể tích: Khối băng trong suốt nở bung với các vết nứt rạn tỏa ra xung quanh, làm vỡ tung một ống nghiệm thủy tinh đo lường. {NO_HERO}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene02",
            "at": "Nếu hiện tượng đóng băng",
            "layout": "Hình ảnh kính hiển vi mô phỏng tế bào thông thường: Những mũi gai băng sắc lẹm đâm rách toạc màng tế bào, dịch nội bào tràn ra ngoài gây hoại tử hoàn toàn. {NO_HERO}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene02",
            "at": "trong tích tắc",
            "id": "L58",
            "layout": "Cảnh báo hoại tử mô: Hình vẽ đồ họa vi phẫu thuật cho thấy các mao mạch bị tắc nghẽn và đóng băng đỏ rực dưới kính hiển vi điện tử. {NO_HERO}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene02",
            "at": "Kính thưa các tinh thể đá",
            "layout": "{HERO} hóa thân thành chú cảnh sát giao thông vùng cực tí hon, tay cầm gậy chỉ huy điều hướng các tinh thể băng xếp hàng rồng rắn đi ra phía ngoài da.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene02",
            "at": "Và đó chính là lúc chiến thuật",
            "layout": "Trang bìa công trình nghiên cứu khoa học năm 1993 của tiến sĩ Jack Costanzo, bên cạnh là mô hình 3D phân tử protein tạo mầm đá phát sáng màu lam ngọc. {NO_HERO}.",
            "stickers": [{"at": "Năm 1993", "value": "NĂM 1993", "label": "công bố khoa học", "side": "L", "y": 350, "target": [0.45, 0.5]}],
            "impacts": []
        },
        {
            "scene": "scene02",
            "at": "Đại học Miami",
            "id": "L74",
            "layout": "Viện nghiên cứu sinh học Đại học Miami: Nhóm các nhà khoa học đang hào hứng quan sát mẫu huyết tương của chú ếch {HERO} dưới kính hiển vi điện tử. {NO_HERO}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene02",
            "at": "protein chuyên biệt",
            "id": "L59",
            "layout": "Cận cảnh chuỗi protein tạo mầm đá: Những hạt phân tử protein hình cầu màu lam ngọc phát sáng, đang hút các phân tử nước li ti lại gần tạo thành mạng lưới tinh thể có trật tự. {NO_HERO}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene02",
            "at": "hạ xuống mức -1°C đến -2°C",
            "layout": "Bảng đo vi khí hậu tế bào: Khi nhiệt độ chạm ngưỡng -1°C đến -2°C, các protein mầm đá hoạt động như nam châm gom các tinh thể băng về khoang ngoại bào. {NO_HERO}.",
            "stickers": [{"at": "-1°C đến -2°C", "value": "-1°..-2°C", "label": "ngưỡng mầm đá", "side": "R", "y": 360, "target": [0.55, 0.5]}],
            "impacts": []
        },
        {
            "scene": "scene02",
            "at": "Thay vì để băng đá",
            "layout": "Bản đồ giải phẫu cắt lớp cơ thể {HERO}: Băng đá đóng thành lớp giáp bảo vệ dày ở ổ bụng và dưới da, trong khi các cơ quan tim gan bên trong vẫn an toàn nguyên vẹn.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene02",
            "at": "rút dần nước lỏng",
            "layout": "Mô hình minh họa thẩm thấu nước: Tế bào nội bào nhẹ nhàng co lại một cách có kiểm soát như quả bóng xẹp bớt nước, nhường chỗ cho lớp băng ngoài khoang đệm.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene02",
            "at": "65-70%",
            "layout": "Biểu đồ tròn tỷ lệ thể tích nước cơ thể {HERO}: Mảng màu xanh lam ngọc chiếm trọn 70% tổng lượng nước hóa thành giáp băng bao bọc bên ngoài. {HERO_S}.",
            "stickers": [{"at": "65-70%", "value": "70% BĂNG", "label": "nước hóa băng đá", "side": "L", "y": 340, "target": [0.4, 0.55]}],
            "impacts": ["65-70%"]
        },
        {
            "scene": "scene02",
            "at": "70% cơ thể",
            "layout": "{HERO} trong tư thế siêu anh hùng khoác bộ giáp băng tinh thể trong suốt óng ánh, tự tin mỉm cười trước bão tuyết vùng cực.",
            "stickers": [],
            "impacts": []
        },

        # ==================== SCENE 03: BÃO ĐƯỜNG CẤP TỐC | GLUCOSE TĂNG VỌT 300 LẦN ====================
        {
            "scene": "scene03",
            "at": 0,
            "layout": "Tế bào sinh học đang đối mặt nguy cơ co rúm: Áp suất thẩm thấu đè nặng lên màng tế bào, chiếc còi báo động khẩn cấp màu đỏ nhấp nháy liên hồi. {NO_HERO}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene03",
            "at": "khiến tế bào bị mất nước",
            "id": "L60",
            "layout": "Hình ảnh mô phỏng quả bóng bay tế bào bị xì hơi teo tóp nhăn nhúm vì mất nước, biểu cảm nhân vật tế bào hoạt hình méo xệch kêu cứu. {NO_HERO}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene03",
            "at": "Ngay vào khoảnh khắc",
            "layout": "Hệ thống thần kinh cảm giác của {HERO}: Làn da chạm vào băng đá bắn ra tia sét tín hiệu sinh học chạy dọc sống lưng về trung tâm chỉ huy lá gan.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene03",
            "at": "Báo cáo chỉ huy trưởng",
            "layout": "Hình ảnh hài hước bên trong nhà máy lá gan: {HERO} đội mũ thuyền trưởng gạt cần van xả lũ màu vàng cam, mở toang các bồn chứa siro đường mật mía ngọt lịm.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene03",
            "at": "Những nghiên cứu đột phá",
            "layout": "Chân dung giáo sư Kenneth Storey trên bìa tạp chí khoa học năm 1988, bên cạnh là biểu đồ lá gan {HERO} phình to gấp nhiều lần chứa đầy kho Glycogen.",
            "stickers": [{"at": "năm 1988", "value": "NĂM 1988", "label": "nghiên cứu Storey", "side": "L", "y": 350, "target": [0.45, 0.5]}],
            "impacts": []
        },
        {
            "scene": "scene03",
            "at": "chiếm tới mười phần trăm",
            "id": "L61",
            "layout": "Cân đo nội tạng Bio-Lab: Chiếc cân điện tử cân lá gan màu nâu đỏ phình to bằng một phần mười cơ thể {HERO}, các khoang chứa đầy ắp những hạt Glycogen vàng lấp lánh.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene03",
            "at": "Chỉ trong vòng vài giờ",
            "layout": "Đồng hồ đo nồng độ đường huyết điện tử: Kim chỉ số vọt từ mức bình thường bay thẳng lên con số 300 lần với cột thủy tinh phát sáng màu vàng mật ong rực rỡ.",
            "stickers": [{"at": "100-300 lần", "value": "300 LẦN", "label": "glucose chống đông", "side": "R", "y": 340, "target": [0.65, 0.55]}],
            "impacts": ["100-300 lần"]
        },
        {
            "scene": "scene03",
            "at": "Nếu nồng độ đường huyết",
            "layout": "Hình ảnh so sánh y học: Bệnh nhân người sốt sắng trước kết quả tiểu đường cao, trong khi {HERO} đang thong thả nhâm nhi cốc siro đường vàng ươm cười khoái chí.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene03",
            "at": "tiêm insulin cấp cứu",
            "id": "L62",
            "layout": "Bệnh viện dã chiến hài hước: Chiếc xe cứu thương vùng cực nhấp nháy đèn còi với ống tiêm insulin to đùng, trong khi {HERO} đứng bên cạnh vỗ bụng cười tự hào.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene03",
            "at": "Song song với đường Glucose",
            "layout": "Mô hình phân tử Cryoprotectant: Các phân tử Glucose hình lục giác đan xen với hạt Urea bao bọc lấy các phân tử protein nội bào như chiếc khiên đệm siêu mềm. {NO_HERO}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene03",
            "at": "Siro này hạ điểm đông đặc",
            "layout": "Cận cảnh chất nguyên sinh bên trong tế bào {HERO}: Dung dịch duy trì ở dạng thạch gel sánh mịn màng, không một tinh thể đá nào có thể kết tủa bên trong.",
            "stickers": [],
            "impacts": []
        },

        # ==================== SCENE 04: CHẾT LÂM SÀNG | TIM 0 NHỊP SUỐT 7 THÁNG ====================
        {
            "scene": "scene04",
            "at": 0,
            "layout": "Băng giá phủ kín toàn cảnh rừng taiga: Đồng hồ đếm ngược sinh tồn 24h chạy về đúng con số 00:00:00, bão tuyết rít gào buốt lạnh âm hai mươi độ C. {NO_HERO}.",
            "stickers": [{"at": "24h", "value": "24H", "label": "đồng hồ sinh tồn", "side": "L", "y": 340, "target": [0.4, 0.45]}],
            "impacts": []
        },
        {
            "scene": "scene04",
            "at": "giai đoạn quyết định",
            "id": "L63",
            "layout": "Bão tuyết màn đêm cực hàn: Cơn lốc xoáy tuyết xanh thẫm bao trùm toàn cảnh rừng taiga, những cột băng đá nhọn hoắt mọc lên từ mặt đất như rừng chông tuyết.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene04",
            "at": "Trái tim bé bỏng của chú ếch gỗ",
            "layout": "Màn hình điện tâm đồ ECG theo dõi nhịp tim: Đồ thị nhịp tim từ 100 nhịp/phút tụt xuống 50 nhịp, 10 nhịp rồi tắt hẳn thành một đường chân trời phẳng lặng.",
            "stickers": [
                {"at": "100 nhịp/phút", "value": "100 NHỊP", "label": "nhịp tim ban đầu", "side": "L", "y": 330, "target": [0.35, 0.5]},
                {"at": "số không tròn trĩnh", "value": "0 NHỊP/P", "label": "tim ngừng đập hẳn", "side": "R", "y": 410, "target": [0.65, 0.55]}
            ],
            "impacts": ["số không tròn trĩnh"]
        },
        {
            "scene": "scene04",
            "at": "Cốc cốc cốc",
            "layout": "{BEAR} tò mò ngồi xổm bên tảng rêu tuyết, dùng que gỗ nhỏ gõ vào người chú ếch {HERO} đã đông cứng, phát ra âm thanh côm cốp như gõ đá cuội.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene04",
            "at": "Không còn một nhịp tim nào",
            "layout": "Màn hình điện não đồ EEG của {DOCTOR}: Chiếc kim vạch ra đường thẳng tắp 0% sóng não, bên cạnh là biểu tượng trái tim bị đóng băng hoàn toàn {HEART_ICE}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene04",
            "at": "đường chân trời thẳng tắp",
            "id": "L64",
            "layout": "Bản ghi điện não đồ EEG phóng đại: Màn hình oscilloscope màu xanh lá cây hiện đường chân trời thẳng tắp 0Hz phẳng lì, chiếc bút đo nằm im không một dao động. {NO_HERO}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene04",
            "at": "Xét theo mọi tiêu chuẩn",
            "id": "L75",
            "layout": "Bác sĩ cú mèo {DOCTOR} cầm chiếc búa phản xạ y tế gõ vào đầu gối chú ếch {HERO} đã đông cứng, lắc đầu xác nhận chết lâm sàng 100%.",
            "stickers": [{"at": "100%", "value": "100%", "label": "chết lâm sàng y học", "side": "R", "y": 350, "target": [0.6, 0.5]}],
            "impacts": []
        },
        {
            "scene": "scene04",
            "at": "Đôi mắt của nó đã chuyển sang",
            "layout": "Cận cảnh khuôn mặt đông đá của {HERO}: Đôi mắt đục ngầu như hai hòn bi ve thủy tinh, toàn thân cứng như thép nguội đọng lớp sương tuyết lấp lánh.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene04",
            "at": "từ độ cao 30cm",
            "layout": "Minh họa chú ếch đông đá rơi từ độ cao 30cm xuống mặt băng nảy tưng tưng côm cốp mà không hề trầy xước mô mềm trước ánh mắt thảng thốt của {BEAR}.",
            "stickers": [{"at": "30cm", "value": "30CM", "label": "thử nghiệm rơi", "side": "L", "y": 360, "target": [0.45, 0.5]}],
            "impacts": []
        },
        {
            "scene": "scene04",
            "at": "tiến sĩ Đôn Lác-xơn tại Viện Sinh học",
            "layout": "Tấm lịch mùa đông Bắc Cực lật trang liên tục từ tháng 10 đến tháng 4: Biểu đồ thời gian 7 tháng tương đương 200 ngày đêm ngủ đông hóa đá của {HERO}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene04",
            "at": "tim ngừng đập hoàn toàn này",
            "id": "L65",
            "layout": "Vũ trụ thời gian 4 mùa Bắc Cực: Hình ảnh quả cầu Trái Đất quay tròn qua các mùa tuyết phủ, chú ếch {HERO} hóa đá nằm im bất động thách thức dòng chảy thời gian.",
            "stickers": [
                {"at": "7 tháng", "value": "7 THÁNG", "label": "thời gian đông đá", "side": "L", "y": 330, "target": [0.35, 0.5]},
                {"at": "200 ngày", "value": "200 NGÀY", "label": "chịu cực lạnh", "side": "R", "y": 410, "target": [0.65, 0.55]}
            ],
            "impacts": []
        },

        # ==================== SCENE 05: KỲ TÍCH HỒI SINH | TRÁI TIM TỰ ĐẬP LẠI ====================
        {
            "scene": "scene05",
            "at": 0,
            "layout": "Ánh bình minh mùa xuân tháng 4 rọi xuống cánh rừng Bắc Cực: Băng tuyết bắt đầu tan chảy, những mầm rêu xanh non nhú lên khỏi mặt đất ẩm ướt. {NO_HERO}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene05",
            "at": "Nước tuyết tan nhỏ từng giọt",
            "id": "L66",
            "layout": "Mùa xuân rã đông cận cảnh: Từng giọt nước tuyết trong suốt lấp lánh rơi róc rách xuống thảm rêu xanh tươi, những bông hoa tuyết màu vàng nở rộ đón nắng mai. {NO_HERO}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene05",
            "at": "Và ngay tại giây phút này",
            "layout": "Sơ đồ so sánh cơ chế rã đông: Động vật có vú rã đông từ ngoài vào trong gây tổn thương tim, trong khi {HERO} rã đông từ sâu trong tâm thất ra ngoài. {HERO_S}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene05",
            "at": "bề mặt da bên ngoài",
            "id": "L67",
            "layout": "Sơ đồ nhiệt bức xạ: Sơ đồ nhiệt chụp cắt lớp cho thấy nhiệt lượng lan tỏa từ bên ngoài vào trong của một chú chuột, đối lập với nhiệt lượng tỏa ra từ tim của {HERO}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene05",
            "at": "Thình thịch! Thình thịch",
            "layout": "{HEART_ICE} bên trong lồng ngực chú ếch bắt đầu tỏa ra ánh hào quang ấm áp màu vàng cam, lớp băng tan chảy thành nước và trái tim bắt đầu co bóp đập lại rộn ràng.",
            "stickers": [],
            "impacts": ["Thình thịch"]
        },
        {
            "scene": "scene05",
            "at": "Trái tim nằm sâu trong lồng ngực",
            "layout": "Cận cảnh cơ tim tự phát xung điện sinh học: Không cần máy sốc điện, từng tế bào cơ tim tự phát ra tia năng lượng hồi sinh nhịp đập đầu tiên sau 7 tháng ngủ vùi. {NO_HERO}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene05",
            "at": "những xung điện sinh học",
            "id": "L68",
            "layout": "Tia sét sinh học phục sinh: Một tia chớp nhỏ màu vàng cam lóe lên ngay tại tâm thất của trái tim {HERO}, phá vỡ lớp vỏ băng mỏng cuối cùng để bơm máu trở lại.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene05",
            "at": "Dòng máu ấm nóng giàu đường",
            "layout": "Hệ tuần hoàn bừng sáng: Dòng máu ấm màu đỏ cam chở oxy và glucose lưu thông qua phổi, gan, thận làm tan biến hoàn toàn các khối băng nội tạng. {HERO_S}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene05",
            "at": "Chỉ trong vòng một đến hai giờ",
            "layout": "Hai lá phổi của {HERO} phập phồng hít thở trở lại luồng không khí mùa xuân trong lành, não bộ bừng sáng hàng triệu tế bào thần kinh hoạt động nhộn nhịp.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene05",
            "at": "Và điều kỳ diệu nhất là",
            "layout": "{HERO} chớp mắt trong veo, vươn vai cựa quậy rồi bật nhảy tanh tách từng bước dài dũng mãnh trên nền rừng mùa xuân rực rỡ hoa tuyết. {HERO_S}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene05",
            "at": "lao thẳng xuống những vũng nước",
            "layout": "Đầm lầy nước băng tan rộn rã: {HERO} đứng trên tảng đá cất tiếng kêu ộp ộp vang lừng gọi bạn tình, các đối thủ trong rừng ngơ ngác nhìn theo thán phục.",
            "stickers": [],
            "impacts": []
        },

        # ==================== SCENE 06: BÀI HỌC VÙNG CỰC | BẢO QUẢN TẠNG GHÉP NGƯỜI ====================
        {
            "scene": "scene06",
            "at": 0,
            "layout": "Bảng tổng kết hồ sơ sinh tồn số 33: Các chỉ số kỷ lục của {HERO} gồm 7 tháng tim 0 nhịp, 70% nước hóa đá và sống sót ở -20°C được vinh danh trang trọng.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene06",
            "at": "sinh tồn ngoạn mục",
            "id": "L69",
            "layout": "Cúp vàng vinh danh sinh tồn Bắc Cực: Chiếc cúp vàng khắc hình chú ếch gỗ dũng mãnh đứng trên tảng băng trôi giữa tràng pháo tay của muôn loài động vật vùng cực.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene06",
            "at": "Nhưng giá trị của chú ếch gỗ",
            "layout": "Biểu tượng phòng thí nghiệm công nghệ y sinh tương lai: Mô hình phân tử chống đông của ếch gỗ được chiếu sáng hologram giữa các ống nghiệm hiện đại. {NO_HERO}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene06",
            "at": "Bí kíp chống đông hóa đá",
            "layout": "{HERO} trong trang phục giáo sư tí hon cầm cuộn bí kíp cổ truyền trao tặng cho các bác sĩ trong phòng mổ cứu người.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene06",
            "at": "sự thật đau lòng này không",
            "id": "L70",
            "layout": "Bệnh viện cấp cứu ghép tạng: Đồng hồ đếm ngược gấp gáp trên tường phòng mổ, các bác sĩ đang căng thẳng theo dõi chiếc thùng bảo quản tạng ghép người. {NO_HERO}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene06",
            "at": "một quả tim hoặc một lá phổi người",
            "layout": "Thực trạng y tế ghép tạng hiện nay: Chiếc thùng bảo quản đá lạnh có đồng hồ đếm ngược chỉ còn 4-6 giờ giới hạn trước khi tạng ghép bị hỏng. {NO_HERO}.",
            "stickers": [{"at": "4-6 tiếng", "value": "4-6 GIỜ", "label": "giới hạn tạng người", "side": "L", "y": 340, "target": [0.45, 0.5]}],
            "impacts": []
        },
        {
            "scene": "scene06",
            "at": "không thể cấy ghép được nữa",
            "id": "L71",
            "layout": "Bản đồ vận chuyển tạng khẩn cấp: Tuyến đường bay trực thăng chở thùng tạng ghép nối giữa hai thành phố xa xôi trên bản đồ thế giới với đồng hồ đếm ngược đỏ rực. {NO_HERO}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene06",
            "at": "Hiện nay, các nhà khoa học hàng đầu",
            "layout": "Phòng nghiên cứu sinh học tương lai tại Đại học Harvard: Các buồng bảo quản lạnh sâu mô phỏng phân tử ếch gỗ bảo quản an toàn cơ quan nội tạng suốt nhiều tháng. {NO_HERO}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene06",
            "at": "đông lạnh sâu an toàn",
            "id": "L72",
            "layout": "Ngân hàng nội tạng tương lai Bio-Vault: Các buồng chứa cryo-capsule công nghệ cao bảo quản trái tim và lá gan phát sáng trong dung dịch bảo quản phôi ếch gỗ. {NO_HERO}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene06",
            "at": "Và xa hơn nữa, đó chính là giấc mơ",
            "layout": "Phi thuyền không gian tương lai bay giữa dải ngân hà rực rỡ: Các phi hành gia nằm ngủ đông an toàn trong khoang cryo-stasis mô phỏng cơ chế của {HERO}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene06",
            "at": "Còn bây giờ, chương trình xin gửi",
            "layout": "Bức tranh bí ẩn hé lộ linh thú Tập 34: Bóng đen huyền bí của chú Quạ Đen thông minh đang dùng mỏ uốn cong chiếc que sắt làm móc câu bắt mồi bên gốc cây cổ thụ. {NO_HERO}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene06",
            "at": "làm lưỡi câu bắt ấu trùng",
            "id": "L73",
            "layout": "Bộ não chim thiên tài: Bản chụp tia X hộp sọ chú Quạ Đen với bộ não phát sáng màu tím thông tuệ, chiếc mỏ khéo léo gắp que sắt uốn cong câu con sâu trong khúc gỗ mục. {NO_HERO}.",
            "stickers": [{"at": "suốt 5 năm trời", "value": "5 NĂM", "label": "nhớ mặt kẻ thù", "side": "R", "y": 360, "target": [0.6, 0.5]}],
            "impacts": []
        },
        {
            "scene": "scene06",
            "at": "Hãy để lại câu trả lời",
            "layout": "Khung kết thúc video YouTube thân thiện: {HERO} cùng {REPORTER} vẫy tay chào khán giả bên cạnh nút Like, Subscribe và chuông thông báo hoạt hình rực rỡ.",
            "stickers": [],
            "impacts": []
        }
    ],
    "shorts": [
        {
            "at": 0,
            "layout": "{REPORTER} trùm áo phao lông thú giữa bão tuyết Alaska -20°C, chỉ tay về phía chiếc nhiệt kế đóng băng rực rỡ. {NO_HERO}.",
            "stickers": [{"at": "-20°C", "value": "-20°C", "label": "bão tuyết Alaska", "side": "R", "y": 480, "target": [0.5, 0.4]}],
            "impacts": ["-20°C"]
        },
        {
            "at": "rồi tự rã đông bật nhảy",
            "id": "S11",
            "layout": "{HERO_S} bật nhảy tanh tách từ khối đá băng tan, đôi mắt đeo kính bảo hộ lấp lánh cười toe toét.",
            "stickers": [],
            "impacts": []
        },
        {
            "at": "Khi mùa đông ập đến",
            "layout": "{HERO_S} nằm tựa lưng trên lớp lá rêu mỏng manh sát mặt đất, thản nhiên đắp chiếc chăn lá cây chờ đợi mùa đông.",
            "stickers": [],
            "impacts": []
        },
        {
            "at": "Một loại protein tạo mầm đá",
            "layout": "Sơ đồ cắt lớp cơ thể {HERO_S}: 70% lượng nước hóa thành giáp băng bao bọc bên ngoài bảo vệ nội tạng an toàn.",
            "stickers": [{"at": "65-70%", "value": "70% BĂNG", "label": "giáp băng ngoại bào", "side": "L", "y": 450, "target": [0.45, 0.5]}],
            "impacts": []
        },
        {
            "at": "Để tế bào không bị xé rách",
            "layout": "Lá gan {HERO_S} phình to mở van xả lũ, bơm dòng siro đường Glucose siêu đậm đặc gấp 300 lần vào từng tế bào.",
            "stickers": [{"at": "300 lần", "value": "300 LẦN", "label": "glucose chống đông", "side": "R", "y": 480, "target": [0.55, 0.45]}],
            "impacts": ["300 lần"]
        },
        {
            "at": "bên trong từng tế bào",
            "id": "S12",
            "layout": "Cận cảnh tế bào nội bào {HERO_S}: Dòng siro vàng cam mật ong tràn vào ngập tràn tế bào, bảo vệ màng tế bào căng mọng an toàn.",
            "stickers": [],
            "impacts": []
        },
        {
            "at": "Kết quả: Trái tim ngừng đập",
            "layout": "Màn hình điện tâm đồ ECG thẳng tắp: Tim 0 nhịp/phút, chú gấu Bắc Cực {BEAR} dùng que gõ vào chú ếch hóa đá kêu côm cốp.",
            "stickers": [{"at": "0 nhịp/phút", "value": "0 NHỊP/P", "label": "tim ngừng đập hẳn", "side": "L", "y": 460, "target": [0.4, 0.5]}],
            "impacts": ["0 nhịp/phút"]
        },
        {
            "at": "não phẳng lì",
            "id": "S13",
            "layout": "Bác sĩ cú mèo {DOCTOR} đeo kính lúp soi vào chú ếch {HERO_S} hóa thành tảng đá hoa cương phủ sương tuyết, bên cạnh là máy EEG phẳng lì 0Hz.",
            "stickers": [],
            "impacts": []
        },
        {
            "at": "Về mặt y học",
            "layout": "{DOCTOR} giơ bảng kết luận chết lâm sàng 100% trong khi {HERO_S} hóa thành viên đá hoa cương suốt 200 ngày.",
            "stickers": [{"at": "100%", "value": "100%", "label": "chết lâm sàng", "side": "R", "y": 480, "target": [0.55, 0.45]}],
            "impacts": []
        },
        {
            "at": "Thế nhưng khi ánh nắng",
            "layout": "Nắng ấm mùa xuân rọi xuống làm tan chảy băng tuyết, những mầm cây xanh non nhú lên xung quanh khối đá ếch gỗ.",
            "stickers": [],
            "impacts": []
        },
        {
            "at": "trái tim tự rã đông đầu tiên",
            "layout": "{HEART_ICE} bừng sáng rực rỡ, tự phát xung điện sinh học và đập lại thình thịch mà không cần máy sốc điện.",
            "stickers": [],
            "impacts": ["trái tim"]
        },
        {
            "at": "và chỉ vài tiếng sau chú ếch",
            "layout": "{HERO_S} bật dậy vươn vai rồi phóng từng bước nhảy dũng mãnh xuống hồ nước mùa xuân cất tiếng gọi bạn tình.",
            "stickers": [],
            "impacts": []
        },
        {
            "at": "Một kiệt tác hồi sinh",
            "layout": "{HERO_S} cười tươi nháy mắt bên cạnh nút Đăng ký kênh YouTube hoạt hình phát sáng rực rỡ.",
            "stickers": [],
            "impacts": []
        }
    ]
}

out_file = P / "specs" / "storyboard.json"
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(storyboard, f, ensure_ascii=False, indent=2)

print(f"Generated {out_file} successfully.")
print(f"Long beats: {len(storyboard['long'])} beats | Shorts beats: {len(storyboard['shorts'])} beats.")
