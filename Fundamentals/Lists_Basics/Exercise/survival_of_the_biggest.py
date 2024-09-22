numbers = [int(el) for el in input().split()]
n = int(input())

for _ in range(n):
    numbers.remove(min(numbers))

print(", ".join([str(el) for el in numbers]))
