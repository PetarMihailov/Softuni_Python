command = input()

resources = {}

while not command == "stop":
    if command not in resources:
        resources[command] = 0
    resources[command] += int(input())

    command = input()

for key in resources:
    print(f"{key} -> {resources[key]}")
