import re

data = input()

pattern = "\\b[A-Z][a-z]+\s[A-Z][a-z]+\\b" # match tab
pattern_1 = "\\b[A-Z][a-z]+ [A-Z][a-z]+\\b"

name = re.findall(pattern_1, data)

print(" ".join(name))
