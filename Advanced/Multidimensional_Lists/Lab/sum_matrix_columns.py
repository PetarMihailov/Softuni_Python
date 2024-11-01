rows, cols = [int(el) for el in input().split(', ')]

matrix = []

for _ in range(rows):
    nums = [int(el) for el in input().split()]
    matrix.append(nums)

for col in range( cols):
    result = 0
    for row in range(rows):
        result += matrix[row][col]
    print(result)
