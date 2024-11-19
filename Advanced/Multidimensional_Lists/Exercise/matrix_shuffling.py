def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


def is_valid_command(command, rows, cols):
    if not len(command) == 5 or not command[0] == "swap":
        return False

    try:
        row1, col1, row2, col2 = map(int, command[1:])
    except ValueError:
        return False

    if (
            row1 < 0 or row1 >= rows or col1 < 0 or col1 >= cols or
            row2 < 0 or row2 >= rows or col2 < 0 or col2 >= cols
    ):
        return False
    return True

rows, cols = map(int, input().split())

matrix = [input().split() for _ in range(rows)]

while True:
    command = input().split()
    if command[0] == "END":
        break

    if is_valid_command(command, rows, cols):
        row1, col1, row2, col2 = map(int, command[1:])
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        print_matrix(matrix)
    else:
        print("Invalid input!")

# second solution

def print_matrix(matr):
    for row in matr:
        print(" ".join(map(str, row)))

def is_valid_command(data, rows, cols):
    if not data[0] == "swap" or not len(data) == 5:
        return False
    try:
        row_1, col_1, row_2, col_2 = map(int, data[1:])
    except ValueError:
        return False

    if row_1 < 0 or row_1 >= rows or col_1 < 0 or col_1 >= cols or \
        row_2 < 0 or row_2 >= rows or col_2 < 0 or col_2 >= cols:
        return False
    return True

rows, cols = map(int, input().split())

matrix = [input().split() for _ in range(rows)]

command = input().split()

while not command[0] == "END":

    if is_valid_command(command, rows, cols):
        row_1, col_1, row_2, col_2 = map(int, command[1:])
        matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
        print_matrix(matrix)
    else:
        print("Invalid input!")

    command = input().split()
