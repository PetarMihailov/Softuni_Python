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

# second solution

lines = int(input())

brackets = []
balanced = True

for _ in range(lines):
    char = input()
    if not char in "(,)":
        continue
    elif char == "(":
        brackets.append(char)
    elif char == ")" and not brackets:
        balanced = False
        break
    elif char == ")" and not brackets.pop() == "(":
        balanced = False
        break

    if len(brackets) > 1:
        balanced = False
        break

if balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
