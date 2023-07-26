a=float(input("Enter your first number:"))
b=float(input("Enter your second number:"))
c=float(input("Enter your third number:"))
if a+b>c and c+a>b and b+c>a:
    print("These number can form a triangle.")
else:
    print("These number cannot form a triangle.")