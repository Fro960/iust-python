import math

def main():
    x1 = int(input("Enter x1: "))
    x2 = int(input("Enter x2: "))
    y1 = int(input("Enter y1: "))
    y2 = int(input("Enter y2: "))
    print(f"Distance is {get_dist(x1, x2, y1, y2):.2f}")

def get_dist(x1, x2, y1, y2):
    x = pow((x1 - x2), 2)
    y = pow((y1 - y2), 2)
    dist = math.sqrt((x + y))
    return dist

main()