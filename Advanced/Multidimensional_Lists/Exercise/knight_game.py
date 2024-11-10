n = int(input())

matrix = [list(input()) for _ in range(n)]



def is_valid_bound(row, col):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False

def calculate_kills(matr, row, col):
    kills = 0
    rows  = [-2, -2, 2, 2, 1, 1, -1, -1]
    cols = [-1, 1, -1, 1, -2, 2, -2, 2] # moving letter "g" for knight over matrix "move[rows][cols]"
    for index in range(len(rows)):
        potential_row = row+rows[index]
        potential_col  = col+cols[index]
        if is_valid_bound(potential_row, potential_col):
            potential_position = matr[potential_row][potential_col]
            if potential_position == "K":
                kills += 1
    return kills

knight = 0

while True:
    max_kills = 0
    knight_position = []

    for row_index in range(n):
        for col_index in range(n):
            if matrix[row_index][col_index] == "K":
             kills = calculate_kills(matrix, row_index, col_index)
             if max_kills < kills:
                 max_kills = kills
                 knight_position = [row_index, col_index]
    if knight_position:
        matrix[knight_position[0]][knight_position[1]] = "0"
        knight += 1
    else:
        break

print(knight)
