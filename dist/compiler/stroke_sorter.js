/**
 * Calculates Euclidean distance between two 2D points.
 */
export function distance(p1, p2) {
    const dx = p1.x - p2.x;
    const dy = p1.y - p2.y;
    return Math.sqrt(dx * dx + dy * dy);
}
/**
 * Optimizes stroke order using Nearest-Neighbor TSP with narrative priority support.
 * Minimizes hand travel distance (pen-lift distance) between disconnected strokes.
 */
export function optimizeStrokeOrder(strokes) {
    if (strokes.length <= 1)
        return [...strokes];
    // Group strokes by priority if present (subject-first drawing order)
    const priorityGroups = new Map();
    for (const s of strokes) {
        const prio = s.priority ?? 0;
        if (!priorityGroups.has(prio)) {
            priorityGroups.set(prio, []);
        }
        priorityGroups.get(prio).push(s);
    }
    const sortedPriorities = Array.from(priorityGroups.keys()).sort((a, b) => a - b);
    const result = [];
    let currentPos = { x: 0, y: 0 };
    for (const prio of sortedPriorities) {
        const group = priorityGroups.get(prio);
        const remaining = [...group];
        // If starting fresh, start from top-left-most stroke (natural drawing start)
        if (result.length === 0) {
            remaining.sort((a, b) => (a.startPoint.y + a.startPoint.x * 0.5) - (b.startPoint.y + b.startPoint.x * 0.5));
            const first = remaining.shift();
            result.push(first);
            currentPos = first.endPoint;
        }
        // Nearest Neighbor chaining
        while (remaining.length > 0) {
            let nearestIdx = 0;
            let minDst = Infinity;
            for (let i = 0; i < remaining.length; i++) {
                const dst = distance(currentPos, remaining[i].startPoint);
                if (dst < minDst) {
                    minDst = dst;
                    nearestIdx = i;
                }
            }
            const nextStroke = remaining.splice(nearestIdx, 1)[0];
            result.push(nextStroke);
            currentPos = nextStroke.endPoint;
        }
    }
    return result;
}
