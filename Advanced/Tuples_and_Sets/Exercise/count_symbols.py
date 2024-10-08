string = input()

count = {}

for el in string:
    if el not in count:
        count[el] = string.count(el)

for el, value in sorted(count.items()):
    print(f"{el}: {value} time/s")
