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
  await page.waitForTimeout(8000);

  const hasWarn = await page.evaluate(() => document.body.innerText.includes('Cảnh báo') || document.body.innerText.includes('vi phạm'));
  console.log('Dashboard hasWarn:', hasWarn);

  // Open Settings properly using bottom-left button
  await page.locator('#settings-item').click().catch(async () => {
    await page.locator('ytcp-navigation-drawer').getByText('Cài đặt').click();
  });
  await page.waitForTimeout(3000);
  await page.locator('ytcp-settings-dialog').getByText('Kênh', { exact: true }).click();
  await page.waitForTimeout(2000);
  await page.locator('ytcp-settings-dialog').getByText('Điều kiện sử dụng tính năng').click();
  await page.waitForTimeout(2000);
  await page.screenshot({ path: 'tmp/features_real.png' });
  const txt = await page.locator('ytcp-settings-dialog').innerText();
  console.log('FEATURES REAL:\n', txt);

  await ctx.close();
})();
