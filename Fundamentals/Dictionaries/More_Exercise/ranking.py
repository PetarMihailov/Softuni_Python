data = input()

contests = {}

while not data == "end of contests":
    contest, password = data.split(":")
    contests[contest] = password

    data = input()

data = input()

interns = {}

while not data == "end of submissions":
    contest, password, username, points = data.split("=>")
    points = int(points)

    if contest in contests and contests[contest] == password:
        if username not in interns:
            interns[username] = {contest: points}
        if contest not in interns[username]:
            interns[username][contest] = points
        if interns[username][contest] < points:
            interns[username][contest] = points

    data = input()

best_candidate = ""
high_score = 0

for name, value in interns.items():
    result = 0
    for val in value.values():
        result += val

    if result > high_score:
        high_score = result
        best_candidate = name

print(f"Best candidate is {best_candidate} with total {high_score} points.\nRanking:")

for key, value in sorted(interns.items()):
    print(key)
    for course, points in sorted(value.items(), key=lambda x: -x[1]):
        print(f"#  {course} -> {points}")
