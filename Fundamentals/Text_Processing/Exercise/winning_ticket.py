def is_jackpot(ticket):
    for symbol in symbols:
        if symbol in ticket and ticket.count(symbol) == 20:
            print(f"ticket \"{ticket}\" - {ticket.count(symbol) // 2}{symbol} Jackpot!")
            return True
    return False


def is_invalid(ticket):
    if not len(ticket) == 20:
        print("invalid ticket")
        return True
    return False


def is_winning(ticket):
    count = 6
    left_half = ticket[:10]
    right_half = ticket[10:]
    for symbol in symbols:
        if symbol*6 in left_half and symbol*6 in right_half:
            for index in range(7, 11):
                if index*symbol in left_half and index*symbol in right_half:
                    count += 1
            print(f"ticket \"{ticket}\" - {count}{symbol}")
            return True
    return False


tickets = [el.strip() for el in input().split(", ")]

symbols = ["@", "#", "$", "^"]

for ticket in tickets:
    if is_invalid(ticket):
        continue
    if is_jackpot(ticket):
        continue
    if is_winning(ticket):
        continue

    print(f"ticket \"{ticket}\" - no match")


