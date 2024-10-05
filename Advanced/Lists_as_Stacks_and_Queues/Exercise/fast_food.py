from collections import deque

qty = int(input())

orders = deque(int(el) for el in input().split())

print(max(orders))

while orders:
    if orders[0] <= qty:
        qty -= orders[0]
        orders.popleft()
    else:
        break

if not orders:
    print("Orders complete")
else:
    print(f"Orders left:", *orders)
