start = input()
end = input()
not_included = input()

combinations = []

for i in range(ord(start), ord(end) +1 ):
    for j in range(ord(start), ord(end) +1 ):
        for k in range(ord(start), ord(end) +1):
            if not chr(i) == not_included and not chr(j) == not_included and not chr(k) == not_included:
                combinations.append(f"{chr(i)}{chr(j)}{chr(k)}")

combinations.append(len(combinations))

print(*combinations)
