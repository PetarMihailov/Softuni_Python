def palindrome(nums):
    nums = nums.split(", ")
    return "\n".join(["True" if num == num[::-1] else "False" for num in nums])


numbers = input()

print(palindrome(numbers))
