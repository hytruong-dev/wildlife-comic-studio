"""
Generate Full-Duration Audio at 1.25x Male Voice (Consistent, Broadcast-Quality, Zero Rate Limits)
Episode 1: Lửng Mật (Honey Badger) - 6 Full Acts (Target: 8:30 - 9:30 min) + Shorts (Target: 50s)
Matches the 30-day channel blueprint in docs/ke_hoach_xay_kenh_youtube_the_gioi_dong_vat_whiteboard_animation.md
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
        "title": "Act 1: The Myth-Buster Hook - Gã Chí Phèo Số Một Hành Tinh",
        "target_sec": 75,
        "paragraphs": [
            "Bạn nghĩ ai mới thực sự là bá chủ tối cao của thảo nguyên hoang dã châu Phi? Là chúa sơn lâm sư tử với tiếng gầm rung chuyển cả núi rừng đại ngàn? Là đàn linh cẩu tàn nhẫn và tham lam với số lượng áp đảo? Hay những gã khổng lồ hộ pháp như voi rừng và tê giác hai sừng? Quên tất cả những điều đó đi! Trong từ điển sinh tồn của thế giới hoang dã, có một sinh vật kỳ dị chỉ cao chưa đầy ba mươi centimet, nặng vỏn vẹn mười hai kilôgam, nhưng lại khiến cả một bầy sư tử nhìn thấy từ đằng xa cũng phải toát mồ hôi hột, tự động né sang một bên đường.",
            "Giới khoa học đặt tên cho nó là Mellivora capensis. Còn trên giang hồ của muôn loài hoang dã, nó được phong tặng danh hiệu kẻ Chí Phèo số một hành tinh: Lửng Mật! Sách Kỷ lục Guinness thế giới từng vinh danh nó là sinh vật không biết sợ nhất hành tinh. Một gã lùn tịt với bộ lông hai màu đen trắng tương phản, dáng đi lững thững khệnh khạng đầy vẻ bất cần đời. Sư tử nặng gấp mười lăm lần nhưng không bao giờ muốn dây vào. Vì sao ư? Đánh nhau với Lửng Mật là mất cả tiếng đồng hồ vật lộn, rách môi, mẻ vuốt, chỉ để đổi lấy một miếng thịt dai nhách đầy mùi hôi hám! Và nếu bạn lỡ đụng vào nó, nó sẽ đuổi theo bạn tới cùng trời cuối đất để trả thù!"
        ]
    },
    {
        "id": "scene02",
        "title": "Act 2: Bảng Chỉ Số Sinh Tồn RPG Stats - Nhân Vật Lỗi Game Của Tự Nhiên",
        "target_sec": 95,
        "paragraphs": [
            "Nếu đưa Lửng Mật vào một tựa game nhập vai thế giới mở sinh tồn, chắc chắn các nhà phát triển game sẽ bị cộng đồng người chơi khiếu nại kịch liệt vì đã tạo ra một nhân vật quá sức mất cân bằng, phá vỡ mọi quy luật vật lý. Chúng ta hãy cùng bóc tách bảng chỉ số sinh tồn có một không hai của gã chiến binh này. Đầu tiên là chỉ số Sức Mạnh Thể Chất STR: Đạt tám mươi lăm trên một trăm điểm. Dưới lớp lông dày cộp như thảm gai là hệ thống bó cơ nén đặc với mật độ khủng khiếp, giúp Lửng Mật có thể kéo lê một xác linh dương nặng gấp ba lần trọng lượng cơ thể nó đi qua hàng cây số thảo nguyên gập ghềnh.",
            "Thứ hai là chỉ số Phòng Thủ DEF: Chạm mốc tuyệt đối chín mươi chín điểm! Nó khoác lên mình một lớp giáp cao su di động dày tới sáu milimét, kháng cự hoàn toàn từ răng nanh của sư tử, nọc độc chết người của bọ cạp đến cả những mũi giáo sắc nhọn bằng kim loại của thổ dân châu Phi. Mọi đòn tấn công khi chém vào lưng nó đều bị trượt đi như chém vào lốp xe tải.",
            "Thứ ba là chỉ số Trí Thông Minh IQ: Đạt chín mươi điểm. Đây hoàn toàn không phải một kẻ hữu dũng vô mưu, mà là một thiên tài bẻ khóa, chế tạo công cụ và tư duy chiến thuật sinh tồn đỉnh cao. Tiếp theo là Độ Bền Bỉ và Lì Đòn TENACITY: Phá vỡ luôn mọi thang đo với chín trăm chín mươi chín điểm! Trong từ điển của Lửng Mật, không có nút đầu hàng và càng không có khái niệm quay đầu bỏ chạy.",
            "Và chỉ số cuối cùng chấn động nhất: Cảm Giác Sợ Hãi FEAR: Không điểm tròn trĩnh! Các nhà sinh vật học hàng đầu đã chứng minh rằng hạch hạnh nhân trong não bộ của Lửng Mật dường như đã bị tạo hóa tháo dỡ hoàn toàn khỏi cơ thể, khiến nó không hề có phản xạ sợ hãi trước bất kỳ nguy hiểm nào trên trần đời!"
        ]
    },
    {
        "id": "scene03",
        "title": "Act 3: Cơ Chế Sinh Tồn Độc Dị - Áo Giáp Cao Su & Lưỡi Hái Đào Hầm",
        "target_sec": 115,
        "paragraphs": [
            "Điều gì đã giúp một sinh vật nhỏ bé sống sót và ngạo nghễ bước đi giữa chốn thảo nguyên đầy rẫy thú dữ ăn thịt? Bí mật nằm ở ba cơ chế giải phẫu kỳ dị bậc nhất mà mẹ thiên nhiên ưu ái ban tặng cho nó. Cơ chế thứ nhất chính là lớp da cao su đàn hồi cực kỳ lỏng lẻo. Lớp da của Lửng Mật dày hơn cả da trâu mộng trưởng thành, nhưng điều kỳ lạ là nó không hề dính chặt vào các mô cơ bắp bên dưới mà lỏng lẻo như một chiếc áo khoác da quá khổ.",
            "Hãy hình dung tình huống sinh tử này: Khi một con báo hoa mai hay linh cẩu châu Phi ngoạm chặt hàm răng vào gáy Lửng Mật và ngỡ rằng con mồi đã nằm gọn trong tay, điều ma quỷ xảy ra: Lửng Mật có thể tự do xoay người một trăm tám mươi độ ngay bên trong chính lớp da của mình, rồi quay ngoắt bộ hàm sắc nhọn cắn trả thẳng vào mũi và mắt của kẻ săn mồi! Cú phản công bất ngờ, tàn nhẫn và đau đớn đến thấu xương khiến bất kỳ con báo nào cũng phải hoảng loạn nhả ra ngay lập tức!",
            "Cơ chế thứ hai là đôi bàn chân trang bị móng vuốt lưỡi hái trước ngực. Mỗi ngón chân trước của Lửng Mật sở hữu chiếc móng dài hơn năm centimet, cong vút và cứng như mũi khoan thép tôi. Nó có thể xới tung tổ mối cứng như khối bê tông chỉ trong vài phút, hay đào sâu vào lòng đất tạo hang trú ẩn kiên cố nhanh hơn một người khỏe mạnh dùng xẻng xúc đất. Còn bộ hàm của nó đủ khỏe để cắn vỡ cả mai rùa dày, nghiền nát xương con mồi ngọt xớt như nhai kẹo giòn.",
            "Và cơ chế thứ ba là vũ khí phòng vệ hóa học độc môn phía sau đuôi. Lửng Mật sở hữu một túi xạ hương đặc biệt có thể đảo ngược ra ngoài, phun ra luồng khí gas thối nồng nặc đến nghẹt thở. Luồng khí này không chỉ xua đuổi bầy ong vò vẽ hung hãn khi nó cướp tổ mật, mà còn làm tê liệt khứu giác siêu nhạy của bầy thú săn mồi lớn, khiến chúng buồn nôn, cay mắt và buộc phải tháo chạy trong sự ức chế tột cùng!"
        ]
    },
    {
        "id": "scene04",
        "title": "Act 4: Cú Bẻ Lái Của Tạo Hóa - Kẻ Nghiện Nọc Độc & Đột Biến Thần Kinh",
        "target_sec": 105,
        "paragraphs": [
            "Thế nhưng tất cả những vũ khí trên vẫn chưa là gì so với thực đơn ăn uống điên rồ và kỳ quặc bậc nhất hành tinh của gã giang hồ này. Lửng Mật nổi tiếng là kẻ nghiện ăn nọc độc tự nhiên. Món ăn khoái khẩu của nó là những loài rắn chết chóc nhất: Rắn phì châu Phi, rắn hổ mang thổi nọc và cả chúa tể rắn hổ mang! Bạn có biết: Rắn chiếm tới hơn một phần tư khẩu phần ăn hằng ngày của nó, và một giọt nọc độc của rắn phì đủ để làm tan rữa tế bào cơ, giết chết mười lăm người trưởng thành trong đau đớn tột cùng chỉ sau ít phút.",
            "Vậy điều gì sẽ xảy ra khi một con rắn hổ mang khổng lồ cắn ngập đôi răng nanh đầy nọc độc thần kinh thẳng vào mặt của Lửng Mật? Liệu kẻ liều lĩnh này có phải trả giá bằng cả mạng sống cho sự ngông cuồng của mình không? Câu trả lời là một cú bẻ lái kinh điển của tiến hóa sinh học làm giới khoa học ngỡ ngàng!",
            "Các nhà di truyền học phát hiện ra rằng, các thụ thể nicotinic acetylcholine trong hệ thần kinh của Lửng Mật đã trải qua đột biến phân tử sau hàng triệu năm đối đầu sinh tử với loài rắn. Đột biến này hoạt động như một lớp áo giáp phân tử kiên cố, khiến độc tố thần kinh cực mạnh của rắn không thể bám vào để làm tê liệt hệ cơ quan hô hấp của nó! Nọc độc rắn khi vào máu nó chẳng khác nào một liều thuốc mê liều cao.",
            "Khi bị rắn hổ mang cắn trúng, nọc độc vẫn ngấm vào tuần hoàn máu. Lúc này, Lửng Mật sẽ từ từ lảo đảo, lăn đùng ra đất và rơi vào trạng thái hôn mê sâu giống hệt như một gã say vừa uống cạn một chum rượu mạnh. Toàn thân nó mềm nhũn, tim đập chậm lại suốt hai đến ba tiếng đồng hồ khiến kẻ thù tưởng nó đã chết chắc. Thế nhưng khi men say nọc độc tan hết và gan trung hòa xong độc chất, Lửng Mật bỗng mở to mắt, đứng dậy lắc đầu rũ lông tỉnh queo như vừa ngủ trưa dậy, rồi thản nhiên cúi xuống nhai nốt nửa con rắn còn lại như một món ăn vặt ngon lành! Thậm chí nó còn khoái chí liếm mép như vừa thưởng thức xong một bữa tiệc hoàng gia!"
        ]
    },
    {
        "id": "scene05",
        "title": "Act 5: Đại Chiến Thiên Nhiên & Bậc Thầy Vượt Ngục Khét Tiếng Stoffel",
        "target_sec": 105,
        "paragraphs": [
            "Bên cạnh thân thể dẻo dai và khả năng kháng độc vô song, trí thông minh của Lửng Mật mới thực sự là thứ khiến các nhà động vật học trên thế giới phải ngả mũ thán phục. Minh chứng sống động nhất cho trí tuệ siêu phàm này chính là chú lửng mật Stoffel tại Trung tâm Phục hồi Hoang dã Moholoholo ở Nam Phi. Stoffel nổi tiếng toàn cầu đến mức được đài truyền hình BBC của Anh làm riêng một bộ phim tài liệu về những phi vụ vượt ngục không tưởng của nó.",
            "Ban đầu, các chuyên gia nhốt Stoffel trong một khu chuồng rào tường bê tông cao lút đầu người. Bạn nghĩ bức tường bê tông cao sẽ giam giữ được nó? Stoffel đã dùng chân cào đất bùn, nặn thành từng viên bi đất tròn to tướng rồi đẩy chúng vào góc tường, xếp chồng lên nhau thành một gò đất cao để nhảy vọt qua rào trốn thoát! Khi các nhân viên dọn sạch bùn đất, Stoffel đi gom những cành cây khô, dựng đứng tựa vào tường làm thang leo. Họ dọn sạch cành cây, nó liền hợp sức lăn những tảng đá lớn lại. Nó thậm chí còn trộm cả chổi quét sân của nhân viên để làm đòn bẩy vượt rào!",
            "Và khi chuồng bị dọn nhẵn thín không còn lấy một viên sỏi, Stoffel thậm chí đã làm quen với một con lửng mật cái cùng phòng, dụ dỗ con cái đứng sát góc tường để nó trèo lên lưng con cái phóng vọt ra ngoài! Và điều hài hước nhất là mục đích vượt ngục của nó: Không phải để tìm đường về với rừng sâu, mà là xông thẳng vào chuồng bầy sư tử kế bên để khiêu chiến và trêu chọc chúa sơn lâm!",
            "Ngay cả khi bị ba con sư tử đực to lớn bao vây nghẹt thở, Lửng Mật tuyệt đối không bao giờ lùi bước. Nó xù dựng toàn bộ lông lưng, gầm rít dữ dội, phun túi xạ hôi thối và lao thẳng vào giữa bầy sư tử khiến các chúa tể thảo nguyên cũng phải e dè nhượng bộ vì nhận ra cái giá phải trả quá đắt để đổi lấy một bữa ăn dai nhách! Đây chính là đẳng cấp của kẻ giang hồ lỳ lợm nhất thế giới tự nhiên!"
        ]
    },
    {
        "id": "scene06",
        "title": "Act 6: Bài Học Sinh Tồn & Seamless Outro Sang Rái Cá Biển",
        "target_sec": 60,
        "paragraphs": [
            "Lửng Mật chính là minh chứng sống động nhất trong tự nhiên cho chân lý: Kích thước cơ thể không bao giờ quyết định vị thế của bạn trên đấu trường sinh tồn. Một sinh vật nhỏ bé nhưng mang ý chí kiên cường, lòng dũng cảm bất diệt và tinh thần không bao giờ khuất phục trước bất kỳ thế lực nào, hoàn toàn có thể khiến cả những kẻ khổng lồ mạnh nhất phải kiêng dè nể sợ. Hãy nhớ rằng: Đừng bao giờ đánh giá thấp bất kỳ ai chỉ qua vẻ bề ngoài!",
            "Thế nhưng, gã Chí Phèo châu Phi này mới chỉ là câu chuyện mở màn cho chuỗi hành trình khám phá những bí ẩn kỳ dị của thế giới muông thú. Nếu bạn nghĩ sự tàn bạo và khó lường chỉ tồn tại trên đất liền thì bạn đã nhầm to. Bởi vì khi lặn xuống đại dương bao la, có một loài sinh vật nổi tiếng với vẻ ngoài siêu đáng yêu, hay nằm ngửa nắm tay nhau ngủ trên mặt nước... nhưng ẩn sau đó lại là những hành vi tâm lý rùng rợn và tàn bạo bậc nhất thế giới động vật: Đó chính là Rái Cá Biển! Chúng bắt cóc con non của hải cẩu, quấy rối các loài vật khác và có những góc khuất man rợ khiến bạn phải lạnh gáy! Cùng vén màn bí mật rùng rợn của loài vật dễ thương này trong tập tiếp theo nhé!"
        ]
    },
    {
        "id": "shorts",
        "title": "Shorts: 3 Sự Thật Điên Rồ Về Lửng Mật",
        "target_sec": 50,
        "paragraphs": [
            "Con vật kỳ dị này chỉ nặng vỏn vẹn mười hai kilôgam, nhưng cả bầy sư tử nhìn thấy từ xa cũng phải toát mồ hôi hột né đường! Bạn có biết ba sự thật điên rồ về Lửng Mật?",
            "Sự thật thứ nhất: Da của nó dày tới sáu milimét, lỏng lẻo như một chiếc áo khoác. Báo hoa mai cắn ngập gáy ư? Nó xoay người một trăm tám mươi độ ngay trong lớp da, cắn ngược vào mũi kẻ thù khiến đối thủ đau điếng tháo chạy!",
            "Sự thật thứ hai: Rắn hổ mang cắn thẳng vào mặt nó. Nọc độc chỉ làm nó lăn ra đất ngủ say hai tiếng như gã say rượu, rồi tỉnh queo dậy nhai nốt con rắn!",
            "Sự thật thứ ba: Bậc thầy vượt ngục Stoffel từng nặn bi đất, bắc thang cành cây và trèo lên lưng bạn gái để trốn sang chuồng sư tử gây sự! Đơn thương độc mã đối đầu ba sư tử đực, nó vẫn lao vào đánh không lùi một bước. Đây chính là Lửng Mật, kẻ Chí Phèo số một hành tinh, con vật chỉ nặng mười hai ký nhưng khiến cả thảo nguyên phải kiêng nể!"
        ]
    }
]

def synthesize_scene_male_125x(item: dict):
    sid = item["id"]
    title = item["title"]
    paragraphs = item["paragraphs"]
    out_wav = AUDIO_DIR / f"{sid}.wav"
    
    print(f"\n=======================================================")
    print(f"[VOICE MALE 1.25x] Synthesizing {sid}: {title}")
    print(f"Paragraphs: {len(paragraphs)}")
    
    part_wavs = []
    for idx, p in enumerate(paragraphs):
        p_clean = p.strip().replace("\n", " ")
        tmp_mp3 = AUDIO_DIR / f"{sid}_part{idx}.mp3"
        part_wav = AUDIO_DIR / f"{sid}_part{idx}.wav"
        
        # Fast reliable Google TTS
        tts = gTTS(text=p_clean, lang="vi", slow=False)
        tts.save(str(tmp_mp3))
        
        # Rubberband Pitch-shift to deep male voice (pitch=0.82) + 1.25x tempo + EQ warmth
        # 0.82 lowers pitch by ~3.5 semitones (perfect natural baritone male voice)
        af_chain = (
            "rubberband=pitch=0.82:tempo=1.25,"
            "highpass=f=75,lowpass=f=13500,"
            "equalizer=f=150:width_type=o:w=1.0:g=2.5,"
            "equalizer=f=3200:width_type=o:w=1.0:g=2.0,"
            "acompressor=threshold=-16dB:ratio=3:attack=5:release=50,"
            "volume=1.25"
        )
        subprocess.run([
            "ffmpeg", "-y", "-i", str(tmp_mp3),
            "-filter:a", af_chain,
            "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le",
            str(part_wav)
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        
        part_wavs.append(part_wav)
        tmp_mp3.unlink(missing_ok=True)
        print(f"  Part {idx+1}/{len(paragraphs)} mastered.")

    # Measure and store part durations
    part_durations = []
    for pw in part_wavs:
        p_cmd = [
            "ffprobe", "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            str(pw)
        ]
        p_dur = float(subprocess.check_output(p_cmd, text=True).strip())
        part_durations.append(p_dur)
    
    parts_meta = AUDIO_DIR / f"{sid}_parts_duration.json"
    parts_meta.write_text(json.dumps(part_durations, indent=2), encoding="utf-8")

    # Concat parts
    concat_txt = AUDIO_DIR / f"{sid}_concat.txt"
    with open(concat_txt, "w", encoding="utf-8") as f:
        for pw in part_wavs:
            p_str = str(pw.resolve()).replace("\\", "/")
            f.write(f"file '{p_str}'\n")
            
    subprocess.run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", str(concat_txt),
        "-c", "copy",
        str(out_wav)
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    
    concat_txt.unlink(missing_ok=True)
    for pw in part_wavs:
        pw.unlink(missing_ok=True)
        
    probe_cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(out_wav)
    ]
    dur_str = subprocess.check_output(probe_cmd, text=True).strip()
    dur_sec = float(dur_str)
    dur_ms = int(round(dur_sec * 1000))
    print(f"[SUCCESS] {sid}.wav duration: {dur_sec:.2f}s ({dur_ms}ms, target ~{item['target_sec']}s)")
    return dur_sec

def main():
    import sys
    target_ids = [arg for arg in sys.argv[1:] if not arg.startswith("-")]
    scenes_to_run = [s for s in FULL_SCENES if s["id"] in target_ids] if target_ids else FULL_SCENES

    print("=======================================================")
    print("BATCH SYNTHESIZE FULL-DURATION 1.25x MALE VOICE")
    print(f"Target Scenes: {[s['id'] for s in scenes_to_run]}")
    print("=======================================================")
    t0 = time.time()
    total_sec = 0.0
    for item in scenes_to_run:
        d = synthesize_scene_male_125x(item)
        if item["id"] != "shorts":
            total_sec += d
            
    print("\n=======================================================")
    print(f"Processed {len(scenes_to_run)} scene(s) in {time.time() - t0:.1f}s!")
    print("=======================================================")

if __name__ == "__main__":
    main()
