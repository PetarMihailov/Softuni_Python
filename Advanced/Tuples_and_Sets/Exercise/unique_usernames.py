n = int(input())

names = set()

for _ in range(n):
    names.add(input())

[print(el) for el in names]

# second splution

print("\n".join(set([input() for _ in range(int(input()))])))
