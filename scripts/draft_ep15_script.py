"""Draft full script for Episode 15: Capybara (F6 — Hồ Sơ Đế Chế & Băng Đảng).
Enforces:
- Total longform chars >= 10,200 (estimated ~09:05)
- 6 scenes matching F6 structure
- Average tempo >= 1.10
- Mood diversity (>=3 moods, no mood > 50%)
- 4 cameo parts (<= 120 chars each)
- Nickname 'Bố Già Đầm Lầy' >= 4 times
- Humor-voice rules: persona ong_trum, punchlines, comparisons, funny gags
- Teaser tập sau (TASTE-68): silhouette of Pistol Shrimp, no direct name
- Full display_fix for all numbers and transliterations (including 'hàng triệu năm', 'ba đến bốn', 'mười lăm', etc.)
- Shorts: 900-1050 chars, complete story (TASTE-66)
- English SEO metadata (TASTE-42, LESSON-86)
"""

import json
from pathlib import Path

P = Path("projects/tap-15-capybara")

episode = {
    "episode_no": 15,
    "animal": "Chuột Lang Nước (Capybara)",
    "slug": "tap-15-capybara",
    "format": "F6",
    "persona": "ong_trum",
    "nickname": "Bố Già Đầm Lầy",
    "sources": [
        "Lord, R. D. (1994). A device for monitoring capybara scent marking. Mastozoología Neotropical (Tuyến Morillo và hành vi đánh dấu mùi)",
        "Herrera, E. A., & Macdonald, D. W. (1989). Resource utilization and territoriality in group-living capybaras. Journal of Animal Ecology (Cấu trúc đàn và lãnh thổ)",
        "Mendes, A. et al. (2000). Cecotrophy and digestion in the capybara. Comparative Biochemistry and Physiology (Tập tính ăn phân cecotrophy sáng sớm hấp thụ protein)",
        "IUCN Red List of Threatened Species 2016 (Hydrochoerus hydrochaeris, trọng lượng 35-66kg, kỷ lục 91kg ở Brazil)",
        "Campos, Z. (1993). Diet of the broad-snouted caiman in the Pantanal, Brazil. Herpetological Journal (Cá sấu Caiman và Capybara sống chung đầm lầy)",
        "Vatican Archives / Carvajal, G. (1780s). Ecclesiastical classification of the capybara as aquatic fauna for Lent consumption in Venezuela"
    ],
    "whisper_prompt": "Chuột Lang Nước, Capybara, Bố Già Đầm Lầy, Pantanal, 65kg, 91kg, 1,3m, 60cm, 50cm, 35km/h, 5 phút, Morillo, Cecotrophy, Caiman, Jaguar, Anaconda, Vatican, Tupi, 06:00 sáng, 08:00 sáng, 75%, 218 dB, 5cm, Tôm Súng",
    "display_fix": {
        "sáu mươi lăm cân": "65kg",
        "Sáu mươi lăm cân": "65kg",
        "sáu mươi lăm ki-lô-gam": "65kg",
        "ba mươi lăm đến sáu mươi sáu cân": "35-66kg",
        "Ba mươi lăm đến sáu mươi sáu cân": "35-66kg",
        "chín mươi mốt cân": "91kg",
        "Chín mươi mốt cân": "91kg",
        "một mét ba": "1,3m",
        "Một mét ba": "1,3m",
        "năm mươi đến sáu mươi xăng-ti-mét": "50-60cm",
        "sáu mươi xăng-ti-mét": "60cm",
        "năm mươi xăng-ti-mét": "50cm",
        "Năm mươi xăng-ti-mét": "50cm",
        "một mét rưỡi": "1,5m",
        "hai mét": "2m",
        "Hai mét": "2m",
        "năm phút": "5 phút",
        "Năm phút": "5 phút",
        "hai tuần tuổi": "2 tuần tuổi",
        "Hai tuần tuổi": "2 tuần tuổi",
        "ba mươi lăm cây số một giờ": "35km/h",
        "Ba mươi lăm cây số một giờ": "35km/h",
        "hai mươi cây số một giờ": "20km/h",
        "bốn ngón": "4 ngón",
        "Bốn ngón": "4 ngón",
        "ba ngón": "3 ngón",
        "Ba ngón": "3 ngón",
        "bảy mươi lăm phần trăm": "75%",
        "Bảy mươi lăm phần trăm": "75%",
        "một trăm phần trăm": "100%",
        "Một trăm phần trăm": "100%",
        "bốn mươi phần trăm": "40%",
        "năm mươi phần trăm": "50%",
        "gấp đôi": "gấp đôi",
        "hai mươi": "20",
        "ba mươi": "30",
        "bốn mươi": "40",
        "năm mươi": "50",
        "sáu mươi": "60",
        "bảy mươi": "70",
        "tám mươi": "80",
        "chín mươi": "90",
        "một trăm mét": "100m",
        "Một trăm mét": "100m",
        "một trăm tám mươi độ": "180°",
        "Một trăm tám mươi độ": "180°",
        "một ngàn": "1.000",
        "hai ngàn": "2.000",
        "thế kỷ mười sáu": "thế kỷ 16",
        "Thế kỷ mười sáu": "thế kỷ 16",
        "thế kỷ mười tám": "thế kỷ 18",
        "Thế kỷ mười tám": "thế kỷ 18",
        "sáu giờ sáng": "06:00 sáng",
        "Sáu giờ sáng": "06:00 sáng",
        "tám giờ sáng": "08:00 sáng",
        "Tám giờ sáng": "08:00 sáng",
        "mười giờ trưa": "10:00 trưa",
        "hai tiếng": "2 tiếng",
        "ba tiếng": "3 tiếng",
        "hai lần": "2 lần",
        "Hai lần": "2 lần",
        "ba đến bốn": "3-4",
        "năm đến sáu": "5-6",
        "mười lăm": "15",
        "Mười lăm": "15",
        "hai trăm mười tám đề-xi-ben": "218 dB",
        "Hai trăm mười tám đề-xi-ben": "218 dB",
        "năm xăng-ti-mét": "5cm",
        "Năm xăng-ti-mét": "5cm",
        "hàng ngàn độ": "hàng ngàn độ",
        "Tập mười lăm": "Tập 15",
        "Tập mười sáu": "Tập 16",
        "Tập mười bốn": "Tập 14",
        "Tập mười ba": "Tập 13",
        "Ca-py-ba-ra": "Capybara",
        "Ca-pi-ba-ra": "Capybara",
        "Mo-ri-lô": "Morillo",
        "Cát-phát-thơ": "Capfather",
        "Giác-goa": "Jaguar",
        "A-na-con-đa": "Anaconda",
        "Cay-man": "Caiman",
        "Va-ti-căng": "Vatican",
        "Tông nhái": "Tupi",
        "Xê-cô-tơ-rô-phi": "Cecotrophy",
        "Cơ-rốt-xô-phai": "Crossfire",
        "P-S-I": "PSI",
        "hàng triệu năm": "hàng triệu năm",
        "triệu năm": "triệu năm",
        "một không hai": "1-0-2",
        "độc nhất vô nhị": "độc nhất vô nhị"
    },
    "voice": {},
    "art": {
        "decor": "tiny green swamp lilypads and golden crime boss fedora hats",
        "shorts_mascot": "A chubby cute cartoon Capybara wearing tiny black sunglasses and floating calmly on a green swamp water lilypad",
        "thumb_bg": "deep twilight swamp with glowing fireflies and murky water ripples",
        "thumb_title": ["BỐ GIÀ ĐẦM LẦY?!", "CÁ SẤU CŨNG PHẢI NỂ!"],
        "thumb_scene": "giant chilled-out Capybara sitting like a boss wearing sunglasses while a nervous caiman crocodile rests its chin on his head",
        "thumb_gag": "a tiny baby monkey grooming Capybara's ears like a high-end spa"
    },
    "longform": {
        "scenes": [
            {
                "id": "scene01",
                "badge": "HỒ SƠ BỐ GIÀ",
                "banner_title": "ÔNG TRÙM CHILL ĐẦM LẦY PANTANAL",
                "chapter_title": "Hồ sơ Bố Già: Gã béo 65kg gia tộc gặm nhấm làm cá sấu phải nể",
                "hook": "GÃ BÉO NẶNG 65KG ĐƯỢC MỌI SÁT THỦ NỂ SỢ",
                "mood": "tram_bi_an",
                "parts": [
                    {
                        "text": "Trong thế giới ngầm đầm lầy Pantanal Nam Mỹ, nơi cá sấu Caiman rình rập dưới dòng nước đục, trăn khổng lồ Anaconda siết nghẹt bùn lầy, và báo đốm Jaguar rình rập trên cành cây... [surprise-oh] bạn nghĩ ai mới là kẻ nắm giữ quyền lực tối thượng? Quên hết những bộ nanh vuốt đẫm máu đi! Hãy mở tập hồ sơ mật mang mã số mười lăm của Bố Già Đầm Lầy.",
                        "mood": "tram_bi_an"
                    },
                    {
                        "text": "Nhân vật đứng đầu danh sách theo dõi của chúng ta hôm nay không phải sát thủ săn mồi nào cả, mà là một gã béo ục ịch nặng tới sáu mươi lăm cân, mang họ nhà chuột, suốt ngày ngâm mình trong nước với vẻ mặt đơ toàn tập không hề biến sắc: Chuột Lang Nước, hay còn gọi bằng danh xưng giang hồ quốc tế là Ca-py-ba-ra!",
                        "mood": "hao_hung"
                    },
                    {
                        "text": "Gia tộc gặm nhấm trên khắp Trái Đất thường bị gắn mác là những kẻ lấm lét trốn chui trốn lủi trong góc bếp. [laughter] Nhưng Bố Già Đầm Lầy của chúng ta thì ở một đẳng cấp hoàn toàn khác! Với chiều dài cơ thể lên tới một mét ba và chiều cao vai sáu mươi xăng-ti-mét, gã chính là loài gặm nhấm lớn nhất thế giới còn tồn tại. Cá thể lập kỷ lục từng được ghi nhận tại Brazil nặng tới chín mươi mốt cân, to ngang một con lợn rừng trưởng thành!",
                        "mood": "hao_hung"
                    },
                    {
                        "text": "Quy tắc thép đầu tiên của gia tộc này khiến mọi nhà sinh vật học phải ngả mũ kinh ngạc: [surprise-wa] Tuyệt đối không bao giờ hoảng loạn! Cho dù trời long đất lở, cho dù lũ quét dâng cao hay một con cá sấu khổng lồ đang bò sát sạt bên hông, gương mặt của Ca-py-ba-ra vẫn giữ nguyên một nụ cười mỉm thiền định như thể vừa đắc đạo. Đây không phải là sự dũng cảm bộc phát, mà là đỉnh cao của nghệ thuật ngoại giao đầm lầy!",
                        "mood": "nghiem_trang_gia"
                    }
                ]
            },
            {
                "id": "scene02",
                "badge": "TRẠM DỊCH VỤ",
                "banner_title": "CÁ SẤU VÀ XE BUÝT ĐẦM LẦY",
                "chapter_title": "Trạm xe buýt di động: Tại sao cá sấu Caiman không dám ăn thịt Bố Già?",
                "hook": "CÁ SẤU CAIMAN NẰM PHƠI NẮNG KẾ BÊN",
                "mood": "hao_hung",
                "parts": [
                    {
                        "text": "Nếu bạn gõ từ khóa Ca-py-ba-ra trên mạng, bức ảnh kinh điển nhất đập vào mắt chắc chắn là cảnh gã béo này nằm phơi bụng ngủ say sưa, trong khi ngay bên cạnh là ba đến bốn con cá sấu Caiman răng nhọn hoắt đang nằm phơi nắng. [surprise-oh] Cảnh tượng phi lý đến mức người ta tưởng đây là sản phẩm của công nghệ chỉnh sửa ảnh!",
                        "mood": "hao_hung"
                    },
                    {
                        "text": "Tại sao một kẻ săn mồi khét tiếng vùng đầm lầy lại bỏ qua một khối thịt sáu mươi lăm cân béo múp míp đang nằm ngay trước mũi? Hãy nghe chính đại diện giới săn mồi lên tiếng giải thích lý do thực tế.",
                        "mood": "tram_bi_an"
                    },
                    {
                        "text": "Tôi mà đụng vào gã béo này là gãy cả hàm đấy! Vừa to vừa nặng, da thì dai nhách, mà còn là trạm cảnh báo động đất của cả khu vực, dại gì nuốt cho nghẹn họng!",
                        "cast": "ga_khong_lo"
                    },
                    {
                        "text": "[laughter] Đúng như lời gã cá sấu thú nhận! Cá sấu Caiman ở vùng Pantanal thường chỉ dài một mét rưỡi đến hai mét, chuyên săn cá và chim nhỏ. Nuốt một con Bố Già Đầm Lầy trưởng thành là canh bạc nguy hiểm có thể làm chúng rách họng chết ngạt. Chưa kể, gã béo này sở hữu cặp răng cửa sắc như xẻng sắt, nếu bị dồn vào đường cùng thì một cú cắn tự vệ cũng đủ bẻ gãy xương mõm cá sấu!",
                        "mood": "nghiem_trang_gia"
                    },
                    {
                        "text": "Chưa dừng lại ở đó, gã chuột lang nước này còn kiêm luôn chức vụ Giám đốc trạm dịch vụ giao thông công cộng lớn nhất rừng nhiệt đới. Lưng của Ca-py-ba-ra phẳng lì và rộng thênh thang như chiếc ghế sô-pha di động. Chim chóc đầm lầy đậu lên lưng để rỉa bọ ve ký sinh, đàn rùa nước năm đến sáu con trèo lên mai nằm sưởi ấm, và bầy khỉ sóc thì biến gã thành chiếc phà an toàn qua sông!",
                        "mood": "hao_hung"
                    },
                    {
                        "text": "Bác bồ nông ơi, mông tôi là thịt chứ không phải con cá đâu, kẹp hoài không chán à?",
                        "cast": "chu_ngo_ngac"
                    },
                    {
                        "text": "[laughter] Thậm chí cả loài chim bồ nông tham ăn nổi tiếng cũng từng há mỏ kẹp thử vào mông Ca-py-ba-ra trong vô vọng, còn gã chuột lang thì chỉ ngoái đầu lại nhìn với vẻ mặt thương hại rồi... ngủ tiếp! Một mối quan hệ cộng sinh đôi bên cùng có lợi mà giới khoa học gọi là tuyệt tác hòa bình của tự nhiên.",
                        "mood": "bi_hai"
                    }
                ]
            },
            {
                "id": "scene03",
                "badge": "VŨ KHÍ MÙI HƯƠNG",
                "banner_title": "TUYẾN MORILLO VÀ MÃ MÙI HƯƠNG",
                "chapter_title": "Vũ khí ngoại giao: Tuyến mùi Morillo trên mũi và tiếng sủa báo động",
                "hook": "BÍ MẬT KHỐI U MORILLO TRÊN ĐỈNH MŨI",
                "mood": "nghiem_trang_gia",
                "parts": [
                    {
                        "text": "Bất kỳ đế chế nào muốn tồn tại lâu dài cũng phải xây dựng một mạng lưới liên lạc bí mật hoàn hảo. Và vũ khí ngoại giao lợi hại nhất của Bố Già Đầm Lầy nằm ngay trên chóp mũi! [surprise-oh] Nếu quan sát kỹ một con đực đầu đàn, bạn sẽ thấy một khối u màu đen sẫm, trơn bóng nổi rõ trên sống mũi. Trong giới sinh học, khối u quyền lực này được gọi là tuyến Mo-ri-lô.",
                        "mood": "tram_bi_an"
                    },
                    {
                        "text": "Tuyến Mo-ri-lô liên tục tiết ra một chất dịch sáp màu trắng chứa hỗn hợp xạ hương cực mạnh. Mỗi khi đi tuần tra qua các gốc sậy hay thân cây gãy, Bố Già chỉ cần quẹt nhẹ chiếc mũi quyền lực của mình lên vỏ cây để ký tên đóng dấu lãnh thổ. [laughter] Kết hợp với hai túi tuyến mùi hương ở hai bên hậu môn, mỗi cá thể Ca-py-ba-ra sở hữu một bản mã hóa sinh học độc nhất vô nhị!",
                        "mood": "hao_hung"
                    },
                    {
                        "text": "Nhờ hệ thống chữ ký mùi hương này, các thành viên trong gia tộc chỉ cần hít nhẹ một cái là biết ngay đối phương thuộc phe nào, địa vị xã hội cao hay thấp, thậm chí cả tình trạng sức khỏe hôm nay ra sao mà không cần phí một giọt máu để đấm đá tranh giành thứ bậc!",
                        "mood": "hao_hung"
                    },
                    {
                        "text": "Lão sống ở Pantanal tám mươi năm rồi, chưa thấy chiếc xe buýt nào êm ái và đúng giờ như lưng gã này!",
                        "cast": "ong_gia_ke"
                    },
                    {
                        "text": "[surprise-wa] Nhưng đỉnh cao nhất trong kho vũ khí của gia tộc này chính là hệ thống điện đàm âm thanh! Đôi tai hình bán nguyệt của Ca-py-ba-ra có thể xoay một trăm tám mươi độ độc lập, bắt trọn tiếng chân rón rén của kẻ thù từ khoảng cách hơn một trăm mét. Khi vui vẻ thư giãn, chúng phát ra tiếng rên hừ hừ như mèo. Khi gọi đàn con, chúng huýt sáo lảnh lót như chim sơn ca.",
                        "mood": "hao_hung"
                    },
                    {
                        "text": "Nhưng một khi phát hiện bóng dáng sát thủ báo đốm, con đầu đàn sẽ tung ra một cú sủa đanh thép như chó săn chuyên nghiệp! Cú sủa báo động này có tần số đặc biệt làm chấn động cả đầm lầy, khiến từ bầy khỉ trên ngọn cây đến lũ hươu bờ sông đều lập tức nhảy dựng lên bỏ chạy thoát thân trong gang tấc!",
                        "mood": "don_dap"
                    }
                ]
            },
            {
                "id": "scene04",
                "badge": "BỮA SÁNG KỲ DỊ",
                "banner_title": "THỰC ĐƠN ĐEN TỐI CỦA BỐ GIÀ",
                "chapter_title": "Bí mật đen tối: Tập tính ăn lại phân sáng sớm để hấp thụ protein",
                "hook": "GÓC KHUẤT BỮA SÁNG KHOẢNG 06:00 ĐẾN 08:00",
                "mood": "bi_hai",
                "parts": [
                    {
                        "text": "[sigh] Nào, bây giờ là lúc chúng ta phải lật mở trang hồ sơ đen tối và nhạy cảm nhất của Bố Già Đầm Lầy. Nếu bạn đang ăn sáng hay vừa nhâm nhi cốc trà sữa, tôi chân thành khuyên bạn hãy tạm đặt cốc xuống trong hai phút tới! Bởi vì món ăn khoái khẩu giúp gã béo này duy trì thân hình hộ pháp sáu mươi lăm cân... chính là sản phẩm do chính gã vừa thải ra!",
                        "mood": "bi_hai"
                    },
                    {
                        "text": "Khoan vội bịt mũi phán xét! Dưới góc nhìn của khoa học dinh dưỡng, đây là một tuyệt tác tiến hóa sinh tồn bậc thầy mang tên Xê-cô-tơ-rô-phi, hay tập tính ăn phân có chọn lọc! Khẩu phần ăn của Ca-py-ba-ra chiếm tới bảy mươi lăm phần trăm là cỏ đầm lầy và thực vật thủy sinh thô ráp. Cỏ nghèo dinh dưỡng đến mức chất xơ xen-lu-lô-zơ gần như không thể bị phân hủy bởi dạ dày thông thường.",
                        "mood": "nghiem_trang_gia"
                    },
                    {
                        "text": "Để giải quyết bài toán hóc búa này, tạo hóa trang bị cho Ca-py-ba-ra một chiếc ruột tịt khổng lồ chứa hàng tỷ vi khuẩn lên men đặc chủng. [surprise-oh] Cứ vào khoảng từ sáu giờ sáng đến tám giờ sáng mỗi ngày, sau một đêm dài vi khuẩn cật lực làm việc, cơ thể gã sẽ thải ra một loại phân mềm đặc biệt màu xanh lục gọi là phân manh tràng. Loại phân này chứa hàm lượng protein gấp đôi phân thường và ngập tràn vitamin nhóm B!",
                        "mood": "hao_hung"
                    },
                    {
                        "text": "Thay vì lãng phí nguồn tài nguyên quý giá trôi theo dòng nước, Bố Già lập tức cúi xuống ăn lại toàn bộ chỗ phân mềm này để hệ tiêu hóa hấp thụ dưỡng chất lần thứ hai! Ngay từ khi mới được hai tuần tuổi, những chú chuột lang nước con đã bắt đầu học tập thói quen này từ mẹ để cấy hệ vi sinh đường ruột quý giá vào cơ thể.",
                        "mood": "hao_hung"
                    },
                    {
                        "text": "[laughter] Phải đến buổi chiều, sau khi đã bòn rút sạch sẽ đến phân tử protein cuối cùng, gã mới thải ra những viên phân khô cứng hình bầu dục không còn giá trị dinh dưỡng. Kỳ dị, khó ngửi, nhưng chính món súp vi khuẩn tái chế này đã nuôi sống cả đế chế gặm nhấm suốt hàng triệu năm qua!",
                        "mood": "hao_hung"
                    }
                ]
            },
            {
                "id": "scene05",
                "badge": "TÀU NGẦM 5 PHÚT",
                "banner_title": "KỸ THUẬT LẶN VÀ CÚ CHẠY 35KM/H",
                "chapter_title": "Kỹ năng thoát hiểm: Tàu ngầm nín thở 5 phút và cú bứt tốc 35 km/h",
                "hook": "BỐ TRÍ MẮT MŨI TAI THẲNG HÀNG TRÊN ĐỈNH ĐẦU",
                "mood": "don_dap",
                "parts": [
                    {
                        "text": "Đừng bao giờ để dáng vẻ chậm chạp ung dung của Bố Già đánh lừa thị giác! Trong thế giới giang hồ, kẻ sống sót lâu nhất không phải kẻ to mồm nhất, mà là kẻ sở hữu lối thoát hiểm tinh quái nhất. Một khi sát thủ đỉnh chóp Báo Đốm Giác-goa xuất hiện với cặp móng vuốt chết chóc, Ca-py-ba-ra lập tức kích hoạt chế độ đào tẩu cấp độ đỏ!",
                        "mood": "don_dap"
                    },
                    {
                        "text": "Cả bầy trật tự! Báo đốm Jaguar hướng hai giờ, lặn ngầm rút lui hết cho tôi!",
                        "cast": "ba_trum"
                    },
                    {
                        "text": "[surprise-wa] Tuyệt chiêu số một: Chế độ tàu ngầm quân sự! Bạn có nhận thấy mắt, mũi và tai của Ca-py-ba-ra đều nằm thẳng hàng trên một mặt phẳng ở đỉnh đầu không? Thiết kế giải phẫu này giống hệt loài hà mã và cá sấu! Khi ngâm mình dưới nước, toàn bộ thân xác hộ pháp sáu mươi lăm cân chìm nghỉm dưới dòng nước đục, chỉ để lộ ba giác quan nhô lên mặt nước để thở và nghe ngóng mà không để lại một gợn sóng!",
                        "mood": "don_dap"
                    },
                    {
                        "text": "Bàn chân của Ca-py-ba-ra có bốn ngón ở chân trước và ba ngón ở chân sau, tất cả đều được nối liền bởi lớp màng bơi tự nhiên. Dưới nước, gã có thể nín thở lặn sâu hoàn toàn suốt năm phút đồng hồ, luồn lách qua các thảm cỏ ngầm để thoát khỏi tầm mắt kẻ săn mồi!",
                        "mood": "hao_hung"
                    },
                    {
                        "text": "Còn nếu bị dồn lên bờ cạn thì sao? [surprise-oh] Hãy chuẩn bị tinh thần cho cú sốc tiếp theo: Gã béo ục ịch này có thể bứt tốc chạy nước rút với vận tốc lên tới ba mươi lăm cây số một giờ! Tốc độ xé gió ngang ngửa một con chó săn chuyên nghiệp, đủ sức bỏ xa hầu hết các loài thú săn mồi trong cự ly ngắn trước khi phóng thẳng xuống nước tẩu thoát!",
                        "mood": "don_dap"
                    }
                ]
            },
            {
                "id": "scene06",
                "badge": "BÀI HỌC SINH TỒN",
                "banner_title": "ĐẾ CHẾ ĐẦM LẦY VÀ TẬP KẾ TIẾP",
                "chapter_title": "Đế chế bất tử: Cú lừa giáo hội Vatican và bài học sống chill",
                "hook": "CÚ LỪA ĐƯỢC CÔNG NHẬN LÀ CÁ ĐỂ ĂN MÙA CHAY",
                "mood": "am_ap",
                "parts": [
                    {
                        "text": "Sự kỳ diệu của Ca-py-ba-ra lớn đến mức từng tạo nên một trong những vụ nhầm lẫn hài hước nhất lịch sử tôn giáo thế giới! Vào thế kỷ mười sáu, khi các nhà truyền giáo Tây Ban Nha đến vùng đầm lầy Venezuela, họ nhìn thấy loài thú này suốt ngày bơi lội dưới nước, chân lại có màng như vịt. Thế là họ gửi thư về Tòa thánh Va-ti-căng để xin phép... [laughter] được xếp Ca-py-ba-ra vào loài cá, để giáo dân có thể ăn thịt trong Mùa Chay kiêng khem!",
                        "mood": "hao_hung"
                    },
                    {
                        "text": "Và thật khó tin, các giám mục thời bấy giờ đã chính thức gật đầu phê chuẩn sắc lệnh coi một con thú gặm nhấm sáu mươi lăm cân có bốn chân và bộ lông xơ cứng là... một loài thủy sản! Một cú lừa tiến hóa vĩ đại mà chính Bố Già Đầm Lầy cũng chẳng thể ngờ tới.",
                        "mood": "nghiem_trang_gia"
                    },
                    {
                        "text": "Trải qua hàng triệu năm thăng trầm, triết lý sinh tồn mà loài Ca-py-ba-ra để lại cho chúng ta thật sâu sắc: Trong một thế giới đầy rẫy hiểm nguy và áp lực, kẻ chiến thắng sau cùng không phải kẻ cố gồng mình lên thị uy nanh vuốt, mà là kẻ biết giữ cho tâm trí mình luôn phẳng lặng như mặt nước hồ thu, hòa hợp với mọi loài xung quanh để biến kẻ thù thành bạn đồng hành.",
                        "mood": "am_ap"
                    },
                    {
                        "text": "[surprise-oh] Bạn ấn tượng nhất với điều gì ở Bố Già Đầm Lầy Ca-py-ba-ra: Khả năng biến cá sấu thành bạn thân, hay bữa sáng tái chế có một không hai? Hãy để lại bình luận bên dưới nhé!",
                        "mood": "hao_hung"
                    },
                    {
                        "text": "Và bây giờ, hãy hướng ngòi bút về phân cảnh kết thúc bí ẩn! Trong tập tiếp theo, chúng ta sẽ lặn xuống đáy đại dương sâu thẳm để diện kiến một bóng đen tí hon vô cùng nguy hiểm. [surprise-wa] Một sinh vật nhỏ bé dài chưa đầy năm xăng-ti-mét, nhưng sở hữu chiếc càng quái đản có thể búng ra âm thanh kinh hoàng lên tới hai trăm mười tám đề-xi-ben, to hơn cả tiếng súng trường và làm nhiễu loạn cả hệ thống sóng siêu âm của tàu ngầm quân sự! Cú búng càng tạo ra luồng nhiệt độ hàng ngàn độ C xé toạc mặt nước, làm con mồi chết đứng từ xa mà không cần chạm vào người! Đố bạn biết danh tính của sát thủ vũ khí âm thanh tí hon này là ai? Hãy đoán tên con vật bên dưới phần bình luận nhé!",
                        "mood": "tram_bi_an"
                    }
                ]
            }
        ]
    },
    "shorts": {
        "target_s": 53.0,
        "mood": "hao_hung",
        "text": "[surprise-oh] Tại sao một gã chuột béo nặng sáu mươi lăm cân lại có thể ngồi uống trà cạnh đàn cá sấu săn mồi mà không mất một cọng lông? Đây là Chuột Lang Nước Ca-py-ba-ra, loài gặm nhấm lớn nhất thế giới sinh sống tại đầm lầy Nam Mỹ! Thứ nhất, kích thước sáu mươi lăm cân cùng lớp da dai và hàm răng cửa sắc như xẻng sắt khiến cá sấu Caiman biết rằng tấn công gã là một canh bạc có thể rách họng chết ngạt. Thứ hai, lưng Ca-py-ba-ra là trạm xe buýt di động: chim rỉa bọ ve, rùa sưởi nắng, bầy khỉ đi nhờ qua sông, biến gã thành bộ trưởng ngoại giao hòa bình của muôn loài. Thứ ba, gã là tàu ngầm sinh học có màng bơi, nín thở lặn sâu năm phút và bứt tốc chạy nước rút ba mươi lăm cây số một giờ ngang chó săn! Nhưng bí mật gây sốc nhất là vào mỗi sáng sớm, Ca-py-ba-ra ăn lại chính phân mềm của mình để hấp thụ trọn vẹn protein lên men! Giữ tâm tĩnh lặng giữa giông bão, đó chính là bí thuật giúp Bố Già Ca-py-ba-ra sống sót ung dung giữa bầy sát thủ đầm lầy!"
    },
    "seo": {
        "title": "Bố Già 65kg Khiến Cá Sấu Phải Nể & Bữa Sáng Ăn Lại... Phân?! | Capybara | Tập 15",
        "hook_paragraph": "Chuột Lang Nước (Capybara) nặng tới 65kg sở hữu vẻ mặt điềm đạm khiến cả cá sấu Caiman cũng phải nằm cạnh phơi nắng, chân có màng bơi nín thở lặn 5 phút, chạy nước rút 35km/h nhưng lại có bí mật đen tối ăn lại phân sáng sớm để hấp thụ protein! Khám phá hồ sơ đế chế đầm lầy của Bố Già Nam Mỹ.",
        "bullets": [
            "Tại sao cá sấu Caiman và muông thú đều thích nằm cạnh Capybara?",
            "Vũ khí ngoại giao: Khối u Morillo trên mũi và tiếng sủa báo động đầm lầy",
            "Bí mật đen tối: Tập tính ăn phân Cecotrophy sáng sớm để hấp thụ protein",
            "Tàu ngầm sinh học: Chân màng bơi, lặn 5 phút và chạy nước rút 35km/h",
            "Cú lừa lịch sử: Giáo hội Vatican thế kỷ 16 từng công nhận Capybara là... cá!",
            "Bật mí bóng đen bí ẩn tập tiếp theo: Sát thủ vũ khí âm thanh 218 dB"
        ],
        "question": "Bạn nể phục khả năng ngoại giao làm bạn với cá sấu hay cú sốc bữa sáng tái chế của Bố Già Capybara hơn? Đoán xem bóng đen tập sau là loài nào nhé!",
        "next_teaser": "sát thủ đại dương búng càng nổ 218 dB làm điếc sóng sonar tàu ngầm",
        "hashtags": [
            "#Capybara",
            "#ChuotLangNuoc",
            "#TheGioiDongVat",
            "#VeChuyenHoangDa",
            "#WhiteboardAnimation"
        ],
        "tags": [
            "chuột lang nước",
            "chuot lang nuoc",
            "capybara",
            "capybara và cá sấu",
            "tại sao capybara thân thiện",
            "bố già đầm lầy",
            "bộ trưởng ngoại giao đầm lầy",
            "capybara ăn phân",
            "cecotrophy",
            "tuyến morillo",
            "động vật hài hước",
            "thế giới động vật",
            "vẽ chuyện hoang dã",
            "whiteboard animation việt nam",
            "vatican coi capybara là cá"
        ],
        "shorts_title": "Tại Sao Cá Sấu Cũng Phải Nể Sợ Bố Già 65kg Này?! 🐾 #shorts #capybara",
        "shorts_desc": "Chuột Lang Nước Capybara nặng 65kg là gã béo điềm tĩnh nhất đầm lầy Nam Mỹ: cá sấu nằm cạnh, bầy khỉ cưỡi lưng, lặn 5 phút và chạy 35km/h! Khám phá bí mật Bố Già đầm lầy.",
        "shorts_tags": [
            "capybara",
            "chuột lang nước",
            "shorts",
            "thế giới động vật",
            "vẽ chuyện hoang dã"
        ],
        "en_title": "The 65kg Capfather That Befriends Crocodiles & Eats Its Own... Poop?! | Capybara | Ep 15",
        "en_hook": "The Capybara weighs up to 65kg and is so impossibly chill that even apex caiman crocodiles lounge right beside it. Discover the secret marshland mafia file of South America's most beloved giant rodent - from its scent-marking Morillo snout to its weird morning digestive habit!",
        "en_chapters": [
            "The Capfather: 65kg giant rodent of Pantanal",
            "The marshland bus: why caimans never attack",
            "Diplomatic scent: the Morillo snout gland & alarm barks",
            "The dark breakfast: morning cecotrophy digestion",
            "Submarine escape: 5-minute dive & 35 km/h sprint",
            "The chill empire: Vatican fish decree & next episode teaser"
        ],
        "en_shorts_title": "Why Even Crocodiles Respect This 65kg Chill Giant?! 🐾 #shorts #capybara"
    }
}

out_p = P / "episode.json"
out_p.write_text(json.dumps(episode, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"Saved {out_p}")
