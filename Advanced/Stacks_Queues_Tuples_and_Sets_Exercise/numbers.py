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



