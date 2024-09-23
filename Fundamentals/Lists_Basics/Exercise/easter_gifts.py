gifts = input().split()
command = input()

while not command == "No Money":
    command = command.split()
    if command[0] == "OutOfStock" and command[1] in gifts:
        gifts = [item.replace(command[1], "None") for item in gifts]
    elif command[0] == "Required" and int(command[2]) in range(len(gifts)):
        index = int(command[2])
        gifts[index] = command[1]
    elif command[0] == "JustInCase":
        gifts[-1] = command[1]

    command = input()

print(" ".join([item for item in gifts if not item == "None"]))
