a = input("Enter the three numbers separated by commas: ")

x,y,z = a.split(",")
num1 = int(x)
num2 = int(y)
num3 = int(z)

if num1 > num2 and num1 > num3:
    print("The largest number is: ", num1)
elif num2 >num1 and num2 > num3:
    print("The largest number is: ", num2)
else:
    print("The largest number is: ", num3)

print("The end of the program")