from math import ceil, floor

tennis_racket = float(input())
count_rackets = int(input())
count_shoes = int(input())

price_rackets = tennis_racket * count_rackets
price_shoes = count_shoes * (tennis_racket / 6)
price = price_rackets + price_shoes
rest_equipment = price * 0.2
total_price = price + rest_equipment
price_djokovich = total_price / 8
price_sponsors  =total_price * 7/8

print(f"Price to be paid by Djokovic {floor(price_djokovich)}")
print(f"Price to be paid by sponsors {ceil(price_sponsors)}")
