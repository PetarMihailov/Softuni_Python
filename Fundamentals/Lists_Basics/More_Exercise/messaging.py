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
