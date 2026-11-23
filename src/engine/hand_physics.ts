export interface Point2D {
  x: number;
  y: number;
}

export interface CompiledStroke {
  id: string;
  d: string;                 // SVG Path data
  length: number;            // Total path length in px
  startMs: number;           // Pen touches paper
  endMs: number;             // Pen leaves paper
  strokeColor: string;
  strokeWidth: number;
  isFillStroke?: boolean;    // Ink line vs Color fill
  startPoint: Point2D;
  endPoint: Point2D;
}

export interface HandPose {
  visible: boolean;
  x: number;
  y: number;
  angleDeg: number;
  liftProgress: number;      // 0 = on paper, 1 = maximum airborne lift
  scale: number;
  shadowOffset: Point2D;
  isDrawing: boolean;
  tipVelocity: number;       // Velocity in px/s
}

export function easeInOutSine(u: number): number {
  const clamped = Math.max(0, Math.min(1, u));
  return -(Math.cos(Math.PI * clamped) - 1) / 2;
}

/**
 * Computes deterministic hand pose and pen tip state for any arbitrary millisecond
 */
export function computeHandPoseAtTime(
  timeMs: number,
  strokes: CompiledStroke[],
  pathElements: Map<string, SVGPathElement>
): HandPose {
  if (strokes.length === 0) {
    return {
      visible: false,
      x: 0,
      y: 0,
      angleDeg: 0,
      liftProgress: 1,
      scale: 1,
      shadowOffset: { x: 8, y: 12 },
      isDrawing: false,
      tipVelocity: 0
    };
  }

  // 1. Check if timeMs is within an active stroke
  for (let i = 0; i < strokes.length; i++) {
    const s = strokes[i];
    if (timeMs >= s.startMs && timeMs <= s.endMs) {
      const pathEl = pathElements.get(s.id);
      const duration = Math.max(1, s.endMs - s.startMs);
      const u = (timeMs - s.startMs) / duration;
      const progress = easeInOutSine(u);
      const currentLen = progress * s.length;

      let pt: Point2D;
      let angleRad = 0;

      if (pathEl) {
        const svgPt = pathEl.getPointAtLength(Math.min(s.length, currentLen));
        pt = { x: svgPt.x, y: svgPt.y };

        const delta = Math.min(4, Math.max(1, s.length * 0.05));
        const pBefore = pathEl.getPointAtLength(Math.max(0, currentLen - delta));
        const pAfter = pathEl.getPointAtLength(Math.min(s.length, currentLen + delta));
        angleRad = Math.atan2(pAfter.y - pBefore.y, pAfter.x - pBefore.x);
      } else {
        // Fallback linear interpolation between stroke startPoint and endPoint
        pt = {
          x: s.startPoint.x + (s.endPoint.x - s.startPoint.x) * progress,
          y: s.startPoint.y + (s.endPoint.y - s.startPoint.y) * progress
        };
        angleRad = Math.atan2(s.endPoint.y - s.startPoint.y, s.endPoint.x - s.startPoint.x);
      }

      // Natural wrist oscillation: tilt within [-12, +12] degrees based on direction
      const rawWristAngle = Math.sin(angleRad) * 8 + Math.cos(angleRad * 2) * 3;
      const wristAngleDeg = Math.max(-12, Math.min(12, rawWristAngle));

      // Instantaneous speed estimation
      const dtMs = 33;
      const uNext = Math.min(1, (timeMs + dtMs - s.startMs) / duration);
      const speedPxPerSec = ((easeInOutSine(uNext) - progress) * s.length / dtMs) * 1000;

      return {
        visible: true,
        x: pt.x,
        y: pt.y,
        angleDeg: wristAngleDeg,
        liftProgress: 0,
        scale: 1.0,
        shadowOffset: { x: 8, y: 12 },
        isDrawing: true,
        tipVelocity: Math.abs(speedPxPerSec)
      };
    }

    // 2. Check if timeMs is within a pen-lift gap between stroke i and stroke i+1
    if (i < strokes.length - 1) {
      const nextStroke = strokes[i + 1];
      if (timeMs > s.endMs && timeMs < nextStroke.startMs) {
        const gapMs = nextStroke.startMs - s.endMs;

        // If pause is longer than 800ms, retract hand downwards smoothly
        if (gapMs > 800) {
          const pauseTime = timeMs - s.endMs;
          if (pauseTime < 300) {
            // Retracting down
            const uRetract = easeInOutSine(pauseTime / 300);
            return {
              visible: true,
              x: s.endPoint.x + uRetract * 120,
              y: s.endPoint.y + uRetract * 400,
              angleDeg: 15 * uRetract,
              liftProgress: 1,
              scale: 1.0,
              shadowOffset: { x: 8 + 30 * uRetract, y: 12 + 40 * uRetract },
              isDrawing: false,
              tipVelocity: 150
            };
          } else if (timeMs > nextStroke.startMs - 300) {
            // Re-entering from below
            const uEnter = easeInOutSine((nextStroke.startMs - timeMs) / 300);
            return {
              visible: true,
              x: nextStroke.startPoint.x + uEnter * 120,
              y: nextStroke.startPoint.y + uEnter * 400,
              angleDeg: 15 * uEnter,
              liftProgress: 1,
              scale: 1.0,
              shadowOffset: { x: 8 + 30 * uEnter, y: 12 + 40 * uEnter },
              isDrawing: false,
              tipVelocity: 150
            };
          }
          return {
            visible: false,
            x: 0,
            y: 0,
            angleDeg: 0,
            liftProgress: 1,
            scale: 1,
            shadowOffset: { x: 0, y: 0 },
            isDrawing: false,
            tipVelocity: 0
          };
        }

        // Standard short pen lift: Quadratic Bezier arc with upward parabolic arch
        const uLift = easeInOutSine((timeMs - s.endMs) / gapMs);
        const liftArc = Math.sin(Math.PI * uLift); // Peak = 1.0 at midpoint

        const pEnd = s.endPoint;
        const pStart = nextStroke.startPoint;

        const ctrlX = (pEnd.x + pStart.x) / 2;
        const ctrlY = Math.min(pEnd.y, pStart.y) - 45 * liftArc;

        const x = (1 - uLift) * (1 - uLift) * pEnd.x + 2 * (1 - uLift) * uLift * ctrlX + uLift * uLift * pStart.x;
        const y = (1 - uLift) * (1 - uLift) * pEnd.y + 2 * (1 - uLift) * uLift * ctrlY + uLift * uLift * pStart.y;

        // Pen lift translation & dynamic scaling
        const liftShiftX = 12 * liftArc;
        const liftShiftY = -18 * liftArc;

        return {
          visible: true,
          x: x + liftShiftX,
          y: y + liftShiftY,
          angleDeg: -6 * liftArc,
          liftProgress: liftArc,
          scale: 1.0 + 0.035 * liftArc,
          shadowOffset: { x: 8 + 18 * liftArc, y: 12 + 24 * liftArc },
          isDrawing: false,
          tipVelocity: 50
        };
      }
    }
  }

  // Before first stroke or after last stroke
  return {
    visible: false,
    x: 0,
    y: 0,
    angleDeg: 0,
    liftProgress: 1,
    scale: 1,
    shadowOffset: { x: 8, y: 12 },
    isDrawing: false,
    tipVelocity: 0
  };
}
