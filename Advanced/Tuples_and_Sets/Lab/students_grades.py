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
