const { chromium } = require('playwright');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');
const CH = JSON.parse(require('fs').readFileSync(path.join(ROOT, 'config/channel.json'), 'utf8'));

(async () => {
  const ctx = await chromium.launchPersistentContext(CH.chrome_profile, {
    headless: false, channel: 'chrome', viewport: { width: 1500, height: 900 },
    args: ['--disable-blink-features=AutomationControlled'],
  });
  const page = ctx.pages()[0] || await ctx.newPage();
  try {
    await page.goto(`https://studio.youtube.com/video/I_Th6_Vfrmg/edit`, { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(6000);
    const btns = await page.evaluate(() => {
      return [...document.querySelectorAll('ytcp-button, button, #save')]
        .map(b => ({
          tag: b.tagName,
          id: b.id,
          text: (b.innerText || '').trim(),
          aria: b.getAttribute('aria-label'),
          disabled: b.getAttribute('aria-disabled'),
          rect: b.getBoundingClientRect()
        }))
        .filter(b => b.text.includes('Lưu') || (b.id && b.id.includes('save')));
    });
    console.log('Save buttons found:', JSON.stringify(btns, null, 2));
  } finally {
    await ctx.close();
  }
})();
