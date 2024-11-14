eggs_in_store = int(input())

eggs_sold = 0

while True:
    command = input()
    if command == "Close":
        print("Store is closed!")
        print(f"{eggs_sold} eggs sold.")
        break

    eggs = int(input())

    if command == "Buy":
        if eggs <= eggs_in_store:
            eggs_in_store -= eggs
            eggs_sold += eggs
        else:
            print(f"Not enough eggs in store!")
            print(f"You can buy only {eggs_in_store}.")
            break

    elif command == "Fill":
        eggs_in_store += eggs
