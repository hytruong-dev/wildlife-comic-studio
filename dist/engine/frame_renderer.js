import fs from 'fs';
import { execSync } from 'child_process';
import { optimizeStrokeOrder } from '../compiler/stroke_sorter.js';
import { convertTextToHandwritingStrokes } from '../compiler/text_to_svg_paths.js';
import { compileRoughRectangle, compileRoughCircle, compileRoughArrow } from '../compiler/rough_doodle_compiler.js';
import { createStickCharacter, createThreeBucketsChart, createRoughBarChart, createRoughLucideIcon, createLeftHandRuleModel, createElectromagnetSetup, createFBICardDiagram, createMotorPrincipleDiagram, createLoudspeakerDiagram, createSleepCycleSineWaveDiagram, createFormulaBoardDiagram, createClockTimelineBar, createSnoozeBanDiagram } from '../compiler/visual_primitives.js';
/**
 * Compiles a visual beat into scheduled CompiledStrokes according to Algorithm 1
 */
export function compileBeatStrokes(beat) {
    const rawStrokes = [];
    const basePos = beat.position || { x: 0, y: 0 };
    for (let elemIdx = 0; elemIdx < beat.elements.length; elemIdx++) {
        const elem = beat.elements[elemIdx];
        const elX = elem.x ?? basePos.x;
        const elY = elem.y ?? basePos.y;
        switch (elem.type) {
            case 'handwritten_text':
                if (elem.text) {
                    rawStrokes.push(...convertTextToHandwritingStrokes(elem.text, elX, elY, {
                        fontSize: elem.fontSize || 42,
                        color: elem.color || elem.strokeColor || '#2C2A29',
                        strokeWidth: elem.strokeWidth || 0.5
                    }));
                }
                break;
            case 'rough_shape':
                if (elem.shape?.startsWith('stick_character_')) {
                    const emotion = elem.shape.replace('stick_character_', '');
                    rawStrokes.push(...createStickCharacter(emotion, elX, elY, 1.0, {
                        strokeColor: elem.strokeColor,
                        fillColor: elem.fillColor,
                        strokeWidth: elem.strokeWidth
                    }));
                }
                else if (elem.shape === 'rectangle') {
                    rawStrokes.push(...compileRoughRectangle(elX, elY, elem.width || 120, elem.height || 80, {
                        strokeColor: elem.strokeColor,
                        fillColor: elem.fillColor,
                        fillStyle: elem.fillStyle,
                        strokeWidth: elem.strokeWidth
                    }));
                }
                else if (elem.shape === 'circle') {
                    rawStrokes.push(...compileRoughCircle(elX, elY, (elem.width || 80) / 2, {
                        strokeColor: elem.strokeColor,
                        fillColor: elem.fillColor,
                        fillStyle: elem.fillStyle,
                        strokeWidth: elem.strokeWidth
                    }));
                }
                break;
            case 'rough_arrow':
                if (elem.from && elem.to) {
                    rawStrokes.push(...compileRoughArrow(elem.from[0], elem.from[1], elem.to[0], elem.to[1], {
                        strokeColor: elem.strokeColor || '#2B6CB0',
                        strokeWidth: elem.strokeWidth || 4.0,
                        curved: elem.curved,
                        curveOffset: elem.curveOffset
                    }));
                }
                break;
            case 'rough_chart_buckets':
                rawStrokes.push(...createThreeBucketsChart(elX, elY, elem.labels, elem.colors));
                break;
            case 'rough_bar_chart':
                if (elem.data) {
                    rawStrokes.push(...createRoughBarChart(elX, elY, elem.width || 400, elem.height || 260, elem.data));
                }
                break;
            case 'lucide_icon':
            case 'rough_lucide_icon':
                if (elem.icon) {
                    rawStrokes.push(...createRoughLucideIcon(elem.icon, elX, elY, elem.width || 80, {
                        strokeColor: elem.strokeColor || '#2C2A29',
                        fillColor: elem.fillColor,
                        strokeWidth: elem.strokeWidth
                    }));
                }
                break;
            case 'physics_hand_rule':
                rawStrokes.push(...createLeftHandRuleModel(elX, elY, elem.width ? elem.width / 400 : 1.0, elem));
                break;
            case 'physics_electromagnet':
                rawStrokes.push(...createElectromagnetSetup(elX, elY, elem.width ? elem.width / 500 : 1.0, elem));
                break;
            case 'physics_fbi_card':
                rawStrokes.push(...createFBICardDiagram(elX, elY, elem.width ? elem.width / 600 : 1.0));
                break;
            case 'physics_motor':
                rawStrokes.push(...createMotorPrincipleDiagram(elX, elY, elem.width ? elem.width / 500 : 1.0, elem));
                break;
            case 'physics_loudspeaker':
                rawStrokes.push(...createLoudspeakerDiagram(elX, elY, elem.width ? elem.width / 500 : 1.0, elem));
                break;
            case 'sleep_cycle_sine_wave':
                rawStrokes.push(...createSleepCycleSineWaveDiagram(elX, elY, elem.width ? elem.width / 900 : 1.0, elem));
                break;
            case 'formula_board':
                rawStrokes.push(...createFormulaBoardDiagram(elX, elY, elem.width ? elem.width / 920 : 1.0));
                break;
            case 'clock_timeline_bar':
                rawStrokes.push(...createClockTimelineBar(elX, elY, elem.width ? elem.width / 880 : 1.0));
                break;
            case 'snooze_ban':
                rawStrokes.push(...createSnoozeBanDiagram(elX, elY, elem.width ? elem.width / 700 : 1.0));
                break;
            case 'photo_reveal':
                {
                    const w = elem.width || 400;
                    const h = elem.height || 300;
                    const sweepParts = [];
                    const isText = beat.beatId.includes('_text') ||
                        (elem.imagePath && (elem.imagePath.includes('_text') || elem.imagePath.includes('title')));
                    if (isText) {
                        // Write along horizontal lines across the text box
                        const numLines = Math.max(2, Math.min(8, Math.round(h / 32)));
                        for (let row = 0; row < numLines; row++) {
                            const yRow = elY + (row + 0.5) * (h / numLines);
                            sweepParts.push(`M ${elX + 15} ${yRow} L ${elX + w - 15} ${yRow}`);
                        }
                    }
                    else {
                        // Sweep zigzag across the subject / scenery box
                        const steps = Math.max(4, Math.min(10, Math.round(h / 40)));
                        for (let row = 0; row < steps; row++) {
                            const yRow = elY + (row + 0.5) * (h / steps);
                            const xLeft = elX + 15;
                            const xRight = elX + w - 15;
                            if (row % 2 === 0) {
                                sweepParts.push(`M ${xLeft} ${yRow} L ${xRight} ${yRow}`);
                            }
                            else {
                                sweepParts.push(`M ${xRight} ${yRow} L ${xLeft} ${yRow}`);
                            }
                        }
                    }
                    rawStrokes.push({
                        id: `sweep_${beat.beatId}_${elemIdx}`,
                        d: sweepParts.join(' '),
                        length: w * 6,
                        startPoint: { x: elX + 15, y: elY + 15 },
                        endPoint: { x: elX + w - 15, y: elY + h - 15 },
                        strokeColor: 'transparent',
                        strokeWidth: 1.0,
                        isFillStroke: true,
                        priority: 5
                    });
                }
                break;
            case 'raster_image':
                if (elem.imagePath && fs.existsSync(elem.imagePath)) {
                    const outJson = elem.imagePath.replace(/\.(png|jpg|jpeg)$/i, '_strokes.json');
                    if (!fs.existsSync(outJson)) {
                        const w = elem.width || 400;
                        const h = elem.height || 400;
                        execSync(`python src/compiler/raster_stream_extractor.py --image "${elem.imagePath}" --output "${outJson}" --x ${elX} --y ${elY} --width ${w} --height ${h}`);
                    }
                    if (fs.existsSync(outJson)) {
                        const content = JSON.parse(fs.readFileSync(outJson, 'utf-8'));
                        rawStrokes.push(...content);
                    }
                }
                break;
        }
    }
    if (rawStrokes.length === 0)
        return [];
    // Sort strokes according to TSP & priority
    const sorted = optimizeStrokeOrder(rawStrokes);
    // Divide into ink outlines vs color fill strokes (Algorithm 1)
    const inkStrokes = sorted.filter(s => !s.isFillStroke);
    const fillStrokes = sorted.filter(s => s.isFillStroke);
    const inkRatio = beat.inkRatio ?? 0.72;
    const totalDuration = Math.max(200, beat.durationMs);
    let inkDuration = 0;
    let fillDuration = 0;
    if (inkStrokes.length > 0 && fillStrokes.length > 0) {
        inkDuration = totalDuration * inkRatio;
        fillDuration = totalDuration * (1 - inkRatio);
    }
    else if (inkStrokes.length > 0) {
        inkDuration = totalDuration;
        fillDuration = 0;
    }
    else {
        inkDuration = 0;
        fillDuration = totalDuration;
    }
    const result = [];
    // Sub-allocate ink strokes
    const scheduleGroup = (strokes, groupStartMs, groupDurationMs) => {
        if (strokes.length === 0)
            return;
        const penLiftMs = Math.min(60, (groupDurationMs * 0.15) / Math.max(1, strokes.length - 1));
        const totalLiftTime = penLiftMs * Math.max(0, strokes.length - 1);
        const drawingTime = Math.max(50, groupDurationMs - totalLiftTime);
        const gamma = 0.7;
        const weights = strokes.map(s => Math.pow(Math.max(1, s.length), gamma));
        const totalWeight = weights.reduce((acc, w) => acc + w, 0);
        let curTime = groupStartMs;
        for (let i = 0; i < strokes.length; i++) {
            const s = strokes[i];
            const strokeDt = (weights[i] / totalWeight) * drawingTime;
            const startMs = curTime;
            const endMs = startMs + strokeDt;
            result.push({
                id: s.id,
                d: s.d,
                length: s.length,
                startMs,
                endMs,
                strokeColor: s.strokeColor,
                strokeWidth: s.strokeWidth,
                isFillStroke: s.isFillStroke,
                startPoint: s.startPoint,
                endPoint: s.endPoint
            });
            curTime = endMs + penLiftMs;
        }
    };
    scheduleGroup(inkStrokes, beat.startMs, inkDuration);
    scheduleGroup(fillStrokes, beat.startMs + inkDuration, fillDuration);
    return result;
}
/**
 * Compiles an entire Storyboard into all strokes, camera keyframes, and motion logs
 */
export function compileStoryboard(storyboard) {
    const allStrokes = [];
    const cameraKeyframes = [];
    const subtitles = [];
    const allImages = [];
    // Support both root storyboard.camera.keyframes and per-scene scene.camera.keyframes
    if (storyboard.camera?.keyframes && storyboard.camera.keyframes.length > 0) {
        cameraKeyframes.push(...storyboard.camera.keyframes);
    }
    else {
        for (const scene of storyboard.scenes) {
            if (scene.camera?.keyframes) {
                cameraKeyframes.push(...scene.camera.keyframes);
            }
        }
    }
    for (const scene of storyboard.scenes) {
        if (scene.subtitles) {
            subtitles.push(...scene.subtitles);
        }
        for (const beat of scene.beats) {
            for (const elem of beat.elements) {
                if (elem.type === 'photo_reveal' && elem.imagePath) {
                    const elX = elem.x ?? beat.position?.x ?? 100;
                    const elY = elem.y ?? beat.position?.y ?? 100;
                    const w = elem.width ?? 400;
                    const h = elem.height ?? 300;
                    allImages.push({
                        id: `img_${beat.beatId}_${allImages.length}`,
                        href: elem.imagePath,
                        x: elX,
                        y: elY,
                        width: w,
                        height: h,
                        startMs: beat.startMs,
                        endMs: beat.startMs + beat.durationMs,
                        stickerBorder: true
                    });
                }
            }
            const beatStrokes = compileBeatStrokes(beat);
            allStrokes.push(...beatStrokes);
        }
    }
    // Sort all compiled strokes by startMs
    allStrokes.sort((a, b) => a.startMs - b.startMs);
    return {
        storyboard,
        allStrokes,
        allImages,
        cameraKeyframes: cameraKeyframes.sort((a, b) => a.timeMs - b.timeMs),
        subtitles: subtitles.sort((a, b) => a.startMs - b.startMs)
    };
}
