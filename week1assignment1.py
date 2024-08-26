#input
Principal = int(input("Enter principal amount:"))
Rate = int(input("Enter interest rate:"))
Time = int(input("Enter the time period (in years):"))

#processing
Interest = (Principal * Rate * Time)/100

#output
print("The calculated simple interest is", Interest)