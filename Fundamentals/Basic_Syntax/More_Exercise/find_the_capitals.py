word = list(input())

capitals = [index for index in range(len(word)) if word[index].isupper()]

print(capitals)
