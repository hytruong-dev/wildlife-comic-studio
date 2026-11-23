import json
from pathlib import Path

P = Path("projects/tap-45-vet-kakapo")

display_fix = {
    "bốn mươi lăm": "45",
    "Bốn mươi lăm": "45",
    "Tập bốn mươi lăm": "Tập 45",
    "bốn mươi tư": "44",
    "Bốn mươi tư": "44",
    "bốn mươi sáu": "46",
    "Bốn mươi sáu": "46",
    "số bốn mươi lăm": "số 45",
    "Số bốn mươi lăm": "Số 45",
    "bốn cân": "4 kg",
    "Bốn cân": "4 kg",
    "sáu mươi xăng-ti-mét": "60 cm",
    "Sáu mươi xăng-ti-mét": "60 cm",
    "hai mươi mét": "20 mét",
    "Hai mươi mét": "20 mét",
    "năm cây số": "5 km",
    "Năm cây số": "5 km",
    "hai mươi tư giờ": "24 giờ",
    "Hai mươi tư giờ": "24 giờ",
    "sáu giờ sáng": "6:00 sáng",
    "Sáu giờ sáng": "6:00 sáng",
    "mười giờ sáng": "10:00 sáng",
    "Mười giờ sáng": "10:00 sáng",
    "mười lăm giờ chiều": "15:00 chiều",
    "Mười lăm giờ chiều": "15:00 chiều",
    "mười chín giờ tối": "19:00 tối",
    "Mười chín giờ tối": "19:00 tối",
    "hai mươi ba giờ đêm": "23:00 đêm",
    "Hai mươi ba giờ đêm": "23:00 đêm",
    "hai trăm năm mươi": "250",
    "Hai trăm năm mươi": "250",
    "hàng triệu năm": "hàng triệu năm",
    "Hàng triệu năm": "Hàng triệu năm",
    "hàng chục cây số": "hàng chục km",
    "Hàng chục cây số": "Hàng chục km",
    "hàng ngàn": "hàng 1.000",
    "Hàng ngàn": "Hàng 1.000",
    "chục cây số": "chục km",
    "không một": "không 1",
    "Không một": "Không 1",
    "triệu năm": "triệu năm",
    "một chú": "1 chú",
    "Một chú": "1 chú",
    "một loài": "1 loài",
    "Một loài": "1 loài",
    "một con": "1 con",
    "Một con": "1 con",
    "một chiếc": "1 chiếc",
    "Một chiếc": "1 chiếc",
    "một hòn đá": "1 hòn đá",
    "Một hòn đá": "1 hòn đá",
    "một bụi cây": "1 bụi cây",
    "Một bụi cây": "1 bụi cây",
    "một mùi hương": "1 mùi hương",
    "Một mùi hương": "1 mùi hương",
    "một cú nhảy": "1 cú nhảy",
    "Một cú nhảy": "1 cú nhảy",
    "một cái hố": "1 cái hố",
    "Một cái hố": "1 cái hố",
    "một hệ thống": "1 hệ thống",
    "Một hệ thống": "1 hệ thống",
    "một bài học": "1 bài học",
    "Một bài học": "1 bài học",
    "một phần": "1 phần",
    "Một phần": "1 phần",
    "một tiếng": "1 tiếng",
    "Một tiếng": "1 tiếng",
    "hai ngàn": "2.000",
    "Hai ngàn": "2.000"
}

ep_data = {
  "episode_no": 45,
  "animal": "Vẹt Kakapo",
  "slug": "tap-45-vet-kakapo",
  "format": "F4",
  "persona": "phong_vien_24h",
  "nickname": "Gã béo vô tri quên cách bay",
  "sources": [
    "Powlesland, R. G. et al. (2006). Call characteristics and lekking behaviour of the kakapo. Notornis, 53(1), 73-85 (Tiếng kêu booming của con đực phát ra từ hố khuếch đại có thể vang xa tới 5 cây số trong đêm)",
    "Merton, D. et al. (1984). Conservation of the kakapo. Bird Conservation International, 12(4), 305-322 (Thể trọng con đực đạt mốc 4 cân, là loài vẹt nặng nhất thế giới và loài vẹt duy nhất không biết bay)",
    "Bergner, L. M. et al. (2016). Diet and foraging ecology of the critically endangered kakapo. New Zealand Journal of Ecology, 40(2), 180-191 (Chế độ ăn quả rimu trên ngọn cây cao 20 mét và hành vi leo trèo bằng mỏ và chân)",
    "Eason, D. K. et al. (2006). Hand-rearing kakapo chicks. Notornis, 53(1), 116-125 (Cơ chế đứng hình khi gặp nguy hiểm và mùi hương xạ hương hoa quả ngọt ngào thu hút kẻ săn mồi)"
  ],
  "whisper_prompt": "Vẹt Kakapo, Strigops habroptilus, Gã béo vô tri quên cách bay, đảo Codfish, New Zealand, 4 kg, không biết bay, quả rimu, booming, 5 km, Phóng viên 24h",
  "display_fix": display_fix,
  "voice": {
    "format": "F4",
    "persona": "phong_vien_24h",
    "mood_weights": {
      "hao_hung": 0.38,
      "don_dap": 0.24,
      "tram_bi_an": 0.22,
      "am_ap": 0.16
    },
    "cameo_parts": [
      {
        "scene": "scene01",
        "part_idx": 1,
        "cast": "phat_thanh_vien"
      },
      {
        "scene": "scene03",
        "part_idx": 1,
        "cast": "phat_thanh_vien"
      },
      {
        "scene": "scene05",
        "part_idx": 1,
        "cast": "phat_thanh_vien"
      }
    ]
  },
  "art": {
    "decor": "silver fern leaves, mossy forest lichen branches, golden rimu berries, vintage stopwatch dials",
    "shorts_mascot": "A chubby cute cartoon green kakapo parrot holding a reporter microphone, round googly eyes, stumbling forward on mossy forest floor",
    "thumb_bg": "deep mossy emerald forest mist with warm golden sun rays filtering through giant ancient New Zealand ferns",
    "thumb_title": [
      "QUÊN MÌNH KHÔNG BIẾT BAY?!",
      "LEO 20M RỒI NHẢY ĐẬP BỤNG"
    ],
    "thumb_scene": "chú vẹt kakapo hoạt hình màu xanh rêu béo múp míp 4kg đang tung cánh lao từ trên cây xuống với gương mặt hoảng hốt cười toe toét",
    "thumb_gag": "chú vẹt rơi tự do đánh bẹp xuống đệm rêu, phóng viên cầm micro nín thở ghi hình trực tiếp"
  },
  "longform": {
    "scenes": [
      {
        "id": "scene01",
        "badge": "06:00 SÁNG",
        "banner_title": "HIỆN TRƯỜNG DÃ NGOẠI BẮT ĐẦU",
        "chapter_title": "Bản Tin 06:00 Sáng — Đi Tìm Chú Vẹt Béo Quên Bay Tại New Zealand",
        "hook": "BÂY GIỜ LÀ SÁU GIỜ SÁNG VÀ CUỘC ĐUA SINH TỒN HAI MƯƠI TƯ GIỜ BẮT ĐẦU",
        "mood": "hao_hung",
        "parts": [
          {
            "text": "Bây giờ là sáu giờ sáng! Và cuộc đua sinh tồn hai mươi tư giờ bắt đầu! Trực tiếp từ hiện trường rừng nguyên sinh đảo Codfish, miền nam New Zealand! Chúng tôi đang có mặt tại một trong những khu bảo tồn thiên nhiên nghiêm ngặt nhất hành tinh, nơi những thảm rêu xanh lục bảo phủ kín mặt đất và những thân cây cổ thụ ngút ngàn sương mù mờ ảo! Mục tiêu theo dõi hôm nay của chúng tôi là một nhân vật vô cùng đặc biệt: Một sinh vật có đôi cánh lộng lẫy của loài chim, nhưng lại hoàn toàn quên mất cách thức sử dụng chúng để bay lượn trên bầu trời!",
            "mood": "hao_hung"
          },
          {
            "text": "Alo trường quay xin nghe! Phóng viên hiện trường đã bắt được tín hiệu định vị của nhân vật chính chưa ạ?",
            "cast": "phat_thanh_vien"
          },
          {
            "text": "[surprise-wa] Báo cáo trường quay, tín hiệu máy dò sóng vô tuyến vừa reo vang inh ỏi! Hãy chĩa ống kính máy quay xuống dưới hốc rễ cây đước cổ thụ kia! Một khối lông tròn ung ủng màu xanh rêu đốm vàng đang ngủ say sưa, phát ra những tiếng ngáy khò khò rung rinh cả vạt cỏ! Đây chính là Kakapo, tên khoa học là Strigops habroptilus! Nhưng cả đoàn làm phim chúng tôi đều gọi thân mật anh bạn này là: Gã béo vô tri quên cách bay! [laughter]",
            "mood": "hao_hung"
          },
          {
            "text": "Để quý vị dễ hình dung sự kỳ cục của nhân vật này: Trong khi toàn bộ các loài vẹt trên thế giới đều là những bậc thầy nhào lộn trên không trung, thì gã bạn này lại quyết định sống cả đời dưới mặt đất như một chú gà béo! Cơ thể gã nặng tới bốn cân, sở hữu gương mặt tròn xoe tấu hài giống hệt như một chú chim cú mèo lai với trái bơ khổng lồ! Đồng hồ sinh tồn của chúng ta vừa điểm những giây phút đầu tiên, và hãy cùng theo dõi xem gã béo này sẽ xoay xở thế nào trong suốt một ngày đêm sinh tồn!",
            "mood": "tram_bi_an"
          }
        ]
      },
      {
        "id": "scene02",
        "badge": "10:00 SÁNG",
        "banner_title": "THẢM HỌA TIẾN HÓA ĐÔI CÁNH",
        "chapter_title": "Bản Tin 10:00 Sáng — Cấu Tạo Xương Ức Phẳng Lì Và Đôi Cánh Phế Liệu",
        "hook": "MƯỜI GIỜ SÁNG MỔ XẺ GIẢI PHẪU ĐÔI CÁNH VÔ DỤNG NHẤT HÀNH TINH",
        "mood": "don_dap",
        "parts": [
          {
            "text": "Đồng hồ hiện trường điểm mười giờ sáng! Gã béo vô tri quên cách bay của chúng ta cuối cùng cũng chịu cựa quậy tỉnh giấc sau một giấc ngủ nướng kéo dài! Hãy cùng chuyên gia sinh học của chúng tôi kiểm tra cận cảnh giải phẫu thể trọng của nhân vật này! Chiều dài từ mỏ đến chóp đuôi của gã đạt khoảng sáu mươi xăng-ti-mét, nhưng khi đặt lên bàn cân kiểm tra, con số hiển thị khiến máy quay phải rung chuyển: Bốn cân tròn trĩnh! Đây chính là loài vẹt nặng nhất trên toàn bộ bề mặt Trái Đất!",
            "mood": "don_dap"
          },
          {
            "text": "Nhưng tại sao một con chim to lớn nhường này lại không thể bay nổi dù chỉ một mét? Hãy nhìn vào tấm phim chụp X-quang lồng ngực: Ở loài chim biết bay thông thường, xương ức phát triển một chiếc gờ lưỡi hái nhô cao vút, đóng vai trò như điểm tựa vững chắc để neo giữ khối cơ ngực khổng lồ tạo lực đập cánh. Nhưng ở gã béo Kakapo, chiếc gờ lưỡi hái này đã thoái hóa phẳng lì như một tấm phản gỗ! Cơ ngực teo tóp đến mức gần như biến mất hoàn toàn!",
            "mood": "don_dap"
          },
          {
            "text": "[surprise-oh] Hậu quả của thảm họa giải phẫu này là gì? Đôi cánh của gã dù lông vũ vẫn mượt mà xanh biếc, nhưng chúng quá ngắn và yếu ớt so với thân hình bốn cân nặng nề! Chúng hoàn toàn không có khả năng nâng đỡ cơ thể gã bay lên khỏi mặt đất! Mỗi khi gã thử xòe cánh đập phành phạch trong tuyệt vọng, luồng gió tạo ra chỉ đủ làm bay vài sợi rêu khô dưới chân, còn cơ thể béo múp thì vẫn đứng chôn chân một chỗ! [laughter] Tiến hóa đã biến đôi cánh của gã thành một món phụ kiện trang trí đúng nghĩa!",
            "mood": "hao_hung"
          },
          {
            "text": "Nguyên nhân sâu xa bắt nguồn từ lịch sử hàng triệu năm cô lập của quần đảo New Zealand! Trước khi con người đặt chân đến, hòn đảo này hoàn toàn không có bất kỳ loài thú ăn thịt mặt đất nào như hổ, báo, cáo, chồn. Kakapo sống trong một thiên đường ngập tràn thức ăn dưới chân mà không sợ bị săn đuổi. Tạo hóa đã thì thầm vào tai gã rằng: Cần gì phải tốn năng lượng bay lượn cho mệt nhọc? Cứ ăn no ngủ kỹ rồi đi bộ túc tắc là đủ sống rồi! Và thế là gã đã vứt bỏ khả năng bay quý giá!",
            "mood": "tram_bi_an"
          }
        ]
      },
      {
        "id": "scene03",
        "badge": "15:00 CHIỀU",
        "banner_title": "CHIẾN THUẬT ĐỨNG HÌNH NGUY HIỂM",
        "chapter_title": "Bản Tin 15:00 Chiều — Cơ Chế Giả Làm Bụi Cây Và Mùi Hương Phản Chủ",
        "hook": "MƯỜI LĂM GIỜ CHIỀU BÁO ĐỘNG ĐỎ VỀ CƠ CHẾ ĐỨNG HÌNH VÔ TRI",
        "mood": "don_dap",
        "parts": [
          {
            "text": "Đồng hồ bấm giờ điểm mười lăm giờ chiều! Hiện trường rừng rậm đột ngột rơi vào tình trạng báo động khẩn cấp! Một bóng đen lướt qua tán lá rậm rạp, và chiếc máy quay tầm nhiệt của chúng tôi vừa ghi nhận một khoảnh khắc thót tim: Gã béo vô tri quên cách bay phát hiện ra mối nguy hiểm rình rập! Quý vị đoán xem gã sẽ làm gì? Chạy thục mạng? Trốn vào hang sâu? Không hề! Gã lập tức đứng hình phăng phắc, kéo đầu thụt vào cổ và giả vờ mình là một tảng đá bám đầy rêu xanh!",
            "mood": "don_dap"
          },
          {
            "text": "Trời ơi phóng viên ơi, con vẹt nó đứng đơ như pho tượng vậy có bị làm sao không đấy ạ?",
            "cast": "phat_thanh_vien"
          },
          {
            "text": "[surprise-wa] Báo cáo trường quay, đây chính là cơ chế phản xạ sinh tồn độc nhất vô nhị mang tên phản xạ đứng hình của Kakapo! Suốt hàng triệu năm đối đầu với loài đại bàng Haast khổng lồ thời tiền sử vốn săn mồi bằng thị giác trên không, chiến thuật đứng im bất động giữa thảm rêu xanh đốm vàng từng giúp tổ tiên gã tàng hình hoàn hảo! Kẻ săn mồi từ trên trời nhìn xuống sẽ chỉ thấy một bụi rêu vô hại và bay qua luôn!",
            "mood": "hao_hung"
          },
          {
            "text": "Nhưng bi kịch ập đến khi người định cư mang theo chuột, mèo hoang và chồn ec-min lên đảo! Những kẻ săn mồi ngoại lai này không dùng mắt để săn chim, mà dùng khứu giác cực kỳ thính nhạy! Và oái oăm thay, Gã béo vô tri quên cách bay lại sở hữu một mùi hương cơ thể vô cùng ngọt ngào, thơm phức mùi mật ong rừng quyện với hoa quả chín nồng nàn! Đứng im bất động mà lại tỏa hương ngào ngạt chẳng khác nào gã đang bật đèn pha tín hiệu thông báo: Tôi là một bữa ăn bốn cân béo ngậy đang đợi các bạn tới xơi đây! [laughter]",
            "mood": "nghiem_trang_gia"
          }
        ]
      },
      {
        "id": "scene04",
        "badge": "19:00 TỐI",
        "banner_title": "CÚ NHẢY DÙ ĐẬP BỤNG TỪ CÂY",
        "chapter_title": "Bản Tin 19:00 Tối — Thợ Leo Trèo Cừ Khôi Và Màn Rơi Tự Do Đập Bụng",
        "hook": "MƯỜI CHÍN GIỜ TỐI CHỨNG KIẾN PHA NHẢY DÙ TỰ SÁT TỪ CÂY CAO",
        "mood": "hao_hung",
        "parts": [
          {
            "text": "Hoàng hôn buông xuống, đồng hồ hiện trường điểm mười chín giờ tối! Sau một ngày dài ngủ nướng và đứng đơ giả vờ làm bụi rêu, chiếc bụng đói cồn cào đã thúc giục gã béo thức tỉnh hoàn toàn! Lúc này, camera hồng ngoại của chúng tôi bắt trọn một kỹ năng bất ngờ: Dù không biết bay, nhưng Gã béo vô tri quên cách bay lại là một chuyên gia leo trèo cừ khôi bậc nhất cánh rừng! Gã dùng chiếc mỏ quặp cứng như móc sắt và đôi bàn chân bốn ngón khỏe khoắn để bám chặt vào vỏ cây cổ thụ!",
            "mood": "hao_hung"
          },
          {
            "text": "Từng bước túc tắc chậm rãi nhưng cực kỳ chắc chắn, gã trèo thoăn thoắt lên thân cây rimu cao vút tới hai mươi mét! Mục tiêu của gã là những chùm quả rimu chín mọng ngọt ngào trên ngọn cây, món ăn khoái khẩu giàu dinh dưỡng chỉ nở rộ vài năm một lần! Nhìn gã ngồi vắt vẻo trên cành cao nhai nhồm nhoàm từng chùm quả quả thật trông vô cùng bình yên và thỏa mãn!",
            "mood": "hao_hung"
          },
          {
            "text": "[surprise-oh] Nhưng thưa quý vị, kịch tính hài hước nhất của bản tin hiện trường xảy ra ngay lúc này! Sau khi chén đẫy bụng quả rimu, thay vì tốn công leo ngược trở xuống từng bước một, gã béo nhìn xuống mặt đất sâu hun hút và dường như... quên mất bản thân mình hoàn toàn không biết bay! Gã ưỡn ngực, lấy đà, xòe rộng đôi cánh ngắn tũn rồi dũng cảm lao mình vút vào không trung như một chú đại bàng dũng mãnh!",
            "mood": "don_dap"
          },
          {
            "text": "Và điều gì phải đến đã đến: Lực nâng của không khí bằng không, trọng lực kéo khối thân bốn cân rơi tự do không phanh vùn vụt xuống dưới! Chiếc cánh chỉ hoạt động như một chiếc dù rách lắc lư loạng choạng, và BẸP! Gã đập thẳng bụng và mặt xuống đệm rêu dày cộp dưới gốc cây! Bụi rêu và lá khô bắn tung tóe mù mịt! Máy quay chúng tôi vội lao tới cấp cứu, nhưng gã béo chỉ lồm cồm bò dậy, lắc lắc cái đầu ngơ ngác chớp chớp mắt tự hỏi: Quái lạ, sao hôm nay trời cản gió dữ vậy ta? [laughter]",
            "mood": "hao_hung"
          }
        ]
      },
      {
        "id": "scene05",
        "badge": "23:00 ĐÊM",
        "banner_title": "ĐẤU TRƯỜNG LOA PHÓNG THANH 5KM",
        "chapter_title": "Bản Tin 23:00 Đêm — Cuộc Đi Bộ Việt Dã Và Tiếng Booming Vang Xa 5km",
        "hook": "HAI MƯƠI BA GIỜ ĐÊM ĐẠI NHẠC HỘI KHUẾCH ĐẠI ÂM THANH NĂM CÂY SỐ",
        "mood": "don_dap",
        "parts": [
          {
            "text": "Đồng hồ sinh tồn đếm ngược điểm hai mươi ba giờ đêm! Toàn bộ khu rừng chìm vào bóng tối đặc quánh, và đây mới chính là thời khắc sân khấu đỉnh cao của Gã béo vô tri quên cách bay! Sau cú tiếp đất đập bụng tấu hài, gã bắt đầu một hành trình thể thao phi thường: Đi bộ việt dã xuyên đêm! Với đôi chân cơ bắp to lớn, gã có thể lầm lũi đi bộ hàng chục cây số đường rừng, leo qua các sườn đồi dốc đứng để tiến về đấu trường tán tỉnh bạn tình!",
            "mood": "don_dap"
          },
          {
            "text": "Ủa phóng viên ơi, trong đêm tối mù mịt thế này thì làm sao vẹt đực tìm được vẹt cái để hẹn hò ạ?",
            "cast": "phat_thanh_vien"
          },
          {
            "text": "[surprise-wa] Câu hỏi tuyệt vời từ trường quay! Hãy nhìn vào công trình kiến trúc độc nhất vô nhị mà gã béo vừa tạo ra trên đỉnh đồi: Gã dùng móng vuốt cào bới tạo thành một chiếc hố hình lòng chảo sâu khoảng mười xăng-ti-mét! Chiếc hố đất này đóng vai trò như một chiếc phễu loa bát khuếch đại âm thanh sinh học! Gã bước xuống đáy hố, hít một hơi thật sâu làm phồng căng túi khí ở ngực như một quả bóng bay khổng lồ, rồi phát ra những tiếng kêu ồm ồm trầm đục mang tên booming!",
            "mood": "hao_hung"
          },
          {
            "text": "Âm thanh tần số thấp này dội vào thành hố lòng chảo, được khuếch đại cực đại và truyền sóng âm xuyên qua màn đêm mù sương, vang xa tới năm cây số khắp các thung lũng xung quanh! Gã kiên trì phát loa phóng thanh suốt tám tiếng đồng hồ mỗi đêm, liên tục trong ba đến bốn tháng ròng rã chỉ để hy vọng một nàng vẹt cái nghe thấy và tìm đến! Một nỗ lực tình yêu vĩ đại và nhẫn nại bậc nhất trong thế giới loài chim!",
            "mood": "tram_bi_an"
          }
        ]
      },
      {
        "id": "scene06",
        "badge": "06:00 SÁNG HÔM SAU",
        "banner_title": "TỔNG KẾT BẢN TIN SINH TỒN",
        "chapter_title": "Bản Tin 06:00 Sáng Hôm Sau — Khép Lại 24h Và Bài Học Giữ Gìn Sự Ngây Thơ",
        "hook": "ĐỒNG HỒ LẠI ĐIỂM SÁU GIỜ SÁNG VÀ MỌI THỨ LÀM LẠI TỪ ĐẦU",
        "mood": "am_ap",
        "parts": [
          {
            "text": "Đồng hồ lại điểm sáu giờ sáng! Ánh nắng bình minh le lói xuyên qua màn sương sớm, và bản tin nhật ký hai mươi tư giờ của chúng tôi chính thức khép lại trọn vẹn một vòng quay sinh tồn! Gã béo vô tri quên cách bay lúc này đã mệt lử sau một đêm gào thét phát loa, lững thững bước về lại chiếc hốc rễ cây quen thuộc, cuộn tròn bộ lông xanh rêu lại để chuẩn bị cho một giấc ngủ nướng mới! Một ngày đầy ắp những cú ngã đập bụng, những pha đứng hình ngơ ngác, nhưng ngập tràn vẻ đẹp hồn nhiên của tạo hóa!",
            "mood": "am_ap"
          },
          {
            "text": "Hiện nay trên toàn thế giới, quần thể loài vẹt Kakapo chỉ còn vỏn vẹn khoảng hai trăm năm mươi cá thể, mỗi chú vẹt đều được các nhà khoa học New Zealand gắn thiết bị theo dõi và chăm sóc từng quả trứng như bảo vật quốc gia! Câu chuyện của Kakapo dạy chúng ta một bài học sâu sắc: Sự ngây thơ không có lỗi, nhưng khi thế giới xung quanh biến đổi quá nhanh, những tâm hồn thuần khiết nhất lại chính là những sinh linh cần được nâng niu và chở che nhiều nhất!",
            "mood": "am_ap"
          },
          {
            "text": "Nếu được gửi một lời nhắn nhủ đến chú vẹt béo Kakapo, bạn sẽ khuyên chú bớt ăn quả rimu hay tập bay nhảy cẩn thận hơn? Hãy để lại bình luận chia sẻ cảm nghĩ của bạn bên dưới nhé!",
            "mood": "hao_hung"
          },
          {
            "text": "Còn bây giờ, chiếc đồng hồ hai mươi tư giờ đang chuẩn bị đưa chúng ta đến với hồ sơ kỳ dị tiếp theo của tập bốn mươi sáu! Một loài động vật bí ẩn đến từ những cánh rừng nhiệt đới Indonesia hoang dã, sở hữu cặp răng nanh kỳ quái mọc ngược đâm xuyên qua cả sống mũi, uốn cong vòng lại và chực chờ đâm thủng chính hộp sọ của nó! Bạn có đoán được sinh vật mang nghịch lý tiến hóa tự sát rùng mình này là loài nào không?",
            "mood": "tram_bi_an"
          }
        ]
      }
    ]
  },
  "shorts": {
    "target_s": 53.0,
    "mood": "hao_hung",
    "text": "[surprise-oh] Quên mất mình không biết bay nhưng vẫn leo tót lên ngọn cây cao hai mươi mét rồi xòe cánh nhảy ùm xuống đập bụng bẹp dí! Đây là Kakapo, loài vẹt nặng nhất thế giới với thể trọng lên tới bốn cân, và cũng là loài vẹt duy nhất trên Trái Đất hoàn toàn quên mất cách bay! Sống hàng triệu năm ở New Zealand không có thú săn mồi, xương ức của gã thoái hóa phẳng lì khiến đôi cánh chỉ còn là vật trang trí. Khi gặp nguy hiểm, gã đứng hình phăng phắc giả làm bụi rêu, nhưng cơ thể lại tỏa ra mùi mật ong thơm phức mời gọi kẻ thù! Ban đêm, gã đi bộ hàng chục cây số, đào hố lòng chảo khuếch đại tiếng kêu vang xa tới năm cây số để gọi bạn tình. Đáng yêu và ngơ ngác vô số tội, hiện cả hành tinh chỉ còn vỏn vẹn khoảng hai trăm năm mươi cá thể được bảo tồn nghiêm ngặt!",
    "title_lines": [
      "QUÊN MÌNH KHÔNG BIẾT BAY",
      "LEO 20M NHẢY ĐẬP BỤNG?!"
    ]
  },
  "seo": {
    "title": "Quên Mình Không Biết Bay: Chú Vẹt Béo 4kg Leo Cây Nhảy Đập Bụng?! | Vẹt Kakapo | Tập 45",
    "hook_paragraph": "Nhật ký 24h đầy tấu hài của Vẹt Kakapo (Strigops habroptilus) — loài vẹt nặng nhất thế giới 4kg quên cách bay, leo ngọn cây 20m nhảy đập bụng, đứng hình giả bụi cây và tiếng gọi bạn tình vang xa 5km!",
    "bullets": [
      "Loài vẹt nặng nhất thế giới (4kg) và duy nhất không biết bay do xương ức phẳng lì",
      "Cơ chế tự vệ 'đứng hình' giả làm bụi rêu nhưng cơ thể tỏa mùi mật ong ngọt ngào",
      "Leo ngọn cây rimu cao 20m ăn quả rồi xòe cánh nhảy dù đập mặt xuống đất",
      "Đào hố lòng chảo khuếch đại tiếng kêu booming vang xa 5km trong đêm tìm bạn tình"
    ],
    "question": "Nếu được nuôi một chú vẹt béo Kakapo, bạn sẽ khuyên chú bớt ăn quả rimu hay mua đệm đỡ cho chú nhảy cây?",
    "next_teaser": "Tập 46: Lợn Hươu Babirusa — loài lợn có cặp răng nanh tự đâm thủng hộp sọ chính mình!",
    "hashtags": ["#VetKakapo", "#Kakapo", "#TheGioiDongVat", "#VeChuyenHoangDa", "#KhoaHoc"],
    "tags": [
      "vet kakapo",
      "kakapo parrot",
      "strigops habroptilus",
      "vet khong biet bay",
      "vet beo 4kg",
      "the gioi dong vat",
      "ve chuyen hoang da",
      "dong vat hai huoc",
      "whiteboard animation"
    ],
    "shorts_title": "Quên mình không biết bay leo cây 20m nhảy đập bụng?! 🦜 #shorts #kakapo",
    "shorts_desc": "Khám phá Vẹt Kakapo — loài vẹt nặng 4kg duy nhất trên Trái Đất không biết bay, leo ngọn cây 20m nhảy dù đập bụng và tiếng gọi bạn tình vang xa 5km!",
    "shorts_tags": ["vet kakapo", "kakapo", "shorts", "the gioi dong vat", "ve chuyen hoang da"]
  }
}

(P / "episode.json").write_text(json.dumps(ep_data, ensure_ascii=False, indent=1), encoding="utf-8")
print("Saved episode.json for Ep 45 successfully!")

