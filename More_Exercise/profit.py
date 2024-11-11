coins_1lv = int(input())
coins_2lv = int(input())
bills_5lv = int(input())
target_sum = int(input())

for x in range(coins_1lv + 1):
    for y in range(coins_2lv + 1):
        for z in range(bills_5lv + 1):
            current_sum = x * 1 + y * 2 + z * 5
            if current_sum == target_sum:
                print(f"{x} * 1 lv. + {y} * 2 lv. + {z} * 5 lv. = {target_sum} lv.")
