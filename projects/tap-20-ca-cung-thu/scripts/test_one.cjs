const { chromium } = require('playwright');

(async () => {
  const profile = 'C:\\Users\\PC\\AppData\\Local\\ms-playwright-mcp\\mcp-chrome-d9065a0';
  const ctx = await chromium.launchPersistentContext(profile, {
    headless: false, channel: 'chrome', viewport: { width: 1400, height: 900 }
  });
  const page = ctx.pages()[0] || await ctx.newPage();
  await page.goto('https://gemini.google.com/u/0/app', { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(4000);

  const prompt = 'Vẽ hình ảnh minh họa phong cách hoạt hình comic 2D bảng trắng trên nền trắng tinh khiết tỉ lệ 16:9: Một chú Cá Cung Thủ hoạt hình vảy bạc ánh kim sọc đen, đội mũ beret đen và kính ngắm một mắt viền đỏ, đang đứng hiên ngang trên một bục vinh quang màu vàng rực rỡ, vẻ mặt tự hào kiêu hãnh. Nền trắng hoàn toàn, không có chữ, không có số, không watermark.';
  console.log('Sending test prompt...');

  const box = page.locator('rich-textarea .ql-editor, div[contenteditable="true"][role="textbox"]').first();
  await box.waitFor({ timeout: 30000 });
  await box.click();
  await page.evaluate((t) => {
    const el = document.querySelector('rich-textarea .ql-editor') || document.querySelector('div[contenteditable="true"][role="textbox"]');
    el.focus(); document.execCommand('insertText', false, t);
  }, prompt);
  await page.waitForTimeout(600);
  await page.keyboard.press('Enter');

  for (let i = 0; i < 20; i++) {
    await page.waitForTimeout(2000);
    const info = await page.evaluate(() => {
      const rs = [...document.querySelectorAll('model-response')];
      if (!rs.length) return { count: 0 };
      const last = rs.at(-1);
      const imgs = [...last.querySelectorAll('img')].map(x => ({ w: x.naturalWidth, h: x.naturalHeight }));
      return { count: rs.length, text: (last.innerText || '').slice(0, 300), imgs };
    });
    console.log(`[step ${i}]`, JSON.stringify(info));
    if (info.imgs && info.imgs.some(x => x.w > 300)) {
      console.log('SUCCESS! Image found!');
      break;
    }
  }

  await ctx.close();
})();
