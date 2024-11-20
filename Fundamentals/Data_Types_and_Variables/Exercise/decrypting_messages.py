key = int(input())
n = int(input())

message = []

for _ in range(n):
    letter = ord(input()) + key
    message.append(chr(letter))

print("".join(message))

# second solutiuon

key = int(input())
lines = int(input())

message = [chr(ord(input())+key) for _ in range(lines)]

print(''.join(message))
