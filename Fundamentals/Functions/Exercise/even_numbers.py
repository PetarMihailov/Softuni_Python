def even_numbers(nums):
    nums = list(map(int, nums.split()))
    even = list(filter(lambda x: x % 2 == 0, nums))
    return even


numbers = input()

print(even_numbers(numbers))
