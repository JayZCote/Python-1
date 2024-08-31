#input
y = int(input("Enter in a year:"))

#processing
def is_leap_year(y):
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

if is_leap_year(y):
    print(y ,"is a leap year.")
else:
    print(y ,"is not a leap year.")