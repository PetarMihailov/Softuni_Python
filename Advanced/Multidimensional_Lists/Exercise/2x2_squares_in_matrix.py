"""
3 4
A B B D
E B B B
I J B B

2

5 4
A A B D
A A B B
I J B B
C C C G
C C K P

3
"""

rows , cols = [int(el) for el in input().split()]

def init_matrix():
    matrix = []
    for _ in range(rows):
        matrix.append(input().split())
    return matrix


def check_el_are_equal(row, col, matr):
    if matr[row][col] == matr[row][col+1] and matr[row][col+1] == matr[row+1][col+1] \
            and matr[row+1][col+1] == matr[row+1][col]:
        return True
    return False


matrix = init_matrix()
counter = 0

for row_index in range(rows-1):
    for col_index in range(cols-1):
        if check_el_are_equal(row_index, col_index, matrix):
            counter += 1

print(counter)
