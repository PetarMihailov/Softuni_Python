data = input()

courses = {}

while ":" in data:
    student, _id, course = data.split(":")
    _id = int(_id)
    if course not in courses:
        courses[course] = {}
    courses[course][student] = _id

    data = input()

course = " ".join(data.split("_"))

for name, _id in courses[course].items():
    print(f"{name} - {_id}")

