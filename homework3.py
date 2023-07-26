name=input("Enter your name:")
family=input("Enter your last name:")
grade1=float(input("Enter your grade for the first course:"))
grade2=float(input("Enter your grade for the second course:"))
grade3=float(input("Enter your grade for the third course:"))

avg=(grade1+grade2+grade3)/3
if avg>=17:
    status="Greate"
elif avg>=12:
    status="Normal"
else:
    status="Fail"
print("Name:",name)
print("Last name:", family)
print("Average:",avg)
print("Status:",status)

