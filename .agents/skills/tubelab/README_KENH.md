# Bộ skill nghiên cứu YouTube (TubeLab) — cách dùng cho kênh "Vẽ Chuyện Hoang Dã"

Nguồn: https://github.com/TubeLabHQ/youtube-research-skills (MIT), bản gốc ở `tools/youtube-research-skills/`.
17 skill nằm cạnh file này; mỗi skill là một quy trình nghiên cứu, agent tự đọc khi yêu cầu khớp mô tả.

## Hai cách chạy

| Chế độ | Cần gì | Dùng được |
|---|---|---|
| **A. Miễn phí (mặc định)** | yt-dlp + YoutubeTags (đã cài) | Đọc kênh, video, tag, gợi ý tìm kiếm, bình luận. Outlier ratio tự tính bằng `src/seo/channel_outliers.py` |
| **B. TubeLab MCP** | Tài khoản TubeLab. Cursor cần API key = gói **Pro** (~400 credit/tháng) | Thêm: tìm outlier toàn YouTube, kênh đang lên theo bộ lọc, công thức tiêu đề đang thịnh hành, kênh tương tự, ước tính RPM/khán giả |

Chưa có tài khoản → luôn dùng chế độ A và nói rõ phần nào bị thiếu (xem bảng "What only TubeLab returns" trong `tubelab-mcp/SKILL.md`).
**Không tự đăng ký, không tự nhập API key, không tiêu credit khi chủ kênh chưa đồng ý.**

## Skill nào đáng dùng cho kênh này

| Mục đích | Skill | Chế độ A làm được? | Khi nào chạy |
|---|---|---|---|
| Kênh mình đang thắng/thua ở đâu | `roast-channel`, `reverse-engineer-channel` | ✅ (dùng `channel_outliers.py` cho ratio) | Mỗi 10 tập, trước khi chốt roadmap |
| Học từ đối thủ cùng chủ đề | `reverse-engineer-channel` (1 kênh), `reverse-engineer-niche` | ✅ 1 kênh · ⚠️ niche (thiếu tìm kênh tương tự) | Khi đổi hướng format |
| Chọn con vật cho tập sau | `video-ideation`, `trend-report` | ⚠️ (dùng autocomplete + video top theo từ khoá thay cho outlier toàn index) | Trước "làm tập tiếp theo" |
| Tiêu đề | `title-formulas` | ⚠️ (công thức lấy từ video top cùng chủ đề; không có index trending) | Trước `pipeline.py seo` |
| Thumbnail | `thumbnail-concepts` | ✅ (xem thumbnail video top bằng `https://i.ytimg.com/vi/<id>/mqdefault.jpg`) | Trước khi sinh T01 |
| Mở đầu video giữ người xem | `script-breakdown` | ✅ (transcript bằng `yt-dlp --write-auto-subs`) | Khi viết hook scene01 |
| Người xem muốn gì | `comment-mining` | ✅ | Chọn con vật / câu hỏi ghim |
| Rủi ro mất kiếm tiền (nội dung AI) | `audit-channel-risk` | ⚠️ (thiếu dữ liệu kênh bị khoá) | Trước khi bật kiếm tiền |
| Không phù hợp lúc này | `sponsorship-prospecting`, `revenue-maxxing`, `niche-finder`, `niche-bending`, `niche-validator`, `niche-watchlist` | — | Khi kênh đủ điều kiện kiếm tiền / muốn mở kênh mới |

## Luật riêng của kênh khi dùng các skill này

- Mọi đề xuất tiêu đề/thumbnail vẫn phải tuân `.agent_memory/director_taste.md` (TASTE-68 hashtag, video dài **luôn có đuôi `| Tập N`** TASTE-72, Shorts kể trọn vẹn TASTE-66).

## Đã gắn vào quy trình mỗi tập (`episode-production`, từ 23/11/2026)

Một công cụ `src/seo/episode_research.py` chạy 3 skill ở chế độ A, kết quả vào `projects/<slug>/specs/`:

| Bước tập | Lệnh | Skill | Dùng để |
|---|---|---|---|
| 0 (chọn góc) | `... ideas [--en "English name"]` | `comment-mining` | hook, cú bẻ lái, câu hỏi ghim |
| 3b (trước T01) | `... thumbs` | `thumbnail-concepts` | mở xem thumbnail top → `art.thumb_*` |
| 8 (trước seo) | `... titles` | `title-formulas` | `seo.title` + `seo.title_alternatives` |

Lọc: chỉ giữ video có đúng tên loài (nguyên từ, đúng dấu — "hải ly" ≠ "Lý Hải") và bỏ phim/nhạc/game/truyện.
Loài hiếm (ít video tiếng Việt) → luôn thêm `--en`.
- Báo cáo ghi vào `docs/research/<skill>_<chủ đề>_<ngày>.md`. Mọi con số phải kèm link video/kênh lấy từ dữ liệu thật — không bịa.
- Kênh mình còn nhỏ (trung vị video dài vài chục view): ratio so với trung vị của chính kênh vẫn có ý nghĩa, nhưng
  video < 2 ngày tuổi chưa đủ view — `channel_outliers.py` mặc định bỏ qua.
- Chỉ đọc dữ liệu công khai. Không sửa gì trên YouTube trong các skill này.

## Lệnh nhanh

```bash
python src/seo/channel_outliers.py                         # outlier kênh mình
python src/seo/channel_outliers.py @handle UCxxxx URL       # outlier kênh đối thủ
python src/seo/seo_research.py projects/<slug>              # tag + gợi ý tìm kiếm + video top của 1 tập
python src/seo/episode_research.py projects/<slug> all --en "English name"   # comment-mining + titles + thumbs của 1 tập
yt-dlp --write-auto-subs --sub-langs vi --skip-download -o "%(id)s" <url>   # transcript cho script-breakdown
```

## Bật chế độ B (khi chủ kênh mua gói Pro)

Thêm vào `.cursor/mcp.json`, khoá đặt trong biến môi trường, KHÔNG ghi thẳng vào file:

```json
"tubelab": { "url": "https://public-api.tubelab.net/mcp", "headers": { "Authorization": "Bearer ${env:TUBELAB_API_KEY}" } }
```
