def check_integer(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    return "Zero"

num = int(input("Enter number: "))
print(check_integer(num))