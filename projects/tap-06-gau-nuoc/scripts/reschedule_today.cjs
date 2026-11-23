/** Move the EP06 long + Shorts schedule to TODAY at HH:MM. Usage: node reschedule_today.cjs HH:MM */
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const PROFILE = 'C:\\Users\\PC\\AppData\\Local\\ms-playwright-mcp\\mcp-chrome-aad48e1';
const CHANNEL = 'UCMX7XBHXoiq_kWIUo73n1Vw';
const SNAP = path.resolve(__dirname, '..', 'renders', 'snapshots');
const HHMM = process.argv[2] || '18:30';
const d = new Date();
const TODAY = `${d.getDate()} thg ${d.getMonth() + 1}, ${d.getFullYear()}`;

async function findIds(page) {
  const ids = {};
  for (const [tab, key, re] of [['upload', 'long', /Gấu Nước \| Tập 6/], ['shorts', 'shorts', /Ốc Sên\?!/]]) {
    await page.goto(`https://studio.youtube.com/channel/${CHANNEL}/videos/${tab}`, { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(8000);
    const links = await page.locator('a[href*="/video/"]').evaluateAll(as => as.map(a => [a.href, (a.closest('ytcp-video-row') || a).innerText]));
    for (const [href, txt] of links) if (re.test(txt)) { ids[key] = href.match(/video\/([\w-]{11})/)[1]; break; }
  }
  return ids;
}

async function reschedule(page, id, tag) {
  await page.goto(`https://studio.youtube.com/video/${id}/edit`, { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(7000);
  await page.locator('ytcp-video-metadata-visibility #select-button, ytcp-video-metadata-visibility').first().click();
  await page.waitForTimeout(2000);
  const dlg = page.locator('ytcp-video-visibility-select, tp-yt-paper-dialog:has(#second-container)').last();
  try { await page.locator('#second-container-expand-button').last().click({ timeout: 3000 }); } catch {}
  await page.waitForTimeout(1000);
  // date
  await page.locator('#datepicker-trigger').last().click();
  await page.waitForTimeout(1000);
  const dateIn = page.locator('ytcp-date-picker input, tp-yt-paper-dialog ytcp-date-picker tp-yt-paper-input input').last();
  await dateIn.click(); await page.keyboard.press('Control+A'); await dateIn.pressSequentially(TODAY, { delay: 30 });
  await page.keyboard.press('Enter'); await page.waitForTimeout(1200);
  // time
  const timeIn = page.locator('#time-of-day-container input, ytcp-datetime-picker #time-of-day-trigger input').last();
  await timeIn.click(); await page.keyboard.press('Control+A'); await timeIn.pressSequentially(HHMM, { delay: 40 });
  await page.keyboard.press('Enter'); await page.waitForTimeout(1200);
  const dt = (await page.locator('#datepicker-trigger').last().innerText()).trim();
  const tv = await timeIn.inputValue();
  console.log(`${tag} ${id}: ${dt} ${tv}`);
  await page.screenshot({ path: path.join(SNAP, `ep06_resched_${tag}.png`) });
  if (!dt.startsWith(`${d.getDate()} `) || tv.trim() !== HHMM) throw new Error(`${tag}: schedule not applied (${dt} ${tv})`);
  await page.locator('#save-button, ytcp-button:has-text("Xong")').filter({ visible: true }).first().click();
  await page.waitForTimeout(2000);
  const save = page.locator('ytcp-button#save, #save').filter({ visible: true }).first();
  if (await save.count()) { await save.click(); await page.waitForTimeout(4000); }
  await page.screenshot({ path: path.join(SNAP, `ep06_resched_${tag}_saved.png`) });
}

(async () => {
  const ctx = await chromium.launchPersistentContext(PROFILE, { headless: false, channel: 'chrome', viewport: { width: 1600, height: 1000 }, args: ['--disable-blink-features=AutomationControlled'] });
  const page = ctx.pages()[0] || await ctx.newPage();
  try {
    const ids = process.argv[3] ? JSON.parse(process.argv[3]) : await findIds(page);
    console.log('ids', ids);
    for (const k of ['long', 'shorts']) if (ids[k]) await reschedule(page, ids[k], k);
    fs.writeFileSync(path.resolve(__dirname, '..', 'upload_result.json'), JSON.stringify({ date: TODAY, time: HHMM, ...Object.fromEntries(Object.entries(ids).map(([k, v]) => [k, `https://youtu.be/${v}`])) }, null, 2));
  } catch (e) { console.error('ERR', e.message); await page.screenshot({ path: path.join(SNAP, 'ep06_resched_error.png') }); process.exitCode = 1; }
  finally { await ctx.close(); }
})();
