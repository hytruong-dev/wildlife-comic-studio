const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const CH = JSON.parse(fs.readFileSync('config/channel.json', 'utf8'));
const STAGE = path.join(require('os').homedir(), '.playwright-mcp');
const srcFile = path.resolve('projects/tap-20-ca-cung-thu/renders/tap-20-ca-cung-thu_long.mp4');
const staged = path.join(STAGE, path.basename(srcFile));
fs.copyFileSync(srcFile, staged);

(async () => {
  const ctx = await chromium.launchPersistentContext(CH.chrome_profile, {
    headless: false, channel: 'chrome', viewport: { width: 1500, height: 900 },
    args: ['--disable-blink-features=AutomationControlled']
  });
  const page = ctx.pages()[0] || await ctx.newPage();
  await page.goto(`https://studio.youtube.com/channel/${CH.channel_id}/videos/upload?d=ud`, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(5000);
  const dlg = page.locator('ytcp-uploads-dialog').first();
  await dlg.locator('input[type="file"]').first().setInputFiles(staged);
  await dlg.locator('#title-textarea #textbox').first().waitFor({ timeout: 120000 });

  for (let s = 0; s < 15; s++) {
    await page.waitForTimeout(1000);
    const info = await page.evaluate(() => {
      const scrim = document.querySelector('ytcp-uploads-dialog .dialog-scrim');
      const scrimVis = scrim ? (getComputedStyle(scrim).display !== 'none' && scrim.getBoundingClientRect().width > 0) : false;
      const matches = [...document.querySelectorAll('*')].filter(e =>
        e.innerText && e.innerText.includes('Video này vi phạm Nguyên tắc cộng đồng') && e.getBoundingClientRect().width > 0
      ).map(e => e.tagName + '#' + e.id + '.' + (e.className || '').toString().slice(0, 40));
      return { scrimVis, matches: matches.slice(-6) };
    });
    console.log(`t=${s + 1}s:`, JSON.stringify(info));
    if (info.matches.length > 0) {
      const btns = await page.evaluate(() => {
        return [...document.querySelectorAll('ytcp-button, button')].filter(b =>
          b.getBoundingClientRect().width > 0 && /Hủy|Thực hiện hành động/.test(b.innerText || '')
        ).map(b => {
          const r = b.getBoundingClientRect();
          return { tag: b.tagName, id: b.id, text: b.innerText.trim(), x: Math.round(r.x + r.width / 2), y: Math.round(r.y + r.height / 2) };
        });
      });
      console.log('BUTTONS FOUND:', JSON.stringify(btns));
      const cancelBtn = btns.find(b => b.text === 'Hủy');
      if (cancelBtn) {
        await page.mouse.click(cancelBtn.x, cancelBtn.y);
        await page.waitForTimeout(3000);
        await page.screenshot({ path: 'tmp/after_cancel_warn.png' });
        const afterScrim = await page.evaluate(() => {
          const scrim = document.querySelector('ytcp-uploads-dialog .dialog-scrim');
          return scrim ? (getComputedStyle(scrim).display !== 'none' && scrim.getBoundingClientRect().width > 0) : false;
        });
        console.log('AFTER CLICK HỦY -> scrimVis:', afterScrim);
      }
      break;
    }
  }
  await ctx.close();
})();
