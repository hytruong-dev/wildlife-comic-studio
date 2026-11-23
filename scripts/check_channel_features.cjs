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

  // Open Settings
  await page.locator('ytcp-navigation-drawer #menu-item-settings, [test-id="settings-item"], text="Cài đặt"').first().click().catch(() => {});
  await page.waitForTimeout(3000);
  await page.getByText('Kênh', { exact: true }).first().click().catch(() => {});
  await page.waitForTimeout(2000);
  await page.getByText('Điều kiện sử dụng tính năng', { exact: true }).first().click().catch(() => {});
  await page.waitForTimeout(3000);
  await page.screenshot({ path: 'tmp/channel_features.png' });
  const featText = await page.locator('ytcp-settings-dialog, tp-yt-paper-dialog').last().innerText().catch(() => '');
  console.log('FEATURES:\n', featText);

  await ctx.close();
})();
