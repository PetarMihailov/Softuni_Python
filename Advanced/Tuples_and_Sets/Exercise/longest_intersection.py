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
