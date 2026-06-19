#This is for loop example 
#for loop used to print numbers from 0 to 9
for i in range (0,10):
    print(i)
#This is while loop example
#while loop used to print numbers from 0 to 100
i = 0
while i<=100:
    print(i)
    i+=1

#Questions 
#Print numbers from 10 to 1 using for loop
for i in range(10,0,-1):
    print(i)
#Print all even numbers between 1 and 20
for i in range(1,21):
    if i%2!=0:
        continue
    print(i)
#Print all odd numbers between 1 and 20
for i in range(1,21):
    if i%2==0:
        continue
    print(i)

#Print numbers from 1 to 100, show only even/odd
for i in range(1,101):
    if i%2 == 0:
        print(f"{i} is even ! ")
    elif i%2 != 0:
        print(f"{i} is odd ! ")


#find the sum of 1 to 100 
total = 0
for i in range(1,101):
    total=total+i
print(f"The sum of 1 to 100 is: {total}")

#find the sum of first n numbers 
num = int(input("Enter a number: "))
total = 0
for i in range(1,num+1):
    total=total+i
print(f"The sum of first {num} numbers is {total}")

#Reverse counting from user number
num = int(input("Enter a number : "))
for i in range(num,0,-1):
    print(i)

#Star Pattern
for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()
