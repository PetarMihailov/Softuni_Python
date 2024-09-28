data = input()

results = {}
submissions = {}

while not data == "exam finished":
    data = data.split("-")
    if data[1] == "banned" and data[0] in results:
        results.pop(data[0])
    elif data[0] not in results:
        results[data[0]] = {"language": data[1], "points": int(data[2])}
    elif data[0] in results and int(data[2]) > results[data[0]]["points"]:
        results[data[0]]["points"] = int(data[2])

    if not data[1] == "banned":
        if data[1] not in submissions:
            submissions[data[1]] = 0
        submissions[data[1]] += 1

    data = input()

print("Results:")
for key, val in results.items():
    print(f"{key} | {val['points']}")


print("Submissions:")
for key, val in submissions.items():
    print(f"{key} - {val}")

