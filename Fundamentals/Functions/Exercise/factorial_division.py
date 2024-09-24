def factorial(num):
    fact = 1
    for el in range(2, num+1):
        fact *= el
    return fact


def division(num_1, num_2):
    return factorial(num_1) / factorial(num_2)


first = int(input())
second = int(input())
print(f"{division(first, second):.2f}")
