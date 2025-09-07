# l = int(input())
# b = int(input())
# product = l*b
# print(product)

def calculate_area(length,width):
    return length * width

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = calculate_area(length,width)

print(f"The area of rectangle is: {area}")