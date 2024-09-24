def perfect(n):
    divisors = [num for num in range(1, n+1) if n % num == 0]
    if sum(divisors) / 2 == n:
        return 'We have a perfect number!'
    return 'It\'s not so perfect.'


number = int(input())

print(perfect(number))

