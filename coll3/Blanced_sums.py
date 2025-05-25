def balancedSums(arr: list[int]) -> str:
    total = sum(arr)
    left_sum = 0
    for i, num in enumerate(arr):
        if left_sum == total - left_sum - num:
            return "YES"
        left_sum += num
    return "NO"