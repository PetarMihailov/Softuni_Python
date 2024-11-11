
n = int(input())  
l = int(input())  

passwords = []

for digit1 in range(1, n+1):  
    for digit2 in range(1, n+1):  
        for letter1 in range(ord('a'), ord('a') + l):  
            for letter2 in range(ord('a'), ord('a') + l): 
                for digit3 in range(max(digit1, digit2) + 1, n + 1): 
                    password = f"{digit1}{digit2}{chr(letter1)}{chr(letter2)}{digit3}"
                    passwords.append(password)

print(" ".join(passwords))
