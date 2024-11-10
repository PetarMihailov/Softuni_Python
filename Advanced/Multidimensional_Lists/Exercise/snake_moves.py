from collections import deque
rows, cols = [int(el) for el in input().split()]
word = deque(input())

matrix = []

for row_index in range(rows):
    matrix.append([0 for el in range(cols)])

for row_index in range(rows):
    for col_index in range(cols):
        current_char = word.popleft()
        matrix[row_index][col_index] = current_char
        word.append(current_char)

for row_index in range(rows):
    if row_index % 2 == 1:
        matrix[row_index].reverse()
    print("".join(matrix[row_index]))

# second solution

rows, cols = [int(el) for el in input().split()]
string = input()

matrix = []

for row in range(rows):
    matrix.append([0 for _ in range(cols)])

string_index = 0

for row in range(rows):
    for col in range(cols):
        matrix[row][col] = string[string_index]
        string_index += 1
        if string_index == len(string):
            string_index = 0

for row, col in enumerate(matrix):
    if not row % 2 == 0:
        col.reverse()
    print(''.join(col))

# third solution

rows, cols = list(map(int, input().split()))
word = input()

index = 0

matrix = []

for row in range(rows):
    row_elements = [None] * cols
    if row % 2 == 0:
        for col in range(cols):
            row_elements[col] = word[index % len(word)]
            index += 1
        print(*row_elements, sep="")
    else:
        for col in range(cols-1, -1, -1):
            row_elements[col] = word[index % len(word)]
            index += 1
        print(*row_elements, sep="")
