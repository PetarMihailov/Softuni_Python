kilometers = int(input())
time = input()

price = 0

if kilometers < 20:
    if time == "day":
        price = kilometers * 0.79
    elif time == "night":
        price = kilometers * 0.90
    price += 0.7
elif 20 <= kilometers < 100:
    price = kilometers * 0.09

elif kilometers >= 100:
    price = kilometers * 0.06

print(f"{price:.2f}")
