F = 1
while F <= 10:
    for i in range(1, 11):
        for j in range(F, min(F + 3, 11)):
            print(f"{j} x {i} = {j * i}", end = "   ")
        print()
    print()
    F += 3