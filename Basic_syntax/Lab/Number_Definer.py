number = float(input())

if abs(number) < 1 and not number == 0:
    print("small", end=" ")
elif abs(number) > 1000000:
    print("large", end=" ")

if number < 0:
    print("negative")
elif number > 0:
    print("positive")
else:
    print("zero")

#
num = float(input())

number = ""

if abs(num) < 1 and not num == 0:
    number = "small"
elif abs(num) > 1000000:
    number = "large"

if num == 0:
    number = "zero"
elif num > 0:
    number += " positive"
else:
    number += " negative"

print(number)