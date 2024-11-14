num_guests = int(input())
price_per_guest = float(input())
budget = float(input())

if 10 <= num_guests <= 15:
    discount = 0.15  
elif 15 < num_guests <= 20:
    discount = 0.20 
elif num_guests > 20:
    discount = 0.25  
else:
    discount = 0.0  

discounted_price_per_guest = price_per_guest * (1 - discount)
total_guest_cost = num_guests * discounted_price_per_guest
cake_cost = budget * 0.10
total_cost = total_guest_cost + cake_cost

if budget >= total_cost:
    remaining_money = budget - total_cost
    print(f"It is party time! {remaining_money:.2f} leva left.")
else:
    needed_money = total_cost - budget
    print(f"No party! {needed_money:.2f} leva needed.")
