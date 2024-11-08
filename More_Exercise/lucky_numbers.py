n = int(input())

nums = []

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for m in range(1, 10):
                if i+j == k+m and n % (i+j) == 0:
                    nums.append(f"{i}{j}{k}{m}")

print(*nums)
