import re
data = input()
search = input()

pattern = rf"\b{search}\b"

result = re.findall(pattern, data, re.IGNORECASE)

print(len(result))
