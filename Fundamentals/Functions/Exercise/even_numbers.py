def even_numbers(nums):
    nums = list(map(int, nums.split()))
    even = list(filter(lambda x: x % 2 == 0, nums))
    return even


numbers = input()

print(even_numbers(numbers))

# second solution

def even_numbers(data):
    return list(filter(lambda x: x % 2 == 0, map(int, data.split())))


number = input()

print(even_numbers(number))
