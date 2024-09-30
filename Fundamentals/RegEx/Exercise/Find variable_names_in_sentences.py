import re

data = input()

pattern = r"((?<=^_)|(?<=\s_))[A-Za-z0-9]+($|(?=[\s\.]))"

match = re.finditer(pattern, data)
result = [el.group() for el in match]
print(",".join(result))
