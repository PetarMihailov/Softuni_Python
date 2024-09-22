key = int(input())
n = int(input())

message = []

for _ in range(n):
    letter = ord(input()) + key
    message.append(chr(letter))

print("".join(message))
