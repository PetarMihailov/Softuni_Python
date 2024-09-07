animals = input().split(", ")

if animals[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    animal_position = len(animals) - animals.index("wolf") - 1
    print(f"Oi! Sheep number {animal_position}! You are about to be eaten by a wolf!")

print(len(animals))


def warn_the_sheep(queue):
    queue.reverse()
    the_wolf_position = queue.index("wolf")
    if the_wolf_position == 0:
        return 'Pls go away and stop eating my sheep'
    else:
        return "Oi! Sheep number " + str(the_wolf_position) + "! You are about to be eaten by a wolf!"

    array = input().split(", ")

    if array.pop() == "wolf":
        print("Please go away and stop eating my sheep")
        raise SystemExit

    arrReversed = array[::-1]

    for i in range(len(arrReversed)):
        if arrReversed[i] != "sheep":
            print(f"Oi! Sheep number {i + 1}! You are about to be eaten by a wolf!")


animals = input().split(", ")[::-1]

if animals[0] == 'wolf':
    print("Please go away and stop eating my sheep")
else:
    for index in range(len(animals)):
        if not animals[index] == 'sheep':
            print(f'Oi! Sheep number {index}! You are about to be eaten by a wolf!')


animals = input().split(", ")[::-1]

if animals[0] == 'wolf':
    print("Please go away and stop eating my sheep")
elif "wolf" in animals:
    print(f'Oi! Sheep number {animals.index("wolf")}! You are about to be eaten by a wolf!')


