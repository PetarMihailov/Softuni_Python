import re

def travel_points(map_string):
    pattern = r"(=|/)([A-Z][a-zA-Z]{2,})\1"
    matches = re.findall(pattern, map_string)
    destinations = [match[1] for match in matches]
    travel_points = sum(len(destination) for destination in destinations)
    print(f"Destinations: {', '.join(destinations)}")
    print(f"Travel Points: {travel_points}")


map_string = input()
travel_points(map_string)
