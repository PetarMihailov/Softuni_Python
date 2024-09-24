def sum_numbers(num_1, num_2):
    return num_1 + num_2


def subtract(num_1, num_2, num_3):
    return sum_numbers(num_1, num_2) - num_3


line_1 = int(input())
line_2 = int(input())
line_3 = int(input())

print(subtract(line_1, line_2, line_3))
