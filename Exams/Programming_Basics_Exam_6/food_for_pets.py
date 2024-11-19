days = int(input())  
total_food = float(input())  

dog_food_total = 0  
cat_food_total = 0  
biscuits_total = 0  

for day in range(1, days + 1):
    dog_food = int(input())  
    cat_food = int(input())  

    dog_food_total += dog_food
    cat_food_total += cat_food

    if day % 3 == 0:
        total_eaten = dog_food + cat_food
        biscuits = total_eaten * 0.10
        biscuits_total += biscuits

total_eaten_food = dog_food_total + cat_food_total
percentage_eaten = (total_eaten_food / total_food) * 100
dog_percentage = (dog_food_total / total_eaten_food) * 100
cat_percentage = (cat_food_total / total_eaten_food) * 100

print(f"Total eaten biscuits: {round(biscuits_total)}gr.")
print(f"{percentage_eaten:.2f}% of the food has been eaten.")
print(f"{dog_percentage:.2f}% eaten from the dog.")
print(f"{cat_percentage:.2f}% eaten from the cat.")
