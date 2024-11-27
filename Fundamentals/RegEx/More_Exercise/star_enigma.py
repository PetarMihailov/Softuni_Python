import re


def star_enigma():
    # Number of messages
    n = int(input())

    # Prepare lists for attacked and destroyed planets
    attacked_planets = []
    destroyed_planets = []

    for _ in range(n):
        # Read the encrypted message
        encrypted_message = input()

        # Count the decryption key (letters [s, t, a, r] case-insensitive)
        key = sum(1 for char in encrypted_message if char.lower() in "star")

        # Decrypt the message by subtracting the key from each character
        decrypted_message = ''.join(chr(ord(char) - key) for char in encrypted_message)

        # Extract planet information using regex
        pattern = r"@(?P<planet>[A-Za-z]+)[^@\-!:>]*:(?P<population>\d+)[^@\-!:>]*!(?P<type>[AD])![^@\-!:>]*->(?P<soldiers>\d+)"
        match = re.search(pattern, decrypted_message)

        if match:
            planet_name = match.group("planet")
            attack_type = match.group("type")

            # Sort into attacked or destroyed based on the attack type
            if attack_type == "A":
                attacked_planets.append(planet_name)
            elif attack_type == "D":
                destroyed_planets.append(planet_name)

    # Sort planets alphabetically
    attacked_planets.sort()
    destroyed_planets.sort()

    # Print results
    print(f"Attacked planets: {len(attacked_planets)}")
    for planet in attacked_planets:
        print(f"-> {planet}")

    print(f"Destroyed planets: {len(destroyed_planets)}")
    for planet in destroyed_planets:
        print(f"-> {planet}")


# Run the function
star_enigma()
