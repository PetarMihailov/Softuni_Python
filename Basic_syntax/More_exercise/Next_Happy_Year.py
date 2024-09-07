year = int(input()) + 1

while True:
    year_as = str(year)
    flag = True
    for index_1 in range(len(year_as)):
        for index_2 in range(len(year_as)):
            if index_1 == index_2:
                continue
            if year_as[index_1] == year_as[index_2]:
                flag = False
                break

    if flag:
        print(year)
        break
    else:
        year += 1

year = int(input()) + 1

while True:
    year += 1
    if len(str(year)) == len(set(str(year))):
        print(year)
        break

