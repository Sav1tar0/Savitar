def gameOfStones(n: int) -> str:
    return "First" if n % 7 not in [0, 1] else "Second"