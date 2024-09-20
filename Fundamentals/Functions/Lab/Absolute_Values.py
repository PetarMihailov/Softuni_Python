# values = [abs(float(i)) for i in input().split()]
#
# print(values)


num = input().split()

num_int = []

for el in num:
    num_int.append(float(el))

res = list(map(abs, num_int))

print(res)

#
def absolute(nums):
    return [abs(float(el)) for el in nums.split()]


nums = input()

print(absolute(nums))