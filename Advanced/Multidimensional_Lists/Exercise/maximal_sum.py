rows, cols = list(map(int, input().split()))

matrix = [[int(el) for el in input().split()] for _ in range(rows)]

max_sum = 0
position = None

for row in range(rows-2):
    for col in range(cols-2):
        sum_current_position = sum([matrix[row][col], matrix[row+1][col], matrix[row+2][col],
                      matrix[row][col+1], matrix[row][col+2], matrix[row+1][col+1], matrix[row+2][col+1],
                      matrix[row+1][col+2], matrix[row+2][col+2]])

        if sum_current_position >= max_sum:
            max_sum = sum_current_position
            position = (row, col)

row, col = position

print(f"Sum = {max_sum}")
print(matrix[row][col], matrix[row][col+1], matrix[row][col+2])
print(matrix[row+1][col], matrix[row+1][col+1], matrix[row+1][col+2])
print(matrix[row+2][col], matrix[row+2][col+1], matrix[row+2][col+2])

