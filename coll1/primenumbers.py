num = int(input("Enter a number: "))

def is_prime(n) :
    if n <= 1:
        return False
    for i in range(2,n) :
        if n % i == 0:
            return False
    else:
        return True
    
print(is_prime(num))