voucher_value = int(input())

ticket_count = 0
other_count = 0

while True:
    purchase = input()

    if purchase == "End":
        break  

    if len(purchase) > 8:
        price = ord(purchase[0]) + ord(purchase[1])
        if price > voucher_value:
            break  
        voucher_value -= price
        ticket_count += 1
    else:
        price = ord(purchase[0])
        if price > voucher_value:
            break  
        voucher_value -= price
        other_count += 1

print(ticket_count)
print(other_count)
