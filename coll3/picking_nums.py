def pickingNumbers(a: list[int]) -> int:
    from collections import Counter
    count = Counter(a)
    max_len = 0
    for num in count:
        max_len = max(max_len, count[num] + count.get(num + 1, 0))
    return max_len