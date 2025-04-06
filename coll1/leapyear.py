year = int(input("Enter a year: "))

def is_leap_year(year):
    if year % 4 == 0:
        print(True)
    elif year % 100 == 0:   
        print(False)
    elif year % 400 == 0:
        print(True)
    else:
        print(False)

print(is_leap_year(year))