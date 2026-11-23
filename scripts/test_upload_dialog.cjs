const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const CH = JSON.parse(fs.readFileSync('config/channel.json', 'utf8'));

(async () => {
  const ctx = await chromium.launchPersistentContext(CH.chrome_profile, {
    headless: false, channel: 'chrome', viewport: { width: 1400, height: 900 },
    args: ['--disable-blink-features=AutomationControlled']
  });
  const page = ctx.pages()[0] || await ctx.newPage();
  await page.goto(`https://studio.youtube.com/channel/${CH.channel_id}/videos/upload?d=ud`, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(5000);
  await page.screenshot({ path: 'tmp/upload_dlg.png' });

  const modalText = await page.evaluate(() => {
    const dialogs = [...document.querySelectorAll('ytcp-uploads-dialog, tp-yt-paper-dialog, ytcp-dialog')].filter(d => d.offsetParent !== null);
    return dialogs.map(d => d.innerText.replace(/\s+/g, ' ').slice(0, 300));
  });
  console.log('VISIBLE DIALOGS:\n', modalText.join('\n---\n'));

  await ctx.close();
})();
