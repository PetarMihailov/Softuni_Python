winner_name = ""
winner_points = -1  
winner_order = -1  

order = 0  

while True:
    name = input().strip()

    if name == "Stop":
        break

    points = 0
    
    for i in range(len(name)):
        ascii_value = ord(name[i])  
        entered_number = int(input())

        if entered_number == ascii_value:
            points += 10
        else:
            points += 2

    if points > winner_points:
        winner_name = name
        winner_points = points
        winner_order = order
    elif points == winner_points and order > winner_order:
        winner_name = name
        winner_points = points
        winner_order = order

    order += 1

print(f"The winner is {winner_name} with {winner_points} points!")
