days = int(input())

total_money = 0
total_wins = 0  

for _ in range(days):
    day_money = 0  
    wins = 0
    losses = 0

    while True:
        game = input()
        if game == "Finish":
            break

        result = input()

        if result == "win":
            wins += 1
            day_money += 20  
        elif result == "lose":
            losses += 1

    if wins > losses:
        day_money *= 1.1
        total_wins += 1

    total_money += day_money

if total_wins > days / 2:
    total_money *= 1.2

if total_wins > days / 2:
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")
