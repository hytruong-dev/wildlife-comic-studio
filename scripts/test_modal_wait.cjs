const { chromium } = require('playwright');
const fs = require('fs');

const CH = JSON.parse(fs.readFileSync('config/channel.json', 'utf8'));

(async () => {
  const ctx = await chromium.launchPersistentContext(CH.chrome_profile, {
    headless: false, channel: 'chrome', viewport: { width: 1400, height: 900 },
    args: ['--disable-blink-features=AutomationControlled']
  });
  const page = ctx.pages()[0] || await ctx.newPage();
  await page.goto(`https://studio.youtube.com/channel/${CH.channel_id}/videos/upload?d=ud`, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(15000);
  await page.screenshot({ path: 'tmp/upload_wait15.png' });

  const modals = await page.evaluate(() => {
    return [...document.querySelectorAll('tp-yt-paper-dialog, ytcp-dialog')].filter(d => d.offsetParent).map(d => d.innerText.replace(/\s+/g, ' ').slice(0, 500));
  });
  console.log('MODALS AFTER 15s:', JSON.stringify(modals, null, 2));

  await ctx.close();
})();
