def flatten_arr(arr):
    flattened_arr = []
    for item in arr:
        if isinstance(item, list):
            for subitem in flatten_arr(item):
                flattened_arr.append(subitem)
        else:
            flattened_arr.append(item)
    return flattened_arr

print(flatten_arr([13, [200, 3], [4, [5, [5,[1.3]]],]]))  
