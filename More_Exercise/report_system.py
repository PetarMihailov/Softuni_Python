budget = float(input())

command = input()

cash = 0
cash_count = 0
credit = 0
credit_count = 0
count = 0
sold = False

while not command == "End":
    command = float(command)

    if count % 2 == 0:
        if command > 100:
            print("Error in transaction!")
        else:
            cash += command
            cash_count += 1
            print("Product sold!")
    else:
        if command < 10:
            print("Error in transaction!")
        else:
            credit += command
            credit_count += 1
            print("Product sold!")

    if cash + credit >= budget:
        sold = True
        break

    count += 1
    command = input()

if sold:
    acs = cash / cash_count
    acc = credit / credit_count
    print(f"Average CS: {acs:.2f}\nAverage CC: {acc:.2f}")
else:
    print("Failed to collect required money for charity.")
