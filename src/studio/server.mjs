import http from 'http';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { compileStoryboard } from '../../dist/engine/frame_renderer.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const rootDir = path.resolve(__dirname, '../..');

const mimeTypes = {
  '.html': 'text/html; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.mjs': 'text/javascript; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.wav': 'audio/wav',
  '.mp3': 'audio/mpeg',
  '.mp4': 'video/mp4',
  '.ttf': 'font/ttf',
  '.svg': 'image/svg+xml'
};

const server = http.createServer(async (req, res) => {
  const urlObj = new URL(req.url, `http://${req.headers.host || 'localhost:3000'}`);
  let reqPath = decodeURI(urlObj.pathname);

  // Default route
  if (reqPath === '/' || reqPath === '/studio') {
    reqPath = '/src/studio/preview_editor.html';
  }

  // API 1: List all available projects
  if (reqPath === '/api/projects') {
    const projectsDir = path.join(rootDir, 'projects');
    const projectList = [];

    if (fs.existsSync(projectsDir)) {
      const dirs = fs.readdirSync(projectsDir).filter(f => {
        try {
          return fs.statSync(path.join(projectsDir, f)).isDirectory();
        } catch {
          return false;
        }
      });

      for (const d of dirs) {
        const pDir = path.join(projectsDir, d);
        const sbPath = path.join(pDir, 'storyboard.json');
        const mp4Path = path.join(pDir, 'output.mp4');
        const wordsPath = path.join(pDir, 'words_timeline.json');

        // Look for audio narration
        const possibleAudios = ['master_audio.wav', 'master_voice.wav', 'narration.wav', 'audio.mp3'];
        let audioFile = null;
        for (const a of possibleAudios) {
          if (fs.existsSync(path.join(pDir, a))) {
            audioFile = `/projects/${d}/${a}`;
            break;
          }
        }

        let title = d;
        let durationMs = 0;
        let beatCount = 0;
        let sceneCount = 0;

        if (fs.existsSync(wordsPath)) {
          try {
            const w = JSON.parse(fs.readFileSync(wordsPath, 'utf-8'));
            if (w.totalDurationMs) durationMs = w.totalDurationMs;
          } catch {}
        }

        if (fs.existsSync(sbPath)) {
          try {
            const sb = JSON.parse(fs.readFileSync(sbPath, 'utf-8'));
            if (sb.title) title = sb.title;
            sceneCount = (sb.scenes || []).length;
            for (const s of (sb.scenes || [])) {
              beatCount += (s.beats || []).length;
              if (durationMs === 0) {
                for (const b of (s.beats || [])) {
                  durationMs = Math.max(durationMs, (b.startMs || 0) + (b.durationMs || 0));
                }
              }
            }
          } catch {}
        }

        const hasMp4 = fs.existsSync(mp4Path);
        const mp4Size = hasMp4 ? fs.statSync(mp4Path).size : 0;

        projectList.push({
          id: d,
          title,
          hasStoryboard: fs.existsSync(sbPath),
          hasMp4,
          mp4Size,
          mp4SizeMB: (mp4Size / (1024 * 1024)).toFixed(2),
          videoUrl: hasMp4 ? `/projects/${d}/output.mp4` : null,
          audioUrl: audioFile,
          durationMs,
          sceneCount,
          beatCount
        });
      }
    }

    // Sort projects: lions and projects with video/storyboards first
    projectList.sort((a, b) => {
      if (a.hasMp4 !== b.hasMp4) return b.hasMp4 ? 1 : -1;
      return b.durationMs - a.durationMs;
    });

    res.writeHead(200, {
      'Content-Type': 'application/json; charset=utf-8',
      'Access-Control-Allow-Origin': '*'
    });
    res.end(JSON.stringify({ success: true, projects: projectList }, null, 2));
    return;
  }

  // API 2: Compile storyboard for a project on demand
  if (reqPath === '/api/compile') {
    const projectId = urlObj.searchParams.get('project');
    if (!projectId) {
      res.writeHead(400, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ error: 'Missing ?project= parameter' }));
      return;
    }

    const pDir = path.join(rootDir, 'projects', projectId);
    const sbPath = path.join(pDir, 'storyboard.json');

    if (!fs.existsSync(sbPath)) {
      res.writeHead(404, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ error: `Storyboard not found for project: ${projectId}` }));
      return;
    }

    try {
      const storyboard = JSON.parse(fs.readFileSync(sbPath, 'utf-8'));
      const compiled = compileStoryboard(storyboard);

      // Check words timeline duration
      const wordsPath = path.join(pDir, 'words_timeline.json');
      let totalDurationMs = 0;
      if (fs.existsSync(wordsPath)) {
        try {
          const w = JSON.parse(fs.readFileSync(wordsPath, 'utf-8'));
          if (w.totalDurationMs) totalDurationMs = w.totalDurationMs;
        } catch {}
      }

      if (totalDurationMs === 0) {
        for (const s of compiled.allStrokes) {
          totalDurationMs = Math.max(totalDurationMs, s.endMs + 1000);
        }
        for (const sub of (compiled.subtitles || [])) {
          totalDurationMs = Math.max(totalDurationMs, sub.endMs + 800);
        }
      }

      // Convert image layers to Base64 data URIs for 100% reliable local preview
      if (compiled.allImages) {
        for (const img of compiled.allImages) {
          if (img.href && !img.href.startsWith('data:')) {
            let absImgPath = path.isAbsolute(img.href) ? img.href : path.resolve(rootDir, img.href);
            if (!fs.existsSync(absImgPath)) {
              absImgPath = path.resolve(pDir, img.href);
            }
            if (fs.existsSync(absImgPath)) {
              const ext = path.extname(absImgPath).toLowerCase().replace('.', '');
              const mime = ext === 'svg' ? 'image/svg+xml' : ('image/' + (ext === 'jpg' ? 'jpeg' : ext));
              const b64 = fs.readFileSync(absImgPath).toString('base64');
              img.href = `data:${mime};base64,${b64}`;
            }
          }
        }
      }

      res.writeHead(200, {
        'Content-Type': 'application/json; charset=utf-8',
        'Access-Control-Allow-Origin': '*'
      });
      res.end(JSON.stringify({
        success: true,
        projectId,
        totalDurationMs,
        data: compiled
      }));
    } catch (err) {
      res.writeHead(500, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ error: err.message, stack: err.stack }));
    }
    return;
  }

  // API 3: Get memory bank status
  if (reqPath === '/api/memory') {
    try {
      const tastePath = path.join(rootDir, '.agent_memory', 'director_taste.md');
      const lessonsPath = path.join(rootDir, '.agent_memory', 'lessons_learned.md');
      const dictPath = path.join(rootDir, '.agent_memory', 'visual_metaphor_dictionary.json');
      const skillsDir = path.join(rootDir, '.agents', 'skills', 'learned');

      let tasteCount = 0;
      if (fs.existsSync(tastePath)) {
        const text = fs.readFileSync(tastePath, 'utf-8');
        tasteCount = (text.match(/\[TASTE-\d+\]/g) || []).length;
      }

      let lessonsCount = 0;
      if (fs.existsSync(lessonsPath)) {
        const text = fs.readFileSync(lessonsPath, 'utf-8');
        lessonsCount = (text.match(/\[LESSON-\d+\]/g) || []).length;
      }

      let metaphorCount = 0;
      if (fs.existsSync(dictPath)) {
        const dict = JSON.parse(fs.readFileSync(dictPath, 'utf-8'));
        metaphorCount = Object.keys(dict.metaphors || {}).length;
      }

      let skills = [];
      if (fs.existsSync(skillsDir)) {
        skills = fs.readdirSync(skillsDir).filter(f => {
          try {
            return fs.statSync(path.join(skillsDir, f)).isDirectory();
          } catch {
            return false;
          }
        });
      }

      res.writeHead(200, {
        'Content-Type': 'application/json; charset=utf-8',
        'Access-Control-Allow-Origin': '*'
      });
      res.end(JSON.stringify({
        success: true,
        directorTasteRules: tasteCount,
        lessonsLearned: lessonsCount,
        visualMetaphors: metaphorCount,
        learnedSkills: skills
      }, null, 2));
    } catch (err) {
      res.writeHead(500, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ error: err.message }));
    }
    return;
  }

  // Static File Serving with HTTP Range support for video/audio
  const filePath = path.join(rootDir, reqPath);

  if (fs.existsSync(filePath) && fs.statSync(filePath).isFile()) {
    const ext = path.extname(filePath).toLowerCase();
    const contentType = mimeTypes[ext] || 'application/octet-stream';
    const stat = fs.statSync(filePath);

    // Range requests for video/audio seeking
    const range = req.headers.range;
    if (range && (ext === '.mp4' || ext === '.wav' || ext === '.mp3')) {
      const parts = range.replace(/bytes=/, '').split('-');
      const start = parseInt(parts[0], 10);
      const end = parts[1] ? parseInt(parts[1], 10) : stat.size - 1;
      const chunkSize = (end - start) + 1;

      res.writeHead(206, {
        'Content-Range': `bytes ${start}-${end}/${stat.size}`,
        'Accept-Ranges': 'bytes',
        'Content-Length': chunkSize,
        'Content-Type': contentType,
        'Access-Control-Allow-Origin': '*'
      });
      fs.createReadStream(filePath, { start, end }).pipe(res);
      return;
    }

    res.writeHead(200, {
      'Content-Type': contentType,
      'Content-Length': stat.size,
      'Accept-Ranges': 'bytes',
      'Access-Control-Allow-Origin': '*'
    });
    fs.createReadStream(filePath).pipe(res);
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' });
    res.end(`404 Not Found: ${reqPath}`);
  }
});

const PORT = 3000;
server.listen(PORT, () => {
  console.log(`\n======================================================`);
  console.log(`  🎬 AI Whiteboard Animation Preview Studio Running!`);
  console.log(`  👉 Open URL: http://localhost:${PORT}`);
  console.log(`  📂 Active Projects API: http://localhost:${PORT}/api/projects`);
  console.log(`  🧠 Memory Bank API: http://localhost:${PORT}/api/memory`);
  console.log(`======================================================\n`);
});
