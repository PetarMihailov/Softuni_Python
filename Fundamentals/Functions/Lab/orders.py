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
