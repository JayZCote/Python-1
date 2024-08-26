#input
weight = float(input("Enter your weight in kilograms:"))
height = float(input("Enter your height in meters:"))

#processing
BMI = weight/(height**2)

#output
print("Your BMI is: ", BMI)