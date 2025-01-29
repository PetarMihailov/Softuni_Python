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

# second solution

def password_validator(password):
    errors = []
    if len(password) not in range(6, 11):
        errors.append("Password must be between 6 and 10 characters")
    if not password.isalnum():
        errors.append("Password must consist only of letters and digits")
    if sum(el.isdigit() for el in password) < 2:
        errors.append("Password must have at least 2 digits")

    if errors:
        return "\n".join(errors)
    else:
        return "Password is valid"

data = input()

print(password_validator(data))
