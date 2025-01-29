def sorting(nums):
    return sorted([int(num) for num in nums.split()])


numbers = input()

print(sorting(numbers))

# second solution

def sorting(data):
   return sorted(map(int, data.split()))


number = input()

print(sorting(number))
