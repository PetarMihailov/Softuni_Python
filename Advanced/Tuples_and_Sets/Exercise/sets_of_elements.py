first, second = list(map(int, input().split()))

set_1 = set(int(input()) for num in range(first))
set_2 = set(int(input()) for number in range(second))

[print(num) for num in set_1.intersection(set_2)]
