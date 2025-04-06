length = input("Enter the length of the rectangle: ")
width = input("Enter the width of the rectangle: ")

def area_of_rectangle(length, width) : 
    length=float(length)
    width=float(width)

    return length * width

print(area_of_rectangle(length, width))