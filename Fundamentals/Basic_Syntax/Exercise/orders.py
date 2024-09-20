orders = int(input())

total_price = 0

for _ in range(orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_count = int(input())
    if 0 < price_per_capsule <= 100 and 1 <= days <= 31 and 1 <= capsules_count <= 2000:
        total_per_order = days * capsules_count * price_per_capsule
        total_price += total_per_order
        print(f"The price for the coffee is: ${total_per_order:.2f}")


print(f"Total: ${total_price:.2f}")
