match1 = input()
match2 = input()
match3 = input()

wins = 0
losses = 0
draws = 0

matches = [match1, match2, match3]

for match in matches:
    home_goals, away_goals = map(int, match.split(":"))

    if home_goals > away_goals:
        wins += 1
    elif home_goals < away_goals:
        losses += 1
    else:
        draws += 1

print(f"Team won {wins} games.")
print(f"Team lost {losses} games.")
print(f"Drawn games: {draws}")
