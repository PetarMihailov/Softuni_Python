fuel = input()
liters = float(input())
card = input()

fuels = {"Gas": 0.93, "Gasoline": 2.22, "Diesel": 2.33}
discounts = {"Gas": 0.08, "Gasoline": 0.18, "Diesel": 0.12}

if card == "Yes":
    fuels[fuel] -= discounts[fuel]

price = liters * fuels[fuel]

if 20 < liters <= 25:
    price *= 0.92
elif liters > 25:
    price *= 0.90

print(f"{price:.2f} lv.")
