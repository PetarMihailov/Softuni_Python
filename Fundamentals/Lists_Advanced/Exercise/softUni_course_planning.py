courses = input().split(", ")
command = input()

while not command == "course start":
    command = command.split(":")
    if command[0] == "Add" and command[1] not in courses:
        courses.append(command[1])
    elif command[0] == "Insert":
        index = int(command[2])
        if index in range(len(courses)) and command[1] not in courses:
            courses.insert(index, command[1])
    elif command[0] == "Remove" and command[1] in courses:
        courses.remove(command[1])
        if f"{command[1]}-Exercise" in courses:
            courses.remove(f"{command[1]}-Exercise")
    elif command[0] == "Swap" and command[1] in courses and command[2] in courses:
        index_1 = courses.index(command[1])
        index_2 = courses.index(command[2])
        courses[index_1], courses[index_2] = courses[index_2], courses[index_1]
        if f"{command[1]}-Exercise" in courses:
            courses.remove(f"{command[1]}-Exercise")
            courses.insert(index_2 + 1, f"{command[1]}-Exercise")
        if f"{command[2]}-Exercise" in courses:
            courses.remove(f"{command[2]}-Exercise")
            courses.insert(index_1 + 1, f"{command[2]}-Exercise")
    elif command[0] == "Exercise":
        if command[1] in courses and not f"{command[1]}-Exercise" in courses:
            index = courses.index(command[1])
            courses.insert(index + 1, f"{command[1]}-Exercise")
        elif command[1] not in courses:
            courses.append(command[1])
            courses.append(f"{command[1]}-Exercise")

    command = input()

for index, value in enumerate(courses, start=1):
    print(f"{index}.{value}")
