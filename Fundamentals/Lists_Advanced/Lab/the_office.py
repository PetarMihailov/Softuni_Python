happiness = [int(num) for num in input().split()]
factor = int(input())

happiness = [num * factor for num in happiness]

filtered = [num for num in happiness if num >= (sum(happiness)/len(happiness))]

if len(filtered) >= len(happiness) / 2:
    print(f"Score: {len(filtered)}/{len(happiness)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(happiness)}. Employees are not happy!")
