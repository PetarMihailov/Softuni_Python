text = input()

result = text[0]

for char in text:
    if not char == result[-1]:
        result += char

print(result)
