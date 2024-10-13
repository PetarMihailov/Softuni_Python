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

# solution 2

lines = int(input())

even_numbers = set()
odd_numbers = set()

for row in range(1, lines+1):
    current_sum = sum([ord(el) for el in input()]) // row

    if current_sum % 2 == 0:
        even_numbers.add(current_sum)
    else:
        odd_numbers.add(current_sum)

sum_evens = sum(even_numbers)
sum_odds = sum(odd_numbers)

if sum_evens == sum_odds:
    str_set = [str(el) for el in odd_numbers.union(even_numbers)]
    print(", ".join(str_set))
elif sum_evens < sum_odds:
    str_set = [str(el) for el in odd_numbers.difference(even_numbers)]
    print(", ".join(str_set))
else:
    str_set = [str(el) for el in odd_numbers.symmetric_difference(even_numbers)]
    print(", ".join(str_set))
