"""
3
11 2 4
4 5 6
10 8 -12
"""

size = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(size)]

primary_diagonal = []
secondary_diagonal = []

for index in range(size):
    primary_diagonal.append(matrix[index][index])
    secondary_diagonal.append(matrix[index][size - index - 1])

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
