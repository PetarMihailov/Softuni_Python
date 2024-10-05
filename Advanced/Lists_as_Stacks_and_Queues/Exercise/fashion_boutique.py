box_of_clothes = [int(el) for el in input().split()]
capacity_of_rack = int(input())

racks = 0
sum_of_clothes = 0

while box_of_clothes:
    clothes = box_of_clothes.pop()
    sum_of_clothes += clothes
    if sum_of_clothes > capacity_of_rack:
        sum_of_clothes = 0
        box_of_clothes.append(clothes)
        racks += 1
    elif sum_of_clothes == capacity_of_rack:
        sum_of_clothes = 0
        racks +=1
    elif len(box_of_clothes) == 0:
        racks += 1

print(racks)
