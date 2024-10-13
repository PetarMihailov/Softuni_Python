string = input()

count = {}

for el in string:
    if el not in count:
        count[el] = string.count(el)

for el, value in sorted(count.items()):
    print(f"{el}: {value} time/s")

# second solution

text = input()

symbols = {char: text.count(char) for char in text}

sorted_symbols = sorted(symbols.items())

[print(f"{symbol[0]}: {symbol[1]} time/s") for symbol in sorted_symbols]
