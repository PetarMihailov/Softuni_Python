import re
data = input()

pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"


data = re.finditer(pattern, data)

print(" ".join([n.group() for n in data]))
