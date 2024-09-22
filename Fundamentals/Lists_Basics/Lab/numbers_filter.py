n = int(input())

numbers = [int(input()) for _ in range(n)]

command = input()

if command == "even":
    numbers = [num for num in numbers if num % 2 == 0]
elif command == "odd":
    numbers = [num for num in numbers if not num % 2 == 0]
elif command == "negative":
    numbers = [num for num in numbers if num < 0]
elif command == "positive":
    numbers = [num for num in numbers if num >= 0]

print(numbers)
