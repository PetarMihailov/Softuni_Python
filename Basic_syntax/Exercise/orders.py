orders = int(input())

total_price = 0

for _ in range(orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_count = int(input())
    total_per_order = days * capsules_count * price_per_capsule
    total_price += total_per_order
    print(f"The price for the coffee is: ${total_per_order:.2f}")

print(f"Total: ${total_price:.2f}")
