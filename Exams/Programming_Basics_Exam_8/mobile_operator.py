contract_length = input()  
contract_type = input()  
mobile_internet = input()  
months = int(input())  

prices = {
    "one": {
        "Small": 9.98,
        "Middle": 18.99,
        "Large": 25.98,
        "ExtraLarge": 35.99
    },
    "two": {
        "Small": 8.58,
        "Middle": 17.09,
        "Large": 23.59,
        "ExtraLarge": 31.79
    }
}

base_price = prices[contract_length][contract_type]

if mobile_internet == "yes":
    if base_price <= 10.00:
        internet_price = 5.50
    elif base_price <= 30.00:
        internet_price = 4.35
    else:
        internet_price = 3.85
    base_price += internet_price

if contract_length == "two":
    base_price *= 0.9625 

total_price = base_price * months

print(f"{total_price:.2f} lv.")
