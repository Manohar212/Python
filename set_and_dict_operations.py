skills = {"Python", "HTML", "CSS", "Python", "JavaScript"}

print(f'set of skills are {skills}')
skills.add('SQL')
print(f'set of skills after adding SQL are {skills}')

frontend = {"HTML", "CSS", "JavaScript"}
backend = {"Python", "SQL", "JavaScript"}

common_skills = frontend.intersection(backend)

# //common_skills = frontend&backend

print(f"Common Skills are {common_skills}")

#Dictionaries 

students = {
    "name" : "Manohar",
    "age" : 20,
    "course" : "Python Core",
    "marks" : [85,90,88]
}

print("Student Name: ")
print(students["name"])
students['is_passed'] = True

students['age']= 23

average = sum(students['marks'])/len(students['marks'])
print(f"Average Marks of Student: {average}")

print("\nStudent Details:")

for key, value in students.items():
    print(key, ":", value)