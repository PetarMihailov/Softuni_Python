def judge_system():
    contests = {}
    individual_standings = {}

    # Process input
    while True:
        line = input()
        if line == "no more time":
            break
        username, contest, points = line.split(" -> ")
        points = int(points)

        # Add contest if not present
        if contest not in contests:
            contests[contest] = {}

        # Update points for the contest
        if username not in contests[contest]:
            contests[contest][username] = points
        else:
            # Update only if the new points are higher
            if points > contests[contest][username]:
                contests[contest][username] = points

        # Update total points for individual standings
        if username not in individual_standings:
            individual_standings[username] = 0
        individual_standings[username] = sum(
            contests[c].get(username, 0) for c in contests
        )

    # Print contests in order of input
    for contest, participants in contests.items():
        print(f"{contest}: {len(participants)} participants")
        sorted_participants = sorted(
            participants.items(),
            key=lambda x: (-x[1], x[0])
        )
        for i, (user, score) in enumerate(sorted_participants, 1):
            print(f"{i}. {user} <::> {score}")

    # Print individual standings
    print("Individual standings:")
    sorted_individuals = sorted(
        individual_standings.items(),
        key=lambda x: (-x[1], x[0])
    )
    for i, (user, total_points) in enumerate(sorted_individuals, 1):
        print(f"{i}. {user} -> {total_points}")


judge_system()
