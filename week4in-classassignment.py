grades = [78, 45, 89, 55, 67, 48, 92, 38, 75, 61]

total = 0
for grade in grades:
    total += grade

average = total / len(grades)

passed = 0
failed = 0
index = 0

while index < len(grades):
    if grades[index] >= 70:
        passed += 1

    else:
        failed += 1
    index += 1

print("average grade:", average)
print("Number of students passed", passed)
print("Number of students failed:", failed)