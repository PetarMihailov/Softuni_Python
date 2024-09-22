n = int(input())

snowball_value = {"weight": 0, "time": 0, "qty": 0}
highest_value = 0

for _ in range(n):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_qty = int(input())

    snowball = (snowball_weight / snowball_time) ** snowball_qty

    if snowball > highest_value:
        highest_value = snowball
        snowball_value = {"weight": snowball_weight, "time": snowball_time, "qty": snowball_qty}

print(f"{snowball_value['weight']} : {snowball_value['time']} = {int(highest_value)} ({snowball_value['qty']})")
