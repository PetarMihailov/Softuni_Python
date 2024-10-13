data = input()

phonebook = {}

while not data.isdigit():
    name, number = data.split("-")
    phonebook[name] = number

    data = input()

line = int(data)

for _ in range(line):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")

# second solution



def fill_phonebook():
    data = input()
    phonebook = {}
    while not data.isdigit():
        name, number = data.split("-")
        phonebook[name] = number
        data = input()
    return phonebook, data

def search_contact(contact_name, phonebook):
    if phonebook.get(contact_name):
        print(f"{contact_name} -> {phonebook[contact_name]}")
    else:
        print(f"Contact {contact_name} does not exist.")



phone_book, line = fill_phonebook()

for _ in range(int(line)):
    search_contact(input(), phone_book)
