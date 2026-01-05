def is_even(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"

num = int(input("Enter number: "))
print(is_even(num))