from math import ceil, floor

days = int(input())
food = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input()) / 1000

total_food = (dog_food + cat_food + turtle_food) * days
diff = abs(total_food - food)

if total_food > food:
    print(f"{ceil(diff)} more kilos of food are needed.")
else:
    print(f"{floor(diff)} kilos of food left.")
