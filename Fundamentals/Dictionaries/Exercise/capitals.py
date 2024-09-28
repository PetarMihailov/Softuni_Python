countries = input().split(", ")
capitals = input().split(", ")

country_capital = dict(zip(countries, capitals))

for key, value in country_capital.items():
    print(f"{key} -> {value}")
