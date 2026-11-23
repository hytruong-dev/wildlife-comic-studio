const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const CH = JSON.parse(fs.readFileSync(path.join(ROOT, 'config/channel.json'), 'utf8'));
const ID = 'I_Th6_Vfrmg';

(async () => {
  const ctx = await chromium.launchPersistentContext(CH.chrome_profile, {
    headless: false, channel: 'chrome', viewport: { width: 1500, height: 900 },
    args: ['--disable-blink-features=AutomationControlled'],
  });
  const page = ctx.pages()[0] || await ctx.newPage();
  try {
    await page.goto(`https://studio.youtube.com/video/${ID}/edit`, { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(6000);

    const snapDir = path.join(ROOT, 'projects/mega-01-dai-hoi-sinh-ton/renders/snapshots');

    const plTrigger = page.locator('ytcp-video-metadata-playlists #basics-playlists-dropdown, ytcp-video-metadata-playlists #trigger, ytcp-video-metadata-playlists ytcp-dropdown-trigger').first();
    await plTrigger.scrollIntoViewIfNeeded();
    await plTrigger.click();
    await page.waitForTimeout(2000);

    // Click checkbox inside dialog
    await page.evaluate((plName) => {
      const items = [...document.querySelectorAll('ytcp-playlist-dialog li, ytcp-playlist-dialog ytcp-checkbox-lit')];
      for (const item of items) {
        if (item.innerText && item.innerText.includes(plName)) {
          const cb = item.querySelector('tp-yt-paper-checkbox') || item;
          cb.click();
          break;
        }
      }
    }, CH.playlist);
    await page.waitForTimeout(1500);

    // Click Done (Xong)
    await page.locator('ytcp-playlist-dialog #done-button, ytcp-playlist-dialog ytcp-button:has-text("Xong")').first().click({ timeout: 5000 });
    await page.waitForTimeout(2500);

    // Click Save button
    const saveBtn = page.locator('#save, ytcp-button#save').first();
    const disabled = await saveBtn.getAttribute('aria-disabled');
    console.log('Save button disabled status:', disabled);
    if (disabled !== 'true') {
      await saveBtn.click({ timeout: 10000 });
      await page.waitForTimeout(5000);
      console.log('Saved playlist successfully!');
    } else {
      console.log('Save button is still disabled? Checking why...');
    }

    await page.screenshot({ path: path.join(snapDir, 'upload_long_saved_final.png') });
    console.log('Saved final screenshot to upload_long_saved_final.png');
  } catch (e) {
    console.error('Error:', e.message);
  } finally {
    await ctx.close();
  }
})();
