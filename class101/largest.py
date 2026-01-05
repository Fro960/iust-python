def largest(x, y):
    if x > y:
        return x
    else:
        return y
    
x = int(input("What's x: "))
y = int(input("What's y: "))
print(f"{largest(x, y)} is larger!")
