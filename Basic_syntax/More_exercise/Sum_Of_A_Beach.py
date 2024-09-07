string = input().lower()

words = ["sand", "water", "fish", "sun"]
counter = [string.count(word) for word in words]


print(sum(counter))