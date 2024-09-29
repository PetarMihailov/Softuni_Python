text = input()

cipher = [chr(ord(el) + 3) for el in text]

print("".join(cipher))
