def decrypt_message(key, messages):
    key = list(map(int, key.split()))
    key_length = len(key)

    for message in messages:
        decrypted_message = ""
        for i, char in enumerate(message):
            decrypted_char = chr(ord(char) - key[i % key_length])
            decrypted_message += decrypted_char

        treasure_type = decrypted_message.split('&')[1]
        coordinates = decrypted_message.split('<')[1].split('>')[0]
        print(f"Found {treasure_type} at {coordinates}")


key = input()
messages = []

while True:
    line = input()
    if line.lower() == "find":
        break
    messages.append(line)

decrypt_message(key, messages)
