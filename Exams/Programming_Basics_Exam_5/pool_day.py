import math

people = int(input())
entry_fee = float(input())
sunbed_price = float(input())
umbrella_price = float(input())

total_entry_fee = people * entry_fee
num_umbrellas = math.ceil(people / 2)
num_sunbeds = math.ceil(people * 0.75)

total_umbrella_cost = num_umbrellas * umbrella_price
total_sunbed_cost = num_sunbeds * sunbed_price

total_cost = total_entry_fee + total_umbrella_cost + total_sunbed_cost

print(f"{total_cost:.2f} lv.")
