player_name = input()

points = 301

successful_shots = 0
unsuccessful_shots = 0

while True:
    field = input()
    if field == "Retire":
        print(f"{player_name} retired after {unsuccessful_shots} unsuccessful shots.")
        break

    points_value = int(input())  

    if field == "Single":
        points_after_shot = points_value
    elif field == "Double":
        points_after_shot = points_value * 2
    elif field == "Triple":
        points_after_shot = points_value * 3

    if points_after_shot <= points:
        points -= points_after_shot
        successful_shots += 1
    else:
        unsuccessful_shots += 1

    if points == 0:
        print(f"{player_name} won the leg with {successful_shots} shots.")
        break
