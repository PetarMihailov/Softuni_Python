hundreds_limit = int(input())
tens_limit = int(input())
units_limit = int(input())

prime_digits = [2, 3, 5, 7]

for hundreds in range(2, hundreds_limit + 1, 2):
    for tens in range(2, tens_limit + 1):
        if tens in prime_digits:
            for units in range(2, units_limit + 1, 2):
               print(f"{hundreds} {tens} {units}")
