def increase_and_decrease(num, nums):
    for idx in range(len(nums)):
        if nums[idx] <= num:
            nums[idx] += num
        else:
            nums[idx] -= num
    return nums


numbers = list(map(int, input().split()))

removed_nums = []

while numbers:
    index = int(input())

    if index < 0:
        value = numbers[0]
        removed_nums.append(value)
        numbers[0] = numbers[-1]
        numbers = increase_and_decrease(value, numbers)
    elif index >= len(numbers):
        value = numbers[-1]
        removed_nums.append(value)
        numbers[-1] = numbers[0]
        numbers = increase_and_decrease(value, numbers)
    else:
        num_to_remove = numbers.pop(index)
        removed_nums.append(num_to_remove)
        numbers = increase_and_decrease(num_to_remove, numbers)


print(sum(removed_nums))
