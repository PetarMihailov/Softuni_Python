numbers = [int(num) for num in input().split(", ")]

boundary = 10

while numbers:
    group = []
    for num in numbers:
        if num <= boundary:
            group.append(num)

    for num in group:
        if num in numbers:
            numbers.remove(num)

    print(f"Group of {boundary}'s: {group}")
    boundary += 10
