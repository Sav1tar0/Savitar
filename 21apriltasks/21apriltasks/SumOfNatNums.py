def sum_natural(n):
    list = []
    for i in range(1, n + 1):
        list.append(i)
    return sum(list)

print(sum_natural(5))  