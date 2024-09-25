rooms = int(input())

free_chairs = 0
flag = True

for room in range(1, rooms+1):
    chairs, people = input().split()
    people = int(people)
    diff = len(chairs) - people

    if diff >= 0:
        free_chairs += diff
    else:
        flag = False
        print(f"{abs(diff)} more chairs needed in room {room}")

if flag:
    print(f"Game On, {free_chairs} free chairs left")
