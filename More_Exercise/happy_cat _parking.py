days = int(input())
hours = int(input())


total_sum = 0

for day in range(1, days + 1):
    daily_sum = 0

    for hour in range(1, hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            price = 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            price = 1.25
        else:
            price = 1.00

        daily_sum += price

    print(f"Day: {day} - {daily_sum:.2f} leva")

    total_sum += daily_sum

print(f"Total: {total_sum:.2f} leva")