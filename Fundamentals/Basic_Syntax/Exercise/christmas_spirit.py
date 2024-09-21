qty = int(input())
days = int(input())

budget = 0
spirit = 0

ORNAMENT_SET = 2
TREE_SKIRTS = 5
TREE_GARLANDS = 3
TREE_LIGHT = 15

for day in range(1, days + 1):
    if day % 11 == 0:
        qty += 2
    if day % 2 == 0:
        budget += ORNAMENT_SET * qty
        spirit += 5
    if day % 3 == 0:
        budget += TREE_SKIRTS * qty + TREE_GARLANDS * qty
        spirit += 13
    if day % 5 == 0:
        budget += TREE_LIGHT * qty
        spirit += 17
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        budget += TREE_SKIRTS + TREE_GARLANDS + TREE_LIGHT
    if day == days and day % 10 == 0:
        spirit -= 30

print(f'Total cost: {budget}\nTotal spirit: {spirit}')

