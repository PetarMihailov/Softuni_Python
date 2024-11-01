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

# second solution

n = int(input())

matrix = []
position = None

for _ in range(n):
    matrix.append([el for el in list(input())])

symbol = input()

for row in range(n):
    for col in range(n):
        if matrix[row][col] == symbol:
            position = (row, col)
            break
    if position:
        break

print(position if position else f"{symbol} does not occur in the matrix")
