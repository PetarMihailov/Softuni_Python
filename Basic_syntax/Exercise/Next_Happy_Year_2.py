year = int(input()) + 1

next_happy_year = ""

while True:
    next_year = str(year)
    for index in range(len(next_year)):
        if next_year[index] not in next_happy_year:
            next_happy_year += next_year[index]
    if len(next_happy_year) == len(next_year):
        break

    next_happy_year = ""
    year += 1

print(next_happy_year)