import sys

rows, cols = [int(el) for el in input().split(", ")]

matrix = []

for _ in range(rows):
    matrix.append([int(el) for el in input().split(", ")])

max_value = -sys.maxsize
position = None

for row in range(rows-1, 0, -1):
    for col in range(cols-1, 0, -1):
        result = matrix[row][col] + matrix[row][col-1] + matrix[row-1][col] + matrix[row-1][col-1]

        if result >= max_value:
            max_value = result
            position = (row, col)

row, col = position

print(matrix[row-1][col-1], matrix[row-1][col])
print(matrix[row][col-1], matrix[row][col])
print(max_value)

# second solution

import sys

rows, cols = [int(el) for el in input().split(", ")]

matrix = []

for _ in range(rows):
    matrix.append([int(el) for el in input().split(", ")])

max_sub_matrix = None
max_sum = -sys.maxsize

for row in range(rows-1, 0, -1):
    for col in range(cols-1, 0, -1):
        sub_matrix = [matrix[row-1][col-1], matrix[row-1][col], matrix[row][col-1], matrix[row][col]]

        current_sum = sum(sub_matrix)

        if current_sum >= max_sum:
            max_sum = current_sum
            max_sub_matrix = sub_matrix

print(max_sub_matrix[0], max_sub_matrix[1])
print(max_sub_matrix[2], max_sub_matrix[3])
print(max_sum)
