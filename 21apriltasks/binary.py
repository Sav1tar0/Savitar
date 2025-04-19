def to_binary(n):
    list = []
    while n >= 1:
        list.append(n % 2)
        n = n // 2
    for i in list[::-1]:
        print(i, end='')
    
             
            
        

print(to_binary(150))  