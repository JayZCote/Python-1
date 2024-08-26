#input
x1 = float(input("Enter x1:"))
y1 = float(input("Enter x2:"))
x2 = float(input("Enter y1:"))
y2 = float(input("Enter y2:"))

#processing
distance = ((x2 -x1)**2 + (y2-y1)**2)**.5

#output
print("The distance between the two points is:", distance)