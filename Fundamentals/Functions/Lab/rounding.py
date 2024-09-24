def rounding(nums):
    return [round(float(num)) for num in nums.split()]


numbers = input()

print(rounding(numbers))
