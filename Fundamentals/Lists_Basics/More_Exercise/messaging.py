sequence = input().split()
text = list(input())

indexes = [sum(map(int, list(el))) for el in sequence]
message = []

for el in indexes:
    index = el
    if index >= len(text):
        index -= len(text)

    char = text.pop(index)
    message.append(char)

print("".join(message))

# second solution

sequence = input().split()
text = list(input())

message = ""

for num in sequence:
    index = sum(int(digit) for digit in num)
    if index >= len(text):
        index -= len(text)

    message += text.pop(index)

print(message)

# third solution

sequence = input().split()
text = list(input())

message = ""

for num in sequence:
    index = sum(int(digit) for digit in num)
    index %= len(text)

    message += text.pop(index)

print(message)

