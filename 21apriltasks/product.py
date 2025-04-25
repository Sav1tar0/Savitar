def product_list(arr, index=0):
    if index == len(arr):
        return 1
    return arr[index] * product_list(arr, index + 1)


print(product_list([2, 3, 4]))
