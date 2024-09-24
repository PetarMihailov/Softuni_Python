def password_validator(value):
    is_valid = True
    if len(value) not in range(6, 11):
        is_valid = False
        print("Password must be between 6 and 10 characters")
    if not value.isalnum():
        is_valid = False
        print("Password must consist only of letters and digits")
    if not len([el for el in value if el.isdigit()]) >= 2:
        is_valid = False
        print("Password must have at least 2 digits")
    return is_valid

password = input()

valid = password_validator(password)

if valid:
    print("Password is valid")
