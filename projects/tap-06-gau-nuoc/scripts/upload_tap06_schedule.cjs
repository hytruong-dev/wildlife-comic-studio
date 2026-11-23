/**
 * EP06 Gấu Nước — upload + schedule long-form and Shorts in the SAME slot today.
 * Slot = next 15-min mark >= now + LEAD_MIN (YouTube needs the time to be in the future).
 * Usage: node upload_tap06_schedule.cjs [long|shorts|both]
 */
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const PROJ = path.resolve(__dirname, '..');
const SNAP = path.join(PROJ, 'renders', 'snapshots');
fs.mkdirSync(SNAP, { recursive: true });
const STAGE = 'C:\\Users\\PC\\.playwright-mcp\\';
const PROFILE = 'C:\\Users\\PC\\AppData\\Local\\ms-playwright-mcp\\mcp-chrome-aad48e1';
const CHANNEL = 'UCMX7XBHXoiq_kWIUo73n1Vw';
const MODE = process.argv[2] || 'both';
const FIXED = process.argv[3]; // optional "HH:MM"

const LONG = {
  file: STAGE + 'tap06_gau_nuoc_longform.mp4',
  thumb: STAGE + 'tap06_gau_nuoc_thumbnail.jpg',
  title: 'Sống Sót 5 Lần Tận Thế... Nhưng Chết Vì Một Con Ốc Sên! | Gấu Nước | Tập 6',
  desc: `Gấu Nước (Tardigrade) nhỏ hơn hạt cát, chịu được âm 272°C, nước sôi 150°C, phóng xạ gấp 1.000 lần liều chết người và từng bị thả trần trụi ngoài vũ trụ 10 ngày mà vẫn sống. Vậy mà một con ốc sên lại có thể giết chết nó! Và ngay lúc này, hàng ngàn con Gấu Nước đang nằm ngủ trên Mặt Trăng...

Tập 6 series Vẽ Chuyện Hoang Dã — kể chuyện động vật bằng tranh vẽ tay bảng trắng (whiteboard animation).

⏱️ MỤC LỤC:
00:00 Intro
00:10 Kẻ sống sót cuối cùng của Trái Đất
01:39 Bảng chỉ số RPG — lỗi game tiến hóa
03:11 Tuyệt kỹ thủy tinh hóa (Cryptobiosis)
04:53 Gót chân A-sin của kẻ bất tử
06:32 Gấu Nước đang nằm trên Mặt Trăng
08:24 Bài học sinh tồn từ Gấu Nước
09:26 Kết thúc

🔥 Trong video:
• Vì sao Gấu Nước sống sót qua cả 5 cuộc đại tuyệt chủng
• Protein TDP biến cơ thể thành "thủy tinh", Dsup che chắn ADN khỏi phóng xạ
• 3 điểm yếu bi hài: chất nhầy ốc sên, giun tròn và… nước hơi ấm 37,6°C
• Vụ rơi tàu Beresheet năm 2019 rải Gấu Nước lên Mặt Trăng

🎬 Xem tiếp các tập trước:
👉 Tập 5 — Chim Bồ Nông: https://youtu.be/KXJQReDxDcA
👉 Tập 4 — Thú Mỏ Vịt: https://youtu.be/ogvEUfQOWGA
👉 Tập 2 — Rái Cá Biển: https://youtu.be/DOPcbU7gvjs
👉 Tập 1 — Lửng Mật: https://youtu.be/WRAp223qZ60

💬 Nếu có siêu năng lực ngủ đông như Gấu Nước, bạn muốn thức dậy vào năm nào? Bình luận cho mình biết nhé!
🔔 Đăng ký kênh Vẽ Chuyện Hoang Dã để xem tập 7: Tôm Tít — cú đấm nhanh như đạn bắn!

#GauNuoc #Tardigrade #TheGioiDongVat #VeChuyenHoangDa #KhoaHoc`,
  tags: 'gấu nước, tardigrade, gau nuoc, water bear, sinh vật bất tử, sinh vật bất tử nhất trái đất, gấu nước mặt trăng, gấu nước ốc sên, cryptobiosis, động vật kỳ lạ, thế giới động vật, khám phá động vật, vẽ chuyện hoang dã, whiteboard animation, khoa học thú vị, beresheet, đại tuyệt chủng',
};
const SHORTS = {
  file: STAGE + 'tap06_gau_nuoc_shorts.mp4',
  title: 'Bất Tử Ngoài Vũ Trụ Nhưng Chết Vì Ốc Sên?! 🐌 #shorts #gaunuoc',
  desc: `Sống qua 5 cuộc đại tuyệt chủng, chịu âm 272°C và nước sôi 150°C… nhưng Gấu Nước lại thua một con ốc sên! 🐌
👉 Xem bản đầy đủ: hàng ngàn Gấu Nước đang nằm trên Mặt Trăng — video Tập 6 trên kênh Vẽ Chuyện Hoang Dã.

#shorts #GauNuoc #Tardigrade #TheGioiDongVat #VeChuyenHoangDa #KhoaHoc`,
  tags: 'gấu nước, tardigrade, sinh vật bất tử, shorts, thế giới động vật, vẽ chuyện hoang dã, động vật kỳ lạ',
};

function slot() {
  if (FIXED) return FIXED;
  const t = new Date(Date.now() + 20 * 60000);
  const m = Math.ceil(t.getMinutes() / 15) * 15;
  t.setMinutes(m, 0, 0);
  return `${String(t.getHours()).padStart(2, '0')}:${String(t.getMinutes()).padStart(2, '0')}`;
}

async function shot(page, n) { await page.screenshot({ path: path.join(SNAP, `ep06_${n}.png`) }).catch(() => {}); }

async function upload(page, v, tag, hhmm) {
  console.log(`\n=== ${tag}: ${v.title}`);
  await page.goto(`https://studio.youtube.com/channel/${CHANNEL}/videos/upload?d=ud`, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(5000);
  const dlg = page.locator('ytcp-uploads-dialog').first();
  await dlg.locator('input[type="file"]').first().setInputFiles(v.file);
  const title = dlg.locator('#title-textarea #textbox').first();
  await title.waitFor({ timeout: 90000 });
  await page.waitForTimeout(3000);
  await title.click(); await page.keyboard.press('Control+A'); await page.keyboard.press('Backspace');
  await title.pressSequentially(v.title, { delay: 5 });
  const desc = dlg.locator('#description-textarea #textbox').first();
  await desc.click(); await page.keyboard.press('Control+A'); await page.keyboard.press('Backspace');
  await desc.fill(v.desc);
  if (v.thumb) {
    const ti = dlg.locator('input#file-loader, input[type="file"][accept*="image"]').first();
    if (await ti.count()) { await ti.setInputFiles(v.thumb); await page.waitForTimeout(3000); console.log('  thumbnail set'); }
  }
  // playlist (best-effort)
  try {
    await dlg.locator('ytcp-video-metadata-playlists #trigger, ytcp-video-metadata-playlists ytcp-dropdown-trigger').first().click({ timeout: 5000 });
    await page.waitForTimeout(1000);
    const cb = page.locator('ytcp-playlist-dialog ytcp-checkbox-lit, ytcp-playlist-dialog tp-yt-paper-checkbox').filter({ hasText: 'Thế Giới Động Vật' }).first();
    if (await cb.isVisible()) await cb.click();
    await page.locator('ytcp-playlist-dialog ytcp-button:has-text("Xong"), ytcp-playlist-dialog #done-button').first().click({ timeout: 5000 });
    console.log('  playlist set');
  } catch (e) { console.log('  playlist skipped:', e.message.split('\n')[0]); await page.keyboard.press('Escape').catch(() => {}); }
  await dlg.locator('[name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]').first().click({ force: true });
  try { await dlg.locator('#toggle-button').first().click({ timeout: 4000 }); await page.waitForTimeout(1000); } catch {}
  try { await dlg.locator('[name="VIDEO_HAS_ALTERED_CONTENT_NO"]').first().click({ force: true, timeout: 4000 }); } catch {}
  try {
    const tags = dlg.locator('ytcp-form-input-container#tags-container input#text-input, #tags-container input').first();
    await tags.scrollIntoViewIfNeeded(); await tags.click(); await tags.fill(v.tags + ','); await page.waitForTimeout(500);
    console.log('  tags set');
  } catch (e) { console.log('  tags skipped:', e.message.split('\n')[0]); }
  try { // category Education-ish: keep channel default; language Vietnamese is channel default
  } catch {}
  await shot(page, `${tag}_1_details`);

  const next = dlg.locator('#next-button');
  for (let i = 0; i < 6; i++) {
    const step = await dlg.getAttribute('workflow-step').catch(() => null);
    if (step === 'REVIEW' || step === 'PUBLISH') break;
    await next.click({ force: true }); await page.waitForTimeout(2500);
  }
  await shot(page, `${tag}_2_visibility`);

  // schedule
  await dlg.locator('#second-container-expand-button').first().click({ force: true });
  await page.waitForTimeout(1500);
  const timeIn = dlg.locator('#time-of-day-container input, ytcp-datetime-picker #time-of-day-trigger input, ytcp-datetime-picker input').last();
  await timeIn.click(); await page.keyboard.press('Control+A'); await timeIn.pressSequentially(hhmm, { delay: 40 });
  await page.keyboard.press('Enter'); await page.waitForTimeout(1500);
  const dateTxt = await dlg.locator('#datepicker-trigger').first().innerText().catch(() => '?');
  const timeVal = await timeIn.inputValue().catch(() => '?');
  console.log(`  schedule = ${dateTxt.trim()} ${timeVal}`);
  await shot(page, `${tag}_3_schedule`);
  if (timeVal.replace(/\s/g, '') !== hhmm) throw new Error(`time not applied (${timeVal} != ${hhmm})`);

  const link = await dlg.locator('a[href*="youtu"]').first().getAttribute('href').catch(() => null);
  console.log('  url =', link);
  // wait for upload to finish before closing (schedule button works while uploading, but keep tab alive)
  await dlg.locator('#done-button').first().click({ force: true });
  await page.waitForTimeout(6000);
  await shot(page, `${tag}_4_done`);
  for (let i = 0; i < 120; i++) { // up to 20 min for file transfer
    const txt = await page.locator('ytcp-uploads-still-processing-dialog, ytcp-video-upload-progress, ytcp-multi-progress-monitor').allInnerTexts().catch(() => []);
    const s = txt.join(' ');
    if (!/Đang tải lên|Uploading|\d+%/.test(s) || /xong|complete|Đang xử lý|Processing|Đã tải lên/i.test(s)) { if (i > 0) break; }
    if (i % 6 === 0) console.log('  ...', s.replace(/\s+/g, ' ').slice(0, 100));
    await page.waitForTimeout(10000);
  }
  try { await page.locator('ytcp-uploads-still-processing-dialog #close-button, ytcp-dialog #close-button').first().click({ timeout: 3000 }); } catch {}
  return link;
}

(async () => {
  const hhmm = slot();
  console.log('SLOT today:', hhmm);
  const ctx = await chromium.launchPersistentContext(PROFILE, {
    headless: false, channel: 'chrome', viewport: { width: 1366, height: 860 },
    args: ['--disable-blink-features=AutomationControlled'],
  });
  const page = ctx.pages()[0] || await ctx.newPage();
  const res = {};
  try {
    if (MODE !== 'shorts') res.long = await upload(page, LONG, 'long', hhmm);
    if (MODE !== 'long') res.shorts = await upload(page, SHORTS, 'shorts', hhmm);
    console.log('\nRESULT', JSON.stringify({ slot: hhmm, ...res }));
    fs.writeFileSync(path.join(PROJ, 'upload_result.json'), JSON.stringify({ slot: hhmm, date: new Date().toISOString(), ...res }, null, 2));
  } catch (e) {
    console.error('UPLOAD ERROR:', e.message);
    await shot(page, 'error');
    process.exitCode = 1;
  } finally {
    await page.waitForTimeout(3000);
    await ctx.close();
  }
})();
