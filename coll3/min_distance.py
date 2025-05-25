def minimum_distances(a: list[int]) -> int:
    last_seen = {}
    min_dist = float('inf')
    for i, num in enumerate(a):
        if num in last_seen:
            min_dist = min(min_dist, i - last_seen[num])
        last_seen[num] = i
    return min_dist if min_dist != float('inf') else -1