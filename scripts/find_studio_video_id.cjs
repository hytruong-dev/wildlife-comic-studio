// Find a video ID in YouTube Studio by clicking the row whose title contains the given text.
//   node scripts/find_studio_video_id.cjs shorts "Bể Kính"
// (Studio rows of freshly uploaded/processing videos expose no <a href>, so we click the title and read the URL.)
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const CH = JSON.parse(fs.readFileSync(path.join(__dirname, '../config/channel.json'), 'utf8'));
const [tab = 'shorts', needle = ''] = process.argv.slice(2);
(async () => {
  const ctx = await chromium.launchPersistentContext(CH.chrome_profile, { headless: false, channel: 'chrome', viewport: { width: 1500, height: 900 } });
  const page = ctx.pages()[0] || await ctx.newPage();
  try {
    await page.goto(`https://studio.youtube.com/channel/${CH.channel_id}/videos/${tab}`, { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(15000);
    const title = page.getByText(needle, { exact: false }).first();
    await title.click({ timeout: 15000 });
    await page.waitForTimeout(6000);
    const m = page.url().match(/video\/([\w-]{11})/);
    console.log('URL', page.url());
    console.log('MATCH', m ? m[1] : 'none');
  } catch (e) {
    console.log('ERR', e.message.split('\n')[0]);
    console.log('PAGE', (await page.evaluate(() => document.body.innerText)).replace(/\s+/g, ' ').slice(0, 1200));
    await page.screenshot({ path: path.join(__dirname, '../projects/tap-07-tom-tit/renders/snapshots/find_id.png') }).catch(() => {});
  }
  finally { await ctx.close(); }
})();
