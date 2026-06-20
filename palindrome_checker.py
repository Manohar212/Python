palindrome = input("Enter a string to check if it's a palindrome: ")
new_palindrome = palindrome[::-1]
if palindrome == new_palindrome:
    print(f"{palindrome} is a palindrome. ")
else:
    print(f"{palindrome} is not a palindrome. ")