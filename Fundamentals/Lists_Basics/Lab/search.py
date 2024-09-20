n = int(input())
include = input()

text = []
filter = []

for i in range(n):
    word = input()
    text.append(word)
    if include in word:
        filter.append(word)

print(text)
print(filter)
