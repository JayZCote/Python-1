#input
history = float(input("Please enter grade for history:"))
science = float(input("Please enter grade for science:"))
math = float(input("Please enter grade for math:"))

#processing
average = (history + science + math)/3

if average >= 90:
    print("Grade: A")

elif 80 <= average <= 89:
    print("Grade: B")

elif 70 <= average <= 79:
    print("Grade: C")

elif 60 <= average <= 69:
    print("Grade: D")

else:
    print("Grade: F")