energy = 100
coins = 100
is_closed = False

events = input().split("|")

for el in events:
    event, number = el.split("-")
    number = int(number)
    if event == "rest":
        if energy + number >= 100:
            gained_energy = 100 - energy
            energy = 100
            print(f"You gained {gained_energy} energy.\nCurrent energy: {energy}.")
        else:
            energy += number
            print(f"You gained {number} energy.\nCurrent energy: {energy}.")
    elif event == "order":
        if energy >= 30:
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins >= number:
            print(f"You bought {event}.")
            coins -= number
        else:
            print(f"Closed! Cannot afford {event}.")
            is_closed = True
            break

if not is_closed:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")
