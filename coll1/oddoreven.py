num = int(input("Enter a number: "))

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
print(is_even(num))