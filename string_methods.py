# Basic Methods
s = "Hello, World!"
print(s.upper())           
print(s.lower())            
print(s.replace('o', 'x'))  
print(s.count('l'))         

# Vowel Counter (from file)
name = input("Enter name: ")
vowels = "aeiouAEIOU"
v_count = 0
c_count = 0

for char in name:
    if char.isalpha():
        if char in vowels:
            v_count += 1
        else:
            c_count += 1

print(f"Vowels: {v_count}, Consonants: {c_count}")

# String Analyzer
text = input("Enter text: ")
print(f"Length: {len(text)}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Words: {len(text.split())}")
print(f"Spaces: {text.count(' ')}")