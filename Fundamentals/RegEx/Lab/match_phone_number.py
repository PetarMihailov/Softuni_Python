import re

data = input()

pattern = r"(\+359\s2\s\d{3}\s\d{4}\b|\+359-2-\d{3}-\d{4}\b)"
pattern_1 = r"\+359( |-)2\1\d{3}\1\d{4}\b"
phones = re.finditer(pattern, data)
phones = [p.group(0) for p in phones]
result = [el.group() for el in re.finditer(pattern_1, data)]


print(", ".join(result))
