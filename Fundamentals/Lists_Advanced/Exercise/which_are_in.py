string_1 = input().split(", ")
string_2 = input()

common_elements = [el for el in string_1 if el in string_2]

print(common_elements)
