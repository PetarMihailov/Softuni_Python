data = sorted(input().split(), key=lambda x: len(x))

result = 0

for index in range(len(data[0])):
    result += ord(data[0][index]) * ord(data[1][index])

reminder = sum([ord(el) for el in data[1][len(data[0]):]])

print(result + reminder)
