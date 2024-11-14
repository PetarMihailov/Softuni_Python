size = input()
color = input()
batch_count = int(input())

price_per_batch = 0

if size == "Large":
    if color == "Red":
        price_per_batch = 16
    elif color == "Green":
        price_per_batch = 12
    elif color == "Yellow":
        price_per_batch = 9
elif size == "Medium":
    if color == "Red":
        price_per_batch = 13
    elif color == "Green":
        price_per_batch = 9
    elif color == "Yellow":
        price_per_batch = 7
elif size == "Small":
    if color == "Red":
        price_per_batch = 9
    elif color == "Green":
        price_per_batch = 8
    elif color == "Yellow":
        price_per_batch = 5

total_revenue = price_per_batch * batch_count
final_revenue = total_revenue * 0.65 

print(f"{final_revenue:.2f} leva.")
