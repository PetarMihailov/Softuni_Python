n = int(input())

names = set()

for _ in range(n):
    names.add(input())

[print(el) for el in names]
