def migratoryBirds(arr):
    from collections import Counter
    count = Counter(arr)
    max_count = max(count.values())
    return min(k for k, v in count.items() if v == max_count)