budget = int(input())
price = input()

while not price == "End":
    budget -= int(price)
    if budget < 0:
        print("You went in overdraft!")
        break

    price = input()

else:
    print("You bought everything needed.")