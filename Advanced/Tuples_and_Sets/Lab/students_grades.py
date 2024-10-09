n = int(input())

students = {}

for _ in range(n):
    student, grade = input().split()
    grade = float(grade)
    if student not in students:
        students[student] = [grade]
    else:
        students[student] += [grade]

for key, value in students.items():
    print(f"{key} -> {' '.join([f'{el:.2f}' for el in value])} (avg: {sum(value)/len(value):.2f})")

# soltion with mean

from statistics import mean

students = int(input())

grades = {}

for _ in range(students):
    name, grade = input().split()
    grade = float(grade)
    if name not in grades:
        grades[name] = []
    grades[name].append(grade)

for data in grades.items():
    print(f"{data[0]} -> {' '.join([f'{el:.2f}' for el in data[1]])} (avg: {mean(data[1]):.2f})")
