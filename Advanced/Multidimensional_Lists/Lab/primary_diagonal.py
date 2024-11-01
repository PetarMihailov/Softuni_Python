n = int(input())

matrix = []

for _ in range(n):
    nums = [int(el) for el in input().split()]
    matrix.append(nums)

diagonal = 0

for i in range(n):
    diagonal += matrix[i][i]

print(diagonal)
