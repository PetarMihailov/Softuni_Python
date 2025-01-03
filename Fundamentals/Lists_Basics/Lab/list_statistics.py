n = int(input())

integers = [int(input()) for el in range(n)]

positives = [el for el in integers if el >= 0]
negatives = [el for el in integers if el < 0]

print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}")
print(f"Sum of negatives: {sum(negatives)}")

# 

nums = [int(input()) for _ in range(int(input()))]

positives = [num for num in nums if num >= 0]
negatives = [num for num in nums if num < 0]

print(f"{positives}\n{negatives}\nCount of positives: {len(positives)}\nSum of negatives: {sum(negatives)}")


