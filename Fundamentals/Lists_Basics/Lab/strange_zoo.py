tail = input()
body = input()
head = input()

meerkat = [tail, body, head]

meerkat[0], meerkat[2] = meerkat[2], meerkat[0]

print(meerkat)

# 

zoo = [input(), input(), input()]

zoo[0], zoo[2] = zoo[2], zoo[0]

print(zoo)
