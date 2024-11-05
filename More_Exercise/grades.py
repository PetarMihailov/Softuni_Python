students = int(input())

fail = []
average = []
good = []
excellent = []

for _ in range(students):
    grade = float(input())

    if grade < 3:
        fail.append(grade)
    elif 3 <= grade <= 3.99:
        average.append(grade)
    elif 4 <= grade <= 4.99:
        good.append(grade)
    else:
        excellent.append(grade)

average_grade = sum(fail + average + good + excellent) / students
percentage_fail = len(fail) / students * 100
percentage_average = len(average) / students * 100
percentage_good = len(good) / students * 100
percentage_excellent = len(excellent) / students * 100

print(f"Top students: {percentage_excellent:.2f}%")
print(f"Between 4.00 and 4.99: {percentage_good:.2f}%")
print(f"Between 3.00 and 3.99: {percentage_average:.2f}%")
print(f"Fail: {percentage_fail:.2f}%")
print(f"Average: {average_grade:.2f}")
