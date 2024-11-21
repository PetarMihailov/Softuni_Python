from collections import deque

numbers = deque([int(el) for el in input().split()])
count = int(input())

result = []

while numbers:
    numbers.rotate(-count)
    executed = numbers.pop()
    result.append(executed)

print(f"[{','.join(map(str, result))}]")

#  second solution

people = list(map(int, input().split()))
count = int(input())

result = []
index = 0

while people:
    index = (index + count - 1) % len(people)
    result.append(people.pop(index))

print(f"[{','.join(map(str, result))}]")
