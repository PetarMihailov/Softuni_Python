n = int(input())

for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()

for i in range(n-1, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

# second solution

n = int(input())

for i in range(1, n + 1):
    print('*' * i)

for i in range(n - 1, 0, -1):
    print('*' * i)
