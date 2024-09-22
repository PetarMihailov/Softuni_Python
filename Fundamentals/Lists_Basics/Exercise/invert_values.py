text = input()

text_list = text.split()
invert_list = []

for index in text_list:
    element = int(index)
    if element > 0:
        element = -abs(element)
        invert_list.append(element)
    else:
        element = abs(element)
        invert_list.append(element)

print(invert_list)

# second solution

numbers = [int(el)*-1 for el in input().split()]

print(numbers)
