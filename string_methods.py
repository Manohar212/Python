#python string manipulation examples 

#define originaal string

s="Hello, world!"

#converting the string to uppercase]
print(s.upper())

#converting the string to lowercase
print(s.lower())

#remove leading and trailing white spaces from the string
print(s.strip())

#replaces all accurances of 'o' with 'x' in the string
print(s.replace ('o','x'))

#count the number of occurences of 'a' in the string
print("Abracadabra".count('a'))

print(f"First character: {s[0]}")
print(f"Last character: {s[-1]}")

name = input("Enter your name: ")
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for char in name:
    if char.isalpha():
        if char in vowels:
            vowel_count +=1
        else:
            consonant_count +=1

print(f"Number of vowels in your name: {vowel_count}")
print(f"Number of consonants in your name: {consonant_count}")