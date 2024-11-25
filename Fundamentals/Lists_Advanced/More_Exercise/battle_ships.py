def count_destroyed_ships(field, attacks):
    destroyed_ships = 0

    # Process each attack
    for attack in attacks:
        row, col = map(int, attack.split('-'))
        # If there's a ship at the attacked position
        if field[row][col] > 0:
            field[row][col] -= 1
            # Check if the ship is destroyed
            if field[row][col] == 0:
                destroyed_ships += 1

    return destroyed_ships


n = int(input())
field = [list(map(int, input().split())) for _ in range(n)]
attacks = input().split()

result = count_destroyed_ships(field, attacks)

print(result)
