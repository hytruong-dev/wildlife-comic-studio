/**
 * Đọc config/channel.json rồi ghi đè bằng config/local.json (riêng từng máy, KHÔNG đưa lên git).
 * Dùng cho mọi script Playwright: chrome_profile khác nhau giữa các máy.
 *   config/local.json: { "chrome_profile": "C:\\Users\\<user>\\AppData\\Local\\vcd-chrome" }
 * Biến môi trường trong chuỗi (%LOCALAPPDATA%, %USERPROFILE%) được tự mở rộng.
 */
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..', '..');

function expand(s) {
  return typeof s === 'string' ? s.replace(/%([^%]+)%/g, (m, k) => process.env[k] ?? m) : s;
}

function loadChannel() {
  const ch = JSON.parse(fs.readFileSync(path.join(ROOT, 'config/channel.json'), 'utf8'));
  const localFile = path.join(ROOT, 'config/local.json');
  if (fs.existsSync(localFile)) {
    const local = JSON.parse(fs.readFileSync(localFile, 'utf8').replace(/^\uFEFF/, ''));  // PowerShell 5 ghi kèm BOM
    for (const [k, v] of Object.entries(local)) {
      ch[k] = (v && typeof v === 'object' && !Array.isArray(v) && ch[k] && typeof ch[k] === 'object') ? { ...ch[k], ...v } : v;
    }
  }
  ch.chrome_profile = expand(ch.chrome_profile);
  return ch;
}

module.exports = { loadChannel, ROOT };
