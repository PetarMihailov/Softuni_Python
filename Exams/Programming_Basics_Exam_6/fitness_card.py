money_available = float(input())  
gender = input()  
age = int(input()) 
sport = input()  

prices = {
    'm': {'Gym': 42, 'Boxing': 41, 'Yoga': 45, 'Zumba': 34, 'Dances': 51, 'Pilates': 39},
    'f': {'Gym': 35, 'Boxing': 37, 'Yoga': 42, 'Zumba': 31, 'Dances': 53, 'Pilates': 37}
}

card_price = prices[gender][sport]

if age <= 19:
    card_price *= 0.80

if money_available >= card_price:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    money_needed = card_price - money_available
    print(f"You don't have enough money! You need ${money_needed:.2f} more.")
