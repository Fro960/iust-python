f =1
d = int(input("enter any number"))
def fact(x, b):
    for i in range(1, x+1):
        b = b * i
    return b
y = fact(d,f)
print(y)