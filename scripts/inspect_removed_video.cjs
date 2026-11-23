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
  await page.goto(`https://studio.youtube.com/channel/${CH.channel_id}/videos/upload`, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(6000);

  // Click on the first video row (the removed one)
  const firstRow = page.locator('ytcp-video-row').first();
  const text = await firstRow.innerText();
  console.log('FIRST ROW:\n', text);

  // Click on the title or restriction
  await firstRow.locator('#video-title, [id*="title"]').first().click().catch(() => {});
  await page.waitForTimeout(6000);
  await page.screenshot({ path: 'tmp/removed_video_detail.png' });

  const detailText = await page.evaluate(() => document.body.innerText.slice(0, 3000));
  console.log('DETAIL TEXT:\n', detailText.slice(0, 1500));

  await ctx.close();
})();
