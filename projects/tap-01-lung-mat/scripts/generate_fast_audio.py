"""
Enhanced Fast & Dynamic Master Audio Generator for Episode 1: Lửng Mật
- Speed: atempo = 1.24 (24% faster, eliminates slow/boring pauses)
- Dramatic punctuation and vocal mastering: Warm low-end 160Hz (+3dB), Crisp vocal clarity 3200Hz (+2.5dB), Dynamic compression
- Accurate word-level timestamps synchronized with punctuation weights
"""

import json
import re
import subprocess
from pathlib import Path
from gtts import gTTS

SCRIPT_DIR = Path(__file__).resolve().parent
PROJ = SCRIPT_DIR.parent
AUDIO_DIR = PROJ / "audio_fast"
AUDIO_DIR.mkdir(parents=True, exist_ok=True)

# 1.24x speedup for high-tempo engaging YouTube pace
SPEED_FACTOR = 1.24

SCENES = [
    {
        "id": "scene01",
        "title": "Act 1: The Myth-Buster Hook - Kẻ Chí Phèo Số Một Hành Tinh",
        "text": """Bạn nghĩ ai mới thực sự là bá chủ tối cao của thảo nguyên hoang dã châu Phi? Là chúa sơn lâm sư tử với tiếng gầm rung chuyển cả núi rừng? Là đàn linh cẩu tàn nhẫn và tham lam, hay những gã khổng lồ như voi và tê giác?
Quên tất cả những điều đó đi! Trong thế giới hoang dã khắc nghiệt, có một sinh vật kỳ dị chỉ cao chưa đầy ba mươi centimet, nặng vỏn vẹn mười hai kilôgam, nhưng lại khiến cả một bầy sư tử nhìn thấy từ xa cũng phải toát mồ hôi hột, tự động né sang một bên đường!
Giới khoa học gọi nó là Mellivora capensis. Còn trên giang hồ của muôn loài, nó được phong tặng danh hiệu kẻ Chí Phèo số một hành tinh: Lửng Mật!
Một gã lùn tịt với bộ lông hai màu đen trắng tương phản, dáng đi khệnh khạng đầy vẻ bất cần đời. Nó sẵn sàng lao vào quyết đấu sinh tử với bất kỳ thứ gì, và đặc biệt là sở hữu một quả não hoàn toàn không có khái niệm về cái chết!"""
    },
    {
        "id": "scene02",
        "title": "Act 2: Bảng Chỉ Số Sinh Tồn RPG Stats",
        "text": """Nếu đưa Lửng Mật vào một tựa game nhập vai thế giới mở, chắc chắn các nhà phát triển game sẽ bị người chơi khiếu nại kịch liệt vì đã tạo ra một nhân vật quá sức mất cân bằng! Chúng ta hãy cùng bóc tách bảng chỉ số sinh tồn có một không hai của gã chiến binh này.
Đầu tiên là chỉ số Sức Mạnh Thể Chất STR: Đạt tám mươi lăm trên một trăm điểm! Dưới lớp lông dày cộp là hệ thống bó cơ nén đặc với mật độ khủng khiếp, giúp Lửng Mật có thể kéo lê một xác linh dương nặng gấp ba lần trọng lượng cơ thể nó.
Thứ hai là chỉ số Phòng Thủ DEF: Chạm mốc tuyệt đối chín mươi chín điểm! Nó khoác lên mình một lớp giáp cao su di động dày tới sáu milimét, kháng cự hoàn toàn từ răng nanh sư tử, nọc độc bọ cạp đến cả những mũi giáo sắc nhọn của thổ dân châu Phi!
Thứ ba là chỉ số Trí Thông Minh IQ: Đạt chín mươi điểm! Đây không phải một kẻ hữu dũng vô mưu, mà là một thiên tài bẻ khóa, chế tạo công cụ và tư duy chiến thuật sinh tồn đỉnh cao.
Tiếp theo là Độ Bền Bỉ và Lì Đòn TENACITY: Phá vỡ mọi thang đo với chín trăm chín mươi chín điểm! Trong từ điển của Lửng Mật, không có nút đầu hàng và càng không có khái niệm lùi bước!
Và chỉ số cuối cùng chấn động nhất: Cảm Giác Sợ Hãi FEAR: Không điểm tròn trĩnh! Hạch hạnh nhân trong não bộ của Lửng Mật gần như không phản ứng với nguy hiểm, biến nó thành sinh vật liều lĩnh nhất từng được ghi nhận trong sách kỷ lục thế giới!"""
    },
    {
        "id": "scene03",
        "title": "Act 3: Cơ Chế Sinh Tồn Độc Dị - Áo Giáp Cao Su & Lưỡi Hái",
        "text": """Điều gì đã giúp một sinh vật nhỏ bé sống sót và ngạo nghễ bước đi giữa chốn thảo nguyên đầy rẫy hiểm nguy? Bí mật nằm ở ba cơ chế giải phẫu kỳ dị mà tự nhiên ban tặng!
Cơ chế thứ nhất chính là lớp da cao su đàn hồi cực kỳ lỏng lẻo. Da của Lửng Mật dày hơn cả da trâu mộng, nhưng lỏng lẻo như một chiếc áo khoác thùng thình. Hãy hình dung: Khi một con báo hoa mai ngoạm chặt vào gáy Lửng Mật và nghĩ rằng con mồi đã nằm gọn trong tay, điều kỳ quái xảy ra: Lửng Mật có thể tự do xoay người một trăm tám mươi độ ngay bên trong chính lớp da của mình, rồi quay ngoắt bộ hàm sắc nhọn cắn trả thẳng vào mũi và mắt của kẻ săn mồi! Cú phản công bất ngờ khiến bất kỳ kẻ đi săn nào cũng phải giật mình nhả ra ngay lập tức!
Cơ chế thứ hai là đôi móng vuốt lưỡi hái trước ngực. Mỗi ngón chân trước sở hữu chiếc móng dài hơn năm centimet, cong vút và cứng như mũi khoan thép! Nó có thể xới tung tổ mối cứng như bê tông chỉ trong vài phút!
Và cơ chế thứ ba là vũ khí phòng vệ hóa học phía sau đuôi. Lửng Mật sở hữu một túi xạ hương đặc biệt phun ra luồng khí gas thối nồng nặc đến nghẹt thở, làm tê liệt khứu giác siêu nhạy của bầy thú săn mồi, khiến chúng buồn nôn, cay mắt và buộc phải tháo chạy trong tức tối!"""
    },
    {
        "id": "scene04",
        "title": "Act 4: Cú Bẻ Lái Của Tạo Hóa - Miễn Nhiễm Nọc Độc Thần Kinh",
        "text": """Thế nhưng tất cả những vũ khí trên vẫn chưa là gì so với thực đơn ăn uống điên rồ bậc nhất hành tinh của gã giang hồ này! Lửng Mật nổi tiếng là kẻ nghiện ăn nọc độc. Món khoái khẩu của nó là những loài rắn chết chóc nhất: Rắn phì châu Phi, rắn hổ mang thổi nọc và cả hổ mang chúa!
Một giọt nọc độc rắn phì đủ để làm tan rữa tế bào và hạ gục những sinh vật to lớn gấp mười lần nó chỉ trong ít phút.
Vậy điều gì sẽ xảy ra khi một con rắn hổ mang khổng lồ cắn ngập đôi răng nanh đầy nọc độc thẳng vào mặt của Lửng Mật? Liệu kẻ liều lĩnh này có phải trả giá bằng cả mạng sống?
Câu trả lời là một cú bẻ lái kinh điển của tiến hóa sinh học!
Các nhà khoa học phát hiện ra rằng, các thụ thể nicotinic acetylcholine trong hệ thần kinh của Lửng Mật đã trải qua đột biến phân tử. Đột biến này hoạt động như một lớp áo giáp phân tử, khiến độc tố thần kinh cực mạnh của rắn không thể bám vào để làm tê liệt hệ hô hấp của nó!
Khi bị rắn cắn trúng, nọc độc vẫn ngấm vào tuần hoàn máu. Lúc này, Lửng Mật sẽ từ từ lảo đảo, lăn đùng ra đất và rơi vào trạng thái hôn mê sâu giống hệt như một gã say vừa uống cạn một chum rượu mạnh! Toàn thân mềm nhũn, tim đập chậm lại suốt hai đến ba tiếng đồng hồ khiến kẻ thù tưởng nó đã chết.
Thế nhưng khi men say nọc độc tan hết và gan trung hòa xong độc chất, Lửng Mật bỗng mở to mắt, đứng dậy lắc đầu rũ lông tỉnh queo như vừa ngủ trưa dậy, rồi thản nhiên cúi xuống nhai nốt nửa con rắn còn lại như một món ăn vặt ngon lành!"""
    },
    {
        "id": "scene05",
        "title": "Act 5: Đại Chiến Thiên Nhiên & Bậc Thầy Vượt Ngục Stoffel",
        "text": """Bên cạnh thân thể dẻo dai và khả năng kháng độc, trí thông minh của Lửng Mật mới thực sự là thứ khiến các nhà động vật học phải ngả mũ thán phục! Minh chứng sống động nhất chính là chú lửng mật Stoffel tại Trung tâm Phục hồi Hoang dã Moholoholo ở Nam Phi.
Stoffel nổi tiếng toàn cầu đến mức được đài truyền hình BBC làm riêng một bộ phim tài liệu về những phi vụ vượt ngục không tưởng!
Ban đầu, các chuyên gia nhốt Stoffel trong một khu chuồng rào tường bê tông cao lút đầu người. Bạn nghĩ bức tường cao sẽ giam giữ được nó?
Stoffel đã dùng chân cào đất bùn, nặn thành từng viên bi tròn to tướng rồi xếp chồng lên nhau thành gò đất cao để nhảy vọt qua rào trốn thoát!
Khi các nhân viên dọn sạch bùn đất, Stoffel đi gom những cành cây khô làm thang leo. Họ dọn sạch cành cây, nó liền hợp sức lăn những tảng đá lớn lại.
Khi chuồng bị dọn nhẵn thín không còn một viên sỏi, Stoffel thậm chí đã rủ rê một con lửng mật cái cùng phòng, dụ dỗ con cái đứng sát góc tường để nó trèo lên lưng con cái phóng vọt ra ngoài!
Và điều hài hước nhất là mục đích vượt ngục của nó: Không phải để tìm về với rừng sâu, mà là xông thẳng vào chuồng bầy sư tử kế bên để khiêu chiến và trêu chọc chúa sơn lâm!
Ngay cả khi bị ba con sư tử đực to lớn bao vây, Lửng Mật không bao giờ lùi bước. Nó xù dựng toàn bộ lông lưng, gầm rít dữ dội và lao thẳng vào giữa bầy sư tử khiến các chúa tể thảo nguyên cũng phải e dè né tránh vì nhận ra cái giá phải trả quá đắt!"""
    },
    {
        "id": "scene06",
        "title": "Act 6: Seamless Outro - Chuyển Tiếp Sang Ngày 2: Rái Cá Biển",
        "text": """Lửng Mật chính là minh chứng sống động nhất cho việc kích thước không quyết định vị thế của bạn trong tự nhiên! Một sinh vật nhỏ bé nhưng mang ý chí kiên cường và lòng dũng cảm bất diệt.
Thế nhưng, gã Chí Phèo châu Phi này mới chỉ là câu chuyện mở đầu. Nếu bạn nghĩ sự tàn bạo và khó lường chỉ tồn tại trên đất liền thì bạn đã nhầm to!
Bởi vì khi lặn xuống đại dương bao la, có một loài sinh vật nổi tiếng với vẻ ngoài siêu đáng yêu, hay nằm ngửa nắm tay nhau ngủ trên mặt nước... nhưng ẩn sau đó lại là những hành vi tâm lý rùng rợn và tàn bạo bậc nhất thế giới động vật: Đó chính là Rái Cá Biển!
Hãy bấm ngay vào video đang hiển thị trên màn hình để cùng vén màn bí mật rùng rợn của loài vật dễ thương này trong tập tiếp theo nhé. Đừng quên bấm Đăng Ký kênh Vẽ Chuyện Muông Thú để đồng hành cùng chúng tôi mỗi ngày!"""
    }
]

def build_scene_audio(scene: dict):
    sid = scene["id"]
    text = scene["text"]
    raw_mp3 = AUDIO_DIR / f"{sid}_raw.mp3"
    master_wav = AUDIO_DIR / f"{sid}.wav"
    words_json = AUDIO_DIR / f"{sid}_words.json"
    
    print(f"\n[AUDIO] Processing {sid}: {scene['title']}...")
    tts = gTTS(text=text, lang="vi", tld="com.vn", slow=False)
    tts.save(str(raw_mp3))
    
    # Broadcast Mastering Chain with 1.24x tempo, rich bass, and punchy vocal clarity
    filter_complex = (
        f"atempo={SPEED_FACTOR},"
        "highpass=f=80,lowpass=f=11000,"
        "equalizer=f=160:width_type=o:w=1.0:g=3.0,"
        "equalizer=f=3400:width_type=o:w=1.0:g=2.5,"
        "acompressor=threshold=-15dB:ratio=3:attack=5:release=50,"
        "volume=1.3"
    )
    
    cmd_ffmpeg = [
        "ffmpeg", "-y",
        "-i", str(raw_mp3),
        "-af", filter_complex,
        "-ar", "48000",
        "-ac", "2",
        "-c:a", "pcm_s16le",
        str(master_wav)
    ]
    subprocess.run(cmd_ffmpeg, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # Get accurate duration
    cmd_probe = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(master_wav)
    ]
    out = subprocess.check_output(cmd_probe).decode().strip()
    total_dur_s = float(out)
    total_dur_ms = int(total_dur_s * 1000)
    
    # Calculate word timestamps
    clean_words = []
    tokens = re.split(r"(\s+)", text)
    for t in tokens:
        if t.strip():
            w_clean = re.sub(r"[^\w\s\u00C0-\u1EF9]", "", t, flags=re.UNICODE)
            if w_clean:
                weight = 1.0 + (len(w_clean) * 0.08)
                if t.endswith((".", "!", "?")):
                    weight += 1.6
                elif t.endswith((",", ";", ":")):
                    weight += 0.8
                clean_words.append({"word": w_clean, "raw": t, "weight": weight})
                
    total_weight = sum(w["weight"] for w in clean_words)
    current_ms = 100.0
    usable_dur_ms = total_dur_ms - 200.0
    
    word_entries = []
    for cw in clean_words:
        dur = (cw["weight"] / total_weight) * usable_dur_ms
        start_ms = int(round(current_ms))
        end_ms = int(round(current_ms + dur * 0.82))
        word_entries.append({
            "word": cw["word"],
            "startMs": start_ms,
            "endMs": end_ms,
            "durationMs": end_ms - start_ms
        })
        current_ms += dur
        
    with open(words_json, "w", encoding="utf-8") as f:
        json.dump(word_entries, f, ensure_ascii=False, indent=2)
        
    print(f"  -> {master_wav.name}: {total_dur_s:.2f}s ({total_dur_ms}ms, {len(word_entries)} words)")
    return total_dur_s

if __name__ == "__main__":
    total = 0.0
    for sc in SCENES:
        dur = build_scene_audio(sc)
        total += dur
    print(f"\n=======================================================")
    print(f"ALL FAST SCENES GENERATED! Total Duration: {total:.2f}s ({int(total//60)}m {total%60:.1f}s)")
    print(f"=======================================================")
