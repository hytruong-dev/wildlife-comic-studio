// @ts-ignore
import roughModule from 'roughjs/bundled/rough.cjs.js';
import { RawStroke, Point2D } from './stroke_sorter.js';

// Initialize rough generator
const roughGen = roughModule.generator();

export interface RoughCompileOptions {
  strokeColor?: string;
  fillColor?: string;
  strokeWidth?: number;
  roughness?: number;
  bowing?: number;
  fillStyle?: 'hachure' | 'zigzag' | 'cross-hatch' | 'dots' | 'solid';
  fillWeight?: number;
  hachureAngle?: number;
  hachureGap?: number;
  seed?: number;
  priority?: number;
}

/**
 * Estimates length and start/end points of an SVG path string (M, C, L, Q)
 */
export function parseSvgPathMetrics(d: string): { length: number; start: Point2D; end: Point2D } {
  let len = 0;
  let startPt: Point2D = { x: 0, y: 0 };
  let endPt: Point2D = { x: 0, y: 0 };
  let curPt: Point2D = { x: 0, y: 0 };
  let hasStart = false;

  // Split path commands
  const regex = /([MLCQZ])([^MLCQZ]*)/gi;
  let match;

  while ((match = regex.exec(d)) !== null) {
    const cmd = match[1].toUpperCase();
    const nums = match[2].trim().split(/[\s,]+/).filter(Boolean).map(Number);

    if (cmd === 'M' && nums.length >= 2) {
      curPt = { x: nums[0], y: nums[1] };
      if (!hasStart) {
        startPt = curPt;
        hasStart = true;
      }
      endPt = curPt;
    } else if (cmd === 'L' && nums.length >= 2) {
      for (let i = 0; i < nums.length; i += 2) {
        const nextPt = { x: nums[i], y: nums[i + 1] };
        len += Math.hypot(nextPt.x - curPt.x, nextPt.y - curPt.y);
        curPt = nextPt;
      }
      endPt = curPt;
    } else if (cmd === 'C' && nums.length >= 6) {
      for (let i = 0; i < nums.length; i += 6) {
        const p1 = { x: nums[i], y: nums[i + 1] };
        const p2 = { x: nums[i + 2], y: nums[i + 3] };
        const p3 = { x: nums[i + 4], y: nums[i + 5] };
        // Approximate cubic bezier length
        const dChord = Math.hypot(p3.x - curPt.x, p3.y - curPt.y);
        const dNet = Math.hypot(p1.x - curPt.x, p1.y - curPt.y) +
                      Math.hypot(p2.x - p1.x, p2.y - p1.y) +
                      Math.hypot(p3.x - p2.x, p3.y - p2.y);
        len += (dChord + dNet) / 2;
        curPt = p3;
      }
      endPt = curPt;
    } else if (cmd === 'Q' && nums.length >= 4) {
      for (let i = 0; i < nums.length; i += 4) {
        const p1 = { x: nums[i], y: nums[i + 1] };
        const p2 = { x: nums[i + 2], y: nums[i + 3] };
        const dChord = Math.hypot(p2.x - curPt.x, p2.y - curPt.y);
        const dNet = Math.hypot(p1.x - curPt.x, p1.y - curPt.y) + Math.hypot(p2.x - p1.x, p2.y - p1.y);
        len += (dChord + dNet) / 2;
        curPt = p2;
      }
      endPt = curPt;
    } else if (cmd === 'Z') {
      len += Math.hypot(startPt.x - curPt.x, startPt.y - curPt.y);
      curPt = startPt;
    }
  }

  return { length: Math.max(2, len), start: startPt, end: endPt };
}

/**
 * Extracts strokes from a Rough.js drawable object
 */
function extractRoughStrokes(drawable: any, options: RoughCompileOptions): RawStroke[] {
  const strokes: RawStroke[] = [];
  const strokeColor = options.strokeColor || '#2C2A29';
  const fillColor = options.fillColor || '#E86A58';
  const strokeWidth = options.strokeWidth || 3.0;
  const prio = options.priority ?? 0;

  for (let sIdx = 0; sIdx < drawable.sets.length; sIdx++) {
    const set = drawable.sets[sIdx];
    const d = roughGen.opsToPath(set);
    if (!d || d.length === 0) continue;

    const isFill = set.type === 'fillSketch' || set.type === 'fillPath';
    const metrics = parseSvgPathMetrics(d);

    strokes.push({
      id: `rough_${set.type}_${Math.random().toString(36).substring(2, 7)}`,
      d,
      length: metrics.length,
      startPoint: metrics.start,
      endPoint: metrics.end,
      strokeColor: isFill ? fillColor : strokeColor,
      strokeWidth: isFill ? Math.max(1.5, strokeWidth * 0.7) : strokeWidth,
      isFillStroke: isFill,
      // Ink outlines draw before color fills
      priority: isFill ? prio + 100 : prio
    });
  }

  return strokes;
}

export function compileRoughRectangle(x: number, y: number, w: number, h: number, options: RoughCompileOptions = {}): RawStroke[] {
  const ro: any = {
    roughness: options.roughness ?? 1.4,
    bowing: options.bowing ?? 1.0,
    stroke: options.strokeColor ?? '#2C2A29',
    strokeWidth: options.strokeWidth ?? 3.5,
    seed: options.seed ?? 10
  };
  if (options.fillColor) {
    ro.fill = options.fillColor;
    ro.fillStyle = options.fillStyle ?? 'hachure';
    ro.fillWeight = options.fillWeight ?? 2.0;
    ro.hachureGap = options.hachureGap ?? 8.0;
    ro.hachureAngle = options.hachureAngle ?? -41.0;
  }
  const drawable = roughGen.rectangle(x, y, w, h, ro);
  return extractRoughStrokes(drawable, options);
}

export function compileRoughCircle(cx: number, cy: number, radius: number, options: RoughCompileOptions = {}): RawStroke[] {
  const ro: any = {
    roughness: options.roughness ?? 1.4,
    bowing: options.bowing ?? 1.0,
    stroke: options.strokeColor ?? '#2C2A29',
    strokeWidth: options.strokeWidth ?? 3.5,
    seed: options.seed ?? 20
  };
  if (options.fillColor) {
    ro.fill = options.fillColor;
    ro.fillStyle = options.fillStyle ?? 'hachure';
    ro.fillWeight = options.fillWeight ?? 2.0;
    ro.hachureGap = options.hachureGap ?? 8.0;
  }
  const drawable = roughGen.circle(cx, cy, radius * 2, ro);
  return extractRoughStrokes(drawable, options);
}

export function compileRoughLine(x1: number, y1: number, x2: number, y2: number, options: RoughCompileOptions = {}): RawStroke[] {
  const drawable = roughGen.line(x1, y1, x2, y2, {
    roughness: options.roughness ?? 1.2,
    bowing: options.bowing ?? 1.0,
    stroke: options.strokeColor ?? '#2C2A29',
    strokeWidth: options.strokeWidth ?? 3.5,
    seed: options.seed ?? 30
  });
  return extractRoughStrokes(drawable, options);
}

export function compileRoughArrow(
  fromX: number,
  fromY: number,
  toX: number,
  toY: number,
  options: RoughCompileOptions & { curved?: boolean; curveOffset?: number } = {}
): RawStroke[] {
  const strokes: RawStroke[] = [];
  const dx = toX - fromX;
  const dy = toY - fromY;
  const angle = Math.atan2(dy, dx);
  const headLen = 22;
  const headAngle = Math.PI / 6; // 30 deg

  if (options.curved) {
    const midX = (fromX + toX) / 2;
    const midY = (fromY + toY) / 2;
    const offset = options.curveOffset ?? 40;
    // Perpendicular curve control
    const ctrlX = midX - Math.sin(angle) * offset;
    const ctrlY = midY + Math.cos(angle) * offset;

    const curveD = `M ${fromX} ${fromY} Q ${ctrlX} ${ctrlY} ${toX} ${toY}`;
    const curveDrawable = roughGen.path(curveD, {
      roughness: options.roughness ?? 1.3,
      stroke: options.strokeColor ?? '#2B6CB0',
      strokeWidth: options.strokeWidth ?? 4.0
    });
    strokes.push(...extractRoughStrokes(curveDrawable, options));
  } else {
    strokes.push(...compileRoughLine(fromX, fromY, toX, toY, options));
  }

  // Arrowhead barb 1
  const h1X = toX - headLen * Math.cos(angle - headAngle);
  const h1Y = toY - headLen * Math.sin(angle - headAngle);
  strokes.push(...compileRoughLine(toX, toY, h1X, h1Y, { ...options, priority: (options.priority ?? 0) + 1 }));

  // Arrowhead barb 2
  const h2X = toX - headLen * Math.cos(angle + headAngle);
  const h2Y = toY - headLen * Math.sin(angle + headAngle);
  strokes.push(...compileRoughLine(toX, toY, h2X, h2Y, { ...options, priority: (options.priority ?? 0) + 2 }));

  return strokes;
}

export function compileRoughPolygon(points: [number, number][], options: RoughCompileOptions = {}): RawStroke[] {
  const ro: any = {
    roughness: options.roughness ?? 1.4,
    stroke: options.strokeColor ?? '#2C2A29',
    strokeWidth: options.strokeWidth ?? 3.5
  };
  if (options.fillColor) {
    ro.fill = options.fillColor;
    ro.fillStyle = options.fillStyle ?? 'hachure';
    ro.fillWeight = options.fillWeight ?? 2.0;
  }
  const drawable = roughGen.polygon(points, ro);
  return extractRoughStrokes(drawable, options);
}

export function compileRoughSvgPath(d: string, options: RoughCompileOptions = {}): RawStroke[] {
  const ro: any = {
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
  const drawable = roughGen.path(d, ro);
  return extractRoughStrokes(drawable, options);
}
