movie = input()  
package = input()  
tickets = int(input())  

prices = {
    "John Wick": {"Drink": 12, "Popcorn": 15, "Menu": 19},
    "Star Wars": {"Drink": 18, "Popcorn": 25, "Menu": 30},
    "Jumanji": {"Drink": 9, "Popcorn": 11, "Menu": 14},
}

price_per_ticket = prices[movie][package]
total_price = price_per_ticket * tickets

if movie == "Star Wars" and tickets >= 4:
    total_price *= 0.7  # 30% отстъпка
elif movie == "Jumanji" and tickets == 2:
    total_price *= 0.85  # 15% отстъпка

print(f"Your bill is {total_price:.2f} leva.")
