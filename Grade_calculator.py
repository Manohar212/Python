m = int(input("Marks in Math: "))
s = int(input("Marks in Science: "))
e = int(input("Marks in English: "))

total_marks = m + s + e
average = total_marks / 3

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
else:
    grade = "Fail"

print(f"Total marks: {total_marks}")
print(f"Average marks: {average}")
print(f"Grade: {grade}")
