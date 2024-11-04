from math import ceil, floor

harvest = int(input())
grape = float(input())
vine = int(input())
workers = int(input())

total_grape = harvest * grape
total_vine = 0.4 * total_grape / 2.5
diff =abs(vine - total_vine)

if total_vine >= vine:
    print(f"Good harvest this year! Total wine: {ceil(total_vine)} liters.")
    print(f"{ceil(diff)} liters left -> {ceil(diff / workers)} liters per person.")
else:
    print(f"It will be a tough winter! More {floor(diff)} liters wine needed.")
