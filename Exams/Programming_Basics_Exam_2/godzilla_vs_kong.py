budget = float(input())
num_extras = int(input())
cost_per_clothing = float(input())

decor_cost = budget * 0.10
total_clothing_cost = num_extras * cost_per_clothing

if num_extras > 150:
    total_clothing_cost *= 0.90

total_cost = decor_cost + total_clothing_cost

if total_cost > budget:
    deficit = total_cost - budget
    print("Not enough money!")
    print(f"Wingard needs {deficit:.2f} leva more.")
else:
    surplus = budget - total_cost
    print("Action!")
    print(f"Wingard starts filming with {surplus:.2f} leva left.")
