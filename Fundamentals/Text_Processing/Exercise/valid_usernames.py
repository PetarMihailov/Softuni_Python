import re
def is_valid_username(username):
    if not len(username) in range(3, 17):
        return False
    if not re.match("^[a-zA-Z0-9_-]+$", username):
        return False
    return True


def print_valid_usernames(usernames_line):
    usernames = usernames_line.split(", ")
    for username in usernames:
        if is_valid_username(username):
            print(username)


data = input()

print_valid_usernames(data)
