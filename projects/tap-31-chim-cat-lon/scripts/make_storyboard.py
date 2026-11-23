# -*- coding: utf-8 -*-
"""Generate complete specs/storyboard.json for Episode 31: Chim Cắt Lớn (Peregrine Falcon)
Strict Prompt Safety: Zero copyright, Zero military weapons, Zero violence/gore.
"""
import json
from pathlib import Path

P = Path("projects/tap-31-chim-cat-lon")

storyboard = {
    "_doc": "Storyboard Tập 31 — Chim Cắt Lớn (Peregrine Falcon) F2 Kỹ Sư Vũ Khí. Chạy: python src/episode/build_plans.py projects/tap-31-chim-cat-lon",
    "characters": {
        "HERO": "chú Chim Cắt Lớn hoạt hình lông ngực vằn xám trắng, đôi mắt to sắc sảo thông minh, đầu đội mũ phi công da cổ điển kèm kính bảo hộ phi công ngộ nghĩnh (cute vintage leather aviator helmet and flight goggles)",
        "HERO_S": "chú Chim Cắt Lớn đội mũ phi công da và kính bảo hộ phi công",
        "NO_HERO": "KHÔNG có chú Chim Cắt Lớn trong cảnh này",
        "PIGEON": "chú chim bồ câu hoạt hình lông xám mập mạp ngơ ngác, cầm máy đo tốc độ đồ chơi màu vàng",
        "ASSISTANT": "cô trợ lý sóc hoạt hình đeo kính cận to tròn, mặc áo blouse trắng phòng thí nghiệm, cầm bản vẽ blueprint khí động học",
        "CHEETAH": "chú báo săn cheetah hoạt hình màu vàng đốm đen, đi giày thể thao đỏ, đang thở dốc ôm đầu gối mệt mỏi",
        "PILOT": "chú phi công gấu hoạt hình mặc đồ bay G-suit màu xanh, mặt tái mét ôm túi nôn ngộ nghĩnh"
    },
    "side_characters": [
        "PIGEON",
        "ASSISTANT",
        "CHEETAH",
        "PILOT"
    ],
    "shorts_side_characters": [
        "PIGEON",
        "PILOT"
    ],
    "shorts_title_lines": [
        "BỔ NHÀO 389 KM/H:",
        "NÓN NÉN KHÍ CHỐNG NỔ PHỔI!"
    ],
    "skip_numbers": [],
    "long": [
        # SCENE 01: HỒ SƠ MẬT | VẬT THỂ BAY 389 KM/H
        {
            "scene": "scene01",
            "at": 0,
            "layout": "Phòng nghiên cứu khí động học công nghệ cao: một tập hồ sơ tài liệu đóng dấu đỏ tươi 'BÁO CÁO GIẢI MÃ SỐ 31' đặt giữa bàn kính, màn hình lớn phía sau hiển thị bầu trời mây trắng bao la. {NO_HERO}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene01",
            "at": "Chào mừng toàn thể",
            "layout": "Phòng thí nghiệm khoa học vui nhộn: {ASSISTANT} đang gõ bàn phím máy tính phân tích biểu đồ khí động học, bên cạnh là mô hình máy bay phản lực đồ chơi. {NO_HERO}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene01",
            "at": "Chim Cắt Lớn",
            "layout": "Chân dung oai phong của {HERO} đứng trên đỉnh vách đá cheo leo, bộ lông xám bạc óng ả, ngực ưỡn tự tin nhìn về phía đường chân trời rực nắng.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene01",
            "at": "Nếu bạn nghĩ",
            "layout": "Đường đua đồng cỏ savan châu Phi: {CHEETAH} đang vừa chạy vừa lè lưỡi thở dốc, đồng hồ đo tốc độ hiện 100 km/h, nhưng trên bầu trời cao {HERO} đã lướt qua để lại vệt gió xoáy làm bay mũ của báo. {CHEETAH}.",
            "stickers": [{"at": "100 km/h", "value": "100 km/h", "label": "báo săn chạy bộ", "side": "R", "y": 360, "target": [0.75, 0.55]}],
            "impacts": []
        },
        {
            "scene": "scene01",
            "at": "Báo cáo radar phòng không",
            "layout": "Trạm quan sát radar trên đài chỉ huy: màn hình radar quét xanh lá cây nhấp nháy một chấm sáng đỏ lao vun vút từ độ cao 5.000m xuống với góc bổ nhào dựng đứng. {NO_HERO}.",
            "stickers": [{"at": "5.000m", "value": "5.000m", "label": "độ cao bổ nhào", "side": "L", "y": 360, "target": [0.3, 0.55]}],
            "impacts": []
        },
        {
            "scene": "scene01",
            "at": "389 km/h! Đúng vậy các",
            "layout": "Bầu trời xanh mây trắng cuộn sóng: {HERO} gập cánh bổ nhào cực nhanh xé toạc các đám mây, phía sau là vệt sóng âm khí động học màu cam rực rỡ, kèm bảng số đo điện tử hiện số khổng lồ '389 km/h'.",
            "stickers": [{"at": "389 km/h", "value": "389 km/h", "label": "kỷ lục bổ nhào", "side": "R", "y": 360, "target": [0.75, 0.55]}],
            "impacts": []
        },
        {
            "scene": "scene01",
            "at": "Năm 2005",
            "layout": "Thí nghiệm thực địa năm 2005: Một chuyên gia nhảy dù mặc đồ bảo hộ lượn giữa tầng mây, bên cạnh là {HERO} đang lao vút song song với thiết bị máy đo vi cơ gắn gọn gàng ở đuôi lông chim. {HERO}.",
            "stickers": [{"at": "Năm 2005", "value": "Năm 2005", "label": "thử nghiệm lịch sử", "side": "L", "y": 360, "target": [0.3, 0.55]}],
            "impacts": []
        },
        {
            "scene": "scene01",
            "at": "Tốc độ này nhanh hơn",
            "layout": "Đồ thị so sánh tốc độ vui nhộn: Chiếc xe đua công thức một màu đỏ cắm cờ F1 trên đường đua chạy hết ga ở dưới, nhưng trên cao {HERO} vượt qua nhẹ như một mũi tên xé gió. {NO_HERO}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene01",
            "at": "Nhưng khoan đã các kỹ sư",
            "layout": "Mô phỏng áp lực gió kinh hoàng: Một hình nộm thí nghiệm bị luồng gió bão cực mạnh thổi bay tóc, thổi phồng má và nứt toác kính, minh họa cho áp lực không khí tàn phá ở 400 km/h. {NO_HERO}.",
            "stickers": [{"at": "gần 400 km/h", "value": "400 km/h", "label": "áp lực gió cực đại", "side": "R", "y": 360, "target": [0.75, 0.55]}],
            "impacts": []
        },
        {
            "scene": "scene01",
            "at": "Vậy bản thiết kế giải phẫu",
            "layout": "Phòng thí nghiệm: {ASSISTANT} trải rộng một tấm bản vẽ blueprint màu xanh lam phát sáng, trên đó vẽ chi tiết cấu trúc xương và khí động học của {HERO}. {NO_HERO}.",
            "stickers": [],
            "impacts": []
        },

        # SCENE 02: BẢN VẼ CƠ KHÍ | NÓN GIẢM ÁP VÀ MÍ MẮT THỨ BA
        {
            "scene": "scene02",
            "at": 0,
            "layout": "Bản vẽ cấu tạo đầu chim cắt: {HERO} nghiêng đầu khoe cận cảnh chiếc mỏ quặp màu xám thép, mũi tên kỹ thuật màu vàng phát sáng chỉ thẳng vào lỗ mũi tròn của chim.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene02",
            "at": "Bình thường lỗ mũi",
            "layout": "Kính phóng đại giải phẫu: So sánh hai lỗ mũi, bên trái là lỗ mũi trơn của chim bồ câu, bên phải là lỗ mũi của {HERO} có chiếc nón xương xoắn ốc tí hon tubercle màu kem nhô lên kiêu hãnh. {NO_HERO}.",
            "stickers": [{"at": "tubercle", "value": "TUBERCLE", "label": "nón xương giảm áp", "side": "L", "y": 360, "target": [0.35, 0.5]}],
            "impacts": []
        },
        {
            "scene": "scene02",
            "at": "Khi chim cắt bổ nhào",
            "layout": "Mô phỏng đường hầm khí động học: Luồng gió mạnh màu xanh lam lao vào mũi chim, khi gặp nón xương tubercle thì lập tức bị phân tách thành các xoáy khí nhỏ cuộn tròn chậm rãi, nhẹ nhàng đi vào khí quản. {NO_HERO}.",
            "stickers": [{"at": "0,5 giây", "value": "0,5 GIÂY", "label": "thời gian vỡ phổi", "side": "R", "y": 360, "target": [0.75, 0.55]}],
            "impacts": []
        },
        {
            "scene": "scene02",
            "at": "Chi tiết này thông minh",
            "layout": "Màn hình so sánh công nghệ sinh học và hàng không: Bên trái là nón mũi của {HERO}, bên phải là cửa hút gió của siêu máy bay phản lực SR-71 Blackbird với chiếc nón cản sốc shock-cone y hệt. {NO_HERO}.",
            "stickers": [{"at": "SR-71", "value": "SR-71", "label": "học tập nón cản sốc", "side": "L", "y": 360, "target": [0.3, 0.55]}],
            "impacts": []
        },
        {
            "scene": "scene02",
            "at": "Bản vẽ kỹ thuật tầng hai",
            "layout": "Cận cảnh đôi cánh khí động học của {HERO}: Đôi cánh dang rộng hình lưỡi liềm nhọn hoắt, các lớp lông vũ màu xám đen xếp chồng khít khao như vảy giáp, các sợi lông cảm biến ở rìa cánh dựng nhẹ điều hướng gió.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene02",
            "at": "Chưa hết đâu đội kỹ thuật",
            "layout": "Cận cảnh đôi mắt của {HERO}: Một màng bảo vệ mí mắt thứ ba mỏng như gương trong suốt quét ngang qua nhãn cầu, làm sạch giọt bụi và ngăn gió lốc, hai hàng nước mắt sinh học làm trơn bóng bề mặt mắt.",
            "stickers": [{"at": "mí mắt thứ ba", "value": "MÍ MẮT 3", "label": "kính bảo hộ sinh học", "side": "L", "y": 360, "target": [0.3, 0.5]}],
            "impacts": []
        },

        # SCENE 03: HỆ THỐNG RADAR | MẮT ĐÔI VÀ XOẮN ỐC LOGARIT
        {
            "scene": "scene03",
            "at": 0,
            "layout": "Bản vẽ giải phẫu hộp sọ: Đôi mắt của {HERO} chiếm trọn gần nửa khoang sọ, có hai tia laser xanh định vị phát ra từ hai hốc mắt sâu fovea trên võng mạc.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene03",
            "at": "Trong khi mắt người chỉ",
            "layout": "Bảng phân tích độ phân giải quang học: Mắt người nhìn phong cảnh nhòe ở cự ly xa, còn màn hình của {HERO} chia đôi với hốc mắt fovea đôi phóng to sắc nét gấp 8 lần thấy rõ từng cử động. {NO_HERO}.",
            "stickers": [{"at": "gấp 8 lần", "value": "x8 LẦN", "label": "độ nét mắt phi công", "side": "L", "y": 360, "target": [0.3, 0.55]}],
            "impacts": []
        },
        {
            "scene": "scene03",
            "at": "Cảm biến quang học báo cáo",
            "layout": "Góc nhìn ngắm bắn từ trên cao 3.000m: {PIGEON} ở dưới mặt đất đang ngậm mẩu bánh mì ngơ ngác, hồng tâm kính ngắm đồ chơi màu đỏ khóa tròn vào người bồ câu. {PIGEON}.",
            "stickers": [{"at": "3km", "value": "3 KM", "label": "cự ly khóa mục tiêu", "side": "R", "y": 360, "target": [0.75, 0.55]}],
            "impacts": []
        },
        {
            "scene": "scene03",
            "at": "Giáo sư Vance Tucker",
            "layout": "Phòng thực nghiệm sinh học Đại học Duke: Giáo sư thỏ đeo kính lão chỉ lên bảng đen vẽ hình một con chim bổ nhào bị ngoẹo cổ lệch 40 độ tạo luồng cản gió lớn màu đỏ cảnh báo. {NO_HERO}.",
            "stickers": [{"at": "40 độ", "value": "40 ĐỘ", "label": "góc lệch hốc mắt sâu", "side": "L", "y": 360, "target": [0.3, 0.55]}],
            "impacts": []
        },
        {
            "scene": "scene03",
            "at": "Để giải bài toán hóc búa",
            "layout": "Mô hình toán học trên nền trời xanh: {HERO} nghiêng thân lượn theo một đường cong xoắn ốc logarit màu vàng óng tuyệt đẹp từ trên cao xoắn dần xuống, đầu giữ thẳng tắp hướng gió, mắt khóa chặt mục tiêu.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene03",
            "at": "Đặc biệt hơn nữa",
            "layout": "Màn hình hiển thị tần số quét mắt: Đồng hồ 130 fps nhảy nhót, {PIGEON} bên dưới bay chậm rì rì như đang trôi trong bong bóng nước, {HERO} ung dung chỉnh cánh lượn quanh mục tiêu.",
            "stickers": [{"at": "130 khung hình/giây", "value": "130 FPS", "label": "tốc độ xử lý mắt", "side": "R", "y": 360, "target": [0.75, 0.55]}],
            "impacts": []
        },

        # SCENE 04: ĐÒN THỰC CHIẾN | GIA LỰC 25G VÀ CÚ ĐẤM NẮM TAY
        {
            "scene": "scene04",
            "at": 0,
            "layout": "Cận cảnh tư thế bổ nhào hoàn hảo: {HERO} khép chặt hai cánh ôm trọn lấy thân hình giọt nước khí động học, đuôi xòe hẹp như bánh lái tên lửa, lao vun vút thẳng đứng từ trên trời cao.",
            "stickers": [{"at": "300m", "value": "300 MÉT", "label": "cự ly gập cánh", "side": "L", "y": 360, "target": [0.3, 0.55]}],
            "impacts": []
        },
        {
            "scene": "scene04",
            "at": "Lúc này tim của nó",
            "layout": "Màn hình sinh trắc học y khoa: Nhịp tim điện tâm đồ của {HERO} nhảy múa dữ dội ở mức 900 nhịp/phút, cơ ngực nổi cơ bắp cuồn cuộn đỏ rực năng lượng dồi dào. {NO_HERO}.",
            "stickers": [{"at": "600-900 nhịp/phút", "value": "900 BPM", "label": "nhịp tim cực đại", "side": "R", "y": 360, "target": [0.75, 0.55]}],
            "impacts": []
        },
        {
            "scene": "scene04",
            "at": "Nhưng điều đáng kinh ngạc nhất",
            "layout": "Cận cảnh bàn chân của {HERO}: Bốn ngón chân có móng vuốt sắc nhọn cuộn tròn thành một nắm đấm bọc sừng cứng như quả cầu sắt đặc, giương thẳng ra phía trước như một võ sĩ quyền anh.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene04",
            "at": "Rầm Nắm đấm móng vuốt",
            "layout": "Khoảnh khắc va chạm rung chuyển bầu trời: Nắm đấm của {HERO} giáng trúng cánh con mồi, tạo ra luồng sóng xung kích sao vàng bay tứ tung, {PIGEON} giật mình hoa mắt bay lộn nhào rơi tự do. {HERO}.",
            "stickers": [{"at": "1kg", "value": "1 KG", "label": "trọng lượng quả đấm", "side": "L", "y": 360, "target": [0.3, 0.55]}],
            "impacts": []
        },
        {
            "scene": "scene04",
            "at": "Ngay sau cú va chạm",
            "layout": "Khoảnh khắc kéo phanh sinh tử: Chỉ cách mặt đất rặng cây vài mét, {HERO} bất ngờ dang rộng đôi cánh hình lưỡi liềm bẻ góc kéo ngược thân mình vút lên bầu trời, tạo luồng gió hất tung bụi cỏ.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene04",
            "at": "Và hãy nhìn vào thông số",
            "layout": "Bảng đo gia tốc G-force: Bên trái là {PILOT} ngồi trên ghế lái tiêm kích chịu 9G mặt mày xám ngoét ngất xỉu ôm túi nôn; bên phải là {HERO} chịu 25G vẫn cười tươi toe toét giơ ngón cái ngầu lòi. {PILOT}.",
            "stickers": [
                {"at": "25G", "value": "25G", "label": "gia tốc kéo lên", "side": "R", "y": 360, "target": [0.75, 0.55]},
                {"at": "9G", "value": "9G", "label": "giới hạn phi công", "side": "L", "y": 360, "target": [0.3, 0.55]}
            ],
            "impacts": []
        },

        # SCENE 05: TỬ HUYỆT VŨ KHÍ | DÁNG ĐI LẠCH BẠCH VÀ VỎ TRỨNG MỎNG
        {
            "scene": "scene05",
            "at": 0,
            "layout": "Bảng phân tích kỹ thuật đóng dấu đỏ: 'ĐIỂM YẾU KỸ THUẬT': {ASSISTANT} cầm thước chỉ vào hình vẽ đôi chân ngắn tủn của chim cắt đặt trên mặt đất. {NO_HERO}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene05",
            "at": "Vì toàn bộ thiết kế",
            "layout": "Bãi cỏ xanh mướt: {HERO} đứng dưới đất với đôi chân ngắn củn, dáng đi lạch bạch ngả nghiêng như say rượu, móng vuốt quắp vào cỏ làm chú vấp ngã chúi mũi ngố không tả nổi. {HERO}.",
            "stickers": [{"at": "25%", "value": "25% HIT", "label": "tỷ lệ bắt dưới đất", "side": "L", "y": 360, "target": [0.3, 0.55]}],
            "impacts": []
        },
        {
            "scene": "scene05",
            "at": "Chưa dừng lại ở đó",
            "layout": "Tình huống trớ trêu: {HERO} vừa săn được mẩu thịt đặt trên tảng đá thì một chú quạ đen và chú mòng biển hung hăng nhảy vào vỗ cánh cướp mất, {HERO} chỉ biết đứng gãi đầu bẽn lẽn. {HERO}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene05",
            "at": "Nhưng bi kịch đen tối",
            "layout": "Đồng ruộng thập niên 1960 u ám: Máy bay nông nghiệp phun những đám khói hóa chất thuốc trừ sâu DDT mù mịt xuống cánh đồng lúa, các loài chim nhỏ ăn phải hạt giống nhiễm độc. {NO_HERO}.",
            "stickers": [{"at": "DDT", "value": "DDT", "label": "hóa chất mỏng vỏ", "side": "R", "y": 360, "target": [0.75, 0.55]}],
            "impacts": []
        },
        {
            "scene": "scene05",
            "at": "Hậu quả là mỗi khi",
            "layout": "Tổ chim cắt trên gờ đá vách núi: Chim bố mẹ ấp trứng trong buồn rầu, những quả trứng chim cắt có lớp vỏ mỏng dính bị nứt toác rạn vỡ vì thiếu hụt canxi, khung cảnh đầy thương cảm. {NO_HERO}.",
            "stickers": [],
            "impacts": []
        },

        # SCENE 06: NGHIỆM THU HỒ SƠ | BÀN GIAO VŨ KHÍ VÀ TẬP KẾ TIẾP
        {
            "scene": "scene06",
            "at": 0,
            "layout": "Chiến dịch bảo tồn năm 1972: Các nhà khoa học nâng niu chăm sóc những chú chim cắt con mới nở trong lồng ấp hiện đại, rồi đeo vòng định vị thả chim về lại bầu trời tự do. {NO_HERO}.",
            "stickers": [{"at": "năm 1972", "value": "NĂM 1972", "label": "lệnh cấm toàn cầu", "side": "L", "y": 360, "target": [0.3, 0.55]}],
            "impacts": []
        },
        {
            "scene": "scene06",
            "at": "và giờ đây Tiêm Kích",
            "layout": "Đô thị hiện đại rực rỡ nắng vàng: {HERO} đậu hiên ngang trên đỉnh tòa tháp chọc trời ngắm nhìn thành phố nhộn nhịp bên dưới, sau đó sải cánh bay lượn kiêu hãnh giữa trời xanh. {HERO}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene06",
            "at": "Báo cáo nghiệm thu kỹ thuật",
            "layout": "Bàn làm việc kỹ thuật: Hồ sơ giải mật số 31 được đóng con dấu xanh lá cây tròn xoe ghi 'ĐÃ NGHIỆM THU XUẤT SẮC', {ASSISTANT} tươi cười cất hồ sơ vào tủ lưu trữ khoa học. {NO_HERO}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene06",
            "at": "Đội kỹ thuật thân mến",
            "layout": "{HERO} nghiêng đầu vẫy cánh chào khán giả, bên cạnh là biểu tượng hộp bình luận YouTube kèm các dấu hỏi chấm rực rỡ mời gọi ý kiến của người xem. {HERO}.",
            "stickers": [],
            "impacts": []
        },
        {
            "scene": "scene06",
            "at": "Và ngay trong hồ sơ",
            "layout": "Đường hầm hang ngầm tối tăm huyền bí dưới lòng đất: Một BÓNG ĐEN BÍ ẨN (solid black silhouette) hình dạng sinh vật gặm nhấm trụi lông kỳ dị với hai chiếc răng cửa to tướng nhô ra, xung quanh là dấu hỏi chấm phát sáng lấp lánh và ký hiệu miễn nhiễm bệnh tật. {NO_HERO}.",
            "stickers": [{"at": "30 năm", "value": "30 NĂM", "label": "tuổi thọ quái kiệt", "side": "R", "y": 360, "target": [0.75, 0.55]}],
            "impacts": []
        }
    ],
    "shorts": [
        {
            "at": 0,
            "layout": "Màn hình radar phòng không báo động đỏ: Một chấm sáng lao vút từ độ cao 5.000m với tốc độ 389 km/h xé toạc bầu trời. {NO_HERO}.",
            "stickers": []
        },
        {
            "at": "Tại sao khi lao",
            "layout": "Mô phỏng áp lực gió cực lớn dội vào một hình nộm thí nghiệm làm thổi bay tóc và nứt kính bảo hộ. {NO_HERO}.",
            "stickers": [{"at": "5.000m", "value": "5.000m", "label": "độ cao bổ nhào", "side": "L", "y": 360, "target": [0.3, 0.55]}]
        },
        {
            "at": "Đây chính là Tiêm Kích",
            "layout": "Chân dung ngầu lòi của {HERO_S} đeo kính phi công và mũ da cổ điển, đứng oai vệ trên mỏm đá cao.",
            "stickers": []
        },
        {
            "at": "Ở tốc độ khủng khiếp",
            "layout": "Luồng gió nén cuồng bạo thổi ầm ầm vào mô hình khí quản hai lá phổi đỏ rực minh họa nguy cơ nổ tung. {NO_HERO}.",
            "stickers": []
        },
        {
            "at": "Nhưng mẹ thiên nhiên",
            "layout": "Cận cảnh lỗ mũi của {HERO_S}: Mũi tên phát sáng chỉ vào chiếc nón xương xoắn ốc tubercle nhỏ xíu bên trong lỗ mũi.",
            "stickers": [{"at": "tubercle", "value": "TUBERCLE", "label": "nón nén khí", "side": "R", "y": 360, "target": [0.75, 0.5]}]
        },
        {
            "at": "Chiếc nón giảm áp này",
            "layout": "Mô phỏng luồng gió nén gặp nón xương biến thành các xoáy khí chậm cuộn tròn êm ái đi vào phổi. {NO_HERO}.",
            "stickers": []
        },
        {
            "at": "Đến cả siêu máy bay",
            "layout": "So sánh màn hình chia đôi giữa nón mũi của {HERO_S} và cửa hút gió của siêu máy bay trinh sát SR-71 Blackbird. {NO_HERO}.",
            "stickers": [{"at": "SR-71", "value": "SR-71", "label": "học tập tự nhiên", "side": "R", "y": 360, "target": [0.75, 0.55]}]
        },
        {
            "at": "Chưa hết chim cắt còn",
            "layout": "Bàn chân của {HERO_S} cuộn tròn bốn ngón thành quả đấm bọc sừng thép đặc quánh giương ra phía trước như võ sĩ quyền anh.",
            "stickers": []
        },
        {
            "at": "chịu gia lực tới 25G",
            "layout": "Màn hình đo gia tốc: {PILOT} ngồi trên tiêm kích ngất xỉu vì 9G, trong khi {HERO_S} chịu 25G vẫn cười toe toét giơ ngón tay ngầu lòi. {PILOT}.",
            "stickers": [{"at": "25G", "value": "25G", "label": "chịu lực 25G", "side": "R", "y": 360, "target": [0.75, 0.55]}]
        },
        {
            "at": "Một kiệt tác khí động học",
            "layout": "{HERO_S} sải cánh liềm chao lượn kiêu hãnh trên bầu trời hoàng hôn rực rỡ, để lại vệt sáng vàng óng tuyệt đẹp.",
            "stickers": []
        }
    ]
}

(P / "specs" / "storyboard.json").write_text(json.dumps(storyboard, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Written specs/storyboard.json successfully with {len(storyboard['long'])} long beats and {len(storyboard['shorts'])} shorts beats!")
