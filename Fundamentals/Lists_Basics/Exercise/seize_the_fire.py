HIGH = range(81, 126)
MEDIUM = range(51, 81)
LOW = range(1, 51)

type_of_fire = input().split("#")
water = int(input())

effort = 0
cells = []

for fire in type_of_fire:
    type_fire, cell = fire.split(" = ")
    cell = int(cell)

    if type_fire == "High" and cell not in HIGH:
        continue
    elif type_fire == "Low" and cell not in LOW:
        continue
    elif type_fire == "Medium" and cell not in MEDIUM:
        continue

    if water >= cell:
        water -= cell
        effort += cell * 0.25
        cells.append(cell)

print("Cells:")
for cell in cells:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}\nTotal Fire: {sum(cells)}")

# second solution

data = input().split("#")
water = int(input())

ranges = {"High": range(81, 126),
        "Medium": range(51, 81),
        "Low": range(1, 51)}

effort = 0
cells = []

for el in data:
    fire, cell = el.split(" = ")
    cell = int(cell)

    if cell in ranges[fire] and water >= cell:
        water -= cell
        effort += cell * 0.25
        cells.append(cell)


print("Cells:")
for cell in cells:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(cells)}")

