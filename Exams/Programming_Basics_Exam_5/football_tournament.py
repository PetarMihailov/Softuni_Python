team_name = input()
matches_played = int(input())

if matches_played == 0:
    print(f"{team_name} hasn't played any games during this season.")
else:
    points = 0
    wins = 0
    draws = 0
    losses = 0

    for _ in range(matches_played):
        result = input().strip()

        if result == 'W':  
            points += 3
            wins += 1
        elif result == 'D':  
            points += 1
            draws += 1
        elif result == 'L':  
            losses += 1

    win_rate = (wins / matches_played) * 100

    print(f"{team_name} has won {points} points during this season.")
    print("Total stats:")
    print(f"## W: {wins}")
    print(f"## D: {draws}")
    print(f"## L: {losses}")
    print(f"Win rate: {win_rate:.2f}%")
