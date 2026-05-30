print("Welcome to Simple Calculator")

value1=float(input("Enter first number:"))
value2=float(input("Enter second number:"))
operation=input("select an operation (Addition/Subtraction/Multiplication/Divison):")
if operation=="Addition":
    print(f"Addition of {value1} and {value2} is {value1+value2}")
elif operation=="Subtraction":
    print(f"Subtraction of {value1} and {value2} is {value1-value2}")
elif operation=="Multiplication":
    print(f"Multiplication of {value1} and {value2} is {value1*value2}")
elif operation=="Divison":
    print(f"Divison of {value1} and {value2} is {value1/value2}")
else:
    print("invalid operation selected")

print("Thank you for using Simple Calculator ")
