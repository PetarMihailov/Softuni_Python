desired_profit = float(input())  
total_income = 0  

while True:
    cocktail_name = input()  
    if cocktail_name == "Party!":
        break

    num_cocktails = int(input()) 
    cocktail_price = len(cocktail_name)  
    order_price = cocktail_price * num_cocktails  

    if order_price % 2 != 0:
        order_price *= 0.75  

    total_income += order_price

    if total_income >= desired_profit:
        print("Target acquired.")
        print(f"Club income - {total_income:.2f} leva.")
        break

if total_income < desired_profit:
    missing_amount = desired_profit - total_income
    print(f"We need {missing_amount:.2f} leva more.")
    print(f"Club income - {total_income:.2f} leva.")
