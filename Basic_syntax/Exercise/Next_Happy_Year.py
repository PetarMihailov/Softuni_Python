year = int(input()) + 1

while True:
    flag = True
    new_year = str(year)
    for index_1 in range(len(new_year)):
        for index_2 in range(len(new_year)):
            if index_1 == index_2:
                continue
            if new_year[index_1] == new_year[index_2]:
                flag = False
                break

    if flag:
        print(year)
        break
    else:
        year += 1







