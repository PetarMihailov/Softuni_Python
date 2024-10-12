stack = [int(el) for el in input().split()]

while stack:
    print(stack.pop(), end=" ")

# second solution

numbers = list(map(int, input().split()))

[print(numbers[index], end=" ") for index in range(len(numbers)-1, -1, -1)]
