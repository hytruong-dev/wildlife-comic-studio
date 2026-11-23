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

  // Check for any warning card, strike card, or notification
  const cards = await page.evaluate(() => {
    const text = document.body.innerText;
    const hasWarning = text.includes('Cảnh báo') || text.includes('Nguyên tắc cộng đồng') || text.includes('vi phạm');
    const warningText = [];
    document.querySelectorAll('*').forEach(el => {
      if (el.innerText && (el.innerText.includes('Cảnh báo') || el.innerText.includes('Nguyên tắc cộng đồng')) && el.children.length === 0) {
        warningText.push(el.innerText);
      }
    });
    return { hasWarning, warningText };
  });

  console.log('CARDS:', JSON.stringify(cards, null, 2));
  await ctx.close();
})();
