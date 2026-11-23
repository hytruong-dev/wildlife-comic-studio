const { chromium } = require('playwright');

(async () => {
  const profile = 'C:\\Users\\PC\\AppData\\Local\\ms-playwright-mcp\\mcp-chrome-d9065a0';
  const ctx = await chromium.launchPersistentContext(profile, {
    headless: false, channel: 'chrome', viewport: { width: 1400, height: 900 }
  });
  const page = ctx.pages()[0] || await ctx.newPage();

  async function test(name, prompt) {
    await page.goto('https://gemini.google.com/u/0/app', { waitUntil: 'domcontentloaded', timeout: 60000 });
    await page.waitForTimeout(3000);
    console.log(`\n--- Testing ${name} ---`);
    const box = page.locator('rich-textarea .ql-editor, div[contenteditable="true"][role="textbox"]').first();
    await box.waitFor({ timeout: 30000 });
    await box.click();
    await page.evaluate((t) => {
      const el = document.querySelector('rich-textarea .ql-editor') || document.querySelector('div[contenteditable="true"][role="textbox"]');
      el.focus(); document.execCommand('insertText', false, t);
    }, prompt);
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
        console.log(`${name} SUCCESS: ${info.w}x${info.h}`);
        return true;
      }
      if (info && info.txt && (info.txt.includes('không tạo được') || info.txt.includes('bên thứ ba'))) {
        console.log(`${name} REFUSED: ${info.txt}`);
        return false;
      }
    }
  }

  // Test 1: exact prompt that worked earlier in test_one.cjs
  await test('Exact test_one', 'Vẽ hình ảnh minh họa phong cách hoạt hình comic 2D bảng trắng trên nền trắng tinh khiết tỉ lệ 16:9: Một chú Cá Cung Thủ hoạt hình vảy bạc ánh kim sọc đen, đội mũ beret đen và kính ngắm một mắt viền đỏ, đang đứng hiên ngang trên một bục vinh quang màu vàng rực rỡ, vẻ mặt tự hào kiêu hãnh. Nền trắng hoàn toàn, không có chữ, không có số, không watermark.');

  // Test 2: in English
  await test('English version', 'Clean 2D comic cartoon illustration on pure solid white background, 16:9: A cute cartoon archerfish with silver and black stripes, wearing a black beret with a red target scope visor, standing proudly on a glowing golden honor podium. Vibrant flat colors, bold outlines, no text, no letters, no numbers, no watermark.');

  await ctx.close();
})();
