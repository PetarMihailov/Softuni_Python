def manage_stock():
    stock = {}
    total_sold = 0

    while True:
        command_line = input()
        if command_line == "Complete":
            break

        command_parts = command_line.split()
        action = command_parts[0]
        quantity = int(command_parts[1])
        food = command_parts[2]

        if action == "Receive":
            if quantity > 0:
                if food not in stock:
                    stock[food] = 0
                stock[food] += quantity

        elif action == "Sell":
            if food not in stock:
                print(f"You do not have any {food}.")
            else:
                if stock[food] < quantity:
                    sold_quantity = stock[food]
                    print(f"There aren't enough {food}. You sold the last {sold_quantity} of them.")
                    total_sold += sold_quantity
                    del stock[food]
                else:
                    stock[food] -= quantity
                    total_sold += quantity
                    print(f"You sold {quantity} {food}.")
                    if stock[food] == 0:
                        del stock[food]

    for item, qty in stock.items():
        print(f"{item}: {qty}")
    print(f"All sold: {total_sold} goods")


manage_stock()
