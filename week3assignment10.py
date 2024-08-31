#input
age = int(input("Enter your age: "))

#processing
if age > 0:
    if age < 18:
        print("Minor")

    elif 18<= age <=65:
        print("Adult")

    else:
        print("Senior citizen")
else:
    print("Error: Age must be a positive number")

