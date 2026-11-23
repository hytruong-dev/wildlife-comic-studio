"""Sinh snippet Playwright MCP (browser_run_code_unsafe filename=...) để thêm bản dịch tiếng Anh
(tiêu đề + mô tả) cho từng video dài, dữ liệu từ config/en_metadata.json.

  python scripts/gen_en_translation_snippets.py         -> tmp/en_tr/<id>.js (mỗi video 1 file)
Mỗi snippet: mở /video/<id>/translations, thêm 'Tiếng Anh' nếu chưa có, bấm Thêm ở cột Tiêu đề và mô tả,
điền, bấm Xuất bản. Nếu đã có bản dịch tiếng Anh thì bỏ qua (không ghi đè).
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
cfg = json.loads((ROOT / "config/en_metadata.json").read_text(encoding="utf-8"))
out = ROOT / "tmp/en_tr"
out.mkdir(parents=True, exist_ok=True)

TEMPLATE = r"""async (page) => {
  const V = __DATA__;
  await page.goto(`https://studio.youtube.com/video/${V.id}/translations`, { timeout: 60000, waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(8000);
  const enRow = () => page.locator('ytgn-video-translation-row').filter({ hasText: /^\s*Tiếng Anh\s/ }).first();
  if (!(await enRow().count())) {
    await page.getByText('Thêm ngôn ngữ', { exact: true }).first().click({ noWaitAfter: true });
    await page.waitForTimeout(2500);
    await page.locator('tp-yt-paper-item:visible').filter({ hasText: /^\s*Tiếng Anh\s*$/ }).first().click({ noWaitAfter: true });
    await page.waitForTimeout(4000);
  }
  const row = enRow();
  const cell = row.locator('#cell-container').nth(1);
  const cellText = (await cell.innerText()).trim();
  if (cellText && cellText !== '–' && cellText !== '-') return `${V.id}: EN metadata already exists (${cellText.slice(0, 40)}) - skipped`;
  const box = await cell.boundingBox();
  await page.mouse.move(box.x + box.width / 2, box.y + box.height / 2);
  await page.waitForTimeout(1200);
  const b = await row.evaluate(e => { const x = [...e.querySelectorAll('#metadata-add, ytcp-button')].find(b => b.getBoundingClientRect().width > 0); if (!x) return null; const r = x.getBoundingClientRect(); return [r.x + r.width / 2, r.y + r.height / 2]; });
  if (!b) return `${V.id}: add button not found`;
  await page.mouse.click(b[0], b[1]);
  await page.waitForTimeout(4000);
  const dlg = page.locator('tp-yt-paper-dialog:visible').filter({ hasText: 'Bản dịch' }).last();
  const ta = dlg.locator('textarea');
  await ta.nth(1).fill(V.title);
  await ta.nth(3).fill(V.desc);
  await page.waitForTimeout(1000);
  await dlg.locator('ytcp-button:has-text("Xuất bản")').first().click({ noWaitAfter: true });
  await page.waitForTimeout(5000);
  const after = (await enRow().locator('#cell-container').nth(1).innerText().catch(() => '?')).replace(/\s+/g, ' ').trim();
  return `${V.id}: published -> ${after.slice(0, 60)}`;
}
"""

for v in cfg["videos"]:
    desc = v["desc"]
    if v.get("chapters"):
        desc += "\n\nCHAPTERS:\n" + v["chapters"]
    desc += cfg["footer"]
    assert len(v["title"]) <= 100, (v["id"], len(v["title"]))
    assert len(desc) <= 5000
    data = json.dumps({"id": v["id"], "title": v["title"], "desc": desc}, ensure_ascii=False)
    (out / f"ep{v['ep']:02d}_{v['id']}.js").write_text(TEMPLATE.replace("__DATA__", data), encoding="utf-8")
    print(f"ep{v['ep']:02d} {v['id']} title={len(v['title'])} desc={len(desc)}")
