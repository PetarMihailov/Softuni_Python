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

# second solution

data = input()

products = {}

while not data == 'statistics':
    key, val = data.split(": ")
    val = int(val)

    if not key in products:
        products[key] = 0
    products[key] += val

    data = input()

print("Products in stock:")

for key, val in products.items():
    print(f"- {key}: {val}")

print(f"Total Products: {len(products)}\nTotal Quantity: {sum(products.values())}")
