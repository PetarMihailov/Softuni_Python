numbers = [int(el) for el in input().split()]
n = int(input())

for _ in range(n):
    numbers.remove(min(numbers))

print(", ".join([str(el) for el in numbers]))

# second solution

numbers = list(map(int, input().split()))
count = int(input())

[numbers.remove(min(numbers)) for _ in range(count)]

print(", ".join([str(el) for el in numbers]))
