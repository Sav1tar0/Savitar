def icecreamParlor(m: int, cost: list[int]) -> list[int]:
    seen = {}
    for i, c in enumerate(cost, 1):
        if m - c in seen:
            return [seen[m - c], i]
        seen[c] = i
    return []