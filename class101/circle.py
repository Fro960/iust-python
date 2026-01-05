def area(radius):
    PI = 3.14
    area = PI * radius ** 2
    return area

radius = int(input("Enter radius: "))
print(area(radius))