import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { spawn, execSync } from 'child_process';
import { chromium } from 'playwright';
import { compileStoryboard } from '../../dist/engine/frame_renderer.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT_DIR = path.resolve(__dirname, '../../');

function parseArgs() {
  const args = process.argv.slice(2);
  const config = {
    storyboardPath: null,
    exportPath: null,
    previewStills: false,
    fps: 30
  };

  for (let i = 0; i < args.length; i++) {
    const arg = args[i];
    if (arg === '--preview-stills') {
      config.previewStills = true;
    } else if (arg === '--export' && i + 1 < args.length) {
      config.exportPath = args[++i];
    } else if (arg === '--fps' && i + 1 < args.length) {
      config.fps = parseInt(args[++i], 10);
    } else if (!arg.startsWith('--') && !config.storyboardPath) {
      config.storyboardPath = arg;
    }
  }

  return config;
}

async function main() {
  const config = parseArgs();
  if (!config.storyboardPath) {
    console.error("Usage: node src/cli/build_video.mjs <storyboard.json> [--export <output.mp4>] [--preview-stills] [--fps 30]");
    process.exit(1);
  }

  const storyboardFullPath = path.resolve(config.storyboardPath);
  if (!fs.existsSync(storyboardFullPath)) {
    console.error(`Storyboard not found: ${storyboardFullPath}`);
    process.exit(1);
  }

  const projectDir = path.dirname(storyboardFullPath);
  const storyboard = JSON.parse(fs.readFileSync(storyboardFullPath, 'utf-8'));
  const fps = config.fps || storyboard.canvas?.fps || 30;
  const width = storyboard.canvas?.width || 1920;
  const height = storyboard.canvas?.height || 1080;

  console.log(`[INFO] Compiling storyboard: ${storyboard.title} (${width}x${height} @ ${fps}fps)`);
  const compiled = compileStoryboard(storyboard);

  // Determine total duration
  let totalDurationMs = 0;
  // Check words_timeline.json if narration exists
  const wordsTimelinePath = path.join(projectDir, 'words_timeline.json');
  if (fs.existsSync(wordsTimelinePath)) {
    const wData = JSON.parse(fs.readFileSync(wordsTimelinePath, 'utf-8'));
    if (wData.totalDurationMs) {
      totalDurationMs = wData.totalDurationMs;
    }
  }

  if (totalDurationMs === 0) {
    for (const s of compiled.allStrokes) {
      totalDurationMs = Math.max(totalDurationMs, s.endMs + 1000);
    }
    for (const sub of compiled.subtitles) {
      totalDurationMs = Math.max(totalDurationMs, sub.endMs + 800);
    }
  }

  const totalFrames = Math.ceil((totalDurationMs / 1000) * fps);
  console.log(`[INFO] Total duration: ${(totalDurationMs / 1000).toFixed(2)}s (${totalFrames} frames)`);

  // Launch Playwright Chromium
  console.log("[INFO] Launching Headless Chromium with Playwright...");
  const browser = await chromium.launch({
    headless: true,
    args: [
      '--disable-web-security',
      '--allow-file-access-from-files',
      '--no-sandbox',
      '--disable-setuid-sandbox'
    ]
  });

  const page = await browser.newPage({
    viewport: { width, height },
    deviceScaleFactor: 1
  });

  page.on('console', (msg) => {
    if (msg.type() === 'error') console.error('[PAGE ERROR]', msg.text());
  });
  page.on('requestfailed', (req) => {
    console.error('[REQUEST FAILED]', req.url(), req.failure()?.errorText);
  });

  const stageFile = path.resolve(ROOT_DIR, 'src/engine/stage.html');
  let stageHtml = fs.readFileSync(stageFile, 'utf-8');

  // Embed all assets as Base64 data URIs so Chromium loads them with 100% reliability
  const assetRegex = /(\.\.\/\.\.\/assets\/([a-zA-Z0-9_\-\/]+\.(png|jpg|jpeg|svg|webp)))/g;
  stageHtml = stageHtml.replace(assetRegex, (match, fullRelPath, relPath, ext) => {
    const absPath = path.resolve(ROOT_DIR, 'assets', relPath);
    if (fs.existsSync(absPath)) {
      const mime = ext === 'svg' ? 'image/svg+xml' : ('image/' + (ext === 'jpg' ? 'jpeg' : ext));
      const b64 = fs.readFileSync(absPath).toString('base64');
      return `data:${mime};base64,${b64}`;
    }
    return match;
  });

  // Always sync HAND_METADATA from assets/hands/hand_metadata.json
  const handMetaFile = path.resolve(ROOT_DIR, 'assets/hands/hand_metadata.json');
  if (fs.existsSync(handMetaFile)) {
    const meta = JSON.parse(fs.readFileSync(handMetaFile, 'utf-8'));
    stageHtml = stageHtml.replace(
      /const HAND_METADATA = \{[\s\S]*?\};/,
      `const HAND_METADATA = ${JSON.stringify(meta, null, 2)};`
    );
  }

  await page.setContent(stageHtml, { waitUntil: 'load' });

  // Verify hand sprite image loaded with valid dimensions
  const imgStatus = await page.evaluate(() => {
    const img = document.getElementById('hand-sprite-img');
    return {
      complete: img?.complete,
      naturalWidth: img?.naturalWidth || 0,
      naturalHeight: img?.naturalHeight || 0
    };
  });
  if (!imgStatus.complete || imgStatus.naturalWidth === 0) {
    console.warn('[WARN] Hand sprite image may not have loaded properly:', imgStatus);
  } else {
    console.log(`[OK] Hand rig loaded successfully (${imgStatus.naturalWidth}x${imgStatus.naturalHeight})`);
  }

  // Convert any image cutouts in compiled.allImages to Base64 data URIs
  if (compiled.allImages) {
    let convertedCount = 0;
    for (const img of compiled.allImages) {
      if (img.href && !img.href.startsWith('data:')) {
        let absImgPath = path.isAbsolute(img.href) ? img.href : path.resolve(ROOT_DIR, img.href);
        if (!fs.existsSync(absImgPath)) {
          absImgPath = path.resolve(projectDir, img.href);
        }
        if (fs.existsSync(absImgPath)) {
          const ext = path.extname(absImgPath).toLowerCase().replace('.', '');
          const mime = ext === 'svg' ? 'image/svg+xml' : ('image/' + (ext === 'jpg' ? 'jpeg' : ext));
          img.href = `data:${mime};base64,${fs.readFileSync(absImgPath).toString('base64')}`;
          convertedCount++;
        } else {
          console.error(`[ERROR] Image asset not found: ${img.href} (checked ROOT_DIR and projectDir)`);
        }
      } else if (img.href && img.href.startsWith('data:')) {
        convertedCount++;
      }
    }
    console.log(`[OK] Embedded ${convertedCount}/${compiled.allImages.length} images as Base64 data URIs.`);
  }

  // Initialize stage with compiled strokes and camera
  await page.evaluate((data) => {
    return window.initStage(data);
  }, compiled);

  // Mode A: Preview Stills Check
  if (config.previewStills) {
    console.log("[INFO] Exporting scene preview stills...");
    const stillsDir = path.join(projectDir, 'preview_stills');
    fs.mkdirSync(stillsDir, { recursive: true });

    let sceneEndMs = 0;
    for (let scIdx = 0; scIdx < storyboard.scenes.length; scIdx++) {
      const scene = storyboard.scenes[scIdx];
      let maxMs = 0;
      for (const b of scene.beats) {
        maxMs = Math.max(maxMs, b.startMs + b.durationMs);
      }
      const checkMs = maxMs > 0 ? maxMs + 200 : 3000;
      await page.evaluate((t) => window.renderFrameAt(t), checkMs);
      const stillPath = path.join(stillsDir, `scene_${scIdx + 1}_${scene.sceneId}.png`);
      await page.screenshot({ path: stillPath, type: 'png' });
      console.log(`[OK] Saved preview still: ${stillPath}`);
    }

    await browser.close();
    console.log("[OK] Preview stills generated successfully.");
    return;
  }

  // Mode B: Full Deterministic Render
  const exportPath = config.exportPath ? path.resolve(config.exportPath) : path.join(projectDir, 'output.mp4');
  const tempVideoOnlyPath = path.join(projectDir, 'temp_video_stream.mp4');
  const motionLogPath = path.join(projectDir, 'hand_motion_log.json');
  const masterAudioPath = path.join(projectDir, 'master_audio.wav');
  const sfxTrackPath = path.join(projectDir, 'sfx_track.wav');

  // Clean up any stale files from previous runs
  try {
    if (fs.existsSync(tempVideoOnlyPath)) fs.unlinkSync(tempVideoOnlyPath);
    if (fs.existsSync(masterAudioPath)) fs.unlinkSync(masterAudioPath);
    if (fs.existsSync(sfxTrackPath)) fs.unlinkSync(sfxTrackPath);
  } catch (err) {}

  console.log(`[INFO] Starting frame rendering pipeline to pipe -> FFmpeg...`);

  // Setup FFmpeg process for video pipe (mjpeg pipe for 13x faster throughput)
  const ffmpegArgs = [
    '-y',
    '-f', 'image2pipe',
    '-vcodec', 'mjpeg',
    '-r', `${fps}`,
    '-i', '-',
    '-c:v', 'libx264',
    '-preset', 'fast',
    '-crf', '18',
    '-pix_fmt', 'yuv420p',
    tempVideoOnlyPath
  ];

  const ffmpeg = spawn('ffmpeg', ffmpegArgs, {
    stdio: ['pipe', 'inherit', 'inherit']
  });

  const motionFrames = [];
  const dtMs = 1000 / fps;

  const startTime = Date.now();
  for (let f = 0; f < totalFrames; f++) {
    const timeMs = Math.round(f * dtMs);
    const telemetry = await page.evaluate((t) => window.renderFrameAt(t), timeMs);
    telemetry.dtMs = dtMs;
    motionFrames.push(telemetry);

    const frameBuf = await page.screenshot({ type: 'jpeg', quality: 95 });
    const canWrite = ffmpeg.stdin.write(frameBuf);
    if (!canWrite) {
      await new Promise(resolve => ffmpeg.stdin.once('drain', resolve));
    }

    if (f % 30 === 0 || f === totalFrames - 1) {
      const pct = Math.round(((f + 1) / totalFrames) * 100);
      const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);
      process.stdout.write(`\r[RENDER] Frame ${f + 1}/${totalFrames} (${pct}%) - Elapsed: ${elapsed}s`);
    }
  }
  console.log("\n[OK] All frames rendered to FFmpeg pipe.");

  ffmpeg.stdin.end();
  await new Promise((resolve, reject) => {
    ffmpeg.on('close', (code) => {
      if (code === 0) resolve(code);
      else reject(new Error(`FFmpeg exited with code ${code}`));
    });
  });

  await browser.close();

  // Save motion log for SFX mixer
  fs.writeFileSync(motionLogPath, JSON.stringify({
    totalDurationMs,
    fps,
    frames: motionFrames
  }, null, 2));
  console.log(`[OK] Saved hand motion log: ${motionLogPath}`);

  // Step 3: Mix Audio (Narration + SFX + BGM)
  let narrationPath = storyboard.audio?.narrationWav;
  if (narrationPath) {
    if (!path.isAbsolute(narrationPath)) {
      const p1 = path.resolve(projectDir, narrationPath);
      const p2 = path.resolve(ROOT_DIR, narrationPath);
      const p3 = path.resolve(projectDir, path.basename(narrationPath));
      narrationPath = fs.existsSync(p1) ? p1 : (fs.existsSync(p2) ? p2 : (fs.existsSync(p3) ? p3 : p1));
    }
  } else {
    narrationPath = path.join(projectDir, 'narration.wav');
  }

  if (fs.existsSync(narrationPath)) {
    console.log(`[INFO] Found narration audio: ${narrationPath}`);
    console.log("[INFO] Mixing synchronized SFX and Narration...");
    const mixerScript = path.resolve(ROOT_DIR, 'src/audio/sfx_mixer.py');
    const mixerCmd = `python "${mixerScript}" --motion-log "${motionLogPath}" --duration-ms ${Math.round(totalDurationMs)} --narration "${narrationPath}" --sfx-out "${sfxTrackPath}" --output "${masterAudioPath}"`;
    try {
      execSync(mixerCmd, { stdio: 'inherit' });
    } catch (e) {
      console.warn("[WARN] SFX mixing error, falling back to raw narration audio:", e.message);
    }
  } else {
    console.warn(`[WARN] Narration audio file not found at: ${narrationPath}`);
  }

  // Step 4: Final Mux (Video + Master Audio -> Final MP4)
  console.log(`[INFO] Muxing final video with audio -> ${exportPath}`);
  const finalAudio = fs.existsSync(masterAudioPath) ? masterAudioPath : (fs.existsSync(narrationPath) ? narrationPath : null);

  let muxCmd;
  if (finalAudio) {
    muxCmd = `ffmpeg -y -i "${tempVideoOnlyPath}" -i "${finalAudio}" -c:v copy -c:a aac -b:a 192k -shortest "${exportPath}"`;
  } else {
    muxCmd = `ffmpeg -y -i "${tempVideoOnlyPath}" -c:v copy "${exportPath}"`;
  }

  execSync(muxCmd, { stdio: 'inherit' });

  // Cleanup temp video stream
  try {
    if (fs.existsSync(tempVideoOnlyPath)) {
      fs.unlinkSync(tempVideoOnlyPath);
    }
  } catch (e) {
    // Non-fatal on Windows lock
  }

  console.log(`\n=======================================================`);
  console.log(`[SUCCESS] AI Whiteboard Animation Video created!`);
  console.log(`File: ${exportPath}`);
  console.log(`=======================================================\n`);
}

main().catch(err => {
  console.error("[FATAL ERROR]:", err);
  process.exit(1);
});
