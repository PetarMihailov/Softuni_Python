alphabet = {chr(97+num): num+1 for num in range(26)}

data = input().split()
result = 0

for el in data:
    first_letter = el[0]
    last_letter = el[-1]
    number = int(el[1:-1])
    if first_letter.isupper():
        number /= alphabet[first_letter.lower()]
    elif first_letter.islower():
        number *= alphabet[first_letter]

    if last_letter.isupper():
        number -= alphabet[last_letter.lower()]
    elif last_letter.islower():
        number += alphabet[last_letter]

    result += number

print(f"{result:.2f}")
