def odd_and_even_sum(num):
    num = list(map(int, num))
    odd_sum = sum([el for el in num if not el % 2 == 0])
    even_sum = sum([el for el in num if el % 2 == 0])
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number = input()

print(odd_and_even_sum(number))
