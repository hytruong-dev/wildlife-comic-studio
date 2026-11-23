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
  await page.goto(`https://studio.youtube.com/channel/${CH.channel_id}`, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(6000);
  await page.screenshot({ path: 'tmp/dashboard.png' });

  const text = await page.evaluate(() => document.body.innerText.slice(0, 3000));
  console.log('DASHBOARD TEXT:\n', text.slice(0, 1500));

  await page.goto(`https://studio.youtube.com/channel/${CH.channel_id}/videos/upload`, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(6000);
  await page.screenshot({ path: 'tmp/videos_list.png' });

  const rows = await page.evaluate(() => {
    return [...document.querySelectorAll('ytcp-video-row')].slice(0, 8).map(r => r.innerText.replace(/\s+/g, ' ').slice(0, 150));
  });
  console.log('VIDEOS LIST:\n', rows.join('\n'));

  await ctx.close();
})();
