strings = input().split()

repeated_strings = [el * len(el) for el in strings]

print("".join(repeated_strings))
