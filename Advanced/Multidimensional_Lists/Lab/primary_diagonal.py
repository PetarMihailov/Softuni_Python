n = int(input())

matrix = []

for _ in range(n):
    nums = [int(el) for el in input().split()]
    matrix.append(nums)

diagonal = 0

for i in range(n):
    diagonal += matrix[i][i]

print(diagonal)

# second solution

rows = int(input())

matrix = []

for _ in range(rows):
    matrix.append([int(el) for el in input().split()])

result = 0

for row in range(rows):
    for col in range(rows):
        if row == col:
            result += matrix[row][col]

print(result)
