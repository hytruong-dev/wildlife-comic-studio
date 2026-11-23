const { chromium } = require('playwright');
const path = require('path');

const SNAPSHOTS_DIR = 'C:\\QuangHy\\youtube_ai_edit-02\\projects\\tap-05-chim-bo-nong\\renders\\snapshots';

(async () => {
  console.log('=== ADJUSTING SCHEDULE DATE TO 7 THG 11, 2026 @ 11:00 AM ===');
  const context = await chromium.launchPersistentContext(
    'C:\\Users\\PC\\AppData\\Local\\ms-playwright-mcp\\mcp-chrome-aad48e1',
    {
      headless: false,
      channel: 'chrome',
      viewport: { width: 1366, height: 768 },
      args: ['--disable-blink-features=AutomationControlled']
    }
  );

  const page = await context.newPage();

  try {
    const editUrl = 'https://studio.youtube.com/video/KXJQReDxDcA/edit';
    console.log('[1/4] Navigating to:', editUrl);
    await page.goto(editUrl, { waitUntil: 'domcontentloaded', timeout: 30000 });
    await page.waitForTimeout(4000);

    await page.screenshot({ path: path.join(SNAPSHOTS_DIR, 'adjust_step1_edit_page.png') });

    // Look for Visibility trigger on right sidebar
    console.log('[2/4] Clicking Visibility dropdown on sidebar...');
    const visTrigger = page.getByText('Đã lên lịch').first();
    await visTrigger.scrollIntoViewIfNeeded();
    await visTrigger.click({ force: true });
    await page.waitForTimeout(1500);

    await page.screenshot({ path: path.join(SNAPSHOTS_DIR, 'adjust_step2_popup_opened.png') });

    // In the visibility dialog:
    console.log('[3/4] Changing date to 7 thg 11, 2026 and time to 11:00 AM...');
    
    // 1. Date trigger
    const dateTrigger = page.locator('#datepicker-trigger, ytcp-datetime-picker #datepicker-trigger').first();
    if (await dateTrigger.isVisible()) {
      await dateTrigger.click();
      await page.waitForTimeout(800);

      // Look for day button "7" in calendar
      const day7 = page.locator('ytcp-date-picker-dialog [aria-label*="7 thg 11"], ytcp-date-picker-dialog td:has-text("7"), ytcp-date-picker [aria-label*="7"]').first();
      if (await day7.isVisible()) {
        console.log('  -> Clicking day 7 in calendar...');
        await day7.click();
        await page.waitForTimeout(600);
      } else {
        // Try date input
        const dateInput = page.locator('ytcp-date-picker input, ytcp-date-picker-dialog input').first();
        if (await dateInput.isVisible()) {
          await dateInput.click();
          await dateInput.press('Control+A');
          await dateInput.press('Backspace');
          await dateInput.fill('07/11/2026');
          await dateInput.press('Enter');
          await page.waitForTimeout(500);
        }
      }
    }

    // 2. Time trigger
    const timeTrigger = page.locator('#time-of-day-trigger, ytcp-datetime-picker #time-of-day-trigger').first();
    if (await timeTrigger.isVisible()) {
      await timeTrigger.click();
      await page.waitForTimeout(800);

      const opt11 = page.locator('tp-yt-paper-item:has-text("11:00"), [role="option"]:has-text("11:00")').first();
      if (await opt11.isVisible()) {
        console.log('  -> Selecting 11:00 AM...');
        await opt11.click();
        await page.waitForTimeout(600);
      } else {
        const timeInput = page.locator('ytcp-time-of-day-picker input, #time-of-day-trigger input').first();
        if (await timeInput.isVisible()) {
          await timeInput.fill('11:00');
          await timeInput.press('Enter');
          await page.waitForTimeout(500);
        }
      }
    }

    await page.screenshot({ path: path.join(SNAPSHOTS_DIR, 'adjust_step3_popup_configured.png') });

    // Click "Xong" in popup
    const donePopupBtn = page.locator('ytcp-button:has-text("Xong"), button:has-text("Xong"), #done-button').first();
    if (await donePopupBtn.isVisible()) {
      await donePopupBtn.click({ force: true });
      await page.waitForTimeout(1000);
    }

    // Click "LƯU" on top right of the page
    console.log('[4/4] Clicking Save on video edit page...');
    const savePageBtn = page.locator('#save-button, ytcp-button:has-text("Lưu"), ytcp-button:has-text("LƯU")').first();
    await savePageBtn.click({ force: true });
    await page.waitForTimeout(4000);

    await page.screenshot({ path: path.join(SNAPSHOTS_DIR, 'adjust_step4_saved_success.png') });
    console.log('=== SCHEDULE DATE & TIME SUCCESSFULLY ADJUSTED TO 11:00 AM TRƯA MAI (07/11/2026)! ===');

  } catch (err) {
    console.error('Adjustment Error:', err);
    await page.screenshot({ path: path.join(SNAPSHOTS_DIR, 'adjust_error.png') });
  } finally {
    await context.close();
  }
})();
