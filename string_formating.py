name="Alice"
age=30

#using the % operator  for string formatting(old-style)
print("My name is %s and Iam %d years old." % (name,age))

#using the str.format() method for string formatting
print("My name is {} and I am {} years old.".format(name,age))

#using f-strings for string formatting (Python 3.6+)
print(f"My name is {name} and I am {age} years old.")