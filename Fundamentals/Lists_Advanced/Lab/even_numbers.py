numbers = input().split(", ")

even_indices = [index for index in range(len(numbers)) if int(numbers[index]) % 2 == 0]

print(even_indices)
