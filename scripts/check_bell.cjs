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

  // Find bell / alerts icon
  const icons = await page.evaluate(() => {
    return [...document.querySelectorAll('ytcp-icon-button, button, [role="button"]')].filter(e => {
      const r = e.getBoundingClientRect();
      return r.y < 100 && r.x > 1000 && r.width > 0;
    }).map(e => ({ tag: e.tagName, id: e.id, aria: e.getAttribute('aria-label'), x: Math.round(e.getBoundingClientRect().x), y: Math.round(e.getBoundingClientRect().y) }));
  });
  console.log('TOP RIGHT BUTTONS:', JSON.stringify(icons));

  // Click notification bell if found
  const bell = icons.find(i => (i.aria || '').toLowerCase().includes('thông báo') || (i.id || '').includes('notif'));
  if (bell) {
    await page.mouse.click(bell.x + 15, bell.y + 15);
    await page.waitForTimeout(4000);
    await page.screenshot({ path: 'tmp/bell_open.png' });
    const txt = await page.evaluate(() => {
      return [...document.querySelectorAll('tp-yt-iron-dropdown, ytcp-notification-dialog, ytcp-popup-container')].map(e => e.innerText).join('\n');
    });
    console.log('BELL TEXT:\n', txt.slice(0, 1500));
  }

  // Also check "Số lượng video bị gỡ" or filter in Content
  await page.goto(`https://studio.youtube.com/channel/${CH.channel_id}/videos/upload`, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(6000);
  // Check if there are multiple pages or a "Filter" for restrictions
  const filterInfo = await page.evaluate(() => document.body.innerText.slice(0, 800));
  console.log('UPLOAD PAGE TOP:', filterInfo.slice(0, 500));

  await ctx.close();
})();
