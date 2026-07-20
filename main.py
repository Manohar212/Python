# Original Weather Program
weather = input("Weather (sunny/rainy/snowy): ")
time_of_day = "night"

if weather == "sunny":
    if time_of_day == "day":
        print("Play with car")
    else:
        print("Sleep")
elif weather == "rainy":
    print("Play with boat")
elif weather == "snowy":
    if time_of_day == "night":
        print("Play with teddy")
    else:
        print("Play with snowman")
else:
    print("Read storybook")

# Your Program: Student Grade
score = int(input("Enter score (0-100): "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# Your Program: Age Category
age = int(input("Enter age: "))

if age < 13:
    category = "Child"
elif age < 18:
    category = "Teen"
elif age < 65:
    category = "Adult"
else:
    category = "Senior"

print(f"Category: {category}")