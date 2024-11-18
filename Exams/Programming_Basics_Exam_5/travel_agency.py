city = input()  
package = input()  
vip_discount = input()  
days = int(input())  

if city not in ["Bansko", "Borovets", "Varna", "Burgas"] or package not in ["noEquipment", "withEquipment", "noBreakfast", "withBreakfast"]:
    print("Invalid input!")
elif days < 1:
    print("Days must be positive number!")
else:
    price_per_day = 0
    if city in ["Bansko", "Borovets"]:
        if package == "withEquipment":
            price_per_day = 100
            if vip_discount == "yes":
                price_per_day *= 0.90  
        elif package == "noEquipment":
            price_per_day = 80
            if vip_discount == "yes":
                price_per_day *= 0.95 
    elif city in ["Varna", "Burgas"]:
        if package == "withBreakfast":
            price_per_day = 130
            if vip_discount == "yes":
                price_per_day *= 0.88  
        elif package == "noBreakfast":
            price_per_day = 100
            if vip_discount == "yes":
                price_per_day *= 0.93  

    total_price = price_per_day * days
    if days > 7:
        total_price -= price_per_day  

    print(f"The price is {total_price:.2f}lv! Have a nice time!")
