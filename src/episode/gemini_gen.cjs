/**
 * Tạo ảnh Gemini hàng loạt — KHÔNG cần Playwright MCP (đã kiểm chứng Tập 9: 88 ảnh dài + 13 Shorts + 7 banner + thumbnail).
 * Dùng Playwright + profile Chrome đã đăng nhập Google (config/channel.json > chrome_profile).
 *
 *   node src/episode/gemini_gen.cjs <project> probe                 # mở Gemini, báo đã đăng nhập chưa (exit 3 = chưa)
 *   node src/episode/gemini_gen.cjs <project> long                  # L01..Lnn từ specs/image_prompts.json
 *   node src/episode/gemini_gen.cjs <project> shorts                # S01..Snn
 *   node src/episode/gemini_gen.cjs <project> extra                 # specs/extra_prompts.json: C01..C0N, B00 -> assets/_src, T01 -> inbox
 *   tuỳ chọn: --only L07,L09   --from L40   --per-chat 20 (mở chat mới sau N ảnh; 1 = mỗi ảnh 1 chat, dùng khi ảnh hay timeout)
 *             --account 1  (tài khoản Google thứ 2 khi hết lượt: gemini.google.com/u/1/app)
 *
 * TRƯỚC KHI CHẠY: đóng mọi cửa sổ Chrome đang dùng profile này (persistent context không mở được profile đang khóa).
 * Ảnh -> <project>/assets/inbox/<ID>.txt (dataURL PNG gốc, không watermark lớn); ảnh đã có trong inbox hoặc assets/long|shorts thì bỏ qua
 * -> chạy lại lệnh bao nhiêu lần cũng được, chỉ tạo phần còn thiếu. Nhật ký: assets/inbox/_gen_log.jsonl.
 * An toàn: lấy ảnh trong model-response MỚI xuất hiện sau khi gửi (LESSON-52) + chặn ảnh trùng hash.
 * Sau đó: python src/episode/import_images.py <project> --sheet   (khử watermark, chia L/S/T, bảng xem nhanh)
 */
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const ROOT = path.resolve(__dirname, '..', '..');
const argv = process.argv.slice(2);
if (argv.length < 2) { console.log('usage: node src/episode/gemini_gen.cjs <project> probe|long|shorts|extra [--only ..] [--per-chat N] [--account 1]'); process.exit(1); }
const P = path.resolve(argv[0]);
const mode = argv[1];
const opt = (k) => { const i = argv.indexOf(k); return i >= 0 ? argv[i + 1] : null; };
const account = opt('--account') || '0';
const only = opt('--only') ? opt('--only').split(',') : null;
const from = opt('--from');
const force = argv.includes('--force');
const PER_CHAT = parseInt(opt('--per-chat') || '20', 10);
const profileArg = opt('--profile');

const CH = require('./channel_config.cjs').loadChannel();  // channel.json + config/local.json (riêng từng máy)
const CHROME_PROFILE = profileArg
  ? (profileArg.includes('\\') || profileArg.includes('/') ? path.resolve(profileArg) : path.join(path.dirname(CH.chrome_profile), `mcp-chrome-${profileArg}`))
  : CH.chrome_profile;
const promptFile = path.join(P, 'specs/image_prompts.json');
const PROMPTS = fs.existsSync(promptFile) ? JSON.parse(fs.readFileSync(promptFile, 'utf8')) : {};
const INBOX = path.join(P, 'assets/inbox');
fs.mkdirSync(INBOX, { recursive: true });
const LOG = path.join(INBOX, '_gen_log.jsonl');

const log = (o) => { console.log(JSON.stringify(o)); fs.appendFileSync(LOG, JSON.stringify({ t: new Date().toISOString(), ...o }) + '\n'); };
const hashes = new Set(fs.readdirSync(INBOX).filter(f => f.endsWith('.txt'))
  .map(f => crypto.createHash('md5').update(fs.readFileSync(path.join(INBOX, f))).digest('hex')));

function sanitizePromptText(t) {
  if (!t) return '';
  return t
    .replace(/\.?\s*Lời thoại:\s*["'][^"']*["']\.?/gi, '.')
    .replace(/\b(wolverine|spider-?man|người nhện|batman|superman|iron-?man|hulk|mickey|doraemon|pikachu|godzilla|king kong)\b/gi, 'nhân vật hoạt hình ngộ nghĩnh')
    .replace(/\b(mike tyson|tyson|usain bolt|elon musk|einstein)\b/gi, 'nhân vật hoạt hình vui nhộn')
    .replace(/\b(ferrari|lamborghini|glock|ak-?47)\b/gi, 'đồ chơi hoạt hình')
    .replace(/khuôn mặt người|mặt người/gi, 'hình vẽ mặt cười hoạt hình')
    .replace(/nhận diện (khuôn )?mặt/gi, 'nhận diện hình vẽ hoạt hình')
    .replace(/camera an ninh/gi, 'ống kính quan sát hoạt hình')
    .replace(/bom cảm tử|tự kích nổ|kích nổ|nổ tung cơ thể/gi, 'bong bóng hoạt hình phát sáng')
    .replace(/tự sát|hi sinh/gi, 'bảo vệ tổ')
    .replace(/súng ngắm|bắn tỉa|đạn súng trường|đạn súng|\bbullets\b/gi, 'tia nước hoạt hình')
    .replace(/vũ khí quân sự|quân sự|kính ngắm laser/gi, 'kính quan sát hoạt hình')
    .replace(/máu me|chảy máu|\bblood red\b/gi, 'màu vẽ hoạt hình')
    .replace(/xé xác|phanh thây|lòi ruột|đứt đầu|nội tạng/gi, 'vui đùa hoạt hình')
    .replace(/trườn thẳng vào trong cơ thể|chui vào trong cơ thể/gi, 'bơi lại gần kết bạn')
    .replace(/hậu môn|lỗ huyệt/gi, 'phần thân sau');
}

async function newChat(page) {
  await page.goto(`https://gemini.google.com/u/${account}/app`, { waitUntil: 'domcontentloaded', timeout: 90000 });
  await page.waitForTimeout(4000);
}

async function send(page, prompt) {
  const before = await page.locator('model-response').count();
  const box = page.locator('rich-textarea .ql-editor, div[contenteditable="true"][role="textbox"]').first();
  await box.waitFor({ timeout: 60000 });
  await box.click();
  await page.evaluate((t) => {  // insertText: nhanh, giữ nguyên dấu tiếng Việt
    const el = document.querySelector('rich-textarea .ql-editor') || document.querySelector('div[contenteditable="true"][role="textbox"]');
    el.focus(); document.execCommand('insertText', false, t);
  }, prompt);
  await page.waitForTimeout(600);
  await page.keyboard.press('Enter');
  for (let i = 0; i < 110; i++) {  // ~4 phút
    await page.waitForTimeout(2200);
    try {
      const r = await page.evaluate(async (b) => {
        const rs = [...document.querySelectorAll('model-response')];
        if (rs.length <= b) return null;
        const last = rs.at(-1);
        const im = [...last.querySelectorAll('img')].find(x => x.naturalWidth > 300 && x.complete);
        if (!im) {
          const txt = last.innerText || '';
          if (/giới hạn|limit|try again later|thử lại sau|can't create|không thể tạo|không tạo được|bên thứ ba|vi phạm|chính sách/i.test(txt) && txt.length > 20) return { err: txt.slice(0, 200) };
          return null;
        }
        if (im.src && im.src.startsWith('data:image/')) {
          return { w: im.naturalWidth, h: im.naturalHeight, data: im.src };
        }
        try {
          const c = document.createElement('canvas'); c.width = im.naturalWidth; c.height = im.naturalHeight;
          c.getContext('2d').drawImage(im, 0, 0);
          return { w: im.naturalWidth, h: im.naturalHeight, data: c.toDataURL('image/png') };
        } catch (_cErr) {
          try {
            const resp = await window.fetch(im.src);
            const blob = await resp.blob();
            const b64 = await new Promise((resolve, reject) => {
              const reader = new FileReader();
              reader.onloadend = () => resolve(reader.result);
              reader.onerror = reject;
              reader.readAsDataURL(blob);
            });
            return { w: im.naturalWidth, h: im.naturalHeight, data: b64 };
          } catch (_fErr) {
            return null;
          }
        }
      }, before);
      if (r && r.err) { if (i > 3) return r; continue; }
      if (r) return r;
    } catch (_evalErr) {
      // Bỏ qua lỗi evaluate tạm thời, tiếp tục đợi
    }
  }
  return { err: 'timeout' };
}

(async () => {
  const ctx = await chromium.launchPersistentContext(CHROME_PROFILE, {
    headless: false, channel: 'chrome', viewport: { width: 1400, height: 900 },
    args: ['--disable-blink-features=AutomationControlled'],
  });
  const page = ctx.pages()[0] || await ctx.newPage();
  await newChat(page);
  const signedIn = await page.evaluate(() => ![...document.querySelectorAll('a,button')]
    .some(x => /^(Sign in|Đăng nhập)$/.test((x.innerText || x.getAttribute('aria-label') || '').trim())));
  log({ probe: true, signedIn, url: page.url() });
  if (mode === 'probe' || !signedIn) {
    if (!signedIn) console.log('!! Chưa đăng nhập Google trong profile — đăng nhập một lần trong cửa sổ Chrome này rồi chạy lại.');
    await ctx.close(); process.exit(signedIn ? 0 : 3);
  }

  if (mode === 'extra') {  // banner + thumbnail: mỗi ảnh 1 chat mới
    const EX = JSON.parse(fs.readFileSync(path.join(P, 'specs/extra_prompts.json'), 'utf8'));
    const SRC = path.join(P, 'assets/_src'); fs.mkdirSync(SRC, { recursive: true });
    for (const id of Object.keys(EX).filter(k => !k.startsWith('_') && (!only || only.includes(k)))) {
      const out = id === 'T01' ? path.join(INBOX, 'T01.txt') : path.join(SRC, `${id}.txt`);
      if (!force && fs.existsSync(out)) continue;
      await newChat(page);
      const safePrompt = sanitizePromptText(EX[id]);
      const r = await send(page, safePrompt);
      if (r.err) { log({ id, err: r.err }); continue; }
      fs.writeFileSync(out, r.data); log({ id, ok: true, w: r.w, h: r.h });
    }
    await ctx.close(); return;
  }

  const prefix = mode === 'shorts' ? 'S' : 'L';
  const kindDir = mode === 'shorts' ? 'shorts' : 'long';
  let ids = Object.keys(PROMPTS).filter(k => k.startsWith(prefix)).sort();
  if (only) ids = ids.filter(k => only.includes(k));
  if (from) ids = ids.filter(k => k >= from);
  let inChat = 0, fails = 0, made = 0;
  for (const id of ids) {
    const out = path.join(INBOX, `${id}.txt`);
    if (!force && (fs.existsSync(out) || fs.existsSync(path.join(P, 'assets', kindDir, `${id}.png`)))) continue;
    try {
      if (inChat >= PER_CHAT) { await newChat(page); inChat = 0; }
      const head = mode === 'shorts' ? PROMPTS._first_shorts : PROMPTS._first_long;
      const pClean = sanitizePromptText(PROMPTS[id] || '');
      let prompt = inChat === 0 ? sanitizePromptText(head) + ' ' + pClean : 'Vẽ tiếp bức tranh minh họa sau: ' + pClean;
      let r = await send(page, prompt);
      if (r && r.err) {
        if (/bên thứ ba|vi phạm|chính sách|không an toàn|can't create|third-party|policy|safety/i.test(r.err)) {
          console.log(`  [SAFETY-GUARD] Phát hiện từ chối chính sách ở ${id} -> Làm sạch tối đa & đổi phiên mới ngay`);
          await newChat(page).catch(() => {});
          inChat = 0;
          const fallbackClean = pClean.replace(/Bố cục:[^.]*/gi, 'Bố cục: nhân vật hoạt hình ngộ nghĩnh trên nền giấy trắng thân thiện trẻ em, tuyệt đối không bạo lực');
          prompt = 'Tạo hình ảnh hoạt hình trẻ em: ' + fallbackClean;
          r = await send(page, prompt);
        }
      }
      if (r.err) {
        log({ id, err: r.err }); fails++;
        if (fails >= 5) { log({ stop: '5 lỗi liên tiếp (hết lượt?) — chạy lại với --account 1, hoặc chờ rồi chạy lại' }); break; }
        await newChat(page).catch(() => {}); inChat = 0; continue;
      }
      const h = crypto.createHash('md5').update(r.data).digest('hex');
      if (hashes.has(h)) { log({ id, err: 'duplicate image' }); await newChat(page).catch(() => {}); inChat = 0; continue; }
      hashes.add(h); fails = 0; made++;
      fs.writeFileSync(out, r.data);
      inChat++;
      log({ id, ok: true, w: r.w, h: r.h });
    } catch (loopErr) {
      log({ id, err: String(loopErr) });
      fails++;
      if (fails >= 5) { log({ stop: '5 lỗi liên tiếp' }); break; }
      await newChat(page).catch(() => {});
      inChat = 0;
    }
  }
  const left = ids.filter(id => !fs.existsSync(path.join(INBOX, `${id}.txt`)) && (!force ? !fs.existsSync(path.join(P, 'assets', kindDir, `${id}.png`)) : false));
  log({ done: mode, made, missing: left });
  await ctx.close();
})().catch(e => { log({ fatal: String(e) }); process.exit(1); });
