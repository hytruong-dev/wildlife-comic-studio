import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';

function runQACheck(storyboardPath) {
  console.log(`\n=======================================================`);
  console.log(`[QA CHECKER] Starting Automated Quality Assurance`);
  console.log(`Target: ${storyboardPath}`);
  console.log(`=======================================================\n`);

  if (!fs.existsSync(storyboardPath)) {
    console.error(`[FAIL] Storyboard file not found: ${storyboardPath}`);
    process.exit(1);
  }

  const projectDir = path.dirname(path.resolve(storyboardPath));
  const storyboard = JSON.parse(fs.readFileSync(storyboardPath, 'utf-8'));
  let passCount = 0;
  let warnCount = 0;
  let failCount = 0;

  // 1. Check Canvas Configuration
  const w = storyboard.canvas?.width || 1920;
  const h = storyboard.canvas?.height || 1080;
  if (w >= 1280 && h >= 720) {
    console.log(`[PASS] Canvas resolution: ${w}x${h} (Standard HD/FHD)`);
    passCount++;
  } else {
    console.warn(`[WARN] Resolution ${w}x${h} is below standard 720p`);
    warnCount++;
  }

  // 2. Check Audio & Word Alignment
  const wordsPath = path.join(projectDir, 'words_timeline.json');
  if (fs.existsSync(wordsPath)) {
    const wData = JSON.parse(fs.readFileSync(wordsPath, 'utf-8'));
    const words = wData.words || [];
    if (words.length > 0) {
      console.log(`[PASS] Word-level alignment found: ${words.length} words with exact timestamps`);
      passCount++;

      // Check for silent gaps > 2.0s
      let hasLongGap = false;
      for (let i = 0; i < words.length - 1; i++) {
        const gap = words[i + 1].startMs - words[i].endMs;
        if (gap > 2000) {
          console.warn(`[WARN] Long silence detected (${gap}ms) between '${words[i].word}' and '${words[i+1].word}'`);
          hasLongGap = true;
          warnCount++;
          break;
        }
      }
      if (!hasLongGap) {
        console.log(`[PASS] Pacing & rhythm check: No excessive pauses detected (< 2.0s)`);
        passCount++;
      }
    } else {
      console.warn(`[WARN] words_timeline.json has 0 words`);
      warnCount++;
    }
  } else {
    console.warn(`[WARN] words_timeline.json not found in project folder`);
    warnCount++;
  }

  // 3. Check Visual Beat Placements & Boundaries (Camera-Aware)
  let outOfBounds = false;
  let collisions = [];
  const beats = [];

  // Collect all camera keyframes across storyboard root and scenes
  const allCamKeyframes = [];
  if (storyboard.camera?.keyframes) {
    allCamKeyframes.push(...storyboard.camera.keyframes);
  }
  for (const scene of storyboard.scenes || []) {
    if (scene.camera?.keyframes) {
      allCamKeyframes.push(...scene.camera.keyframes);
    }
  }
  allCamKeyframes.sort((a, b) => a.timeMs - b.timeMs);

  function getCamAtTime(timeMs) {
    if (allCamKeyframes.length === 0) return { x: 960, y: 540, scale: 1.0 };
    if (timeMs <= allCamKeyframes[0].timeMs) return allCamKeyframes[0];
    if (timeMs >= allCamKeyframes[allCamKeyframes.length - 1].timeMs) return allCamKeyframes[allCamKeyframes.length - 1];
    for (let k = 0; k < allCamKeyframes.length - 1; k++) {
      const k1 = allCamKeyframes[k];
      const k2 = allCamKeyframes[k + 1];
      if (timeMs >= k1.timeMs && timeMs <= k2.timeMs) {
        const u = (timeMs - k1.timeMs) / Math.max(1, k2.timeMs - k1.timeMs);
        return {
          x: k1.x + (k2.x - k1.x) * u,
          y: k1.y + (k2.y - k1.y) * u,
          scale: (k1.scale || 1.0) + ((k2.scale || 1.0) - (k1.scale || 1.0)) * u
        };
      }
    }
    return { x: 960, y: 540, scale: 1.0 };
  }

  // 3b. Verify camera coverage across scenes
  let missingCamCoverage = false;
  for (const scene of storyboard.scenes || []) {
    for (const beat of scene.beats || []) {
      beats.push(beat);
      
      // Determine beat bounding box
      let pos = beat.position;
      if (!pos && beat.elements && beat.elements.length > 0) {
        let minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;
        for (const el of beat.elements) {
          const ex = el.x ?? el.from?.[0] ?? 0;
          const ey = el.y ?? el.from?.[1] ?? 0;
          const ew = el.width ?? (el.to ? Math.abs(el.to[0] - ex) : 200);
          const eh = el.height ?? (el.to ? Math.abs(el.to[1] - ey) : 50);
          minX = Math.min(minX, ex);
          minY = Math.min(minY, ey);
          maxX = Math.max(maxX, ex + ew);
          maxY = Math.max(maxY, ey + eh);
        }
        if (minX !== Infinity) {
          pos = { x: minX, y: minY, width: maxX - minX, height: maxY - minY };
        }
      }

      if (pos) {
        const camCenter = getCamAtTime(beat.startMs);
        const scale = camCenter.scale || 1.0;
        const bw = (pos.width || 300) * scale;
        const bh = (pos.height || 300) * scale;

        // Project to screen coordinates
        const relX = 960 + (pos.x - camCenter.x) * scale;
        const relY = 540 + (pos.y - camCenter.y) * scale;

        // Check if drawing happens off-screen (camera freeze / island disconnect)
        if (relX + bw < 0 || relX > w || relY + bh < 0 || relY > h) {
          console.error(`[FAIL] Camera Disconnect: Beat '${beat.beatId}' drawn completely off-screen at (${relX.toFixed(0)}, ${relY.toFixed(0)})! Camera at (${camCenter.x}, ${camCenter.y})`);
          missingCamCoverage = true;
          failCount++;
        } else if (relX < 10 || relY < 10 || relX + bw > w - 10 || relY + bh > h - 10) {
          console.warn(`[WARN] Beat '${beat.beatId}' bounding box (${pos.x}, ${pos.y}, ${bw}, ${bh}) exceeds safe margin (Viewport: ${relX.toFixed(0)}, ${relY.toFixed(0)})`);
          outOfBounds = true;
          warnCount++;
        }
      }
    }
  }

  if (!missingCamCoverage) {
    console.log(`[PASS] Camera Coverage & Anti-Freeze check: All scenes and beats centered in viewport during render`);
    passCount++;
  }

  if (!outOfBounds) {
    console.log(`[PASS] Boundary safety check: All elements within 1920x1080 safe action margins`);
    passCount++;
  }

  // 3c. Check Image & Media Asset Availability on Disk
  let missingAssets = 0;
  let totalAssetsChecked = 0;
  for (const scene of storyboard.scenes || []) {
    for (const beat of scene.beats || []) {
      for (const el of beat.elements || []) {
        if ((el.type === 'photo_reveal' || el.type === 'raster_image') && el.imagePath) {
          totalAssetsChecked++;
          const rootAbs = path.resolve(process.cwd(), el.imagePath);
          const projAbs = path.resolve(projectDir, el.imagePath);
          if (!fs.existsSync(rootAbs) && !fs.existsSync(projAbs)) {
            console.error(`[FAIL] Missing image asset: '${el.imagePath}' in beat '${beat.beatId}'`);
            missingAssets++;
            failCount++;
          }
        }
      }
    }
  }

  if (totalAssetsChecked > 0) {
    if (missingAssets === 0) {
      console.log(`[PASS] Asset availability check: All ${totalAssetsChecked} image layers verified on disk`);
      passCount++;
    } else {
      console.error(`[FAIL] ${missingAssets}/${totalAssetsChecked} image layers missing from disk!`);
    }
  }

  // Check Overlaps between concurrent beats in same scene
  for (let i = 0; i < beats.length; i++) {
    for (let j = i + 1; j < beats.length; j++) {
      const b1 = beats[i];
      const b2 = beats[j];
      // Check if time overlaps
      const tOverlap = (b1.startMs < b2.startMs + b2.durationMs) && (b2.startMs < b1.startMs + b1.durationMs);
      if (tOverlap && b1.position && b2.position) {
        const p1 = b1.position;
        const p2 = b2.position;
        const w1 = p1.width || 250;
        const h1 = p1.height || 250;
        const w2 = p2.width || 250;
        const h2 = p2.height || 250;

        const xIntersect = Math.max(0, Math.min(p1.x + w1, p2.x + w2) - Math.max(p1.x, p2.x));
        const yIntersect = Math.max(0, Math.min(p1.y + h1, p2.y + h2) - Math.max(p1.y, p2.y));
        if (xIntersect * yIntersect > 2000) {
          collisions.push(`${b1.beatId} <-> ${b2.beatId}`);
        }
      }
    }
  }

  if (collisions.length === 0) {
    console.log(`[PASS] Collision & Overlap check: No concurrent bounding-box collisions`);
    passCount++;
  } else {
    console.warn(`[WARN] Potential layout overlap between: ${collisions.join(', ')}`);
    warnCount++;
  }

  // 4. Check Output Video File if rendered
  const outMp4 = path.join(projectDir, 'output.mp4');
  if (fs.existsSync(outMp4)) {
    const stats = fs.statSync(outMp4);
    if (stats.size > 100000) {
      console.log(`[PASS] Video output integrity check: ${outMp4} (${(stats.size / 1024 / 1024).toFixed(2)} MB)`);
      passCount++;
    } else {
      console.error(`[FAIL] Video output file is suspiciously small: ${stats.size} bytes`);
      failCount++;
    }
  }

  console.log(`\n-------------------------------------------------------`);
  console.log(`[SUMMARY] Passed: ${passCount} | Warnings: ${warnCount} | Failures: ${failCount}`);
  console.log(`-------------------------------------------------------\n`);

  if (failCount > 0) {
    process.exit(1);
  }
}

const target = process.argv[2] || 'projects/demo-project/storyboard.json';
runQACheck(target);
