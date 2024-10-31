rows = int(input())

matrix = []

for _ in range(rows):
    nums =  [int(el) for el in input().split(", ")]
    matrix.extend(nums)

print(matrix)

# 

