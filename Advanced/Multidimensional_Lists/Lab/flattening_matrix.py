rows = int(input())

matrix = []

for _ in range(rows):
    nums =  [int(el) for el in input().split(", ")]
    matrix.extend(nums)

print(matrix)

# 

rows = int(input())

matrix = []

for _ in range(rows):
    nums =  [int(el) for el in input().split(", ")]
    matrix.append(nums)

result = []

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        result.append(matrix[row][col])

print(result)
