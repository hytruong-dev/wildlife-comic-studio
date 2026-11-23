import json
from pathlib import Path

ep = {
    "episode_no": 8,
    "animal": "Chồn Gulo",
    "slug": "tap-08-chon-gulo",
    "whisper_prompt": "Chồn Gulo, Wolverine, Gulo gulo, Gấu Xám Grizzly, Chồn hôi Skunk bear, Băng tuyết Taiga, Yellowstone, Alaska, Răng hàm xoay 90 độ, Đệm chân tuyết, M3, Bất tử xứ tuyết",
    "display_fix": {
        "mười lăm ki-lô-gam": "15kg",
        "hai mươi lăm ki-lô-gam": "25kg",
        "ba trăm ki-lô-gam": "300kg",
        "bốn trăm ki-lô-gam": "400kg",
        "sáu mươi lăm xăng-ti-mét": "65cm",
        "một trăm lẻ năm xăng-ti-mét": "105cm",
        "âm bốn mươi độ C": "-40°C",
        "âm năm mươi độ C": "-50°C",
        "chín mươi độ": "90°",
        "sáu mét": "6m",
        "hai mươi mét": "20m",
        "bảy mươi cây số": "70km",
        "bốn mươi lăm dặm": "45 dặm",
        "chín mươi phút": "90 phút",
        "ba ngàn một trăm mét": "3.100m",
        "một ngàn năm trăm mét": "1.500m",
        "một ngàn năm trăm cây số vuông": "1.500km²",
        "một ngàn cây số vuông": "1.000km²",
        "hai mươi lần": "20 lần",
        "mười lần": "10 lần",
        "ba con sói": "3 con sói",
        "năm mươi mét": "50m",
        "ba ngày": "3 ngày",
        "hai mươi năm": "20 năm",
        "hai mươi tuổi": "20 tuổi",
        "Gu-lô": "Gulo",
        "Uân-vơ-rin": "Wolverine",
        "Gờ-rít-zli": "Grizzly",
        "Tai-ga": "Taiga",
        "Yên-lâu-xtôn": "Yellowstone",
        "Mác-vơn": "Marvel",
        "X-kâng Bia": "Skunk Bear",
        "Et-xki-mô": "Eskimo",
        "A-lát-xka": "Alaska",
        "Mông-ta-na": "Montana",
        "Mông Cờ-li-vơ-lân": "Mount Cleveland",
        "M-ba": "M3",
        "hai mươi bốn trên bảy": "24/7",
        "A-T-K": "ATK",
        "S-P-D": "SPD",
        "D-E-F": "DEF",
        "H-P": "HP"
    },
    "voice": {
        "speed": 1.05,
        "steps": 32,
        "tempo_long": 1.10,
        "tempo_shorts_min": 1.10
    },
    "longform": {
        "scenes": [
            {
                "id": "scene01",
                "chapter_title": "Gã Chí Phèo xứ tuyết dám cướp mồi của gấu xám",
                "hook": "Kẻ điên rồ nhất vùng băng giá Bắc Cực",
                "parts": [
                    "[surprise-oh] Nếu bạn nghĩ chúa tể vùng băng tuyết phương Bắc là loài gấu trắng khổng lồ hay những đàn sói xám hung hãn, thì bạn vừa bỏ qua một kẻ điên khét tiếng nhất thế giới hoang dã! Một sinh vật thân hình cũn cỡn như con gấu bông lai chồn hương, nặng vỏn vẹn mười lăm ki-lô-gam, nhưng sở hữu lá gan to hơn cả ngọn núi lửa! Hãy làm quen với Chồn Gu-lô, hay còn gọi là Uân-vơ-rin, nhân vật nguyên mẫu đã truyền cảm hứng cho siêu anh hùng Người Sói móng vuốt kim loại của hãng Mác-vơn! Nhìn bề ngoài, chú ta lùn tịt, bốn chân ngắn củn, dáng đi lạch bạch lắc lư trông cực kỳ cù lần. Thế nhưng, ẩn sau ngoại hình lù khù đó là bản tính hung dữ, cục súc và liều lĩnh đến mức điên rồ! [laughter] Kẻ thù thấy nó thì phát hoảng, thợ săn nghe tên nó thì lắc đầu ngán ngẩm, còn các loài thú ăn thịt đầu bảng thì chỉ ước gì chưa từng chạm mặt gã giang hồ này trong đời!",
                    "Các nhà động vật học thường gọi Chồn Gu-lô là người anh em xứ tuyết của Lửng Mật. Nếu Lửng Mật là Chí Phèo của thảo nguyên châu Phi nóng rẫy, thì Chồn Gu-lô chính là trùm giang hồ bảo kê cả vùng rừng Tai-ga lạnh thấu xương! Lý do đơn giản: chú ta không hề có khái niệm sợ hãi trong từ điển sống! Dù đối thủ có là một con gấu xám Gờ-rít-zli nặng ba trăm ki-lô-gam hay cả một đàn sói đói đang vây quanh bữa ăn, gã lùn này vẫn sẵn sàng xông thẳng vào cướp trắng miếng thịt trước mũi đối phương! [laughter] Một gã tí hon mang dũng khí của một con quái vật không thể thuần hóa!",
                    "Chưa hết đâu, gã này còn là cơn ác mộng truyền kiếp của những người thợ săn và thợ bẫy thú rừng phương Bắc! Mỗi khi thợ săn dựng lều và đặt bẫy gỗ kiên cố trong rừng, Chồn Gu-lô sẽ lén đi theo sau, dùng răng cắn nát bẫy, cuỗm sạch thịt mồi, rồi đột nhập vào tận kho lều ăn sạch lương thực! Đỉnh điểm của sự trêu ngươi là trước khi bỏ đi, chú ta còn phun một bãi xạ hôi nồng nặc lên toàn bộ số đồ đạc còn lại coi như lời chào tạm biệt! [laughter] Thợ săn mở cửa lều chỉ biết ôm đầu khóc thét vì vừa mất của vừa phải ngửi mùi hôi suốt cả mùa đông!"
                ]
            },
            {
                "id": "scene02",
                "chapter_title": "Bảng chỉ số RPG — Lỗi game của tạo hóa xứ lạnh",
                "hook": "Khi thiên nhiên quên cài thanh tụt máu do bão tuyết",
                "parts": [
                    "[surprise-wa] Nếu đưa Chồn Gu-lô vào một tựa game nhập vai sinh tồn, chắc chắn nhân vật này sẽ bị gắn mác là kẻ gian lận chỉ số một cách trắng trợn! Hãy cùng bóc tách bảng chỉ số sinh tồn dị biệt của gã võ sĩ xứ tuyết: Sức mạnh tấn công A-T-K: chín mươi điểm! Đừng để thân hình dài sáu mươi lăm xăng-ti-mét đánh lừa bạn; lực cắn của nó đủ sức bẻ gãy xương đùi đông cứng của nai sừng tấm trong một tích tắc! Chỉ số phòng thủ D-E-F: chín mươi lăm điểm! Da của nó dày như tấm thảm bọc thép, lớp lông kỵ nước không bao giờ bị đóng băng dù nhiệt độ có hạ xuống âm bốn mươi độ C! Và đáng sợ nhất là chỉ số thể lực bền bỉ: chạm nóc tuyệt đối một ngàn điểm không đáy! Nó có thể chạy liên tục bảy mươi cây số qua các rặng núi dốc đứng ngập tuyết mà nhịp tim vẫn đập đều như một cỗ máy vĩnh cửu!",
                    "Để bạn dễ hình dung sự vi diệu của bộ khung cơ thể này: Chồn Gu-lô sở hữu bốn bàn chân bè cực rộng, có màng da và móng vuốt sắc nhọn hoạt động y hệt một đôi ủng trượt tuyết chuyên dụng! Trong khi những con mồi nặng nề như tuần lộc hay nai sừng tấm bị sa lầy tuyết ngập đến tận bụng và bất lực giãy giụa, gã lùn này lại lướt đi trên mặt tuyết mềm nhẹ nhàng như một nghệ sĩ trượt băng nghệ thuật! [laughter] Thế là một cuộc rượt đuổi không cân sức biến thành trò đùa: kẻ khổng lồ thì kiệt sức vì lún tuyết, còn kẻ tí hon thì thong thả chạy vòng quanh đợi con mồi hết pin rồi mới nhảy vào kết liễu!",
                    "Chưa hết đâu, cơ bắp cổ và hàm của Chồn Gu-lô phát triển khủng khiếp đến mức nó có thể tha một chiếc đầu nai nặng gấp đôi trọng lượng cơ thể mình leo phăng phăng lên vách núi dựng đứng! Cứ như thể một cậu bé mười tuổi nâng bổng chiếc xe máy phân khối lớn rồi chạy bộ lên đỉnh dốc vậy! [laughter] Thật là một thiết kế vật lý thách thức mọi định luật công thái học của tự nhiên!"
                ]
            },
            {
                "id": "scene03",
                "chapter_title": "Chiếc răng hàm xoay 90 độ & Tuyến xạ Skunk Bear",
                "hook": "Cỗ máy nghiền nát xương đá và vũ khí hóa học hủy diệt",
                "parts": [
                    "[surprise-oh] Nhưng vũ khí cơ học quái đản nhất của Chồn Gu-lô nằm ở bên trong khoang miệng của nó! Các nhà giải phẫu học từng kinh ngạc khi phát hiện chiếc răng hàm trên đặc biệt của nó được xoay ngang chín mươi độ hướng hẳn vào phía trong vòm họng! Chiếc răng này hoạt động như một chiếc kìm cộng lực bẻ sắt: nó cho phép Chồn Gu-lô ngoạm chặt và nghiền nát những khúc xương lớn đã bị đông cứng thành đá tảng ở âm năm mươi độ C! [surprise-ah] Vào mùa đông khắc nghiệt khi thức ăn khan hiếm cùng cực, tất cả các loài dã thú khác đều phải bỏ lại những bộ xương đóng băng vì sợ mẻ răng, thì Chồn Gu-lô ung dung bước tới, bẻ vụn từng mẩu xương và hút sạch tủy béo giàu dinh dưỡng bên trong! Đối với nó, xương đông lạnh chẳng khác nào những que kem đá bùi ngậy giữa mùa đông!",
                    "[surprise-wa] Bên cạnh chiếc răng kìm sắt, gã này còn sở hữu một vũ khí sinh học kinh hoàng khiến người ta đặt cho nó biệt danh Chồn Gấu Hôi, tức X-kâng Bia! Ngay dưới đuôi của nó là một tuyến xạ mùi cực nồng, có khả năng phun ra một hợp chất hóa học bốc mùi khủng khiếp! Mùi hôi này là sự kết hợp kinh dị giữa mùi trứng thối lưu huỳnh, mắm tôm ủ lâu ngày và mùi tất ướt của một đội bóng sau trận chung kết! [laughter] Khi cướp được thức ăn hoặc giấu mồi, chú ta sẽ lập tức tưới đẫm dung dịch hôi hám này lên miếng thịt. Kết quả là chẳng có con thú săn mồi nào, dù đói đến mấy, dám hạ mình chạm mồm vào đống thức ăn thối hoắc đó nữa!",
                    "Ngoài ra, khứu giác của Chồn Gu-lô nhạy bén đến mức khó tin: nó có thể đánh hơi thấy xác một con nai bị tuyết lở chôn vùi sâu tới sáu mét dưới lòng đất! Sau đó, nó dùng bốn móng vuốt cào bới như một chiếc máy xúc mini, đào xuyên qua lớp băng tuyết dày để lôi bữa ăn miễn phí lên thưởng thức! [laughter] Đúng là một chiếc ra-đa sống của thần chết vùng tuyết trắng!",
                    "Đặc biệt, bộ lông của Chồn Gu-lô là một kiệt tác cách nhiệt tối thượng của tự nhiên! Cấu trúc sợi lông rỗng và phủ lớp dầu kỵ nước hoàn hảo, khiến sương giá và hơi ẩm không thể bám dính hay đông đá. Người thợ săn bản địa Et-xki-mô từ ngàn xưa đã xem lông Chồn Gu-lô là thứ đắt giá nhất để may viền mũ trùm đầu mùa đông: khi thở ra ở âm bốn mươi độ C, hơi thở của con người sẽ lập tức đóng băng thành dải dao cạo sắc nhọn cứa vào mặt nếu dùng lông thú thường, nhưng với lông Chồn Gu-lô, bạn chỉ cần gạt nhẹ tay là toàn bộ tuyết đá rơi sạch như bụi! [laughter] Một chiếc áo giáp chống băng giá mà không hãng thời trang nào trên thế giới có thể bắt chước!"
                ]
            },
            {
                "id": "scene04",
                "chapter_title": "Gót chân A-sin — Quái vật dạ dày & Cuộc sống cô độc đến lập dị",
                "hook": "Cái bụng không đáy và gã độc thân khó tính nhất hành tinh",
                "parts": [
                    "[sigh] Nghe đến đây, bạn hẳn đang nghĩ Chồn Gu-lô là một cỗ máy sinh tồn hoàn hảo không một vết xước đúng không? Nhưng tạo hóa luôn cài cắm những trò hề trớ trêu! Tên khoa học của nó, Gu-lô Gu-lô, trong tiếng La-tinh có nghĩa đen là Kẻ Phàm Ăn! Tốc độ trao đổi chất của nó nhanh đến mức điên cuồng để duy trì thân nhiệt giữa cái lạnh âm bốn mươi độ C, biến nó thành một kẻ nô lệ của dạ dày! Nó phải ăn liên tục và thèm ăn đến phát rồ! Để không bị chết đói, nó biến cả khu rừng tuyết thành một chuỗi tủ lạnh siêu thị: bất cứ con mồi nào ăn không hết, nó xé nhỏ ra rồi chôn sâu vào các hốc băng tuyết để đông lạnh dự trữ! [laughter] Nhưng chính cái nết ăn như hổ đó khiến nó luôn trong trạng thái cáu kỉnh, gắt gỏng như người bị hạ đường huyết suốt hai mươi bốn trên bảy!",
                    "Và điểm yếu bi hài nhất của Chồn Gu-lô chính là bản tính cô độc đến mức cực đoan! Một con đực có thể cai quản lãnh thổ rộng tới một ngàn năm trăm cây số vuông, tức là rộng bằng cả một thành phố lớn, và nó không bao giờ chấp nhận bất kỳ sinh vật nào lai vãng! Ngay cả với đồng loại cùng loài, khuôn mặt chú ta lúc nào cũng nhăn nhó, cau có như mất sổ gạo! Chúng chỉ gặp nhau đúng vài ngày ngắn ngủi trong năm để duy trì nòi giống, rồi lập tức quay lưng bỏ chạy như thể không muốn nhìn mặt nhau thêm một giây nào nữa! [laughter] Một chiến binh vô địch thiên hạ, nhưng cả cuộc đời chỉ lủi thủi độc hành giữa rừng tuyết hoang vu không một bóng bạn bè!",
                    "Nhưng bạn có biết điều trớ trêu nhất của gã giang hồ này là gì không? Dù cả đời liều mạng đánh nhau với gấu và sói để bảo vệ miếng ăn, nhưng Chồn Gu-lô lại cực kỳ cưng chiều đàn con của mình! Chồn bố thỉnh thoảng vẫn quay lại thăm đàn con nhỏ, dẫn chúng đi săn và dạy chúng kỹ năng bẻ xương tuyết. Nghĩa là ngoài mặt thì cáu kỉnh cục súc với cả thế giới, nhưng bên trong lại là một người cha mẫu mực bí mật! [laughter] Đúng là giang hồ xứ tuyết cũng có lúc yếu lòng!"
                ]
            },
            {
                "id": "scene05",
                "chapter_title": "Những trận chiến có thật — Một mình đuổi cả gấu lẫn sói",
                "hook": "Khi gã tí hon 15kg bắt kẻ khổng lồ 300kg phải nhượng bộ",
                "parts": [
                    "[surprise-oh] Những giai thoại về độ liều của Chồn Gu-lô hoàn toàn được ghi lại bằng máy quay của các nhà sinh vật học thực địa! Tại Vườn quốc gia Yên-lâu-xtôn ở Mỹ, các nhà nghiên cứu từng ghi nhận một thước phim chấn động: một con Chồn Gu-lô nặng chưa đầy mười lăm ki-lô-gam dám hiên ngang lao thẳng vào một xác nai mà một con Gấu Xám Gờ-rít-zli nặng ba trăm ki-lô-gam đang thưởng thức! Chú chồn nhỏ không hề lùi bước, xù toàn bộ lông lên, nhe hàm răng kìm sắt gầm gừ những tiếng rít chói tai và lao tới đớp thẳng vào mõm gấu khổng lồ! [surprise-ah] Bị tấn công bất ngờ bởi một kẻ điên không sợ chết kèm theo mùi hôi nồng nặc bốc lên, con gấu xám khổng lồ nặng gấp hai mươi lần chỉ biết gầm gừ khó chịu rồi lùi lũi bỏ đi! [laughter] Đúng là một minh chứng sống cho câu nói: Kẻ mạnh sợ kẻ liều, kẻ liều sợ kẻ không cần mạng sống!",
                    "Chưa dừng lại ở đó, tại vùng lãnh nguyên A-lát-xka, người ta từng chứng kiến cảnh một con Chồn Gu-lô đơn độc đánh bật ba con sói xám to lớn khỏi miếng mồi! Sói xám nổi tiếng với chiến thuật bầy đàn thông minh, nhưng đứng trước một gã lùn vừa cắn đau, vừa hôi thối, lại vừa lăn xả như cảm tử quân, bầy sói đành ngậm ngùi rút lui vì nhận ra rằng: Dù có hạ được nó thì bản thân cũng mang thương tật nặng, hoàn toàn không đáng để đánh đổi giữa mùa đông khắc nghiệt!",
                    "Một nghiên cứu nổi tiếng khác theo dõi chú chồn mang mã số M-ba tại bang Mông-ta-na đã khiến giới khoa học ngả mũ: trong vòng chín mươi phút, chú ta đã leo thẳng đứng lên đỉnh núi Mông Cờ-li-vơ-lân cao hơn ba ngàn một trăm mét phủ đầy băng tuyết dựng đứng! Các vận động viên leo núi chuyên nghiệp phải mất cả ngày trời với đầy đủ dây bảo hiểm và rìu băng, còn chú ta chỉ coi đó là một buổi đi dạo buổi sáng trước khi ăn điểm tâm! [laughter] Thể lực của gã này đúng là ngoài hành tinh!"
                ]
            },
            {
                "id": "scene06",
                "chapter_title": "Bài học sinh tồn từ Chồn Gulo & Teaser tập sau",
                "hook": "Bản lĩnh không đo bằng kích thước cơ thể",
                "parts": [
                    "Nhìn lại hành trình sinh tồn của Chồn Gu-lô giữa vùng địa đầu băng giá, chúng ta nhận ra một bài học sâu sắc: Kích thước cơ thể hay hoàn cảnh xuất phát điểm chưa bao giờ là yếu tố quyết định giới hạn của bạn! Sinh ra với thân hình nhỏ bé giữa một vùng đất ngập tràn những kẻ săn mồi khổng lồ, Chồn Gu-lô không chọn cách ẩn nấp sợ sệt, mà tự tôi luyện cho mình sức chịu đựng phi thường, lòng dũng cảm thép và sự bền bỉ không thể bị bẻ gãy! Nó biến cái lạnh chết người thành chiếc tủ lạnh bảo quản thức ăn, và biến sự nhỏ bé thành vũ khí cơ động lướt trên tuyết! Trong cuộc sống cũng vậy: Khi bạn dám đương đầu với những nghịch cảnh lớn hơn bản thân gấp nhiều lần và kiên trì bước tiếp mỗi ngày, cả thế giới sẽ phải nghiêng mình nhường bước cho bạn!",
                    "Nếu được chọn giữa sức mạnh thể lực bền bỉ leo núi không biết mệt của Chồn Gu-lô và cú đấm nóng ngang Mặt Trời của Tôm Tít ở tập trước, bạn sẽ chọn siêu năng lực nào để sinh tồn? Hãy để lại bình luận bên dưới cho chúng mình biết nhé! Đừng quên bấm Đăng ký kênh và chuông thông báo để không bỏ lỡ Tập chín: Chim Cánh Cụt — Đằng sau dáng đi lạch bạch dễ thương là những màn giao dịch đen tối nhất Nam Cực! Hẹn gặp lại các bạn trong cuộc phiêu lưu tiếp theo!"
                ]
            }
        ]
    },
    "shorts": {
        "target_s": 53.0,
        "text": "[surprise-oh] Nặng vỏn vẹn mười lăm ki-lô-gam nhưng dám lao vào cướp mồi của một con Gấu Xám nặng ba trăm ki-lô-gam! Kẻ điên rồ bậc nhất xứ tuyết phương Bắc chính là Chồn Gu-lô, hay còn gọi là Uân-vơ-rin! Với bốn bàn chân bè rộng như đôi ủng trượt tuyết, gã tí hon này lướt nhẹ trên tuyết mềm trong khi những con mồi khổng lồ sa lầy bất lực! Bộ lông kỵ nước không bao giờ đông đá ở âm bốn mươi độ C, và chiếc răng hàm trên xoay ngang chín mươi độ hoạt động như kìm cộng lực bẻ vụn cả xương đá đông lạnh! [surprise-wa] Nó có thể chạy liên tục bảy mươi cây số qua vách núi dựng đứng, và khi bị bao vây, nó sẽ phun ra luồng mùi hôi thối kinh hoàng khiến cả bầy sói cũng phải ôm mũi bỏ chạy! [laughter] Nhưng nghịch lý hài hước là gã chiến binh bất bại này lại cô độc đến phát khóc, cả đời chỉ lủi thủi một mình vì tính tình quá cộc cằn! [question-ah] Bạn muốn biết chú ta đã đuổi gấu xám cướp mồi như thế nào? Bấm xem ngay video dài Tập tám bên dưới kênh nhé! [surprise-oh] Nặng vỏn vẹn mười lăm ki-lô-gam nhưng dám lao vào cướp mồi của một con Gấu Xám nặng ba trăm ki-lô-gam!"
    },
    "seo": {
        "title": "Nặng 15kg Dám Cướp Mồi Của Cả Đàn Sói Và Gấu Xám?! | Chồn Gulo | Tập 8",
        "hook_paragraph": "Chồn Gulo (Wolverine) chỉ nặng 15kg nhưng sở hữu lá gan to nhất thế giới động vật: răng hàm xoay 90 độ nghiền nát xương đông lạnh, chân như ủng trượt tuyết và dám đơn độc lao vào cướp mồi của Gấu Xám 300kg! Khám phá bí mật sinh tồn của chiến binh bất tử xứ tuyết.",
        "bullets": [
            "Chiếc răng hàm carnassial xoay 90 độ bẻ vụn xương đông cứng ở -50°C",
            "Bàn chân cấu trúc ủng trượt tuyết snowshoes lướt trên tuyết lún",
            "Tuyến xạ hôi Skunk Bear khiến gấu xám và bầy sói bỏ chạy ngán ngẩm",
            "Sức bền quái vật: chạy 70km/ngày và leo đỉnh núi tuyết 3.100m trong 90 phút"
        ],
        "question": "Nếu phải đối đầu giữa Chồn Gulo 15kg liều mạng và Gấu Xám 300kg trên núi tuyết, bạn sẽ chọn ai? Bình luận bên dưới nhé!",
        "next_teaser": "Chim Cánh Cụt — Đằng sau dáng đi lạch bạch dễ thương là những màn giao dịch đen tối nhất Nam Cực",
        "hashtags": [
            "#ChonGulo",
            "#Wolverine",
            "#TheGioiDongVat",
            "#VeChuyenHoangDa",
            "#KhoaHoc"
        ],
        "tags": [
            "chồn gulo",
            "chon gulo",
            "wolverine",
            "gulo gulo",
            "người sói ngoài đời thực",
            "chồn gấu hôi",
            "skunk bear",
            "gấu xám grizzly",
            "thế giới động vật",
            "động vật kỳ lạ",
            "vẽ chuyện hoang dã",
            "whiteboard animation",
            "khoa học thú vị",
            "băng tuyết bắc cực",
            "sinh tồn hoang dã"
        ],
        "shorts_title": "Nặng 15kg Đuổi Cả Gấu Xám 300kg Khỏi Bữa Ăn?! ❄️ #shorts #chongulo",
        "shorts_desc": "Chồn Gulo (Wolverine) chỉ nặng 15kg nhưng dám cướp mồi của gấu xám 300kg và cả bầy sói nhờ chiếc răng hàm xoay 90 độ bẻ xương đông lạnh! ❄️\n👉 Xem bản đầy đủ vụ đại chiến xứ tuyết — video Tập 8 trên kênh Vẽ Chuyện Hoang Dã.\n\n#shorts #ChonGulo #Wolverine #TheGioiDongVat #VeChuyenHoangDa #KhoaHoc",
        "shorts_tags": [
            "chồn gulo",
            "wolverine",
            "gulo",
            "shorts",
            "thế giới động vật",
            "vẽ chuyện hoang dã",
            "động vật kỳ lạ"
        ]
    }
}

p = Path("projects/tap-08-chon-gulo/episode.json")
p.write_text(json.dumps(ep, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Wrote {p}")
