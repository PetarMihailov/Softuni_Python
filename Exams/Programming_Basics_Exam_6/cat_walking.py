minutes_per_walk = int(input())
walks_per_day = int(input())
calories_per_day = int(input())

calories_burned_per_minute = 5
total_burned_calories = minutes_per_walk * walks_per_day * calories_burned_per_minute

required_calories_burned = calories_per_day * 0.5

if total_burned_calories >= required_calories_burned:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_burned_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_burned_calories}.")
