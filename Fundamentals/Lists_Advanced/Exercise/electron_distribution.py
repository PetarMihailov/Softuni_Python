electrons = int(input())

shell = []
index = 1

while electrons > 0:
    shell_electrons = 2 * index ** 2

    if electrons < shell_electrons:
        shell_electrons = electrons
        shell.append(shell_electrons)
        electrons = 0
    else:
        shell.append(shell_electrons)
        electrons -= shell_electrons

    index += 1

print(shell)
