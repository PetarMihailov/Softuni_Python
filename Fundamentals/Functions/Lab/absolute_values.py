def absolute_values(nums):
    nums = nums.split()
    return [abs(float(num)) for num in nums]

data = input()

print(absolute_values(data))
