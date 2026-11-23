// Playwright MCP snippet: đếm số thành phần màn hình kết thúc của từng video dài (chỉ đọc, không lưu).
async (page) => {
  const IDS = ['WRAp223qZ60', 'DOPcbU7gvjs', 'WbE6Nn7XUIE', 'ogvEUfQOWGA', 'KXJQReDxDcA', 'HEjl0zaZSTQ', 'jLgbk3YMqq4', 'R4S5wDrD-KQ', 'HC1vxRkS1Yk', 'xeQbH_olDGc'];
  const out = [];
  for (const id of IDS) {
    try {
      await page.goto(`https://studio.youtube.com/video/${id}/edit`);
      await page.waitForTimeout(6000);
      await page.getByText('Màn hình kết thúc', { exact: true }).first().click();
      await page.waitForTimeout(8000);
      const rows = await page.locator('ytve-endscreen-row').allInnerTexts();
      out.push(`${id}: ${rows.length} -> ${rows.map(r => r.replace(/\s+/g, ' ').trim()).join(' / ')}`);
      await page.keyboard.press('Escape');
      await page.waitForTimeout(1500);
    } catch (e) { out.push(`${id}: ERROR ${String(e).slice(0, 100)}`); }
  }
  return out.join('\n');
}
