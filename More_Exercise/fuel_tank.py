fuel = input().lower()
liters = int(input())

if fuel not in ["diesel", "gas", "gasoline"]:
    print("Invalid fuel!")
elif liters < 25:
    print(f"Fill your tank with {fuel}!")
elif liters >= 25:
    print(f"You have enough {fuel}.")
