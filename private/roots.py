while True:
    a = int(input("Enter a: "))
    if a == 0:
        continue
    else:    
        b = int(input("Enter b: "))
        c = int(input("Enter c: "))
    dis = b**2 - 4 * a * c
    if dis > 0:
        print(f"roots are real and distinct")
    elif dis < 0:
        print(f"roots are complex")
    else:
        print(f"roots are real and equal")
    break

    

                  