price_per_kg_flour = float(input())
kg_flour = float(input())
kg_sugar = float(input())
num_egg_packs = int(input())
num_yeast_packs = int(input())

price_per_kg_sugar = price_per_kg_flour * 0.75  
price_per_egg_pack = price_per_kg_flour * 1.10  
price_per_yeast_pack = price_per_kg_sugar * 0.20  

total_flour_cost = kg_flour * price_per_kg_flour
total_sugar_cost = kg_sugar * price_per_kg_sugar
total_egg_cost = num_egg_packs * price_per_egg_pack
total_yeast_cost = num_yeast_packs * price_per_yeast_pack

total_cost = total_flour_cost + total_sugar_cost + total_egg_cost + total_yeast_cost

print(f"{total_cost:.2f}")
