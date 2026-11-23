# -*- coding: utf-8 -*-
"""Generate complete episode.json for Episode 31: Chim Cắt Lớn (Peregrine Falcon)
Format: F2 (Giải Mã Vũ Khí Tối Mật) | Persona: ky_su_vu_khi
"""
import json
from pathlib import Path

P = Path("projects/tap-31-chim-cat-lon")

ep = {
    "episode_no": 31,
    "animal": "Chim Cắt Lớn",
    "slug": "tap-31-chim-cat-lon",
    "format": "F2",
    "persona": "ky_su_vu_khi",
    "_angle_from_roadmap": "Giải mã tên lửa 389 km/h: Nón giảm áp trong lỗ mũi chống nổ phổi và kính bảo hộ mí mắt thứ ba.",
    "_shorts_idea_from_roadmap": "Tại sao phổi Chim Cắt không bị nổ tung khi lao xuống với tốc độ gần 400 km/h?",
    "nickname": "Tiêm Kích Lông Vũ",
    "sources": [
        "Franklin, K. (2005), National Geographic — Đo đạc tốc độ bổ nhào 389 km/h của chim cắt Frightful bằng thiết bị đo gắn trên cơ thể nhảy dù từ 5.000m",
        "Tucker, V. A. (1998), Journal of Experimental Biology — Khí động học lực cản và mô phỏng đường hầm gió góc cánh chim cắt trong tư thế bổ nhào stoop dive",
        "Tucker, V. A. et al. (2000), J. Exp. Biol. — Phát hiện đường bay xoắn ốc logarit do vùng fovea sâu lệch 40 độ tối ưu tầm nhìn và giảm lực cản không khí",
        "Ponitz, B. et al. (2014), PLoS ONE — Cơ chế cấu trúc vảy lông và hình thái cánh giọt nước kiểm soát dòng khí siêu tốc",
        "Smithsonian & National Geographic (2008) — Cấu trúc nón xương tubercle trong lỗ mũi hoạt động như tấm cản sốc shock-cone của động cơ máy bay phản lực",
        "Cade, T. J. et al. (1988), The Peregrine Fund — Khảo sát tác động tích tụ sinh học của thuốc trừ sâu DDT làm mỏng vỏ trứng và chương trình nhân giống phục hồi toàn cầu"
    ],
    "whisper_prompt": "Chim Cắt Lớn, Tiêm Kích Lông Vũ, Falco peregrinus, Ken Franklin, Frightful, Vance Tucker, SR-71, Blackbird, 389 km/h, 400 km/h, 300 km/h, 200 km/h, 100 km/h, 25G, 9G, 5.000m, 3.000m, 3km, 300m, 40 độ, 600 nhịp/phút, 900 nhịp/phút, 130 khung hình/giây, 60 khung hình/giây, tubercle, fovea, DDT, Chuột Chũi Trũi",
    "display_fix": {
        "ba trăm tám mươi chín ki-lô-mét một giờ": "389 km/h",
        "Ba trăm tám mươi chín ki-lô-mét một giờ": "389 km/h",
        "ba trăm tám chín ki-lô-mét một giờ": "389 km/h",
        "Ba trăm tám chín ki-lô-mét một giờ": "389 km/h",
        "gần bốn trăm ki-lô-mét một giờ": "gần 400 km/h",
        "Gần bốn trăm ki-lô-mét một giờ": "gần 400 km/h",
        "bốn trăm ki-lô-mét một giờ": "400 km/h",
        "Bốn trăm ki-lô-mét một giờ": "400 km/h",
        "ba trăm ki-lô-mét một giờ": "300 km/h",
        "Ba trăm ki-lô-mét một giờ": "300 km/h",
        "hai trăm ki-lô-mét một giờ": "200 km/h",
        "Hai trăm ki-lô-mét một giờ": "200 km/h",
        "một trăm ki-lô-mét một giờ": "100 km/h",
        "Một trăm ki-lô-mét một giờ": "100 km/h",
        "năm ngàn mét": "5.000m",
        "Năm ngàn mét": "5.000m",
        "năm nghìn mét": "5.000m",
        "Năm nghìn mét": "5.000m",
        "ba ngàn mét": "3.000m",
        "Ba ngàn mét": "3.000m",
        "ba ki-lô-mét": "3km",
        "Ba ki-lô-mét": "3km",
        "ba trăm mét": "300m",
        "Ba trăm mét": "300m",
        "hai mươi lăm G": "25G",
        "Hai mươi lăm G": "25G",
        "chín G": "9G",
        "Chín G": "9G",
        "sáu trăm đến chín trăm nhịp một phút": "600-900 nhịp/phút",
        "Sáu trăm đến chín trăm nhịp một phút": "600-900 nhịp/phút",
        "một trăm ba mươi khung hình một giây": "130 khung hình/giây",
        "Một trăm ba mươi khung hình một giây": "130 khung hình/giây",
        "sáu mươi khung hình một giây": "60 khung hình/giây",
        "Sáu mươi khung hình một giây": "60 khung hình/giây",
        "bốn mươi độ": "40 độ",
        "Bốn mươi độ": "40 độ",
        "nửa giây": "0,5 giây",
        "Nửa giây": "0,5 giây",
        "không phẩy một giây": "0,1 giây",
        "Không phẩy một giây": "0,1 giây",
        "hai mươi lăm phần trăm": "25%",
        "Hai mươi lăm phần trăm": "25%",
        "chín mươi phần trăm": "90%",
        "Chín mươi phần trăm": "90%",
        "năm hai ngàn không trăm linh năm": "năm 2005",
        "Năm hai ngàn không trăm linh năm": "Năm 2005",
        "thập niên một ngàn chín trăm sáu mươi": "thập niên 1960",
        "Thập niên một ngàn chín trăm sáu mươi": "Thập niên 1960",
        "năm một ngàn chín trăm bảy mươi hai": "năm 1972",
        "Năm một ngàn chín trăm bảy mươi hai": "Năm 1972",
        "tập ba mươi hai": "Tập 32",
        "Tập ba mươi hai": "Tập 32",
        "ba mươi hai": "32",
        "Ba mươi hai": "32",
        "ba mươi năm": "30 năm",
        "Ba mươi năm": "30 năm",
        "mười lần": "10 lần",
        "Mười lần": "10 lần",
        "tám lần": "8 lần",
        "Tám lần": "8 lần",
        "một ki-lô-gam": "1kg",
        "Một ki-lô-gam": "1kg",
        "Bo-ing": "Boeing",
        "Phan-cô Pê-rê-gri-nút": "Falco peregrinus",
        "Ken Phơ-răng-clin": "Ken Franklin",
        "Phrai-phun": "Frightful",
        "Van-xơ Tắc-cơ": "Vance Tucker",
        "Đê Đê Tê": "DDT",
        "ép một": "F1",
        "Ép một": "F1",
        "ép hai": "F2",
        "Ép hai": "F2",
        "ét-sơ-rờ bảy mươi mốt": "SR-71",
        "Bờ-lách-bớt": "Blackbird",
        "pho-ve-a": "fovea",
        "tu-béc-cơ": "tubercle"
    },
    "voice": {},
    "art": {
        "decor": "blueprint grid lines, supersonic airflow shockwaves, technical crosshairs, miniature mechanical gears",
        "shorts_mascot": "A cool cartoon peregrine falcon wearing pilot flight goggles and holding a miniature blueprint scroll",
        "thumb_bg": "dramatic dark navy high altitude sky with burning orange supersonic airflow trails",
        "thumb_title": ["BỔ NHÀO 389 KM/H?!", "NÓN NÉN KHÍ CHỐNG NỔ PHỔI"],
        "thumb_scene": "chú chim cắt lớn đeo kính phi công ngầu lòi đang bổ nhào cắm đầu như tên lửa, cánh khép chặt tạo hình giọt nước",
        "thumb_gag": "chú bồ câu ngố phía dưới cầm máy bắn tốc độ bị thổi bay cả kính, mồm há hốc kinh ngạc"
    },
    "longform": {
        "scenes": [
            {
                "id": "scene01",
                "badge": "HỒ SƠ MẬT",
                "banner_title": "VẬT THỂ BAY 389 KM/H",
                "chapter_title": "Hồ sơ mật: Tiêm kích lông vũ đạt kỷ lục 389 km/h bổ nhào xé toạc bầu trời",
                "hook": "HỒ SƠ MẬT CẤP ĐỘ ĐỎ: KỶ LỤC TỐC ĐỘ NHANH NHẤT HÀNH TINH",
                "mood": "tram_bi_an",
                "parts": [
                    {
                        "text": "Hồ sơ mật cấp độ đỏ. Mở khóa! Chào mừng toàn thể đội ngũ kỹ thuật quay trở lại phòng nghiên cứu vũ khí sinh học. Hôm nay chúng ta giải mật một cỗ máy bay không người lái tự nhiên có tốc độ kinh hoàng nhất lịch sử tiến hóa: Chim Cắt Lớn, danh pháp khoa học Phan-cô Pê-rê-gri-nút. Nếu bạn nghĩ báo hoa mai chạy một trăm ki-lô-mét một giờ đã là đỉnh chóp, thì cỗ máy này sẽ biến báo đốm thành một trò đùa rùa bò.",
                        "mood": "tram_bi_an"
                    },
                    {
                        "text": "Báo cáo radar phòng không: Phát hiện vật thể lạ bổ nhào từ độ cao năm ngàn mét! Vận tốc đo được ba trăm tám mươi chín ki-lô-mét một giờ!",
                        "cast": "phat_thanh_vien"
                    },
                    {
                        "text": "[surprise-oh] Ba trăm tám mươi chín ki-lô-mét một giờ! Đúng vậy các đồng chí, đây không phải thông số chém gió trong phim viễn tưởng. Năm hai ngàn không trăm linh năm, phi công nhảy dù Ken Phơ-răng-clin đã cùng chú chim cắt mang tên Phrai-phun thực hiện một cú nhảy từ máy bay ở độ cao năm ngàn mét. Khi Ken nhảy dù tự do, chú chim cắt gập cánh lao theo và thiết bị đo gắn trên đuôi chim đã chạm mốc không tưởng: ba trăm tám mươi chín ki-lô-mét một giờ! Tốc độ này nhanh hơn cả xe đua công thức một ép một và vượt xa mọi phương tiện giao thông trên mặt đất! [laughter]",
                        "mood": "hao_hung"
                    },
                    {
                        "text": "Nhưng khoan đã các kỹ sư. Ở tốc độ gần bốn trăm ki-lô-mét một giờ, theo định luật vật lý cơ bản, bất kỳ sinh vật bình thường nào cũng sẽ bị luồng gió nén cực mạnh xé toạc màng nhĩ, rách toạc giác mạc và thổi nổ tung hai lá phổi ngay trên không trung! Vậy bản thiết kế giải phẫu của Tiêm Kích Lông Vũ này giấu những linh kiện tối mật gì? Mời đội kỹ thuật bước ngay vào bóc tách bản vẽ cơ khí!",
                        "mood": "don_dap"
                    }
                ]
            },
            {
                "id": "scene02",
                "badge": "BẢN VẼ CƠ KHÍ",
                "banner_title": "NÓN GIẢM ÁP VÀ MÍ MẮT THỨ BA",
                "chapter_title": "Bản vẽ khí động học: Nón giảm áp nẹp mũi chống nổ phổi và kính bảo hộ sinh học",
                "hook": "BẢN VẼ KỸ THUẬT: CƠ CHẾ NÉN KHÍ VÀ MÀNG BẢO VỆ MẮT SIÊU THANH",
                "mood": "hao_hung",
                "parts": [
                    {
                        "text": "Bản vẽ kỹ thuật tầng một: Hệ thống điều hòa áp suất khí quyển. Các bạn hãy nhìn thẳng vào lỗ mũi của Chim Cắt Lớn. Bình thường lỗ mũi chim chỉ là một cái khe trơn nhẵn, nhưng ở Tiêm Kích Lông Vũ, ngay chính giữa mỗi lỗ mũi lại mọc ra một nón xương nhô lên hình xoắn ốc gọi là tu-béc-cơ. Đây chính là kiệt tác khí động học trị giá triệu đô của mẹ thiên nhiên!",
                        "mood": "hao_hung"
                    },
                    {
                        "text": "Khi chim cắt bổ nhào với vận tốc ba trăm tám mươi chín ki-lô-mét một giờ, luồng không khí dội vào mũi với áp lực khổng lồ. Nếu không có vật cản, luồng khí nén này sẽ tràn thẳng vào khí quản như một quả bom nổ chậm, làm vỡ tan các phế nang phổi trong nửa giây. Nhưng chiếc nón tu-béc-cơ đóng vai trò như một van giảm chấn siêu cấp, chia nhỏ luồng gió thành các xoáy khí chậm dần, giúp chim hít thở êm ái như đang ngồi uống trà sữa ở vận tốc ba trăm ki-lô-mét một giờ! [surprise-wa]",
                        "mood": "don_dap"
                    },
                    {
                        "text": "Chi tiết này thông minh đến mức các kỹ sư hàng không vũ trụ khi thiết kế động cơ phản lực cho siêu máy bay do thám ét-sơ-rờ bảy mươi mốt Bờ-lách-bớt đã phải mô phỏng y hệt chiếc nón giảm áp này ở cửa hút gió để động cơ không bị nghẹt khí khi bay siêu âm!",
                        "mood": "tram_bi_an"
                    },
                    {
                        "text": "Bản vẽ kỹ thuật tầng hai: Cánh khí động học chống rung gãy. Toàn bộ bộ lông của chim cắt được phủ một lớp vảy vi mô đặc biệt. Khi chim gập cánh tạo hình lưỡi liềm, các hàng lông cánh tự động khóa chặt vào nhau thành một bề mặt cứng cáp liền khối, triệt tiêu hoàn toàn hiện tượng rung lắc khí động học vốn có thể xé toạc đôi cánh của những loài chim thông thường! Không chỉ có vậy, ở chóp cánh chim cắt còn có các sợi lông tơ đóng vai trò như cảm biến vi chấn. Khi phát hiện luồng khí nhiễu loạn ở rìa cánh, các sợi lông này lập tức dựng đứng lên một góc nhỏ để tái định hướng dòng khí, giống hệt như cánh nhỏ ở đầu cánh của máy bay Bo-ing hiện đại!",
                        "mood": "hao_hung"
                    },
                    {
                        "text": "Chưa hết đâu đội kỹ thuật! Khi lao qua tầng mây với vận tốc tên lửa, bụi cát và gió lốc sẽ cào xước mắt bạn ra sao? Chim cắt không hề lo chuyện đó vì nó sở hữu một mí mắt thứ ba trong suốt, tựa như một chiếc kính bảo hộ sinh học. Mí mắt này quét ngang nhấp nháy liên tục, vừa bôi trơn nước mắt chống khô rát, vừa đóng vai trò như kính chắn gió trong suốt cho phép chim nhìn rõ từng cọng lông của con mồi mà không cần chớp mắt!",
                        "mood": "hao_hung"
                    }
                ]
            },
            {
                "id": "scene03",
                "badge": "HỆ THỐNG RADAR",
                "banner_title": "MẮT ĐÔI VÀ XOẮN ỐC LOGARIT",
                "chapter_title": "Hệ thống ngắm bắn: Hốc mắt đôi fovea và quỹ đạo bay xoắn ốc logarit",
                "hook": "HỆ THỐNG NGẮM BẮN: QUỸ ĐẠO XOẮN ỐC LOGARIT KHÓA MỤC TIÊU CÁCH 3KM",
                "mood": "don_dap",
                "parts": [
                    {
                        "text": "Chuyển sang bản vẽ tầng ba: Hệ thống ngắm bắn và cảm biến quang học tầm xa. Đôi mắt của Chim Cắt Lớn chiếm tới gần nửa trọng lượng hộp sọ. Trong khi mắt người chỉ có một điểm vàng hội tụ ánh sáng sắc nét nhất, thì mắt chim cắt lại trang bị hẳn hai hốc mắt sâu gọi là pho-ve-a đôi: một hốc nhìn thẳng để định vị cự ly và một hốc nhìn xéo sang hai bên với độ phân giải siêu nét gấp tám lần mắt phi công!",
                        "mood": "don_dap"
                    },
                    {
                        "text": "Cảm biến quang học báo cáo: Khóa mục tiêu là một chú bồ câu béo múp ở khoảng cách ba ki-lô-mét! Tọa độ đã lưu vào bộ nhớ!",
                        "cast": "phat_thanh_vien"
                    },
                    {
                        "text": "[laughter] Nhìn thấy mục tiêu cách ba ki-lô-mét là một chuyện, nhưng làm sao để lao xuống đớp mồi lại nảy sinh một nghịch lý vật lý vô cùng đau đầu. Giáo sư Van-xơ Tắc-cơ thuộc Đại học Duke qua các bài báo trên tạp chí Thực nghiệm Sinh học đã phát hiện ra bí mật chấn động: Hốc mắt nhìn nét nhất của chim cắt nằm lệch một góc bốn mươi độ sang bên cạnh. Nếu chim bay thẳng tắp cắm đầu xuống, nó sẽ phải ngoẹo cổ sang một bên để nhìn mồi!",
                        "mood": "hao_hung"
                    },
                    {
                        "text": "Mà các kỹ sư biết đấy, đang lao ba trăm ki-lô-mét một giờ mà ngoẹo đầu sang bên thì lực cản gió sẽ bẻ gãy cổ hoặc làm chim xoay mòng mòng mất lái ngay lập tức! Để giải bài toán hóc búa này, Tiêm Kích Lông Vũ đã lập trình sẵn trong não bộ một đường bay xoắn ốc logarit hoàn hảo. Nó giữ đầu thẳng tắp để triệt tiêu tối đa lực cản, đồng thời nghiêng thân lượn theo một đường cong hình học chính xác tuyệt đối, giữ cho mắt luôn nhìn chằm chằm vào con mồi suốt từ độ cao ba ngàn mét xuống đất! Quả là một thuật toán dẫn đường tên lửa đỉnh cao!",
                        "mood": "tram_bi_an"
                    },
                    {
                        "text": "Đặc biệt hơn nữa, não bộ của chim cắt xử lý hình ảnh với tần số lên tới một trăm ba mươi khung hình một giây, cao hơn gấp đôi mức sáu mươi khung hình một giây của con người! Nhờ khả năng siêu xử lý này, toàn bộ quỹ đạo của con mồi bay lượn bên dưới đều hiện ra như những cảnh quay chậm chậm rãi, cho phép chim cắt căn chỉnh góc tấn công mượt mà như trong trò chơi điện tử!",
                        "mood": "hao_hung"
                    }
                ]
            },
            {
                "id": "scene04",
                "badge": "ĐÒN THỰC CHIẾN",
                "banner_title": "GIA LỰC 25G VÀ CÚ ĐẤM NẮM TAY",
                "chapter_title": "Đòn đánh thực chiến: Cú kéo lên 25G và nắm đấm móng vuốt hạ gục con mồi",
                "hook": "THỰC CHIẾN TÀN KHỐC: CHỊU ĐỰNG GIA TỐC 25G VÀ CÚ VA CHẠM KINH HOÀNG",
                "mood": "hao_hung",
                "parts": [
                    {
                        "text": "Bây giờ, mời đội kỹ thuật chứng kiến khoảnh khắc khai hỏa đòn tấn công thực chiến. Khi đã áp sát con mồi ở cự ly ba trăm mét, chim cắt gập chặt hai cánh vào sát thân mình, biến toàn bộ cơ thể thành một viên đạn hình giọt nước khí động học hoàn hảo. Lúc này, tim của nó đập điên cuồng từ sáu trăm đến chín trăm nhịp một phút để bơm oxy tới từng thớ cơ ngực săn chắc như đá tảng.",
                        "mood": "hao_hung"
                    },
                    {
                        "text": "Nhưng điều đáng kinh ngạc nhất nằm ở cách nó hạ gục con mồi. Nó không hề xòe móng ra để quắp như đại bàng hay diều hâu. Ở vận tốc ba trăm ki-lô-mét một giờ, nếu xòe móng quắp mồi, quán tính dữ dội sẽ bẻ gãy ngón chân chim cắt ngay lập tức! Thay vào đó, nó cuộn tròn các ngón chân lại thành một nắm đấm đặc sệt bọc sừng, biến thành một quả đấm thép bay tự do!",
                        "mood": "don_dap"
                    },
                    {
                        "text": "Rầm! Nắm đấm móng vuốt giáng thẳng vào lưng hoặc cánh của con mồi với động năng tương đương một viên đạn chì bắn ra từ súng hơi. Hãy tưởng tượng một quả tạ kim loại nặng gần một ki-lô-gam đập thẳng vào bạn ở tốc độ ba trăm ki-lô-mét một giờ! Cú va chạm kinh hoàng làm con mồi gãy cổ rụng rơi tự do trong không trung, trước khi chim cắt lộn một vòng ngoạn mục để đón lấy chiến lợi phẩm giữa tầng mây!",
                        "mood": "hao_hung"
                    },
                    {
                        "text": "Ngay sau cú va chạm nổ tung, chim cắt phải thực hiện một động tác hãm phanh kéo ngược cơ thể lên trên không trung. Đây chính là thời khắc sinh tử: Nếu tính toán sai chỉ một phần mười giây không phẩy một giây, nó sẽ cắm thẳng đầu xuống đất và nát vụn thành trăm mảnh!",
                        "mood": "don_dap"
                    },
                    {
                        "text": "[surprise-oh] Và hãy nhìn vào thông số gia tốc kéo lên: Hai mươi lăm G! Một phi công lái máy bay chiến đấu hiện đại nhất chỉ chịu được tối đa chín G trong vài giây là mạch máu tụ xuống chân, mắt tối sầm ngất xỉu. Ấy thế mà Tiêm Kích Lông Vũ chịu đựng hai mươi lăm G mà mắt vẫn sáng quắc, đầu vẫn tỉnh queo! Khung xương đòn chữ V liền khối của nó cứng vững gấp mười lần vật liệu hợp kim nhân tạo! [laughter]",
                        "mood": "don_dap"
                    }
                ]
            },
            {
                "id": "scene05",
                "badge": "TỬ HUYỆT VŨ KHÍ",
                "banner_title": "DÁNG ĐI NGỐ VÀ VỎ TRỨNG MỎNG",
                "chapter_title": "Tử huyệt kỹ thuật: Dáng đi vụng về dưới mặt đất và cuộc khủng hoảng DDT",
                "hook": "ĐIỂM YẾU BẤT NGỜ: TIÊM KÍCH VỤNG VỀ TRÊN MẶT ĐẤT VÀ HIỂM HỌA TUYỆT CHỦNG",
                "mood": "bi_hai",
                "parts": [
                    {
                        "text": "Thưa các kỹ sư, theo đúng quy chuẩn báo cáo hồ sơ vũ khí ép hai, không có vũ khí nào là hoàn hảo tuyệt đối. Mọi cỗ máy tối tân đều phải đánh đổi bằng những điểm yếu kỹ thuật dở khóc dở cười. Điểm yếu thứ nhất của Chim Cắt Lớn chính là: Đừng bao giờ bắt nó đi bộ dưới mặt đất!",
                        "mood": "bi_hai"
                    },
                    {
                        "text": "Vì toàn bộ thiết kế tiến hóa dồn hết cho việc bay liệng siêu tốc, đôi chân của chim cắt rất ngắn, cơ đùi yếu và móng vuốt quá cong dài. Khi hạ cánh xuống bãi cỏ, từ một tiêm kích bầu trời oai phong lẫm liệt, nó bỗng biến hình thành một chú bồ câu say rượu đi lạch bạch vụng về, nhảy chồm chồm như vừa dẫm phải đinh! Nếu con mồi chạy ngoằn ngoèo trong bụi rậm dưới đất, tỷ lệ tóm mồi của chim cắt tụt dốc thê thảm từ chín mươi phần trăm xuống dưới hai mươi lăm phần trăm! [laughter]",
                        "mood": "hao_hung"
                    },
                    {
                        "text": "Chưa dừng lại ở đó, kỹ năng cận chiến trên mặt đất của nó tệ đến mức thường xuyên bị quạ đen, hải âu hay bồ nông nhảy vào bắt nạt và cướp trắng bữa ăn vừa săn được, khiến sát thủ siêu thanh chỉ biết đứng trơ mắt nhìn đầy bất lực!",
                        "mood": "bi_hai"
                    },
                    {
                        "text": "Nhưng bi kịch đen tối nhất trong lịch sử của Tiêm Kích Lông Vũ lại không đến từ thiên địch tự nhiên, mà đến từ một hóa chất vô hình do con người tạo ra vào thập niên một ngàn chín trăm sáu mươi: Thuốc trừ sâu Đê Đê Tê. Khi chim cắt ăn các loài chim nhỏ tích tụ hóa chất này, chất độc phá hủy cơ chế chuyển hóa canxi, khiến vỏ trứng chim cắt mỏng đi trông thấy.",
                        "mood": "tram_bi_an"
                    },
                    {
                        "text": "Hậu quả là mỗi khi chim bố mẹ ấp trứng, chính sức nặng cơ thể chúng lại vô tình đè bẹp nát những đứa con chưa kịp chào đời. Toàn bộ quần thể chim cắt ở Bắc Mỹ và châu Âu sụt giảm nghiêm trọng đến mức suýt bị xóa sổ vĩnh viễn khỏi bản đồ sinh học, gióng lên hồi chuông cảnh tỉnh đau đớn cho cả nhân loại!",
                        "mood": "tram_bi_an"
                    }
                ]
            },
            {
                "id": "scene06",
                "badge": "NGHIỆM THU HỒ SƠ",
                "banner_title": "BÀN GIAO VŨ KHÍ VÀ TẬP KẾ TIẾP",
                "chapter_title": "Báo cáo nghiệm thu: Bài học phục hồi và câu đố bóng đen quái kiệt tập 32",
                "hook": "TỔNG KẾT HỒ SƠ: SỰ HỒI SINH NGOẠN MỤC VÀ DỰ BÁO TẬP KẾ TIẾP",
                "mood": "am_ap",
                "parts": [
                    {
                        "text": "May mắn thay, chiến dịch bảo tồn quy mô toàn cầu sau lệnh cấm Đê Đê Tê năm một ngàn chín trăm bảy mươi hai đã tạo nên một kỳ tích phục hồi ngoạn mục. Các nhà khoa học đã nhân giống thả chim về tự nhiên, và giờ đây Tiêm Kích Lông Vũ lại kiêu hãnh chao lượn trên bầu trời các tòa nhà chọc trời từ Nữu Ước tới Luân Đôn, biến nó thành biểu tượng bất diệt cho khả năng phục hồi của mẹ thiên nhiên.",
                        "mood": "am_ap"
                    },
                    {
                        "text": "Báo cáo nghiệm thu kỹ thuật: Vũ khí siêu thanh hoàn toàn đạt chuẩn! Đề nghị lưu trữ vào kho dữ liệu khoa học bảo tồn!",
                        "cast": "phat_thanh_vien"
                    },
                    {
                        "text": "Đội kỹ thuật thân mến, bạn thấy ấn tượng nhất với trang bị nào của Chim Cắt Lớn: Nón xương chống nổ phổi trong lỗ mũi, hốc mắt đôi xoắn ốc logarit hay quả đấm thép chịu gia lực hai mươi lăm G? Hãy để lại bình luận phân tích của bạn ngay bên dưới nhé!",
                        "mood": "hao_hung"
                    },
                    {
                        "text": "Và ngay trong hồ sơ giải mật tập ba mươi hai tiếp theo, chúng ta sẽ rời bầu trời cao vời vợi để chui sâu xuống lòng đất tối tăm, gặp gỡ một bóng đen bí ẩn dị hợm bậc nhất hành tinh! Sinh vật này hoàn toàn trụi lông, da nhăn nheo như củ khoai tây luộc, không hề biết cảm giác đau đớn trước axit đậm đặc và sở hữu bộ gen miễn nhiễm ung thư kỳ diệu giúp nó sống thọ tới hơn ba mươi năm, gấp mười lần họ hàng loài gặm nhấm! Đố các kỹ sư đoán được bóng đen quái kiệt tiếp theo này là ai?",
                        "mood": "tram_bi_an"
                    }
                ]
            }
        ]
    },
    "shorts": {
        "target_s": 53.0,
        "mood": "hao_hung",
        "text": "Hồ sơ mật cấp độ đỏ. Mở khóa! [surprise-oh] Tại sao khi lao xuống từ độ cao năm ngàn mét với vận tốc ba trăm tám mươi chín ki-lô-mét một giờ, hai lá phổi của Chim Cắt Lớn không hề bị nổ tung? Đây chính là Tiêm Kích Lông Vũ, sinh vật bay nhanh nhất lịch sử hành tinh chúng ta! Ở tốc độ khủng khiếp gần bốn trăm ki-lô-mét một giờ, áp lực không khí mạnh đến mức có thể thổi rách toạc khí quản của bất kỳ con thú nào. Nhưng mẹ thiên nhiên đã bí mật lắp đặt ngay trong lỗ mũi chim cắt một chiếc nón xương xoắn ốc tí hon gọi là tu-béc-cơ. Chiếc nón giảm áp này chia nhỏ luồng gió nén thành các xoáy khí chậm, giúp chim hít thở êm ái như đang ngồi hóng gió mát! Đến cả siêu máy bay do thám ét-sơ-rờ bảy mươi mốt Bờ-lách-bớt của con người cũng phải học lỏm thiết kế nón cản sốc này để bay siêu âm. Chưa hết, chim cắt còn cuộn ngón chân thành quả đấm thép giáng thẳng vào con mồi, chịu gia lực tới hai mươi lăm G mà mắt vẫn tỉnh queo! Một kiệt tác khí động học đỉnh chóp của tự nhiên!"
    },
    "seo": {
        "title": "Sinh Vật Bổ Nhào 389 km/h & Nón Nén Khí Chống Nổ Phổi?! | Tập 31",
        "hook_paragraph": "Chim Cắt Lớn (Falco peregrinus) đạt kỷ lục tốc độ bổ nhào không tưởng 389 km/h xé toạc bầu trời. Tại sao lá phổi của nó không bị nổ tung trước áp lực gió cực lớn và làm thế nào để nó khóa mục tiêu con mồi cách 3km bằng quỹ đạo xoắn ốc logarit kỳ diệu?",
        "bullets": [
            "Kỷ lục bổ nhào 389 km/h từ độ cao 5.000m đo đạc bằng thiết bị gắn trên cơ thể chim năm 2005",
            "Bản vẽ nón giảm áp tubercle trong lỗ mũi giúp hít thở an toàn mà không nổ phổi",
            "Đôi mắt fovea đôi nhìn xa 3km và thuật toán quỹ đạo bay xoắn ốc logarit của Vance Tucker",
            "Cú đấm móng vuốt mid-air hạ gục con mồi và khả năng chịu gia lực 25G gấp 3 lần phi công chiến đấu",
            "Tử huyệt dáng đi lạch bạch dưới đất và bài học bảo tồn sau thảm họa thuốc trừ sâu DDT"
        ],
        "question": "Trong các trang bị khí động học của Chim Cắt Lớn, bạn thấy chi tiết nào thông minh nhất: Nón nén khí trong mũi, quỹ đạo xoắn ốc logarit hay quả đấm thép chịu lực 25G?",
        "next_teaser": "bóng đen quái kiệt trụi lông dưới lòng đất, không biết đau đớn và miễn nhiễm ung thư",
        "hashtag_broad": "#độngvật",
        "hashtag_animal": "#chimcắt",
        "hashtags": ["#độngvật", "#chimcắt", "#VẽChuyệnHoangDã"],
        "tags": [
            "chim cắt lớn", "chim cắt", "peregrine falcon", "falco peregrinus",
            "chim bay nhanh nhất thế giới", "động vật nhanh nhất hành tinh", "bổ nhào 389 km/h",
            "nón giảm áp tubercle", "xoắn ốc logarit", "gia tốc 25G", "vũ khí sinh học",
            "thế giới động vật", "vẽ chuyện hoang dã", "whiteboard animation", "khoa học vui"
        ],
        "shorts_title": "Tại Sao Phổi Chim Cắt Không Nổ Tung Ở Tốc Độ 389 km/h?!",
        "shorts_desc": "Chim Cắt Lớn (Falco peregrinus) lao xuống từ độ cao 5.000m với tốc độ 389 km/h mà hai lá phổi không hề bị áp lực gió thổi nổ tung nhờ chiếc nón giảm áp tubercle tối mật trong lỗ mũi! Khám phá kiệt tác khí động học tự nhiên truyền cảm hứng cho siêu tiêm kích SR-71 Blackbird.",
        "shorts_tags": ["chim cắt lớn", "peregrine falcon", "shorts", "động vật", "khoa học", "vẽ chuyện hoang dã"],
        "en_title": "How Peregrine Falcon Dives at 389 km/h Without Exploding Lungs?! | Ep 31",
        "en_hook": "The Peregrine Falcon is the fastest animal on Earth, diving at an astonishing 389 km/h (242 mph). How do its lungs survive the massive airflow shockwave, and how does it target prey using a logarithmic spiral flight path?",
        "en_chapters": [
            "Declassified File: The 389 km/h Stoop Dive Record",
            "Mechanical Blueprint: Nasal Baffles and Third Eyelid",
            "Targeting Radar: Dual Foveae and Logarithmic Spiral",
            "Combat Strike: 25G Pull-Out and Clenched Talon Punch",
            "Technical Weakness: Clumsy Ground Walking and DDT Crisis",
            "Final Inspection: Conservation Triumph and Next Episode Teaser"
        ],
        "en_shorts_title": "Why Don't Falcon Lungs Burst at 389 km/h?!"
    }
}

(P / "episode.json").write_text(json.dumps(ep, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Written updated episode.json successfully!")
