def ascii_sum_between_chars(char1, char2, random_string):
    ascii1, ascii2 = ord(char1), ord(char2)
    start, end = min(ascii1, ascii2), max(ascii1, ascii2)
    total_sum = sum(ord(char) for char in random_string if start < ord(char) < end)
    print(total_sum)


char1 = input()
char2 = input()
random_string = input()

ascii_sum_between_chars(char1, char2, random_string)
