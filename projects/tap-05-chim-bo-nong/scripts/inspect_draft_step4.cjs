const { chromium } = require('playwright');
const path = require('path');

const SNAPSHOTS_DIR = 'C:\\QuangHy\\youtube_ai_edit-02\\projects\\tap-05-chim-bo-nong\\renders\\snapshots';

(async () => {
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
    console.log('[1] Navigating to videos list...');
    await page.goto('https://studio.youtube.com/channel/UCMX7XBHXoiq_kWIUo73n1Vw/videos', {
      waitUntil: 'networkidle',
      timeout: 30000
    });
    await page.waitForTimeout(3000);

    // Find the draft row
    const editDraftBtn = page.locator('ytcp-button:has-text("Chỉnh sửa bản nháp"), button:has-text("Chỉnh sửa bản nháp"), ytcp-video-row:has-text("Chim Bồ Nông") #edit-draft-button, ytcp-video-row:has-text("Chim Bồ Nông") button').first();
    console.log('[2] Clicking Edit Draft...');
    if (await editDraftBtn.isVisible()) {
      await editDraftBtn.click();
    } else {
      // Click row directly
      const row = page.locator('ytcp-video-row:has-text("Chim Bồ Nông")').first();
      await row.click();
    }
    await page.waitForTimeout(3000);

    const dialog = page.locator('ytcp-uploads-dialog').first();
    console.log('Dialog visible:', await dialog.isVisible());

    // Loop click Next until we reach Visibility step
    for (let i = 0; i < 4; i++) {
      const step = await dialog.getAttribute('workflow-step');
      console.log(`Step iteration ${i}: workflow-step =`, step);
      if (step === 'PUBLISH' || step === 'VISIBILITY') {
        console.log('Reached Visibility/Publish step!');
        break;
      }
      const nextBtn = dialog.locator('#next-button button, #next-button, button:has-text("TIẾP THEO"), button:has-text("Tiếp theo")').first();
      if (await nextBtn.isVisible()) {
        await nextBtn.click({ force: true });
        await page.waitForTimeout(2000);
      }
    }

    await page.screenshot({ path: path.join(SNAPSHOTS_DIR, 'step4_visibility_screen.png') });

    // Inspect all buttons/radios on Step 4
    const scheduleHeaders = await dialog.locator('#schedule-section, #schedule-expand-button, [aria-label*="Lên lịch"], tp-yt-paper-radio-button, ytcp-button').all();
    console.log('Schedule elements found:', scheduleHeaders.length);
    for (let i = 0; i < Math.min(scheduleHeaders.length, 10); i++) {
      const txt = (await scheduleHeaders[i].innerText().catch(() => '')).trim();
      const id = await scheduleHeaders[i].getAttribute('id').catch(() => '');
      console.log(`  El ${i}: id="${id}", text="${txt}"`);
    }

  } catch (err) {
    console.error('Error:', err);
  } finally {
    await context.close();
  }
})();
