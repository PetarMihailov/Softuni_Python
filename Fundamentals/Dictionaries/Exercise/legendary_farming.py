mapper = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
materials = {"shards": 0, "fragments": 0, "motes": 0}

junk = {}
is_found = False

while True:
    data = input().split()

    for index in range(0, len(data), 2):
        qty, material = int(data[index]), data[index+1].lower()

        if material in materials:
            materials[material] += qty
            if materials[material] >= 250:
                materials[material] -= 250
                print(f"{mapper[material]} obtained!")
                is_found = True
                break
        else:
            if material not in junk:
                junk[material] = 0
            junk[material] += qty

    if is_found:
        break

for key in materials:
    print(f"{key}: {materials[key]}")

for key in junk:
    print(f"{key}: {junk[key]}")
