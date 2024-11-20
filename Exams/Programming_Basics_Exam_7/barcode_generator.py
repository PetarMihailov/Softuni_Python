start_range = input()
end_range = input()

for d1 in range(int(start_range[0]), int(end_range[0]) + 1):
    for d2 in range(int(start_range[1]), int(end_range[1]) + 1):
        for d3 in range(int(start_range[2]), int(end_range[2]) + 1):
            for d4 in range(int(start_range[3]), int(end_range[3]) + 1):
                if d1 % 2 == 1 and d2 % 2 == 1 and d3 % 2 == 1 and d4 % 2 == 1:
                    print(f"{d1}{d2}{d3}{d4}", end=" ")
