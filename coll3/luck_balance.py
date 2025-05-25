def luckBalance(k: int, contests: list[list[int]]) -> int:
    important = []
    total = 0
    for luck, importance in contests:
        if importance == 1:
            important.append(luck)
        else:
            total += luck
    important.sort(reverse=True)
    total += sum(important[:k]) - sum(important[k:])
    return total