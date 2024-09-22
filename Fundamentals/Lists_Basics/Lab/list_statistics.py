n = int(input())

integers = [int(input()) for el in range(n)]

positives = [el for el in integers if el >= 0]
negatives = [el for el in integers if el < 0]

print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}")
print(f"Sum of negatives: {sum(negatives)}")
