# SETUP MÁY MỚI — đóng gói toàn bộ môi trường sản xuất "Vẽ Chuyện Hoang Dã"

> **Dành cho AI (Cursor / Claude / AntiGravity) trên máy mới.** Khi chủ kênh nói *"đọc toàn bộ dự án"*, *"cài đặt máy mới"*,
> *"setup"*: làm đúng thứ tự dưới đây, **tự chạy lệnh, không hỏi lại**, chỉ dừng ở 2 bước bắt buộc làm tay (mục 6, mục 8).
> Xong thì đọc `AGENTS.md` để đồng bộ bộ nhớ và sẵn sàng "làm tập tiếp theo".

Mục tiêu: video ra **giống hệt** máy gốc. Chất lượng phụ thuộc 4 thứ, đều được khóa ở đây:

1. **Phiên bản phần mềm** — khóa trong `requirements.txt`, `package-lock.json`, commit của `tools/`.
2. **Giọng đọc** — VoiceStudio 0.5.3 + model OmniVoice revision `c5fdb5cc` + giọng mẫu trong `assets/voice_refs/`.
3. **Tài sản** — font, bàn tay, nhạc nền, intro/outro, hiệu ứng âm thanh trong `assets/` (có trong git).
4. **Bộ nhớ đạo diễn** — `.agent_memory/` (gu thẩm mỹ, bài học), `.agents/skills/`, `docs/`, `config/` (có trong git).

---

## 0. Cách nhanh nhất (1 lệnh)

```powershell
git clone https://github.com/hytruong-dev/wildlife-comic-studio.git
cd wildlife-comic-studio
powershell -ExecutionPolicy Bypass -File scripts\setup_new_machine.ps1
```

Script tự cài mục 1-5 và 7, kiểm mục 6 và 8, rồi in bảng **OK / THIEU**. Chạy lại bao nhiêu lần cũng được.
Chỉ kiểm tra mà không cài gì: thêm `-CheckOnly`. Còn dòng THIEU nào thì làm theo mục tương ứng dưới đây.

---

## 1. Phần mềm hệ thống

| Phần mềm | Phiên bản máy gốc | Cài (winget) | Dùng cho |
|---|---|---|---|
| Git | 2.55 | `winget install Git.Git` | clone dự án + `tools/` |
| Python | **3.14.4** (≥ 3.11) | `winget install Python.Python.3.14` | toàn bộ pipeline (`src/episode/pipeline.py`) |
| Node.js | **24.15** (≥ 20) | `winget install OpenJS.NodeJS` | Playwright: ảnh Gemini, upload YouTube |
| FFmpeg | **9.0 full build** (gyan.dev) | `winget install Gyan.FFmpeg` | ghép video, âm thanh, loudness |
| Google Chrome | bản ổn định | `winget install Google.Chrome` | `gemini_gen.cjs`, `upload_youtube.cjs` chạy `channel: 'chrome'` |

Sau khi cài: **mở terminal mới** để PATH có `python`, `node`, `ffmpeg`. Kiểm: `python --version; node --version; ffmpeg -version`.

## 2. Python packages của pipeline

```powershell
python -m pip install -r requirements.txt
```

Khóa đúng phiên bản máy gốc: faster-whisper 1.2.1, opencv-python 5.0.0.93, numpy 2.5.1, scipy 1.18.1, scikit-image 0.26.0,
pillow 12.3.0, soundfile 0.14.0, yt-dlp 2026.10.26, requests, beautifulsoup4… (xem file). **Không** cài torch ở đây — torch nằm
trong venv riêng của VoiceStudio (mục 6).

## 3. Node packages

```powershell
npm ci          # dùng package-lock.json -> playwright 1.64.1, remotion, roughjs, opentype.js, gsap
```

Pipeline **không cần** `npx playwright install` vì mọi script mở Chrome thật (`channel: 'chrome'`).

## 4. Repo ngoài trong `tools/` (không đưa lên git — clone lại đúng commit)

| Thư mục | Repo | Commit | Dùng ở đâu |
|---|---|---|---|
| `tools/YoutubeTags` | [nuhmanpk/YoutubeTags](https://github.com/nuhmanpk/YoutubeTags) | `cc960f0` | gợi ý tìm kiếm YouTube vi/VN — `src/seo/seo_research.py`, `episode_research.py`, `topic_demand.py` |
| `tools/hybrid-youtube-growth-engine` | [catball912/hybrid-youtube-growth-engine](https://github.com/catball912/hybrid-youtube-growth-engine) | `b5a34ea` | chấm điểm SEO 0-100 — `seo_research.py` |
| `tools/YouTube-Video-SEO-Analyzer` | [kumarAnand05/YouTube-Video-SEO-Analyzer](https://github.com/kumarAnand05/YouTube-Video-SEO-Analyzer) | `b95b943` | tham khảo luật kiểm SEO (đã chuyển vào `seo_research.py`) |
| `tools/youtube-suggest-scraper` | [ChocoData-com/youtube-suggest-scraper](https://github.com/ChocoData-com/youtube-suggest-scraper) | `4546f37` | `src/seo/youtube_seo_engine.py` |
| `tools/Open-Tube-SEO` | [BizMapper/Open-Tube-SEO](https://github.com/BizMapper/Open-Tube-SEO) | `1514848` | `src/seo/youtube_seo_engine.py` (luật tiêu đề/từ khóa) |
| `tools/youtube-research-skills` | [TubeLabHQ/youtube-research-skills](https://github.com/TubeLabHQ/youtube-research-skills) | `a8a6746` | bản gốc 17 skill; bản dùng thật đã chép vào `.agents/skills/tubelab/` (có trong git) |
| `tools/srt-whiteboard-animation` | [geeklee/srt-whiteboard-animation](https://github.com/geeklee/srt-whiteboard-animation) | `696a724` | renderer cũ (`live_color_*`, `card_reveal_*`) + ảnh bàn tay đã sửa — bản vá ở `assets/vendor_patches/` |
| `tools/hyperframes` | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | `0bd1fd5` | thư viện hiệu ứng âm thanh cho `hybrid_whiteboard_renderer.py` (tùy chọn, 1,5 GB) |

Lệnh tay cho từng repo (script mục 0 đã tự làm):

```powershell
git clone <url> tools/<thư mục>; git -C tools/<thư mục> checkout <commit>
Copy-Item assets/vendor_patches/srt-whiteboard-animation/assets/* tools/srt-whiteboard-animation/assets/ -Force
```

**Pipeline sản xuất tập mới** (`longform_v2_renderer.py`, `shorts_v4_renderer.py`) **chỉ đọc `assets/`**, không phụ thuộc `tools/`.
`tools/` chỉ cần cho SEO/nghiên cứu và các renderer cũ.

## 5. Model Whisper (bước `align` căn chữ với giọng)

`pipeline.py align` dùng **faster-whisper `small`** (int8, CPU) — tự tải ~464 MB lần đầu vào `%USERPROFILE%\.cache\huggingface\hub`.
Tải trước cho khỏi chờ:

```powershell
python -c "from faster_whisper import WhisperModel; WhisperModel('small', device='cpu', compute_type='int8')"
```

## 6. VoiceStudio + OmniVoice — giọng đọc (⚠️ BƯỚC TAY, 1 lần)

Kênh chỉ dùng **VoiceStudio (OmniVoice, chạy cục bộ, miễn phí)**. ElevenLabs/edge-tts đã bỏ — **không dùng lại, không xin API key**.

1. Tải bản Windows: **https://github.com/debpalash/VoiceStudio/releases** (máy gốc: **0.5.3**, AGPL-3.0). Trang chủ https://voicestudio.sh.
2. Cài, **mở app 1 lần** cho nó tự tạo venv Python 3.11 + torch (máy gốc: torch 2.8.0+cu128, chạy CPU vẫn được).
3. Trong app → tab **Models** → tải **OmniVoice** (`k2-fsa/OmniVoice`, ~5,5 GB, revision máy gốc `c5fdb5ccb189668d56333f77ba2629f4cd7535f4`).
4. Kiểm 2 đường dẫn mặc định (pipeline đọc tự động):
   - venv: `%LOCALAPPDATA%\com.debpalash.omnivoice-studio\project\.venv\Scripts\python.exe`
   - model: `%LOCALAPPDATA%\OmniVoice\hf_cache\models--k2-fsa--OmniVoice`
   Cài chỗ khác → ghi vào `config/local.json`: `{ "voice": { "voicestudio_python": "D:\\...\\python.exe" } }`
   và đặt biến môi trường `VOICESTUDIO_DIR` trỏ tới thư mục `project`.
5. Kiểm: `python src/episode/pipeline.py check projects/<tập bất kỳ>` → phải in **`VoiceStudio OK`**.

Thông số giọng (đã khóa trong `config/channel.json > voice`, không sửa): giọng mẫu `assets/voice_refs/adam_funny_ep1.wav` (+ `.txt`),
speed 1.05, steps 32, tempo video dài 1.10, Shorts ≥ 1.10. 9 giọng cameo `assets/voice_refs/cast_*.wav`
(thiếu thì `python scripts/make_cast_refs.py`). Tốc độ: CPU ~7 phút xử lý cho 1 phút giọng → tập 9 phút ≈ 70-85 phút, chạy nền.

## 7. Cấu hình riêng máy — `config/local.json` (không lên git)

`config/channel.json` là cấu hình chung (có trong git). Thứ khác nhau giữa các máy ghi vào `config/local.json`, được đọc **đè lên**
`channel.json` bởi `src/episode/channel_config.cjs` (Node) và `pipeline.py` (Python):

```json
{ "chrome_profile": "C:\\Users\\<user>\\AppData\\Local\\vcd-chrome" }
```

Script mục 0 tự tạo file này với `%LOCALAPPDATA%\vcd-chrome`.

## 8. Đăng nhập Google trong Chrome profile (⚠️ BƯỚC TAY, 1 lần)

Ảnh Gemini và upload YouTube chạy bằng Chrome thật với profile ở mục 7:

```powershell
node src/episode/gemini_gen.cjs projects/<tập bất kỳ> probe
```

Cửa sổ Chrome mở ra → đăng nhập tài khoản Google của kênh (Gemini + YouTube Studio) → chạy lại lệnh → phải ra `signedIn: true`.
**Đóng mọi cửa sổ Chrome đang dùng profile đó** trước mỗi lần chạy `gemini_gen` / `upload_youtube` / `update_tags`.

## 9. Tự động hóa tùy chọn (chỉ bật khi chủ kênh muốn)

- **Gắn "Video có liên quan" cho Shorts** sau giờ đăng — Task Scheduler (máy gốc: 17:20 và 20:20, hết hạn 31/12/2026):

  ```powershell
  $a = New-ScheduledTaskAction -Execute (Get-Command python).Source -Argument "`"$PWD\src\episode\auto_link_shorts.py`"" -WorkingDirectory $PWD
  $t = @((New-ScheduledTaskTrigger -Daily -At 17:20), (New-ScheduledTaskTrigger -Daily -At 20:20))
  Register-ScheduledTask -TaskName VeChuyenHoangDa_AutoLinkShorts -Action $a -Trigger $t
  ```
  Chỉ chạy trên **một** máy để tránh hai máy cùng sửa Shorts.
- **Playwright MCP** cho thao tác tay trong Cursor: `.cursor/mcp.json` — đổi `--user-data-dir` sang profile mục 7. Pipeline không cần MCP.

## 10. Những gì KHÔNG có trong git và cách lấy lại

| Thứ | Vì sao không đưa lên | Lấy lại |
|---|---|---|
| `projects/*/renders/`, `assets/`, `audio/*.wav` (~70 GB) | quá nặng (GitHub giới hạn 100 MB/file) | Video đã có trên YouTube. Cần làm lại: `gemini_gen` → `tts` → `render` từ `episode.json` + `specs/` (có trong git) |
| `tools/` (1,6 GB) | repo của người khác | mục 4 |
| `node_modules/` | cài lại được | `npm ci` |
| VoiceStudio + model (~5,5 GB) | app riêng, giấy phép AGPL | mục 6 |
| `config/local.json`, Chrome profile | riêng từng máy, chứa phiên đăng nhập | mục 7, 8 |

Có trong git cho mỗi tập: `episode.json`, `specs/` (storyboard, prompt ảnh), `content/` (mega), `audio/*.json` (transcript căn thời gian),
`EPISODE_SPEC.md`, `seo_package.md`, `upload*.json` — đủ để tái tạo hoặc làm tiếp mọi tập.

Muốn chép **cả ảnh/giọng/video** của tập đang làm dở sang máy mới: chép tay thư mục `projects/<slug>/` (ổ cứng, Google Drive) —
pipeline nhận file có sẵn và bỏ qua bước đã xong.

## 11. Kiểm tra cuối — máy mới đã sẵn sàng khi

- [ ] `powershell -ExecutionPolicy Bypass -File scripts\setup_new_machine.ps1 -CheckOnly` → **không còn dòng THIEU**
- [ ] `python src/episode/pipeline.py check projects/<tập>` → `VoiceStudio OK`
- [ ] `node src/episode/gemini_gen.cjs projects/<tập> probe` → `signedIn: true`
- [ ] Đọc `AGENTS.md` → in dòng `🧠 [Memory Synced] ...`

Sau đó chủ kênh nói **"làm tập tiếp theo <con vật>"** là chạy được như máy gốc.
