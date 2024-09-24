def characters_in_range(start, end):
    result = [chr(char) for char in range(ord(start)+1, ord(end))]
    return " ".join(result)


char_1 = input()
char_2 = input()

print(characters_in_range(char_1, char_2))
