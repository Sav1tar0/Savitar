def second_most_frequent(arr):
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1 
        else:
            frequency[num] = 1  
    max_freq = 0
    second_max_freq = 0
    for count in frequency.values():
        if count > max_freq:
            second_max_freq = max_freq 
            max_freq = count 
        elif count > second_max_freq and count < max_freq:
            second_max_freq = count  
    for num, count in frequency.items():
        if count == second_max_freq:
            return num  
print(second_most_frequent([1, 2, 2, 3, 3, 3, 4, 4, 4, 5])) 
