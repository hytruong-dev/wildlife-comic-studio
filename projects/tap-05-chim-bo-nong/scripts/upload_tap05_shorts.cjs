/**
 * YouTube Studio Shorts Uploader & Scheduler for Episode 5: Chim Bồ Nông
 * Schedule time: 11:00 AM (07/11/2026) - synchronized with Main Video
 */

const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const SNAPSHOTS_DIR = path.resolve(__dirname, '../renders/snapshots');
if (!fs.existsSync(SNAPSHOTS_DIR)) {
  fs.mkdirSync(SNAPSHOTS_DIR, { recursive: true });
}

const VIDEO_PATH = 'C:\\Users\\PC\\.playwright-mcp\\tap05_chim_bo_nong_shorts.mp4';
const SHORTS_TITLE = 'Kẻ Đòi Nuốt Cả Thế Giới: Kẹp Thử Capybara & Túi 13L Nước! 😱 #shorts #chimbonong #vechuyenhoangda';
const SHORTS_DESCRIPTION = `Chiếc mỏ tham lam bậc nhất giới động vật: Thấy cái gì cử động là há mỏ kẹp thử, từ Capybara béo tròn đến chim bồ câu! Túi da phình to 13 lít nước khiến nó đứng đơ như tượng không thể cất cánh!

👉 Xem ngay bản FULL chi tiết giải mã 4 Dị Biệt chấn động của Chim Bồ Nông trên kênh Vẽ Chuyện Hoang Dã: https://youtu.be/KXJQReDxDcA

#shorts #chimbonong #pelican #vechuyenhoangda #thegioidongvat #dongvatkydi #capybara #edutainment`;

const SHORTS_TAGS = 'shorts, chim bồ nông, chim bo nong, pelican, capybara, bồ nông nuốt capybara, mỏ chim bồ nông, vẽ chuyện hoang dã, ve chuyen hoang da, thế giới động vật, động vật kỳ lạ, whiteboard animation, edutainment';

(async () => {
  console.log('=== STARTING YOUTUBE STUDIO SHORTS UPLOAD & SCHEDULE ===');
  console.log('Video Path:', VIDEO_PATH);
  console.log('Title:', SHORTS_TITLE);

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
    console.log('[Step 1/5] Navigating to YouTube Studio Upload dialog...');
    await page.goto('https://studio.youtube.com/channel/UCMX7XBHXoiq_kWIUo73n1Vw/videos/upload?d=ud', {
      waitUntil: 'domcontentloaded',
      timeout: 30000
    });
    await page.waitForTimeout(4000);

    const dialog = page.locator('ytcp-uploads-dialog').first();
    const fileInput = dialog.locator('input[type="file"]').first();

    console.log('[Step 2/5] Uploading Shorts Video File...');
    await fileInput.setInputFiles(VIDEO_PATH);
    await page.waitForTimeout(6000);

    console.log('[Step 3/5] Setting Details (Title, Description, Tags, Audience)...');
    
    // Set Title
    await page.evaluate((title) => {
      const titleBox = document.querySelector('#title-textarea #textbox, ytcp-social-suggestions-textbox[aria-label*="tiêu đề"] #textbox');
      if (titleBox) {
        titleBox.focus();
        titleBox.innerText = title;
        titleBox.dispatchEvent(new Event('input', { bubbles: true }));
        titleBox.dispatchEvent(new Event('change', { bubbles: true }));
      }
    }, SHORTS_TITLE);
    await page.waitForTimeout(1000);

    // Set Description
    await page.evaluate((desc) => {
      const descBox = document.querySelector('#description-textarea #textbox, ytcp-social-suggestions-textbox[aria-label*="nội dung"] #textbox, #description-container #textbox');
      if (descBox) {
        descBox.focus();
        descBox.innerText = desc;
        descBox.dispatchEvent(new Event('input', { bubbles: true }));
        descBox.dispatchEvent(new Event('change', { bubbles: true }));
      }
    }, SHORTS_DESCRIPTION);
    await page.waitForTimeout(1000);

    // Audience: Not made for kids
    await page.evaluate(() => {
      const notForKids = document.querySelector('tp-yt-paper-radio-button[name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]');
      if (notForKids) notForKids.click();
    });
    await page.waitForTimeout(1000);

    // Expand Show More (Hiện thêm)
    await page.evaluate(() => {
      const showMoreBtn = document.querySelector('#toggle-button, ytcp-button#toggle-button');
      if (showMoreBtn) showMoreBtn.click();
    });
    await page.waitForTimeout(1200);

    // Altered content: NO
    await page.evaluate(() => {
      const alteredNo = document.querySelector('tp-yt-paper-radio-button[name="ALTERED_CONTENT_NO"]');
      if (alteredNo) alteredNo.click();
    });
    await page.waitForTimeout(1000);

    // Tags
    await page.evaluate((tags) => {
      const tagInput = document.querySelector('ytcp-form-input-container#tags-container input, #tags-container #text-input');
      if (tagInput) {
        tagInput.focus();
        tagInput.value = tags;
        tagInput.dispatchEvent(new Event('input', { bubbles: true }));
        tagInput.dispatchEvent(new KeyboardEvent('keydown', { key: 'Enter', code: 'Enter', keyCode: 13, which: 13, bubbles: true }));
        tagInput.dispatchEvent(new KeyboardEvent('keyup', { key: 'Enter', code: 'Enter', keyCode: 13, which: 13, bubbles: true }));
      }
    }, SHORTS_TAGS);
    await page.waitForTimeout(2000);

    await page.screenshot({ path: path.join(SNAPSHOTS_DIR, 'shorts_upload_step1_details.png') });

    // Step 1 -> Step 2
    console.log('[Step 4/5] Navigating through wizard steps...');
    const nextBtn = dialog.locator('#next-button');
    await nextBtn.click();
    await page.waitForTimeout(2500);

    // Step 2 (Video Elements) - Related video linking
    try {
      console.log('  -> Attempting to link Related Video (Bản dài tập 5)...');
      await page.evaluate(() => {
        const relatedRow = Array.from(document.querySelectorAll('ytcp-video-metadata-editor-side-panel, ytcp-video-metadata-side-panel-row, ytcp-button')).find(el => el.innerText && el.innerText.includes('Video liên quan'));
        if (relatedRow) {
          const btn = relatedRow.querySelector('button, ytcp-button') || relatedRow;
          btn.click();
        }
      });
      await page.waitForTimeout(1500);
      
      // Select the first video (which is Ep 5 Longform)
      await page.evaluate(() => {
        const videoItems = document.querySelectorAll('ytcp-entity-card, ytcp-video-row');
        if (videoItems.length > 0) {
          videoItems[0].click();
        }
      });
      await page.waitForTimeout(1000);
    } catch (e) {
      console.log('  (Related video optional notice):', e.message);
    }

    // Step 2 -> Step 3
    await nextBtn.click();
    await page.waitForTimeout(2500);

    // Step 3 -> Step 4
    await nextBtn.click();
    await page.waitForTimeout(3000);

    console.log('[Step 5/5] Setting Schedule for 11:00 AM (07/11/2026)...');
    
    // Open Schedule section
    await page.evaluate(() => {
      const scheduleContainer = document.querySelector('#second-container, #second-container-expand-button');
      if (scheduleContainer) {
        scheduleContainer.click();
      } else {
        const schedRadio = document.querySelector('tp-yt-paper-radio-button[name="SCHEDULE"], #schedule-radio-button');
        if (schedRadio) schedRadio.click();
      }
    });
    await page.waitForTimeout(2000);

    // Ensure Date is 7 thg 11, 2026
    await page.evaluate(async () => {
      const trigger = document.querySelector('#datepicker-trigger');
      if (trigger) {
        trigger.click();
        await new Promise(r => setTimeout(r, 600));
        const dialog = document.querySelector('ytcp-date-picker tp-yt-paper-dialog');
        if (dialog) {
          const months = Array.from(dialog.querySelectorAll('.calendar-month'));
          let targetMonth = null;
          for (const m of months) {
            if (m.innerText.includes('11') && m.innerText.includes('2026')) {
              targetMonth = m.parentElement;
              break;
            }
          }
          const scope = targetMonth || dialog;
          const spans = Array.from(scope.querySelectorAll('span')).filter(s => s.innerText.trim() === '7');
          if (spans.length > 0) spans[0].click();
        }
      }
    });
    await page.waitForTimeout(1500);

    // Set Time to 11:00
    await page.evaluate(async () => {
      const timeInput = document.querySelector('ytcp-datetime-picker #textbox input');
      if (timeInput) {
        timeInput.click();
        await new Promise(r => setTimeout(r, 800));
        const opt = Array.from(document.querySelectorAll('tp-yt-paper-item, [role="option"]')).find(el => el.innerText.trim() === '11:00');
        if (opt) {
          opt.click();
        } else {
          timeInput.value = '11:00';
          timeInput.dispatchEvent(new Event('input', { bubbles: true }));
          timeInput.dispatchEvent(new Event('change', { bubbles: true }));
        }
      }
    });
    await page.waitForTimeout(1500);

    await page.screenshot({ path: path.join(SNAPSHOTS_DIR, 'shorts_upload_step4_configured.png') });

    // Click "Lên lịch" (#done-button)
    console.log('  -> Clicking Schedule (Lên lịch) button...');
    const doneBtn = dialog.locator('#done-button');
    await doneBtn.waitFor({ state: 'visible', timeout: 10000 });
    await doneBtn.click();
    await page.waitForTimeout(5000);

    // Get Video URL
    let videoUrl = null;
    try {
      const linkEl = dialog.locator('a.ytcp-video-info, a[href*="youtu.be"], a[href*="youtube.com/shorts"]').first();
      if (await linkEl.isVisible()) {
        videoUrl = await linkEl.getAttribute('href');
      }
    } catch (_) {}

    await page.screenshot({ path: path.join(SNAPSHOTS_DIR, 'shorts_upload_scheduled_success.png') });
    console.log('=== SHORTS SCHEDULED SUCCESSFULLY! ===');
    console.log('Shorts Video URL:', videoUrl || 'In Studio');

  } catch (err) {
    console.error('Shorts upload error:', err);
    await page.screenshot({ path: path.join(SNAPSHOTS_DIR, 'shorts_upload_error.png') });
  } finally {
    await context.close();
  }
})();
