const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const CH = JSON.parse(fs.readFileSync('config/channel.json', 'utf8'));
const STAGE = path.join(require('os').homedir(), '.playwright-mcp');
const staged = path.join(STAGE, 'tap-20-ca-cung-thu_long.mp4');

(async () => {
  const ctx = await chromium.launchPersistentContext(CH.chrome_profile, {
    headless: false, channel: 'chrome', viewport: { width: 1500, height: 900 },
    args: ['--disable-blink-features=AutomationControlled']
  });
  const page = ctx.pages()[0] || await ctx.newPage();
  await page.goto(`https://studio.youtube.com/channel/${CH.channel_id}/videos/upload?d=ud`, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(5000);
  const dlg = page.locator('ytcp-uploads-dialog').first();
  await dlg.locator('input[type="file"]').first().setInputFiles(staged);
  await dlg.locator('#title-textarea #textbox').first().waitFor({ timeout: 120000 });
  await page.waitForTimeout(8000);
  await page.screenshot({ path: 'tmp/upload_at_8s.png' });

  const scrimInfo = await page.evaluate(() => {
    const tb = document.querySelector('ytcp-uploads-dialog #title-textarea #textbox');
    const r = tb ? tb.getBoundingClientRect() : null;
    const hit = r ? document.elementFromPoint(r.x + 20, r.y + 10) : null;
    const hitChain = [];
    let cur = hit;
    while (cur && hitChain.length < 8) {
      hitChain.push(cur.tagName + '#' + cur.id + '.' + (cur.className || '').toString().slice(0, 40));
      cur = cur.parentElement || (cur.getRootNode && cur.getRootNode().host);
    }
    const allDialogs = [...document.querySelectorAll('tp-yt-paper-dialog, ytcp-dialog, ytcp-uploads-dialog')].map(d => ({
      tag: d.tagName, id: d.id,
      vis: d.getBoundingClientRect().width > 0,
      txt: (d.innerText || '').replace(/\s+/g, ' ').slice(0, 150)
    }));
    return { tbRect: r, hitChain, allDialogs };
  });
  console.log('SCRIM INFO AT 8s:\n', JSON.stringify(scrimInfo, null, 2));

  await ctx.close();
})();
