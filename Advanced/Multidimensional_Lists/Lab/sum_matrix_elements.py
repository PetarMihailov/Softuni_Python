rows, cols = [int(el) for el in input().split(", ")]

matrix = [[int(el) for el in input().split(", ")] for i in range(rows)]

result = 0

for row in range(rows):
    for col in range(cols):
        result += matrix[row][col]

print(result)
print(matrix)

# second solution

rows, cols = [int(el) for el in input().split(", ")]

matrix = []

for _ in range(rows):
    matrix.append(list(map(int, input().split(", "))))

print(sum([sum(el) for el in matrix]))
print(matrix)
