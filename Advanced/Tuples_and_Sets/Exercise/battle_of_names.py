n = int(input())

odd = set()
even = set()

for row in range(1, n+1):
    name = input()
    result = sum([ord(el) for el in name]) // row

    if result % 2 == 0:
        even.add(result)
    else:
        odd.add(result)

if sum(odd) == sum(even):
    result = list(map(str, odd.union(even)))
    print(", ".join(result))
elif sum(odd) > sum(even):
    result = list(map(str, odd.difference(even)))
    print(", ".join(result))
else:
    result = list(map(str, odd.symmetric_difference(even)))
    print(", ".join(result))

