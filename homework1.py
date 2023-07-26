import math
num1= float(input("Enter your first number:"))
num2= float(input("Enter your second number:"))

print("Choose an operation:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Radical")
print("6.Factorial")
print("7.Sine")
print("8.Cosine")
print("9.Tangent")
print("10.cotangent")

choice=int(input("Enter choice:"))

if choice==1:
    result=num1+num2
elif choice==2:
    result=num1-num2
elif choice==3:
    result=num1*num2
elif choice==4:
    result=num1/num2
elif choice==5:
   result=math.sqrt(num1)+math.sqrt(num2)
elif choice==6:
    result=math.factorial(num1)+math.factorial(num2)
elif choice==7:
    result=math.sin(num1)+math.sin(num2)
elif choice==8:
    result=math.cos(num1)+math.cos(num2)
elif choice==9:
    result=math.tan(num1)+math.tan(num2)
elif choice==10:
    result=1/math.tan(num1)+1/math.tan(num2)
else:
    print("Invalid input")
print("The result is:", result)

