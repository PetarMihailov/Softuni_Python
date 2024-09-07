divisor = int(input())
bound = int(input())

n = 0

for i in range(1, bound + 1):
    if i % divisor == 0:
        n = i

print(n)

divisor = int(input())
bound = int(input())

n = 0

for i in range(bound, 0, -1):
    if i % divisor == 0:
        n = i
        break

print(n)

