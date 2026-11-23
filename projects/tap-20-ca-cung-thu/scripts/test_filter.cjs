const { chromium } = require('playwright');
const fs = require('fs');

(async () => {
  const profile = 'C:\\Users\\PC\\AppData\\Local\\ms-playwright-mcp\\mcp-chrome-d9065a0';
  const ctx = await chromium.launchPersistentContext(profile, {
    headless: false, channel: 'chrome', viewport: { width: 1400, height: 900 }
  });
  const page = ctx.pages()[0] || await ctx.newPage();
  await page.goto('https://gemini.google.com/u/0/app', { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(4000);

  const testPrompts = [
    // Variant 1: No "Lời thoại"
    'HÌNH L07 (16:9 ngang, cùng quy chuẩn comic 2D whiteboard và cùng nhân vật chú Cá Cung Thủ sọc đen bạc, đội mũ beret đen và kính ngắm một mắt viền đỏ; nền trắng tinh hoàn toàn, KHÔNG chữ, không số, không logo). Bố cục: Bục danh dự quân sự bằng vàng có hình huy hiệu sao, chú Cá Cung Thủ vảy bạc sọc đen đội mũ beret đen và kính ngắm xạ thủ viền đỏ đứng trên bục danh dự trang nghiêm, vây trước chắp tay đầy khí phách, kính ngắm laser phát ánh sáng đỏ kiêu hãnh.',
    // Variant 2: Cleaned
    'Vẽ hình ảnh minh họa 2D comic whiteboard tỉ lệ 16:9 trên nền trắng tinh khiết: Bục danh dự màu vàng rực rỡ, chú Cá Cung Thủ hoạt hình vảy bạc sọc đen đội mũ beret đen và kính ngắm một mắt viền đỏ đứng hiên ngang trang nghiêm, vây trước chắp tay kiêu hãnh. Nền trắng hoàn toàn, không chữ, không số, không logo.',
  ];

  for (let idx = 0; idx < testPrompts.length; idx++) {
    console.log(`\n--- Testing Variant ${idx + 1} ---`);
    const box = page.locator('rich-textarea .ql-editor, div[contenteditable="true"][role="textbox"]').first();
    await box.waitFor({ timeout: 30000 });
    await box.click();
    await page.evaluate((t) => {
      const el = document.querySelector('rich-textarea .ql-editor') || document.querySelector('div[contenteditable="true"][role="textbox"]');
      el.focus(); document.execCommand('insertText', false, t);
    }, testPrompts[idx]);
    await page.waitForTimeout(600);
    await page.keyboard.press('Enter');

    for (let i = 0; i < 15; i++) {
      await page.waitForTimeout(2000);
      const info = await page.evaluate(() => {
        const rs = [...document.querySelectorAll('model-response')];
        if (!rs.length) return null;
        const last = rs.at(-1);
        const img = [...last.querySelectorAll('img')].find(x => x.naturalWidth > 300);
        if (img) return { ok: true, w: img.naturalWidth, h: img.naturalHeight };
        const txt = (last.innerText || '').slice(0, 200);
        return { ok: false, txt };
      });
      if (info && info.ok) {
        console.log(`Variant ${idx + 1} SUCCESS: ${info.w}x${info.h}`);
        break;
      }
      if (info && info.txt && info.txt.includes('không tạo được')) {
        console.log(`Variant ${idx + 1} REFUSED: ${info.txt}`);
        break;
      }
    }
  }

  await ctx.close();
})();
