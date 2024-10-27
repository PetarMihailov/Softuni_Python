from collections import deque
boxes = list(map(int, input().split()))
magics = deque(map(int, input().split()))

presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

crafted_presents = {

}

while boxes and magics:
    box = boxes.pop()
    magic = magics.popleft()

    result = box * magic

    if result in presents:
        toy = presents[result]
        if toy in crafted_presents:
            crafted_presents[toy] += 1
        else:
            crafted_presents[toy] = 1
    elif result < 0:
        boxes.append(box + magic)
    elif result > 0:
        boxes.append(box + 15)
    else:
        if box == 0 and magic == 0:
            continue
        elif box == 0:
            magics.appendleft(magic)
        elif magic == 0:
            boxes.append(box)

if ("Doll" in crafted_presents and "Wooden train" in crafted_presents) or \
        ("Teddy bear" in crafted_presents and "Bicycle" in crafted_presents):
    print(f"The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if boxes:
    print(f"Materials left: {', '.join([str(el) for el in reversed(boxes)])}")
if magics:
    print(f"Magic left: {', '.join([str(el) for el in magics])}")

for present, count in sorted(crafted_presents.items()):
    print(f"{present}: {count}")

# second solution

from collections import deque

def check(present):
    if present["Doll"]["qty"] >= 1 and  present["Wooden train"]["qty"] >= 1:
        return True
    elif present["Teddy bear"]["qty"] >= 1 and present["Bicycle"]["qty"] >= 1:
        return True
    return False


materials = [el for el in map(int, input().split())]
magics = deque([el for el in map(int, input().split())])

presents = {"Doll": {"magic": 150, "qty": 0},
           "Wooden train": {"magic": 250, "qty": 0},
           "Teddy bear": {"magic": 300, "qty": 0},
           "Bicycle": {"magic": 400, "qty": 0}}

while materials and magics:
    material, magic = materials.pop(), magics.popleft()
    result = material * magic
    is_equal = False

    if material == 0 and magic == 0:
        continue
    elif material == 0:
        magics.appendleft(magic)
        continue
    elif magic == 0:
        materials.append(material)
        continue

    if result < 0:
        result = material + magic
        materials.append(result)
        continue

    for data in presents.values():
        if result == data["magic"]:
            data["qty"] += 1
            is_equal = True
            break

    if not is_equal:
        materials.append(material + 15)


if check(presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(map(str, materials[::-1]))}")
if magics:
    print(f"Magic left: {', '.join(map(str, magics))}")

for key, val in sorted(presents.items()):
    if val["qty"] > 0:
        print(f"{key}: {val['qty']}")
