from collections import deque

numbers = deque([int(el) for el in input().split()])
count = int(input())

result = []

while numbers:
    numbers.rotate(-count)
    executed = numbers.pop()
    result.append(executed)

print(f"[{','.join(map(str, result))}]")
