n = int(input())

names = set()

for _ in range(n):
    names.add(input())

[print(name) for name in names]

# second solution

print("\n".join(set(input() for _ in range(int(input())))))
