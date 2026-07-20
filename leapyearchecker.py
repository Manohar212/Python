# Original Leap Year
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# Test Cases:
# 2000 → leap (divisible by 400)
# 1900 → not leap (divisible by 100 but not 400)
# 2004 → leap (divisible by 4)
# 2001 → not leap (not divisible by 4)

# Your Program: Eligibility Checker
age = int(input("Age: "))
income = float(input("Annual income: "))

if (age >= 18 and age <= 65) and (income >= 20000):
    print("Eligible for loan")
else:
    print("Not eligible")

# Your Program: Game Access
is_member = input("Member? (yes/no): ").lower() == "yes"
age = int(input("Age: "))

if (is_member) or (age >= 18):
    print("Access granted")
else:
    print("Access denied")

# Your Program: Discount Calculator
purchase = float(input("Purchase amount: "))
is_member = input("Member? (yes/no): ").lower() == "yes"
is_holiday = input("Holiday sale? (yes/no): ").lower() == "yes"

discount = 0
if is_member:
    discount += 10
if is_holiday:
    discount += 20
if purchase > 500:
    discount += 5

final_price = purchase * (1 - discount/100)
print(f"Discount: {discount}%, Final price: {final_price:.2f}")