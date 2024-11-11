start = int(input())
end = int(input())
magic_number = int(input())

combination_count = 0
found = False

for first in range(start, end + 1):
    for second in range(start, end + 1):
        combination_count += 1
        if first + second == magic_number:
            print(f"Combination N:{combination_count} ({first} + {second} = {magic_number})")
            found = True
            break
    if found:
        break

if not found:
    print(f"{combination_count} combinations - neither equals {magic_number}")
