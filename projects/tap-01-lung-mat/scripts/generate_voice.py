"""
Robust Voice Generator for Episode 1: Lửng Mật (Honey Badger)
- Caches already generated scenes
- Respects Microsoft Edge-TTS rate limits with 3-5s cooldown between calls
- Outputs 48kHz WAV audio and millisecond-accurate word timelines
"""

import asyncio
import json
import subprocess
import time
from pathlib import Path
import edge_tts

SCRIPT_DIR = Path(__file__).resolve().parent
PROJ = SCRIPT_DIR.parent
AUDIO_DIR = PROJ / "audio"
AUDIO_DIR.mkdir(parents=True, exist_ok=True)

VOICE = "vi-VN-NamMinhNeural"

SCENES_PARAGRAPHS = [
    {
        "id": "scene_01",
        "title": "Act 1: The Myth-Buster Hook - Gã Chí Phèo Số Một Hành Tinh",
        "paragraphs": [
            "Bạn nghĩ ai mới thực sự là bá chủ của thảo nguyên châu Phi? Là sư tử với tiếng gầm rung chuyển rừng già? Là đàn linh cẩu tàn bạo, hay những con voi khổng lồ nặng vài tấn? Quên hết đi! Trong thế giới hoang dã khắc nghiệt, có một sinh vật kỳ dị chỉ cao chưa đầy ba mươi centimet, nặng vỏn vẹn mười hai kilôgam, nhưng lại khiến cả chúa sơn lâm nhìn thấy từ đằng xa cũng phải lắc đầu ngao ngán, tự động né sang một bên đường.",
            "Giới khoa học gọi nó là Mellivora capensis. Còn trên giang hồ muôn loài, nó được tôn làm Chí Phèo số một hành tinh: Lửng Mật! Một gã lùn tịt, đầu húi cua hai màu lông tương phản, bước đi khệnh khạng với thái độ bất cần đời, và đặc biệt là sở hữu một quả não hoàn toàn không có khái niệm về cái chết!"
        ]
    },
    {
        "id": "scene_02",
        "title": "Act 2: Bảng Chỉ Số Sinh Tồn RPG Stats",
        "paragraphs": [
            "Nếu đưa Lửng Mật vào một tựa game nhập vai sinh tồn, chắc chắn nhà phát hành game sẽ bị người chơi kiện vì tạo ra một nhân vật quá sức mất cân bằng. Hãy cùng soi bảng chỉ số nhân vật độc nhất vô nhị này! Đầu tiên là sức mạnh thể chất, đạt tám mươi lăm điểm. Đừng nhìn thân hình tròn lẳn như khúc gỗ mà lầm! Dưới lớp lông đó là các bó cơ nén đặc với mật độ khủng khiếp. Lửng Mật có thể kéo lê một xác linh dương nặng gấp ba lần trọng lượng cơ thể nó.",
            "Thứ hai là chỉ số phòng thủ, chạm nóc chín mươi chín trên một trăm! Nó khoác lên mình một lớp giáp cao su di động dày tới sáu milimét, chống lại từ răng nanh sư tử, nọc bọ cạp đến cả những mũi lao sắc nhọn của thổ dân. Thứ ba là trí thông minh, chín mươi điểm. Đây không phải một kẻ hữu dũng vô mưu, mà là bậc thầy bẻ khóa, chế tạo công cụ và tư duy chiến thuật đỉnh cao.",
            "Tiếp theo là độ lì đòn và lầy lội, phá vỡ mọi thang đo với chín trăm chín mươi chín điểm! Trong từ điển của Lửng Mật, chỉ có tiến lên hoặc đối thủ bỏ chạy, tuyệt đối không có nút thoái lui. Và chỉ số cuối cùng, chấn động nhất: cảm giác sợ hãi là không điểm tròn trĩnh! Các nhà sinh vật học khẳng định, hạch hạnh nhân trong não bộ, nơi tiếp nhận nỗi sợ, dường như đã bị tạo hóa tháo dỡ hoàn toàn khỏi loài vật này!"
        ]
    },
    {
        "id": "scene_03",
        "title": "Act 3: Cơ Chế Sinh Tồn Độc Dị - Áo Giáp Cao Su & Lưỡi Hái",
        "paragraphs": [
            "Vậy điều gì đã biến một con vật nhỏ bé trở thành cơn ác mộng di động? Bí mật nằm ở ba cơ chế sinh học độc dị mà mẹ thiên nhiên ưu ái ban tặng. Cơ chế thứ nhất là lớp da cao su lỏng lẻo kỳ quặc. Da của Lửng Mật dày hơn cả da trâu mộng, nhưng nó không dính chặt vào cơ bắp mà lỏng lẻo như một chiếc áo khoác quá khổ.",
            "Hãy tưởng tượng: khi một con báo hoa mai hay linh cẩu ngoạm chặt vào gáy Lửng Mật và ngỡ rằng đã tóm sống được con mồi, điều ma quỷ xảy ra: Lửng Mật có thể tự do xoay người một trăm tám mươi độ ngay bên trong chính lớp da của nó, rồi quay ngoắt hàm răng sắc nhọn cắn nát mũi và mắt của kẻ săn mồi! Một cú phản đòn đau đớn khiến bất kỳ con báo nào cũng phải hoảng loạn nhả ra ngay lập tức!",
            "Cơ chế thứ hai là bộ vuốt đào hầm lưỡi hái. Hai bàn chân trước của nó trang bị những chiếc móng vuốt dài hơn năm centimet, cong vút và cứng như mũi khoan kim cương. Nó có thể xới tung tổ mối cứng như bê tông chỉ trong vài phút, hay đào sâu vào lòng đất tạo nơi ẩn nấp nhanh hơn một người cầm xẻng xúc đất.",
            "Và cơ chế thứ ba là quả bom sinh học hậu môn. Tương tự như loài chồn hôi nhưng ở cấp độ hủy diệt hơn, túi xạ hương dưới đuôi Lửng Mật có thể phun ra một luồng khí nồng nặc mùi hôi thối đặc quánh. Thứ mùi này không chỉ xua đuổi ong vò vẽ khi nó cướp tổ mật, mà còn làm tê liệt khứu giác siêu nhạy của bầy sư tử, khiến chúng choáng váng buồn nôn và thà nhịn đói còn hơn đứng gần gã bốc mùi này!"
        ]
    },
    {
        "id": "scene_04",
        "title": "Act 4: Cú Bẻ Lái Của Tạo Hóa - Miễn Nhiễm Nọc Độc Thần Kinh",
        "paragraphs": [
            "Nhưng những điều trên vẫn chưa là gì so với sở thích ăn uống điên rồ nhất hành tinh của Lửng Mật. Món ăn khoái khẩu của nó không chỉ là mật ong rừng, mà là những loài rắn độc chết chóc nhất: rắn phì châu Phi, rắn hổ mang thổi nọc và cả hổ mang chúa! Bạn có biết: một giọt nọc độc của rắn phì đủ để làm tan rữa các mô cơ và giết chết mười lăm người trưởng thành trong đau đớn tột cùng.",
            "Vậy điều gì sẽ xảy ra khi một con hổ mang khổng lồ cắn ngập đôi răng nanh đầy nọc độc thẳng vào mõm Lửng Mật? Liệu gã Chí Phèo này có phải trả giá bằng tính mạng cho sự liều lĩnh điên rồ của mình không? Câu trả lời là một cú bẻ lái kinh điển của tiến hóa! Các nhà di truyền học phát hiện ra rằng, các thụ thể thần kinh trong cơ thể Lửng Mật đã bị đột biến qua hàng triệu năm. Đột biến này hoạt động như một lớp khiên chắn phân tử, khiến độc tố thần kinh của rắn không thể bám vào để làm tê liệt các cơ quan hô hấp!",
            "Khi bị rắn hổ mang cắn trúng, nọc độc vẫn ngấm vào máu. Lúc này, Lửng Mật sẽ từ từ lảo đảo, lăn đùng ra đất và rơi vào trạng thái hôn mê sâu giống hệt như một gã bợm rượu say xỉn quắc cần câu! Tim nó đập chậm lại, toàn thân cứng đờ suốt hai đến ba tiếng đồng hồ. Đối thủ tưởng nó đã chết. Nhưng không! Khi gan và hệ miễn dịch trung hòa hết độc tố, Lửng Mật bất ngờ mở mắt, chớp chớp vài cái, đứng dậy lắc đầu rũ lông như vừa ngủ trưa dậy, và tỉnh queo cúi xuống nhai nốt khúc đuôi của con rắn độc vừa cắn nó!"
        ]
    },
    {
        "id": "scene_05",
        "title": "Act 5: Đại Chiến Thiên Nhiên & Bậc Thầy Vượt Ngục Stoffel",
        "paragraphs": [
            "Không chỉ sở hữu thân thể bất tử, Lửng Mật còn là những thiên tài bẻ khóa với chỉ số thông minh khiến con người phải ngả mũ thán phục. Minh chứng sống động nhất chính là Stoffel, chú lửng mật huyền thoại tại Trung tâm Phục hồi Hoang dã ở Nam Phi. Stoffel nổi tiếng đến mức được đài BBC làm riêng một bộ phim tài liệu về tài năng vượt ngục.",
            "Ban đầu, các nhân viên nhốt Stoffel trong một khu chuồng rào tường bê tông cao lút đầu. Bạn nghĩ tường cao sẽ giữ chân được nó? Stoffel đã dùng chân cào đất bùn, nặn thành những viên bi đất tròn to tướng rồi đẩy chúng vào góc tường, xếp chồng lên nhau thành một gò đất cao để nhảy vọt qua rào! Khi các nhân viên dọn sạch bùn đất, Stoffel gom những cành cây khô, dựng đứng vào tường làm thang leo. Họ dọn sạch cành cây, nó liền lăn những tảng đá lớn lại.",
            "Họ dọn sạch cả đá, Stoffel thậm chí đã rủ rê một con lửng mật cái khác cùng phòng, lừa con cái đứng sát góc tường để nó dẫm lên lưng con cái phóng ra ngoài! Và mục đích vượt ngục của nó là gì? Không phải để trốn vào rừng sâu hưởng tự do, mà là để xông thẳng vào chuồng bầy sư tử kế bên, gầm gừ cà khịa và cắn đuôi các chúa sơn lâm to xác! Ngay cả khi bị ba con sư tử đực trưởng thành bao vây, Lửng Mật không bao giờ quay đầu bỏ chạy. Nó xù toàn bộ lông trên lưng, nhe hàm răng sắc nhọn, gầm rít như một chiếc máy cưa và lao thẳng vào giữa bầy sư tử. Thái độ điên cuồng đó khiến sư tử nhận ra: ăn được miếng thịt dai nhách này thì cũng mất nửa cái mũi, thôi lùi lại cho lành!"
        ]
    },
    {
        "id": "scene_06",
        "title": "Act 6: Seamless Outro - Chuyển Tiếp Sang Ngày 2: Rái Cá Biển",
        "paragraphs": [
            "Lửng Mật, sinh vật nhỏ bé nhưng mang linh hồn của một chiến binh bất khuất, minh chứng cho việc kích thước không quyết định bạn là ai trên đấu trường sinh tồn. Gã giang hồ thảo nguyên châu Phi này có thể là tay anh chị đáng gờm nhất trên đất liền. Nhưng nếu bạn nghĩ sự tàn bạo và khó lường chỉ thuộc về Lửng Mật thì bạn đã nhầm to!",
            "Nếu lặn xuống đại dương bao la, bạn sẽ bắt gặp một loài sinh vật nổi tiếng với vẻ ngoài siêu đáng yêu, hay nắm tay nhau ngủ trên mặt nước... nhưng ẩn sau đó lại là những hành vi tâm lý đen tối và rùng rợn bậc nhất thế giới tự nhiên: Rái Cá Biển! Hãy bấm ngay vào video đang xuất hiện trên màn hình để cùng khám phá bộ mặt thật kinh hoàng của loài vật dễ thương này trong tập tiếp theo nhé! Đừng quên bấm Đăng Ký kênh Vẽ Chuyện Muông Thú để không bỏ lỡ những thước phim hoạt họa độc đáo!"
        ]
    }
]

async def generate_single_paragraph(text: str, temp_file: Path):
    max_retries = 5
    for attempt in range(max_retries):
        try:
            comm = edge_tts.Communicate(text, VOICE, boundary="WordBoundary")
            words = []
            with open(temp_file, "wb") as f:
                async for chunk in comm.stream():
                    if chunk["type"] == "audio":
                        f.write(chunk["data"])
                    elif chunk["type"] == "WordBoundary":
                        start_ms = int(chunk["offset"] / 10000)
                        duration_ms = int(chunk["duration"] / 10000)
                        words.append({
                            "word": chunk["text"],
                            "startMs": start_ms,
                            "endMs": start_ms + duration_ms,
                            "durationMs": duration_ms
                        })
            if words and temp_file.exists() and temp_file.stat().st_size > 1000:
                return words
            raise ValueError("Zero audio chunks or empty words received")
        except Exception as e:
            wait_s = 4 * (attempt + 1)
            print(f"    [Thử lại {attempt+1}/{max_retries}] Lỗi TTS: {e}. Đang hạ nhiệt {wait_s}s...", flush=True)
            if temp_file.exists():
                temp_file.unlink()
            await asyncio.sleep(wait_s)
            if attempt == max_retries - 1:
                raise

async def process_scene(scene: dict):
    scene_id = scene["id"]
    title = scene["title"]
    final_wav = AUDIO_DIR / f"{scene_id}.wav"
    words_json = AUDIO_DIR / f"{scene_id}_words.json"
    
    # Check if already generated cleanly
    if final_wav.exists() and final_wav.stat().st_size > 500000 and words_json.exists():
        probe = subprocess.check_output([
            "ffprobe", "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            str(final_wav)
        ]).decode("utf-8").strip()
        dur = float(probe)
        words = json.loads(words_json.read_text(encoding="utf-8"))
        print(f"  [ĐÃ CÓ SẴN] {scene_id}: {dur:.2f}s ({len(words)} từ) -> Bỏ qua sinh lại.", flush=True)
        return dur

    paragraphs = scene["paragraphs"]
    print(f"\n>>> Đang tạo giọng đọc cho {scene_id}: {title} ({len(paragraphs)} đoạn văn)...", flush=True)
    
    part_files = []
    all_words = []
    cumulative_ms = 0
    
    for i, p in enumerate(paragraphs):
        p_file = AUDIO_DIR / f"{scene_id}_part{i+1}.mp3"
        print(f"  - Đoạn {i+1}/{len(paragraphs)} ({len(p)} ký tự)...", flush=True)
        words = await generate_single_paragraph(p, p_file)
        
        # Shift word timings by cumulative duration
        for w in words:
            all_words.append({
                "word": w["word"],
                "startMs": w["startMs"] + cumulative_ms,
                "endMs": w["endMs"] + cumulative_ms,
                "durationMs": w["durationMs"]
            })
            
        probe = subprocess.check_output([
            "ffprobe", "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            str(p_file)
        ]).decode("utf-8").strip()
        p_dur_ms = int(float(probe) * 1000)
        cumulative_ms += p_dur_ms
        part_files.append(p_file)
        
        # Cooldown between paragraphs to avoid Microsoft rate-limits
        await asyncio.sleep(2.5)
        
    # Concat all paragraph MP3s into final 48kHz WAV
    concat_list = AUDIO_DIR / f"{scene_id}_concat.txt"
    with open(concat_list, "w", encoding="utf-8") as f:
        for pf in part_files:
            f.write(f"file '{pf.resolve()}'\n")
            
    subprocess.run([
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0",
        "-i", str(concat_list),
        "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le",
        str(final_wav)
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    
    # Clean up part files
    if concat_list.exists():
        concat_list.unlink()
    for pf in part_files:
        if pf.exists():
            pf.unlink()
        
    with open(words_json, "w", encoding="utf-8") as f:
        json.dump(all_words, f, ensure_ascii=False, indent=2)
        
    probe_final = subprocess.check_output([
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(final_wav)
    ]).decode("utf-8").strip()
    final_dur = float(probe_final)
    print(f"  [HOÀN TẤT {scene_id}] Thời lượng: {final_dur:.2f}s ({len(all_words)} từ)", flush=True)
    
    # Cooldown between scenes
    await asyncio.sleep(3.0)
    return final_dur

async def main():
    print("=" * 70, flush=True)
    print("KHỞI CHẠY TIẾN TRÌNH SINH GIỌNG ĐỌC FULL 6 SCENES CHO TẬP 1: LỬNG MẬT", flush=True)
    print("=" * 70, flush=True)
    total_dur = 0.0
    for s in SCENES_PARAGRAPHS:
        dur = await process_scene(s)
        total_dur += dur
        
    mins = int(total_dur // 60)
    secs = int(total_dur % 60)
    print("\n" + "=" * 70, flush=True)
    print(f"HOÀN THÀNH TẤT CẢ 6 SCENES!", flush=True)
    print(f"TỔNG THỜI LƯỢNG GIỌNG ĐỌC: {mins} phút {secs} giây ({total_dur:.2f} giây)", flush=True)
    print(f"ĐÃ LƯU TẠI: {AUDIO_DIR}", flush=True)
    print("=" * 70, flush=True)

if __name__ == "__main__":
    asyncio.run(main())
