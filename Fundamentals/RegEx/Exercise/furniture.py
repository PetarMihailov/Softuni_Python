import re

data = input()

pattern = r"(?<!.)>>(?P<product>[a-zA-Z]+)<<(?P<price>\d+(\.\d+)?)\!(?P<qty>\d+)(?!.)"
total_money = 0
furniture = []

while not data == "Purchase":
    valid = re.match(pattern, data)
    if valid:
        match = valid.groupdict()
        name = match["product"]
        furniture.append(name)
        total_money += float(match["price"]) * int(match["qty"])

    data = input()

print("Bought furniture:")
if furniture:
    print("\n".join(furniture))

print(f"Total money spend: {total_money:.2f}")

