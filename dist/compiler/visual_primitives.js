import fs from 'fs';
import path from 'path';
// @ts-ignore
import roughModule from 'roughjs/bundled/rough.cjs.js';
import { compileRoughRectangle, compileRoughCircle, compileRoughLine, compileRoughArrow, parseSvgPathMetrics } from './rough_doodle_compiler.js';
import { convertTextToHandwritingStrokes } from './text_to_svg_paths.js';
// -------------------------------------------------------------
// 1. CHARACTER EXPRESSIONS (Parametric Hand-Drawn Stick Figures)
// -------------------------------------------------------------
export function createStickCharacter(type, x, y, scale = 1.0, options = {}) {
    const strokes = [];
    const sc = options.strokeColor || '#2C2A29';
    const sw = options.strokeWidth || 4.0;
    const s = scale;
    // Head center (x, y)
    const headRadius = 32 * s;
    strokes.push(...compileRoughCircle(x, y, headRadius, { ...options, strokeColor: sc, strokeWidth: sw }));
    // Face details depending on emotion
    if (type === 'confused') {
        // Confused spiral/cross eyes
        strokes.push(...compileRoughLine(x - 14 * s, y - 8 * s, x - 6 * s, y - 8 * s, options));
        strokes.push(...compileRoughLine(x + 6 * s, y - 10 * s, x + 14 * s, y - 4 * s, options));
        // Wavy / slanted confused mouth
        strokes.push(...compileRoughLine(x - 12 * s, y + 14 * s, x, y + 8 * s, options));
        strokes.push(...compileRoughLine(x, y + 8 * s, x + 12 * s, y + 16 * s, options));
        // Sweat drop
        strokes.push(...compileRoughCircle(x + 36 * s, y - 12 * s, 4 * s, { ...options, fillColor: '#3182CE' }));
    }
    else if (type === 'happy') {
        // Upward arc smile & happy arc eyes
        strokes.push(...compileRoughCircle(x - 10 * s, y - 6 * s, 3 * s, { ...options, fillColor: sc }));
        strokes.push(...compileRoughCircle(x + 10 * s, y - 6 * s, 3 * s, { ...options, fillColor: sc }));
        strokes.push(...compileRoughArrow(x - 14 * s, y + 10 * s, x + 14 * s, y + 10 * s, { ...options, curved: true, curveOffset: -12 * s }));
    }
    else if (type === 'thinking') {
        // Looking up and thinking
        strokes.push(...compileRoughCircle(x - 8 * s, y - 10 * s, 4 * s, { ...options, fillColor: sc }));
        strokes.push(...compileRoughCircle(x + 8 * s, y - 10 * s, 4 * s, { ...options, fillColor: sc }));
        strokes.push(...compileRoughLine(x - 6 * s, y + 12 * s, x + 8 * s, y + 10 * s, options));
        // Thought bubbles
        strokes.push(...compileRoughCircle(x + 38 * s, y - 30 * s, 6 * s, options));
        strokes.push(...compileRoughCircle(x + 52 * s, y - 48 * s, 10 * s, options));
        strokes.push(...compileRoughCircle(x + 72 * s, y - 70 * s, 16 * s, { ...options, fillColor: '#FAF089' }));
    }
    else {
        // Default neutral face
        strokes.push(...compileRoughCircle(x - 10 * s, y - 6 * s, 3 * s, { ...options, fillColor: sc }));
        strokes.push(...compileRoughCircle(x + 10 * s, y - 6 * s, 3 * s, { ...options, fillColor: sc }));
        strokes.push(...compileRoughLine(x - 10 * s, y + 12 * s, x + 10 * s, y + 12 * s, options));
    }
    // Torso
    const neckY = y + headRadius;
    const hipY = neckY + 90 * s;
    strokes.push(...compileRoughLine(x, neckY, x, hipY, { ...options, strokeWidth: sw * 1.1 }));
    // Arms & Legs based on posture
    if (type === 'confused') {
        // Hands on head / temples
        strokes.push(...compileRoughLine(x, neckY + 20 * s, x - 40 * s, neckY + 10 * s, options));
        strokes.push(...compileRoughLine(x - 40 * s, neckY + 10 * s, x - 26 * s, y - 5 * s, options));
        strokes.push(...compileRoughLine(x, neckY + 20 * s, x + 40 * s, neckY + 10 * s, options));
        strokes.push(...compileRoughLine(x + 40 * s, neckY + 10 * s, x + 26 * s, y - 5 * s, options));
        // Legs slightly pigeon-toed
        strokes.push(...compileRoughLine(x, hipY, x - 28 * s, hipY + 80 * s, options));
        strokes.push(...compileRoughLine(x - 28 * s, hipY + 80 * s, x - 18 * s, hipY + 85 * s, options));
        strokes.push(...compileRoughLine(x, hipY, x + 28 * s, hipY + 80 * s, options));
        strokes.push(...compileRoughLine(x + 28 * s, hipY + 80 * s, x + 18 * s, hipY + 85 * s, options));
    }
    else if (type === 'happy') {
        // Arms raised in V-triumph
        strokes.push(...compileRoughLine(x, neckY + 18 * s, x - 45 * s, neckY - 25 * s, options));
        strokes.push(...compileRoughLine(x, neckY + 18 * s, x + 45 * s, neckY - 25 * s, options));
        // Legs standing firm
        strokes.push(...compileRoughLine(x, hipY, x - 30 * s, hipY + 85 * s, options));
        strokes.push(...compileRoughLine(x, hipY, x + 30 * s, hipY + 85 * s, options));
    }
    else if (type === 'pointing') {
        // Left arm down, right arm pointing forward towards right
        strokes.push(...compileRoughLine(x, neckY + 20 * s, x - 25 * s, neckY + 65 * s, options));
        strokes.push(...compileRoughLine(x, neckY + 20 * s, x + 65 * s, neckY + 10 * s, options));
        strokes.push(...compileRoughLine(x + 65 * s, neckY + 10 * s, x + 85 * s, neckY + 8 * s, options));
        // Legs
        strokes.push(...compileRoughLine(x, hipY, x - 25 * s, hipY + 85 * s, options));
        strokes.push(...compileRoughLine(x, hipY, x + 25 * s, hipY + 85 * s, options));
    }
    else {
        // Thinking posture: one arm to chin, other supporting elbow
        strokes.push(...compileRoughLine(x, neckY + 20 * s, x - 25 * s, neckY + 55 * s, options));
        strokes.push(...compileRoughLine(x - 25 * s, neckY + 55 * s, x, neckY + 55 * s, options));
        strokes.push(...compileRoughLine(x, neckY + 20 * s, x + 25 * s, neckY + 45 * s, options));
        strokes.push(...compileRoughLine(x + 25 * s, neckY + 45 * s, x + 12 * s, y + 16 * s, options));
        // Legs
        strokes.push(...compileRoughLine(x, hipY, x - 24 * s, hipY + 85 * s, options));
        strokes.push(...compileRoughLine(x, hipY, x + 24 * s, hipY + 85 * s, options));
    }
    return strokes;
}
// -------------------------------------------------------------
// 2. THREE BUCKETS / JARS CHART (50 / 30 / 20 Budget Rule)
// -------------------------------------------------------------
export function createThreeBucketsChart(startX, startY, labels = ["50% Thiết yếu", "30% Mong muốn", "20% Tiết kiệm"], colors = ["#3182CE", "#DD6B20", "#38A169"]) {
    const strokes = [];
    const jarWidth = 140;
    const jarHeight = 170;
    const gap = 55;
    labels.forEach((label, idx) => {
        const x = startX + idx * (jarWidth + gap);
        const y = startY;
        const color = colors[idx % colors.length];
        // Jar Rim
        strokes.push(...compileRoughRectangle(x - 8, y, jarWidth + 16, 22, {
            strokeColor: '#2C2A29',
            fillColor: '#EDF2F7',
            fillStyle: 'solid'
        }));
        // Jar Body with Hachure Fill
        strokes.push(...compileRoughRectangle(x, y + 22, jarWidth, jarHeight, {
            strokeColor: '#2C2A29',
            fillColor: color,
            fillStyle: 'hachure',
            fillWeight: 2.2,
            hachureGap: 7.0
        }));
        // Vietnamese Handwriting Label under each jar
        strokes.push(...convertTextToHandwritingStrokes(label, x - 10, y + jarHeight + 55, {
            fontSize: 24,
            color: color,
            strokeWidth: 2.4
        }));
    });
    return strokes;
}
// -------------------------------------------------------------
// 3. HAND-DRAWN BAR CHART
// -------------------------------------------------------------
export function createRoughBarChart(x, y, w, h, data) {
    const strokes = [];
    // Axes (X and Y)
    strokes.push(...compileRoughLine(x, y, x, y + h, { strokeColor: '#2C2A29', strokeWidth: 4 }));
    strokes.push(...compileRoughLine(x, y + h, x + w, y + h, { strokeColor: '#2C2A29', strokeWidth: 4 }));
    if (data.length === 0)
        return strokes;
    const maxVal = Math.max(...data.map(d => d.value), 1);
    const barGap = 25;
    const barWidth = Math.max(30, (w - barGap * (data.length + 1)) / data.length);
    data.forEach((item, idx) => {
        const barH = (item.value / maxVal) * (h - 40);
        const barX = x + barGap + idx * (barWidth + barGap);
        const barY = (y + h) - barH;
        const barColor = item.color || '#3182CE';
        // Sketched bar
        strokes.push(...compileRoughRectangle(barX, barY, barWidth, barH, {
            strokeColor: '#2C2A29',
            fillColor: barColor,
            fillStyle: 'hachure',
            fillWeight: 2.0
        }));
        // Label under bar
        strokes.push(...convertTextToHandwritingStrokes(item.label, barX - 5, y + h + 32, {
            fontSize: 22,
            color: '#2C2A29'
        }));
    });
    return strokes;
}
// -------------------------------------------------------------
// 4. LUCIDE SVG ICON TO ROUGH DOODLE COMPILER
// -------------------------------------------------------------
export function createRoughLucideIcon(iconName, targetX, targetY, size = 100, options = {}) {
    const strokes = [];
    const iconPath = path.resolve(`node_modules/lucide-static/icons/${iconName}.svg`);
    if (!fs.existsSync(iconPath)) {
        console.warn(`[WARN] Lucide icon '${iconName}' not found, falling back to circle marker`);
        return compileRoughCircle(targetX + size / 2, targetY + size / 2, size / 2, options);
    }
    const svgContent = fs.readFileSync(iconPath, 'utf-8');
    const scale = size / 24.0; // Lucide icons have 24x24 viewBox
    // Parse path elements d="..."
    const pathRegex = /<path[^>]*d="([^"]+)"/g;
    let match;
    while ((match = pathRegex.exec(svgContent)) !== null) {
        const rawD = match[1];
        // Compile rough path in 0..24 coordinate space
        const ro = {
            roughness: options.roughness ?? 1.2,
            bowing: options.bowing ?? 1.0,
            stroke: options.strokeColor ?? '#2C2A29',
            strokeWidth: options.strokeWidth ?? 3.0
        };
        if (options.fillColor) {
            ro.fill = options.fillColor;
            ro.fillStyle = options.fillStyle ?? 'hachure';
            ro.fillWeight = options.fillWeight ?? 1.8;
        }
        // @ts-ignore
        const drawable = roughModule.generator().path(rawD, ro);
        for (let sIdx = 0; sIdx < drawable.sets.length; sIdx++) {
            const set = drawable.sets[sIdx];
            // Scale and translate op coordinates
            for (const op of set.ops) {
                op.data = op.data.map((val, idx) => idx % 2 === 0 ? targetX + val * scale : targetY + val * scale);
            }
            // @ts-ignore
            const d = roughModule.generator().opsToPath(set);
            if (!d || d.length === 0)
                continue;
            const isFill = set.type === 'fillSketch' || set.type === 'fillPath';
            const metrics = parseSvgPathMetrics(d);
            strokes.push({
                id: `icon_${iconName}_${sIdx}_${Math.random().toString(36).substring(2, 7)}`,
                d,
                length: metrics.length,
                startPoint: metrics.start,
                endPoint: metrics.end,
                strokeColor: isFill ? (options.fillColor || '#E86A58') : (options.strokeColor || '#2C2A29'),
                strokeWidth: isFill ? Math.max(1.5, (options.strokeWidth || 3.0) * 0.7) : (options.strokeWidth || 3.0),
                isFillStroke: isFill,
                priority: isFill ? (options.priority ?? 0) + 50 : (options.priority ?? 0)
            });
        }
    }
    // Parse circle elements <circle cx=".." cy=".." r=".."/>
    const circleRegex = /<circle[^>]*cx="([^"]+)"[^>]*cy="([^"]+)"[^>]*r="([^"]+)"/g;
    while ((match = circleRegex.exec(svgContent)) !== null) {
        const cx = targetX + parseFloat(match[1]) * scale;
        const cy = targetY + parseFloat(match[2]) * scale;
        const r = parseFloat(match[3]) * scale;
        strokes.push(...compileRoughCircle(cx, cy, r, options));
    }
    // Parse rect elements <rect x=".." y=".." width=".." height=".." rx=".."/>
    const rectRegex = /<rect[^>]*x="([^"]+)"[^>]*y="([^"]+)"[^>]*width="([^"]+)"[^>]*height="([^"]+)"/g;
    while ((match = rectRegex.exec(svgContent)) !== null) {
        const rx = targetX + parseFloat(match[1]) * scale;
        const ry = targetY + parseFloat(match[2]) * scale;
        const rw = parseFloat(match[3]) * scale;
        const rh = parseFloat(match[4]) * scale;
        strokes.push(...compileRoughRectangle(rx, ry, rw, rh, options));
    }
    // Parse line elements <line x1=".." y1=".." x2=".." y2=".."/>
    const lineRegex = /<line[^>]*x1="([^"]+)"[^>]*y1="([^"]+)"[^>]*x2="([^"]+)"[^>]*y2="([^"]+)"/g;
    while ((match = lineRegex.exec(svgContent)) !== null) {
        const x1 = targetX + parseFloat(match[1]) * scale;
        const y1 = targetY + parseFloat(match[2]) * scale;
        const x2 = targetX + parseFloat(match[3]) * scale;
        const y2 = targetY + parseFloat(match[4]) * scale;
        strokes.push(...compileRoughLine(x1, y1, x2, y2, options));
    }
    return strokes;
}
// -------------------------------------------------------------
// 5. PHYSICS & ELECTROMAGNETISM: LEFT-HAND RULE PRIMITIVES
// -------------------------------------------------------------
/**
 * Procedural Hand-Drawn Left-Hand Rule Anatomical Diagram
 * Features authentic left hand anatomy, vector arrows (F, B, I) and formula
 */
export function createLeftHandRuleModel(x, y, scale = 1.0, options = {}) {
    const strokes = [];
    const s = scale;
    // --- 1. Realistic Left Hand Outline (Palmar View) ---
    const wristLeftX = x + 25 * s;
    const wristRightX = x + 95 * s;
    const wristY = y + 155 * s;
    const wristBottomY = y + 215 * s;
    // Wrist contour
    strokes.push(...compileRoughLine(wristLeftX, wristY, wristLeftX - 5 * s, wristBottomY, { strokeColor: '#2C2A29', strokeWidth: 3.2 }));
    strokes.push(...compileRoughLine(wristRightX, wristY, wristRightX + 5 * s, wristBottomY, { strokeColor: '#2C2A29', strokeWidth: 3.2 }));
    strokes.push(...compileRoughLine(wristLeftX - 5 * s, wristBottomY, wristRightX + 5 * s, wristBottomY, { strokeColor: '#2C2A29', strokeWidth: 2.5 }));
    // Palm Body
    strokes.push(...compileRoughRectangle(x + 10 * s, y + 45 * s, 95 * s, 110 * s, {
        strokeColor: '#2C2A29',
        fillColor: '#FEEBC8',
        fillStyle: 'solid',
        strokeWidth: 3.2
    }));
    // Crease lines on palm (lifeline & heartline)
    strokes.push(...compileRoughLine(x + 30 * s, y + 75 * s, x + 65 * s, y + 130 * s, { strokeColor: '#D69E2E', strokeWidth: 2.0 }));
    strokes.push(...compileRoughLine(x + 25 * s, y + 105 * s, x + 85 * s, y + 105 * s, { strokeColor: '#D69E2E', strokeWidth: 2.0 }));
    // --- 2. Thumb pointing LEFT at 90 degrees (Force F) ---
    strokes.push(...compileRoughRectangle(x - 90 * s, y + 80 * s, 105 * s, 35 * s, {
        strokeColor: '#2C2A29',
        fillColor: '#FEEBC8',
        fillStyle: 'solid',
        strokeWidth: 3.0
    }));
    strokes.push(...compileRoughLine(x - 85 * s, y + 83 * s, x - 85 * s, y + 110 * s, { strokeColor: '#D69E2E', strokeWidth: 2.2 }));
    strokes.push(...compileRoughLine(x - 40 * s, y + 80 * s, x - 40 * s, y + 115 * s, { strokeColor: '#CBD5E0', strokeWidth: 1.8 }));
    // 90-degree right angle symbol between thumb and index finger
    const cornerX = x + 10 * s;
    const cornerY = y + 78 * s;
    strokes.push(...compileRoughLine(cornerX, cornerY, cornerX - 18 * s, cornerY, { strokeColor: '#E53E3E', strokeWidth: 2.5 }));
    strokes.push(...compileRoughLine(cornerX - 18 * s, cornerY, cornerX - 18 * s, cornerY - 18 * s, { strokeColor: '#E53E3E', strokeWidth: 2.5 }));
    strokes.push(...convertTextToHandwritingStrokes("90°", cornerX - 42 * s, cornerY - 6 * s, {
        fontSize: Math.round(20 * s),
        color: '#E53E3E',
        strokeWidth: 2.0
    }));
    // --- 3. Four Fingers pointing UP (Current I) ---
    const fingers = [
        { name: 'Index', xOff: 12, len: 125, w: 21 },
        { name: 'Middle', xOff: 35, len: 140, w: 22 },
        { name: 'Ring', xOff: 59, len: 125, w: 21 },
        { name: 'Little', xOff: 82, len: 100, w: 19 }
    ];
    fingers.forEach(f => {
        const fx = x + f.xOff * s;
        const fy = y + 45 * s - f.len * s;
        strokes.push(...compileRoughRectangle(fx, fy, f.w * s, f.len * s, {
            strokeColor: '#2C2A29',
            fillColor: '#FEEBC8',
            fillStyle: 'solid',
            strokeWidth: 2.8
        }));
        strokes.push(...compileRoughLine(fx + 2 * s, fy + f.len * 0.4 * s, fx + (f.w - 2) * s, fy + f.len * 0.4 * s, { strokeColor: '#D69E2E', strokeWidth: 1.6 }));
        strokes.push(...compileRoughLine(fx + 2 * s, fy + f.len * 0.7 * s, fx + (f.w - 2) * s, fy + f.len * 0.7 * s, { strokeColor: '#D69E2E', strokeWidth: 1.6 }));
    });
    // --- 4. High-Contrast Vector Arrows ---
    strokes.push(...compileRoughArrow(x - 90 * s, y + 98 * s, x - 230 * s, y + 98 * s, {
        strokeColor: '#E53E3E',
        strokeWidth: 5.5
    }));
    strokes.push(...convertTextToHandwritingStrokes("LỰC TỪ F (Ngón Cái)", x - 320 * s, y + 68 * s, {
        fontSize: Math.round(26 * s),
        color: '#E53E3E',
        strokeWidth: 2.5
    }));
    strokes.push(...compileRoughArrow(x + 46 * s, y + 140 * s, x + 46 * s, y - 145 * s, {
        strokeColor: '#DD6B20',
        strokeWidth: 5.5
    }));
    strokes.push(...convertTextToHandwritingStrokes("DÒNG ĐIỆN I (Cổ tay -> Ngón giữa)", x + 75 * s, y - 120 * s, {
        fontSize: Math.round(26 * s),
        color: '#DD6B20',
        strokeWidth: 2.5
    }));
    strokes.push(...compileRoughCircle(x + 52 * s, y + 95 * s, 32 * s, {
        strokeColor: '#2B6CB0',
        fillColor: '#BEE3F8',
        fillStyle: 'solid',
        strokeWidth: 3.2
    }));
    strokes.push(...compileRoughLine(x + 36 * s, y + 79 * s, x + 68 * s, y + 111 * s, { strokeColor: '#2B6CB0', strokeWidth: 4.5 }));
    strokes.push(...compileRoughLine(x + 68 * s, y + 79 * s, x + 36 * s, y + 111 * s, { strokeColor: '#2B6CB0', strokeWidth: 4.5 }));
    strokes.push(...compileRoughArrow(x + 160 * s, y + 95 * s, x + 90 * s, y + 95 * s, {
        strokeColor: '#2B6CB0',
        strokeWidth: 4.0
    }));
    strokes.push(...convertTextToHandwritingStrokes("TỪ TRƯỜNG B (Đâm xuyên lòng bàn tay)", x - 80 * s, y + 250 * s, {
        fontSize: Math.round(24 * s),
        color: '#2B6CB0',
        strokeWidth: 2.4
    }));
    // Formula badge
    strokes.push(...compileRoughRectangle(x + 100 * s, y + 155 * s, 360 * s, 95 * s, {
        strokeColor: '#2B6CB0',
        fillColor: '#F7FAFC',
        fillStyle: 'solid',
        strokeWidth: 2.8
    }));
    strokes.push(...convertTextToHandwritingStrokes("F = B . I . L . sin(α)", x + 125 * s, y + 195 * s, {
        fontSize: Math.round(28 * s),
        color: '#2B6CB0',
        strokeWidth: 3.0
    }));
    strokes.push(...convertTextToHandwritingStrokes("Lực Laplace tác dụng lên đoạn dây dẫn", x + 120 * s, y + 232 * s, {
        fontSize: Math.round(18 * s),
        color: '#4A5568',
        strokeWidth: 1.8
    }));
    return strokes;
}
/**
 * Setup of Magnetic Poles (North N on Top, South S on Bottom)
 * Accurately matching the Vietnamese spoken script!
 */
export function createElectromagnetSetup(x, y, scale = 1.0, options = {}) {
    const strokes = [];
    const s = scale;
    // 1. Pole North (N - Red) on TOP (As stated in audio script!)
    strokes.push(...compileRoughRectangle(x + 30 * s, y, 260 * s, 65 * s, {
        strokeColor: '#2C2A29',
        fillColor: '#E53E3E',
        fillStyle: 'solid',
        strokeWidth: 3.2
    }));
    strokes.push(...convertTextToHandwritingStrokes("CỰC BẮC (N)", x + 75 * s, y + 45 * s, {
        fontSize: Math.round(30 * s),
        color: '#FFFFFF',
        strokeWidth: 3.2
    }));
    // 2. Pole South (S - Blue) on BOTTOM (As stated in audio script!)
    strokes.push(...compileRoughRectangle(x + 30 * s, y + 270 * s, 260 * s, 65 * s, {
        strokeColor: '#2C2A29',
        fillColor: '#3182CE',
        fillStyle: 'solid',
        strokeWidth: 3.2
    }));
    strokes.push(...convertTextToHandwritingStrokes("CỰC NAM (S)", x + 75 * s, y + 315 * s, {
        fontSize: Math.round(30 * s),
        color: '#FFFFFF',
        strokeWidth: 3.2
    }));
    // 3. Magnetic Field Lines B (N -> S) pointing vertically DOWN
    const lineXPositions = [70, 120, 160, 210, 250];
    lineXPositions.forEach(lx => {
        strokes.push(...compileRoughArrow(x + lx * s, y + 70 * s, x + lx * s, y + 265 * s, {
            strokeColor: '#2B6CB0',
            strokeWidth: 3.0
        }));
    });
    strokes.push(...convertTextToHandwritingStrokes("Từ trường B: Hướng từ TRÊN xuống DƯỚI", x + 310 * s, y + 115 * s, {
        fontSize: Math.round(22 * s),
        color: '#2B6CB0',
        strokeWidth: 2.2
    }));
    // 4. Conductor Wire carrying current I HORIZONTALLY from LEFT to RIGHT
    const wireY = y + 165 * s;
    strokes.push(...compileRoughLine(x - 40 * s, wireY, x + 340 * s, wireY, {
        strokeColor: '#D69E2E',
        strokeWidth: 8.0
    }));
    strokes.push(...compileRoughArrow(x + 40 * s, wireY, x + 240 * s, wireY, {
        strokeColor: '#DD6B20',
        strokeWidth: 4.5
    }));
    strokes.push(...convertTextToHandwritingStrokes("Dòng điện I: Từ TRÁI sang PHẢI", x + 310 * s, y + 160 * s, {
        fontSize: Math.round(22 * s),
        color: '#DD6B20',
        strokeWidth: 2.2
    }));
    // 5. Result Force F (Pointing toward the viewer / Forward out of screen)
    strokes.push(...compileRoughCircle(x + 160 * s, wireY, 28 * s, {
        strokeColor: '#E53E3E',
        fillColor: '#FED7D7',
        fillStyle: 'solid',
        strokeWidth: 3.5
    }));
    strokes.push(...compileRoughCircle(x + 160 * s, wireY, 6 * s, {
        strokeColor: '#E53E3E',
        fillColor: '#E53E3E',
        fillStyle: 'solid',
        strokeWidth: 4.0
    }));
    strokes.push(...convertTextToHandwritingStrokes("LỰC TỪ F: ĐẨY DÂY VỀ PHÍA TRƯỚC!", x - 20 * s, y + 365 * s, {
        fontSize: Math.round(28 * s),
        color: '#E53E3E',
        strokeWidth: 3.0
    }));
    return strokes;
}
/**
 * Mnemonic Badges for F - B - I with 3D Orthogonal Hand Axes
 */
export function createFBICardDiagram(x, y, scale = 1.0) {
    const strokes = [];
    const s = scale;
    // Three Badges
    const items = [
        { letter: 'F', title: 'FORCE (LỰC TỪ)', sub: 'Ngón Cái choãi 90°', color: '#E53E3E', bg: '#FED7D7' },
        { letter: 'B', title: 'FIELD (TỪ TRƯỜNG)', sub: 'Ngón Trỏ chỉ từ trường', color: '#2B6CB0', bg: '#BEE3F8' },
        { letter: 'I', title: 'CURRENT (DÒNG ĐIỆN)', sub: 'Ngón Giữa chỉ dòng điện', color: '#D69E2E', bg: '#FEFCBF' }
    ];
    const cardW = 185 * s;
    const cardH = 230 * s;
    const gap = 30 * s;
    items.forEach((item, idx) => {
        const cx = x + idx * (cardW + gap);
        // Outer card
        strokes.push(...compileRoughRectangle(cx, y, cardW, cardH, {
            strokeColor: '#2C2A29',
            fillColor: item.bg,
            fillStyle: 'solid',
            strokeWidth: 3.0
        }));
        // Huge Letter
        strokes.push(...convertTextToHandwritingStrokes(item.letter, cx + 65 * s, y + 80 * s, {
            fontSize: Math.round(76 * s),
            color: item.color,
            strokeWidth: 4.5
        }));
        // Subtitles inside card
        strokes.push(...convertTextToHandwritingStrokes(item.title, cx + 14 * s, y + 130 * s, {
            fontSize: Math.round(18 * s),
            color: '#2C2A29',
            strokeWidth: 2.2
        }));
        strokes.push(...convertTextToHandwritingStrokes(item.sub, cx + 12 * s, y + 175 * s, {
            fontSize: Math.round(17 * s),
            color: '#4A5568',
            strokeWidth: 1.8
        }));
    });
    // 3D Orthogonal Coordinate System Model beside the cards
    const axisX = x + 3 * (cardW + gap) + 80 * s;
    const axisY = y + 150 * s;
    // Z-axis (Thumb - Force F) pointing UP
    strokes.push(...compileRoughArrow(axisX, axisY, axisX, axisY - 140 * s, { strokeColor: '#E53E3E', strokeWidth: 5.0 }));
    strokes.push(...convertTextToHandwritingStrokes("Z: F (Ngón Cái)", axisX - 35 * s, axisY - 150 * s, { fontSize: Math.round(22 * s), color: '#E53E3E', strokeWidth: 2.5 }));
    // Y-axis (Index - Field B) pointing forward-left at 45 deg
    strokes.push(...compileRoughArrow(axisX, axisY, axisX - 70 * s, axisY + 55 * s, { strokeColor: '#2B6CB0', strokeWidth: 5.0 }));
    strokes.push(...convertTextToHandwritingStrokes("Y: B (Ngón Trỏ)", axisX - 130 * s, axisY + 75 * s, { fontSize: Math.round(22 * s), color: '#2B6CB0', strokeWidth: 2.5 }));
    // X-axis (Middle - Current I) pointing right
    strokes.push(...compileRoughArrow(axisX, axisY, axisX + 130 * s, axisY, { strokeColor: '#DD6B20', strokeWidth: 5.0 }));
    strokes.push(...convertTextToHandwritingStrokes("X: I (Ngón Giữa)", axisX + 75 * s, axisY + 30 * s, { fontSize: Math.round(22 * s), color: '#DD6B20', strokeWidth: 2.5 }));
    // 90 deg right-angle brackets between axes
    strokes.push(...compileRoughLine(axisX, axisY - 25 * s, axisX + 25 * s, axisY - 25 * s, { strokeColor: '#4A5568', strokeWidth: 2.0 }));
    strokes.push(...compileRoughLine(axisX + 25 * s, axisY - 25 * s, axisX + 25 * s, axisY, { strokeColor: '#4A5568', strokeWidth: 2.0 }));
    return strokes;
}
/**
 * Electric Motor Rotational Torque Principle & Loudspeaker
 */
export function createMotorPrincipleDiagram(x, y, scale = 1.0, options = {}) {
    const strokes = [];
    const s = scale;
    // Stator Magnets
    // North (Left)
    strokes.push(...compileRoughRectangle(x, y + 25 * s, 80 * s, 130 * s, {
        strokeColor: '#2C2A29',
        fillColor: '#E53E3E',
        fillStyle: 'solid',
        strokeWidth: 3.0
    }));
    strokes.push(...convertTextToHandwritingStrokes("N", x + 30 * s, y + 105 * s, {
        fontSize: Math.round(44 * s),
        color: '#FFFFFF',
        strokeWidth: 3.5
    }));
    // South (Right)
    strokes.push(...compileRoughRectangle(x + 360 * s, y + 25 * s, 80 * s, 130 * s, {
        strokeColor: '#2C2A29',
        fillColor: '#3182CE',
        fillStyle: 'solid',
        strokeWidth: 3.0
    }));
    strokes.push(...convertTextToHandwritingStrokes("S", x + 390 * s, y + 105 * s, {
        fontSize: Math.round(44 * s),
        color: '#FFFFFF',
        strokeWidth: 3.5
    }));
    // Rotor Rectangular Coil in 3D perspective
    const coilX = x + 120 * s;
    const coilY = y + 50 * s;
    strokes.push(...compileRoughLine(coilX, coilY, coilX + 200 * s, coilY - 20 * s, { strokeColor: '#D69E2E', strokeWidth: 5.5 }));
    strokes.push(...compileRoughLine(coilX + 200 * s, coilY - 20 * s, coilX + 200 * s, coilY + 80 * s, { strokeColor: '#D69E2E', strokeWidth: 5.5 }));
    strokes.push(...compileRoughLine(coilX + 200 * s, coilY + 80 * s, coilX, coilY + 100 * s, { strokeColor: '#D69E2E', strokeWidth: 5.5 }));
    strokes.push(...compileRoughLine(coilX, coilY + 100 * s, coilX, coilY, { strokeColor: '#D69E2E', strokeWidth: 5.5 }));
    // Central Rotating Axle
    strokes.push(...compileRoughLine(x + 220 * s, y - 25 * s, x + 220 * s, y + 175 * s, {
        strokeColor: '#718096',
        strokeWidth: 4.0
    }));
    // Force vectors F1 (Up) on left side, F2 (Down) on right side creating rotational couple
    strokes.push(...compileRoughArrow(coilX, coilY + 50 * s, coilX, coilY - 35 * s, {
        strokeColor: '#E53E3E',
        strokeWidth: 5.0
    }));
    strokes.push(...convertTextToHandwritingStrokes("F1 (Lên)", coilX - 80 * s, coilY - 5 * s, {
        fontSize: Math.round(22 * s),
        color: '#E53E3E',
        strokeWidth: 2.2
    }));
    strokes.push(...compileRoughArrow(coilX + 200 * s, coilY + 30 * s, coilX + 200 * s, coilY + 115 * s, {
        strokeColor: '#E53E3E',
        strokeWidth: 5.0
    }));
    strokes.push(...convertTextToHandwritingStrokes("F2 (Xuống)", coilX + 215 * s, coilY + 105 * s, {
        fontSize: Math.round(22 * s),
        color: '#E53E3E',
        strokeWidth: 2.2
    }));
    // Circular rotation indicator arrow
    strokes.push(...compileRoughArrow(x + 190 * s, y + 170 * s, x + 260 * s, y + 170 * s, {
        strokeColor: '#38A169',
        strokeWidth: 4.5,
        curved: true,
        curveOffset: 25 * s
    }));
    strokes.push(...convertTextToHandwritingStrokes("Khung Dây Quay Liên Tục!", x + 120 * s, y + 215 * s, {
        fontSize: Math.round(24 * s),
        color: '#2F855A',
        strokeWidth: 2.4
    }));
    return strokes;
}
/**
 * Loudspeaker Principle Diagram (Voice Coil + Magnetic Gap + Cone + Acoustic Waves)
 */
export function createLoudspeakerDiagram(x, y, scale = 1.0, options = {}) {
    const strokes = [];
    const s = scale;
    // 1. Permanent Magnet Base & Core
    strokes.push(...compileRoughRectangle(x, y + 40 * s, 100 * s, 100 * s, {
        strokeColor: '#2C2A29',
        fillColor: '#718096',
        fillStyle: 'solid',
        strokeWidth: 3.0
    }));
    strokes.push(...convertTextToHandwritingStrokes("Nam châm", x + 10 * s, y + 95 * s, {
        fontSize: Math.round(18 * s),
        color: '#FFFFFF'
    }));
    // 2. Voice Coil (Cuộn dây âm thanh) wrapped around core
    const coilX = x + 105 * s;
    for (let i = 0; i < 4; i++) {
        strokes.push(...compileRoughRectangle(coilX + i * 12 * s, y + 55 * s, 10 * s, 70 * s, {
            strokeColor: '#DD6B20',
            fillColor: '#F6AD55',
            fillStyle: 'solid',
            strokeWidth: 2.2
        }));
    }
    strokes.push(...convertTextToHandwritingStrokes("Cuộn dây âm thanh", coilX - 25 * s, y + 155 * s, {
        fontSize: Math.round(20 * s),
        color: '#DD6B20'
    }));
    // 3. Acoustic Cone (Màng loa hình nón)
    const coneStart = coilX + 48 * s;
    strokes.push(...compileRoughLine(coneStart, y + 55 * s, coneStart + 110 * s, y + 10 * s, {
        strokeColor: '#2C2A29',
        strokeWidth: 4.5
    }));
    strokes.push(...compileRoughLine(coneStart, y + 125 * s, coneStart + 110 * s, y + 170 * s, {
        strokeColor: '#2C2A29',
        strokeWidth: 4.5
    }));
    strokes.push(...compileRoughLine(coneStart + 110 * s, y + 10 * s, coneStart + 110 * s, y + 170 * s, {
        strokeColor: '#2C2A29',
        strokeWidth: 4.5
    }));
    strokes.push(...convertTextToHandwritingStrokes("Màng Loa", coneStart + 30 * s, y + 100 * s, {
        fontSize: Math.round(22 * s),
        color: '#2C2A29'
    }));
    // 4. Double-ended vibration arrow (Lực từ dao động tới lui)
    strokes.push(...compileRoughArrow(coneStart - 15 * s, y + 30 * s, coneStart + 35 * s, y + 30 * s, {
        strokeColor: '#E53E3E',
        strokeWidth: 3.5
    }));
    strokes.push(...compileRoughArrow(coneStart + 35 * s, y + 30 * s, coneStart - 15 * s, y + 30 * s, {
        strokeColor: '#E53E3E',
        strokeWidth: 3.5
    }));
    strokes.push(...convertTextToHandwritingStrokes("Lực từ rung tới lui", coneStart - 35 * s, y + 18 * s, {
        fontSize: Math.round(18 * s),
        color: '#E53E3E'
    }));
    // 5. Sound Waves emitting from cone into air
    const waveX = coneStart + 125 * s;
    strokes.push(...compileRoughArrow(waveX, y + 45 * s, waveX + 35 * s, y + 135 * s, {
        strokeColor: '#3182CE',
        strokeWidth: 3.5,
        curved: true,
        curveOffset: 18 * s
    }));
    strokes.push(...compileRoughArrow(waveX + 30 * s, y + 30 * s, waveX + 75 * s, y + 150 * s, {
        strokeColor: '#3182CE',
        strokeWidth: 4.0,
        curved: true,
        curveOffset: 25 * s
    }));
    strokes.push(...compileRoughArrow(waveX + 65 * s, y + 15 * s, waveX + 115 * s, y + 165 * s, {
        strokeColor: '#3182CE',
        strokeWidth: 4.5,
        curved: true,
        curveOffset: 32 * s
    }));
    strokes.push(...convertTextToHandwritingStrokes("Sóng Âm Thanh!", waveX + 25 * s, y + 195 * s, {
        fontSize: Math.round(24 * s),
        color: '#2B6CB0'
    }));
    return strokes;
}
/**
 * Đồ thị Sóng Giấc Ngủ 90 phút (5 Giai đoạn khoa học chuẩn Web5Ngay / Tri Kỷ Cảm Xúc)
 */
export function createSleepCycleSineWaveDiagram(x, y, scale = 1.0, options = {}) {
    const strokes = [];
    const s = scale;
    // 1. Trục tọa độ
    const axisW = 900 * s;
    const axisH = 400 * s;
    strokes.push(...compileRoughLine(x, y + axisH, x + axisW, y + axisH, {
        strokeColor: '#2C2A29',
        strokeWidth: 3.5
    }));
    strokes.push(...compileRoughLine(x, y, x, y + axisH, {
        strokeColor: '#2C2A29',
        strokeWidth: 3.5
    }));
    // Nhãn trục
    strokes.push(...convertTextToHandwritingStrokes("Độ Sâu Giấc Ngủ", x - 10 * s, y - 35 * s, {
        fontSize: Math.round(24 * s),
        color: '#2C2A29'
    }));
    strokes.push(...convertTextToHandwritingStrokes("Thời Gian (0 -> 90 Phút / Chu Kỳ)", x + axisW - 320 * s, y + axisH + 45 * s, {
        fontSize: Math.round(22 * s),
        color: '#2C2A29'
    }));
    // 2. Đường sóng hình sin giấc ngủ uốn lượn mềm mại
    // P0(x+20, y+80) -> P1(x+180, y+160) -> P2(x+360, y+340) -> P3(x+540, y+360) -> P4(x+720, y+100) -> P5(x+860, y+80)
    const wavePoints = [
        [x + 30 * s, y + 80 * s],
        [x + 180 * s, y + 150 * s],
        [x + 360 * s, y + 330 * s],
        [x + 520 * s, y + 350 * s],
        [x + 700 * s, y + 120 * s],
        [x + 860 * s, y + 80 * s]
    ];
    for (let i = 0; i < wavePoints.length - 1; i++) {
        const p1 = wavePoints[i];
        const p2 = wavePoints[i + 1];
        strokes.push(...compileRoughLine(p1[0], p1[1], p2[0], p2[1], {
            strokeColor: '#2B6CB0',
            strokeWidth: 5.0
        }));
    }
    // 3. 5 Giai đoạn & Chú thích
    // GĐ 1: Ru ngủ
    strokes.push(...compileRoughCircle(wavePoints[0][0], wavePoints[0][1], 24 * s, {
        strokeColor: '#2F855A',
        fillColor: '#C6F6D5',
        fillStyle: 'solid'
    }));
    strokes.push(...convertTextToHandwritingStrokes("1. Ru Ngủ", wavePoints[0][0] - 20 * s, wavePoints[0][1] - 40 * s, {
        fontSize: Math.round(20 * s),
        color: '#2F855A'
    }));
    // GĐ 2: Ngủ nông (50%)
    strokes.push(...compileRoughCircle(wavePoints[1][0], wavePoints[1][1], 24 * s, {
        strokeColor: '#3182CE',
        fillColor: '#BEE3F8',
        fillStyle: 'solid'
    }));
    strokes.push(...convertTextToHandwritingStrokes("2. Ngủ Nông (50%)", wavePoints[1][0] - 40 * s, wavePoints[1][1] - 35 * s, {
        fontSize: Math.round(20 * s),
        color: '#3182CE'
    }));
    // GĐ 3: Ngủ sâu (10%)
    strokes.push(...compileRoughCircle(wavePoints[2][0], wavePoints[2][1], 26 * s, {
        strokeColor: '#D9381E',
        fillColor: '#FED7D7',
        fillStyle: 'solid'
    }));
    strokes.push(...convertTextToHandwritingStrokes("3. Ngủ Sâu (10%)", wavePoints[2][0] - 60 * s, wavePoints[2][1] + 35 * s, {
        fontSize: Math.round(20 * s),
        color: '#D9381E'
    }));
    // GĐ 4: Ngủ rất sâu (Delta)
    strokes.push(...compileRoughCircle(wavePoints[3][0], wavePoints[3][1], 28 * s, {
        strokeColor: '#9B2C2C',
        fillColor: '#FEB2B2',
        fillStyle: 'solid'
    }));
    strokes.push(...convertTextToHandwritingStrokes("4. Ngủ Rất Sâu", wavePoints[3][0] - 50 * s, wavePoints[3][1] + 35 * s, {
        fontSize: Math.round(20 * s),
        color: '#9B2C2C'
    }));
    // Cảnh báo vùng nguy hiểm (GĐ 3 & 4)
    strokes.push(...compileRoughRectangle(x + 300 * s, y + 250 * s, 300 * s, 140 * s, {
        strokeColor: '#E53E3E',
        strokeWidth: 2.5
    }));
    strokes.push(...convertTextToHandwritingStrokes("BÁO THỨC REO Ở ĐÂY = CỰC MỆT!", x + 310 * s, y + 280 * s, {
        fontSize: Math.round(18 * s),
        color: '#E53E3E'
    }));
    // GĐ 5: Ngủ mơ REM
    strokes.push(...compileRoughCircle(wavePoints[4][0], wavePoints[4][1], 26 * s, {
        strokeColor: '#2F855A',
        fillColor: '#C6F6D5',
        fillStyle: 'solid'
    }));
    strokes.push(...convertTextToHandwritingStrokes("5. Ngủ Mơ (REM)", wavePoints[4][0] - 50 * s, wavePoints[4][1] - 40 * s, {
        fontSize: Math.round(20 * s),
        color: '#2F855A'
    }));
    // Khung Điểm Vàng Thức Dậy
    strokes.push(...compileRoughRectangle(x + 650 * s, y + 20 * s, 260 * s, 70 * s, {
        strokeColor: '#2F855A',
        strokeWidth: 2.5
    }));
    strokes.push(...convertTextToHandwritingStrokes("ĐIỂM VÀNG THỨC DẬY!", x + 670 * s, y + 55 * s, {
        fontSize: Math.round(20 * s),
        color: '#2F855A'
    }));
    return strokes;
}
/**
 * Bảng Công Thức Vàng Tính Giờ Thức Dậy Hoàn Hảo
 */
export function createFormulaBoardDiagram(x, y, scale = 1.0) {
    const strokes = [];
    const s = scale;
    // Khung bảng công thức chính
    strokes.push(...compileRoughRectangle(x, y, 920 * s, 360 * s, {
        strokeColor: '#2B6CB0',
        strokeWidth: 4.0
    }));
    strokes.push(...convertTextToHandwritingStrokes("CÔNG THỨC VÀNG THỨC DẬY KHÔNG MỆT", x + 160 * s, y + 45 * s, {
        fontSize: Math.round(30 * s),
        color: '#2B6CB0'
    }));
    // Dòng công thức
    strokes.push(...compileRoughRectangle(x + 40 * s, y + 75 * s, 840 * s, 90 * s, {
        strokeColor: '#D9381E',
        strokeWidth: 3.5
    }));
    strokes.push(...convertTextToHandwritingStrokes("GIỜ THỨC = GIỜ NGỦ + 14 PHÚT + (90P x N)", x + 70 * s, y + 130 * s, {
        fontSize: Math.round(34 * s),
        color: '#D9381E'
    }));
    // Mũi tên giải thích
    strokes.push(...compileRoughArrow(x + 230 * s, y + 175 * s, x + 230 * s, y + 215 * s, {
        strokeColor: '#4A5568',
        strokeWidth: 2.5
    }));
    strokes.push(...convertTextToHandwritingStrokes("14p: Chìm vào giấc", x + 150 * s, y + 245 * s, {
        fontSize: Math.round(20 * s),
        color: '#4A5568'
    }));
    strokes.push(...compileRoughArrow(x + 580 * s, y + 175 * s, x + 580 * s, y + 215 * s, {
        strokeColor: '#4A5568',
        strokeWidth: 2.5
    }));
    strokes.push(...convertTextToHandwritingStrokes("N = 3, 4, 5, hoặc 6 chu kỳ", x + 470 * s, y + 245 * s, {
        fontSize: Math.round(20 * s),
        color: '#4A5568'
    }));
    // Ví dụ chuẩn
    strokes.push(...convertTextToHandwritingStrokes("Ví dụ: Ngủ 22:00 (N=5) -> Thức dậy lúc 05:44 Sáng (Tỉnh táo 100%)", x + 60 * s, y + 310 * s, {
        fontSize: Math.round(24 * s),
        color: '#2F855A'
    }));
    return strokes;
}
/**
 * Thước Đo 5 Chu Kỳ Ngủ (Timeline Bar)
 */
export function createClockTimelineBar(x, y, scale = 1.0) {
    const strokes = [];
    const s = scale;
    const blockW = 160 * s;
    const blockH = 80 * s;
    for (let i = 0; i < 5; i++) {
        const bx = x + i * (blockW + 15 * s);
        strokes.push(...compileRoughRectangle(bx, y, blockW, blockH, {
            strokeColor: '#2B6CB0',
            strokeWidth: 3.0
        }));
        strokes.push(...convertTextToHandwritingStrokes(`CK ${i + 1}: 90p`, bx + 25 * s, y + 48 * s, {
            fontSize: Math.round(22 * s),
            color: '#2B6CB0'
        }));
    }
    strokes.push(...convertTextToHandwritingStrokes("TỔNG: 5 CHU KỲ = 7.5 TIẾNG (GIẤC NGỦ HOÀN HẢO)", x + 160 * s, y + 130 * s, {
        fontSize: Math.round(26 * s),
        color: '#2F855A'
    }));
    return strokes;
}
/**
 * Biển Cảnh Báo Tuyệt Đối Cấm Ngủ Nướng (No Snooze)
 */
export function createSnoozeBanDiagram(x, y, scale = 1.0) {
    const strokes = [];
    const s = scale;
    // Khung báo động đỏ
    strokes.push(...compileRoughRectangle(x, y, 700 * s, 260 * s, {
        strokeColor: '#E53E3E',
        strokeWidth: 4.5
    }));
    // Dấu gạch chéo đỏ lớn
    strokes.push(...compileRoughLine(x + 50 * s, y + 50 * s, x + 250 * s, y + 210 * s, {
        strokeColor: '#E53E3E',
        strokeWidth: 8.0
    }));
    strokes.push(...compileRoughLine(x + 250 * s, y + 50 * s, x + 50 * s, y + 210 * s, {
        strokeColor: '#E53E3E',
        strokeWidth: 8.0
    }));
    strokes.push(...convertTextToHandwritingStrokes("CẤM NGỦ NƯỚNG 10 PHÚT!", x + 280 * s, y + 90 * s, {
        fontSize: Math.round(32 * s),
        color: '#E53E3E'
    }));
    strokes.push(...convertTextToHandwritingStrokes("Ngủ ráng 10-15p = Rơi lại Ngủ Sâu", x + 280 * s, y + 140 * s, {
        fontSize: Math.round(22 * s),
        color: '#4A5568'
    }));
    strokes.push(...convertTextToHandwritingStrokes("Dậy lần 2 sẽ nhức đầu mệt gấp đôi!", x + 280 * s, y + 185 * s, {
        fontSize: Math.round(22 * s),
        color: '#D9381E'
    }));
    return strokes;
}
