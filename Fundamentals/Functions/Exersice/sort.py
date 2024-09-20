def sort(nums):
    nums = list(map(int, nums.split()))
    nums.sort()
    return nums


numbers = input()

print(sort(numbers))
