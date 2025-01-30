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

# second solution

import math


def factorial_division(num1, num2):
    factorial1 = math.factorial(num1)
    factorial2 = math.factorial(num2)
    result = factorial1 / factorial2
    return f"{result:.2f}"


num_1 = int(input())
num_2 = int(input())

print(factorial_division(num_1, num_2))
