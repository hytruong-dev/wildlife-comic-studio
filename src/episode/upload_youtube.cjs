/**
 * Upload + schedule an episode (long-form + Shorts) to YouTube Studio.
 * ONLY run when the channel owner explicitly orders publishing.
 *
 *   node src/episode/upload_youtube.cjs projects/<slug> --date 2026-11-08 --time 18:00 [--only long|shorts] [--shorts-time 18:00]
 *   node src/episode/upload_youtube.cjs projects/<slug> --date ... --time ... --fix-only --long-id ID --shorts-id ID   (re-schedule only)
 *   Lịch chuẩn TASTE-68: --date D --time 17:00 --shorts-date D+1 --shorts-time 11:30 (1 tập/ngày)
 *
 * Reads projects/<slug>/upload.json (made by `pipeline.py seo`) and config/channel.json.
 * Uses a persistent Chrome profile already logged into the channel (close other Chrome
 * windows using that profile first). Studio always defaults the date to TOMORROW, so the
 * date is typed explicitly and verified (LESSON-63). Result -> projects/<slug>/upload_result.json
 */
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '../..');
const CH = require('./channel_config.cjs').loadChannel();  // channel.json + config/local.json (riêng từng máy)
const P = path.resolve(process.argv[2] || '');
const arg = (k, d) => { const i = process.argv.indexOf(k); return i > 0 ? process.argv[i + 1] : d; };
const DATE = arg('--date'); const TIME = arg('--time'); const ONLY = arg('--only'); const STIME = arg('--shorts-time', TIME);
if (!DATE || !TIME || !fs.existsSync(path.join(P, 'upload.json'))) {
  console.log('usage: node src/episode/upload_youtube.cjs projects/<slug> --date YYYY-MM-DD --time HH:MM'); process.exit(1);
}
const UP = JSON.parse(fs.readFileSync(path.join(P, 'upload.json'), 'utf8'));
const SNAP = path.join(P, 'renders', 'snapshots'); fs.mkdirSync(SNAP, { recursive: true });
const STAGE = path.join(require('os').homedir(), '.playwright-mcp'); fs.mkdirSync(STAGE, { recursive: true });
// TASTE-68: long 17:00 day D, its Shorts 11:30 day D+1 (--shorts-date) so "Video có liên quan" can point to a public long video.
const SDATE = arg('--shorts-date', DATE);
const studioDate = (iso) => { const [y, m, d] = iso.split('-').map(Number); return { d, s: CH.studio_locale_date.replace('{d}', d).replace('{m}', m).replace('{y}', y) }; };
let { d: D, s: STUDIO_DATE } = studioDate(DATE);
const useDate = (iso) => { ({ d: D, s: STUDIO_DATE } = studioDate(iso)); };

const shot = (page, n) => page.screenshot({ path: path.join(SNAP, `upload_${n}.png`) }).catch(() => {});
const stage = (f) => { const dst = path.join(STAGE, path.basename(f)); fs.copyFileSync(f, dst); return dst; };

// Step A (upload dialog): choose "Schedule" + exact date + time.
async function setScheduleInDialog(page, dlg, hhmm, tag) {
  await dlg.locator('#second-container-expand-button').first().click({ force: true });
  await page.waitForTimeout(1500);
  try {
    await dlg.locator('#datepicker-trigger').first().click();
    await page.waitForTimeout(1000);
    const dateIn = page.locator('ytcp-date-picker input, tp-yt-paper-dialog ytcp-date-picker tp-yt-paper-input input').last();
    await dateIn.click(); await page.keyboard.press('Control+A'); await dateIn.pressSequentially(STUDIO_DATE, { delay: 30 });
    await page.keyboard.press('Enter'); await page.waitForTimeout(1200);
  } catch (e) { console.log('  dialog date note:', e.message.split('\n')[0]); }
  const timeIn = dlg.locator('#time-of-day-container input, ytcp-datetime-picker #time-of-day-trigger input, ytcp-datetime-picker input').last();
  await timeIn.click(); await page.keyboard.press('Control+A'); await timeIn.pressSequentially(hhmm, { delay: 40 });
  await page.keyboard.press('Enter'); await page.waitForTimeout(1500);
  const dt = await dlg.locator('#datepicker-trigger').first().innerText().catch(() => '?');
  console.log(`  dialog schedule = ${dt.trim()} ${await timeIn.inputValue().catch(() => '?')}`);
  await shot(page, `${tag}_schedule_dialog`);
}

// Step B (proven in EP06 reschedule_today.cjs): fix exact date+time on /video/<id>/edit and verify.
async function fixSchedule(page, id, hhmm, tag) {
  await page.goto(`https://studio.youtube.com/video/${id}/edit`, { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(7000);
  await page.locator('ytcp-video-metadata-visibility #select-button, ytcp-video-metadata-visibility').first().click();
  await page.waitForTimeout(2000);
  const visDp = page.locator('#datepicker-trigger').filter({ visible: true });
  if (!(await visDp.count())) {
    try { await page.locator('#second-container-expand-button').filter({ visible: true }).last().click({ timeout: 4000 }); } catch {}
    await page.waitForTimeout(1500);
  }
  await visDp.last().click();
  await page.waitForTimeout(1000);
  const dateIn = page.locator('ytcp-date-picker input, tp-yt-paper-dialog ytcp-date-picker tp-yt-paper-input input').filter({ visible: true }).last();
  await dateIn.click(); await page.keyboard.press('Control+A'); await dateIn.pressSequentially(STUDIO_DATE, { delay: 30 });
  await page.keyboard.press('Enter'); await page.waitForTimeout(1200);
  const timeIn = page.locator('#time-of-day-container input, ytcp-datetime-picker #time-of-day-trigger input').filter({ visible: true }).last();
  await timeIn.click(); await page.keyboard.press('Control+A'); await timeIn.pressSequentially(hhmm, { delay: 40 });
  await page.keyboard.press('Enter'); await page.waitForTimeout(1200);
  const dt = (await visDp.last().innerText()).trim();
  const tv = (await timeIn.inputValue()).trim();
  console.log(`  ${tag} ${id}: ${dt} ${tv}`);
  await shot(page, `${tag}_schedule_fixed`);
  if (!dt.startsWith(`${D} `) || tv !== hhmm) throw new Error(`${tag}: schedule not applied (${dt} ${tv}); expected ${STUDIO_DATE} ${hhmm}`);
  await page.locator('#save-button, ytcp-button:has-text("Xong")').filter({ visible: true }).first().click();
  await page.waitForTimeout(2000);
  const save = page.locator('ytcp-button#save, #save').filter({ visible: true }).first();
  // Save stays disabled when the schedule was already correct (no change) -> skip instead of timing out.
  if (await save.count() && (await save.getAttribute('aria-disabled')) !== 'true') {
    await save.click({ timeout: 15000 }).catch(async () => { await page.keyboard.press('Escape'); await save.click({ timeout: 10000 }); });
    await page.waitForTimeout(4000);
  } else { console.log(`  ${tag}: already scheduled, nothing to save`); await page.keyboard.press('Escape').catch(() => {}); }
  await shot(page, `${tag}_schedule_saved`);
  return `${dt} ${tv}`;
}

async function dismissPolicyWarning(page, tag) {
  const warnDlg = page.locator('tp-yt-paper-dialog, ytcp-dialog').filter({ hasText: 'Video này vi phạm Nguyên tắc cộng đồng' }).first();
  if (await warnDlg.isVisible().catch(() => false)) {
    console.log(`  [!] Detected Community Guidelines warning popup during ${tag} — clicking "Hủy" (Dismiss) to proceed`);
    await shot(page, `${tag}_warning_popup`);
    await warnDlg.locator('ytcp-button:has-text("Hủy"), button:has-text("Hủy"), #dismiss-button, #close-button').last().click({ force: true }).catch(() => {});
    await page.waitForTimeout(2000);
    return true;
  }
  return false;
}

async function checkDailyUploadLimit(page, dlg, tag) {
  const txt = await page.evaluate(() => document.body.innerText || '').catch(() => '');
  if (/Đã đạt giới hạn tải video lên hằng ngày|Daily upload limit reached/i.test(txt)) {
    await shot(page, `${tag}_daily_limit`);
    throw new Error(`DAILY_UPLOAD_LIMIT during ${tag}: YouTube báo đã đạt giới hạn tải video lên hằng ngày`);
  }
}

async function upload(page, v, tag, hhmm) {
  console.log(`\n=== ${tag}: ${v.title}`);
  await page.goto(`https://studio.youtube.com/channel/${CH.channel_id}/videos/upload?d=ud`, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(5000);
  const dlg = page.locator('ytcp-uploads-dialog').first();
  await dlg.locator('input[type="file"]').first().setInputFiles(stage(v.file));
  const title = dlg.locator('#title-textarea #textbox').first();
  await title.waitFor({ timeout: 120000 }); await page.waitForTimeout(5000);
  await dismissPolicyWarning(page, tag);
  await checkDailyUploadLimit(page, dlg, tag);
  await dlg.locator('.dialog-scrim').first().waitFor({ state: 'hidden', timeout: 15000 }).catch(() => {});
  await title.click(); await page.keyboard.press('Control+A'); await page.keyboard.press('Backspace');
  await title.pressSequentially(v.title, { delay: 5 });
  const desc = dlg.locator('#description-textarea #textbox').first();
  await desc.click(); await page.keyboard.press('Control+A'); await page.keyboard.press('Backspace');
  await desc.fill(v.desc);
  if (v.thumb && fs.existsSync(v.thumb)) {
    const ti = dlg.locator('input#file-loader, input[type="file"][accept*="image"]').first();
    if (await ti.count()) { await ti.setInputFiles(stage(v.thumb)); await page.waitForTimeout(3000); console.log('  thumbnail set'); }
  }
  await dismissPolicyWarning(page, tag);
  try {
    const plTrigger = dlg.locator('ytcp-video-metadata-playlists #basics-playlists-dropdown, ytcp-video-metadata-playlists #trigger, ytcp-video-metadata-playlists ytcp-dropdown-trigger').first();
    await plTrigger.scrollIntoViewIfNeeded();
    await plTrigger.click({ timeout: 5000 });
    await page.waitForTimeout(1500);
    const plClicked = await page.evaluate((plName) => {
      const items = [...document.querySelectorAll('ytcp-playlist-dialog li, ytcp-playlist-dialog ytcp-checkbox-lit, ytcp-playlist-dialog tp-yt-paper-checkbox')];
      for (const item of items) {
        if (item.innerText && item.innerText.includes(plName)) {
          const cb = item.querySelector('tp-yt-paper-checkbox, input[type="checkbox"], #checkbox') || item;
          cb.click();
          return true;
        }
      }
      return false;
    }, CH.playlist);
    if (!plClicked) throw new Error(`playlist "${CH.playlist}" not found in dialog`);
    await page.waitForTimeout(1000);
    await page.locator('ytcp-playlist-dialog ytcp-button:has-text("Xong"), ytcp-playlist-dialog #done-button, ytcp-playlist-dialog button:has-text("Xong")').first().click({ timeout: 5000 });
    console.log('  playlist set');
  } catch (e) {  // LESSON-86: this used to fail silently for weeks because the playlist did not exist
    console.log(`  !! PLAYLIST NOT SET (${e.message}) — add the video to "${CH.playlist}" by hand`);
    await page.keyboard.press('Escape').catch(() => {});
  }
  await dlg.locator('[name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]').first().click({ force: true }); // LESSON-41
  try { await dlg.locator('#toggle-button').first().click({ timeout: 4000 }); await page.waitForTimeout(1000); } catch {}
  try { await dlg.locator('[name="VIDEO_HAS_ALTERED_CONTENT_NO"]').first().click({ force: true, timeout: 4000 }); } catch {}
  try {
    const tags = dlg.locator('#tags-container input').first();
    await tags.scrollIntoViewIfNeeded(); await tags.click(); await tags.fill(v.tags + ','); console.log('  tags set');
  } catch { console.log('  tags skipped'); }
  await shot(page, `${tag}_details`);
  await checkDailyUploadLimit(page, dlg, tag);
  const next = dlg.locator('#next-button');
  for (let i = 0; i < 6; i++) {
    const step = await dlg.getAttribute('workflow-step').catch(() => null);
    if (step === 'REVIEW' || step === 'PUBLISH') break;
    await next.click({ force: true }); await page.waitForTimeout(2500);
  }
  await setScheduleInDialog(page, dlg, hhmm, tag);
  const link = await dlg.locator('a[href*="youtu.be/"], a[href*="/shorts/"], a[href*="watch?v="]').first().getAttribute('href').catch(() => null);
  console.log('  url =', link);
  await dlg.locator('#done-button').first().click({ force: true });
  await page.waitForTimeout(5000);
  // If checks are still running, Studio pops up "Chúng tôi vẫn đang kiểm tra nội dung của bạn" -> click confirm ("Đã hiểu" / "Vẫn lên lịch")
  const checkDlg = page.locator('tp-yt-paper-dialog, ytcp-dialog').filter({ hasText: /vẫn đang kiểm tra|still checking/i }).last();
  if (await checkDlg.isVisible().catch(() => false)) {
    console.log(`  [!] Dismissing "still checking" confirmation during ${tag}`);
    const okBtn = checkDlg.locator('ytcp-button, button').filter({ hasText: /Đã hiểu|Vẫn lên lịch|Vẫn xuất bản|Got it|Schedule anyway/i }).last();
    if (await okBtn.count()) { await okBtn.click({ force: true }); await page.waitForTimeout(4000); }
  }
  for (let i = 0; i < 180; i++) { // wait until the file transfer is done (max 30 min)
    const s = (await page.locator('ytcp-uploads-still-processing-dialog, ytcp-multi-progress-monitor').allInnerTexts().catch(() => [])).join(' ');
    if (i > 0 && !/Đang tải lên|Đã tải được|Uploading/i.test(s)) break;
    if (i % 6 === 0) console.log('  ...', s.replace(/\s+/g, ' ').slice(0, 90));
    await page.waitForTimeout(10000);
  }
  try { await page.locator('ytcp-uploads-still-processing-dialog #close-button, ytcp-dialog #close-button').first().click({ timeout: 3000 }); } catch {}
  const m = (link || '').match(/(?:youtu\.be\/|shorts\/|v=)([\w-]{11})/);
  return m ? m[1] : findId(page, tag === 'long' ? 'upload' : 'short', v.title); // Studio tab is /videos/short (not "shorts")
}

async function findId(page, tab, title) {
  await page.goto(`https://studio.youtube.com/channel/${CH.channel_id}/videos/${tab}`, { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(10000);
  const links = await page.locator('a[href*="/video/"]').evaluateAll(as => as.map(a => [a.href, (a.closest('ytcp-video-row') || a).innerText]));
  const hit = links.find(([, t]) => t.includes(title.slice(0, 35)));
  if (hit) return hit[0].match(/video\/([\w-]{11})/)[1];
  // Processing/draft rows have no <a href>: click the title text and read the id from the URL (?udvid= or /video/).
  try {
    await page.getByText(title.slice(0, 30), { exact: false }).first().click({ timeout: 15000 });
    await page.waitForTimeout(6000);
    const m = page.url().match(/(?:video\/|[?&]udvid=)([\w-]{11})/);
    return m ? m[1] : null;
  } catch { return null; }
}

// End screen "1 video, 1 playlist, 1 subscribe" -> playlist CH.playlist (verified 2026-11-10 on EP1-12).
async function addEndScreen(page, id) {
  await page.goto(`https://studio.youtube.com/video/${id}/edit`, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(8000);
  page.locator('ytcp-video-metadata-editor-sidepanel').getByText('Màn hình kết thúc', { exact: true }).first().click({ noWaitAfter: true }).catch(() => {});
  await page.waitForTimeout(10000);
  const existing = await page.locator('ytve-endscreen-row').count();
  if (existing >= 3) {
    await page.keyboard.press('Escape');
    await shot(page, 'long_endscreen_verified');
    return `already set (${existing} elements)`;
  }
  await page.locator('[role=gridcell][aria-label="1 video, 1 danh sách phát, 1 đăng ký"]').first().click({ noWaitAfter: true });
  await page.waitForTimeout(4000);
  await page.locator('ytve-endscreen-editor-preview-overlay-item.error').first().click({ force: true, noWaitAfter: true });
  await page.waitForTimeout(2500);
  const box = await page.locator('ytve-options-panel-entity-item .entityName').first().boundingBox();
  if (box) await page.mouse.click(box.x + box.width / 2, box.y + box.height / 2);
  await page.waitForTimeout(5000);
  await page.locator('ytcp-playlist-pick-dialog ytcp-entity-card').filter({ hasText: CH.playlist }).first().click({ force: true, noWaitAfter: true });
  await page.waitForTimeout(3000);
  if (await page.locator('ytve-endscreen-editor-preview-overlay-item.error').count()) {
    await page.keyboard.press('Escape');
    throw new Error('end screen playlist not set');
  }
  await page.locator('ytve-endscreen-modal ytcp-button:has-text("Lưu")').first().click({ noWaitAfter: true });
  await page.waitForTimeout(6000);
  await shot(page, 'long_endscreen_saved');
  return 'saved (1 video, 1 playlist, 1 subscribe)';
}

// English title + description translation (TASTE-42). Supports both new Studio drawer UI and legacy table UI.
async function addEnglish(page, id, title, desc) {
  await page.goto(`https://studio.youtube.com/video/${id}/translations`, { timeout: 60000, waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(8000);
  // 1) Check ytgn-video-translation-row first (cells: [0]=Âm thanh, [1]=Phụ đề, [2]=Tiêu đề và mô tả)
  const enRow = () => page.locator('ytgn-video-translation-row').filter({ hasText: /^\s*Tiếng Anh\s/ }).first();
  if (await enRow().count()) {
    const rowTxt = (await enRow().innerText()).replace(/\s+/g, ' ').trim();
    const cells = enRow().locator('#cell-container');
    const metaCell = (await cells.count()) >= 3 ? cells.nth(2) : cells.nth(1);
    const txt = (await metaCell.innerText().catch(() => '')).trim();
    if (/Đã xuất bản|Published/i.test(rowTxt) || (txt && txt !== '–' && txt !== '-')) return 'already set';
    const box = await metaCell.boundingBox();
    if (box) {
      await page.mouse.move(box.x + box.width / 2, box.y + box.height / 2);
      await page.waitForTimeout(1200);
    }
    const b = await enRow().evaluate(e => { const x = [...e.querySelectorAll('#metadata-add, #metadata-edit, ytcp-button')].find(b => b.getBoundingClientRect().width > 0); if (!x) return null; const r = x.getBoundingClientRect(); return [r.x + r.width / 2, r.y + r.height / 2]; });
    if (b) {
      await page.mouse.click(b[0], b[1]);
      await page.waitForTimeout(4000);
      const dlg = page.locator('tp-yt-paper-dialog:visible').filter({ hasText: 'Bản dịch' }).last();
      if (await dlg.count()) {
        const ta = dlg.locator('textarea');
        await ta.nth(1).fill(title); await ta.nth(3).fill(desc);
        await dlg.locator('ytcp-button:has-text("Xuất bản")').first().click({ noWaitAfter: true });
        await page.waitForTimeout(5000);
        return 'published';
      }
      const titleBox = page.locator('div#textbox[aria-label="Tiêu đề"], div#textbox[aria-label="Title"]').filter({ visible: true }).last();
      await titleBox.waitFor({ timeout: 15000 });
      await titleBox.click(); await page.keyboard.press('Control+A'); await page.keyboard.press('Backspace');
      await titleBox.fill(title);
      const descBox = page.locator('div#textbox[aria-label="Mô tả"], div#textbox[aria-label="Description"]').filter({ visible: true }).last();
      await descBox.click(); await page.keyboard.press('Control+A'); await page.keyboard.press('Backspace');
      await descBox.fill(desc);
      await page.waitForTimeout(1500);
      const updBtn = page.locator('ytcp-button:has-text("Cập nhật"), ytcp-button:has-text("Xuất bản"), ytcp-button:has-text("Update"), ytcp-button:has-text("Publish")').filter({ visible: true }).first();
      if ((await updBtn.getAttribute('aria-disabled')) === 'true') return 'already set';
      await updBtn.click();
      await page.waitForTimeout(5000);
      return 'published';
    }
    throw new Error('English "Thêm" button not found');
  }
  // 2) New Studio translations table: check if a row with "Tiếng Anh" already has translated title
  const trEn = page.locator('tbody tr').filter({ hasText: /^\s*Tiếng Anh(\s|$)/ }).first();
  if (await trEn.count()) {
    const rowTxt = (await trEn.innerText()).replace(/\s+/g, ' ').trim();
    if (rowTxt.includes(title.slice(0, 20))) return 'already set';
  }
  // Open "Thêm ngôn ngữ" -> "Tiếng Anh" (test-id="en")
  await page.getByText('Thêm ngôn ngữ', { exact: true }).filter({ visible: true }).first().click();
  await page.waitForTimeout(2500);
  await page.locator('tp-yt-paper-item[test-id="en"]:visible, tp-yt-paper-item:visible, [role="option"]:visible').filter({ hasText: /^\s*Tiếng Anh\s*$/ }).first().click({ force: true });
  await page.waitForTimeout(4000);
  // Check if legacy row appeared or new drawer/panel opened
  if (await enRow().count()) {
    const cell = enRow().locator('#cell-container').nth(1);
    const box = await cell.boundingBox();
    await page.mouse.move(box.x + box.width / 2, box.y + box.height / 2);
    await page.waitForTimeout(1200);
    const b = await enRow().evaluate(e => { const x = [...e.querySelectorAll('#metadata-add, ytcp-button')].find(b => b.getBoundingClientRect().width > 0); if (!x) return null; const r = x.getBoundingClientRect(); return [r.x + r.width / 2, r.y + r.height / 2]; });
    if (!b) throw new Error('English "Thêm" button not found');
    await page.mouse.click(b[0], b[1]);
    await page.waitForTimeout(4000);
    const dlg = page.locator('tp-yt-paper-dialog:visible').filter({ hasText: 'Bản dịch' }).last();
    const ta = dlg.locator('textarea');
    await ta.nth(1).fill(title); await ta.nth(3).fill(desc);
    await dlg.locator('ytcp-button:has-text("Xuất bản")').first().click({ noWaitAfter: true });
    await page.waitForTimeout(5000);
    return 'published';
  }
  const titleBox = page.locator('div#textbox[aria-label="Tiêu đề"], div#textbox[aria-label="Title"]').filter({ visible: true }).last();
  await titleBox.waitFor({ timeout: 15000 });
  await titleBox.click(); await page.keyboard.press('Control+A'); await page.keyboard.press('Backspace');
  await titleBox.fill(title);
  const descBox = page.locator('div#textbox[aria-label="Mô tả"], div#textbox[aria-label="Description"]').filter({ visible: true }).last();
  await descBox.click(); await page.keyboard.press('Control+A'); await page.keyboard.press('Backspace');
  await descBox.fill(desc);
  await page.waitForTimeout(1500);
  const updBtn = page.locator('ytcp-button:has-text("Cập nhật"), ytcp-button:has-text("Xuất bản"), ytcp-button:has-text("Update"), ytcp-button:has-text("Publish")').filter({ visible: true }).first();
  if ((await updBtn.getAttribute('aria-disabled')) === 'true') return 'already set';
  await updBtn.click();
  await page.waitForTimeout(5000);
  return 'published';
}

(async () => {
  const ctx = await chromium.launchPersistentContext(CH.chrome_profile, {
    headless: false, channel: 'chrome', viewport: { width: 1500, height: 900 }, args: ['--disable-blink-features=AutomationControlled'],
  });
  const page = ctx.pages()[0] || await ctx.newPage();
  const res = { date: DATE, time: TIME };
  try {
    const FIX = process.argv.includes('--fix-only'); // ids already uploaded: --fix-only --long-id X --shorts-id Y
    if (ONLY !== 'shorts') res.long_id = FIX ? arg('--long-id') : await upload(page, UP.long, 'long', TIME);
    if (ONLY !== 'long') { useDate(SDATE); res.shorts_id = FIX ? arg('--shorts-id') : await upload(page, UP.shorts, 'shorts', STIME); }
    if (SDATE !== DATE) res.shorts_date = SDATE;
    if (STIME !== TIME) res.shorts_time = STIME;
    for (const [k, hh, dd] of [['long', TIME, DATE], ['shorts', STIME, SDATE]]) {
      const id = res[`${k}_id`];
      if (!id) continue;
      useDate(dd);
      res[`${k}_url`] = `https://youtu.be/${id}`;
      res[`${k}_schedule`] = await fixSchedule(page, id, hh, k);
    }
    // Post-upload extras: never fatal, but always reported (LESSON-86).
    if (res.long_id) {
      try { res.long_endscreen = await addEndScreen(page, res.long_id); } catch (e) { res.long_endscreen = `FAILED: ${e.message}`; }
      console.log(`  long end screen: ${res.long_endscreen}`);
    }
    for (const k of ['long', 'shorts']) {
      const v = UP[k], id = res[`${k}_id`];
      if (!id || !v || !v.en_title) continue;
      try { res[`${k}_english`] = await addEnglish(page, id, v.en_title, v.en_desc || ''); } catch (e) { res[`${k}_english`] = `FAILED: ${e.message}`; }
      console.log(`  ${k} English metadata: ${res[`${k}_english`]}`);
    }
    if (res.shorts_id && res.long_id)
      console.log(`  !! Shorts "Video có liên quan" -> ${res.long_url}: set by hand in Studio (needs one-time channel verification)`);
    console.log('\nRESULT', JSON.stringify(res, null, 1));
    fs.writeFileSync(path.join(P, 'upload_result.json'), JSON.stringify(res, null, 2));
  } catch (e) { console.error('UPLOAD ERROR:', e.message); await shot(page, 'error'); process.exitCode = 1; }
  finally { await ctx.close(); }
})();
