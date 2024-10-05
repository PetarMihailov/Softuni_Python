from collections import deque
green_light = int(input())
free_window = int(input())
data = input()

cars = deque()
counter = 0
flag = False

while not data == "END":
    if data == "green":
        current_green = green_light
        while cars and current_green > 0:
            current_car = cars.popleft()
            if current_green >= len(current_car) or current_green+free_window >= len(current_car):
                counter += 1
                current_green -= len(current_car)
            else:
                idx = free_window+current_green
                print("A crash happened!")
                print(f"{current_car} was hit at {current_car[idx]}.")
                flag = True
                break
    else:
        cars.append(data)
    if flag:
        break

    data = input()

if not flag:
    print("Everyone is safe.")
    print(f"{counter} total cars passed the crossroads.")
