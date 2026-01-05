def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x - 1)

num = int(input("Enter number: "))
print(factorial(num))