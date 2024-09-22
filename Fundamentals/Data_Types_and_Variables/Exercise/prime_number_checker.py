num = int(input())

flag = False

if num == 0 or num == 1:
    flag = True
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break


if flag:
    print("False")
else:
    print("True")
