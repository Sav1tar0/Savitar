def is_sorted(arr, index=0):
    if index == len(arr) - 1:
        return True
    if arr[index] > arr[index + 1]:
        return False
    return is_sorted(arr, index + 1)
    




print(is_sorted([1, 2, 3, 4]))