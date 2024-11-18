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
