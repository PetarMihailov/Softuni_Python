num_cakes = int(input())

max_points = 0
winner_name = ""

for _ in range(num_cakes):
    baker_name = input()
    total_points = 0

    while True:
        score = input()
        if score == "Stop":
            break
        total_points += int(score)

    print(f"{baker_name} has {total_points} points.")

    if total_points > max_points:
        max_points = total_points
        winner_name = baker_name
        print(f"{baker_name} is the new number 1!")

print(f"{winner_name} won competition with {max_points} points!")
