
current_word = ""
secret_chars = {"c": False, "o": False, "n": False}
result = ""

while True:
    char = input()
    if char == "End":
        break

    if not char.isalpha():
        continue

    if char in secret_chars:
        if not secret_chars[char]:
            secret_chars[char] = True
        else:
            current_word += char
    else:
        current_word += char

    if all(secret_chars.values()):
        result += current_word + " "
        current_word = ""
        secret_chars = {"c": False, "o": False, "n": False}

print(result)


