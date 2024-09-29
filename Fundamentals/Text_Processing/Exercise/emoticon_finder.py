text = input()

result = []

for index in range(len(text)):
    if text[index] == ":":
        result.append(text[index:index+2])

print("\n".join(result))
