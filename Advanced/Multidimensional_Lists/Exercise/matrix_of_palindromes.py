rows, cols = [int(el) for el in input().split()]

matrix = []

for row in range(rows):
    row_chars = []

    for col in range(cols):
        first_and_last = chr(97 + row)
        middle = chr(97 + row + col)

        palindrome = first_and_last + middle + first_and_last
        row_chars.append(palindrome)

    matrix.append(row_chars)

for el in matrix:
    print(*el)
