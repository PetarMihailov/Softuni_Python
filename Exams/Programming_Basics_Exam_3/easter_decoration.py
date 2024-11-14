prices = {
    "basket": 1.50,
    "wreath": 3.80,
    "chocolate bunny": 7.00
}

num_clients = int(input())

total_spent = 0  
total_clients = 0 

for _ in range(num_clients):
    client_items = 0  
    client_total = 0  

    while True:
        item = input()
        if item == "Finish":
            break
        client_items += 1
        client_total += prices[item]

    if client_items % 2 == 0:
        client_total *= 0.8

    total_spent += client_total
    total_clients += 1

    print(f"You purchased {client_items} items for {client_total:.2f} leva.")

average_bill = total_spent / total_clients
print(f"Average bill per client is: {average_bill:.2f} leva.")
