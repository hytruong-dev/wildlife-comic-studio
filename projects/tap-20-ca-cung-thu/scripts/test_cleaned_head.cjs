const { chromium } = require('playwright');
const fs = require('fs');

(async () => {
  const profile = 'C:\\Users\\PC\\AppData\\Local\\ms-playwright-mcp\\mcp-chrome-d9065a0';
  const ctx = await chromium.launchPersistentContext(profile, {
    headless: false, channel: 'chrome', viewport: { width: 1400, height: 900 }
  });
  const page = ctx.pages()[0] || await ctx.newPage();
  await page.goto('https://gemini.google.com/u/0/app', { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(3000);

  const head = 'Tạo hình ảnh (cảnh 7/67 của video YouTube về Cá Cung Thủ). QUY CHUẨN CHUNG: tỉ lệ NGANG 16:9; phong cách tranh minh họa hoạt hình comic 2D vẽ tay kiểu whiteboard explainer, nét mực đen đậm sắc nét, tô màu phẳng tươi sáng, biểu cảm hoạt hình hài hước cường điệu, thân thiện với trẻ em; NỀN TRẮNG TINH hoàn toàn, không khung viền, KHÔNG chữ, không số, không logo; chủ thể nằm gọn trong khung, chừa lề trắng. NHÂN VẬT CHÍNH cố định: chú Cá Cung Thủ hoạt hình màu bạc ánh kim sọc đen thẳng đứng, đôi mắt to lồi màu vàng rực rỡ đặc trưng, đầu đội một chiếc mũ beret màu đen kèm kính ngắm một mắt viền đỏ ngộ nghĩnh. ';
  const prompt = head + 'Bố cục: Bục vinh quang màu vàng rực rỡ, chú Cá Cung Thủ hoạt hình vảy bạc ánh kim sọc đen đội mũ beret đen và kính ngắm một mắt viền đỏ đứng hiên ngang trang nghiêm, vây trước chắp tay đầy kiêu hãnh.';

  console.log('Sending test prompt with cleaned head...');
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
    console.log(`[step ${i}]`, JSON.stringify(info));
    if (info && info.ok) {
      console.log(`SUCCESS: ${info.w}x${info.h}`);
      break;
    }
    if (info && info.txt && (info.txt.includes('không tạo được') || info.txt.includes('bên thứ ba'))) {
      console.log(`REFUSED: ${info.txt}`);
      break;
    }
  }

  await ctx.close();
})();
