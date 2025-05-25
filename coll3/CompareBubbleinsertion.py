def compare_swaps_bubble_insertion_sort(arr):
    bubble_swaps = 0
    insertion_swaps = 0
    n = len(arr)
    
    # Bubble sort swaps
    bubble_arr = arr.copy()
    for i in range(n):
        for j in range(n-1):
            if bubble_arr[j] > bubble_arr[j+1]:
                bubble_arr[j], bubble_arr[j+1] = bubble_arr[j+1], bubble_arr[j]
                bubble_swaps += 1
    
    # Insertion sort swaps
    insertion_arr = arr.copy()
    for i in range(1, len(insertion_arr)):
        key = insertion_arr[i]
        j = i-1
        while j >=0 and key < insertion_arr[j]:
            insertion_arr[j+1] = insertion_arr[j]
            insertion_swaps += 1
            j -= 1
        insertion_arr[j+1] = key
    
    return "insertion" if insertion_swaps <= bubble_swaps else "bubble"