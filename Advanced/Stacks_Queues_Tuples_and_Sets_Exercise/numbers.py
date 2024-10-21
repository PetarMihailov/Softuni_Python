first_sequence = set(list(map(int, input().split())))
second_sequence = set(list(map(int, input().split())))

line = int(input())

for _ in range(line):
    data = input().split()

    if data[0] == "Add":
        if data[1] == "First":
            first_sequence.update(list(map(int, data[2:])))
        else:
            second_sequence.update(list(map(int, data[2:])))
    elif data[0] == "Remove":
        if data[1] == "First":
            first_sequence = first_sequence.difference([int(el) for el in data[2:]])
        else:
            second_sequence = second_sequence.difference([int(el) for el in data[2:]])
    else:
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))

print(*sorted(first_sequence), sep=", ")
print(", ".join([str(el) for el in sorted(list(second_sequence))]))


# second solution

first_sequence = set(list(map(int, input().split())))
second_sequence = set(list(map(int, input().split())))

line = int(input())

for _ in range(line):
    data = input().split()

    if data[0] == "Add":
        if data[1] == "First":
            [first_sequence.add(int(el)) for el in data[2:]]
        else:
            [second_sequence.add(int(el)) for el in data[2:]]
    elif data[0] == "Remove":
        if data[1] == "First":
            for el in data[2:]:
                first_sequence.discard(int(el))
        else:
            for el in data[2:]:
                second_sequence.discard(int(el))
    else:
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))

print(*sorted(first_sequence), sep=", ")
print(", ".join([str(el) for el in sorted(list(second_sequence))]))

# third solution

set_1 = set([int(el) for el in input().split()])
set_2 = set([int(el) for el in input().split()])

lines = int(input())

for _ in range(lines):
    data = input().split()

    if data[0] == "Add" and data[1] ==  "First":
        set_1.update(set([int(el) for el in data[2:]]))
    elif data[0] == "Add" and data[1] == "Second":
        set_2.update(set([int(el) for el in data[2:]]))
    elif data[0] == "Remove" and data[1] == "First":
        set_1 = set_1.difference(set([int(el) for el in data[2:]]))
    elif data[0] == "Remove" and data[1] == "Second":
        set_2 = set_2.difference(set([int(el) for el in data[2:]]))
    elif data[0] == "Check" and data[1] == "Subset":
        print(set_1.issubset(set_2) or set_2.issubset(set_1))

print(*sorted(set_1), sep=", ")


