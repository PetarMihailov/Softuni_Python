text = input()

count = {char: text.count(char) for char in text if not char.isspace()}

for key, value in count.items():
    print(f"{key} -> {value}")
