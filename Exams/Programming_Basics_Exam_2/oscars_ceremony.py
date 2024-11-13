rent = int(input())

statues_cost = rent * 0.70
catering_cost = statues_cost * 0.85
sound_cost = catering_cost / 2

total_cost = rent + statues_cost + catering_cost + sound_cost

print(f"{total_cost:.2f}")
