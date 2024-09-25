command = input()

to_do_list = [0] * 10

while not command == "End":
    priority, task = command.split("-")
    priority = int(priority) - 1
    to_do_list.pop(priority)
    to_do_list.insert(priority, task)

    command = input()

print([el for el in to_do_list if not el == 0])
