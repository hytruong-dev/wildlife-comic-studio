"""
Generate Full-Duration Audio at 1.25x Male Voice (Consistent, Broadcast-Quality, Family-Friendly All Ages)
Episode 2: Rái Cá Biển (Sea Otter - Enhydra lutris) - 6 Full Acts (Target: 8:30 - 9:30 min) + Shorts (Target: 50s)
Matches the 30-day channel blueprint in docs/ke_hoach_xay_kenh_youtube_the_gioi_dong_vat_whiteboard_animation.md
and TASTE-16 (All Ages Family-Friendly Edutainment).
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
        "title": "Act 1: The Myth-Buster Hook - Cú Lừa Đáng Yêu Nhất Đại Dương",
        "target_sec": 80,
        "paragraphs": [
            "Ở tập trước, chúng ta đã diện kiến Lửng Mật, gã Chí Phèo mười hai kilôgam trên thảo nguyên châu Phi khiến cả bầy sư tử phải né đường. Nhưng bạn có biết Lửng Mật còn có một người anh em họ hàng ruột thịt cùng thuộc gia tộc nhà Chồn đã quyết định rời bỏ đất liền để xuống làm bá chủ đại dương? Khi nhắc đến Rái Cá Biển, hàng triệu người trên thế giới lập tức nghĩ ngay đến hình ảnh những cục bông tròn xoe, nằm ngửa bồng bềnh trên mặt sóng, hai bàn chân trước áp lên má nũng nịu và nắm chặt tay nhau khi ngủ như biểu tượng vĩnh cửu của tình yêu lãng mạn.",
            "Thế nhưng hãy khoan vội tan chảy! Đằng sau gương mặt ngây thơ như thú nhồi bông ấy lại là một bậc thầy thực dụng, một kẻ thu phí đường biển khét tiếng với cái tên khoa học là Enhydra lutris. Thực tế, việc rái cá biển nắm tay nhau khi ngủ hoàn toàn không phải vì lãng mạn ngôn tình, mà là một sợi dây neo sinh tồn lạnh lùng! Vì ngủ ngửa trên mặt biển đầy sóng gió, nếu không nắm tay nhau thành bè hoặc tự trói mình vào đám rong biển tảo bẹ khổng lồ, dòng hải lưu sẽ cuốn chúng trôi tuột ra khơi xa, lạc mất bãi thức ăn hoặc trôi thẳng vào hàm của cá voi sát thủ! Và khi cơn đói ập đến, cục bông đáng yêu này sẵn sàng lột xác thành một gã giang hồ cướp cạn tinh quái bậc nhất đại dương!"
        ]
    },
    {
        "id": "scene02",
        "title": "Act 2: Bảng Chỉ Số Sinh Tồn RPG Stats - Thánh Ăn Vạ Đội Lốt Thú Nhồi Bông",
        "target_sec": 95,
        "paragraphs": [
            "Nếu đưa Rái Cá Biển vào bảng xếp hạng nhân vật trong thế giới tự nhiên, bạn sẽ ngỡ ngàng trước bộ chỉ số sinh tồn vừa siêu phàm vừa lầy lội đến khó tin của loài thú biển nặng tới bốn mươi lăm kilôgam này. Đầu tiên là chỉ số Ngụy Trang Đáng Yêu CUTENESS: Đạt điểm tuyệt đối một trăm trên một trăm! Với đôi mắt tròn đen láy, bộ ria mép rung rinh và tuyệt chiêu xoa mặt làm duyên, Rái Cá Biển dễ dàng đánh lừa chín mươi chín phần trăm nhân loại, khiến ai nhìn vào cũng tưởng đây là sinh vật hiền lành nhất hành tinh.",
            "Thứ hai là chỉ số Phòng Thủ Giáp Lông FUR ARMOR: Chạm mốc chín mươi lăm trên một trăm điểm! Khác với cá voi hay hải cẩu có lớp mỡ dày dưới da, Rái Cá Biển hoàn toàn không có mỡ. Thay vào đó, tạo hóa trang bị cho nó bộ lông dày đặc nhất thế giới động vật với một trăm sáu mươi nghìn sợi lông trên mỗi centimet vuông da, tạo thành một chiếc áo phao không khí cách nhiệt hoàn hảo giữa vùng biển Bắc Thái Bình Dương lạnh buốt không độ C.",
            "Thứ ba là chỉ số Trí Thông Minh và Chế Tạo Công Cụ IQ: Đạt chín mươi hai trên một trăm điểm. Đây là một trong số cực ít loài thú biển biết sử dụng búa đá điêu luyện như thợ cơ khí để đập vỡ những lớp vỏ cứng như bê tông cốt thép dưới đáy biển sâu.",
            "Và cuối cùng là chỉ số Độ Lầy Lội và Mánh Khóe Giang Hồ TRICKERY: Phá vỡ mọi thang đo với chín trăm chín mươi chín điểm! Từ việc cướp trắng bữa ăn của đồng loại, bắt giữ rái cá con làm con tin để đòi tiền chuộc bằng hải sản, cho đến phi vụ cướp ván lướt sóng của con người, không một chiêu trò tinh quái nào mà loài vật này chưa từng thực hiện!"
        ]
    },
    {
        "id": "scene03",
        "title": "Act 3: Giải Phẫu Sinh Học - Áo Phao 1 Triệu Sợi Lông & Túi Thần Kỳ Doraemon",
        "target_sec": 100,
        "paragraphs": [
            "Để hiểu vì sao Rái Cá Biển lại phải sống cuộc đời tinh quái đến vậy, chúng ta phải giải phẫu ba thiết kế sinh học độc nhất vô nhị trên cơ thể của nó. Thiết kế đầu tiên chính là bộ lông giữ kỷ lục thế giới. Nếu trên toàn bộ da đầu của một con người chỉ có khoảng một trăm nghìn sợi tóc, thì chỉ cần một khoảng da nhỏ bằng con tem thư trên lưng Rái Cá Biển đã chứa tới hơn một triệu sợi lông! Các sợi lông này đan chéo vào nhau như mái ngói, khóa chặt một lớp bọt khí ấm áp sát da, khiến nước biển băng giá không bao giờ chạm nổi vào da thật của chúng. Vì thế, bạn sẽ thấy rái cá dành tới bốn tiếng mỗi ngày chỉ để cào lông, thổi khí và vắt nước như một thợ giặt chuyên nghiệp.",
            "Thiết kế thứ hai là lò phản ứng trao đổi chất đốt năng lượng khủng khiếp. Vì không có mỡ giữ nhiệt, cơ thể Rái Cá Biển phải tự đốt năng lượng nhanh gấp ba lần các loài thú có vú cùng kích cỡ để giữ ấm ở mức ba mươi tám độ C. Cái giá phải trả là một chiếc bụng không đáy: Mỗi ngày, nó bắt buộc phải ăn lượng hải sản khổng lồ tương đương hai mươi lăm đến ba mươi phần trăm trọng lượng cơ thể! Hãy thử tưởng tượng, nếu một người nặng sáu mươi kilôgam ăn theo chế độ của rái cá, người đó sẽ phải nuốt hết mười tám kilôgam tôm hùm, cua hoàng đế, nhím biển và bào ngư mỗi ngày!",
            "Và thiết kế thứ ba kỳ diệu nhất: Chiếc túi thần kỳ Doraemon nằm ngay dưới nách! Dưới hai nách chân trước của Rái Cá Biển có hai nếp da chùng tự nhiên tạo thành chiếc túi đeo chéo. Túi bên trái dùng để nhét đầy thức ăn gom được dưới đáy biển đem lên mặt nước. Còn túi bên phải được nó dùng để cất giữ một viên đá tảng sắc cạnh yêu thích suốt nhiều năm liền! Khi nổi lên mặt sóng, nó nằm ngửa biến chiếc bụng thành cái đe, rút búa đá từ dưới nách ra và đập nát vỏ trai, vỏ bào ngư với tốc độ bốn mươi lăm nhát búa chỉ trong mười lăm giây!"
        ]
    },
    {
        "id": "scene04",
        "title": "Act 4: Cú Bẻ Lái Của Tạo Hóa - Mánh Khóe Bắt Cóc Con Tin Đòi Chuộc Đồ Ăn",
        "target_sec": 95,
        "paragraphs": [
            "Chính áp lực sinh tử phải kiếm đủ hơn mười kilôgam hải sản cao cấp mỗi ngày nếu không muốn bị hạ thân nhiệt đã đẩy nhiều gã rái cá biển vào con đường tội phạm đường thủy đầy bi hài! Khi nguồn thức ăn khan hiếm hoặc khi quá lười phải lặn xuống vùng nước sâu nín thở suốt năm phút, những con rái cá đực to xác đã phát minh ra một mánh khóe tống tiền khiến các nhà sinh vật học biển tại vịnh Monterey nước Mỹ phải bật cười kinh ngạc.",
            "Mánh khóe đó được giới khoa học gọi là chiến thuật bắt giữ con tin đòi chuộc hải sản! Bạn biết đấy, lông của rái cá con mới sinh chứa đầy không khí nên chúng nổi phềnh trên mặt nước như một chiếc phao cứu sinh, hoàn toàn không thể tự lặn xuống nước được. Mỗi khi đi săn, rái cá mẹ phải quấn con non vào đám rong biển trên mặt nước rồi mới lặn xuống đáy biển tìm cua và bào ngư.",
            "Chỉ chờ có thế, gã rái cá đực lười biếng liền âm thầm bơi tới, vòng hai tay ôm chặt lấy chú rái cá con đang nổi bồng bềnh và giữ làm con tin! Khi rái cá mẹ vừa ngoi lên mặt nước với một con cua béo ngậy hay con bào ngư to tướng trên tay, gã bắt cóc liền dìm nhẹ rái cá con xuống mặt nước khiến chú nhóc kêu chít chít cầu cứu.",
            "Thương con đứt ruột, bà mẹ rái cá không còn cách nào khác đành phải bơi tới, ngậm ngùi giao nộp toàn bộ phần thức ăn vừa vất vả săn được cho kẻ bắt cóc! Ngay khi nhận được con cua tiền chuộc, gã rái cá đực lập tức thả con tin ra rồi ung dung nằm ngửa vừa chén hải sản vừa vẫy đuôi khoái chí! Thậm chí những lúc đang đánh nhau, nếu thấy đối thủ cầm hòn đá búa xịn hơn, chúng còn cắn vào mũi nhau chỉ để cướp bằng được viên đá đẹp về tay mình!"
        ]
    },
    {
        "id": "scene05",
        "title": "Act 5: Vệ Binh Rừng Tảo Bẹ & Huyền Thoại Hải Tặc Cướp Ván Lướt Sóng 841",
        "target_sec": 95,
        "paragraphs": [
            "Dù lắm chiêu trò và lầy lội là thế, nhưng nếu thiếu đi Rái Cá Biển, toàn bộ hệ sinh thái đại dương ven bờ sẽ lập tức sụp đổ! Dưới đáy biển Thái Bình Dương có những khu rừng tảo bẹ khổng lồ cao tới hàng chục mét, là ngôi nhà chung của hàng trăm loài cá và cũng là lá phổi xanh hấp thụ khí nhà kính mạnh gấp nhiều lần rừng nhiệt đới. Kẻ thù nguy hiểm nhất của rừng tảo bẹ chính là đội quân Nhím Biển Tím với hàng triệu chiếc gai nhọn hoắt.",
            "Khi không có thiên địch kiểm soát, đàn nhím biển sẽ bò tràn lan như một đội quân zombie dưới đáy biển, gặm cụt toàn bộ gốc tảo bẹ và biến khu rừng xanh tốt thành một vùng sa mạc đá chết chóc. Và vị cứu tinh duy nhất dám ăn thịt lũ nhím biển đầy gai nhọn ấy chính là Rái Cá Biển! Chúng dùng búa đá đập vỡ lớp vỏ gai, chén sạch hàng ngàn con nhím biển mỗi tuần. Thú vị hơn, ăn nhiều nhím biển tím đến mức toàn bộ bộ xương và hàm răng của nhiều con rái cá biển chuyển hẳn sang màu tím biếc!",
            "Không chỉ làm bá chủ dưới đáy biển, Rái Cá Biển còn chẳng hề ngán con người! Nổi tiếng nhất thế giới là cô rái cá biển năm tuổi mang số hiệu tám bốn một tại vùng biển Santa Cruz, bang California. Cô nàng tám bốn một này đã trở thành một hải tặc thực thụ khi liên tục bơi ra chặn đầu các vận động viên lướt sóng, nhe răng dọa nạt đuổi họ xuống nước rồi ngang nhiên leo lên chiếm đoạt những tấm ván lướt sóng đắt tiền để nằm phơi nắng!",
            "Suốt cả mùa hè, cảnh sát biển và các chuyên gia cứu hộ động vật hoang dã đã mang lưới vây bắt hàng chục lần, nhưng cô rái cá tám bốn một luôn dùng trí thông minh đỉnh cao để lặn ngụp né lưới, thậm chí còn nhảy lên chính ván trượt của đội vây bắt để trêu ngươi trước sự reo hò cổ vũ của hàng triệu cư dân mạng toàn cầu!"
        ]
    },
    {
        "id": "scene06",
        "title": "Act 6: Bài Học Đại Dương & Seamless Outro Sang Tập 3: Cá Heo",
        "target_sec": 65,
        "paragraphs": [
            "Câu chuyện về Rái Cá Biển một lần nữa cho chúng ta thấy sự kỳ diệu và hài hước của mẹ thiên nhiên: Không có sinh vật nào hoàn toàn là thiên thần, và cũng chẳng có ai hoàn toàn là kẻ xấu. Đằng sau những mánh khóe cướp đồ ăn hay chiếm ván lướt sóng dở khóc dở cười ấy là cuộc vật lộn sinh tồn không ngừng nghỉ giữa vùng biển lạnh giá, đồng thời chính chiếc bụng đói không đáy của Rái Cá Biển lại là lá chắn bảo vệ cả một hệ sinh thái rừng tảo bẹ đại dương xanh tươi.",
            "Thế nhưng, nếu bạn nghĩ những màn cướp bóc thức ăn của Rái Cá Biển đã là đỉnh cao của sự tinh quái dưới biển khơi thì hãy chuẩn bị tinh thần cho tập tiếp theo! Bởi vì ngoài khơi xa kia, có một loài sinh vật luôn xuất hiện trong phim hoạt hình với nụ cười thân thiện, thông minh và hay cứu người chết đuối... nhưng thực chất lại là băng đảng giang hồ đáng sợ bậc nhất đại dương: Đó chính là Cá Heo! Chúng lập hội bắt nạt cá mập, và thậm chí còn chuyền tay nhau những con cá nóc kịch độc như chơi bóng chuyền để tận hưởng cảm giác lâng lâng! Hãy bấm đăng ký kênh ngay để không bỏ lỡ bộ mặt thật của loài Cá Heo trong Tập ba nhé!"
        ]
    },
    {
        "id": "shorts",
        "title": "Shorts: 3 Sự Thật Ngã Ngửa Về Rái Cá Biển",
        "target_sec": 50,
        "paragraphs": [
            "Đừng để gương mặt tròn xoe đáng yêu này đánh lừa bạn! Đây là ba sự thật ngã ngửa về Rái Cá Biển, người anh em họ hàng ruột dưới đại dương của Lửng Mật!",
            "Sự thật thứ nhất: Rái Cá Biển nắm tay nhau khi ngủ không phải vì tình yêu lãng mạn, mà là dây neo chống trôi dạt! Và dưới nách của chúng có một chiếc túi da thần kỳ như túi Doraemon để cất giấu viên đá búa gia truyền suốt nhiều năm!",
            "Sự thật thứ hai: Vì phải ăn lượng hải sản bằng một phần tư cơ thể mỗi ngày để giữ ấm, những gã rái cá đực lười biếng chuyên giở trò bắt giữ rái cá con trên mặt nước làm con tin, ép rái cá mẹ phải nộp cua và bào ngư làm tiền chuộc thì mới chịu thả!",
            "Sự thật thứ ba: Cô rái cá số tám bốn một ở Mỹ từng một mình cướp hàng chục tấm ván lướt sóng của vận động viên và trêu ngươi cả đội cảnh sát biển! Vừa là thánh ăn vạ lầy lội, vừa là vệ binh ăn nhím biển giải cứu rừng tảo bẹ, đó chính là Rái Cá Biển!"
        ]
    }
]


def synthesize_scene_male_125x(item: dict):
    sid = item["id"]
    title = item["title"]
    paragraphs = item["paragraphs"]
    out_wav = AUDIO_DIR / f"{sid}.wav"

    print(f"\n=======================================================")
    print(f"[VOICE MALE 1.25x - EP02] Synthesizing {sid}: {title}")
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
    print(f"EPISODE 2 AUDIO SYNTHESIS COMPLETE in {time.time() - t0:.1f}s!")
    print(f"Total Long-form Voiceover Duration: {total_long_sec:.2f}s ({total_long_sec/60:.2f} min)")
    print("=======================================================")


if __name__ == "__main__":
    main()
