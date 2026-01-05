students = int(input("Enter number of students: "))

passed = 0
failed = 0

while students > 0:
    marks = int(input("Enter marks: "))
    if marks < 0:
        break
    elif marks > 100:
        continue
    elif marks == 0:
        pass
    elif marks >= 40:
        passed += 1
    else:
        failed += 1
    students -= 1

print(f"Total passed = {passed} \nTotal Failed = {failed}")