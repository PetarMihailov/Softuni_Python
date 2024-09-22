n = int(input())

tank = 0

for _ in range(n):
    water = int(input())

    if tank + water <= 255:
        tank += water
    else:
        print("Insufficient capacity!")

print(tank)
