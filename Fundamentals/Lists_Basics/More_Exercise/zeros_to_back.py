numbers = list(map(int, input().split(", ")))

nums = [el for el in numbers if not el == 0]
zeros = [el for el in numbers if el == 0]

print(nums + zeros)
