"""
Generate Full-Duration Audio at 1.25x Male Voice (Consistent, Broadcast-Quality, Family-Friendly All Ages)
Episode 4: Thú Mỏ Vịt (Platypus - Ornithorhynchus anatinus) - 6 Full Acts (Target: 8:15 - 9:15 min) + Shorts (Target: 50s)
Matches the Channel Blueprint in docs/ke_hoach_xay_kenh_youtube_the_gioi_dong_vat_whiteboard_animation.md
and TASTE-16, TASTE-41, TASTE-44 (2 Video/Day Schedule).
"""

import sys
import os
import json
import re
import subprocess
import time
from pathlib import Path
from gtts import gTTS

ROOT = Path(__file__).resolve().parents[3]
PROJ = Path(__file__).resolve().parents[1]
AUDIO_DIR = PROJ / "audio"
AUDIO_DIR.mkdir(parents=True, exist_ok=True)

FULL_SCENES = [
    {
        "id": "scene01",
        "title": "Act 1: The Myth-Buster Hook - Cú Sốc Khâu Vá Của Giới Khoa Học Thế Kỷ 18",
        "paragraphs": [
            "Ở tập trước, chúng ta đã cùng nhau bơi ra đại dương bao la để giải mã bí mật đằng sau nụ cười vĩnh cửu của Cá Heo và chiêm ngưỡng những pha húc văng cá mập trắng đầy dũng cảm. Hôm nay, hãy cùng ngòi bút của Vẽ Chuyện Hoang Dã du hành đến những dòng suối trong vắt miền đông nước Úc để gặp gỡ sinh vật kỳ quặc nhất từng tồn tại trên Trái Đất: Thú Mỏ Vịt! Nếu bạn nghĩ mình đã hiểu hết về thế giới động vật, hãy chuẩn bị tinh thần để ngã ngửa trước một kiệt tác chắp vá hài hước nhất của mẹ thiên nhiên!",
            "Câu chuyện bắt đầu vào năm một nghìn bảy trăm chín mươi tám, khi thuyền trưởng John Hunter đóng gói một tiêu bản Thú Mỏ Vịt từ Úc gửi về Bảo tàng Lịch sử Tự nhiên Luân Đôn nước Anh. Khi mở chiếc hộp gỗ ra, nhà sinh vật học lừng danh George Shaw đã sững sờ không thốt nên lời! Ông quả quyết rằng đây chắc chắn là một trò đùa quái ác của các thủy thủ: Một kẻ nào đó đã tinh quái lấy chiếc mỏ của một con vịt khâu dính vào đầu của một con rái cá, rồi gắn thêm chiếc đuôi của một con hải ly!",
            "Để vạch trần trò lừa đảo, tiến sĩ Shaw thậm chí đã cầm một chiếc kéo sắc bén rạch thẳng vào phần gốc mỏ của tiêu bản để tìm đường chỉ khâu! Nhưng càng rạch, ông càng bàng hoàng nhận ra: Không hề có một mũi kim sợi chỉ nào! Chiếc mỏ vịt ấy mọc liền một khối hoàn hảo với hộp sọ của con vật! Cả giới khoa học châu Âu thời bấy giờ rơi vào một cuộc khủng hoảng phân loại học chấn động: Sinh vật này có mỏ vịt, đuôi hải ly, chân màng bơi, nhưng thân lại phủ đầy lông thú ấm áp. Nó là chim, là cá, là thú có vú hay là một sản phẩm nhặt đồ thừa của tạo hóa? Hãy cùng nét vẽ hôm nay khám phá nhé!"
        ]
    },
    {
        "id": "scene02",
        "title": "Act 2: Bảng Chỉ Số Sinh Tồn RPG Stats - Quái Kiệt Chắp Vá Của Mẹ Thiên Nhiên",
        "paragraphs": [
            "Nếu đưa Thú Mỏ Vịt vào bảng xếp hạng siêu anh hùng của thế giới hoang dã, chắc chắn các nhà làm game sẽ phải đau đầu vì bộ chỉ số sinh tồn vượt ngoài mọi quy luật sinh học thông thường! Đầu tiên là chỉ số Độ Kỳ Dị Đột Biến WEIRDNESS MUTATION: Chạm mốc chín trăm chín mươi chín trên một trăm điểm! Đây là loài vật duy nhất trên hành tinh mang đặc điểm của ba lớp sinh vật khác nhau: Đẻ trứng vỏ mềm như loài bò sát, ấp trứng bằng bụng ấm như loài chim, nhưng lại nuôi con bằng sữa ngọt ngào của loài thú có vú!",
            "Thứ hai là chỉ số Giác Quan Điện Trường Sinh Học ELECTRO RECEPTION: Đạt điểm tuyệt đối một trăm trên một trăm! Chiếc mỏ của Thú Mỏ Vịt không hề cứng như sừng của vịt thật, mà mềm mại như da lộn, tích hợp tới bốn mươi nghìn cảm biến điện trường và sáu mươi nghìn thụ thể xúc giác. Dù nhắm nghiền mắt và bịt kín tai khi lặn dưới nước đục, nó vẫn phát hiện chính xác từng xung điện thần kinh phát ra từ nhịp tim của một chú tôm nhỏ đang trốn dưới lớp bùn sâu!",
            "Thứ ba là chỉ số Vũ Khí Cựa Độc Chân Sau VENOM SPUR: Đạt chín mươi lăm trên một trăm điểm! Trong thế giới thú có vú, cực kỳ hiếm có loài nào sở hữu nọc độc tự nhiên. Thế nhưng ở Thú Mỏ Vịt đực, mỗi gót chân sau được trang bị một chiếc cựa sắc nhọn dài mười lăm milimét, nối liền với tuyến độc cực mạnh. Nọc độc này đủ sức hạ gục một chú chó săn và khiến một người đàn ông trưởng thành đau đớn dữ dội suốt nhiều tuần lễ mà không một loại thuốc giảm đau thông thường nào dập tắt được!",
            "Và cuối cùng là chỉ số Nuôi Con Độc Dị MILK SWEAT: Đạt chín mươi tám trên một trăm điểm! Mặc dù là thú có vú nuôi con bằng sữa, nhưng Thú Mỏ Vịt hoàn toàn không có núm vú! Thay vào đó, sữa mẹ được tiết ra trực tiếp từ các tuyến sữa biến đổi qua lỗ chân lông trên da bụng, rỉ ra từng giọt đọng trên các rãnh lông như những hạt mồ hôi để các chú thú mỏ vịt con liếm láp thưởng thức!"
        ]
    },
    {
        "id": "scene03",
        "title": "Act 3: Cơ Chế Sinh Tồn Độc Dị - Mỏ Radar Điện Trường, Đuôi Chứa Mỡ & Phát Sáng Dưới Đèn UV",
        "paragraphs": [
            "Để sinh tồn dưới những dòng suối lạnh buốt và dòng nước cuộn xiết, Thú Mỏ Vịt sở hữu những thiết kế giải phẫu kỳ diệu mà khoa học hiện đại phải thán phục. Thiết kế đầu tiên chính là chiếc mỏ bọc da siêu nhạy cảm. Bạn có biết không: Mỗi khi lặn xuống đáy nước săn mồi, Thú Mỏ Vịt lập tức nhắm chặt cả đôi mắt, khép kín lỗ tai và bịt kín hai lỗ mũi lại! Có nghĩa là nó hoàn toàn mù, điếc và mất khứu giác khi ở dưới nước!",
            "Vậy làm thế nào nó bắt được mồi? Bí mật nằm ở chiếc mỏ thần kỳ hoạt động như một cỗ máy định vị GPS sinh học kép! Khi một con tôm ngoe nguẩy càng dưới đáy suối, cử động đó tạo ra hai tín hiệu đồng thời: Sóng cơ học truyền qua nước và một xung điện trường siêu nhỏ phát ra từ cơ bắp con tôm. Chiếc mỏ thú mỏ vịt tiếp nhận cả hai tín hiệu cùng lúc, rồi não bộ tính toán độ lệch thời gian siêu vi mô giữa sóng điện và sóng cơ để xác định vị trí con mồi chuẩn xác đến từng phần mười milimét!",
            "Thiết kế thứ hai là chiếc đuôi dẹt to bản giống hệt đuôi hải ly. Nhưng thay vì dùng để đập nước cảnh báo như hải ly, chiếc đuôi của Thú Mỏ Vịt thực chất là một kho chứa mỡ di động! Nó có thể tích trữ tới một nửa lượng mỡ dự trữ của toàn bộ cơ thể trong chiếc đuôi này, giúp con vật có đủ năng lượng sống sót qua những mùa đông lạnh giá khan hiếm thức ăn.",
            "Và điều kinh ngạc nhất mới được các nhà khoa học phát hiện gần đây: Khi bạn rọi một chiếc đèn tia cực tím UV vào bộ lông của Thú Mỏ Vịt trong bóng tối, toàn bộ lớp lông màu nâu bùn lập tức phát ra ánh sáng huỳnh quang màu xanh ngọc bích rực rỡ và huyền bí! Cơ chế phát quang sinh học này giúp chúng nhận ra đồng loại trong màn đêm dưới đáy suối mà kẻ săn mồi trên cạn không hề hay biết!"
        ]
    },
    {
        "id": "scene04",
        "title": "Act 4: Cú Bẻ Lái Của Tạo Hóa - Ăn Cơm Bằng Sỏi Đá & Bi Kịch Không Có Dạ Dày",
        "paragraphs": [
            "Đến đây, bạn có thể nghĩ Thú Mỏ Vịt đã là sinh vật hoàn hảo của tự nhiên. Thế nhưng, tạo hóa luôn thích cài cắm những cú bẻ lái bi hài nhất vào phút thứ tư của câu chuyện! Bạn có tin được không: Thú Mỏ Vịt là một trong số cực ít loài thú có vú trên Trái Đất hoàn toàn KHÔNG CÓ DẠ DÀY!",
            "Đúng vậy, bạn không nghe nhầm đâu! Trong quá trình tiến hóa hàng chục triệu năm, các gen chịu trách nhiệm sản xuất axit dạ dày và enzym tiêu hóa pepsin của Thú Mỏ Vịt đã bị xóa sạch hoàn toàn khỏi mã di truyền. Đường tiêu hóa của nó là một đường ống thẳng đuột: Thức ăn từ miệng đi qua thực quản và nối thẳng tắp vào ruột non non nớt mà không hề có chiếc túi dạ dày nào để co bóp hay tiêu hóa thức ăn!",
            "Chưa dừng lại ở đó, Thú Mỏ Vịt trưởng thành còn không hề có một chiếc răng nào trong miệng! Khi sinh ra, con non có những chiếc răng sữa nhỏ xíu, nhưng chỉ vài tuần sau, những chiếc răng này rụng sạch và được thay thế bằng hai phiến sừng thô ráp. Vậy làm thế nào để nó nghiền nát lớp vỏ cứng của những con tôm càng, ốc nước ngọt và ấu trùng côn trùng?",
            "Câu trả lời là một mánh khóe ăn uống có một không hai: Ăn cơm kèm theo sỏi đá! Mỗi khi lặn xuống đáy suối gom tôm tép, Thú Mỏ Vịt tiện thể xúc luôn một vốc sỏi nhỏ và cát thô nhét đầy vào hai túi má phúng phính. Khi ngoi lên mặt nước, nó nằm ngửa thư giãn, dùng cơ hàm đẩy những viên sỏi nghiền nát lớp vỏ giáp xác con mồi như chiếc cối giã gạo, rồi nuốt phần thịt mềm thẳng xuống ruột, sau đó nhổ sỏi đá ra ngoài! Mang trong mình tập hợp những nghịch lý ngớ ngẩn không tưởng như vậy, làm sao loài vật này có thể sống sót qua hàng trăm triệu năm?"
        ]
    },
    {
        "id": "scene05",
        "title": "Act 5: Chiến Binh Cổ Đại Vượt Kỷ Khủng Long & Bí Ẩn 10 Nhiễm Sắc Thể Giới Tính",
        "paragraphs": [
            "Câu trả lời nằm ở sức sống mãnh liệt của một hóa thạch sống thực thụ! Tổ tiên của Thú Mỏ Vịt đã tung tăng bơi lội dưới những dòng suối từ hơn một trăm triệu năm trước, cùng thời kỳ với những hung thần bạo chúa T-Rex và thằn lằn bay khổng lồ của kỷ Creta!",
            "Khi một tiểu hành tinh khổng lồ lao xuống Trái Đất sáu mươi sáu triệu năm trước xóa sổ toàn bộ loài khủng long và đẩy hành tinh vào mùa đông hạt nhân tăm tối, Thú Mỏ Vịt nhờ lối sống bán thủy sinh, ẩn nấp trong các hang đất ngầm sâu tới ba mươi mét dọc bờ suối và ăn các sinh vật đáy nhỏ bé mà bình an vượt qua đại tuyệt chủng!",
            "Đặc biệt, năm hai nghìn không trăm lẻ tám, khi các nhà di truyền học quốc tế giải mã thành công bộ gen của Thú Mỏ Vịt, cả thế giới khoa học lại một lần nữa chấn động! Trong khi con người và hầu hết các loài thú có vú chỉ có hai nhiễm sắc thể giới tính là X và Y để quyết định giới tính nam hay nữ, thì Thú Mỏ Vịt sở hữu tới MƯỜI nhiễm sắc thể giới tính! Con đực có tới năm nhiễm sắc thể X và năm nhiễm sắc thể Y kết nối thành một chuỗi vòng phức tạp!",
            "Bộ gen của nó là một bức tranh ghép hoàn hảo giữa gen động vật có vú, gen chim và gen bò sát: Nó có gen đẻ trứng của loài chim, gen nọc độc tương tự như loài rắn chuông, nhưng lại sở hữu protein sữa của loài thú có vú. Bàn tay của Thú Mỏ Vịt còn có chiếc màng bơi xòe rộng khi bơi dưới nước, nhưng khi bước lên cạn, chiếc màng này tự động cuộn gập lại vào lòng bàn chân để lộ bộ móng vuốt sắc bén giúp nó đào những đường hầm trú ẩn kiên cố bậc nhất thiên nhiên hoang dã!"
        ]
    },
    {
        "id": "scene06",
        "title": "Act 6: Lời Nhắn Nhủ Sinh Thái & Seamless Outro Sang Tập 5: Chim Bồ Nông",
        "paragraphs": [
            "Hành trình khám phá Thú Mỏ Vịt dạy cho chúng ta một bài học sâu sắc về sự kỳ diệu và đa dạng của cuộc sống: Đôi khi những thứ tưởng chừng như chắp vá, kỳ quặc và ngớ ngẩn lại chính là kiệt tác tiến hóa hoàn hảo nhất để thích nghi với môi trường sống khắc nghiệt. Ngày nay, Thú Mỏ Vịt đang phải đối mặt với nguy cơ suy giảm số lượng do biến đổi khí hậu và ô nhiễm nguồn nước tại Úc. Hãy cùng chung tay bảo vệ môi trường và những dòng sông sạch để loài hóa thạch sống đáng yêu này mãi tự do bơi lội dưới làn nước trong xanh nhé!",
            "Và nếu bạn nghĩ một con vật có mỏ vịt, đẻ trứng, tiết sữa qua da và giấu cựa độc ở gót chân đã là kẻ kỳ dị nhất hành tinh, thì ở tập tiếp theo, ngòi bút của chúng ta sẽ vẽ nên một kẻ tham lam vô đối trên bầu trời! Một loài chim sở hữu chiếc mỏ như một chiếc túi rác không đáy: Cứ thấy thứ gì chuyển động là cố nuốt chửng vào bụng, từ chim bồ câu, cá lớn, capybara cho đến cả máy quay phim của các nhiếp ảnh gia: Đó chính là Chim Bồ Nông! Hãy nhấn Đăng Ký kênh Vẽ Chuyện Hoang Dã ngay để không bỏ lỡ tập phim siêu hài hước vào ngày mai nhé!"
        ]
    },
    {
        "id": "shorts",
        "title": "Shorts: 3 Sự Thật Ngã Ngửa Về Thú Mỏ Vịt Kỳ Quặc",
        "paragraphs": [
            "Đừng để vẻ ngoài ngộ nghĩnh này đánh lừa bạn! Đây là ba sự thật gây sốc về Thú Mỏ Vịt, sinh vật chắp vá kỳ dị nhất hành tinh!",
            "Sự thật thứ nhất: Khi lần đầu nhìn thấy tiêu bản Thú Mỏ Vịt năm một nghìn bảy trăm chín mươi tám, các nhà khoa học châu Âu tưởng ai đó chơi khăm lấy mỏ vịt khâu vào mình rái cá, đến mức lấy kéo rạch tìm đường chỉ khâu!",
            "Sự thật thứ hai: Thú mỏ vịt hoàn toàn không có dạ dày và không có răng! Nó bắt buộc phải nhét sỏi đá vào túi má để nghiền nát tôm cua rồi nuốt thẳng xuống ruột non!",
            "Sự thật thứ ba: Nó vừa đẻ trứng như chim, vừa có cựa độc ở gót chân như rắn, vừa nuôi con bằng sữa tiết ra từ da bụng như mồ hôi, lại còn phát sáng màu xanh ngọc bích dưới ánh đèn tia cực tím!",
            "Bấm ngay vào kênh Vẽ Chuyện Hoang Dã để xem bản Full siêu thú vị nhé!"
        ]
    }
]


def synthesize_scene_male_125x(item: dict):
    sid = item["id"]
    title = item["title"]
    paragraphs = item["paragraphs"]
    out_wav = AUDIO_DIR / f"{sid}.wav"

    print(f"\n=======================================================")
    print(f"[VOICE MALE 1.25x - EP04] Synthesizing {sid}: {title}")
    print(f"Paragraphs: {len(paragraphs)}")

    part_wavs = []
    for idx, p in enumerate(paragraphs):
        p_clean = p.strip().replace("\n", " ")
        tmp_mp3 = AUDIO_DIR / f"{sid}_part{idx}.mp3"
        part_wav = AUDIO_DIR / f"{sid}_part{idx}.wav"

        tts = gTTS(text=p_clean, lang="vi", slow=False)
        tts.save(str(tmp_mp3))

        af_chain = (
            "rubberband=pitch=0.82:tempo=1.25,"
            "highpass=f=75,lowpass=f=13500,"
            "equalizer=f=150:width_type=o:w=1.0:g=2.5,"
            "equalizer=f=3200:width_type=o:w=1.0:g=2.0,"
            "acompressor=threshold=-16dB:ratio=3:attack=5:release=50,"
            "volume=1.25"
        )
        subprocess.run(
            [
                "ffmpeg", "-y", "-i", str(tmp_mp3),
                "-filter:a", af_chain,
                "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le",
                str(part_wav),
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True,
        )

        part_wavs.append(part_wav)
        tmp_mp3.unlink(missing_ok=True)
        print(f"  Part {idx+1}/{len(paragraphs)} mastered.")

    part_durations = []
    for pw in part_wavs:
        p_cmd = [
            "ffprobe", "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            str(pw),
        ]
        p_dur = float(subprocess.check_output(p_cmd, text=True).strip())
        part_durations.append(round(p_dur, 3))

    parts_meta = AUDIO_DIR / f"{sid}_parts_duration.json"
    parts_meta.write_text(json.dumps(part_durations, indent=2), encoding="utf-8")

    concat_txt = AUDIO_DIR / f"{sid}_concat.txt"
    with open(concat_txt, "w", encoding="utf-8") as f:
        for pw in part_wavs:
            p_str = str(pw.resolve()).replace("\\", "/")
            f.write(f"file '{p_str}'\n")

    subprocess.run(
        [
            "ffmpeg", "-y", "-f", "concat", "-safe", "0",
            "-i", str(concat_txt),
            "-c", "copy",
            str(out_wav),
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=True,
    )

    concat_txt.unlink(missing_ok=True)
    for pw in part_wavs:
        pw.unlink(missing_ok=True)

    probe_cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(out_wav),
    ]
    dur_sec = float(subprocess.check_output(probe_cmd, text=True).strip())
    dur_ms = int(round(dur_sec * 1000))
    print(f"[SUCCESS] {sid}.wav duration: {dur_sec:.2f}s ({dur_ms}ms, parts={part_durations})")
    return dur_sec


def main():
    target_ids = [arg for arg in sys.argv[1:] if not arg.startswith("-")]
    scenes_to_run = [s for s in FULL_SCENES if s["id"] in target_ids] if target_ids else FULL_SCENES

    t0 = time.time()
    total_long_sec = 0.0
    for item in scenes_to_run:
        d = synthesize_scene_male_125x(item)
        if item["id"] != "shorts":
            total_long_sec += d

    print("\n=======================================================")
    print(f"EPISODE 4 AUDIO SYNTHESIS COMPLETE in {time.time() - t0:.1f}s!")
    print(f"Total Long-form Voiceover Duration: {total_long_sec:.2f}s ({total_long_sec/60:.2f} min)")
    print("=======================================================")


if __name__ == "__main__":
    main()
