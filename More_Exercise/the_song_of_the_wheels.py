control_value = int(input())

valid_combinations = []
found_password = None

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if (a < b) and (c > d) and (a * b + c * d == control_value):
                    combination = f"{a}{b}{c}{d}"
                    valid_combinations.append(combination)

                    if len(valid_combinations) == 4:
                        found_password = combination

print(" ".join(valid_combinations))

if found_password:
    print(f"Password: {found_password}")
else:
    print("No!")
