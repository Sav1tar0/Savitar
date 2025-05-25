def howManyGames(p: int, d: int, m: int, s: int) -> int:
    games = 0
    while s >= p:
        games += 1
        s -= p
        p = max(p - d, m)
    return games