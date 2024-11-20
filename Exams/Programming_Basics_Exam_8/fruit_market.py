price_strawberries = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
raspberries_kg = float(input())
strawberries_kg = float(input())

price_raspberries = price_strawberries / 2
price_oranges = price_raspberries * 0.6
price_bananas = price_raspberries * 0.2


total_cost = (
    strawberries_kg * price_strawberries +
    bananas_kg * price_bananas +
    oranges_kg * price_oranges +
    raspberries_kg * price_raspberries
)

print(f"{total_cost:.2f}")
