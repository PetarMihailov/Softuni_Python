nums = [2, 3, 5, 7]

first = int(input())
second = int(input())
third = int(input())

for i in range(1, first+1):
    for j in range(1, second+1):
        for k in range(1, third+1):
            if i % 2 == 0 and j in nums and k % 2 == 0:
                print(f"{i} {j} {k}")
