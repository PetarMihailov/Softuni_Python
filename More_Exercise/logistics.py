n = int(input())

bus = 0
truck = 0
train = 0
price = 0



for _ in range(n):
    cargo = int(input())

    if cargo <= 3:
        bus += cargo
        price += cargo * 200
    elif 4 <= cargo <= 11:
        truck += cargo
        price += cargo * 175
    else:
        train += cargo
        price += cargo * 120

total_cargo = bus + truck + train
average = price / total_cargo

print(f"{average:.2f}")
print(f"{bus/total_cargo*100:.2f}%")
print(f"{truck/total_cargo*100:.2f}%")
print(f"{train/total_cargo*100:.2f}%")
