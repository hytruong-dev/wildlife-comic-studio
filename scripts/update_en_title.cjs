const { chromium } = require('playwright');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');
const CH = JSON.parse(require('fs').readFileSync(path.join(ROOT, 'config/channel.json'), 'utf8'));
const ID = 'I_Th6_Vfrmg';
const NEW_EN_TITLE = '[SPECIAL] 10 Animal Champions In The Ultimate Survival Tournament: Who Wins?!';

(async () => {
  const ctx = await chromium.launchPersistentContext(CH.chrome_profile, {
    headless: false, channel: 'chrome', viewport: { width: 1500, height: 900 },
    args: ['--disable-blink-features=AutomationControlled'],
  });
  const page = ctx.pages()[0] || await ctx.newPage();
  try {
    await page.goto(`https://studio.youtube.com/video/${ID}/translations`, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await page.waitForTimeout(7000);
    const row = page.locator('ytgn-video-translation-row').filter({ hasText: /^\s*Tiếng Anh\s/ }).first();
    const cell = row.locator('#cell-container').nth(1);
    const box = await cell.boundingBox();
    await page.mouse.move(box.x + box.width / 2, box.y + box.height / 2);
    await page.waitForTimeout(1200);

    const b = await row.evaluate(e => {
      const x = [...e.querySelectorAll('#metadata-edit, #metadata-add, ytcp-button')].find(b => b.getBoundingClientRect().width > 0);
      if (!x) return null;
      const r = x.getBoundingClientRect();
      return [r.x + r.width / 2, r.y + r.height / 2];
    });
    if (b) {
      await page.mouse.click(b[0], b[1]);
      await page.waitForTimeout(4000);
      const dlg = page.locator('tp-yt-paper-dialog:visible').filter({ hasText: 'Bản dịch' }).last();
      const ta = dlg.locator('textarea');
      await ta.nth(1).fill(NEW_EN_TITLE);
      await page.waitForTimeout(1000);
      await dlg.locator('ytcp-button:has-text("Xuất bản")').first().click({ noWaitAfter: true });
      await page.waitForTimeout(4000);
      console.log('Updated English title successfully!');
    } else {
      console.log('Edit button for English translation not found.');
    }
  } finally {
    await ctx.close();
  }
})();
