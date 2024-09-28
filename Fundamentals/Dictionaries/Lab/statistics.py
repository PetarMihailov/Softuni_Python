command = input()

products = {}

while not command == "statistics":
    product, qty = command.split(": ")
    qty = int(qty)

    if product not in products:
        products[product] = qty
    else:
        products[product] += qty

    command = input()

print("Products in stock:")
for key, val in products.items():
    print(f"- {key}: {val}")

print(f"Total Products: {len(products)}\nTotal Quantity: {sum([qty for qty in products.values()])}")
