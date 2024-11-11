a = int(input())
b = int(input())
max_passwords = int(input())

A_ascii = 35
B_ascii = 64

password_count = 0
passwords = []

for x in range(1, a + 1):
    for y in range(1, b + 1):
        password = f"{chr(A_ascii)}{chr(B_ascii)}{x}{y}{chr(B_ascii)}{chr(A_ascii)}"
        passwords.append(password)
        password_count += 1

        if password_count == max_passwords:
            break

        A_ascii += 1
        if A_ascii > 55:
            A_ascii = 35

        B_ascii += 1
        if B_ascii > 96:
            B_ascii = 64

    if password_count == max_passwords:
        break

print("|".join(passwords) + "|")
