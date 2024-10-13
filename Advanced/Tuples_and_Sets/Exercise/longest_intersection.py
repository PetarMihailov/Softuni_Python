n = int(input())

intersections = []

for _ in range(n):
    first, second = input().split("-")
    start, end = [int(el) for el in first.split(",")]
    first_seq = range(start, end+1)
    start, end = [int(el) for el in second.split(",")]
    second_seq = range(start, end+1)
    intersections.append(set(first_seq).intersection(second_seq))

sort = sorted(intersections, key=lambda x: -len(x))[0]

print(f"Longest intersection is {list(sort)} with length {len(sort)}")

# solution 2

lines = int(input())

longest_intersection = []

for _ in range(lines):
    first_data, second_data = input().split("-")
    first_start, first_end = [int(el) for el in first_data.split(",")]
    second_start, second_end = [int(el) for el in second_data.split(",")]

    intersection = range(max(first_start, second_start), min(first_end, second_end) + 1)
    longest_intersection.append(intersection)

longest_intersection= sorted(longest_intersection, key=lambda x: -len(x))[0]

print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")
