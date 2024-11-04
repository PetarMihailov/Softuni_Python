from math import ceil, floor

m = float(input()) * 3.25
z = float(input()) * 4
r = float(input()) * 3.5
c = float(input()) * 8
gift = float(input())

total_price = (m + z + r + c) * 0.95
diff = abs(total_price - gift)

if total_price >= gift:
    print(f"She is left with {floor(diff)} leva.")
else:
    print(f"She will have to borrow {ceil(diff)} leva.")
