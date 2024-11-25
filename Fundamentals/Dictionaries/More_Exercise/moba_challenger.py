def moba_tracker():
    players = {}

    while True:
        command = input()
        if command == "Season end":
            break

        if " -> " in command:
            # Add or update player position and skill
            player, position, skill = command.split(" -> ")
            skill = int(skill)

            if player not in players:
                players[player] = {}

            if position not in players[player] or players[player][position] < skill:
                players[player][position] = skill

        elif " vs " in command:
            # Handle player vs player duel
            player1, player2 = command.split(" vs ")

            if player1 in players and player2 in players:
                # Check for common positions
                common_positions = set(players[player1]) & set(players[player2])
                if common_positions:
                    # Calculate total skills
                    total_skill_player1 = sum(players[player1].values())
                    total_skill_player2 = sum(players[player2].values())

                    if total_skill_player1 > total_skill_player2:
                        del players[player2]
                    elif total_skill_player2 > total_skill_player1:
                        del players[player1]

    # Calculate total skills and sort players
    sorted_players = sorted(
        players.items(),
        key=lambda x: (-sum(x[1].values()), x[0])
    )

    # Print results
    for player, positions in sorted_players:
        total_skill = sum(positions.values())
        print(f"{player}: {total_skill} skill")

        sorted_positions = sorted(
            positions.items(),
            key=lambda x: (-x[1], x[0])
        )
        for position, skill in sorted_positions:
            print(f"- {position} <::> {skill}")


# Example usage:
# Input example:
# Peter -> Support -> 250
# George -> Tank -> 300
# Simon -> Support -> 200
# George vs Simon
# Season end
moba_tracker()
