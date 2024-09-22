n = int(input())

brackets = []

for index in range(n):
    line = input()

    if line == "(" or line == ")":
        brackets.append(line)

flag = True

for index in range(0, len(brackets), 2):
    if brackets[index] == "(" and brackets[index+1] == ")":
        continue
    else:
        flag = False
        break

if not flag:
    print("UNBALANCED")
else:
    print("BALANCED")
