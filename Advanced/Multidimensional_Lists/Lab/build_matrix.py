matrix = [['1', '2', '3',], ['4', '5', '6',], ['7', '8', '9',]]

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        print(matrix[row][col], end=" ")
    print()

#

matrix = [['1', '2', '3',], ['4', '5', '6',], ['7', '8', '9',]]

for row in range(len(matrix)):
    print(*matrix[row])

#

row = int(input())

matrix = []

for _ in range(row):
    data = input().split()
    matrix.append(data)

print(matrix)

# 

