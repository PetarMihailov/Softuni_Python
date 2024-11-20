price_over_20kg = float(input())  
weight = float(input())  
days_to_trip = int(input())  
num_bags = int(input())  

if weight < 10:
    base_price = price_over_20kg * 0.20
elif 10 <= weight <= 20:
    base_price = price_over_20kg * 0.50
else:
    base_price = price_over_20kg

if days_to_trip > 30:
    final_price_per_bag = base_price * 1.10
elif 7 <= days_to_trip <= 30:
    final_price_per_bag = base_price * 1.15
else:  # days_to_trip < 7
    final_price_per_bag = base_price * 1.40

total_price = final_price_per_bag * num_bags

print(f"The total price of bags is: {total_price:.2f} lv.")
