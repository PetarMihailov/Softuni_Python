def check_index(idx_1, idx_2, string):
    return 0 <= idx_1 <= idx_2 < len(string)


username = input()
command = input()

while not command == "Registration":
    data = command.split()
    if data[0] == "Letters":
        if data[1] == "Lower":
            username = username.lower()
            print(username)
        elif data[1] == "Upper":
            username = username.upper()
            print(username)
    elif data[0] == "Reverse":
        start_index, end_index = map(int, data[1:])
        if check_index(start_index, end_index, username):
            string = username[start_index:end_index+1]
            print(string[::-1])
    elif data[0] == "Substring":
        if data[1] in username:
            username = username.replace(data[1], "", 1)
            print(username)
        else:
            print(f"The username {username} doesn't contain {data[1]}.")
    elif data[0] == "Replace":
        username = username.replace(data[1], "-")
        print(username)
    elif data[0] == "IsValid":
        if data[1] in username:
            print("Valid username.")
        else:
            print(f"{data[1]} must be contained in your username.")


    command = input()
