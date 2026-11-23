<#
.SYNOPSIS
  Cài toàn bộ môi trường sản xuất video "Vẽ Chuyện Hoang Dã" trên máy Windows mới. Chạy lại bao nhiêu lần cũng an toàn.

.USAGE
  powershell -ExecutionPolicy Bypass -File scripts\setup_new_machine.ps1            # cài + kiểm tra
  powershell -ExecutionPolicy Bypass -File scripts\setup_new_machine.ps1 -CheckOnly # chỉ kiểm tra

  Chi tiết từng bước + lý do: SETUP_MAY_MOI.md
#>
param([switch]$CheckOnly)

$ErrorActionPreference = 'Continue'
$ROOT = Split-Path -Parent $PSScriptRoot
Set-Location $ROOT
$results = [System.Collections.Generic.List[object]]::new()
function Ok($name, $detail)   { $results.Add([pscustomobject]@{Muc=$name; KetQua='OK';    ChiTiet=$detail}) }
function Bad($name, $detail)  { $results.Add([pscustomobject]@{Muc=$name; KetQua='THIEU'; ChiTiet=$detail}) }
function Step($t) { Write-Host "`n=== $t" -ForegroundColor Cyan }
function Refresh-Path { $env:Path = [Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [Environment]::GetEnvironmentVariable('Path','User') }
function Has($cmd) { [bool](Get-Command $cmd -ErrorAction SilentlyContinue) }
function WingetInstall($id) {
  if ($CheckOnly) { return }
  if (-not (Has winget)) { Write-Host "  khong co winget — cai tay $id" -ForegroundColor Yellow; return }
  winget install --id $id -e --accept-source-agreements --accept-package-agreements --silent
  Refresh-Path
}

# ---------------------------------------------------------------- 1. Phần mềm hệ thống
Step "1. Phan mem he thong (git, Python, Node, ffmpeg, Chrome)"
if (-not (Has git))    { WingetInstall 'Git.Git' }
if (-not (Has python)) { WingetInstall 'Python.Python.3.14' }
if (-not (Has node))   { WingetInstall 'OpenJS.NodeJS' }
if (-not (Has ffmpeg)) { WingetInstall 'Gyan.FFmpeg' }
$chrome = "$env:ProgramFiles\Google\Chrome\Application\chrome.exe"
if (-not (Test-Path $chrome)) { WingetInstall 'Google.Chrome' }
Refresh-Path
foreach ($c in 'git','python','node','npm','ffmpeg') {
  if (Has $c) { $v = (& $c --version 2>&1 | Select-Object -First 1); Ok $c "$v" } else { Bad $c "winget install (xem SETUP_MAY_MOI.md muc 2)" }
}
if (Test-Path $chrome) { Ok 'chrome' $chrome } else { Bad 'chrome' 'winget install Google.Chrome' }

# ---------------------------------------------------------------- 2. Python packages của pipeline
Step "2. Python packages (requirements.txt)"
if ((Has python) -and -not $CheckOnly) { python -m pip install --upgrade pip -q; python -m pip install -r requirements.txt }
if (Has python) {
  $miss = python -c "import importlib.util as u; m=['faster_whisper','cv2','numpy','scipy','skimage','PIL','soundfile','requests','yt_dlp','bs4']; print(','.join(x for x in m if not u.find_spec(x)))"
  if ($miss) { Bad 'pip packages' "thieu: $miss" } else { Ok 'pip packages' 'faster-whisper, opencv, numpy, scipy, scikit-image, pillow, soundfile, yt-dlp...' }
  if (Has yt-dlp) { Ok 'yt-dlp' (yt-dlp --version) } else { Bad 'yt-dlp' 'python -m pip install yt-dlp (va them Scripts vao PATH)' }
}

# ---------------------------------------------------------------- 3. Node packages + Playwright
Step "3. Node packages (package.json: playwright, remotion, roughjs...)"
if ((Has npm) -and -not $CheckOnly) { if (Test-Path package-lock.json) { npm ci } else { npm install } }
if (Test-Path node_modules/playwright/package.json) { Ok 'node_modules' ("playwright " + (Get-Content node_modules/playwright/package.json | ConvertFrom-Json).version) }
else { Bad 'node_modules' 'npm ci' }

# ---------------------------------------------------------------- 4. Repo ngoài trong tools/ (khóa đúng commit)
Step "4. Repo ngoai trong tools/ (dung commit nhu may goc)"
$tools = @(
  @{n='YoutubeTags';                  u='https://github.com/nuhmanpk/YoutubeTags.git';                    c='cc960f068f5a07f21b5720208ea2f8f56cce5f61'},
  @{n='hybrid-youtube-growth-engine'; u='https://github.com/catball912/hybrid-youtube-growth-engine.git'; c='b5a34eae7630d261b28ccdd097aec425e13cbd00'},
  @{n='YouTube-Video-SEO-Analyzer';   u='https://github.com/kumarAnand05/YouTube-Video-SEO-Analyzer.git'; c='b95b9439532f5959b0f5558f62146d1b6ccad106'},
  @{n='youtube-suggest-scraper';      u='https://github.com/ChocoData-com/youtube-suggest-scraper.git';   c='4546f37ee00637d4ef7fa38c3ac4d1a935ab2535'},
  @{n='Open-Tube-SEO';                u='https://github.com/BizMapper/Open-Tube-SEO.git';                 c='151484879bc1314da580638bd083d7367445d9e1'},
  @{n='youtube-research-skills';      u='https://github.com/TubeLabHQ/youtube-research-skills.git';       c='a8a674681e5297ce700ba9393e11cff451f2768a'},
  @{n='srt-whiteboard-animation';     u='https://github.com/geeklee/srt-whiteboard-animation.git';        c='696a7243c0e6ffb6827676e539c2ca5ebae2bf6b'},
  @{n='hyperframes';                  u='https://github.com/heygen-com/hyperframes.git';                  c='0bd1fd59721a2660d07474e1628e18d6c1ced09f'}
)
New-Item -ItemType Directory -Force tools | Out-Null
foreach ($t in $tools) {
  $dir = Join-Path 'tools' $t.n
  if (-not (Test-Path "$dir/.git") -and -not $CheckOnly) { git clone -q $t.u $dir }
  if (Test-Path "$dir/.git") {
    if (-not $CheckOnly) { git -C $dir fetch -q origin $t.c 2>$null; git -C $dir -c advice.detachedHead=false checkout -q $t.c 2>$null }
    $head = git -C $dir rev-parse HEAD
    if ($head -eq $t.c) { Ok "tools/$($t.n)" $t.c.Substring(0,7) } else { Ok "tools/$($t.n)" "commit $($head.Substring(0,7)) (goc $($t.c.Substring(0,7)))" }
  } else { Bad "tools/$($t.n)" "git clone $($t.u) $dir" }
}
# Bản vá ảnh bàn tay đã chỉnh trên máy gốc (renderer cũ đọc từ tools/srt-whiteboard-animation/assets)
$patch = 'assets/vendor_patches/srt-whiteboard-animation/assets'
if ((Test-Path $patch) -and (Test-Path 'tools/srt-whiteboard-animation/assets') -and -not $CheckOnly) {
  Copy-Item "$patch/*" 'tools/srt-whiteboard-animation/assets/' -Force
}

# ---------------------------------------------------------------- 5. Model Whisper "small" (align)
Step "5. Model faster-whisper 'small' cho buoc align (~464MB, tai 1 lan)"
if ((Has python) -and -not $CheckOnly) {
  python -c "from faster_whisper import WhisperModel; WhisperModel('small', device='cpu', compute_type='int8'); print('whisper small OK')"
}
$ws = Join-Path $env:USERPROFILE '.cache\huggingface\hub\models--Systran--faster-whisper-small'
if (Test-Path $ws) { Ok 'whisper small' $ws } else { Bad 'whisper small' 'python -c "from faster_whisper import WhisperModel; WhisperModel(''small'')"' }

# ---------------------------------------------------------------- 6. VoiceStudio (giọng đọc) — phải cài tay app
Step "6. VoiceStudio + model OmniVoice (giong doc)"
$vsPy = Join-Path $env:LOCALAPPDATA 'com.debpalash.omnivoice-studio\project\.venv\Scripts\python.exe'
$vsModel = Join-Path $env:LOCALAPPDATA 'OmniVoice\hf_cache\models--k2-fsa--OmniVoice'
if (Test-Path $vsPy) { Ok 'VoiceStudio' $vsPy } else { Bad 'VoiceStudio' 'Tai https://github.com/debpalash/VoiceStudio/releases (ban Windows), mo 1 lan, tab Models -> tai OmniVoice' }
if (Test-Path $vsModel) { Ok 'model OmniVoice' '~5.5GB' } else { Bad 'model OmniVoice' 'Mo VoiceStudio -> Models -> OmniVoice -> Download' }
if (Test-Path $vsPy) {
  & $vsPy -c "import torch, omnivoice; print('torch', torch.__version__, '| cuda', torch.cuda.is_available())" 2>&1 | ForEach-Object { Write-Host "  $_" }
}

# ---------------------------------------------------------------- 7. Cấu hình riêng máy + tài sản giọng
Step "7. config/local.json (Chrome profile rieng may nay) + tai san giong mau"
$local = 'config/local.json'
if (-not (Test-Path $local) -and -not $CheckOnly) {
  $prof = Join-Path $env:LOCALAPPDATA 'vcd-chrome'
  $json = @{ chrome_profile = $prof } | ConvertTo-Json
  [IO.File]::WriteAllText((Join-Path $ROOT $local), $json, (New-Object Text.UTF8Encoding $false))  # không BOM
  Write-Host "  tao $local -> chrome_profile = $prof"
}
if (Test-Path $local) { Ok 'config/local.json' ((Get-Content $local -Raw) -replace '\s+',' ') } else { Bad 'config/local.json' 'chay lai script khong co -CheckOnly' }
foreach ($f in 'assets/voice_refs/adam_funny_ep1.wav','assets/voice_refs/adam_funny_ep1.txt','assets/bgm/calm-acoustic.wav',
               'assets/branding/intro_ve_chuyen_hoang_da.mp4','assets/branding/outro_ve_chuyen_hoang_da.mp4',
               'assets/fonts/BeVietnamPro-Bold.ttf','assets/fonts/Mali-Bold.ttf','assets/hands/hand-marker-right.png') {
  if (Test-Path $f) { Ok $f 'co' } else { Bad $f 'thieu file tai san — git pull lai' }
}
$cast = (Get-ChildItem assets/voice_refs -Filter 'cast_*.wav' -ErrorAction SilentlyContinue).Count
if ($cast -ge 9) { Ok 'giong cameo cast_*.wav' "$cast file" } else { Bad 'giong cameo cast_*.wav' "chi co $cast — python scripts/make_cast_refs.py" }

# ---------------------------------------------------------------- 8. Kiểm tra pipeline thật
Step "8. Kiem tra pipeline (pipeline.py check tren tap mau)"
$sample = Get-ChildItem projects -Directory -Filter 'tap-*' -ErrorAction SilentlyContinue | Sort-Object Name | Select-Object -Last 1
if ($sample -and (Has python)) {
  $out = python src/episode/pipeline.py check $sample.FullName 2>&1 | Out-String
  if ($out -match 'VoiceStudio OK') { Ok 'pipeline.py check' "VoiceStudio OK ($($sample.Name))" } else { Bad 'pipeline.py check' ($out.Trim() -split "`n" | Select-Object -First 2) -join ' ' }
}

# ---------------------------------------------------------------- Tổng kết
Write-Host "`n================ KET QUA ================" -ForegroundColor Cyan
$results | Format-Table -AutoSize -Wrap
$bad = @($results | Where-Object KetQua -eq 'THIEU')
if ($bad.Count -eq 0) {
  Write-Host "SAN SANG SAN XUAT. Buoc tay con lai (1 lan): dang nhap Google trong Chrome profile:" -ForegroundColor Green
  Write-Host "  node src/episode/gemini_gen.cjs projects/$($sample.Name) probe   -> signedIn: true" -ForegroundColor Green
} else {
  Write-Host "$($bad.Count) muc con THIEU — xem cot ChiTiet hoac SETUP_MAY_MOI.md" -ForegroundColor Yellow
  exit 1
}
