import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def square_root(x):
    return math.sqrt(x)

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def cot(x):
    return 1 / math.tan(x)

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Square root")
print("6.Factorial")
print("7.Sin")
print("8.Cos")
print("9.Tan")
print("10.Cot")

while True:
    choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

    elif choice in ('5', '6', '7', '8', '9', '10'):
        num = float(input("Enter a number: "))

        if choice == '5':
            print("Square root of", num, "=", square_root(num))

        elif choice == '6':
            print("Factorial of", num, "=", factorial(num))

        elif choice == '7':
            print("Sin(", num, ") =", sin(num))

        elif choice == '8':
            print("Cos(", num, ") =", cos(num))

        elif choice == '9':
            print("Tan(", num, ") =", tan(num))

        elif choice == '10':
            print("Cot(", num, ") =", cot(num))
    else:
        print("Invalid Input")

