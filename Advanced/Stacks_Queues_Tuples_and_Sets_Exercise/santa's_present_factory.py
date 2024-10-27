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
