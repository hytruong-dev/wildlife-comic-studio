const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const CH = JSON.parse(fs.readFileSync(path.join(ROOT, 'config/channel.json'), 'utf8'));
const ID = 'I_Th6_Vfrmg';
const NEW_TITLE = '[TẬP ĐẶC BIỆT] 10 Quái Kiệt Thi Đấu 8 Vòng Sinh Tồn: Ai Lên Ngôi Vô Địch?';

(async () => {
  const ctx = await chromium.launchPersistentContext(CH.chrome_profile, {
    headless: false, channel: 'chrome', viewport: { width: 1500, height: 900 },
    args: ['--disable-blink-features=AutomationControlled'],
  });
  const page = ctx.pages()[0] || await ctx.newPage();
  try {
    console.log(`Navigating to /video/${ID}/edit to update title...`);
    await page.goto(`https://studio.youtube.com/video/${ID}/edit`, { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(6000);

    const titleBox = page.locator('#title-textarea #textbox, ytcp-social-suggestions-textbox #textbox').first();
    await titleBox.click();
    await page.keyboard.press('Control+A');
    await page.keyboard.press('Backspace');
    await titleBox.pressSequentially(NEW_TITLE, { delay: 10 });
    await page.waitForTimeout(1500);

    const saveBtn = page.locator('#save, ytcp-button#save').first();
    const disabled = await saveBtn.getAttribute('aria-disabled');
    console.log('Save button disabled:', disabled);
    if (disabled !== 'true') {
      await saveBtn.click({ timeout: 10000 });
      await page.waitForTimeout(4000);
      console.log('Title updated and saved successfully!');
    }

    const snapDir = path.join(ROOT, 'projects/mega-01-dai-hoi-sinh-ton/renders/snapshots');
    await page.screenshot({ path: path.join(snapDir, 'title_updated_studio.png') });
    console.log('Screenshot saved to title_updated_studio.png');
  } catch (e) {
    console.error('Error:', e.message);
  } finally {
    await ctx.close();
  }
})();
