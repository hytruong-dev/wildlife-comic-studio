import json
from pathlib import Path

ep37_data = {
    "title": "Tập 37: Lạc Đà Sa Mạc — Cỗ Máy Lọc Nước Siêu Cấp 50°C",
    "animal": "Lạc Đà Sa Mạc",
    "format": "F1",
    "persona": "bac_si",
    "nickname": "Cỗ Máy Lọc Nước Sa Mạc",
    "voice": {
        "tempo_long": 1.11,
        "tempo_shorts_min": 1.12,
        "min_long_s": 510,
        "max_long_s": 900
    },
    "whisper_prompt": "Lạc Đà Sa Mạc, Camelus dromedarius, Cỗ Máy Lọc Nước Sa Mạc, bướu mỡ, hồng cầu oval, siêu lọc thận, 50 độ C, 200 lít nước",
    "display_fix": {
        "Tập ba mươi bảy": "Tập 37",
        "Tập ba mươi tám": "Tập 38",
        "năm mươi độ C": "50°C",
        "bốn mươi độ C": "40°C",
        "ba mươi độ C": "30°C",
        "bốn mươi mốt độ C": "41°C",
        "ba mươi bốn độ C": "34°C",
        "hai trăm lít nước": "200 lít nước",
        "một trăm ba mươi lít nước": "130 lít nước",
        "mười lăm phút": "15 phút",
        "ba phút": "3 phút",
        "ba mươi ngày": "30 ngày",
        "bốn mươi ngày": "40 ngày",
        "hai tuần": "2 tuần",
        "hai mươi lăm phần trăm": "25%",
        "ba mươi phần trăm": "30%",
        "bốn mươi phần trăm": "40%",
        "hai trăm bốn mươi phần trăm": "240%",
        "tám mươi kilôgam": "80 kg",
        "bốn mươi kilôgam": "40 kg",
        "năm trăm kilôgam": "500 kg",
        "hai ngàn": "2.000",
        "một ngàn dặm": "1.000 dặm",
        "hai mươi bốn giờ": "24 giờ",
        "thế kỷ hai mươi mốt": "thế kỷ 21",
        "hàng triệu năm": "hàng triệu năm",
        "triệu năm": "triệu năm",
        "Camelus": "Camelus",
        "dromedarius": "dromedarius",
        "NASA": "NASA"
    },
    "longform": {
        "scenes": [
            {
                "id": "scene01",
                "badge": "CA CẤP CỨU ĐẶC BIỆT",
                "chapter_title": "Nhập viện cấp cứu: Bài toán sốc nhiệt và mất nước năm mươi độ C",
                "hook": "Bệnh nhân lạc đà bình thản bước qua bão cát tử thần",
                "mood": "hao_hung",
                "parts": [
                    {
                        "speaker": "host",
                        "mood": "hao_hung",
                        "text": "Chào mừng các y bác sĩ, các điều dưỡng viên và toàn thể thực tập sinh bước vào Ca trực cấp cứu đặc biệt của Bệnh viện Dã chiến Sa Mạc Sahara! [laughter] Hôm nay, chúng ta vừa tiếp nhận một bệnh nhân vô cùng kỳ lạ và bất quy tắc. Một đối tượng lang thang giữa chảo lửa năm mươi độ C, cát bỏng rát chân, không một giọt nước uống suốt hai tuần ròng rã, nhưng khi bước vào phòng khám, mạch đập vẫn đều đặn, huyết áp ổn định tuyệt đối và ánh mắt thì thảnh thơi nhai cỏ khô như thể đang đi nghỉ dưỡng tại bờ biển!"
                    },
                    {
                        "speaker": "host",
                        "mood": "don_dap",
                        "text": "Đối tượng trên bàn hội chẩn của chúng ta hôm nay mang tên khoa học Camelus dromedarius, nhưng trong toàn bộ giới y khoa tự nhiên, chúng tôi gọi nó bằng một mật danh đầy kính nể: Cỗ Máy Lọc Nước Sa Mạc! Nếu một con người bình thường rơi vào hoàn cảnh này, cơ thể chúng ta sẽ nhanh chóng rơi vào trạng thái sốc nhiệt cấp độ bốn, máu đông đặc lại như thạch, suy đa tạng và tử vong chỉ sau chưa đầy bốn mươi tám giờ đồng hồ!"
                    },
                    {
                        "speaker": "cameo",
                        "mood": "surprise-oh",
                        "text": "[surprise-oh] Báo cáo Bác sĩ trưởng khoa, chỉ số sinh tồn của bệnh nhân ghi nhận mất nước vượt ngưỡng hai mươi lăm phần trăm trọng lượng cơ thể mà không hề có dấu hiệu trụy tim mạch!"
                    },
                    {
                        "speaker": "host",
                        "mood": "tram_bi_an",
                        "text": "Báo cáo rất chính xác thưa y tá trưởng! Đối với cơ thể người, chỉ cần mất mười lăm phần trăm lượng nước trong cơ thể là tim đã ngừng đập vì thể tích máu sụt giảm nghiêm trọng. Thế nhưng Cỗ Máy Lọc Nước Sa Mạc có thể mất tới ba mươi phần trăm, thậm chí bốn mươi phần trăm lượng nước trong cơ thể mà vẫn bước đi hiên ngang vượt qua những cồn cát bỏng cháy hàng ngàn cây số!"
                    },
                    {
                        "speaker": "host",
                        "mood": "hao_hung",
                        "text": "Vậy đâu là những vũ khí y sinh học tối mật giúp sinh vật này thách thức mọi định luật sinh lý học truyền thống? Mời toàn thể hội đồng bác sĩ mở tập hồ sơ bệnh án số một để cùng tôi bóc tách phép màu giải phẫu đầu tiên!"
                    }
                ]
            },
            {
                "id": "scene02",
                "badge": "BỆNH ÁN SỐ 1",
                "chapter_title": "Bệnh án số 1: Chiếc bướu mỡ năng lượng chứ không phải túi nước",
                "hook": "Giải mã lầm tưởng kinh điển về kho chứa nước trên lưng",
                "mood": "hao_hung",
                "parts": [
                    {
                        "speaker": "host",
                        "mood": "hao_hung",
                        "text": "Hãy bắt đầu với chẩn đoán sai lầm phổ biến nhất trong lịch sử nhân loại: Chiếc bướu khổng lồ trên lưng lạc đà! Hàng triệu người từ xưa đến nay vẫn ngây thơ tin rằng bên trong chiếc bướu đó là một bồn chứa nước di động khổng lồ, nơi lạc đà tích trữ hàng chục lít nước tinh khiết để uống dần khi khát. [laughter] Nếu bác sĩ nào chẩn đoán như vậy, tôi xin phép thu hồi chứng chỉ hành nghề ngay lập tức!"
                    },
                    {
                        "speaker": "host",
                        "mood": "tram_bi_an",
                        "text": "Dưới lát cắt chụp cộng hưởng từ và sinh thiết giải phẫu, chiếc bướu này không chứa một giọt nước lỏng nào cả! Toàn bộ chiếc bướu nặng tới bốn mươi kilôgam, thậm chí tám mươi kilôgam ở những con đực trưởng thành, là một khối mỡ đậm đặc tinh khiết! Đây là một kho dự trữ năng lượng sinh hóa siêu cô đặc giúp Cỗ Máy Lọc Nước Sa Mạc sinh tồn suốt cả tháng trời không cần ăn uống."
                    },
                    {
                        "speaker": "cameo",
                        "mood": "surprise-oh",
                        "text": "[surprise-oh] Ủa Bác sĩ ơi, vậy tại sao mỡ lại tập trung hết lên lưng mà không phân bố đều khắp cơ thể như động vật khác?"
                    },
                    {
                        "speaker": "host",
                        "mood": "hao_hung",
                        "text": "Một câu hỏi chẩn đoán cực kỳ thông minh thưa bác sĩ nội trú! Nếu lớp mỡ dày cộp đó phân bố đều dưới da như loài gấu bắc cực hay cá voi sát thủ, cơ thể lạc đà sẽ bị bọc kín trong một chiếc áo phao cách nhiệt dày cộp. Dưới cái nắng năm mươi độ C của sa mạc, nhiệt lượng bên trong cơ thể sẽ không thể thoát ra ngoài và lạc đà sẽ bị nấu chín từ bên trong chỉ sau vài giờ!"
                    },
                    {
                        "speaker": "host",
                        "mood": "tram_bi_an",
                        "text": "Bằng cách gom toàn bộ lượng mỡ cách nhiệt tập trung duy nhất lên đỉnh lưng, chiếc bướu đóng vai trò như một chiếc dù che nắng tự nhiên, hấp thụ ánh nắng mặt trời rọi thẳng từ trên cao xuống, trong khi toàn bộ phần cơ thể còn lại hoàn toàn không có mỡ dưới da, cho phép nhiệt lượng tỏa thẳng ra môi trường xung quanh một cách tối đa!"
                    }
                ]
            },
            {
                "id": "scene03",
                "badge": "BỆNH ÁN SỐ 2",
                "chapter_title": "Bệnh án số 2: Tế bào hồng cầu hình oval co giãn vô hạn",
                "hook": "Tuyệt tác tế bào học chống vỡ tan và chống đông máu",
                "mood": "hao_hung",
                "parts": [
                    {
                        "speaker": "host",
                        "mood": "hao_hung",
                        "text": "Bây giờ, xin mời các chuyên gia huyết học bước vào phòng xét nghiệm tế bào học, nơi cất giữ bí mật y sinh tinh xảo nhất của Cỗ Máy Lọc Nước Sa Mạc: Những tế bào hồng cầu hình oval kỳ dị! Ở toàn bộ các loài động vật có vú khác, bao gồm cả con người, tế bào hồng cầu luôn có hình đĩa lõm hai mặt tròn trịa. Khi chúng ta mất nước nặng, máu trở nên đặc quánh và các tế bào hồng cầu hình tròn sẽ bị mắc kẹt tại các mao mạch nhỏ hẹp, gây tắc nghẽn tuần hoàn và dẫn đến tử vong."
                    },
                    {
                        "speaker": "host",
                        "mood": "don_dap",
                        "text": "Thế nhưng hồng cầu của lạc đà lại có hình oval bầu dục thuôn dài! Cấu trúc khí động học đặc biệt này cho phép chúng trượt lướt qua các mao mạch siêu nhỏ một cách trơn tru ngay cả khi máu của lạc đà đã đặc quánh lại như si-rô vì mất nước kéo dài suốt nhiều ngày!"
                    },
                    {
                        "speaker": "cameo",
                        "mood": "surprise-oh",
                        "text": "[surprise-oh] Thưa Giáo sư, khi tìm thấy nguồn nước, bệnh nhân có thể uống một lượng nước khổng lồ trong tích tắc đúng không ạ?"
                    },
                    {
                        "speaker": "host",
                        "mood": "hao_hung",
                        "text": "Chính xác là một kỳ tích tiếp nước ngoạn mục! Khi tìm thấy một vũng nước hay ốc đảo, Cỗ Máy Lọc Nước Sa Mạc có thể nốc cạn một trăm ba mươi lít nước, thậm chí hai trăm lít nước chỉ trong vòng chưa đầy mười lăm phút! [laughter] Nếu là người bình thường uống ngần ấy nước, hiện tượng ngộ độc nước sẽ xảy ra tức khắc: Áp suất thẩm thấu tụt giảm khiến các tế bào hồng cầu tròn vỡ tung hàng loạt và tử vong ngay tại chỗ!"
                    },
                    {
                        "speaker": "host",
                        "mood": "tram_bi_an",
                        "text": "Nhưng màng tế bào hồng cầu hình oval của lạc đà có khả năng co giãn phi thường: Chúng có thể phồng to gấp hai trăm bốn mươi phần trăm thể tích ban đầu mà không hề bị vỡ! Chúng nở ra như những quả bóng bay co giãn vô hạn, nhẹ nhàng hấp thụ toàn bộ lượng nước khổng lồ đó vào hệ tuần hoàn một cách an toàn tuyệt đối!"
                    }
                ]
            },
            {
                "id": "scene04",
                "badge": "BỆNH ÁN SỐ 3",
                "chapter_title": "Bệnh án số 3: Quả thận siêu lọc cô đặc nước tiểu thành si-rô",
                "hook": "Hệ thống tái hấp thu nước hiệu suất chín mươi chín phần trăm",
                "mood": "hao_hung",
                "parts": [
                    {
                        "speaker": "host",
                        "mood": "hao_hung",
                        "text": "Tiếp theo, xin mời hội đồng kiểm tra hệ thống cơ quan nội tạng đắt giá nhất của bệnh nhân: Đôi quả thận siêu lọc! Khi nước là thứ quý hơn vàng ròng giữa sa mạc, việc bài tiết lãng phí dù chỉ một giọt nước cũng đồng nghĩa với bản án tử hình. Thận của Cỗ Máy Lọc Nước Sa Mạc sở hữu quai Henle dài gấp nhiều lần so với các loài động vật thông thường, tạo ra một gradient nồng độ thẩm thấu cực kỳ khủng khiếp."
                    },
                    {
                        "speaker": "host",
                        "mood": "tram_bi_an",
                        "text": "Hệ thống ống thận này vắt kiệt từng phân tử nước từ dịch lọc trước khi bài tiết ra ngoài. Kết quả là nước tiểu của lạc đà cô đặc đến mức sánh đặc như si-rô đặc quẹt, có nồng độ muối và khoáng chất cao gấp đôi nước biển tự nhiên! [laughter] Không một loài động vật có vú nào có thể bài xuất nước tiểu đậm đặc đến mức đó mà không bị suy thận cấp tính!"
                    },
                    {
                        "speaker": "cameo",
                        "mood": "surprise-oh",
                        "text": "[surprise-oh] Báo cáo Bác sĩ trưởng, chất thải rắn của bệnh nhân khô khốc đến mức có thể đốt cháy làm chất đốt ngay lập tức!"
                    },
                    {
                        "speaker": "host",
                        "mood": "hao_hung",
                        "text": "Báo cáo hoàn toàn trùng khớp với thực nghiệm lâm sàng! Ruột già của lạc đà tái hấp thu nước triệt để đến mức phân của chúng thải ra khô cong như những viên sỏi gỗ, đến mức người du mục Bedouin có thể nhặt lên và nhóm lửa đun nấu ngay tại chỗ mà không cần phơi khô!"
                    },
                    {
                        "speaker": "host",
                        "mood": "don_dap",
                        "text": "Mọi giọt ẩm đi vào cơ thể đều bị giữ lại và tuần hoàn khép kín với hiệu suất tái sử dụng lên tới chín mươi chín phần trăm, biến cơ thể lạc đà thành một nhà máy xử lý nước tuần hoàn hoàn hảo nhất Trái Đất!"
                    }
                ]
            },
            {
                "id": "scene05",
                "badge": "BỆNH ÁN SỐ 4",
                "chapter_title": "Bệnh án số 4: Ống thở ngưng tụ hơi nước và lỗ mũi van một chiều",
                "hook": "Hệ thống làm mát điều hòa và khóa bụi cát sa mạc",
                "mood": "hao_hung",
                "parts": [
                    {
                        "speaker": "host",
                        "mood": "hao_hung",
                        "text": "Nếu các bạn nghĩ rằng kiểm soát bài tiết là đã chặn đứng mọi lối thoát của nước, thì các bác sĩ đã bỏ quên con đường bốc hơi vô hình nhưng cực kỳ nguy hiểm: Đường hô hấp! Mỗi hơi thở ra của con người mang theo một lượng hơi nước ấm áp bốc hơi vào không khí. Giữa sa mạc khô hạn, nếu thở ra lượng hơi ẩm đó, cơ thể sẽ bị rút cạn kiệt chỉ sau vài giờ thở dốc."
                    },
                    {
                        "speaker": "host",
                        "mood": "tram_bi_an",
                        "text": "Để giải bài toán này, khoang mũi của Cỗ Máy Lọc Nước Sa Mạc được cấu tạo từ các vách xoắn ốc cuộn nhiều tầng phủ đầy niêm mạc hút ẩm đặc biệt. Khi lạc đà thở ra, không khí ấm và ẩm từ phổi đi qua khoang mũi lạnh sẽ bị ngưng tụ hơi nước lại lập tức! Lượng nước ngưng tụ này thấm ngược trở lại niêm mạc mũi để tái hấp thu vào máu, chỉ có luồng không khí khô ráo được thở ra ngoài!"
                    },
                    {
                        "speaker": "cameo",
                        "mood": "surprise-oh",
                        "text": "[surprise-oh] Bác sĩ ơi, còn khi bão cát ập đến thì sao ạ? Bụi cát có tràn vào phổi làm ngạt thở bệnh nhân không?"
                    },
                    {
                        "speaker": "host",
                        "mood": "hao_hung",
                        "text": "Một cơ chế bảo hộ đường thở hoàn mỹ thưa trợ lý! Lỗ mũi của lạc đà được trang bị các cơ vòng van một chiều có thể tự động khép chặt lại hoàn toàn khi có gió cát! Kết hợp cùng đôi hàng mi dày hai tầng đan xen và lớp màng chớp trong suốt bảo vệ mắt, lạc đà có thể thản nhiên bước đi giữa tâm bão cát mù mịt mà không hề hít phải một hạt bụi nào!"
                    },
                    {
                        "speaker": "host",
                        "mood": "don_dap",
                        "text": "Thậm chí thân nhiệt của lạc đà còn có khả năng dao động linh hoạt từ ba mươi bốn độ C vào ban đêm lên tới bốn mươi mốt độ C vào ban ngày! Bằng cách tự nâng nhiệt độ cơ thể lên ngang bằng nhiệt độ môi trường, chúng hoàn toàn không cần đổ mồ hôi để làm mát, tiết kiệm thêm hàng chục lít nước mỗi ngày!"
                    }
                ]
            },
            {
                "id": "scene06",
                "badge": "XUẤT VIỆN AN TOÀN",
                "chapter_title": "Ra viện an toàn: Tinh hoa y học phỏng sinh học giữa biển cát",
                "hook": "Bài học sinh tồn vĩ đại cho tương lai loài người",
                "mood": "hao_hung",
                "parts": [
                    {
                        "speaker": "host",
                        "mood": "hao_hung",
                        "text": "Thưa toàn thể hội đồng y khoa, sau khi khám nghiệm toàn diện từ bướu mỡ chống sốc nhiệt, tế bào hồng cầu hình oval co giãn vô hạn, quả thận siêu lọc cho đến khoang mũi ngưng tụ hơi thở, chúng tôi xin long trọng ký giấy xuất viện cho bệnh nhân Lạc Đà Sa Mạc với xếp loại thể lực phi thường xuất sắc tuyệt đối!"
                    },
                    {
                        "speaker": "host",
                        "mood": "tram_bi_an",
                        "text": "Cỗ Máy Lọc Nước Sa Mạc không đơn thuần là một con thú thồ hàng nhẫn nại, mà là đỉnh cao của công nghệ phỏng sinh học mà nền y học hiện đại của thế kỷ hai mươi mốt vẫn đang ngày đêm nghiên cứu ứng dụng. Các nhà khoa học NASA đang dựa trên cấu trúc hồng cầu co giãn của lạc đà để nghiên cứu các loại dịch truyền nhân tạo cho các phi hành gia bay vào không gian sâu."
                    },
                    {
                        "speaker": "cameo",
                        "mood": "laughter",
                        "text": "[laughter] Quả là một bậc thầy sinh tồn vĩ đại của tự nhiên thưa Bác sĩ trưởng! Thiên nhiên luôn là người thầy thuốc thông thái nhất!"
                    },
                    {
                        "speaker": "host",
                        "mood": "hao_hung",
                        "text": "Hoàn toàn chuẩn xác! Lần tới khi bạn nhìn thấy hình ảnh chú lạc đà thong dong sải bước trên những đồi cát sa mạc hoang vu, hãy nhớ rằng bạn đang chiêm ngưỡng một cỗ máy sinh học tinh vi bậc nhất mà tạo hóa từng tạo tác! Còn bây giờ, giữa chiếc bướu mỡ năng lượng và tế bào hồng cầu oval co giãn, giải pháp y sinh nào làm bạn kinh ngạc nhất? Hãy để lại bình luận bên dưới nhé!"
                    },
                    {
                        "speaker": "host",
                        "mood": "am_ap",
                        "text": "Và đừng quên bấm đăng ký kênh để đón xem Tập ba mươi tám khám phá cỗ máy leo núi trọng lực chín mươi độ của Dê Núi Bắc Mỹ! Hẹn gặp lại toàn thể các bạn trong chuyến hành trình khám phá những kỳ quan sinh học tiếp theo!"
                    }
                ]
            }
        ]
    },
    "shorts": {
        "text": "[surprise-oh] Bạn có biết loài động vật nào có thể uống cạn hai trăm lít nước chỉ trong mười lăm phút mà không bị vỡ hồng cầu chết ngay lập tức không? [laughter] Đó chính là Lạc Đà Sa Mạc — Cỗ Máy Lọc Nước siêu cấp của thiên nhiên! Trái ngược với hiểu lầm của hàng triệu người, chiếc bướu trên lưng nó không hề chứa một giọt nước nào mà là một khối bướu mỡ nặng tới bốn mươi kilôgam giúp chống sốc nhiệt năm mươi độ C! [dissatisfaction-hnn] Bí mật sinh tử thực sự nằm ở tế bào hồng cầu hình oval độc nhất vô nhị: Chúng có thể phồng to gấp hai trăm bốn mươi phần trăm thể tích để nạp nước tức thì, kết hợp cùng quả thận siêu lọc cô đặc nước tiểu thành si-rô đặc quẹt! Nhờ đó, sinh vật phi thường này có thể nhịn uống suốt ba mươi ngày giữa chảo lửa sa mạc mà vẫn sống khỏe re!"
    }
}

p = Path("projects/tap-37-lac-da-sa-mac/episode.json")
p.write_text(json.dumps(ep37_data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Generated ep37 script to {p} ({len(json.dumps(ep37_data))} chars)")

