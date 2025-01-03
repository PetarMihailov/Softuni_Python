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

# second solution

cards = input().split()
shuffles = int(input())

for _ in range(shuffles):
    half = len(cards) // 2
    left_half = cards[:half]
    right_half = cards[half:]
    cards = [card for pair in zip(left_half, right_half) for card in pair]

print(cards)
