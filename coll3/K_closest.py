def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    points.sort(key=lambda p: p[0]**2 + p[1]**2)
    return points[:k]



