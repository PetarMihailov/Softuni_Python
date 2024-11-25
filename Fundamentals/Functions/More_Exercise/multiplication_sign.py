def multiplication_sign(a, b, c):
    negative_count = sum(1 for el in (a, b, c) if el < 0)

    if 0 in (a, b, c):
        return "zero"
    elif negative_count % 2 == 0:
        return "positive"
    else:
        return "negative"


a = int(input())
b = int(input())
c = int(input())
print(multiplication_sign(a, b, c))
