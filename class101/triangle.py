import math

def main():
    base = int(input("Enter base: "))
    perp = int(input("Enter perp: "))
    print(hypo(base, perp))

def hypo(b, p):
    return math.hypot(b, p)

main()