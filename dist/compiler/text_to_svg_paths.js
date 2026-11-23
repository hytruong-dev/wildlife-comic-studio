import opentype from 'opentype.js';
import path from 'path';
import fs from 'fs';
let cachedFont = null;
export function loadHandwritingFont(fontPath) {
    if (cachedFont && !fontPath)
        return cachedFont;
    const targetPath = fontPath || path.resolve('assets/fonts/Mali-Bold.ttf');
    if (!fs.existsSync(targetPath)) {
        // Fallback to BeVietnamPro or PlaypenSans
        const fallback1 = path.resolve('assets/fonts/BeVietnamPro-Bold.ttf');
        if (fs.existsSync(fallback1))
            return opentype.loadSync(fallback1);
        const fallback2 = path.resolve('assets/fonts/PlaypenSans-Regular.ttf');
        if (fs.existsSync(fallback2))
            return opentype.loadSync(fallback2);
        throw new Error(`Font file not found: ${targetPath}`);
    }
    const font = opentype.loadSync(targetPath);
    if (!fontPath)
        cachedFont = font;
    return font;
}
/**
 * Calculates approximate length of an SVG path given by opentype commands
 */
export function estimatePathCommandsLength(commands) {
    let len = 0;
    let startPt = { x: 0, y: 0 };
    let endPt = { x: 0, y: 0 };
    let currentPt = { x: 0, y: 0 };
    let hasStart = false;
    for (const cmd of commands) {
        if (cmd.type === 'M') {
            currentPt = { x: cmd.x, y: cmd.y };
            if (!hasStart) {
                startPt = currentPt;
                hasStart = true;
            }
            endPt = currentPt;
        }
        else if (cmd.type === 'L') {
            const dx = cmd.x - currentPt.x;
            const dy = cmd.y - currentPt.y;
            len += Math.sqrt(dx * dx + dy * dy);
            currentPt = { x: cmd.x, y: cmd.y };
            endPt = currentPt;
        }
        else if (cmd.type === 'C') {
            // Approximate cubic bezier length with chord + control net
            const dChord = Math.sqrt((cmd.x - currentPt.x) ** 2 + (cmd.y - currentPt.y) ** 2);
            const dNet = Math.sqrt((cmd.x1 - currentPt.x) ** 2 + (cmd.y1 - currentPt.y) ** 2) +
                Math.sqrt((cmd.x2 - cmd.x1) ** 2 + (cmd.y2 - cmd.y1) ** 2) +
                Math.sqrt((cmd.x - cmd.x2) ** 2 + (cmd.y - cmd.y2) ** 2);
            len += (dChord + dNet) / 2;
            currentPt = { x: cmd.x, y: cmd.y };
            endPt = currentPt;
        }
        else if (cmd.type === 'Q') {
            const dChord = Math.sqrt((cmd.x - currentPt.x) ** 2 + (cmd.y - currentPt.y) ** 2);
            const dNet = Math.sqrt((cmd.x1 - currentPt.x) ** 2 + (cmd.y1 - currentPt.y) ** 2) +
                Math.sqrt((cmd.x - cmd.x1) ** 2 + (cmd.y - cmd.y1) ** 2);
            len += (dChord + dNet) / 2;
            currentPt = { x: cmd.x, y: cmd.y };
            endPt = currentPt;
        }
        else if (cmd.type === 'Z') {
            const dx = startPt.x - currentPt.x;
            const dy = startPt.y - currentPt.y;
            len += Math.sqrt(dx * dx + dy * dy);
            currentPt = startPt;
        }
    }
    return { length: Math.max(1, len), start: startPt, end: endPt };
}
/**
 * Splits opentype path into separate sub-paths (M ... Z)
 * so diacritics and distinct strokes can be written sequentially
 */
export function splitPathIntoSubpaths(pathObj) {
    const subpaths = [];
    let currentCommands = [];
    for (const cmd of pathObj.commands) {
        if (cmd.type === 'M' && currentCommands.length > 0) {
            const p = new opentype.Path();
            p.commands = currentCommands;
            subpaths.push(p);
            currentCommands = [cmd];
        }
        else {
            currentCommands.push(cmd);
        }
    }
    if (currentCommands.length > 0) {
        const p = new opentype.Path();
        p.commands = currentCommands;
        subpaths.push(p);
    }
    return subpaths;
}
/**
 * Converts Vietnamese text into ordered RawStrokes representing handwriting motion
 */
export function convertTextToHandwritingStrokes(text, startX, startY, options = {}) {
    const fontSize = options.fontSize || 42;
    const color = options.color || '#2C2A29';
    const strokeWidth = options.strokeWidth !== undefined ? Math.min(0.8, options.strokeWidth) : 0.5;
    const letterSpacing = options.letterSpacing || 2.0;
    const font = loadHandwritingFont(options.fontPath);
    const strokes = [];
    let currentX = startX;
    const scale = fontSize / font.unitsPerEm;
    const chars = Array.from(text);
    chars.forEach((ch, charIdx) => {
        // If space character, just advance position
        if (ch === ' ' || ch === '\t') {
            currentX += fontSize * 0.42 + letterSpacing;
            return;
        }
        const glyph = font.charToGlyph(ch);
        const glyphPath = glyph.getPath(currentX, startY, fontSize);
        const d = glyphPath.toPathData(2);
        if (!d || d.length === 0)
            return;
        const { length, start, end } = estimatePathCommandsLength(glyphPath.commands);
        if (length < 2)
            return;
        strokes.push({
            id: `text_${charIdx}_${Math.random().toString(36).substring(2, 7)}`,
            d,
            length,
            startPoint: start,
            endPoint: end,
            strokeColor: color,
            strokeWidth,
            isFillStroke: false,
            priority: charIdx // Preserves left-to-right writing order
        });
        const advance = (glyph.advanceWidth || font.unitsPerEm * 0.6) * scale;
        currentX += advance + letterSpacing;
    });
    return strokes;
}
