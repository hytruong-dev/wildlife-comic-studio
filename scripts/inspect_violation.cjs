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
  const link = page.getByText('Lời cảnh cáo về Nguyên tắc cộng đồng', { exact: false }).first();
  await link.waitFor({ timeout: 25000 }).catch(() => {});
  await page.waitForTimeout(2000);
  await page.screenshot({ path: 'tmp/dashboard_violation2.png' });
  if (await link.isVisible().catch(() => false)) {
    await link.click();
    await page.waitForTimeout(4000);
    await page.screenshot({ path: 'tmp/violation_modal2.png' });
    const modalText = await page.evaluate(() => {
      return [...document.querySelectorAll('tp-yt-paper-dialog, ytcp-dialog')].filter(e => e.offsetParent).map(e => e.innerText).join('\n---\n');
    });
    console.log('MODAL TEXT:\n', modalText.slice(0, 2500));
  } else {
    console.log('Link not found after 25s');
  }
  await ctx.close();
})();
