data = [el.lower() for el in input().split()]

occurrences = {key: data.count(key) for key in data}

for key in occurrences:
    if not occurrences[key] % 2 == 0:
        print(key, end=" ")

# second solution

data = [el.lower() for el in input().split()]

occurrences = {key: data.count(key) for key in data if not data.count(key) % 2 == 0}

print(*occurrences)
