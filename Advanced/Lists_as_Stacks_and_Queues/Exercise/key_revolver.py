from collections import deque
price_bullet = int(input())
size_barrel = int(input())
bullets = list(map(int, input().split()))
locks = deque(list(map(int, input().split())))
intelligence = int(input())

shots = 0

while locks:
    if not bullets:
        break
    if locks[0] >= bullets[-1]:
        bullets.pop()
        locks.popleft()
        shots += 1
        intelligence -= price_bullet
        print("Bang!")
    elif locks[0] < bullets[-1]:
        bullets.pop()
        shots += 1
        intelligence -= price_bullet
        print("Ping!")

    if shots == size_barrel and bullets:
        print("Reloading!")
        shots = 0

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${intelligence}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
