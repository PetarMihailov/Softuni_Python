fee = float(input())

sneakers = fee * 0.60
tracksuit = sneakers * 0.80
ball = tracksuit / 4
accessories = ball / 5

total_price = sneakers + tracksuit + ball + accessories + fee

print(f"{total_price:.2f}")
