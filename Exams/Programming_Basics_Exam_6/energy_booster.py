fruit = input()
size = input()
sets_count = int(input())

prices = {
    "Watermelon": {"small": 56, "big": 28.70},
    "Mango": {"small": 36.66, "big": 19.60},
    "Pineapple": {"small": 42.10, "big": 24.80},
    "Raspberry": {"small": 20, "big": 15.20}
}

gels_per_set = {"small": 2, "big": 5}

price_per_gel = prices[fruit][size]
total_gels = gels_per_set[size] * sets_count
total_price = total_gels * price_per_gel

if 400 <= total_price <= 1000:
    total_price *= 0.85
elif total_price > 1000:
    total_price *= 0.50

print(f"{total_price:.2f} lv.")
