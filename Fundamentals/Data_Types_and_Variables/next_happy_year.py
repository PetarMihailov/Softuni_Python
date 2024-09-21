year = input()
next_year = int(year) + 1

while True:
    if len(set(str(next_year))) == len(list(year)):
        print(next_year)
        break

    next_year += 1
