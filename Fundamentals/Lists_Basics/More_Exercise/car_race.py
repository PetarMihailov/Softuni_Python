def sum_time(nums):
    time = 0
    for num in nums:
        time += num
        if num == 0:
            time *= 0.8
    return time


numbers = [int(el) for el in input().split()]

half = len(numbers) // 2

first = numbers[:half]
second = reversed(numbers[half+1:])

time_first = sum_time(first)
time_second = sum_time(second)

if time_first < time_second:
    print(f"The winner is left with total time: {time_first:.1f}")
else:
    print(f"The winner is right with total time: {time_second:.1f}")
