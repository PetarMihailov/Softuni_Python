while True:
    num = float(input())
    if 1 <= num <= 100:
        print(f'The number {num} is between 1 and 100')
        break

num = float(input())

while 1 > num or num > 100:
    num = float(input())

print(f'The number {num} is between 1 and 100')

num = float(input())

while not (1 <= num <= 100):
    num = float(input())

print(f'The number {num} is between 1 and 100')