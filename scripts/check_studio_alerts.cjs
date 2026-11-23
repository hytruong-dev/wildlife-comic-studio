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
  await page.screenshot({ path: 'tmp/studio_check.png' });
  
  const dialogs = await page.evaluate(() => {
    return [...document.querySelectorAll('tp-yt-paper-dialog, ytcp-dialog, ytcp-confirmation-dialog, [role="dialog"]')].map(d => ({
      tagName: d.tagName,
      id: d.id,
      text: d.innerText ? d.innerText.slice(0, 500) : ''
    }));
  });
  
  console.log('DIALOGS:', JSON.stringify(dialogs, null, 2));
  await ctx.close();
})();
