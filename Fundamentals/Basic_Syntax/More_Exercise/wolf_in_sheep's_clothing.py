animals = input().split(", ")[::-1]

if animals[0] == 'wolf':
    print('Please go away and stop eating my sheep')
elif "wolf" in animals:
    print(f"Oi! Sheep number {animals.index('wolf')}! You are about to be eaten by a wolf!")
