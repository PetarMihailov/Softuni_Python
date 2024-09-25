message = input().split()

letter = []

for el in message:
    letters = list(el)
    numbers = [i for i in letters if i.isdigit()]
    numbers = "".join(numbers)
    word = [el for el in letters if not el.isdigit()]
    first = int(numbers)
    letter.append(chr(first))
    word[-1], word[0] = word[0], word[-1]
    letter += word
    letter.append(" ")


print("".join(letter))
