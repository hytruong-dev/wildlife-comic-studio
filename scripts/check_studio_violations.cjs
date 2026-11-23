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
  await page.waitForTimeout(6000);

  // Check notification bell or alerts
  const alerts = await page.evaluate(() => {
    return [...document.querySelectorAll('ytcp-notification-card, ytcp-banner, .alert, #alerts, [class*="strike"], [class*="warning"]')].map(e => e.innerText.replace(/\s+/g, ' ').slice(0, 300));
  });
  console.log('ALERTS:', alerts);

  // Open channel settings -> Feature eligibility
  await page.goto(`https://studio.youtube.com/channel/${CH.channel_id}/settings`, { waitUntil: 'domcontentloaded', timeout: 60000 }).catch(() => {});
  await page.waitForTimeout(4000);
  
  // Check videos/upload with filter or scroll
  await page.goto(`https://studio.youtube.com/channel/${CH.channel_id}/videos/upload`, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(6000);
  const rows = await page.evaluate(() => {
    return [...document.querySelectorAll('ytcp-video-row')].map(r => r.innerText.replace(/\s+/g, ' ').slice(0, 120));
  });
  console.log('ALL UPLOAD ROWS (top 10):\n', rows.slice(0, 10).join('\n'));

  // Click notification bell if present
  await page.locator('#notification-button, ytcp-notification-bell, [aria-label*="Thông báo"]').first().click().catch(() => {});
  await page.waitForTimeout(3000);
  await page.screenshot({ path: 'tmp/notifications.png' });

  await ctx.close();
})();
