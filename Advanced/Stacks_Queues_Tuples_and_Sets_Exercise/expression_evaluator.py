from collections import deque

elements = input().split()
numbers = deque()


def operation(operator, a, b):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a // b


for el in elements:
    if el in "+-*/":
        while len(numbers) > 1:
            first = numbers.popleft()
            second = numbers.popleft()

            result = operation(el, first, second)
            numbers.appendleft(result)

    else:
        numbers.append(int(el))

print(numbers.popleft())

# second solution

from collections import deque

elements = input().split()
numbers = deque()

operators = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b
}
for el in elements:
    if el in "+-*/":
        while len(numbers) > 1:
            first = numbers.popleft()
            second = numbers.popleft()

            result = operators[el](first, second)
            numbers.appendleft(result)

    else:
        numbers.append(int(el))

print(numbers.popleft())
