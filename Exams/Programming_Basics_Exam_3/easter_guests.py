import math

num_guests = int(input())
budget = float(input())

bread_price = 4.0  
egg_price = 0.45   

num_breads = math.ceil(num_guests / 3)  
num_eggs = num_guests * 2               

total_bread_cost = num_breads * bread_price
total_egg_cost = num_eggs * egg_price
total_cost = total_bread_cost + total_egg_cost

if budget >= total_cost:
    remaining_money = budget - total_cost
    print(f"Lyubo bought {num_breads} Easter bread and {num_eggs} eggs.")
    print(f"He has {remaining_money:.2f} lv. left.")
else:
    needed_money = total_cost - budget
    print("Lyubo doesn't have enough money.")
    print(f"He needs {needed_money:.2f} lv. more.")
