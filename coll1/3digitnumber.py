num = input("Enter a 3-digit number(100-999): " )
my_digits = []


def split_three_digit_number(num):
    for i in num :
        a= int(i)
        my_digits.append(a)
    if len(num) != 3 :
        print("invalid number")
    return my_digits

final_tuple = tuple((split_three_digit_number(num)))
print(final_tuple)

