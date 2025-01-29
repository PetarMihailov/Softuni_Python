def palindrome(nums):
    nums = nums.split(", ")
    return "\n".join(["True" if num == num[::-1] else "False" for num in nums])


numbers = input()

print(palindrome(numbers))

# second solution

def palindrome(word):
    return "True" if word == word[::-1] else "False"


data = input()

print("\n".join(map(palindrome, data.split(", "))))
