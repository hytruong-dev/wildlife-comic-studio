/**
 * Gắn "Video có liên quan" cho Shorts -> video dài cùng tập (TASTE-68).
 * Shorts không có liên kết này thì người xem Shorts không có nút sang bản dài (đo 12/11/2026: 1.000-3.500 view Shorts
 * nhưng video dài chỉ 0-33 view).
 *
 *   node src/episode/link_shorts_related.cjs projects/<slug> [projects/<slug2> ...]
 *   node src/episode/link_shorts_related.cjs --pair <shortsId> <longId>
 *
 * Đọc shorts_id / long_id từ projects/<slug>/upload_result.json. Ghi kết quả vào upload_result.json (shorts_related).
 */
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '../..');
const CH = require('./channel_config.cjs').loadChannel();  // channel.json + config/local.json (riêng từng máy)

const jobs = [];
const argv = process.argv.slice(2);
if (argv[0] === '--pair') jobs.push({ sid: argv[1], lid: argv[2] });
else for (const p of argv) {
  const f = path.join(path.resolve(p), 'upload_result.json');
  const r = JSON.parse(fs.readFileSync(f, 'utf8'));
  const sid = r.shorts_id || ((r.shorts || '').match(/youtu\.be\/([\w-]{11})/) || [])[1];
  const lid = r.long_id || ((r.long || '').match(/youtu\.be\/([\w-]{11})/) || [])[1];
  jobs.push({ sid, lid, file: f });
}
if (!jobs.length || jobs.some(j => !j.sid || !j.lid)) { console.log('usage: see header'); process.exit(1); }

async function link(page, sid, lid) {
  await page.goto(`https://studio.youtube.com/video/${sid}/edit`, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(9000);
  const label = page.getByText('Video có liên quan', { exact: true }).first();
  await label.scrollIntoViewIfNeeded();
  const before = await page.evaluate(() => { const t = document.body.innerText; const i = t.indexOf('Video có liên quan'); return t.slice(i + 18, i + 120).trim().split('\n')[0]; });
  await label.click();
  await page.waitForTimeout(4000);
  const dlg = page.locator('ytcp-video-pick-dialog').filter({ visible: true }).first();
  await dlg.waitFor({ timeout: 15000 });
  const search = dlg.locator('input[placeholder="Tìm kiếm video của bạn"]').first();
  await search.click();
  await search.fill(lid);
  await page.waitForTimeout(4000);
  // Result cards: pick the one whose thumbnail/link contains the long id, else the first card.
  const picked = await dlg.evaluate((el, lid) => {
    const vis = e => e.getBoundingClientRect().width > 0;
    const cards = [...el.querySelectorAll('ytcp-entity-card, ytcp-video-pick-dialog-video-card, [role=option], .card, ytcp-video-row')].filter(vis);
    let c = cards.find(x => x.innerHTML.includes(lid)) || cards[0];
    if (!c) return null;
    c.scrollIntoView(); c.click();
    return (c.innerText || '').replace(/\s+/g, ' ').slice(0, 90);
  }, lid);
  if (!picked) throw new Error('no search result for ' + lid);
  await page.waitForTimeout(3000);
  const after = await page.evaluate(() => { const t = document.body.innerText; const i = t.indexOf('Video có liên quan'); return t.slice(i + 18, i + 160).trim().split('\n')[0]; });
  const save = page.locator('ytcp-button#save, #save').filter({ visible: true }).first();
  if ((await save.getAttribute('aria-disabled')) === 'true') return { before, after, picked, saved: false };
  await save.click({ timeout: 15000 });
  await page.waitForTimeout(5000);
  return { before, after, picked, saved: true };
}

(async () => {
  const ctx = await chromium.launchPersistentContext(CH.chrome_profile, {
    headless: false, channel: 'chrome', viewport: { width: 1500, height: 900 }, args: ['--disable-blink-features=AutomationControlled'],
  });
  const page = ctx.pages()[0] || await ctx.newPage();
  for (const j of jobs) {
    let res;
    try { res = await link(page, j.sid, j.lid); } catch (e) { res = { error: e.message.split('\n')[0] }; }
    console.log(`${j.sid} -> ${j.lid}:`, JSON.stringify(res));
    if (j.file && !res.error) {
      const r = JSON.parse(fs.readFileSync(j.file, 'utf8'));
      r.shorts_related = `${res.after} (${res.saved ? 'saved' : 'unchanged'})`;
      fs.writeFileSync(j.file, JSON.stringify(r, null, 2));
    }
  }
  await ctx.close();
})();
