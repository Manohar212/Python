#GREETING THE USER ✌️✌️

print("Welcome to Simple Calculator")

#TAKING INPUT FROM THE USER  💕💕
value1=float(input("Enter first number:"))
value2=float(input("Enter second number:"))
operation=input("select an operation (Addition/Subtraction/Multiplication/Divison):")
#PERFORMING CALCULATION BASED ON USER INPUT  🤩🤩
if operation=="Addition":
    print(f"Addition of {value1} and {value2} is {value1+value2}")
elif operation=="Subtraction":
    print(f"Subtraction of {value1} and {value2} is {value1-value2}")
elif operation=="Multiplication":
    print(f"Multiplication of {value1} and {value2} is {value1*value2}")
elif operation=="Divison":
    print(f"Divison of {value1} and {value2} is {value1/value2}")
# if invalid operation is selected the else statement will be executed
else:
    print("invalid operation selected")

#CLOSING MESSAGE  😘😘
print("Thank you for using Simple Calculator 🤭🤭")