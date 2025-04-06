list = (6, 9, 3)
a = list[0]
b = list[1]
c = list[2]

def max_of_three(list):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
print( max_of_three(list) )