num_eggs = int(input())

red = 0
orange = 0
blue = 0
green = 0

for _ in range(num_eggs):
    color = input().strip()

    if color == "red":
        red += 1
    elif color == "orange":
        orange += 1
    elif color == "blue":
        blue += 1
    elif color == "green":
        green += 1

print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")

max_eggs = max(red, orange, blue, green)

if max_eggs == red:
    max_color = "red"
elif max_eggs == orange:
    max_color = "orange"
elif max_eggs == blue:
    max_color = "blue"
else:
    max_color = "green"

print(f"Max eggs: {max_eggs} -> {max_color}")
