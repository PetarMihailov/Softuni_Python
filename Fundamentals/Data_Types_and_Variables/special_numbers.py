n = int(input())

for num in range(1, n+1):
    result = sum([int(el) for el in list(str(num))])

    if result in [5, 7, 11]:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")
