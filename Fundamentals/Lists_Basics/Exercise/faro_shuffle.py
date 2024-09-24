cards = input().split()
count = int(input())

top = cards.pop(0)
bottom = cards.pop(-1)

shuffle = []

for _ in range(count):
    left_half = cards[:len(cards) // 2]
    right_half = cards[len(cards) // 2:]
    for index_1 in range(len(left_half)):
        shuffle.append(right_half[index_1])
        shuffle.append(left_half[index_1])

    cards = shuffle
    shuffle = []

cards.insert(0, top)
cards.append(bottom)

print(cards)
