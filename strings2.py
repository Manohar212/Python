student_name = "MANOHAR"
print(student_name[0])   
print(student_name[6])   
print(student_name[-1])  
print(student_name[-7])  

# Try yourself
your_name = input("enter your name: ")
print(f"First letter: {your_name[0]}")
print(f"Last letter: {your_name[-1]}")
print(f"Middle letter: {your_name[len(your_name)//2]}")

# Make analyzer
word = input("Enter a word: ")
print(f"Length: {len(word)}")
print(f"First: {word[0]}")
print(f"Last: {word[-1]}")
print(f"All characters:")
for i in range(len(word)):
    print(f"Index {i}: {word[i]}")