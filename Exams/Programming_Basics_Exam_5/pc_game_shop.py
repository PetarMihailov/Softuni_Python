n = int(input())

hearthstone_count = 0
fornite_count = 0
overwatch_count = 0
others_count = 0

for _ in range(n):
    game_name = input()
    if game_name == "Hearthstone":
        hearthstone_count += 1
    elif game_name == "Fornite":
        fornite_count += 1
    elif game_name == "Overwatch":
        overwatch_count += 1
    else:
        others_count += 1

hearthstone_percent = (hearthstone_count / n) * 100
fornite_percent = (fornite_count / n) * 100
overwatch_percent = (overwatch_count / n) * 100
others_percent = (others_count / n) * 100

print(f"Hearthstone - {hearthstone_percent:.2f}%")
print(f"Fornite - {fornite_percent:.2f}%")
print(f"Overwatch - {overwatch_percent:.2f}%")
print(f"Others - {others_percent:.2f}%")
