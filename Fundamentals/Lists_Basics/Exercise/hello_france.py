TICKET = 150
CLOTHES = 50
SHOES = 35.00
ACCESSORIES = 20.50

buy_items = []

items = input().split("|")
budget = float(input())

for item in items:
    item_name, price = item.split("->")
    price = float(price)

    if budget >= price:
        if item_name == "Clothes" and price > CLOTHES:
            continue
        elif item_name == "Shoes" and price > SHOES:
            continue
        elif item_name == "Accessories" and price > ACCESSORIES:
            continue

        buy_items.append(price)
        budget -= price

sell_items = [item * 1.4 for item in buy_items]
profit = sum(sell_items) - sum(buy_items)

print(" ".join([f"{item:.2f}" for item in sell_items]))
print(f"Profit: {profit:.2f}")

if budget + sum(sell_items) >= TICKET:
    print("Hello, France!")
else:
    print("Not enough money.")