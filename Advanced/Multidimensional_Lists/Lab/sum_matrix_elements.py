rows, cols = [int(el) for el in input().split(", ")]

matrix = [[int(el) for el in input().split(", ")] for i in range(rows)]

result = 0

for row in range(rows):
    for col in range(cols):
        result += matrix[row][col]

print(result)
print(matrix)
