data = input()

phonebook = {}

while not data.isdigit():
    name, number = data.split("-")
    phonebook[name] = number

    data = input()

line = int(data)

for _ in range(line):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")
