n = int(input())

matrix = []

for _ in range(n):
    matrix.append(list(input()))

searched_char = input()

position = None

for row in range(n):
    for col in range(n):
        if matrix[row][col] == searched_char:
            position = (row, col)
            break
    if position:
        break
        
if position:
    print(position)
else:
    print(f"{searched_char} does not occur in the matrix")
