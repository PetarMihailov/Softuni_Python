def min_max_sum(nums):
    nums = list(map(int, nums.split()))
    maximum, minimum, result = max(nums), min(nums), sum(nums)
    return f"The minimum number is {minimum}\nThe maximum number" \
           f" is {maximum}\nThe sum number is: {result}"


numbers = input()

print(min_max_sum(numbers))
