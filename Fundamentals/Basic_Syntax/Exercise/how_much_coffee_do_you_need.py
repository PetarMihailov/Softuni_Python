command = input()

events = ["coding", "dog", "cat", "movie"]
coffees = 0

while not command == "END":
    if command.lower() in events:
        if command.islower():
            coffees += 1
        else:
            coffees += 2

        if coffees > 5:
            print("You need extra sleep")
            break

    command = input()

else:
    print(coffees)
