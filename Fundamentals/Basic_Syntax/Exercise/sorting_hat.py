command = input()

flag = False

while not command == "Welcome!":
    if command == "Voldemort":
        print("You must not speak of that name!")
        flag = True
        break
    elif len(command) < 5:
        print(f"{command} goes to Gryffindor.")
    elif len(command) == 5:
        print(f"{command} goes to Slytherin.")
    elif len(command) == 6:
        print(f"{command} goes to Ravenclaw.")
    else:
        print(f"{command} goes to Hufflepuff.")

    command = input()

if not flag:
    print("Welcome to Hogwarts.")
