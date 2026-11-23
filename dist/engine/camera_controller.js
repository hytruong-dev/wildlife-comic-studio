export function easeInOutCubic(u) {
    const c = Math.max(0, Math.min(1, u));
    return c < 0.5 ? 4 * c * c * c : 1 - Math.pow(-2 * c + 2, 3) / 2;
}
/**
 * Closed-form critically damped spring easing (as in cth9191/animate)
 */
export function springEase(u) {
    const c = Math.max(0, Math.min(1, u));
    // Underdamped spring with slight organic overshoot
    const omega = 5.5;
    const zeta = 0.85;
    const decay = Math.exp(-zeta * omega * c);
    const osc = Math.cos(omega * Math.sqrt(1 - zeta * zeta) * c);
    return 1 - decay * osc;
}
export class CameraController {
    keyframes;
    constructor(keyframes = []) {
        this.keyframes = [...keyframes].sort((a, b) => a.timeMs - b.timeMs);
        if (this.keyframes.length === 0) {
            this.keyframes.push({ timeMs: 0, x: 960, y: 540, scale: 1.0 });
        }
    }
    getCameraStateAtTime(timeMs) {
        if (this.keyframes.length === 1) {
            const k = this.keyframes[0];
            return { x: k.x, y: k.y, scale: k.scale, isMoving: false, velocity: 0 };
        }
        // Before first keyframe
        if (timeMs <= this.keyframes[0].timeMs) {
            const k = this.keyframes[0];
            return { x: k.x, y: k.y, scale: k.scale, isMoving: false, velocity: 0 };
        }
        // After last keyframe
        if (timeMs >= this.keyframes[this.keyframes.length - 1].timeMs) {
            const k = this.keyframes[this.keyframes.length - 1];
            return { x: k.x, y: k.y, scale: k.scale, isMoving: false, velocity: 0 };
        }
        // Find keyframe interval [k1, k2]
        for (let i = 0; i < this.keyframes.length - 1; i++) {
            const k1 = this.keyframes[i];
            const k2 = this.keyframes[i + 1];
            if (timeMs >= k1.timeMs && timeMs <= k2.timeMs) {
                const dt = Math.max(1, k2.timeMs - k1.timeMs);
                const u = (timeMs - k1.timeMs) / dt;
                let factor;
                if (k2.easing === 'spring') {
                    factor = springEase(u);
                }
                else if (k2.easing === 'linear') {
                    factor = u;
                }
                else {
                    factor = easeInOutCubic(u);
                }
                const x = k1.x + (k2.x - k1.x) * factor;
                const y = k1.y + (k2.y - k1.y) * factor;
                const scale = k1.scale + (k2.scale - k1.scale) * factor;
                const dist = Math.hypot(k2.x - k1.x, k2.y - k1.y);
                const velocity = (dist / dt) * 1000;
                return {
                    x,
                    y,
                    scale,
                    isMoving: velocity > 10,
                    velocity
                };
            }
        }
        const last = this.keyframes[this.keyframes.length - 1];
        return { x: last.x, y: last.y, scale: last.scale, isMoving: false, velocity: 0 };
    }
}
