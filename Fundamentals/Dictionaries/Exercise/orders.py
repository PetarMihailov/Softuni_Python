data = input()

products = {}

while not data == "buy":
    product, price, quantity = data.split(" ")
    price = float(price)
    quantity = int(quantity)

    if product not in products:
        products[product] = {"price": 0.0, "quantity": 0}
    products[product]["price"] = price
    products[product]["quantity"] += quantity

    data = input()

for key, val in products.items():
    print(f"{key} -> {val['price'] * val['quantity']:.2f}")
