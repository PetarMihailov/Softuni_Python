num = float(input())

if abs(num) < 1 and not num == 0:
    print("small", end=" ")
elif abs(num) > 1000000:
    print("large", end=" ")

if num < 0:
    print("negative")
elif num > 0:
    print("positive")
else:
    print("zero")
