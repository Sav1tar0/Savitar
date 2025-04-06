list = [23, 45, 67, 89, 12, 34, 56, 78, 90]

def average(numbers):
    total = sum(numbers)
    count = len(numbers)
    avg = total / count
    return avg

print(average(list))