lines = int(input())

students = {}

for _ in range(lines):
    name, grade = input(), float(input())
    if name not in students:
        students[name] = []
    students[name].append(grade)

average_grades = {}

for name, grades in students.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f"{name} -> {average_grade:.2f}")

