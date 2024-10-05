from collections import deque

n = int(input())

stations = deque()

for _ in range(n):
    stations.append(input())

for pumps in range(n):
    is_valid = True
    tank = 0
    for pump in range(n):
        current_station = stations[pump]
        petrol, distance = current_station.split()
        petrol = int(petrol)
        distance = int(distance)
        tank += petrol - distance

        if tank < 0:
            is_valid = False
            stations.append(stations.popleft())
            break

    if is_valid:
        print(pumps)
        break
