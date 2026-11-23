import json
from pathlib import Path

ep38_data = {
    "title": "Tập 38: Dê Núi Bắc Mỹ — Vua Trọng Lực Thách Thức Vách Đá 90°",
    "animal": "Dê Núi Bắc Mỹ",
    "format": "F5",
    "persona": "nha_khoa_hoc",
    "nickname": "Vua Trọng Lực 90 Độ",
    "episode_no": 38,
    "sources": [
        "Journal of Experimental Biology - Biomechanics of Locomotion on Steep Slopes in Mountain Goats",
        "Zoological Society of London - Morphology and Friction Mechanics of Split Hooves in Oreamnos americanus",
        "Alpine Sports & Bio-Robotics - Climbing Mechanics and Friction Grippers Inspired by Mountain Goats"
    ],
    "voice": {
        "tempo_long": 1.11,
        "tempo_shorts_min": 1.12,
        "min_long_s": 510,
        "max_long_s": 900
    },
    "whisper_prompt": "Dê Núi Bắc Mỹ, Oreamnos americanus, Vua Trọng Lực 90 Độ, vách đá dựng đứng, móng chẻ hai mảnh, đệm cao su ma sát, 90 độ, 4.000 mét, Rocky Mountains",
    "display_fix": {
        "Tập ba mươi tám": "Tập 38",
        "Tập ba mươi chín": "Tập 39",
        "chín mươi độ": "90°",
        "tám mươi độ": "80°",
        "sáu mươi độ": "60°",
        "bốn mươi lăm độ": "45°",
        "bốn ngàn mét": "4.000m",
        "ba ngàn mét": "3.000m",
        "một ngàn mét": "1.000m",
        "bốn trăm mét": "400m",
        "hai mét": "2m",
        "bốn mét": "4m",
        "năm mét": "5m",
        "một mét": "1m",
        "hai xăng-ti-mét": "2cm",
        "ba xăng-ti-mét": "3cm",
        "một trăm bốn mươi kilôgam": "140 kg",
        "bảy mươi kilôgam": "70 kg",
        "một trăm phần trăm": "100%",
        "năm mươi phần trăm": "50%",
        "sáu mươi phần trăm": "60%",
        "hai mươi bốn giờ": "24 giờ",
        "thế kỷ hai mươi mốt": "thế kỷ 21",
        "hàng triệu năm": "hàng triệu năm",
        "triệu năm": "triệu năm",
        "Oreamnos": "Oreamnos",
        "americanus": "americanus",
        "Rocky": "Rocky",
        "NASA": "NASA"
    },
    "longform": {
        "scenes": [
            {
                "id": "scene01",
                "badge": "ĐẤU TRƯỜNG 90°",
                "banner_title": "THÁCH THỨC TRỌNG LỰC VỰC THẲM",
                "chapter_title": "Khởi động đường đua chín mươi độ: Thách thức trọng lực giữa vực sâu ngàn mét",
                "hook": "Sinh vật thách thức định luật vạn vật hấp dẫn của Newton",
                "mood": "hao_hung",
                "parts": [
                    {
                        "speaker": "host",
                        "mood": "hao_hung",
                        "text": "Chào mừng toàn thể các vận động viên leo núi, các chuyên gia cơ học chuyển động và các bạn đam mê thể thao mạo hiểm bước vào Đấu trường vách đá tử thần trên dãy núi Rocky hùng vĩ! [laughter] Hôm nay, chúng ta sẽ cùng nhau chiêm ngưỡng một cỗ máy sinh học kỳ dị nhất hành tinh, kẻ biến những định luật vạn vật hấp dẫn của nhà bác học Isaac Newton thành một trò đùa giải trí!"
                    },
                    {
                        "speaker": "host",
                        "mood": "don_dap",
                        "text": "Trước mắt chúng ta là một bức tường đá granite dựng đứng chín mươi độ, nhẵn thín như mặt bàn kính, cao chót vót bốn ngàn mét giữa trời xanh mây trắng. Phía dưới chân là vực sâu thăm thẳm không đáy, nơi chỉ cần trượt chân một milimét thôi là bất kỳ sinh vật nào cũng sẽ tan xương nát thịt! Thế nhưng, hãy nhìn lên đỉnh chóp nhọn hoắt kia: Một bóng dáng màu trắng muốt đang bình thản dạo bước, thậm chí đứng thăng bằng chỉ trên một gờ đá hẹp chưa đầy hai xăng-ti-mét!"
                    },
                    {
                        "speaker": "cameo",
                        "cast": "phat_thanh_vien",
                        "mood": "don_dap",
                        "text": "[surprise-oh] Thưa Bình luận viên trưởng, cảm biến gia tốc và trọng trường xác nhận đối tượng đang đứng yên trên vách đá dốc tám mươi chín độ mà không hề có dây bảo hộ hay móc sắt trợ lực!"
                    },
                    {
                        "speaker": "host",
                        "mood": "tram_bi_an",
                        "text": "Một thông số phi thường thưa phát thanh viên hiện trường! Đối tượng đó mang tên khoa học Oreamnos americanus, nhưng người yêu thiên nhiên khắp năm châu gọi nó bằng danh xưng bất khả chiến bại: Vua Trọng Lực 90 Độ! Trong khi các nhà vô địch leo núi chuyên nghiệp của loài người phải trang bị giày đinh, dây dù, móc sắt carabiner và bột chống trơn mới dám thử sức, thì chú dê núi này chỉ cần bốn chiếc móng guốc tự nhiên là đủ để biến vách núi thẳng đứng thành đại lộ thênh thang!"
                    },
                    {
                        "speaker": "host",
                        "mood": "hao_hung",
                        "text": "Bí mật cơ học nào ẩn giấu bên dưới bộ móng guốc ma thuật và hệ xương khớp của sinh vật này? Mời các bạn cùng tôi mở bản vẽ kỹ thuật tầng một để giải mã vũ khí kẹp đá đầu tiên!"
                    }
                ]
            },
            {
                "id": "scene02",
                "badge": "VŨ KHÍ SỐ 1",
                "banner_title": "BỘ MÓNG CHẺ KẸP ĐÁ THỦY LỰC",
                "chapter_title": "Bí kíp số 1: Bộ móng guốc hai mảnh kẹp đá như kìm bấm thủy lực",
                "hook": "Cấu trúc móng chẻ độc lập ôm trọn từng gờ đá siêu nhỏ",
                "mood": "hao_hung",
                "parts": [
                    {
                        "speaker": "host",
                        "mood": "hao_hung",
                        "text": "Hãy bắt đầu với chi tiết cơ khí quan trọng bậc nhất tiếp xúc trực tiếp với mặt đá: Bộ móng guốc chẻ đôi kỳ diệu! Nếu móng ngựa là một khối sừng liền mạch cứng ngắc dễ trượt ngã, thì móng của Vua Trọng Lực 90 Độ lại được chia đôi thành hai nửa móng guốc độc lập hoàn toàn, có thể mở rộng hoặc khép chặt lại linh hoạt như một chiếc kìm bấm thủy lực chuyên dụng!"
                    },
                    {
                        "speaker": "host",
                        "mood": "tram_bi_an",
                        "text": "Lớp vỏ ngoài của móng được cấu tạo từ chất sừng keratin cực kỳ cứng rắn và sắc nhọn như dao cạo. Khi móng chạm vào vách đá, hai nửa móng lập tức xòe rộng ra để kẹp chặt lấy gờ đá li ti, khóa cứng vị trí tiếp xúc và ngăn không cho chân bị trượt ngang dù chỉ một phần mười milimét!"
                    },
                    {
                        "speaker": "cameo",
                        "cast": "chu_ngo_ngac",
                        "mood": "hao_hung",
                        "text": "[surprise-oh] Ủa Bác sĩ ơi, vậy nếu gờ đá nhỏ chỉ bằng đầu ngón tay thì móng guốc bám vào đâu để chịu được sức nặng cả trăm ký của nó?"
                    },
                    {
                        "speaker": "host",
                        "mood": "don_dap",
                        "text": "Một câu hỏi rất sắc sảo thưa trợ lý tập sự! Phía sau hai nửa móng chính, dê núi còn sở hữu hai chiếc móng phụ thoái hóa gọi là móng huyền. Khi cơ thể trượt nhẹ trên sườn dốc nghiêng, hai chiếc móng phụ này sẽ cắm phập vào vách đá như chiếc mỏ neo phụ trợ, đóng vai trò như chiếc phanh khẩn cấp hãm đà rơi tự do ngay trong tích tắc!"
                    },
                    {
                        "speaker": "host",
                        "mood": "tram_bi_an",
                        "text": "Nhờ cơ chế kẹp hai tầng này, dù con đực trưởng thành nặng tới một trăm bốn mươi kilôgam, toàn bộ khối lượng khổng lồ đó vẫn được truyền tải chuẩn xác xuống các điểm tì chỉ rộng vỏn vẹn vài milimét trên vách đá hoa cương dựng đứng!"
                    }
                ]
            },
            {
                "id": "scene03",
                "badge": "VŨ KHÍ SỐ 2",
                "banner_title": "ĐỆM CAO SU MA SÁT BÁM DÍNH",
                "chapter_title": "Bí kíp số 2: Đệm cao su ma sát cao bám dính siêu cấp",
                "hook": "Vật liệu phỏng sinh học lấy cảm hứng cho lốp xe đua",
                "mood": "hao_hung",
                "parts": [
                    {
                        "speaker": "host",
                        "mood": "hao_hung",
                        "text": "Nếu lớp vỏ sừng cứng bên ngoài là chiếc kẹp gắp đá, thì phần lòng bàn chân bên trong lại là một kiệt tác vật liệu polymer tự nhiên: Lớp đệm thịt ma sát siêu bám dính! Nằm lọt thỏm giữa hai nửa móng sừng là một lớp đệm mô xốp mềm dẻo và đàn hồi, sần sùi với hàng ngàn vi rãnh hút chân không siêu nhỏ."
                    },
                    {
                        "speaker": "host",
                        "mood": "don_dap",
                        "text": "Khi móng guốc dẫm lên bề mặt đá gồ ghề, lớp đệm mềm này sẽ tự động biến dạng và lún sâu vào từng kẽ nứt li ti của mặt đá, tạo ra diện tích tiếp xúc ma sát cực đại! Hệ số ma sát tĩnh của lớp đệm này cao gấp ba lần so với các loại đế giày cao su leo núi đắt tiền nhất hiện nay của con người!"
                    },
                    {
                        "speaker": "cameo",
                        "cast": "co_tro_ly",
                        "mood": "hao_hung",
                        "text": "[surprise-oh] Thưa Chuyên gia, có phải bề mặt đệm chân này vẫn bám dính hoàn hảo ngay cả trên lớp băng tuyết trơn trượt không ạ?"
                    },
                    {
                        "speaker": "host",
                        "mood": "hao_hung",
                        "text": "Chính xác tuyệt đối thưa trợ lý! Ngay cả khi nhiệt độ rơi xuống âm ba mươi độ C và vách đá bị bao phủ bởi lớp băng tuyết trơn như mỡ, lớp đệm thịt này vẫn giữ được độ đàn hồi dẻo dai mà không hề bị đông cứng hay giòn rụm. Nó hoạt động hệt như lốp xe đua chuyên dụng dùng trong điều kiện mưa tuyết của giải đua Công thức Một!"
                    },
                    {
                        "speaker": "host",
                        "mood": "tram_bi_an",
                        "text": "Sự kết hợp giữa viền sừng cứng cáp bên ngoài để cắm vào khe nứt và đệm cao su êm ái bên trong để hút ma sát biến mỗi bước chân của Vua Trọng Lực 90 Độ thành một giác hút cơ học bất khả xâm phạm!"
                    }
                ]
            },
            {
                "id": "scene04",
                "badge": "VŨ KHÍ SỐ 3",
                "banner_title": "TRỌNG TÂM THẤP VÀ KHỚP VAI XOAY",
                "chapter_title": "Bí kíp số 3: Trọng tâm cơ thể siêu thấp và khớp bả vai xoay linh hoạt",
                "hook": "Giải phẫu học tối ưu hóa cân bằng động lực học",
                "mood": "hao_hung",
                "parts": [
                    {
                        "speaker": "host",
                        "mood": "hao_hung",
                        "text": "Bây giờ, xin mời các kỹ sư cơ khí chuyển góc nhìn lên toàn bộ hệ thống khung gầm của bệnh nhân: Trọng tâm cơ thể và khớp bả vai! Nếu một con người hay loài hươu nai cố gắng bước lên vách đá dốc, thân hình cao lêu nghêu sẽ khiến trọng tâm cơ thể bị đẩy ra ngoài vách đá, tạo ra mô-men lật đổ khiến chúng lập tức ngã nhào xuống vực sâu."
                    },
                    {
                        "speaker": "host",
                        "mood": "tram_bi_an",
                        "text": "Thế nhưng cấu trúc giải phẫu của dê núi Bắc Mỹ lại hoàn toàn ngược lại: Chúng sở hữu đôi chân trước ngắn hơn chân sau, lồng ngực vạm vỡ ép sát vào sườn núi, và các khối cơ bắp vai cuồn cuộn giúp kéo trọng tâm cơ thể hạ thấp tối đa và ép sát vào mặt phẳng vách đá!"
                    },
                    {
                        "speaker": "cameo",
                        "cast": "ong_gia_ke",
                        "mood": "am_ap",
                        "text": "Hơn thế nữa, khớp bả vai của loài dê này có biên độ xoay tự do cực kỳ rộng, cho phép hai chân trước xoay ngang sang hai bên như hai cánh tay lực lưỡng để bám víu và kéo toàn bộ cơ thể đi lên!"
                    },
                    {
                        "speaker": "host",
                        "mood": "don_dap",
                        "text": "Nhờ khối cơ bắp cổ và vai cực khỏe, Vua Trọng Lực 90 Độ có thể nâng toàn bộ trọng lượng một trăm bốn mươi kilôgam của mình chỉ bằng hai chân trước trong tư thế treo lơ lửng giữa không trung! Không một loài thú móng guốc nào trên Trái Đất có thể thực hiện được tư thế xà đơn ngoạn mục đến như vậy!"
                    },
                    {
                        "speaker": "host",
                        "mood": "hao_hung",
                        "text": "Mọi véc-tơ lực học đều được triệt tiêu và ép thẳng vào tâm vách đá, biến cơ thể nó thành một khối hợp nhất vững chãi như một tảng đá mọc ra từ lòng núi!"
                    }
                ]
            },
            {
                "id": "scene05",
                "badge": "VŨ KHÍ SỐ 4",
                "banner_title": "CÚ BÚNG TƯỜNG NGOẠN MỤC",
                "chapter_title": "Bí kíp số 4: Cú nhảy búng tường ngoạn mục xoay người giữa không trung",
                "hook": "Kỹ thuật parkour đỉnh cao của nhà vô địch vách đá",
                "mood": "hao_hung",
                "parts": [
                    {
                        "speaker": "host",
                        "mood": "hao_hung",
                        "text": "Nhưng đỉnh cao nghệ thuật leo núi của sinh vật này chỉ thực sự bùng nổ khi nó rơi vào ngõ cụt: Không còn gờ đá nào phía trước để tiến lên! Trong hoàn cảnh đó, nếu là con người hay bất kỳ loài thú nào, họ sẽ tuyệt vọng và chờ chết. Thế nhưng đối với dê núi, đây lại là lúc màn trình diễn nhào lộn parkour thượng thừa bắt đầu!"
                    },
                    {
                        "speaker": "host",
                        "mood": "don_dap",
                        "text": "Nó sẽ dồn toàn lực vào đôi chân sau lò xo, tung mình nhảy vọt ra khỏi vách đá sang bức tường đá đối diện cách xa tới bốn mét! Ngay khi chạm vào mặt đá phẳng lì, nó không hề cố gắng dừng lại mà lập tức dùng bốn móng guốc đạp mạnh vào vách đá để búng ngược lại bức tường ban đầu ở một vị trí cao hơn!"
                    },
                    {
                        "speaker": "cameo",
                        "cast": "chu_ngo_ngac",
                        "mood": "don_dap",
                        "text": "[surprise-oh] Thưa Huấn luyện viên, động tác búng tường liên hoàn đó diễn ra trong bao lâu? Nó có thể xoay người đổi hướng giữa không trung được không ạ?"
                    },
                    {
                        "speaker": "host",
                        "mood": "hao_hung",
                        "text": "Toàn bộ cú búng tường xoay người một trăm tám mươi độ chỉ diễn ra trong vòng chưa đầy nửa giây! Bằng cách thay đổi góc đạp của móng guốc, nó có thể nhảy zig-zag giữa hai khe nứt hẹp của hẻm núi để leo thẳng lên đỉnh dốc với tốc độ nhanh gấp mười lần một người leo núi chuyên nghiệp!"
                    },
                    {
                        "speaker": "host",
                        "mood": "tram_bi_an",
                        "text": "Thậm chí khi bị chó sói hay báo sư tử truy đuổi, Vua Trọng Lực 90 Độ chỉ cần nhảy nhẹ xuống một gờ đá dốc đứng phía dưới là kẻ săn mồi đã phải đứng trên bờ vực chùn bước trong bất lực và sợ hãi!"
                    }
                ]
            },
            {
                "id": "scene06",
                "badge": "TRAO HUY CHƯƠNG",
                "banner_title": "ĐỈNH CAO THỂ THAO MẠO HIỂM",
                "chapter_title": "Trao huy chương vàng: Đỉnh cao thể thao mạo hiểm phỏng sinh học",
                "hook": "Tôn vinh cỗ máy vượt dốc vĩ đại nhất của tạo hóa",
                "mood": "hao_hung",
                "parts": [
                    {
                        "speaker": "host",
                        "mood": "hao_hung",
                        "text": "Thưa toàn thể ban giám khảo và khán giả theo dõi đấu trường, sau khi chấm điểm toàn bộ bốn vũ khí từ móng chẻ kìm bấm thủy lực, đệm cao su ma sát siêu cấp, trọng tâm cơ thể hạ thấp cho đến cú búng tường zig-zag ngoạn mục, hội đồng chuyên môn nhất trí trao tặng Huy chương Vàng Thể thao Mạo hiểm cho Dê Núi Bắc Mỹ!"
                    },
                    {
                        "speaker": "host",
                        "mood": "tram_bi_an",
                        "text": "Vua Trọng Lực 90 Độ chính là nguồn cảm hứng vô tận cho các kỹ sư chế tạo robot thám hiểm địa hình hiểm trở của NASA để khảo sát các hẻm núi sâu trên Sao Hỏa và Mặt Trăng. Các tập đoàn sản xuất thiết bị leo núi cũng đang mô phỏng cấu trúc đệm móng của dê núi để tạo ra thế hệ giày leo núi bám dính không trọng lực cho con người."
                    },
                    {
                        "speaker": "cameo",
                        "cast": "ong_gia_ke",
                        "mood": "am_ap",
                        "text": "[laughter] Thật là một kỳ quan cơ học và thể thao vĩ đại của thiên nhiên hoang dã! Nơi hiểm nguy nhất lại chính là ngôi nhà an toàn và bình yên nhất của những kẻ dám vượt lên trọng lực!"
                    },
                    {
                        "speaker": "host",
                        "mood": "hao_hung",
                        "text": "Hoàn toàn chuẩn xác! Lần tới khi bạn đối mặt với những ngọn núi cao tưởng chừng như không thể vượt qua trong cuộc sống, hãy nhớ đến hình ảnh chú dê núi kiên cường đứng vững trên vách đá chín mươi độ! Còn bây giờ, giữa chiếc móng chẻ thủy lực và đệm cao su ma sát, cơ chế nào khiến bạn trầm trồ nhất? Hãy để lại bình luận bên dưới nhé!"
                    },
                    {
                        "speaker": "host",
                        "mood": "am_ap",
                        "text": "Và đừng quên bấm đăng ký kênh để đón xem Tập ba mươi chín khám phá sát thủ ngây thơ giấu mặt của Chim Bách Thanh! Hẹn gặp lại toàn thể các bạn trong những chuyến phiêu lưu kỳ thú tiếp theo!"
                    }
                ]
            }
        ]
    },
    "shorts": {
        "text": "[surprise-oh] Bạn có tin trên Trái Đất có một loài động vật nặng tới một trăm bốn mươi kilôgam nhưng có thể đứng thăng bằng trên vách đá dựng đứng chín mươi độ nhẵn thín như mặt bàn kính không? [laughter] Đó chính là Dê Núi Bắc Mỹ — Vua Trọng Lực vô địch của thiên nhiên! Bí mật kinh thiên động địa nằm ở bộ móng guốc chẻ đôi kỳ ảo: Hai nửa móng có thể kẹp chặt gờ đá như kìm bấm thủy lực, kết hợp cùng lớp đệm thịt cao su ma sát cực đại có hệ số bám dính gấp ba lần đế giày leo núi chuyên nghiệp! [dissatisfaction-hnn] Khi gặp ngõ cụt giữa vực sâu ngàn mét, nó có thể tung mình nhảy xa bốn mét và búng tường xoay người một trăm tám mươi độ chỉ trong chớp mắt! Thật là một bậc thầy nhào lộn thách thức mọi định luật vật lý!"
    }
}

p = Path("projects/tap-38-de-nui-bac-my/episode.json")
p.write_text(json.dumps(ep38_data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Generated ep38 script to {p} ({len(json.dumps(ep38_data))} chars)")

