def largestPermutation(k: int, arr: list[int]) -> list[int]:
    n = len(arr)
    pos = {val: i for i, val in enumerate(arr)}
    for i in range(n):
        if k == 0:
            break
        if arr[i] == n - i:
            continue
        swap_pos = pos[n - i]
        pos[arr[i]] = swap_pos
        pos[n - i] = i
        arr[i], arr[swap_pos] = arr[swap_pos], arr[i]
        k -= 1
    return arr