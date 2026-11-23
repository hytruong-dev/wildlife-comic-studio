async (page) => {
  // Wait until the newest model-response contains a finished image, then stash its dataURL in window.__img.
  for (let k = 0; k < 120; k++) {
    const r = await page.evaluate(() => {
      const rs = [...document.querySelectorAll('model-response')];
      const last = rs.at(-1);
      if (!last) return { st: 'none' };
      const im = [...last.querySelectorAll('img')].find(x => x.naturalWidth > 300 && x.complete);
      if (!im) return { st: 'wait', n: rs.length, txt: last.innerText.slice(0, 160) };
      const c = document.createElement('canvas');
      c.width = im.naturalWidth; c.height = im.naturalHeight;
      c.getContext('2d').drawImage(im, 0, 0);
      window.__img = c.toDataURL('image/png');
      return { st: 'ok', n: rs.length, w: im.naturalWidth, h: im.naturalHeight, len: window.__img.length };
    });
    if (r.st === 'ok') return r;
    if (k > 20 && r.txt && /không thể|can't|cannot|giới hạn|limit/i.test(r.txt)) return r;
    await page.waitForTimeout(3000);
  }
  return { st: 'timeout' };
}
