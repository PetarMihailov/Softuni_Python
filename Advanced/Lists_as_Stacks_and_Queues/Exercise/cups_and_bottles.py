from collections import deque
cups = deque(list(map(int, input().split())))
bottles = list(map(int, input().split()))

waste = 0

while cups and bottles:

    if bottles[-1] >= cups[0]:
        waste += bottles.pop() - cups.popleft()
    else:
        if cups[0] >= 0:
            cups[0] -= bottles.pop()

if cups:
    print(f"Cups:", *cups)
else:
    print(f"Bottles:", *bottles)

print(f"Wasted litters of water: {waste}")
