coins = [int(num) for num in input().split(", ")]
beggars = int(input())
count = 0
beggars_list = [0] * beggars

for coin in coins:
    beggars_list[count] += coin
    count += 1
    if count >= beggars:
        count = 0
print(beggars_list)

# second solution

numbers = list(map(int, input().split(", ")))
beggars_count = int(input())

result = [0] * beggars_count


for index in range(len(numbers)):
    beggar_index = index % beggars_count
    result[beggar_index] += numbers[index]

print(result)
