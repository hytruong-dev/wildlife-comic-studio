const { chromium } = require('playwright');
const fs = require('fs');

const CH = JSON.parse(fs.readFileSync('config/channel.json', 'utf8'));

(async () => {
  const ctx = await chromium.launchPersistentContext(CH.chrome_profile, {
    headless: false, channel: 'chrome', viewport: { width: 1400, height: 900 },
    args: ['--disable-blink-features=AutomationControlled']
  });
  const page = ctx.pages()[0] || await ctx.newPage();
  await page.goto(`https://studio.youtube.com/channel/${CH.channel_id}`, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(7000);

  await page.locator('ytcp-icon-button[aria-label="Thông báo"]').first().click();
  await page.waitForTimeout(3000);
  await page.mouse.click(950, 225);
  await page.waitForTimeout(5000);
  await page.screenshot({ path: 'tmp/violation_detail.png' });
  const text = await page.evaluate(() => {
    const dlgs = [...document.querySelectorAll('tp-yt-paper-dialog, ytcp-dialog')].filter(e => e.offsetParent);
    return dlgs.map(d => d.innerText).join('\n---\n') || document.body.innerText.slice(0, 2000);
  });
  console.log('VIOLATION DETAIL:\n', text.slice(0, 2500));

  await ctx.close();
})();
