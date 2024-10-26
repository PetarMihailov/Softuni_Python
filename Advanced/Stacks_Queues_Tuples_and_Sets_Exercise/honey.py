from collections import deque

bees = deque([int(el) for el in input().split()])
nectars = [int(el) for el in input().split()]
symbols = deque(input().split())

honey = 0

operators = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y
}

while bees and nectars:
    bee = bees[0]
    nectar = nectars.pop()

    if bee > nectar:
        continue

    bees.popleft()
    operator = symbols.popleft()

    try:
        honey += abs(operators[operator](bee, nectar))
    except:
        pass



print(f"Total honey made: {honey}")

if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectars:
    print(f"Nectar left: {', '.join(map(str, nectars))}")

# solution without try, except

from collections import deque

bees = deque([int(el) for el in input().split()])
nectars = [int(el) for el in input().split()]
symbols = deque(input().split())

honey = 0

operators = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y if y > 0 else 0
}

while bees and nectars:
    bee = bees[0]
    nectar = nectars.pop()

    if bee > nectar:
        continue

    bees.popleft()
    operator = symbols.popleft()
    honey += abs(operators[operator](bee, nectar))

print(f"Total honey made: {honey}")

if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectars:
    print(f"Nectar left: {', '.join(map(str, nectars))}")
