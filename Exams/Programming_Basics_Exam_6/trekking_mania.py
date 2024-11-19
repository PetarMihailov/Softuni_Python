groups_count = int(input())  
group_sizes = []  


for _ in range(groups_count):
    group_size = int(input())
    group_sizes.append(group_size)

mussala_count = 0
montblan_count = 0
kilimanjaro_count = 0
k2_count = 0
everest_count = 0

for size in group_sizes:
    if size <= 5:
        mussala_count += size
    elif size <= 12:
        montblan_count += size
    elif size <= 25:
        kilimanjaro_count += size
    elif size <= 40:
        k2_count += size
    else:
        everest_count += size

total_climbers = sum(group_sizes)

mussala_percentage = (mussala_count / total_climbers) * 100
montblan_percentage = (montblan_count / total_climbers) * 100
kilimanjaro_percentage = (kilimanjaro_count / total_climbers) * 100
k2_percentage = (k2_count / total_climbers) * 100
everest_percentage = (everest_count / total_climbers) * 100

print(f"{mussala_percentage:.2f}%")
print(f"{montblan_percentage:.2f}%")
print(f"{kilimanjaro_percentage:.2f}%")
print(f"{k2_percentage:.2f}%")
print(f"{everest_percentage:.2f}%")
