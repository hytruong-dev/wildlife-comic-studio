// Playwright MCP snippet: browser_run_code_unsafe { filename: "<abs path to this file>" }
// Gắn màn hình kết thúc "1 video + 1 danh sách phát + 1 đăng ký" (playlist Thế Giới Động Vật)
// cho các video dài trong IDS. Video đã có màn hình kết thúc thì bỏ qua (không ghi đè).
async (page) => {
  const IDS = ['xeQbH_olDGc', 'WRAp223qZ60', 'DOPcbU7gvjs', 'WbE6Nn7XUIE', 'ogvEUfQOWGA', 'KXJQReDxDcA', 'HEjl0zaZSTQ'];
  const PL = 'Thế Giới Động Vật';
  const out = [];
  for (const id of IDS) {
    try {
      await page.goto(`https://studio.youtube.com/video/${id}/edit`);
      await page.waitForTimeout(7000);
      await page.getByText('Màn hình kết thúc', { exact: true }).first().click();
      await page.waitForTimeout(9000);
      const modal = page.locator('ytve-endscreen-modal');
      const existing = await page.locator('ytve-endscreen-row').count();
      if (existing > 0) { await page.keyboard.press('Escape'); out.push(`${id}: already has end screen (${existing}) - skipped`); continue; }
      await page.locator('[role=gridcell][aria-label="1 video, 1 danh sách phát, 1 đăng ký"]').first().click();
      await page.waitForTimeout(4000);
      let ok = false;
      for (let a = 0; a < 3 && !ok; a++) {
        await page.locator('ytve-endscreen-editor-preview-overlay-item.error').first().click({ force: true }).catch(() => {});
        await page.waitForTimeout(2500);
        const box = await page.locator('ytve-options-panel-entity-item .entityName').first().boundingBox();
        if (box) await page.mouse.click(box.x + box.width / 2, box.y + box.height / 2);
        const card = page.locator('ytcp-playlist-pick-dialog ytcp-entity-card').filter({ hasText: PL }).first();
        try { await card.waitFor({ state: 'visible', timeout: 10000 }); await card.click({ force: true }); ok = true; } catch {}
        await page.waitForTimeout(3000);
      }
      const txt = (await modal.innerText()).replace(/\s+/g, ' ');
      if (!ok || /Vui lòng chọn/.test(txt)) { await page.keyboard.press('Escape'); out.push(`${id}: playlist not set - NOT saved`); continue; }
      await modal.locator('ytcp-button:has-text("Lưu")').first().click();
      await page.waitForTimeout(6000);
      out.push(`${id}: saved=${!(await modal.isVisible().catch(() => false))}`);
    } catch (e) { out.push(`${id}: ERROR ${String(e).slice(0, 150)}`); }
  }
  return out.join('\n');
}
