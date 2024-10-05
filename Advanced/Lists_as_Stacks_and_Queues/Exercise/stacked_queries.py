lines = int(input())

stack = []

for _ in range(lines):
    query = [int(el) for el in input().split()]
    if len(query) == 2:
        stack.append(query[1])
    elif query[0] == 2 and stack:
        stack.pop()
    elif query[0] == 3 and stack:
        print(max(stack))
    elif query[0] == 4 and stack:
        print(min(stack))

print(", ".join([str(el) for el in stack][::-1]))

