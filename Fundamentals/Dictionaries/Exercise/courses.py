data = input()

courses= {}

while not data == "end":
    course, student = data.split(" : ")
    if course not in courses:
        courses[course] = []
    courses[course].append(student)

    data = input()

for key, value in courses.items():
    print(f"{key}: {len(value)}")
    for student in value:
        print(f"-- {student}")
