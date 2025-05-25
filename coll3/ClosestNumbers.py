def closestNumbers(arr: list[int]) -> list[int]:
    arr.sort()
    min_diff = float('inf')
    result = []
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i-1]
        if diff < min_diff:
            min_diff = diff
            result = [arr[i-1], arr[i]]
        elif diff == min_diff:
            result.extend([arr[i-1], arr[i]])
    return result