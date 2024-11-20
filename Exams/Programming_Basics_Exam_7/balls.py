n = int(input())  

total_points = 0
red_count = 0
orange_count = 0
yellow_count = 0
white_count = 0
other_count = 0
black_divides = 0

for _ in range(n):
    color = input().strip().lower()
    if color == "red":
        total_points += 5
        red_count += 1
    elif color == "orange":
        total_points += 10
        orange_count += 1
    elif color == "yellow":
        total_points += 15
        yellow_count += 1
    elif color == "white":
        total_points += 20
        white_count += 1
    elif color == "black":
        total_points //= 2
        black_divides += 1
    else:
        other_count += 1

print(f"Total points: {total_points}")
print(f"Red balls: {red_count}")
print(f"Orange balls: {orange_count}")
print(f"Yellow balls: {yellow_count}")
print(f"White balls: {white_count}")
print(f"Other colors picked: {other_count}")
print(f"Divides from black balls: {black_divides}")
