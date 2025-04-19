def sum_digits(n):
    list = []
    for i in str(n):
        list.append(int(i))
    return sum(list)




print(sum_digits(1234))  