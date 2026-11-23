"""
Batch Voice Generation for Episode 1: Lửng Mật (Scenes 03 to 06)
Executes single robust Communicate calls per scene with 8s cooldown.
Saves 48kHz WAV audio and word timelines in projects/tap-01-lung-mat/audio/
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

REMAINING_SCENES = [
    {
        "id": "scene_03",
        "title": "Act 3: Cơ Chế Sinh Tồn Độc Dị - Áo Giáp Cao Su & Lưỡi Hái",
        "text": """Vậy điều gì đã biến một con vật nhỏ bé trở thành cơn ác mộng di động? Bí mật nằm ở ba cơ chế sinh học độc dị mà mẹ thiên nhiên ưu ái ban tặng. Cơ chế thứ nhất là lớp da cao su lỏng lẻo kỳ quặc. Da của Lửng Mật dày hơn cả da trâu mộng, dày tới sáu milimét, nhưng nó không dính chặt vào cơ bắp mà lỏng lẻo như một chiếc áo khoác quá khổ. Khi một con báo hoa mai hay linh cẩu ngoạm chặt vào gáy Lửng Mật và ngỡ rằng đã tóm sống được con mồi, điều ma quỷ xảy ra: Lửng Mật có thể tự do xoay người một trăm tám mươi độ ngay bên trong chính lớp da của nó, rồi quay ngoắt hàm răng sắc nhọn cắn nát mũi và mắt của kẻ săn mồi! Cơ chế thứ hai là bộ vuốt đào hầm lưỡi hái. Hai bàn chân trước của nó trang bị những chiếc móng vuốt dài hơn năm centimet, cong vút và cứng như mũi khoan kim cương, xới tung tổ mối cứng như bê tông chỉ trong vài phút. Và cơ chế thứ ba là quả bom sinh học hậu môn. Túi xạ hương dưới đuôi Lửng Mật có thể phun ra một luồng khí nồng nặc mùi hôi thối đặc quánh, làm tê liệt khứu giác nhạy bén của bầy sư tử, khiến chúng choáng váng buồn nôn và thà nhịn đói còn hơn đứng gần gã bốc mùi này!"""
    },
    {
        "id": "scene_04",
        "title": "Act 4: Cú Bẻ Lái Của Tạo Hóa - Miễn Nhiễm Nọc Độc Thần Kinh",
        "text": """Nhưng những điều trên vẫn chưa là gì so với sở thích ăn uống điên rồ nhất hành tinh của Lửng Mật. Món ăn khoái khẩu của nó không chỉ là mật ong rừng, mà là những loài rắn độc chết chóc nhất: rắn phì châu Phi, rắn hổ mang thổi nọc và cả hổ mang chúa! Bạn có biết: một giọt nọc độc của rắn phì đủ để làm tan rữa các mô cơ và giết chết mười lăm người trưởng thành trong đau đớn tột cùng. Vậy điều gì sẽ xảy ra khi một con hổ mang khổng lồ cắn ngập đôi răng nanh đầy nọc độc thẳng vào mõm Lửng Mật? Liệu kẻ liều lĩnh này có phải trả giá bằng mạng sống hay có phép màu nào cứu rỗi nó? Câu trả lời là một cú bẻ lái kinh điển của tiến hóa! Các nhà khoa học phát hiện ra rằng, các thụ thể thần kinh trong cơ thể Lửng Mật đã bị đột biến qua hàng triệu năm, tạo thành lớp khiên phân tử ngăn chặn nọc độc liên kết vào tế bào. Khi bị rắn hổ mang cắn trúng, Lửng Mật sẽ từ từ lảo đảo, lăn đùng ra đất và rơi vào trạng thái hôn mê sâu suốt hai tiếng như một gã say rượu quắc cần câu. Nhưng khi độc tố tan hết, nó bật dậy, lắc đầu rũ lông tỉnh queo như vừa ngủ trưa dậy, và thản nhiên nhai nốt nửa con rắn còn lại!"""
    },
    {
        "id": "scene_05",
        "title": "Act 5: Đại Chiến Thiên Nhiên & Bậc Thầy Vượt Ngục Stoffel",
        "text": """Không chỉ sở hữu thân thể bất tử, Lửng Mật còn là những thiên tài bẻ khóa với trí thông minh khiến con người phải ngả mũ thán phục. Minh chứng sống động nhất chính là chú lửng mật huyền thoại Stoffel tại Trung tâm Phục hồi Hoang dã ở Nam Phi. Khi bị nhốt trong chuồng rào tường bê tông cao lút đầu, Stoffel đã dùng chân cào đất bùn, nặn thành những viên bi đất tròn to tướng rồi đẩy chúng vào góc tường, xếp chồng lên nhau thành một gò đất cao để nhảy vọt qua rào! Khi các nhân viên dọn sạch bùn đất, Stoffel gom những cành cây khô, dựng đứng vào tường làm thang leo. Họ dọn sạch cành cây, nó liền lăn những tảng đá lớn lại. Họ dọn sạch cả đá, Stoffel thậm chí đã rủ rê một con lửng cái cùng phòng, lừa con cái đứng sát góc tường để nó dẫm lên lưng con cái phóng ra ngoài! Và mục đích vượt ngục của nó là gì? Không phải để trốn vào rừng sâu hưởng tự do, mà là xông thẳng vào chuồng bầy sư tử kế bên, gầm gừ cà khịa và cắn đuôi các chúa sơn lâm to xác! Ngay cả khi bị ba con sư tử đực trưởng thành bao vây, Lửng Mật không bao giờ quay đầu bỏ chạy. Nó xù toàn bộ lông trên lưng, nhe hàm răng sắc nhọn, gầm rít và lao thẳng vào giữa bầy sư tử, khiến sư tử cũng phải lắc đầu lùi lại!"""
    },
    {
        "id": "scene_06",
        "title": "Act 6: Seamless Outro - Chuyển Tiếp Sang Ngày 2: Rái Cá Biển",
        "text": """Lửng Mật, sinh vật nhỏ bé nhưng mang linh hồn của một chiến binh bất khuất, minh chứng cho việc kích thước không quyết định bạn là ai trên đấu trường sinh tồn. Gã giang hồ thảo nguyên châu Phi này có thể là tay anh chị đáng gờm nhất trên đất liền. Nhưng nếu bạn nghĩ sự tàn bạo và khó lường chỉ thuộc về Lửng Mật thì bạn đã nhầm to! Nếu lặn xuống đại dương bao la, bạn sẽ bắt gặp một loài sinh vật nổi tiếng với vẻ ngoài siêu đáng yêu, hay nắm tay nhau ngủ trên mặt nước... nhưng ẩn sau đó lại là những hành vi tâm lý đen tối và rùng rợn bậc nhất thế giới tự nhiên: Rái Cá Biển! Hãy bấm ngay vào video đang xuất hiện trên màn hình để cùng khám phá bộ mặt thật kinh hoàng của loài vật dễ thương này trong tập tiếp theo nhé! Đừng quên bấm Đăng Ký kênh Vẽ Chuyện Muông Thú để đón xem những thước phim hoạt họa độc đáo tiếp theo!"""
    }
]

async def generate_scene(item: dict):
    scene_id = item["id"]
    title = item["title"]
    text = item["text"].strip()
    
    mp3_file = AUDIO_DIR / f"{scene_id}_raw.mp3"
    wav_file = AUDIO_DIR / f"{scene_id}.wav"
    words_json = AUDIO_DIR / f"{scene_id}_words.json"
    
    if wav_file.exists() and wav_file.stat().st_size > 500000 and words_json.exists():
        print(f"  [ĐÃ CÓ] {scene_id} -> Bỏ qua.")
        return
        
    print(f"\n>>> [TTS] Đang xử lý {scene_id}: {title} ({len(text)} ký tự)...", flush=True)
    
    max_retries = 3
    for attempt in range(max_retries):
        try:
            # 8s sleep between calls to avoid Microsoft rate limits
            await asyncio.sleep(8)
            comm = edge_tts.Communicate(text, VOICE, boundary="WordBoundary")
            words = []
            with open(mp3_file, "wb") as f:
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
            if words and mp3_file.exists() and mp3_file.stat().st_size > 1000:
                with open(words_json, "w", encoding="utf-8") as f:
                    json.dump(words, f, ensure_ascii=False, indent=2)
                break
            raise ValueError("Zero audio received")
        except Exception as e:
            print(f"    [Thử lại {attempt+1}/{max_retries}] Lỗi: {e}, chờ 12s...", flush=True)
            if mp3_file.exists():
                mp3_file.unlink()
            await asyncio.sleep(12)
            if attempt == max_retries - 1:
                raise
                
    # Convert MP3 to 48kHz WAV
    subprocess.run([
        "ffmpeg", "-y", "-i", str(mp3_file),
        "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le",
        str(wav_file)
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    
    if mp3_file.exists():
        mp3_file.unlink()
        
    probe = subprocess.check_output([
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(wav_file)
    ]).decode("utf-8").strip()
    dur = float(probe)
    print(f"  [HOÀN THÀNH {scene_id}] Thời lượng: {dur:.2f}s ({len(words)} từ khớp mốc thời gian)", flush=True)

async def main():
    print("=" * 60, flush=True)
    print("BẮT ĐẦU TẠO AUDIO CHO CÁC PHÂN CẢNH 3 ĐẾN 6", flush=True)
    print("=" * 60, flush=True)
    for s in REMAINING_SCENES:
        await generate_scene(s)
    print("\n" + "=" * 60, flush=True)
    print("TẤT CẢ PHÂN CẢNH 3 ĐẾN 6 ĐÃ HOÀN TẤT!", flush=True)
    print("=" * 60, flush=True)

if __name__ == "__main__":
    asyncio.run(main())
