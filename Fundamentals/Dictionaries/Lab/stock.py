products = input().split()
search_products = input().split()

bakery = {}

for index in range(0, len(products), 2):
    product = products[index]
    quantity = int(products[index+1])
    bakery[product] = quantity

for product in search_products:
    if product in bakery:
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")


