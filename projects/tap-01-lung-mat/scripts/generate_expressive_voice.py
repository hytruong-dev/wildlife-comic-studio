"""
Expressive Neural Voice Generator for Episode 1: Lửng Mật
- Uses Microsoft Neural Voice: vi-VN-NamMinhNeural
- Fast Pacing: rate = +22%
- Dramatic Inflection with natural punctuation (..., !, ?, ,)
- Word-boundary timestamp synchronization
- Broadcast Audio Mastering via FFmpeg (Warm EQ, Crisp Presence, Dynamic Compression)
"""

import asyncio
import json
import subprocess
from pathlib import Path
import aiohttp

from edge_tts.constants import WSS_URL, SEC_MS_GEC_VERSION, WSS_HEADERS
from edge_tts.drm import DRM
from edge_tts.communicate import connect_id, get_headers_and_data

SCRIPT_DIR = Path(__file__).resolve().parent
PROJ = SCRIPT_DIR.parent
AUDIO_DIR = PROJ / "audio_expressive"
AUDIO_DIR.mkdir(parents=True, exist_ok=True)

VOICE = "vi-VN-NamMinhNeural"
RATE = "+22%"

SCENES = [
    {
        "id": "scene01",
        "title": "Act 1: The Myth-Buster Hook - Gã Chí Phèo Số Một Hành Tinh",
        "text": (
            "Bạn nghĩ ai mới thực sự là bá chủ của thảo nguyên châu Phi? "
            "Là sư tử với tiếng gầm rung chuyển rừng già? "
            "Là đàn linh cẩu tàn bạo, hay những con voi khổng lồ nặng vài tấn? "
            "Quên hết đi! "
            "Trong thế giới hoang dã khắc nghiệt, có một sinh vật kỳ dị chỉ cao chưa đầy ba mươi centimet, "
            "nặng vỏn vẹn mười hai kilôgam... nhưng lại khiến cả chúa sơn lâm nhìn thấy từ đằng xa cũng phải lắc đầu ngao ngán, "
            "tự động né sang một bên đường! "
            "Giới khoa học gọi nó là Mellivora capensis. "
            "Còn trên giang hồ muôn loài, nó được tôn làm Chí Phèo số một hành tinh: Lửng Mật! "
            "Một gã lùn tịt, đầu húi cua hai màu lông tương phản, "
            "bước đi khệnh khạng với thái độ bất cần đời, và đặc biệt là sở hữu một quả não hoàn toàn không có khái niệm về cái chết!"
        )
    },
    {
        "id": "scene02",
        "title": "Act 2: Bảng Chỉ Số Sinh Tồn RPG Stats",
        "text": (
            "Nếu đưa Lửng Mật vào một tựa game nhập vai sinh tồn, chắc chắn nhà phát hành game sẽ bị người chơi kiện vì tạo ra một nhân vật quá sức mất cân bằng! "
            "Hãy cùng soi bảng chỉ số nhân vật độc nhất vô nhị này! "
            "Đầu tiên là sức mạnh thể chất, đạt tám mươi lăm điểm! Đừng nhìn thân hình tròn lẳn như khúc gỗ mà lầm. "
            "Dưới lớp lông đó là các bó cơ nén đặc với mật độ khủng khiếp. Lửng Mật có thể kéo lê một xác linh dương nặng gấp ba lần cơ thể nó! "
            "Thứ hai là chỉ số phòng thủ, chạm nóc chín mươi chín trên một trăm! "
            "Nó khoác lên mình một lớp giáp cao su di động dày tới sáu milimét, chống lại từ răng nanh sư tử, nọc bọ cạp đến cả những mũi lao sắc nhọn! "
            "Thứ ba là trí thông minh, chín mươi điểm. Đây không phải một kẻ hữu dũng vô mưu, mà là bậc thầy bẻ khóa và tư duy chiến thuật đỉnh cao! "
            "Tiếp theo là độ lì đòn, phá vỡ mọi thang đo với chín trăm chín mươi chín điểm! Trong từ điển của Lửng Mật, chỉ có tiến lên hoặc đối thủ bỏ chạy, tuyệt đối không có nút thoái lui! "
            "Và chỉ số cuối cùng, chấn động nhất: cảm giác sợ hãi là không điểm tròn trĩnh! "
            "Hạch hạnh nhân nơi tiếp nhận nỗi sợ trong não bộ dường như đã bị tạo hóa tháo dỡ hoàn toàn khỏi loài vật này!"
        )
    },
    {
        "id": "scene03",
        "title": "Act 3: Cơ Chế Sinh Tồn Độc Dị - Áo Giáp Cao Su & Lưỡi Hái",
        "text": (
            "Vậy điều gì đã biến một con vật nhỏ bé trở thành cơn ác mộng di động? "
            "Bí mật nằm ở ba cơ chế sinh học độc dị mà mẹ thiên nhiên ưu ái ban tặng! "
            "Cơ chế thứ nhất là lớp da cao su lỏng lẻo kỳ quặc. "
            "Da của Lửng Mật dày hơn cả da trâu mộng, nhưng lỏng lẻo như một chiếc áo khoác quá khổ. "
            "Khi một con báo hoa mai ngoạm chặt vào gáy Lửng Mật, điều ma quỷ xảy ra: "
            "Lửng Mật có thể tự do xoay người một trăm tám mươi độ ngay bên trong chính lớp da của nó, "
            "rồi quay ngoắt hàm răng sắc nhọn cắn nát mũi và mắt của kẻ săn mồi! "
            "Một cú phản đòn đau đớn khiến bất kỳ con báo nào cũng phải hoảng loạn nhả ra ngay lập tức! "
            "Cơ chế thứ hai là bộ vuốt đào hầm lưỡi hái. "
            "Hai bàn chân trước trang bị những chiếc móng vuốt dài hơn năm centimet, cong vút và cứng như mũi khoan kim cương! "
            "Nó có thể xới tung tổ mối cứng như bê tông chỉ trong vài phút! "
            "Và cơ chế thứ ba là quả bom sinh học hậu môn. "
            "Túi xạ hương dưới đuôi Lửng Mật có thể phun ra một luồng khí nồng nặc mùi hôi thối đặc quánh, "
            "làm tê liệt khứu giác siêu nhạy của bầy sư tử, khiến chúng choáng váng buồn nôn và thà nhịn đói còn hơn đứng gần gã bốc mùi này!"
        )
    },
    {
        "id": "scene04",
        "title": "Act 4: Cú Bẻ Lái Của Tạo Hóa - Miễn Nhiễm Nọc Độc Thần Kinh",
        "text": (
            "Nhưng những điều trên vẫn chưa là gì so với sở thích ăn uống điên rồ nhất hành tinh của Lửng Mật! "
            "Món ăn khoái khẩu của nó chính là những loài rắn độc chết chóc nhất: "
            "rắn phì châu Phi, rắn hổ mang thổi nọc và cả hổ mang chúa! "
            "Một giọt nọc độc rắn phì đủ để giết chết mười lăm người trưởng thành trong đau đớn tột cùng. "
            "Vậy điều gì sẽ xảy ra khi một con hổ mang khổng lồ cắn ngập đôi răng nanh đầy nọc độc vào mõm Lửng Mật? "
            "Câu trả lời là một cú bẻ lái kinh điển của tiến hóa! "
            "Các thụ thể thần kinh trong cơ thể Lửng Mật đã bị đột biến, hoạt động như một lớp khiên chắn phân tử, "
            "khiến độc tố thần kinh của rắn không thể bám vào để làm tê liệt hệ hô hấp! "
            "Khi bị rắn hổ mang cắn trúng, Lửng Mật sẽ từ từ lảo đảo, lăn đùng ra đất và rơi vào trạng thái hôn mê sâu giống như một gã say xỉn quắc cần câu! "
            "Tim đập chậm lại, toàn thân cứng đờ suốt hai đến ba tiếng đồng hồ. "
            "Nhưng không! Khi gan và hệ miễn dịch trung hòa hết độc tố, "
            "Lửng Mật bất ngờ mở mắt, đứng dậy lắc đầu rũ lông như vừa ngủ trưa dậy, và tỉnh queo cúi xuống nhai nốt khúc đuôi của con rắn vừa cắn nó!"
        )
    },
    {
        "id": "scene05",
        "title": "Act 5: Đại Chiến Thiên Nhiên & Bậc Thầy Vượt Ngục Stoffel",
        "text": (
            "Không chỉ sở hữu thân thể bất tử, Lửng Mật còn là những thiên tài bẻ khóa với chỉ số thông minh khiến con người phải ngả mũ thán phục! "
            "Minh chứng sống động nhất chính là Stoffel, chú lửng mật huyền thoại tại Trung tâm Phục hồi Hoang dã ở Nam Phi. "
            "Ban đầu, các nhân viên nhốt Stoffel trong một khu chuồng rào tường bê tông cao lút đầu. "
            "Stoffel đã dùng chân cào đất bùn, nặn thành những viên bi tròn to tướng rồi xếp chồng lên nhau thành gò đất cao để nhảy vọt qua rào! "
            "Khi bị dọn sạch bùn đất, Stoffel gom những cành cây khô làm thang leo. Họ dọn sạch cành cây, nó liền lăn những tảng đá lớn lại! "
            "Và mục đích vượt ngục của nó là gì? "
            "Không phải để trốn vào rừng sâu, mà là để xông thẳng vào chuồng bầy sư tử kế bên, gầm gừ cà khịa và cắn đuôi các chúa sơn lâm to xác! "
            "Ngay cả khi bị ba con sư tử đực trưởng thành bao vây, Lửng Mật không bao giờ bỏ chạy. "
            "Nó xù toàn bộ lông trên lưng, nhe hàm răng sắc nhọn, gầm rít như một chiếc máy cưa và lao thẳng vào giữa bầy sư tử! "
            "Thái độ điên cuồng đó khiến sư tử nhận ra: ăn được miếng thịt dai nhách này thì cũng mất nửa cái mũi, thôi lùi lại cho lành!"
        )
    },
    {
        "id": "scene06",
        "title": "Act 6: Seamless Outro - Chuyển Tiếp Sang Ngày 2: Rái Cá Biển",
        "text": (
            "Lửng Mật, sinh vật nhỏ bé nhưng mang linh hồn của một chiến binh bất khuất, "
            "minh chứng cho việc kích thước không quyết định bạn là ai trên đấu trường sinh tồn! "
            "Gã giang hồ thảo nguyên này có thể là tay anh chị đáng gờm nhất trên đất liền. "
            "Nhưng nếu bạn nghĩ sự tàn bạo và khó lường chỉ thuộc về Lửng Mật thì bạn đã nhầm to! "
            "Nếu lặn xuống đại dương bao la, bạn sẽ bắt gặp một loài sinh vật nổi tiếng với vẻ ngoài siêu đáng yêu, "
            "hay nắm tay nhau ngủ trên mặt nước... nhưng ẩn sau đó lại là những hành vi tâm lý đen tối và rùng rợn bậc nhất thế giới tự nhiên: "
            "Rái Cá Biển! "
            "Hãy bấm ngay vào video đang xuất hiện trên màn hình để cùng khám phá bộ mặt thật kinh hoàng của loài vật dễ thương này trong tập tiếp theo nhé! "
            "Đừng quên bấm Đăng Ký kênh để không bỏ lỡ những câu chuyện hoang dã kỳ thú nhất!"
        )
    }
]

async def synthesize_segment(clean_text: str, out_raw_mp3: Path, out_words_json: Path):
    gec = DRM.generate_sec_ms_gec()
    url = f"{WSS_URL}&ConnectionId={connect_id()}&Sec-MS-GEC={gec}&Sec-MS-GEC-Version={SEC_MS_GEC_VERSION}"
    headers = DRM.headers_with_muid(WSS_HEADERS)
    audio_data = bytearray()
    words = []
    
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect(url, headers=headers) as ws:
            config_req = (
                "X-Timestamp:Mon Nov 02 2026 18:00:00 GMT+0700\r\n"
                "Content-Type:application/json; charset=utf-8\r\n"
                "Path:speech.config\r\n\r\n"
                '{"context":{"synthesis":{"audio":{"metadataoptions":{"sentenceBoundaryEnabled":"false","wordBoundaryEnabled":"true"},"outputFormat":"audio-24khz-48kbitrate-mono-mp3"}}}}\r\n'
            )
            await ws.send_str(config_req)
            
            # Clean text escaped
            esc = clean_text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            ssml = (
                f'<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="vi-VN">'
                f'<voice name="{VOICE}">'
                f'<prosody rate="{RATE}">'
                f'{esc}'
                f'</prosody>'
                f'</voice></speak>'
            )
            ssml_req = (
                f"X-RequestId:{connect_id()}\r\n"
                "Content-Type:application/ssml+xml\r\n"
                "X-Timestamp:Mon Nov 02 2026 18:00:00 GMT+0700\r\n"
                "Path:ssml\r\n\r\n"
                + ssml
            )
            await ws.send_str(ssml_req)
            
            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.BINARY:
                    if len(msg.data) >= 2:
                        header_len = int.from_bytes(msg.data[:2], "big")
                        params, data = get_headers_and_data(msg.data, header_len)
                        if params.get(b"Path") == b"audio" and params.get(b"Content-Type") == b"audio/mpeg":
                            audio_data.extend(data)
                elif msg.type == aiohttp.WSMsgType.TEXT:
                    if "turn.end" in msg.data:
                        break
                    elif "audio.metadata" in msg.data:
                        idx = msg.data.find("\r\n\r\n")
                        if idx != -1:
                            try:
                                meta = json.loads(msg.data[idx+4:])
                                for item in meta.get("Metadata", []):
                                    if item.get("Type") == "WordBoundary":
                                        d = item["Data"]
                                        w_text = d["text"]["Text"]
                                        start_ms = d["Offset"] / 10000.0
                                        dur_ms = d["Duration"] / 10000.0
                                        words.append({
                                            "word": w_text,
                                            "startMs": round(start_ms, 1),
                                            "endMs": round(start_ms + dur_ms, 1)
                                        })
                            except Exception:
                                pass
                elif msg.type in (aiohttp.WSMsgType.CLOSED, aiohttp.WSMsgType.CLOSING):
                    break

    with open(out_raw_mp3, "wb") as f:
        f.write(audio_data)
    with open(out_words_json, "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)

def master_audio(in_mp3: Path, out_wav: Path):
    """
    Broadcast Audio Mastering Filter:
    - Highpass 80Hz (removes low rumbling)
    - Lowpass 14000Hz (smooths high frequency harshness)
    - Equalizer: warm bass bump at 140Hz, vocal presence boost at 3200Hz
    - Dynamic compressor for consistent punchy loudness
    - 48kHz 16-bit PCM WAV standard
    """
    af_filter = (
        "highpass=f=80,lowpass=f=14000,"
        "equalizer=f=140:width_type=o:w=1.0:g=2.5,"
        "equalizer=f=3200:width_type=o:w=1.0:g=2.0,"
        "acompressor=threshold=-16dB:ratio=3:attack=5:release=50,"
        "volume=1.25"
    )
    cmd = [
        "ffmpeg", "-y",
        "-i", str(in_mp3),
        "-af", af_filter,
        "-ar", "48000",
        "-ac", "2",
        "-c:a", "pcm_s16le",
        str(out_wav)
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

async def generate_all_scenes():
    print("======================================================================")
    print("STARTING EXPRESSIVE NEURAL VOICE GENERATION (+22% RATE + MASTERING)")
    print("======================================================================")
    total_dur = 0.0
    
    for sc in SCENES:
        sid = sc["id"]
        raw_mp3 = AUDIO_DIR / f"{sid}_fast_raw.mp3"
        words_json = AUDIO_DIR / f"{sid}_fast_words.json"
        master_wav = AUDIO_DIR / f"{sid}_fast.wav"
        
        print(f"\n>>> Generating {sid}: {sc['title']}...")
        await synthesize_segment(sc["text"], raw_mp3, words_json)
        
        # Apply broadcast mastering
        master_audio(raw_mp3, master_wav)
        
        # Get duration
        cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(master_wav)]
        dur = float(subprocess.check_output(cmd).decode().strip())
        total_dur += dur
        
        with open(words_json, "r", encoding="utf-8") as f:
            w_list = json.load(f)
            
        print(f"    [DONE] {sid} mastered: {dur:.2f}s ({len(w_list)} words captured) -> {master_wav.name}")
        await asyncio.sleep(1.0)  # respectful gap
        
    print(f"\nAll scenes generated! Total Duration: {total_dur:.2f}s ({int(total_dur//60)}m {total_dur%60:.1f}s)")

if __name__ == "__main__":
    asyncio.run(generate_all_scenes())
