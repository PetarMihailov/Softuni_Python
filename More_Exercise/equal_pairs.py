import sys

n = int(input())

result = []
max_diff = -sys.maxsize

for _ in range(n):
    first, second = int(input()), int(input())
    result.append((first, second))

equal = True

for index in range(n-1):
    diff = abs(sum(result[index]) - sum(result[index+1]))
    if diff:
        equal = False
    if diff > max_diff:
        max_diff = diff

if equal:
    print(f"Yes, value={sum(result[0])}")
else:
    print(f"No, maxdiff={max_diff}")

# second solution

import sys

n = int(input())

result = [(int(input()), int(input())) for _ in range(n)]
max_diff = -sys.maxsize

equal = True

for index in range(n-1):
    diff = abs(sum(result[index]) - sum(result[index+1]))
    if diff:
        equal = False
    if diff > max_diff:
        max_diff = diff

if equal:
    print(f"Yes, value={sum(result[0])}")
else:
    print(f"No, maxdiff={max_diff}")
