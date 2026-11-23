"""
Generate Male Voice (vi-VN-NamMinhNeural) with 1.5x Speed (+50%)
For Episode 1: Lung Mat (Honey Badger) - All 6 Scenes + Shorts
Updates audio files and scales spec timelines proportionally.
"""

import sys
import os
import json
import re
import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROJ = Path(__file__).resolve().parents[1]
AUDIO_DIR = PROJ / "audio"
SPECS_DIR = PROJ / "specs"

VOICE = "vi-VN-NamMinhNeural"
RATE = "+50%"

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
    },
    {
        "id": "shorts",
        "title": "Shorts: 3 Sự Thật Điên Rồ Về Lửng Mật",
        "text": """Con vật này chỉ nặng mười hai ký, nhưng sư tử thấy nó cũng phải tránh đường!
Sự thật thứ nhất: da nó dày sáu milimét, và lỏng như một chiếc áo khoác. Báo hoa mai cắn vào gáy? Nó xoay một trăm tám mươi độ ngay trong lớp da, rồi cắn ngược vào mũi kẻ thù!
Sự thật thứ hai: rắn hổ mang cắn thẳng vào mặt nó. Nó lăn ra ngủ hai tiếng, rồi tỉnh dậy, ăn nốt con rắn!
Sự thật thứ ba: chú lửng Stoffel vượt ngục hàng chục lần. Bằng bùn, bằng cành cây, bằng đá, và bằng cả lưng của bạn gái nó! Bị ba con sư tử bao vây? Nó vẫn lao vào đánh.
Đây là Lửng Mật, kẻ Chí Phèo số một hành tinh!"""
    }
]

def synthesize_scene(item: dict):
    sid = item["id"]
    text = item["text"].strip().replace("\n", " ")
    
    tmp_txt = AUDIO_DIR / f"{sid}_input.txt"
    tmp_mp3 = AUDIO_DIR / f"{sid}_raw.mp3"
    out_wav = AUDIO_DIR / f"{sid}.wav"
    
    tmp_txt.write_text(text, encoding="utf-8")
    
    print(f"\n=======================================================")
    print(f"[TTS 1.5x] Generating Male Voice ({VOICE}, {RATE}) for {sid}...")
    print(f"Text length: {len(text)} chars")
    
    # Run edge-tts CLI
    cmd = [
        "edge-tts",
        "--voice", VOICE,
        "--rate", RATE,
        "-f", str(tmp_txt),
        "--write-media", str(tmp_mp3)
    ]
    subprocess.run(cmd, check=True)
    
    # Broadcast audio mastering (48kHz stereo, EQ warmth, compressor)
    af_chain = (
        "highpass=f=75,lowpass=f=13500,"
        "equalizer=f=150:width_type=o:w=1.0:g=2.2,"
        "equalizer=f=3000:width_type=o:w=1.0:g=1.8,"
        "acompressor=threshold=-16dB:ratio=3:attack=5:release=50,"
        "volume=1.2"
    )
    cmd_ff = [
        "ffmpeg", "-y",
        "-i", str(tmp_mp3),
        "-filter:a", af_chain,
        "-ar", "48000",
        "-ac", "2",
        "-c:a", "pcm_s16le",
        str(out_wav)
    ]
    subprocess.run(cmd_ff, check=True)
    
    # Cleanup temp files
    tmp_txt.unlink(missing_ok=True)
    tmp_mp3.unlink(missing_ok=True)
    
    # Probe duration
    probe_cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(out_wav)
    ]
    dur_str = subprocess.check_output(probe_cmd, text=True).strip()
    dur_sec = float(dur_str)
    dur_ms = int(round(dur_sec * 1000))
    print(f"[SUCCESS] {sid}.wav mastered: {dur_sec:.2f}s ({dur_ms}ms)")
    
    # Update spec timeline
    spec_path = SPECS_DIR / f"{sid}_spec.json"
    if spec_path.exists():
        update_spec_timeline(spec_path, dur_ms)
        
    return dur_ms

def update_spec_timeline(spec_path: Path, new_total_ms: int):
    with open(spec_path, "r", encoding="utf-8") as f:
        spec = json.load(f)
        
    old_total_ms = spec.get("duration_ms", 60000)
    spec["duration_ms"] = new_total_ms
    
    ratio = new_total_ms / max(1.0, old_total_ms)
    
    for p in spec.get("panels", []):
        p["start_ms"] = int(round(p["start_ms"] * ratio))
        p["end_ms"] = int(round(p["end_ms"] * ratio))
        
    with open(spec_path, "w", encoding="utf-8") as f:
        json.dump(spec, f, ensure_ascii=False, indent=2)
        
    print(f"  [Spec Updated] {spec_path.name}: {old_total_ms}ms -> {new_total_ms}ms (ratio: {ratio:.3f})")

def main():
    print("=======================================================")
    print(f"BATCH SYNTHESIZE MALE VOICE 1.5x ({VOICE}, {RATE})")
    print("=======================================================")
    t0 = time.time()
    for item in SCENES:
        synthesize_scene(item)
    print(f"\n[DONE ALL] All audio files and specs updated in {time.time() - t0:.1f}s!")

if __name__ == "__main__":
    main()
