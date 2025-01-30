products = input().split()

bakery = {}

for index in range(0, len(products), 2):
    key = products[index]
    value = int(products[index+1])
    bakery[key] = value

print(bakery)

#  second solution

data = input().split()

products = {data[index]: int(data[index+1]) for index in range(0, len(data), 2)}

print(products)
