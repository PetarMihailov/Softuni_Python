def tribonacci_sequence(n):
    if n == 1:
        print(1)
        return
    elif n == 2:
        print("1 1")
        return
    elif n == 3:
        print("1 1 2")
        return

    tribonacci = [1, 1, 2]

    for i in range(3, n):
        next_number = tribonacci[-1] + tribonacci[-2] + tribonacci[-3]
        tribonacci.append(next_number)

    print(" ".join(map(str, tribonacci)))


n = int(input())
tribonacci_sequence(n)
