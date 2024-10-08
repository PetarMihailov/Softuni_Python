numbers = list(map(float, input().split()))

counts = {key: numbers.count(key) for key in numbers}

print('\n'.join([f"{data[0]} - {data[1]} times" for data in counts.items()]))


# solution 2

numbers = (float(el) for el in input().split())

occ = {}

for el in numbers:
    if el not in occ:
        occ[el] = 0
    occ[el] += 1

for el in occ:
    print(f"{el} - {occ[el]} times")
