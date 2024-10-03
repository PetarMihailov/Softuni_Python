from collections import deque

liters = int(input())
name = input()

queue = deque()

while not name == "Start":
    queue.append(name)
    name = input()

data = input()

while not data == "End":
    if data.startswith("refill"):
        liters += int(data.split()[1])
    else:
        liter = int(data)
        if liters >= liter:
            liters -= liter
            print(f"{queue.popleft()} got water")
        else:
            print(f"{queue.popleft()} must wait")

    data = input()

print(f"{liters} liters left")
