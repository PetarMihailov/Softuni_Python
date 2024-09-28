lines = int(input())

cars = {}

for _ in range(lines):
    command = input().split()

    if command[0] == "register":
        name, plate = command[1], command[2]

        if name not in cars:
            cars[name] = plate
            print(f"{name} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {cars[name]}")
    elif command[0] == "unregister":
        name = command[1]

        if name in cars:
            del cars[name]
            print(f"{name} unregistered successfully")
        else:
            print(f"ERROR: user {name} not found")

for key, val in cars.items():
    print(f"{key} => {val}")
