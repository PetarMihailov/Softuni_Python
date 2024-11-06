nums = [float(input()) for el in range(int(input()))]

odd_sum = sum([nums[idx] for idx in range(len(nums)) if idx % 2 == 0])

if odd_sum:
    odd_min = f"{min([nums[idx] for idx in range(len(nums)) if odd_sum and idx % 2 == 0]):.2f}"
    odd_max = f"{max([nums[idx] for idx in range(len(nums)) if odd_sum and idx % 2 == 0]):.2f}"
else:
    odd_min = "No"
    odd_max = "No"

even_sum = sum([nums[idx] for idx in range(len(nums)) if not idx % 2 == 0])

if even_sum:
    even_min = f"{min([nums[idx] for idx in range(len(nums)) if not idx % 2 == 0]):.2f}"
    even_max = f"{max([nums[idx] for idx in range(len(nums)) if even_sum and not idx % 2 == 0]):.2f}"
else:
    even_min = "No"
    even_max = "No"

print(f"OddSum={odd_sum:.2f},")
print(f"OddMin={odd_min},")
print(f"OddMax={odd_max},")
print(f"EvenSum={even_sum:.2f},")
print(f"EvenMin={even_min},")
print(f"EvenMax={even_max}")
