"""
Primary diagonal: 1, 5, 9. Sum: 15
Secondary diagonal: 3, 5, 7. Sum: 15

3
1, 2, 3
4, 5, 6
7, 8, 9
"""

size = int(input())

matrix = [[int(el) for el in input().split(", ")] for _ in range(size)]

primary_diagonal = []
secondary_diagonal = []

for idx in range(size):
    primary_diagonal.append(matrix[idx][idx])
    secondary_diagonal.append(matrix[idx][size - idx - 1])

print(f"Primary diagonal: {', '.join([str(el) for el in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(el) for el in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")

# second solution

matrix = [[int(el) for el in input().split(", ")] for i in range(int(input()))]

primary = []
secondary = []
col = len(matrix) - 1

for index in range(len(matrix)):
    primary.append(matrix[index][index])
    secondary.append(matrix[index][col])

    col -= 1

print(f"Primary diagonal: {', '.join([str(el) for el in primary])}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join([str(el) for el in secondary])}. Sum: {sum(secondary)}")
