vowels = ["a", "o", "e", "i", "u", "A", "O", "E", "I", "U"]

text = input()

no_vowels = [el for el in text if not el in vowels]

print("".join(no_vowels))
