def orders(product, qty):
    price = None
    if product == 'coffee':
        price = qty * 1.50
    elif product == 'coke':
        price = qty * 1.40
    elif product == 'water':
        price = qty * 1.00
    elif product == 'snacks':
        price = qty * 2.00
    return f"{price:.2f}"

prod = input()
quant = float(input())

print(orders(prod, quant))

# second solution

def calculate_order(items, item, quantity):
    if item in items:
        return items.get(item) * quantity


product = input()
qty = int(input())

items_qty = {
    "coffee": 1.50,
    "coke": 1.40,
    "water": 1.00,
    "snacks": 2.00
}


print(f"{calculate_order(items_qty, product, qty):.2f}")
