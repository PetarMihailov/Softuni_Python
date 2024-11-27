import re

def race_results():
    # Read the list of participants
    participants = input().split(", ")

    # Dictionary to store racers and their distances
    racer_data = {racer: 0 for racer in participants}

    # Process the race data
    while True:
        data = input()
        if data == "end of race":
            break

        # Extract name (letters only) and distance (digits only)
        name = "".join(re.findall(r"[A-Za-z]", data))
        distance = sum(map(int, re.findall(r"\d", data)))

        # Update distance if name is in participants
        if name in racer_data:
            racer_data[name] += distance

    # Sort participants by distance in descending order
    sorted_racers = sorted(racer_data.items(), key=lambda x: -x[1])

    places = ["1st", "2nd", "3rd"]
    for i in range(min(3, len(sorted_racers))):
        print(f"{places[i]} place: {sorted_racers[i][0]}")


race_results()
