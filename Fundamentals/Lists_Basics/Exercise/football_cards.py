team_a = [int(el) for el in range(1, 12)]
team_b = [int(el) for el in range(1, 12)]

cards = input().split()
flag =  False

for card in cards:
    team, player = card.split("-")
    player = int(player)
    if team == "A" and player in team_a:
        team_a.remove(player)
    elif team == "B" and player in team_b:
        team_b.remove(player)

    if len(team_a) < 7 or len(team_b) < 7:
        flag = True
        break

if not flag:
    print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
else:
    print(f"Team A - {len(team_a)}; Team B - {len(team_b)}\nGame was terminated")
