divisible_nums = []

def divisible_numbers(list, divisor):
    for i in list:
        if i % divisor == 0:
            divisible_nums.append(i)
    return len(divisible_nums)

print(divisible_numbers([10, 15, 20, 25, 31], 5))