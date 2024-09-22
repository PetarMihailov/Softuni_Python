n = int(input())
word = input()

strings = [input() for _ in range(n)]
filtered = [el for el in strings if word in el]

print(strings)
print(filtered)
