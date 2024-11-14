num_cakes = int(input())  
num_egg_packs = int(input())  
kg_cookies = int(input())  

price_per_cake = 3.20
price_per_egg_pack = 4.35
price_per_kg_cookies = 5.40
price_per_egg_dye = 0.15

total_cake_cost = num_cakes * price_per_cake
total_egg_cost = num_egg_packs * price_per_egg_pack
total_cookies_cost = kg_cookies * price_per_kg_cookies
total_egg_dye_cost = num_egg_packs * 12 * price_per_egg_dye  

total_cost = total_cake_cost + total_egg_cost + total_cookies_cost + total_egg_dye_cost

print(f"{total_cost:.2f}")
