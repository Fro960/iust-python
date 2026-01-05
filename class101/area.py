import math

def main():
    global pi
    pi = math.pi
    radius = int(input("Enter radius: "))
    print(f"Area of circle is {area(radius):.2f}")
    print(f"Circumference of circle is {circumference(radius):.2f}")

def area(r):
    area = pi * math.pow(r, 2)
    return area

def circumference(r):
    circumference = 2 * pi * r
    return circumference

main()