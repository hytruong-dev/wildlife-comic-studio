/**
 * Automated YouTube Studio Uploader & Scheduler for Episode 5: Chim Bồ Nông
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
  console.log('=== STARTING YOUTUBE STUDIO UPLOAD (EPISODE 5) ===');
  console.log('Video:', VIDEO_PATH);
  console.log('Thumb:', THUMB_PATH);
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
    console.log('[1/7] Navigating to YouTube Studio Upload page...');
    await page.goto('https://studio.youtube.com/channel/UCMX7XBHXoiq_kWIUo73n1Vw/videos/upload?d=ud', {
      waitUntil: 'networkidle',
      timeout: 30000
    });
    await page.waitForTimeout(3000);

    const dialog = page.locator('ytcp-uploads-dialog').first();
    const fileInput = dialog.locator('input[type="file"]').first();

    console.log('[2/7] Selecting video file for upload...');
    await fileInput.setInputFiles(VIDEO_PATH);
    await page.waitForTimeout(5000);

    console.log('[3/7] Filling Title, Description & Uploading Thumbnail...');
    // Title
    const titleBox = dialog.locator('#title-textarea #textbox, ytcp-social-suggestions-textbox[aria-label*="tiêu đề"] #textbox').first();
    await titleBox.click();
    await titleBox.press('Control+A');
    await titleBox.press('Backspace');
    await titleBox.fill(metadata.title_vi);
    await page.waitForTimeout(500);

    // Description
    const descBox = dialog.locator('#description-textarea #textbox, ytcp-social-suggestions-textbox[aria-label*="mô tả"] #textbox').first();
    await descBox.click();
    await descBox.fill(metadata.description_vi);
    await page.waitForTimeout(500);

    // Thumbnail
    const thumbInput = dialog.locator('input[type="file"][accept*="image"], #file-loader').first();
    if (await thumbInput.count() > 0) {
      console.log('  -> Setting custom thumbnail...');
      await thumbInput.setInputFiles(THUMB_PATH);
      await page.waitForTimeout(2000);
    }

    // Audience: Not made for kids
    console.log('  -> Setting Audience: Not made for kids (mọi lứa tuổi)...');
    const notForKidsRadio = dialog.locator('tp-yt-paper-radio-button[name="VIDEO_MADE_FOR_KIDS_NOT_MFK"], [name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]').first();
    await notForKidsRadio.click();
    await page.waitForTimeout(500);

    // Playlist
    console.log('  -> Adding to Playlist: Thế Giới Động Vật...');
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
      console.log('  (Playlist optional notice):', e.message);
    }

    // Show more (Hiện thêm)
    console.log('  -> Expanding Show More (Hiện thêm)...');
    const showMoreBtn = dialog.locator('#toggle-button, ytcp-button:has-text("Hiện thêm"), ytcp-button:has-text("Xem thêm")').first();
    if (await showMoreBtn.isVisible()) {
      await showMoreBtn.click({ force: true });
      await page.waitForTimeout(600);
    }

    // Altered content: NO
    console.log('  -> Setting Altered content: NO...');
    const alteredNo = dialog.locator('[name="VIDEO_HAS_ALTERED_CONTENT_NO"]').first();
    if (await alteredNo.isVisible()) {
      await alteredNo.click({ force: true });
      await page.waitForTimeout(400);
    }

    // Tags
    console.log('  -> Filling Tags...');
    const tagsInput = dialog.locator('#tags-container input, #text-input').first();
    if (await tagsInput.isVisible()) {
      await tagsInput.click({ force: true });
      await tagsInput.fill(metadata.tags_string);
      await tagsInput.press('Enter');
      await page.waitForTimeout(500);
    }

    // Screenshot Step 1 Details
    await page.screenshot({ path: path.join(SNAPSHOTS_DIR, 'upload_step1_details.png') });

    // Step 1 -> Step 2 (Video elements)
    console.log('[4/7] Moving to Step 2: Video elements...');
    const nextBtn1 = dialog.locator('#next-button button, #next-button').first();
    await nextBtn1.click({ force: true });
    await page.waitForTimeout(2000);

    // End screen: Import or add
    console.log('  -> Setting End Screen...');
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

    // Step 2 -> Step 3 (Checks)
    console.log('[5/7] Moving to Step 3: Checks...');
    const nextBtn2 = dialog.locator('#next-button button, #next-button').first();
    await nextBtn2.click({ force: true });
    await page.waitForTimeout(2000);

    // Step 3 -> Step 4 (Visibility / Schedule)
    console.log('[6/7] Moving to Step 4: Visibility & Scheduling (Hẹn giờ 11h trưa mai)...');
    const nextBtn3 = dialog.locator('#next-button button, #next-button').first();
    await nextBtn3.click({ force: true });
    await page.waitForTimeout(2500);

    // Click on Schedule (Lên lịch)
    console.log('  -> Selecting Schedule (Lên lịch)...');
    const scheduleRadio = dialog.locator('#schedule-radio-button, tp-yt-paper-radio-button[name="SCHEDULE"], [aria-label*="Lên lịch"]').first();
    await scheduleRadio.scrollIntoViewIfNeeded();
    await scheduleRadio.click({ force: true });
    await page.waitForTimeout(1000);

    // Date & Time picker
    // Set date to tomorrow
    console.log('  -> Setting Date and Time: 11:00 AM tomorrow...');
    try {
      // Find date trigger
      const dateTrigger = dialog.locator('#datepicker-trigger, ytcp-datetime-picker #datepicker-trigger').first();
      if (await dateTrigger.isVisible()) {
        await dateTrigger.click();
        await page.waitForTimeout(800);

        // Date input inside dialog
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

      // Find time trigger
      const timeTrigger = dialog.locator('#time-of-day-trigger, ytcp-datetime-picker #time-of-day-trigger').first();
      if (await timeTrigger.isVisible()) {
        await timeTrigger.click();
        await page.waitForTimeout(800);

        // Type 11:00 or select 11:00
        const timeInput = page.locator('ytcp-time-of-day-picker input, #time-of-day-trigger input').first();
        if (await timeInput.isVisible()) {
          await timeInput.fill('11:00');
          await timeInput.press('Enter');
        } else {
          // Look for 11:00 option
          const opt11 = page.locator('tp-yt-paper-item:has-text("11:00"), [role="option"]:has-text("11:00")').first();
          if (await opt11.isVisible()) {
            await opt11.click();
          }
        }
        await page.waitForTimeout(500);
      }
    } catch (e) {
      console.log('  (DatePicker notice):', e.message);
    }

    // Capture screenshot before clicking Schedule
    await page.screenshot({ path: path.join(SNAPSHOTS_DIR, 'upload_step4_schedule_ready.png') });

    // Video URL check
    const linkEl = dialog.locator('a[href*="youtu.be"], a.ytcp-video-info').first();
    let videoUrl = null;
    if (await linkEl.count() > 0) {
      videoUrl = await linkEl.getAttribute('href');
    }
    console.log('  -> Video URL:', videoUrl);

    // Click Lên lịch (Schedule button)
    console.log('[7/7] Clicking Schedule (Lên lịch) button...');
    const scheduleBtn = dialog.locator('#done-button button, #done-button, ytcp-button:has-text("Lên lịch")').first();
    await scheduleBtn.click({ force: true });
    await page.waitForTimeout(6000);

    // Confirmation dialog screenshot
    await page.screenshot({ path: path.join(SNAPSHOTS_DIR, 'upload_scheduled_success.png') });
    console.log('=== UPLOAD & SCHEDULING COMPLETE ===');
    console.log('Scheduled Video URL:', videoUrl);

    // Close modal if open
    const closeBtn = page.locator('ytcp-post-publish-dialog #close-button, ytcp-dialog #close-button, button:has-text("Đóng")').first();
    if (await closeBtn.isVisible()) {
      await closeBtn.click();
      await page.waitForTimeout(2000);
    }

  } catch (err) {
    console.error('Upload error:', err);
    await page.screenshot({ path: path.join(SNAPSHOTS_DIR, 'upload_error.png') });
  } finally {
    await context.close();
  }
})();
