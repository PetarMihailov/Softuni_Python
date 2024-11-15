a1 = int(input())  
a2 = int(input()) 
n = int(input())  

for symbol1 in range(a1, a2):
    for symbol2 in range(1, n):
        for symbol3 in range(1, n // 2):
            symbol4 = ord(chr(symbol1))
            if symbol1 % 2 != 0 and (symbol2 + symbol3 + symbol4) % 2 != 0:
                ticket = f"{chr(symbol1)}-{symbol2}{symbol3}{symbol4}"
                print(ticket)
