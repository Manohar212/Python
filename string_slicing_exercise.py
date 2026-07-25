#Exercise 
s="Hello world"
print(s[1])
print(s[-1])
print(s[1:3])
print(s[1:-1])
print(s[:3])
print(s[2:])
print(s[:-1])
print(s[::2])
print(s[1::2])
print(s[::-1])

# Practical Applications
sentence = input("Enter sentence: ")
words = sentence.split()
first_word = words[0]
last_word = words[-1]
print(f"First: {first_word}")
print(f"Last: {last_word}")

# Extract initials
name = input("Enter full name: ")
names = name.split()
initials = "".join([n[0] for n in names])
print(f"Initials: {initials}")