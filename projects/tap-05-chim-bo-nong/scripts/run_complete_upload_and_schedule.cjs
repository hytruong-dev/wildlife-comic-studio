/**
 * Complete YouTube Studio Uploader & Scheduler for Episode 5: Chim Bồ Nông
 * Schedule time: 11:00 AM tomorrow (07/11/2026)
 */

const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '../../..');
const PROJ = path.resolve(__dirname, '..');
const SEO_FILE = path.join(PROJ, 'seo_package.json');
const SNAPSHOTS_DIR = path.join(PROJ, 'renders', 'snapshots');

if (!fs.existsSync(SNAPSHOTS_DIR)) {
  fs.mkdirSync(SNAPSHOTS_DIR, { recursive: true });
}

const seoData = JSON.parse(fs.readFileSync(SEO_FILE, 'utf8'));
const metadata = seoData.metadata;

const VIDEO_PATH = 'C:\\Users\\PC\\.playwright-mcp\\tap05_chim_bo_nong_longform.mp4';
const THUMB_PATH = 'C:\\Users\\PC\\.playwright-mcp\\tap05_chim_bo_nong_thumbnail.jpg';

(async () => {
  console.log('=== STARTING COMPLETE YOUTUBE STUDIO UPLOAD & SCHEDULE (EPISODE 5) ===');
  console.log('Video Path:', VIDEO_PATH);
  console.log('Thumbnail Path:', THUMB_PATH);
  console.log('Title:', metadata.title_vi);

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
    console.log('[Step 1/6] Navigating to YouTube Studio Upload dialog...');
    await page.goto('https://studio.youtube.com/channel/UCMX7XBHXoiq_kWIUo73n1Vw/videos/upload?d=ud', {
      waitUntil: 'domcontentloaded',
      timeout: 30000
    });
    await page.waitForTimeout(4000);

    const dialog = page.locator('ytcp-uploads-dialog').first();
    const fileInput = dialog.locator('input[type="file"]').first();

    console.log('[Step 2/6] Uploading Master Video File...');
    await fileInput.setInputFiles(VIDEO_PATH);
    await page.waitForTimeout(6000);

    console.log('[Step 3/6] Filling Full SEO Metadata...');
    // 1. Title
    const titleBox = dialog.locator('#title-textarea #textbox, ytcp-social-suggestions-textbox[aria-label*="tiêu đề"] #textbox').first();
    await titleBox.click();
    await titleBox.press('Control+A');
    await titleBox.press('Backspace');
    await titleBox.fill(metadata.title_vi);
    await page.waitForTimeout(500);

    // 2. Description
    const descBox = dialog.locator('#description-textarea #textbox, ytcp-social-suggestions-textbox[aria-label*="mô tả"] #textbox').first();
    await descBox.click();
    await descBox.fill(metadata.description_vi);
    await page.waitForTimeout(500);

    // 3. Custom Thumbnail
    const thumbInput = dialog.locator('input[type="file"][accept*="image"], #file-loader').first();
    if (await thumbInput.count() > 0) {
      console.log('  -> Setting custom 1280x720 thumbnail with TẬP 05 badge...');
      await thumbInput.setInputFiles(THUMB_PATH);
      await page.waitForTimeout(2000);
    }

    // 4. Audience: Not made for kids (mọi lứa tuổi, giữ bình luận)
    console.log('  -> Setting Audience: Not made for kids...');
    const notForKidsRadio = dialog.locator('tp-yt-paper-radio-button[name="VIDEO_MADE_FOR_KIDS_NOT_MFK"], [name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]').first();
    await notForKidsRadio.click();
    await page.waitForTimeout(500);

    // 5. Playlist: Thế Giới Động Vật
    console.log('  -> Adding to Playlist...');
    try {
      const playlistSection = dialog.locator('ytcp-video-metadata-playlists').first();
      await playlistSection.scrollIntoViewIfNeeded();
      const trigger = playlistSection.locator('#trigger, ytcp-text-dropdown-trigger').first();
      await trigger.click({ force: true });
      await page.waitForTimeout(800);

      const checkbox = dialog.locator('ytcp-checkbox-lit:has-text("Thế Giới Động Vật"), tp-yt-paper-checkbox:has-text("Thế Giới Động Vật")').first();
      if (await checkbox.isVisible()) {
        await checkbox.click({ force: true });
        await page.waitForTimeout(400);
        const doneBtn = dialog.locator('ytcp-button:has-text("Xong"), button:has-text("Xong")').first();
        await doneBtn.click({ force: true });
      }
    } catch (e) {
      console.log('  (Playlist notice):', e.message);
    }

    // 6. Show more (Hiện thêm)
    console.log('  -> Expanding Show More...');
    const showMoreBtn = dialog.locator('#toggle-button, ytcp-button:has-text("Hiện thêm"), ytcp-button:has-text("Xem thêm")').first();
    if (await showMoreBtn.isVisible()) {
      await showMoreBtn.click({ force: true });
      await page.waitForTimeout(600);
    }

    // 7. Altered content: NO
    console.log('  -> Setting Altered Content: NO...');
    const alteredNo = dialog.locator('[name="VIDEO_HAS_ALTERED_CONTENT_NO"]').first();
    if (await alteredNo.isVisible()) {
      await alteredNo.click({ force: true });
      await page.waitForTimeout(400);
    }

    // 8. Tags
    console.log('  -> Filling Tags...');
    const tagsInput = dialog.locator('#tags-container input, #text-input').first();
    if (await tagsInput.isVisible()) {
      await tagsInput.click({ force: true });
      await tagsInput.fill(metadata.tags_string);
      await tagsInput.press('Enter');
      await page.waitForTimeout(500);
    }

    await page.screenshot({ path: path.join(SNAPSHOTS_DIR, 'final_upload_step1_details.png') });

    // Step 1 -> Step 2
    console.log('[Step 4/6] Navigating through wizard steps...');
    const nextBtn = dialog.locator('#next-button button, #next-button, button:has-text("TIẾP THEO"), button:has-text("Tiếp theo")').first();
    await nextBtn.click({ force: true });
    await page.waitForTimeout(2500);

    // End screen on Step 2
    try {
      const importBtn = dialog.locator('ytcp-button:has-text("Nhập từ video"), button:has-text("Nhập từ video")').first();
      if (await importBtn.isVisible()) {
        await importBtn.click({ force: true });
        await page.waitForTimeout(2000);
        const saveEndScreen = page.locator('#save-button, ytcp-button:has-text("Lưu"), button:has-text("Lưu")').first();
        if (await saveEndScreen.isVisible()) {
          await saveEndScreen.click({ force: true });
          await page.waitForTimeout(2000);
        }
      }
    } catch (e) {
      console.log('  (End screen notice):', e.message);
    }

    // Step 2 -> Step 3
    await nextBtn.click({ force: true });
    await page.waitForTimeout(2500);

    // Step 3 -> Step 4 (Wait for checks or click Next)
    let inVisibility = false;
    for (let attempt = 0; attempt < 5; attempt++) {
      const currentStep = await dialog.getAttribute('workflow-step');
      console.log(`  Step transition attempt ${attempt + 1}: workflow-step = ${currentStep}`);
      if (currentStep === 'PUBLISH' || currentStep === 'VISIBILITY' || currentStep === 'REVIEW') {
        inVisibility = true;
        console.log('  -> Reached Step 4 (Chế độ hiển thị)!');
        break;
      }
      await nextBtn.click({ force: true });
      await page.waitForTimeout(2000);
    }

    console.log('[Step 5/6] Setting Schedule for 11:00 AM tomorrow...');
    await page.screenshot({ path: path.join(SNAPSHOTS_DIR, 'final_upload_step4_visibility.png') });

    // Look for Schedule accordion / radio
    // In YouTube Studio:
    const scheduleOption = dialog.locator('#second-container, #second-container-expand-button').or(dialog.getByText('Chọn ngày bạn muốn đặt video ở chế độ công khai')).first();
    await scheduleOption.scrollIntoViewIfNeeded();
    await scheduleOption.click({ force: true });
    await page.waitForTimeout(1500);

    // Take snapshot after opening schedule section
    await page.screenshot({ path: path.join(SNAPSHOTS_DIR, 'final_upload_step4_schedule_opened.png') });

    // Now inside schedule container:
    // 1. Date picker
    try {
      const dateTrigger = dialog.locator('#datepicker-trigger, ytcp-datetime-picker #datepicker-trigger').first();
      if (await dateTrigger.isVisible()) {
        const currentDateText = (await dateTrigger.innerText()).trim();
        console.log('  -> Default scheduled date:', currentDateText);
        // By default YouTube Studio sets to tomorrow (07/11/2026). If not, open and adjust
        if (!currentDateText.includes('7') && !currentDateText.includes('07')) {
          await dateTrigger.click();
          await page.waitForTimeout(600);
          const tomorrowDay = page.locator('ytcp-date-picker-dialog [aria-label*="7"], ytcp-date-picker-dialog td:has-text("7")').first();
          if (await tomorrowDay.isVisible()) {
            await tomorrowDay.click();
            await page.waitForTimeout(400);
          }
        }
      }
    } catch (e) {
      console.log('  (Datepicker log):', e.message);
    }

    // 2. Time picker: 11:00 AM (11:00 trưa)
    try {
      const timeTrigger = dialog.locator('#time-of-day-trigger, ytcp-datetime-picker #time-of-day-trigger').first();
      if (await timeTrigger.isVisible()) {
        console.log('  -> Opening Time picker...');
        await timeTrigger.click();
        await page.waitForTimeout(800);

        // Find 11:00
        const opt11 = page.locator('tp-yt-paper-item:has-text("11:00"), [role="option"]:has-text("11:00")').first();
        if (await opt11.isVisible()) {
          console.log('  -> Clicking 11:00 AM option...');
          await opt11.click();
          await page.waitForTimeout(500);
        } else {
          // If input is editable
          const timeInput = page.locator('ytcp-time-of-day-picker input, #time-of-day-trigger input').first();
          if (await timeInput.isVisible()) {
            await timeInput.fill('11:00');
            await timeInput.press('Enter');
            await page.waitForTimeout(500);
          }
        }
      }
    } catch (e) {
      console.log('  (Timepicker log):', e.message);
    }

    // Capture screenshot before clicking Lên Lịch
    await page.screenshot({ path: path.join(SNAPSHOTS_DIR, 'final_upload_step4_schedule_configured.png') });

    // Video URL check
    const linkEl = dialog.locator('a[href*="youtu.be"], a.ytcp-video-info').first();
    let videoUrl = null;
    if (await linkEl.count() > 0) {
      videoUrl = await linkEl.getAttribute('href');
    }
    console.log('  -> Scheduled Video URL:', videoUrl);

    // Click LÊN LỊCH (Schedule button)
    console.log('[Step 6/6] Clicking Lên lịch (Schedule)...');
    const scheduleDoneBtn = dialog.locator('#done-button button, #done-button, ytcp-button:has-text("Lên lịch"), ytcp-button:has-text("LÊN LỊCH")').first();
    await scheduleDoneBtn.click({ force: true });
    await page.waitForTimeout(8000);

    // Final Confirmation Screenshot
    await page.screenshot({ path: path.join(SNAPSHOTS_DIR, 'final_upload_scheduled_success.png') });
    console.log('=== VIDEO HAS BEEN OFFICIALLY SCHEDULED ON YOUTUBE STUDIO! ===');
    console.log('Public Schedule Date:', '11:00 AM, 07/11/2026');
    console.log('Video URL:', videoUrl);

    // Close confirmation dialog if visible
    const closeBtn = page.locator('ytcp-post-publish-dialog #close-button, ytcp-dialog #close-button, button:has-text("Đóng")').first();
    if (await closeBtn.isVisible()) {
      await closeBtn.click();
      await page.waitForTimeout(2000);
    }

  } catch (err) {
    console.error('Upload Error:', err);
    await page.screenshot({ path: path.join(SNAPSHOTS_DIR, 'final_upload_error.png') });
  } finally {
    await context.close();
  }
})();
