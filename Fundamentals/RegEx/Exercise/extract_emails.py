import re

data = input()

pattern = r"(^|(?<=\s))[A-Za-z0-9]+[\._-]?[A-Za-z0-9]+@[A-Za-z]+\-?[A-Za-z]+(\.[A-Za-z]+-?[a-zA-z]+)+($|(?=.))"

result = [el.group() for el in re.finditer(pattern, data)]

print("\n".join(result))
