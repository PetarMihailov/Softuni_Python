food_kg = int(input())  
food_grams = food_kg * 1000  

while True:
    food_per_meal = input()  
    if food_per_meal == "Adopted":
        break  
    food_per_meal = int(food_per_meal)  
    food_grams -= food_per_meal  

if food_grams >= 0:
    print(f"Food is enough! Leftovers: {food_grams} grams.")
else:
    print(f"Food is not enough. You need {abs(food_grams)} grams more.")
