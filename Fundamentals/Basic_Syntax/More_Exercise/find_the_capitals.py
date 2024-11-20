word = list(input())

capitals = [index for index in range(len(word)) if word[index].isupper()]

print(capitals)

# second solution

string = input()

indexes = [index for index, char in enumerate(string) if char.isupper()]

print(indexes)
