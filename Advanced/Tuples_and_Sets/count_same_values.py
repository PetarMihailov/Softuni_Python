numbers = list(map(float, input().split()))

counts = {key: numbers.count(key) for key in numbers}

print('\n'.join([f"{data[0]} - {data[1]} times" for data in counts.items()]))
