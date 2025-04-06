num = int(input("Enter a number: "))

def factorial(n):
    if n < 0:
        return "Invalid input"
    elif n == 0 or n == 1:
        return 1
    else :
        return n * factorial(n - 1)
    
print(factorial(num))