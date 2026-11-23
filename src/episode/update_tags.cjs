/**
 * Bổ sung THẺ TAG (chỉ tag) cho video dài ĐÃ upload, lấy từ projects/<slug>/upload.json (long.tags).
 * GIỮ NGUYÊN mọi tag đang có trên video, chỉ thêm tag còn thiếu (dừng trước giới hạn 500 ký tự của Studio).
 * Không đụng tiêu đề, mô tả, thumbnail, lịch đăng, chế độ hiển thị.
 *
 *   node src/episode/update_tags.cjs projects/<slug> [projects/<slug2> ...] [--dry-run]
 *
 * --dry-run: mở trang sửa, điền tag, đọc lại để so khớp, rồi HUỶ (không bấm Lưu).
 * Đọc long_id từ upload_result.json; ghi kết quả vào upload_result.json (tags_update).
 * Dùng Chrome profile đã đăng nhập kênh (config/channel.json) — đóng các cửa sổ Chrome dùng profile đó trước.
 */
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '../..');
const CH = require('./channel_config.cjs').loadChannel();  // channel.json + config/local.json (riêng từng máy)
const DRY = process.argv.includes('--dry-run');
const projects = process.argv.slice(2).filter(a => !a.startsWith('--'));

const jobs = projects.map(p => {
  const P = path.resolve(p);
  const up = JSON.parse(fs.readFileSync(path.join(P, 'upload.json'), 'utf8'));
  const resFile = path.join(P, 'upload_result.json');
  const res = JSON.parse(fs.readFileSync(resFile, 'utf8'));
  const id = res.long_id || ((res.long_url || '').match(/youtu\.be\/([\w-]{11})/) || [])[1];
  const tags = (up.long.tags || '').split(',').map(t => t.trim()).filter(Boolean);
  return { slug: path.basename(P), id, tags, resFile };
});
if (!jobs.length || jobs.some(j => !j.id || !j.tags.length)) { console.log('usage: see header (thiếu long_id hoặc tags)'); process.exit(1); }

const norm = s => s.normalize('NFC').trim().toLowerCase();

async function readChips(page) {
  return page.evaluate(() => {
    const box = document.querySelector('ytcp-video-metadata-editor #tags-container, #tags-container');
    if (!box) return null;
    return [...box.querySelectorAll('ytcp-chip, ytcp-chip-bar ytcp-chip')]
      .map(c => (c.getAttribute('text') || c.innerText || '').replace(/\s*close\s*$/i, '').trim()).filter(Boolean);
  });
}

async function updateOne(page, j) {
  await page.goto(`https://studio.youtube.com/video/${j.id}/edit`, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(8000);
  // Tag nằm trong phần "Hiện thêm" ở trang chi tiết video.
  const more = page.locator('ytcp-video-metadata-editor #toggle-button, #toggle-button').filter({ visible: true }).first();
  if (await more.count()) { await more.scrollIntoViewIfNeeded(); await more.click(); await page.waitForTimeout(2000); }
  const input = page.locator('#tags-container input').filter({ visible: true }).first();
  await input.waitFor({ timeout: 15000 });
  await input.scrollIntoViewIfNeeded();
  const before = await readChips(page);
  console.log(`  ${j.slug} live tags (${(before || []).length}): ${JSON.stringify(before)}`);

  // Giữ tag hiện có trên video (có thể đã được chủ kênh/upload thêm tay), chỉ thêm tag mới còn thiếu.
  // Không xoá tag cũ: an toàn hơn và không mất từ khoá đang có lượt xem.
  const have = new Set((before || []).map(norm));
  j.tags = j.tags.filter(t => !have.has(norm(t)));
  const merged = [...(before || []), ...j.tags];
  const ytLen = merged.reduce((s, t) => s + t.length + (t.includes(' ') ? 2 : 0), 0) + Math.max(merged.length - 1, 0);
  if (ytLen > 495) {
    // Vượt giới hạn 500 ký tự của Studio: chỉ thêm tag mới theo thứ tự ưu tiên tới khi đầy.
    const keep = [];
    let len = (before || []).reduce((s, t) => s + t.length + (t.includes(' ') ? 2 : 0), 0) + Math.max((before || []).length - 1, 0);
    for (const t of j.tags) { const add = t.length + (t.includes(' ') ? 2 : 0) + 1; if (len + add <= 495) { keep.push(t); len += add; } }
    j.tags = keep;
  }
  j.want = [...(before || []), ...j.tags];
  if (!j.tags.length) return { id: j.id, before: (before || []).length, after: (before || []).length, added: [], saved: false, note: 'nothing new to add' };
  // Điền tag mới ở cuối (dấu phẩy biến mỗi tag thành 1 chip).
  await input.click(); await page.keyboard.press('End');
  await input.fill(j.tags.join(',') + ',');
  await page.keyboard.press('Enter').catch(() => {});
  await page.waitForTimeout(1500);

  const after = await readChips(page) || [];
  const want = j.want.map(norm), got = after.map(norm);
  const missing = want.filter(t => !got.includes(t)), extra = got.filter(t => !want.includes(t));
  const ok = !missing.length && !extra.length;
  const info = { id: j.id, before: (before || []).length, after: after.length, added: j.tags, missing, extra };
  if (!ok) { await page.keyboard.press('Escape').catch(() => {}); return { ...info, saved: false, error: 'tag mismatch — not saved' }; }
  if (DRY) {
    const undo = page.locator('ytcp-button#discard, #discard, ytcp-button:has-text("Hủy thay đổi"), ytcp-button:has-text("Undo changes")').filter({ visible: true }).first();
    if (await undo.count()) await undo.click().catch(() => {});
    return { ...info, saved: false, dry_run: true };
  }
  const save = page.locator('ytcp-button#save, #save').filter({ visible: true }).first();
  if ((await save.getAttribute('aria-disabled')) === 'true') return { ...info, saved: false, note: 'unchanged' };
  await save.click({ timeout: 15000 });
  await page.waitForTimeout(5000);
  // Xác minh sau khi lưu: tải lại trang và đọc lại tag.
  await page.reload({ waitUntil: 'domcontentloaded' }); await page.waitForTimeout(8000);
  const more2 = page.locator('#toggle-button').filter({ visible: true }).first();
  if (await more2.count()) { await more2.click(); await page.waitForTimeout(2000); }
  const persisted = (await readChips(page) || []).map(norm);
  const lost = want.filter(t => !persisted.includes(t));
  return { ...info, saved: true, verified: !lost.length, lost };
}

(async () => {
  const ctx = await chromium.launchPersistentContext(CH.chrome_profile, {
    headless: false, channel: 'chrome', viewport: { width: 1500, height: 900 }, args: ['--disable-blink-features=AutomationControlled'],
  });
  const page = ctx.pages()[0] || await ctx.newPage();
  let fails = 0;
  for (const j of jobs) {
    let r;
    try { r = await updateOne(page, j); } catch (e) { r = { id: j.id, error: e.message.split('\n')[0] }; }
    if (r.error || (r.saved && !r.verified)) fails++;
    await page.screenshot({ path: path.join(path.dirname(j.resFile), 'renders', 'snapshots', `tags_update${DRY ? '_dry' : ''}.png`) }).catch(() => {});
    console.log(`${j.slug}: ${JSON.stringify(r)}`);
    if (!DRY && r.saved) {
      const res = JSON.parse(fs.readFileSync(j.resFile, 'utf8'));
      res.tags_update = `${new Date().toISOString()} ${r.after} tags ${r.verified ? 'verified' : 'UNVERIFIED'}`;
      fs.writeFileSync(j.resFile, JSON.stringify(res, null, 2));
    }
  }
  await ctx.close();
  process.exitCode = fails ? 1 : 0;
})();
