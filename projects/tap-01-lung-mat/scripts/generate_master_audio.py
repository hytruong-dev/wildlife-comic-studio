"""
Master Audio & Word Timings Generator for Episode 1: Lửng Mật (Honey Badger)
- Full 6 Acts matching 8:30 - 9:30 minutes channel target
- Uses gTTS with FFmpeg broadcast audio chain (48kHz, warm EQ, broadcast levels)
- Computes weighted proportional word-level timestamps (handling pauses at commas and periods)
- Outputs scene01.wav - scene06.wav and scene01_words.json - scene06_words.json
"""

import json
import re
import subprocess
from pathlib import Path
from gtts import gTTS

SCRIPT_DIR = Path(__file__).resolve().parent
PROJ = SCRIPT_DIR.parent
AUDIO_DIR = PROJ / "audio"
AUDIO_DIR.mkdir(parents=True, exist_ok=True)

SCENES = [
    {
        "id": "scene01",
        "title": "Act 1: The Myth-Buster Hook - Kẻ Chí Phèo Số Một Hành Tinh",
        "text": """Bạn nghĩ ai mới thực sự là bá chủ tối cao của thảo nguyên hoang dã châu Phi? Là chúa sơn lâm sư tử với tiếng gầm rung chuyển cả núi rừng? Là đàn linh cẩu tàn nhẫn và tham lam, hay những gã khổng lồ như voi và tê giác?
Quên tất cả những điều đó đi! Trong từ điển sinh tồn của thế giới hoang dã, có một sinh vật kỳ dị chỉ cao chưa đầy ba mươi centimet, nặng vỏn vẹn mười hai kilôgam, nhưng lại khiến cả một bầy sư tử nhìn thấy từ xa cũng phải toát mồ hôi hột, tự động né sang một bên đường.
Giới khoa học đặt tên cho nó là Mellivora capensis. Còn trên giang hồ của muôn loài, nó được phong tặng danh hiệu kẻ Chí Phèo số một hành tinh: Lửng Mật!
Một gã lùn tịt với bộ lông hai màu đen trắng tương phản, dáng đi lững thững khệnh khạng đầy vẻ bất cần đời. Nó sẵn sàng lao vào quyết đấu sinh tử với bất kỳ thứ gì có thở, và đặc biệt là sở hữu một quả não hoàn toàn không có khái niệm về cái chết!"""
    },
    {
        "id": "scene02",
        "title": "Act 2: Bảng Chỉ Số Sinh Tồn RPG Stats",
        "text": """Nếu đưa Lửng Mật vào một tựa game nhập vai thế giới mở, chắc chắn các nhà phát triển game sẽ bị cộng đồng người chơi khiếu nại kịch liệt vì đã tạo ra một nhân vật quá sức mất cân bằng. Chúng ta hãy cùng bóc tách bảng chỉ số sinh tồn có một không hai của gã chiến binh này.
Đầu tiên là chỉ số Sức Mạnh Thể Chất STR: Đạt tám mươi lăm trên một trăm điểm. Dưới lớp lông dày cộp là hệ thống bó cơ nén đặc với mật độ khủng khiếp, giúp Lửng Mật có thể kéo lê một xác linh dương nặng gấp ba lần trọng lượng cơ thể nó đi qua hàng cây số.
Thứ hai là chỉ số Phòng Thủ DEF: Chạm mốc tuyệt đối chín mươi chín điểm! Nó khoác lên mình một lớp giáp cao su di động dày tới sáu milimét, kháng cự hoàn toàn từ răng nanh của sư tử, nọc độc của bọ cạp đến cả những mũi giáo sắc nhọn của thổ dân châu Phi.
Thứ ba là chỉ số Trí Thông Minh IQ: Đạt chín mươi điểm. Đây không phải một kẻ hữu dũng vô mưu, mà là một thiên tài bẻ khóa, chế tạo công cụ và tư duy chiến thuật sinh tồn đỉnh cao.
Tiếp theo là Độ Bền Bỉ và Lì Đòn TENACITY: Phá vỡ mọi thang đo với chín trăm chín mươi chín điểm! Trong từ điển của Lửng Mật, không có nút đầu hàng và càng không có khái niệm lùi bước.
Và chỉ số cuối cùng chấn động nhất: Cảm Giác Sợ Hãi FEAR: Không điểm tròn trĩnh! Các nhà sinh vật học đã chứng minh rằng hạch hạnh nhân trong não bộ của Lửng Mật gần như không phản ứng với nguy hiểm, biến nó thành sinh vật liều lĩnh nhất từng được ghi nhận trong sách kỷ lục thế giới!"""
    },
    {
        "id": "scene03",
        "title": "Act 3: Cơ Chế Sinh Tồn Độc Dị - Áo Giáp Cao Su & Lưỡi Hái",
        "text": """Điều gì đã giúp một sinh vật nhỏ bé sống sót và ngạo nghễ bước đi giữa chốn thảo nguyên đầy rẫy hiểm nguy? Bí mật nằm ở ba cơ chế giải phẫu kỳ dị mà tự nhiên ban tặng.
Cơ chế thứ nhất chính là lớp da cao su đàn hồi cực kỳ lỏng lẻo. Lớp da của Lửng Mật dày hơn cả da trâu mộng, nhưng nó không hề dính chặt vào cơ bắp mà lỏng lẻo như một chiếc áo khoác thùng thình. Hãy hình dung tình huống này: Khi một con báo hoa mai hay chó săn châu Phi ngoạm chặt vào gáy Lửng Mật và nghĩ rằng con mồi đã nằm gọn trong tay, điều kỳ quái xảy ra: Lửng Mật có thể tự do xoay người một trăm tám mươi độ ngay bên trong chính lớp da của mình, rồi quay ngoắt bộ hàm sắc nhọn cắn trả thẳng vào mũi và mắt của kẻ săn mồi! Cú phản công bất ngờ và đau đớn khiến bất kỳ kẻ đi săn nào cũng phải giật mình nhả ra ngay lập tức.
Cơ chế thứ hai là đôi móng vuốt lưỡi hái trước ngực. Mỗi ngón chân trước của Lửng Mật sở hữu chiếc móng dài hơn năm centimet, cong vút và cứng như mũi khoan thép tôi. Nó có thể xới tung tổ mối cứng như bê tông chỉ trong vài phút, hay đào sâu vào lòng đất tạo hang trú ẩn nhanh hơn một người dùng xẻng xúc đất.
Và cơ chế thứ ba là vũ khí phòng vệ hóa học phía sau đuôi. Lửng Mật sở hữu một túi xạ hương đặc biệt có thể đảo ngược ra ngoài, phun ra luồng khí gas thối nồng nặc đến nghẹt thở. Luồng khí này không chỉ làm tê liệt khứu giác siêu nhạy của bầy thú săn mồi lớn, mà còn khiến chúng buồn nôn, cay mắt và buộc phải tháo chạy trong tức tối!"""
    },
    {
        "id": "scene04",
        "title": "Act 4: Cú Bẻ Lái Của Tạo Hóa - Miễn Nhiễm Nọc Độc Thần Kinh",
        "text": """Thế nhưng tất cả những vũ khí trên vẫn chưa là gì so với thực đơn ăn uống điên rồ bậc nhất hành tinh của gã giang hồ này. Lửng Mật nổi tiếng là kẻ nghiện ăn nọc độc. Món khoái khẩu của nó là những loài rắn chết chóc nhất: Rắn phì châu Phi, rắn hổ mang thổi nọc và cả hổ mang chúa!
Bạn có biết, một giọt nọc độc của rắn phì đủ để làm tan rữa tế bào và hạ gục những sinh vật to lớn gấp mười lần nó chỉ trong ít phút.
Vậy điều gì sẽ xảy ra khi một con rắn hổ mang khổng lồ cắn ngập đôi răng nanh đầy nọc độc thẳng vào mặt của Lửng Mật? Liệu kẻ liều lĩnh này có phải trả giá bằng cả mạng sống?
Câu trả lời là một cú bẻ lái kinh điển của tiến hóa sinh học!
Các nhà khoa học phát hiện ra rằng, các thụ thể nicotinic acetylcholine trong hệ thần kinh của Lửng Mật đã trải qua đột biến phân tử sau hàng triệu năm đối đầu với loài rắn. Đột biến này hoạt động như một lớp áo giáp phân tử, khiến độc tố thần kinh cực mạnh của rắn không thể bám vào để làm tê liệt hệ hô hấp của nó.
Khi bị rắn cắn trúng, nọc độc vẫn ngấm vào tuần hoàn máu. Lúc này, Lửng Mật sẽ từ từ lảo đảo, lăn đùng ra đất và rơi vào trạng thái hôn mê sâu giống hệt như một gã say vừa uống cạn một chum rượu mạnh. Toàn thân nó mềm nhũn, tim đập chậm lại suốt hai đến ba tiếng đồng hồ khiến kẻ thù tưởng nó đã chết.
Thế nhưng khi men say nọc độc tan hết và gan trung hòa xong độc chất, Lửng Mật bỗng mở to mắt, đứng dậy lắc đầu rũ lông tỉnh queo như vừa ngủ trưa dậy, rồi thản nhiên cúi xuống nhai nốt nửa con rắn còn lại như một món ăn vặt ngon lành!"""
    },
    {
        "id": "scene05",
        "title": "Act 5: Đại Chiến Thiên Nhiên & Bậc Thầy Vượt Ngục Stoffel",
        "text": """Bên cạnh thân thể dẻo dai và khả năng kháng độc, trí thông minh của Lửng Mật mới thực sự là thứ khiến các nhà động vật học phải ngả mũ thán phục. Minh chứng sống động nhất cho trí tuệ siêu phàm này chính là chú lửng mật Stoffel tại Trung tâm Phục hồi Hoang dã Moholoholo ở Nam Phi.
Stoffel nổi tiếng toàn cầu đến mức được đài truyền hình BBC làm riêng một bộ phim tài liệu về những phi vụ vượt ngục không tưởng.
Ban đầu, các chuyên gia nhốt Stoffel trong một khu chuồng rào tường bê tông cao lút đầu người. Bạn nghĩ bức tường cao sẽ giam giữ được nó?
Stoffel đã dùng chân cào đất bùn, nặn thành từng viên bi đất tròn to tướng rồi đẩy chúng vào góc tường, xếp chồng lên nhau thành một gò đất cao để nhảy vọt qua rào trốn thoát!
Khi các nhân viên dọn sạch bùn đất, Stoffel đi gom những cành cây khô, dựng đứng tựa vào tường làm thang leo.
Họ dọn sạch cành cây, nó liền hợp sức lăn những tảng đá lớn lại.
Khi chuồng bị dọn nhẵn thín không còn một viên sỏi, Stoffel thậm chí đã làm quen với một con lửng mật cái cùng phòng, dụ dỗ con cái đứng sát góc tường để nó trèo lên lưng con cái phóng vọt ra ngoài!
Và điều hài hước nhất là mục đích vượt ngục của nó: Không phải để tìm về với rừng sâu, mà là xông thẳng vào chuồng bầy sư tử kế bên để khiêu chiến và trêu chọc chúa sơn lâm!
Ngay cả khi bị ba con sư tử đực to lớn bao vây, Lửng Mật không bao giờ lùi bước. Nó xù dựng toàn bộ lông lưng, gầm rít dữ dội và lao thẳng vào giữa bầy sư tử khiến các chúa tể thảo nguyên cũng phải e dè né tránh vì nhận ra cái giá phải trả quá đắt!"""
    },
    {
        "id": "scene06",
        "title": "Act 6: Seamless Outro - Chuyển Tiếp Sang Ngày 2: Rái Cá Biển",
        "text": """Lửng Mật chính là minh chứng sống động nhất cho việc kích thước không quyết định vị thế của bạn trong tự nhiên. Một sinh vật nhỏ bé nhưng mang ý chí kiên cường và lòng dũng cảm bất diệt.
Thế nhưng, gã Chí Phèo châu Phi này mới chỉ là câu chuyện mở đầu. Nếu bạn nghĩ sự tàn bạo và khó lường chỉ tồn tại trên đất liền thì bạn đã nhầm to.
Bởi vì khi lặn xuống đại dương bao la, có một loài sinh vật nổi tiếng với vẻ ngoài siêu đáng yêu, hay nằm ngửa nắm tay nhau ngủ trên mặt nước... nhưng ẩn sau đó lại là những hành vi tâm lý rùng rợn và tàn bạo bậc nhất thế giới động vật: Đó chính là Rái Cá Biển!
Hãy bấm ngay vào video đang hiển thị trên màn hình để cùng vén màn bí mật rùng rợn của loài vật dễ thương này trong tập tiếp theo nhé. Đừng quên bấm Đăng Ký kênh Vẽ Chuyện Muông Thú để đồng hành cùng chúng tôi mỗi ngày!"""
    }
]

def generate_weighted_word_timeline(text: str, total_duration_ms: int):
    # Tokenize into words preserving punctuation cues
    raw_tokens = text.split()
    words_data = []
    
    # Weight per word: base length + extra pause for punctuation
    total_weights = 0.0
    token_weights = []
    
    for token in raw_tokens:
        clean = re.sub(r'[^\w\s]', '', token)
        base_w = max(1.0, len(clean) * 0.8)
        pause_w = 0.0
        if token.endswith(('.', '!', '?')):
            pause_w = 4.0  # ~300-400ms pause
        elif token.endswith((',', ';', ':')):
            pause_w = 2.0  # ~150-200ms pause
        w = base_w + pause_w
        token_weights.append((token, clean, w, pause_w))
        total_weights += w
        
    ms_per_weight = (total_duration_ms - 400) / max(1.0, total_weights)
    cur_ms = 200  # 200ms lead-in
    
    for token, clean, w, pause_w in token_weights:
        word_dur = int((w - pause_w) * ms_per_weight)
        pause_dur = int(pause_w * ms_per_weight)
        words_data.append({
            "word": token,
            "clean": clean,
            "startMs": int(cur_ms),
            "endMs": int(cur_ms + word_dur),
            "durationMs": int(word_dur)
        })
        cur_ms += word_dur + pause_dur
        
    return words_data

def build_scene_audio(scene: dict):
    scene_id = scene["id"]
    title = scene["title"]
    text = scene["text"].strip()
    
    tmp_mp3 = AUDIO_DIR / f"{scene_id}_tmp.mp3"
    wav_out = AUDIO_DIR / f"{scene_id}.wav"
    words_out = AUDIO_DIR / f"{scene_id}_words.json"
    
    print(f"\n>>> [TTS] Đang sinh âm thanh cho {scene_id}: {title} ({len(text)} ký tự)...")
    tts = gTTS(text, lang="vi")
    tts.save(str(tmp_mp3))
    
    # Process audio through broadcast filter chain (atempo=1.06, warm EQ, 48kHz stereo)
    subprocess.run([
        "ffmpeg", "-y", "-i", str(tmp_mp3),
        "-filter:a", "atempo=1.06,highpass=f=75,lowpass=f=12500,volume=1.2",
        "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le",
        str(wav_out)
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    
    tmp_mp3.unlink()
    
    # Get exact audio duration
    probe = subprocess.check_output([
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(wav_out)
    ]).decode("utf-8").strip()
    dur_sec = float(probe)
    total_ms = int(dur_sec * 1000)
    
    # Generate weighted word timeline
    words_timeline = generate_weighted_word_timeline(text, total_ms)
    with open(words_out, "w", encoding="utf-8") as f:
        json.dump(words_timeline, f, ensure_ascii=False, indent=2)
        
    mins = int(dur_sec // 60)
    secs = int(dur_sec % 60)
    print(f"  [XONG {scene_id}] Thời lượng: {mins}:{secs:02d} ({dur_sec:.2f}s) | {len(words_timeline)} từ đồng bộ")
    return dur_sec

def main():
    print("=" * 70)
    print("BẮT ĐẦU SẢN XUẤT MASTER AUDIO TOÀN DIỆN 6 PHÂN CẢNH TẬP 1 (LỬNG MẬT)")
    print("Mục tiêu: Đạt chuẩn 8:30 - 9:30 phút theo Blue Print kênh YouTube")
    print("=" * 70)
    
    total_sec = 0.0
    for sc in SCENES:
        dur = build_scene_audio(sc)
        total_sec += dur
        
    total_mins = int(total_sec // 60)
    total_secs = int(total_sec % 60)
    print("\n" + "=" * 70)
    print(f"HOÀN THÀNH SẢN XUẤT AUDIO 6 PHÂN CẢNH!")
    print(f"TỔNG THỜI LƯỢNG MASTER AUDIO: {total_mins} phút {total_secs} giây ({total_sec:.2f}s)")
    print(f"ĐÃ LƯU TRỌN BỘ TẠI: {AUDIO_DIR}")
    print("=" * 70)

if __name__ == "__main__":
    main()
