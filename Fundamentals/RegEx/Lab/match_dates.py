import re

data = input()

pattern = r"(?P<day>\d{2})(?P<separator>[-/\.])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})"

matches = [el.groupdict() for el in re.finditer(pattern, data)]

print("\n".join([f"Day: {el['day']}, Month: {el['month']}, Year: {el['year']}" for el in matches]))
