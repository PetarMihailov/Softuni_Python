budget = float(input())  
nights = int(input())  
price_per_night = float(input())  
extra_expenses_percentage = int(input())  

if nights > 7:
    price_per_night *= 0.95

nights_expenses = nights * price_per_night
extra_expenses = budget * (extra_expenses_percentage / 100)
total_expenses = nights_expenses + extra_expenses

if total_expenses <= budget:
    remaining_money = budget - total_expenses
    print(f"Ivanovi will be left with {remaining_money:.2f} leva after vacation.")
else:
    needed_money = total_expenses - budget
    print(f"{needed_money:.2f} leva needed.")
