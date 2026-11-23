const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const CH = JSON.parse(fs.readFileSync('config/channel.json', 'utf8'));
const STAGE = path.join(require('os').homedir(), '.playwright-mcp');
const staged = path.join(STAGE, 'tap-20-ca-cung-thu_long.mp4');

(async () => {
  const ctx = await chromium.launchPersistentContext(CH.chrome_profile, {
    headless: false, channel: 'chrome', viewport: { width: 1500, height: 900 },
    args: ['--disable-blink-features=AutomationControlled']
  });
  const page = ctx.pages()[0] || await ctx.newPage();
  await page.goto(`https://studio.youtube.com/channel/${CH.channel_id}/videos/upload?d=ud`, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(4000);
  const dlg = page.locator('ytcp-uploads-dialog').first();
  await dlg.locator('input[type="file"]').first().setInputFiles(staged);
  await dlg.locator('#title-textarea #textbox').first().waitFor({ timeout: 120000 });

  for (let s = 5; s <= 35; s += 10) {
    await page.waitForTimeout(10000);
    await page.screenshot({ path: `tmp/scrim_t${s}.png` });
    const dump = await page.evaluate(() => {
      function walk(node, out = []) {
        if (!node) return out;
        if (node.nodeType === 1) {
          if (node.innerText && /vi phạm|cảnh cáo|Thực hiện hành động|hạn mức|tối đa/i.test(node.innerText)) {
            const r = node.getBoundingClientRect();
            if (r.width > 0 && node.innerText.length < 1500) {
              out.push(node.tagName + '#' + node.id + '.' + (node.className || '').toString().slice(0, 30) + ` [${Math.round(r.x)},${Math.round(r.y)},${Math.round(r.width)}x${Math.round(r.height)}]: ` + node.innerText.replace(/\s+/g, ' ').slice(0, 200));
            }
          }
          if (node.shadowRoot) walk(node.shadowRoot, out);
        }
        for (const c of node.children || []) walk(c, out);
        return out;
      }
      const scrim = document.querySelector('ytcp-uploads-dialog .dialog-scrim');
      const scrimCss = scrim ? { disp: getComputedStyle(scrim).display, op: getComputedStyle(scrim).opacity, pe: getComputedStyle(scrim).pointerEvents, vis: getComputedStyle(scrim).visibility } : null;
      return { scrimCss, hits: walk(document.body).slice(-8) };
    });
    console.log(`t=${s}s:`, JSON.stringify(dump, null, 2));
  }

  await ctx.close();
})();
