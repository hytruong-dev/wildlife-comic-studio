const { chromium } = require('playwright');
const PROFILE = 'C:\\Users\\PC\\AppData\\Local\\ms-playwright-mcp\\mcp-chrome-aad48e1';
(async () => {
  const ctx = await chromium.launchPersistentContext(PROFILE, { headless: false, channel: 'chrome', viewport: { width: 1600, height: 1000 }, args: ['--disable-blink-features=AutomationControlled'] });
  const page = ctx.pages()[0] || await ctx.newPage();
  for (const id of ['HEjl0zaZSTQ', '0GLhSHMc16w']) {
    await page.goto(`https://studio.youtube.com/video/${id}/edit`, { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(9000);
    const vis = await page.locator('ytcp-video-metadata-visibility').first().innerText().catch(() => '?');
    const title = await page.locator('#title-textarea #textbox').first().innerText().catch(() => '?');
    console.log(id, '|', title.slice(0, 60), '|', vis.replace(/\s+/g, ' '));
  }
  await ctx.close();
})();
